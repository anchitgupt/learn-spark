#!/usr/bin/env python3
"""Optional local browser checks for Spark Fieldnotes. Not part of CI.

Serves the generated `_site` build on an ephemeral port and drives a headless
browser through the interactive behaviour: completion progress, answer
disclosures, search, the notebook (add/edit/export/import), question filters,
mobile navigation, the execution walkthrough, the visual lab, the
no-JavaScript fallbacks, and responsive overflow.

Usage:
    python3 scripts/build.py              # build the site first
    python3 scripts/browser_test.py       # starts its own HTTP server
    python3 scripts/browser_test.py --headed
    python3 scripts/browser_test.py --url https://anchitgupt.github.io/learn-spark/

One-time setup (or rely on an installed Chrome via the launch fallback):
    python3 -m pip install playwright
    python3 -m playwright install chromium

GitHub Actions deliberately runs content, link, and JavaScript syntax checks
only; run this script locally before publishing interactive changes.
"""
import argparse
import contextlib
import functools
import http.server
import json
import sys
import tempfile
import threading
import time
from contextlib import contextmanager
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / '_site'
WIDTHS = [320, 390, 768, 1280]

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print('Playwright is not installed. Run:')
    print('  python3 -m pip install playwright && python3 -m playwright install chromium')
    sys.exit(2)


class Report:
    def __init__(self):
        self.passed = 0
        self.failures = []

    def check(self, name, ok, detail=''):
        if ok:
            self.passed += 1
            print(f'  ok  {name}')
        else:
            self.failures.append(f'{name} — {detail}' if detail else name)
            print(f'FAIL  {name}' + (f' — {detail}' if detail else ''))

    def section(self, title):
        print(f'\n== {title}')

    def summary(self):
        total = self.passed + len(self.failures)
        if self.failures:
            print(f'\nFAIL: {len(self.failures)} of {total} browser checks failed:')
            for item in self.failures:
                print('  -', item)
            return 1
        print(f'\nPASS: {total} browser checks passed.')
        return 0


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


@contextmanager
def serve_site():
    handler = functools.partial(QuietHandler, directory=str(OUT))
    httpd = http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    try:
        yield f'http://127.0.0.1:{httpd.server_address[1]}'
    finally:
        httpd.shutdown()
        thread.join(timeout=5)


def launch(browser_type, headed):
    options = {'headless': not headed}
    try:
        return browser_type.launch(**options)
    except Exception as first_error:
        try:
            return browser_type.launch(channel='chrome', **options)
        except Exception:
            print('No Chromium available for Playwright. Run: python3 -m playwright install chromium')
            raise first_error


def track(page, bucket):
    page.on('pageerror', lambda error: bucket.append(str(error)))
    page.on('console', lambda message: bucket.append(message.text) if message.type == 'error' else None)


def storage(page):
    raw = page.evaluate("localStorage.getItem('spark-fieldnotes-v1')")
    return json.loads(raw) if raw else None


def wait_toast(page, text, timeout=5000):
    try:
        page.wait_for_function(
            "text => { const t = document.querySelector('#toast');"
            " return t.classList.contains('visible') && t.textContent.includes(text); }",
            arg=text, timeout=timeout,
        )
        return True
    except Exception:
        return False


def run_checks(browser, base, report, lessons, pages, exercises, questions):
    slugs = [lesson['slug'] for lesson in lessons]
    last = slugs[-1]
    predict_ids = next(l for l in lessons if l['slug'] == 'predict-execution')['exercises']
    predict = [item for item in exercises if item['id'] in predict_ids]
    check = report.check
    url = lambda name: f'{base}/{name}'

    # ---------- load every page ----------
    report.section('Pages load')
    desktop = browser.new_context(viewport={'width': 1280, 'height': 900}, reduced_motion='reduce')
    desktop.grant_permissions(['clipboard-read', 'clipboard-write'], origin=base)
    page = desktop.new_page()
    errors = []
    track(page, errors)
    bad = []
    for name in pages:
        response = page.goto(url(name), wait_until='load')
        if response is None or response.status >= 400:
            bad.append(f'{name}:{response.status if response else "no response"}')
    check(f'all {len(pages)} pages load with HTTP 200', not bad, ', '.join(bad))

    # ---------- completion progress ----------
    report.section('Completion progress')
    page.goto(url('index.html'))
    page.evaluate("localStorage.removeItem('spark-fieldnotes-v1')")
    page.reload()
    check(f'fresh visit shows 0 / {len(slugs)}', page.locator('#progress-count').text_content().strip() == f'0 / {len(slugs)}')

    seed = json.dumps({'version': 1, 'completed': slugs[:-1], 'notes': []})
    page.evaluate("value => localStorage.setItem('spark-fieldnotes-v1', value)", seed)
    page.reload()
    expected = f'{len(slugs) - 1} / {len(slugs)}'
    check(f'{len(slugs) - 1} saved lessons show {expected}', page.locator('#progress-count').text_content().strip() == expected)

    resume = page.locator('#resume-learning')
    check('resume link targets the next lesson',
          resume.get_attribute('href') == f'{last}.html' and 'Continue' in resume.text_content())

    page.goto(url(f'{last}.html'))
    button = page.locator('.complete-button')
    toggle = lambda: button.get_attribute('aria-pressed')
    check('lesson starts unmarked', toggle() == 'false')
    button.click()
    check('marking a lesson updates the button and toast',
          toggle() == 'true' and wait_toast(page, 'Reading progress updated.'))
    check('marking a lesson persists to storage',
          last in (storage(page) or {}).get('completed', []))
    page.reload()
    check('marked lesson survives a reload', page.locator('.complete-button').get_attribute('aria-pressed') == 'true')
    page.locator('.complete-button').click()
    check('unmarking a lesson restores the count',
          page.locator('.complete-button').get_attribute('aria-pressed') == 'false'
          and len((storage(page) or {}).get('completed', [])) == len(slugs) - 1)

    # ---------- answer disclosures ----------
    report.section('Prediction disclosures')
    page.goto(url('predict-execution.html'))
    check('three exercises are present', page.locator('section.prediction-exercise').count() == len(predict))
    flow_ok = all(page.locator(f"#{item['id']} .prediction-flow li").count() == len(item['flow']) for item in predict)
    check('flow steps match the content', flow_ok)
    output_ok = all(
        item['output'].strip() in page.locator(f"#{item['id']} .expected p").first.text_content()
        for item in predict
    )
    check('expected results match the content', output_ok)
    page.locator('#filter-count details.prediction-answer > summary').click()
    check('mouse opens a reasoning disclosure',
          page.locator('#filter-count details.prediction-answer').evaluate('d => d.open'))
    page.locator('#groupby-write details.prediction-answer > summary').focus()
    page.keyboard.press('Enter')
    check('keyboard opens a reasoning disclosure',
          page.locator('#groupby-write details.prediction-answer').evaluate('d => d.open'))
    page.locator('#filter-count details.followup-answer > summary').click()
    check('follow-up disclosure opens too',
          page.locator('#filter-count details.followup-answer').evaluate('d => d.open'))

    # ---------- copy button ----------
    report.section('Copy button')
    code_text = page.locator('#filter-count .code-block code').first.text_content()
    page.locator('#filter-count .copy-code').first.click()
    copied = page.evaluate('navigator.clipboard.readText()')
    check('copy button copies the snippet exactly', copied == code_text,
          f'copied {len(copied or "")} of {len(code_text)} chars')
    check('copy button confirms with a toast', wait_toast(page, 'Code copied.'))

    # ---------- search ----------
    report.section('Search')
    page.goto(url('index.html'))
    page.click('#open-search')
    dialog_open = page.locator('#search-dialog').evaluate('d => d.open')
    focused = page.evaluate("document.activeElement && document.activeElement.id")
    check('search opens with focus in the input', dialog_open and focused == 'site-search')
    try:
        page.wait_for_selector('#search-results a', timeout=5000)
    except Exception:
        pass
    check('search index loads results', page.locator('#search-results a').count() > 0)
    page.fill('#site-search', 'groupby')
    page.wait_for_selector('#search-results a')
    hrefs = page.eval_on_selector_all('#search-results a', 'els => els.map(e => e.getAttribute("href"))')
    check('search finds the groupBy exercise', any('predict-execution.html#groupby-write' in h for h in hrefs), ', '.join(hrefs[:3]))
    page.fill('#site-search', 'dictionary encoding')
    page.wait_for_selector('#search-results a')
    hrefs = page.eval_on_selector_all('#search-results a', 'els => els.map(e => e.getAttribute("href"))')
    check('search finds the file-format question', any('questions.html#format-dictionary' in h for h in hrefs), ', '.join(hrefs[:3]))
    page.keyboard.press('Escape')
    check('Escape closes search', not page.locator('#search-dialog').evaluate('d => d.open'))
    page.keyboard.press('Control+k')
    opened = page.locator('#search-dialog').evaluate('d => d.open')
    page.keyboard.press('Control+k')
    check('Ctrl+K toggles search', opened and not page.locator('#search-dialog').evaluate('d => d.open'))
    page.click('#open-search')
    page.fill('#site-search', 'zzzz not a thing')
    page.wait_for_selector('#search-results p')
    check('empty search explains itself', 'No matches' in page.locator('#search-results p').text_content())
    page.click('[data-close-dialog]')
    check('close button dismisses search', not page.locator('#search-dialog').evaluate('d => d.open'))

    # ---------- question bank ----------
    report.section('Question bank')
    scenario_count = sum(1 for q in questions if q['type'] == 'Scenario')
    page.goto(url('questions.html'))
    visible = lambda: page.evaluate("document.querySelectorAll('.question-card:not([hidden])').length")
    check(f'all {len(questions)} questions render', page.locator('.question-card').count() == len(questions)
          and page.locator('#question-count').text_content().strip() == f'{len(questions)} questions')
    page.click('[data-filter="Scenario"]')
    check(f'Scenario filter shows {scenario_count} questions', visible() == scenario_count
          and page.locator('#question-count').text_content().strip() == f'{scenario_count} questions'
          and page.locator('[data-filter="Scenario"]').get_attribute('aria-pressed') == 'true')
    for kind in sorted({q['type'] for q in questions} - {'Scenario'}):
        kind_count = sum(1 for q in questions if q['type'] == kind)
        page.click(f'[data-filter="{kind}"]')
        check(f'{kind} filter shows {kind_count} questions', visible() == kind_count)
    page.click('[data-filter="All"]')
    check('All filter restores every question', visible() == len(questions))
    page.fill('#question-search', 'coalesce(1)')
    check('text filter finds the coalesce(1) question',
          page.locator('#practice-partitions-shuffles').is_visible() and visible() == 1)
    page.fill('#question-search', 'salting')
    check('text filter finds the new salting question',
          page.locator('#senior-salting').is_visible())
    page.fill('#question-search', 'zzzz')
    check('no-match state appears when filtering', page.locator('#no-questions').is_visible())
    page.fill('#question-search', '')
    page.locator('#practice-what-is-spark details.answer > summary').click()
    check('question answer reveals by mouse',
          page.locator('#practice-what-is-spark details.answer').evaluate('d => d.open'))

    web_questions = [q for q in questions if q.get('inspiration')]
    citation_errors = []
    for q in web_questions:
        card = page.locator(f'#{q["id"]}')
        card.locator('details').evaluate('d => { d.open = true; }')
        expected_links = [q['inspiration']] + q['references']
        actual_links = card.locator('details a').evaluate_all(
            'links => links.map(a => ({title: a.textContent, url: a.getAttribute("href")}))')
        if (len(actual_links) != len(expected_links)
                or any(actual['url'] != expected['url'] or expected['title'] not in actual['title']
                       for actual, expected in zip(actual_links, expected_links))
                or card.locator('.question-origin').text_content() != 'Web-inspired practice'
                or q['reviewed'] not in card.locator('details').text_content()
                or q['version'] not in card.locator('details').text_content()
                or 'not runtime-tested' not in card.locator('details').text_content()):
            citation_errors.append(q['id'])
    check('web-inspired questions show their own attribution, references, and review scope',
          bool(web_questions) and not citation_errors, ', '.join(citation_errors))
    page.fill('#question-search', 'unionByName')
    check('new unionByName question is searchable',
          page.locator('#web-union-by-name').is_visible() and visible() == 1)
    page.fill('#question-search', '')

    # ---------- storage formats lesson ----------
    report.section('Storage formats lesson')
    page.goto(url('storage-formats.html'))
    check('the Parquet layout diagram renders',
          page.locator('figure.architecture img[src="assets/parquet-layout.svg"]').is_visible())
    diagram_box = page.locator('figure.architecture img[src="assets/parquet-layout.svg"]').bounding_box()
    check('the diagram has a rendered size', bool(diagram_box) and diagram_box['width'] > 0)
    page.locator('#explain-back details.answer > summary').click()
    check('the storage explain-back disclosure opens',
          page.locator('#explain-back details.answer').evaluate('d => d.open'))

    # ---------- lesson figures, runtime notes, and exercise lessons ----------
    report.section('Lesson figures and recorded runs')
    missing_figures, missing_runtime, exercise_errors = [], [], []
    by_id = {item['id']: item for item in exercises}
    for lesson in lessons:
        if not (lesson.get('diagram') or lesson.get('runtime') or lesson.get('exercises')):
            continue
        page.goto(url(f"{lesson['slug']}.html"))
        if lesson.get('diagram'):
            image = page.locator(f"figure.architecture img[src=\"{lesson['diagram']['src']}\"]")
            box = image.bounding_box() if image.count() == 1 else None
            natural = image.evaluate('img => img.naturalWidth') if image.count() == 1 else 0
            if not (box and box['width'] > 0 and natural > 0):
                missing_figures.append(lesson['slug'])
        if lesson.get('runtime') and lesson['runtime'] not in (page.locator('#try-it .runtime-note').text_content() or ''):
            missing_runtime.append(lesson['slug'])
        for exercise_id in lesson.get('exercises', []):
            section = page.locator(f'#{exercise_id}')
            section.locator('details.prediction-answer').evaluate('d => { d.open = true; }')
            observed = by_id[exercise_id].get('observed')
            if section.count() != 1 or (observed and observed.strip() not in section.locator('.expected').last.text_content()):
                exercise_errors.append(exercise_id)
    check('every lesson diagram loads with a rendered size', not missing_figures, ', '.join(missing_figures))
    check('runtime-verified lessons show their recorded run', not missing_runtime, ', '.join(missing_runtime))
    check('exercise lessons render every exercise and its observed counts', not exercise_errors, ', '.join(exercise_errors))

    # ---------- senior DE guide ----------
    report.section('Senior DE guide')
    guide_data = json.loads((ROOT / 'content/senior-interview-guide.json').read_text())
    guide_items = sum(len(group['items']) for group in guide_data)
    page.goto(url('questions.html'))
    senior = page.locator('#senior-de')
    check('the senior bank guide renders with its prompt count',
          senior.count() == 1 and f'{guide_items} prompts in {len(guide_data)} groups' in senior.locator('summary').first.text_content())
    senior.locator('summary').first.click()
    check('the guide lists every group', senior.locator(':scope > details').count() == len(guide_data))
    check(f'the guide lists all {guide_items} prompt links', senior.locator('ol a').count() == guide_items)
    senior.locator(':scope > details').first.locator('summary').click()
    senior.locator('ol a').first.click()
    check('a guide prompt link reaches its question card',
          page.url.endswith('#flow-reported') and page.locator('#flow-reported').count() == 1)

    # ---------- notebook ----------
    report.section('Notebook')
    page.goto(url('notebook.html'))
    options = page.eval_on_selector_all('#note-topic option', 'els => els.map(e => e.value)')
    check('every lesson is a notebook topic', len(options) == len(slugs) and 'predict-execution' in options)
    page.fill('#note-question', 'Can a broadcast join still shuffle?')
    page.select_option('#note-topic', 'predict-execution')
    page.fill('#note-answer', 'Check the Exchange operators in the physical plan first.')
    page.click('#question-form button[type="submit"]')
    check('saving a note shows it in the list and storage',
          page.locator('#notes-count').text_content().strip() == '1 saved'
          and (storage(page) or {}).get('notes', [])[0]['question'] == 'Can a broadcast join still shuffle?')
    page.reload()
    check('notes survive a reload', page.locator('#notes-count').text_content().strip() == '1 saved'
          and page.locator('.note-card h3').first.text_content() == 'Can a broadcast join still shuffle?')
    page.locator('.note-card button:has-text("Edit")').first.click()
    check('edit loads the note into the form', page.locator('#form-title').text_content() == 'Edit your question')
    page.fill('#note-question', 'Can a broadcast join still shuffle? (edited)')
    page.click('#question-form button[type="submit"]')
    check('editing updates the saved note',
          page.locator('.note-card h3').first.text_content() == 'Can a broadcast join still shuffle? (edited)')

    tmpdir = Path(tempfile.mkdtemp(prefix='spark-fieldnotes-'))
    with page.expect_download() as download_info:
        page.click('#export-notes')
    export_path = tmpdir / 'export.json'
    download_info.value.save_as(str(export_path))
    exported = json.loads(export_path.read_text())
    check('export downloads a valid notebook',
          exported.get('version') == 1 and len(exported.get('notes', [])) == 1
          and isinstance(exported.get('completed'), list))

    page.once('dialog', lambda dialog: dialog.accept())
    page.locator('.note-card button:has-text("Delete")').first.click()
    page.wait_for_function("document.querySelector('#notes-count').textContent.trim() === '0 saved'")
    check('deleting a note (with confirmation) empties the list', True)
    page.set_input_files('#import-notes', str(export_path))
    page.wait_for_function("document.querySelector('#notes-count').textContent.trim() === '1 saved'")
    check('import restores the exported note', True)
    page.set_input_files('#import-notes', str(export_path))
    check('re-importing skips duplicates', wait_toast(page, 'Duplicates skipped.')
          and page.locator('#notes-count').text_content().strip() == '1 saved')
    invalid_path = tmpdir / 'invalid.json'
    invalid_path.write_text('{ not json')
    page.set_input_files('#import-notes', str(invalid_path))
    check('invalid import is rejected', wait_toast(page, 'Invalid JSON')
          and page.locator('#notes-count').text_content().strip() == '1 saved')

    # ---------- execution walkthrough ----------
    report.section('Execution walkthrough')
    page.goto(url('execution-flow.html'))
    hidden = lambda: page.evaluate("[...document.querySelectorAll('[data-flow-panel]')].map(p => p.hidden)")
    check('six phases render with the first selected', hidden() == [False, True, True, True, True, True]
          and 'Phase 1 of 6' in page.locator('#flow-status').text_content())
    check('previous is disabled on the first phase', page.locator('#flow-prev').is_disabled())
    page.click('[data-flow-select="2"]')
    check('selecting a phase shows only that panel',
          hidden() == [True, True, False, True, True, True]
          and page.locator('[data-flow-select="2"]').get_attribute('aria-pressed') == 'true')
    page.click('#flow-next')
    check('next advances the phase and status', 'Phase 4 of 6' in page.locator('#flow-status').text_content())
    page.click('[data-flow-select="5"]')
    check('next is disabled on the last phase', page.locator('#flow-next').is_disabled())
    page.locator('[data-flow-select="3"]').focus()
    page.keyboard.press('Enter')
    check('keyboard selects a phase', hidden()[3] is False)

    # ---------- visual lab ----------
    report.section('Visual lab')
    page.goto(url('lab.html'))
    step = lambda: page.locator('#lab-step-label').text_content().strip()
    check('lab starts at step 1', step() == 'STEP 1 / 4')
    page.click('#lab-step')
    check('step control advances the walkthrough', step() == 'STEP 2 / 4'
          and 'Group by city' in page.locator('#lab-description').text_content())
    page.click('#lab-reset')
    check('reset returns to step 1', step() == 'STEP 1 / 4')
    page.select_option('#lab-mode', 'filter')
    page.click('#lab-step')
    check('filter mode explains local work', 'Filter to Pune' in page.locator('#lab-description').text_content())
    page.click('#lab-play')
    playing = page.locator('#lab-play').text_content().strip()
    page.click('#lab-play')
    check('play toggles to pause and back', playing == 'Pause walkthrough'
          and page.locator('#lab-play').text_content().strip() == 'Play walkthrough')
    check('canvas has a rendered size', page.locator('#shuffle-canvas').bounding_box()['width'] > 0)

    # ---------- mobile navigation ----------
    report.section('Mobile navigation')
    mobile = browser.new_context(viewport={'width': 390, 'height': 844}, reduced_motion='reduce')
    mobile_errors = []
    mpage = mobile.new_page()
    track(mpage, mobile_errors)
    mpage.goto(url('index.html'))
    check('sidebar is inert at phone width', mpage.evaluate("document.querySelector('#sidebar').inert") is True)
    mpage.click('.mobile-toggle')
    check('menu opens with focus on the first link',
          mpage.locator('.mobile-toggle').get_attribute('aria-expanded') == 'true'
          and mpage.evaluate("document.querySelector('#sidebar').classList.contains('open')")
          and mpage.evaluate("document.querySelector('.scrim').hidden === false")
          and mpage.evaluate("document.querySelector('#sidebar').contains(document.activeElement)"))
    mpage.keyboard.press('Escape')
    check('Escape closes the menu and restores focus',
          mpage.evaluate("document.querySelector('.mobile-toggle').getAttribute('aria-expanded') === 'false'")
          and mpage.evaluate("document.activeElement === document.querySelector('.mobile-toggle')"))
    mpage.click('.mobile-toggle')
    mpage.click('#sidebar a[href="what-is-spark.html"]')
    mpage.wait_for_url('**/what-is-spark.html')
    check('menu link navigates to the lesson', 'What is Apache Spark' in mpage.title())

    # ---------- no JavaScript ----------
    report.section('No-JavaScript pass (390 px)')
    nojs = browser.new_context(java_script_enabled=False, viewport={'width': 390, 'height': 844})
    npage = nojs.new_page()
    npage.goto(url('what-is-spark.html'))
    display = lambda sel: npage.eval_on_selector(sel, 'el => getComputedStyle(el).display')
    check('lesson text and answers remain readable',
          npage.locator('h1').first.is_visible() and npage.locator('#explain-back details').is_visible()
          and display('.complete-button') == 'none')
    npage.goto(url('index.html'))
    check('interactive chrome hides itself', display('.search-trigger') == 'none')
    npage.goto(url('notebook.html'))
    check('notebook explains the JavaScript requirement',
          'needs JavaScript to save and edit notes' in npage.content())
    npage.goto(url('questions.html'))
    cards = npage.evaluate("document.querySelectorAll('.question-card:not([hidden])').length")
    check('question cards remain visible without JavaScript', cards == len(questions))
    npage.locator('#web-checkpoint-vs-cache summary').click()
    check('new question references are accessible without JavaScript',
          npage.locator('#web-checkpoint-vs-cache .question-references a').first.is_visible())

    # ---------- responsive overflow ----------
    report.section('Responsive overflow (disclosures open)')
    for width in WIDTHS:
        page.set_viewport_size({'width': width, 'height': 900})
        overflowing = []
        for name in pages:
            page.goto(url(name), wait_until='load')
            page.evaluate("document.querySelectorAll('details').forEach(d => { d.open = true; })")
            if page.evaluate('document.documentElement.scrollWidth') > page.evaluate('document.documentElement.clientWidth') + 1:
                overflowing.append(name)
        check(f'no horizontal overflow at {width} px', not overflowing, ', '.join(overflowing))

    # ---------- error logs ----------
    report.section('JavaScript errors')
    check('no JavaScript errors (desktop)', not errors, '; '.join(errors[:3]))
    check('no JavaScript errors (mobile)', not mobile_errors, '; '.join(mobile_errors[:3]))

    desktop.close()
    mobile.close()
    nojs.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--headed', action='store_true', help='show the browser window')
    parser.add_argument('--url', help='test a running site instead of serving _site')
    options = parser.parse_args()

    if not options.url and not (OUT / 'index.html').is_file():
        print('Build the site first: python3 scripts/build.py')
        return 2

    lessons = json.loads((ROOT / 'content/lessons.json').read_text())
    questions = json.loads((ROOT / 'content/questions.json').read_text())
    exercises = json.loads((ROOT / 'content/predictions.json').read_text())
    pages = ['index.html'] + [f"{lesson['slug']}.html" for lesson in lessons] + ['lab.html', 'questions.html', 'notebook.html']

    report = Report()
    started = time.time()
    site = contextlib.nullcontext(options.url.rstrip('/')) if options.url else serve_site()
    with site as base:
        print(f'Serving checks against {base}')
        with sync_playwright() as playwright:
            browser = launch(playwright.chromium, options.headed)
            try:
                run_checks(browser, base, report, lessons, pages, exercises, questions)
            except Exception as error:
                report.failures.append(f'aborted: {error}')
                print(f'\nABORTED: {error}')
            finally:
                browser.close()
    code = report.summary()
    print(f'{time.time() - started:.1f}s')
    return code


if __name__ == '__main__':
    sys.exit(main())
