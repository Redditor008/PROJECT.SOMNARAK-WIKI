#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_gate_numbers.py — gate 49: a gate number means one script (R-53, O-39).

WHY THIS EXISTS

Between batch 202 and batch 212 the archive began citing gates by number — *"check_relic_gauge.py
(gate 93)"*, *"check_gate_wiring.py (gate 92)"* — and no register ever defined what a number meant.
The numbers were assigned ad hoc, batch by batch, by whoever was writing at the time. So:

    gate 92  was claimed by  check_relic_interaction_damage.py  and  check_gate_wiring.py
    gate 93  was claimed by  check_relic_gauge.py              and  check_section_registry.py

Four documents cited two different scripts by the same number, and both citations were internal
links to nothing. A number that two gates answer to is not a number.

THE DEFINITION

`REFERENCE_SOMNARAK_WIKI/GATES.md` numbers every gate by **its position in `tools/gate.sh`** — the
order the build runs them. That is derived, not invented, so it cannot drift while the build stands.

WHAT FAILS

  * `GATES.md` disagreeing with `tools/gate.sh` in either direction;
  * a prose citation pairing a script with a number the register gives to something else;
  * a prose citation naming a number the register does not have.

    python3 tools/auditors/check_gate_numbers.py
    python3 tools/auditors/check_gate_numbers.py -v
"""
import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GATE_SH = os.path.join(ROOT, 'tools', 'gate.sh')
GATES_MD = os.path.join(ROOT, 'REFERENCE_SOMNARAK_WIKI', 'GATES.md')
DOC_DIR = os.path.join(ROOT, 'REFERENCE_SOMNARAK_WIKI')

BUILD = re.compile(r'^check\s+"([^"]*)"\s+python3\s+(\S+)')
ROW = re.compile(r'^\|\s*\*\*(\d+)\*\*\s*\|\s*`([^`]+)`')
# `check_x.py` (gate 44)   ·   `check_x.py` (gate 44, ...
CITE = re.compile(r'`([A-Za-z0-9_/]+\.py)`\s*\((?:gate|Gate)\s*(\d+)')
# a bare "(gate 44)" with no script in front of it
BARE = re.compile(r'\((?:gate|Gate)\s*(\d+)\)')


def build_gates():
    """[(script, expected pass string)] in build order — the definition of a gate number."""
    out = []
    with io.open(GATE_SH, encoding='utf-8') as fh:
        for line in fh:
            m = BUILD.match(line.rstrip('\n'))
            if m:
                out.append((m.group(2), m.group(1)))
    return out


def registered():
    """{number: script} as GATES.md states it."""
    out = {}
    with io.open(GATES_MD, encoding='utf-8') as fh:
        for line in fh:
            m = ROW.match(line.rstrip('\n'))
            if m:
                out[int(m.group(1))] = m.group(2)
    return out


def compare(build, table):
    """Differences between the build and the register. Pure — the tests drive it."""
    issues = []
    if len(build) != len(table):
        issues.append(('count', 'build runs %d gates, GATES.md lists %d' % (len(build), len(table))))
    for i, (script, _passes) in enumerate(build, 1):
        if i in table and table[i] != script:
            issues.append(('register', 'gate %d is %s in the build but %s in GATES.md'
                           % (i, script, table[i])))
        elif i not in table:
            issues.append(('register', 'gate %d (%s) has no GATES.md row' % (i, script)))
    for n in table:
        if n > len(build):
            issues.append(('register', 'GATES.md lists gate %d, the build has only %d'
                           % (n, len(build))))
    return issues


def citations(text):
    """[(script, number)] for every citation that pairs a script with a gate number."""
    return [(m.group(1), int(m.group(2))) for m in CITE.finditer(text)]


def bad_citations(texts, table):
    """Citations whose number does not match the register. Pure."""
    issues = []
    by_script = {}
    for n, script in table.items():
        by_script.setdefault(os.path.basename(script), []).append(n)
    for name, text in texts:
        for script, num in citations(text):
            base = os.path.basename(script)
            if num not in table:
                issues.append((name, '%s cites gate %d, which the register does not have'
                               % (base, num)))
            elif os.path.basename(table[num]) != base:
                issues.append((name, '%s is cited as gate %d, but gate %d is %s'
                               % (base, num, num, os.path.basename(table[num]))))
        # a bare number that resolves to nothing at all
        for m in BARE.finditer(text):
            n = int(m.group(1))
            if n not in table and CITE.search(text[max(0, m.start() - 90):m.start()]) is None:
                issues.append((name, 'cites gate %d, which the register does not have' % n))
    return issues


def docs():
    out = []
    for path in sorted(glob.glob(os.path.join(DOC_DIR, '**', '*.md'), recursive=True)):
        with io.open(path, encoding='utf-8') as fh:
            out.append((os.path.relpath(path, ROOT), fh.read()))
    return out


def main(argv):
    verbose = '-v' in argv
    build = build_gates()
    table = registered()
    issues = compare(build, table)
    citation_issues = bad_citations(docs(), table)
    issues = [('register: ' + w, d) for w, d in issues] + \
             [('cited: ' + n, d) for n, d in citation_issues]
    if verbose:
        for kind, detail in issues:
            print('%-58s %s' % (kind[:56], detail))
    print('gates the build runs %d · gates GATES.md numbers %d' % (len(build), len(table)))
    print('gate citations that disagree with the register: %d' % len(citation_issues))
    print('gate-number defects: %d' % len(issues))
    if issues:
        print('RESULT: FAIL — %d gate-number defects' % len(issues))
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
