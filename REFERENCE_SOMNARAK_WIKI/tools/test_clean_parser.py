import re

def clean_markdown_body(md_text):
    lines = md_text.splitlines()
    cleaned_lines = []
    
    skip_until_next_h2 = False
    in_profile = False
    
    for line in lines:
        stripped = line.strip()
        
        # Skip title and top metadata block
        if stripped.startswith("# Echo-Core") or stripped.startswith("# 1.") or stripped.startswith("# THE_"):
            continue
        if stripped.startswith("> **WIKI SECTION:") or stripped.startswith("> **CLASSIFICATION:") or stripped.startswith("> **SPOILER STATUS:"):
            continue
        if "This page contains detailed information about" in stripped:
            continue
            
        # Check for Contents section to skip
        if stripped.startswith("## Contents") or stripped.startswith("## Table of Contents") or stripped == "## 1. Contents":
            skip_until_next_h2 = True
            continue
            
        if skip_until_next_h2:
            if stripped.startswith("## "):
                skip_until_next_h2 = False
            else:
                continue
                
        # Check for Profile section to skip (since rendered in sidebar)
        if stripped == "## Profile" or stripped == "## 1. Profile":
            skip_until_next_h2 = True
            continue
            
        # Strip leading numbers from headings like "## 1. Appearance" -> "## Appearance"
        h_match = re.match(r'^(#{2,4})\s+([0-9]+\.\s+)?(.+)$', stripped)
        if h_match:
            hashes = h_match.group(1)
            title = h_match.group(3).strip()
            # Clean title
            title = re.sub(r'\[Echo-Core\]', '', title).strip()
            title = re.sub(r'[*_]', '', title).strip()
            cleaned_lines.append(f"{hashes} {title}")
            continue
            
        cleaned_lines.append(line)
        
    return "\n".join(cleaned_lines)

with open("/home/user/salvaged_source_materials/FOR WIKI/00_Source_Materials/Character_Wiki/THE_DIRECTOR.md", "r") as f:
    raw = f.read()

res = clean_markdown_body(raw)
print("=== Cleaned Result Sample ===")
for l in res.splitlines()[:35]:
    print(l)
