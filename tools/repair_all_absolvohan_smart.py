#!/usr/bin/env python3
"""
tools/repair_all_absolvohan_smart.py
Smart repair of all boxes in The Absolvohan Parts 2 through 8 using box_formatter:
- Resolves all truncated brackets and parentheses.
- Wraps long lines cleanly using _process_row into 67-character inner rows.
- Replaces divider lines with canonical +---------------+ separators.
- Enforces strict 71-character symmetry and zero unclosed delimiters.
"""

import sys, os, re
sys.path.append(os.path.dirname(__file__))
from box_formatter import _process_row
from complete_absolvohan_repairs import BRACKET_MAP, PAREN_MAP

def clean_row_content(inner):
    inner = inner.rstrip('|').strip()

    # Apply mappings
    for k, v in BRACKET_MAP.items():
        if inner.endswith(k):
            inner = inner[:-len(k)] + v
            break

    for k, v in PAREN_MAP.items():
        if inner.endswith(k):
            inner = inner[:-len(k)] + v
            break

    # If unclosed bracket, close it if reasonable
    if inner.count('[') > inner.count(']'):
        m = re.search(r'\[([A-Za-z0-9% -]+)$', inner)
        if m:
            inner += ']'

    # If unclosed paren, close it if reasonable
    if inner.count('(') > inner.count(')'):
        m = re.search(r'\(([^)]+)$', inner)
        if m:
            inner += ')'

    return inner

def repair_box(box_lines, width=71):
    # box_lines include the opening +===...===+ and closing +===...===+
    # We want to re-format the box cleanly
    out = []
    max_len = width - 4 # 67

    for line in box_lines:
        s = line.rstrip()
        # Top or bottom or section divider
        if s.startswith("+") and s.endswith("+"):
            # Check if double border
            if "=" in s:
                out.append("+" + "=" * (width - 2) + "+\n")
            else:
                out.append("+" + "-" * (width - 2) + "+\n")
            continue

        if s.startswith("|") and s.endswith("|"):
            inner = s[1:-1].strip()

            # Check if internal divider
            if set(inner).issubset(set("-+ ")):
                out.append("+" + "-" * (width - 2) + "+\n")
                continue

            # Stage grid special row
            if "[N01]" in inner and ("[N10]" in inner or "[N0" in inner):
                out.append("|     [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]     |\n")
                continue

            # Unit tokens row (e.g. [SPORE-A][KIM]...)
            if inner.startswith("[") and not inner.startswith("[STAGE") and "][" in inner or (inner.startswith("[") and inner.endswith("]") and not inner.startswith("- ")):
                # If unit tokens row
                clean_tokens = clean_row_content(inner)
                token_rows = _process_row(clean_tokens, max_len)
                for tr in token_rows:
                    out.append(f"| {tr.ljust(max_len)} |\n")
                continue

            # Regular content row
            cleaned = clean_row_content(inner)
            processed_rows = _process_row(cleaned, max_len)
            for pr in processed_rows:
                out.append(f"| {pr.ljust(max_len)} |\n")
            continue

        # If somehow line inside box didn't match border
        out.append(line)

    return out

def repair_file(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    i = 0
    modified = False

    while i < len(lines):
        line = lines[i]
        s = line.rstrip()

        # Check for start of text box inside ```text
        if s.startswith("+") and (s.endswith("+") or s.endswith("+`")) and ("=" in s or "-" in s):
            # Gather all box lines
            box_lines = [line]
            j = i + 1
            while j < len(lines):
                box_lines.append(lines[j])
                js = lines[j].rstrip()
                if js.startswith("+") and js.endswith("+") and ("=" in js or "-" in js):
                    # Check if this is the end of the box
                    # Usually followed by ``` or empty line
                    if j + 1 < len(lines) and lines[j+1].startswith("```"):
                        break
                    # Or if next line is not starting with |
                    if j + 1 < len(lines) and not lines[j+1].startswith("|"):
                        break
                j += 1
            
            repaired_box = repair_box(box_lines)
            new_lines.extend(repaired_box)
            i = j + 1
            modified = True
            continue

        new_lines.append(line)
        i += 1

    with open(path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print(f"Smart repaired: {path}")

def main():
    parts = [
        "SOMNARAK-WORLD/The_Absolvohan/Part_2_Days_1_to_25.md",
        "SOMNARAK-WORLD/The_Absolvohan/Part_3_Days_29_to_49.md",
        "SOMNARAK-WORLD/The_Absolvohan/Part_4_Days_53_to_73.md",
        "SOMNARAK-WORLD/The_Absolvohan/Part_5_Days_77_to_97.md",
        "SOMNARAK-WORLD/The_Absolvohan/Part_6_Days_101_to_121.md",
        "SOMNARAK-WORLD/The_Absolvohan/Part_7_Days_125_to_145.md",
        "SOMNARAK-WORLD/The_Absolvohan/Part_8_Days_149_to_177.md",
    ]
    for p in parts:
        repair_file(p)

if __name__ == "__main__":
    main()
