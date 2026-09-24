#!/usr/bin/env python3
"""
tools/box_formatter.py — Canonical Text Box & Borderless Banner Generator
Project Somnarak Non-Wiki Archive

Enforces strict compliance with Project Somnarak and Arena.ai Chatroom standards:
1. Arena.ai Chatroom Standard (Width: EXACTLY 74 COLUMNS):
   - Command: --chatroom or default width 74.
   - Total width: 74 columns (+ + 72 =/- + +).
   - Inner content width: 70 columns (| + space + 68 chars + space + |).
   - Matches the Arena.ai chatroom 74-character auto-wrap limit.
2. Enclosed ASCII Boxes in Markdown Files:
   - Width: 71 to 74 columns (standard compact format).
   - Counts all rows, benchmarks against target width, and pads shorter rows.
   - Long lines wrap into visual sub-rows at word boundaries without truncation.
   - Fully CJK / East Asian Width aware (proper display width padding).
3. Borderless Banners:
   - Width: Exactly 74 characters long ("=" * 74 and "-" * 74).
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
    
    # Fits on one line
    if get_display_width(r) <= max_len:
        return [r]
    
    # Unit diagram token line
    if r_strip.startswith("[") and not r_strip.startswith("- "):
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

def make_box(title, raw_rows, width=74, max_width=None):
    """
    Builds a symmetrical ASCII text box.
    - Default width: 74 columns (Arena.ai chatroom standard).
    - Counts all rows, benchmarks against target width, and pads shorter rows.
    - Wraps overflowing content cleanly across sub-rows without token truncation.
    """
    if max_width is not None and width > max_width:
        width = max_width

    target_inner_dw = width - 4
    max_len = target_inner_dw

    formatted_rows = []
    for r in raw_rows:
        if isinstance(r, (list, tuple)):
            for sub_r in r:
                formatted_rows.extend(_process_row(str(sub_r), max_len))
        else:
            formatted_rows.extend(_process_row(str(r), max_len))

    actual_box_width = width

    top = "+" + "=" * (actual_box_width - 2) + "+"
    bottom = "+" + "=" * (actual_box_width - 2) + "+"
    sep = "+" + "-" * (actual_box_width - 2) + "+"

    out = [top]
    if title:
        t_clean = f" {title.strip()} "
        cur_t_dw = get_display_width(t_clean)
        if cur_t_dw > (actual_box_width - 2):
            t_clean = t_clean[:(actual_box_width - 2)]
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
                out.append(r)
        out.append(bottom)
    return "\n".join(out)

def main():
    parser = argparse.ArgumentParser(
        description="Format text into symmetrical ASCII boxes (74 cols chatroom / file)"
    )
    parser.add_argument("--title", default="", help="Box or banner title")
    parser.add_argument("--chatroom", action="store_true", help="Force exact 74-column chatroom width")
    parser.add_argument("--width", type=int, default=74, help="Box width in columns (default: 74)")
    parser.add_argument("--banner", action="store_true", help="Generate borderless banner (74 cols)")
    parser.add_argument("--text", nargs="+", help="Content lines to format")
    args = parser.parse_args()

    width = 74 if args.chatroom else args.width

    lines = args.text if args.text else [
        "Project Somnarak Non-Wiki Archive",
        "Arena.ai Chatroom Standard: 74 Columns",
        "---",
        "Status: 100% Monospace Precision",
        "Zero crooked lines across all viewports"
    ]

    if args.banner:
        result = make_borderless_banner(args.title or "PROJECT SOMNARAK DISPATCH", lines, width=width)
    else:
        result = make_box(args.title or "PROJECT SOMNARAK HUD", lines, width=width)

    print("```text")
    print(result)
    print("```")

if __name__ == "__main__":
    main()
