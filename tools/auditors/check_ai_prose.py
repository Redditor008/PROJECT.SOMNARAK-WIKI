#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_ai_prose.py — gate 90: the owner's Banned List, enforced.

The owner supplied the writing guideline this archive is held to
(`REFERENCE_SOMNARAK_WIKI/RULES/SOURCE_Unified_Narrative_Writing_Rules_for_AI.md`, §2
"The Banned List — What Never to Write"), and `R-45` §0.1 makes its twelve items binding
on every section of every dossier.

Each pattern below is quoted from that file. Where the guideline's own wording is a
sentence-shaped example ("She felt the weight of her decision pressing down on her") the
pattern is generalised to the construction that makes it a tic, not to the words alone —
so `the weight of a stone` is not flagged if the stone has a mass on file, and
`the weight of her decision` is.

WHAT FAILS (hard)
  * any of the twelve banned constructions, in any section. These are countable and the
    owner named them.

WHAT IS REPORTED (rollout)
  * the essayist openers — thesis sentence, "not X but Y", "the point is", rhetorical
    triplet — counted per section. These are the voice defect of `R-45` §0.2 and they are
    repaired by giving a section an author, which is writing and does not happen in bulk.

Usage:
    python3 tools/auditors/check_ai_prose.py            gate
    python3 tools/auditors/check_ai_prose.py --list     every hit with its file and line
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PATTERNS = ('SOMNARAK-WORLD/Sorrow_Entities/**/SE-*.md',
            'SOMNARAK-WORLD/Unknown_Entities/SE-*.md')

# (label, pattern, note) — every note cites the guideline
BANNED = [
    ('ozone',
     r'\bozone\b',
     'BANNED: "the air crackled with ozone"'),
    ('testament / reminder',
     r'\b(a testament|testament to|a reminder that|stands? as a reminder)\b',
     'BANNED: "a testament to the devastating power"'),
    ('palpable / tangible',
     r'\b(palpable|palpably|tangibly)\b',
     'BANNED: "the tension in the room was palpable"'),
    ('shiver / goosebumps',
     r'\b(shivers? (?:down|ran|up|through)|goosebumps?|goose ?flesh|a chill (?:ran|went|crawled))\b',
     'BANNED: "a shiver ran down her spine"'),
    ('echoed through / reverberated',
     r'\b(echoed through|reverberat(?:ed|ing|es))\b',
     'BANNED: "her words echoed through the empty corridor"'),
    ('symphony / dance / tapestry of',
     r'\b((?:a )?symphony of|(?:a )?dance of|(?:a )?tapestry of)\b',
     'BANNED: "a symphony of destruction"'),
    ('something shifted',
     r'\bsomething (?:shifted|changed|stirred)\b',
     'BANNED: "something shifted in the air between them"'),
    ('in that moment',
     r'\bin (?:this|that) moment\b',
     'BANNED: "in that moment, she knew everything had changed"'),
    ('little did they know',
     r'\blittle did (?:they|he|she|anyone|we) know\b',
     'BANNED: narrator bragging about the future'),
    ('dead weight metaphor',
     r'\bthe (?:weight|burden|gravity) of (?:her|his|their|its|the (?:decision|choice|moment|'
     r'truth|fact|silence|absence|loss|memory|guilt|duty|debt|grief|sorrow|responsibility))\b',
     'BANNED: "she felt the weight of her decision"'),
    ('weather as emotion',
     r'\b(rain hammered|mirroring the storm|as if the sky|the sky (?:wept|mourned|grieved))\b',
     'BANNED: weather is not about anyone\'s feelings'),
    ('exhaustive person description',
     r'\b(piercing (?:blue|green|grey|gray|emerald|azure) eyes|cascading \w+ hair|porcelain skin|'
     r'auburn hair, \w+ eyes)\b',
     'BANNED: one memorable detail, not a police report'),
]

# The voice defect of R-45 s0.2 — reported, not failed.
ESSAYIST = [
    ('thesis opener',
     r'^[A-Z][a-z]+ (?:is|are|has|have) [a-z][^.;]{0,60}\. The [A-Z]'),
    ('not X but Y',
     r'\bis not (?:merely |just |only )?[a-z][^,.;]{3,70}, but\b|\bnot (?:merely |just |only )?'
     r'[a-z][^,.;]{3,70}, (?:but|rather)\b'),
    ('"the point"',
     r'\b(?:is|was) the point\b|\bthe point is\b'),
    ('rhetorical triplet',
     r'\bWhat is \w+ is \w+\. What is \w+ is \w+\.'),
    ('announces significance',
     r'\b(?:which is exactly|that is exactly|is precisely) (?:the|what|how|why)\b'),
]


def dossiers():
    found = []
    for pat in PATTERNS:
        found.extend(glob.glob(os.path.join(ROOT, pat), recursive=True))
    return sorted(set(found))


def scan(text):
    """[(label, line_no, excerpt, note, hard)]"""
    out = []
    for i, line in enumerate(text.split('\n'), 1):
        if line.startswith(('```',)):
            continue
        stripped = re.sub(r'`[^`]*`', '', line)
        for label, pat, note in BANNED:
            for m in re.finditer(pat, stripped, re.I):
                a = max(0, m.start() - 40)
                out.append((label, i, stripped[a:m.end() + 40].strip(), note, True))
        if line.startswith(('|', '>', '#')):
            continue
        for label, pat in ESSAYIST:
            for m in re.finditer(pat, stripped, re.I | re.M):
                a = max(0, m.start() - 40)
                out.append((label, i, stripped[a:m.end() + 40].strip(),
                            'R-45 s0.2 essayist voice', False))
    return out


def main():
    listing = '--list' in sys.argv
    files = dossiers()
    hard = 0
    soft = 0
    by_label = {}
    hits = []

    for path in files:
        with open(path, encoding='utf-8') as fh:
            text = fh.read()
        for label, ln, ex, note, is_hard in scan(text):
            hits.append((path, label, ln, ex, note, is_hard))
            if is_hard:
                hard += 1
            else:
                soft += 1
            by_label.setdefault((label, is_hard), 0)
            by_label[(label, is_hard)] += 1

    print()
    print('AI PROSE — owner Banned List + R-45 s0.2 — %d dossiers' % len(files))
    print()
    if by_label:
        print('  %-34s %6s  %s' % ('item', 'hits', 'severity'))
        for (label, is_hard), n in sorted(by_label.items(), key=lambda x: (-x[0][1], -x[1])):
            print('  %-34s %6d  %s' % (label, n, 'FAIL' if is_hard else 'reported'))
        print()
    print('  banned-list hits   %3d   (FAIL above zero)' % hard)
    print('  essayist openers   %3d   (reported, R-45 s0.2)' % soft)
    print()

    if listing:
        for path, label, ln, ex, note, is_hard in sorted(hits, key=lambda h: (not h[5], h[0])):
            print('%s %s:%d  [%s]' % ('FAIL' if is_hard else '  ..', os.path.basename(path), ln, label))
            print('     %s' % ex[:150])
        print()

    if hard:
        print('RESULT: FAIL — %d banned-list hits' % hard)
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main())
