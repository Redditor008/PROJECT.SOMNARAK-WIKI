#!/usr/bin/env python3
"""
tools/expand_katabagil_p2.py
Expands Passage 2 (Petrobyeok - The Calcified Bastion) in SOMNARAK-WORLD/Katabagil/Passage_2_Petrobyeok.md
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

def get_p2_engagement():
    dossier_box = make_box("APEX BOSS DOSSIER: SECC-028 'BASTION SOVEREIGN'", [
        "APEX TARGET        : SECC-028 'The Monolithic Bastion Sovereign'",
        "CLASSIFICATION     : Major-γ (Grade-γ Potency) | Bastion Core Gatekeeper",
        "ENCOUNTER DOMAIN   : Strata 2 Great Bastion Sluice Arch (-450m Depth)",
        "---",
        "BOSS COMBAT PROFILE (SECC-028):",
        "- Total Health (HP): 2,800 HP | Posture Pool: 260/260",
        "- Stagger 1 Proc   : 60% Posture Strain (156 Posture) / Hammer Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Terminal Dismantling)",
        "- Resistances      : Lament 2.0x (Fatal), Grudge/Void 1.0x, Weight 0.5x",
        "---",
        "TARGETABLE COMPONENT PARTS:",
        "1. Left Siege Hammer: 700 HP | Posture 200/200 (Overhead crushing smashes)",
        "2. Retaining Bulwark: 900 HP | Posture 220/220 (High-defense kinetic shield)",
        "3. Ancestral Furnace: 1,200 HP | Posture 260/260 (Central glowing core)"
    ])

    hud_t01 = make_box("TACTICAL STAGE HUD: PASSAGE 02 — BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 — STRATA 2 CALCIFIED BASTION (-450M)]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]   [HARIN]  [DOHA]  [SORA]  [BOSS]   [YEON]  [MINJAE][JISOO]         [SILENT]",
        "                                 [HAMMER]                                 ",
        "---",
        "- Node 01: Sluice Borehole Staging / Armored Rig 'The Iron Mole'",
        "- Node 02: Harin (Vanguard Band 1 / Bastion of the Low Tower Shield)",
        "- Node 03: Doha (Point-Blank Band 1 / Calcified Pneumatic Ram)",
        "- Node 04: Sora (Mid-Field Band 2 / Silver Cowl Lament Siphon)",
        "- Node 05: SECC-028 Bastion Sovereign (Left Hammer & Right Bulwark)",
        "- Node 06: Yeonhwa (Mid-Field Band 3 / Sonar Fault Beacon Theodolite)",
        "- Node 07: Minjae (Rear Band 4 / Structural Stress Analysis Slate)",
        "- Node 08: Jisoo (Rear Band 5 / Cryo Harpoon Logistics Berth)",
        "- Node 10: The Silent One (High Ashlar Arch / Severed Relic Cleaver)",
        "---",
        "- Harin       : Spd 4 -> 2 AP | HP 4,200/4,200 | SP 45/50 | Posture 180/180",
        "- Silent One  : Spd 7 -> 4 AP | HP 3,100/3,100 | SP 40/40 | Posture 120/120",
        "- Doha        : Spd 5 -> 3 AP | HP 3,600/3,600 | SP 40/40 | Posture 150/150",
        "- Sora        : Spd 7 -> 4 AP | HP 2,600/2,600 | SP 50/50 | Posture 100/100",
        "- Yeonhwa     : Spd 7 -> 4 AP | HP 2,700/2,700 | SP 45/45 | Posture 100/100",
        "- Boss Core   : Spd 4 -> 2 AP | HP 1,200/1,200 | Posture 260/260 [ANCHORED]",
        "- Left Hammer : Spd 5 -> 3 AP | HP 700/700     | Posture 200/200 [CRUSHING]",
        "- Right Shield: Spd 3 -> 1 AP | HP 900/900     | Posture 220/220 [DEFENDING]"
    ])

    hud_t02 = make_box("TACTICAL STAGE HUD: PASSAGE 02 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — HAMMER AMPUTATION & BEDROCK PISTON]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]            [HARIN] [DOHA]  [BOSS]   [SORA]  [YEON]  [MINJAE][JISOO] [SILENT]",
        "                                 [RUBBLE]                                 ",
        "---",
        "- Node 03: Harin (Aegis Intercept Shielding Mid-Field Specialists)",
        "- Node 04: Doha (Pneumatic Overdrive: Bedrock Piston Smashes Elbow)",
        "- Node 05: SECC-028 Bastion Sovereign (Left Hammer Destroyed 0/700 HP)",
        "- Node 06: Sora (Lament Siphon Dissolving Mortar Seams)",
        "- Node 07: Yeonhwa (Sonar Fault Lock on Retaining Bulwark)",
        "- Node 10: The Silent One (Twin Pale Flurry Slicing Tendons from Flank)",
        "---",
        "- Doha        : Spd 7 -> 4 AP [SURGE] | HP 3,600/3,600 | SP 44/50 | Posture 150/150",
        "- Silent One  : Spd 9 -> 5 AP [SURGE] | HP 3,100/3,100 | SP 46/50 | Posture 120/120",
        "- Boss Core   : Spd 3 -> 1 AP | HP 1,200/1,200 | Posture 198/260",
        "- Left Hammer : DESTROYED (0/700 HP) | TECTONIC PULVERIZATION CANCELLED",
        "- Right Shield: Spd 2 -> 1 AP | HP 900/900     | Posture 172/220"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: PASSAGE 02 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — STAGGER THRESHOLD 1 & UNYIELDING LINE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]            [HARIN] [DOHA]  [BOSS]   [SORA]  [YEON]  [SILENT]        [JISOO] ",
        "---",
        "- Node 03: Harin (Bastion of the Low: Unyielding Line Meets Bulwark)",
        "- Node 04: Doha (Pneumatic Counter-Lever Prying Shield Bracket)",
        "- Node 05: SECC-028 (STAGGER LEVEL 1 / DEFENSES COLLAPSED / STEAM SURGE)",
        "- Node 06: Sora (Lament Needle Drive Searing Glowing Furnace Core)",
        "- Node 07: Yeonhwa (Sonar Beacon Directing Squad Penetration)",
        "- Node 08: The Silent One (Severing Crescent Slashing Core Housing)",
        "---",
        "- Harin       : Spd 6 -> 3 AP [SURGE] | HP 4,140/4,200 | SP 48/50 | Posture 180/180",
        "- Boss Core   : Spd 0 -> 0 AP | HP 988/1,200   | Posture 94/260 [STAGGER LEVEL 1]",
        "- Right Shield: Spd 0 -> 0 AP | HP 658/900     | Posture 84/220 [CRACKED]",
        "- Total Boss  : HP 1,946/2,800 [THRESHOLD BREACHED / TAKES 1.5X DAMAGE]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: PASSAGE 02 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — MAXIMUM BURST & THRESHOLD SKIP]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]                    [HARIN] [BOSS]   [DOHA]  [SILENT][YEON]  [SORA]  [JISOO] ",
        "---",
        "- Node 04: Harin (Pneumatic Shield Bash Rattling Core Chassis)",
        "- Node 05: SECC-028 Bastion Sovereign (Immobilized on Both Knees)",
        "- Node 06: Doha (Calcified Pneumatic Ram: Core Breaker Strike)",
        "- Node 07: The Silent One (Relic Cleaver: Void Execution Flurry)",
        "- Node 08: Yeonhwa & Sora (Acoustic Dart & Lament Flood Barrage)",
        "- Node 10: Jisoo (Cryo Harpoon Anchoring Loose Ashlar Blocks)",
        "---",
        "- Silent One  : Spd 10 -> 5 AP [BURST CRIT] | HP 3,100/3,100 | SP 50/50",
        "- Boss Core   : Spd 0 -> 0 AP | HP 446/1,200   | Posture 42/260",
        "- Right Shield: Spd 0 -> 0 AP | HP 458/900     | Posture 36/220",
        "- Total Boss  : HP 904/2,800 [BURST DAMAGE 1,042! SECOND THRESHOLD SKIPPED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: PASSAGE 02 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — ANCESTRAL RECKONING & THE UNMAKING STRIKE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]                    [HARIN] [BOSS]   [DOHA]  [SILENT][YEON]  [SORA]  [JISOO] ",
        "---",
        "- Node 04: Harin (Ground Spikes Bracing Against Tectonic Quake)",
        "- Node 05: SECC-028 (Catastrophic Collapse / Petrified Hands Twitching)",
        "- Node 06: Doha (Architect's Final Decree: The Unmaking Strike)",
        "- Node 07: The Silent One (Severing Residual Kinetic Arcs)",
        "- Node 09: Sora (Cranial Silver Cowl Stabilizing Doha's Mind)",
        "---",
        "- Doha        : Spd 8 -> 4 AP [OVERDRIVE] | HP 3,600/3,600 | SP 50/50 [RESOLVE]",
        "- Boss Core   : Spd 2 -> 1 AP | HP 224/1,200   | Posture 18/260",
        "- Right Shield: DESTROYED (0/900 HP) | BULWARK SHATTERED INTO DUST",
        "- Total Boss  : HP 224/2,800 [DEFENSES DESTROYED / SLUMPED FORWARD]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: PASSAGE 02 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — THE DISMANTLING OF GUILT & MASON'S COMPASS]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]                            [DOHA]   [HARIN] [YEON]  [SORA]  [SILENT][GATE]  ",
        "                                 [REST]                           [MINJAE][JISOO] ",
        "---",
        "- Node 05: SECC-028 Bastion Sovereign (PACIFIED & DISSOLVED TO GRAVEL)",
        "- Node 06: Doha (Extracts Ancestral Keystroke Crystal with Bare Hands)",
        "- Node 07: Harin & Yeonhwa (Surveying Stable Gravel Ramp Through Sluice)",
        "- Node 08: Sora (Confirming Complete Spiritual Tranquility of Stone)",
        "- Node 09: Minjae & Jisoo (Securing 'The Mason's Compass of Year Zero')",
        "- Node 10: Great Bastion Breach Arch (Pathway to Strata 3 Furtugil OPEN)",
        "---",
        "- Vanguard Squad: Zero Fatalities | Composure 50/50 SP (Tranquil)",
        "- Encounter Status: 100% PACIFIED | Pathway to Furtugil OPEN"
    ])

    return f"""### The Vanguard Squad Combat Loadout

| Specialist | Position & Range Band | Primary Armament | Active Tactical Role | M.A.W.-W Class | Current SP |
|---|---|---|---|---|---|
| **Harin** | Band 1 (Melee Front) | *The Bastion of the Low* | Kinetic Redirection, Shockwave Shield, Taunt | Heavy (Spd -1, Poise +25) | 45/50 SP |
| **Doha** | Band 1 (Melee Front) | *Calcified Pneumatic Ram* | Bedrock Sapping, Armor Shatter, Part Puncture | Medium (Spd 0, Poise +20) | 40/40 SP |
| **The Silent One**| Band 1 (Melee Striker)| *Severed Relic Cleaver* | Void/Grudge Executioner, Part Amputation | Medium (Spd 0, Crit +30%) | 40/40 SP |
| **Sora** | Band 2 (Mid Support) | *Silver Slumber Cowl* | Lament Water Resonance, Harmonic SP Recovery | Light (Spd +1, SP Rec +15)| 50/50 SP |
| **Yeonhwa** | Band 3 (Ranged Command)| *The Horizon Theodolite* | Sonar Fault Tagging, Acoustic Coordination | Light (Spd +1, Evasion +15%)| 45/45 SP |
| **Minjae** | Band 4 (Forensic Scribe)| *Year Zero Archaeological Slate*| Structural Stress Telemetry, Archive Logs | Light (Spd +1, Scan +20%) | 45/45 SP |
| **Jisoo** | Band 5 (Logistics Rear)| *High-Pressure Cryo Harpoon*| Ballast Accounting, Munition Logistics | Light (Spd +1, Ballast 71%) | 45/45 SP |

---

### Turn-Based Combat Gauntlet: Dismantling the Wall

```text
{dossier_box}
```

---

```text
{hud_t01}
```

###### Turn 01 Action Resolution Log (Clashing Against the Living Mountain)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Harin activates `[Pneumatic Bulwark Stance]`: Grants herself and adjacent allies $+3$ Protection; intercepts the highest speed hostile clash targeting Band 1–2.
  * Doha prepares `[Bedrock Fracture Stance]`: Inflicts $+25\%$ bonus Posture Strain on structural stone parts.
  * Yeonhwa shouts: *"Sora, drench the joints! The mortar is calcified Han—if you flood the seams with pure Lament, the stone will soften!"*
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Doha (Speed 5 -> 3 AP, M.A.W.-W Medium delta $0$, Poise $+20$): Holds Node 03. Spends 2 AP on `[Pneumatic Ram: Counter-Strike]`. Holds 1 AP in Guard.
  * Harin (Speed 4 -> 2 AP, M.A.W.-W Heavy Armor delta $-1$, Poise $+25$): Holds Node 02. Spends 2 AP on `[Pneumatic Bulwark: Kinetic Deflection]`.
  * Sora (Speed 7 -> 4 AP, M.A.W.-W Light delta $+1$): Holds Node 04. Spends 2 AP on `[Lament Tide: Weeping Deluge]`. Holds 2 AP in Reserve.
  * Yeonhwa (Speed 7 -> 4 AP, M.A.W.-W Light delta $+1$): Holds Node 06. Spends 2 AP on `[Sonar Target Lock: Hammer Joint]`.
  * The Silent One (Speed 7 -> 4 AP, M.A.W.-W Medium delta $0$, Crit $+30\%$): Holds high arch at Node 10. Spends 2 AP on positioning.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 03 to 05)**: SECC-028 Slot 1 (Left Siege Hammer) executes `[Foundational Impact]` (Base 16 + 2 Coins = 24 Power, Heavy Weight).
    * Doha clashes with `[Pneumatic Ram: Counter-Strike]` (Base 18 + 2 Coins = 32 Power, Heavy Blunt).
    * **Clash Outcome**: Doha WINS THE CLASH (32 vs 24)!
    * The hydraulic ram collides violently with the massive three-ton stone hammer!
    * The kinetic shockwave shatters the hammer's wrist joint, dealing **168 Blunt damage** and $+48$ Posture Strain!
  * **Clash 2 (Node 02 to 05)**: SECC-028 Slot 2 (Retaining Bulwark) slams forward with `[Quarantine Slam]` (Base 16 + 1 Coin = 22 Power, Heavy Weight).
    * Harin intercepts with `[Pneumatic Bulwark: Kinetic Deflection]` (Base 18 + 2 Coins = 30 Power).
    * **Clash Outcome**: Harin WINS THE CLASH (30 vs 22)!
    * Absorbs the kinetic thrust cleanly (`[P3: Parry/Protection]`); deflects the stone bulwark outward! Harin takes 0 damage.
  * **Lament Vulnerability Exploitation**:
    * Sora unleashes `[Lament Tide: Weeping Deluge]` directly onto the Left Siege Hammer's calcified mortar joints:
      * Siphon of pure liquid Lament strikes calcified mortar seams (Fatal 2.0x proc!).
      * Deals **196 Cryo-Lament damage**! The mortar froths and dissolves into white brine, severely compromising the hammer's structural integrity.
- **Step 4: Turn End State**:
  * Left Siege Hammer HP: 700 -> **336/700** | Posture: **102/200 [MORTAR DISSOLVING]**.
  * Total Boss HP: 2,800 -> **2,436/2,800** | Posture: **198/260**.
  * Vanguard Composure: **100% (All SP > 45)**. Zero damage taken.

---

```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Amputating the Left Siege Hammer)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Doha and The Silent One both activate `Momentum Surge` (+2 Speed on Turn 02).
  * SECC-028 roars, lifting the cracked Siege Hammer to execute `[Tectonic Pulverization]` (3 Coins, Area of Effect Range 5).
  * Doha shouts: *"Not on my watch! Break the arm!"*
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Doha (Speed 7 -> 4 AP [Surge]): Steps from Node 03 to Node 04. Spends 3 AP on `[Pneumatic Overdrive: Bedrock Piston]`.
  * The Silent One (Speed 9 -> 5 AP [Surge]): Drops from Node 10 onto the basalt elbow at Node 05. Spends 3 AP on `[Twin Pale Flurry]`.
  * Harin (Speed 4 -> 2 AP): Steps to Node 03, executing `[Aegis Intercept]` (2 AP) to shield Sora and Yeonhwa.
  * Sora (Speed 7 -> 4 AP): Casts `[Lament Needle Drive]` (2 AP).
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 03 to 05)**: SECC-028 unleashes `[Tectonic Pulverization]` wind-up.
    * Harin's `[Aegis Intercept]` locks down the forward shockwave, containing the seismic tremor (`[P3: Parry/Protection]`). Harin takes only 14 mitigated chip damage (HP: 4,186/4,200).
  * **Piston Demolition Assault on Left Hammer**:
    * The Silent One strikes the softened stone elbow with `[Twin Pale Flurry]` (Base 20 + 2 Coins Heads = 32 Power, Void Slash):
      * Deals **180 Void damage** directly into the softened basalt tendons!
    * Doha follows through with `[Pneumatic Overdrive: Bedrock Piston]` (Base 22 + 2 Coins Heads = 36 Power, Heavy Blunt):
      * Massive kinetic explosion! Deals **340 Bludgeoning damage**!
    * **TARGETED PART DESTROYED**: The Left Basalt Siege Hammer shatters into twenty metric tons of tumbling rubble (**Hammer HP: 0/700**)!
    * **EFFECT**: Boss ultimate `[Tectonic Pulverization]` is permanently cancelled! Boss permanently loses 1 Speed Slot!
- **Step 4: Turn End State**:
  * Left Siege Hammer: **DESTROYED (0/700 HP)**.
  * Total Boss HP: 2,436 -> **2,158/2,800** | Posture: **152/260 [HAMMER SHATTERED]**.
  * Vanguard Composure: Harin 48 SP, Doha 44 SP, Silent One 46 SP, Sora 50 SP, Yeonhwa 45 SP.

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (Pushing the First Stagger Threshold & Unyielding Line)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Enraged by the amputation of its hammer, the titan sweeps its Right Retaining Bulwark across the floor in `[The Wall's Rejection]` (Heavy Weight, 2 Coins).
  * Harin gains `Momentum Surge` (+2 Speed -> Net Speed 6, 3 AP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Harin (Speed 6 -> 3 AP): Steps forward to Node 03, meeting the bulwark shield-to-shield with `[Bastion of the Low: Unyielding Line]` (2 AP).
  * Doha (Speed 5 -> 3 AP): Plants a hydraulic lever beneath the shield bracket at Node 04 (2 AP on `[Sapper Counter-Lever]`).
  * Yeonhwa (Speed 7 -> 4 AP): Tags the central glowing furnace core with `[Sonar Fault Beacon]` (2 AP).
  * Sora (Speed 7 -> 4 AP): Channels `[Lament Needle Drive]` (2 AP) directly into the exposed chest core.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 03 to 05)**: SECC-028 unleashes `[The Wall's Rejection]` (Base 18 + 2 Coins = 28 Power, Heavy Weight).
    * Harin clashes with `[Bastion of the Low: Unyielding Line]` (Base 21 + 2 Coins = 33 Power, Tower Shield).
    * **Clash Outcome**: Harin WINS THE CLASH (33 vs 28)!
    * Harin's two-meter tower shield slams into the basalt bulwark with an ear-splitting boom. Harin plants her hydraulic ground spikes, driving the five-meter titan backward six paces!
  * **Lament Weakness Penetration**:
    * Sora lands `[Lament Needle Drive]` squarely into the glowing chest furnace:
      * Striking Fatal 2.0x Lament weakness!
      * Deals **280 Cryo-Lament damage**! White steam billows violently from the entity's chest cavity!
- **Step 4: STAGGER THRESHOLD 1 TRIGGERED!**:
  * Total Boss HP drops past 70% to **1,946/2,800 HP**; Posture collapses past 60% strain line!
  * **STAGGER LEVEL 1 ACTIVE!** The titan falls onto both knees in the dust. All defenses collapse; takes $+50\%$ damage across all incoming attacks!
- **Step 5: Turn End State**:
  * Total Boss HP: 2,158 -> **1,946/2,800 [THRESHOLD BREACHED: Below 1,960 HP!]**.
  * Boss Posture: **94/260 [STAGGER LEVEL 1]**.
  * Vanguard Status: Unbroken.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Maximum Burst & Threshold Skip)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * SECC-028 remains completely immobilized on both knees; its glowing red furnace sputters thick white steam.
  * The entire Vanguard coordinates an all-out offensive barrage targeting the exposed furnace core.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Doha (Speed 5 -> 3 AP): Moves to Node 06. Spends 3 AP on `[Calcified Pneumatic Ram: Core Breaker]`.
  * The Silent One (Speed 10 -> 5 AP, Momentum Crit): Holds Node 07. Spends 3 AP on `[Relic Cleaver: Void Execution]`, 2 AP on `[Severing Arc]`.
  * Yeonhwa (Speed 7 -> 4 AP): Stands at Node 08. Spends 2 AP on `[Acoustic Resonance Dart]`.
  * Harin (Speed 4 -> 2 AP): Steps to Node 04. Spends 2 AP on `[Pneumatic Shield Bash]`.
  * Jisoo (Speed 7 -> 4 AP): Fires `[Cryo Harpoon Anchor]` from Node 10 (2 AP).
- **Step 3: Unopposed Stagger Punishment Rotation**:
  * Doha's `[Core Breaker]`: Smashes through the basalt ribcage for **340 Weight damage**!
  * The Silent One's `[Void Execution]`: Slices through the glowing embers for **412 Void damage**!
  * Yeonhwa's `[Acoustic Resonance Dart]`: Shatters acoustic conduits for **156 Void damage**!
  * Harin's `[Pneumatic Shield Bash]`: Rumbles through the chassis for **134 Blunt damage**!
  * **TOTAL BURST DAMAGE: 1,042 DAMAGE!**
- **Step 4: SECOND STAGGER THRESHOLD (1,120 HP) COMPLETELY SKIPPED!**:
  * Boss HP plunges from 1,946 all the way down to **904/2,800 HP**!
  * The furnace core cracks open, spilling molten magma tears across the basalt floor.
- **Step 5: Turn End State**:
  * Total Boss HP: 1,946 -> **904/2,800** (Core HP: **446/1,200** | Shield HP: **458/900**).
  * Posture: **42/260**.

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Phase 2 Escalation: Ancestral Reckoning & The Unmaking Strike)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * The titan recovers from stagger, its stone chassis fractured from top to bottom. The thousands of petrified hands covering its shoulders begin to twitch and reach toward Doha!
  * A voice echoes from the hollow archway of its face—a voice of grinding basalt and distant thunder:
    > *"Child of Doha... Why do you unmake the wall? If the gate falls... the weeping will drown the world!"*
  * High-density Grudge and Weight surge from the fractured core! Doha SP: 44 -> 14 (Emotional Fracture warning!).
  * Doha looks at the burning core, tears welling in his eyes, but his jaw sets with absolute resolve:
    > *"My grandfather locked you in the dark to save his own skin! The weeping will not drown the world—because this time, we are descending to the source to finish what you started! Rest your hands, grandfather! The wall is coming down!"*
  * Doha activates Relic Overdrive: `[Architect's Final Decree: The Unmaking Strike]` (Cost: 3 AP, 25 SP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Doha (Speed 8 -> 4 AP [Overdrive]): Advances to Node 06, charging his four-inch tungsten drill spike.
  * Harin (Speed 4 -> 2 AP): Holds Node 04, locking ground spikes to brace against tectonic tremors.
  * Sora (Speed 7 -> 4 AP): Casts `[Cranial Silver Cowl]` (2 AP), stabilizing Doha's mind back to 50 SP.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 06 to 05)**: SECC-028 initiates `[Catastrophic Collapse]` (Last Stand Attack: Base 20 + 3 Coins = 29 Power, Heavy Weight).
    * Doha clashes with `[Architect's Final Decree: The Unmaking Strike]` (Base 25 + 3 Coins Heads = 43 Power, Heavy Blunt/Weight).
    * **Clash Outcome**: DOHA OVERWHELMING RELIC CLASH WIN (43 vs 29)!
    * Doha's pneumatic ram drives directly into the center of the House Doha crest on the Right Bulwark!
    * The four-inch tungsten spike detonates inside the furnace core, delivering **680 Bludgeoning-Weight damage**!
    * **TARGETED PART DESTROYED**: The Right Retaining Bulwark shatters into fine powder (**Shield HP: 0/900**)!
- **Step 4: Turn End State**:
  * Right Retaining Bulwark: **DESTROYED (0/900 HP)**.
  * SECC-028 is completely disarmed; all defenses shattered.
  * Total Boss HP: 904 -> **224/2,800** | Posture: **18/260 [CRITICAL COLLAPSE]**.
  * Vanguard Composure: 50/50 SP across all members.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (The Dismantling of Guilt & Mason's Compass)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * The titan slumps forward, unable to raise its arms. The glowing crimson fire in its chest fades to a gentle, warm amber ember.
  * Hostile intent drops to zero. Posture reaches **0/260 [TERMINAL DISMANTLING]**.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Doha (Speed 5 -> 3 AP): Steps onto the titan's stone knee at Node 05, climbing up to the hollow archway of its chest.
  * Harin, The Silent One, and Sora stand at Node 06 in respectful vigil.
  * Minjae and Jisoo advance to Node 09 with recovery cradles.
- **Step 3: Non-Lethal Dismantling & Peaceful Resolution**:
  * Doha does not strike it again. With bare, gloved hands, he reaches inside the cooling furnace and grasps the central keystroke crystal.
  * *"You did your duty,"* Doha whispers softly. *"For four thousand years, you held the line. Let me carry the weight now."*
  * With a gentle pull, Doha extracts the central crystal.
  * The titan sighs—a sound like a soft evening wind blowing across stone. The colossal basalt chassis does not collapse in violence; it smoothly dissolves into a ramp of dark, stable gravel leading directly through the Sluice Arch into the deep tunnels beyond.
- **Step 4: Operational Artifact Extraction & Strata Access**:
  * **Artifact Acquired**: `[Relic: The Mason's Compass of Year Zero]` (Grade-ω Structural Relic).
  * **Tectonic Outcome**: The Great Bastion Wall is breached permanently.
  * **Descent Access**: Pathway to Strata 3 (Furtugil / Severed Arteries, -450m to -900m) is officially **OPEN**.
  * **Casualties**: Flawless Victory. Zero Fatalities. Harin (HP 4,186/4,200), Doha (HP 3,600/3,600). Squad Composure 50/50 SP."""

def update_passage_2():
    path = "SOMNARAK-WORLD/Katabagil/Passage_2_Petrobyeok.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    start_str = "### The Vanguard Squad Combat Loadout"
    end_str = "## Chapter VIII: Epilogue — Beyond the Wall"

    start_idx = content.find(start_str)
    end_idx = content.find(end_str)

    if start_idx == -1 or end_idx == -1:
        print(f"Error locating boundaries! start_idx={start_idx}, end_idx={end_idx}")
        return

    new_engagement = get_p2_engagement() + "\n\n---\n\n"
    new_content = content[:start_idx] + new_engagement + content[end_idx:]

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Updated Passage 2 successfully!")

if __name__ == "__main__":
    update_passage_2()
