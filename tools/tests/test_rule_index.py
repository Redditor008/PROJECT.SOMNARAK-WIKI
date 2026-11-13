# -*- coding: utf-8 -*-
"""Gate 90 — a rule is indexed the moment it is stated (O-30, R-12)."""
import unittest

from tools.auditors import check_rule_index as gate

RULES = 'REFERENCE_SOMNARAK_WIKI/RULES'


class TheComparison(unittest.TestCase):
    """The pure half: what the README says against what the folder holds."""

    def disk(self, *ids):
        return {i: '%s/%s_x.md' % (RULES, i) for i in ids}

    def test_a_matching_pair_passes(self):
        disk = self.disk('R-01', 'R-02')
        rows = [('R-01', 'R-01_x.md'), ('R-02', 'R-02_x.md')]
        self.assertEqual(gate.compare(disk, rows, exists=lambda p: True), [])

    def test_a_rule_on_disk_but_not_indexed_fails(self):
        disk = self.disk('R-01', 'R-02')
        rows = [('R-01', 'R-01_x.md')]
        bad = gate.compare(disk, rows, exists=lambda p: True)
        self.assertTrue(any(b[0] == 'R-02' and 'not in RULES/README' in b[1] for b in bad), bad)

    def test_a_row_pointing_at_nothing_fails(self):
        disk = self.disk('R-01')
        rows = [('R-01', 'R-01_x.md'), ('R-99', 'R-99_missing.md')]
        bad = gate.compare(disk, rows, exists=lambda p: p.endswith('R-01_x.md'))
        self.assertTrue(any(b[0] == 'R-99' and 'not there' in b[1] for b in bad), bad)

    def test_a_row_pointing_at_another_rule_fails(self):
        disk = self.disk('R-01', 'R-02')
        rows = [('R-01', 'R-01_x.md'), ('R-02', 'R-01_x.md')]
        bad = gate.compare(disk, rows, exists=lambda p: True)
        self.assertTrue(any('another rule' in b[1] for b in bad), bad)

    def test_a_rule_indexed_twice_fails(self):
        disk = self.disk('R-01')
        rows = [('R-01', 'R-01_x.md'), ('R-01', 'R-01_x.md')]
        bad = gate.compare(disk, rows, exists=lambda p: True)
        self.assertTrue(any('more than once' in b[1] for b in bad), bad)


class TheShippedIndex(unittest.TestCase):

    def test_every_rule_on_disk_is_indexed(self):
        disk, rows, bad = gate.measure()
        self.assertGreaterEqual(len(disk), 50)
        self.assertEqual(len(rows), len(disk), 'the table is not the folder')
        self.assertEqual(bad, [], '%d index problems' % len(bad))

    def test_the_five_new_rules_are_in_it(self):
        _disk, rows, _bad = gate.measure()
        listed = {r[0] for r in rows}
        for rid in ('R-46', 'R-47', 'R-48', 'R-49', 'R-50'):
            self.assertIn(rid, listed)


if __name__ == '__main__':
    unittest.main()
