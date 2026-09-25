#!/usr/bin/env python3
"""
tools/expand_katharcheok_op2.py
Expands Operation 2 (Lethepyo - The Bleached Wards) in SOMNARAK-WORLD/Katharcheok/Operation_2_Lethepyo.md
Replaces the older summary/compressed boxes in ### Tactical Engagement: 6-Turn Pacification Gauntlet
with full 10-node spatial tactical HUDs, Speed/AP breakdowns, M.A.W.-W weight deltas,
and Four P-framework action resolution logs across all 6 turns.
"""

import sys, os
sys.path.append(os.path.dirname(__file__))
from box_formatter import make_box

def get_op2_engagement():
    dossier_box = make_box("TARGET DOSSIER: CHIEF CHEMIST SURA & LETHE MIASMA CORE", [
        "APEX TARGET        : Chief Chemist Sura ('The Memory Bleacher')",
        "MODULAR WEAPON     : Chemical Distillation Sprayer (Pressurized Acid)",
        "CONTRABAND ENTITY  : SE-C-IIIγ-928 'Lethe Miasma Core' (Rank III)",
        "ESCORT MINIONS     : Chemical Enforcers (x2) & Solvent Technicians",
        "ENCOUNTER DOMAIN   : Zone B+C Sub-Drainage Conduits (-75m Depth)",
        "---",
        "BOSS COMBAT PROFILE (CHIEF CHEMIST SURA):",
        "- Exoskeleton HP   : 2,000 HP | Body HP: 2,000 HP (Total 4,000 HP)",
        "- Sprayer Arm HP   : 1,400 HP (Modular Destructible Weapon Part)",
        "- Posture Pool     : 220/220 (Dual Threshold Stagger System)",
        "- Stagger 1 Proc   : 60% Posture Strain (132 Posture) / Sprayer Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Terminal Stagger / Cryo-Seal)",
        "- Primary Attack   : Pressurized Pale Spray & Solvent Scalpel (Pale/Acid)",
        "---",
        "CONTRABAND ENTITY PROFILE (SE-C-IIIγ-928 'LETHE'):",
        "- Entity HP Pool   : 2,800 HP | Posture Pool: 200/200",
        "- Total Combined   : 6,200 Encounter HP",
        "- Attack Affinity  : Tidal Amnesia & Pale Oblivion Surge (Mind Drain)"
    ])

    hud_t01 = make_box("TACTICAL STAGE HUD: OPERATION 02 — BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 — ZONE B+C SUB-DRAINAGE LETHE VAULT]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER][TAEHO] [JOON]  [SOOJIN][SURA]   [YUNA]  [MINHO] [CIVS]          [LETHE] ",
        "                                 [SPRAY]                          [ECHO]  ",
        "---",
        "- Node 01: Breach Entry / Class-II Armored Cruiser 'The Iron Vanguard'",
        "- Node 02: Commander Taeho (Vanguard Band 1 / Phalanx Bastion Obsidian)",
        "- Node 03: Engineer Joon (Point-Blank Band 1 / Deployable Mantlet Barrier)",
        "- Node 04: Handler Soojin (Close Skirmish Band 2 / Aerosol Neutralizer)",
        "- Node 05: Chief Chemist Sura & Distillation Sprayer (Central Platform)",
        "- Node 06: Auditor Yuna (Mid-Field Band 3 / Cipher-Scan Frequency Rig)",
        "- Node 07: Investigator Minho (Mid-Field Band 3 / Neural Lancet Sniper)",
        "- Node 08: Extraction Berths (18 Amnesiac Captive Citizens)",
        "- Node 10: SE-C-IIIγ-928 Lethe Miasma & Infiltrator Echo (Catwalk Stealth)",
        "---",
        "- Taeho       : Spd 4 -> 2 AP | HP 4,400/4,400 | SP 45/50 | Posture 180/180",
        "- Joon        : Spd 5 -> 3 AP | HP 3,800/3,800 | SP 40/40 | Posture 150/150",
        "- Yuna        : Spd 7 -> 4 AP | HP 2,700/2,700 | SP 50/50 | Posture 100/100",
        "- Minho       : Spd 7 -> 4 AP | HP 2,900/2,900 | SP 45/45 | Posture 110/110",
        "- Soojin      : Spd 5 -> 3 AP | HP 3,600/3,600 | SP 50/50 | Posture 140/140",
        "- Echo        : Spd 9 -> 5 AP | HP 2,600/2,600 | SP 40/40 | Posture 90/90 [STEALTH]",
        "- Sura Chassis: Spd 4 -> 2 AP | HP 2,000/2,000 | Posture 220/220 [SEALED]",
        "- Sprayer Arm : Spd 3 -> 1 AP | HP 1,400/1,400 | Posture 120/120 [PRIMED]",
        "- Lethe Core  : Spd 5 -> 3 AP | HP 2,800/2,800 | Posture 200/200 [CAGED]"
    ])

    hud_t02 = make_box("TACTICAL STAGE HUD: OPERATION 02 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — SPRAYER SAPPING & FREQUENCY SCRAMBLE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER][TAEHO] [JOON]  [SOOJIN][SURA]   [YUNA]  [MINHO] [CIVS]  [ECHO]  [LETHE] ",
        "                                 [SPRAY]                                  ",
        "---",
        "- Node 02: Commander Taeho (Advancing to Node 03 / Concussive Shield Bash)",
        "- Node 03: Engineer Joon (Hydraulic Kinetic Ram Smashes Vapor Manifold)",
        "- Node 04: Handler Soojin (Resonance Snare Restricting Amnesiac Vapors)",
        "- Node 05: Chief Chemist Sura (Exoskeleton 1,370/2,000 / Sprayer 920/1,400)",
        "- Node 06: Auditor Yuna (Cipher-Pulse Destabilizing Sura's Servos)",
        "- Node 07: Investigator Minho (Memory Anchor Restoring Squad Composure)",
        "- Node 09: Infiltrator Echo (Overhead Feeder Severed / 300L Acid Vented)",
        "- Node 10: Lethe Miasma Core (Vapor Agitation Rising / 2,550/2,800 HP)",
        "---",
        "- Joon        : Spd 7 -> 4 AP [SURGE] | HP 3,800/3,800 | SP 40/40 | Posture 150/150",
        "- Minho       : Spd 9 -> 5 AP [SURGE] | HP 2,900/2,900 | SP 50/50 | Posture 110/110",
        "- Sura Chassis: Spd 3 -> 1 AP | HP 1,370/2,000 | Posture 162/220 [DESTABILIZED]",
        "- Sprayer Arm : Spd 2 -> 1 AP | HP 920/1,400   | Posture 64/120 [CRACKED]",
        "- Lethe Core  : Spd 4 -> 2 AP | HP 2,550/2,800 | Posture 178/200 [RESTRICTED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: OPERATION 02 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — SPRAYER DESTROYED & STAGGER THRESHOLD 1]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER]        [TAEHO] [JOON]  [SURA]   [YUNA]  [MINHO] [CIVS]  [ECHO]  [LETHE] ",
        "---",
        "- Node 03: Commander Taeho (Heavy Piston Strike Smashes Chest Plate)",
        "- Node 04: Engineer Joon (Thermite Disruption Clamp Igniting Battery)",
        "- Node 05: Chief Chemist Sura (STAGGER LEVEL 1 / SPRAYER DESTROYED)",
        "- Node 06: Auditor Yuna (Downloading Memory Ledger Coordinates)",
        "- Node 07: Investigator Minho (Synaptic Pierce Dismantles Sprayer Valve)",
        "- Node 09: Infiltrator Echo (Driving Eclipse Stiletto into Servo Joints)",
        "- Node 10: Lethe Miasma Core (Pressurized Containment Trembling)",
        "---",
        "- Taeho       : Spd 6 -> 3 AP [SURGE] | HP 4,400/4,400 | SP 48/50 | Posture 180/180",
        "- Sura Chassis: Spd 0 -> 0 AP | HP 290/2,000   | Posture 74/220 [STAGGER LEVEL 1]",
        "- Sprayer Arm : DESTROYED (0/1,400 HP)",
        "- Lethe Core  : Spd 5 -> 3 AP | HP 2,550/2,800 | Posture 178/200"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: OPERATION 02 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — BERSERK LETHE & LEADED SANCTUARY WARD]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER]        [TAEHO] [JOON]  [SURA]   [SOOJIN][YUNA]  [CIVS]  [ECHO]  [LETHE] ",
        "                                                  [MINHO]                 ",
        "---",
        "- Node 03: Commander Taeho (Shielding Civilian Extraction Berths)",
        "- Node 04: Engineer Joon (Pneumatic Pry Bar Unjamming Hostage Restraints)",
        "- Node 05: Chief Chemist Sura (Recovered / Pulling Emergency Purge Lever)",
        "- Node 06: Handler Soojin (Leaded Sanctuary Damping Field Active)",
        "- Node 07: Auditor Yuna & Minho (Hacking Sluice Ventilation / Vapors Purged)",
        "- Node 08: 18 Civilian Captives (Cognitive Shields Holding Intact)",
        "- Node 10: SE-C-IIIγ-928 Lethe (BERSERK STATE / Tidal Amnesia Surge)",
        "---",
        "- Soojin      : Spd 7 -> 4 AP [SURGE] | HP 3,600/3,600 | SP 50/50 | Posture 140/140",
        "- Sura Chassis: Spd 2 -> 1 AP | HP 290/2,000   | Posture 52/220",
        "- Lethe Core  : Spd 6 -> 4 AP | HP 2,100/2,800 | Posture 112/200 [BERSERK]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: OPERATION 02 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — PHANTOM SEVER & TERMINAL STAGGER]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER]        [TAEHO] [JOON]  [SURA]   [SOOJIN][YUNA]  [CIVS]          [LETHE] ",
        "                                                  [MINHO]         [ECHO]  ",
        "---",
        "- Node 03: Commander Taeho (Priming Iron Gavel for Cockpit Breach)",
        "- Node 04: Engineer Joon (Tearing Away Buckled Leg Supports on Sura)",
        "- Node 05: Sura Exoskeleton (TERMINAL STAGGER / POSTURE 0/220 / CRUSHED)",
        "- Node 06: Handler Soojin (Aligning Class-IV Leaded Cryo-Cask at Funnel)",
        "- Node 07: Investigator Minho (Silver Lancet Stripping Cognitive Anchor)",
        "- Node 09: Infiltrator Echo (Eclipse Stiletto Phantom Sever on Core)",
        "- Node 10: SE-C-IIIγ-928 Lethe (TERMINAL STAGGER / POSTURE 0/200 / COLLAPSED)",
        "---",
        "- Echo        : Spd 11 -> 5 AP [MOMENTUM CRIT] | HP 2,600/2,600 | SP 40/40",
        "- Sura Chassis: Spd 0 -> 0 AP | HP 0/2,000     | Posture 0/220 [CHASSIS CRUSHED]",
        "- Lethe Core  : Spd 0 -> 0 AP | HP 1,110/2,800 | Posture 0/200 [TERMINAL STAGGER]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: OPERATION 02 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX OVERDRIVE: IRON GAVEL & CRYO-SEAL]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER]                [JOON]  [TAEHO]  [SOOJIN][YUNA]  [CIVS]          [CASK]  ",
        "                                 [SURA]           [MINHO]         [ECHO]  ",
        "---",
        "- Node 05: Chief Chemist Sura (EXTRACTED UNCONSCIOUS & SECURED)",
        "- Node 06: Auditor Yuna (4,216 Memory Crystals Secured & Encrypted)",
        "- Node 08: 18 Civilian Captives (Safely Unlatched / Zero Loss)",
        "- Node 10: SE-C-IIIγ-928 Lethe (100% CONTAINED IN CRYOGENIC VACUUM CASK)",
        "---",
        "- Strike Cadre: Zero Fatalities | Composure 50/50 SP (Lucidity)",
        "- Encounter Status: 100% PACIFIED | Handoff to RD Floor 2 Ready"
    ])

    return f"""### Tactical Engagement: 6-Turn Pacification Gauntlet

```text
{dossier_box}
```

---

```text
{hud_t01}
```

###### Turn 01 Action Resolution Log (Kinetic Ingress & Aerosol Neutralization)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Commander Taeho initializes `[Law of the Mantle]`: All allies within 1 node gain +3 Protection and physical stagger immunity.
  * Infiltrator Echo activates `[Shadow Cloak]`: Enters stealth for 2 turns; cannot be targeted by single-target attacks; +50\% Critical Strike Chance.
  * Handler Soojin initializes `[Aerosol Neutralization Ward]`, deploying an active chemical filter around Nodes 02–04.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Commander Taeho (Speed 4 -> 2 AP, M.A.W.-W Heavy Armor delta -1, Poise +25): Holds Node 02. Spends 2 AP on `[Phalanx Bastion: Obsidian Wall]`.
  * Engineer Joon (Speed 5 -> 3 AP, M.A.W.-W Medium delta 0): Holds Node 03. Spends 2 AP on `[Deployable Mantlet Barrier]`. Holds 1 AP in Reserve.
  * Auditor Yuna (Speed 7 -> 4 AP, M.A.W.-W Light delta +1): Holds Node 06 (Range Band 3). Spends 2 AP on `[Cipher-Scan: Chemical Frequencies]`, 2 AP on `[Asset Scan]`.
  * Investigator Minho (Speed 7 -> 4 AP, M.A.W.-W Light delta +1): Stands at Node 07. Spends 2 AP on `[Neural Lancet: Calibrated Dart]`. Holds 2 AP in Reserve.
  * Handler Soojin (Speed 5 -> 3 AP, M.A.W.-W Medium delta 0): Holds Node 04. Spends 2 AP on maintaining the neutralization ward. Holds 1 AP in Guard.
  * Infiltrator Echo (Speed 9 -> 5 AP, M.A.W.-W Feather delta +2): Advances through overhead drainage catwalks to Node 10 from stealth. Spends 2 AP on positioning.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 02 to 05)**: Chief Chemist Sura unleashes `[Pressurized Pale Spray]` (Base 13 + 2 Coins = 25 Power, Corrosive) against Node 02.
    * Commander Taeho counters with `[Phalanx Bastion: Obsidian Wall]` (Base 15 + 2 Coins = 29 Power, Kinetic Shield).
    * **Clash Outcome**: Taeho WINS THE CLASH (29 vs 25)!
    * The kinetic force field disperses the toxic chemical stream without a drop breaching the shield (`[P3: Parry/Protection]`).
    * Taeho reflects **150 kinetic tremor damage** back into Sura's heavy hazmat exoskeleton! Inflicts +26 Posture Strain.
  * **Clash 2 (Node 03 to 05)**: Chemical Enforcers attempt `[Solvent Syringe Thrust]` (Atk Power 19, Pierce).
    * Engineer Joon's `[Deployable Mantlet Barrier]` (Def Power 23, Kinetic Shield).
    * **Clash Outcome**: Joon WINS THE CLASH (23 vs 19).
    * Syringes shatter against the reinforced titanium mantlet; zero damage taken.
  * **Unopposed Ranged Fire**:
    * Auditor Yuna's `[Cipher-Scan]` identifies the high-pressure feeder joints of the Distillation Sprayer arm.
    * Investigator Minho fires `[Neural Lancet: Calibrated Dart]` from Node 07 into Sura's hydraulic actuator, dealing **220 Pierce damage** and +22 Posture Strain!
    * Handler Soojin's aerosol ward completely nullifies ambient amnesiac fumes around the squad.
- **Step 4: Turn End State**:
  * Sura Hazmat Exoskeleton HP: 2,000 -> **1,630/2,000** (Combined Encounter HP: **5,830/6,200**).
  * Sura Posture: 220 -> **172/220**.
  * Squad Composure: **100% (50/50 SP)**. All 6 Officers uninjured.

---

```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Sprayer Sapping & Frequency Scramble)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Engineer Joon and Investigator Minho both trigger `Momentum Surge` (+2 Speed next turn).
  * Sura's Chemical Distillation Sprayer begins high-pressure pre-ignition.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Engineer Joon (Speed 7 -> 4 AP): Advances from Node 03 to Node 04. Spends 3 AP to unleash `[Hydraulic Kinetic Ram: Structural Sapping]`.
  * Auditor Yuna (Speed 7 -> 4 AP): Moves to Node 06, deploying `[Cipher-Pulse: Resonance Intercept]` (2 AP) against Sura's servo motors.
  * Commander Taeho (Speed 4 -> 2 AP): Steps to Node 03, executing `[Shield Bash: Concussive Drive]` (2 AP).
  * Investigator Minho (Speed 9 -> 5 AP): Casts `[Memory Anchor: Cognitive Salve]` (2 AP), reinforcing squad composure.
  * Handler Soojin (Speed 5 -> 3 AP): Flings `[Resonance Snare: Leaded Ring]` (2 AP) around SE-C-IIIγ-928's vapor perimeter.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 04 to 05)**: Distillation Sprayer fires `[Concentrated Oblivion Jet]` (Base 11 + 2 Coins = 23 Power, Mind Drain).
    * Engineer Joon executes `[Hydraulic Kinetic Ram]` (Base 15 + 2 Coins = 27 Power, Heavy Blunt).
    * **Clash Outcome**: Joon WINS THE CLASH (27 vs 23)!
    * The hydraulic ram smashes straight into the outer vapor manifold of the sprayer!
    * Deals **480 Blunt damage** directly to the Distillation Sprayer arm and inflicts +48 Posture Strain!
  * **Clash 2 (Node 06 to 05)**: Chief Chemist Sura brandishes `[High-Frequency Solvent Scalpel]` (Power 21).
    * Auditor Yuna unleashes `[Cipher-Pulse: Resonance Intercept]` (Def Power 25).
    * **Clash Outcome**: Yuna WINS THE CLASH (25 vs 21).
    * The electromagnetic pulse destabilizes Sura's balance servos, reducing her speed to 1 and exposing her thoracic plate.
  * **Follow-Up Maneuvers**:
    * Taeho's `[Shield Bash]` deals **260 Blunt damage** to the exoskeleton chassis.
    * Minho's cognitive salve restores +15 SP across the strike cadre.
    * Infiltrator Echo slices an overhead solvent feeder, venting 300 liters of concentrated acid harmlessly into the floor drainage sump!
- **Step 4: Turn End State**:
  * Sura Exoskeleton HP: 1,630 -> **1,370/2,000** | Posture: **162/220**.
  * Distillation Sprayer HP: 1,400 -> **920/1,400** | Posture: **64/120 [CRACKED]**.
  * SE-C-IIIγ-928 Lethe HP: 2,800 -> **2,550/2,800** | Posture: **178/200**.
  * Combined Encounter HP: **4,840/6,200** | Squad Composure: **98%**.

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Neural Lancet Pierce & Stagger Threshold 1)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Commander Taeho's `Momentum Surge` activates (+2 Speed next turn -> Net Speed 6, 3 AP).
  * Sura attempts to overcharge her remaining chemical payload: `[Aerosol Amnesia Storm]`.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Investigator Minho (Speed 9 -> 5 AP): Takes elevated perch at Node 07. Spends 3 AP to fire `[Neural Lancet: Synaptic Pierce]`.
  * Commander Taeho (Speed 6 -> 3 AP): Charges from Node 03 to Node 05, unleashing `[Heavy Piston Strike]` (2 AP).
  * Engineer Joon (Speed 7 -> 4 AP): Plants `[Thermite Disruption Clamp]` (2 AP) directly on Sura's power cell.
  * Infiltrator Echo (Speed 9 -> 5 AP): Drops from catwalk onto Sura's back chassis, driving `[Eclipse Stiletto]` (2 AP).
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 07 to 05)**: Sura unleashes `[Aerosol Amnesia Storm]` (Base 14 + 2 Coins = 26 Power, Mind Drain).
    * Investigator Minho fires `[Neural Lancet: Synaptic Pierce]` (Base 18 + 2 Coins = 30 Power, High-Precision Pierce).
    * **Clash Outcome**: Minho WINS THE CLASH (30 vs 26)!
    * Minho's silver lancet pierces the central rotary valve of the sprayer arm with microscopic accuracy!
    * **TARGETED PART DESTROYED**: `[The Chemical Distillation Sprayer]` explodes into twisted aluminum and sparking cables (**920 Sprayer HP destroyed: 0/1,400**)!
  * **STAGGER THRESHOLD 1 TRIGGERED!**
    * Combined Target HP drops below 60% (3,720 HP), and Sura's Posture falls past the 60% strain line!
    * **STAGGER LEVEL 1 ACTIVE!** Sura's exoskeleton sparks violently, losing 100% defense and taking 2.0x direct damage. All enemy counter-stances cancelled!
  * **Punishment Strike Phase**:
    * Commander Taeho's `[Heavy Piston Strike]` delivers **420 Blunt damage** to the sparking chassis.
    * Engineer Joon's thermite clamp burns through the auxiliary accumulator for **350 Thermal damage**.
    * Infiltrator Echo's `[Eclipse Stiletto]` slices hydraulic tendons for **310 Slash damage**.
- **Step 4: Turn End State**:
  * Sura Exoskeleton HP: 1,370 -> **290/2,000** (Chassis critically fractured!).
  * Distillation Sprayer: **0/1,400 [DESTROYED]**.
  * Combined Encounter HP: **2,840/6,200** | Posture: **74/220 [STAGGER LEVEL 1]**.
  * Squad Composure: **100% (50/50 SP)**.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Pale Oblivion Surge & Leaded Sanctuary Ward)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Recovering from Stagger, Sura desperately yanks the emergency siphon bypass lever on SE-C-IIIγ-928's holding vat!
  * **ENCOUNTER EVENT**: The containment vat ruptures! SE-C-IIIγ-928 'Lethe' surges into **Berserk State** (+4 Attack Power)!
  * The entire chamber floods with blinding, dense pale amnesiac miasma.
  * Handler Soojin's `Momentum Surge` activates (+2 Speed -> Net Speed 7, 4 AP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Handler Soojin (Speed 7 -> 4 AP): Moves to Node 06, deploying `[Leaded Sanctuary: Damping Field]` (3 AP) to enclose the entire squad and the adjacent civilian berths.
  * Commander Taeho (Speed 4 -> 2 AP): Steps to Node 03, locking his Obsidian shield in front of the hostage pens.
  * Auditor Yuna (Speed 7 -> 4 AP): Hacks the facility ventilation exhaust at Node 06, venting pale vapors outdoors (2 AP).
  * Investigator Minho (Speed 7 -> 4 AP): Dispenses `[Neuro-Stabilizing Aerosol]` (2 AP) to protect civilian minds.
  * Engineer Joon (Speed 5 -> 3 AP): Uses pneumatic pry bar at Node 04 to begin unjamming hostage restraint locks (2 AP).
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 10 to 06)**: Berserk SE-C-IIIγ-928 unleashes `[Pale Oblivion Surge: Tidal Amnesia]` (Base 21 + 2 Coins = 31 Power, Area Mind Purge).
    * Handler Soojin deploys `[Leaded Sanctuary: Damping Field]` (Base 24 + 2 Coins = 34 Power, Vacuum Barrier).
    * **Clash Outcome**: Soojin WINS THE CLASH (34 vs 31)!
    * The lead-lined resonance sphere captures the psychic blast perfectly (`[P3: Parry/Protection]`).
    * Zero amnesiac particles penetrate the leaded ward. Soojin redirects the captured resonance back into the entity's core, dealing **450 Void damage** and +66 Posture Strain!
- **Step 4: Turn End State**:
  * Sura Exoskeleton HP: **290/2,000**.
  * SE-C-IIIγ-928 Lethe Core HP: 2,550 -> **2,100/2,800** | Posture: **112/200**.
  * Combined Encounter HP: **2,390/6,200** | Squad Composure: **94%**.

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Phantom Sever & Terminal Stagger Threshold 2)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Infiltrator Echo readies `[Eclipse Stiletto: Phantom Sever]` from the overhead steam conduits (+50% Crit Chance, ignores 100% defense).
  * Investigator Minho aligns his sight on the entity's primary cognitive anchor.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Infiltrator Echo (Speed 11 -> 5 AP, Momentum + Stealth Boost): Drops from the high pipe directly onto Node 10. Spends 3 AP on `[Phantom Sever]`.
  * Investigator Minho (Speed 7 -> 4 AP): Fires `[Silver Lancet: Cognitive Disruptor]` from Node 07 into the exposed core (2 AP).
  * Engineer Joon (Speed 5 -> 3 AP): Smashes away Sura's buckled leg supports at Node 04 (2 AP).
  * Auditor Yuna (Speed 7 -> 4 AP): Finalizes forensic download of 4,216 stolen memory files at Node 06 (2 AP).
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 10)**: SE-C-IIIγ-928 lashes out with `[Grasping Shroud of Forgetfulness]` (Atk Power 27, Pierce).
    * Infiltrator Echo executes `[Eclipse Stiletto: Phantom Sever]` (Base 22 + 2 Coins Heads = 32 Power, Slash).
    * **Clash Outcome**: Echo WINS THE CLASH (32 vs 27)!
    * Echo slices cleanly through the synthetic sorrow conduits feeding the miasma core!
    * **CRITICAL HIT!** Deals **580 Slash damage** directly to the core and strips 70 Posture points!
  * **Targeted Fire**:
    * Investigator Minho's `[Silver Lancet]` strikes the exposed cognitive anchor, dealing **410 Freezing Pierce damage** and wiping out the entity's remaining Posture!
    * Engineer Joon tears away Sura's buckled leg servos with the pneumatic pry bar, dealing **290 Blunt damage** and crushing the exoskeleton completely (Exoskeleton HP: 0/2,000)!
- **Step 4: TERMINAL STAGGER THRESHOLD 2 TRIGGERED!**:
  * Both Sura and SE-C-IIIγ-928 reach **Posture 0/220** and **0/200**!
  * **TERMINAL STAGGER ACTIVE!** Sura's chassis collapses under hydraulic feedback, pinning her to the deck. SE-C-IIIγ-928's amnesiac shroud implodes into a dense, sluggish vortex.
  * Combined Encounter HP drops below 25% (Total HP: **1,110/6,200**).
- **Step 5: Turn End State**:
  * Sura Exoskeleton HP: **0/2,000 [CHASSIS CRUSHED]** | Posture: **0/220**.
  * SE-C-IIIγ-928 Lethe HP: **1,110/2,800** | Posture: **0/200 [TERMINAL STAGGER]**.
  * Squad Composure: **100% (50/50 SP)**.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Overdrive: Iron Gavel & Cryo-Seal)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Commander Taeho charges `[Decree of Unbroken Order — Iron Gavel]` (Cost: 35 SP).
  * Handler Soojin activates `[Class-IV Leaded Cryo-Seal: Vault of Solitude]` (Cost: 35 SP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Commander Taeho (Speed 4 -> 2 AP): Steps up to Node 05, standing over Sura's pinned chassis. Spends 2 AP on Climax Overdrive.
  * Handler Soojin (Speed 5 -> 3 AP): Wheels the Class-IV Cryogenic Leaded Cask directly beneath the Lethe funnel at Node 10. Spends 3 AP on Climax Containment.
  * Engineer Joon and Infiltrator Echo: Unlatch the final restraint collars on the 18 civilian hostages at Node 08, wrapping them in insulated blankets.
  * Auditor Yuna: Verifies Level-5 encryption on the 4,216 seized memory crystals at Node 06.
- **Step 3: Climax Overdrive Executions**:
  * **Climax 1 (Commander Taeho vs Chief Chemist Sura)**:
    * Taeho raises his heavy obsidian shield, channeling a focused concussive kinetic pulse: `[Iron Gavel: Decreed Subjugation]` (Power 42).
    * Smashes the reinforced cockpit canopy cleanly along pre-existing stress fractures.
    * The canopy fractures away safely without injuring the pilot. Non-lethal kinetic tremor renders Sura unconscious.
    * **CHIEF CHEMIST SURA EXTRACTED & INCAPACITATED!** Remanded to Warden custody!
  * **Climax 2 (Handler Soojin vs SE-C-IIIγ-928 'Lethe')**:
    * Soojin clamps the leaded seal collar onto the Lethe funnel, triggering absolute sub-zero cryogenic vacuum suction: `[Vault of Solitude]` (Power 40).
    * All swirling amnesiac vapors are drawn into the leaded cask within 4.2 seconds! Zero atmospheric leakage detected.
    * The hydraulic locking pins engage with a heavy metallic boom: **CRYOGENIC VACUUM SEAL COMPLETE**.
    * **SE-C-IIIγ-928 HP DROPS TO 0!** Fully contained in inert dormancy and logged for transfer to Reverie Directorate Floor 2!
- **Step 4: Pacification & Operational Outcome**:
  * **Chief Chemist Sura**: Exoskeleton destroyed; pilot safely secured in Warden custody.
  * **Distillation Sprayer**: 100% demolished.
  * **SE-C-IIIγ-928 'Lethe'**: 100% contained in cryogenic lead cask. Zero leakage.
  * **Civilian Hostages**: 18 citizens liberated and stabilized with zero long-term cognitive loss.
  * **Evidence**: 4,216 intact memory crystals seized, exposing high-ranking syndicate buyers.
"""

def update_operation_2():
    path = "SOMNARAK-WORLD/Katharcheok/Operation_2_Lethepyo.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    start_str = "### Tactical Engagement: 6-Turn Pacification Gauntlet"
    end_str = "### Post-Action Forensic Inventory"

    start_idx = content.find(start_str)
    end_idx = content.find(end_str)

    if start_idx == -1 or end_idx == -1:
        print(f"Error: Could not locate boundaries! start_idx={start_idx}, end_idx={end_idx}")
        return

    new_engagement = get_op2_engagement() + "\n\n"
    new_content = content[:start_idx] + new_engagement + content[end_idx:]

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Updated Operation 2 successfully!")

if __name__ == "__main__":
    update_operation_2()
