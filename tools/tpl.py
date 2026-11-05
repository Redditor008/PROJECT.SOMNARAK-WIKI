#!/usr/bin/env python3
"""Template-residue census for the SE/UE dossiers (Workstream 6).

Workstream 1 measured shared *body* prose at a 30-dossier threshold and drove it
to 0.00%. That scope deliberately excluded table rows, blockquotes and headings
(`tools/boilerplate_report.py`, `body` scope), so slot-filled table cells and
placeholder-instruction cells left by the previous AI survived the whole
campaign. This tool measures exactly what that scope could not see.

A line is RESIDUE when it is shared by >= THRESHOLD dossiers, carries >= 10
words of content, and is not sanctioned furniture.

Sanctioned furniture (a *label* may repeat; a *value* may not):
  - markdown table header / separator rows,
  - the system blockquotes (R.D. Operational Record, Mechanics Reference,
    R.D. Field Parameters, M.A.W. definition, Object/Place Work Rule,
    "Progressive declassified records"),
  - rows whose value is derived from the SECC code itself (potency and
    coherence modifiers, entity role/type, sorrow category, valid work types,
    work difficulty, comprehension level, vessel-destructible, the barred work-type
    rows read off the Threat Score, the fixed-object Speed row, the
    "no breach counter" activation row, and the Stationary/Mobile movement row),
  - the two global combat rules (Falloff Rule, Damage Application).

Usage:
    tpl.py                 census over all dossiers
    tpl.py --top N         list the N worst residue lines
    tpl.py <path> [...]    per-file residue listing
"""
import os
import re
import sys
import collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WINGS = ['SOMNARAK-WORLD/Sorrow_Entities', 'SOMNARAK-WORLD/Unknown_Entities']
THRESHOLD = 10

# A dossier is a file that carries an SECC designation. The wings also hold a
# README each and one long-form log; counting those as dossiers made this census
# report 302 where every auditor reports 301, and the two numbers were quoted
# against each other for three batches.
DESIGNATION = re.compile(r'(?:\*\*Designation\*\*|SECC Designation):?\*{0,2}\s*\|?\s*`?'
                         r'([CNO])-(I{1,3}|IV|V)([\u03b1\u03b2\u03b3\u03b4\u03c9])-(\d+[a-z]?)')

FURNITURE = [
    r'^\|\s*Name / Category\s*\|',
    r'^\|\s*Work Type\s*\|\s*Response\s*\|',
    r'^\|\s*Stage\s*\|\s*Required record\s*\|',
    r'^\|\s*Related entity\s*\|',
    r'^\|\s*Observation stage\s*\|',
    r'^\|\s*Activation field\s*\|',
    r'^\|\s*Field\s*\|\s*Detail\s*\|',
    r'^\|\s*-{2,}',
    r'^>\s*\*\*R\.D\. Operational Record:',
    r'^>\s*\*\*R\.D\. Field Parameters:',
    r'^>\s*\*\*Mechanics Reference:',
    r'^>\s*\*\*Materialized Agony Wear',
    r'^>\s*\*\*Object/Place Work Rule:',
    r'^>\s*Progressive declassified records',
    r'^\|\s*\*\*(Potency|Coherence) modifier\*\*\s*\|',
    r'^\|\s*\*\*Entity (role|Type)\*\*\s*\|',
    r'^\|\s*\*\*Sorrow Category\*\*\s*\|',
    r'^\|\s*\*\*Valid Work Types\*\*\s*\|',
    r'^\|\s*\*\*Work difficulty\*\*\s*\|',
    r'^\|\s*\*\*R\.D\. Comprehension Level\*\*\s*\|',
    r'^\|\s*\*\*Vessel-Destructible\*\*\s*\|',
    # The barred pair reads off the Threat Score (R-41). The legacy tokens stay
    # in the pattern so a half-migrated file is exempted here and reported by
    # check_work_preference, rather than being filed as a copied value.
    r'^\|\s*\*\*(Flerehan|Pugnahan)\*\*[^|]*\|\s*\*{0,2}(?:N/A|0%|-100%|Net-Neutral|Negative-Low)',
    r'^\|\s*\*\*Speed\*\*\s*\|\s*N/A',
    r'^\|\s*\*\*Activation threshold\*\*\s*\|\s*Activation / expansion trigger',
    r'^\|\s*\*\*Movement\*\*\s*\|\s*(Stationary|Mobile)\b',
    r'^\*\*Falloff Rule:',
    r'^\*\*Damage Application:',
]
FURNITURE = [re.compile(p) for p in FURNITURE]


def dossiers():
    """Every file in the wings that is a dossier, and every file that is not."""
    out, other = [], []
    for d in WINGS:
        for f in sorted(os.listdir(os.path.join(ROOT, d))):
            if not f.endswith('.md') or f == 'README.md':
                continue
            p = os.path.join(ROOT, d, f)
            with open(p, encoding='utf-8') as fh:
                text = fh.read()
            (out if DESIGNATION.search(text) else other).append(p)
    return out, other


def candidate(s):
    """Is this line in scope at all (content-bearing, not a heading/furniture)?"""
    if s.startswith('#') or len(s) < 40:
        return False
    if len(re.sub(r'[`*|>]', ' ', s).split()) < 10:
        return False
    return not any(p.search(s) for p in FURNITURE)


def census():
    files, other = dossiers()
    owner = collections.defaultdict(set)
    for p in files:
        with open(p, encoding='utf-8') as fh:
            for ln in fh:
                s = ln.strip()
                if candidate(s):
                    owner[s].add(p)
    shared = {s: v for s, v in owner.items() if len(v) >= THRESHOLD}
    return files, shared, other


def main():
    args = sys.argv[1:]
    paths = [a for a in args if not a.startswith('-') and not a.isdigit()]
    files, shared, other = census()
    if paths:
        for p in paths:
            ap = p if p.startswith('/') else os.path.join(ROOT, p)
            n = 0
            with open(ap, encoding='utf-8') as fh:
                for i, ln in enumerate(fh, 1):
                    s = ln.strip()
                    if s in shared:
                        n += 1
                        print('%5d  [%3d dossiers]  %s' % (i, len(shared[s]), s[:150]))
            print('RESIDUE %d  %s' % (n, os.path.basename(ap)))
        return
    inst = sum(len(v) for v in shared.values())
    dirty = set()
    for v in shared.values():
        dirty |= v
    print('dossiers                      %d  (%d file%s with no SECC designation)'
          % (len(files), len(other), '' if len(other) == 1 else 's'))
    print('distinct residue lines        %d  (shared by >= %d dossiers)'
          % (len(shared), THRESHOLD))
    print('residue instances             %d' % inst)
    print('dossiers carrying residue     %d / %d' % (len(dirty), len(files)))
    print('clean dossiers                %d' % (len(files) - len(dirty)))
    if '--top' in args:
        n = int(args[args.index('--top') + 1])
        top = sorted(((len(v), s) for s, v in shared.items()), reverse=True)[:n]
        print()
        for c, s in top:
            print('%4d  %s' % (c, s[:160]))


if __name__ == '__main__':
    main()
