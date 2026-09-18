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
| **`main`** | Web Wiki Frontend | `docs/`, `tools/`, `BUILD_RECORDS/`, static HTML/CSS/JS, vector art | Serves the public encyclopedia via GitHub Pages (1,040+ pages) |
| **`NON-WIKI`** (This Branch) | Canon Lore & Reference Archive | `REFERENCE_SOMNARAK_WIKI/`, master codices, entity dossiers, registries | The pure, authoritative markdown source library (~3.5M words) |

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
│
└── REFERENCE_SOMNARAK_WIKI/                # Master Canon & Reference Archive (1,863 files)
    ├── ALL_34_REFERENCE_FILES_AUDIT.md     # Audit of the 34 foundational codices in 07_Reference
    ├── ALL_FILES_AUDIT_MANIFEST.md         # Comprehensive manifest of all 1,863 reference files
    ├── CATEGORY_AND_PAGE_PLAN.md           # Information architecture & classification plan
    ├── CONTENT_AND_VISUAL_STANDARDS.md     # Narrative, terminological, and visual standards
    ├── LIVE_DEPLOYMENT_AND_BRANCH_POLICY.md# Branch policy and deployment acceptance standards
    ├── MASTER_HANDOFF_PROTOCOL.md          # Multi-session continuity protocol
    ├── MAW_PERSONALIZE_PROGRESS.md         # Weapon personalization ledger
    ├── MAW_WEAPON_ARCHETYPES.md            # Weapon archetype taxonomy and research
    ├── OPERATING_RULES.md                  # Canon integrity & directory rules
    ├── PROJECT_MOON_WIKI_NESTED_PLACEMENT_RESEARCH.md # Structural comparative research
    ├── PUBLIC_PAGE_COMPLIANCE_AUDIT_2026-08-31.md     # Public page compliance audit
    ├── README.md                           # Internal directory overview
    │
    └── LORE or REFERANCE/                  # Master Narrative Corpus (Note exact folder spelling)
        ├── 01_Sorrow_Entities/             # 529 files: SE-001 through SE-997 dossiers & tales
        ├── 02_Hope_Transformation/         # 14 files: HT-001 to HT-012, Trinity, and Hand of Hope
        ├── 03_Unknown_Entities/            # 8 files: UNK-248 to UNK-903 & Regressor Log
        ├── 04_Ordeals/                     # 60 files: Black, Blue, Grey, Pale, Purple (1st–Tide Watches)
        ├── 07_Reference/                   # 34 files: Macro-Canon Master Codices
        ├── CHARACTER_WIKI/                 # 9 files: The Nine Echo-Cores of Facility 01
        └── M.A.W. Codex_Set Registry/      # 1,196 files: 42 registry folders with A/B/C/D item sets
```

---

## 3. Standing Owner Rules (Binding on All Sessions)

1. **A0 — Push Always:** Every single file creation, edit, rename, or deletion must be committed **and pushed** to the assigned session branch in the same turn. Never end a turn with uncommitted changes or unpushed local commits.
2. **A5 — File Safety:** Never delete or overwrite owner files or canonical reference documents without an explicit, file-named instruction from the owner.
3. **Canon Terminology is Immutable:** Retain authentic Somnarak-native terminology across all documentation:
   - Sorrow Entities (SE), SECC designations, and threat tiers (`ZAYIN`, `TETH`, `HE`, `WAW`, `ALEPH`).
   - M.A.W. (Materialized Armament of Woe), Weapons (W), Suits (S), Gifts (G).
   - Han energy, Liquid Han, Absolvohan, Resonant Clash.
   - Facility 01 ("The Hand of Change"), Reverie Directorate, High Council.
   - Four damage elements: Grudge (원한), Lament (비탄), Void (공허), Weight (비중).
4. **Source-Led Integrity:** Content in markdown files derives strictly from the canonical texts in `REFERENCE_SOMNARAK_WIKI/` or established Somnarak lore. Never inject generic placeholder filler.
5. **Exact Path Spelling:** The primary folder in `REFERENCE_SOMNARAK_WIKI` is spelled `LORE or REFERANCE` (with the owner's exact spelling). Do not rename or alter it.

---

## 4. Working with the Canon Repositories

### A. The 34 Foundational Codices (`07_Reference/`)
- These 34 master files establish the cosmological, physical, and political framework of Somnarak.
- When referencing world rules, always cite the corresponding codex (e.g., `PROJECT_SOMNARAK.md` for cosmology, `SOMNARAK_BATTLE_SYSTEM.md` for combat mechanics, `The_REVERIE_DIRECTORATE.md` for Facility 01 floors).

### B. Sorrow Entity Files (`01_Sorrow_Entities/`)
- Filename convention: `SE-<SECC Code>_<English Name>_<Korean Name>.md` (e.g. `SE-C-IIIβ-014_The_Debt_Eater_빚을_먹는_자.md`).
- Entities carry containment procedures, work affinities (Ferrehan, Flerehan, Pugnahan, Viderehan), breach behaviors, and narrative tales.

### C. M.A.W. Codex Set Registry (`M.A.W. Codex_Set Registry/`)
- Each set folder is organized under a registry range (e.g. `Registry_001_to_007/001_The_Orphaned_Bell/`).
- Every complete set contains four files:
  - `SE-<ID>-A__SIDE_CODEX_<Name>.md`: The donor entity's lore and extraction parameters.
  - `SE-<ID>-B__MAW-W_<Weapon>.md`: Weapon specs (damage element, range/speed band, special moves).
  - `SE-<ID>-C__MAW-S_<Suit>.md`: Suit defenses, elemental resistances, and passive traits.
  - `SE-<ID>-D__MAW-G_<Gift>.md`: Gift slot, resonance triggers, and appearance.

### D. Five-Color Ordeals (`04_Ordeals/`)
- Ordeals are organized by color: `BLACK` (Weight), `BLUE` (Lament), `GREY` (Grudge), `PALE` (Void), and `PURPLE` (Mixed).
- Each color contains entities for four watches: `First_Watch`, `Second_Watch`, `Third_Watch`, and `Tide_Watch`.

### E. Facility 01 Echo-Cores (`CHARACTER_WIKI/`)
- Contains detailed dossiers on the 9 Echo-Cores: Director Ayshuk, Secretary Seiyon, Majin (Floor 1), Dekan (Floor 2), Mellda (Floor 3), Ishall (Floor 4), Marjuk (Floor 5), Zyrak (Floor 6), and Xyan (Floor 8).

---

## 5. Verification & Inspection Recipes

Use standard Python 3 and bash tools to inspect, verify, and audit the markdown files:

```bash
# 1. Run the master archive audit (UTF-8, 34 codices, M.A.W. sets, entity counts)
python3 tools/audit_lore_archive.py

# 2. Verbose audit listing incomplete or exception sets
python3 tools/audit_lore_archive.py --verbose

# 3. Export structured audit data as JSON
python3 tools/audit_lore_archive.py --json

# 4. Search for references to a specific entity or concept across all files
grep -rn "SE-001" "REFERENCE_SOMNARAK_WIKI/LORE or REFERANCE/"
```

---

## 6. Git Workflow & Turn Discipline

1. **Check branch state at turn start:**
   ```bash
   git branch --show-current
   git status --short
   ```
2. **Make required modifications.** Validate file structure and encoding.
3. **Commit with clean messages:** Use plain single quotes; do not use backticks.
4. **Push immediately:**
   ```bash
   git push origin <assigned-branch>
   ```
5. **Verify push:**
   ```bash
   git rev-parse HEAD
   git rev-parse origin/<assigned-branch>
   ```
   Both hashes must match before ending the turn.
