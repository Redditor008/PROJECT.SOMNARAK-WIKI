#!/usr/bin/env python3
"""check_dossier_consistency.py — one dossier, one set of facts.

An entity dossier states the same facts in several places: the SECC block, the
Operational Parameters table, the Combat Record, the Registrum, the trivia and
the prose that runs between them. Each is written for a different reader and
each is checked by a different linter, so a file can pass every linter while
telling two readers two different things.

**This is not hypothetical.** `SE-C-Iα-000 Kind Echo` carried a containment event
of excessive kindness next to a SECC line describing cold grief, an observation
ladder saying it did not activate, and a threat assessment saying there was no
danger. Twelve linters were green. Kind Echo was caught by a reader using the
file for another project.

The classes below are the ones that can be tested without judgement. Every one
of them is a *contradiction*, not a style: two statements that cannot both be
true. Where a class needs a human reading — a material described two ways, a
"never" next to a recorded incident — this tool reports the *co-location* and
does not call it a defect, because the lesson of this archive is that a check
which guesses is a check that gets switched off.

    python3 tools/auditors/check_dossier_consistency.py
    python3 tools/auditors/check_dossier_consistency.py -v
    python3 tools/auditors/check_dossier_consistency.py --only potency
    python3 tools/auditors/check_dossier_consistency.py --files A.md B.md
"""
import glob
import io
import re
import sys

# SE-*.md, not *.md. The earlier glob swept in two README files and
# Book_of_Regressor_Log_Dramaturgy.md, a lore document that is not a dossier, so
# the tool reported 302 while the archive held 301. A census that counts two
# READMEs as dossiers is not a census of dossiers.
DIRS = ['SOMNARAK-WORLD/Sorrow_Entities/SE-*.md',
        'SOMNARAK-WORLD/Unknown_Entities/SE-*.md']

# Measured 2026-11-02, batch 134. May only fall.
#
# Every class is 0 across all 301 dossiers. The mechanical half of this result is
# the more useful one: potency against risk tier, the coherence word, the element
# against the damage type, one field carrying two codes and the comprehension
# ladder were all measured clean, which means the archive's tables never disagreed
# with each other — the Kind Echo failure was entirely in prose.
#
# `r01` reached 0 from 93. 84 sentences and clauses that reported the file's own
# editing history were removed or restated as settled fact; the last 9 were real
# in-world uses of the same words and are named, one file at a time, in ALLOWLIST
# above. Zero is the correct ceiling, not a convenient one: any dossier that starts
# describing its own revisions again fails on the next run.
RATCHET = {'r01': 0}

# Over the ceiling fails: a new self-referential sentence was written.
# Under it also fails, with the instruction to lower the ceiling in this commit,
# so a batch that pays debt down records the new floor instead of leaving the next
# session a number that overstates its own work.

# The codex ladder. A potency word outside this set is an invention.
POTENCY_WORD = {'α': 'Minor', 'β': 'Moderate', 'γ': 'Major',
                'δ': 'Critical', 'ω': 'Catastrophic'}
COHERENCE_WORD = {'I': 'Residue', 'II': 'Echo', 'III': 'Fragment',
                  'IV': 'Entity', 'V': 'Sovereign'}
ELEMENTS = ('Lament', 'Grudge', 'Void', 'Weight')
# The thirteen words the dossiers actually file, per the conversion guide §IX.4.
COMPREHENSION = {
    '1': {'Initial', 'Trace', 'Minimal'},
    '2': {'Basic', 'Escalating', 'Limited'},
    '3': {'Advanced', 'Monitored', 'Critical'},
    '4': {'Mastered', 'Deep'},
    '5': {'Sovereign', 'Maximum'},
}

# R-01. Each of these makes a line in a file its own subject. In-world correction
# — a clerk who misfiled a name, a practice superseded inside the setting — is
# content and is deliberately NOT matched here.
EDIT_META = [
    (r'\b(?:the|an) earlier (?:entry|filing|record|version|text|reading|grade|number|wording)\b',
     'refers to an earlier version of this file'),
    (r'\bthe old (?:entry|filing|record|wording|text|grade|number)\b',
     'refers to an earlier version of this file'),
    (r'\b(?:entries|rows|lines) (?:below|above) (?:claiming|saying|stating|that have)\b',
     'refers to other lines in this file'),
    (r'\bhas been corrected\b(?! against the record)',
     'says the file was edited'),
    (r'\b(?:was|were) corrected (?:here|against this|to say so)\b',
     'says the file was edited'),
    (r'\bremains? visible in the file\b', 'describes the file, not the world'),
    (r'\bno dated state change\b', 'describes the file, not the world'),
    (r'\battribution error\b', 'names an editorial mistake'),
    (r'\b(?:formerly|previously) (?:read|said|stated|listed|graded|filed)\b',
     'says what the file used to say'),
]

# Reported, never failed. "This file records", "the older records give" and
# "older entries treating it as" all contain a word that looks editorial and a
# sentence that may be about the world — an in-world archive really does have
# older records. Flagging these as defects is how a checker earns a mute.
# In-world uses of the same words. These are not the file describing its own edits:
# the register really does hold earlier entries, a facility really did revise a
# notice in Y4243, the record hall really is an old building. Each is listed by
# file AND by the exact matched text, so the exemption cannot spread — the same
# words in any other file, or a second use in the same file, still fails.
ALLOWLIST = {
    ('SE-C-IIIγ-063_The_Rejector_거부하는_자.md', 'an earlier entry'):
        'the Rejector has made 406 refusals and has never contradicted one of them',
    ('SE-C-IIβ-101_Emberling_embers_의_아이.md', 'the earlier wording'):
        'a facility notice was revised in Y4243; an in-world date, not an edit',
    ('SE-C-IIβ-777_Last_Fruit_타오르는_열매.md', 'an earlier version'):
        'a declaration requirement was withdrawn by the facility, in-world',
    ('SE-C-Iα-392_Mirror_of_Rising_솟아오른_거울.md', 'the old record'):
        'the old record hall of the Mask Market, a place, three times in this file',
    ('SE-N-IIIγ-127_Mirror_of_Broken_부서진_거울.md', 'an earlier version'):
        'the target believes an earlier version of themselves was the real one',
    ('SE-O-Iα-643_Frozen_Mirror_얼어붙은_거울.md', 'attribution error'):
        'a finding to rule out in an investigation, not an editorial mistake',
}

EDIT_META_SOFT = [
    (r'\bthis file (?:says|states|claims|records|disagrees|contradicts)\b',
     'the sentence takes the file as its subject'),
    (r'\bolder (?:files|entries|records|text)\b', 'refers to older records'),
]

# Statements that cannot both be true, reported as co-location, not as a defect.
TENSION = [
    ('absolute-never',
     r'\bnever (?:been )?(?:injured|caused harm|harmed|hurt|killed)\b|\bno record holds\b',
     r'recorded case|the first bearer|the first .*field bearer|in its recorded',
     'says nothing has ever been hurt while carrying a recorded case'),
    ('material',
     r'\bnot (?:carved|crystalline|crystal)\b|\bnot .*made of crystal\b',
     r'Han-crystal|crystalline|translucent crystal',
     'denies a material elsewhere asserted'),
    ('absolute-no-event',
     r'\b(?:does not|never|cannot) (?:activate|breach)\b|\bno (?:event )?risk\b',
     r'^#{2,3} .*Event Behavior|\*\*Event Type\*\*',
     'says it does not act while filing an event'),
]


def rows(text, label):
    return [m.group(1).strip() for m in re.finditer(
        r'\|\s*\*{0,2}' + re.escape(label) + r'\*{0,2}\s*\|\s*([^|\n]*)\|', text, re.I)]


def first_code(value):
    m = re.search(r'([αβγδω])', value) or re.search(r'\b(I{1,3}|IV|V)\b', value)
    return m.group(1) if m else None


def check(path, text):
    """Return (defects, tensions) for one dossier."""
    defects, tensions = [], []
    name = path.split('/')[-1]

    # ── potency and risk tier must name the same grade
    pot = rows(text, 'Potency')
    risk = rows(text, 'Risk tier')
    for p in pot:
        pc = first_code(p)
        if not pc:
            continue
        if POTENCY_WORD[pc].lower() not in p.lower():
            defects.append(('potency-word', f'potency {pc} called "{p[:60]}", '
                                            f'codex word is {POTENCY_WORD[pc]}'))
        for r in risk:
            rc = first_code(r)
            if rc and rc != pc:
                defects.append(('grade-split', f'potency {pc} but risk tier {rc}'))
            elif rc == pc and POTENCY_WORD[pc].lower() not in r.lower():
                defects.append(('risk-word', f'risk tier {rc} called "{r[:60]}", '
                                             f'codex word is {POTENCY_WORD[pc]}'))

    # ── coherence letter and word
    for c in rows(text, 'Coherence'):
        cc = first_code(c)
        if cc in COHERENCE_WORD and re.search(r'\b(I{1,3}|IV|V)\b', c):
            if COHERENCE_WORD[cc].lower() not in c.lower():
                defects.append(('coherence-word', f'coherence {cc} called "{c[:60]}", '
                                                  f'codex word is {COHERENCE_WORD[cc]}'))

    # ── one field, two different codes
    for label in ('Risk tier', 'Potency', 'Coherence', 'Element'):
        codes = {first_code(v) for v in rows(text, label)} - {None}
        if len(codes) > 1:
            defects.append(('field-split', f'{label} carries {sorted(codes)}'))

    # ── element must match the damage type the Combat Record deals
    el = rows(text, 'Element')
    dmg = re.search(r'\|\s*(Lament|Grudge|Void|Weight)\s+[\d–\-]', text)
    if el and dmg:
        code = re.search(r'(Lament|Grudge|Void|Weight)', el[0])
        if code and code.group(1) != dmg.group(1):
            defects.append(('element', f'SECC element {code.group(1)}, damage {dmg.group(1)}'))

    # ── comprehension level word must come from the guide's closed 13-word ladder.
    # Scoped to the R.D.'s own registry. `Unknown_Entities` files the field as a
    # monitoring descriptor instead — "3 — Mountain Pass Telemetry", "2 — Caravan
    # Escort Telemetry", "3 — Elevated" — which is that registry's convention, not a
    # contradiction: the value is invented but it does not contradict anything in the
    # same file. Reading the whole tail as the word, and then reading a registry
    # variant as an error, reported 13 defects where 8 were conventions.
    for c in (rows(text, 'R.D. Comprehension Level')
              if '/Sorrow_Entities/' in path else []):
        m = re.match(r'\s*([1-5])\s*[—-]\s*(.+?)\s*$', c)
        if not m:
            continue
        lvl = m.group(1)
        # The ladder word leads. "Mastered (training entity; fully understood)" is
        # the word Mastered with a note after it, and reading the whole tail as the
        # word reported nine legal filings as defects before this line existed.
        word = re.split(r'[\s(/—–-]', m.group(2).strip())[0].rstrip(',;:.')
        legal = COMPREHENSION.get(lvl, set())
        if word not in legal:
            defects.append(('comprehension', f'level {lvl} filed as "{word}", ladder allows '
                                             f'{sorted(legal)}'))

    # ── R-01
    for pat, why in EDIT_META:
        for m in re.finditer(pat, text, re.I):
            if (name, m.group(0).lower()) in ALLOWLIST:
                continue
            ctx = text[max(0, m.start() - 55):m.end() + 75].replace('\n', ' ')
            defects.append(('r01', f'{why} — "...{ctx}..."'))

    for pat, why in EDIT_META_SOFT:
        for m in re.finditer(pat, text, re.I):
            ctx = text[max(0, m.start() - 55):m.end() + 75].replace('\n', ' ')
            tensions.append(('edit-meta?', f'{why} — "...{ctx}..."'))

    # ── tension classes: reported, never failed
    for label, a, b, why in TENSION:
        ma, mb = re.search(a, text, re.I | re.M), re.search(b, text, re.I | re.M)
        if ma and mb:
            tensions.append((label, why))

    return defects, tensions


def main(argv):
    verbose = '-v' in argv or '--verbose' in argv
    only = argv[argv.index('--only') + 1] if '--only' in argv else None
    if '--files' in argv:
        paths = argv[argv.index('--files') + 1:]
    else:
        paths = []
        for pattern in DIRS:
            paths.extend(sorted(glob.glob(pattern)))
        paths = [p for p in sorted(set(paths)) if not p.endswith('README.md')]

    total = 0
    shown = 0
    by_class = {}
    tension_files = 0
    for path in paths:
        try:
            text = io.open(path, encoding='utf-8').read()
        except OSError:
            continue
        defects, tensions = check(path, text)
        if only:
            defects = [d for d in defects if d[0] == only]
            tensions = [t for t in tensions if t[0] == only]
        if tensions:
            tension_files += 1
        if not defects:
            continue
        total += len(defects)
        for kind, detail in defects:
            by_class[kind] = by_class.get(kind, 0) + 1
        # The listing is capped for readability; the COUNT never is. An earlier
        # version broke out of the loop here, which made the report's own total
        # disagree with the archive — a stopping-early bug dressed as a summary.
        if shown < 40 or verbose:
            print(f'  {path.split("/")[-1]}')
            for kind, detail in defects:
                print(f'      [{kind}] {detail}')
            shown += 1
        elif shown == 40:
            print('  ... more; run -v for the full listing')
            shown += 1

    print(f'\nDOSSIER CONSISTENCY — {len(paths)} dossiers')
    bad = False
    for kind in sorted(set(list(by_class) + list(RATCHET))):
        n = by_class.get(kind, 0)
        ceiling = RATCHET.get(kind)
        if ceiling is None:
            print(f'  {kind:16} {n:4}   NOT RATCHETED — a new class needs a ceiling')
            bad = bad or n > 0
            continue
        if n > ceiling:
            print(f'  {kind:16} {n:4}   ABOVE CEILING {ceiling} — new defect')
            bad = True
        elif n < ceiling:
            print(f'  {kind:16} {n:4}   BELOW CEILING — lower it to {n}')
            bad = True
        else:
            print(f'  {kind:16} {n:4}   at ceiling')
    print(f'  {"tensions flagged":16} {tension_files:4}  (co-location only — read them, do not fail on them)')
    print('RESULT: ' + ('FAIL' if bad else 'PASS'))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
