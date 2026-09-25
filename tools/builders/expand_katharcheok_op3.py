#!/usr/bin/env python3
"""
tools/expand_katharcheok_op3.py
Expands Operation 3 (Messischwi - The Low Sinks) in SOMNARAK-WORLD/Katharcheok/Operation_3_Messischwi.md
Replaces the older summary/compressed boxes in ### Tactical Engagement: 6-Turn Pacification Gauntlet
with full 10-node spatial tactical HUDs, Speed/AP breakdowns, M.A.W.-W weight deltas,
and Four P-framework action resolution logs across all 6 turns.
"""

import sys, os
sys.path.append(os.path.dirname(__file__))
from box_formatter import make_box

def get_op3_engagement():
    dossier_box = make_box("TARGET DOSSIER: WARLORD BOKNAM & SE-C-IIIγ-120 'RAGE CAGE'", [
        "APEX TARGET        : Warlord Boknam ('The Meat Hook Baron')",
        "MODULAR WEAPON     : Pneumatic Harvest Hook Arm (Heavy Slash/Snare)",
        "CONTRABAND ENTITY  : SE-C-IIIγ-120 'Rage Cage' (Rank III Threat / Redcage)",
        "ESCORT MINIONS     : Siphon Enforcers (x2) & Slag Bone-Sawyers",
        "ENCOUNTER DOMAIN   : Zone B Low Sinks Sub-Abattoir (-120m Depth)",
        "---",
        "BOSS COMBAT PROFILE (WARLORD BOKNAM):",
        "- Winch Rig HP     : 2,200 HP | Core Body HP: 2,000 HP (Total 4,200 HP)",
        "- Harvest Hook HP  : 1,600 HP (Modular Destructible Weapon Part)",
        "- Posture Pool     : 240/240 (Dual Threshold Stagger System)",
        "- Stagger 1 Proc   : 60% Posture Strain (144 Posture) / Hook Destruction",
        "- Stagger 2 Proc   : 0% Posture Collapse (Terminal Stagger / Cask Ready)",
        "- Primary Attack   : Pneumatic Hook Cleave & High-Tension Snare (Slash)",
        "---",
        "CONTRABAND ENTITY PROFILE (SE-C-IIIγ-120 'RAGE CAGE'):",
        "- Entity HP Pool   : 3,000 HP | Posture Pool: 220/220",
        "- Total Combined   : 6,800 Encounter HP",
        "- Attack Affinity  : Crimson Rage Surge & Grudge Resonance (Fire/Blood)"
    ])

    hud_t01 = make_box("TACTICAL STAGE HUD: OPERATION 03 — BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 — ZONE B LOW SINKS ABATTOIR VAULT]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER][TAEHO] [JOON]  [SOOJIN][BOKNAM] [YUNA]  [MINHO] [CIVS]          [CAGE]  ",
        "                                 [HOOK]                           [ECHO]  ",
        "---",
        "- Node 01: Breach Entry / Class-II Armored Cruiser 'The Iron Vanguard'",
        "- Node 02: Commander Taeho (Vanguard Band 1 / Phalanx Bastion Granite)",
        "- Node 03: Engineer Joon (Point-Blank Band 1 / Deployable Mantlet Barrier)",
        "- Node 04: Handler Soojin (Close Skirmish Band 2 / Sedative Aerosol Ward)",
        "- Node 05: Warlord Boknam & Harvest Hook (Central Processing Dais)",
        "- Node 06: Auditor Yuna (Mid-Field Band 3 / Forensic Wiretap Console)",
        "- Node 07: Investigator Minho (Mid-Field Band 3 / Mnemonic Sniper Rafter)",
        "- Node 08: Extraction Berths (24 Captive Abattoir Workers)",
        "- Node 10: SE-C-IIIγ-120 'Rage Cage' & Infiltrator Echo (Chain Stealth)",
        "---",
        "- Taeho       : Spd 4 -> 2 AP | HP 4,400/4,400 | SP 45/50 | Posture 180/180",
        "- Joon        : Spd 5 -> 3 AP | HP 3,800/3,800 | SP 40/40 | Posture 150/150",
        "- Yuna        : Spd 7 -> 4 AP | HP 2,700/2,700 | SP 50/50 | Posture 100/100",
        "- Minho       : Spd 7 -> 4 AP | HP 2,900/2,900 | SP 45/45 | Posture 110/110",
        "- Soojin      : Spd 5 -> 3 AP | HP 3,600/3,600 | SP 50/50 | Posture 140/140",
        "- Echo        : Spd 9 -> 5 AP | HP 2,600/2,600 | SP 40/40 | Posture 90/90 [STEALTH]",
        "- Boknam Rig  : Spd 4 -> 2 AP | HP 2,200/2,200 | Posture 240/240 [ARMORED]",
        "- Hook Weapon : Spd 3 -> 1 AP | HP 1,600/1,600 | Posture 140/140 [PRIMED]",
        "- Rage Cage   : Spd 5 -> 3 AP | HP 3,000/3,000 | Posture 220/220 [CAGED]"
    ])

    hud_t02 = make_box("TACTICAL STAGE HUD: OPERATION 03 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — WINCH SAPPING & FREQUENCY JAM]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER][TAEHO] [JOON]  [SOOJIN][BOKNAM] [YUNA]  [MINHO] [CIVS]  [ECHO]  [CAGE]  ",
        "                                 [HOOK]                                   ",
        "---",
        "- Node 02: Commander Taeho (Advancing to Node 03 / Concussive Shield Bash)",
        "- Node 03: Engineer Joon (Hydraulic Kinetic Ram Smashes Winch Pulley)",
        "- Node 04: Handler Soojin (Leaded Snare Restricting Rage Expansion)",
        "- Node 05: Warlord Boknam (Rig 1,480/2,200 / Harvest Hook 1,180/1,600)",
        "- Node 06: Auditor Yuna (Cipher-Pulse Dampening Redcage Resentment)",
        "- Node 07: Investigator Minho (Memory Anchor Restoring Squad Composure)",
        "- Node 09: Infiltrator Echo (Chain Hoist Catwalk Flank behind Dais)",
        "- Node 10: SE-C-IIIγ-120 'Rage Cage' (2,750/3,000 HP / Bars Heating)",
        "---",
        "- Joon        : Spd 7 -> 4 AP [SURGE] | HP 3,800/3,800 | SP 40/40 | Posture 150/150",
        "- Minho       : Spd 9 -> 5 AP [SURGE] | HP 2,900/2,900 | SP 50/50 | Posture 110/110",
        "- Boknam Rig  : Spd 3 -> 1 AP | HP 1,480/2,200 | Posture 172/240 [PULLEY BROKEN]",
        "- Hook Weapon : Spd 2 -> 1 AP | HP 1,180/1,600 | Posture 82/140 [STRAINED]",
        "- Rage Cage   : Spd 4 -> 2 AP | HP 2,750/3,000 | Posture 194/220 [SNARED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: OPERATION 03 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — HOOK SHATTER & STAGGER THRESHOLD 1]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER]        [TAEHO] [JOON]  [BOKNAM] [YUNA]  [MINHO] [CIVS]  [ECHO]  [CAGE]  ",
        "---",
        "- Node 03: Commander Taeho (Heavy Piston Strike Smashes Winch Armor)",
        "- Node 04: Engineer Joon (Thermite Disruption Clamp Igniting Motor)",
        "- Node 05: Warlord Boknam (STAGGER LEVEL 1 / HOOK DESTROYED)",
        "- Node 06: Auditor Yuna (Debt Ledger Download In Progress)",
        "- Node 07: Investigator Minho (Synaptic Pierce Dismantles Hook Joint)",
        "- Node 09: Infiltrator Echo (Driving Eclipse Stiletto into Winch Servos)",
        "- Node 10: SE-C-IIIγ-120 'Rage Cage' (Red Steam Churning)",
        "---",
        "- Taeho       : Spd 6 -> 3 AP [SURGE] | HP 4,400/4,400 | SP 48/50 | Posture 180/180",
        "- Boknam Rig  : Spd 0 -> 0 AP | HP 380/2,200   | Posture 86/240 [STAGGER LEVEL 1]",
        "- Hook Weapon : DESTROYED (0/1,600 HP)",
        "- Rage Cage   : Spd 5 -> 3 AP | HP 2,750/3,000 | Posture 194/220"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: OPERATION 03 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — BERSERK RAGE CAGE & LEADED BARRIER WARD]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER]        [TAEHO] [JOON]  [BOKNAM] [SOOJIN][YUNA]  [CIVS]  [ECHO]  [CAGE]  ",
        "                                                  [MINHO]                 ",
        "---",
        "- Node 03: Commander Taeho (Shielding Processing Berths & Captives)",
        "- Node 04: Engineer Joon (Pneumatic Pry Bar Unlatching Siphon Berths)",
        "- Node 05: Warlord Boknam (Recovered / Pulling Safety Valve on Cage)",
        "- Node 06: Handler Soojin (Leaded Barrier Ward Enclosing Squad)",
        "- Node 07: Auditor Yuna & Minho (Purging High-Pressure Steam Conduits)",
        "- Node 08: 24 Civilian Captives (Cognitive Shields Holding Intact)",
        "- Node 10: SE-C-IIIγ-120 'Rage Cage' (BERSERK STATE / Crimson Fury Surge)",
        "---",
        "- Soojin      : Spd 7 -> 4 AP [SURGE] | HP 3,600/3,600 | SP 50/50 | Posture 140/140",
        "- Boknam Rig  : Spd 2 -> 1 AP | HP 380/2,200   | Posture 60/240",
        "- Rage Cage   : Spd 6 -> 4 AP | HP 2,270/3,000 | Posture 124/220 [BERSERK]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: OPERATION 03 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — PHANTOM SEVER & TERMINAL STAGGER]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER]        [TAEHO] [JOON]  [BOKNAM] [SOOJIN][YUNA]  [CIVS]          [CAGE]  ",
        "                                                  [MINHO]         [ECHO]  ",
        "---",
        "- Node 03: Commander Taeho (Priming Iron Gavel for Cockpit Breach)",
        "- Node 04: Engineer Joon (Tearing Away Buckled Winch Struts)",
        "- Node 05: Boknam Winch Rig (TERMINAL STAGGER / POSTURE 0/240 / CRUSHED)",
        "- Node 06: Handler Soojin (Aligning Class-IV Leaded Cryo-Cask at Dais)",
        "- Node 07: Investigator Minho (Silver Lancet Stripping Core Resentment)",
        "- Node 09: Infiltrator Echo (Eclipse Stiletto Phantom Sever on Bars)",
        "- Node 10: SE-C-IIIγ-120 'Rage Cage' (TERMINAL STAGGER / POSTURE 0/220)",
        "---",
        "- Echo        : Spd 11 -> 5 AP [MOMENTUM CRIT] | HP 2,600/2,600 | SP 40/40",
        "- Boknam Rig  : Spd 0 -> 0 AP | HP 0/2,200     | Posture 0/240 [CHASSIS CRUSHED]",
        "- Rage Cage   : Spd 0 -> 0 AP | HP 1,190/3,000 | Posture 0/220 [TERMINAL STAGGER]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: OPERATION 03 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX OVERDRIVE: IRON GAVEL & CRYO-SEAL]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER]                [JOON]  [TAEHO]  [SOOJIN][YUNA]  [CIVS]          [CASK]  ",
        "                                 [BOKNAM]         [MINHO]         [ECHO]  ",
        "---",
        "- Node 05: Warlord Boknam (EXTRACTED UNCONSCIOUS & SECURED)",
        "- Node 06: Auditor Yuna (6,400 Black-Market Debt Records Secured)",
        "- Node 08: 24 Civilian Captives (Safely Unlatched / Zero Fatalities)",
        "- Node 10: SE-C-IIIγ-120 'Rage Cage' (100% CONTAINED IN CRYOGENIC CASK)",
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

###### Turn 01 Action Resolution Log (Kinetic Ingress & Hook Deflection)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Commander Taeho initializes `[Law of the Mantle]`: All allies within 1 node gain +3 Protection and physical stagger immunity.
  * Infiltrator Echo activates `[Shadow Cloak]`: Enters stealth for 2 turns; cannot be targeted by single-target attacks; +50\% Critical Strike Chance.
  * Handler Soojin initializes `[Sedative Aerosol Ward]`, suppressing crimson rage fumes leaking from SE-C-IIIγ-120.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Commander Taeho (Speed 4 -> 2 AP, M.A.W.-W Heavy Armor delta -1, Poise +25): Holds Node 02. Spends 2 AP on `[Phalanx Bastion: Granite Wall]`.
  * Engineer Joon (Speed 5 -> 3 AP, M.A.W.-W Medium delta 0): Holds Node 03. Spends 2 AP on `[Deployable Mantlet Barrier]`. Holds 1 AP in Reserve.
  * Auditor Yuna (Speed 7 -> 4 AP, M.A.W.-W Light delta +1): Holds Node 06 (Range Band 3). Spends 2 AP on `[Cipher-Scan: Hydraulic Frequency]`, 2 AP on `[Asset Scan]`.
  * Investigator Minho (Speed 7 -> 4 AP, M.A.W.-W Light delta +1): Stands at Node 07. Spends 2 AP on `[Neural Lancet: Calibrated Dart]`. Holds 2 AP in Reserve.
  * Handler Soojin (Speed 5 -> 3 AP, M.A.W.-W Medium delta 0): Holds Node 04. Spends 2 AP on maintaining the sedative ward. Holds 1 AP in Guard.
  * Infiltrator Echo (Speed 9 -> 5 AP, M.A.W.-W Feather delta +2): Scales rusted chain hoists toward Node 10 from stealth. Spends 2 AP on positioning.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 02 to 05)**: Warlord Boknam unleashes `[Pneumatic Hook Cleave]` (Base 14 + 2 Coins = 26 Power, Heavy Slash) against Node 02.
    * Commander Taeho counters with `[Phalanx Bastion: Granite Wall]` (Base 16 + 2 Coins = 30 Power, Kinetic Shield).
    * **Clash Outcome**: Taeho WINS THE CLASH (30 vs 26)!
    * The kinetic shield completely deflects the massive barbed steel hook (`[P3: Parry/Protection]`).
    * Taeho reflects **160 kinetic tremor damage** back into Boknam's steam winch rig! Inflicts +28 Posture Strain.
  * **Clash 2 (Node 03 to 05)**: Siphon Enforcers charge with `[Rotary Bone-Saw Rush]` (Atk Power 20, Slash).
    * Engineer Joon's `[Deployable Mantlet Barrier]` (Def Power 24, Kinetic Shield).
    * **Clash Outcome**: Joon WINS THE CLASH (24 vs 20).
    * Saws spark harmlessly off the titanium plate; zero damage taken.
  * **Unopposed Ranged Fire**:
    * Auditor Yuna's `[Cipher-Scan]` identifies the high-pressure steam winch pressure release valve.
    * Investigator Minho fires `[Neural Lancet: Calibrated Dart]` from Node 07 into Boknam's armored shoulder, dealing **240 Pierce damage** and +24 Posture Strain!
    * Handler Soojin's sedative ward neutralizes ambient rage fumes around the squad.
- **Step 4: Turn End State**:
  * Boknam Winch Rig HP: 2,200 -> **1,800/2,200** (Combined Encounter HP: **6,400/6,800**).
  * Boknam Posture: 240 -> **188/240**.
  * Squad Composure: **100% (50/50 SP)**. All 6 Officers uninjured.

---

```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Sapping the Hydraulic Winch & Frequency Jam)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Engineer Joon and Investigator Minho both trigger `Momentum Surge` (+2 Speed next turn).
  * Boknam winds up the high-tension cable spool for an area drag: `[High-Tension Cable Snare]`.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Engineer Joon (Speed 7 -> 4 AP): Advances from Node 03 to Node 04. Spends 3 AP to unleash `[Hydraulic Kinetic Ram: Structural Sapping]`.
  * Auditor Yuna (Speed 7 -> 4 AP): Moves to Node 06, deploying `[Cipher-Pulse: Damping Wall]` (2 AP) against SE-C-IIIγ-120's rage cycle.
  * Commander Taeho (Speed 4 -> 2 AP): Steps to Node 03, executing `[Shield Bash: Heavy Tremor]` (2 AP).
  * Investigator Minho (Speed 9 -> 5 AP): Casts `[Memory Anchor: Cognitive Salve]` (2 AP), reinforcing squad composure (+15 SP).
  * Handler Soojin (Speed 5 -> 3 AP): Flings `[Resonance Snare: Leaded Ring]` (2 AP) around the cage perimeter.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 04 to 05)**: Boknam fires `[High-Tension Cable Snare]` (Base 12 + 2 Coins = 24 Power, Pierce).
    * Engineer Joon executes `[Hydraulic Kinetic Ram]` (Base 16 + 2 Coins = 28 Power, Heavy Blunt).
    * **Clash Outcome**: Joon WINS THE CLASH (28 vs 24)!
    * The hydraulic ram smashes straight into the secondary cable pulley drum!
    * Deals **520 Blunt damage** directly to Boknam's Steam Winch Rig and inflicts +52 Posture Strain!
  * **Clash 2 (Node 06 to 10)**: SE-C-IIIγ-120 'Rage Cage' pulses `[Crimson Resentment Pulse]` (Power 22, Grudge).
    * Auditor Yuna unleashes `[Cipher-Pulse: Damping Wall]` (Def Power 26, EMP).
    * **Clash Outcome**: Yuna WINS THE CLASH (26 vs 22).
    * The EMP pulse dampens the entity's rage cycle, dealing **250 Resonance damage** to SE-C-IIIγ-120 and +26 Posture Strain!
  * **Follow-Up Maneuvers**:
    * Taeho's `[Shield Bash]` deals **280 Blunt damage** to the winch chassis.
    * Minho's cognitive salve restores +15 SP across the strike cadre.
    * Infiltrator Echo severs overhead steam bypass conduits, releasing 200 PSI of blinding scalding steam away from the hostages!
- **Step 4: Turn End State**:
  * Boknam Winch Rig HP: 1,800 -> **1,480/2,200** | Posture: **172/240 [PULLEY BROKEN]**.
  * Harvest Hook Weapon HP: 1,600 -> **1,180/1,600** | Posture: **82/140**.
  * SE-C-IIIγ-120 Rage Cage HP: 3,000 -> **2,750/3,000** | Posture: **194/220**.
  * Combined Encounter HP: **5,410/6,800** | Squad Composure: **98%**.

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Precision Lancet Pierce & Stagger Threshold 1)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Commander Taeho's `Momentum Surge` activates (+2 Speed next turn -> Net Speed 6, 3 AP).
  * Boknam attempts his brutal overhead execution: `[Pneumatic Hook Execution]`.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Investigator Minho (Speed 9 -> 5 AP): Positions on an elevated rafter at Node 07. Spends 3 AP on `[Neural Lancet: Synaptic Pierce]`.
  * Commander Taeho (Speed 6 -> 3 AP): Charges from Node 03 to Node 05, unleashing `[Heavy Piston Strike]` (2 AP).
  * Engineer Joon (Speed 7 -> 4 AP): Plants `[Thermite Disruption Clamp]` (2 AP) directly on Boknam's winch motor.
  * Infiltrator Echo (Speed 9 -> 5 AP): Drops from chains onto the hook's wrist assembly, driving `[Eclipse Stiletto]` (2 AP).
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 07 to 05)**: Boknam unleashes `[Pneumatic Hook Execution]` (Base 15 + 2 Coins = 27 Power, Heavy Slash).
    * Investigator Minho fires `[Neural Lancet: Synaptic Pierce]` (Base 19 + 2 Coins = 31 Power, High-Precision Pierce).
    * **Clash Outcome**: Minho WINS THE CLASH (31 vs 27)!
    * Minho's silver lancet strikes the main hydraulic valve of the hook joint with pinpoint accuracy!
    * **TARGETED PART DESTROYED**: `[The Pneumatic Harvest Hook Arm]` shears completely off, clattering into the abattoir drain (**1,180 Hook HP destroyed: 0/1,600**)!
  * **STAGGER THRESHOLD 1 TRIGGERED!**
    * Combined Target HP drops below 60% (4,080 HP), and Boknam's Posture falls past the 60% strain line!
    * **STAGGER LEVEL 1 ACTIVE!** Boknam's rig loses all defense, taking 1.5x direct damage. All enemy counter-stances cancelled!
  * **Punishment Strike Phase**:
    * Commander Taeho's `[Heavy Piston Strike]` delivers **460 Blunt damage** to the exposed winch chassis.
    * Engineer Joon's thermite clamp burns through the drive gears for **380 Thermal damage**.
    * Infiltrator Echo's `[Eclipse Stiletto]` slices servo tendons for **340 Slash damage**.
- **Step 4: Turn End State**:
  * Boknam Winch Rig HP: 1,480 -> **380/2,200** (Chassis critically buckled!).
  * Harvest Hook Weapon: **0/1,600 [DESTROYED]**.
  * Combined Encounter HP: **3,130/6,800** | Posture: **86/240 [STAGGER LEVEL 1]**.
  * Squad Composure: **100% (50/50 SP)**.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Crimson Rage Surge & Leaded Barrier Ward)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Recovering from Stagger, Boknam yanks the emergency bypass valve on the Redcage at Node 10!
  * **ENCOUNTER EVENT**: SE-C-IIIγ-120 'Rage Cage' enters **Berserk State** (+4 Attack Power)!
  * Red iron bars glow incandescent white; dense, boiling blood-rage vapor floods the abattoir.
  * Handler Soojin's `Momentum Surge` activates (+2 Speed -> Net Speed 7, 4 AP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Handler Soojin (Speed 7 -> 4 AP): Moves to Node 06, deploying `[Leaded Barrier Ward: Vacuum Sphere]` (3 AP) enclosing the squad and hostage berths.
  * Commander Taeho (Speed 4 -> 2 AP): Steps to Node 03, locking his Obsidian shield in front of the holding cells.
  * Auditor Yuna (Speed 7 -> 4 AP): Hacks the abattoir steam vents at Node 06, dumping hydraulic pressure (2 AP).
  * Investigator Minho (Speed 7 -> 4 AP): Dispenses `[Neuro-Stabilizing Aerosol]` (2 AP) to protect captive sanity.
  * Engineer Joon (Speed 5 -> 3 AP): Uses pneumatic pry bar at Node 04 to pop open the captive cell latch pins (2 AP).
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 10 to 06)**: Berserk SE-C-IIIγ-120 unleashes `[Crimson Fury Deluge: Scalding Blood]` (Base 22 + 2 Coins = 32 Power, Area Fire/Grudge).
    * Handler Soojin deploys `[Leaded Barrier Ward]` (Base 25 + 2 Coins = 35 Power, Vacuum Barrier).
    * **Clash Outcome**: Soojin WINS THE CLASH (35 vs 32)!
    * The lead-lined vacuum sphere fully absorbs the scalding blood-steam (`[P3: Parry/Protection]`).
    * Zero thermal particles penetrate the leaded ward. Soojin redirects the trapped resonance back into the cage, dealing **480 Void damage** and +70 Posture Strain!
- **Step 4: Turn End State**:
  * Boknam Winch Rig HP: **380/2,200** | Posture: **60/240**.
  * SE-C-IIIγ-120 Rage Cage HP: 2,750 -> **2,270/3,000** | Posture: **124/220**.
  * Combined Encounter HP: **2,650/6,800** | Squad Composure: **96%**.

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Phantom Stiletto Sever & Terminal Stagger Threshold 2)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Infiltrator Echo readies `[Eclipse Stiletto: Phantom Sever]` from the overhead rusted meat chains (+50% Crit Chance, ignores 100% defense).
  * Investigator Minho targets the entity's primary red iron heart latch.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Infiltrator Echo (Speed 11 -> 5 AP, Momentum + Stealth Boost): Drops from the high chains onto Node 10. Spends 3 AP on `[Phantom Sever]`.
  * Investigator Minho (Speed 7 -> 4 AP): Fires `[Silver Lancet: Cognitive Disruptor]` from Node 07 into the exposed cage latch (2 AP).
  * Engineer Joon (Speed 5 -> 3 AP): Smashes away Boknam's remaining winch struts at Node 04 (2 AP).
  * Auditor Yuna (Speed 7 -> 4 AP): Finalizes forensic download of 6,400 illicit debt records at Node 06 (2 AP).
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 10)**: SE-C-IIIγ-120 lashes out with `[Barbed Chain Frenzy]` (Atk Power 28, Slash).
    * Infiltrator Echo executes `[Eclipse Stiletto: Phantom Sever]` (Base 23 + 2 Coins Heads = 33 Power, Slash).
    * **Clash Outcome**: Echo WINS THE CLASH (33 vs 28)!
    * Echo slices cleanly through the red iron arterial conduits feeding the cage bars!
    * **CRITICAL HIT!** Deals **620 Slash damage** directly to the core and strips 80 Posture points!
  * **Targeted Fire**:
    * Investigator Minho's `[Silver Lancet]` strikes the exposed core latch, dealing **460 Freezing Pierce damage** and wiping out the entity's remaining Posture!
    * Engineer Joon crushes Boknam's buckled winch chassis with the pneumatic ram, dealing **380 Blunt damage** and demolishing the rig completely (Rig HP: 0/2,200)!
- **Step 4: TERMINAL STAGGER THRESHOLD 2 TRIGGERED!**:
  * Both Boknam and SE-C-IIIγ-120 reach **Posture 0/240** and **0/220**!
  * **TERMINAL STAGGER ACTIVE!** Boknam's rig collapses under hydraulic explosion, pinning him to the stone tiles. SE-C-IIIγ-120's rage steam ceases bubbling, cooling into dull gray iron.
  * Combined Encounter HP drops below 20% (Total HP: **1,190/6,800**).
- **Step 5: Turn End State**:
  * Boknam Winch Rig HP: **0/2,200 [CHASSIS CRUSHED]** | Posture: **0/240**.
  * SE-C-IIIγ-120 Rage Cage HP: **1,190/3,000** | Posture: **0/220 [TERMINAL STAGGER]**.
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
  * Commander Taeho (Speed 4 -> 2 AP): Steps up to Node 05, standing over Boknam's pinned chassis. Spends 2 AP on Climax Overdrive.
  * Handler Soojin (Speed 5 -> 3 AP): Wheels the Class-IV Cryogenic Leaded Cask directly beneath the Redcage funnel at Node 10. Spends 3 AP on Climax Containment.
  * Engineer Joon and Infiltrator Echo: Unlatch the final cell doors on the 24 civilian workers at Node 08, escorting them to the cruiser.
  * Auditor Yuna: Verifies Level-5 encryption on the 6,400 seized transaction drives at Node 06.
- **Step 3: Climax Overdrive Executions**:
  * **Climax 1 (Commander Taeho vs Warlord Boknam)**:
    * Taeho raises his heavy obsidian shield, channeling a 120 dB directed concussive wave: `[Iron Gavel: Decreed Subjugation]` (Power 42).
    * Smashes the reinforced cockpit armor cleanly along stress fissures.
    * The armor breaks away; non-lethal kinetic tremor renders Boknam unconscious.
    * **WARLORD BOKNAM EXTRACTED & INCAPACITATED!** Remanded to Warden custody!
  * **Climax 2 (Handler Soojin vs SE-C-IIIγ-120 'Rage Cage')**:
    * Soojin clamps the leaded seal collar onto the Redcage vents, triggering absolute sub-zero cryogenic vacuum suction: `[Vault of Solitude]` (Power 40).
    * All boiling crimson rage vapors are sucked into the leaded cask within 4.0 seconds! Zero atmospheric leakage detected.
    * The hydraulic locking pins engage with a heavy metallic boom: **CRYOGENIC VACUUM SEAL COMPLETE**.
    * **SE-C-IIIγ-120 HP DROPS TO 0!** Fully contained in inert dormancy and logged for transfer to Reverie Directorate Floor 2!
- **Step 4: Pacification & Operational Outcome**:
  * **Warlord Boknam**: Winch rig demolished; warlord safely secured in Warden custody.
  * **Pneumatic Harvest Hook**: 100% destroyed.
  * **SE-C-IIIγ-120 'Rage Cage'**: 100% contained in cryogenic lead cask. Zero leakage.
  * **Civilian Hostages**: 24 citizens liberated and stabilized with zero fatalities.
  * **Evidence**: 6,400 black-market debt transaction records seized, exposing high-ranking abattoir backers.
"""

def update_operation_3():
    path = "SOMNARAK-WORLD/Katharcheok/Operation_3_Messischwi.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    start_str = "### Tactical Engagement: 6-Turn Pacification Gauntlet"
    end_str = "### Post-Action Forensic Inventory"

    start_idx = content.find(start_str)
    end_idx = content.find(end_str)

    if start_idx == -1 or end_idx == -1:
        print(f"Error: Could not locate boundaries! start_idx={start_idx}, end_idx={end_idx}")
        return

    new_engagement = get_op3_engagement() + "\n\n"
    new_content = content[:start_idx] + new_engagement + content[end_idx:]

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Updated Operation 3 successfully!")

if __name__ == "__main__":
    update_operation_3()
