#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_relic_interaction_damage.py — gate 92: a relic charges by the second (R-47).

The owner's direction, 2026-11-04:

> *"Also Do Relic SE Need HP, ATK Still Can But It Interaction Dmg As In The Longer The Agent
> Used/Equip/Hold It The Higher The Dmg Taken And The Dmg Is x Dmg/x Second/ect.[Based Of What
> Category Of Relic It Is]"*

Three rules, three checks:

HP — every relic carries a Sorrow Gauge [HP]. It is the containment meter, not a hit point.

ATK — **no dossier carries an ATK row**, relic or subject. A relic does not strike; its
offensive value lives in the `-B` weapon record of its M.A.W. set.

INTERACTION DAMAGE — a relic's Work Damage row is a **dose**, not a session. It states
`X <element> / N s`, it states that the clock tightens, and it states what resets it.
The base clock is set by the relic category:

    I-Relic (Indumentum)  — worn on the body       — 10 s
    O-Relic (Officium)    — a rite performed       — 15 s
    A-Relic (Arcanum)     — consulted for an answer— 20 s
    O-Relic (Offertorium) — a votive left in place — 30 s

    python3 tools/auditors/check_relic_interaction_damage.py       # ratchet check
    python3 tools/auditors/check_relic_interaction_damage.py -v    # per-dossier listing
    python3 tools/auditors/check_relic_interaction_damage.py --stats
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
TOOLTYPE = re.compile(r'\*\*Tool Type\*\*\s*\|\s*([^|]+)\|')
WORK_DAMAGE = re.compile(r'^\|\s*\*\*Work Damage\*\*\s*\|\s*([^\n]*?)\s*\|\s*$', re.M)
ATK_ROW = re.compile(r'^\|\s*\*\*ATK\*\*\s*\|', re.M)
GAUGE = re.compile(r'^\|\s*\*\*Sorrow Gauge \[HP\]\*\*\s*\|', re.M)

# --- the dose ---------------------------------------------------------------
# a clock: `/ 10 s`, `per 10 s`, `every 10 s`
CLOCK = re.compile(r'(?:/|\bper\b|\bevery\b)\s*\d+(?:\.\d+)?\s*s\b', re.I)
# the clock must be seen to tighten
TIGHTENS = re.compile(r'\bhalv(?:e|es|ed|ing)\b|\bhalf\b|\bshorten\w*\b|\btighten\w*\b|'
                      r'\bdoubl(?:e|es|ed|ing)\b|\bspeeds?\b|\baccelerat\w*\b', re.I)
# a minute horizon
MINUTE = re.compile(r'\bminute', re.I)
# the reset
RESET = re.compile(r'\breset\w*\b|\bcomes? off\b|\bput (?:it )?down\b|\btaken off\b|'
                   r'\btake it off\b|\blet(?:s|ting)? go\b|\bbreaks? contact\b|\breleased\b|'
                   r'\bremoved\b|\bstops? (?:the|when)\b', re.I)

# base clock per relic category (R-47 §2)
CATEGORY_CLOCK = (
    ('Indumentum', 10),
    ('Officium', 15),
    ('Arcanum', 20),
    ('Offertorium', 30),
)

# A relic with no Tool Type — a Place, a Time, a Hazard — is not a tool you pick up.
# Its clock is read off Entity Type, which every dossier files. R-47 s2.
ENTITY_CLOCK = (
    ('Possession', 10),
    ('Hazard', 15),
    ('Time', 20),
    ('Object', 30),
    ('Place', 30),
)

# Dossiers allowed to stand before the rollout: this only ever falls.
RATCHET = 0
RATCHET_SET = '2026-11-04'


def dossiers():
    found = []
    for pat in DOSSIERS:
        found.extend(glob.glob(os.path.join(ROOT, pat), recursive=True))
    return sorted(set(found))


def is_relic(text):
    m = TYPE.search(text)
    if not m:
        return False
    return 'Subject' not in m.group(1)


def category(text):
    m = TOOLTYPE.search(text)
    if m:
        raw = m.group(1)
        for name, clock in CATEGORY_CLOCK:
            if name.lower() in raw.lower():
                return name, clock
    # no Tool Type: the Entity Type sets the clock (R-47 s2)
    m = TYPE.search(text)
    if m:
        raw = m.group(1)
        for name, clock in ENTITY_CLOCK:
            if name.lower() in raw.lower():
                return name, clock
    return None, None


def problems(text):
    """What is wrong with this dossier under R-47, as a list of strings."""
    out = []
    if ATK_ROW.search(text):
        out.append('ATK row — a relic does not strike; the value belongs in its -B record')

    if not is_relic(text):
        return out

    if not GAUGE.search(text):
        out.append('no Sorrow Gauge [HP] row — the containment meter is not optional')

    m = WORK_DAMAGE.search(text)
    if not m:
        out.append('no Work Damage row')
        return out

    row = m.group(1)
    if not CLOCK.search(row):
        out.append('no clock: the row gives a session range, not a dose per second')
        return out
    if not (TIGHTENS.search(row) or MINUTE.search(row)):
        out.append('no acceleration: the clock never tightens')
    if not RESET.search(row):
        out.append('no reset: the row does not say what stops it')

    name, clock = category(text)
    if clock:
        got = [float(x) for x in re.findall(r'(?:/|\bper\b|\bevery\b)\s*(\d+(?:\.\d+)?)\s*s\b',
                                            row, re.I)]
        if got and got[0] != clock:
            out.append('clock is %gs; a %s opens at %ds'
                       % (got[0], name, clock))
    return out


def main(argv):
    files = dossiers()
    relics, bad, ok = 0, [], 0
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
            ok += 1

    if '--stats' in argv:
        cats = {}
        for path in files:
            with io.open(path, encoding='utf-8') as fh:
                text = fh.read()
            if not is_relic(text):
                continue
            name, clock = category(text)
            cats[name or '(unfiled)'] = cats.get(name or '(unfiled)', 0) + 1
        for name, n in sorted(cats.items(), key=lambda x: -x[1]):
            print('  %-14s %3d' % (name, n))
        print('  %d relic dossiers' % relics)
        return 0

    for path, p in bad:
        rel = os.path.relpath(path, ROOT)
        print('%s  %s' % (rel, '; '.join(p)[:120]))

    print()
    print('RELIC INTERACTION DAMAGE — R-47 — %d relic dossiers' % relics)
    print('  carrying a per-second dose with a tightening clock and a reset  %3d' % ok)
    print('  still on a session range                                          %3d   ratchet %d  set %s'
          % (len(bad), RATCHET, RATCHET_SET))
    print()
    if len(bad) > RATCHET:
        print('RESULT: FAIL — %d over the ratchet of %d' % (len(bad), RATCHET))
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
