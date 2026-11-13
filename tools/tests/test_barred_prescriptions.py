# -*- coding: utf-8 -*-
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'auditors'))
import check_barred_prescriptions as cbp


class ThePairIsGivenAWord(unittest.TestCase):

    def test_a_cell_that_prints_the_retired_token_fails(self):
        self.assertTrue(cbp.line_problem('| Flerehan | N/A |'))
        self.assertTrue(cbp.line_problem('| **Pugnahan** | N/A | No movement |'))
        self.assertTrue(cbp.line_problem('| Flerehan | 0% |'))
        self.assertTrue(cbp.line_problem('| Pugnahan | -100% |'))

    def test_a_sentence_that_teaches_it_fails(self):
        self.assertTrue(cbp.line_problem(
            'Flerehan and Pugnahan are strictly N/A for those classes.'))
        self.assertTrue(cbp.line_problem(
            'Flerehan & Pugnahan designated N/A on Object, Place, and Time'))

    def test_a_worded_cell_passes(self):
        self.assertFalse(cbp.line_problem(
            '| Flerehan | **Net-Neutral** — the threshold does not come down. |'))
        self.assertFalse(cbp.line_problem(
            '| Pugnahan | **Negative-Low** — the threshold goes to 0. |'))

    def test_a_sentence_that_retires_the_token_passes(self):
        self.assertFalse(cbp.line_problem(
            'The cell reads Net-Neutral or Negative-Low, never `N/A`.'))
        self.assertFalse(cbp.line_problem(
            '`N/A` and `0%`/`-100%` are retired (`R-41`).'))
        self.assertFalse(cbp.line_problem(
            'the rows carry the barred word, not N/A'))

    def test_a_line_that_never_names_the_pair_is_out_of_scope(self):
        self.assertFalse(cbp.line_problem('| Geography | N/A |'))
        self.assertFalse(cbp.line_problem('0% resistance to Grudge'))


if __name__ == '__main__':
    unittest.main()
