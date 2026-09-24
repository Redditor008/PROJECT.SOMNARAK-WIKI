# PROJECT SOMNARAK // CANONICAL CHRONOLOGY & TIMELINE ANCHORS
## Master Single Source of Truth (SSOT) for Planetary, Municipal & Cycle Chronology

```text
+========================================================================+
|             PROJECT SOMNARAK // CANONICAL TIMELINE ANCHOR              |
+========================================================================+
| Document ID           | TIMELINE-CANON-4238                            |
| Master Era Anchor     | Year 4,238 - The Dawn Initiative Era           |
| Current Cycle Anchor  | Cycle 1,778 of The Absolvohan                  |
| Calendar Standard     | Mugenhan Municipal Solar Standard (MMSS)       |
| Dilation Law          | 1 Operational Cycle = ~1 Calendar Year         |
+------------------------------------------------------------------------+
| Sequential Triad      | SED -> UCD -> R.D. (Strictly Pre-Dawn)         |
| Watershed Turning     | The Dawn of Hope (Cycle 1,778 / Year 4,238)    |
| Post-R.D. / Post-Dawn | UNK SE (After R.D.) + All Subsequent Lore      |
+========================================================================+
```

---

## 1. EPOCH DEFINITIONS & ERA ANCHORS

### The Primary Anchor: Year 4,238
The canonical baseline of the current era across all contemporary field records, operative dossiers, and administrative dispatches is **Year 4,238** (The Dawn Initiative Era). All relative historical time spans ("N years ago", "N centuries ago") are computed strictly relative to this date.

```text
[ Year 0 ] ------ [ Year 200 ] ------ [ Year 2,460 ] ------ [ Year 4,238 ]
Settler Landing   The Cheongula       Cycle 0001 (R.D.)     Dawn of Hope  
(4,238 Yrs Ago)   (4,038 Yrs Ago)     (1,778 Cycles Ago)    (Watershed)   
```

---

## 2. CHRONOLOGICAL MILESTONES

| Calendar Year | Cycle Equivalent | Historical Milestone & Canonical Operation | Canon Reference |
| :--- | :--- | :--- | :--- |
| **Year 0** | Pre-Cycle Era | **The Settlement Arrival:** Refugee pioneers land on Mugenhan and establish the Somnarak valley settlement. | `SOMNARAK_CHEONGULA` |
| **Year 195** | Pre-Cycle Era | **The Menders' Warning:** Early syndicates identify volatile subterranean Han accumulation beneath Zone B. | `SOMNARAK_CHEONGULA` |
| **Year 200** | Pre-Cycle Era | **The Cheongula (The First Sorrow):** 1,000 citizens in Zone B consumed by raw Han; the First Sorrow and the Maw's inception. | `SOMNARAK_CHEONGULA` |
| **Year 2,460** | **Cycle 0001** | **The Absolvohan Inception:** Director Majin establishes the 1,778-Cycle containment loop to harvest and refine Han. | `The_ABSOLVOHAN` |
| **Years 2,460–3,970** | **Cycles 0001–1,510** | **Ante-Dawn Phase 1 — SED (Katabagil):** Subterranean expeditions 1–7 explore bedrock (-2,000m to -3,500m), mapping aquifers and Cheongula origins. | `SOMNARAK-WORLD/Katabagil/` |
| **Year 3,972** | **Cycle 1,512** | **The Great Rust Severance (266 Cycles Ago):** Major syndicate rebellion in The Raw; massive extraction failure. | `CANTO_02`, `SED_03` |
| **Years 3,973–4,039** | **Cycles 1,513–1,579** | **Ante-Dawn Phase 2 — UCD (Katharcheok):** Six underworld pacification purges through The Raw, dismantling the Five Syndicates. | `SOMNARAK-WORLD/Katharcheok/` |
| **Year 4,040** | **Cycle 1,580** | **The Great Collapse (198 Cycles / ~200 Years Ago):** Severe acoustic containment breach; death of Yoon's sister. | `CANTO_02` (B1 Fix) |
| **Years 4,041–4,238** | **Cycles 1,581–1,778** | **Ante-Dawn Phase 3 — R.D. (The Absolvohan):** Containment of 292 standard Sorrow Entities across Floors 1–8; Echo-Core Realizations. | `SOMNARAK-WORLD/The_Absolvohan/` |
| **Year 4,238** | **Cycle 1,778 (Climax)** | **THE WATERSHED EVENT — THE DAWN OF HOPE:** Hand of Hope opens; 15% sorrow-to-hope transmutation; SED, UCD, and R.D. conclude. | `SOMNARAK_DAWN_OF_HOPE.md` |
| **Year 4,238+** | **Post-Cycle Era** | **UNK SE Manifestation (Strictly After R.D.):** 12 authentic anomaly dossiers emerge in the deep vault and post-loop aftermath. | `SOMNARAK-WORLD/Unknown_Entities/` |
| **Years 4,238–4,247** | **Post-Dawn Phase 1** | **The Dawn Initiative:** The 12 Hope Bearers operate mobile fortress *The Lantern*, expanding hope from 15% toward 45%. | `SOMNARAK_DAWN_OF_HOPE.md` |
| **Year 4,239+** | **Post-Dawn Phase 2** | **The Horizon Caravan (Jipyeongseondae):** Six overland expeditions cross the wasteland to Cheonbulok and Mugeukji. | `SOMNARAK-WORLD/Jipyeongseondae/` |
| **Year 4,240+** | **Post-Dawn Phase 3** | **The Memory Archive (Gieok Jeojangso):** Reception protocol across seven strata floors extracting Key Pages for the Silent City. | `SOMNARAK-WORLD/Gieok_Jeojangso/` |
| **Year 4,250+** | **Post-Dawn Phase 4** | **Company 4 — The Wound Walkers:** Sooah's post-Dawn spiritual pilgrimage across the Seven Crucible Stations. | `SOMNARAK_WOUND_WALKERS.md` |
| **Year 4,255+** | **Global Era** | **Continental Reconstruction:** Trans-continental rail relays, tectonic stabilization, and external civil reconnection. | Master Narrative SSOT |

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

---

## 6. THE MACRO-CHRONOLOGICAL EPOCH PARTITION (THE THREE WINGS & POST-DAWN LAW)

### Binding Canon Law
By direct executive decree of the Project Owner:
**"All This Three SED, UCD, AND R.D. Happen Before DAWN OF HOPE And ANYTHING ELSE HAPPEN AFTER DAWN OF HOPE."**
**"UNK SE Is After R.D. Even"**
**"CONTINENTAL GEOGRAPHY IS NOT AN SE"**

```text
+========================================================================+
|        PROJECT SOMNARAK // MACRO-CHRONOLOGICAL EPOCH PARTITION         |
+========================================================================+
| Ante-Dawn Epoch       | SED -> UCD -> R.D. (Strictly Pre-Dawn)         |
| Watershed Event       | The Dawn of Hope (Cycle 1,778 / Year 4,238)    |
| Post-R.D. / Post-Dawn | UNK SE (After R.D.) + All Subsequent Lore      |
+------------------------------------------------------------------------+
| Sovereign Canon Law   | SED -> UCD -> R.D. -> DAWN OF HOPE -> ALL ELSE |
| UNK SE Canon Rule     | UNK SE occurs strictly AFTER R.D. operations   |
+========================================================================+
```

```text
[ EPOCH I: ANTE-DAWN ]     [ WATERSHED EVENT ]     [ EPOCH II: POST-DAWN ]
SED -> UCD -> R.D. Wings ->    DAWN OF HOPE    ->  UNK SE & Post-Dawn Lore
(Pre-Dawn Tripartite)       (Cycle 1,778)          (After R.D. & All Else)
```

### 6.1 Epoch I: The Ante-Dawn Era (Before Dawn of Hope — Pre-Cycle to Cycle 1,778)
All primary operations, exploration logs, and tactical chronicles of the founding tripartite wings occur strictly **BEFORE** the Dawn of Hope in sequential progression:
1. **Subterranean Expedition Division (SED / Katabagil):**
   - The seven expeditionary descent passages (`SOMNARAK-WORLD/Katabagil/`, Passages 1–7) exploring the ancient bedrock (-2,000m to -3,500m), mapping the subterranean aquifers, and uncovering the deep origins of the Maw and the Cheongula.
2. **Underworld Cleanup Descend (UCD / Katharcheok):**
   - The six pacification purge arcs (`SOMNARAK-WORLD/Katharcheok/`, Purges 1–6) across The Raw, dismantling the Five Syndicates (Veil Merchants, Memory Washers, Harvesters, Debt Brokers, Entity Traders) and neutralizing rogue constructs.
3. **The Reverie Directorate (R.D. / The Absolvohan):**
   - Facility 01 containment operations, Han-Energy harvesting, and the continuous 1,778-Cycle loop under Director Majin and the Echo-Core Leads.
   - The containment, research, and pacification of the 292 canonical Sorrow Entities across Floors 1 through 8.
   - The Floor Realizations of the departmental Leads (Dekan, Zyrak, Marjuk, Sooah, Mellda, Ayshuk, Xyan, Ishall, Seiyon).

### 6.2 The Watershed Turning Point: The Dawn of Hope (Cycle 1,778 / Year 4,238)
The central turning point in planetary history:
- At the climax of the 1,778th Cycle, the Hand of Hope (  희망의 손  , *Huimang-ui Son*) opens.
- 15% of Somnarak's ambient sorrow is transmuted into resonant Hope Entities (HT-001 through HT-012, The Trinity, and Hand of Hope).
- The three foundational operations (SED, UCD, R.D.) conclude their primary ante-Dawn mandates, providing the stabilized foundation for the new era.

### 6.3 Epoch II: The Post-Dawn & Post-R.D. Era (After Dawn of Hope & After R.D. — Year 4,238 to Year 4,250+)
**ANYTHING ELSE** in the narrative chronology takes place strictly **AFTER** the Dawn of Hope, and **UNK SE is positioned strictly AFTER R.D.**:
1. **Unknown Sorrow Entities (UNK SE /   미분류 슬픔 개체  ):**
   - Canonical Mandate: **UNK SE Is After R.D.**
   - While the 292 standard Sorrow Entities are contained during R.D. Facility 01's 1,778-cycle loops, the 12 authentic Unknown Sorrow Entities (`SOMNARAK-WORLD/Unknown_Entities/`) manifest and are recorded strictly **AFTER R.D.**:
     - `SE-N-IVγ-250 The Extinguished` specifically tracks and hunts Hope Bearers (who emerge only after the Dawn of Hope).
     - `SE-N-IIIβ-247 The Undelivered Thanks` carries gratitude stones honoring fallen Hope Bearers.
     - `SE-N-IVδ-902 The Repeated Survivor` and `Book of Regressor Log Dramaturgy` record the meta-conscious aftermath of the broken loop cycles.
     - Outside Sorrow frontier anomalies (such as The Glass Silt Drifter and The Singing Needle) are discovered beyond Somnarak in the unmapped frontier during post-R.D. overland expeditions. Continental landmasses and regional geology are permanent terrain, not Sorrow Entities.
2. **The Dawn Initiative (  새벽 이니셔티브  , *Saebyeok Inisieotibeu*):**
   - The 12 Hope Bearers operating from the mobile fortress *The Lantern* (  등불  , *Deungbul*), expanding hope from 15% to 45% across the continent (`SOMNARAK_DAWN_OF_HOPE.md`).
3. **The Horizon Caravan (Jipyeongseondae /   지평선대  ):**
   - The six trans-desolate overland expedition arcs crossing the wasteland to reconnect Somnarak with the forgotten cities of Cheonbulok and Mugeukji (`SOMNARAK-WORLD/Jipyeongseondae/`).
4. **The Memory Archive (Gieok Jeojangso /   기억저장소  ):**
   - Secretary Seiyon's Library Reception Protocol across the seven subterranean strata floors, transmuting historical trauma into sovereign Key Pages to awaken the Silent City (`SOMNARAK-WORLD/Gieok_Jeojangso/`).
5. **The Wound Walkers (Company 4 /   상처 걷는 자  ):**
   - The post-Dawn spiritual pilgrimage of Sooah across the Seven Crucible Stations in Year 4,250+ to heal the lingering municipal scars that remain after all other companies have finished (`SOMNARAK_WOUND_WALKERS.md`).
6. **Continental Reconstruction & Global Reconnection:**
   - All subsequent expeditions beyond Mugenhan's perimeter, planetary tectonic stabilization, and the establishment of post-Dawn civil institutions.
