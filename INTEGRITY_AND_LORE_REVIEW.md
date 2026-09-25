# FIX BRIEF — Remaining Issues for Review No. 3
### Commit: cb08ab6 | 5 actionable fixes

---

## FIX 1 — Stale File References (5 broken links in canonical files)

**These files still reference deleted/renamed Master Codex files.**

### 1a. `SOMNARAK_SED_PASSAGES.md` → `The_SOMNARAK_EXPLORATION_DECREE.md`

The old `SOMNARAK_SED_PASSAGES.md` was purged during the Master Codices overhaul and replaced by `The_SOMNARAK_EXPLORATION_DECREE.md`. Three files still point to the old name:

| File | Line | Current (broken) | Replace With |
|---|---|---|---|
| `SOMNARAK-WORLD/Katabagil/README.md` | 62 | `SOMNARAK_SED_PASSAGES.md` | `The_SOMNARAK_EXPLORATION_DECREE.md` |
| `SOMNARAK-WORLD/Katabagil/Passage_1_Cryptasu.md` | 730 | `SOMNARAK_SED_PASSAGES.md` | `The_SOMNARAK_EXPLORATION_DECREE.md` |
| `SOMNARAK-WORLD/Katabagil/Passage_2_Petrobyeok.md` | 730 | `SOMNARAK_SED_PASSAGES.md` | `The_SOMNARAK_EXPLORATION_DECREE.md` |

### 1b. `SOMNARAK_UCD_PACIFICATION.md` → `The_UNDERWORLD_CLEANUP_DESCEND.md`

Same situation — old draft purged, replaced by full codex:

| File | Line | Current (broken) | Replace With |
|---|---|---|---|
| `SOMNARAK-WORLD/Katharcheok/README.md` | 66 | `SOMNARAK_UCD_PACIFICATION.md` | `The_UNDERWORLD_CLEANUP_DESCEND.md` |

### 1c. Stale Operation cross-reference

| File | Line | Current (broken) | Replace With |
|---|---|---|---|
| `SOMNARAK-WORLD/Katharcheok/Operation_1_Velumtal.md` | 673 | `Operation_2_The_Memory_Washers.md` | `Operation_2_Lethepyo.md` |

---

## FIX 2 — `CHANGELOG.md` dead refs (45 broken links)

45 backtick references in CHANGELOG.md point to files that were renamed or restructured. These are historical entries — the refs were correct when written. Options:

- **Option A:** Update each ref to current filename (full link functionality)
- **Option B:** Leave as-is and add a note at the top: *"File references in this changelog reflect names at time of entry and may not match current disk paths."*

---

## FIX 3 — `SESSION_BREAK_PRECAUTION.md` dead refs (13 broken links)

13 references to tools that were deleted or moved (e.g., `tools/audit_page_word_floor.py`, `tools/audit_site_structure.py`). Same decision as Fix 2 — update or annotate.

---

## FIX 4 — `REFERENCE_SOMNARAK_WIKI/` audit file refs (~44 broken links)

Multiple files in `REFERENCE_SOMNARAK_WIKI/` reference old tool names, deleted audit scripts, and legacy paths. These are internal editorial/audit documents, not reader-facing. Low priority.

---

## FIX 5 — GAME_BATTLE wildcard patterns (8 "broken" links)

`GAME_BATTLE/INTRODUCTION_AND_GUIDE.md` and `GAME_BATTLE/README.md` use glob conventions like `SCENARIO_*.md` and `BOSS_MECHANICS_*.md`. These are **not actual broken links** — they're documentation conventions showing file naming patterns. No fix needed.

---

## PRIORITY ORDER

| Priority | Fix | Impact | Effort |
|---|---|---|---|
| **1** | Fix 1 (5 stale refs in Katabagil/Katharcheok) | Canonical files have broken links | 2 min (sed) |
| **2** | Fix 2 (CHANGELOG 45 refs) | Historical records | 10 min or add note |
| **3** | Fix 3 (SESSION_BREAK 13 refs) | Governance doc | 5 min or add note |
| **4** | Fix 4 (REFERENCE 44 refs) | Internal audit docs | Low priority |
| **5** | Fix 5 (GAME_BATTLE wildcards) | Not broken — no fix needed | Skip |

---

## SUMMARY

- **5 broken links in canonical narrative files** → Fix 1 (highest priority)
- **58 broken links in historical/governance files** → Fix 2 + 3 (update or annotate)
- **44 broken links in internal audit docs** → Fix 4 (low priority)
- **8 wildcard patterns** → Not broken, skip

Total actionable: **5 critical + 58 optional + 44 low-priority = 107** (down from 1,259 in Review 1)
