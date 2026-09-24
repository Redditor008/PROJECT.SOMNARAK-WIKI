#!/usr/bin/env python3
"""
Generate Canto IV: The Sub-Zero Ridge (Marksman Ha-Eun).
Strict Compliance:
- Zero P.M. vocabulary (No ZAYIN/TETH/HE/WAW/ALEPH, No E.G.O, No Abnormality, No Enkephalin, No Distortion)
- Native Somnarak terminology: Han-Energy, Composure, Posture, Void (Pale White), Sorrow Entity, Ranks I-V, Grades a-w
- Two-space buffer around all Korean characters: '  [korean]  '
- 71-col ASCII text boxes via tools.box_formatter
- Zero raw <br> tags, zero raw HTML, zero LaTeX math dollar signs
- 10-node tactical spatial engine combat sequence
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import tools.box_formatter as bf

OUTPUT_PATH = "SOMNARAK-WORLD/Story_Cantos/CANTO_04_THE_SUB_ZERO_RIDGE_HA_EUN.md"

def wrap_box(box_text):
    return "```text\n" + box_text + "\n```\n\n"

def build_canto_04():
    lines = []
    
    # Master Header
    lines.append("# CANTO IV: THE SUB-ZERO RIDGE (  영하의 능선  )")
    lines.append("## Marksman Ha-Eun and the Frozen Veil of Outpost E-09")
    lines.append("### The Reverie Directorate — Containment Chronicles of Cycle 1,778\n")
    
    # Master HUD Box
    hud_rows = [
        "CANTO IV: THE SUB-ZERO RIDGE (THE COLD LENS)",
        "PROTAGONIST  : Marksman Ha-Eun (The Needle / Cryo-Sniper)",
        "AFFILIATION  : The Reverie Directorate — Zone E Bastion Frontier",
        "THEATER      : Outpost E-09 Glacier Trench (-40C Surface Perimeter)",
        "FRACTURE     : Emotional Numbness & Voluntary Hypothermia of Soul",
        "EQUIPMENT    : MAW-W-103-01 The Cold Lens & The Cold Veil Vestments",
        "COMPOSURE    : Baseline 105 / Crisis Threshold 35 / Max Posture 170",
        "ACT I        : The Glacial Perch — Cryo-Trench & Lost Childhood",
        "ACT II       : The Whiteout Veil — Perimeter Blinding Flash-Freeze",
        "ACT III      : The Resonant Catharsis — Break the Pull Sniper Clash"
    ]
    lines.append(wrap_box(bf.make_box("MASTER CODEX: NARRATIVE CANTO IV", hud_rows, width=71)))
    
    lines.append("> *\"When the temperature drops past minus forty, the wind stops feeling like air. It feels like broken glass pressed against your eyeballs. You stop shivering. You stop wishing for a fire. You realize that if you feel nothing at all, nothing out in the dark can ever hurt you again. That is the lie the frost tells you.\"*")
    lines.append("> — Marksman Ha-Eun (  하은  ), Outpost E-09 Watch Log\n")
    lines.append("---\n")
    
    # Act I
    lines.append("## Act I: The Glacial Perch (  빙하의 망루  )\n")
    act1_rows = [
        "ACT I: THE GLACIAL PERCH (ZONE E BASTION WATCHTOWER)",
        "LOCATION     : Outpost E-09 Observation Parapet (-40C Surface Edge)",
        "TIMESTAMP    : Fourth Watch (03:30 Midnight / Frontier Vigil)",
        "PERSONNEL    : Marksman Ha-Eun, Warden Min-Jae, Vanguard Taeho",
        "STATUS       : Baseline Composure 105/105 | Wind Chill -52C"
    ]
    lines.append(wrap_box(bf.make_box("TACTICAL DISPATCH: ACT I STATUS", act1_rows, width=71)))
    
    act1_prose = """The breath leaving her mouth did not rise. It fell.

At minus forty-two degrees Celsius, warm air condensed so rapidly that it dropped toward the steel grating of the observation tower like fine white hail.

Marksman Ha-Eun (  하은  ) lay prone on the frozen basalt parapet of Outpost E-09, perched twenty-five meters above the perimeter trench of Zone E. Her cheek was pressed firmly against the cold composite cheek-rest of *The Cold Lens* (`MAW-W-103-01`). A crust of hard blue rime coated her dark Directorate goggles, but through the circular aperture of the pale Han (  한  ) glass disc, the world was blindingly sharp.

The weapon did not fire lead cartridges. It focused pure, crystalline Void (  공허  ) energy.

The chassis was fashioned from dull gunmetal wrapped in strips of thermal-resistant seal hide, but the heart of the rifle was a circular optic disc of frost-white crystal extracted from the frozen boundary vaults of Sector C. Through that lens, the howling blizzards of the Desolate (  황량한 황무지  ) were stripped of their chaos. Distance, thermal gradients, wind vectors—everything resolved into flat, motionless geometry.

And with every shot she took through that glass, a tiny, nameless fragment of her memory was quietly erased.

Two cycles ago, she had spent an engagement suppressing a swarm of Rank II Murmurs climbing the outer cliff. When the watch ended, she realized she could no longer remember the color of her childhood bedroom curtains in the Upper Terraces. A cycle before that, she had forgotten the melody of a song her elder sister used to hum while washing laundry.

She had traded them willingly. Memories were warm, and in the freezing trenches of Zone E, warmth was a liability. Warmth made you long for home. Warmth made your trigger finger hesitate when a silhouette appeared on the white horizon.

"Your core temperature is down to thirty-four point two degrees, Ha-Eun."

The radio in her ear crackled with the deep, gravelly voice of Warden Min-Jae (  민재  ).

A heavy hydraulic hatch clanked open at the base of the tower ladder. Min-Jae climbed up, his massive armored silhouette dusted in snow. In his left hand, he carried an insulated thermos vessel wrapped in layers of thick wool; in his right, two self-heating chemical thermal bricks that glowed with a dull, cherry-red heat.

"I can't feel the crosshair drift if I'm shivering," Ha-Eun replied, her voice muffled behind her fleece respirator. She didn't take her eye off the scope. "Thermal bricks create rising heat mirages in front of the lens. Take them back down to the bunker."

"I'm not leaving them down in the bunker," Min-Jae said, stepping onto the metal platform. The tower groaned under his three hundred kilograms of basalt-plated armor. He set the glowing heat bricks beside her boots and popped the latch on the insulated thermos. The fragrant steam of hot barley water and crushed chicory root curled into the biting air, carrying an earthy, rich sweetness that felt foreign against the scent of frozen slate.

"Drink it," Min-Jae commanded, offering her a steaming tin cup.

Ha-Eun hesitated, then pulled back her right glove with her teeth. Her fingertips were waxy and pale, the capillary blood retreating from the frost. She wrapped her bare hand around the hot tin. The sudden heat surged into her nerves like needles of fire. She gasped, nearly dropping the cup.

"Pain means the tissue is still alive," Min-Jae observed quietly, leaning his heavy forearms against the frozen railing. He stared out into the pitch-black abyss of the wasteland, where the twin moons of Mugenhan cast long, eerie blue shadows across endless glaciers. "Taeho is in the generator shack cursing at the fuel lines. The paraffin gelled in the intake filters again."

"He shouldn't be here," Ha-Eun said, sipping the scalding liquid. The warmth traveled down her throat, thawing the cold knot in her chest. "Floor 01 frontline personnel aren't assigned to Zone E frontier watches. This is exterior garrison duty. You should be down in the warm armories of Central Command."

"Our sector is clear for thirty-six hours," Min-Jae answered. "And the regulations say that bearer of `MAW-W-103-01` must have a designated relationship anchor present within operational range during high-threat watches. You haven't filed an anchor evaluation in three hundred days, Ha-Eun."

Ha-Eun's jaw tightened beneath her mask.

"I don't need an anchor."

"The weapon's codex says otherwise," Min-Jae countered, his tone gentle but immovable. "The Cold Lens requires an anchor to verify that the bearer still knows the difference between clarity and numbness. If you look through that lens long enough without an anchor calling your name, you don't just shoot entities. You shoot your own humanity."

From down in the trench, a booming voice echoed up the ventilation shafts.

"Hey! Snow bird!"

Vanguard Taeho (  태호  ) emerged onto the trench duckboards below, swinging his arms and stomping his iron-shackled boots to keep his circulation flowing. He was wearing three layers of quilted wool over his combat plate, looking like an over-stuffed bear. He cupped his hands to his mouth and shouted up at the watchtower:

"I got the heater running! If you don't come down in twenty minutes, I'm eating your ration biscuits! All six of them!"

Ha-Eun looked down through the iron mesh at the broad-shouldered striker. A faint, almost imperceptible twitch softened the hard lines around her eyes.

"He's an idiot," she murmured.

"He is," Min-Jae agreed with a faint chuckle. "But he hasn't forgotten your name once in four hundred cycles. That counts for something on this ridge."

Before Ha-Eun could answer, the crosshair in her optic lens flared with blinding, razor-sharp white light.

The ambient wind did not pick up—it died completely.

A terrifying, suffocating vacuum fell across the trench line. The temperature display on the parapet console dropped precipitously: minus forty-two... minus fifty... minus sixty-one.

The frost on the steel handrails began to grow backward, crystallizing into intricate, jagged lattices of pale blue needles that reached toward the sky like frozen claws.

In the dead center of Ha-Eun's scope, three kilometers out on the glacier, a pale curtain of shifting frost descended from the clouds.

"Outpost alert," Ha-Eun's voice lost all warmth, flattening into pure, diamond-hard focus. "The Frozen Veil is on the ridge."
"""
    lines.append(act1_prose.strip() + "\n\n---\n")
    
    # Act II
    lines.append("## Act II: The Whiteout Veil (  화이트아웃 베일  )\n")
    act2_rows = [
        "ACT II: THE WHITEOUT VEIL (PERIMETER CRYOGENIC BREACH)",
        "LOCATION     : Outpost E-09 Perimeter Trench Line (-65C Inversion)",
        "TIMESTAMP    : Fourth Watch (04:15 Cryo-Meltdown)",
        "TARGET       : SE-C-IVd-103 The Frozen Veil (Critical Potency d)",
        "HAZARD       : Sub-Zero Flash Freeze / Emotional Erasure Aura"
    ]
    lines.append(wrap_box(bf.make_box("TACTICAL DISPATCH: ACT II BREACH", act2_rows, width=71)))
    
    act2_prose_part1 = """The silence that accompanied the breach was louder than artillery.

When `SE-C-IVδ-103 The Frozen Veil` (  얼어붙은 베일  ) approaches, thermal energy ceases to exist. It is not cold air moving across land; it is the absolute extraction of molecular kinetic energy, leaving behind a sterile void of pure Pale White (  공허  ) stillness.

The barbed wire entanglements along the perimeter trench shattered with the sound of breaking crystal under their own tension. The hydraulic lubricant in the outpost's automated defense turrets turned into solid white wax in less than four seconds, snapping internal gear teeth and plunging the trench into total darkness as the generators seized.

"Command! We have total generator failure at Outpost E-09!"

Sensor Tech Jinho (  진호  ) screamed through the localized short-range radio, his voice shivering violently from the communications bunker at Node 1. "The ambient temperature is minus sixty-eight degrees! My sensor panels are cracking! The entity... it isn't an animal! It's a wall! A living blizzard sixty meters high!"

"Min-Jae, get down here!" Taeho's roar cut through the static. "The trench gate is icing over! The locking pins are frozen solid!"

"Drop from the tower, Ha-Eun!" Min-Jae shouted, unclipping his heavy *Tectonic Bulwark* from his back brace. "The parapet is exposed! We fight from the trench line!"

Min-Jae leaped over the railing, activating his hydraulic boot thrusters to cushion his descent into the snow-filled trench twenty-five meters below.

Ha-Eun did not retreat.

She racked the charging bolt of *The Cold Lens*. A pale, incandescent glow ignited along the rifle's barrel flutes, drawing the freezing ambient Void energy directly into the chamber. She pressed her eye to the rubber eyecup.

The entity was advancing across the glacial flats at Node 9.

It manifested as a colossal, translucent curtain of weeping ice—a towering feminine silhouette draped in endless sheets of frozen bridal lace, trailing eighty yards of jagged icicle tendrils across the ground. Inside the semi-transparent chest of the entity, suspended in a cage of solid glacial crystal, pulsed a frozen human heart that beat with slow, agonized, glacial rhythm.
"""
    lines.append(act2_prose_part1.strip() + "\n\n")
    
    breach_hud = [
        "ENTITY       : SE-C-IVd-103 (The Frozen Veil / Rank IV Entity)",
        "POTENCY      : Critical Potency d / Element: Void (Pale White)",
        "THERMAL LOSS : Ambient -68.4C / Frostbite Strain -22 Posture/Turn",
        "VOID PULL    : Absolute Emotional Numbness / Memory Erasure Hazard",
        "LETHAL THRESH: Complete Cryogenic Vitrification of Core Personnel"
    ]
    lines.append(wrap_box(bf.make_box("CONTAINMENT BREACH: CRYOGENIC PROFILE", breach_hud, width=71)))
    
    act2_prose_part2 = """The entity's presence fell over the outpost like a lead shroud.

```text
+=====================================================================+
|              OUTPOST E-09 PERIMETER DIAGNOSTIC REPORT               |
+---------------------------------------------------------------------+
| STRUCTURAL STATUS : Frontline Trench Parapet 62% Compromised        |
| PERSONNEL HEALTH  : Jinho Posture 45/140 | Min-Jae Posture 110/195  |
| COMPOSURE MONITOR : Taeho 58/110 (Shivering) | Ha-Eun 42/105        |
| ANCHOR LINK       : Unverified / Danger of Total Affective Erasure  |
+=====================================================================+
```

The voice did not come through the radio. It resonated directly through the glass optic of Ha-Eun's rifle, vibrating against her cheekbone.

*\"Why do you keep your hands warm, little needle?\"*

The voice was sweet, soft, and infinitely peaceful—like falling asleep in a drift of fresh powdered snow after marching thirty miles in the dark.

*\"Warmth is where the tears come from. If you let yourself freeze, you will never have to bury another comrade. You will never have to watch Min-Jae's shield buckle. You will never have to hear Taeho scream. Step into the veil. Give me your last warm memory, and I will give you eternal rest.\"*

Inside Ha-Eun's skull, the cold expanded.

Her Composure gauge plummeted: 105... 72... 42... 36.

She saw the final memory she had kept guarded in the deepest vault of her heart: a summer morning in the lower garden before the cycle resets began, sitting on a stone wall with her father, eating a ripe plum whose sweet juice ran down her fingers. The memory was warm. It smelled of sun-baked earth and fresh fruit.

The pale light of *The Cold Lens* flickered hungrily, its Void edge reaching toward that memory, preparing to consume it to fuel an ultimate piercing shot.

If she fired now without an anchor, she would kill the entity.

And she would wake up tomorrow having forgotten that she had ever had a father at all.

"Ha-Eun! Don't you dare close your eyes!"

A deafening roar shattered the whiteout.

Down in the trench at Node 4, Min-Jae slammed his *Bastion Aegis* into the icy ground. From the center of the basalt slab, a burst of emergency red flares ignited—not a weapon, but the burning sulfur of the squad's emergency survival beacons. A dome of flickering orange light washed across the frozen snow, pushing the biting frost back three paces.

"Ha-Eun!" Min-Jae roared into the blizzard, his eyebrows white with frost, his lips blue. "Remember the tea! The barley tea on the firing range! Cycle 1,740! Taeho spilled half the pot into his boots and cried like a baby because his toes smelled like grain!"

"It was good tea!" Taeho yelled from Node 5, swinging his heavy maul into a towering spear of glacial ice that had erupted from the trench floor. The kinetic impact sent shards of blue ice flying into the fog. "Don't let this ice-bitch take that memory, Ha-Eun! It's the only time Min-Jae ever smiled on a Monday!"

The ridiculous, stubborn words sliced through the suffocating fog in her brain.

The memory of her father did not vanish. It stayed, anchored by the ridiculous, profane reality of the two idiots standing in sixty-eight-below weather, freezing their blood to keep her from forgetting.

Ha-Eun let out a long, ragged gasp. Her teeth clattered, but the glaze of white numbness vanished from her eyes.

"Min-Jae," she whispered into the comms, her voice trembling with restored sensation. "Clear the line of sight. I'm taking the shot."

Min-Jae bared his bloodied teeth in a savage grin. "Line is open, needle. Shoot."
"""
    lines.append(act2_prose_part2.strip() + "\n\n---\n")
    
    # Act III
    lines.append("## Act III: The Resonant Catharsis (  공명의 정화  )\n")
    act3_rows = [
        "ACT III: THE RESONANT CATHARSIS (10-NODE TACTICAL RESOLUTION)",
        "LOCATION     : Outpost E-09 Perimeter Trench & Glacial Flats",
        "TIMESTAMP    : Fourth Watch (04:40 Tactical Engagement)",
        "ENGAGEMENT   : Iron Quad vs The Frozen Veil (10-Node Grid)",
        "OUTCOME      : Core Shatter / Anchor Verification Complete"
    ]
    lines.append(wrap_box(bf.make_box("TACTICAL DISPATCH: ACT III CLASH", act3_rows, width=71)))
    
    act3_prose_part1 = """The combat theater of Outpost E-09 was mapped across ten tactical nodes along the perimeter trench line, extending from the bunker threshold out onto the frozen glacial flats.
"""
    lines.append(act3_prose_part1.strip() + "\n\n")
    
    # 10-node spatial combat grid banner
    grid_lines = [
        bf.make_borderless_banner("10-NODE SPATIAL COMBAT GRID: OUTPOST E-09 PERIMETER DEFENSE", width=71),
        "[NODE 01] [NODE 02] [NODE 03] [NODE 04] [NODE 05] [NODE 06] [NODE 07] [NODE 08] [NODE 09] [NODE 10]",
        "[ Jinho ] [ Baffle] [       ] [Min-Jae] [ Taeho ] [ Ha-Eun] [       ] [       ] [ VEIL  ] [       ]",
        "[Bunker ] [ Trench] [ Empty ] [ANCHOR ] [STRIKER] [SNIPER ] [ Empty ] [ Empty ] [CORE   ] [ Empty ]",
        "-" * 71,
        "Node 01 : Sub-surface comms bunker / Jinho under survival thermal wrap.",
        "Node 02 : Trench access ramp / Heavy barbed wire entanglements.",
        "Node 03 : Mid-trench duckboards / Emergency sulfur flare station.",
        "Node 04 : Frontline defensive bastion / Min-Jae Bastion Shield wall.",
        "Node 05 : Forward trench salient / Taeho kinetic disruption point.",
        "Node 06 : Elevated observation parapet / Ha-Eun primary sniper perch.",
        "Node 07 : Outer perimeter barbed wire / Glacial advance threshold.",
        "Node 08 : The Precipice Line / Sub-zero cryogenic vortex boundary.",
        "Node 09 : The Frozen Veil Core / Floating glacial crystalline heart.",
        "Node 10 : The Outer Desolate Flats / Endless blizzard polar waste.",
        "=" * 71
    ]
    lines.append("```text\n" + "\n".join(grid_lines) + "\n```\n\n")
    
    lines.append("### Turn-Based Tactical Combat Resolution\n")
    lines.append("The suppression of `SE-C-IVδ-103 The Frozen Veil` was executed across six tactical turns within the primary combat phase, utilizing speed priority, action point investment, and the Four P-Framework:\n\n")
    
    combat_log_rows = [
        "TURN 1: SPEED INITIATION & FLASH-FREEZE ONSLAUGHT",
        "- The Frozen Veil activates [Absolute Zero Cascade] (Speed 7).",
        "- Temperature drops to -72C; Nodes 4-7 caked in solid glacial rime.",
        "- Min-Jae rolls Speed 3 (Bastion): Spends 2 AP on [Geothermal Flare]",
        "  anchoring his shield at Node 4. Flare aura grants +30 Frost Resist.",
        "- Min-Jae Posture: 145/195 | Composure: 78/110.",
        "-------------------------------------------------------------------",
        "TURN 2: TECTONIC SHATTER & ICE BREACH (PILLAR: PRESENCE)",
        "- Taeho rolls Speed 5: Spends 3 AP on [Thermal Maul Smash] at Node 5.",
        "- Heavy iron maul impacts the advancing ice wall (Clash 26 vs 22).",
        "- Victory Taeho! Outer ice barrier shattered; reveals Core at Node 9.",
        "- Presence Trigger: Ha-Eun witnesses the two men braving -70C to hold",
        "  the perimeter for her. Realizes she is anchored by their living warmth.",
        "- Ha-Eun Composure stabilizes: 42 -> 88/105. Posture: 150/170.",
        "-------------------------------------------------------------------",
        "TURN 3: ALIGNING THE CRYOGENIC APERTURE",
        "- Ha-Eun at Node 6 spends 2 AP on [Aperture Focus]:",
        "  Racks Cold Lens rifle chamber. Locks onto entity's frozen heart.",
        "- The Frozen Veil prepares lethal skill [Whiteout Memory Theft] (Spd 6)",
        "- Target: Ha-Eun at Node 6. Lethal mental drain charging.",
        "-------------------------------------------------------------------",
        "TURN 4: THE SUB-ZERO PRECIPICE (PILLAR: PRECIPICE)",
        "- The Frozen Veil projects spectral frost tentacles into the tower.",
        "- Tendrils coil around Ha-Eun's rifle, attempting to freeze her hands.",
        "- Precipice reached: Instead of retreating into numbness, Ha-Eun",
        "  embraces the physical pain of the freezing metal to maintain aim.",
        "- Pain validates life! Composure holds firm at 85/105.",
        "-------------------------------------------------------------------",
        "TURN 5: SIGNATURE ACTIVATION — BREAK THE PULL (PILLAR: PURPOSE)",
        "- Anchor Check Executed: Min-Jae confirms anchor bond over radio:",
        "  'I name Marksman Ha-Eun of the Iron Quad. Return to our warmth!'",
        "- Requirement met! Ha-Eun activates MAW-W-103-01 skill [Break the Pull].",
        "- A brilliant, pure white laser line cuts across the optic disc,",
        "  severing the entity's emotional drain without consuming her memory!",
        "-------------------------------------------------------------------",
        "TURN 6: CRITICAL SNIPER SUPPRESSION (PILLAR: PACT)",
        "- Ha-Eun pulls the trigger at Node 6: [Piercing White Silence]!",
        "- Clash Power: 44 vs 32! CRITICAL CLASH OVERWHELM!",
        "- High-velocity Void beam punches through the frozen heart at Node 9.",
        "- The Frozen Veil shatters into billions of glittering diamond flakes.",
        "- Atmospheric pressure normalizes. Dawn breaks over Outpost E-09."
    ]
    lines.append(wrap_box(bf.make_box("TACTICAL COMBAT LOG: TURNS 1 THROUGH 6", combat_log_rows, width=71)))
    
    act3_prose_part2 = """### The Climax of Act III

When Ha-Eun locked her crosshairs onto the frozen heart at Node 9, her breath was steady.

The rifle stock was so cold that the skin of her right cheek had frozen to the composite cheek-rest. Every millimeter of movement tore living flesh. Yet she did not flinch. She welcomed the sharp, burning agony—it was proof that she was still human, that she was still breathing, that she was not a ghost in an iron tower.

Through the scope, the towering feminine silhouette of *The Frozen Veil* opened its arms, preparing to release [Whiteout Memory Theft].

Around Ha-Eun, the frost tendrils shrieked as Min-Jae's sulfur flares pushed them back.

*\"I name Marksman Ha-Eun of the Iron Quad!\"* Min-Jae's voice roared through the earpiece, tearing away the entity's seductive lullaby like an axe cutting rope. *\"Return to our warmth!\"*

"Confirmed," Ha-Eun whispered.

Her gloved finger squeezed the trigger.

There was no deafening explosion. There was only a razor-thin, crystalline *SNICK*—the sound of an icicle snapping in absolute vacuum.

From the muzzle of *The Cold Lens*, a beam of pure, incandescent white light erupted. It was not fire; it was a line of perfect, absolute Void (  공허  ) energy that sliced through the howling blizzard at four thousand meters per second.

The white beam crossed the spatial gap from Node 6 to Node 9 in less than three milliseconds.

It struck the pulsing frozen heart dead center.

For a heartbeat, the entire mountain range went silent. The howling gale stopped. The clouds froze in the sky.

Then, the heart cracked.

A hairline fissure of blinding violet light shot through the glacial core. With the ringing chime of a cathedral chandelier shattering on marble, the sixty-meter colossus of ice imploded. A blinding shockwave of powdered snow and sparkling diamond dust swept across the ridge, dusting the trench parapet in a brilliant, harmless white blanket.

The sub-zero inversion broke.

The temperature gauge on the tower railing clicked upward: minus sixty... minus forty-five... minus twenty-eight.

The heavy grey clouds over the Desolate parted. For the first time in ninety days, a sliver of pale golden sunlight cut across the jagged peaks of Mugenhan, reflecting off the snow like scattered pearls.

Ha-Eun slowly pulled her face away from the rifle. A smear of red blood marked the cheek-rest where her skin had stuck to the cold metal, but she didn't care.

She unbuttoned her fleece respirator and took a deep, unfiltered breath of the mountain air. It was sharp, biting, and intensely cold—yet underneath the cold, she could smell the rich, sulfuric smoke of Min-Jae's flares, the oily tang of Taeho's maul, and the distant, earthy scent of melting pine rime.

She remembered.

She remembered her father's garden. She remembered the sweet plum. And looking down into the trench, she remembered every single face that had ever stood watch beside her.

Footsteps clattered up the metal ladder.

Min-Jae hauled his massive frame onto the platform, breathing heavily, steam billowing from his armor vents. Without saying a word, he pulled a fresh, unopened thermos from his combat rig, unscrewed the cap, and poured a brimming cup of dark, steaming barley tea.

He offered it to her.

Ha-Eun took the cup with both hands. Her fingers were still red, raw, and trembling, but as the heat seeped into her palms, she closed her eyes and let the warmth wash over her face.

"Good shot, needle," Min-Jae said softly.

Taeho's head popped up over the tower trapdoor, his cheeks covered in black soot from the flare canisters. "Did you save any tea for me, or did the ice queen drink it all?"

Ha-Eun looked down at the steaming cup, then looked up at Taeho. A genuine, radiant smile broke across her frost-burned face.

"I saved half, Taeho," she said softly. "Come up and drink."
"""
    lines.append(act3_prose_part2.strip() + "\n")
    
    content = "\n".join(lines)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Wrote {OUTPUT_PATH} ({len(content)} bytes)")

if __name__ == "__main__":
    build_canto_04()
