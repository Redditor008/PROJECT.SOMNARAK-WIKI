#!/usr/bin/env python3
"""
tools/expand_part_2_days.py
Appends fully-realized Day 21 and Day 25 operational chronicles to Part 2 (Days 1 to 25),
integrating the 10-Node spatial grid, Speed/Range profiles, M.A.W.-W modifiers, and Four P-framework.
"""

import sys, os
sys.path.append(os.path.dirname(__file__))
from box_formatter import make_box

def generate_day_21():
    t_box = make_box("REVERIE DIRECTORATE — CENTRAL COMMAND TERMINAL", [
        "FACILITY MANAGEMENT INTERFACE: DAY 21 SHIFT",
        "ENERGY HARVEST QUOTA  : 0.080 TONS // CURRENT HARVEST: 0.000 TONS",
        "COVERT BALLAST RESERVE : 48.250 TONS [HYDRAULIC CRYO-VAULTS]",
        "ACTIVE CONTAINMENT    : SE-001, 005, 032 (WEIGHTING BIRD), 033",
        "DEPARTMENTAL STATUS   : FLOORS 1 THROUGH 4 SYNCHRONIZED"
    ])

    roster_box = make_box("DEPLOYED ROSTER: FLOORS 1 THROUGH 4 TACTICAL MATRIX", [
        "AGENT & RATING        | STATS, GEAR & FOUR P-FRAMEWORK SPEC",
        "----------------------+-----------------------------------------------",
        "Agent Hong (Grade IV) | HP 48 | SP 60 | Work 52 | Speed 6 (3 AP + 1 Move)",
        "Line Specialist       | M.A.W.-W: Hollow Requiem (Lament / Medium / 1 AP)",
        "Floor 4 Assigned      | Suit: Hollow Shroud (Light / Spd +1) | Halo Gift",
        "                      | Posture: 55/55 | Parry: 14 Power | Pass: Choral Echo",
        "                      | Panic Typology: Despair (Triggers at SP <= -35)",
        "----------------------+-----------------------------------------------",
        "Agent Tak (Grade IV)  | HP 59 | SP 42 | Work 44 | Speed 5 (3 AP)",
        "Breacher / Anchor     | M.A.W.-W: Fury Blade (Grudge / Heavy / 2 AP)",
        "Floor 2 Assigned      | Suit: Furnace Plate (Heavy / Spd -1 / Posture 70)",
        "                      | Guard: 16 Direct Absorb | Pass: Smoldering Poise",
        "                      | Panic Typology: Berserk (Triggers at SP <= -30)",
        "----------------------+-----------------------------------------------",
        "Agent Jo (Grade III)  | HP 40 | SP 45 | Work 45 | Speed 6 (3 AP)",
        "Mid-Field Warden      | M.A.W.-W: Stun Lance (Void / Medium / 1 AP / Band 2)",
        "Floor 3 Assigned      | Suit: Standard Aegis (Medium / Spd 0 / Posture 50)",
        "                      | Parry: 11 Power | Pass: Harmonic Aegis (+10% Res)",
        "                      | Panic Typology: Wandering (Triggers at SP <= -25)"
    ])

    ordeal_box = make_box("TACTICAL DOSSIER: CRIMSON NOON ORDEAL SUPPRESSION", [
        "DESIGNATION           : THE PROCESSION OF CARVED MASKS (NOON)",
        "CLASSIFICATION        : CRIMSON (GRUDGE) SECOND WATCH AGGRESSOR",
        "INTRUSION POINT       : FLOOR 4 RESEARCH FORGE CORRIDOR (NODE 03)",
        "HOSTILE PARAMETERS    : HP 180/180 | Posture 90/90 | Speed 5 (3 AP)",
        "ATTACK AFFINITY       : Grudge (Physical Cleave / Red Tremor)",
        "AFFINITY VULNERABILITY: Lament (White Resonance: 1.5x Multiplier)",
        "SPECIAL THREAT        : Blade Flurry hits 2 adjacent nodes simultaneously",
        "TACTICAL ORDERS       : INTERCEPT AT NODE 02; CRUSH WITH LAMENT FIRE"
    ])

    hud_t01 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 — FLOOR 4 RESEARCH FORGE MAIN CORRIDOR]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [TAK]   [MASK]  [JO]    [HONG]                          [AYSHUK]",
        "---",
        "SPATIAL RANGES & POSITIONS:",
        "- Node 02: Agent Tak (Line Anchor / Heavy Armor / Range Band 1)",
        "- Node 03: Carved Mask (Crimson Hostile / Ingress Epicenter)",
        "- Node 04: Agent Jo (Mid-Field Specialist / Range Band 2)",
        "- Node 05: Agent Hong (Lament Sharpshooter / Range Band 3)",
        "- Node 10: Research Lead Ayshuk (Observation Terminal / Band 5)",
        "---",
        "OPERATIVE STATUS & RESOURCE POOLS:",
        "- Agent Tak  : Spd 5 -> 3 AP | HP 59/59 | SP 42/42 | Posture 70/70",
        "- Agent Jo   : Spd 6 -> 3 AP | HP 40/40 | SP 45/45 | Posture 50/50",
        "- Agent Hong : Spd 6 -> 3 AP | HP 48/48 | SP 60/60 | Posture 55/55",
        "- Carved Mask: Spd 5 -> 3 AP | HP 180/180 | Posture 90/90"
    ])

    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — PUSHING TO STAGGER LEVEL 1]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [TAK]   [MASK]  [JO]    [HONG]                          [AYSHUK]",
        "---",
        "- Node 02: Agent Tak (Holding Ground / Guard Shield Locked)",
        "- Node 03: Carved Mask (Staggered by Lament Blast / Posture 48/90)",
        "- Node 04: Agent Jo (Thrusting Void Lance / Band 2)",
        "- Node 05: Agent Hong (Choral Requiem Echo Firing)",
        "---",
        "- Agent Tak  : Spd 5 -> 3 AP | HP 55/59 | SP 42/42 | Posture 58/70",
        "- Agent Jo   : Spd 6 -> 3 AP | HP 40/40 | SP 45/45 | Posture 50/50",
        "- Agent Hong : Spd 6 -> 3 AP | HP 48/48 | SP 60/60 | Posture 55/55",
        "- Carved Mask: Spd 3 -> 1 AP | HP 128/180 | Posture 48/90 [CRACKED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER LEVEL 1]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [TAK]   [MASK]          [HONG]                          [AYSHUK]",
        "                [JO]",
        "---",
        "- Node 02: Agent Tak (Priming Fury Blade Cleave)",
        "- Node 03: Carved Mask (STAGGER LEVEL 1 / 1.5x DAMAGE TAKEN)",
        "- Node 03: Agent Jo (Flanking Ingress / Point-Blank Band 1)",
        "- Node 05: Agent Hong (Momentum Surge Active / +2 Speed Next Turn)",
        "---",
        "- Agent Tak  : Spd 5 -> 3 AP | HP 55/59 | SP 42/42 | Posture 58/70",
        "- Agent Jo   : Spd 6 -> 3 AP | HP 40/40 | SP 45/45 | Posture 50/50",
        "- Agent Hong : Spd 6 -> 3 AP | HP 48/48 | SP 60/60 | Posture 55/55",
        "- Carved Mask: Spd 0 -> 0 AP | HP 68/180  | Posture 22/90 [STAGGERED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — CARVED MASK DESPERATION CARNIVAL]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [TAK]   [MASK]  [JO]    [HONG]                          [AYSHUK]",
        "---",
        "- Node 02: Agent Tak (Smoldering Poise Active / Absorbing Blows)",
        "- Node 03: Carved Mask (Recovered / Channeling Carnival Cleave)",
        "- Node 04: Agent Jo (Parrying Secondary Flurry)",
        "- Node 05: Agent Hong (Spd 8 / AP 4 / Rapid Choral Discharge)",
        "---",
        "- Agent Tak  : Spd 5 -> 3 AP | HP 50/59 | SP 42/42 | Posture 44/70",
        "- Agent Jo   : Spd 6 -> 3 AP | HP 37/40 | SP 45/45 | Posture 42/50",
        "- Agent Hong : Spd 8 -> 4 AP [SURGE] | HP 48/48 | SP 60/60 | Posture 55/55",
        "- Carved Mask: Spd 5 -> 3 AP | HP 36/180  | Posture 12/90 [CRITICAL]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER THRESHOLD 2]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [TAK]   [MASK]                                          [AYSHUK]",
        "        [JO]    [HONG]",
        "---",
        "- Node 02: Agent Tak & Agent Jo (Cross-Locking Hostile Frame)",
        "- Node 03: Carved Mask (TERMINAL STAGGER / POSTURE 0/90 / 2.0x DMG)",
        "- Node 03: Agent Hong (Channeling Direct Lament Dissolution)",
        "---",
        "- Agent Tak  : Spd 5 -> 3 AP | HP 50/59 | SP 42/42 | Posture 44/70",
        "- Agent Jo   : Spd 6 -> 3 AP | HP 37/40 | SP 45/45 | Posture 42/50",
        "- Agent Hong : Spd 6 -> 3 AP | HP 48/48 | SP 60/60 | Posture 55/55",
        "- Carved Mask: Spd 0 -> 0 AP | HP 10/180  | Posture 0/90 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [TAK]   [ASH]   [JO]    [HONG]                          [AYSHUK]",
        "---",
        "- Node 02: Agent Tak (Returning Blade to Scabbard)",
        "- Node 03: Carved Mask (Shattered / Crystallizing into Han Amber)",
        "- Node 04: Agent Jo (Venting Steam Conduits)",
        "- Node 05: Agent Hong (Harvesting Refined Reagents)",
        "---",
        "- Agent Tak  : Spd 5 -> 3 AP | HP 50/59 | SP 42/42 | Posture 56/70",
        "- Agent Jo   : Spd 6 -> 3 AP | HP 37/40 | SP 45/45 | Posture 50/50",
        "- Agent Hong : Spd 6 -> 3 AP | HP 48/48 | SP 60/60 | Posture 55/55",
        "- Carved Mask: HP 0/180 [DESTROYED] | +0.010 TONS REFINED HAN HARVESTED"
    ])

    eval_box = make_box("END-OF-DAY PERFORMANCE EVALUATION: DAY 21", [
        "METRIC                 | TARGET QUOTA   | REALIZED PERFORMANCE",
        "-----------------------+----------------+---------------------",
        "Han Energy Harvested   | 0.080 Tons     | 0.086 Tons [MET]",
        "Containment Breaches   | 0 Breaches Max | 0 Breaches [CLEARED]",
        "Personnel Casualties   | 0 Fatalities   | 0 Fatalities [PERFECT]",
        "Second Watch Ordeal Suppressed | 1/1 Suppressed | 100% Rate [RESOLVED]",
        "Meltdowns Cleared      | 4/4 Cleared    | 100% Rate [NEUTRALIZED]",
        "-----------------------+----------------+---------------------",
        "SHIFT PERFORMANCE GRADE: GRADE S (SUPREME DISPATCH)",
        "REAGENTS ACCUMULATED   : +24 RHR (REFINED HAN REAGENTS)",
        "OPERATIVE ADVANCEMENT  :",
        "- Agent Hong : +4 Clarity, +3 Composure (Senior Warden)",
        "- Agent Tak  : +5 Resilience, +2 Resolve (Bulwark Sentinel)",
        "- Agent Jo   : +4 Composure, +3 Clarity (Promoted to Grade IV)"
    ])

    extract_box = make_box("EXTRACTION WELL ARCHIVE: SELECT NEXT COMPANION", [
        "CHOICE ALPHA [SE-C-IIIg-002]:",
        "'A stone titan whose mournful footsteps shake the bedrock of",
        "the southern wastes.'",
        "---",
        "CHOICE BETA  [SE-C-IIIg-145]:",
        "'A garden of razor thorns that drinks anger and flowers into",
        "burning iron.'",
        "---",
        "CHOICE GAMMA [SE-C-IIIb-072]:",
        "'A mirror that shows not your face, but the person you betrayed",
        "to survive the Before-Time.'"
    ])

    forge_box = make_box("M.A.W. SYNTHESIS FORGING LOG — DAY 21", [
        "FORGE SPECIFICATION    | SLOT / PROPERTIES / PARAMETERS",
        "-----------------------+----------------------------------------------",
        "Judicial Scale Blade   | Weapon: 6-9 Weight (Heavy / Speed Delta -1)",
        "                       | Range Band 1 | 2 AP | Inflicts +20% Posture",
        "Judicial Feather Robe  | Suit: Medium Armor (Speed Delta 0)",
        "                       | Resist: 0.7 Grudge / 0.8 Lament / 0.7 Weight",
        "Scale Crown Gift       | Head Slot: +6 SP, +5% Parry Counter Power",
        "-----------------------+----------------------------------------------",
        "EQUIPMENT ALLOCATION   | BESTOWED UPON AGENT TAK (ANCHOR SPECIALIST)"
    ])

    content = f"""
### Day 21

### Story — Dialogue

> **Ayshuk:** _"Research telemetry from Floor 4. Entity 032 — The Weighting Bird — has completed chamber stabilization. Its scales have balanced thirty consecutive emotional feeds without tipping toward execution."_

> **Majin:** _"And the feathers?"_

> **Ayshuk:** _"The plumage remains pale bronze. But when Agent Hong passed the observation glass, the left scale dipped by 1.4 grams. The bird felt his lingering remorse over the recruits lost in cycle 1,775."_

> **Zyrak:** _"I forged the Judicial Scale Blade from its shed talons this morning. Heavy as lead, sharp as winter ice. If an operative strikes with unjust wrath, the hilt burns cold. It demands composure."_

> **Majin:** _"Good. Give it to Tak. He knows the weight of an anchor. What of the outer perimeter, Seiyon?"_

> **Seiyon:** _"Atmospheric pressure above Floor 1 is oscillating. Crimson resonance particles are gathering along the western ventilation conduits. A Second Watch Ordeal is approaching."_

> **Majin:** _"Deploy Hong, Tak, and Jo to the research corridor. Hold Node 02. Let the bird watch how the Directorate measures justice."_

---

### Gameplay — Day 21: Central Command Tactical Interface

```text
{t_box}
```

Shift parameters engaged for Day 21. Daily collection quota increases to **0.080 tons** of refined Han. Deep cryogenic ballast reserves register **48.250 tons**—surpassing the mid-point of our preliminary accumulation arc. Floor 4 (Insight Forge) is fully synchronized under Lead Researcher Ayshuk, allowing direct observation of newly contained companion **SE-C-IIIγ-032** (*The Weighting Bird*).

Tactical priorities for Day 21:
1. Conduct safe calibration runs on The Weighting Bird to harvest high-density Weight-affinity Han.
2. Maintain zero casualties during expected Second Watch (Noon) Ordeal intrusion.
3. Advance operative combat proficiencies using the Four P-Framework.

#### 1. Pre-Shift Tactical Deployment & Operative Profiles

```text
{roster_box}
```

Director Majin issues operational clearance: **[DAY 21 PROTOCOL ENGAGED]**.

---

#### 2. Granular Work Type Management: Chamber 032 (The Weighting Bird)

Agent Hong is dispatched to Chamber 032 for Viderehan observation:
- `[DISPATCH: Agent Hong -> Floor 4, Chamber 032]`
- `[PROTOCOL: Viderehan Observation (Judicial Calibration / Weight Affinity)]`

```text
> Chamber Telemetry: "The bronze bird tilts its head, peering into Hong's open chest..."
> Fear Check: Level IV Senior Agent vs Class III Entity -> RESULT: ABSOLUTE CALM.
```

- **Work Tick 01–04:** 4 Successes. The bronze scale swings smoothly, registering the purity of Hong's dedication to the Directorate's mission.
- **Work Tick 05:** Failure! Hong recalls the faces of fallen comrades from previous loops. The right scale drops sharply! 4 Black (Weight) damage sustained. Hong's SP absorbs the strain (SP: 56/60).
- **Work Tick 06–10:** 5 Successes.
- **Work Result:** **9/10 Positive Han Crystals (EXCELLENT WORK RESULT)!**
- Yield: **+0.024 tons** refined Han deposited into Floor 4's primary capacitor.

Energy climbs to `0.046 / 0.080 tons`.

---

#### 3. Ordeal Manifestation: Second Watch (Crimson Noon) Suppression

At 14:15, the facility alarms sound a rhythmic, brassy toll. Crimson mist vents from the Floor 4 air ducts:

```text
{ordeal_box}
```

A massive, floating carnival construct formed of jagged porcelain theatre masks and whirling razor blades materializes at Node 03. It lets out a high-pitched, mocking laugh that vibrates the metal grating of Floor 4!

```text
{hud_t01}
```

##### Turn 01 Action Resolution Log (Spatial Ingress & Heavy Clash)
- **Operative Movement & Actions**:
  * **Agent Tak (Speed 5 -> 3 AP)**: Spends 1 AP to plant his heavy boots at Node 02, entering Point-Blank Range Band 1. Declares `[Fury Blade Cleave]` (Costs 2 AP).
  * **Agent Jo (Speed 6 -> 3 AP)**: Spends 1 AP to advance to Node 04 (Range Band 2). Declares `[Stun Lance Piercing Thrust]` (Costs 2 AP).
  * **Agent Hong (Speed 6 -> 3 AP)**: Holds Node 05 (Range Band 3). Spends 2 AP to lock optical targeting with `[Hollow Requiem Choral Wave]`. Holds 1 AP in Defensive Guard (+10 Block).
- **Clash Resolution (Node 02 to Node 03)**:
  * Carved Mask targets Tak with `[Whirling Porcelain Guillotine]`:
    * Hostile Roll: Base 8 + (2 Coins Heads: +4) = **12 Power**.
  * Agent Tak unleashes `[Fury Blade Cleave]`:
    * *Tak Passive Trigger:* `Smoldering Poise` (+2 Clash Power when holding Node 02).
    * Tak Roll: Base 9 + (2 Coins Heads: +4) = **15 Power**.
  * **Result**: **Agent Tak WINS THE CLASH (15 vs 12)!**
    * The razor blades screech against Tak's heavy shield. Tak drives his fury blade through the mask's porcelain cheek!
    * Deals 26 Grudge damage (HP: 154/180). Inflicts +18 Posture Strain (Posture: 72/90).

---

```text
{hud_t02}
```

##### Turn 02 Action Resolution Log (Lament Vulnerability & Stagger Build)
- **Coordinated Tripartite Assault**:
  * **Agent Hong (Speed 6 -> 3 AP)** fires from Range Band 3:
    * `[Hollow Requiem Choral Wave]` strikes the mask's acoustic resonance frequency!
    * Damage: 18 White * 1.5x (Lament Vulnerability) = **27 Direct Lament Damage**!
  * **Agent Jo (Speed 6 -> 3 AP)** executes `[Stun Lance Thrust]` from Node 04:
    * Deals 14 Void damage.
  * **Agent Tak (Speed 5 -> 3 AP)** blocks the counter-flurry with `[Directional Guard]`, taking only 4 chip damage (HP: 55/59).
  * Carved Mask HP drops from 154 to **113/180**!
  * Combined Posture strain strips another 24 points: Posture drops to **48/90**, crossing the **60% Posture Threshold**!
  * **STAGGER LEVEL 1 TRIGGERED!** The porcelain masks fracture with loud cracks; hostile actions canceled for Turn 03!

---

```text
{hud_t03}
```

##### Turn 03 Action Resolution Log (Stagger Level 1 Exploitation)
- **Allied Focus Fire**:
  * With the hostile staggered, all attacks deal 1.5x direct damage!
  * **Agent Hong**: Passive `Momentum Surge` triggers! Hong gains +2 Speed for next turn. His choral beam tears through the porcelain core, dealing **38 Lament damage**!
  * **Agent Tak**: Smashes with `[Two-Handed Cleave]`, dealing **24 Grudge damage**!
  * **Agent Jo**: Infiltrates to Node 03, dealing **18 Void damage**!
  * Total damage: 80! Hostile HP plummets from 113 to **33/180**!
  * Posture collapses to **14/90**!

---

```text
{hud_t04}
```

##### Turn 04 Action Resolution Log (Desperation Carnival Cleave)
- **Hostile Recovery & Desperation Protocol**:
  * The Carved Mask recovers, rotating wildly in a 360-degree blade tempest: `[Carnival Cleave]`.
  * **Agent Tak**: Uses 2 AP to activate `[Bulwark Interception]`, absorbing the brunt of the kinetic storm. Tak sustains 5 damage (HP: 50/59), shielding Jo and Hong completely!
  * **Agent Hong (Speed 8 under Surge -> 4 AP)**: Fires two consecutive Lament bursts from Range Band 3, dealing 20 damage!
  * Hostile HP reaches **13/180**!

---

```text
{hud_t05}
```

##### Turn 05 Action Resolution Log (Terminal Stagger Induction)
- **Execution Setup**:
  * Agent Jo executes a precision pin at Node 02 with his Stun Lance, draining the last 14 Posture points!
  * **TERMINAL STAGGER LEVEL 2 TRIGGERED:** Posture hits 0/90. The porcelain construct shatters into disjointed fragments, hovering helpless above the deckplates!

---

```text
{hud_t06}
```

##### Turn 06 Action Resolution Log (Climax Execution)
- **Final Subdual**:
  * Agent Tak brings down the Judicial Scale Blade with the full weight of his heavy armor.
  * The blade cuts through the central axis. With a sound like breaking fine china, the Carved Mask explodes into radiant amber dust and shimmering Han crystals!
  * **+0.010 tons of refined Han harvested!**

Shift energy hits **0.086 / 0.080 tons**! Quota surpassed!

---

#### 4. Shift Evaluation Index & Daily RHR Allocation

```text
{eval_box}
```

---

#### 5. Well Extraction Protocol (Containment Authorization)

```text
{extract_box}
```

##### Director Majin's Assessment & Authorization
- *Choice Alpha* is *The Grieving Colossus* (SE-C-IIIγ-002)—a massive entity with high weight strain.
- *Choice Gamma* is *The Broken Mirror* (SE-C-IIIβ-072)—psychologically destabilizing for high-Clarity personnel.
- *Choice Beta* is **Garden of Thorns** (SE-C-IIIγ-145)—an aggressive combat training entity essential for refining our Breachers' Resilience.

AUTHORIZATION CONFIRMED: **Choice Beta: SE-C-IIIγ-145 (*Garden of Thorns*)**.

---

#### 6. M.A.W. Synthesis & Armament Forging

```text
{forge_box}
```

Agent Tak is equipped with the *Judicial Scale Blade*, drastically amplifying Floor 2's frontline holding power.

---

#### 7. Nocturnal Sub-Vault Telemetry & Director's Vigil

At 02:15, Majin inspects the Floor 4 observation gallery. Through the reinforced viewport, *The Weighting Bird* sleeps peacefully upon its bronze perch, its scales level and balanced.

Beneath the floor, the hydraulic ballast meters verify **48.250 tons** of stored sorrow.

Seiyon's voice whispers across the terminal: *"The balance holds, Majin."*

Majin nods slowly: *"Four more days until the quarter-milestone. Keep the pressure steady."*
"""
    return content

def generate_day_25():
    t_box = make_box("REVERIE DIRECTORATE — CENTRAL COMMAND TERMINAL", [
        "FACILITY MANAGEMENT INTERFACE: DAY 25 MILESTONE SHIFT",
        "ENERGY HARVEST QUOTA  : 0.100 TONS // CURRENT HARVEST: 0.000 TONS",
        "COVERT BALLAST RESERVE : 48.550 TONS [HYDRAULIC CRYO-VAULTS]",
        "ACTIVE CONTAINMENT    : SE-001, 005, 032, 033, 145 (THORNS)",
        "CYCLE MILESTONE       : 25 OF 365 DAYS COMPLETE (BATCH 1 FINALE)"
    ])

    roster_box = make_box("DEPLOYED ROSTER: BATCH 1 TERMINAL ENGAGEMENT", [
        "AGENT & RATING        | STATS, GEAR & FOUR P-FRAMEWORK SPEC",
        "----------------------+-----------------------------------------------",
        "Agent Tak (Grade IV)  | HP 64 | SP 44 | Work 46 | Speed 5 (3 AP)",
        "Frontline Bulwark     | M.A.W.-W: Judicial Blade (Weight / Heavy / 2 AP)",
        "Floor 2 Assigned      | Suit: Furnace Plate (Heavy) | Scale Crown Gift",
        "                      | Posture: 75/75 | Guard: 16 Absorb | Pass: Weight Poise",
        "                      | Panic Typology: Berserk (SP <= -30)",
        "----------------------+-----------------------------------------------",
        "Agent Hong (Grade IV) | HP 48 | SP 64 | Work 55 | Speed 6 (3 AP + 1 Move)",
        "Senior Marksman       | M.A.W.-W: Hollow Requiem (Lament / Medium / 1 AP)",
        "Floor 4 Assigned      | Suit: Hollow Shroud (Light / Spd +1) | Halo Gift",
        "                      | Posture: 55/55 | Parry: 14 Power | Pass: Momentum Surge",
        "                      | Panic Typology: Despair (SP <= -35)",
        "----------------------+-----------------------------------------------",
        "Agent Kang (Grade III)| HP 54 | SP 38 | Work 40 | Speed 6 (3 AP)",
        "Line Breacher         | M.A.W.-W: Thorn Bracer (Grudge / Medium / 1 AP)",
        "Floor 3 Assigned      | Suit: Reinforced Mail (Medium / Spd 0 / Posture 60)",
        "                      | Parry: 12 Power | Pass: Thorn Reflect (+15% Dmg)",
        "                      | Panic Typology: Catatonic (SP <= -25)"
    ])

    ordeal_box = make_box("TACTICAL DOSSIER: AMBER NOON ORDEAL SUPPRESSION", [
        "DESIGNATION           : THE BURROWING CHITIN (AMBER NOON)",
        "CLASSIFICATION        : AMBER (WEIGHT) SECOND WATCH CARAPACE HOSTILE",
        "INTRUSION POINT       : FLOOR 2 CONTAINMENT TRENCH (NODE 02 INGRESS)",
        "HOSTILE PARAMETERS    : HP 220/220 | Posture 110/110 | Speed 4 (2 AP)",
        "ATTACK AFFINITY       : Weight (Kinetic Tremor / Black Rupture)",
        "AFFINITY VULNERABILITY: Void (Pierce / Energy Dissolution: 1.5x)",
        "SPECIAL THREAT        : Subterranean burrow cancels ranged targeting",
        "TACTICAL ORDERS       : PIN AT NODE 02; BREAK CARAPACE WITH HEAVY CLEAVE"
    ])

    hud_t01 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 — FLOOR 2 SUBTERRANEAN TRENCH CORRIDOR]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [CHITIN][TAK]   [KANG]  [HONG]                          [DEKAN]",
        "---",
        "SPATIAL RANGES & POSITIONS:",
        "- Node 02: Burrowing Chitin (Subterranean Eruption Epicenter)",
        "- Node 03: Agent Tak (Line Anchor / Heavy Bulwark / Range Band 1)",
        "- Node 04: Agent Kang (Line Breacher / Thorn Gauntlets / Band 2)",
        "- Node 05: Agent Hong (Senior Marksman / Range Band 3)",
        "- Node 10: Containment Lead Dekan (Reinforced Watchtower / Band 5)",
        "---",
        "OPERATIVE STATUS & RESOURCE POOLS:",
        "- Agent Tak   : Spd 5 -> 3 AP | HP 64/64 | SP 44/44 | Posture 75/75",
        "- Agent Kang  : Spd 6 -> 3 AP | HP 54/54 | SP 38/38 | Posture 60/60",
        "- Agent Hong  : Spd 6 -> 3 AP | HP 48/48 | SP 64/64 | Posture 55/55",
        "- Chitin Beast: Spd 4 -> 2 AP | HP 220/220 | Posture 110/110"
    ])

    hud_t02 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 — CRACKING THE DORSAL SHELL]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [CHITIN][TAK]   [KANG]  [HONG]                          [DEKAN]",
        "---",
        "- Node 02: Burrowing Chitin (Posture 72/110 / Carapace Fissuring)",
        "- Node 03: Agent Tak (Judicial Blade Heavy Strike Landed)",
        "- Node 04: Agent Kang (Thorn Reflect Parry Executed)",
        "- Node 05: Agent Hong (Aiming High-Angle Choral Pulse)",
        "---",
        "- Agent Tak   : Spd 5 -> 3 AP | HP 58/64 | SP 44/44 | Posture 62/75",
        "- Agent Kang  : Spd 6 -> 3 AP | HP 54/54 | SP 38/38 | Posture 60/60",
        "- Agent Hong  : Spd 6 -> 3 AP | HP 48/48 | SP 64/64 | Posture 55/55",
        "- Chitin Beast: Spd 3 -> 1 AP | HP 165/220 | Posture 72/110 [CRACKED]"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 — POSTURE BREAK STAGGER LEVEL 1]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [CHITIN]        [HONG]                                  [DEKAN]",
        "        [TAK]   [KANG]",
        "---",
        "- Node 02: Chitin Beast (STAGGER LEVEL 1 / 1.5x DAMAGE TAKEN)",
        "- Node 02: Agent Tak (Point-Blank Band 1 Cleave)",
        "- Node 03: Agent Kang (Thorn Flurry Driving into Fissure)",
        "- Node 04: Agent Hong (Advancing with Momentum Surge)",
        "---",
        "- Agent Tak   : Spd 5 -> 3 AP | HP 58/64 | SP 44/44 | Posture 62/75",
        "- Agent Kang  : Spd 6 -> 3 AP | HP 54/54 | SP 38/38 | Posture 60/60",
        "- Agent Hong  : Spd 8 -> 4 AP [SURGE] | HP 48/48 | SP 64/64 | Posture 55/55",
        "- Chitin Beast: Spd 0 -> 0 AP | HP 92/220  | Posture 35/110 [STAGGERED]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 — SEISMIC TREMOR REBOUND]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [CHITIN][TAK]   [KANG]  [HONG]                          [DEKAN]",
        "---",
        "- Node 02: Chitin Beast (Channeling Subterranean Tremor)",
        "- Node 03: Agent Tak (Grounding Kinetic Shockwave with Shield)",
        "- Node 04: Agent Kang (Thorn Armor Absorbing Residual Vibration)",
        "- Node 05: Agent Hong (Rapid Firing Choral Beams)",
        "---",
        "- Agent Tak   : Spd 5 -> 3 AP | HP 52/64 | SP 44/44 | Posture 48/75",
        "- Agent Kang  : Spd 6 -> 3 AP | HP 50/54 | SP 38/38 | Posture 52/60",
        "- Agent Hong  : Spd 6 -> 3 AP | HP 48/48 | SP 64/64 | Posture 55/55",
        "- Chitin Beast: Spd 4 -> 2 AP | HP 48/220  | Posture 18/110 [WEAKENED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 — TERMINAL STAGGER THRESHOLD 2]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [CHITIN]                                                [DEKAN]",
        "        [TAK]   [KANG]  [HONG]",
        "---",
        "- Node 02: Chitin Beast (TERMINAL STAGGER / POSTURE 0/110 / 2.0x DMG)",
        "- Node 02: Agent Tak (Pinning Mandibles with Judicial Blade)",
        "- Node 03: Agent Kang (Driving Thorn Spike into Exposed Core)",
        "- Node 04: Agent Hong (Harmonic Resonance Overdrive)",
        "---",
        "- Agent Tak   : Spd 5 -> 3 AP | HP 52/64 | SP 44/44 | Posture 48/75",
        "- Agent Kang  : Spd 6 -> 3 AP | HP 50/54 | SP 38/38 | Posture 52/60",
        "- Agent Hong  : Spd 6 -> 3 AP | HP 48/48 | SP 64/64 | Posture 55/55",
        "- Chitin Beast: Spd 0 -> 0 AP | HP 14/220  | Posture 0/110 [COLLAPSED]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: COMBAT PHASE 01 — BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 — CLIMAX EXECUTION & PURIFICATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "        [DUST]  [TAK]   [KANG]  [HONG]                          [DEKAN]",
        "---",
        "- Node 02: Chitin Beast (Carapace Shattered / Siphoned into Flues)",
        "- Node 03: Agent Tak (Resting Blade / Wiping Amber Fluid)",
        "- Node 04: Agent Kang (Securing Carapace Fragments)",
        "- Node 05: Agent Hong (Reporting Sector Clear)",
        "---",
        "- Agent Tak   : Spd 5 -> 3 AP | HP 52/64 | SP 44/44 | Posture 60/75",
        "- Agent Kang  : Spd 6 -> 3 AP | HP 50/54 | SP 38/38 | Posture 60/60",
        "- Agent Hong  : Spd 6 -> 3 AP | HP 48/48 | SP 64/64 | Posture 55/55",
        "- Chitin Beast: HP 0/220 [PURIFIED] | +0.015 TONS REFINED HAN HARVESTED"
    ])

    eval_box = make_box("END-OF-DAY PERFORMANCE EVALUATION: DAY 25", [
        "METRIC                 | TARGET QUOTA   | REALIZED PERFORMANCE",
        "-----------------------+----------------+---------------------",
        "Han Energy Harvested   | 0.100 Tons     | 0.108 Tons [SURPASSED]",
        "Containment Breaches   | 0 Breaches Max | 0 Breaches [PERFECT]",
        "Personnel Casualties   | 0 Fatalities   | 0 Fatalities [PERFECT]",
        "Amber Noon Suppressed  | 1/1 Suppressed | 100% Rate [RESOLVED]",
        "Meltdowns Cleared      | 5/5 Cleared    | 100% Rate [STABILIZED]",
        "-----------------------+----------------+---------------------",
        "SHIFT PERFORMANCE GRADE: GRADE S (QUARTER-CYCLE MASTERY)",
        "REAGENTS ACCUMULATED   : +28 RHR (REFINED HAN REAGENTS)",
        "OPERATIVE ADVANCEMENT  :",
        "- Agent Tak  : +5 Resilience, +3 Resolve (Senior Bulwark)",
        "- Agent Hong : +4 Clarity, +3 Composure (Senior Sentinel)",
        "- Agent Kang : +5 Resilience, +3 Composure (Promoted to Grade IV)"
    ])

    forge_box = make_box("M.A.W. SYNTHESIS FORGING LOG — DAY 25", [
        "FORGE SPECIFICATION    | SLOT / PROPERTIES / PARAMETERS",
        "-----------------------+----------------------------------------------",
        "Chitin Carapace Mail   | Suit: Heavy Armor (Speed Delta -1)",
        "                       | Resist: 0.6 Grudge / 1.0 Lament / 0.5 Weight",
        "Chitin Great-Maul      | Weapon: 7-11 Weight (Heavy / Speed Delta -1)",
        "                       | Range Band 1 | 2 AP | Inflicts Tremor Stagger",
        "Carapace Crest Gift    | Head Slot: +8 HP, +10 Max Posture Meter",
        "-----------------------+----------------------------------------------",
        "EQUIPMENT ALLOCATION   | BESTOWED UPON AGENT KANG (BREACH SPECIALIST)"
    ])

    content = f"""
### Day 25

### Story — Dialogue

> **Dekan:** _"Twenty-five days, Director. The first quarter-milestone has arrived."_

> **Majin:** _"And the floor integrity?"_

> **Dekan:** _"Floors 1 through 4 are operating at 99.1% containment efficiency. The rookie clerks have stopped shaking during shift changes. The blood on the corridor gratings has been scrubbed. But the Maw... the Maw is heavier, Majin. The black tar rose two inches last night."_

> **Majin:** _"It rises because we are extracting instead of merely observing. We are starving it of the ambient sorrow it usually consumes."_

> **Dekan:** _"If we starve it too quickly, it will break through Floor 2's basalt anchors before Day 160."_

> **Majin:** _"Then we reinforce the anchors. Zyrak is forging hydraulic ballast locks from the Chitin Carapace plates. Seiyon, give me the reserves reading."_

> **Seiyon:** _"Ballast reserves confirm forty-eight point five-five tons. We have accumulated one point two-five tons during Batch 1 alone. At this acceleration, we will reach the supercritical forty-nine point eight threshold exactly on Day 160."_

> **Majin:** _"Then the timeline holds. Initiate Day 25 shift. Let us conclude Batch 1 with honor."_

---

### Gameplay — Day 25: Central Command Tactical Interface

```text
{t_box}
```

The Day 25 shift commences under heightened industrial pressure. Daily collection quota reaches **0.100 tons** of pure refined Han. Covert cryogenic reserves in the sub-vaults confirm **48.550 tons**—establishing an unbroken trajectory toward the mid-cycle release.

Operational priorities for Day 25:
1. Conduct high-pressure containment on **SE-C-IIIγ-145** (*Garden of Thorns*) and **SE-C-IIIγ-033** (*The Guarding Bird*).
2. Suppress the anticipated Amber Second Watch Ordeal along Floor 2's lower trench.
3. Finalize Batch 1 promotions and armaments for the frontline vanguard.

#### 1. Pre-Shift Tactical Deployment & Operative Profiles

```text
{roster_box}
```

Director Majin engages the floor-wide dispatch relays: **[DAY 25 OPERATIONAL SHIFT COMMENCED]**.

---

#### 2. Granular Work Type Management: Chamber 145 (Garden of Thorns)

Agent Kang enters Chamber 145 for Pugnahan combat calibration:
- `[DISPATCH: Agent Kang -> Floor 3, Chamber 145]`
- `[PROTOCOL: Pugnahan Pruning (Combat Resistance / Grudge Affinity)]`

```text
> Chamber Telemetry: "Razor thorns uncoil from the iron trellis, seeking flesh..."
> Fear Check: Grade III Breacher vs Class III Entity -> RESULT: COMPOSED.
```

- **Work Tick 01–03:** 3 Successes. Kang cleaves overgrown briars with his shock maul.
- **Work Tick 04:** Failure! A razor vine whips across Kang's chest plate; 4 Red (Grudge) damage sustained. Kang's *Thorn Reflect* passive sparks, sending kinetic recoil back into the bush!
- **Work Tick 05–08:** 4 Successes.
- **Work Tick 09:** Failure! 4 Red damage sustained (HP: 46/54).
- **Work Tick 10:** Success! Kang severs the central resonant blossom.
- **Work Result:** **8/10 Positive Han Crystals (NORMAL WORK RESULT).**
- Yield: **+0.026 tons** of refined Han lubricant extracted.

Energy meter rises to `0.068 / 0.100 tons`.

---

#### 3. Ordeal Manifestation: Second Watch (Amber Noon) Suppression

At 15:30, seismic sensors on Floor 2 detect violent drilling beneath the containment trenches:

```text
{ordeal_box}
```

A massive, segmented insectoid monstrosity encased in petrified amber chitin bursts through the basalt plates at Node 02, spraying razor-sharp rock shards across the trench!

```text
{hud_t01}
```

##### Turn 01 Action Resolution Log (Carapace Impact & Frontline Anchor)
- **Operative Movement & Clash Standoff**:
  * **Agent Tak (Speed 5 -> 3 AP)**: Plants his boots firmly at Node 03, swinging the heavy Judicial Scale Blade in a vertical arc (Costs 2 AP).
  * The Chitin Beast unleashes `[Burrowing Mandible Crush]` against Node 03 (2 AP / Weight Affinity):
    * Hostile Roll: Base 9 + (2 Coins Heads: +4) = **13 Power**.
  * Agent Tak's Roll:
    * *Tak Passive Trigger:* `Weight Poise` active (+2 Base Clash Power).
    * Tak Roll: Base 10 + (2 Coins Heads: +4) = **16 Power**!
  * **Clash Result**: **Agent Tak WINS THE CLASH (16 vs 13)!**
    * The Judicial Blade smashes into the beast's armored forehead, driving it backward.
    * Deals 28 Weight damage (HP: 192/220). Inflicts +22 Posture Strain (Posture: 88/110).

---

```text
{hud_t02}
```

##### Turn 02 Action Resolution Log (Fissure Exploitation & Posture Reduction)
- **Coordinated Breaching Strike**:
  * **Agent Kang (Speed 6 -> 3 AP)** steps into Node 03 alongside Tak:
    * Declares `[Thorn Gauntlet Pincer Strike]` (Costs 2 AP).
    * Drives sharp thorn spikes into the crack opened by Tak's blade, dealing **27 Grudge damage**!
  * **Agent Hong (Speed 6 -> 3 AP)** fires from Range Band 3 (Node 05):
    * Firing Void-attuned Lament beams, exploiting the entity's acoustic vulnerabilities: **24 Damage**!
  * Chitin Beast HP drops from 192 to **141/220**!
  * Posture drops from 88 to **44/110**, crossing the **60% Posture Threshold**!
  * **STAGGER LEVEL 1 TRIGGERED!** The insectoid legs buckle, and the creature collapses against the trench wall!

---

```text
{hud_t03}
```

##### Turn 03 Action Resolution Log (Stagger Level 1 Exploitation)
- **Vanguard Overload (1.5x Direct Damage)**:
  * **Agent Hong**: Passive `Momentum Surge` activates! Gains +2 Speed for next turn. Discharges high-frequency beam: **36 Damage**!
  * **Agent Tak**: Executes `[Two-Handed Judicial Sunder]`: **33 Damage**!
  * **Agent Kang**: Unleashes rapid thorn barrage: **26 Damage**!
  * Total single-turn damage: 95! Chitin Beast HP drops to **46/220**!
  * Posture meter collapses to **12/110**!

---

```text
{hud_t04}
```

##### Turn 04 Action Resolution Log (Subterranean Tremor Counter-Surge)
- **Hostile Desperation Protocol**:
  * The Chitin Beast thrashes in fury, slamming its thorax against the ground to trigger `[Subterranean Tremor]`.
  * **Agent Tak**: Deploys `[Directional Guard Absorption]`, grounding the seismic tremor into the bedrock and reducing damage to all allies by 70%! Tak sustains 6 chip damage (HP: 52/64).
  * **Agent Hong (Speed 8 under Surge -> 4 AP)**: Fires two consecutive piercing shots from Range Band 3, dealing 28 damage!
  * Chitin Beast HP falls to **18/220**!

---

```text
{hud_t05}
```

##### Turn 05 Action Resolution Log (Terminal Stagger Induction)
- **Mandible Lock & Stagger**:
  * Agent Tak drives the flat of his blade between the creature's mandibles, locking its head against the floorplates.
  * Agent Kang delivers a point-blank punch into the central nerve cluster:
    * Drains the final 12 Posture points!
    * **TERMINAL STAGGER LEVEL 2 TRIGGERED!** Posture hits **0/110**. The beast ceases all movement, completely neutralized.

---

```text
{hud_t06}
```

##### Turn 06 Action Resolution Log (Climax Execution & Harvest)
- **Final Subdual**:
  * Agent Tak, Agent Kang, and Agent Hong execute a synchronized execution discharge.
  * The amber chitin shell shatters into thousands of polished translucent crystals that dissolve into pure Han vapor.
  * Floor 2's pneumatic collection flues siphon the harvest: **+0.015 tons of refined Han secured**!

Total daily harvest reaches **0.108 / 0.100 tons**! Quota surpassed!

---

#### 4. Shift Evaluation Index & Daily RHR Allocation

```text
{eval_box}
```

---

#### 5. M.A.W. Synthesis & Armament Forging

```text
{forge_box}
```

Agent Kang equips the *Chitin Carapace Mail* and *Chitin Great-Maul*, transforming him into Floor 3's premier heavyweight breacher.

---

#### 6. Nocturnal Sub-Vault Telemetry & Director's Vigil

At 23:59, Director Majin stands in the central command gallery beside Secretary Seiyon. Across the panoramic holographic displays, all four active floors glow with serene green telemetry.

Beneath Floor 6, the hydraulic ballast meters verify **48.550 tons** of refined sorrow held in cryogenic stasis.

Seiyon speaks softly: *"Batch 1 is officially concluded, Director. Twenty-five days without a fatality. The operatives are confident. The gear is holding."*

Majin turns toward the dark expanse of Floor 5, where Border Lead Mellda's wardens are already fortifying the blast doors for the upcoming shift:

*"Do not let them grow complacent, Seiyon. On Day 29, the Smothering Mother will test our resolve. And beyond her lies the deep forest."*

Majin places his hand upon the central terminal, locking the master ledgers of Batch 1.

The convergence accelerates. Reserves stand at 48.55 tons. The dawn draws closer.
"""
    return content

def update_part_2():
    path = "SOMNARAK-WORLD/The_Absolvohan/Part_2_Days_1_to_25.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the end of Day 17
    # Replace Day 17 nocturnal vigil conclusion with smooth transition to Day 21
    old_end = """Batch 1 is officially complete. Reserves stand at 47.92 tons. The convergence builds."""
    
    new_day_17_end = """Reserves stand at 47.92 tons. Day 17 concludes smoothly as the Directorate prepares for the arrival of the avian triad."""
    
    if old_end in content:
        content = content.replace(old_end, new_day_17_end)
    else:
        print("Warning: old_end text not found directly, checking variations...")

    day_21 = generate_day_21()
    day_25 = generate_day_25()

    content = content + "\n" + day_21 + "\n" + day_25

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully updated Part 2 with Day 21 and Day 25!")

if __name__ == "__main__":
    update_part_2()
