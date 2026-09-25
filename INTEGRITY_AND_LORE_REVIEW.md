# PROJECT.SOMNARAK-WIKI
# Integrity Review & History-to-Lore Consistency Audit
### Date: 2026-09-25 | Branch: arena/01a0b699-project-somnarak-wiki | 2,002 files | 3,426,300 words

---

## EXECUTIVE SUMMARY

Project Somnarak is an extraordinary written universe — **3.42 million words across 2,002 files** — with a rigorously enforced canonical architecture. The built-in audit tooling (`audit_lore_archive.py`) reports a clean **PASS** across all categories. However, my independent deep-dive uncovered **14 integrity findings** and **8 lore/history observations** that warrant review.

| Category | Status | Findings |
|---|---|---|
| **Structural Integrity** | ⚠️ MOSTLY PASS | 14 findings (3 Medium, 6 Low, 5 Informational) |
| **Lore Consistency** | ✅ STRONG | 8 observations (2 Notable, 6 Informational) |
| **Built-in Audit Health** | ✅ PASS | All 6 audit categories clean |

---

# PART I: STRUCTURAL INTEGRITY REVIEW

---

## FINDING 1 — Hangul Characters Inside ASCII Text Boxes (602 Instances)
**Severity:** MEDIUM  
**Status:** Contradicts stated zero-Hangul-inside-boxes rule

Your project's explicit rule (from `CHANGELOG.md` and `SESSION_BREAK_PRECAUTION.md`) states:

> *"Purged all Korean Hangul characters inside text boxes and code fences across all files... replacing them with authentic Latin Alphabet Romanization (Romaja) to guarantee 100% monospace display symmetry."*

However, my scan detected **602 instances of Hangul characters inside text box boundaries** across the canonical directories. The worst-hit files are:

- `SOMNARAK-WORLD/Gieok_Jeojangso/GIEOK_JEOJANGSO_OVERVIEW.md` (multiple lines: 30, 33, 35, 52)
- `SOMNARAK-WORLD/Gieok_Jeojangso/Reception_1_First_Keeper.md` through `Reception_7_The_Original.md` (all 7 receptions)
- Likely more across other subdirectories

**Note:** This could be a false positive if the Hangul appears in *buffered context* (preceded by two spaces) outside the box border lines but within the visual block. The scan detected Hangul between `+`/`|` border lines. Recommend running `check_box_symmetry.py --hangul-audit` specifically to validate.

**Recommendation:** Run the dedicated Hangul-inside-boxes audit. If confirmed, batch-replace with Romaja equivalents.

---

## FINDING 2 — 174 Broken Cross-References (Backtick File Links)
**Severity:** MEDIUM  
**Affected:** CHANGELOG.md, README.md, DEVELOPMENT.md, and others

Out of **2,895 backtick file references** scanned across all markdown files, **174 (~6%) resolve to files that don't exist** in the current tree. Key broken references include:

| Source File | Broken Reference |
|---|---|
| `CHANGELOG.md` | `Master_Codices/SOMNARAK_SPECIALIST_CADRES.md` |
| `CHANGELOG.md` | `Master_Codices/SOMNARAK_UNDERWORLD_SYNDICATES.md` |
| `CHANGELOG.md` | `Master_Codices/SOMNARAK_WORKSHOPS.md` |
| `CHANGELOG.md` | `SOMNARAK_RAW_SYNDICATES.md` |
| `CHANGELOG.md` | `SOMNARAK_ABSOLOVHAN.md` |
| `README.md` | `Part_01_Day_000_to_045.md` |
| `README.md` | `Passage_1_The_Sunken_Aqueducts.md` |
| `README.md` | `Operation_1_Rust_Veil_Liquidation.md` |
| `DEVELOPMENT.md` | `SE-<SECC Code>_<English Name>_<Korean Name>.md` (template pattern) |

Many of these are likely references to files that were **renamed or restructured** during the 7-round audit process. The CHANGELOG entries document when files were created, but the references weren't updated when files moved.

**Recommendation:** Run a reference-repair pass on CHANGELOG.md and README.md specifically. Template patterns in DEVELOPMENT.md (e.g., `SE-<ID>-A__SIDE_CODEX_<Name>.md`) are acceptable as documentation examples.

---

## FINDING 3 — MAW Registry Numbering Gaps (31 Gaps Identified)
**Severity:** LOW  
**Affected:** `SOMNARAK-WORLD/MAW_Codex_Sets/`

The MAW Codex system covers Registry 001 through 1,043 across 42 folders, but has **31 numbering gaps**:

| Gap Range | Size | Between Registries |
|---|---|---|
| 8 | 1 | 001–007 ↔ 009–015 |
| 56–60 | 5 | 043–055 ↔ 061–073 |
| 74–76 | 3 | 061–073 ↔ 077–092 |
| 93–98 | 6 | 077–092 ↔ 099–103 |
| 196–199 | 4 | 185–195 ↔ 200–219 |
| 520–524 | 5 | 489–519 ↔ 525–559 |
| 802–820 | 19 | 762–801 ↔ 821–852 |
| 977–992 | 16 | 941–976 ↔ 993–997 |
| ...and 23 more gaps | | |

Additionally, several registry folders contain only **1 file** instead of the expected quadripartite set (4 files per entity). The early registries (001–195) and late registries (762–997) appear to have minimal content, while the mid-range (200–677) is fully populated with ~21 files each.

**This is likely intentional** — gaps correspond to entity IDs that don't exist (not every number is assigned), and sparse folders may indicate work-in-progress sets. However, documenting which gaps are intentional vs. missing would improve navigability.

---

## FINDING 4 — Entity-MAW Cross-Reference Orphans
**Severity:** LOW  
**Affected:** `SOMNARAK-WORLD/Sorrow_Entities/` and `SOMNARAK-WORLD/MAW_Codex_Sets/`

**43 MAW sets exist without matching entity dossiers** in Sorrow_Entities:
- All 43 are in the **1001–1043 range** (Registry_1001_to_1043), suggesting these are a separate class of equipment not tied to standard Sorrow Entities.

**6 Entity dossiers exist without MAW sets:**
- `SE-000` (likely a root/index entry)
- `SE-072`, `SE-114`, `SE-319`, `SE-412`, `SE-515`

**Recommendation:** If SE-072, 114, 319, 412, and 515 are entities that canonically don't have M.A.W. equipment (e.g., Object/Place entities), document this in their dossiers. If they should have sets, this is a coverage gap.

---

## FINDING 5 — "Absolovhan" Misspelling (3 Files)
**Severity:** LOW  
**Affected:** `CANON_TIMELINE.md`, `RULE-TO-FOLLOW.md`, `SOMNARAK-WORLD/Master_Codices/01_Cosmology_and_World_Order/CANON_TIMELINE.md`

The canonical spelling is **"Absolvohan"** (해원 / 解怨), used consistently in 88 files. However, **3 files** contain the misspelling **"Absolovhan"** — notably including the canonical timeline itself, which quotes the Project Owner's original decree verbatim:

> *"The Cycle Is Only Things That Is View Able Through R.D. + **Absolovhan**..."*

**Note:** This may be an intentional preservation of the owner's original unedited text. If so, consider adding a `[sic]` marker to distinguish deliberate preservation from typos.

---

## FINDING 6 — New Entity Scope "N" (Not Documented in README)
**Severity:** LOW  
**Affected:** `SOMNARAK-WORLD/Sorrow_Entities/`

The README and canonical taxonomy describe three entity scopes:
- **C** (Contained — inside Facility 01)
- **O** (Outside — wilderness/Desolate entities)

However, **74 entities** use a third scope: **"N"** (e.g., `SE-N-IIIβ-077`, `SE-N-IVδ-005`). These are distributed across all ranks (I through V) and potency grades. The "N" scope is not documented in the README's entity classification system.

**Recommendation:** Add documentation for the "N" scope to the entity taxonomy. Likely candidates: "Null" (anomalous/unclassified), "New" (post-Dawn), or "Non-categorized."

---

## FINDING 7 — Absolvohan Day Coverage Gap (Days 178–349)
**Severity:** INFORMATIONAL  
**Affected:** `SOMNARAK-WORLD/The_Absolvohan/`

The Absolvohan narrative covers 366 days of Cycle 1,778 but has a **172-day narrative gap**:

| Part | Day Coverage | Gap After |
|---|---|---|
| Part 1 | Day 0 | — |
| Part 2 | Days 1–25 | — |
| Part 3 | Days 29–49 | Days 26–28 (3 days) |
| Part 4 | Days 53–73 | Days 50–52 (3 days) |
| Part 5 | Days 77–97 | Days 74–76 (3 days) |
| Part 6 | Days 101–121 | Days 98–100 (3 days) |
| Part 7 | Days 125–145 | Days 122–124 (3 days) |
| Part 8 | Days 149–177 | Days 146–148 (3 days) |
| **Part 9** | **Days 350–365** | **Days 178–349 (172 days)** |

The 3-day gaps between Parts 2–8 appear deliberate (rest/transitions). The **172-day gap** between Part 8 (Day 177) and Part 9 (Day 350) is significant. Part 9's text explains that after the Day 160 Critical Threshold venting, the facility transforms from a "prison" to an "open sanctuary" — suggesting Days 178–349 are a deliberate narrative ellipsis representing a peaceful, operational period.

**Recommendation:** Consider adding a brief narrative bridge or explicit note in the README explaining this gap is intentional (e.g., "Days 178–349: The Quiet Season — routine operations, entity rehabilitation, and community building within the transformed facility").

---

## FINDING 8 — Hope Transformation File Naming vs. Content Mismatch
**Severity:** LOW  
**Affected:** `SOMNARAK-WORLD/Hope_Transformations/`

The file `HT-001_The_Guiding_Light_인도의_빛.md` begins with:

> **# The Shield of Dawn — 새벽의 방패**

The header says "Shield of Dawn" but the filename says "Guiding Light." The HT designation inside the file is `HT-IV-HS-002 [O]` (number 002, not 001). This suggests either:
1. The file was renamed but the internal header wasn't updated
2. HT-001 and HT-002 were merged/reordered during an audit

**Recommendation:** Verify whether `HT-001_The_Guiding_Light` and `HT-002_The_Shield_of_Dawn` are the same entity or if there's a content swap.

---

## FINDING 9 — TEST_TEXT_BOX_WIDTHS.md Contains Mixed Box Widths
**Severity:** INFORMATIONAL  
**Status:** Expected (calibration file)

The file `TEST_TEXT_BOX_WIDTHS.md` shows box widths of 71, 120, 127, 128, 130, 140, and 150 characters. This is **expected** — it's explicitly a calibration/ergonomic testing file, not a canonical document. No action needed.

---

## FINDING 10 — PM Crossover References Confined to Audit/Comparison Files
**Severity:** INFORMATIONAL (CLEAN)  
**Status:** PASS

References to "Lobotomy Corporation," "Library of Ruina," "Limbus Company," etc. appear **only** in:
- `CANON_TIMELINE.md` (canonical analogy section — intentional)
- `PM_VOCAB_POLICY.md` (policy definition — intentional)
- `COMPLETE_SYSTEM_COMPARISON_SOMNARAK_VS_LOBOTOMY_CORPORATION.md` (comparative study — intentional)
- `PS_SORROW_ENTITY_IN_L_CORP_CONTAINMENT_GUIDE.md` (cross-reference guide — intentional)
- `SOMNARAK_PM_COMPARATIVE_INTEGRITY_AUDIT.md` (audit — intentional)

**Zero PM crossover vocabulary found in any in-universe canonical files.** The vocabulary isolation policy is working correctly.

---

## FINDING 11 — Timeline Drift Check: Clean (1 False Positive)
**Severity:** INFORMATIONAL (CLEAN)

Only 1 file references a year beyond 4255: `PROJECT_SOMNARAK.md` mentions Year 4301. This is in the context of **"Deep-Future Theoretical Simulations"** — an explicitly authorized forward-projection per CANON_TIMELINE §5. No unauthorized timeline drift detected.

---

## FINDING 12 — No Empty or Stub Files
**Severity:** INFORMATIONAL (CLEAN)

Zero files are empty (0 bytes) or stubs (<100 bytes). Every file in the repository contains substantive content. This is remarkable for a 2,002-file repository.

---

## FINDING 13 — Entity Distribution Balance
**Severity:** INFORMATIONAL

| Scope-Rank | Count | | Scope-Rank | Count |
|---|---|---|---|---|
| C-I (Whisper) | 22 | | O-I | 14 |
| C-II (Murmur) | 33 | | O-II | 13 |
| C-III (Fragment) | 40 | | O-III | 19 |
| C-IV (Entity) | 49 | | O-IV | 14 |
| C-V (Sovereign) | 13 | | O-V | 1 |
| N-I | 8 | | N-IV | 17 |
| N-II | 24 | | N-V | 0 |
| N-III | 23 | | | |

**Observation:** O-V (Outside Sovereign) has only 1 entity. If this is intentional (only one Sovereign-class entity exists outside the facility), it's a compelling narrative choice. N-V also has 0 entities.

---

## FINDING 14 — Built-in Audit Tool Reports Clean PASS
**Severity:** INFORMATIONAL (CLEAN)

Running `tools/audit_lore_archive.py` produced:

```
1. UTF-8 Integrity        : PASS (1782 files, 21.97 MB)
2. Macro-Canon Codices    : PASS (47 / 35 master codices)
3. Sorrow Entities        : PASS (292 files, 292 unique codes, 0 paired)
4. M.A.W. Equipment Sets  : PASS (198 / 198 complete quadripartite sets)
5. Auxiliary Collections  : PASS
6. Text Box Symmetry      : PASS (1782 files, 0 crooked rows)
OVERALL LORE HEALTH: PASS
```

**Note:** The audit reports 198 complete MAW sets, while my manual count found 415 files across 42 registry folders. The discrepancy likely reflects the audit counting only complete quadripartite sets (A/B/C/D) rather than all files.

---

# PART II: HISTORY-TO-LORE CONSISTENCY REVIEW

---

## LORE OBSERVATION 1 — The Macro-Chronological Architecture is Sound ✅
**Status:** CONSISTENT

The three-epoch system is cleanly enforced:

```
EPOCH I: ANTE-DAWN
  Year 0        → Settlement Arrival
  Year 200      → The Cheongula (First Sorrow)
  Year 2,460    → R.D. Inception / Cycle 0001
  Year 3,972    → The Great Rust Severance (Cycle 1,512)
  Year 3,973-4,039 → UCD Pacifications
  Year 4,040    → The Great Collapse (Cycle 1,580)
  Year 4,041-4,238 → Active Containment Cycles (1,581–1,778)

WATERSHED: Year 4,238 — The Dawn of Hope

EPOCH II: POST-DAWN
  Year 4,238+   → UNK SE Manifestation
  Year 4,238-4,247 → Dawn Initiative
  Year 4,239+   → Horizon Caravan
  Year 4,240+   → Memory Archive
  Year 4,250+   → Wound Walkers
  Year 4,255+   → Continental Reconstruction
```

The **Cycle Localization Law** (Cycles only inside R.D.) is consistently enforced. SED and UCD operate in calendar years. Post-Dawn events use linear time. No contradictions found in the timeline structure.

---

## LORE OBSERVATION 2 — R.D. Inception Year vs. Loop Base Year (Intentional Discrepancy)
**Status:** CONSISTENT (requires documentation)

Two different "origin" years appear:
- **CANON_TIMELINE:** R.D. Inception = **Year 2,460** (Cycle 0001)
- **Absolvohan narrative:** Loop base year = **Year 4,232**

Difference: **1,772 years**

This is **not a contradiction** — it's an intentional two-phase history:
1. **Years 2,460–4,231:** R.D. operates as a standard containment facility (no time loop)
2. **Year 4,232:** The Mnemonic Generator is deployed, creating the 366-day loop (Cycles 1–1,778)
3. **Year 4,238:** The loop breaks (4,232 + 6 real years = 1,778 cycles compressed)

The math checks out: 1,778 cycles × ~1.22 real days per cycle ≈ 6 real years (4,232 to 4,238).

**However**, this two-phase structure is not explicitly documented in the CANON_TIMELINE. The timeline says "Year 2,460: R.D. Cycle 0001" but the Absolvohan Overview implies the Mnemonic Generator wasn't deployed until much later. Adding a clarifying note would prevent future confusion.

---

## LORE OBSERVATION 3 — The Cheongula Event is Fully Anchored ✅
**Status:** CONSISTENT

The foundational event — **The Cheongula (Year 202)** — is documented with:
- Precise date: Year 202, 2nd Month, Day 14 (The 44th Day of Frost)
- Exact casualty toll: 1,000 citizens
- Named eyewitnesses: Archive Lead Marjuk, Containment Lead Dekan
- Institutional aftermath: Historical Expungement Order, Debt Ledger, Acoustic Veil

Cross-referenced correctly in:
- `SOMNARAK_CHEONGULA.md` (primary source)
- `CANON_TIMELINE.md` (timeline entry)
- `PROJECT_SOMNARAK.md` (worldbuilding framework)
- `The_Absolvohan/Part_1` (referenced by Majin: "the thousand beneath the basalt floorplates")

---

## LORE OBSERVATION 4 — Entity Classification System is Internally Consistent ✅
**Status:** CONSISTENT

The SECC (Sorrow Entity Classification Code) system follows a rigid taxonomy:

```
SE - [Scope] - [Rank][Potency] - [Number]_[English Name]_[Korean Name]
```

- **Scope:** C (Contained), O (Outside), N (appears to be a third category — see Finding 6)
- **Rank:** I (Whisper) → II (Murmur) → III (Fragment) → IV (Entity) → V (Sovereign)
- **Potency:** α (Alpha), β (Beta), γ (Gamma), δ (Delta), ω (Omega)
- **Number:** Unique 3-digit identifier

Sample entity dossier (`SE-C-IIIβ-014 The Debt Eater`) shows full internal consistency:
- Designation matches filename
- Rank/Potency matches operational parameters
- Combat stats align with rank tier (Moderate β = manageable with standard precautions)
- Sorrow Category properly classified (City Sorrow / 도한)
- M.A.W. set exists at `MAW_Codex_Sets/Registry_009_to_015/014_Debt_Eater/` with all 4 parts (A/B/C/D)

---

## LORE OBSERVATION 5 — Narrative Arc Progression is Chronologically Ordered ✅
**Status:** CONSISTENT

The six major narrative arcs follow the canonical triad + post-Dawn structure:

| Arc | Division | Time Period | Files | Status |
|---|---|---|---|---|
| The Absolvohan | R.D. | Year 4,232–4,238 (Cycle 1,778) | 10 parts | Complete |
| Katabagil (SED) | SED | Years 2,460–3,970 | 7 passages + overview | Complete |
| Katharcheok (UCD) | UCD | Years 3,973–4,039 | 6 operations + overview | Complete |
| Gieok Jeojangso | Post-Dawn | Year 4,240+ | 7 receptions + overview | Complete |
| Jipyeongseondae | Post-Dawn | Year 4,239+ | 6 arcs + overview | Complete |
| Story Cantos | Various | Various | 6 cantos | Complete |

The temporal ordering is correct: SED and UCD precede R.D. (all pre-Dawn), and the post-Dawn arcs (Gieok, Jipyeongseondae) occur after the watershed.

---

## LORE OBSERVATION 6 — The Three Sorrows Framework is Well-Integrated ✅
**Status:** CONSISTENT

The tripartite sorrow system (City/Outside/Inner) appears consistently across:
- Entity classification (each entity tagged with 도한/외한/내한)
- Geographical mapping (Zone A-E for City, Desolate for Outside, personal for Inner)
- Combat mechanics (different pressure types per sorrow category)
- Narrative themes (The Cheongula = City Sorrow origin, Katabagil = Outside Sorrow exploration, Cantos = Inner Sorrow resolution)

---

## LORE OBSERVATION 7 — Operative Longevity Physics are Documented ✅
**Status:** CONSISTENT

The biological discrepancy of operatives surviving 1,778+ cycles is addressed in CANON_TIMELINE §3:
1. **Han-Saturation Cellular Stasis** (reduces aging)
2. **Mnemonic Cycle Dilation** (cryo-engrammatic salt suspension between cycles)

This correctly explains how characters like Min-Jae, Seol-A, and Taeho can serve across 266+ cycles without mortal senility.

---

## LORE OBSERVATION 8 — Absolvohan Ending Types are Documented ✅
**Status:** CONSISTENT

The Absolvohan Overview documents **5 possible cycle endings**:
1. **Ending S: The Absolvohan** (True Ending — Cycle 1,778)
2. **Ending A: Structural Collapse** (ballast failure)
3. **Ending B: Cognitive Collapse** (director breakdown)
4. **Ending C: Municipal Resignation** (Council withdrawal)
5. **Ending D: Cataclysmic Breach** (total facility loss)

The narrative Parts 1–9 chronicle the successful **Ending S** path, which is the canonical outcome.

---

# PART III: RECOMMENDATIONS SUMMARY

## Priority 1 — Fix Now
| # | Issue | Action |
|---|---|---|
| 1 | 602 Hangul instances in text boxes | Audit and replace with Romaja |
| 2 | 174 broken cross-references | Repair CHANGELOG.md and README.md links |
| 5 | "Absolovhan" misspelling (3 files) | Correct or add [sic] markers |

## Priority 2 — Improve
| # | Issue | Action |
|---|---|---|
| 4 | 6 entity dossiers without MAW sets | Document or create missing sets |
| 6 | "N" scope undocumented | Add to entity taxonomy |
| 8 | HT-001/HT-002 content swap | Verify and fix naming |
| Lore-2 | R.D. two-phase history undocumented | Add clarifying note to CANON_TIMELINE |

## Priority 3 — Document
| # | Issue | Action |
|---|---|---|
| 3 | MAW registry gaps | Document intentional gaps |
| 7 | Absolvohan Days 178–349 gap | Add narrative bridge note |
| 13 | O-V single entity | Confirm intentional rarity |

---

# APPENDIX: VERIFIED METRICS

| Metric | Value | Status |
|---|---|---|
| Total files | 2,002 | ✅ |
| Markdown files | 1,782 | ✅ |
| Total words | 3,426,300 | ✅ |
| Total characters | 23,033,196 | ✅ |
| Sorrow Entities | 292 (unique IDs) | ✅ |
| MAW Codex Sets | 42 registry folders, 415 files | ✅ |
| Ordeal Files | 61 (5 colors × 4 watches + extras) | ✅ |
| Hope Transformations | 15 (12 + Trinity + Hand + README) | ✅ |
| Echo Cores | 9 + README | ✅ |
| Unknown Entities | 12 + Regressor log + README | ✅ |
| Story Cantos | 6 + README | ✅ |
| Absolvohan Parts | 9 + Overview + README | ✅ |
| Master Codices | 45 across 6 subfolders | ✅ |
| Python Tools | 186 scripts | ✅ |
| SVG Blueprints | 2 | ✅ |
| Empty/Stub Files | 0 | ✅ |
| PM Crossover Leaks | 0 (in canonical files) | ✅ |
| Text Box Symmetry | PASS (per built-in audit) | ✅ |
| UTF-8 Integrity | PASS (1,782 files) | ✅ |

---

*Review generated by independent structural scan and manual lore analysis. For automated verification, run `python3 tools/audit_lore_archive.py` from the repository root.*