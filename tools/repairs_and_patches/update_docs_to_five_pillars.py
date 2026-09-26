import re

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
| Five Master Pillars  | 1. WIKI (Comprehensive Setting & Lore Codex)    |
|                      | 2. STORY (Chronicles, Cycles & MAD Animatic)    |
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

It establishes the immediate atmosphere of The Absolvohan (  비탄의 장  , *Bitan-ui Jang*), sets the cosmological premise, and provides **Five Master Gateway Pillars** connecting directly to every branch of the repository:

```text
                                              [ docs/index.html ]
                                         BRAND NEW MASTER FRONT PAGE
                                                      |
       +--------------------+-------------------------+-------------------------+--------------------+
       |                    |                         |                         |                    |
       v                    v                         v                         v                    v
 [ 1. WIKI HUB ]     [ 2. STORY HUB ]          [ 3. GAME HUB ]        [ 4. GAME WIKI HUB ]   [ 5. COLLECTION HUB ]
  - World Lore        - 1,778 Cycle Logs       - 10-Node Spatial Grid  - P.M. Wiki.gg/Fandom  - 292 Sorrow Entities
  - SECC Codices      - SED / UCD Story Arcs   - Action Slot Battle    - L Corp Management    - 287+ SVG Weapons
  - Factions/Cadres   - Animatic MAD Script    - Clash Simulation      - LoR Combat Decks     - Tool Relic Dossiers
  - Comparative Text  - Secretary Meltdowns    - Workshop Gacha Forge  - Limbus Sin Database  - Blueprint Schematics
```

---

## 2. THE FIVE MASTER PILLARS

```text
+========================================================================+
|                       THE FIVE CORRIDOR GATEWAYS                       |
+========================================================================+
| Gateway Pillar       | Primary Domain & In-Universe Manifestation      |
+======================+=================================================+
| 1. WIKI              | The Scholarly & Operational Lore Knowledge Base |
| 2. STORY             | The Dramaturgical Narratives & Cycle Records    |
| 3. GAME              | The Interactive Tactical Simulation Engine      |
| 4. GAME WIKI         | P.M. Wiki.gg & Fandom Style Game Mechanics Wiki |
| 5. COLLECTION        | The Curated Specimen Archives & Hardware Vault  |
+========================================================================+
```

### Pillar I: The WIKI Hub (  위키 허브  , *Wiki Heobeu*)
- **Core Focus:** Comprehensive setting encyclopedia, mechanical reference codices, administrative architecture, and comparative world studies.
- **Key Modules & Routes:**
  1. **Cosmology & Geography:** Detailed documentation of Somnarak City (  솜나락 도성  ), The Raw (  생경  ), The Desolate (  황무지  ), and the subterranean strata.
  2. **The Reverie Directorate & The Absolvohan:** Departmental structures, administrative protocols, Floor Secretaries 01 through 10, Salt-Scrubbers, and the Dekan's High Command.
  3. **SECC Classification Codex:** Canonical decoding rules for Designation codes, Coherence tiers (I to V), Potency ranks (α to ω), Sorrow Categories, and Elemental affinities.
  4. **Organizations & Factions:** The High Council, The Giltong arbiters, the 5 Syndicates of The Raw (The Menders, Rust Frays, Veil Merchants, Memory Washers, Debt Concourse), and the 10 Specialist Cadres.
  5. **Comparative Codex:** The 19-section master comparative treatise analyzing 1-to-1 mechanical, narrative, and philosophical equivalents between Project Somnarak and Lobotomy Corporation / Project Moon.

### Pillar II: The STORY Hub (  서사 허브  , *Seosa Heobeu*)
- **Core Focus:** Canonical narratives, historical cycle logs, character psychologies, field operation books, and animatic storyboards.
- **Key Modules & Routes:**
  1. **The 1,778 Mnemonic Cycles:** Chronicled logs of past cycle resets, the accumulation of ancestral Han across centuries, and the tragic recurring loops of the facility.
  2. **Field Operation Chronicles:**
     - **The SED Corps (Special Extraction Division):** Arcs 1 through 7 detailing high-risk containment operations and anomaly pacification.
     - **The UCD Strike Force (Undercity Cleansing Directorate):** Arcs 1 through 6 covering brutal anti-syndicate and containment cleanup campaigns in The Raw.
  3. **Echo-Core Resonant Realization Wars:** The 4-phase psychological boss battles where each Floor Secretary descends into their core trauma (Lament, Grudge, Weight, Void) to achieve harmonic enlightenment.
  4. **The Animatic MAD Screenplay ("Nee, Dorodoro-san"):** The synchronized 8-scene directorial animatic script (`TRYOUT,SANDBOX/PROJECT.SOMNARAK-Animatic-Text.txt`), featuring the 19.67-second cold intro, 80% Entity-First screen time with bespoke Tales, Appearances, and Breach Behaviors, culminating in the 10-Secretary Meltdown climax.
  5. **Character Dossiers:** The psychological profiles of The Dekan, Arch-Liaisons, and fallen operatives.

### Pillar III: The GAME Hub (  게임 허브  , *Geim Heobeu*)
- **Core Focus:** Interactive playable tactical combat simulation, work containment mechanics, and workshop crafting engines.
- **Key Modules & Routes:**
  1. **The 10-Node Spatial Grid Combat Engine:**
     - Node-based spatial tactical field (Nodes 1 through 10).
     - Frontline engagement, flank maneuvers, push/pull knockback mechanics, and area-of-effect zone denial.
  2. **Speed & Action Slot System:**
     - Dynamic Speed rolls determining initiative and Action Slot counts per turn.
     - Clash calculation: Higher Speed intercepting attacks, Clash outcome formulas, and Power stacking.
     - Turn structure: 6 Battle Turns constituting 1 complete Combat Phase.
  3. **Containment Work Execution:**
     - Interactive simulation of the Four Work Types (*Viderehan*, *Ferrehan*, *Flerehan*, *Pugnahan*).
     - Strict enforcement of the **Two-Work-Type Rule** for Object, Place, and Time entities (*Viderehan* and *Ferrehan* only).
  4. **Workshop Crafting & Gacha Mechanics:**
     - Grades 1 through 5 Workshop commissioning (Giltong, Su-Ho, Tam-Sa, Sim-Pan, etc.).
     - Drop probability simulation: Grade 5 Legendary (0.5%), Grade 4 (1.0%), Grade 3 (5.0%).

### Pillar IV: The GAME WIKI Hub (  게임 위키 허브  , *Geim Wiki Heobeu*)
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
     - **10-Node Grid Tactical Formulas:** Spatial distance penalties, flanking bonuses, push/pull knockback meters, and AoE node coverage.
     - **Speed & Action Slot Progression:** Turn-by-turn action slot formulas, initiative clashes, and 6-turn combat phase resolution.
     - **Han Pressure (ATK) vs. Sorrow Gauge (HP):** Offense and defense level discrepancies, stagger threshold calculations, and damage resistance math.
     - **Containment Work Percentages:** Rigorous probability tables for Viderehan, Ferrehan, Flerehan, Pugnahan across Ranks I to V and Potencies α to ω.
     - **Two-Work-Type Rule Database:** Strict enforcement index verifying all 131 Non-Subject entities (Object, Place, Time) with Flerehan and Pugnahan set to N/A.
     - **Grade 1 to 5 Workshop Forging Matrix:** Material requirements, Han-ore refinement, and verified drop probabilities (Grade 5 Legendary: 0.5%, Grade 4: 1.0%, Grade 3: 5.0%).
     - **M.A.W. Equipment Stat Catalog:** 287+ SVG weapon profiles, defensive suits, and charms with elemental damage resistance values.
     - **Unified PM-to-Somnarak System Translation Matrix:** 1-to-1 mechanic converter bridging L Corp / LoR / Limbus terms directly to Somnarak operational equivalents.

### Pillar V: The COLLECTION Hub (  수집 허브  , *Sujip Heobeu*)
- **Core Focus:** Curated specimen archives, visual art assets, hardware showcases, and audio vaults.
- **Key Modules & Routes:**
  1. **The 292 Sorrow Entity Master Vault:** Complete individual dossiers for all 292 Sorrow Entities, containing verified Core Stat Lines, Tales, Appearances, and Breach Behaviors.
  2. **The M.A.W. Armory (287+ SVG Weapons):** Hand-crafted vector silhouettes for every single weapon in the registry, showcasing custom blades, fangs, mauls, lenses, clocks, and relics in batch-1 chrome finish.
  3. **Relic-Entity / Tool Abnormality Catalog:** The 131 non-subject artifacts categorized by operational profile (Single-Use, Equippable, Continuous) with tiered Log & Method unlock tables.
  4. **Multimedia & Schematics Vault:** Architectural blueprints (`SOMNARAK_CITY_LAYOUT.svg`, `THE_HAND_DR_LAYOUT.svg`), ambient soundscapes, and visual assets.

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
   - **Card 1: WIKI** -> Direct jump to Encyclopedic Codices, System Comparison, and World Archives.
   - **Card 2: STORY** -> Direct jump to Cycle Chronicles, Animatic Storyboard, and Field Arcs.
   - **Card 3: GAME** -> Direct jump to the 10-Node Grid Tactical Simulator and Battle Rules.
   - **Card 4: GAME WIKI** -> Direct jump to Project Moon (L Corp, LoR, Limbus) & Somnarak Gaming Database.
   - **Card 5: COLLECTION** -> Direct jump to 292 Sorrow Entities, M.A.W. SVG Armory, and Relics.
4. **Recent Transmissions & System Notices:**
   - Quick updates on recent archive discoveries, entity individualization audits, and workshop advancements.

---

## 4. INTEGRATION & DEPLOYMENT CHECKLIST

- [x] Architectural specification compiled at `docs/README.md` and `docs/FRONT_HOME_PAGE_SPECIFICATION.md`.
- [x] Five Master Pillars defined with distinct routing destinations: `/wiki/`, `/story/`, `/game/`, `/game-wiki/`, `/collection/`.
- [x] Integration with 292 Sorrow Entities, 287+ SVG M.A.W. weapons, and 16 Project Moon research volumes verified.
- [x] Full PM Wiki.gg & Fandom coverage specified for Lobotomy Corporation, Library of Ruina, and Limbus Company.
- [x] Zero template leaks or code vocabulary violations in public documentation.
"""

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)

with open(spec_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated docs/README.md and docs/FRONT_HOME_PAGE_SPECIFICATION.md successfully.")
