import re

# 1. Update docs/README.md and docs/FRONT_HOME_PAGE_SPECIFICATION.md
readme_path = "docs/README.md"
spec_path = "docs/FRONT_HOME_PAGE_SPECIFICATION.md"

content = """# /docs ARCHITECTURE & FRONT HOME PAGE PORTAL SPECIFICATION
## MASTER ENTRYWAY BLUEPRINT: WIKI · STORY · GAME · GAME WIKI · COLLECTION
### GITHUB PAGES PUBLISHING ROOT: `docs/index.html`

```text
+========================================================================+
|             PROJECT SOMNARAK // DOCS FRONT PORTAL BLUEPRINT            |
+========================================================================+
| Document Purpose     | Architecture Specification for /docs Root       |
| Primary Artifact     | docs/index.html (Brand New Master Front Page)   |
| Core Role            | Central Gateway & Hub Navigation Nexus          |
| Canonical Sources    | STRICTLY & EXCLUSIVELY TWO ROOT REPOSITORIES:   |
|                      | 1. SOMNARAK-WORLD                               |
|                      | 2. GAME_BATTLE                                  |
| Five Master Pillars  | 1. WIKI (Comprehensive Setting & Lore Codex)    |
|                      | 2. STORY (Chronicles, Cantos & Cycle Records)   |
|                      | 3. GAME (10-Node Grid & Tactical Simulation)    |
|                      | 4. GAME WIKI (P.M. Wiki.gg / Fandom Style Wiki) |
|                      | 5. COLLECTION (Entities, MAW Armory & Relics)   |
| Visual Identity      | Subterranean Industrial Baroque & Han Resonance |
| Live Target          | GitHub Pages Publish Root (/docs)               |
+========================================================================+
```

---

## 1. EXECUTIVE VISION & RE-ARCHITECTURAL DIRECTIVE

The `/docs` directory serves as the public **GitHub Pages publishing root** for Project Somnarak. Under the updated architecture, `docs/index.html` is established as the **Master Front Home Page**—an immersive, high-impact grand portal gateway (  초대형 포털 대문  , *Chodaehyeong Poteol Daemun*) that welcomes visitors, researchers, operatives, and players into the Project Somnarak universe.

### Strict Canonical Data Source Mandate
All content, mechanics, lore, scenarios, and navigation links within the `/docs` ecosystem are derived strictly and exclusively from two primary repositories:
1. **`SOMNARAK-WORLD`**: The master archive containing the 292 Sorrow Entity dossiers, MAW armory sets, cosmology, cantos, organizations, and municipal codices.
2. **`GAME_BATTLE`**: The tactical combat and simulation archive containing 10-node grid battle scenarios, boss mechanics, cycle engrams, and realization systems.

No external or temporary sandbox directories are referenced.

```text
                                              [ docs/index.html ]
                                         BRAND NEW MASTER FRONT PAGE
                                                      |
       +--------------------+-------------------------+-------------------------+--------------------+
       |                    |                         |                         |                    |
       v                    v                         v                         v                    v
 [ 1. WIKI HUB ]     [ 2. STORY HUB ]          [ 3. GAME HUB ]        [ 4. GAME WIKI HUB ]   [ 5. COLLECTION HUB ]
  - World Lore        - Story Cantos 01-06     - 10-Node Spatial Grid  - P.M. Wiki.gg/Fandom  - 292 Sorrow Entities
  - SECC Codices      - 1,778 Cycle Logs       - Tactical Scenarios    - L Corp Management    - 287+ SVG Weapons
  - Factions/Cadres   - Echo-Core Realize      - Boss Mechanics        - LoR Combat Decks     - Tool Relic Dossiers
  - Comparative Text  - Operator Incident Logs - Squad Archetypes      - Limbus Sin Database  - Blueprint Schematics
  (SOMNARAK-WORLD)    (SOMNARAK-WORLD)         (GAME_BATTLE)           (P.M. / GAME_BATTLE)   (SOMNARAK-WORLD)
```

---

## 2. THE FIVE MASTER PILLARS

```text
+========================================================================+
|                       THE FIVE CORRIDOR GATEWAYS                       |
+========================================================================+
| Gateway Pillar       | Primary Domain & In-Universe Manifestation      |
+======================+=================================================+
| 1. WIKI              | The Scholarly Lore & Codices (SOMNARAK-WORLD)   |
| 2. STORY             | The Dramaturgical Story Cantos (SOMNARAK-WORLD) |
| 3. GAME              | Tactical Scenarios & Engine (GAME_BATTLE)       |
| 4. GAME WIKI         | P.M. Wiki.gg & Fandom Style Game Mechanics Wiki |
| 5. COLLECTION        | Specimen Archives & Armory (SOMNARAK-WORLD)     |
+========================================================================+
```

### Pillar I: The WIKI Hub (  위키 허브  , *Wiki Heobeu*)
- **Source:** `SOMNARAK-WORLD/Master_Codices/`
- **Core Focus:** Comprehensive setting encyclopedia, mechanical reference codices, administrative architecture, and comparative world studies.
- **Key Modules & Routes:**
  1. **Cosmology & Geography:** Detailed documentation of Somnarak City (  솜나락 도성  ), The Raw (  생경  ), The Desolate (  황무지  ), and the subterranean strata.
  2. **The Reverie Directorate & The Absolvohan:** Departmental structures, administrative protocols, Floor Secretaries 01 through 10, Salt-Scrubbers, and the Dekan's High Command (`SOMNARAK-WORLD/The_Absolvohan/`).
  3. **SECC Classification Codex:** Canonical decoding rules for Designation codes, Coherence tiers (I to V), Potency ranks (α to ω), Sorrow Categories, and Elemental affinities.
  4. **Organizations & Factions:** The High Council, The Giltong arbiters, the 5 Syndicates of The Raw (The Menders, Rust Frays, Veil Merchants, Memory Washers, Debt Concourse), and the 10 Specialist Cadres.
  5. **Comparative Codex:** The 19-section master comparative treatise analyzing 1-to-1 mechanical, narrative, and philosophical equivalents between Project Somnarak and Lobotomy Corporation / Project Moon.

### Pillar II: The STORY Hub (  서사 허브  , *Seosa Heobeu*)
- **Source:** `SOMNARAK-WORLD/Story_Cantos/`
- **Core Focus:** Canonical narratives, historical cycle logs, character psychologies, and field operation books.
- **Key Modules & Routes:**
  1. **Canonical Story Cantos (01 through 06):**
     - Canto 01: The Bastion Anchor (Min-Jae)
     - Canto 02: The Acoustic Void (Seol-A)
     - Canto 03: The Shattered Striker (Taeho)
     - Canto 04: The Sub-Zero Ridge (Ha-Eun)
     - Canto 05: Suture of Lost Pages (Seiyon)
     - Canto 06: The Slum Breacher (Kang)
  2. **The 1,778 Mnemonic Cycles:** Chronicled logs of past cycle resets, the accumulation of ancestral Han across centuries, and the tragic recurring loops of the facility.
  3. **Echo-Core Resonant Realization Wars:** The 4-phase psychological boss battles where operatives descend into core trauma (Lament, Grudge, Weight, Void) to achieve harmonic enlightenment (`SOMNARAK-WORLD/Echo_Cores/`).
  4. **Character Dossiers & Records:** The psychological profiles of The Dekan, Arch-Liaisons, and fallen operatives.

### Pillar III: The GAME Hub (  게임 허브  , *Geim Heobeu*)
- **Source:** `GAME_BATTLE/`
- **Core Focus:** Interactive playable tactical combat simulation, scenario encounters, and tactical battle mechanics.
- **Key Modules & Routes:**
  1. **Canonical Encounter Scenarios:**
     - Scenario 01: Canonical Encounter - Grieving Colossus (`GAME_BATTLE/CANONICAL_ENCOUNTER_01_GRIEVING_COLOSSUS.md`)
     - Scenario 02: Containment Breach Floor 02 (`GAME_BATTLE/SCENARIO_02_CONTAINMENT_BREACH_FLOOR_02.md`)
     - Scenario 03: Underworld Rust Veil Purge (`GAME_BATTLE/SCENARIO_03_UNDERWORLD_RUST_VEIL_PURGE.md`)
     - Scenario 04: SED Sunken Aqueduct Descent (`GAME_BATTLE/SCENARIO_04_SED_SUNKEN_AQUEDUCT_DESCENT.md`)
     - Scenario 05: Horizon Caravan Leviathan Siege (`GAME_BATTLE/SCENARIO_05_HORIZON_CARAVAN_LEVIATHAN_SIEGE.md`)
     - Scenario 06: Memory Archive Stratum Realization (`GAME_BATTLE/SCENARIO_06_MEMORY_ARCHIVE_STRATUM_REALIZATION.md`)
  2. **Boss Mechanics Specifications:**
     - Boss Mechanics: Grieving Colossus (`GAME_BATTLE/BOSS_MECHANICS_GRIEVING_COLOSSUS.md`)
     - Boss Mechanics: King of Menders (`GAME_BATTLE/BOSS_MECHANICS_KING_OF_MENDERS.md`)
     - Boss Mechanics: Weeping Mirror (`GAME_BATTLE/BOSS_MECHANICS_WEEPING_MIRROR.md`)
  3. **Combat Systems & Squad Archetypes:**
     - 10-Node Spatial Grid Combat Rules (`GAME_BATTLE/INTRODUCTION_AND_GUIDE.md`)
     - Cycle Engram System (`GAME_BATTLE/CYCLE_ENGRAM_SYSTEM.md`)
     - Echo-Core Realization System (`GAME_BATTLE/ECHO_CORE_REALIZATION_SYSTEM.md`)
     - Squad Archetype: Reverie Containment (`GAME_BATTLE/SQUAD_ARCHETYPE_REVERIE_CONTAINMENT.md`)
     - Squad Archetype: UCD Pacification (`GAME_BATTLE/SQUAD_ARCHETYPE_UCD_PACIFICATION.md`)

### Pillar IV: The GAME WIKI Hub (  게임 위키 허브  , *Geim Wiki Heobeu*)
- **Source:** `docs/game-wiki/index.html` (synthesizing `GAME_BATTLE/` and `SOMNARAK-WORLD/` with canonical Project Moon mechanics)
- **Core Focus:** Comprehensive mechanical gameplay encyclopedia modeled directly after the **Project Moon Wikis** across **wiki.gg** and **Fandom** (`lobotomycorporation.wiki.gg`, `libraryofruina.wiki.gg`, `limbuscompany.wiki.gg`), providing exhaustive formulas, card databases, stat matrices, and combat calculators cross-referenced with Somnarak game systems.
- **Key Modules & Routes:**
  1. **Lobotomy Corporation Game Database (Management Simulation):**
     - **Abnormality Work Matrix:** Fortitude (Instinct), Prudence (Insight), Temperance (Attachment), Justice (Repression) success formulas.
     - **Energy & Box Formulas:** PE-Box and NE-Box generation rates, daily quotas, and Work speed multipliers.
     - **Qliphoth Mechanics:** Meltdown levels I through X, Qliphoth Overload penalties, and Cliphoth Counter triggers.
     - **Ordeal Survival Manuals:** Dawn, Noon, Dusk, and Midnight of Green, Amber, Crimson, and Violet.
     - **Sephirah Meltdown Guides:** Step-by-step suppression strategies for Asiyah, Briah, and Atziluth floor meltdowns (Malkuth to Keter).
     - **E.G.O Equipment Index:** Full stats for Weapons, Suits, and Gifts across ZAYIN, TETH, HE, WAW, and ALEPH tiers.
     - **Tool Abnormality Codices:** Continuous, Single-Use, and Equippable operational logs and lethal failure conditions.
  2. **Library of Ruina Game Database (Deckbuilding Tactical Dice Battle):**
     - **Key Page Catalog & Attribution Guide:** Passive transfer mechanics, cost optimization, Slash/Pierce/Blunt/Block/Evade dice power boosts.
     - **Combat Page Compendium:** 0-cost to 4-cost page curves, dice types, On Hit, Clash Win, and Clash Lose card effects.
     - **Speed Dice & Clashing Engine:** Speed rolls, target redirection, clash win formulas, and power stacking calculations.
     - **Stagger & Resistances:** Stagger thresholds, damage vulnerabilities (Fatal, Weak, Normal, Endured, Ineffective), and recovery formulas.
     - **Emotion Level System:** Emotion Levels 0 to V, positive/negative Emotion Coins, light recovery, and maximum light expansion.
     - **Floor Realization Boss Strategy Guides:** 4-phase and 5-phase realization walkthroughs for all 10 Library floors.
     - **E.G.O Awakening & Distortion Pages:** Awakening page drafting, synchronization modes, and passive perks.
  3. **Limbus Company Game Database (Sin Resonance Strategic RPG):**
     - **12 Sinners & Identity Matrix:** Base, 00, and 000 ID ratings, Uptie I to IV upgrades, Threadspinning, and stat growths.
     - **Coin Power Mechanics:** Base Power, Plus Coins, Minus Coins, Coin count, Clash Win formulas, and Damage calculation.
     - **Sanity (SP) Formula Engine:** -45 to +45 scale, coin flip heads probability `(50% + SP%)`, Panic triggers, and Corroded skill behaviors.
     - **Sin Affinities & Resonance Matrix:** Wrath, Lust, Sloth, Gluttony, Gloom, Pride, Envy; 3+ Sin Resonance and Absolute Resonance damage amplifiers.
     - **Keyword Status Effects:**
       * Burn (Potency / Count decay mechanics)
       * Bleed (Clash coin interaction and bleed tick math)
       * Tremor (Burst, Decay, Reverberation, Everlasting, Fracture stagger raise)
       * Rupture (Hit-count depletion and true damage calculation)
       * Sinking (SP depletion vs. Gloom affinity damage against SP-less targets)
       * Poise (Critical strike chance and critical damage scaling)
       * Charge (Count generation, barrier preservation, and tier-spending thresholds)
     - **Mirror Dungeon & Refraction Railway Compendium:** Event outcome tables, E.G.O Gift fusion recipes, pack prioritization, and turn-count optimization.
  4. **Project Somnarak Game Systems & Mechanics Engine:**
     - **10-Node Grid Tactical Formulas:** Spatial distance penalties, flanking bonuses, push/pull knockback meters, and AoE node coverage (derived from `GAME_BATTLE/`).
     - **Speed & Action Slot Progression:** Turn-by-turn action slot formulas, initiative clashes, and 6-turn combat phase resolution.
     - **Han Pressure (ATK) vs. Sorrow Gauge (HP):** Offense and defense level discrepancies, stagger threshold calculations, and damage resistance math.
     - **Containment Work Percentages:** Rigorous probability tables for Viderehan, Ferrehan, Flerehan, Pugnahan across Ranks I to V and Potencies α to ω.
     - **Two-Work-Type Rule Database:** Strict enforcement index verifying all 131 Non-Subject entities (Object, Place, Time) with Flerehan and Pugnahan set to N/A.
     - **Grade 1 to 5 Workshop Forging Matrix:** Material requirements, Han-ore refinement, and verified drop probabilities (Grade 5 Legendary: 0.5%, Grade 4: 1.0%, Grade 3: 5.0%).
     - **M.A.W. Equipment Stat Catalog:** 287+ SVG weapon profiles, defensive suits, and charms with elemental damage resistance values (`SOMNARAK-WORLD/MAW_Codex_Sets/`).
     - **Unified PM-to-Somnarak System Translation Matrix:** 1-to-1 mechanic converter bridging L Corp / LoR / Limbus terms directly to Somnarak operational equivalents.

### Pillar V: The COLLECTION Hub (  수집 허브  , *Sujip Heobeu*)
- **Source:** `SOMNARAK-WORLD/Sorrow_Entities/` & `SOMNARAK-WORLD/MAW_Codex_Sets/`
- **Core Focus:** Curated specimen archives, visual art assets, hardware showcases, and audio vaults.
- **Key Modules & Routes:**
  1. **The 292 Sorrow Entity Master Vault:** Complete individual dossiers for all 292 Sorrow Entities, containing verified Core Stat Lines, Tales, Appearances, and Breach Behaviors (`SOMNARAK-WORLD/Sorrow_Entities/`).
  2. **The M.A.W. Armory (287+ SVG Weapons):** Hand-crafted vector silhouettes for every single weapon in the registry, showcasing custom blades, fangs, mauls, lenses, clocks, and relics in batch-1 chrome finish (`SOMNARAK-WORLD/MAW_Codex_Sets/`).
  3. **Relic-Entity / Tool Abnormality Catalog:** The 131 non-subject artifacts categorized by operational profile (Single-Use, Equippable, Continuous) with tiered Log & Method unlock tables.
  4. **Architectural Blueprints:** `SOMNARAK_CITY_LAYOUT.svg` and `THE_HAND_DR_LAYOUT.svg`.

---

## 3. TECHNICAL SPECIFICATIONS FOR `docs/index.html`

```text
+========================================================================+
|                 FRONT HOME PAGE UI/UX ARCHITECTURE                     |
+========================================================================+
| Design Aesthetic     | Subterranean Industrial Baroque, Cold Steel,    |
|                      | Midnight Slate, Luminescent Blue & Crimson Han  |
| Hero Section         | Title Banner, Cycle 1,778 Atmospheric Monitor,  |
|                      | Live Facility Status & Emergency Alert Ticker   |
| Central Grid         | 5 High-Impact Pentad Cards (Wiki, Story, Game,  |
|                      | Game Wiki, Collection) with icons & quick-links |
| Global Header        | Top Navigation Bar with breadcrumbs and search  |
| Global Footer        | Canonical Identity, Version Build, Repo Links   |
| Canonical Linking    | Exclusively to SOMNARAK-WORLD & GAME_BATTLE     |
| Technology Stack     | Vanilla HTML5, Modern Responsive CSS Grid,      |
|                      | Zero Framework Bloat, Pure High-Speed Hosting   |
+========================================================================+
```

### Layout Wireframe & User Flow
1. **Header & Status Banner:**
   - Displays current operational cycle: `CYCLE 1,778 // THE ABSOLVOHAN`.
   - Live Atmospheric Watch level indicator (e.g., `ATMOSPHERIC WATCH: LEVEL 1 — STABLE`).
2. **Hero Presentation:**
   - Cinematic introduction to Project Somnarak: the desperate struggle to contain human sorrow and harvest Han-Energy from contained entities beneath Somnarak City.
3. **The Five Interactive Gateway Portals (Pentad Grid):**
   - **Card 1: WIKI** -> Direct jump to `SOMNARAK-WORLD/Master_Codices/`.
   - **Card 2: STORY** -> Direct jump to `SOMNARAK-WORLD/Story_Cantos/`.
   - **Card 3: GAME** -> Direct jump to `GAME_BATTLE/`.
   - **Card 4: GAME WIKI** -> Direct jump to `docs/game-wiki/index.html`.
   - **Card 5: COLLECTION** -> Direct jump to `SOMNARAK-WORLD/Sorrow_Entities/`.
4. **Recent Transmissions & System Notices:**
   - Quick updates on recent archive discoveries, entity individualization audits, and tactical battle scenarios.

---

## 4. INTEGRATION & DEPLOYMENT CHECKLIST

- [x] Architectural specification compiled at `docs/README.md` and `docs/FRONT_HOME_PAGE_SPECIFICATION.md`.
- [x] Canonical data sources strictly restricted to `SOMNARAK-WORLD` and `GAME_BATTLE`.
- [x] Five Master Pillars defined with direct routes into canonical repositories.
- [x] Integration with 292 Sorrow Entities, 287+ SVG M.A.W. weapons, and tactical scenarios verified.
- [x] Full PM Wiki.gg & Fandom coverage specified for Lobotomy Corporation, Library of Ruina, and Limbus Company.
- [x] Zero external/temporary sandbox references in public documentation.
"""

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)

with open(spec_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated docs/README.md and docs/FRONT_HOME_PAGE_SPECIFICATION.md with strict sources.")
