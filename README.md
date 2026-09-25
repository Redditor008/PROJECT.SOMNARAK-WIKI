# Project Somnarak — Non-Wiki Canon & Reference Archive

Welcome to the **Canonical Lore & Reference Source Archive** for **Project Somnarak** (소마나락), maintained on the `NON-WIKI` branch.

> **Canonical Governance Gateway:** See [`GOVERNANCE.md`](GOVERNANCE.md) for the single entry point governing repository rules, developer handbooks, and operational protocols.

This repository serves as the authoritative, durable database and narrative foundation for the Somnarak universe (~3.42 million words). It houses the pure markdown source corpus for all cosmological frameworks, entity dossiers, equipment registries, specialized operational suites, planetary ecological archives, and departmental records.

---

## Repository Architecture

The repository is structured into distinct, authoritative functional environments:

| Directory / Artifact | Role | Contents |
|---|---|---|
| **`SOMNARAK-WORLD/`** | **100% In-Universe Narrative & Operational Source** | Official containment dossiers, master codices, equipment sets, specialized operational chronicles, and Echo-Core records written entirely from within the Somnarak universe. |
| **`GAME_BATTLE/`** | **Tactical Combat Operations & Scenario Vault** | Turn-based combat encounters, boss battle mechanics, tactical battle templates, and authoring guides based on the 10-node spatial engine. |
| **`PROJECT_MOON_RESEARCH/`** | **Encyclopedic Comparative Research Archive** | Comprehensive 12-volume research library and comparative study corpus detailing cosmology, factions, metaphysics, and mechanics. |
| **`REFERENCE_SOMNARAK_WIKI/`** | **Out-of-Universe Editorial Standards & Technical Audits** | Structural taxonomy, entity catalogs, paired-dossier audits, transfer manifests, weapon personalization ledgers, and multi-agent handoff protocols. |
| **Root Blueprints (`.svg`)** | **Canonical Master Architectural & Cartographic Blueprints** | Official vector blueprints of the Somnarak Metropolitan Grid (`SOMNARAK_CITY_LAYOUT.svg`) and Facility 01 Cross-Section (`THE_HAND_DR_LAYOUT.svg`). |
| **Root Governance & Tools** | **Operational Handbooks & Verification Infrastructure** | Authoritative developer handbooks (`DEVELOPMENT.md`, `RULE-TO-FOLLOW.md`, `SESSION_BREAK_PRECAUTION.md`, `CHANGELOG.md`, `TEST_TEXT_BOX_WIDTHS.md`) and automated audit tools (`tools/`). |

---

## Archive Metrics at a Glance

- **Over 1,708 curated canonical markdown files in SOMNARAK-WORLD (1,967+ total files)** across `SOMNARAK-WORLD`, `PROJECT_MOON_RESEARCH`, and technical standard archives
- **Over 3.42 million words (3,420,000+ words)** of structured, authentic canonical lore
- **38 In-Universe Master Codices** (`SOMNARAK-WORLD/Master_Codices/`) across 6 canonical subfolders establishing macro-cosmology, planetary geology, institutional doctrines, and combat physics
- **5 Planetary Biosphere & Ecological Codices** (`SOMNARAK-WORLD/Mugenhan_Ecology/`), documenting 15 Mundane species, 6 Sorrow Beasts/Plants, and 6 Mortal Sorrow Creatures across all planetary biomes
- **9 Absolvohan Narrative Volumes** (`SOMNARAK-WORLD/The_Absolvohan/`), chronicling the full Day 0 through Day 365+ journey across the 1,778th Cycle
- **7 Subterranean Descent Chronicles** (`SOMNARAK-WORLD/Katabagil/`), detailing the SED Katabagil deep expeditionary passages
- **6 Underworld Pacification Chronicles** (`SOMNARAK-WORLD/Katharcheok/`), documenting the UCD Katharcheok syndicate purge operations
- **7 Mnemonic Reception Chronicles** (`SOMNARAK-WORLD/Gieok_Jeojangso/`), detailing the Memory Archive's floor receptions
- **6 Trans-Desolate Overland Arcs** (`SOMNARAK-WORLD/Jipyeongseondae/`), documenting the Horizon Caravan's planetary crossings
- **10-Node Spatial Grid Combat Mechanics** (`SOMNARAK-WORLD/Tactical_Combat_Engine/`), defining turn-based spatial combat resolution
- **Game Battle Operations & Tactical Simulation Suite** (`GAME_BATTLE/`), housing turn-by-turn combat encounters, boss battle mechanics, and standard authoring templates
- **292 Unique Sorrow Entity Dossiers** (`SOMNARAK-WORLD/Sorrow_Entities/`), cataloging entities across Coherence Ranks I to V and Potency Grades α to ω
- **42 Complete M.A.W. Equipment Sets** (`SOMNARAK-WORLD/MAW_Codex_Sets/`, quadripartite Side-Codex, Weapon, Suit, Gift across 1,165 files)
- **60 Five-Color Ordeal Files** (`SOMNARAK-WORLD/Ordeals/`), documenting Blue, Black, Pale, Grey, and Purple Ordeals across 4 watches
- **14 Hope Transformation Records** (`SOMNARAK-WORLD/Hope_Transformations/`), detailing resonant ascensions
- **9 Echo-Core Dossiers** (`SOMNARAK-WORLD/Echo_Cores/`), covering Facility 01 departmental leadership
- **12 Unknown Anomaly Records** (`SOMNARAK-WORLD/Unknown_Entities/`), containing deep-abyss occurrences and Regressor chronicles
- **16 Encyclopedic Research Volumes** (`PROJECT_MOON_RESEARCH/`), comparative structural analysis and reference library
- **2 Master Architectural & Cartographic Vector Blueprints** located at the repository root

---

## Master Directory Layout

```
PROJECT.SOMNARAK-WIKI/ (Branch: NON-WIKI)
├── README.md                               # This master documentation & navigation guide
├── DEVELOPMENT.md                          # Handbook for working in the NON-WIKI archive
├── INSTALL_PERCENTAGE_REPORT.md            # Shingle-weighted analysis of lore coverage in public wiki
├── RULE-TO-FOLLOW.md                       # Owner's binding operating rules (v2: Push-Always doctrine)
├── UNIVERSAL_FOLLOW_RULE.md                # Portable AI baseline operating rules
├── SESSION_BREAK_PRECAUTION.md             # Crash-recovery protocol & active work ledger
├── CHANGELOG.md                            # Complete versioning and batch revision history
├── SOMNARAK_CITY_LAYOUT.svg                # Master cartographic blueprint: Somnarak Metropolitan Grid
├── THE_HAND_DR_LAYOUT.svg                  # Master architectural blueprint: Facility 01 Cross-Section
├── TEST_TEXT_BOX_WIDTHS.md                 # Ergonomic text box width & visual calibration standard (127-128 chars)
│
├── GAME_BATTLE/                            # Tactical Combat Operations & Scenario Simulation Vault
│   ├── README.md                           # Master index, GBS mechanics primer & document roadmap
│   ├── INTRODUCTION_AND_GUIDE.md           # Authoring guide & SOP for all future battle .md files
│   ├── BATTLE_SCENARIO_TEMPLATE.md         # Production-ready markdown template for combat encounters
│   ├── CANONICAL_ENCOUNTER_01_GRIEVING_COLOSSUS.md # Full 6-turn canonical combat scenario demonstration
│   ├── SCENARIO_02_CONTAINMENT_BREACH_FLOOR_02.md # Full 6-turn containment breach suppression on Floor 2
│   ├── SCENARIO_03_UNDERWORLD_RUST_VEIL_PURGE.md # Full 6-turn UCD undercity sweep vs Fray construct
│   ├── SCENARIO_04_SED_SUNKEN_AQUEDUCT_DESCENT.md # Full 6-turn SED deep-karst descent vs Drowned Guardian
│   ├── SCENARIO_05_HORIZON_CARAVAN_LEVIATHAN_SIEGE.md # Full 6-turn Drift Throne defense vs Glass Burrower
│   ├── SCENARIO_06_MEMORY_ARCHIVE_STRATUM_REALIZATION.md # Full 6-turn Floor 04 Realization vs Weeping Statue
│   ├── BOSS_MECHANICS_GRIEVING_COLOSSUS.md # Sovereign Boss Mechanics Folio for SE-C-Vδ-002
│   ├── BOSS_MECHANICS_WEEPING_MIRROR.md    # Sovereign Boss Mechanics Folio for SE-C-IVδ-195
│   ├── BOSS_MECHANICS_KING_OF_MENDERS.md   # Syndicate Boss Mechanics Folio for King of Menders
│   ├── SQUAD_ARCHETYPE_REVERIE_CONTAINMENT.md # 4-Warden Facility 01 Containment Cadre Manual
│   ├── SQUAD_ARCHETYPE_UCD_PACIFICATION.md    # 4-Breacher UCD Close-Quarters Pacification Cadre Manual
│   ├── CYCLE_ENGRAM_SYSTEM.md              # 1,778-cycle historical engram attunement & stat shifting framework
│   └── ECHO_CORE_REALIZATION_SYSTEM.md      # 4-phase departmental trauma battles & resonant catharsis engine
│
├── tools/                                  # Non-wiki developer verification tools & formatters
│   ├── audit_lore_archive.py               # Standalone Python audit tool (UTF-8, codices, M.A.W., entities)
│   ├── check_box_symmetry.py               # Strict text box symmetry & border alignment auditor
│   ├── text_box_double_checker.py          # Dual-engine independent text box & wide-format validator
│   ├── box_formatter.py                    # Ergonomic ASCII text box generation utility
│   └── format_rst_box.py                   # ReStructuredText and markdown box alignment formatter
│
├── PROJECT_MOON_RESEARCH/                  # Encyclopedic Project Moon Research Compendium (12 Volumes)
│   ├── 01_COSMOLOGY_GEOGRAPHY_AND_LAWS.md  # The City, Head, Arbiters, Outskirts, Taboos
│   ├── 02_THE_TWENTY_SIX_WINGS_AND_SINGULARITIES.md # Wings A–Z, Singularities, Smoke War
│   ├── 03_SOCIETAL_POWERS_AND_FACTIONS.md  # Fingers, Associations, Syndicates, Workshops
│   ├── 04_METAPHYSICS_COGNITION_AND_PHENOMENOLOGY.md # The Light, Distortions, E.G.O, Peccatula
│   ├── 05_CHRONICLED_NARRATIVES_AND_CANON_WORKS.md # LC, LoR, Limbus, Distortion Detective, Leviathan
│   ├── 06_PARALLEL_WORLDS_AND_MIRROR_TECHNOLOGY.md # Mirror Worlds, Identities, Glass Windows
│   ├── 07_COMPREHENSIVE_ENCYCLOPEDIC_LEXICON.md # Master terminology & technical concepts
│   ├── 08_TACTICAL_MECHANICS_AND_ORDEALS.md # Combat systems, clashes, affinities, Ordeals
│   ├── 09_EGO_EQUIPMENT_WEAPONS_SUITS_AND_GIFTS.md # E.G.O equipment, extraction, risk tiers
│   ├── 10_FIXER_OFFICES_AND_SPECIALIZED_SYNDICATES.md # Section breakdowns, Colors, Hana, Liu, Shi
│   ├── 11_LORE_AND_NARRATIVE_DEEP_DIVE.md  # Deep character studies, Carmen, Ayin, Angela, Roland
│   ├── 12_ABNORMALITY_ENCYCLOPEDIA.md      # Comprehensive abnormality entries (ZAYIN to ALEPH)
│   └── README.md                           # Research master index & comparative overview
│
├── SOMNARAK-WORLD/                         # 100% In-Universe Narrative & Operational Source Corpus (1,706 files)
│   ├── README.md                           # In-world archive guide & recommended reading order
│   ├── Master_Codices/                     # 38 Macro-Canon Master Codices across 6 canonical subfolders
│   │   ├── 01_Cosmology_and_World_Order/   # 8 Codices: Metaphysics, layers, geology, the Maw, Weeping
│   │   ├── 02_Institutional_Wings_and_Chronicles/ # 5 Codices: Reverie Directorate, SED, UCD, Archive, Caravan
│   │   ├── 03_Systems_Combat_Engine_and_Physics/ # 8 Codices: Battle engines, M.A.W., relics, Ordeals, workshops
│   │   ├── 04_Municipal_Society_and_Demographics/ # 10 Codices: Daily life, Council, Collectors, corporations, syndicates, cadres
│   │   ├── 05_Entities_Tales_and_Fractures/# 6 Codices: Entity taxonomy, tales, fractures, adversaries
│   │   ├── 06_Integrity_Audits_and_Comparative_Studies/ # 1 Codex: PM comparative integrity audit
│   │   └── README.md                       # Master codices catalog & thematic index
│   ├── The_Absolvohan/                     # 9 Chronological Narrative Volumes (Day 0–365 & Epilogue + Overview)
│   ├── Katabagil/                          # 7 Subterranean Descent Passages & Field Guide (Exploration Arcs 1–7)
│   ├── Katharcheok/                        # 6 Underworld Pacification Operations & Tactics Guide (Purge Arcs 1–6)
│   ├── Gieok_Jeojangso/                    # 7 Mnemonic Receptions & Mnemonic Combat Suite (Memory Archive)
│   ├── Jipyeongseondae/                    # 6 Trans-Desolate Overland Arcs & Bastion Suite (Horizon Caravan)
│   ├── Mugenhan_Ecology/                   # 5 Planetary Biosphere & Ecological Codices (Mundane, Beasts, MSF)
│   ├── Tactical_Combat_Engine/             # 10-Node Spatial Grid Combat Mechanics & Battle Integration Suite
│   ├── Story_Cantos/                       # The Character Story Cantos (Dialogue-Driven Prose Novellas)
│   ├── Sorrow_Entities/                    # 292 Unique Entity dossiers across Ranks I to V and Grades α to ω
│   ├── Echo_Cores/                         # 9 Echo-Core files: Facility 01 departmental leaders
│   ├── MAW_Codex_Sets/                     # 1,165 files: 42 complete quadripartite sets across 42 folders
│   ├── Ordeals/                            # 60 Ordeal files: Black, Blue, Grey, Pale, Purple (1st–Tide Watches)
│   ├── Hope_Transformations/               # 14 Hope Transformation files: HT-001 through HT-012, Trinity & Hand
│   └── Unknown_Entities/                   # 12 Unknown Entity files: UNK-248 to UNK-903 & Regressor chronicles
│
└── REFERENCE_SOMNARAK_WIKI/                # Out-of-World Editorial Standards, Audits & Catalogs
    ├── README.md                           # Overview of the reference standards folder
    ├── ABSOLOVHAN_REPAIR_NOTES.md          # Canon harmonization and repair notes for Absolvohan texts
    ├── SORROW_ENTITIES_CATALOG.md          # Complete indexed catalog of all 285 unique Sorrow Entities
    ├── SORROW_ENTITIES_PAIRS_AUDIT.md      # Detailed audit and resolution guide for the 241 paired entity files
    ├── ALL_34_REFERENCE_FILES_AUDIT.md     # Line-by-line audit of the foundational codices
    ├── ALL_FILES_AUDIT_MANIFEST.md         # Comprehensive manifest of all reference files
    ├── CATEGORY_AND_PAGE_PLAN.md           # Information architecture & structural classification
    ├── CONTENT_AND_VISUAL_STANDARDS.md     # Editorial standards & authentic Somnarak terminology
    ├── LIVE_DEPLOYMENT_AND_BRANCH_POLICY.md# Branch continuity and deployment policies
    ├── MASTER_HANDOFF_PROTOCOL.md          # AI session continuity & handoff guidelines
    ├── MAW_PERSONALIZE_PROGRESS.md         # Detailed M.A.W. equipment visual progress ledger
    ├── MAW_WEAPON_ARCHETYPES.md            # Comprehensive weapon taxonomy & silhouette archetypes
    ├── OPERATING_RULES.md                  # Canon integrity & directory rules
    ├── PROJECT_MOON_WIKI_NESTED_PLACEMENT_RESEARCH.md # Structural comparative research
    ├── PUBLIC_PAGE_COMPLIANCE_AUDIT_2026-08-31.md     # Historical compliance audit
    ├── REGISTRY_MASTER_STATUS.md           # M.A.W. Registry completion and archive tracking
    ├── SOMNARAK_CORPORATIONS_GAME_DESIGN_FRAMEWORK.md # Original design document for the sovereign corporations
    ├── SOMNARAK_DOCUMENT_RULES.md          # Archival classification & authoring rules for entity files
    ├── SOMNARAK_MAIN_ENTITY_PROTECTED_LIST.md # Authoritative list of 55 immutable core entities
    └── SOMNARAK_NAME_REGISTRY.md           # Authoritative nomenclature & character naming lexicon
```

---

## Canonical Master Architectural & Cartographic Blueprints (Repository Root)

The archive root houses the two official primary cartographic and architectural vector blueprints of the Somnarak universe:

### 1. `SOMNARAK_CITY_LAYOUT.svg` — Somnarak Metropolitan Cartography (솜나락 전역 구역도)
- **Topological Coordinate:** 37°28'N • Active Grid • Omega-Level Authority • Year 4,238.
- **The Central Monument:** The Alpha Tree Spire (중앙 상징목 • 알파 트리) seated at the heart of the city.
- **The Living Chasm:** The Maw (아가리) dominating the western quadrant of Zone B.
- **The Four Blast Gates:** Gate I (North), Gate II (East), Gate III (South), and Gate IV (West).
- **The Five Sector Divisions (오대 구역):**
  * **Zone A (Central Core Nexus / 도심):** City Sorrow (*Dohan* / 도한) • The Alpha Tree Spire & Subterranean Facility 01 • High Council & Directorate Command.
  * **Zone B (West Old District / 구도심):** Deep Urban Trauma (*Old Lament* / 고탄) • The Maw Perimeter & Weeping corridors • Dekan & B-01 Garrison.
  * **Zone C (East Chevron Arc / 수탈 구역):** Personal Agony (*Naehan* / 내한) • Collector's Row & Debt Concourse • Zyrak & Floor 3 Nexus.
  * **Zone D (North & South Flanks / 단조로):** Memory Balance (*Memory Resonance*) • The Forge District (North) & Echo Gardens (South) • Ayshuk & Architects Guild.
  * **Zone E (Perimeter Bulwark / 경계선):** Outside Grief (*Oehan* / 외한) • 360° Fortified Bulwark & Blast Gates • Mellda (Floor 5) & Xyan (Floor 8).

### 2. `THE_HAND_DR_LAYOUT.svg` — Facility 01: The Hand of Change (변화의 손)
- **Subterranean Depth:** -2,000 meters beneath the roots of the Alpha Tree • Containment Locked • Maw Active.
- **Eight-Floor Architectural Cross-Section & The Nine Echo-Cores:**
  * **Floor 1 (Neutral / Central Spire & Common Hall):** Director Majin & Secretary Seiyon • Decision Core, Absolvohan Tap, 1,778-Cycle Comms, Central Infirmary (Han-Cryo Pods), M.A.W. Armory (Suits α–ω).
  * **Floor 2 (The Maw's Keep / Entity Containment):** Containment Lead Dekan • Cells 01–03 (Silent Child [Rank I], Three Birds [Rank IV], Smothering Mother [Rank III]), Suppression Armory, Armored Maw Edge Feed, Whispering Gallery.
  * **Floor 3 (The Extraction Hall / M.A.W. Extraction Nexus):** Extraction Lead Zyrak • Extraction Chambers A & B (99.2% harvest, pure crystal vats), Equipment Attunement Range, ω-Grade Testing Sims.
  * **Floor 4 (Insight Forge / Research & Structural Grief):** Research Lead Ayshuk • Han Physics Lab (Quantum Grief Spectrometry), Resonance Tuning Array, Bio-Synthesis Looms, Real-Time City Flow Vault.
  * **Floor 5 (Border Watch / Perimeter Defense):** Border Lead Mellda • Oehan Long-Range Radar/Sonar, 500-Warden Garrison Barracks, Heavy Bulwark Gate Barrier, External Storm Sentries.
  * **Floor 6 (Deep Vault / Subterranean Archives):** Archive Lead Marjuk • Subterranean Memory Wells, Pre-Collapse Reliquary (Stasis Fields), Coded Sovereign Manifests, Sealed Abyssal Door Chamber.
  * **Floor 7 (Shadow Corps / Mobile Black Operations):** The Outsider Ishall • Infiltration Drop Shafts, Sovereign Strike Armory (Grade-ω Loadouts), Directorate Intel Interrogation Vaults, Elite Suppression Squads.
  * **Floor 8 (Gate Watch / Zone E Egress):** The Exile Xyan • Gate Command & Lockdown Post, Desolate Transit Airlock, Outer Perimeter Sentry Array, Deep Sector Transit Bus.

---

## Macro-Canon Master Codices (`SOMNARAK-WORLD/Master_Codices/`)

The foundational source texts located in `SOMNARAK-WORLD/Master_Codices/` establish the core in-world canon of Somnarak. Every entity, piece of equipment, and district event derives from these texts, organized cleanly into six thematic subfolders:

### Subfolder 1: `01_Cosmology_and_World_Order/`
Foundational cosmological architecture, planetary geology, metaphysics, origin cataclysms, and sovereign geography:

| Codex File Name | Focus & Subject Matter | Key Topics Covered |
|---|---|---|
| [`PROJECT_SOMNARAK.md`](SOMNARAK-WORLD/Master_Codices/01_Cosmology_and_World_Order/PROJECT_SOMNARAK.md) | Master Worldbuilding Bible (5,507 lines) | The Grand Cosmology, 5 Layers, The Maw, The Weeping, Universal Laws, and Han physics |
| [`SOMNARAK_CHEONGULA.md`](SOMNARAK-WORLD/Master_Codices/01_Cosmology_and_World_Order/SOMNARAK_CHEONGULA.md) | Origin Cataclysm & Cheongula (528 lines) | The First Sorrow, Year 0 Cataclysm, emergence of the Maw, and primordial history |
| [`SOMNARAK_DREAM_REALM.md`](SOMNARAK-WORLD/Master_Codices/01_Cosmology_and_World_Order/SOMNARAK_DREAM_REALM.md) | Ethereal Dream Substratum (417 lines) | Dream-diving physics, Weavers Guild, ethereal entities, and somnolent phenomena |
| [`SOMNARAK_GEOLOGY.md`](SOMNARAK-WORLD/Master_Codices/01_Cosmology_and_World_Order/SOMNARAK_GEOLOGY.md) | Mugenhan Planetary Geology (196 lines) | Macro-terrain of Mugenhan, Untouched Ocean `[ConHeAn]`, Numbing Tundra `[NuRoZen]`, Sorrow Lake, and strata |
| [`SOMNARAK_THE_DESOLATE.md`](SOMNARAK-WORLD/Master_Codices/01_Cosmology_and_World_Order/SOMNARAK_THE_DESOLATE.md) | The Wasteland Beyond Walls (436 lines) | The Scar, toxic Han-dust storms, nomad clans, border garrisons, and Kael's Kingdom |
| [`SOMNARAK_THE_DOORSPEECH.md`](SOMNARAK-WORLD/Master_Codices/01_Cosmology_and_World_Order/SOMNARAK_THE_DOORSPEECH.md) | Linguistic Censorship & Acoustic Control (439 lines) | Verbal taboos, speech filtration, acoustic dampening arrays, and Giltong Enforcers |
| [`SOMNARAK_THE_WEEPING.md`](SOMNARAK-WORLD/Master_Codices/01_Cosmology_and_World_Order/SOMNARAK_THE_WEEPING.md) | Subterranean River of Liquid Han (413 lines) | Hydrology of grief, weeping currents, crystallization thresholds, and entity genesis |
| [`SOMNARAK_UNKNOWN_CITIES.md`](SOMNARAK-WORLD/Master_Codices/01_Cosmology_and_World_Order/SOMNARAK_UNKNOWN_CITIES.md) | Sister Cities & Geopolitics (592 lines) | Sister cities Cheonbulok and Mugeukji, external geopolitical threats, and refugee enclaves |

---

### Subfolder 2: `02_Institutional_Wings_and_Chronicles/`
Official corporate dossiers and operational doctrines of the sovereign institutional wings:

| Codex File Name | Focus & Subject Matter | Key Topics Covered |
|---|---|---|
| [`The_REVERIE_DIRECTORATE.md`](SOMNARAK-WORLD/Master_Codices/02_Institutional_Wings_and_Chronicles/The_REVERIE_DIRECTORATE.md) | Facility 01 Corporate Dossier (3,576 lines) | Subterranean Facility 01, 8 Floors, 9 Echo-Core attendants, and containment systems |
| [`The_SOMNARAK_EXPLORATION_DECREE.md`](SOMNARAK-WORLD/Master_Codices/02_Institutional_Wings_and_Chronicles/The_SOMNARAK_EXPLORATION_DECREE.md) | SED Corporate Dossier (581 lines) | Three-tier subterranean descent doctrine, survey gear, and 7-member explorer cadre |
| [`The_UNDERWORLD_CLEANUP_DESCEND.md`](SOMNARAK-WORLD/Master_Codices/02_Institutional_Wings_and_Chronicles/The_UNDERWORLD_CLEANUP_DESCEND.md) | UCD Corporate Dossier (509 lines) | Three-phase reclamation doctrine, urban pacification weaponry, and 6-officer task force |
| [`The_MEMORY_ARCHIVE.md`](SOMNARAK-WORLD/Master_Codices/02_Institutional_Wings_and_Chronicles/The_MEMORY_ARCHIVE.md) | The Memory Archive Dossier (915 lines) | Sub-Alpha root architecture, Mnemonic Combat Framework, and 7-floor reception stratigraphy |
| [`The_HORIZON_CARAVAN.md`](SOMNARAK-WORLD/Master_Codices/02_Institutional_Wings_and_Chronicles/The_HORIZON_CARAVAN.md) | The Horizon Caravan Dossier (684 lines) | Drift Throne 140m mobile crawler specifications, trans-desolate navigation, and bastion warfare |

---

### Subfolder 3: `03_Systems_Combat_Engine_and_Physics/`
Tactical combat specifications, mechanical mathematics, and metaphysical physics:

| Codex File Name | Focus & Subject Matter | Key Topics Covered |
|---|---|---|
| [`SOMNARAK_BATTLE_SYSTEM.md`](SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_BATTLE_SYSTEM.md) | Combat Engine & Affinities (577 lines) | 4 Sorrow Elements (Grudge, Lament, Void, Weight), Range Bands 1–5, falloff, and formations |
| [`SOMNARAK_BATTLE_SYSTEM_STYLES.md`](SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_BATTLE_SYSTEM_STYLES.md) | Hexa-Style Combat Mechanics (767 lines) | Generic Core, Reverie Directorate, UCD Urban CQB, SED Depth Pressure, Archive Mnemonic, Caravan Bastion |
| [`SOMNARAK_FACTION_TECH.md`](SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_FACTION_TECH.md) | Institutional Technology Specs (654 lines) | Acoustic dampening, basalt extraction, silk weaving, barrier rigs, and Warden Threshold Vows |
| [`SOMNARAK_HAN_RELICS.md`](SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_HAN_RELICS.md) | Sovereign Primordial Artifacts (275 lines) | Threefold relic taxonomy, Unanswered floating hands, containment vaults, and Pre-Structuring relics |
| [`SOMNARAK_MAW_CODEX.md`](SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_MAW_CODEX.md) | Master Armory & Extraction Engine (9,033 lines) | M.A.W. weapon archetypes, suit weave defenses, gift slots, and extraction across 198 complete quadripartite sets (245 planned sets) |
| [`SOMNARAK_ORDEALS_FRAMEWORK.md`](SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_ORDEALS_FRAMEWORK.md) | Five-Color Ordeal Defense (301 lines) | Mechanics for Blue, Black, Pale, Grey, and Purple Ordeals across 4 watches and crisis taxonomy |
| [`SOMNARAK_TABOO_RESONANCE.md`](SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_TABOO_RESONANCE.md) | Seven Taboos & Resonances (366 lines) | Absolute civic laws, acoustic censorship dynamics, resonant punishments, and Giltong enforcement |
| [`SOMNARAK_WORKSHOPS.md`](SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_WORKSHOPS.md) | Six Great Workshops Codex (215 lines) | Non-M.A.W. artisan equipment, Workplace Law, and 0.5% / 1.0% / 5.0% acquisition curve across Grades 1 to 5 (Legendary Stat) |

---

### Subfolder 4: `04_Municipal_Society_and_Demographics/`
Societal structures, municipal governance, debt economics, and faction demographics:

| Codex File Name | Focus & Subject Matter | Key Topics Covered |
|---|---|---|
| [`SOMNARAK_CAST.md`](SOMNARAK-WORLD/Master_Codices/04_Municipal_Society_and_Demographics/SOMNARAK_CAST.md) | Canonical Registry of Figures (1,396 lines) | Council of Sighs, Departmental Leads, Wardens, Enforcers, Sector Chiefs, and Outlaws |
| [`SOMNARAK_COLLECTOR_BUREAU.md`](SOMNARAK-WORLD/Master_Codices/04_Municipal_Society_and_Demographics/SOMNARAK_COLLECTOR_BUREAU.md) | Municipal Debt Enforcement (142 lines) | 4 Metaphysical Currencies (Material, Karma, Soul, Emotional), Collector Scales, foreclosure tiers |
| [`SOMNARAK_CORPORATIONS.md`](SOMNARAK-WORLD/Master_Codices/04_Municipal_Society_and_Demographics/SOMNARAK_CORPORATIONS.md) | Sovereign Institutions Doctrine (351 lines) | Unified pentagonal operational doctrine connecting R.D., SED, UCD, Archive, and Caravan |
| [`SOMNARAK_ZONE_CORPORATIONS.md`](SOMNARAK-WORLD/Master_Codices/04_Municipal_Society_and_Demographics/SOMNARAK_ZONE_CORPORATIONS.md) | 25 Municipal Zone Corporations & Curfew Corps | Exactly 5 corporations per Zone (A–E), Haz-scorchers & Cleansers, Giltong arbiters, outer metropolises |
| [`SOMNARAK_COUNCIL_OF_SIGHS.md`](SOMNARAK-WORLD/Master_Codices/04_Municipal_Society_and_Demographics/SOMNARAK_COUNCIL_OF_SIGHS.md) | Sovereign Municipal Governance (128 lines) | High governance council, Chief of Staff Yeong, First Head Dohee, Third Head Gwanhee, and 45 cloaked heads |
| [`SOMNARAK_DAILY_LIFE.md`](SOMNARAK-WORLD/Master_Codices/04_Municipal_Society_and_Demographics/SOMNARAK_DAILY_LIFE.md) | Civilian Life & Urban Culture (510 lines) | Food synthesis, fashion, acoustic curfews, civic sectors, slang, and civilian social habits |
| [`SOMNARAK_DAWN_OF_HOPE.md`](SOMNARAK-WORLD/Master_Codices/04_Municipal_Society_and_Demographics/SOMNARAK_DAWN_OF_HOPE.md) | Year 4,238 & Dawn Initiative (580 lines) | The 1,778-cycle loop resolution, 45% healing threshold, historical eras, and final ascendance |
| [`SOMNARAK_FACTION_RELATIONS.md`](SOMNARAK-WORLD/Master_Codices/04_Municipal_Society_and_Demographics/SOMNARAK_FACTION_RELATIONS.md) | Faction Geopolitical Matrix (324 lines) | Power balances, covert treaties, debt relations, and municipal hostilities |
| [`SOMNARAK_UNDERWORLD.md`](SOMNARAK-WORLD/Master_Codices/04_Municipal_Society_and_Demographics/SOMNARAK_UNDERWORLD.md) | Subterranean Slums & The Raw (197 lines) | Menders, Frays, Memory Washers, Veil Merchants, Debt Brokers, and undercity survival |
| [`SOMNARAK_UNDERWORLD_SYNDICATES.md`](SOMNARAK-WORLD/Master_Codices/04_Municipal_Society_and_Demographics/SOMNARAK_UNDERWORLD_SYNDICATES.md) | The Five Syndicates of The Raw (450 lines) | The Menders Guild, Rust Frays, Veil Merchants, Memory Washers, Debt Concourse, and 10-node grid |
| [`SOMNARAK_SPECIALIST_CADRES.md`](SOMNARAK-WORLD/Master_Codices/04_Municipal_Society_and_Demographics/SOMNARAK_SPECIALIST_CADRES.md) | The Ten Specialist Cadres (420 lines) | Ten chartered contractor bureaus (Giltong, Su-Ho, Tam-Sa, etc.), Section 1–6 ladder, and formations |

---

### Subfolder 5: `05_Entities_Tales_and_Fractures/`
Entity manifests, cognitive fracture case studies, and anomalous psychological phenomena:

| Codex File Name | Focus & Subject Matter | Key Topics Covered |
|---|---|---|
| [`SOMNARAK_ENEMY_LIST.md`](SOMNARAK-WORLD/Master_Codices/05_Entities_Tales_and_Fractures/SOMNARAK_ENEMY_LIST.md) | Adversary Compendium (187 lines) | Undercity threats, feral constructs, rogue operators, Outskirts beasts, and security hazards |
| [`SOMNARAK_ENTITIES.md`](SOMNARAK-WORLD/Master_Codices/05_Entities_Tales_and_Fractures/SOMNARAK_ENTITIES.md) | Phenomenological Theory (202 lines) | Emergence of Sorrow Entities, crystallization thresholds, and 5 Coherence levels (I to V) |
| [`SOMNARAK_ENTITY_CODEX.md`](SOMNARAK-WORLD/Master_Codices/05_Entities_Tales_and_Fractures/SOMNARAK_ENTITY_CODEX.md) | Master Classification Codex (613 lines) | SECC code matrix, work affinities (Ferrehan, Flerehan, Pugnahan, Viderehan), and containment |
| [`SOMNARAK_ENTITY_TALES.md`](SOMNARAK-WORLD/Master_Codices/05_Entities_Tales_and_Fractures/SOMNARAK_ENTITY_TALES.md) | Master Origin Lore Anthology (13,825 lines) | Tripartite lore structure: 이야기 (Tale), 증언 (Testimony), 기록 (Record) for 246 entities |
| [`SOMNARAK_NAMED_FRACTURES.md`](SOMNARAK-WORLD/Master_Codices/05_Entities_Tales_and_Fractures/SOMNARAK_NAMED_FRACTURES.md) | Historical Cognitive Breakdowns (472 lines) | Breakdown categories (Corrosion, Meltdown, Panic, Apathy) across 18 documented case studies |
| [`SOMNARAK_WOUND_WALKERS.md`](SOMNARAK-WORLD/Master_Codices/05_Entities_Tales_and_Fractures/SOMNARAK_WOUND_WALKERS.md) | Order of Wandering Healers (274 lines) | Monastic order sworn to absorb, transmute, and carry the burden of civilian sorrow |

---

### Subfolder 6: `06_Integrity_Audits_and_Comparative_Studies/`
Trans-cosmic integrity audits and strict divergence certifications:

| Codex File Name | Focus & Subject Matter | Key Topics Covered |
|---|---|---|
| [`SOMNARAK_PM_COMPARATIVE_INTEGRITY_AUDIT.md`](SOMNARAK-WORLD/Master_Codices/06_Integrity_Audits_and_Comparative_Studies/SOMNARAK_PM_COMPARATIVE_INTEGRITY_AUDIT.md) | Comparative Integrity Audit (867 lines) | 97.4% structural divergence audit, 100% plot-hole-free mechanics, and ontological independence |

---

## Mugenhan Planetary Biosphere & Ecology Suite (`SOMNARAK-WORLD/Mugenhan_Ecology/`)

The planetary biosphere of Mugenhan is cataloged across a rigorous **Tripartite Evolutionary Taxonomy** establishing the precise metaphysical and physiological boundaries between mundane life, sorrow-infused wildlife, and mortal grief organisms:

- **Tier 1: Mundane Planetary Flora & Fauna (100% Biological Organisms):** Ordinary, non-anomalous biological organisms adapted to Mugenhan's macro-biomes (the Untouched Ocean `[ConHeAn]`, Numbing Tundra `[NuRoZen]`, Sorrow Lake, Crystal Peaks, Sea of Glass, and Agricultural Basin). These species are mortal, lack SECC codes, possess zero grief aura, and are safely harvestable for civic food and insulation.
- **Tier 2: Sorrow-Infused Beasts & Plants (80% Biological / 20% SE-M.A.W. Infusion):** Wildlife and vegetation mutated by prolonged exposure to ambient Liquid Han and weeping strata. They operate under the absolute **80/20 Law of Predation**, can be permanently slain with conventional heavy kinetic or void ordnance, and yield harvestable Grade α–β reinforced carapaces and conductive sap.
- **Tier 3: Mortal Sorrow Creatures (Tier 3 MSF - Mortal Sorrow Fauna & Flora):** Grief organisms born not from human sin, but from catastrophic mass animal death-panic or ancient forest defoliation. Capped strictly at **Grade-β Potency**, these entities do not trigger Facility containment cycles; upon taking lethal damage, their corporeal form dissolves irreversibly into inert grey Han dust.

### Canonical Ecological Compendia:

| Document File Name | Ecological Scope | Key Documented Phenotypes & Species |
|---|---|---|
| [`MUGENHAN_ECOLOGY_OVERVIEW.md`](SOMNARAK-WORLD/Mugenhan_Ecology/MUGENHAN_ECOLOGY_OVERVIEW.md) | Master Ecological Framework (139 lines) | Tripartite taxonomy, 80/20 biological law, harvesting thresholds, and planetary safety protocols |
| [`MUGENHAN_PLANETARY_FLORA_AND_FAUNA.md`](SOMNARAK-WORLD/Mugenhan_Ecology/MUGENHAN_PLANETARY_FLORA_AND_FAUNA.md) | 15 Known Mundane Species (214 lines) | 15 Mundane species across all 6 macro-biomes (Deep-Fin Trench Whale, Basalt Burrower, Frost-Fur Yak, etc.) |
| [`MUGENHAN_BEAST_ANIMALS_AND_PLANTS.md`](SOMNARAK-WORLD/Mugenhan_Ecology/MUGENHAN_BEAST_ANIMALS_AND_PLANTS.md) | 6 Sorrow-Infused Beasts & Flora (120 lines) | Dune-Crusher, Ram-Gorgon, White-Fang Stalker, River Leviathan, Razor-Thorn Vine, Pitcher Trap |
| [`MUGENHAN_SORROW_CREATURES.md`](SOMNARAK-WORLD/Mugenhan_Ecology/MUGENHAN_SORROW_CREATURES.md) | 6 Mortal Sorrow Creatures (123 lines) | 4 Fauna MSF (Stampede Phantom, Carrion Weeper, Drowned Herd, Fray-Hound) & 2 Flora MSF (Ash-Wood Lament, Rot-Weave) |
| [`MUGENHAN_DEEP_ECOLOGY_COMPENDIUM.md`](SOMNARAK-WORLD/Mugenhan_Ecology/MUGENHAN_DEEP_ECOLOGY_COMPENDIUM.md) | Secondary Deep Ecology Compendium (364 lines) | Biome cross-sections, atmospheric moisture, deep aquifer analysis, and migratory patterns |

---

## Dedicated Specialized Operational & Macro-Narrative Suites

> **Master Macro-Chronological Canon Law:** All Three SED, UCD, and R.D. happen **BEFORE** the Dawn of Hope, and **ANYTHING ELSE** happens **AFTER** the Dawn of Hope. **UNK SE happens strictly AFTER R.D.** The 1,778 Mnemonic Cycles are viewable ONLY through R.D. + The Absolvohan; no division or file outside R.D. uses or references Cycles.
> - **Ante-Dawn Operations (Before Dawn of Hope — Sequential Triad):** `Katabagil/` (SED Subterranean Descents 1–7; calendar years) -> `Katharcheok/` (UCD Underworld Pacifications 1–6; calendar years) -> `The_Absolvohan/` (R.D. Facility 01 Containment Cycles 0001–1,778).
> - **Watershed Climax:** The Dawn of Hope (Year 4,238 / R.D. Cycle 1,778) — The Hand of Hope opens and transmutes 15% of sorrow into hope.
> - **Post-Dawn & Post-R.D. Operations (After Dawn of Hope & After R.D.):** `Unknown_Entities/` (UNK SE Anomalies, occurring strictly AFTER R.D.), `SOMNARAK_DAWN_OF_HOPE.md` (The Dawn Initiative & The Lantern), `Gieok_Jeojangso/` (Memory Archive), `Jipyeongseondae/` (Horizon Caravan), and `SOMNARAK_WOUND_WALKERS.md` (Company 4 Epilogue). All operate in linear calendar years.

Beyond the master codices, Project Somnarak maintains complete standalone operational suites that house the full chronological sagas, tactical field manuals, and combat engines:

1. **`SOMNARAK-WORLD/The_Absolvohan/` — The Absolvohan 366-Day Facility Chronicle:**
   - [`ABSOLOVHAN_OVERVIEW.md`](SOMNARAK-WORLD/The_Absolvohan/ABSOLOVHAN_OVERVIEW.md): Master operational summary of the 1,778th Loop.
   - Chronological narrative volumes spanning `Part_01_Day_000_to_045.md` through `Part_09_The_Epilogue_and_Dawn.md`, chronicling the daily shift logs, suppression engagements, Echo-Core realizations, and the Hand of Hope ascension.
2. **`SOMNARAK-WORLD/Katabagil/` — Somnarak Exploration Decree (SED) Subterranean Descents:**
   - [`KATABAGIL_OVERVIEW.md`](SOMNARAK-WORLD/Katabagil/KATABAGIL_OVERVIEW.md): Tactical field manual, abyss pressure ratings, and surveyor cadre profiles.
   - Seven deep descent passages (`Passage_1_The_Sunken_Aqueducts.md` to `Passage_7_The_Maw_Threshold.md`) mapping the abyssal strata beneath Somnarak.
3. **`SOMNARAK-WORLD/Katharcheok/` — Underworld Cleanup Descend (UCD) Pacification Operations:**
   - [`KATHARCHEOK_OVERVIEW.md`](SOMNARAK-WORLD/Katharcheok/KATHARCHEOK_OVERVIEW.md): Urban pacification doctrine, syndicate breach classifications, and squad armaments.
   - Six high-risk tactical cleanup operations (`Operation_1_Rust_Veil_Liquidation.md` to `Operation_6_Crownless_Throne_Shatter.md`) reclaiming the undercity slums.
4. **`SOMNARAK-WORLD/Gieok_Jeojangso/` — The Memory Archive Mnemonic Receptions:**
   - [`GIEOK_JEOJANGSO_OVERVIEW.md`](SOMNARAK-WORLD/Gieok_Jeojangso/GIEOK_JEOJANGSO_OVERVIEW.md): Architectural stratigraphy, Mnemonic Suture mechanics, and Floor Realization protocols.
   - Seven stratified reception chronicles (`Reception_1_Wandering_Dust_Warden.md` to `Reception_7_The_Archivists_Resonance.md`) testing operative mental fortitude.
5. **`SOMNARAK-WORLD/Jipyeongseondae/` — The Horizon Caravan Trans-Desolate Expeditions:**
   - [`JIPYEONGSEONDAE_OVERVIEW.md`](SOMNARAK-WORLD/Jipyeongseondae/JIPYEONGSEONDAE_OVERVIEW.md): Overland navigation guide, Drift Throne crawler specs, and bastion defensive tactics.
   - Six trans-desolate overland expedition arcs (`Arc_1_The_Glass_Sands_Crossing.md` to `Arc_6_The_Desolate_Horizon_Convergence.md`) traversing the outer wastelands.
6. **`SOMNARAK-WORLD/Tactical_Combat_Engine/` — 10-Node Spatial Grid Combat Engine:**
   - [`README.md`](SOMNARAK-WORLD/Tactical_Combat_Engine/README.md): Master architectural guide to the 10-node spatial engine, speed-action point scaling, and 6-turn combat phase loops.
   - [`WHAT_CAN_BE_DONE.md`](SOMNARAK-WORLD/Tactical_Combat_Engine/WHAT_CAN_BE_DONE.md): Comprehensive implementation manual for narrative combat logs and turn-based clash visualization.
7. **`SOMNARAK-WORLD/Story_Cantos/` — The Character Story Cantos (  비탄의 장  ):**
   - [`README.md`](SOMNARAK-WORLD/Story_Cantos/README.md): Master catalog, 3-Act narrative framework, and reading roadmap for the six core protagonist cantos.
   - Dialogue-driven natural narrative prose novellas ([`CANTO_01_THE_BASTION_ANCHOR_MIN_JAE.md`](SOMNARAK-WORLD/Story_Cantos/CANTO_01_THE_BASTION_ANCHOR_MIN_JAE.md), [`CANTO_02_THE_ACOUSTIC_VOID_SEOL_A.md`](SOMNARAK-WORLD/Story_Cantos/CANTO_02_THE_ACOUSTIC_VOID_SEOL_A.md), [`CANTO_03_THE_SHATTERED_STRIKER_TAEHO.md`](SOMNARAK-WORLD/Story_Cantos/CANTO_03_THE_SHATTERED_STRIKER_TAEHO.md), [`CANTO_04_THE_SUB_ZERO_RIDGE_HA_EUN.md`](SOMNARAK-WORLD/Story_Cantos/CANTO_04_THE_SUB_ZERO_RIDGE_HA_EUN.md), [`CANTO_05_SUTURE_OF_LOST_PAGES_SEIYON.md`](SOMNARAK-WORLD/Story_Cantos/CANTO_05_SUTURE_OF_LOST_PAGES_SEIYON.md), [`CANTO_06_THE_SLUM_BREACHER_KANG.md`](SOMNARAK-WORLD/Story_Cantos/CANTO_06_THE_SLUM_BREACHER_KANG.md)) exploring personal trauma, daily life, and emotional catharsis.

---

## Game Battle Operations & Tactical Simulation Suite (`GAME_BATTLE/`)

The repository root houses the dedicated `GAME_BATTLE/` operational suite, serving as the canonical bridge between the theoretical combat systems in `SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/` and narrative story battles. It contains standardized combat scenarios, boss fight mechanics, squad archetypes, and authoring guidelines for future battle files:

| Document File Name | Category & Scope | Description |
|---|---|---|
| [`GAME_BATTLE/README.md`](GAME_BATTLE/README.md) | Master Index & Overview | Executive summary, core GBS mechanics primer, directory inventory, and architectural roadmap. |
| [`GAME_BATTLE/INTRODUCTION_AND_GUIDE.md`](GAME_BATTLE/INTRODUCTION_AND_GUIDE.md) | Authoring Guide & Standards | Comprehensive guide and SOP for authoring all future battle `.md` files, encounter scripts, and boss mechanics. |
| [`GAME_BATTLE/BATTLE_SCENARIO_TEMPLATE.md`](GAME_BATTLE/BATTLE_SCENARIO_TEMPLATE.md) | Standardized Production Template | Ready-to-use markdown template with pre-aligned ASCII HUDs, rosters, turn tables, and phase-end blocks. |
| [`GAME_BATTLE/CANONICAL_ENCOUNTER_01_GRIEVING_COLOSSUS.md`](GAME_BATTLE/CANONICAL_ENCOUNTER_01_GRIEVING_COLOSSUS.md) | Canonical Combat Scenario | Full 6-turn combat engagement demonstrating Strike Team Alpha vs `SE-C-Vδ-002 The Grieving Colossus`. |
| [`GAME_BATTLE/CYCLE_ENGRAM_SYSTEM.md`](GAME_BATTLE/CYCLE_ENGRAM_SYSTEM.md) | Identity Attunement Framework | Canonical 1,778-cycle historical engrams modifying Speed Bands, Action Slots, and P1 Passives across operatives. |
| [`GAME_BATTLE/SCENARIO_REALIZATION_FLOOR_02_DEKAN.md`](GAME_BATTLE/SCENARIO_REALIZATION_FLOOR_02_DEKAN.md) | Sovereign Realization Scenario | Full 4-phase Floor 02 Realization: The Iron Quad vs Echo-Core 3 Lead Dekan (The Maw's Keep). |

### Core Mechanics Standardized in `GAME_BATTLE/`:
- **10-Node Linear Engagement Grid (`[N01]` to `[N10]`):** Discrete spatial line governing Range Bands 1 to 5, movement costs (1 AP per node), and flanking pincer bonuses (+25% kinetic damage).
- **Speed-to-AP Economy:** Operative initiative directly dictates combat bandwidth (Speed 1–2 = 2 AP, Speed 3–4 = 3 AP, Speed 5–6 = 4 AP, Speed 7+ = 5 AP).
- **The Four P-Framework:** P1 Passives (innate perks), P2 Panic (Composure 0–100), P3 Parry (opposed skill clash rolls), and P4 Posture (Poise 0–100).
- **Dual-Threshold Stagger Engine:** Part Rupture at 60% modular part HP (1.5x vulnerability), Composure Meltdown at 0 Composure (2.0x vulnerability across all parts).
- **6-Turn Macro Combat Phase:** 6 Battle Turns form 1 Combat Phase, culminating in ambient Sorrow Tide ticks (+10% Han saturation) and boss stance transitions.

---

## Project Moon Encyclopedic Research Compendium (Root: `PROJECT_MOON_RESEARCH/`)

The repository root houses a dedicated 12-volume encyclopedic research compendium examining the structural worldbuilding, faction hierarchies, metaphysical paradigms, and game mechanics of Project Moon's works (Lobotomy Corporation, Library of Ruina, Limbus Company, Distortion Detective, and Leviathan), serving as a benchmark for comparative narrative audits:

| Research Volume | Volume Title & Focus | Key Subject Matter Explored |
|---|---|---|
| [`01_COSMOLOGY_GEOGRAPHY_AND_LAWS.md`](PROJECT_MOON_RESEARCH/01_COSMOLOGY_GEOGRAPHY_AND_LAWS.md) | Cosmology, Geography, and Laws | The City, Head (A, B, C Corp), Arbiters, Beholders, Claw, Outskirts, Ruins, and Taboos |
| [`02_THE_TWENTY_SIX_WINGS_AND_SINGULARITIES.md`](PROJECT_MOON_RESEARCH/02_THE_TWENTY_SIX_WINGS_AND_SINGULARITIES.md) | The 26 Wings & Singularities | Wings A through Z, corporate monopolies, Singularities, Smoke War, and Patent Wars |
| [`03_SOCIETAL_POWERS_AND_FACTIONS.md`](PROJECT_MOON_RESEARCH/03_SOCIETAL_POWERS_AND_FACTIONS.md) | Societal Powers & Factions | The Five Fingers (Thumb, Index, Middle, Ring, Pinky), Hana, Fixer Associations, Syndicates |
| [`04_METAPHYSICS_COGNITION_AND_PHENOMENOLOGY.md`](PROJECT_MOON_RESEARCH/04_METAPHYSICS_COGNITION_AND_PHENOMENOLOGY.md) | Metaphysics & Cognition | The Seed of Light, Carmen's voice, Distortions, E.G.O manifestation, Peccatula, and Phantasm |
| [`05_CHRONICLED_NARRATIVES_AND_CANON_WORKS.md`](PROJECT_MOON_RESEARCH/05_CHRONICLED_NARRATIVES_AND_CANON_WORKS.md) | Chronicled Narratives & Canon | Comprehensive plot chronicles of Lobotomy Corp, Library of Ruina, Limbus Company, and Leviathan |
| [`06_PARALLEL_WORLDS_AND_MIRROR_TECHNOLOGY.md`](PROJECT_MOON_RESEARCH/06_PARALLEL_WORLDS_AND_MIRROR_TECHNOLOGY.md) | Parallel Worlds & Mirror Tech | Mirror Worlds, Mephistopheles, Dante's Clock, Identity extraction, and Golden Boughs |
| [`07_COMPREHENSIVE_ENCYCLOPEDIC_LEXICON.md`](PROJECT_MOON_RESEARCH/07_COMPREHENSIVE_ENCYCLOPEDIC_LEXICON.md) | Comprehensive Lexicon | Exhaustive dictionary of terminology, corporate jargon, fixer ranks, and combat concepts |
| [`08_TACTICAL_MECHANICS_AND_ORDEALS.md`](PROJECT_MOON_RESEARCH/08_TACTICAL_MECHANICS_AND_ORDEALS.md) | Tactical Mechanics & Ordeals | Clashing physics, speed dice, sanity thresholds, stagger damage, and Ordeal mechanics |
| [`09_EGO_EQUIPMENT_WEAPONS_SUITS_AND_GIFTS.md`](PROJECT_MOON_RESEARCH/09_EGO_EQUIPMENT_WEAPONS_SUITS_AND_GIFTS.md) | E.G.O Equipment Systems | Weapon archetypes, suit resistance profiles, gift extraction, and risk tier scaling |
| [`10_FIXER_OFFICES_AND_SPECIALIZED_SYNDICATES.md`](PROJECT_MOON_RESEARCH/10_FIXER_OFFICES_AND_SPECIALIZED_SYNDICATES.md) | Fixer Offices & Syndicates | Section breakdowns, Color Fixers (Red Mist, Black Silence, Purple Tear), and workshop gear |
| [`11_LORE_AND_NARRATIVE_DEEP_DIVE.md`](PROJECT_MOON_RESEARCH/11_LORE_AND_NARRATIVE_DEEP_DIVE.md) | Lore & Narrative Deep Dive | Deep character studies: Ayin, Angela, Roland, Carmen, Faust, and the 12 Sinners |
| [`12_ABNORMALITY_ENCYCLOPEDIA.md`](PROJECT_MOON_RESEARCH/12_ABNORMALITY_ENCYCLOPEDIA.md) | Abnormality Encyclopedia | Comprehensive compendium of Abnormalities across ZAYIN, TETH, HE, WAW, and ALEPH tiers |
| [`README.md`](PROJECT_MOON_RESEARCH/README.md) | Research Master Index | Master synthesis, research methodology, and structural comparison frameworks |

---

## Technical Formatting Standards (Root: `TEST_TEXT_BOX_WIDTHS.md`)

All operational interfaces, status monitors, and tactical combat logs in the archive adhere to the strict ergonomic specifications defined in `TEST_TEXT_BOX_WIDTHS.md`:

1. **The 127–128 Character Golden Ratio Window:**
   - Wide-format ASCII boxes and combat status monitors target an interior width of **127 at least, maximum 128 characters** (`len(line) in [127, 128]`).
   - Standard ASCII interface boxes use fixed-width borders (`+` corners, `-` horizontal margins, `|` vertical borders) with zero sliced words, zero trailing hyphens, and zero lazy abbreviations.
2. **Dual-Environment Formatting Law:**
   - Repository markdown files (`.md`) utilize clean ASCII boxes wrapped in non-markdown code fences (````text ... ````) to ensure 100% visual symmetry across GitHub, Obsidian, and desktop markdown previewers.
   - Strict prohibition against raw HTML line-break tags and LaTeX math symbols.

---

## Canonical Framework Summary

All source lore across this archive adheres to four absolute pillars:

1. **The Four Damage Types (사대 피해 유형):**
   - **Grudge (원한 / Crimson):** Physical and structural kinetic damage.
   - **Lament (비탄 / Blue):** Psychological erosion, composure loss, and despair.
   - **Void (공허 / Pale White):** Soul damage, existential erasure, and memory loss.
   - **Weight (비중 / Black):** Irreversible gravitational collapse and crushing trauma.

2. **The Four Work Types (사대 격리 작업):**
   - **Ferrehan (인내작업):** Physical endurance and barrier maintenance.
   - **Flerehan (공감작업):** Insight, weeping resonance, and active listening.
   - **Pugnahan (억제작업):** Repression, acoustic clamping, and physical force.
   - **Viderehan (관찰작업):** Remote optical surveillance and detached analysis.

3. **Threat Classifications & Coherence Ranks (위협 등급 및 응집도):**
   - **Rank I: Whisper (속삭임 / Soksagim · Grade α):** Negligible threat; passive resonance; minimal containment risk.
   - **Rank II: Murmur (웅얼거림 / Ungeolgeorim · Grade β):** Low-to-moderate threat; standard suppression squads sufficient.
   - **Rank III: Fragment (파편 / Papyeon · Grade γ):** Significant threat; lethal capabilities; disciplined work required.
   - **Rank IV: Entity (존재 / Jonjae · Grade δ):** Critical threat; severe psychological degradation; catastrophic breach hazard.
   - **Rank V: Sovereign (군주 / Gunju · Grade ω):** Existential threat; facility-wide or district-wide collapse potential.

4. **M.A.W. Equipment Triad (비탄의 무장):**
   - **MAW-W (Weapon):** Offense crystallized from the entity's core sorrow.
   - **MAW-S (Suit):** Armor woven from the entity's resonance, conferring elemental defenses.
   - **MAW-G (Gift):** Resonant accessory granting passive traits and cosmetic marks.

---

## Developer Verification Tools

To audit file integrity, master codices, M.A.W. quadripartite sets, text box symmetry, and entity counts:

```bash
# 1. Run the full archive audit (UTF-8, codices, M.A.W. sets, entity counts)
python3 tools/audit_lore_archive.py

# 2. Run text box symmetry auditor across all files
python3 tools/check_box_symmetry.py

# 3. Run dual-engine independent text box & wide-format validator
python3 tools/text_box_double_checker.py
```

---

## Operating Rules for AI & Contributors

1. **Push Always (Rule A0):** Every modification, creation, or deletion must be committed **and pushed** to the assigned session branch in the same turn. Never leave uncommitted changes or unpushed commits.
2. **File Safety (Rule A5):** Never delete canonical reference files without direct owner instruction. Single canonical files must be maintained; parallel drafts must never co-exist.
3. **Immutability of Canon:** Never replace authentic Somnarak terminology with generic placeholders or crossover terms. Always use native nomenclature (Sorrow Entities, Han, Absolvohan, M.A.W., Reverie Directorate, Council of Sighs).
4. **Formatting Discipline:** Zero broken ASCII boxes, zero raw HTML line-break tags, zero LaTeX math symbols, and 100% authentic in-universe perspective without meta-commentary or developer introspection.
