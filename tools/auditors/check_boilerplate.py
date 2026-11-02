#!/usr/bin/env python3
"""check_boilerplate.py — measure the shared sentences in the M.A.W. records.

R-14 defines boilerplate by intent, not by repetition: generic text on a
load-bearing field "is a lie about the entity, because those are the fields a
worker would act on." A corrosion arc, a binding, and a cost are all fields a
worker acts on. When 165 records print the same corrosion sentence, the archive
is not describing 165 pieces; it is describing one sentence 165 times.

This auditor exists because that debt was carried for a dozen batches as an
undefined counter in `WORK_IN_PROGRESS.md` — "corrosion A 103 of 139", "C 165",
"B-variant 15" — quoted in three places and defined in none, so nobody could
measure it, and the finishedness score could not see it. A number without a
rule is a rumour. This is the rule, and these are the measurements.

**The ratchet.** Each family carries a ceiling that may only ever fall. Exceeding
it fails the run: new boilerplate is not allowed. Falling *below* it also fails
the run, with the instruction to lower the ceiling — because a batch that pays
down the debt must record the new floor in the same commit, or the next session
inherits a number that overstates its own debt and the progress is unverifiable.

There is no flag that lowers the ceiling automatically. A checker that can lower
its own bar is not a checker; the edit is deliberate, dated, and visible in the
diff.

    python3 tools/auditors/check_boilerplate.py            # measure, ratchet check
    python3 tools/auditors/check_boilerplate.py -v         # per-file listing
    python3 tools/auditors/check_boilerplate.py --only NAME
    python3 tools/auditors/check_boilerplate.py --files A.md B.md   # audit named files

`--files` exists because of a real defect in batch 130. The conversion script that
cleaned `Registry_993_to_997` asserted cleanliness against a hand-written list of
template strings, and that list was missing two of the nine families — so six
records were reported clean while still carrying both. **A guard that re-states
the rule will drift from the rule.** `--files` asks this module, which is where the
rule lives, and exits non-zero if any named file still carries a family. Conversion
scripts should call it rather than keep their own list.
"""
import glob
import io
import re
import sys

RECORDS = 'SOMNARAK-WORLD/MAW_Codex_Sets/**/SE-*.md'

# name -> (label, matcher, why it is boilerplate)
FAMILIES = [
    ('corrosion-stock',
     'stock corrosion sentence',
     lambda t: 'Corrosion runs from first-person description of the event' in t,
     'R-14 mark 1: the corrosion arc is what happens to the bearer. One sentence '
     'for 165 pieces says nothing about any of them.'),
    ('autobiography',
     '"treating the response as autobiography" line',
     lambda t: 'Treating the response as autobiography reproduced the wound and fixed the rule' in t,
     'R-14 mark 4: the sentence was written to cover the seam where the source '
     'trace was spliced in, and it stands exactly where the damage was.'),
    ('set-opening',
     '"{piece} is the {kind} record of the {set} set" opener',
     lambda t: re.search(r'is the (?:suit|weapon|stigma) record of the ', t) is not None,
     'R-14 mark 2: a pattern dictionary. The piece is introduced by its slot in a '
     'set instead of by what it is.'),
    ('source-trace-doctrine',
     '"The source-trace fixed doctrine:" opener',
     lambda t: 'The source-trace fixed doctrine:' in t,
     'R-14 mark 1: the doctrine line is the record telling the worker what the '
     'entity tests, which is a load-bearing field.'),
    ('cost-opener',
     '"The cost is the {noun}:" opener',
     lambda t: re.search(r'The cost is the [\w\u2019\']+:', t) is not None,
     'R-14 mark 2: the noun changes, the sentence does not. A cost slotted into a '
     'template is a label rotated by slot.'),
    ('binding-opener',
     '"Binding names the source event" opener',
     lambda t: 'Binding names the source event' in t,
     'R-14 mark 2: the binding is the condition a worker must satisfy before the '
     'piece can be taken up at all.'),
    ('maintenance-line',
     'generic maintenance instruction',
     lambda t: 'record bearer, trigger, source response, cost, and unresolved detail' in t,
     'R-14 mark 1: maintenance is what a worker does with the piece on a Tuesday. '
     'The line names no part, no material and no procedure. SE-643-B shows the '
     'bespoke form — "thaw only the hilt with body heat" — so this is a choice.'),
    ('shutdown-line',
     'generic emergency-shutdown instruction',
     lambda t: 'shutdown preserves the record but does not refund its cost' in t,
     'R-14 mark 1: shutdown is the procedure that saves a bearer. This one tells '
     'them a witness must speak and that the cost is not refunded, which is true '
     'of every piece and therefore useful about none.'),
    ('gauge-default',
     '"The Sorrow Gauge held at its opening band."',
     lambda t: 'The Sorrow Gauge held at its opening band' in t,
     'R-14 mark 3/5: the Sorrow Gauge is a mechanic that can rise. Across 133 '
     'instances of this sentence in 76 records it never once rose or changed — not '
     'one record files a Gauge that moved. That is not a reading, it is a default '
     'nobody computed. Found in batch 132 by reading SE-1030-B whole; no regex was '
     'looking for a number that never varies.'),
    ('stigma-canonical',
     '"grants a minor boon ... mirrors the entity\'s nature"',
     lambda t: 'Grants a minor boon tied to' in t,
     'R-14 mark 1: the sentence says the effect mirrors the entity and then does '
     'not say what the effect is. It is a placeholder wearing a description.'),
]

# Deliberately NOT counted here, and the reason, so a later session does not
# re-litigate it: `encountered this source response`, `only after the team
# attributed it to X`, and `The first bearer of ...` are a fixed *frame* carrying
# an entity-specific answer. A form is not boilerplate. The test R-14 gives is
# whether the text would be true of a different dossier with the nouns swapped;
# those three would not be, because the answer inside them changes with the piece.
# The families above would.

# Measured 2026-11-02, at the start of batch 130. Each ceiling may only fall.
# The first pass at `cost-opener` read 115 because `\w+:` cannot match a possessive,
# and `SE-997-D` writes "The cost is the light's source:". The pattern now accepts
# one, and the true starting figure was 116. A count that misses a form is how a
# family gets under-reported; assume every family here has one until proven otherwise.
RATCHET = {
    'corrosion-stock':       160,
    'autobiography':          98,
    'set-opening':           131,
    'source-trace-doctrine': 124,
    'cost-opener':           111,
    'binding-opener':         51,
    'maintenance-line':      327,
    'shutdown-line':         327,
    'stigma-canonical':       12,
    'gauge-default':          76,
}
RATCHET_SET = '2026-11-02'


def measure():
    files = sorted(glob.glob(RECORDS, recursive=True))
    hits = {name: [] for name, _, _, _ in FAMILIES}
    for path in files:
        try:
            text = io.open(path, encoding='utf-8').read()
        except OSError:
            continue
        for name, _, match, _ in FAMILIES:
            if match(text):
                hits[name].append(path)
    return files, hits


def audit_files(paths):
    """Report every family each named file still carries. Used by conversion
    scripts so the rule is asked, never re-stated."""
    bad = 0
    for path in paths:
        try:
            text = io.open(path, encoding='utf-8').read()
        except OSError:
            print(f'  MISSING {path}')
            bad += 1
            continue
        found = [name for name, _, match, _ in FAMILIES if match(text)]
        leaf = path.split('/')[-1]
        if found:
            bad += 1
            print(f'  DIRTY {leaf}: {", ".join(found)}')
        else:
            print(f'  clean {leaf}')
    print(f'RESULT: {"FAIL" if bad else "PASS"} — {bad} of {len(paths)} files still carry a family')
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
        print('RESULT: FAIL — no M.A.W. records found; the glob is wrong, not the archive.')
        return 1

    failures = []
    print(f'BOILERPLATE — {len(files)} M.A.W. records · ratchet set {RATCHET_SET}')
    print(f'  {"family":24} {"files":>6} {"ceiling":>8}   state')

    for name, label, _, why in FAMILIES:
        if only and only != name:
            continue
        n = len(hits[name])
        ceiling = RATCHET[name]
        if n > ceiling:
            state = 'ABOVE CEILING — new boilerplate'
            failures.append((name, n, ceiling, 'above'))
        elif n < ceiling:
            state = f'BELOW CEILING — lower it to {n}'
            failures.append((name, n, ceiling, 'below'))
        else:
            state = 'at ceiling'
        print(f'  {name:24} {n:6} {ceiling:8}   {state}')

        if verbose and hits[name]:
            print(f'      {why}')
            for path in hits[name][:40]:
                print(f'        {path.split("/")[-1]}')
            if len(hits[name]) > 40:
                print(f'        ... {len(hits[name]) - 40} more')

    distinct = set()
    for name in hits:
        distinct.update(hits[name])
    print(f'  {"distinct files carrying any":24} {len(distinct):6}')
    print(f'  {"clean records":24} {len(files) - len(distinct):6}')

    for name, n, ceiling, direction in failures:
        if direction == 'above':
            print(f'    REGRESSION {name}: {n} files, ceiling {ceiling} — '
                  f'a shared sentence was written into a new record. Rewrite it for that record.')
        else:
            print(f'    RATCHET {name}: measured {n}, ceiling still {ceiling} — '
                  f'edit RATCHET["{name}"] to {n} in this commit so the gain is locked in.')

    if failures:
        print('RESULT: FAIL')
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
