#!/usr/bin/env python3
"""tests for check_work_preference.py — 0%, -100%, and the one threat reading."""

import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'auditors'))

import check_work_preference as pref  # noqa: E402


def table(a, b, c, d, kind='**Object/Place**', hp=650):
    rows = [('Flerehan', a), ('Pugnahan', b), ('Viderehan', c), ('Ferrehan', d)]
    body = '\n'.join('| **%s** (x) | what it does | %s |' % (k, g) for k, g in rows)
    return ('| **Entity Type** | %s |\n| **Sorrow Gauge [HP]** | %d/%d |\n'
            '| Work Type | Response | Gauge Change |\n|---|---|---|\n%s\n'
            % (kind, hp, hp, body))


class TheAlphabet(unittest.TestCase):
    def test_percentage_cells_read_back(self):
        self.assertEqual(pref.normalize(' -100% '), '-100%')
        self.assertEqual(pref.normalize('0%'), '0%')
        self.assertEqual(pref.normalize('**-100%**'), '-100%')

    def test_the_old_forms_are_retired_not_silently_accepted(self):
        self.assertEqual(pref.normalize('N/A'), 'RETIRED')
        self.assertEqual(pref.normalize('—'), 'RETIRED')

    def test_a_minus_sign_is_not_a_retired_cell(self):
        # The bug this test exists for: a dead-cell pattern run before the
        # percentage pattern read `-100%` as a dash and every converted relic
        # was reported as still carrying N/A.
        self.assertNotEqual(pref.normalize('-100%'), 'RETIRED')

    def test_the_signs_and_neutral(self):
        self.assertEqual(pref.normalize('Decrease'), 'Down')
        self.assertEqual(pref.normalize('Increase'), 'Up')
        self.assertEqual(pref.normalize('Stable'), 'Neutral')
        self.assertEqual(pref.normalize('No movement'), 'Neutral')


class TheBarredPair(unittest.TestCase):
    def test_a_converted_relic_is_clean(self):
        text = table('0%', '0%', 'Neutral', 'Down', hp=420)
        self.assertEqual(pref.vector_of(text), ['0%', '0%', 'Neutral', 'Down'])
        self.assertEqual(pref.barred_pair_problems(['0%', '0%']), [])

    def test_an_unequal_pair_is_refused(self):
        bad = pref.barred_pair_problems(['0%', '-100%'])
        self.assertTrue(bad)
        self.assertIn('one threat reading', ' '.join(bad))

    def test_a_recorded_increase_on_a_barred_cell_is_refused(self):
        bad = pref.barred_pair_problems(['0%', 'Up'])
        self.assertTrue(bad)


class TheThreatPoint(unittest.TestCase):
    def test_under_five_hundred_gives_zero(self):
        text = table('0%', '0%', 'Neutral', 'Down', hp=499)
        files, problems, dist = None, [], None
        vec = pref.vector_of(text)
        hp = int(pref.HP.search(text).group(1))
        self.assertEqual('-100%' if hp >= 500 else '0%', '0%')
        self.assertEqual(vec[:2], ['0%', '0%'])

    def test_at_five_hundred_gives_minus_one_hundred(self):
        text = table('-100%', '-100%', 'Neutral', 'Down', hp=500)
        hp = int(pref.HP.search(text).group(1))
        self.assertEqual('-100%' if hp >= 500 else '0%', '-100%')

    def test_the_two_cells_are_one_number_not_two_checks(self):
        # A dossier whose pair is split cannot be produced by the rule at all.
        self.assertTrue(pref.barred_pair_problems(['-100%', '0%']))


class ShippedTree(unittest.TestCase):
    def test_corpus_is_on_the_alphabet_and_under_the_ratchet(self):
        files, problems, dist = pref.measure()
        self.assertGreater(len(files), 295, 'the glob stopped matching dossiers')
        self.assertEqual(problems, [], '%d dossiers off the alphabet' % len(problems))
        on_two = sum(n for _, n in dist.most_common(2))
        self.assertLessEqual(on_two, pref.RATCHET, '%d on two vectors' % on_two)

    def test_the_palette_is_bigger_than_what_is_in_use(self):
        _, _, dist = pref.measure()
        self.assertGreater(len(dist), 5)
        pairs = {(v[2], v[3]) for v in dist}
        self.assertGreaterEqual(len(pairs), 4)


if __name__ == '__main__':
    unittest.main()
