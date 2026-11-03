#!/usr/bin/env python3
"""
tools/tests/test_slot_templates.py

The five families are slot templates: sentences whose nouns change and whose
claim does not. The point of the guard is not to ban five strings — a banned
string is a checklist, and a checklist is what batch 130 got wrong when a
hand-written list of nine template strings missed two families. The point is to
ban the *shape*, so a new variant fails even though nobody wrote it down.

That is what these tests pin: the matcher fires on an instance it has never seen,
it does not fire on the bespoke sentence that replaced one, and the shipped tree
measures zero. Fixtures are inline strings; nothing is written to the archive.
"""

import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'auditors'))

import check_slot_templates as slots  # noqa: E402


def matches(text):
    return [name for name, _, match, _ in slots.FAMILIES if match(text)]


class TestFamiliesFire(unittest.TestCase):
    def test_register_bullet_as_shipped(self):
        self.assertEqual(matches('- Expresses Lament pressure in a lament register.'),
                         ['element-register-bullet'])

    def test_register_bullet_article_variant(self):
        # "an odd register" — the article must not be the thing that decides.
        self.assertEqual(matches('- Expresses Void pressure in an anomalous register.'),
                         ['element-register-bullet'])

    def test_form_unmistakable_as_shipped(self):
        self.assertEqual(
            matches('- The hazard form is unmistakable — this is a lament entity, '
                    'not a general one.'),
            ['form-unmistakable'])

    def test_first_catalogued_with_a_chained_clause(self):
        # The 9xx files that padded the claim with a real clause.
        self.assertEqual(
            matches('- One of the first catalogued **Object-Mind** entities in '
                    'Somnarak, and the only one that was built on purpose by a '
                    'person who is named.'),
            ['first-catalogued'])

    def test_structural_uniqueness(self):
        self.assertEqual(
            matches('- Its grudge descriptor makes it structurally unique among '
                    'hazard entities.'),
            ['structural-uniqueness'])

    def test_register_feels_different(self):
        self.assertEqual(
            matches('- The weight pressure in the body register feels different '
                    'from standard weight — more specific, more personal.'),
            ['register-feels-different'])

    def test_unseen_variant_still_fires(self):
        # Nobody wrote this sentence; the shape is what is banned.
        self.assertEqual(
            matches('- The void pressure in the dream register feels unlike '
                    'standard void.'),
            ['register-feels-different'])


class TestBespoKeIsClean(unittest.TestCase):
    def test_replacement_lines_do_not_match(self):
        clean = [
            "- It breathes nine times a minute, and the rate has never matched "
            "the respiration of anybody standing in the corridor.",
            "- Of 527 logged arrivals, none has been shortened by anything "
            "anybody did; the mean dwell of two minutes fifty seconds has not "
            "moved in seventeen years.",
            "- 211 channels are on file, and closing one ends it within the "
            "second in every one of them.",
            "- The hall seats forty-four, and at dusk the seats fill in the "
            "order of precedence recorded on the hall plan.",
        ]
        for line in clean:
            with self.subTest(line=line[:40]):
                self.assertEqual(matches(line), [])

    def test_a_reading_that_can_be_wrong_is_not_a_slot(self):
        # Same subject matter, opposite property: it names a figure, a series
        # and a method, so it is a reading rather than a restatement.
        self.assertEqual(
            matches("- The gauge stood at 60 per cent for eleven days, and fell "
                    "to 40 when the pipe route was grouted."),
            [])


class TestShippedTree(unittest.TestCase):
    def test_dossiers_are_clean(self):
        files, hits = slots.measure()
        self.assertGreater(len(files), 290, 'the glob stopped matching dossiers')
        for name, found in hits.items():
            with self.subTest(family=name):
                self.assertEqual(found, [], f'{name} has {len(found)} instance(s)')

    def test_ratchet_is_at_zero(self):
        self.assertEqual(set(slots.RATCHET), {n for n, _, _, _ in slots.FAMILIES})
        for name, ceiling in slots.RATCHET.items():
            self.assertEqual(ceiling, 0, f'{name} ceiling should be at the floor')

    def test_line_matching_counts_instances_not_files(self):
        # measure() must report every line, because a dossier that printed the
        # same slot five times carried five defects, not one.
        fixture = os.path.join(ROOT, 'tools', 'tests', 'fixtures',
                               'slot_templates_dirty.md')
        hits = slots.measure(paths=[fixture])[1]
        self.assertEqual(len(hits['element-register-bullet']), 2)


if __name__ == '__main__':
    unittest.main()
