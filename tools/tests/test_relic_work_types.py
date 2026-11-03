#!/usr/bin/env python3
"""tests for check_relic_work_types.py — R-40: a relic is handled, not worked."""

import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'auditors'))

import check_relic_work_types as relic  # noqa: E402

TABLE = """## Behavior

| Work Type | Response | Gauge Change |
|---|---|---|
| **Flerehan** | N/A | N/A |
| **Pugnahan** | N/A | N/A |
| **Viderehan** | something | Stable |
| **Ferrehan** | something | Decrease |
"""

HANDLED = """## Handling Process

| Stage | What is done | Who holds it | What it costs |
|---|---|---|---|
| **Approach** | posting | duty Warden | a watch |
"""


def dossier(kind, body, work_row=True):
    row = '| **Valid Work Types** | x |\n' if work_row else '| **Handling** | x |\n'
    return '| **Entity Type** | **%s** |\n%s%s' % (kind, row, body)


class FindsTheRetiredShape(unittest.TestCase):
    def test_a_relic_with_a_work_table_is_flagged(self):
        bad = relic.offences(dossier('Object/Place', TABLE))
        self.assertIn('## Behavior section', bad)
        self.assertIn('Valid Work Types row', bad)
        self.assertTrue(any('Work Type row' in b for b in bad))

    def test_a_converted_relic_is_clean(self):
        self.assertEqual(relic.offences(dossier('Object', HANDLED, work_row=False)), [])


class Scope(unittest.TestCase):
    def test_a_subject_keeps_its_table(self):
        self.assertFalse(relic.is_relic(dossier('**Subject** — mobile', '')))

    def test_every_non_subject_is_a_relic(self):
        for kind in ('**Object**', '**Place**', '**Time**',
                     '**Hazard**', '**Possession**'):
            self.assertTrue(relic.is_relic(dossier(kind, '')), kind)

    def test_a_file_with_no_entity_type_is_not_graded(self):
        self.assertFalse(relic.is_relic('# no row here\n'))


class ShippedTree(unittest.TestCase):
    def test_ratchet_holds_and_goes_down_only(self):
        files, hits, converted = relic.measure()
        self.assertGreater(len(files), 140, 'the glob stopped matching relics')
        self.assertLessEqual(len(hits), relic.RATCHET, '%d still worked' % len(hits))
        self.assertEqual(len(hits) + len(converted), len(files))
        self.assertLess(relic.RATCHET, 143, 'the ratchet has not been set below the start')


if __name__ == '__main__':
    unittest.main()
