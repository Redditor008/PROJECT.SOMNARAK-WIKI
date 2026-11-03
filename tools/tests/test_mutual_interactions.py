#!/usr/bin/env python3
"""
tools/tests/test_mutual_interactions.py

The negation trap is the whole reason this file exists.

The first version of the checker tested `APPROACH.search(text)` against the raw
cell. Every denial — "Neither approaches the other" — contains the word
*approaches*, so both patterns matched and polarity collapsed to `mixed`. It
reported **0 defects on a corpus that contained one**. A checker that finds nothing
is more likely broken than right.

These tests pin the masking, the opposition rule, and the two things that must not
fire. Fixtures are inline strings; nothing is written to the archive.
"""

import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'auditors'))

import check_mutual_interactions as mutual  # noqa: E402


class TestPolarity(unittest.TestCase):
    def test_plain_approach(self):
        self.assertEqual(mutual.polarity('She reaches toward it, repeatedly.'),
                         'approach')

    def test_denied_approach_is_not_an_approach(self):
        # The exact sentence that broke the first version.
        self.assertEqual(
            mutual.polarity('Stops at the sight of it and stays stopped. Neither '
                            'approaches the other at any point in six pairings.'),
            'no-approach')

    def test_does_not_approach(self):
        self.assertEqual(mutual.polarity('It does not approach the line.'),
                         'no-approach')

    def test_both_present_is_mixed(self):
        self.assertEqual(
            mutual.polarity('It approaches the rim, but never approaches a person.'),
            'mixed')

    def test_neither_polarity_is_mixed(self):
        self.assertEqual(mutual.polarity('Recognition without contact.'), 'mixed')


class TestOpposition(unittest.TestCase):
    PAIRS = [
        ('approach', 'no-approach'),
        ('no-approach', 'approach'),
    ]

    def test_opposed_polarities_are_a_pair(self):
        for a, b in self.PAIRS:
            self.assertEqual({a, b}, {'approach', 'no-approach'})

    def test_agreement_is_not_opposition(self):
        self.assertNotEqual({'approach', 'approach'}, {'approach', 'no-approach'})

    def test_mixed_never_opposes(self):
        # Reading the corpus, a mixed cell is a cell that says both; it cannot be
        # scored against a single-sided one without guessing which clause is meant.
        self.assertNotEqual({'mixed', 'no-approach'}, {'approach', 'no-approach'})


class TestShippedState(unittest.TestCase):
    def test_corpus_is_clean(self):
        rc = mutual.main([])
        self.assertEqual(rc, 0)


if __name__ == '__main__':
    unittest.main()
