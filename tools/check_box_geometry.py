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
  * "rule stops N short of the rail" - 204 rows across GAME_BATTLE and
    Master_Codices draw an interior divider as `| ----+---- |` rather than a
    full `+---+` junction row. That is a house style, uniform inside each file.
  * the 104-column viewport ceiling - the archive's own formatting template
    reserves 127-128 columns for tactical monitors.

So this gate fails on exactly one class: A BOX WHOSE ROWS DO NOT MEASURE THE
SAME. That is the defect a reader actually sees, and it is the one nothing else
was catching.

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


def real_problems(box):
    """Only the geometry problems this archive treats as defects."""
    out = []
    for p in textbox.check(box, max_width=CEILING):
        if 'non-ASCII' in p:
            continue                      # Greek notation is canonical
        if 'rule stops' in p:
            continue                      # house divider style, see docstring
        if any(k in p for k in KEEP):
            out.append(p)
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
