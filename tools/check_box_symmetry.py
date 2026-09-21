#!/usr/bin/env python3
"""
tools/check_box_symmetry.py — Automated Character, Border & Display Width Symmetry Checker
Project Somnarak Non-Wiki Archive

Enforces strict geometric symmetry across all ASCII text boxes and tables in Markdown files:
1. Mandatory Top Border (Start): First row must start with '+' and end with '+' (e.g. +======+).
2. Mandatory Bottom Border (End): Last row must start with '+' and end with '+' (e.g. +======+).
3. Mandatory Side Borders (Left & Right): Every row must begin with '|' or '+' and terminate with '|' or '+'.
4. Exact Letter/Character Count: Every row in a box must match the exact width of the top/bottom borders (no row is 1 letter longer or shorter).
5. Exact Monospace Display Width: Every row must have identical visual width according to East Asian Width standards (CJK safe).
6. Middle rows/interior column layouts remain flexible for complex multi-row designs while maintaining outer boundary symmetry.
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
    """Audit all ASCII text boxes in a single Markdown file for symmetry, top/bottom borders, and side borders."""
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
        last_line_num, last_line = box_borders[-1]

        # 1. Mandatory Top Border (Start): Must start and end with '+'
        if not (first_line.startswith("+") and first_line.endswith("+")):
            issues.append({
                "file": filepath,
                "line": first_line_num,
                "type": "Missing or unclosed TOP border (start row must begin and terminate with '+')",
                "text": first_line
            })

        # 2. Mandatory Bottom Border (End): Must start and end with '+'
        if not (last_line.startswith("+") and last_line.endswith("+")):
            issues.append({
                "file": filepath,
                "line": last_line_num,
                "type": "Missing or unclosed BOTTOM border (end row must begin and terminate with '+')",
                "text": last_line
            })

        expected_len = len(first_line)
        expected_dw = get_display_width(first_line)

        for line_num, line in box_borders:
            curr_len = len(line)
            curr_dw = get_display_width(line)

            # 3. Mandatory Side Borders (Left & Right)
            if not (line.startswith("+") or line.startswith("|")):
                issues.append({
                    "file": filepath,
                    "line": line_num,
                    "type": "Missing LEFT side border (row must start with '+' or '|')",
                    "text": line
                })
            if not (line.endswith("+") or line.endswith("|")):
                issues.append({
                    "file": filepath,
                    "line": line_num,
                    "type": "Missing RIGHT side border (row must terminate with '+' or '|')",
                    "text": line
                })

            # 4. Row Character Length Symmetry (no row is 1 letter longer or shorter)
            if curr_len != expected_len:
                diff = curr_len - expected_len
                sign = f"+{diff}" if diff > 0 else f"{diff}"
                issues.append({
                    "file": filepath,
                    "line": line_num,
                    "type": f"Row length mismatch with box border ({sign} chars: {curr_len} vs {expected_len})",
                    "text": line
                })
                continue

            # 5. Display Width Symmetry (CJK / fullwidth character detection)
            if curr_dw != expected_dw:
                diff = curr_dw - expected_dw
                sign = f"+{diff}" if diff > 0 else f"{diff}"
                issues.append({
                    "file": filepath,
                    "line": line_num,
                    "type": f"Display width mismatch ({sign} cols: {curr_dw} vs {expected_dw})",
                    "text": line
                })

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
    """Scan all markdown files in root_dir and collect symmetry and border issues."""
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
    parser = argparse.ArgumentParser(description="Check letter symmetry, top/bottom borders, and side borders in Markdown text boxes")
    parser.add_argument("--path", default=".", help="Root path to audit (default: repository root)")
    args = parser.parse_args()

    scanned_count, issues = scan_all_markdown_files(args.path)

    print("=" * 72)
    print(" PROJECT SOMNARAK — ASCII TEXT BOX SYMMETRY & BORDER AUDITOR")
    print("=" * 72)
    print(f"Scanned Markdown Files : {scanned_count}")
    print(f"Total Symmetry Flaws   : {len(issues)}")
    print("-" * 72)

    if issues:
        print("[!] Crooked, unbordered, or asymmetrical text box rows detected:")
        for iss in issues:
            print(f"  {iss['file']}:{iss['line']} [{iss['type']}]")
            print(f"     > {iss['text']}")
        print("=" * 72)
        print(" RESULT: FAILED (Border or symmetry issues detected)")
        print("=" * 72)
        return 1
    else:
        print("[OK] All text boxes have mandatory '+' top (start) and bottom (end) borders.")
        print("[OK] All text boxes have mandatory '|' or '+' left and right side borders.")
        print("[OK] All text boxes have 100% symmetrical letter counts and display widths.")
        print("=" * 72)
        print(" RESULT: PASSED (100% Geometric Border & Character Symmetry)")
        print("=" * 72)
        return 0

if __name__ == "__main__":
    sys.exit(main())
