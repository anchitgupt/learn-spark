"""Check generated links, fragments, source metadata, and Python example syntax."""
import ast
import json
import re
from datetime import date
from html import escape, unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from chapters import CHAPTER_GROUPS, COLLECTIONS, QUESTION_TYPES

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / '_site'

# Versioned Spark documentation and source, plus the official documentation of the
# sibling Apache format/table projects and Delta Lake that this site cites for storage topics.
APPROVED_DOC_PREFIXES = (
    'spark.apache.org/docs/',
    'github.com/apache/spark/blob/v3.5.7/',
    'parquet.apache.org/',
    'orc.apache.org/',
    'avro.apache.org/',
    'iceberg.apache.org/',
    'hudi.apache.org/',
    'docs.delta.io/',
    'github.com/delta-io/delta/blob/v3.2.1/',
)
BASELINE = 'Apache Spark 3.5.7'
PYTHON_BLOCK = re.compile(r'<div class="code-block"><div><span>PYTHON / PYSPARK</span>.*?<pre[^>]*><code>(.*?)</code></pre>', re.S)


def approved_source(url):
    split = urlsplit(url)
    combined = split.netloc + split.path
    return split.scheme == 'https' and any(combined.startswith(prefix) for prefix in APPROVED_DOC_PREFIXES)


def runtime_note(text):
    """A recorded run names the runtime and an ISO date."""
    return 'PySpark 3.5.7' in text and re.search(r'\b\d{4}-\d{2}-\d{2}\b', text)


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.ids = set()
        self.links = []
        self.h1 = 0
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'h1':
            self.h1 += 1
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, 'Duplicate id: ' + attrs['id']
            self.ids.add(attrs['id'])
        for key in ['href', 'src', 'poster']:
            if key in attrs:
                self.links.append(attrs[key])
        if tag == 'img':
            assert 'alt' in attrs, 'Missing image alt text'


pages = {p.name: Page(p) for p in OUT.glob('*.html')}
lessons = json.loads((ROOT / 'content/lessons.json').read_text())
assert len(pages) == len(lessons) + 5, 'Build all lesson and collection pages first'
checks = 0
for filename, page in pages.items():
    assert page.h1 == 1, filename + ': expected one h1'
    for link in page.links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            continue
        assert not url.path.startswith('/'), 'Root-relative link breaks project Pages: ' + link
        target = unquote(url.path) or filename
        assert (OUT / target).is_file(), filename + ': missing ' + target
        if url.fragment and target in pages:
            assert unquote(url.fragment) in pages[target].ids, filename + ': missing anchor ' + link
        checks += 1
slugs = [l['slug'] for l in lessons]
assert len(set(slugs)) == len(slugs)
python_blocks = 0
for lesson in lessons:
    assert lesson['sources'] and lesson['reviewed'] and lesson['version']
    assert lesson.get('chapter') in CHAPTER_GROUPS, lesson['slug'] + ': needs a known chapter label'
    assert all(approved_source(s['url']) for s in lesson['sources']), lesson['slug'] + ': use versioned official documentation or Spark source'
    assert len({s['id'] for s in lesson['sources'] if 'id' in s}) == len([s for s in lesson['sources'] if 'id' in s]), lesson['slug'] + ': duplicate source id'
    ast.parse(lesson['code'])
    html = (OUT / (lesson['slug'] + '.html')).read_text()
    assert escape(lesson['chapter']) + ' / LESSON' in html, lesson['slug'] + ': eyebrow must name its chapter'
    if 'diagram' in lesson:
        figure = lesson['diagram']
        assert figure.get('alt', '').strip() and figure.get('caption', '').strip(), lesson['slug'] + ': diagrams need alt text and a caption'
        assert (ROOT / figure['src']).is_file() and figure['src'].startswith('assets/'), lesson['slug'] + ': diagram must be a repository asset'
    if 'runtime' in lesson:
        assert runtime_note(lesson['runtime']), lesson['slug'] + ': runtime notes name PySpark 3.5.7 and the run date'
    # Every block labeled Python on a lesson page must at least parse.
    for block in PYTHON_BLOCK.findall(html):
        ast.parse(unescape(block))
        python_blocks += 1
questions = json.loads((ROOT / 'content/questions.json').read_text())
predictions = json.loads((ROOT / 'content/predictions.json').read_text())
question_topics = json.loads((ROOT / 'content/question-topics.json').read_text())
assert not set(question_topics) & set(slugs), 'question-topics.json labels must not shadow lesson slugs'
exercises = {item['id']: item for item in predictions}
questions_page = (OUT / 'questions.html').read_text()
assert len(set(q['id'] for q in questions)) == len(questions)
assert all(re.fullmatch(r'[a-z0-9-]+', q['id']) for q in questions)
for q in questions:
    assert (q['topic'] in slugs or q['topic'] in question_topics) and q['source'], q['id'] + ': needs a known topic and a source'
    assert q.get('origin') in ('reported', 'practice'), q['id'] + ': origin must be "reported" or "practice"'
    assert q.get('type') in QUESTION_TYPES, q['id'] + ': unknown question type'
    if 'collection' in q:
        assert q['collection'] in COLLECTIONS, q['id'] + ': unknown collection'
    if 'inspiration' in q:
        assert q['origin'] == 'practice', q['id'] + ': an online topic list is not a reported interview'
        inspiration = q['inspiration']
        url = urlsplit(inspiration['url'])
        assert inspiration['title'].strip() and url.scheme == 'https' and url.netloc, q['id'] + ': needs a named HTTPS inspiration link'
        assert q.get('references'), q['id'] + ': web-inspired questions need technical references'
    if 'references' in q:
        assert q['references'] and q.get('version', '').startswith(BASELINE), q['id'] + ': references need the Spark baseline'
        assert date.fromisoformat(q['reviewed']).isoformat() == q['reviewed'], q['id'] + ': needs an ISO review date'
        for ref in q['references']:
            assert ref['title'].strip() and approved_source(ref['url']), q['id'] + ': use named, versioned official references'
    if 'runtime' in q:
        assert runtime_note(q['runtime']), q['id'] + ': runtime notes name PySpark 3.5.7 and the run date'
    if 'exercise' in q:
        # Exercise-linked questions take the exercise's spoken answer and follow-up at build time.
        assert q['exercise'] in exercises and 'answer' not in q and 'followup' not in q, q['id'] + ': reference one known exercise instead of copying its answer'
        exercise = exercises[q['exercise']]
        assert escape(exercise['spoken']) in questions_page and escape(exercise['followup']) in questions_page, q['id'] + ': card must show its exercise answer and follow-up'
    else:
        assert q.get('answer') and q.get('followup'), q['id'] + ': needs an answer and follow-up'
        assert all(q['answer'] != item['spoken'] for item in predictions), q['id'] + ': copies an exercise answer; reference it with "exercise"'
assert all('qa-' + q['id'] in pages['qa.html'].ids for q in questions), 'the Q&A sheet must include every question'
guide = json.loads((ROOT / 'content/senior-interview-guide.json').read_text())
guide_ids = []
known_ids = {q['id'] for q in questions}
for group in guide:
    assert group.get('title') and group.get('items'), 'senior guide: groups need a title and items'
    for item in group['items']:
        assert item.get('prompt') and item.get('question'), 'senior guide: items need a prompt and question'
        assert item['question'] in known_ids, 'senior guide: unknown question ' + item['question']
        guide_ids.append(item['question'])
senior = [q['id'] for q in questions if q.get('collection') == 'senior-de']
assert set(senior) <= set(guide_ids), 'senior guide must index every senior-de question: ' + ', '.join(sorted(set(senior) - set(guide_ids)))
assert f'{len(guide_ids)} prompts in {len(guide)} groups' in questions_page, 'questions page must show the senior guide prompt count'
for item in json.loads((OUT / 'search.json').read_text()):
    assert not re.search(r'<[a-zA-Z/][^>]*>|&(?:[a-zA-Z]+|#\d+);', item['title'] + ' ' + item['text']), item['url'] + ': search text contains HTML markup'
    target = urlsplit(item['url'])
    assert (OUT / target.path).is_file()
    if target.fragment:
        assert target.fragment in pages[target.path].ids
phases = json.loads((ROOT / 'content/execution-phases.json').read_text())
assert phases
for phase in phases:
    assert all(phase.get(k) for k in ['title', 'owner', 'state', 'detail', 'data', 'evidence', 'anchor'])
    assert phase['anchor'] in pages['execution-flow.html'].ids
prediction_ids = [item['id'] for item in predictions]
assert len(set(prediction_ids)) == len(prediction_ids)
assert all(re.fullmatch(r'[a-z0-9-]+', item) for item in prediction_ids)
referenced = [item for lesson in lessons for item in lesson.get('exercises', [])]
assert sorted(referenced) == sorted(prediction_ids), 'Each exercise must be referenced once'
exercise_page = {item: lesson['slug'] + '.html' for lesson in lessons for item in lesson.get('exercises', [])}
for exercise in predictions:
    assert all(exercise.get(key) for key in ['title', 'intro', 'code', 'prompts', 'flow', 'reasoning', 'output', 'verify_code', 'evidence', 'spoken', 'followup', 'followup_answer', 'sources'])
    assert all(step.get('label') and step.get('detail') for step in exercise['flow'])
    assert 'observed' not in exercise or ('PySpark 3.5.7' in exercise['observed']), exercise['id'] + ': observed counts must name the runtime'
    ast.parse(exercise['code'])
    ast.parse(exercise['verify_code'])
    target = pages[exercise_page[exercise['id']]]
    assert exercise['id'] in target.ids
    assert all('source-' + source in target.ids for source in exercise['sources'])
print(f'PASS: {len(pages)} pages, {checks} local links/assets, {len(lessons)} lesson schemas/examples, {python_blocks} Python blocks, {len(questions)} questions, {len(predictions)} exercises.')
