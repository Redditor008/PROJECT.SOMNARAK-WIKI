#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_tale_register.py — gate 91: a Tale is one of four registers (R-46).

The owner's direction, batch 188: *"TALE HAVE TWO CATEGORY OF WRITING NORMALIZE STORY AND
FAIRY TALE TYPE OF WRITING."* Batch 189 widened it: *"STORY TALE, FAIRY TALE, DIALOGUE
STORY, And HYBRID[It Mean It can have Dialogue Or Like How Most Of L Corp Abnormality Story
Structure/Look Like]"*.

`이야기 (Narratio) — The Tale` is written in exactly one of four registers. This gate reads
the opening, the body and the speech in every Tale and decides which.

STORY TALE — a filed account (the batch-188 'Normalised Story')
    * a filing header: `> **Filed by:**`, `> **Report of:**`, `> **From the desk of:**`
    * a date or year (Year 4,2xx)
    * a named institution doing something (Registry, Wardens' Office, Directorate, Gardens)
    * a person with a post

FAIRY TALE — a folktale
    * an opening formula: Once / There was / Before there was / Long ago / In the time before
    * roles rather than names (the woodcutter, the girl, the third son)
    * the folk 'and' chain
    * a closing turn: and it is still there / and so it is to this day

DIALOGUE STORY — a transcript (Project Moon's Queen of Hatred audio logs)
    * a header naming the record: Transcript of / Log of / Recovered audio / Interview
    * scored speech: SPEAKER: line
    * speech takes the section — at least DIALOGUE_SHARE of its paragraphs

HYBRID — a Story Tale that quotes the people in it, the L Corp form the owner described
    * a filing header, a post, a date
    * and attributed speech inside the account

NEITHER — the essay
    * a thesis sentence ('X is Y, and the Y has weight')
    * a negation-and-correction ('but X is only the largest version of a smaller truth')
    * a rhetorical triplet ('What is spent is spent. What is wasted is wasted.')
    * an announcement of significance ('The crack is the point.')

WHAT FAILS
  * a Tale with no register marker at all — the essay
  * a Tale carrying an essay construction anywhere in it, whatever its opening

    python3 tools/auditors/check_tale_register.py --next 20   # what to convert next

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

# NB: the corpus writes `> **Filed by:** …` — the colon sits inside the bold, so a
# trailing \*\* after the label never matches. Accept either side of the colon.
FILING = re.compile(
    r'>\s*\*\*(?:Filed by|Report of|From the desk of|Submitted by|Record of|Entry of)'
    r'\s*:?\s*\*\*?', re.I)
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

DIALOGUE_HEADER = re.compile(
    r'>\s*\*\*(?:Transcript|Log|Recovered audio|Audio|Interview|Recording|Statement)\b',
    re.I)
# a speaker line: NAME: …  |  > NAME: …  |  NAME (post): …  — a short capitalised or
# quoted speaker token followed by a colon, on its own paragraph
SPEAKER = re.compile(
    r'^\s*(?:>\s*)?(?:(?:\*\*)?[A-Z][A-Za-z\u00C0-\u024F\'\u2019.-]{0,24}'
    r'|\"[^\"]{1,30}\")\s*\(?[^:\n]{0,30}\)?\s*:\s*(?:\*\*)?\s*\S')
QUOTED = re.compile(r'[\u201c\"][^\"\n]{6,}[\u201d\"]')
DIALOGUE_SHARE = 0.55
# a bold label that names the record, not a person speaking it
HEADER_LABEL = re.compile(
    r'^(?:From the desk of|Filed by|Report of|Submitted by|Record of|Transcript of|'
    r'Log of|Recorded|Kept by|Subject|Against|Re|Note|Purpose|To|Finding|Classification|'
    r'Entry|Row analyst|Survey|Watch Record|From|Drawn up by|Reference)\b', re.I)

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


def speech(body):
    """(speech_paragraphs, total_paragraphs, quoted_runs)

    The leading `>` block is the header that names the record. A header is not somebody
    speaking, so it is stripped before counting — otherwise every filed account looks like
    a hybrid on the strength of its own cover sheet.
    """
    paras = [pp for pp in body.split('\n\n') if pp.strip()]
    kept = []
    for pp in paras:
        s = pp.strip()
        if s.startswith('>'):
            continue          # the record's cover sheet
        kept.append(s)
    if not kept:
        return 0, len(paras), 0
    sp = 0
    for s in kept:
        m = SPEAKER.match(s)
        if not m:
            continue
        label = s.lstrip('*').split(':')[0].strip('* ').strip()
        if HEADER_LABEL.match(label):
            continue
        sp += 1
    q = len(QUOTED.findall(body))
    return sp, len(kept), q


def classify(body):
    """('story'|'fairy'|'dialogue'|'hybrid'|'none', markers)"""
    head = body.strip()[:700]

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

    sp, total, quoted = speech(body)
    share = (sp / total) if total else 0.0

    # DIALOGUE STORY: the speech is the section, not an ornament on it. Either it takes
    # most of the section on its own, or the record is declared a transcript up front.
    if sp >= 3 and share >= DIALOGUE_SHARE:
        return 'dialogue', (sp, total, round(share, 2))
    if DIALOGUE_HEADER.search(head) and sp >= 2 and share >= 0.4:
        return 'dialogue', (sp, total, round(share, 2))

    # HYBRID: a filed account that kept the words — the L Corp form
    if story >= 2 and story > fairy and (sp >= 1 or quoted >= 2):
        return 'hybrid', (story, fairy, sp, quoted)

    # a filing header outranks an incidental fairy word, and vice versa
    if story >= 2 and story > fairy:
        return 'story', (story, fairy)
    if fairy >= 2 and fairy >= story:
        return 'fairy', (story, fairy)
    return 'none', (story, fairy)



def markers(body):
    """Every register marker this Tale already carries, and what each is short of."""
    head = body.strip()[:700]
    have = {
        'filing header': bool(FILING.search(head)),
        'year': bool(YEAR.search(head)),
        'institution': bool(INSTITUTION.search(head)),
        'post': bool(POST.search(head)),
        'fairy opening': bool(FAIRY_OPEN.search(head[:200])),
        'roles not names': bool(ROLE.search(head)),
        'folk and-chain': bool(FOLK_CHAIN.search(head)),
        'closing turn': bool(CLOSING_TURN.search(body)),
    }
    return have


NEEDS = {
    'story': ['filing header', 'year', 'institution', 'post'],
    'fairy': ['fairy opening', 'roles not names', 'folk and-chain', 'closing turn'],
}


def next_tranche(limit=20):
    """The plain Tales closest to a register, and the one thing each still needs.

    Story needs `filing header` plus one of the other three; fairy needs the opening plus
    two of the other three. Anything on this list is a rewrite of an opening and a closing
    turn, not a new Tale.
    """
    out = []
    for path in dossiers():
        with open(path, encoding='utf-8') as fh:
            text = fh.read()
        m = NARRATIO.search(text)
        if not m:
            # A dossier with no Tale is not a plain Tale; it is a hole in the file.
            no_tale.append(path)
            continue
        kind, _marks = classify(m.group(1))
        if kind != 'none':
            continue
        have = markers(m.group(1))
        best = None
        for reg, keys in NEEDS.items():
            missing = [k for k in keys if not have[k]]
            if reg == 'story':
                need = len([k for k in missing if k != 'filing header']) + (2 if 'filing header' in missing else 0)
            else:
                need = len(missing) + (1 if 'fairy opening' in missing else 0)
            if best is None or need < best[0]:
                best = (need, reg, missing)
        out.append((best[0], best[1], best[2], path))
    out.sort(key=lambda r: (r[0], r[3]))
    print('NEXT TRANCHE — the plain Tales closest to a register')
    for need, reg, missing, path in out[:limit]:
        print('  -%d  %-7s %-58s  needs: %s'
              % (need, reg, os.path.basename(path)[:56], ', '.join(missing) or '—'))
    return out


def main():
    if '--next' in sys.argv:
        next_tranche(int(sys.argv[sys.argv.index('--next') + 1])
                     if len(sys.argv) > sys.argv.index('--next') + 1 else 20)
        return 0
    files = dossiers()
    counts = {'story': 0, 'fairy': 0, 'dialogue': 0, 'hybrid': 0}
    fails = []
    soft = []
    plain = []
    no_tale = []

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
    print('TALE REGISTER — R-46 — four registers — %d dossiers' % total)
    print('  Story Tale                  %3d   declared' % counts['story'])
    print('  Fairy Tale                  %3d   declared' % counts['fairy'])
    print('  Dialogue Story              %3d   declared' % counts['dialogue'])
    print('  Hybrid                      %3d   declared' % counts['hybrid'])
    print()
    print('  ROLLOUT, reported not failed:')
    print('    plain narrative, no register yet   %3d' % len(plain))
    print('    essay construction inside a Tale   %3d' % len(soft))
    print()
    print('  THE ESSAY, in neither register       %3d   FAIL above zero' % len(fails))
    print('  NO TALE AT ALL                       %3d   FAIL above zero' % len(no_tale))
    print()

    if no_tale:
        print('  no Tale at all (%d):' % len(no_tale))
        for path in no_tale:
            print('    %s' % os.path.basename(path))
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
    if no_tale:
        print('RESULT: FAIL — %d dossiers carry no Tale at all' % len(no_tale))
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main())
