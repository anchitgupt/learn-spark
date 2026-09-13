"""Check generated links, fragments, source metadata, and Python example syntax."""
import ast
import json
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
assert len(pages) >= 12, 'Build the site first'
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
lessons = json.loads((ROOT / 'content/lessons.json').read_text())
slugs = [l['slug'] for l in lessons]
assert len(set(slugs)) == len(slugs)
for lesson in lessons:
    assert lesson['sources'] and lesson['reviewed'] and lesson['version']
    assert all(s['url'].startswith('https://spark.apache.org/docs/') for s in lesson['sources'])
    ast.parse(lesson['code'])
questions = json.loads((ROOT / 'content/questions.json').read_text())
assert len(set(q['id'] for q in questions)) == len(questions)
assert all(q['topic'] in slugs and q['answer'] and q['source'] for q in questions)
for item in json.loads((OUT / 'search.json').read_text()):
    assert (OUT / item['url']).is_file()
print(f'PASS: {len(pages)} pages, {checks} local links/assets, {len(lessons)} lesson schemas/examples, {len(questions)} questions.')
