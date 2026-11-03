#!/usr/bin/env python3
"""fix_md_tables.py — repair the three table faults check_md_tables.py finds.

Built for batch 158, when the archive held **369 ragged tables** and every one of
them had the same cause: a two-cell `| **Maximum Amount** | N — X |` row left
under a five-column CORE STATISTICS header. A row with fewer cells than its
header does not render as a short row — GFM drops the surplus on the floor and
the last column slides left, so the numbers landed under the wrong headings.

Three repairs, in the order they are tried, and no fourth:

1. **`stray-maximum`** — a 2-cell row reading `**Maximum Amount**` inside a wider
   table is lifted out and printed as its own `| Field | Record |` table directly
   beneath the parent. That is the shape `TEMPLATES/SE/03_MAW_WEAPON_TEMPLATE.md`,
   `04_MAW_SUIT` and `05_MAW_STIGMA` already use for this field, so the repair
   converges on the templates rather than inventing a fourth style.
2. **`short-row`** — any other row carrying fewer cells than its header gets the
   missing cells added empty, so the columns keep their positions.
3. **`no-separator`** — a header row followed directly by data gets its `|---|`
   separator inserted at the header's width.

It never fills a cell with invented text. Where the content is genuinely missing —
`SE-N-IVδ-611` and `-641` were transcribed with whole cells absent — the repair
writes `— *not separately recorded*`, and the prose above the table is left alone.

    python3 tools/fix_md_tables.py            # dry run, prints what it would do
    python3 tools/fix_md_tables.py --apply    # write
    python3 tools/fix_md_tables.py --apply PATH ...
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'auditors'))

from check_md_tables import PIPESPLIT, SEP, cells, corpus, tables  # noqa: E402

MAXROW = re.compile(r'^\|\s*\*{0,2}Maximum Amount\*{0,2}\s*\|(.+)\|\s*$')
MISSING = '— *not separately recorded*'


def plan(lines):
    """Return [(start, end, kind)] for every block this script can repair."""
    jobs = []
    for s, e in tables(lines):
        block = lines[s:e]
        if len(block) < 2:
            continue
        if not SEP.match(block[1]):
            jobs.append((s, e, 'no-separator'))
            continue
        width = cells(block[0])
        if any(cells(line) != width for line in block):
            jobs.append((s, e, 'ragged'))
    return jobs


def repair(block, kind):
    """Return (new lines, extra lines after the table) for one block."""
    width = cells(block[0])
    if kind == 'no-separator':
        return [block[0], '|' + '---|' * width] + block[1:], []
    keep, extras = [], []
    for k, line in enumerate(block):
        if k < 2 or cells(line) == width:
            keep.append(line)
            continue
        m = MAXROW.match(line.strip())
        if m and cells(line) == 2:
            extras.append('| **Maximum Amount** |%s|' % m.group(1))
            continue
        parts = PIPESPLIT.split(line)
        missing = width - cells(line)
        parts[-1:-1] = [' %s ' % MISSING] * missing
        keep.append('|'.join(parts))
    tail = []
    if extras:
        # A blank on both sides: the parent table must not run into the mini
        # table, and the prose after the table must not run into the mini table.
        tail = ['', '| Field | Record |', '|---|---|'] + extras + ['']
    return keep, tail


def fix(path, dry=True):
    """Return the number of blocks repaired in `path`."""
    with io.open(path, encoding='utf-8') as fh:
        text = fh.read()
    lines = text.split('\n')
    jobs = plan(lines)
    if not jobs:
        return 0
    out, cur = [], 0
    for s, e, kind in jobs:
        out.extend(lines[cur:s])
        block, tail = repair(lines[s:e], kind)
        out.extend(block)
        out.extend(tail)
        cur = e
        if tail and cur < len(lines) and lines[cur].strip() == '':
            cur += 1              # collapse our trailing blank with the file's own
    out.extend(lines[cur:])
    new = '\n'.join(out)
    if not dry and new != text:
        with io.open(path, 'w', encoding='utf-8') as fh:
            fh.write(new)
    return len(jobs)


def main(argv):
    apply_ = '--apply' in argv
    paths = [a for a in argv if not a.startswith('-')] or corpus()
    blocks = files = 0
    for path in paths:
        n = fix(path, dry=not apply_)
        if n:
            files += 1
            blocks += n
            print('%s  %d' % (path, n))
    print('%s: %d blocks in %d files' % ('APPLIED' if apply_ else 'DRY', blocks, files))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
