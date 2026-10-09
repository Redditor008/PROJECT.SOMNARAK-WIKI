#!/usr/bin/env python3
"""Focused tests for conservative M.A.W. field normalization."""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import maw_compare


class TestMawComparison(unittest.TestCase):
    def test_same_range_matches_when_codex_omits_redundant_element(self):
        primary = maw_compare.normalize_scalar("damage", "Grudge 3–6")
        codex = maw_compare.normalize_scalar("damage", "3-6")
        self.assertTrue(maw_compare.equivalent_values("damage", primary, codex))

    def test_different_damage_ranges_do_not_match(self):
        primary = maw_compare.normalize_scalar("damage", "Lament 6–10")
        codex = maw_compare.normalize_scalar("damage", "5–9")
        self.assertFalse(maw_compare.equivalent_values("damage", primary, codex))

    def test_explicitly_different_damage_elements_do_not_match(self):
        primary = maw_compare.normalize_scalar("damage", "Weight 7–12")
        codex = maw_compare.normalize_scalar("damage", "Grudge 7–12")
        self.assertFalse(maw_compare.equivalent_values("damage", primary, codex))

    def test_mixed_is_recognized_as_an_explicit_damage_type(self):
        self.assertEqual(
            maw_compare.normalize_scalar("damage", "Mixed 10–15"),
            ("mixed", 10.0, 15.0),
        )

    def test_speed_descriptor_is_compared_when_both_records_state_it(self):
        fast = maw_compare.normalize_scalar("speed", "3 — Fast")
        normal = maw_compare.normalize_scalar("speed", "3 (Normal)")
        self.assertFalse(maw_compare.equivalent_values("speed", fast, normal))

    def test_range_descriptor_is_compared_when_both_records_state_it(self):
        medium = maw_compare.normalize_scalar("range", "3 — Medium")
        long = maw_compare.normalize_scalar("range", "3 (Long: 4–8m)")
        self.assertFalse(maw_compare.equivalent_values("range", medium, long))

    def test_combined_speed_range_row_is_split_into_fields(self):
        facts = maw_compare.doc_facts(
            "\n".join(
                [
                    "| Field | Record |",
                    "|---|---|",
                    "| Speed / Range | 3 — Fast / 3 — Medium |",
                ]
            ),
            "Weapon",
        )
        self.assertEqual(facts["speed"], ["3 — Fast"])
        self.assertEqual(facts["range"], ["3 — Medium"])


if __name__ == "__main__":
    unittest.main()
