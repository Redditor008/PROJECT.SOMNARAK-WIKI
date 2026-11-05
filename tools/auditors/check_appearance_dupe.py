#!/usr/bin/env python3
"""
tools/auditors/check_appearance_dupe.py

An appearance section describes what is seen. A mechanic belongs in the effect
field. When the same sentence sits in both, one of them is inflation.

THE DEFECT, CONCRETELY
    ### Appearance
    The Dancing Plate is a fitted harness of Grudge Han-iron plates ... The plate
    absorbs direct Grudge pressure while a wearer follows a declared finite
    movement route.

    ### Passive effect— *Moving Guard*
    The Plate absorbs direct Grudge pressure while a wearer follows a declared,
    finite movement route.

The ability was pasted into the description. Four files did this; the sentence was
never about the object's look, so a reader learns nothing from meeting it twice.

WHY IT MATTERS
  R-39 says a fix must write rather than cut — but it also says the opposite when
  expansion would be illogical, and inventing a visual for an invisible mechanic is
  illogical. The four were rewritten to say the one thing the appearance section can
  truthfully say about an invisible effect: that nothing on the object advertises it,
  which is itself a visible fact (the marks stay plain, the ridges keep their points),
  and to hand the reader to the field where the mechanic is filed.

WHAT IS NOT FLAGGED
  * A short phrase reused in passing ("Grudge pressure") — sentences are compared at
    8+ words, normalised.
  * Summary sections that recap detail by design (FULL-SET RESONANCE, SUBJECT,
    WITNESS RECORD). Only the Appearance↔effect pair is scored here.

Ceiling 0, ratcheted both ways.
"""

import collections
import glob
import io
import os
import re
import sys

WORLD = 'SOMNARAK-WORLD/**/*.md'
RATCHET = 0

EFFECT = re.compile(r'passive effect|ability|effect file|signature', re.I)
HEADING = re.compile(r'^#{2,4}\s+(.+)')


def sections(text):
    cur = '(top)'
    out = []
    for line in text.split('\n'):
        m = HEADING.match(line)
        if m:
            cur = re.sub(r'\s+', ' ', m.group(1)).strip()
            continue
        out.append((cur, line))
    return out


def sentences(line):
    parts = re.split(r'(?<=[.!?])\s+(?=[A-Z“"(])', line.strip())
    return [p.strip() for p in parts
            if p.strip() and p.strip()[0].isupper()
            and p.strip().endswith(('.', '!', '?', '.”', '."'))
            and len(p.split()) >= 8]


def norm(s):
    s = s.lower().replace('\u2019', "'")
    return ' '.join(re.sub(r'[^a-z0-9 ]', ' ', s).split())


def scan(path):
    """Return [(effect_section, sentence)] duplicated into Appearance."""
    where = collections.defaultdict(set)
    text = {}
    with io.open(path, encoding='utf-8') as fh:
        body = fh.read()
    for name, line in sections(body):
        if line.strip().startswith('|'):
            continue
        for s in sentences(line):
            where[norm(s)].add(name)
            text[norm(s)] = s
    out = []
    for key, names in where.items():
        if len(names) < 2:
            continue
        app = [n for n in names if n.lower().startswith('appearance')]
        eff = [n for n in names if EFFECT.search(n) and not n.lower().startswith('appearance')]
        if app and eff:
            out.append((eff[0], text[key]))
    return out


def main(argv):
    verbose = '-v' in argv or '--verbose' in argv
    defects = []
    files = sorted(glob.glob(WORLD, recursive=True))
    for path in files:
        for effect, sentence in scan(path):
            defects.append((path, effect, sentence))

    print(f'APPEARANCE DUPLICATION — {len(files)} files')
    if verbose:
        for path, effect, sentence in defects:
            print(f'      {path:70} [{effect[:26]}] {sentence[:80]}')
    print(f'  ability-in-appearance  {len(defects)}   ceiling {RATCHET}')
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
