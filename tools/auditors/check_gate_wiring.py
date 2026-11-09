#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_gate_wiring.py — gate 92: a gate that is not invoked is a document, not a gate.

WHY THIS EXISTS

Batch 206 added `check_rule_index.py` and called it gate 90. It was written, tested, cited in the
CHANGELOG, cited in `WORK_IN_PROGRESS.md`, cited in `RULES/README.md`, and named as a standard in
`how_finished.py` — and it was never added to `tools/gate.sh`. It could not fail a build. Every
document said the archive was guarded against an unindexed rule; the only file that runs gates
said nothing about it.

That is the exact shape of a status that is not earned, so it gets a gate of its own: every auditor
`how_finished.py` measures must appear in `tools/gate.sh`.

WHAT FAILS

  * a gate named in `how_finished.STANDARDS` that `tools/gate.sh` never invokes.

WHAT IS REPORTED

  * how many distinct gates are cited, and how many of them are wired, so a check that matched
    nothing is visible instead of green.

    python3 tools/auditors/check_gate_wiring.py
    python3 tools/auditors/check_gate_wiring.py -v
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GATE_SH = os.path.join(ROOT, 'tools', 'gate.sh')

if ROOT not in sys.path:
    sys.path.insert(0, ROOT)


def cited():
    """Every distinct auditor path that how_finished.py measures."""
    from tools.auditors import how_finished
    out = []
    for _name, gate, _pat, _against in how_finished.STANDARDS:
        if gate not in out:
            out.append(gate)
    return out


def compare(paths, text):
    """Pure: which cited gates the build script never invokes."""
    return [p for p in paths if p not in text]


def main(argv):
    verbose = '-v' in argv
    paths = cited()
    text = io.open(GATE_SH, encoding='utf-8').read()
    missing = compare(paths, text)
    absent = [p for p in paths if not os.path.exists(os.path.join(ROOT, p))]
    if verbose:
        for p in paths:
            print('%-58s %s' % (p, 'wired' if p not in missing else 'NOT WIRED'))
    print('gates cited by how_finished: %d · invoked by gate.sh: %d'
          % (len(paths), len(paths) - len(missing)))
    print('gates cited but not wired: %d' % len(missing))
    if missing:
        for p in missing:
            print('  not wired: %s' % p)
        print('RESULT: FAIL — %d gates cited but never invoked' % len(missing))
        return 1
    if absent:
        for p in absent:
            print('  cited but absent from disk: %s' % p)
        print('RESULT: FAIL — %d cited gates do not exist' % len(absent))
        return 1
    print('RESULT: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
