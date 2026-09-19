"""
Utility to generate and validate reStructuredText ASCII tables
conforming to Arena.ai Chatroom constraints:
- Enclosure: ALWAYS enclose inside fenced code block (``` ... ```)
- Unicode symbols for table borders: [No] (pure ASCII: +, -, |, =)
- reStructuredText syntax: [Yes]
- Character Limit Per ROW: <= 48 characters max.
"""

def make_box(lines, width=48):
    """
    Wraps text lines into a single-cell reStructuredText box
    with max row length of 48 characters.
    """
    inner_w = width - 2  # account for left and right border
    top_bot = "+" + "-" * inner_w + "+"
    
    out = [top_bot]
    for line in lines:
        if len(line) > inner_w:
            words = line.split()
            cur = ""
            for w in words:
                if len(cur) + len(w) + (1 if cur else 0) <= inner_w:
                    cur = (cur + " " + w) if cur else w
                else:
                    out.append("| " + cur.ljust(inner_w - 1) + "|")
                    cur = w
            if cur:
                out.append("| " + cur.ljust(inner_w - 1) + "|")
        else:
            out.append("| " + line.ljust(inner_w - 1) + "|")
    out.append(top_bot)
    return "\n".join(out)


def make_rst_table(headers, rows, col_widths=None, max_width=48):
    """
    Builds a multi-column reStructuredText ASCII grid table
    ensuring total row width <= max_width (default 48).
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
    
    table_lines = [sep_line]
    
    # Header
    hdr_cells = [" " + headers[i].ljust(col_widths[i] - 1) for i in range(num_cols)]
    table_lines.append("|" + "|".join(hdr_cells) + "|")
    table_lines.append(hdr_sep)
    
    # Rows
    for row in rows:
        row_cells = [" " + str(row[i]).ljust(col_widths[i] - 1) for i in range(num_cols)]
        table_lines.append("|" + "|".join(row_cells) + "|")
        table_lines.append(sep_line)
        
    for l in table_lines:
        assert len(l) <= max_width, f"Row exceeded limit ({len(l)} > {max_width}): {l}"
        
    return "\n".join(table_lines)


if __name__ == "__main__":
    b = make_box(["DIRECTIVE CONFIRMED", "Enclose inside code blocks", "Width: 48 chars max"], width=48)
    print("```")
    print(b)
    print("```")
    print("\nTable example (width 48):")
    t = make_rst_table(["Setting", "Rule"], [["Enclosure", "Code block (```)"], ["Borders", "ASCII only (+,-,|)"], ["Width", "48 chars max"]], col_widths=[14, 30], max_width=48)
    print("```")
    print(t)
    print("```")
