#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_section_registry.py — gate 93: every dossier carries the sections its template asks for.

WHY THIS EXISTS

`R-45` §3 says every section is written to its contract; it never said what happens when the
section is simply not there. A gate that reads the sections it finds cannot see a section that is
missing — it reports a clean ratio over a file that is short. Batch 205 found four dossiers with no
Tale at all, and the standard had been printing green over them for eleven batches.

This gate reads the template, not a list, and asks of every dossier: are the sections here?

WHAT IS REQUIRED

Fourteen sections every dossier carries, one of `Combat Record` / `Contact Record`, and one of
`Behavior` (a subject) / `Handling Process` (a relic) — the template's own alternates, chosen from
the `**Entity Type**` row. `Apex Record` is required on Rank IV and V only, because the template
scopes it that way (*"Where this is a Rank IV–V record"*).

WHAT FAILS

  * a dossier missing a section it is required to carry, and not already listed in `DEBT`.

WHAT IS REPORTED

  * the total number missing, so `how_finished.py` can call the standard OPEN rather than DONE;
  * the number that are *new* — those are what fail the build.

`DEBT` is a dated snapshot, not a policy. Batch 208 recorded 29 gaps and three batches paid every
one of them; the list is now **empty**, which is the state it should stay in. The mechanism is kept
deliberately: a missing section now fails the build on the first dossier it appears in, with no
ratchet to absorb it.

    python3 tools/auditors/check_section_registry.py
    python3 tools/auditors/check_section_registry.py -v
"""
import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# The template's scaffold, after the category alternates have been resolved.
ALWAYS = [
    'SECC Classification', 'Operational Parameters', 'Appearance', 'Origin',
    'M.A.W. Equipment', '관찰 기록 (Observation Log)', '이야기 보고 (Story Log)',
    '최종 관찰 (Final Observation)', '감각 묘사 (Flavor Text)', '이야기 (Narratio)',
    '증언 (Testimonium)', '기록 (Registrum)', 'Trivia', 'Document Information',
]
EITHER = ['Combat Record', 'Contact Record']
HIGH_RANK = ('IV', 'V')

# Measured 2026-11-05. Batch 208 recorded 29 gaps; 210 closed 16, 211 closed 5, 212 closed the last
# 8. **The debt is empty** — the mechanism stays so that the next missing section fails immediately
# instead of being ratcheted.
DEBT = {}


def dossier_files():
    return [p for p in sorted(glob.glob(os.path.join(ROOT, 'SOMNARAK-WORLD/**/SE-*.md'),
                                        recursive=True))
            if 'MAW_Codex' not in p]


def read(path):
    with io.open(path, encoding='utf-8') as fh:
        return fh.read()


def designation(text):
    """The dossier's own code, as the file writes it: `C-Vγ-225`, `N-IIIβ-1056`."""
    m = re.search(r'\*\*Designation\*\*\s*\|\s*`([A-Z])-([IV]+)([αβγδω])-(\d+[a-z]?)', text)
    return '%s-%s%s-%s' % (m.group(1), m.group(2), m.group(3), m.group(4)) if m else None


def audit(text):
    """(the sections this dossier is required to carry but does not, its designation). Pure."""
    heads = [h.strip() for h in re.findall(r'^## (.+?)$', text, re.M)]
    rank = designation(text)

    def has(prefix):
        return any(h.startswith(prefix) for h in heads)

    missing = [s for s in ALWAYS if not has(s)]
    if not any(has(a) for a in EITHER):
        missing.append(' / '.join(EITHER))

    et = re.search(r'^\|\s*\*\*Entity Type\*\*\s*\|\s*(.+?)\s*\|$', text, re.M)
    is_subject = bool(et and re.match(r'[\* ]*Subject', et.group(1).strip()))
    wanted = 'Behavior' if is_subject else 'Handling Process'
    if not has(wanted):
        missing.append(wanted)

    if rank and rank.split('-')[1][:-1] in HIGH_RANK and not has('Apex Record'):
        missing.append('Apex Record')
    return missing, rank


def split_debt(gaps, debt=None):
    """Which gaps are new, and which were already recorded. Pure — the tests drive it."""
    debt = DEBT if debt is None else debt
    new, known = [], []
    for code, missing in gaps:
        recorded = debt.get(code, set())
        for section in missing:
            (known if section in recorded else new).append((code, section))
    return new, known


def main(argv):
    verbose = '-v' in argv
    gaps = []
    for path in dossier_files():
        missing, code = audit(read(path))
        if missing:
            gaps.append((code or os.path.basename(path), missing))
    new, known = split_debt(gaps)
    if verbose:
        for code, missing in gaps:
            print('%-14s %s' % (code, ', '.join(missing)))
    total = len(new) + len(known)
    print('dossiers read %d' % len(dossier_files()))
    print('sections missing: %d' % total)
    print('  recorded debt: %d' % len(known))
    print('  not in the recorded debt: %d' % len(new))
    if new:
        for code, section in new:
            print('  NEW GAP %s — %s' % (code, section))
        print('RESULT: FAIL — %d sections missing that no record accounts for' % len(new))
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
