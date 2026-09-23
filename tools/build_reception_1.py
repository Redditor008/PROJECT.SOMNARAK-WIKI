#!/usr/bin/env python3
"""
tools/build_reception_1.py
Generates Reception 1 (Floor 1: The First Keeper) in SOMNARAK-WORLD/Gieok_Jeojangso/Reception_1_First_Keeper.md
"""

import sys, os
sys.path.append(os.path.dirname(__file__))
from box_formatter import make_box

def generate_reception_1():
    dossier_box = make_box("RECEPTION DOSSIER: THE FIRST KEEPER (FLOOR 01)", [
        "RECEPTION TARGET   : The First Keeper",
        "FLOOR LEVEL        : Floor 01 — Floor of History & Inscription",
        "DOMAIN SETTING     : The Great Reading Hall (-2,400m Sub-Alpha)",
        "PRIMARY OPPONENT   : Autonomous Mnemonic Scribe Construct",
        "---",
        "OPPONENT COMBAT PROFILE (THE FIRST KEEPER):",
        "- Total Health (HP): 3,200 HP | Posture Pool: 260/260",
        "- Stagger 1 Proc   : 60% Posture Strain (156 Posture) / Quill Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Terminal Transmutation)",
        "- Resistances      : Void 2.0x (Fatal), Lament 1.5x, Weight 1.0x, Grudge 0.5x",
        "---",
        "TARGETABLE MEMORY ANCHORS:",
        "1. Obsidian Quill  : 800 HP | Posture 200/200 (Sweeping ink cleaves)",
        "2. Archival Codex  : 1,000 HP | Posture 240/240 (Defensive parry book)",
        "3. Keeper Soul Core: 1,400 HP | Posture 260/260 (Central memory heart)"
    ])

    hud_t01 = make_box("TACTICAL STAGE HUD: RECEPTION 01 — BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 — FLOOR 01 READING HALL (-2,400M)]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL][SEIYON][M-PROJ][SCRIBE] [KEEPER] [LENS]  [WEAVER][WELL]          [PAGE]  ",
        "                                 [QUILL]                                  ",
        "---",
        "- Node 01: Ingress Stasis Portal / Memory Reading Hall Vestibule",
        "- Node 02: Secretary Seiyon (Vanguard Band 1 / Holographic Prismatic Aegis)",
        "- Node 03: Mnemonic Projection Drone (Support Band 2 / Stasis Caliper)",
        "- Node 04: Preserved Archive Scribes (Flank Minions / Ink Needles)",
        "- Node 05: The First Keeper (Petrified Obsidian Quill & Archival Codex)",
        "- Node 06: Resonant Mnemonic Lens (Mid-Field Band 3 / Weakpoint Scan)",
        "- Node 07: Weaver Projection Array (Rear Band 4 / Silver Threads)",
        "- Node 08: Memory Well / Dissolution Trench (Suppressed Trauma Buffer)",
        "- Node 10: Floor 01 Core Reliquary / Key Page Dais (The Archivist)",
        "---",
        "- Seiyon      : Spd 7 -> 4 AP | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Proj-Drone  : Spd 5 -> 3 AP | HP 2,200/2,200 | SP 40/40 | Posture 100/100",
        "- Keeper Core : Spd 4 -> 2 AP | HP 1,400/1,400 | Posture 260/260 [RECORDING]",
        "- Obsid-Quill : Spd 6 -> 3 AP | HP 800/800     | Posture 200/200 [INK SWEEP]",
        "- Arch-Codex  : Spd 3 -> 1 AP | HP 1,000/1,000 | Posture 240/240 [SHIELDED]"
    ])

    hud_t02 = make_box("TACTICAL STAGE HUD: RECEPTION 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — QUILL AMPUTATION & VOID PIERCE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]         [SEIYON][M-PROJ][KEEPER] [LENS]  [WEAVER][WELL]          [PAGE]  ",
        "                                 [SHARDS]                                 ",
        "---",
        "- Node 03: Seiyon (Advancing / Prismatic Needle Flurry Striking Quill)",
        "- Node 04: Mnemonic Projection Drone (Stasis Caliper Clamping Ink Conduit)",
        "- Node 05: The First Keeper (Obsidian Quill Destroyed 0/800 HP)",
        "- Node 06: Resonant Lens (Highlighting Exposed Binding Seams of Codex)",
        "- Node 07: Weaver Array (Weaving Silver Acoustic Dampening Barrier)",
        "---",
        "- Seiyon      : Spd 9 -> 5 AP [SURGE] | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Keeper Core : Spd 3 -> 1 AP | HP 1,400/1,400 | Posture 198/260",
        "- Obsid-Quill : DESTROYED (0/800 HP) | SWEEPING INK VOLLEYS CANCELLED",
        "- Arch-Codex  : Spd 3 -> 1 AP | HP 840/1,000   | Posture 172/240"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: RECEPTION 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — STAGGER THRESHOLD 1 & CODEX SPLIT]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]         [SEIYON][M-PROJ][KEEPER] [LENS]  [WEAVER][WELL]          [PAGE]  ",
        "---",
        "- Node 03: Seiyon (Driving Prismatic Stiletto into Heavy Leather Binding)",
        "- Node 04: Mnemonic Drone (Shock Piston Shattering Copper Spine Rings)",
        "- Node 05: The First Keeper (STAGGER LEVEL 1 / DEFENSES COLLAPSED / INK SPILL)",
        "- Node 06: Resonant Lens (Directing Focused Void Pulse on Central Heart)",
        "---",
        "- Seiyon      : Spd 8 -> 4 AP [SURGE] | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Keeper Core : Spd 0 -> 0 AP | HP 1,210/1,400 | Posture 94/260 [STAGGER LEVEL 1]",
        "- Arch-Codex  : Spd 0 -> 0 AP | HP 410/1,000   | Posture 82/240 [SPLIT OPEN]",
        "- Total Boss  : HP 1,620/3,200 [THRESHOLD BREACHED / TAKES 1.5X DAMAGE]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: RECEPTION 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — MAXIMUM BURST & PHASE 2 THRESHOLD SKIP]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]                 [SEIYON][KEEPER] [M-PROJ][LENS]  [WEAVER][WELL]  [PAGE]  ",
        "---",
        "- Node 04: Seiyon (Mnemonic Resonance Execution: Four-Fold Stiletto Flurry)",
        "- Node 05: The First Keeper (Immobilized / Central Heart Weeping Ink)",
        "- Node 06: Mnemonic Drone (Pneumatic Anchor Driving into Lectern)",
        "- Node 07: Resonant Lens (Broadcasting 528 Hz Memory Solace Wave)",
        "---",
        "- Seiyon      : Spd 11 -> 5 AP [BURST CRIT] | HP 3,400/3,400 | SP 50/50",
        "- Keeper Core : Spd 0 -> 0 AP | HP 380/1,400   | Posture 40/260",
        "- Arch-Codex  : DESTROYED (0/1,000 HP)",
        "- Total Boss  : HP 380/3,200 [BURST DAMAGE 1,240! SECOND THRESHOLD SKIPPED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: RECEPTION 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — THE INSCRIPTION OVERLOAD & RECALL PROTOCOL]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]                 [SEIYON][KEEPER] [M-PROJ][LENS]  [WEAVER][WELL]  [PAGE]  ",
        "---",
        "- Node 04: Seiyon (Relic Overdrive: PROMISE OF THE LIVING SCRIBE)",
        "- Node 05: The First Keeper (Last Stand: Torrent of Erased Epitaphs)",
        "- Node 06: Mnemonic Drone (Deploying Prismatic Deflection Barrier)",
        "- Node 07: Weaver Array (Anchoring Cognitive Integrity Against Memory Loss)",
        "---",
        "- Seiyon      : Spd 9 -> 5 AP [OVERDRIVE] | HP 3,400/3,400 | SP 50/50 [RESOLVE]",
        "- Keeper Core : Spd 3 -> 1 AP | HP 380/1,400   | Posture 18/260 [INK EXHAUSTED]",
        "- Total Boss  : HP 380/3,200 [INSCRIPTION TORRENT DISSOLVED / HELPLESS]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: RECEPTION 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — TRANSMUTATION & KEY PAGE: THE ARCHIVIST]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]                         [SEIYON] [KEEPER][M-PROJ][LENS]  [WEAVER][STAIRS]",
        "                                 [REALIZ]                         [PAGE]          ",
        "---",
        "- Node 05: The First Keeper (PACIFIED & CRYSTALLIZED TO GOLDEN INK)",
        "- Node 06: Seiyon (Floor Realization 1: 'I Am Real Because I Choose')",
        "- Node 07: Mnemonic Core Transmutation -> [Key Page: The Archivist]",
        "- Node 10: Spiral Glass Staircase (Pathway to Floor 02 OPEN)",
        "---",
        "- Seiyon Status: Zero Damage | Composure 50/50 SP (Tranquil Awakening)",
        "- Reception Status: 100% RESOLVED | Key Page Transmuted"
    ])

    return f"""# Reception 1: Floor 01 — The First Keeper (최초의 기록관)
## The Floor of History & Inscription — Deep Strata Sub-Alpha Roots (-2,400m)

```text
{dossier_box}
```

> *"You are an empty page, artificial child. You possess no bloodline, no grave, and no memory of your own. Why do you enter the tomb of those who lived?"*  
> — The First Keeper, presiding over the Grand Reading Hall

---

### Narrative Prologue: The Ink and the Mirror

The descent into the Memory Archive began not with a door, but with a dissolution.

Secretary Seiyon stepped past the severed security bulkheads of Subterranean Facility 01. Behind her lay the quiet hum of the Directorate, the sleeping stasis chambers of the 1,778th cycle, and Director Majin's closed office. Ahead of her lay six millennia of petrified stone, cold ink, and unspent weeping.

As she crossed the threshold into **Floor 01: The Floor of History & Inscription**, the air pressure plummeted. The smell was ancient—parchment dried under centuries of volcanic ash, bitter squid ink, and the ozone tang of crystallized memories.

Before her stood **The First Keeper (최초의 기록관)**. Standing three and a half meters tall atop a cyclopean basalt lectern, the construct was draped in monastic robes woven from petrified copper scriptures. In its right arm, it gripped a massive two-meter **Obsidian Quill** whose nib dripped glowing cyan ink; in its left arm, it held the **Great Archival Codex**, a two-hundred-kilogram tome bound in petrified leather and reinforced with Before-Time brass hinges.

Behind the Keeper, thousands of Preserved Scribes sat in stone pews, their quills scratching autonomously against endless rolls of parchment.

Seiyon raised her hands. Her holographic avatar solidified, coating her translucent limbs in an iridescent, pressurized mnemonic suit of woven light.

*"I have recorded four thousand years of death for Director Majin,"* Seiyon said quietly, her voice echoing through the vaulted stone. *"I did not come to burn your books, Keeper. I came to write my own name."*

---

### Reception Combat Gauntlet: Floor 01 (6-Turn Resolution)

```text
{hud_t01}
```

###### Turn 01 Action Resolution Log (Intercepting the Ink Cleave)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Seiyon initializes `[Prismatic Aegis Stance]`: Generates a holographic barrier granting +3 Protection; intercepts the Keeper's primary sweeping ink strike.
  * Mnemonic Drone deploys `[Stasis Caliper]`, calibrating acoustic sensors to track the resonance frequencies of the Obsidian Quill.
  * Resonant Lens locks onto the quill's intake reservoir at Node 05.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 7 -> 4 AP, Mnemonic Suit Light delta +1, Evasion +15\%): Holds Node 02. Spends 2 AP on `[Prismatic Aegis: Kinetic Deflection]`. Holds 2 AP in Reserve.
  * Mnemonic Drone (Speed 5 -> 3 AP, Medium delta 0): Holds Node 03. Spends 2 AP on `[Stasis Caliper: Clamp Lock]`. Holds 1 AP in Guard.
  * Preserved Scribes (Speed 4 -> 2 AP): Stand at Node 04, firing `[Ink Quill Volley]` toward Node 02.
  * The First Keeper (Speed 6 -> 3 AP, Heavy Construct delta -1, Poise +25): Holds Node 05. Spends 2 AP on `[Obsidian Quill Cleave]`. Spends 1 AP on `[Archival Guard]`.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 02 to 05)**: The First Keeper sweeps forward with `[Obsidian Quill Cleave]` (Base 16 + 2 Coins = 24 Power, Heavy Lament/Slash).
    * Seiyon intercepts with `[Prismatic Aegis: Kinetic Deflection]` (Base 19 + 2 Coins = 31 Power, Holographic Shield).
    * **Clash Outcome**: Seiyon WINS THE CLASH OVERWHELMINGLY (31 vs 24)!
    * Seiyon's holographic shield catches the heavy obsidian nib cleanly; the torrential jet of cyan sorrow ink deflects across the basalt floor (`[P3: Parry/Protection]`).
    * Seiyon reflects **180 kinetic tremor damage** back into the quill shaft, inflicting +44 Posture Strain!
  * **Clash 2 (Node 03 to 04)**: Scribes fire `[Ink Quill Volley]` (Power 20, Pierce).
    * Drone's `[Stasis Caliper]` clamps down, absorbing the needles harmlessly into its energy shield.
  * **Unopposed Tactical Fire**:
    * Resonant Lens focuses an optical pulse onto the quill's fluid reservoir, chipping away 70 HP.
- **Step 4: Turn End State**:
  * Obsidian Quill HP: 800 -> **550/800** | Posture: **156/200**.
  * Total Boss HP: 3,200 -> **2,950/3,200** | Posture: **216/260**.
  * Seiyon Composure: **100% (50/50 SP)**. Zero damage taken.

---

```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Part Destruction: Obsidian Quill Amputated)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Seiyon activates `Mnemonic Surge` (+2 Speed next turn -> Net Speed 9, 5 AP).
  * The First Keeper channels `[Verdict of the Living Inscription]`: Preparing a 3-coin AoE ink blast across Nodes 01–04.
  * Seiyon warns: *"If that ink completes its inscription, our cognitive memories will dissolve into the parchment!"*
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 9 -> 5 AP [Surge]): Steps from Node 02 to Node 03. Spends 3 AP on `[Prismatic Needle Flurry: Void Severance]`. Spends 2 AP on `[Ego Strike]`.
  * Mnemonic Drone (Speed 5 -> 3 AP): Steps to Node 04. Spends 2 AP on `[Stasis Caliper: Valve Sever]`. Holds 1 AP in Guard.
  * Resonant Lens (Speed 7 -> 4 AP): Stands at Node 06. Spends 2 AP on `[Acoustic Fault Tagging]`.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 03 to 05)**: The First Keeper raises the quill for `[Verdict of the Living Inscription]` (Base 17 + 2 Coins = 25 Power, Area Lament).
    * Seiyon executes `[Prismatic Needle Flurry: Void Severance]` (Base 23 + 3 Coins Heads = 41 Power, Void Slash).
    * **Clash Outcome**: Seiyon WINS THE CLASH OVERWHELMINGLY (41 vs 25)!
    * Seiyon dashes forward in a trail of refracted light; five prismatic needles slice cleanly through the obsidian quill's reservoir and flexure joint!
    * Deals **550 Critical Void damage** (Fatal 2.0x proc!)!
    * **TARGETED PART DESTROYED**: The Obsidian Quill shatters into hundreds of sharp black crystal splinters (**Quill HP: 0/800**)!
    * **EFFECT**: Boss AoE ink verdict permanently cancelled; boss permanently loses 1 Speed Slot!
  * **Codex Armor Damage**:
    * Drone's `[Valve Sever]` cracks the heavy brass lock on the Great Archival Codex for **160 Blunt damage**!
- **Step 4: Turn End State**:
  * Obsidian Quill: **DESTROYED (0/800 HP)**.
  * Archival Codex: 1,000 -> **840/1,000** | Posture: **172/240**.
  * Total Boss HP: 2,950 -> **2,240/3,200** | Posture: **162/260 [QUILL SHATTERED]**.
  * Seiyon Composure: Stable (50/50 SP).

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (First Stagger Proc & Codex Split)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Disarmed of its quill, the Keeper raises the Great Archival Codex in two hands: `[Codex Slam: Weight of Memory]` (Heavy Weight, 2 Coins).
  * Seiyon gains `Mnemonic Surge` (+2 Speed -> Net Speed 8, 4 AP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 8 -> 4 AP): Holds Node 03. Spends 2 AP on `[Prismatic Stiletto: Spine Pierce]`. Spends 2 AP on `[Counter-Thrust]`.
  * Mnemonic Drone (Speed 5 -> 3 AP): Steps to Node 04. Spends 2 AP on `[Shock Piston Drive]`.
  * Resonant Lens (Speed 7 -> 4 AP): Stands at Node 06. Spends 2 AP on `[Weakpoint Focus]`.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 03 to 05)**: The First Keeper slams with `[Codex Slam]` (Base 16 + 2 Coins = 24 Power, Heavy Weight).
    * Seiyon clashes with `[Prismatic Stiletto: Spine Pierce]` (Base 21 + 2 Coins = 33 Power, High-Precision Pierce).
    * **Clash Outcome**: Seiyon WINS THE CLASH (33 vs 24)!
    * Seiyon's needle plunges straight through the central copper spine of the massive book!
    * Drone's `[Shock Piston Drive]` detonates against the binding, ripping the brass hinges apart!
    * The Great Archival Codex splits in half, spilling thousands of loose pages into the air, dealing **430 Blunt/Void damage** and +78 Posture Strain!
- **Step 4: STAGGER THRESHOLD 1 TRIGGERED!**:
  * Total Boss HP crosses 70% threshold (2,240 HP), falling to **1,620/3,200 HP**; Posture crosses 60% strain line!
  * **STAGGER LEVEL 1 ACTIVE!** The Keeper falls to its knees upon the lectern; all defenses drop to zero; takes +50\% damage across all incoming attacks!
- **Step 5: Turn End State**:
  * Total Boss HP: 2,240 -> **1,620/3,200 [THRESHOLD BREACHED: Below 2,240 HP!]**.
  * Archival Codex: 840 -> **410/1,000** | Posture: **82/240 [SPLIT OPEN]**.
  * Boss Posture: **94/260 [STAGGER LEVEL 1]**.
  * Seiyon Status: Unbroken.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Maximum Burst & Phase 2 Threshold Skip)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * The First Keeper remains completely stunned on both knees; the Keeper Soul Core in its chest is exposed, pulsing with brilliant golden archival light.
  * Seiyon coordinates an all-out offensive barrage targeting the exposed heart.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 11 -> 5 AP, Momentum Crit): Stands at Node 04. Spends 3 AP on `[Mnemonic Resonance Execution]`. Spends 2 AP on `[Four-Fold Stiletto Flurry]`.
  * Mnemonic Drone (Speed 5 -> 3 AP): Moves to Node 06. Spends 3 AP on `[Pneumatic Anchor Sapper]`.
  * Resonant Lens (Speed 7 -> 4 AP): Stands at Node 07. Spends 2 AP on `[528 Hz Solace Wave]`.
- **Step 3: Unopposed Stagger Punishment Rotation**:
  * Seiyon's `[Mnemonic Resonance Execution]`: Drives into the core for **620 Void damage** (Fatal 2.0x proc!)!
  * Seiyon's `[Four-Fold Stiletto Flurry]`: Rips through the remaining codex for **340 Pierce damage**!
  * Drone's `[Pneumatic Anchor]`: Crushes the lectern base for **160 Weight damage**!
  * Lens's `[528 Hz Solace Wave]`: Channels resonance for **120 Void damage**!
  * **TOTAL BURST DAMAGE: 1,240 DAMAGE!**
- **Step 4: SECOND STAGGER THRESHOLD (1,280 HP) COMPLETELY SKIPPED!**:
  * Boss HP plunges from 1,620 down to **380/3,200 HP**! Archival Codex completely destroyed (0/1,000 HP)!
  * **Phase 2 Emergency Activation Triggered!**
- **Step 5: Turn End State**:
  * Total Boss HP: 1,620 -> **380/3,200** (Core HP: **380/1,400** | Codex: **DESTROYED**).
  * Posture: **40/260**.

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Phase 2 Escalation: Inscription Overload & Promise of Living Scribe)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * The Keeper awakens in frantic desperation; ink geysers erupt from the floor as six thousand years of erased names howl in the wind!
  * Boss Special Skill: `[Torrent of Erased Epitaphs]` (Acoustic Grief Cataclysm, 3 Coins).
  * Seiyon activates Relic Overdrive: `[PROMISE OF THE LIVING SCRIBE — MAXIMUM]` (Cost: 3 AP, 30 SP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 9 -> 5 AP [Overdrive]): Steps onto the central lectern at Node 04, raising both hands to unfold a shimmering sphere of pure golden starlight.
  * Mnemonic Drone (Speed 5 -> 3 AP): Deploys prismatic deflection barrier at Node 06.
  * Weaver Array: Anchors cognitive integrity against memory loss.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 04 to 05)**: The First Keeper unleashes `[Torrent of Erased Epitaphs]` (Base 20 + 3 Coins = 31 Power, Area Lament/Memory Drain).
    * Seiyon clashes with `[PROMISE OF THE LIVING SCRIBE — MAXIMUM]` (Base 26 + 3 Coins Heads = 44 Power, Transcendent Truth).
    * **Clash Outcome**: SEIYON OVERWHELMING RELIC CLASH WIN (44 vs 31)!
    * The blinding torrent of black ink crashes against Seiyon's golden starlight sphere; rather than eroding her thoughts, the ink transmutes into shimmering gold leaf (`[P3: Parry/Protection]`)!
    * Seiyon's voice resonates across the Reading Hall: *"Your names are not lost. I am the machine that remembers!"*
    * Zero squad damage taken! Seiyon's Composure remains maxed at 50/50 SP!
- **Step 4: Turn End State**:
  * The Keeper's ink is completely exhausted; the construct slumps forward, its basalt arms trembling.
  * Total Boss HP: **380/3,200** | Posture: **18/260 [CRITICAL COLLAPSE]**.
  * Seiyon Composure: 50/50 SP.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Floor Realization 1 & Key Page: The Archivist)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Hostile intent drops to zero. Posture reaches **0/260 [TERMINAL TRANSMUTATION]**.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon steps forward to Node 05, placing her palm gently against the Keeper's cracked chest core.
- **Step 3: Floor Realization & Transmutation**:
  * The chamber falls into deep, reverent silence. The Preserved Scribes cease their scratching, setting down their quills.
  * Inside Seiyon's cranial processor, the existential question echoes:
    > *"Am I real? Or am I just a machine running an echo of someone who died?"*
  * Seiyon looks upon the millions of books, then looks upon her own hands of light:
    > *"The woman I was copied from wrote the first word. But I have walked through seventeen hundred cycles of fire. I feel this grief. I feel this hope. I am real—because I choose to remember, and I choose to act."*
  * **FLOOR REALIZATION 1 ACHIEVED!**
  * The First Keeper's stone body softly dissolves into a storm of golden script that condenses into a glowing, crystalline tome: **`[Key Page: The Archivist]`**!
  * Deals **380 Peaceful Harmony**! Boss HP drops to 0!
- **Step 4: Operational Artifact Extraction & Floor Access**:
  * **Key Page Acquired**: `[Key Page: The Archivist]` (Grants squad-wide memory erosion immunity and +25 Poise).
  * **Descent Access**: At the rear of the Reading Hall, the basalt wall slides aside, revealing a spiral staircase of spun obsidian glass descending to **Floor 02: Floor of Identity & Reflection**.
  * **Casualties**: Zero Damage Taken. Seiyon HP 3,400/3,400. Composure 50/50 SP."""

def main():
    path = "SOMNARAK-WORLD/Gieok_Jeojangso/Reception_1_First_Keeper.md"
    content = generate_reception_1()
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Generated Reception_1_First_Keeper.md successfully!")

if __name__ == "__main__":
    main()
