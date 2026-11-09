#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_rule_index.py — gate 90: a rule is indexed the moment it is stated (O-30, R-12).

`RULES/README.md` says, in its own last line, that a rule is added the moment it is stated.
It was not true: batches 193–205 filed **R-46** through **R-50** and the index still ended at
`R-35`, so five binding rules were invisible to anyone who opened the folder's front page.

This gate reads the folder rather than a list: every `R-nn_*.md` on disk must appear in the
README table, and every row in the table must point at a file that exists.

WHAT FAILS
  * a rule file on disk with no row in `RULES/README.md`;
  * a row in `RULES/README.md` linking to a file that is not there;
  * a rule file whose title in the table does not begin with the same `R-nn`.

WHAT IS REPORTED
  * the count on each side, so a gate that matched nothing at all is visible.

    python3 tools/auditors/check_rule_index.py
    python3 tools/auditors/check_rule_index.py -v
"""
import glob
import io
import os
import re
import sys

RULES = 'REFERENCE_SOMNARAK_WIKI/RULES'
README = os.path.join(RULES, 'README.md')
ROW = re.compile(r'\[`(R-\d+)`\]\(([^)]+)\)')
FILENAME = re.compile(r'^(R-\d+)_.+\.md$')


def on_disk():
    out = {}
    for path in sorted(glob.glob(os.path.join(RULES, 'R-*.md'))):
        m = FILENAME.match(os.path.basename(path))
        if m:
            out[m.group(1)] = path
    return out


def indexed():
    text = io.open(README, encoding='utf-8').read()
    return [(m.group(1), m.group(2)) for m in ROW.finditer(text)]


def compare(disk, rows, exists=None):
    """Pure: the differences between what is on disk and what the README lists.

    `exists` is injectable so the tests can drive the logic without writing files.
    """
    exists = os.path.exists if exists is None else exists
    listed = [r[0] for r in rows]
    bad = []
    for rid in disk:
        if rid not in listed:
            bad.append((rid, 'on disk, not in RULES/README.md'))
    for rid, target in rows:
        path = os.path.join(RULES, target)
        if not exists(path):
            bad.append((rid, 'indexed but the file is not there: %s' % target))
        elif not os.path.basename(path).startswith(rid + '_'):
            bad.append((rid, 'the row points at another rule: %s' % target))
    dupe = [r for r in set(listed) if listed.count(r) > 1]
    for rid in sorted(dupe):
        bad.append((rid, 'indexed more than once'))
    return bad


def measure():
    disk = on_disk()
    rows = indexed()
    return disk, rows, compare(disk, rows)


def main(argv):
    disk, rows, bad = measure()
    if '-v' in argv:
        for rid, target in rows:
            print('%-6s %s' % (rid, target))
    for rid, why in bad:
        print('%s  %s' % (rid, why))
    print('rules filed and not indexed: %d' % len(bad))
    if bad:
        print('rules indexed: %d of %d on disk' % (len(rows) - len(bad), len(disk)))
        print('RESULT: FAIL — %d rules filed and not indexed' % len(bad))
        return 1
    print('rules on disk %d · indexed %d' % (len(disk), len(rows)))
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
