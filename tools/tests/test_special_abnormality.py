# -*- coding: utf-8 -*-
"""Gate 84 — a declared terminus is never worked and never extracted (R-35)."""
import unittest

from tools.auditors import check_special_abnormality as gate

SPECIAL = ('| **Entity Type** | **Subject** \u2014 Non-breaching |\n'
           '| **Special Class** | **Special Abnormality** \u2014 terminus of a line |\n'
           '| **Han-Energy yield** | \u2014 \u00b7 nothing is collected |\n')


class DeclaredTerminus(unittest.TestCase):

    def test_clean_terminus_passes(self):
        self.assertEqual(gate.problems(SPECIAL), [])

    def test_work_table_is_refused(self):
        text = SPECIAL + ('| **Flerehan** (Tears) | x | Stable |\n'
                          '| **Pugnahan** (Confrontation) | y | Increase |\n')
        bad = gate.problems(text)
        self.assertTrue(any('Work Type row' in b for b in bad), bad)

    def test_maw_production_line_is_refused(self):
        text = SPECIAL + '### M.A.W. Weapon \u2014 The X\n\n### M.A.W. Suit \u2014 The Y\n'
        bad = gate.problems(text)
        self.assertTrue(any('M.A.W. production line' in b for b in bad), bad)

    def test_modelled_yield_is_refused(self):
        text = SPECIAL.replace('\u2014 \u00b7 nothing is collected',
                               '28\u201340 per cycle on paper')
        bad = gate.problems(text)
        self.assertTrue(any('collected Han-Energy yield' in b for b in bad), bad)

    def test_ordinary_entity_is_not_measured(self):
        text = ('| **Entity Type** | **Subject** |\n'
                '| **Flerehan** (Tears) | x | Stable |\n'
                '### M.A.W. Weapon \u2014 The Z\n')
        self.assertEqual(gate.problems(text), [])


if __name__ == '__main__':
    unittest.main()
