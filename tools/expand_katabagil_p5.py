#!/usr/bin/env python3
"""
tools/expand_katabagil_p5.py
Expands Passage 5 (Limesteum - The Calcinated Fracture) in SOMNARAK-WORLD/Katabagil/Passage_5_Limesteum.md
Replaces the older combat gauntlet with full 10-node spatial tactical HUDs, Speed/AP breakdowns,
M.A.W.-W weight deltas, and Four P-framework action resolution logs across all 6 turns.
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

def get_p5_engagement():
    dossier_box = make_box("APEX BOSS DOSSIER: SECC-068 'ASHEN BOUNDARY SOVEREIGN'", [
        "APEX TARGET        : SECC-068 'The Ashen Boundary Sovereign'",
        "CLASSIFICATION     : Major-γ (Grade-γ Potency) | Tectonic Boundary Apex",
        "ENCOUNTER DOMAIN   : Strata 5 Calcinated Boundary Core (-2,100m Depth)",
        "---",
        "BOSS COMBAT PROFILE (SECC-068):",
        "- Total Health (HP): 4,000 HP | Posture Pool: 320/320",
        "- Stagger 1 Proc   : 60% Posture Strain (192 Posture) / Cleaver Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Terminal Solidification)",
        "- Resistances      : Lament 2.0x (Fatal), Void 1.5x, Grudge 0.5x, Weight 0.5x",
        "---",
        "TARGETABLE COMPONENT PARTS:",
        "1. Magma Cleaver   : 1,050 HP | Posture 260/260 (Sweeping molten blade)",
        "2. Slag Bastion    : 1,300 HP | Posture 280/280 (High-defense stone shield)",
        "3. Furnace Core    : 1,650 HP | Posture 320/320 (Central volcanic furnace)"
    ])

    hud_t01 = make_box("TACTICAL STAGE HUD: PASSAGE 05 — BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 — STRATA 5 BOUNDARY CORE (-2,100M)]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]   [HARIN]  [DOHA]  [SORA]  [BOSS]   [YEON]  [SILENT][MINJAE]        [JISOO] ",
        "                                 [CLEAVER]                                ",
        "---",
        "- Node 01: Bedrock Staircase Base / Armored Rig 'The Iron Mole'",
        "- Node 02: Harin (Vanguard Band 1 / Bastion of the Low Tower Shield)",
        "- Node 03: Doha (Point-Blank Band 1 / Cryo Pneumatic Fracture Ram)",
        "- Node 04: Sora (Mid-Field Band 2 / Silver Cowl Glacial Siphon)",
        "- Node 05: SECC-068 Boundary Sovereign (Magma Cleaver & Slag Bastion)",
        "- Node 06: Yeonhwa (Mid-Field Band 3 / Thermal Sonar Theodolite)",
        "- Node 07: The Silent One (High Basalt Arch / Severed Relic Cleaver)",
        "- Node 08: Minjae (Tactical Record Band 4 / Keeper's Lens & Stylus)",
        "- Node 10: Jisoo (Rear Band 5 / Cryo Harpoon Logistics Berth)",
        "---",
        "- Harin       : Spd 4 -> 2 AP | HP 4,200/4,200 | SP 46/50 | Posture 180/180",
        "- Silent One  : Spd 7 -> 4 AP | HP 3,100/3,100 | SP 42/40 | Posture 120/120",
        "- Doha        : Spd 5 -> 3 AP | HP 3,600/3,600 | SP 40/40 | Posture 150/150",
        "- Sora        : Spd 7 -> 4 AP | HP 2,600/2,600 | SP 50/50 | Posture 100/100",
        "- Yeonhwa     : Spd 7 -> 4 AP | HP 2,700/2,700 | SP 45/45 | Posture 100/100",
        "- Minjae      : Spd 7 -> 4 AP | HP 2,800/2,800 | SP 50/50 | Posture 110/110",
        "- Boss Core   : Spd 4 -> 2 AP | HP 1,650/1,650 | Posture 320/320 [BURNING]",
        "- Cleaver Arm : Spd 5 -> 3 AP | HP 1,050/1,050 | Posture 260/260 [MOLTEN]",
        "- Slag Shield : Spd 3 -> 1 AP | HP 1,300/1,300 | Posture 280/280 [VITRIFIED]"
    ])

    hud_t02 = make_box("TACTICAL STAGE HUD: PASSAGE 05 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — MAGMA CLEAVER SHATTERED & VOID CUT]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]            [HARIN] [DOHA]  [BOSS]   [SORA]  [YEON]  [MINJAE][JISOO] [SILENT]",
        "                                 [QUENCH]                                 ",
        "---",
        "- Node 03: Harin (Anchored / Deflecting Blistering Ash Convection)",
        "- Node 04: Doha (Pneumatic Fracture Ram Cracking Slag Bastion)",
        "- Node 05: SECC-068 Boundary Sovereign (Magma Cleaver Destroyed 0/1,050)",
        "- Node 06: Sora (Glacial Cascade Quenching Volcanic Joints)",
        "- Node 07: Yeonhwa (Thermal Sonar Fault Lock on Slag Shield Core)",
        "- Node 10: The Silent One (Severing Crescent Severing Tungsten Wrist)",
        "---",
        "- Silent One  : Spd 9 -> 5 AP [SURGE] | HP 3,100/3,100 | SP 46/50 | Posture 120/120",
        "- Doha        : Spd 7 -> 4 AP [SURGE] | HP 3,600/3,600 | SP 44/40 | Posture 150/150",
        "- Boss Core   : Spd 4 -> 2 AP | HP 1,650/1,650 | Posture 248/320",
        "- Cleaver Arm : DESTROYED (0/1,050 HP) | AOE MAGMA WAVE PERMANENTLY SEALED",
        "- Slag Shield : Spd 3 -> 1 AP | HP 980/1,300   | Posture 210/280"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: PASSAGE 05 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — STAGGER THRESHOLD 1 & SHIELD BREACH]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]            [HARIN] [DOHA]  [BOSS]   [SORA]  [YEON]  [SILENT]        [JISOO] ",
        "---",
        "- Node 03: Harin (Piston Shield Wall Bracing Against Shrapnel)",
        "- Node 04: Doha (Sapper Counter-Lever Shattering Vitrified Shield)",
        "- Node 05: SECC-068 (STAGGER LEVEL 1 / DEFENSES COLLAPSED / IMMOBILIZED)",
        "- Node 06: Sora (Chime of Quenched Slag Weakening Furnace Grates)",
        "- Node 07: Yeonhwa (Directing Optical Theodolite Beam on Core)",
        "- Node 08: The Silent One (Preparing Void Core Penetration)",
        "---",
        "- Harin       : Spd 6 -> 3 AP [SURGE] | HP 4,200/4,200 | SP 48/50 | Posture 180/180",
        "- Boss Core   : Spd 0 -> 0 AP | HP 1,540/1,650 | Posture 122/320 [STAGGER LEVEL 1]",
        "- Slag Shield : Spd 0 -> 0 AP | HP 480/1,300   | Posture 94/280 [BREACHED]",
        "- Total Boss  : HP 2,520/4,000 [THRESHOLD BREACHED / TAKES 1.5X DAMAGE]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: PASSAGE 05 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — MAXIMUM BURST & PHASE 2 THRESHOLD SKIP]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]                    [HARIN] [BOSS]   [DOHA]  [SILENT][YEON]  [SORA]  [JISOO] ",
        "---",
        "- Node 04: Harin (Bulwark Kinetic Pummel Crushing Knee Hinges)",
        "- Node 05: SECC-068 Boundary Sovereign (Staggered / Furnace Flaring)",
        "- Node 06: Doha (Sapper Thermite Detonation Searing Magma Pipes)",
        "- Node 07: The Silent One (The Burden Cleave Driving into Heart)",
        "- Node 08: Yeonhwa & Sora (Theodolite Laser & Glacial Repose)",
        "- Node 10: Jisoo (Cryo Harpoon Anchoring Cooling Leg Joints)",
        "---",
        "- Silent One  : Spd 10 -> 5 AP [BURST CRIT] | HP 3,100/3,100 | SP 50/50",
        "- Boss Core   : Spd 0 -> 0 AP | HP 440/1,650   | Posture 52/320",
        "- Slag Shield : DESTROYED (0/1,300 HP)",
        "- Total Boss  : HP 1,100/4,000 [BURST DAMAGE 1,420! SECOND THRESHOLD SKIPPED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: PASSAGE 05 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TECTONIC FISSURE & CHRONICLE OF TRUTH]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]                    [HARIN] [BOSS]   [MINJAE][SILENT][YEON]  [SORA]  [JISOO] ",
        "                                                  [DOHA]                          ",
        "---",
        "- Node 04: Harin (Shielding Squad From 600°C Tectonic Ash Wave)",
        "- Node 05: SECC-068 (Cataclysmic Tectonic Fissure / Volcanic Rift)",
        "- Node 06: Minjae (Relic Overdrive: UNVARNISHED CHRONICLE OF TRUTH)",
        "- Node 07: The Silent One & Doha (Readying Void Cleave on Keystone)",
        "- Node 09: Sora (Chime of Quenched Slag Calming Tectonic Spores)",
        "---",
        "- Minjae      : Spd 8 -> 4 AP [OVERDRIVE] | HP 2,800/2,800 | SP 50/50 [TABLETS]",
        "- Boss Core   : Spd 4 -> 2 AP | HP 440/1,650   | Posture 26/320 [FREEZING]",
        "- Total Boss  : HP 440/4,000 [TECTONIC CATACLYSM BOUND & AVERTED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: PASSAGE 05 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — OBSIDIAN SOLIDIFICATION & BORDER KEYSTONE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]                            [MINJAE] [SILENT][HARIN] [DOHA]  [SORA]  [SHAFT] ",
        "                                 [REST]                           [YEON]  [JISOO] ",
        "---",
        "- Node 05: SECC-068 Boundary Sovereign (PACIFIED & SOLIDIFIED TO OBSIDIAN)",
        "- Node 06: Minjae (Extracts 'Keystone of the Fractured Border')",
        "- Node 07: The Silent One (Parts Keystone Furnace Core with Void Cleave)",
        "- Node 08: Harin & Doha (Securing Unsealed Tectonic Vents & Shaft Edge)",
        "- Node 10: Vertical Bedrock Shaft (Pathway to Strata 6 Traumagol OPEN)",
        "---",
        "- Vanguard Squad: Zero Fatalities | Composure 50/50 SP (Dignified)",
        "- Encounter Status: 100% PACIFIED | Pathway to Traumagol OPEN"
    ])

    return f"""### The Vanguard Squad Combat Loadout

| Specialist | Position & Range Band | Primary Armament | Active Tactical Role | M.A.W.-W Class | Current SP |
|---|---|---|---|---|---|
| **Minjae** | Band 4 (Tactical Record)| *The Keeper's Lens & Stylus*| Truth Resonance, Tectonic Anchor, Chron | Light (Spd +1, Scan +20%) | 50/50 SP |
| **Harin** | Band 1 (Melee Front) | *The Bastion of the Low* | Kinetic Wall, Slag Redirection, Shockwave | Heavy (Spd -1, Poise +25) | 46/50 SP |
| **Doha** | Band 1 (Melee Front) | *Calcified Pneumatic Ram* | Bedrock Fracture, Slag Sapping, Thermite | Medium (Spd 0, Poise +20) | 40/40 SP |
| **The Silent One**| Band 1 (Melee Striker)| *Severed Relic Cleaver* | Void Executioner, Cleaver Amputation | Medium (Spd 0, Crit +30%) | 42/40 SP |
| **Sora** | Band 2 (Mid Support) | *Silver Slumber Cowl* | Glacial Lament Resonance, Slag Quenching | Light (Spd +1, SP Rec +15)| 50/50 SP |
| **Yeonhwa** | Band 3 (Ranged Command)| *The Horizon Theodolite* | Thermal Fault Tagging, Acoustic Lock | Light (Spd +1, Evasion +15%)| 45/45 SP |
| **Jisoo** | Band 5 (Logistics Rear)| *High-Pressure Cryo Harpoon*| Ballast Accounting, Winch Rigging | Light (Spd +1, Ballast 52%) | 45/45 SP |

---

### Turn-Based Combat Gauntlet: Extinguishing the Border Sovereign

```text
{dossier_box}
```

---

```text
{hud_t01}
```

###### Turn 01 Action Resolution Log (Intercepting the Molten Cleaver)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Harin activates `[Vow of the Low Bulwark]`: Drives shield spikes into the basalt floor; gains $+3$ Protection and intercepts the Sovereign's primary molten sweep.
  * Sora initializes `[Glacial Cascade]`: Prepares cryo-lament water reservoirs to quench molten basalt armor.
  * Yeonhwa casts `[Thermal Sonar Lock]`: Tags the overheated wrist joint of the Calcinated Magma Cleaver.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Harin (Speed 4 -> 2 AP, M.A.W.-W Heavy Armor delta $-1$, Poise $+25$): Holds Node 02. Spends 2 AP on `[Vow of the Low Bulwark: Kinetic Wall]`.
  * The Silent One (Speed 7 -> 4 AP, M.A.W.-W Medium delta $0$, Crit $+30\%$): Perches on high basalt arches at Node 07. Spends 2 AP on positioning.
  * Doha (Speed 5 -> 3 AP, M.A.W.-W Medium delta $0$, Poise $+20$): Holds Node 03. Spends 2 AP on `[Pneumatic Fracture Ram]`. Holds 1 AP in Guard.
  * Sora (Speed 7 -> 4 AP, M.A.W.-W Light delta $+1$): Holds Node 04. Spends 2 AP on `[Glacial Cascade]`. Holds 2 AP in Reserve.
  * Yeonhwa (Speed 7 -> 4 AP, M.A.W.-W Light delta $+1$): Holds Node 06. Spends 2 AP on `[Thermal Sonar Lock]`, 2 AP on `[Acoustic Dart]`.
  * Minjae (Speed 7 -> 4 AP, M.A.W.-W Light delta $+1$): Stands at Node 08, recording structural fault vectors.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 02 to 05)**: SECC-068 unleashes `[Molten Slag Cleave]` (Base 17 + 2 Coins = 27 Power, Heavy Grudge/Heat).
    * Harin intercepts with `[Vow of the Low Bulwark: Kinetic Wall]` (Base 20 + 2 Coins = 32 Power, Kinetic Shield).
    * **Clash Outcome**: Harin WINS THE CLASH OVERWHELMINGLY (32 vs 27)!
    * Harin plants her shield into the basalt floor; impact sparks cascade across the rift as the molten magma cleaver is deflected cleanly (`[P3: Parry/Protection]`).
    * Harin reflects **230 kinetic tremor damage** back into the cleaver arm, inflicting $+48$ Posture Strain!
  * **Elemental Weakness Exploitation**:
    * Sora unleashes `[Glacial Cascade]` directly into the glowing magma wrist joint:
      * Siphon of glacial Lament brine strikes boiling volcanic rock (Fatal 2.0x proc!).
      * Deals **190 Cryo-Lament damage**! The molten rock hissingly blackens into brittle, vitrified slag.
- **Step 4: Turn End State**:
  * Calcinated Magma Cleaver HP: 1,050 -> **630/1,050** | Posture: **168/260 [QUENCHING]**.
  * Total Boss HP: 4,000 -> **3,580/4,000** | Posture: **272/320**.
  * Vanguard Composure: **100% (All SP > 45)**. Zero damage taken.

---

```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Part Destruction: Magma Cleaver Shattered)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * The Silent One and Doha activate `Momentum Surge` (+2 Speed on Turn 02).
  * SECC-068 attempts `[Volcanic Backhand Sweep]` targeting the mid-line ranks.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * The Silent One (Speed 9 -> 5 AP [Surge]): Drops from overhead basalt arches at Node 07 onto the glowing cleaver wrist at Node 05. Spends 3 AP on `[Severing Crescent: Void Cleave]`.
  * Doha (Speed 7 -> 4 AP [Surge]): Steps from Node 03 to Node 04. Spends 3 AP on `[Pneumatic Fracture Ram]`.
  * Harin (Speed 4 -> 2 AP): Holds Node 03, deflecting blistering ash convection with `[Bulwark Stance]`.
  * Sora (Speed 7 -> 4 AP): Holds Node 06, pouring pressurized cryo-water across the furnace vents (2 AP).
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 07 to 05)**: SECC-068 swings with `[Volcanic Backhand Sweep]` (Base 17 + 2 Coins = 27 Power, Heavy Grudge).
    * The Silent One executes `[Severing Crescent: Void Cleave]` (Base 23 + 3 Coins Heads = 41 Power, Void Slash).
    * **Clash Outcome**: The Silent One WINS THE CLASH OVERWHELMINGLY (41 vs 27)!
    * The dark relic cleaver slices cleanly through the vitrified tungsten wrist joint!
    * Deals **480 Critical Void damage** (Fatal 2.0x proc!)!
    * **TARGETED PART DESTROYED**: The Calcinated Magma Cleaver shears off and plunges into the magma lake, exploding into boiling steam (**Cleaver HP: 0/1,050**)!
    * **EFFECT**: Boss AoE magma wave attack permanently sealed; boss permanently loses 1 Speed Slot!
  * **Slag Bastion Shield Damage**:
    * Doha's `[Pneumatic Fracture Ram]` cracks the Vitrified Slag Bastion, dealing **240 Blunt damage**!
- **Step 4: Turn End State**:
  * Calcinated Magma Cleaver: **DESTROYED (0/1,050 HP)**.
  * Vitrified Slag Bastion: 1,300 -> **980/1,300** | Posture: **210/280**.
  * Total Boss HP: 3,580 -> **3,080/4,000** | Posture: **206/320 [CLEAVER SHATTERED]**.
  * Vanguard Composure: Stable (> 44 SP across all members).

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (First Stagger Proc & Shield Breach)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * SECC-068 attempts a desperate shield slam: `[Tectonic Bash]` (Heavy Weight, 2 Coins).
  * Doha gains `Momentum Surge` (+2 Speed -> Net Speed 7, 4 AP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Doha (Speed 7 -> 4 AP): Steps to Node 04. Spends 2 AP on `[Sapper Counter-Lever]`.
  * Harin (Speed 6 -> 3 AP): Steps to Node 03. Spends 2 AP on `[Piston Shield Wall]`.
  * Sora (Speed 7 -> 4 AP): Casts `[Chime of Quenched Slag]` (2 AP), weakening furnace grates.
  * Yeonhwa (Speed 7 -> 4 AP): Casts `[Acoustic Theodolite Laser]` (2 AP).
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 04 to 05)**: SECC-068 slams forward with `[Tectonic Bash]` (Base 16 + 2 Coins = 24 Power, Heavy Weight).
    * Doha clashes with `[Sapper Counter-Lever]` (Base 20 + 2 Coins = 32 Power, Heavy Lever).
    * **Clash Outcome**: Doha WINS THE CLASH (32 vs 24)!
    * Doha levers his tungsten sapper spike into the vitrified shield core; the pneumatic piston fires with concussive force!
    * The Slag Bastion shatters into burning gravel, dealing **420 Blunt damage** and $+76$ Posture Strain!
- **Step 4: STAGGER THRESHOLD 1 TRIGGERED!**:
  * Total Boss HP crosses 70% threshold (2,800 HP), falling to **2,520/4,000 HP**; Posture crosses 60% strain line!
  * **STAGGER LEVEL 1 ACTIVE!** The titan falls to its knees in the cooling ash; all defenses drop to zero; takes $+50\%$ damage across all incoming attacks!
- **Step 5: Turn End State**:
  * Total Boss HP: 3,080 -> **2,520/4,000 [THRESHOLD BREACHED: Below 2,800 HP!]**.
  * Slag Bastion: 980 -> **480/1,300** | Posture: **94/280 [BREACHED]**.
  * Boss Posture: **122/320 [STAGGER LEVEL 1]**.
  * Vanguard Status: Unbroken.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Maximum Burst & Phase 2 Threshold Skip)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * SECC-068 remains completely immobilized on its knees; the Boundary Furnace Core in its chest is flaring white heat through shattered grates.
  * All Vanguard Specialists coordinate maximum burst fire targeting the central furnace core.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * The Silent One (Speed 10 -> 5 AP, Momentum Crit): Stands at Node 07. Spends 3 AP on `[The Burden Cleave: Core Strike]`.
  * Harin (Speed 4 -> 2 AP): Steps to Node 04. Spends 2 AP on `[Bulwark Kinetic Pummel]`.
  * Doha (Speed 5 -> 3 AP): Moves to Node 06. Spends 3 AP on `[Sapper Thermite Detonation]`.
  * Yeonhwa (Speed 7 -> 4 AP): Stands at Node 08. Spends 2 AP on `[Acoustic Theodolite Laser]`.
  * Jisoo (Speed 7 -> 4 AP): Fires `[Cryo Harpoon Anchor]` from Node 10 (2 AP).
- **Step 3: Unopposed Stagger Punishment Rotation**:
  * The Silent One's `[Core Strike]`: Slices through the glowing core for **590 Void damage** (Weakness 1.5x proc!)!
  * Harin's `[Bulwark Kinetic Pummel]`: Smashes knee hinges for **260 Weight damage**!
  * Doha's `[Sapper Thermite Detonation]`: Sockets incendiary charges into magma pipes for **340 Grudge damage**!
  * Yeonhwa's `[Acoustic Theodolite Laser]`: Focuses resonance for **230 Void damage**!
  * **TOTAL BURST DAMAGE: 1,420 DAMAGE!**
- **Step 4: SECOND STAGGER THRESHOLD (1,600 HP) COMPLETELY SKIPPED!**:
  * Boss HP plunges from 2,520 down to **1,100/4,000 HP**! Slag Bastion completely destroyed (0/1,300 HP)!
  * **Phase 2 Emergency Activation Triggered!**
- **Step 5: Turn End State**:
  * Total Boss HP: 2,520 -> **1,100/4,000** (Core HP: **440/1,650** | Bastion: **DESTROYED**).
  * Posture: **52/320**.

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Phase 2 Escalation: Tectonic Fissure & Chronicle of Truth)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Sovereign awakens in volcanic desperation; subterranean gas pockets ignite across the concourse!
  * Boss Special Skill: `[Cataclysmic Tectonic Fissure]` (Tectonic Cataclysm, 3 Coins).
  * Speed Dice expands to 4 slots! Ash and molten rock engulf the rift floor.
  * Minjae activates Relic Overdrive: `[UNVARNISHED CHRONICLE OF TRUTH — MAXIMUM]` (Cost: 3 AP, 30 SP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Minjae (Speed 8 -> 4 AP [Overdrive]): Steps onto the fault line at Node 06, projecting the Keeper Tablets into the air.
  * Harin (Speed 4 -> 2 AP): Shields the squad from 600°C ash waves at Node 04 with `[Bulwark Wall]`.
  * Doha (Speed 5 -> 3 AP): Drops tectonic anchors into Node 06.
  * The Silent One (Speed 7 -> 4 AP): Prepares `[Void Overdrive Cleave]` at Node 07.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 06 to 05)**: SECC-068 unleashes `[Cataclysmic Tectonic Fissure]` (Base 21 + 3 Coins = 33 Power, Area Weight/Heat).
    * Minjae clashes with `[UNVARNISHED CHRONICLE OF TRUTH — MAXIMUM]` (Base 27 + 3 Coins Heads = 47 Power, Truth Resonance).
    * **Clash Outcome**: MINJAE OVERWHELMING RELIC CLASH WIN (47 vs 33)!
    * The names of the sacrificed thousand burn with blinding golden brilliance into the acoustic air!
    * Historical truth resonance binds the shifting tectonic plates together!
    * The Sovereign freezes in shock and recognition; the tectonic cataclysm is averted (`[P3: Parry/Protection]`)!
    * Zero squad damage taken! Squad Composure maxed at 50/50 SP!
- **Step 4: Turn End State**:
  * Total Boss HP: **1,100 -> 440/4,000** | Posture: **26/320 [CRITICAL COLLAPSE]**.
  * Vanguard Composure: 50/50 SP across all members.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Quenching the Core & Obsidian Solidification)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * The Sovereign's magma cools into brittle, smoking obsidian glass. Posture reaches **0/320 [TERMINAL SOLIDIFICATION]**.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Harin and Doha pin the titan's smoking legs with tungsten anchors at Nodes 07–08.
  * Sora unleashes `[Glacial Repose]`, flooding the furnace cavity with pure chilled Lament water.
  * Minjae steps up to the petrified hand at Node 06.
  * The Silent One steps onto the cooling chest rim at Node 07.
- **Step 3: Overdrive Execution & Peaceful Pacification**:
  * The Silent One delivers the final blow: `[Void Overdrive Cleave]` (Power 45).
  * The relic cleaver cleanly parts the cooling keystone furnace core.
  * Deals **1,100 Pure Void Resonance damage**! SECC-068 HP drops to 0!
  * The blinding crimson glare fades into a cool violet twilight; the molten lake solidifies into thick sheets of black volcanic glass.
- **Step 4: Operational Artifact Extraction & Strata Access**:
  * **Artifact Acquired**: `[Relic: The Keystone of the Fractured Border]` (Hexagonal block of cold white limestone carved with the seal of Year Zero).
  * **Minjae's Tribute**: Minjae presses the keystone against his chest: *"Rest now, grandfather. Your sacrifice is no longer a corporate secret. It is written in stone."*
  * **Descent Access**: The unsealed tectonic vents part, revealing a sheer, vertical shaft plunging three thousand meters straight down.
  * **Descent Destination**: Descending into Strata 6 (Traumagol / The Trauma Abyss, -2,100m to -2,800m).
  * **Casualties**: Flawless Victory. Zero Fatalities. Harin (HP 4,200/4,200), Doha (HP 3,600/3,600). Squad Composure 50/50 SP."""

def update_passage_5():
    path = "SOMNARAK-WORLD/Katabagil/Passage_5_Limesteum.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    start_str = "### The Vanguard Squad Combat Loadout"
    end_str = "## Chapter VIII: Epilogue & Acquisition"

    start_idx = content.find(start_str)
    end_idx = content.find(end_str)

    if start_idx == -1 or end_idx == -1:
        print(f"Error locating boundaries! start_idx={start_idx}, end_idx={end_idx}")
        return

    new_engagement = get_p5_engagement() + "\n\n---\n\n"
    new_content = content[:start_idx] + new_engagement + content[end_idx:]

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Updated Passage 5 successfully!")

if __name__ == "__main__":
    update_passage_5()
