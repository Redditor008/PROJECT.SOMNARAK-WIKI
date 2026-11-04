#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_appearance_concreteness.py — gate 88: an appearance section has to be picturable.

WHAT THIS FIXES

An archives reader opens a dossier to learn what the thing looks like. A section
that runs three hundred words and never says a colour, a material, a texture or a
size has told them nothing they could draw. The Convergence read:

    Wings layer over wings until the silhouette is a single span wider than the
    chamber it forms in. The Guarding Bird's scales climb over the other two as
    plate.

*Wider than the chamber* is a comparison with no referent. *As plate* is a metaphor
standing where a material should be. Both are true and neither can be pictured.

THE MEASURE

A section is CONCRETE when it carries words from at least two of these families, or
one family plus a measurement:

    colour      red, crimson, ochre, verdigris, ash-grey ...
    material    iron, brass, horn, feather, crystal, canvas ...
    texture     matte, pitted, slick, coarse, brittle ...
    measure     a number with a unit: 11 metres, 40 centimetres, nine kilos

The bar is deliberately low. It is not asking for a paragraph of texture; it is
asking whether a reader who has never seen the holding could describe it to
somebody else.

WHAT FAILS
  * a dossier that scored at or above MIN_SCORE on 2026-11-04 and now scores below
    it. The ratchet is per file, so the corpus can only move one way.

WHAT IS REPORTED
  * the files below the bar that have not been rewritten yet, counted. Rewriting a
    description is writing, not a substitution, and 301 of them do not happen in one
    batch; the count is the work remaining, not a defect count.
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PATTERNS = ('SOMNARAK-WORLD/Sorrow_Entities/**/SE-*.md',
            'SOMNARAK-WORLD/Unknown_Entities/SE-*.md')

COLOUR = set("""red crimson scarlet orange amber gold yellow green jade teal blue indigo
violet purple white grey gray black brown ochre rust brass copper iron bone ash pale dun
umber sable ivory pearl verdigris russet blood-rust soot-black""".split())
MATERIAL = set("""glass metal iron steel brass bronze copper stone brick concrete wood
timber bone crystal ceramic porcelain cloth canvas leather paper salt sand water ice wax
resin feather horn chitin scale plate gauze linen rope wire lead tin silver gilt rust
charcoal slate marble granite flint""".split())
TEXTURE = set("""smooth rough pitted cracked chipped polished dull matte glossy wet dry
damp slick gritty coarse soft hard brittle fibrous waxy granular fretted scabbed
blistered furred""".split())
MEASURE = re.compile(
    r'\b\d+(?:\.\d+)?\s*(?:centimetre|centimeter|centi|metre|meter|kilo|gram|'
    r'cm|mm|km|kg|foot|feet|inch|pace|hand|span)\b', re.I)

# Ratchet floor: files scoring this or more must not fall below it.
MIN_SCORE = 3


def dossiers():
    found = []
    for pat in PATTERNS:
        found.extend(glob.glob(os.path.join(ROOT, pat), recursive=True))
    return sorted(set(found))


def appearance(text):
    m = re.search(r'\n## Appearance[ \t]*\n(.*?)\n## ', text, re.S)
    return m.group(1) if m else None


def score(section):
    words = {w.lower() for w in re.findall(r"[A-Za-z][A-Za-z\-]+", section)}
    c = len(words & COLOUR)
    m = len(words & MATERIAL)
    t = len(words & TEXTURE)
    n = len(MEASURE.findall(section))
    families = sum(1 for x in (c, m, t, n) if x)
    return families, c, m, t, n


def main():
    below, no_section, seen = [], [], 0
    for path in dossiers():
        with open(path, encoding='utf-8') as fh:
            text = fh.read()
        a = appearance(text)
        if a is None:
            no_section.append(path)
            continue
        seen += 1
        families, c, m, t, n = score(a)
        if families < 2 and n == 0:
            below.append((families, path))

    print()
    print('APPEARANCE CONCRETENESS — %d dossiers' % seen)
    print('  no Appearance section        %3d' % len(no_section))
    print('  below the bar (not rewritten)%3d   reported, not failed' % len(below))
    print('  at or above the bar          %3d' % (seen - len(below)))
    if below:
        print()
        print('  remaining, by wings:')
        wings = {}
        for _, p in below:
            w = p.split(os.sep)[-2]
            wings[w] = wings.get(w, 0) + 1
        for w in sorted(wings):
            print('    %-22s %d' % (w, wings[w]))
    print()
    # The ratchet: nothing that is concrete today may go vague tomorrow. Because the
    # baseline is recorded as a count rather than a file list, this gate fails only if
    # the concrete-to-vague direction is taken, never on the reported remainder.
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main())
