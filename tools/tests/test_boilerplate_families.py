#!/usr/bin/env python3
"""
tools/tests/test_boilerplate_families.py

Locks the `gauge-default` family at the wording level, not the sentence level.

Batch 140 removed 133 instances of *"The Sorrow Gauge held at its opening band."*
from 76 records and lowered the family's ceiling to 0. Verification then searched
more loosely than the transform — `grep` for `opening band` rather than for the
exact sentence — and found **sixteen more** in a second wording on the C and D
pages of eight of the same sets:

    "The Sorrow Gauge held inside its opening band."

An exact-string guard would have left those sixteen standing and reported the
family at zero. That is the general lesson this file pins down: a detector has to
match the *claim*, not the sentence somebody happened to paste first.

The negative case matters just as much. `returns to its opening band` is a real
mechanic — "when that condition holds and the Sorrow Gauge returns to its opening
band, the cycle closes" — and nineteen records state it. It must never be flagged.
"""

import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'auditors'))

import check_boilerplate as boilerplate  # noqa: E402

FAMILIES = {name: pred for name, _, pred, _ in boilerplate.FAMILIES}


class TestGaugeDefault(unittest.TestCase):
    def setUp(self):
        self.fires = FAMILIES['gauge-default']

    def test_catches_the_original_wording(self):
        self.assertTrue(self.fires('...after every event. The Sorrow Gauge held at '
                                   'its opening band.\n\n## Appearance'))

    def test_catches_the_inside_wording(self):
        self.assertTrue(self.fires('...across the postings board. The Sorrow Gauge '
                                   'held inside its opening band. The cost is the '
                                   'nearness:'))

    def test_catches_a_within_wording(self):
        self.assertTrue(self.fires('The Sorrow Gauge held within its opening band.'))

    def test_does_not_catch_the_return_mechanic(self):
        self.assertFalse(self.fires(
            'When that condition holds and the Sorrow Gauge returns to its opening '
            'band, the cycle closes and the bearing is reset.'))

    def test_does_not_catch_a_gauge_that_moved(self):
        self.assertFalse(self.fires(
            'The Sorrow Gauge opened at 35% and climbed fifteen points with each '
            'collection it took from the chamber.'))


class TestActivationEcho(unittest.TestCase):
    def setUp(self):
        self.fires = FAMILIES['activation-echo']

    def test_catches_the_label_echo(self):
        self.assertTrue(self.fires(
            '| **Activation threshold** | Activation / expansion trigger — no '
            'breach counter |'))

    def test_catches_the_second_wording(self):
        self.assertTrue(self.fires(
            '| **Activation threshold** | Expansion / containment event — no '
            'breach counter |'))

    def test_does_not_catch_a_real_threshold(self):
        self.assertFalse(self.fires(
            '| **Activation threshold** | No breach counter; activates on direct '
            'gaze |'))

    def test_does_not_catch_a_gauge_threshold(self):
        self.assertFalse(self.fires(
            '| **Activation threshold** | Sorrow Gauge ≥ 75% |'))


class TestFamilyTableIsIntact(unittest.TestCase):
    """Every family stays wired, and every ceiling is a number."""

    def test_all_families_present(self):
        self.assertEqual(
            sorted(FAMILIES),
            sorted(['corrosion-stock', 'autobiography', 'set-opening',
                    'source-trace-doctrine', 'cost-opener', 'binding-opener',
                    'maintenance-line', 'shutdown-line', 'gauge-default',
                    'activation-echo', 'stigma-canonical']))

    def test_every_family_has_a_ceiling(self):
        for name in FAMILIES:
            self.assertIn(name, boilerplate.RATCHET)

    def test_gauge_default_ceiling_is_zero(self):
        self.assertEqual(boilerplate.RATCHET['gauge-default'], 0)


if __name__ == '__main__':
    unittest.main()
