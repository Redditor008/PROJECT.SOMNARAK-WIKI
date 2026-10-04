import re
import glob
import os
import sys

print("=== PROJECT SOMNARAK // PAN-REPO CANON TIMELINE LINTER ===")

CURRENT_YEAR = 4238
CURRENT_CYCLE = 1778
WINDOW_END = 4255  # post-Dawn projection window: 4239-4255 legitimate per codex rows

# Whitelist patterns for authorized forward projections according to CANON_TIMELINE.md Section 5
WHITELIST_PATTERNS = [
    re.compile(r'Year\s+4250\+'),                     # Company 4 Wound Walkers epilogue
    re.compile(r'predicted for Year 4239'),            # SE-O-Vγ-003 prospective weather prediction
    re.compile(r'Years?\s+4,?301'),                    # Theoretical deep-future decay tables in PROJECT_SOMNARAK
    re.compile(r'Years?\s+4,?567'),
    re.compile(r'Years?\s+4,?892'),
    re.compile(r'Years?\s+5,?234'),
    re.compile(r'Years?\s+5,?789'),
    re.compile(r'CANON_TIMELINE\.md'),                 # Master SSOT definition
    re.compile(r'CANONICAL_METRICS'),                  # Metrics tracking
]

errors = []
warnings = []

# Pan-repo file collection
search_patterns = [
    "SOMNARAK-WORLD/**/*.md",
    "GAME_BATTLE/**/*.md",
    "*.md"
]

all_files = []
for pat in search_patterns:
    all_files.extend(glob.glob(pat, recursive=True))

# Deduplicate and filter out git, tools, and reference documentation
clean_files = []
for f in sorted(list(set(all_files))):
    if ".git" in f or "tools/" in f or "REFERENCE_SOMNARAK_WIKI" in f or "CHANGELOG" in f or "INTEGRITY_AND_LORE_REVIEW" in f:
        continue
    clean_files.append(f)

p_year = re.compile(r'\bYear\s+(\d{4})\b')
p_year_comma = re.compile(r'\bYears?\s+(\d),(\d{3})\b')
p_cycles_ago = re.compile(r'(\d+)\s+cycles\s+ago', re.IGNORECASE)
# V5-11: loop-end / Hand-of-Hope must be Year 4,238; SED/UCD campaigns must predate 4,201
p_loop_end_year = re.compile(r'\bYears?\s+4,?23[23]\b(?!\s*\+)|(?<![\d+])4,?23[23](?!\s*\+)(?!\d)')
p_loop_end_trig = re.compile(r'Hand of Hope|Absolvohan fires|loop (ends|end|breaks|break|terminates|terminated)|\bDawn\b')
p_sed_ucd = re.compile(r'SED|UCD|Katabagil|Katharcheok')
p_campaign = re.compile(r'campaign|descent|operation|purge|expedition|offensive', re.IGNORECASE)
p_any_year = re.compile(r'\b4,?(\d{3})\b')

for f in clean_files:
    if "CANON_TIMELINE.md" in f or "banned_strings" in f:
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
            
        # B3 retired: Year 4247 sits inside the legitimate 4239-4255 post-Dawn window.
            
        # Check F1: Any year beyond the 4255 window without explicit whitelist
        years = [int(m.group(1)) for m in p_year.finditer(line)]
        years += [int(m.group(1) + m.group(2)) for m in p_year_comma.finditer(line)]
        for y in years:
            if y > WINDOW_END:
                # check if line matches whitelist
                if not any(wp.search(line) for wp in WHITELIST_PATTERNS):
                    errors.append(f"{f}:{line_num} -> F1 Violation: Year {y} exceeds Year {WINDOW_END} window: '{line.strip()}'")

        # V5-11 checks run per sentence segment (never split box-row ' : ' cells)
        segments = re.split(r'\||;\s*|\.\s+|\!\s+|\?\s+', line)
        # Check C1: loop-end / Hand-of-Hope language pinned to Year 4,232/4,233
        if any(p_loop_end_year.search(sg) and p_loop_end_trig.search(sg) for sg in segments):
            errors.append(f"{f}:{line_num} -> C1 Violation: loop-end/Hand/Dawn language must use Year 4,238, not 4,232/4,233: '{line.strip()[:120]}'")
        # Check C2: SED/UCD campaigns dated after Year 4,200
        if any(p_sed_ucd.search(sg) and p_campaign.search(sg) for sg in segments):
            for ym in p_any_year.finditer(line):
                yy = 4000 + int(ym.group(1))
                if 4200 < yy <= 4299:
                    errors.append(f"{f}:{line_num} -> C2 Violation: SED/UCD campaign year {yy} is after Year 4,200: '{line.strip()[:120]}'")
                    break

        # Check relative cycle math in text: "X cycles ago"
        m_cyc = p_cycles_ago.search(line)
        if m_cyc:
            delta = int(m_cyc.group(1))
            inferred_cycle = CURRENT_CYCLE - delta
            if inferred_cycle < 0:
                errors.append(f"{f}:{line_num} -> Negative cycle inferred ({inferred_cycle}) from '{line.strip()}'.")

print(f"Audited {len(clean_files)} files pan-repo across SOMNARAK-WORLD, GAME_BATTLE, and repository root.")
if errors:
    print(f"\n[FAIL] Found {len(errors)} timeline contradiction(s):")
    for e in errors:
        print("  -", e)
    sys.exit(1)
else:
    print(f"[PASS] 0 timeline contradictions found! All {len(clean_files)} files perfectly conform to Year 4,238 / Cycle 1,778 anchor.")
