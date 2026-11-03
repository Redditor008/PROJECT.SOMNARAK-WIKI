#!/usr/bin/env python3
"""
tools/tests/test_citations.py

The citation lens is the only one with no judgement in it: a record either exists
or it does not. These tests hold that property, and hold the one piece of
reasoning the tool does perform — deciding whether a filename or a header is the
stale side when the two disagree.
"""

import importlib.util
import os
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TOOL = os.path.join(ROOT, 'tools', 'auditors', 'check_citations.py')

spec = importlib.util.spec_from_file_location('cc', TOOL)
cc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cc)


class TestParsing(unittest.TestCase):
    def test_designation_code_shape(self):
        """The archive joins rank and element: C-IIIβ-015, not C-III-β-015."""
        m = cc.CODE.match('C-IIIβ-015')
        self.assertIsNotNone(m)
        self.assertEqual(m.group(2), 'III')
        self.assertEqual(m.group(3), 'β')

    def test_filename_code_with_subletter(self):
        m = cc.FILE_CODE.match('SE-C-Iα-071b_Blessing_Giver_축복_주는_자.md')
        self.assertEqual(m.group(1), 'C-Iα-071b')

    def test_designation_field(self):
        t = '| **Designation** | `C-Iβ-071b [LS]` |'
        self.assertEqual(cc.DESIGNATION.search(t).group(1).split()[0].strip('`'), 'C-Iβ-071b')


class TestField(unittest.TestCase):
    def test_reads_coherence(self):
        self.assertEqual(cc.field('| **Coherence** | Fragment (III) — precise |', 'Coherence'),
                         'Fragment (III) — precise')


class TestArchive(unittest.TestCase):
    def test_no_dead_citations(self):
        """Every one of the archive's cross-references names a record that exists."""
        self.assertEqual(cc.RATCHET['dead-citation'], 0)

    def test_no_duplicate_designations(self):
        self.assertEqual(cc.RATCHET['duplicate-designation'], 0)

    def test_no_stale_filenames(self):
        """Cleared in batch 138: every filename now carries its own dossier's code.

        The two Kind Healer variants were `SE-C-Iα-071b`/`071c` while filing
        `C-Iβ-071b`/`C-IIγ-071c` in their headers. At zero, a new mismatch fails.
        """
        self.assertEqual(cc.RATCHET['stale-filename'], 0)

    def test_gate_passes(self):
        import subprocess, sys
        r = subprocess.run([sys.executable, TOOL], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout[-600:])
        self.assertIn('RESULT: PASS', r.stdout)


if __name__ == '__main__':
    unittest.main()
