# GAME BATTLE — Tactical Combat Operations & Scenario Vault

```text
+---------------------------------------------------------------------+
|        GAME BATTLE OPERATIONS & TACTICAL SIMULATION VAULT           |
+---------------------------------------------------------------------+
| System Code       : SOMNARAK-GBS-TACTICAL-VAULT                     |
| Operational Scope : Turn-Based Combat Encounters & Scenario Scripts |
| Grid Topology     : 10-Node Linear Engagement Corridor ([N01]-[N10])|
| Action Economy    : Speed-Scaled Action Points (AP 2 to 5 per Turn) |
| Core Framework    : Four P-Framework (Passives, Panic, Parry, Poise)|
| Stagger Model     : Dual-Threshold (60% Part Rupture / 0% Meltdown) |
| Phase Rhythm      : 6 Battle Turns = 1 Macro Environmental Phase    |
+---------------------------------------------------------------------+
```

## 1. Introduction: Purpose of the GAME_BATTLE Repository

The `GAME_BATTLE/` directory serves as the root-level operational hub for all tactical combat scenarios, turn-based battle simulations, encounter designs, boss fight specifications, and canonical combat logs within Project Somnarak.

While theoretical combat physics and damage elements are codified in `SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_BATTLE_SYSTEM.md` and `SOMNARAK_BATTLE_SYSTEM_STYLES.md`, and technical implementation architecture is maintained in `SOMNARAK-WORLD/Tactical_Combat_Engine/`, the `GAME_BATTLE/` environment is dedicated to:

1. **Concrete Combat Encounters:** Fully chronicled, turn-by-turn tactical engagements depicting Strike Teams battling Sorrow Entities across all sectors of Somnarak.
2. **Standardized Scenario Authoring:** Establishing the authoritative blueprint, guidelines, and schemas for all future battle `.md` files.
3. **Turn-Based Combat Visualization:** Providing visual 10-node ASCII battle-line topographies that make narrative reading as tactically clear as playing a turn-based tactical RPG.
4. **Balancing & Simulation Benchmarking:** Testing M.A.W. equipment loadouts, elemental affinities, speed bands, and part-dismantling strategies under strict mathematical rules.

---

## 2. Core Battle System Architecture at a Glance

All battle documents authored within `GAME_BATTLE/` must strictly implement the standard **Somnarak Grid Battle System (GBS)**:

```text
+---------------------------------------------------------------------+
|             10-NODE ENGAGEMENT CORRIDOR TOPOGRAPHY                  |
+---------------------------------------------------------------------+
| [N01] [N02] [N03] [N04] [N05] [N06] [N07] [N08] [N09] [N10]         |
| Allied Deployment [N01-03] | Center [N04-06] | Hostile Zone [N07-10]|
| Band 1: Dist 0 (Melee)     | Band 2: Dist 1-2 (Polearm/Shot)        |
| Band 3: Dist 3-4 (Rifle)   | Band 4: Dist 5-6 (Sniper/Artillery)    |
| Band 5: Dist 7+ (Global Acoustic Cannon / Sovereign Resonance)      |
+---------------------------------------------------------------------+
```

### 2.1 The 10-Node Linear Engagement Grid
- Every encounter unfolds along a 10-node discrete spatial axis (`[N01]` to `[N10]`).
- Position dictates Range Bands, flanking bonuses (+25% kinetic damage for pincer formations), and cover effectiveness.
- Moving 1 node costs 1 Action Point (AP). Attempting to move past an active hostile triggers an automatic Opportunity Clash.

### 2.2 Speed Scaling & Action Point Economy
Speed directly determines combat bandwidth per turn:
- **Speed 1 to 2 (Heavy / Fortress):** 2 Action Points per turn.
- **Speed 3 to 4 (Medium / Standard):** 3 Action Points per turn.
- **Speed 5 to 6 (Light / Skirmisher):** 4 Action Points per turn.
- **Speed 7+ (Ultra-Light / Agility Vanguard):** 5 Action Points per turn.

### 2.3 The Four P-Framework
- **P1: Passives (고유 특성):** Automatic conditional triggers from operative background and M.A.W. resonance.
- **P2: Panic / Composure (평정심 · 0 to 100):** Psychological resilience against Lament and Void attacks. At Composure <= 25, Panic triggers. At Composure 0, Terminal Meltdown occurs.
- **P3: Parry / Protection (흘려내기):** Direct clash resolution between opposed attacks in mutual range. Higher roll deflects attack and deals margin as Posture strain.
- **P4: Posture / Poise (자세 유지력 · 0 to 100):** Physical stability against Grudge and Weight trauma. Reaching 0 triggers Posture Break (loss of AP and 1-turn Stagger).

### 2.4 Dual-Threshold Stagger Engine
- **Part Rupture (Tactical Stagger):** Reducing a modular body part below 60% HP disables its associated skills and increases its damage vulnerability to 1.5x for 1 turn.
- **Composure Meltdown (Terminal Stagger):** Reducing Composure to 0 collapses the entire entity for a full phase, forcing 2.0x vulnerability across all parts.

### 2.5 Macro-Phase Structure (6-Turn Combat Cycle)
- Exactly **6 Battle Turns constitute 1 Combat Phase**.
- Turn 06 serves as the high-stakes Phase Climax.
- At Phase-End, the engine evaluates ambient Sorrow Tide (+10% Han saturation), status ticks, and boss stance evolutions.

---

## 3. Directory Inventory & Document Catalog

The `GAME_BATTLE/` directory contains the following foundational operational documents:

| Document File Name | Category & Scope | Description |
|---|---|---|
| [`README.md`](README.md) | Master Index & Overview | Executive summary, core mechanics primer, directory inventory, and architectural roadmap. |
| [`INTRODUCTION_AND_GUIDE.md`](INTRODUCTION_AND_GUIDE.md) | Authoring Guide & Standards | Comprehensive guide for authoring all future `.md` battle files, encounter scripts, and boss mechanics. |
| [`BATTLE_SCENARIO_TEMPLATE.md`](BATTLE_SCENARIO_TEMPLATE.md) | Standardized Production Template | Ready-to-use markdown template with pre-aligned ASCII HUDs, rosters, turn tables, and phase-end blocks. |
| [`CANONICAL_ENCOUNTER_01_GRIEVING_COLOSSUS.md`](CANONICAL_ENCOUNTER_01_GRIEVING_COLOSSUS.md) | Canonical Combat Scenario | Full 6-turn combat engagement demonstrating Strike Team Alpha vs `SE-C-Vδ-002 The Grieving Colossus`. |
| [`SCENARIO_02_CONTAINMENT_BREACH_FLOOR_02.md`](SCENARIO_02_CONTAINMENT_BREACH_FLOOR_02.md) | Canonical Combat Scenario | Full 6-turn containment breach suppression: Dekan's squad vs `SE-N-IVδ-005 The Smothering Mother`. |
| [`SCENARIO_03_UNDERWORLD_RUST_VEIL_PURGE.md`](SCENARIO_03_UNDERWORLD_RUST_VEIL_PURGE.md) | Canonical Combat Scenario | Full 6-turn UCD undercity sweep: Task Force Alpha vs `RIG-FRAY-019 The Slag-Forged Breaker`. |
| [`SCENARIO_04_SED_SUNKEN_AQUEDUCT_DESCENT.md`](SCENARIO_04_SED_SUNKEN_AQUEDUCT_DESCENT.md) | Canonical Combat Scenario | Full 6-turn SED deep-karst descent: Vanguard Cadre vs `SECC-012 The Drowned Guardian`. |
| [`SCENARIO_05_HORIZON_CARAVAN_LEVIATHAN_SIEGE.md`](SCENARIO_05_HORIZON_CARAVAN_LEVIATHAN_SIEGE.md) | Canonical Combat Scenario | Full 6-turn Horizon Caravan defense: Drift Throne vs `SECC-088 The Titanic Glass Burrower`. |
| [`SCENARIO_06_MEMORY_ARCHIVE_STRATUM_REALIZATION.md`](SCENARIO_06_MEMORY_ARCHIVE_STRATUM_REALIZATION.md) | Canonical Combat Scenario | Full 6-turn Floor 04 Realization: Seiyon & Suture Cadre vs `The Weeping Statue` (Lament Core). |
| [`BOSS_MECHANICS_GRIEVING_COLOSSUS.md`](BOSS_MECHANICS_GRIEVING_COLOSSUS.md) | Sovereign Boss Mechanics Folio | Quadripartite modular anatomy, 3-phase tectonic shifts, AI intention deck, and M.A.W. synthesis for `SE-C-Vδ-002`. |
| [`CYCLE_ENGRAM_SYSTEM.md`](CYCLE_ENGRAM_SYSTEM.md) | Identity Attunement Framework | Canonical 1,778-cycle historical engrams modifying Speed Bands, Action Slots, and P1 Passives across operatives. |
| [`ECHO_CORE_REALIZATION_SYSTEM.md`](ECHO_CORE_REALIZATION_SYSTEM.md) | Departmental Realization Wars | Four-phase psychological catharsis engine, Sorrow Inversion meltdowns, dialogue scripts, and sovereign engrams. |

---

## 4. Master Roadmap for Future `.md` Files

The following battle scenarios, boss mechanics folios, and squad guides are slated for addition to `GAME_BATTLE/`:

### 4.1 High-Priority Scenario Documents (`SCENARIO_*.md`)
1. `SCENARIO_02_CONTAINMENT_BREACH_FLOOR_02.md`: [COMPLETED] Facility 01 Floor 2 containment breach suppression featuring Dekan's suppression squad clashing with `SE-N-IVδ-005 The Smothering Mother`.
2. `SCENARIO_03_UNDERWORLD_RUST_VEIL_PURGE.md`: [COMPLETED] UCD Operation 1 tactical sweep in the undercity slums, deploying Breacher units against syndicate Fray constructs.
3. `SCENARIO_04_SED_SUNKEN_AQUEDUCT_DESCENT.md`: [COMPLETED] Katabagil Passage 1 deep-abyss subterranean encounter against pressure-adapted feral Sorrow Beasts.
4. `SCENARIO_05_HORIZON_CARAVAN_LEVIATHAN_SIEGE.md`: [COMPLETED] Trans-Desolate overland defense of the Drift Throne crawler against a migrating River Leviathan at the Glass Sands.
5. `SCENARIO_06_MEMORY_ARCHIVE_STRATUM_REALIZATION.md`: [COMPLETED] Floor 4 Mnemonic Reception clash utilizing Mnemonic Suture mechanics and Floor Realization phases.

### 4.2 Boss Mechanics Folios (`BOSS_MECHANICS_*.md`)
1. `BOSS_MECHANICS_GRIEVING_COLOSSUS.md`: [COMPLETED] Modular part profiles (Stone Head, Left Knee, Right Knee, Basalt Core), intention deck behaviors, and Phase 2 tectonic shifts.
2. `BOSS_MECHANICS_WEEPING_MIRROR.md`: Reflection duplication mechanics, Lament aura drain, and mirror-shatter execution phases.
3. `BOSS_MECHANICS_KING_OF_MENDERS.md`: Syndicate flesh-welding mechanics, debt-mark stacking, and multi-node tether traps.

### 4.3 Squad Archetype & Doctrine Manuals (`SQUAD_*.md`)
1. `SQUAD_ARCHETYPE_REVERIE_CONTAINMENT.md`: Standard 4-warden Facility 01 loadout (Vanguard Shield, Acoustic Siphon, Core Striker, Cryo-Anchor).
2. `SQUAD_ARCHETYPE_UCD_PACIFICATION.md`: Heavy kinetic and breach-loadout configurations for close-quarters undercity pacifications.

---

## 5. Technical Authoring Rules & Quality Standards

Every markdown document in `GAME_BATTLE/` must adhere to the immutable technical standards of Project Somnarak:

1. **Strict Monospace ASCII Box Symmetry:**
   - All ASCII HUDs and battlefield topographies must be enclosed in non-markdown code fences (````text ... ````).
   - Standard boxes must measure exactly 71 columns (`+` + 69 `-` + `+`).
   - Wide-format boxes must measure exactly 127 or 128 columns per `TEST_TEXT_BOX_WIDTHS.md`.
   - Every border must start and terminate symmetrically with `+` or `|`. Zero crooked rows permitted.
2. **Zero Forbidden Formatting Tags:**
   - Absolute prohibition against raw HTML line-break tags.
   - Absolute prohibition against LaTeX math dollar signs.
3. **100% In-Universe Canonical Voice:**
   - Written strictly from the perspective of Reverie Directorate tactical evaluators, combat analysts, and field commanders.
   - Zero out-of-universe meta-commentary, zero self-reflection, and zero developer introspection.
4. **Native Somnarak Terminology Only:**
   - Sorrow Entities (never Abnormalities), SECC codes, Coherence Ranks I to V, Potency Grades α to ω.
   - M.A.W. Weapons, Suits, and Gifts (never E.G.O).
   - Composure and Meltdown (never Sanity and Distortion).
   - Wardens, Enforcers, Custodians, Keepers, and Surveyors (never Fixers).

---

**Directory Code:** `DIR-GAME-BATTLE-001`  
**Supervising Wing:** Reverie Directorate Tactical Simulation Division  
**Operational Status:** Active Canonical Combat Archive
