# Project Somnarak // Story Writer's Comprehensive Reference Guide
**Archive Package:** [`ARCHIVE/artifacts/PROJECT_SOMNARAK_STORY_REFERENCE_COMPENDIUM.zip`](../../ARCHIVE/artifacts/PROJECT_SOMNARAK_STORY_REFERENCE_COMPENDIUM.zip)  
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
| SOMNARAK-WORLD/          | Complete primary canon: 290 Sorrow Entity   |
|                          | dossiers, 285 quadripartite MAW armory      |
|                          | sets, 45 Master Codices, Cantos 01-06, and  |
|                          | 366-day Absolvohan operational chronicles.  |
+------------------------------------------------------------------------+
| PROJECT_MOON_RESEARCH/   | Exhaustive 16-volume research compendium of |
|                          | Project Moon lore: Abnormalities, 26 Wings, |
|                          | Fixer Offices, E.G.O equipment, and City.   |
+------------------------------------------------------------------------+
| CANON/                   | Comparative analysis and governance: the    |
|                          | 1:1 Somnarak/Lobotomy comparison, the       |
|                          | timeline, and the universal follow rule.    |
+------------------------------------------------------------------------+
| SOMNARAK_GEOLOGY.md      | Planetary geology: The Untouched Wild Lands |
|                          | (UnWiHan), Untouched Ocean, Zone topography |
+------------------------------------------------------------------------+
| GAME_BATTLE/             | Tactical combat simulation: Scenarios 02-06,|
|                          | Boss Realizations, Cycle Engrams, Squads.   |
+------------------------------------------------------------------------+
| REFERENCE_SOMNARAK_WIKI/ | Authorial framework: the R-01 to R-63 rule  |
|                          | register, MAW Variety Design Framework,     |
|                          | chatroom standards, and this style guide.   |
+------------------------------------------------------------------------+
| tools/box_formatter.py   | TablesGenerator reference engine for pure   |
|                          | ASCII text boxes & tables (74 columns).     |
+------------------------------------------------------------------------+
```

---

## 2. Story Writer's Quick Reference Map

When drafting a scene, dialogue, combat sequence, or narrative arc, consult these primary files:

### A. Sorrow Entities (Monsters, Anomalies & Manifestations)
- **Archive Path:** `SOMNARAK-WORLD/Sorrow_Entities/` (290 bespoke files).
- **Format:** Every dossier provides the SECC classification code, Coherence (Ranks I–V), Potency (Grades α–ω), Sorrow Element (Grudge, Resentment, Sorrow, Mourning, Despair), Physical Form, Operational Parameters (valid work types, gauge yields), Combat Record (move names, flavor text, triggers, damage), Appearance, Interaction Records with other entities, and the **Tale (이야기 / Narratio)** and **Testimony (증언 / Testimonium)**.
- **Rule:** Never invent new entities; draw exclusively from the 290 canonical files.

### B. Weapons, Suits, & Relics (M.A.W. Equipment)
- **Archive Path:** `SOMNARAK-WORLD/MAW_Codex_Sets/` (42 numeric registry folders, 285 entity sets, 279 of them filed complete).
- **A set is four files, and three of them are equipment.** The fourth is the record that ties the set to its donor:
  1. **Side Codex (`SE-…-A`):** the donor entity's extraction parameters and the identity the set inherits.
  2. **Weapon (`MAW-W`):** physical manifestation of the entity's tale (Requiem blade, Maul, Fang, Lens).
  3. **Suit (`MAW-S`):** protective attire mitigating specific Sorrow elements (Shroud, Mantle, Plate, Veil).
  4. **Stigma (`MAW-G`):** a wearable relic granted at random on a successful work, never manufactured (Mask, Charm, Lantern, Stone).
- **Three is the number of kinds, and no set has a fourth kind.** There is no pendant, token or trinket slot; a writer who invents one has invented an object class the facility cannot issue.
- **Master Overview:** `SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_MAW_CODEX.md`.

### C. Factions, Corporations, & World Order
- **Master Codices:** `SOMNARAK-WORLD/Master_Codices/` (45 codices in five folders)
  - `SOMNARAK_CORPORATIONS.md` — the Five Sovereign Institutions, the Wings, and their jurisdiction.
  - `SOMNARAK_UNDERWORLD_SYNDICATES.md` — the Five Syndicates of The Raw operating outside the law.
  - `SOMNARAK_SPECIALIST_CADRES.md` — the Ten Specialist Cadres deployed for containment and pacification.
  - `The_REVERIE_DIRECTORATE.md` — central R.D. facility operations, Echo-Cores, containment wings and the sector topography the stories are staged on.

### D. Macro-Chronology & Historical Epochs
- **File:** `CANON/CANON_TIMELINE.md`, mirrored in `SOMNARAK-WORLD/Master_Codices/01_Cosmology_and_World_Order/CANON_TIMELINE.md`
- **Master Sequence Law:**
  1. **Ante-Dawn Operations (Strictly Pre-Dawn):** Subterranean Expedition Division (SED) -> Underworld Cleanup Descend (UCD) -> The Reverie Directorate (R.D. Facility 01).
  2. **The Watershed Event:** The Dawn of Hope (Year 4,238 Mugenhan Municipal Standard / Cycle 1,778 within R.D.).
  3. **Post-Dawn Frontier Lore:** Unknown Sorrow Entities (UNK SE in `SOMNARAK-WORLD/Unknown_Entities/`), The Horizon Caravan (*Jipyeongseondae*), The Memory Archive (*Gieok Jeojangso*), and The Wound Walkers (Company 4).
- **Cycle Localization Rule:** The 1,778 Mnemonic Cycles belong EXCLUSIVELY to R.D. and The Absolvohan. General municipal records and post-Dawn frontier teams use the **Year 4,238** planetary calendar.

### E. Tactical Combat & Battle Scenarios
- **Directory:** `GAME_BATTLE/`
  - `CANONICAL_ENCOUNTER_01_GRIEVING_COLOSSUS.md` and `SCENARIO_02` to `SCENARIO_06` — turn-by-turn combat engagements, containment breaches and boss encounters.
  - `ECHO_CORE_REALIZATION_SYSTEM.md` and `SCENARIO_REALIZATION_FLOOR_02_DEKAN.md` — Core Meltdown and Floor Realization battles where Department Secretaries awaken their Echo-Cores.
  - `CYCLE_ENGRAM_SYSTEM.md`, `BATTLE_SCENARIO_TEMPLATE.md`, and the two squad archetypes — identity attunement on the 1,778 cycles, and the quadripartite suppression team.

### F. Echo-Cores & the Extended Backstory
- **Echo-Core dossiers:** `SOMNARAK-WORLD/Echo_Cores/` — **nine** department heads (Director, Secretary, Containment Lead, Extraction Lead, Research Lead, Border Lead, Archive Lead, Outsider, Exile). These are the people the facility is run by, and the dossiers are their personnel files.
- **Extended backstories:** `SOMNARAK-WORLD/Echo_Cores/Backstory_Extended/` — nine files, `01` through `09`, one per core. These are the story the dossier summarises, not a second dossier: the same life, told at length.
- **Governing standard:** `REFERENCE_SOMNARAK_WIKI/OUT_OF_WORLD/00_BACKSTORY_EXTENDED_STRUCTURE_AND_FORM.md` — time categories, POV, the Connection String, weights and lettering.
- **The working law:** the dossier is the yardstick and the extended file is built from it (`R-57`). If the two disagree, the extended file is wrong.

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
|                          | (Endurance). Flerehan and Pugnahan are      |
|                          | barred: Net-Neutral or Negative-Low.        |
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

## 4. How a Scene Is Written Here

The laws above govern what is true. These govern how it is told. Each one exists because a file
was published without it — the rule numbers are in `REFERENCE_SOMNARAK_WIKI/RULES/`, and each
carries the defect it was written to stop.

### 4.1 A tale has one of four registers (`R-46`)

| Register | What it is | Opens with |
|---|---|---|
| **Story Tale** | a filed account — somebody's job was to write this down | *Filed by* / *Report of*, then a date |
| **Fairy Tale** | the kind of story a district tells about itself | *Once* / *There was* / *Long ago* |
| **Dialogue Story** | a transcript — the story is what was said | *Transcript of* / *Log of*, then a date |
| **Hybrid** | a Story Tale that quotes the people in it | a filing header, then a dated exchange |

The four are not a quality ranking. Which one an entity gets is a fact about the entity. The essay
is not among them.

### 4.2 Dialogue is performed, not reported (`R-24`)

- **Three weights.** Roman is ordinary volume and most lines are roman. *Italic* is dropped volume —
  a whisper, a threat said quietly, the line a speaker does not want carried. **Bold** is raised
  volume — a command over noise, the point where control slips.
- **Five lettering devices, each with a cap.** Caps once per scene, only inside bold, only where the
  room is louder than the speaker. An uneven set (`S e i y o n.`) once per file — a word assembled
  rather than said. Shaky and broken type twice each. Unequal paragraph masses are mandatory: the
  shape of the page is part of the performance.
- **Stack every line.** One speaker, one line, on its own paragraph. Dialogue pressed into a running
  mention (*"she said that the director had agreed and asked whether it would be filed"*) is dialogue
  the reader cannot hear, and it is a defect, not a shortcut.
- **The label is the person or the office, never a costume.** A name is the default; a title alone is
  for a record that holds no name; name-and-title is for the scene that turns on the difference. The
  strike test: remove the titles, and if the scene stops working, the title was load-bearing.

### 4.3 Every scene is stamped (`R-62`)

One line under the heading, before the prose, carrying the distance to the thing the scene counts
toward — in the largest honest unit — and the clock:

```text
> **STAMP — 9 days before [REDACTED] happened · 17:40 · Floor 3, the bench**
```

Where the far end has no date yet, it is written `[REDACTED]` and stays redacted until the story
reaches the midnight before it. **The prose must agree with the stamp it sits between.** A scene
stamped 09:00 and a scene stamped 14:00 are not an hour apart, whatever the paragraph says.

### 4.4 A death belongs to the dying, and a turning point is a scene (`R-58`, `R-60`)

- The person who dies has to have acted, wanted and chosen in their own scenes; a death that only
  happens to someone is furniture. The test is whether you can summarise them in three traits only
  they possess.
- A turn that is narrated is not a turn. If a character changes, the page shows the moment they
  change, in a scene, with a before and an after.

### 4.5 The reader's test — six traps that keep catching us

1. **Do not let a later power leak backwards.** The Director cannot die only from the day of the
   M.A.W. fusion, 63 days after the Solidification. Before that, the medic's warning is a threat and
   not a redundancy — write it as one.
2. **Check the clock against the stamps, not against the feeling of the scene.**
3. **Check every number against itself.** The same night held seventeen hundred iterations in two
   scenes and fifteen hundred in a third; the third was wrong.
4. **Check the count against the people in it.** "Eighteen men" in a scene with a woman officer on
   the channel is a fact error a reader catches in one line.
5. **Check what the file has already done.** A new scene added to a late chapter must deliver what
   the file has not yet delivered, or it re-writes an ending the reader has already been given.
6. **Check that a dossier points at the world, not at the shelf (`R-63`).** A filing inside Somnarak
   cannot cite a filename, a folder path or a section number. Name the record — *the Memory Archive
   holds it* — and let it hold it.

---

## 5. Text Box & Table Tooling (`tools/box_formatter.py`)

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
