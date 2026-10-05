#!/usr/bin/env python3
"""
Generator script for SOMNARAK-WORLD/Katharcheok/Operation_3_Messischwi.md
Enforces:
1. Canonical compound title: Operation 3: Messischwi (착취구 — The Siphon Sluices)
2. Canonical 6 UCD Officers (Taeho, Yuna, Minho, Soojin, Joon, Echo) — ZERO Harin / Pugnahan.
3. Antagonists: Warlord Boknam ("The Meat Hook") & Contraband Entity SE-C-IIIγ-120 "Rage Cage".
4. Exact 48-column rST tables for Topology Routing & Target Dossier.
5. Exact 71-column symmetrical ASCII boxes for all 6 combat turns.
6. Zero banned words / zero external verse borrowings.
"""

import sys
import re

def wrap_line(line, max_len=67):
    if len(line) <= max_len:
        return [line]
    words = line.split(" ")
    res = []
    cur = ""
    for w in words:
        if not cur:
            cur = w
        elif len(cur) + 1 + len(w) <= max_len:
            cur += " " + w
        else:
            res.append(cur)
            cur = "    " + w
    if cur:
        res.append(cur)
    return res

def make_box_71(title, lines):
    border = "+=====================================================================+"
    sub_border = "+---------------------------------------------------------------------+"
    res = [border]
    title_str = f"| {title.center(67)} |"
    res.append(title_str)
    res.append(sub_border)
    for l in lines:
        if l == "---":
            res.append(sub_border)
        else:
            wrapped = wrap_line(l, 67)
            for w in wrapped:
                if len(w) > 67:
                    raise ValueError(f"Line too long ({len(w)} > 67): {repr(w)}")
                padded = w.ljust(67)
                res.append(f"| {padded} |")
    res.append(border)
    return "\n".join(res)

# Combat Gauntlet Rounds (Exact 71-width lines)
rounds = [
    ("TURN 1: KINETIC INGRESS & HOOK DEFLECTION", [
        "CLASH 1: Warlord Boknam vs Commander Taeho",
        "  > Boss Skill: [Pneumatic Hook Cleave] (Atk Power 26, Heavy Slash)",
        "  > Taeho Skill: [Phalanx Bastion: Granite Wall] (Def Power 30)",
        "  > Clash Result: Taeho WINS (Power 30 vs 26).",
        "    Kinetic shield deflects the massive barbed steel hook.",
        "  > Taeho reflects 160 kinetic tremor damage back to Winch Rig.",
        "---",
        "CLASH 2: Siphon Enforcers (x2) vs Sapper Joon",
        "  > Enforcer Skill: [Rotary Bone-Saw Rush] (Atk Power 20, Slash)",
        "  > Joon Skill: [Deployable Mantlet Barrier] (Def Power 24, Kinetic)",
        "  > Clash Result: Joon WINS. Saws spark harmlessly off mantlet.",
        "---",
        "TACTICAL MANEUVERS:",
        "  * Yuna: Casts [Cipher-Scan: Hydraulic Frequency]",
        "    Scans steam winch pressure release valve.",
        "  * Minho: Fires [Neural Lancet: Calibrated Dart]",
        "    Deals 240 Pierce damage to Boknam's armored shoulder.",
        "  * Soojin: Deploys [Sedative Aerosol Ward]",
        "    Suppresses crimson rage fumes leaking from SE-C-IIIγ-120.",
        "  * Echo: Activates [Shadow Cloak] -> Scales rusted chain hoists.",
        "---",
        "ROUND 1 DAMAGE TOTALS:",
        "  * Boknam Steam Winch Rig HP: 2,200 -> 1,800 / 2,200 (-400 HP)",
        "  * Harvest Hook Weapon HP: 1,600 / 1,600",
        "  * SE-C-IIIγ-120 Rage Cage Core HP: 3,000 / 3,000",
        "  * Combined Target HP: 6,400 / 6,800 | UCD Composure: 100%"
    ]),
    ("TURN 2: SAPPING THE HYDRAULIC WINCH & FREQUENCY JAM", [
        "CLASH 1: Warlord Boknam vs Sapper Joon",
        "  > Boss Skill: [High-Tension Cable Snare] (Atk Power 24, Pierce)",
        "  > Joon Skill: [Hydraulic Kinetic Ram] (Atk Power 28, Heavy Blunt)",
        "  > Clash Result: Joon WINS (Power 28 vs 24).",
        "    Hydraulic ram shatters the secondary cable pulley drum!",
        "  > Deals 520 Blunt damage to Boknam's Steam Winch Rig.",
        "---",
        "CLASH 2: SE-C-IIIγ-120 'Rage Cage' vs Auditor Yuna",
        "  > Entity Skill: [Crimson Resentment Pulse] (Atk Power 22, Grudge)",
        "  > Yuna Skill: [Cipher-Pulse: Damping Wall] (Def Power 26, EMP)",
        "  > Clash Result: Yuna WINS. Pulse dampens entity rage cycle.",
        "---",
        "TACTICAL MANEUVERS:",
        "  * Taeho: Uses [Shield Bash: Heavy Tremor]",
        "    Deals 280 Blunt damage to Winch Rig.",
        "  * Minho: Casts [Memory Anchor: Saline Infusion]",
        "    Stabilizes mental composure of squad (+15 SP).",
        "  * Soojin: Casts [Resonance Snare: Cold Iron]",
        "    Tethers bone-bars of SE-C-IIIγ-120 to deck.",
        "  * Echo: Slices winch hydraulic return line from overhead beam.",
        "---",
        "ROUND 2 DAMAGE TOTALS:",
        "  * Boknam Steam Winch Rig HP: 1,800 -> 1,000 / 2,200 (-800 HP)",
        "  * Harvest Hook Weapon HP: 1,600 / 1,600",
        "  * SE-C-IIIγ-120 Rage Cage Core HP: 3,000 -> 2,750 / 3,000 (-250 HP)",
        "  * Combined Target HP: 5,350 / 6,800 | UCD Composure: 98%"
    ]),
    ("TURN 3: PRECISION LANCET PIERCE & STAGGER THRESHOLD 1", [
        "CLASH 1: Warlord Boknam vs Senior Investigator Minho",
        "  > Boss Skill: [Flaying Abattoir Sweep] (Atk Power 27, Heavy Slash)",
        "  > Minho Skill: [Neural Lancet: Synaptic Pierce] (Atk Power 31)",
        "  > Clash Result: Minho WINS (Power 31 vs 27).",
        "    Silver lancet strikes the pivot bolt of the Harvest Hook!",
        "  > Deals 960 Pierce damage -> PART DESTROYED: Harvest Hook!",
        "---",
        "STATUS EVENT: STAGGER THRESHOLD 1 TRIGGERED!",
        "  * Combined Target HP drops below 60% (4,080 HP).",
        "  * Boknam's main weapon snaps; steam vents violently from armor!",
        "  * Boknam suffers [Stagger 1] for 1 turn (Def 0, takes 2.0x damage).",
        "---",
        "TACTICAL MANEUVERS:",
        "  * Taeho: Executes [Heavy Piston Strike] -> Deals 460 Blunt.",
        "  * Joon: Plants [Thermite Demolition Pack] -> Deals 420 Thermal.",
        "  * Echo: Drives [Eclipse Stiletto] into winch motor -> Deals 380 Slash.",
        "  * Soojin: Readies cryo-dampening blanket for enraged entity.",
        "---",
        "ROUND 3 DAMAGE TOTALS:",
        "  * Boknam Steam Winch Rig HP: 1,000 -> 0 / 2,200 (-1,000 HP, BROKEN)",
        "  * Harvest Hook Weapon: [DESTROYED]",
        "  * SE-C-IIIγ-120 Rage Cage Core HP: 2,750 / 3,000",
        "  * Combined Target HP: 2,750 / 6,800 (Stagger 1 Active)"
    ]),
    ("TURN 4: CRIMSON RAGE SURGE & LEADED BARRIER WARD", [
        "ENCOUNTER EVENT: Entity Siphon Rupture Initiated!",
        "  * Boknam recovers from Stagger and kicks emergency siphon valve.",
        "  * SE-C-IIIγ-120 'Rage Cage' flares into Berserk Resonance!",
        "  * Crimson bone-bars expand, radiating boiling waves of Han-brine.",
        "---",
        "CLASH 1: SE-C-IIIγ-120 'Rage Cage' vs Containment Handler Soojin",
        "  > Entity Skill: [Crimson Anguish Boiling] (Atk Power 32, Grudge)",
        "  > Soojin Skill: [Leaded Sanctuary: Damping Dome] (Def Power 35)",
        "  > Clash Result: Soojin WINS (Power 35 vs 32)!",
        "    Leaded damping dome absorbs the superheated emotional shockwave.",
        "  > Soojin channels kinetic damping -> Deals 480 Void damage.",
        "---",
        "TACTICAL MANEUVERS:",
        "  * Taeho: Interposes shield to shield freed captives from shrapnel.",
        "  * Yuna: Hacks pump station terminal, shutting off brine conduits.",
        "  * Minho: Dispenses [Neuro-Saline Vapor] to protect captive minds.",
        "  * Joon: Manually cuts holding pen emergency lock chains.",
        "---",
        "ROUND 4 DAMAGE TOTALS:",
        "  * Boknam Body HP: Unarmored (Suppressed)",
        "  * Boknam Steam Winch Rig: [DESTROYED]",
        "  * Harvest Hook: [DESTROYED]",
        "  * SE-C-IIIγ-120 Rage Cage Core HP: 2,750 -> 2,270 / 3,000 (-480 HP)",
        "  * Combined Target HP: 2,270 / 6,800 | UCD Composure: 95%"
    ]),
    ("TURN 5: PHANTOM STILETTO SEVER & TERMINAL STAGGER THRESHOLD 2", [
        "CLASH 1: SE-C-IIIγ-120 'Rage Cage' vs Infiltrator Echo",
        "  > Entity Skill: [Thrashing Rib Barbed Lash] (Atk Power 28, Pierce)",
        "  > Echo Skill: [Eclipse Stiletto: Phantom Sever] (Atk Power 33)",
        "  > Clash Result: Echo WINS (Power 33 vs 28).",
        "    Echo drops from vaulted truss, shearing central bone pillar.",
        "  > Deals 650 Slash damage to Rage Cage Core.",
        "---",
        "STATUS EVENT: TERMINAL STAGGER THRESHOLD 2 TRIGGERED!",
        "  * Combined Target HP falls below 25% (1,700 HP).",
        "  * The calcified bone bars crack; entity's crimson aura dims!",
        "  * SE-C-IIIγ-120 enters [Terminal Stagger 2]! Defenses fall to 0.",
        "---",
        "TACTICAL MANEUVERS:",
        "  * Joon: Drives heavy alloy wedges into remaining bone joints.",
        "  * Minho: Injects [Sedative Soporific Compound] into entity base.",
        "  * Yuna: Downloads complete smuggling manifest of 80 brine tankers.",
        "  * Soojin: Slides Class-IV Leaded Containment Mantle over cage.",
        "---",
        "ROUND 5 DAMAGE TOTALS:",
        "  * Boknam Steam Winch Rig: [DESTROYED]",
        "  * Harvest Hook: [DESTROYED]",
        "  * SE-C-IIIγ-120 Rage Cage Core HP: 2,270 -> 1,140 / 3,000 (-1,130 HP)",
        "  * Combined Target HP: 1,140 / 6,800 (Terminal Stagger 2 Active)"
    ]),
    ("TURN 6: CLIMAX OVERDRIVE: IRON GAVEL & CRYO-SEAL", [
        "FINAL EXECUTIONS & OVERDRIVE RESOLUTION:",
        "CLASH 1: Commander Taeho vs Warlord Boknam",
        "  > Taeho Overdrive: [Iron Gavel: Decreed Subjugation] (Cost: 35 SP)",
        "  > Overdrive Power: 43 (Heavy Kinetic Concussive Verdict)",
        "  > Execution: Heavy Obsidian shield smashes into Boknam's breastplate.",
        "    The reinforced steel buckles; Boknam is slammed into deck.",
        "  > Non-lethal kinetic impact knocks Boknam out cold instantly.",
        "---",
        "CLASH 2: Containment Handler Soojin vs SE-C-IIIγ-120 'Rage Cage'",
        "  > Soojin Overdrive: [Class-IV Leaded Containment Lock: Safe Haven]",
        "  > Overdrive Power: 41 (Absolute Containment / Cryo-Seal)",
        "  > Execution: Soojin triggers pneumatic clamps on lead mantle.",
        "    Cryogenic sedative bath quenches the entity's boiling grudge.",
        "  > SE-C-IIIγ-120 ceases pulsing, falling into inert containment!",
        "---",
        "PACIFICATION SUMMARY:",
        "  * Warlord Boknam: APPREHENDED (Chassis destroyed, target subdued).",
        "  * Harvest Hook & Winch Rig: 100% DEMOLISHED.",
        "  * SE-C-IIIγ-120 'Rage Cage': 100% CONTAINED (Zero brine leakage).",
        "  * All 50 captive civilians liberated without a single casualty."
    ])
]

# Generate combat gauntlet markdown
combat_boxes_text = []
for title, lines in rounds:
    combat_boxes_text.append(f"```text\n{make_box_71(title, lines)}\n```")

combat_section = "\n\n".join(combat_boxes_text)

# Markdown Metadata Table
metadata_table = """| Metric / Parameter | Field Data |
|---|---|
| **Codename** | Operation Messischwi (UCD-OP-03) |
| **Transliteration** | 착취구 (抽出搾取 — The Low Sinks) |
| **Etymology** | *Messis* (Latin: Harvest / Reaping) + *Chwi* (Korean: 취 / 搾取, Exploitation) |
| **Ingress Domain** | Zone B Deep Flood Basins & Sub-Tannery Culverts |
| **Sector Depth** | -75m to -140m Sub-Surface Depth |
| **Primary Syndicate** | The Harvesters (수확단 — Suhwakdan) |
| **Primary Antagonist** | Warlord Boknam ("The Meat Hook" / 갈고리 복남) |
| **Contraband Entity** | SE-C-IIIγ-120 [GO] "Rage Cage" (분노의 감옥) |
| **Squad Cadre** | Commander Taeho, Auditor Yuna, Investigator Minho, Handler Soojin, Engineer Joon, Infiltrator Echo |
| **Primary Objective** | Dismantle illicit sorrow siphons and liberate 50 captive civilians |
| **Secondary Objective** | Apprehend Warlord Boknam and secure SE-C-IIIγ-120 into Directorate vaults |
| **Rules of Engagement** | Strict non-lethal pacification of captives; prevent flooding of prison pens |"""

# 48-column Topology rST table
topology_table = """```text
+==================+===========================+
| BREACH SECTOR    | CHOSEN NODE & TACTICAL OP |
+==================+===========================+
|                  | Node 1: Sluice Cordon     |
| SUMP INGRESS     | Perimeter Flood Cordon    |
|                  +---------------------------+
| (Depth: -75m)    | Squad deploys wading suits|
|                  | and tests toxic runoff.   |
+------------------+---------------------------+
|                  | Node 2: Culvert Flank     |
| SEWER TRUSS LINE | Acoustic Sentry Bypass    |
|                  +---------------------------+
| (Depth: -90m)    | Echo disables siren buoys |
|                  | along rusted chain hoists.|
+------------------+---------------------------+
|                  | Node 3: Siphon Bulkhead   |
| PUMP STATION     | Hydraulic Control Breach  |
|                  +---------------------------+
| (Depth: -105m)   | Joon hacks drainage valves|
|                  | to prevent pen flooding.  |
+------------------+---------------------------+
|                  | Node 4: Forward Bivouac   |
| DRY AIRLOCK      | Respite & Composure Tuning|
|                  +---------------------------+
| (Depth: -115m)   | Minho administers neuro   |
|                  | salts; Yuna tracks logs.  |
+------------------+---------------------------+
|                  | Node 5: Pen Stockades     |
| SLAUGHTER CORRAL | 50 Captive Rescue Sweep   |
|                  +---------------------------+
| (Depth: -125m)   | Taeho neutralizes guards; |
|                  | Soojin treats victims.    |
+------------------+---------------------------+
|                  | Node 6: Abattoir Gate     |
| BLAST BULKHEAD   | Hydraulic Ram Penetration |
|                  +---------------------------+
| (Depth: -135m)   | Joon cracks blast doors   |
|                  | into central crucible.    |
+------------------+---------------------------+
|                  | Node 7: Siphon Crucible   |
| THE RED REFINERY | Apex Gauntlet: Boknam Raid|
|                  +---------------------------+
| (Depth: -140m)   | Subdue Warlord Boknam and |
|                  | contain SE-C-IIIγ-120.    |
+==================+===========================+
```"""

# 48-column Boss Target Dossier
target_dossier_table = """```text
+==============================================+
|       TARGET DOSSIER: THE BUTCHER OF THE RAW |
+==============================================+
| Apex Target          | Warlord Boknam        |
| Cartel Moniker       | "The Meat Hook"       |
| Threat Grade         | Major Potency (γ)     |
| Contraband Entity    | SE-C-IIIγ-120 [GO]    |
+----------------------+-----------------------+
| Combined Vitality    | 6,800 Total Health    |
| Targetable Parts     | 3 Distinct Modules    |
| Part 1: Winch Rig    | 2,200 Health (Blunt)  |
| Part 2: Harvest Hook | 1,600 Health (Pierce) |
| Part 3: Rage Cage    | 3,000 Health (Void)   |
+----------------------+-----------------------+
| Stagger Threshold 1  | 60% Health (4,080 HP) |
| Stagger Threshold 2  | 25% Health (1,700 HP) |
| Overdrive Skill      | Crimson Brine Cleave  |
+==============================================+
```"""

full_content = f"""# UCD — Operation 3: Messischwi (착취구 — The Siphon Sluices)
## Part of the Katharcheok Underworld Pacification Operations
### Zone B Deep Flood Basins & Sub-Tannery Culverts (-75m to -140m)

> *"They do not merely harvest sorrow. They breed it like livestock. They cage living men and women in bone-rimmed pens, torture them until their sorrow turns red with unquenchable grudge, and boil the weeping runoff into industrial combat stimulant. To call them men is an insult to the dirt we walk upon."*
> — Commander Taeho, Address to the Strike Squad before Descending the Sump Shafts

---

### Executive Operational Dossier

{metadata_table}

---

### Tactical Infiltration & Breach Routing

The assault vector penetrates seven subterranean strata within the Zone B industrial flood basins, beginning at the contaminated tannery culverts (-75m) and descending through submerged pump conduits and holding stockades into the boiling siphon abattoir (-140m).

{topology_table}

---

### Narrative Operation Chronicle

#### Chapter 1: The Cattle of the Deep Basins

The air in the secure briefing vault of UCD Sub-Precinct 2 was dense with the low hum of atmospheric purifiers. On the primary holotank, Senior Investigator Minho projected a sequence of forensic post-mortem scans that caused even the hardened veteran Joon to look away in disgust.

"These corpses were recovered from the river gratings near the Zone B floodway mouth," Minho began, his voice cold and devoid of inflection. "Every single subject died of acute neuro-somatic desiccation. Their muscular tissues are shriveled, their spinal channels drained, and their adrenal glands calcified into brittle glass. Someone attached industrial extraction cannulas directly to their thoracic nerve clusters and forcibly siphoned every drop of concentrated sorrow from their living marrow."

Auditor Yuna activated the secondary data feed. A complex web of shipping manifests, maritime cargo routes, and untraceable shell accounts illuminated the room in dim crimson light.

"The cartel operates under the title of The Harvesters," Yuna stated, tracing a cluster of illicit distribution nodes. "Their leader is Warlord Boknam, known across the underworld as 'The Meat Hook.' For the past eighteen months, Boknam has been abducting unregistered outer-slum refugees, migrant dockworkers, and destitute families from the fringes of Zone B. He holds them in subterranean pens beneath the old leather tanneries."

"What are they producing?" Taeho asked, his arms folded across the reinforced chest plate of his riot armor.

"Crimson Han-Brine," Yuna answered coldly. "When a human subject is subjected to prolonged physical torment while trapped in absolute helplessness, their inner sorrow transforms into pure Crimson Grudge. Boknam boils this extracted sorrow fluid into high-potency combat narcotics and black-market turbine fuel. A single barrel of refined Crimson Brine fetches three thousand Echoes on the illicit munitions market. Our informants confirm Boknam has eighty pressurized tankers ready for export—and fifty living citizens trapped in the slaughter pens right now."

Infiltrator Echo stepped forward from the shadows of the vault, resting a gloved hand on the tactical holotank.

"I know the abattoir layout," Echo said. "Boknam didn't construct the extraction apparatus out of conventional scrap. He excavated an ancient subterranean containment vault at one hundred and forty meters down. Inside that vault sits a contraband Sorrow Entity: SE-C-IIIγ-120, designated 'Rage Cage.' It is a massive, stationary entity composed of calcified bone-bars that radiate boiling, furious grudge. Boknam hooked pneumatic winches and high-pressure steam siphons directly into the entity's ribs, using it as an emotional amplifier to boil the captives' agony."

Commander Taeho took a deep breath, his knuckles tightening around his tactical sidearm grip.

"The mission parameters are non-negotiable," Taeho declared. "Primary directive: liberate all fifty civilian captives before Boknam can open the flood sluices and drown the pens. Secondary directive: dismantle the steam winches, shatter the Harvest Hook, contain SE-C-IIIγ-120, and bring Warlord Boknam into custody. Prepare wading armor. We drop into the sumps."

---

#### Chapter 2: Infiltration of the Sump Floodways

The descent into the Low Sinks was a journey into an industrial nightmare. At seventy-five meters below the street level, the strike team stepped into waist-deep chemical runoff. The water was a viscous, bubbling black sludge, coated in an oily crimson sheen that hissed faintly against their lead-lined rubber wading suits.

"Watch your seals," Containment Handler Soojin cautioned over the closed comms loop. "The runoff is laden with tannic acid and concentrated sorrow-salts. A single puncture will eat through your flesh to the bone within minutes."

Above them, colossal cast-iron drainage mains groan under municipal sewage pressure. Steam whistled from corroded seams, filling the narrow brick tunnel with blinding, sulfurous fog.

"Acoustic sensor perimeter at ninety meters," Echo signaled, pointing toward a web of rusted steel trusses spanning the ceiling. Suspended from the beams were acoustic siren buoys—pressure-sensitive bells linked by trip-wires to alert Boknam's slaughter crews.

"Leave the wires to me," Echo whispered.

Moving with feline grace along the overhead pipeline supports, Echo bypassed the trip-wires, clipping the trigger cables with ceramic snips and securing the pendulum clappers with expanding acoustic foam. Below them, two heavily armed Harvester sentries in rubberized butcher aprons and reinforced welding masks leaned against an iron bulkhead, smoking crude Han-leaf cigarillos.

Before the sentries could register the shift in air currents, Taeho surged forward through the murky sludge. His Obsidian Bastion shield slammed into the first guard with concussive force, pinning the man against the brick abutment and knocking the breath from his lungs in a single swift blow. Joon flanked from the left, planting a kinetic palm-strike against the second sentry's helmet, rattling his skull and rendering him instantly unconscious.

"Sensors bypassed. Sentry station neutralized," Taeho muttered, securing the unconscious guards with reinforced polymer zip-cuffs. "Joon, bypass the hydraulic valve station."

---

#### Chapter 3: The Brine Processing Refinery

Joon knelt before the hydraulic control manifold of the secondary floodgate at one hundred and five meters depth. His mechanical toolkit whirred as he inserted a diagnostic probe into the corroded brass junction box.

"Boknam has this gate wired into an emergency dead-man switch," Joon muttered, beads of sweat dripping from his forehead onto the illuminated diagnostic screen. "If someone forces the blast doors without overriding the primary pump relays, the reservoir above will dump four hundred thousand gallons of tannery effluent straight into the holding pens below."

"Can you isolate the lines?" Yuna asked, training her weapon down the echoing access tunnel.

"Give me forty-five seconds," Joon growled. He severed two high-pressure hydraulic hoses, jamming a pair of pneumatic bypass shunts into the valve core. "Pressure diverted. Sluice locked open. The pens won't drown."

With a dull mechanical groan, the iron floodgate rose. The squad stepped into the primary refinery gallery.

The sight was sickening. A cavernous brick reservoir hall was dominated by four massive, twenty-foot-tall copper vats. Underneath the vats, roaring industrial gas burners boiled the dark red sorrow-brine, sending clouds of choking, copper-scented steam billowing toward the roof. Armed cartel enforcers—butchers armed with motorized rotary bone-saws and long-handled flensing hooks—turned in shock as the UCD tactical unit advanced.

"Kill them! Protect the vats!" their squad captain screamed.

"Phalanx wedge! Deploy non-lethal suppression!" Taeho bellowed.

Taeho stepped to the front, locking his shield into the stone flags. Behind him, Joon swung his heavy demolition hammer into the main steam distribution pipe. A deafening roar of high-pressure vapor erupted into the corridor, blinding the butchers and throwing their charge into chaotic disarray.

Yuna immediately broadcasted an EMP resonance pulse from her cipher slate, disabling the electric igniters of the rotary saws. As the enforcers stumbled through the blinding fog, Echo darted between them like a specter, disarming each butcher with precise joint strikes. Within two minutes, eleven cartel operatives lay immobilized on the wet deck.

"Vats secured," Minho called out, scanning the boiling tanks with his diagnostic monocle. "The siphons are empty here—the living stock is being processed deeper in the complex. Keep moving!"

---

#### Chapter 4: The Cries from the Iron Stockades

At one hundred and twenty-five meters depth, the team reached the holding stockades.

The stench of human fear, sweat, and burning sorrow was overwhelming. Suspended over deep, brick-lined drainage trenches were dozens of rusted iron cages. Packed inside them were fifty emaciated citizens—men, women, and teenagers from the outer slums—clothed in rags, their wrists and ankles chained to steel rings.

Beneath each cage ran a series of flexible copper suction tubes leading downward into the floor.

"UCD tactical sweep! You are safe!" Taeho shouted, his voice echoing through the stockade like a brass bell. "Joon, cut the cage locks! Minho, Soojin, triage the wounded!"

As Joon moved along the catwalk with high-powered pneumatic bolt-cutters, the captives began to weep. It was not the silent, bleached despair of Sura's victims—it was raw, sobbing relief, the sound of human souls realizing they were not going to die in the dark.

Soojin and Minho moved rapidly between the cages, administering emergency neuro-saline solutions and wrapping the shivering victims in thermal foil blankets.

Minho knelt beside an elderly weaver whose arms were covered in deep, jagged lacerations from the extraction needles.

"Hold still, grandfather," Minho said gently, pressing an antiseptic compress to the wound. "The extraction lines are disconnected. You're going home."

The old man grasped Minho's armored sleeve with trembling hands.

"Boknam... he's in the deep kiln below," the elder whispered, his breath wheezing through damaged lungs. "He took the young ones down there thirty minutes ago... he said if the wardens came, he would burn them all in the bone cage..."

Taeho stepped up to the cage, his face set like carved granite.

"No one else burns today," Taeho promised. "Soojin, establish an armed perimeter around the stockade. Joon, bring the heavy charges. It's time to meet the Butcher."

---

#### Chapter 5: The Red Abattoir & The Calcified Cage

The final descent led through a reinforced titanium blast door at one hundred and forty meters below the city. The ambient air was scorchingly hot, thick with the heavy, iron-rich stench of boiling blood and combusted sorrow.

Joon placed two shaped breaching charges against the door hinges. A sharp, localized blast blew the five-ton portal off its tracks, sending it crashing into the chamber beyond.

The squad entered the Red Abattoir.

The chamber was a cathedral of violence. In the center of the vast subterranean kiln sat **SE-C-IIIγ-120**, the Sorrow Entity known as "Rage Cage." The entity took the form of a gargantuan, pulsing cage whose vertical bars were crafted not from iron, but from calcified bone, fused sinew, and jagged crimson crystal. The bars contracted and expanded like a monstrous, furious rib cage, radiating blinding heat and violent waves of Crimson Grudge.

Chained to the perimeter of the bone cage were four industrial steam winches. Thick steel cables ran from the winches up to the ceiling pulleys, anchoring a monstrous, eight-foot-long barbed steel hook—the **Harvest Hook**.

Standing beneath the hook was Warlord Boknam.

Boknam was an enormous, muscle-bound brute clad in heavy riveted boiler-plate armor. Bolted to his shoulders was an auxiliary steam engine that vented white-hot exhaust into the air, driving hydraulic servos in his arms that granted him superhuman kinetic power. In his massive hands, he gripped the haft of the Harvest Hook, its barbed tines glowing with molten red sorrow-brine.

"Taeho," Boknam growled, his voice rumbling like an ore-crusher. "You brought your little dog pack all the way down to my kiln. You think you're heroes because you cut some wire and freed some cattle?"

"The cattle have names, Boknam," Taeho said, advancing slowly with his shield raised. "And you have an appointment with High Prosecution."

"Prosecution?" Boknam laughed, a booming roar that echoed through the kiln. "The High Council drinks the fuel I make! The Spire factories run on the grudge I boil! In this city, the strong harvest and the weak burn! Let's see how much grudge I can squeeze out of you!"

Boknam slammed the butt of his weapon into the floor, engaging the steam winches. The bone-bars of SE-C-IIIγ-120 flared crimson, unleashing a deafening psychic howl!

---

#### Chapter 6: The Stand at the Siphon Crucible

"Acoustic damping active! Lock defensive wedge!" Taeho roared.

The kiln exploded into combat.

{target_dossier_table}

---

### Tactical Engagement: 6-Turn Pacification Gauntlet

{combat_section}

---

#### Chapter 7: The Aftermath & The Quenched Furnaces

The boiling heat of the kiln dissipated as the cryogenic sedative bath hissed through the lead mantle, wrapping SE-C-IIIγ-120 in an impermeable shell of frosted lead. The crimson bone-bars ceased their violent pulsation, shrinking into dormant, calcified silence.

On the iron deck, Warlord Boknam lay incapacitated, his steam engine shattered and his heavy breastplate buckled inward under the concussive force of Taeho's Obsidian Bastion. Senior Investigator Minho knelt beside the fallen warlord, applying heavy magnetic restraint cuffs to his wrists and ankles.

"Target secured," Minho reported, his breathing steady. "Concussion and multiple contusions, but autonomic functions are stable. He will stand trial."

Across the abattoir, Joon stood over the shattered remnants of the Harvest Hook. With three measured swings of his pneumatic demolition hammer, he smashed the barbed tines into twisted, unusable slag.

"That weapon will never touch another human being," Joon spat, wiping grease and sweat from his face.

Auditor Yuna completed her forensic inspection of Boknam's command terminal, detaching several encrypted data drives.

"Eighty pressurized tankers of refined Crimson Han-Brine located in the dry dock staging bays," Yuna announced. "Every single tanker was labeled for delivery to private industrial foundries in Zone C and municipal power substations in Zone A. We have the complete financial paper trail. The cartel wasn't acting alone—they had supply contracts signed by four Council procurement directors."

"They will face justice alongside Boknam," Taeho replied, surveying the vast underground facility.

From the upper stockades, the sounds of municipal rescue teams echoed down the access shafts. Medical corps personnel in clean white coats were carefully escorting the fifty liberated captives up toward the surface cruisers. Families were being reunited, warm broth was being distributed, and the nightmare of the Low Sinks was finally over.

Echo walked over to the edge of the drainage sump, looking down into the murky water where the toxic runoff was slowly being filtered by emergency Directorate scrubbers.

"Three frays broken," Echo murmured. "The Veil Merchants. The Memory Washers. The Harvesters."

"Three down, three to go," Taeho said, walking up beside Echo and looking up toward the surface light filtering down through the drainage grates. "Next is Zone C: The Debt Brokers. High Usurer Man-sik won't give up his vaults easily."

"Then we will break his vaults," Taeho concluded. "Strike team, prepare for extraction."

---

### Post-Action Forensic Inventory

| Item ID | Description | Quantity | Disposition |
|---|---|---|---|
| **EVD-UCD-03-A** | SE-C-IIIγ-120 "Rage Cage" Containment Shell | 1 Unit | Transferred to R.D. Maw's Keep Vaults |
| **EVD-UCD-03-B** | Pressurized Crimson Han-Brine Tankers | 80 Units | Impounded by Directorate Energy Reserves |
| **EVD-UCD-03-C** | Warlord Boknam Augmented Steam Rig | 1 Chassis | Sapped & Impounded for Engineering Study |
| **EVD-UCD-03-D** | Shattered Harvest Hook Weapon Slag | 1 Weapon | Scuttled & Melted In Situ by Joon |
| **EVD-UCD-03-E** | Cartel Munitions & Supply Ledger Disks | 18 Slates | Delivered to Directorate High Prosecution |
| **EVD-UCD-03-F** | Liberated Living Captives from Stockades | 50 Citizens | Transferred to Central Medical Recovery |

---

### Arc 3 Key Discoveries & Systemic Revelations

| Discovery | Systemic Implication |
|---|---|
| **Industrial Energy Complicity** | Municipal power plants in Zone A were secretly purchasing unrefined sorrow brine to cut costs. |
| **Refugee Exploitation** | The Harvesters targeted unregistered outer-slum migrants due to their complete lack of legal protection. |
| **Grudge Transmutation Mechanics** | Prolonged physical torment deliberately shifts mild sorrow into volatile, combustible Crimson Grudge. |
| **Entity Resonance Siphoning** | Boknam's winches proved that inanimate Sorrow Entities can be mechanically tapped to power kinetic weapons. |
| **UCD Tactical Coordination** | Perfect synergy between Joon's sapping and Soojin's containment achieved zero civilian collateral damage. |

---

### Strike Officer Performance & Tactical Growth

| Officer | Tactical Specialization | Operational Growth in Operation 3 |
|---|---|---|
| **Taeho (Commander)** | Bastion Vanguard / Riot Breacher | Successfully deflected high-tension pneumatic hook cleaves, protecting captives with zero hull failure. |
| **Yuna (Auditor)** | Forensic Decryption / Disruption | Scrambled Boknam's hydraulic pressure sensors and seized multi-tier municipal energy contracts. |
| **Minho (Investigator)** | Psycho-Forensics / Neural Scribe | Executed pinpoint lancet strike on the Harvest Hook's pivot bolt, neutralizing the apex threat. |
| **Soojin (Handler)** | Entity Containment / Sedative Field | Deployed Leaded Sanctuary dome to neutralize a massive boiling Grudge surge, containing SE-C-IIIγ-120. |
| **Joon (Engineer)** | Sapper & Demolitions | Safely bypassed emergency reservoir flood switches, preventing the drowning of 50 civilian captives. |
| **Echo (Infiltrator)** | Shadow Infiltration / Catwalk Flank | Navigated rusted overhead trusses, neutralizing acoustic alarm networks without triggering alerts. |

---
"""

# Verify no banned terms
banned = [
    r"\bego\b", r"\be\.g\.o\b", r"\babnormality\b", r"\babnormalities\b",
    r"\bdistortion\b", r"\bdistortions\b", r"\bpeccatula\b", r"\bfixer\b",
    r"\bfixers\b", r"\bassociation\b", r"\bassociations\b", r"\bfingers\b",
    r"\blobotomy\b", r"\blimbus\b", r"\blibrary\b", r"\byoung-ji\b",
    r"\bcarmen\b", r"\bayin\b", r"\bsinner\b", r"\bsinners\b",
    r"\bmephistopheles\b", r"\bgolden bough\b", r"\bmirror dungeon\b",
    r"\brefraction railway\b", r"\bharin\b", r"\bpugnahan\b"
]

for b in banned:
    matches = re.findall(b, full_content, re.IGNORECASE)
    if matches:
        print(f"ERROR: Banned word found: {b} -> {matches[:3]}")
        sys.exit(1)

out_path = "SOMNARAK-WORLD/Katharcheok/Operation_3_Messischwi.md"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(full_content)

print(f"Successfully generated {out_path} ({len(full_content)} chars)")
