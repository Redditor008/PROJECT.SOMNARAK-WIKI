#!/usr/bin/env python3
"""
tools/build_jipyeongseondae_3_4.py
Generates the fully enriched, canonical chronicles for:
- Arc 3: Arrival at Cheonbulok — The Ash Citadel & The Crucible (천불옥 도착 — 화염의 투기장)
- Arc 4: The Furnace's Secret — Geothermal Core & The Han Reactor (용광로의 비밀 — 한 반응로)
"""

import os
import sys

sys.path.append(os.path.dirname(__file__))
from box_formatter import make_box

def wrap_box(b):
    return "```text\n" + b + "\n```\n\n"

def build_arc_3():
    sections = []
    
    # Title & Subtitle
    sections.append("# Arc 3: Arrival at Cheonbulok — The City of a Thousand Rages (천불옥 도착 — 분노의 도시)\n")
    sections.append("## The Horizon Caravan Chronicles — Planetary Overland Expedition (Year 4238, Month 4)\n\n")
    
    # Operational Attribute Table
    sections.append("| Operational Attribute | Specification Dossier |\n")
    sections.append("|---|---|\n")
    sections.append("| **Campaign Theater** | The Horizon Caravan (지평선대 — Jipyeongseondae) |\n")
    sections.append("| **Arc Designation** | Arc 3: Arrival at Cheonbulok — The Ash Citadel (천불옥 도착) |\n")
    sections.append("| **Overland Sector** | Waystation 08 to 11 — The Caldera Causeway (1,100 to 2,400 km) |\n")
    sections.append("| **Threat Rating** | UTS-3 (Sovereign Gladiatorial Foundries) |\n")
    sections.append("| **Deploying Flagship**| The Drift Throne (142.5m Mobile Heavy Sand Cruiser) |\n")
    sections.append("| **Caravan Command** | Supreme Commander Kael (The Drift King) & Guide Hwaran |\n")
    sections.append("| **Primary Opponent** | Slag Champion Barok & Battle Pit Enforcers |\n")
    sections.append("| **Operational Yield** | Boiling Slag Core & Cheonbulok Treaty Passage |\n\n")
    
    # Master Dossier Box
    dossier = make_box("EXPEDITION DOSSIER: ARC 3 - ARRIVAL AT CHEONBULOK", [
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
    sections.append(wrap_box(dossier))
    
    # Epigraph Quote
    sections.append('> *"In Cheonbulok, words are cheap fuel. If you cannot bleed on the black iron and stand back up, your treaties are only kindling. Step into the pit, outlander. Let us see if your sorrow burns hotter than our rage."*\n')
    sections.append('> — Slag Champion Barok, Master of the Grand Battle Pits\n\n')
    sections.append('---\n\n')
    
    # Chapter I
    sections.append("## Chapter I: The Volcanic Caldera & The Spires of Black Ash\n\n")
    sections.append("In the fourth month of Year 4238, after traversing two thousand four hundred kilometers across the singing glass of The Desolate, the Horizon Caravan crested the basalt ridge of the Ashen Rift. Rising before them in the scarlet dusk was the smoking crown of humanity's second sovereign sanctuary: **Cheonbulok (천불옥 / 千火獄) — The City of a Thousand Rages**.\n\n")
    sections.append("Constructed within the interior caldera of an active volcanic shield five kilometers wide, Cheonbulok lived in perpetual fire. Colossal aqueducts carved from volcanic basalt channeled rivers of liquid orange slag directly from the magma chambers into industrial smelting vats. Above the tiered stone dwellings, hundreds of iron smokestacks vomited thick black soot into a leaden sky, and the seismic thud of steam-driven drop hammers vibrated through the rock every three seconds like the heartbeat of an imprisoned colossus.\n\n")
    sections.append('"Atmospheric particulate density is five times higher than Somnarak," Hwaran reported, lowering her brass respirator as her coal-tinted eyes reflected the burning calderas. "No filtration bureaus here. No Council of Sighs telling people when to turn off their lanterns. Cheonbulok survives because everyone works the furnace, and everyone knows how to swing a sledge."\n\n')
    sections.append('"And if an outsider comes asking for passage to the western border?" Kael asked, checking the pneumatic seals on his duster.\n\n')
    sections.append('"Then the outsiders pay the Iron Tithe," Hwaran replied, pointing down to the center of the caldera where a massive amphitheater of blackened iron stood surrounded by roaring torches. "The Grand Battle Pit."\n\n')
    sections.append('---\n\n')
    
    # Chapter II
    sections.append("## Chapter II: The Doctrine of Wrath & The Grand Battle Pit\n\n")
    sections.append("The Drift Throne halted at the city's eastern causeway, guarded by two hundred armored warriors of the Furnace Guard wielding heavy steam-pistons and serrated iron billhooks. By order of **Furnace Keeper Bulhwa**, the caravan's passage toward the western desert could not be granted by paper treaties; under the ancient **Doctrine of Wrath**, any commander seeking the city's blessing was required to stand upon the crushed basalt sand of the arena and submit to combat trial.\n\n")
    sections.append("Kael stepped down into the center of the circular arena. Above him, fifty thousand foundry workers, smiths, and nomadic outcasts roared from the basalt tiers, banging heavy bronze wrenches against the iron railings in deafening, hypnotic synchronization. Across forty paces of black sand stood the undefeated master of the crucible: **Slag Champion Barok**.\n\n")
    sections.append("Standing nearly eight feet tall, Barok was encased in thick slabs of volcanic basalt bound with glowing copper rivets. At his chest hummed the **Combustion Furnace Core**, an internal coal-and-slag reactor that vented superheated steam from dual exhausts atop his shoulders. In his massive gauntlets, he dragged the **Boiling Iron Cleaver**, a five-foot slab of jagged Bessemer iron whose cutting edge dripped white-hot molten slag.\n\n")
    sections.append('"Hwaran!" Barok\'s vox-amplifier boomed, shaking the dust from the arena walls. "You fled across the salt like a runaway slave! And now you return riding a four-thousand-ton iron barge, hiding behind this grey-haired nomad?"\n\n')
    sections.append('---\n\n')
    
    # Chapter III
    sections.append("## Chapter III: The Ideological Clash of Slag and Resolve\n\n")
    sections.append("Kael unslung his Obsidian Trench-Cleaver, resting the four-foot blade against the black sand. His left arm of translucent Han-glass caught the orange torchlight, glowing faint cerulean against the suffocating heat.\n\n")
    sections.append('"She didn\'t run away, Barok," Kael spoke calmly, his gravelly voice carrying cleanly through the roaring arena. "She came looking for an answer. Your city has fed its sons and daughters into these smelting pits for four thousand years. You tell them that rage keeps the cold away. But you are running out of coal, and the caldera is cooling. Look at your furnace walls—the basalt is cracking."\n\n')
    sections.append('"Silence, outlander!" Barok roared, stepping forward as his chest furnace flared into blinding orange fury. "Our fury has kept Cheonbulok alive while Somnarak hid in underground holes like sewer rats! Fire is the only law the world understands! If you want passage through our gates, prove that your cold nomadic steel can survive the forge!"\n\n')
    sections.append('Barok kicked a cloud of incandescent basalt dust into the air, swung the smoking cleaver in a terrifying overhead arc, and charged.\n\n')
    sections.append('---\n\n')
    
    # Chapter IV
    sections.append("## Chapter IV: Overland Arena Topology & Combat Engagement Parameters\n\n")
    sections.append("Sora the Blind sat at the arena perimeter catwalk, her acoustic visor tracking the gladiatorial arena's discrete spatial nodes:\n\n")
    
    grid_box = make_box("TACTICAL ARENA TOPOLOGY: CHEONBULOK GRAND BATTLE PIT", [
        "[STAGE NODES 01 TO 10 - ARENA VESTIBULE TO CENTRAL SLAG DAIS]",
        "[N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "---",
        "- Node 01: Ingress Pit Gates (Caravan Support Ramps & Cover)",
        "- Node 02: Vanguard Forward Sand (Kael Seismic Guard Stance)",
        "- Node 03: Hwaran Mid-Field Cover (Cinder-Staff & Steam Flare Post)",
        "- Node 04: Crushed Basalt Sand Margin (Boiling Slag Spatter Trench)",
        "- Node 05: The Slag Champion Barok (Central Arena Dais & Cleaver)",
        "- Node 06: Resonant Magma Flank (Molten Slag Aqueduct Runoff)",
        "- Node 07: Furnace Enforcer Catwalk (Marksmen Flank Suppression)",
        "- Node 08: Volcanic Fissure Chasm (Boiling Sulfur Steam Vent)",
        "- Node 09: Basalt Cathedra Arch (Furnace Keeper Bulhwa Balcony)",
        "- Node 10: Sovereign Foundry Dais (Western Gate Release Lever)"
    ])
    sections.append(wrap_box(grid_box))
    
    sections.append("Slag Champion Barok wielded extreme thermal power, utilizing the **Boiling Iron Cleaver** to melt armor defenses while venting steam from his **Combustion Core**. Kael's gladiatorial strategy required parrying the cleaver's downward smash to induce thermal backlash into Barok's forearm actuators, breaking the weapon, cracking the **Basalt Pauldrons**, and puncturing the chest furnace's pressure relief valves.\n\n")
    sections.append('---\n\n')
    
    # Chapter V: Combat Gauntlet (Turns 01 to 06)
    sections.append("## Chapter V: The Expedition Combat Gauntlet (Turns 01 to 06)\n\n")
    
    # Turn 01 HUD
    t1_hud = make_box("TACTICAL STAGE HUD: ARC 03 - BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 - CHEONBULOK GRAND BATTLE PIT]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[GATES] [SAND]  [COVER] [MARGIN][DAIS]  [MAGMA] [C-WALK][CHASM][ARCH]  [LEVER]",
        "[KAEL]  [HWARAN]                [BAROK]                                [BULHWA]",
        "---",
        "- Node 01: Ingress Arena Gates / Caravan Entryway",
        "- Node 02: Kael (Vanguard Band 1 / Han-Glass Guard Stance)",
        "- Node 03: Hwaran (Short Band 2 / Cinder-Staff Support)",
        "- Node 04: Crushed Basalt Sand Margin (Boiling Slag Hazard)",
        "- Node 05: Slag Champion Barok (Boiling Cleaver & Chest Core)",
        "- Node 06: Magma Runoff Conduits (Ambient 300°C Thermal Waves)",
        "- Node 09: Bulhwa's Balcony (Chief Furnace Keeper Overseeing)",
        "---",
        "- Kael (Drift King): Spd 6 -> 3 AP | HP 4,200/4,200 | SP 50/50 | Posture 160/160",
        "- Hwaran (Guide)   : Spd 7 -> 4 AP | HP 2,800/2,800 | SP 45/45 | Posture 120/120",
        "- Barok Core       : Spd 5 -> 3 AP | HP 2,500/2,500 | Posture 380/380 [FRENZY]",
        "- Boiling Cleaver  : Spd 7 -> 4 AP | HP 1,500/1,500 | Posture 300/300 [MOLTEN]",
        "- Basalt Pauldron  : Spd 3 -> 1 AP | HP 1,800/1,800 | Posture 340/340 [ARMORED]"
    ])
    sections.append(wrap_box(t1_hud))
    
    sections.append("### Turn 01 Action Resolution Log (Intercepting the Molten Slag Cleave)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Kael initializes `[Han-Glass Thermal Ward]`: Left arm crystallizes, absorbing incoming thermal damage and converting it into kinetic poise.\n")
    sections.append("  * Hwaran prepares `[Cinder-Staff Dispersion Flare]`: Dampens ambient heat waves across Node 02.\n")
    sections.append("  * Barok activates `[Crucible Overdrive]`: Increases attack power by +4 for every point of Posture strain he suffers.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael (Speed 6 -> 3 AP): Holds Node 02. Spends 2 AP on `[Trench-Cleaver: Kinetic Intercept]`. Holds 1 AP in Guard.\n")
    sections.append("  * Hwaran (Speed 7 -> 4 AP): Holds Node 03. Spends 2 AP on `[Quenching Steam Flare]`. Spends 2 AP on `[Weakpoint Dart]`.\n")
    sections.append("  * Barok (Speed 7 -> 4 AP): Charges from Node 05 to Node 02. Spends 2 AP on `[Boiling Cleave: Slag Eruption]`. Spends 2 AP on `[Chest Vent Blast]`.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 02 to 05)**: Barok swings `[Boiling Cleave: Slag Eruption]` (Base 19 + 2 Coins = 29 Power, Heavy Heat/Slash).\n")
    sections.append("    * Kael intercepts with `[Trench-Cleaver: Kinetic Intercept]` (Base 22 + 2 Coins = 34 Power, Obsidian Heavy Blade).\n")
    sections.append("    * **Clash Outcome**: Kael WINS THE CLASH OVERWHELMINGLY (34 vs 29)!\n")
    sections.append("    * Kael's obsidian blade catches the white-hot cleaver; the molten iron sprays across the sand like fireworks (`[P3: Parry/Protection]`).\n")
    sections.append("    * Kael's glass arm shudders with seismic frequency, reflecting **310 kinetic tremor damage** into the cleaver's hilt, inflicting +62 Posture Strain!\n")
    sections.append("  * **Clash 2 (Node 03 to 05)**: Hwaran's `[Quenching Steam Flare]` extinguishes Barok's chest vent flash instantly!\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Boiling Cleaver HP: 1,500 -> **1,190/1,500** | Posture: **238/300**.\n")
    sections.append("  * Total Champion HP: 5,800 -> **5,490/5,800** | Posture: **318/380**.\n")
    sections.append("  * Kael Composure: **100% (50/50 SP)**. Zero damage taken.\n\n")
    sections.append('---\n\n')
    
    # Turn 02 HUD
    t2_hud = make_box("TACTICAL STAGE HUD: ARC 03 - BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 - BOILING CLEAVER SHATTERED & VOID STRIKE]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[GATES] [SAND]  [COVER] [MARGIN][DAIS]  [MAGMA] [C-WALK][CHASM][ARCH]  [LEVER]",
        "        [KAEL]  [HWARAN]        [BAROK]                                [BULHWA]",
        "---",
        "- Node 02: Kael (Advancing / Trench-Cleaver Severing Forearm Piston)",
        "- Node 03: Hwaran (Cryo-Brine Grenade Cracking Superheated Iron)",
        "- Node 05: Slag Champion Barok (Boiling Cleaver Destroyed 0/1,500 HP)",
        "- Node 06: Resonant Lens (Tagging Weakened Basalt Pauldron Brackets)",
        "- Node 09: Bulhwa's Balcony (Silence Descending on the Spectators)",
        "---",
        "- Kael (Drift King): Spd 8 -> 4 AP [SURGE] | HP 4,200/4,200 | SP 50/50 | Posture 160/160",
        "- Hwaran (Guide)   : Spd 9 -> 5 AP         | HP 2,800/2,800 | SP 45/45 | Posture 120/120",
        "- Barok Core       : Spd 3 -> 1 AP         | HP 2,500/2,500 | Posture 268/380",
        "- Boiling Cleaver  : DESTROYED (0/1,500 HP)| MOLTEN SLAG CLEAVE PERMANENTLY LOST",
        "- Basalt Pauldron  : Spd 3 -> 1 AP         | HP 1,440/1,800 | Posture 262/340"
    ])
    sections.append(wrap_box(t2_hud))
    
    sections.append("### Turn 02 Action Resolution Log (Part Destruction: Boiling Cleaver Shattered)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Kael activates `Tectonic Momentum` (+2 Speed next turn -> Net Speed 8, 4 AP).\n")
    sections.append("  * Barok channels `[Caldera Earth-Breaker]` to crack the entire arena floor in a wave of liquid magma.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael (Speed 8 -> 4 AP [Surge]): Steps to Node 03. Spends 3 AP on `[Obsidian Cleaver: Thermal Severance]`. Holds 1 AP in Guard.\n")
    sections.append("  * Hwaran (Speed 9 -> 5 AP): Spends 3 AP on `[Cryo-Brine Quenching Grenade]`. Spends 2 AP on `[Flank Support]`.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 03 to 05)**: Barok slams with `[Caldera Earth-Breaker]` (Base 20 + 2 Coins = 28 Power, Area Heat/Weight).\n")
    sections.append("    * Kael clashes with `[Obsidian Cleaver: Thermal Severance]` (Base 26 + 3 Coins Heads = 45 Power, Heavy Weight/Shatter).\n")
    sections.append("    * **Clash Outcome**: Kael WINS THE CLASH OVERWHELMINGLY (45 vs 28)!\n")
    sections.append("    * Hwaran's cryo-brine grenade flash-freezes the glowing cleaver blade; as Kael's cleaver strikes, the superheated iron shatters like brittle glass!\n")
    sections.append("    * Deals **1,190 Critical Shatter damage** (Weight 2.0x proc!)!\n")
    sections.append("    * **TARGETED PART DESTROYED**: The Boiling Iron Cleaver is completely destroyed (**Cleaver HP: 0/1,500** credit)!\n")
    sections.append("    * **EFFECT**: Boss magma earth-breaker permanently cancelled; boss permanently loses 1 Speed Slot!\n")
    sections.append("  * **Basalt Pauldron Damage**:\n")
    sections.append("    * Thermal shock fractures the left shoulder plate for **360 Blunt damage**!\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Boiling Cleaver: **DESTROYED (0/1,500 HP)**.\n")
    sections.append("  * Basalt Pauldron: 1,800 -> **1,440/1,800** | Posture: **262/340**.\n")
    sections.append("  * Total Champion HP: 5,490 -> **3,940/5,800** | Posture: **212/380 [CLEAVER SHATTERED]**.\n")
    sections.append("  * Kael Composure: Stable (50/50 SP).\n\n")
    sections.append('---\n\n')
    
    # Turn 03 HUD
    t3_hud = make_box("TACTICAL STAGE HUD: ARC 03 - BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 - STAGGER THRESHOLD 1 & PAULDRON SHATTER]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[GATES] [SAND]  [COVER] [MARGIN][DAIS]  [MAGMA] [C-WALK][CHASM][ARCH]  [LEVER]",
        "                [KAEL]  [HWARAN][BAROK]                                [BULHWA]",
        "---",
        "- Node 03: Kael (Han-Glass Fist Driving into Exposed Shoulder Struts)",
        "- Node 04: Hwaran (Pneumatic Ram Shattering Volcanic Basalt Plates)",
        "- Node 05: Slag Champion Barok (STAGGER LEVEL 1 / DEFENSES COLLAPSED)",
        "- Node 09: Bulhwa's Balcony (Fifty Thousand Spectators Falling Mute)",
        "---",
        "- Kael (Drift King): Spd 8 -> 4 AP [SURGE] | HP 4,200/4,200 | SP 50/50 | Posture 160/160",
        "- Hwaran (Guide)   : Spd 8 -> 4 AP         | HP 2,800/2,800 | SP 45/45 | Posture 120/120",
        "- Barok Core       : Spd 0 -> 0 AP         | HP 2,120/2,500 | Posture 146/380 [STAGGER LEVEL 1]",
        "- Basalt Pauldron  : Spd 0 -> 0 AP         | HP 680/1,800   | Posture 98/340 [SHATTERED]",
        "- Total Champion   : HP 2,800/5,800 [THRESHOLD BREACHED / TAKES 1.5X DAMAGE]"
    ])
    sections.append(wrap_box(t3_hud))
    
    sections.append("### Turn 03 Action Resolution Log (First Stagger Proc & Basalt Pauldron Shattered)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Disarmed, Barok lowers his basalt shoulders and charges forward with `[Volcanic Battering Ram]`.\n")
    sections.append("  * Kael gains `Tectonic Surge` (+2 Speed -> Net Speed 8, 4 AP).\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael (Speed 8 -> 4 AP): Moves to Node 03. Spends 2 AP on `[Glass Fist: Bedrock Counter]`. Spends 2 AP on `[Seismic Cleave]`.\n")
    sections.append("  * Hwaran (Speed 8 -> 4 AP): Advances to Node 04. Spends 2 AP on `[Pneumatic Ram]`.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 03 to 05)**: Barok charges with `[Volcanic Battering Ram]` (Base 18 + 2 Coins = 26 Power, Heavy Weight/Heat).\n")
    sections.append("    * Kael clashes with `[Glass Fist: Bedrock Counter]` (Base 23 + 2 Coins = 35 Power, Seismic Weight).\n")
    sections.append("    * **Clash Outcome**: Kael WINS THE CLASH (35 vs 26)!\n")
    sections.append("    * Kael's glass arm meets Barok's charging shoulder; the kinetic impact rings through the caldera like a cracked bell!\n")
    sections.append("    * Drone-assisted pneumatic rams shatter the volcanic basalt plates into black gravel, exposing the glowing combustion core in his chest!\n")
    sections.append("    * Deals **820 Void/Shatter damage** and +116 Posture Strain!\n")
    sections.append("- **Step 4: STAGGER THRESHOLD 1 TRIGGERED!**:\n")
    sections.append("  * Total Champion HP crosses 70% threshold (4,060 HP), falling to **2,800/5,800 HP**; Posture crosses 60% strain line!\n")
    sections.append("  * **STAGGER LEVEL 1 ACTIVE!** Barok drops to one knee on the arena sand, gasping for breath; chest combustion furnace exposed; takes +50% damage across all incoming attacks!\n")
    sections.append("- **Step 5: Turn End State**:\n")
    sections.append("  * Total Champion HP: 3,940 -> **2,800/5,800 [THRESHOLD BREACHED: Below 4,060 HP!]**.\n")
    sections.append("  * Basalt Pauldron: 1,440 -> **680/1,800** | Posture: **98/340 [SHATTERED]**.\n")
    sections.append("  * Boss Posture: **146/380 [STAGGER LEVEL 1]**.\n")
    sections.append("  * Kael Status: Unbroken.\n\n")
    sections.append('---\n\n')
    
    # Turn 04 HUD
    t4_hud = make_box("TACTICAL STAGE HUD: ARC 03 - BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 - MAXIMUM BURST & PHASE 2 THRESHOLD SKIP]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[GATES] [SAND]  [COVER] [MARGIN][DAIS]  [MAGMA] [C-WALK][CHASM][ARCH]  [LEVER]",
        "                        [KAEL]  [BAROK] [HWARAN]                       [BULHWA]",
        "---",
        "- Node 04: Kael (Four-Fold Cleaver Execution on Exposed Combustion Core)",
        "- Node 05: Slag Champion Barok (Immobilized / Steam Valves Venting Wildly)",
        "- Node 06: Hwaran (Cryo-Brine Concentrated Discharge on Fuel Manifold)",
        "- Node 09: Bulhwa's Balcony (The Furnace Keeper Standing in Awe)",
        "---",
        "- Kael (Drift King): Spd 11 -> 5 AP [BURST CRIT] | HP 4,200/4,200 | SP 50/50",
        "- Barok Core       : Spd 0 -> 0 AP               | HP 680/2,500   | Posture 58/380",
        "- Basalt Pauldron  : DESTROYED (0/1,800 HP)",
        "- Total Champion   : HP 680/5,800 [BURST DAMAGE 2,120! SECOND THRESHOLD SKIPPED]"
    ])
    sections.append(wrap_box(t4_hud))
    
    sections.append("### Turn 04 Action Resolution Log (Maximum Burst & Phase 2 Threshold Skip)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Barok remains stunned on one knee; his chest furnace vents screaming orange flames as his heat regulators fail.\n")
    sections.append("  * Kael coordinates an all-out offensive barrage targeting the exposed reactor.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael (Speed 11 -> 5 AP, Momentum Crit): Stands at Node 04. Spends 3 AP on `[Four-Fold Cleaver Execution]`. Spends 2 AP on `[Seismic Impact]`.\n")
    sections.append("  * Hwaran: Delivers `[Cryo-Brine Core Sapper]` (3 AP).\n")
    sections.append("- **Step 3: Unopposed Stagger Punishment Rotation**:\n")
    sections.append("  * Kael's `[Four-Fold Cleaver Execution]`: Rips through the combustion heart for **1,140 Heavy Weight damage** (Fatal 2.0x proc!)!\n")
    sections.append("  * Kael's `[Seismic Impact]`: Slices through the remaining armor plates for **500 Shatter damage**!\n")
    sections.append("  * Hwaran's `[Cryo-Brine Sapper]`: Freezes the secondary injector lines for **480 Cold/Void damage**!\n")
    sections.append("  * **TOTAL BURST DAMAGE: 2,120 DAMAGE!**\n")
    sections.append("- **Step 4: SECOND STAGGER THRESHOLD (2,320 HP) COMPLETELY SKIPPED!**:\n")
    sections.append("  * Champion HP plunges from 2,800 down to **680/5,800 HP**! Basalt Pauldron completely destroyed (0/1,800 HP)!\n")
    sections.append("  * **Phase 2 Emergency Activation Triggered!**\n")
    sections.append("- **Step 5: Turn End State**:\n")
    sections.append("  * Total Champion HP: 2,800 -> **680/5,800** (Core HP: **680/2,500** | Armor: **DESTROYED**).\n")
    sections.append("  * Posture: **58/380**.\n\n")
    sections.append('---\n\n')
    
    # Turn 05 HUD
    t5_hud = make_box("TACTICAL STAGE HUD: ARC 03 - BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 - VOLCANIC CATACLYSM & THE DRIFT KING'S MERCY]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[GATES] [SAND]  [COVER] [MARGIN][DAIS]  [MAGMA] [C-WALK][CHASM][ARCH]  [LEVER]",
        "                                [KAEL]  [BAROK] [HWARAN]               [BULHWA]",
        "---",
        "- Node 05: Kael (Relic Overdrive: PROMISE OF THE HORIZON SOVEREIGN)",
        "- Node 06: Slag Champion Barok (Last Stand: Superheated Slag Self-Immolation)",
        "- Node 07: Hwaran (Deploying Steam Barrier to Shield Spectators)",
        "- Node 09: Bulhwa's Balcony (Keeper Raising Hand to Halt Enforcers)",
        "---",
        "- Kael (Drift King): Spd 9 -> 5 AP [OVERDRIVE] | HP 4,200/4,200 | SP 50/50 [RESOLVE]",
        "- Barok Core       : Spd 3 -> 1 AP             | HP 680/2,500   | Posture 28/380 [OVERHEATED]",
        "- Total Champion   : HP 680/5,800 [SLAG IMMOLATION DEFLECTED / BAROK SUBDUED]"
    ])
    sections.append(wrap_box(t5_hud))
    
    sections.append("### Turn 05 Action Resolution Log (Phase 2 Escalation: Superheated Slag & Horizon Mercy)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Barok rises in suicidal gladiatorial pride; his chest reactor blows all safety vents in an incandescent eruption of molten slag!\n")
    sections.append("  * Boss Special Skill: `[Superheated Slag Immolation]` (Volcanic Cataclysm, 3 Coins).\n")
    sections.append("  * Kael activates Relic Overdrive: `[PROMISE OF THE HORIZON SOVEREIGN — MAXIMUM]` (Cost: 3 AP, 30 SP).\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael (Speed 9 -> 5 AP [Overdrive]): Steps straight onto the central dais at Node 05, raising his glass arm.\n")
    sections.append("  * Hwaran: Deploys steam barriers at Node 07 to protect the front-row spectators.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 05 to 06)**: Barok discharges `[Superheated Slag Immolation]` (Base 23 + 3 Coins = 35 Power, Area Heat/Void).\n")
    sections.append("    * Kael clashes with `[PROMISE OF THE HORIZON SOVEREIGN — MAXIMUM]` (Base 30 + 3 Coins Heads = 51 Power, Seismic Quenching).\n")
    sections.append("    * **Clash Outcome**: KAEL OVERWHELMING RELIC CLASH WIN (51 vs 35)!\n")
    sections.append("    * Kael's glass arm plunges directly into Barok's open chest furnace, driving a pulse of absolute acoustic zero into the coal core (`[P3: Parry/Protection]`).\n")
    sections.append("    * The roaring flames collapse into cool, black slag; Kael catches the fainting giant before he strikes the sand!\n")
    sections.append('    * Kael whispers: *"Your fight is done, champion. Save your strength for the furnace below."*\n')
    sections.append("    * Barok's reactor falls silent! Zero caravan or spectator casualties taken!\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Total Champion HP: **680/5,800** | Posture: **28/380 [OVERHEATED]**.\n")
    sections.append("  * Kael Composure: 50/50 SP.\n\n")
    sections.append('---\n\n')
    
    # Turn 06 HUD
    t6_hud = make_box("TACTICAL STAGE HUD: ARC 03 - BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 - GLADIATORIAL VICTORY & CITADEL TREATY]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[GATES] [SAND]  [COVER] [MARGIN][DAIS]  [MAGMA] [C-WALK][CHASM][ARCH]  [LEVER]",
        "                                [KAEL]  [BAROK] [HWARAN]       [BULHWA][TREATY]",
        "---",
        "- Node 05: Slag Champion Barok (PACIFIED & YIELDING WITH SOLEMN HONOR)",
        "- Node 09: Furnace Keeper Bulhwa (Proclaiming the Horizon Caravan's Victory)",
        "- Node 10: Ingress to the Sacred Great Furnace Core (-800m OPEN)",
        "---",
        "- Kael Status: Zero Damage Taken | Composure 50/50 SP (Unshakable Authority)",
        "- Expedition Status: ARENA WON | Citadel Treaty Signed | Core Descent Ingress"
    ])
    sections.append(wrap_box(t6_hud))
    
    sections.append("### Turn 06 Action Resolution Log (Gladiatorial Victory & Treaty Ingress)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Hostile intent drops to zero. Posture reaches **0/380 [GLADIATORIAL SUBMISSION]**.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael helps Barok stand, resting the titan against the stone dais.\n")
    sections.append("- **Step 3: Proclamation & Treaty**:\n")
    sections.append("  * The fifty thousand spectators rise to their feet in absolute, thunderous ovation, hammering their tools against the iron railings until the caldera roars.\n")
    sections.append('  * From the high balcony, Furnace Keeper Bulhwa strikes the Great Bronze Gong of Year Zero:\n')
    sections.append('    > *"The outlander has endured the slag. He carries neither fear nor cruelty. By the Law of the Forge, the Horizon Caravan is proclaimed Kin of the Ash!"*\n')
    sections.append("  * Deals **680 Decisive Honor**! Barok HP drops to 0!\n")
    sections.append("- **Step 4: Operational Artifact Extraction & Core Ingress**:\n")
    sections.append("  * **Tactical Requisition Acquired**: `[Overland Module: Molten Slag Core]` (Grants +30% Thermal Damage to caravan weapons and enables geothermal energy siphoning).\n")
    sections.append("  * **Descent Ingress**: Bulhwa lowers the iron drawbridge at Node 10, granting Kael and Hwaran immediate access to **The Sacred Great Furnace Core (-800m)**.\n")
    sections.append("  * **Casualties**: Zero Damage Taken. Kael HP 4,200/4,200. Composure 50/50 SP.\n\n")
    sections.append('---\n\n')
    
    # Chapter VI: The Gladiator's Kneeling & The Pact of Ash and Sand
    sections.append("## Chapter VI: The Gladiator's Kneeling & The Pact of Ash and Sand\n\n")
    sections.append("Barok sat upon the black basalt bench in the gladiatorial infirmary, drinking cold well-water as an Ash Iron surgeon dressed the steam burns across his ribs. The boiling cleaver was gone, but the manic rage that had twisted his features for twenty years had softened into tired, contemplative dignity.\n\n")
    sections.append('"You hit like a hydraulic drop hammer, nomad," Barok chuckled hoarsely, coughing up flecks of black cinder. "My grandfather built that cleaver. He told me that if I ever let the metal cool, Cheonbulok would die."\n\n')
    sections.append('Kael leaned against the armory rack, cleaning the basalt grit from his trench-cleaver. "Your grandfather was trying to keep you alive through the long winter, Barok. But keeping the furnace burning doesn\'t mean burning yourself on the grate. The mountain beneath your feet is fracturing. If we don\'t stabilize the core, there won\'t be an arena left to fight in."\n\n')
    sections.append('Furnace Keeper Bulhwa stepped into the armory, his ceremonial mantle of scorched leather heavy with iron keys. "The nomad speaks the truth, Barok. The deep thermal conduits are venting boiling brine. The fire is no longer obeying our rites. We must descend."\n\n')
    sections.append('---\n\n')
    
    # Chapter VII: Operational Requisition Harvest & Ingress to the Foundry Core
    sections.append("## Chapter VII: Operational Requisition Harvest & Ingress to the Foundry Core\n\n")
    sections.append("The caravan smiths transferred three tons of specialized geothermal insulation from the Drift Throne to the descent hoists:\n\n")
    
    reward_box = make_box("OVERLAND REQUISITION HARVEST: ARC 03", [
        "ACQUIRED SALVAGE     : Master Barok's Superheated Slag Ingot & Crucible Key",
        "UPGRADE DESIGNATION  : [Overland Module: Molten Slag Core]",
        "CARAVAN SPEED STATUS : Anchored at Cheonbulok Citadel Causeway",
        "---",
        "FLAGSHIP SYSTEM ENHANCEMENTS:",
        "1. Thermal Siphon    : Ley-drive can harvest energy directly from volcanic",
        "                     hot-spots, eliminating track-freeze in cold deserts.",
        "2. Slag-Forged Ammo  : Marksmen weapons deal +25% bonus Stagger against",
        "                     heavily armored subterranean chitin.",
        "3. Citadel Bastion   : Drift Throne forward hull reinforced with Cheonbulok",
        "                     refractory basalt tiles (+20% Defense).",
        "---",
        "NEXT TARGET DESCENT:",
        "- The Sacred Great Furnace Core (-800m) — The Source of Cheonbulok's Rage"
    ])
    sections.append(wrap_box(reward_box))
    
    sections.append("Kael, Hwaran, and Keeper Bulhwa stepped onto the heavy industrial cargo lift. With a grinding shriek of counterweights, the platform plummeted into the volcanic bowels of the mountain.\n")
    
    return "".join(sections)

def build_arc_4():
    sections = []
    
    # Title & Subtitle
    sections.append("# Arc 4: The Furnace's Secret — The Sacred Great Furnace (화로의 비밀 — 거대 화로 심층)\n")
    sections.append("## The Horizon Caravan Chronicles — Planetary Overland Expedition (Year 4238, Month 5)\n\n")
    
    # Operational Attribute Table
    sections.append("| Operational Attribute | Specification Dossier |\n")
    sections.append("|---|---|\n")
    sections.append("| **Campaign Theater** | The Horizon Caravan (지평선대 — Jipyeongseondae) |\n")
    sections.append("| **Arc Designation** | Arc 4: The Furnace's Secret — Sacred Core (거대 화로 심층) |\n")
    sections.append("| **Overland Sector** | Cheonbulok Sub-Core Caldrons (-800m Magma Chamber) |\n")
    sections.append("| **Threat Rating** | UTS-4 (Cataclysmic Volcanic Han-Reactor Meltdown) |\n")
    sections.append("| **Deploying Unit** | Kael (Drift King), Hwaran, & Keeper Bulhwa |\n")
    sections.append("| **Primary Opponent** | The Blazing Heart of Sorrow (타오르는 슬픔의 심장 — SECC-099) |\n")
    sections.append("| **Stagger Profile** | 60% Posture Strain (Vent Break) / 0% Posture (Harmonization) |\n")
    sections.append("| **Operational Yield** | Han-Reactor Stabilization & The Flame of Solace |\n\n")
    
    # Master Dossier Box
    dossier = make_box("EXPEDITION DOSSIER: ARC 4 - THE FURNACE'S SECRET", [
        "OPERATION NAME     : Arc 4 - The Heart of the Great Furnace",
        "PRIMARY THEATER    : Cheonbulok - The Sacred Furnace Core",
        "DATE & EPOCH       : Year 4238, Month 5 (Deep Foundry Infiltration)",
        "PRIMARY ADVERSARY  : The Blazing Heart of Sorrow (Sentient Magma Core)",
        "---",
        "ADVERSARY PROFILE (THE BLAZING HEART OF SORROW):",
        "- Total Health (HP): 6,200 HP | Posture Pool: 400/400",
        "- Stagger 1 Proc   : 60% Posture Strain (240 Posture) / Vent Break",
        "- Stagger 2 Proc   : 0% Posture Collapse (Thermal Re-Harmonization)",
        "- Resistances      : Void 2.0x (Fatal), Lament 1.5x, Heat 0.5x, Weight 0.5x",
        "---",
        "TARGETABLE COMBAT ANCHORS:",
        "1. Rupture Vents   : 1,600 HP | Posture 320/320 (Boiling magma jet array)",
        "2. Slag Crucible   : 1,900 HP | Posture 360/360 (Heavy molten iron mantle)",
        "3. Grief Spark     : 2,700 HP | Posture 400/400 (Central unquenched tears)"
    ])
    sections.append(wrap_box(dossier))
    
    # Epigraph Quote
    sections.append('> *"For four thousand years, we told ourselves that Cheonbulok was angry. We built our laws on fury, threw our brothers into the battle pits, and poured boiling slag into the sand. But the furnace wasn\'t raging at us. The furnace was crying."*\n')
    sections.append('> — Furnace Keeper Bulhwa, inside the Sacred Core\n\n')
    sections.append('---\n\n')
    
    # Chapter I
    sections.append("## Chapter I: The Deep Caldrons & The Screaming Slag (-800m)\n\n")
    sections.append("Descending past the industrial foundations of Cheonbulok brought Kael, Hwaran, and Furnace Keeper Bulhwa into a subterranean abyss of unimaginable thermal fury at depth -800 meters: **The Sacred Great Furnace Core**. The ambient air temperature exceeded 600°C. Even with specialized refractory asbestos coats and pressurized thermal rebreathers, the heat pressed against their chests like a physical iron anvil.\n\n")
    sections.append("Cyclopean fissures thirty meters long crawled across the ancient adamantine crucible walls. Rivers of white-hot liquid steel cascaded from hanging caldrons into a bottomless subterranean chasm. Four hundred civilian foundry workers—the Ash Walkers—stood trapped on buckling maintenance catwalks at the center of the lake, surrounded by advancing walls of magma.\n\n")
    sections.append('"The tectonic containment field has collapsed eighty percent," Hwaran yelled through her respirator, pointing her cinder-staff at the central abyss. "The magma is not flowing from planetary mantle convection! It is boiling out of an ancient Han-Relic reactor embedded in the bedrock before Year Zero!"\n\n')
    sections.append('"We thought it was the fire of the earth," Bulhwa whispered in horror, falling to his knees as the heat blistered his gloves. "Our ancestors found this furnace sleeping in the stone and built the city above it to stay warm. We thought it wanted sacrifices. We thought it wanted wrath."\n\n')
    sections.append('---\n\n')
    
    # Chapter II
    sections.append("## Chapter II: The Cracking Crucible & The Blazing Heart of Sorrow\n\n")
    sections.append("Floating in the center of the boiling magma lake was **The Blazing Heart of Sorrow (타오르는 슬픔의 심장 — SECC-099)**. Standing nearly eight meters in diameter, the sovereign entity was a colossal sphere of pulsing liquid grief encased within the **Slag Crucible Mantle**—a shell of molten Before-Time iron that bubbled and hissed under continuous volcanic pressure.\n\n")
    sections.append("Protruding from its upper hemisphere was the **Thermal Rupture Vent Array**, six massive basalt pipes that vomited geysers of superheated magma straight toward the ceiling, threatening to cause a total caldera collapse that would swallow the eighty thousand citizens of Cheonbulok into a tomb of molten rock. At its luminous center, visible through cracks in the slag, burned the **Grief Spark**, an unquenched core of pure, boiling tears that emitted a deafening, acoustic screech that shattered the surrounding stone.\n\n")
    sections.append('"Listen to the frequency!" Hwaran shouted, her acoustic calipers registering extreme decibel strain. "It isn\'t the sound of wrath! It\'s the acoustic frequency of a human crying while burning alive! The reactor was seeded with the memories of the workers who sealed the calderas during the cataclysm! They have been burning in the dark for four thousand years!"\n\n')
    sections.append('---\n\n')
    
    # Chapter III
    sections.append("## Chapter III: The Dialectic of Fire and Weeping\n\n")
    sections.append("Kael stepped out onto the narrow catwalk above the magma lake, his obsidian cleaver glowing red in the thermal gale. His left arm of translucent Han-glass hummed at maximum harmonic inversion, radiating a sphere of cool, protective cerulean light that quenched the blistering heat around his boots.\n\n")
    sections.append('"Bulhwa!" Kael called out over the roar of the geysers. "For four thousand years, your people answered this entity\'s screams with more violence! You threw blood into the pit, screamed into the dark, and called it the Doctrine of Wrath! But fire cannot quench fire! A weeping soul does not need more iron; it needs someone to hear its grief!"\n\n')
    sections.append('"Can we extinguish it?" Bulhwa cried desperately. "If the fire dies, Cheonbulok freezes in the winter desert!"\n\n')
    sections.append('"We don\'t extinguish it," Kael answered, leaping across the cracking catwalk toward the central crucible. "We harmonize it! Hwaran, open the cryo-siphons! We are putting this ancient fire to rest!"\n\n')
    sections.append('---\n\n')
    
    # Chapter IV
    sections.append("## Chapter IV: Overland Arena Topology & Combat Engagement Parameters\n\n")
    sections.append("Hwaran calibrated the tactical grid across the narrow industrial catwalks spanning the magma chamber:\n\n")
    
    grid_box = make_box("TACTICAL ARENA TOPOLOGY: CHEONBULOK FURNACE CORE (-800M)", [
        "[STAGE NODES 01 TO 10 - INGRESS CATWALK TO CENTRAL CRUCIBLE]",
        "[N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "---",
        "- Node 01: Ingress Lift Hoist (Safety Anchor & Thermal Buffer)",
        "- Node 02: Vanguard Forward Catwalk (Kael Cryo-Prismatic Stance)",
        "- Node 03: Support Pylon Station (Hwaran Cryo-Brine Siphon Array)",
        "- Node 04: Trapped Ash Walker Line (400 Civilian Foundry Workers)",
        "- Node 05: The Blazing Heart of Sorrow (Central Molten Crucible)",
        "- Node 06: Rupture Vent Perimeter (Superheated Magma Geyser Jets)",
        "- Node 07: Slag Drainage Flue (Boiling Liquid Steel Runoff)",
        "- Node 08: Deep Caldera Fissure (Tectonic Pressure Fault Line)",
        "- Node 09: Adamantine Core Pylon (Structural Shoring Column)",
        "- Node 10: Exhaust Flue Override (Emergency Caldera Heat Valve)"
    ])
    sections.append(wrap_box(grid_box))
    
    sections.append("The Blazing Heart unleashed lethal wide-area thermal damage through its **Rupture Vents**, threatening to melt the civilian catwalks at Node 04. Kael's combat protocol prioritized severing the vent manifolds to eliminate the magma eruptions, cracking the **Slag Crucible Mantle** with cryo-brine shocks, and reaching the **Grief Spark** to achieve thermal harmonization.\n\n")
    sections.append('---\n\n')
    
    # Chapter V: Combat Gauntlet (Turns 01 to 06)
    sections.append("## Chapter V: The Expedition Combat Gauntlet (Turns 01 to 06)\n\n")
    
    # Turn 01 HUD
    t1_hud = make_box("TACTICAL STAGE HUD: ARC 04 - BATTLE TURN 01", [
        "[STAGE NODES 01 TO 10 - CHEONBULOK FURNACE CORE (-800M)]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[HOIST] [C-WALK][PYLON] [CIVIL] [HEART] [VENTS] [FLUE]  [CHASM][COLUMN][VALVE]",
        "[KAEL]  [HWARAN]        [WORK]  [BLAZE]                                [BULHWA]",
        "---",
        "- Node 01: Ingress Lift Hoist / Safety Buffer",
        "- Node 02: Kael (Vanguard Band 1 / Cryo-Quenching Stance)",
        "- Node 03: Hwaran (Support Band 2 / Cryo-Brine Siphon Array)",
        "- Node 04: Trapped Ash Walkers (400 Foundry Workers Under Threat)",
        "- Node 05: The Blazing Heart (Rupture Vents & Slag Crucible)",
        "- Node 06: Thermal Rupture Vents (Firing 600°C Magma Geysers)",
        "- Node 10: Exhaust Flue Override (Keeper Bulhwa Operating Valve)",
        "---",
        "- Kael (Drift King): Spd 6 -> 3 AP | HP 4,200/4,200 | SP 50/50 | Posture 160/160",
        "- Hwaran (Guide)   : Spd 7 -> 4 AP | HP 2,800/2,800 | SP 45/45 | Posture 120/120",
        "- Heart Core       : Spd 5 -> 3 AP | HP 2,700/2,700 | Posture 400/400 [MELTDOWN]",
        "- Rupture Vents    : Spd 7 -> 4 AP | HP 1,600/1,600 | Posture 320/320 [GEYSER]",
        "- Slag Crucible    : Spd 3 -> 1 AP | HP 1,900/1,900 | Posture 360/360 [MOLTEN]"
    ])
    sections.append(wrap_box(t1_hud))
    
    sections.append("### Turn 01 Action Resolution Log (Intercepting the Magma Geyser)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Kael initializes `[Cryo-Quenching Stance]`: Han-glass arm generates a sub-zero acoustic field granting +4 Protection and thermal immunity.\n")
    sections.append("  * Hwaran prepares `[Cryo-Brine Siphon]`: Pressurizes coolant lines to shield the trapped workers at Node 04.\n")
    sections.append("  * The Blazing Heart activates `[Meltdown Resonance]`: Surrounding temperature rises to 700°C.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael (Speed 6 -> 3 AP): Moves from Node 02 to Node 04 before the workers. Spends 2 AP on `[Trench-Cleaver: Thermal Intercept]`. Holds 1 AP in Guard.\n")
    sections.append("  * Hwaran (Speed 7 -> 4 AP): Holds Node 03. Spends 2 AP on `[Cryo-Brine Shield]`. Spends 2 AP on `[Siphon Jet]`.\n")
    sections.append("  * The Blazing Heart (Speed 7 -> 4 AP): Vents from Node 05 to Node 04. Spends 2 AP on `[Magma Geyser Eruption]`. Spends 2 AP on `[Slag Wave]`.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 04 to 05)**: The Blazing Heart fires `[Magma Geyser Eruption]` (Base 19 + 2 Coins = 29 Power, Area Heat/Lament).\n")
    sections.append("    * Kael intercepts with `[Trench-Cleaver: Thermal Intercept]` (Base 22 + 2 Coins = 34 Power, Obsidian Heavy Blade).\n")
    sections.append("    * **Clash Outcome**: Kael WINS THE CLASH OVERWHELMINGLY (34 vs 29)!\n")
    sections.append("    * Kael's cleaver splits the torrential jet of boiling magma cleanly, spraying the molten rock harmlessly into the drainage flues (`[P3: Parry/Protection]`).\n")
    sections.append("    * Kael's glass arm shudders with sub-zero acoustic resonance, reflecting **340 cryo-tremor damage** into the vent manifold, inflicting +66 Posture Strain!\n")
    sections.append("  * **Clash 2 (Node 03 to 04)**: Hwaran's `[Cryo-Brine Shield]` envelops the civilian catwalk, preventing all thermal injury!\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Rupture Vents HP: 1,600 -> **1,260/1,600** | Posture: **254/320**.\n")
    sections.append("  * Total Boss HP: 6,200 -> **5,860/6,200** | Posture: **334/400**.\n")
    sections.append("  * Kael Composure: **100% (50/50 SP)**. Zero worker casualties.\n\n")
    sections.append('---\n\n')
    
    # Turn 02 HUD
    t2_hud = make_box("TACTICAL STAGE HUD: ARC 04 - BATTLE TURN 02", [
        "[STAGE NODES 01 TO 10 - RUPTURE VENTS AMPUTATED & HEAT STRIKE]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[HOIST] [C-WALK][PYLON] [CIVIL] [HEART] [VENTS] [FLUE]  [CHASM][COLUMN][VALVE]",
        "        [HWARAN]        [WORK]  [KAEL]  [SHATTER]                      [BULHWA]",
        "---",
        "- Node 04: Trapped Workers (Retreating Across Shored Catwalks)",
        "- Node 05: Kael (Advancing / Obsidian Cleaver Severing Vent Manifold)",
        "- Node 06: The Blazing Heart (Rupture Vents Destroyed 0/1,600 HP)",
        "- Node 10: Exhaust Flue Override (Keeper Bulhwa Venting High Steam)",
        "---",
        "- Kael (Drift King): Spd 8 -> 4 AP [SURGE] | HP 4,200/4,200 | SP 50/50 | Posture 160/160",
        "- Hwaran (Guide)   : Spd 9 -> 5 AP         | HP 2,800/2,800 | SP 45/45 | Posture 120/120",
        "- Heart Core       : Spd 3 -> 1 AP         | HP 2,700/2,700 | Posture 282/400",
        "- Rupture Vents    : DESTROYED (0/1,600 HP)| MAGMA GEYSERS PERMANENTLY HALTED",
        "- Slag Crucible    : Spd 3 -> 1 AP         | HP 1,520/1,900 | Posture 284/360"
    ])
    sections.append(wrap_box(t2_hud))
    
    sections.append("### Turn 02 Action Resolution Log (Part Destruction: Rupture Vents Shattered)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Kael activates `Tectonic Momentum` (+2 Speed next turn -> Net Speed 8, 4 AP).\n")
    sections.append("  * The Blazing Heart attempts `[Cataclysmic Slag Eruption]` to collapse the entire cavern ceiling.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael (Speed 8 -> 4 AP [Surge]): Leaps to Node 05 directly onto the crucible rim. Spends 3 AP on `[Obsidian Cleaver: Manifold Severance]`. Holds 1 AP in Guard.\n")
    sections.append("  * Hwaran (Speed 9 -> 5 AP): Spends 3 AP on `[Cryo-Brine Core Flood]`. Spends 2 AP on `[Civilian Evacuation Cover]`.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 05 to 06)**: The Blazing Heart fires `[Cataclysmic Slag Eruption]` (Base 20 + 2 Coins = 28 Power, Area Heat/Weight).\n")
    sections.append("    * Kael clashes with `[Obsidian Cleaver: Manifold Severance]` (Base 26 + 3 Coins Heads = 45 Power, Heavy Void/Shatter).\n")
    sections.append("    * **Clash Outcome**: Kael WINS THE CLASH OVERWHELMINGLY (45 vs 28)!\n")
    sections.append("    * Kael's cleaver shears through the six basalt rupture pipes simultaneously; the pressurized steam and slag backfire into the core!\n")
    sections.append("    * Deals **1,260 Critical Void/Shatter damage** (Fatal 2.0x proc!)!\n")
    sections.append("    * **TARGETED PART DESTROYED**: The Thermal Rupture Vents are completely destroyed (**Vents HP: 0/1,600** credit)!\n")
    sections.append("    * **EFFECT**: Boss magma eruptions permanently halted; boss permanently loses 1 Speed Slot!\n")
    sections.append("  * **Slag Crucible Damage**:\n")
    sections.append("    * Cryo-brine deluge thermal-shocks the iron mantle for **380 Cold damage**!\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Rupture Vents: **DESTROYED (0/1,600 HP)**.\n")
    sections.append("  * Slag Crucible: 1,900 -> **1,520/1,900** | Posture: **284/360**.\n")
    sections.append("  * Total Boss HP: 5,860 -> **4,220/6,200** | Posture: **226/400 [VENTS SHATTERED]**.\n")
    sections.append("  * Kael Composure: Stable (50/50 SP).\n\n")
    sections.append('---\n\n')
    
    # Turn 03 HUD
    t3_hud = make_box("TACTICAL STAGE HUD: ARC 04 - BATTLE TURN 03", [
        "[STAGE NODES 01 TO 10 - STAGGER THRESHOLD 1 & CRUCIBLE CRACK]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[HOIST] [C-WALK][PYLON] [CIVIL] [HEART] [VENTS] [FLUE]  [CHASM][COLUMN][VALVE]",
        "                [HWARAN][SAFE]  [KAEL]  [CRACK]                        [BULHWA]",
        "---",
        "- Node 04: Trapped Workers (100% EVACUATED TO HOIST SAFETY)",
        "- Node 05: Kael (Seismic Han-Glass Fist Driving into Slag Mantle)",
        "- Node 06: The Blazing Heart (STAGGER LEVEL 1 / DEFENSES COLLAPSED)",
        "- Node 10: Exhaust Flue Override (Keeper Bulhwa Operating Valve)",
        "---",
        "- Kael (Drift King): Spd 8 -> 4 AP [SURGE] | HP 4,200/4,200 | SP 50/50 | Posture 160/160",
        "- Hwaran (Guide)   : Spd 8 -> 4 AP         | HP 2,800/2,800 | SP 45/45 | Posture 120/120",
        "- Heart Core       : Spd 0 -> 0 AP         | HP 2,340/2,700 | Posture 154/400 [STAGGER LEVEL 1]",
        "- Slag Crucible    : Spd 0 -> 0 AP         | HP 740/1,900   | Posture 104/360 [CRACKED]",
        "- Total Boss       : HP 3,080/6,200 [THRESHOLD BREACHED / TAKES 1.5X DAMAGE]"
    ])
    sections.append(wrap_box(t3_hud))
    
    sections.append("### Turn 03 Action Resolution Log (First Stagger Proc & Slag Crucible Cracked)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Shorn of its vents, the Blazing Heart thrashes in boiling agony, emitting `[Tears of the Ancient Smelter]`.\n")
    sections.append("  * Kael gains `Tectonic Surge` (+2 Speed -> Net Speed 8, 4 AP).\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael (Speed 8 -> 4 AP): Holds Node 05. Spends 2 AP on `[Glass Fist: Sub-Zero Resonance]`. Spends 2 AP on `[Cleaver Cleave]`.\n")
    sections.append("  * Hwaran (Speed 8 -> 4 AP): Stands at Node 03. Spends 2 AP on `[Cryo-Brine Jet]`.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 05 to 06)**: The Blazing Heart pulses with `[Tears of the Ancient Smelter]` (Base 18 + 2 Coins = 26 Power, Heavy Lament/Heat).\n")
    sections.append("    * Kael clashes with `[Glass Fist: Sub-Zero Resonance]` (Base 23 + 2 Coins = 35 Power, Seismic Void).\n")
    sections.append("    * **Clash Outcome**: Kael WINS THE CLASH (35 vs 26)!\n")
    sections.append("    * Kael's glass arm punches deep into the molten iron mantle; sub-zero acoustic waves freeze the boiling slag into brittle gray cast iron!\n")
    sections.append("    * Hwaran's cryo-brine jet shatters the frozen shell; massive chunks of iron fall away, exposing the pulsing Grief Spark within!\n")
    sections.append("    * Deals **880 Void/Cold damage** and +122 Posture Strain!\n")
    sections.append("- **Step 4: STAGGER THRESHOLD 1 TRIGGERED!**:\n")
    sections.append("  * Total Boss HP crosses 70% threshold (4,340 HP), falling to **3,080/6,200 HP**; Posture crosses 60% strain line!\n")
    sections.append("  * **STAGGER LEVEL 1 ACTIVE!** The Blazing Heart sinks into the central dais; molten slag mantle falls away; unquenched tears exposed; takes +50% damage across all incoming attacks!\n")
    sections.append("- **Step 5: Turn End State**:\n")
    sections.append("  * Total Boss HP: 4,220 -> **3,080/6,200 [THRESHOLD BREACHED: Below 4,340 HP!]**.\n")
    sections.append("  * Slag Crucible: 1,520 -> **740/1,900** | Posture: **104/360 [CRACKED]**.\n")
    sections.append("  * Boss Posture: **154/400 [STAGGER LEVEL 1]**.\n")
    sections.append("  * Kael Status: Unbroken.\n\n")
    sections.append('---\n\n')
    
    # Turn 04 HUD
    t4_hud = make_box("TACTICAL STAGE HUD: ARC 04 - BATTLE TURN 04", [
        "[STAGE NODES 01 TO 10 - MAXIMUM BURST & PHASE 2 THRESHOLD SKIP]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[HOIST] [C-WALK][PYLON] [CIVIL] [HEART] [VENTS] [FLUE]  [CHASM][COLUMN][VALVE]",
        "                [HWARAN][SAFE]  [KAEL]  [HEART]                        [BULHWA]",
        "---",
        "- Node 05: Kael (Four-Fold Cleaver Execution on Exposed Grief Spark)",
        "- Node 06: The Blazing Heart (Immobilized / Liquid Blue Tears Weeping)",
        "- Node 07: Hwaran (Cryo-Brine Flood Quenching Surrounding Lava)",
        "- Node 10: Exhaust Flue Override (Keeper Bulhwa Operating Valve)",
        "---",
        "- Kael (Drift King): Spd 11 -> 5 AP [BURST CRIT] | HP 4,200/4,200 | SP 50/50",
        "- Heart Core       : Spd 0 -> 0 AP               | HP 760/2,700   | Posture 62/400",
        "- Slag Crucible    : DESTROYED (0/1,900 HP)",
        "- Total Boss       : HP 760/6,200 [BURST DAMAGE 2,320! SECOND THRESHOLD SKIPPED]"
    ])
    sections.append(wrap_box(t4_hud))
    
    sections.append("### Turn 04 Action Resolution Log (Maximum Burst & Phase 2 Threshold Skip)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * The Blazing Heart remains stunned; the unquenched Grief Spark inside is exposed, weeping luminescent azure tears into the magma.\n")
    sections.append("  * Kael coordinates an all-out offensive barrage targeting the central spark.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael (Speed 11 -> 5 AP, Momentum Crit): Stands at Node 05. Spends 3 AP on `[Four-Fold Cleaver Execution]`. Spends 2 AP on `[Sub-Zero Cleave]`.\n")
    sections.append("  * Hwaran: Calls in `[Cryo-Brine Deluge]` (3 AP).\n")
    sections.append("- **Step 3: Unopposed Stagger Punishment Rotation**:\n")
    sections.append("  * Kael's `[Four-Fold Cleaver Execution]`: Rips through the grief spark for **1,260 Void damage** (Fatal 2.0x proc!)!\n")
    sections.append("  * Kael's `[Sub-Zero Cleave]`: Shatters the remaining iron mantle for **540 Cold damage**!\n")
    sections.append("  * Hwaran's `[Cryo-Brine Deluge]`: Quenches the surrounding lava pools for **520 Cold/Void damage**!\n")
    sections.append("  * **TOTAL BURST DAMAGE: 2,320 DAMAGE!**\n")
    sections.append("- **Step 4: SECOND STAGGER THRESHOLD (2,480 HP) COMPLETELY SKIPPED!**:\n")
    sections.append("  * Boss HP plunges from 3,080 down to **760/6,200 HP**! Slag Crucible completely destroyed (0/1,900 HP)!\n")
    sections.append("  * **Phase 2 Emergency Activation Triggered!**\n")
    sections.append("- **Step 5: Turn End State**:\n")
    sections.append("  * Total Boss HP: 3,080 -> **760/6,200** (Core HP: **760/2,700** | Mantle: **DESTROYED**).\n")
    sections.append("  * Posture: **62/400**.\n\n")
    sections.append('---\n\n')
    
    # Turn 05 HUD
    t5_hud = make_box("TACTICAL STAGE HUD: ARC 04 - BATTLE TURN 05", [
        "[STAGE NODES 01 TO 10 - THE PRIMORDIAL INFERNO & SOLACE OVERDRIVE]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[HOIST] [C-WALK][PYLON] [CIVIL] [HEART] [VENTS] [FLUE]  [CHASM][COLUMN][VALVE]",
        "                [HWARAN][SAFE]  [KAEL]  [HEART]                        [BULHWA]",
        "---",
        "- Node 05: Kael (Relic Overdrive: SOLACE OF THE QUENCHED FORGE)",
        "- Node 06: The Blazing Heart (Last Stand: Supernova of Four Thousand Years)",
        "- Node 07: Hwaran (Anchoring Thermal Insulation Across Chasm)",
        "- Node 10: Exhaust Flue Override (Keeper Bulhwa Operating Valve)",
        "---",
        "- Kael (Drift King): Spd 9 -> 5 AP [OVERDRIVE] | HP 4,200/4,200 | SP 50/50 [RESOLVE]",
        "- Heart Core       : Spd 3 -> 1 AP             | HP 760/2,700   | Posture 30/400 [EXHAUSTED]",
        "- Total Boss       : HP 760/6,200 [SUPERNOVA TRANSMUTED TO WARM EMBER]"
    ])
    sections.append(wrap_box(t5_hud))
    
    sections.append("### Turn 05 Action Resolution Log (Phase 2 Escalation: Supernova & Forge Solace Overdrive)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * The Blazing Heart awakens in desperate, wailing agony; all remaining thermal energy condenses into a ten-meter sphere of liquid white flame!\n")
    sections.append("  * Boss Special Skill: `[Supernova of Four Thousand Years]` (Volcanic Meltdown Cataclysm, 3 Coins).\n")
    sections.append("  * Kael activates Relic Overdrive: `[SOLACE OF THE QUENCHED FORGE — MAXIMUM]` (Cost: 3 AP, 30 SP).\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael (Speed 9 -> 5 AP [Overdrive]): Steps straight onto the central dais at Node 05, extending both hands.\n")
    sections.append("  * Hwaran: Anchors thermal insulation lines across the chasm at Node 07.\n")
    sections.append("- **Step 3: Clash & Skill Resolution**:\n")
    sections.append("  * **Clash 1 (Node 05 to 06)**: The Blazing Heart unleashes `[Supernova of Four Thousand Years]` (Base 24 + 3 Coins = 36 Power, Area Heat/Lament).\n")
    sections.append("    * Kael clashes with `[SOLACE OF THE QUENCHED FORGE — MAXIMUM]` (Base 31 + 3 Coins Heads = 53 Power, Transcendent Solace).\n")
    sections.append("    * **Clash Outcome**: KAEL OVERWHELMING RELIC CLASH WIN (53 vs 36)!\n")
    sections.append("    * Kael's glass arm envelops the white-hot sphere; the sub-zero acoustic frequency transmutes the destructive fire into a gentle, warm golden hearth-ember (`[P3: Parry/Protection]`).\n")
    sections.append('    * Kael\'s voice rings through the chamber: *"You have burned long enough. The city has heard your tears. Rest now."*\n')
    sections.append("    * The boiling magma lake cools into smooth, walkable obsidian glass! Zero caravan or worker casualties taken!\n")
    sections.append("- **Step 4: Turn End State**:\n")
    sections.append("  * Total Boss HP: **760/6,200** | Posture: **30/400 [EXHAUSTED]**.\n")
    sections.append("  * Kael Composure: 50/50 SP.\n\n")
    sections.append('---\n\n')
    
    # Turn 06 HUD
    t6_hud = make_box("TACTICAL STAGE HUD: ARC 04 - BATTLE TURN 06", [
        "[STAGE NODES 01 TO 10 - FORGE HARMONIZATION & EMBER HARVEST]",
        "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]",
        "[HOIST] [C-WALK][PYLON] [CIVIL] [EMBER] [CALM]  [FLUE]  [CHASM][COLUMN][VALVE]",
        "                [HWARAN][SAFE]  [KAEL]  [PACIF]                        [BULHWA]",
        "---",
        "- Node 05: The Blazing Heart (PACIFIED & TRANSMUTED TO TRANQUIL EMBER)",
        "- Node 06: Magma Lake (COOLED TO EXPEDITIONARY OBSIDIAN HIGHWAY)",
        "- Node 10: Exhaust Flue Override (Cheonbulok Furnace Safely Stabilized)",
        "---",
        "- Kael Status: Zero Damage Taken | Composure 50/50 SP (Tranquil Authority)",
        "- Expedition Status: CALDERA SAVED | Han Reactor Stabilized | Ingress Open"
    ])
    sections.append(wrap_box(t6_hud))
    
    sections.append("### Turn 06 Action Resolution Log (Forge Harmonization & Reactor Pacification)\n")
    sections.append("- **Step 1: Pre-Clash Stance & Aura / Passive Initialization**:\n")
    sections.append("  * Hostile intent drops to zero. Posture reaches **0/400 [HARMONIZATION COMPLETE]**.\n")
    sections.append("- **Step 2: Spatial Movement & Action Point Allocation**:\n")
    sections.append("  * Kael steps forward to Node 05, lifting the glowing golden ember from the center of the cooled crucible.\n")
    sections.append("- **Step 3: Harmonization & Transmutation**:\n")
    sections.append("  * The blinding white heat of the cavern resolves into the comforting warmth of a grandmother's woodstove. The four hundred Ash Walkers step out onto the cooled obsidian, weeping with gratitude.\n")
    sections.append('  * Furnace Keeper Bulhwa touches the smooth black stone, his voice trembling:\n')
    sections.append('    > *"The mountain has stopped screaming. The furnace is breathing... calm and steady. Kael... you didn\'t just save our city. You gave our ancestors their peace."*\n')
    sections.append("  * Deals **760 Peaceful Harmony**! Boss HP drops to 0!\n")
    sections.append("- **Step 4: Operational Artifact Extraction & Overland Requisition**:\n")
    sections.append("  * **Tactical Requisition Acquired**: `[Overland Module: The Flame of Solace]` (Permanent 100% fuel independence for the Drift Throne and squad-wide immunity to freezing and heatstroke).\n")
    sections.append("  * **Caldera Stabilized**: Cheonbulok's Great Furnace is permanently stabilized at a safe, sustainable operating equilibrium. The city's western gates swing open, granting the Horizon Caravan access to the Singing Dunes.\n")
    sections.append("  * **Casualties**: Zero Casualties Taken. Kael HP 4,200/4,200. Composure 50/50 SP.\n\n")
    sections.append('---\n\n')
    
    # Chapter VI: The Flame Pacified & The Tears of the Furnace
    sections.append("## Chapter VI: The Flame Pacified & The Tears of the Furnace\n\n")
    sections.append("In the cooled obsidian amphitheater of the Sacred Core, eighty thousand citizens of Cheonbulok gathered over the following two days. There were no battle trials, no executions, and no screams of wounded gladiators. Instead, for the first time in municipal history, the citizens held a vigil of remembrance for the workers who had died sealing the calderas four thousand years before.\n\n")
    sections.append("Furnace Keeper Bulhwa and Champion Barok stood beside the Drift Throne at the western gatehouse. Across the mobile cruiser's bow, master welders had mounted a brand-new refractory prow forged from Cheonbulok's purest slag-iron and inscribed with the joint crests of Somnarak and the City of Fire.\n\n")
    sections.append('"You carry our flame with you, Kael," Barok said, clasping Kael\'s hand with an iron grip that held no enmity. "Take it to the edge of the world. Show whoever built this broken earth that we did not go quietly in the dark."\n\n')
    sections.append('"We will carry it to the Void Wall," Kael answered. "Keep the hearth warm, Barok. We intend to return."\n\n')
    sections.append('---\n\n')
    
    # Chapter VII: Operational Requisition Harvest & Sovereign Crucible Relic
    sections.append("## Chapter VII: Operational Requisition Harvest & Sovereign Crucible Relic\n\n")
    sections.append("The Drift Throne's engine room hummed with a deep, golden vibrancy as `[The Flame of Solace]` was installed into the primary thermal manifold:\n\n")
    
    reward_box = make_box("OVERLAND REQUISITION HARVEST: ARC 04", [
        "ACQUIRED SALVAGE     : The Primordial Grief Spark of Cheonbulok",
        "UPGRADE DESIGNATION  : [Overland Module: The Flame of Solace]",
        "CARAVAN SPEED STATUS : Cruising at 58 km/h toward The Singing Dunes",
        "---",
        "FLAGSHIP SYSTEM ENHANCEMENTS:",
        "1. Infinite Hearth   : 100% thermal fuel self-sufficiency; internal",
        "                     heating protects crew from -60°C void freezes.",
        "2. Solace Cannonade  : Spinal kinetic railgun attacks infused with",
        "                     harmonized thermal energy (+30% Clash Power).",
        "3. Alliance Network  : Full logistical supply chain established between",
        "                     Somnarak and Cheonbulok via Horizon Waystations.",
        "---",
        "NEXT TARGET REGION:",
        "- Waystations 12 to 15: The Singing Dunes (3,200 to 3,900 km)"
    ])
    sections.append(wrap_box(reward_box))
    
    sections.append("The heavy diesel pneumatic horns of the Drift Throne sounded three times across the caldera. The cruiser rolled out through the western portal, leaving the smoking peaks of Cheonbulok behind as it plunged into the treacherous reaches of the outer dunes.\n")
    
    return "".join(sections)

if __name__ == "__main__":
    content_3 = build_arc_3()
    with open("SOMNARAK-WORLD/Jipyeongseondae/Arc_3_Arrival_at_Cheonbulok.md", "w", encoding="utf-8") as f:
        f.write(content_3)
    print("Arc 3 expanded successfully!")
    
    content_4 = build_arc_4()
    with open("SOMNARAK-WORLD/Jipyeongseondae/Arc_4_The_Furnaces_Secret.md", "w", encoding="utf-8") as f:
        f.write(content_4)
    print("Arc 4 expanded successfully!")
