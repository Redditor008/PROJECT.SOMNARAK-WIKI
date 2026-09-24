#!/usr/bin/env python3
"""
tools/box_formatter.py — Canonical Text Box & Borderless Banner Generator
Project Somnarak Non-Wiki Archive

Enforces strict compliance with Project Somnarak and Arena.ai Chatroom standards:
1. Enclosed ASCII Boxes (+ and | borders):
   - Standard width: 71 columns (compact/mobile safe).
   - Hard upper ceiling: 74 columns (prevents Arena.ai chatroom viewport auto-wrap down).
   - Counts all rows in the box, benchmarks against the longest row, and pads shorter rows.
   - Long lines wrap into visual sub-rows at word boundaries rather than truncating tokens.
   - Fully CJK / East Asian Width aware (proper display width padding).
2. Borderless Banners (no side borders):
   - Top and bottom horizontal borders are made EXACTLY 74 characters long ("=" * 74).
   - Horizontal dividers are made EXACTLY 74 characters long ("-" * 74).
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

def pad_to_display_width(s, target_dw):
    """Pad string s with ASCII spaces until its monospace display width equals target_dw."""
    cur_dw = get_display_width(s)
    diff = target_dw - cur_dw
    if diff > 0:
        return s + (" " * diff)
    return s

def wrap_text_display_width(text, max_dw, indent=""):
    """Wrap a long string into sub-rows such that no row exceeds max_dw in display width."""
    words = text.split()
    if not words:
        return [""]
    lines = []
    cur = words[0]
    for w in words[1:]:
        if get_display_width(cur) + 1 + get_display_width(w) <= max_dw:
            cur += " " + w
        else:
            lines.append(cur)
            cur = indent + w
    lines.append(cur)
    return lines

def _process_row(r, max_len):
    """Process an individual row into sub-rows fitting within max_len columns."""
    r_strip = r.strip()
    if r_strip == "---":
        return ["---"]
    if r_strip.startswith("==="):
        return ["==="]
    
    # Stage node diagram line
    if "[N01]" in r and ("---" in r or "[N10]" in r or "[N0" in r):
        return ["    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]    "]
    
    # Fits on one line
    if get_display_width(r) <= max_len:
        return [r]
    
    # Unit diagram token line
    if r_strip.startswith("[") and not r_strip.startswith("- "):
        parts = re.findall(r"\s*\[[^\]]+\]", r)
        if parts:
            compact = "".join(parts).strip()
            if get_display_width(compact) <= max_len:
                return [compact]
            else:
                mid = len(parts) // 2
                p1 = "".join(parts[:mid]).strip()
                p2 = "".join(parts[mid:]).strip()
                return [p1, p2]
    
    # Pipe-separated table/status row
    if " | " in r:
        parts = r.split(" | ")
        lines = []
        cur = parts[0]
        for p in parts[1:]:
            if get_display_width(cur) + 3 + get_display_width(p) <= max_len:
                cur += " | " + p
            else:
                lines.append(cur)
                cur = "  | " + p
        lines.append(cur)
        return lines

    # Standard bullet or sentence text
    indent = "  " if r_strip.startswith("- ") else ""
    return wrap_text_display_width(r, max_len, indent)

def make_box(title, raw_rows, width=71, max_width=74):
    """
    Builds a symmetrical ASCII text box.
    - Clamped to max_width (default 74 cols max for Arena.ai chatroom compliance).
    - Counts all rows, benchmarks against the longest row, and pads shorter rows.
    - Wraps overflowing content cleanly across sub-rows without token truncation.
    """
    if width > max_width:
        width = max_width
    max_len = width - 4

    formatted_rows = []
    for r in raw_rows:
        if isinstance(r, (list, tuple)):
            for sub_r in r:
                formatted_rows.extend(_process_row(str(sub_r), max_len))
        else:
            formatted_rows.extend(_process_row(str(r), max_len))

    # COUNT ALL ROWS: Compute display width of all content rows and title
    row_dws = [get_display_width(fr) for fr in formatted_rows if fr not in ("---", "===")]
    title_dw = get_display_width(f" {title.strip()} ") if title else 0
    max_content_dw = max(row_dws, default=0)
    longest_needed_dw = max(max_content_dw, title_dw)

    # Determine inner target display width (benchmark against longest row, bounded by max_width - 4)
    target_inner_dw = max(max_len, longest_needed_dw)
    if target_inner_dw + 4 > max_width:
        target_inner_dw = max_width - 4
    
    actual_box_width = target_inner_dw + 4

    top = "+" + "=" * (actual_box_width - 2) + "+"
    bottom = "+" + "=" * (actual_box_width - 2) + "+"
    sep = "+" + "-" * (actual_box_width - 2) + "+"

    out = [top]
    if title:
        t_clean = f" {title.strip()} "
        cur_t_dw = get_display_width(t_clean)
        diff = (actual_box_width - 2) - cur_t_dw
        left_pad = max(diff // 2, 0)
        right_pad = max(diff - left_pad, 0)
        out.append("|" + (" " * left_pad) + t_clean + (" " * right_pad) + "|")
        out.append(sep)

    for fr in formatted_rows:
        if fr == "---":
            out.append(sep)
        elif fr == "===":
            out.append(top)
        else:
            padded_content = pad_to_display_width(fr.rstrip(), target_inner_dw)
            out.append(f"| {padded_content} |")
    out.append(bottom)
    return "\n".join(out)

def make_borderless_banner(title, rows=None, width=74):
    """
    Builds a borderless ASCII banner or divider.
    Per Arena.ai Chatroom Law: If a banner does not have left and right borders,
    its top and bottom horizontal borders are made EXACTLY 74 characters long.
    """
    top = "=" * width
    bottom = "=" * width
    sep = "-" * width
    out = [top]
    if title:
        t_clean = f" {title.strip()} "
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
                out.append(r)
        out.append(bottom)
    return "\n".join(out)

def main():
    parser = argparse.ArgumentParser(
        description="Format text into symmetrical ASCII boxes (<= 74 cols) or borderless banners (74 cols)"
    )
    parser.add_argument("--title", default="", help="Box or banner title")
    parser.add_argument("--width", type=int, default=71, help="Box width in columns (default: 71, max: 74)")
    parser.add_argument("--banner", action="store_true", help="Generate borderless banner (exactly 74 columns)")
    parser.add_argument("--text", nargs="+", help="Content lines to format")
    args = parser.parse_args()

    lines = args.text if args.text else [
        "Project Somnarak Non-Wiki Archive",
        "Dual-Environment Typography & Viewport Standard",
        "---",
        "Compact Box Width : <= 74 characters max (safe for Arena.ai chatroom auto-wrap)",
        "Borderless Banner : exactly 74 characters long for top and bottom borders"
    ]

    if args.banner:
        result = make_borderless_banner(args.title or "PROJECT SOMNARAK DISPATCH", lines, width=74)
    else:
        result = make_box(args.title or "PROJECT SOMNARAK HUD", lines, width=args.width, max_width=74)

    print("```text")
    print(result)
    print("```")

if __name__ == "__main__":
    main()
