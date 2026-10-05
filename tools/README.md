# Project Somnarak // Tooling Suite & Verification Architecture

Welcome to the Project Somnarak engineering toolchain. This directory houses the automated linters, integrity checkers, text-box formatters, and historical generation scripts that protect the canon integrity of the Somnarak universe.

---

## 1. Directory Structure

```text
tools/
├── README.md                                 # This document
├── audit_lore_archive.py                     # Master archive auditor (blocking merge gate)
├── check_box_symmetry.py                     # Text box width and border symmetry checker
├── timeline_lint.py                          # Pan-repo canon timeline & chronological validator
├── seam_lint.py                              # Semantic seam, editing-splice, and PM term linter
├── box_formatter.py                          # TablesGenerator-based 74-col grid table and ASCII box generator
├── text_box_double_checker.py                # Secondary text box symmetry validator
├── generate_canonical_metrics_registry.py    # SSOT metrics engine (updates CANONICAL_METRICS)
├── sync_readme_metrics.py                    # Propagates SSOT badges to README.md
├── banned_strings.txt                        # Blocklist of revision splices and foreign PM terms
├── auditors/                                 # Specialized inspection & secondary audit scripts
├── builders/                                 # Historical generation & expansion scripts (118 builders)
├── formatters/                               # Text formatting and display-width utilities
├── repairs_and_patches/                      # One-off repair, patch, and migration scripts
└── tests/                                    # Unit test suites and validation fixtures
```

---

## 2. Core Active Toolchain

| Tool | Purpose | Primary Flags / Command |
| :--- | :--- | :--- |
| **`audit_lore_archive.py`** | Master audit across UTF-8, codices, 291 SEs, 198 MAW sets, auxiliary collections, and box symmetry. Blocks merge if any sub-check fails. | `python3 tools/audit_lore_archive.py [--json] [--verbose]` |
| **`check_box_symmetry.py`** | Audits ASCII text boxes across all markdown files for row-length and display-width symmetry. | `python3 tools/check_box_symmetry.py [--fix]` |
| **`timeline_lint.py`** | Scans all files pan-repo for chronological contradictions against the Year 4,238 / Cycle 1,778 baseline. | `python3 tools/timeline_lint.py` |
| **`seam_lint.py`** | Detects revision splices, punctuation collisions (`.,`), and un-whitelisted PM terminology. | `python3 tools/seam_lint.py` |
| **`generate_canonical_metrics_registry.py`** | Inspects filesystem on disk to regenerate authoritative `CANONICAL_METRICS.json` and `CANONICAL_METRICS.md`. | `python3 tools/generate_canonical_metrics_registry.py` |
| **`sync_readme_metrics.py`** | Synchronizes badges in `README.md` from `CANONICAL_METRICS.json`. | `python3 tools/sync_readme_metrics.py` |
| **`box_formatter.py`** | TablesGenerator reference engine (`https://www.tablesgenerator.com/text_tables`): creates perfectly aligned 74-column chatroom and wide-format ASCII grid tables and boxes with zero crooked rows and 5-row vertical growth cell wrapping. | `python3 tools/box_formatter.py` |
| **`tpl.py`** | Workstream 6 census: template residue — lines shared by ten or more dossiers that are not sanctioned furniture (`R-23`). No args = summary, `--top N` = worst lines, `<path>…` = per-file residue with line numbers. | `python3 tools/tpl.py --top 20` |
| **`sect.py`** | The Tale standard (`R-24`): generic-prose census by 8-gram sharing. `--sections` = per-section league table, `--files N` = best/worst dossiers, `<path>` = per-line attribution. | `python3 tools/sect.py --sections` |
| **`dirtylines.py`** | `R-27` attribution: for every section of a dossier over 0.05, only the lines inside it that carry shared 8-grams. Often a single slot-filled sentence is the whole defect. | `python3 tools/dirtylines.py <path>` |
| **`editmeta.py`** | `R-01` candidates: sentences about earlier wording ("has been corrected against the Behavior table", "the earlier entry naming …", "previously carried here", "The earlier entry grading it Moderate … is corrected here"). Finds, never edits; in-world administrative history is not matched on purpose. | `python3 tools/editmeta.py [dir …]` |
| **`ghlink.py`** | `R-12` links in the owner's format: `[[name](github url "file.md")]`, percent-encoded, on the checked-out branch. `--short` for the English name only, `--changed` for every dossier that differs from `NON-WIKI`, `--branch` to override. Reads the branch from git; never hard-codes one. | `python3 tools/ghlink.py [--short] [--branch B] [--changed [REF]] <path> …` |
| **`ladder.py`** | What changes with level, by Coherence rank: the stat line, breach capability, the event section, the rank record each rank adds (Watch, Warden, Apex, Sovereign Chronicle), dispositions, conformance to the conversion guide, the shared escalation figure, the relic banner vocabulary, and the dossiers whose SECC table and Registrum header disagree on comprehension level or potency. Regenerates the figures in Comparative Study 02. Reports, never edits; not part of the gate. | `python3 tools/ladder.py [--rows \| --layers]` |
| **`wikistd.py`** | The `R-29` test: abnormality-wiki parity (nine sections), a specific management condition, an own numeric series, a classified disposition and section-cleanliness, per dossier and in total. The disposition lookup is keyed on the filename code (Document ID). | `python3 tools/wikistd.py [--gaps N \| <path>]` |
| **`syncbranch.py`** | Brings HEAD and the working tree level with `origin/<branch>` without losing anything. If the tree is byte-identical to a commit already pushed it moves to the tip; otherwise it fast-forwards when no local edit overlaps; it refuses, with the reason, when local commits are unpushed or an edit would be overwritten. Written because two sessions can push to one branch, and `git reset --mixed` moves HEAD but not the files, so the next `git add -A` would have reverted the other session. `gate.sh` calls it first. | `python3 tools/syncbranch.py [--check]` |
| **`gate.sh`** | The standing push gate: linters (each must print its explicit PASS string), unit tests, row-pipe check (run with `core.quotepath=off`, so dossiers with Greek or Hangul names are checked rather than silently skipped), breach floors (`R-28`), metrics regenerated and staged, then commit, push to the **checked-out session branch** and verify HEAD against the remote ref. Refuses `main` and `NON-WIKI`. | `bash tools/gate.sh "<commit message>"` |
| **`tests/test_linters.py`** | Unit test suite verifying that linters catch known defects and accept valid fixtures. | `python3 -m unittest tools/tests/test_linters.py` |

---

## 3. Subdirectories

### `auditors/`
Specialized inspection scripts for specific subsets of the archive (e.g., verifying the Two-Work-Type rule across Object/Place/Time SEs, threat tier distributions, or ordeal rosters).

### `builders/`
Historical generation scripts used during major lore expansion milestones (Story Cantos, Memory Archive readings, Katabagil descent passages, Katharcheok pacification operations). Retained for reproducibility.

### `repairs_and_patches/`
Historical one-off repair scripts from past audit rounds (e.g., splice elimination passes, box width harmonizations, and archived utility drafts like `audit_two_work_rule_fixed.py`).

### `formatters/`
Utilities for formatting ASCII tables, MAD timing sequences, and reStructuredText/markdown display boxes.

### `tests/`
Automated test runners and fixture files used in the CI/CD pipeline.
