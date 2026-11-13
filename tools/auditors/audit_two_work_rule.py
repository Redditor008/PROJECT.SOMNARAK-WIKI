#!/usr/bin/env python3
"""audit_two_work_rule.py — do the non-Subject dossiers carry the barred pair?

Scratch report, not a gate. It used to look for `Flerehan | N/A` and
`Pugnahan | N/A` inside a `## Operational Parameters` section; both halves of that
reading were retired — batch 155b replaced `N/A` in a barred cell with a word, and
batch 159 replaced the words with **Net-Neutral** / **Negative-Low** read off the
Threat Score — so the report said 0% compliant against a rule the owner had
already overruled, and it crashed on a missing `import os` before it could say so.

The reading is now the gate's own (`check_work_preference.vector_of`), so this
report cannot drift from `R-41` again.
"""
import glob
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import check_work_preference as pref  # noqa: E402


def main():
    non_subjects, compliant, needs_fix = [], [], []
    for path in sorted(glob.glob('SOMNARAK-WORLD/Sorrow_Entities/*.md')):
        if 'README' in path:
            continue
        text = open(path, encoding='utf-8').read()
        if not pref.is_relic(text):
            continue
        non_subjects.append(path)
        vec = pref.vector_of(text)
        if vec and vec[0] in pref.BAR and vec[1] in pref.BAR:
            compliant.append(path)
        else:
            needs_fix.append((path, vec))
    print('Total Non-Subject Entities (Object, Place, Time): %d' % len(non_subjects))
    pct = 100.0 * len(compliant) / len(non_subjects) if non_subjects else 0.0
    print('Carrying the barred pair as words: %d / %d (%.1f%%)'
          % (len(compliant), len(non_subjects), pct))
    print('Entities needing Two-Work-Type Rule alignment: %d' % len(needs_fix))
    if needs_fix:
        print('Sample needing alignment: %s'
              % [os.path.basename(p) for p, _ in needs_fix[:5]])
    return 0


if __name__ == '__main__':
    sys.exit(main())
