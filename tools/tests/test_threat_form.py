# -*- coding: utf-8 -*-
"""Gate 85 — a Top-or-above entity carries its band in the file, not in the code (R-42)."""
import unittest

from tools.auditors import check_threat_form as gate

TOP = ('| **Coherence** | Entity (IV) |\n'
       '| **Potency** | Critical (\u03b4) |\n'
       '| **Han Pressure [ATK]** | %s per hit \u00b7 Weight |\n')
HIGH = ('| **Coherence** | Sovereign (V) |\n'
        '| **Potency** | Critical (\u03b4) |\n'
        '| **Han Pressure [ATK]** | %s per hit \u00b7 Weight |\n')
SPECIAL_ROW = '| **Special Class** | **Special Abnormality** \u2014 terminus |\n'


class TopAndHigh(unittest.TestCase):

    def test_top_opens_inside_the_band(self):
        self.assertEqual(gate.problems(TOP % '30\u201355'), [])

    def test_top_opening_below_the_floor_fails(self):
        bad = gate.problems(TOP % '14\u201332')
        self.assertTrue(any('under the band floor of 30' in b for b in bad), bad)

    def test_high_opening_below_the_floor_fails(self):
        bad = gate.problems(HIGH % '25\u201353')
        self.assertTrue(any('under the band floor of 50' in b for b in bad), bad)

    def test_high_at_the_floor_passes(self):
        self.assertEqual(gate.problems(HIGH % '50\u201380'), [])

    def test_below_top_straddle_is_not_measured(self):
        text = ('| **Coherence** | Fragment (III) |\n'
                '| **Potency** | Major (\u03b3) |\n'
                '| **Han Pressure [ATK]** | 9\u201320 per hit |\n')
        self.assertEqual(gate.problems(text), [])


class ContactRecord(unittest.TestCase):

    def test_top_contact_record_with_reason_line_passes(self):
        text = TOP % '\u2014 nothing strikes' + ('## Contact Record\n\n'
                                                 '> **Why this file has no combat actions.** It is a wall.\n')
        self.assertEqual(gate.problems(text), [])

    def test_top_contact_record_without_reason_line_fails(self):
        text = TOP % '\u2014 nothing strikes' + '## Contact Record\n\nIt is a wall.\n'
        bad = gate.problems(text)
        self.assertTrue(any('no R-36 reason line' in b for b in bad), bad)

    def test_top_with_no_section_at_all_fails(self):
        bad = gate.problems(TOP % '\u2014')
        self.assertTrue(any('neither a Combat Record' in b for b in bad), bad)


class SpecialClass(unittest.TestCase):

    def test_special_banded_at_high_passes(self):
        self.assertEqual(gate.problems(SPECIAL_ROW + HIGH % '50\u201380'), [])

    def test_special_banded_at_top_fails(self):
        bad = gate.problems(SPECIAL_ROW + TOP % '30\u201355')
        self.assertTrue(any('not High' in b for b in bad), bad)

    def test_special_below_high_floor_fails(self):
        bad = gate.problems(SPECIAL_ROW + HIGH % '25\u201353')
        self.assertTrue(any('under the band floor of 50' in b for b in bad), bad)


if __name__ == '__main__':
    unittest.main()
