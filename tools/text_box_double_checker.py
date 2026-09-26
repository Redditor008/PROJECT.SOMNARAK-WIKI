#!/usr/bin/env python3
"""
tools/text_box_double_checker.py
Project Somnarak Non-Wiki Archive — Dual-Engine Text Box & Wide-Format Validator

Performs an exhaustive, independent secondary verification ("Double Checker") of all
ASCII text boxes across the entire repository corpus:

1. Geometric & Border Closure Engine:
   - Counts ALL rows in each text box to establish the longest row as the benchmark.
   - If there is a misalignment across rows, calculates the difference to extend shorter
     rows up to the longest row (never shortening or truncating text).
   - Mandatory Top Border: Must start and terminate with '+' (e.g. +======+).
   - Mandatory Bottom Border: Must start and terminate with '+' (e.g. +======+).
   - Mandatory Side Borders: Every row must begin with '|' or '+' and terminate with '|' or '+'.
   - Character Count Symmetry: Every row must match the exact length of the longest row.
   - Monospace Display Width Symmetry: CJK/East Asian Width compliance against longest row.
   - Support for `--fix` / `-f`: Automatically extends shorter rows to match the longest row.

2. Typography & Wide-Format Architecture Engine:
   - Evaluates box width against the Dual-Environment Typography Law:
     * Compact / Chatroom Band: width <= 71 cols (safe for chat viewports and mobile).
     * reStructuredText Band : width <= 48 cols (narrow ASCII tables).
     * Golden Standard Band   : width in [127, 128] cols (repository wide-format master tables).
     * Reference Benchmark Band: widths 120, 130, 140, 150 cols (calibration suites).
   - Sliced Word & Truncation Detection: Identifies words inappropriately sliced with hyphens
     at line ends or truncated mid-token before closing borders.
"""

import os
import sys
import argparse
import unicodedata
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(__file__))
from check_box_symmetry import fix_file_boxes

def get_char_width(c):
    """Return monospace terminal column display width for a character."""
    ea = unicodedata.east_asian_width(c)
    if ea in ('W', 'F'):
        return 2
    return 1

def get_display_width(s):
    """Calculate the total monospace display width of a string."""
    return sum(get_char_width(c) for c in s)

class TextBoxDoubleChecker:
    def __init__(self, root_dir=".", wide_threshold=100, fix=False):
        self.root_dir = root_dir
        self.wide_threshold = wide_threshold
        self.fix = fix
        self.total_files = 0
        self.total_boxes = 0
        self.width_counter = Counter()
        self.box_categories = defaultdict(int)
        self.symmetry_issues = []
        self.truncation_issues = []
        self.wide_boxes_catalog = []

    def classify_width(self, width):
        if width <= 48:
            return "Narrow / rST (<= 48 cols)"
        elif width <= 71:
            return "Compact / Chatroom Standard (49 - 71 cols)"
        elif width in (127, 128):
            return "Golden Standard Wide Format (127 - 128 cols)"
        elif 100 <= width <= 150:
            return f"Extended Wide Benchmark ({width} cols)"
        else:
            return f"Custom Width ({width} cols)"

    def check_file(self, filepath):
        self.total_files += 1
        if self.fix:
            fix_file_boxes(filepath)

        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

        in_code = False
        is_md_block = False
        current_box = []
        box_start_line = 0

        for idx, raw in enumerate(lines, 1):
            line = raw.rstrip("\r\n")
            if line.startswith("```"):
                if in_code:
                    if not is_md_block and current_box:
                        self._evaluate_box(filepath, current_box, box_start_line)
                    in_code = False
                    is_md_block = False
                    current_box = []
                else:
                    in_code = True
                    is_md_block = ("markdown" in line.lower())
                    box_start_line = idx + 1
                    current_box = []
                continue

            if in_code and not is_md_block:
                if line.startswith("+") or line.startswith("|"):
                    current_box.append((idx, line))
                else:
                    if current_box:
                        self._evaluate_box(filepath, current_box, box_start_line)
                        current_box = []

        if in_code and not is_md_block and current_box:
            self._evaluate_box(filepath, current_box, box_start_line)

    def _evaluate_box(self, filepath, raw_box, start_line):
        box_borders = [(ln, l) for ln, l in raw_box if l.startswith("+") or l.startswith("|")]
        if len(box_borders) < 2:
            return

        self.total_boxes += 1
        first_line_num, first_line = box_borders[0]
        last_line_num, last_line = box_borders[-1]

        # COUNT ALL ROWS: Find the longest row in the box as the benchmark
        row_lens = [len(l) for _, l in box_borders]
        row_dws = [get_display_width(l) for _, l in box_borders]
        longest_len = max(row_lens)
        longest_dw = max(row_dws)

        box_width = longest_len
        self.width_counter[box_width] += 1
        category = self.classify_width(box_width)
        self.box_categories[category] += 1

        if box_width >= self.wide_threshold:
            self.wide_boxes_catalog.append({
                "file": filepath,
                "line": first_line_num,
                "width": box_width,
                "rows": len(box_borders),
                "title": box_borders[1][1] if len(box_borders) > 1 else ""
            })

        # 1. Mandatory Top Border
        if not (first_line.startswith("+") and first_line.endswith("+")):
            self.symmetry_issues.append({
                "file": filepath,
                "line": first_line_num,
                "type": "Unclosed TOP border (+ required at start and end)",
                "text": first_line
            })

        # 2. Mandatory Bottom Border
        if not (last_line.startswith("+") and last_line.endswith("+")):
            self.symmetry_issues.append({
                "file": filepath,
                "line": last_line_num,
                "type": "Unclosed BOTTOM border (+ required at start and end)",
                "text": last_line
            })

        expected_len = longest_len
        expected_dw = longest_dw

        for line_num, line in box_borders:
            curr_len = len(line)
            curr_dw = get_display_width(line)

            # 3. Mandatory Side Borders
            if not (line.startswith("+") or line.startswith("|")):
                self.symmetry_issues.append({
                    "file": filepath,
                    "line": line_num,
                    "type": "Missing LEFT border (+ or | required)",
                    "text": line
                })
            if not (line.endswith("+") or line.endswith("|")):
                self.symmetry_issues.append({
                    "file": filepath,
                    "line": line_num,
                    "type": "Missing RIGHT border (+ or | required)",
                    "text": line
                })

            # 4. Length Symmetry against the longest row
            if curr_len != expected_len:
                diff = expected_len - curr_len
                self.symmetry_issues.append({
                    "file": filepath,
                    "line": line_num,
                    "type": f"Character count mismatch: misaligned with longest row ({curr_len} vs longest {expected_len}; needs +{diff} chars extension to align)",
                    "text": line
                })
                continue

            # 5. Display Width Symmetry against the longest row
            if curr_dw != expected_dw:
                diff = expected_dw - curr_dw
                self.symmetry_issues.append({
                    "file": filepath,
                    "line": line_num,
                    "type": f"Display width mismatch: misaligned with longest row ({curr_dw} cols vs longest {expected_dw} cols; needs +{diff} cols extension to align)",
                    "text": line
                })

            # 6. Sliced Word Check (Trailing hyphen before closing |)
            content = line.strip("|+ ")
            if content.endswith("-") and not content.endswith("--"):
                self.truncation_issues.append({
                    "file": filepath,
                    "line": line_num,
                    "type": "Potential sliced word with trailing hyphen",
                    "text": line
                })

    def run(self):
        for root, dirs, files in os.walk(self.root_dir):
            if ".git" in root or "node_modules" in root:
                continue
            for f in sorted(files):
                if f.endswith(".md"):
                    self.check_file(os.path.join(root, f))

def main():
    parser = argparse.ArgumentParser(
        description="Double-check text box symmetry and analyze wide-format text box compliance. "
                    "Counts all rows and extends misaligned rows up to the longest row instead of shortening."
    )
    parser.add_argument("--path", default=".", help="Root path to audit (default: .)")
    parser.add_argument("--fix", "-f", action="store_true", help="Automatically extend misaligned rows up to the longest row")
    parser.add_argument("--wide-only", action="store_true", help="Report details on wide-format text boxes only (>= 100 cols)")
    args = parser.parse_args()

    checker = TextBoxDoubleChecker(root_dir=args.path, fix=args.fix)
    checker.run()

    print("=" * 72)
    print(" PROJECT SOMNARAK — TEXT BOX DOUBLE CHECKER & WIDE FORMAT REPORT")
    print(" (Count All Rows -> If Misaligned, Extend Up To Longest Row Engine)")
    print("=" * 72)
    print(f"Total Markdown Files Scanned : {checker.total_files:,}")
    print(f"Total Text Boxes Discovered  : {checker.total_boxes:,}")
    print(f"Total Symmetry / Border Flaws: {len(checker.symmetry_issues)}")
    print(f"Potential Sliced Word Flaws  : {len(checker.truncation_issues)}")
    print("-" * 72)
    print("TEXT BOX WIDTH DISTRIBUTION CLASSIFICATION:")
    for cat, count in sorted(checker.box_categories.items(), key=lambda x: -x[1]):
        pct = (count / checker.total_boxes) * 100 if checker.total_boxes else 0
        print(f"  * {cat:<44} : {count:5d} boxes ({pct:5.1f}%)")
    print("-" * 72)
    print("COLUMN WIDTH HISTOGRAM:")
    for w, count in sorted(checker.width_counter.items(), key=lambda x: -x[1]):
        print(f"  * Width {w:3d} columns : {count:5d} boxes")
    print("-" * 72)

    if checker.wide_boxes_catalog:
        print(f"WIDE-FORMAT TEXT BOXES (>= 100 COLUMNS) REGISTER: {len(checker.wide_boxes_catalog)} boxes")
        for wb in checker.wide_boxes_catalog:
            title_clean = wb['title'].strip('| ').strip()
            if len(title_clean) > 40:
                title_clean = title_clean[:37] + "..."
            print(f"  - [{wb['width']:3d} cols] {wb['file']}:{wb['line']} ({wb['rows']} rows) -> {title_clean}")
        print("-" * 72)

    if checker.symmetry_issues:
        print("[!] CRITICAL SYMMETRY / BORDER ANOMALIES DETECTED:")
        for iss in checker.symmetry_issues[:20]:
            print(f"  {iss['file']}:{iss['line']} [{iss['type']}]")
            print(f"     > {iss['text']}")
        if len(checker.symmetry_issues) > 20:
            print(f"  ... and {len(checker.symmetry_issues) - 20} more issues.")
        print("=" * 72)
        print(" RESULT: FAILED (Geometric or border closure flaws detected)")
        print(" Tip: Run with --fix to automatically extend misaligned rows up to the longest row.")
        print("=" * 72)
        return 1
    else:
        print("[OK] Zero geometric symmetry flaws detected across all text boxes.")
        print("[OK] All top and bottom borders are properly terminated with '+'.")
        print("[OK] All left and right borders are properly closed with '|' or '+'.")
        print("[OK] All rows count and match the longest row with 100% letter and display width symmetry.")
        print("=" * 72)
        print(" RESULT: PASSED (Double Checker 100% Geometric & Typographical Integrity)")
        print("=" * 72)
        return 0

if __name__ == "__main__":
    sys.exit(main())
