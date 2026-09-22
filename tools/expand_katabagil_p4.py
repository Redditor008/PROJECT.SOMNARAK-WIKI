#!/usr/bin/env python3
"""
tools/expand_katabagil_p4.py
Expands Passage 4 (Radikkum - Ethereal Echo Gardens) in SOMNARAK-WORLD/Katabagil/Passage_4_Radikkum.md
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

def get_p4_engagement():
    dossier_box = make_box("APEX BOSS DOSSIER: SECC-056 'ARBOR OF PRIMORDIAL REGRET'", [
        "APEX TARGET        : SECC-056 'The Arbor of Primordial Regret'",
        "CLASSIFICATION     : Major-γ (Grade-γ Potency) | Ancient Memory-Arbor Apex",
        "ENCOUNTER DOMAIN   : Strata 4 Sunken Arbor Cathedral (-1,500m Depth)",
        "---",
        "BOSS COMBAT PROFILE (SECC-056):",
        "- Total Health (HP): 3,600 HP | Posture Pool: 300/300",
        "- Stagger 1 Proc   : 60% Posture Strain (180 Posture) / Tendril Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Terminal Slumber)",
        "- Resistances      : Grudge 2.0x (Fatal), Void 1.5x, Weight 1.0x, Lament 0.5x",
        "---",
        "TARGETABLE COMPONENT PARTS:",
        "1. Canopy Tendrils : 950 HP | Posture 240/240 (Sweeping strikes & amnesia)",
        "2. Heartwood Bark  : 1,200 HP | Posture 260/260 (Petrified high-defense shell)",
        "3. Salt Idol Core  : 1,450 HP | Posture 300/300 (Central acoustic singer)"
    ])

    hud_t01 = make_box("TACTICAL STAGE HUD: PASSAGE 04 — BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 — STRATA 4 ARBOR CATHEDRAL (-1,500M)]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]   [HARIN]  [DOHA]  [SORA]  [BOSS]   [YEON]  [SILENT][MINJAE]        [JISOO] ",
        "                                 [ROOTS]                                  ",
        "---",
        "- Node 01: Monorail Terminus Staging / Armored Rig 'The Iron Mole'",
        "- Node 02: Harin (Vanguard Band 1 / Bastion of the Low Tower Shield)",
        "- Node 03: Doha (Point-Blank Band 1 / Calcified Pneumatic Fracture Ram)",
        "- Node 04: Sora (Lead Resonator Band 2 / Silver Cowl Mnemonic Repose)",
        "- Node 05: SECC-056 Memory Arbor (Canopy Root Tendrils & Heartwood Bark)",
        "- Node 06: Yeonhwa (Mid-Field Band 3 / Sonar Spore Lock Theodolite)",
        "- Node 07: The Silent One (High Coral Branches / Severed Relic Cleaver)",
        "- Node 08: Minjae (Rear Band 4 / Memory Archive Slate)",
        "- Node 10: Jisoo (Rear Band 5 / Cryo Harpoon Logistics Berth)",
        "---",
        "- Harin       : Spd 4 -> 2 AP | HP 4,200/4,200 | SP 46/50 | Posture 180/180",
        "- Silent One  : Spd 7 -> 4 AP | HP 3,100/3,100 | SP 42/40 | Posture 120/120",
        "- Doha        : Spd 5 -> 3 AP | HP 3,600/3,600 | SP 40/40 | Posture 150/150",
        "- Sora        : Spd 7 -> 4 AP | HP 2,600/2,600 | SP 50/50 | Posture 100/100",
        "- Yeonhwa     : Spd 7 -> 4 AP | HP 2,700/2,700 | SP 45/45 | Posture 100/100",
        "- Boss Core   : Spd 4 -> 2 AP | HP 1,450/1,450 | Posture 300/300 [SINGING]",
        "- Canopy Roots: Spd 5 -> 3 AP | HP 950/950     | Posture 240/240 [SPORES]",
        "- Heartwood   : Spd 3 -> 1 AP | HP 1,200/1,200 | Posture 260/260 [PETRIFIED]"
    ])

    hud_t02 = make_box("TACTICAL STAGE HUD: PASSAGE 04 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — CANOPY TENDRILS SEVERED & VOID CUT]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]            [HARIN] [DOHA]  [BOSS]   [SORA]  [YEON]  [MINJAE][JISOO] [SILENT]",
        "                                 [SEVER]                                  ",
        "---",
        "- Node 03: Harin (Vow of the Low Bulwark Deflecting Whiplash Root)",
        "- Node 04: Doha (Pneumatic Core Sapper Driving Tungsten Drill)",
        "- Node 05: SECC-056 Memory Arbor (Canopy Tendrils Severed 0/950 HP)",
        "- Node 06: Sora (Silver Cowl Dissipating Residual Mnemonic Hallucinations)",
        "- Node 07: Yeonhwa (Sonar Fault Lock on Heartwood Growth Rings)",
        "- Node 10: The Silent One (Burden Cleaver Void Amputation Cleaving Limb)",
        "---",
        "- Silent One  : Spd 9 -> 5 AP [SURGE] | HP 3,100/3,100 | SP 46/50 | Posture 120/120",
        "- Doha        : Spd 7 -> 4 AP [SURGE] | HP 3,600/3,600 | SP 44/40 | Posture 150/150",
        "- Boss Core   : Spd 4 -> 2 AP | HP 1,450/1,450 | Posture 228/300",
        "- Canopy Roots: DESTROYED (0/950 HP) | WHIPLASH ROOT ATTACK PERMANENTLY LOST",
        "- Heartwood   : Spd 3 -> 1 AP | HP 880/1,200   | Posture 194/260"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: PASSAGE 04 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — STAGGER THRESHOLD 1 & HEARTWOOD SPLIT]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]            [HARIN] [DOHA]  [BOSS]   [SORA]  [YEON]  [SILENT]        [JISOO] ",
        "---",
        "- Node 03: Harin (Bracing Front Ranks Against Bark Splinters)",
        "- Node 04: Doha (Tungsten Fracture Wedge Splitting Growth Rings)",
        "- Node 05: SECC-056 (STAGGER LEVEL 1 / DEFENSES COLLAPSED / IMMOBILIZED)",
        "- Node 06: Sora (Tuning of the Deep Inflicting +4 Mnemonic Vulnerable)",
        "- Node 07: Yeonhwa (Directing Optical Theodolite Beam on Core)",
        "- Node 08: The Silent One (Preparing Core Severance Stance)",
        "---",
        "- Harin       : Spd 6 -> 3 AP [SURGE] | HP 4,200/4,200 | SP 48/50 | Posture 180/180",
        "- Boss Core   : Spd 0 -> 0 AP | HP 1,350/1,450 | Posture 110/300 [STAGGER LEVEL 1]",
        "- Heartwood   : Spd 0 -> 0 AP | HP 470/1,200   | Posture 86/260 [SPLIT OPEN]",
        "- Total Boss  : HP 2,340/3,600 [THRESHOLD BREACHED / TAKES 1.5X DAMAGE]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: PASSAGE 04 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — MAXIMUM BURST & PHASE 2 THRESHOLD SKIP]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]                    [HARIN] [BOSS]   [DOHA]  [SILENT][YEON]  [SORA]  [JISOO] ",
        "---",
        "- Node 04: Harin (Bulwark Kinetic Pummel Crushing Root Knees)",
        "- Node 05: SECC-056 Memory Arbor (Salt Idol Exposed & Trembling)",
        "- Node 06: Doha (Sapper Magnesium Detonation Searing Resin)",
        "- Node 07: The Silent One (The Burden Cleave Driving into Heart)",
        "- Node 08: Yeonhwa & Sora (Theodolite Laser & Mnemonic Resonance)",
        "- Node 10: Jisoo (Cryo Harpoon Securing Collapsing Canopy Boughs)",
        "---",
        "- Silent One  : Spd 10 -> 5 AP [BURST CRIT] | HP 3,100/3,100 | SP 50/50",
        "- Boss Core   : Spd 0 -> 0 AP | HP 420/1,450   | Posture 46/300",
        "- Heartwood   : DESTROYED (0/1,200 HP)",
        "- Total Boss  : HP 1,030/3,600 [BURST DAMAGE 1,310! SECOND THRESHOLD SKIPPED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: PASSAGE 04 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — THE MEMORY FLOOD & REQUIEM OF SLUMBER]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]                    [HARIN] [BOSS]   [DOHA]  [SILENT][YEON]  [SORA]  [JISOO] ",
        "---",
        "- Node 04: Harin (Locking Ground Anchors Against Psychic Deluge)",
        "- Node 05: SECC-056 (Tide of Unremembered Tears / Memory Phantoms)",
        "- Node 06: Doha (Planting Stabilizer Brackets Around Root Trunk)",
        "- Node 07: The Silent One (Charging Burden Cleaver Void Overdrive)",
        "- Node 09: Sora (Relic Overdrive: REQUIEM OF THE LIVING SLUMBER)",
        "---",
        "- Sora        : Spd 8 -> 4 AP [OVERDRIVE] | HP 2,600/2,600 | SP 50/50 [BELL CHIME]",
        "- Boss Core   : Spd 4 -> 2 AP | HP 420/1,450   | Posture 24/300 [TEARS PARTED]",
        "- Total Boss  : HP 420/3,600 [PSYCHIC BACKLASH COLLAPSED / WEAKENED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: PASSAGE 04 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — FINAL REST & ROOT-KEY OF FIRST SLUMBER]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]                            [SORA]   [SILENT][HARIN] [DOHA]  [YEON]  [SLUICE]",
        "                                 [REST]                           [MINJAE][JISOO] ",
        "---",
        "- Node 05: SECC-056 Memory Arbor (PACIFIED & PETALS DISSOLVING TO LIGHT)",
        "- Node 06: The Silent One (Parts Primordial Salt Idol with Relic Cleaver)",
        "- Node 07: Sora (Extracts 'The Root-Key of the First Slumber')",
        "- Node 08: Harin & Doha (Securing Unsealed Water Sluice Floodgates)",
        "- Node 10: Spiral Bedrock Staircase (Pathway to Strata 5 Limesteum OPEN)",
        "---",
        "- Vanguard Squad: Zero Fatalities | Composure 50/50 SP (Tranquil)",
        "- Encounter Status: 100% PACIFIED | Pathway to Limesteum OPEN"
    ])

    return f"""### The Vanguard Squad Combat Loadout

| Specialist | Position & Range Band | Primary Armament | Active Tactical Role | M.A.W.-W Class | Current SP |
|---|---|---|---|---|---|
| **Sora** | Band 2 (Lead Resonator)| *Silver Slumber Cowl* | Mnemonic Cleansing, Team SP Shielding | Light (Spd +1, SP Rec +15)| 50/50 SP |
| **Harin** | Band 1 (Melee Front) | *The Bastion of the Low* | Kinetic Tanking, Aggro Redirection, Shield | Heavy (Spd -1, Poise +25) | 46/50 SP |
| **Doha** | Band 1 (Melee Front) | *Calcified Pneumatic Ram* | Bedrock Fracture, Root Sapping, Magnesium | Medium (Spd 0, Poise +20) | 40/40 SP |
| **The Silent One**| Band 1 (Melee Striker)| *Severed Relic Cleaver* | Void Executioner, Tendril Amputation | Medium (Spd 0, Crit +30%) | 42/40 SP |
| **Yeonhwa** | Band 3 (Ranged Command)| *The Horizon Theodolite* | Spore Sensor Tagging, Weakpoint Laser | Light (Spd +1, Evasion +15%)| 45/45 SP |
| **Minjae** | Band 4 (Forensic Scribe)| *Year Zero Archaeological Slate*| Memory Archive Telemetry, Name Recovery | Light (Spd +1, Scan +20%) | 45/45 SP |
| **Jisoo** | Band 5 (Logistics Rear)| *High-Pressure Cryo Harpoon*| Ballast Accounting, Winch Rigging | Light (Spd +1, Ballast 58%) | 45/45 SP |

---

### Turn-Based Combat Gauntlet: Pacifying the Memory Arbor

```text
{dossier_box}
```

---

```text
{hud_t01}
```

###### Turn 01 Action Resolution Log (Canopy Roots & Spore Entanglement)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Sora initializes `[Harmonic Bell Resonator]`: Calibrates Silver Cowl acoustic chime to 432 Hz, creating an atmospheric counter-wave against airborne spore miasmas.
  * Harin activates `[Bulwark Intercept]`: Positioned at Node 02, intercepts projectile thorn showers targeting rear specialists.
  * Yeonhwa casts `[Sonar Spore Lock]`: Identifies fungal spore nodules along the canopy root joints.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Sora (Speed 7 -> 4 AP, M.A.W.-W Light delta $+1$): Holds Node 04. Spends 2 AP on `[Harmonic Bell Resonator: Acoustic Repose]`. Holds 2 AP in Reserve.
  * Harin (Speed 4 -> 2 AP, M.A.W.-W Heavy Armor delta $-1$, Poise $+25$): Holds Node 02. Spends 2 AP on `[Bulwark Intercept: Shield Wall]`.
  * The Silent One (Speed 7 -> 4 AP, M.A.W.-W Medium delta $0$, Crit $+30\%$): Perches on coral branches at Node 07. Spends 2 AP on positioning.
  * Doha (Speed 5 -> 3 AP, M.A.W.-W Medium delta $0$, Poise $+20$): Holds Node 03. Spends 2 AP on `[Tungsten Fracture Wedge]`. Holds 1 AP in Guard.
  * Yeonhwa (Speed 7 -> 4 AP, M.A.W.-W Light delta $+1$): Holds Node 06. Spends 2 AP on `[Sonar Spore Lock]`, 2 AP on `[Optical Theodolite Laser]`.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 04 to 05)**: SECC-056 unleashes `[Grave-Spore Cloud]` (Base 16 + 2 Coins = 24 Power, Area Amnesia/Lament).
    * Sora counters with `[Harmonic Bell Resonator]` (Base 19 + 2 Coins = 31 Power, Acoustic Repose).
    * **Clash Outcome**: Sora WINS THE CLASH OVERWHELMINGLY (31 vs 24)!
    * The radiant 432 Hz acoustic pulse strikes the expanding spore cloud, dispersing the toxic amnesia mist back into the root branches!
    * Canopy Tendrils take **210 Lament damage** from the reflected acoustic shockwave, inflicting $+46$ Posture Strain!
  * **Clash 2 (Node 02 to 05)**: Arbor thrashes with `[Thorn Shower Volley]` (Power 22, Pierce).
    * Harin's `[Bulwark Intercept]` absorbs the entire salvo (`[P3: Parry/Protection]`). The two-meter tower shield deflects every petrified quill; zero team damage taken.
- **Step 4: Turn End State**:
  * Canopy Root Tendrils HP: 950 -> **740/950** | Posture: **194/240**.
  * Total Boss HP: 3,600 -> **3,390/3,600** | Posture: **254/300**.
  * Vanguard Composure: **100% (All SP > 42)**. Zero damage taken.

---

```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Part Destruction: Canopy Tendrils Severed)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * The Silent One and Doha activate `Momentum Surge` (+2 Speed on Turn 02).
  * SECC-056 channels `[Whiplash Root Sweep]` targeting the front vanguard.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Harin (Speed 4 -> 2 AP): Holds Node 03, executing `[Vow of the Low Bulwark: Plant]` (2 AP).
  * The Silent One (Speed 9 -> 5 AP [Surge]): Drops from high coral boughs at Node 07 onto the main root limb at Node 05. Spends 3 AP on `[Burden Cleaver: Void Amputation]`.
  * Doha (Speed 7 -> 4 AP [Surge]): Steps from Node 03 to Node 04. Spends 3 AP on `[Pneumatic Core Sapper]`.
  * Sora (Speed 7 -> 4 AP): Holds Node 06, dissipating residual hallucinations with `[Mnemonic Repose]` (2 AP).
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 03 to 05)**: SECC-056 sweeps with `[Whiplash Root Sweep]` (Base 17 + 2 Coins = 27 Power, Heavy Weight).
    * Harin clashes with `[Vow of the Low Bulwark: Plant]` (Base 20 + 2 Coins = 32 Power, Tower Shield).
    * **Clash Outcome**: Harin WINS THE CLASH (32 vs 27)!
    * Harin plants her shield firmly; the crushing three-ton root bounces harmlessly off the reinforced face! Harin takes 0 damage.
  * **Void Amputation on Canopy Tendrils**:
    * The Silent One executes `[Burden Cleaver: Void Amputation]` (Base 22 + 3 Coins Heads = 39 Power, Void Slash):
      * Slices cleanly through the primary tendon of the canopy root cluster!
      * Deals **420 Critical Void damage** (Fatal 2.0x proc!)!
      * **TARGETED PART DESTROYED**: The Canopy Root Tendrils are completely severed, dropping like massive timber onto the floor (**Tendril HP: 0/950**)!
      * **EFFECT**: Boss whiplash root sweep permanently disabled; boss permanently loses 1 Speed Slot!
    * Doha's `[Pneumatic Core Sapper]` drives a tungsten drill into the lower trunk, dealing **220 Blunt damage**!
- **Step 4: Turn End State**:
  * Canopy Root Tendrils: **DESTROYED (0/950 HP)**.
  * Heartwood Bark: 1,200 -> **880/1,200** | Posture: **194/260**.
  * Total Boss HP: 3,390 -> **2,750/3,600** | Posture: **182/300 [ROOTS SEVERED]**.
  * Vanguard Composure: Stable (> 44 SP across all members).

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (First Stagger Proc & Heartwood Split)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * SECC-056 raises `[Petrified Bark Bastion]`: Generates a massive temporary armor shield around its trunk.
  * Doha gains `Momentum Surge` (+2 Speed -> Net Speed 7, 4 AP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Doha (Speed 7 -> 4 AP): Steps to Node 04. Spends 3 AP on `[Tungsten Fracture Wedge: Growth Split]`.
  * Sora (Speed 7 -> 4 AP): Stands at Node 06. Spends 2 AP on `[Tuning of the Deep]`, inflicting $+4$ Mnemonic Fragility.
  * Harin (Speed 6 -> 3 AP): Steps to Node 03. Spends 2 AP on `[Aegis Wall]`.
  * Yeonhwa (Speed 7 -> 4 AP): Stands at Node 07. Spends 2 AP on `[Theodolite Weakpoint Laser]`.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 04 to 05)**: SECC-056 braces with `[Petrified Bark Bastion]` (Def Power 24).
    * Doha strikes with `[Tungsten Fracture Wedge: Growth Split]` (Atk Power 34, Heavy Blunt).
    * **Clash Outcome**: Doha WINS THE CLASH (34 vs 24)!
    * Doha drives the wedge into the primary growth ring; the pneumatic ram detonates with thunderous force!
    * The petrified heartwood splits open wide! Bark armor completely destroyed, dealing **410 Blunt damage** and $+72$ Posture Strain!
- **Step 4: STAGGER THRESHOLD 1 TRIGGERED!**:
  * Total Boss HP crosses 70% threshold (2,520 HP), falling to **2,340/3,600 HP**; Posture crosses 60% strain line!
  * **STAGGER LEVEL 1 ACTIVE!** The Arbor's branches collapse downward; all defenses drop to zero; takes $+50\%$ damage across all incoming attacks!
- **Step 5: Turn End State**:
  * Total Boss HP: 2,750 -> **2,340/3,600 [THRESHOLD BREACHED: Below 2,520 HP!]**.
  * Heartwood Bark: 880 -> **470/1,200** | Posture: **86/260 [SPLIT OPEN]**.
  * Boss Posture: **110/300 [STAGGER LEVEL 1]**.
  * Vanguard Status: Unbroken.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Maximum Burst & Phase 2 Threshold Skip)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * SECC-056 remains completely stunned; the Crying Salt Idol inside the hollow trunk is fully exposed and weeping luminous brine.
  * All Specialists coordinate maximum burst fire targeting the central salt idol.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * The Silent One (Speed 10 -> 5 AP, Momentum Crit): Stands at Node 07. Spends 3 AP on `[The Burden Cleave: Core Strike]`.
  * Harin (Speed 4 -> 2 AP): Steps to Node 04. Spends 2 AP on `[Bulwark Kinetic Pummel]`.
  * Doha (Speed 5 -> 3 AP): Moves to Node 06. Spends 3 AP on `[Sapper Magnesium Detonation]`.
  * Yeonhwa (Speed 7 -> 4 AP): Stands at Node 08. Spends 2 AP on `[Theodolite Laser]`.
  * Jisoo (Speed 7 -> 4 AP): Fires `[Cryo Harpoon Anchor]` from Node 10 (2 AP).
- **Step 3: Unopposed Stagger Punishment Rotation**:
  * The Silent One's `[Core Strike]`: Slices through the idol for **540 Void damage** (Weakness 1.5x proc!)!
  * Harin's `[Bulwark Kinetic Pummel]`: Smashes the base for **240 Weight damage**!
  * Doha's `[Sapper Magnesium Detonation]`: Sockets incendiary flares for **310 Explosive Grudge damage** (Fatal 2.0x proc!)!
  * Yeonhwa's `[Theodolite Laser]`: Rips through resonance conduits for **220 Void damage**!
  * **TOTAL BURST DAMAGE: 1,310 DAMAGE!**
- **Step 4: SECOND STAGGER THRESHOLD (1,440 HP) COMPLETELY SKIPPED!**:
  * Boss HP plunges from 2,340 down to **1,030/3,600 HP**! Heartwood Bark completely destroyed (0/1,200 HP)!
  * **Phase 2 Emergency Activation Triggered!**
- **Step 5: Turn End State**:
  * Total Boss HP: 2,340 -> **1,030/3,600** (Core HP: **420/1,450** | Bark: **DESTROYED**).
  * Posture: **46/300**.

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Phase 2 Escalation: The Memory Flood & Requiem of Living Slumber)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Arbor awakens in agonizing grief; a four-thousand-year dreamscape floods the entire chasm!
  * Boss Special Skill: `[Tide of Unremembered Tears]` (Acoustic Cataclysm, 3 Coins).
  * Speed Dice expands to 4 slots! Memory phantoms of forgotten orphans surround the squad.
  * Sora activates Relic Overdrive: `[REQUIEM OF THE LIVING SLUMBER]` (Cost: 3 AP, 30 SP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Sora (Speed 8 -> 4 AP [Overdrive]): Floats into the heartwood hollow at Node 05, unfolding her Silver Cowl.
  * Harin (Speed 4 -> 2 AP): Locks ground anchors at Node 04 to brace against the psychic deluge.
  * Doha (Speed 5 -> 3 AP): Plants stabilizer brackets around the root base at Node 06.
  * The Silent One (Speed 7 -> 4 AP): Prepares `[Burden Cleaver: Void Overdrive Execution]` at Node 07.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 05 to 05)**: SECC-056 unleashes `[Tide of Unremembered Tears]` (Base 20 + 3 Coins = 32 Power, Area Pale/Acoustic).
    * Sora clashes with `[REQUIEM OF THE LIVING SLUMBER]` (Base 26 + 3 Coins Heads = 45 Power, Supreme Mnemonic Ward).
    * **Clash Outcome**: SORA OVERWHELMING RELIC CLASH WIN (45 vs 32)!
    * A radiant 528 Hz bell chime envelops the team in a shimmering protective silver dome (`[P3: Parry/Protection]`).
    * The tidal wave of weeping spirits parts cleanly around the harmonic wave! Zero squad damage taken!
    * Sora speaks softly to the weeping idol: *"Your sorrow is recorded. You may sleep."*
    * The Arbor's psychic backlash collapses into stillness!
- **Step 4: Turn End State**:
  * Total Boss HP: **1,030 -> 420/3,600** | Posture: **24/300 [CRITICAL COLLAPSE]**.
  * Vanguard Composure: 50/50 SP across all members.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Final Rest & Root-Key of the First Slumber)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * The Arbor's sap turns to clear water; weeping branches droop peacefully. Posture reaches **0/300 [TERMINAL SLUMBER]**.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Harin and Doha secure the outer root limbs with steel anchor cables at Nodes 06–07.
  * The Silent One steps forward onto the exposed heartwood platform at Node 06.
  * Sora steps directly before the salt idol cradle at Node 05.
  * Minjae and Jisoo advance to Node 08 to log archival blueprints and retrieve the relic.
- **Step 3: Overdrive Execution & Peaceful Pacification**:
  * The Silent One raises the Relic: `[The Burden Cleaver: Void Overdrive Execution]` (Power 45).
  * The cleaver cleanly parts the primordial crystalline salt idol core.
  * Deals **1,030 Pure Void Resonance damage**! SECC-056 HP drops to 0!
  * The blinding amber glare softens into a warm twilight; fragrant white and gold petals shower the squad, dissolving into pure light.
- **Step 4: Operational Artifact Extraction & Strata Access**:
  * **Artifact Acquired**: `[Relic: The Root-Key of the First Slumber]` (Petrified heartwood key wrapped in silver flowering vines).
  * **Sora's Solace**: Sora lifts the relic from the cradle: *"The children are sleeping now. They will not have to dream for anyone else ever again."*
  * **Descent Access**: The unsealed water sluice floodgates swing open, revealing the massive spiral staircase carved directly into bedrock.
  * **Descent Destination**: Descending into Strata 5 (Limesteum / The Calcinated Fracture, -1,500m to -2,100m).
  * **Casualties**: Flawless Victory. Zero Fatalities. Harin (HP 4,200/4,200), Doha (HP 3,600/3,600). Squad Composure 50/50 SP."""

def update_passage_4():
    path = "SOMNARAK-WORLD/Katabagil/Passage_4_Radikkum.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    start_str = "### The Vanguard Squad Combat Loadout"
    end_str = "## Chapter VIII: Epilogue & Acquisition"

    start_idx = content.find(start_str)
    end_idx = content.find(end_str)

    if start_idx == -1 or end_idx == -1:
        print(f"Error locating boundaries! start_idx={start_idx}, end_idx={end_idx}")
        return

    new_engagement = get_p4_engagement() + "\n\n---\n\n"
    new_content = content[:start_idx] + new_engagement + content[end_idx:]

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Updated Passage 4 successfully!")

if __name__ == "__main__":
    update_passage_4()
