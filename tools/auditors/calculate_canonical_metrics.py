import glob
import os
import json

def get_files(pattern):
    return [f for f in glob.glob(pattern, recursive=True) if os.path.isfile(f)]

se_files = [f for f in glob.glob("SOMNARAK-WORLD/Sorrow_Entities/*.md") if not f.endswith("README.md")]
ue_files = [f for f in glob.glob("SOMNARAK-WORLD/Unknown_Entities/*.md") if not f.endswith("README.md")]
ht_files = [f for f in glob.glob("SOMNARAK-WORLD/Hope_Transformations/*.md") if not f.endswith("README.md")]
ordeal_files = [f for f in glob.glob("SOMNARAK-WORLD/Ordeals/*.md") if not f.endswith("README.md")]
cantos_files = [f for f in glob.glob("SOMNARAK-WORLD/Story_Cantos/*.md") if not f.endswith("README.md")]
gb_files = [f for f in glob.glob("GAME_BATTLE/*.md") if not f.endswith("README.md")]
maw_sets = [d for d in glob.glob("SOMNARAK-WORLD/MAW_Codex_Sets/*") if os.path.isdir(d)]
maw_files = [f for f in glob.glob("SOMNARAK-WORLD/MAW_Codex_Sets/**/*.md", recursive=True)]
somnarak_world_files = [f for f in glob.glob("SOMNARAK-WORLD/**/*", recursive=True) if os.path.isfile(f)]
pm_research_files = [f for f in glob.glob("PROJECT_MOON_RESEARCH/*.md") if not f.endswith("README.md")]
docs_files = [f for f in glob.glob("docs/**/*", recursive=True) if os.path.isfile(f)]
all_repo_files = [f for f in glob.glob("**/*", recursive=True) if os.path.isfile(f) and not f.startswith(".git/")]

# Relic files in Sorrow_Entities:
relic_files = []
for f in se_files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    if "-Relic" in c or "Tool Abnormality" in c or "A-Relic" in c:
        relic_files.append(f)

metrics = {
    "total_sorrow_entities": len(se_files),
    "total_relic_entities": len(relic_files),
    "relic_entity_percentage": round(len(relic_files) / len(se_files) * 100, 2),
    "total_unknown_entities": len(ue_files),
    "total_hope_transformations": len(ht_files),
    "total_ordeals": len(ordeal_files),
    "total_story_cantos": len(cantos_files),
    "total_game_battle_scenarios": len(gb_files),
    "total_maw_codex_sets": len(maw_sets),
    "total_maw_markdown_files": len(maw_files),
    "total_pm_research_volumes": len(pm_research_files),
    "total_somnarak_world_files": len(somnarak_world_files),
    "total_docs_files": len(docs_files),
    "total_repository_files_ex_git": len(all_repo_files),
}

print(json.dumps(metrics, indent=2))
