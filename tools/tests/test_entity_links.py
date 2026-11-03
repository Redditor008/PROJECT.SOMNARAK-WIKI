#!/usr/bin/env python3
"""
tools/tests/test_entity_links.py

The link rule has to catch an unlinked name and must not force a link where the
name is ambiguous or unfiled. Both halves are tested; fixtures live in a temp
directory and never in the archive.
"""

import io
import os
import shutil
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


class CrossReferenceTest(unittest.TestCase):
    """The Cross-References surface (batch 148)."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(lambda: [os.remove(os.path.join(self.tmp, f))
                                 for f in os.listdir(self.tmp)])
        self.index = {
            'the debt scale': 'SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIIβ-015_The_Debt_Scale.md',
            'redacted': 'SOMNARAK-WORLD/Sorrow_Entities/SE-N-IIIγ-184_Redacted.md',
        }

    def write(self, line):
        path = os.path.join(self.tmp, 'z.md')
        io.open(path, 'w', encoding='utf-8').write(line + '\n')
        return path

    def test_unlinked_multiwd_name_is_reported(self):
        path = self.write('**Cross-References:** Zone B · The Debt Scale · the register')
        self.assertEqual(len(links.scan_cross_refs(path, self.index)), 1)

    def test_linked_name_is_not_reported(self):
        path = self.write('**Cross-References:** Zone B · [The Debt Scale](x.md) · the register')
        self.assertEqual(links.scan_cross_refs(path, self.index), [])

    def test_single_word_title_is_refused(self):
        # "the redacted reading" must not become a link to the entity *Redacted*.
        path = self.write('**Cross-References:** the redacted reading · the file')
        self.assertEqual(links.scan_cross_refs(path, self.index), [])

    def test_linker_writes_and_then_scans_clean(self):
        path = self.write('**Cross-References:** Zone B · The Debt Scale · the register')
        added = links.link_cross_refs(path, self.index)
        self.assertEqual(added, 1)
        self.assertEqual(links.scan_cross_refs(path, self.index), [])
        body = io.open(path, encoding='utf-8').read()
        # The fixture lives outside the repo, so only the target's tail is stable.
        self.assertIn('[The Debt Scale](', body)
        self.assertIn('SE-C-IIIβ-015_The_Debt_Scale.md)', body)


class SelfLinkTest(unittest.TestCase):
    """Found by reading, not by counting: SE-C-Iα-071 linked to itself.

    The line named a different record — *The Kind Healer's Shadow* — but the
    linker matched the Healer's own title inside the possessive and produced
    `[The Kind Healer](…its own file…)’s Shadow`. The name was linked, so the
    unlinked counter saw nothing; the target was the defect.
    """

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.index = {'debt scale': 'SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIIβ-015_The_Debt_Scale.md'}

    def write(self, body, name='SE-C-IIIβ-015_The_Debt_Scale.md'):
        path = os.path.join(self.tmp, name)
        io.open(path, 'w', encoding='utf-8').write(body)
        return path

    def test_link_to_itself_is_reported(self):
        path = self.write('**Cross-References:** Zone B · '
                          '[The Debt Scale](SE-C-IIIβ-015_The_Debt_Scale.md) · the register')
        found = links.scan_self_links(path)
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0][0], 'The Debt Scale')

    def test_link_to_another_record_is_not_reported(self):
        os.makedirs(os.path.join(self.tmp, 'sub'), exist_ok=True)
        io.open(os.path.join(self.tmp, 'sub', 'other.md'), 'w', encoding='utf-8').write('# other')
        path = self.write('**Cross-References:** Zone B · [Other](sub/other.md) · the register')
        self.assertEqual(links.scan_self_links(path), [])

    def test_linker_refuses_to_write_a_self_link(self):
        # The name resolves to this file, so the writer must leave it plain
        # rather than send the reader back to the page they are on.
        body = ('**Cross-References:** Zone B · The Debt Scale · the register\n')
        path = self.write(body)
        added = links.link_cross_refs(path, {
            'debt scale': os.path.join(self.tmp, 'SE-C-IIIβ-015_The_Debt_Scale.md')})
        self.assertEqual(added, 0)
        self.assertEqual(io.open(path, encoding='utf-8').read(), body)

    def test_shipped_dossiers_have_no_self_links(self):
        import glob
        bad = []
        for path in glob.glob(os.path.join(ROOT, 'SOMNARAK-WORLD', 'Sorrow_Entities', '*.md')):
            if links.scan_self_links(path):
                bad.append(os.path.basename(path))
        self.assertEqual(bad, [])


if __name__ == '__main__':
    unittest.main()
