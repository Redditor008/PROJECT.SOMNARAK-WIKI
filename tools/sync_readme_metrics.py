import json
import re
import os
import sys

print("=== PROJECT SOMNARAK // README METRICS SYNCHRONIZER ===")

METRICS_PATH = "CANONICAL_METRICS.json"
README_PATH = "README.md"

if not os.path.exists(METRICS_PATH):
    print(f"Error: {METRICS_PATH} not found!")
    sys.exit(1)

with open(METRICS_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

se_count = data["canonical_entities"]["sorrow_entities_count"]
maw_sets = data["canonical_combat_and_hardware"]["maw_codex_sets_count"]
maw_profiles = data["canonical_combat_and_hardware"]["maw_equipment_profiles_count"]
unk_count = data["canonical_entities"]["unknown_entities_count"]
pm_count = data["research_and_documentation"]["pm_research_volumes_count"]
sw_files = data["file_system_totals"]["somnarak_world_files_total"]
repo_files = data["file_system_totals"]["repository_files_total_ex_git"]

with open(README_PATH, "r", encoding="utf-8") as f:
    readme = f.read()

# Replace metrics in README
# 1. Word count and file totals at glance
readme = re.sub(
    r'- \*\*Over \d+[\d,]* curated canonical markdown files in SOMNARAK-WORLD \(\d+\+ total files\)\*\*',
    f'- **Over {sw_files:,} curated canonical markdown files in SOMNARAK-WORLD ({repo_files:,}+ total files)**',
    readme
)
readme = re.sub(
    r'- \*\*Over \d+(\.\d+)? million words\*\*',
    '- **Over 3.42 million words (3,420,000+ words)**',
    readme
)
readme = re.sub(
    r'\(~[\d\.]+ million words\)',
    '(~3.42 million words)',
    readme
)

# 2. SE count
readme = re.sub(
    r'- \*\*\d+ Unique Sorrow Entity Dossiers\*\*',
    f'- **{se_count} Unique Sorrow Entity Dossiers**',
    readme
)
readme = re.sub(
    r'Sorrow_Entities/\s+# \d+ Unique Entity dossiers',
    f'Sorrow_Entities/                    # {se_count} Unique Entity dossiers',
    readme
)

# 3. MAW Sets & Profiles
readme = re.sub(
    r'- \*\*\d+ Complete M\.A\.W\. Equipment Sets\*\* \(`SOMNARAK-WORLD/MAW_Codex_Sets/`[^\)]*\)',
    f'- **{maw_sets} Complete M.A.W. Equipment Sets** (`SOMNARAK-WORLD/MAW_Codex_Sets/`, quadripartite Side-Codex, Weapon, Suit, Gift across {maw_profiles:,} files)',
    readme
)
readme = re.sub(
    r'MAW_Codex_Sets/\s+# [\d,]+ files: \d+ complete quadripartite sets across \d+ folders',
    f'MAW_Codex_Sets/                     # {maw_profiles:,} files: {maw_sets} complete quadripartite sets across {maw_sets} folders',
    readme
)

# 4. Unknown Entities count
readme = re.sub(
    r'- \*\*\d+ Unknown Anomaly Records\*\*',
    f'- **{unk_count} Unknown Anomaly Records**',
    readme
)
readme = re.sub(
    r'Unknown_Entities/\s+# \d+ Unknown Entity files',
    f'Unknown_Entities/                   # {unk_count} Unknown Entity files',
    readme
)

# 5. PM Research Volumes
readme = re.sub(
    r'- \*\*\d+ Encyclopedic Research Volumes\*\*',
    f'- **{pm_count} Encyclopedic Research Volumes**',
    readme
)

with open(README_PATH, "w", encoding="utf-8") as f:
    f.write(readme)

print(f"Successfully synchronized {README_PATH} from {METRICS_PATH}:")
print(f" - Sorrow Entities: {se_count}")
print(f" - MAW Equipment Sets: {maw_sets} sets / {maw_profiles} files")
print(f" - Unknown Entities: {unk_count}")
print(f" - PM Research Volumes: {pm_count}")
print(f" - SOMNARAK-WORLD Files: {sw_files}")
print(f" - Total Repository Files: {repo_files}")
