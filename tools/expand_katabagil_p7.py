#!/usr/bin/env python3
"""
tools/expand_katabagil_p7.py
Expands Passage 7 (Fontisaem - The Primordial Nadir) in SOMNARAK-WORLD/Katabagil/Passage_7_Fontisaem.md
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

def get_p7_engagement():
    dossier_box = make_box("APEX ENCOUNTER DOSSIER: SECC-UR-VIIω-001", [
        "APEX TARGET        : SECC-UR-VIIω-001 'The First Mourner'",
        "CLASSIFICATION     : Sovereign-ω (Grade-ω Potency) | Primordial Origin",
        "ENCOUNTER DOMAIN   : Strata 7 Primordial Wellspring (-2,800m to Core)",
        "---",
        "BOSS COMBAT PROFILE (SECC-UR-VIIω-001):",
        "- Total Health (HP): 6,000 HP | Posture Pool: 360/360",
        "- Stagger 1 Proc   : 60% Posture Strain (216 Posture) / Halo Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Terminal Solace)",
        "- Resistances      : Void 2.0x (Fatal), Grudge 1.0x, Lament/Weight 0.5x",
        "---",
        "TARGETABLE COMPONENT PARTS:",
        "1. Aura of Grief   : 1,200 HP | Posture 300/300 (Surging tidal barrier)",
        "2. Tear Halo       : 1,500 HP | Posture 320/320 (Crystalline tear halo)",
        "3. Wellspring Heart: 3,300 HP | Posture 360/360 (Central mourning soul)"
    ])

    hud_t01 = make_box("TACTICAL STAGE HUD: PASSAGE 07 — BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 — STRATA 7 PRIMORDIAL WELLSPRING (-2,800M)]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]   [HARIN]  [DOHA]  [SORA]  [MOURN]  [YEON]  [MINJAE][JISOO]         [SILENT]",
        "                                 [AURA]                                   ",
        "---",
        "- Node 01: Cyclopean Stair Landing / Armored Rig 'The Iron Mole'",
        "- Node 02: Harin (Vanguard Band 1 / Bastion of the Low Tower Shield)",
        "- Node 03: Doha (Point-Blank Band 1 / Calcified Pneumatic Anchor Ram)",
        "- Node 04: Sora (Lead Resonator Band 2 / Silver Cowl 528 Hz Harmonics)",
        "- Node 05: SECC-UR-VIIω-001 First Mourner (Aura of Grief & Tear Halo)",
        "- Node 06: Yeonhwa (Mid-Field Band 3 / Sonar Acoustic Theodolite)",
        "- Node 07: Minjae (Archaeological Record Band 4 / Year Zero Tablet)",
        "- Node 08: Jisoo (Forensic Record Band 4 / Hydraulic Ballast Ledger)",
        "- Node 10: The Silent One (Center of Wellspring / The Burden Cleaver)",
        "---",
        "- Harin       : Spd 4 -> 2 AP | HP 4,200/4,200 | SP 48/50 | Posture 180/180",
        "- Silent One  : Spd 7 -> 4 AP | HP 3,100/3,100 | SP 44/40 | Posture 120/120",
        "- Doha        : Spd 5 -> 3 AP | HP 3,600/3,600 | SP 40/40 | Posture 150/150",
        "- Sora        : Spd 7 -> 4 AP | HP 2,600/2,600 | SP 50/50 | Posture 100/100",
        "- Yeonhwa     : Spd 7 -> 4 AP | HP 2,700/2,700 | SP 45/45 | Posture 100/100",
        "- Minjae      : Spd 7 -> 4 AP | HP 2,800/2,800 | SP 50/50 | Posture 110/110",
        "- Jisoo       : Spd 7 -> 4 AP | HP 2,750/2,750 | SP 50/50 | Posture 110/110",
        "- Boss Heart  : Spd 4 -> 2 AP | HP 3,300/3,300 | Posture 360/360 [WEEPING]",
        "- Grief Aura  : Spd 6 -> 3 AP | HP 1,200/1,200 | Posture 300/300 [TIDAL]",
        "- Tear Halo   : Spd 4 -> 2 AP | HP 1,500/1,500 | Posture 320/320 [SAPPHIRE]"
    ])

    hud_t02 = make_box("TACTICAL STAGE HUD: PASSAGE 07 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — AURA OF GRIEF SHATTERED & 528 HZ CHIME]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]            [HARIN] [DOHA]  [MOURN]  [SORA]  [YEON]  [MINJAE][JISOO] [SILENT]",
        "                                 [EXPOSE]                                 ",
        "---",
        "- Node 03: Harin (Anchored / Deflecting Ocean Spray)",
        "- Node 04: Doha (Pneumatic Anchor Sapper Pinning Shoreline Fault)",
        "- Node 05: SECC-UR-VIIω-001 (Aura of Grief Destroyed 0/1,200 HP)",
        "- Node 06: Sora (Silver Cowl Harmonic Damping Shattering Barrier)",
        "- Node 07: Yeonhwa (Theodolite Focus Beam Marking Inner Core)",
        "- Node 08: Minjae (Year Zero Inscription Weakening Halo Cohesion)",
        "- Node 10: The Silent One (Severing Crescent Ready for Halo Cleave)",
        "---",
        "- Sora        : Spd 9 -> 5 AP [SURGE] | HP 2,600/2,600 | SP 50/50 | Posture 100/100",
        "- Silent One  : Spd 9 -> 5 AP [SURGE] | HP 3,100/3,100 | SP 48/50 | Posture 120/120",
        "- Boss Heart  : Spd 4 -> 2 AP | HP 3,300/3,300 | Posture 282/360",
        "- Grief Aura  : DESTROYED (0/1,200 HP) | TIDAL BARRIER COLLAPSED",
        "- Tear Halo   : Spd 4 -> 2 AP | HP 1,450/1,500 | Posture 246/320"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: PASSAGE 07 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — STAGGER THRESHOLD 1 & TEAR HALO SEVERANCE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]            [HARIN] [DOHA]  [MOURN]  [SORA]  [YEON]  [SILENT]        [JISOO] ",
        "                                                  [MINJAE]                        ",
        "---",
        "- Node 03: Harin & Doha (Bracing Shoreline Against Millennial Echo)",
        "- Node 05: SECC-UR-VIIω-001 (STAGGER LEVEL 1 / DEFENSES COLLAPSED)",
        "- Node 06: Sora & Minjae (Harmonic Requiem Preparing Sync Fire)",
        "- Node 07: Yeonhwa (Optical Focus Beam Locking Wellspring Heart)",
        "- Node 08: The Silent One (Severing Crescent Shearing Halo to Shards)",
        "---",
        "- Silent One  : Spd 10 -> 5 AP [SURGE] | HP 3,100/3,100 | SP 50/50 | Posture 120/120",
        "- Boss Heart  : Spd 0 -> 0 AP | HP 2,960/3,300 | Posture 144/360 [STAGGER LEVEL 1]",
        "- Tear Halo   : Spd 0 -> 0 AP | HP 960/1,500   | Posture 112/320 [SHEARED]",
        "- Total Boss  : HP 3,920/6,000 [THRESHOLD BREACHED / TAKES 1.5X DAMAGE]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: PASSAGE 07 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — MAXIMUM BURST & PHASE 2 THRESHOLD SKIP]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]                    [HARIN] [MOURN]  [DOHA]  [SILENT][YEON]  [SORA]  [JISOO] ",
        "                                                  [MINJAE]                        ",
        "---",
        "- Node 04: Harin & Doha (Sapper Bulwark Compression Strike 440 Dmg)",
        "- Node 05: SECC-UR-VIIω-001 (Staggered / Wellspring Heart Exposed)",
        "- Node 06: Sora & Minjae (Harmonic Requiem of Truth 560 Lament)",
        "- Node 07: Yeonhwa & Jisoo (Acoustic Ledger Liquidation 520 Void)",
        "- Node 08: The Silent One (The Burden Cleave Core Strike 780 Void)",
        "- Node 10: Jisoo (Cryo Harpoon Anchoring Liquid Starlight Rim)",
        "---",
        "- Silent One  : Spd 11 -> 5 AP [BURST CRIT] | HP 3,100/3,100 | SP 50/50",
        "- Boss Heart  : Spd 0 -> 0 AP | HP 1,620/3,300 | Posture 64/360",
        "- Tear Halo   : DESTROYED (0/1,500 HP)",
        "- Total Boss  : HP 1,620/6,000 [BURST DAMAGE 2,300! SECOND THRESHOLD SKIPPED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: PASSAGE 07 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — INFINITE DELUGE & REQUIEM OF ABSOLUTION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]                    [HARIN] [MOURN]  [SILENT][DOHA]  [YEON]  [SORA]  [MINJAE]",
        "                                                          [JISOO]                 ",
        "---",
        "- Node 04: Harin & Doha (Vanguard Phalanx Holding Oceanic Shoreline)",
        "- Node 05: SECC-UR-VIIω-001 (Infinite Mugenhan Deluge / Boiling Sea)",
        "- Node 06: The Silent One (Relic Overdrive: REQUIEM OF THE FIRST MOURNER)",
        "- Node 07: Yeonhwa, Sora, Minjae, Jisoo (Harmonic Chimes in Unison)",
        "- Node 10: Center of Wellspring (The Burden Cleaver Bathing in Starlight)",
        "---",
        "- Silent One  : Spd 12 -> 5 AP [OVERDRIVE] | HP 3,100/3,100 | SP 50/50 [VOICE]",
        "- Boss Heart  : Spd 5 -> 3 AP | HP 1,620/3,300 | Posture 30/360 [ABSORBED]",
        "- Total Boss  : HP 1,620/6,000 [BOILING OCEAN SETTLES INTO TRANQUIL GLASS]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: PASSAGE 07 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — COMMUNION & PRIMORDIAL TEAR OF YEAR ZERO]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]                            [SILENT] [HARIN] [DOHA]  [SORA]  [YEON]  [SURFACE]",
        "                                 [REST]                           [MINJAE][JISOO]  ",
        "---",
        "- Node 05: SECC-UR-VIIω-001 First Mourner (PACIFIED & DISSOLVED TO LIGHT)",
        "- Node 06: The Silent One (Receives 'The Primordial Tear of Year Zero')",
        "- Node 07: Harin, Doha, Sora (Kneeling in Reverent Vigil Around Altar)",
        "- Node 08: Yeonhwa, Minjae, Jisoo (Finalizing Master 7-Strata Map)",
        "- Node 10: Cyclopean Floodgates Stabilized (Ascent Route to Surface OPEN)",
        "---",
        "- Vanguard Squad: Zero Fatalities | Composure 50/50 SP (Transcendent)",
        "- Encounter Status: 100% PACIFIED | Katabagil Descent COMPLETE"
    ])

    return f"""### The Vanguard Squad Combat Loadout

| Specialist | Position & Range Band | Primary Armament | Active Tactical Role | M.A.W.-W Class | Current SP |
|---|---|---|---|---|---|
| **The Silent One**| Band 1 (Melee Striker) | *The Burden of Year Zero* | Void Striker, Part Amputation, Overdrive | Medium (Spd 0, Crit +30%) | 44/40 SP |
| **Harin** | Band 1 (Melee Front) | *The Bastion of the Low* | Kinetic Fortress, Tidal Redirection | Heavy (Spd -1, Poise +25) | 48/50 SP |
| **Doha** | Band 1 (Melee Front) | *Calcified Pneumatic Ram* | Bedrock Fracture, Sapper Compression | Medium (Spd 0, Poise +20) | 40/40 SP |
| **Sora** | Band 2 (Mid Support) | *Silver Slumber Cowl* | Harmonic Damping, Lament Resonance | Light (Spd +1, SP Rec +15)| 50/50 SP |
| **Yeonhwa** | Band 3 (Ranged Command)| *The Horizon Theodolite* | Acoustic Fault Tagging, Theodolite Beam | Light (Spd +1, Evasion +15%)| 45/45 SP |
| **Minjae** | Band 4 (Forensic Scribe)| *Year Zero Archaeological Slate*| Truth Inscription, Historical Recording | Light (Spd +1, Scan +20%) | 50/50 SP |
| **Jisoo** | Band 4 (Tactical Record)| *Hydraulic Ballast Ledger*| Cosmic Audit, Ledger Liquidation | Light (Spd +1, Ballast 38%) | 50/50 SP |

---

### Turn-Based Combat Gauntlet: Pacifying the Primordial Source

```text
{dossier_box}
```

---

```text
{hud_t01}
```

###### Turn 01 Action Resolution Log (Intercepting the Primordial Tide)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Harin activates `[Vow of the Low Bulwark]`: Plants her tower shield deep into the crystalline starlight sand; gains $+3$ Protection and physical stagger immunity.
  * Doha prepares `[Pneumatic Anchor Sapper]`: Drives hydraulic anchors into the shoreline fault line to stabilize squad footing.
  * Yeonhwa initializes `[Sonar Acoustic Theodolite]`: Maps the frequency oscillations of the surrounding liquid Han ocean.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Harin (Speed 4 -> 2 AP, M.A.W.-W Heavy Armor delta $-1$, Poise $+25$): Holds Node 02. Spends 2 AP on `[Vow of the Low Bulwark: Kinetic Fortress]`.
  * The Silent One (Speed 7 -> 4 AP, M.A.W.-W Medium delta $0$, Crit $+30\%$): Holds the shoreline rim at Node 10. Spends 2 AP on positioning.
  * Doha (Speed 5 -> 3 AP, M.A.W.-W Medium delta $0$, Poise $+20$): Holds Node 03. Spends 2 AP on `[Pneumatic Anchor Sapper]`. Holds 1 AP in Guard.
  * Sora (Speed 7 -> 4 AP, M.A.W.-W Light delta $+1$): Holds Node 04. Spends 2 AP on `[Silver Cowl: Harmonic Damping]`. Holds 2 AP in Reserve.
  * Yeonhwa (Speed 7 -> 4 AP, M.A.W.-W Light delta $+1$): Holds Node 06. Spends 2 AP on `[Sonar Scan]`, 2 AP on `[Theodolite Beam]`.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 02 to 05)**: SECC-UR-VIIω-001 unleashes `[Primordial Weeping Tide]` (Base 18 + 2 Coins = 28 Power, Heavy Oceanic Lament).
    * Harin intercepts with `[Vow of the Low Bulwark: Kinetic Fortress]` (Base 22 + 2 Coins = 34 Power, Supreme Kinetic Shield).
    * **Clash Outcome**: Harin WINS THE CLASH OVERWHELMINGLY (34 vs 28)!
    * Harin plants the tower shield firmly into the starlight sand; the blinding turquoise sorrow wave breaks into harmless, warm spray (`[P3: Parry/Protection]`).
    * Harin reflects **310 kinetic tremor damage** into the Aura of Primordial Grief, inflicting $+58$ Posture Strain!
  * **Unopposed Bedrock Sapping**:
    * Doha's `[Pneumatic Anchor Sapper]` locks down the shoreline fault line, preventing tidal displacement and securing squad positioning!
- **Step 4: Turn End State**:
  * Aura of Primordial Grief HP: 1,200 -> **890/1,200** | Posture: **242/300**.
  * Total Boss HP: 6,000 -> **5,690/6,000** | Posture: **302/360**.
  * Vanguard Composure: **100% (All SP > 48)**. Zero damage taken.

---

```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Part Destruction: Aura of Grief Shattered)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Sora and The Silent One activate `Momentum Surge` (+2 Speed on Turn 02).
  * SECC-UR-VIIω-001 sweeps with `[Petrified Tear Barrage]` targeting the backline ranks.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Sora (Speed 9 -> 5 AP [Surge]): Steps to Node 06. Spends 3 AP on `[Silver Cowl: Harmonic Damping Wave]`.
  * The Silent One (Speed 9 -> 5 AP [Surge]): Steps from Node 10 to Node 08. Spends 3 AP on `[Severing Crescent Stance]`.
  * Harin (Speed 4 -> 2 AP): Holds Node 03, deflecting oceanic spray with `[Bulwark Wall]`.
  * Minjae (Speed 7 -> 4 AP): Inscribes `[Year Zero Inscription]` (2 AP), weakening tear halo cohesion.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 06 to 05)**: SECC-UR-VIIω-001 fires `[Petrified Tear Barrage]` (Base 18 + 2 Coins = 26 Power, Piercing Lament).
    * Sora clashes with `[Silver Cowl: Harmonic Damping Wave]` (Base 23 + 3 Coins Heads = 41 Power, Lament Harmony).
    * **Clash Outcome**: Sora WINS THE CLASH OVERWHELMINGLY (41 vs 26)!
    * The Silver Cowl resonates at pure 528 Hz; the harmonic wave completely shatters the surging tidal barrier!
    * Deals **580 Lament damage** (Fatal 2.0x proc!)!
    * **TARGETED PART DESTROYED**: The Aura of Primordial Grief collapses completely, exposing the entity's inner sanctum (**Aura HP: 0/1,200**)!
    * **EFFECT**: Boss loses tidal barrier shielding; boss permanently loses 1 Speed Slot!
- **Step 4: Turn End State**:
  * Aura of Primordial Grief: **DESTROYED (0/1,200 HP)**.
  * Halo of Petrified Tears: 1,500 -> **1,450/1,500** | Posture: **246/320**.
  * Total Boss HP: 5,690 -> **4,750/6,000** | Posture: **244/360 [AURA SHATTERED]**.
  * Vanguard Composure: Stable (> 48 SP across all members).

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (First Stagger Proc & Tear Halo Severance)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * SECC-UR-VIIω-001 pulses with `[Echo of Millennial Bereavement]` (Area Pale, 2 Coins).
  * The Silent One gains `Momentum Surge` (+2 Speed -> Net Speed 10, 5 AP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * The Silent One (Speed 10 -> 5 AP): Steps to Node 08. Spends 3 AP on `[Severing Crescent: Void Cleave]`.
  * Harin and Doha (Speed 4 & 5 -> 2 & 3 AP): Hold Nodes 03–04, locking shields against the echo wave.
  * Yeonhwa (Speed 7 -> 4 AP): Casts `[Theodolite Focus Beam]` (2 AP), marking the central core.
  * Sora and Minjae: Prepare synchronized harmonic resonance.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 08 to 05)**: SECC-UR-VIIω-001 unleashes `[Echo of Millennial Bereavement]` (Base 19 + 2 Coins = 27 Power, Pale).
    * The Silent One executes `[Severing Crescent: Void Cleave]` (Base 25 + 3 Coins Heads = 43 Power, Void Slash).
    * **Clash Outcome**: The Silent One WINS THE CLASH OVERWHELMINGLY (43 vs 27)!
    * The dark relic cleaver cleanly shears through the Petrified Tear Halo!
    * Deals **540 Void damage** (Fatal 2.0x proc!)!
    * **TARGETED PART DESTROYED**: The Halo of Petrified Tears shatters into shimmering sapphire dust (**Halo HP: 0/1,500**)!
- **Step 4: STAGGER THRESHOLD 1 TRIGGERED!**:
  * Total Boss HP crosses 70% threshold (4,200 HP), falling to **3,920/6,000 HP**; Posture crosses 60% strain line!
  * **STAGGER LEVEL 1 ACTIVE!** The First Mourner bows its head upon the altar; all defenses drop to zero; takes $+50\%$ damage across all incoming attacks!
- **Step 5: Turn End State**:
  * Total Boss HP: 4,750 -> **3,920/6,000 [THRESHOLD BREACHED: Below 4,200 HP!]**.
  * Halo of Petrified Tears: **DESTROYED (0/1,500 HP)**.
  * Boss Posture: **144/360 [STAGGER LEVEL 1]**.
  * Vanguard Status: Unbroken.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Maximum Burst & Phase 2 Threshold Skip)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * SECC-UR-VIIω-001 remains completely stunned; the Wellspring Heart in its chest cavity is exposed, pulsing with radiant white sorrow.
  * All seven specialists coordinate synchronized resonant focus fire.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Harin & Doha: Execute `[Sapper Bulwark Compression Strike]` (4 AP combined).
  * Sora & Minjae: Channel `[Harmonic Requiem of Truth]` (4 AP combined).
  * Yeonhwa & Jisoo: Unleash `[Acoustic Ledger Liquidation]` (4 AP combined).
  * The Silent One: Executes `[The Burden Cleave: Core Strike]` (3 AP).
- **Step 3: Unopposed Stagger Punishment Rotation**:
  * Harin & Doha's `[Sapper Bulwark Compression Strike]`: Delivers **440 Weight damage**!
  * Sora & Minjae's `[Harmonic Requiem of Truth]`: Delivers **560 Pure Lament damage**!
  * Yeonhwa & Jisoo's `[Acoustic Ledger Liquidation]`: Delivers **520 Void damage**!
  * The Silent One's `[The Burden Cleave: Core Strike]`: Delivers **780 Void damage** (Fatal 2.0x proc!)!
  * **TOTAL BURST DAMAGE: 2,300 DAMAGE!**
- **Step 4: SECOND STAGGER THRESHOLD (2,400 HP) COMPLETELY SKIPPED!**:
  * Boss HP plunges from 3,920 down to **1,620/6,000 HP**!
  * **Phase 2 Emergency Activation Triggered!**
- **Step 5: Turn End State**:
  * Total Boss HP: 3,920 -> **1,620/6,000** (Core HP: **1,620/3,300**).
  * Posture: **64/360**.

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Phase 2 Escalation: Infinite Mugenhan Deluge & Requiem of Absolution)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * The First Mourner awakens in cosmic agony; the entire subterranean ocean begins to boil with turquoise luminescence!
  * Boss Special Skill: `[Infinite Mugenhan Deluge]` (Primordial Cataclysm, 5 Coins).
  * Speed Dice gains 5 slots! Cosmic grief surges to drown reality itself.
  * The Silent One breaks four centuries of absolute silence:
    > *"WE CARRY THIS SORROW TOGETHER!"*
  * The Silent One activates Relic Overdrive: `[REQUIEM OF THE FIRST MOURNER — ABSOLUTION]` (Cost: 3 AP, 30 SP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * The Silent One (Speed 12 -> 5 AP [Overdrive]): Steps directly to Node 06 before the altar.
  * Harin & Doha (Speed 4 & 5): Hold Node 04, locking shields to stabilize the shoreline.
  * Yeonhwa, Sora, Minjae, and Jisoo: Stand at Nodes 07–08, channeling their instruments in harmony.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 06 to 05)**: SECC-UR-VIIω-001 unleashes `[Infinite Mugenhan Deluge]` (Base 25 + 5 Coins = 40 Power, Cosmic Han).
    * The Silent One clashes with `[REQUIEM OF THE FIRST MOURNER — ABSOLUTION]` (Base 32 + 4 Coins Heads = 54 Power, Transcendent Solace).
    * **Clash Outcome**: THE SILENT ONE OVERWHELMING RELIC CLASH WIN (54 vs 40)!
    * The Burden of Year Zero opens, bathing the chasm in warm, golden starlight (`[P3: Parry/Protection]`)!
    * The millennial burden of loss is absorbed peacefully into the seven specialists' shared consciousness!
    * The boiling ocean settles into tranquil, mirror-like glass; the primordial cataclysm is averted!
    * Zero squad damage taken! Squad Composure maxed at 50/50 SP each!
- **Step 4: Turn End State**:
  * Total Boss HP: **1,620/6,000** | Posture: **30/360 [SOUL AT PEACE]**.
  * Vanguard Composure: 50/50 SP across all members.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Communion & The Primordial Tear of Year Zero)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * The First Mourner opens their eyes, weeping tears of warm light. Posture reaches **0/360 [TERMINAL SOLACE]**.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * The seven specialists kneel in unison around the quiet wellspring at Nodes 05–07.
  * Sora, Minjae, and Jisoo speak together: *"You are no longer alone."*
  * The Silent One rests the relic cleaver gently upon the stone altar at Node 05.
- **Step 3: Non-Lethal Communion & Peaceful Resolution**:
  * The Primordial Source achieves eternal solace; the tide stills into warm, pearlescent light.
  * Deals **1,620 Peaceful Harmony**! First Mourner HP drops to 0!
  * Thousands of white sorrow blossoms open their petals across the calm water, releasing a fragrance of unburdened peace.
- **Step 4: Operational Artifact Extraction & Completion of Katabagil**:
  * **Artifact Acquired**: `[Relic: The Primordial Tear of Year Zero]` (Flawless tear-drop gemstone placed into The Silent One's palm).
  * **The Silent One's Promise**: *"Rest now. We will carry the memory. The world will never forget."*
  * **Tectonic Outcome**: The cyclopean floodgates stabilize at a tranquil, steady flow; subterranean Sorrow Tides are calmed permanently.
  * **The Ascent**: The seven specialists turn and begin their ascent back to the surface of Somnarak, carrying the complete 7-strata map and records to the people.
  * **Casualties**: Flawless Victory. Zero Fatalities. Harin (HP 4,200/4,200), Doha (HP 3,600/3,600). Squad Composure 50/50 SP."""

def update_passage_7():
    path = "SOMNARAK-WORLD/Katabagil/Passage_7_Fontisaem.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    start_str = "### The Vanguard Squad Combat Loadout"
    end_str = "## Chapter VIII: Epilogue: The Ascent & The Unbroken Ledger"

    start_idx = content.find(start_str)
    end_idx = content.find(end_str)

    if start_idx == -1 or end_idx == -1:
        print(f"Error locating boundaries! start_idx={start_idx}, end_idx={end_idx}")
        return

    new_engagement = get_p7_engagement() + "\n\n---\n\n"
    new_content = content[:start_idx] + new_engagement + content[end_idx:]

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Updated Passage 7 successfully!")

if __name__ == "__main__":
    update_passage_7()
