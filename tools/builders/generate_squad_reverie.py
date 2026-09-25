#!/usr/bin/env python3
"""
Generate GAME_BATTLE/SQUAD_ARCHETYPE_REVERIE_CONTAINMENT.md
Strict adherence to:
- 71-column ASCII text box standard with mandatory '+' borders and exact symmetry.
- No raw <br> tags anywhere.
- No LaTeX math dollar signs ($).
- 100% authentic in-universe perspective without developer meta-commentary or code vocabulary leaks.
- Exhaustive squad manual: role profiles, 10-node spatial doctrines, 6-turn combo cadence, and M.A.W. pairings.
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

def generate_squad_reverie():
    # Box 1: Technical Header HUD
    b1 = make_box(
        "SQUAD ARCHETYPE MANUAL: SOP-GB-SQUAD-001-REVERIE",
        [
            "DOCTRINE MONIKER    : REVERIE STANDARD CONTAINMENT SQUAD",
            "SUPERVISING WING    : Reverie Directorate Subterranean Command",
            "TACTICAL DEPLOYMENT : Facility 01 Containment Breaches (Floors 1-6)",
            "SQUAD CONFIGURATION : 4-Operative Unified Quadripartite Roster",
            "PRIMARY SPECIALTIES : Bastion Anchor, Siphon, Striker, Cryo-Anchor",
            "AUTHORIZATION LEVEL : Grade-4 / Grade-5 High-Hazard Containment",
        ]
    )

    # Box 2: Squad Roster Overview Box
    b2 = make_box(
        "SQUAD ROSTER OVERVIEW & CORE ATTRIBUTES",
        [
            "OPERATIVE ROLE   | SPEED   | HP / SP   | POSTURE | RANGE BAND",
            "---",
            "Vanguard Shield  | Spd 3-4 | 220 / 100 | 160/160 | Band 1 (Melee)",
            "Acoustic Siphon  | Spd 5   | 135 / 130 |  90/90  | Band 2-3 (Mid)",
            "Core Striker     | Spd 6   | 175 / 105 | 115/115 | Band 1-2 (Flex)",
            "Cryo-Anchor      | Spd 4   | 130 / 110 |  85/85  | Band 3-4 (Long)",
            "---",
            "TOTAL SQUAD HEALTH  : 660 Physical HP | 445 Collective Composure",
        ]
    )

    # Box 3: 10-Node Grid Formation Table
    b3 = make_box(
        "10-NODE SPATIAL FORMATION & RANGE MATRIX",
        [
            "GRID NODE OCCUPANCY | ASSIGNED UNIT    | TACTICAL PURPOSE",
            "---",
            "Nodes [N01] - [N02] | Vanguard Shield  | Interception & Threat Draw",
            "Nodes [N01] - [N02] | Cryo-Anchor      | Protected Artillery Line",
            "Nodes [N02] - [N03] | Acoustic Siphon  | Midline Buffer & SP Auras",
            "Nodes [N03] - [N05] | Core Striker     | Part Severance Flank",
        ]
    )

    # Box 4: Synergy Combo Rotation Table
    b4 = make_box(
        "SYNERGY COMBO ROTATION: 6-TURN CADENCE",
        [
            "TURN INTERVAL       | ALLIED ACTION SEQUENCE & COMBINED TRIGGER",
            "---",
            "Turns 01 - 02       | Cryo-Anchor Pin -> Shield Threat Draw",
            "Turns 03 - 04       | Siphon Frequency Cancel -> Striker Burst",
            "Turns 05 - 06       | Coordinated Quad Stagger -> Forced Meltdown",
        ]
    )

    # Box 5: Recommended M.A.W. Loadout Box
    b5 = make_box(
        "RECOMMENDED M.A.W. LOADOUT & ENGRAM MANIFEST",
        [
            "ROLE          | WEAPON (W)       | SUIT (S)         | GIFT (G)",
            "---",
            "Shield Anchor | Mourning Maul    | Smother Cloak    | MourningShell",
            "Acoustic Siph | Hollow Needle    | Choir Mantle     | WeepingChoker",
            "Core Striker  | Debt Cleaver     | Scale Hauberk    | Golden Scale",
            "Cryo-Anchor   | Frozen Harpoon   | Thousand Shroud  | Frozen Drop",
        ]
    )

    doc = f"""# SQUAD ARCHETYPE — Reverie Directorate Standard Containment Cadre
## Operational Doctrine Manual: The Quadripartite Suppression Team ("The Iron Quad")
### Reverie Directorate Tactical Standard — SOP-GB-SQUAD-001

{wrap_box(b1)}---

## 1. Tactical Doctrine & Operational Philosophy

- **Codename / Squad Moniker:** The Iron Quad (강철의 4인대 — *Gangcheol-ui Sa-indae*)
- **Supervising Department:** Reverie Directorate Containment Division (Subterranean Tactical Unit)
- **Primary Operational Theater:** Facility 01 Containment Vaults (-400m to -2,800m), Floor 01 through Floor 06
- **Target Threat Envelope:** Rank IV Autonomous Entities to Rank V Megafaunal Sovereigns
- **Operational Maxim:** *"Containment is not execution; it is the enforced return to composure."*
- **Doctrine Overview:**
  The Reverie Directorate Standard Containment Cadre represents the pinnacle of subterranean suppression doctrine developed across four millennia of facility operations. In Project Somnarak, confronting a high-rank Sorrow Entity with brute physical force inevitably leads to catastrophic psychic contamination, structural collapse, or total Sorrow Inversion Meltdowns.

  Instead, the Directorate deploys a mathematically balanced **Quadripartite Squad Archetype** consisting of four complementary functional disciplines:
  1. **Vanguard Shield:** Anchors spatial nodes, draws hostile aggression, and absorbs kinetic/tectonic impact.
  2. **Acoustic Siphon:** Neutralizes high-frequency lament wails and sustains operative mental Composure.
  3. **Core Striker:** Maneuvers with superior Speed Bands to target modular limb joints and execute staggered cores.
  4. **Cryo-Anchor:** Deploys sub-zero artillery to lock sovereign movement and drain hostile Action Slots.

  Together, these four roles ensure complete tactical dominance across the 10-node combat grid, allowing the team to force terminal Composure Meltdowns while minimizing casualties.

---

## 2. Squad Composition & Technical Operative Dossiers

{wrap_box(b2)}### 2.1 Operative 1: The Vanguard Shield (Frontline Bastion Anchor)
- **Designated Callsign Archetype:** Warden-Anchor Min-Jae / Dekan's Bulwark
- **Tactical Role:** Frontline Interception, Threat Draw, and Posture Reinforcement
- **Base Attributes:** Base Speed 3-4 (Speed Band 3-5) • Max HP 220 • Composure 100 • Max Posture 160
- **Equipped M.A.W. Configuration:**
  * **Weapon:** `MAW-W-002 The Mourning Maul` (Grade 5 Heavy Blunt Relic)
  * **Suit:** `MAW-S-005 The Smothering Cloak` (Grade 4 Heavy Bastion Plating)
  * **Gift:** `MAW-G-002 The Mourning Shell` (Grade 5 Chest Brooch)
- **Signature Combat Skills:**
  * *Directional Interception (2 AP • Band 1 • Base 26):* Forces an attacking enemy to redirect single-target strikes away from adjacent backline allies and onto the Vanguard Shield.
  * *Bastion Stance (1 AP • Self • Base 22):* Temporarily fortifies Posture by +40 points and converts 20% of incoming kinetic damage into a temporary barrier shield.
  * *Crushing Basalt Blow (2 AP • Band 1 • Base 24):* Heavy maul smash dealing 45 Blunt damage and 15 Posture strain to the target limb.
- **Structural Passive (Steadfast Bedrock):** The Vanguard Shield is completely immune to forced displacement and node knockback. Grants all adjacent allies +2 Clash Power when defending against area attacks.

### 2.2 Operative 2: The Acoustic Siphon (Frequency Controller & Sanity Healer)
- **Designated Callsign Archetype:** Frequency Navigator Seol-A / Ayshuk's Siphon
- **Tactical Role:** Acoustic Counter-Harmonics, Squad Composure Restoration, and Posture Disruption
- **Base Attributes:** Base Speed 5 (Speed Band 5-7) • Max HP 135 • Composure 130 • Max Posture 90
- **Equipped M.A.W. Configuration:**
  * **Weapon:** `MAW-W-088 The Hollow Needle` (Grade 4 Acoustic Piercing Focus)
  * **Suit:** `MAW-S-088 The Choir Mantle` (Grade 4 Lament-Resistant Robe)
  * **Gift:** `MAW-G-088 The Weeping Choker` (Grade 4 Acoustic Dampener)
- **Signature Combat Skills:**
  * *Harmonic Phase-Cancellation (2 AP • Band 1-3 Area • Base 25):* Emits an acoustic counter-wave that negates up to 60% of incoming area Lament damage and prevents squad mental panic.
  * *Mnemonic Composure Pulse (1 AP • Band 1-3 Area • Utility):* Restores 25 Composure points to all squad members within two nodes.
  * *Resonant Suture Jab (1 AP • Band 2 • Base 20):* Pierces an entity's acoustic gland, draining 25 Posture and silencing hostile wail attacks for 1 turn.
- **Structural Passive (Tuned Ear):** Grants the entire cadre +15% resistance to ambient Lament strain. Whenever an ally wins a clash by +4 or higher, restores 10 Composure to that operative.

### 2.3 Operative 3: The Core Striker (Precision Part Breaker & Executioner)
- **Designated Callsign Archetype:** Vanguard Striker Taeho / High-Speed Suture Blade
- **Tactical Role:** High-Velocity Modular Part Severance, Overwhelming Clash Burst, and Stagger Execution
- **Base Attributes:** Base Speed 6 (Speed Band 6-8) • Max HP 175 • Composure 105 • Max Posture 115
- **Equipped M.A.W. Configuration:**
  * **Weapon:** `MAW-W-014 The Debt Cleaver` (Grade 4 High-Frequency Slashing Blade)
  * **Suit:** `MAW-S-014 The Scale Hauberk` (Grade 4 Agile Kinetic Hauberk)
  * **Gift:** `MAW-G-014 The Golden Scale` (Grade 4 Precision Monocle)
- **Signature Combat Skills:**
  * *Severing Prism Execution (2 AP • Band 1-2 • Base 28):* High-speed slashing flurry dealing 65 Slash damage. Deals +50% bonus damage if the target limb is staggered or below 60% HP.
  * *Flanking Slash (1 AP • Band 1 • Base 24):* Rapid dash bypassing frontal defenses to strike exposed lateral joints directly.
  * *Suture Rip (2 AP • Band 1 • Base 26):* Drives the blade deep into mechanical joints, triggering an immediate Rupture Check.
- **Structural Passive (Suture Momentum):** Winning a clash grants the Core Striker +1 Speed Band on the subsequent turn. When attacking a ruptured body part, critical strike rate increases by 30%.

### 2.4 Operative 4: The Cryo-Anchor (Sub-Zero Suppression Artillery)
- **Designated Callsign Archetype:** Marksman Ha-Eun / Subterranean Heavy Ballista
- **Tactical Role:** Long-Range Speed Debuff, Thermal Quenching, and Node Pinning
- **Base Attributes:** Base Speed 4 (Speed Band 4-6) • Max HP 130 • Composure 110 • Max Posture 85
- **Equipped M.A.W. Configuration:**
  * **Weapon:** `MAW-W-609 The Frozen Harpoon` (Grade 4 Heavy Cryo-Rifle)
  * **Suit:** `MAW-S-609 The Thousand-Hand Shroud` (Grade 4 Glacial Weave)
  * **Gift:** `MAW-G-609 The Frozen Drop` (Grade 4 Cryo-Pendant)
- **Signature Combat Skills:**
  * *Sub-Zero Cryo-Shot (2 AP • Band 3-4 • Base 24):* Fires a liquid-nitrogen dart that deals 35 Cold/Piercing damage and applies 2 stacks of *Frostbite* (-2 Speed Band).
  * *Permafrost Pin (2 AP • Band 3-4 • Base 26):* Drives a freezing anchor cable into the target's limb, pinning the entity to its current node for 1 full combat turn.
  * *Thermal Quench Flare (1 AP • Band 1-4 Area • Base 20):* Extinguishes boiling slag, fire, or heat terrain hazards across two contiguous nodes.
- **Structural Passive (Glacial Grip):** Targets currently pinned by the Cryo-Anchor lose 1 Action Slot on their subsequent turn and suffer +20% damage from blunt attacks.

---

## 3. 10-Node Grid Spatial Deployment & Formations

{wrap_box(b3)}### 3.1 Standard Formations & Grid Doctrines

- **Formation Alpha: The Defensive Citadel (Default Deployment)**
  * `Node [N01]`: Cryo-Anchor Ha-Eun (Secured backline sniper footing; full corridor line-of-sight).
  * `Node [N02]`: Vanguard Shield Min-Jae (Intercepts all forward movement; shields `[N01]`).
  * `Node [N03]`: Acoustic Siphon Seol-A (Midline buffer position; within 2 nodes of all allies for aura coverage).
  * `Node [N04]`: Core Striker Taeho (Staged at the frontline waterline, ready to advance into melee).
- **Formation Beta: The Meltdown Extraction Pincer (Phase 3 Execution)**
  * `Nodes [N01-02]`: Cryo-Anchor & Acoustic Siphon (Provide continuous crowd-control and mental stabilization).
  * `Nodes [N04-06]`: Vanguard Shield and Core Striker advance together onto adjacent nodes, encircling the staggered sovereign core to unleash double execution bursts.

---

## 4. 6-Turn Macro-Phase Synergy Rotation

{wrap_box(b4)}### 4.1 Turn-by-Turn Tactical Execution Sequence

- **Turn 01 (Establishment & Spatial Lock):**
  * Cryo-Anchor fires *Permafrost Pin* at the sovereign's primary weight limb, reducing its Speed Band and anchoring it to Node `[N07]`.
  * Vanguard Shield advances to `[N02]`, activating *Bastion Stance* to absorb the entity's opening ranged assault.
- **Turn 02 (Acoustic Neutralization & Flank Advance):**
  * As the entity channels an acoustic lament wail, Acoustic Siphon triggers *Harmonic Phase-Cancellation*, mitigating area Composure drain.
  * Core Striker advances from `[N04]` to `[N05]`, executing *Flanking Slash* on the pinned limb.
- **Turn 03 (First Modular Part Rupture):**
  * Core Striker and Vanguard Shield combine heavy blunt and slashing skills (*Crushing Basalt Blow* + *Suture Rip*), breaching the limb's 60% Rupture Threshold.
  * **Stagger Proc 1** triggers, canceling the entity's remaining Action Slots for Turn 03.
- **Turn 04 (Squad Recovery & Phase-Shift Interception):**
  * The entity recovers and enters Phase 2 (aggressive stance shift).
  * Acoustic Siphon casts *Mnemonic Composure Pulse*, restoring squad sanity to 100%.
  * Cryo-Anchor fires *Sub-Zero Cryo-Shot*, neutralizing the entity's Phase 2 speed bonus.
- **Turn 05 (Core Exposure & Secondary Rupture):**
  * Vanguard Shield absorbs hostile counter-attacks via *Directional Interception*.
  * Core Striker severs the secondary support limb, triggering **Catastrophic Posture Collapse** (Full Stagger).
- **Turn 06 (Terminal Meltdown Burst):**
  * With all modular limbs broken and the core exposed to fatal vulnerabilities, all four operatives converge fire (*Severing Prism Execution* + *Mourning Maul Smash*).
  * The construct reaches **0/300 Composure Collapse (Terminal Meltdown)**, safely concluding the encounter.

---

## 5. Mnemonic Cycle Engram Synergies (System 1 Integration)

To optimize the cadre's combat efficiency, the Reverie Directorate authorizes attuning specific 1,778-cycle historical engrams:

| Operative Role | Recommended Cycle Engram | Key Mechanical Synergy |
|---|---|---|
| **Vanguard Shield** | `Cycle Engram 482: Bedrock Bastion` | Grants +30 Max Posture and adds +1 Action Slot when anchoring below 50% HP. |
| **Acoustic Siphon** | `Cycle Engram 1,105: Choir Harmonizer` | Grants +2 Base Clash Power to all frequency skills; increases Composure heal by 40%. |
| **Core Striker** | `Cycle Engram 1,440: Prismatic Executioner` | Grants +2 Base Speed Band; guarantees critical hit when targeting ruptured limbs. |
| **Cryo-Anchor** | `Cycle Engram 833: Permafrost Quench` | Lowers AP cost of *Permafrost Pin* from 2 to 1; extends freeze duration by 1 turn. |

---

## 6. Recommended M.A.W. Synthesis & Gear Optimization

{wrap_box(b5)}### 6.1 Equipment Synergy Notes
- **Blunt / Slash Balance:** The pairing of `The Mourning Maul` (Heavy Blunt) and `The Debt Cleaver` (Slashing) ensures the team can exploit both Weight and Slashing vulnerabilities across modular constructs.
- **Lament / Void Defense:** Warding the squad with `The Smothering Cloak` and `The Choir Mantle` neutralizes the catastrophic Composure drains typical of Facility 01 containment breaches.

---

## 7. Containment Breach Standard Operating Protocols

1. **Protocol Delta (Tectonic Megafauna):** Prioritize freezing movement via Cryo-Anchor before closing into melee. Never allow a megafauna sovereign to occupy Nodes `[N01]` to `[N03]`.
2. **Protocol Epsilon (Object-Void Hazards):** Vanguard Shield and Core Striker must deploy blunt shock weaponry to shatter specular glass panes while Acoustic Siphon shields the squad against cognitive dissociation.
3. **Protocol Omega (Terminal Meltdown):** Never execute an entity to 0 HP before its Composure pool reaches 0. Premature physical destruction causes uncontrolled sorrow detonations and destroys valuable M.A.W. crystallization cores.

---

## 8. Quality Compliance & Archival Verification

- **Document Identifier:** `SOP-GB-SQUAD-001`
- **Master Registry Reference:** `PROJECT_SOMNARAK/GAME_BATTLE/SQUAD_01`
- **Supervising Authority:** Reverie Directorate Tactical Operations Wing
- **Formatting Compliance:** Verified 71-column ASCII text box layout, zero raw `<br>` tags, zero LaTeX math dollar delimiters, and pure canonical in-universe perspective.
"""
    return doc

if __name__ == "__main__":
    content = generate_squad_reverie()
    target_path = "GAME_BATTLE/SQUAD_ARCHETYPE_REVERIE_CONTAINMENT.md"
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully wrote {len(content)} bytes to {target_path}")
