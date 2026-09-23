#!/usr/bin/env python3
"""
tools/build_jipyeongseondae_1_2.py
Generates the fully enriched, canonical chronicles for:
- Arc 1: Departure — Somnarak Zone E & The Exile's Gate (출항 — 추방자의 관문)
- Arc 2: The Desolate Crossing — Sea of Glass & Dune Whales (황야 횡단 — 유리의 바다)
"""

import os
import sys

sys.path.append(os.path.dirname(__file__))
from box_formatter import make_box

def wrap_box(b):
    return "```text\n" + b + "\n```\n\n"

def build_arc_1():
    sections = []
    
    # Title & Subtitle
    sections.append("# Arc 1: Departure — Somnarak Zone E & The Exile's Gate (출항 — 추방자의 관문)\n")
    sections.append("## The Horizon Caravan Chronicles — Planetary Overland Expedition (Year 4238, Month 1)\n\n")
    
    # Operational Attribute Table
    sections.append("| Operational Attribute | Specification Dossier |\n")
    sections.append("|---|---|\n")
    sections.append("| **Campaign Theater** | The Horizon Caravan (지평선대 — Jipyeongseondae) |\n")
    sections.append("| **Arc Designation** | Arc 1: Departure — The Exile's Gate (추방자의 관문) |\n")
    sections.append("| **Overland Sector** | Somnarak Zone E Border Wall — Blast Gate V (0 to 25 km) |\n")
    sections.append("| **Threat Rating** | UTS-2 (Regional Warden Interdiction Battery) |\n")
    sections.append("| **Deploying Flagship**| The Drift Throne (142.5m Mobile Heavy Sand Cruiser) |\n")
    sections.append("| **Caravan Command** | Supreme Commander Kael (The Drift King) & Guide Hwaran |\n")
    sections.append("| **Primary Opponent** | Warden Battery Commander Vane & Fort Interdiction |\n")
    sections.append("| **Operational Yield** | Blast Gate V Breached & Waystation 01 Ley Access |\n\n")
    
    # Master Dossier Box
    dossier = make_box("EXPEDITION DOSSIER: ARC 1 - THE EXILE'S GATE", [
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
    sections.append(wrap_box(dossier))
    
    # Epigraph Quote
    sections.append('> *"For forty-six years, this gate was a one-way grave. They marched you past the iron teeth, sealed the hydraulic blast doors behind you, and washed your name from the census. Today, we do not sneak past the gate. Today, the gate opens for us."*\n')
    sections.append('> — Kael, The Drift King, standing before Blast Gate V\n\n')
    sections.append('---\n\n')
    
    # Chapter I
    sections.append("## Chapter I: The Leviathan Awakens & The Dust of Zone E\n\n")
    sections.append("The ground began to shake three kilometers before the outer scrap-slums of Zone E saw the silhouette. It was a dull, rhythmic tectonic tremor that vibrated through the corrugated tin roofs, overturned rusted oil drums, and sent flocks of soot-stained pigeons scattering into the overcast smog. Then, rising above the mounds of slag and tangled copper wire, came the iron prow of **The Drift Throne**.\n\n")
    sections.append("The 142.5-meter mobile fortress moved on four articulated sets of heavy adamantine caterpillar tracks, each link taller than a man and forged from Before-Time trench steel. Steam vented from its rear exhaust ports in rhythmic, deafening geysers, carrying the sweet smell of mineral grease and superheated Han-brine. Suspended beneath its reinforced armored belly, twin tungsten ley-probes dragged through the bedrock, harvesting subterranean acoustic resonance to feed its fuel-neutral drive.\n\n")
    sections.append('Aboard the forward catwalk, eighty feet above the frozen red clay, Supreme Commander Kael gripped the rusted handrail. His left arm—an articulated limb of pale, translucent Han-glass that hummed with seismic resonance—glowed faint azure beneath the sleeve of his heavy oilskin duster. Flanking him was Tactical Guide Hwaran, her coal-smudged face framed by soot-tinted ballistic goggles, her hand resting on the lever of her customized steam repeater.\n\n')
    sections.append('"Ley-seismograph confirms solid bedrock along the approach, Commander," Hwaran reported, her voice carrying cleanly through the gale. "Blast Gate V is fifty paces ahead. But Commander Vane has powered up the heavy rail batteries. The bastions are locked in firing position."\n\n')
    sections.append('"Let him lock them," Kael said quietly, his voice like river gravel grinding under iron wheels. "A wall only stops those who intend to return."\n\n')
    sections.append('---\n\n')
    
    # Chapter II
    sections.append("## Chapter II: Blast Gate V & The Warden Redoubt\n\n")
    sections.append("Rising sixty meters into the soot-stained sky, **Blast Gate V** was the western tooth of Somnarak's municipal bulwark. Constructed from solid basalt masonry three meters thick and reinforced with interlocking hydraulic portcullises, the gate had served for half a century as the city's exile terminal. Those condemned by the Council of Sighs were marched between its serrated iron teeth and driven out into the wastes of The Desolate, their citizenship revoked and their identities expunged from the census.\n\n")
    sections.append("Perched atop the central gatehouse was **Warden Battery Commander Vane**. Draped in the dark blue greatcoat of the Municipal Bulwark Corps and reinforced with an exoskeleton of hydraulic recoil dampers, Vane stood behind the armored parapet of **Fort Interdiction**. Flanking him were two dual-barrel 400mm kinetic rail cannons, their rifled barrels traversing downward to bear directly upon the Drift Throne's bridge.\n\n")
    sections.append('"Halt, exile!" Vane\'s voice roared through the fortress loudspeakers, distorted by atmospheric static. "You are an unregistered mechanized convoy operating under treasonous defiance of Section 12 of the Municipal Bulwark Code! Order your sand-rigs to shut down their engines and submit your nomadic scum to quarantine shackles, or this battery will reduce your crawling junk-heap to powdered iron!"\n\n')
    sections.append('---\n\n')
    
    # Chapter III
    sections.append("## Chapter III: The Parley of Ash and Iron\n\n")
    sections.append("Kael raised his left hand, signaling the engine deck. Master Wright Gwan pulled the throttle lever; with a deafening hydraulic screech, the Drift Throne ground to a halt fifty paces before the gate's killing zone, its forward ramps lowering onto the frozen ground like an iron drawbridge.\n\n")
    sections.append('"I did not bring four thousand tons of nomadic steel across three hundred leagues of salt to die on your doorstep, Vane," Kael called back, his deep baritone amplified by the cruiser\'s forward acoustic horn. "The Absolvohan device has activated beneath the city. The Council of Sighs signed the Horizon Pact with the Dawn Initiative. Our expedition is chartered by sovereign treaty. Raise the portcullis."\n\n')
    sections.append('"The Council sits two kilometers below ground drinking filtered wine!" Vane spat back, slamming his armored fist against the brass railing. "They don\'t know the wastes like I do! Beyond that gate lies four thousand kilometers of vitrified glass, acoustic leviathans, and the screaming void! Nothing leaves this city. Nothing enters! Gun crews—commence firing!"\n\n')
    sections.append('The massive rail cannons flared with blinding electric sparks. The siege of the Exile\'s Gate had begun.\n\n')
    sections.append('---\n\n')
    
    # Chapter IV
    sections.append("## Chapter IV: Overland Arena Topology & Combat Engagement Parameters\n\n")
    sections.append("Chief Ley-Seer Sora the Blind adjusted her acoustic headset, projecting the spatial grid across the Drift Throne's tactical display:\n\n")
    
    grid_box = make_box("TACTICAL ARENA TOPOLOGY: SOMNARAK ZONE E EXILE'S GATE", [
        "[STAGE NODES 01 TO 10 - DEBARKATION RAMPS TO FORTRESS REDOUBT]",
        "[N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "---",
        "- Node 01: Drift Throne Debarkation Ramps (Kael Vanguard Band 1)",
        "- Node 02: Dune Scouts & Hwaran (Short Band 2 / Sand-Skimmer Support)",
        "- Node 03: Concrete Berms (Heavy Dredgers Deploying Ballistic Shields)",
        "- Node 04: The Killing Zone (Zone E Automated Minefield & Barbed Wire)",
        "- Node 05: Fort Interdiction (Commander Vane, Kinetic Rail Battery)",
        "- Node 06: Elevated Wall Catwalk (Warden Marksmen / Sniper Array)",
        "- Node 07: High Bastion Wall (Long-Range Mortar Battery)",
        "- Node 08: Hydraulic Gatehouse Piston Housing (Structural Seam)",
        "- Node 09: Blast Gate V Main Portcullis (Reinforced Adamantine Teeth)",
        "- Node 10: Drift Throne Bridge & Siege Battery (Helm Command)"
    ])
    sections.append(wrap_box(grid_box))
    
    sections.append("Fort Interdiction relied upon its dual **Rail Battery** to inflict catastrophic kinetic trauma at long range while protected behind the **Aegis Shield**. Kael's combat doctrine required advancing under the cover of deployable blast berms, neutralizing the battery with heavy trench-cleaver strikes, shattering the forcefield generator, and storming the **Bunker Core**.\n\n")
    sections.append('---\n\n')
    
    # Chapter V: Combat Gauntlet (Turns 01 to 06)
    sections.append("## Chapter V: The Expedition Combat Gauntlet (Turns 01 to 06)\n\n")
    
    # Turn 01 HUD
    t1_hud = make_box("TACTICAL STAGE HUD: ARC 01 - BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 - SOMNARAK ZONE E EXILE'S GATE]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[RAMPS] [SCOUT] [BERM]  [KILL]  [FORT]  [C-WALK][WALL]  [SUMP]  [VENT]  [THRONE]",
        "[KAEL]  [HWARAN]                [VANE]                                  [HELM]",
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
        "- Kael (Drift King): Spd 6 -> 3 AP | HP 4,200/4,200 | SP 50/50 | Posture 160/160",
        "- Hwaran (Guide)   : Spd 7 -> 4 AP | HP 2,800/2,800 | SP 45/45 | Posture 120/120",
        "- Vane (Commander) : Spd 4 -> 2 AP | HP 2,100/2,100 | Posture 340/340 [BUNKER]",
        "- Rail Battery     : Spd 5 -> 3 AP | HP 1,200/1,200 | Posture 280/280 [CHARGING]",
        "- Aegis Shield Gen : Spd 3 -> 1 AP | HP 1,500/1,500 | Posture 300/300 [ACTIVE]"
    ])
    sections.append(wrap_box(t1_hud))
    
    sections.append("### Turn 01 Action Resolution Log (Intercepting the Rail Battery)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Kael initializes `[Han-Glass Ward Stance]`: Left arm crystallizes into resonant glass, granting +4 Protection against kinetic fire.\n")
    sections.append("  * Hwaran prepares `[Furnace Tracer Dart]`: Identifies acoustic weakpoints in Fort Interdiction's power conduit.\n")
    sections.append("  * Fort Interdiction activates `[Overwatch Targeting Grid]`: Increases kinetic accuracy by +20%.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael (Speed 6 -> 3 AP, Heavy Duster delta -1, Poise +20): Advances from Node 01 to Node 02. Spends 2 AP on `[Trench-Cleaver: Kinetic Intercept]`. Holds 1 AP in Guard.\n")
    sections.append("  * Hwaran (Speed 7 -> 4 AP, Scout Gear delta +1, Evasion +15%): Advances to Node 02. Spends 2 AP on `[Steam Repeater Volley]`. Spends 2 AP on `[Acoustic Flare]`.\n")
    sections.append("  * Rail Battery (Speed 5 -> 3 AP): Locks onto Node 02. Spends 3 AP on `[Dual 400mm Hyper-Kinetic Shell]`.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 02 to 05)**: Rail Battery fires `[Dual 400mm Hyper-Kinetic Shell]` (Base 18 + 2 Coins = 28 Power, Heavy Kinetic).\n")
    sections.append("    * Kael intercepts with `[Trench-Cleaver: Kinetic Intercept]` (Base 21 + 2 Coins = 33 Power, Obsidian Heavy Blade).\n")
    sections.append("    * **Clash Outcome**: Kael WINS THE CLASH OVERWHELMINGLY (33 vs 28)!\n")
    sections.append("    * Kael's obsidian cleaver shears the incoming tungsten slug in half mid-flight; the explosive blast detonates harmlessly against his glass arm (`[P3: Parry/Protection]`).\n")
    sections.append("    * Seismic tremor reflects **260 kinetic damage** back through the fortress firing port, inflicting +54 Posture Strain!\n")
    sections.append("  * **Clash 2 (Node 02 to 06)**: Hwaran's `[Steam Repeater Volley]` suppresses the sniper catwalk, forcing three warden squads into cover.\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Rail Battery HP: 1,200 -> **940/1,200** | Posture: **226/280**.\n")
    sections.append("  * Total Fortress HP: 4,800 -> **4,540/4,800** | Posture: **286/340**.\n")
    sections.append("  * Kael Composure: **100% (50/50 SP)**. Zero caravan damage taken.\n\n")
    sections.append('---\n\n')
    
    # Turn 02 HUD
    t2_hud = make_box("TACTICAL STAGE HUD: ARC 01 - BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 - RAIL BATTERY AMPUTATION & BREACH]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[RAMPS] [SCOUT] [BERM]  [KILL]  [FORT]  [C-WALK][WALL]  [SUMP]  [VENT]  [THRONE]",
        "        [KAEL]  [HWARAN]        [VANE]                                  [HELM]",
        "---",
        "- Node 02: Kael (Advancing / Trench-Cleaver Cleaving Battery Mounts)",
        "- Node 03: Hwaran (Furnace Incendiary Shell Overheating Generators)",
        "- Node 05: Fort Interdiction (Rail Battery Destroyed 0/1,200 HP)",
        "- Node 06: Drift Throne Spinal Railgun (Targeting Aegis Shield Nodes)",
        "- Node 10: Helm Command (Venting Counter-Battery Steam)",
        "---",
        "- Kael (Drift King): Spd 8 -> 4 AP [SURGE] | HP 4,200/4,200 | SP 50/50 | Posture 160/160",
        "- Hwaran (Guide)   : Spd 9 -> 5 AP         | HP 2,800/2,800 | SP 45/45 | Posture 120/120",
        "- Vane (Commander) : Spd 3 -> 1 AP         | HP 2,100/2,100 | Posture 238/340",
        "- Rail Battery     : DESTROYED (0/1,200 HP)| HEAVY KINETIC ARTILLERY SILENCED",
        "- Aegis Shield Gen : Spd 3 -> 1 AP         | HP 1,180/1,500 | Posture 230/300"
    ])
    sections.append(wrap_box(t2_hud))
    
    sections.append("### Turn 02 Action Resolution Log (Part Destruction: Rail Battery Shattered)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Kael activates `Desert King's Momentum` (+2 Speed next turn -> Net Speed 8, 4 AP).\n")
    sections.append("  * Vane orders emergency overcharge on the remaining gun barrel: `[Full Salvo Overpressure]`.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael (Speed 8 -> 4 AP [Surge]): Leaps from Node 02 across the berms to Node 03. Spends 3 AP on `[Obsidian Cleaver: Seismic Sundering]`. Holds 1 AP in Guard.\n")
    sections.append("  * Hwaran (Speed 9 -> 5 AP): Moves to Node 03. Spends 3 AP on `[Incendiary Slag Grenade]`. Spends 2 AP on `[Flank Cover]`.\n")
    sections.append("  * Drift Throne Battery (Speed 6 -> 3 AP): Fires long-range kinetic salvo into Aegis generator.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 03 to 05)**: Rail Battery fires `[Full Salvo Overpressure]` (Base 19 + 2 Coins = 27 Power, Heavy Kinetic).\n")
    sections.append("    * Kael clashes with `[Obsidian Cleaver: Seismic Sundering]` (Base 25 + 3 Coins Heads = 44 Power, Heavy Weight/Shatter).\n")
    sections.append("    * **Clash Outcome**: Kael WINS THE CLASH OVERWHELMINGLY (44 vs 27)!\n")
    sections.append("    * Kael lands atop the bunker roof, driving his massive cleaver directly through the battery's hydraulic elevation gear!\n")
    sections.append("    * The gun mounting explodes in a fireball of hydraulic fluid and shattered tungsten gears!\n")
    sections.append("    * Deals **940 Critical Shatter damage** (Weight 2.0x proc!)!\n")
    sections.append("    * **TARGETED PART DESTROYED**: The Twin Rail Battery is completely destroyed (**Battery HP: 0/1,200** credit)!\n")
    sections.append("    * **EFFECT**: Fortress artillery permanently silenced; fortress permanently loses 1 Speed Slot!\n")
    sections.append("  * **Aegis Generator Damage**:\n")
    sections.append("    * Hwaran's incendiary grenade fuses the forcefield cooling vents for **320 Heat damage**!\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Rail Battery: **DESTROYED (0/1,200 HP)**.\n")
    sections.append("  * Aegis Shield: 1,500 -> **1,180/1,500** | Posture: **230/300**.\n")
    sections.append("  * Total Fortress HP: 4,540 -> **3,280/4,800** | Posture: **182/340 [BATTERY SHATTERED]**.\n")
    sections.append("  * Kael Composure: Stable (50/50 SP).\n\n")
    sections.append('---\n\n')
    
    # Turn 03 HUD
    t3_hud = make_box("TACTICAL STAGE HUD: ARC 01 - BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 - STAGGER THRESHOLD 1 & AEGIS BREACH]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[RAMPS] [SCOUT] [BERM]  [KILL]  [FORT]  [C-WALK][WALL]  [SUMP]  [VENT]  [THRONE]",
        "                [KAEL]  [HWARAN][VANE]                                  [HELM]",
        "---",
        "- Node 03: Kael (Han-Glass Fist Driving into Forcefield Emitter)",
        "- Node 04: Hwaran (Thermite Charge Burning Hydraulic Feeders)",
        "- Node 05: Fort Interdiction (STAGGER LEVEL 1 / FORCEFIELD COLLAPSED)",
        "- Node 10: Drift Throne Siege Ram (Advancing on Gatehouse Pylons)",
        "---",
        "- Kael (Drift King): Spd 8 -> 4 AP [SURGE] | HP 4,200/4,200 | SP 50/50 | Posture 160/160",
        "- Hwaran (Guide)   : Spd 8 -> 4 AP         | HP 2,800/2,800 | SP 45/45 | Posture 120/120",
        "- Vane (Commander) : Spd 0 -> 0 AP         | HP 1,840/2,100 | Posture 126/340 [STAGGER LEVEL 1]",
        "- Aegis Shield Gen : Spd 0 -> 0 AP         | HP 560/1,500   | Posture 88/300 [BREACHED]",
        "- Total Fortress   : HP 2,400/4,800 [THRESHOLD BREACHED / TAKES 1.5X DAMAGE]"
    ])
    sections.append(wrap_box(t3_hud))
    
    sections.append("### Turn 03 Action Resolution Log (First Stagger Proc & Aegis Forcefield Shattered)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Vane retreats into the reinforced bunker cupola, activating emergency shielding: `[Bulwark Lockdown]`.\n")
    sections.append("  * Kael channels seismic charge into his translucent glass fist: `[Tectonic Resonance Charge]`.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael (Speed 8 -> 4 AP): Moves to Node 04 right at the bunker entrance. Spends 2 AP on `[Glass Fist: Resonance Fracture]`. Spends 2 AP on `[Cleaver Cleave]`.\n")
    sections.append("  * Hwaran (Speed 8 -> 4 AP): Advances to Node 04. Spends 2 AP on `[Thermite Breaching Charge]`.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 04 to 05)**: Aegis Generator projects `[Bulwark Lockdown]` (Defense Power 23).\n")
    sections.append("    * Kael strikes with `[Glass Fist: Resonance Fracture]` (Base 24 + 2 Coins = 36 Power, Seismic Weight).\n")
    sections.append("    * **Clash Outcome**: Kael WINS THE CLASH OVERWHELMINGLY (36 vs 23)!\n")
    sections.append("    * Kael's crystalline fist punches directly through the forcefield projector; acoustic waves shatter the sapphire emitter into blue powder!\n")
    sections.append("    * Hwaran's thermite charge burns through the armor housing, melting the power cables!\n")
    sections.append("    * Deals **620 Seismic/Heat damage** and +104 Posture Strain!\n")
    sections.append("- **Step 4: STAGGER THRESHOLD 1 TRIGGERED!**:\n")
    sections.append("  * Total Fortress HP crosses 70% threshold (3,360 HP), falling to **2,400/4,800 HP**; Posture crosses 60% strain line!\n")
    sections.append("  * **STAGGER LEVEL 1 ACTIVE!** The blue forcefield shatters into blinding sparks; bunker blast doors crack open; fortress takes +50% damage across all incoming attacks!\n")
    sections.append("- **Step 5: Turn End State**:\n")
    sections.append("  * Total Fortress HP: 3,280 -> **2,400/4,800 [THRESHOLD BREACHED: Below 3,360 HP!]**.\n")
    sections.append("  * Aegis Shield: 1,180 -> **560/1,500** | Posture: **88/300 [BREACHED]**.\n")
    sections.append("  * Boss Posture: **126/340 [STAGGER LEVEL 1]**.\n")
    sections.append("  * Kael Status: Unbroken.\n\n")
    sections.append('---\n\n')
    
    # Turn 04 HUD
    t4_hud = make_box("TACTICAL STAGE HUD: ARC 01 - BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 - MAXIMUM BURST & PHASE 2 THRESHOLD SKIP]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[RAMPS] [SCOUT] [BERM]  [KILL]  [FORT]  [C-WALK][WALL]  [SUMP]  [VENT]  [THRONE]",
        "                        [KAEL]  [VANE]  [HWARAN]                        [HELM]",
        "---",
        "- Node 04: Kael (Four-Fold Trench-Cleaver Execution on Redoubt)",
        "- Node 05: Commander Vane (Immobilized / Exoskeleton Venting Hydraulic Fluid)",
        "- Node 06: Hwaran (Spinal Battery Concentrated Fire on Blast Doors)",
        "- Node 10: Drift Throne Prow Ram (Crushing Outer Trench Barricades)",
        "---",
        "- Kael (Drift King): Spd 11 -> 5 AP [BURST CRIT] | HP 4,200/4,200 | SP 50/50",
        "- Vane (Commander) : Spd 0 -> 0 AP               | HP 580/2,100   | Posture 48/340",
        "- Aegis Shield Gen : DESTROYED (0/1,500 HP)",
        "- Total Fortress   : HP 580/4,800 [BURST DAMAGE 1,820! SECOND THRESHOLD SKIPPED]"
    ])
    sections.append(wrap_box(t4_hud))
    
    sections.append("### Turn 04 Action Resolution Log (Maximum Burst & Phase 2 Threshold Skip)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Fort Interdiction remains completely stunned; the blast doors are torn open, exposing Commander Vane's command console.\n")
    sections.append("  * Kael and the Drift Throne coordinate an all-out offensive barrage targeting the command bunker.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael (Speed 11 -> 5 AP, Momentum Crit): Enters Node 05. Spends 3 AP on `[Four-Fold Trench Execution]`. Spends 2 AP on `[Tectonic Breaker]`.\n")
    sections.append("  * Hwaran: Calls in `[Drift Throne Spinal Kinetic Barrage]` (3 AP).\n")
    sections.append("- **Step 3: Unopposed Stagger Punishment Rotation**:\n")
    sections.append("  * Kael's `[Four-Fold Trench Execution]`: Rips through the bunker interior for **960 Heavy Weight damage** (Fatal 2.0x proc!)!\n")
    sections.append("  * Kael's `[Tectonic Breaker]`: Crushes the primary power conduit for **420 Shatter damage**!\n")
    sections.append("  * Drift Throne Spinal Barrage: High-explosive shells obliterate the Aegis generator housing for **440 Blast damage**!\n")
    sections.append("  * **TOTAL BURST DAMAGE: 1,820 DAMAGE!**\n")
    sections.append("- **Step 4: SECOND STAGGER THRESHOLD (1,920 HP) COMPLETELY SKIPPED!**:\n")
    sections.append("  * Fortress HP plunges from 2,400 down to **580/4,800 HP**! Aegis Shield generator completely destroyed (0/1,500 HP)!\n")
    sections.append("  * **Phase 2 Emergency Activation Triggered!**\n")
    sections.append("- **Step 5: Turn End State**:\n")
    sections.append("  * Total Fortress HP: 2,400 -> **580/4,800** (Bunker HP: **580/2,100** | Shield: **DESTROYED**).\n")
    sections.append("  * Posture: **48/340**.\n\n")
    sections.append('---\n\n')
    
    # Turn 05 HUD
    t5_hud = make_box("TACTICAL STAGE HUD: ARC 01 - BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 - LAST STAND & THE DRIFT KING'S CLEAVER]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[RAMPS] [SCOUT] [BERM]  [KILL]  [FORT]  [C-WALK][WALL]  [SUMP]  [VENT]  [THRONE]",
        "                                [KAEL]  [VANE]  [HWARAN]                [HELM]",
        "---",
        "- Node 05: Kael (Relic Overdrive: WRATH OF THE HORIZON SOVEREIGN)",
        "- Node 06: Commander Vane (Last Stand: Overheated Exoskeleton Core Overload)",
        "- Node 07: Hwaran (Covering Catwalks with Concentrated Suppressing Fire)",
        "- Node 10: Drift Throne (Spinal Battery Targeting Blast Gate Hinges)",
        "---",
        "- Kael (Drift King): Spd 9 -> 5 AP [OVERDRIVE] | HP 4,200/4,200 | SP 50/50 [RESOLVE]",
        "- Vane (Commander) : Spd 3 -> 1 AP             | HP 580/2,100   | Posture 24/340 [OVERHEATING]",
        "- Total Fortress   : HP 580/4,800 [EXOSKELETON BURST DEFLECTED / VANE DISARMED]"
    ])
    sections.append(wrap_box(t5_hud))
    
    sections.append("### Turn 05 Action Resolution Log (Phase 2 Escalation: Fortress Last Stand & Horizon Cleaver)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Commander Vane steps from the burning bunker, his hydraulic exoskeleton venting superheated steam as he primes an emergency core self-destruct!\n")
    sections.append("  * Boss Special Skill: `[Bunker Overdrive: Core Detonation]` (Thermal Kinetic Cataclysm, 3 Coins).\n")
    sections.append("  * Kael activates Relic Overdrive: `[WRATH OF THE HORIZON SOVEREIGN — MAXIMUM]` (Cost: 3 AP, 30 SP).\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael (Speed 9 -> 5 AP [Overdrive]): Steps straight onto Vane's command parapet at Node 05, raising the Obsidian Cleaver in both hands.\n")
    sections.append("  * Hwaran: Anchors suppression line at Node 07.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 05 to 06)**: Vane discharges `[Bunker Overdrive: Core Detonation]` (Base 22 + 3 Coins = 33 Power, Area Heat/Kinetic).\n")
    sections.append("    * Kael clashes with `[WRATH OF THE HORIZON SOVEREIGN — MAXIMUM]` (Base 29 + 3 Coins Heads = 50 Power, Seismic Execution).\n")
    sections.append("    * **Clash Outcome**: KAEL OVERWHELMING RELIC CLASH WIN (50 vs 33)!\n")
    sections.append("    * Kael's cleaver splits the exoskeleton's overheating capacitor block clean off Vane's shoulders (`[P3: Parry/Protection]`).\n")
    sections.append("    * The thermal detonation vents harmlessly upward into the overcast sky; Kael's glass arm drives Vane into the concrete deck!\n")
    sections.append('    * Kael\'s gravelly voice cuts through the smoke: *"The gate was meant to swing both ways, Commander. Stand down."*\n')
    sections.append("    * The fortress defenses fall silent! Zero caravan casualties taken!\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Total Fortress HP: **580/4,800** | Posture: **24/340 [OVERHEATING]**.\n")
    sections.append("  * Kael Composure: 50/50 SP.\n\n")
    sections.append('---\n\n')
    
    # Turn 06 HUD
    t6_hud = make_box("TACTICAL STAGE HUD: ARC 01 - BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 - GATE BREACH & DEPARTURE INTO THE DESOLATE]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[RAMPS] [SCOUT] [BERM]  [KILL]  [FORT]  [C-WALK][WALL]  [GATE]  [DESOL] [THRONE]",
        "                                        [KAEL]  [VANE]  [OPEN]  [A-LEY] [CRUISE]",
        "---",
        "- Node 08: Blast Gate V Hydraulic Portcullis (SEVERED & HOISTED WIDE)",
        "- Node 09: Boundary Waystation 01 (Ingress into The Desolate OPEN)",
        "- Node 10: The Drift Throne (142.5m Cruiser Rolling Outward at 45 km/h)",
        "---",
        "- Kael Status: Zero Damage Taken | Composure 50/50 SP (Unshakable Resolve)",
        "- Expedition Status: GATE BREACHED | Waystation 01 Unlocked"
    ])
    sections.append(wrap_box(t6_hud))
    
    sections.append("### Turn 06 Action Resolution Log (Fortress Capitulation & Gate Hoisted)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Hostile intent drops to zero. Posture reaches **0/340 [FORTRESS CAPITULATION]**.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael steps off the parapet, planting the cleaver into the gatehouse winch control.\n")
    sections.append("- **Step 3: Breakthrough & Capitulation**:\n")
    sections.append("  * Vane slumps against the shattered sandbags, coughing up gray dust, his mechanical exoskeleton stripped of power.\n")
    sections.append('  * *"You won\'t survive out there, Kael,"* Vane whispers, his eyes tracing the colossal silhouette of the mobile cruiser. *"The glass storms... the singing sand... it eats iron."*\n')
    sections.append('  * Kael turns his gaze toward the endless western horizon, where the white salt flats meet the pale red sky:\n')
    sections.append('    > *"Iron was made to be tested, Commander. If we die, the sand will keep our bones. But we will die moving forward."*\n')
    sections.append("  * Deals **580 Decisive Subjugation**! Fortress HP drops to 0!\n")
    sections.append("- **Step 4: Operational Artifact Extraction & Caravan Passage**:\n")
    sections.append("  * **Tactical Requisition Acquired**: `[Overland Module: Fortress Pneumatics]` (Grants +25% Ram Power to the Drift Throne and reinforces forward blast doors).\n")
    sections.append("  * **Overland Passage**: The cyclopean hydraulic rams of the Drift Throne hook into the severed portcullis chains, tearing Blast Gate V open with a thunderous roar. The 142.5-meter cruiser rolls through the threshold, its caterpillar tracks grinding onto the virgin glass of **The Desolate**.\n")
    sections.append("  * **Casualties**: Zero Caravan Damage Taken. Kael HP 4,200/4,200. Composure 50/50 SP.\n\n")
    sections.append('---\n\n')
    
    # Chapter VI: The Overland Breakthrough & Caravan Reorganization
    sections.append("## Chapter VI: The Overland Breakthrough & Caravan Reorganization\n\n")
    sections.append("As the colossal rear treads of the Drift Throne crossed the threshold of Blast Gate V, a profound silence descended upon the caravan. The suffocating smog of Somnarak—the bitter, sulfurous haze that had choked generations of citizens—fell away behind them like a dirty shroud. Ahead stretched the limitless expanse of **The Desolate (황야)**, bathed in the pale amber glow of an unpolluted sky.\n\n")
    sections.append("Aboard the command bridge, Master Wright Gwan hammered a brass rivet into the throttle linkage, wiping oil from his brow. Below in the galley, the Hearthkeepers set down their emergency fire blankets and lit the coal brazier, preparing warm broth for the forward scout crews. Across the four mobile flank-rigs, nomadic banners—the twin-headed hawk of the Dunewalkers and the iron anvil of the Ash Clan—snapped fiercely in the dry desert wind.\n\n")
    sections.append('"All four caterpillar bogies operating at nominal torque," Gwan shouted over the roar of the transmission gears. "Acoustic ley-sensors have locked onto the subterranean fault line running west-southwest. Commander, we have positive acoustic ground-traction!"\n\n')
    sections.append('Kael walked back into the bridge, his trench-cleaver sheathed across his shoulders. He pulled a tin flask from his duster, took a slow drink of distilled water, and looked out across the navigation table where Chief Ley-Seer Sora was tracing a copper stylus across a chart of vitrified waystations.\n\n')
    sections.append('"First relay point?" Kael asked.\n\n')
    sections.append('"Waystation 01: Exile\'s Rest, twenty-five kilometers ahead," Sora answered, her blind, bandaged eyes turned toward the glass window. "The sand is singing, Kael. Low and deep. It knows we have left the wall."\n\n')
    sections.append('---\n\n')
    
    # Chapter VII: Operational Requisition Harvest & Waystation Ingress
    sections.append("## Chapter VII: Operational Requisition Harvest & Waystation Ingress\n\n")
    sections.append("The caravan crossed the first twenty-five kilometers in three hours of steady, uninterrupted cruising, leaving deep, twin-track trenches cut into the alkali flats.\n\n")
    
    reward_box = make_box("OVERLAND REQUISITION HARVEST: ARC 01", [
        "ACQUIRED SALVAGE     : Fortress Hydraulic Shoring Rams & Kinetic Shells",
        "UPGRADE DESIGNATION  : [Overland Module: Fortress Pneumatics]",
        "CARAVAN SPEED STATUS : Cruising at 45 km/h across Alkali Flatlands",
        "---",
        "FLAGSHIP SYSTEM ENHANCEMENTS:",
        "1. Reinforced Prow   : Prow ramming attacks gain +30% kinetic stagger",
        "                     damage against armored obstacles and barricades.",
        "2. Counter-Battery   : Forward marksmen gain +2 Range Band coverage",
        "                     when engaging stationary fortifications.",
        "3. Ley-Traction Grip : Sand drift penalty reduced by 25% across salt flats.",
        "---",
        "NEXT TARGET WAYSTATION:",
        "- Waystation 02: Salt Basin Outpost (120 km) — Ingress to Sea of Glass"
    ])
    sections.append(wrap_box(reward_box))
    
    sections.append("Kael stood at the observation cupola as the sun began to sink toward the jagged rim of the horizon. Behind them, Somnarak was already shrinking into a jagged smudge of gray chimneys and dying smoke. Ahead lay the endless Sea of Glass, where leviathans swam through the dunes.\n")
    
    return "".join(sections)

def build_arc_2():
    sections = []
    
    # Title & Subtitle
    sections.append("# Arc 2: The Desolate Crossing — Sea of Glass & Dune Whales (황야 횡단 — 유리의 바다)\n")
    sections.append("## The Horizon Caravan Chronicles — Planetary Overland Expedition (Year 4238, Month 2)\n\n")
    
    # Operational Attribute Table
    sections.append("| Operational Attribute | Specification Dossier |\n")
    sections.append("|---|---|\n")
    sections.append("| **Campaign Theater** | The Horizon Caravan (지평선대 — Jipyeongseondae) |\n")
    sections.append("| **Arc Designation** | Arc 2: The Desolate Crossing — Sea of Glass (유리의 바다) |\n")
    sections.append("| **Overland Sector** | Waystations 04 to 07 — Sea of Vitrified Glass (500 to 950 km) |\n")
    sections.append("| **Threat Rating** | UTS-3 (Titanic Subterranean Megafauna Encounter) |\n")
    sections.append("| **Deploying Flagship**| The Drift Throne (142.5m Mobile Heavy Sand Cruiser) |\n")
    sections.append("| **Caravan Command** | Supreme Commander Kael (The Drift King) & Wright Gwan |\n")
    sections.append("| **Primary Opponent** | The Titanic Glass Burrower (유리 바다의 포식자 — SECC-088) |\n")
    sections.append("| **Operational Yield** | Vitrified Chitin Plating & Sonic Harpoon Calibration |\n\n")
    
    # Master Dossier Box
    dossier = make_box("EXPEDITION DOSSIER: ARC 2 - THE SEA OF GLASS", [
        "OPERATION NAME     : Arc 2 - Crossing the Sea of Glass",
        "PRIMARY THEATER    : Waystations 04 to 07 - The Vitrified Expanse",
        "DISTANCE TRAVERSED : 500 km to 950 km from Somnarak",
        "PRIMARY ADVERSARY  : The Titanic Glass Burrower (SECC-088 Leviathan)",
        "---",
        "ADVERSARY PROFILE (TITANIC GLASS BURROWER):",
        "- Total Health (HP): 5,400 HP | Posture Pool: 360/360",
        "- Stagger 1 Proc   : 60% Posture Strain (216 Posture) / Mandible Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Leviathan Pacification)",
        "- Resistances      : Weight 2.0x (Fatal), Grudge 1.5x, Void 0.5x, Lament 0.5x",
        "---",
        "TARGETABLE COMBAT ANCHORS:",
        "1. Burrow Mandibles: 1,400 HP | Posture 280/280 (Crushing vitreous shears)",
        "2. Chitin Carapace : 1,800 HP | Posture 320/320 (Vitrified glass armor plates)",
        "3. Siphon Heart    : 2,200 HP | Posture 360/360 (Acoustic resonance bladder)"
    ])
    sections.append(wrap_box(dossier))
    
    # Epigraph Quote
    sections.append('> *"Out here, the sand is not stone powdered by water. It is glass shattered by thunder and baked by five thousand years of sun. And beneath that glass swims something that regards our cruiser not as a machine, but as an intruder in its feeding trench."*\n')
    sections.append('> — Master Wright Gwan, adjusting the starboard harpoon rig\n\n')
    sections.append('---\n\n')
    
    # Chapter I
    sections.append("## Chapter I: The Vitrified Expanse & The Singing Dunes\n\n")
    sections.append("By the second month of Year 4238, the red alkali clay of the borderlands had surrendered completely to an endless, shimmering wilderness: **The Sea of Vitrified Glass (유리의 바다)**. Spanning from Waystation 04 to Waystation 07 (Kilometer 500 to 950), the terrain consisted of vast dunes composed not of soft quartz sand, but of microscopic shards of greenish volcanic glass that ground together with a piercing, musical chime whenever the desert gales swept across the ridges.\n\n")
    sections.append("Under the midday sun, the vitrified plain mirrored the pale sky with blinding, merciless intensity. Surface temperatures exceeded fifty-five degrees Celsius. The Drift Throne's massive caterpillar tracks kicked up glittering rooster-tails of pulverized glass that hissed against the hull's armored skirting like supersonic buckshot. To prevent catastrophic wear on the track pins, Wright Gwan's crews worked in rotating four-hour shifts, spraying pressurized graphite lubricant directly into the bogie assemblies.\n\n")
    sections.append('"Seismic transducers are picking up abnormal acoustic harmonics from the starboard trench," Chief Ley-Seer Sora called out from the observation cupola, her hand resting on the vibrating brass housing of the theodolite. "Frequency matches a UTS-3 apex burrower. It is tracking our engine pulse. Speed: sixty knots. Depth: thirty meters beneath the glass."\n\n')
    sections.append('Kael leaned over the helm console, squinting through the heat-shimmer on the forward dunes. "Gwan, spool up the acoustic harm-quenchers. Hwaran, ready the harpoon batteries. We have company."\n\n')
    sections.append('---\n\n')
    
    # Chapter II
    sections.append("## Chapter II: The Leviathan of the Deep Sand\n\n")
    sections.append("Three hundred meters off the starboard bow, the glass dunes erupted in a monumental geyser of green crystal sand. Rising eighty meters into the blinding sky was **The Titanic Glass Burrower (SECC-088)**.\n\n")
    sections.append("The leviathan was over ninety meters in length, its serpentine body armored in overlapping plates of vitrified silicate chitin that deflected direct sunlight like polished obsidian mirrors. In place of a face, it possessed three concentric rings of **Burrowing Mandibles**—serrated shearing blades composed of crystallized diamond-glass capable of grinding solid basalt boulders into silt. At its throat hummed the **Resonant Siphon Heart**, a bioluminescent organ that drank subterranean acoustic vibrations and expelled supersonic pressure waves through gill-like vents along its flanks.\n\n")
    sections.append('"It\'s an acoustic feeder!" Hwaran yelled, strapping herself into the mount of the dorsal harpoon deck. "Our ley-drive is broadcasting a five-hundred-hertz pulse into the bedrock. It thinks the Drift Throne is a rival sovereign invading its spawning trough!"\n\n')
    sections.append('The titan gave a deafening, sub-bass roar that shattered the panoramic observation windows of the outer deckhouses. It banked sharply across the dune ridge, descending into a supersonic breach dive aimed directly amidships at the crawler\'s exposed caterpillar drives.\n\n')
    sections.append('---\n\n')
    
    # Chapter III
    sections.append("## Chapter III: The Harpooner's Vow\n\n")
    sections.append("Kael vaulted onto the starboard catwalk, his duster whipping violently in the slipstream. He pulled the manual release pin on the **Acoustic Trench Harpoon**, an eight-hundred-pound tungsten spear connected to the cruiser's main winch drum by a two-inch braided steel cable.\n\n")
    sections.append('"We do not run from the desert!" Kael roared, his voice ringing over the scream of the tracks and the grinding glass. "In the city, they taught us to hide behind walls when monsters came! Out here, the monster learns that the caravan carries teeth! Wright Gwan—hard to starboard! Catch its dive on our armored prow!"\n\n')
    sections.append('"Starboard thrusters full forward!" Gwan roared back through the speaking tube, slamming the dual diesel pneumatic regulators. "Brace for impact!"\n\n')
    sections.append('The 142.5-meter mobile cruiser heaved violently onto its side bogies, pivoting forty-five degrees to meet the charging leviathan head-on. The battle for the Sea of Glass had begun.\n\n')
    sections.append('---\n\n')
    
    # Chapter IV
    sections.append("## Chapter IV: Overland Arena Topology & Combat Engagement Parameters\n\n")
    sections.append("Sora projected the overland tactical land grid across the bridge holographic table:\n\n")
    
    grid_box = make_box("TACTICAL ARENA TOPOLOGY: SEA OF GLASS DUNE CREST (-800M EXT)", [
        "[STAGE NODES 01 TO 10 - STARBOARD CATWALK TO LEVIATHAN BREACH]",
        "[N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "---",
        "- Node 01: Drift Throne Starboard Catwalk (Kael Vanguard Harpoon Station)",
        "- Node 02: Dorsal Gun Deck (Hwaran Rapid Harpoon Battery)",
        "- Node 03: Armored Sand-Skimmer Prow (Heavy Deflection Ram)",
        "- Node 04: The Vitrified Breach Slope (Glass Silt Avalanche Zone)",
        "- Node 05: The Glass Burrower Snout (Crushing Mandibles & Intake)",
        "- Node 06: Resonant Acoustic Flank (Vitrified Chitin Carapace Plates)",
        "- Node 07: Sub-Surface Trench (Burrower Siphon Heart Resonance Pool)",
        "- Node 08: Deep Dune Abyss (Subterranean Acoustic Wake)",
        "- Node 09: Vitrified Ridge Apex (High-Ground Ballistic Vantage)",
        "- Node 10: Drift Throne Spinal Heavy Winch (Tungsten Cable Anchor)"
    ])
    sections.append(wrap_box(grid_box))
    
    sections.append("The Glass Burrower utilized terrifying speed and mass to breach from beneath the sand, crushing targets between its **Burrowing Mandibles**. Kael's strategy required intercepting the beast's breach lunges with the heavy harpoon, shattering its mandibles to prevent it from submerging, cracking the **Chitin Carapace** with pneumatic rams, and driving a seismic lance into the **Siphon Heart**.\n\n")
    sections.append('---\n\n')
    
    # Chapter V: Combat Gauntlet (Turns 01 to 06)
    sections.append("## Chapter V: The Expedition Combat Gauntlet (Turns 01 to 06)\n\n")
    
    # Turn 01 HUD
    t1_hud = make_box("TACTICAL STAGE HUD: ARC 02 - BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 - SEA OF GLASS DUNE CREST]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[CATWALK][GUN-DK][PROW]  [SLOPE] [SNOUT] [FLANK] [TRENCH][ABYSS][RIDGE][WINCH]",
        "[KAEL]   [HWARAN]                [BURROW]                               [GWAN]",
        "---",
        "- Node 01: Drift Throne Starboard Catwalk (Kael Vanguard Band 1)",
        "- Node 02: Dorsal Gun Deck (Hwaran Rapid Harpoon Support)",
        "- Node 03: Armored Prow (Heavy Kinetic Deflection Shield)",
        "- Node 04: Vitrified Sand Slope (Silt Avalanche Hazard)",
        "- Node 05: The Glass Burrower (Crushing Mandibles & Siphon Heart)",
        "- Node 06: Resonant Flank (Heavy Vitrified Chitin Armor)",
        "- Node 10: Drift Throne Heavy Winch (Master Wright Gwan)",
        "---",
        "- Kael (Drift King): Spd 6 -> 3 AP | HP 4,200/4,200 | SP 50/50 | Posture 160/160",
        "- Hwaran (Guide)   : Spd 7 -> 4 AP | HP 2,800/2,800 | SP 45/45 | Posture 120/120",
        "- Burrower Core    : Spd 5 -> 3 AP | HP 2,200/2,200 | Posture 360/360 [BREACHING]",
        "- Mandibles        : Spd 7 -> 4 AP | HP 1,400/1,400 | Posture 280/280 [CRUSHING]",
        "- Chitin Carapace  : Spd 3 -> 1 AP | HP 1,800/1,800 | Posture 320/320 [VITRIFIED]"
    ])
    sections.append(wrap_box(t1_hud))
    
    sections.append("### Turn 01 Action Resolution Log (Intercepting the Breach Lunge)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Kael initializes `[Seismic Harpoon Stance]`: Grants +4 Protection and massive stagger resistance against colossal impacts.\n")
    sections.append("  * Hwaran prepares `[Acoustic Cable Tether]`: Links the dorsal winch drum to the heavy harpoon.\n")
    sections.append("  * The Glass Burrower emerges with `[Subterranean Supersonic Breach]`: Increases clash power by +6 during breach turns.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael (Speed 6 -> 3 AP): Holds Node 01. Spends 2 AP on `[Trench-Cleaver: Kinetic Intercept]`. Holds 1 AP in Guard.\n")
    sections.append("  * Hwaran (Speed 7 -> 4 AP): Holds Node 02. Spends 2 AP on `[Harpoon Volley]`. Spends 2 AP on `[Acoustic Tracking Flare]`.\n")
    sections.append("  * The Glass Burrower (Speed 7 -> 4 AP): Surges from Node 05 to Node 01. Spends 2 AP on `[Vitreous Mandible Shear]`. Spends 2 AP on `[Glass Silt Geyser]`.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 01 to 05)**: The Glass Burrower lunges with `[Vitreous Mandible Shear]` (Base 19 + 2 Coins = 29 Power, Piercing Weight).\n")
    sections.append("    * Kael intercepts with `[Trench-Cleaver: Kinetic Intercept]` (Base 22 + 2 Coins = 34 Power, Obsidian Heavy Blade).\n")
    sections.append("    * **Clash Outcome**: Kael WINS THE CLASH OVERWHELMINGLY (34 vs 29)!\n")
    sections.append("    * Kael drives the broad flat of the cleaver between the beast's outer mandibles, levering the crushing jaws apart with his glass arm (`[P3: Parry/Protection]`).\n")
    sections.append("    * Seismic tremor reflects **280 kinetic tremor damage** into the jaw hinges, inflicting +58 Posture Strain!\n")
    sections.append("  * **Clash 2 (Node 02 to 05)**: Hwaran's `[Harpoon Volley]` drives two steel tethers directly into the creature's neck joint, anchoring it to the cruiser!\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Mandibles HP: 1,400 -> **1,120/1,400** | Posture: **222/280**.\n")
    sections.append("  * Total Leviathan HP: 5,400 -> **5,120/5,400** | Posture: **302/360**.\n")
    sections.append("  * Kael Composure: **100% (50/50 SP)**. Zero caravan damage taken.\n\n")
    sections.append('---\n\n')
    
    # Turn 02 HUD
    t2_hud = make_box("TACTICAL STAGE HUD: ARC 02 - BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 - MANDIBLES SHATTERED & TETHER LOCKED]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[CATWALK][GUN-DK][PROW]  [SLOPE] [SNOUT] [FLANK] [TRENCH][ABYSS][RIDGE][WINCH]",
        "         [KAEL]  [HWARAN]        [BURROW]                               [GWAN]",
        "---",
        "- Node 02: Kael (Advancing on Catwalk / Slicing Mandible Flexor)",
        "- Node 03: Hwaran (Dorsal Winch Engaging Hydraulic Cable Tension)",
        "- Node 05: The Glass Burrower (Mandibles Destroyed 0/1,400 HP)",
        "- Node 06: Drift Throne Prow Ram (Slamming into Flank Carapace)",
        "- Node 10: Heavy Winch (Master Wright Gwan Locking Cable Drum)",
        "---",
        "- Kael (Drift King): Spd 8 -> 4 AP [SURGE] | HP 4,200/4,200 | SP 50/50 | Posture 160/160",
        "- Hwaran (Guide)   : Spd 9 -> 5 AP         | HP 2,800/2,800 | SP 45/45 | Posture 120/120",
        "- Burrower Core    : Spd 3 -> 1 AP         | HP 2,200/2,200 | Posture 254/360",
        "- Mandibles        : DESTROYED (0/1,400 HP)| CRUSHING SHEAR PERMANENTLY LOST",
        "- Chitin Carapace  : Spd 3 -> 1 AP         | HP 1,460/1,800 | Posture 248/320"
    ])
    sections.append(wrap_box(t2_hud))
    
    sections.append("### Turn 02 Action Resolution Log (Part Destruction: Mandibles Shattered)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Kael activates `Tectonic Surge` (+2 Speed next turn -> Net Speed 8, 4 AP).\n")
    sections.append("  * The Burrower attempts `[Vitreous Sand Drill]` to dive beneath the dune and drag the cruiser with it.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael (Speed 8 -> 4 AP [Surge]): Steps to Node 02. Spends 3 AP on `[Obsidian Cleaver: Jaw Shatter]`. Holds 1 AP in Guard.\n")
    sections.append("  * Hwaran (Speed 9 -> 5 AP): Spends 3 AP on `[Hydraulic Winch Lock]`. Spends 2 AP on `[Explosive Harpoon Strike]`.\n")
    sections.append("  * Wright Gwan: Engages caterpillar reverse thrusters to create maximum cable tension.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 02 to 05)**: The Burrower channels `[Vitreous Sand Drill]` (Base 20 + 2 Coins = 28 Power, Area Weight).\n")
    sections.append("    * Kael clashes with `[Obsidian Cleaver: Jaw Shatter]` (Base 26 + 3 Coins Heads = 45 Power, Weight/Shatter).\n")
    sections.append("    * **Clash Outcome**: Kael WINS THE CLASH OVERWHELMINGLY (45 vs 28)!\n")
    sections.append("    * Kael leaps onto the creature's snout, driving the obsidian blade directly through the central diamond mandible joint!\n")
    sections.append("    * The high-frequency vibration shatters all three rings of diamond teeth into green glass shards!\n")
    sections.append("    * Deals **1,120 Critical Shatter damage** (Fatal 2.0x proc!)!\n")
    sections.append("    * **TARGETED PART DESTROYED**: The Crushing Mandibles are completely destroyed (**Mandibles HP: 0/1,400** credit)!\n")
    sections.append("    * **EFFECT**: Beast cannot submerge back into the sand; permanently loses 1 Speed Slot!\n")
    sections.append("  * **Chitin Carapace Damage**:\n")
    sections.append("    * Cable tension whips the beast against the armored prow for **340 Blunt damage**!\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Mandibles: **DESTROYED (0/1,400 HP)**.\n")
    sections.append("  * Chitin Carapace: 1,800 -> **1,460/1,800** | Posture: **248/320**.\n")
    sections.append("  * Total Leviathan HP: 5,120 -> **3,660/5,400** | Posture: **196/360 [MANDIBLES SHATTERED]**.\n")
    sections.append("  * Kael Composure: Stable (50/50 SP).\n\n")
    sections.append('---\n\n')
    
    # Turn 03 HUD
    t3_hud = make_box("TACTICAL STAGE HUD: ARC 02 - BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 - STAGGER THRESHOLD 1 & CARAPACE CRACK]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[CATWALK][GUN-DK][PROW]  [SLOPE] [SNOUT] [FLANK] [TRENCH][ABYSS][RIDGE][WINCH]",
        "                 [KAEL]  [HWARAN][BURROW]                               [GWAN]",
        "---",
        "- Node 03: Kael (Seismic Glass Arm Driving Spike into Carapace Seam)",
        "- Node 04: Hwaran (Pneumatic Ram Shattering Silicate Ribs)",
        "- Node 05: The Glass Burrower (STAGGER LEVEL 1 / DEFENSES COLLAPSED)",
        "- Node 10: Drift Throne Winch (Hauling Titan Onto Dune Surface)",
        "---",
        "- Kael (Drift King): Spd 8 -> 4 AP [SURGE] | HP 4,200/4,200 | SP 50/50 | Posture 160/160",
        "- Hwaran (Guide)   : Spd 8 -> 4 AP         | HP 2,800/2,800 | SP 45/45 | Posture 120/120",
        "- Burrower Core    : Spd 0 -> 0 AP         | HP 1,940/2,200 | Posture 134/360 [STAGGER LEVEL 1]",
        "- Chitin Carapace  : Spd 0 -> 0 AP         | HP 680/1,800   | Posture 94/320 [CRACKED]",
        "- Total Leviathan  : HP 2,620/5,400 [THRESHOLD BREACHED / TAKES 1.5X DAMAGE]"
    ])
    sections.append(wrap_box(t3_hud))
    
    sections.append("### Turn 03 Action Resolution Log (First Stagger Proc & Chitin Carapace Cracked)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Thrashing on the surface, the Burrower whips its massive body in `[Tail Flail of Vitrified Rock]`.\n")
    sections.append("  * Kael gains `Tectonic Surge` (+2 Speed -> Net Speed 8, 4 AP).\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael (Speed 8 -> 4 AP): Moves to Node 03. Spends 2 AP on `[Glass Fist: Bedrock Ram]`. Spends 2 AP on `[Cleaver Cleave]`.\n")
    sections.append("  * Hwaran (Speed 8 -> 4 AP): Advances to Node 04. Spends 2 AP on `[Pneumatic Spike]`.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 03 to 05)**: The Burrower sweeps with `[Tail Flail of Vitrified Rock]` (Base 18 + 2 Coins = 26 Power, Heavy Kinetic).\n")
    sections.append("    * Kael clashes with `[Glass Fist: Bedrock Ram]` (Base 23 + 2 Coins = 35 Power, Seismic Weight).\n")
    sections.append("    * **Clash Outcome**: Kael WINS THE CLASH (35 vs 26)!\n")
    sections.append("    * Kael's glass arm punches into the silicate carapace plate; the acoustic shockwave radiates through the titan's skeletal frame!\n")
    sections.append("    * Drone-assisted pneumatic spikes shatter the armor plating across its neck, exposing the pulsating azure Siphon Heart!\n")
    sections.append("    * Deals **780 Void/Shatter damage** and +114 Posture Strain!\n")
    sections.append("- **Step 4: STAGGER THRESHOLD 1 TRIGGERED!**:\n")
    sections.append("  * Total Leviathan HP crosses 70% threshold (3,780 HP), falling to **2,620/5,400 HP**; Posture crosses 60% strain line!\n")
    sections.append("  * **STAGGER LEVEL 1 ACTIVE!** The titan crashes onto the sand, its snout buried in the dust; defenses drop to zero; takes +50% damage across all incoming attacks!\n")
    sections.append("- **Step 5: Turn End State**:\n")
    sections.append("  * Total Leviathan HP: 3,660 -> **2,620/5,400 [THRESHOLD BREACHED: Below 3,780 HP!]**.\n")
    sections.append("  * Chitin Carapace: 1,460 -> **680/1,800** | Posture: **94/320 [CRACKED]**.\n")
    sections.append("  * Boss Posture: **134/360 [STAGGER LEVEL 1]**.\n")
    sections.append("  * Kael Status: Unbroken.\n\n")
    sections.append('---\n\n')
    
    # Turn 04 HUD
    t4_hud = make_box("TACTICAL STAGE HUD: ARC 02 - BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 - MAXIMUM BURST & PHASE 2 THRESHOLD SKIP]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[CATWALK][GUN-DK][PROW]  [SLOPE] [SNOUT] [FLANK] [TRENCH][ABYSS][RIDGE][WINCH]",
        "                         [KAEL]  [BURROW][HWARAN]                       [GWAN]",
        "---",
        "- Node 04: Kael (Four-Fold Cleaver Void Execution on Siphon Heart)",
        "- Node 05: The Glass Burrower (Immobilized / Acoustic Bladder Leaking Azure Fluid)",
        "- Node 06: Hwaran (Spinal Battery Focused Slag Barrage)",
        "- Node 10: Drift Throne Winch (Tensioning Steel Cables to Maximum Load)",
        "---",
        "- Kael (Drift King): Spd 11 -> 5 AP [BURST CRIT] | HP 4,200/4,200 | SP 50/50",
        "- Burrower Core    : Spd 0 -> 0 AP               | HP 640/2,200   | Posture 52/360",
        "- Chitin Carapace  : DESTROYED (0/1,800 HP)",
        "- Total Leviathan  : HP 640/5,400 [BURST DAMAGE 1,980! SECOND THRESHOLD SKIPPED]"
    ])
    sections.append(wrap_box(t4_hud))
    
    sections.append("### Turn 04 Action Resolution Log (Maximum Burst & Phase 2 Threshold Skip)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * The Glass Burrower lies helpless on the dune; the Siphon Heart in its throat pulses with frantic, bioluminescent flashes.\n")
    sections.append("  * Kael coordinates an all-out offensive barrage targeting the exposed resonance bladder.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael (Speed 11 -> 5 AP, Momentum Crit): Stands at Node 04. Spends 3 AP on `[Four-Fold Cleaver Execution]`. Spends 2 AP on `[Seismic Impact]`.\n")
    sections.append("  * Hwaran: Calls in `[Spinal Battery Focused Slag Barrage]` (3 AP).\n")
    sections.append("- **Step 3: Unopposed Stagger Punishment Rotation**:\n")
    sections.append("  * Kael's `[Four-Fold Cleaver Execution]`: Drives into the siphon bladder for **1,060 Heavy Weight damage** (Fatal 2.0x proc!)!\n")
    sections.append("  * Kael's `[Seismic Impact]`: Slices through the remaining armor plates for **460 Shatter damage**!\n")
    sections.append("  * Spinal Slag Barrage: Superheated iron rounds obliterate the carapace collar for **460 Fire/Blunt damage**!\n")
    sections.append("  * **TOTAL BURST DAMAGE: 1,980 DAMAGE!**\n")
    sections.append("- **Step 4: SECOND STAGGER THRESHOLD (2,160 HP) COMPLETELY SKIPPED!**:\n")
    sections.append("  * Leviathan HP plunges from 2,620 down to **640/5,400 HP**! Chitin Carapace completely destroyed (0/1,800 HP)!\n")
    sections.append("  * **Phase 2 Emergency Activation Triggered!**\n")
    sections.append("- **Step 5: Turn End State**:\n")
    sections.append("  * Total Leviathan HP: 2,620 -> **640/5,400** (Heart HP: **640/2,200** | Armor: **DESTROYED**).\n")
    sections.append("  * Posture: **52/360**.\n\n")
    sections.append('---\n\n')
    
    # Turn 05 HUD
    t5_hud = make_box("TACTICAL STAGE HUD: ARC 02 - BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 - ACOUSTIC TSUNAMI & THE OVERDRIVE PACIFICATION]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[CATWALK][GUN-DK][PROW]  [SLOPE] [SNOUT] [FLANK] [TRENCH][ABYSS][RIDGE][WINCH]",
        "                                 [KAEL]  [BURROW][HWARAN]               [GWAN]",
        "---",
        "- Node 05: Kael (Relic Overdrive: HARMONIC CLEAVER OF THE HORIZON)",
        "- Node 06: The Glass Burrower (Last Stand: Supersonic Acoustic Shockwave)",
        "- Node 07: Hwaran (Deploying Acoustic Quenching Pylons)",
        "- Node 10: Drift Throne Harm-Quenchers (Absorbing Residual Sonic Feedback)",
        "---",
        "- Kael (Drift King): Spd 9 -> 5 AP [OVERDRIVE] | HP 4,200/4,200 | SP 50/50 [RESOLVE]",
        "- Burrower Core    : Spd 3 -> 1 AP             | HP 640/2,200   | Posture 26/360 [EXHAUSTED]",
        "- Total Leviathan  : HP 640/5,400 [ACOUSTIC SHOCKWAVE QUENCHED / TITAN SUBDUED]"
    ])
    sections.append(wrap_box(t5_hud))
    
    sections.append("### Turn 05 Action Resolution Log (Phase 2 Escalation: Acoustic Shockwave & Horizon Pacification)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * The titan thrashes in blind panic; its Siphon Heart swells to double its volume, preparing a supersonic shockwave to pulverize the crawler!\n")
    sections.append("  * Boss Special Skill: `[Supersonic Acoustic Shockwave]` (Seismic Siphon Cataclysm, 3 Coins).\n")
    sections.append("  * Kael activates Relic Overdrive: `[HARMONIC CLEAVER OF THE HORIZON — MAXIMUM]` (Cost: 3 AP, 30 SP).\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael (Speed 9 -> 5 AP [Overdrive]): Steps straight onto the creature's exposed collar at Node 05, raising his glass arm high.\n")
    sections.append("  * Hwaran: Deploys mobile acoustic quenching pylons at Node 07.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 05 to 06)**: The Burrower discharges `[Supersonic Acoustic Shockwave]` (Base 23 + 3 Coins = 34 Power, Area Acoustic/Weight).\n")
    sections.append("    * Kael clashes with `[HARMONIC CLEAVER OF THE HORIZON — MAXIMUM]` (Base 30 + 3 Coins Heads = 51 Power, Seismic Harmony).\n")
    sections.append("    * **Clash Outcome**: KAEL OVERWHELMING RELIC CLASH WIN (51 vs 34)!\n")
    sections.append("    * Kael's glass arm resonates at the exact inverse harmonic frequency of the titan's siphon bladder (`[P3: Parry/Protection]`).\n")
    sections.append("    * The supersonic wave collapses into a low, gentle acoustic hum; Kael drives the hilt of the cleaver into the bladder's nerve center!\n")
    sections.append('    * Kael speaks into the sand: *"Sleep, beast of the glass. The caravan does not claim your grave; we only claim our road."*\n')
    sections.append("    * The creature's thrashing ceases, its massive head resting calmly upon the dune! Zero caravan casualties!\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Total Leviathan HP: **640/5,400** | Posture: **26/360 [EXHAUSTED]**.\n")
    sections.append("  * Kael Composure: 50/50 SP.\n\n")
    sections.append('---\n\n')
    
    # Turn 06 HUD
    t6_hud = make_box("TACTICAL STAGE HUD: ARC 02 - BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 - PACIFICATION & SEA OF GLASS HARVEST]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[CATWALK][GUN-DK][PROW]  [SLOPE] [SNOUT] [TITAN] [WAYST] [DUNES] [CRUISE][THRONE]",
        "                                         [KAEL]  [PACIF] [WAY-07][ROLL]  [CRUISE]",
        "---",
        "- Node 06: The Titanic Glass Burrower (PACIFIED & SUBMERGING PEACEFULLY)",
        "- Node 07: Waystation 07: Glass Caldera (Overland Ingress SECURED)",
        "- Node 10: The Drift Throne (Cruising West at 52 km/h across Sea of Glass)",
        "---",
        "- Kael Status: Zero Damage Taken | Composure 50/50 SP (Tranquil Authority)",
        "- Expedition Status: SEA OF GLASS TRAVERSED | Waystations 04-07 Secured"
    ])
    sections.append(wrap_box(t6_hud))
    
    sections.append("### Turn 06 Action Resolution Log (Leviathan Pacification & Harvest)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Hostile intent drops to zero. Posture reaches **0/360 [LEVIATHAN PACIFICATION]**.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael uncouples the heavy harpoon cables, releasing the giant back into the desert depths.\n")
    sections.append("- **Step 3: Pacification & Desert Harmony**:\n")
    sections.append("  * The Glass Burrower exhales a deep plume of fine white glass dust, turns slowly, and slides back beneath the dunes with majestic, fluid grace.\n")
    sections.append('  * Wright Gwan wipes cold sweat from his goggles: *"By the old gods... I thought the tracks were gone for good."*\n')
    sections.append('  * Kael looks down at a shed plate of vitrified silicate chitin left on the catwalk—half a ton of indestructible diamond-glass armor:\n')
    sections.append('    > *"The desert does not yield to force, Gwan. It yields to those who know how to listen to its song."*\n')
    sections.append("  * Deals **640 Decisive Pacification**! Leviathan HP drops to 0!\n")
    sections.append("- **Step 4: Operational Artifact Extraction & Caravan Ingress**:\n")
    sections.append("  * **Tactical Requisition Acquired**: `[Overland Module: Vitrified Chitin Plating]` (Grants +35% Resistance against sandstorms and thermal friction; upgrades crawler skirting).\n")
    sections.append("  * **Overland Passage**: The Drift Throne clears the dune crest, rolling into the sheltered basin of **Waystation 07: Glass Caldera (Kilometer 950)**, the gateway to the volcanic mountain ranges of Cheonbulok.\n")
    sections.append("  * **Casualties**: Zero Caravan Damage Taken. Kael HP 4,200/4,200. Composure 50/50 SP.\n\n")
    sections.append('---\n\n')
    
    # Chapter VI: The Overland Breakthrough & Caravan Reorganization
    sections.append("## Chapter VI: The Overland Breakthrough & Caravan Reorganization\n\n")
    sections.append("Within the volcanic caldera of Waystation 07, the mobile fortress dropped anchor for twenty-four hours of maintenance and replenishment. The crew gathered around the central maintenance bay as Wright Gwan and the Ash Iron smiths hoisted the shed leviathan chitin plates into the crawler's hydraulic presses. The green glass armor was cut into reinforced panels and welded along the crawler's forward bogies, replacing the dented steel plates with material that could withstand volcanic heat.\n\n")
    sections.append("In the observation cupola, Chief Ley-Seer Sora poured boiling chicory tea into metal cups for Kael and Hwaran. Outside, the night sky over the Sea of Glass was a tapestry of cold, unblinking stars, untouched by the smoke of Somnarak.\n\n")
    sections.append('"Five hundred kilometers behind us," Hwaran murmured, holding the warm tin between her soot-stained palms. "Another four hundred and fifty to the Ash Citadel of Cheonbulok. My former masters will have received word of our approach by now."\n\n')
    sections.append('"Let them prepare their arena," Kael answered, his eyes fixed on the distant red glow of the caldera ridge to the west. "The Caravan does not come to conquer Cheonbulok. We come to light a furnace that does not consume its children."\n\n')
    sections.append('---\n\n')
    
    # Chapter VII: Operational Requisition Harvest & Waystation Ingress
    sections.append("## Chapter VII: Operational Requisition Harvest & Waystation Ingress\n\n")
    sections.append("With the crawler's skirting reinforced and the acoustic probes recalibrated to volcanic basalt frequencies, the caravan prepared for the ascent into the Ash Ridge:\n\n")
    
    reward_box = make_box("OVERLAND REQUISITION HARVEST: ARC 02", [
        "ACQUIRED SALVAGE     : 4.5 Metric Tons of Vitrified Silicate Chitin",
        "UPGRADE DESIGNATION  : [Overland Module: Vitrified Chitin Plating]",
        "CARAVAN SPEED STATUS : Cruising at 52 km/h across Caldera Slopes",
        "---",
        "FLAGSHIP SYSTEM ENHANCEMENTS:",
        "1. Vitrified Skirting: Track assemblies gain 100% immunity to abrasive",
        "                     glass wear and +35% thermal resistance.",
        "2. Resonant Harpoon  : Starboard harpoon battery gains acoustic tracking,",
        "                     increasing critical hit chance against burrowers by +30%.",
        "3. Siphon Tuning     : Subterranean acoustic fuel recovery increased by +15%.",
        "---",
        "NEXT TARGET WAYSTATION:",
        "- Waystation 08: Caldera Causeway (1,100 km) — Ingress to Cheonbulok"
    ])
    sections.append(wrap_box(reward_box))
    
    sections.append("The caterpillar engines roared to life, their exhaust plumes glowing faint blue against the desert dusk. The Drift Throne crested the caldera rim, steering toward the towering volcanic chimneys of Cheonbulok.\n")
    
    return "".join(sections)

if __name__ == "__main__":
    content_1 = build_arc_1()
    with open("SOMNARAK-WORLD/Jipyeongseondae/Arc_1_Departure.md", "w", encoding="utf-8") as f:
        f.write(content_1)
    print("Arc 1 expanded successfully!")
    
    content_2 = build_arc_2()
    with open("SOMNARAK-WORLD/Jipyeongseondae/Arc_2_The_Desolate_Crossing.md", "w", encoding="utf-8") as f:
        f.write(content_2)
    print("Arc 2 expanded successfully!")
