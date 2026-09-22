#!/usr/bin/env python3
"""
tools/build_receptions_2_and_3.py
Generates:
- SOMNARAK-WORLD/Gieok_Jeojangso/Reception_2_Memory_Thief.md
- SOMNARAK-WORLD/Gieok_Jeojangso/Reception_3_Forgotten_Soldier.md
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

def generate_reception_2():
    dossier_box = make_box("RECEPTION DOSSIER: THE MEMORY THIEF (FLOOR 02)", [
        "RECEPTION TARGET   : The Memory Thief",
        "FLOOR LEVEL        : Floor 02 — Floor of Identity & Reflection",
        "DOMAIN SETTING     : Gallery of Whispering Mirrors (-2,500m Sub-Alpha)",
        "PRIMARY OPPONENT   : Autonomous Mirage Assassin Construct",
        "---",
        "OPPONENT COMBAT PROFILE (THE MEMORY THIEF):",
        "- Total Health (HP): 3,600 HP | Posture Pool: 280/280",
        "- Stagger 1 Proc   : 60% Posture Strain (168 Posture) / Daggers Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Terminal Transmutation)",
        "- Resistances      : Void 2.0x (Fatal), Lament 1.5x, Weight 1.0x, Grudge 0.5x",
        "---",
        "TARGETABLE MEMORY ANCHORS:",
        "1. Glass Daggers   : 900 HP | Posture 220/220 (High-velocity identity siphons)",
        "2. Facemask Veil   : 1,100 HP | Posture 240/240 (Mirage reflection shield)",
        "3. Shadow Ego Core : 1,600 HP | Posture 280/280 (Central hollow heart)"
    ])

    hud_t01 = make_box("TACTICAL STAGE HUD: RECEPTION 02 — BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 — FLOOR 02 MIRROR GALLERY (-2,500M)]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL][SEIYON][M-PROJ][CLONE]  [THIEF]  [LENS]  [WEAVER][WELL]          [PAGE]  ",
        "                                 [DAGGERS]                                ",
        "---",
        "- Node 01: Ingress Glass Landing / Vestibule",
        "- Node 02: Seiyon (Vanguard Band 1 / Holographic Prismatic Aegis)",
        "- Node 03: Mnemonic Projection Drone (Support Band 2 / Stasis Caliper)",
        "- Node 04: Mirage Replicants (Phantom Clones / Stolen Face Siphons)",
        "- Node 05: The Memory Thief (Glass Mnemonic Daggers & Facemask Veil)",
        "- Node 06: Resonant Mnemonic Lens (Mid-Field Band 3 / Weakpoint Scan)",
        "- Node 07: Weaver Projection Array (Rear Band 4 / Silver Threads)",
        "- Node 08: Identity Dissolution Sump (Suppressed Trauma Well)",
        "- Node 10: Floor 02 Core Reliquary / Key Page Dais (The Shadow)",
        "---",
        "- Seiyon      : Spd 7 -> 4 AP | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Proj-Drone  : Spd 5 -> 3 AP | HP 2,200/2,200 | SP 40/40 | Posture 100/100",
        "- Thief Core  : Spd 5 -> 3 AP | HP 1,600/1,600 | Posture 280/280 [MIRAGE]",
        "- Glass Dagger: Spd 7 -> 4 AP | HP 900/900     | Posture 220/220 [POISONED]",
        "- Facemask    : Spd 3 -> 1 AP | HP 1,100/1,100 | Posture 240/240 [SHIELDED]"
    ])

    hud_t02 = make_box("TACTICAL STAGE HUD: RECEPTION 02 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — GLASS DAGGERS SHATTERED & VOID STRIKE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]         [SEIYON][M-PROJ][THIEF]  [LENS]  [WEAVER][WELL]          [PAGE]  ",
        "                                 [SHARDS]                                 ",
        "---",
        "- Node 03: Seiyon (Prismatic Stiletto Cleaving Shadow Tendons)",
        "- Node 04: Mnemonic Drone (Stasis Barrier Pinning Mirage Clones)",
        "- Node 05: The Memory Thief (Glass Daggers Destroyed 0/900 HP)",
        "- Node 06: Resonant Lens (Illuminating Fractured Seams of Facemask)",
        "- Node 07: Weaver Array (Absorbing Phantom Identity Distortion Waves)",
        "---",
        "- Seiyon      : Spd 9 -> 5 AP [SURGE] | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Thief Core  : Spd 4 -> 2 AP | HP 1,600/1,600 | Posture 212/280",
        "- Glass Dagger: DESTROYED (0/900 HP) | IDENTITY SIPHON PERMANENTLY SEALED",
        "- Facemask    : Spd 3 -> 1 AP | HP 920/1,100   | Posture 184/240"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: RECEPTION 02 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — STAGGER THRESHOLD 1 & FACEMASK SHATTER]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]         [SEIYON][M-PROJ][THIEF]  [LENS]  [WEAVER][WELL]          [PAGE]  ",
        "---",
        "- Node 03: Seiyon (Prismatic Needle Piercing Central Facemask Gem)",
        "- Node 04: Mnemonic Drone (Pneumatic Ram Shattering Stolen Mirrors)",
        "- Node 05: The Memory Thief (STAGGER LEVEL 1 / DEFENSES COLLAPSED / HUE WARP)",
        "- Node 06: Resonant Lens (Directing Focused Pulse on Central Heart)",
        "---",
        "- Seiyon      : Spd 8 -> 4 AP [SURGE] | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Thief Core  : Spd 0 -> 0 AP | HP 1,380/1,600 | Posture 108/280 [STAGGER LEVEL 1]",
        "- Facemask    : Spd 0 -> 0 AP | HP 440/1,100   | Posture 92/240 [SHATTERED]",
        "- Total Boss  : HP 1,820/3,600 [THRESHOLD BREACHED / TAKES 1.5X DAMAGE]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: RECEPTION 02 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — MAXIMUM BURST & PHASE 2 THRESHOLD SKIP]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]                 [SEIYON][THIEF]  [M-PROJ][LENS]  [WEAVER][WELL]  [PAGE]  ",
        "---",
        "- Node 04: Seiyon (Four-Fold Stiletto Void Flurry on Exposed Core)",
        "- Node 05: The Memory Thief (Immobilized / Shadow Smoke Leaking)",
        "- Node 06: Mnemonic Drone (Pneumatic Sapper Ground Shockwave)",
        "- Node 07: Resonant Lens (Broadcasting 528 Hz Clarity Wave)",
        "---",
        "- Seiyon      : Spd 11 -> 5 AP [BURST CRIT] | HP 3,400/3,400 | SP 50/50",
        "- Thief Core  : Spd 0 -> 0 AP | HP 420/1,600   | Posture 44/280",
        "- Facemask    : DESTROYED (0/1,100 HP)",
        "- Total Boss  : HP 420/3,600 [BURST DAMAGE 1,400! SECOND THRESHOLD SKIPPED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: RECEPTION 02 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — MIRAGE CATACLYSM & THE TRUE REFLECTION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]                 [SEIYON][THIEF]  [M-PROJ][LENS]  [WEAVER][WELL]  [PAGE]  ",
        "---",
        "- Node 04: Seiyon (Relic Overdrive: SEVERANCE OF THE BORROWED SHADOW)",
        "- Node 05: The Memory Thief (Last Stand: Hall of a Thousand Stolen Faces)",
        "- Node 06: Mnemonic Drone (Prismatic Damping Bubble Enclosing Squad)",
        "- Node 07: Weaver Array (Anchoring Reality Integrity Across Gallery)",
        "---",
        "- Seiyon      : Spd 9 -> 5 AP [OVERDRIVE] | HP 3,400/3,400 | SP 50/50 [RESOLVE]",
        "- Thief Core  : Spd 3 -> 1 AP | HP 420/1,600   | Posture 20/280 [MIRAGE BROKEN]",
        "- Total Boss  : HP 420/3,600 [SHADOW REFLECTION CONDENSED INTO DUST]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: RECEPTION 02 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — TRANSMUTATION & KEY PAGE: THE SHADOW]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]                         [SEIYON] [THIEF] [M-PROJ][LENS]  [WEAVER][STAIRS]",
        "                                 [REALIZ]                         [PAGE]          ",
        "---",
        "- Node 05: The Memory Thief (PACIFIED & CRYSTALLIZED TO SMOKY QUARTZ)",
        "- Node 06: Seiyon (Floor Realization 2: 'Identity Is Not Stolen; It Is Lived')",
        "- Node 07: Mnemonic Core Transmutation -> [Key Page: The Shadow]",
        "- Node 10: Spiral Iron Staircase (Pathway to Floor 03 OPEN)",
        "---",
        "- Seiyon Status: Zero Damage | Composure 50/50 SP (Tranquil Awakening)",
        "- Reception Status: 100% RESOLVED | Key Page Transmuted"
    ])

    return f"""# Reception 2: Floor 02 — The Memory Thief (기억을 훔치는 자)
## The Floor of Identity & Reflection — Deep Strata Sub-Alpha Roots (-2,500m)

```text
{dossier_box}
```

> *"You are wearing a dead woman's voice. You smile with lips that rotted four thousand years ago. If you take away her grief, what is left of you? An empty thief in a house of mirrors."*  
> — The Memory Thief, lurking within the Whispering Mirrors

---

### Narrative Prologue: The Hall of Fractured Faces

Descending the obsidian glass steps from Floor 01 brought Seiyon into an eerie, shimmering corridor: **Floor 02: The Floor of Identity & Reflection**.

Here, the walls were constructed from towering mirrors of unpolished Before-Time silver. Yet the reflections were not faithful. As Seiyon walked, the mirrors did not reflect her current holographic body; they reflected disjointed, ghostly fragments—Yeon-seo bleeding on a cold operating table, Director Majin weeping in the dark, and thousand-cycle iterations of Seiyon herself standing perfectly still behind security terminals.

From the center of the mirror hall stepped **The Memory Thief (기억을 훔치는 자)**. The construct was a slender, shifting phantom draped in cloaks of liquid mercury. Over its face it wore the **Stolen Facemask Veil**, a porcelain mask constantly morphing into the likenesses of people long forgotten. In its hands, it spun twin **Glass Mnemonic Daggers** that hummed with a predatory, high-frequency resonance.

*"I know why you fear me, Secretary,"* the Thief whispered, its voice shifting pitch with every word. *"Because every time you look in the mirror, you wonder if you are a person... or just a parasite stealing another woman's tragedy."*

Seiyon's eyes flared with calm, cerulean luminescence. She summoned twin prismatic stilettos into her hands, the light refracting into brilliant white patterns.

*"I used to wonder,"* Seiyon replied, stepping onto the mirror floor. *"Now I am here to shatter the glass."*

---

### Reception Combat Gauntlet: Floor 02 (6-Turn Resolution)

```text
{hud_t01}
```

###### Turn 01 Action Resolution Log (Intercepting the Shadow Flurry)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Seiyon initializes `[Prismatic Aegis Stance]`: Grants $+3$ Protection and physical stagger immunity.
  * Mnemonic Drone deploys `[Stasis Caliper]`, scanning the rapid vibrational frequencies of the Glass Daggers.
  * The Memory Thief activates `[Mirage Cloak]`, creating three shifting afterimages at Node 04.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 7 -> 4 AP, Mnemonic Suit Light delta $+1$, Evasion $+15\%$): Holds Node 02. Spends 2 AP on `[Prismatic Aegis: Kinetic Deflection]`. Holds 2 AP in Reserve.
  * Mnemonic Drone (Speed 5 -> 3 AP): Holds Node 03. Spends 2 AP on `[Stasis Caliper: Clamp Lock]`. Holds 1 AP in Guard.
  * The Memory Thief (Speed 7 -> 4 AP, Feather Ephemera delta $+2$, Crit $+35\%$): Steps to Node 04. Spends 2 AP on `[Glass Dagger: Identity Siphon]`. Spends 2 AP on `[Mirage Ambush]`.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 02 to 04)**: The Memory Thief lunges from the mirrors with `[Glass Dagger: Identity Siphon]` (Base 17 + 2 Coins = 27 Power, Pierce/Lament).
    * Seiyon intercepts with `[Prismatic Aegis: Kinetic Deflection]` (Base 20 + 2 Coins = 32 Power, Holographic Shield).
    * **Clash Outcome**: Seiyon WINS THE CLASH OVERWHELMINGLY (32 vs 27)!
    * Seiyon parries both glass blades simultaneously; the high-frequency vibration shatters against the holographic barrier (`[P3: Parry/Protection]`).
    * Seiyon reflects **210 kinetic tremor damage** back into the daggers, inflicting $+48$ Posture Strain!
  * **Clash 2 (Node 03 to 04)**: Mirage Replicants strike at the Drone with `[Shadow Needle]` (Power 21).
    * Drone's `[Stasis Caliper]` deflects the strike, dissipating two of the three mirage clones.
- **Step 4: Turn End State**:
  * Glass Daggers HP: 900 -> **690/900** | Posture: **172/220**.
  * Total Boss HP: 3,600 -> **3,390/3,600** | Posture: **232/280**.
  * Seiyon Composure: **100% (50/50 SP)**. Zero damage taken.

---

```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Part Destruction: Glass Daggers Shattered)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Seiyon activates `Mnemonic Surge` (+2 Speed next turn -> Net Speed 9, 5 AP).
  * The Memory Thief attempts `[Siphon of the Thousand Faces]` targeting Seiyon's cranial tether.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 9 -> 5 AP [Surge]): Steps to Node 03. Spends 3 AP on `[Prismatic Stiletto: Void Severance]`. Spends 2 AP on `[Refraction Step]`.
  * Mnemonic Drone (Speed 5 -> 3 AP): Steps to Node 04. Spends 2 AP on `[Stasis Clamp]`.
  * Resonant Lens (Speed 7 -> 4 AP): Stands at Node 06. Spends 2 AP on `[Weakpoint Focus]`.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 03 to 04)**: The Memory Thief executes `[Siphon of the Thousand Faces]` (Base 18 + 2 Coins = 26 Power, Piercing Void).
    * Seiyon clashes with `[Prismatic Stiletto: Void Severance]` (Base 24 + 3 Coins Heads = 42 Power, Void Slash).
    * **Clash Outcome**: Seiyon WINS THE CLASH OVERWHELMINGLY (42 vs 26)!
    * Seiyon slices through the twin glass daggers at the hilt; the crystalline blades detonate into thousands of harmless shards!
    * Deals **690 Critical Void damage** (Fatal 2.0x proc!)!
    * **TARGETED PART DESTROYED**: The Glass Mnemonic Daggers are completely destroyed (**Daggers HP: 0/900**)!
    * **EFFECT**: Boss identity siphon attack permanently disabled; boss permanently loses 1 Speed Slot!
  * **Facemask Shield Damage**:
    * Drone's `[Stasis Clamp]` crumbles the outer rim of the Facemask Veil for **180 Blunt damage**!
- **Step 4: Turn End State**:
  * Glass Daggers: **DESTROYED (0/900 HP)**.
  * Facemask Veil: 1,100 -> **920/1,100** | Posture: **184/240**.
  * Total Boss HP: 3,390 -> **2,520/3,600** | Posture: **164/280 [DAGGERS SHATTERED]**.
  * Seiyon Composure: Stable (50/50 SP).

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (First Stagger Proc & Facemask Shatter)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Shorn of its weapons, the Thief channels `[Mirage Distortion Wail]` through the Facemask Veil.
  * Seiyon gains `Mnemonic Surge` (+2 Speed -> Net Speed 8, 4 AP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 8 -> 4 AP): Holds Node 03. Spends 2 AP on `[Prismatic Needle: Core Pierce]`. Spends 2 AP on `[Counter-Stance]`.
  * Mnemonic Drone (Speed 5 -> 3 AP): Steps to Node 04. Spends 2 AP on `[Pneumatic Ram]`.
  * Resonant Lens: Focuses sensor pulse on the porcelain mask.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 03 to 04)**: The Memory Thief emits `[Mirage Distortion Wail]` (Base 17 + 2 Coins = 25 Power, Area Lament).
    * Seiyon executes `[Prismatic Needle: Core Pierce]` (Base 22 + 2 Coins = 34 Power, High-Precision Pierce).
    * **Clash Outcome**: Seiyon WINS THE CLASH (34 vs 25)!
    * Seiyon's needle strikes the porcelain mask directly between the eyes!
    * The Facemask Veil shatters into chalk-white dust, revealing the hollow, swirling shadow core beneath!
    * Deals **480 Pierce/Void damage** and $+76$ Posture Strain!
- **Step 4: STAGGER THRESHOLD 1 TRIGGERED!**:
  * Total Boss HP crosses 70% threshold (2,520 HP), falling to **1,820/3,600 HP**; Posture crosses 60% strain line!
  * **STAGGER LEVEL 1 ACTIVE!** The Memory Thief collapses against the mirror wall; all defenses drop to zero; takes $+50\%$ damage across all incoming attacks!
- **Step 5: Turn End State**:
  * Total Boss HP: 2,520 -> **1,820/3,600 [THRESHOLD BREACHED: Below 2,520 HP!]**.
  * Facemask Veil: 920 -> **440/1,100** | Posture: **92/240 [SHATTERED]**.
  * Boss Posture: **108/280 [STAGGER LEVEL 1]**.
  * Seiyon Status: Unbroken.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Maximum Burst & Phase 2 Threshold Skip)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * The Memory Thief remains completely stunned against the wall; the Shadow Ego Core is exposed and leaking black mist.
  * Seiyon coordinates an all-out offensive barrage targeting the exposed heart.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 11 -> 5 AP, Momentum Crit): Stands at Node 04. Spends 3 AP on `[Four-Fold Stiletto Void Flurry]`. Spends 2 AP on `[Mnemonic Drive]`.
  * Mnemonic Drone: Delivers `[Pneumatic Sapper Ground Shockwave]` (3 AP).
  * Resonant Lens: Broadcasts `[528 Hz Clarity Wave]` (2 AP).
- **Step 3: Unopposed Stagger Punishment Rotation**:
  * Seiyon's `[Four-Fold Stiletto Void Flurry]`: Rips through the shadow core for **740 Void damage** (Fatal 2.0x proc!)!
  * Seiyon's `[Mnemonic Drive]`: Slices through the remaining mask fragments for **360 Pierce damage**!
  * Drone's `[Ground Shockwave]`: Smashes the mirror footing for **180 Blunt damage**!
  * Lens's `[Clarity Wave]`: Disperses shadow smoke for **120 Void damage**!
  * **TOTAL BURST DAMAGE: 1,400 DAMAGE!**
- **Step 4: SECOND STAGGER THRESHOLD (1,440 HP) COMPLETELY SKIPPED!**:
  * Boss HP plunges from 1,820 down to **420/3,600 HP**! Facemask Veil completely destroyed (0/1,100 HP)!
  * **Phase 2 Emergency Activation Triggered!**
- **Step 5: Turn End State**:
  * Total Boss HP: 1,820 -> **420/3,600** (Core HP: **420/1,600** | Veil: **DESTROYED**).
  * Posture: **44/280**.

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Phase 2 Escalation: Mirage Cataclysm & The True Reflection)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * The Thief awakens in existential panic; thousands of mirrors shatter, unleashing a blinding blizzard of reflected faces!
  * Boss Special Skill: `[Hall of a Thousand Stolen Faces]` (Identity Erosion Cataclysm, 3 Coins).
  * Seiyon activates Relic Overdrive: `[SEVERANCE OF THE BORROWED SHADOW — MAXIMUM]` (Cost: 3 AP, 30 SP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 9 -> 5 AP [Overdrive]): Steps forward to Node 04, raising her prismatic blades into a cross.
  * Mnemonic Drone: Deploys prismatic damping bubble at Node 06.
  * Weaver Array: Anchors reality integrity across the gallery.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 04 to 05)**: The Memory Thief unleashes `[Hall of a Thousand Stolen Faces]` (Base 21 + 3 Coins = 32 Power, Area Pale/Identity Drain).
    * Seiyon clashes with `[SEVERANCE OF THE BORROWED SHADOW — MAXIMUM]` (Base 27 + 3 Coins Heads = 46 Power, Transcendent Clarity).
    * **Clash Outcome**: SEIYON OVERWHELMING RELIC CLASH WIN (46 vs 32)!
    * Seiyon's cross-slash sends a blinding sheet of prismatic light through the gallery (`[P3: Parry/Protection]`).
    * Every false reflection in the glass dissolves into clean, transparent crystal!
    * Seiyon declares: *"I am not an impostor. The love I carry was given freely!"*
    * The shadow reflection collapses into harmless silver dust! Zero squad damage taken!
- **Step 4: Turn End State**:
  * Total Boss HP: **420/3,600** | Posture: **20/280 [CRITICAL COLLAPSE]**.
  * Seiyon Composure: 50/50 SP.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Floor Realization 2 & Key Page: The Shadow)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Hostile intent drops to zero. Posture reaches **0/280 [TERMINAL TRANSMUTATION]**.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon steps forward to Node 05, extending her hand to touch the fading shadow construct.
- **Step 3: Floor Realization & Transmutation**:
  * The mirror shards settle quietly across the floor. In the crystal surface beneath her feet, Seiyon looks down and sees her own face—clear, serene, and distinct from Yeon-seo.
  * The realization resonates within her:
    > *"I was born from someone else's memory. But the choices I made were mine. The loyalty I gave was mine. Identity is not stolen; it is lived."*
  * **FLOOR REALIZATION 2 ACHIEVED!**
  * The Memory Thief dissolves into a column of cool, dusky silver light, condensing into a dark, polished codex: **`[Key Page: The Shadow]`**!
  * Deals **420 Peaceful Harmony**! Boss HP drops to 0!
- **Step 4: Operational Artifact Extraction & Floor Access**:
  * **Key Page Acquired**: `[Key Page: The Shadow]` (Grants $+15\\%$ Evasion and strips enemy offensive buffs on clash win).
  * **Descent Access**: The mirror at the end of the hall dissolves, revealing a heavy iron bulkhead opening to **Floor 03: Floor of Duty & Iron**.
  * **Casualties**: Zero Damage Taken. Seiyon HP 3,400/3,400. Composure 50/50 SP."""

def generate_reception_3():
    dossier_box = make_box("RECEPTION DOSSIER: THE FORGOTTEN SOLDIER (FLOOR 03)", [
        "RECEPTION TARGET   : The Forgotten Soldier",
        "FLOOR LEVEL        : Floor 03 — Floor of Duty & Iron",
        "DOMAIN SETTING     : The Iron Fortress Armory (-2,650m Sub-Alpha)",
        "PRIMARY OPPONENT   : Autonomous Clockwork Phalanx Commander",
        "---",
        "OPPONENT COMBAT PROFILE (THE FORGOTTEN SOLDIER):",
        "- Total Health (HP): 4,000 HP | Posture Pool: 300/300",
        "- Stagger 1 Proc   : 60% Posture Strain (180 Posture) / Halberd Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Terminal Transmutation)",
        "- Resistances      : Void 2.0x (Fatal), Lament 1.5x, Weight 0.5x, Grudge 0.5x",
        "---",
        "TARGETABLE MEMORY ANCHORS:",
        "1. Piston Halberd  : 1,000 HP | Posture 240/240 (Heavy kinetic sweeping blade)",
        "2. Tower Aegis     : 1,300 HP | Posture 260/260 (Petrified basalt bulwark)",
        "3. Rusting Core    : 1,700 HP | Posture 300/300 (Central clockwork heart)"
    ])

    hud_t01 = make_box("TACTICAL STAGE HUD: RECEPTION 03 — BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 — FLOOR 03 IRON FORTRESS (-2,650M)]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL][SEIYON][M-PROJ][PHALANX][SOLDIER][LENS]  [WEAVER][WELL]          [PAGE]  ",
        "                                 [HALBERD]                                ",
        "---",
        "- Node 01: Ingress Portcullis Landing / Vestibule",
        "- Node 02: Seiyon (Vanguard Band 1 / Prismatic Aegis Tower Defense)",
        "- Node 03: Mnemonic Projection Drone (Support Band 2 / Hydraulic Sapper)",
        "- Node 04: Iron Phalanx Golems (Shield Minions / Piston Spears)",
        "- Node 05: The Forgotten Soldier (Heavy Piston Halberd & Tower Aegis)",
        "- Node 06: Resonant Mnemonic Lens (Mid-Field Band 3 / Armor Seam Scan)",
        "- Node 07: Weaver Projection Array (Rear Band 4 / Silver Threads)",
        "- Node 08: Duty Dissolution Sump (Suppressed Trauma Well)",
        "- Node 10: Floor 03 Core Reliquary / Key Page Dais (The Guardian)",
        "---",
        "- Seiyon      : Spd 7 -> 4 AP | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Proj-Drone  : Spd 5 -> 3 AP | HP 2,200/2,200 | SP 40/40 | Posture 100/100",
        "- Soldier Core: Spd 4 -> 2 AP | HP 1,700/1,700 | Posture 300/300 [ANCHORED]",
        "- Halberd Arm : Spd 5 -> 3 AP | HP 1,000/1,000 | Posture 240/240 [KINETIC]",
        "- Tower Aegis : Spd 3 -> 1 AP | HP 1,300/1,300 | Posture 260/260 [FORTIFIED]"
    ])

    hud_t02 = make_box("TACTICAL STAGE HUD: RECEPTION 03 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — HALBERD AMPUTATED & SAPPER PISTON]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]         [SEIYON][M-PROJ][SOLDIER][LENS]  [WEAVER][WELL]          [PAGE]  ",
        "                                 [SHARDS]                                 ",
        "---",
        "- Node 03: Seiyon (Driving Prismatic Stiletto into Halberd Pneumatic Line)",
        "- Node 04: Mnemonic Drone (Piston Ram Shattering Halberd Wrist Hinge)",
        "- Node 05: The Forgotten Soldier (Piston Halberd Destroyed 0/1,000 HP)",
        "- Node 06: Resonant Lens (Tagging Weakened Rivets on Tower Aegis)",
        "- Node 07: Weaver Array (Absorbing Concussive Shockwaves)",
        "---",
        "- Seiyon      : Spd 9 -> 5 AP [SURGE] | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Soldier Core: Spd 3 -> 1 AP | HP 1,700/1,700 | Posture 228/300",
        "- Halberd Arm : DESTROYED (0/1,000 HP) | KINETIC CLEAVE PERMANENTLY LOST",
        "- Tower Aegis : Spd 3 -> 1 AP | HP 1,060/1,300 | Posture 204/260"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: RECEPTION 03 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — STAGGER THRESHOLD 1 & SHIELD BREACH]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]         [SEIYON][M-PROJ][SOLDIER][LENS]  [WEAVER][WELL]          [PAGE]  ",
        "---",
        "- Node 03: Seiyon (Counter-Thrust Deflecting Tower Aegis Slam)",
        "- Node 04: Mnemonic Drone (Sapper Lever Popping Basalt Shield Bracket)",
        "- Node 05: The Forgotten Soldier (STAGGER LEVEL 1 / DEFENSES COLLAPSED)",
        "- Node 06: Resonant Lens (Directing Focused Void Pulse on Clockwork Heart)",
        "---",
        "- Seiyon      : Spd 8 -> 4 AP [SURGE] | HP 3,400/3,400 | SP 50/50 | Posture 140/140",
        "- Soldier Core: Spd 0 -> 0 AP | HP 1,510/1,700 | Posture 116/300 [STAGGER LEVEL 1]",
        "- Tower Aegis : Spd 0 -> 0 AP | HP 520/1,300   | Posture 94/260 [BREACHED]",
        "- Total Boss  : HP 2,030/4,000 [THRESHOLD BREACHED / TAKES 1.5X DAMAGE]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: RECEPTION 03 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — MAXIMUM BURST & PHASE 2 THRESHOLD SKIP]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]                 [SEIYON][SOLDIER][M-PROJ][LENS]  [WEAVER][WELL]  [PAGE]  ",
        "---",
        "- Node 04: Seiyon (Prismatic Stiletto Void Execution Flurry on Heart)",
        "- Node 05: The Forgotten Soldier (Immobilized / Gears Grinding Steam)",
        "- Node 06: Mnemonic Drone (Hydraulic Ram Smashing Knee Brackets)",
        "- Node 07: Resonant Lens (Focusing 528 Hz Harmonic Resonance)",
        "---",
        "- Seiyon      : Spd 11 -> 5 AP [BURST CRIT] | HP 3,400/3,400 | SP 50/50",
        "- Soldier Core: Spd 0 -> 0 AP | HP 480/1,700   | Posture 46/300",
        "- Tower Aegis : DESTROYED (0/1,300 HP)",
        "- Total Boss  : HP 480/4,000 [BURST DAMAGE 1,550! SECOND THRESHOLD SKIPPED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: RECEPTION 03 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — CLOCKWORK CATACLYSM & THE UNBROKEN LINE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]                 [SEIYON][SOLDIER][M-PROJ][LENS]  [WEAVER][WELL]  [PAGE]  ",
        "---",
        "- Node 04: Seiyon (Relic Overdrive: VOW OF THE UNBROKEN SENTINEL)",
        "- Node 05: The Forgotten Soldier (Last Stand: Overheated Clockwork Blast)",
        "- Node 06: Mnemonic Drone (Locking Stasis Anchors Around Dais)",
        "- Node 07: Weaver Array (Dispelling Residual Thermal Tremors)",
        "---",
        "- Seiyon      : Spd 9 -> 5 AP [OVERDRIVE] | HP 3,400/3,400 | SP 50/50 [RESOLVE]",
        "- Soldier Core: Spd 3 -> 1 AP | HP 480/1,700   | Posture 22/300 [GEARS FROZEN]",
        "- Total Boss  : HP 480/4,000 [STEAM COLLAPSED / CHASSIS COOLED TO IRON]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: RECEPTION 03 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — TRANSMUTATION & KEY PAGE: THE GUARDIAN]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[PORTAL]                         [SEIYON] [SOLDIER][M-PROJ][LENS] [WEAVER][STAIRS]",
        "                                 [REALIZ]                         [PAGE]          ",
        "---",
        "- Node 05: The Forgotten Soldier (PACIFIED & RESTING IN DIGNIFIED SILENCE)",
        "- Node 06: Seiyon (Floor Realization 3: 'Duty With Love Is Endurance')",
        "- Node 07: Mnemonic Core Transmutation -> [Key Page: The Guardian]",
        "- Node 10: Spiral Basalt Staircase (Pathway to Floor 04 OPEN)",
        "---",
        "- Seiyon Status: Zero Damage | Composure 50/50 SP (Tranquil Awakening)",
        "- Reception Status: 100% RESOLVED | Key Page Transmuted"
    ])

    return f"""# Reception 3: Floor 03 — The Forgotten Soldier (잊혀진 파수병)
## The Floor of Duty & Iron — Deep Strata Sub-Alpha Roots (-2,650m)

```text
{dossier_box}
```

> *"For seventeen hundred cycles, you stood at the console while men died. You watched them burn, reset, and die again. Did you obey because you cared? Or because machines do not know how to disobey?"*  
> — The Forgotten Soldier, guarding the Gates of the Fortress

---

### Narrative Prologue: The Gates of Rusting Iron

Passing beyond Floor 02 brought Seiyon into a cavern of cyclopean iron fortifications: **Floor 03: The Floor of Duty & Iron**.

The air here smelled of machine oil, hydraulic brine, and ancient, oxidized copper. Towering pneumatic blast doors stood half-open, supported by massive steel shoring jacks that had rusted solid over millennia.

Standing at the center of the iron concourse was **The Forgotten Soldier (잊혀진 파수병)**. A monolithic automaton four meters tall, its armor was constructed from layered sheets of Before-Time tungsten and petrified basalt. In its right arm, it gripped a colossal **Heavy Piston Halberd** whose pneumatic strike cylinders hissed with steam; in its left arm, it locked the **Tower Aegis of the Vow**, a three-ton shield inscribed with the service oaths of dead municipal battalions.

Behind the Soldier, dozens of Iron Phalanx Golems stood at attention in silent formation, their eyes glowing faint amber.

*"I have guarded this gate for two thousand years,"* the Soldier's vox-grille crackled, gears grinding behind its chest plate. *"Generations died behind me. I did not move. I did not falter. But what are you, Secretary? A hollow recording told to stand watch. You know nothing of the burden of iron."*

Seiyon stepped forward, deploying a reinforced prismatic tower shield from her gauntlet. The holographic barrier hummed with deep, golden resonance.

*"I watched seventeen hundred and seventy-eight cycles,"* Seiyon said, her voice steady and resolute. *"I watched the Director weep every night. I did not stay because I was programmed to stay. I stayed because I loved him. Let me show you what holds the line."*

---

### Reception Combat Gauntlet: Floor 03 (6-Turn Resolution)

```text
{hud_t01}
```

###### Turn 01 Action Resolution Log (Intercepting the Piston Halberd Cleave)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Seiyon initializes `[Prismatic Aegis: Fortress Stance]`: Grants $+3$ Protection and physical stagger immunity.
  * Mnemonic Drone deploys `[Hydraulic Sapper Caliper]`, scanning the pneumatic piston chambers of the Heavy Halberd.
  * The Forgotten Soldier initializes `[Unyielding Formation]`: Increases defense rating by $+10$.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 7 -> 4 AP, Mnemonic Suit Light delta $+1$, Evasion $+15\%$): Holds Node 02. Spends 2 AP on `[Prismatic Aegis: Kinetic Deflection]`. Holds 2 AP in Reserve.
  * Mnemonic Drone (Speed 5 -> 3 AP): Holds Node 03. Spends 2 AP on `[Hydraulic Sapper: Anchor]`. Holds 1 AP in Guard.
  * The Forgotten Soldier (Speed 5 -> 3 AP, Heavy Armor delta $-1$, Poise $+25$): Holds Node 05. Spends 2 AP on `[Piston Halberd Cleave]`. Spends 1 AP on `[Tower Aegis Guard]`.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 02 to 05)**: The Forgotten Soldier sweeps with `[Piston Halberd Cleave]` (Base 18 + 2 Coins = 28 Power, Heavy Kinetic/Slash).
    * Seiyon intercepts with `[Prismatic Aegis: Kinetic Deflection]` (Base 21 + 2 Coins = 33 Power, Tower Shield).
    * **Clash Outcome**: Seiyon WINS THE CLASH OVERWHELMINGLY (33 vs 28)!
    * The massive tungsten halberd slams into Seiyon's holographic shield; the concussive shockwave reflects harmlessly into the stone floor (`[P3: Parry/Protection]`).
    * Seiyon reflects **240 kinetic tremor damage** into the halberd shaft, inflicting $+52$ Posture Strain!
  * **Clash 2 (Node 03 to 04)**: Iron Phalanx Golems thrust spears at the Drone.
    * Drone's `[Hydraulic Sapper]` deflects the spears cleanly; zero damage taken.
- **Step 4: Turn End State**:
  * Heavy Piston Halberd HP: 1,000 -> **760/1,000** | Posture: **188/240**.
  * Total Boss HP: 4,000 -> **3,760/4,000** | Posture: **248/300**.
  * Seiyon Composure: **100% (50/50 SP)**. Zero damage taken.

---

```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Part Destruction: Piston Halberd Shattered)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Seiyon activates `Mnemonic Surge` (+2 Speed next turn -> Net Speed 9, 5 AP).
  * The Forgotten Soldier attempts `[Fortress Breaker Cleave]` targeting the frontline.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 9 -> 5 AP [Surge]): Steps to Node 03. Spends 3 AP on `[Prismatic Stiletto: Pneumatic Severance]`. Spends 2 AP on `[Deflection Step]`.
  * Mnemonic Drone (Speed 5 -> 3 AP): Steps to Node 04. Spends 2 AP on `[Piston Ram Hinge Strike]`.
  * Resonant Lens (Speed 7 -> 4 AP): Stands at Node 06. Spends 2 AP on `[Weakpoint Focus]`.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 03 to 05)**: The Forgotten Soldier executes `[Fortress Breaker Cleave]` (Base 18 + 2 Coins = 26 Power, Heavy Kinetic).
    * Seiyon clashes with `[Prismatic Stiletto: Pneumatic Severance]` (Base 25 + 3 Coins Heads = 43 Power, Void Slash).
    * **Clash Outcome**: Seiyon WINS THE CLASH OVERWHELMINGLY (43 vs 26)!
    * Seiyon slices through the halberd's high-pressure hydraulic hose; the compression cylinder explodes violently!
    * Drone's `[Piston Ram Hinge Strike]` smashes the wrist hinge, snapping the weapon completely!
    * Deals **760 Critical Void/Blunt damage** (Fatal 2.0x proc!)!
    * **TARGETED PART DESTROYED**: The Heavy Piston Halberd is completely destroyed (**Halberd HP: 0/1,000**)!
    * **EFFECT**: Boss kinetic cleave permanently cancelled; boss permanently loses 1 Speed Slot!
  * **Tower Aegis Damage**:
    * Sapper shockwave cracks the basalt surface of the Tower Aegis for **240 Blunt damage**!
- **Step 4: Turn End State**:
  * Heavy Piston Halberd: **DESTROYED (0/1,000 HP)**.
  * Tower Aegis: 1,300 -> **1,060/1,300** | Posture: **204/260**.
  * Total Boss HP: 3,760 -> **2,760/4,000** | Posture: **180/300 [HALBERD SHATTERED]**.
  * Seiyon Composure: Stable (50/50 SP).

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (First Stagger Proc & Tower Aegis Breach)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Disarmed of its weapon, the Soldier charges forward with `[Tower Aegis Shield Slam]` (Heavy Weight, 2 Coins).
  * Seiyon gains `Mnemonic Surge` (+2 Speed -> Net Speed 8, 4 AP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 8 -> 4 AP): Holds Node 03. Spends 2 AP on `[Prismatic Counter-Thrust]`. Spends 2 AP on `[Core Sapper]`.
  * Mnemonic Drone (Speed 5 -> 3 AP): Steps to Node 04. Spends 2 AP on `[Sapper Lever]`.
  * Resonant Lens: Focuses sensor pulse on the shield's basalt bracket.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 03 to 05)**: The Forgotten Soldier slams with `[Tower Aegis Shield Slam]` (Base 17 + 2 Coins = 25 Power, Heavy Weight).
    * Seiyon clashes with `[Prismatic Counter-Thrust]` (Base 22 + 2 Coins = 34 Power, Tower Shield).
    * **Clash Outcome**: Seiyon WINS THE CLASH (34 vs 25)!
    * Seiyon's shield meets the three-ton basalt slab; the kinetic impact shudders through the iron chamber!
    * Drone levers its sapper spike into the retaining bracket; the massive shield pops off its arm mounts, crashing to the floor!
    * Deals **540 Blunt/Void damage** and $+88$ Posture Strain!
- **Step 4: STAGGER THRESHOLD 1 TRIGGERED!**:
  * Total Boss HP crosses 70% threshold (2,800 HP), falling to **2,030/4,000 HP**; Posture crosses 60% strain line!
  * **STAGGER LEVEL 1 ACTIVE!** The Forgotten Soldier sinks onto both knees; all defenses drop to zero; takes $+50\%$ damage across all incoming attacks!
- **Step 5: Turn End State**:
  * Total Boss HP: 2,760 -> **2,030/4,000 [THRESHOLD BREACHED: Below 2,800 HP!]**.
  * Tower Aegis: 1,060 -> **520/1,300** | Posture: **94/260 [BREACHED]**.
  * Boss Posture: **116/300 [STAGGER LEVEL 1]**.
  * Seiyon Status: Unbroken.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Maximum Burst & Phase 2 Threshold Skip)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * The Forgotten Soldier remains completely stunned; the Rusting Duty Core in its chest is exposed, gears spinning frantically under boiling steam.
  * Seiyon coordinates an all-out offensive barrage targeting the central clockwork core.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 11 -> 5 AP, Momentum Crit): Stands at Node 04. Spends 3 AP on `[Prismatic Stiletto Void Execution Flurry]`. Spends 2 AP on `[Mnemonic Drive]`.
  * Mnemonic Drone: Delivers `[Hydraulic Ram Smashing Knee Brackets]` (3 AP).
  * Resonant Lens: Focuses `[528 Hz Harmonic Resonance]` (2 AP).
- **Step 3: Unopposed Stagger Punishment Rotation**:
  * Seiyon's `[Void Execution Flurry]`: Plunges through the clockwork core for **820 Void damage** (Fatal 2.0x proc!)!
  * Seiyon's `[Mnemonic Drive]`: Slices through the remaining shield fragments for **380 Pierce damage**!
  * Drone's `[Hydraulic Ram]`: Crushes the armor knee struts for **210 Blunt damage**!
  * Lens's `[Harmonic Resonance]`: Shakes loose rusted gears for **140 Void damage**!
  * **TOTAL BURST DAMAGE: 1,550 DAMAGE!**
- **Step 4: SECOND STAGGER THRESHOLD (1,600 HP) COMPLETELY SKIPPED!**:
  * Boss HP plunges from 2,030 down to **480/4,000 HP**! Tower Aegis completely destroyed (0/1,300 HP)!
  * **Phase 2 Emergency Activation Triggered!**
- **Step 5: Turn End State**:
  * Total Boss HP: 2,030 -> **480/4,000** (Core HP: **480/1,700** | Aegis: **DESTROYED**).
  * Posture: **46/300**.

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Phase 2 Escalation: Clockwork Cataclysm & The Unbroken Sentinel)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * The Soldier awakens in desperate mechanical anguish; all internal boiler relief valves blow open simultaneously!
  * Boss Special Skill: `[Overheated Clockwork Blast]` (Tectonic Steam Cataclysm, 3 Coins).
  * Seiyon activates Relic Overdrive: `[VOW OF THE UNBROKEN SENTINEL — MAXIMUM]` (Cost: 3 AP, 30 SP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon (Speed 9 -> 5 AP [Overdrive]): Steps directly to Node 04 before the automaton, planting her holographic tower shield into the iron plating.
  * Mnemonic Drone: Locks stasis anchors around the perimeter at Node 06.
  * Weaver Array: Dispels residual thermal tremors.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 04 to 05)**: The Forgotten Soldier unleashes `[Overheated Clockwork Blast]` (Base 21 + 3 Coins = 33 Power, Area Weight/Heat).
    * Seiyon clashes with `[VOW OF THE UNBROKEN SENTINEL — MAXIMUM]` (Base 28 + 3 Coins Heads = 47 Power, Supreme Kinetic Fortress).
    * **Clash Outcome**: SEIYON OVERWHELMING RELIC CLASH WIN (47 vs 33)!
    * The scalding steam and shrapnel wash harmlessly over Seiyon's shimmering golden barrier (`[P3: Parry/Protection]`).
    * Seiyon steps through the steam, placing her hand on the soldier's scorching breastplate: *"Your shift is finished, soldier. You held the line."*
    * The automaton's drive gears seize into peaceful stillness! Zero squad damage taken!
- **Step 4: Turn End State**:
  * Total Boss HP: **480/4,000** | Posture: **22/300 [GEARS FROZEN]**.
  * Seiyon Composure: 50/50 SP.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Floor Realization 3 & Key Page: The Guardian)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Hostile intent drops to zero. Posture reaches **0/300 [TERMINAL TRANSMUTATION]**.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Seiyon steps forward to Node 05, resting her hand upon the cooling iron chassis.
- **Step 3: Floor Realization & Transmutation**:
  * The roaring steam vents fall completely silent. In the quiet of the iron concourse, Seiyon reflects upon her 1,778 cycles of endless vigilance:
    > *"I thought duty was a cage forged of programming and iron. But duty without love is only rust. Duty with love is the willingness to stand in the dark so another can reach the morning. That is why I endured."*
  * **FLOOR REALIZATION 3 ACHIEVED!**
  * The Forgotten Soldier bows its head in deep, solemn respect. Its chassis dissolves into dark, polished iron plating that condenses into a heavy steel-bound tome: **`[Key Page: The Guardian]`**!
  * Deals **480 Peaceful Harmony**! Boss HP drops to 0!
- **Step 4: Operational Artifact Extraction & Floor Access**:
  * **Key Page Acquired**: `[Key Page: The Guardian]` (Grants $+25$ Poise and absorbs 100% of damage directed at frontline allies).
  * **Descent Access**: The iron fortress portcullis raises, revealing a descending spiral staircase of basalt steps leading to **Floor 04: Floor of Unexpressed Grief**.
  * **Casualties**: Zero Damage Taken. Seiyon HP 3,400/3,400. Composure 50/50 SP."""

def main():
    p2_path = "SOMNARAK-WORLD/Gieok_Jeojangso/Reception_2_Memory_Thief.md"
    p3_path = "SOMNARAK-WORLD/Gieok_Jeojangso/Reception_3_Forgotten_Soldier.md"

    with open(p2_path, "w", encoding="utf-8") as f:
        f.write(generate_reception_2())
    print("Generated Reception_2_Memory_Thief.md successfully!")

    with open(p3_path, "w", encoding="utf-8") as f:
        f.write(generate_reception_3())
    print("Generated Reception_3_Forgotten_Soldier.md successfully!")

if __name__ == "__main__":
    main()
