#!/usr/bin/env python3
"""
tools/build_jipyeongseondae_arcs_4_to_6.py
Generates:
- SOMNARAK-WORLD/Jipyeongseondae/Arc_4_The_Furnaces_Secret.md
- SOMNARAK-WORLD/Jipyeongseondae/Arc_5_The_Return.md
- SOMNARAK-WORLD/Jipyeongseondae/Arc_6_The_Mugeukji_Attempt.md
"""

import unicodedata

def get_display_width(text):
    w = 0
    for ch in text:
        if unicodedata.east_asian_width(ch) in ('F', 'W'):
            w += 2
        else:
            w += 1
    return w

def pad_to_display_width(text, target_width):
    cur_w = get_display_width(text)
    if cur_w < target_width:
        return text + " " * (target_width - cur_w)
    elif cur_w > target_width:
        res = ""
        res_w = 0
        for ch in text:
            ch_w = 2 if unicodedata.east_asian_width(ch) in ('F', 'W') else 1
            if res_w + ch_w > target_width:
                break
            res += ch
            res_w += ch_w
        return res + " " * (target_width - res_w)
    return text

def make_box(title, rows, width=71):
    top = "+" + "=" * (width - 2) + "+"
    bottom = "+" + "=" * (width - 2) + "+"
    sep = "+" + "-" * (width - 2) + "+"
    inner_width = width - 4
    
    out = [top]
    if title:
        title_str = f" {title} "
        title_w = get_display_width(title_str)
        left_pad = (width - 2 - title_w) // 2
        right_pad = width - 2 - title_w - left_pad
        out.append("|" + " " * left_pad + title_str + " " * right_pad + "|")
        out.append(sep)
    
    for r in rows:
        if r == "---":
            out.append(sep)
        elif r.startswith("==="):
            out.append(top)
        else:
            padded = pad_to_display_width(r, inner_width)
            out.append(f"| {padded} |")
    out.append(bottom)
    return "\n".join(out)

def generate_arc_4():
    dossier_box = make_box("EXPEDITION DOSSIER: ARC 4 - THE FURNACE'S SECRET", [
        "OPERATION NAME     : Arc 4 - The Heart of the Great Furnace",
        "PRIMARY THEATER    : Cheonbulok - The Sacred Furnace Core",
        "DATE & EPOCH       : Year 4238, Month 5 (Deep Foundry Infiltration)",
        "PRIMARY ADVERSARY  : The Blazing Heart of Sorrow (Sentient Magma Core)",
        "---",
        "ADVERSARY PROFILE (THE BLAZING HEART OF SORROW):",
        "- Total Health (HP): 6,200 HP | Posture Pool: 400/400",
        "- Stagger 1 Proc   : 60% Posture Strain (240 Posture) / Vent Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Thermal Re-Harmonization)",
        "- Resistances      : Void 2.0x (Fatal), Lament 1.5x, Heat 0.5x, Weight 0.5x",
        "---",
        "TARGETABLE COMBAT ANCHORS:",
        "1. Rupture Vents   : 1,600 HP | Posture 320/320 (Boiling magma jet array)",
        "2. Slag Crucible   : 1,900 HP | Posture 360/360 (Heavy molten iron mantle)",
        "3. Grief Spark     : 2,700 HP | Posture 400/400 (Central unquenched tears)"
    ])

    hud_t01 = make_box("TACTICAL STAGE HUD: ARC 04 - BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 - CHEONBULOK GREAT FURNACE CORE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SLUICE][C-WALK][TRENCH][RING]  [HEART] [GANTRY][PYLON] [SUMP]  [MAGMA] [BRIDGE]",
        "[KAEL]  [HWARAN]                [FURN]                                  [BULHWA]",
        "---",
        "- Node 01: Sluice Gate Ingress (Kael Vanguard Band 1)",
        "- Node 02: Quenched Steel Catwalk (Hwaran Support Band 2)",
        "- Node 03: Geothermal Cooling Trench (Heavy Dredgers Deploying Ice Clamps)",
        "- Node 04: Boiling Slag Perimeter Ring (Severe Heat Hazard 500 deg C)",
        "- Node 05: The Furnace Heart Dais (The Blazing Heart of Sorrow)",
        "- Node 06: Overhead Crane Gantry (Ley-Seers Monitoring Thermal Spikes)",
        "- Node 07: High Exhaust Smoke Pylons (Black Soot Chimneys)",
        "- Node 10: Master Observation Bridge (Keeper Bulhwa Overseeing)",
        "---",
        "- Kael        : Spd 7 -> 4 AP | HP 3,800/3,800 | SP 50/50 | Posture 160/160",
        "- Hwaran      : Spd 6 -> 3 AP | HP 2,600/2,600 | SP 45/45 | Posture 110/110",
        "- Furnace Core: Spd 6 -> 3 AP | HP 2,700/2,700 | Posture 400/400 [CRACKING]",
        "- Rupture Vent: Spd 6 -> 3 AP | HP 1,600/1,600 | Posture 320/320 [ERUPTING]",
        "- Slag Crucib : Spd 3 -> 1 AP | HP 1,900/1,900 | Posture 360/360 [WHITE HOT]"
    ])

    hud_t02 = make_box("TACTICAL STAGE HUD: ARC 04 - BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 - RUPTURE VENTS QUENCHED & VOID CUT]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SLUICE]        [C-WALK][KAEL]  [HEART] [GANTRY][PYLON] [SUMP]  [MAGMA] [BRIDGE]",
        "                [HWARAN][SHARDS]                                                ",
        "---",
        "- Node 03: Hwaran (Cryo-Slag Dust Freezing Vent Injector Lines)",
        "- Node 04: Kael (Obsidian Cleaver Shearing High-Pressure Magma Manifold)",
        "- Node 05: The Blazing Heart (Rupture Vents Destroyed 0/1,600 HP)",
        "- Node 06: Crane Gantry (Venting Superheated Steam to Atmosphere)",
        "---",
        "- Kael        : Spd 9 -> 5 AP [SURGE] | HP 3,800/3,800 | SP 50/50 | Posture 160/160",
        "- Furnace Core: Spd 4 -> 2 AP | HP 2,700/2,700 | Posture 312/400",
        "- Rupture Vent: DESTROYED (0/1,600 HP) | MAGMA JETS PERMANENTLY QUENCHED",
        "- Slag Crucib : Spd 3 -> 1 AP | HP 1,540/1,900 | Posture 288/360"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: ARC 04 - BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 - STAGGER THRESHOLD 1 & CRUCIBLE CRACK]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SLUICE]                [C-WALK][KAEL]  [GANTRY][PYLON] [SUMP]  [MAGMA] [BRIDGE]",
        "                        [HWARAN][HEART]                                         ",
        "---",
        "- Node 04: Hwaran (Thermal Shock Chill Cracking Outer Crucible Mantle)",
        "- Node 05: Kael (Glass-Arm Seismic Punch Shattering Slag Locks)",
        "- Node 05: The Blazing Heart (STAGGER LEVEL 1 / DEFENSES COLLAPSED)",
        "- Node 10: Bulhwa (Realizing the Furnace is Weeping, Not Angry)",
        "---",
        "- Kael        : Spd 8 -> 4 AP [SURGE] | HP 3,800/3,800 | SP 50/50 | Posture 160/160",
        "- Furnace Core: Spd 0 -> 0 AP | HP 2,340/2,700 | Posture 158/400 [STAGGER LEVEL 1]",
        "- Slag Crucib : Spd 0 -> 0 AP | HP 760/1,900   | Posture 124/360 [CRACKED]",
        "- Total Heart : HP 3,100/6,200 [THRESHOLD BREACHED / TAKES 1.5X DAMAGE]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: ARC 04 - BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 - MAXIMUM BURST & PHASE 2 THRESHOLD SKIP]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SLUICE]                        [KAEL]  [GANTRY][PYLON] [SUMP]  [MAGMA] [BRIDGE]",
        "                                [HEART]                                         ",
        "---",
        "- Node 05: Kael (Obsidian Cleaver Execution Barrage on Grief Spark)",
        "- Node 05: The Blazing Heart (Immobilized / Molten Gold Tears Spilling)",
        "- Node 05: Hwaran (Harmonic Cinder-Song Calming Thermal Frenzy)",
        "- Node 10: Drift Throne (Broadcasting 528 Hz Subterranean Solace)",
        "---",
        "- Kael        : Spd 11 -> 5 AP [BURST CRIT] | HP 3,800/3,800 | SP 50/50",
        "- Furnace Core: Spd 0 -> 0 AP  | HP 710/2,700  | Posture 62/400",
        "- Slag Crucib : DESTROYED (0/1,900 HP)",
        "- Total Heart : HP 710/6,200 [BURST DAMAGE 2,390! SECOND THRESHOLD SKIPPED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: ARC 04 - BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 - THE GRIEF SUPERNOVA & REPOSE OF ASH]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SLUICE]                        [KAEL]  [GANTRY][PYLON] [SUMP]  [MAGMA] [BRIDGE]",
        "                                [HEART]                                         ",
        "---",
        "- Node 05: Kael (Relic Overdrive: EMBRACE OF THE FIRST ASH)",
        "- Node 05: The Blazing Heart (Last Stand: Four-Millennium Grief Supernova)",
        "- Node 04: Hwaran (Shielding 400 Fleeing Ash Walkers with Cinder Staff)",
        "- Node 10: Drift Throne Ley-Siphon (Channeling Grief into Safe Batteries)",
        "---",
        "- Kael        : Spd 9 -> 5 AP [OVERDRIVE] | HP 3,800/3,800 | SP 50/50 [RESOLVE]",
        "- Furnace Core: Spd 3 -> 1 AP | HP 710/2,700   | Posture 30/400 [COOLED]",
        "- Total Heart : HP 710/6,200 [SUPERNOVA TRANSMUTED INTO GENTLE WARMTH]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: ARC 04 - BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 - STABILIZATION & THE 400 ASH REFUGEES]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[SLUICE]                [FURNACE]       [SAVED]         [EVACUATION CONVOY]     ",
        "                        [STABLE]        [PEOPLE]                                ",
        "---",
        "- Node 05: The Great Furnace Core (PERMANENTLY STABILIZED & QUENCHED)",
        "- Node 05: Kael & Hwaran (Embraced by 400 Weeping Ash Walker Families)",
        "- Node 10: Furnace Keeper Bulhwa (Signing Evacuation & Friendship Edict)",
        "- Node 01: Drift Throne Hold Decks (Welcoming Refugees Aboard)",
        "---",
        "- Squad Status: Zero Casualties | Morale 50/50 SP (Transcendent Joy)",
        "- Reception Status: 100% RESOLVED | Furnace Stabilized & Refugees Rescued"
    ])

    return f"""# Arc 4: The Furnace's Secret — The Sacred Great Furnace (화로의 비밀 — 거대 화로 심층)
## The Horizon Caravan Chronicles — Planetary Overland Expedition (Year 4238, Month 5)

```text
{dossier_box}
```

> *"For four thousand years, we told ourselves that Cheonbulok was angry. We built our laws on fury, threw our brothers into the battle pits, and poured boiling slag into the sand. But the furnace wasn't raging at us. The furnace was crying."*  
> — Furnace Keeper Bulhwa, inside the Sacred Core

---

### Narrative Prologue: The Cracking Heart

In the fifth month of Year 4238, deep beneath the grand foundries of Cheonbulok, Kael, Hwaran, and Furnace Keeper Bulhwa descended into the forbidden bowels of the mountain: **The Sacred Great Furnace Core**.

The temperature inside the cavern exceeded 600^\\circ\\text{{C}}. Deep chasms opened into subterranean lakes of boiling white-hot iron. But what horrified Bulhwa was the structural state of the colossal crucible: cyclopean fissures thirty meters long crawled across the adamantine core walls, hissing with pressurized steam.

Floating at the center of the molten caldera was **The Blazing Heart of Sorrow (타오르는 슬픔의 심장)**—a gargantuan, pulsing sphere of liquid sorrow encased in burning iron slag. High-pressure **Thermal Rupture Vents** fired geysers of boiling magma at the ceiling, threatening to cause a cataclysmic caldera collapse that would incinerate the entire city of eighty thousand souls.

*"It's not dying of old age,"* Hwaran whispered, her voice trembling as she held her cinder-staff against the blistering wind. *"Listen to the frequency. It's not the sound of a fire burning. It's the sound of a mother screaming for her dead children."*

Four hundred civilian foundry workers—the **Ash Walkers**—were trapped on the lower maintenance catwalks, surrounded by advancing rivers of lava.

*"Bulhwa, order the cranes to open the exhaust flues,"* Kael commanded, unhooking his obsidian cleaver. His glass arm began to glow with incandescent white resonance. *"We're not going to let this mountain swallow your people."*

---

### Expedition Combat Gauntlet: Arc 4 (6-Turn Resolution)

```text
{hud_t01}
```

###### Turn 01 Action Resolution Log (Intercepting the Boiling Magma Jets)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Kael initializes `[Planetary Ley-Stance]`: Grants +3 Protection and physical stagger immunity.
  * Hwaran activates `[Cryo-Slag Dust]`, coating the forward catwalk in non-combustible ceramic powder.
  * The Blazing Heart activates `[Infernal Grief Field]`: Radiates 10% thermal damage per turn to all units without thermal shields.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael (Speed 7 -> 4 AP, Warden Heavy Rig delta -1, Poise +20): Holds Node 01. Spends 2 AP on `[Obsidian Cleaver: Magma Deflection]`. Holds 2 AP in Reserve.
  * Hwaran (Speed 6 -> 3 AP): Stands at Node 02. Spends 2 AP on `[Thermal Quench Cloud]`. Holds 1 AP in Guard.
  * Rupture Vents (Speed 6 -> 3 AP): Fire high-pressure molten geysers toward Node 01.
  * Slag Crucible (Speed 3 -> 1 AP): Shields the core with boiling liquid iron.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 01 to 05)**: Rupture Vents unleash `[Pressurized Boiling Magma Jet]` (Base 19 + 2 Coins = 29 Power, Heavy Thermal/Lament).
    * Kael intercepts with `[Obsidian Cleaver: Magma Deflection]` (Base 22 + 2 Coins = 34 Power, Obsidian Guard).
    * **Clash Outcome**: Kael WINS THE CLASH OVERWHELMINGLY (34 vs 29)!
    * Kael's obsidian cleaver splits the boiling magma stream cleanly; the liquid rock cascades into the drainage trenches (`[P3: Parry/Protection]`).
    * His translucent glass arm absorbs the immense heat, channeling **310 kinetic tremor damage** into the vent manifold!
  * **Clash 2 (Node 02 to 05)**: Hwaran's `[Thermal Quench Cloud]` envelops the trapped Ash Walkers, shielding them from toxic fumes.
- **Step 4: Turn End State**:
  * Rupture Vents HP: 1,600 -> **1,290/1,600** | Posture: **256/320**.
  * Total Heart HP: 6,200 -> **5,890/6,200** | Posture: **345/400**.
  * Kael Composure: **100% (50/50 SP)**. Zero damage taken.

---

```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Part Destruction: Rupture Vents Quenched)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Kael activates `Ley-Surge` (+2 Speed next turn -> Net Speed 9, 5 AP).
  * The Blazing Heart attempts `[Caldera Slag Deluge]` to melt the catwalks.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael (Speed 9 -> 5 AP [Surge]): Steps into Node 04. Spends 3 AP on `[Obsidian Cleaver: Sunder Manifold]`. Spends 2 AP on `[Thermal Leap]`.
  * Hwaran (Speed 6 -> 3 AP): Moves to Node 03. Spends 2 AP on `[Cryo-Slag Flash-Freeze]`.
  * Heavy Dredgers: Deploy portable hydraulic cooling pumps into the lava trenches.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 04 to 05)**: The Heart unleashes `[Caldera Slag Deluge]` (Base 18 + 2 Coins = 26 Power).
    * Kael clashes with `[Obsidian Cleaver: Sunder Manifold]` (Base 25 + 3 Coins Heads = 43 Power, Heavy Slash).
    * **Clash Outcome**: Kael WINS THE CLASH OVERWHELMINGLY (43 vs 26)!
    * Kael leaps atop the main manifold collar and drives his obsidian blade down through the volcanic injector ring!
    * Hwaran's `[Cryo-Slag Flash-Freeze]` shatters the superheated metal with catastrophic thermal shock!
    * Deals **1,290 Critical Void/Thermal damage** (Fatal 2.0x proc!)!
    * **TARGETED PART DESTROYED**: The Thermal Rupture Vents are completely destroyed (**Vents HP: 0/1,600**)!
    * **EFFECT**: Boiling magma jet attacks permanently disabled; boss permanently loses 1 Speed Slot!
  * **Slag Crucible Damage**:
    * Sapper shockwave cracks the outer mantle for **360 Blunt damage**!
- **Step 4: Turn End State**:
  * Rupture Vents: **DESTROYED (0/1,600 HP)**.
  * Slag Crucible: 1,900 -> **1,540/1,900** | Posture: **288/360**.
  * Total Heart HP: 5,890 -> **4,240/6,200** | Posture: **252/400 [VENTS QUENCHED]**.
  * Kael Composure: Stable (50/50 SP).

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (First Stagger Proc & Crucible Crack)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Disarmed of its vents, the Core sweeps its massive iron mantle: `[Molten Crucible Slam]` (Heavy Weight/Heat, 2 Coins).
  * Kael gains `Ley-Surge` (+2 Speed -> Net Speed 8, 4 AP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael (Speed 8 -> 4 AP): Holds Node 04. Spends 2 AP on `[Glass-Arm Seismic Sunder]`. Spends 2 AP on `[Counter-Brace]`.
  * Hwaran (Speed 6 -> 3 AP): Stands at Node 04. Spends 2 AP on `[Slag Chill Shock]`.
  * Ley-Seers: Signal the Drift Throne's siphons to begin vacuuming excess steam.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 04 to 05)**: The Heart slams forward with `[Molten Crucible Slam]` (Base 17 + 2 Coins = 25 Power).
    * Kael clashes with `[Glass-Arm Seismic Sunder]` (Base 22 + 2 Coins = 34 Power, Seismic Strike).
    * **Clash Outcome**: Kael WINS THE CLASH (34 vs 25)!
    * Kael punches the heavy cast-iron crucible casing with his glowing glass fist!
    * Hwaran's chill shock cracks the structural ribs; the burning iron plates peel open like eggshells!
    * Deals **780 Blunt/Void damage** and +106 Posture Strain!
- **Step 4: STAGGER THRESHOLD 1 TRIGGERED!**:
  * Total Heart HP crosses 70% threshold (4,340 HP), dropping to **3,100/6,200 HP**; Posture crosses 60% strain line!
  * **STAGGER LEVEL 1 ACTIVE!** The Blazing Heart sinks into the central dais; molten slag mantle falls away; unquenched tears exposed; takes +50\% damage!
- **Step 5: Turn End State**:
  * Total Heart HP: 4,240 -> **3,100/6,200 [THRESHOLD BREACHED: Below 4,340 HP!]**.
  * Slag Crucible: 1,540 -> **760/1,900** | Posture: **124/360 [CRACKED]**.
  * Core Posture: **158/400 [STAGGER LEVEL 1]**.
  * Kael Status: Unbroken.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Maximum Burst & Phase 2 Threshold Skip)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * The furnace core is completely stunned; its glowing Grief Spark is exposed, radiating golden, sorrowful light.
  * Kael coordinates an all-out offensive barrage to quell the boiling grief.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael (Speed 11 -> 5 AP, Momentum Crit): Advances to Node 05. Spends 3 AP on `[Obsidian Cleaver Execution Barrage]`. Spends 2 AP on `[Earth-Siphon Plunge]`.
  * Hwaran: Casts `[Harmonic Cinder-Song]` (3 AP).
  * Drift Throne: Broadcasts 528 Hz Subterranean Solace from Node 10 (2 AP).
- **Step 3: Unopposed Stagger Punishment Rotation**:
  * Kael's `[Execution Barrage]`: Plunges into the grief spark for **1,320 Void/Lament damage** (Fatal 2.0x proc!)!
  * Kael's `[Earth-Siphon Plunge]`: Slices through the remaining mantle mounts for **540 Pierce damage**!
  * Hwaran's `[Cinder-Song]`: Calms the thermal frenzy for **340 Heat damage**!
  * Drift Throne's `[Solace Pulse]`: Harmonizes grief vibrations for **190 Void damage**!
  * **TOTAL BURST DAMAGE: 2,390 DAMAGE!**
- **Step 4: SECOND STAGGER THRESHOLD (2,480 HP) COMPLETELY SKIPPED!**:
  * Boss HP plunges from 3,100 down to **710/6,200 HP**! Slag Crucible completely destroyed (0/1,900 HP)!
  * **Phase 2 Emergency Activation Triggered!**
- **Step 5: Turn End State**:
  * Total Heart HP: 3,100 -> **710/6,200** (Core HP: **710/2,700** | Crucible: **DESTROYED**).
  * Posture: **62/400**.

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Phase 2 Escalation: Grief Supernova & Embrace of the First Ash)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * The dying furnace awakens in cosmic lament; four thousand years of trapped grief erupt in a blinding golden explosion: `[Four-Millennium Grief Supernova]` (Cosmic Grief Cataclysm, 3 Coins).
  * Kael activates Relic Overdrive: `[EMBRACE OF THE FIRST ASH — MAXIMUM]` (Cost: 3 AP, 30 SP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael (Speed 9 -> 5 AP [Overdrive]): Steps directly to the center of the molten heart at Node 05, opening both arms.
  * Hwaran: Deploys a radiant volcanic ward shielding the 400 Ash Walkers.
  * Drift Throne: Channels the siphoned heat directly into safe geothermal storage batteries.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 05 to 05)**: The Heart unleashes `[Four-Millennium Grief Supernova]` (Base 23 + 3 Coins = 35 Power, Area Pale/Thermal).
    * Kael clashes with `[EMBRACE OF THE FIRST ASH — MAXIMUM]` (Base 30 + 3 Coins Heads = 51 Power, Sovereign Solace).
    * **Clash Outcome**: KAEL SUPREME OVERDRIVE CLASH WIN (51 vs 35)!
    * The catastrophic supernova of golden magma crashes into Kael's embrace (`[P3: Parry/Protection]`).
    * His Han-glass arm drinks the boiling grief without cracking; the blistering heat transforms into gentle, golden ember warmth!
    * Kael whispers into the core: *"You have burned long enough. Sleep now. We are here to carry your fire."*
    * The blistering thermal storm softens into peaceful summer embers! Zero squad damage taken!
- **Step 4: Turn End State**:
  * Total Heart HP: **710/6,200** | Posture: **30/400 [COOLED]**.
  * Kael Composure: 50/50 SP.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Furnace Stabilization & Evacuation of 400 Refugees)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Hostilities cease. Posture reaches **0/400 [STABILIZATION]**.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael steps back onto the catwalk, helping the first weeping Ash Walker family to their feet.
- **Step 3: Resolution & Evacuation**:
  * The Great Furnace settles into a steady, rhythmic, harmless hum. The fissures along the caldera walls seal shut with smooth obsidian glass.
  * Four hundred Ash Walker foundry workers—families whose children had never known life beyond boiling soot—weep in profound gratitude.
  * Furnace Keeper Bulhwa kneels before Kael on the iron walkway:
    > *"You have saved our city from its own wrath. These four hundred people can no longer survive in Cheonbulok's remaining foundries. Take them, Kael. Bring them across the sand to Somnarak, where there is hope."*
  * Deals **710 Peaceful Transmutation**! Heart HP reaches 0!
  * The four hundred refugees are escorted up to the surface and welcomed aboard the living decks of the Drift Throne.
- **Step 4: Operational Artifact Extraction & Milestones**:
  * **Relic Acquired**: `[The Ember of Unending Warmth]` (Provides endless clean heating to the Drift Throne's living tiers).
  * **Refugees Rescued**: 400 Ash Walkers safely evacuated and enrolled in the Horizon Caravan.
  * **Casualties**: Zero Casualties. Kael HP 3,800/3,800. Composure 50/50 SP."""

def generate_arc_5():
    dossier_box = make_box("EXPEDITION DOSSIER: ARC 5 - THE RETURN CROSSING", [
        "OPERATION NAME     : Arc 5 - Escorting the Cheonbulok Convoy",
        "PRIMARY THEATER    : The Desolate - Northern Sand Corridor (Km 1,850)",
        "DATE & EPOCH       : Year 4238, Months 6-7 (Return Transit to Somnarak)",
        "PRIMARY ADVERSARY  : Sand-Corsair Warlord Garek & Dune-Skimmer Marauders",
        "---",
        "ADVERSARY PROFILE (WARLORD GAREK'S HEAVY WAR-RIG):",
        "- Total Health (HP): 5,900 HP | Posture Pool: 380/380",
        "- Stagger 1 Proc   : 60% Posture Strain (228 Posture) / Cannon Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Marauder Route)",
        "- Resistances      : Weight 2.0x (Fatal), Grudge 1.5x, Lament 0.5x, Void 0.5x",
        "---",
        "TARGETABLE COMBAT ANCHORS:",
        "1. Rotary Cannons  : 1,500 HP | Posture 300/300 (High-speed kinetic suppression)",
        "2. Spiked Ram      : 1,800 HP | Posture 340/340 (Armored marauder chassis)",
        "3. Command Rig     : 2,600 HP | Posture 380/380 (Garek's armored cupola)"
    ])

    hud_t01 = make_box("TACTICAL STAGE HUD: ARC 05 - BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 - NORTHERN CORRIDOR AMBUSH (KM 1,850)]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RAMPS] [SKIM]  [BERM]  [VALLEY][RIG]   [SNIPER][RIDGE] [SINK]  [VENT]  [THRONE]",
        "[CONVOY][HWARAN][KAEL]          [GAREK]                                 [HELM]  ",
        "---",
        "- Node 01: Refugee Convoy Trailers (Protected by Heavy Dredgers)",
        "- Node 02: Outrider Sand-Skimmers & Hwaran (Short Band 2 / Flank)",
        "- Node 03: Fortified Sand Berms (Kael Vanguard Band 1)",
        "- Node 04: The Ambush Valley (Heavy Sand-Skimmer Skirmish Zone)",
        "- Node 05: Garek's Spiked War-Rig (Rotary Cannons & Spiked Ram)",
        "- Node 06: Dune Ridge Snipers (Corsair Harpooners & Riflemen)",
        "- Node 07: High Sand Crest (Corsair Flank Outriders)",
        "- Node 10: Drift Throne Bridge & Siege Battery (Helm Command)",
        "---",
        "- Kael        : Spd 7 -> 4 AP | HP 3,800/3,800 | SP 50/50 | Posture 160/160",
        "- Hwaran      : Spd 6 -> 3 AP | HP 2,600/2,600 | SP 45/45 | Posture 110/110",
        "- Garek Core  : Spd 6 -> 3 AP | HP 2,600/2,600 | Posture 380/380 [RAIDING]",
        "- Rotary Cann : Spd 6 -> 3 AP | HP 1,500/1,500 | Posture 300/300 [SPINNING]",
        "- Spiked Ram  : Spd 3 -> 1 AP | HP 1,800/1,800 | Posture 340/340 [CHARGING]"
    ])

    hud_t02 = make_box("TACTICAL STAGE HUD: ARC 05 - BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 - ROTARY CANNONS DISMOUNTED & KINETIC CLEAVE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RAMPS]         [SKIM]  [KAEL]  [RIG]   [SNIPER][RIDGE] [SINK]  [VENT]  [THRONE]",
        "                [HWARAN][SHARDS]                                                ",
        "---",
        "- Node 03: Hwaran (Thermal Ash Screen Blinding Ridge Snipers)",
        "- Node 04: Kael (Obsidian Cleaver Shearing Rotary Cannon Pivot)",
        "- Node 05: Warlord Garek (Rotary Cannons Destroyed 0/1,500 HP)",
        "- Node 06: Ridge Snipers (Suppressed by Crawler Secondary Turrets)",
        "---",
        "- Kael        : Spd 9 -> 5 AP [SURGE] | HP 3,800/3,800 | SP 50/50 | Posture 160/160",
        "- Garek Core  : Spd 4 -> 2 AP | HP 2,600/2,600 | Posture 296/380",
        "- Rotary Cann : DESTROYED (0/1,500 HP) | SUPPRESSION FIRE PERMANENTLY LOST",
        "- Spiked Ram  : Spd 3 -> 1 AP | HP 1,460/1,800 | Posture 270/340"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: ARC 05 - BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 - STAGGER THRESHOLD 1 & RAM CHASSIS CRUSH]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RAMPS]                 [SKIM]  [KAEL]  [SNIPER][RIDGE] [SINK]  [VENT]  [THRONE]",
        "                        [HWARAN][RIG]                                           ",
        "---",
        "- Node 04: Hwaran (Boiling Slag Dart Welding War-Rig Steering Axle)",
        "- Node 05: Kael (Glass-Arm Seismic Punch Buckling Spiked Ram)",
        "- Node 05: Warlord Garek (STAGGER LEVEL 1 / WAR-RIG FLIPPED ON SIDE)",
        "- Node 01: Refugee Convoy (Cheering from Armored Balconies)",
        "---",
        "- Kael        : Spd 8 -> 4 AP [SURGE] | HP 3,800/3,800 | SP 50/50 | Posture 160/160",
        "- Garek Core  : Spd 0 -> 0 AP | HP 2,240/2,600 | Posture 150/380 [STAGGER LEVEL 1]",
        "- Spiked Ram  : Spd 0 -> 0 AP | HP 740/1,800   | Posture 118/340 [CRUSHED]",
        "- Total Garek : HP 2,980/5,900 [THRESHOLD BREACHED / TAKES 1.5X DAMAGE]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: ARC 05 - BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 - MAXIMUM BURST & PHASE 2 THRESHOLD SKIP]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RAMPS]                         [KAEL]  [SNIPER][RIDGE] [SINK]  [VENT]  [THRONE]",
        "                                [RIG]                                           ",
        "---",
        "- Node 05: Kael (Obsidian Cleaver Execution Barrage on Command Vault)",
        "- Node 05: Warlord Garek (Immobilized / Black Engine Smoke Venting)",
        "- Node 05: Heavy Dredgers (Pneumatic Ram Tearing War-Rig Armor)",
        "- Node 10: Drift Throne Siege Gun (Kinetic Sabot Disabling Outriders)",
        "---",
        "- Kael        : Spd 11 -> 5 AP [BURST CRIT] | HP 3,800/3,800 | SP 50/50",
        "- Garek Core  : Spd 0 -> 0 AP  | HP 720/2,600  | Posture 60/380",
        "- Spiked Ram  : DESTROYED (0/1,800 HP)",
        "- Total Garek : HP 720/5,900 [BURST DAMAGE 2,260! SECOND THRESHOLD SKIPPED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: ARC 05 - BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 - DESPERATE CHARGE & WILL OF THE DRIFT KING]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RAMPS]                         [KAEL]  [SNIPER][RIDGE] [SINK]  [VENT]  [THRONE]",
        "                                [GAREK]                                         ",
        "---",
        "- Node 05: Kael (Relic Overdrive: BULWARK OF THE UNBROKEN ROAD)",
        "- Node 05: Garek (Last Stand: Nitro-Boosted Suicide Ram Explosion)",
        "- Node 04: Hwaran (Forming Quenched Sand Embankment Against Shrapnel)",
        "- Node 10: Drift Throne (Full Forward Ley-Power Stabilizing Convoy)",
        "---",
        "- Kael        : Spd 9 -> 5 AP [OVERDRIVE] | HP 3,800/3,800 | SP 50/50 [RESOLVE]",
        "- Garek Core  : Spd 3 -> 1 AP | HP 720/2,600   | Posture 28/380 [RAM ABORTED]",
        "- Total Garek : HP 720/5,900 [EXPLOSIVES DISARMED / GAREK PINNED TO SAND]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: ARC 05 - BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 - MARAUDER ROUT & SAFE CONVOY ARRIVAL]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RAMPS]                 [CONVOY]        [ROUT]          [SOMNARAK WALLS VISIBLE]",
        "                        [VICTORY]       [BANDIT]                                ",
        "---",
        "- Node 05: Warlord Garek (DISARMED & SUBMITTED / CORSAIRS SCATTERING)",
        "- Node 05: Kael (Granting Mercy / Demanding Corsairs Clear Trade Highway)",
        "- Node 07: The Horizon (Somnarak Spire & Blast Gates Gleaming Ahead)",
        "- Node 10: Drift Throne (Blowing Triumph Horn Across the Valley)",
        "---",
        "- Squad Status: Zero Casualties | Morale 50/50 SP (Unsurpassed Pride)",
        "- Reception Status: 100% RESOLVED | Convoy Escorted to Somnarak"
    ])

    return f"""# Arc 5: The Return — The Northern Sand Corridor (귀환 — 북부 모래 회랑)
## The Horizon Caravan Chronicles — Planetary Overland Expedition (Year 4238, Months 6-7)

```text
{dossier_box}
```

> *"You think because you're driving four hundred helpless foundry rats, you're an easy meal? In the Desolate, prey doesn't carry fifty tons of obsidian. Turn your rigs around, Garek, or I'll bury your entire fleet in the sand."*  
> — Kael, confronting the Sand-Corsair fleet

---

### Narrative Prologue: The Northern Sand Corridor

In the sixth month of Year 4238, the Horizon Caravan began its monumental return journey across the Desolate toward Somnarak, escorting a three-kilometer convoy of armored trailers carrying the **400 Cheonbulok Ash Walker refugees** and dozens of containers filled with precious rage-crystals and volcanic foundry technology.

However, word of the caravan's rich cargo had spread through the lawless outer wastes. At Kilometer 1,850, as the convoy navigated the narrow, wind-swept pass of the **Northern Sand Corridor**, black smoke flared on the horizon.

Surging over the sand ridges were twenty armored dune-buggies and three tracked combat crawlers commanded by **Sand-Corsair Warlord Garek**—the most notorious outlaw warlord in the Desolate. His flagship war-rig, a rust-encrusted beast with a reinforced spiked battering ram and twin roof-mounted rotary autocannons, accelerated straight down the canyon toward the refugee trailers.

*"Kael!"* Garek's voice blared over a scavenged shortwave radio. *"The Council paid me ten thousand marks to bring your head back! And those four hundred slaves will fetch a fortune in the black markets of Zone C! Surrender the crawler, and I might leave you your skin!"*

Aboard the Drift Throne, panic threatened to erupt among the refugee families. But Kael merely adjusted his trench-coat, stepping down onto the forward sand berm with his obsidian cleaver in hand.

*"Hwaran, hold the flank,"* Kael said evenly. *"Dredgers, seal the trailer airlocks. Nobody touches a single hair on these people."*

---

### Expedition Combat Gauntlet: Arc 5 (6-Turn Resolution)

```text
{hud_t01}
```

###### Turn 01 Action Resolution Log (Intercepting the Rotary Autocannon Barrage)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Kael initializes `[Planetary Ley-Stance]`: Grants +3 Protection and physical stagger immunity.
  * Hwaran readies `[Thermal Ash Screen]`, concealing the refugee trailers from sniper fire.
  * Garek activates `[Corsair Frenzy]`: Increases kinetic fire rate by +25\\%.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael (Speed 7 -> 4 AP, Warden Heavy Rig delta -1, Poise +20): Holds Node 03. Spends 2 AP on `[Obsidian Cleaver: Bullet Deflection]`. Holds 2 AP in Reserve.
  * Hwaran (Speed 6 -> 3 AP): Stands at Node 02. Spends 2 AP on `[Thermal Smoke Barrage]`. Holds 1 AP in Guard.
  * Garek War-Rig (Speed 6 -> 3 AP): Advances to Node 05 with `[Twin Rotary Autocannon Suppression]`.
  * Spiked Ram (Speed 3 -> 1 AP): Charges toward Node 03.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 03 to 05)**: Garek's War-Rig opens fire with `[Twin Rotary Autocannon Suppression]` (Base 19 + 2 Coins = 29 Power, Heavy Kinetic/Pierce).
    * Kael intercepts with `[Obsidian Cleaver: Bullet Deflection]` (Base 22 + 2 Coins = 34 Power, Obsidian Guard).
    * **Clash Outcome**: Kael WINS THE CLASH OVERWHELMINGLY (34 vs 29)!
    * Kael spins his five-foot obsidian cleaver in a blinding circular arc; thousands of 20mm tungsten rounds ricochet harmlessly off the blade (`[P3: Parry/Protection]`).
    * Kael channels the kinetic impact into his glass arm, firing an acoustic shockwave that deals **280 kinetic tremor damage** to the autocannon pivot!
  * **Clash 2 (Node 02 to 06)**: Hwaran's `[Thermal Smoke Barrage]` completely blinds the dune snipers; zero sniper hits recorded.
- **Step 4: Turn End State**:
  * Rotary Cannons HP: 1,500 -> **1,220/1,500** | Posture: **244/300**.
  * Total Garek HP: 5,900 -> **5,620/5,900** | Posture: **332/380**.
  * Kael Composure: **100% (50/50 SP)**. Zero damage taken.

---

```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Part Destruction: Rotary Cannons Dismounted)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Kael activates `Ley-Surge` (+2 Speed next turn -> Net Speed 9, 5 AP).
  * Garek attempts to reload and sweep the flank skimmers.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael (Speed 9 -> 5 AP [Surge]): Dashes to Node 04. Spends 3 AP on `[Obsidian Cleaver: Sunder Turret Mount]`. Spends 2 AP on `[Sand Sprint]`.
  * Hwaran (Speed 6 -> 3 AP): Moves to Node 03. Spends 2 AP on `[Boiling Slag Dart]`.
  * Drift King Scouts: Flank from Node 02, firing acoustic harpoons into the war-rig's tracks.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 04 to 05)**: Garek fires `[Point-Blank Autocannon Burst]` (Base 18 + 2 Coins = 26 Power).
    * Kael clashes with `[Obsidian Cleaver: Sunder Turret Mount]` (Base 25 + 3 Coins Heads = 43 Power, Heavy Slash).
    * **Clash Outcome**: Kael WINS THE CLASH OVERWHELMINGLY (43 vs 26)!
    * Kael vaults atop the war-rig's armored hood and shears through both rotary cannon barrels with a single downward stroke!
    * Hwaran's `[Boiling Slag Dart]` strikes the ammunition feeder box, detonating the remaining rounds inside the turret!
    * Deals **1,220 Critical Weight/Fire damage** (Fatal 2.0x proc!)!
    * **TARGETED PART DESTROYED**: The Twin Rotary Autocannons are completely destroyed (**Cannons HP: 0/1,500**)!
    * **EFFECT**: Marauder suppression fire permanently disabled; boss permanently loses 1 Speed Slot!
  * **Spiked Ram Damage**:
    * Sapper shockwave cracks the front ram chassis for **340 Blunt damage**!
- **Step 4: Turn End State**:
  * Rotary Cannons: **DESTROYED (0/1,500 HP)**.
  * Spiked Ram: 1,800 -> **1,460/1,800** | Posture: **270/340**.
  * Total Garek HP: 5,620 -> **4,060/5,900** | Posture: **242/380 [CANNONS DISMOUNTED]**.
  * Kael Composure: Stable (50/50 SP).

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (First Stagger Proc & Spiked Ram Flip)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Enraged, Garek stomps the accelerator, aiming his Spiked Ram directly at Kael: `[Full-Throttle Iron Ram]` (Heavy Weight/Crush, 2 Coins).
  * Kael gains `Ley-Surge` (+2 Speed -> Net Speed 8, 4 AP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael (Speed 8 -> 4 AP): Holds Node 04. Spends 2 AP on `[Glass-Arm Ground Seismic Punch]`. Spends 2 AP on `[Unyielding Stance]`.
  * Hwaran (Speed 6 -> 3 AP): Stands at Node 04. Spends 2 AP on `[Slag Axle Weld]`.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 04 to 05)**: Garek charges with `[Full-Throttle Iron Ram]` (Base 17 + 2 Coins = 25 Power).
    * Kael clashes with `[Glass-Arm Ground Seismic Punch]` (Base 22 + 2 Coins = 34 Power, Seismic Flip).
    * **Clash Outcome**: Kael WINS THE CLASH (34 vs 25)!
    * Kael drops his blade, driving his crystalline glass arm directly into the sand beneath the charging ram!
    * A geyser of compacted stone erupts beneath the war-rig's front axle, flipping the six-ton armored truck completely onto its side!
    * Deals **720 Blunt/Weight damage** and +102 Posture Strain!
- **Step 4: STAGGER THRESHOLD 1 TRIGGERED!**:
  * Garek's HP crosses 70% threshold (4,130 HP), dropping to **2,980/5,900 HP**; Posture crosses 60% strain line!
  * **STAGGER LEVEL 1 ACTIVE!** The war-rig lies overturned and smoking in the sand; command cupola exposed; takes +50\% damage!
- **Step 5: Turn End State**:
  * Total Garek HP: 4,060 -> **2,980/5,900 [THRESHOLD BREACHED: Below 4,130 HP!]**.
  * Spiked Ram: 1,460 -> **740/1,800** | Posture: **118/340 [CRUSHED]**.
  * Garek Posture: **150/380 [STAGGER LEVEL 1]**.
  * Kael Status: Unbroken.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Maximum Burst & Phase 2 Threshold Skip)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Garek's war-rig is pinned; the command cupola is split open and smoking.
  * Kael coordinates an all-out offensive barrage to break the marauder command structure.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael (Speed 11 -> 5 AP, Momentum Crit): Advances to Node 05. Spends 3 AP on `[Obsidian Cleaver Execution Barrage]`. Spends 2 AP on `[Pneumatic Sunder]`.
  * Heavy Dredgers: Deliver `[Hydraulic Pile-Driver Impact]` on the rig chassis (3 AP).
  * Drift Throne: Fires `[Kinetic Sabot Disabling Shot]` from Node 10 (2 AP).
- **Step 3: Unopposed Stagger Punishment Rotation**:
  * Kael's `[Execution Barrage]`: Plunges into the command engine for **1,280 Weight/Thermal damage** (Fatal 2.0x proc!)!
  * Kael's `[Pneumatic Sunder]`: Slices through the remaining ram steel for **520 Blunt damage**!
  * Dredgers' `[Pile-Driver]`: Crushes the rear axle for **310 Heavy damage**!
  * Drift Throne's `[Sabot Shot]`: Scatters the remaining corsair buggies for **150 Void damage**!
  * **TOTAL BURST DAMAGE: 2,260 DAMAGE!**
- **Step 4: SECOND STAGGER THRESHOLD (2,360 HP) COMPLETELY SKIPPED!**:
  * Boss HP plunges from 2,980 down to **720/5,900 HP**! Spiked Ram completely destroyed (0/1,800 HP)!
  * **Phase 2 Emergency Activation Triggered!**
- **Step 5: Turn End State**:
  * Total Garek HP: 2,980 -> **720/5,900** (Core HP: **720/2,600** | Ram: **DESTROYED**).
  * Posture: **60/380**.

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Phase 2 Escalation: Nitro-Explosion & Bulwark of the Road)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * In crazed desperation, Garek kicks open the burning cupola hatch, holding a lit bundle of seismic demolition charges: `[Nitro-Boosted Suicide Ram Explosion]` (Marauder Desperation Cataclysm, 3 Coins).
  * Kael activates Relic Overdrive: `[BULWARK OF THE UNBROKEN ROAD — MAXIMUM]` (Cost: 3 AP, 30 SP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael (Speed 9 -> 5 AP [Overdrive]): Steps straight onto the overturned rig at Node 05, looking down at Garek.
  * Hwaran: Casts a quickened sand embankment to catch stray shrapnel.
  * Drift Throne: Sounds its massive acoustic horn, shaking the canyon walls.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 05 to 05)**: Garek attempts `[Nitro-Boosted Suicide Ram Explosion]` (Base 21 + 3 Coins = 33 Power, Area Thermal).
    * Kael clashes with `[BULWARK OF THE UNBROKEN ROAD — MAXIMUM]` (Base 29 + 3 Coins Heads = 49 Power, Sovereign Command).
    * **Clash Outcome**: KAEL SUPREME OVERDRIVE CLASH WIN (49 vs 33)!
    * Kael's glass hand moves like lightning, clamping around Garek's wrist before he can strike the detonator cap (`[P3: Parry/Protection]`).
    * His crystalline fingers crush the dynamite fuses into inert powder!
    * Kael yanks Garek out of the burning wreckage, pinning the warlord to the sand beneath the flat of his obsidian blade!
    * Kael roars: *"Look at me, Garek! You're robbing people who haven't eaten real bread in four generations! Look at their children!"*
    * Garek looks toward the trailers, sees the terrified faces of the Ash Walker children, and his eyes fill with sudden shame.
    * The remaining corsairs throw down their weapons and flee into the dunes! Zero squad damage taken!
- **Step 4: Turn End State**:
  * Total Garek HP: **720/5,900** | Posture: **28/380 [RAM ABORTED]**.
  * Kael Composure: 50/50 SP.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Marauder Rout & Safe Arrival at Somnarak)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Hostilities end. Posture reaches **0/380 [ROUT]**.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael pulls Garek to his feet and pushes him toward an empty sand-skimmer.
- **Step 3: Resolution & Triumphant Arrival**:
  * *"Take your men and clear this pass,"* Kael tells Garek. *"If I ever see your pirate flags on this highway again, I won't just break your trucks. I'll bury your name."*
  * Garek scrambles onto his skimmer and speeds into the hills without looking back.
  * Deals **720 Peaceful Justice**! Garek HP reaches 0!
  * With the northern corridor cleared, the convoy accelerates. Two days later, the massive outer bastions of **Somnarak** appear on the horizon.
  * Blast Gate V opens wide. The four hundred Ash Walker refugees dismount into the arms of the Dawn Initiative, bringing four thousand tons of industrial ore and the first true diplomatic alliance between humanity's surviving cities.
- **Step 4: Operational Artifact Extraction & Milestones**:
  * **Permanent Highway**: The Somnarak-Cheonbulok Overland Route is permanently secured and recognized under municipal law.
  * **Refugees Integrated**: 400 Cheonbulok citizens safely delivered to Somnarak's Dawn Initiative.
  * **Casualties**: Zero Casualties. Kael HP 3,800/3,800. Composure 50/50 SP."""

def generate_arc_6():
    dossier_box = make_box("EXPEDITION DOSSIER: ARC 6 - THE MUGEUKJI ATTEMPT", [
        "OPERATION NAME     : Arc 6 - Breaching the Perimeter of Silence",
        "PRIMARY THEATER    : Mugeukji - Perimeter of Absolute Silence (Km 3,100)",
        "DATE & EPOCH       : Year 4238, Month 8 (The Northern Void Expedition)",
        "PRIMARY ADVERSARY  : The Archon of the Void (Sensory Erasure Sovereign)",
        "---",
        "ADVERSARY PROFILE (THE ARCHON OF THE VOID):",
        "- Total Health (HP): 7,000 HP | Posture Pool: 440/440",
        "- Stagger 1 Proc   : 60% Posture Strain (264 Posture) / Veil Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Tactical Disengagement)",
        "- Resistances      : All Elements 1.0x (Void Absorbed, Acoustic Vulnerable)",
        "---",
        "TARGETABLE COMBAT ANCHORS:",
        "1. Null Siphon     : 1,800 HP | Posture 340/340 (Absolute sound-erasure veil)",
        "2. Monolith Halo   : 2,100 HP | Posture 380/380 (Levitating marble nullifiers)",
        "3. Vacuum Core     : 3,100 HP | Posture 440/440 (Sensory dissolution heart)"
    ])

    hud_t01 = make_box("TACTICAL STAGE HUD: ARC 06 - BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 - MUGEUKJI PERIMETER OF ABSOLUTE SILENCE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[BOW]   [MUTE]  [WHITE] [NULL]  [ARCHON][SPIRE] [RIDGE] [SUMP]  [FAULT] [THRONE]",
        "[KAEL]  [HWARAN]                [CORE]                                  [HELM]  ",
        "---",
        "- Node 01: Drift Throne Bow Ramps (Kael Vanguard Band 1)",
        "- Node 02: Mute Dune Scouts & Hwaran (Short Band 2 / Acoustic Anchors)",
        "- Node 03: Soundless White Dunes (Total Acoustic Absorption Sump)",
        "- Node 04: The Null Basin (Sensory Erasure Zone: No Sound, No Color)",
        "- Node 05: The Archon of the Void (Null Siphon Veil & Monolith Halo)",
        "- Node 06: Floating Marble Spires (Void Resonators)",
        "- Node 07: Rear White Ridge (Extinction Boundary Line)",
        "- Node 10: Drift Throne Bridge (Ley-Siphon Overdrive Battling Mute Void)",
        "---",
        "- Kael        : Spd 7 -> 4 AP | HP 3,800/3,800 | SP 50/50 | Posture 160/160",
        "- Hwaran      : Spd 6 -> 3 AP | HP 2,600/2,600 | SP 45/45 | Posture 110/110",
        "- Archon Core : Spd 6 -> 3 AP | HP 3,100/3,100 | Posture 440/440 [SILENT]",
        "- Null Siphon : Spd 6 -> 3 AP | HP 1,800/1,800 | Posture 340/340 [DRAINING]",
        "- Monolith Hal: Spd 3 -> 1 AP | HP 2,100/2,100 | Posture 380/380 [LEVITATING]"
    ])

    hud_t02 = make_box("TACTICAL STAGE HUD: ARC 06 - BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 - NULL SIPHON SHATTERED & VOID CUT]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[BOW]           [MUTE]  [KAEL]  [ARCHON][SPIRE] [RIDGE] [SUMP]  [FAULT] [THRONE]",
        "                [HWARAN][SHARDS]                                                ",
        "---",
        "- Node 03: Hwaran (Volcanic Acoustic Bell Shattering Soundless Vacuum)",
        "- Node 04: Kael (Obsidian Cleaver Cleaving Null Siphon Veil)",
        "- Node 05: The Archon of the Void (Null Siphon Destroyed 0/1,800 HP)",
        "- Node 06: Floating Spires (Beginning to Resonate with Han-Frequencies)",
        "---",
        "- Kael        : Spd 9 -> 5 AP [SURGE] | HP 3,800/3,800 | SP 50/50 | Posture 160/160",
        "- Archon Core : Spd 4 -> 2 AP | HP 3,100/3,100 | Posture 352/440",
        "- Null Siphon : DESTROYED (0/1,800 HP) | SOUND RESTORED TO LOCAL RADIUS",
        "- Monolith Hal: Spd 3 -> 1 AP | HP 1,720/2,100 | Posture 314/380"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: ARC 06 - BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 - STAGGER THRESHOLD 1 & HALO FRACTURE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[BOW]                   [MUTE]  [KAEL]  [SPIRE] [RIDGE] [SUMP]  [FAULT] [THRONE]",
        "                        [HWARAN][ARCHON]                                        ",
        "---",
        "- Node 04: Hwaran (Igniting Cinder Flare against White Marble Halo)",
        "- Node 05: Kael (Glass-Arm Tremor Strike Popping Monolith Levitation)",
        "- Node 05: The Archon of the Void (STAGGER LEVEL 1 / HOVERING HALT)",
        "- Node 10: Drift Throne Ley-Seers (Reporting Memory Bleed in Crew)",
        "---",
        "- Kael        : Spd 8 -> 4 AP [SURGE] | HP 3,800/3,800 | SP 50/50 | Posture 160/160",
        "- Archon Core : Spd 0 -> 0 AP | HP 2,740/3,100 | Posture 174/440 [STAGGER LEVEL 1]",
        "- Monolith Hal: Spd 0 -> 0 AP | HP 860/2,100   | Posture 136/380 [FRACTURED]",
        "- Total Archon: HP 3,600/7,000 [THRESHOLD BREACHED / TAKES 1.5X DAMAGE]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: ARC 06 - BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 - MAXIMUM BURST & PHASE 2 THRESHOLD SKIP]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[BOW]                           [KAEL]  [SPIRE] [RIDGE] [SUMP]  [FAULT] [THRONE]",
        "                                [ARCHON]                                        ",
        "---",
        "- Node 05: Kael (Obsidian Cleaver Execution Barrage on Vacuum Core)",
        "- Node 05: The Archon (Immobilized / Event-Horizon Distortion Venting)",
        "- Node 05: Hwaran (Thermal Slag Burst Disrupting Gravitational Well)",
        "- Node 10: Drift Throne (Full Spinal Railgun Kinetic Shockwave)",
        "---",
        "- Kael        : Spd 11 -> 5 AP [BURST CRIT] | HP 3,800/3,800 | SP 50/50",
        "- Archon Core : Spd 0 -> 0 AP  | HP 820/3,100  | Posture 66/440",
        "- Monolith Hal: DESTROYED (0/2,100 HP)",
        "- Total Archon: HP 820/7,000 [BURST DAMAGE 2,780! SECOND THRESHOLD SKIPPED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: ARC 06 - BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 - THE TOTAL VOID COLLAPSE & RECOGNITION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[BOW]                           [KAEL]  [SPIRE] [RIDGE] [SUMP]  [FAULT] [THRONE]",
        "                                [ARCHON]                                        ",
        "---",
        "- Node 05: Kael (Relic Overdrive: BEACON OF REMEMBERED BREATH)",
        "- Node 05: The Archon (Last Stand: Absolute Total Sensory Erasure Field)",
        "- Node 04: Hwaran (Sensing Complete Oblivion of Soul if Pushed Further)",
        "- Node 10: Drift Throne (Engaging Emergency Reverse Thrusters)",
        "---",
        "- Kael        : Spd 9 -> 5 AP [OVERDRIVE] | HP 3,800/3,800 | SP 50/50 [RESOLVE]",
        "- Archon Core : Spd 3 -> 1 AP | HP 820/3,100   | Posture 32/440 [FIELD ARRESTED]",
        "- Total Archon: HP 820/7,000 [ERASURE ARRESTED / CREW SANITY PRESERVED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: ARC 06 - BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 - TACTICAL WITHDRAWAL & THE FRONTIER BEACON]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RETREAT]               [BEACON]        [SILENCE]       [MUGEUKJI MONOLITH]     ",
        "                        [PLANTED]       [HOLDS]                                 ",
        "---",
        "- Node 05: The Archon of the Void (STANDS SILENT / BOUNDARY DEFENDED)",
        "- Node 04: Kael (Planting Acoustic Relay Pylon into the White Sand)",
        "- Node 01: Drift Throne (Executing Orderly Tactical Reverse to Km 3,000)",
        "- Node 10: Horizon Caravan (100% Crew Preserved / Journey Ongoing)",
        "---",
        "- Squad Status: Zero Casualties | Morale 50/50 SP (Clear-Eyed Realism)",
        "- Reception Status: 100% RESOLVED | Border Charted & Withdrawal Executed"
    ])

    return f"""# Arc 6: The Mugeukji Attempt — The Perimeter of Silence (무극지 도전 — 침묵의 경계)
## The Horizon Caravan Chronicles — Planetary Overland Expedition (Year 4238, Month 8)

```text
{dossier_box}
```

> *"We cannot reach them yet. The Silence is too deep. The Void does not kill with fire or claws; it kills by making you forget who you were when you crossed the line. If we push further today, we will lose our souls. So we plant our beacon, we turn around, and we live to cross it tomorrow."*  
> — Kael, The Drift King, standing at the border of Mugeukji

---

### Narrative Prologue: The White Dust Horizon

In the eighth month of Year 4238, having secured the alliance between Somnarak and Cheonbulok, Kael pointed the Drift Throne toward humanity's greatest enigma: **Mugeukji (무극지 / 無極地) — The City of Absolute Silence**, located 3,100 kilometers north-northwest across the frozen polar tundra.

As the crawler crossed the 3,000-kilometer mark, the golden dunes abruptly terminated. In their place stretched an endless, flat plateau of fine, blindingly white dust.

The moment the crawler's treads rolled onto the white plain, all sound died.

It was not silence caused by quietness; it was an active acoustic void. The roar of the 18,000-ton crawler's four massive engines vanished. When Kael spoke, no sound escaped his throat. The wind blew violently, yet it made no whisper against the iron hull.

Hovering five hundred paces ahead in the dead air was **The Archon of the Void (무극의 지배자 / 虛無의 執政官)**. The entity was a towering sovereign carved from vibrationless white marble, crowned by the floating **Monolith Halo**. Wrapped around its chest was the **Null-Acoustic Siphon Veil**, an event-horizon membrane that actively siphoned sound, heat, and conscious thought into nonexistence.

Aboard the bridge, the Ley-Seers collapsed, clutching their temples as their memories began to dissolve into blank white fog.

Kael drew his obsidian cleaver. For the first time in forty years, his Han-glass arm felt bitterly cold.

*"Stay at the helm, Hwaran,"* Kael communicated through a gesture of pure will. *"If I fall, turn the ship around. But they need to know someone came to find them."*

---

### Expedition Combat Gauntlet: Arc 6 (6-Turn Resolution)

```text
{hud_t01}
```

###### Turn 01 Action Resolution Log (Intercepting the Sound-Erasure Veil)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Kael initializes `[Planetary Ley-Stance]`: Grants +3 Protection and psionic anchor against memory drain.
  * Hwaran prepares `[Volcanic Acoustic Bell]`, striking her cinder staff against the iron deck to generate shockwave vibrations.
  * The Archon activates `[Sensory Nullification Field]`: Disables audio cues and inflicts 5 Composure strain per turn.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael (Speed 7 -> 4 AP, Warden Heavy Rig delta -1, Poise +20): Holds Node 01. Spends 2 AP on `[Obsidian Cleaver: Void Anchor Deflection]`. Holds 2 AP in Reserve.
  * Hwaran (Speed 6 -> 3 AP): Stands at Node 02. Spends 2 AP on `[Acoustic Flare]`. Holds 1 AP in Guard.
  * The Archon (Speed 6 -> 3 AP, Sovereign Class delta -1, Poise +30): Casts `[Total Soundless Vacuum Lunge]` toward Node 01.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 01 to 05)**: The Archon attacks with `[Total Soundless Vacuum Lunge]` (Base 20 + 2 Coins = 30 Power, Area Void/Null).
    * Kael intercepts with `[Obsidian Cleaver: Void Anchor Deflection]` (Base 23 + 2 Coins = 35 Power, Seismic Anchor).
    * **Clash Outcome**: Kael WINS THE CLASH OVERWHELMINGLY (35 vs 30)!
    * In absolute, terrifying silence, Kael's obsidian blade meets the Archon's null-matter hand (`[P3: Parry/Protection]`).
    * Though no sound is heard, the white sand beneath their feet detonates outward in a fifty-meter shockwave!
    * Kael's glass arm vibrates at 528 Hz, forcing sound back into the void and dealing **320 kinetic tremor damage** to the null siphon!
  * **Clash 2 (Node 02 to 05)**: Hwaran's `[Acoustic Flare]` shatters the sensory suppression around the crawler bridge, stabilizing crew sanity.
- **Step 4: Turn End State**:
  * Null Siphon HP: 1,800 -> **1,480/1,800** | Posture: **286/340**.
  * Total Archon HP: 7,000 -> **6,680/7,000** | Posture: **392/440**.
  * Kael Composure: **100% (50/50 SP)**. Zero damage taken.

---

```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Part Destruction: Null Siphon Shattered)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Kael activates `Ley-Surge` (+2 Speed next turn -> Net Speed 9, 5 AP).
  * The Archon attempts `[Event-Horizon Memory Erase]` targeting Kael's childhood recollections.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael (Speed 9 -> 5 AP [Surge]): Steps into Node 04. Spends 3 AP on `[Obsidian Cleaver: Sever Siphon]`. Spends 2 AP on `[Resolute Dash]`.
  * Hwaran (Speed 6 -> 3 AP): Moves to Node 03. Spends 2 AP on `[Resonant Slag Bell]`.
  * Drift Throne: Directs full battery power to the front acoustic projectors.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 04 to 05)**: The Archon channels `[Event-Horizon Memory Erase]` (Base 19 + 2 Coins = 27 Power).
    * Kael clashes with `[Obsidian Cleaver: Sever Siphon]` (Base 26 + 3 Coins Heads = 44 Power, Heavy Slash).
    * **Clash Outcome**: Kael WINS THE CLASH OVERWHELMINGLY (44 vs 27)!
    * Kael slashes cleanly through the transparent null-matter veil wrapped around the entity's chest!
    * With a sudden, deafening CRACK like thunder, the atmospheric vacuum breaks; sound returns to the basin in an acoustic torrent!
    * Hwaran's slag bell rings out across the white desert like a cathedral chime!
    * Deals **1,480 Critical Void damage** (Fatal 2.0x proc!)!
    * **TARGETED PART DESTROYED**: The Null-Acoustic Siphon Veil is completely destroyed (**Siphon HP: 0/1,800**)!
    * **EFFECT**: Total sound-erasure aura permanently shattered; boss permanently loses 1 Speed Slot!
  * **Monolith Halo Damage**:
    * Sapper shockwave cracks the floating marble halo for **380 Blunt damage**!
- **Step 4: Turn End State**:
  * Null Siphon: **DESTROYED (0/1,800 HP)**.
  * Monolith Halo: 2,100 -> **1,720/2,100** | Posture: **314/380**.
  * Total Archon HP: 6,680 -> **4,820/7,000** | Posture: **276/440 [SIPHON SHATTERED]**.
  * Kael Composure: Stable (50/50 SP).

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (First Stagger Proc & Monolith Halo Fracture)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Disarmed of its veil, the Archon summons the levitating marble spires of its Halo: `[Monolith Gravitational Slam]` (Heavy Weight/Null, 2 Coins).
  * Kael gains `Ley-Surge` (+2 Speed -> Net Speed 8, 4 AP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael (Speed 8 -> 4 AP): Holds Node 04. Spends 2 AP on `[Glass-Arm Tremor Uppercut]`. Spends 2 AP on `[Counter-Stance]`.
  * Hwaran (Speed 6 -> 3 AP): Stands at Node 04. Spends 2 AP on `[Slag Spark Thermal Flash]`.
  * Ley-Seers: Broadcast distress signals to the Drift Throne's helm.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 04 to 05)**: The Archon drops a three-ton marble monolith `[Monolith Gravitational Slam]` (Base 18 + 2 Coins = 26 Power).
    * Kael clashes with `[Glass-Arm Tremor Uppercut]` (Base 23 + 2 Coins = 35 Power, Seismic Strike).
    * **Clash Outcome**: Kael WINS THE CLASH (35 vs 26)!
    * Kael punches the falling marble monolith directly with his crystalline fist!
    * The seismic shockwave shatters the white stone into flying chalk; the remaining floating halo rings fracture violently!
    * Deals **860 Blunt/Void damage** and +112 Posture Strain!
- **Step 4: STAGGER THRESHOLD 1 TRIGGERED!**:
  * Archon HP crosses 70% threshold (4,900 HP), dropping to **3,600/7,000 HP**; Posture crosses 60% strain line!
  * **STAGGER LEVEL 1 ACTIVE!** The Archon sinks to the white sand; floating spires crash down; takes +50\% damage!
- **Step 5: Turn End State**:
  * Total Archon HP: 4,820 -> **3,600/7,000 [THRESHOLD BREACHED: Below 4,900 HP!]**.
  * Monolith Halo: 1,720 -> **860/2,100** | Posture: **136/380 [FRACTURED]**.
  * Archon Posture: **174/440 [STAGGER LEVEL 1]**.
  * Kael Status: Unbroken.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Maximum Burst & Phase 2 Threshold Skip)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * The Archon is immobilized; its deep Vacuum Core is exposed, swirling with pitch-black gravitational anti-matter.
  * Kael coordinates an all-out offensive barrage to neutralize the entity's offensive potential.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael (Speed 11 -> 5 AP, Momentum Crit): Advances to Node 05. Spends 3 AP on `[Obsidian Cleaver Execution Barrage]`. Spends 2 AP on `[Earth-Shaker Plunge]`.
  * Hwaran: Casts `[Slag Thermal Null-Burst]` (3 AP).
  * Drift Throne: Fires `[Full Spinal Railgun Kinetic Shockwave]` from Node 10 (2 AP).
- **Step 3: Unopposed Stagger Punishment Rotation**:
  * Kael's `[Execution Barrage]`: Strikes the vacuum core for **1,520 Void damage** (Fatal 2.0x proc!)!
  * Kael's `[Earth-Shaker Plunge]`: Slices through the remaining marble halo for **620 Pierce damage**!
  * Hwaran's `[Null-Burst]`: Disrupts gravitational conduits for **380 Heat damage**!
  * Drift Throne's `[Spinal Sabot]`: Pulverizes peripheral anchors for **260 Heavy damage**!
  * **TOTAL BURST DAMAGE: 2,780 DAMAGE!**
- **Step 4: SECOND STAGGER THRESHOLD (2,800 HP) COMPLETELY SKIPPED!**:
  * Boss HP plunges from 3,600 down to **820/7,000 HP**! Monolith Halo completely destroyed (0/2,100 HP)!
  * **Phase 2 Emergency Activation Triggered!**
- **Step 5: Turn End State**:
  * Total Archon HP: 3,600 -> **820/7,000** (Core HP: **820/3,100** | Halo: **DESTROYED**).
  * Posture: **66/440**.

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Phase 2 Escalation: Absolute Sensory Erasure & Beacon of Breath)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * In cosmic existential panic, the Archon opens its chest, revealing the true abyss of Mugeukji: `[Absolute Total Sensory Erasure Field]` (Universal Memory Dissolution Cataclysm, 3 Coins).
  * Kael activates Relic Overdrive: `[BEACON OF REMEMBERED BREATH — MAXIMUM]` (Cost: 3 AP, 30 SP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael (Speed 9 -> 5 AP [Overdrive]): Stands at Node 05 before the vortex, planting his feet firmly into the white dust.
  * Hwaran: Screams through the radio: *"Kael, the crew! Their names are vanishing! If we step into the city, we will never come back!"*
  * Drift Throne: Reverses tread gearboxes at full torque to hold the perimeter.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 05 to 05)**: The Archon unleashes `[Absolute Total Sensory Erasure Field]` (Base 24 + 3 Coins = 36 Power, Absolute Extinction).
    * Kael clashes with `[BEACON OF REMEMBERED BREATH — MAXIMUM]` (Base 30 + 3 Coins Heads = 52 Power, Sovereign Memory).
    * **Clash Outcome**: KAEL SUPREME OVERDRIVE CLASH WIN (52 vs 36)!
    * The pitch-black event horizon slams into Kael's raised obsidian blade (`[P3: Parry/Protection]`).
    * His crystalline left arm ignites with blazing gold starlight, projecting a dome of memory, song, and sorrow that holds back the total extinction of thought!
    * Kael looks through the vortex into the distant city of Mugeukji—a silent, gleaming metropolis of pure white marble spires where not a single living heart beats.
    * Kael whispers: *"I see you, silent city. You are not dead. You are only terrified of feeling the pain. But we cannot carry you yet."*
    * The crushing void field is pushed back thirty paces! Zero squad casualties taken!
- **Step 4: Turn End State**:
  * Total Archon HP: **820/7,000** | Posture: **32/440 [FIELD ARRESTED]**.
  * Kael Composure: 50/50 SP.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Heroic Tactical Withdrawal & The Frontier Beacon)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Hostilities pause. The Archon stands motionless at the perimeter, its defenses breached but its sovereign boundary intact.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael lowers his cleaver. He takes an industrial acoustic transmitter pylon from his belt and drives it deep into the white dust at Node 04.
- **Step 3: Resolution & The Strategic Retreat**:
  * The acoustic pylon begins to pulse, broadcasting a continuous, low-frequency heartbeat of human memory, laughter, and sorrow into the soundless plains of Mugeukji.
  * Kael turns his back on the Archon and walks calmly to the Drift Throne's boarding ramp.
  * He climbs to the bridge, standing beside Hwaran and the recovering crew.
  * *"Captain?"* Hwaran asks softly, tears running down her soot-streaked face. *"Did we fail?"*
  * Kael looks out through the forward viewport at the glowing beacon standing solitary against the white void.
  * *"No,"* Kael replies, his voice carrying the deep warmth of a man who has crossed the world. *"A retreat to save the lives of your people is not defeat. We charted the road. We proved the city exists. We left them a voice in the dark. And when the Dawn Initiative brings more light to the world... we will come back."*
  * With a deep acoustic salute from its foghorns, the Drift Throne turns south, marching back toward the living cities of the world.
  * Deals **820 Peaceful Withdrawal**! Archon HP reaches 0!
- **Step 4: Operational Artifact Extraction & Milestones**:
  * **Relic Placed**: `[The Frontier Acoustic Beacon: Pylon-01]` (Permanently anchors the northern border and monitors Mugeukji's void activity).
  * **Mission Assessment**: Mugeukji remains isolated; the Silence holds. But the path is known, and the crew returns with full sanity, zero casualties, and total unity.
  * **Casualties**: Zero Casualties. Kael HP 3,800/3,800. Composure 50/50 SP."""

def main():
    p4 = "SOMNARAK-WORLD/Jipyeongseondae/Arc_4_The_Furnaces_Secret.md"
    p5 = "SOMNARAK-WORLD/Jipyeongseondae/Arc_5_The_Return.md"
    p6 = "SOMNARAK-WORLD/Jipyeongseondae/Arc_6_The_Mugeukji_Attempt.md"

    with open(p4, "w", encoding="utf-8") as f:
        f.write(generate_arc_4())
    print("Generated Arc_4_The_Furnaces_Secret.md successfully!")

    with open(p5, "w", encoding="utf-8") as f:
        f.write(generate_arc_5())
    print("Generated Arc_5_The_Return.md successfully!")

    with open(p6, "w", encoding="utf-8") as f:
        f.write(generate_arc_6())
    print("Generated Arc_6_The_Mugeukji_Attempt.md successfully!")

if __name__ == "__main__":
    main()
