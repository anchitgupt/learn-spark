"""Check generated links, fragments, source metadata, and Python example syntax."""
import ast
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / '_site'


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.ids = set()
        self.links = []
        self.h1 = 0
        self.code_blocks = []
        self.in_code = False
        self.in_pre = False
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'pre':
            self.in_pre = True
        if tag == 'code' and self.in_pre:
            self.in_code = True
            self.code_blocks.append('')
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

    def handle_endtag(self, tag):
        if tag == 'code':
            self.in_code = False
        if tag == 'pre':
            self.in_pre = False

    def handle_data(self, data):
        if self.in_code:
            self.code_blocks[-1] += data


pages = {p.name: Page(p) for p in OUT.glob('*.html')}
lessons = json.loads((ROOT / 'content/lessons.json').read_text())
assert len(pages) == len(lessons) + 4, 'Build all lesson and collection pages first'
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
for lesson in lessons:
    assert lesson['sources'] and lesson['reviewed'] and lesson['version']
    assert all(s['url'].startswith((
        'https://spark.apache.org/docs/',
        'https://github.com/apache/spark/blob/v3.5.7/',
    )) for s in lesson['sources']), 'Use versioned official documentation or Spark source'
    ast.parse(lesson['code'])
questions = json.loads((ROOT / 'content/questions.json').read_text())
assert len(set(q['id'] for q in questions)) == len(questions)
assert all(re.fullmatch(r'[a-z0-9-]+', q['id']) for q in questions)
assert all(q['topic'] in slugs and q['answer'] and q['source'] for q in questions)
for item in json.loads((OUT / 'search.json').read_text()):
    target = urlsplit(item['url'])
    assert (OUT / target.path).is_file()
    if target.fragment:
        assert target.fragment in pages[target.path].ids
phases = json.loads((ROOT / 'content/execution-phases.json').read_text())
assert phases
for phase in phases:
    assert all(phase.get(k) for k in ['title', 'owner', 'state', 'detail', 'data', 'evidence', 'anchor'])
    assert phase['anchor'] in pages['execution-flow.html'].ids
predictions = json.loads((ROOT / 'content/predictions.json').read_text())
prediction_ids = [item['id'] for item in predictions]
assert len(set(prediction_ids)) == len(prediction_ids)
assert all(re.fullmatch(r'[a-z0-9-]+', item) for item in prediction_ids)
referenced = [item for lesson in lessons for item in lesson.get('exercises', [])]
assert sorted(referenced) == sorted(prediction_ids), 'Each exercise must be referenced once'
for exercise in predictions:
    assert all(exercise.get(key) for key in ['title', 'intro', 'code', 'prompts', 'flow', 'reasoning', 'output', 'verify_code', 'evidence', 'spoken', 'followup', 'followup_answer', 'sources'])
    assert all(step.get('label') and step.get('detail') for step in exercise['flow'])
    ast.parse(exercise['code'])
    ast.parse(exercise['verify_code'])
    assert exercise['id'] in pages['predict-execution.html'].ids
    assert all('source-' + source in pages['predict-execution.html'].ids for source in exercise['sources'])
# This lesson's pre/code blocks are all Python, including shared setup and AQE.
for code in pages['predict-execution.html'].code_blocks:
    ast.parse(code)
print(f'PASS: {len(pages)} pages, {checks} local links/assets, {len(lessons)} lesson schemas/examples, {len(questions)} questions, {len(predictions)} prediction exercises.')
