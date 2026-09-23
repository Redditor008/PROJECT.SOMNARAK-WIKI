# BATTLE SCENARIO TEMPLATE — Standardized Tactical Engagement Format
## Canonical Blueprint for All Future Game Battle Documents

```text
+---------------------------------------------------------------------+
| TACTICAL ENGAGEMENT RECORD: [INSERT BATTLE DESIGNATION CODE]        |
+---------------------------------------------------------------------+
| Operational Area  : [Insert District / Zone / Subterranean Strata]  |
| Threat Rating     : [Insert Rank I-V] ([Insert Grade α-ω Potency])  |
| Strike Team       : [Insert Squad Name] ([Assigned Wing/Faction])   |
| Squad Strength    : 4 Operatives ([Insert Operative Names])         |
| Primary Objective : [Insert Primary Objective / Extraction / Purge] |
+---------------------------------------------------------------------+
```

## 1. Tactical Overview & Operational Parameters

- **Topological Coordinate:** [Insert Sector, e.g., Zone B Maw Perimeter, Depth -450m]
- **Ambient Han Saturation:** [Insert Saturation Level, e.g., 35% Ambient Weeping Density]
- **Environmental Hazard Modifiers:**
  * [Hazard 1: e.g., Acoustic Echo Reverberation (+10% Lament Strain)]
  * [Hazard 2: e.g., Collapsed Basalt Rubble (Nodes [N04] and [N05] cost 2 AP to traverse)]
- **Mission Briefing:**
  [Provide a 100-to-150-word in-universe operational summary detailing why the squad was dispatched, what containment or pacification failure occurred, and what operational threshold must be reached.]

---

## 2. Combatant Rosters & Technical Profiles

### 2.1 Allied Strike Team (4 Operatives)

| Operative Callsign | Role | Base Spd | Max HP | Composure | Posture | Equipped M.A.W. Set | Range Band |
|---|---|---|---|---|---|---|---|
| **Operative 1** | Vanguard | 5 | 160 | 100 | 120 | MAW-[Set ID] (Grade γ) | Band 1 (Melee) |
| **Operative 2** | Striker | 4 | 140 | 90 | 100 | MAW-[Set ID] (Grade γ) | Band 2 (Short) |
| **Operative 3** | Acoustic Lead | 4 | 120 | 110 | 80 | MAW-[Set ID] (Grade β) | Band 3 (Medium) |
| **Operative 4** | Anchor / Sniper | 3 | 110 | 100 | 90 | MAW-[Set ID] (Grade γ) | Band 4 (Long) |

### 2.2 Hostile Entity: [Insert Canonical Name] (`[Insert SECC Code]`)
- **Coherence Rank & Potency:** Rank [I to V] • Grade [α to ω]
- **Total Composure Pool:** [e.g., 250 Points] • Meltdown Threshold: 0 Points
- **Modular Body Part Anatomy:**

| Modular Part Name | Part Max HP | Rupture Threshold (60%) | Lament Def | Grudge Def | Void Def | Weight Def |
|---|---|---|---|---|---|---|
| **Part 1 (e.g., Head)** | 500 HP | 300 HP | 0.8x | 1.0x | 1.2x | 0.5x |
| **Part 2 (e.g., Core)** | 800 HP | 480 HP | 1.0x | 0.7x | 1.0x | 0.4x |
| **Part 3 (e.g., Limb)** | 400 HP | 240 HP | 1.2x | 1.2x | 0.8x | 1.0x |

- **Hostile Intention Deck:**
  * **Skill A (Basic Attack):** AP Cost [1-2] • Target Band [1-3] • Element [Grudge/Lament/Void/Weight] • Base Power [10-18].
  * **Skill B (Heavy / Elite Attack):** AP Cost [2-3] • Target Band [2-4] • Element [Grudge/Lament/Void/Weight] • Base Power [20-32].

---

## 3. Initial 10-Node Grid Topography Map

```text
+---------------------------------------------------------------------+
|                 INITIAL 10-NODE GRID TOPOGRAPHY                     |
+---------------------------------------------------------------------+
| [N01]   [N02]   [N03]   [N04]   [N05]   [N06]   [N07]   [N08]  ...  |
| [OP-04] [OP-03] [OP-02] [OP-01] [COVER] -----   [HOSTILE BODY]      |
| Allied Deployment [N01-03] | Center [N04-06] | Hostile Zone [N07-10]|
+---------------------------------------------------------------------+
```

- **Allied Starting Nodes:** Operative 4 at `[N01]`, Operative 3 at `[N02]`, Operative 2 at `[N03]`, Operative 1 at `[N04]`.
- **Environmental Markers:** Industrial Bulkhead / Destructible Cover located at `[N05]`.
- **Hostile Position:** Modular Target occupies `[N07]` and `[N08]`.

---

## 4. Turn-by-Turn Operational Chronicle

### Battle Turn 01: Initial Advance & Reconnaissance Clashes

#### 1. Initiative & Action Point Allocation
- **Operative 1:** Rolled Speed 5 -> 4 Action Points (AP).
- **Operative 2:** Rolled Speed 4 -> 3 Action Points (AP).
- **Operative 3:** Rolled Speed 4 -> 3 Action Points (AP).
- **Operative 4:** Rolled Speed 3 -> 2 Action Points (AP).
- **Hostile Target:** Rolled Speed 3 -> 3 Action Points (AP).

#### 2. Node Maneuvers & Tactical Positioning
- Operative 1 advances from `[N04]` to `[N05]`, taking position behind the industrial bulkhead (1 AP spent, 3 AP remaining).
- Operative 2 advances from `[N03]` to `[N04]` (1 AP spent, 2 AP remaining).
- Operative 3 and Operative 4 hold positions at `[N02]` and `[N01]` respectively.

#### 3. Clash & Parry Resolutions
- **Clash 01:** Operative 1 queues Defensive Parry vs Hostile Skill A targeting `[N05]`.
  * Operative 1 Roll: Speed 5 + Shield Power 12 = 17.
  * Hostile Roll: Speed 3 + Attack Power 11 = 14.
  * Result: **Operative 1 Deflects (Margin +3)**. Hostile suffers 6 direct Posture strain. Hostile attack cancelled.

#### 4. Modular Part Damage & Composure Tracking
- Operative 4 fires long-range kinetic bolt from `[N01]` targeting Part 3 at `[N07]` (Distance = 6, Band 4 valid).
  * Damage Dealt: 45 Grudge Damage.
  * Part 3 HP: 400 -> 355 / 400 (Rupture Threshold: 240 HP).
- Hostile Composure: Unchanged (250 / 250).

---

### Battle Turn 02: Pressure Escalation & Part Targeting
[Document Turn 02 following the identical five-part sub-structure.]

---

### Battle Turn 03: Part Rupture Threshold Breach
[Document Turn 03, highlighting when a body part crosses below its 60% HP threshold, triggering Part Rupture.]

---

### Battle Turn 04: Tactical Stagger Exploitation
[Document Turn 04, detailing the 1.5x damage bonus against the ruptured part.]

---

### Battle Turn 05: Composure Meltdown Breach
[Document Turn 05, detailing when Hostile Composure hits 0, triggering Terminal Meltdown.]

---

### Battle Turn 06: Phase Climax & Synchronized Execution
[Document Turn 06, detailing maximum damage exploitation during the Terminal Meltdown window.]

---

## 5. Macro Phase-End Resolution Block (Phase 01 Complete)

```text
+---------------------------------------------------------------------+
|                 MACRO PHASE-END RESOLUTION SUMMARY                  |
+---------------------------------------------------------------------+
| Completed Phase   : Combat Phase 01 (Battle Turns 01 to 06)         |
| Sorrow Tide Tick  : Ambient Han Saturation increased from 35% to 45%|
| Part Status       : Part 3 Ruptured (Disabled) • Part 1 Intact      |
| Hostile Composure : Meltdown Active (Recovers to 50 pts at Phase 02)|
| Squad Status      : All Operatives Combat-Capable (0 Casualties)    |
+---------------------------------------------------------------------+
```

- **Sorrow Tide Escalation:** Ambient weeping mist intensifies (+10% ambient saturation).
- **Status Ticks:** Lingering Bleed/Resonance ticks resolve across combatants.
- **Boss Stance Transition:** If HP crosses a major milestone (e.g., 50%), the boss transitions to its enrage stance.

---

## 6. After-Action Report & Extraction Manifest

```text
+---------------------------------------------------------------------+
|         AFTER-ACTION TACTICAL REPORT & EXTRACTION MANIFEST          |
+---------------------------------------------------------------------+
| Engagement Result : Decisive Tactical Victory                       |
| Harvest Recovered : 420 kg Refined Liquid Han / 85 kg Han Dust      |
| M.A.W. Extracted  : 1x Weapon Core (Grade γ) • 1x Suit Weave        |
| Squad Casualties  : 0 Fatalities • Operative 1 Light Posture Strain |
| Debrief Status    : Cleared for Return to Central Sector Garrison   |
+---------------------------------------------------------------------+
```

- **Tactical Evaluation:** Analysis of squad synergy, range band adherence, and clash efficiency.
- **Quarantine & Recovery:** Operatives report to Reverie Directorate Composure Restoration Pods.

---

**Template Classification:** `SOMNARAK-GBS-TEMPLATE-001`  
**Standard Authority:** Reverie Directorate Tactical Simulation Bureau
