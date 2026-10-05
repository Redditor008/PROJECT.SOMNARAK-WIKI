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
# Echo-Core command-floor canon: EC-N commands Floor (N-1) for N>=2; EC1 holds Floor 1
p_ec_command = re.compile(r'Echo-Core (\d)[^.\n]{0,80}?(?:command(?:s|er)?|holds?|keeps?|leads?|heads?|administers?|runs?|watches over)[^.\n]{0,40}?Floor 0?(\d)'.replace(chr(92)+'n', chr(92)+'n'))

# Retired rank names must not return: Wail/Whisper/Murmur near Rank or a Roman numeral
p_old_rank = re.compile(r'\b(Wail|Whisper|Murmur)\b.{0,24}\b([Rr]ank|II(?![.\d])|III(?![.\d])|IV(?![.\d])|V(?![.\d]))\b|\b([Rr]ank|II(?![.\d])|III(?![.\d])|IV(?![.\d])|V(?![.\d]))\b.{0,24}\b(Wail|Whisper|Murmur)\b')

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

        # Check Echo-Core command-floor canon
        for m in p_ec_command.finditer(line):
            n, fl = int(m.group(1)), int(m.group(2))
            want = 1 if n < 2 else n - 1
            if fl != want:
                errors.append(f"{f}:{line_num} -> [EC_FLOOR] Echo-Core {n} paired with Floor {fl} (canon: EC-N commands Floor N-1; EC1 holds Floor 1)")

        # Check retired rank names (V5-9); the codex deprecation note is whitelisted
        if not ("SOMNARAK_ENTITY_CODEX.md" in f and "Archival variants" in line):
            for m in p_old_rank.finditer(line):
                errors.append(f"{f}:{line_num} -> [OLD_RANK] Retired rank usage: '{m.group(0).strip()[:50]}'")

# Scoped prose path check: backticked / barked *.md filenames outside known-good
# scopes (research mirror, templates-as-examples, history logs) must exist on disk.
_path_skip_dirs = ("REFERENCE_", "PROJECT_MOON_RESEARCH", "TEMPLATES", "tools")
_path_skip_files = {"CHANGELOG.md", "INTEGRITY_AND_LORE_REVIEW.md",
                    "CANONICAL_METRICS.md", "EXPANSION_RESEARCH_STORY_AND_BATTLE.md",
                    "UNIVERSAL_FOLLOW_RULE.md"}
_path_skip_line = ("File plan", "Example", "illustrative", "Purged", "hypothetical",
                   "Archived files", "Legacy", "(archival", " or `", "draft names",
                   "Purged obsolete")
p_md_token = re.compile(r'(?<![A-Za-z0-9_/-])([A-Z][A-Za-z0-9_/-]{2,}?\.md)\b')
_disk_md = set(os.path.basename(p) for p in glob.glob("**/*.md", recursive=True))


def _skip_token(tok):
    base = tok.split("/")[-1]
    if base.startswith(("SE-", "Ordeal_", "ORDEAL-", "HT-", "UNK_", "UNK-")):
        return True
    if re.match(r'SE-[A-Z]-[IVX]', base):
        return True
    if "-A__" in base or "-B__" in base or "-C__" in base or "-D__" in base:
        return True
    return False


_path_files = [f for f in glob.glob("SOMNARAK-WORLD/**/*.md", recursive=True)
               if should_audit(f)]
_path_files += [f for f in glob.glob("GAME_BATTLE/*.md")]
_path_files += [f for f in glob.glob("docs/*.md")]
_path_files += [f for f in glob.glob("*.md")]
for f in _path_files:
    if any(d in f for d in _path_skip_dirs):
        continue
    if os.path.basename(f) in _path_skip_files or not should_audit(f):
        continue
    with open(f, 'r', encoding='utf-8') as fp:
        for line_num, line in enumerate(fp, start=1):
            if any(k in line for k in _path_skip_line):
                continue
            for m in p_md_token.finditer(line):
                tok = m.group(1)
                if _skip_token(tok):
                    continue
                if tok.split("/")[-1] not in _disk_md and "N_" not in tok:
                    errors.append(f"{f}:{line_num} -> [STALE_PATH] '{tok}' has no on-disk file")

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
