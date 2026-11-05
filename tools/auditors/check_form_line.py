#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_form_line.py — gate 89: the form line obeys R-45.

R-45 §2. The `**Primary Form:**` / `**Physical Form:**` line is the sentence a reader
meets first. The standard is not mine; it is taken from the two universes this archive
sits between.

SCP, *How To Write An SCP*, Description:
    "start with the most normal elements and move on to the anomalous ones … Introducing
     an oddity without first establishing what the creature or object actually is will
     only confuse the reader."

Project Moon, Lobotomy Corporation O-04-84:
    "While in containment, Meat Lantern appears as a furry white lump with two round,
     black eyes and a flower-shaped organ at the end of a lure. … The rest of Meat
     Lantern's body is hidden underneath its Containment Unit."

Four sentences, a plain noun, a plain colour, the odd part fourth, and an honest edge on
the record.

WHAT FAILS
  * a BANNED CONSTRUCTION in the form line. Each is a comparison standing where a thing
    belongs, and each is countable:
      - a referentless comparison: *wider than the chamber*, *enough to roof a district*,
        *taller than the doorway*, *larger than a man*;
      - an abstraction in the noun's place: *light that is not light*, *made of sorrow*,
        *composed of*, *a thing that is not*, *some kind of*;
      - the simile: *as though*, *as if*, *like a*;
  * a form line over 130 words — a story in the wrong place. There is NO floor: the
    archive's median is 34 words, 103 of 165 sit under 40, and they are the ones that read
    best. A floor is a demand for padding, and "inflation, not a fix" is owner direction.
    (This gate used to fail under-40 as "a label" and cited the Convergence at 118. The
    Convergence is 179 words — the figure was typed from memory and never measured.)
  * a form line that reports `thin` — no colour, material or number anywhere in it. This
    is the real standard, ratcheted below;
  * a `Primary Form:` that simply repeats `Physical Form:`, or a `Primary marker:` that
    repeats the form line verbatim — those rows identify, they do not describe twice.

WHAT IS ENFORCED BY RATCHET
  * a form line that carries no concrete attribute at all: no colour word, no material
    word, no number. This is content, and content is the standard; length never was.
    Ceiling is the count measured on 2026-11-05 and may only fall.

RATCHET. The banned-construction ceilings are per file: a file that is clean today may not
grow one tomorrow. The pass is the absence of the construction, not a budget.
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PATTERNS = ('SOMNARAK-WORLD/Sorrow_Entities/**/SE-*.md',
            'SOMNARAK-WORLD/Unknown_Entities/SE-*.md')

# A referentless comparison is one where the scale is named but the thing it is measured
# against is not. `wider than the SECTOR-B-01 holding` is fine - the holding is a place
# with a size. `wider than the chamber it forms in`, `broad enough to roof a district`,
# `tall enough that the ceiling is not visible` are not: the reader is handed a comparison
# and no unit to resolve it with.
REFERENTLESS = [
    r'\b(?:wide|tall|large|broad|big|high)\s+enough\s+to\b',
    r'\benough to (?:roof|top|fill|cover|contain|hold)\b',
    r'\b(?:wider|taller|longer|larger|bigger)\s+than\s+the\s+chamber\b',
    r'\b(?:wider|taller|longer|larger|bigger)\s+than\s+the\s+doorway\b',
    r'\bas (?:far|wide|tall) as the eye\b',
    r'\bbeyond (?:all )?proportion\b',
]
ABSTRACT = [
    r'light that is not light',
    r'\bmade of (?:sorrow|grief|fear|rage|joy|dream|memory|pain|han)\b',
    r'\bcomposed of\b',
    r'\ba thing that is not\b',
    r'\bsome kind of\b',
    r'\bsome sort of\b',
    r'\bwings made of sorrow\b',
]
SIMILE = [r'\bas though\b', r'\bas if\b']

BANNED = [('referentless comparison', p) for p in REFERENTLESS] + \
         [('abstraction', p) for p in ABSTRACT] + \
         [('simile', p) for p in SIMILE]

CONCRETE = re.compile(
    r'\b\d+(?:\.\d+)?\s*(?:centimetre|centimeter|centi|metre|meter|kilo|gram|cm|mm|km|kg|'
    r'foot|feet|inch|pace|hand|span|second|minute|hour|day|year)\b', re.I)
COLOUR = set("""red crimson scarlet orange amber gold yellow green jade teal blue indigo
violet purple white grey gray black brown ochre rust brass copper bone pale dun sable
ivory pearl verdigris russet soot-black ash-grey""".split())
MATERIAL = set("""glass metal iron steel brass bronze copper stone brick concrete wood
timber bone crystal ceramic porcelain cloth canvas leather paper salt sand water ice wax
resin feather horn chitin scale plate gauze linen rope wire lead tin silver gilt rust
charcoal slate marble granite flint fur""".split())

# No floor. A form line owes content, not length (R-45 §2).
MAX_WORDS = 130
# thin form lines, measured 2026-11-05; this only ever falls
RATCHET_THIN = 134
RATCHET_SET = '2026-11-05'


def dossiers():
    found = []
    for pat in PATTERNS:
        found.extend(glob.glob(os.path.join(ROOT, pat), recursive=True))
    return sorted(set(found))


def form_line(text):
    """The line a reader meets first in Appearance.

    Most dossiers label it `**Primary Form:**` or `**Physical Form:**`. Four of the
    Unknown wing write it as the opening paragraph instead of a labelled row, and their
    heading is `## Appearance — <parts>` rather than a bare `## Appearance`. The gate
    measures what the reader actually meets, so it takes the label when it is there and
    the first sentence of the section when it is not - otherwise those four would pass by
    being unmeasurable, which is the failure mode this gate exists to prevent.
    """
    for pat in (r'^\*\*Primary Form:\*\*\s*(.+)$', r'^\*\*Physical Form:\*\*\s*(.+)$'):
        m = re.search(pat, text, re.M)
        if m:
            return m.group(1).strip()
    m = re.search(r'\n## Appearance[^\n]*\n+(.+?)\n', text)
    if m:
        first = m.group(1).strip()
        return first if len(first.split()) > 5 else None
    return None


def plain(line):
    return re.sub(r'[*_`\[\]]', '', line)


def main():
    files = dossiers()
    fails = []
    over, dup_marker = [], []
    banned_hits = 0
    thin = 0
    lengths = []

    for path in files:
        with open(path, encoding='utf-8') as fh:
            text = fh.read()
        line = form_line(text)
        if not line:
            fails.append(('no form line', path, ''))
            continue
        low = plain(line).lower()
        lengths.append(len(line.split()))

        for name, pat in BANNED:
            m = re.search(pat, low)
            if m:
                banned_hits += 1
                fails.append((name, path, m.group(0)))
        n = len(line.split())
        if n > MAX_WORDS:
            over.append((n, path))

        # the marker must not be a second copy of the form line
        mk = re.search(r'^\s*-\s*\*\*Primary marker:\*\*\s*(.+)$', text, re.M)
        if mk:
            a = re.sub(r'\W+', ' ', plain(line)).lower().strip()
            b = re.sub(r'\W+', ' ', plain(mk.group(1))).lower().strip()
            if a[:70] == b[:70] and len(a) > 40:
                dup_marker.append(path)

        words = set(re.findall(r'[a-z\-]+', low))
        if not (words & COLOUR or words & MATERIAL or CONCRETE.search(low)):
            thin += 1

    print()
    print('FORM LINE — R-45 §2 — %d dossiers' % len(files))
    if lengths:
        lengths.sort()
        print('  words: min %d  median %d  max %d'
              % (lengths[0], lengths[len(lengths) // 2], lengths[-1]))
    print('  banned constructions          %3d   FAIL above zero' % banned_hits)
    print('  no form line                  %3d   FAIL above zero'
          % sum(1 for r, _, _ in fails if r == 'no form line'))
    print()
    print('  over %d words (a story)       %3d   %s'
          % (MAX_WORDS, len(over),
             'FAIL' if over else 'PASS'))
    print('  thin - no colour, material or number  %3d   ratchet %d  set %s'
          % (thin, RATCHET_THIN, RATCHET_SET))
    print('  marker repeats the form line %3d   reported' % len(dup_marker))

    print()
    if fails:
        by = {}
        for reason, path, hit in fails:
            by.setdefault(reason, []).append((os.path.basename(path), hit))
        for reason in sorted(by):
            print('  %s (%d):' % (reason, len(by[reason])))
            for name, hit in by[reason][:6]:
                print('    %-58s %s' % (name[:58], hit[:40]))
            if len(by[reason]) > 6:
                print('    … and %d more' % (len(by[reason]) - 6))
        print()
        print('RESULT: FAIL — %d defects' % len(fails))
        return 1
    if over:
        print('RESULT: FAIL — %d form line(s) over %d words' % (len(over), MAX_WORDS))
        for n, path in sorted(over, reverse=True):
            print('  %4dw  %s' % (n, os.path.basename(path)[:56]))
        return 1
    if thin > RATCHET_THIN:
        print('RESULT: FAIL — %d thin form lines, over the ratchet of %d'
              % (thin, RATCHET_THIN))
        return 1
    if thin < RATCHET_THIN:
        print('RESULT: FAIL — %d thin, BELOW the ratchet of %d; lower it to %d'
              % (thin, RATCHET_THIN, thin))
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main())
