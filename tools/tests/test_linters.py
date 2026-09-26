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

FIXTURE_DIR = os.path.join(os.path.dirname(__file__), "fixtures")

class TestTimelineLinter(unittest.TestCase):
    def setUp(self):
        self.current_year = 4238
        self.p_year = re.compile(r'\bYear\s+(\d{4})\b')
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
            if "Year 4247" in line:
                errors.append(f"B3 violation at line {line_num}")
            for m in self.p_year.finditer(line):
                y = int(m.group(1))
                if y > self.current_year:
                    errors.append(f"F1 violation: Year {y} at line {line_num}")
        return errors

    def test_good_fixture_passes(self):
        errors = self.check_timeline_file(os.path.join(FIXTURE_DIR, "good_timeline_sample.md"))
        self.assertEqual(len(errors), 0, f"Expected 0 errors on good fixture, got: {errors}")

    def test_future_year_caught(self):
        errors = self.check_timeline_file(os.path.join(FIXTURE_DIR, "bad_timeline_year_future.md"))
        self.assertTrue(any("F1 violation" in e or "B3 violation" in e for e in errors))

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


if __name__ == "__main__":
    unittest.main()
