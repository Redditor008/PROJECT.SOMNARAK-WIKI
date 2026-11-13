#!/usr/bin/env python3
"""
tools/tests/test_appearance_dupe.py

Proves the appearance-duplication check can fail, and that it leaves legitimate
repetition alone. Fixtures are written to a temp directory, never to the archive.
"""

import io
import os
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'auditors'))

import check_appearance_dupe as dupe  # noqa: E402

SHIPPED = """# Item

## Appearance

The plate is a harness of iron covering the spine and knees. Nothing on the harness advertises that absorption: the knee marks stay plain and the links keep the same narrow flex whether the plate has taken pressure or not.

### Passive effect— *Moving Guard*

The plate absorbs direct Grudge pressure while a wearer follows a declared, finite movement route. It does not protect a person merely because they are busy.
"""

DUPLICATED = """# Item

## Appearance

The plate is a harness of iron covering the spine and knees. The plate absorbs direct Grudge pressure while a wearer follows a declared finite movement route.

### Passive effect— *Moving Guard*

The plate absorbs direct Grudge pressure while a wearer follows a declared, finite movement route. It does not protect a person merely because they are busy.
"""


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(lambda: [os.remove(os.path.join(self.tmp, f))
                                 for f in os.listdir(self.tmp)])

    def write(self, body):
        path = os.path.join(self.tmp, 'SE-000-C__MAW-S_Test.md')
        io.open(path, 'w', encoding='utf-8').write(body)
        return path


class TestDetects(Base):
    def test_pasted_ability_is_caught(self):
        found = dupe.scan(self.write(DUPLICATED))
        self.assertEqual(len(found), 1)
        self.assertIn('absorbs direct Grudge pressure', found[0][1])

    def test_internal_punctuation_difference_still_caught(self):
        # "declared finite" vs "declared, finite" — the comma must not hide it.
        self.assertEqual(len(dupe.scan(self.write(DUPLICATED))), 1)
        body = DUPLICATED.replace('declared finite', 'declared, finite')
        self.assertEqual(len(dupe.scan(self.write(body))), 1)

    def test_repeat_between_two_effect_fields_is_not_this_class(self):
        # A recap between two effect fields is a different question; this checker
        # only scores Appearance against an effect field.
        body = DUPLICATED.replace('## Appearance', '### Ability A')
        self.assertEqual(dupe.scan(self.write(body)), [])


class TestLeavesAlone(Base):
    def test_shipped_shape_passes(self):
        self.assertEqual(dupe.scan(self.write(SHIPPED)), [])

    def test_short_phrase_reuse_passes(self):
        body = SHIPPED.replace('It does not protect a person merely because they '
                               'are busy.', 'Grudge pressure is the medium.')
        self.assertEqual(dupe.scan(self.write(body)), [])

    def test_table_rows_are_not_scanned(self):
        body = SHIPPED + '\n| **Appearance** | absorbs Grudge pressure |\n'
        self.assertEqual(dupe.scan(self.write(body)), [])


if __name__ == '__main__':
    unittest.main()
