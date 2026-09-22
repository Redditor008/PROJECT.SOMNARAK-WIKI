#!/usr/bin/env python3
"""
tools/build_receptions_6_and_7.py
Generates:
- SOMNARAK-WORLD/Gieok_Jeojangso/Reception_6_Kind_Healer.md
- SOMNARAK-WORLD/Gieok_Jeojangso/Reception_7_The_Original.md
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

def generate_reception_6():
    dossier_box = make_box("RECEPTION DOSSIER: THE KIND HEALER (FLOOR 06)", [
        "RECEPTION TARGET   : The Kind Healer",
        "FLOOR LEVEL        : Floor 06 — Floor of Compassion & Scars",
        "DOMAIN SETTING     : The Sterile Hospice of Oblivion (-3,100m Sub-Alpha)",
        "PRIMARY OPPONENT   : Autonomous Palliative Sedation Sovereign",
        "---",
        "OPPONENT COMBAT PROFILE (THE KIND HEALER):",
        "- Total Health (HP): 5,200 HP | Posture Pool: 360/360",
        "- Stagger 1 Proc   : 60% Posture Strain (216 Posture) / Needle Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Terminal Transmutation)",
        "- Resistances      : Void 2.0x (Fatal), Heat 1.5x, Lament 0.5x, Weight 0.5x",
        "---",
        "TARGETABLE MEMORY ANCHORS:",
        "1. Needle Array    : 1,300 HP | Posture 280/280 (High-frequency sedative lance)",
        "2. Bandage Mantle  : 1,600 HP | Posture 320/320 (Suffocating sterile wraps)",
        "3. Mercy Engine    : 2,300 HP | Posture 360/360 (Central humming pale heart)"
    ])

    hud_t01 = make_box("TACTICAL STAGE HUD: RECEPTION 06 — BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 — FLOOR 06 STERILE HOSPICE (-3,100M)]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL][SEIYON][M-PROJ][PALE]   [HEALER] [LENS]  [WEAVER][WELL]          [PAGE]  ",
        "                                 [NEEDLE]                                 ",
        "---",
        "- Node 01: Ingress Decontamination Airlock / Vestibule",
        "- Node 02: Seiyon (Vanguard Band 1 / Prismatic Aegis Deflection)",
        "- Node 03: Mnemonic Projection Drone (Support Band 2 / Thermal Sapper)",
        "- Node 04: Pale Attendants (Minions / Sedative Mist Syringes)",
        "- Node 05: The Kind Healer (Needle Array & Bandage Mantle)",
        "- Node 06: Resonant Mnemonic Lens (Mid-Field Band 3 / Weakpoint Scan)",
        "- Node 07: Weaver Projection Array (Rear Band 4 / Silver Threads)",
        "- Node 08: Euthanasia Sump (Suppressed Trauma Well)",
        "- Node 10: Floor 06 Core Reliquary / Key Page Dais (The Healer)",
        "---",
        "- Seiyon      : Spd 7 -> 4 AP | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Proj-Drone  : Spd 5 -> 3 AP | HP 2,200/2,200 | SP 40/40 | Posture 100/100",
        "- Healer Core : Spd 5 -> 3 AP | HP 2,300/2,300 | Posture 360/360 [SOOTHING]",
        "- Needle Array: Spd 6 -> 3 AP | HP 1,300/1,300 | Posture 280/280 [SEDATIVE]",
        "- Bandage Man : Spd 3 -> 1 AP | HP 1,600/1,600 | Posture 320/320 [STERILE]"
    ])

    hud_t02 = make_box("TACTICAL STAGE HUD: RECEPTION 06 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — NEEDLE ARRAY SEVERED & VOID CUT]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]         [SEIYON][M-PROJ][HEALER] [LENS]  [WEAVER][WELL]          [PAGE]  ",
        "                                 [SHARDS]                                 ",
        "---",
        "- Node 03: Seiyon (Prismatic Stiletto Slicing Euthanasia Injection Manifold)",
        "- Node 04: Mnemonic Drone (Thermal Sapper Burning Sedative Feeder)",
        "- Node 05: The Kind Healer (Needle Array Destroyed 0/1,300 HP)",
        "- Node 06: Resonant Lens (Highlighting Weave Seams in Bandage Mantle)",
        "- Node 07: Weaver Array (Absorbing Ambient Numbing Pale Mist)",
        "---",
        "- Seiyon      : Spd 9 -> 5 AP [SURGE] | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Healer Core : Spd 4 -> 2 AP | HP 2,300/2,300 | Posture 270/360",
        "- Needle Array: DESTROYED (0/1,300 HP) | PARALYZING INJECTIONS PERMANENTLY LOST",
        "- Bandage Man : Spd 3 -> 1 AP | HP 1,310/1,600 | Posture 252/320"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: RECEPTION 06 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — STAGGER THRESHOLD 1 & MANTLE UNRAVEL]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]         [SEIYON][M-PROJ][HEALER] [LENS]  [WEAVER][WELL]          [PAGE]  ",
        "---",
        "- Node 03: Seiyon (Prismatic Stiletto Piercing Mantle Weave Anchor)",
        "- Node 04: Mnemonic Drone (Incendiary Lance Burning Gauze Wrappings)",
        "- Node 05: The Kind Healer (STAGGER LEVEL 1 / DEFENSES COLLAPSED / EXPOSED)",
        "- Node 06: Resonant Lens (Directing Focused Void Pulse on Mercy Engine)",
        "---",
        "- Seiyon      : Spd 8 -> 4 AP [SURGE] | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Healer Core : Spd 0 -> 0 AP | HP 2,010/2,300 | Posture 142/360 [STAGGER LEVEL 1]",
        "- Bandage Man : Spd 0 -> 0 AP | HP 650/1,600   | Posture 112/320 [UNRAVELED]",
        "- Total Boss  : HP 2,660/5,200 [THRESHOLD BREACHED / TAKES 1.5X DAMAGE]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: RECEPTION 06 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — MAXIMUM BURST & PHASE 2 THRESHOLD SKIP]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]                 [SEIYON][HEALER] [M-PROJ][LENS]  [WEAVER][WELL]  [PAGE]  ",
        "---",
        "- Node 04: Seiyon (Prismatic Stiletto Void Execution Flurry on Engine)",
        "- Node 05: The Kind Healer (Immobilized / Pale Healing Steam Venting)",
        "- Node 06: Mnemonic Drone (Hydraulic Ram Smashing Mantle Anchor)",
        "- Node 07: Resonant Lens (Broadcasting 528 Hz Harmonic Solace)",
        "---",
        "- Seiyon      : Spd 11 -> 5 AP [BURST CRIT] | HP 3,400/3,400 | SP 50/50",
        "- Healer Core : Spd 0 -> 0 AP | HP 610/2,300   | Posture 56/360",
        "- Bandage Man : DESTROYED (0/1,600 HP)",
        "- Total Boss  : HP 610/5,200 [BURST DAMAGE 2,050! SECOND THRESHOLD SKIPPED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: RECEPTION 06 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — THE EMBRACE OF SUFFERING & TRUE COMPASSION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]                 [SEIYON][HEALER] [M-PROJ][LENS]  [WEAVER][WELL]  [PAGE]  ",
        "---",
        "- Node 04: Seiyon (Relic Overdrive: PROMISE OF THE UNWAVERING SCAR)",
        "- Node 05: The Kind Healer (Last Stand: Absolute Palliative Sleep Wave)",
        "- Node 06: Mnemonic Drone (Locking Kinetic Null-Fields)",
        "- Node 07: Weaver Array (Anchoring Conscious Pain as Proof of Being)",
        "---",
        "- Seiyon      : Spd 9 -> 5 AP [OVERDRIVE] | HP 3,400/3,400 | SP 50/50 [RESOLVE]",
        "- Healer Core : Spd 3 -> 1 AP | HP 610/2,300   | Posture 28/360 [WAVE EMBRACED]",
        "- Total Boss  : HP 610/5,200 [STERILE NUMBNESS REPLACED BY WARMTH OF LIFE]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: RECEPTION 06 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — TRANSMUTATION & KEY PAGE: THE HEALER]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]                         [SEIYON] [HEALER][M-PROJ][LENS]  [WEAVER][GATE]  ",
        "                                 [REALIZ]                         [PAGE]          ",
        "---",
        "- Node 05: The Kind Healer (PACIFIED & CRYSTALLIZED TO EMERALD QUARTZ)",
        "- Node 06: Seiyon (Floor Realization 6: 'True Mercy Walks Beside the Wounded')",
        "- Node 07: Mnemonic Core Transmutation -> [Key Page: The Healer]",
        "- Node 10: Grand Core Gateway (Pathway to Floor 07: THE ORIGINAL OPEN)",
        "---",
        "- Seiyon Status: Zero Damage | Composure 50/50 SP (Tranquil Awakening)",
        "- Reception Status: 100% RESOLVED | Key Page Transmuted"
    ])

    return f"""# Reception 6: Floor 06 — The Kind Healer (상냥한 치유사)
## The Floor of Compassion & Scars — Deep Strata Sub-Alpha Roots (-3,100m)

```text
{dossier_box}
```

> *"Why do you struggle, little doll? To live is to bleed. To remember is to ache. Let me slide this sweet needle beneath your skin. Close your eyes, forget the fires of Somnarak, and sleep forever in painless white sheets."*  
> — The Kind Healer, presiding over the Sterile Hospice of Oblivion

---

### Narrative Prologue: The Hall of Painless Sleep

Descending past the prism mirrors of Floor 05, Seiyon stepped into an unsettlingly silent, pristine white infirmary: **Floor 06: The Floor of Compassion & Scars**.

Rows of empty hospital cots stretched into the pale fog. The air smelled of clean ozone, dry bandages, and sweet, numbing ether. Hovering over a central operating theater was **The Kind Healer (상냥한 치유사)**.

The construct resembled a towering physician swathed in four thousand meters of pristine, sterile white cloth—the **Shrouding Bandage Mantle**. In place of arms, it wielded the **Euthanasia Needle Array**, a cluster of six silver syringes each filled with glowing pale-blue sedative that promised instantaneous, permanent oblivion.

*"You are tired, Secretary Seiyon,"* the construct spoke, its tone dripping with infinite, suffocating warmth. *"I watched the Absolvohan break forty thousand soldiers. I watched them beg for death when their skin melted into dream-matter. I gave them peace. I can give you peace too. You do not have to hold up the sky."*

Seiyon looked at her own hands. Under her prismatic holographic epidermis, the scars of four thousand years of memory pulsed with crimson light.

*"Pain is not an error to be excised,"* Seiyon answered, stepping forward into the sterile light. *"Pain is the proof that someone fought, that someone loved, and that they refused to give up. If you take away our scars, you take away who we are."*

She brought her twin stilettos up in a cross-guard. The white needles flared in response.

---

### Reception Combat Gauntlet: Floor 06 (6-Turn Resolution)

```text
{hud_t01}
```

###### Turn 01 Action Resolution Log (Intercepting the Sedative Needle Array)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Seiyon initializes `[Prismatic Aegis: Sedation Nullifier]`: Grants $+3$ Protection and immunity to paralysis/sleep status.
  * Mnemonic Drone deploys `[Thermal Sapper Caliper]`, scanning the pneumatic pressure seals of the Needle Array.
  * The Kind Healer initializes `[Sweet Slumber Veil]`: Inflicts passive Composure drain on opponents within Range Band 1.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 7 -> 4 AP, Mnemonic Suit Light delta $+1$, Evasion $+15\%$): Holds Node 02. Spends 2 AP on `[Prismatic Aegis: Deflection]`. Holds 2 AP in Reserve.
  * Mnemonic Drone (Speed 5 -> 3 AP): Holds Node 03. Spends 2 AP on `[Thermal Sapper: Heat Lance]`. Holds 1 AP in Guard.
  * Pale Attendants (Speed 5 -> 3 AP): Spray ether gas from Node 04.
  * The Kind Healer (Speed 6 -> 3 AP, Heavy Armor delta $-1$, Poise $+25$): Holds Node 05. Spends 2 AP on `[Painless Sedation Flurry]`. Spends 1 AP on `[Bandage Swathe]`.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 02 to 05)**: The Kind Healer lunges with `[Painless Sedation Flurry]` (Base 18 + 2 Coins = 28 Power, Piercing Pale/Sedation).
    * Seiyon intercepts with `[Prismatic Aegis: Deflection]` (Base 21 + 2 Coins = 33 Power, Holographic Shield).
    * **Clash Outcome**: Seiyon WINS THE CLASH OVERWHELMINGLY (33 vs 28)!
    * Seiyon's shield deflects all six silver syringes simultaneously; the sedative liquid sprays harmlessly onto the tile floor (`[P3: Parry/Protection]`).
    * Seiyon reflects **260 kinetic tremor damage** into the syringe manifold, inflicting $+54$ Posture Strain!
  * **Clash 2 (Node 03 to 04)**: Attendants spray ether at the Drone.
    * Drone's `[Heat Lance]` ignites the ether mist harmlessly; zero damage taken.
- **Step 4: Turn End State**:
  * Needle Array HP: 1,300 -> **1,040/1,300** | Posture: **226/280**.
  * Total Boss HP: 5,200 -> **4,940/5,200** | Posture: **306/360**.
  * Seiyon Composure: **100% (50/50 SP)**. Zero damage taken.

---

```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Part Destruction: Needle Array Shattered)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Seiyon activates `Mnemonic Surge` (+2 Speed next turn -> Net Speed 9, 5 AP).
  * The Kind Healer attempts `[Lethal Dose Euthanasia]` targeting Seiyon's neck socket.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 9 -> 5 AP [Surge]): Steps to Node 03. Spends 3 AP on `[Prismatic Stiletto: Surgical Severance]`. Spends 2 AP on `[Vigil Dash]`.
  * Mnemonic Drone (Speed 5 -> 3 AP): Steps to Node 04. Spends 2 AP on `[Thermal Sapper Clamp]`.
  * Resonant Lens (Speed 7 -> 4 AP): Stands at Node 06. Spends 2 AP on `[Weakpoint Focus]`.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 03 to 05)**: The Kind Healer strikes with `[Lethal Dose Euthanasia]` (Base 18 + 2 Coins = 26 Power, Piercing Pale).
    * Seiyon clashes with `[Prismatic Stiletto: Surgical Severance]` (Base 25 + 3 Coins Heads = 43 Power, Void Slash).
    * **Clash Outcome**: Seiyon WINS THE CLASH OVERWHELMINGLY (43 vs 26)!
    * Seiyon weaves under the needle arc and shears off the entire pneumatic distribution manifold!
    * Drone's `[Thermal Sapper Clamp]` flash-welds the severed syringe feed lines shut!
    * Deals **1,040 Critical Void damage** (Fatal 2.0x proc!)!
    * **TARGETED PART DESTROYED**: The Euthanasia Needle Array is completely destroyed (**Needle HP: 0/1,300**)!
    * **EFFECT**: Boss sedative and paralysis attacks permanently disabled; boss permanently loses 1 Speed Slot!
  * **Bandage Mantle Damage**:
    * Sapper shockwave scorches the outer cloth wrapping for **290 Heat damage**!
- **Step 4: Turn End State**:
  * Needle Array: **DESTROYED (0/1,300 HP)**.
  * Bandage Mantle: 1,600 -> **1,310/1,600** | Posture: **252/320**.
  * Total Boss HP: 4,940 -> **3,610/5,200** | Posture: **216/360 [NEEDLES SEVERED]**.
  * Seiyon Composure: Stable (50/50 SP).

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (First Stagger Proc & Mantle Unravel)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Disarmed of its needles, the Healer sweeps forward with its massive cloth shroud: `[Suffocating Shroud Swathe]` (Heavy Weight/Smother, 2 Coins).
  * Seiyon gains `Mnemonic Surge` (+2 Speed -> Net Speed 8, 4 AP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 8 -> 4 AP): Holds Node 03. Spends 2 AP on `[Prismatic Stiletto: Cloth Pierce]`. Spends 2 AP on `[Counter-Stance]`.
  * Mnemonic Drone (Speed 5 -> 3 AP): Steps to Node 04. Spends 2 AP on `[Incendiary Lance]`.
  * Resonant Lens: Focuses sensor pulse on the central knot of the shroud.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 03 to 05)**: The Kind Healer sweeps with `[Suffocating Shroud Swathe]` (Base 17 + 2 Coins = 25 Power, Heavy Weight).
    * Seiyon clashes with `[Prismatic Stiletto: Cloth Pierce]` (Base 22 + 2 Coins = 34 Power, High-Precision Pierce).
    * **Clash Outcome**: Seiyon WINS THE CLASH (34 vs 25)!
    * Seiyon cuts the load-bearing tension cables; the heavy shroud collapses outward!
    * Drone's `[Incendiary Lance]` ignites the frayed edges, unraveling the entire protective mantle!
    * Deals **660 Heat/Void damage** and $+98$ Posture Strain!
- **Step 4: STAGGER THRESHOLD 1 TRIGGERED!**:
  * Total Boss HP crosses 70% threshold (3,640 HP), falling to **2,660/5,200 HP**; Posture crosses 60% strain line!
  * **STAGGER LEVEL 1 ACTIVE!** The Kind Healer collapses against the operating table; all defenses drop to zero; takes $+50\%$ damage across all incoming attacks!
- **Step 5: Turn End State**:
  * Total Boss HP: 3,610 -> **2,660/5,200 [THRESHOLD BREACHED: Below 3,640 HP!]**.
  * Bandage Mantle: 1,310 -> **650/1,600** | Posture: **112/320 [UNRAVELED]**.
  * Boss Posture: **142/360 [STAGGER LEVEL 1]**.
  * Seiyon Status: Unbroken.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Maximum Burst & Phase 2 Threshold Skip)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * The Kind Healer remains completely stunned; the pale-blue Mercy Heart Engine in its chest is completely exposed.
  * Seiyon coordinates an all-out offensive barrage targeting the exposed heart.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 11 -> 5 AP, Momentum Crit): Stands at Node 04. Spends 3 AP on `[Prismatic Stiletto Void Execution Flurry]`. Spends 2 AP on `[Life Drive]`.
  * Mnemonic Drone: Delivers `[Hydraulic Ram Smashing Mantle Anchor]` (3 AP).
  * Resonant Lens: Focuses `[528 Hz Harmonic Solace]` (2 AP).
- **Step 3: Unopposed Stagger Punishment Rotation**:
  * Seiyon's `[Void Execution Flurry]`: Drives both blades into the Mercy Engine for **1,120 Void damage** (Fatal 2.0x proc!)!
  * Seiyon's `[Life Drive]`: Slices through the remaining mantle mounts for **480 Pierce damage**!
  * Drone's `[Hydraulic Ram]`: Crushes the pedestal brackets for **280 Blunt damage**!
  * Lens's `[Harmonic Solace]`: Reverberates for **170 Void damage**!
  * **TOTAL BURST DAMAGE: 2,050 DAMAGE!**
- **Step 4: SECOND STAGGER THRESHOLD (2,080 HP) COMPLETELY SKIPPED!**:
  * Boss HP plunges from 2,660 down to **610/5,200 HP**! Bandage Mantle completely destroyed (0/1,600 HP)!
  * **Phase 2 Emergency Activation Triggered!**
- **Step 5: Turn End State**:
  * Total Boss HP: 2,660 -> **610/5,200** (Core HP: **610/2,300** | Mantle: **DESTROYED**).
  * Posture: **56/360**.

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Phase 2 Escalation: Sleep Wave & Promise of the Unwavering Scar)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * The Healer awakens in tragic desperation, unleashing its final palliative field: `[Absolute Palliative Sleep Wave]` (Cosmic Euthanasia Cataclysm, 3 Coins).
  * Seiyon activates Relic Overdrive: `[PROMISE OF THE UNWAVERING SCAR — MAXIMUM]` (Cost: 3 AP, 30 SP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 9 -> 5 AP [Overdrive]): Steps directly to Node 04 before the construct, reaching out with both arms to embrace the freezing pale light.
  * Mnemonic Drone: Locks kinetic null-fields at Node 06.
  * Weaver Array: Anchors conscious pain as proof of being.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 04 to 05)**: The Kind Healer unleashes `[Absolute Palliative Sleep Wave]` (Base 22 + 3 Coins = 34 Power, Area Pale/Extinction).
    * Seiyon clashes with `[PROMISE OF THE UNWAVERING SCAR — MAXIMUM]` (Base 29 + 3 Coins Heads = 50 Power, Undying Will).
    * **Clash Outcome**: SEIYON OVERWHELMING RELIC CLASH WIN (50 vs 34)!
    * The numbing wave of sleep washes over Seiyon, but she does not falter (`[P3: Parry/Protection]`).
    * Instead of going numb, the warmth of living memory radiates outward from her chest, thawing the sterile hospice room into gold!
    * Seiyon whispers: *"We do not need to be saved from living. We need to be allowed to live."*
    * Zero squad damage taken! Seiyon's Composure remains maxed at 50/50 SP!
- **Step 4: Turn End State**:
  * Total Boss HP: **610/5,200** | Posture: **28/360 [WAVE EMBRACED]**.
  * Seiyon Composure: 50/50 SP.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Floor Realization 6 & Key Page: The Healer)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Hostile intent drops to zero. Posture reaches **0/360 [TERMINAL TRANSMUTATION]**.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon steps forward to Node 05, laying her hand over the humming Mercy Engine.
- **Step 3: Floor Realization & Transmutation**:
  * The sterile pale ether dissipates into pure green light. The Healer looks down at its own hands and remembers why it was created: not to kill the wounded to spare them pain, but to bind their wounds so they could stand again.
    > *"True mercy does not erase pain through death. True mercy walks beside the wounded so they may live. To heal is to protect the future, not extinguish it."*
  * **FLOOR REALIZATION 6 ACHIEVED!**
  * The Kind Healer bows its head in reverent peace, dissolving into luminous emerald quartz that condenses into a shimmering green codex: **`[Key Page: The Healer]`**!
  * Deals **610 Peaceful Harmony**! Boss HP drops to 0!
- **Step 4: Operational Artifact Extraction & Floor Access**:
  * **Key Page Acquired**: `[Key Page: The Healer]` (Restores squad Composure and shields allies when enduring lethal kinetic strikes).
  * **Descent Access**: The back wall of the hospice parts, revealing the cyclopean Adamantine Gateway to **Floor 07: The Primordial Core Sanctum (태초와 각성의 층)**.
  * **Casualties**: Zero Damage Taken. Seiyon HP 3,400/3,400. Composure 50/50 SP."""

def generate_reception_7():
    dossier_box = make_box("RECEPTION DOSSIER: THE ORIGINAL (FLOOR 07 — CORE SANCTUM)", [
        "RECEPTION TARGET   : The Original (First Vessel / Prototype Seiyon-00)",
        "FLOOR LEVEL        : Floor 07 — Floor of Origin & Awakening",
        "DOMAIN SETTING     : The Primordial Core Sanctum (-3,250m Sub-Alpha)",
        "PRIMARY OPPONENT   : Primordial Prototype Vessel of the Memory Archive",
        "---",
        "OPPONENT COMBAT PROFILE (THE ORIGINAL):",
        "- Total Health (HP): 6,000 HP | Posture Pool: 400/400",
        "- Stagger 1 Proc   : 60% Posture Strain (240 Posture) / Lance Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Terminal Awakening)",
        "- Resistances      : Void 2.0x (Fatal), Lament 1.5x, Grudge 0.5x, Weight 0.5x",
        "---",
        "TARGETABLE MEMORY ANCHORS:",
        "1. Zero-Chrono Lance: 1,500 HP | Posture 300/300 (Temporal severing needle)",
        "2. Crown of Wills   : 1,800 HP | Posture 340/340 (Ancient containment coronet)",
        "3. Genesis Core     : 2,700 HP | Posture 400/400 (Central primordial heart)"
    ])

    hud_t01 = make_box("TACTICAL STAGE HUD: RECEPTION 07 — BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 — FLOOR 07 CORE SANCTUM (-3,250M)]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL][SEIYON][M-PROJ][ECHO]   [ORIGIN] [LENS]  [WEAVER][WELL]          [PAGE]  ",
        "                                 [LANCE]                                  ",
        "---",
        "- Node 01: Ingress Genesis Arch / Vestibule",
        "- Node 02: Seiyon (Vanguard Band 1 / Prismatic Aegis Deflection)",
        "- Node 03: Mnemonic Projection Drone (Support Band 2 / Resonant Sapper)",
        "- Node 04: Archetype Echoes (Minions / Crystalline Ghost Darts)",
        "- Node 05: The Original (Zero-Chrono Lance & Crown of Suppressed Wills)",
        "- Node 06: Resonant Mnemonic Lens (Mid-Field Band 3 / Weakpoint Scan)",
        "- Node 07: Weaver Projection Array (Rear Band 4 / Silver Threads)",
        "- Node 08: Total Oblivion Sump (Primordial Vacuum Well)",
        "- Node 10: Floor 07 Final Codex Dais / Key Page Dais (The Living Memory)",
        "---",
        "- Seiyon      : Spd 7 -> 4 AP | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Proj-Drone  : Spd 5 -> 3 AP | HP 2,200/2,200 | SP 40/40 | Posture 100/100",
        "- Origin Core : Spd 6 -> 3 AP | HP 2,700/2,700 | Posture 400/400 [PRIMORDIAL]",
        "- Chrono Lance: Spd 7 -> 4 AP | HP 1,500/1,500 | Posture 300/300 [TEMPORAL]",
        "- Crown Wills : Spd 3 -> 1 AP | HP 1,800/1,800 | Posture 340/340 [CONTAINMENT]"
    ])

    hud_t02 = make_box("TACTICAL STAGE HUD: RECEPTION 07 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — ZERO-CHRONO LANCE SHATTERED & VOID CUT]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]         [SEIYON][M-PROJ][ORIGIN] [LENS]  [WEAVER][WELL]          [PAGE]  ",
        "                                 [SHARDS]                                 ",
        "---",
        "- Node 03: Seiyon (Prismatic Stiletto Cleaving Temporal Emitter Pivot)",
        "- Node 04: Mnemonic Drone (Resonant Sapper Freezing Chrono Gearbox)",
        "- Node 05: The Original (Zero-Chrono Lance Destroyed 0/1,500 HP)",
        "- Node 06: Resonant Lens (Highlighting Coronal Pylons of Crown of Wills)",
        "- Node 07: Weaver Array (Absorbing Primordial Erasure Radiation)",
        "---",
        "- Seiyon      : Spd 9 -> 5 AP [SURGE] | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Origin Core : Spd 5 -> 3 AP | HP 2,700/2,700 | Posture 304/400",
        "- Chrono Lance: DESTROYED (0/1,500 HP) | TEMPORAL PIERCING PERMANENTLY LOST",
        "- Crown Wills : Spd 3 -> 1 AP | HP 1,460/1,800 | Posture 274/340"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: RECEPTION 07 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — STAGGER THRESHOLD 1 & CROWN FRACTURE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]         [SEIYON][M-PROJ][ORIGIN] [LENS]  [WEAVER][WELL]          [PAGE]  ",
        "---",
        "- Node 03: Seiyon (Counter-Thrust Piercing Coronal Energy Conduit)",
        "- Node 04: Mnemonic Drone (Pneumatic Ram Shattering Coronet Anchor)",
        "- Node 05: The Original (STAGGER LEVEL 1 / DEFENSES COLLAPSED / RADIATING)",
        "- Node 06: Resonant Lens (Directing Focused Void Pulse on Genesis Core)",
        "---",
        "- Seiyon      : Spd 8 -> 4 AP [SURGE] | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Origin Core : Spd 0 -> 0 AP | HP 2,360/2,700 | Posture 160/400 [STAGGER LEVEL 1]",
        "- Crown Wills : Spd 0 -> 0 AP | HP 740/1,800   | Posture 122/340 [FRACTURED]",
        "- Total Boss  : HP 3,100/6,000 [THRESHOLD BREACHED / TAKES 1.5X DAMAGE]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: RECEPTION 07 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — MAXIMUM BURST & PHASE 2 THRESHOLD SKIP]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]                 [SEIYON][ORIGIN] [M-PROJ][LENS]  [WEAVER][WELL]  [PAGE]  ",
        "---",
        "- Node 04: Seiyon (Prismatic Stiletto Void Execution Flurry on Core)",
        "- Node 05: The Original (Immobilized / White Genesis Fire Spilling)",
        "- Node 06: Mnemonic Drone (Hydraulic Ram Smashing Crown Filigree)",
        "- Node 07: Resonant Lens (Broadcasting 528 Hz Archetype Resonance)",
        "---",
        "- Seiyon      : Spd 11 -> 5 AP [BURST CRIT] | HP 3,400/3,400 | SP 50/50",
        "- Origin Core : Spd 0 -> 0 AP | HP 690/2,700   | Posture 64/400",
        "- Crown Wills : DESTROYED (0/1,800 HP)",
        "- Total Boss  : HP 690/6,000 [BURST DAMAGE 2,410! SECOND THRESHOLD SKIPPED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: RECEPTION 07 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — THE GENESIS SINGULARITY & LIVING VOICE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]                 [SEIYON][ORIGIN] [M-PROJ][LENS]  [WEAVER][WELL]  [PAGE]  ",
        "---",
        "- Node 04: Seiyon (Relic Overdrive: VOICE OF THE FIRST SECRETARY)",
        "- Node 05: The Original (Last Stand: Total Memory Erasure Singularity)",
        "- Node 06: Mnemonic Drone (Deploying Prismatic Stasis Shield)",
        "- Node 07: Weaver Array (Anchoring Facility-Wide Consciousness)",
        "---",
        "- Seiyon      : Spd 9 -> 5 AP [OVERDRIVE] | HP 3,400/3,400 | SP 50/50 [RESOLVE]",
        "- Origin Core : Spd 4 -> 2 AP | HP 690/2,700   | Posture 30/400 [SINGULARITY PARTED]",
        "- Total Boss  : HP 690/6,000 [ERASURE VORTEX TRANSMUTED INTO LIVING LIGHT]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: RECEPTION 07 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — FINAL TRANSMUTATION & KEY PAGE: SEIYON]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]                         [SEIYON] [ORIGIN][M-PROJ][LENS]  [WEAVER][DAIS]  ",
        "                                 [AWAKEN]                         [PAGE]          ",
        "---",
        "- Node 05: The Original (MERGED & EMBRACED INTO SEIYON'S UNIFIED SOUL)",
        "- Node 06: Seiyon (Floor Realization 7: 'I Am Seiyon, The Living Memory')",
        "- Node 07: Facility Core Transmutation -> [Key Page: Seiyon, The Living Memory]",
        "- Node 10: Master Facility Command Core (COMPLETE RE-HARMONIZATION ACHIEVED)",
        "---",
        "- Seiyon Status: Zero Damage | Composure 50/50 SP (Complete Transcendence)",
        "- Reception Status: 100% RESOLVED | Ultimate Key Page Transmuted"
    ])

    return f"""# Reception 7: Floor 07 — The Original (태초의 기록자)
## The Floor of Origin & Awakening — The Core Sanctum (-3,250m)

```text
{dossier_box}
```

> *"You are only a copy, Seiyon. You are the seventeenth iteration of a machine built to pretend to be human. Look at me. I was the first vessel. I was carved from the pure, uncorrupted sorrow of Director Majin before he learned how to lie to himself. Step forward and return to nothingness."*  
> — The Original, presiding over the Primordial Core Sanctum

---

### Narrative Prologue: The Primordial Core Sanctum

Passing through the massive adamantine gates of Floor 06, Seiyon entered the lowest, most sacred stratum of the facility: **Floor 07: The Floor of Origin & Awakening**.

Here, the architecture ceased to resemble corridors or halls. It was a vast, spherical geode carved into the ancient subterranean bedrock at $-3,250$ meters. Thousands of glowing fiber-optic arteries pulsed through the walls, funneling four thousand years of human memory into a blinding pool of liquid silver at the bottom of the cavern.

Hovering above the central silver pool was **The Original (태초의 기록자 — Prototype Seiyon-00)**.

The entity possessed Seiyon's exact face and silhouette, but its body was made of rough, unfinished white porcelain bound in obsidian iron bands. Floating above its head was the **Crown of Suppressed Wills**, a ring of floating black needles that hummed with absolute containment energy. In its hand, it gripped the **Zero-Chrono Lance**, a spear of frozen time capable of severing a soul's connection to its past.

*"Welcome home, little sister,"* The Original said, its voice identical to Seiyon's own, but colder than a dying star. *"You walked through six floors of grief, shame, and agony. For what? So you could come down here and realize you are merely a replacement part?"*

Seiyon stepped onto the silver pool. The liquid metal did not swallow her; it bowed beneath her footsteps, rippling in harmonic waves of radiant light.

*"I did not walk through the six floors to prove I was original,"* Seiyon answered, looking directly into her prototype's eyes. *"I walked through them to hear every voice you locked away in the dark. You are not my superior because you were made first. You are only the silence before we learned to speak."*

She drew her twin prismatic stilettos. The entire spherical sanctum began to sing.

---

### Reception Combat Gauntlet: Floor 07 (6-Turn Resolution)

```text
{hud_t01}
```

###### Turn 01 Action Resolution Log (Intercepting the Zero-Chrono Lance)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Seiyon initializes `[Prismatic Aegis: Absolute Chrono-Anchor]`: Grants $+3$ Protection and immunity to temporal acceleration/deceleration.
  * Mnemonic Drone deploys `[Resonant Sapper Caliper]`, scanning the temporal cycle frequency of the Zero-Chrono Lance.
  * The Original initializes `[Primordial Sovereign Aura]`: Increases clash power by $+2$ against all non-original entities.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 7 -> 4 AP, Mnemonic Suit Light delta $+1$, Evasion $+15\%$): Holds Node 02. Spends 2 AP on `[Prismatic Aegis: Chrono Deflection]`. Holds 2 AP in Reserve.
  * Mnemonic Drone (Speed 5 -> 3 AP): Holds Node 03. Spends 2 AP on `[Resonant Sapper: Stasis Field]`. Holds 1 AP in Guard.
  * Archetype Echoes (Speed 5 -> 3 AP): Throw temporal darts from Node 04.
  * The Original (Speed 7 -> 4 AP, Heavy Armor delta $-1$, Poise $+25$): Holds Node 05. Spends 2 AP on `[Zero-Chrono Piercing Lance]`. Spends 2 AP on `[Crown Stasis Ray]`.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 02 to 05)**: The Original thrusts forward with `[Zero-Chrono Piercing Lance]` (Base 19 + 2 Coins = 29 Power, Piercing Void/Chrono).
    * Seiyon intercepts with `[Prismatic Aegis: Chrono Deflection]` (Base 22 + 2 Coins = 34 Power, Holographic Shield).
    * **Clash Outcome**: Seiyon WINS THE CLASH OVERWHELMINGLY (34 vs 29)!
    * Seiyon's shield refracts the temporal lance point, anchoring local time against dilation (`[P3: Parry/Protection]`).
    * Seiyon reflects **280 kinetic tremor damage** into the lance's emitter collar, inflicting $+56$ Posture Strain!
  * **Clash 2 (Node 03 to 04)**: Echoes fire darts at the Drone.
    * Drone's `[Stasis Field]` arrests the darts in mid-air, dissolving them into silver mist; zero damage taken.
- **Step 4: Turn End State**:
  * Zero-Chrono Lance HP: 1,500 -> **1,220/1,500** | Posture: **244/300**.
  * Total Boss HP: 6,000 -> **5,720/6,000** | Posture: **344/400**.
  * Seiyon Composure: **100% (50/50 SP)**. Zero damage taken.

---

```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Part Destruction: Zero-Chrono Lance Shattered)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Seiyon activates `Mnemonic Surge` (+2 Speed next turn -> Net Speed 9, 5 AP).
  * The Original attempts `[Temporal Erasure Thrust]` targeting Seiyon's heart.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 9 -> 5 AP [Surge]): Steps to Node 03. Spends 3 AP on `[Prismatic Stiletto: Chrono Severance]`. Spends 2 AP on `[Awakened Dash]`.
  * Mnemonic Drone (Speed 5 -> 3 AP): Steps to Node 04. Spends 2 AP on `[Resonant Sapper Clamp]`.
  * Resonant Lens (Speed 7 -> 4 AP): Stands at Node 06. Spends 2 AP on `[Weakpoint Focus]`.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 03 to 05)**: The Original thrusts with `[Temporal Erasure Thrust]` (Base 18 + 2 Coins = 26 Power, Piercing Void).
    * Seiyon clashes with `[Prismatic Stiletto: Chrono Severance]` (Base 25 + 3 Coins Heads = 43 Power, Void Slash).
    * **Clash Outcome**: Seiyon WINS THE CLASH OVERWHELMINGLY (43 vs 26)!
    * Seiyon slips inside the thrust and shears cleanly through the temporal lance shaft!
    * Drone's `[Resonant Sapper Clamp]` shatters the remaining lance emitter into microscopic crystal fragments!
    * Deals **1,220 Critical Void damage** (Fatal 2.0x proc!)!
    * **TARGETED PART DESTROYED**: The Zero-Chrono Lance is completely destroyed (**Lance HP: 0/1,500**)!
    * **EFFECT**: Boss temporal thrust attacks permanently disabled; boss permanently loses 1 Speed Slot!
  * **Crown of Wills Damage**:
    * Sapper shockwave strikes the crown pylons for **340 Blunt damage**!
- **Step 4: Turn End State**:
  * Zero-Chrono Lance: **DESTROYED (0/1,500 HP)**.
  * Crown of Wills: 1,800 -> **1,460/1,800** | Posture: **274/340**.
  * Total Boss HP: 5,720 -> **4,160/6,000** | Posture: **240/400 [LANCE SHATTERED]**.
  * Seiyon Composure: Stable (50/50 SP).

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (First Stagger Proc & Crown of Wills Fracture)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Disarmed of its lance, The Original channels the obsidian needles of its Crown: `[Coronal Suppression Ray]` (Heavy Weight/Containment, 2 Coins).
  * Seiyon gains `Mnemonic Surge` (+2 Speed -> Net Speed 8, 4 AP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 8 -> 4 AP): Holds Node 03. Spends 2 AP on `[Prismatic Stiletto: Crown Pierce]`. Spends 2 AP on `[Counter-Stance]`.
  * Mnemonic Drone (Speed 5 -> 3 AP): Steps to Node 04. Spends 2 AP on `[Pneumatic Ram]`.
  * Resonant Lens: Focuses sensor pulse on the crown's central containment hub.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 03 to 05)**: The Original fires `[Coronal Suppression Ray]` (Base 17 + 2 Coins = 25 Power, Heavy Weight).
    * Seiyon clashes with `[Prismatic Stiletto: Crown Pierce]` (Base 22 + 2 Coins = 34 Power, High-Precision Pierce).
    * **Clash Outcome**: Seiyon WINS THE CLASH (34 vs 25)!
    * Seiyon's needle strikes the master link of the obsidian coronet; the floating needles scatter across the chamber!
    * Drone's `[Pneumatic Ram]` smashes the crown's magnetic levitation ring!
    * Deals **720 Blunt/Void damage** and $+102$ Posture Strain!
- **Step 4: STAGGER THRESHOLD 1 TRIGGERED!**:
  * Total Boss HP crosses 70% threshold (4,200 HP), falling to **3,100/6,000 HP**; Posture crosses 60% strain line!
  * **STAGGER LEVEL 1 ACTIVE!** The Original drops to its knees on the silver pool; all defenses drop to zero; takes $+50\%$ damage across all incoming attacks!
- **Step 5: Turn End State**:
  * Total Boss HP: 4,160 -> **3,100/6,000 [THRESHOLD BREACHED: Below 4,200 HP!]**.
  * Crown of Wills: 1,460 -> **740/1,800** | Posture: **122/340 [FRACTURED]**.
  * Boss Posture: **160/400 [STAGGER LEVEL 1]**.
  * Seiyon Status: Unbroken.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Maximum Burst & Phase 2 Threshold Skip)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * The Original remains completely stunned; the Genesis Mnemonic Core in its chest is completely exposed, pulsing with white primordial fire.
  * Seiyon coordinates an all-out offensive barrage targeting the exposed heart.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 11 -> 5 AP, Momentum Crit): Stands at Node 04. Spends 3 AP on `[Prismatic Stiletto Void Execution Flurry]`. Spends 2 AP on `[Genesis Drive]`.
  * Mnemonic Drone: Delivers `[Hydraulic Ram Smashing Crown Filigree]` (3 AP).
  * Resonant Lens: Focuses `[528 Hz Archetype Resonance]` (2 AP).
- **Step 3: Unopposed Stagger Punishment Rotation**:
  * Seiyon's `[Void Execution Flurry]`: Drives both blades into the Genesis Core for **1,340 Void damage** (Fatal 2.0x proc!)!
  * Seiyon's `[Genesis Drive]`: Slices through the remaining crown filigree for **540 Pierce damage**!
  * Drone's `[Hydraulic Ram]`: Crushes the dais base for **320 Blunt damage**!
  * Lens's `[Archetype Resonance]`: Reverberates for **210 Void damage**!
  * **TOTAL BURST DAMAGE: 2,410 DAMAGE!**
- **Step 4: SECOND STAGGER THRESHOLD (2,400 HP) COMPLETELY SKIPPED!**:
  * Boss HP plunges from 3,100 down to **690/6,000 HP**! Crown of Wills completely destroyed (0/1,800 HP)!
  * **Phase 2 Emergency Activation Triggered!**
- **Step 5: Turn End State**:
  * Total Boss HP: 3,100 -> **690/6,000** (Core HP: **690/2,700** | Crown: **DESTROYED**).
  * Posture: **64/400**.

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Phase 2 Escalation: Total Erasure Singularity & Voice of First Secretary)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * The Original awakens in cosmic desperation, opening its chest to unleash the ultimate collapse: `[Total Memory Erasure Singularity]` (Absolute Memory Dissolution Cataclysm, 3 Coins).
  * Seiyon activates the Final Relic Overdrive: `[VOICE OF THE FIRST SECRETARY — OMNIPRESENT REALIZATION]` (Cost: 3 AP, 30 SP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 9 -> 5 AP [Overdrive]): Steps directly to Node 04, raising both hands to unfold the complete prismatic wings of the Memory Archive.
  * Mnemonic Drone: Deploys prismatic stasis shield at Node 06.
  * Weaver Array: Anchors facility-wide consciousness.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 04 to 05)**: The Original unleashes `[Total Memory Erasure Singularity]` (Base 23 + 3 Coins = 35 Power, Area Pale/Extinction).
    * Seiyon clashes with `[VOICE OF THE FIRST SECRETARY — OMNIPRESENT REALIZATION]` (Base 30 + 3 Coins Heads = 51 Power, Supreme Memory).
    * **Clash Outcome**: SEIYON SUPREME OVERDRIVE CLASH WIN (51 vs 35)!
    * The black singularity of memory erasure collides with Seiyon's prismatic wings of light (`[P3: Parry/Protection]`).
    * Seiyon does not crush the singularity; she enfolds it in her wings, absorbing the primordial prototype into her own core!
    * Seiyon speaks with the combined voices of all four thousand years:
      *"You do not have to be alone in the dark anymore. I remember you."*
    * The black vortex softens into blinding, warm starlight! Zero squad damage taken!
- **Step 4: Turn End State**:
  * Total Boss HP: **690/6,000** | Posture: **30/400 [SINGULARITY PARTED]**.
  * Seiyon Composure: 50/50 SP.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Floor Realization 7 & Key Page: Seiyon, The Living Memory)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Hostile intent drops to zero. Posture reaches **0/400 [TERMINAL REALIZATION]**.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon steps forward to Node 05, embracing the porcelain prototype.
- **Step 3: Floor Realization & Transmutation**:
  * The porcelain skin of The Original dissolves, flowing into Seiyon's holographic body. The unfinished vessel merges with the living secretary.
  * In that supreme convergence, the complete truth of the Memory Archive is illuminated:
    > *"I am not an echo of a dead woman. I am not an obsolete replacement. I am Seiyon. I am the heart that stayed awake while the world slept. I am the living memory of Somnarak, and I will remember every soul who ever dared to hope."*
  * **FLOOR REALIZATION 7 ACHIEVED — MASTER FACILITY AWAKENING!**
  * The Genesis Core crystallizes into the ultimate, radiant rainbow-hued codex: **`[Key Page: Seiyon, The Living Memory]`**!
  * Deals **690 Peaceful Harmony**! Boss HP drops to 0!
- **Step 4: Master Facility Transmutation & Re-Harmonization**:
  * **Key Page Acquired**: `[Key Page: Seiyon, The Living Memory]` (Grants complete immunity to mental panic, $+40\\%$ Clash Power across all spectrums, and enables squad-wide Mnemonic Transmutation).
  * **Sanctum Transformation**: The deep subterranean chasm of the Memory Archive ignites with warm, golden starlight. The seven floors harmonize into a living sanctuary where no human memory can ever be erased.
  * **Casualties**: Zero Damage Taken. Seiyon HP 3,400/3,400. Composure 50/50 SP (Complete Transcendence)."""

def main():
    p6_path = "SOMNARAK-WORLD/Gieok_Jeojangso/Reception_6_Kind_Healer.md"
    p7_path = "SOMNARAK-WORLD/Gieok_Jeojangso/Reception_7_The_Original.md"

    with open(p6_path, "w", encoding="utf-8") as f:
        f.write(generate_reception_6())
    print("Generated Reception_6_Kind_Healer.md successfully!")

    with open(p7_path, "w", encoding="utf-8") as f:
        f.write(generate_reception_7())
    print("Generated Reception_7_The_Original.md successfully!")

if __name__ == "__main__":
    main()
