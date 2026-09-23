# DEVELOPMENT.md — Somnarak Non-Wiki Archive Development Handbook

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
├── tools/                                  # Non-wiki developer tools
│   └── audit_lore_archive.py               # Standalone Python auditor (UTF-8, codices, M.A.W., entities)
│
├── SOMNARAK-WORLD/                         # 100% In-Universe Narrative & Operational Source Corpus (1,860+ files)
│   ├── README.md                           # In-world archive guide & recommended reading order
│   ├── Master_Codices/                     # 31 Macro-Canon Master Codices (Cosmology, Directorate, Systems)
│   ├── The_Absolvohan/                     # 9 Chronological Narrative Volumes (Day 0–365 & Epilogue)
│   ├── Sorrow_Entities/                    # 529 files: SE-001 through SE-997 dossiers & tales
│   ├── Echo_Cores/                         # 9 files: The Nine Echo-Cores of Facility 01
│   ├── MAW_Codex_Sets/                     # 1,196 files: 42 registry folders with A/B/C/D item sets
│   ├── Ordeals/                            # 60 files: Black, Blue, Grey, Pale, Purple (1st–Tide Watches)
│   ├── Hope_Transformations/               # 14 files: HT-001 to HT-012, Trinity, and Hand of Hope
│   └── Unknown_Entities/                   # 8 files: UNK-248 to UNK-903 & Regressor Log
│
└── REFERENCE_SOMNARAK_WIKI/                # Out-of-World Editorial Standards, Audits & Catalogs
    ├── README.md                           # Overview of the reference standards folder
    ├── ABSOLOVHAN_REPAIR_NOTES.md          # Canon harmonization and repair notes for Absolvohan texts
    ├── SORROW_ENTITIES_CATALOG.md          # Complete indexed catalog of all 285 unique Sorrow Entities
    ├── SORROW_ENTITIES_PAIRS_AUDIT.md      # Detailed audit and resolution guide for the 241 paired entity files
    ├── ALL_34_REFERENCE_FILES_AUDIT.md     # Line-by-line audit of the foundational codices
    ├── ALL_FILES_AUDIT_MANIFEST.md         # Comprehensive manifest of all reference files
    ├── CATEGORY_AND_PAGE_PLAN.md           # Information architecture & classification plan
    ├── CONTENT_AND_VISUAL_STANDARDS.md     # Narrative, terminological, and visual standards
    ├── LIVE_DEPLOYMENT_AND_BRANCH_POLICY.md# Branch policy and deployment acceptance standards
    ├── MASTER_HANDOFF_PROTOCOL.md          # Multi-session continuity protocol
    ├── MAW_PERSONALIZE_PROGRESS.md         # Weapon personalization ledger
    ├── MAW_WEAPON_ARCHETYPES.md            # Weapon archetype taxonomy and research
    ├── OPERATING_RULES.md                  # Canon integrity & directory rules
    ├── PROJECT_MOON_WIKI_NESTED_PLACEMENT_RESEARCH.md # Structural comparative research
    ├── PUBLIC_PAGE_COMPLIANCE_AUDIT_2026-08-31.md     # Public page compliance audit
    ├── REGISTRY_MASTER_STATUS.md           # M.A.W. Registry completion tracking
    ├── SOMNARAK_CORPORATIONS_GAME_DESIGN_FRAMEWORK.md # Original comparative design document
    ├── SOMNARAK_DOCUMENT_RULES.md          # Archival classification & authoring rules for entity files
    ├── SOMNARAK_MAIN_ENTITY_PROTECTED_LIST.md # Authoritative list of 55 immutable core entities
    └── SOMNARAK_NAME_REGISTRY.md           # Authoritative nomenclature & character naming lexicon
```

---

## 3. Standing Owner Rules (Binding on All Sessions)

1. **A0 — Push Always:** Every single file creation, edit, rename, or deletion must be committed **and pushed** to the assigned session branch in the same turn. Never end a turn with uncommitted changes or unpushed local commits.
2. **A5 — File Safety:** Never delete or overwrite owner files or canonical reference documents without an explicit, file-named instruction from the owner.
3. **Canon Terminology is Immutable:** Retain authentic Somnarak-native terminology across all documentation:
   - Sorrow Entities (SE), SECC designations, Coherence Ranks (I: Whisper, II: Murmur, III: Fragment, IV: Entity, V: Sovereign), and Potency Grades (α to ω).
   - M.A.W. (Materialized Armament of Woe), Weapons (W), Suits (S), Gifts (G).
   - Han energy, Liquid Han, Absolvohan, Resonant Clash.
   - Facility 01 ("The Hand of Change"), Reverie Directorate, High Council.
   - Four damage elements: Grudge (원한), Lament (비탄), Void (공허), Weight (비중).
4. **Source-Led Integrity:** Content in markdown files derives strictly from the canonical texts in `SOMNARAK-WORLD/` or established Somnarak lore. Never inject generic placeholder filler.
5. **Folder Distinction:** All in-world lore files belong in `SOMNARAK-WORLD/`. Out-of-world meta documents, audits, and handoffs belong in `REFERENCE_SOMNARAK_WIKI/`.

---

## 4. Working with the In-World Canon Repositories (`SOMNARAK-WORLD/`)

### A. The Master Codices (`SOMNARAK-WORLD/Master_Codices/`)
- These 31 master files establish the cosmological, physical, and political framework of Somnarak.
- When referencing world rules, always cite the corresponding codex (e.g., `PROJECT_SOMNARAK.md` for cosmology, `SOMNARAK_BATTLE_SYSTEM.md` for combat mechanics, `The_REVERIE_DIRECTORATE.md` for Facility 01 floors).

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
