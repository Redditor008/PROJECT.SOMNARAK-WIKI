# GAME BATTLE — Canonical Introduction & Future Authoring Guide
## Tactical Combat Engine Standard Operating Procedure (SOP)

```text
+---------------------------------------------------------------------+
|        GAME BATTLE SUITE — MASTER INTRODUCTION & AUTHORING GUIDE    |
+---------------------------------------------------------------------+
| Standard Code     : SOP-GB-DOC-AUTHORING-001                        |
| Authority         : Reverie Directorate Tactical Simulation Bureau  |
| Classification    : Unrestricted Operational Combat Standard        |
| Target Format     : Pure Markdown (.md) with Monospace ASCII HUDs   |
| Width Benchmark   : 71 Columns Compact / 127-128 Columns Extended   |
| Mathematical Law  : Deterministic Arithmetic / Zero Dollar Signs    |
| Vocabulary Law    : 100% Authentic Somnarak Native Nomenclature     |
+---------------------------------------------------------------------+
```

## 1. Executive Introduction: The Mission of the GAME_BATTLE Environment

The `GAME_BATTLE/` directory is the canonical repository for tactical combat documentation, playable encounter simulations, and narrative battle chronicles within Project Somnarak.

In traditional game design and narrative archives, combat mechanics often exist as abstract rulebooks detached from the narrative prose. The `GAME_BATTLE/` suite bridges this divide: **every battle file is both a rigorous mathematical simulation and an immersive, turn-by-turn narrative chronicle**.

By combining the **10-Node Linear Engagement Grid**, **Speed-to-Action Point economies**, **the Four P-Framework (Passives, Panic, Parry, Poise)**, and **dual-threshold staggers (modular part ruptures and composure meltdowns)**, battles in Somnarak read with the tactical precision of a high-stakes turn-based tactical RPG.

This guide establishes the binding architectural requirements, section anatomy, mathematical formulas, and formatting rules that every future `.md` file in `GAME_BATTLE/` must follow.

---

## 2. Document Taxonomy: Four Classes of Battle Files

Future contributors and automated systems authoring documents within `GAME_BATTLE/` must categorize each new file into one of four standardized classes:

```text
+---------------------------------------------------------------------+
|             GAME BATTLE DOCUMENT TAXONOMY & CLASSIFICATION          |
+---------------------------------------------------------------------+
| Class 1: Tactical Scenarios  | Prefix: SCENARIO_*.md                |
| Class 2: Boss Mechanics      | Prefix: BOSS_MECHANICS_*.md          |
| Class 3: Squad Archetypes    | Prefix: SQUAD_ARCHETYPE_*.md         |
| Class 4: Faction Directives  | Prefix: FACTION_BATTLE_*.md          |
+---------------------------------------------------------------------+
```

### Class 1: Tactical Scenarios (`SCENARIO_*.md` or `BATTLE_*.md`)
- **Focus:** Complete, chronological turn-by-turn combat engagements between a specific operative squad and hostile entities.
- **Rhythm:** Standard encounters span 1 to 2 Combat Phases (6 to 12 Battle Turns).
- **Deliverables:** Step-by-step initiative rolls, node movements, clash resolutions, part damage, stagger triggers, and after-action logs.

### Class 2: Boss Mechanics & Phase Folios (`BOSS_MECHANICS_*.md`)
- **Focus:** Technical design documents for Rank IV Entities and Rank V Sovereigns.
- **Components:** Modular body part anatomies (Head, Limbs, Core), hit point pools, rupture thresholds, elemental resistance matrices, AI intention decks, and multi-phase stance evolution triggers.

### Class 3: Strike Team Archetypes & Builds (`SQUAD_ARCHETYPE_*.md`)
- **Focus:** Optimized 4-person operative tactical team compositions.
- **Components:** Assigned wings, role distribution (Vanguard, Striker, Acoustic Controller, Anchor), M.A.W. Wear Grade pairings (Weapons, Suits, Gifts), passive synergies, and range band coverage.

### Class 4: Faction Combat Directives (`FACTION_BATTLE_*.md`)
- **Focus:** Institutional combat styles and field doctrines.
- **Varieties:** Reverie Directorate containment tactics, SED subterranean depth-pressure survival, UCD urban CQB part dismantling, Memory Archive mnemonic suture clashing, and Horizon Caravan trans-desolate bastion warfare.

---

## 3. Mandatory Structural Anatomy of a Battle File

Every combat scenario document authored in `GAME_BATTLE/` must contain the following seven canonical sections in exact order:

```text
+---------------------------------------------------------------------+
|             SEVEN MANDATORY SECTIONS OF A BATTLE DOCUMENT           |
+---------------------------------------------------------------------+
| Section 1: Standard Tactical Header HUD (71-Col ASCII Block)        |
| Section 2: Engagement Context & Environmental Setting               |
| Section 3: Combatant Rosters & Loadout Specifications               |
| Section 4: Initial 10-Node Grid Topography Map                      |
| Section 5: Turn-by-Turn Operational Chronicle (Turns 01 to 06)      |
| Section 6: Macro Phase-End Resolution Block                         |
| Section 7: After-Action Report & Extraction Manifest                |
+---------------------------------------------------------------------+
```

### Section 1: Standard Tactical Header HUD
Every document opens with a standardized 71-column monospace ASCII header block identifying the battle code, location, threat level, participating operatives, and hostile target:

```text
+---------------------------------------------------------------------+
| TACTICAL ENGAGEMENT RECORD: BATTLE-001-GRIEVING-COLOSSUS            |
+---------------------------------------------------------------------+
| Operational Area  : Zone B Maw Perimeter (Subterranean Depth -450m) |
| Threat Rating     : Rank V Sovereign (Grade δ Potency)              |
| Strike Team       : Strike Team Alpha (Reverie Directorate)         |
| Squad Strength    : 4 Operatives (Taeho, Seol-A, Min-Jae, Ha-Eun)   |
| Primary Objective : Part Dismantling & Composure Meltdown Extraction|
+---------------------------------------------------------------------+
```

### Section 2: Engagement Context & Environmental Setting
- **Geographic & Sector Coordinate:** Exact metropolitan zone (Zones A to E) or subterranean strata.
- **Ambient Han Saturation:** Environmental grief density (measured in percentages, e.g., 35% ambient saturation).
- **Hazard Modifiers:** Low visibility, acoustic reverberation, falling rubble, caustic weeping puddles, or sandstorms.

### Section 3: Combatant Rosters & Loadout Specifications
Both allied operatives and hostile entities must be cataloged with their exact numerical profiles:
- **Operatives (4 Units):**
  * Name, Callsign, Role.
  * Base Speed, Maximum Health, Composure Pool (0–100), Posture Pool (0–100).
  * Equipped M.A.W. Triad: Weapon (Wear Grade, Damage Element, Range Band), Suit (Resistances), Gift (Passive).
- **Hostile Entity:**
  * SECC Code, Canonical Name, Coherence Rank (I to V), Potency Grade (α to ω).
  * Total Composure Pool (0 to 100+), Meltdown Threshold.
  * Modular Body Parts: Part Name, HP Pool, Rupture Threshold (60% of Max HP), Part Resistance Matrix.
  * Intention Deck: Attack skills, targeting priorities, AP cost, Range Bands.

### Section 4: Initial 10-Node Grid Topography Map
Render the starting battlefield layout using the canonical 10-node ASCII map:

```text
+---------------------------------------------------------------------+
|                 INITIAL 10-NODE GRID TOPOGRAPHY                     |
+---------------------------------------------------------------------+
| [N01]   [N02]   [N03]   [N04]   [N05]   [N06]   [N07]   [N08]  ...  |
| [HA-EUN][MIN-J] [TAEHO] [SEOL-A][BARRIER]----   [COLOSSUS BODY]     |
| Vanguard Bastion [N01-03] | Center [N04-06] | Hostile Zone [N07-10] |
+---------------------------------------------------------------------+
```

### Section 5: Turn-by-Turn Operational Chronicle
For each Battle Turn (Turns 01 through 06):
1. **Initiative & AP Allocation:** Tabulate each unit's rolled Speed and resulting Action Points.
2. **Movement & Node Shifts:** Document any operative or enemy repositioning, along with AP expenditures.
3. **Clash & Parry Resolutions:** Detail opposed skill rolls, margin calculations, and Posture strain.
4. **Damage & Rupture Tracking:** Calculate kinetic/elemental damage dealt, check against the 60% Part Rupture threshold, and update remaining hit points.
5. **Composure & Meltdown Tracking:** Record psychological erosion from Lament/Void attacks and track remaining Composure points.

### Section 6: Macro Phase-End Resolution Block
After Turn 06 (and Turn 12/18 in extended encounters):
- **Sorrow Tide Check:** Increase ambient Han saturation by +10%.
- **Status Effect Ticks:** Apply lingering Bleed, Corrosion, or Weeping stacks.
- **Boss Stance Transition:** Document if the boss crossed an HP threshold and shifts into an enraged or defensive stance.

### Section 7: After-Action Report & Extraction Manifest
- **Engagement Outcome:** Decisive Victory, Tactical Withdrawal, or Mutual Stagger.
- **Harvest Manifest:** Amount of crystallized Han dust recovered (in kg), M.A.W. extraction yields (Weapons, Suits, Gifts).
- **Squad Casualties:** Physical wounds sustained, Composure restoration time, and medical triage status.

---

## 4. Core Mathematical Formulas & Mechanics Reference

All calculations within battle files must utilize clean, deterministic arithmetic:

```text
+---------------------------------------------------------------------+
|             CANONICAL COMBAT FORMULAS & ARITHMETIC LAWS             |
+---------------------------------------------------------------------+
| Distance Formula  : Distance = |Node_Source - Node_Target|          |
| Damage Equation   : Dmg = Base_Dmg * Skill_Mult * Resist_Mult * Stag|
| Clash Resolution  : Margin = Ally_Clash_Roll - Hostile_Clash_Roll   |
| Pincer Formation  : +25% Bonus Kinetic Damage when Flanking         |
| Part Rupture      : Triggers when Part HP <= 60% of Max HP          |
| Terminal Meltdown : Triggers when Total Composure == 0              |
+---------------------------------------------------------------------+
```

### 4.1 Node Distance & Range Band Validation
- Point-Blank (Band 1): Distance = 0 (same node or directly adjacent).
- Short Range (Band 2): Distance = 1 to 2 nodes.
- Medium Range (Band 3): Distance = 3 to 4 nodes.
- Long Range (Band 4): Distance = 5 to 6 nodes.
- Global Siege (Band 5): Distance = 7+ nodes.

### 4.2 Speed-to-AP Conversion
- Speed 1 to 2: 2 Action Points.
- Speed 3 to 4: 3 Action Points.
- Speed 5 to 6: 4 Action Points.
- Speed 7+: 5 Action Points.

### 4.3 Stagger Vulnerability Multipliers
- Standard State: 1.0x damage taken.
- Part Ruptured State: 1.5x damage taken on the ruptured modular part.
- Terminal Meltdown State: 2.0x damage taken across all body parts.

---

## 5. Technical Formatting & Quality Laws

Authors and agents must strictly observe the four quality laws of the Somnarak repository:

1. **Monospace ASCII Box Symmetry:**
   - Every ASCII HUD must be enclosed in non-markdown code fences (````text ... ````).
   - Compact boxes must have a width of exactly 71 columns (`+` + 69 `-` + `+`).
   - Extended wide-format boxes must have a width of exactly 127 or 128 columns per `TEST_TEXT_BOX_WIDTHS.md`.
   - Every line must start with `+` or `|` and terminate with `+` or `|`. Zero crooked rows.
2. **Zero Forbidden Formatting Tags:**
   - No raw HTML line-break tags.
   - No LaTeX math dollar signs.
3. **100% In-Universe Perspective:**
   - Author files as classified municipal defense records, tactical after-action reviews, or field combat telemetry.
   - Do not include conversational meta-commentary ("In this file, we will show...").
4. **Native Somnarak Nomenclature Only:**
   - Use Sorrow Entities (never Abnormalities), SECC codes, Coherence Ranks I to V, Potency Grades α to ω.
   - Use M.A.W. equipment (never E.G.O).
   - Use Composure and Meltdown (never Sanity and Distortion).
   - Use Wardens, Enforcers, Custodians, Keepers, and Surveyors (never Fixers).

---

## 6. Pre-Commit Verification Checklist

Before committing any new `.md` battle document to `GAME_BATTLE/`:

- [ ] File name follows convention (`SCENARIO_*.md`, `BOSS_MECHANICS_*.md`, `SQUAD_*.md`).
- [ ] Contains all seven mandatory sections in proper sequence.
- [ ] All ASCII HUDs wrapped in ````text ... ```` code fences.
- [ ] Ran `python3 tools/check_box_symmetry.py` (0 errors reported).
- [ ] Ran `python3 tools/text_box_double_checker.py` (0 errors reported).
- [ ] Ran `python3 tools/audit_lore_archive.py` (100% PASS).
- [ ] Verified zero raw HTML line-break tags and zero LaTeX math dollar signs.
- [ ] Staged and committed in the same turn per Owner Rule A0 (Push Always).

---

**Guide Standard Code:** `SOP-GB-001`  
**Issuing Authority:** Reverie Directorate Tactical Simulation Bureau  
**Status:** Canonical Authoring Directive
