#!/usr/bin/env python3
"""
tools/tests/test_entity_links.py

The link rule has to catch an unlinked name and must not force a link where the
name is ambiguous or unfiled. Both halves are tested; fixtures live in a temp
directory and never in the archive.
"""

import io
import os
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'auditors'))

import check_entity_links as links  # noqa: E402


class IndexTest(unittest.TestCase):
    def test_real_index_resolves_a_known_record(self):
        idx = links.build_index()
        self.assertIn('debt eater', idx)
        self.assertIn('SE-C-IIIβ-014', idx['debt eater'])

    def test_alias_resolves(self):
        idx = links.build_index()
        self.assertIn('remembrance', idx)

    def test_index_holds_only_unique_names(self):
        idx = links.build_index()
        for name, path in idx.items():
            self.assertIsInstance(path, str)
            self.assertTrue(path.endswith('.md'), name)


class ScanTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(lambda: [os.remove(os.path.join(self.tmp, f))
                                 for f in os.listdir(self.tmp)])
        self.index = {'debt eater': 'SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIIβ-014_Debt_Eater.md'}

    def write(self, cell):
        path = os.path.join(self.tmp, 'x.md')
        io.open(path, 'w', encoding='utf-8').write(
            '## Entity Interaction Record\n\n'
            '| Related entity | Canonical interaction |\n'
            '|---|---|\n'
            f'| {cell} | Something observed. |\n')
        return path

    def test_unlinked_resolvable_name_is_reported(self):
        found = links.scan(self.write('**The Debt Eater**'), self.index)
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0][1], 'The Debt Eater')

    def test_already_linked_name_is_clean(self):
        found = links.scan(self.write('[**The Debt Eater**](SE-C-IIIβ-014_Debt_Eater.md)'),
                           self.index)
        self.assertEqual(found, [])

    def test_unfiled_name_stays_plain(self):
        found = links.scan(self.write('**The Sorrow River**'), self.index)
        self.assertEqual(found, [])

    def test_outside_an_interaction_table_is_not_scored(self):
        path = os.path.join(self.tmp, 'y.md')
        io.open(path, 'w', encoding='utf-8').write('| The Debt Eater | prose |\n')
        self.assertEqual(links.scan(path, self.index), [])


if __name__ == '__main__':
    unittest.main()
