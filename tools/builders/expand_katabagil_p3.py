#!/usr/bin/env python3
"""
tools/expand_katabagil_p3.py
Expands Passage 3 (Furtugil - Severed Smuggler Arteries) in SOMNARAK-WORLD/Katabagil/Passage_3_Furtugil.md
Replaces the older combat gauntlet with full 10-node spatial tactical HUDs, Speed/AP breakdowns,
M.A.W.-W weight deltas, and Four P-framework action resolution logs across all 6 turns.
"""

import sys, os
sys.path.append(os.path.dirname(__file__))
from box_formatter import make_box

def get_p3_engagement():
    dossier_box = make_box("APEX BOSS DOSSIER: SECC-041 'RAIL SOVEREIGN'", [
        "APEX TARGET        : SECC-041 'The Clandestine Rail Sovereign'",
        "CLASSIFICATION     : Major-γ (Grade-γ Potency) | Pre-Structuring Transit Apex",
        "ENCOUNTER DOMAIN   : Strata 3 Grand Concourse Junction (-900m Depth)",
        "---",
        "BOSS COMBAT PROFILE (SECC-041):",
        "- Total Health (HP): 3,200 HP | Posture Pool: 280/280",
        "- Stagger 1 Proc   : 60% Posture Strain (168 Posture) / Mandible Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Terminal Derailment)",
        "- Resistances      : Void 2.0x (Fatal), Lament 1.5x, Weight 1.0x, Grudge 0.5x",
        "---",
        "TARGETABLE COMPONENT PARTS:",
        "1. Rail Mandibles  : 850 HP | Posture 220/220 (High-velocity crushing bites)",
        "2. Carapace Plating: 1,100 HP | Posture 250/250 (Kinetic deflection shield)",
        "3. Lantern Core    : 1,250 HP | Posture 280/280 (Central pale searchlight)"
    ])

    hud_t01 = make_box("TACTICAL STAGE HUD: PASSAGE 03 — BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 — STRATA 3 CONCOURSE JUNCTION (-900M)]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]   [HARIN]  [DOHA]  [SORA]  [BOSS]   [YEON]  [SILENT][MINJAE]        [JISOO] ",
        "                                 [MANDIB]                                 ",
        "---",
        "- Node 01: Concourse Turnstile Ingress / Armored Rig 'The Iron Mole'",
        "- Node 02: Harin (Vanguard Band 1 / Bastion of the Low Tower Shield)",
        "- Node 03: Doha (Point-Blank Band 1 / Calcified Pneumatic Drill Ram)",
        "- Node 04: Sora (Mid-Field Band 2 / Silver Cowl Lament Water Resonance)",
        "- Node 05: SECC-041 Rail Sovereign (Armored Mandibles & Carapace Plating)",
        "- Node 06: Yeonhwa (Mid-Field Band 3 / Sonar Track Lock Theodolite)",
        "- Node 07: The Silent One (High Catenary Rafters / Relic Cleaver)",
        "- Node 08: Minjae (Rear Band 4 / Transit Telemetry Slate)",
        "- Node 10: Jisoo (Rear Band 5 / Cryo Harpoon Logistics Berth)",
        "---",
        "- Harin       : Spd 4 -> 2 AP | HP 4,200/4,200 | SP 46/50 | Posture 180/180",
        "- Silent One  : Spd 7 -> 4 AP | HP 3,100/3,100 | SP 40/40 | Posture 120/120",
        "- Doha        : Spd 5 -> 3 AP | HP 3,600/3,600 | SP 38/40 | Posture 150/150",
        "- Sora        : Spd 7 -> 4 AP | HP 2,600/2,600 | SP 50/50 | Posture 100/100",
        "- Yeonhwa     : Spd 7 -> 4 AP | HP 2,700/2,700 | SP 45/45 | Posture 100/100",
        "- Boss Core   : Spd 4 -> 2 AP | HP 1,250/1,250 | Posture 280/280 [STEAMING]",
        "- Mandibles   : Spd 6 -> 3 AP | HP 850/850     | Posture 220/220 [RAM READY]",
        "- Carapace    : Spd 3 -> 1 AP | HP 1,100/1,100 | Posture 250/250 [ARMORED]"
    ])

    hud_t02 = make_box("TACTICAL STAGE HUD: PASSAGE 03 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — MANDIBLES SHATTERED & VOID CUT]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]            [HARIN] [DOHA]  [BOSS]   [SORA]  [YEON]  [MINJAE][JISOO] [SILENT]",
        "                                 [SCRAP]                                  ",
        "---",
        "- Node 03: Harin (Anchored / Deflecting Compressed Locomotive Exhaust)",
        "- Node 04: Doha (Tungsten Chisel Bore Cracking Carapace Segment 3)",
        "- Node 05: SECC-041 Rail Sovereign (Mandibles Destroyed 0/850 HP)",
        "- Node 06: Sora (Cascading Torrent Rusting Drive Gears)",
        "- Node 07: Yeonhwa (Sonar Fault Lock on Exposed Hydraulic Hoses)",
        "- Node 10: The Silent One (Severing Crescent Slicing Left Hydraulic Piston)",
        "---",
        "- Silent One  : Spd 9 -> 5 AP [SURGE] | HP 3,100/3,100 | SP 46/50 | Posture 120/120",
        "- Doha        : Spd 7 -> 4 AP [SURGE] | HP 3,600/3,600 | SP 42/40 | Posture 150/150",
        "- Boss Core   : Spd 4 -> 2 AP | HP 1,250/1,250 | Posture 212/280",
        "- Mandibles   : DESTROYED (0/850 HP) | HYDRAULIC PINCERS DISABLED",
        "- Carapace    : Spd 3 -> 1 AP | HP 790/1,100   | Posture 182/250"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: PASSAGE 03 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — STAGGER THRESHOLD 1 & CARAPACE BREACH]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]            [HARIN] [DOHA]  [BOSS]   [SORA]  [YEON]  [SILENT]        [JISOO] ",
        "---",
        "- Node 03: Harin (Piston Shield Blocking Carapace Flail)",
        "- Node 04: Doha (Sapper Counter-Lever Popping Heavy Carapace Segment)",
        "- Node 05: SECC-041 (STAGGER LEVEL 1 / DEFENSES REDUCED TO 0 / IMMOBILIZED)",
        "- Node 06: Sora (Chime of Discord Inflicting +3 Fragility on Guilt)",
        "- Node 07: Yeonhwa (Tracking Weakened Guilt Seams with Acoustic Dart)",
        "- Node 08: The Silent One (Preparing Execution Cleave on Core)",
        "---",
        "- Harin       : Spd 6 -> 3 AP [SURGE] | HP 4,200/4,200 | SP 48/50 | Posture 180/180",
        "- Boss Core   : Spd 0 -> 0 AP | HP 1,160/1,250 | Posture 104/280 [STAGGER LEVEL 1]",
        "- Carapace    : Spd 0 -> 0 AP | HP 480/1,100   | Posture 92/250 [BREACHED]",
        "- Total Boss  : HP 1,950/3,200 [THRESHOLD BREACHED / TAKES 1.5X DAMAGE]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: PASSAGE 03 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — MAXIMUM BURST & PHASE 2 THRESHOLD SKIP]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]                    [HARIN] [BOSS]   [DOHA]  [SILENT][YEON]  [SORA]  [JISOO] ",
        "---",
        "- Node 04: Harin (Bulwark Piston Pummel Smashing Boiler Ring)",
        "- Node 05: SECC-041 Rail Sovereign (Staggered / Pale Searchlight Exposed)",
        "- Node 06: Doha (High-Velocity Sapper Charge Blasting Track Flange)",
        "- Node 07: The Silent One (Relic Cleaver Execution Driving into Heart)",
        "- Node 08: Yeonhwa & Sora (Acoustic Void Dart & Discord Shockwave)",
        "- Node 10: Jisoo (Cryo Harpoon Securing Derailed Wheel Truck)",
        "---",
        "- Silent One  : Spd 10 -> 5 AP [BURST CRIT] | HP 3,100/3,100 | SP 50/50",
        "- Boss Core   : Spd 0 -> 0 AP | HP 310/1,250   | Posture 44/280",
        "- Carapace    : DESTROYED (0/1,100 HP)",
        "- Total Boss  : HP 790/3,200 [BURST DAMAGE 1,160! SECOND THRESHOLD SKIPPED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: PASSAGE 03 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — PHASE 2 ESCALATION & VOW OF THE LOW BULWARK]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]                    [HARIN] [BOSS]   [DOHA]  [SILENT][YEON]  [SORA]  [JISOO] ",
        "---",
        "- Node 04: Harin (Relic Overdrive: VOW OF THE LOW BULWARK MAXIMUM)",
        "- Node 05: SECC-041 (All-Stations Overdrive Screech / 40 Steam Boilers)",
        "- Node 06: Doha (Planting Hydraulic Track Jacks Under Switch)",
        "- Node 07: The Silent One (Charging Burden Cleaver Void Overdrive)",
        "- Node 09: Sora (Harmonizing 528 Hz Acoustic Repose Across Squad)",
        "---",
        "- Harin       : Spd 8 -> 4 AP [OVERDRIVE] | HP 4,200/4,200 | SP 50/50 [VOW ACTIVE]",
        "- Boss Core   : Spd 5 -> 3 AP | HP 310/1,250   | Posture 22/280 [BOILERS DRAINED]",
        "- Total Boss  : HP 310/3,200 [STEAM EXHAUSTED / WHEELS SPINNING USELESSLY]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: PASSAGE 03 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — THE FINAL DERAILMENT & STRATA 4 MONORAIL]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RIG]                            [HARIN]  [SILENT][DOHA]  [YEON]  [SORA]  [MONORAIL]",
        "                                 [REST]                           [MINJAE][JISOO]   ",
        "---",
        "- Node 05: SECC-041 Rail Sovereign (DERAILED & 100% PACIFIED)",
        "- Node 06: The Silent One (Plunges Cleaver Through Pale Searchlight)",
        "- Node 07: Harin (Pins Broken Dagger of Recon Unit Seven to Chest)",
        "- Node 08: Minjae & Jisoo (Extracting 'Clandestine Transit Seal')",
        "- Node 10: Pristine Vacuum Stasis Monorail Car (Activated & Boarded)",
        "---",
        "- Vanguard Squad: Zero Fatalities | Composure 50/50 SP (Lucid)",
        "- Encounter Status: 100% PACIFIED | Pathway to Strata 4 Aqueochon OPEN"
    ])

    return f"""### The Vanguard Squad Combat Loadout

| Specialist | Position & Range Band | Primary Armament | Active Tactical Role | M.A.W.-W Class | Current SP |
|---|---|---|---|---|---|
| **Harin** | Band 1 (Melee Front) | *The Bastion of the Low* | Kinetic Redirection, Shockwave Shield, Taunt | Heavy (Spd -1, Poise +25) | 46/50 SP |
| **Doha** | Band 1 (Melee Front) | *Calcified Pneumatic Ram* | Rail Sabotage, Armor Shatter, Part Puncture | Medium (Spd 0, Poise +20) | 38/40 SP |
| **The Silent One**| Band 1 (Melee Striker)| *Severed Relic Cleaver* | Void/Grudge Executioner, Part Amputation | Medium (Spd 0, Crit +30%) | 40/40 SP |
| **Sora** | Band 3 (Mid Support) | *Silver Slumber Cowl* | Lament Water Resonance, Harmonic SP Recovery | Light (Spd +1, SP Rec +15)| 50/50 SP |
| **Yeonhwa** | Band 4 (Ranged Command)| *The Horizon Theodolite* | Track Sensor Interception, Acoustic Tagging | Light (Spd +1, Evasion +15%)| 45/45 SP |
| **Minjae** | Band 4 (Forensic Scribe)| *Year Zero Archaeological Slate*| Transit Blueprint Logging, Historical Mapping | Light (Spd +1, Scan +20%) | 45/45 SP |
| **Jisoo** | Band 5 (Logistics Rear)| *High-Pressure Cryo Harpoon*| Ballast Accounting, Rail Winch Logistics | Light (Spd +1, Ballast 65%) | 45/45 SP |

---

### Turn-Based Combat Gauntlet: Slaying the Rail Sovereign

```text
{dossier_box}
```

---

```text
{hud_t01}
```

###### Turn 01 Action Resolution Log (Intercepting the Velocity Ram)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Harin activates `[Vow of the Low Bulwark]`: Drives shield ground spikes into the track ties; absorbs kinetic ram impacts and redirects shockwaves.
  * Yeonhwa initializes `[Sonar Track Lock]`: Intercepts the locomotive's ultrasonic guide frequencies, increasing squad clash power against the mandibles by +2.
  * Sora readies `[Lament Water Resonance]`, aiming at the overheating wheel trucks.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Harin (Speed 4 -> 2 AP, M.A.W.-W Heavy Armor delta -1, Poise +25): Holds Node 02 directly in front of the double rails. Spends 2 AP on `[Vow of the Low Bulwark: Anchor]`.
  * The Silent One (Speed 7 -> 4 AP, M.A.W.-W Medium delta 0, Crit +30\%): Perches on high catenary rafters at Node 07. Spends 2 AP on `[Severing Crescent Stance]`.
  * Doha (Speed 5 -> 3 AP, M.A.W.-W Medium delta 0, Poise +20): Holds Node 03. Spends 2 AP on `[Tungsten Chisel Bore]`. Holds 1 AP in Guard.
  * Sora (Speed 7 -> 4 AP, M.A.W.-W Light delta +1): Holds Node 04. Spends 2 AP on `[Cascading Torrent]`. Holds 2 AP in Reserve.
  * Yeonhwa (Speed 7 -> 4 AP, M.A.W.-W Light delta +1): Holds Node 06. Spends 2 AP on `[Sonar Track Lock]`, 2 AP on `[Acoustic Dart]`.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 02 to 05)**: SECC-041 unleashes `[Locomotive Charge]` (Base 16 + 2 Coins = 24 Power, Heavy Kinetic Ram) barreling down the tracks.
    * Harin intercepts with `[Vow of the Low Bulwark: Anchor]` (Base 19 + 2 Coins = 31 Power, Kinetic Shield).
    * **Clash Outcome**: Harin WINS THE CLASH OVERWHELMINGLY (31 vs 24)!
    * Harin drives her shield spike deep into the track ties. The kinetic shockwave ripples violently through the concourse; the Sovereign's front trucks derail!
    * Harin reflects **195 kinetic tremor damage** directly into the Armored Rail Mandibles (`[P3: Parry/Protection]`), inflicting +42 Posture Strain!
  * **Elemental Weakness Exploitation**:
    * Sora unleashes `[Cascading Torrent]` into the glowing wheel shafts and brake friction calipers:
      * Siphon of pressurized Lament water strikes red-hot steel gears (Weakness 1.5x proc!).
      * Deals **180 Lament damage**! Steam roars from the undercarriage as the molten wheel assemblies seize violently.
- **Step 4: Turn End State**:
  * Armored Rail Mandibles HP: 850 -> **655/850** | Posture: **178/220**.
  * Total Boss HP: 3,200 -> **2,825/3,200** | Posture: **238/280**.
  * Vanguard Composure: **100% (All SP > 44)**. Zero damage taken.

---

```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Part Destruction: Armored Rail Mandibles Shattered)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * The Silent One and Doha activate `Momentum Surge` (+2 Speed on Turn 02).
  * SECC-041 attempts `[Dual Pincer Guillotine]` targeting The Silent One.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * The Silent One (Speed 9 -> 5 AP [Surge]): Drops from catenary rafters at Node 07 onto the locomotive hood at Node 05. Spends 3 AP on `[Severing Crescent: Void Cleave]`.
  * Doha (Speed 7 -> 4 AP [Surge]): Steps from Node 03 to Node 04. Spends 3 AP on `[Tungsten Chisel Bore]`.
  * Harin (Speed 4 -> 2 AP): Holds Node 03, deflecting compressed locomotive steam with `[Bulwark Stance]`.
  * Yeonhwa (Speed 7 -> 4 AP): Casts `[Sonar Fault Lock]` (2 AP).
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 07 to 05)**: SECC-041 snaps with `[Dual Pincer Guillotine]` (Base 16 + 2 Coins = 24 Power, Pierce/Slash).
    * The Silent One executes `[Severing Crescent: Void Cleave]` (Base 22 + 3 Coins Heads = 37 Power, Void Slash).
    * **Clash Outcome**: The Silent One WINS THE CLASH OVERWHELMINGLY (37 vs 24)!
    * The dark relic cleaver slices cleanly through the left hydraulic mandible!
    * Deals **380 Critical Void damage** (Fatal 2.0x proc!) and wipes out the part's remaining health!
    * **TARGETED PART DESTROYED**: The Armored Rail Mandibles shatter into twisted iron teeth (**Mandible HP: 0/850**)!
    * **EFFECT**: Boss crushing pincer attacks permanently disabled; boss loses 1 Speed Slot!
  * **Sapper Flange Puncture**:
    * Doha's `[Tungsten Chisel Bore]` punches through Segment 3 of the Carapace Plating, dealing **185 Blunt damage**!
- **Step 4: Turn End State**:
  * Armored Rail Mandibles: **DESTROYED (0/850 HP)**.
  * Carapace Plating: 1,100 -> **790/1,100** | Posture: **182/250**.
  * Total Boss HP: 2,825 -> **2,260/3,200** | Posture: **174/280 [MANDIBLES DISABLED]**.
  * Vanguard Composure: Stable (> 42 SP across all members).

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (First Stagger Proc & Carapace Breach)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Sovereign thrashes its segmented body in wild fury: `[Carapace Thrash]` (Area Sweep, 2 Coins).
  * Harin gains `Momentum Surge` (+2 Speed -> Net Speed 6, 3 AP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Doha (Speed 5 -> 3 AP): Steps to Node 04. Spends 2 AP on `[Sapper Counter-Lever]`.
  * Harin (Speed 6 -> 3 AP): Holds Node 03. Spends 2 AP on `[Piston Shield Block]`.
  * Sora (Speed 7 -> 4 AP): Casts `[Chime of Discord]` (2 AP), inflicting +3 Fragility on the entity's guilt core.
  * Yeonhwa (Speed 7 -> 4 AP): Casts `[Acoustic Resonance Dart]` (2 AP).
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 04 to 05)**: SECC-041 unleashes `[Carapace Thrash]` (Base 16 + 2 Coins = 24 Power, Heavy Weight).
    * Doha clashes with `[Sapper Counter-Lever]` (Base 19 + 2 Coins = 31 Power, Heavy Lever).
    * **Clash Outcome**: Doha WINS THE CLASH (31 vs 24)!
    * Doha levers his pneumatic drill under the plating seams; the massive retaining bracket pops off with a deafening metallic screech!
    * Carapace takes **310 Blunt damage** and +64 Posture Strain!
- **Step 4: STAGGER THRESHOLD 1 TRIGGERED!**:
  * Total Boss HP drops past 70% (2,240 HP) down to **1,950/3,200 HP**; Posture crosses 60% strain line!
  * **STAGGER LEVEL 1 ACTIVE!** The locomotive engine derails onto its side. All defenses fall to zero; takes +50\% damage across all incoming attacks!
- **Step 5: Turn End State**:
  * Total Boss HP: 2,260 -> **1,950/3,200 [THRESHOLD BREACHED: Below 2,240 HP!]**.
  * Carapace Plating: 790 -> **480/1,100** | Posture: **92/250 [BREACHED]**.
  * Boss Posture: **104/280 [STAGGER LEVEL 1]**.
  * Vanguard Status: Unbroken.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Maximum Burst & Phase 2 Threshold Skip)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * SECC-041 remains completely immobilized on its side; searchlight core exposed and blinking erratically.
  * All Vanguard members coordinate an all-out offensive barrage targeting the exposed Traitor's Lantern Core.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * The Silent One (Speed 10 -> 5 AP, Momentum Crit): Stands at Node 07. Spends 3 AP on `[Relic Cleaver Execution]`.
  * Harin (Speed 4 -> 2 AP): Steps to Node 04. Spends 2 AP on `[Bulwark Piston Pummel]`.
  * Doha (Speed 5 -> 3 AP): Moves to Node 06. Spends 3 AP on `[High-Velocity Sapper Charge]`.
  * Yeonhwa (Speed 7 -> 4 AP): Stands at Node 08. Spends 2 AP on `[Acoustic Core Penetration]`.
  * Jisoo (Speed 7 -> 4 AP): Fires `[Cryo Harpoon Anchor]` from Node 10 (2 AP).
- **Step 3: Unopposed Stagger Punishment Rotation**:
  * The Silent One's `[Relic Cleaver Execution]`: Slices through the lantern housing for **490 Void damage** (Fatal 2.0x proc!)!
  * Harin's `[Bulwark Piston Pummel]`: Smashes the boiler ring for **210 Weight damage**!
  * Doha's `[High-Velocity Sapper Charge]`: Detonates on the track flange for **280 Explosive Grudge damage**!
  * Yeonhwa's `[Acoustic Core Penetration]`: Rips through resonance channels for **180 Void damage**!
  * **TOTAL BURST DAMAGE: 1,160 DAMAGE!**
- **Step 4: SECOND STAGGER THRESHOLD (1,280 HP) COMPLETELY SKIPPED!**:
  * Boss HP plunges from 1,950 down to **790/3,200 HP**! Carapace Plating completely destroyed (0/1,100 HP)!
  * **Phase 2 Emergency Activation Triggered!**
- **Step 5: Turn End State**:
  * Total Boss HP: 1,950 -> **790/3,200** (Core HP: **310/1,250** | Carapace: **DESTROYED**).
  * Posture: **44/280**.

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Phase 2 Escalation: Betrayal Overload & Vow of the Low Bulwark)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Sovereign recovers, steam erupting violently from all 40 boiler valves!
  * Speed Dice unlocks 4th slot! The searchlight core blinds the concourse with agonizing pale glare:
    `[All-Stations Overdrive Screech]` (AoE Hazard, 3 Coins).
  * Harin activates Relic Overdrive: `[VOW OF THE LOW BULWARK — MAXIMUM]` (Cost: 3 AP, 30 SP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Harin (Speed 8 -> 4 AP [Overdrive]): Stands alone in the center of the double rails at Node 04, locking her shield with both hands.
  * Doha (Speed 5 -> 3 AP): Plants hydraulic track jacks under the switch rails at Node 06.
  * The Silent One (Speed 7 -> 4 AP): Prepares `[Burden Cleaver: Void Overdrive Execution]` at Node 07.
  * Sora (Speed 7 -> 4 AP): Harmonizes 528 Hz acoustic repose across the squad, stabilizing all SP at 50/50.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 04 to 05)**: SECC-041 unleashes `[All-Stations Overdrive Screech]` (Base 20 + 3 Coins = 30 Power, Area Pale/Sonic).
    * Harin clashes with `[VOW OF THE LOW BULWARK — MAXIMUM]` (Base 26 + 3 Coins Heads = 44 Power, Supreme Kinetic Shield).
    * **Clash Outcome**: HARIN OVERWHELMING RELIC CLASH WIN (44 vs 30)!
    * The blinding searchlight and sonic scream smash against the steel plate; brilliant showers of sparks erupt over the concourse (`[P3: Parry/Protection]`).
    * Harin absorbs 100% of the shockwave! Zero squad damage taken!
    * Harin roars into the steam: *"RECON UNIT SEVEN! YOUR SHIFT IS FINISHED!"*
- **Step 4: Turn End State**:
  * The Sovereign is completely drained of steam; traction wheels spin uselessly against the rails.
  * Total Boss HP: **790 -> 310/3,200** | Posture: **22/280 [CRITICAL COLLAPSE]**.
  * Vanguard Composure: 50/50 SP across all members.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (The Final Derailment & Strata 4 Monorail)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Sovereign lies helpless, boiler pressure zero. Posture reaches **0/280 [TERMINAL DERAILMENT]**.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Harin (Speed 4 -> 2 AP): Drives the pointed base of her shield into the rail switch at Node 05, flipping the tracks and completely overturning the rear carriage.
  * The Silent One (Speed 7 -> 4 AP): Steps onto the overturned locomotive chassis at Node 06.
  * Minjae and Jisoo advance to Node 08 to log archival blueprints and prepare the monorail car.
- **Step 3: Overdrive Execution & Peaceful Pacification**:
  * The Silent One raises the Relic: `[The Burden Cleaver: Void Overdrive Execution]` (Power 45).
  * The blade plunges cleanly through the pale searchlight lens into the heart of the engine!
  * Deals **840 Critical Void damage**! SECC-041 HP is reduced to 0!
  * The screaming sirens and grinding gears fall utterly silent. The locomotive chassis cools into dark, inert iron.
- **Step 4: Operational Artifact Extraction & Strata Access**:
  * **Artifact Acquired**: `[Relic: The Clandestine Transit Seal of Year Zero]` (Heavy circular disc of forged tungsten and obsidian crystal).
  * **Harin's Vow**: Harin pins the broken dagger of Recon Unit Seven beside her squad's tags: *"They can rest now."*
  * **Descent Access**: The master rail terminal display flickers green. A pristine vacuum stasis monorail passenger car rolls forward onto the active tracks.
  * **Descent Destination**: The double tracks plunge down a steep 60-degree descent into Strata 4 (Radikkum / Aqueochon: The Drowned Metropolis, -900m to -1,500m).
  * **Casualties**: Zero Fatalities. Harin (HP 4,200/4,200), Doha (HP 3,600/3,600). Squad Composure 50/50 SP."""

def update_passage_3():
    path = "SOMNARAK-WORLD/Katabagil/Passage_3_Furtugil.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    start_str = "### The Vanguard Squad Combat Loadout"
    end_str = "## Chapter VIII: Epilogue & Acquisition"

    start_idx = content.find(start_str)
    end_idx = content.find(end_str)

    if start_idx == -1 or end_idx == -1:
        print(f"Error locating boundaries! start_idx={start_idx}, end_idx={end_idx}")
        return

    new_engagement = get_p3_engagement() + "\n\n---\n\n"
    new_content = content[:start_idx] + new_engagement + content[end_idx:]

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Updated Passage 3 successfully!")

if __name__ == "__main__":
    update_passage_3()
