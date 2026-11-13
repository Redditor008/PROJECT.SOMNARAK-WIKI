#!/usr/bin/env python3
"""
tools/tests/test_series_counts.py

A numeral pool is not a repeated sentence, so `check_boilerplate` cannot see it
and `check_slot_templates` cannot either — the sentence around the number is
different every time and only the number is shared.

The tests pin three things: a pool of three fires, a pair does not (two holdings
can agree by chance; three cannot), and the shipped archive is at zero after the
batch-150 repair. Fixtures are written to a temp directory and removed.
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

import check_series_counts as series  # noqa: E402


class PoolTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)

    def write(self, name, body):
        path = os.path.join(self.tmp, name)
        io.open(path, 'w', encoding='utf-8').write(body)
        return path

    def test_three_dossiers_sharing_a_series_length_is_a_pool(self):
        paths = [self.write(f'{i}.md', 'The record closes after 211 cycles.')
                 for i in range(3)]
        _, seen = series.measure(paths)
        self.assertEqual(len(series.pools(seen)), 1)
        self.assertEqual(series.pools(seen)[0][:2], (211, 'cycles'))

    def test_two_dossiers_are_a_coincidence_not_a_pool(self):
        paths = [self.write(f'{i}.md', 'The record closes after 211 cycles.')
                 for i in range(2)]
        _, seen = series.measure(paths)
        self.assertEqual(series.pools(seen), [])
        self.assertEqual(len(series.pools(seen, minimum=2)), 1)

    def test_same_number_different_unit_is_not_a_pool(self):
        paths = [self.write('a.md', 'After 211 cycles it closed.'),
                 self.write('b.md', 'After 211 sessions it closed.'),
                 self.write('c.md', 'After 211 watches it closed.')]
        _, seen = series.measure(paths)
        self.assertEqual(series.pools(seen), [])

    def test_small_event_counts_are_ignored(self):
        # "four occurrences" is an event count on one page, not a series length.
        paths = [self.write(f'{i}.md', 'There were four occurrences.') for i in range(5)]
        _, seen = series.measure(paths)
        self.assertEqual(seen, {})

    def test_a_pool_of_a_figure_never_seen_before_still_fires(self):
        # The guard must not be a list of the two numbers that were actually bad.
        paths = [self.write(f'{i}.md', 'Ninety years of work: 1,407 descents.')
                 for i in range(4)]
        _, seen = series.measure(paths)
        self.assertEqual([p[:2] for p in series.pools(seen)], [(1407, 'descents')])


class ShippedTreeTest(unittest.TestCase):
    def test_no_pool_in_the_archive(self):
        files, seen = series.measure()
        self.assertGreater(len(files), 290, 'the glob stopped matching dossiers')
        found = series.pools(seen)
        self.assertEqual(found, [], f'{len(found)} pooled figure(s): '
                                    f'{[(v, u, len(o)) for v, u, o in found]}')

    def test_the_four_pools_are_gone(self):
        # Not "the numeral disappeared" — one dossier may still hold 211 sessions
        # on its own evidence. What must be gone is the *pool*: three or more
        # files agreeing on a series length they cannot all have measured.
        _, seen = series.measure()
        pooled = {(v, u) for v, u, _ in series.pools(seen)}
        for pair in ((188, 'cycles'), (211, 'cycles'),
                     (211, 'sessions'), (211, 'watches')):
            with self.subTest(pair=pair):
                self.assertNotIn(pair, pooled)

    def test_the_world_clock_is_not_a_series_count(self):
        # "nine years" appears in dozens of files and must never be flagged.
        _, seen = series.measure()
        for (value, unit) in seen:
            self.assertNotEqual(unit, 'years')


if __name__ == '__main__':
    unittest.main()
