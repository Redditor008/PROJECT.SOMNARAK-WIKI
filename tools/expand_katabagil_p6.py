#!/usr/bin/env python3
"""
tools/expand_katabagil_p6.py
Expands Passage 6 (Traumagol - The Occlusihan Rift) in SOMNARAK-WORLD/Katabagil/Passage_6_Traumagol.md
Replaces the older combat gauntlet with full 10-node spatial tactical HUDs, Speed/AP breakdowns,
M.A.W.-W weight deltas, and Four P-framework action resolution logs across all 6 turns.
"""

import sys, os
sys.path.append(os.path.dirname(__file__))
from box_formatter import make_box

def get_p6_engagement():
    dossier_box = make_box("APEX BOSS DOSSIER: SECC-1004 'THE SCAR WALKER'", [
        "APEX TARGET        : SECC-1004 'The Scar Walker'",
        "CLASSIFICATION     : Critical-δ (Grade-δ Potency) | Sovereign of Occlusihan",
        "ENCOUNTER DOMAIN   : Strata 6 Occlusihan Wound (-2,800m Depth)",
        "---",
        "BOSS COMBAT PROFILE (SECC-1004):",
        "- Total Health (HP): 4,800 HP | Posture Pool: 340/340",
        "- Stagger 1 Proc   : 60% Posture Strain (204 Posture) / Glaive Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Terminal Pacification)",
        "- Resistances      : Void 2.0x (Fatal), Lament 1.0x, Grudge 0.5x, Weight 0.5x",
        "---",
        "TARGETABLE COMPONENT PARTS:",
        "1. Fury Glaive     : 1,150 HP | Posture 280/280 (Sweeping crimson polearm)",
        "2. Occlusihan Plate: 1,450 HP | Posture 300/300 (Heavy grave-marker armor)",
        "3. Wound Heart Core: 2,200 HP | Posture 340/340 (Central soul-lattice heart)"
    ])

    hud_t01 = make_box("TACTICAL STAGE HUD: PASSAGE 06 — BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 — STRATA 6 OCCLUSIHAN WOUND (-2,800M)]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]   [HARIN]  [DOHA]  [SORA]  [BOSS]   [YEON]  [SILENT][JISOO]         [MINJAE]",
        "                                 [GLAIVE]                                 ",
        "---",
        "- Node 01: Vertical Shaft Platform / Armored Rig 'The Iron Mole'",
        "- Node 02: Harin (Vanguard Band 1 / Bastion of the Low Tower Shield)",
        "- Node 03: Doha (Point-Blank Band 1 / Calcified Pneumatic Fracture Ram)",
        "- Node 04: Sora (Mid-Field Band 2 / Silver Cowl Mnemonic Repose)",
        "- Node 05: SECC-1004 Scar Walker (Solidified Fury Glaive & Cuirass)",
        "- Node 06: Yeonhwa (Mid-Field Band 3 / Sonar Acoustic Theodolite)",
        "- Node 07: The Silent One (Overhead Ribcage Catwalks / Relic Cleaver)",
        "- Node 08: Jisoo (Forensic Record Band 4 / Hydraulic Ballast Ledger)",
        "- Node 10: Minjae (Rear Band 5 / Historical Archival Slate)",
        "---",
        "- Harin       : Spd 4 -> 2 AP | HP 4,200/4,200 | SP 46/50 | Posture 180/180",
        "- Silent One  : Spd 7 -> 4 AP | HP 3,100/3,100 | SP 42/40 | Posture 120/120",
        "- Doha        : Spd 5 -> 3 AP | HP 3,600/3,600 | SP 40/40 | Posture 150/150",
        "- Sora        : Spd 7 -> 4 AP | HP 2,600/2,600 | SP 50/50 | Posture 100/100",
        "- Yeonhwa     : Spd 7 -> 4 AP | HP 2,700/2,700 | SP 45/45 | Posture 100/100",
        "- Jisoo       : Spd 7 -> 4 AP | HP 2,750/2,750 | SP 50/50 | Posture 110/110",
        "- Boss Core   : Spd 4 -> 2 AP | HP 2,200/2,200 | Posture 340/340 [HOWLING]",
        "- Fury Glaive : Spd 5 -> 3 AP | HP 1,150/1,150 | Posture 280/280 [CRIMSON]",
        "- Cuirass Plate: Spd 3 -> 1 AP | HP 1,450/1,450 | Posture 300/300 [OBSIDIAN]"
    ])

    hud_t02 = make_box("TACTICAL STAGE HUD: PASSAGE 06 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — FURY GLAIVE SHATTERED & VOID CUT]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]            [HARIN] [DOHA]  [BOSS]   [SORA]  [YEON]  [JISOO] [MINJAE][SILENT]",
        "                                 [SHARDS]                                 ",
        "---",
        "- Node 03: Harin (Anchored / Deflecting Phantom Shrapnel Storm)",
        "- Node 04: Doha (Pneumatic Fracture Ram Cracking Obsidian Seams)",
        "- Node 05: SECC-1004 Scar Walker (Fury Glaive Destroyed 0/1,150 HP)",
        "- Node 06: Sora (Silver Requiem Chime Quelling Wrath Embers)",
        "- Node 07: Yeonhwa (Sonar Fault Lock on Grave-Marker Cuirass)",
        "- Node 10: The Silent One (Severing Crescent Cleaving Glaive Shaft)",
        "---",
        "- Silent One  : Spd 9 -> 5 AP [SURGE] | HP 3,100/3,100 | SP 46/50 | Posture 120/120",
        "- Doha        : Spd 7 -> 4 AP [SURGE] | HP 3,600/3,600 | SP 44/40 | Posture 150/150",
        "- Boss Core   : Spd 4 -> 2 AP | HP 2,200/2,200 | Posture 264/340",
        "- Fury Glaive : DESTROYED (0/1,150 HP) | SWEEPING CLEAVE PERMANENTLY LOST",
        "- Cuirass Plate: Spd 3 -> 1 AP | HP 1,110/1,450 | Posture 232/300"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: PASSAGE 06 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — STAGGER THRESHOLD 1 & CUIRASS FRACTURE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]            [HARIN] [DOHA]  [BOSS]   [SORA]  [YEON]  [SILENT]        [JISOO] ",
        "---",
        "- Node 03: Harin (Piston Shield Wall Bracing Against Shrapnel)",
        "- Node 04: Doha (Sapper Counter-Lever Popping Heavy Cuirass Plate)",
        "- Node 05: SECC-1004 (STAGGER LEVEL 1 / DEFENSES COLLAPSED / IMMOBILIZED)",
        "- Node 06: Sora (Chime of Quelled Grief Weakening Phantoms)",
        "- Node 07: Minjae (Keeper Inscription Weakening Soul Lattice)",
        "- Node 08: The Silent One (Preparing Void Core Thrust)",
        "---",
        "- Harin       : Spd 6 -> 3 AP [SURGE] | HP 4,200/4,200 | SP 48/50 | Posture 180/180",
        "- Boss Core   : Spd 0 -> 0 AP | HP 2,050/2,200 | Posture 130/340 [STAGGER LEVEL 1]",
        "- Cuirass Plate: Spd 0 -> 0 AP | HP 650/1,450   | Posture 102/300 [FRACTURED]",
        "- Total Boss  : HP 3,100/4,800 [THRESHOLD BREACHED / TAKES 1.5X DAMAGE]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: PASSAGE 06 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — MAXIMUM BURST & PHASE 2 THRESHOLD SKIP]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]                    [HARIN] [BOSS]   [DOHA]  [SILENT][YEON]  [SORA]  [JISOO] ",
        "---",
        "- Node 04: Harin (Bulwark Kinetic Pummel Crushing Leg Joints)",
        "- Node 05: SECC-1004 Scar Walker (Staggered / Living Wound Exposed)",
        "- Node 06: Doha (Sapper Thermite Detonation Searing Phantom Armor)",
        "- Node 07: The Silent One (The Burden Cleave Driving into Heart)",
        "- Node 08: Yeonhwa & Sora (Theodolite Laser & Harmonic Repose)",
        "- Node 10: Jisoo (Cryo Harpoon Anchoring Cooling Obsidian Ribs)",
        "---",
        "- Silent One  : Spd 10 -> 5 AP [BURST CRIT] | HP 3,100/3,100 | SP 50/50",
        "- Boss Core   : Spd 0 -> 0 AP | HP 870/2,200   | Posture 58/340",
        "- Cuirass Plate: DESTROYED (0/1,450 HP)",
        "- Total Boss  : HP 1,520/4,800 [BURST DAMAGE 1,580! SECOND THRESHOLD SKIPPED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: PASSAGE 06 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — OCCLUSIHAN RESENTMENT & ABSOLUTE AUDIT]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]                    [HARIN] [BOSS]   [JISOO] [SILENT][YEON]  [SORA]  [MINJAE]",
        "                                                  [DOHA]                          ",
        "---",
        "- Node 04: Harin (Shielding Squad From 400-Year War Agony Wave)",
        "- Node 05: SECC-1004 (Cataclysmic Occlusihan Resentment / Six Armies)",
        "- Node 06: Jisoo (Relic Overdrive: ABSOLUTE ACKNOWLEDGMENT OF DEBT)",
        "- Node 07: The Silent One & Doha (Readying Void Cleave on Wound Crest)",
        "- Node 09: Sora (Chime of Quelled Grief Calming Phantoms)",
        "---",
        "- Jisoo       : Spd 8 -> 4 AP [OVERDRIVE] | HP 2,750/2,750 | SP 50/50 [LEDGER]",
        "- Boss Core   : Spd 4 -> 2 AP | HP 870/2,200   | Posture 28/340 [ACKNOWLEDGED]",
        "- Total Boss  : HP 870/4,800 [WAR CATACLYSM DISSIPATING INTO SILENCE]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: PASSAGE 06 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — PACIFYING THE RIFT & OCCLUSIHAN WOUND-CREST]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]                            [JISOO]  [SILENT][HARIN] [DOHA]  [SORA]  [OCEAN] ",
        "                                 [REST]                           [YEON]  [MINJAE]",
        "---",
        "- Node 05: SECC-1004 Scar Walker (PACIFIED & KNEELING IN TWILIGHT CALM)",
        "- Node 06: Jisoo (Receives 'The Occlusihan Wound-Crest' in Reverence)",
        "- Node 07: The Silent One (Delivers Final Peaceful Touch of The Burden)",
        "- Node 08: Harin & Doha (Securing Cyclopean Spiral Staircase Edge)",
        "- Node 10: Subterranean Ocean Descent (Pathway to Strata 7 Fontisaem OPEN)",
        "---",
        "- Vanguard Squad: Zero Fatalities | Composure 50/50 SP (Serene)",
        "- Encounter Status: 100% PACIFIED | Pathway to Fontisaem OPEN"
    ])

    return f"""### The Vanguard Squad Combat Loadout

| Specialist | Position & Range Band | Primary Armament | Active Tactical Role | M.A.W.-W Class | Current SP |
|---|---|---|---|---|---|
| **Jisoo** | Band 4 (Tactical Record)| *Hydraulic Ballast Ledger*| True Audit, Debt Acknowledgment, Overdrive | Light (Spd +1, Ballast 45%) | 50/50 SP |
| **Harin** | Band 1 (Melee Front) | *The Bastion of the Low* | Kinetic Lock, Glaive Redirection, Wall | Heavy (Spd -1, Poise +25) | 46/50 SP |
| **Doha** | Band 1 (Melee Front) | *Calcified Pneumatic Ram* | Bedrock Fracture, Plate Sapping, Wedge | Medium (Spd 0, Poise +20) | 40/40 SP |
| **The Silent One**| Band 1 (Melee Striker)| *Severed Relic Cleaver* | Void Executioner, Glaive Amputation | Medium (Spd 0, Crit +30%) | 42/40 SP |
| **Sora** | Band 2 (Mid Support) | *Silver Slumber Cowl* | Silver Requiem Resonance, Grief Quelling | Light (Spd +1, SP Rec +15)| 50/50 SP |
| **Yeonhwa** | Band 3 (Ranged Command)| *The Horizon Theodolite* | Acoustic Fault Tagging, Theodolite Laser | Light (Spd +1, Evasion +15%)| 45/45 SP |
| **Minjae** | Band 4 (Forensic Scribe)| *Year Zero Archaeological Slate*| Casualty Roster Transcription, Inscription | Light (Spd +1, Scan +20%) | 45/45 SP |

---

### Turn-Based Combat Gauntlet: Pacifying the Scar Walker

```text
{dossier_box}
```

---

```text
{hud_t01}
```

###### Turn 01 Action Resolution Log (Intercepting the Fury Glaive)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Harin activates `[Bastion Kinetic Lock]`: Drives the tower shield into the obsidian ridge; gains +3 Protection and intercepts the Walker's sweeping glaive arc.
  * Sora initializes `[Silver Requiem Chime]`: Emits 528 Hz harmonics to calm the howling wails of the ancient war dead.
  * Yeonhwa casts `[Acoustic Fault Lock]`: Focuses sensor arrays on the Solidified Fury Glaive's central balance fulcrum.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Harin (Speed 4 -> 2 AP, M.A.W.-W Heavy Armor delta -1, Poise +25): Holds Node 02. Spends 2 AP on `[Bastion Kinetic Lock: Obsidian Ground]`.
  * The Silent One (Speed 7 -> 4 AP, M.A.W.-W Medium delta 0, Crit +30\%): Perches on overhead ribcage catwalks at Node 07. Spends 2 AP on positioning.
  * Doha (Speed 5 -> 3 AP, M.A.W.-W Medium delta 0, Poise +20): Holds Node 03. Spends 2 AP on `[Pneumatic Wedge Drive]`. Holds 1 AP in Guard.
  * Sora (Speed 7 -> 4 AP, M.A.W.-W Light delta +1): Holds Node 04. Spends 2 AP on `[Silver Requiem Chime]`. Holds 2 AP in Reserve.
  * Yeonhwa (Speed 7 -> 4 AP, M.A.W.-W Light delta +1): Holds Node 06. Spends 2 AP on `[Acoustic Fault Lock]`, 2 AP on `[Acoustic Dart]`.
  * Jisoo (Speed 7 -> 4 AP, M.A.W.-W Light delta +1): Stands at Node 08, verifying casualty ledgers.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 02 to 05)**: SECC-1004 unleashes `[Fury Glaive Cleave]` (Base 18 + 2 Coins = 28 Power, Heavy Grudge/Slash).
    * Harin intercepts with `[Bastion Kinetic Lock]` (Base 21 + 2 Coins = 33 Power, Tower Shield).
    * **Clash Outcome**: Harin WINS THE CLASH OVERWHELMINGLY (33 vs 28)!
    * Harin plants the tower shield firmly into the obsidian ridge; the crimson fury glaive shudders violently and rebounds off the reinforced steel face (`[P3: Parry/Protection]`).
    * Harin reflects **260 kinetic tremor damage** into the glaive shaft, inflicting +52 Posture Strain!
  * **Unopposed Sapper Strike**:
    * Doha's `[Pneumatic Wedge Drive]` cracks the obsidian bedrock beneath the Walker's lead foot, dealing **180 Blunt damage**!
- **Step 4: Turn End State**:
  * Solidified Fury Glaive HP: 1,150 -> **890/1,150** | Posture: **188/280**.
  * Total Boss HP: 4,800 -> **4,540/4,800** | Posture: **288/340**.
  * Vanguard Composure: **100% (All SP > 46)**. Zero damage taken.

---

```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Part Destruction: Solidified Fury Glaive Shattered)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * The Silent One and Doha activate `Momentum Surge` (+2 Speed on Turn 02).
  * SECC-1004 attempts `[Occlusihan Shockwave]` sweeping the front and mid ranks.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * The Silent One (Speed 9 -> 5 AP [Surge]): Drops from overhead ribcage catwalks at Node 07 onto the glaive fulcrum at Node 05. Spends 3 AP on `[Severing Crescent: Void Cleave]`.
  * Doha (Speed 7 -> 4 AP [Surge]): Steps from Node 03 to Node 04. Spends 3 AP on `[Pneumatic Fracture Ram]`.
  * Harin (Speed 4 -> 2 AP): Holds Node 03, deflecting phantom shrapnel with `[Bulwark Stance]`.
  * Sora (Speed 7 -> 4 AP): Holds Node 06, quelling burning embers with `[Silver Requiem]` (2 AP).
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 07 to 05)**: SECC-1004 swings with `[Occlusihan Shockwave]` (Base 18 + 2 Coins = 28 Power, Area Grudge).
    * The Silent One executes `[Severing Crescent: Void Cleave]` (Base 24 + 3 Coins Heads = 43 Power, Void Slash).
    * **Clash Outcome**: The Silent One WINS THE CLASH OVERWHELMINGLY (43 vs 28)!
    * The dark relic cleaver slices cleanly through the Solidified Fury Glaive's central obsidian spine!
    * Deals **520 Critical Void damage** (Fatal 2.0x proc!)!
    * **TARGETED PART DESTROYED**: The Solidified Fury Glaive fractures into smoking black shards (**Glaive HP: 0/1,150**)!
    * **EFFECT**: Boss sweeping cleave permanently disabled; boss permanently loses 1 Speed Slot!
  * **Cuirass Armor Damage**:
    * Doha's `[Pneumatic Fracture Ram]` cracks the Occlusihan Cuirass, dealing **260 Blunt damage**!
- **Step 4: Turn End State**:
  * Solidified Fury Glaive: **DESTROYED (0/1,150 HP)**.
  * Occlusihan Cuirass: 1,450 -> **1,110/1,450** | Posture: **232/300**.
  * Total Boss HP: 4,540 -> **3,760/4,800** | Posture: **220/340 [GLAIVE SHATTERED]**.
  * Vanguard Composure: Stable (> 44 SP across all members).

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (First Stagger Proc & Cuirass Fracture)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * SECC-1004 unleashes a desperate counter: `[Unmourned Retribution]` (Heavy Weight, 2 Coins).
  * Doha gains `Momentum Surge` (+2 Speed -> Net Speed 7, 4 AP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Doha (Speed 7 -> 4 AP): Steps to Node 04. Spends 2 AP on `[Sapper Counter-Lever]`.
  * Harin (Speed 6 -> 3 AP): Steps to Node 03. Spends 2 AP on `[Piston Shield Wall]`.
  * Minjae (Speed 7 -> 4 AP): Casts `[Keeper Inscription]` (2 AP), weakening the phantom lattice.
  * Yeonhwa (Speed 7 -> 4 AP): Casts `[Acoustic Theodolite Laser]` (2 AP).
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 04 to 05)**: SECC-1004 strikes with `[Unmourned Retribution]` (Base 17 + 2 Coins = 25 Power, Heavy Weight).
    * Doha clashes with `[Sapper Counter-Lever]` (Base 21 + 2 Coins = 33 Power, Heavy Lever).
    * **Clash Outcome**: Doha WINS THE CLASH (33 vs 25)!
    * Doha levers his tungsten sapper spike into the Occlusihan Cuirass seam; the pneumatic ram detonations echo like artillery!
    * The ancient war plate fractures from collar to waist, dealing **460 Blunt damage** and +82 Posture Strain!
- **Step 4: STAGGER THRESHOLD 1 TRIGGERED!**:
  * Total Boss HP crosses 70% threshold (3,360 HP), falling to **3,100/4,800 HP**; Posture crosses 60% strain line!
  * **STAGGER LEVEL 1 ACTIVE!** The titan falls to its knees upon the obsidian ridge; all defenses drop to zero; takes +50\% damage across all incoming attacks!
- **Step 5: Turn End State**:
  * Total Boss HP: 3,760 -> **3,100/4,800 [THRESHOLD BREACHED: Below 3,360 HP!]**.
  * Occlusihan Cuirass: 1,110 -> **650/1,450** | Posture: **102/300 [FRACTURED]**.
  * Boss Posture: **130/340 [STAGGER LEVEL 1]**.
  * Vanguard Status: Unbroken.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Maximum Burst & Phase 2 Threshold Skip)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * SECC-1004 remains completely stunned on both knees; the Living Wound Core in its chest cavity is exposed, burning with turbulent crimson soul-light.
  * All Vanguard Specialists coordinate maximum burst fire targeting the exposed wound core.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * The Silent One (Speed 10 -> 5 AP, Momentum Crit): Stands at Node 07. Spends 3 AP on `[The Burden Cleave: Core Strike]`.
  * Harin (Speed 4 -> 2 AP): Steps to Node 04. Spends 2 AP on `[Bulwark Kinetic Pummel]`.
  * Doha (Speed 5 -> 3 AP): Moves to Node 06. Spends 3 AP on `[Sapper Thermite Detonation]`.
  * Yeonhwa (Speed 7 -> 4 AP): Stands at Node 08. Spends 2 AP on `[Acoustic Theodolite Laser]`.
  * Jisoo (Speed 7 -> 4 AP): Fires `[Cryo Harpoon Anchor]` from Node 10 (2 AP).
- **Step 3: Unopposed Stagger Punishment Rotation**:
  * The Silent One's `[Core Strike]`: Slices through the soul lattice for **680 Void damage** (Fatal 2.0x proc!)!
  * Harin's `[Bulwark Kinetic Pummel]`: Smashes leg joints for **290 Weight damage**!
  * Doha's `[Sapper Thermite Detonation]`: Burns away obsidian struts for **360 Explosive Grudge damage**!
  * Yeonhwa's `[Acoustic Theodolite Laser]`: Focuses resonance for **250 Focused Resonance damage**!
  * **TOTAL BURST DAMAGE: 1,580 DAMAGE!**
- **Step 4: SECOND STAGGER THRESHOLD (1,920 HP) COMPLETELY SKIPPED!**:
  * Boss HP plunges from 3,100 down to **1,520/4,800 HP**! Occlusihan Cuirass completely destroyed (0/1,450 HP)!
  * **Phase 2 Emergency Activation Triggered!**
- **Step 5: Turn End State**:
  * Total Boss HP: 3,100 -> **1,520/4,800** (Core HP: **870/2,200** | Cuirass: **DESTROYED**).
  * Posture: **58/340**.

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Phase 2 Escalation: Occlusihan Resentment & Absolute Audit)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Walker awakens in titanic agony, releasing four centuries of unmourned war resentment!
  * Boss Special Skill: `[Cataclysmic Occlusihan Resentment]` (War Cataclysm, 3 Coins).
  * Speed Dice expands to 4 slots! Phantoms of eighty thousand fallen soldiers materialize across the chasm.
  * Jisoo activates Relic Overdrive: `[ABSOLUTE ACKNOWLEDGMENT OF UNPAID DEBT — MAXIMUM]` (Cost: 3 AP, 30 SP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Jisoo (Speed 8 -> 4 AP [Overdrive]): Steps onto the rift edge at Node 06, opening the Hydraulic Ballast Ledger.
  * Harin (Speed 4 -> 2 AP): Shields the squad from 400-year war agony waves at Node 04 with `[Bastion Wall]`.
  * Doha (Speed 5 -> 3 AP): Drops structural anchors into Node 06.
  * The Silent One (Speed 7 -> 4 AP): Prepares `[The Burden Peace]` at Node 07.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 06 to 05)**: SECC-1004 unleashes `[Cataclysmic Occlusihan Resentment]` (Base 22 + 3 Coins = 34 Power, Area Pale/Grudge).
    * Jisoo clashes with `[ABSOLUTE ACKNOWLEDGMENT OF UNPAID DEBT — MAXIMUM]` (Base 28 + 3 Coins Heads = 49 Power, Truth Audit).
    * **Clash Outcome**: JISOO OVERWHELMING RELIC CLASH WIN (49 vs 34)!
    * Jisoo reads the names of every fallen soldier from the thirty copper ledgers into the howling abyss!
    * The unpaid structural debt of the First War is formally acknowledged by the living (`[P3: Parry/Protection]`)!
    * The ancient fury dissipates into peaceful silence; the war cataclysm is halted!
    * Zero squad damage taken! Squad Composure maxed at 50/50 SP!
- **Step 4: Turn End State**:
  * Total Boss HP: **1,520 -> 870/4,800** | Posture: **28/340 [CRITICAL COLLAPSE]**.
  * Vanguard Composure: 50/50 SP across all members.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Pacifying the Rift & Occlusihan Wound-Crest)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * The Scar Walker kneels upon the obsidian ridge, head bowed in peaceful rest. Posture reaches **0/340 [TERMINAL PACIFICATION]**.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Harin and Doha secure the perimeter as Sora chants a peaceful hymn.
  * Jisoo walks forward across the quiet stone to Node 06.
  * The Silent One steps forward onto the central dais at Node 06.
  * Minjae and Yeonhwa log the final coordinates and map the unsealed staircase.
- **Step 3: Overdrive Execution & Peaceful Pacification**:
  * The Silent One delivers the final pacification: `[The Burden Peace: Soul Release]` (Power 45).
  * The cleaver touches the core gently, releasing the bound souls with pure reverent grace.
  * Deals **870 Pure Resonant Void damage**! SECC-1004 HP drops to 0!
  * The crimson fires gently flicker out, leaving behind a tranquil twilight calm.
- **Step 4: Operational Artifact Extraction & Strata Access**:
  * **Artifact Acquired**: `[Relic: The Occlusihan Wound-Crest]` (Ornate crest of dark silver and polished obsidian).
  * **Jisoo's Reconciliation**: Jisoo receives the relic in her hands: *"The audit is complete. The debt is not paid. But it is seen. It is remembered. And we will carry it with us."*
  * **Descent Access**: The bedrock floor parts, revealing a cyclopean spiral staircase descending into pale iridescent blue light.
  * **Descent Destination**: The sound of a subterranean ocean echoes from below—**Strata 7: Fontisaem—The Primordial Wellspring (-2,800m to Core)**.
  * **Casualties**: Flawless Victory. Zero Fatalities. Harin (HP 4,200/4,200), Doha (HP 3,600/3,600). Squad Composure 50/50 SP."""

def update_passage_6():
    path = "SOMNARAK-WORLD/Katabagil/Passage_6_Traumagol.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    start_str = "### The Vanguard Squad Combat Loadout"
    end_str = "## Chapter VIII: Epilogue & Acquisition"

    start_idx = content.find(start_str)
    end_idx = content.find(end_str)

    if start_idx == -1 or end_idx == -1:
        print(f"Error locating boundaries! start_idx={start_idx}, end_idx={end_idx}")
        return

    new_engagement = get_p6_engagement() + "\n\n---\n\n"
    new_content = content[:start_idx] + new_engagement + content[end_idx:]

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Updated Passage 6 successfully!")

if __name__ == "__main__":
    update_passage_6()
