#!/usr/bin/env python3
"""
tools/auditors/check_gauge_chain.py

The owner's instruction, verbatim: *"when you fixing, write instead of erasing or
cutting used logic, and the logic needs to chain to one another."*

Batch 140 answered that by accident and batch 142 answered it on purpose. The
M.A.W. set is four pages that describe one entity: a Side Codex (A) and three
pieces (B weapon, C suit, D stigma). The Sorrow Gauge belongs to the *entity*, so
the four pages must quote one reading, not four.

Before batch 142 the pieces said:

    | **Binding rule:** ... after every event. The Sorrow Gauge held at its
      opening band.

— a sentence with no number in it, identical in 57 files, sitting inside a list of
conditions. After batch 142 each piece files its own field:

    **Gauge:** 739/739; opens at 45–65%; no hit band is filed.

and its failure mode chains the consequence to the same two figures:

    ... raises the source Gauge, so the 739/739 meter moves off its 45–65% opening
    band before the bearer feels the reversal.

WHAT THIS CHECKS
  1. Every piece's `**Gauge:**` maximum and opening band appear in its set's A-page
     `Gauge / Pressure` row. A piece may not invent its own meter.
  2. Every A-page prose clause ("The gauge opens at X of its Y meter") uses the
     same two figures as its own table row.
  3. Every failure mode that cites a meter cites the piece's own figures.

A figure that appears on a piece page and nowhere on the set record is the defect
this exists to stop: the chain is what makes the four pages one record.

Ceiling 0, ratcheted both ways.
"""

import glob
import io
import os
import re
import sys

ROOT = os.getcwd()
SETS = os.path.join(ROOT, 'SOMNARAK-WORLD', 'MAW_Codex_Sets')

RATCHET = 0

# Two set schemas exist. The 1000-series files `| Gauge / Pressure | 739/739; starts
# 45-65% ... |`; older ranges file `| Gauge / pressure | 45-65% / Lament 18-41 |`.
# The label differs only in case, but the older value carries no max/max figure, so
# the maximum check applies only where the row actually holds one.
ROW = re.compile(r'\|\s*Gauge\s*/\s*[Pp]ressure\s*\|\s*([^|\n]+?)\s*\|')
FIELD = re.compile(r'\*\*Gauge:\*\*\s*([^;\n]+);\s*opens at\s*([^;\n]+);')
ACLAUSE = re.compile(r'The gauge opens at ([\d–\-]+%) of its ([\d,]+/[\d,]+) meter')
FAILURE = re.compile(r'so the ([\d,]+/[\d,]+) meter moves off its ([\d–\-]+%) opening band')


def figures(text):
    """Every number that can identify a meter reading."""
    return set(re.findall(r'[\d,]+/[\d,]+|[\d–\-]+%', text))


def verify_set(setdir):
    """Return the broken links in one set. Empty list means the chain holds.

    A set is only held to this rule if one of its pieces files a `**Gauge:**`
    field. Ranges 001-195 use an older schema that carries the gauge elsewhere
    (`| Gauge Overflow |`, `| Gauge / pressure |`), and holding those to the
    1000-series field would report the schema, not a defect.
    """
    defects = []
    pieces = sorted(glob.glob(os.path.join(setdir, '*-[BCD]__*.md')))
    fields = {}
    for piece in pieces:
        ptext = io.open(piece, encoding='utf-8').read()
        f = FIELD.search(ptext)
        if f:
            fields[piece] = (f, ptext)
    if not fields:
        return defects, 0

    apages = glob.glob(os.path.join(setdir, '*-A__*.md'))
    if not apages:
        return defects, 0
    atext = io.open(apages[0], encoding='utf-8').read()
    row = ROW.search(atext)
    if not row:
        defects.append((os.path.relpath(apages[0], ROOT), 'no Gauge / Pressure row',
                        'a set record must file the meter its pieces quote'))
        return defects, len(fields)
    row_figs = figures(row.group(1))

    clause = ACLAUSE.search(atext)
    if clause:
        if clause.group(1) not in row_figs or clause.group(2) not in row_figs:
            defects.append((os.path.relpath(apages[0], ROOT),
                            f'{clause.group(1)} of {clause.group(2)}',
                            'A-page clause disagrees with its own row'))

    for piece, (f, ptext) in sorted(fields.items()):
        rel = os.path.relpath(piece, ROOT)
        mx, band = f.group(1).strip(), f.group(2).strip()
        if mx not in row_figs and re.search(r'\d+/\d+', row.group(1)):
            defects.append((rel, f'maximum {mx}',
                            'piece files a figure its set record does not'))
        if band not in row_figs:
            defects.append((rel, f'band {band}',
                            'piece files a figure its set record does not'))
        fail = FAILURE.search(ptext)
        if fail and (fail.group(1) != mx or fail.group(2) != band):
            defects.append((rel, f'{fail.group(1)} / {fail.group(2)}',
                            'failure mode cites a different meter'))
    return defects, len(fields)


def main(argv):
    verbose = '-v' in argv or '--verbose' in argv
    defects = []
    checked_pieces = 0
    sets = 0

    for reg in sorted(d for d in os.listdir(SETS)
                      if re.fullmatch(r'Registry_\d+_to_\d+', d)):
        for setdir in sorted(glob.glob(os.path.join(SETS, reg, '*'))):
            if not os.path.isdir(setdir):
                continue
            found, n = verify_set(setdir)
            if n:
                sets += 1
                checked_pieces += n
            defects.extend(found)

    print(f'GAUGE CHAIN — {checked_pieces} piece pages across {sets} sets')
    if verbose:
        for rel, what, why in defects:
            print(f'      {rel:70} {what:22} {why}')
    print(f'  broken-chain          {len(defects)}   ceiling {RATCHET}')
    if len(defects) > RATCHET:
        print(f'RESULT: FAIL — {len(defects)} ABOVE CEILING {RATCHET}')
        return 1
    if len(defects) < RATCHET:
        print(f'RESULT: FAIL — BELOW CEILING, lower it to {len(defects)}')
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
