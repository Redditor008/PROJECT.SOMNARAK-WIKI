#!/usr/bin/env python3
"""
tools/tests/test_ratio_basis.py

The defect this guard was written for was **created by a repair**, in batch 150,
and it survived because it looked like rounding: `147 of 188` became
`78 per cent of the readings` when the pooled denominator was removed. Both
halves of the ratio were fabricated; the percentage carried them through.

The tests therefore pin the four spellings the repair actually used — digits,
words, percentage, and the reversed fraction — and the three things the guard
must leave alone: a mechanic threshold, a percentage that *is* derived from a
pair on the page, and a proportion that names its counts.
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

import check_ratio_basis as basis  # noqa: E402


def fires(text):
    return [what for what, _ in basis.scan_text(text)]


class FiresOnTheRepair(unittest.TestCase):
    def test_percentage_of_readings(self):
        self.assertEqual(
            fires('The pulse has matched in 78 per cent of the readings and the '
                  '41 misses are the file.'),
            ['78 per cent of the readings'])

    def test_percentage_of_cycles(self):
        self.assertEqual(
            fires('in 45 per cent of cycles the sheet has named somebody'),
            ['45 per cent of cycles'])

    def test_fraction_with_the_series_in_the_middle(self):
        self.assertEqual(
            fires('it has matched in nineteen descents of every twenty, and the '
                  'nine that did not are the nine pulls.'),
            ['nineteen descents of every twenty'])

    def test_fraction_with_the_series_implied(self):
        # No series noun in the phrase at all — the sentence around it supplies
        # the context, and a reader still cannot check the division.
        self.assertEqual(
            fires('the question has worked in nineteen of every twenty'),
            ['nineteen of every twenty'])


class LeavesAlone(unittest.TestCase):
    def test_a_mechanic_threshold_is_not_a_proportion(self):
        self.assertEqual(fires('Resistance 30 per cent against Void pressure.'), [])
        self.assertEqual(fires('Above 65 per cent, once in the record.'), [])

    def test_a_percentage_derived_from_a_stated_pair_is_fine(self):
        text = ('Eighteen of the forty-one fall in Tide weeks, which is forty-four '
                'per cent of the motions on the file.')
        self.assertEqual(fires(text), [])

    def test_a_fraction_that_states_both_counts_is_fine(self):
        # The pair is on the page; a reader can do the division.
        self.assertEqual(fires('147 of 188 readings matched, and the 41 misses are '
                               'the file.'), [])

    def test_prose_words_that_are_not_fractions(self):
        self.assertEqual(fires('Nine of the twenty rooms have been surveyed.'), [])


class ShippedTree(unittest.TestCase):
    def test_corpus_is_clean(self):
        files, hits = basis.measure()
        self.assertGreater(len(files), 290, 'the glob stopped matching dossiers')
        self.assertEqual(hits, [], f'{len(hits)} unsupported proportion(s)')

    def test_ceiling_is_at_zero(self):
        self.assertEqual(basis.RATCHET, 0)


if __name__ == '__main__':
    unittest.main()
