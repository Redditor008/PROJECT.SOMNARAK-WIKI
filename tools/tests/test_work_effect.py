# -*- coding: utf-8 -*-
"""Gate 88 — a work can cost, cost nothing, or give (R-49)."""
import unittest

from tools.auditors import check_work_effect as gate

SUBJECT = ('| **Entity Type** | **Subject** — Non-breaching: activation only |\n'
           '| **Element** | Grudge |\n'
           '| **Han-Energy yield** | 12\u201318 per cycle |\n'
           '%s\n')

DAMAGE = '| **Work Damage** | 3\u20136 Grudge \u2014 the cost is being named |'
NEUTRAL = ('| **Work Damage** | None \u2014 the Lament it draws is spent in the chamber and not '
           'carried out |')
GIFT = ('| **Work Damage** | None \u2014 the flame steadies and the heat stays in the room |\n'
        '| **Work Gift** | +5\u201310 Composure for the rest of the cycle \u2014 it is paid in the '
        'memory it was drawn from |')


def page(row, ops=True):
    body = SUBJECT % row
    if ops:
        body = '## Operational Parameters\n\n' + body + '\n'
    return body


class TheThreeVerdicts(unittest.TestCase):

    def test_a_damage_band_passes(self):
        self.assertEqual(gate.problems(page(DAMAGE)), [])

    def test_a_neutral_with_a_clause_passes(self):
        self.assertEqual(gate.problems(page(NEUTRAL)), [])

    def test_a_gift_with_all_four_parts_passes(self):
        self.assertEqual(gate.problems(page(GIFT)), [])

    def test_a_neutral_without_a_clause_fails(self):
        bad = gate.problems(page('| **Work Damage** | None \u2014 nothing |'))
        self.assertTrue(any('no clause' in b for b in bad), bad)

    def test_no_effect_is_not_a_reading(self):
        bad = gate.problems(page('| **Work Damage** | None \u2014 no effect at all on anybody here |'))
        self.assertTrue(any('no effect' in b for b in bad), bad)

    def test_a_percentage_in_the_cell_fails(self):
        bad = gate.problems(page('| **Work Damage** | None \u2014 65% of the time the room pays it '
                                 'and the worker does not |'))
        self.assertTrue(any('percentage' in b for b in bad), bad)


class TheGiftIsALoan(unittest.TestCase):

    def test_a_gift_under_a_damage_band_fails(self):
        bad = gate.problems(page(DAMAGE + '\n' + GIFT.split('\n')[1]))
        self.assertTrue(any('one verdict' in b for b in bad), bad)

    def test_a_gift_without_a_band_fails(self):
        row = GIFT.replace('+5\u201310', '+5')
        bad = gate.problems(page(row))
        self.assertTrue(any('no band' in b for b in bad), bad)

    def test_a_gift_without_a_stat_fails(self):
        bad = gate.problems(page(GIFT.replace('Composure', 'the worker')))
        self.assertTrue(any('names no stat' in b for b in bad), bad)

    def test_a_gift_without_an_end_fails(self):
        bad = gate.problems(page(GIFT.replace('for the rest of the cycle', 'for a while')))
        self.assertTrue(any('states no end' in b for b in bad), bad)

    def test_a_gift_without_a_price_fails(self):
        row = ('| **Work Damage** | None \u2014 the flame steadies and the heat stays in the room |\n'
               '| **Work Gift** | +5\u201310 Composure for the rest of the cycle, at no stated price |')
        bad = gate.problems(page(row))
        self.assertTrue(any('states no price' in b for b in bad), bad)


class TheShippedSplit(unittest.TestCase):

    def test_the_three_counts_are_the_rule(self):
        counts, fail, _ = gate.measure()
        self.assertEqual(counts, gate.TARGET, counts)
        self.assertEqual(fail, [], '%d subjects off the rule' % len(fail))

    def test_a_terminal_holding_is_out_of_scope(self):
        text = ('## Operational Parameters\n\n| **Entity Type** | **Subject** |\n'
                '| **Han-Energy yield** | \u2014 \u00b7 nothing is collected |\n')
        self.assertEqual(gate.problems(text), [])


if __name__ == '__main__':
    unittest.main()
