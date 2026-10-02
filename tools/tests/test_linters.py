#!/usr/bin/env python3
"""
tools/tests/test_linters.py
Comprehensive unit test suite for Project Somnarak automated linters:
1. Timeline Linter (tools/timeline_lint.py logic)
2. Semantic Seam & Defect Linter (tools/seam_lint.py logic)
"""

import unittest
import os
import re
import sys

FIXTURE_DIR = os.path.join(os.path.dirname(__file__), "fixtures")

class TestTimelineLinter(unittest.TestCase):
    def setUp(self):
        self.current_year = 4238
        self.window_end = 4255
        self.p_year = re.compile(r'\bYear\s+(\d{4})\b')
        self.p_year_comma = re.compile(r'\bYears?\s+(\d),(\d{3})\b')
        self.p_cycles_ago = re.compile(r'(\d+)\s+cycles\s+ago', re.IGNORECASE)

    def check_timeline_file(self, filepath):
        errors = []
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for idx, line in enumerate(lines):
            line_num = idx + 1
            if "five hundred years ago" in line and ("Yoon" in line or "1,580" in line):
                errors.append(f"B1 violation at line {line_num}")
            if "founded 6,000 years ago" in line:
                errors.append(f"B2 violation at line {line_num}")
            years = [int(m.group(1)) for m in self.p_year.finditer(line)]
            years += [int(m.group(1) + m.group(2)) for m in self.p_year_comma.finditer(line)]
            for y in years:
                if y > self.window_end:
                    errors.append(f"F1 violation: Year {y} at line {line_num}")
        return errors

    def test_good_fixture_passes(self):
        errors = self.check_timeline_file(os.path.join(FIXTURE_DIR, "good_timeline_sample.md"))
        self.assertEqual(len(errors), 0, f"Expected 0 errors on good fixture, got: {errors}")

    def test_future_year_caught(self):
        errors = self.check_timeline_file(os.path.join(FIXTURE_DIR, "bad_timeline_year_future.md"))
        self.assertTrue(any("F1 violation" in e for e in errors))

    def test_6000_years_caught(self):
        errors = self.check_timeline_file(os.path.join(FIXTURE_DIR, "bad_timeline_6000_years.md"))
        self.assertTrue(any("B2 violation" in e for e in errors))

    def test_yoon_500_caught(self):
        errors = self.check_timeline_file(os.path.join(FIXTURE_DIR, "bad_timeline_yoon_500.md"))
        self.assertTrue(any("B1 violation" in e for e in errors))


class TestSeamLinter(unittest.TestCase):
    def setUp(self):
        self.banned_strings_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "banned_strings.txt")
        self.banned_patterns = []
        with open(self.banned_strings_path, "r", encoding="utf-8") as f:
            for l in f:
                l = l.strip()
                if l and not l.startswith("#"):
                    self.banned_patterns.append(re.compile(re.escape(l), re.IGNORECASE))

    def check_seam_file(self, filepath):
        violations = []
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        for p in self.banned_patterns:
            if p.search(content):
                violations.append(p.pattern)
        return violations

    def test_good_fixture_passes(self):
        violations = self.check_seam_file(os.path.join(FIXTURE_DIR, "good_seam_sample.md"))
        self.assertEqual(len(violations), 0, f"Expected 0 violations on good fixture, got: {violations}")

    def test_splice_caught(self):
        violations = self.check_seam_file(os.path.join(FIXTURE_DIR, "bad_seam_splice.md"))
        self.assertTrue(len(violations) > 0, "Expected splice violations caught")

    def test_out_of_1000_caught(self):
        violations = self.check_seam_file(os.path.join(FIXTURE_DIR, "bad_seam_out_of_1000.md"))
        self.assertTrue(any("out\\ of\\ 1000" in v or "1000" in v for v in violations))


class TestLabelLinter(unittest.TestCase):
    """V6-6: dossier table labels and bare [SE-code] tags."""

    GOOD = "SE-C-IIIγ-999_Good_Label_Sample.md"
    BAD = "SE-C-IIIγ-998_Bad_Label_Tag.md"

    def setUp(self):
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
        import label_lint
        self.lint = label_lint

    def audit(self, fixture):
        return self.lint.audit_file(os.path.join(FIXTURE_DIR, fixture))

    def codes(self, fixture):
        return [e.split("-> ")[1].split("]")[0].lstrip("[") for e in self.audit(fixture)]

    def test_good_fixture_passes(self):
        errors = self.audit(self.GOOD)
        self.assertEqual(len(errors), 0, f"Expected 0 errors on good fixture, got: {errors}")

    def test_self_name_label_caught(self):
        self.assertIn("LABEL_SELF_NAME", self.codes(self.BAD))

    def test_code_parenthetical_label_caught(self):
        self.assertIn("LABEL_CODE_PAREN", self.codes(self.BAD))

    def test_bare_code_tag_in_table_cell_caught(self):
        # The V6-1 revert missed 395 tags because they sat inside table cells
        # rather than at the end of a sentence. This guards that regression.
        self.assertIn("BARE_CODE_TAG", self.codes(self.BAD))

    def test_entry_callout_self_name_caught(self):
        # 509 of these survived the V6-1 revert because it only swept table
        # labels and [SE-] tags, never the bold Entry callout headers.
        self.assertIn("CALLOUT_SELF_NAME", self.codes(self.BAD))

    def test_undecorated_entry_callout_passes(self):
        self.assertIsNone(self.lint.P_ENTRY_DECOR.search(
            "**Entry 3 \u2014 <Excerpt from Counseling Log>**"))

    def test_worktype_self_name_caught(self):
        # A third syntactic position for the same V5-12 decoration: 302 of
        # these survived both the V6-1 sweep and the R5 Entry-callout rule.
        self.assertIn("WORKTYPE_SELF_NAME", self.codes(self.BAD))

    def test_undecorated_worktype_label_passes(self):
        self.assertIsNone(self.lint.P_WORKTYPE_DECOR.search(
            "| **Flerehan** | Softens and withdraws. | Decrease |"))

    def test_worktype_parenthetical_that_is_not_the_name_is_ignored(self):
        # "(Tears)" is the canonical gloss and must never be stripped.
        m = self.lint.P_WORKTYPE_DECOR.search("| **Flerehan (Tears)** | x |")
        self.assertIsNotNone(m)
        self.assertEqual(m.group(2), "Tears")

    def test_unknown_label_caught(self):
        self.assertIn("LABEL_NOT_ALLOWED", self.codes(self.BAD))

    def test_markdown_link_is_not_a_bare_tag(self):
        self.assertIsNone(self.lint.P_BARE_TAG.search("see [SE-C-IIIγ-021](../x.md) for detail"))
        self.assertIsNotNone(self.lint.P_BARE_TAG.search("throw it off. [SE-C-IIIγ-021]"))

    def test_schema_label_is_allowed(self):
        self.assertTrue(self.lint.label_allowed("Starting Sorrow Gauge"))
        self.assertFalse(self.lint.label_allowed("Starting Sorrow Gauge (The Maw)"))


if __name__ == "__main__":
    unittest.main()
