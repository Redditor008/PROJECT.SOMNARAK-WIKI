#!/usr/bin/env python3
"""
tools/expand_katharcheok_op1.py
Expands Operation 1 (Velumtal - The Mask Market Raid) in SOMNARAK-WORLD/Katharcheok/Operation_1_Velumtal.md
Replaces the older summary/compressed boxes in ## Engagement Protocol: The Lapidary Vault Siege
with full 10-node spatial tactical HUDs, Speed/AP breakdowns, M.A.W.-W weight deltas,
and Four P-framework action resolution logs across all 6 turns.
"""

import sys, os
sys.path.append(os.path.dirname(__file__))
from box_formatter import make_box

def get_op1_engagement():
    dossier_box = make_box("TARGET DOSSIER: THE FALSE WEAVER & CONTRABAND SHROUD", [
        "APEX TARGET        : Boss Gwangseok ('The Mask Weaver')",
        "ACCOMPANIMENT      : SECC-019 Contraband Sorrow Entity ('The False Shroud')",
        "ESCORT MINIONS     : Foundry Enforcers (x2) & Slag Pourers",
        "ENCOUNTER DOMAIN   : Zone D Mantle Commons Sub-Vault 4 (-25m Depth)",
        "---",
        "BOSS COMBAT PROFILE:",
        "- Total HP Pool    : 5,400 HP (Exoskeleton: 1,800 | Core Body: 3,600)",
        "- Posture Pool     : 240/240 (Dual Threshold Stagger System)",
        "- Stagger 1 Proc   : 60% Posture Strain (144 Posture) / 3,800 HP",
        "- Stagger 2 Proc   : 0% Posture Collapse (Terminal Stagger / Cask Ready)",
        "- Primary Armament : Industrial Pneumatic Sledgehammer (Heavy Blunt)",
        "- Defense Matrix   : Counterfeit Veil Cloak & Vapor Shroud (Evasion/Pale)",
        "---",
        "CONTRABAND ENTITY PROFILE (SECC-019):",
        "- Entity HP Pool   : 2,400 HP | Posture Pool: 180/180",
        "- Entity Threat    : Rank II/III Sub-Municipal Contraband",
        "- Attack Affinity  : Grief Vapor Shroud (Psychic / Pale Delusion)"
    ])

    hud_t01 = make_box("TACTICAL STAGE HUD: OPERATION 01 — BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 — ZONE D SUB-VAULT 4 FOUNDRY BREACH]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER][TAEHO] [JOON]  [SOOJIN][BOSS]   [YUNA]  [MINHO] [CIVS]          [SECC]  ",
        "                                 [ENF-1]                          [ECHO]  ",
        "---",
        "- Node 01: Breach Entry / Class-II Armored Cruiser 'The Iron Vanguard'",
        "- Node 02: Commander Taeho (Vanguard Band 1 / Phalanx Bastion Raised)",
        "- Node 03: Engineer Joon (Point-Blank Band 1 / Deployable Alloy Mantlet)",
        "- Node 04: Handler Soojin (Close Skirmish Band 2 / Resonance Snare)",
        "- Node 05: Boss Gwangseok & Enforcer 1 (Central Foundry Anvil Core)",
        "- Node 06: Auditor Yuna (Mid-Field Band 3 / Forensic Wiretap Console)",
        "- Node 07: Investigator Minho (Mid-Field Band 3 / Mnemonic Sniper Berth)",
        "- Node 08: Hostage Pens (12 Captive Civilian Mask-Carvers)",
        "- Node 10: SECC-019 'False Shroud' & Infiltrator Echo (Shadow Stealth)",
        "---",
        "- Taeho       : Spd 4 -> 2 AP | HP 4,400/4,400 | SP 45/50 | Posture 180/180",
        "- Joon        : Spd 5 -> 3 AP | HP 3,800/3,800 | SP 40/40 | Posture 150/150",
        "- Yuna        : Spd 7 -> 4 AP | HP 2,700/2,700 | SP 50/50 | Posture 100/100",
        "- Minho       : Spd 7 -> 4 AP | HP 2,900/2,900 | SP 45/45 | Posture 110/110",
        "- Soojin      : Spd 5 -> 3 AP | HP 3,600/3,600 | SP 50/50 | Posture 140/140",
        "- Echo        : Spd 9 -> 5 AP | HP 2,600/2,600 | SP 40/40 | Posture 90/90 [STEALTH]",
        "- Gwangseok   : Spd 4 -> 2 AP | HP 5,400/5,400 | Posture 240/240 [ARMORED]",
        "- SECC-019    : Spd 5 -> 3 AP | HP 2,400/2,400 | Posture 180/180 [CAGED]"
    ])

    hud_t02 = make_box("TACTICAL STAGE HUD: OPERATION 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — CLOAKING SHATTER & EMP OVERLOAD]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER][TAEHO] [JOON]  [SOOJIN][BOSS]   [YUNA]  [MINHO] [CIVS]  [ECHO]  [SECC]  ",
        "---",
        "- Node 02: Commander Taeho (Maintaining Kinetic Phalanx Wall)",
        "- Node 03: Engineer Joon (Hydraulic Piston Sapping Jack Primed)",
        "- Node 04: Handler Soojin (Leaded Snare Binding SECC-019 Tendrils)",
        "- Node 05: Boss Gwangseok (Exoskeleton 1,130/1,800 / Evasion 0%)",
        "- Node 06: Auditor Yuna (Veil EMP Disruptor Discharged / Overload)",
        "- Node 07: Investigator Minho (Targeting Pneumatic Sledgehammer Hub)",
        "- Node 09: Infiltrator Echo (Shadow Catwalk Flank behind Dais)",
        "- Node 10: SECC-019 (Grief Shroud Agitated / Siphon Conduits Exposed)",
        "---",
        "- Taeho       : Spd 4 -> 2 AP | HP 4,400/4,400 | SP 45/50 | Posture 180/180",
        "- Joon        : Spd 5 -> 3 AP | HP 3,800/3,800 | SP 40/40 | Posture 150/150",
        "- Yuna        : Spd 9 -> 5 AP [SURGE] | HP 2,700/2,700 | SP 50/50 | Posture 100/100",
        "- Minho       : Spd 7 -> 4 AP | HP 2,900/2,900 | SP 45/45 | Posture 110/110",
        "- Soojin      : Spd 5 -> 3 AP | HP 3,600/3,600 | SP 50/50 | Posture 140/140",
        "- Echo        : Spd 9 -> 5 AP | HP 2,600/2,600 | SP 40/40 | Posture 90/90 [STEALTH]",
        "- Gwangseok   : Spd 3 -> 1 AP | HP 4,730/5,400 | Posture 186/240 [EMP OVERLOAD]",
        "- SECC-019    : Spd 4 -> 2 AP | HP 2,120/2,400 | Posture 152/180 [SNARED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: OPERATION 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — HAMMER SHATTER & STAGGER THRESHOLD 1]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER]        [TAEHO] [JOON]  [BOSS]   [YUNA]  [MINHO] [CIVS]  [ECHO]  [SECC]  ",
        "---",
        "- Node 03: Commander Taeho & Engineer Joon (Advancing to Node 04)",
        "- Node 05: Boss Gwangseok (STAGGER LEVEL 1 / HAMMER DESTROYED)",
        "- Node 06: Auditor Yuna (Debt Foreclosure Beam Locked on Exoskeleton)",
        "- Node 07: Investigator Minho (Cryo-Needle Piercing Hydraulic Core)",
        "- Node 09: Infiltrator Echo (Stiletto Primed at Entity Siphon Tubes)",
        "- Node 10: SECC-019 (Sorrow Valve Fluttering / Agitation Rising)",
        "---",
        "- Taeho       : Spd 6 -> 3 AP [SURGE] | HP 4,400/4,400 | SP 48/50 | Posture 180/180",
        "- Joon        : Spd 7 -> 4 AP [SURGE] | HP 3,800/3,800 | SP 40/40 | Posture 150/150",
        "- Gwangseok   : Spd 0 -> 0 AP | HP 3,750/5,400 | Posture 92/240 [STAGGER LEVEL 1]",
        "- SECC-019    : Spd 4 -> 2 AP | HP 2,120/2,400 | Posture 152/180 [RESTRICTED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: OPERATION 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — ENTITY BERSERK & LEADED DAMPING BUBBLE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER]        [TAEHO] [JOON]  [BOSS]   [SOOJIN][YUNA]  [CIVS]  [ECHO]  [SECC]  ",
        "                                                  [MINHO]                 ",
        "---",
        "- Node 03: Commander Taeho (Baton Counter vs Recovered Brawler Punch)",
        "- Node 04: Engineer Joon (Shoring Up Structural Catwalk Supports)",
        "- Node 05: Boss Gwangseok (Exoskeleton Shattered / Desperate Brawler)",
        "- Node 06: Handler Soojin (Leaded Damping Bubble Covering Squad)",
        "- Node 07: Auditor Yuna & Minho (Restoring Composure / Mnemonic Anchor)",
        "- Node 08: Civilian Hostage Berths (Fully Shielded by Leaded Barrier)",
        "- Node 10: SECC-019 (BERSERK RAGE / Delusion of the False Sky)",
        "---",
        "- Taeho       : Spd 4 -> 2 AP | HP 4,400/4,400 | SP 50/50 | Posture 180/180",
        "- Soojin      : Spd 7 -> 4 AP [SURGE] | HP 3,600/3,600 | SP 50/50 | Posture 140/140",
        "- Gwangseok   : Spd 3 -> 1 AP | HP 2,980/5,400 | Posture 58/240 [UNARMORED]",
        "- SECC-019    : Spd 6 -> 3 AP | HP 1,980/2,400 | Posture 94/180 [BERSERK]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: OPERATION 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — PHANTOM SEVER & TERMINAL STAGGER]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER]        [TAEHO] [JOON]  [BOSS]   [SOOJIN][YUNA]  [CIVS]          [SECC]  ",
        "                                                  [MINHO]         [ECHO]  ",
        "---",
        "- Node 03: Commander Taeho (Priming Iron Verdict on Boss)",
        "- Node 05: Boss Gwangseok (TERMINAL STAGGER / POSTURE 0/240)",
        "- Node 06: Handler Soojin (Rolling Class-IV Vacuum Cask into Position)",
        "- Node 07: Investigator Minho (Neural Inscription Lance Firing)",
        "- Node 09: Infiltrator Echo (Stiletto Sever from Stealth on Core)",
        "- Node 10: SECC-019 (TERMINAL STAGGER / POSTURE 0/180 / SHROUD COLLAPSED)",
        "---",
        "- Taeho       : Spd 4 -> 2 AP | HP 4,400/4,400 | SP 50/50 | Posture 180/180",
        "- Echo        : Spd 11 -> 5 AP [MOMENTUM CRIT] | HP 2,600/2,600 | SP 40/40",
        "- Gwangseok   : Spd 0 -> 0 AP | HP 600/5,400   | Posture 0/240 [COLLAPSED]",
        "- SECC-019    : Spd 0 -> 0 AP | HP 850/2,400   | Posture 0/180 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: OPERATION 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — OVERDRIVE PACIFICATION & CASK SEAL]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER]                [JOON]  [TAEHO]  [SOOJIN][YUNA]  [CIVS]          [CASK]  ",
        "                                 [BOSS]           [MINHO]         [ECHO]  ",
        "---",
        "- Node 05: Boss Gwangseok (SUBDUED & ARRESTED / Concussive Lock)",
        "- Node 06: Auditor Yuna (Ledgers Downloaded / 100% Asset Seizure)",
        "- Node 08: 12 Civilian Mask-Carvers (Liberated / Zero Casualties)",
        "- Node 10: SECC-019 (SEALED IN LEAD CASK / Handoff to RD Floor 2 Ready)",
        "---",
        "- Strike Cadre: Zero Fatalities | Composure 50/50 SP (Lucidity)",
        "- Boss & Entity: HP 0 / 5,400 & 0 / 2,400 [100% PACIFIED & SECURED]"
    ])

    return f"""## Engagement Protocol: The Lapidary Vault Siege

```text
{dossier_box}
```

---

```text
{hud_t01}
```

###### Turn 01 Action Resolution Log (Kinetic Ingress & Phalanx Lockdown)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Commander Taeho initializes `[Law of the Mantle]`: All allies within 1 node gain +3 Protection and immune to physical stagger.
  * Infiltrator Echo activates `[Shadow Cloak]`: Enters stealth for 2 turns; cannot be targeted by single-target attacks; +50\% Critical Strike Chance.
  * Engineer Joon plants *Deployable Mantlet Barrier* at Node 03, giving Range Band 1 protection against slag spray.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Commander Taeho (Speed 4 -> 2 AP, M.A.W.-W Heavy Armor delta -1, Poise +25): Holds Node 02. Spends 2 AP on `[Phalanx Bastion: Obsidian Wall]`.
  * Engineer Joon (Speed 5 -> 3 AP, M.A.W.-W Medium delta 0): Holds Node 03. Spends 2 AP on `[Magnetic Barricade]`. Holds 1 AP in Reserve.
  * Auditor Yuna (Speed 7 -> 4 AP, M.A.W.-W Light delta +1): Holds Node 06 (Range Band 3). Spends 2 AP on `[Forensic Monocle Analysis]`, 2 AP on `[Asset Scan]`.
  * Investigator Minho (Speed 7 -> 4 AP, M.A.W.-W Light delta +1): Stands at Node 07. Spends 2 AP on `[Neural Needle: Calibrated Dart]`. Holds 2 AP in Reserve.
  * Handler Soojin (Speed 5 -> 3 AP, M.A.W.-W Medium delta 0): Holds Node 04. Spends 2 AP on `[Resonance Snare: Leaded Line]`. Holds 1 AP in Guard.
  * Infiltrator Echo (Speed 9 -> 5 AP, M.A.W.-W Feather delta +2): Advances through high catwalk conduits to Node 10 from stealth. Spends 2 AP on positioning.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 02 to 05)**: Boss Gwangseok declares `[Anvil Cleave]` (Base 12 + 2 Coins = 24 Power, Heavy Blunt) against Node 02.
    * Commander Taeho counters with `[Phalanx Bastion]` (Base 14 + 2 Coins = 28 Power, Kinetic Shield).
    * **Clash Outcome**: Taeho WINS THE CLASH (28 vs 24)!
    * Taeho's heavy obsidian mantlet completely absorbs the kinetic shock (`[P3: Parry/Protection]`).
    * Reflects **140 kinetic tremor damage** back into Gwangseok's pneumatic chassis! Inflicts +24 Posture Strain.
  * **Clash 2 (Node 03 to 05)**: Foundry Enforcers unleash `[Pressurized Slag Throw]` (Atk Power 18, Thermal Burn).
    * Engineer Joon's `[Magnetic Barricade]` (Def Power 22, Alloy Shield).
    * **Clash Outcome**: Joon WINS THE CLASH (22 vs 18).
    * Slag is deflected into the drainage trough; zero damage taken.
  * **Unopposed Ranged Fire**:
    * Auditor Yuna's `[Forensic Monocle]` identifies structural stress fissures in the Forging Hammer junction.
    * Investigator Minho fires `[Neural Needle]` from Node 07 into Gwangseok's hydraulic neck ring, dealing **210 Pierce damage** and +18 Posture Strain!
    * Handler Soojin flings `[Resonance Snare]` from Node 04, latching onto SECC-019's containment cage at Node 10, preventing emotional mist expansion.
- **Step 4: Turn End State**:
  * Gwangseok Exoskeleton HP: 1,800 -> **1,450/1,800** (Total Boss HP: **5,050/5,400**).
  * Gwangseok Posture: 240 -> **198/240**.
  * Squad Composure: **45/50 SP**. All 6 Officers uninjured.

---

```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (EMP Disruption & Cloaking Shatter)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Auditor Yuna's `Momentum Surge` activates! (+2 Speed next turn -> Net Speed 9, 5 AP).
  * Boss Gwangseok activates *Counterfeit Cloak Burst*, attempting to phase into refractive false-veil stealth (+40% Evasion).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Auditor Yuna (Speed 9 -> 5 AP): Steps to Node 06. Spends 3 AP to fire `[Veil EMP Disruptor: System Overload]`, 2 AP on `[Cipher Freeze]`.
  * Handler Soojin (Speed 5 -> 3 AP): Advances from Node 04 to Node 05 perimeter. Spends 2 AP on `[Leaded Basalt Counter-Pulse]`.
  * Commander Taeho (Speed 4 -> 2 AP): Holds Node 02, maintaining front barrier for Joon.
  * Investigator Minho (Speed 7 -> 4 AP): Focuses optical lens from Node 07 on Gwangseok's hammer joint. Spends 2 AP on `[Neural Lancet]`.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 06 to 05)**: Boss Gwangseok attempts `[Counterfeit Cloak Burst]` (Power 22).
    * Auditor Yuna unleashes `[Veil EMP Disruptor]` (Base 15 + 2 Coins = 27 Power, EMP Overload).
    * **Clash Outcome**: Yuna WINS THE CLASH (27 vs 22)!
    * The EMP wave detonates across Node 05. The false cloaking gems overload, crackling violently before disintegrating into gray mineral ash!
    * Gwangseok suffers **320 Pale Resonance Shock**! Evasion drops permanently to 0%, and Posture takes +38 Strain!
  * **Clash 2 (Node 04 to 10)**: SECC-019 lashes out with `[Grief Vapor Shroud]` (Power 20, Area Psychic).
    * Handler Soojin counters with `[Leaded Basalt Counter-Pulse]` (Def Power 26).
    * **Clash Outcome**: Soojin WINS THE CLASH (26 vs 20).
    * Leaded pulse compresses the grief vapor back toward Node 10, dealing **280 Resonance damage** to SECC-019 and inflicting +28 Posture Strain!
- **Step 4: Turn End State**:
  * Gwangseok Exoskeleton HP: 1,450 -> **1,130/1,800** (Total Boss HP: **4,730/5,400**).
  * Gwangseok Posture: 198 -> **160/240**.
  * SECC-019 HP: 2,400 -> **2,120/2,400** | Posture: 180 -> **152/180**.
  * Squad Composure: **48/50 SP**.

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Hammer Shatter & Stagger Threshold 1)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Commander Taeho and Engineer Joon both trigger `Momentum Surge` (+2 Speed next turn).
  * Boss Gwangseok prepares his maximum kinetic attack: `[Sledgehammer Execution]`.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Engineer Joon (Speed 7 -> 4 AP): Advances from Node 03 to Node 04. Spends 3 AP to unleash `[Hydraulic Impact Ram: Structural Sapping]`.
  * Commander Taeho (Speed 6 -> 3 AP): Charges from Node 02 to Node 04, locking mantlets beside Joon. Spends 2 AP on `[Acoustic Crackdown]`.
  * Investigator Minho (Speed 7 -> 4 AP): Fires `[Cryo-Needle]` at hydraulic fuel lines from Node 07 (2 AP).
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 04 to 05)**: Boss Gwangseok declares `[Sledgehammer Execution]` (Base 16 + 2 Coins = 26 Power, Heavy Blunt).
    * Engineer Joon executes `[Hydraulic Impact Ram]` (Base 19 + 2 Coins = 31 Power, Structural Sapping).
    * **Clash Outcome**: Joon WINS THE CLASH (31 vs 26)!
    * The pneumatic ram strikes directly at the hammer's articulated wrist coupling!
    * **TARGETED PART DESTROYED**: `[The Industrial Forging Hammer]` shatters into twisted scrap and hydraulic spray (**1,130 Exoskeleton HP instantly destroyed**)!
    * Severe kinetic recoil tears through Gwangseok's chest chassis, inflicting +68 Posture Strain!
  * **STAGGER THRESHOLD 1 TRIGGERED!**
    * Gwangseok's Posture reaches **92/240** (surpassing the 60% Posture Strain threshold of 144 points), and total HP drops below 3,800 HP!
    * **STAGGER LEVEL 1 ACTIVE!** Gwangseok's defense drops to 0, taking 1.5x direct damage. All enemy counter-stances are cancelled!
  * **Punishment Follow-Up**:
    * Commander Taeho delivers `[Acoustic Crackdown]`, slamming the heavy baton into the exposed torso for **360 Blunt damage (Critical Hit!)**.
    * Investigator Minho lands `[Cryo-Needle]`, freezing ruptured fuel lines for **280 Pierce damage**.
- **Step 4: Turn End State**:
  * Boss Gwangseok HP: 4,730 -> **3,750/5,400** (Exoskeleton completely destroyed: 0/1,800).
  * Gwangseok Posture: **92/240 [STAGGER LEVEL 1]**.
  * Squad Composure: **48/50 SP**.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (The Entity Frenzy & Leaded Damping Bubble)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Desperate and unarmored, Gwangseok smashes the emergency release lever on SECC-019's containment cage at Node 10!
  * **ENCOUNTER EVENT**: SECC-019 enters **Berserk State** (+4 Attack Power, Grief Shroud expands to Nodes 05–10).
  * Handler Soojin's `Momentum Surge` activates (+2 Speed -> Net Speed 7, 4 AP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Handler Soojin (Speed 7 -> 4 AP): Moves to Node 06, deploying `[Leaded Damping Bubble: Vacuum Barrier]` (3 AP) covering Nodes 04–08.
  * Commander Taeho (Speed 4 -> 2 AP): Stands at Node 03, intercepting Gwangseok's desperate charge with `[Baton Parry]` (2 AP).
  * Auditor Yuna (Speed 7 -> 4 AP): Intercepts SECC-019's secondary resonance relay with `[Asset Foreclosure]` (2 AP).
  * Investigator Minho (Speed 7 -> 4 AP): Administers `[Mnemonic Recall Salve]` (2 AP), restoring +15 SP across squad.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 10 to 06)**: Berserk SECC-019 unleashes `[Delusion of the False Sky]` (Base 20 + 2 Coins = 28 Power, Area Psychic Pulse).
    * Handler Soojin deploys `[Leaded Damping Bubble]` (Base 22 + 2 Coins = 30 Power, Vacuum Barrier).
    * **Clash Outcome**: Soojin WINS THE CLASH (30 vs 28)!
    * The lead-lined vacuum sphere expands, fully absorbing the psychic shockwave (`[P3: Parry/Protection]`).
    * Zero psychic damage breaches the barrier. Soojin redirects vacuum back-pressure, dealing **140 Void damage** to SECC-019 and +58 Posture Strain!
  * **Clash 2 (Node 05 to 03)**: Recovered Gwangseok lunges with `[Desperate Brawler Punch]` (Atk Power 16, Blunt).
    * Commander Taeho executes `[Baton Parry]` (Def Power 24, Acoustic Counter).
    * **Clash Outcome**: Taeho WINS THE CLASH (24 vs 16).
    * Taeho deflects the bare fist, smashing Gwangseok back against the cold forge anvil for **180 Blunt damage** and +34 Posture Strain!
  * **Catwalk Maneuver**: Infiltrator Echo positions silently above Node 10 directly behind SECC-019's primary resonance stem.
- **Step 4: Turn End State**:
  * Boss Gwangseok HP: 3,750 -> **2,980/5,400** | Posture: **58/240**.
  * SECC-019 HP: 2,120 -> **1,980/2,400** | Posture: **94/180**.
  * Squad Composure: **50/50 SP (Synchronized Lucidity achieved!)**.

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Neural Inclination & Terminal Stagger)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Infiltrator Echo readies `[Stiletto Sever from Stealth]` (+50% Crit Chance, ignores 100% defense).
  * Investigator Minho primes `[Neural Inscription Lance: Piercing Cryo]`.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Infiltrator Echo (Speed 11 -> 5 AP, Momentum + Stealth Boost): Drops silently from the high catenary pipe onto Node 10. Spends 3 AP on `[Phantom Stiletto Cleave]`.
  * Investigator Minho (Speed 7 -> 4 AP): Fires `[Neural Inscription Lance]` from Node 07 into the entity's exposed resonance valve (3 AP).
  * Engineer Joon (Speed 5 -> 3 AP): Pinning Gwangseok's legs with hydraulic jacks at Node 05 (2 AP).
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 10)**: SECC-019 attempts `[Suffocating False Embrace]` (Atk Power 23, Pierce).
    * Infiltrator Echo strikes with `[Stiletto Sever from Stealth]` (Base 22 + 2 Coins Heads = 32 Power, Slash).
    * **Clash Outcome**: Echo WINS THE CLASH (32 vs 23)!
    * Echo's phase-tuned blades slice cleanly through the synthetic sorrow conduits feeding the shroud!
    * **CRITICAL HIT!** Deals **580 Slash damage** directly to the core and wipes out all remaining Posture!
  * **Targeted Fire**: Investigator Minho's `[Neural Inscription Lance]` strikes the severed valve, delivering **480 Freezing Pierce damage**!
  * Joon's hydraulic jacks crush Gwangseok's remaining support pistons, dealing **380 Blunt damage** and wiping his remaining 58 Posture points!
- **Step 4: TERMINAL STAGGER THRESHOLD 2 TRIGGERED!**:
  * Both Boss Gwangseok and SECC-019 reach **Posture 0/240** and **0/180**!
  * **TERMINAL STAGGER ACTIVE!** Boss Gwangseok collapses to both knees, vomiting bile. SECC-019's false shroud dissolves into inert vapor.
  * Encounter HP drops below 1,800 HP (Total HP: **1,450/5,400**).
- **Step 5: Turn End State**:
  * Boss Gwangseok HP: **600/5,400** | Posture: **0/240 [TERMINAL STAGGER]**.
  * SECC-019 HP: **850/2,400** | Posture: **0/180 [TERMINAL STAGGER]**.
  * Squad Composure: **50/50 SP**.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Overdrive Pacification & Leading Cask Seal)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Commander Taeho charges `[Decree of Unbroken Order — Iron Verdict]` (Cost: 35 SP).
  * Handler Soojin activates `[Quarantine Mandate — Zero Leakage]` (Cost: 35 SP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Commander Taeho (Speed 4 -> 2 AP): Steps up to Node 05, standing over the kneeling cartel boss. Spends 2 AP on the Climax Overdrive.
  * Handler Soojin (Speed 5 -> 3 AP): Wheels the Class-IV Leaded Vacuum Cask directly onto Node 10. Spends 3 AP on the Climax Containment.
  * Engineer Joon and Infiltrator Echo: Secure the 12 civilian hostages at Node 08, wrapping them in thermal mantlets.
  * Auditor Yuna: Plugs cryptographic shunts into Gwangseok's master forge server at Node 06, seizing all counterfeit financial ledgers.
- **Step 3: Climax Overdrive Executions**:
  * **Climax 1 (Commander Taeho vs Boss Gwangseok)**:
    * Taeho unholsters his tungsten truncheon, channeling a 120 dB directed concussive wave: `[Iron Verdict]`.
    * Strikes Gwangseok's collarbone with mathematical non-lethal precision.
    * Deals **600 Concussive Blunt Damage**!
    * **BOSS GWANGSEOK HP DROPS TO 0!** Subdued, handcuffed with reinforced titanium zipties, and remanded to Warden custody!
  * **Climax 2 (Handler Soojin vs SECC-019)**:
    * Soojin unlatches the Class-IV leaded-basalt vacuum cask, triggering high-grade cryogenic suction: `[Quarantine Mandate]`.
    * The swirling emotional vapor of SECC-019 is drawn into the lead vault without a single milliliter of atmospheric leakage!
    * The heavy basalt lid drops with a resounding hydraulic thud: **VACUUM SEAL COMPLETE**.
    * **SECC-019 HP DROPS TO 0!** Fully contained, tagged as `SECC-019-PACIFIED`, and logged for transport to Reverie Directorate Floor 2!
- **Step 4: Pacification & Operational Outcome**:
  * **Boss Gwangseok**: Arrested and interrogated.
  * **SECC-019**: 100% contained in lead cask. Zero casualties.
  * **Civilian Workers**: 12 captive mask-carvers liberated and escorted to *The Iron Vanguard*.
  * **Evidence**: 4,200 counterfeit Veil stones and 14 ledger drives seized.
"""

def update_operation_1():
    path = "SOMNARAK-WORLD/Katharcheok/Operation_1_Velumtal.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the start of ## Engagement Protocol
    start_str = "## Engagement Protocol: The Lapidary Vault Siege"
    end_str = "## Chapter 7: The Aftermath & The Broken Mold"

    start_idx = content.find(start_str)
    end_idx = content.find(end_str)

    if start_idx == -1 or end_idx == -1:
        print(f"Error: Could not locate boundaries! start_idx={start_idx}, end_idx={end_idx}")
        return

    new_engagement = get_op1_engagement() + "\n\n"
    new_content = content[:start_idx] + new_engagement + content[end_idx:]

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Updated Operation 1 successfully!")

if __name__ == "__main__":
    update_operation_1()
