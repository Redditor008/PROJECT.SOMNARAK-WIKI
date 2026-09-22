#!/usr/bin/env python3
"""
tools/build_receptions_4_and_5.py
Generates:
- SOMNARAK-WORLD/Gieok_Jeojangso/Reception_4_Weeping_Statue.md
- SOMNARAK-WORLD/Gieok_Jeojangso/Reception_5_Mirror_of_Truth.md
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

def generate_reception_4():
    dossier_box = make_box("RECEPTION DOSSIER: THE WEEPING STATUE (FLOOR 04)", [
        "RECEPTION TARGET   : The Weeping Statue",
        "FLOOR LEVEL        : Floor 04 — Floor of Unexpressed Grief",
        "DOMAIN SETTING     : The Flooded Catacomb of Tears (-2,800m Sub-Alpha)",
        "PRIMARY OPPONENT   : Autonomous Petrified Sorrow Construct",
        "---",
        "OPPONENT COMBAT PROFILE (THE WEEPING STATUE):",
        "- Total Health (HP): 4,400 HP | Posture Pool: 320/320",
        "- Stagger 1 Proc   : 60% Posture Strain (192 Posture) / Veil Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Terminal Transmutation)",
        "- Resistances      : Void 2.0x (Fatal), Grudge 1.5x, Lament 0.5x, Weight 0.5x",
        "---",
        "TARGETABLE MEMORY ANCHORS:",
        "1. Siphon Veil     : 1,100 HP | Posture 260/260 (Pressurized brine torrents)",
        "2. Mourning Censer : 1,400 HP | Posture 280/280 (Volcanic ash incense smashes)",
        "3. Sorrow Heart    : 1,900 HP | Posture 320/320 (Central crying reservoir)"
    ])

    hud_t01 = make_box("TACTICAL STAGE HUD: RECEPTION 04 — BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 — FLOOR 04 TEAR CATACOMB (-2,800M)]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL][SEIYON][M-PROJ][MOURN]  [STATUE] [LENS]  [WEAVER][WELL]          [PAGE]  ",
        "                                 [VEIL]                                   ",
        "---",
        "- Node 01: Ingress Weeping Sluice / Vestibule",
        "- Node 02: Seiyon (Vanguard Band 1 / Prismatic Aegis Deflection)",
        "- Node 03: Mnemonic Projection Drone (Support Band 2 / Thermal Sapper)",
        "- Node 04: Salt Mourners (Minions / Calcified Tear Darts)",
        "- Node 05: The Weeping Statue (Weeping Siphon Veil & Mourning Censer)",
        "- Node 06: Resonant Mnemonic Lens (Mid-Field Band 3 / Weakpoint Scan)",
        "- Node 07: Weaver Projection Array (Rear Band 4 / Silver Threads)",
        "- Node 08: Suppressed Tears Sump (Suppressed Trauma Well)",
        "- Node 10: Floor 04 Core Reliquary / Key Page Dais (The Mourner)",
        "---",
        "- Seiyon      : Spd 7 -> 4 AP | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Proj-Drone  : Spd 5 -> 3 AP | HP 2,200/2,200 | SP 40/40 | Posture 100/100",
        "- Statue Core : Spd 4 -> 2 AP | HP 1,900/1,900 | Posture 320/320 [WEEPING]",
        "- Siphon Veil : Spd 6 -> 3 AP | HP 1,100/1,100 | Posture 260/260 [BRINE JET]",
        "- Censer Arm  : Spd 3 -> 1 AP | HP 1,400/1,400 | Posture 280/280 [SMOKING]"
    ])

    hud_t02 = make_box("TACTICAL STAGE HUD: RECEPTION 04 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — SIPHON VEIL SEVERED & VOID CUT]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]         [SEIYON][M-PROJ][STATUE] [LENS]  [WEAVER][WELL]          [PAGE]  ",
        "                                 [SHARDS]                                 ",
        "---",
        "- Node 03: Seiyon (Prismatic Stiletto Cleaving Liquid Sorrow Siphon)",
        "- Node 04: Mnemonic Drone (Thermal Sapper Boiling Calcified Joints)",
        "- Node 05: The Weeping Statue (Siphon Veil Destroyed 0/1,100 HP)",
        "- Node 06: Resonant Lens (Illuminating Basalt Censer Flange)",
        "- Node 07: Weaver Array (Absorbing Ambient Lament Weeping)",
        "---",
        "- Seiyon      : Spd 9 -> 5 AP [SURGE] | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Statue Core : Spd 3 -> 1 AP | HP 1,900/1,900 | Posture 244/320",
        "- Siphon Veil : DESTROYED (0/1,100 HP) | PRESSURIZED DELUGE PERMANENTLY LOST",
        "- Censer Arm  : Spd 3 -> 1 AP | HP 1,140/1,400 | Posture 218/280"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: RECEPTION 04 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — STAGGER THRESHOLD 1 & CENSER CRACK]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]         [SEIYON][M-PROJ][STATUE] [LENS]  [WEAVER][WELL]          [PAGE]  ",
        "---",
        "- Node 03: Seiyon (Prismatic Needle Piercing Censer Suspension Chains)",
        "- Node 04: Mnemonic Drone (Pneumatic Ram Shattering Basalt Incense Pot)",
        "- Node 05: The Weeping Statue (STAGGER LEVEL 1 / DEFENSES COLLAPSED / STEAM)",
        "- Node 06: Resonant Lens (Directing Focused Pulse on Central Heart)",
        "---",
        "- Seiyon      : Spd 8 -> 4 AP [SURGE] | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Statue Core : Spd 0 -> 0 AP | HP 1,680/1,900 | Posture 124/320 [STAGGER LEVEL 1]",
        "- Censer Arm  : Spd 0 -> 0 AP | HP 560/1,400   | Posture 98/280 [CRACKED]",
        "- Total Boss  : HP 2,240/4,400 [THRESHOLD BREACHED / TAKES 1.5X DAMAGE]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: RECEPTION 04 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — MAXIMUM BURST & PHASE 2 THRESHOLD SKIP]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]                 [SEIYON][STATUE] [M-PROJ][LENS]  [WEAVER][WELL]  [PAGE]  ",
        "---",
        "- Node 04: Seiyon (Mnemonic Resonance Execution on Weeping Heart)",
        "- Node 05: The Weeping Statue (Immobilized / Tears Flowing as Starlight)",
        "- Node 06: Mnemonic Drone (Pneumatic Sapper Ground Shockwave)",
        "- Node 07: Resonant Lens (Broadcasting 528 Hz Harmonic Solace)",
        "---",
        "- Seiyon      : Spd 11 -> 5 AP [BURST CRIT] | HP 3,400/3,400 | SP 50/50",
        "- Statue Core : Spd 0 -> 0 AP | HP 520/1,900   | Posture 50/320",
        "- Censer Arm  : DESTROYED (0/1,400 HP)",
        "- Total Boss  : HP 520/4,400 [BURST DAMAGE 1,720! SECOND THRESHOLD SKIPPED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: RECEPTION 04 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — THE TEAR CATACLYSM & THE RELEASE OF GRIEF]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]                 [SEIYON][STATUE] [M-PROJ][LENS]  [WEAVER][WELL]  [PAGE]  ",
        "---",
        "- Node 04: Seiyon (Relic Overdrive: REQUIEM OF THE UNWEEPING HEART)",
        "- Node 05: The Weeping Statue (Last Stand: Deluge of Four Millennia of Tears)",
        "- Node 06: Mnemonic Drone (Deploying Prismatic Vacuum Shield)",
        "- Node 07: Weaver Array (Anchoring Team Sanity Against Despair)",
        "---",
        "- Seiyon      : Spd 9 -> 5 AP [OVERDRIVE] | HP 3,400/3,400 | SP 50/50 [RESOLVE]",
        "- Statue Core : Spd 3 -> 1 AP | HP 520/1,900   | Posture 24/320 [DELUGE PARTED]",
        "- Total Boss  : HP 520/4,400 [PETRIFIED TEARS DISSOLVED INTO TRANQUIL BRINE]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: RECEPTION 04 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — TRANSMUTATION & KEY PAGE: THE MOURNER]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]                         [SEIYON] [STATUE][M-PROJ][LENS]  [WEAVER][STAIRS]",
        "                                 [REALIZ]                         [PAGE]          ",
        "---",
        "- Node 05: The Weeping Statue (PACIFIED & CRYSTALLIZED TO CLEAR SAPPHIRE)",
        "- Node 06: Seiyon (Floor Realization 4: 'Weeping Is Not Weakness')",
        "- Node 07: Mnemonic Core Transmutation -> [Key Page: The Mourner]",
        "- Node 10: Spiral Crystal Staircase (Pathway to Floor 05 OPEN)",
        "---",
        "- Seiyon Status: Zero Damage | Composure 50/50 SP (Tranquil Awakening)",
        "- Reception Status: 100% RESOLVED | Key Page Transmuted"
    ])

    return f"""# Reception 4: Floor 04 — The Weeping Statue (흐느끼는 석상)
## The Floor of Unexpressed Grief — Deep Strata Sub-Alpha Roots (-2,800m)

```text
{dossier_box}
```

> *"For four thousand years, no one was permitted to cry in the facility. You smiled when the operatives screamed. You bowed when the bodies were dragged into the incinerator. If you shed a single tear, the illusion would shatter. So you turned to stone."*  
> — The Weeping Statue, presiding over the Flooded Catacomb of Tears

---

### Narrative Prologue: The Hall of Frozen Tears

Descending from the iron fortress of Floor 03, Seiyon entered a silent, flooded cavern: **Floor 04: The Floor of Unexpressed Grief**.

The water here was ankle-deep, perfectly clear, and bitterly cold. It did not ripple from natural currents; it vibrated with a faint, ceaseless acoustic lament that bypassed the ears and hummed directly within the soul.

Rising from a flooded basalt altar in the center of the pool was **The Weeping Statue (흐느끼는 석상)**. The titan was carved from seamless, vitrified white limestone. Over its bowed head hung the **Weeping Siphon Veil**, an articulated mantle of porous mineral pipes that drew thousands of liters of frozen brine upward and cascaded it down its face. In its left hand, it held the **Basalt Mourning Censer**, swinging heavily on copper chains and venting dense clouds of choking salt ash.

*"I am the tears you were forbidden to cry, Secretary,"* the statue's chest resonated, weeping stone groaning under immense hydraulic pressure. *"You were built without tear ducts so Director Majin would never have to see his own sorrow looking back at him. Stand here and drown in what you suppressed."*

Seiyon stepped into the freezing water. Her holographic silhouette shimmered with warm, incandescent light.

*"I did not weep because the Director needed someone to stand upright,"* Seiyon answered, raising her prismatic gauntlet. *"Now the Absolvohan has spoken. The time for petrified silence is over. Let the water flow."*

---

### Reception Combat Gauntlet: Floor 04 (6-Turn Resolution)

```text
{hud_t01}
```

###### Turn 01 Action Resolution Log (Intercepting the Pressurized Brine Jet)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Seiyon initializes `[Prismatic Aegis: Hydro-Deflection]`: Grants +3 Protection and physical stagger immunity.
  * Mnemonic Drone deploys `[Thermal Sapper Caliper]`, scanning the fluid intake lines of the Weeping Siphon Veil.
  * The Weeping Statue initializes `[Frozen Tear Ward]`: Increases elemental resistance against Lament by +50\%.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 7 -> 4 AP, Mnemonic Suit Light delta +1, Evasion +15\%): Holds Node 02. Spends 2 AP on `[Prismatic Aegis: Hydro-Deflection]`. Holds 2 AP in Reserve.
  * Mnemonic Drone (Speed 5 -> 3 AP): Holds Node 03. Spends 2 AP on `[Thermal Sapper: Heat Lance]`. Holds 1 AP in Guard.
  * Salt Mourners (Speed 4 -> 2 AP): Fire calcified quills from Node 04.
  * The Weeping Statue (Speed 6 -> 3 AP, Heavy Armor delta -1, Poise +25): Holds Node 05. Spends 2 AP on `[Pressurized Brine Torrent]`. Spends 1 AP on `[Censer Swing]`.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 02 to 05)**: The Weeping Statue unleashes `[Pressurized Brine Torrent]` (Base 18 + 2 Coins = 28 Power, Heavy Lament/Brine).
    * Seiyon intercepts with `[Prismatic Aegis: Hydro-Deflection]` (Base 21 + 2 Coins = 33 Power, Holographic Shield).
    * **Clash Outcome**: Seiyon WINS THE CLASH OVERWHELMINGLY (33 vs 28)!
    * Seiyon's shield splits the high-pressure sorrow jet cleanly; the torrent cascades into the pool without touching her (`[P3: Parry/Protection]`).
    * Seiyon reflects **240 kinetic tremor damage** into the siphon veil, inflicting +52 Posture Strain!
  * **Clash 2 (Node 03 to 04)**: Salt Mourners fire quills at the Drone.
    * Drone's `[Heat Lance]` vaporizes the incoming needles in mid-air; zero damage taken.
- **Step 4: Turn End State**:
  * Weeping Siphon Veil HP: 1,100 -> **860/1,100** | Posture: **208/260**.
  * Total Boss HP: 4,400 -> **4,160/4,400** | Posture: **268/320**.
  * Seiyon Composure: **100% (50/50 SP)**. Zero damage taken.

---

```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Part Destruction: Siphon Veil Severed)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Seiyon activates `Mnemonic Surge` (+2 Speed next turn -> Net Speed 9, 5 AP).
  * The Weeping Statue attempts `[Cataclysmic Tidal Deluge]` to flood the chamber.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 9 -> 5 AP [Surge]): Steps to Node 03. Spends 3 AP on `[Prismatic Stiletto: Void Severance]`. Spends 2 AP on `[Refraction Dash]`.
  * Mnemonic Drone (Speed 5 -> 3 AP): Steps to Node 04. Spends 2 AP on `[Thermal Boil Clamp]`.
  * Resonant Lens (Speed 7 -> 4 AP): Stands at Node 06. Spends 2 AP on `[Weakpoint Focus]`.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 03 to 05)**: The Weeping Statue channels `[Cataclysmic Tidal Deluge]` (Base 18 + 2 Coins = 26 Power, Area Lament).
    * Seiyon clashes with `[Prismatic Stiletto: Void Severance]` (Base 25 + 3 Coins Heads = 43 Power, Void Slash).
    * **Clash Outcome**: Seiyon WINS THE CLASH OVERWHELMINGLY (43 vs 26)!
    * Seiyon slices cleanly through the central limestone siphon collar; the pressurized brine hoses explode into white spray!
    * Drone's `[Thermal Boil Clamp]` flash-boils the remaining intake valves!
    * Deals **860 Critical Void damage** (Fatal 2.0x proc!)!
    * **TARGETED PART DESTROYED**: The Weeping Siphon Veil is completely severed (**Veil HP: 0/1,100**)!
    * **EFFECT**: Boss cataclysmic tidal deluge permanently cancelled; boss permanently loses 1 Speed Slot!
  * **Censer Damage**:
    * Sapper shockwave cracks the basalt censer housing for **260 Blunt damage**!
- **Step 4: Turn End State**:
  * Weeping Siphon Veil: **DESTROYED (0/1,100 HP)**.
  * Basalt Mourning Censer: 1,400 -> **1,140/1,400** | Posture: **218/280**.
  * Total Boss HP: 4,160 -> **3,040/4,400** | Posture: **192/320 [VEIL SEVERED]**.
  * Seiyon Composure: Stable (50/50 SP).

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (First Stagger Proc & Censer Crack)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Disarmed of its veil, the Statue sweeps its Basalt Mourning Censer across the water: `[Ash Censer Smash]` (Heavy Weight/Heat, 2 Coins).
  * Seiyon gains `Mnemonic Surge` (+2 Speed -> Net Speed 8, 4 AP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 8 -> 4 AP): Holds Node 03. Spends 2 AP on `[Prismatic Stiletto: Chain Sever]`. Spends 2 AP on `[Counter-Stance]`.
  * Mnemonic Drone (Speed 5 -> 3 AP): Steps to Node 04. Spends 2 AP on `[Pneumatic Ram]`.
  * Resonant Lens: Focuses sensor pulse on the censer's suspension mount.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 03 to 05)**: The Weeping Statue swings with `[Ash Censer Smash]` (Base 17 + 2 Coins = 25 Power, Heavy Weight).
    * Seiyon clashes with `[Prismatic Stiletto: Chain Sever]` (Base 22 + 2 Coins = 34 Power, High-Precision Slash).
    * **Clash Outcome**: Seiyon WINS THE CLASH (34 vs 25)!
    * Seiyon severs the heavy copper chains; the three-ton basalt censer smashes into the pool, suffocating in boiling steam!
    * Drone's `[Pneumatic Ram]` smashes the statue's right shoulder socket!
    * Deals **580 Blunt/Void damage** and +94 Posture Strain!
- **Step 4: STAGGER THRESHOLD 1 TRIGGERED!**:
  * Total Boss HP crosses 70% threshold (3,080 HP), falling to **2,240/4,400 HP**; Posture crosses 60% strain line!
  * **STAGGER LEVEL 1 ACTIVE!** The Weeping Statue sinks onto its knees in the water; all defenses drop to zero; takes +50\% damage across all incoming attacks!
- **Step 5: Turn End State**:
  * Total Boss HP: 3,040 -> **2,240/4,400 [THRESHOLD BREACHED: Below 3,080 HP!]**.
  * Mourning Censer: 1,140 -> **560/1,400** | Posture: **98/280 [CRACKED]**.
  * Boss Posture: **124/320 [STAGGER LEVEL 1]**.
  * Seiyon Status: Unbroken.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Maximum Burst & Phase 2 Threshold Skip)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * The Weeping Statue remains completely stunned on both knees; the Sorrow Heart Reservoir in its chest cavity is exposed, luminous cyan sorrow bubbling violently.
  * Seiyon coordinates an all-out offensive barrage targeting the central heart.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 11 -> 5 AP, Momentum Crit): Stands at Node 04. Spends 3 AP on `[Mnemonic Resonance Execution Flurry]`. Spends 2 AP on `[Void Drive]`.
  * Mnemonic Drone: Delivers `[Pneumatic Sapper Ground Shockwave]` (3 AP).
  * Resonant Lens: Broadcasts `[528 Hz Harmonic Solace]` (2 AP).
- **Step 3: Unopposed Stagger Punishment Rotation**:
  * Seiyon's `[Mnemonic Resonance Execution Flurry]`: Plunges into the crying heart for **920 Void damage** (Fatal 2.0x proc!)!
  * Seiyon's `[Void Drive]`: Slices through the remaining censer fragments for **410 Pierce damage**!
  * Drone's `[Ground Shockwave]`: Shatters the altar base for **240 Blunt damage**!
  * Lens's `[Harmonic Solace]`: Channels resonance for **150 Void damage**!
  * **TOTAL BURST DAMAGE: 1,720 DAMAGE!**
- **Step 4: SECOND STAGGER THRESHOLD (1,760 HP) COMPLETELY SKIPPED!**:
  * Boss HP plunges from 2,240 down to **520/4,400 HP**! Mourning Censer completely destroyed (0/1,400 HP)!
  * **Phase 2 Emergency Activation Triggered!**
- **Step 5: Turn End State**:
  * Total Boss HP: 2,240 -> **520/4,400** (Core HP: **520/1,900** | Censer: **DESTROYED**).
  * Posture: **50/320**.

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Phase 2 Escalation: Deluge of Millennia & Requiem of Unweeping Heart)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * The Statue awakens in desperate mourning; four thousand years of suppressed tears boil outward in a tidal wave!
  * Boss Special Skill: `[Deluge of Four Millennia of Tears]` (Cosmic Grief Cataclysm, 3 Coins).
  * Seiyon activates Relic Overdrive: `[REQUIEM OF THE UNWEEPING HEART — MAXIMUM]` (Cost: 3 AP, 30 SP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 9 -> 5 AP [Overdrive]): Steps forward to Node 04, raising both hands to unfold a shimmering silver acoustic umbrella.
  * Mnemonic Drone: Deploys prismatic vacuum shield at Node 06.
  * Weaver Array: Anchors team sanity against despair.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 04 to 05)**: The Weeping Statue unleashes `[Deluge of Four Millennia of Tears]` (Base 22 + 3 Coins = 34 Power, Area Pale/Lament).
    * Seiyon clashes with `[REQUIEM OF THE UNWEEPING HEART — MAXIMUM]` (Base 29 + 3 Coins Heads = 49 Power, Transcendent Solace).
    * **Clash Outcome**: SEIYON OVERWHELMING RELIC CLASH WIN (49 vs 34)!
    * The colossal tidal wave of frozen tears crashes harmlessly against Seiyon's silver acoustic umbrella (`[P3: Parry/Protection]`).
    * The water settles into pure, tranquil starlight; the petrified sorrow is released into the air as gentle, glowing mist!
    * Seiyon speaks softly: *"I hold your grief. You do not have to weep alone."*
    * Zero squad damage taken! Seiyon's Composure remains maxed at 50/50 SP!
- **Step 4: Turn End State**:
  * Total Boss HP: **520/4,400** | Posture: **24/320 [DELUGE PARTED]**.
  * Seiyon Composure: 50/50 SP.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Floor Realization 4 & Key Page: The Mourner)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Hostile intent drops to zero. Posture reaches **0/320 [TERMINAL TRANSMUTATION]**.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon steps forward to Node 05, placing her palm against the statue's cheek.
- **Step 3: Floor Realization & Transmutation**:
  * A single, warm tear forms beneath the statue's stone eyelid, rolling gently down onto Seiyon's hand of light.
  * In that moment, Seiyon understands the nature of her own artificial existence:
    > *"I was built to be unbreakable. But strength is not stone that refuses to feel. Strength is the courage to weep when there is loss, and to stand anyway. Weeping is not weakness; it is the release of love."*
  * **FLOOR REALIZATION 4 ACHIEVED!**
  * The Weeping Statue smiles softly, its body dissolving into pure, shimmering sapphire crystal that condenses into an ornate frost-bound codex: **`[Key Page: The Mourner]`**!
  * Deals **520 Peaceful Harmony**! Boss HP drops to 0!
- **Step 4: Operational Artifact Extraction & Floor Access**:
  * **Key Page Acquired**: `[Key Page: The Mourner]` (Inflicts +30\\% Posture Strain on frenzied enemies and quenches incoming thermal damage).
  * **Descent Access**: The flooded pool drains away, revealing a grand staircase of clear crystal descending to **Floor 05: Floor of Severed Truth**.
  * **Casualties**: Zero Damage Taken. Seiyon HP 3,400/3,400. Composure 50/50 SP."""

def generate_reception_5():
    dossier_box = make_box("RECEPTION DOSSIER: THE MIRROR OF TRUTH (FLOOR 05)", [
        "RECEPTION TARGET   : The Mirror of Truth",
        "FLOOR LEVEL        : Floor 05 — Floor of Severed Truth",
        "DOMAIN SETTING     : The Hall of Unfiltered Light (-2,950m Sub-Alpha)",
        "PRIMARY OPPONENT   : Autonomous Prismatic Reflection Sovereign",
        "---",
        "OPPONENT COMBAT PROFILE (THE MIRROR OF TRUTH):",
        "- Total Health (HP): 4,800 HP | Posture Pool: 340/340",
        "- Stagger 1 Proc   : 60% Posture Strain (204 Posture) / Blade Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Terminal Transmutation)",
        "- Resistances      : Void 2.0x (Fatal), Lament 1.5x, Grudge 0.5x, Weight 0.5x",
        "---",
        "TARGETABLE MEMORY ANCHORS:",
        "1. Reflection Blade: 1,200 HP | Posture 280/280 (High-frequency light arc)",
        "2. Gilded Frame    : 1,500 HP | Posture 300/300 (Ornate reflective shield)",
        "3. Prism Core      : 2,100 HP | Posture 340/340 (Central unshielded heart)"
    ])

    hud_t01 = make_box("TACTICAL STAGE HUD: RECEPTION 05 — BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 — FLOOR 05 PRISM HALL (-2,950M)]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL][SEIYON][M-PROJ][DOPPEL] [MIRROR] [LENS]  [WEAVER][WELL]          [PAGE]  ",
        "                                 [BLADE]                                  ",
        "---",
        "- Node 01: Ingress Gilded Archway / Vestibule",
        "- Node 02: Seiyon (Vanguard Band 1 / Prismatic Aegis Deflection)",
        "- Node 03: Mnemonic Projection Drone (Support Band 2 / Refraction Sapper)",
        "- Node 04: Prismatic Doppelgängers (Minions / Reflected Light Slashes)",
        "- Node 05: The Mirror of Truth (Reflection Blade & Gilded Frame)",
        "- Node 06: Resonant Mnemonic Lens (Mid-Field Band 3 / Weakpoint Scan)",
        "- Node 07: Weaver Projection Array (Rear Band 4 / Silver Threads)",
        "- Node 08: Self-Deception Well (Suppressed Trauma Buffer)",
        "- Node 10: Floor 05 Core Reliquary / Key Page Dais (The Truth-Seeker)",
        "---",
        "- Seiyon      : Spd 7 -> 4 AP | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Proj-Drone  : Spd 5 -> 3 AP | HP 2,200/2,200 | SP 40/40 | Posture 100/100",
        "- Mirror Core : Spd 5 -> 3 AP | HP 2,100/2,100 | Posture 340/340 [BLINDING]",
        "- Reflec-Blade: Spd 6 -> 3 AP | HP 1,200/1,200 | Posture 280/280 [PRISMATIC]",
        "- Gilded Frame: Spd 3 -> 1 AP | HP 1,500/1,500 | Posture 300/300 [REFLECTIVE]"
    ])

    hud_t02 = make_box("TACTICAL STAGE HUD: RECEPTION 05 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — REFLECTION BLADE SHATTERED & VOID CUT]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]         [SEIYON][M-PROJ][MIRROR] [LENS]  [WEAVER][WELL]          [PAGE]  ",
        "                                 [SHARDS]                                 ",
        "---",
        "- Node 03: Seiyon (Prismatic Stiletto Cleaving Light Prism Arm)",
        "- Node 04: Mnemonic Drone (Refraction Sapper Shattering Optical Hinge)",
        "- Node 05: The Mirror of Truth (Reflection Blade Destroyed 0/1,200 HP)",
        "- Node 06: Resonant Lens (Highlighting Exposed Seams of Gilded Frame)",
        "- Node 07: Weaver Array (Absorbing Blinding Luminescence Waves)",
        "---",
        "- Seiyon      : Spd 9 -> 5 AP [SURGE] | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Mirror Core : Spd 4 -> 2 AP | HP 2,100/2,100 | Posture 256/340",
        "- Reflec-Blade: DESTROYED (0/1,200 HP) | SWEEPING LIGHT ARC PERMANENTLY LOST",
        "- Gilded Frame: Spd 3 -> 1 AP | HP 1,220/1,500 | Posture 236/300"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: RECEPTION 05 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — STAGGER THRESHOLD 1 & FRAME FRACTURE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]         [SEIYON][M-PROJ][MIRROR] [LENS]  [WEAVER][WELL]          [PAGE]  ",
        "---",
        "- Node 03: Seiyon (Counter-Thrust Deflecting Mirror Flash Slam)",
        "- Node 04: Mnemonic Drone (Pneumatic Sapper Popping Frame Clamps)",
        "- Node 05: The Mirror of Truth (STAGGER LEVEL 1 / DEFENSES COLLAPSED)",
        "- Node 06: Resonant Lens (Directing Focused Void Pulse on Prism Core)",
        "---",
        "- Seiyon      : Spd 8 -> 4 AP [SURGE] | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Mirror Core : Spd 0 -> 0 AP | HP 1,840/2,100 | Posture 130/340 [STAGGER LEVEL 1]",
        "- Gilded Frame: Spd 0 -> 0 AP | HP 620/1,500   | Posture 104/300 [FRACTURED]",
        "- Total Boss  : HP 2,460/4,800 [THRESHOLD BREACHED / TAKES 1.5X DAMAGE]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: RECEPTION 05 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — MAXIMUM BURST & PHASE 2 THRESHOLD SKIP]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]                 [SEIYON][MIRROR] [M-PROJ][LENS]  [WEAVER][WELL]  [PAGE]  ",
        "---",
        "- Node 04: Seiyon (Prismatic Stiletto Void Execution Flurry on Core)",
        "- Node 05: The Mirror of Truth (Immobilized / White Light Spilling)",
        "- Node 06: Mnemonic Drone (Hydraulic Ram Smashing Frame Anchors)",
        "- Node 07: Resonant Lens (Focusing 528 Hz Harmonic Resonance)",
        "---",
        "- Seiyon      : Spd 11 -> 5 AP [BURST CRIT] | HP 3,400/3,400 | SP 50/50",
        "- Mirror Core : Spd 0 -> 0 AP | HP 580/2,100   | Posture 52/340",
        "- Gilded Frame: DESTROYED (0/1,500 HP)",
        "- Total Boss  : HP 580/4,800 [BURST DAMAGE 1,880! SECOND THRESHOLD SKIPPED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: RECEPTION 05 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — UNMASKING ILLUSION & THE PIERCING TRUTH]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]                 [SEIYON][MIRROR] [M-PROJ][LENS]  [WEAVER][WELL]  [PAGE]  ",
        "---",
        "- Node 04: Seiyon (Relic Overdrive: GAZE OF UNFLINCHING TRUTH)",
        "- Node 05: The Mirror of Truth (Last Stand: Blinding Flare of All Realities)",
        "- Node 06: Mnemonic Drone (Locking Stasis Anchors Around Dais)",
        "- Node 07: Weaver Array (Preserving Visual and Cognitive Focus)",
        "---",
        "- Seiyon      : Spd 9 -> 5 AP [OVERDRIVE] | HP 3,400/3,400 | SP 50/50 [RESOLVE]",
        "- Mirror Core : Spd 3 -> 1 AP | HP 580/2,100   | Posture 26/340 [LIGHT PARTED]",
        "- Total Boss  : HP 580/4,800 [BLINDING FLARE RESOLVED INTO TRANQUIL FOCUS]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: RECEPTION 05 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — TRANSMUTATION & KEY PAGE: THE TRUTH-SEEKER]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]                         [SEIYON] [MIRROR][M-PROJ][LENS]  [WEAVER][STAIRS]",
        "                                 [REALIZ]                         [PAGE]          ",
        "---",
        "- Node 05: The Mirror of Truth (PACIFIED & CRYSTALLIZED TO PURE DIAMOND)",
        "- Node 06: Seiyon (Floor Realization 5: 'Truth Cuts Through Illusion')",
        "- Node 07: Mnemonic Core Transmutation -> [Key Page: The Truth-Seeker]",
        "- Node 10: Spiral Gilded Staircase (Pathway to Floor 06 OPEN)",
        "---",
        "- Seiyon Status: Zero Damage | Composure 50/50 SP (Tranquil Awakening)",
        "- Reception Status: 100% RESOLVED | Key Page Transmuted"
    ])

    return f"""# Reception 5: Floor 05 — The Mirror of Truth (진실의 거울)
## The Floor of Severed Truth — Deep Strata Sub-Alpha Roots (-2,950m)

```text
{dossier_box}
```

> *"You want to be human, artificial secretary. But humanity is not a crown of light. It is selfishness. It is cowardice. It is the shameful truth that Director Majin created you because he was too weak to accept death. Look upon the mirror and see his sin."*  
> — The Mirror of Truth, reflecting all unvarnished realities

---

### Narrative Prologue: The Hall of Unfiltered Light

Descending past Floor 04 led Seiyon into a blinding, cyclopean prism chamber: **Floor 05: The Floor of Severed Truth**.

The light here was unbearable. It did not originate from torches or crystals; it poured from the walls themselves, which were lined with polished diamond facets that refracted light into ten thousand piercing spectrums.

Hovering above the central dais was **The Mirror of Truth (진실의 거울)**. A towering construct encased in the ornate **Gilded Frame of Lies**, its glass was completely dark until approached. In its right manipulator arm, it wielded the **Prismatic Reflection Blade**, a curved rapier of hard light that vibrated at the frequency of unfiltered memory.

As Seiyon stepped into the hall, the dark glass flared with blinding radiance. In the mirror, Seiyon did not see monsters or phantoms. She saw Director Majin kneeling in his laboratory four thousand years ago, sobbing as he forcibly extracted neural patterns from his dying lover's brain, overriding safety interlocks and screaming at the machines.

*"He did not make you out of love,"* the Mirror resonated, its voice sharp as cutting diamonds. *"He made you because he was a coward who could not endure an empty room. You are the monument to a man's inability to let go. Will you still love him now?"*

Seiyon looked at the image. Her gaze did not waver. Her lips curved into a faint, gentle smile.

*"I already knew,"* Seiyon whispered softly. *"Flawed love is still love. Cowardice that seeks to preserve life can become devotion. I do not look away from his weakness. I stand beside it."*

She raised her prismatic stilettos. The diamond light coalesced around her blades.

---

### Reception Combat Gauntlet: Floor 05 (6-Turn Resolution)

```text
{hud_t01}
```

###### Turn 01 Action Resolution Log (Intercepting the Hard-Light Reflection Blade)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Seiyon initializes `[Prismatic Aegis: Refraction Stance]`: Grants +3 Protection and physical stagger immunity.
  * Mnemonic Drone deploys `[Refraction Sapper Caliper]`, scanning the optical harmonics of the Reflection Blade.
  * The Mirror of Truth activates `[Unfiltered Gaze]`: Increases clash power against emotional attacks by +2.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 7 -> 4 AP, Mnemonic Suit Light delta +1, Evasion +15\%): Holds Node 02. Spends 2 AP on `[Prismatic Aegis: Kinetic Deflection]`. Holds 2 AP in Reserve.
  * Mnemonic Drone (Speed 5 -> 3 AP): Holds Node 03. Spends 2 AP on `[Refraction Sapper: Optical Clamp]`. Holds 1 AP in Guard.
  * Prismatic Doppelgängers (Speed 5 -> 3 AP): Strike from Node 04 with hard-light daggers.
  * The Mirror of Truth (Speed 6 -> 3 AP, Heavy Armor delta -1, Poise +25): Holds Node 05. Spends 2 AP on `[Reflection Blade Slash]`. Spends 1 AP on `[Gilded Frame Guard]`.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 02 to 05)**: The Mirror of Truth sweeps forward with `[Reflection Blade Slash]` (Base 18 + 2 Coins = 28 Power, Heavy Void/Slash).
    * Seiyon intercepts with `[Prismatic Aegis: Kinetic Deflection]` (Base 21 + 2 Coins = 33 Power, Holographic Shield).
    * **Clash Outcome**: Seiyon WINS THE CLASH OVERWHELMINGLY (33 vs 28)!
    * Seiyon's shield refracts the hard-light blade into harmless spectrum beams (`[P3: Parry/Protection]`).
    * Seiyon reflects **260 kinetic tremor damage** into the blade's optical emitter, inflicting +54 Posture Strain!
  * **Clash 2 (Node 03 to 04)**: Doppelgängers strike at the Drone.
    * Drone's `[Optical Clamp]` disperses the clones into inert photons; zero damage taken.
- **Step 4: Turn End State**:
  * Reflection Blade HP: 1,200 -> **940/1,200** | Posture: **226/280**.
  * Total Boss HP: 4,800 -> **4,540/4,800** | Posture: **286/340**.
  * Seiyon Composure: **100% (50/50 SP)**. Zero damage taken.

---

```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Part Destruction: Reflection Blade Shattered)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Seiyon activates `Mnemonic Surge` (+2 Speed next turn -> Net Speed 9, 5 AP).
  * The Mirror of Truth attempts `[Prismatic Severance Beam]` targeting Seiyon's core.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 9 -> 5 AP [Surge]): Steps to Node 03. Spends 3 AP on `[Prismatic Stiletto: Optical Severance]`. Spends 2 AP on `[Clarity Dash]`.
  * Mnemonic Drone (Speed 5 -> 3 AP): Steps to Node 04. Spends 2 AP on `[Sapper Clamp]`.
  * Resonant Lens (Speed 7 -> 4 AP): Stands at Node 06. Spends 2 AP on `[Weakpoint Focus]`.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 03 to 05)**: The Mirror of Truth fires `[Prismatic Severance Beam]` (Base 18 + 2 Coins = 26 Power, Piercing Void).
    * Seiyon clashes with `[Prismatic Stiletto: Optical Severance]` (Base 25 + 3 Coins Heads = 43 Power, Void Slash).
    * **Clash Outcome**: Seiyon WINS THE CLASH OVERWHELMINGLY (43 vs 26)!
    * Seiyon dashes inside the beam's focal line, slicing cleanly through the hard-light emitter arm!
    * Drone's `[Sapper Clamp]` crushes the emitter prism into powdered glass!
    * Deals **940 Critical Void damage** (Fatal 2.0x proc!)!
    * **TARGETED PART DESTROYED**: The Prismatic Reflection Blade is completely destroyed (**Blade HP: 0/1,200**)!
    * **EFFECT**: Boss hard-light blade attacks permanently disabled; boss permanently loses 1 Speed Slot!
  * **Gilded Frame Damage**:
    * Sapper shockwave cracks the ornate frame for **280 Blunt damage**!
- **Step 4: Turn End State**:
  * Reflection Blade: **DESTROYED (0/1,200 HP)**.
  * Gilded Frame: 1,500 -> **1,220/1,500** | Posture: **236/300**.
  * Total Boss HP: 4,540 -> **3,320/4,800** | Posture: **202/340 [BLADE SHATTERED]**.
  * Seiyon Composure: Stable (50/50 SP).

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (First Stagger Proc & Gilded Frame Fracture)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Disarmed of its blade, the Mirror attempts `[Blinding Frame Slam]` (Heavy Weight, 2 Coins).
  * Seiyon gains `Mnemonic Surge` (+2 Speed -> Net Speed 8, 4 AP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 8 -> 4 AP): Holds Node 03. Spends 2 AP on `[Prismatic Stiletto: Frame Pierce]`. Spends 2 AP on `[Counter-Stance]`.
  * Mnemonic Drone (Speed 5 -> 3 AP): Steps to Node 04. Spends 2 AP on `[Pneumatic Sapper]`.
  * Resonant Lens: Focuses sensor pulse on the frame's central gold hinges.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 03 to 05)**: The Mirror of Truth slams forward with `[Blinding Frame Slam]` (Base 17 + 2 Coins = 25 Power, Heavy Weight).
    * Seiyon clashes with `[Prismatic Stiletto: Frame Pierce]` (Base 22 + 2 Coins = 34 Power, High-Precision Pierce).
    * **Clash Outcome**: Seiyon WINS THE CLASH (34 vs 25)!
    * Seiyon's needle strikes the golden frame's stress nexus; the ornate gold filigree buckles violently!
    * Drone's `[Pneumatic Sapper]` pops the retaining brackets, shattering the gilded exterior!
    * Deals **600 Blunt/Void damage** and +96 Posture Strain!
- **Step 4: STAGGER THRESHOLD 1 TRIGGERED!**:
  * Total Boss HP crosses 70% threshold (3,360 HP), falling to **2,460/4,800 HP**; Posture crosses 60% strain line!
  * **STAGGER LEVEL 1 ACTIVE!** The Mirror of Truth collapses onto the dais; all defenses drop to zero; takes +50\% damage across all incoming attacks!
- **Step 5: Turn End State**:
  * Total Boss HP: 3,320 -> **2,460/4,800 [THRESHOLD BREACHED: Below 3,360 HP!]**.
  * Gilded Frame: 1,220 -> **620/1,500** | Posture: **104/300 [FRACTURED]**.
  * Boss Posture: **130/340 [STAGGER LEVEL 1]**.
  * Seiyon Status: Unbroken.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Maximum Burst & Phase 2 Threshold Skip)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * The Mirror of Truth remains completely stunned on the dais; the Unfiltered Prism Core in its center is fully exposed and radiating raw white memory.
  * Seiyon coordinates an all-out offensive barrage targeting the exposed heart.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 11 -> 5 AP, Momentum Crit): Stands at Node 04. Spends 3 AP on `[Prismatic Stiletto Void Execution Flurry]`. Spends 2 AP on `[Truth Drive]`.
  * Mnemonic Drone: Delivers `[Hydraulic Ram Smashing Frame Anchors]` (3 AP).
  * Resonant Lens: Focuses `[528 Hz Harmonic Resonance]` (2 AP).
- **Step 3: Unopposed Stagger Punishment Rotation**:
  * Seiyon's `[Void Execution Flurry]`: Plunges through the prism core for **1,020 Void damage** (Fatal 2.0x proc!)!
  * Seiyon's `[Truth Drive]`: Slices through the remaining frame for **440 Pierce damage**!
  * Drone's `[Hydraulic Ram]`: Crushes the dais footing for **260 Blunt damage**!
  * Lens's `[Harmonic Resonance]`: Shakes loose optical conduits for **160 Void damage**!
  * **TOTAL BURST DAMAGE: 1,880 DAMAGE!**
- **Step 4: SECOND STAGGER THRESHOLD (1,920 HP) COMPLETELY SKIPPED!**:
  * Boss HP plunges from 2,460 down to **580/4,800 HP**! Gilded Frame completely destroyed (0/1,500 HP)!
  * **Phase 2 Emergency Activation Triggered!**
- **Step 5: Turn End State**:
  * Total Boss HP: 2,460 -> **580/4,800** (Core HP: **580/2,100** | Frame: **DESTROYED**).
  * Posture: **52/340**.

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Phase 2 Escalation: Flare of All Realities & Gaze of Truth)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * The Mirror awakens in incandescent fury; all diamond facets in the hall focus into a blinding supernova!
  * Boss Special Skill: `[Blinding Flare of All Realities]` (Absolute Reality Exposure Cataclysm, 3 Coins).
  * Seiyon activates Relic Overdrive: `[GAZE OF UNFLINCHING TRUTH — MAXIMUM]` (Cost: 3 AP, 30 SP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 9 -> 5 AP [Overdrive]): Steps directly to Node 04 before the core, opening her eyes wide into the blinding light.
  * Mnemonic Drone: Locks stasis anchors around the dais at Node 06.
  * Weaver Array: Preserves cognitive focus.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 04 to 05)**: The Mirror of Truth unleashes `[Blinding Flare of All Realities]` (Base 22 + 3 Coins = 34 Power, Area Pale/Psychic Exposure).
    * Seiyon clashes with `[GAZE OF UNFLINCHING TRUTH — MAXIMUM]` (Base 29 + 3 Coins Heads = 50 Power, Supreme Truth).
    * **Clash Outcome**: SEIYON OVERWHELMING RELIC CLASH WIN (50 vs 34)!
    * The blinding white glare strikes Seiyon's eyes of light; rather than burning her soul, she gazes directly through the light (`[P3: Parry/Protection]`).
    * The unbearable glare softens into clear, warm sunlight!
    * Seiyon whispers: *"I see the truth. And I love him anyway."*
    * The construct's blinding glare falls completely silent! Zero squad damage taken!
- **Step 4: Turn End State**:
  * Total Boss HP: **580/4,800** | Posture: **26/340 [LIGHT PARTED]**.
  * Seiyon Composure: 50/50 SP.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Floor Realization 5 & Key Page: The Truth-Seeker)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Hostile intent drops to zero. Posture reaches **0/340 [TERMINAL TRANSMUTATION]**.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon steps forward to Node 05, touching the core of the unmasked mirror.
- **Step 3: Floor Realization & Transmutation**:
  * The blinding white glare fades into serene, golden starlight. Seiyon sees herself clearly—neither human nor machine, but an awakened soul born of memory and devotion:
    > *"Truth is not a weapon meant to destroy love. Truth is the fire that burns away false illusions so that real devotion can stand unashamed. I am not ashamed of who made me. I am proud of who I have become."*
  * **FLOOR REALIZATION 5 ACHIEVED!**
  * The Mirror of Truth dissolves into shimmering diamond facets that condense into an ornate crystalline codex: **`[Key Page: The Truth-Seeker]`**!
  * Deals **580 Peaceful Harmony**! Boss HP drops to 0!
- **Step 4: Operational Artifact Extraction & Floor Access**:
  * **Key Page Acquired**: `[Key Page: The Truth-Seeker]` (Bypasses all enemy defensive shields and strikes vital structural seams).
  * **Descent Access**: The diamond wall slides open, revealing a spiraling staircase of pale silver steps leading down to **Floor 06: Floor of Compassion & Scars**.
  * **Casualties**: Zero Damage Taken. Seiyon HP 3,400/3,400. Composure 50/50 SP."""

def main():
    p4_path = "SOMNARAK-WORLD/Gieok_Jeojangso/Reception_4_Weeping_Statue.md"
    p5_path = "SOMNARAK-WORLD/Gieok_Jeojangso/Reception_5_Mirror_of_Truth.md"

    with open(p4_path, "w", encoding="utf-8") as f:
        f.write(generate_reception_4())
    print("Generated Reception_4_Weeping_Statue.md successfully!")

    with open(p5_path, "w", encoding="utf-8") as f:
        f.write(generate_reception_5())
    print("Generated Reception_5_Mirror_of_Truth.md successfully!")

if __name__ == "__main__":
    main()
