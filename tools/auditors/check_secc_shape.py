#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_secc_shape.py — gate 91: the SECC table answers one question per row (R-51).

WHY THIS EXISTS

The dossier template, `TEMPLATES/SE/01_SORROW_ENTITY_DOSSIER_TEMPLATE.md`, states the two rows:

    | **Coherence** | {{Rank Written}} ({{I-V}}) — {{Behaviour descriptor}} |
    | **Potency**   | {{Potency Written}} ({{α/β/γ/δ/ω}}) — {{Threat descriptor}} |

So each row carries **one value and, at most, one descriptor**. Nothing measured that. Seven
dossiers had written the pair backwards — `I — Residue (barely formed)` instead of
`Residue (I) — Barely formed` — and five had let the descriptor become a sentence: a clause of
behaviour with its own finite verb, which is the thing `R-45` §3 was objecting to and the thing a
table row cannot hold.

WHAT FAILS

  * a cell that is not `Value (Symbol)`, optionally followed by `— descriptor`;
  * a cell whose word and symbol disagree (`Fragment (IV)`);
  * a cell whose symbol disagrees with the `Designation` code (`C-IIIβ-014`);
  * a descriptor longer than twelve words, or ending in a full stop — a sentence in a cell.

WHAT IS REPORTED

  * how many cells carry a value only and how many carry a descriptor, so a gate that silently
    matched nothing is visible rather than green.

The vocabularies are the ones the world pages state, not a memory of them:
  rank names — `Pages/38-Classification Code.md` §3;
  grade names — `Pages/38-Classification Code.md` §4 and `Pages/07-Sorrow Entities.md` line 64.

    python3 tools/auditors/check_secc_shape.py
    python3 tools/auditors/check_secc_shape.py -v
"""
import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

RANKS = {'I': 'Residue', 'II': 'Echo', 'III': 'Fragment', 'IV': 'Entity', 'V': 'Sovereign'}
GRADES = {'α': 'Minor', 'β': 'Moderate', 'γ': 'Major', 'δ': 'Critical', 'ω': 'Catastrophic'}

COHERENCE = re.compile(r'^(Residue|Echo|Fragment|Entity|Sovereign) \((I|II|III|IV|V)\)'
                       r'(?: — (.+))?$')
POTENCY = re.compile(r'^(Minor|Moderate|Major|Critical|Catastrophic) \((α|β|γ|δ|ω)\)'
                     r'(?: — (.+))?$')
DESIGNATION = re.compile(r'\*\*Designation\*\*\s*\|\s*`[A-Z]-([IV]+)([αβγδω])')
SECTION = re.compile(r'^## SECC Classification\s*$(.*?)(?=^## )', re.M | re.S)
CELL = r'^\|\s*\*\*%s\*\*\s*\|\s*([^|\n]+?)\s*\|\s*$'
MAX_WORDS = 12


def dossier_files():
    out = []
    for path in sorted(glob.glob(os.path.join(ROOT, 'SOMNARAK-WORLD/**/SE-*.md'), recursive=True)):
        if 'MAW_Codex' in path:
            continue
        out.append(path)
    return out


def read_row(section, field):
    m = re.search(CELL % field, section, re.M)
    return m.group(1).strip() if m else None


def audit(text):
    """(issues, counters) for one dossier. Pure — the tests drive it without touching disk."""
    issues = []
    stats = {'files': 0, 'coherence value': 0, 'coherence +desc': 0,
             'potency value': 0, 'potency +desc': 0, 'designation': 0}
    sec = SECTION.search(text)
    if not sec:
        return [('no SECC Classification section', '')], stats
    stats['files'] = 1
    body = sec.group(1)
    code = DESIGNATION.search(text)
    stats['designation'] = 1 if code else 0

    for field, rx, table, idx in (('Coherence', COHERENCE, RANKS, 1),
                                  ('Potency', POTENCY, GRADES, 2)):
        cell = read_row(body, field)
        if cell is None:
            issues.append(('no %s row' % field, ''))
            continue
        m = rx.match(cell)
        if not m:
            issues.append(('%s not "Value (Symbol)"' % field, cell))
            continue
        word, sym = m.group(1), m.group(2)
        if table.get(sym) != word:
            issues.append(('%s word/symbol disagree' % field, cell))
            continue
        if code and sym != (code.group(1) if idx == 1 else code.group(2)):
            issues.append(('%s disagrees with Designation' % field, cell))
        desc = m.group(3)
        if desc:
            stats['%s +desc' % field.lower()] += 1
            words = len(desc.split())
            if words > MAX_WORDS:
                issues.append(('%s descriptor is a sentence (%d words)' % (field, words), desc))
            elif desc.rstrip().endswith('.'):
                issues.append(('%s descriptor ends in a full stop' % field, desc))
        else:
            stats['%s value' % field.lower()] += 1
    return issues, stats


def main(argv):
    verbose = '-v' in argv
    total = {'files': 0, 'coherence value': 0, 'coherence +desc': 0,
             'potency value': 0, 'potency +desc': 0, 'designation': 0}
    bad = []
    for path in dossier_files():
        issues, stats = audit(io.open(path, encoding='utf-8').read())
        for k in total:
            total[k] += stats[k]
        for why, cell in issues:
            bad.append((os.path.basename(path), why, cell))
    if verbose:
        for row in bad:
            print('%-54s %-44s %s' % (row[0][:52], row[1], row[2][:60]))
    print('dossiers read %d' % len(dossier_files()))
    print('coherence — value only %d · with descriptor %d'
          % (total['coherence value'], total['coherence +desc']))
    print('potency   — value only %d · with descriptor %d'
          % (total['potency value'], total['potency +desc']))
    print('designation codes cross-checked %d of %d' % (total['designation'], len(dossier_files())))
    print('secc cells off contract: %d' % len(bad))
    if bad:
        print('RESULT: FAIL — %d SECC cells off contract' % len(bad))
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
