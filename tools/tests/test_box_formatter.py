#!/usr/bin/env python3
"""
tools/tests/test_box_formatter.py
Unit tests for tools/box_formatter.py (TablesGenerator Reference Engine)
"""

import unittest
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from box_formatter import (
    get_char_width,
    get_display_width,
    pad_cell_display_width,
    wrap_cell_text,
    compute_col_widths,
    make_table,
    make_kv_table,
    make_box,
    make_borderless_banner
)

class TestBoxFormatter(unittest.TestCase):

    def test_display_width_ascii_and_cjk(self):
        self.assertEqual(get_display_width("abc"), 3)
        self.assertEqual(get_display_width("한글"), 4)
        self.assertEqual(get_display_width("Test [한글] End"), 15)

    def test_pad_cell_display_width(self):
        padded_left = pad_cell_display_width("Item", 10, align="left")
        self.assertEqual(padded_left, "Item      ")
        self.assertEqual(get_display_width(padded_left), 10)

        padded_right = pad_cell_display_width("Item", 10, align="right")
        self.assertEqual(padded_right, "      Item")
        self.assertEqual(get_display_width(padded_right), 10)

        padded_center = pad_cell_display_width("Item", 10, align="center")
        self.assertEqual(padded_center, "   Item   ")
        self.assertEqual(get_display_width(padded_center), 10)

    def test_wrap_cell_text_no_truncation(self):
        text = "This is a long sentence that must wrap without any truncated words across lines cleanly."
        wrapped = wrap_cell_text(text, inner_w=20, max_subrows=5)
        self.assertTrue(len(wrapped) <= 5)
        for w in wrapped:
            self.assertTrue(get_display_width(w) <= 20)
        # Ensure words are not sliced
        reconstructed = " ".join(wrapped)
        self.assertIn("sentence", reconstructed)
        self.assertIn("truncated", reconstructed)

    def test_wrap_cell_text_long_token_split(self):
        long_token = "origin/arena/01a0b699-project-somnarak-wiki"
        wrapped = wrap_cell_text(long_token, inner_w=20, max_subrows=5)
        for w in wrapped:
            self.assertTrue(get_display_width(w) <= 20)

    def test_compute_col_widths_74(self):
        widths_1 = compute_col_widths(1, total_width=74)
        self.assertEqual(widths_1, [72])
        self.assertEqual(sum(widths_1) + 2, 74)

        widths_2 = compute_col_widths(2, total_width=74)
        self.assertEqual(widths_2, [26, 45])
        self.assertEqual(sum(widths_2) + 3, 74)

        widths_3 = compute_col_widths(3, total_width=74)
        self.assertEqual(sum(widths_3) + 4, 74)

    def test_make_box_exact_74(self):
        box = make_box(
            "TEST TITLE HUD",
            [
                "Line 1 content",
                "Line 2 with very long content that wraps across multiple sub-rows without breaking the 74-character width.",
                "---",
                "Footer line status: ALL PASS"
            ],
            width=74
        )
        lines = box.splitlines()
        for idx, l in enumerate(lines, 1):
            self.assertEqual(len(l), 74, f"Line {idx} length {len(l)} != 74: {l}")
            self.assertEqual(get_display_width(l), 74, f"Line {idx} display width {get_display_width(l)} != 74: {l}")
            self.assertTrue(l.startswith("+") or l.startswith("|"))
            self.assertTrue(l.endswith("+") or l.endswith("|"))

    def test_make_table_exact_74_tablesgenerator(self):
        table = make_table(
            title="SYSTEM VALIDATION TABLE",
            headers=["COMPONENT", "SPECIFICATION DETAIL"],
            rows=[
                ["Borders", "Pure ASCII (+, -, |, =) matching TablesGenerator text tables."],
                ["Wrapping", "Multi-line cell wrapping adhering to the 5-Row Vertical Growth Rule."],
                ["Git Branch", "arena/01a0b699-project-somnarak-wiki committed upstream."]
            ],
            width=74,
            style="rst"
        )
        lines = table.splitlines()
        for idx, l in enumerate(lines, 1):
            self.assertEqual(len(l), 74, f"Line {idx} length {len(l)} != 74: {l}")
            self.assertEqual(get_display_width(l), 74, f"Line {idx} display width {get_display_width(l)} != 74: {l}")
            self.assertTrue(l.startswith("+") or l.startswith("|"))
            self.assertTrue(l.endswith("+") or l.endswith("|"))

    def test_make_kv_table(self):
        kv = make_kv_table(
            [
                ["Repository", "PROJECT.SOMNARAK-WIKI"],
                ["Current Year", "Year 4,238 Mugenhan Standard"],
                ["Linter Pass Rate", "100% across all 1,785 scanned files"]
            ],
            width=74
        )
        lines = kv.splitlines()
        for idx, l in enumerate(lines, 1):
            self.assertEqual(len(l), 74, f"Line {idx} length {len(l)} != 74: {l}")

    def test_make_borderless_banner(self):
        banner = make_borderless_banner("DISPATCH ALERT", ["Subsystem 1 Online", "Subsystem 2 Nominal"], width=74)
        for idx, l in enumerate(banner.splitlines(), 1):
            self.assertEqual(len(l), 74, f"Line {idx} length {len(l)} != 74: {l}")

if __name__ == "__main__":
    unittest.main()
