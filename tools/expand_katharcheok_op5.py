#!/usr/bin/env python3
"""
tools/expand_katharcheok_op5.py
Expands Operation 5 (Therionok - The Black Cages) in SOMNARAK-WORLD/Katharcheok/Operation_5_Therionok.md
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

def get_op5_engagement():
    dossier_box = make_box("TARGET DOSSIER: BEASTMASTER JAGYEON & SE-C-IIIγ-102", [
        "APEX TARGET        : Beastmaster Jagyeon ('The Arena Patriarch')",
        "MODULAR WEAPON     : Harmonic Shock Whip (High-Voltage Electric/Slash)",
        "CONTRABAND ENTITY  : SE-C-IIIγ-102 'Chained Frenzy' (WAW Threat / Dancing Chains)",
        "ESCORT MINIONS     : Pit Gladiators (x2) & Barbed Harpooners",
        "ENCOUNTER DOMAIN   : Zone D & E Colosseum Arena & Cages (-260m Depth)",
        "---",
        "BOSS COMBAT PROFILE (BEASTMASTER JAGYEON):",
        "- Beast Armor HP   : 2,400 HP | Core Body HP: 2,400 HP (Total 4,800 HP)",
        "- Shock Whip HP    : 1,800 HP (Modular Destructible Weapon Part)",
        "- Posture Pool     : 240/240 (Dual Threshold Stagger System)",
        "- Stagger 1 Proc   : 60% Posture Strain (144 Posture) / Whip Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Terminal Stagger / Cask Ready)",
        "- Primary Attack   : Harmonic Shock Lash & Dual Lightning Cleave (Slash)",
        "---",
        "CONTRABAND ENTITY PROFILE (SE-C-IIIγ-102 'CHAINED FRENZY'):",
        "- Entity HP Pool   : 3,400 HP | Posture Pool: 240/240",
        "- Total Combined   : 7,600 Encounter HP",
        "- Attack Affinity  : Crimson Chain Flail & Razor Iron Storm (Grudge)"
    ])

    hud_t01 = make_box("TACTICAL STAGE HUD: OPERATION 05 — BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 — ZONE D+E UNDERGROUND ARENA PIT]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER][TAEHO] [JOON]  [SOOJIN][JAGYEON][YUNA]  [MINHO] [CIVS]          [CHAINS]",
        "                                 [WHIP]                           [ECHO]  ",
        "---",
        "- Node 01: Breach Entry / Class-II Armored Cruiser 'The Iron Vanguard'",
        "- Node 02: Commander Taeho (Vanguard Band 1 / Phalanx Bastion Obsidian)",
        "- Node 03: Engineer Joon (Point-Blank Band 1 / Deployable Mantlet Barrier)",
        "- Node 04: Handler Soojin (Close Skirmish Band 2 / Sedative Aerosol Ward)",
        "- Node 05: Beastmaster Jagyeon & Shock Whip (Central Arena Sand Ring)",
        "- Node 06: Auditor Yuna (Mid-Field Band 3 / Spectator Wiretap Console)",
        "- Node 07: Investigator Minho (Mid-Field Band 3 / Mnemonic Sniper Pillar)",
        "- Node 08: Slave Cages (28 Captive Arena Gladiators)",
        "- Node 10: SE-C-IIIγ-102 'Chained Frenzy' & Infiltrator Echo (Pillar Stealth)",
        "---",
        "- Taeho       : Spd 4 -> 2 AP | HP 4,400/4,400 | SP 45/50 | Posture 180/180",
        "- Joon        : Spd 5 -> 3 AP | HP 3,800/3,800 | SP 40/40 | Posture 150/150",
        "- Yuna        : Spd 7 -> 4 AP | HP 2,700/2,700 | SP 50/50 | Posture 100/100",
        "- Minho       : Spd 7 -> 4 AP | HP 2,900/2,900 | SP 45/45 | Posture 110/110",
        "- Soojin      : Spd 5 -> 3 AP | HP 3,600/3,600 | SP 50/50 | Posture 140/140",
        "- Echo        : Spd 9 -> 5 AP | HP 2,600/2,600 | SP 40/40 | Posture 90/90 [STEALTH]",
        "- Jagyeon Rig : Spd 4 -> 2 AP | HP 2,400/2,400 | Posture 240/240 [BEAST-HIDE]",
        "- Whip Part   : Spd 3 -> 1 AP | HP 1,800/1,800 | Posture 150/150 [ELECTRIFIED]",
        "- Chain Beast : Spd 5 -> 3 AP | HP 3,400/3,400 | Posture 240/240 [COLLARED]"
    ])

    hud_t02 = make_box("TACTICAL STAGE HUD: OPERATION 05 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — WHIP SAPPING & FREQUENCY JAM]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER][TAEHO] [JOON]  [SOOJIN][JAGYEON][YUNA]  [MINHO] [CIVS]  [ECHO]  [CHAINS]",
        "                                 [WHIP]                                   ",
        "---",
        "- Node 02: Commander Taeho (Advancing to Node 03 / Concussive Shield Bash)",
        "- Node 03: Engineer Joon (Hydraulic Kinetic Ram Smashes Whip Generator)",
        "- Node 04: Handler Soojin (Leaded Snare Restricting Thrashing Chains)",
        "- Node 05: Beastmaster Jagyeon (Armor 1,660/2,400 / Whip 1,240/1,800)",
        "- Node 06: Auditor Yuna (Cipher-Pulse Disrupting Slave-Collar Frequency)",
        "- Node 07: Investigator Minho (Memory Anchor Restoring Squad Composure)",
        "- Node 09: Infiltrator Echo (High Basalt Pillar Flank behind Ring)",
        "- Node 10: SE-C-IIIγ-102 'Chained Frenzy' (3,120/3,400 HP / Collar Sparks)",
        "---",
        "- Joon        : Spd 7 -> 4 AP [SURGE] | HP 3,800/3,800 | SP 40/40 | Posture 150/150",
        "- Minho       : Spd 9 -> 5 AP [SURGE] | HP 2,900/2,900 | SP 50/50 | Posture 110/110",
        "- Jagyeon Rig : Spd 3 -> 1 AP | HP 1,660/2,400 | Posture 170/240 [GENERATOR BROKEN]",
        "- Whip Part   : Spd 2 -> 1 AP | HP 1,240/1,800 | Posture 86/150 [VOLTAGE LOSS]",
        "- Chain Beast : Spd 4 -> 2 AP | HP 3,120/3,400 | Posture 204/240 [SNARED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: OPERATION 05 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — WHIP SHATTER & STAGGER THRESHOLD 1]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER]        [TAEHO] [JOON]  [JAGYEON][YUNA]  [MINHO] [CIVS]  [ECHO]  [CHAINS]",
        "---",
        "- Node 03: Commander Taeho (Heavy Piston Strike Smashes Beast Breastplate)",
        "- Node 04: Engineer Joon (Thermite Disruption Clamp Igniting Battery)",
        "- Node 05: Beastmaster Jagyeon (STAGGER LEVEL 1 / WHIP DESTROYED)",
        "- Node 06: Auditor Yuna (Slave Auction Registry Download In Progress)",
        "- Node 07: Investigator Minho (Synaptic Pierce Dismantles Whip Hub)",
        "- Node 09: Infiltrator Echo (Driving Eclipse Stiletto into Servo Joints)",
        "- Node 10: SE-C-IIIγ-102 'Chained Frenzy' (Chains Trembling in Rage)",
        "---",
        "- Taeho       : Spd 6 -> 3 AP [SURGE] | HP 4,400/4,400 | SP 48/50 | Posture 180/180",
        "- Jagyeon Rig : Spd 0 -> 0 AP | HP 420/2,400   | Posture 84/240 [STAGGER LEVEL 1]",
        "- Whip Part   : DESTROYED (0/1,800 HP)",
        "- Chain Beast : Spd 5 -> 3 AP | HP 3,120/3,400 | Posture 204/240"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: OPERATION 05 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — BERSERK CHAINED FRENZY & LEADED WARD]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER]        [TAEHO] [JOON]  [JAGYEON][SOOJIN][YUNA]  [CIVS]  [ECHO]  [CHAINS]",
        "                                                  [MINHO]                 ",
        "---",
        "- Node 03: Commander Taeho (Shielding Gladiator Pens & Captives)",
        "- Node 04: Engineer Joon (Pneumatic Pry Bar Unlatching Heavy Cage Latches)",
        "- Node 05: Beastmaster Jagyeon (Recovered / Pulling Remote Shock Collar Trigger)",
        "- Node 06: Handler Soojin (Leaded Sanctuary Ward Enclosing Arena Squad)",
        "- Node 07: Auditor Yuna & Minho (Cutting Arena Remote Shock Currents)",
        "- Node 08: 28 Captive Gladiators (Cognitive Shields Holding Intact)",
        "- Node 10: SE-C-IIIγ-102 'Chained Frenzy' (BERSERK STATE / Razor Chain Storm)",
        "---",
        "- Soojin      : Spd 7 -> 4 AP [SURGE] | HP 3,600/3,600 | SP 50/50 | Posture 140/140",
        "- Jagyeon Rig : Spd 2 -> 1 AP | HP 420/2,400   | Posture 58/240",
        "- Chain Beast : Spd 6 -> 4 AP | HP 2,580/3,400 | Posture 130/240 [BERSERK]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: OPERATION 05 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — PHANTOM SEVER & TERMINAL STAGGER]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER]        [TAEHO] [JOON]  [JAGYEON][SOOJIN][YUNA]  [CIVS]          [CHAINS]",
        "                                                  [MINHO]         [ECHO]  ",
        "---",
        "- Node 03: Commander Taeho (Priming Iron Gavel for Cockpit Breach)",
        "- Node 04: Engineer Joon (Tearing Away Buckled Greaves on Jagyeon)",
        "- Node 05: Jagyeon Armor (TERMINAL STAGGER / POSTURE 0/240 / CRUSHED)",
        "- Node 06: Handler Soojin (Aligning Class-IV Leaded Cryo-Cask at Dais)",
        "- Node 07: Investigator Minho (Silver Lancet Stripping Slave-Collar Root)",
        "- Node 09: Infiltrator Echo (Eclipse Stiletto Phantom Sever on Chains)",
        "- Node 10: SE-C-IIIγ-102 'Chained Frenzy' (TERMINAL STAGGER / POSTURE 0/240)",
        "---",
        "- Echo        : Spd 11 -> 5 AP [MOMENTUM CRIT] | HP 2,600/2,600 | SP 40/40",
        "- Jagyeon Rig : Spd 0 -> 0 AP | HP 0/2,400     | Posture 0/240 [CHASSIS CRUSHED]",
        "- Chain Beast : Spd 0 -> 0 AP | HP 1,360/3,400 | Posture 0/240 [TERMINAL STAGGER]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: OPERATION 05 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX OVERDRIVE: IRON GAVEL & CRYO-CASK SEAL]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[CRUISER]                [JOON]  [TAEHO]  [SOOJIN][YUNA]  [CIVS]          [CASK]  ",
        "                                 [JAGYEON]        [MINHO]         [ECHO]  ",
        "---",
        "- Node 05: Beastmaster Jagyeon (EXTRACTED UNCONSCIOUS & SECURED)",
        "- Node 06: Auditor Yuna (8,900 Slave & Wagering Records Seized)",
        "- Node 08: 28 Captive Gladiators (Safely Unlatched / Zero Fatalities)",
        "- Node 10: SE-C-IIIγ-102 'Chained Frenzy' (100% CONTAINED IN CRYOGENIC CASK)",
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

###### Turn 01 Action Resolution Log (Kinetic Ingress & Shock Whip Deflection)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Commander Taeho initializes `[Law of the Mantle]`: All allies within 1 node gain $+3$ Protection and physical stagger immunity.
  * Infiltrator Echo activates `[Shadow Cloak]`: Enters stealth for 2 turns; cannot be targeted by single-target attacks; $+50\%$ Critical Strike Chance.
  * Handler Soojin initializes `[Sedative Aerosol Ward]`, suppressing agitated sorrow emissions in the sand pit.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Commander Taeho (Speed 4 -> 2 AP, M.A.W.-W Heavy Armor delta $-1$, Poise $+25$): Holds Node 02. Spends 2 AP on `[Phalanx Bastion: Obsidian Wall]`.
  * Engineer Joon (Speed 5 -> 3 AP, M.A.W.-W Medium delta $0$): Holds Node 03. Spends 2 AP on `[Deployable Mantlet Barrier]`. Holds 1 AP in Reserve.
  * Auditor Yuna (Speed 7 -> 4 AP, M.A.W.-W Light delta $+1$): Holds Node 06 (Range Band 3). Spends 2 AP on `[Cipher-Scan: Neural Collar Frequency]`, 2 AP on `[Asset Scan]`.
  * Investigator Minho (Speed 7 -> 4 AP, M.A.W.-W Light delta $+1$): Stands at Node 07. Spends 2 AP on `[Neural Lancet: Calibrated Dart]`. Holds 2 AP in Reserve.
  * Handler Soojin (Speed 5 -> 3 AP, M.A.W.-W Medium delta $0$): Holds Node 04. Spends 2 AP on maintaining the sedative ward. Holds 1 AP in Guard.
  * Infiltrator Echo (Speed 9 -> 5 AP, M.A.W.-W Feather delta $+2$): Scales basalt arena pillars toward Node 10 from stealth. Spends 2 AP on positioning.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 02 to 05)**: Beastmaster Jagyeon lashes out with `[Harmonic Shock Lash]` (Base 16 + 2 Coins = 28 Power, Electric/Slash) against Node 02.
    * Commander Taeho counters with `[Phalanx Bastion: Obsidian Wall]` (Base 18 + 2 Coins = 32 Power, Kinetic Shield).
    * **Clash Outcome**: Taeho WINS THE CLASH (32 vs 28)!
    * The kinetic shield grounds the 50,000-volt high-voltage arc directly into the sand deck (`[P3: Parry/Protection]`).
    * Taeho reflects **180 kinetic tremor damage** back into Jagyeon's beast-hide harness! Inflicts $+28$ Posture Strain.
  * **Clash 2 (Node 03 to 05)**: Pit Gladiators thrust with `[Barbed Harpoon Thrust]` (Atk Power 22, Pierce).
    * Engineer Joon's `[Deployable Mantlet Barrier]` (Def Power 26, Kinetic Shield).
    * **Clash Outcome**: Joon WINS THE CLASH (26 vs 22).
    * Harpoons shatter against the reinforced titanium mantlet; zero damage taken.
  * **Unopposed Ranged Fire**:
    * Auditor Yuna's `[Cipher-Scan]` identifies the high-voltage battery housing at Jagyeon's hip.
    * Investigator Minho fires `[Neural Lancet: Calibrated Dart]` from Node 07 into Jagyeon's reinforced greaves, dealing **260 Pierce damage** and $+26$ Posture Strain!
    * Handler Soojin's sedative ward stabilizes ambient sorrow emissions around the arena floor.
- **Step 4: Turn End State**:
  * Jagyeon Beast Armor HP: 2,400 -> **1,960/2,400** (Combined Encounter HP: **7,160/7,600**).
  * Jagyeon Posture: 240 -> **186/240**.
  * Squad Composure: **100% (50/50 SP)**. All 6 Officers uninjured.

---

```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Sapping the Whip Generator & Frequency Jam)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Engineer Joon and Investigator Minho both trigger `Momentum Surge` (+2 Speed next turn).
  * Jagyeon overcharges the dual whip coils: `[Dual Lightning Cleave]`.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Engineer Joon (Speed 7 -> 4 AP): Advances from Node 03 to Node 04. Spends 3 AP to unleash `[Hydraulic Kinetic Ram: Structural Sapping]`.
  * Auditor Yuna (Speed 7 -> 4 AP): Moves to Node 06, deploying `[Cipher-Pulse: Damping Wall]` (2 AP) against SE-C-IIIγ-102's collar receiver.
  * Commander Taeho (Speed 4 -> 2 AP): Steps to Node 03, executing `[Shield Bash: Heavy Tremor]` (2 AP).
  * Investigator Minho (Speed 9 -> 5 AP): Casts `[Memory Anchor: Cognitive Salve]` (2 AP), reinforcing squad composure (+15 SP).
  * Handler Soojin (Speed 5 -> 3 AP): Flings `[Resonance Snare: Cold Iron]` (2 AP) around the chain beast's limbs.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 04 to 05)**: Jagyeon executes `[Dual Lightning Cleave]` (Base 14 + 2 Coins = 26 Power, Heavy Slash).
    * Engineer Joon executes `[Hydraulic Kinetic Ram]` (Base 18 + 2 Coins = 30 Power, Heavy Blunt).
    * **Clash Outcome**: Joon WINS THE CLASH (30 vs 26)!
    * The hydraulic ram smashes straight into the hip battery generator of the whip!
    * Deals **560 Blunt damage** directly to the Harmonic Shock Whip and inflicts $+56$ Posture Strain!
  * **Clash 2 (Node 06 to 10)**: SE-C-IIIγ-102 'Chained Frenzy' thrashes with `[Crimson Chain Flail]` (Power 24, Grudge).
    * Auditor Yuna unleashes `[Cipher-Pulse: Damping Wall]` (Def Power 28, EMP).
    * **Clash Outcome**: Yuna WINS THE CLASH (28 vs 24).
    * The EMP wave scrambles the collar's agony generator, dealing **280 Resonance damage** to SE-C-IIIγ-102 and $+36$ Posture Strain!
  * **Follow-Up Maneuvers**:
    * Taeho's `[Shield Bash]` deals **300 Blunt damage** to Jagyeon's breastplate.
    * Minho's cognitive salve restores $+15$ SP across the strike cadre.
    * Infiltrator Echo severs an overhead winch cable, dropping a heavy iron cage onto the gladiators' weapon rack!
- **Step 4: Turn End State**:
  * Jagyeon Beast Armor HP: 1,960 -> **1,660/2,400** | Posture: **170/240 [GENERATOR BROKEN]**.
  * Harmonic Shock Whip HP: 1,800 -> **1,240/1,800** | Posture: **86/150**.
  * SE-C-IIIγ-102 Chain Beast HP: 3,400 -> **3,120/3,400** | Posture: **204/240**.
  * Combined Encounter HP: **6,020/7,600** | Squad Composure: **98%**.

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Precision Lancet Pierce & Stagger Threshold 1)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Commander Taeho's `Momentum Surge` activates (+2 Speed next turn -> Net Speed 6, 3 AP).
  * Jagyeon attempts his lethal arena execution sweep: `[Thunderous Execution Lash]`.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Investigator Minho (Speed 9 -> 5 AP): Positions atop a basalt pillar at Node 07. Spends 3 AP on `[Neural Lancet: Synaptic Pierce]`.
  * Commander Taeho (Speed 6 -> 3 AP): Charges from Node 03 to Node 05, unleashing `[Heavy Piston Strike]` (2 AP).
  * Engineer Joon (Speed 7 -> 4 AP): Plants `[Thermite Disruption Clamp]` (2 AP) directly on Jagyeon's battery coupling.
  * Infiltrator Echo (Speed 9 -> 5 AP): Drops from high pillars onto the whip's emitter hub, driving `[Eclipse Stiletto]` (2 AP).
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 07 to 05)**: Jagyeon unleashes `[Thunderous Execution Lash]` (Base 16 + 2 Coins = 28 Power, Heavy Slash).
    * Investigator Minho fires `[Neural Lancet: Synaptic Pierce]` (Base 20 + 2 Coins = 32 Power, High-Precision Pierce).
    * **Clash Outcome**: Minho WINS THE CLASH (32 vs 28)!
    * Minho's silver lancet pierces the primary plasma coil of the whip with surgical precision!
    * **TARGETED PART DESTROYED**: `[The Harmonic Shock Whip]` explodes into smoking copper braids and shattered porcelain insulation (**1,240 Whip HP destroyed: 0/1,800**)!
  * **STAGGER THRESHOLD 1 TRIGGERED!**
    * Combined Target HP drops below 60% (4,560 HP), and Jagyeon's Posture falls past the 60% strain line!
    * **STAGGER LEVEL 1 ACTIVE!** Jagyeon's beast armor loses all defense, taking 1.5x direct damage. All enemy counter-stances cancelled!
  * **Punishment Strike Phase**:
    * Commander Taeho's `[Heavy Piston Strike]` delivers **500 Blunt damage** to the exposed breastplate.
    * Engineer Joon's thermite clamp burns through the greaves for **440 Thermal damage**.
    * Infiltrator Echo's `[Eclipse Stiletto]` slices servo tendons for **300 Slash damage**.
- **Step 4: Turn End State**:
  * Jagyeon Beast Armor HP: 1,660 -> **420/2,400** (Chassis critically buckled!).
  * Harmonic Shock Whip: **0/1,800 [DESTROYED]**.
  * Combined Encounter HP: **3,540/7,600** | Posture: **84/240 [STAGGER LEVEL 1]**.
  * Squad Composure: **100% (50/50 SP)**.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Crimson Frenzy Thrash & Leaded Sanctuary Ward)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Recovering from Stagger, Jagyeon hits the remote torture override on the beast's collar at Node 10!
  * **ENCOUNTER EVENT**: SE-C-IIIγ-102 'Chained Frenzy' enters **Berserk State** (+4 Attack Power)!
  * Massive barbed chains whip in an uncontrollable hurricane of red sparks and whistling steel.
  * Handler Soojin's `Momentum Surge` activates (+2 Speed -> Net Speed 7, 4 AP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Handler Soojin (Speed 7 -> 4 AP): Moves to Node 06, deploying `[Leaded Sanctuary Ward: Vacuum Dome]` (3 AP) enclosing the squad and slave holding pens.
  * Commander Taeho (Speed 4 -> 2 AP): Steps to Node 03, locking his Obsidian shield in front of the gladiator cages.
  * Auditor Yuna (Speed 7 -> 4 AP): Hacks the arena electrical grid at Node 06, cutting off all torture voltage feeds (2 AP).
  * Investigator Minho (Speed 7 -> 4 AP): Dispenses `[Neuro-Stabilizing Aerosol]` (2 AP) to protect captive sanity.
  * Engineer Joon (Speed 5 -> 3 AP): Uses pneumatic pry bar at Node 04 to pop open the heavy cage padlocks (2 AP).
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 10 to 06)**: Berserk SE-C-IIIγ-102 unleashes `[Razor Iron Storm: Chained Frenzy]` (Base 23 + 2 Coins = 33 Power, Area Slash/Grudge).
    * Handler Soojin deploys `[Leaded Sanctuary Ward]` (Base 26 + 2 Coins = 36 Power, Vacuum Barrier).
    * **Clash Outcome**: Soojin WINS THE CLASH (36 vs 33)!
    * The lead-lined vacuum sphere fully captures the whirling razor-chain shockwave (`[P3: Parry/Protection]`).
    * Zero chain shards penetrate the leaded barrier. Soojin redirects the trapped kinetic energy back into the beast's tether, dealing **540 Void damage** and $+74$ Posture Strain!
- **Step 4: Turn End State**:
  * Jagyeon Beast Armor HP: **420/2,400** | Posture: **58/240**.
  * SE-C-IIIγ-102 Chain Beast HP: 3,120 -> **2,580/3,400** | Posture: **130/240**.
  * Combined Encounter HP: **3,000/7,600** | Squad Composure: **96%**.

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Phantom Stiletto Sever & Terminal Stagger Threshold 2)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Infiltrator Echo readies `[Eclipse Stiletto: Phantom Sever]` from the overhead arena arches (+50% Crit Chance, ignores 100% defense).
  * Investigator Minho targets the slave-collar's central explosive squib.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Infiltrator Echo (Speed 11 -> 5 AP, Momentum + Stealth Boost): Drops from the high arch onto Node 10. Spends 3 AP on `[Phantom Sever]`.
  * Investigator Minho (Speed 7 -> 4 AP): Fires `[Silver Lancet: Cognitive Disruptor]` from Node 07 into the exposed collar root (2 AP).
  * Engineer Joon (Speed 5 -> 3 AP): Smashes away Jagyeon's remaining leg armor at Node 04 (2 AP).
  * Auditor Yuna (Speed 7 -> 4 AP): Finalizes forensic download of 8,900 slave contracts and illegal wagering ledgers at Node 06 (2 AP).
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 10)**: SE-C-IIIγ-102 thrashes with `[Barbed Spine Cleave]` (Atk Power 29, Slash).
    * Infiltrator Echo executes `[Eclipse Stiletto: Phantom Sever]` (Base 24 + 2 Coins Heads = 34 Power, Slash).
    * **Clash Outcome**: Echo WINS THE CLASH (34 vs 29)!
    * Echo slices cleanly through the thick barbed-iron spine connecting the entity's central shackle!
    * **CRITICAL HIT!** Deals **680 Slash damage** directly to the core and strips 90 Posture points!
  * **Targeted Fire**:
    * Investigator Minho's `[Silver Lancet]` strikes the collar receiver, disarming the explosive squib and dealing **460 Freezing Pierce damage**!
    * Engineer Joon demolishes Jagyeon's buckled beast-hide armor with the pneumatic ram, dealing **420 Blunt damage** and crushing the harness completely (Armor HP: 0/2,400)!
- **Step 4: TERMINAL STAGGER THRESHOLD 2 TRIGGERED!**:
  * Both Jagyeon and SE-C-IIIγ-102 reach **Posture 0/240** and **0/240**!
  * **TERMINAL STAGGER ACTIVE!** Jagyeon falls unconscious into the arena sand. SE-C-IIIγ-102's chains fall slack, the beast collapsing into exhausted weeping.
  * Combined Encounter HP drops below 20% (Total HP: **1,360/7,600**).
- **Step 5: Turn End State**:
  * Jagyeon Beast Armor HP: **0/2,400 [ARMOR CRUSHED]** | Posture: **0/240**.
  * SE-C-IIIγ-102 Chain Beast HP: **1,360/3,400** | Posture: **0/240 [TERMINAL STAGGER]**.
  * Squad Composure: **100% (50/50 SP)**.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Climax Overdrive: Iron Gavel & Cryo-Cask Seal)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Commander Taeho charges `[Decree of Unbroken Order — Iron Gavel]` (Cost: 35 SP).
  * Handler Soojin activates `[Class-IV Leaded Cryo-Seal: Vault of Solitude]` (Cost: 35 SP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Commander Taeho (Speed 4 -> 2 AP): Steps up to Node 05, standing over Jagyeon's body. Spends 2 AP on Climax Overdrive.
  * Handler Soojin (Speed 5 -> 3 AP): Wheels the Class-IV Cryogenic Leaded Cask directly beside the chained entity at Node 10. Spends 3 AP on Climax Containment.
  * Engineer Joon and Infiltrator Echo: Unlatch the final cage doors on the 28 captive gladiators at Node 08, wrapping them in warm mantlets.
  * Auditor Yuna: Verifies Level-5 encryption on the 8,900 seized wagering drives at Node 06.
- **Step 3: Climax Overdrive Executions**:
  * **Climax 1 (Commander Taeho vs Beastmaster Jagyeon)**:
    * Taeho channels a 120 dB directed concussive wave through his tungsten truncheon: `[Iron Gavel: Decreed Subjugation]` (Power 42).
    * Delivers a single calculated strike to Jagyeon's carotid nerve cluster.
    * Non-lethal kinetic tremor ensures complete, safe neurological sedation.
    * **BEASTMASTER JAGYEON SUBDUED & INCAPACITATED!** Remanded to Warden custody!
  * **Climax 2 (Handler Soojin vs SE-C-IIIγ-102 'Chained Frenzy')**:
    * Soojin unlatches the leaded collar, extending cryogenic containment arms around the sleeping entity: `[Vault of Solitude]` (Power 40).
    * All residual sorrow vapor and chain residue are drawn into the vacuum cask within 4.3 seconds! Zero atmospheric leakage detected.
    * The heavy basalt locking collar snaps shut with a resounding metallic boom: **CRYOGENIC VACUUM SEAL COMPLETE**.
    * **SE-C-IIIγ-102 HP DROPS TO 0!** Fully contained in peaceful dormancy and logged for transfer to Reverie Directorate Floor 2!
- **Step 4: Pacification & Operational Outcome**:
  * **Beastmaster Jagyeon**: Armor demolished; arena boss safely secured in Warden custody.
  * **Harmonic Shock Whip**: 100% destroyed.
  * **SE-C-IIIγ-102 'Chained Frenzy'**: 100% contained in cryogenic lead cask. Zero leakage.
  * **Civilian Captives**: 28 gladiators liberated from illegal fighting contracts without casualties.
  * **Evidence**: 8,900 slave deeds and betting logs recovered, uncovering corrupt municipal wardens.
"""

def update_operation_5():
    path = "SOMNARAK-WORLD/Katharcheok/Operation_5_Therionok.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    start_str = "### Tactical Engagement: 6-Turn Pacification Gauntlet"
    end_str = "### Post-Action Forensic Inventory"

    start_idx = content.find(start_str)
    end_idx = content.find(end_str)

    if start_idx == -1 or end_idx == -1:
        print(f"Error: Could not locate boundaries! start_idx={start_idx}, end_idx={end_idx}")
        return

    new_engagement = get_op5_engagement() + "\n\n"
    new_content = content[:start_idx] + new_engagement + content[end_idx:]

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Updated Operation 5 successfully!")

if __name__ == "__main__":
    update_operation_5()
