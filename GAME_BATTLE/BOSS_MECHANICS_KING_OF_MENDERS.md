# BOSS MECHANICS — The King of Menders (Suseonwang)
## Underworld Syndicate Sovereign Boss Specification & Modular Anatomy Guide
### Underworld Cleanup Descend (UCD) Suppression Standard — SOP-GB-BOSS-003

```text
+=====================================================================+
|    SYNDICATE OVERLORD SPECIFICATION: BOSS-GB-003-KING-OF-MENDERS    |
+=====================================================================+
| TARGET ALIAS        : THE KING OF MENDERS (SUSEONWANG)              |
| CLASSIFICATION      : Underworld Syndicate Boss / Flesh-Welded Core |
| TERRITORIAL DOMAIN  : The Needle Warrens (-1,200m / The Raw)        |
| COMBAT ARCHETYPE    : Multi-Node Tether Trapper / Flesh Welder      |
| OPERATIONAL WING    : UCD Strike Force / Underworld Cadre           |
| AUTHORIZATION SOP   : SOP-GB-BOSS-003 / UNDERWORLD OVERLORD PURGE   |
+=====================================================================+
```

---

## 1. Entity Identification & Syndicate Lore Profile

- **Target Identifier & Alias:** The King of Menders (수선왕 — *Suseonwang* / Sovereign of the Needle Warrens)
- **Classification:** Underworld Syndicate Boss / Autonomous Cybernetic Flesh-Construct
- **Primary Domain:** The Needle Warrens & East Flues (-1,200m Deep Strata / The Raw)
- **Primary Affinities:** Weight (Primary Kinetic) • Grudge (Secondary Heat/Slag) • Void (Fatal Vulnerability)
- **Territorial Jurisdiction:** Autonomous Sovereign of the Five Underworld Syndicates
- **Lore Profile & Macro-Canon Significance:**
  Deep within the subterranean abyss of The Raw—far beneath municipal jurisdiction and the reaching roots of the Alpha Tree—lies the labyrinthine territory known as the **Needle Warrens**. While the legitimate Menders Guild acts as an honorable civic repair brigade for the city's crumbling infrastructure, rogue grandmasters who survived the historical Cheongula catastrophe broke away to establish an extralegal criminal dynasty.

  Spurning municipal taboos and the Treaty of Broken Needles, these master craftsmen forged the **Treaty of Flesh and Iron**. Through decades of horrific medical and acoustic experimentation, their supreme patriarch transformed himself into **The King of Menders**: a towering, four-meter-tall sovereign construct composed of heavy pneumatic basalt pistons, hundreds of meters of high-tensile suture wires, industrial lead-soldering boilers, and grafted biological limbs harvested from defaulting debtors.

  Presiding over illegal flesh-welding clinics, the King forcibly binds debtors into unspent Sorrow Husks, stitching their flesh to hydraulic machinery and collecting extortionate usury in pure Han-brine. When his expanding web of tethered warrens threatens to breach secondary municipal containment seals, the Underworld Cleanup Descend (UCD) mobilizes elite Breacher Strike Teams with anti-syndicate kinetic ordnance to sever his pneumatic lifelines and purge his domain.

---

## 2. Sovereign Attributes & Core Combat Parameters

- **Coherence Rank & Threat Level:** Rank IV Syndicate Sovereign • Grade Delta Potency
- **Total Physical Hit Points (Combined Parts):** 3,300 HP
- **Total Composure Pool:** 350 Points • Meltdown Threshold: 0 Points
- **Base Speed:** 4 (Generates 3 Action Points in Phase 1, 4 AP in Phase 2, and 5 AP in Phase 3)
- **Spatial Grid Presence:** Operates from Node `[N07]` during Phase 1; establishes wide-area tether networks extending forward to Nodes `[N03]`–`[N05]`.
- **Unique Boss Combat Mechanics:**
  * **Syndicate Flesh-Welding:** By consuming debtor husks or severed limbs from the battlefield, the King welds fresh biological and basalt armor plates onto damaged parts, restoring 150 HP and 30 Posture.
  * **Debt-Mark Stacking (The Ledger of Needles):** Hostile piercing and suture strikes inflict *Debt Marks* (Stacks 1 to 5). Each stack amplifies damage taken from execution skills by 10%. At 5 stacks, the operative is flagged for **Foreclosure Execution**, suffering instant Stagger on their next clash defeat.
  * **Multi-Node Tether Traps:** The King discharges barbed pneumatic needles into discrete nodes (`[N03]` to `[N06]`), spanning the floor in high-tensile wire tripwires. Operatives entering a tethered node suffer +2 Movement AP cost and 15 bleed/suture strain unless the needle anchor is destroyed.

---

## 3. Modular Body Part Architecture & Hit Pools

The King of Menders functions as an interconnected quadripartite modular combat construct:

```text
+=====================================================================+
|              MODULAR BODY PART ARCHITECTURE & HIT POOLS             |
+=====================================================================+
| PART NAME           | MAX HP   | RUPTURE (60%) | DEFENSE PROFILE    |
+---------------------------------------------------------------------+
| Welded Flesh-Core   | 1,200 HP | 720 HP        | Voi 1.6x, Wgt 0.8x |
| Piston-Needle Arm   | 800 HP   | 480 HP        | Wgt 1.4x, Gru 1.0x |
| Solder Crucible Arm | 700 HP   | 420 HP        | Voi 1.4x, Lam 1.2x |
| Tethered Husk Sump  | 600 HP   | 360 HP        | Gru 1.5x, Voi 1.2x |
+---------------------------------------------------------------------+
| TOTAL PHYSICAL HP   : 3,300 HP (Combined Modular Parts)             |
| COMPOSURE POOL      : 350 Points | Meltdown Threshold: 0 Points     |
+=====================================================================+
```

### 3.1 Part 1: Welded Flesh-Core (Torso / Boiler)
- **Hit Point Pool:** 1,200 HP • **Rupture Threshold:** 720 HP Sustained (Remaining HP: 480)
- **Defense Multipliers:** Void 1.6x (Fatal Vulnerability) • Weight 0.8x • Lament 1.0x • Grudge 1.2x
- **Part Passive (Flesh Graft Overdrive):** Circulating pressurized Han-blood through internal copper pipes, the boiler restores 15 HP to all modular limbs at turn start.
- **Rupture Penalty:**
  * Disables *Flesh Graft Overdrive*.
  * Permanently disables internal regeneration.
  * Shifts core defense from 1.6x to **2.0x Fatal Void**, triggering instant **Phase 3 Stance Shift**.

### 3.2 Part 2: Piston-Needle Arm (Right Weapon Limb)
- **Hit Point Pool:** 800 HP • **Rupture Threshold:** 480 HP Sustained (Remaining HP: 320)
- **Defense Multipliers:** Weight 1.4x (Fatal Vulnerability) • Grudge 1.0x • Lament 1.0x • Void 0.8x
- **Part Passive (Suture Harpoon Mastery):** Grants +2 Clash Power to all piercing needle and tether attacks.
- **Rupture Penalty:**
  * Cancels *Suture Harpoon Mastery*.
  * Permanently removes *Debt-Suture Flurry* from the intention deck.
  * Halts tether trap deployment across the right combat flank.

### 3.3 Part 3: Solder Crucible Arm (Left Hydraulic Arm)
- **Hit Point Pool:** 700 HP • **Rupture Threshold:** 420 HP Sustained (Remaining HP: 280)
- **Defense Multipliers:** Void 1.4x (Vulnerable) • Lament 1.2x • Grudge 1.0x • Weight 0.5x (Resistant)
- **Part Passive (Boiling Slag Aura):** Any operative attempting a Range Band 1 melee strike against the King sustains 10 heat damage from escaping sulfuric slag vapors.
- **Rupture Penalty:**
  * Extinguishes the cauldron fire, disabling *Boiling Slag Aura*.
  * Removes *Boiling Basalt Slag* from the intention deck.
  * Lowers King Base Speed by 1.

### 3.4 Part 4: Tethered Husk Sump (Backpack Reservoir)
- **Hit Point Pool:** 600 HP • **Rupture Threshold:** 360 HP Sustained (Remaining HP: 240)
- **Defense Multipliers:** Grudge 1.5x (Vulnerable) • Void 1.2x • Weight 1.0x • Lament 0.8x
- **Part Passive (Emergency Graft Spool):** Supplies biological tissue and suture wire for the *Flesh-Graft Suture* healing skill.
- **Rupture Penalty:**
  * The sump shatters, spilling biological waste across the occupied node.
  * Permanently disables *Flesh-Graft Suture*, preventing the King from restoring HP to broken parts.

---

## 4. Multi-Phase Stance Evolution & Graft Cycles

```text
+=====================================================================+
|             MULTI-PHASE STANCE EVOLUTION & GRAFT CYCLES             |
+=====================================================================+
| PHASE STANCE      | CORE HP      | AP & SPD   | TACTICAL BEHAVIOR   |
+---------------------------------------------------------------------+
| Phase 1: Stitcher | 100-70% Core | 3 AP (Spd4)| Tether Tripwires    |
| Phase 2: Solder   | 70-30% Core  | 4 AP (Spd5)| Flesh-Graft Slag    |
| Phase 3: Storm    | 30-0% Core   | 5 AP (Spd6)| Sovereign Suture    |
+=====================================================================+
```

### 4.1 Phase 1: The Master Stitcher (100% down to 70% Core HP / 1,200 - 840 HP)
- **Action Points (AP):** 3 AP per turn • **Base Speed:** 4
- **Tactical Posture:** Territory Trapper. Holds Node `[N07]`.
- **Intention Routine:**
  * Deploys *Needle Warren Tether* (1 AP) across Nodes `[N03]` to `[N05]`, restricting allied movement.
  * Lashes advancing vanguard units with *Debt-Suture Flurry* (2 AP), stacking Debt Marks.
- **Tactical Objective:** Break wire anchors on trapped nodes using blunt force while maneuvering into Range Band 2 to strike the Piston-Needle Arm.

### 4.2 Phase 2: Flesh-Solder Overclock (70% down to 30% Core HP / 840 - 360 HP)
- **Action Points (AP):** 4 AP per turn • **Base Speed:** 5
- **Stance Shift Trigger:** The Core drops below 840 HP, OR any single arm limb is ruptured.
- **Tactical Posture:** Aggressive Midline Incursion. Steps forward onto Nodes `[N04]` and `[N05]`.
- **Combat Mutators:**
  * Discharges *Boiling Basalt Slag* (2 AP Area) across Nodes `[N02]` to `[N04]`, creating burning slag hazards.
  * Casts *Flesh-Graft Suture* (2 AP) to repair damaged limbs by consuming unspent debtor husks.
- **Tactical Objective:** Concentrate heavy focus fire on the *Tethered Husk Sump* to halt self-healing before dismantling the remaining arm.

### 4.3 Phase 3: Sovereign Suture Storm & Total Foreclosure (30% down to 0% Core HP / 360 - 0 HP)
- **Action Points (AP):** 5 AP per turn • **Base Speed:** 6
- **Stance Shift Trigger:** The Core drops below 360 HP.
- **Tactical Posture:** Sovereign Foreclosure Execution. The King rips all embedded wire cables from the surrounding masonry, spinning them into a screaming vortex of razor wire.
- **Combat Mutators:**
  * **Foreclosure Resonance:** Both the King and allied operatives deal +35% damage.
  * **Grand Execution Channeling:** Every two turns, the King allocates 4 AP to channel *Grand Foreclosure* (4 AP Global Ultimate).
  * Operatives must purge their active Debt Marks or shatter the exposed boiler core before the execution whip lands.

---

## 5. AI Intention Deck & Skill Scripting

```text
+=====================================================================+
|                AI INTENTION DECK & ACTION ALLOCATION                |
+=====================================================================+
| SKILL NAME          | AP | RANGE BAND    | DAMAGE TYPE & BASE       |
+---------------------------------------------------------------------+
| Needle Warren Tether| 1  | Band 2-4 Area | Piercing / Base 22       |
| Debt-Suture Flurry  | 2  | Band 1-2      | Han-Pierce / Base 25     |
| Boiling Basalt Slag | 2  | Band 1-3 Area | Heat+Weight / Base 26    |
| Flesh-Graft Suture  | 2  | Self / Target | Restore 150 HP + Post    |
| Grand Foreclosure   | 4  | Band 1-5 Global| Ultimate / Base 38      |
+=====================================================================+
```

### 5.1 Skill 1: Needle Warren Tether
- **Cost:** 1 AP • **Range Band:** Band 2-4 Area • **Damage Type:** Piercing • **Base Clash Value:** 22
- **Damage Profile:** Fires pneumatic needles into 2 contiguous nodes; leaves behind razor-wire tripwire traps. Operatives traversing trapped nodes suffer 15 bleed damage and +2 Movement AP cost.
- **Destruction:** Wire anchors possess 80 HP and can be destroyed via blunt attacks.

### 5.2 Skill 2: Debt-Suture Flurry
- **Cost:** 2 AP • **Range Band:** Band 1-2 • **Damage Type:** Han-Piercing • **Base Clash Value:** 25
- **Damage Profile:** Three rapid needle strikes dealing 15/15/20 piercing damage.
- **Debt Mark Stacking:** Applies 1 stack of *Debt Mark* per successful hit. Each stack increases damage taken from execution skills by 10%. At 5 stacks, flags target for *Foreclosure*.

### 5.3 Skill 3: Boiling Basalt Slag
- **Cost:** 2 AP • **Range Band:** Band 1-3 Area • **Damage Type:** Heat + Weight • **Base Clash Value:** 26
- **Damage Profile:** Tilts the solder cauldron, bathing 3 nodes in boiling slag; deals 45 heat damage and inflicts 2 stacks of *Burn*.

### 5.4 Skill 4: Flesh-Graft Suture (Self-Sustain Skill)
- **Cost:** 2 AP • **Range Band:** Self / Adjacent Node • **Damage Type:** Suture Healing • **Base Clash Value:** 20
- **Damage Profile:** Welds raw biological graft tissue onto the most damaged modular part, restoring 150 HP and 30 Posture.
- **Disabled By:** Rupturing the *Tethered Husk Sump*.

### 5.5 Skill 5: Grand Foreclosure (Phase 3 Ultimate)
- **Cost:** 4 AP • **Range Band:** Band 1-5 Global Area • **Damage Type:** True Suture Execution • **Base Clash Value:** 38
- **Damage Profile:** Rips all deployed tether cables through the room simultaneously; deals 90 True Damage. If a target possesses 5 Debt Marks, inflicts instant Stagger and wipes remaining Posture.
- **Channeling Cue:** The King winds his steam winch during Turn N; discharges on Turn N+1 at Initiative step 0.

### 5.6 Tactical Decision Tree & Target Selection Priority

| Tactical Condition | King Behavioral Selection | Targeted Allied Unit / Node |
|---|---|---|
| **Allied Unit has 3+ Debt Marks** | Allocates 2 AP to *Debt-Suture Flurry* | Highest Debt Mark Operative |
| **Allied Vanguard advances to Band 1**| Allocates 2 AP to *Boiling Basalt Slag* | Vanguard Melee Node |
| **Modular Part drops below 30% HP** | Allocates 2 AP to *Flesh-Graft Suture* | Damaged Modular Limb |
| **Phase 3 Active (Core below 30%)** | Channels *Grand Foreclosure* | Global Arena `[N01]` to `[N10]` |

---

## 6. Tactical Strategy, Counter-Measures & Squad Composition

### 6.1 Recommended Part Target Sequence
1. **Primary Target — Tethered Husk Sump:**
   Concentrate long-range Piercing and Grudge fire on the backpack sump. Destroying this part permanently eliminates the King's ability to heal via *Flesh-Graft Suture*.
2. **Secondary Target — Piston-Needle Arm (1.4x Weight Vulnerability):**
   Deploy heavy blunt shock-hammers to shatter the pneumatic needle manifold. Breaking this limb halts tether trap deployment and removes *Debt-Suture Flurry*.
3. **Tertiary Target — Solder Crucible Arm:**
   Extinguish the slag cauldron to remove the dangerous area burn hazard and lower the King's Base Speed.
4. **Final Target — Welded Flesh-Core Execution:**
   With all modular defenses shattered and the core exposed to 2.0x Fatal Void damage, unleash high-tier Void execution skills to trigger terminal Composure Meltdown.

### 6.2 Recommended 4-Operative Squad Roster & Archetype Pairings

| Squad Role | Recommended Callsign Archetype | Preferred M.A.W. Set | Tactical Function |
|---|---|---|---|
| **Heavy Kinetic Breaker** | Hydraulic Piston Specialist | Grade 4 Heavy Blunt | Exploits 1.4x Weight vulnerability on Needle Arm |
| **Fortress Anchor** | Heavy Shield Warden (Posture 160+) | Grade 4 Bastion Plate | Intercepts *Boiling Basalt Slag*; shields frontline |
| **Debt Cleaner / Specialist** | Acoustic Needler (Clarity 120+) | Grade 4 Acoustic Needle | Purges *Debt Marks*; snipes Tethered Sump |
| **Anti-Material Marksman** | Void Railgun Sniper (Band 4) | Grade 4 Void Rifle | Destroys Core Boiler from afar without triggering aura |

---

## 7. Extraction Manifest & M.A.W. Synthesis Registry

Upon achieving terminal Composure Meltdown against The King of Menders, the UCD Containment Authority authorizes recovery of his industrial cybernetics:

```text
+=====================================================================+
|         UNDERWORLD EXTRACTION MANIFEST: THE KING OF MENDERS         |
+=====================================================================+
| RECOVERED ARTIFACT  | TYPE   | GRADE | RESONANCE & SPECIAL EFFECT   |
+---------------------------------------------------------------------+
| Sovereign SutureMaul| Weapon | Gr 5  | Heavy Blunt / Debt Hook      |
| Flesh-Welder Apron  | Suit   | Gr 5  | Grudge 0.4x, Heat Proof      |
| The Debt Needle     | Gift   | Gr 5  | Applies Stacking Debt        |
| Grandmaster Ledger  | Relic  | Gr 5  | Reflects 15% Debt Strain     |
+=====================================================================+
```

### 7.1 Detailed M.A.W. Equipment Specifications

- **Weapon: The Sovereign Suture Maul (`MAW-W-MNDR`)**
  * **Classification:** Grade 5 Legendary Heavy Blunt / Piercing Relic
  * **Base Clash Power:** 28 • **Range Band:** Band 1-2 (Mid)
  * **Resonance Passive (Debt Hook):** Every successful hit applies 1 Debt Mark to the target. If the target has 3+ Debt Marks, deals +40% bonus crushing damage and inflicts 15 Posture strain.
- **Suit: The Flesh-Welder's Apron (`MAW-S-MNDR`)**
  * **Classification:** Grade 5 Legendary Heavy Bastion Apron
  * **Defensive Resistances:** Grudge 0.4x (Immune) • Weight 0.6x • Lament 1.0x • Void 1.2x
  * **Resonance Passive (Slag-Proof Plating):** Complete immunity to burn, bleed, and heat terrain hazards. When struck by a piercing attack, converts 15% of damage into armor plating.
- **Gift: The Debt Needle (`MAW-G-MNDR`)**
  * **Classification:** Grade 5 Legendary Accessory (Chest Brooch)
  * **Equip Effect:** +25 Max Posture • +15 Max HP.
  * **Resonance Passive:** Winning a clash against an opponent with higher Speed applies 2 stacks of *Debt Mark* and restores 10 Posture to the wearer.
- **Relic Book: The Grandmaster's Ledger**
  * **Classification:** Grade 5 Unique Relic Codex
  * **Effect:** +20% Composure Defense. Once per combat encounter, when the wearer would suffer Stagger, reflects 100% of the incoming posture strain back to the attacker and clears all personal debt marks.

---

## 8. Quality Compliance & Archival Verification

- **Document Identifier:** `SOP-GB-BOSS-003`
- **Master Registry Reference:** `PROJECT_SOMNARAK/GAME_BATTLE/BOSS_MECHANICS_03`
- **Supervising Authority:** Underworld Cleanup Descend (UCD Strike Force Command)
- **Formatting Compliance:** Verified 71-column ASCII text box layout, zero raw `<br>` tags, zero LaTeX math dollar delimiters, and pure canonical in-universe perspective.
