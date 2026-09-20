#!/usr/bin/env python3
"""Repo integrity checks. Run with `make check`."""
import re, sys, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
fail = []

def note(msg): fail.append(msg)

# 1. every relative markdown link resolves
for f in root.rglob('*.md'):
    for m in re.finditer(r'\]\((?!https?:|mailto:)([^)]+)\)', f.read_text()):
        target = m.group(1).split('#')[0]
        if not target:
            continue
        if not (f.parent / target).resolve().exists():
            note(f"broken link: {f.relative_to(root)} -> {m.group(1)}")

professions = {p.name for p in root.glob('jobs/*/*.md') if p.name != 'README.md'}

# 2. all three cross-reference tables cover every profession
for tbl in ['pay.md', 'language-requirements.md', 'visa-routes.md']:
    path = root / 'reference' / tbl
    if not path.exists():
        note(f"missing reference table: {tbl}"); continue
    listed = set(re.findall(r'\.\./jobs/[^/]+/([^)]+\.md)', path.read_text()))
    for miss in sorted(professions - listed):
        note(f"{tbl}: no row for {miss}")

# 3. pay table: no duplicate rows, sorted by entry midpoint descending
pay = (root / 'reference' / 'pay.md')
if pay.exists():
    rows = re.findall(r'^\| \[([^\]]+)\]\(([^)]+)\)[^|]*\|\s*€([\d,]+) – €([\d,]+)',
                      pay.read_text(), re.M)
    seen = {}
    for name, href, lo, hi in rows:
        if href in seen:
            note(f"pay.md: duplicate row for {href}")
        seen[href] = True
    mids = [(n, (int(lo.replace(',', '')) + int(hi.replace(',', ''))) // 2)
            for n, _, lo, hi in rows]
    for a, b in zip(mids, mids[1:]):
        if a[1] < b[1]:
            note(f"pay.md: out of order — {a[0]} ({a[1]}) before {b[0]} ({b[1]})")

# 4. every profession file carries a Last reviewed date
for p in sorted(root.glob('jobs/*/*.md')):
    if p.name == 'README.md':
        continue
    if '**Last reviewed**' not in p.read_text():
        note(f"{p.relative_to(root)}: no 'Last reviewed' field")

if fail:
    print(f"FAIL ({len(fail)} issue{'s' if len(fail) != 1 else ''})")
    for f in fail:
        print("  " + f)
    sys.exit(1)
print(f"OK — {len(professions)} professions, links resolve, tables complete, pay table sorted")
