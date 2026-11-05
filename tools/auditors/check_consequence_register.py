#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_consequence_register.py — gate 86: consequence reaches as far as the band does (R-43).

Ranked by `R-41`'s Threat Score, named by the owner:

    Low (ZAYIN) - Medium (TETH) - Common (HE) - Top (WAW) - High (ALEPH) - SPECIAL

WHAT FAILS
  * a High or SPECIAL file whose `### Consequences` never names an institution-scale payer.
    A district-sized holding that costs one tired worker has written the personnel register
    and skipped the one that matters.
  * a Low (ZAYIN) file carrying an `[**Ultimate**]`. A thing found in one room has no finisher.
    All 27 of them carried the same copied AoE line before this gate existed.

WHAT IS REPORTED, NOT FAILED
  * the middle rungs. A Common entity claiming the city, or a Top entity that never leaves the
    personnel register. Printed with counts so the owner can rule; the archive is repaired in
    tranches and a gate that fails on sixty files teaches nobody anything.

WHY IT IS NOT A DAMAGE CHECK
  `R-42` already holds the stat line to its band. This gate is about reach: who pays, who signs
  for it, and how far the paperwork travels. The Maw passes it with no hands and no eyes.
"""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from check_stat_bands import GRADE, RANK, row, tier_of  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PATHS = sorted(glob.glob(os.path.join(ROOT, 'SOMNARAK-WORLD', '*', 'SE-*.md')))

INSTITUTION = re.compile(
    r'\b(district|city|municipal|quarter|perimeter|registry|facility|facilities|station|institute|'
    r'archive|directorate|posture|order above|wing|wings|department|establishment|'
    r'ground is given up)\b', re.I)
ULTIMATE = re.compile(r'\[\*\*Ultimate\*\*\]')


def band_of(text):
    coherence, potency = row(text, 'Coherence'), row(text, 'Potency')
    if not coherence or not potency:
        return None
    r = re.search(r'\b(I{1,3}|IV|V)\b', coherence)
    g = re.search(r'([αβγδω])', potency)
    if not r or not g:
        return None
    return tier_of(RANK[r.group(1)] + GRADE[g.group(1)])


def consequences(text):
    m = re.search(r'### Consequences\n(.*?)(?=\n## |\n### )', text, re.S)
    return m.group(1) if m else ''


def is_special(text):
    return bool(re.search(r'\|\s*\*\*Special Class\*\*\s*\|[^\n]*Special Abnormality', text))


def problems(text):
    """Failures this gate refuses. Pure function; the tests drive it directly."""
    tier = band_of(text)
    if tier is None:
        return []
    bad = []
    if tier == 'ALEPH' or is_special(text):
        body = consequences(text)
        if not body.strip():
            bad.append('High/Special with no Consequences section')
        elif not INSTITUTION.search(body):
            bad.append('High/Special consequences never reach an institution-scale payer')
    if tier == 'ZAYIN' and ULTIMATE.search(text):
        bad.append('Low carries an [**Ultimate**]')
    return bad


# Over-reach is measured against the CITY, not against the institution word.
# R-43 s3 puts a wing loss on the Common rung and a written procedure on the Medium
# one, so `wing`, `registry` and `archive` appearing in a TETH or HE consequence is
# exactly on-rung. What a TETH or HE holding may not do is cost the city.
CITY_SCALE = re.compile(r'\b(city|municipal|district|perimeter|whole of Somnarak|the public)\b', re.I)


def notes(text):
    """Reported, never failed: the middle of the ladder drifting off its rung."""
    tier = band_of(text)
    body = consequences(text)
    if not tier or not body:
        return []
    out = []
    if tier in ('HE', 'TETH') and CITY_SCALE.search(body):
        out.append('%s consequences claim city scale' % tier)
    if tier == 'WAW' and not INSTITUTION.search(body):
        out.append('Top consequences never leave the personnel register')
    return out


def main():
    fail, note, counted = [], [], {}
    for path in PATHS:
        with open(path, encoding='utf-8') as fh:
            text = fh.read()
        name = os.path.basename(path)
        found = problems(text)
        if found:
            fail.append((name, found))
        for n in notes(text):
            note.append('%s  %s' % (name, n))
            counted[n.split(' consequences')[0].split(' never')[0]] = \
                counted.get(n.split(' consequences')[0].split(' never')[0], 0) + 1

    for name, found in fail:
        print('%s  %s' % (name, '; '.join(found)[:150]))
    for n in note:
        print('NOTE  %s' % n[:150])
    print('reported only: %s' % (', '.join('%s=%d' % kv for kv in sorted(counted.items())) or 'none'))
    print('consequence-register failures: %d  reported: %d' % (len(fail), len(note)))
    if fail:
        print('RESULT: FAIL')
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main())
