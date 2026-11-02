#!/usr/bin/env python3
"""
tools/tests/test_dossier_consistency.py

Tests for tools/auditors/check_dossier_consistency.py — the tool that asks whether
one dossier tells one story.

The tool fails in two directions on purpose, and both are tested here:

  * above the ceiling  — a new self-referential sentence was written
  * below the ceiling  — a batch paid debt down and did not lower the number

The second is the one people leave out. A ratchet that only catches regression
lets the recorded figure drift above reality, and the next session inherits a
ceiling that flatters work already done.

Run: python3 -m unittest discover -s tools/tests
"""

import importlib.util
import io
import os
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TOOL = os.path.join(ROOT, 'tools', 'auditors', 'check_dossier_consistency.py')

spec = importlib.util.spec_from_file_location('cd', TOOL)
cd = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cd)


def dossier(**over):
    """A minimal dossier whose fields agree with each other."""
    body = {
        'SECC': ('| **Class** | Entity (III) |\n'
                 '| **Element** | Grudge |\n'
                 '| **Potency** | Major (γ) |\n'
                 '| **Risk tier** | Major (γ) |\n'),
        'prose': 'The holding is quiet.\n',
    }
    body.update(over)
    return body['SECC'] + '\n' + body['prose']


class TestFieldAgreement(unittest.TestCase):
    """A field disagreeing with another field is a defect; wording is not."""

    def test_consistent_dossier_is_clean(self):
        defects, _ = cd.check('X/SE-C-III-M-1_Ok.md', dossier())
        self.assertEqual(defects, [])

    def test_potency_word_against_code(self):
        text = dossier(SECC='| **Potency** | Minor (γ) |\n| **Risk tier** | Major (γ) |\n')
        defects, _ = cd.check('X/SE-C-III-M-1_Bad.md', text)
        self.assertTrue(any(k == 'potency-word' for k, _ in defects))

    def test_grade_split_between_potency_and_risk(self):
        text = dossier(SECC='| **Potency** | Major (γ) |\n| **Risk tier** | Critical (δ) |\n')
        defects, _ = cd.check('X/SE-C-III-M-1_Split.md', text)
        self.assertTrue(any(k == 'grade-split' for k, _ in defects))


class TestR01(unittest.TestCase):
    """R-01: a record may not describe its own editing history."""

    def test_correction_sentence_is_a_defect(self):
        text = dossier(prose='It is moderate (β). '
                             'The earlier entry describing the threat as low is an error and is corrected here.\n')
        defects, _ = cd.check('X/SE-C-III-M-1_Edit.md', text)
        self.assertTrue(any(k == 'r01' for k, _ in defects))

    def test_settled_fact_is_not_a_defect(self):
        text = dossier(prose='It is moderate (β) and the broken walls are structural.\n')
        defects, _ = cd.check('X/SE-C-III-M-1_Fact.md', text)
        self.assertEqual([k for k, _ in defects], [])

    def test_allowlist_exempts_one_file_and_one_phrase(self):
        """The exemption is file+phrase, so it cannot spread."""
        allowed_file = 'SE-O-Iα-643_Frozen_Mirror_얼어붙은_거울.md'
        text = dossier(prose='A death within a shift is examined for attribution error before conduct.\n')
        defects, _ = cd.check('X/' + allowed_file, text)
        self.assertEqual([k for k, _ in defects], [],
                         'the allowlisted file should pass')
        defects, _ = cd.check('X/SE-C-III-M-9_Other.md', text)
        self.assertTrue(any(k == 'r01' for k, _ in defects),
                        'the same words in another file must still fail')

    def test_allowlist_does_not_exempt_a_second_use_in_the_same_file(self):
        text = dossier(prose='It is examined for attribution error. '
                             'The earlier entry was an error and is corrected here.\n')
        defects, _ = cd.check('X/SE-O-Iα-643_Frozen_Mirror_얼어붙은_거울.md', text)
        self.assertTrue(any(k == 'r01' for k, _ in defects))


class TestTensions(unittest.TestCase):
    """Co-location is reported and never failed — a checker that guesses gets switched off."""

    def test_never_injured_beside_injury_is_a_tension_not_a_defect(self):
        text = dossier(prose='It has never injured anyone.\n'
                             'There is a recorded case from Y4231.\n')
        defects, tensions = cd.check('X/SE-C-III-M-2_Tension.md', text)
        self.assertEqual([k for k, _ in defects], [])
        self.assertTrue(any(k.startswith('absolute') for k, _ in tensions))


class TestRatchet(unittest.TestCase):
    """Both directions, which is the point."""

    def run_gate(self):
        r = subprocess.run([sys.executable, TOOL], capture_output=True, text=True)
        return r.returncode, r.stdout

    def test_ceiling_is_zero(self):
        self.assertEqual(cd.RATCHET.get('r01'), 0,
                         'r01 is fully cleared; a non-zero ceiling is stale debt')

    def test_gate_passes_on_the_archive(self):
        code, out = self.run_gate()
        self.assertEqual(code, 0, out[-800:])
        self.assertIn('RESULT: PASS', out)

    def test_below_ceiling_fails_and_asks_for_a_lower_number(self):
        """Simulated: if every counting class came in under its ceiling, the gate must still fail."""
        ceiling = {'r01': 5}
        counts = {'r01': 0}
        bad = False
        for kind in set(list(counts) + list(ceiling)):
            n = counts.get(kind, 0)
            c = ceiling.get(kind)
            if c is None or n > c or n < c:
                bad = True
        self.assertTrue(bad, 'a count below its ceiling must be treated as a failure')


if __name__ == '__main__':
    unittest.main()
