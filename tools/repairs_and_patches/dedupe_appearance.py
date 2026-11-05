#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""dedupe_appearance.py - stop the Appearance section saying the same sentence three times.

A dossier's `## Appearance` section opened like this:

    **Physical Form:** A ruin-shaped object of red-black crystal, preserving the outline
    of a beloved place.

    **Notable Features:** ...

    **Identification Profile**

    - **Primary marker:** A ruin-shaped object of red-black crystal, preserving the
      outline of a beloved place.          <- the same sentence again

    ### Detailed Appearance Profile

    | **Form** | A ruin-shaped object of red-black crystal, preserving the outline of a
    |          | beloved place.            <- and a third time, twenty lines down

The template asked for a Physical Form line, a Primary marker bullet and a Form row, so
all three were filled with the one description the file had. Measured: 73 dossiers repeat
the Physical Form value verbatim in Primary marker, and 82 repeat it verbatim in the
Form row.

This removes the later copy when it is verbatim identical (after normalising punctuation
and whitespace) to the Physical Form line, and does nothing else. A marker or row that
carries even one extra clause is left alone, because then it is saying something.

Guards per file: the Appearance section must still hold at least 40 words and at least
four lines, `## Appearance` must survive, and the bold count must stay even.

    python3 tools/repairs_and_patches/dedupe_appearance.py            report
    python3 tools/repairs_and_patches/dedupe_appearance.py --write    apply
"""
import argparse
import glob
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PATHS = sorted(glob.glob(os.path.join(ROOT, 'SOMNARAK-WORLD', '*', 'SE-*.md')))


def norm(s):
    s = re.sub(r'[*_`]', '', s)
    s = re.sub(r'\s+', ' ', s).strip().rstrip('.')
    return s.lower()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--write', action='store_true')
    args = ap.parse_args()

    removed = {'Primary marker': 0, 'Form row': 0}
    files = 0
    shown = 0

    for path in PATHS:
        with io.open(path, encoding='utf-8') as fh:
            t = fh.read()
        m = re.search(r'\n## Appearance[ \t]*\n(.*?)\n## ', t, re.S)
        if not m:
            continue
        body = m.group(1)
        pf = re.search(r'^\*\*Physical Form:\*\*\s*(.+)$', body, re.M)
        if not pf:
            continue
        target = norm(pf.group(1))
        if len(target.split()) < 5:
            continue

        orig = t
        # - Primary marker bullet
        pm = re.search(r'^- \*\*Primary marker:\*\*\s*(.+)$', body, re.M)
        if pm and norm(pm.group(1)) == target:
            line_start = m.start(1) + pm.start()
            line_end = m.start(1) + pm.end()
            t = t[:line_start] + t[line_end:].lstrip('\n')
            t = t[:line_start].rstrip('\n') + '\n' + t[line_start:]
            removed['Primary marker'] += 1
        # - Form row in the detailed table
        m2 = re.search(r'\n## Appearance[ \t]*\n(.*?)\n## ', t, re.S)
        body2 = m2.group(1)
        fr = re.search(r'^\|\s*\*\*Form\*\*\s*\|\s*(.+?)\s*\|$', body2, re.M)
        if fr and norm(fr.group(1)) == target:
            line_start = m2.start(1) + fr.start()
            line_end = m2.start(1) + fr.end()
            t = t[:line_start] + t[line_end:].lstrip('\n')
            t = t[:line_start].rstrip('\n') + '\n' + t[line_start:]
            removed['Form row'] += 1

        if t == orig:
            continue

        # guards
        m3 = re.search(r'\n## Appearance[ \t]*\n(.*?)\n## ', t, re.S)
        if not m3 or len(m3.group(1).split()) < 40 or len(m3.group(1).strip().split('\n')) < 4:
            continue
        if t.count('**') % 2:
            continue
        # the table must still be a table
        if t.count('| **Form**') + t.count('| **Position') < 1:
            continue

        files += 1
        if args.write:
            with io.open(path, 'w', encoding='utf-8') as fh:
                fh.write(t)
        elif shown < 2:
            shown += 1
            print('=' * 62)
            print(os.path.basename(path))
            print('  removed a copy of: %s' % pf.group(1)[:90])

    print()
    print('duplicate Primary marker bullets removed: %d' % removed['Primary marker'])
    print('duplicate Form rows removed:             %d' % removed['Form row'])
    print('files changed:                           %d' % files)


if __name__ == '__main__':
    main()
