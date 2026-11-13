# -*- coding: utf-8 -*-
"""Gate 94 — a command ends in a file (R-52, O-38)."""
import io
import os
import unittest

from tools.auditors import check_command_capture as gate

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

REG = """
**Batches run 1 to 3.**

# Part IV — The batch record

| era | batches | what it was for |
|---|---|---|
| **The first** | 1–2 | two batches |
| **The rest** | 3–3 | one more |

# Part V — Where the commands stand
"""

SPAN = {'register': '**R-01** **R-02** **O-01** **O-02**', 'declared': 3}


class TheCapture(unittest.TestCase):
    """The pure half — no disk."""

    def test_everything_filed_passes(self):
        issues = gate.unfiled(['R-01', 'R-02'], ['O-01', 'O-02'], [1, 2, 3],
                              {'O-01', 'O-02'}, [(1, 2), (3, 3)], SPAN)
        self.assertEqual(issues, [])

    def test_a_rule_never_named_in_the_register_fails(self):
        """The SECC failure: a rule exists and the register does not know it."""
        issues = gate.unfiled(['R-01', 'R-99'], [], [1], set(), [(1, 3)], SPAN)
        self.assertEqual([(k, i) for k, i, _ in issues], [('rule', 'R-99')])

    def test_an_order_with_no_row_in_the_table_fails(self):
        """A command written into the orders file but not into the register."""
        issues = gate.unfiled([], ['O-01', 'O-38'], [1], {'O-01'}, [(1, 3)], SPAN)
        self.assertEqual([(k, i) for k, i, _ in issues], [('order', 'O-38')])

    def test_a_batch_outside_every_era_fails(self):
        """A batch done and logged, with no era to hold it."""
        issues = gate.unfiled([], [], [1, 2, 4], set(), [(1, 2)], {'register': '', 'declared': 5})
        self.assertEqual([(k, i) for k, i, _ in issues], [('batch', '4')])

    def test_a_span_short_of_the_highest_batch_fails(self):
        issues = gate.unfiled([], [], [1, 5], set(), [(1, 5)], {'register': '', 'declared': 3})
        self.assertIn(('span', '3'), [(k, i) for k, i, _ in issues])

    def test_an_empty_check_reports_nothing_rather_than_passing_loudly(self):
        """Every list empty is a valid pass — but the gate prints all four counts."""
        self.assertEqual(gate.unfiled([], [], [], set(), [], {'register': '', 'declared': None}), [])


class TheParsing(unittest.TestCase):
    """The era table is parsed from a real register fragment, not a guess."""

    def test_ranges_are_read_from_the_era_table(self):
        self.assertEqual(gate.era_ranges(REG), [(1, 2), (3, 3)])

    def test_a_single_batch_era_counts(self):
        self.assertIn((3, 3), gate.era_ranges(REG))

    def test_part_four_excludes_part_five(self):
        self.assertNotIn('Part V', gate.part_four(REG))

    def test_the_declared_span_is_read(self):
        self.assertIn('1 to 3', REG)


class TheArchive(unittest.TestCase):
    """Against the real registers on disk."""

    def test_every_command_ends_in_a_file(self):
        d = gate.measure()
        issues = gate.unfiled(d['rules'], d['orders'], d['batches'],
                              d['table_orders'], d['ranges'], d['span'])
        self.assertEqual(issues, [], issues[:5])

    def test_the_registers_are_big_enough_to_be_reading_something(self):
        d = gate.measure()
        self.assertGreaterEqual(len(d['rules']), 50)
        self.assertGreaterEqual(len(d['orders']), 35)
        self.assertGreaterEqual(len(d['batches']), 80)

    def test_the_rule_that_this_gate_serves_is_on_disk(self):
        self.assertIn('R-52', gate.rule_ids())

    def test_the_order_that_this_gate_serves_is_a_table_row(self):
        self.assertIn('O-38', gate.measure()['table_orders'])


if __name__ == '__main__':
    unittest.main()
