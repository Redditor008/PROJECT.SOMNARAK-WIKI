#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_work_effect.py — gate 88: a work can cost, cost nothing, or give (R-49).

The owner's instruction, 2026-11-05:

> *"Either Dmg/Neutral/Buff The Agent Who Is Doing Work On The SE And For Percentage
> Dmg 65%/ Neutral 25% / Buff 10% Of All SE"*

Before this rule every worked subject charged the worker: 158 subjects, 158 charges, 0 that cost
nothing. The row now carries one of three verdicts, read off the row itself:

    Damage    a band and the holding's own element          (`R-44` — unchanged)
    Neutral   `None` and a clause saying who pays instead
    Gift      `None`, plus a `**Work Gift**` row

WHAT FAILS
  * a subject with no `**Work Damage**` row at all, on a holding that has a work loop;
  * a `None` with no clause, or a clause shorter than eight words, or a bare `no effect`;
  * a `**Work Gift**` row on anything but the gift verdict — a gift and a damage band are one
    verdict, not two;
  * a gift missing its band, its named stat, its end, or its price;
  * a percentage printed in either row (the split lives in the rule, not in the dossier);
  * the three counts drifting off **101 / 39 / 15** of the 155 worked subjects.

    python3 tools/auditors/check_work_effect.py          # ratchet check
    python3 tools/auditors/check_work_effect.py -v       # per-dossier verdict
    python3 tools/auditors/check_work_effect.py --stats  # the split
"""
import glob
import io
import re
import sys

PATHS = sorted(glob.glob('SOMNARAK-WORLD/**/SE-*.md', recursive=True))

TYPE = re.compile(r'\*\*Entity Type\*\*\s*\|\s*([^|\n]+)')
DMG = re.compile(r'^\|\s*\*\*Work Damage\*\*\s*\|([^|\n]*)\|', re.M)
GIFT = re.compile(r'^\|\s*\*\*Work Gift\*\*\s*\|([^|\n]*)\|', re.M)
OPS = re.compile(r'^## Operational Parameters\s*$(.*?)(?=^## |\Z)', re.M | re.S)
BAND = re.compile(r'^\d+\s*[\u2013-]\s*\d+(?:\s+[A-Z][a-z]+|,\s*cycling all four)')
STATS = ('Composure', 'Resilience')

TARGET = {'damage': 101, 'neutral': 39, 'gift': 15}
RATCHET_SET = '2026-11-05'


def worked(text):
    sec = OPS.search(text)
    if not sec:
        return ''
    yield_cell = re.search(r'^\|\s*\*\*Han-Energy yield\*\*\s*\|([^|\n]*)', sec.group(1), re.M)
    if yield_cell and yield_cell.group(1).strip().startswith('\u2014'):
        return ''
    m = DMG.search(sec.group(1))
    return m.group(1).strip() if m else ''


def verdict_of(cell, gift):
    if cell.startswith('None'):
        return 'gift' if gift is not None else 'neutral'
    return 'damage'


def problems(text):
    """Failures on one dossier. Pure function; the tests drive it directly."""
    if 'Subject' not in (TYPE.search(text).group(1) if TYPE.search(text) else ''):
        return []
    sec = OPS.search(text)
    if not sec:
        return []
    cell = DMG.search(sec.group(1))
    if not cell:
        yield_cell = re.search(r'^\|\s*\*\*Han-Energy yield\*\*\s*\|([^|\n]*)', sec.group(1), re.M)
        if yield_cell and yield_cell.group(1).strip().startswith('\u2014'):
            return []
        return ['no Work Damage row on a holding with a work loop']
    val = cell.group(1).strip()
    gift = GIFT.search(sec.group(1))
    bad = []

    if '%' in val or (gift and '%' in gift.group(1)):
        bad.append('prints a percentage — the split lives in R-49, not in the cell')

    if val.startswith('None'):
        clause = re.sub(r'^None\s*[—–-]\s*', '', val).strip()
        if len(clause.split()) < 8:
            bad.append('None with no clause: the row must say who pays instead')
        if re.match(r'no effect|nothing happens|n/?a\b', clause, re.I):
            bad.append('None reads as "no effect", which is not a reading')
    elif not BAND.match(val):
        bad.append('a damage row must open with a band and the element, not %r' % val[:40])

    if gift and not val.startswith('None'):
        bad.append('a Work Gift row sits under a damage band — one verdict, not two')
    if gift:
        g = gift.group(1).strip()
        if not re.search(r'\+\d+\s*[\u2013-]\s*\d+', g):
            bad.append('gift has no band')
        if not any(s in g for s in STATS):
            bad.append('gift names no stat (%s)' % '/'.join(STATS))
        if 'for the rest of the cycle' not in g:
            bad.append('gift states no end')
        if not re.search(r'\u2014|--', g):
            bad.append('gift states no price')
    return bad


def measure():
    counts = {'damage': 0, 'neutral': 0, 'gift': 0}
    rows, fail = [], []
    for path in PATHS:
        if 'MAW_Codex' in path:
            continue
        text = io.open(path, encoding='utf-8').read()
        sec = OPS.search(text)
        if not sec or 'Subject' not in (TYPE.search(text).group(1) if TYPE.search(text) else ''):
            continue
        cell = DMG.search(sec.group(1))
        if not cell:
            if problems(text):
                fail.append((path, problems(text)))
            continue
        v = verdict_of(cell.group(1).strip(), GIFT.search(sec.group(1)))
        counts[v] += 1
        rows.append((path, v))
        bad = problems(text)
        if bad:
            fail.append((path, bad))
    return counts, fail, rows


def main(argv):
    counts, fail, rows = measure()
    if '--stats' in argv:
        total = sum(counts.values())
        print('worked subjects %d · damage %d · neutral %d · gift %d'
              % (total, counts['damage'], counts['neutral'], counts['gift']))
        for k in ('damage', 'neutral', 'gift'):
            print('  %-8s %3d  (%.1f%% — target %d)'
                  % (k, counts[k], 100.0 * counts[k] / max(total, 1), TARGET[k]))
        return 0
    if '-v' in argv:
        for path, v in rows:
            print('%-9s %s' % (v, path.split('/')[-1][:70]))
    for path, bad in fail:
        print('%s  %s' % (path.split('/')[-1][:60], '; '.join(bad)[:140]))
    drift = [(k, counts[k], TARGET[k]) for k in TARGET if counts[k] != TARGET[k]]
    for k, got, want in drift:
        print('the %s count is %d, the rule fixes %d' % (k, got, want))
    if fail or drift:
        print('work-effect failures: %d · drift: %d' % (len(fail), len(drift)))
        print('RESULT: FAIL')
        return 1
    total = sum(counts.values())
    print('damage %d · neutral %d · gift %d  of %d worked subjects  ratchet %s'
          % (counts['damage'], counts['neutral'], counts['gift'], total, RATCHET_SET))
    print('work-effect failures: 0')
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
