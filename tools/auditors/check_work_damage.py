#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_work_damage.py — gate 87: a work session has a cost, and the cost is the holding's own (R-44).

L Corp files, in the basic information, a **Work Damage**: a type and an amount the employee takes
while working. This archive filed work preferences and an energy yield and nothing about what the
session cost the person doing it. `R-44` adds `| **Work Damage** |`.

WHAT FAILS
  * an amount outside the band for the entity's tier;
  * a type that is not the entity's own `Element` row;
  * a `Work Damage` row on a holding with no work loop — the yield opens on an em dash. That is how
    a terminus (R-35) or a relic (R-40) gets caught;
  * a High holding with a work loop and no `Work Damage` row at all.

WHAT IS NOT THIS GATE'S
  * the two verdicts that read `None` — R-49 gives a holding the right to cost the worker nothing
    or to pay them; those rows carry no band and no element, and `check_work_effect.py` reads them.

WHAT IS REPORTED
  * the lower bands that have not been rolled out yet, counted per band. The row is a reading of
    what each holding is, and 301 readings do not happen in one batch.

BANDS (R-44 s3), deliberately the shape of L Corp's own spread:

    ZAYIN  1-3      TETH  1-4      HE  2-6      WAW  3-8      ALEPH  5-10
"""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from check_stat_bands import GRADE, RANK, row, tier_of  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PATHS = sorted(glob.glob(os.path.join(ROOT, 'SOMNARAK-WORLD', '*', 'SE-*.md')))

BANDS = {'ZAYIN': (1, 3), 'TETH': (1, 4), 'HE': (2, 6), 'WAW': (3, 8), 'ALEPH': (5, 10)}
ELEMENTS = ('Lament', 'Grudge', 'Void', 'Weight')


def band_of(text):
    coherence, potency = row(text, 'Coherence'), row(text, 'Potency')
    if not coherence or not potency:
        return None
    r = re.search(r'\b(I{1,3}|IV|V)\b', coherence)
    g = re.search(r'([αβγδω])', potency)
    if not r or not g:
        return None
    return tier_of(RANK[r.group(1)] + GRADE[g.group(1)])


def has_work_loop(text):
    yield_cell = row(text, 'Han-Energy yield') or ''
    return not yield_cell.strip().startswith('\u2014')


def element_of(text):
    cell = row(text, 'Element') or ''
    if re.search(r'all four', cell, re.I):
        return 'all four'
    for e in ELEMENTS:
        if e in cell:
            return e
    return None


def amount(cell):
    m = re.search(r'(\d+)\s*(?:\u2013|-|~)\s*(\d+)', cell or '')
    return (int(m.group(1)), int(m.group(2))) if m else None


def problems(text):
    """Failures this gate refuses. Pure function; the tests drive it directly."""
    tier = band_of(text)
    if tier is None:
        return []
    cell = row(text, r'Work Damage')
    loop = has_work_loop(text)
    bad = []

    if not loop:
        if cell is not None:
            bad.append('no work loop but carries a Work Damage row')
        return bad

    if cell is None:
        if tier == 'ALEPH':
            bad.append('High holding with a work loop and no Work Damage row')
        return bad

    if cell.strip().startswith('None'):
        # R-49: two of the three verdicts read `None` — the band and the element
        # belong to the damage verdict only, and check_work_effect.py owns them.
        return bad

    lo, hi = BANDS[tier]
    rng = amount(cell)
    if not rng:
        bad.append('Work Damage row has no readable amount')
    elif rng[0] < lo or rng[1] > hi:
        bad.append('Work Damage %d\u2013%d outside the %s band %d\u2013%d'
                   % (rng[0], rng[1], tier, lo, hi))

    element = element_of(text)
    if element == 'all four':
        if not re.search(r'all four|cycling all four', cell, re.I):
            bad.append('element is all four but the damage type does not say so')
    elif element and element not in cell:
        bad.append('damage type does not match the Element row (%s)' % element)
    return bad


def main():
    fail, missing = [], {}
    for path in PATHS:
        with open(path, encoding='utf-8') as fh:
            text = fh.read()
        name = os.path.basename(path)
        found = problems(text)
        if found:
            fail.append((name, found))
        tier = band_of(text)
        if (tier and tier != 'ALEPH' and has_work_loop(text)
                and row(text, r'Work Damage') is None):
            missing[tier] = missing.get(tier, 0) + 1

    for name, found in fail:
        print('%s  %s' % (name, '; '.join(found)[:150]))
    print('still to roll out (work loop, no Work Damage row): %s'
          % (', '.join('%s=%d' % kv for kv in sorted(missing.items())) or 'none'))
    print('work-damage failures: %d' % len(fail))
    if fail:
        print('RESULT: FAIL')
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main())
