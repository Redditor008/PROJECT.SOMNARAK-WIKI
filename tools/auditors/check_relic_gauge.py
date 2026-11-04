#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_relic_gauge.py — gate 93: a gauge must change an instruction (R-48).

The owner's direction, 2026-11-04:

> *"WHAT THE USED OF HP ON RELIC SE THAT WONT USED THE HP, YES POSSESSION CAN USED THE HP SO
> FOR RELIC SE THAT WILL NEVER BREACH FIRST ERASE THE [HP] AND TRANSFORMS THE HP NUMBER INTO A
> MEANINGFUL GAUGE SO WHAT GOOD USED THE GAUGE THAT IS NOT USED FOR SE HP SO THINK OF THAT"*

`HP` means: a number, it can reach zero, at zero the thing stops. A relic that never breaches is
never suppressed, so its `[HP]` has no referent — it is a number that looks like information.

A gauge earns its ink at a band boundary that changes an instruction. So a non-breaching relic's
gauge is a **state meter**, named for what it is made of, with three ascending bands and a
different instruction at each.

    Element Grudge  -> [Pressure]   force against a boundary
    Element Weight  -> [Load]       mass on a support
    Element Lament  -> [Depth]      how far down the grief has gone
    Element Void    -> [Saturation] how much absence has been poured in

Possession keeps [HP] (the bearer is what falls). Breaching relics keep [HP] (suppression is what
it is for). Subjects keep it too.

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
GAUGE = re.compile(r'^\|\s*\*\*Sorrow Gauge \[([^\]]+)\]\*\*\s*\|\s*([^\n]*?)\s*\|\s*$', re.M)

MEASURE = {
    'grudge': 'Pressure',
    'weight': 'Load',
    'lament': 'Depth',
    'void': 'Saturation',
}
MEASURES = set(MEASURE.values())

# three ascending band thresholds: under / below / from / above / at  + a number
BAND = re.compile(r'\b(?:under|below|from|above|at|past|over)\s+(\d+(?:\.\d+)?)', re.I)

# this only ever falls
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
    """A relic that can breach keeps [HP]: suppression is what HP is for."""
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


def problems(text):
    """What is wrong with this dossier under R-48, as a list of strings."""
    m = GAUGE.search(text)
    if not m:
        return ['no Sorrow Gauge row']

    label, body = m.group(1).strip(), m.group(2)

    if keeps_hp(text):
        if label != 'HP':
            return ['this holding is suppressed-or-borne and must keep [HP]; it reads [%s]'
                    % label]
        return []

    out = []
    if label == 'HP':
        out.append('[HP] on a holding that never breaches — the number has no referent')
        return out

    if label not in MEASURES:
        out.append('[%s] is not one of the four measures (%s)'
                   % (label, ', '.join(sorted(MEASURES))))
        return out

    el = element_of(text)
    if el and MEASURE[el] != label:
        out.append('Element is %s, so the gauge is [%s]; this reads [%s]'
                   % (el.capitalize(), MEASURE[el], label))

    # a reading clause: a verb of reading, or the phrase that locates the number
    if not re.search(r'\bread(?:s|ing)?\b|\btaken\b|\bmeasured?\b|\bplumb|\bnumber\b|\breading\b|'
                     r'\bfull at\b|\bcount(?:s|ed)?\b|\bweigh(?:s|ed)?\b|\btimed?\b', body, re.I):
        out.append('the row does not say what it reads, or where')

    bands = [float(x) for x in BAND.findall(body)]
    if len(bands) < 3:
        out.append('%d band threshold(s); three ascending bands are required' % len(bands))
    elif bands != sorted(bands):
        out.append('band thresholds are not ascending (%s)'
                   % ', '.join('%g' % b for b in bands))
    elif len(set(bands)) < 3:
        out.append('three bands but only %d distinct thresholds' % len(set(bands)))
    return out


def main(argv):
    files = dossiers()
    relics, converted, bad = 0, 0, []
    for path in files:
        with io.open(path, encoding='utf-8') as fh:
            text = fh.read()
        if not is_relic(text):
            continue
        relics += 1
        p = problems(text)
        if p:
            if not keeps_hp(text):
                bad.append((path, p))
        else:
            if not keeps_hp(text):
                converted += 1

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
            print('  %-12s %3d' % (k, n))
        print('  %d relic dossiers' % relics)
        return 0

    for path, p in bad:
        rel = os.path.relpath(path, ROOT)
        print('%s  %s' % (rel, '; '.join(p)[:120]))

    print()
    print('RELIC GAUGE — R-48 — %d relic dossiers' % relics)
    print('  carrying a state meter with three bands and an instruction at each  %3d'
          % converted)
    print('  still on [HP] or on a malformed gauge                                  %3d   ratchet %d  set %s'
          % (len(bad), RATCHET, RATCHET_SET))
    print()
    if len(bad) > RATCHET:
        print('RESULT: FAIL — %d over the ratchet of %d' % (len(bad), RATCHET))
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
