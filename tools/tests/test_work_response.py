#!/usr/bin/env python3
"""tests for check_work_response.py — the Element row decides the four signs."""

import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'auditors'))

import check_work_response as wr  # noqa: E402


def dossier(element, entity='**Subject**', rows=None):
    rows = rows or [('Flerehan', 'Decrease'), ('Pugnahan', 'Increase'),
                    ('Viderehan', 'Stable'), ('Ferrehan', 'Decrease')]
    body = '\n'.join('| **%s** (x) | something | %s |' % (k, g) for k, g in rows)
    return ('| **Entity Type** | %s |\n| **Element** | %s |\n'
            '| Work Type | Response | Gauge Change |\n|---|---|---|\n%s\n'
            % (entity, element, body))


SUBJECT = {
    'Lament': [('Flerehan', 'Decrease'), ('Pugnahan', 'Increase'),
               ('Viderehan', 'Stable'), ('Ferrehan', 'Stable')],
    'Grudge': [('Flerehan', 'Increase'), ('Pugnahan', 'Decrease'),
               ('Viderehan', 'Stable'), ('Ferrehan', 'Stable')],
    'Void': [('Flerehan', 'Stable'), ('Pugnahan', 'Stable'),
             ('Viderehan', 'Decrease'), ('Ferrehan', 'Increase')],
    'Weight': [('Flerehan', 'Stable'), ('Pugnahan', 'Stable'),
               ('Viderehan', 'Increase'), ('Ferrehan', 'Decrease')],
}

RELIC = {
    'Lament': [('Flerehan', 'N/A'), ('Pugnahan', 'N/A'),
               ('Viderehan', 'Stable'), ('Ferrehan', 'Stable')],
    'Void': [('Flerehan', 'N/A'), ('Pugnahan', 'N/A'),
             ('Viderehan', 'Decrease'), ('Ferrehan', 'Increase')],
    'Weight': [('Flerehan', '—'), ('Pugnahan', '—'),
               ('Viderehan', 'Increase'), ('Ferrehan', 'Decrease')],
}


class FollowsTheMatrix(unittest.TestCase):
    def test_each_element_has_its_own_shape(self):
        for element, rows in SUBJECT.items():
            self.assertEqual(wr.scan_text(dossier(element, rows=rows)), [],
                             element)

    def test_the_four_shapes_are_all_different(self):
        vectors = {e: tuple(g for _, g in r) for e, r in SUBJECT.items()}
        self.assertEqual(len(set(vectors.values())), 4)

    def test_relics_are_graded_on_the_two_cells_they_have(self):
        for element, rows in RELIC.items():
            self.assertEqual(wr.scan_text(dossier(element, '**Object/Place**',
                                                  rows=rows)), [], element)


class BreaksTheMatrix(unittest.TestCase):
    def test_the_retired_monoculture_is_caught_in_every_element(self):
        old = [('Flerehan', 'Decrease'), ('Pugnahan', 'Increase'),
               ('Viderehan', 'Stable'), ('Ferrehan', 'Decrease')]
        for element in ('Lament', 'Grudge', 'Void'):
            self.assertTrue(wr.scan_text(dossier(element, rows=old)), element)
        # Void is the sharpest: observation should be the strong work, and the
        # old table has it inert while endurance — its Weak cell — does the work.
        hits = dict((w, (g, want)) for w, g, want in
                    wr.scan_text(dossier('Void', rows=old)))
        self.assertEqual(hits['Viderehan'], ('Stable', 'Decrease'))
        self.assertEqual(hits['Ferrehan'], ('Decrease', 'Increase'))

    def test_a_relic_may_not_claim_a_barred_work_type(self):
        bad = [('Flerehan', 'Decrease'), ('Pugnahan', 'N/A'),
               ('Viderehan', 'Stable'), ('Ferrehan', 'Stable')]
        hits = wr.scan_text(dossier('Lament', '**Object/Place**', rows=bad))
        self.assertEqual(hits[0][:2], ('Flerehan', 'Decrease'))
        self.assertEqual(hits[0][2], 'N/A')

    def test_a_missing_sign_is_reported_not_skipped(self):
        bad = [('Flerehan', 'Nothing happens'), ('Pugnahan', 'Increase'),
               ('Viderehan', 'Stable'), ('Ferrehan', 'Stable')]
        hits = wr.scan_text(dossier('Lament', rows=bad))
        self.assertEqual(hits[0][0], 'Flerehan')


class Scope(unittest.TestCase):
    def test_a_dossier_without_an_element_row_is_not_graded(self):
        text = ('| **Entity Type** | **Subject** |\n'
                '| Work Type | Response | Gauge Change |\n|---|---|---|\n'
                '| **Flerehan** (x) | a | Decrease |\n')
        self.assertIsNone(wr.scan_text(text))

    def test_a_mixed_element_is_not_graded(self):
        rows = SUBJECT['Lament']
        self.assertIsNone(wr.scan_text(
            dossier('Mixed — Lament base with strong Hope emergence', rows=rows)))
        self.assertIsNone(wr.scan_text(dossier('All four', rows=rows)))

    def test_the_exemption_has_a_reason_and_a_shipped_count(self):
        self.assertTrue(wr.EXEMPT)
        for key, reason in wr.EXEMPT.items():
            self.assertRegex(key, r'^SE-[A-Z]-[IV]+')
            self.assertGreater(len(reason), 60)

    def test_corpus_stays_under_the_ratchet(self):
        files, hits = wr.measure()
        self.assertGreater(len(files), 290, 'the glob stopped matching dossiers')
        self.assertLessEqual(len(hits), wr.RATCHET,
                             '%d off the matrix' % len(hits))


if __name__ == '__main__':
    unittest.main()
