#!/usr/bin/env python3
"""check_box_geometry.py - crooked-box gate, built on tools/textbox.py.

WHAT THIS ADDS
--------------
`tools/text_box_double_checker.py` only inspects boxes inside ``` fences, and
`tools/check_box_symmetry.py` checks border character symmetry. Neither checks
a box that is sitting bare in the middle of a document. Three such boxes lived
in `GUIDES/MAW_VARIETY_DESIGN_FRAMEWORK.md`, two of them genuinely crooked, and
no check reported them for 120 batches. `tools/textbox.py` found them on its
first run.

WHY THE FILTER EXISTS
---------------------
`textbox.check()` enforces three things this archive does not want enforced:

  * "printable ASCII only" - this archive's canonical notation is Greek
    (alpha beta gamma delta omega), and 677 of its boxes carry it. A box
    containing a grade letter is not defective.
  * the 104-column viewport ceiling - the archive's own formatting template
    reserves 127-128 columns for tactical monitors.

It DOES enforce that a rule row is an unbroken line reaching both rails. 204
such rows drew the divider as `| ----+---- |`, leaving the fill short of each
rail; all 204 are now repaired, so the class is a defect and stays one.

So this gate fails on: A BOX WHOSE ROWS DO NOT MEASURE THE SAME, and A RULE ROW
WITH A GAP IN IT.

USAGE
    python3 tools/check_box_geometry.py            # whole tree
    python3 tools/check_box_geometry.py FILE...    # named files

Prints "RESULT: PASS" (with the box count) or "RESULT: FAIL" and the boxes.
"""
import glob
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import textbox

SKIP_DIRS = ('ARCHIVE/', 'tools/tests/', '.git/')

# textbox's own viewport ceiling is 104; this archive's template allows 127-128
# for tactical monitors, so the ceiling is raised for the one class of box that
# is meant to be that wide.
CEILING = 128
textbox.HARD_MAX = CEILING

KEEP = ('CROOKED', 'cap widths differ', 'top cap must', 'bottom cap must',
        'must open and close', 'exceeds')


def holes(box):
    """A rule row must be an unbroken line between its two end characters.

    A rule drawn as `| ----+----   |` leaves the fill short of the rail, and one
    drawn as `+----+----   -+` leaves a gap *inside* the line. Both were present
    in the archive and neither was reported: the first because `textbox` calls it
    a house style, the second because it did not exist until a repair introduced
    it. A space between the rails of a rule row is always a defect.
    """
    out = []
    for i, l in enumerate(box.split('\n'), 1):
        s = l.strip()
        if not (s.startswith('+') and s.endswith('+')):
            continue
        if not set(s) <= set('+-= '):
            continue
        if not ('-' in s or '=' in s):
            continue
        if ' ' in s[1:-1]:
            out.append('row %d: hole in the rule at %s'
                       % (i, [k for k, c in enumerate(s) if c == ' '][:4]))
    return out


def real_problems(box):
    """Only the geometry problems this archive treats as defects."""
    out = []
    for p in textbox.check(box, max_width=CEILING):
        if 'non-ASCII' in p:
            continue                      # Greek notation is canonical
        if 'rule stops' in p:
            out.append(p)                 # a rule short of the rail is now a defect
        elif any(k in p for k in KEEP):
            out.append(p)
    out.extend(holes(box))
    return out


def paths(argv):
    if argv:
        return argv
    seen = []
    for p in sorted(glob.glob('**/*.md', recursive=True)):
        if p.startswith(SKIP_DIRS):
            continue
        seen.append(p)
    return seen


def main(argv):
    total = bad = files = 0
    report = []
    for path in paths(argv):
        try:
            text = io.open(path, encoding='utf-8', errors='ignore').read()
        except IOError:
            continue
        boxes = textbox.find_boxes(text)
        if not boxes:
            continue
        files += 1
        for i, box in enumerate(boxes, 1):
            total += 1
            pr = real_problems(box)
            if pr:
                bad += 1
                report.append((path, i, pr))

    for path, i, pr in report:
        print('CROOKED BOX: %s box %d' % (path, i))
        for x in pr[:6]:
            print('    %s' % x)

    print('-')
    print('boxes measured : %d across %d files' % (total, files))
    print('crooked        : %d' % bad)
    if bad:
        print('RESULT: FAIL')
        return 1
    print('RESULT: PASS (0 crooked boxes)')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
