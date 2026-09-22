#!/usr/bin/env python3
"""
tools/expand_katabagil_p1.py
Expands Passage 1 (Cryptasu - The Drowned Catacombs) in SOMNARAK-WORLD/Katabagil/Passage_1_Cryptasu.md
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

def get_p1_engagement():
    dossier_box = make_box("APEX BOSS DOSSIER: SECC-012 'THE DROWNED GUARDIAN'", [
        "APEX TARGET        : SECC-012 'The Drowned Guardian of Year Zero'",
        "CLASSIFICATION     : Major-γ (Grade-γ Potency) | Abyssal Gatekeeper",
        "ENCOUNTER DOMAIN   : Strata 1 Nadir Reservoir (-150m Depth)",
        "---",
        "BOSS COMBAT PROFILE (SECC-012):",
        "- Total Health (HP): 2,400 HP | Posture Pool: 260/260",
        "- Stagger 1 Proc   : 60% Posture Strain (156 Posture) / Siphon Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Terminal Pacification)",
        "- Resistances      : Grudge 2.0x (Fatal), Lament 0.5x, Void 1.0x",
        "---",
        "TARGETABLE COMPONENT PARTS:",
        "1. Left Siphon Arm : 600 HP | Posture 180/180 (Siphons brine / AoE)",
        "2. Bronze Cleaver  : 800 HP | Posture 200/200 (Sweeping blade cleave)",
        "3. Weeping Core    : 1,000 HP | Posture 260/260 (Liquid Han reservoir)"
    ])

    hud_t01 = make_box("TACTICAL STAGE HUD: PASSAGE 01 — BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 — STRATA 1 FLOODED RESERVOIR (-150M)]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]   [HARIN]  [DOHA]  [YEON]  [BOSS]   [SORA]  [MINJAE][JISOO]         [SILENT]",
        "                                 [SIPHON]                                 ",
        "---",
        "- Node 01: Borehole Drillhead / Armored Rig 'The Iron Mole' Staging",
        "- Node 02: Harin (Vanguard Band 1 / Pneumatic Bulwark Bastion)",
        "- Node 03: Doha (Point-Blank Band 1 / Calcified Pneumatic Ram)",
        "- Node 04: Yeonhwa (Mid-Field Band 3 / Sonar Target Lock Theodolite)",
        "- Node 05: SECC-012 Drowned Guardian (Left Siphon & Right Cleaver)",
        "- Node 06: Sora (Mid-Field Band 3 / Silver Cowl Mnemonic Threads)",
        "- Node 07: Minjae (Rear Band 4 / Archival Telemetry Slate)",
        "- Node 08: Jisoo (Rear Band 5 / Cryo Harpoon Logistics Berth)",
        "- Node 10: The Silent One (High Basalt Arch / Severed Relic Cleaver)",
        "---",
        "- Harin       : Spd 4 -> 2 AP | HP 4,200/4,200 | SP 45/50 | Posture 180/180",
        "- Silent One  : Spd 7 -> 4 AP | HP 3,100/3,100 | SP 40/40 | Posture 120/120",
        "- Doha        : Spd 5 -> 3 AP | HP 3,600/3,600 | SP 40/40 | Posture 150/150",
        "- Sora        : Spd 7 -> 4 AP | HP 2,600/2,600 | SP 50/50 | Posture 100/100",
        "- Yeonhwa     : Spd 7 -> 4 AP | HP 2,700/2,700 | SP 45/45 | Posture 100/100",
        "- Boss Core   : Spd 4 -> 2 AP | HP 1,000/1,000 | Posture 260/260 [SUBMERGED]",
        "- Siphon Arm  : Spd 6 -> 3 AP | HP 600/600     | Posture 180/180 [SIPHONING]",
        "- Bronze Blade: Spd 4 -> 2 AP | HP 800/800     | Posture 200/200 [ARMED]"
    ])

    hud_t02 = make_box("TACTICAL STAGE HUD: PASSAGE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — SIPHON BREAK & OVERDRIVE PISTON]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]            [HARIN] [DOHA]  [BOSS]   [YEON]  [SORA]  [MINJAE][JISOO] [SILENT]",
        "                                 [SIPHON]                                 ",
        "---",
        "- Node 03: Harin (Advancing / Absorbing Cleave with Pneumatic Bulwark)",
        "- Node 04: Doha (Pneumatic Overdrive: Bedrock Piston Smashes Siphon)",
        "- Node 05: SECC-012 Drowned Guardian (Siphon Arm Destroyed 0/600 HP)",
        "- Node 06: Yeonhwa (Sonar Target Lock Synchronizing Flank Slashes)",
        "- Node 07: Sora (Silver Cowl Nullifying Ambient Weeping Brine)",
        "- Node 10: The Silent One (Twin Pale Flurry Severing Hydraulic Hoses)",
        "---",
        "- Doha        : Spd 7 -> 4 AP [SURGE] | HP 3,600/3,600 | SP 44/50 | Posture 150/150",
        "- Silent One  : Spd 9 -> 5 AP [SURGE] | HP 3,100/3,100 | SP 46/50 | Posture 120/120",
        "- Boss Core   : Spd 3 -> 1 AP | HP 1,000/1,000 | Posture 204/260",
        "- Siphon Arm  : DESTROYED (0/600 HP) | DELUGE ULTIMATE CANCELLED",
        "- Bronze Blade: Spd 3 -> 1 AP | HP 800/800     | Posture 146/200"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: PASSAGE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — STAGGER THRESHOLD 1 & DUAL DEFENSE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]            [HARIN] [DOHA]  [BOSS]   [YEON]  [SORA]  [SILENT]        [JISOO] ",
        "---",
        "- Node 03: Harin & Doha (Joint Bulwark Stance vs Executioner's Cleave)",
        "- Node 05: SECC-012 Drowned Guardian (STAGGER LEVEL 1 / DEFENSES 0)",
        "- Node 06: Yeonhwa (Acoustic Dart Stripping Exposed Bronze Rivets)",
        "- Node 07: Sora (Silver Cowl Empathic Ward Granting +3 Clash Power)",
        "- Node 08: The Silent One (Relic Cleaver Driving into Weeping Core)",
        "---",
        "- Harin       : Spd 6 -> 3 AP [SURGE] | HP 4,120/4,200 | SP 48/50 | Posture 180/180",
        "- Boss Core   : Spd 0 -> 0 AP | HP 714/1,000   | Posture 92/260 [STAGGER LEVEL 1]",
        "- Bronze Blade: Spd 0 -> 0 AP | HP 440/800     | Posture 88/200 [CRACKED]",
        "- Total Boss  : HP 1,672/2,400 [THRESHOLD BREACHED / TAKES 1.5X DAMAGE]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: PASSAGE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — MAXIMUM BURST & THRESHOLD SKIP]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]                    [HARIN] [BOSS]   [DOHA]  [SILENT][YEON]  [SORA]  [JISOO] ",
        "---",
        "- Node 04: Harin (Piston Pummel Securing Dais Perimeter)",
        "- Node 05: SECC-012 Drowned Guardian (Unconscious from Stagger Strain)",
        "- Node 06: Doha (Hydraulic Bedrock Shatter Crushing Bronze Thorax)",
        "- Node 07: The Silent One (Severing Void Arc Slicing Weeping Core)",
        "- Node 08: Yeonhwa & Sora (Acoustic Needle Volley Suppressing Core)",
        "- Node 10: Jisoo (Cryo Harpoon Anchoring Base of Petrified Throne)",
        "---",
        "- Silent One  : Spd 10 -> 5 AP [BURST CRIT] | HP 3,100/3,100 | SP 50/50",
        "- Boss Core   : Spd 0 -> 0 AP | HP 314/1,000   | Posture 40/260",
        "- Bronze Blade: Spd 0 -> 0 AP | HP 220/800     | Posture 32/200",
        "- Total Boss  : HP 754/2,400 [BURST DAMAGE 918! SECOND THRESHOLD SKIPPED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: PASSAGE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — THE ANCIENT PRAYER & CLEAVER AMPUTATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]                    [HARIN] [BOSS]   [SILENT][DOHA]  [YEON]  [SORA]  [JISOO] ",
        "---",
        "- Node 04: Harin (Absorbing Boiling Psychic Shockwave)",
        "- Node 05: SECC-012 (Recovering / Blazing Cyan Whirlpool / Psychic Han)",
        "- Node 06: The Silent One (Relic Overdrive: Primordial Severance Cleave)",
        "- Node 07: Doha (Anchoring Bedrock Jacks Against Fluvial Vortex)",
        "- Node 09: Sora (Cranial Silver Chorus Restores +20 SP Across Squad)",
        "---",
        "- Sora        : Spd 7 -> 4 AP | HP 2,600/2,600 | SP 50/50 | CHORUS ACTIVE",
        "- Boss Core   : Spd 3 -> 1 AP | HP 312/1,000   | Posture 20/260",
        "- Bronze Blade: DESTROYED (0/800 HP) | CLEAVER SHATTERED INTO SHARDS",
        "- Total Boss  : HP 312/2,400 [DISARMED & WEEPING / POSTURE FAILING]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: PASSAGE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — THE FINAL RELEASE & FIRST SLUICE KEY]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]                            [SORA]   [HARIN] [DOHA]  [YEON]  [SILENT][GATE]  ",
        "                                 [REST]                           [MINJAE][JISOO] ",
        "---",
        "- Node 05: SECC-012 Drowned Guardian (PACIFIED & DISSOLVING PEACEFULLY)",
        "- Node 06: Sora (Empathic Solace Communion on Cracked Core)",
        "- Node 07: Harin & Doha (Securing the Great Crypta Gate Sluice)",
        "- Node 08: Yeonhwa (Scanning Strata 2 Stairwell Wireframe)",
        "- Node 09: Minjae & Jisoo (Extracting 'The First Sluice Key')",
        "- Node 10: Great Crypta Gate (Unlocked Permanently to Strata 2)",
        "---",
        "- Vanguard Squad: Zero Fatalities | Composure 50/50 SP (Tranquil)",
        "- Encounter Status: 100% PACIFIED | Pathway to Petrobyeok OPEN"
    ])

    return f"""### The Vanguard Squad Combat Loadout

| Specialist | Position & Range Band | Primary Armament | Active Tactical Role | M.A.W.-W Class | Current SP |
|---|---|---|---|---|---|
| **Harin** | Band 1 (Melee Front) | *The Bastion of the Low* | Kinetic Tanking, Aggro Redirection, Shockwave Bash | Heavy (Spd -1, Poise +25) | 45/50 SP |
| **The Silent One**| Band 1 (Melee Striker)| *Severed Relic Cleaver* | Void/Grudge Executioner, Part Amputation | Medium (Spd 0, Crit +30%) | 40/40 SP |
| **Doha** | Band 2 (Close Sapper) | *Calcified Pneumatic Ram* | Bedrock Sapping, Armor Shattering, Stagger Accel | Medium (Spd 0, Poise +20) | 40/40 SP |
| **Sora** | Band 3 (Mid Support) | *Silver Slumber Cowl* | Resonance Tuning, Team SP Recovery, Empathic Ward | Light (Spd +1, SP Rec +15)| 50/50 SP |
| **Yeonhwa** | Band 4 (Ranged Command)| *The Horizon Theodolite* | Sonar Weakpoint Tagging, Clash Redirection | Light (Spd +1, Evasion +15%)| 45/45 SP |
| **Minjae** | Band 4 (Forensic Scribe)| *Year Zero Archaeological Slate*| Historical Telemetry, Structural Analysis | Light (Spd +1, Scan +20%) | 45/45 SP |
| **Jisoo** | Band 5 (Logistics Rear)| *High-Pressure Cryo Harpoon*| Ballast Accounting, Munition Distribution | Light (Spd +1, Ballast 81%) | 45/45 SP |

---

### Turn-Based Combat Gauntlet: The Battle for the Gate

```text
{dossier_box}
```

---

```text
{hud_t01}
```

###### Turn 01 Action Resolution Log (Establishing the Formation & Brine Torrent Deflection)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Harin activates `[Pneumatic Bulwark Stance]`: Grants herself and adjacent allies $+3$ Protection; intercepts the highest speed enemy clash targeting Band 1–2.
  * Yeonhwa initializes `[Sonar Target Lock]`: Focuses acoustic theodolite sensors on the Left Hydraulic Siphon Arm, increasing squad stagger damage against it by $+25\%$.
  * Sora deploys `[Silver Cowl: Empathic Nullification]`, neutralizing the reservoir's ambient acoustic weeping.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Harin (Speed 4 -> 2 AP, M.A.W.-W Heavy Armor delta $-1$, Poise $+25$): Holds Node 02. Spends 2 AP on `[Pneumatic Bulwark: Kinetic Deflection]`.
  * The Silent One (Speed 7 -> 4 AP, M.A.W.-W Medium delta $0$, Crit $+30\%$): Holds high arch flank at Node 10. Spends 2 AP on `[Severing Parry]`. Holds 2 AP in Reserve.
  * Doha (Speed 5 -> 3 AP, M.A.W.-W Medium delta $0$, Poise $+20$): Advances to Node 03. Spends 2 AP on `[Pneumatic Hammer Strike]`. Holds 1 AP in Guard.
  * Sora (Speed 7 -> 4 AP, M.A.W.-W Light delta $+1$): Holds Node 06. Spends 2 AP on `[Empathic Nullification Ward]`. Holds 2 AP in Reserve.
  * Yeonhwa (Speed 7 -> 4 AP, M.A.W.-W Light delta $+1$): Holds Node 04. Spends 2 AP on `[Sonar Target Lock: Siphon Frequency]`, 2 AP on `[Acoustic Resonance Dart]`.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 02 to 05)**: SECC-012 Slot 1 (Left Siphon) fires `[Pressurized Brine Torrent]` (Base 16 + 2 Coins = 26 Power, Heavy Lament/Brine) toward Node 02.
    * Harin intercepts with `[Pneumatic Bulwark: Kinetic Deflection]` (Base 18 + 2 Coins = 32 Power, Kinetic Shield).
    * **Clash Outcome**: Harin WINS THE CLASH (32 vs 26)!
    * The high-pressure brine torrent splits cleanly across the reinforced tungsten shield rim (`[P3: Parry/Protection]`). Harin takes 0 damage.
    * Harin reflects **140 kinetic tremor damage** back through the water jet into the Left Siphon Arm, inflicting $+38$ Posture Strain!
  * **Clash 2 (Node 10 to 05)**: SECC-012 Slot 2 (Bronze Cleaver) unleashes `[Sweeping Cleave]` (Base 17 + 1 Coin = 25 Power, Heavy Slash).
    * The Silent One clashes with `[Severing Parry]` (Base 20 + 2 Coins = 30 Power, Void/Slash).
    * **Clash Outcome**: The Silent One WINS THE CLASH (30 vs 25)!
    * Parries the colossal cleaver with a razor-thin blade deflection; counter-slashes for **172 Grudge damage** into the titan's bronze wrist!
  * **Unopposed Tactical Fire**:
    * Doha lands `[Pneumatic Hammer Strike]` directly on the siphon's intake coupling, dealing **144 Weight damage**!
    * Yeonhwa's `[Acoustic Resonance Dart]` chips away 68 HP from the siphon housing.
- **Step 4: Turn End State**:
  * Left Siphon Arm HP: 600 -> **236/600** | Posture: **104/180**.
  * Total Boss HP: 2,400 -> **2,016/2,400** | Posture: **204/260**.
  * Vanguard Composure: **100% (All SP > 45)**. Zero damage taken.

---

```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Breaking the Siphon & Piston Shatter)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Doha and The Silent One both trigger `Momentum Surge` (+2 Speed on Turn 02).
  * SECC-012 activates `[Deluge of the First Day]`: The siphon begins drawing thousands of liters of reservoir brine to drown the chamber.
  * Yeonhwa warns: *"Focus the left arm! If that piston completes its cycle, the chamber submerges under three atmospheres of pressurized brine!"*
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Doha (Speed 7 -> 4 AP [Surge]): Steps from Node 03 to Node 04. Spends 3 AP on `[Pneumatic Overdrive: Bedrock Piston]`.
  * The Silent One (Speed 9 -> 5 AP [Surge]): Drops from Node 10 onto the siphon sleeve at Node 05. Spends 3 AP on `[Twin Pale Flurry]`.
  * Harin (Speed 4 -> 2 AP): Steps to Node 03, executing `[Vanguard Taunt]` (2 AP) to draw the Bronze Cleaver away from the strikers.
  * Yeonhwa (Speed 7 -> 4 AP): Casts `[Resonance Pulse: Target Siphon]` (2 AP).
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 03 to 05)**: SECC-012 strikes with `[Bronze Cleaver Smash]` (Power 24, Slash).
    * Harin absorbs the strike with `[Bulwark Iron Body]` (Power 28, Heavy Guard).
    * **Clash Outcome**: Harin absorbs the blow safely, taking only 18 mitigated chip damage (HP: 4,182/4,200).
  * **Piston Demolition Assault on Siphon**:
    * Doha unleashes `[Bedrock Piston]` (Base 21 + 2 Coins Heads = 33 Power, Heavy Blunt):
      * Smashes directly through the siphon's hydraulic valve casing!
      * Deals **380 Blunt damage** and $+64$ Posture Strain!
    * The Silent One follows up with `[Twin Pale Flurry]` (Base 19 + 2 Coins Heads = 31 Power, Void Slash):
      * Slices through the brass intake hoses, dealing **220 Void damage**!
    * **TARGETED PART DESTROYED**: The Left Hydraulic Siphon Arm shears clean off the shoulder, exploding into scrap bronze and waterlogged bone (**Siphon HP: 0/600**)!
    * **EFFECT**: Boss ultimate `[Deluge of the First Day]` is permanently cancelled! Boss permanently loses 1 Speed Slot!
- **Step 4: Turn End State**:
  * Left Siphon Arm: **DESTROYED (0/600 HP)**.
  * Total Boss HP: 2,016 -> **1,890/2,400** | Posture: **146/260 [SIPHON SHATTERED]**.
  * Vanguard Composure: Harin 48 SP, Doha 44 SP, Silent One 46 SP, Sora 50 SP, Yeonhwa 45 SP.

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Pushing the First Stagger Threshold & Dual Defense)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Shorn of its siphon arm, the titan roars—a blast of acoustic Han that vibrates through the water.
  * It raises its massive Bronze Cleaver in two hands, channeling `[Executioner's Judgment]` (3 Coins, Fatal Grudge damage).
  * Harin gains `Momentum Surge` (+2 Speed -> Net Speed 6, 3 AP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Harin (Speed 6 -> 3 AP): Steps to Node 03. Spends 2 AP on `[Unbreakable Ward]`.
  * Doha (Speed 5 -> 3 AP): Props his calcified ram beneath Harin's shield to lock the frame (2 AP on `[Assisted Bulwark Anchor]`).
  * Sora (Speed 7 -> 4 AP): Casts `[Silver Cowl: Empathic Ward]` (2 AP), granting $+3$ Clash Power to all frontline allies.
  * The Silent One (Speed 7 -> 4 AP): Maneuvers into the Band 1 flank at Node 08. Spends 3 AP on `[Relic Cleaver: Core Thrust]`.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 03 to 05)**: SECC-012 unleashes `[Executioner's Judgment]` (Base 21 + 3 Coins = 31 Power, Fatal Grudge).
    * Harin and Doha execute `[Joint Unbreakable Ward]` (Base 22 + Cowl Bonus $+3$ + 2 Coins = 37 Power).
    * **Clash Outcome**: VANGUARD OVERWHELMING WIN (37 vs 31)!
    * The massive bronze cleaver slams harmlessly into the reinforced tower shield. Shockwaves disperse harmlessly into the reservoir floor (`[P3: Parry/Protection]`).
  * **Flank Strike on Weeping Core**:
    * The Silent One plunges the dark relic cleaver into the exposed seams of the chest core: `[Core Thrust]` (Base 22 + 2 Coins Heads = 34 Power, Fatal Grudge 2.0x proc!).
    * Deals **218 Fatal Grudge damage** directly to the Weeping Core!
- **Step 4: STAGGER THRESHOLD 1 TRIGGERED!**:
  * Total Boss HP drops past 70% to **1,672/2,400 HP**; Posture collapses past 60% strain line!
  * **STAGGER LEVEL 1 ACTIVE!** The titan falls to one knee in the flooded basin. All defenses drop to zero; takes $+50\%$ damage across all incoming attacks!
- **Step 5: Turn End State**:
  * Total Boss HP: 1,890 -> **1,672/2,400 [THRESHOLD BREACHED: Below 1,680 HP!]**.
  * Boss Posture: **92/260 [STAGGER LEVEL 1]**.
  * Vanguard Status: Unbroken.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Maximum Burst & Threshold Skip)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * SECC-012 remains completely immobilized on its knee; zero counter-actions available.
  * The entire Vanguard coordinates an all-out offensive barrage targeting the exposed cyan core.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Doha (Speed 5 -> 3 AP): Moves to Node 06. Spends 3 AP on `[Hydraulic Bedrock Shatter]`.
  * The Silent One (Speed 10 -> 5 AP, Momentum Crit): Holds Node 07. Spends 3 AP on `[Severing Void Arc]`, 2 AP on `[Relic Flurry]`.
  * Yeonhwa (Speed 7 -> 4 AP): Stands at Node 08. Spends 2 AP on `[Acoustic Resonance Dart]`.
  * Sora (Speed 7 -> 4 AP): Stands at Node 08. Spends 2 AP on `[Lament Needle Drive]`.
  * Jisoo (Speed 7 -> 4 AP): Fires `[Cryo Harpoon Anchor]` from Node 10 (2 AP).
- **Step 3: Unopposed Stagger Punishment Rotation**:
  * Doha's `[Hydraulic Bedrock Shatter]`: Smashes through the petrified ribcage for **280 Weight damage**!
  * The Silent One's `[Severing Void Arc]`: Slices clean through the glowing core for **364 Void damage**!
  * Yeonhwa's `[Acoustic Resonance Dart]`: Pierces resonant frequencies for **126 Void damage**!
  * Sora's `[Lament Needle Drive]`: Channels silver frequencies for **148 Lament damage**!
  * Jisoo's `[Cryo Harpoon Anchor]`: Pins the chassis for **110 Pierce damage**!
  * **TOTAL BURST DAMAGE: 1,028 DAMAGE!**
- **Step 4: SECOND STAGGER THRESHOLD (960 HP) COMPLETELY SKIPPED!**:
  * Boss HP plunges from 1,672 all the way down to **644/2,400 HP**!
  * The titan's chest core cracks open wide, spilling brilliant glowing cyan liquid into the reservoir.
- **Step 5: Turn End State**:
  * Total Boss HP: 1,672 -> **754/2,400** (Core HP: **314/1,000** | Cleaver HP: **220/800**).
  * Posture: **40/260**.

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Phase 2 Escalation: The Ancient Prayer & Cleaver Amputation)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * SECC-012 recovers from stagger, its eyes blazing with brilliant pale light. The water in the reservoir begins to boil and swirl into a massive whirlpool around the throne.
  * The Guardian speaks—not through vocal cords, but by transmitting three thousand simultaneous memory fragments into the squad's cranial tethers:
    > *"We were forgotten... The surface smiled while we drowned in darkness... Join us in the deep bed!"*
  * High-pressure psychic scream hits the team! Harin SP: 48 -> 28; Doha SP: 44 -> 24.
  * Sora immediately unleashes `[Cranial Silver Chorus]`: Channeling her silver tuning needles into the bedrock, restoring $+20$ SP across the entire squad! Paranoia warning averted!
- **Step 2: Spatial Movement & Action Point Allocation**:
  * The Silent One (Speed 7 -> 4 AP): Steps forward into Node 06, activating `[Relic Overdrive: Primordial Severance]` (Cost: 3 AP, 25 SP).
  * Harin (Speed 4 -> 2 AP): Holds Node 04, bracing against the boiling whirlpool with `[Pneumatic Anchor]`.
  * Doha (Speed 5 -> 3 AP): Drops hydraulic shoring jacks into Node 07.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 06 to 05)**: SECC-012 raises its shattered Bronze Cleaver for a desperate final cleave: `[Last Stand of the Drowned]` (Base 20 + 2 Coins = 28 Power, Heavy Slash).
    * The Silent One executes `[Primordial Severance: The Unanswered Cut]` (Base 24 + 3 Coins Heads = 39 Power, Void/Slash).
    * **Clash Outcome**: The Silent One WINS THE CLASH OVERWHELMINGLY (39 vs 28)!
    * The dark blade ignites with brilliant pale white luminescence. It cuts cleanly through the remaining bronze cleaver, severing the titan's right arm at the elbow joint!
    * **TARGETED PART DESTROYED**: The three-meter executioner's bronze cleaver shatters into inert bronze shards sinking to the reservoir floor (**Cleaver HP: 0/800**)!
- **Step 4: Turn End State**:
  * Bronze Cleaver: **DESTROYED (0/800 HP)**.
  * SECC-012 is completely disarmed and helpless!
  * Total Boss HP: 754 -> **312/2,400** | Posture: **20/260 [CRITICAL COLLAPSE]**.
  * Vanguard Composure: Stable (> 45 SP across all members).

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (The Final Release & First Sluice Key)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * The Guardian drops its severed limbs into the water. Its chest core, fractured and leaking glowing cyan sorrow, pulses with a slow, fading rhythm.
  * Hostile intent drops to zero. Posture reaches **0/260 [TERMINAL PACIFICATION]**.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Sora (Speed 7 -> 4 AP): Walks forward through the shallow water from Node 08 to Node 05, stepping past Harin and Doha.
  * The Silent One, Harin, and Doha hold perimeter watch at Nodes 06–07.
  * Minjae and Jisoo advance to Node 09 to log archival telemetry and prepare salvage clamps.
- **Step 3: Empathetic Solace & Pacification Resolution**:
  * Sora places her gloved hand gently against the cracked crystalline chest core of the titan.
  * *"You have guarded this gate for four thousand years,"* Sora whispers, her voice echoing gently through the vast cavern. *"You held back the deep so the children above could walk in sunlight. Your vigil is done, guardian. Rest now."*
  * The Guardian's stone face softens. The rigid basalt features relax into a faint, peaceful expression.
  * The entity does not detonate into violent shrapnel; it quietly dissolves into pure, shimmering crystalline sand that settles softly across the reservoir floor.
- **Step 4: Operational Artifact Extraction & Strata Access**:
  * **Artifact Extracted**: `[Item: The First Sluice Key]` (Pre-Consolihan Master Relic forged of rustless Before-Time alloy).
  * **Tectonic Outcome**: The colossal stone retaining wall unlocks with a deep hydraulic hum.
  * **Descent Access**: The spiraling stairwell leading into Strata 2 (Petrobyeok / Calcified Bastion, -150m to -450m) is officially **OPEN**.
  * **Casualties**: Zero Fatalities. Harin (HP 4,182/4,200), Doha (HP 3,600/3,600). Squad Composure 50/50 SP."""

def update_passage_1():
    path = "SOMNARAK-WORLD/Katabagil/Passage_1_Cryptasu.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    start_str = "### The Vanguard Squad Combat Loadout"
    end_str = "## Chapter VIII: Epilogue — The Descent Into Strata 2"

    start_idx = content.find(start_str)
    end_idx = content.find(end_str)

    if start_idx == -1 or end_idx == -1:
        print(f"Error locating boundaries! start_idx={start_idx}, end_idx={end_idx}")
        return

    new_engagement = get_p1_engagement() + "\n\n---\n\n"
    new_content = content[:start_idx] + new_engagement + content[end_idx:]

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Updated Passage 1 successfully!")

if __name__ == "__main__":
    update_passage_1()
