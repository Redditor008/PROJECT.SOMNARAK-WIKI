# DEVELOPMENT.md — Somnarak Non-Wiki Archive Development Handbook

> **Repository Governance Gateway:** For the top-level index connecting all repository governance files, see [`GOVERNANCE.md`](GOVERNANCE.md).

> **Read this file first.** It is the standing handoff for AI/developer sessions
> working on the `NON-WIKI` branch of `PROJECT.SOMNARAK-WIKI`: repository architecture,
> canon source standards, file structures, verification methods, and operating rules.
> Keep it current: when a future session changes any standing convention, update
> the relevant section in the same commit.

---

## 1. Architecture of Project Somnarak

Project Somnarak is maintained across two primary branches in `Redditor008/PROJECT.SOMNARAK-WIKI`:

| Branch | Identity | Contents | Role |
|---|---|---|---|
| **`main`** | Web Wiki Frontend | `docs/`, static HTML/CSS/JS, vector art, web search | Serves the public encyclopedia via GitHub Pages (1,040+ pages) |
| **`NON-WIKI`** (This Branch) | Canon Lore & Reference Archive | `SOMNARAK-WORLD/`, `REFERENCE_SOMNARAK_WIKI/`, master codices, registries | The pure, authoritative markdown source library (~3.5M words) |

The `NON-WIKI` branch is stripped of web build scripts, HTML pages, and frontend bundles. It serves as the durable database and narrative foundation for the Somnarak universe.

- **Owner:** Redditor008.
- **Assigned Session Branch:** Arena sessions operate on their assigned session branch (`arena/<id>-project-somnarak-wiki`), committed and pushed directly.

---

## 2. Repository Layout on `NON-WIKI`

```
PROJECT.SOMNARAK-WIKI/ (NON-WIKI branch)
├── README.md                               # Master archive index, canon guide & directory overview
├── DEVELOPMENT.md                          # This development handbook
├── INSTALL_PERCENTAGE_REPORT.md            # Coverage audit measuring reference content in the wiki
├── RULE-TO-FOLLOW.md                       # Owner's binding operating rules (v2: Push-Always doctrine)
├── UNIVERSAL_FOLLOW_RULE.md                # Portable AI baseline operating rules
├── SESSION_BREAK_PRECAUTION.md             # Session break, recovery protocol & work ledger
├── CHANGELOG.md                            # Release notes & batch modification history
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
│   ├── audit_lore_archive.py               # Standalone Python auditor (UTF-8, codices, M.A.W., entities)
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
│   ├── Master_Codices/                     # 39 Macro-Canon Master Codices across 6 canonical subfolders
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
│   ├── Sorrow_Entities/                    # 287 Unique Entity dossiers across Ranks I to V and Grades α to ω
│   ├── Echo_Cores/                         # 9 Echo-Core files: Facility 01 departmental leaders
│   ├── MAW_Codex_Sets/                     # 1,196 files: 198 complete quadripartite sets across 42 folders
│   ├── Ordeals/                            # 60 Ordeal files: Black, Blue, Grey, Pale, Purple (1st–Tide Watches)
│   ├── Hope_Transformations/               # 14 Hope Transformation files: HT-001 through HT-012, Trinity & Hand
│   └── Unknown_Entities/                   # 15 Unknown Entity files: UNK-248 to UNK-903 & Regressor chronicles
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

## 3. Standing Owner Rules (Binding on All Sessions)

1. **A0 — Push Always:** Every single file creation, edit, rename, or deletion must be committed **and pushed** to the assigned session branch in the same turn. Never end a turn with uncommitted changes or unpushed local commits.
2. **A5 — File Safety:** Never delete or overwrite owner files or canonical reference documents without an explicit, file-named instruction from the owner.
3. **Canon Terminology is Immutable:** Retain authentic Somnarak-native terminology across all documentation:
   - Sorrow Entities (SE), SECC designations with Origin Scopes (C: City Sorrow / 도한, N: Inner Sorrow / 내한, O: Outside Sorrow / 외한), Coherence Ranks (I: Whisper, II: Murmur, III: Fragment, IV: Entity, V: Sovereign), and Potency Grades (α to ω).
   - M.A.W. (Materialized Armament of Woe), Weapons (W), Suits (S), Gifts (G).
   - Han energy, Liquid Han, Absolvohan, Resonant Clash.
   - Facility 01 ("The Hand of Change"), Reverie Directorate, High Council.
   - Four damage elements: Grudge (원한), Lament (비탄), Void (공허), Weight (비중).
4. **Source-Led Integrity:** Content in markdown files derives strictly from the canonical texts in `SOMNARAK-WORLD/` or established Somnarak lore. Never inject generic placeholder filler.
5. **Folder Distinction:** All in-world lore files belong in `SOMNARAK-WORLD/`. Out-of-world meta documents, audits, and handoffs belong in `REFERENCE_SOMNARAK_WIKI/`.
6. **Master Macro-Chronological Partition & Cycle Localization:** All Three SED (Katabagil), UCD (Katharcheok), and R.D. (The Absolvohan Facility 01) occur strictly **BEFORE** the Dawn of Hope in sequential progression (SED -> UCD -> R.D.). **ANYTHING ELSE** (The Dawn Initiative & The Lantern, The Horizon Caravan, The Memory Archive realizations, The Wound Walkers, continental expansion) occurs strictly **AFTER** the Dawn of Hope. **UNK SE is positioned strictly AFTER R.D.** (manifesting in the Post-R.D. / Post-Dawn era). The 1,778 Mnemonic Cycles belong strictly and exclusively to R.D. + The Absolvohan (Facility 01); outside entities and post-Dawn wings do not measure calendar time by Cycles, though retrospective historical/aftermath references to the R.D. loop (e.g., survivor memories, regressor records) are canonical and permitted. Continental geography is strictly terrain and not an SE.

---

## 4. Working with the In-World Canon Repositories (`SOMNARAK-WORLD/`)

### A. The Master Codices (`SOMNARAK-WORLD/Master_Codices/`)
- These 45 master files organized across 6 canonical subfolders establish the cosmological, physical, municipal, and political framework of Somnarak.
- When referencing world rules, always cite the corresponding codex path (e.g., `SOMNARAK-WORLD/Master_Codices/01_Cosmology_and_World_Order/PROJECT_SOMNARAK.md` for cosmology, `SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_BATTLE_SYSTEM_STYLES.md` for combat mechanics, `SOMNARAK-WORLD/Master_Codices/02_Institutional_Wings_and_Chronicles/The_REVERIE_DIRECTORATE.md` for Facility 01 floors, `SOMNARAK-WORLD/Master_Codices/01_Cosmology_and_World_Order/SOMNARAK_GEOLOGY.md` for planetary geology, `SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_WORKSHOPS.md` for non-M.A.W. equipment and artisan forge systems, `SOMNARAK-WORLD/Master_Codices/04_Municipal_Society_and_Demographics/SOMNARAK_UNDERWORLD_SYNDICATES.md` for underworld factions and extralegal governance, `SOMNARAK-WORLD/Master_Codices/04_Municipal_Society_and_Demographics/SOMNARAK_SPECIALIST_CADRES.md` for chartered contractor bureaus, `SOMNARAK-WORLD/Master_Codices/04_Municipal_Society_and_Demographics/SOMNARAK_ZONE_CORPORATIONS.md` for the 25 municipal zone corporations, Haz-scorchers, Cleansers, and Giltong arbiter authority).

### B. Sorrow Entity Files (`SOMNARAK-WORLD/Sorrow_Entities/`)
- Filename convention: `SE-<SECC Code>_<English Name>_<Korean Name>.md` (e.g. `SE-C-IIIβ-014_The_Debt_Eater_빚을_먹는_자.md`).
- Entities carry containment procedures, work affinities (Ferrehan, Flerehan, Pugnahan, Viderehan), breach behaviors, and narrative tales.

### C. M.A.W. Codex Sets (`SOMNARAK-WORLD/MAW_Codex_Sets/`)
- Each set folder is organized under a registry range (e.g. `Registry_001_to_007/001_The_Orphaned_Bell/`).
- Every complete set contains four files:
  - `SE-<ID>-A__SIDE_CODEX_<Name>.md`: The donor entity's lore and extraction parameters.
  - `SE-<ID>-B__MAW-W_<Weapon>.md`: Weapon specs (damage element, range/speed band, special moves).
  - `SE-<ID>-C__MAW-S_<Suit>.md`: Suit defenses, elemental resistances, and passive traits.
  - `SE-<ID>-D__MAW-G_<Gift>.md`: Gift slot, resonance triggers, and appearance.

### D. Five-Color Ordeals (`SOMNARAK-WORLD/Ordeals/`)
- Ordeals are organized by color: `BLACK` (Weight), `BLUE` (Lament), `GREY` (Grudge), `PALE` (Void), and `PURPLE` (Mixed).
- Each color contains entities for four watches: `First_Watch`, `Second_Watch`, `Third_Watch`, and `Tide_Watch`.

### E. Facility 01 Echo-Cores (`SOMNARAK-WORLD/Echo_Cores/`)
- Contains detailed dossiers on the 9 Echo-Cores: Director Majin (Floor 1), Secretary Seiyon, Dekan (Floor 2), Zyrak (Floor 3), Mellda (Floor 5), Marjuk (Floor 6), Ayshuk (Floor 4), Ishall (Floor 7), and Xyan (Floor 8).

---

## 5. Verification & Inspection Recipes

Use standard Python 3 and bash tools to inspect, verify, and audit the markdown files:

```bash
# 1. Run the master archive audit (UTF-8, codices, M.A.W. sets, entity counts)
python3 tools/audit_lore_archive.py

# 2. Verbose audit listing incomplete or exception sets
python3 tools/audit_lore_archive.py --verbose

# 3. Export structured audit data as JSON
python3 tools/audit_lore_archive.py --json

# 4. Search for references to a specific entity or concept across all files
grep -rn "SE-001" "SOMNARAK-WORLD/"
```

---

## 6. Git Workflow & Turn Discipline

1. **Check branch state at turn start:**
   ```bash
   git branch --show-current
   git status --short
   ```
2. **Make required modifications.** Validate file structure and encoding.
3. **Run pre-commit gate:**
   ```bash
   python3 tools/audit_lore_archive.py
   git diff --check
   ```
4. **Commit with clean messages:** Use plain single quotes; do not use backticks.
5. **Push immediately:**
   ```bash
   git push origin <assigned-branch>
   ```
6. **Verify push:**
   ```bash
   git rev-parse HEAD
   git rev-parse origin/<assigned-branch>
   ```
   Both hashes must match before ending the turn.
