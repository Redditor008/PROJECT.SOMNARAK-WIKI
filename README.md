# Project Somnarak — Non-Wiki Canon & Reference Archive

Welcome to the **Canonical Lore & Reference Source Archive** for **Project Somnarak** (소마나락), maintained on the `NON-WIKI` branch.

This repository serves as the authoritative, durable database and narrative foundation for the Somnarak universe (~3.5 million words). It houses the pure markdown source corpus for all cosmological frameworks, entity dossiers, equipment registries, and departmental records.

---

## Repository Architecture

The repository is cleanly divided into two master trees:

| Directory | Role | Contents |
|---|---|---|
| **`SOMNARAK-WORLD/`** | **100% In-Universe Narrative & Operational Source** | Official containment dossiers, master codices, equipment sets, and Echo-Core records written entirely from within the Somnarak universe. |
| **`REFERENCE_SOMNARAK_WIKI/`** | **Out-of-Universe Editorial Standards & Technical Audits** | Structural taxonomy, entity catalogs, paired-dossier audits, transfer manifests, and multi-agent handoff protocols. |

---

## Archive Metrics at a Glance

- **1,891 total markdown files** across `SOMNARAK-WORLD` and `REFERENCE_SOMNARAK_WIKI`
- **Over 3.7 million words** of structured, canonical lore
- **31 In-Universe Master Codices** (`SOMNARAK-WORLD/Master_Codices/`) establishing the entire cosmology, geopolitical landscape, and physical laws of Somnarak
- **9 Absolvohan Narrative Volumes** (`SOMNARAK-WORLD/The_Absolvohan/`), chronicling the full Day 0 through Day 365+ journey of Director Majin and Secretary Seiyon across the 1,778th and final Cycle
- **529 Sorrow Entity Dossiers** (`SOMNARAK-WORLD/Sorrow_Entities/`), representing 285 unique canonical entities across threat levels ZAYIN through ALEPH
- **291 M.A.W. Equipment Sets** (`SOMNARAK-WORLD/MAW_Codex_Sets/`, 1,196 files across 42 registry groups), cataloging Weapons, Suits, and Gifts
- **60 Five-Color Ordeal Files** (`SOMNARAK-WORLD/Ordeals/`), documenting First, Second, Third, and Tide watches
- **14 Hope Transformation Records** (`SOMNARAK-WORLD/Hope_Transformations/`), detailing resonant ascensions
- **9 Echo-Core Dossiers** (`SOMNARAK-WORLD/Echo_Cores/`), covering the departmental leadership of Facility 01 ("The Hand of Change")
- **8 Unknown Anomaly Records** (`SOMNARAK-WORLD/Unknown_Entities/`), containing unclassified deep-abyss occurrences

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
├── SOMNARAK-WORLD/                         # 100% In-Universe Narrative & Operational Source Corpus (1,860+ files)
│   ├── README.md                           # In-world archive guide & recommended reading order
│   ├── Master_Codices/                     # 35 Macro-Canon Master Codices: Cosmology, Factions, Systems
│   ├── The_Absolvohan/                     # 9 Chronological Narrative Volumes (Day 0–365 & Epilogue)
│   ├── The_SED/                            # 7 Subterranean Descent Passages & Field Guide (Exploration Arcs 1–7)
│   ├── The_UCD/                            # 6 Underworld Pacification Operations & Tactics Guide (Purge Arcs 1–6)
│   ├── Sorrow_Entities/                    # 529 Entity files: Dossiers, tales, and containment data
│   ├── Echo_Cores/                         # 9 Echo-Core files: Facility 01 departmental leaders
│   ├── MAW_Codex_Sets/                     # 1,196 files across 42 registry folders (A/B/C/D quadripartite sets)
│   ├── Ordeals/                            # 60 Ordeal files: Black, Blue, Grey, Pale, Purple (1st–Tide Watches)
│   ├── Hope_Transformations/               # 14 Hope Transformation files: HT-001 through HT-012, Trinity & Hand
│   └── Unknown_Entities/                   # 8 Unknown Entity files: UNK-248 through UNK-903 & Dramaturgy
│
└── REFERENCE_SOMNARAK_WIKI/                # Out-of-World Editorial Standards, Audits & Catalogs
    ├── README.md                           # Overview of the reference standards folder
    ├── ABSOLOVHAN_REPAIR_NOTES.md          # Canon harmonization and repair notes for Absolvohan texts
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
    ├── PUBLIC_PAGE_COMPLIANCE_AUDIT_2026-08-31.md     # Historical compliance audit
    ├── REGISTRY_MASTER_STATUS.md           # M.A.W. Registry completion and archive tracking
    ├── SOMNARAK_CORPORATIONS_GAME_DESIGN_FRAMEWORK.md # Original design document for the 3 corporations
    ├── SOMNARAK_DOCUMENT_RULES.md          # Archival classification & authoring rules for entity files
    ├── SOMNARAK_MAIN_ENTITY_PROTECTED_LIST.md # Authoritative list of 55 immutable core entities
    └── SOMNARAK_NAME_REGISTRY.md           # Authoritative nomenclature & character naming lexicon
```

---

## Macro-Canon Master Codices (`SOMNARAK-WORLD/Master_Codices/`)

The foundational source texts located in `SOMNARAK-WORLD/Master_Codices/` establish the core in-world canon of Somnarak. Every entity, piece of equipment, and district event derives from these texts:

| Codex File Name | Focus & Subject Matter | Key Topics Covered |
|---|---|---|
| `PROJECT_SOMNARAK.md` | Master Worldbuilding Core (5,502 lines) | The Grand Cosmology, 5 Layers, The Maw, The Weeping, Universal Laws |
| `The_REVERIE_DIRECTORATE.md` | Facility 01 Corporate Dossier (3,073 lines) | Subterranean Facility 01, 8 Floors, 9 Echo-Core attendants, containment systems |
| `SOMNARAK_ABSOLOVHAN.md` | Absolvohan 366-Day Master Story & Gameplay | Resonant Clash, Day 0 to Day 365, Critical Threshold, the Hand of Hope |
| `The_SOMNARAK_EXPLORATION_DECREED.md` | SED Corporate Dossier | Three-tier subterranean descent doctrine, specialized survey gear, 7-member explorer cadre |
| `SOMNARAK_SED_PASSAGES.md` | SED Seven Descents Master Story & Gameplay | Passages 1–7: The Undercity, Forgotten Districts, Hidden Routes, Deep Gardens, Scar, Source |
| `The_UNDERWORLD_CLEANUP_DESCEND.md` | UCD Corporate Dossier | Three-phase reclamation doctrine, urban pacification weaponry, 6-officer task force cadre |
| `SOMNARAK_UCD_PACIFICATION.md` | UCD Six Pacifications Master Story & Gameplay | Operations 1–6: Veil Merchants, Memory Washers, Harvesters, Debt Brokers, Entity Traders, King |
| `SOMNARAK_BATTLE_SYSTEM.md` | Combat Engine & Damage Types | 4 Damage Elements (Grudge, Lament, Void, Weight), Formations |
| `SOMNARAK_CHEONGULA.md` | The First Sorrow & The Maw Cataclysm | Historical origin of Cheongula, the Maw, and the First Sorrow |
| `SOMNARAK_CORPORATIONS.md` | The Three Corporations Doctrine | Reverie Directorate (R.D.), Exploration (SED), Enforcement (UCD) |
| `SOMNARAK_DAILY_LIFE.md` | Civilian Life & Urban Culture | Food synthesis, fashion, acoustic curfews, districts, and slang |
| `SOMNARAK_DAWN_OF_HOPE.md` | Year 4,238 & The Dawn Initiative | The 1,778-cycle loop resolution and the 45% healing threshold |
| `SOMNARAK_DREAM_REALM.md` | The Ethereal Dream Substratum | Dream-diving, Weavers Guild, ethereal entities, sleep phenomena |
| `SOMNARAK_ENEMY_LIST.md` | Adversary Compendium | Undercity threats, feral constructs, rogue operators, Outskirts beasts |
| `SOMNARAK_ENTITIES.md` | Entity Group Taxonomy & Chains | Connected entities, resonance chains, 5 Coherence levels (I to V) |
| `SOMNARAK_ENTITY_CODEX.md` | Comprehensive Classification Codex | SECC breakdown, work affinities, and containment guidelines |
| `SOMNARAK_ENTITY_TALES.md` | Master Origin Lore Anthology | Tripartite structure: 이야기 (Tale), 증언 (Testimony), 기록 (Record) |
| `SOMNARAK_FACTION_RELATIONS.md`| Faction Geopolitical Matrix | Power balances, treaties, debts, and hostilities between groups |
| `SOMNARAK_FACTION_TECH.md` | Institutional Technology Specifications| Acoustic dampening, basalt extraction, silk weaving, barrier rigs |
| `SOMNARAK_HAN_RELICS.md` | Ancient Sovereign Artifacts | Pre-Structuring relics, properties, containment protocols |
| `SOMNARAK_HORIZON_CARAVAN.md` | Nomad Traders & Desert Outposts | Exterior trade routes, desert navigation, and frontier survival |
| `SOMNARAK_MAW_CODEX.md` | Master Armory & Extraction Engine | M.A.W. Weapon archetypes, suit weave defense ratings, gift slots |
| `SOMNARAK_MEMORY_ARCHIVE.md` | Pre-Cataclysm Historical Logs | Fragmentary memory transcripts from before the First Cycle |
| `SOMNARAK_NAMED_FRACTURES.md` | Historical Tragic Figures | Named citizens who underwent catastrophic psychological Fracture |
| `SOMNARAK_ORDEALS_FRAMEWORK.md` | Five-Color Ordeal Defense | Tactical mechanics for Blue, Black, Pale, Grey, and Purple Ordeals |
| `SOMNARAK_SED.md` | Somnarak Exploration Decreed | Deep subterranean reconnaissance, Maw descents, expedition teams |
| `SOMNARAK_TABOO_RESONANCE.md` | Seven Taboos & Resonances | Absolute civic laws, acoustic censorship, and the Giltong Enforcers |
| `SOMNARAK_THE_DESOLATE.md` | The Wasteland Beyond the Walls | The Scar, toxic Han-dust storms, nomad clans, and Kael's Kingdom |
| `SOMNARAK_THE_DOORSPEECH.md` | Linguistic Censorship & Acoustic Control| Verbal taboos, speech filtration, and the Acoustic Enforcers |
| `SOMNARAK_THE_WEEPING.md` | Subterranean River of Liquid Han | Hydrology of grief, crystallization points, and entity genesis |
| `SOMNARAK_UCD.md` | Underworld Cleanup Descend | Tactical purge operations targeting the criminal syndicates and Frays |
| `SOMNARAK_UNDERWORLD.md` | Subterranean Slums & The Raw | Menders, Frays, Memory Washers, Veil Merchants, and Debt Brokers |
| `SOMNARAK_UNKNOWN_CITIES.md` | Sister Cities (Cheonbulok, Mugeukji) | External geopolitics, refugee enclaves, and forgotten city-states |
| `SOMNARAK_WOUND_WALKERS.md` | Order of Wandering Healers | The monastic order sworn to absorb and transmute human sorrow |
| `The_REVERIE_DIRECTORATE.md` | Facility 01 Internal Structure | Floor-by-floor layout, Echo-Core profiles, and emergency protocols |

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

3. **Threat Classifications (위협 등급):**
   - **`ZAYIN` (I):** Negligible threat; passive resonance; minimal containment risk.
   - **`TETH` (II):** Low-to-moderate threat; standard suppression squads sufficient.
   - **`HE` (III):** Significant threat; lethal capabilities; disciplined work required.
   - **`WAW` (IV):** Critical threat; severe psychological degradation; catastrophic breach hazard.
   - **`ALEPH` (V):** Existential threat; facility-wide or district-wide collapse potential.

4. **M.A.W. Equipment Triad (비탄의 무장):**
   - **MAW-W (Weapon):** Offense crystallized from the entity's core sorrow.
   - **MAW-S (Suit):** Armor woven from the entity's resonance, conferring elemental defenses.
   - **MAW-G (Gift):** Resonant accessory granting passive traits and cosmetic marks.

---

## Developer Verification Tools

To audit file integrity, master codices, M.A.W. quadripartite sets, and entity counts:

```bash
# Run the full archive audit (all 1,880 markdown files)
python3 tools/audit_lore_archive.py

# Run with verbose set breakdown
python3 tools/audit_lore_archive.py --verbose

# Export audit report as structured JSON
python3 tools/audit_lore_archive.py --json
```

---

## Operating Rules for AI & Contributors

1. **Push Always (Rule A0):** Every modification, creation, or deletion must be committed and pushed in the same turn.
2. **File Safety (Rule A5):** Never delete canonical reference files without direct owner instruction.
3. **Immutability of Canon:** Never replace authentic Somnarak terminology with generic placeholders. Retain all native nomenclature (Sorrow Entities, Han, Absolvohan, M.A.W., Reverie Directorate).
