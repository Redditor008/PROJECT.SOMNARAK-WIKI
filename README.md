# Project Somnarak — Non-Wiki Canon & Reference Archive

Official authoritative repository of canonical lore, worldbuilding, and reference documentation for **Somnarak** — the City of Unresolved Sorrow.
*Year 4,238 · Dawn Initiative · Reverie Directorate Protocol*

---

## Overview

Welcome to the **`NON-WIKI`** branch of **Project Somnarak**.

This branch serves as the authoritative, pure-markdown **source repository** for all Somnarak worldbuilding materials, narrative manuscripts, entity containment files, and equipment registries. It is stripped of web build tools, HTML front-end pages, and browser bundles, focusing entirely on canon preservation, structural auditing, and editorial reference.

| Branch | Purpose | Scope | Primary Asset |
|---|---|---|---|
| **`main`** | Public Web Wiki Frontend | Static website served via GitHub Pages | HTML pages, CSS, JS, SVG compositions, web search |
| **`NON-WIKI`** (This Branch) | Canon Lore & Reference Archive | Authoritative markdown source corpus | 1,870+ reference files, entity codices, M.A.W. registries (~3.5M words) |

---

## Repository Architecture: Two Master Trees

The archive cleanly separates in-universe lore from out-of-world editorial and audit documents:

1. **`SOMNARAK-WORLD/`**: The complete in-universe canonical corpus (1,850+ files). Written strictly from an in-world perspective (Directorate clerks, Facility 01 Echo-Cores, containment workers, and city chroniclers). Contains the 34 foundational codices, Sorrow Entity dossiers, M.A.W. equipment sets, Ordeals, Hope Transformations, and Echo-Core personnel files.
2. **`REFERENCE_SOMNARAK_WIKI/`**: Out-of-world editorial standards, structural audits, master catalogs, multi-session handoff protocols, and research manifests.

---

## Archive Statistics

- **1,879 total markdown files** across `SOMNARAK-WORLD` and `REFERENCE_SOMNARAK_WIKI`
- **Over 3.46 million words** of structured, canonical lore
- **34 Macro-Canon Master Codices** (`SOMNARAK-WORLD/07_Reference/`) establishing the entire cosmology, geopolitical landscape, and physical laws of Somnarak
- **529 Sorrow Entity Dossiers** (`SOMNARAK-WORLD/01_Sorrow_Entities/`), representing 285 unique canonical entities across threat levels ZAYIN through ALEPH
- **291 M.A.W. Equipment Sets** (`SOMNARAK-WORLD/M.A.W. Codex_Set Registry/`, 1,196 files across 42 registry groups), cataloging Weapons, Suits, and Gifts
- **60 Five-Color Ordeal Files** (`SOMNARAK-WORLD/04_Ordeals/`), documenting First, Second, Third, and Tide watches
- **14 Hope Transformation Records** (`SOMNARAK-WORLD/02_Hope_Transformation/`), detailing resonant ascensions
- **9 Echo-Core Dossiers** (`SOMNARAK-WORLD/CHARACTER_WIKI/`), covering the departmental leadership of Facility 01 ("The Hand of Change")
- **8 Unknown Anomaly Records** (`SOMNARAK-WORLD/03_Unknown_Entities/`), containing unclassified deep-abyss occurrences

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
├── tools/                                  # Non-wiki developer tools
│   └── audit_lore_archive.py               # Standalone Python audit tool (UTF-8, codices, M.A.W., entities)
│
├── SOMNARAK-WORLD/                         # 100% In-Universe Narrative & Operational Source Corpus (1,850+ files)
│   ├── README.md                           # In-world archive guide & recommended reading order
│   ├── 01_Sorrow_Entities/                 # 529 Entity files: Dossiers, tales, and containment data
│   ├── 02_Hope_Transformation/             # 14 Hope Transformation files: HT-001 through HT-012, Trinity & Hand
│   ├── 03_Unknown_Entities/                # 8 Unknown Entity files: UNK-248 through UNK-903 & Dramaturgy
│   ├── 04_Ordeals/                         # 60 Ordeal files: Black, Blue, Grey, Pale, Purple (1st–Tide Watches)
│   ├── 07_Reference/                       # 34 Macro-Canon Master Codices: Cosmology, Factions, Systems
│   ├── CHARACTER_WIKI/                     # 9 Echo-Core files: Facility 01 departmental leaders
│   └── M.A.W. Codex_Set Registry/          # 1,196 files across 42 registry folders (A/B/C/D quadripartite sets)
│
└── REFERENCE_SOMNARAK_WIKI/                # Out-of-World Editorial Standards, Audits & Catalogs
    ├── README.md                           # Overview of the reference standards folder
    ├── SORROW_ENTITIES_CATALOG.md          # Complete indexed catalog of all 285 unique Sorrow Entities
    ├── SORROW_ENTITIES_PAIRS_AUDIT.md      # Detailed audit and resolution guide for the 241 paired entity files
    ├── ALL_34_REFERENCE_FILES_AUDIT.md     # Line-by-line audit of the 34 foundational codices
    ├── ALL_FILES_AUDIT_MANIFEST.md         # Comprehensive manifest of all reference files
    ├── CATEGORY_AND_PAGE_PLAN.md           # Information architecture & structural classification
    ├── CONTENT_AND_VISUAL_STANDARDS.md     # Editorial standards & authentic Somnarak terminology
    ├── LIVE_DEPLOYMENT_AND_BRANCH_POLICY.md# Branch continuity and deployment policies
    ├── MASTER_HANDOFF_PROTOCOL.md          # AI session continuity & handoff guidelines
    ├── MAW_PERSONALIZE_PROGRESS.md         # Detailed M.A.W. equipment visual progress ledger
    ├── MAW_WEAPON_ARCHETYPES.md            # Comprehensive weapon taxonomy & silhouette archetypes
    ├── OPERATING_RULES.md                  # Canon integrity & directory rules
    ├── PROJECT_MOON_WIKI_NESTED_PLACEMENT_RESEARCH.md # Structural comparative research
    └── PUBLIC_PAGE_COMPLIANCE_AUDIT_2026-08-31.md     # Historical compliance audit
```

---

## The 34 Macro-Canon Master Codices (`SOMNARAK-WORLD/07_Reference/`)

The 34 files located in `SOMNARAK-WORLD/07_Reference/` constitute the foundational in-world canon of Somnarak. Every entity, piece of equipment, and district event derives from these texts.

| Codex File Name | Focus & Subject Matter | Key Topics Covered |
|---|---|---|
| `PROJECT_SOMNARAK.md` | Master Worldbuilding Core (5,502 lines) | The Grand Cosmology, 5 Layers, The Maw, The Weeping, Universal Laws |
| `The_REVERIE_DIRECTORATE.md` | Facility 01 Architecture (2,934 lines) | 8 Subterranean Floors, 9 Echo-Cores, Ordeal suppression systems |
| `SOMNARAK_ABSOLOVHAN.md` | Sovereign Golden Dawn & Absolvohan | Resonant Clash, Absolvohan parts 1–9, the Hand of Hope |
| `SOMNARAK_BATTLE_SYSTEM.md` | Combat Engine & Damage Types | 4 Damage Types (Grudge, Lament, Void, Weight), Work Types, Panic |
| `SOMNARAK_CAST.md` | 25 Known People of Somnarak | Echo-Cores, leads, commanders, outlaws, and underworld brokers |
| `SOMNARAK_CHEONGULA.md` | The First Sorrow & The Maw Event | Origin of the Cheongula Cataclysm, Year 0, The Great Fracture |
| `SOMNARAK_CORPORATIONS.md` | The Three Industrial Monopolies | Corporate dominance, resource extraction, economic governance |
| `SOMNARAK_DAILY_LIFE.md` | Urban Life & Acoustic Curfews | Food, fashion, sound suppressors, slum culture, city holidays |
| `SOMNARAK_DAWN_OF_HOPE.md` | Dawn Initiative & Timeline | Year 4,238 Dawn Initiative, the 1,778 Cycles, historical epochs |
| `SOMNARAK_DOCUMENT_RULES.md` | Directorate Archival Rules | Classification standards, classification levels, redaction rules |
| `SOMNARAK_DREAM_REALM.md` | The Dream Realm & Weavers Guild | Dream-diving, subconscious condensation, ethereal aberrations |
| `SOMNARAK_ENEMY_LIST.md` | External Threats & Aberrations | Outskirts beasts, rogue Han-constructs, anomalous predators |
| `SOMNARAK_ENTITIES.md` | Entity System Overview | Emergence mechanics, sorrow condensation, containment theory |
| `SOMNARAK_ENTITY_CODEX.md` | Complete Entity Codex | Comprehensive threat indices (ZAYIN, TETH, HE, WAW, ALEPH) |
| `SOMNARAK_ENTITY_TALES.md` | Collected Entity Lore & Tales | In-universe folklore, agent interview logs, origin chronicles |
| `SOMNARAK_FACTION_RELATIONS.md` | Diplomatic & Power Dynamics | Inter-faction rivalries, treaties, covert operations |
| `SOMNARAK_FACTION_TECH.md` | Han Technologies & Machinery | Extraction engines, resonance dampers, containment plating |
| `SOMNARAK_HAN_RELICS.md` | Han Relic Registry | Artifacts imbued with ancient sorrow, unique relic behaviors |
| `SOMNARAK_HORIZON_CARAVAN.md` | The Nomads & Trade Caravans | Desert routes, wandering merchants, exterior wasteland trade |
| `SOMNARAK_MAIN_ENTITY_PROTECTED_LIST.md` | Protected Canonical Manifest | The immutable baseline Sorrow Entities and core designations |
| `SOMNARAK_MAW_CODEX.md` | Master M.A.W. Equipment Codex | Materialized Armament of Woe extraction, resonance, and wear |
| `SOMNARAK_MEMORY_ARCHIVE.md` | Historical Records & Cycles | Recovered pre-cataclysm texts, ancient memories, cyclical resets |
| `SOMNARAK_NAMED_FRACTURES.md` | Psychological Fractures | Agent mental degradation states, corrosion stages, therapy logs |
| `SOMNARAK_NAME_REGISTRY.md` | Standardized Nomenclature | Korean-English transliteration rules and terminology standards |
| `SOMNARAK_ORDEALS_FRAMEWORK.md` | Five-Color Ordeals Framework | Midnight, Dawn, Dusk, and Noon wave parameters and mechanics |
| `SOMNARAK_SED.md` | Sorrow Extraction Division | Operational guidelines, quota requirements, extraction hazards |
| `SOMNARAK_TABOO_RESONANCE.md` | Taboo Resonance Physics | The Seven Taboos, acoustic triggers, resonant backlash |
| `SOMNARAK_THE_DESOLATE.md` | The Desolate Outskirts | The Scar, nomadic wastes, Han-storms, Kael's Kingdom |
| `SOMNARAK_THE_DOORSPEECH.md` | Acoustic Censorship & Taboos | The Giltong Enforcers, speech monitors, silenced districts |
| `SOMNARAK_THE_WEEPING.md` | The River of Liquid Han | The underground river, sorrow accumulation, entity crystallization |
| `SOMNARAK_UCD.md` | Underworld Cleanup Descend | Strike Team Taeho/Yuna/Minho/Soojin, subterranean purge missions |
| `SOMNARAK_UNDERWORLD.md` | The Raw & Underworld Factions | Menders, Frays, Memory Washers, Veil Merchants, Debt Brokers |
| `SOMNARAK_UNKNOWN_CITIES.md` | Lost Sister Cities | Corners 2 & 3: Cheonbulok and Mugeukji, refugee migrations |
| `SOMNARAK_WOUND_WALKERS.md` | Wound Walkers Order | The wandering healers, eternal sorrow alleviation, ascetic vows |

---

## Facility 01 & The Nine Echo-Cores (`SOMNARAK-WORLD/CHARACTER_WIKI/`)

The subterranean facility "The Hand of Change" is structured across 8 operational floors, led by the **Nine Echo-Cores**:

| Echo-Core / Lead | File Name | Role & Department | Key Attributes |
|---|---|---|---|
| **Ayshuk** | `THE_DIRECTOR.md` | Director of Facility 01 | Executive Command, Dawn Protocol, Sovereign Authority |
| **Seiyon** | `THE_SECRETARY.md` | Chief Secretary / Central Command | Operations Coordination, Schedule & Records, Liaison |
| **Majin** | `THE_CONTAINMENT_LEAD.md` | Floor 1: Containment Lead | Primary Suppression, Physical Restraint, Safety Enforcer |
| **Dekan** | `THE_ARCHIVE_LEAD.md` | Floor 2: Archive Lead | Historical Data, Anomaly Cataloging, Memory Protection |
| **Mellda** | `THE_EXTRACTION_LEAD.md` | Floor 3: Extraction Lead | Han Energy Refining, M.A.W. Materialization, Forge Master |
| **Ishall** | `THE_RESEARCH_LEAD.md` | Floor 4: Research Lead | Behavioral Insight, Biological Analysis, Tech Development |
| **Marjuk** | `THE_BORDER_LEAD.md` | Floor 5: Border Watch Lead | Perimeter Security, Perimeter Quarantine, Incursion Defense |
| **Zyrak** | `THE_EXILE.md` | Floor 6: Deep Vault Lead | Black-level Quarantine, Isolation Chambers, Forbidden Artifacts |
| **Xyan** | `THE_OUTSIDER.md` | Floor 8: Gate Watch Lead | Threshold Surveillance, Exterior Horizon Monitoring, Gate Defense |

---

## M.A.W. Equipment System (`SOMNARAK-WORLD/M.A.W. Codex_Set Registry/`)

The **Materialized Armament of Woe (M.A.W.)** registry contains complete equipment sets extracted from Sorrow Entities. Each set follows a strict quadripartite structure:

```
Registry_<Range>/<Set_ID>_<Entity_Name>/
├── SE-<ID>-A__SIDE_CODEX_<Entity>.md       # Entity source lore, extraction prerequisites, identity
├── SE-<ID>-B__MAW-W_<Weapon_Name>.md       # Weapon: Form, speed/range, damage element, special attacks
├── SE-<ID>-C__MAW-S_<Suit_Name>.md         # Suit: Resistances, endurance ratings, protective traits
└── SE-<ID>-D__MAW-G_<Gift_Name>.md         # Gift: Slot (Head/Eye/Neck/etc.), resonance buff, appearance
```

### Damage & Resistance Affinity System
Equipment and combat in Somnarak utilize four canonical energy types derived from Han:
- **Grudge (원한 / 怨恨)**: Physical, kinetic sorrow. Crushing and cutting forces.
- **Lament (비탄 / 悲歎)**: Psychological, weeping sorrow. Attacks sanity and coherence.
- **Void (공허 / 空虛)**: Structural, erasing sorrow. Dual physical and mental breakdown.
- **Weight (비중 / 悲重)**: Existential, gravitational sorrow. Percentage-based, irreversible burden.

---

## Core Canon Lexicon

When reviewing or expanding the Somnarak universe, adhere strictly to Somnarak-native terminology:

- **Somnarak (솜나락)**: The City of Unresolved Sorrow. Built over The Maw and the subterranean Weeping River.
- **Han (한 / 恨)**: The primordial sorrow-energy that fuels the city's industry, drives entity emergence, and powers M.A.W. gear.
- **Sorrow Entity (SE)**: Anomalous manifestations condensed from human sorrow, regret, and the Weeping River. Classified by SECC codes and threat levels: `ZAYIN` (I), `TETH` (II), `HE` (III), `WAW` (IV), `ALEPH` (V).
- **M.A.W. (Materialized Armament of Woe)**: Weapons, suits, and gifts stabilized from entity resonance.
- **Absolvohan (해한 / 解恨)**: The metaphysical release and purification of unresolved sorrow; the culmination of the Dawn Initiative.
- **The Reverie Directorate (몽환국 / 夢幻局)**: The governing apparatus that administers Facility 01 and citywide Han allocation.
- **Facility 01 ("The Hand of Change")**: The primary subterranean containment and extraction complex.
- **Ordeals (시련 / 試練)**: Scheduled anomalous phenomena categorized by five colors (Black, Blue, Grey, Pale, Purple) and four watches (First Watch, Second Watch, Third Watch, Tide Watch).

---

## Local Navigation & Tooling

To explore, audit, and search the markdown corpus efficiently from the terminal:

```bash
# Run the complete archive health audit
python3 tools/audit_lore_archive.py

# Verbose audit showing set details
python3 tools/audit_lore_archive.py --verbose

# Export audit results as JSON
python3 tools/audit_lore_archive.py --json

# Search for an entity or concept across all reference files
grep -rn "Absolvohan" "SOMNARAK-WORLD/"

# List all master codices in 07_Reference
ls -lh "SOMNARAK-WORLD/07_Reference"
```

---

## Working Rules & Contribution Guidelines

All work on this repository is governed by the following binding documents:

1. **Rule A0: Push Always** (`RULE-TO-FOLLOW.md`): Every file creation, edit, or deletion must be committed and pushed to the assigned session branch in the same turn.
2. **Rule A5: File Safety** (`RULE-TO-FOLLOW.md`): Never delete or overwrite canon source files or owner archives without explicit instruction.
3. **Session Fragility Precautions** (`SESSION_BREAK_PRECAUTION.md`): Keep units of work small, commit often, and maintain an accurate ledger.
4. **Authentic Terminology** (`REFERENCE_SOMNARAK_WIKI/CONTENT_AND_VISUAL_STANDARDS.md`): Retain canonical Somnarak nomenclature across all files.
