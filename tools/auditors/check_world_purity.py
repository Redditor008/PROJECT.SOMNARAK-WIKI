#!/usr/bin/env python3
"""
tools/auditors/check_world_purity.py

Enforces the folder rule: SOMNARAK-WORLD/ holds in-world records and nothing else.

The owner's instruction, verbatim: *"NEVER ADD ANYTHING THAT IS NON-IN-WORLD STUFF
IN SOMNARAK WORLD FOLDER — THAT HOW THE FOLDERING WORK, SO EVERYTHING THAT IS IN
WORLD CAN BE DUMP IN ONE PLACE."*

The tree already promises this in its own charter (`SOMNARAK-WORLD/README.md`,
PURITY RULE). This tool is what makes the promise checkable, because every other
auditor in `tools/auditors/` checks a document's *content* and none of them asked
whether the document belongs in the tree at all.

WHAT COUNTS AS OUT OF WORLD
  A record dated Year 4238 cannot contain 2026. It cannot contain a git commit, a
  build batch, a work-in-progress marker, a GitHub URL, a path to the tooling, or
  a count of how many dossiers the archive holds. Each of those is a fact about
  our world, and each of them has already had to be scrubbed out of this archive
  one class at a time — which is exactly the argument for checking it centrally.

WHAT IS NOT FLAGGED, AND WHY
  The check is deliberately narrow, because a checker that guesses gets switched
  off. These are legal and must never fail:

  * `Auditor`, `Keeper`, `Warden` — in-world ranks and job titles.
  * "the archive", "the record", "the register" — the in-world institution.
  * `Year 4238`, and every other Year — that is the world's own calendar.
  * `PIN` inside an in-world phrase (`PIN AT NODE 02` is a tactical order),
    which is why the WIP marker is matched as `PIN WIP`, not as `PIN`.
  * "splinter" is not "linter" and "weeping" is not "WIP" — both were false
    positives during the audit that produced this file, and both are why the
    patterns below are phrase-shaped rather than word-shaped.

Ratchet fails in both directions: over the ceiling a new leak was written, under
it the ceiling is stale and the batch that lowered it must lower the number.
"""

import glob
import os
import re
import sys

WORLD = 'SOMNARAK-WORLD/**/*.md'

# The tree's own charter has to describe the tree, so it is allowed to name the
# sibling folders the rule points at. It is still held to every other rule.
CHARTER = 'SOMNARAK-WORLD/README.md'

LEAKS = [
    ('real-world-date',
     r'\b20(?:2[0-9])-[01]\d-[0-3]\d\b|\b(?:January|February|March|April|May|June|July|'
     r'August|September|October|November|December)\s+20(?:2[0-9])\b',
     'a date from our world inside a record dated by the Year calendar'),
    ('commit-hash',
     r'`[0-9a-f]{7,40}`|\bcommit(?:s)?\s+`?[0-9a-f]{7,40}\b|\bPUSH VERIFIED\b',
     'a git commit or push record'),
    ('build-batch',
     r'\bBatch \d{2,3}\b|\brepo-wide\b|\bthis repository\b|\bthe repo\b',
     'build-batch or repository vocabulary'),
    ('wip-marker',
     r'PIN\s*WIP|\bWIP\b(?!\s*(?:AT|NODE|LINE|the))',
     'work-in-progress marker'),
    # `the owner` alone is in-world and common — "the owner's feelings about the
    # memory", "when an owner or a keeper". Only the phrase that names OUR owner
    # is a leak. Narrowed after the first run flagged 32 in-world uses.
    ('owner-voice',
     r'archive owner',
     'the owner speaking, rather than the in-world institution'),
    ('outward-link',
     r'github\.com|REFERENCE_SOMNARAK_WIKI/|\btools/',
     'a link or path pointing outside the world'),
    # Only a count of the archive AS A FILE COLLECTION is a leak. In-world
    # record-keeping says "653 records had no figure", "the Day 177 record",
    # "12,000 Files expunged", "291 dossiers" — all four are the world counting
    # itself, and the first run flagged every one of them. So: the word `files`
    # only, lower case only, and never when a Day, a Year, a Cycle or a Part is
    # what is being counted.
    ('meta-count',
     r'(?<!Day )(?<!Year )(?<!Part )(?<!Cycle )\b\d[\d,]* (?-i:files)\b'
     r'|\bindexes \d+ of \d+\b',
     'a count of the archive counted from outside it'),
]

RATCHET = {k: 0 for k, _, _ in LEAKS}

# One exemption, and it is narrow on purpose: the charter's purity paragraph
# names the sibling research folders, because a rule about what may not be here
# has to say where that material went instead. Nothing else in the charter is
# excused, and no other file is excused at all.
CHARTER_EXEMPT = re.compile(
    r'Comparison, conversion, and craft-research material lives outside this tree[^.]*\.',
    re.I)


def main(argv):
    verbose = '-v' in argv or '--verbose' in argv
    paths = sorted(glob.glob(WORLD, recursive=True))

    defects = {k: [] for k, _, _ in LEAKS}
    for p in paths:
        try:
            with open(p, encoding='utf-8') as f:
                text = f.read()
        except (UnicodeDecodeError, OSError):
            continue
        rel = p.replace(os.sep, '/')
        for kind, pat, why in LEAKS:
            body = text
            if rel == CHARTER:
                body = CHARTER_EXEMPT.sub('', body)
            for m in re.finditer(pat, body, re.I):
                line = body[:m.start()].count('\n') + 1
                ctx = body[max(0, m.start() - 45):m.end() + 45].replace('\n', ' ')
                defects[kind].append((rel, line, m.group(0), why, ctx))

    print(f'WORLD PURITY — {len(paths)} files in SOMNARAK-WORLD')
    bad = False
    total = 0
    for kind, _, _ in LEAKS:
        got = len(defects[kind])
        total += got
        ceiling = RATCHET[kind]
        if got > ceiling:
            print(f'  {kind:18} {got:4}   ABOVE CEILING {ceiling} — non-in-world material')
            bad = True
        elif got < ceiling:
            print(f'  {kind:18} {got:4}   BELOW CEILING — lower it to {got}')
            bad = True
        else:
            print(f'  {kind:18} {got:4}   at ceiling')
        if verbose or got > ceiling:
            for rel, line, tok, why, ctx in defects[kind][:25]:
                print(f'      {rel.replace("SOMNARAK-WORLD/", "")[:52]:52}:{line:<5} {tok[:22]:22} {why}')
                if verbose:
                    print(f'          ...{ctx[:120]}...')

    print(f'  {"total":18} {total:4}')
    print('RESULT: ' + ('FAIL' if bad else 'PASS'))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
