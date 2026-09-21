#!/usr/bin/env python3
"""
tools/check_box_symmetry.py — Automated Character & Display Width Symmetry Checker
Project Somnarak Non-Wiki Archive

Enforces strict geometric symmetry across all ASCII text boxes and tables in Markdown files:
1. Exact Letter/Character Count: Every row in a box must have identical string length (no row is 1 letter longer or shorter).
2. Exact Monospace Display Width: Every row must have identical visual width according to East Asian Width standards.
3. Strict Column Divider Alignment: All vertical separators (| and +) must align to the exact same column index across adjacent multi-column rows.
4. Outer Border Integrity: Every row must start and end with | or +.
"""

import os
import sys
import argparse
import unicodedata

def get_char_width(c):
    """Return monospace terminal column display width for a character."""
    ea = unicodedata.east_asian_width(c)
    if ea in ('W', 'F'):
        return 2
    return 1

def get_display_width(s):
    """Calculate the total monospace display width of a string."""
    return sum(get_char_width(c) for c in s)

def audit_file_symmetry(filepath):
    """Audit all ASCII text boxes in a single Markdown file for symmetry."""
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    in_code = False
    is_markdown_block = False
    current_box = []
    box_start_line = 0
    issues = []

    def evaluate_box(box, start_line):
        if len(box) < 2:
            return

        box_borders = [(line_num, line) for line_num, line in box if line.startswith("+") or line.startswith("|")]
        if len(box_borders) < 2:
            return

        first_line_num, first_line = box_borders[0]
        expected_len = len(first_line)
        expected_dw = get_display_width(first_line)

        prev_col_seps = None

        for line_num, line in box_borders:
            curr_len = len(line)
            curr_dw = get_display_width(line)

            # 1. Row Character Length Symmetry (no row is 1 letter longer or shorter)
            if curr_len != expected_len:
                diff = curr_len - expected_len
                sign = f"+{diff}" if diff > 0 else f"{diff}"
                issues.append({
                    "file": filepath,
                    "line": line_num,
                    "type": f"Row length mismatch ({sign} chars: {curr_len} vs expected {expected_len})",
                    "text": line
                })
                continue

            # 2. Display Width Symmetry (CJK / fullwidth character detection)
            if curr_dw != expected_dw:
                diff = curr_dw - expected_dw
                sign = f"+{diff}" if diff > 0 else f"{diff}"
                issues.append({
                    "file": filepath,
                    "line": line_num,
                    "type": f"Display width mismatch ({sign} cols: {curr_dw} vs expected {expected_dw})",
                    "text": line
                })

            # 3. Outer Border Integrity
            if not (line.startswith("+") or line.startswith("|")):
                issues.append({
                    "file": filepath,
                    "line": line_num,
                    "type": "Missing outer left border (+ or |)",
                    "text": line
                })
            if not (line.endswith("+") or line.endswith("|")):
                issues.append({
                    "file": filepath,
                    "line": line_num,
                    "type": "Missing outer right border (+ or |)",
                    "text": line
                })

            # 4. Interior Column Alignment between adjacent rows with same column count
            if line.startswith("|"):
                pipe_positions = [i for i, c in enumerate(line) if c == '|']
                if len(pipe_positions) > 2:
                    if prev_col_seps and len(prev_col_seps) == len(pipe_positions):
                        if pipe_positions != prev_col_seps:
                            issues.append({
                                "file": filepath,
                                "line": line_num,
                                "type": f"Interior column divider misalignment (found at {pipe_positions}, previous row at {prev_col_seps})",
                                "text": line
                            })
                    prev_col_seps = pipe_positions
                else:
                    prev_col_seps = None
            elif line.startswith("+"):
                plus_positions = [i for i, c in enumerate(line) if c == '+']
                if len(plus_positions) > 2:
                    prev_col_seps = plus_positions
                else:
                    prev_col_seps = None

    for idx, raw in enumerate(lines, 1):
        line = raw.rstrip("\r\n")
        if line.startswith("```"):
            if in_code:
                if not is_markdown_block:
                    evaluate_box(current_box, box_start_line)
                in_code = False
                is_markdown_block = False
                current_box = []
            else:
                in_code = True
                is_markdown_block = ("markdown" in line.lower())
                box_start_line = idx + 1
                current_box = []
            continue

        if in_code and not is_markdown_block:
            if line.startswith("+") or line.startswith("|"):
                current_box.append((idx, line))
            else:
                if current_box:
                    evaluate_box(current_box, box_start_line)
                    current_box = []

    if in_code and not is_markdown_block and current_box:
        evaluate_box(current_box, box_start_line)

    return issues

def scan_all_markdown_files(root_dir="."):
    """Scan all markdown files in root_dir and collect symmetry issues."""
    all_issues = []
    scanned_count = 0
    for root, dirs, files in os.walk(root_dir):
        if ".git" in root or "node_modules" in root:
            continue
        for f in sorted(files):
            if f.endswith(".md"):
                filepath = os.path.join(root, f)
                scanned_count += 1
                iss = audit_file_symmetry(filepath)
                all_issues.extend(iss)
    return scanned_count, all_issues

def main():
    parser = argparse.ArgumentParser(description="Check letter and display width symmetry in Markdown text boxes")
    parser.add_argument("--path", default=".", help="Root path to audit (default: repository root)")
    args = parser.parse_args()

    scanned_count, issues = scan_all_markdown_files(args.path)

    print("=" * 72)
    print(" PROJECT SOMNARAK — ASCII TEXT BOX SYMMETRY AUDITOR")
    print("=" * 72)
    print(f"Scanned Markdown Files : {scanned_count}")
    print(f"Total Symmetry Flaws   : {len(issues)}")
    print("-" * 72)

    if issues:
        print("[!] Crooked or asymmetrical text box rows detected:")
        for iss in issues:
            print(f"  {iss['file']}:{iss['line']} [{iss['type']}]")
            print(f"     > {iss['text']}")
        print("=" * 72)
        print(" RESULT: FAILED (Crooked borders detected)")
        print("=" * 72)
        return 1
    else:
        print("[OK] All text boxes have 100% symmetrical letter counts and display widths.")
        print("[OK] Zero crooked borders or misaligned column dividers detected.")
        print("=" * 72)
        print(" RESULT: PASSED (100% Geometric Symmetry)")
        print("=" * 72)
        return 0

if __name__ == "__main__":
    sys.exit(main())
