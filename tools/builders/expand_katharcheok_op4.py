#!/usr/bin/env python3
"""
tools/expand_katharcheok_op4.py
Expands Operation 4 (Usurachae - The Usury Vaults) in SOMNARAK-WORLD/Katharcheok/Operation_4_Usurachae.md
Replaces the older summary/compressed boxes in ### Tactical Engagement: 6-Turn Pacification Gauntlet
with full 10-node spatial tactical HUDs, Speed/AP breakdowns, M.A.W.-W weight deltas,
and Four P-framework action resolution logs across all 6 turns.
"""

import sys, os
sys.path.append(os.path.dirname(__file__))
from box_formatter import make_box

def get_op4_engagement():
    dossier_box = make_box("TARGET DOSSIER: HIGH USURER MAN-SIK & SE-C-IIIβ-015 'DEBT SCALE'", [
        "APEX TARGET        : High Usurer Man-sik ('The Golden Shylock')",
        "MODULAR WEAPON     : Electrified Foreclosure Cudgel (Heavy Blunt/Shock)",
        "CONTRABAND ENTITY  : SE-C-IIIβ-015 'The Debt Scale' (Rank III / Debt Scale)",
        "ESCORT MINIONS     : Gilded Mercenaries (x2) & Pneumatic Coin-Gunners",
        "ENCOUNTER DOMAIN   : Zone C Usury Vaults & Gold Siphon (-180m Depth)",
        "---",
        "BOSS COMBAT PROFILE (HIGH USURER MAN-SIK):",
        "- Midas Chassis HP : 2,400 HP | Core Body HP: 2,200 HP (Total 4,600 HP)",
        "- Cudgel Weapon HP : 1,600 HP (Modular Destructible Weapon Part)",
        "- Posture Pool     : 240/240 (Dual Threshold Stagger System)",
        "- Stagger 1 Proc   : 60% Posture Strain (144 Posture) / Cudgel Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Terminal Stagger / Cask Ready)",
        "- Primary Attack   : Foreclosure Cudgel Slam & High-Voltage Sweep (Blunt)",
        "---",
        "CONTRABAND ENTITY PROFILE (SE-C-IIIβ-015 'DEBT SCALE'):",
        "- Entity HP Pool   : 3,200 HP | Posture Pool: 240/240",
        "- Total Combined   : 7,200 Encounter HP",
        "- Attack Affinity  : Judicial Obligation Weighing & Void Judgement (Void)"
    ])

    hud_t01 = make_box("TACTICAL STAGE HUD: OPERATION 04 — BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 — ZONE C USURY VAULT REPOSITORY]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER][TAEHO] [JOON]  [SOOJIN][MANSIK] [YUNA]  [MINHO] [CIVS]          [SCALE] ",
        "                                 [CUDGEL]                         [ECHO]  ",
        "---",
        "- Node 01: Breach Entry / Class-II Armored Cruiser 'The Iron Vanguard'",
        "- Node 02: Commander Taeho (Vanguard Band 1 / Phalanx Bastion Obsidian)",
        "- Node 03: Engineer Joon (Point-Blank Band 1 / Deployable Mantlet Barrier)",
        "- Node 04: Handler Soojin (Close Skirmish Band 2 / Resonance Damping Sphere)",
        "- Node 05: High Usurer Man-sik & Cudgel (Central Golden Dais)",
        "- Node 06: Auditor Yuna (Mid-Field Band 3 / Financial Terminal Freeze)",
        "- Node 07: Investigator Minho (Mid-Field Band 3 / Mnemonic Sniper Rafter)",
        "- Node 08: Debtor Holding Cages (32 Indentured Citizen Debtors)",
        "- Node 10: SE-C-IIIβ-015 'Debt Scale' & Infiltrator Echo (Tray Stealth)",
        "---",
        "- Taeho       : Spd 4 -> 2 AP | HP 4,400/4,400 | SP 45/50 | Posture 180/180",
        "- Joon        : Spd 5 -> 3 AP | HP 3,800/3,800 | SP 40/40 | Posture 150/150",
        "- Yuna        : Spd 7 -> 4 AP | HP 2,700/2,700 | SP 50/50 | Posture 100/100",
        "- Minho       : Spd 7 -> 4 AP | HP 2,900/2,900 | SP 45/45 | Posture 110/110",
        "- Soojin      : Spd 5 -> 3 AP | HP 3,600/3,600 | SP 50/50 | Posture 140/140",
        "- Echo        : Spd 9 -> 5 AP | HP 2,600/2,600 | SP 40/40 | Posture 90/90 [STEALTH]",
        "- Man-sik Rig : Spd 4 -> 2 AP | HP 2,400/2,400 | Posture 240/240 [GOLD-PLATED]",
        "- Cudgel Part : Spd 3 -> 1 AP | HP 1,600/1,600 | Posture 140/140 [CHARGED]",
        "- Debt Scale  : Spd 5 -> 3 AP | HP 3,200/3,200 | Posture 240/240 [CAGED]"
    ])

    hud_t02 = make_box("TACTICAL STAGE HUD: OPERATION 04 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — CUDGEL SAPPING & LEDGER DECRYPTION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER][TAEHO] [JOON]  [SOOJIN][MANSIK] [YUNA]  [MINHO] [CIVS]  [ECHO]  [SCALE] ",
        "                                 [CUDGEL]                                 ",
        "---",
        "- Node 02: Commander Taeho (Advancing to Node 03 / Concussive Shield Bash)",
        "- Node 03: Engineer Joon (Hydraulic Kinetic Ram Smashes Cudgel Conduit)",
        "- Node 04: Handler Soojin (Leaded Snare Restricting Scale Dish Tilting)",
        "- Node 05: High Usurer Man-sik (Rig 1,690/2,400 / Cudgel 1,060/1,600)",
        "- Node 06: Auditor Yuna (Cipher-Pulse Disrupting Void Obligation Frequency)",
        "- Node 07: Investigator Minho (Memory Anchor Restoring Squad Composure)",
        "- Node 09: Infiltrator Echo (High Cable Tray Flank behind Dais)",
        "- Node 10: SE-C-IIIβ-015 'Debt Scale' (2,910/3,200 HP / Bone Dish Hum)",
        "---",
        "- Joon        : Spd 7 -> 4 AP [SURGE] | HP 3,800/3,800 | SP 40/40 | Posture 150/150",
        "- Minho       : Spd 9 -> 5 AP [SURGE] | HP 2,900/2,900 | SP 50/50 | Posture 110/110",
        "- Man-sik Rig : Spd 3 -> 1 AP | HP 1,690/2,400 | Posture 176/240 [CONDUIT CRACKED]",
        "- Cudgel Part : Spd 2 -> 1 AP | HP 1,060/1,600 | Posture 76/140 [STRAINED]",
        "- Debt Scale  : Spd 4 -> 2 AP | HP 2,910/3,200 | Posture 208/240 [SNARED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: OPERATION 04 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — CUDGEL SHATTER & STAGGER THRESHOLD 1]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER]        [TAEHO] [JOON]  [MANSIK] [YUNA]  [MINHO] [CIVS]  [ECHO]  [SCALE] ",
        "---",
        "- Node 03: Commander Taeho (Heavy Piston Strike Smashes Midas Chest)",
        "- Node 04: Engineer Joon (Thermite Disruption Clamp Igniting Battery)",
        "- Node 05: High Usurer Man-sik (STAGGER LEVEL 1 / CUDGEL DESTROYED)",
        "- Node 06: Auditor Yuna (Debt Ledger Download In Progress)",
        "- Node 07: Investigator Minho (Synaptic Pierce Dismantles Cudgel Core)",
        "- Node 09: Infiltrator Echo (Driving Eclipse Stiletto into Servo Joints)",
        "- Node 10: SE-C-IIIβ-015 'Debt Scale' (Void Mist Churning)",
        "---",
        "- Taeho       : Spd 6 -> 3 AP [SURGE] | HP 4,400/4,400 | SP 48/50 | Posture 180/180",
        "- Man-sik Rig : Spd 0 -> 0 AP | HP 410/2,400   | Posture 88/240 [STAGGER LEVEL 1]",
        "- Cudgel Part : DESTROYED (0/1,600 HP)",
        "- Debt Scale  : Spd 5 -> 3 AP | HP 2,910/3,200 | Posture 208/240"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: OPERATION 04 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — BERSERK DEBT SCALE & LEADED SANCTUARY WARD]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER]        [TAEHO] [JOON]  [MANSIK] [SOOJIN][YUNA]  [CIVS]  [ECHO]  [SCALE] ",
        "                                                  [MINHO]                 ",
        "---",
        "- Node 03: Commander Taeho (Shielding Debtor Cages & Captives)",
        "- Node 04: Engineer Joon (Pneumatic Pry Bar Unlatching Debtor Cells)",
        "- Node 05: High Usurer Man-sik (Recovered / Pulling Safety Lever on Scale)",
        "- Node 06: Handler Soojin (Leaded Sanctuary Ward Enclosing Squad)",
        "- Node 07: Auditor Yuna & Minho (Freezing 120 Cartel Shell Bank Accounts)",
        "- Node 08: 32 Indentured Captives (Cognitive Shields Holding Intact)",
        "- Node 10: SE-C-IIIβ-015 'Debt Scale' (BERSERK STATE / Void Judgement)",
        "---",
        "- Soojin      : Spd 7 -> 4 AP [SURGE] | HP 3,600/3,600 | SP 50/50 | Posture 140/140",
        "- Man-sik Rig : Spd 2 -> 1 AP | HP 410/2,400   | Posture 62/240",
        "- Debt Scale  : Spd 6 -> 4 AP | HP 2,390/3,200 | Posture 136/240 [BERSERK]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: OPERATION 04 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — PHANTOM SEVER & TERMINAL STAGGER]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER]        [TAEHO] [JOON]  [MANSIK] [SOOJIN][YUNA]  [CIVS]          [SCALE] ",
        "                                                  [MINHO]         [ECHO]  ",
        "---",
        "- Node 03: Commander Taeho (Priming Iron Gavel for Cockpit Breach)",
        "- Node 04: Engineer Joon (Tearing Away Buckled Midas Exoskeleton Struts)",
        "- Node 05: Man-sik Rig (TERMINAL STAGGER / POSTURE 0/240 / CRUSHED)",
        "- Node 06: Handler Soojin (Aligning Class-IV Leaded Cryo-Cask at Dais)",
        "- Node 07: Investigator Minho (Silver Lancet Stripping Obligation Core)",
        "- Node 09: Infiltrator Echo (Eclipse Stiletto Phantom Sever on Sinew)",
        "- Node 10: SE-C-IIIβ-015 'Debt Scale' (TERMINAL STAGGER / POSTURE 0/240)",
        "---",
        "- Echo        : Spd 11 -> 5 AP [MOMENTUM CRIT] | HP 2,600/2,600 | SP 40/40",
        "- Man-sik Rig : Spd 0 -> 0 AP | HP 0/2,400     | Posture 0/240 [CHASSIS CRUSHED]",
        "- Debt Scale  : Spd 0 -> 0 AP | HP 1,280/3,200 | Posture 0/240 [TERMINAL STAGGER]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: OPERATION 04 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX OVERDRIVE: IRON GAVEL & CRYO-SEAL]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER]                [JOON]  [TAEHO]  [SOOJIN][YUNA]  [CIVS]          [CASK]  ",
        "                                 [MANSIK]         [MINHO]         [ECHO]  ",
        "---",
        "- Node 05: High Usurer Man-sik (EXTRACTED UNCONSCIOUS & SECURED)",
        "- Node 06: Auditor Yuna (12,400 Promissory Debt Records Seized & Wiped)",
        "- Node 08: 32 Indentured Debtors (Safely Unlatched / Zero Fatalities)",
        "- Node 10: SE-C-IIIβ-015 'Debt Scale' (100% CONTAINED IN CRYOGENIC CASK)",
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

###### Turn 01 Action Resolution Log (Kinetic Ingress & Golden Cudgel Deflection)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Commander Taeho initializes `[Law of the Mantle]`: All allies within 1 node gain +3 Protection and physical stagger immunity.
  * Infiltrator Echo activates `[Shadow Cloak]`: Enters stealth for 2 turns; cannot be targeted by single-target attacks; +50\% Critical Strike Chance.
  * Handler Soojin initializes `[Resonance Damping Sphere]`, stabilizing the chamber against judicial void pulses from the scale.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Commander Taeho (Speed 4 -> 2 AP, M.A.W.-W Heavy Armor delta -1, Poise +25): Holds Node 02. Spends 2 AP on `[Phalanx Bastion: Obsidian Wall]`.
  * Engineer Joon (Speed 5 -> 3 AP, M.A.W.-W Medium delta 0): Holds Node 03. Spends 2 AP on `[Deployable Mantlet Barrier]`. Holds 1 AP in Reserve.
  * Auditor Yuna (Speed 7 -> 4 AP, M.A.W.-W Light delta +1): Holds Node 06 (Range Band 3). Spends 2 AP on `[Cipher-Scan: Debt Frequency]`, 2 AP on `[Asset Scan]`.
  * Investigator Minho (Speed 7 -> 4 AP, M.A.W.-W Light delta +1): Stands at Node 07. Spends 2 AP on `[Neural Lancet: Calibrated Dart]`. Holds 2 AP in Reserve.
  * Handler Soojin (Speed 5 -> 3 AP, M.A.W.-W Medium delta 0): Holds Node 04. Spends 2 AP on maintaining the damping sphere. Holds 1 AP in Guard.
  * Infiltrator Echo (Speed 9 -> 5 AP, M.A.W.-W Feather delta +2): Slips into vault cable trays toward Node 10 from stealth. Spends 2 AP on positioning.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 02 to 05)**: High Usurer Man-sik unleashes `[Foreclosure Cudgel Slam]` (Base 15 + 2 Coins = 27 Power, Heavy Blunt) against Node 02.
    * Commander Taeho counters with `[Phalanx Bastion: Obsidian Wall]` (Base 17 + 2 Coins = 31 Power, Kinetic Shield).
    * **Clash Outcome**: Taeho WINS THE CLASH (31 vs 27)!
    * The kinetic shield absorbs the electrified golden cudgel blow without buckling (`[P3: Parry/Protection]`).
    * Taeho reflects **170 kinetic tremor damage** back into Man-sik's Midas engine! Inflicts +28 Posture Strain.
  * **Clash 2 (Node 03 to 05)**: Gilded Mercenaries fire `[Pneumatic Coin-Shot Volley]` (Atk Power 21, Pierce).
    * Engineer Joon's `[Deployable Mantlet Barrier]` (Def Power 25, Kinetic Shield).
    * **Clash Outcome**: Joon WINS THE CLASH (25 vs 21).
    * Heavy coin-shot flattens harmlessly against the titanium mantlet; zero damage taken.
  * **Unopposed Ranged Fire**:
    * Auditor Yuna's `[Cipher-Scan]` identifies the high-voltage capacitor coupling inside the cudgel's wrist joint.
    * Investigator Minho fires `[Neural Lancet: Calibrated Dart]` from Node 07 into the Midas exoskeleton shoulder, dealing **250 Pierce damage** and +24 Posture Strain!
    * Handler Soojin's damping sphere suppresses ambient void resonance from the Debt Scale.
- **Step 4: Turn End State**:
  * Man-sik Midas Chassis HP: 2,400 -> **1,980/2,400** (Combined Encounter HP: **6,780/7,200**).
  * Man-sik Posture: 240 -> **188/240**.
  * Squad Composure: **100% (50/50 SP)**. All 6 Officers uninjured.

---

```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Sapping Hydraulic Servos & Ledger Decryption)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Engineer Joon and Investigator Minho both trigger `Momentum Surge` (+2 Speed next turn).
  * Man-sik channels high voltage through his cudgel for an electrified arc sweep: `[High-Voltage Usury Sweep]`.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Engineer Joon (Speed 7 -> 4 AP): Advances from Node 03 to Node 04. Spends 3 AP to unleash `[Hydraulic Kinetic Ram: Structural Sapping]`.
  * Auditor Yuna (Speed 7 -> 4 AP): Moves to Node 06, deploying `[Cipher-Pulse: Frequency Disruptor]` (2 AP) against SE-C-IIIβ-015's balance dish.
  * Commander Taeho (Speed 4 -> 2 AP): Steps to Node 03, executing `[Shield Bash: Kinetic Drive]` (2 AP).
  * Investigator Minho (Speed 9 -> 5 AP): Casts `[Memory Anchor: Cognitive Salve]` (2 AP), reinforcing squad composure (+15 SP).
  * Handler Soojin (Speed 5 -> 3 AP): Flings `[Resonance Snare: Leaded Ring]` (2 AP) around the bone-scale frame.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 04 to 05)**: Man-sik executes `[High-Voltage Usury Sweep]` (Base 13 + 2 Coins = 25 Power, Electric).
    * Engineer Joon executes `[Hydraulic Kinetic Ram]` (Base 17 + 2 Coins = 29 Power, Heavy Blunt).
    * **Clash Outcome**: Joon WINS THE CLASH (29 vs 25)!
    * The hydraulic ram smashes straight into the cudgel's power conduit sleeve!
    * Deals **540 Blunt damage** directly to the Foreclosure Cudgel and inflicts +54 Posture Strain!
  * **Clash 2 (Node 06 to 10)**: SE-C-IIIβ-015 'Debt Scale' pulses `[Judicial Obligation Weighing]` (Power 23, Void).
    * Auditor Yuna unleashes `[Cipher-Pulse: Frequency Disruptor]` (Def Power 27, EMP).
    * **Clash Outcome**: Yuna WINS THE CLASH (27 vs 23).
    * The frequency disruptor stalls the balance dish, dealing **290 Resonance damage** to SE-C-IIIβ-015 and +28 Posture Strain!
  * **Follow-Up Maneuvers**:
    * Taeho's `[Shield Bash]` deals **290 Blunt damage** to the Midas chassis.
    * Minho's cognitive salve restores +15 SP across the strike cadre.
    * Infiltrator Echo severs gold-plated power buses along the vault ceiling, cutting high-voltage feeds to the mercenaries!
- **Step 4: Turn End State**:
  * Man-sik Midas Chassis HP: 1,980 -> **1,690/2,400** | Posture: **176/240 [CONDUIT CRACKED]**.
  * Foreclosure Cudgel Weapon HP: 1,600 -> **1,060/1,600** | Posture: **76/140**.
  * SE-C-IIIβ-015 Debt Scale HP: 3,200 -> **2,910/3,200** | Posture: **208/240**.
  * Combined Encounter HP: **5,660/7,200** | Squad Composure: **98%**.

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Precision Lancet Pierce & Stagger Threshold 1)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Commander Taeho's `Momentum Surge` activates (+2 Speed next turn -> Net Speed 6, 3 AP).
  * Man-sik attempts his lethal execution sweep: `[Absolute Foreclosure Slam]`.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Investigator Minho (Speed 9 -> 5 AP): Positions on an elevated cable tray at Node 07. Spends 3 AP on `[Neural Lancet: Synaptic Pierce]`.
  * Commander Taeho (Speed 6 -> 3 AP): Charges from Node 03 to Node 05, unleashing `[Heavy Piston Strike]` (2 AP).
  * Engineer Joon (Speed 7 -> 4 AP): Plants `[Thermite Disruption Clamp]` (2 AP) directly on the cudgel battery capacitor.
  * Infiltrator Echo (Speed 9 -> 5 AP): Drops from high cable trays onto the cudgel's wrist joint, driving `[Eclipse Stiletto]` (2 AP).
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 07 to 05)**: Man-sik unleashes `[Absolute Foreclosure Slam]` (Base 16 + 2 Coins = 28 Power, Heavy Blunt).
    * Investigator Minho fires `[Neural Lancet: Synaptic Pierce]` (Base 20 + 2 Coins = 32 Power, High-Precision Pierce).
    * **Clash Outcome**: Minho WINS THE CLASH (32 vs 28)!
    * Minho's silver lancet pierces the main capacitor core of the cudgel with microscopic precision!
    * **TARGETED PART DESTROYED**: `[The Foreclosure Cudgel Arm]` explodes in a shower of golden sparks and molten copper (**1,060 Cudgel HP destroyed: 0/1,600**)!
  * **STAGGER THRESHOLD 1 TRIGGERED!**
    * Combined Target HP drops below 60% (4,320 HP), and Man-sik's Posture falls past the 60% strain line!
    * **STAGGER LEVEL 1 ACTIVE!** Man-sik's Midas rig loses all defense, taking 1.5x direct damage. All enemy counter-stances cancelled!
  * **Punishment Strike Phase**:
    * Commander Taeho's `[Heavy Piston Strike]` delivers **480 Blunt damage** to the exposed chest plate.
    * Engineer Joon's thermite clamp burns through the auxiliary servos for **420 Thermal damage**.
    * Infiltrator Echo's `[Eclipse Stiletto]` slices hydraulic tendons for **380 Slash damage**.
- **Step 4: Turn End State**:
  * Man-sik Midas Chassis HP: 1,690 -> **410/2,400** (Chassis critically buckled!).
  * Foreclosure Cudgel Weapon: **0/1,600 [DESTROYED]**.
  * Combined Encounter HP: **3,320/7,200** | Posture: **88/240 [STAGGER LEVEL 1]**.
  * Squad Composure: **100% (50/50 SP)**.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Void Judgement Surge & Leaded Sanctuary Ward)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Recovering from Stagger, Man-sik pulls the emergency debt-resonance lever on SE-C-IIIβ-015 at Node 10!
  * **ENCOUNTER EVENT**: SE-C-IIIβ-015 'The Debt Scale' enters **Berserk State** (+4 Attack Power)!
  * The bone dishes tilt violently; crushing void gravity waves ripple across the vault floor.
  * Handler Soojin's `Momentum Surge` activates (+2 Speed -> Net Speed 7, 4 AP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Handler Soojin (Speed 7 -> 4 AP): Moves to Node 06, deploying `[Leaded Sanctuary Ward: Vacuum Dome]` (3 AP) enclosing the squad and debtor holding cells.
  * Commander Taeho (Speed 4 -> 2 AP): Steps to Node 03, locking his Obsidian shield in front of the debtor pens.
  * Auditor Yuna (Speed 7 -> 4 AP): Hacks the central ledger terminal at Node 06, freezing 120 shadow bank accounts (2 AP).
  * Investigator Minho (Speed 7 -> 4 AP): Dispenses `[Neuro-Stabilizing Aerosol]` (2 AP) to protect debtor sanity.
  * Engineer Joon (Speed 5 -> 3 AP): Uses pneumatic pry bar at Node 04 to pop open the reinforced debtor cell doors (2 AP).
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 10 to 06)**: Berserk SE-C-IIIβ-015 unleashes `[Absolute Foreclosure: Gravitic Void Surge]` (Base 23 + 2 Coins = 33 Power, Area Void).
    * Handler Soojin deploys `[Leaded Sanctuary Ward]` (Base 26 + 2 Coins = 36 Power, Vacuum Barrier).
    * **Clash Outcome**: Soojin WINS THE CLASH (36 vs 33)!
    * The lead-lined vacuum sphere fully captures the crushing void gravity wave (`[P3: Parry/Protection]`).
    * Zero void distortion breaches the leaded barrier. Soojin redirects the trapped resonance into the scale dishes, dealing **520 Void damage** and +72 Posture Strain!
- **Step 4: Turn End State**:
  * Man-sik Midas Chassis HP: **410/2,400** | Posture: **62/240**.
  * SE-C-IIIβ-015 Debt Scale HP: 2,910 -> **2,390/3,200** | Posture: **136/240**.
  * Combined Encounter HP: **2,800/7,200** | Squad Composure: **96%**.

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Phantom Stiletto Sever & Terminal Stagger Threshold 2)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Infiltrator Echo readies `[Eclipse Stiletto: Phantom Sever]` from the overhead cable trays (+50% Crit Chance, ignores 100% defense).
  * Investigator Minho targets the entity's central fulcrum fulcrum bearing.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Infiltrator Echo (Speed 11 -> 5 AP, Momentum + Stealth Boost): Drops from the high trays onto Node 10. Spends 3 AP on `[Phantom Sever]`.
  * Investigator Minho (Speed 7 -> 4 AP): Fires `[Silver Lancet: Cognitive Disruptor]` from Node 07 into the exposed fulcrum bearing (2 AP).
  * Engineer Joon (Speed 5 -> 3 AP): Smashes away Man-sik's remaining chassis supports at Node 04 (2 AP).
  * Auditor Yuna (Speed 7 -> 4 AP): Finalizes forensic download of 12,400 predatory debt contracts at Node 06 (2 AP).
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 10)**: SE-C-IIIβ-015 lashes out with `[Gilded Obligation Guillotine]` (Atk Power 29, Void/Slash).
    * Infiltrator Echo executes `[Eclipse Stiletto: Phantom Sever]` (Base 24 + 2 Coins Heads = 34 Power, Slash).
    * **Clash Outcome**: Echo WINS THE CLASH (34 vs 29)!
    * Echo slices cleanly through the gold-sinew cables connecting the two bone balance pans!
    * **CRITICAL HIT!** Deals **660 Slash damage** directly to the core and strips 90 Posture points!
  * **Targeted Fire**:
    * Investigator Minho's `[Silver Lancet]` strikes the central fulcrum bearing, dealing **450 Freezing Pierce damage** and wiping out the entity's remaining Posture!
    * Engineer Joon demolishes the buckled Midas chassis with the pneumatic ram, dealing **410 Blunt damage** and crushing the exoskeleton completely (Rig HP: 0/2,400)!
- **Step 4: TERMINAL STAGGER THRESHOLD 2 TRIGGERED!**:
  * Both Man-sik and SE-C-IIIβ-015 reach **Posture 0/240** and **0/240**!
  * **TERMINAL STAGGER ACTIVE!** Man-sik collapses under hydraulic collapse, pinned to the floor plates. SE-C-IIIβ-015's balance pans hit the dais, its void aura extinguishing into cold ash.
  * Combined Encounter HP drops below 20% (Total HP: **1,280/7,200**).
- **Step 5: Turn End State**:
  * Man-sik Midas Chassis HP: **0/2,400 [CHASSIS CRUSHED]** | Posture: **0/240**.
  * SE-C-IIIβ-015 Debt Scale HP: **1,280/3,200** | Posture: **0/240 [TERMINAL STAGGER]**.
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
  * Commander Taeho (Speed 4 -> 2 AP): Steps up to Node 05, standing over Man-sik's pinned chassis. Spends 2 AP on Climax Overdrive.
  * Handler Soojin (Speed 5 -> 3 AP): Wheels the Class-IV Cryogenic Leaded Cask directly beneath the Debt Scale fulcrum at Node 10. Spends 3 AP on Climax Containment.
  * Engineer Joon and Infiltrator Echo: Unlatch the final cell doors on the 32 indentured debtors at Node 08, wrapping them in thermal mantlets.
  * Auditor Yuna: Verifies Level-5 encryption on the 12,400 seized debt drives at Node 06, executing immediate debt nullification scripts.
- **Step 3: Climax Overdrive Executions**:
  * **Climax 1 (Commander Taeho vs High Usurer Man-sik)**:
    * Taeho raises his heavy obsidian shield, channeling a 120 dB directed concussive wave: `[Iron Gavel: Decreed Subjugation]` (Power 42).
    * Smashes the reinforced golden helmet visor cleanly along pre-existing stress fractures.
    * The golden plate fractures away safely; non-lethal kinetic tremor renders Man-sik unconscious.
    * **HIGH USURER MAN-SIK EXTRACTED & INCAPACITATED!** Remanded to Warden custody!
  * **Climax 2 (Handler Soojin vs SE-C-IIIβ-015 'The Debt Scale')**:
    * Soojin clamps the leaded seal collar onto the Debt Scale fulcrum, triggering absolute sub-zero cryogenic vacuum suction: `[Vault of Solitude]` (Power 40).
    * All swirling void emotional vapors are sucked into the leaded cask within 4.1 seconds! Zero atmospheric leakage detected.
    * The hydraulic locking pins engage with a heavy metallic boom: **CRYOGENIC VACUUM SEAL COMPLETE**.
    * **SE-C-IIIβ-015 HP DROPS TO 0!** Fully contained in inert dormancy and logged for transfer to Reverie Directorate Floor 2!
- **Step 4: Pacification & Operational Outcome**:
  * **High Usurer Man-sik**: Midas chassis demolished; usurer safely secured in Warden custody.
  * **Electrified Foreclosure Cudgel**: 100% destroyed.
  * **SE-C-IIIβ-015 'The Debt Scale'**: 100% contained in cryogenic lead cask. Zero leakage.
  * **Civilian Debtors**: 32 citizens liberated and all predatory contracts legally incinerated.
  * **Evidence**: 12,400 promissory contracts and 840 kg of illicit bullion seized.
"""

def update_operation_4():
    path = "SOMNARAK-WORLD/Katharcheok/Operation_4_Usurachae.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    start_str = "### Tactical Engagement: 6-Turn Pacification Gauntlet"
    end_str = "### Post-Action Forensic Inventory"

    start_idx = content.find(start_str)
    end_idx = content.find(end_str)

    if start_idx == -1 or end_idx == -1:
        print(f"Error: Could not locate boundaries! start_idx={start_idx}, end_idx={end_idx}")
        return

    new_engagement = get_op4_engagement() + "\n\n"
    new_content = content[:start_idx] + new_engagement + content[end_idx:]

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Updated Operation 4 successfully!")

if __name__ == "__main__":
    update_operation_4()
