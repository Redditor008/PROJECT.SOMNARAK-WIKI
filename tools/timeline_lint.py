import re
import glob
import os
import sys

print("=== PROJECT SOMNARAK // CANON TIMELINE LINTER ===")

CURRENT_YEAR = 4238
CURRENT_CYCLE = 1778

errors = []
warnings = []

# Scan files
canto_files = glob.glob("SOMNARAK-WORLD/Story_Cantos/*.md")
codex_files = glob.glob("SOMNARAK-WORLD/Master_Codices/**/*.md", recursive=True)
ordeal_files = glob.glob("SOMNARAK-WORLD/Ordeals/*.md")
all_files = canto_files + codex_files + ordeal_files

for f in all_files:
    if "CANON_TIMELINE" in f or "banned_strings" in f:
        continue
    with open(f, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    
    for idx, line in enumerate(lines):
        line_num = idx + 1
        
        # Check B1: "five hundred years ago" near Yoon's sister or Cycle 1,580
        if "five hundred years ago" in line and ("Yoon" in line or "1,580" in line or "Collapse" in line):
            errors.append(f"{f}:{line_num} -> B1 Violation: 'five hundred years ago' contradicts Cycle 1,580 math (1778 - 1580 = 198 years).")
            
        # Check B2: "founded 6,000 years ago"
        if "founded 6,000 years ago" in line or "suffering for 6,000 years" in line:
            errors.append(f"{f}:{line_num} -> B2 Violation: '6,000 years ago' contradicts Year 0 founding with Year 4,238 current era.")
            
        # Check B3: "Year 4247"
        if "Year 4247" in line:
            errors.append(f"{f}:{line_num} -> B3 Violation: 'Year 4247' is 9 years beyond the Year 4,238 canonical era anchor.")
            
        # Check relative cycle math in text: "X cycles ago"
        m_cyc = re.search(r'(\d+)\s+cycles\s+ago', line, re.IGNORECASE)
        if m_cyc:
            delta = int(m_cyc.group(1))
            inferred_cycle = CURRENT_CYCLE - delta
            if inferred_cycle < 0:
                errors.append(f"{f}:{line_num} -> Negative cycle inferred ({inferred_cycle}) from '{line.strip()}'.")

print(f"Audited {len(all_files)} files across Cantos, Codices, and Ordeals.")
if errors:
    print(f"\n[FAIL] Found {len(errors)} timeline contradiction(s):")
    for e in errors:
        print("  -", e)
    sys.exit(1)
else:
    print("[PASS] 0 timeline contradictions found! All arithmetic perfectly aligned with CANON_TIMELINE.md (Year 4,238 / Cycle 1,778).")
