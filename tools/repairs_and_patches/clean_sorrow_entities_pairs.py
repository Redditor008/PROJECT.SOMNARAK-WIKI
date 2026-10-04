#!/usr/bin/env python3
"""
tools/clean_sorrow_entities_pairs.py
Consolidates the 241 duplicate entity pairs in SOMNARAK-WORLD/Sorrow_Entities/
into single canonical files, updating all cross-references across the repository.
"""

import os
import re
import glob

PAIRS_AUDIT_PATH = "REFERENCE_SOMNARAK_WIKI/SORROW_ENTITIES_PAIRS_AUDIT.md"
SE_DIR = "SOMNARAK-WORLD/Sorrow_Entities"

def parse_pairs():
    with open(PAIRS_AUDIT_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    matches = re.findall(r'\|\s*`([^`]+)`\s*\|\s*\*\*(\d+)\*\*\s*\|\s*([^|]+)\|\s*`([^`]+)`\s*\|', text)
    
    replacements = {}
    to_delete = set()
    to_keep = set()

    for code, count, var_str, rec in matches:
        filenames = re.findall(r'`([^`]+\.md)`', var_str)
        rec_clean = rec.strip()
        to_keep.add(rec_clean)
        for fn in filenames:
            fn_clean = fn.strip()
            if fn_clean != rec_clean:
                to_delete.add(fn_clean)
                replacements[fn_clean] = rec_clean

    return replacements, to_delete, to_keep

def update_references(replacements):
    all_md_files = glob.glob("SOMNARAK-WORLD/**/*.md", recursive=True) + glob.glob("REFERENCE_SOMNARAK_WIKI/**/*.md", recursive=True)
    updated_files = 0
    total_replacements = 0

    for fpath in all_md_files:
        with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        new_content = content
        file_changed = False
        for old_fn, new_fn in replacements.items():
            if old_fn in new_content:
                new_content = new_content.replace(old_fn, new_fn)
                file_changed = True
                total_replacements += 1

        if file_changed:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_content)
            updated_files += 1

    print(f"Updated {total_replacements} references across {updated_files} markdown files.")

def remove_duplicates(to_delete):
    deleted_count = 0
    for fn in to_delete:
        p = os.path.join(SE_DIR, fn)
        if os.path.exists(p):
            os.remove(p)
            deleted_count += 1
        else:
            print(f"Warning: File not found to delete: {p}")
    print(f"Successfully deleted {deleted_count} redundant duplicate entity dossiers.")

def main():
    replacements, to_delete, to_keep = parse_pairs()
    print(f"Parsed {len(replacements)} replacements from pairs audit.")
    print(f"Files to delete: {len(to_delete)}, Canonical to keep: {len(to_keep)}")

    # Update references first
    update_references(replacements)

    # Delete duplicates
    remove_duplicates(to_delete)

    # Verify remaining files in Sorrow_Entities
    remaining = [f for f in os.listdir(SE_DIR) if f.endswith(".md") and f != "README.md"]
    print(f"Total remaining entity dossiers in {SE_DIR}: {len(remaining)}")

if __name__ == "__main__":
    main()
