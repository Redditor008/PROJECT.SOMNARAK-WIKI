#!/usr/bin/env python3
import sys

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
            if len(l) > 67:
                raise ValueError(f"Line too long ({len(l)} > 67): {repr(l)}")
            padded = l.ljust(67)
            res.append(f"| {padded} |")
    res.append(border)
    return "\n".join(res)

all_rounds = [
    ("TURN 1: KINETIC INGRESS & PHALANX LOCKDOWN", [
        "CLASH 1: Boss Gwangseok vs Commander Taeho",
        "  > Boss Skill: [Anvil Cleave] (Atk Power 24, Blunt/Crush)",
        "  > Taeho Skill: [Phalanx Bastion] (Def Power 28, Kinetic Shield)",
        "  > Clash Result: Taeho WINS (Power 28 vs 24).",
        "    Kinetic shock absorbed.",
        "  > Taeho reflects 140 kinetic tremor damage back to Exoskeleton.",
        "---",
        "CLASH 2: Foundry Enforcers (x2) vs Engineer Joon",
        "  > Enforcer Skill: [Pressurized Slag Throw]",
        "    (Atk Power 18, Thermal Burn)",
        "  > Joon Skill: [Magnetic Barricade] (Def Power 22, Alloy Shield)",
        "  > Clash Result: Joon WINS. Slag deflected into concrete floor.",
        "---",
        "TACTICAL MANEUVERS:",
        "  * Yuna: Casts [Forensic Monocle]",
        "    Analyzes Forging Hammer weakness.",
        "  * Minho: Fires [Neural Needle] -> Deals 210 Pierce to Gwangseok.",
        "  * Soojin: Deploys [Resonance Snare]",
        "    Bounds SECC-019 containment.",
        "  * Echo: Activates [Shadow Cloak] -> Slips into rear blind spot.",
        "---",
        "ROUND 1 DAMAGE TOTALS:",
        "  * Boss Gwangseok HP: 5,050 / 5,400 (Exoskeleton: 1,450 / 1,800)",
        "  * Squad Status: All 6 Officers uninjured. Composure: 45 / 50 SP."
    ]),
    ("TURN 2: EMP DISRUPTION & CLOAKING SHATTER", [
        "CLASH 1: Boss Gwangseok vs Auditor Yuna",
        "  > Boss Skill: [Counterfeit Cloak Burst]",
        "    (Atk Power 22, Evasion Up)",
        "  > Yuna Skill: [Veil EMP Disruptor] (Atk Power 27, EMP Overload)",
        "  > Clash Result: Yuna WINS (Power 27 vs 22). EMP wave detonates.",
        "  > Gwangseok false cloaking gems overload and shatter into dust.",
        "  > Gwangseok suffers 320 Pale resonance shock.",
        "    Evasion dropped to 0.",
        "---",
        "CLASH 2: SECC-019 vs Handler Soojin",
        "  > Entity Skill: [Grief Vapor Shroud]",
        "    (Atk Power 20, Hallucination)",
        "  > Soojin Skill: [Lead Seal Gauntlets]",
        "    (Def Power 25, Damping Field)",
        "  > Clash Result: Soojin WINS.",
        "    Sorrow vapor siphoned into lead filter.",
        "---",
        "TACTICAL MANEUVERS:",
        "  * Echo: Strikes from stealth with [Stiletto Flank]",
        "    Deals 340 Slash damage.",
        "  * Taeho: Hits Exoskeleton with [Heavy Baton]",
        "    Inflicts 3 Tremor.",
        "  * Joon: Prepares [Hydraulic Ram] for subsequent round breach.",
        "---",
        "ROUND 2 DAMAGE TOTALS:",
        "  * Boss Gwangseok HP: 4,390 / 5,400 (Exoskeleton: 790 / 1,800)",
        "  * Squad Status: Composure stable at 46 / 50 SP. No casualties."
    ]),
    ("TURN 3: SAPPING THE FORGE & STAGGER THRESHOLD 1", [
        "CLASH 1: Boss Gwangseok vs Engineer Joon",
        "  > Boss Skill: [Sledgehammer Execution]",
        "    (Atk Power 26, Heavy Blunt)",
        "  > Joon Skill: [Hydraulic Impact Ram]",
        "    (Atk Power 31, Structural Sapping)",
        "  > Clash Result: Joon WINS (Power 31 vs 26).",
        "    Ram hits Hammer joint.",
        "  > PART BROKEN: [The Forging Hammer] destroyed!",
        "    (1,200 / 1,200 HP lost).",
        "  > Severe recoil shatters pneumatic conduits on torso.",
        "---",
        "STAGGER 1 TRIGGERED: Total Boss HP drops below 3,800 HP!",
        "  * Boss Gwangseok enters STAGGER!",
        "    Physical defenses reduced by 50%.",
        "  * All enemy counter-stances canceled for remainder of the turn.",
        "---",
        "PUNISHMENT STRIKES:",
        "  * Taeho: [Acoustic Crackdown] deals 360 Blunt",
        "    damage (Critical Hit!).",
        "  * Minho: [Cryo-Needle] deals 280 Pierce, freezing fuel lines.",
        "---",
        "ROUND 3 DAMAGE TOTALS:",
        "  * Boss Gwangseok HP: 3,750 / 5,400",
        "    (Exoskeleton destroyed: 0 / 1,800)",
        "  * Gwangseok Staggered! Squad Composure rises to 48 / 50 SP."
    ]),
    ("TURN 4: THE ENTITY FRENZY & RESONANCE RECOVERY", [
        "ENCOUNTER EVENT: Gwangseok breaks emergency seal on cage!",
        "  * SECC-019 enters Berserk State (+4 Attack Power).",
        "---",
        "CLASH 1: SECC-019 vs Handler Soojin",
        "  > Entity Skill: [Delusion of the False Sky]",
        "    (Atk Power 28, Area Shock)",
        "  > Soojin Skill: [Lead Damping Bubble]",
        "    (Def Power 30, Vacuum Barrier)",
        "  > Clash Result: Soojin WINS (Power 30 vs 28).",
        "    Vacuum bubble absorbs psychic pulse.",
        "---",
        "CLASH 2: Recovered Gwangseok vs Commander Taeho",
        "  > Gwangseok Skill: [Desperate Brawler Punch]",
        "    (Atk Power 16, Blunt)",
        "  > Taeho Skill: [Baton Parry] (Def Power 24, Acoustic Counter)",
        "  > Clash Result: Taeho WINS.",
        "    Gwangseok knocked back against furnace.",
        "---",
        "TACTICAL MANEUVERS:",
        "  * Yuna: Casts [Asset Foreclosure]",
        "    Locks SECC-019 secondary core.",
        "  * Minho: Restores +15 SP to Soojin using [Mnemonic Recall].",
        "  * Echo: Repositions behind the entity primary resonance valve.",
        "---",
        "ROUND 4 DAMAGE TOTALS:",
        "  * SECC-019 HP: 1,980 / 2,400 | Total Encounter HP: 2,980 / 5,400",
        "  * Squad Composure: 50 / 50 SP (Synchronized Lucidity achieved!)."
    ]),
    ("TURN 5: NEURAL INCLINATION & STAGGER THRESHOLD 2", [
        "CLASH 1: SECC-019 vs Infiltrator Echo",
        "  > Entity Skill: [Suffocating False Embrace]",
        "    (Atk Power 23, Pierce)",
        "  > Echo Skill: [Stiletto Sever from Stealth] (Atk Power 32, Slash)",
        "  > Clash Result: Echo WINS (Power 32 vs 23).",
        "    Critical strike on core!",
        "  > Echo slices synthetic sorrow conduits feeding the shroud.",
        "---",
        "TACTICAL TARGETING: Investigator Minho",
        "  > Minho Skill: [Neural Inscription Lance]",
        "    (Atk Power 29, Piercing Cryo)",
        "  > Hits exposed resonance valve -> Deals 480 freezing damage.",
        "---",
        "STAGGER 2 TRIGGERED: Total Encounter HP drops below 1,800 HP!",
        "  * Both Boss Gwangseok and SECC-019 enter Terminal Stagger!",
        "  * Gwangseok drops to both knees; SECC-019 shroud collapses.",
        "---",
        "ROUND 5 DAMAGE TOTALS:",
        "  * Boss Gwangseok HP: 600 / 3,000 | SECC-019 HP: 850 / 2,400",
        "  * Total Encounter HP: 1,450 / 5,400 (Terminal Stagger Procs!)."
    ]),
    ("TURN 6: OVERDRIVE PACIFICATION & LEADING CASK SEAL", [
        "FINAL EXECUTIONS & OVERDRIVE RESOLUTION:",
        "CLASH 1: Commander Taeho vs Boss Gwangseok",
        "  > Taeho Overdrive: [Iron Verdict] (Cost: 35 SP)",
        "    Decree of Unbroken Order unleashed.",
        "  > Taeho strikes with tungsten truncheon discharging 120 dB wave.",
        "  > Deals 600 heavy Blunt concussion damage to Gwangseok.",
        "  > Boss Gwangseok HP: 0 / 3,000. INCAPACITATED & ARRESTED!",
        "---",
        "CLASH 2: Handler Soojin vs SECC-019",
        "  > Soojin Overdrive: [Quarantine Mandate] (Cost: 35 SP)",
        "    Zero Leakage protocol activated.",
        "  > Soojin deploys Class-IV leaded vacuum cask with basalt seal.",
        "  > SECC-019 remaining emotional fluid siphoned into lead vault.",
        "  > Entity HP: 0 / 2,400. SAFELY CONTAINED WITHOUT CASUALTIES!",
        "---",
        "PACIFICATION RESOLUTION: COMPLETE VICTORY!",
        "  * Boss Gwangseok: Subdued and handcuffed.",
        "    Remanded to Warden custody.",
        "  * SECC-019: Sealed in lead cask.",
        "    Logged for RD Maw Keep transfer.",
        "  * Civilian Workers: 12 liberated and shielded. Zero casualties."
    ])
]

round_boxes = [make_box_71(title, lines) for title, lines in all_rounds]

full_content = f"""# KATHARCHEOK — Operation 1: Velumtal (지하 정화 소탕록 제1장: 가면포 / 假面市場)
## Underworld Sweep 1: Counterfeit Veil Foundries & The Mask Market Raid

| Operational Attribute | Mission Specification |
|---|---|
| **Campaign Title** | Katharcheok: The Six Underworld Pacifications (지하 정화 소탕록) |
| **Operation Designation**| Operation 1: Velumtal (가면포 — The Mask Market) |
| **Target Sector** | Zone D Mantle Commons & Sub-Drainage Conduits (0m to -25m) |
| **Ingress Point** | Mantle Commons Northern Sluice & Sub-Vault 4 |
| **Dominant Cartel** | The Veil Merchants Fray (베일 상인단) |
| **Primary Target** | Boss Gwangseok ("The Mask Weaver") & Master Artisan Yeon-woo |
| **Deploying Unit** | The Six Strike Officers of the Joint Task Force (Full Cadre) |
| **Transport Rig** | Class-II Armored Riot Cruiser *The Iron Vanguard* |
| **Contraband Entity Threat**| SECC-019 "The False Shroud" (Rank II/III Contraband Sorrow Entity) |

> *"The Veil is supposed to protect humanity from the weeping outside. But when the Council taxes safety until only the wealthy can breathe, men like Gwangseok turn grief into a counterfeit trade. A false veil does not stop the sorrow; it merely hides the face of the one who is suffocating."*  
> — Commander Taeho, Pre-Breach Tactical Address, Mantle Commons Ingress

---

## The Tactical Breach Grid: Mask Market Ingress Topology

The tactical clearance of the counterfeit Veil stone foundries beneath Zone D is executed across a coordinated seven-node urban breach topology. The Task Force must balance civilian collateral containment, asset preservation, and entity pacification:

```text
+==================+===========================+
| BREACH SECTOR    | CHOSEN NODE & TACTICAL OP |
+==================+===========================+
|                  | Node 1: Market Rim        |
| PERIMETER CORDON | Civilian Cordon & Acoustic|
|                  +---------------------------+
| (Surface to -5m) | Node 2: Alley Interdiction|
|                  | Tripwires & Scout Bypass  |
+------------------+---------------------------+
|                  | Node 3: Sluice Gate       |
| SUB-DRAINAGE RUN | Sub-Sluice 4 Ingress Raid |
|                  +---------------------------+
| (-5m to -15m)    | Node 4: Forward Respite   |
|                  | Bivouac & Composure Tuning|
|                  +---------------------------+
|                  | Node 5: Foundry Terminal  |
|                  | Forensic Ledger Seizure   |
+------------------+---------------------------+
|                  | Node 6: Blast Bulkhead    |
| SANCTUM BREACH   | Joon Hydraulic Piston Ram |
|                  +---------------------------+
| (-15m to -25m)   | Node 7: Lapidary Vault    |
|                  | Boss Gwangseok & SECC-019 |
+==================+===========================+
```

---

## Chapter 1: The Forensic Trail & Briefing at Dawn

The briefing auditorium of the Central Warden Citadel in Zone D was silent except for the low hum of the holographic projector. Outside the reinforced slit windows, the pale grey smog of the Mantle Commons hung heavy over the tenements. On the central display table, a cluster of shimmering azure and violet crystals rotated in suspended animation.

Commander Taeho stood at the head of the conference table, his iron-plated gauntlets resting on the head of his heavy tungsten truncheon. His gaze moved across the five officers gathered before him: Auditor Yuna, Investigator Minho, Handler Soojin, Engineer Joon, and Infiltrator Echo.

"At 03:00 hours this morning, High Council Executive Order 108 became active," Taeho spoke, his baritone voice echoing off the basalt masonry. "Our jurisdiction across The Raw is absolute. Our first objective is the heart of Zone D: The Mask Market. Our target is the criminal syndicate operating under the moniker of **The Veil Merchants Fray**."

Auditor Yuna stepped forward, adjusting her brass-rimmed actuarial monocle. With a sharp flick of her finger, holographic financial streams replaced the crystal imagery. "For six months, the Collectors Bureau has tracked impossible discrepancies in Zone D's municipal energy ledgers. Over eleven thousand households in the Mantle Commons possess functioning Veil matrix fields, yet less than four hundred have paid the mandatory municipal sorrow-filtration tax to the Council. They are not buying genuine Council Veil Stones. They are buying black-market counterfeits manufactured right beneath their feet."

"And the consequence?" Taeho asked.

"Catastrophic failure," Yuna replied, her voice cold and precise. "Authentic Veil Stones are refined from high-density crystalline Han, stabilized through Reverie Directorate thermal dampeners. The stones sold by the Veil Merchants are forged from porous, raw sub-karst mudstone, coated in diluted sorrow brine, and polished with synthetic resin. They function for twelve to eighteen days, giving the buyer a false sense of emotional security. Then, the matrix fractures. When the stone shatters, the user is struck by unshielded, supercritical sorrow radiation. In the past month alone, seventy-four citizens in Sector 3 suffered spontaneous cognitive collapse and entity crystallization."

Investigator Minho tapped his vellum notebook. "And worse, our archival data confirms that the cartel is not merely selling inert rock. They have captured a juvenile, uncatalogued Sorrow Entity. They are using its weeping emotional fluid as a primer to coat the counterfeit gems. That is a direct Class-I violation of municipal containment law."

Echo spoke from the shadows near the back door, their face obscured behind the shifting silver cowl of their defected operative mantle. "The syndicate boss is Gwangseok. In the underworld, they call him 'The Mask Weaver.' He doesn't operate in the open. His foundry is buried thirty meters beneath the Mantle Commons, disguised as an antique glassblowing workshop behind the Lantern Bazaar. His enforcers are armed with pneumatic rivet guns and illicit Han-crystal machetes. If you march regular wardens into that alley, the lookout sentries will pull the emergency levers and dump sixty thousand gallons of corrosive acid into the workshop, incinerating the evidence, the workers, and the captive entity."

Taeho lifted his heavy truncheon, locking it into his belt holster. "Then regular wardens are not going in. We deploy via *The Iron Vanguard*. Joon, prepare the magnetic breaching ram. Soojin, prep a Class-IV leaded vacuum cask. Echo, you have the point. Non-lethal rules of engagement remain active for all civilian laborers. We move in twenty minutes."

---

## Chapter 2: Infiltration of the Lantern Bazaar

The Mantle Commons was a labyrinth of iron fire escapes, narrow stone alleys, and perpetual steam. Hundreds of canvas-topped market stalls crowded the street, lit by thousands of glowing paper lanterns tinted in indigo and amber. Merchants hawked street food, synthetic textiles, and hand-carved ceramic masks—the ubiquitous cultural symbol of Zone D, where citizens concealed their faces to preserve emotional privacy under the oppressive gaze of Council tax inspectors.

*The Iron Vanguard* APC halted two blocks north in a disused municipal coal staging dock. Disembarking silently in civilian mantles over their combat gear, the six strike officers merged into the bustling crowd.

"Lookouts on the third-floor fire escapes," Echo murmured over the encrypted acoustic comm-link, their stride rhythmic and natural. "Two on the left roof, equipped with optical binoculars. One on the chimney above the noodle shop. Do not look up."

"I have their communication relay pinned," Yuna whispered, touching her caliper staff concealed beneath her wool coat. "I am broadcasting a looped carrier signal to their receiver. For the next eight minutes, their monitors show an empty alley."

Minho scanned the crowd through his forensic lenses. "The air is heavy here. Han saturation is at forty-five percent. Look at the people's respirators—half of them have cracked filters. Look at the lapels of their coats. Those small, violet stones pinned to their collars... those are Gwangseok's counterfeits."

"They wear them because they have no choice," Joon grumbled quietly, his heavy engineer pack shifting on his broad shoulders. "An authentic Council Veil Stone costs eight hundred credits. A family in the Mantle Commons makes sixty credits a month. Gwangseok sells his fakes for twenty-five. To these people, he isn't a criminal. He's the only reason their children can walk outside without weeping blood."

"Which makes his crime all the more monstrous," Taeho said firmly. "He profits from their poverty, knowing his stones will kill them in three weeks. Echo, where is the ingress?"

Echo stopped at the end of a blind alley lined with rusted oil barrels. Behind a stack of rotting cedar crates stood a heavy iron door with a reinforced sliding peephole. A small brass sign above the lintel read: *Mantle Glass & Lapidary Arts — Authorized Municipal Supplier*.

"Foundry entrance," Echo whispered. "Two guards behind the plate. Hydraulic lock keyed to a pressure plate under the floorboards."

"Joon," Taeho commanded. "Eight seconds."

---

## Chapter 3: The Lapidary Foundry Breach

Engineer Joon stepped forward, uncoupling the **Magnetic Pneumatic Piston Ram** from his back. He pressed the four contact pads of the ram against the iron door frame. The electromagnets engaged with a deep, resonant clunk that vibrated through the stone lintel.

"Breaching in three... two... one," Joon counted.

He depressed the dual triggers. A concussive burst of compressed CO2 drove the hardened tungsten piston into the door's deadbolt mechanism with twenty metric tons of hydraulic force. The reinforced deadbolt sheared cleanly in two, and the heavy door blew inward off its hinges, crashing into the workshop floor with a deafening clang.

Before the dust could clear, Commander Taeho surged through the breach, his heavy riot shield locked in front of him. "UCD! Drop your weapons and hit the floor!"

The workshop was a cavernous subterranean hall bathed in the sickly yellow glow of industrial Han-vapor lamps. Long wooden workbenches stretched across the room, lined with grinding wheels, stone saws, and chemical soaking baths. Twelve civilian laborers—their faces covered in dust and sweat—froze in terror, dropping their polishing tools.

At the far end of the room, three syndicate enforcers clad in reinforced leather coats drew crude Han-crystal machetes and pneumatic nail guns.

"Wardens!" the lead guard shrieked, raising his nail gun. "Kill the dogs!"

"Phalanx lock!" Taeho commanded. He stepped forward, planting his shield into the flagstones. The burst of steel nails ricocheted harmlessly off his ballistic carapace. Taeho leveled his acoustic riot pike, pulling the trigger.

A directed, 22 kHz acoustic shockwave erupted from the pike's muzzle. The high-frequency sonic pulse slammed through the lead guard's chest, instantly paralyzing his neuromuscular junctions. The guard dropped his weapon, collapsing to his knees in stunned, breathless paralysis.

Behind Taeho, Echo blurred across the room like a shadow, their stiletto striking the second guard's wrist with surgical precision, disarming him before sweeping his legs from beneath him. Joon rushed the third guard, slamming his magnetic barrier shield forward and pinning the enforcer against the brick wall.

"Workshop secured!" Joon shouted.

"Minho, secure the workers," Taeho ordered, scanning the room. "Check them for weapons and injuries. Non-lethal screening only."

Minho approached the huddled laborers, speaking with calm, practiced reassurance. "Stay down, keep your hands visible. You are not under arrest. The UCD is here to dismantle the forge."

---

## Chapter 4: The Truth of the False Veils

Auditor Yuna walked along the primary workbench, picking up a half-carved stone from an iron vice. She tapped the stone with her caliper staff, analyzing the crystal structure on her forensic monocle.

"Disgraceful," Yuna muttered, her brow furrowing. "Porous mudstone from the Zone B drainage quarries. They soak it in chemical dye to match the violet hue of Grade-γ stones, then inject liquid sorrow into the micro-fissures using hydraulic needles. The moment the dye reacts with ambient body heat, the stone begins to degrade."

A door at the back of the workshop creaked open. An elderly woman with silver-streaked hair, wearing a jeweler's apron covered in ink and acid burns, stepped out into the hall, her hands raised.

"Artisan Yeon-woo," Echo identified her instantly. "Former Master Lapidary of the Keepers Archive."

Yeon-woo looked at Echo, then at Taeho's warden badge, a bitter, exhausted smile touching her lips. "So the Council finally sent their hounds. Did Minister Park order the raid? Or was it Commissioner Vane?"

"You violated Municipal Statute 12," Taeho stated coldly. "Counterfeiting municipal safety apparatus. Seventy-four people have collapsed in this district from your stones."

"And five thousand people survived the winter because of them!" Yeon-woo spat, her voice trembling with righteous fury. "Do you have any idea what it costs to live in the Mantle Commons, Commander? The Council raises the Veil tax every quarter! They tell the poor: pay five hundred credits or let your lungs calcify in the fog! The people came to us begging! We gave them stones that worked!"

"They worked for two weeks!" Yuna countered fiercely. "You sold them ticking time bombs! When the matrix shatters, the backfire fractures their nervous systems!"

"Because Gwangseok diluted the resin!" Yeon-woo shouted, pointing toward the heavy trapdoor in the floor. "My original formula was stable! It could hold for six months! But Gwangseok got greedy. He wanted repeat customers. He cut the stabilizers, brought in the beast from the under-quarries, and forced me to mass-produce trash!"

"Where is Gwangseok?" Taeho demanded.

Yeon-woo looked down at the iron trapdoor. "Beneath the floor. Sub-Vault 4. He's down there with his personal guard... and the creature. He's pumping the entity's tears directly into the master vat."

---

## Chapter 5: The Subterranean Vault & The Weeping Cage

Joon used his pneumatic ram to unlatch the hydraulic seals of the floor trapdoor. A steep stone staircase descended into suffocating, icy dampness.

As the squad descended into Sub-Vault 4, the temperature plummeted dramatically. The ambient Han concentration spiked to eighty-five percent. Ahead, the rhythmic, metallic *thump-thump-thump* of a steam-powered hydraulic press echoed through the dark, accompanied by a sound that made Handler Soojin's blood run cold: a high-pitched, childlike weeping that vibrated through the stone floor.

"That's not human crying," Soojin whispered, her leaded gauntlets glowing with defensive runes. "That is an embryonic Sorrow Entity. Class-II at least. It is in extreme psychological distress."

They reached the threshold of the subterranean lapidary chamber. The room was immense—a pre-cataclysm masonry cistern retrofitted into an illegal industrial factory. In the center stood a colossal steel forging press, driven by a sputtering Han-steam boiler.

Suspended above the press inside an electrified iron cage hung a grotesque yet pitiable creature: **SECC-019 "The False Shroud"**. The entity resembled a hovering, translucent shroud composed of weeping sapphire mists, its hollow facial cavity shedding continuous streams of radiant, iridescent sorrow brine. Rubber tubes were jammed into its spectral core, siphoning the liquid directly into the forging molds below.

Standing at the control console was **Boss Gwangseok ("The Mask Weaver")**. A massive, broad-shouldered man clad in a customized pneumatic exo-suit, Gwangseok wore an ornate porcelain demon mask inlaid with gold wire. In his right hand, he wielded a massive, steam-powered lapidary forging hammer, its head glowing with unstable orange heat.

"Taeho," Gwangseok's voice boomed through the mask's vocal synthesizer, deep and distorted. "I wondered how long it would take for the Council to notice my little enterprise."

---

## Chapter 6: The Stand in the Cistern

Commander Taeho stepped into the chamber, raising his heavy baton. "Gwangseok. Shut down the press. Disconnect the siphons. Step away from the console."

Gwangseok laughed—a harsh, barking sound. "Shut it down? Do you know what this operation is worth, Warden? Two hundred thousand credits a week. Half of Zone D drinks, breathes, and sleeps under my false stones. The Council ministers take their cut through shell companies in Zone C! You think you're enforcing justice? You're just cutting into your masters' profit margins!"

"The ministers will answer to the courts," Yuna said coldly, her caliper staff whirring to life. "And you will answer for seventy-four counts of involuntary manslaughter and the torture of an unauthorized entity."

"I answer to no one beneath the surface!" Gwangseok roared.

He slammed his fist onto the control console. An alarm shrieked, and high-voltage electricity surged through the cage of SECC-019. The entity let out a piercing, resonant scream of agony that shattered the glass gauges across the room. The containment bars snapped open, and the weeping creature dropped into the cistern floor, its translucent shroud billowing outward in a blinding, psycho-active azure wave.

Gwangseok leveled his massive forging hammer, the pneumatic pistons hissing with steam. "Kill them all! Feed the wardens to the forge!"

"UCD strike formation!" Taeho bellowed. "Phalanx advance! Soojin, prep the lead cask! We take them both down!"

---

## Engagement Protocol: The Lapidary Vault Siege

```text
+==============================================+
|       TARGET DOSSIER: THE FALSE WEAVER       |
+==============================================+
| Apex Target          | Boss Gwangseok        |
|                      | "The Mask Weaver"     |
+----------------------+-----------------------+
| Accompaniment        | SECC-019 Contraband   |
|                      | "The False Shroud"    |
+----------------------+-----------------------+
| Boss HP Pool         | 5,400 Total HP        |
|                      | (Combined Encounter)  |
+----------------------+-----------------------+
| Stagger Thresholds   | Stagger 1: 3,800 HP   |
|                      | Stagger 2: 1,800 HP   |
+----------------------+-----------------------+
| Primary Weapons      | Pneumatic Sledgehammer|
|                      | Sorrow Vapor Shroud   |
+======================+=======================+
```

```text
{round_boxes[0]}
```

```text
{round_boxes[1]}
```

```text
{round_boxes[2]}
```

```text
{round_boxes[3]}
```

```text
{round_boxes[4]}
```

```text
{round_boxes[5]}
```

---

## Chapter 7: The Aftermath & The Broken Mold

The silence that followed the engagement was broken only by the hiss of cooling steam and the gentle drip of sorrow brine from the shattered vats.

Boss Gwangseok lay sprawled across the stone floor, his pneumatic exoskeleton smoking and cracked, his heavy porcelain demon mask split in two. Commander Taeho stood over him, clicking the heavy leaded-basalt handcuffs around the syndicate kingpin's wrists.

Gwangseok coughed, spitting a mixture of blood and soot onto the stones. He looked up at Taeho with feverish, bloodshot eyes. "You think... you won, Warden? You think taking down my forge changes anything? Go out into the streets. Look at the people. Tomorrow morning, they'll wake up without stones. The fog will roll in, and they'll choke on their own tears. You haven't saved them. You've just condemned them."

"They will receive authentic Council filters," Taeho said evenly. "Funded directly from the seizure of your offshore accounts."

"The Council?" Gwangseok laughed weakly. "The Council will hoard every credit. You're a fool, Taeho. You're an iron dog barking on an empty chain."

Taeho hauled Gwangseok to his feet, handing him over to the two phalanx wardens who had entered the cistern. "Take him to *The Iron Vanguard*. Secure him in the Level -20 detention block."

Across the chamber, Handler Soojin knelt beside the Class-IV leaded vacuum cask. Inside the observation viewport, the pale blue form of SECC-019 floated in suspension, its weeping calmed by the leaded dampening fluid.

"Entity is stable," Soojin reported, wiping sweat from her forehead. "Its resonance core suffered minor trauma from the extraction tubes, but its coherence is intact. It won't fracture."

Minho stood beside her, his hands gently tracing the cask's seals. "What was it before they caged it?"

"A grief echo from the Inundation," Soojin murmured. "The sorrow of someone who covered their face with a veil so their family wouldn't see them cry. Gwangseok took that quiet sorrow and turned it into an engine of profit."

Auditor Yuna emerged from the back office, carrying a heavy steel lockbox. She opened the lid, revealing dozens of bound leather ledgers stamped with the gold-wax crest of the High Council.

"Look at this, Taeho," Yuna said, her voice shaking with quiet fury. "Promissory notes, kickback receipts, and shipping manifests. Five Council commissioners—including Senior Minister Park's chief aide—were taking twelve percent of Gwangseok's revenue. They knew about this forge. They protected it from municipal audits."

Taeho looked at the documents, his face hardening into an expression of unyielding stone. "Keep those ledgers under armed guard, Minho. Nobody touches them. Nobody burns them."

"What do we do with the workers?" Joon asked, looking back at the twelve laborers sitting huddled against the wall, wrapped in emergency foil blankets.

"They were coerced debtors," Taeho replied. "Minho will verify their identities and issue municipal protection scrips. Joon, prepare the demolition charges. We collapse the forging presses and seal the sluice gate. This forge will never pour another drop of false comfort."

Twenty minutes later, the squad climbed the stone stairs to the street level. As the muffled detonations of Joon's charges rumbled deep beneath the earth, collapsing the illegal lapidary foundry into rubble, the morning sun finally broke through the smog of the Mantle Commons, illuminating the streets of Zone D with pale, honest light.

---

## Operation 1 — Forensic Inventory & Post-Action Report

### 1. Seized Contraband & Assets
| Inventory Classification | Quantity / Specification | Disposition & Chain of Custody |
|---|---|---|
| **Counterfeit Veil Stones** | 450 finished units (Mudstone/Resin) | Confiscated; slated for high-heat incinerator destruction |
| **Lapidary Forging Presses** | 12 pneumatic hydraulic stamping rigs | Demolished on-site by Division 05 sapping charges |
| **Unrefined Sorrow Brine** | 1,400 liters of diluted Crimson Han | Secured into leaded tankers; transferred to R.D. Facility 01 |
| **Contraband Sorrow Entity** | SECC-019 "The False Shroud" (Rank II Murmur)| Sealed in Class-IV Cask; routed to R.D. Floor 2 (Maw's Keep)|
| **Syndicate Master Ledger** | 3 bound volumes + encrypted hard drive | Transferred to Auditor Yuna & Keepers Archive custody |
| **Illicit Currency Seizure** | 840,000 Municipal Scrips (Cash/Notes) | Deposited into Zone D Citizen Emergency Relief Fund |

### 2. Personnel Status & Casualty Report
- **UCD Strike Cadre:** 0 casualties, 0 injuries. Maximum squad composure maintained (+50 SP).
- **Civilian Laborers:** 12 workers secured, screened, and granted municipal immunity as victims of debt coercion.
- **Hostile Combatants:** 3 syndicate guards incapacitated via non-lethal acoustic pikes; Boss Gwangseok subdued and detained.

---

## Arc 1 — Key Discoveries & Character Growth

### Key Institutional Discoveries
| Discovery | Tactical & Political Implication |
|---|---|
| **Systemic Veil Exclusion** | Thousands of citizens in Zone D buy counterfeits because legitimate Council Veil taxes are unaffordable. |
| **Entity Sorrow Synthesis** | Syndicates are actively violating Taboo 5 by using captured Sorrow Entities as raw industrial manufacturing material. |
| **High Council Complicity** | Five Council commissioners were accepting kickbacks to conceal the Veil Merchants' operations from municipal wardens. |
| **The Raw's Interdependence** | The criminal economy is deeply intertwined with daily survival; destroying cartels requires providing legitimate public alternatives. |

### Character Growth & Development
| Officer | Psychological & Tactical Development |
|---|---|
| **Taeho (Commander)** | Confronts the bitter reality that the cartels exist because municipal governance failed; recommits to protecting citizens above politics. |
| **Yuna (Auditor)** | Secures direct documentary proof of Council corruption; resolves to use the UCD's legal independence to prosecute oligarchs. |
| **Minho (Investigator)**| Deepens his empathy for coerced laborers; ensures no worker is unfairly criminalized for surviving under syndicate rule. |
| **Soojin (Handler)** | Successfully executes her first in-field entity containment of the campaign; vows to liberate all trafficked entities in The Raw. |
| **Joon (Engineer)** | Achieves flawless structural sapping, destroying the criminal foundry without damaging the civilian tenements above. |
| **Echo (Infiltrator)** | Proves their loyalty to the Task Force by guiding them through former syndicate territory, taking the first step toward personal redemption. |

---

## Next Operational Ingress: Operation 2 — Lethepyo

With the Veil Merchants' primary manufacturing foundries dismantled, intelligence extracted from Gwangseok's hard drives points directly to the drainage canals connecting Zone B and Zone C. There, the second and most terrifying syndicate operates: **The Memory Washers Fray**, commanded by Chief Chemist Sura.

- **Next Chapter:** `Operation_2_The_Memory_Washers.md` (Lethepyo / 표백원)
- **Sector Target:** Zones B & C — The Bleached Wards
"""

with open("SOMNARAK-WORLD/Katharcheok/Operation_1_Velumtal.md", "w", encoding="utf-8") as f:
    f.write(full_content)

print(f"Successfully generated Operation_1_Velumtal.md ({len(full_content)} chars)")
