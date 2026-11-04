#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_relic_gauge.py — gate 93: the charge (R-48).

The owner's direction, 2026-11-04:

> *"WHAT IF YOU DIVIDED EXPLANATION AND THE TABLE IN TWO AND ALSO REINVENT WHAT THE NUMBER IS FOR
> RELIC SE ... AND SO EACH TIER OF THE SE HAVE BRAND NEW INVENTED GAUGE NUMBER AND WHAT IF THIS
> GAUGE IS PUNISHMENT + LIMIT OF USING IT ... THERE SHOULD BE HARD LIMIT THAT IS UNIVERSAL FOR ALL
> RELIC SE, AND ... A CONSEQUENCE OF TRYING TO USED IT WHEN IT NOT YET 'RECHARGE' AND THE RECHARGE
> RATE CAN WORK LIKE ... THERE IS A LINE FROM MAX TO 00"*

THE CHARGE
    The gauge is the relic's charge and it is both the punishment and the limit. The punishment,
    because the number is the size of what the thing takes out of the holder. The limit, because
    at 000 the relic is spent and will not take a hand.

THE NUMBER IS THE TIER'S
    ZAYIN 240 · TETH 420 · HE 660 · WAW 880 · ALEPH 1,080. No file chooses its own. Every figure
    sits inside the band check_stat_bands.py already enforces.

THE UNIVERSAL WALL
    Sixty seconds of contact. Not tiered, not categorised, not negotiable. The thing spends its
    whole length in that minute, so a larger charge is a heavier draw, never a longer leash.

THE TWO LINES
    down   660 ----------- 60 s ----------- 000
    up     000 -- 1 min -- 066 -- 2 min -- 132 ... -- 10 min -- 660

THE CONSEQUENCE
    Taken up before the brim: the Work Damage clock resumes where it stopped, it does not start
    over. Taken up at 000: the first dose lands at once and the refill restarts from nothing.

THE DIVISION
    The table cell is data — charge, state, wall, refill — and may not run past 110 characters.
    The mechanic is a paragraph outside the table. A cell that has to be read twice is a
    paragraph in the wrong place.

    python3 tools/auditors/check_relic_gauge.py       # ratchet check
    python3 tools/auditors/check_relic_gauge.py -v    # per-dossier listing
    python3 tools/auditors/check_relic_gauge.py --stats
"""
import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOSSIERS = ('SOMNARAK-WORLD/Sorrow_Entities/**/SE-*.md',
            'SOMNARAK-WORLD/Unknown_Entities/SE-*.md')

TYPE = re.compile(r'\*\*Entity Type\*\*\s*\|\s*([^|]+)\|')
ELEMENT = re.compile(r'^\|\s*\*\*Element\*\*\s*\|\s*([^|\n]+)', re.M)
COHERENCE = re.compile(r'^\|\s*\*\*Coherence\*\*\s*\|\s*([^|\n]+)', re.M)
POTENCY = re.compile(r'^\|\s*\*\*Potency\*\*\s*\|\s*([^|\n]+)', re.M)
GAUGE = re.compile(r'^\|\s*\*\*Sorrow Gauge \[([^\]]+)\]\*\*\s*\|\s*([^\n]*?)\s*\|\s*$', re.M)
CHARGE = re.compile(r'^\*\*Charge\.\*\*\s*(.+?)(?:\n\n|\Z)', re.M | re.S)

MEASURE = {'grudge': 'Pressure', 'weight': 'Load', 'lament': 'Depth', 'void': 'Saturation'}
MEASURES = set(MEASURE.values())

# The tier invents the number. Nowhere else.
CHARGE_OF_TIER = {'ZAYIN': 240, 'TETH': 420, 'HE': 660, 'WAW': 880, 'ALEPH': 1080}

RANK = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5}
GRADE = {'α': 1, 'β': 2, 'γ': 3, 'δ': 4, 'ω': 5}

CELL_MAX = 110

RATCHET = 0
RATCHET_SET = '2026-11-04'


def dossiers():
    found = []
    for pat in DOSSIERS:
        found.extend(glob.glob(os.path.join(ROOT, pat), recursive=True))
    return sorted(set(found))


def entity_type(text):
    m = TYPE.search(text)
    return m.group(1) if m else ''


def is_subject(text):
    return 'Subject' in entity_type(text)


def is_relic(text):
    t = entity_type(text)
    return bool(t) and 'Subject' not in t


def is_possession(text):
    return 'possession' in entity_type(text).lower()


def is_breaching(text):
    t = entity_type(text).lower()
    return 'can breach' in t or 'breach annexes' in t or 'recorded breach' in t


def keeps_hp(text):
    return is_subject(text) or is_possession(text) or is_breaching(text)


def element_of(text):
    m = ELEMENT.search(text)
    if not m:
        return None
    raw = m.group(1).strip().lower()
    for key in MEASURE:
        if key in raw:
            return key
    return None


def tier_of(text):
    c, p = COHERENCE.search(text), POTENCY.search(text)
    if not (c and p):
        return None
    r = re.search(r'\b(I{1,3}|IV|V)\b', c.group(1))
    g = re.search(r'([αβγδω])', p.group(1))
    if not (r and g):
        return None
    score = RANK[r.group(1)] + GRADE[g.group(1)]
    return 'ZAYIN' if score <= 3 else 'TETH' if score <= 5 else 'HE' if score == 6 \
        else 'WAW' if score <= 8 else 'ALEPH'


def problems(text):
    m = GAUGE.search(text)
    if not m:
        return ['no Sorrow Gauge row']

    label, body = m.group(1).strip(), m.group(2).strip()

    if keeps_hp(text):
        if label != 'HP':
            return ['this holding is suppressed or borne by a person and must keep [HP]; '
                    'it reads [%s]' % label]
        return []

    out = []
    if label == 'HP':
        return ['[HP] on a holding that is never suppressed — the number has no zero to reach']

    if label not in MEASURES:
        return ['[%s] is not one of the four measures (%s)'
                % (label, ', '.join(sorted(MEASURES)))]

    el = element_of(text)
    if el and MEASURE[el] != label:
        out.append('Element is %s, so the gauge is [%s]; this reads [%s]'
                   % (el.capitalize(), MEASURE[el], label))

    # the division: the cell is data, not prose
    if len(body) > CELL_MAX:
        out.append('the cell runs to %d characters — the table is data, the mechanic is the '
                   'paragraph under it' % len(body))

    tier = tier_of(text)
    want = CHARGE_OF_TIER.get(tier)
    r = re.match(r'^\*\*(\d+)\s+of\s+(\d+)\*\*', body)
    if not r:
        out.append('the cell does not open with `000 of <length>` in bold')
    else:
        if want is not None and int(r.group(2)) != want:
            out.append('ceiling %s but %s carries %d' % (r.group(2), tier, want))
        if int(r.group(1)) != 0:
            out.append('reads %s/%s — a relic at rest reads 000; the gauge fills, it does '
                       'not drain' % (r.group(1), r.group(2)))

    for phrase, why in (('ready', 'the settled state'),
                        ('60 s', 'the sixty-second wall'),
                        ('recharge 10 min', 'the recharge time')):
        if phrase not in body.lower():
            out.append('the cell does not carry %s' % why)

    # a settled relic reads at the bottom, not in a 35-50% band
    s = re.search(r'\*\*Starting Sorrow Gauge\*\*\s*\|\s*([^|\n]+)', text)
    if s and not re.match(r'\s*0{2,3}\b', s.group(1)):
        out.append('Starting Sorrow Gauge reads %r — a settled relic reads 000'
                   % s.group(1).strip()[:40])

    # the standing section (R-48 §6)
    sec = re.search(r'^## The Charge\n(.*?)(?=\n## |\Z)', text, re.M | re.S)
    if not sec:
        out.append('no `## The Charge` section — the mechanic is not stated anywhere')
        return out
    body_s = sec.group(1)
    low = body_s.lower()

    if want is not None and ('**%d**' % want) not in body_s:
        out.append('the Charge section does not state the %s wall (%d)' % (tier, want))
    for phrase, why in (('sixty seconds', 'the sixty-second fill'),
                        ('at rest', 'the resting reading'),
                        ('tenth of the length', 'the run-down rate'),
                        ('work damage', 'the chain to Work Damage')):
        if phrase not in low:
            out.append('the Charge section does not state %s' % why)
    if 'what it takes' not in low:
        out.append('the Charge section does not say what it takes out of the handler')

    # the paragraph it replaced must not linger beside it
    if CHARGE.search(text):
        out.append('a `**Charge.**` paragraph is still in the table area — the section '
                   'replaced it')

    return out


def main(argv):
    files = dossiers()
    relics, good, bad = 0, 0, []
    for path in files:
        with io.open(path, encoding='utf-8') as fh:
            text = fh.read()
        if not is_relic(text):
            continue
        relics += 1
        p = problems(text)
        if p:
            bad.append((path, p))
        else:
            good += 1

    if '--stats' in argv:
        cats = {}
        for path in files:
            with io.open(path, encoding='utf-8') as fh:
                text = fh.read()
            if not is_relic(text):
                continue
            m = GAUGE.search(text)
            key = ('[%s]' % m.group(1)) if m else '(none)'
            cats[key] = cats.get(key, 0) + 1
        for k, n in sorted(cats.items(), key=lambda x: -x[1]):
            print('  %-14s %3d' % (k, n))
        tiers = {}
        for path in files:
            with io.open(path, encoding='utf-8') as fh:
                text = fh.read()
            if not is_relic(text) or keeps_hp(text):
                continue
            tiers[tier_of(text)] = tiers.get(tier_of(text), 0) + 1
        for k in ('ZAYIN', 'TETH', 'HE', 'WAW', 'ALEPH'):
            print('  %-6s charge %-5s %3d dossiers'
                  % (k, CHARGE_OF_TIER[k], tiers.get(k, 0)))
        print('  %d relic dossiers, %d convert' % (relics, sum(tiers.values())))
        return 0

    for path, p in bad:
        print('%s  %s' % (os.path.relpath(path, ROOT), '; '.join(p)[:130]))

    print()
    print('RELIC CHARGE — R-48 — %d relic dossiers' % relics)
    print('  tier charge, 110-char data cell, mechanic outside the table     %3d' % good)
    print('  malformed, off-tier, or still on [HP]                            %3d   ratchet %d  set %s'
          % (len(bad), RATCHET, RATCHET_SET))
    print()
    if len(bad) > RATCHET:
        print('RESULT: FAIL — %d over the ratchet of %d' % (len(bad), RATCHET))
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
