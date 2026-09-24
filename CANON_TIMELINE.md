# PROJECT SOMNARAK // CANONICAL CHRONOLOGY & TIMELINE ANCHORS
## Master Single Source of Truth (SSOT) for Planetary, Municipal & Cycle Chronology

```text
+========================================================================+
|             PROJECT SOMNARAK // CANONICAL TIMELINE ANCHOR              |
+========================================================================+
| Document ID          | TIMELINE-CANON-4238                             |
| Master Era Anchor    | Year 4,238 - The Dawn Initiative Era            |
| Current Cycle Anchor | Cycle 1,778 of The Absolvohan                   |
| Calendar Standard    | Mugenhan Municipal Solar Standard (MMSS)        |
| Dilation Law         | 1 Operational Cycle = ~1 Calendar Year          |
+========================================================================+
```

---

## 1. EPOCH DEFINITIONS & ERA ANCHORS

### The Primary Anchor: Year 4,238
The canonical baseline of the current era across all contemporary field records, operative dossiers, and administrative dispatches is **Year 4,238** (The Dawn Initiative Era). All relative historical time spans ("N years ago", "N centuries ago") are computed strictly relative to this date.

```text
[ Year 0 ] ----------------- [ Year 200 ] ----------------- [ Year 4,238 ]
Settlers Arrive              The Cheongula              Current Era Anchor
(4,238 Years Ago)            (4,038 Years Ago)               (Cycle 1,778)
```

---

## 2. CHRONOLOGICAL MILESTONES

| Calendar Year | Cycle Equivalent | Historical Milestone | Canon Reference |
| :--- | :--- | :--- | :--- |
| **Year 0** | Pre-Cycle Era | **The Settlement Arrival:** Refugee pioneers land on Mugenhan and establish the Somnarak valley settlement. | `SOMNARAK_CHEONGULA` |
| **Year 195** | Pre-Cycle Era | **The Menders' Warning:** Early syndicates identify volatile subterranean Han accumulation beneath Zone B. | `SOMNARAK_CHEONGULA` |
| **Year 200** | Pre-Cycle Era | **The Cheongula (The First Sorrow):** 1,000 citizens in Zone B consumed by raw Han; the First Sorrow and the Maw's inception. | `SOMNARAK_CHEONGULA` |
| **Year 2,460** | **Cycle 0001** | **The Absolvohan Inception:** Director Majin establishes the 1,778-Cycle containment loop to harvest and refine Han. | `The_ABSOLVOHAN` |
| **Year 3,972** | **Cycle 1,512** | **The Great Rust Severance (266 Cycles Ago):** Major syndicate rebellion in The Raw; massive extraction failure. | `CANTO_02`, `SED_03` |
| **Year 4,040** | **Cycle 1,580** | **The Great Collapse (198 Cycles / ~200 Years Ago):** Severe acoustic containment breach; death of Yoon's sister. | `CANTO_02` (B1 Fix) |
| **Year 4,238** | **Cycle 1,778** | **The Current Era:** The Absolvohan approaches the 1,778th realization; Dawn Initiative operational. | Contemporary Canon |

---

## 3. MNEMONIC CYCLE DILATION & OPERATIVE LONGEVITY (LAW B4)

To resolve the biological discrepancy of non-augmented operatives (such as Vanguard Min-Jae, Specialist Seol-A, and Striker Taeho) serving across 266+ cycles without mortal senility, the following canonical physics apply:

1. **Han-Saturation Cellular Stasis (  한 포화 세포 정체  , *Han Pohwa Sepo Jeongche*):**
   - High-density ambient Han in lower containment strata drastically reduces cellular oxidation and biological telomere decay.
2. **Mnemonic Cycle Dilation (  기억 주기 지연  , *Gieok Jugi Jiyeon*):**
   - When an Absolvohan cycle collapses and triggers a municipal reset, active operatives bound to high-grade M.A.W. weaponry or Echo-Cores do not experience continuous linear decades.
   - Between operational cycles, personnel are placed into cryo-engrammatic salt suspension within the deep vaults, waking only during active containment watches or breach alarms.
   - Their somatic age remains anchored to the date of their initial binding oath.

---

## 4. MATHEMATICAL VERIFICATION RULES FOR AUTOMATED LINTING

All automated scripts (e.g., `tools/timeline_lint.py`) must enforce the following validation constraints:
- `Current_Year == 4238`
- `Current_Cycle == 1778`
- `Cycle_Delta == Current_Cycle - Historical_Cycle`
- `Time_Ago_Years == Current_Year - Historical_Year`
- For Cycle 1,580: `1,778 - 1,580 = 198` -> Must be described as **"two hundred years ago"** (never "five hundred years ago").
- For Cycle 1,512: `1,778 - 1,512 = 266` -> Must be described as **"two hundred and sixty-six cycles ago"**.
- For Founding: Must be described as **"4,238 years ago"** (Settlement Year 0).

---

## 5. FORWARD-PROJECTION & CONTEMPORARY RECORD POLICY (F1 RULE)

To maintain absolute chronological integrity across all 1,778+ files in the repository, the following policies govern document dates, operative field logs, and future projections:

1. **Contemporary Operational Baseline (Year 4,238 Anchor):**
   - All active containment dossiers (`SOMNARAK-WORLD/Sorrow_Entities/`, `SOMNARAK-WORLD/Unknown_Entities/`), tactical field logs, Ordeal incident reports, and administrative memoranda represent active operations anchored strictly in **Year 4,238** (Cycle 1,778).
   - Document metadata dates (`**Date:** Year XXXX`) and field observation logs (`**Entry 2 — <Excerpt from Field Log, Year XXXX>**`) for active contemporary containment files must not exceed **Year 4,238**.
   - Any historical draft artifacts bearing dates from Years 4,239 through 4,255 in operational dossiers are classified as uncalibrated forward drift and must be re-anchored to **Year 4,238** (or contemporary retrospective range).

2. **Authorized Forward-Projections & Macro-Chronological Roadmaps:**
   The following explicit forward projections are recognized and canonically whitelisted:
   - **The Dawn Initiative Transmutation Milestone (Year 4,247):** The projected future milestone in `SOMNARAK_DAWN_OF_HOPE.md` where planetary transmutation shifts from 15% to 45%.
   - **Company 4 — The Wound Walkers Epilogue (Year 4,250+):** The post-Dawn spiritual pilgrimage chronicled in `SOMNARAK_WOUND_WALKERS.md` and referenced in master epilogue indices.
   - **Deep-Future Theoretical Simulations (Year 4,300+):** Mathematical models, simulated future breach projections, and cycle decay forecasts in `PROJECT_SOMNARAK.md` simulating far-future planetary entropy (e.g., Years 4,301, 4,567, 4,892, 5,234, 5,789).
   - **Short-Range Operational Forecasts (Year 4,239):** Explicit prospective statements predicting imminent cyclic phenomena within one year (e.g., "The next Han-storm season is predicted for Year 4239" in `SE-O-Vγ-003`).

