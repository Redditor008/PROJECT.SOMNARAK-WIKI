#!/usr/bin/env python3
"""
tools/build_jipyeongseondae_overview.py
Generates:
- SOMNARAK-WORLD/Jipyeongseondae/JIPYEONGSEONDAE_OVERVIEW.md
"""

import unicodedata

def get_display_width(text):
    w = 0
    for ch in text:
        if unicodedata.east_asian_width(ch) in ('F', 'W'):
            w += 2
        else:
            w += 1
    return w

def pad_to_display_width(text, target_width):
    cur_w = get_display_width(text)
    if cur_w < target_width:
        return text + " " * (target_width - cur_w)
    elif cur_w > target_width:
        # truncate safely
        res = ""
        res_w = 0
        for ch in text:
            ch_w = 2 if unicodedata.east_asian_width(ch) in ('F', 'W') else 1
            if res_w + ch_w > target_width:
                break
            res += ch
            res_w += ch_w
        return res + " " * (target_width - res_w)
    return text

def make_box(title, rows, width=71):
    top = "+" + "=" * (width - 2) + "+"
    bottom = "+" + "=" * (width - 2) + "+"
    sep = "+" + "-" * (width - 2) + "+"
    inner_width = width - 4
    
    out = [top]
    if title:
        title_str = f" {title} "
        title_w = get_display_width(title_str)
        left_pad = (width - 2 - title_w) // 2
        right_pad = width - 2 - title_w - left_pad
        out.append("|" + " " * left_pad + title_str + " " * right_pad + "|")
        out.append(sep)
    
    for r in rows:
        if r == "---":
            out.append(sep)
        elif r.startswith("==="):
            out.append(top)
        else:
            padded = pad_to_display_width(r, inner_width)
            out.append(f"| {padded} |")
    out.append(bottom)
    return "\n".join(out)

def generate_overview():
    overview_box = make_box("JIPYEONGSEONDAE OPERATIONAL SPECIFICATION", [
        "ARCHIVE CODE    : JIPYEONGSEONDAE-OVERVIEW-4238",
        "INSTITUTION     : The Horizon Caravan (Jipyeongseon Dae)",
        "PRIMARY VESSEL  : The Drift Throne (140m Mobile Sand Cruiser)",
        "EXPEDITION HEAD : Kael, The Drift King (Former Warden Commander)",
        "REGIONAL GUIDE  : Hwaran, The Furnace Defector (Cheonbulok)",
        "---",
        "PLANETARY EXPEDITION THEATER:",
        "- Origin Base   : Somnarak Zone E - The Exile's Gate",
        "- Intermediate  : The Desolate Interior (The Sea of Glass)",
        "- Target Alpha  : Cheonbulok - The City of a Thousand Rages",
        "- Target Beta   : Mugeukji - The City of Absolute Silence (Unreached)",
        "---",
        "TACTICAL SYSTEM ENGAGEMENT:",
        "- Combat Arena  : 10-Node Horizontal Land Grid ([N01] to [N10])",
        "- Action System : Dynamic Speed / Action Points (AP 2 to 5)",
        "- Spatial Range : Range Bands 1 to 5 (Melee to Global Artillery)",
        "- Armor Engine  : M.A.W.-W Quad-Weight Classes (Light to Fortress)"
    ])

    stage_box = make_box("THE 10-NODE EXPEDITION SPATIAL GRID ARCHITECTURE", [
        "[STAGE NODES 01 TO 10 - OVERLAND EXPEDITION THEATER]",
        "[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N09]---[N10]",
        "[RAMPS] [SKIM]  [BARR]  [BASIN] [APEX]  [PYLON] [DUNES] [CHASM] [VENT]  [CORE]  ",
        "---",
        "- [N01] Ramp / Intercept: Crawler debarkation ramp (Point-Blank Band 1)",
        "- [N02] Skimmer Flank   : Rapid sand-skimmer outrider deployment",
        "- [N03] Sand Barricade  : Fortified dune berms / portable ballistic shields",
        "- [N04] Mid-Sand Basin  : Primary vanguard clash zone (Range Band 2)",
        "- [N05] Boss Anchor Apex: Sovereign entity apex / heavy enemy commander",
        "- [N06] Pylon Catwalk   : Hydraulic telescopic sniper & spotter masts",
        "- [N07] Rear Sand Dunes : Heavy artillery & acoustic mortar fire line",
        "- [N08] Sand Chasm Sump : Unstable shifting sinkhole hazard zone",
        "- [N09] Ley-Line Vent   : Geothermal Han-flow geyser (Thermal/Void hazard)",
        "- [N10] Command Bridge  : Drift Throne bridge & siege railgun battery"
    ])

    threat_box = make_box("REGIONAL URBAN THREAT MATRIX (UTS-1 TO UTS-4)", [
        "UTS-1: LOW HAZARD      | Somnarak Zone E outskirts, dust mites, light ash",
        "UTS-2: MODERATE HAZARD | The Desolate, Han-storms, Burrowers, nomads",
        "UTS-3: HIGH HAZARD     | Border fortress garrisons, kinetic batteries",
        "UTS-4: CRITICAL HAZARD | Volcanic furnace calderas, Void sensory null"
    ])

    crew_box = make_box("DRIFT THRONE CREW ROSTER & SPECIFICATIONS", [
        "[COMMANDER]  : Kael (Drift King) - Heavy Trench-Cleaver / Ley-Pulse",
        "[GUIDE]      : Hwaran (Furnace Defector) - Volcanic Staff / Ash Ward",
        "[OUTRIDERS]  : Dune Scouts - Sand-Skimmers / Kinetic Rifles",
        "[VANGUARD]   : Heavy Dredgers - Class IV Exo-Suits / Pile-Drivers",
        "[NAVIGATORS] : Ley-Seers - Subterranean Acoustic Sonar Array",
        "[FLAGSHIP]   : The Drift Throne - 142.5m Tracked Mobile Fortress"
    ])

    return f"""# Jipyeongseondae Overview: The Horizon Caravan Operational Guide (지평선대 총람 / 地平線隊 總覽)
## Tactical Overland Navigation, Planetary Traverse Mechanics, and Expedition Combat Architecture

```text
{overview_box}
```

> *"Somnarak told us that beyond the walls there was only death. They lied to keep us small. There is death in the sand, yes—titan worms that swallow land-crawlers whole, glass storms that shred iron, and fires that burn without fuel. But there are also people. There are other cities crying in the dark. And we will build a road between them."*  
> — Kael, The Drift King, Year 4238

---

## I. Ontological & Geopolitical Foundation

### 1. The Tri-City Disconnection
For forty-two centuries following the great planetary fracture, humanity's remnants believed their home city was the solitary survivor of the apocalypse:
- **Somnarak (솜나락)**: The City of Unresolved Sorrow. Ruled by the bureaucratic Council of Sighs and fortified within concentric blast walls. Focused on emotional containment and sorrow crystal harvesting.
- **Cheonbulok (천불옥 / 千火獄)**: The City of a Thousand Rages. Located 2,400 kilometers to the southeast across the Desolate. Carved into an active volcanic caldera, its society is governed by gladiatorial combat, boiling iron foundries, and the sacred Great Furnace.
- **Mugeukji (무극지 / 無極地)**: The City of Absolute Silence. Located 3,100 kilometers to the north-northwest. An enigma encased within a 100-kilometer sensory nullification perimeter where sound, emotion, and memory are erased.

### 2. The Desolate: The Sea of Glass and Han-Flows
The overland wastes separating these civilization hubs are known collectively as **The Desolate (황야)**. Far from being an inert desert, the Desolate is an active, vibrating mantle of crystallized mineral grief:
- **Han-Flow Lines (한류맥)**: Deep seismic acoustic rivers of sorrow flowing through the planetary crust. Where these lines intersect, the ground stabilizes, allowing heavy vehicles to traverse the sand without sinking into bottomless dust chasms.
- **Glass-Storms (유리 폭풍)**: Atmospheric disturbances where temperatures plummet to $-40^\\circ\\text{{C}}$ while supersonic winds sweep razor-sharp shards of crystallized sorrow across the dunes.

---

## II. The Drift Throne & Nomadic Crew Specialization

```text
{crew_box}
```

### 1. Kael — The Drift King
A decorated former Warden Commander who was exiled into the wastes in Year 4192. Over four decades of harsh wilderness exposure, his body adapted to planetary Han radiation, turning his left arm into vitrified Han-glass. He commands the Drift Throne with absolute tactical authority, wielding the **Obsidian Trench-Cleaver** and directing acoustic shockwaves that stabilize sandy terrain.

### 2. Hwaran — The Furnace Defector
A native of Cheonbulok who escaped the city's sacrificial Battle Pits. She possesses intimate knowledge of volcanic slag navigation, Cheonbulok clan politics, and the thermal instabilities of the Great Furnace. In combat, she wields the **Volcanic Cinder-Staff**, deploying thermal smoke barriers and neutralizing hostile firestorms.

### 3. The Specialist Contingents
- **Dune Scouts**: Fast reconnaissance units riding high-speed treaded skimmers. They occupy forward nodes (`[N02]`, `[N03]`), executing hit-and-run rifle skirmishes and painting targets for the crawler's main batteries.
- **Heavy Dredgers**: Elite shock troopers equipped with reinforced hydraulic pile-drivers and deployable bulwarks. They anchor frontline defense nodes (`[N01]`, `[N03]`), absorbing kinetic shocks from colossal burrowers.
- **Ley-Seers**: Mnemonic navigators stationed at the helm (`[N10]`), interpreting real-time subterranean acoustic readings to prevent the crawler from driving into abyssal sinkholes.

---

## III. The 10-Node Expedition Tactical Combat Grid

```text
{stage_box}
```

### 1. The 10-Node Spatial Topology
Every combat engagement in the Jipyeongseondae chronicles is mapped onto a discrete 10-node horizontal battle stage:
- **Node 01 (`[N01]`) — Ingress Ramps / Crawler Hull**: Debarkation gangway of the Drift Throne. Provides $+2$ Protection to friendly units holding this node.
- **Node 02 (`[N02]`) — Skimmer Outrider Lane**: Rapid flanking lane for light vehicles and outriders. Grants $+15\\%$ Evasion.
- **Node 03 (`[N03]`) — Sand Barricade Line**: Fortified dune berms equipped with deployable kinetic barricades.
- **Node 04 (`[N04]`) — Mid-Sand Basin**: Forward clash zone where medium melee and short-range skirmishes collide.
- **Node 05 (`[N05]`) — Sovereign Boss Anchor**: The central node occupied by the primary adversary, behemoth construct, or enemy commander.
- **Node 06 (`[N06]`) — Pylon Catwalk**: Elevated telescopic sniper mast and acoustic sensor array. Grants Range Band $+1$ to marksmen.
- **Node 07 (`[N07]`) — Rear Dune Ridge**: Elevated sandbank utilized by heavy mortar teams and support casters.
- **Node 08 (`[N08]`) — Sand Chasm Sump**: Dangerous shifting sand hazard. Units entering this node suffer $-2$ Speed and must test Posture to avoid sinking.
- **Node 09 (`[N09]`) — Subterranean Ley-Vent**: Geothermal vent erupting with boiling Han-brine or volatile steam every 3 turns.
- **Node 10 (`[N10]`) — Drift Throne Command Bridge / Siege Battery**: The central command deck housing Kael's throne and the long-range kinetic railgun.

### 2. Speed, Action Points (AP), and Range Bands
- **Action Points (AP)**:
  $$\\text{{AP}} = \\max\\left(2, \\lfloor \\text{{Base Speed}} / 2 \\rfloor + \\text{{Equipment Modifiers}}\\right)$$
- **Range Bands 1 to 5**:
  * **Band 1 (Melee / Point-Blank)**: Adjacent node attacks (Target distance: $\\Delta N = 1$). Full kinetic cleaves and pile-driver impacts.
  * **Band 2 (Close Assault)**: Short range (Target distance: $\\Delta N = 2$). Shotgun blasts and thermal flamethrowers.
  * **Band 3 (Mid-Field Tactical)**: Medium range (Target distance: $\\Delta N = 3$). Kinetic battle rifles and targeted acoustic javelins.
  * **Band 4 (Long-Range Ballistic)**: Heavy fire (Target distance: $\\Delta N = 4$). Mortar bombardments and anti-materiel sniper fire.
  * **Band 5 (Extreme Global Siege)**: Massive artillery (Target distance: $\\Delta N \\ge 5$). Drift Throne spinal railgun strikes.

### 3. M.A.W.-W Armor Weight Classes
- **Light Outrider ($W < 25\\text{{kg}}$)**: Speed $+2$, Evasion $+15\\%$, AP $+1$.
- **Medium Warden ($25\\text{{kg}} \\le W \\le 60\\text{{kg}}$)**: Standard baseline profile, no speed penalties, balanced posture.
- **Heavy Dredger ($61\\text{{kg}} \\le W \\le 120\\text{{kg}}$)**: Speed $-1$, Protection $+3$, Poise $+20$. Immune to light stagger.
- **Fortress Crawler ($W > 120\\text{{kg}}$)**: Speed $-2$, Protection $+6$, Poise $+50$. Unyielding Armor Block.

### 4. The Four P-Framework
- **P1: Passives (고유 지속효과)**: Innate environmental adaptations (e.g., Kael's *Glass-Veined Resilience*, Hwaran's *Slag-Walker*).
- **P2: Panic / Composure (침착도 및 혼란)**: 0 to 50 SP scale. Glass storms inflict environmental Composure erosion; zero SP causes Blind Panic or Lethargy.
- **P3: Parry / Protection (흘리기 및 보호)**: High-speed parries that deflect projectile vectors across spatial nodes.
- **P4: Posture / Poise (체간 및 치명 집중)**: Posture gauges regulate stagger states; poise stacks guarantee critical structural breaks.

### 5. Dual-Threshold Stagger Engine
- **Stagger 1 (60% Posture Strain / Part Dismantling)**: Triggered when an adversary's key structural component (e.g., crawler tread, weapon arm, furnace vent) is reduced to 0 HP or their Posture reaches 60% strain. Cancels channeled special attacks and inflicts $+50\\%$ vulnerability for 1 turn.
- **Stagger 2 (0% Posture Collapse / Terminal Overdrive)**: Triggered when the entity's total Posture drops to 0. The target is completely immobilized, stripped of defensive coins, and exposed to catastrophic Execution Finishers.

---

## IV. Trans-Planetary Route Stratigraphy & Threat Scales

```text
{threat_box}
```

The Caravan's journey is graded along four Urban Threat Scales:
- **UTS-1 (Zone E Outskirts)**: Low-level border skirmishes, minor sand mites, and localized dust clouds.
- **UTS-2 (The Desolate Interior)**: Severe Han-glass storms, rogue dune corsairs, and Class-IV subterranean burrowers.
- **UTS-3 (City Frontiers & Garrisons)**: Heavy artillery emplacements, automated kinetic barrier forts, and sovereign border patrols.
- **UTS-4 (City Interiors & Cores)**: Volcanic caldera eruptions, gladiatorial death matches, and absolute sensory null fields.

---

## V. The Six Expedition Arcs Summary & Reading Order

```text
+=====================================================================+
|               THE SIX EXPEDITION ARCS OF JIPYEONGSEONDAE            |
+=====================================================================+
| Arc 1: Departure              | Somnarak Zone E: The Exile's Gate   |
| Arc 2: The Desolate Crossing  | The Desolate: The Sea of Glass      |
| Arc 3: Arrival at Cheonbulok  | Cheonbulok: The Volcanic Caldera    |
| Arc 4: The Furnace's Secret   | Cheonbulok: The Great Furnace Core  |
| Arc 5: The Return             | The Desolate: Return Trade Corridor |
| Arc 6: The Mugeukji Attempt   | Mugeukji: Absolute Silence Border   |
+=====================================================================+
```

1. **[Arc 1: Departure](Arc_1_Departure.md)**: Kael brings the Drift Throne to Somnarak's gates. Clashes with the Warden Border Battery to force the Council to ratify the Overland Expedition Charter.
2. **[Arc 2: The Desolate Crossing](Arc_2_The_Desolate_Crossing.md)**: The Caravan braves the deep Sea of Glass, confronting a 200-meter Glass-Dune Colossus during a category-5 Han-storm.
3. **[Arc 3: Arrival at Cheonbulok](Arc_3_Arrival_at_Cheonbulok.md)**: Entering the volcanic caldera of Cheonbulok, Kael fights in the gladiatorial Battle Pits against Slag Champion Barok to earn an audience with the Furnace Keepers.
4. **[Arc 4: The Furnace's Secret](Arc_4_The_Furnaces_Secret.md)**: Entering the cracking core of the Great Furnace, Kael and Hwaran confront the agonizing grief of a dying city and rescue 400 fleeing Ash Walkers.
5. **[Arc 5: The Return](Arc_5_The_Return.md)**: Escorting the massive refugee convoy back toward Somnarak, the Caravan repels an ambush by the Desolate Sand-Corsairs, establishing the first permanent trade route.
6. **[Arc 6: The Mugeukji Attempt](Arc_6_The_Mugeukji_Attempt.md)**: The Caravan ventures north to contact Mugeukji, confronting the horrifying sensory null field of the Archon of the Void before executing a strategic withdrawal to preserve the crew's sanity.
"""

def main():
    path = "SOMNARAK-WORLD/Jipyeongseondae/JIPYEONGSEONDAE_OVERVIEW.md"
    with open(path, "w", encoding="utf-8") as f:
        f.write(generate_overview())
    print("Generated JIPYEONGSEONDAE_OVERVIEW.md successfully!")

if __name__ == "__main__":
    main()
