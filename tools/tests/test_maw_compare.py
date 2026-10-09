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

    def test_item_codex_combined_pattern_coverage_and_falloff_rows_parse(self):
        facts = maw_compare.doc_facts(
            "\n".join(
                [
                    "| Field | Record |",
                    "|---|---|",
                    "| Pattern / Coverage | Single / one designated target |",
                    "| Coverage / Falloff | Line, up to 3 targets: 100% → 70% → 50% |",
                ]
            ),
            "Weapon",
        )
        self.assertEqual(maw_compare.normalize_scalar("pattern", facts["pattern"][0]), "single")
        self.assertIn(1.0, {maw_compare.normalize_scalar("coverage", value) for value in facts["coverage"]})
        self.assertIn(3.0, {maw_compare.normalize_scalar("coverage", value) for value in facts["coverage"]})
        self.assertEqual(maw_compare.normalize_scalar("falloff", facts["falloff"][0]), (100.0, 70.0, 50.0))

    def test_full_side_card_pages_parse_weapon_suit_and_stigma_fields(self):
        text = "\n".join(
            [
                "## PAGE 04 — WEAPON STAT CARD",
                "### M.A.W. Weapon — Test Fang",
                "| Field | Record |",
                "|---|---|",
                "| Damage | Grudge 7–12 |",
                "| Speed / Range | 3 — Fast / 3 — Medium |",
                "| Pattern | Skewer — up to 3 targets; 100% → 70% → 50% |",
                "| Maximum Amount / Echo Cost | 3 / 40 Sorrow Echoes |",
                "## PAGE 05 — SUIT STAT CARD",
                "### M.A.W. Suit — Test Veil",
                "| Lament | Grudge | Void | Weight | Maximum / Echo Cost |",
                "|---|---|---|---|---|",
                "| 0.4 — Resistant | 1.0 — Normal | 1.6 — Weak | 0.8 — Warded | 3 / 35 |",
                "## PAGE 06 — STIGMA STAT CARD",
                "### M.A.W. Stigma — Test Charm",
                "| Field | Record |",
                "|---|---|",
                "| Slot / chance | Tail / 4% |",
                "| Grade / element | β / Void |",
                "| Source bonus | +2 to the named check |",
            ]
        )
        cards = maw_compare.parse_side_cards(text)
        self.assertEqual(set(cards), {"Weapon", "Suit", "Stigma"})
        weapon = cards["Weapon"]["facts"]
        self.assertEqual(weapon["speed"], ["3 — Fast"])
        self.assertEqual(weapon["range"], ["3 — Medium"])
        self.assertEqual(weapon["max_amount"], ["3"])
        self.assertEqual(weapon["echo_cost"], ["40 Sorrow Echoes"])
        self.assertEqual(weapon["coverage"], ["up to 3 targets"])
        self.assertEqual(weapon["falloff"], ["Skewer — up to 3 targets; 100% → 70% → 50%"])
        self.assertEqual(len(cards["Suit"]["facts"]["resistance"]), 4)
        self.assertEqual(cards["Stigma"]["facts"]["slot"], ["Tail / 4%"])
        self.assertEqual(cards["Stigma"]["facts"]["chance"], ["4%"])
        self.assertEqual(cards["Stigma"]["facts"]["grade"], ["β"])

    def test_compact_bullet_cards_are_classified_and_parsed_by_equipment_type(self):
        text = "\n".join(
            [
                "## PAGE 04–06 — COMPACT M.A.W. CARDS",
                "- **Edge Fang:** Grudge 7–12; Speed 3; Range 3; Skewer; up to 3 targets; 100% → 70% → 50%; 3 maximum; 40 Echoes. A short note.",
                "- **Edge Veil:** Lament 0.4 / Grudge 1.0 / Void 1.6 / Weight 0.8; 3 maximum; 35 Echoes. A short note.",
                "- **Edge Charm:** Tail; 4%; +2 Resilience during source work. A short note.",
            ]
        )
        cards = maw_compare.parse_side_cards(text)
        self.assertEqual(set(cards), {"Weapon", "Suit", "Stigma"})
        self.assertEqual(cards["Weapon"]["facts"]["damage"], ["Grudge 7–12"])
        self.assertEqual(cards["Weapon"]["facts"]["max_amount"], ["3"])
        self.assertEqual(cards["Weapon"]["facts"]["falloff"], ["Grudge 7–12; Speed 3; Range 3; Skewer; up to 3 targets; 100% → 70% → 50%; 3 maximum; 40 Echoes"])
        self.assertEqual(len(cards["Suit"]["facts"]["resistance"]), 4)
        self.assertEqual(cards["Suit"]["facts"]["max_amount"], ["3"])
        self.assertEqual(cards["Stigma"]["facts"]["slot"], ["Tail"])
        self.assertEqual(cards["Stigma"]["facts"]["chance"], ["4%"])

    def test_compact_equipment_table_cards_are_parsed(self):
        text = "\n".join(
            [
                "## PAGE 04 — COMPACT EQUIPMENT CARDS",
                "### Test Fang",
                "| Field | Record |",
                "|---|---|",
                "| Damage | Lament 5–9 |",
                "| Speed / Range | 2 — Normal / 2 — Short |",
                "| Pattern | Single — one designated target |",
                "| Falloff | 100% → 70% → 50% |",
                "| Cost | 25 Sorrow Echoes |",
                "### Test Veil",
                "| Element | Resistance |",
                "|---|---|",
                "| Lament | 0.4 — Resistant |",
                "| Grudge | 1.0 — Normal |",
                "| Void | 1.6 — Weak |",
                "| Weight | 0.8 — Warded |",
                "### Test Charm",
                "| Field | Record |",
                "|---|---|",
                "| Slot | Tail |",
                "| Acquisition Chance | 5% |",
                "| Set Effect | +1 during source work |",
            ]
        )
        cards = maw_compare.parse_side_cards(text)
        self.assertEqual(set(cards), {"Weapon", "Suit", "Stigma"})
        self.assertEqual(cards["Weapon"]["facts"]["damage"], ["Lament 5–9"])
        self.assertEqual(cards["Weapon"]["facts"]["falloff"], ["100% → 70% → 50%"])
        self.assertEqual(cards["Suit"]["facts"]["resistance"][0], ("Lament", "0.4"))
        self.assertEqual(cards["Stigma"]["facts"]["slot"], ["Tail"])
        self.assertEqual(cards["Stigma"]["facts"]["chance"], ["5%"])

    def test_coverage_ignores_unrelated_numbers_and_extracts_target_counts(self):
        self.assertIsNone(maw_compare.normalize_scalar("coverage", "360° radial area burst"))
        self.assertEqual(maw_compare.normalize_scalar("coverage", "up to 3 targets"), 3.0)
        self.assertEqual(maw_compare.normalize_scalar("coverage", "1 designated target at point-blank range"), 1.0)


if __name__ == "__main__":
    unittest.main()
