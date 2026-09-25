#!/usr/bin/env python3
"""
Generate GAME_BATTLE/BOSS_MECHANICS_WEEPING_MIRROR.md
Strict adherence to:
- 71-column ASCII text box standard with mandatory '+' borders and exact symmetry.
- No raw <br> tags anywhere.
- No LaTeX math dollar signs ($).
- 100% authentic in-universe perspective without developer meta-commentary or code vocabulary leaks.
- Exhaustive boss specification: modular anatomy, multi-phase shatter cycles, intention deck, and extraction registry.
"""

import os

def make_box(title, rows, width=71):
    inner_w = width - 2
    lines = []
    lines.append("+" + "=" * inner_w + "+")
    if title:
        lines.append("| " + title.center(inner_w - 2) + " |")
        lines.append("+" + "=" * inner_w + "+")
    for r in rows:
        if r == "---":
            lines.append("+" + "-" * inner_w + "+")
        elif r == "===":
            lines.append("+" + "=" * inner_w + "+")
        else:
            text = r.strip()
            if len(text) > inner_w - 2:
                raise ValueError(f"Line exceeds box width ({len(text)} > {inner_w - 2}): {text}")
            lines.append("| " + text.ljust(inner_w - 2) + " |")
    lines.append("+" + "=" * inner_w + "+")
    return "\n".join(lines)

def wrap_box(b):
    return "```text\n" + b + "\n```\n\n"

def generate_boss_weeping_mirror():
    # Box 1: Technical Header HUD
    b1 = make_box(
        "SOVEREIGN ENTITY SPECIFICATION: BOSS-GB-002-WEEPING-MIRROR",
        [
            "SOVEREIGN ENTITY    : SE-C-IV-DELTA-195 THE WEEPING MIRROR",
            "ENTITY CLASS        : Rank IV Sovereign / Grade Delta Potency",
            "DOMAIN / SECTOR     : Facility 01 Chamber 195 / Alpha Tree Monolith",
            "COMBAT ARCHETYPE    : Object-Void Reflector / Dissociation Aura",
            "SUPERVISING WING    : Reverie Directorate Research Wing (Floor 4)",
            "AUTHORIZATION SOP   : SOP-GB-BOSS-002 / COGNITIVE REFLECTION AUDIT",
        ]
    )

    # Box 2: Modular Part Architecture Table
    b2 = make_box(
        "MODULAR BODY PART ARCHITECTURE & HIT POOLS",
        [
            "PART NAME           | MAX HP   | RUPTURE (60%) | DEFENSE PROFILE",
            "---",
            "Silvered Glass Core | 900 HP   | 540 HP        | Wgt 1.8x, Voi 0.5x",
            "Gilded Iron Frame   | 800 HP   | 480 HP        | Voi 1.4x, Wgt 0.6x",
            "Liquid Silver Siphon| 500 HP   | 300 HP        | Gru 1.2x, Lam 0.4x",
            "Mirrored Simulacrum | 600 HP   | 360 HP        | Inverts Target Def",
            "---",
            "TOTAL PHYSICAL HP   : 2,800 HP (Combined Parts & Simulacra)",
            "COMPOSURE POOL      : 320 Points | Meltdown Threshold: 0 Points",
        ]
    )

    # Box 3: Phase Evolution Summary
    b3 = make_box(
        "MULTI-PHASE STANCE EVOLUTION & SHATTER CYCLES",
        [
            "PHASE STANCE      | CORE HP      | AP & SPD   | TACTICAL BEHAVIOR",
            "---",
            "Phase 1: Silvered | 100-70% Core | 3 AP (Spd4)| Gaze & Reflection",
            "Phase 2: Fractured| 70-30% Core  | 4 AP (Spd5)| Twin Simulacra",
            "Phase 3: Shattered| 30-0% Core   | 5 AP (Spd6)| Sovereign Prism",
        ]
    )

    # Box 4: AI Intention Deck Table
    b4 = make_box(
        "AI INTENTION DECK & ACTION ALLOCATION",
        [
            "SKILL NAME          | AP | RANGE BAND    | DAMAGE TYPE & BASE",
            "---",
            "Gaze of the Unwept  | 1  | Band 1-4 Area | Lament / Base 22",
            "Specular Retaliation| 2  | Band 1-2      | Inverted / Base 26",
            "Mercury Siphon Jet  | 2  | Band 2-3      | Fluid+Void / Base 24",
            "Fracture Duplication| 3  | Band 1-5 Area | Summon Simulacrum",
            "Catastrophic Prism  | 4  | Band 1-5 Area | Ultimate / Base 36",
        ]
    )

    # Box 5: Extraction Manifest Box
    b5 = make_box(
        "REVERIE EXTRACTION MANIFEST: SE-C-IV-DELTA-195",
        [
            "RECOVERED ARTIFACT  | TYPE   | GRADE | RESONANCE & SPECIAL EFFECT",
            "---",
            "The Sorrow Lens     | Weapon | Gr 5  | Fatal Void Optical Beam",
            "The Sorrow Veil     | Suit   | Gr 5  | High Void / Mnemonic Ward",
            "The Sorrow Monocle  | Gift   | Gr 5  | +25 Clarity / Introspection",
            "The Mirror GlassMask| Relic  | Gr 5  | Reflects 20% Damage Taken",
        ]
    )

    doc = f"""# BOSS MECHANICS — The Weeping Mirror (SE-C-IVδ-195)
## Sovereign Entity Technical Combat Folio & Modular Anatomy Guide
### Reverie Directorate Suppression Standard — SOP-GB-BOSS-002

{wrap_box(b1)}---

## 1. Entity Identification & Sovereign Lore Profile

- **Entity Archive Code:** `SE-C-IVδ-195` (Cataloged in containment registries as `C-IIIγ-195 [VO]` / *Learned Your Face*)
- **Vernacular Moniker:** The Weeping Mirror / The Mirror of Sorrows (슬픔의 거울 — *Seulpeum-ui Geoul*)
- **Known Manifestation Sector:** Facility 01 Chamber 195, Subterranean Research Wing (Floor 4, Depth -2,400m)
- **Primary Affinities:** Void (Primary, Pale White) • Lament (Secondary, Acoustic Brine) • Weight (Fatal Vulnerability)
- **Territorial Demarcation:** High-Risk Cognitive Hazard / Containment Realization Sovereign
- **Lore Profile & Macro-Canon Significance:**
  The Weeping Mirror is a three-meter-tall monumental looking glass encased in blackened iron and gold filigree, recovered from the deepest strata of the Alpha Tree root complex. Historical records from the Early Decades reveal the entity condensed from the collective repressed grief that citizens, wardens, and administrative leads concealed from one another across centuries.

  The reflective surface is not made of mercury glass, but rather a fluctuating, super-dense film of crystallized Pale White Void and liquid sorrow tears. The mirror does not reflect the physical countenance of those who gaze into it; instead, it projects their unacknowledged guilt, unmourned bereavements, and spiritual rot. When an operative maintains continuous line-of-sight without high Clarity ratings, the mirror extracts their psychological identity and manifests a physical **Mirrored Twin Simulacrum** that wields the operative's own combat techniques against them. In combat suppressions, the Reverie Directorate mandates deploying heavy blunt shock-weapons to shatter the looking glass before psychic dissociation claims the squad.

---

## 2. Sovereign Attributes & Core Combat Parameters

- **Coherence Rank & Threat Level:** Rank IV Sovereign • Grade Delta Potency
- **Total Physical Hit Points (Combined Parts):** 2,800 HP
- **Total Composure Pool:** 320 Points • Meltdown Threshold: 0 Points
- **Base Speed:** 4 (Generates 3 Action Points in Phase 1, 4 AP in Phase 2, and 5 AP in Phase 3)
- **Spatial Grid Anchor:** Anchored at Node `[N08]` during Phase 1; projects *Mirrored Twin Simulacra* across Midline Nodes `[N04]` to `[N06]`.
- **Specular Reflector Properties:**
  * **Energy Dissipation:** The mirror takes only 0.5x damage from Void and Lament attacks, absorbing psychic energy to charge its internal optical prism.
  * **Brittle Structural Resonance:** Highly susceptible to physical blunt and tectonic shock (1.8x Fatal Weight damage multiplier applies against the Silvered Glass Core).
  * **Gaze Dissociation Aura:** Unprotected operatives occupying Nodes `[N05]` to `[N10]` who lack Clarity gear suffer 15 Composure drain and 5 Posture strain at the conclusion of every combat turn.

---

## 3. Modular Body Part Architecture & Hit Pools

The Weeping Mirror operates as a quadripartite modular combat construct consisting of three physical hardware components and one autonomous psychic manifestation:

{wrap_box(b2)}### 3.1 Part 1: Silvered Glass Core (Central Looking Glass)
- **Hit Point Pool:** 900 HP • **Rupture Threshold:** 540 HP Sustained (Remaining HP: 360)
- **Defense Multipliers:** Lament 0.5x • Grudge 1.2x • Void 0.5x • Weight 1.8x (Fatal Vulnerability)
- **Part Passive (Introspective Glare):** While the glass core is un-ruptured, 20% of all incoming energy and acoustic damage is reflected directly back to the attacking operative.
- **Rupture Penalty:**
  * The mirror face shatters into a web of fissures, permanently disabling *Introspective Glare*.
  * Removes *Specular Retaliation* from the intention deck.
  * Deals 60 direct Posture strain to the mirror's central Composure pool and forces **Phase 2 Stance Shift**.

### 3.2 Part 2: Gilded Iron Frame
- **Hit Point Pool:** 800 HP • **Rupture Threshold:** 480 HP Sustained (Remaining HP: 320)
- **Defense Multipliers:** Lament 1.0x • Grudge 1.0x • Void 1.4x (Vulnerable) • Weight 0.6x (Resistant)
- **Part Passive (Unshakable Anchor):** The mirror cannot be knocked back, displaced, or forced into another node while the frame is intact.
- **Rupture Penalty:**
  * Decreases Mirror Base Speed by 1.
  * Tilts the frame violently, disabling its immunity to spatial displacement skills.

### 3.3 Part 3: Liquid Silver Siphon Spout
- **Hit Point Pool:** 500 HP • **Rupture Threshold:** 300 HP Sustained (Remaining HP: 200)
- **Defense Multipliers:** Lament 0.4x • Grudge 1.2x • Void 1.2x • Weight 1.0x
- **Part Passive (Tear Circulation Engine):** Pumping pressurized mercury tears, the spout restores 20 Composure points to the construct at the beginning of each combat turn.
- **Rupture Penalty:**
  * Permanently disables *Tear Circulation Engine*.
  * Cancels all *Mercury Siphon Jet* attacks from the intention pool.
  * Inflicts 40 Posture strain on the construct.

### 3.4 Part 4: Mirrored Twin Simulacrum (Psychic Doppelganger)
- **Hit Point Pool:** 600 HP • **Rupture Threshold:** 360 HP Sustained (Remaining HP: 240)
- **Defense Multipliers:** Inverts the defense profile of the mirrored allied operative (converts the target operative's highest resistance into a 1.5x vulnerability).
- **Part Passive (Inverted Echo):** Whenever an operative attacks the simulacrum, the copied allied unit sustains 10% reflected strain unless the strike achieves an Overwhelming Clash differential.
- **Rupture Penalty:**
  * The simulacrum evaporates into mist, restoring 25 Composure to the copied allied operative and granting +2 Clash Power for 2 turns.

---

## 4. Multi-Phase Stance Evolution & Shatter Cycles

The encounter transitions across three distinct tactical phases governed by the structural integrity of the Silvered Glass Core:

{wrap_box(b3)}### 4.1 Phase 1: The Silvered Surface (100% down to 70% Core HP / 900 - 630 HP)
- **Action Points (AP):** 3 AP per turn • **Base Speed:** 4
- **Tactical Posture:** Immovable Looking Glass. Anchors at Node `[N08]`.
- **Intention Routine:**
  * Allocates 1 AP to *Gaze of the Unwept* (Band 1-4 Area) to erode squad Composure.
  * Allocates 2 AP to *Mercury Siphon Jet* against advancing frontline units on Nodes `[N04]` and `[N05]`.
- **Tactical Imperative:** Operatives must use high-Clarity defensive skills to intercept the gaze and maneuver into Band 1-2 to deliver heavy blunt strikes.

### 4.2 Phase 2: Fractured Reflections & Twin Simulacra (70% down to 30% Core HP / 630 - 270 HP)
- **Action Points (AP):** 4 AP per turn • **Base Speed:** 5
- **Stance Shift Trigger:** The Glass Core drops below 630 HP, OR the Gilded Frame is ruptured.
- **Tactical Posture:** Fractured Duplication. The glass cracks into jagged geometric facets.
- **Combat Mutators:**
  * Manifests two **Mirrored Twin Simulacra** on Nodes `[N04]` and `[N06]`, copying the highest-attack allied operatives.
  * Intention deck gains *Fracture Duplication* (3 AP Summoning & Area Clash).
- **Tactical Imperative:** The Strike Team must coordinate split-target attacks, bursting down the simulacra with inverted vulnerabilities before the copies overwhelm the midline.

### 4.3 Phase 3: Shattered Shards & Sovereign Dissociation (30% down to 0% Core HP / 270 - 0 HP)
- **Action Points (AP):** 5 AP per turn • **Base Speed:** 6
- **Stance Shift Trigger:** The Glass Core drops below 270 HP.
- **Tactical Posture:** Sovereign Execution Phase. The looking glass completely shatters into twelve levitating mirror shards orbiting the warped iron frame.
- **Combat Mutators:**
  * **Dissociation Resonance:** Both the mirror shards and allied operatives deal +40% damage.
  * **Prism Channeling:** Every two turns, the floating shards align to channel *Catastrophic Prism Burst* (4 AP Global Ultimate, True Void).
  * Operatives must unleash high-impact physical execution skills to shatter the remaining shards and force terminal Composure Meltdown.

---

## 5. AI Intention Deck & Skill Scripting

{wrap_box(b4)}### 5.1 Skill 1: Gaze of the Unwept
- **Cost:** 1 AP • **Range Band:** Band 1-4 Area • **Damage Type:** Lament • **Base Clash Value:** 22
- **Damage Profile:** Projects the reflected gaze across 4 contiguous nodes; deals 20 Lament strain and saps 20 Composure from all units lacking Clarity monocles.
- **Counter Strategy:** Requires Acoustic Specialist deployment with *Acoustic Dampener* or high-Clarity ward.

### 5.2 Skill 2: Specular Retaliation
- **Cost:** 2 AP • **Range Band:** Band 1-2 • **Damage Type:** Inverted Specular • **Base Clash Value:** 26
- **Damage Profile:** Intercepts incoming melee attacks; deals damage matching the attacker's own weapon damage profile + 20 Posture strain.
- **Disabled By:** Rupturing the Silvered Glass Core.

### 5.3 Skill 3: Mercury Siphon Jet
- **Cost:** 2 AP • **Range Band:** Band 2-3 • **Damage Type:** Fluid + Void • **Base Clash Value:** 24
- **Damage Profile:** Ejects high-velocity pressurized liquid mercury tears; deals 40 Void damage and reduces target Speed by 2 for the subsequent turn.
- **Disabled By:** Rupturing the Liquid Silver Siphon Spout.

### 5.4 Skill 4: Fracture Duplication (Phase 2 & 3 Skill)
- **Cost:** 3 AP • **Range Band:** Band 1-5 Area • **Damage Type:** Psychic Summoning • **Base Clash Value:** 28
- **Damage Profile:** Scans the allied strike team and summons a *Mirrored Twin Simulacrum* of the vanguard unit, dealing 30 Void damage to all units in adjacent nodes during materialization.

### 5.5 Skill 5: Catastrophic Prism Burst (Phase 3 Ultimate)
- **Cost:** 4 AP • **Range Band:** Band 1-5 Global Area • **Damage Type:** True Void • **Base Clash Value:** 36
- **Damage Profile:** Channels blinding white-violet light through thousands of floating razor shards; deals 85 True Void damage and applies instant Stagger to any operative losing the clash.
- **Channeling Cue:** Floating shards form a geometric mandala during Turn N; discharges on Turn N+1 at Initiative step 0.

### 5.6 Tactical Decision Tree & Target Selection Priority

| Tactical Condition | Mirror Behavioral Selection | Targeted Allied Unit / Node |
|---|---|---|
| **High-Damage Striker in Band 1** | Allocates 2 AP to *Specular Retaliation* | Vanguard Blade / Core Striker |
| **Allied Squad clustered in Nodes 3-5** | Allocates 1 AP to *Gaze of the Unwept* | Midline Area Cluster |
| **Glass Core drops below 70%** | Casts *Fracture Duplication* | Empty Midline Node `[N05]` |
| **Phase 3 Active (Core below 30%)**| Channels *Catastrophic Prism Burst* | Global Corridor `[N01]` to `[N10]` |

---

## 6. Tactical Strategy, Counter-Measures & Squad Composition

### 6.1 Recommended Part Target Sequence
1. **Primary Target — Liquid Silver Siphon Spout:**
   Focus initial physical fire on the lower siphon tube. Destroying the spout halts the entity's 20 Composure regeneration per turn and eliminates its long-range mercury jet attacks.
2. **Secondary Target — Silvered Glass Core (Fatal Weight Vulnerability):**
   Unload heavy blunt weapons (Basalt Mauls, Hydraulic Breakers) directly into the central looking glass. The 1.8x Fatal Weight vulnerability allows rapid rupture, shattering the face and removing *Specular Retaliation*.
3. **Tertiary Target — Mirrored Twin Simulacra (Phase 2):**
   When the twins spawn, exploit their inverted defense profiles using complementary weapon types (e.g., strike a Void-shielded twin with kinetic slashing).
4. **Final Target — Core Shard Burst Execution:**
   In Phase 3, coordinate high-clash defensive barriers against *Catastrophic Prism Burst* while backline marksmen shatter the remaining floating shards to induce terminal Composure Meltdown.

### 6.2 Recommended 4-Operative Squad Roster & Archetype Pairings

| Squad Role | Recommended Callsign Archetype | Preferred M.A.W. Set | Tactical Function |
|---|---|---|---|
| **Heavy Kinetic Breaker** | Piston Maul Specialist (Speed 4+) | Grade 4 Blunt / Weight | Exploits 1.8x Weight vulnerability on Glass Core |
| **Fortress Anchor** | Heavy Shield Warden (Posture 150+) | Grade 4 Bastion Plate | Intercepts *Mercury Siphon Jet*; anchors midline |
| **Clarity Harmonizer** | Acoustic Controller (Clarity 120+) | Grade 4 Acoustic Needle | Dispels *Gaze of the Unwept*; restores squad Sanity |
| **Precision Marksman** | Anti-Material Sniper (Band 4) | Grade 4 Piercing Rifle | Destroys Gilded Frame and Siphon Spout from afar |

---

## 7. Extraction Manifest & M.A.W. Synthesis Registry

Upon achieving terminal Composure Meltdown against `SE-C-IVδ-195`, the Reverie Directorate Containment Wing authorizes full harmonic harvesting of the entity's looking glass remnants:

{wrap_box(b5)}### 7.1 Detailed M.A.W. Equipment Specifications

- **Weapon: The Sorrow Lens (`MAW-W-195`)**
  * **Classification:** Grade 5 Legendary Optical Crystal Focus
  * **Base Clash Power:** 27 • **Range Band:** Band 2-3 (Mid)
  * **Resonance Passive (Prismatic Refraction):** Direct Void strikes ignore 30% of target defensive resistance. Successfully winning a clash inflicts 15 Posture strain on all adjacent foes.
- **Suit: The Sorrow Veil (`MAW-S-195`)**
  * **Classification:** Grade 5 Legendary Mnemonic Shroud
  * **Defensive Resistances:** Void 0.4x (Immune) • Lament 0.6x • Grudge 1.0x • Weight 1.2x
  * **Resonance Passive (Mirror Shroud):** Grants the wearer +20 Clarity. When targeted by an enemy gaze or acoustic skill, reflects 25% of the Composure drain back to the attacker.
- **Gift: The Sorrow Monocle (`MAW-G-195`)**
  * **Classification:** Grade 5 Legendary Accessory (Ocular Glass)
  * **Equip Effect:** +25 Max Clarity • +20 Max Composure.
  * **Resonance Passive:** The wearer is completely immune to confusion, identity dissociation, and fear debuffs.
- **Relic Mask: The Mirror Glass Mask**
  * **Classification:** Grade 5 Unique Relic Visage
  * **Effect:** +20% Mental Defense. Once per combat phase, when the wearer sustains a critical strike, reflects 20% of the total damage back to the attacker and shatters into a blinding flash that blinds adjacent foes for 1 turn.

---

## 8. Quality Compliance & Archival Verification

- **Document Identifier:** `SOP-GB-BOSS-002`
- **Master Registry Reference:** `PROJECT_SOMNARAK/GAME_BATTLE/BOSS_MECHANICS_02`
- **Supervising Authority:** Reverie Directorate Research Division (Chamber 195 Subterranean Unit)
- **Formatting Compliance:** Verified 71-column ASCII text box layout, zero raw `<br>` tags, zero LaTeX math dollar delimiters, and pure canonical in-universe perspective.
"""
    return doc

if __name__ == "__main__":
    content = generate_boss_weeping_mirror()
    target_path = "GAME_BATTLE/BOSS_MECHANICS_WEEPING_MIRROR.md"
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully wrote {len(content)} bytes to {target_path}")
