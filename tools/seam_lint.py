import re
import glob
import os
import sys

print("=== PROJECT SOMNARAK // SEMANTIC-SEAM & DEFECT LINTER ===")

errors = []

# Exclude tools, git, banned_strings, and comparative study codices
def should_audit(path):
    if ".git" in path or "tools/" in path:
        return False
    if "banned_strings.txt" in path or "CANON_TIMELINE" in path:
        return False
    return True

# Banned exact sub-strings in all narrative / entity files
banned_exact = [
    ("out of 1000", "Boilerplate HP fraction leftover"),
    ("themed to its form and element", "Unresolved generator ability placeholder"),
    ("cured.,", "Double punctuation revision splice"),
    ("different tiers. the entity", "Spliced classification sentence fragment"),
    (". or fed the entity", "Orphaned conjunction sentence splice"),
    (". before the next assignment.", "Orphaned prepositional sentence splice"),
]

# Regex patterns (excludes valid relative filesystem paths like '../' or '../../')
p_double_dot = re.compile(r'(?<![\./])\.\.(?![\./])')
p_word_dot_comma = re.compile(r'\b[a-z]{2,}\.,')

files = [f for f in glob.glob("SOMNARAK-WORLD/**/*.md", recursive=True) if should_audit(f)]

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
        
    for idx, line in enumerate(lines):
        line_num = idx + 1
        
        # Check exact banned strings
        for bad_str, reason in banned_exact:
            if bad_str.lower() in line.lower():
                errors.append(f"{f}:{line_num} -> [BANNED_STRING] '{bad_str}' ({reason})")
                
        # Check double dots (excluding ellipsis)
        if p_double_dot.search(line):
            errors.append(f"{f}:{line_num} -> [DOUBLE_DOT] Found exact '..' without third dot: '{line.strip()[:60]}'")
            
        # Check word.,
        if p_word_dot_comma.search(line):
            errors.append(f"{f}:{line_num} -> [PUNCT_SPLICE] Found lowercase word ending with '.,': '{line.strip()[:60]}'")

print(f"Audited {len(files)} files in SOMNARAK-WORLD.")
if errors:
    print(f"\n[FAIL] Found {len(errors)} semantic seam / defect violation(s):")
    for e in errors[:25]:
        print("  -", e)
    if len(errors) > 25:
        print(f"  ... and {len(errors) - 25} more.")
    sys.exit(1)
else:
    print("[PASS] 0 semantic seams or defect violations found! Archive is 100.0% clean across all audited wings.")
