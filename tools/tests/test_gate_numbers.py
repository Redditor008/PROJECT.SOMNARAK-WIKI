# -*- coding: utf-8 -*-
"""Gate 49 — a number names one gate (R-53, O-39)."""
import io
import os
import unittest

from tools.auditors import check_gate_numbers as gate

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

BUILD = [
    ('tools/check_box_symmetry.py', 'RESULT: PASSED'),
    ('tools/auditors/check_relic_gauge.py', 'RESULT: PASS'),
    ('tools/auditors/check_gate_wiring.py', 'RESULT: PASS'),
]
TABLE = {1: 'tools/check_box_symmetry.py',
         2: 'tools/auditors/check_relic_gauge.py',
         3: 'tools/auditors/check_gate_wiring.py'}


class TheRegister(unittest.TestCase):
    """The register is derived from the build, so drift is a defect, not an opinion."""

    def test_a_matching_register_passes(self):
        self.assertEqual(gate.compare(BUILD, TABLE), [])

    def test_a_missing_row_fails(self):
        issues = gate.compare(BUILD, {1: 'tools/check_box_symmetry.py'})
        self.assertTrue(any('no GATES.md row' in d for _, d in issues), issues)

    def test_a_wrong_row_fails(self):
        """The real collision: gate 92 naming two scripts."""
        bad = dict(TABLE)
        bad[3] = 'tools/auditors/check_relic_interaction_damage.py'
        issues = gate.compare(BUILD, bad)
        self.assertTrue(any('in GATES.md' in d for _, d in issues), issues)

    def test_a_short_build_fails(self):
        issues = gate.compare(BUILD[:2], TABLE)
        self.assertTrue(any(k == 'count' for k, _ in issues), issues)

    def test_a_row_past_the_end_of_the_build_fails(self):
        bad = dict(TABLE)
        bad[9] = 'tools/auditors/check_secc_shape.py'
        issues = gate.compare(BUILD, bad)
        self.assertTrue(any('only' in d for _, d in issues), issues)


class TheCitations(unittest.TestCase):
    """A citation pairs a script with a number; the number must be that script's."""

    def test_a_correct_citation_passes(self):
        texts = [('doc.md', '`check_gate_wiring.py` (gate 3) does the work')]
        self.assertEqual(gate.bad_citations(texts, TABLE), [])

    def test_a_citation_of_the_wrong_number_fails(self):
        """The real defect: check_gate_wiring cited as gate 92, which is the relic gate."""
        texts = [('doc.md', '`check_gate_wiring.py` (gate 2) does the work')]
        issues = gate.bad_citations(texts, TABLE)
        self.assertEqual(len(issues), 1)
        self.assertIn('gate 2 is check_relic_gauge.py', issues[0][1])

    def test_a_citation_of_a_number_that_does_not_exist_fails(self):
        texts = [('doc.md', '`check_gate_wiring.py` (gate 92) does the work')]
        issues = gate.bad_citations(texts, TABLE)
        self.assertTrue(any('register does not have' in d for _, d in issues), issues)

    def test_a_bare_number_with_no_script_fails(self):
        texts = [('doc.md', 'this was closed (gate 92) in an earlier batch')]
        issues = gate.bad_citations(texts, TABLE)
        self.assertTrue(issues, issues)

    def test_citations_are_read_as_pairs(self):
        found = gate.citations('`check_relic_gauge.py` (gate 2) and `check_gate_wiring.py` (gate 3)')
        self.assertEqual([n for _, n in found], [2, 3])


class TheArchive(unittest.TestCase):
    """Against the real build and the real documents."""

    def test_the_register_matches_the_build(self):
        self.assertEqual(gate.compare(gate.build_gates(), gate.registered()), [])

    def test_no_document_cites_a_number_that_disagrees(self):
        issues = gate.bad_citations(gate.docs(), gate.registered())
        self.assertEqual(issues, [], issues[:5])

    def test_the_register_numbers_every_gate(self):
        build = gate.build_gates()
        self.assertGreaterEqual(len(build), 45)
        self.assertEqual(sorted(gate.registered()), list(range(1, len(build) + 1)))

    def test_this_gate_is_itself_numbered_and_wired(self):
        table = gate.registered()
        number = [n for n, s in table.items()
                  if s == 'tools/auditors/check_gate_numbers.py']
        self.assertEqual(len(number), 1, 'this gate must appear exactly once in GATES.md')
        text = io.open(gate.GATE_SH, encoding='utf-8').read()
        self.assertIn('tools/auditors/check_gate_numbers.py', text)


if __name__ == '__main__':
    unittest.main()
