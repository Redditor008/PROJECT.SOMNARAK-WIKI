#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_threat_form.py — gate 85: a Top-or-above entity carries its band in the file, not the code.

`R-42` fixes the reading. The owner's ladder, in his words:

    Low      ZAYIN   2-3
    Medium   TETH    4-5
    Common   HE      6
    Top      WAW     7-8
    High     ALEPH   9-10
    SPECIAL  --      the terminus class, banded at High and above it

What fails, for every dossier banded Top or High:

  * a `Han Pressure [ATK]` range that opens below its band floor. A Top entity's lightest
    blow cannot be a Common entity's blow. Below Top the straddle stays a note (R-42 s3);
  * a `## Contact Record` that does not carry the R-36 reason line, so the file never says
    why a thing that does not fight is still filed this high.

What fails, additionally, for a `| **Special Class** | **Special Abnormality**` dossier:

  * a band below High — the class sits above the ladder, so a terminus scoring lower than a
    handled Top record is a contradiction in the code;
  * an ATK range opening below the High floor.

What this gate cannot do: read whether the prose is frightening. It measures the floor and the
argument. The rest of R-42 is a reading done by hand.
"""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from check_stat_bands import BANDS, GRADE, RANK, row, tier_of  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PATHS = sorted(glob.glob(os.path.join(ROOT, 'SOMNARAK-WORLD', '*', 'SE-*.md')))

BAND_NAME = {'WAW': 'Top', 'ALEPH': 'High'}
ENFORCED = ('WAW', 'ALEPH')
SPECIAL_TIER = 'ALEPH'
REASON_LINE = '> **Why this file has no combat actions.**'


def band_of(text):
    """('WAW'|'ALEPH'|..., code string) or (None, why)."""
    coherence, potency = row(text, 'Coherence'), row(text, 'Potency')
    if not coherence or not potency:
        return None, 'no Coherence/Potency row'
    r = re.search(r'\b(I{1,3}|IV|V)\b', coherence)
    g = re.search(r'([αβγδω])', potency)
    if not r or not g:
        return None, 'unreadable Coherence/Potency'
    return tier_of(RANK[r.group(1)] + GRADE[g.group(1)]), None


def atk_low(text):
    cell = row(text, r'Han Pressure \[ATK\]')
    if cell is None:
        return None
    m = re.search(r'(\d+)\s*(?:–|-|~)\s*(\d+)', cell)
    if m:
        return int(m.group(1))
    m = re.search(r'\d+', cell)
    return int(m.group()) if m else None


def problems(text):
    """Every way one dossier fails R-42. Pure function; the tests drive it directly."""
    bad = []
    tier, why = band_of(text)
    if tier is None:
        return ['%s' % why]
    special = bool(re.search(r'\|\s*\*\*Special Class\*\*\s*\|[^\n]*Special Abnormality', text))

    if special and tier != SPECIAL_TIER:
        bad.append('Special Abnormality banded %s, not High (%s)'
                   % (tier, BAND_NAME.get(tier, tier)))
    if tier not in ENFORCED:
        return bad

    name = BAND_NAME[tier]
    low = atk_low(text)
    if low is None:
        if '## Contact Record' in text:
            if REASON_LINE not in text:
                bad.append('%s with a Contact Record and no R-36 reason line' % name)
        elif '## Combat Record' not in text:
            bad.append('%s with neither a Combat Record nor a Contact Record' % name)
        return bad

    floor = BANDS[tier][2]
    if low < floor:
        bad.append('%s ATK opens at %d, under the band floor of %d' % (name, low, floor))
    return bad


def main():
    files, bad = [], []
    for path in PATHS:
        with open(path, encoding='utf-8') as fh:
            text = fh.read()
        tier, _ = band_of(text)
        if tier in ENFORCED:
            files.append(path)
        found = problems(text)
        if found:
            bad.append((os.path.basename(path), found))

    for name, found in bad:
        print('%s  %s' % (name, '; '.join(found)[:150]))
    print('Top-or-above records: %d  failing the form test: %d' % (len(files), len(bad)))
    if bad:
        print('RESULT: FAIL')
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main())
