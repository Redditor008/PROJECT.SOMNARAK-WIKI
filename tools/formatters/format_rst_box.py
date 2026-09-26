"""
tools/formatters/format_rst_box.py
Utility to generate and validate reStructuredText ASCII tables (TablesGenerator reference)
conforming to Arena.ai Chatroom constraints and Project Somnarak standards:
- Enclosure: ALWAYS enclose inside fenced code block (``` ... ```)
- Unicode symbols for table borders: [No] (pure ASCII: +, -, |, =)
- reStructuredText syntax: [Yes] (TablesGenerator reference standard)
- Multi-line Cell Wrapping: When cell content exceeds column width,
  the row expands into multiple lines (rows) without truncating words (1 to 5 sub-rows).
"""

import sys
import os

# Ensure tools directory is in sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from box_formatter import make_box, make_table, make_kv_table


def make_rst_table(headers, rows, col_widths=None, max_width=48):
    """
    Builds a multi-column reStructuredText ASCII grid table
    ensuring total row width == max_width (default 48).
    When cell text exceeds column width, wraps into multiple lines.
    """
    return make_table(
        headers=headers,
        rows=rows,
        col_widths=col_widths,
        width=max_width,
        style="rst"
    )


if __name__ == "__main__":
    b = make_box(["DIRECTIVE CONFIRMED", "Enclose inside code blocks", "Width: 48 chars max with automatic word wrapping"], width=48)
    print("```text")
    print(b)
    print("```")
    print("\nTable example (width 48):")
    t = make_rst_table(
        ["Setting", "Specification"],
        [
            ["Borders", "Pure ASCII (+, -, |, =)"],
            ["Limit", "Exactly 48 Characters Max with multi-line wrapping"],
            ["Syntax", "reStructuredText [Yes]"]
        ],
        col_widths=[15, 30],
        max_width=48
    )
    print("```text")
    print(t)
    print("```")
    print("\nTable example (width 74 chatroom standard):")
    t74 = make_table(
        headers=["STANDARD COMPONENT", "OPERATIONAL EXECUTION DETAIL"],
        rows=[
            ["TablesGenerator Grid", "Pure ASCII reStructuredText grid (+-+|) matching https://www.tablesgenerator.com/text_tables."],
            ["Zero Crooked Rows", "Rigid monospace column boundaries guaranteed across 100% of generated lines."]
        ],
        width=74
    )
    print("```text")
    print(t74)
    print("```")
