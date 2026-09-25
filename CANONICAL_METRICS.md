# PROJECT SOMNARAK // CANONICAL METRICS REGISTRY
## Single Source of Truth (SSOT) — Programmatically Audited & Verified
**Audit Date:** 2026-09-24  
**Audit Tool:** `tools/generate_canonical_metrics_registry.py`  
**JSON Output:** `CANONICAL_METRICS.json`

---

### 1. Sorrow Entities & Specimen Metrics

| Metric Dimension | Programmatic Count | Status / Benchmark |
| :--- | :--- | :--- |
| **Total Sorrow Entities (`SOMNARAK-WORLD/Sorrow_Entities/`)** | **292** | 100% Individualized & Audited |
| **Relic-Entities (Tool Abnormalities)** | **88** | 30.14% (Quota >= 25.0% PASS) |
| **Two-Work-Type Rule Compliance (Non-Subject Entities)** | **283 / 283** | **100.0% Compliant** |
| **Core Stat Line Compliance (Speed, Gauges, Resistances)** | **292 / 292** | **100.0% Compliant** |
| **Unknown Entities (`SOMNARAK-WORLD/Unknown_Entities/`)** | **12** | Standardized |
| **Hope Transformations (`SOMNARAK-WORLD/Hope_Transformations/`)** | **14** | Standardized |
| **Ordeals (`SOMNARAK-WORLD/Ordeals/`)** | **60** | Dawn to Midnight |

> **Unit Definition Note (Unknown Entities):** The 12 Unknown Entities metric denotes 12 total markdown files in `SOMNARAK-WORLD/Unknown_Entities/` (excluding README.md), comprising 11 Unknown Sorrow Entity dossiers plus 1 Regressor Log Book (*Book of Regressor Log Dramaturgy*).

---

### 2. Narrative, Systems & Combat Metrics

| Category | Programmatic Count | Reference Path |
| :--- | :--- | :--- |
| **Story Cantos** | **6 Cantos** (01–06) | `SOMNARAK-WORLD/Story_Cantos/` |
| **Mnemonic Cycles** | **1,778 Cycles** | Canonical Absolvohan History |
| **Tactical Game Battle Scenarios & Systems** | **16 Scenarios** | `GAME_BATTLE/` |
| **M.A.W. Codex Sets** | **42 Sets** | `SOMNARAK-WORLD/MAW_Codex_Sets/` |
| **M.A.W. Equipment Profiles** | **1165 Markdown Dossiers** | `SOMNARAK-WORLD/MAW_Codex_Sets/` |
| **M.A.W. Complete Quadripartite Sets** | **198 / 198 Complete Sets** | `SOMNARAK-WORLD/MAW_Codex_Sets/` |
| **Specialist Cadres** | **10 Cadres** | `SOMNARAK-WORLD/Master_Codices/` |
| **Underworld Syndicates of The Raw** | **5 Syndicates** | `SOMNARAK-WORLD/Master_Codices/` |
| **Project Moon Research Volumes** | **16 Volumes** | `PROJECT_MOON_RESEARCH/` |

> **Unit Definition Note (M.A.W. Equipment):** The 1,165 M.A.W. Equipment Profiles metric counts individual profile dossiers exclusively across 42 sets. In total, the subtree contains 1,208 markdown files (1,165 profiles + 42 set registries + 1 master README). Complete quadripartite sets stand at 198 / 198 complete sets.

---

### 3. File System Aggregate Counts

| Repository Scope | Programmatic File Count |
| :--- | :--- |
| **`SOMNARAK-WORLD/` Subtree** | **1706 files** |
| **`docs/` Publishing Subtree** | **4 files** |
| **Total Non-Git Repository Files** | **1977 files** |

---

### Automated Verification Script
To re-verify and update all canonical metrics, execute:
```bash
python3 tools/generate_canonical_metrics_registry.py
```
