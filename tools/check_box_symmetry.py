#!/usr/bin/env python3
"""
tools/check_box_symmetry.py — Automated Character, Border & Display Width Symmetry Checker
Project Somnarak Non-Wiki Archive

Enforces strict geometric symmetry across all ASCII text boxes and tables in Markdown files:
1. Counts ALL rows in every text box to find the longest row (maximum length and display width).
2. If there is a misalignment across rows, the tool calculates the missing length and adds it up
   to the longer row: extending shorter rows with padding spaces or border fill rather than shortening
   or truncating long text.
3. Mandatory Top Border (Start): First row must start with '+' and end with '+' (e.g. +======+).
4. Mandatory Bottom Border (End): Last row must start with '+' and end with '+' (e.g. +======+).
5. Mandatory Side Borders (Left & Right): Every row must begin with '|' or '+' and terminate with '|' or '+'.
6. Exact Character Count & Display Width: All rows must match the longest row in the box.
7. Support for `--fix` / `-f`: Automatically extends all shorter rows to match the longest row in-place.
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

def fix_box_extend_to_longest(box_lines):
    """
    Extends all rows in a text box to align with the longest row.
    Counts all rows, finds the maximum length and display width, and extends
    shorter rows up to that maximum. Never shortens or slices text.
    """
    border_lines = [l for l in box_lines if l.startswith("+") or l.startswith("|")]
    if len(border_lines) < 2:
        return box_lines

    # 1. Count all rows and find the longest row
    longest_dw = max(get_display_width(l) for l in border_lines)
    longest_len = max(len(l) for l in border_lines)
    target_dw = max(longest_dw, longest_len)

    fixed = []

    # Check if first line is missing a proper top border
    first_b = border_lines[0]
    if not (first_b.startswith("+") and first_b.endswith("+")):
        top_border = "+" + "=" * (target_dw - 2) + "+"
        fixed.append(top_border)

    for line in box_lines:
        if not (line.startswith("+") or line.startswith("|")):
            fixed.append(line)
            continue

        cur_dw = get_display_width(line)
        if line.startswith("+"):
            fill = "=" if "=" in line else "-"
            if line.endswith("+"):
                if cur_dw < target_dw:
                    diff = target_dw - cur_dw
                    line = line[:-1] + (fill * diff) + "+"
            else:
                diff = target_dw - cur_dw - 1
                diff = max(diff, 0)
                line = line + (fill * diff) + "+"
        elif line.startswith("|"):
            if line.endswith("|"):
                if cur_dw < target_dw:
                    diff = target_dw - cur_dw
                    line = line[:-1] + (" " * diff) + "|"
            else:
                diff = target_dw - cur_dw - 1
                diff = max(diff, 0)
                line = line + (" " * diff) + "|"
        fixed.append(line)

    # Check if last line is missing a proper bottom border
    last_b = border_lines[-1]
    if not (last_b.startswith("+") and last_b.endswith("+")):
        bot_border = "+" + "=" * (target_dw - 2) + "+"
        fixed.append(bot_border)

    return fixed

def fix_file_boxes(filepath):
    """
    Scans a markdown file and extends any misaligned text box rows to match
    the longest row in that box. Returns True if the file was modified.
    """
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    out_lines = []
    in_code = False
    is_markdown_block = False
    current_box = []
    modified = False

    def flush_box():
        nonlocal current_box, modified
        if not current_box:
            return
        if len(current_box) >= 2:
            fixed_box = fix_box_extend_to_longest(current_box)
            if fixed_box != current_box:
                modified = True
            for fl in fixed_box:
                out_lines.append(fl + "\n")
        else:
            for bl in current_box:
                out_lines.append(bl + "\n")
        current_box = []

    for raw in lines:
        line = raw.rstrip("\r\n")
        if line.startswith("```"):
            if in_code:
                if not is_markdown_block:
                    flush_box()
                in_code = False
                is_markdown_block = False
                out_lines.append(raw)
            else:
                in_code = True
                is_markdown_block = ("markdown" in line.lower())
                out_lines.append(raw)
            continue

        if in_code and not is_markdown_block:
            if line.startswith("+") or line.startswith("|"):
                current_box.append(line)
            else:
                if current_box:
                    flush_box()
                out_lines.append(raw)
        else:
            out_lines.append(raw)

    if in_code and not is_markdown_block and current_box:
        flush_box()

    if modified:
        with open(filepath, "w", encoding="utf-8") as f:
            f.writelines(out_lines)
    return modified

def audit_file_symmetry(filepath, fix=False):
    """
    Audit all ASCII text boxes in a single Markdown file for symmetry, top/bottom borders,
    and side borders. Counts all rows and benchmarks against the longest row.
    If fix=True, extends shorter rows up to the longest row before auditing.
    """
    if fix:
        fix_file_boxes(filepath)

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

        # COUNT ALL ROWS: Find the longest row in the box as the benchmark
        row_lens = [len(line) for _, line in box_borders]
        row_dws = [get_display_width(line) for _, line in box_borders]
        longest_len = max(row_lens)
        longest_dw = max(row_dws)

        expected_len = longest_len
        expected_dw = longest_dw

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

            # 4. Row Character Length Symmetry (count all rows, identify missing length to extend to longest)
            if curr_len != expected_len:
                diff = expected_len - curr_len
                issues.append({
                    "file": filepath,
                    "line": line_num,
                    "type": f"Row length mismatch: misaligned with longest row ({curr_len} vs longest {expected_len}; needs +{diff} chars extension to align)",
                    "text": line
                })
                continue

            # 5. Display Width Symmetry (CJK / fullwidth character detection)
            if curr_dw != expected_dw:
                diff = expected_dw - curr_dw
                issues.append({
                    "file": filepath,
                    "line": line_num,
                    "type": f"Display width mismatch: misaligned with longest row ({curr_dw} cols vs longest {expected_dw} cols; needs +{diff} cols extension to align)",
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

def scan_all_markdown_files(root_dir=".", fix=False):
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
                iss = audit_file_symmetry(filepath, fix=fix)
                all_issues.extend(iss)
    return scanned_count, all_issues

def main():
    parser = argparse.ArgumentParser(
        description="Check letter symmetry, top/bottom borders, and side borders in Markdown text boxes. "
                    "Counts all rows and extends misaligned rows up to the longest row instead of shortening."
    )
    parser.add_argument("--path", default=".", help="Root path to audit (default: repository root)")
    parser.add_argument("--file", help="Audit and optionally fix a single markdown file")
    parser.add_argument("--fix", "-f", action="store_true", help="Automatically extend misaligned rows up to the longest row")
    args = parser.parse_args()

    print("=" * 72)
    print(" PROJECT SOMNARAK — ASCII TEXT BOX SYMMETRY & BORDER AUDITOR")
    print(" (Count All Rows -> If Misaligned, Extend Up To Longest Row Engine)")
    print("=" * 72)

    if args.file:
        if not os.path.isfile(args.file):
            print(f"[ERROR] File not found: {args.file}")
            return 1
        issues = audit_file_symmetry(args.file, fix=args.fix)
        print(f"Audited File         : {args.file}")
        print(f"Total Symmetry Flaws : {len(issues)}")
        print("-" * 72)
        if issues:
            print("[!] Misaligned rows detected:")
            for iss in issues:
                print(f"  Line {iss['line']} [{iss['type']}]")
                print(f"     > {iss['text']}")
            print("=" * 72)
            print(" RESULT: FAILED (Misalignments detected)")
            print("=" * 72)
            return 1
        else:
            print("[OK] All text boxes have mandatory '+' top (start) and bottom (end) borders.")
            print("[OK] All text boxes have mandatory '|' or '+' left and right side borders.")
            print("[OK] All rows count and match the longest row with 100% letter and display width symmetry.")
            print("=" * 72)
            print(" RESULT: PASSED (100% Geometric Border & Character Symmetry)")
            print("=" * 72)
            return 0

    scanned_count, issues = scan_all_markdown_files(args.path, fix=args.fix)

    print(f"Scanned Markdown Files : {scanned_count}")
    print(f"Total Symmetry Flaws   : {len(issues)}")
    print("-" * 72)

    if issues:
        print("[!] Crooked, unbordered, or asymmetrical text box rows detected:")
        for iss in issues[:25]:
            print(f"  {iss['file']}:{iss['line']} [{iss['type']}]")
            print(f"     > {iss['text']}")
        if len(issues) > 25:
            print(f"  ... and {len(issues) - 25} more misalignments.")
        print("=" * 72)
        print(" RESULT: FAILED (Border or symmetry issues detected)")
        print(" Tip: Run with --fix to automatically extend misaligned rows up to the longest row.")
        print("=" * 72)
        return 1
    else:
        print("[OK] All text boxes have mandatory '+' top (start) and bottom (end) borders.")
        print("[OK] All text boxes have mandatory '|' or '+' left and right side borders.")
        print("[OK] All rows count and match the longest row with 100% letter and display width symmetry.")
        print("=" * 72)
        print(" RESULT: PASSED (100% Geometric Border & Character Symmetry)")
        print("=" * 72)
        return 0

if __name__ == "__main__":
    sys.exit(main())
