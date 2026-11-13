# -*- coding: utf-8 -*-
"""Gate 87 — a work session has a cost, and the cost is the holding's own (R-44)."""
import unittest

from tools.auditors import check_work_damage as gate

HIGH = ('| **Coherence** | Sovereign (V) |\n'
        '| **Potency** | Critical (\u03b4) |\n'
        '| **Element** | Grudge |\n'
        '| **Han-Energy yield** | 20\u201328 per cycle |\n'
        '| **Work Damage** | %s |\n')
LOW = ('| **Coherence** | Residue (I) |\n'
       '| **Potency** | Minor (\u03b1) |\n'
       '| **Element** | Lament |\n'
       '| **Han-Energy yield** | 6\u201310 per cycle |\n')
SPECIAL = ('| **Coherence** | Sovereign (V) |\n'
           '| **Potency** | Critical (\u03b4) |\n'
           '| **Element** | All four \u2014 Lament, Grudge, Void, Weight |\n'
           '| **Han-Energy yield** | \u2014 \u00b7 nothing is collected |\n')


class HighBand(unittest.TestCase):

    def test_high_cost_in_band_and_element_passes(self):
        self.assertEqual(gate.problems(HIGH % '8\u201310 Grudge \u2014 being named'), [])

    def test_high_cost_outside_the_band_fails(self):
        bad = gate.problems(HIGH % '1\u20133 Grudge \u2014 being named')
        self.assertTrue(any('outside the ALEPH band' in b for b in bad), bad)

    def test_wrong_element_fails(self):
        bad = gate.problems(HIGH % '8\u201310 Lament \u2014 being named')
        self.assertTrue(any('does not match the Element row' in b for b in bad), bad)

    def test_high_without_the_row_fails(self):
        text = HIGH.split('| **Work Damage**')[0]
        bad = gate.problems(text)
        self.assertTrue(any('no Work Damage row' in b for b in bad), bad)


class NoWorkLoop(unittest.TestCase):

    def test_terminus_carrying_a_cost_fails(self):
        bad = gate.problems(SPECIAL + '| **Work Damage** | 8\u201310 all four |\n')
        self.assertTrue(any('no work loop' in b for b in bad), bad)

    def test_terminus_without_a_cost_passes(self):
        self.assertEqual(gate.problems(SPECIAL), [])


class LowerBands(unittest.TestCase):

    def test_low_band_accepts_a_small_cost(self):
        self.assertEqual(gate.problems(LOW + '| **Work Damage** | 1\u20133 Lament \u2014 a coin |\n'), [])

    def test_low_band_refuses_a_high_cost(self):
        bad = gate.problems(LOW + '| **Work Damage** | 8\u201310 Lament \u2014 a coin |\n')
        self.assertTrue(any('outside the ZAYIN band' in b for b in bad), bad)

    def test_lower_band_missing_the_row_is_not_failed(self):
        self.assertEqual(gate.problems(LOW), [])


if __name__ == '__main__':
    unittest.main()
