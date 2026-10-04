#!/usr/bin/env python3
"""
tools/box_formatter.py — Canonical Text Box & Grid Table Generator (TablesGenerator Reference)
Project Somnarak Non-Wiki Archive

Reference Standard: https://www.tablesgenerator.com/text_tables
Adheres strictly to Project Somnarak and Arena.ai Chatroom standards:
1. TablesGenerator Reference Architecture:
   - Pure standard ASCII borders (+, -, |, =). Zero Unicode box drawing glitches.
   - reStructuredText & Plain Text Grid Table syntax.
   - Rigid monospace vertical column alignment: outer borders at col 0 and (width - 1),
     internal column dividers (|) 100% straight and unyielding from top to bottom.
2. The 5-Row Vertical Growth Rule (User Directive):
   - A single logical entry / table cell expands vertically up to 5 visual sub-rows.
   - Zero word truncation: wrap text cleanly at word boundaries.
   - If an unbroken token exceeds column width, split safely without breaking borders.
   - Cap cell growth at 5 visual sub-rows maximum to prevent visual clutter.
3. Arena.ai Chatroom Standard (Width: EXACTLY 74 COLUMNS):
   - Total width: 74 columns (+ + 72 =/- + +).
   - Inner content width (single box): 70 columns (| + space + 68 chars + space + |).
   - Inner column widths (2-col table): 24 chars (Slot 26) + 43 chars (Slot 45) -> 74 cols.
   - Strict runtime assertion on EVERY generated line: guaranteed 100% geometric symmetry.
4. Wide-Format & Custom Width Support:
   - Configurable width: 74 (chatroom), 71 (compact), 127/128 (repository wide format).
"""

import re
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

def pad_cell_display_width(s, inner_w, align="left"):
    """
    Pad string s with spaces to match exact monospace display width inner_w.
    Supports 'left', 'center', and 'right' alignment.
    Safe against overflowing strings by cleanly trimming if needed.
    """
    cur_dw = get_display_width(s)
    if cur_dw == inner_w:
        return s
    diff = inner_w - cur_dw
    if diff < 0:
        # String exceeds inner_w, safe trim
        trimmed = ""
        for c in s:
            if get_display_width(trimmed) + get_char_width(c) <= inner_w:
                trimmed += c
            else:
                break
        diff = inner_w - get_display_width(trimmed)
        return trimmed + (" " * diff)
    
    if align == "right":
        return (" " * diff) + s
    elif align == "center":
        left = diff // 2
        right = diff - left
        return (" " * left) + s + (" " * right)
    else:  # left
        return s + (" " * diff)

def pad_to_exact_width(s, target_dw, align="left"):
    """Backwards-compatible alias for pad_cell_display_width."""
    return pad_cell_display_width(s, target_dw, align=align)

def wrap_cell_text(text, inner_w, max_subrows=5):
    """
    Wrap text to fit within inner_w display width adhering to the 5-Row Vertical Growth Rule.
    - Zero word truncation: splits at natural word boundaries.
    - Breaks unbroken tokens exceeding inner_w into chunks that fit inner_w.
    - Capped at max_subrows visual lines (default: 5).
    """
    if not text:
        return [""]
    raw_lines = str(text).split("\n")
    all_wrapped = []
    for r in raw_lines:
        r_str = r.strip()
        if not r_str:
            all_wrapped.append("")
            continue
        words = r_str.split()
        if not words:
            all_wrapped.append("")
            continue
        cur = ""
        for w in words:
            w_dw = get_display_width(w)
            if w_dw > inner_w:
                if cur:
                    all_wrapped.append(cur)
                    cur = ""
                # Break long unbroken token into chunks of display width inner_w
                chunk = ""
                for char in w:
                    if get_display_width(chunk) + get_char_width(char) <= inner_w:
                        chunk += char
                    else:
                        all_wrapped.append(chunk)
                        chunk = char
                if chunk:
                    cur = chunk
            elif not cur:
                cur = w
            elif get_display_width(cur) + 1 + w_dw <= inner_w:
                cur += " " + w
            else:
                all_wrapped.append(cur)
                cur = w
        if cur:
            all_wrapped.append(cur)

    if max_subrows is not None and len(all_wrapped) > max_subrows:
        all_wrapped = all_wrapped[:max_subrows]

    return all_wrapped if all_wrapped else [""]

def wrap_text_display_width(text, max_dw, indent=""):
    """Backwards-compatible text wrapper returning lines indented if specified."""
    wrapped = wrap_cell_text(text, max_dw - len(indent))
    if not indent:
        return wrapped
    return [indent + line if idx > 0 else line for idx, line in enumerate(wrapped)]

def _process_row(r, max_len):
    """Backwards-compatible row processor for legacy scripts."""
    r_strip = r.strip()
    if r_strip == "---":
        return ["---"]
    if r_strip.startswith("==="):
        return ["==="]
    if get_display_width(r) <= max_len:
        return [r]
    # Unit diagram token line e.g. [N1] [N2]
    if r_strip.startswith("[") and not r_strip.startswith("- ") and re.match(r"^(\s*\[[^\]]+\])+\s*$", r_strip):
        parts = re.findall(r"\s*\[[^\]]+\]", r)
        if parts:
            lines = []
            cur = ""
            for p in parts:
                p_clean = p.strip()
                if not cur:
                    cur = p_clean
                elif get_display_width(cur) + 1 + get_display_width(p_clean) <= max_len:
                    cur += " " + p_clean
                else:
                    lines.append(cur)
                    cur = p_clean
            if cur:
                lines.append(cur)
            return lines if lines else [r[:max_len]]
    return wrap_cell_text(r, max_len, max_subrows=5)

def compute_col_widths(num_cols, total_width=74, ratios=None):
    """
    Computes slot widths for each column such that:
      sum(col_widths) + len(col_widths) + 1 == total_width
    Each slot width includes the inner text width plus 2 surrounding spaces.
    """
    overhead = num_cols + 1
    available = total_width - overhead
    if available < num_cols * 3:
        raise ValueError(f"Total width {total_width} is too small for {num_cols} columns")

    if num_cols == 1:
        return [available]

    if num_cols == 2 and ratios is None:
        # Standard Key-Value 2-column ratio: Slot 26 (inner 24) + Slot 45 (inner 43) -> 74
        if total_width == 74:
            return [26, 45]
        w0 = max(15, (available * 35) // 100)
        w1 = available - w0
        return [w0, w1]

    if ratios is None:
        base = available // num_cols
        rem = available % num_cols
        widths = [base] * num_cols
        widths[-1] += rem
        return widths
    else:
        total_ratio = sum(ratios)
        widths = [int(available * (r / total_ratio)) for r in ratios]
        diff = available - sum(widths)
        widths[-1] += diff
        return widths

def make_table(headers=None, rows=None, title=None, col_widths=None, width=74,
               alignments=None, style="rst", max_subrows=5):
    """
    Generates an ASCII grid table following the TablesGenerator reference standard.
    (https://www.tablesgenerator.com/text_tables)

    Parameters:
    - headers: Optional list of header strings.
    - rows: List of rows, where each row is a list/tuple of cell strings, or pipe-separated string.
    - title: Optional spanning header title at the top of the table.
    - col_widths: Explicit slot widths for columns, or None for automatic calculation.
    - width: Exact total table width in characters (default: 74 for Arena chatroom).
    - alignments: Column text alignment ('left', 'center', 'right', or per-column list).
    - style: 'rst' (reStructuredText grid with +---+ and +===+) or 'boxed'.
    - max_subrows: Maximum visual sub-rows per logical entry (default: 5 per user directive).

    Returns:
    - Symmetrical ASCII grid table string where every line has len == width.
    """
    rows = rows or []
    parsed_rows = []
    for r in rows:
        if isinstance(r, (list, tuple)):
            parsed_rows.append([str(c) for c in r])
        elif isinstance(r, str):
            if " | " in r:
                parsed_rows.append([c.strip() for c in r.split(" | ")])
            else:
                parsed_rows.append([r])
        else:
            parsed_rows.append([str(r)])

    num_cols = 1
    if headers:
        num_cols = max(num_cols, len(headers))
    if parsed_rows:
        num_cols = max(num_cols, max(len(r) for r in parsed_rows))

    norm_rows = []
    for r in parsed_rows:
        if len(r) < num_cols:
            norm_rows.append(r + [""] * (num_cols - len(r)))
        else:
            norm_rows.append(r[:num_cols])

    if col_widths is None:
        col_widths = compute_col_widths(num_cols, total_width=width)
    else:
        expected_total = sum(col_widths) + len(col_widths) + 1
        assert expected_total == width, \
            f"Provided col_widths {col_widths} sum + overhead ({expected_total}) != width ({width})"

    inner_widths = [cw - 2 for cw in col_widths]

    if alignments is None:
        alignments = ["left"] * num_cols
    elif isinstance(alignments, str):
        alignments = [alignments] * num_cols
    elif len(alignments) < num_cols:
        alignments = list(alignments) + ["left"] * (num_cols - len(alignments))

    def make_col_border(sep_char="-"):
        return "+" + "+".join(sep_char * cw for cw in col_widths) + "+"

    table_lines = []

    if title:
        t_char = "=" if style == "boxed" else "-"
        table_lines.append("+" + t_char * (width - 2) + "+")
        t_padded = pad_cell_display_width(title.strip(), width - 4, align="center")
        table_lines.append(f"| {t_padded} |")
        if headers:
            table_lines.append(make_col_border("="))
        else:
            table_lines.append(make_col_border("-"))
    else:
        top_char = "=" if style == "boxed" else "-"
        table_lines.append(make_col_border(top_char))

    if headers:
        wrapped_headers = [wrap_cell_text(h, iw, max_subrows=max_subrows) for h, iw in zip(headers, inner_widths)]
        h_height = max(len(wh) for wh in wrapped_headers)
        for sub_idx in range(h_height):
            line_parts = []
            for col_idx, (wh, iw, align) in enumerate(zip(wrapped_headers, inner_widths, alignments)):
                cell_text = wh[sub_idx] if sub_idx < len(wh) else ""
                padded = pad_cell_display_width(cell_text, iw, align)
                line_parts.append(f" {padded} ")
            table_lines.append("|" + "|".join(line_parts) + "|")
        table_lines.append(make_col_border("="))

    for r_idx, r in enumerate(norm_rows):
        wrapped_cells = [wrap_cell_text(cell, iw, max_subrows=max_subrows) for cell, iw in zip(r, inner_widths)]
        r_height = max(len(wc) for wc in wrapped_cells)
        for sub_idx in range(r_height):
            line_parts = []
            for col_idx, (wc, iw, align) in enumerate(zip(wrapped_cells, inner_widths, alignments)):
                cell_text = wc[sub_idx] if sub_idx < len(wc) else ""
                padded = pad_cell_display_width(cell_text, iw, align)
                line_parts.append(f" {padded} ")
            table_lines.append("|" + "|".join(line_parts) + "|")
        table_lines.append(make_col_border("-" if (r_idx < len(norm_rows) - 1 or style != "boxed") else "="))

    # Bulletproof validation: every single line must match width exactly
    for idx, l in enumerate(table_lines, 1):
        assert len(l) == width, f"Row {idx} length {len(l)} != {width}: {l}"
        assert get_display_width(l) == width, f"Row {idx} display width {get_display_width(l)} != {width}: {l}"

    return "\n".join(table_lines)

def make_kv_table(pairs, col_widths=None, width=74, title=None, headers=None,
                  alignments=None, style="rst", max_subrows=5):
    """
    Dedicated helper to generate a 2-column key-value status table.
    Default slot widths for width 74: [26, 45] (inner 24 and 43).
    """
    return make_table(
        headers=headers,
        rows=pairs,
        title=title,
        col_widths=col_widths,
        width=width,
        alignments=alignments,
        style=style,
        max_subrows=max_subrows
    )

def make_box(title, raw_rows=None, width=74, max_width=None, max_subrows=5):
    """
    Builds a single-column symmetrical ASCII text box (HUD card / announcement).
    - Default width: 74 columns (Arena.ai chatroom standard).
    - Automatically wraps long lines into visual sub-rows (1 to 5 rows).
    - Capped at max_subrows (default: 5) per user directive.
    - Strict validation: every line is verified to match width exactly.
    """
    if isinstance(title, (list, tuple)):
        raw_rows = title
        title = ""
    raw_rows = raw_rows or []

    if max_width is not None and width > max_width:
        width = max_width

    slot_w = width - 2
    inner_w = slot_w - 2  # width - 4

    top = "+" + "=" * slot_w + "+"
    bottom = "+" + "=" * slot_w + "+"
    sep = "+" + "-" * slot_w + "+"

    out = [top]
    if title:
        t_clean = f" {title.strip()} "
        cur_t_dw = get_display_width(t_clean)
        if cur_t_dw > slot_w:
            t_clean = t_clean[:slot_w]
            cur_t_dw = get_display_width(t_clean)
        diff = slot_w - cur_t_dw
        left_pad = max(diff // 2, 0)
        right_pad = max(diff - left_pad, 0)
        out.append("|" + (" " * left_pad) + t_clean + (" " * right_pad) + "|")
        out.append(sep)

    for r in raw_rows:
        if isinstance(r, str):
            r_strip = r.strip()
            if r_strip == "---":
                out.append(sep)
                continue
            elif r_strip.startswith("==="):
                out.append(top)
                continue
            wrapped = wrap_cell_text(r, inner_w, max_subrows=max_subrows)
            for sub in wrapped:
                padded = pad_cell_display_width(sub, inner_w, align="left")
                out.append(f"| {padded} |")
        elif isinstance(r, (list, tuple)):
            for sub_r in r:
                wrapped = wrap_cell_text(str(sub_r), inner_w, max_subrows=max_subrows)
                for sub in wrapped:
                    padded = pad_cell_display_width(sub, inner_w, align="left")
                    out.append(f"| {padded} |")

    out.append(bottom)

    # Bulletproof check: every single row must equal width
    for idx, l in enumerate(out, 1):
        assert len(l) == width, f"Row {idx} length {len(l)} != {width}: {l}"
        assert get_display_width(l) == width, f"Row {idx} display width {get_display_width(l)} != {width}: {l}"

    return "\n".join(out)

def make_borderless_banner(title, rows=None, width=74):
    """
    Builds a borderless ASCII banner or divider.
    Defaults to width=74 characters.
    """
    top = "=" * width
    bottom = "=" * width
    sep = "-" * width
    out = [top]
    if title:
        t_clean = f" {title.strip()} "
        cur_dw = get_display_width(t_clean)
        if cur_dw > width:
            t_clean = t_clean[:width]
            cur_dw = get_display_width(t_clean)
        diff = max(width - cur_dw, 0)
        left = diff // 2
        right = diff - left
        out.append((" " * left) + t_clean + (" " * right))
        out.append(top)
    if rows:
        for r in rows:
            if r == "---":
                out.append(sep)
            elif r == "===":
                out.append(top)
            else:
                cur_dw = get_display_width(r)
                if cur_dw <= width:
                    out.append(pad_cell_display_width(r, width, align="left"))
                else:
                    wrapped = wrap_cell_text(r, width, max_subrows=5)
                    for sub in wrapped:
                        out.append(pad_cell_display_width(sub, width, align="left"))
        out.append(bottom)
    for idx, l in enumerate(out, 1):
        assert len(l) == width, f"Banner row {idx} len {len(l)} != {width}: {l}"
        assert get_display_width(l) == width, f"Banner row {idx} dw {get_display_width(l)} != {width}: {l}"
    return "\n".join(out)

def main():
    parser = argparse.ArgumentParser(
        description="Format text into symmetrical ASCII tables & boxes (TablesGenerator reference standard)"
    )
    parser.add_argument("--title", default="", help="Table or box title")
    parser.add_argument("--chatroom", action="store_true", help="Force exact 74-column chatroom width")
    parser.add_argument("--width", type=int, default=74, help="Width in columns (default: 74)")
    parser.add_argument("--table", action="store_true", help="Format as multi-column grid table")
    parser.add_argument("--kv", action="store_true", help="Format as 2-column key-value table")
    parser.add_argument("--banner", action="store_true", help="Generate borderless banner (74 cols)")
    parser.add_argument("--headers", nargs="+", help="Column headers for table")
    parser.add_argument("--text", nargs="+", help="Content lines to format")
    args = parser.parse_args()

    width = 74 if args.chatroom else args.width

    if args.banner:
        lines = args.text if args.text else ["Project Somnarak Non-Wiki Archive", "100% Monospace Precision"]
        result = make_borderless_banner(args.title or "PROJECT SOMNARAK DISPATCH", lines, width=width)
    elif args.table or (args.headers and len(args.headers) > 1):
        headers = args.headers or ["COMPONENT", "SPECIFICATION"]
        rows = [t.split(" | ") if " | " in t else [t, ""] for t in (args.text or ["Item A | Value A", "Item B | Value B"])]
        result = make_table(headers=headers, rows=rows, title=args.title or None, width=width)
    elif args.kv:
        rows = [t.split(" | ") if " | " in t else [t, ""] for t in (args.text or ["Status | Active", "Verification | 100%"])]
        result = make_kv_table(rows, title=args.title or None, width=width)
    else:
        lines = args.text if args.text else [
            "Project Somnarak Non-Wiki Archive",
            "Arena.ai Chatroom Standard: 74 Columns",
            "---",
            "TablesGenerator Reference Standard (+-+| Grid)",
            "Zero crooked lines across all viewports"
        ]
        result = make_box(args.title or "PROJECT SOMNARAK HUD", lines, width=width)

    print("```text")
    print(result)
    print("```")

if __name__ == "__main__":
    main()
