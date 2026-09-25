#!/usr/bin/env python3
"""
Generator script for SOMNARAK-WORLD/Katharcheok/Operation_5_Therionok.md
Enforces:
1. Canonical compound title: Operation 5: Therionok (흑옥투 — The Black Cages)
2. Canonical 6 UCD Officers (Taeho, Yuna, Minho, Soojin, Joon, Echo) — ZERO Harin / Pugnahan.
3. Antagonists: Beastmaster Jagyeon ("The Chain Binder") & Contraband Entity SE-C-IIIγ-102 "The Dancing Chains" / "The Chained Frenzy".
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
    ("TURN 1: KINETIC INGRESS & SHOCK WHIP DEFLECTION", [
        "CLASH 1: Beastmaster Jagyeon vs Commander Taeho",
        "  > Boss Skill: [Harmonic Shock Lash] (Atk Power 28, Electric/Slash)",
        "  > Taeho Skill: [Phalanx Bastion: Obsidian Wall] (Def Power 32)",
        "  > Clash Result: Taeho WINS (Power 32 vs 28).",
        "    Kinetic shield grounds the 50,000-volt high-voltage arc.",
        "  > Taeho reflects 180 kinetic tremor damage back to Beast-Armor.",
        "---",
        "CLASH 2: Pit Gladiators (x2) vs Sapper Joon",
        "  > Gladiator Skill: [Barbed Harpoon Thrust] (Atk Power 22, Pierce)",
        "  > Joon Skill: [Deployable Mantlet Barrier] (Def Power 26, Kinetic)",
        "  > Clash Result: Joon WINS. Harpoons shatter against mantlet.",
        "---",
        "TACTICAL MANEUVERS:",
        "  * Yuna: Casts [Cipher-Scan: Neural Collar Frequency]",
        "    Scans slave-collar resonance receiver on SE-C-IIIγ-102.",
        "  * Minho: Fires [Neural Lancet: Calibrated Dart]",
        "    Deals 260 Pierce damage to Jagyeon's reinforced greaves.",
        "  * Soojin: Deploys [Sedative Aerosol Ward]",
        "    Calms agitated sorrow emissions in the sand pit.",
        "  * Echo: Activates [Shadow Cloak] -> Scales basalt arena pillars.",
        "---",
        "ROUND 1 DAMAGE TOTALS:",
        "  * Jagyeon Beast-Hide Armor HP: 2,400 -> 1,960 / 2,400 (-440 HP)",
        "  * Harmonic Shock Whip HP: 1,800 / 1,800",
        "  * SE-C-IIIγ-102 Chained Frenzy Core HP: 3,400 / 3,400",
        "  * Combined Target HP: 7,160 / 7,600 | UCD Composure: 100%"
    ]),
    ("TURN 2: SAPPING THE WHIP GENERATOR & FREQUENCY JAM", [
        "CLASH 1: Beastmaster Jagyeon vs Sapper Joon",
        "  > Boss Skill: [Dual Lightning Cleave] (Atk Power 26, Heavy Slash)",
        "  > Joon Skill: [Hydraulic Kinetic Ram] (Atk Power 30, Heavy Blunt)",
        "  > Clash Result: Joon WINS (Power 30 vs 26).",
        "    Hydraulic ram smashes the hip battery generator of the whip!",
        "  > Deals 560 Blunt damage to Harmonic Shock Whip.",
        "---",
        "CLASH 2: SE-C-IIIγ-102 'Chained Frenzy' vs Auditor Yuna",
        "  > Entity Skill: [Crimson Chain Flail] (Atk Power 24, Grudge/Slash)",
        "  > Yuna Skill: [Cipher-Pulse: Damping Wall] (Def Power 28, EMP)",
        "  > Clash Result: Yuna WINS. EMP pulse disrupts chain harmonic.",
        "---",
        "TACTICAL MANEUVERS:",
        "  * Taeho: Uses [Shield Bash: Heavy Tremor]",
        "    Deals 300 Blunt damage to Jagyeon's breastplate.",
        "  * Minho: Casts [Memory Anchor: Cognitive Salve]",
        "    Reinforces squad mental composure (+15 SP).",
        "  * Soojin: Deploys [Resonance Snare: Cold Iron]",
        "    Restricts thrashing movement of the beast's limbs.",
        "  * Echo: Slices overhead winch line, dropping steel cage on flank.",
        "---",
        "ROUND 2 DAMAGE TOTALS:",
        "  * Jagyeon Beast-Hide Armor HP: 1,960 -> 1,660 / 2,400 (-300 HP)",
        "  * Harmonic Shock Whip HP: 1,800 -> 1,240 / 1,800 (-560 HP)",
        "  * SE-C-IIIγ-102 Chained Frenzy Core HP: 3,400 -> 3,100 / 3,400 (-300 HP)",
        "  * Combined Target HP: 6,000 / 7,600 | UCD Composure: 98%"
    ]),
    ("TURN 3: PRECISION LANCET PIERCE & STAGGER THRESHOLD 1", [
        "CLASH 1: Beastmaster Jagyeon vs Senior Investigator Minho",
        "  > Boss Skill: [Overcharged Frenzy Lash] (Atk Power 29, Electric)",
        "  > Minho Skill: [Neural Lancet: Synaptic Pierce] (Atk Power 33)",
        "  > Clash Result: Minho WINS (Power 33 vs 29).",
        "    Silver lancet severs the insulated grip of the Shock Whip!",
        "  > Deals 1,240 Pierce damage -> PART DESTROYED: Shock Whip!",
        "---",
        "STATUS EVENT: STAGGER THRESHOLD 1 TRIGGERED!",
        "  * Combined Target HP drops below 60% (4,560 HP).",
        "  * Whip short-circuits, electrocuting Jagyeon's armored gauntlets!",
        "  * Jagyeon suffers [Stagger 1] for 1 turn (Def 0, takes 2.0x damage).",
        "---",
        "TACTICAL MANEUVERS:",
        "  * Taeho: Executes [Heavy Piston Strike] -> Deals 520 Blunt.",
        "  * Joon: Plants [Thermite Disruption Clamp] -> Deals 480 Thermal.",
        "  * Echo: Drives [Eclipse Stiletto] into hip armor -> Deals 440 Slash.",
        "  * Soojin: Readies cryo-dampening mantle for upcoming beast surge.",
        "---",
        "ROUND 3 DAMAGE TOTALS:",
        "  * Jagyeon Beast-Hide Armor HP: 1,660 -> 220 / 2,400 (-1,440 HP)",
        "  * Harmonic Shock Whip: [DESTROYED]",
        "  * SE-C-IIIγ-102 Chained Frenzy Core HP: 3,100 / 3,400",
        "  * Combined Target HP: 3,320 / 7,600 (Stagger 1 Active)"
    ]),
    ("TURN 4: CRIMSON FRENZY THRASH & LEADED SANCTUARY WARD", [
        "ENCOUNTER EVENT: Neural Slave-Collar Overload!",
        "  * Jagyeon recovers from Stagger, triggering slave-collar surge.",
        "  * SE-C-IIIγ-102 'The Chained Frenzy' snaps collar in blind fury!",
        "  * The beast thrashes wildly, whipping burning red chains across pit.",
        "---",
        "CLASH 1: SE-C-IIIγ-102 'Chained Frenzy' vs Handler Soojin",
        "  > Entity Skill: [Whirling Pyre of Grudge-Chains] (Atk Power 34)",
        "  > Soojin Skill: [Leaded Sanctuary: Damping Dome] (Def Power 37)",
        "  > Clash Result: Soojin WINS (Power 37 vs 34)!",
        "    Leaded damping dome absorbs the fiery kinetic chain strikes.",
        "  > Soojin channels kinetic damping -> Deals 540 Void damage.",
        "---",
        "TACTICAL MANEUVERS:",
        "  * Taeho: Interposes shield to shield spectator box exits from fire.",
        "  * Yuna: Locks arena blast gates, preventing entity from escaping.",
        "  * Minho: Dispenses [Neuro-Calming Aerosol] to soothe beast psyche.",
        "  * Joon: Fires pneumatic anchor pitons into beast's rear chains.",
        "---",
        "ROUND 4 DAMAGE TOTALS:",
        "  * Jagyeon Beast-Hide Armor HP: 220 / 2,400",
        "  * Harmonic Shock Whip: [DESTROYED]",
        "  * SE-C-IIIγ-102 Chained Frenzy Core HP: 3,100 -> 2,560 / 3,400 (-540 HP)",
        "  * Combined Target HP: 2,780 / 7,600 | UCD Composure: 95%"
    ]),
    ("TURN 5: PHANTOM STILETTO SEVER & TERMINAL STAGGER THRESHOLD 2", [
        "CLASH 1: SE-C-IIIγ-102 'Chained Frenzy' vs Infiltrator Echo",
        "  > Entity Skill: [Thrashing Vertebrae Cleave] (Atk Power 30, Slash)",
        "  > Echo Skill: [Eclipse Stiletto: Phantom Sever] (Atk Power 35)",
        "  > Clash Result: Echo WINS (Power 35 vs 30).",
        "    Echo leaps from basalt ledge, shearing central chain link.",
        "  > Deals 720 Slash damage to Dancing Chains Core.",
        "---",
        "STATUS EVENT: TERMINAL STAGGER THRESHOLD 2 TRIGGERED!",
        "  * Combined Target HP falls below 25% (1,900 HP).",
        "  * The vertebrae chain links fracture; beast collapses into sand!",
        "  * Both Jagyeon and SE-C-IIIγ-102 enter [Terminal Stagger 2]!",
        "---",
        "TACTICAL MANEUVERS:",
        "  * Joon: Shatters remaining shock collar relays on the arena floor.",
        "  * Minho: Injects [Sedative Soporific Solution] into beast flank.",
        "  * Yuna: Completes full download of 80 criminal bidder manifests.",
        "  * Soojin: Slides Class-IV Leaded Vacuum Cask over dormant core.",
        "---",
        "ROUND 5 DAMAGE TOTALS:",
        "  * Jagyeon Beast-Hide Armor HP: 220 -> 0 / 2,400 (-220 HP, CRUSHED)",
        "  * Harmonic Shock Whip: [DESTROYED]",
        "  * SE-C-IIIγ-102 Chained Frenzy Core HP: 2,560 -> 1,220 / 3,400 (-1,340 HP)",
        "  * Combined Target HP: 1,220 / 7,600 (Terminal Stagger 2 Active)"
    ]),
    ("TURN 6: CLIMAX OVERDRIVE: IRON GAVEL & CRYO-CASK SEAL", [
        "FINAL EXECUTIONS & OVERDRIVE RESOLUTION:",
        "CLASH 1: Commander Taeho vs Beastmaster Jagyeon",
        "  > Taeho Overdrive: [Iron Gavel: Decreed Subjugation] (Cost: 35 SP)",
        "  > Overdrive Power: 45 (Devastating Kinetic Blunt Verdict)",
        "  > Execution: Heavy Obsidian shield smashes into Jagyeon's helm.",
        "    The reinforced plate fractures; Jagyeon is slammed into sand.",
        "  > Non-lethal concussive impact renders Jagyeon unconscious.",
        "---",
        "CLASH 2: Containment Handler Soojin vs SE-C-IIIγ-102 'Dancing Chains'",
        "  > Soojin Overdrive: [Class-IV Leaded Vacuum Seal: Eternal Peace]",
        "  > Overdrive Power: 43 (Absolute Containment / Cryo-Lock)",
        "  > Execution: Soojin clamps leaded seal collar onto entity core.",
        "    Cryogenic vacuum suction pulls all flaming chain-links into cask.",
        "  > SE-C-IIIγ-102 cools into inert dormancy inside lead mantle!",
        "---",
        "PACIFICATION SUMMARY:",
        "  * Beastmaster Jagyeon: APPREHENDED (Armor broken, target secured).",
        "  * Harmonic Shock Whip & Slave Collars: 100% DEMOLISHED.",
        "  * SE-C-IIIγ-102 'Dancing Chains': 100% CONTAINED (Zero casualties).",
        "  * 12 captive juvenile entities safely secured and transferred to R.D."
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
| **Codename** | Operation Therionok (UCD-OP-05) |
| **Transliteration** | 흑옥투 (黑獄賣買 — The Black Cages) |
| **Etymology** | *Therion* (Greek: Beast / Wild Entity) + *Ok* (Korean: 옥 / 獄, Prison / Arena) |
| **Ingress Domain** | Zones D & E Abandoned Basalt Quarries & Subterranean Amphitheater |
| **Sector Depth** | -210m to -280m Sub-Surface Depth |
| **Primary Syndicate** | The Entity Traders (엔티티 밀매단) |
| **Primary Antagonist** | Beastmaster Jagyeon ("The Chain Binder" / 사슬잡이 작연) |
| **Contraband Entity** | SE-C-IIIγ-102 [GO] "Dancing Chains" / "The Chained Frenzy" (사슬의 광란) |
| **Squad Cadre** | Commander Taeho, Auditor Yuna, Investigator Minho, Handler Soojin, Engineer Joon, Infiltrator Echo |
| **Primary Objective** | Infiltrate underground gladiatorial arena and seize illicit auction ledgers |
| **Secondary Objective** | Subdue Beastmaster Jagyeon, liberate captive entities, and seal SE-C-IIIγ-102 |
| **Rules of Engagement** | Strict non-lethal pacification; protect captive entities from slaughter |"""

# 48-column Topology rST table
topology_table = """```text
+==================+===========================+
| BREACH SECTOR    | CHOSEN NODE & TACTICAL OP |
+==================+===========================+
|                  | Node 1: Quarry Ingress    |
| HOIST SHAFT PASS | Perimeter Shaft Cordon    |
|                  +---------------------------+
| (Depth: -210m)   | Squad deploys winch cables|
|                  | and secures entry shaft.  |
+------------------+---------------------------+
|                  | Node 2: Sentry Interdict  |
| BASALT CONCOURSE | Acoustic Sensor Sapping   |
|                  +---------------------------+
| (Depth: -225m)   | Echo silences trip buoys; |
|                  | Taeho suppresses sentries.|
+------------------+---------------------------+
|                  | Node 3: The Menagerie     |
| HOLDING CELLS    | Juvenile Entity Salvage   |
|                  +---------------------------+
| (Depth: -240m)   | Soojin dispenses sedatives|
|                  | to calm abused entities.  |
+------------------+---------------------------+
|                  | Node 4: Forward Bivouac   |
| DRY AIRLOCK      | Respite & Composure Tuning|
|                  +---------------------------+
| (Depth: -255m)   | Minho administers neuro   |
|                  | salts; Yuna taps terminals|
+------------------+---------------------------+
|                  | Node 5: Auction Loges     |
| SPECTATOR TIER   | High-Roller Subjugation   |
|                  +---------------------------+
| (Depth: -265m)   | Yuna seizes buyer logs;   |
|                  | Joon cuts emergency power.|
+------------------+---------------------------+
|                  | Node 6: Colosseum Gates   |
| IRON BLAST PORTAL| Hydraulic Ram Penetration |
|                  +---------------------------+
| (Depth: -275m)   | Joon breaches arena gates |
|                  | into central blood pit.   |
+------------------+---------------------------+
|                  | Node 7: The Blood Pit     |
| SAND AMPHITHEATER| Apex Gauntlet: Jagyeon Op |
|                  +---------------------------+
| (Depth: -280m)   | Subdue Beastmaster Jagyeon|
|                  | and contain SE-C-IIIγ-102.|
+==================+===========================+
```"""

# 48-column Boss Target Dossier
target_dossier_table = """```text
+==============================================+
|       TARGET DOSSIER: THE BEAST BINDER       |
+==============================================+
| Apex Target          | Beastmaster Jagyeon   |
| Cartel Moniker       | "The Chain Binder"    |
| Threat Grade         | Major Potency (γ)     |
| Contraband Entity    | SE-C-IIIγ-102 [GO]    |
+----------------------+-----------------------+
| Combined Vitality    | 7,600 Total Health    |
| Targetable Parts     | 3 Distinct Modules    |
| Part 1: Beast Armor  | 2,400 Health (Blunt)  |
| Part 2: Shock Whip   | 1,800 Health (Pierce) |
| Part 3: Frenzy Core  | 3,400 Health (Void)   |
+----------------------+-----------------------+
| Stagger Threshold 1  | 60% Health (4,560 HP) |
| Stagger Threshold 2  | 25% Health (1,900 HP) |
| Overdrive Skill      | Crimson Chain Storm   |
+==============================================+
```"""

full_content = f"""# UCD — Operation 5: Therionok (흑옥투 — The Black Cages)
## Part of the Katharcheok Underworld Pacification Operations
### Zones D & E Abandoned Basalt Quarries & Subterranean Amphitheater (-210m to -280m)

> *"To cage an entity of pure grief, torture it with electrical currents until its sorrow curdles into homicidal rage, and force it to tear indentured gladiators apart for the applause of wealthy gamblers is not commerce. It is a crime against the very nature of human existence. Today, we break the cages."*
> — Containment Handler Soojin, Pre-Breach Briefing at the Quarry Head

---

### Executive Operational Dossier

{metadata_table}

---

### Tactical Infiltration & Breach Routing

The assault vector descends through seven subterranean tiers within the abandoned basalt quarries between Zones D and E, beginning at the quarry hoist machinery (-210m) and penetrating the underground holding menagerie into the sunken blood amphitheater (-280m).

{topology_table}

---

### Narrative Operation Chronicle

#### Chapter 1: The Caged Horrors

The atmosphere in the subterranean briefing vault of UCD Sub-Precinct 4 was thick with dread. On the central holotank, Containment Handler Soojin and Senior Investigator Minho projected footage seized from an underworld courier intercepted along the Zone D perimeter.

The projection showed a circular pit of churned red sand surrounded by high-voltage basalt fences. In the center, a juvenile Sorrow Entity—a small, translucent phantasm of weeping glass—shivered against the bars of a crude lead battery. A towering man in spiked leather armor thrust an electrified pole into the cage. A blue-white discharge of fifty thousand volts surged into the entity, causing it to emit a shrill, heart-wrenching psychic wail that shattered the recording device's audio sensors.

"This is the Black Cages," Soojin said, her voice shaking with quiet fury. "Operated by the Entity Traders Fray. They do not just traffic contraband artifacts—they capture living, juvenile Sorrow Entities from the outskirts and the deep drainage vaults. They torment them with harmonic shock prods to maximize their aggressive frenzy, then pit them against indentured debtors in gladiatorial bloodsports."

Auditor Yuna activated the secondary terminal, displaying a roster of high-stakes auction transactions.

"The bloodsport is merely the entertainment," Yuna explained coldly. "The true profit lies in the auctions that follow each match. High-grade entities that survive the arena are fitted with crude neural-slave collars and sold as biological siege engines to rogue private security corporations, criminal cartels, and corrupt colonial magnates. A single combat-trained entity commands up to two hundred thousand Echoes."

"Who commands the ring?" Commander Taeho asked, his arms folded tightly.

"Beastmaster Jagyeon, known across the underworld as 'The Chain Binder,'" Infiltrator Echo answered, stepping forward. "Jagyeon was once an auxiliary containment specialist expelled from the Reverie Directorate fifteen years ago for torturing specimens. He excavated the ancient basalt quarries at two hundred and eighty meters down. And he possesses an apex prize: SE-C-IIIγ-102, designated 'Dancing Chains.' Jagyeon bound the entity into a monstrous feral chimera he calls 'The Chained Frenzy.' It is powered by pure Crimson Grudge, its vertebrae links glowing white-hot with fury."

Taeho adjusted the straps of his riot armor, his expression set like stone.

"The parameters of Operation 5 are absolute," Taeho commanded. "Primary objective: seal the arena and capture all participating criminal gamblers. Secondary objective: neutralize Beastmaster Jagyeon, liberate all twelve captive juvenile entities into Directorate medical casks, and contain SE-C-IIIγ-102 without civilian collateral damage. Prepare heavy descent gear. We drop into the quarries."

---

#### Chapter 2: Infiltration of the Quarry Shafts

The descent into the abandoned basalt quarries was a descent into an abyss of black stone. At two hundred and ten meters below the surface, the squad stood at the rim of a massive vertical excavation shaft. The air was dry and freezing, carrying the sharp scent of ozone, burnt animal hair, and volatile Crimson Grudge.

"Anchoring descent lines," Sapper Joon whispered, drilling pneumatic pitons into the volcanic basalt. "Two hundred meters of vertical drop. Watch the side ledges—Jagyeon has lookouts posted in the old crane alcoves."

Moving in coordinated silence, the six operatives rappelled down the sheer basalt wall. Overhead, the distant rumble of surface machinery faded into the oppressive quiet of the deep earth.

"Sensor perimeter at two hundred and twenty-five meters," Echo signaled, hanging suspended from their harness.

A web of acoustic trip-wires and infrared beam sensors stretched across the narrow gallery leading to the menagerie. Two cartel sentries in studded leather carapace and thermal visors leaned against a rusted steam hoist, drinking cheap synthetic liquor.

Echo released their harness clamp, dropping soundlessly onto a basalt lintel six feet above the sentries. With a single fluid sweep of their cushioned stun-baton, Echo struck the first sentry's neural nexus. Taeho landed an instant later, his Obsidian shield slamming into the second sentry with muffled concussive force, driving the breath from the guard's lungs and rendering him unconscious before he could reach his alarm horn.

"Sensors looped. Sentries bound," Taeho reported, securing the unconscious men. "Moving into the menagerie."

---

#### Chapter 3: The Subterranean Menagerie

At two hundred and forty meters depth, the squad breached the iron gates of the holding menagerie.

The sight made Soojin gasp in horror. The cavernous basalt hall was divided into dozens of reinforced iron cages. Inside were twelve juvenile Sorrow Entities—Rank II (Murmur) and Rank I (Whisper) grade fragments whimpering in the dark. Several had crude copper shock collars clamped around their ethereal forms, while others were chained to heavy lead anchors.

"They are terrified," Minho murmured, his silver lancet vibrating with the sympathetic resonance of their weeping. "They are not feral by nature—they have been driven mad by constant electric shock and confinement."

"We need to stabilize them before the arena alarms trigger," Soojin urged, unclipping high-volume sedative aerosol dispensers from her utility belt.

Soojin set the dispensers along the central walkway. A gentle, lavender-tinted mist of Han-saline and sedative compound rolled across the cages. Within seconds, the frantic whimpering subsided. The juvenile entities curled into peaceful, shimmering spheres of dormant light.

Joon moved swiftly down the line with pneumatic bolt-cutters, snapping the padlocks and replacing them with temporary Directorate vacuum seals.

"Twelve entities stabilized and prepped for evacuation," Joon reported, wiping sweat from his brow. "Now let's go shut down the circus."

---

#### Chapter 4: The Auction of Living Agony

At two hundred and sixty-five meters below the city, the squad reached the spectator tiers overlooking the sunken colosseum.

Through the reinforced one-way viewing glass of the VIP loges, the squad observed eighty high-profile cartel patrons—crime lords in velvet coats, corrupt municipal contractors, and foreign mercenary brokers—sipping champagne while watching the bloodsport below.

"Yuna, lock down the terminals," Taeho ordered.

Auditor Yuna attached her cipher slate to the central communications junction. Her hands danced across the interface, broadcasting an overriding lock protocol that sealed every hydraulic exit hatch leading out of the spectator loges.

"Exits locked," Yuna announced softly. "All commercial bidding ledgers seized. Eighty bank accounts and twenty-four shell company contracts identified. They aren't going anywhere."

Echo slipped into the arena control booth overhead. With three rapid strikes, Echo neutralized the arena electricians, throwing the master breaker to disable the high-voltage perimeter fences in the sand pit below.

"Fences offline," Echo reported over comms. "The pit is open. Go, Commander."

---

#### Chapter 5: The Arena of Blood & Chains

At two hundred and seventy-five meters depth, Joon set four heavy shaped breaching charges against the iron blast doors of the gladiatorial entrance tunnel.

*BOOM.*

The four-meter gates blew inward, falling with a thunderous crash into the churned red sand of the arena floor. The squad charged into the amphitheater (-280m), forming a tight combat wedge behind Taeho's Obsidian Bastion.

The arena was a colossal circular pit carved from black basalt rock. In the center, chained to four massive hydraulic winches, was **SE-C-IIIγ-102**, "The Dancing Chains."

The Sorrow Entity had been forcibly bound into a terrifying, quadrupedal chimera of fused bone, jagged obsidian scales, and hundreds of glowing red vertebrae chain-links. The beast thrashed against the arena floor, its glowing chain-tails whipping through the air with deafening sonic cracks, radiating furious heat and intense Crimson Grudge.

Standing atop a raised basalt outcropping was Beastmaster Jagyeon.

Jagyeon was an imposing, battle-scarred giant clad in heavy spiked beast-hide armor. In his hands, he wielded twin **Harmonic Shock Whips**—ten-foot braided copper cables that crackled with fifty thousand volts of blinding blue sorrow-disruption arcs.

"Directorate dogs!" Jagyeon roared, his voice booming across the blood-soaked sand. "You think you can ruin my arena? You think you can steal my prize? Look upon the Chained Frenzy! It has torn forty champions to pieces! It will pick your bones clean!"

Jagyeon cracked his shock whips together, sending a massive electrical pulse into the chimera's slave-collar. The beast unleashed a terrifying, ear-splitting psychic shriek, its crimson chains igniting with blazing Han-fire!

---

#### Chapter 6: The Stand in the Sunken Colosseum

"Hold the line! Acoustic wards active!" Taeho bellowed, locking his shield into the red sand.

The battle for the Black Cages was joined.

{target_dossier_table}

---

### Tactical Engagement: 6-Turn Pacification Gauntlet

{combat_section}

---

#### Chapter 7: The Aftermath & The Calmed Menagerie

The roar of the crowd had long turned into terrified silence as municipal warden units flooded the spectator loges, placing high-grade magnetic restraint cuffs on all eighty criminal gamblers.

In the center of the arena pit, the blinding red glow of SE-C-IIIγ-102 had faded into absolute stillness. Soojin knelt beside the heavy lead vacuum cask, checking the pressure gauges with practiced precision. Inside, the dancing chains lay dormant, fully quenched and safely stabilized at sub-zero temperatures.

On the churned red sand, Beastmaster Jagyeon lay unconscious, his spiked armor shattered and his shock whips twisted into useless copper wire. Senior Investigator Minho secured Jagyeon with reinforced carbon-steel restraints.

"Jagyeon is secured," Minho said, looking down at the fallen beastmaster. "Multiple concussive contusions, but autonomic functions are normal. He will face forty consecutive life sentences in the Deep Vaults."

Across the arena, Joon and Echo oversaw the extraction of the twelve captive juvenile entities. Directorate medical transport teams carefully loaded the dormant, glowing spheres into climate-controlled containment cradles for transfer to the Reverie Directorate's rehabilitation sanctuaries.

"All twelve entities safely evacuated," Soojin reported, her voice filled with deep relief. "None suffered permanent psychic trauma. With gentle care and proper resonance tuning, they will fully recover."

Auditor Yuna walked up to Taeho, displaying the completed digital manifests on her cipher slate.

"Eighty criminal patrons detained," Yuna said. "We have seized twenty-four million Echoes in frozen gambling assets and uncovered contracts proving that three private security firms were purchasing weaponized entities for illegal border skirmishes. The entire trafficking network has been decapitated."

Taeho looked up at the towering basalt walls of the colosseum, his face illuminated by the amber glow of the emergency lamps.

"Five operations completed," Taeho said quietly. "The Mask Market. The Bleached Wards. The Low Sinks. The Usury Vaults. And now the Black Cages."

"Only one remains," Echo said, stepping up beside him. "The Underworld King. King Kang-hyuk. In the Sunken Citadel beneath Zone B."

"Kang-hyuk built his throne on the backs of all five syndicates," Taeho said, his grip tightening on his shield strap. "With all five syndicates broken, his citadel stands alone. Prepare the squad for Operation 6: Basileugung. We end this war."

---

### Post-Action Forensic Inventory

| Item ID | Description | Quantity | Disposition |
|---|---|---|---|
| **EVD-UCD-05-A** | SE-C-IIIγ-102 "Dancing Chains" Vacuum Cask | 1 Unit | Transferred to R.D. Maw's Keep Containment |
| **EVD-UCD-05-B** | Liberated Juvenile Sorrow Entities | 12 Entities | Transferred to R.D. Sanctuary Facilities |
| **EVD-UCD-05-C** | Jagyeon Spiked Beast-Armor Chassis | 1 Wreckage | Impounded for Directorate Ballistic Study |
| **EVD-UCD-05-D** | Shattered Harmonic Shock Whip Coils | 2 Whips | Scuttled & Melted In Situ by Joon |
| **EVD-UCD-05-E** | Arena Bidding Servers & Manifest Drives | 12 Disks | Delivered to Directorate High Prosecution |
| **EVD-UCD-05-F** | Detained Criminal Syndicate Patrons | 80 Suspects | In Custody at Central Warden Penitentiary |

---

### Arc 5 Key Discoveries & Systemic Revelations

| Discovery | Systemic Implication |
|---|---|
| **Private Military Trafficking** | Rogue security firms actively purchased weaponized Sorrow Entities for corporate warfare. |
| **Harmonic Torment Methodology** | Electrical stimulation deliberately forces juvenile entities into rampant Grudge frenzies. |
| **Gladiatorial Black Markets** | Illegal bloodsports served as fronts for multi-million Echo corporate money laundering. |
| **Entity Rehabilitation Feasibility** | Abused Sorrow Entities can be returned to peaceful dormancy through sedative Han-saline mist. |
| **Five-Cartel Decapitation** | With the defeat of the Entity Traders, all subordinate underworld syndicates are dismantled. |

---

### Strike Officer Performance & Tactical Growth

| Officer | Tactical Specialization | Operational Growth in Operation 5 |
|---|---|---|
| **Taeho (Commander)** | Bastion Vanguard / Riot Breacher | Successfully grounded 50,000-volt high-voltage shock whip arcs with zero kinetic penetration. |
| **Yuna (Auditor)** | Forensic Decryption / Disruption | Decrypted proprietary arena bidding servers, freezing 24 million Echoes in criminal assets. |
| **Minho (Investigator)** | Psycho-Forensics / Neural Scribe | Executed surgical lancet strike on the shock whip's insulated power conduit, disabling the weapon. |
| **Soojin (Handler)** | Entity Containment / Sedative Field | Calmed 12 terrified juvenile entities and safely contained the raging SE-C-IIIγ-102 without casualties. |
| **Joon (Engineer)** | Sapper & Demolitions | Breached four-meter reinforced arena blast gates in seconds and dismantled the gladiatorial grid. |
| **Echo (Infiltrator)** | Shadow Infiltration / Catwalk Flank | Infiltrated arena control booths, disabling high-voltage electric fences to allow tactical entry. |

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

out_path = "SOMNARAK-WORLD/Katharcheok/Operation_5_Therionok.md"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(full_content)

print(f"Successfully generated {out_path} ({len(full_content)} chars)")
