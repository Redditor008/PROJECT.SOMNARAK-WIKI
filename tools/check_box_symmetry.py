import os, sys, re, unicodedata

def char_width(c):
    # East Asian Width: W (Wide) and F (Fullwidth) take 2 columns in monospace
    ea = unicodedata.east_asian_width(c)
    if ea in ('W', 'F'):
        return 2
    return 1

def string_display_width(s):
    return sum(char_width(c) for c in s)

def check_file_boxes(filepath):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
    
    in_box = False
    box_lines = []
    box_start_idx = 0
    issues = []
    
    for idx, raw in enumerate(lines, 1):
        line = raw.rstrip("\r\n")
        if line.startswith("```"):
            if in_box:
                # evaluate finished box
                issues.extend(evaluate_box(filepath, box_start_idx, box_lines))
                in_box = False
                box_lines = []
            else:
                in_box = True
                box_start_idx = idx + 1
                box_lines = []
            continue
        
        if in_box:
            # Check if this line is a box border line (starts with + or |)
            if line.startswith("+") or line.startswith("|"):
                box_lines.append((idx, line))
            else:
                if box_lines:
                    issues.extend(evaluate_box(filepath, box_start_idx, box_lines))
                    box_lines = []
    
    if in_box and box_lines:
        issues.extend(evaluate_box(filepath, box_start_idx, box_lines))
        
    return issues

def evaluate_box(filepath, start_idx, box_lines):
    if not box_lines:
        return []
    
    issues = []
    # 1. Check line length and display width consistency
    first_idx, first_line = box_lines[0]
    expected_len = len(first_line)
    expected_display_w = string_display_width(first_line)
    
    # Track separator positions of first line (positions of + or |)
    expected_seps = [i for i, c in enumerate(first_line) if c in ('+', '|')]
    
    for idx, l in box_lines:
        l_len = len(l)
        l_disp = string_display_width(l)
        seps = [i for i, c in enumerate(l) if c in ('+', '|')]
        
        # Check string length
        if l_len != expected_len:
            issues.append((filepath, idx, f"String len mismatch: {l_len} vs expected {expected_len}", l))
            continue
            
        # Check display width
        if l_disp != expected_display_w:
            issues.append((filepath, idx, f"Display width mismatch (crooked CJK?): {l_disp} vs expected {expected_display_w}", l))
            
        # Check separator alignment
        if seps != expected_seps:
            issues.append((filepath, idx, f"Separator mismatch (crooked columns): {seps} vs expected {expected_seps}", l))
            
    return issues

# Test across repository
print("Scanning repository for crooked text boxes...")
all_issues = []
for root, dirs, files in os.walk("."):
    if ".git" in root or "node_modules" in root:
        continue
    for f in files:
        if f.endswith(".md"):
            p = os.path.join(root, f)
            iss = check_file_boxes(p)
            all_issues.extend(iss)

print(f"Total box symmetry issues found: {len(all_issues)}")
for item in all_issues[:30]:
    print(f"{item[0]}:{item[1]}: {item[2]} -> {item[3]}")
