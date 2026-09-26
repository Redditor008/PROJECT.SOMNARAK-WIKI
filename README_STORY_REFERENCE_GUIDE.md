# Project Somnarak // Story Writer's Comprehensive Reference Guide
**Archive Package:** `PROJECT_SOMNARAK_STORY_REFERENCE_COMPENDIUM.zip`  
**Anchor Epoch:** Year 4,238 (Mugenhan Municipal Standard) // Cycle 1,778 (R.D. Internal Loop)  
**Standard Tool Reference:** [TablesGenerator Text Tables](https://www.tablesgenerator.com/text_tables)

---

## 1. Executive Summary & Archive Architecture

This compendium has been curated specifically as an authoritative, all-in-one reference package for authors, scriptwriters, worldbuilders, and scenario designers writing stories within the **Project Somnarak** universe or conducting cross-comparative studies with **Project Moon** (*Lobotomy Corporation*, *Library of Ruina*, *Limbus Company*).

```text
+------------------------------------------------------------------------+
|             STORY WRITER'S ARCHIVE DIRECTORY ARCHITECTURE              |
+==========================+=============================================+
| DIRECTORY / FILE         | NARRATIVE UTILITY & CONTENTS                |
+==========================+=============================================+
| SOMNARAK-WORLD/          | Complete primary canon: 292 Sorrow Entity   |
|                          | dossiers, 198 quadripartite MAW armory      |
|                          | sets, 47 Master Codices, Cantos 01-06, and  |
|                          | 366-day Absolvohan operational chronicles.  |
+------------------------------------------------------------------------+
| PROJECT_MOON_RESEARCH/   | Exhaustive 16-volume research compendium of |
|                          | Project Moon lore: Abnormalities, 26 Wings, |
|                          | Fixer Offices, E.G.O equipment, and City.   |
+------------------------------------------------------------------------+
| COMPLETE_SYSTEM_         | Comprehensive 1:1 side-by-side comparative  |
| COMPARISON_SOMNARAK_VS_  | analysis contrasting Somnarak mechanics     |
| LOBOTOMY_CORPORATION.md  | with Lobotomy Corporation systems.          |
+------------------------------------------------------------------------+
| CANON_TIMELINE.md        | Master macro-chronological anchor ledger;   |
|                          | establishes strict ante-Dawn and post-Dawn  |
|                          | sequence and Year 4,238 municipal anchor.   |
+------------------------------------------------------------------------+
| SOMNARAK_GEOLOGY.md      | Planetary geology: The Untouched Wild Lands |
|                          | (UnWiHan), Untouched Ocean, Zone topography |
+------------------------------------------------------------------------+
| GAME_BATTLE/             | Tactical combat simulation: Scenarios 01-06,|
|                          | Boss Realizations, Cycle Engrams, Squads.   |
+------------------------------------------------------------------------+
| REFERENCE_SOMNARAK_WIKI/ | Authorial framework: MAW Variety Design     |
|                          | Framework, chatroom standards, style guide. |
+------------------------------------------------------------------------+
| tools/box_formatter.py   | TablesGenerator reference engine for pure   |
|                          | ASCII text boxes & tables (74 columns).     |
+------------------------------------------------------------------------+
```

---

## 2. Story Writer's Quick Reference Map

When drafting a scene, dialogue, combat sequence, or narrative arc, consult these primary files:

### A. Sorrow Entities (Monsters, Anomalies & Manifestations)
- **Archive Path:** `SOMNARAK-WORLD/Sorrow_Entities/` (292 bespoke files).
- **Format:** Every dossier provides the SECC classification code, Coherence (Ranks I–V), Potency (Grades α–ω), Sorrow Element (Grudge, Resentment, Sorrow, Mourning, Despair), Physical Form, Operational Parameters (valid work types, gauge yields), Combat Record (move names, flavor text, triggers, damage), Appearance, Interaction Records with other entities, and the **Tale (이야기 / Narratio)** and **Testimony (증언 / Testimonium)**.
- **Rule:** Never invent new entities; draw exclusively from the 292 canonical files.

### B. Weapons, Suits, & Relics (M.A.W. Equipment)
- **Archive Path:** `SOMNARAK-WORLD/MAW_Codex_Sets/` (198 complete quadripartite sets across numerical registries).
- **Equipment Quadrilogy:** Every entity yields four bespoke armaments:
  1. **Weapon (`MAW-W`):** Physical manifestation of the entity's tale (e.g. Requiem blade, Maul, Fang, Lens).
  2. **Suit (`MAW-S`):** Protective attire mitigating specific Sorrow elements (Shroud, Mantle, Plate, Veil).
  3. **Gift (`MAW-G`):** Wearable relic granting passive resonance perks (Mask, Charm, Lantern, Stone).
  4. **Pendant / Token (`MAW-P`):** Speed, range, and resonance calibration trinket.
- **Master Overview:** `SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_MAW_CODEX.md`.

### C. Factions, Corporations, & World Order
- **Master Codices:** `SOMNARAK-WORLD/Master_Codices/`
  - `SOMNARAK_CORPORATIONS.md` — The Five Zone Corporations governing the municipal core.
  - `SOMNARAK_UNDERWORLD_SYNDICATES.md` — The Five Syndicates of The Raw operating outside the law.
  - `SOMNARAK_SPECIALIST_CADRES.md` — The Ten Specialist Cadres deployed for containment and pacification.
  - `The_REVERIE_DIRECTORATE.md` — Central R.D. facility operations, Echo-Cores, and containment wings.
  - `SOMNARAK_SECTOR_WINGS_ARCHITECTURE.md` — 15 canonical sectors across facility topography.

### D. Macro-Chronology & Historical Epochs
- **File:** `CANON_TIMELINE.md`
- **Master Sequence Law:**
  1. **Ante-Dawn Operations (Strictly Pre-Dawn):** Subterranean Expedition Division (SED) -> Underworld Cleanup Descend (UCD) -> The Reverie Directorate (R.D. Facility 01).
  2. **The Watershed Event:** The Dawn of Hope (Year 4,238 Mugenhan Municipal Standard / Cycle 1,778 within R.D.).
  3. **Post-Dawn Frontier Lore:** Unknown Sorrow Entities (UNK SE in `SOMNARAK-WORLD/Unknown_Entities/`), The Horizon Caravan (*Jipyeongseondae*), The Memory Archive (*Gieok Jeojangso*), and The Wound Walkers (Company 4).
- **Cycle Localization Rule:** The 1,778 Mnemonic Cycles belong EXCLUSIVELY to R.D. and The Absolvohan. General municipal records and post-Dawn frontier teams use the **Year 4,238** planetary calendar.

### E. Tactical Combat & Battle Scenarios
- **Directory:** `GAME_BATTLE/`
  - `SCENARIO_01_TO_06.md` — Turn-by-turn combat engagements, containment breaches, and boss encounters.
  - `SCENARIO_REALIZATION_*.md` — Core Meltdown and Floor Realization battles where Department Secretaries awaken their Echo-Cores.

---

## 3. The Five Inviolable Canonical Laws for Writers

```text
+------------------------------------------------------------------------+
|              THE FIVE CANONICAL LAWS FOR SOMNARAK AUTHORS              |
+==========================+=============================================+
| RULE NAME                | OPERATIONAL APPLICATION IN FICTION          |
+==========================+=============================================+
| 1. Macro-Epoch Partition | Ante-Dawn lore strictly proceeds SED ->     |
|                          | UCD -> R.D. All frontier caravans, UNK SEs, |
|                          | and archive descents occur AFTER the Dawn.  |
+------------------------------------------------------------------------+
| 2. Cycle Localization    | The 1,778 Cycles exist ONLY inside R.D.     |
|                          | and Facility 01. The outside world and civic|
|                          | records measure time via Year 4,238.        |
+------------------------------------------------------------------------+
| 3. Two-Work-Type Rule    | Object, Place, and Time entities permit     |
|                          | ONLY Viderehan (Observation) and Ferrehan   |
|                          | (Endurance). Flerehan and Pugnahan are N/A. |
+------------------------------------------------------------------------+
| 4. Planetary Geography   | Macro-features (The Untouched Wild Land,    |
|                          | Untouched Ocean) are planetary geography;   |
|                          | they are NEVER cataloged as Sorrow Entities.|
+------------------------------------------------------------------------+
| 5. Zero PM Terminology   | Use native Somnarak terms: Sorrow Entity,   |
|                          | M.A.W., Echo-Core, Han-Energy, The          |
|                          | Absolvohan, Watches, Ranks I-V, Grades a-w. |
+------------------------------------------------------------------------+
```

---

## 4. Text Box & Table Tooling (`tools/box_formatter.py`)

When generating ASCII dialog boxes, character stat sheets, HUD readouts, or technical ledgers for your story:

- **Reference Architecture:** [TablesGenerator Text Tables](https://www.tablesgenerator.com/text_tables).
- **Target Width:** Exactly **74 columns** (`width=74`) for chatrooms and mobile viewports, or **127/128 columns** for wide-format codices.
- **5-Row Vertical Growth Rule:** Cells expand vertically between 1 and 5 visual sub-rows at word boundaries with zero word slicing or truncation.
- **Python Usage Example:**
  ```python
  from tools.box_formatter import make_table, make_box
  
  # Multi-column grid table
  table = make_table(
      title="OPERATIVE STATUS REPORT",
      headers=["OPERATIVE", "ASSIGNMENT & EQUIPMENT"],
      rows=[
          ["Taeho", "Commander | M.A.W. Set: The Mourning Maul"],
          ["Seiyon", "Echo-Core Analyst | Sector 04 Containment Wing"]
      ],
      width=74
  )
  print(table)
  ```

---

*Project Somnarak Non-Wiki Archive — Curated for Authors, Worldbuilders, and Scenario Directors.*
