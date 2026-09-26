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
| **`audit_lore_archive.py`** | Master audit across UTF-8, codices, 292 SEs, 198 MAW sets, auxiliary collections, and box symmetry. Blocks merge if any sub-check fails. | `python3 tools/audit_lore_archive.py [--json] [--verbose]` |
| **`check_box_symmetry.py`** | Audits ASCII text boxes across all markdown files for row-length and display-width symmetry. | `python3 tools/check_box_symmetry.py [--fix]` |
| **`timeline_lint.py`** | Scans all files pan-repo for chronological contradictions against the Year 4,238 / Cycle 1,778 baseline. | `python3 tools/timeline_lint.py` |
| **`seam_lint.py`** | Detects revision splices, punctuation collisions (`.,`), and un-whitelisted PM terminology. | `python3 tools/seam_lint.py` |
| **`generate_canonical_metrics_registry.py`** | Inspects filesystem on disk to regenerate authoritative `CANONICAL_METRICS.json` and `CANONICAL_METRICS.md`. | `python3 tools/generate_canonical_metrics_registry.py` |
| **`sync_readme_metrics.py`** | Synchronizes badges in `README.md` from `CANONICAL_METRICS.json`. | `python3 tools/sync_readme_metrics.py` |
| **`box_formatter.py`** | TablesGenerator reference engine (`https://www.tablesgenerator.com/text_tables`): creates perfectly aligned 74-column chatroom and wide-format ASCII grid tables and boxes with zero crooked rows and 5-row vertical growth cell wrapping. | `python3 tools/box_formatter.py` |
| **`tests/test_linters.py`** | Unit test suite verifying that linters catch known defects and accept valid fixtures. | `python3 -m unittest tools/tests/test_linters.py` |

---

## 3. Subdirectories

### `auditors/`
Specialized inspection scripts for specific subsets of the archive (e.g., verifying the Two-Work-Type rule across Object/Place/Time SEs, threat tier distributions, or ordeal rosters).

### `builders/`
Historical generation scripts used during major lore expansion milestones (Story Cantos, Memory Archive receptions, Katabagil descent passages, Katharcheok pacification operations). Retained for reproducibility.

### `repairs_and_patches/`
Historical one-off repair scripts from past audit rounds (e.g., splice elimination passes, box width harmonizations, and archived utility drafts like `audit_two_work_rule_fixed.py`).

### `formatters/`
Utilities for formatting ASCII tables, MAD timing sequences, and reStructuredText/markdown display boxes.

### `tests/`
Automated test runners and fixture files used in the CI/CD pipeline.
