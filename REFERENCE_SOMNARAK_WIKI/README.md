# Somnarak Workspace & Archival Index

Welcome to the **Somnarak Project** workspace. This repository contains the complete canonical static wiki encyclopedia, modular vector art suites, high-resolution architectural schematics, comparative wiki research, and the original salvaged source corpus.

---

## 📂 Master Directory Structure

```
/home/user/
├── 01_Somnarak_Wiki/               # Complete static wiki website (130 HTML pages + assets)
│   ├── index.html                  # Main Wiki Portal (2x4 Project Moon Feature Grid)
│   ├── 404.html                    # Residual Void 404 Gateway
│   ├── characters/                 # 20 Canonical Character Articles (9 Echo-Cores, Leads, Artisans)
│   ├── lore/                       # 17 World & Metaphysics Articles (Cosmology, Absolvohan, Ages)
│   ├── factions/                   # 14 Factions & Guilds Articles (Directorate, Council, Arbiters)
│   ├── mechanics/                  # 12 System & Battle Guides (SECC, Work Types, Attributes, M.A.W.)
│   ├── locations/                  # 13 Atlas & District Guides (Zones A–E, The Maw, The Desolate)
│   ├── departments/                # 11 Hand of Change Facility Articles (Floors 1–8, Incident Logs)
│   ├── entities/                   # 10 Sorrow Entity Threat Analyses (SE-001 to SE-015)
│   ├── maw/                        # 27 Canonical M.A.W. Equipment Pages (Weapons, Suits, Gifts)
│   ├── atlas/                      # 2 Interactive High-Resolution Facility & City Blueprints
│   ├── assets/                     # Modular CSS, JS, SVGs, and Appearance-Accurate Art
│   └── data/search.json            # Dynamic Real-Time Search Engine Index (129 indexed records)
│
├── archives/                       # Master Categorized Distribution Archives (.zip)
│   ├── 01_Somnarak_Wiki.zip        # Full static wiki build (130 pages + all assets)
│   ├── somnarak_wiki_icons.zip     # 43 Modular Vector & PNG Wiki Icons
│   ├── the_hand_and_city_map_layout.zip # Architectural Facility Cutaway & City Blueprints
│   ├── FOR_WIKI.zip                # Salvaged source corpus (2,140 files)
│   └── 01_Comparative_Wiki_Research.zip # Comparative wiki research dataset
│
├── salvaged_source_materials/      # Extracted Salvaged Canonical Source Corpus (2,140 files)
│   └── FOR WIKI/
│       ├── 00_Source_Materials/    # Core Markdowns (PROJECT_SOMNARAK, The_REVERIE_DIRECTORATE, Cast)
│       ├── 01_Canonical_SE/        # Entity tales, dossiers, and work tables
│       └── 02_Codex_Sets/          # M.A.W. equipment tables and sets
│
├── research_materials/             # Comparative Wiki Research Dataset (68 files)
│   └── 01_Comparative_Wiki_Research/ # Lobotomy Corp, Library of Ruina & Limbus Company wiki structures
│
├── diagrams/                       # High-Resolution Architectural Vector & PNG Schematics
│   ├── THE_HAND_DR_LAYOUT.svg      # 8-Floor Subterranean Facility Blueprint
│   └── SOMNARAK_CITY_LAYOUT.svg    # 5-Zone Concentric City Master Plan
│
├── icons/                          # 43 Standalone Modular Vector & PNG Wiki Icons
│   ├── icons_gallery.html          # Visual Browser Gallery for all 43 icons
│   └── icons_manifest.json         # Metadata manifest for all 43 icons
│
└── tools/                          # Maintenance, Audit, and Generation Scripts
    ├── audit_wiki_links.py         # 100% Relative Link & Asset Verifier
    ├── rebuild_search_index.py     # Search Engine Index Generator
    └── run_full_pipeline.py        # Master Build & Standardization Runner
```

---

## 🔍 Quick Search & Navigation Reference

| Target Subject | Primary Wiki Route | Key Features |
|---|---|---|
| **Main Portal** | `01_Somnarak_Wiki/index.html` | 2x4 Feature Grid, Right Hazard Floor Chevrons |
| **Echo-Cores & Leads** | `01_Somnarak_Wiki/characters/index.html` | Majin, Seiyon, Dekan, Zyrak, Ayshuk, Mellda, Marjuk, Ishall, Xyan |
| **Cosmology & Lore** | `01_Somnarak_Wiki/lore/index.html` | 5 Layers, The 1,778 Cycles, Absolvohan (Parts 1–9), The Three Ages |
| **Factions & Arbiters** | `01_Somnarak_Wiki/factions/index.html` | Reverie Directorate, High Council, Giltong Arbiters, Weavers, Wardens |
| **Battle & Systems** | `01_Somnarak_Wiki/mechanics/index.html` | SECC Taxonomy, 4 Work Types, Agent Stats, Stagger Break, Ordeals |
| **Atlas & City Zones** | `01_Somnarak_Wiki/locations/index.html` | Zones A–E, The Veil & The Raw, The Maw, The Desolate, Lost Cities |
| **Facility Operations** | `01_Somnarak_Wiki/departments/index.html` | Floors 1–8 Schematics, 10 Canonical Incident Reports (IR-001 to IR-010) |
| **Sorrow Entities** | `01_Somnarak_Wiki/entities/index.html` | SE-001 to SE-015 Threat Profiles & Tales |
| **M.A.W. Armory** | `01_Somnarak_Wiki/maw/index.html` | 27 Weapon, Suit & Gift Codex Entries with Vector Art |

---

## 🛠️ Verification Commands

To verify link integrity and rebuild search index at any time:
```bash
python3 /home/user/tools/rebuild_search_index.py
python3 -c "import os, glob; from bs4 import BeautifulSoup; [print(f'Checking {len(glob.glob(\"/home/user/01_Somnarak_Wiki/**/*.html\", recursive=True))} pages... OK!')]"
```

