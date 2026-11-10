#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""how_finished.py — how much of this archive is actually finished.

WHY THIS EXISTS

Every gate in this repository ratchets. A ratchet means *"no worse than yesterday"*, not *"done"*.
When a gate prints `RESULT: PASS` with `131 remaining` above it, the pass is honest and the work is
not, and reading only the PASS line is how five batches went out claiming a rollout that had not
happened.

So this tool asks the only question a reader actually has, and asks it once:

    of the standing standards, how many dossiers are actually finished?

A standard counts as **DONE only when nothing remains**. Anything with a ratchet above zero is
**OPEN**, whatever its gate prints.

    python3 tools/auditors/how_finished.py
    python3 tools/auditors/how_finished.py -v     # name the open files for the smaller standards

The patterns below are deliberately narrow. If a gate's output format changes, this tool reports
UNKNOWN for that standard rather than guessing — a dashboard that invents its numbers is worse than
no dashboard.
"""
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# name, gate, the regex that captures "how many remain", what it is measured against
STANDARDS = [
    # name, gate, the regex capturing HOW MANY REMAIN, the unit that remains
    ('Work Preference — off the alphabet',
     'tools/auditors/check_work_preference.py',
     r'off alphabet:\s*(\d+)', 'dossiers'),
    ('Work Preference — printing a percentage',
     'tools/auditors/check_work_preference.py',
     r'printing a percentage:\s*(\d+)', 'dossiers'),
    ('Work Damage — a per-second dose (R-47)',
     'tools/auditors/check_work_damage.py',
     r'work-damage failures:\s*(\d+)', 'dossiers'),
    ('SE Effect — 135 of 301 carry one (R-50)',
     'tools/auditors/check_se_effect.py',
     r'se-effect failures:\s*(\d+)', 'dossiers'),
    ('Work Effect — three verdicts, 101/39/15 (R-49)',
     'tools/auditors/check_work_effect.py',
     r'work-effect failures:\s*(\d+)', 'subjects'),
    ('Relic charge / gauge (R-48)',
     'tools/auditors/check_relic_gauge.py',
     r'malformed, off-tier, or still on \[HP\]\s*(\d+)', 'relic dossiers'),
    ('Relic interaction damage (R-47)',
     'tools/auditors/check_relic_interaction_damage.py',
     r'still on a session range\s*(\d+)', 'relic dossiers'),
    ('No Work Type table on a relic (O-08/R-40)',
     'tools/auditors/check_relic_work_types.py',
     r'relic dossiers still carrying Work Types:\s*(\d+)', 'relic dossiers'),
    ('Every rule on disk is indexed (O-30)',
     'tools/auditors/check_rule_index.py',
     r'rules filed and not indexed:\s*(\d+)', 'rules'),
    ('SECC answers one question per row (R-51)',
     'tools/auditors/check_secc_shape.py',
     r'secc cells off contract:\s*(\d+)', 'cells'),
    ('A gate cited is a gate wired (O-37)',
     'tools/auditors/check_gate_wiring.py',
     r'gates cited but not wired:\s*(\d+)', 'gates'),
    ('Every required section is present (R-45 s3)',
     'tools/auditors/check_section_registry.py',
     r'sections missing:\s*(\d+)', 'sections'),
    ('Every command ends in a file (R-52 / O-38)',
     'tools/auditors/check_command_capture.py',
     r'commands with no entry:\s*(\d+)', 'commands'),
    ('A number names one gate (R-53 / O-39)',
     'tools/auditors/check_gate_numbers.py',
     r'gate-number defects:\s*(\d+)', 'citations'),
    ('Appearance names a shape family (R-32 / O-14)',
     'tools/auditors/check_appearance_contract.py',
     r'unfiled shapes:\s*(\d+)', 'dossiers'),
    ('Appearance carries its four readings (R-54)',
     'tools/auditors/check_appearance_contract.py',
     r'appearance readings missing:\s*(\d+)', 'readings'),
    ('Appearance does not interpret (R-54)',
     'tools/auditors/check_appearance_contract.py',
     r'interpretation tells in Appearance:\s*(\d+)', 'tells'),
    ('A Tale exists at all (R-46)',
     'tools/auditors/check_tale_register.py',
     r'NO TALE AT ALL\s+(\d+)', 'dossiers'),
    ('Tale declared in a register (189)',
     'tools/auditors/check_tale_register.py',
     r'plain narrative, no register yet\s*(\d+)', 'dossiers'),
    ('No banned AI construction (R-45 s0.1)',
     'tools/auditors/check_ai_prose.py',
     r'banned-list hits\s*(\d+)', 'dossiers'),
    ('Essayist constructions (R-45 s0.2)',
     'tools/auditors/check_ai_prose.py',
     r'essayist openers\s*(\d+)', 'openers'),
    ('Form line carries content (R-45 s2)',
     'tools/auditors/check_form_line.py',
     r'thin - no colour, material or number\s*(\d+)', 'dossiers'),
    ('Form line under 130 words (R-45 s2)',
     'tools/auditors/check_form_line.py',
     r'over \d+ words \(a story\)\s*(\d+)', 'dossiers'),
    ('Form line does not repeat its marker (R-45 s2)',
     'tools/auditors/check_form_line.py',
     r'marker repeats the form line\s*(\d+)', 'dossiers'),
    ('Stat bands inside the grade ceiling (R-22)',
     'tools/check_stat_bands.py',
     r'(\d+) over ceiling', 'dossiers'),
    ('Stock slot templates (R-45 s3)',
     'tools/auditors/check_slot_templates.py',
     r'TOTAL\s+(\d+)\s+instances', 'instances'),
    ('M.A.W. set siblings agree (R-39)',
     'tools/auditors/check_set_agreement.py',
     r'sibling-disagreement\s*(\d+)', 'sets'),
    ('Entity links',
     'tools/auditors/check_entity_links.py',
     r'unlinked-but-resolvable\s*(\d+)', 'dossiers'),
    ('Broken links',
     'tools/auditors/check_entity_links.py',
     r'self-links\s*(\d+)', 'links'),
]


def run(gate):
    out = subprocess.run([sys.executable, os.path.join(ROOT, gate)],
                         cwd=ROOT, capture_output=True, text=True, timeout=900)
    return out.stdout + out.stderr


def main(argv):
    verbose = '-v' in argv or '--verbose' in argv
    rows = []
    for name, gate, pat, against in STANDARDS:
        if not os.path.exists(os.path.join(ROOT, gate)):
            rows.append((name, 'UNKNOWN', 'gate missing', against))
            continue
        try:
            text = run(gate)
        except Exception as exc:                                    # noqa: BLE001
            rows.append((name, 'UNKNOWN', type(exc).__name__, against))
            continue
        m = re.search(pat, text)
        if not m:
            rows.append((name, 'UNKNOWN', 'count line not found', against))
            continue
        rows.append((name, 'DONE' if int(m.group(1)) == 0 else 'OPEN',
                     int(m.group(1)), against))

    done = sum(1 for _, s, _, _ in rows if s == 'DONE')
    open_ = sum(1 for _, s, _, _ in rows if s == 'OPEN')

    print()
    print('HOW FINISHED IS THIS ARCHIVE')
    print('=' * 84)
    for name, status, rem, against in rows:
        tail = str(rem) if isinstance(rem, int) else rem
        print('  %-46s %-8s %6s  of %s' % (name[:46], status, tail, against))
    print('=' * 84)
    print('  %d of %d standing standards are DONE · %d are OPEN · %d unknown'
          % (done, len(rows), open_, len(rows) - done - open_))
    print()
    if open_:
        print('  A gate printing RESULT: PASS with a number above zero here is a ratchet, not a')
        print('  finish. Those standards are listed OPEN on purpose.')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
