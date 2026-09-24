#!/usr/bin/env python3
"""
Generate GAME_BATTLE/BATTLE_SCENARIO_TEMPLATE.md.
Transforms the template into a fully fleshed-out Canonical Reference Scenario Specification:
- Zero placeholder brackets ([Insert ...], [Document Turn ...], etc.).
- Concrete in-universe Somnarak lore, names, and stats.
- Zero Korean Hangul in text boxes (Korean Alphabet Romanization only).
- Korean two-space buffer outside text boxes.
- Zero P.M. crossover vocabulary.
- 71-col ASCII text box symmetry.
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import tools.box_formatter as bf

OUTPUT_PATH = "GAME_BATTLE/BATTLE_SCENARIO_TEMPLATE.md"

def wrap_box(box_text):
    return "```text\n" + box_text + "\n```\n\n"

def build_scenario_template():
    lines = []
    
    # Master Header
    lines.append("# BATTLE SCENARIO SPECIFICATION — Standardized Tactical Engagement Format")
    lines.append("## Canonical Battle Model: Operation Sub-Basalt Anchor & Breach Containment")
    lines.append("### Reference Scenario Specification — SOP-GB-SPEC-001\n")
    
    # Master HUD Box (Strictly English / Romanized Alphabet only - zero Hangul!)
    hud_rows = [
        "TACTICAL ENGAGEMENT RECORD: BATTLE-SPEC-001-SUB-BASALT",
        "OPERATIONAL AREA  : Zone B Sub-Basalt Strata, Facility 01 Perimeter",
        "DEPTH COORDINATE  : Depth -450m Subterranean Bastion Trench",
        "THREAT RATING     : Rank IV (Grade Delta Potency)",
        "STRIKE TEAM       : Strike Team Delta (Reverie Directorate Security)",
        "SQUAD STRENGTH    : 4 Operatives (Min-Jae, Taeho, Seol-A, Jinho)",
        "PRIMARY OBJECTIVE : Breach Containment & Acoustic Gate Resealing",
        "ENGAGEMENT STATUS : Standardized Operational Battle Specification"
    ]
    lines.append(wrap_box(bf.make_box("REVERIE DIRECTORATE TACTICAL ENGAGEMENT RECORD", hud_rows, width=71)))
    
    # Section 1
    lines.append("## 1. Tactical Overview & Operational Parameters\n")
    sec1 = """- **Topological Coordinate:** Zone B Maw Perimeter, Depth -450m Sub-Basalt Strata.
- **Ambient Han Saturation:** 35% Ambient Weeping Density (14.2 mMb).
- **Environmental Hazard Modifiers:**
  * **Acoustic Echo Reverberation:** Vault resonance amplifies psychic shrieks. Units failing a defensive clash suffer +10% Lament (  비탄  / Bitan [Lament]) strain.
  * **Collapsed Basalt Rubble:** Seismic shifts have shattered the flooring; Nodes `[N04]` and `[N05]` require 2 Action Points (AP) to traverse instead of 1 AP.
- **Mission Briefing:**
  At 03:40 hours, automated acoustic sensors at Containment Perimeter B-04 registered a severe pressure spike following the destabilization of **The Shattered Clockwork (  부서진 시계  / Buseojin Sigye [The Shattered Clockwork] • `SE-C-IVγ-044`)**. Strike Team Delta was deployed via Sub-Sump Transit Rail to re-establish the secondary containment perimeter, suppress the entity's kinetic pendulum strikes, shatter its primary balance gears, and enforce lock-down before the weeping mist reaches civilian ventilation shafts.
"""
    lines.append(sec1.strip() + "\n\n---\n")
    
    # Section 2
    lines.append("## 2. Combatant Rosters & Technical Profiles\n")
    lines.append("### 2.1 Allied Strike Team Delta (4 Operatives)\n\n")
    
    roster_table = """| Operative Callsign | Tactical Role | Base Spd | Max HP | Composure | Posture | Equipped M.A.W. Set | Range Band |
|---|---|---|---|---|---|---|---|
| **Warden Min-Jae** | Citadel Vanguard | 5 | 160 | 100 | 120 | Tectonic Bulwark (Grade γ) | Band 1 (Melee) |
| **Vanguard Taeho** | Kinetic Striker | 4 | 140 | 90 | 100 | Ancestral Signet (Grade γ) | Band 2 (Short) |
| **Specialist Seol-A**| Acoustic Flanker | 4 | 120 | 110 | 80 | Silenced Requiem (Grade β) | Band 3 (Medium) |
| **Tech Jinho** | Sensor Anchor | 3 | 110 | 100 | 90 | Calibrated Dampener (Grade γ)| Band 4 (Long) |
"""
    lines.append(roster_table.strip() + "\n\n")
    
    lines.append("### 2.2 Hostile Entity: The Shattered Clockwork (`SE-C-IVγ-044`)\n")
    boss_info = """- **Coherence Rank & Potency:** Rank IV Fragment • Grade Gamma (γ) Potency
- **Total Composure Pool:** 250 Points • Meltdown Threshold: 0 Points
- **Base Speed:** 4 (Generates 3 Action Points per turn)
- **Modular Body Part Anatomy:**

| Modular Part Name | Part Max HP | Rupture Threshold (60%) | Lament Def | Grudge Def | Void Def | Weight Def |
|---|---|---|---|---|---|---|
| **Brass Dial Face** | 500 HP | 300 HP | 0.8x | 1.0x | 1.2x | 0.5x |
| **Escapement Core** | 800 HP | 480 HP | 1.0x | 0.7x | 1.0x | 0.4x |
| **Pendulum Arm** | 400 HP | 240 HP | 1.2x | 1.2x | 0.8x | 1.0x |

- **Hostile Intention Deck:**
  * **Chime of Despair (Basic Attack):** 2 AP • Target Band 1-3 • Element: Lament • Base Power 14.
  * **Pendulum Cleave (Heavy Strike):** 3 AP • Target Band 1-2 • Element: Weight • Base Power 24.
  * **Temporal Whir (Buff/Disrupt):** 1 AP • Self/Area • Accelerates entity Speed by +2 for next turn.
"""
    lines.append(boss_info.strip() + "\n\n---\n")
    
    # Section 3
    lines.append("## 3. Initial 10-Node Grid Topography Map\n\n")
    grid_rows = [
        "INITIAL 10-NODE GRID TOPOGRAPHY: ZONE B TACTICAL CORRIDOR",
        "[N01]   [N02]   [N03]   [N04]   [N05]   [N06]   [N07]   [N08]   [N09]   [N10]",
        "[Jinho] [Seol-A] [Taeho] [Min-Jae] [COVER] -----   [ENTITY BODY]   -----   -----",
        "Allied Deployment [N01-03] | Center [N04-06] | Hostile Presence [N07-08]"
    ]
    lines.append(wrap_box(bf.make_box("SPATIAL GRID TOPOGRAPHY", grid_rows, width=71)))
    
    sec3_notes = """- **Allied Starting Nodes:** Tech Jinho at `[N01]`, Specialist Seol-A at `[N02]`, Vanguard Taeho at `[N03]`, Warden Min-Jae at `[N04]`.
- **Environmental Markers:** Basalt Bulkhead / Destructible Kinetic Cover located at `[N05]`.
- **Hostile Position:** The Shattered Clockwork occupies `[N07]` and `[N08]`.
"""
    lines.append(sec3_notes.strip() + "\n\n---\n")
    
    # Section 4
    lines.append("## 4. Turn-by-Turn Operational Chronicle\n\n")
    
    # Turn 1
    t1 = """### Battle Turn 01: Initial Advance & Reconnaissance Clashes

#### 1. Initiative & Action Point Allocation
- **Warden Min-Jae:** Speed 5 -> 4 Action Points (AP).
- **Vanguard Taeho:** Speed 4 -> 3 Action Points (AP).
- **Specialist Seol-A:** Speed 4 -> 3 Action Points (AP).
- **Tech Jinho:** Speed 3 -> 2 Action Points (AP).
- **The Shattered Clockwork:** Speed 3 -> 3 Action Points (AP).

#### 2. Node Maneuvers & Tactical Positioning
- Min-Jae advances from `[N04]` to `[N05]`, taking cover behind the basalt bulkhead (2 AP spent due to rubble hazard, 2 AP remaining).
- Taeho advances from `[N03]` to `[N04]` (1 AP spent, 2 AP remaining).
- Seol-A and Jinho hold positions at `[N02]` and `[N01]`.

#### 3. Clash & Parry Resolutions
- **Clash 01:** Min-Jae queues [Defensive Bulwark Parry] vs Hostile [Chime of Despair] targeting `[N05]`.
  * Min-Jae Roll: Speed 5 + Shield Power 12 = 17.
  * Hostile Roll: Speed 3 + Attack Power 11 = 14.
  * Result: **Min-Jae Deflects (Margin +3)**. Hostile suffers 6 direct Posture strain; attack canceled.

#### 4. Modular Part Damage & Composure Tracking
- Jinho fires calibrated acoustic bolt from `[N01]` targeting the Pendulum Arm at `[N07]` (Distance = 6, Band 4 valid).
  * Damage Dealt: 45 Grudge (  원한  / Wonhan [Grudge]) Damage.
  * Pendulum Arm HP: 400 -> 355 / 400 (Rupture Threshold: 240 HP).
- Hostile Composure: Holds at 250 / 250.
"""
    lines.append(t1.strip() + "\n\n---\n")
    
    # Turn 2
    t2 = """### Battle Turn 02: Pressure Escalation & Flank Maneuvers

#### 1. Initiative & Action Point Allocation
- **Min-Jae:** Speed 4 -> 3 AP.
- **Taeho:** Speed 5 -> 4 AP.
- **Seol-A:** Speed 6 -> 4 AP.
- **Jinho:** Speed 4 -> 3 AP.
- **Hostile:** Speed 4 -> 3 AP.

#### 2. Node Maneuvers & Tactical Positioning
- Seol-A uses 2 AP to sprint from `[N02]` through `[N03]` to `[N06]`, establishing an acoustic flank on the entity's left flank.
- Taeho advances from `[N04]` to `[N05]` behind Min-Jae's shield barrier (2 AP spent).
- Min-Jae holds firm at `[N05]` (3 AP held for reactionary parries).

#### 3. Clash & Parry Resolutions
- **Clash 02:** Min-Jae parries [Pendulum Cleave] aimed at `[N05]`.
  * Min-Jae Roll: Speed 4 + Bulwark 18 = 22.
  * Hostile Roll: Speed 4 + Cleave 19 = 23.
  * Result: **Hostile Slight Edge (Margin -1)**. Min-Jae absorbs 14 Weight damage into armor; Posture holds at 106/120.

#### 4. Modular Part Damage & Composure Tracking
- Seol-A unleashes [Silenced Requiem Thrust] from `[N06]` into the Pendulum Arm joint.
  * Damage Dealt: 65 Lament damage.
  * Pendulum Arm HP: 355 -> 290 / 400 (Rupture Threshold: 240 HP).
- Hostile Composure: Decreases from 250 -> 230 / 250.
"""
    lines.append(t2.strip() + "\n\n---\n")
    
    # Turn 3
    t3 = """### Battle Turn 03: Part Rupture Threshold Breach

#### 1. Initiative & Action Point Allocation
- **Min-Jae:** Speed 5 -> 4 AP.
- **Taeho:** Speed 5 -> 4 AP.
- **Seol-A:** Speed 5 -> 4 AP.
- **Jinho:** Speed 3 -> 2 AP.
- **Hostile:** Speed 3 -> 3 AP.

#### 2. Node Maneuvers & Tactical Positioning
- Taeho charges from `[N05]` into melee range at `[N06]`, preparing a heavy kinetic sunder strike.
- Min-Jae advances to `[N06]` to cover Taeho's left flank.
- Jinho maintains long-range tracking at `[N01]`.

#### 3. Clash & Parry Resolutions
- **Clash 03:** Taeho executes [Ancestral Signet Slam] vs Hostile [Chime of Despair].
  * Taeho Roll: Speed 5 + Sunder 20 = 25.
  * Hostile Roll: Speed 3 + Chime 14 = 17.
  * Result: **Taeho Overwhelms (Margin +8)**. Critical kinetic impact shatters the outer casing.

#### 4. Modular Part Damage & Part Rupture Trigger
- Taeho's strike connects squarely with the Pendulum Arm at `[N07]`.
  * Damage Dealt: 85 Grudge damage.
  * Pendulum Arm HP: 290 -> 205 / 400 (**CROSSES BELOW 240 HP RUPTURE THRESHOLD!**).
  * **PART RUPTURE EVENT:** The Pendulum Arm snaps its primary axle. Pendulum Cleave is permanently disabled. Entity suffers 30 immediate Posture loss.
- Hostile Composure: Drops from 230 -> 160 / 250.
"""
    lines.append(t3.strip() + "\n\n---\n")
    
    # Turn 4
    t4 = """### Battle Turn 04: Tactical Stagger Exploitation

#### 1. Initiative & Action Point Allocation
- **Min-Jae:** Speed 4 -> 3 AP.
- **Taeho:** Speed 4 -> 3 AP.
- **Seol-A:** Speed 7 -> 5 AP.
- **Jinho:** Speed 4 -> 3 AP.
- **Hostile:** Speed 2 (Staggered by ruptured gear) -> 2 AP.

#### 2. Node Maneuvers & Tactical Positioning
- Squad establishes a 3-way pincer: Min-Jae and Taeho at `[N06]`, Seol-A at `[N07]`, Jinho at `[N02]`.

#### 3. Clash & Parry Resolutions
- Hostile attempts emergency [Temporal Whir] to accelerate gear rotation.
- Jinho discharges [Harmonic Dampener Pulse] from `[N02]`, canceling the spin acceleration.

#### 4. Modular Part Damage & Composure Tracking
- Seol-A exploits the ruptured Pendulum Arm with [Siphon Lunge] (1.5x Rupture Vulnerability Multiplier).
  * Base Damage: 50 -> Modified Damage: 75 Void (  공허  / Gongheo [Void]) damage.
  * Pendulum Arm HP: 205 -> 130 / 400.
- Min-Jae strikes Escapement Core with heavy shield bash dealing 40 Weight damage.
  * Escapement Core HP: 800 -> 760 / 800.
- Hostile Composure: Drops sharply from 160 -> 75 / 250.
"""
    lines.append(t4.strip() + "\n\n---\n")
    
    # Turn 5
    t5 = """### Battle Turn 05: Composure Meltdown Breach

#### 1. Initiative & Action Point Allocation
- **Min-Jae:** Speed 4 -> 3 AP.
- **Taeho:** Speed 6 -> 4 AP.
- **Seol-A:** Speed 6 -> 4 AP.
- **Jinho:** Speed 4 -> 3 AP.
- **Hostile:** Speed 2 -> 2 AP.

#### 2. Node Maneuvers & Tactical Positioning
- Taeho and Min-Jae step directly into `[N07]`, enclosing the entity's central dial.

#### 3. Clash & Parry Resolutions
- Hostile unleashes desperate, uncoordinated gear grinding.
- Taeho parries effortlessly: Speed 6 + Signet 18 = 24 vs Hostile 12. Complete deflection.

#### 4. Composure Meltdown Event
- Min-Jae and Taeho execute a coordinated dual hammer strike against the Escapement Core.
  * Total Damage: 110 physical damage.
  * Escapement Core HP: 760 -> 650 / 800.
  * **COMPOSURE MELTDOWN TRIGGER:** Hostile Composure pool reaches exactly 0 / 250!
  * **TERMINAL MELTDOWN ACTIVE:** All entity body parts take 2.0x vulnerability damage for the next turn. Entity cannot execute offensive skills.
"""
    lines.append(t5.strip() + "\n\n---\n")
    
    # Turn 6
    t6 = """### Battle Turn 06: Phase Climax & Synchronized Execution

#### 1. Initiative & Action Point Allocation
- **Min-Jae:** Speed 5 -> 4 AP.
- **Taeho:** Speed 5 -> 4 AP.
- **Seol-A:** Speed 7 -> 5 AP.
- **Jinho:** Speed 5 -> 4 AP.
- **Hostile:** Speed 0 (Meltdown Incapacitated) -> 0 AP.

#### 2. Node Maneuvers & Tactical Positioning
- Full squad concentrates at `[N07]` and `[N08]` around the collapsed construct.

#### 3. Coordinated Execution Strikes (2.0x Meltdown Bonus)
- Jinho pins the core with an anchor bolt dealing 80 damage (40 base x 2.0x).
- Seol-A severs the sensory chimes with [Requiem Finisher] dealing 160 damage (80 base x 2.0x).
- Taeho unleashes [Maximum Sunder] directly into the Escapement Core dealing 280 damage (140 base x 2.0x).
  * Escapement Core HP: 650 -> 130 / 800.
- Min-Jae plants the containment seal atop the Brass Dial Face, dealing 90 Weight damage and cementing the magnetic lock.
  * Brass Dial Face HP: 500 -> 410 / 500.
  * Entity reaches complete pacification threshold. Containment shroud deployed!
"""
    lines.append(t6.strip() + "\n\n---\n")
    
    # Section 5
    lines.append("## 5. Macro Phase-End Resolution Block (Phase 01 Complete)\n\n")
    res_rows = [
        "MACRO PHASE-END RESOLUTION SUMMARY: BATTLE-SPEC-001",
        "COMPLETED PHASE   : Combat Phase 01 (Battle Turns 01 to 06)",
        "SORROW TIDE TICK  : Ambient Han Saturation increased 35% -> 45%",
        "PART STATUS       : Pendulum Arm Ruptured • Core Compromised",
        "HOSTILE COMPOSURE : Terminal Meltdown Enforced (0 / 250)",
        "SQUAD STATUS      : All 4 Operatives Combat-Ready (0 Casualties)",
        "CONTAINMENT LOCK  : Level 4 Magnetic Stasis Shroud Deployed"
    ]
    lines.append(wrap_box(bf.make_box("MACRO PHASE-END RESOLUTION", res_rows, width=71)))
    
    sec5_text = """- **Sorrow Tide Escalation:** Ambient weeping vapor rises (+10% ambient saturation), but secondary venting seals prevent containment corridor contamination.
- **Status Ticks:** Minor thermal and acoustic strains resolve through squad filtration respirators.
- **Encounter Result:** The Shattered Clockwork is fully pacified and re-anchored to Facility 01 containment rails.
"""
    lines.append(sec5_text.strip() + "\n\n---\n")
    
    # Section 6
    lines.append("## 6. After-Action Report & Extraction Manifest\n\n")
    aar_rows = [
        "AFTER-ACTION TACTICAL REPORT & EXTRACTION MANIFEST",
        "ENGAGEMENT RESULT : Decisive Containment Victory",
        "HARVEST RECOVERED : 420 kg Refined Liquid Han / 85 kg Han Dust",
        "M.A.W. EXTRACTED  : 1x Weapon Core (Grade Gamma) - Clockwork Maul",
        "SQUAD CASUALTIES  : Zero Fatalities - Min-Jae Minor Armor Strain",
        "DEBRIEF STATUS    : Cleared for Return to Central Sector Garrison"
    ]
    lines.append(wrap_box(bf.make_box("AFTER-ACTION REPORT", aar_rows, width=71)))
    
    sec6_text = """- **Tactical Evaluation:** Flawless 10-node spatial coordination. Min-Jae's vanguard shield absorb at Node 5 enabled Seol-A and Taeho to flank and breach the Pendulum Arm rupture threshold by Turn 3.
- **Quarantine & Recovery:** Strike Team Delta operatives completed 30-minute psychic filtration in Floor 01 decompression chambers with 100% Composure restored.

---

**Specification Classification:** `SOMNARAK-GBS-SPEC-001`  
**Supervising Authority:** Reverie Directorate Tactical Simulation Bureau
"""
    lines.append(sec6_text.strip())
    
    content = "\n".join(lines)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Wrote {OUTPUT_PATH} ({len(content)} bytes)")

if __name__ == "__main__":
    build_scenario_template()
