"""
Utility to generate and validate reStructuredText ASCII tables
conforming to Arena.ai Chatroom constraints:
- Enclosure: ALWAYS enclose inside fenced code block (``` ... ```)
- Unicode symbols for table borders: [No] (pure ASCII: +, -, |, =)
- reStructuredText syntax: [Yes]
- Character Limit Per ROW: <= 48 characters max.
- Multi-line Cell Wrapping: When cell content exceeds column width,
  the row expands into multiple lines (rows) without truncating words.
"""

import textwrap

def make_box(lines, width=48):
    """
    Wraps text lines into a single-cell reStructuredText box
    with max row length of 48 characters.
    """
    inner_w = width - 4  # account for left border '| ', right border ' |'
    top_bot = "+" + "=" * (width - 2) + "+"
    
    out = [top_bot]
    for line in lines:
        wrapped = textwrap.wrap(str(line), width=inner_w)
        if not wrapped:
            wrapped = [""]
        for w in wrapped:
            out.append("| " + w.ljust(inner_w) + " |")
    out.append(top_bot)
    return "\n".join(out)


def make_rst_table(headers, rows, col_widths=None, max_width=48):
    """
    Builds a multi-column reStructuredText ASCII grid table
    ensuring total row width == max_width (default 48).
    When cell text exceeds column width, wraps into multiple lines.
    """
    num_cols = len(headers)
    if col_widths is None:
        overhead = num_cols + 1
        available = max_width - overhead
        each = available // num_cols
        col_widths = [each] * num_cols
        col_widths[-1] += available - (each * num_cols)
        
    sep_line = "+" + "+".join("-" * w for w in col_widths) + "+"
    hdr_sep = "+" + "+".join("=" * w for w in col_widths) + "+"
    
    def format_row(cells):
        wrapped = []
        for text, w in zip(cells, col_widths):
            inner_w = w - 2
            lines = textwrap.wrap(str(text), width=inner_w)
            if not lines:
                lines = [""]
            wrapped.append(lines)
        max_lines = max(len(c) for c in wrapped)
        out = []
        for line_idx in range(max_lines):
            row_str = "|"
            for col_idx, w in enumerate(col_widths):
                lines = wrapped[col_idx]
                cell_text = lines[line_idx] if line_idx < len(lines) else ""
                row_str += " " + cell_text.ljust(w - 2) + " |"
            out.append(row_str)
        return out

    table_lines = [sep_line]
    table_lines.extend(format_row(headers))
    table_lines.append(hdr_sep)
    for r in rows:
        table_lines.extend(format_row(r))
        table_lines.append(sep_line)
        
    for l in table_lines:
        assert len(l) == max_width, f"Row width error ({len(l)} != {max_width}): {l}"
        
    return "\n".join(table_lines)


if __name__ == "__main__":
    b = make_box(["DIRECTIVE CONFIRMED", "Enclose inside code blocks", "Width: 48 chars max with automatic word wrapping"], width=48)
    print("```text")
    print(b)
    print("```")
    print("\nTable example (width 48):")
    t = make_rst_table(["Setting", "Specification"], [["Borders", "Pure ASCII (+, -, |, =)"], ["Limit", "Exactly 48 Characters Max with multi-line wrapping"], ["Syntax", "reStructuredText [Yes]"]], col_widths=[15, 30], max_width=48)
    print("```text")
    print(t)
    print("```")
