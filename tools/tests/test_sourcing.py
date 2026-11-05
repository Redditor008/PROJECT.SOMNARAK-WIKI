#!/usr/bin/env python3
"""
tools/tests/test_sourcing.py

Tests for tools/auditors/check_sourcing.py — the journalist's read.

The distinction these tests protect is the whole point of the tool: a word that
looks like a fault is not necessarily one. "Unreconciled" is how this archive
refuses to average two measurements; "no definition reconciles these" is how it
ships a contradiction. The first must never fail. The second always must.
"""

import importlib.util
import os
import shutil
import tempfile
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TOOL = os.path.join(ROOT, 'tools', 'auditors', 'check_sourcing.py')

spec = importlib.util.spec_from_file_location('cs', TOOL)
cs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cs)


class TestRateConflict(unittest.TestCase):
    def test_card_rate_against_prose_rate(self):
        text = ('**Acquisition Probability:** 5%\n'
                '**Ability:** Granted at near-100% probability in training.\n')
        defects, _, _ = cs.scan(self._one(text))
        self.assertIn('rate-conflict', defects)

    def test_one_rate_alone_is_fine(self):
        text = '**Acquisition Probability:** 5%\n**Ability:** Granted at 5% on a work.\n'
        defects, _, _ = cs.scan(self._one(text))
        self.assertNotIn('rate-conflict', defects)

    def _one(self, text):
        """scan() takes paths, so write the fixture to a temp dir — never into
        the archive, where a leftover scratch dossier would enter the census."""
        d = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, d, True)
        p = os.path.join(d, 'SE-TEST-Scratch.md')
        with open(p, 'w', encoding='utf-8') as f:
            f.write(text)
        return [p]


class TestUnresolvedNotes(unittest.TestCase):
    def test_declaring_a_conflict_and_shipping_it_fails(self):
        text = ('**Full-set review:** the two sources say 5% and near-100%, with no '
                'definition reconciling them. Keep those claims distinct; no value was normalized.\n')
        defects, reports, _ = cs.scan(self._one(text))
        self.assertIn('unresolved-note', defects)

    def test_filing_two_measurements_apart_is_not_a_fault(self):
        """The archive refusing to average two readings is good practice."""
        text = 'The engineer measured 41 and the Warden 47; both series are filed unreconciled.\n'
        defects, reports, _ = cs.scan(self._one(text))
        self.assertNotIn('unresolved-note', defects)
        self.assertTrue(any('unreconciled' in k for k in reports))

    def _one(self, text):
        """scan() takes paths, so write the fixture to a temp dir — never into
        the archive, where a leftover scratch dossier would enter the census."""
        d = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, d, True)
        p = os.path.join(d, 'SE-TEST-Scratch.md')
        with open(p, 'w', encoding='utf-8') as f:
            f.write(text)
        return [p]


class TestArchive(unittest.TestCase):
    def test_gate_passes(self):
        r = subprocess.run([sys.executable, TOOL], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout[-800:])
        self.assertIn('RESULT: PASS', r.stdout)

    def test_shipped_contradiction_ceilings_are_zero(self):
        for k in ('rate-conflict', 'unresolved-note', 'false-uniqueness'):
            self.assertEqual(cs.RATCHET.get(k), 0, f'{k} must not carry stale debt')

    def test_testimony_is_attributed(self):
        """Every quotation in the archive names who said it."""
        r = subprocess.run([sys.executable, TOOL], capture_output=True, text=True)
        self.assertIn('0 quoted lines without an attribution', r.stdout)


if __name__ == '__main__':
    unittest.main()
