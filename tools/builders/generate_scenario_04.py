#!/usr/bin/env python3
"""
tools/generate_scenario_04.py
Generates GAME_BATTLE/SCENARIO_04_SED_SUNKEN_AQUEDUCT_DESCENT.md with 100% strict 71-column ASCII text box symmetry.
Uses wrap_box for every single text box to guarantee exact mathematical alignment.
"""

from box_formatter import make_box

def wrap_box(title, rows, width=71):
    box = make_box(title, rows, width)
    return "```text\n" + box + "\n```\n\n"

def build_scenario():
    content = []
    
    # Title Header
    content.append("# SCENARIO 04 — Somnarak Exploration Decree: Sunken Aqueduct Descent\n")
    content.append("## Tactical Engagement Record: Cryptasu Strata 1 Descent & The Drowned Guardian Suppression\n")
    content.append("### Canonical Tactical Scenario — SOP-GB-SCENARIO-004\n\n")
    
    # Header Box
    b0 = wrap_box("TACTICAL ENGAGEMENT RECORD: BATTLE-004-SUNKEN-AQUEDUCT", [
        "OPERATIONAL CAMPAIGN: Katabagil Passage 1 (Cryptasu / Flooded Catacomb)",
        "DEPLOYING WING     : Somnarak Exploration Decree (SED Vanguard Cadre)",
        "THEATER LOCATION   : Strata 1 Sub-Municipal Karst (-150m Subterranean)",
        "TARGET ENTITY/BEAST: SECC-012 The Drowned Guardian of Year Zero",
        "SURVEY SPECIALISTS : Yeonhwa (Lead), Sora (Diver), Kang, Jin (Medic)",
        "PRIMARY OBJECTIVE  : Tendril Rupture, Meltdown, & Strata 2 Gate Clearance"
    ])
    content.append(b0)
    
    content.append("""---

## 1. Tactical Overview & Operational Parameters

- **Topological Coordinate:** Strata 1 Sub-Municipal Karst, Culvert Gate 04 Threshold (-150m Depth).
- **Ambient Han Saturation:** 115 mHb Hydrostatic Sorrow Density (Freezing weeping brine at 4°C).
- **Environmental Hazard Modifiers:**
  * **Submerged Karst Basin:** Nodes `[N04]` to `[N07]` are submerged in 1.5 meters of frigid brine; physical movement costs +1 AP; all thermal/burn attacks are completely disabled.
  * **Geyser Vent Surge:** Node `[N06]` vents high-pressure subterranean brine geysers on Turn 3 and Turn 6, dealing 20 Weight damage and knocking occupants back 2 nodes.
  * **Acoustic Water Reverberation:** Ranged acoustic and sonar skills gain +2 Coin Power when fired into or through submerged nodes.
- **Mission Briefing:**
  During the initial descent into the drowned catacombs beneath Zone B, the SED Vanguard Survey Cadre encountered a dormant hydraulic apex beast: **SECC-012 The Drowned Guardian of Year Zero**. Nested directly over the primary culvert drainage valve at Depth -150m, the creature's massive barnacled bulk prevents the survey team from opening the water gates to drain the route into Strata 2. Lead Cartographer Yeonhwa must deploy her team across the flooded basin, sever the creature's grasping siphon tendrils, shatter its ancient basalt shell, and induce a Composure Meltdown to clear the passage.

---

## 2. Combatant Rosters & Technical Profiles

### 2.1 Allied SED Deep Survey Cadre

| Operative Callsign | Role | Base Spd | Max HP | Composure | Posture | Equipped M.A.W. Set | Range Band |
|---|---|---|---|---|---|---|---|
| **Yeonhwa (Lead)** | Sonar Pathfinder | 5 | 140 | 115 | 90 | Yeoul Gr 4 Sonar Needler | Band 2-3 (Mid) |
| **Specialist Sora** | Resonance Diver | 4 | 175 | 105 | 115 | Sim-Yeon Abyssal Harpoon | Band 1-2 (Mid) |
| **Rig Operator Kang**| Heavy Drill Breaker| 3 | 210 | 95 | 150 | Pneumatic Rock-Drill (Gr 4)| Band 1 (Melee) |
| **Depth Scribe Jin**| Ballast Medic | 4 | 125 | 120 | 80 | Chim-Mok Acoustic Siphon | Band 4 (Long) |

### 2.2 Hostile Entity: The Drowned Guardian of Year Zero (`SECC-012`)
- **Coherence Rank & Potency:** Rank III Fragment • Grade Beta Potency
- **Total Composure Pool:** 220 Points • Meltdown Threshold: 0 Points
- **Base Speed:** 3 (Generates 3 Action Points per turn)
- **Modular Body Part Anatomy:**

| Modular Part Name | Part Max HP | Rupture Threshold (60%) | Lament Def | Grudge Def | Void Def | Weight Def |
|---|---|---|---|---|---|---|
| **Hydrostatic Tendrils** | 600 HP | 360 HP | 1.2x | 0.8x | 1.5x | 0.6x |
| **Barnacled Basalt Shell**| 900 HP | 540 HP | 0.7x | 0.5x | 1.4x | 0.8x |
| **Brine-Weeping Maw** | 1,000 HP | 600 HP | 1.0x | 0.6x | 2.0x | 1.0x |

- **Hostile Intention Deck:**
  * **Hydrostatic Tendril Lash:** 2 AP • Range Band 1-3 • Weight • Base 20. Deals 30 kinetic damage and drags target 1 node deeper into water.
  * **Brine Geyser Vomit:** 1 AP • Range Band 1-4 • Void • Base 16. Bathes target node in freezing brine, draining 20 Composure.
  * **Shell Clamp Retaliation:** 2 AP • Range Band 1 • Defensive • Base 22. Retaliates against melee attacks with crushing shell clamp.

---

## 3. Initial 10-Node Grid Topography Map

""")

    # Grid Topography Box
    b_grid = wrap_box("INITIAL 10-NODE GRID TOPOGRAPHY — STRATA 1 CULVERT", [
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]    ",
        "[JIN]   [YEONHWA][KANG]  [SORA]  [WATER] [GEYSER][GUARDIAN BODY] [GATE] ",
        "Dry Karst Shelf [N01-03] | Submerged Basin [N04-07] | Culvert [N08-10]"
    ])
    content.append(b_grid)

    content.append("""- **Allied Starting Coordinates:** Scribe Jin at `[N01]`, Lead Yeonhwa at `[N02]`, Rig Operator Kang at `[N03]`, Specialist Sora at `[N04]`.
- **Terrain Modifiers:** Nodes `[N04]` to `[N07]` are submerged in frigid brine (movement costs +1 AP).
- **Hazard Point:** High-pressure brine geyser vent located at Node `[N06]`.
- **Target Position:** The Drowned Guardian occupies Nodes `[N07]` and `[N08]`.
- **Exploration Objective:** Strata 2 Culvert Valve & Descent Gate located at Node `[N10]`.

---

## 4. Turn-by-Turn Operational Chronicle

### Battle Turn 01: Submerged Ingress & Sonar Pinning

#### 1. Initiative & Action Point Allocation
- **Yeonhwa (Lead):** Rolled Speed 6 -> 4 Action Points (AP).
- **Specialist Sora:** Rolled Speed 4 -> 3 Action Points (AP).
- **Rig Operator Kang:** Rolled Speed 3 -> 2 Action Points (AP).
- **Depth Scribe Jin:** Rolled Speed 4 -> 3 Action Points (AP).
- **The Drowned Guardian:** Rolled Speed 3 -> 3 Action Points (AP) (Queues *Hydrostatic Tendril Lash* targeting `[N04]`).

#### 2. Node Maneuvers & Tactical Positioning
- Rig Operator Kang expends 2 AP to wade through the freezing water from `[N03]` to `[N04]`, positioning his heavy pneumatic drill in front of Sora.
- Specialist Sora holds position at `[N04]`, priming her abyssal harpoon (3 AP intact).
- Yeonhwa shifts from `[N02]` to `[N03]` on the dry shelf, establishing line-of-sight (1 AP spent, 3 AP remaining).
- Scribe Jin activates the acoustic life-ballast array at `[N01]` (3 AP intact).

#### 3. Clash & Parry Resolutions
- **Clash 01 (Kang vs Hydrostatic Tendril Lash):**
  * Kang queues *Pneumatic Drill Counter-Brace* (2 AP).
  * Kang Roll: Speed 3 + Drill Power 19 = 22.
  * Guardian Roll: Speed 3 + Tendril Power 18 = 21.
  * Result: **Kang Deflects (Margin +1)**. The spinning rock drill grinds violently against the wet tendril flesh, deflecting the blow. Guardian suffers 4 Posture strain; attack cancelled.

#### 4. Modular Part Damage & Composure Tracking
- Lead Yeonhwa fires a pressurized Sonar Harpoon from `[N03]` targeting the Hydrostatic Tendrils at `[N07]` (Distance = 4, Band 3 valid):
  * Acoustic Water Bonus: +2 Power applied!
  * Damage Dealt: 50 * Lament Multiplier (1.2x) = 60 Damage!
  * Hydrostatic Tendrils HP: 600 -> 540 / 600 (Rupture Threshold: 360 HP).
  * **Sonar Pin Inflicted:** All subsequent attacks against the tendrils gain +15% critical hit chance.
- Guardian Composure: 220 / 220. Posture: 96 / 100.

---

### Battle Turn 02: Tendril Grapple Crisis & Depth Siphon

#### 1. Initiative & Action Point Allocation
- **Yeonhwa (Lead):** Rolled Speed 5 -> 4 AP.
- **Specialist Sora:** Rolled Speed 5 -> 4 AP.
- **Rig Operator Kang:** Rolled Speed 3 -> 2 AP.
- **Depth Scribe Jin:** Rolled Speed 4 -> 3 AP.
- **The Drowned Guardian:** Rolled Speed 4 -> 3 AP (Queues *Hydrostatic Tendril Lash* targeting `[N04]` and *Brine Geyser Vomit*).

#### 2. Node Maneuvers & Grapple Crisis
- The Guardian's submerged tendril whips beneath the dark water, bypassing Kang's drill and wrapping around Specialist Sora at `[N04]`!
- Sora is dragged 1 node deeper into the freezing water, from `[N04]` to `[N05]`!
- Frigid brine floods Sora's diving suit, dealing 15 cold damage (HP: 175 -> 160) and 15 Composure drain (105 -> 90).
- Kang turns his heavy drill toward Node `[N05]`, wading through the water to support Sora (1 AP spent, 1 AP remaining).

#### 3. Clash & Severing Attacks
- **Severance Strike (Sora & Kang vs Grasping Tendril):**
  * Sora triggers *Abyssal Discharge* (2 AP) through her harpoon directly into the coiling limb:
    - Base Damage: 55 * Void (1.5x) * Critical (1.15x) = 95 Damage!
  * Kang drives the spinning rock drill into the base of the tendril (1 AP):
    - Base Damage: 60 * Weight (0.6x) = 36 Damage.
  * Yeonhwa fires a high-frequency pneumatic bolt (2 AP) into the nerve junction:
    - Base Damage: 45 * Lament (1.2x) = 54 Damage.
  * Total Round Tendril Damage: 185 Damage!
  * Hydrostatic Tendrils HP: 540 -> 355 / 600 -> **RUPTURE THRESHOLD (360 HP) BREACHED!**

#### 4. Part Rupture Trigger & Effect
- **PART RUPTURE CONFIRMED:** The primary grasping tendril splits and severs with a muffled acoustic pop beneath the water!
- **Mechanical Penalties Inflicted on Beast:**
  * All Tendril Lash and grapple skills permanently disabled!
  * Specialist Sora is immediately freed at Node `[N05]`.
  * The beast recoils into the culvert gate, suffering **Tactical Stagger**; all incoming damage multiplied by **1.5x** for 1 turn!
  * Guardian Composure drops: 220 -> 165 / 220. Posture collapses to 20 / 100.

---

### Battle Turn 03: Geyser Vent Eruption & Tactical Stagger Exploitation

#### 1. Initiative & Action Point Allocation
- **Yeonhwa (Lead):** Rolled Speed 6 -> 4 AP.
- **Specialist Sora:** Rolled Speed 4 -> 3 AP.
- **Rig Operator Kang:** Rolled Speed 4 -> 3 AP.
- **Depth Scribe Jin:** Rolled Speed 5 -> 4 AP.
- **The Drowned Guardian:** Staggered! (0 AP, Defense dice disabled).

#### 2. Hazard Resolution & Stagger Exploitation
- At Turn Start, Node `[N06]` violently erupts with a pressurized subterranean brine geyser!
- Fortunately, Sora holds at `[N05]` and the Guardian is at `[N07]`; neither unit is struck by the geyser plume.
- With the beast staggered and vulnerable, the squad concentrates heavy firepower to crack the **Barnacled Basalt Shell**:
- **Rig Operator Kang (Node 05):** Expends 3 AP on *Pneumatic Bedrock Drill*:
  * Base Damage: 110 * Weight (0.8x) * Stagger Multiplier (1.5x) = 132 Damage!
  * Basalt Shell HP: 900 -> 768 / 900.
- **Specialist Sora (Node 05):** Drives her electrified harpoon into the cracked shell seam (2 AP):
  * Base Damage: 85 * Void (1.4x) * Stagger (1.5x) = 178 Damage!
  * Basalt Shell HP: 768 -> 590 / 900 (Rupture Threshold: 540 HP).
- **Lead Yeonhwa (Node 03):** Fires armor-piercing sonar bolt (2 AP):
  * Damage Dealt: 65 * 1.4x * 1.5x = 136 Damage!
  * Basalt Shell HP: 590 -> 454 / 900 -> **SHELL RUPTURED!**

#### 3. Shell Rupture Aftermath
- The thick, ancient basalt carapace splits wide open, exposing the pulsating, violet **Brine-Weeping Maw** beneath.
- Guardian Composure: 165 -> 95 / 220.

---

### Battle Turn 04: The Exposed Maw & Freezing Breath Crisis

#### 1. Initiative & Action Point Allocation
- **Yeonhwa (Lead):** Rolled Speed 5 -> 4 AP.
- **Specialist Sora:** Rolled Speed 5 -> 4 AP.
- **Rig Operator Kang:** Rolled Speed 3 -> 2 AP.
- **Depth Scribe Jin:** Rolled Speed 4 -> 3 AP.
- **The Drowned Guardian:** Recovers from Stagger, rolls Speed 3 -> 3 AP (Queues *Brine Geyser Vomit* targeting `[N05]`).

#### 2. Interception & Protective Screen
- Kang steps into the front of Node `[N05]`, using his reinforced ballast shield to absorb the freezing brine spray.
  * Kang Roll: Speed 3 + Shield 20 = 23 vs Guardian Vomit 17.
  * Result: **Kang Blocks**. Brine spray deflected harmlessly into the water.
- Depth Scribe Jin channels *Cryo-Stabilizing Infusion* from Node `[N01]`, restoring 25 Composure to Sora (Composure: 90 -> 105).

#### 3. Coordinated Core Damage
- Specialist Sora charges forward through the water into Node `[N06]`, thrusting her abyssal harpoon directly into the exposed Brine-Weeping Maw (2 AP):
  * Base Damage: 80 * Void Multiplier (2.0x) = 160 Massive Damage!
  * Weeping Maw HP: 1,000 -> 840 / 1,000.
- Lead Yeonhwa fires two consecutive sonar darts into the exposed nerve bundle (2 AP):
  * Total Damage: 110 Damage!
  * Weeping Maw HP: 840 -> 730 / 1,000.
- Guardian Composure: 95 -> 50 / 220. Posture: 35 / 100.

---

### Battle Turn 05: Brine-Weeping Maw Meltdown (Terminal Collapse)

#### 1. Initiative & Action Point Allocation
- **Yeonhwa (Lead):** Rolled Speed 6 -> 4 AP.
- **Specialist Sora:** Rolled Speed 5 -> 4 AP.
- **Rig Operator Kang:** Rolled Speed 4 -> 3 AP.
- **Depth Scribe Jin:** Rolled Speed 5 -> 4 AP.
- **The Drowned Guardian:** Rolled Speed 2 -> 2 AP (Queues desperate thrash *Drowning Flail*).

#### 2. The Final Cognitive Neutralization
- Scribe Jin identifies the central sorrow crystallization node within the beast's mouth and loads an acoustic resonance spike into his siphon array (3 AP):
  * Jin fires directly from `[N01]` across the acoustic water corridor into the open maw at `[N07]`.
  * Water Resonance Multiplier: +2 Coin Power!
  * Direct Void Damage: 95 * 2.0x = 190 True Damage!
  * Weeping Maw HP: 730 -> 540 / 1,000 -> **MAW RUPTURED!**
  * Composure Drain: -80 Composure Points!
  * **COMPOSURE POOL HIT: 50 - 80 = 0 POINTS!**

#### 3. Terminal Meltdown Trigger
- **TERMINAL MELTDOWN ACTIVE:** The Drowned Guardian lets out a hollow, gargling acoustic shriek; the brine within its body crystallizes rapidly into dark ice.
- All defenses collapse to **2.0x Fatal vulnerability**!
- The beast slumps lifelessly against the culvert basin floor at Nodes `[N07-08]`.

---

### Battle Turn 06: Synchronized Culvert Gate Unlocking & Descent Route Clearance

#### 1. Final Execution & Valve Operation
- **Rig Operator Kang & Specialist Sora (Node 07):** Drive heavy pneumatic ground anchors through the beast's immobilized shell, pinning the carcass firmly against the bedrock to prevent it from obstructing water flow.
- **Lead Cartographer Yeonhwa (Node 10):** Advances to the ancient bronze wheel of Culvert Gate 04:
  * Yeonhwa and Kang apply 450 kg of pneumatic torque to the frozen wheel.
  * The ancient bronze gears groan and rotate; the heavy sluice gate rises with a rush of foaming water.
- Thousands of gallons of trapped weeping brine drain out of the basin, descending through the massive culvert conduit directly toward Strata 2 (-350m Depth).
- Scribe Jin establishes the acoustic telemetry beacon, logging the descent path as officially open and secure.

---

## 5. Macro Phase-End Resolution Block (Phase 01 Complete)

""")

    # Phase-End Box
    b_phase = wrap_box("MACRO PHASE-END RESOLUTION SUMMARY — BATTLE 04", [
        "COMPLETED PHASE  : Combat Phase 01 (Battle Turns 01 to 06)",
        "BEAST STATUS     : Tendrils Severed (355 HP) • Shell Shattered (454 HP)",
        "MAW STATUS       : Ruptured (540 HP) • Vitrified in Dormant Sorrow Ice",
        "COMPOSURE POOL   : 0 / 220 (Terminal Meltdown Confirmed)",
        "DRAINAGE STATUS  : Culvert Gate 04 Open • Basin Water Drained 80%",
        "SQUAD CASUALTIES : 0 Fatalities • Specialist Sora (15 HP Frigid Trauma)"
    ])
    content.append(b_phase)

    content.append("""---

## 6. After-Action Report & Survey Manifest

""")

    # After-Action Box
    b_aar = wrap_box("AFTER-ACTION TACTICAL REPORT & SURVEY MANIFEST", [
        "ENGAGEMENT RESULT: Decisive Descent Victory • Strata 2 Route Unlocked",
        "HYDROLOGY REPORT : Culvert 04 Flow Stable • Water Level Dropped 1.8m",
        "SPECIMEN HARVEST : 420 Liters Weeping Brine • 60 kg Basalt Shell Ore",
        "RELIC RECOVERED  : 1x Year Zero Karst Survey Log (Bronze Cylinder)",
        "DESCENT STATUS   : SED Expedition cleared for Passage 2 Ingress",
        "COMMENDATION     : Yeonhwa & Kang cited for rapid hydraulic bypass"
    ])
    content.append(b_aar)

    content.append("""---
*End of Canonical Tactical Scenario SOP-GB-SCENARIO-004.*
""")
    
    return "".join(content)

if __name__ == "__main__":
    scenario_text = build_scenario()
    target_path = "GAME_BATTLE/SCENARIO_04_SED_SUNKEN_AQUEDUCT_DESCENT.md"
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(scenario_text)
    print(f"Successfully wrote {len(scenario_text)} bytes to {target_path}")
