#!/usr/bin/env python3
"""
Generate Canto VI: The Slum Breacher (Breacher Kang).
Strict Compliance:
- Zero P.M. vocabulary (No ZAYIN/TETH/HE/WAW/ALEPH, No E.G.O, No Abnormality, No Enkephalin, No Distortion)
- Native Somnarak terminology: Han-Energy, Composure, Posture, Weight (Black), Sorrow Entity, Ranks I-V, Grades a-w
- Two-space buffer around all Korean characters: '  [korean]  '
- Alphabet / Romanization style alongside Korean: '  [korean]  / [Alphabet Romanization] [[English Translation]]'
- 71-col ASCII text boxes via tools.box_formatter
- Zero raw <br> tags, zero raw HTML, zero LaTeX math dollar signs
- 10-node tactical spatial engine combat sequence
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import tools.box_formatter as bf

OUTPUT_PATH = "SOMNARAK-WORLD/Story_Cantos/CANTO_06_THE_SLUM_BREACHER_KANG.md"

def wrap_box(box_text):
    return "```text\n" + box_text + "\n```\n\n"

def build_canto_06():
    lines = []
    
    # Master Header
    lines.append("# CANTO VI: THE SLUM BREACHER (  슬럼 침투병  / Seulleom Chimtubyeong [The Slum Breacher])")
    lines.append("## Breacher Kang and the Mask Forge of Zone B")
    lines.append("### The Reverie Directorate — Containment Chronicles of Cycle 1,778\n")
    
    # Master HUD Box
    hud_rows = [
        "CANTO VI: THE SLUM BREACHER (THE VOID MAUL)",
        "PROTAGONIST  : Chief Breacher Kang (The Ram / Urban Demolition)",
        "AFFILIATION  : Underworld Cleanup Descend (UCD) — Strike Team 04",
        "THEATER      : Zone B Sub-Sump Canal 08 & Mask Forge (-120m Cistern)",
        "FRACTURE     : Undercity Brotherhood vs Municipal Pacification Duty",
        "EQUIPMENT    : MAW-W-054-01 The Void Maul & Hazard Breacher Plate",
        "COMPOSURE    : Baseline 110 / Crisis Threshold 32 / Max Posture 190",
        "ACT I        : The Sump and the Shield-Plate — Canal 08 Staging Post",
        "ACT II       : The Faceless Foundry — Mask Forge Meltdown & Rust Frays",
        "ACT III      : The Resonant Catharsis — Hollow Impact Brotherhood Clash"
    ]
    lines.append(wrap_box(bf.make_box("MASTER CODEX: NARRATIVE CANTO VI", hud_rows, width=71)))
    
    lines.append("> *\"In the upper plazas, they wear masks to look pretty. Down in the sump, we wear masks so our mothers won't weep when they find our bodies in the slag. You think putting on a municipal uniform washed you clean, Kang? You still smell like canal sludge. The only difference is now you're holding the hammer.\"*")
    lines.append("> — Underboss Jin-Woo (  진우  / Jin-Woo), Intercepted Voice Log before Canal 08 Breach\n")
    lines.append("---\n")
    
    # Act I
    lines.append("## Act I: The Sump and the Shield-Plate (  하수구와 방패판  / Hasugu-wa Bangpaepan [The Sump and the Shield-Plate])\n")
    act1_rows = [
        "ACT I: THE SUMP AND THE SHIELD-PLATE (CANAL 08 STAGING)",
        "LOCATION     : Zone B Drainage Sump & Sub-Canal 08 Outflow (-120m)",
        "TIMESTAMP    : Third Watch (15:20 Afternoon / Tactical Staging)",
        "PERSONNEL    : Breacher Kang, Warden Min-Jae, Vanguard Taeho",
        "STATUS       : Baseline Composure 110/110 | Methane Index 4.2 ppm"
    ]
    lines.append(wrap_box(bf.make_box("TACTICAL DISPATCH: ACT I STATUS", act1_rows, width=71)))
    
    act1_prose = """The canal water was black as burnt oil.

It flowed sluggishly through the arched brick culverts of Sub-Sump Canal 08, one hundred and twenty meters beneath the squalid tenement blocks of Zone B. The surface of the water was coated with an iridescent film of petroleum waste, chemical runoff from illegal stim-dens, and the foul, sulfurous sludge of the undercity.

Chief Breacher Kang (  강  / Kang) knelt on the rusted iron catwalk, dipping an asbestos cleaning rag into a bucket of neutralized lye to scrub the hydraulic fittings of his breaching ram.

His arms were thick as cedar logs, corded with scarred muscle and heavily tattooed with the faded blue ink of the Mask Market (  가면 시장  / Gamyeon Sijang [The Mask Market])—the desperate, lawless bazaar where orphans and runaway debtors sold their names to survive. Over his shoulders he wore the heavy, reinforced hazard armor of the Underworld Cleanup Descend (UCD /   지하 정화 소탕대  / Jiha Jeonghwa Sotangdae [Underworld Cleanup Descend]), its olive-drab steel plates reinforced with lead shielding to absorb the caustic back-blast of industrial demolition charges.

Resting against the railing was *The Void Maul* (`MAW-W-054-01`).

The weapon's head was shaped like a concave black dish—an empty bowl of dense volcanic stone ringed with dull grey alloy. It was forged from the remnant shell of `SE-C-IIβ-054 The Empty Mask` (  빈 가면  / Bin Gamyeon [The Empty Mask]). When the maul struck an identity-erasing construct, the hollow bowl absorbed the emptiness, turning the absence of a name into crushing Weight (  무게  / Muge [Weight]) damage.

But the cost was severe: every time the maul discharged its payload, the bearer felt a creeping numbness in their own mind—a hollow void where their own name used to be, until another human being spoke it aloud into their face.

"You're checking that hydraulic seal for the fourth time, Kang."

Warden Min-Jae (  민재  / Min-Jae) stepped off the rusted iron service ladder, his massive *Tectonic Bulwark* held loosely in his left hand. The veteran warden had traded his pristine Directorate tunic for an oil-stained hazard duster, his heavy boots splashing through the ankle-deep muck of the drainage walkway.

"A jammed seal means the piston backfires into my shoulder," Kang muttered, his voice raspy, carrying the rough gutter accent of the Zone B tenements. "In these narrow sewer pipes, you don't get a second chance to swing. You breach the gate on the first stroke, or the syndicate fills the corridor with pressurized caustic vapor."

"Taeho and Seol-A have already secured the secondary drainage valves," Min-Jae said, sitting on an overturned cable spool. He looked down at the dark, swirling water beneath their boots. "The reports from Central Archive say the Rust Frays (  녹슨 가닥들  / Nokseun Gadakdeul [The Rust Frays]) have taken over the ancient hydraulic foundry in Sector B-02. They're mass-producing counterfeit masks using a breached entity core."

Kang's jaw tightened. He wrung out the lye rag, the caustic liquid burning his scarred knuckles.

"Jin-Woo is running the foundry," Kang said quietly.

Min-Jae looked up, his brown eyes steady. "Your oath-brother from the Mask Market."

"We grew up in the same drainage culvert," Kang said, his voice flat, drained of sentiment. "When the debt collectors came for our tenement block twelve years ago, we stole two counterfeit Veil stones and hid inside a sewer pipe for forty-eight hours with sewage up to our chins. We swore an oath: when we got older, we'd tear down the debt towers together."

Kang tossed the rag into the bucket with a wet splash.

"Then I joined the UCD. And Jin-Woo stayed behind."

"You joined because the syndicates were butchering their own people," Min-Jae said firmly.

"The kids in the slums don't see it that way," Kang replied, his eyes dark with old bitterness. "To them, I'm a Directorate dog. A gutter rat who put on a brass badge so he could come back down here with a sledgehammer and break the skulls of the boys he used to share bread with. Jin-Woo sent me a message through the pipe-rat runners yesterday. He said if I step through that gate, he won't bury me. He'll mold an empty mask over my face and sell my corpse to the Debt Concourse."

A heavy iron boot slammed down onto the catwalk behind them.

Vanguard Taeho (  태호  / Taeho) marched up, carrying a heavy pneumatic cutting torch across his broad shoulders. He smelled of sulfur and machine oil, his face streaked with soot.

"Let him try," Taeho grunted, spitting a mouthful of bitter chicory grounds into the canal. "I was born in the foundry district of Zone D, Kang. I know what these syndicate bastards are. They talk about brotherhood while they slip a debt collar around your neck and sell your sister to the extraction pens. Jin-Woo isn't your brother anymore. He's a cartel boss sitting on a pile of stolen faces."

Specialist Seol-A (  설아  / Seol-A) appeared at the top of the stairwell, her silver resonance collar glowing faintly in the murky gloom. Her crystalline spear was locked to her combat harness, her posture taut and alert.

"Movement in the forward conduit," Seol-A reported, her voice sharp and clear. "The acoustic sensors picked up thirty distinct footsteps marching in perfect synchronization. No breathing. No dialogue. They are moving through the flood sluice toward our position."

Kang stood up. He grabbed the long black haft of *The Void Maul*, the concave dish humming faintly against his palm as it detected the nearby absence of human identity.

"Those aren't soldiers," Kang whispered, his knuckles turning white against the grip. "Those are the thralls from the Mask Forge. Jin-Woo has already started the crucible."
"""
    lines.append(act1_prose.strip() + "\n\n---\n")
    
    # Act II
    lines.append("## Act II: The Faceless Foundry (  얼굴 없는 주조소  / Eolgul Eomneun Jujosoh [The Faceless Foundry])\n")
    act2_rows = [
        "ACT II: THE FACELESS FOUNDRY (MASK FORGE BREACH)",
        "LOCATION     : Sector B-02 Hydraulic Foundry & Sluice Gate 04",
        "TIMESTAMP    : Third Watch (16:05 Combat Breach)",
        "TARGET       : SE-C-IIb-054 The Empty Mask & Rust Fray Underboss",
        "HAZARD       : Identity Void Aura / Mass Thrall Puppet Swarm"
    ]
    lines.append(wrap_box(bf.make_box("TACTICAL DISPATCH: ACT II BREACH", act2_rows, width=71)))
    
    act2_prose_part1 = """The breaching charge blew the three-ton iron sluice gate inward with an ear-splitting concussion.

Water and steam erupted through the breach as the Iron Quad charged through the smoke into the ancient foundry chamber.

The space was a cavernous subterranean cistern, eighty meters long, dominated by four colossal hydraulic forging presses that rose toward the vaulted brick ceiling. Molten slag ran through open floor channels, casting a hellish, flickering crimson glare across the wet masonry.

At the center of the hall, suspended over a massive boiling vat of liquefied Han (  한  / Han) resin, was the manufacturing dais.

Dozens of Zone B debtors stood around the vat like mindless statues. Over each of their faces was welded a featureless black mask—smooth, devoid of eyes or mouth, an obsidian void that swallowed light. They moved in mechanical unison, ladling boiling resin into iron molds, stamping out hundreds of counterfeit masks for the black market.

And standing atop the central platform was Underboss Jin-Woo (  진우  / Jin-Woo).

He was no longer the skinny, ragged street orphan Kang had shared cold bread with twelve years ago. He was clad in spiked syndicate carapace armor, his chest crisscrossed with pressurized stim-tubes. And fused seamlessly to his face was the sovereign relic of `SE-C-IIβ-054 The Empty Mask` (  빈 가면  / Bin Gamyeon [The Empty Mask]).

The mask had no features—only a deep, sucking void of pure black stone that seemed to bend the surrounding air inward like a miniature gravitational singularity.
"""
    lines.append(act2_prose_part1.strip() + "\n\n")
    
    breach_hud = [
        "ENTITY       : SE-C-IIb-054 (The Empty Mask / Indumentum Relic)",
        "HOST         : Underboss Jin-Woo / Affiliation: The Rust Frays",
        "ELEMENT      : Weight (Black) / Category: City Sorrow",
        "VOID THREAT  : Identity Erasure Radius 40m / Progressive Composure Drain",
        "LETHAL THRESH: Complete Identity Dissolution into Indumentum Shell"
    ]
    lines.append(wrap_box(bf.make_box("CONTAINMENT BREACH: HOLLOW PROFILE", breach_hud, width=71)))
    
    act2_prose_part2 = """When Jin-Woo spoke, the sound did not come from a mouth. It came from the hollow reverberation inside the stone dish of his face.

*\"You're late, Breacher Kang.\"*

The voice was cold, flat, stripped of all the laughter, rage, and swagger that had once defined the street boy from Canal 08.

*\"Look at them, Kang. Look at how quiet they are. Up in the Directorate towers, they tell you that a man needs a name. But down here in the mud, a name is just a bill that never gets paid. A name is a debt that passes to your children. When I take their faces, I take their debt. I take their shame. In this forge, we are all equal. We are all nothing.\"*

With a flick of Jin-Woo's armored wrist, the thirty masked debtors turned toward the breach in terrifying unison. They raised rusted scrap-iron cleavers, pneumatic nail drivers, and broken steam pipes, advancing across the wet floorplates.

"Suppress the crowd! Do not use lethal force on the debtors!" Min-Jae bellowed, slamming his *Bastion Aegis* into the canal floor at Node 4. The shockwave of amber light washed across the front row of thralls, staggering them without shattering their limbs. "Kang, get to the crucible! The mask is feeding on the resin vat!"

"On it!" Kang roared, charging forward.

As he closed the distance, Jin-Woo raised his left hand.

A crushing wavefront of black Weight (  무게  / Muge [Weight]) energy exploded from the Empty Mask, sweeping across the foundry.

The air pressure tripled. Taeho's knees buckled at Node 5 as fifty kilograms of invisible downforce slammed onto his shoulders. Even Min-Jae's heavy boots slid backward through the muck, the basalt shield groaning under forty tons of localized gravity.

Kang was hit dead center at Node 7.

The psychic back-blast hit his mind like a physical battering ram. Inside his skull, the memories began to blur.

*Who are you, breacher?*

The void inside the mask coiled into his thoughts. He saw his mother's face—and suddenly her features dissolved into smooth, featureless black stone. He saw the cold night in the sewer pipe with Jin-Woo—and his own voice in the memory faded into silence.

His Composure gauge on his breastplate display flashed red: 110... 68... 45... 32.

The hollow dish of *The Void Maul* in his hands began to pulse with blinding grey light, drinking in the identity void from the room. But as the weapon charged, Kang felt his own grip weakening. He looked down at his gloved hands and for five terrifying seconds, he couldn't remember what his own name was.

*Am I... an enforcer? Am I... a syndicate runner? What was I before I held this iron?*

His knees hit the wet steel plates. The maul clattered against the floor.

Jin-Woo stepped down from the platform, drawing a serrated trench cleaver coated in caustic blue venom. He raised the blade above Kang's exposed neck.

*\"See?\"* Jin-Woo whispered softly into the hollow air. *\"Even you couldn't keep your face in the dark. Sleep, little brother. Let the canal take your name.\"*

"KANG!"

A roar shook the very foundations of the foundry.

Min-Jae was down on one knee, holding back eight thralls with the edge of his shield, his face purple from exertion.

"CHIEF BREACHER KANG! STAND UP!"

Beside him, Taeho smashed his war maul into the ground, creating a blinding shower of sparks that illuminated the dark ceiling. "YOUR NAME IS KANG! THE MEANEST BASTARD ON FLOOR 01! DON'T YOU DARE FORGET IT IN FRONT OF THIS CLOWN!"

"Kang!" Seol-A's voice cut through the comms like a silver blade. "Take the swing!"

The three voices hit him like an electric jolt to a stopped heart.

*Kang.*

The word exploded through the void in his mind. The blurred memories snapped back into diamond clarity: his mother's worn hands, the oath in the cold pipe, the blood on his vanguard armor, and the three soldiers who had walked into sixty feet of sewage and poison gas just to have his back.

"My name," Kang snarled, his eyes blazing behind his cracked visor as his hands locked around the haft of *The Void Maul*, "is Kang."

He lunged upward from the mud, driving his shoulder into Jin-Woo's chest.

"AND I'M HERE TO SMASH YOUR MASK!"
"""
    lines.append(act2_prose_part2.strip() + "\n\n---\n")
    
    # Act III
    lines.append("## Act III: The Resonant Catharsis (  공명의 정화  / Gongmyeong-ui Jeonghwa [The Resonant Catharsis])\n")
    act3_rows = [
        "ACT III: THE RESONANT CATHARSIS (10-NODE TACTICAL RESOLUTION)",
        "LOCATION     : Sector B-02 Mask Crucible & Hydraulic Foundry",
        "TIMESTAMP    : Third Watch (16:30 Tactical Resolution)",
        "ENGAGEMENT   : Iron Quad vs The Empty Mask (10-Node Grid)",
        "OUTCOME      : Mask Shell Shattered / Brotherhood Reclaimed"
    ]
    lines.append(wrap_box(bf.make_box("TACTICAL DISPATCH: ACT III CLASH", act3_rows, width=71)))
    
    act3_prose_part1 = """The spatial combat grid inside the Sector B-02 Mask Forge was mapped across ten tactical nodes, stretching from the blown sluice gate to the boiling resin crucible at the foundry's rear.
"""
    lines.append(act3_prose_part1.strip() + "\n\n")
    
    # 10-node spatial combat grid banner
    grid_lines = [
        bf.make_borderless_banner("10-NODE SPATIAL COMBAT GRID: MASK FORGE CRUCIBLE ENGAGEMENT", width=71),
        "[NODE 01] [NODE 02] [NODE 03] [NODE 04] [NODE 05] [NODE 06] [NODE 07] [NODE 08] [NODE 09] [NODE 10]",
        "[ Jinho ] [ Sluice] [       ] [Min-Jae] [ Taeho ] [Seol-A ] [ Kang  ] [       ] [JIN-WOO] [       ]",
        "[Comms  ] [ Breach] [ Empty ] [ANCHOR ] [STRIKER] [ FLANK ] [BREACH] [ Empty ] [MASK   ] [ Empty ]",
        "-" * 71,
        "Node 01 : Entrance sluice threshold / Jinho holding extraction comms.",
        "Node 02 : Flooded catwalk approach / Caustic water hazard zone.",
        "Node 03 : Mid-foundry conduit junction / Scrap-iron barricade.",
        "Node 04 : Frontline defensive fulcrum / Min-Jae Bastion Shield wall.",
        "Node 05 : Forward thrall-clearing line / Taeho kinetic disruption.",
        "Node 06 : Lateral slag flume catwalk / Seol-A high-speed flank.",
        "Node 07 : Heavy Breacher platform / Kang kinetic charge position.",
        "Node 08 : The Precipice Threshold / Boiling Han resin spillway.",
        "Node 09 : The Mask Forge Crucible / Jin-Woo & The Empty Mask Core.",
        "Node 10 : Subterranean canal overflow drain / Toxic exhaust sump.",
        "=" * 71
    ]
    lines.append("```text\n" + "\n".join(grid_lines) + "\n```\n\n")
    
    lines.append("### Turn-Based Tactical Combat Resolution\n")
    lines.append("The suppression of `SE-C-IIβ-054 The Empty Mask` was executed across six tactical turns within the primary combat phase, utilizing speed priority, action point investment, and the Four P-Framework:\n\n")
    
    combat_log_rows = [
        "TURN 1: SPEED & POSITIONING PHASE",
        "- Underboss Jin-Woo initiates [Hollow Command] (Speed 6).",
        "- Deploys 30 masked debtors across Nodes 4-6 to form meat shield.",
        "- Min-Jae rolls Speed 3: Spends 2 AP on [Non-Lethal Shield Sweep]",
        "  at Node 4, pinning the frontline without crushing debtor limbs.",
        "- Min-Jae Posture: 175/195 | Composure: 85/110.",
        "-------------------------------------------------------------------",
        "TURN 2: FLANKING THE CRUCIBLE BELLOWS (PILLAR: PRESENCE)",
        "- Seol-A rolls Speed 8: Spends 3 AP on [Siphon Vault] to reach Node 6.",
        "- Pierces pneumatic bellows of the resin vat, halving mask production.",
        "- Taeho advances to Node 5, using [Molten Maul Disruption] to shatter",
        "  the scrap-iron barricades. Presence Trigger: Kang sees his squad",
        "  risking their lives in toxic sludge solely to help him save his brother.",
        "- Kang Composure recovers: 32 -> 80/110. Posture: 165/190.",
        "-------------------------------------------------------------------",
        "TURN 3: THE HEAVY BREACHER SPRINT",
        "- Kang spends 3 AP on [Hydraulic Breacher Overdrive]:",
        "  Pneumatic rams vent steam, propelling him from Node 4 -> Node 7.",
        "- Jin-Woo counters with [Void Cleave] (Clash Power 24).",
        "- Kang clashes with [Void Maul Guard]: Clash Power 26 vs 24!",
        "- Victory Kang! Deflects venom blade; closes distance to Node 8.",
        "-------------------------------------------------------------------",
        "TURN 4: THE PRECIPICE OF THE CRUCIBLE (PILLAR: PRECIPICE)",
        "- Jin-Woo unleashes [Face of Oblivion] at Node 9:",
        "  A crushing 50-ton Weight gravity beam aimed straight at Kang.",
        "- Kang steps onto Node 8, right over the boiling resin vat.",
        "- Precipice reached: Instead of shielding, Kang absorbs the downforce",
        "  into the concave dish of The Void Maul! Dish glows brilliant white!",
        "-------------------------------------------------------------------",
        "TURN 5: THE ANCHOR VOW (PILLAR: PURPOSE)",
        "- Identity cost threatens to wipe Kang's memory as dish reaches 100%.",
        "- Min-Jae, Taeho, and Seol-A roar his name simultaneously: 'KANG!'",
        "- Requirement met! External naming clears the identity toll.",
        "- Kang activates MAW-W-054-01 unique trait [Hollow Shatter].",
        "- Purpose reclaimed: 'I didn't come to kill you, Jin-Woo. I came to",
        "  bring you home!'",
        "-------------------------------------------------------------------",
        "TURN 6: HOLLOW IMPACT & SHELL SHATTER (PILLAR: PACT)",
        "- Kang vaults from Node 8 -> Node 9 with [Hollow Shatter]!",
        "- Clash Power: 44 vs 32! CRITICAL CLASH OVERWHELM!",
        "- Concave maul dish strikes the featureless black mask dead center.",
        "- Impact wave shatters the stone mask into a thousand inert shards",
        "  without breaking the human skull beneath! Entity suppressed!"
    ]
    lines.append(wrap_box(bf.make_box("TACTICAL COMBAT LOG: TURNS 1 THROUGH 6", combat_log_rows, width=71)))
    
    act3_prose_part2 = """### The Climax of Act III

When Kang leaped across the boiling resin vat into Node 9, the air screamed with the friction of his hydraulic exhaust.

Jin-Woo stood at the center of the crucible, both hands raised, channeling fifty tons of localized gravitational Weight (  무게  / Muge [Weight]) directly into the black void of his mask. If that gravity detonated at point-blank range, Kang's armor would be crushed into a three-inch patty of lead and bone.

Kang did not raise his shield.

He held *The Void Maul* with both hands, muscles tearing in his forearms as the weapon's concave dish drank in the full, unbridled emptiness of the room. The grey alloy rim burned with incandescent white fire.

"Jin-Woo!" Kang roared, his boots slamming onto the crucible dais.

The mask pulsed with pure oblivion.

*\"You have no name, breacher...\"*

"MY NAME IS KANG!"

He swung.

**[HOLLOW SHATTER]**

The concave dish of the maul struck the smooth black stone of the mask with the force of an artillery shell hitting a bunker wall.

The kinetic energy was staggering. A circular shockwave of displaced air blew the boiling Han resin twenty feet into the air. But the blow did not crush Jin-Woo's skull. *The Void Maul* had been calibrated for a single, surgical purpose: it did not hit bone—it hit absence.

For a frozen heartbeat, the black stone resisted.

Then, a spider-web of glowing white fissures spread across the featureless void.

With a sound like a cathedral bell cracking in two, the mask shattered.

Fragments of dense black rock exploded outward, dissolving into harmless grey dust as they hit the floor. The entity's suffocating gravitational field collapsed instantly.

Across the foundry, the thirty masked debtors gasped in unison as the counterfeit masks fell from their faces, clattering onto the metal duckboards. They looked at their hands, blinking in the yellow torchlight, their names and memories flooding back into their eyes.

On the dais, Jin-Woo collapsed onto his hands and knees.

Blood poured from his nose and ears, dripping into the cooling sludge. But his face was bare. The jagged scar across his right eyebrow—the scar from an iron pipe when he was fourteen—was visible in the warm lantern light.

His chest heaved. He looked up at Kang with wide, terrified, completely human eyes.

"Kang...?" Jin-Woo whispered, his voice trembling like a child waking from a nightmare. "My face... it's... I can feel the air."

Kang let the sixty-kilogram maul drop from his numb fingers. It hit the stone with a heavy, final *THUD*.

He sank to one knee, breathing raggedly, steam hissing from the cooling vents of his hazard armor. He reached out with his bare, calloused hand, grabbed Jin-Woo by the scruff of his spiked collar, and pulled him forward until their foreheads touched.

"You're an idiot, Jin-Woo," Kang said, his voice thick with unspilt tears and canal grit. "A stubborn, arrogant, gutter idiot."

Jin-Woo let out a weak, coughing laugh that turned into a sob. He grabbed Kang's armored forearms, his hands trembling violently.

"You really... came down into the sump for me, you bastard?"

"I told you twelve years ago," Kang said softly, wiping a smear of black sludge from his brother's cheek. "We get out of the mud together."

Behind them, heavy footsteps splashed through the receding water.

Min-Jae walked onto the dais, his massive shield lowered, his face smudged with soot and blood. Beside him, Taeho grinned broadly, shouldering his war maul, while Seol-A sheathed her spear and began checking the medical vitals of the freed debtors.

Min-Jae looked down at Jin-Woo, then looked at Kang.

"Is the breach secure, Chief Breacher?" Min-Jae asked, his voice carrying the calm authority of a frontline commander.

Kang stood up, pulling Jin-Woo to his feet with him, supporting his brother's trembling weight against his broad shoulder.

"The breach is secure, warden," Kang said, looking Min-Jae directly in the eye. "Every single person in this room is walking out alive."

Min-Jae nodded slowly, a rare, genuine smile creasing the corners of his eyes.

"Then let's go home, Iron Quad. The morning watch has ended."

Together, the four soldiers and the freed citizens turned their backs on the dark crucible and walked out of the sump, ascending the stone steps toward the dawn of Somnarak.
"""
    lines.append(act3_prose_part2.strip() + "\n")
    
    content = "\n".join(lines)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Wrote {OUTPUT_PATH} ({len(content)} bytes)")

if __name__ == "__main__":
    build_canto_06()
