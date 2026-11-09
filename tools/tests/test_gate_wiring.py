# -*- coding: utf-8 -*-
"""Gate 92 — a gate cited is a gate wired (O-37)."""
import io
import os
import unittest

from tools.auditors import check_gate_wiring as gate

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def build_text():
    with io.open(gate.GATE_SH, encoding='utf-8') as fh:
        return fh.read()


BUILD = """
check "RESULT: PASS"  python3 tools/auditors/check_rule_index.py
check "RESULT: PASS"  python3 tools/auditors/check_secc_shape.py
"""


class TheComparison(unittest.TestCase):
    """The pure half: what `how_finished` measures against what the build runs."""

    def test_a_cited_gate_that_is_invoked_passes(self):
        cited = ['tools/auditors/check_rule_index.py']
        self.assertEqual(gate.compare(cited, BUILD), [])

    def test_a_cited_gate_that_is_never_invoked_fails(self):
        """Batch 206's rule-index gate: written, tested, cited, never wired."""
        cited = ['tools/auditors/check_rule_index.py', 'tools/auditors/check_se_effect.py']
        self.assertEqual(gate.compare(cited, BUILD), ['tools/auditors/check_se_effect.py'])

    def test_an_empty_build_wires_nothing(self):
        cited = ['tools/auditors/check_rule_index.py']
        self.assertEqual(gate.compare(cited, ''), cited)

    def test_the_comparison_names_every_missing_gate(self):
        cited = ['a/one.py', 'a/two.py', 'a/three.py']
        self.assertEqual(len(gate.compare(cited, 'python3 a/two.py\n')), 2)


class TheArchive(unittest.TestCase):
    """Against the real `how_finished.py` and the real `tools/gate.sh`."""

    def test_every_standard_names_a_gate(self):
        """23 standards share 17 distinct auditors; an empty list would pass silently."""
        self.assertGreaterEqual(len(gate.cited()), 15)

    def test_every_cited_gate_is_invoked_by_the_build(self):
        missing = gate.compare(gate.cited(), build_text())
        self.assertEqual(missing, [], missing)

    def test_every_cited_gate_exists_on_disk(self):
        absent = [p for p in gate.cited() if not os.path.exists(os.path.join(ROOT, p))]
        self.assertEqual(absent, [], absent)

    def test_this_gate_is_itself_wired(self):
        """It measures everything else; it must also measure itself."""
        self.assertIn('tools/auditors/check_gate_wiring.py', build_text())


if __name__ == '__main__':
    unittest.main()
