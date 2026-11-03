#!/usr/bin/env python3
"""
tools/tests/test_sentence_starts.py

Both families were found by reading a file after a repair had been applied to
it, which is the case a number-checker cannot cover: every figure in a broken
sentence can be correct. These tests pin the two shapes, and they pin the two
things the guard must *not* fire on — an abbreviation and a value that begins
with a capital letter for its own reasons.
"""

import io
import os
import sys
import tempfile
import shutil
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'auditors'))

import check_sentence_starts as starts  # noqa: E402


class LowercaseStartTest(unittest.TestCase):
    def test_the_sentence_this_batch_broke(self):
        text = ('3. **Resolution:** The party comes out with the room count matching. '
                'the descent record; the count has matched in nineteen descents of '
                'every twenty.')
        self.assertEqual([f for f, _, _ in starts.scan_text(text)], ['lowercase-start'])

    def test_a_correct_sentence_does_not_fire(self):
        text = ('3. **Resolution:** The party comes out with the room count matching. '
                'The descent record holds the count.')
        self.assertEqual(starts.scan_text(text), [])

    def test_an_ellipsis_is_dialogue_not_a_fragment(self):
        text = '> **[Seiyon]** "I am... operational, Director."'
        self.assertEqual(starts.scan_text(text), [])

    def test_vs_is_an_abbreviation(self):
        # Fires on the word before the stop, not after it.
        text = "- The wings' colour (gold vs. violet) marks the chain's direction."
        self.assertEqual(starts.scan_text(text), [])

    def test_a_lowercase_word_after_a_number_does_not_fire(self):
        text = 'Damage falls to 4. the residue is recorded separately.'
        self.assertEqual([f for f, _, _ in starts.scan_text(text)], ['lowercase-start'])


class LabelEchoTest(unittest.TestCase):
    def test_field_answered_by_another_fields_label(self):
        text = ('| **Position / movement** | Physical Form: A market stall that '
                'appears overnight. |')
        self.assertEqual([f for f, _, _ in starts.scan_text(text)], ['label-echo'])

    def test_bullet_form_is_caught_too(self):
        text = '- **Position / movement:** Primary Form: A pressure-shaped humanoid.'
        self.assertEqual([f for f, _, _ in starts.scan_text(text)], ['label-echo'])

    def test_a_field_opening_on_its_own_label_is_fine(self):
        text = '| **Physical Form** | Non-Organic — A dressed-stone complex. |'
        self.assertEqual(starts.scan_text(text), [])

    def test_a_value_that_merely_mentions_a_label_is_fine(self):
        # The Dormant Monolith false positive: "Sorrow Gauge ≥ 90 per cent" is a
        # reading, and Sorrow Gauge is deliberately not in the label list.
        text = ('| **Activation threshold** | Sorrow Gauge ≥ 90 per cent, read '
                'against declined reliefs. |')
        self.assertEqual(starts.scan_text(text), [])


class ShippedTreeTest(unittest.TestCase):
    def test_corpus_is_clean(self):
        files, hits = starts.measure()
        self.assertGreater(len(files), 290, 'the glob stopped matching dossiers')
        self.assertEqual(hits, [], f'{len(hits)} fragment(s) in the corpus')

    def test_ceilings_are_at_the_floor(self):
        self.assertEqual(set(starts.RATCHET), {'lowercase-start', 'label-echo'})
        for family, ceiling in starts.RATCHET.items():
            self.assertEqual(ceiling, 0, family)


if __name__ == '__main__':
    unittest.main()
