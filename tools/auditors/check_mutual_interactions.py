#!/usr/bin/env python3
"""
tools/auditors/check_mutual_interactions.py

Two records describing the same pairing must agree about it.

Batch 146 linked every filed `Related entity` name, which made the relationship
graph readable for the first time: **416 directed edges, 402 one-way and only 7
mutual.** The asymmetry is correct — each wing surveys its own holdings, and a Zone D
file has no duty to record a Zone B survey. But the 7 mutual pairs are two records
speaking about one event, and those are checkable.

WHAT THIS CATCHES
  Approach polarity. If one record says the entity reaches toward / approaches /
  closes on the other, and the other says neither approaches / stays stopped /
  does not close the distance, the same pairing cannot be both.

  Found on the first run: `SE-C-Vδ-002 The Grieving Colossus` filed *"She reaches
  toward it, repeatedly"* for The Smothering Mother, while her own record filed
  *"Neither approaches the other at any point in six pairings"* — and her general
  rule states she stopped short exactly once, for the Silent Child.

WHICH RECORD OWNS THE FACT
  The record of the entity whose behaviour is being described. Her file is the
  authority on what she does; the observing wing's file is the authority on what it
  saw, which is a different claim. So the repair aligns the observer to the owner and
  keeps the observer's own observation — here, that the district misread the
  stillness as kinship.

WHAT IS NOT FLAGGED
  * One-way edges. 402 of 416; absence of a return survey is not a contradiction.
  * Different counts of pairings run by different wings. Five co-presences in one
    series and six pairings in another are two series, not one number twice.
  * Restatements of the same fact in different words. Only opposed polarity fires.

Ceiling 0, ratcheted both ways.
"""

import glob
import io
import os
import re
import sys

ROOT = os.getcwd()
DOSSIER_GLOBS = [
    os.path.join(ROOT, 'SOMNARAK-WORLD', 'Sorrow_Entities', 'SE-*.md'),
    os.path.join(ROOT, 'SOMNARAK-WORLD', 'Unknown_Entities', '*.md'),
]
RATCHET = 0

APPROACH = re.compile(
    r'\b(reaches? (?:toward|for|out)|approaches|advances? on|closes? (?:on|the distance)|'
    r'closes? in|steps? toward|crosses? to)\b', re.I)
NO_APPROACH = re.compile(
    r'\b(neither approaches|does not approach|does not advance|stays? stopped|'
    r'stops? at the sight|never approaches|no approach|keeps? (?:its|her|his) distance)\b',
    re.I)


def interaction_rows(path):
    """[(target_abspath, cell_text)] for one dossier."""
    with io.open(path, encoding='utf-8') as fh:
        text = fh.read()
    out = []
    for block in re.findall(r'\| Related entity \|.*?\n\n', text, re.S):
        for line in block.split('\n'):
            if not line.startswith('|') or 'Related entity' in line:
                continue
            if set(line.strip()) <= set('|-: '):
                continue
            cells = line.split('|')
            if len(cells) < 3:
                continue
            m = re.search(r'\]\(([^)]+\.md)\)', cells[1])
            if m:
                out.append((os.path.normpath(os.path.join(os.path.dirname(path), m.group(1))),
                            cells[2].strip()))
    return out


def polarity(text):
    """Mask negations before testing for approach.

    "Neither approaches" contains the word "approaches". Testing for approach
    first — or testing both against the raw text — makes every denial read as
    `mixed`, which is how the first version of this checker reported 0 defects on a
    corpus that contained one. The denial is removed from the string, and only what
    survives can assert an approach.
    """
    denied = bool(NO_APPROACH.search(text))
    rest = NO_APPROACH.sub(' ', text)
    asserted = bool(APPROACH.search(rest))
    if asserted and not denied:
        return 'approach'
    if denied and not asserted:
        return 'no-approach'
    return 'mixed'


def main(argv):
    verbose = '-v' in argv or '--verbose' in argv
    files = sorted(p for g in DOSSIER_GLOBS for p in glob.glob(g))
    edges = {(os.path.normpath(p), d): t for p in files for d, t in interaction_rows(p)}

    defects = []
    mutual = 0
    for (a, b), text in sorted(edges.items()):
        if (b, a) not in edges:
            continue
        if a > b:
            continue                       # score each pair once
        mutual += 1
        pa, pb = polarity(text), polarity(edges[(b, a)])
        if {pa, pb} == {'approach', 'no-approach'}:
            defects.append((a, b, pa, pb))

    print(f'MUTUAL INTERACTIONS — {len(files)} dossiers · {len(edges)} edges · '
          f'{mutual} mutual pairs')
    if verbose:
        for a, b, pa, pb in defects:
            print(f'      {os.path.basename(a)[:44]:46} {pa:12} vs '
                  f'{os.path.basename(b)[:40]:42} {pb}')
    print(f'  opposed-polarity      {len(defects)}   ceiling {RATCHET}')
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
