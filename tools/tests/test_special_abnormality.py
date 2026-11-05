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


class NoRegistrySet(unittest.TestCase):
    """A set cannot both say 'no registry' and keep B/C/D pages on disk."""

    def test_declared_no_registry_with_pieces_is_refused(self):
        pages = {'A': '\n'.join(['## PAGE 03 \u2014 NO M.A.W. REGISTRY', '',
                                  'Nothing is filed.']),
                 'B': '## PAGE 01\n'}
        self.assertTrue(gate.declares_no_registry(pages))

    def test_single_page_set_is_fine(self):
        self.assertFalse(gate.declares_no_registry({'A': '## PAGE 03 \u2014 NO M.A.W. REGISTRY\n'}))

    def test_completion_one_of_one_counts_as_no_registry(self):
        pages = {'A': '**Codex Set Completion:** `1/1`\n', 'C': '## PAGE 02\n'}
        self.assertTrue(gate.declares_no_registry(pages))

    def test_full_set_is_not_flagged(self):
        pages = {'A': '## PAGE 01\n**Codex Set Completion:** `4/4`\n',
                 'B': '## PAGE 01\n', 'C': '## PAGE 02\n', 'D': '## PAGE 03\n'}
        self.assertFalse(gate.declares_no_registry(pages))


if __name__ == '__main__':
    unittest.main()
