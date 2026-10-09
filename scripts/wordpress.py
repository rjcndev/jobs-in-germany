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
import json, os, re, subprocess, sys, tempfile, pathlib, unicodedata

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
    """Turn the README's folder tree code block into a list of links."""
    def repl(m):
        items = []
        for line in m.group(1).split('\n'):
            d = re.match(r'^[│├└─\s]*([\w-]+)/\s*(.*)$', line)
            if not d:
                continue
            name, note = d.groups()
            if name == 'jobs':
                continue
            path = 'reference/README.md' if name == 'reference' else f'jobs/{name}/README.md'
            items.append(f'- [{name}]({path})' + (f' — {note}' if note else ''))
        return '\n'.join(items) + '\n'
    return re.sub(r'(?<=## Structure\n\n)```\n(.*?)```\n', repl, text, flags=re.S)


def landing(text):
    """The README as the site's landing page: linked folder tree, repo link."""
    source = f'The source is on GitHub: [rjcndev/jobs-in-germany]({REPO}).\n\n'
    return link_tree(text).replace('## Structure', source + '## Structure', 1)


def convert(src, url, text=None):
    text = src.read_text() if text is None else text
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
    body = rewrite_links('\n'.join(lines).lstrip('\n'), src, url)
    return f'---\ntitle: {json.dumps(title, ensure_ascii=False)}\n---\n\n{body}'


def first_heading(path):
    m = re.search(r'^# (.+)$', path.read_text(), re.M)
    return m.group(1).strip() if m else path.stem


def generated_index(title, intro, files, src_dir):
    """Index page for a folder that has no README.md of its own."""
    items = '\n'.join(f'- [{first_heading(f)}]({f.name})' for f in files)
    return f'# {title}\n\n{intro}\n\n{items}\n', src_dir / 'README.md'


# Pages to publish: (output path on the branch, source file, generated text or None)
pages = [('jobs-in-germany/index.md', root / 'README.md', None)]
for cat in sorted(p for p in (root / 'jobs').iterdir() if p.is_dir()):
    files = sorted(f for f in cat.glob('*.md') if f.name != 'README.md')
    readme = cat / 'README.md'
    gen = None
    if not readme.exists():
        name = cat.name.replace('-', ' ').capitalize()
        gen = generated_index(name, f'Profession profiles in the {cat.name} category.', files, cat)
    pages.append((f'jobs-in-germany/{cat.name}/index.md', readme, gen))
    pages += [(f'jobs-in-germany/{cat.name}/{f.name}', f, None) for f in files]
ref = sorted((root / 'reference').glob('*.md'))
pages.append(('jobs-in-germany/reference/index.md', root / 'reference' / 'README.md',
              generated_index('Reference', 'Background material the profession profiles link to.',
                              ref, root / 'reference')))
pages += [(f'jobs-in-germany/reference/{f.name}', f, None) for f in ref]

# Anchors each page will carry, so links to #sections can be checked.
anchors = {}
for out, src, gen in pages:
    text = gen[0] if gen else src.read_text()
    url = page_url(src.relative_to(root).as_posix())
    anchors[url] = {a for _, a in headings(text)}

with tempfile.TemporaryDirectory() as tmp:
    tmp = pathlib.Path(tmp)
    for out, src, gen in pages:
        url = page_url(src.relative_to(root).as_posix())
        dest = tmp / out
        dest.parent.mkdir(parents=True, exist_ok=True)
        if gen:
            with tempfile.NamedTemporaryFile('w', suffix='.md', dir=src.parent, delete=False) as g:
                g.write(gen[0])
            try:
                dest.write_text(convert(pathlib.Path(g.name), url))
            finally:
                os.unlink(g.name)
        else:
            text = landing(src.read_text()) if src == root / 'README.md' else None
            dest.write_text(convert(src, url, text))

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
