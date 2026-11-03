#!/usr/bin/env python3
"""tests for check_md_tables.py and fix_md_tables.py — the three table faults.

The scanner exists because a naive `startswith('|')` pass reported 4,697 broken
tables in the archive and 4,697 of them were in-world ASCII box art inside a
fence. Each test here pins one of the ways that false positive, or a real fault,
was possible.
"""

import io
import os
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'auditors'))

import check_md_tables as tab  # noqa: E402
import fix_md_tables as fix  # noqa: E402


class Scratch(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.mkdtemp()
        self.path = os.path.join(self.dir, 't.md')

    def tearDown(self):
        shutil.rmtree(self.dir, ignore_errors=True)

    def write(self, text):
        with io.open(self.path, 'w', encoding='utf-8') as fh:
            fh.write(text)
        return self.path

    def read(self):
        with io.open(self.path, encoding='utf-8') as fh:
            return fh.read()


class TheBoxArtFalsePositive(Scratch):
    def test_fenced_box_art_is_not_a_table(self):
        self.write('```text\n+------------+\n| Header only |\n+------------+\n```\n')
        self.assertEqual(tab.scan([self.path]), [])

    def test_a_tilde_fence_is_closed_only_by_a_tilde_fence(self):
        # TEMPLATES/ nests ```text inside ~~~markdown; a scanner that toggles on
        # "any fence line" reads the inner closing ``` as a fresh opening and
        # then reports the template's own box borders as tables.
        self.write('~~~markdown\n```text\n| not | a | table |\n```\n~~~\n')
        self.assertEqual(tab.scan([self.path]), [])

    def test_a_fence_must_be_three_or_more(self):
        self.assertEqual(tab.fence_state('``two``', None), None)

    def test_text_after_the_fence_is_scanned_again(self):
        self.write('```\n| a | b |\n```\n| H1 | H2 |\n|---|---|\n| a | b |\n')
        self.assertEqual(tab.scan([self.path]), [])


class TheThreeFaults(Scratch):
    def test_single_row(self):
        self.write('| only | one |\n')
        self.assertEqual(tab.scan([self.path])[0][2], 'single-row')

    def test_no_separator(self):
        self.write('| H1 | H2 |\n| a | b |\n')
        self.assertEqual(tab.scan([self.path])[0][2], 'no-separator')

    def test_ragged(self):
        self.write('| H1 | H2 | H3 |\n|---|---|---|\n| a | b |\n')
        self.assertEqual(tab.scan([self.path])[0][2], 'ragged [2, 3]')

    def test_an_unclosed_code_span_is_a_fault(self):
        # The owner's warning: a cell that opens a span and never closes it
        # swallows every pipe after it, so the row stops being four cells.
        self.write('| H1 | H2 | H3 |\n|---|---|---|\n| a | `open | c |\n')
        kinds = [f[2] for f in tab.scan([self.path])]
        self.assertIn('odd-backticks', kinds)

    def test_a_closed_span_with_a_pipe_inside_is_fine(self):
        self.write('| H1 | H2 |\n|---|---|\n| `a \\| b` | c |\n')
        self.assertEqual(tab.scan([self.path]), [])

    def test_a_clean_table_passes(self):
        self.write('| H1 | H2 |\n|---|---|\n| a | b |\n')
        self.assertEqual(tab.scan([self.path]), [])


class TheEscapeAwareSplit(Scratch):
    def test_an_escaped_pipe_does_not_split_a_cell(self):
        self.write('| Move | [8 Grudge \\| 8 Lament] |\n|---|---|\n| a | b |\n')
        self.assertEqual(tab.scan([self.path]), [])

    def test_a_double_escaped_pipe_is_the_scanner_s_blind_spot(self):
        # In GFM `\\\\|` is a literal backslash followed by a real cell boundary:
        # the pipe is *not* escaped. The lookbehind cannot tell it from `\\|`, so
        # this scanner reads the row as one cell too few. The blind spot is
        # covered outside the scanner: `grep -rn '\\\\\\\\|' --include=*.md .` must be
        # empty, and the batch-158 repair drove it from 5 to 0.
        self.assertEqual(len(tab.PIPESPLIT.split('a \\\\| b')), 1)


class TheThreeRepairs(Scratch):
    def test_a_stray_maximum_row_becomes_its_own_two_column_table(self):
        self.write('| Name | Qty | Note | Stat | Tag |\n|---|---|---|---|---|\n'
                   '| a | 1 | b | c | d |\n| **Maximum Amount** | 9 — row |\n\ntail\n')
        self.assertEqual(fix.fix(self.path, dry=False), 1)
        out = self.read()
        self.assertIn('| Field | Record |\n|---|---|\n| **Maximum Amount** | 9 — row |\n\n', out)
        self.assertEqual(tab.scan([self.path]), [])

    def test_a_short_row_keeps_its_column_positions(self):
        self.write('| H1 | H2 | H3 |\n|---|---|---|\n| a | b |\n')
        fix.fix(self.path, dry=False)
        self.assertIn('| a | b | %s |' % fix.MISSING, self.read())
        self.assertEqual(tab.scan([self.path]), [])

    def test_a_missing_separator_is_inserted_at_the_header_width(self):
        self.write('| A | B | C |\n| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n')
        fix.fix(self.path, dry=False)
        self.assertEqual(tab.scan([self.path]), [])

    def test_the_dry_run_writes_nothing(self):
        before = '| H1 | H2 |\n| a | b |\n'
        self.write(before)
        self.assertEqual(fix.fix(self.path, dry=True), 1)
        self.assertEqual(self.read(), before)

    def test_a_fenced_block_is_never_rewritten(self):
        before = '```\n| H1 | H2 |\n| a | b |\n```\n'
        self.write(before)
        self.assertEqual(fix.fix(self.path, dry=False), 0)
        self.assertEqual(self.read(), before)


class TheCorpus(unittest.TestCase):
    def test_the_archive_has_no_broken_tables(self):
        self.assertEqual(tab.scan(tab.corpus()), [])


if __name__ == '__main__':
    unittest.main()
