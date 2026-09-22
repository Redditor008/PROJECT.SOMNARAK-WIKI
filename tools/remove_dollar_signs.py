#!/usr/bin/env python3
"""
tools/remove_dollar_signs.py
Systematically removes all LaTeX dollar sign math delimiters ($...$ and $$...$$)
across markdown files in SOMNARAK-WORLD/ and TEST_TEXT_BOX_WIDTHS.md,
replacing them with clean plain-text representations.
"""

import os
import re

def clean_math(match):
    s = match.group(1).strip()
    # Replacements within math
    s = re.sub(r'\\text\{([^}]+)\}', r'\1', s)
    s = re.sub(r'\\left\(', '(', s)
    s = re.sub(r'\\right\)', ')', s)
    s = re.sub(r'\\lfloor', 'floor(', s)
    s = re.sub(r'\\rfloor', ')', s)
    s = re.sub(r'\\Delta', 'Delta', s)
    s = re.sub(r'\\sum', 'sum', s)
    s = re.sub(r'\\times', '*', s)
    s = re.sub(r'\\quad', ' ', s)
    s = re.sub(r'\\le', '<=', s)
    s = re.sub(r'\\ge', '>=', s)
    s = re.sub(r'\\circ\\text\{C\}|\^\\circ\\text\{C\}|\^\\circ C', '°C', s)
    s = re.sub(r'\\%', '%', s)
    s = re.sub(r'\\_', '_', s)
    s = s.replace('\\', '')
    return s

def clean_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    orig = content

    # 1. Block math: $$ ... $$
    content = re.sub(r'\$\$(.*?)\$\$', clean_math, content, flags=re.DOTALL)

    # 2. Inline math: $ ... $
    content = re.sub(r'\$(.*?)\$', clean_math, content)

    # Specific cleanups if any stray backslashes or artifacts remain
    content = content.replace('\\%', '%')

    if content != orig:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    target_dirs = ["SOMNARAK-WORLD"]
    extra_files = ["TEST_TEXT_BOX_WIDTHS.md"]

    modified = []
    for d in target_dirs:
        for root, dirs, files in os.walk(d):
            for f in sorted(files):
                if f.endswith(".md"):
                    p = os.path.join(root, f)
                    if clean_file(p):
                        modified.append(p)

    for ef in extra_files:
        if os.path.exists(ef):
            if clean_file(ef):
                modified.append(ef)

    print(f"Cleaned dollar signs in {len(modified)} files:")
    for m in modified:
        print(f"  - {m}")

if __name__ == "__main__":
    main()
