#!/usr/bin/env python3
"""
tools/generate_scenario_03.py
Generates GAME_BATTLE/SCENARIO_03_UNDERWORLD_RUST_VEIL_PURGE.md with 100% strict 71-column ASCII text box symmetry.
Uses wrap_box for every single text box to guarantee exact mathematical alignment.
"""

from box_formatter import make_box

def wrap_box(title, rows, width=71):
    box = make_box(title, rows, width)
    return "```text\n" + box + "\n```\n\n"

def build_scenario():
    content = []
    
    # Title Header
    content.append("# SCENARIO 03 — Underworld Cleanup Descend: The Rust & Veil Purge\n")
    content.append("## Tactical Engagement Record: Mask Market Foundry Sweep & Fray Construct Neutralization\n")
    content.append("### Canonical Tactical Scenario — SOP-GB-SCENARIO-003\n\n")
    
    # Header Box
    b0 = wrap_box("TACTICAL ENGAGEMENT RECORD: BATTLE-003-RUST-VEIL-PURGE", [
        "OPERATIONAL CAMPAIGN: Katharcheok Operation 1 (Velumtal / The Mask Market)",
        "DEPLOYING WING     : Underworld Cleanup Descend (UCD Joint Task Force)",
        "THEATER LOCATION   : Zone D Mantle Commons Sub-Drainage (-25m Depth)",
        "TARGET ENTITY/RIG  : The Slag-Forged Breaker (Illicit Fray Construct)",
        "STRIKE OFFICERS    : Commander Taeho, Officer Joon, Seol-A, Min-Jae",
        "PRIMARY OBJECTIVE  : Breach Foundry, Dismantle Construct, Seize Core"
    ])
    content.append(b0)
    
    content.append("""---

## 1. Tactical Overview & Operational Parameters

- **Topological Coordinate:** Zone D Mantle Commons Sub-Sluice 4, Foundry Terminal (-25m Depth).
- **Ambient Han Saturation:** 30% Mixed Sorrow Saturation (Choking sulfur vapors and Weeping mist).
- **Environmental Hazard Modifiers:**
  * **Superheated Slag Vents:** Nodes `[N05]` and `[N06]` vent boiling runoff at Turn End; units occupying these nodes take 15 true burn damage.
  * **Acoustic Baffle Shadows:** Nodes `[N07]` to `[N10]` are muffled by illegal Chim-Mok dampening baffles; ranged attacks suffer -2 Coin Power.
  * **Cramped Subterranean Tunnel:** Narrow 3-meter aqueduct corridor; maximum 2 allied units may occupy the same node without stacking penalties.
- **Mission Briefing:**
  Following intelligence extracted from captured Shroud Couriers, UCD Task Force Alpha launched a rapid-entry raid against an unregistered Veil foundry in Sub-Sluice 4. The syndicate—operating under a joint pact between the Veil Merchants and Rust Frays—has deployed an illegal industrial combat rig: **The Slag-Forged Breaker**. Powered by an illicitly harvested sorrow core (`SECC-019`) and armed with a high-pressure pneumatic demolition hammer, the construct guards the vault blast door. Commander Taeho must breach the frontline, shatter the construct's kinetic hammer, and force a Composure Meltdown to secure the illicit dies before the syndicate can flood the sluice.

---

## 2. Combatant Rosters & Technical Profiles

### 2.1 Allied UCD Tactical Strike Cadre

| Operative Callsign | Role | Base Spd | Max HP | Composure | Posture | Equipped M.A.W. Set | Range Band |
|---|---|---|---|---|---|---|---|
| **Commander Taeho** | Vanguard Cleaver | 5 | 180 | 105 | 120 | MAW-W-014 (Grade γ Blade) | Band 1 (Melee) |
| **Officer Joon** | Hydraulic Rammer | 4 | 200 | 95 | 140 | Heavy Piston Ram (Gr 4) | Band 1-2 (Mid) |
| **Officer Seol-A** | Acoustic Scribe | 5 | 130 | 120 | 85 | MAW-W-088 (Grade γ Needle)| Band 2-3 (Mid) |
| **Enforcer Min-Jae**| Fortress Pavise | 3 | 220 | 100 | 160 | Cheol-Gyeong Basalt Pavise | Band 1 (Melee) |

### 2.2 Hostile Construct: The Slag-Forged Breaker (`RIG-FRAY-019`)
- **Coherence Rank & Potency:** Rank III Fragment • Grade Beta Potency
- **Total Composure Pool:** 200 Points • Meltdown Threshold: 0 Points
- **Base Speed:** 3 (Generates 3 Action Points per turn)
- **Modular Body Part Anatomy:**

| Modular Part Name | Part Max HP | Rupture Threshold (60%) | Lament Def | Grudge Def | Void Def | Weight Def |
|---|---|---|---|---|---|---|
| **Pneumatic Slag-Hammer**| 650 HP | 390 HP | 1.0x | 0.8x | 1.2x | 0.5x |
| **Smelted Basalt Plating**| 1,100 HP| 660 HP | 0.6x | 0.5x | 1.5x | 0.7x |
| **Contraband Shroud Core**| 400 HP | 240 HP | 1.5x | 1.0x | 2.0x | 1.0x |

- **Hostile Intention Deck:**
  * **Demolition Hammer Slam:** 2 AP • Range Band 1-2 • Weight • Base 22. Deals 35 kinetic damage and 15 Posture strain.
  * **Sulfur Slag Venting:** 1 AP • Range Band 1-3 Area • Grudge Burn • Base 16. Bathes target node in molten slag.
  * **Hydraulic Rush:** 2 AP • Range Band 1-4 • Kinetic • Base 20. Charges forward 2 nodes, knocking targets aside.

---

## 3. Initial 10-Node Grid Topography Map

""")

    # Grid Topography Box
    b_grid = wrap_box("INITIAL 10-NODE GRID TOPOGRAPHY — SUB-SLUICE 4", [
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]    ",
        "[SEOL-A] [MIN-J] [JOON]  [TAEHO] [COVER] [VENT]  [BREAKER BODY]  [VAULT]",
        "Allied Sluice Ingress [N01-03] | Canal [N04-06] | Hostile Sector [N07-10]"
    ])
    content.append(b_grid)

    content.append("""- **Allied Starting Coordinates:** Officer Seol-A at `[N01]`, Enforcer Min-Jae at `[N02]`, Officer Joon at `[N03]`, Commander Taeho at `[N04]`.
- **Destructible Cover:** Reinforced Maintenance Baffle located at `[N05]`.
- **Environmental Hazard:** Active Sulfur Slag Vent located at `[N06]`.
- **Hostile Position:** The Slag-Forged Breaker occupies Nodes `[N07]` and `[N08]`.
- **Mission Objective:** Subterranean Foundry Vault Blast Door located at `[N10]`.

---

## 4. Turn-by-Turn Operational Chronicle

### Battle Turn 01: Sluice Breach & Heavy Pavise Clash

#### 1. Initiative & Action Point Allocation
- **Commander Taeho:** Rolled Speed 6 -> 4 Action Points (AP).
- **Officer Joon:** Rolled Speed 4 -> 3 Action Points (AP).
- **Officer Seol-A:** Rolled Speed 5 -> 4 Action Points (AP).
- **Enforcer Min-Jae:** Rolled Speed 3 -> 2 Action Points (AP).
- **The Slag-Forged Breaker:** Rolled Speed 3 -> 3 Action Points (AP) (Queues *Demolition Hammer Slam* targeting `[N04]`).

#### 2. Node Maneuvers & Tactical Positioning
- Enforcer Min-Jae expends 2 AP to advance through `[N03]` to `[N04]`, passing Taeho and interlocking his basalt pavise at the frontline.
- Commander Taeho expends 1 AP to shift laterally behind Min-Jae's shield into `[N04]`, holding in ready stance (3 AP remaining).
- Officer Joon advances to `[N03]` (1 AP spent, 2 AP remaining).
- Officer Seol-A holds overwatch at `[N01]` (4 AP intact).

#### 3. Clash & Parry Resolutions
- **Clash 01 (Min-Jae vs Demolition Hammer Slam):**
  * Min-Jae queues *Cheol-Gyeong Bastion Anchor* (2 AP).
  * Min-Jae Roll: Speed 3 + Shield Power 22 = 25.
  * Breaker Roll: Speed 3 + Hammer Power 19 = 22.
  * Result: **Min-Jae Deflects (Margin +3)**. The massive pneumatic hammer smashes violently into the basalt pavise with a deafening ring. The shockwave is grounded directly into the tunnel floor. Construct suffers 8 Posture strain; attack neutralized.

#### 4. Modular Part Damage & Composure Tracking
- Officer Seol-A fires a high-velocity acoustic needle from `[N01]` targeting the Pneumatic Slag-Hammer Arm at `[N07]` (Distance = 6, Band 3 valid).
  * Damage Dealt: 40 * Lament Multiplier (1.0x) = 40 Damage.
  * Hammer Arm HP: 650 -> 610 / 650 (Rupture Threshold: 390 HP).
- Commander Taeho executes a rapid dashing thrust (2 AP) around Min-Jae's shield, striking the arm piston.
  * Damage Dealt: 55 * Grudge Multiplier (0.8x) = 44 Damage.
  * Hammer Arm HP: 610 -> 566 / 650.
- Breaker Composure: 200 / 200. Posture: 92 / 100.

---

### Battle Turn 02: Pincer Advance & Sulfur Vent Crisis

#### 1. Initiative & Action Point Allocation
- **Commander Taeho:** Rolled Speed 5 -> 4 AP.
- **Officer Joon:** Rolled Speed 5 -> 4 AP.
- **Officer Seol-A:** Rolled Speed 4 -> 3 AP.
- **Enforcer Min-Jae:** Rolled Speed 3 -> 2 AP.
- **The Slag-Forged Breaker:** Rolled Speed 4 -> 3 AP (Queues *Sulfur Slag Venting* targeting `[N04-05]` and *Hydraulic Rush*).

#### 2. Node Maneuvers & Tactical Positioning
- Recognizing the upcoming slag vent, Taeho expends 2 AP to sprint through `[N05]` and take flanking position at `[N06]`.
- Officer Joon charges forward from `[N03]` into `[N05]`, activating his hydraulic piston ram.
- Min-Jae remains at `[N04]`, bracing against the incoming hydraulic rush.
- With Taeho at `[N06]` and Joon at `[N05]`, **Pincer Advantage (+25% kinetic damage)** activates against Node `[N07]`.

#### 3. Clash & Hazard Resolution
- **Clash 02 (Min-Jae vs Hydraulic Rush):**
  * Min-Jae locks his pavise into the ground.
  * Min-Jae Roll: Speed 3 + Anchor 20 = 23.
  * Breaker Roll: Speed 4 + Rush 18 = 22.
  * Result: **Min-Jae Absorbs (Margin +1)**. The charging construct halts dead in its tracks at Node `[N05]`, unable to overcome Min-Jae's stance.
- **Pincer Strike on Hammer Arm:**
  * Joon executes *Hydraulic Piston Punch* (2 AP):
    - Base Damage: 65 * Weight (0.5x) * Pincer (1.25x) = 41 Damage.
  * Taeho executes *UCD Cleaver Slash* (2 AP):
    - Base Damage: 75 * Grudge (0.8x) * Pincer (1.25x) = 75 Damage!
  * Hammer Arm HP: 566 -> 450 / 650 (Rupture Threshold: 390 HP).

#### 4. Posture & Composure Tracking
- Slag venting at Node `[N06]` grazes Taeho for 12 burn damage (HP: 180 -> 168).
- Breaker Composure: 200 -> 180 / 200. Posture: 92 -> 68 / 100.

---

### Battle Turn 03: Part Rupture Threshold Breach (Hammer Arm Severed)

#### 1. Initiative & Action Point Allocation
- **Commander Taeho:** Rolled Speed 6 -> 4 AP.
- **Officer Joon:** Rolled Speed 4 -> 3 AP.
- **Officer Seol-A:** Rolled Speed 6 -> 4 AP.
- **Enforcer Min-Jae:** Rolled Speed 3 -> 2 AP.
- **The Slag-Forged Breaker:** Rolled Speed 3 -> 3 AP (Queues *Demolition Hammer Slam* targeting `[N05]`).

#### 2. Concentrated Arm Demolition
- Officer Seol-A activates *Acoustic Focus Rune*, granting +3 coin power to all allied attacks targeting Node `[N07]`.
- Taeho expends 3 AP to execute *Three-Point Kinetic Sunder*:
  * Strike 1: 32 Damage.
  * Strike 2: 35 Damage.
  * Strike 3: 40 Damage.
  * Total Damage: 107 Damage!
  * Hammer Arm HP: 450 -> 343 / 650 -> **RUPTURE THRESHOLD (390 HP) BREACHED!**

#### 3. Part Rupture Trigger & Effect
- **PART RUPTURE CONFIRMED:** The construct's right hydraulic line bursts in a shrieking cloud of steam; the heavy slag hammer drops to the stone floor with a thunderous crash!
- **Mechanical Penalties Inflicted on Construct:**
  * All Demolition Hammer skills permanently disabled!
  * Queued attack on Node `[N05]` cancelled!
  * Construct suffers **Tactical Stagger**; all incoming damage multiplied by **1.5x** for 1 turn!
  * Posture pool drops to 15 / 100.

---

### Battle Turn 04: Tactical Stagger Exploitation & Carapace Breach

#### 1. Initiative & Action Point Allocation
- **Commander Taeho:** Rolled Speed 5 -> 4 AP.
- **Officer Joon:** Rolled Speed 5 -> 4 AP.
- **Officer Seol-A:** Rolled Speed 5 -> 4 AP.
- **Enforcer Min-Jae:** Rolled Speed 4 -> 3 AP.
- **The Slag-Forged Breaker:** Staggered! (0 AP, Defense dice disabled).

#### 2. Synchronized Offensive Exploitation
- Exploiting the Stagger window, the squad shifts focus to shatter the Smelted Basalt Carapace protecting the contraband core:
- **Officer Joon (Node 05):** Spends 3 AP on *Maximum Overdrive Ram*:
  * Base Damage: 95 * Weight (0.7x) * Stagger Multiplier (1.5x) = 100 Damage!
  * Basalt Carapace HP: 1,100 -> 1,000 / 1,100.
- **Commander Taeho (Node 06):** Spends 3 AP on *Executioner Sunder*:
  * Base Damage: 110 * Void Edge (1.5x) * Stagger Multiplier (1.5x) = 248 Massive Damage!
  * Basalt Carapace HP: 1,000 -> 752 / 1,100 (Rupture Threshold: 660 HP).
- **Officer Seol-A (Node 01):** Fires Void needle into the cracked chest seam:
  * Damage Dealt: 50 * 1.5x * 1.5x = 112 Damage!
  * Basalt Carapace HP: 752 -> 640 / 1,100 -> **CARAPACE RUPTURED!**
- The heavy front plating shears off, exposing the glowing violet **Contraband Shroud Core** (`SECC-019`).
- Breaker Composure: 180 -> 95 / 200 (Severe cognitive feedback).

---

### Battle Turn 05: Contraband Core Meltdown (Terminal Collapse)

#### 1. Initiative & Action Point Allocation
- **Commander Taeho:** Rolled Speed 6 -> 4 AP.
- **Officer Joon:** Rolled Speed 4 -> 3 AP.
- **Officer Seol-A:** Rolled Speed 6 -> 4 AP.
- **Enforcer Min-Jae:** Rolled Speed 3 -> 2 AP.
- **The Slag-Forged Breaker:** Recovers from Stagger, rolls Speed 2 -> 2 AP (Fires desperate *Emergency Slag Vent*).

#### 2. The Final Cognitive Neutralization
- Min-Jae advances to `[N05]`, using his pavise to shield Joon and Taeho from the emergency slag spray.
- Officer Seol-A identifies the unstable sorrow frequency of the exposed core and channels *Mnemonic Resonance Drain* (3 AP):
  * Hit strikes directly into the pulsating sorrow crystal.
  * Shroud Core Damage: 80 * Void Multiplier (2.0x) = 160 True Damage!
  * Shroud Core HP: 400 -> 240 / 400 -> **CORE RUPTURED!**
  * Core Composure Drain: -120 Composure Points!
  * **COMPOSURE POOL HIT: 95 - 120 = 0 POINTS!**

#### 3. Terminal Meltdown Trigger
- **TERMINAL MELTDOWN ACTIVE:** The counterfeit sorrow core enters violent resonance cascade, causing the construct's basalt framework to seize up completely.
- All defenses drop to **2.0x Fatal vulnerability**!
- The construct collapses onto its knees, completely incapacitated at Nodes `[N07-08]`.

---

### Battle Turn 06: Synchronized Core Extraction & Vault Seizure

#### 1. Final Execution & Lockdown Maneuver
- **Officer Joon (Node 05):** Fires pneumatic restraint clamps into the construct's frame, pinning the chassis to the ground.
- **Commander Taeho (Node 06):** Uses specialized Directorate containment forceps to sever the core's resonant conduits:
  * The contraband sorrow core (`SECC-019`) is surgically detached and dropped into a lead-lined cryogenic transport capsule.
  * The remaining basalt construct becomes an inert pile of slag and scrap metal.
- **Officer Seol-A & Enforcer Min-Jae:** Breach the Vault Blast Door at Node `[N10]`, securing 14 illegal counterfeit Veil dies, 800 bootleg resonance visors, and 500 liters of unrefined sorrow fluid before the fleeing cartel operatives can ignite the scuttling charges.

---

## 5. Macro Phase-End Resolution Block (Phase 01 Complete)

""")

    # Phase-End Box
    b_phase = wrap_box("MACRO PHASE-END RESOLUTION SUMMARY — BATTLE 03", [
        "COMPLETED PHASE  : Combat Phase 01 (Battle Turns 01 to 06)",
        "CONSTRUCT STATUS : Slag-Hammer Ruptured (343 HP) • Carapace Ruptured",
        "CORE STATUS      : Contraband Shroud Core Neutralized & Extracted",
        "COMPOSURE POOL   : 0 / 200 (Terminal Meltdown Confirmed)",
        "FOUNDRY STATUS   : Vault Blast Door Breached • Counterfeit Dies Seized",
        "SQUAD CASUALTIES : 0 Fatalities • Commander Taeho (12 HP Slag Burn)"
    ])
    content.append(b_phase)

    content.append("""---

## 6. After-Action Report & Seizure Manifest

""")

    # After-Action Box
    b_aar = wrap_box("AFTER-ACTION TACTICAL REPORT & SEIZURE MANIFEST", [
        "ENGAGEMENT RESULT: Complete Tactical Victory & Sub-Sluice Pacification",
        "CONTRABAND SEIZED: 14 Steel Mask Dies • 820 Bootleg Veil Visors",
        "RAW MATERIAL YIELD: 520 Liters Raw Sorrow Sludge • 35 kg Basalt Scrap",
        "CORE RECOVERED   : 1x Grade-Beta Contraband Core (SECC-019 Shroud)",
        "CARTEL STATUS    : 8 Smugglers Captured • Forge Scuttling Prevented",
        "TACTICAL CITATION: Officer Joon & Enforcer Min-Jae for Anchor Defense"
    ])
    content.append(b_aar)

    content.append("""---
*End of Canonical Tactical Scenario SOP-GB-SCENARIO-003.*
""")
    
    return "".join(content)

if __name__ == "__main__":
    scenario_text = build_scenario()
    target_path = "GAME_BATTLE/SCENARIO_03_UNDERWORLD_RUST_VEIL_PURGE.md"
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(scenario_text)
    print(f"Successfully wrote {len(scenario_text)} bytes to {target_path}")
