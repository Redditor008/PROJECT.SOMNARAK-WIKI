#!/usr/bin/env python3
"""
tools/build_jipyeongseondae_arcs_1_to_3.py
Generates:
- SOMNARAK-WORLD/Jipyeongseondae/Arc_1_Departure.md
- SOMNARAK-WORLD/Jipyeongseondae/Arc_2_The_Desolate_Crossing.md
- SOMNARAK-WORLD/Jipyeongseondae/Arc_3_Arrival_at_Cheonbulok.md
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

def generate_arc_1():
    dossier_box = make_box("EXPEDITION DOSSIER: ARC 1 - THE EXILE'S GATE", [
        "OPERATION NAME     : Arc 1 - Departure from Somnarak",
        "PRIMARY THEATER    : Somnarak Zone E - The Exile's Gate",
        "DATE & EPOCH       : Year 4238, Month 1 (Post-Absolvohan Activation)",
        "PRIMARY ADVERSARY  : Warden Battery Commander Vane & Fort Interdiction",
        "---",
        "ADVERSARY PROFILE (WARDEN INTERDICTION FORTRESS):",
        "- Total Health (HP): 4,800 HP | Posture Pool: 340/340",
        "- Stagger 1 Proc   : 60% Posture Strain (204 Posture) / Battery Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Fortress Capitulation)",
        "- Resistances      : Weight 2.0x (Fatal), Grudge 1.5x, Void 0.5x, Lament 0.5x",
        "---",
        "TARGETABLE COMBAT ANCHORS:",
        "1. Rail Battery    : 1,200 HP | Posture 280/280 (Heavy anti-armor kinetic)",
        "2. Aegis Shield    : 1,500 HP | Posture 300/300 (Forcefield generator)",
        "3. Bunker Core     : 2,100 HP | Posture 340/340 (Vane's command redoubt)"
    ])

    hud_t01 = make_box("TACTICAL STAGE HUD: ARC 01 - BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 - SOMNARAK ZONE E EXILE'S GATE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RAMPS] [SCOUT] [BERM]  [KILL]  [FORT]  [C-WALK][WALL]  [SUMP]  [VENT]  [THRONE]",
        "[KAEL]  [HWARAN]                [VANE]                                  [HELM]  ",
        "---",
        "- Node 01: Drift Throne Debarkation Ramps (Kael Vanguard Band 1)",
        "- Node 02: Dune Scouts & Hwaran (Short Band 2 / Sand-Skimmer Support)",
        "- Node 03: Concrete Berms (Heavy Dredgers Deploying Ballistic Shields)",
        "- Node 04: The Killing Zone (Zone E Automated Minefield & Barbed Wire)",
        "- Node 05: Fort Interdiction (Commander Vane, Kinetic Rail Battery)",
        "- Node 06: Elevated Wall Catwalk (Warden Marksmen / Sniper Array)",
        "- Node 07: High Bastion Wall (Long-Range Mortar Battery)",
        "- Node 10: Drift Throne Bridge & Siege Battery (Helm Command)",
        "---",
        "- Kael        : Spd 7 -> 4 AP | HP 3,800/3,800 | SP 50/50 | Posture 160/160",
        "- Hwaran      : Spd 6 -> 3 AP | HP 2,600/2,600 | SP 45/45 | Posture 110/110",
        "- Fort Core   : Spd 4 -> 2 AP | HP 2,100/2,100 | Posture 340/340 [LOCKED]",
        "- Rail Battery: Spd 6 -> 3 AP | HP 1,200/1,200 | Posture 280/280 [CHARGING]",
        "- Aegis Shield: Spd 3 -> 1 AP | HP 1,500/1,500 | Posture 300/300 [ACTIVE]"
    ])

    hud_t02 = make_box("TACTICAL STAGE HUD: ARC 01 - BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 - RAIL BATTERY DISMANTLED & TRENCH ADVANCE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RAMPS]         [SCOUT] [KAEL]  [FORT]  [C-WALK][WALL]  [SUMP]  [VENT]  [THRONE]",
        "                [HWARAN][SHARDS]                                                ",
        "---",
        "- Node 03: Hwaran (Thermal Ash Screen Blinding Wall Marksmen)",
        "- Node 04: Kael (Obsidian Trench-Cleaver Shearing Battery Elevation Mount)",
        "- Node 05: Fort Interdiction (Rail Battery Destroyed 0/1,200 HP)",
        "- Node 06: Wall Marksmen (Suppressed by Heavy Dredger Counter-Fire)",
        "---",
        "- Kael        : Spd 9 -> 5 AP [SURGE] | HP 3,800/3,800 | SP 50/50 | Posture 160/160",
        "- Fort Core   : Spd 3 -> 1 AP | HP 2,100/2,100 | Posture 260/340",
        "- Rail Battery: DESTROYED (0/1,200 HP) | MAIN CANNON SUPPRESSED",
        "- Aegis Shield: Spd 3 -> 1 AP | HP 1,210/1,500 | Posture 238/300"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: ARC 01 - BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 - STAGGER THRESHOLD 1 & AEGIS SHATTER]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RAMPS]                 [SCOUT] [KAEL]  [C-WALK][WALL]  [SUMP]  [VENT]  [THRONE]",
        "                        [HWARAN][FORT]                                          ",
        "---",
        "- Node 04: Hwaran (Overheating Shield Capacitor with Slag Sparks)",
        "- Node 05: Kael (Han-Glass Seismic Tremor Punch Breaching Bunker Door)",
        "- Node 05: Fort Interdiction (STAGGER LEVEL 1 / SHIELD COLLAPSED)",
        "- Node 06: Wall Snipers (Fleeing to Rear Bastion Ramps)",
        "---",
        "- Kael        : Spd 8 -> 4 AP [SURGE] | HP 3,800/3,800 | SP 50/50 | Posture 160/160",
        "- Fort Core   : Spd 0 -> 0 AP | HP 1,820/2,100 | Posture 130/340 [STAGGER LEVEL 1]",
        "- Aegis Shield: Spd 0 -> 0 AP | HP 620/1,500   | Posture 102/300 [SHATTERED]",
        "- Total Fort  : HP 2,440/4,800 [THRESHOLD BREACHED / TAKES 1.5X DAMAGE]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: ARC 01 - BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 - MAXIMUM BURST & PHASE 2 THRESHOLD SKIP]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RAMPS]                         [KAEL]  [C-WALK][WALL]  [SUMP]  [VENT]  [THRONE]",
        "                                [FORT]                                          ",
        "---",
        "- Node 05: Kael (Obsidian Cleaver Execution Barrage on Command Vault)",
        "- Node 05: Fort Interdiction (Immobilized / Steam Venting / Gates Buckling)",
        "- Node 05: Heavy Dredgers (Hydraulic Pile-Driver Smashing Steel Portcullis)",
        "- Node 10: Drift Throne Siege Gun (Broadside Sonic Disruptor Blast)",
        "---",
        "- Kael        : Spd 11 -> 5 AP [BURST CRIT] | HP 3,800/3,800 | SP 50/50",
        "- Fort Core   : Spd 0 -> 0 AP  | HP 590/2,100  | Posture 52/340",
        "- Aegis Shield: DESTROYED (0/1,500 HP)",
        "- Total Fort  : HP 590/4,800 [BURST DAMAGE 1,850! SECOND THRESHOLD SKIPPED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: ARC 01 - BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 - VANE'S LAST STAND & DRIFT KING'S WILL]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RAMPS]                         [KAEL]  [C-WALK][WALL]  [SUMP]  [VENT]  [THRONE]",
        "                                [VANE]                                          ",
        "---",
        "- Node 05: Kael (Relic Overdrive: OATH OF THE UNCHAINED HORIZON)",
        "- Node 05: Commander Vane (Last Stand: Emergency Fortress Meltdown Overload)",
        "- Node 04: Hwaran (Deploying Volcanic Slag Insulation Net)",
        "- Node 10: Drift Throne Helm (Engaging Full Forward Ley-Drive Motors)",
        "---",
        "- Kael        : Spd 9 -> 5 AP [OVERDRIVE] | HP 3,800/3,800 | SP 50/50 [RESOLVE]",
        "- Fort Core   : Spd 3 -> 1 AP | HP 590/2,100   | Posture 26/340 [CONTAINED]",
        "- Total Fort  : HP 590/4,800 [MELTDOWN QUENCHED / VANE PARRIED TO RESTRAINT]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: ARC 01 - BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 - TREATY RATIFICATION & BLAST GATES OPENED]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RAMPS]                 [CARAVAN]       [OPEN]          [DESOLATE WASTELAND]    ",
        "                        [TREATY]        [GATE]                                  ",
        "---",
        "- Node 05: Fort Interdiction (CAPITULATED / VANE CONCEDES WITH RESPECT)",
        "- Node 05: Kael & Council Envoy (Expedition Charter Ratified)",
        "- Node 07: Blast Gate V (Sovereign Portcullis Raised / Desolate Revealed)",
        "- Node 10: Drift Throne (Engaging Quadruple Tracks / MARCH BEGINS)",
        "---",
        "- Squad Status: Zero Casualties | Morale 50/50 SP (Unshakable Conviction)",
        "- Reception Status: 100% RESOLVED | Expedition Departure Cleared"
    ])

    return f"""# Arc 1: Departure — Somnarak Zone E & The Exile's Gate (출항 — 추방자의 관문)
## The Horizon Caravan Chronicles — Planetary Overland Expedition (Year 4238, Month 1)

```text
{dossier_box}
```

> *"For forty-six years, this gate was a one-way grave. They marched you past the iron teeth, sealed the hydraulic blast doors behind you, and washed your name from the census. Today, we do not sneak past the gate. Today, the gate opens for us."*  
> — Kael, The Drift King, standing before Blast Gate V

---

### Narrative Prologue: The Iron Perimeter

In the first month of Year 4238, the monstrous roar of four sets of industrial caterpillar tracks shook the reinforced concrete foundations of Somnarak's western border wall: **Zone E — The Exile's Gate**.

Rising above the rusty corrugated shanties of the outer scrap-slums was **The Drift Throne**. The 140-meter land cruiser halted fifty paces before the cyclopean adamantine portcullis of Blast Gate V. Its twin ley-siphon probes hissed as they grounded into the rock, venting clean steam into the soot-choked air.

Standing atop the bastion ramparts was **Warden Battery Commander Vane**, accompanied by three platoons of border wardens. The heavy dual kinetic cannons of the fortress battery traversed down, locking their twin rifled barrels onto the mobile crawler's bridge.

*"Halt, exile!"* Vane's voice thundered through the fortress loudspeakers. *"You are a condemned traitor under Section 12 of the Municipal Bulwark Code. Order your nomads to dismount and submit to quarantine shackles, or this battery will reduce your scrap-barge to slag!"*

Aboard the forward catwalk of the crawler, Kael adjusted his leather duster. His left arm—an articulated limb of pale, translucent Han-glass that hummed with seismic resonance—rested on the hilt of his massive Obsidian Trench-Cleaver.

*"I did not bring four thousand tons of steel across three hundred leagues of salt to die on your doorstep, Commander,"* Kael answered, his gravelly voice carrying cleanly over the wind. *"Somnarak's Council of Sighs signed an expedition pact with the Dawn Initiative. You were ordered to raise the gate."*

*"The Council sits two kilometers below ground in luxury!"* Vane barked. *"They don't know the wastes like I do. Nothing leaves this city. Nothing enters. Gun crews—commence firing!"*

The massive cannons roared. The siege of the Exile's Gate had begun.

---

### Expedition Combat Gauntlet: Arc 1 (6-Turn Resolution)

```text
{hud_t01}
```

###### Turn 01 Action Resolution Log (Intercepting the Heavy Kinetic Rail Cannon)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Kael initializes `[Planetary Ley-Stance]`: Grants $+3$ Protection and immune to kinetic knockback.
  * Hwaran readies her `[Volcanic Ash Shroud]`, preparing thermal blinding smoke.
  * Fort Interdiction activates `[Overwatch Targeting Grid]`: Increases kinetic accuracy by $+20\\%$.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael (Speed 7 -> 4 AP, Warden Heavy Rig delta $-1$, Poise $+20$): Advances to Node 02. Spends 2 AP on `[Obsidian Cleaver: Bulwark Intercept]`. Holds 2 AP in Reserve.
  * Hwaran (Speed 6 -> 3 AP, Light Skimmer delta $+1$): Holds Node 02. Spends 2 AP on `[Thermal Ash Screen]`. Holds 1 AP in Guard.
  * Commander Vane (Speed 6 -> 3 AP): Holds Node 05. Spends 2 AP on `[Dual Kinetic Rail Barrage]`. Spends 1 AP on `[Aegis Forcefield Pulse]`.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 02 to 05)**: Fort Interdiction fires `[Dual Kinetic Rail Barrage]` (Base 18 + 2 Coins = 28 Power, Heavy Weight/Kinetic).
    * Kael intercepts with `[Obsidian Cleaver: Bulwark Intercept]` (Base 21 + 2 Coins = 33 Power, Obsidian Guard).
    * **Clash Outcome**: Kael WINS THE CLASH OVERWHELMINGLY (33 vs 28)!
    * Kael plants his glass arm into the ground, angling his five-foot obsidian blade directly into the incoming 150mm kinetic sabot shell (`[P3: Parry/Protection]`).
    * The armor-piercing round shatters against the indestructible outer edge, deflecting skyward to detonate harmlessly against the upper concrete parapet!
    * Kael channels the seismic shockwave back through the bedrock, dealing **260 kinetic tremor damage** to the rail battery's hydraulic elevation carriage!
  * **Clash 2 (Node 02 to 06)**: Wall snipers target Hwaran.
    * Hwaran's `[Thermal Ash Screen]` covers the roadway in dense, boiling black ash, completely breaking line of sight; snipers miss entirely.
- **Step 4: Turn End State**:
  * Rail Battery HP: 1,200 -> **940/1,200** | Posture: **226/280**.
  * Total Fort HP: 4,800 -> **4,540/4,800** | Posture: **286/340**.
  * Kael Composure: **100% (50/50 SP)**. Zero damage taken.

---

```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Part Destruction: Rail Battery Dismantled)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Kael activates `Ley-Surge` (+2 Speed next turn -> Net Speed 9, 5 AP).
  * Commander Vane attempts emergency hydraulic realignment for a point-blank blast.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael (Speed 9 -> 5 AP [Surge]): Dashes through the smoke to Node 04. Spends 3 AP on `[Obsidian Trench-Cleaver: Sunder Mounting]`. Spends 2 AP on `[Seismic Leap]`.
  * Hwaran (Speed 6 -> 3 AP): Moves to Node 03. Spends 2 AP on `[Molten Slag Dart]`.
  * Heavy Dredgers: Advance to Node 03 with deployable ballistic shields.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 04 to 05)**: Rail Battery fires emergency canister shot `[Close-Range Shrapnel Blast]` (Base 17 + 2 Coins = 25 Power).
    * Kael clashes with `[Obsidian Trench-Cleaver: Sunder Mounting]` (Base 25 + 3 Coins Heads = 43 Power, Heavy Slash).
    * **Clash Outcome**: Kael WINS THE CLASH OVERWHELMINGLY (43 vs 25)!
    * Kael vaults atop the battery cupola and drives his obsidian blade down through the hydraulic swivel ring!
    * Hwaran's `[Molten Slag Dart]` strikes the exposed ammunition feed belt, cooking off the propellants in the loading tray!
    * Deals **940 Critical Weight/Fire damage** (Fatal 2.0x proc!)!
    * **TARGETED PART DESTROYED**: The Kinetic Rail Battery is completely demolished (**Battery HP: 0/1,200**)!
    * **EFFECT**: Fortress kinetic heavy barrage disabled; fort permanently loses 1 Speed Slot!
  * **Aegis Shield Damage**:
    * Sapper shockwave fractures the outer forcefield projector for **290 Blunt damage**!
- **Step 4: Turn End State**:
  * Rail Battery: **DESTROYED (0/1,200 HP)**.
  * Aegis Shield: 1,500 -> **1,210/1,500** | Posture: **238/300**.
  * Total Fort HP: 4,540 -> **3,310/4,800** | Posture: **206/340 [BATTERY SEVERED]**.
  * Kael Composure: Stable (50/50 SP).

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (First Stagger Proc & Aegis Forcefield Shatter)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Stripped of his cannons, Vane engages the fort's emergency defenses: `[Overloaded Aegis Shockwave]` (Area Kinetic/Force, 2 Coins).
  * Kael gains `Ley-Surge` (+2 Speed -> Net Speed 8, 4 AP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael (Speed 8 -> 4 AP): Holds Node 04. Spends 2 AP on `[Han-Glass Tremor Strike]`. Spends 2 AP on `[Rooted Fortress Stance]`.
  * Hwaran (Speed 6 -> 3 AP): Stands at Node 03. Spends 2 AP on `[Slag Spark Thermal Overload]`.
  * Heavy Dredgers: Anchor hydraulic braces into the asphalt.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 04 to 05)**: Fort Interdiction unleashes `[Overloaded Aegis Shockwave]` (Base 18 + 2 Coins = 26 Power).
    * Kael clashes with `[Han-Glass Tremor Strike]` (Base 23 + 2 Coins = 35 Power, Seismic Shatter).
    * **Clash Outcome**: Kael WINS THE CLASH (35 vs 26)!
    * Kael slams his crystalline glass fist straight into the focal emitter of the blue forcefield!
    * Hwaran's slag sparks ignite the ozone discharge coils, sending a catastrophic feedback loop through the generator!
    * Deals **590 Weight/Thermal damage** and $+98$ Posture Strain!
- **Step 4: STAGGER THRESHOLD 1 TRIGGERED!**:
  * Fort HP crosses 70% threshold (3,360 HP), dropping to **2,440/4,800 HP**; Posture crosses 60% strain line!
  * **STAGGER LEVEL 1 ACTIVE!** The blue forcefield shatters into blinding sparks; bunker blast doors crack open; fortress takes $+50\%$ damage!
- **Step 5: Turn End State**:
  * Total Fort HP: 3,310 -> **2,440/4,800 [THRESHOLD BREACHED: Below 3,360 HP!]**.
  * Aegis Shield: 1,210 -> **620/1,500** | Posture: **102/300 [CRACKED]**.
  * Fort Posture: **130/340 [STAGGER LEVEL 1]**.
  * Kael Status: Unbroken.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Maximum Burst & Phase 2 Threshold Skip)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * The bunker gate is buckled and smoking; Vane's inner command redoubt is exposed.
  * Kael coordinates an all-out combined-arms offensive to incapacitate the fort without civilian casualties.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael (Speed 11 -> 5 AP, Momentum Crit): Storms Node 05. Spends 3 AP on `[Obsidian Cleaver Execution Barrage]`. Spends 2 AP on `[Earth-Shaker Ground Slam]`.
  * Heavy Dredgers: Deliver `[Hydraulic Pile-Driver Impact]` (3 AP).
  * Drift Throne: Fires `[Broadside Sonic Disruptor]` from Node 10 (2 AP).
- **Step 3: Unopposed Stagger Punishment Rotation**:
  * Kael's `[Obsidian Cleaver Execution Barrage]`: Shatters the bunker stanchions for **1,020 Weight damage** (Fatal 2.0x proc!)!
  * Kael's `[Earth-Shaker Ground Slam]`: Slices through the remaining shield relays for **420 Blunt damage**!
  * Dredgers' `[Pile-Driver]`: Rams the portcullis lock pins for **260 Heavy damage**!
  * Drift Throne's `[Sonic Disruptor]`: Pulverizes communication arrays for **150 Void damage**!
  * **TOTAL BURST DAMAGE: 1,850 DAMAGE!**
- **Step 4: SECOND STAGGER THRESHOLD (1,920 HP) COMPLETELY SKIPPED!**:
  * Fort HP plunges from 2,440 down to **590/4,800 HP**! Aegis Shield completely destroyed (0/1,500 HP)!
  * **Phase 2 Emergency Activation Triggered!**
- **Step 5: Turn End State**:
  * Total Fort HP: 2,440 -> **590/4,800** (Core HP: **590/2,100** | Shield: **DESTROYED**).
  * Posture: **52/340**.

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Phase 2 Escalation: Emergency Meltdown & Oath of the Horizon)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Desperate and bleeding from shrapnel, Commander Vane reaches for the emergency reactor purge lever to incinerate the gate corridor!
  * Fort Special Skill: `[Emergency Fortress Meltdown Overload]` (Area Thermal Annihilation, 3 Coins).
  * Kael activates Relic Overdrive: `[OATH OF THE UNCHAINED HORIZON — MAXIMUM]` (Cost: 3 AP, 30 SP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael (Speed 9 -> 5 AP [Overdrive]): Steps directly into the smoking bunker bridge at Node 05, raising his glass arm.
  * Hwaran: Deploys volcanic slag insulation net around the cooling pipes.
  * Drift Throne: Pours full acoustic reverse harmonics into the gate footing.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 05 to 05)**: Fort Interdiction attempts `[Emergency Fortress Meltdown Overload]` (Base 21 + 3 Coins = 33 Power).
    * Kael clashes with `[OATH OF THE UNCHAINED HORIZON — MAXIMUM]` (Base 29 + 3 Coins Heads = 49 Power, Sovereign Will).
    * **Clash Outcome**: KAEL SUPREME OVERDRIVE CLASH WIN (49 vs 33)!
    * Kael's obsidian blade pins Vane's hand to the console inches from the purge switch (`[P3: Parry/Protection]`).
    * His glowing glass arm grips the overheating cooling manifold, channeling the geothermal heat directly into his own crystallized bones!
    * Kael roars: *"You served this city for thirty years, Vane. Don't die for a gate that's already fallen!"*
    * The emergency sirens wind down into dead silence! Meltdown safely aborted!
    * Zero squad damage taken! Kael's Composure remains maxed at 50/50 SP!
- **Step 4: Turn End State**:
  * Total Fort HP: **590/4,800** | Posture: **26/340 [MELTDOWN ABORTED]**.
  * Kael Composure: 50/50 SP.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Treaty Ratification & Departure into the Desolate)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Hostilities cease. Posture reaches **0/340 [CAPITULATION]**.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael releases Vane, offering his flesh hand to pull the commander to his feet.
- **Step 3: Resolution & Departure**:
  * Commander Vane coughs up soot, looking out through the shattered embrasure at the colossal form of the Drift Throne and the thousands of cheering nomads lining its decks.
  * *"You're out of your mind, Kael,"* Vane wheezes, wiping blood from his brow. *"You're driving four thousand people into an ocean of glass."*
  * *"Better an ocean of glass with the stars overhead,"* Kael replies, handing Vane the official Council parchment, *"than a concrete cage where people forget how to breathe."*
  * Vane presses his command seal to the document. He raises the emergency telephone:
    > *"All posts, this is Command. Stand down. Disengage locks. Raise Blast Gate Five. The Horizon Caravan has the right of way."*
  * With a grinding shriek that echoes across the entire western hemisphere of Somnarak, the 200-ton adamantine teeth of Blast Gate V rise into the ceiling.
  * The Drift Throne engages its four massive track assemblies. The 140-meter behemoth rolls forward through the archway, breaking the boundary line of Somnarak and descending onto the endless golden-red dunes of **The Desolate**.
  * Deals **590 Peaceful Capitulation**! Fort HP reaches 0!
- **Step 4: Operational Artifact Extraction & Milestones**:
  * **Charter Acquired**: `[Overland Planetary Transit Charter: Year 4238]`.
  * **Transit Clearance**: Somnarak perimeter cleared. Permanent overland route established.
  * **Casualties**: Zero Squad Casualties. Kael HP 3,800/3,800. Composure 50/50 SP."""

def generate_arc_2():
    dossier_box = make_box("EXPEDITION DOSSIER: ARC 2 - THE DESOLATE CROSSING", [
        "OPERATION NAME     : Arc 2 - Crossing the Sea of Glass",
        "PRIMARY THEATER    : The Desolate - Mid-Basin Salt Dunes (Km 1,120)",
        "DATE & EPOCH       : Year 4238, Months 2-3 (Deep Wasteland Transit)",
        "PRIMARY ADVERSARY  : The Glass-Dune Colossus (SE-IV Titanic Sand Burrower)",
        "---",
        "ADVERSARY PROFILE (THE GLASS-DUNE COLOSSUS):",
        "- Total Health (HP): 5,600 HP | Posture Pool: 380/380",
        "- Stagger 1 Proc   : 60% Posture Strain (228 Posture) / Mandible Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Titanic Submersion)",
        "- Resistances      : Heat 2.0x (Fatal), Lament 1.5x, Weight 0.5x, Void 0.5x",
        "---",
        "TARGETABLE COMBAT ANCHORS:",
        "1. Sand Mandibles  : 1,400 HP | Posture 300/300 (Crushing vitrified jaws)",
        "2. Dorsal Carapace : 1,800 HP | Posture 340/340 (Razor obsidian spine plates)",
        "3. Resonance Heart : 2,400 HP | Posture 380/380 (Pulsing subterranean core)"
    ])

    hud_t01 = make_box("TACTICAL STAGE HUD: ARC 02 - BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 - SEA OF GLASS HAN-STORM (KM 1,120)]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RAMPS] [SKIM]  [BERM]  [SINK]  [MAW]   [SPINE] [CREST] [CHASM] [VENT]  [THRONE]",
        "[KAEL]  [HWARAN]                [COLOSS]                                [HELM]  ",
        "---",
        "- Node 01: Drift Throne Bow Ramps (Kael Vanguard Band 1)",
        "- Node 02: Sand-Skimmers & Hwaran (Short Band 2 / Harpoon Launchers)",
        "- Node 03: Hydraulic Dune Berms (Heavy Dredgers Anchoring Treads)",
        "- Node 04: Liquefied Sand Basin (Subterranean Vibration Vortex)",
        "- Node 05: The Glass-Dune Colossus Maw (Vitrified Sand Mandibles)",
        "- Node 06: Colossus Dorsal Spines (Razor Obsidian Armor Plates)",
        "- Node 07: Shifting Dune Crest (Acoustic Pylon Beacon Line)",
        "- Node 10: Drift Throne Bridge & Sonar Array (Ley-Drive Full Throttle)",
        "---",
        "- Kael        : Spd 7 -> 4 AP | HP 3,800/3,800 | SP 50/50 | Posture 160/160",
        "- Hwaran      : Spd 6 -> 3 AP | HP 2,600/2,600 | SP 45/45 | Posture 110/110",
        "- Coloss Core : Spd 5 -> 3 AP | HP 2,400/2,400 | Posture 380/380 [SUBMERGED]",
        "- Sand Mandib : Spd 6 -> 3 AP | HP 1,400/1,400 | Posture 300/300 [CRUSHING]",
        "- Dorsal Carap: Spd 3 -> 1 AP | HP 1,800/1,800 | Posture 340/340 [ARMORED]"
    ])

    hud_t02 = make_box("TACTICAL STAGE HUD: ARC 02 - BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 - MANDIBLES SHATTERED & SLAG INJECTION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RAMPS]         [SKIM]  [KAEL]  [COLOSS][SPINE] [CREST] [CHASM] [VENT]  [THRONE]",
        "                [HWARAN][SHARDS]                                                ",
        "---",
        "- Node 03: Hwaran (Volcanic Magma Dart Melting Vitrified Armor)",
        "- Node 04: Kael (Obsidian Cleaver Shearing Left Mandible Pin)",
        "- Node 05: Glass-Dune Colossus (Sand Mandibles Destroyed 0/1,400 HP)",
        "- Node 06: Dorsal Spines (Exposed to Concentrated Crawler Fire)",
        "---",
        "- Kael        : Spd 9 -> 5 AP [SURGE] | HP 3,800/3,800 | SP 50/50 | Posture 160/160",
        "- Coloss Core : Spd 4 -> 2 AP | HP 2,400/2,400 | Posture 290/380",
        "- Sand Mandib : DESTROYED (0/1,400 HP) | CRUSHING BITE PERMANENTLY LOST",
        "- Dorsal Carap: Spd 3 -> 1 AP | HP 1,480/1,800 | Posture 272/340"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: ARC 02 - BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 - STAGGER THRESHOLD 1 & CARAPACE FRACTURE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RAMPS]                 [SKIM]  [KAEL]  [SPINE] [CREST] [CHASM] [VENT]  [THRONE]",
        "                        [HWARAN][COLOSS]                                        ",
        "---",
        "- Node 04: Hwaran (Boiling Slag Geyser Cracking Dorsal Scutes)",
        "- Node 05: Kael (Seismic Glass-Arm Punch Popping Spine Hinges)",
        "- Node 05: Glass-Dune Colossus (STAGGER LEVEL 1 / HEAD PINNED IN DUST)",
        "- Node 10: Drift Throne (Launching Pneumatic Harpoon Anchors)",
        "---",
        "- Kael        : Spd 8 -> 4 AP [SURGE] | HP 3,800/3,800 | SP 50/50 | Posture 160/160",
        "- Coloss Core : Spd 0 -> 0 AP | HP 2,080/2,400 | Posture 146/380 [STAGGER LEVEL 1]",
        "- Dorsal Carap: Spd 0 -> 0 AP | HP 760/1,800   | Posture 120/340 [FRACTURED]",
        "- Total Coloss: HP 2,840/5,600 [THRESHOLD BREACHED / TAKES 1.5X DAMAGE]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: ARC 02 - BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 - MAXIMUM BURST & PHASE 2 THRESHOLD SKIP]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RAMPS]                         [KAEL]  [COLOSS][CREST] [CHASM] [VENT]  [THRONE]",
        "                                [BURST]                                         ",
        "---",
        "- Node 05: Kael (Obsidian Cleaver Seismic Execution on Resonance Heart)",
        "- Node 05: Glass-Dune Colossus (Immobilized / Liquid Han-Brine Venting)",
        "- Node 05: Hwaran (Thermal Firestorm Incinerating Sub-Carapace Glands)",
        "- Node 10: Drift Throne Siege Gun (Direct High-Yield Acoustic Torpedo)",
        "---",
        "- Kael        : Spd 11 -> 5 AP [BURST CRIT] | HP 3,800/3,800 | SP 50/50",
        "- Coloss Core : Spd 0 -> 0 AP  | HP 680/2,400  | Posture 58/380",
        "- Dorsal Carap: DESTROYED (0/1,800 HP)",
        "- Total Coloss: HP 680/5,600 [BURST DAMAGE 2,160! SECOND THRESHOLD SKIPPED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: ARC 02 - BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 - HAN-STORM DELUGE & LEY-SONG HARMONIZATION]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RAMPS]                         [KAEL]  [COLOSS][CREST] [CHASM] [VENT]  [THRONE]",
        "                                [SONG]                                          ",
        "---",
        "- Node 05: Kael (Relic Overdrive: SONG OF THE BURIED EARTH)",
        "- Node 05: Colossus (Last Stand: Category-5 Supercell Han-Glass Vortex)",
        "- Node 04: Hwaran (Expanding Slag Thermal Dome Over Refugee Trailers)",
        "- Node 10: Drift Throne Helm (Synchronizing Ley-Siphon Sonar at 528 Hz)",
        "---",
        "- Kael        : Spd 9 -> 5 AP [OVERDRIVE] | HP 3,800/3,800 | SP 50/50 [RESOLVE]",
        "- Coloss Core : Spd 3 -> 1 AP | HP 680/2,400   | Posture 28/380 [VORTEX CALMED]",
        "- Total Coloss: HP 680/5,600 [GLASS SHARDS COALESCED INTO HARMLESS SILT]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: ARC 02 - BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 - COLOSSUS PACIFICATION & SAFE PASSAGE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RAMPS]                 [CARAVAN]       [BEHEM]         [OPEN HORIZON HIGHWAY]  ",
        "                        [TRANSIT]       [PEACE]                                 ",
        "---",
        "- Node 05: Glass-Dune Colossus (PACIFIED / SUBMERGING GENTLY INTO DEEP LEY)",
        "- Node 05: Kael (Standing Atop Sand Crest / Acoustic Resonance Complete)",
        "- Node 07: The Sea of Glass (Storm Dissipated / Golden Sand Corridor Clear)",
        "- Node 10: Drift Throne (Full Ahead Flank / Cheonbulok Heading Locked)",
        "---",
        "- Squad Status: Zero Casualties | Morale 50/50 SP (Triumphant Conviction)",
        "- Reception Status: 100% RESOLVED | Sea of Glass Traversed"
    ])

    return f"""# Arc 2: The Desolate Crossing — The Sea of Glass (황야 횡단 — 유리의 바다)
## The Horizon Caravan Chronicles — Planetary Overland Expedition (Year 4238, Months 2-3)

```text
{dossier_box}
```

> *"The sand here is not rock ground down by wind. It is tears frozen by a sun that died before our ancestors learned to speak. If you panic, the earth swallows you. If you sing to it, it lets you pass."*  
> — Kael, navigating the Mid-Basin Glass Dunes

---

### Narrative Prologue: The Shifting Sands

Two months into the trans-continental expedition, the Horizon Caravan had entered the deepest, most treacherous quadrant of the planetary wasteland: **The Sea of Glass (유리의 바다)**, located 1,120 kilometers southeast of Somnarak.

Here, the dunes rose three hundred meters high, composed entirely of crystalline Han-silica that reflected the pale sky like fractured mirrors. The temperature plummeted to $-35^\\circ\\text{{C}}$ at dusk, and supersonic thermal downdrafts whipped the dunes into violent glass-storms capable of shredding vulcanized steel treads.

From the bridge of the Drift Throne, the Ley-Seers screamed a seismic warning:
*"Massive subterranean displacement detected at bearing 140! Depth minus eighty meters and rising at fifty kilometers per hour! It's not a dune—it's a Colossus!"*

With a sound like the shattering of a thousand glaciers, the desert floor ruptured. Rising two hundred meters into the howling storm was **The Glass-Dune Colossus (유리사구 거수)**—a titanic SE-IV burrower whose segmented carapace was made of vitrified obsidian plates, and whose gaping maw was ringed with six rows of crushing mineral mandibles.

A category-5 Han-storm boiled around its crown, threatening to flip the 18,000-ton crawler onto its side.

*"All hands, lock magnetic dune anchors!"* Kael roared, leaping from the bow ramps onto the shifting sand. *"Hwaran, prime your slag darts! We don't turn back!"*

---

### Expedition Combat Gauntlet: Arc 2 (6-Turn Resolution)

```text
{hud_t01}
```

###### Turn 01 Action Resolution Log (Intercepting the Vitrified Sand Mandibles)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Kael initializes `[Planetary Ley-Stance]`: Grants $+3$ Protection and immunity to quicksand entrapment.
  * Hwaran prepares `[Thermal Slag Barrier]`, warming squad footing against $-35^\\circ\\text{{C}}$ frostbite.
  * The Colossus activates `[Seismic Liquefaction]`: Turns Nodes 03 to 05 into shifting sinkholes.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael (Speed 7 -> 4 AP, Warden Heavy Rig delta $-1$, Poise $+20$): Holds Node 01. Spends 2 AP on `[Obsidian Cleaver: Mandible Intercept]`. Holds 2 AP in Reserve.
  * Hwaran (Speed 6 -> 3 AP): Stands at Node 02. Spends 2 AP on `[Thermal Slag Dart]`. Holds 1 AP in Guard.
  * The Colossus (Speed 6 -> 3 AP, Behemoth Class delta $-2$, Poise $+40$): Charges Node 01 with `[Titan Mandible Chomp]`.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 01 to 05)**: The Colossus strikes with `[Titan Mandible Chomp]` (Base 19 + 2 Coins = 29 Power, Heavy Weight/Crush).
    * Kael intercepts with `[Obsidian Cleaver: Mandible Intercept]` (Base 22 + 2 Coins = 34 Power, Obsidian Deflection).
    * **Clash Outcome**: Kael WINS THE CLASH OVERWHELMINGLY (34 vs 29)!
    * Kael wedges his massive obsidian cleaver crosswise inside the beast's upper mandible hinges (`[P3: Parry/Protection]`).
    * His crystalline left arm pulses with harmonic counter-frequencies, freezing the colossal jaw open!
    * Deals **280 kinetic tremor damage** into the mandible socket!
  * **Clash 2 (Node 02 to 05)**: Hwaran fires `[Thermal Slag Dart]`.
    * The molten projectile strikes the beast's frozen snout, causing vitrified silica to crack with violent thermal shock; inflicts $+45$ Posture Strain!
- **Step 4: Turn End State**:
  * Sand Mandibles HP: 1,400 -> **1,120/1,400** | Posture: **240/300**.
  * Total Colossus HP: 5,600 -> **5,320/5,600** | Posture: **325/380**.
  * Kael Composure: **100% (50/50 SP)**. Zero damage taken.

---

```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Part Destruction: Sand Mandibles Shattered)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Kael activates `Ley-Surge` (+2 Speed next turn -> Net Speed 9, 5 AP).
  * The Colossus attempts `[Subterranean Thrap Deluge]` to drag the crawler under.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael (Speed 9 -> 5 AP [Surge]): Steps onto the beast's lower jaw at Node 04. Spends 3 AP on `[Obsidian Cleaver: Mandible Cleave]`. Spends 2 AP on `[Dune Vault]`.
  * Hwaran (Speed 6 -> 3 AP): Moves to Node 03. Spends 2 AP on `[Boiling Slag Jet]`.
  * Heavy Dredgers: Fire pneumatic tension cables to secure the beast's head.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 04 to 05)**: The Colossus thrashes with `[Subterranean Thrap Deluge]` (Base 18 + 2 Coins = 26 Power).
    * Kael clashes with `[Obsidian Cleaver: Mandible Cleave]` (Base 25 + 3 Coins Heads = 43 Power, Heavy Slash).
    * **Clash Outcome**: Kael WINS THE CLASH OVERWHELMINGLY (43 vs 26)!
    * Kael brings his cleaver down in an arc of concentrated kinetic weight, slicing through the left mandible hinge!
    * Hwaran's `[Boiling Slag Jet]` pours superheated iron directly into the exposed wound, thermal-shattering the entire jaw array!
    * Deals **1,120 Critical Thermal/Weight damage** (Fatal 2.0x proc!)!
    * **TARGETED PART DESTROYED**: The Vitrified Sand Mandibles are completely destroyed (**Mandibles HP: 0/1,400**)!
    * **EFFECT**: Colossus crushing attack permanently disabled; boss permanently loses 1 Speed Slot!
  * **Dorsal Carapace Damage**:
    * Sapper shockwave cracks the dorsal plates for **320 Blunt damage**!
- **Step 4: Turn End State**:
  * Sand Mandibles: **DESTROYED (0/1,400 HP)**.
  * Dorsal Carapace: 1,800 -> **1,480/1,800** | Posture: **272/340**.
  * Total Colossus HP: 5,320 -> **3,880/5,600** | Posture: **234/380 [MANDIBLES SHATTERED]**.
  * Kael Composure: Stable (50/50 SP).

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (First Stagger Proc & Carapace Fracture)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Disarmed of its jaws, the Colossus attempts to roll its razor dorsal armor over the crawler: `[Obsidian Fin Roll]` (Heavy Weight/Slash, 2 Coins).
  * Kael gains `Ley-Surge` (+2 Speed -> Net Speed 8, 4 AP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael (Speed 8 -> 4 AP): Holds Node 04. Spends 2 AP on `[Glass-Veined Tremor Cleave]`. Spends 2 AP on `[Counter-Brace]`.
  * Hwaran (Speed 6 -> 3 AP): Stands at Node 04. Spends 2 AP on `[Slag Geyser]`.
  * Resonant Lens: Spotters on the crawler bridge paint the carapace stress joints.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 04 to 05)**: Colossus rolls with `[Obsidian Fin Roll]` (Base 17 + 2 Coins = 25 Power).
    * Kael clashes with `[Glass-Veined Tremor Cleave]` (Base 22 + 2 Coins = 34 Power, Seismic Pierce).
    * **Clash Outcome**: Kael WINS THE CLASH (34 vs 25)!
    * Kael strikes the main dorsal hinge plate; the brittle obsidian armor scutes pop open like dry scales!
    * Hwaran's `[Slag Geyser]` melts the exposed connective tissues beneath!
    * Deals **720 Thermal/Weight damage** and $+104$ Posture Strain!
- **Step 4: STAGGER THRESHOLD 1 TRIGGERED!**:
  * Colossus HP crosses 70% threshold (3,920 HP), falling to **2,840/5,600 HP**; Posture crosses 60% strain line!
  * **STAGGER LEVEL 1 ACTIVE!** The titan crashes onto the sand, its snout buried in the dust; defenses drop to zero; takes $+50\%$ damage!
- **Step 5: Turn End State**:
  * Total Colossus HP: 3,880 -> **2,840/5,600 [THRESHOLD BREACHED: Below 3,920 HP!]**.
  * Dorsal Carapace: 1,480 -> **760/1,800** | Posture: **120/340 [FRACTURED]**.
  * Colossus Posture: **146/380 [STAGGER LEVEL 1]**.
  * Kael Status: Unbroken.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Maximum Burst & Phase 2 Threshold Skip)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * The Colossus is pinned in the sand; its Seismic Resonance Heart is exposed between fractured dorsal plates.
  * Kael coordinates an all-out offensive barrage to crush the core before the storm worsens.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael (Speed 11 -> 5 AP, Momentum Crit): Stands atop Node 05. Spends 3 AP on `[Obsidian Cleaver Seismic Execution]`. Spends 2 AP on `[Ley-Drive Ground Thrust]`.
  * Hwaran: Casts `[Thermal Firestorm]` (3 AP).
  * Drift Throne: Fires `[Direct Acoustic Torpedo]` from Node 10 (2 AP).
- **Step 3: Unopposed Stagger Punishment Rotation**:
  * Kael's `[Seismic Execution]`: Plunges into the resonance organ for **1,180 Weight/Thermal damage** (Fatal 2.0x proc!)!
  * Kael's `[Ground Thrust]`: Slices through the remaining dorsal fin for **480 Pierce damage**!
  * Hwaran's `[Firestorm]`: Incinerates sub-carapace glands for **320 Heat damage**!
  * Drift Throne's `[Acoustic Torpedo]`: Pulverizes seismic conduits for **180 Void damage**!
  * **TOTAL BURST DAMAGE: 2,160 DAMAGE!**
- **Step 4: SECOND STAGGER THRESHOLD (2,240 HP) COMPLETELY SKIPPED!**:
  * Boss HP plunges from 2,840 down to **680/5,600 HP**! Dorsal Carapace completely destroyed (0/1,800 HP)!
  * **Phase 2 Emergency Activation Triggered!**
- **Step 5: Turn End State**:
  * Total Colossus HP: 2,840 -> **680/5,600** (Core HP: **680/2,400** | Carapace: **DESTROYED**).
  * Posture: **58/380**.

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Phase 2 Escalation: Supercell Han-Vortex & Song of the Buried Earth)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Dying and agitated, the Colossus channels the entire planetary storm into a vortex: `[Category-5 Supercell Han-Glass Vortex]` (Planetary Sand Cataclysm, 3 Coins).
  * Kael activates Relic Overdrive: `[SONG OF THE BURIED EARTH — MAXIMUM]` (Cost: 3 AP, 30 SP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael (Speed 9 -> 5 AP [Overdrive]): Steps to the crest of the colossus's skull at Node 05, driving his crystalline arm into its cerebral neural nexus.
  * Hwaran: Expands thermal slag dome over the refugee trailers.
  * Drift Throne: Synchronizes ley-siphon sonar to 528 Hz harmonic solfeggio.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 05 to 05)**: Colossus unleashes `[Category-5 Supercell Han-Glass Vortex]` (Base 22 + 3 Coins = 34 Power, Area Pale/Weight).
    * Kael clashes with `[SONG OF THE BURIED EARTH — MAXIMUM]` (Base 29 + 3 Coins Heads = 50 Power, Planetary Song).
    * **Clash Outcome**: KAEL SUPREME OVERDRIVE CLASH WIN (50 vs 34)!
    * Instead of cutting the beast down, Kael pours the soothing harmonic frequencies of the Absolvohan into its petrified brain (`[P3: Parry/Protection]`).
    * The howling 180 km/h razor winds slow; the razor glass particles melt in mid-air, falling to the sand as warm, gentle rain!
    * Kael whispers: *"Rest, great beast. We are not here to steal your desert. We are only walking through."*
    * The behemoth's agonized thrashing ceases entirely! Zero squad damage taken!
- **Step 4: Turn End State**:
  * Total Colossus HP: **680/5,600** | Posture: **28/380 [VORTEX CALMED]**.
  * Kael Composure: 50/50 SP.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Pacification & The Highway of Clear Sand)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Hostilities cease. Posture reaches **0/380 [PACIFICATION]**.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael steps back down onto the crawler's boarding ramp.
- **Step 3: Resolution & Safe Passage**:
  * The Glass-Dune Colossus emits a long, low acoustic rumble of gratitude that vibrates peacefully through the crawler's hull.
  * It slowly sinks into the liquefied sand, leaving behind a wide, hardened highway of compacted obsidian where the storm once raged.
  * Deals **680 Peaceful Harmony**! Colossus HP reaches 0!
  * Beyond the settled dust, the distant jagged silhouette of the volcanic calderas of **Cheonbulok** appears against the horizon, glowing with orange forge-light.
- **Step 4: Operational Artifact Extraction & Milestones**:
  * **Relic Harvested**: `[Heart of the Glass Colossus]` (Enables automatic terrain stabilization for the Drift Throne).
  * **Route Cleared**: Sea of Glass successfully charted and traversed.
  * **Casualties**: Zero Casualties. Kael HP 3,800/3,800. Composure 50/50 SP."""

def generate_arc_3():
    dossier_box = make_box("EXPEDITION DOSSIER: ARC 3 - ARRIVAL AT CHEONBULOK", [
        "OPERATION NAME     : Arc 3 - Arrival at the City of Rages",
        "PRIMARY THEATER    : Cheonbulok - The Grand Battle Pit Caldera",
        "DATE & EPOCH       : Year 4238, Month 4 (Arrival in Volcanic Foundry)",
        "PRIMARY ADVERSARY  : Slag Champion Barok & Battle Pit Enforcers",
        "---",
        "ADVERSARY PROFILE (SLAG CHAMPION BAROK):",
        "- Total Health (HP): 5,800 HP | Posture Pool: 380/380",
        "- Stagger 1 Proc   : 60% Posture Strain (228 Posture) / Cleaver Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Gladiatorial Submission)",
        "- Resistances      : Void 2.0x (Fatal), Lament 1.5x, Heat 0.5x, Weight 0.5x",
        "---",
        "TARGETABLE COMBAT ANCHORS:",
        "1. Boiling Cleaver : 1,500 HP | Posture 300/300 (Superheated slag blade)",
        "2. Basalt Pauldron : 1,800 HP | Posture 340/340 (Volcanic armor mantle)",
        "3. Combustion Core : 2,500 HP | Posture 380/380 (Steam-venting chest furnace)"
    ])

    hud_t01 = make_box("TACTICAL STAGE HUD: ARC 03 - BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 - CHEONBULOK GRAND BATTLE PIT]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RAMPS] [FLANK] [PITS]  [RING]  [DAIS]  [C-WALK][VATS]  [LAVA]  [MAGMA] [THRONE]",
        "[KAEL]  [HWARAN]                [BAROK]                                 [HELM]  ",
        "---",
        "- Node 01: Arena Entry Ramps (Kael Vanguard Band 1)",
        "- Node 02: Flanking Ashes (Hwaran & Dune Scouts / Short Band 2)",
        "- Node 03: Open Slag Trenches (Boiling Iron Runoff Hazard)",
        "- Node 04: The Gladiatorial Duelist Ring (Crushed Basalt Sand)",
        "- Node 05: The Center Dais (Slag Champion Barok, Boiling Cleaver)",
        "- Node 06: Overhead Spectator Catwalks (Howling Cheonbulok Citizens)",
        "- Node 07: Crucible Slag Vats (Industrial Molten Pourers)",
        "- Node 10: Arena Overlook Platform (Furnace Keeper Bulhwa Observing)",
        "---",
        "- Kael        : Spd 7 -> 4 AP | HP 3,800/3,800 | SP 50/50 | Posture 160/160",
        "- Hwaran      : Spd 6 -> 3 AP | HP 2,600/2,600 | SP 45/45 | Posture 110/110",
        "- Barok Core  : Spd 6 -> 3 AP | HP 2,500/2,500 | Posture 380/380 [FURIOSO]",
        "- Boil-Cleaver: Spd 6 -> 3 AP | HP 1,500/1,500 | Posture 300/300 [GLOWING]",
        "- Basalt Pauld: Spd 3 -> 1 AP | HP 1,800/1,800 | Posture 340/340 [MANTLED]"
    ])

    hud_t02 = make_box("TACTICAL STAGE HUD: ARC 03 - BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 - BOILING CLEAVER SHATTERED & VOID CUT]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RAMPS]         [FLANK] [KAEL]  [BAROK] [C-WALK][VATS]  [LAVA]  [MAGMA] [THRONE]",
        "                [HWARAN][SHARDS]                                                ",
        "---",
        "- Node 03: Hwaran (Volcanic Cinder-Staff Snuffing Ignition Feeder)",
        "- Node 04: Kael (Obsidian Cleaver Shearing Superheated Slag Edge)",
        "- Node 05: Slag Champion Barok (Boiling Cleaver Destroyed 0/1,500 HP)",
        "- Node 06: Cheonbulok Spectators (Shocked Silence Across Arena)",
        "---",
        "- Kael        : Spd 9 -> 5 AP [SURGE] | HP 3,800/3,800 | SP 50/50 | Posture 160/160",
        "- Barok Core  : Spd 4 -> 2 AP | HP 2,500/2,500 | Posture 292/380",
        "- Boil-Cleaver: DESTROYED (0/1,500 HP) | SLAG CLEAVE PERMANENTLY LOST",
        "- Basalt Pauld: Spd 3 -> 1 AP | HP 1,460/1,800 | Posture 268/340"
    ])

    hud_t03 = make_box("TACTICAL STAGE HUD: ARC 03 - BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 - STAGGER THRESHOLD 1 & PAULDRON SHATTER]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RAMPS]                 [FLANK] [KAEL]  [C-WALK][VATS]  [LAVA]  [MAGMA] [THRONE]",
        "                        [HWARAN][BAROK]                                         ",
        "---",
        "- Node 04: Hwaran (Thermal Shock Chill Cracking Basalt Shoulder Guards)",
        "- Node 05: Kael (Glass-Arm Seismic Punch Smashing Pauldron Mounts)",
        "- Node 05: Slag Champion Barok (STAGGER LEVEL 1 / KNEELING IN SLAG)",
        "- Node 06: Arena Guards (Restrained by Bulhwa's Hand Gesture)",
        "---",
        "- Kael        : Spd 8 -> 4 AP [SURGE] | HP 3,800/3,800 | SP 50/50 | Posture 160/160",
        "- Barok Core  : Spd 0 -> 0 AP | HP 2,140/2,500 | Posture 148/380 [STAGGER LEVEL 1]",
        "- Basalt Pauld: Spd 0 -> 0 AP | HP 720/1,800   | Posture 116/340 [SHATTERED]",
        "- Total Barok : HP 2,860/5,800 [THRESHOLD BREACHED / TAKES 1.5X DAMAGE]"
    ])

    hud_t04 = make_box("TACTICAL STAGE HUD: ARC 03 - BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 - MAXIMUM BURST & PHASE 2 THRESHOLD SKIP]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RAMPS]                         [KAEL]  [C-WALK][VATS]  [LAVA]  [MAGMA] [THRONE]",
        "                                [BAROK]                                         ",
        "---",
        "- Node 05: Kael (Obsidian Cleaver Execution Barrage on Combustion Core)",
        "- Node 05: Slag Champion Barok (Immobilized / White Steam Venting)",
        "- Node 05: Hwaran (Volcanic Slag Null-Burst on Exhaust Valves)",
        "- Node 10: Drift Throne (Broadcasting 528 Hz Harmonic Peace Sonar)",
        "---",
        "- Kael        : Spd 11 -> 5 AP [BURST CRIT] | HP 3,800/3,800 | SP 50/50",
        "- Barok Core  : Spd 0 -> 0 AP  | HP 690/2,500  | Posture 58/380",
        "- Basalt Pauld: DESTROYED (0/1,800 HP)",
        "- Total Barok : HP 690/5,800 [BURST DAMAGE 2,170! SECOND THRESHOLD SKIPPED]"
    ])

    hud_t05 = make_box("TACTICAL STAGE HUD: ARC 03 - BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 - BERSERK ERUPTION & CALM OF THE NOMAD]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RAMPS]                         [KAEL]  [C-WALK][VATS]  [LAVA]  [MAGMA] [THRONE]",
        "                                [BAROK]                                         ",
        "---",
        "- Node 05: Kael (Relic Overdrive: EYE OF THE UNBURNING EYE)",
        "- Node 05: Barok (Last Stand: Thousand-Rage Volcanic Cataclysm Slam)",
        "- Node 04: Hwaran (Forming Quenched Basalt Footing for Kael)",
        "- Node 10: Bulhwa (Standing from Throne in Shock and Reverence)",
        "---",
        "- Kael        : Spd 9 -> 5 AP [OVERDRIVE] | HP 3,800/3,800 | SP 50/50 [RESOLVE]",
        "- Barok Core  : Spd 3 -> 1 AP | HP 690/2,500   | Posture 28/380 [FLAME QUENCHED]",
        "- Total Barok : HP 690/5,800 [VOLCANIC WRATH COOLED TO LIVING WARMTH]"
    ])

    hud_t06 = make_box("TACTICAL STAGE HUD: ARC 03 - BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 - SUBMISSION & AUDIENCE WITH THE FURNACE]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RAMPS]                 [ARENA]         [SUBMIT]        [FURNACE SANCTUM OPEN]  ",
        "                        [HONOR]         [BAROK]                                 ",
        "---",
        "- Node 05: Slag Champion Barok (YIELDED / EXTENDING HAND OF BROTHERHOOD)",
        "- Node 05: Kael (Lowering Obsidian Cleaver / Cheering Arena Crowds)",
        "- Node 10: Furnace Keeper Bulhwa (Descending from Throne / Welcoming Caravan)",
        "- Node 10: Great Furnace Sanctum Gates (OPENED TO THE HORIZON CARAVAN)",
        "---",
        "- Squad Status: Zero Casualties | Morale 50/50 SP (Supreme Prestige)",
        "- Reception Status: 100% RESOLVED | Cheonbulok Entry Granted"
    ])

    return f"""# Arc 3: Arrival at Cheonbulok — The City of a Thousand Rages (천불옥 도착 — 분노의 도시)
## The Horizon Caravan Chronicles — Planetary Overland Expedition (Year 4238, Month 4)

```text
{dossier_box}
```

> *"In Cheonbulok, words are cheap fuel. If you cannot bleed on the black iron and stand back up, your treaties are only kindling. Step into the pit, outlander. Let us see if your sorrow burns hotter than our rage."*  
> — Slag Champion Barok, Master of the Grand Battle Pits

---

### Narrative Prologue: The Volcanic Caldera

In the fourth month of Year 4238, after traveling 2,400 kilometers across the Desolate, the Horizon Caravan arrived at the smoking gates of humanity's second surviving city: **Cheonbulok (천불옥 / 千火獄) — The City of a Thousand Rages**.

Built inside the rim of a gargantuan volcanic caldera, Cheonbulok was a city of fire and iron. Massive aqueducts carried rivers of boiling orange slag to titanic foundry crucibles. Black soot rained from a blood-red sky, and the air roared with the ceaseless rhythmic pounding of pneumatic steam hammers.

The citizens did not live by the bureaucratic curfews of Somnarak. Here, survival was governed by the **Doctrine of Wrath**. To enter the city and speak with **Furnace Keeper Bulhwa**, law dictated that an outsider must submit to the judgment of the arena: **The Grand Battle Pit**.

Stepping into the crushed basalt sand of the arena floor, Kael looked up at fifty thousand roaring spectators lining the tiers. Across the circular pit stood **Slag Champion Barok**, an eight-foot titan clad in jagged volcanic basalt armor. In his right hand, he dragged the **Boiling Iron Cleaver**, its serrated blade glowing incandescent white with liquid slag.

*"Hwaran!"* Barok snarled across the arena, spitting boiling embers. *"You fled across the sand like a whipped hound! And now you bring this grey-haired nomad to die for you?"*

Hwaran gripped her cinder-staff at the edge of the pit. *"He didn't come to die, Barok. He came to show you that your rage is burning out the city."*

Kael stepped past Hwaran, planting his obsidian cleaver into the basalt sand.

*"Less talk, champion,"* Kael said calmly. *"Let's see if your furnace has any steel left in it."*

---

### Expedition Combat Gauntlet: Arc 3 (6-Turn Resolution)

```text
{hud_t01}
```

###### Turn 01 Action Resolution Log (Intercepting the Boiling Iron Cleaver)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Kael initializes `[Planetary Ley-Stance]`: Grants $+3$ Protection and physical stagger immunity.
  * Hwaran prepares `[Slag Quench Barrier]`, cooling ambient heat damage.
  * Barok activates `[Berserk Rage Crucible]`: Increases clash power by $+3$ when above 80% HP.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael (Speed 7 -> 4 AP, Warden Heavy Rig delta $-1$, Poise $+20$): Holds Node 01. Spends 2 AP on `[Obsidian Cleaver: Slag Deflection]`. Holds 2 AP in Reserve.
  * Hwaran (Speed 6 -> 3 AP): Holds Node 02. Spends 2 AP on `[Volcanic Smoke Screen]`. Holds 1 AP in Guard.
  * Barok (Speed 6 -> 3 AP, Heavy Armor delta $-1$, Poise $+25$): Lunges from Node 05 to Node 01 with `[Boiling Slag Cleave]`.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 01 to 05)**: Barok sweeps with `[Boiling Slag Cleave]` (Base 19 + 2 Coins = 29 Power, Heavy Heat/Slash).
    * Kael intercepts with `[Obsidian Cleaver: Slag Deflection]` (Base 22 + 2 Coins = 34 Power, Obsidian Guard).
    * **Clash Outcome**: Kael WINS THE CLASH OVERWHELMINGLY (34 vs 29)!
    * The incandescent slag blade strikes Kael's obsidian cleaver; white sparks cascade thirty feet across the arena floor (`[P3: Parry/Protection]`).
    * Kael's translucent glass arm absorbs the immense thermal heat, turning deep crimson as it redirects **280 kinetic tremor damage** into Barok's weapon hilt!
  * **Clash 2 (Node 02 to 05)**: Hwaran throws quenching dust at Barok's boots, reducing his traction on the basalt.
- **Step 4: Turn End State**:
  * Boiling Cleaver HP: 1,500 -> **1,220/1,500** | Posture: **244/300**.
  * Total Barok HP: 5,800 -> **5,520/5,800** | Posture: **326/380**.
  * Kael Composure: **100% (50/50 SP)**. Zero damage taken.

---

```text
{hud_t02}
```

###### Turn 02 Action Resolution Log (Part Destruction: Boiling Cleaver Shattered)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Kael activates `Ley-Surge` (+2 Speed next turn -> Net Speed 9, 5 AP).
  * Barok roars in fury, preparing `[Molten Guillotine Split]`.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael (Speed 9 -> 5 AP [Surge]): Steps into Node 04. Spends 3 AP on `[Obsidian Cleaver: Sunder Blade]`. Spends 2 AP on `[Gladiatorial Pivot]`.
  * Hwaran (Speed 6 -> 3 AP): Moves to Node 03. Spends 2 AP on `[Cinder-Staff Frost Quench]`.
  * Drift King Scouts: Cheer from the debarkation ramps.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 04 to 05)**: Barok executes `[Molten Guillotine Split]` (Base 18 + 2 Coins = 26 Power).
    * Kael clashes with `[Obsidian Cleaver: Sunder Blade]` (Base 25 + 3 Coins Heads = 43 Power, Heavy Slash).
    * **Clash Outcome**: Kael WINS THE CLASH OVERWHELMINGLY (43 vs 26)!
    * Kael sidesteps the overhead strike and delivers a devastating horizontal cross-slash directly into the glowing blade's thermal seam!
    * Hwaran's frost quench flash-cools the hot iron, turning it brittle in an instant!
    * Deals **1,220 Critical Void/Weight damage** (Fatal 2.0x proc!)!
    * **TARGETED PART DESTROYED**: The Boiling Iron Cleaver shatters into a shower of black cast-iron shrapnel (**Cleaver HP: 0/1,500**)!
    * **EFFECT**: Barok's slag cleave attacks permanently disabled; boss permanently loses 1 Speed Slot!
  * **Basalt Pauldron Damage**:
    * Sapper shockwave cracks the shoulder armor for **340 Blunt damage**!
- **Step 4: Turn End State**:
  * Boiling Cleaver: **DESTROYED (0/1,500 HP)**.
  * Basalt Pauldron: 1,800 -> **1,460/1,800** | Posture: **268/340**.
  * Total Barok HP: 5,520 -> **3,960/5,800** | Posture: **234/380 [CLEAVER SHATTERED]**.
  * Kael Composure: Stable (50/50 SP).

---

```text
{hud_t03}
```

###### Turn 03 Action Resolution Log (First Stagger Proc & Pauldron Shatter)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Disarmed of his weapon, Barok charges with his massive basalt shoulder guard: `[Basalt Shoulder Battering Ram]` (Heavy Weight/Blunt, 2 Coins).
  * Kael gains `Ley-Surge` (+2 Speed -> Net Speed 8, 4 AP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael (Speed 8 -> 4 AP): Holds Node 04. Spends 2 AP on `[Glass-Arm Seismic Counter]`. Spends 2 AP on `[Rooted Stance]`.
  * Hwaran (Speed 6 -> 3 AP): Stands at Node 04. Spends 2 AP on `[Thermal Crack Shock]`.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 04 to 05)**: Barok charges with `[Basalt Shoulder Battering Ram]` (Base 17 + 2 Coins = 25 Power).
    * Kael clashes with `[Glass-Arm Seismic Counter]` (Base 22 + 2 Coins = 34 Power, Seismic Strike).
    * **Clash Outcome**: Kael WINS THE CLASH (34 vs 25)!
    * Kael catches the three-ton basalt shoulder charge directly on his crystalline glass fist!
    * The seismic shockwave ripples backward through the stone armor; the heavy volcanic pauldron explodes outward!
    * Deals **740 Blunt/Weight damage** and $+102$ Posture Strain!
- **Step 4: STAGGER THRESHOLD 1 TRIGGERED!**:
  * Barok's HP crosses 70% threshold (4,060 HP), dropping to **2,860/5,800 HP**; Posture crosses 60% strain line!
  * **STAGGER LEVEL 1 ACTIVE!** Barok drops to one knee on the arena sand, gasping for breath; chest combustion furnace exposed; takes $+50\%$ damage!
- **Step 5: Turn End State**:
  * Total Barok HP: 3,960 -> **2,860/5,800 [THRESHOLD BREACHED: Below 4,060 HP!]**.
  * Basalt Pauldron: 1,460 -> **720/1,800** | Posture: **116/340 [SHATTERED]**.
  * Barok Posture: **148/380 [STAGGER LEVEL 1]**.
  * Kael Status: Unbroken.

---

```text
{hud_t04}
```

###### Turn 04 Action Resolution Log (Maximum Burst & Phase 2 Threshold Skip)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Barok is kneeling; his chest combustion engine is exposed and glowing red-hot.
  * Kael executes an unopposed barrage to breach the core without inflicting lethal trauma.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael (Speed 11 -> 5 AP, Momentum Crit): Advances to Node 05. Spends 3 AP on `[Obsidian Cleaver Execution Barrage]`. Spends 2 AP on `[Pneumatic Pummel]`.
  * Hwaran: Casts `[Volcanic Slag Null-Burst]` (3 AP).
  * Drift Throne: Broadcasts 528 Hz harmonic pulse from Node 10 (2 AP).
- **Step 3: Unopposed Stagger Punishment Rotation**:
  * Kael's `[Execution Barrage]`: Strikes the chest boiler plates for **1,210 Void/Weight damage** (Fatal 2.0x proc!)!
  * Kael's `[Pneumatic Pummel]`: Slices through the remaining shoulder plates for **500 Blunt damage**!
  * Hwaran's `[Null-Burst]`: Extinguishes fuel vents for **310 Heat damage**!
  * Drift Throne's `[Harmonic Pulse]`: Quells rage resonance for **150 Void damage**!
  * **TOTAL BURST DAMAGE: 2,170 DAMAGE!**
- **Step 4: SECOND STAGGER THRESHOLD (2,320 HP) COMPLETELY SKIPPED!**:
  * Boss HP plunges from 2,860 down to **690/5,800 HP**! Basalt Pauldron completely destroyed (0/1,800 HP)!
  * **Phase 2 Emergency Activation Triggered!**
- **Step 5: Turn End State**:
  * Total Barok HP: 2,860 -> **690/5,800** (Core HP: **690/2,500** | Pauldron: **DESTROYED**).
  * Posture: **58/380**.

---

```text
{hud_t05}
```

###### Turn 05 Action Resolution Log (Phase 2 Escalation: Volcanic Cataclysm & Eye of the Unburning)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * In supreme gladiatorial pride, Barok ignites the arena floor into magma: `[Thousand-Rage Volcanic Cataclysm Slam]` (Gladiatorial Wrath Cataclysm, 3 Coins).
  * Kael activates Relic Overdrive: `[EYE OF THE UNBURNING EYE — MAXIMUM]` (Cost: 3 AP, 30 SP).
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael (Speed 9 -> 5 AP [Overdrive]): Steps directly into the bubbling lava pool at Node 05, facing Barok eye-to-eye.
  * Hwaran: Instantly quenches the basalt footing under Kael's boots.
  * Furnace Keeper Bulhwa: Leans forward from the royal box in disbelief.
- **Step 3: Clash & Skill Resolution**:
  * **Clash 1 (Node 05 to 05)**: Barok strikes with `[Thousand-Rage Volcanic Cataclysm Slam]` (Base 22 + 3 Coins = 34 Power, Area Heat/Weight).
    * Kael clashes with `[EYE OF THE UNBURNING EYE — MAXIMUM]` (Base 29 + 3 Coins Heads = 50 Power, Unshakable Will).
    * **Clash Outcome**: KAEL SUPREME OVERDRIVE CLASH WIN (50 vs 34)!
    * The fiery magma hammer strikes Kael's raised obsidian blade; instead of burning him, the molten metal parts around him like water (`[P3: Parry/Protection]`).
    * Kael grabs Barok's smoking wrist with his glowing glass hand, grounding the volcanic wrath harmlessly into the earth!
    * Kael speaks softly over the roar of the arena:
      *"Rage is a good shield, Barok. But it's a terrible hearth. You can't keep your people warm with fire that burns them alive."*
    * Barok's eyes widen as the blind red fury fades into exhaustion. Zero squad damage taken!
- **Step 4: Turn End State**:
  * Total Barok HP: **690/5,800** | Posture: **28/380 [FLAME QUENCHED]**.
  * Kael Composure: 50/50 SP.

---

```text
{hud_t06}
```

###### Turn 06 Action Resolution Log (Gladiatorial Submission & Audience Granted)
- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:
  * Combat ends. Posture reaches **0/380 [SUBMISSION]**.
- **Step 2: Spatial Movement & Action Point Allocation**:
  * Kael lowers his blade and releases Barok's wrist.
- **Step 3: Resolution & Welcome to Cheonbulok**:
  * Barok breathes heavily, kneeling in the cooled basalt sand. He raises his right hand into the air, signaling unconditional submission and brotherhood.
  * Fifty thousand citizens erupt into thunderous cheering, chanting Kael's name across the caldera!
  * From the grand royal box, **Furnace Keeper Bulhwa** stands, raising his gold-filigree staff:
    > *"Citizens of Cheonbulok! The outsider has bled on our stone and stood unbroken! His sorrow is forged of true steel. Lower the furnace bridges! The Horizon Caravan is welcome in the City of a Thousand Rages!"*
  * Deals **690 Honorable Capitulation**! Barok HP reaches 0!
- **Step 4: Operational Artifact Extraction & Milestones**:
  * **Passage Granted**: Full diplomatic immunity and trade rights within Cheonbulok.
  * **Access Unlocked**: The inner sanctum of **The Great Furnace Core** is opened to Kael and Hwaran.
  * **Casualties**: Zero Casualties. Kael HP 3,800/3,800. Composure 50/50 SP."""

def main():
    p1 = "SOMNARAK-WORLD/Jipyeongseondae/Arc_1_Departure.md"
    p2 = "SOMNARAK-WORLD/Jipyeongseondae/Arc_2_The_Desolate_Crossing.md"
    p3 = "SOMNARAK-WORLD/Jipyeongseondae/Arc_3_Arrival_at_Cheonbulok.md"

    with open(p1, "w", encoding="utf-8") as f:
        f.write(generate_arc_1())
    print("Generated Arc_1_Departure.md successfully!")

    with open(p2, "w", encoding="utf-8") as f:
        f.write(generate_arc_2())
    print("Generated Arc_2_The_Desolate_Crossing.md successfully!")

    with open(p3, "w", encoding="utf-8") as f:
        f.write(generate_arc_3())
    print("Generated Arc_3_Arrival_at_Cheonbulok.md successfully!")

if __name__ == "__main__":
    main()
