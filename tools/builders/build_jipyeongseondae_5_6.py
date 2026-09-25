#!/usr/bin/env python3
"""
tools/build_jipyeongseondae_5_6.py
Generates the fully enriched, canonical chronicles for:
- Arc 5: The Return Journey — Sandstorm & Corsair Ambush (귀환로 — 모래폭풍과 해적단)
- Arc 6: The Mugeukji Attempt — Void Wall & Sovereign of the Horizon (무극지 진입 — 지평선의 군주)
"""

import os
import sys

sys.path.append(os.path.dirname(__file__))
from box_formatter import make_box

def wrap_box(b):
    return "```text\n" + b + "\n```\n\n"

def build_arc_5():
    sections = []
    
    # Title & Subtitle
    sections.append("# Arc 5: The Return — The Northern Sand Corridor (귀환 — 북부 모래 회랑)\n")
    sections.append("## The Horizon Caravan Chronicles — Planetary Overland Expedition (Year 4238, Months 6-7)\n\n")
    
    # Operational Attribute Table
    sections.append("| Operational Attribute | Specification Dossier |\n")
    sections.append("|---|---|\n")
    sections.append("| **Campaign Theater** | The Horizon Caravan (지평선대 — Jipyeongseondae) |\n")
    sections.append("| **Arc Designation** | Arc 5: The Return — The Northern Sand Corridor (북부 모래 회랑) |\n")
    sections.append("| **Overland Sector** | Waystations 12 to 15 — The Singing Dunes (1,850 to 2,400 km) |\n")
    sections.append("| **Threat Rating** | UTS-3 (Armored Corsair Armada & Dune Ambush) |\n")
    sections.append("| **Deploying Flagship**| The Drift Throne + 400-Soul Cheonbulok Refugee Convoy |\n")
    sections.append("| **Caravan Command** | Supreme Commander Kael (The Drift King) & Guide Hwaran |\n")
    sections.append("| **Primary Opponent** | Sand-Corsair Warlord Garek & Dune-Skimmer Marauders |\n")
    sections.append("| **Operational Yield** | Armored War-Rig Salvage & Safe Convoy Transit |\n\n")
    
    # Master Dossier Box
    dossier = make_box("EXPEDITION DOSSIER: ARC 5 - THE RETURN CROSSING", [
        "OPERATION NAME     : Arc 5 - Escorting the Cheonbulok Convoy",
        "PRIMARY THEATER    : The Desolate - Northern Sand Corridor (Km 1,850)",
        "DATE & EPOCH       : Year 4238, Months 6-7 (Return Transit to Somnarak)",
        "PRIMARY ADVERSARY  : Sand-Corsair Warlord Garek & Dune-Skimmer Marauders",
        "---",
        "ADVERSARY PROFILE (WARLORD GAREK'S HEAVY WAR-RIG):",
        "- Total Health (HP): 5,900 HP | Posture Pool: 380/380",
        "- Stagger 1 Proc   : 60% Posture Strain (228 Posture) / Cannon Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Marauder Route)",
        "- Resistances      : Weight 2.0x (Fatal), Grudge 1.5x, Lament 0.5x, Void 0.5x",
        "---",
        "TARGETABLE COMBAT ANCHORS:",
        "1. Rotary Cannons  : 1,500 HP | Posture 300/300 (High-speed kinetic suppression)",
        "2. Spiked Ram      : 1,800 HP | Posture 340/340 (Armored marauder chassis)",
        "3. Command Rig     : 2,600 HP | Posture 380/380 (Garek's armored cupola)"
    ])
    sections.append(wrap_box(dossier))
    
    # Epigraph Quote
    sections.append('> *"You think because you\'re driving four hundred helpless foundry rats, you\'re an easy meal? In the Desolate, prey doesn\'t carry fifty tons of obsidian. Turn your rigs around, Garek, or I\'ll bury your entire fleet in the sand."*\n')
    sections.append('> — Kael, confronting the Sand-Corsair fleet\n\n')
    sections.append('---\n\n')
    
    # Chapter I
    sections.append("## Chapter I: The Convoy of Four Hundred Souls & The Narrow Defile\n\n")
    sections.append("In the sixth month of Year 4238, the Drift Throne commenced its arduous return transit toward Somnarak, escorting a two-kilometer column of armored sand-trailers carrying the **four hundred Cheonbulok Ash Walker refugees**, along with crucial geothermal heat-crystals and sovereign metallurgical tooling. Having traversed the volcanic calderas, the convoy entered the treacherous labyrinth of the **Northern Sand Corridor (Kilometer 1,850)**.\n\n")
    sections.append("Here, towering sandstone ridges three hundred meters high pinched the desert road into a jagged, narrow defile barely eighty paces wide. The afternoon sun baked the canyon walls into glowing terracotta furnaces, and the dry northern gales kicked up howling dust storms that blinded optical sensors and choked radiator fans. With the refugee trailers tethered in single file behind the cruiser, maneuverability was severely restricted.\n\n")
    sections.append('"Acoustic echo indicates vehicle engines in the side ravines," Chief Ley-Seer Sora reported, her blindfold vibrating against her temples. "Multiple light combustion engines... twenty buggies at eight o\'clock, three tracked war-rigs closing from the ridge above. They have dropped caltrops across the exit."\n\n')
    sections.append('Kael leaned over the starboard wing of the bridge, binoculars pressed to his eyes. Through the swirling red dust, banners of black rawhide decorated with iron skulls fluttered from the dunes: the dreaded **Iron Dust Corsairs**.\n\n')
    sections.append('---\n\n')
    
    # Chapter II
    sections.append("## Chapter II: Warlord Garek & The Iron Dust War-Rig\n\n")
    sections.append("Leading the ambush was **Sand-Corsair Warlord Garek**, the terror of the outer trade routes. His flagship war-rig—a monstrous thirty-meter battle crawler constructed from scavenged municipal girders and plated with welded railway iron—roared down from the eastern ridge. Mounted atop its cupola was a twin 50mm **Rotary Autocannon Battery** that spewed thousands of depleted uranium rounds per minute, chewing up the sandstone walls in blinding showers of stone splinters.\n\n")
    sections.append("At the rig's prow jutted a massive **Spiked Harpoon Ram**, studded with hardened tungsten teeth designed to peel open armored trailers like tin cans. Behind Garek's rig, two dozen dune-skimmers swarmed like hornets, firing kinetic harpoons into the rear refugee carriages.\n\n")
    sections.append('"Kael!" Garek\'s voice crackled over the scavenged shortwave radio, dripping with sadistic mockery. "Word on the salt is the Council put a bounty on your head, and the foundry rats behind you are worth five hundred credits each in the Zone C fighting pits! Cut your engines, step off that steel barge, and I might let the children walk!"\n\n')
    sections.append('---\n\n')
    
    # Chapter III
    sections.append("## Chapter III: The Parley of Vultures and Kings\n\n")
    sections.append("Aboard the Drift Throne, frantic shouts echoed through the refugee trailers as mothers shielded their children behind sandbags. Kael did not raise his voice. He walked to the debarkation gangway, uncoupled his four-foot Obsidian Trench-Cleaver, and swung it onto his right shoulder.\n\n")
    sections.append('"Hwaran," Kael said quietly, his eyes cold and level through the dust storm. "Take the dorsal marksmen and suppress those buggies on the high ridge. Gwan, lock the crawler\'s rear caterpillar brakes. Drop the anchor spades."\n\n')
    sections.append('"Commander," Hwaran asked, checking the magazine of her steam repeater. "Do we offer terms?"\n\n')
    sections.append('"The desert offers only two terms, Guide," Kael answered, stepping out into the open sand directly in front of the advancing armada. "Turn around, or become roadbed."\n\n')
    sections.append('With a thunderous crash of gears, Garek\'s war-rig revved its supercharged diesel engines, exhaust plumes blackening the red canyon, and charged down the defile.\n\n')
    sections.append('---\n\n')
    
    # Chapter IV
    sections.append("## Chapter IV: Overland Arena Topology & Combat Engagement Parameters\n\n")
    sections.append("Sora mapped the tight canyon corridor across the tactical land HUD:\n\n")
    
    grid_box = make_box("TACTICAL ARENA TOPOLOGY: NORTHERN SAND CORRIDOR (KM 1,850)", [
        "[STAGE NODES 01 TO 10 - REFUGEE CONVOY TO CORSAIR WAR-RIG]",
        "[N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "---",
        "- Node 01: Refugee Trailer Column (400 Ash Walkers Under Anchor)",
        "- Node 02: Drift Throne Forward Ramps (Kael Vanguard Defensive Post)",
        "- Node 03: Narrow Sandstone Choke (Hwaran Suppressing Marksmen)",
        "- Node 04: The Caltrop Trench (Explosive Spikes & Dust Sump)",
        "- Node 05: Warlord Garek's War-Rig (Spiked Ram & Rotary Cannons)",
        "- Node 06: High Sandstone Rafters (Corsair Buggies Flank Skirmish)",
        "- Node 07: Eastern Scree Slope (Secondary Technical Ambush Rigs)",
        "- Node 08: Deep Gully Wash (Sandstorm Flash Flood Hazard)",
        "- Node 09: Defile Exit Portal (Pathway Back to Somnarak Outskirts)",
        "- Node 10: Drift Throne Dorsal Heavy Battery (Long-Range Spinal Gun)"
    ])
    sections.append(wrap_box(grid_box))
    
    sections.append("Warlord Garek relied upon high-speed kinetic shock, using the **Spiked Ram** to crush barricades while the **Rotary Cannons** pinned defenders. Kael's combat plan required deflecting the high-speed autocannon burst with his Han-glass arm, sundering the gun mounts, shattering the forward battering ram with a seismic cleave, and boarding the **Command Rig**.\n\n")
    sections.append('---\n\n')
    
    # Chapter V: Combat Gauntlet (Turns 01 to 06)
    sections.append("## Chapter V: The Expedition Combat Gauntlet (Turns 01 to 06)\n\n")
    
    # Turn 01 HUD
    t1_hud = make_box("TACTICAL STAGE HUD: ARC 05 - BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 - NORTHERN SAND CORRIDOR DEFILE]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[CONVOY][RAMPS] [CHOKE] [TRENCH][RIG]   [RAFTER][SLOPE] [GULLY] [EXIT]  [THRONE]",
        "[CIVIL] [KAEL]  [HWARAN]        [GAREK]                                 [GWAN]",
        "---",
        "- Node 01: Refugee Column / 400 Civilians Under Cover",
        "- Node 02: Kael (Vanguard Band 1 / Han-Glass Kinetic Intercept)",
        "- Node 03: Hwaran (Short Band 2 / Steam Repeater Flank Guard)",
        "- Node 04: Sandstone Choke Point (High Caltrop Density)",
        "- Node 05: Warlord Garek's War-Rig (Twin Rotary Autocannons)",
        "- Node 06: Corsair Dune-Skimmers (Flank Suppression Swarm)",
        "- Node 10: Drift Throne Spinal Battery (Master Wright Gwan)",
        "---",
        "- Kael (Drift King): Spd 6 -> 3 AP | HP 4,200/4,200 | SP 50/50 | Posture 160/160",
        "- Hwaran (Guide)   : Spd 7 -> 4 AP | HP 2,800/2,800 | SP 45/45 | Posture 120/120",
        "- Garek Core       : Spd 5 -> 3 AP | HP 2,600/2,600 | Posture 380/380 [CHARGING]",
        "- Rotary Cannons   : Spd 7 -> 4 AP | HP 1,500/1,500 | Posture 300/300 [SPINNING]",
        "- Spiked Ram       : Spd 3 -> 1 AP | HP 1,800/1,800 | Posture 340/340 [ARMORED]"
    ])
    sections.append(wrap_box(t1_hud))
    
    sections.append("### Turn 01 Action Resolution Log (Intercepting the Rotary Cannons)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Kael initializes `[Seismic Deflection Stance]`: Han-glass arm generates a high-density acoustic shield granting +4 Protection.\n")
    sections.append("  * Hwaran prepares `[High-Angle Steam Tracer]`: Suppresses the dune-skimmers along Node 06.\n")
    sections.append("  * Garek activates `[Corsair Frenzy]`: Increases kinetic fire rate by +25%.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael (Speed 6 -> 3 AP): Holds Node 02. Spends 2 AP on `[Trench-Cleaver: Ballistic Sweep]`. Holds 1 AP in Guard.\n")
    sections.append("  * Hwaran (Speed 7 -> 4 AP): Holds Node 03. Spends 2 AP on `[Flank Suppression Volley]`. Spends 2 AP on `[Smoke Canister]`.\n")
    sections.append("  * Garek (Speed 7 -> 4 AP): Charges from Node 05 to Node 03. Spends 2 AP on `[Twin Rotary Barrage]`. Spends 2 AP on `[Spiked Ram Rush]`.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 02 to 05)**: Garek fires `[Twin Rotary Barrage]` (Base 18 + 2 Coins = 28 Power, Rapid Kinetic/Pierce).\n")
    sections.append("    * Kael intercepts with `[Trench-Cleaver: Ballistic Sweep]` (Base 21 + 2 Coins = 33 Power, Obsidian Heavy Blade).\n")
    sections.append("    * **Clash Outcome**: Kael WINS THE CLASH OVERWHELMINGLY (33 vs 28)!\n")
    sections.append("    * Kael's cleaver spins in an impenetrable circle of dark obsidian; hundreds of heavy autocannon rounds ricochet violently into the canyon walls (`[P3: Parry/Protection]`).\n")
    sections.append("    * Reflected kinetic tremor inflicts **290 damage** back into the gun turrets, causing +56 Posture Strain!\n")
    sections.append("  * **Clash 2 (Node 03 to 06)**: Hwaran's `[Smoke Canister]` blinds the flank skimmers, causing four buggies to collide and roll into the gully!\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Rotary Cannons HP: 1,500 -> **1,210/1,500** | Posture: **244/300**.\n")
    sections.append("  * Total War-Rig HP: 5,900 -> **5,610/5,900** | Posture: **324/380**.\n")
    sections.append("  * Kael Composure: **100% (50/50 SP)**. Zero refugee casualties.\n\n")
    sections.append('---\n\n')
    
    # Turn 02 HUD
    t2_hud = make_box("TACTICAL STAGE HUD: ARC 05 - BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 - ROTARY CANNONS AMPUTATED & CLEAVER CRUSH]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[CONVOY][RAMPS] [CHOKE] [TRENCH][RIG]   [RAFTER][SLOPE] [GULLY] [EXIT]  [THRONE]",
        "        [HWARAN][KAEL]  [RAM]   [GAREK]                                 [GWAN]",
        "---",
        "- Node 02: Hwaran (Covering the Defile with Concentrated Sniper Fire)",
        "- Node 03: Kael (Advancing / Leaping onto War-Rig Hood to Sever Guns)",
        "- Node 05: Warlord Garek (Rotary Cannons Destroyed 0/1,500 HP)",
        "- Node 10: Drift Throne Heavy Ram (Closing the Gap to Back Kael)",
        "---",
        "- Kael (Drift King): Spd 8 -> 4 AP [SURGE] | HP 4,200/4,200 | SP 50/50 | Posture 160/160",
        "- Hwaran (Guide)   : Spd 9 -> 5 AP         | HP 2,800/2,800 | SP 45/45 | Posture 120/120",
        "- Garek Core       : Spd 3 -> 1 AP         | HP 2,600/2,600 | Posture 274/380",
        "- Rotary Cannons   : DESTROYED (0/1,500 HP)| HIGH-SPEED SUPPRESSION SILENCED",
        "- Spiked Ram       : Spd 3 -> 1 AP         | HP 1,460/1,800 | Posture 268/340"
    ])
    sections.append(wrap_box(t2_hud))
    
    sections.append("### Turn 02 Action Resolution Log (Part Destruction: Rotary Cannons Shattered)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Kael activates `Tectonic Momentum` (+2 Speed next turn -> Net Speed 8, 4 AP).\n")
    sections.append("  * Garek attempts `[Ram-Plow Full Throttle]` to flatten Kael and shatter the caravan drawbridge.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael (Speed 8 -> 4 AP [Surge]): Steps from Node 02 to Node 03. Spends 3 AP on `[Obsidian Cleaver: Turret Severance]`. Holds 1 AP in Guard.\n")
    sections.append("  * Hwaran (Speed 9 -> 5 AP): Spends 3 AP on `[Armor-Piercing Slag Shot]`. Spends 2 AP on `[Flank Suppression]`.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 03 to 05)**: Garek charges with `[Ram-Plow Full Throttle]` (Base 20 + 2 Coins = 28 Power, Heavy Weight/Ram).\n")
    sections.append("    * Kael clashes with `[Obsidian Cleaver: Turret Severance]` (Base 26 + 3 Coins Heads = 45 Power, Heavy Weight/Shatter).\n")
    sections.append("    * **Clash Outcome**: Kael WINS THE CLASH OVERWHELMINGLY (45 vs 28)!\n")
    sections.append("    * Kael vaults over the charging ram, landing squarely on the war-rig's armored hood; his cleaver slices through both rotary gun mounts like butter!\n")
    sections.append("    * The ammo magazines ignite, blasting the turrets fifty feet into the air in a spectacular explosion!\n")
    sections.append("    * Deals **1,210 Critical Shatter damage** (Weight 2.0x proc!)!\n")
    sections.append("    * **TARGETED PART DESTROYED**: The Rotary Autocannon Battery is completely destroyed (**Cannons HP: 0/1,500** credit)!\n")
    sections.append("    * **EFFECT**: Marauder suppression fire permanently silenced; boss permanently loses 1 Speed Slot!\n")
    sections.append("  * **Spiked Ram Damage**:\n")
    sections.append("    * Hwaran's slag shot punches through the ram's hydraulic piston for **340 Heat damage**!\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Rotary Cannons: **DESTROYED (0/1,500 HP)**.\n")
    sections.append("  * Spiked Ram: 1,800 -> **1,460/1,800** | Posture: **268/340**.\n")
    sections.append("  * Total War-Rig HP: 5,610 -> **4,060/5,900** | Posture: **218/380 [CANNONS SHATTERED]**.\n")
    sections.append("  * Kael Composure: Stable (50/50 SP).\n\n")
    sections.append('---\n\n')
    
    # Turn 03 HUD
    t3_hud = make_box("TACTICAL STAGE HUD: ARC 05 - BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 - STAGGER THRESHOLD 1 & SPIKED RAM SHATTER]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[CONVOY][RAMPS] [CHOKE] [TRENCH][RIG]   [RAFTER][SLOPE] [GULLY] [EXIT]  [THRONE]",
        "                [HWARAN][KAEL]  [GAREK]                                 [GWAN]",
        "---",
        "- Node 03: Hwaran (Thermite Charge Burning Rig Transmission)",
        "- Node 04: Kael (Seismic Han-Glass Fist Driving into Ram Struts)",
        "- Node 05: Warlord Garek (STAGGER LEVEL 1 / RIG OVERTURNED)",
        "- Node 10: Drift Throne (Securing Defile Perimeter with Spinal Battery)",
        "---",
        "- Kael (Drift King): Spd 8 -> 4 AP [SURGE] | HP 4,200/4,200 | SP 50/50 | Posture 160/160",
        "- Hwaran (Guide)   : Spd 8 -> 4 AP         | HP 2,800/2,800 | SP 45/45 | Posture 120/120",
        "- Garek Core       : Spd 0 -> 0 AP         | HP 2,240/2,600 | Posture 152/380 [STAGGER LEVEL 1]",
        "- Spiked Ram       : Spd 0 -> 0 AP         | HP 620/1,800   | Posture 92/340 [CRUSHED]",
        "- Total War-Rig    : HP 2,860/5,900 [THRESHOLD BREACHED / TAKES 1.5X DAMAGE]"
    ])
    sections.append(wrap_box(t3_hud))
    
    sections.append("### Turn 03 Action Resolution Log (First Stagger Proc & Spiked Ram Crushed)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Enraged, Garek slams the rig's transmission into reverse, attempting to crush Kael against the canyon wall with `[Death-Spin Ram Drill]`.\n")
    sections.append("  * Kael gains `Tectonic Surge` (+2 Speed -> Net Speed 8, 4 AP).\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael (Speed 8 -> 4 AP): Moves to Node 04 right at the radiator grill. Spends 2 AP on `[Glass Fist: Engine Fracture]`. Spends 2 AP on `[Cleaver Cleave]`.\n")
    sections.append("  * Hwaran (Speed 8 -> 4 AP): Holds Node 03. Spends 2 AP on `[Thermite Transmission Dart]`.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 04 to 05)**: Garek sweeps with `[Death-Spin Ram Drill]` (Base 18 + 2 Coins = 26 Power, Heavy Kinetic/Shatter).\n")
    sections.append("    * Kael clashes with `[Glass Fist: Engine Fracture]` (Base 23 + 2 Coins = 35 Power, Seismic Weight).\n")
    sections.append("    * **Clash Outcome**: Kael WINS THE CLASH (35 vs 26)!\n")
    sections.append("    * Kael drives his translucent glass fist straight into the spiked ram's central mounting knuckle; the acoustic vibration shears the four-inch bolts instantly!\n")
    sections.append("    * The two-ton steel ram breaks free, jamming beneath the war-rig's front axle and flipping the thirty-meter crawler onto its side in a catastrophic rollover!\n")
    sections.append("    * Deals **840 Void/Shatter damage** and +126 Posture Strain!\n")
    sections.append("- **Step 4: STAGGER THRESHOLD 1 TRIGGERED!**:\n")
    sections.append("  * Total War-Rig HP crosses 70% threshold (4,130 HP), falling to **2,860/5,900 HP**; Posture crosses 60% strain line!\n")
    sections.append("  * **STAGGER LEVEL 1 ACTIVE!** The war-rig lies overturned and smoking in the sand; command cupola exposed; takes +50% damage across all incoming attacks!\n")
    sections.append("- **Step 5: Turn End State**:\n")
    sections.append("  * Total War-Rig HP: 4,060 -> **2,860/5,900 [THRESHOLD BREACHED: Below 4,130 HP!]**.\n")
    sections.append("  * Spiked Ram: 1,460 -> **620/1,800** | Posture: **92/340 [CRUSHED]**.\n")
    sections.append("  * Boss Posture: **152/380 [STAGGER LEVEL 1]**.\n")
    sections.append("  * Kael Status: Unbroken.\n\n")
    sections.append('---\n\n')
    
    # Turn 04 HUD
    t4_hud = make_box("TACTICAL STAGE HUD: ARC 05 - BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 - MAXIMUM BURST & PHASE 2 THRESHOLD SKIP]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[CONVOY][RAMPS] [CHOKE] [TRENCH][RIG]   [RAFTER][SLOPE] [GULLY] [EXIT]  [THRONE]",
        "                        [HWARAN][KAEL]  [GAREK]                         [GWAN]",
        "---",
        "- Node 04: Hwaran (Suppressing Remaining Skimmers with Slag Rounds)",
        "- Node 05: Kael (Four-Fold Cleaver Execution on Overturned Cupola)",
        "- Node 06: Warlord Garek (Immobilized / Trapped Inside Smoking Wreck)",
        "- Node 10: Drift Throne (Securing the Entire Canyon Defile)",
        "---",
        "- Kael (Drift King): Spd 11 -> 5 AP [BURST CRIT] | HP 4,200/4,200 | SP 50/50",
        "- Garek Core       : Spd 0 -> 0 AP               | HP 690/2,600   | Posture 60/380",
        "- Spiked Ram       : DESTROYED (0/1,800 HP)",
        "- Total War-Rig    : HP 690/5,900 [BURST DAMAGE 2,170! SECOND THRESHOLD SKIPPED]"
    ])
    sections.append(wrap_box(t4_hud))
    
    sections.append("### Turn 04 Action Resolution Log (Maximum Burst & Phase 2 Threshold Skip)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Garek's war-rig lies disabled on its side; fuel tanks are punctured, leaking diesel across the crushed sandstone.\n")
    sections.append("  * Kael coordinates an all-out offensive barrage targeting the command cupola.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael (Speed 11 -> 5 AP, Momentum Crit): Stands atop the overturned chassis at Node 05. Spends 3 AP on `[Four-Fold Cleaver Execution]`. Spends 2 AP on `[Seismic Impact]`.\n")
    sections.append("  * Hwaran: Calls in `[Spinal Battery Precision Kinetic Strike]` (3 AP).\n")
    sections.append("- **Step 3: Unopposed Stagger Punishment Rotation**:\n")
    sections.append("  * Kael's `[Four-Fold Cleaver Execution]`: Rips through the armored cupola for **1,180 Heavy Weight damage** (Fatal 2.0x proc!)!\n")
    sections.append("  * Kael's `[Seismic Impact]`: Crushes the remaining ram mounts for **510 Shatter damage**!\n")
    sections.append("  * Drift Throne Spinal Shot: Kinetic round obliterates the rig's engine block for **480 Blast damage**!\n")
    sections.append("  * **TOTAL BURST DAMAGE: 2,170 DAMAGE!**\n")
    sections.append("- **Step 4: SECOND STAGGER THRESHOLD (2,360 HP) COMPLETELY SKIPPED!**:\n")
    sections.append("  * War-Rig HP plunges from 2,860 down to **690/5,900 HP**! Spiked Ram completely destroyed (0/1,800 HP)!\n")
    sections.append("  * **Phase 2 Emergency Activation Triggered!**\n")
    sections.append("- **Step 5: Turn End State**:\n")
    sections.append("  * Total War-Rig HP: 2,860 -> **690/5,900** (Cupola HP: **690/2,600** | Ram: **DESTROYED**).\n")
    sections.append("  * Posture: **60/380**.\n\n")
    sections.append('---\n\n')
    
    # Turn 05 HUD
    t5_hud = make_box("TACTICAL STAGE HUD: ARC 05 - BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 - CORSAIR LAST STAND & THE DRIFT KING'S VERDICT]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[CONVOY][RAMPS] [CHOKE] [TRENCH][RIG]   [RAFTER][SLOPE] [GULLY] [EXIT]  [THRONE]",
        "                                [HWARAN][KAEL]  [GAREK]                 [GWAN]",
        "---",
        "- Node 05: Kael (Relic Overdrive: PROMISE OF THE HORIZON SOVEREIGN)",
        "- Node 06: Warlord Garek (Last Stand: Twin Sawed-Off Slag Shotguns)",
        "- Node 07: Hwaran (Disarming Fleeing Corsair Technicals)",
        "- Node 10: Drift Throne (Opening Broadside on Retreating Dune-Skimmers)",
        "---",
        "- Kael (Drift King): Spd 9 -> 5 AP [OVERDRIVE] | HP 4,200/4,200 | SP 50/50 [RESOLVE]",
        "- Garek Core       : Spd 3 -> 1 AP             | HP 690/2,600   | Posture 32/380 [BLEEDING]",
        "- Total War-Rig    : HP 690/5,900 [SLAG BLAST DEFLECTED / GAREK DISARMED]"
    ])
    sections.append(wrap_box(t5_hud))
    
    sections.append("### Turn 05 Action Resolution Log (Phase 2 Escalation: Corsair Last Stand & Horizon Cleaver)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Garek kicks open the crumpled hatch of the cupola, bleeding from the scalp, raising twin sawed-off heavy slag shotguns!\n")
    sections.append("  * Boss Special Skill: `[Point-Blank Double Slag Blast]` (Brutal Kinetic Cataclysm, 3 Coins).\n")
    sections.append("  * Kael activates Relic Overdrive: `[PROMISE OF THE HORIZON SOVEREIGN — MAXIMUM]` (Cost: 3 AP, 30 SP).\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael (Speed 9 -> 5 AP [Overdrive]): Steps straight onto the smoking hatch at Node 06, bringing the obsidian blade down.\n")
    sections.append("  * Hwaran: Secures the flanking ravines at Node 07.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 05 to 06)**: Garek fires `[Point-Blank Double Slag Blast]` (Base 23 + 3 Coins = 35 Power, Point-Blank Kinetic/Heat).\n")
    sections.append("    * Kael clashes with `[PROMISE OF THE HORIZON SOVEREIGN — MAXIMUM]` (Base 30 + 3 Coins Heads = 52 Power, Seismic Execution).\n")
    sections.append("    * **Clash Outcome**: KAEL OVERWHELMING RELIC CLASH WIN (52 vs 35)!\n")
    sections.append("    * Kael's glass arm deflects the twin blasts of buckshot into the sky (`[P3: Parry/Protection]`).\n")
    sections.append("    * The broad side of his trench-cleaver smashes into Garek's chest, shattering his shotgun receivers and pinning him to the crushed iron roof!\n")
    sections.append('    * Kael leans down, his voice cold as a winter night on the salt flats: *"You picked the wrong convoy, Garek."*\n')
    sections.append("    * Garek's surviving crew members drop their weapons and scatter in terror! Zero refugee casualties taken!\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Total War-Rig HP: **690/5,900** | Posture: **32/380 [BLEEDING]**.\n")
    sections.append("  * Kael Composure: 50/50 SP.\n\n")
    sections.append('---\n\n')
    
    # Turn 06 HUD
    t6_hud = make_box("TACTICAL STAGE HUD: ARC 05 - BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 - CORSAIR ROUT & CANYON SECURED]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[CONVOY][RAMPS] [CHOKE] [TRENCH][WRECK] [ROUT]  [SLOPE] [GULLY] [OPEN]  [THRONE]",
        "                                [HWARAN][KAEL]  [GAREK]                 [GWAN]",
        "---",
        "- Node 05: Warlord Garek (SURRENDERED & BOUND IN RIGGING CABLES)",
        "- Node 06: Corsair Armada (100% ROUTED & ABANDONING VEHICLES)",
        "- Node 09: Northern Sand Corridor Exit (Pathway to Somnarak OPEN)",
        "---",
        "- Kael Status: Zero Damage Taken | Composure 50/50 SP (Supreme Authority)",
        "- Expedition Status: AMBUSH BROKEN | 400 Refugees Safe | Corridor Cleared"
    ])
    sections.append(wrap_box(t6_hud))
    
    sections.append("### Turn 06 Action Resolution Log (Corsair Rout & Caravan Passage)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Hostile intent drops to zero. Posture reaches **0/380 [TOTAL ROUT]**.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael hauls Garek from the wreckage, tossing him onto the sand before the refugee convoy.\n")
    sections.append("- **Step 3: Rout & Desert Justice**:\n")
    sections.append("  * Garek spits blood, looking up at the hundreds of Ash Walker foundry workers who have stepped out of the trailers holding iron prybars:\n")
    sections.append('  * *"Kill me then, Kael. The desert don\'t keep prisoners."*\n')
    sections.append('  * Kael plants his cleaver into the earth, looking down at the broken warlord:\n')
    sections.append('    > *"You are not worth the iron it would take to hang you, Garek. Strip your rigs of fuel and water, give the keys to Wright Gwan, and start walking back to Zone C on foot. If I ever see your banners on this road again, the sand will have you."*\n')
    sections.append("  * Deals **690 Decisive Authority**! Garek HP drops to 0!\n")
    sections.append("- **Step 4: Operational Artifact Extraction & Convoy Resumption**:\n")
    sections.append("  * **Tactical Requisition Acquired**: `[Overland Module: Corsair Superchargers]` (Increases maximum convoy cruising speed by +15 km/h and unlocks twin heavy harpoon mounts).\n")
    sections.append("  * **Corridor Cleared**: The remaining pirate buggies are dismantled for scrap and fuel. The Drift Throne hooks Garek's war-rig behind the convoy as a salvage tender and rolls outward into the open plain.\n")
    sections.append("  * **Casualties**: Zero Refugee or Caravan Casualties. Kael HP 4,200/4,200. Composure 50/50 SP.\n\n")
    sections.append('---\n\n')
    
    # Chapter VI: The Corsair Rout & The Sovereign of the Dunes
    sections.append("## Chapter VI: The Corsair Rout & The Sovereign of the Dunes\n\n")
    sections.append("The narrow sandstone defile opened out into the vast, sweeping plains of the Upper Salt Basin. Behind the convoy, Garek and his surviving marauders were tiny, desperate silhouettes trudging eastward across the shimmering alkali flats, stripped of their vehicles and heavy arms. Aboard the Drift Throne's trailers, the four hundred Ash Walkers began to sing—an ancient nomadic anthem of homecoming that carried across the salt on the evening breeze.\n\n")
    sections.append("In the maintenance deck, Master Wright Gwan had already jury-rigged the captured war-rig's twin supercharged fuel pumps into the Drift Throne's auxiliary ley-turbines. The mobile cruiser surged forward with unprecedented power, its massive caterpillar tracks gliding effortlessly over the desert ridges.\n\n")
    sections.append('"All four hundred refugees accounted for, Commander," Hwaran reported, stepping into the observation bridge with two tin mugs of hot broth. "Zero injuries. Somnarak\'s western gates are forty-eight hours out."\n\n')
    sections.append('Kael took the cup, gazing out through the forward window toward the far northern horizon, where the sky ceased to be red or gray and turned a pure, frighteningly pristine white.\n\n')
    sections.append('"We take the refugees back to Zone E first," Kael said quietly. "Then we refuel, we reload the harpoons, and we point the prow north."\n\n')
    sections.append('"Mugeukji?" Hwaran whispered, her voice tightening.\n\n')
    sections.append('"The edge of the world," Kael answered. "Where the sound ends."\n\n')
    sections.append('---\n\n')
    
    # Chapter VII: Operational Requisition Harvest & Waystation Ingress
    sections.append("## Chapter VII: Operational Requisition Harvest & Waystation Ingress\n\n")
    sections.append("The caravan completed the final crossing to Waystation 15 under full supercharged cruising speed:\n\n")
    
    reward_box = make_box("OVERLAND REQUISITION HARVEST: ARC 05", [
        "ACQUIRED SALVAGE     : Captured Heavy War-Rig & 3,000 Gallons Refined Diesel",
        "UPGRADE DESIGNATION  : [Overland Module: Corsair Superchargers]",
        "CARAVAN SPEED STATUS : Cruising at 70 km/h across Northern Basin",
        "---",
        "FLAGSHIP SYSTEM ENHANCEMENTS:",
        "1. Supercharged Drive: Cruiser top speed increased from 55 to 70 km/h,",
        "                     allowing rapid evasion of supersonic sandstorms.",
        "2. Harpoon Tender    : Salvaged rig converted into mobile heavy winch tender",
        "                     (+50% Towing Capacity across sand bogs).",
        "3. Convoy Morale     : Cheonbulok refugee integration complete; 120 skilled",
        "                     foundry hands added to maintenance cadre.",
        "---",
        "NEXT TARGET REGION:",
        "- Kilometer 3,100 to 4,800: The Perimeter of Silence & The Mugeukji Attempt"
    ])
    sections.append(wrap_box(reward_box))
    
    sections.append("The Drift Throne rolled into the outer staging grounds of Somnarak Zone E, safe, unbroken, and ready for its ultimate voyage to the North.\n")
    
    return "".join(sections)

def build_arc_6():
    sections = []
    
    # Title & Subtitle
    sections.append("# Arc 6: The Mugeukji Attempt — The Perimeter of Silence (무극지 도전 — 침묵의 경계)\n")
    sections.append("## The Horizon Caravan Chronicles — Planetary Overland Expedition (Year 4238, Month 8)\n\n")
    
    # Operational Attribute Table
    sections.append("| Operational Attribute | Specification Dossier |\n")
    sections.append("|---|---|\n")
    sections.append("| **Campaign Theater** | The Horizon Caravan (지평선대 — Jipyeongseondae) |\n")
    sections.append("| **Arc Designation** | Arc 6: The Mugeukji Attempt — The Perimeter of Silence |\n")
    sections.append("| **Overland Sector** | Kilometer 3,100 to 4,800 — The Polar White Dust Expanse |\n")
    sections.append("| **Threat Rating** | UTS-4 (Apex Sovereign Sensory Erasure Horizon) |\n")
    sections.append("| **Deploying Flagship**| The Drift Throne (Autonomous Deep Frontier Configuration) |\n")
    sections.append("| **Caravan Command** | Supreme Commander Kael, Guide Hwaran, & Seer Sora |\n")
    sections.append("| **Primary Opponent** | The Archon of the Void (무극의 지배자 — Sovereign SECC-108) |\n")
    sections.append("| **Stagger Profile** | 60% Posture Strain (Veil Break) / 0% Posture (Disengagement) |\n")
    sections.append("| **Operational Yield** | The Horizon Beacon & The Sovereign Drift Charter |\n\n")
    
    # Master Dossier Box
    dossier = make_box("EXPEDITION DOSSIER: ARC 6 - THE MUGEUKJI ATTEMPT", [
        "OPERATION NAME     : Arc 6 - Breaching the Perimeter of Silence",
        "PRIMARY THEATER    : Mugeukji - Perimeter of Absolute Silence (Km 3,100)",
        "DATE & EPOCH       : Year 4238, Month 8 (The Northern Void Expedition)",
        "PRIMARY ADVERSARY  : The Archon of the Void (Sensory Erasure Sovereign)",
        "---",
        "ADVERSARY PROFILE (THE ARCHON OF THE VOID):",
        "- Total Health (HP): 7,000 HP | Posture Pool: 440/440",
        "- Stagger 1 Proc   : 60% Posture Strain (264 Posture) / Veil Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Tactical Disengagement)",
        "- Resistances      : All Elements 1.0x (Void Absorbed, Acoustic Vulnerable)",
        "---",
        "TARGETABLE COMBAT ANCHORS:",
        "1. Null Siphon     : 1,800 HP | Posture 340/340 (Absolute sound-erasure veil)",
        "2. Monolith Halo   : 2,100 HP | Posture 380/380 (Levitating marble nullifiers)",
        "3. Vacuum Core     : 3,100 HP | Posture 440/440 (Sensory dissolution heart)"
    ])
    sections.append(wrap_box(dossier))
    
    # Epigraph Quote
    sections.append('> *"We cannot reach them yet. The Silence is too deep. The Void does not kill with fire or claws; it kills by making you forget who you were when you crossed the line. If we push further today, we will lose our souls. So we plant our beacon, we turn around, and we live to cross it tomorrow."*\n')
    sections.append('> — Kael, The Drift King, standing at the border of Mugeukji\n\n')
    sections.append('---\n\n')
    
    # Chapter I
    sections.append("## Chapter I: The White Dust Horizon & The Death of All Sound\n\n")
    sections.append("In the eighth month of Year 4238, having established the sovereign overland trade treaty between Somnarak and Cheonbulok, Kael turned the Drift Throne north-northwest toward humanity's greatest planetary enigma: **Mugeukji (무극지 / 無極地) — The City of Absolute Silence**. Across three thousand one hundred kilometers of polar desert, the golden sands ended with razor-sharp abruptness, replaced by an endless, flat plain of fine, blindingly white powder.\n\n")
    sections.append("The moment the cruiser's caterpillar treads rolled onto the white plateau, all sound ceased.\n\n")
    sections.append("It was not silence caused by quietness or lack of wind. It was an active, predatory acoustic vacuum. The deafening roar of the 142.5-meter crawler's four diesel-hydraulic engines vanished instantly. When Kael spoke, no vibration left his lips; his vocal cords strained in complete, suffocating muteness. Outside, gale-force winds whipped sheets of white powder across the hull at ninety knots, yet the glass windows did not rattle. There was only absolute, terrifying nothingness.\n\n")
    sections.append('"Acoustic telemetry is dead," Sora signaled using rapid hand-signs, her bandaged face pale with agony. "The vacuum is reaching inside our minds. It is drinking our thoughts. If we stay in this field for sixty minutes, our memories will unravel into blank paper."\n\n')
    sections.append('Kael looked out the forward observation cupola. Rising from the dead white plain five hundred paces ahead was the sovereign guardian of the threshold.\n\n')
    sections.append('---\n\n')
    
    # Chapter II
    sections.append("## Chapter II: The Monolith Halo & The Marble Archon\n\n")
    sections.append("Hovering five meters above the white powder stood **The Archon of the Void (무극의 지배자 / 虛無의 執政官 — SECC-108)**. Standing seven meters tall, the sovereign construct resembled an ancient colossus carved from seamless, vibrationless white marble. It had no face—only a concave, polished mirror of obsidian that absorbed all reflected light.\n\n")
    sections.append("Floating in a slow, hypnotic orbit above its head was the **Monolith Halo**, eight levitating slabs of Before-Time limestone inscribed with the erased characters of an extinct language. Draped around its torso was the **Null-Acoustic Siphon Veil**, an articulated mantle of anti-matter filaments that actively pulled sound, kinetic energy, and psychic identity into total dissolution. At its core burned the **Vacuum Heart**, a singularity that drank the ambient acoustic resonance of the earth.\n\n")
    sections.append('The Archon did not speak. It did not threaten. It merely existed as the physical embodiment of the world\'s end—the insurmountable wall separating humanity\'s surviving scrap-heaps from whatever lay locked within the forgotten polar north.\n\n')
    sections.append('---\n\n')
    
    # Chapter III
    sections.append("## Chapter III: The Silent Dialectic & The Burden of Remembering\n\n")
    sections.append("Kael walked down the debarkation ramp onto the white dust. Beneath his boots, the powder felt colder than glacial ice, yet it did not melt. His left arm of translucent Han-glass was the only thing in the universe that still had a voice: the crystal hummed at three hundred and thirty hertz, glowing with deep, stubborn amber light that fought back the encroaching white fog.\n\n")
    sections.append("He drew the Obsidian Trench-Cleaver. In the absolute silence, the blade made no scrape as it cleared the leather sheath. Across twenty paces, Kael locked eyes with the faceless obsidian mirror.\n\n")
    sections.append('Inside his mind, the Archon\'s presence pressed down like a lead weight, transmitting pure conceptual intent:\n\n')
    sections.append('*[Why do you push against the boundary, insect of dust? Beyond this line lies the peace that your burning cities could never build. In Mugeukji, no one hungers. No one weeps. No one bleeds. Lay down your iron and be forgotten.]*\n\n')
    sections.append('Kael planted his boots firmly into the white dust. His jaw set in lines of granite, he projected his thoughts straight into the void:\n\n')
    sections.append('*[We did not crawl three thousand kilometers through sand and fire to be erased. We bleed because we are alive. We weep because we love. If your city has forgotten how to hurt, then your city is already a graveyard. We are not turning back until we plant our flag.]*\n\n')
    sections.append('The Archon raised its marble arm. The white dust rose into a swirling hurricane of absolute vacuum. The final battle of the Horizon had begun.\n\n')
    sections.append('---\n\n')
    
    # Chapter IV
    sections.append("## Chapter IV: Overland Arena Topology & Combat Engagement Parameters\n\n")
    sections.append("Using pre-arranged hand signals, Hwaran and Wright Gwan coordinated the Drift Throne's acoustic weapon array:\n\n")
    
    grid_box = make_box("TACTICAL ARENA TOPOLOGY: MUGEUKJI PERIMETER OF SILENCE (KM 3,100)", [
        "[STAGE NODES 01 TO 10 - DEBARKATION RAMPS TO VOID ARCHON DAIS]",
        "[N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "---",
        "- Node 01: Drift Throne Debarkation Ramps (Kael Acoustic Vanguard Anchor)",
        "- Node 02: Hwaran Forward Acoustic Post (Harmonic Signal Beacon Array)",
        "- Node 03: Wright Gwan Support Station (Pressurized Ley-Sound Cannons)",
        "- Node 04: White Dust Tundra Margin (Extreme Null-Vacuum Field)",
        "- Node 05: The Archon of the Void (Central White Marble Colossus)",
        "- Node 06: Monolith Halo Orbital Ring (Eight Levitating Nullifiers)",
        "- Node 07: Sub-Surface Vacuum Trench (Acoustic Erasure Sump)",
        "- Node 08: Deep Polar Fissure (Absolute Zero Thermal Drain)",
        "- Node 09: The Boundary Monolith Line (The Border of Mugeukji)",
        "- Node 10: Drift Throne Acoustic Horn Array (Sora Maximum Decibel Rig)"
    ])
    sections.append(wrap_box(grid_box))
    
    sections.append("The Archon of the Void could not be harmed by conventional kinetic weapons; its **Null Siphon Veil** absorbed all kinetic and thermal energy into nonexistence. Kael's only viable strategy was using his resonant Han-glass arm and the Drift Throne's acoustic horns to generate overwhelming sonic resonance, overloading the **Monolith Halo**, cracking the veil, and driving a harmonic spike into the **Vacuum Core**.\n\n")
    sections.append('---\n\n')
    
    # Chapter V: Combat Gauntlet (Turns 01 to 06)
    sections.append("## Chapter V: The Expedition Combat Gauntlet (Turns 01 to 06)\n\n")
    
    # Turn 01 HUD
    t1_hud = make_box("TACTICAL STAGE HUD: ARC 06 - BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 - MUGEUKJI SILENCE PERIMETER]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[RAMPS] [BEACON][CANNON][MARGIN][ARCHON][HALO]  [TRENCH][CHASM] [BORDER][HORNS]",
        "[KAEL]  [HWARAN][GWAN]          [VOID]                                  [SORA]",
        "---",
        "- Node 01: Drift Throne Ramps / Kael Vanguard Band 1",
        "- Node 02: Hwaran (Short Band 2 / Harmonic Signal Beacon)",
        "- Node 03: Wright Gwan (Support Band 2 / Ley-Sound Cannon)",
        "- Node 04: White Dust Margin (Absolute Sound Erasure Field)",
        "- Node 05: The Archon of the Void (Null Siphon & Monolith Halo)",
        "- Node 06: Levitating Halo Ring (Eight Marble Nullifiers)",
        "- Node 10: Drift Throne Acoustic Horns (Chief Ley-Seer Sora)",
        "---",
        "- Kael (Drift King): Spd 6 -> 3 AP | HP 4,200/4,200 | SP 50/50 | Posture 160/160",
        "- Hwaran (Guide)   : Spd 7 -> 4 AP | HP 2,800/2,800 | SP 45/45 | Posture 120/120",
        "- Archon Core      : Spd 5 -> 3 AP | HP 3,100/3,100 | Posture 440/440 [SILENCE]",
        "- Null Siphon      : Spd 7 -> 4 AP | HP 1,800/1,800 | Posture 340/340 [DRAIN]",
        "- Monolith Halo    : Spd 3 -> 1 AP | HP 2,100/2,100 | Posture 380/380 [ORBITING]"
    ])
    sections.append(wrap_box(t1_hud))
    
    sections.append("### Turn 01 Action Resolution Log (Intercepting the Sensory Erasure Wave)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Kael initializes `[Acoustic Resonance Ward]`: Han-glass arm vibrates at 528 Hz, projecting an audible sound-bubble granting +4 Protection.\n")
    sections.append("  * Sora powers up the Drift Throne's heavy acoustic horns at Node 10: Broadcasting the Anthem of the Nomad.\n")
    sections.append("  * The Archon pulses with `[Aura of Absolute Non-Existence]`: All physical kinetic attacks deal 0 damage unless accompanied by sonic resonance.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael (Speed 6 -> 3 AP): Holds Node 01. Spends 2 AP on `[Trench-Cleaver: Acoustic Deflection]`. Holds 1 AP in Guard.\n")
    sections.append("  * Hwaran (Speed 7 -> 4 AP): Holds Node 02. Spends 2 AP on `[Harmonic Signal Beacon]`. Spends 2 AP on `[Acoustic Flare]`.\n")
    sections.append("  * The Archon (Speed 7 -> 4 AP): Glides from Node 05 to Node 02. Spends 2 AP on `[Sensory Erasure Wave]`. Spends 2 AP on `[Monolith Stasis Pulse]`.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 01 to 05)**: The Archon pulses `[Sensory Erasure Wave]` (Base 20 + 2 Coins = 30 Power, Area Void/Amnesia).\n")
    sections.append("    * Kael intercepts with `[Trench-Cleaver: Acoustic Deflection]` (Base 23 + 2 Coins = 35 Power, Seismic Heavy Blade).\n")
    sections.append("    * **Clash Outcome**: Kael WINS THE CLASH OVERWHELMINGLY (35 vs 30)!\n")
    sections.append("    * Kael strikes his glass arm against the obsidian cleaver; the deafening acoustic chime shatters the silence, tearing a hole through the erasure wave (`[P3: Parry/Protection]`).\n")
    sections.append("    * Acoustic shockwave reflects **340 sonic damage** back into the Null Siphon, inflicting +68 Posture Strain!\n")
    sections.append("  * **Clash 2 (Node 02 to 06)**: Hwaran's `[Harmonic Beacon]` anchors the squad's memories; zero composure drain taken!\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Null Siphon HP: 1,800 -> **1,460/1,800** | Posture: **272/340**.\n")
    sections.append("  * Total Archon HP: 7,000 -> **6,660/7,000** | Posture: **372/440**.\n")
    sections.append("  * Kael Composure: **100% (50/50 SP)**. Zero cognitive damage taken.\n\n")
    sections.append('---\n\n')
    
    # Turn 02 HUD
    t2_hud = make_box("TACTICAL STAGE HUD: ARC 06 - BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 - NULL SIPHON SHATTERED & SONIC BREACH]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[RAMPS] [BEACON][CANNON][MARGIN][ARCHON][HALO]  [TRENCH][CHASM] [BORDER][HORNS]",
        "        [HWARAN][GWAN]  [KAEL]  [SHATTER]                               [SORA]",
        "---",
        "- Node 03: Wright Gwan (Discharging Dual Pressurized Sonic Cannons)",
        "- Node 04: Kael (Advancing / Driving Resonant Cleaver into Siphon Veil)",
        "- Node 05: The Archon (Null Siphon Destroyed 0/1,800 HP)",
        "- Node 10: Drift Throne Horns (Broadcasting Overwhelming 140 dB Pulse)",
        "---",
        "- Kael (Drift King): Spd 8 -> 4 AP [SURGE] | HP 4,200/4,200 | SP 50/50 | Posture 160/160",
        "- Hwaran (Guide)   : Spd 9 -> 5 AP         | HP 2,800/2,800 | SP 45/45 | Posture 120/120",
        "- Archon Core      : Spd 3 -> 1 AP         | HP 3,100/3,100 | Posture 306/440",
        "- Null Siphon      : DESTROYED (0/1,800 HP)| SOUND ERASURE PERMANENTLY COLLAPSED",
        "- Monolith Halo    : Spd 3 -> 1 AP         | HP 1,680/2,100 | Posture 298/380"
    ])
    sections.append(wrap_box(t2_hud))
    
    sections.append("### Turn 02 Action Resolution Log (Part Destruction: Null Siphon Shattered)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Kael activates `Tectonic Momentum` (+2 Speed next turn -> Net Speed 8, 4 AP).\n")
    sections.append("  * The Archon attempts `[Event Horizon Collapse]` to permanently dissolve the caravan into white powder.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael (Speed 8 -> 4 AP [Surge]): Steps to Node 04 right before the marble titan. Spends 3 AP on `[Obsidian Cleaver: Sonic Severance]`. Holds 1 AP in Guard.\n")
    sections.append("  * Hwaran (Speed 9 -> 5 AP): Spends 3 AP on `[High-Frequency Acoustic Pulse]`. Spends 2 AP on `[Memory Anchor]`.\n")
    sections.append("  * Wright Gwan: Discharges the Drift Throne's forward sonic cannons at point-blank range.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 04 to 05)**: The Archon channels `[Event Horizon Collapse]` (Base 21 + 2 Coins = 29 Power, Area Void/Erasure).\n")
    sections.append("    * Kael clashes with `[Obsidian Cleaver: Sonic Severance]` (Base 27 + 3 Coins Heads = 47 Power, Acoustic Weight).\n")
    sections.append("    * **Clash Outcome**: Kael WINS THE CLASH OVERWHELMINGLY (47 vs 29)!\n")
    sections.append("    * Kael's cleaver, vibrating with the full 140-decibel roar of the cruiser's horns, slices through the anti-matter filaments of the Null Siphon!\n")
    sections.append("    * The silence shatters with a deafening crack like thunder; sound returns to the polar plain in a concussive shockwave!\n")
    sections.append("    * Deals **1,460 Critical Acoustic damage** (Fatal 2.0x proc!)!\n")
    sections.append("    * **TARGETED PART DESTROYED**: The Null-Acoustic Siphon Veil is completely destroyed (**Siphon HP: 0/1,800** credit)!\n")
    sections.append("    * **EFFECT**: Silence aura destroyed; boss permanently loses 1 Speed Slot!\n")
    sections.append("  * **Monolith Halo Damage**:\n")
    sections.append("    * Sonic cannon shockwave shatters two floating limestone slabs for **420 Sonic damage**!\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Null Siphon: **DESTROYED (0/1,800 HP)**.\n")
    sections.append("  * Monolith Halo: 2,100 -> **1,680/2,100** | Posture: **298/380**.\n")
    sections.append("  * Total Archon HP: 6,660 -> **4,780/7,000** | Posture: **242/440 [SIPHON SHATTERED]**.\n")
    sections.append("  * Kael Composure: Stable (50/50 SP).\n\n")
    sections.append('---\n\n')
    
    # Turn 03 HUD
    t3_hud = make_box("TACTICAL STAGE HUD: ARC 06 - BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 - STAGGER THRESHOLD 1 & MONOLITH HALO SHATTER]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[RAMPS] [BEACON][CANNON][MARGIN][ARCHON][HALO]  [TRENCH][CHASM] [BORDER][HORNS]",
        "        [HWARAN][GWAN]  [KAEL]  [CRACK]                                 [SORA]",
        "---",
        "- Node 04: Kael (Seismic Han-Glass Fist Driving into Levitating Halo)",
        "- Node 05: The Archon (STAGGER LEVEL 1 / WHITE MARBLE FRACTURED)",
        "- Node 06: Monolith Halo (Six Remaining Slabs Shattering into Dust)",
        "- Node 10: Drift Throne Horns (Broadcasting Sovereign Acoustic Chord)",
        "---",
        "- Kael (Drift King): Spd 8 -> 4 AP [SURGE] | HP 4,200/4,200 | SP 50/50 | Posture 160/160",
        "- Hwaran (Guide)   : Spd 8 -> 4 AP         | HP 2,800/2,800 | SP 45/45 | Posture 120/120",
        "- Archon Core      : Spd 0 -> 0 AP         | HP 2,740/3,100 | Posture 172/440 [STAGGER LEVEL 1]",
        "- Monolith Halo    : Spd 0 -> 0 AP         | HP 740/2,100   | Posture 112/380 [SHATTERED]",
        "- Total Archon     : HP 3,480/7,000 [THRESHOLD BREACHED / TAKES 1.5X DAMAGE]"
    ])
    sections.append(wrap_box(t3_hud))
    
    sections.append("### Turn 03 Action Resolution Log (First Stagger Proc & Monolith Halo Shattered)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Disarmed of its veil, the Archon brings down the **Monolith Halo** in a crushing orbit: `[Judgment of the Silent Monolith]`.\n")
    sections.append("  * Kael gains `Tectonic Surge` (+2 Speed -> Net Speed 8, 4 AP).\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael (Speed 8 -> 4 AP): Holds Node 04. Spends 2 AP on `[Glass Fist: Bedrock Fracture]`. Spends 2 AP on `[Cleaver Cleave]`.\n")
    sections.append("  * Hwaran (Speed 8 -> 4 AP): Advances to Node 04. Spends 2 AP on `[Acoustic Resonance Dart]`.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 04 to 05)**: The Archon slams with `[Judgment of the Silent Monolith]` (Base 19 + 2 Coins = 27 Power, Heavy Weight/Void).\n")
    sections.append("    * Kael clashes with `[Glass Fist: Bedrock Fracture]` (Base 24 + 2 Coins = 36 Power, Seismic Weight).\n")
    sections.append("    * **Clash Outcome**: Kael WINS THE CLASH (36 vs 27)!\n")
    sections.append("    * Kael's glass fist punches directly through the lead marble monolith; the acoustic shockwave arcs through the orbital ring, detonating all six remaining slabs!\n")
    sections.append("    * Drone-directed acoustic darts pierce the Archon's marble collar, creating cyclopean fractures down its chest!\n")
    sections.append("    * Deals **940 Void/Acoustic damage** and +130 Posture Strain!\n")
    sections.append("- **Step 4: STAGGER THRESHOLD 1 TRIGGERED!**:\n")
    sections.append("  * Total Archon HP crosses 70% threshold (4,900 HP), falling to **3,480/7,000 HP**; Posture crosses 60% strain line!\n")
    sections.append("  * **STAGGER LEVEL 1 ACTIVE!** The Archon sinks to the white sand; floating spires crash down; takes +50% damage across all incoming attacks!\n")
    sections.append("- **Step 5: Turn End State**:\n")
    sections.append("  * Total Archon HP: 4,780 -> **3,480/7,000 [THRESHOLD BREACHED: Below 4,900 HP!]**.\n")
    sections.append("  * Monolith Halo: 1,680 -> **740/2,100** | Posture: **112/380 [SHATTERED]**.\n")
    sections.append("  * Boss Posture: **172/440 [STAGGER LEVEL 1]**.\n")
    sections.append("  * Kael Status: Unbroken.\n\n")
    sections.append('---\n\n')
    
    # Turn 04 HUD
    t4_hud = make_box("TACTICAL STAGE HUD: ARC 06 - BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 - MAXIMUM BURST & PHASE 2 THRESHOLD SKIP]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[RAMPS] [BEACON][CANNON][MARGIN][ARCHON][HALO]  [TRENCH][CHASM] [BORDER][HORNS]",
        "                [GWAN]  [HWARAN][KAEL]  [CORE]                          [SORA]",
        "---",
        "- Node 04: Hwaran (Directing All Flagship Acoustic Batteries onto Core)",
        "- Node 05: Kael (Four-Fold Cleaver Execution on Exposed Vacuum Core)",
        "- Node 06: The Archon (Immobilized / White Marble Weeping Prismatic Cracks)",
        "- Node 10: Drift Throne Horns (Sustaining Maximum Decibel Saturation)",
        "---",
        "- Kael (Drift King): Spd 11 -> 5 AP [BURST CRIT] | HP 4,200/4,200 | SP 50/50",
        "- Archon Core      : Spd 0 -> 0 AP               | HP 820/3,100   | Posture 68/440",
        "- Monolith Halo    : DESTROYED (0/2,100 HP)",
        "- Total Archon     : HP 820/7,000 [BURST DAMAGE 2,660! SECOND THRESHOLD SKIPPED]"
    ])
    sections.append(wrap_box(t4_hud))
    
    sections.append("### Turn 04 Action Resolution Log (Maximum Burst & Phase 2 Threshold Skip)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * The Archon remains stunned on the white dust; the Vacuum Core in its chest is completely exposed, pulling white powder into its gravity well.\n")
    sections.append("  * Kael coordinates an all-out offensive barrage targeting the central singularity.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael (Speed 11 -> 5 AP, Momentum Crit): Stands at Node 05 before the chest cavity. Spends 3 AP on `[Four-Fold Cleaver Execution]`. Spends 2 AP on `[Seismic Impact]`.\n")
    sections.append("  * Hwaran: Calls in `[Spinal Battery Acoustic Shockwave]` (3 AP).\n")
    sections.append("- **Step 3: Unopposed Stagger Punishment Rotation**:\n")
    sections.append("  * Kael's `[Four-Fold Cleaver Execution]`: Rips through the vacuum core for **1,480 Acoustic/Weight damage** (Fatal 2.0x proc!)!\n")
    sections.append("  * Kael's `[Seismic Impact]`: Shatters the remaining marble ribs for **600 Shatter damage**!\n")
    sections.append("  * Spinal Acoustic Shockwave: Obliterates the halo remnants for **580 Sonic damage**!\n")
    sections.append("  * **TOTAL BURST DAMAGE: 2,660 DAMAGE!**\n")
    sections.append("- **Step 4: SECOND STAGGER THRESHOLD (2,800 HP) COMPLETELY SKIPPED!**:\n")
    sections.append("  * Archon HP plunges from 3,480 down to **820/7,000 HP**! Monolith Halo completely destroyed (0/2,100 HP)!\n")
    sections.append("  * **Phase 2 Emergency Activation Triggered!**\n")
    sections.append("- **Step 5: Turn End State**:\n")
    sections.append("  * Total Archon HP: 3,480 -> **820/7,000** (Core HP: **820/3,100** | Halo: **DESTROYED**).\n")
    sections.append("  * Posture: **68/440**.\n\n")
    sections.append('---\n\n')
    
    # Turn 05 HUD
    t5_hud = make_box("TACTICAL STAGE HUD: ARC 06 - BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 - THE POLAR APOCALYPSE & HORIZON OVERDRIVE]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[RAMPS] [BEACON][CANNON][MARGIN][ARCHON][HALO]  [TRENCH][CHASM] [BORDER][HORNS]",
        "                        [HWARAN][KAEL]  [VOID]                          [SORA]",
        "---",
        "- Node 05: Kael (Relic Overdrive: PROMISE OF THE HORIZON SOVEREIGN)",
        "- Node 06: The Archon (Last Stand: Absolute Vacuum Singularity Collapse)",
        "- Node 07: Hwaran (Anchoring Harmonic Beacon against Gravity Pull)",
        "- Node 10: Drift Throne Horns (Full Engine Power Directed to Acoustic Pulse)",
        "---",
        "- Kael (Drift King): Spd 9 -> 5 AP [OVERDRIVE] | HP 4,200/4,200 | SP 50/50 [RESOLVE]",
        "- Archon Core      : Spd 3 -> 1 AP             | HP 820/3,100   | Posture 34/440 [SINGULARITY]",
        "- Total Archon     : HP 820/7,000 [SINGULARITY COLLAPSED / HARMONIC RESONANCE]"
    ])
    sections.append(wrap_box(t5_hud))
    
    sections.append("### Turn 05 Action Resolution Log (Phase 2 Escalation: Absolute Singularity & Horizon Overdrive)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * The Archon awakens in desperate existential realization; the Vacuum Core collapses into an absolute black hole that pulls the entire polar plain inward!\n")
    sections.append("  * Boss Special Skill: `[Absolute Vacuum Singularity Collapse]` (Sensory Erasure Cataclysm, 3 Coins).\n")
    sections.append("  * Kael activates Relic Overdrive: `[PROMISE OF THE HORIZON SOVEREIGN — MAXIMUM]` (Cost: 3 AP, 30 SP).\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael (Speed 9 -> 5 AP [Overdrive]): Steps directly into the roaring event horizon at Node 05, raising his glass arm high.\n")
    sections.append("  * Hwaran: Anchors the caravan's seismic winches at Node 07 to withstand the gravitational pull.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 05 to 06)**: The Archon unleashes `[Absolute Vacuum Singularity Collapse]` (Base 25 + 3 Coins = 37 Power, Area Void/Dissolution).\n")
    sections.append("    * Kael clashes with `[PROMISE OF THE HORIZON SOVEREIGN — MAXIMUM]` (Base 32 + 3 Coins Heads = 55 Power, Transcendent Harmony).\n")
    sections.append("    * **Clash Outcome**: KAEL OVERWHELMING RELIC CLASH WIN (55 vs 37)!\n")
    sections.append("    * Kael's glass arm plunges directly into the black hole; rather than being swallowed, his arm acts as a tuning fork for the entire living world (`[P3: Parry/Protection]`).\n")
    sections.append("    * The laughter of Somnarak's children, the roar of Cheonbulok's forges, and the songs of the nomadic dunes pour through the crystal in a blinding torrent of sound!\n")
    sections.append('    * Kael whispers into the void: *"You cannot swallow a world that refuses to be forgotten!"*\n')
    sections.append("    * The black hole shatters into warm, golden sunlight! Zero caravan casualties taken!\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Total Archon HP: **820/7,000** | Posture: **34/440 [SINGULARITY]**.\n")
    sections.append("  * Kael Composure: 50/50 SP.\n\n")
    sections.append('---\n\n')
    
    # Turn 06 HUD
    t6_hud = make_box("TACTICAL STAGE HUD: ARC 06 - BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 - THE BEACON PLANTED & SOVEREIGN DRIFT]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[RAMPS] [BEACON][CANNON][MARGIN][ARCHON][BEACON][BORDER][HORIZ] [RETURN][THRONE]",
        "                                [KAEL]  [PEACE] [WAY-17][NORTH] [SOUTH] [ROLL]",
        "---",
        "- Node 05: The Archon of the Void (PACIFIED & RESTING IN NOBLE REVERENCE)",
        "- Node 06: Waystation 17: Horizon Boundary (ACOUSTIC BEACON PLANTED)",
        "- Node 09: The Perimeter of Mugeukji (MAPPED & RECORDED FOR FUTURE RETURN)",
        "- Node 10: The Drift Throne (Turning South Toward Somnarak at 55 km/h)",
        "---",
        "- Kael Status: Zero Damage Taken | Composure 50/50 SP (Unshakable Sovereign Authority)",
        "- Expedition Status: THRESHOLD REACHED | Master Beacon Planted | Grand Return"
    ])
    sections.append(wrap_box(t6_hud))
    
    sections.append("### Turn 06 Action Resolution Log (The Beacon Planted & Tactical Disengagement)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Hostile intent drops to zero. Posture reaches **0/440 [TACTICAL DISENGAGEMENT]**.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael steps forward to Node 06, driving a three-meter acoustic relay spire deep into the polar bedrock.\n")
    sections.append("- **Step 3: The Archon's Bow & Sovereign Treaty**:\n")
    sections.append("  * The shattered marble colossus rises slowly. Looking upon the golden beacon pulsing in the white dust, the entity lowers its faceless head in solemn, majestic acknowledgment:\n")
    sections.append('  * *[You have spoken your name into the quiet, son of iron. Mugeukji will not open its gates today, for the world is not yet ready to hear what we remember. But the road is open. Return when your people have learned how to sing without tears.]*\n')
    sections.append('  * Kael raises his cleaver in formal salute:\n')
    sections.append('    > *"We will return, Archon. Keep the border until we bring the morning."*\n')
    sections.append("  * Deals **820 Transcendent Reverence**! Archon HP drops to 0!\n")
    sections.append("- **Step 4: Operational Artifact Extraction & Grand Return Passage**:\n")
    sections.append("  * **Master Relic Acquired**: `[Overland Master Relic: The Horizon Beacon]` (Establishes a permanent acoustic communication link between Somnarak, Cheonbulok, and the Northern Perimeter; unlocks the Sovereign Drift Charter).\n")
    sections.append("  * **The Turnaround**: The Drift Throne executes a monumental 180-degree turn upon the white dust plateau, its caterpillar tracks cutting deep ceremonial ruts as it steers south toward Somnarak.\n")
    sections.append("  * **Casualties**: Zero Casualties Taken. Kael HP 4,200/4,200. Composure 50/50 SP.\n\n")
    sections.append('---\n\n')
    
    # Chapter VI: The Acoustic Beacon & The Wisdom of the Threshold
    sections.append("## Chapter VI: The Acoustic Beacon & The Wisdom of the Threshold\n\n")
    sections.append("The white dust fell away behind the Drift Throne as its caterpillar tracks regained the familiar, gritty traction of the northern gravel flats. Behind them, standing at Kilometer 3,100 like a lone lighthouse upon a frozen sea, **The Horizon Beacon** pulsed with warm golden light, transmitting an unbroken 528-hertz acoustic chime across the desert to every waystation along the four-thousand-kilometer chain.\n\n")
    sections.append("Aboard the bridge, Chief Ley-Seer Sora removed her bandaged visor, tears of relief tracing clean lines through the white dust on her cheeks. Across the communication frequencies, the voices of Somnarak and Cheonbulok were singing together—clear, synchronized, and unbroken across the vast curve of the earth.\n\n")
    sections.append('"We didn\'t breach the city," Hwaran murmured, watching the white horizon vanish into the southern dusk. "Was it a failure, Kael?"\n\n')
    sections.append('"A reckless child breaks down a locked door and dies in the cold," Kael answered, his hand resting gently on the wheel. "A sovereign explorer marks the road, builds the bridges, and makes sure his people survive to walk through it when the time comes. We proved the world is alive, Hwaran. That is not failure. That is the beginning."\n\n')
    sections.append('---\n\n')
    
    # Chapter VII: Operational Requisition Harvest & The Sovereign Drift
    sections.append("## Chapter VII: Operational Requisition Harvest & The Sovereign Drift\n\n")
    sections.append("With the northern boundary mapped and the seventeen acoustic waystations permanently linked into a unified continental network, the Horizon Caravan achieved its ultimate charter:\n\n")
    
    reward_box = make_box("OVERLAND MASTER REQUISITION: THE HORIZON BEACON", [
        "ACQUIRED MASTER RELIC : [Overland Master Relic: The Horizon Beacon]",
        "PRIMARY WEAR CLASS    : Grade Omega Sovereign Overland Charter",
        "PLANETARY COVERAGE    : 4,800 km Unified Trans-Desolate Ley Network",
        "---",
        "SOVEREIGN CARAVAN TRAITS:",
        "1. Continental Accord : Permanent diplomatic, military, and resource",
        "                      trade established between Somnarak & Cheonbulok.",
        "2. The Living Horizon : The Desolate is no longer an exile grave;",
        "                      it is a mapped, sovereign nomadic frontier.",
        "3. Master Ley-Traction: Drift Throne achieves permanent maximum speed",
        "                      (75 km/h) across all terrain, including void sumps.",
        "---",
        "MISSION STATUS: EXPEDITION FULLY AND CANONICALLY RESOLVED",
        "- The Drift Throne returns home as the Sovereign of the Horizon."
    ])
    sections.append(wrap_box(reward_box))
    
    sections.append("The diesel horns of the Drift Throne sounded in joyous, unyielding victory across the vast desert night. Ahead, through the warm twilight, the glowing spires of Somnarak and the smoking furnaces of Cheonbulok shone together under a single, waking sky.\n\n")
    sections.append("The Horizon Caravan had crossed the world, and the world would never be dark again.\n")
    
    return "".join(sections)

if __name__ == "__main__":
    content_5 = build_arc_5()
    with open("SOMNARAK-WORLD/Jipyeongseondae/Arc_5_The_Return.md", "w", encoding="utf-8") as f:
        f.write(content_5)
    print("Arc 5 expanded successfully!")
    
    content_6 = build_arc_6()
    with open("SOMNARAK-WORLD/Jipyeongseondae/Arc_6_The_Mugeukji_Attempt.md", "w", encoding="utf-8") as f:
        f.write(content_6)
    print("Arc 6 expanded successfully!")
