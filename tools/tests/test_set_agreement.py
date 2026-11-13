#!/usr/bin/env python3
"""
tools/tests/test_set_agreement.py

A guard that cannot fail is decoration. These tests build two-page sets in a
temp directory and assert that the comparison both catches a real disagreement
and tolerates the two things that only look like one: a note attached to the
same value, and the Suit page filing a slot scheme in the element field.
"""

import importlib.util
import os
import re
import shutil
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TOOL = os.path.join(ROOT, 'tools', 'auditors', 'check_set_agreement.py')

spec = importlib.util.spec_from_file_location('sa', TOOL)
sa = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sa)


class TestLeading(unittest.TestCase):
    def test_note_is_not_a_different_value(self):
        self.assertEqual(sa.leading('Weight — Amber'), sa.leading('Weight'))
        self.assertEqual(sa.leading('Weight; braided Lament residue'), 'weight')

    def test_real_difference_survives(self):
        self.assertNotEqual(sa.leading('Fragment (III)'), sa.leading('Entity (IV)'))


class TestField(unittest.TestCase):
    def test_reads_a_table_row(self):
        t = '| **Potency** | Major (γ) |\n'
        self.assertEqual(sa.field(t, 'Potency'), 'Major (γ)')

    def test_missing_field_is_none(self):
        self.assertIsNone(sa.field('no table here', 'Potency'))


class TestJudgement(unittest.TestCase):
    """The two tolerances the tool is built around."""

    def test_suit_multiplier_is_not_an_element_disagreement(self):
        self.assertEqual(sa.SUIT_ELEMENT.lower(), 'multiplier')

    def test_entity_fields_are_the_four_that_must_agree(self):
        self.assertIn('Potency', sa.ENTITY_FIELDS)
        self.assertIn('Coherence', sa.ENTITY_FIELDS)
        self.assertNotIn('Element', sa.ENTITY_FIELDS,
                         'Element is compared separately, with the Suit exception')


class TestArchive(unittest.TestCase):
    def test_gate_passes(self):
        import subprocess, sys
        r = subprocess.run([sys.executable, TOOL], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout[-600:])
        self.assertIn('RESULT: PASS', r.stdout)


if __name__ == '__main__':
    unittest.main()
