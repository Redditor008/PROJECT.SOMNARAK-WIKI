#!/usr/bin/env python3
"""
tools/expand_katharcheok_op6.py
Expands Operation 6 (Basileugung - The Sunken Citadel) in SOMNARAK-WORLD/Katharcheok/Operation_6_Basileugung.md
Replaces the older summary/compressed boxes in ### Tactical Engagement: 6-Turn Pacification Gauntlet
with full 10-node spatial tactical HUDs, Speed/AP breakdowns, M.A.W.-W weight deltas,
and Four P-framework action resolution logs across all 6 turns.
"""

def make_box(title, rows, width=71):
    top = "+" + "=" * (width - 2) + "+"
    bottom = "+" + "=" * (width - 2) + "+"
    sep = "+" + "-" * (width - 2) + "+"
    
    out = [top]
    if title:
        title_str = f" {title} "
        out.append(f"|{title_str.center(width - 2)}|")
        out.append(sep)
    
    for r in rows:
        if r == "---":
            out.append(sep)
        elif r.startswith("==="):
            out.append(top)
        else:
            text = r[:width - 4]
            out.append(f"| {text.ljust(width - 4)} |")
    out.append(bottom)
    return "\n".join(out)

def get_op6_engagement():
    dossier_box = make_box("TARGET DOSSIER: GRAND PATRIARCH CHEON & SE-C-IIIγ-490", [
        "APEX TARGET        : Grand Patriarch Cheon ('The Sunken King')",
        "MODULAR WEAPON     : Crown Scepter Weapon Arm (Heavy Blunt/Pale Shock)",
        "CONTRABAND ENTITY  : SE-C-IIIγ-490 'The Hollow Knight' (ALEPH Threat)",
        "ESCORT MINIONS     : Royal Guard Enforcers (x2) & Heavy Spearmen",
        "ENCOUNTER DOMAIN   : Zone B Sunken Citadel Royal Throne Room (-350m)",
        "---",
        "BOSS COMBAT PROFILE (GRAND PATRIARCH CHEON):",
        "- Sovereign Rig HP : 2,600 HP | Core Body HP: 2,400 HP (Total 5,000 HP)",
        "- Crown Scepter HP : 1,800 HP (Modular Destructible Weapon Part)",
        "- Posture Pool     : 260/260 (Dual Threshold Stagger System)",
        "- Stagger 1 Proc   : 60% Posture Strain (156 Posture) / Scepter Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Terminal Stagger / Cask Ready)",
        "- Primary Attack   : Sovereign Cleave Slam & Royal Lightning Cleave",
        "---",
        "CONTRABAND ENTITY PROFILE (SE-C-IIIγ-490 'THE HOLLOW KNIGHT'):",
        "- Entity HP Pool   : 3,600 HP | Posture Pool: 260/260",
        "- Total Combined   : 8,000 Encounter HP",
        "- Attack Affinity  : Pale Sunder Storm & Mournful Greatsword (Pale)"
    ])

    hud_t01 = make_box("TACTICAL STAGE HUD: OPERATION 06 — BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 — ZONE B SUNKEN CITADEL THRONE ROOM]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER][TAEHO] [JOON]  [SOOJIN][CHEON]  [YUNA]  [MINHO] [CIVS]          [KNIGHT]",
        "                                 [SCEPTER]                        [ECHO]  ",
        "---",
        "- Node 01: Breach Entry / Class-II Armored Cruiser 'The Iron Vanguard'",
        "- Node 02: Commander Taeho (Vanguard Band 1 / Phalanx Bastion Obsidian)",
        "- Node 03: Engineer Joon (Point-Blank Band 1 / Deployable Mantlet Barrier)",
        "- Node 04: Handler Soojin (Close Skirmish Band 2 / Sedative Aerosol Ward)",
        "- Node 05: Grand Patriarch Cheon & Crown Scepter (Central Royal Throne)",
        "- Node 06: Auditor Yuna (Mid-Field Band 3 / Financial Terminal Freeze)",
        "- Node 07: Investigator Minho (Mid-Field Band 3 / Mnemonic Sniper Arch)",
        "- Node 08: Hostage Berths (16 Municipal Council Delegates & Aides)",
        "- Node 10: SE-C-IIIγ-490 Hollow Knight & Infiltrator Echo (Arch Stealth)",
        "---",
        "- Taeho       : Spd 4 -> 2 AP | HP 4,400/4,400 | SP 45/50 | Posture 180/180",
        "- Joon        : Spd 5 -> 3 AP | HP 3,800/3,800 | SP 40/40 | Posture 150/150",
        "- Yuna        : Spd 7 -> 4 AP | HP 2,700/2,700 | SP 50/50 | Posture 100/100",
        "- Minho       : Spd 7 -> 4 AP | HP 2,900/2,900 | SP 45/45 | Posture 110/110",
        "- Soojin      : Spd 5 -> 3 AP | HP 3,600/3,600 | SP 50/50 | Posture 140/140",
        "- Echo        : Spd 9 -> 5 AP | HP 2,600/2,600 | SP 40/40 | Posture 90/90 [STEALTH]",
        "- Cheon Rig   : Spd 4 -> 2 AP | HP 2,600/2,600 | Posture 260/260 [GILDED]",
        "- Scepter Part: Spd 3 -> 1 AP | HP 1,800/1,800 | Posture 160/160 [CHARGED]",
        "- Knight Core : Spd 5 -> 3 AP | HP 3,600/3,600 | Posture 260/260 [CAGED]"
    ])

    hud_t02 = make_box("TACTICAL STAGE HUD: OPERATION 06 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — SCEPTER SAPPING & POWER JAM]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER][TAEHO] [JOON]  [SOOJIN][CHEON]  [YUNA]  [MINHO] [CIVS]  [ECHO]  [KNIGHT]",
        "                                 [SCEPTER]                                ",
        "---",
        "- Node 02: Commander Taeho (Advancing to Node 03 / Concussive Shield Bash)",
        "- Node 03: Engineer Joon (Hydraulic Kinetic Ram Smashes Scepter Conduit)",
        "- Node 04: Handler Soojin (Leaded Snare Restricting Hollow Knight Greatsword)",
        "- Node 05: Grand Patriarch Cheon (Rig 1,820/2,600 / Scepter 1,220/1,800)",
        "- Node 06: Auditor Yuna (Cipher-Pulse Disrupting Sovereign Power Matrix)",
        "- Node 07: Investigator Minho (Memory Anchor Restoring Squad Composure)",
        "- Node 09: Infiltrator Echo (High Throne Arch Flank behind Dais)",
        "- Node 10: SE-C-IIIγ-490 'Hollow Knight' (3,280/3,600 HP / Pale Glow)",
        "---",
        "- Joon        : Spd 7 -> 4 AP [SURGE] | HP 3,800/3,800 | SP 40/40 | Posture 150/150",
        "- Minho       : Spd 9 -> 5 AP [SURGE] | HP 2,900/2,900 | SP 50/50 | Posture 110/110",
        "- Cheon Rig   : Spd 3 -> 1 AP | HP 1,820/2,600 | Posture 188/260 [CONDUIT CRACKED]",
        "- Scepter Part: Spd 2 -> 1 AP | HP 1,220/1,800 | Posture 92/160 [STRAINED]",
        "- Knight Core : Spd 4 -> 2 AP | HP 3,280/3,600 | Posture 222/260 [SNARED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: OPERATION 06 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — SCEPTER SHATTER & STAGGER THRESHOLD 1]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER]        [TAEHO] [JOON]  [CHEON]  [YUNA]  [MINHO] [CIVS]  [ECHO]  [KNIGHT]",
        "---",
        "- Node 03: Commander Taeho (Heavy Piston Strike Smashes Sovereign Breastplate)",
        "- Node 04: Engineer Joon (Thermite Disruption Clamp Igniting Battery)",
        "- Node 05: Grand Patriarch Cheon (STAGGER LEVEL 1 / SCEPTER DESTROYED)",
        "- Node 06: Auditor Yuna (Conspiracy Ledger Download In Progress)",
        "- Node 07: Investigator Minho (Synaptic Pierce Dismantles Scepter Hub)",
        "- Node 09: Infiltrator Echo (Driving Eclipse Stiletto into Servo Joints)",
        "- Node 10: SE-C-IIIγ-490 'Hollow Knight' (Pale Steam Churning)",
        "---",
        "- Taeho       : Spd 6 -> 3 AP [SURGE] | HP 4,400/4,400 | SP 48/50 | Posture 180/180",
        "- Cheon Rig   : Spd 0 -> 0 AP | HP 460/2,600   | Posture 96/260 [STAGGER LEVEL 1]",
        "- Scepter Part: DESTROYED (0/1,800 HP)",
        "- Knight Core : Spd 5 -> 3 AP | HP 3,280/3,600 | Posture 222/260"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: OPERATION 06 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — BERSERK HOLLOW KNIGHT & LEADED WARD]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER]        [TAEHO] [JOON]  [CHEON]  [SOOJIN][YUNA]  [CIVS]  [ECHO]  [KNIGHT]",
        "                                                  [MINHO]                 ",
        "---",
        "- Node 03: Commander Taeho (Shielding Delegate Berths & Captives)",
        "- Node 04: Engineer Joon (Pneumatic Pry Bar Unlatching Delegate Cells)",
        "- Node 05: Grand Patriarch Cheon (Recovered / Pulling Safety Valve on Knight)",
        "- Node 06: Handler Soojin (Leaded Sanctuary Ward Enclosing Squad)",
        "- Node 07: Auditor Yuna & Minho (Cutting Citadel Master Power Matrix)",
        "- Node 08: 16 Municipal Delegates (Cognitive Shields Holding Intact)",
        "- Node 10: SE-C-IIIγ-490 'Hollow Knight' (BERSERK STATE / Pale Sunder Storm)",
        "---",
        "- Soojin      : Spd 7 -> 4 AP [SURGE] | HP 3,600/3,600 | SP 50/50 | Posture 140/140",
        "- Cheon Rig   : Spd 2 -> 1 AP | HP 460/2,600   | Posture 68/260",
        "- Knight Core : Spd 6 -> 4 AP | HP 2,720/3,600 | Posture 144/260 [BERSERK]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: OPERATION 06 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — PHANTOM SEVER & TERMINAL STAGGER]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER]        [TAEHO] [JOON]  [CHEON]  [SOOJIN][YUNA]  [CIVS]          [KNIGHT]",
        "                                                  [MINHO]         [ECHO]  ",
        "---",
        "- Node 03: Commander Taeho (Priming Iron Gavel for Cockpit Breach)",
        "- Node 04: Engineer Joon (Tearing Away Buckled Sovereign Chassis Struts)",
        "- Node 05: Cheon Rig (TERMINAL STAGGER / POSTURE 0/260 / CRUSHED)",
        "- Node 06: Handler Soojin (Aligning Class-IV Leaded Cryo-Cask at Dais)",
        "- Node 07: Investigator Minho (Silver Lancet Stripping Mournful Core)",
        "- Node 09: Infiltrator Echo (Eclipse Stiletto Phantom Sever on Armor)",
        "- Node 10: SE-C-IIIγ-490 'Hollow Knight' (TERMINAL STAGGER / POSTURE 0/260)",
        "---",
        "- Echo        : Spd 11 -> 5 AP [MOMENTUM CRIT] | HP 2,600/2,600 | SP 40/40",
        "- Cheon Rig   : Spd 0 -> 0 AP | HP 0/2,600     | Posture 0/260 [CHASSIS CRUSHED]",
        "- Knight Core : Spd 0 -> 0 AP | HP 1,440/3,600 | Posture 0/260 [TERMINAL STAGGER]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: OPERATION 06 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX OVERDRIVE: IRON GAVEL & CRYO-SEAL]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER]                [JOON]  [TAEHO]  [SOOJIN][YUNA]  [CIVS]          [CASK]  ",
        "                                 [CHEON]          [MINHO]         [ECHO]  ",
        "---",
        "- Node 05: Grand Patriarch Cheon (EXTRACTED UNCONSCIOUS & SECURED)",
        "- Node 06: Auditor Yuna (14,800 Conspiracy & Treason Files Secured)",
        "- Node 08: 16 Municipal Delegates (Safely Unlatched / Zero Fatalities)",
        "- Node 10: SE-C-IIIγ-490 'Hollow Knight' (100% CONTAINED IN CRYOGENIC CASK)",
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

###### Turn 01 Action Resolution Log (Kinetic Ingress & Royal Cleave Deflection)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Commander Taeho initializes `[Law of the Mantle]`: All allies within 1 node gain $+3$ Protection and physical stagger immunity.
  * Infiltrator Echo activates `[Shadow Cloak]`: Enters stealth for 2 turns; cannot be targeted by single-target attacks; $+50\%$ Critical Strike Chance.
  * Handler Soojin initializes `[Sedative Aerosol Ward]`, suppressing ambient pale resonance weeping in the throne hall.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Commander Taeho (Speed 4 -> 2 AP, M.A.W.-W Heavy Armor delta $-1$, Poise $+25$): Holds Node 02. Spends 2 AP on `[Phalanx Bastion: Obsidian Wall]`.
  * Engineer Joon (Speed 5 -> 3 AP, M.A.W.-W Medium delta $0$): Holds Node 03. Spends 2 AP on `[Deployable Mantlet Barrier]`. Holds 1 AP in Reserve.
  * Auditor Yuna (Speed 7 -> 4 AP, M.A.W.-W Light delta $+1$): Holds Node 06 (Range Band 3). Spends 2 AP on `[Cipher-Scan: Sovereign Frequency]`, 2 AP on `[Asset Scan]`.
  * Investigator Minho (Speed 7 -> 4 AP, M.A.W.-W Light delta $+1$): Stands at Node 07. Spends 2 AP on `[Neural Lancet: Calibrated Dart]`. Holds 2 AP in Reserve.
  * Handler Soojin (Speed 5 -> 3 AP, M.A.W.-W Medium delta $0$): Holds Node 04. Spends 2 AP on maintaining the sedative ward. Holds 1 AP in Guard.
  * Infiltrator Echo (Speed 9 -> 5 AP, M.A.W.-W Feather delta $+2$): Advances through high throne arches toward Node 10 from stealth. Spends 2 AP on positioning.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 02 to 05)**: Grand Patriarch Cheon unleashes `[Sovereign Cleave Slam]` (Base 17 + 2 Coins = 29 Power, Heavy Blunt/Pale) against Node 02.
    * Commander Taeho counters with `[Phalanx Bastion: Obsidian Wall]` (Base 19 + 2 Coins = 33 Power, Kinetic Shield).
    * **Clash Outcome**: Taeho WINS THE CLASH (33 vs 29)!
    * The kinetic shield absorbs the devastating pale shockwave without buckling (`[P3: Parry/Protection]`).
    * Taeho reflects **190 kinetic tremor damage** back into Cheon's sovereign chassis! Inflicts $+30$ Posture Strain.
  * **Clash 2 (Node 03 to 05)**: Royal Guard Enforcers thrust with `[Gilded Halberd Rush]` (Atk Power 23, Pierce).
    * Engineer Joon's `[Deployable Mantlet Barrier]` (Def Power 27, Kinetic Shield).
    * **Clash Outcome**: Joon WINS THE CLASH (27 vs 23).
    * Halberds shatter against the reinforced titanium mantlet; zero damage taken.
  * **Unopposed Ranged Fire**:
    * Auditor Yuna's `[Cipher-Scan]` identifies the high-voltage power capacitor housing inside the Crown Scepter wrist joint.
    * Investigator Minho fires `[Neural Lancet: Calibrated Dart]` from Node 07 into Cheon's armored gorget, dealing **270 Pierce damage** and $+28$ Posture Strain!
    * Handler Soojin's sedative ward dampens ambient pale weeping from the Hollow Knight.
- **Step 4: Turn End State**:
  * Cheon Sovereign Chassis HP: 2,600 -> **2,140/2,600** (Combined Encounter HP: **7,540/8,000**).
  * Cheon Posture: 260 -> **202/260**.
  * Squad Composure: **100% (50/50 SP)**. All 6 Officers uninjured.

---

```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Scepter Sapping & Power Jam)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Engineer Joon and Investigator Minho both trigger `Momentum Surge` (+2 Speed next turn).
  * Cheon channels royal lightning through the Crown Scepter: `[Royal Lightning Cleave]`.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Engineer Joon (Speed 7 -> 4 AP): Advances from Node 03 to Node 04. Spends 3 AP to unleash `[Hydraulic Kinetic Ram: Structural Sapping]`.
  * Auditor Yuna (Speed 7 -> 4 AP): Moves to Node 06, deploying `[Cipher-Pulse: Damping Wall]` (2 AP) against the Citadel's master power matrix.
  * Commander Taeho (Speed 4 -> 2 AP): Steps to Node 03, executing `[Shield Bash: Kinetic Drive]` (2 AP).
  * Investigator Minho (Speed 9 -> 5 AP): Casts `[Memory Anchor: Cognitive Salve]` (2 AP), reinforcing squad composure (+15 SP).
  * Handler Soojin (Speed 5 -> 3 AP): Flings `[Resonance Snare: Cold Iron]` (2 AP) around the Hollow Knight's greatsword arm.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 04 to 05)**: Cheon executes `[Royal Lightning Cleave]` (Base 15 + 2 Coins = 27 Power, Heavy Slash).
    * Engineer Joon executes `[Hydraulic Kinetic Ram]` (Base 19 + 2 Coins = 31 Power, Heavy Blunt).
    * **Clash Outcome**: Joon WINS THE CLASH (31 vs 27)!
    * The hydraulic ram smashes straight into the scepter's high-pressure power capacitor sleeve!
    * Deals **580 Blunt damage** directly to the Crown Scepter and inflicts $+58$ Posture Strain!
  * **Clash 2 (Node 06 to 10)**: SE-C-IIIγ-490 'The Hollow Knight' pulses `[Mournful Pale Shockwave]` (Power 25, Pale).
    * Auditor Yuna unleashes `[Cipher-Pulse: Damping Wall]` (Def Power 29, EMP).
    * **Clash Outcome**: Yuna WINS THE CLASH (29 vs 25).
    * The EMP wave scrambles the throne's containment field, dealing **320 Resonance damage** to SE-C-IIIγ-490 and $+38$ Posture Strain!
  * **Follow-Up Maneuvers**:
    * Taeho's `[Shield Bash]` deals **320 Blunt damage** to Cheon's breastplate.
    * Minho's cognitive salve restores $+15$ SP across the strike cadre.
    * Infiltrator Echo severs high-voltage hydraulic cables beneath the throne dais, cutting emergency generator feeds!
- **Step 4: Turn End State**:
  * Cheon Sovereign Chassis HP: 2,140 -> **1,820/2,600** | Posture: **188/260 [CONDUIT CRACKED]**.
  * Crown Scepter Weapon HP: 1,800 -> **1,220/1,800** | Posture: **92/160**.
  * SE-C-IIIγ-490 Hollow Knight HP: 3,600 -> **3,280/3,600** | Posture: **222/260**.
  * Combined Encounter HP: **6,320/8,000** | Squad Composure: **98%**.

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Precision Lancet Pierce & Stagger Threshold 1)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Commander Taeho's `Momentum Surge` activates (+2 Speed next turn -> Net Speed 6, 3 AP).
  * Cheon attempts his royal execution slam: `[Verdict of the Sunken King]`.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Investigator Minho (Speed 9 -> 5 AP): Positions on an elevated arch at Node 07. Spends 3 AP on `[Neural Lancet: Synaptic Pierce]`.
  * Commander Taeho (Speed 6 -> 3 AP): Charges from Node 03 to Node 05, unleashing `[Heavy Piston Strike]` (2 AP).
  * Engineer Joon (Speed 7 -> 4 AP): Plants `[Thermite Disruption Clamp]` (2 AP) directly on the scepter battery.
  * Infiltrator Echo (Speed 9 -> 5 AP): Drops from high arches onto the scepter's wrist joint, driving `[Eclipse Stiletto]` (2 AP).
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 07 to 05)**: Cheon unleashes `[Verdict of the Sunken King]` (Base 17 + 2 Coins = 29 Power, Heavy Blunt).
    * Investigator Minho fires `[Neural Lancet: Synaptic Pierce]` (Base 21 + 2 Coins = 33 Power, High-Precision Pierce).
    * **Clash Outcome**: Minho WINS THE CLASH (33 vs 29)!
    * Minho's silver lancet pierces the scepter's central gyro-stabilizer with surgical precision!
    * **TARGETED PART DESTROYED**: `[The Crown Scepter Weapon Arm]` shears in half, crashing onto the marble dais (**1,220 Scepter HP destroyed: 0/1,800**)!
  * **STAGGER THRESHOLD 1 TRIGGERED!**
    * Combined Target HP drops below 60% (4,800 HP), and Cheon's Posture falls past the 60% strain line!
    * **STAGGER LEVEL 1 ACTIVE!** Cheon's rig loses all defense, taking 1.5x direct damage. All enemy counter-stances cancelled!
  * **Punishment Strike Phase**:
    * Commander Taeho's `[Heavy Piston Strike]` delivers **520 Blunt damage** to the exposed breastplate.
    * Engineer Joon's thermite clamp burns through the shoulder servos for **460 Thermal damage**.
    * Infiltrator Echo's `[Eclipse Stiletto]` slices hydraulic tendons for **380 Slash damage**.
- **Step 4: Turn End State**:
  * Cheon Sovereign Chassis HP: 1,820 -> **460/2,600** (Chassis critically buckled!).
  * Crown Scepter Weapon: **0/1,800 [DESTROYED]**.
  * Combined Encounter HP: **3,740/8,000** | Posture: **96/260 [STAGGER LEVEL 1]**.
  * Squad Composure: **100% (50/50 SP)**.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Berserk Hollow Knight & Leaded Sanctuary Ward)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Recovering from Stagger, Cheon desperately breaks the master stasis seals on SE-C-IIIγ-490 at Node 10!
  * **ENCOUNTER EVENT**: SE-C-IIIγ-490 'The Hollow Knight' enters **Berserk State** (+4 Attack Power)!
  * Pale spiritual frost blankets the hall; a colossal crystalline greatsword ignites with blinding pale fire.
  * Handler Soojin's `Momentum Surge` activates (+2 Speed -> Net Speed 7, 4 AP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Handler Soojin (Speed 7 -> 4 AP): Moves to Node 06, deploying `[Leaded Sanctuary Ward: Vacuum Dome]` (3 AP) enclosing the squad and delegate berths.
  * Commander Taeho (Speed 4 -> 2 AP): Steps to Node 03, locking his Obsidian shield in front of the hostage cages.
  * Auditor Yuna (Speed 7 -> 4 AP): Hacks the Citadel's electrical control hub at Node 06, shutting down high-voltage grids (2 AP).
  * Investigator Minho (Speed 7 -> 4 AP): Dispenses `[Neuro-Stabilizing Aerosol]` (2 AP) to protect delegate minds.
  * Engineer Joon (Speed 5 -> 3 AP): Uses pneumatic pry bar at Node 04 to pop open the delegate cell padlocks (2 AP).
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 10 to 06)**: Berserk SE-C-IIIγ-490 unleashes `[Pale Sunder Storm: Mournful Cleave]` (Base 24 + 2 Coins = 34 Power, Area Pale).
    * Handler Soojin deploys `[Leaded Sanctuary Ward]` (Base 27 + 2 Coins = 37 Power, Vacuum Barrier).
    * **Clash Outcome**: Soojin WINS THE CLASH (37 vs 34)!
    * The lead-lined vacuum sphere fully captures the pale sunder shockwave (`[P3: Parry/Protection]`).
    * Zero pale particles penetrate the leaded ward. Soojin redirects the trapped kinetic energy back into the knight's armor, dealing **560 Void damage** and $+78$ Posture Strain!
- **Step 4: Turn End State**:
  * Cheon Sovereign Chassis HP: **460/2,600** | Posture: **68/260**.
  * SE-C-IIIγ-490 Hollow Knight HP: 3,280 -> **2,720/3,600** | Posture: **144/260**.
  * Combined Encounter HP: **3,180/8,000** | Squad Composure: **96%**.

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Phantom Stiletto Sever & Terminal Stagger Threshold 2)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Infiltrator Echo readies `[Eclipse Stiletto: Phantom Sever]` from the overhead gilded throne canopy (+50% Crit Chance, ignores 100% defense).
  * Investigator Minho targets the knight's central pale breastplate rune.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Infiltrator Echo (Speed 11 -> 5 AP, Momentum + Stealth Boost): Drops from the high canopy onto Node 10. Spends 3 AP on `[Phantom Sever]`.
  * Investigator Minho (Speed 7 -> 4 AP): Fires `[Silver Lancet: Cognitive Disruptor]` from Node 07 into the exposed rune (2 AP).
  * Engineer Joon (Speed 5 -> 3 AP): Smashes away Cheon's remaining chassis supports at Node 04 (2 AP).
  * Auditor Yuna (Speed 7 -> 4 AP): Finalizes forensic download of 14,800 high-level conspiracy documents at Node 06 (2 AP).
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 10)**: SE-C-IIIγ-490 sweeps with `[Crystalline Greatsword Cleave]` (Atk Power 30, Pale/Slash).
    * Infiltrator Echo executes `[Eclipse Stiletto: Phantom Sever]` (Base 25 + 2 Coins Heads = 35 Power, Slash).
    * **Clash Outcome**: Echo WINS THE CLASH (35 vs 30)!
    * Echo slices cleanly through the spiritual tendons linking the knight's hollow armor!
    * **CRITICAL HIT!** Deals **720 Slash damage** directly to the core and strips 100 Posture points!
  * **Targeted Fire**:
    * Investigator Minho's `[Silver Lancet]` strikes the pale rune, dealing **560 Freezing Pierce damage** and wiping out the entity's remaining Posture!
    * Engineer Joon demolishes Cheon's buckled sovereign chassis with the pneumatic ram, dealing **460 Blunt damage** and crushing the exoskeleton completely (Chassis HP: 0/2,600)!
- **Step 4: TERMINAL STAGGER THRESHOLD 2 TRIGGERED!**:
  * Both Cheon and SE-C-IIIγ-490 reach **Posture 0/260** and **0/260**!
  * **TERMINAL STAGGER ACTIVE!** Cheon collapses under pneumatic feedback, pinned to the marble floor. SE-C-IIIγ-490's hollow armor shatters into inert plate pieces, its pale core floating helplessly.
  * Combined Encounter HP drops below 20% (Total HP: **1,440/8,000**).
- **Step 5: Turn End State**:
  * Cheon Sovereign Chassis HP: **0/2,600 [CHASSIS CRUSHED]** | Posture: **0/260**.
  * SE-C-IIIγ-490 Hollow Knight HP: **1,440/3,600** | Posture: **0/260 [TERMINAL STAGGER]**.
  * Squad Composure: **100% (50/50 SP)**.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Overdrive: Iron Gavel & Royal Cryo-Seal)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Commander Taeho charges `[Decree of Unbroken Order — Iron Gavel]` (Cost: 35 SP).
  * Handler Soojin activates `[Class-IV Leaded Cryo-Seal: Vault of Solitude]` (Cost: 35 SP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Commander Taeho (Speed 4 -> 2 AP): Steps up to Node 05, standing over Cheon's body. Spends 2 AP on Climax Overdrive.
  * Handler Soojin (Speed 5 -> 3 AP): Wheels the Class-IV Cryogenic Leaded Cask directly beneath the pale core at Node 10. Spends 3 AP on Climax Containment.
  * Engineer Joon and Infiltrator Echo: Unlatch the final cell doors on the 16 municipal delegates at Node 08, wrapping them in warm mantlets.
  * Auditor Yuna: Verifies Level-5 encryption on the 14,800 seized conspiracy drives at Node 06.
- **Step 3: Climax Overdrive Executions**:
  * **Climax 1 (Commander Taeho vs Grand Patriarch Cheon)**:
    * Taeho channels a 120 dB directed concussive wave through his tungsten truncheon: `[Iron Gavel: Decreed Subjugation]` (Power 42).
    * Delivers a single calculated strike to Cheon's carotid nerve cluster.
    * Non-lethal kinetic tremor ensures complete, safe neurological sedation.
    * **GRAND PATRIARCH CHEON SUBDUED & INCAPACITATED!** Remanded to Warden custody!
  * **Climax 2 (Handler Soojin vs SE-C-IIIγ-490 'The Hollow Knight')**:
    * Soojin unlatches the leaded collar, extending cryogenic containment arms around the pale core: `[Vault of Solitude]` (Power 40).
    * All swirling pale emotional vapors are drawn into the vacuum cask within 4.4 seconds! Zero atmospheric leakage detected.
    * The heavy basalt locking collar snaps shut with a resounding metallic boom: **CRYOGENIC VACUUM SEAL COMPLETE**.
    * **SE-C-IIIγ-490 HP DROPS TO 0!** Fully contained in peaceful dormancy and logged for transfer to Reverie Directorate Floor 2!
- **Step 4: Pacification & Operational Outcome**:
  * **Grand Patriarch Cheon**: Sovereign chassis demolished; syndicate patriarch safely secured in Warden custody.
  * **Crown Scepter Weapon Arm**: 100% destroyed.
  * **SE-C-IIIγ-490 'The Hollow Knight'**: 100% contained in cryogenic lead cask. Zero leakage.
  * **Municipal Delegates**: 16 high-ranking council aides liberated without casualties.
  * **Evidence**: 14,800 classified documents seized, exposing corrupt council commissioners and completing the absolute pacification of The Raw!
"""

def update_operation_6():
    path = "SOMNARAK-WORLD/Katharcheok/Operation_6_Basileugung.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    start_str = "### Tactical Engagement: 6-Turn Pacification Gauntlet"
    end_str = "### Post-Action Forensic Inventory"

    start_idx = content.find(start_str)
    end_idx = content.find(end_str)

    if start_idx == -1 or end_idx == -1:
        print(f"Error: Could not locate boundaries! start_idx={start_idx}, end_idx={end_idx}")
        return

    new_engagement = get_op6_engagement() + "\n\n"
    new_content = content[:start_idx] + new_engagement + content[end_idx:]

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Updated Operation 6 successfully!")

if __name__ == "__main__":
    update_operation_6()
