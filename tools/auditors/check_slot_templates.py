#!/usr/bin/env python3
"""check_slot_templates.py — find sentences that are a slot, not a fact.

A slot template is a sentence whose nouns change and whose claim does not. The
test is R-14's, applied to the dossiers instead of the M.A.W. records: *would this
be true of a different entity with the nouns swapped?* If yes, it is not a
description of this entity — it is the shape of one.

The five families here were found by reading, in the full-SE review of
2026-11-03, in the 9xx block. They are worse than the boilerplate families in
`check_boilerplate.py` for a specific reason: boilerplate repeats one sentence,
which a reader can see and discount. These repeat a *grammar*, so every instance
looks locally written and the page never shows the seam:

    - Expresses Lament pressure in a lament register.
    - The hazard form is unmistakable — this is a lament entity, not a general one.
    - One of the first catalogued **Hazard-Lament** entities in Somnarak.
    - Its lament descriptor makes it structurally unique among hazard entities.
    - The lament pressure in the lament register feels different from standard
      lament — more specific, more personal.

Five sentences, five claims, none of them checkable. "Structurally unique" names
no structure. "More specific, more personal" names no difference. "One of the
first catalogued" was in 23 files, so either the catalogue was built in one
afternoon or the sentence is not a fact. The measured count was **66 instances in
29 dossiers** — and every one of those dossiers already held the specific fact
that could have filled the line instead.

Matchers are written as shapes, not as the exact shipped strings, because the
shipped strings are what a ratchet of 0 is meant to keep out. A new variant —
"feels unlike standard void", "makes it structurally singular" — is the same
defect and must fail the same way.

    python3 tools/auditors/check_slot_templates.py           # ratchet check
    python3 tools/auditors/check_slot_templates.py -v        # per-instance listing
    python3 tools/auditors/check_slot_templates.py --files A.md   # audit named files

Ceilings start at 0, dated. There is no flag that raises them.
"""
import glob
import io
import re
import sys

DOSSIERS = ('SOMNARAK-WORLD/Sorrow_Entities/**/SE-*.md',
            'SOMNARAK-WORLD/Unknown_Entities/*.md')

# name -> (label, matcher, why it is a slot and not a fact)
FAMILIES = [
    ('element-register-bullet',
     '"Expresses {element} pressure in a {manifestation} register."',
     lambda t: re.search(r'Expresses \w+ pressure in an? \w+ register\b', t),
     'The element and the manifestation are already two rows of the SECC table '
     'twelve lines above. The bullet restates them as if the restatement were an '
     'observation, so the Appearance block opens by telling the reader nothing '
     'the classification block did not.'),
    ('form-unmistakable',
     '"The {type} form is unmistakable — this is a {manifestation} entity."',
     lambda t: re.search(r'form is unmistakable\b', t),
     'Says the identification is certain and does not say what identifies it. '
     'The same bullet in the same file usually does give the marker — the '
     'breathing rate, the onset of weeping, the load gauge — in the line below, '
     'which is the fact this line should have carried.'),
    ('first-catalogued',
     '"One of the first catalogued **{type}-{manifestation}** entities in Somnarak."',
     lambda t: re.search(r'\bOne of the first catalogued\b', t),
     'Carried by 23 dossiers. A wing cannot hold 23 firsts, and the archive '
     'files no catalogue order that would let a reader check the claim. Where '
     'the sentence had a real clause after the comma, that clause was the '
     'trivia; the frame around it was decoration with a factual tone.'),
    ('structural-uniqueness',
     '"Its {manifestation} descriptor makes it structurally unique among {type} entities."',
     lambda t: re.search(r'descriptor makes it structurally unique\b', t),
     'Names no structure and no comparison. Uniqueness is a claim about the '
     'other members of a class, so it is only checkable by naming the feature '
     'and the class — which the files can do and, after this batch, do.'),
    ('register-feels-different',
     '"The {element} pressure in the {manifestation} register feels different from standard {element}."',
     lambda t: re.search(r'register feels (?:different from|unlike) standard \w+', t),
     'The vaguest of the five: "more specific, more personal" is the file '
     'reporting its own impression of its own classification. A reading is a '
     'reading when it can be wrong; this one cannot be.'),
]

# Measured 2026-11-03, before the batch: 66 instances across 29 dossiers.
# Ceilings may only ever fall; they are already at the floor.
RATCHET = {
    'element-register-bullet':   0,
    'form-unmistakable':         0,
    'first-catalogued':          0,
    'structural-uniqueness':     0,
    'register-feels-different':  0,
}
RATCHET_SET = '2026-11-03'


def dossier_files():
    found = []
    for pattern in DOSSIERS:
        found.extend(glob.glob(pattern, recursive=True))
    return sorted(set(found))


def measure(paths=None):
    """Return (files, hits) with hits[name] = [(path, line_text), ...]."""
    files = paths if paths is not None else dossier_files()
    hits = {name: [] for name, _, _, _ in FAMILIES}
    for path in files:
        try:
            with io.open(path, encoding='utf-8') as handle:
                text = handle.read()
        except OSError:
            continue
        for line in text.split('\n'):
            for name, _, match, _ in FAMILIES:
                if match(line):
                    hits[name].append((path, line.strip()))
    return files, hits


def audit_files(paths):
    bad = 0
    for path in paths:
        try:
            with io.open(path, encoding='utf-8') as handle:
                text = handle.read()
        except OSError:
            print(f'  MISSING {path}')
            bad += 1
            continue
        found = []
        for line in text.split('\n'):
            for name, _, match, _ in FAMILIES:
                if match(line):
                    found.append(name)
                    break
        leaf = path.split('/')[-1]
        if found:
            bad += 1
            print(f'  DIRTY {leaf}: {", ".join(sorted(set(found)))}')
        else:
            print(f'  clean {leaf}')
    print(f'RESULT: {"FAIL" if bad else "PASS"} — {bad} of {len(paths)} files carry a slot template')
    return 1 if bad else 0


def main(argv):
    if '--files' in argv:
        named = argv[argv.index('--files') + 1:]
        if not named:
            print('RESULT: FAIL — --files needs at least one path')
            return 1
        return audit_files(named)

    verbose = '-v' in argv or '--verbose' in argv
    only = None
    if '--only' in argv:
        only = argv[argv.index('--only') + 1]

    files, hits = measure()
    if not files:
        print('RESULT: FAIL — no dossiers matched; the glob is wrong, not the corpus')
        return 1

    failed = 0
    total = 0
    print(f'check_slot_templates — {len(files)} dossiers, ceilings set {RATCHET_SET}')
    for name, label, _, why in FAMILIES:
        if only and name != only:
            continue
        found = hits[name]
        count = len(found)
        total += count
        ceiling = RATCHET[name]
        if count > ceiling:
            status = 'OVER'
            failed += 1
        elif count < ceiling:
            status = 'UNDER — lower the ceiling'
            failed += 1
        else:
            status = 'at ceiling'
        print(f'  {name:26s} {count:3d}  ceiling {ceiling:3d}  {status}')
        if verbose and found:
            print(f'      {label}')
            for path, line in found:
                print(f'      {path.split("/")[-1][:52]:52s} {line[:110]}')
    print(f'  {"TOTAL":26s} {total:3d}  instances')
    print(f'RESULT: {"FAIL" if failed else "PASS"} — {failed} families off ratchet, {total} instances')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
