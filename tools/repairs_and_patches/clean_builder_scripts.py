#!/usr/bin/env python3
"""
tools/clean_builder_scripts.py
Cleans LaTeX dollar signs from Python string templates in tools/build_*.py.
"""

import glob
import re

def clean_script(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    orig = content

    # Replace escaped or raw dollar signs used as LaTeX delimiters
    # In python strings, they appear as  or 
    # Replace patterns like +3, +3, etc.
    content = re.sub(r'\\?\\?([+-]?\d+(?:\.\d+)?%?)\\?', r'\1', content)
    content = re.sub(r'\\?\\?\\text\{([^}]+)\}\\?', r'\1', content)
    content = re.sub(r'\\?\\?\\Delta\\? N\\?', r'Delta N', content)
    content = re.sub(r'\\?\\?(\\Delta\\? N\s*\\?[<>]=?\s*\d+)\\?', r'\1', content)
    content = re.sub(r'\\?\\?([A-Za-z0-9_<>=\s\+\-\*/\(\)]+)\\?', lambda m: m.group(1).replace('\\', ''), content)
    content = content.replace('\', '')
    content = content.replace('', '')

    # Fix any accidental variable replacements if any (there are no  variables in python)
    if content != orig:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    builders = glob.glob("tools/build_*.py")
    for b in sorted(builders):
        if clean_script(b):
            print(f"Cleaned {b}")

if __name__ == "__main__":
    main()
