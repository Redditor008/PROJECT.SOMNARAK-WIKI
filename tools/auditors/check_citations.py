#!/usr/bin/env python3
"""
tools/auditors/check_citations.py

Does the archive's citation network close?

Every dossier cites other dossiers by SECC code — `C-Iα-000`, `C-IIIβ-015`,
`N-Vω-1055`. That is how a reader follows a claim from one record to another, and
it is the one class of statement in this archive that is checkable without any
judgement at all: either the record named exists, or the citation is dead.

Three things are tested here.

1. A cited code resolves to a dossier file.       dead citation — fails
2. No two dossiers claim the same Designation.    collision — fails
3. A dossier's filename carries its own code.     stale filename — measured

The third is measured rather than failed because changing a filename is an
owner-file operation under A5, and because a filename and a header can disagree
with only one of them wrong. Where they disagree, this tool reports which is
which by asking the rest of the dossier: the Designation field, the Coherence
field and the Potency field all agree with each other, and only the filename
does not. That is what makes the stale one identifiable.

Also reported, never failed: which dossiers nothing cites. An archive that
cites itself unevenly is not broken, but the shape is worth seeing.
"""

import collections
import glob
import os
import re
import sys

DIRS = ['SOMNARAK-WORLD/Sorrow_Entities/SE-*.md',
        'SOMNARAK-WORLD/Unknown_Entities/SE-*.md']

RATCHET = {
    'dead-citation': 0,
    'duplicate-designation': 0,
    # Cleared in batch 138 on the owner's instruction. The two Kind Healer
    # variants were renamed to carry their own codes — `SE-C-Iβ-071b` and
    # `SE-C-IIγ-071c` — with the catalogue, the Entity Codex, the two in-world
    # Pages entries, the disposition index and the quote ledger all following.
    # The escalation is the point: serial 071 holds the lineage while the rank
    # and grade rise through it.
    'stale-filename': 0,
}

CODE = re.compile(r'\b([CNO])-(I{1,3}|IV|V)([αβγδω])-(\d{3})\b')
FILE_CODE = re.compile(r'^SE-([CNO]-(?:I{1,3}|IV|V)[αβγδω]-\d+[a-z]?)')
DESIGNATION = re.compile(r'\|\s*\*{0,2}Designation\*{0,2}\s*\|\s*`?([^`|\n]*)`?')
RANK_WORD = {'I': 'Residue', 'II': 'Echo', 'III': 'Fragment', 'IV': 'Entity', 'V': 'Sovereign'}


def field(text, label):
    m = re.search(r'\|\s*\*{0,2}' + re.escape(label) + r'\*{0,2}\s*\|\s*([^|\n]*)\|', text, re.I)
    return m.group(1).strip() if m else None


def load():
    paths = []
    for pat in DIRS:
        paths.extend(sorted(glob.glob(pat)))
    return sorted(set(paths))


def main(argv):
    verbose = '-v' in argv or '--verbose' in argv
    paths = load()

    texts, codes_owned = {}, {}
    for p in paths:
        with open(p, encoding='utf-8') as f:
            texts[p] = f.read()
        m = FILE_CODE.match(os.path.basename(p))
        if m:
            codes_owned.setdefault(m.group(1), []).append(p)

    defects = {'dead-citation': [], 'duplicate-designation': [], 'stale-filename': []}
    cited = collections.Counter()

    # -- designations each dossier files in its own header
    header = {}
    for p, t in texts.items():
        d = DESIGNATION.search(t)
        if d:
            header[p] = d.group(1).strip().split()[0].strip('`')

    by_header = collections.defaultdict(list)
    for p, h in header.items():
        by_header[h].append(p)
    for h, ps in by_header.items():
        if len(ps) > 1:
            defects['duplicate-designation'].append(
                (h, f'{len(ps)} dossiers file the same Designation: ' +
                    ', '.join(os.path.basename(q)[:44] for q in ps)))

    # -- citations resolve
    for p, t in texts.items():
        for m in CODE.finditer(t):
            code = f'{m.group(1)}-{m.group(2)}{m.group(3)}-{m.group(4)}'
            cited[code] += 1
            if code not in codes_owned and code not in by_header:
                defects['dead-citation'].append(
                    (os.path.basename(p), f'cites {code}, which no dossier files'))

    # -- filename carries the dossier's own code
    for p, h in header.items():
        m = FILE_CODE.match(os.path.basename(p))
        if not m:
            continue
        if m.group(1) != h:
            # establish which of the two is stale from the rest of the dossier
            coh = (field(texts[p], 'Coherence') or '')
            pot = (field(texts[p], 'Potency') or '')
            # The header carries two claims a filename also carries: a rank and
            # an element grade. Ask the dossier's own fields which side they
            # support, checking both — for 071b the ranks are identical and only
            # the element differs, so a rank-only test cannot decide it.
            hr = re.match(r'(I{1,3}|IV|V)', h.split('-')[1])
            hg = re.search(r'[αβγδω]', h.split('-')[1])
            word = RANK_WORD.get(hr.group(1)) if hr else None
            rank_ok = bool(word) and word.lower() in coh.lower()
            grade_ok = bool(hg) and hg.group(0) in pot
            if rank_ok or grade_ok:
                why = ('header agrees with this dossier\'s own ' +
                       ('Coherence' if rank_ok else '') +
                       (' and ' if rank_ok and grade_ok else '') +
                       ('Potency' if grade_ok else '') +
                       ', so the filename is stale')
            else:
                why = 'header, Coherence and Potency do not agree — needs a read'
            defects['stale-filename'].append(
                (os.path.basename(p), f'filename files {m.group(1)}, header files {h} — {why}'))

    n = {k: len(v) for k, v in defects.items()}
    print(f'CITATIONS — {len(paths)} dossiers · {sum(cited.values())} citations to '
          f'{len(cited)} distinct codes · {len(header)} Designation headers')

    bad = False
    for kind in ('dead-citation', 'duplicate-designation', 'stale-filename'):
        ceiling = RATCHET[kind]
        got = n[kind]
        if got > ceiling:
            print(f'  {kind:24} {got:4}   ABOVE CEILING {ceiling}')
            bad = True
        elif got < ceiling:
            print(f'  {kind:24} {got:4}   BELOW CEILING — lower it to {got}')
            bad = True
        else:
            print(f'  {kind:24} {got:4}   at ceiling' +
                  ('   (held under A5)' if kind == 'stale-filename' else ''))
        if verbose or got > ceiling:
            for f, why in defects[kind]:
                print(f'      {f[:52]:52} {why[:120]}')

    orphans = [p for p, h in header.items() if cited.get(h, 0) == 0]
    print(f'  {"uncited dossiers":24} {len(orphans):4}   reported only — no other record names them')

    print('RESULT: ' + ('FAIL' if bad else 'PASS'))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
