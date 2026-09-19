"""
Utility to generate and validate reStructuredText ASCII tables
conforming to Arena.ai Chatroom constraints:
- Unicode symbols for table borders: [No] (pure ASCII: +, -, |, =)
- reStructuredText syntax: [Yes]
- Character Limit Per ROW: <= 48 characters.
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
            # wrap line
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
        # compute widths to fit in max_width
        # border overhead: num_cols + 1 characters for '+' and '|'
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
    box = make_box(["M.A.W. TAXONOMY ARSENAL", "reStructuredText Standard", "Max width: 48 chars"])
    print(box)
    print("\nTable example:")
    tbl = make_rst_table(["Category", "Role"], [["MELEE", "Kinetic Reach"], ["RANGE", "Ballistic"], ["MIXED", "Hybrid"], ["UNIQUE", "Conceptual"]], [16, 29])
    print(tbl)
