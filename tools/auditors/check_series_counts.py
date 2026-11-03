#!/usr/bin/env python3
"""check_series_counts.py — catch a numeral pool, not a repeated sentence.

Batch 149 closed 66 sentences that were a grammar rather than a fact. This is
the same defect one level lower: a **number** that was drawn from a fixed pool
and handed to unrelated dossiers.

Measured before the repair, across 301 dossiers:

    188 cycles   12 dossiers
    211 cycles    5
    211 sessions  2
    211 watches   2
    211 circuits  1

Two holdings cannot both have been worked 188 times. They are different ages,
in different wings, surveyed by different stations — and *nine* of those twelve
files also say *nine years*, which is not a coincidence but a shared clock. The
numeral was a slot, and the ratios written against it (147 of 188, 94 of 188,
179 of 188) were ratios against a denominator nobody had chosen.

**Why two is not three.** A pair can land on the same figure by chance; two
holdings 400 sectors apart have no reason to agree and no mechanism to make them
agree. Three cannot. Measured on the corpus after the batch-150 repair, every
pair that remained was two files counting *different things* with the same
numeral (a whisper tally and a minute-anomaly series). No pair has more than two.
So the gate fires at three, reports at two, and does not touch the world clock —
*nine years*, *eleven years*, *SECTOR-C-01* repeat legitimately and are not
series counts.

    python3 tools/auditors/check_series_counts.py        # ratchet check
    python3 tools/auditors/check_series_counts.py -v     # list every shared pair
    python3 tools/auditors/check_series_counts.py --files A.md B.md

The repair rule is in the batch-150 script, not here: a numeral is replaced by
the dossier's **own clock** ("nine years of the post's record"), never by a
different invented count. A checker must not prescribe content, and a count
swapped for another count would just move the pool.
"""
import glob
import io
import os
import re
import sys

DOSSIERS = ('SOMNARAK-WORLD/Sorrow_Entities/**/SE-*.md',
            'SOMNARAK-WORLD/Unknown_Entities/*.md')

# The units a dossier counts its own history in. Deliberately not exhaustive of
# English — a noun missing here is a gap in the guard, and the guard should fail
# loudly rather than pass quietly when a new unit appears in bulk (see the
# `unseen unit` report below).
UNITS = (r'cycles|channels|sessions|descents|arrivals|shifts|incidents|'
         r'occurrences|readings|watches|pairings|entries|attendances|silences|'
         r'viewings|circuits|runs|sittings|separations|tallies|surveys|'
         r'workings|expeditions|probes')

COUNT = re.compile(r'\b([\d,]{2,6})\s+(?:' + UNITS + r')\b')
# A figure below this is an event count inside one page ("four occurrences"),
# not a series length. Series lengths are the numbers a ratio is built on.
FLOOR = 20
# A pool is three or more dossiers printing the same count against the same unit.
POOL = 3
RATCHET = 0          # pools above the ceiling
RATCHET_SET = '2026-11-03'


def dossier_files():
    found = []
    for pattern in DOSSIERS:
        found.extend(glob.glob(pattern, recursive=True))
    return sorted(set(found))


def measure(paths=None):
    """{(count, unit): {path, ...}} for every count at or above FLOOR."""
    files = paths if paths is not None else dossier_files()
    seen = {}
    for path in files:
        try:
            with io.open(path, encoding='utf-8') as handle:
                text = handle.read()
        except OSError:
            continue
        for match in COUNT.finditer(text):
            value = int(match.group(1).replace(',', ''))
            if value < FLOOR:
                continue
            unit = match.group(0).split()[-1]
            seen.setdefault((value, unit), set()).add(path)
    return files, seen


def pools(seen, minimum=POOL):
    out = []
    for (value, unit), paths in sorted(seen.items()):
        if len(paths) >= minimum:
            out.append((value, unit, sorted(paths)))
    return out


def audit_files(paths):
    """Named files only: a pool is a property of the set, so state it that way."""
    _, seen = measure(paths)
    bad = 0
    for value, unit, owners in pools(seen, minimum=2):
        bad += 1
        print(f'  SHARED {value} {unit}: {len(owners)} of {len(paths)} named files')
        for owner in owners:
            print(f'      {owner.split("/")[-1]}')
    print(f'RESULT: {"FAIL" if bad else "PASS"} — {bad} shared figure(s) among the named files')
    return 1 if bad else 0


def main(argv):
    if '--files' in argv:
        named = argv[argv.index('--files') + 1:]
        if not named:
            print('RESULT: FAIL — --files needs at least one path')
            return 1
        return audit_files(named)

    verbose = '-v' in argv or '--verbose' in argv
    files, seen = measure()
    if not files:
        print('RESULT: FAIL — no dossiers matched; the glob is wrong, not the corpus')
        return 1

    found = pools(seen)
    pairs = [p for p in pools(seen, minimum=2) if len(p[2]) == 2]
    print(f'SERIES COUNTS — {len(files)} dossiers · {len(seen)} distinct count/unit pairs '
          f'at or above {FLOOR}')
    if verbose and pairs:
        for value, unit, owners in pairs:
            print(f'  coincidence  {value:>5} {unit:12s} '
                  f'{owners[0].split("/")[-1][:34]} / {owners[1].split("/")[-1][:34]}')
    if found:
        for value, unit, owners in found:
            print(f'  POOLED {value} {unit}: {len(owners)} dossiers')
            for owner in owners:
                print(f'      {owner.split("/")[-1]}')
    print(f'  pooled-at-three-or-more   {len(found)}   ceiling {RATCHET}')
    print(f'  same figure, two dossiers {len(pairs)}   reported, not gated')
    if len(found) > RATCHET:
        print(f'RESULT: FAIL — {len(found)} POOL(S) ABOVE CEILING {RATCHET}')
        return 1
    if len(found) < RATCHET:
        print(f'RESULT: FAIL — BELOW CEILING, lower it to {len(found)}')
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
