#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_relic_gauge.py — gate 93: the gauge is what is left in the hands (R-48).

The owner's direction, 2026-11-04:

> *"WHAT THE USED OF HP ON RELIC SE THAT WONT USED THE HP ... TRANSFORMS THE HP NUMBER INTO A
> MEANINGFUL GAUGE SO WHAT GOOD USED THE GAUGE THAT IS NOT USED FOR SE HP SO THINK OF THAT"*

> *"... IT STILL READ ILLOGICAL ... AND FEEL BLOATED ... I LIKE HOW THE SE TYPE IS HOW THE GAUGE
> AFFECT THE AGENT TRY TO REINVENT IT INTO A MORE LOGICAL MECHANIC"*

A relic is never suppressed, so HP has no zero to reach. But a relic is *handled*, and handling
has a cost that every dossier already states: the `**Work Damage**` row, a dose per second that
accelerates with contact time (R-47).

    Work Damage   = the rate the hands are being spent
    Sorrow Gauge  = how much of the handler is left to spend

The gauge is therefore not the relic's health. It is the reserve in the hands holding it. Full at
rest — which is why every reading in the archive read at its ceiling, and why that was never a
broken meter. At zero the relic is untouched and the hands are done.

The measure is named for the Element, i.e. what the holding puts into the handler:

    Grudge -> [Pressure]   force pushed back through the arm
    Weight -> [Load]       mass carried on the carrier's frame
    Lament -> [Depth]      grief taken down into the person
    Void   -> [Saturation] absence poured in until there is no room left

Recovery is the category's own condition and returns only half; what is not recovered is the
mechanic.

WHAT THIS CHECKS
  1. a non-breaching, non-possession relic carries no [HP];
  2. the label is one of the four measures and agrees with the `Element` row;
  3. the reading is `N/N` and the row says `at rest` — a dossier records the resting reading;
  4. the row points at `Work Damage` as the thing that spends it;
  5. three thresholds, strictly descending, the last one 0;
  6. a recovery clause, and the one its own category requires;
  7. possession, breaching relics and subjects keep [HP].

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

MEASURE = {'grudge': 'Pressure', 'weight': 'Load', 'lament': 'Depth', 'void': 'Saturation'}
MEASURES = set(MEASURE.values())

# a threshold: "Under 340", "At 0"
THRESH = re.compile(r'\b(?:under|at|below|past|from)\s+(\d+)', re.I)

# what brings the reserve back, by category (R-48 §5)
RECOVERY = {
    'Indumentum': re.compile(r'\bpiece is off\b|\boff, and what the skin', re.I),
    'Officium':   re.compile(r'\brite is closed\b', re.I),
    'Arcanum':    re.compile(r'\bwritten and filed\b', re.I),
    'Offertorium': re.compile(r'\boffering is taken back\b', re.I),
    'Object':     re.compile(r'\bboundary is re-probed\b', re.I),
    'Place':      re.compile(r'\bboundary is re-probed\b', re.I),
    'Time':       re.compile(r'\boutside the interval\b', re.I),
    'Hazard':     re.compile(r'\brotated out\b', re.I),
}

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


def category(text):
    """The holding's own category, for the recovery clause (R-48 §5)."""
    m = re.search(r'\*\*Tool Type\*\*\s*\|\s*([^|\n]+)', text)
    raw = (m.group(1) if m else '')
    if not raw.strip():
        m = re.search(r'\*\*Entity Type\*\*\s*\|\s*([^|\n]+)', text)
        raw = (m.group(1) if m else '')
    for key in ('Indumentum', 'Officium', 'Arcanum', 'Offertorium'):
        if key.lower() in raw.lower():
            return key
    low = raw.lower()
    if 'possession' in low:
        return 'Possession'
    if 'time' in low:
        return 'Time'
    if 'hazard' in low:
        return 'Hazard'
    if 'place' in low:
        return 'Place'
    return 'Object'


def problems(text):
    """What is wrong with this dossier's gauge under R-48, as a list of strings."""
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

    # 3. resting reading and the two words that say so
    r = re.match(r'^(\d+)\s*/\s*(\d+)\b', body)
    if not r:
        out.append('the row does not open with a reading')
    elif r.group(1) != r.group(2):
        out.append('reads %s/%s — a dossier records the resting reading, which is full'
                   % (r.group(1), r.group(2)))
    if not re.search(r'\bat rest\b', body, re.I):
        out.append('the row does not say the reading is taken at rest')

    # 4. the spender
    if 'work damage' not in body.lower():
        out.append('the row does not point at Work Damage as what spends it')

    # 5. three descending thresholds, last one 0
    bands = [int(x) for x in THRESH.findall(body)]
    if len(bands) < 3:
        out.append('%d threshold(s); three are required' % len(bands))
    else:
        bands = bands[:3]
        if not (bands[0] > bands[1] > bands[2]):
            out.append('thresholds must descend (%s) — a reserve is spent downward'
                       % ', '.join(map(str, bands)))
        if bands[2] != 0:
            out.append('the last threshold must be 0, not %d' % bands[2])

    # 6. recovery, and the one this category requires
    if not re.search(r'\bcomes back\b', body, re.I):
        out.append('no recovery clause')
    else:
        cat = category(text)
        rx = RECOVERY.get(cat)
        if rx and not rx.search(body):
            out.append('recovery is not the %s condition (R-48 §5)' % cat)

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
            print('  %-13s %3d' % (k, n))
        print('  %d relic dossiers' % relics)
        return 0

    for path, p in bad:
        print('%s  %s' % (os.path.relpath(path, ROOT), '; '.join(p)[:120]))

    print()
    print('RELIC GAUGE — R-48 — %d relic dossiers' % relics)
    print('  a reserve with a spender, descending bands and a half return      %3d' % good)
    print('  malformed or still on [HP]                                        %3d   ratchet %d  set %s'
          % (len(bad), RATCHET, RATCHET_SET))
    print()
    if len(bad) > RATCHET:
        print('RESULT: FAIL — %d over the ratchet of %d' % (len(bad), RATCHET))
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
