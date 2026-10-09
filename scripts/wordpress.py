#!/usr/bin/env python3
"""Build the `wordpress` branch that the Git It Write plugin publishes from.

The repo's own links are relative paths to .md files so they work on GitHub and
Gitea. WordPress pages live at different URLs, so this script writes a copy of
the content with every link rewritten to the page it will become, and commits
it to the `wordpress` branch without touching the working tree. Run with
`make wordpress`, then `git push github wordpress`.

Page layout under BASE (one Git It Write entry, branch `wordpress`, folder root):

    README.md                  -> BASE/
    jobs/<cat>/README.md       -> BASE/<cat>/
    jobs/<cat>/<file>.md       -> BASE/<cat>/<file>/
    reference/<file>.md        -> BASE/reference/<file>/

Links to anything not published (TODO.md, TEMPLATE.md, ...) point at GitHub.
"""
import html, json, os, re, subprocess, sys, tempfile, pathlib, unicodedata

BASE = '/jobs-in-germany'
REPO = 'https://github.com/rjcndev/jobs-in-germany'
GITHUB = f'{REPO}/blob/main'
BRANCH = 'wordpress'

root = pathlib.Path(__file__).resolve().parent.parent
problems = []


def page_url(rel):
    """Site path for a repo-relative path, or None if it is not published."""
    parts = rel.split('/')
    if rel in ('README.md', ''):
        return BASE + '/'
    if parts[0] == 'jobs' and len(parts) == 2 and parts[1] == '':
        return BASE + '/'
    if parts[0] == 'jobs' and len(parts) >= 2:
        cat = parts[1]
        if len(parts) == 2 or parts[2] in ('', 'README.md'):
            return f'{BASE}/{cat}/'
        if len(parts) == 3 and parts[2].endswith('.md'):
            return f'{BASE}/{cat}/{parts[2][:-3]}/'
    if parts[0] == 'reference':
        if len(parts) == 1 or parts[1] in ('', 'README.md'):
            return f'{BASE}/reference/'
        if len(parts) == 2 and parts[1].endswith('.md'):
            return f'{BASE}/reference/{parts[1][:-3]}/'
    return None


def slugify(text, seen):
    """GitHub's heading anchor: lowercase, drop punctuation, spaces to hyphens."""
    text = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', text)  # link text only
    text = re.sub(r'[`*_~]', '', text).strip().lower()
    slug = ''.join(c for c in text
                   if c in ' -' or unicodedata.category(c)[0] in 'LN')
    slug = slug.replace(' ', '-')
    n = seen.get(slug, 0)
    seen[slug] = n + 1
    return slug if n == 0 else f'{slug}-{n}'


def headings(text):
    """(line index, anchor) for every ATX heading outside code fences."""
    out, seen, fence = [], {}, False
    for i, line in enumerate(text.split('\n')):
        if line.startswith('```'):
            fence = not fence
        m = None if fence else re.match(r'^(#{1,6})\s+(.*?)\s*#*\s*$', line)
        if m:
            out.append((i, slugify(m.group(2), seen)))
    return out


def rewrite_links(text, src, own_url):
    def repl(m):
        href = m.group(2)
        if re.match(r'^(https?:|mailto:)', href):
            return m.group(0)
        path, _, frag = href.partition('#')
        if not path:
            if frag not in anchors.get(own_url, set()):
                problems.append(f'{src.relative_to(root)}: no heading #{frag} on this page')
            return m.group(0)
        target = (src.parent / path).resolve()
        rel = target.relative_to(root).as_posix() + ('/' if path.endswith('/') else '')
        url = page_url(rel)
        if url is None:
            url = f'{GITHUB}/{rel.rstrip("/")}'
        elif frag and frag not in anchors.get(url, set()):
            problems.append(f'{src.relative_to(root)}: no heading #{frag} on {url}')
        return f'{m.group(1)}({url}{"#" + frag if frag else ""})'
    return re.sub(r'(\])\(([^)\s]+)\)', repl, text)


def link_tree(text):
    """Turn the README's folder tree code block into category cards."""
    def repl(m):
        items = []
        for line in m.group(1).split('\n'):
            d = re.match(r'^[│├└─\s]*([\w-]+)/\s*(.*)$', line)
            if not d:
                continue
            name, note = d.groups()
            if name == 'jobs':
                continue
            if name == 'reference':
                path, sub = 'reference/README.md', note
            else:
                path = f'jobs/{name}/README.md'
                n = len([f for f in (root / 'jobs' / name).glob('*.md') if f.name != 'README.md'])
                sub = f'{n} profession{"s" if n != 1 else ""}'
            items.append(card(category_title(name), path, sub))
        return cards(items)
    return re.sub(r'(?<=## Structure\n\n)```\n(.*?)```\n', repl, text, flags=re.S)


# README sections for whoever maintains the repo, left off the site.
REPO_ONLY = ('Adding a profession', 'Checks', 'Publishing', 'Conventions')


def landing(text):
    """The README as the site's landing page: linked folder tree, repo link,
    no repo-maintenance sections."""
    for heading in REPO_ONLY:
        text, n = re.subn(rf'^## {re.escape(heading)}\n.*?(?=^## |\Z)', '', text, flags=re.M | re.S)
        if n != 1:
            problems.append(f'README.md: no "## {heading}" section to leave off the site')
    text = text.replace('One file per profession, named after the German job title in kebab-case.\n\n', '')
    source = f'The source is on GitHub: [rjcndev/jobs-in-germany]({REPO}).\n\n'
    return link_tree(text).replace('## Structure', source + '## Structure', 1)


def first_heading(path):
    m = re.search(r'^# (.+)$', path.read_text(), re.M)
    return m.group(1).strip() if m else path.stem


def category_title(name):
    if name == 'reference':
        return 'Reference'
    readme = root / 'jobs' / name / 'README.md'
    if readme.exists():
        return first_heading(readme)
    return {'it': 'IT'}.get(name, name.replace('-', ' ').capitalize())


def summary(path):
    """First sentence of a page's opening blockquote, for its card."""
    quote = ' '.join(l[1:].strip() for l in path.read_text().split('\n') if l.startswith('>'))
    quote = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', quote)  # cards are links already
    m = re.match(r'(.+?[.!?])(\s|$)', quote)
    return (m.group(1) if m else quote).replace('*', '')


def card(title, href, sub=''):
    return f'- [{title}]({href})' + (f' <span>{html.escape(sub, quote=False)}</span>' if sub else '')


# Parsedown Extra's markdown="1" wrappers mangle blockquotes, so the stylesheet
# hooks onto empty marker divs placed just before the element they style.
def marker(name):
    return f'<div class="jig-{name}"></div>'


def cards(items):
    return marker('cards') + '\n\n' + '\n'.join(items) + '\n'


def file_cards(files):
    return cards([card(first_heading(f), f.name, summary(f)) for f in files])


def mark_facts(lines):
    """Mark a profile's key-facts table: the first one with an empty header row."""
    fence = False
    for i, line in enumerate(lines):
        if line.startswith('```'):
            fence = not fence
        if not fence and re.match(r'^\|\s*\|\s*\|\s*$', line):
            return lines[:i] + [marker('facts'), ''] + lines[i:]
    return lines


def breadcrumbs(url):
    parts = url[len(BASE):].strip('/').split('/')
    if parts == ['']:
        return ''
    crumbs = [f'<a href="{BASE}/">Jobs in Germany</a>']
    if len(parts) == 2:
        crumbs.append(f'<a href="{BASE}/{parts[0]}/">{html.escape(category_title(parts[0]))}</a>')
    return '<p class="jig-crumbs">' + ' <span>›</span> '.join(crumbs) + '</p>'


def convert(src, url, text):
    lines = text.split('\n')
    h1 = next((i for i, l in enumerate(lines) if l.startswith('# ')), None)
    title = lines[h1][2:].strip() if h1 is not None else src.stem
    for i, anchor in reversed(headings(text)):
        if anchor.isascii():
            lines[i] = f'{lines[i]} {{#{anchor}}}'  # Parsedown Extra heading id
        else:  # Parsedown Extra's {#id} only takes ASCII
            lines[i] = f'{lines[i]} <a id="{anchor}"></a>'
    if h1 is not None:
        del lines[h1]  # the theme prints the page title itself
    body = rewrite_links('\n'.join(mark_facts(lines)).strip('\n'), src, url)
    # The page marker scopes the site's stylesheet (scripts/wordpress.css) to these pages.
    head = '\n\n'.join(x for x in (marker('page'), breadcrumbs(url)) if x)
    body = f'{head}\n\n{body}'
    return f'---\ntitle: {json.dumps(title, ensure_ascii=False)}\n---\n\n{body}\n'


def generated_index(title, intro, files):
    """Index page for a folder that has no README.md of its own."""
    return f'# {title}\n\n{intro}\n\n{file_cards(files)}'


# Pages to publish: (output path on the branch, source path, page text)
landing_text = landing((root / 'README.md').read_text())
pages = [('jobs-in-germany/index.md', root / 'README.md', landing_text)]
for cat in sorted(p for p in (root / 'jobs').iterdir() if p.is_dir()):
    files = sorted(f for f in cat.glob('*.md') if f.name != 'README.md')
    readme = cat / 'README.md'
    if readme.exists():
        text = readme.read_text().rstrip('\n') + '\n\n## Professions in this category\n\n' + file_cards(files)
    else:
        text = generated_index(category_title(cat.name), 'Profession profiles in this category.', files)
    pages.append((f'jobs-in-germany/{cat.name}/index.md', readme, text))
    pages += [(f'jobs-in-germany/{cat.name}/{f.name}', f, f.read_text()) for f in files]
ref = sorted((root / 'reference').glob('*.md'))
pages.append(('jobs-in-germany/reference/index.md', root / 'reference' / 'README.md',
              generated_index('Reference', 'Background material the profession profiles link to.', ref)))
pages += [(f'jobs-in-germany/reference/{f.name}', f, f.read_text()) for f in ref]

# Anchors each page will carry, so links to #sections can be checked.
anchors = {page_url(src.relative_to(root).as_posix()): {a for _, a in headings(text)}
           for _, src, text in pages}

with tempfile.TemporaryDirectory() as tmp:
    tmp = pathlib.Path(tmp)
    for out, src, text in pages:
        dest = tmp / out
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(convert(src, page_url(src.relative_to(root).as_posix()), text))

    if problems:
        print(f'FAIL ({len(problems)} unresolved anchor{"s" if len(problems) != 1 else ""})')
        for p in problems:
            print('  ' + p)
        sys.exit(1)

    git = lambda *a, **kw: subprocess.run(['git', '-C', str(root), *a], check=True,
                                          capture_output=True, text=True, **kw).stdout.strip()
    env = dict(os.environ, GIT_INDEX_FILE=str(tmp.parent / f'.wp-index-{os.getpid()}'))
    try:
        git('--work-tree', str(tmp), 'add', '-A', '.', env=env)
        tree = git('write-tree', env=env)
    finally:
        pathlib.Path(env['GIT_INDEX_FILE']).unlink(missing_ok=True)

    parent = subprocess.run(['git', '-C', str(root), 'rev-parse', '-q', '--verify', f'refs/heads/{BRANCH}'],
                            capture_output=True, text=True).stdout.strip()
    if parent and git('rev-parse', f'{parent}^{{tree}}') == tree:
        print(f'{BRANCH} is already up to date')
        sys.exit(0)
    head = git('rev-parse', '--short', 'HEAD')
    msg = f'Build WordPress pages from main@{head}'
    commit = git('commit-tree', tree, *(['-p', parent] if parent else []), '-m', msg)
    git('update-ref', f'refs/heads/{BRANCH}', commit)
    print(f'{BRANCH} -> {commit[:7]}: {len(pages)} pages. Push with: git push github {BRANCH}')
