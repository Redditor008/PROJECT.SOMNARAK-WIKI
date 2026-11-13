#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_dossier_world_pointer.py — gate 57: a dossier points at the world, not at a filename.

THE OWNER'S INSTRUCTION

    *"ALSO IN THE DOSSIER THERE SHOULD NEVER BE A .md MENTION USED OTHER WAY TO POINT
     OTHER FILE IN A DOSSIER THAT SHOULD ACT AS IF IT WAS A DOSSIER"*

A dossier is an in-world document. A reader inside the world cannot see a filename, a
folder path, or a section number in a research register — those are facts about the
archive, not about the city. When the Director's dossier said

    **shielding him from terminal psychic dissolution** (`The_MEMORY_ARCHIVE.md` § 3.2)

it stepped out of the world to wave at the shelf. The sentence already opens with *"The
Memory Archive holds the manner of her death"*, so the pointer was not even carrying the
attribution; it was carrying the filing cabinet.

WHAT IS A DEFECT

  * `bare-filename`  a `.md` name a reader can see — in prose, in a code span, in a table
                     cell. This is the class the owner named.
  * `folder-path`    `SOMNARAK-WORLD/`, `Master_Codices/`, `REFERENCE_SOMNARAK_WIKI/`,
                     `tools/` — a shelf, not a record.
  * `section-cite`   a bare `§ 3.2` / `§ 4` cross-file section number. In-world records say
                     "the Archive's third register", "the north wall register", "Floor 07".

WHAT IS NOT A DEFECT, AND WHY

  * a markdown **link**. `[The Debt Scale](SE-C-IIIβ-015_The_Debt_Scale_빚의_저울.md)` renders
    as *The Debt Scale* — the filename is in the destination and never on the page. The
    archive needs 2,276 of these to navigate at all, and every one of them renders in-world.
    The rule is therefore about **visible text**, not about bytes: a `.md` may exist in a
    link destination and nowhere else.
  * `the file` / `in this file`. A classified dossier is a file. R-01 permits in-world
    self-reference; this gate does not police it.
  * a filename in a backstory file's **appendix**. That appendix is the archive's own
    apparatus and cites records by name because the structure standard (§X.3) requires it.
    The story body above it is held to the full rule.
  * `filed`, `filing`, `case file`, `evidence file` — the world's own vocabulary.

THE MEASUREMENT

Every dossier is read, every link destination is replaced by its label, and what is left is
what a reader sees. That text may not contain a filename, a folder path, or a bare section
citation. Ceiling is zero and stays zero; there is no debt register, because the two files
that carried the class were fixed in the batch that created the rule.

    python3 tools/auditors/check_dossier_world_pointer.py
    python3 tools/auditors/check_dossier_world_pointer.py -v
"""
import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# A dossier: the nine Echo-Core records and the Sorrow-Entity filings.
DOSSIERS = (
    'SOMNARAK-WORLD/Echo_Cores/THE_*.md',
    'SOMNARAK-WORLD/Sorrow_Entities/SE-*.md',
    'SOMNARAK-WORLD/Unknown_Entities/SE-*.md',
)

# A backstory file is a story with an appendix. The **story body** is held to the same rule,
# because it is read as prose; the appendix is archive apparatus and cites records by name on
# purpose (the structure standard requires each fact tied to the file that carries it). So the
# appendix is cut before the test, not exempted inside it.
BACKSTORY = 'SOMNARAK-WORLD/Echo_Cores/Backstory_Extended/*.md'
APPENDIX = '\n## Appendix'

LINK = re.compile(r'\[([^\]]*)\]\([^)]*\)', re.S)

LEAKS = [
    ('bare-filename',
     # the backtick must NOT be in the lookbehind: a filename in a code span is the exact
     # class the owner named, and excluding it made the gate blind to its own first case.
     re.compile(r'(?<![\w\-\.])[A-Za-z0-9_\-][A-Za-z0-9_\-\.]*\.md\b'),
     'a filename on the page'),
    ('folder-path',
     re.compile(r'(?:SOMNARAK-WORLD|Master_Codices|REFERENCE_SOMNARAK_WIKI|Gieok_Jeojangso|'
                r'Backstory_Extended|Sorrow_Entities|Unknown_Entities)/|\btools/'),
     'a folder path on the page'),
    ('section-cite',
     re.compile(r'§{1,2}\s*\d'),
     'a section number from the archive, not the record'),
]

# The H1 of an SE file is its own title; a filename appearing there would already have been
# caught by the filename/H1 dashboard. No exemption is needed for it, and none is granted.
EXEMPT_LINE = re.compile(r'^\s*(?:```|\|?\s*<!--)')


def visible(text):
    """What a reader sees: every link replaced by its label."""
    return LINK.sub(lambda m: m.group(1), text)


def scan(path, cut_appendix=False):
    out = []
    with io.open(path, encoding='utf-8', errors='replace') as f:
        raw = f.read()
    if cut_appendix:
        i = raw.find(APPENDIX)
        if i > 0:
            raw = raw[:i]
    body = visible(raw)
    for kind, pat, why in LEAKS:
        for m in pat.finditer(body):
            line = body[:m.start()].count('\n') + 1
            ctx = body[max(0, m.start() - 55):m.end() + 55].replace('\n', ' ').strip()
            out.append((kind, line, m.group(0), why, ctx))
    return out


def main(argv):
    verbose = '-v' in argv or '--verbose' in argv
    paths, bodies = [], []
    for pat in DOSSIERS:
        paths.extend(sorted(glob.glob(os.path.join(ROOT, pat))))
    bodies.extend(sorted(glob.glob(os.path.join(ROOT, BACKSTORY))))
    # a glob that matches nothing is not a pass
    if not paths:
        print('RESULT: FAIL — no dossier matched; the gate measured nothing')
        return 1

    defects = []
    for p in paths:
        for d in scan(p):
            defects.append((p.replace(ROOT + os.sep, '').replace(os.sep, '/'),) + d)
    for p in bodies:
        for d in scan(p, cut_appendix=True):
            defects.append((p.replace(ROOT + os.sep, '').replace(os.sep, '/') + ' [story body]',) + d)

    print(f'DOSSIER WORLD POINTER — {len(paths)} dossiers + {len(bodies)} backstory story bodies read, '
          f'ceiling 0')
    if defects:
        for rel, kind, line, tok, why, ctx in defects[:40]:
            print(f'  {rel}:{line}  [{kind}] {tok!r} — {why}')
            if verbose:
                print(f'      …{ctx}…')
        print(f'pointers visible on the page: {len(defects)}')
        print(f'RESULT: FAIL — {len(defects)} pointer(s) that a reader can see')
        return 1

    print('  bare-filename  0  ·  folder-path  0  ·  section-cite  0')
    print('pointers visible on the page: 0')
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
