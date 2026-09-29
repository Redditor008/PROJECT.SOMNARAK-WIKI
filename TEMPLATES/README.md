# SOMNARAK TEMPLATES — Deep-Knowledge-First Generation Kit

**Archive Sector:** `TEMPLATES/` (Out-of-Universe Authoring Kit — Never In-World Canon)  
**Authority:** Reverie Directorate Editorial Standards + `GOVERNANCE.md` Tier 2  
**Temporal Anchor:** Year 4,238 · Dawn Initiative · Cycle 1,778 (Absolvohan Only)  
**Purpose:** Every file in this directory exists so that **deep canonical knowledge is known BEFORE any generation ever occurs**. No dossier, codex, scenario, or chronicle should be drafted without first reading its template and the Global Primer.

---

## How To Use This Kit

1. **Read `00_GLOBAL_DEEP_KNOWLEDGE_PRIMER.md` first — always.** It contains the 9 immutable laws that apply to every generation task.
2. **Open the specific template for your task** (e.g., `01_SORROW_ENTITY_DOSSIER_TEMPLATE.md` for a new Entity).
3. **Fill every `{{PLACEHOLDER}}` in order.** Do not delete sections; write `N/A` only where the template explicitly permits it.
4. **Run the validation checklist at the end of each template** before committing.
5. **Run linters:** `python3 tools/audit_lore_archive.py` + `python3 tools/check_box_symmetry.py` must PASS.

---

## Template Index — 23 Deep-Knowledge Templates

### Global Foundation
| # | Template File | Generates |
|---|---|---|
| 00 | `00_GLOBAL_DEEP_KNOWLEDGE_PRIMER.md` | All documents — mandatory first read |
| 22 | `22_BOX_AND_TABLE_FORMATTING_TEMPLATE.md` | Any ASCII box or table |
| 23 | `23_CANONICAL_NAMING_AND_BANNED_STRINGS_TEMPLATE.md` | Names, SECC codes, and vocabulary |

### Entities & Equipment
| # | Template File | Generates |
|---|---|---|
| 01 | `01_SORROW_ENTITY_DOSSIER_TEMPLATE.md` | `SOMNARAK-WORLD/Sorrow_Entities/SE-*.md` |
| 02 | `02_MAW_SIDE_CODEX_TEMPLATE.md` | `SOMNARAK-WORLD/MAW_Codex_Sets/.../SE-*-A__SIDE_CODEX_*.md` |
| 03 | `03_MAW_WEAPON_TEMPLATE.md` | `SOMNARAK-WORLD/MAW_Codex_Sets/.../SE-*-B__MAW-W_*.md` |
| 04 | `04_MAW_SUIT_TEMPLATE.md` | `SOMNARAK-WORLD/MAW_Codex_Sets/.../SE-*-C__MAW-S_*.md` |
| 05 | `05_MAW_STIGMA_TEMPLATE.md` | `SOMNARAK-WORLD/MAW_Codex_Sets/.../SE-*-D__MAW-G_*.md` |
| 06 | `06_ORDEAL_TEMPLATE.md` | `SOMNARAK-WORLD/Ordeals/Ordeal_*.md` |
| 07 | `07_HOPE_TRANSFORMATION_TEMPLATE.md` | `SOMNARAK-WORLD/Hope_Transformations/HT-*.md` |
| 08 | `08_UNKNOWN_ENTITY_TEMPLATE.md` | `SOMNARAK-WORLD/Unknown_Entities/SE-*.md` |

### Leadership & World Codices
| # | Template File | Generates |
|---|---|---|
| 09 | `09_ECHO_CORE_DOSSIER_TEMPLATE.md` | `SOMNARAK-WORLD/Echo_Cores/THE_*.md` |
| 10 | `10_MASTER_CODEX_TEMPLATE.md` | `SOMNARAK-WORLD/Master_Codices/**/*.md` |
| 17 | `17_MUGENHAN_ECOLOGY_TEMPLATE.md` | `SOMNARAK-WORLD/Mugenhan_Ecology/*.md` |

### Narrative Chronicles
| # | Template File | Generates |
|---|---|---|
| 11 | `11_ABSOLOVHAN_DAYLOG_TEMPLATE.md` | `SOMNARAK-WORLD/The_Absolvohan/Part_*.md` |
| 12 | `12_KATABAGIL_PASSAGE_TEMPLATE.md` | `SOMNARAK-WORLD/Katabagil/Passage_*.md` |
| 13 | `13_KATHARCHEOK_OPERATION_TEMPLATE.md` | `SOMNARAK-WORLD/Katharcheok/Operation_*.md` |
| 14 | `14_GIEOK_READING_TEMPLATE.md` | `SOMNARAK-WORLD/Gieok_Jeojangso/Reading_*.md` |
| 15 | `15_JIPYEONGSEONDAE_ARC_TEMPLATE.md` | `SOMNARAK-WORLD/Jipyeongseondae/Arc_*.md` |
| 16 | `16_STORY_CANTO_TEMPLATE.md` | `SOMNARAK-WORLD/Story_Cantos/CANTO_*.md` |

### Tactical Systems
| # | Template File | Generates |
|---|---|---|
| 18 | `18_TACTICAL_COMBAT_ENGINE_TEMPLATE.md` | `SOMNARAK-WORLD/Tactical_Combat_Engine/*.md` |
| 19 | `19_BATTLE_SCENARIO_DEEP_TEMPLATE.md` | `GAME_BATTLE/SCENARIO_*.md` + `CANONICAL_ENCOUNTER_*.md` |
| 20 | `20_BOSS_MECHANICS_TEMPLATE.md` | `GAME_BATTLE/BOSS_MECHANICS_*.md` |
| 21 | `21_SQUAD_ARCHETYPE_TEMPLATE.md` | `GAME_BATTLE/SQUAD_ARCHETYPE_*.md` |

---

## Deep Knowledge Guarantee

Each template embeds the same 9 laws plus its domain-specific constraints **inside the template itself**, so a generator never needs to search external files. The laws are written at the top of every template under `## DEEP KNOWLEDGE — READ BEFORE WRITING`.

## File Naming Rule for Templates

Template files themselves are NEVER moved into `SOMNARAK-WORLD/` or `GAME_BATTLE/`. They stay in `TEMPLATES/`. Generated canon files use the naming convention documented inside each template.

## Validation

After filling a template:

```bash
python3 tools/audit_lore_archive.py
python3 tools/check_box_symmetry.py
python3 tools/timeline_lint.py
python3 tools/seam_lint.py
```

All four must return `PASS` before push (Rule A0: commit + push in same turn).

---

*This kit replaces tribal knowledge with written law. If a rule is not in the primer, it is not a rule — update the primer first.*
