#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_tale_register.py — gate 91: a Tale is a Normalised Story or a Fairy Tale (R-46).

The owner's direction: *"TALE HAVE TWO CATEGORY OF WRITING NORMALIZE STORY AND FAIRY TALE
TYPE OF WRITING."*

`이야기 (Narratio) — The Tale` is written in exactly one of two registers. This gate reads
the opening and the body of every Tale and decides which, on markers that are structural
rather than stylistic, then fails on any Tale that reads as neither.

NORMALISED STORY — a filed account
    * a filing header: `> **Filed by:**`, `> **Report of:**`, `> **From the desk of:**`
    * a date or year (Year 4,2xx)
    * a named institution doing something (Registry, Wardens' Office, Directorate, Gardens)
    * a person with a post

FAIRY TALE — a folktale
    * an opening formula: Once / There was / Before there was / Long ago / In the time before
    * roles rather than names (the woodcutter, the girl, the third son)
    * the folk 'and' chain
    * a closing turn: and it is still there / and so it is to this day

NEITHER — the essay
    * a thesis sentence ('X is Y, and the Y has weight')
    * a negation-and-correction ('but X is only the largest version of a smaller truth')
    * a rhetorical triplet ('What is spent is spent. What is wasted is wasted.')
    * an announcement of significance ('The crack is the point.')

WHAT FAILS
  * a Tale with no register marker at all — the essay
  * a Tale carrying an essay construction anywhere in it, whatever its opening

WHAT IS REPORTED
  * the split between the two registers, and the Tales whose opening is neither but whose
    body is clean (reported so the count is visible; a Tale needs an opening to be read).
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PATTERNS = ('SOMNARAK-WORLD/Sorrow_Entities/**/SE-*.md',
            'SOMNARAK-WORLD/Unknown_Entities/SE-*.md')

NARRATIO = re.compile(r'\n## 이야기 \(Narratio\)[^\n]*\n(.*?)\n## ', re.S)

FILING = re.compile(r'>\s*\*\*(Filed by|Report of|From the desk of|Submitted by|Record of)\*\*', re.I)
YEAR = re.compile(r'\bYear 4,\d{3}\b|\bYear 4,\d{2}\b')
INSTITUTION = re.compile(
    r"\b(Registry|Public Record Office|Wardens?'? Office|the Directorate|the Gardens|"
    r"Collectors?'? office|Debt Registry|Archive|Extraction|Containment)\b")
POST = re.compile(r'\b(Clerk|Archivist|Warden|Keeper|Collector|Supervisor|Officer|'
                  r'Inspector|Secretary|Lead|Director)\b')

FAIRY_OPEN = re.compile(
    r'^(Once\b|There was\b|There were\b|Before there was\b|Before the city\b|'
    r'Long ago\b|In the time before\b|In those years\b|When the city was young\b)', re.M)
ROLE = re.compile(r'\b(the woodcutter|the girl|the boy|the mother|the father|the old woman|'
                  r'the old man|the third son|the youngest|the king|the child who)\b', re.I)
FOLK_CHAIN = re.compile(r'\band\b[^.]{5,60}\band\b[^.]{5,60}\band\b')
CLOSING_TURN = re.compile(r'\b(and it is still there|and so it is to this day|'
                          r'and it has not stopped|and there it stayed)\b', re.I)

ESSAY = [
    ('thesis opener',
     r'^[A-Z][a-z]+ (?:is|are|has|have) [a-z][^.;]{0,60}\. The [A-Z]'),
    ('negation-and-correction',
     r'\b(?:but|though) [a-z][^,.;]{2,50} is only the (?:largest|smallest|first|last) '
     r'(?:version|form|part) of\b'),
    ('rhetorical triplet',
     r'\bWhat is \w+ is \w+\. What is \w+ is \w+\.'),
    ('announces significance',
     r'\b(?:is|was) the point\b|\bthe point is\b'),
    ('abstract subject + modal',
     r'^(?:The )?(?:grief|sorrow|anxiety|fear|memory|silence|weight) [a-z]+s? '
     r'(?:is|are|does|has)\b'),
]


def dossiers():
    found = []
    for pat in PATTERNS:
        found.extend(glob.glob(os.path.join(ROOT, pat), recursive=True))
    return sorted(set(found))


def classify(body):
    """('fairy'|'story'|'none', markers)"""
    head = body.strip()[:700]
    first = head.split('\n')[0].strip()

    story = 0
    story += 2 if FILING.search(head) else 0
    story += 1 if YEAR.search(head) else 0
    story += 1 if INSTITUTION.search(head) else 0
    story += 1 if POST.search(head) else 0

    fairy = 0
    fairy += 2 if FAIRY_OPEN.search(head[:200]) else 0
    fairy += 1 if ROLE.search(head) else 0
    fairy += 1 if FOLK_CHAIN.search(head) else 0
    fairy += 1 if CLOSING_TURN.search(body) else 0

    # a filing header outranks an incidental fairy word, and vice versa
    if story >= 2 and story > fairy:
        return 'story', (story, fairy)
    if fairy >= 2 and fairy >= story:
        return 'fairy', (story, fairy)
    return 'none', (story, fairy)


def main():
    files = dossiers()
    counts = {'story': 0, 'fairy': 0}
    fails = []
    soft = []
    plain = []

    for path in files:
        with open(path, encoding='utf-8') as fh:
            text = fh.read()
        m = NARRATIO.search(text)
        if not m:
            continue
        body = m.group(1)
        kind, marks = classify(body)

        # anchor per paragraph, not per wrapped line: hard-wrapped prose puts
        # arbitrary words at a line start, and ^ in a thesis opener is a
        # claim about how a paragraph begins, not about where the margin fell
        paras = [' '.join(pp.split()) for pp in body.split('\n\n') if pp.strip()]
        essay_hits = []
        for label, pat in ESSAY:
            for pp in paras:
                for mm in re.finditer(pat, pp, re.I):
                    essay_hits.append((label, mm.group(0)[:70]))

        if kind == 'none':
            if essay_hits:
                # the genuine defect: the AI essay, in neither register
                fails.append((path, 'the essay — in neither register', essay_hits[:2]))
            else:
                # plain narrative that has not been given a register yet: rollout
                plain.append(path)
        else:
            counts[kind] += 1
            if essay_hits:
                soft.append((path, kind, essay_hits[:1]))

    total = len(files)
    print()
    print('TALE REGISTER — R-46 — %d dossiers' % total)
    print('  Normalised Story            %3d   declared' % counts['story'])
    print('  Fairy Tale                  %3d   declared' % counts['fairy'])
    print()
    print('  ROLLOUT, reported not failed:')
    print('    plain narrative, no register yet   %3d' % len(plain))
    print('    essay construction inside a Tale   %3d' % len(soft))
    print()
    print('  THE ESSAY, in neither register       %3d   FAIL above zero' % len(fails))
    print()

    if fails:
        print('  the essay (%d):' % len(fails))
        for path, why, hits in fails[:12]:
            print('    %-56s %s' % (os.path.basename(path)[:56], why[:40]))
            for label, ex in hits:
                print('        [%s] %s' % (label, ex[:80]))
        if len(fails) > 12:
            print('    … and %d more' % (len(fails) - 12))
        print()
        print('RESULT: FAIL — %d Tales in neither register' % len(fails))
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main())
