#!/usr/bin/env python3
"""
Generate SOMNARAK_GEOLOGY.md with perfect text-box symmetry,
zero HTML tags, zero dollar signs, and exhaustive in-universe lore.
"""

def make_box(width, title, lines):
    # width is total line length including borders
    inner_width = width - 4
    out = []
    top_border = "+" + "-" * (width - 2) + "+"
    out.append(top_border)
    if title:
        t_pad = title.center(inner_width)
        out.append(f"| {t_pad} |")
        out.append("+" + "-" * (width - 2) + "+")
    for l in lines:
        if len(l) > inner_width:
            raise ValueError(f"Line too long ({len(l)} > {inner_width}): {l}")
        l_pad = l.ljust(inner_width)
        out.append(f"| {l_pad} |")
    out.append("+" + "-" * (width - 2) + "+")
    return "```text\n" + "\n".join(out) + "\n```\n\n"

def build_geology_md():
    box1 = make_box(71, "PLANETARY GEOLOGICAL REGISTRY - PLANET MUGENHAN", [
        "Registry ID       : GEO-ARCHIVE-MUGENHAN-001",
        "Authority         : Directorate of Survey & Horizon Caravan",
        "Target Celestial  : Planet Mugenhan (Boundless Sorrow)",
        "Total Surface Area: 510,000,000 square kilometers",
        "Crustal Thickness : 35 to 80 kilometers (Silicate & Han Strata)",
        "Acoustic Frequency: 432 Hz Planetary Mantle Resonant Frequency",
        "Security Tier     : Sovereign Council Archive - Class I"
    ])

    box2 = make_box(71, "TERRITORIAL QUADRANT DISTRIBUTION - THE FOUR CORNERS", [
        "Corner 1 (Cheonji)   : Somnarak Sovereign Urban Basin (127.5M km2)",
        "Corner 2 (Cheonbulok): Forge Bastion & Foundries (127.5M km2)",
        "Corner 3 (Mugeukji)  : Numbing Frozen Tundra & Polar Cap (127.5M)",
        "Corner 4 (UnWiHan)   : Consoling Untouched Ocean & Wilds (127.5M)",
        "Central Transit      : Sea of Glass Vitrified Transport Route",
        "Endorheic Sink       : The Sorrow Lake (Sub-Surface Concentrated)"
    ])

    box3 = make_box(71, "SPECIAL ENVIRONMENTAL ZONES - CANONICAL FIELD ANCHORS", [
        "Zone [ConHeAn]    : Consoling Untouched Ocean (Primordial Basin)",
        "Zone [NuRoZen]    : Numbing Frozen Tundra (Polar Stasis Cap)",
        "Feature Alpha     : The Sorrow Lake (Rising Lament Sink)",
        "Feature Beta      : The Crystal Peaks (Acoustic Wind Barrier)",
        "Feature Gamma     : The Sea of Glass (Vitrified Obsidian Corridor)",
        "Feature Delta     : Mantle Terraces & Deep Agricultural Aquifers"
    ])

    content = f"""# Planetary Geology & Macro-Terrain of Mugenhan

---

{box1}
## 1. Executive Summary & Planetary Scale

Planet Mugenhan (무한 / Boundless Sorrow) spans a total surface area of approximately 510,000,000 square kilometers, possessing a physical scale and surface gravity equivalent to terrestrial baseline standards. Unlike celestial bodies characterized solely by inert mineral crusts and plate tectonic convection driven by thermal radioactive decay, Mugenhan's lithosphere, hydrosphere, and cryosphere are deeply interwoven with the metaphysical fluid medium known as Han (한).

The planet's internal structure consists of:
- **The Solid Silicate Crust (35–80 km):** A dense foundation of granite, basalt, and mineralized Han-crystal strata.
- **The Hydraulic Mantle (80–2,900 km):** A high-pressure convective layer where fluid Han circulates through vast tectonic subterranean channels (the Flerehan veins), maintaining a global acoustic hum of 432 Hz.
- **The Metallic-Crystalline Core (2,900–6,371 km):** A dense sphere of nickel-iron and petrified primordial Han, acting as the magnetic and metaphysical anchor of planetary coherence.

---

## 2. Macro-Territorial Distribution: The Four Corners (Sabang)

{box2}
The planetary landmass is traditionally categorized across Four Sovereign Quadrants (사방 — Sabang), each spanning roughly 127,500,000 square kilometers:

### 2.1 Corner 1: Cheonji — Somnarak Sovereign Basin
The northwestern quadrant, anchored by the sovereign city of Somnarak and the massive biological-tectonic root network of the Alpha Tree. This quadrant features:
- Extensive agrarian river valleys and terraced hills supporting over 70% traditional agriculture.
- The 10 km Desolate buffer zone encircling the outer bastions of Zone E.
- The deepest excavated subterranean strata (Fac-01 through Fac-05), penetrating into the ancient Cheongula fault lines.

### 2.2 Corner 2: Cheonbulok — The Forge-Tectonic Bastion
The eastern quadrant, defined by intense geothermal activity, volcanic basalt rifts, and heavy industrial foundries. It serves as the primary extraction center for raw kinetic metals and furnace coal, continually feeding industrial munitions to Corner 1 across the Sea of Glass.

### 2.3 Corner 3: Mugeukji — The Northern Stasis Waste
The polar quadrant, home to hyper-cryogenic permafrost plains, towering ice spires, and the vast expanse of the Numbing Frozen Tundra. Ambient kinetic activity drops to near-absolute zero, functioning as the planetary cryogenic sink where active sorrow is rendered inert through sheer cold.

### 2.4 Corner 4: UnWiHan — The Virgin Wilderness & Untouched Ocean
The southern and southeastern quadrant, characterized by wild, unpaved primordial ecosystems. Ancient old-growth forests, monumental river basins, and the endless expanse of The Consoling Untouched Ocean dominate this territory, entirely untouched by urban paving or corporate extraction.

---

## 3. Major Planetary Landmarks & Special Environmental Zones

{box3}

### 3.1 The Consoling Untouched Ocean [ConHeAn] (위안의 미답해)

The Consoling Untouched Ocean, designated in sovereign cartography as `[ConHeAn]`, is the largest open body of water on Planet Mugenhan, occupying over 65% of Quadrant 4 and extending beyond the southern maritime horizon.

#### Physical Characteristics
- **Water Composition:** Pure, pristine fluid Han in total laminar equilibrium. The water is completely devoid of industrial contaminants, heavy metals, or toxic particulate matter. It radiates a soft indigo-bioluminescent glow visible from high-altitude survey balloons.
- **Acoustic Signature:** Rather than crashing with violent wave breaks, the oceanic swells resonate at an infrasonic harmonic frequency of 528 Hz. This continuous, low-frequency hum acts as a planetary acoustic blanket.
- **Living Flora & Megafauna:** Unlike the dead Sorrow Lake, `[ConHeAn]` supports thriving elemental marine life. Towering blue glass kelp beds grow hundreds of meters tall, sheltering schools of translucent ribbon-fish and massive, gentle abyssal leviathans that filter raw ambient sorrow out of the ocean floor.

#### Metaphysical & Psychological Influence
- **Existential Consolation:** Exposure to the waters of `[ConHeAn]` induces a profound state of emotional resolution. Personnel standing along its shores report an immediate cessation of acute anxiety, anger, and grief. The water does not kill; it consoles, cradling the mind until painful memories soften into peaceful stillness.
- **The Drowning Risk (Peaceful Surrender):** Operatives entering the water without Class-5 anchor lines often experience an overwhelming desire to lie back and float forever. They feel no panic or pain; as their bodies slowly dissolve into the laminar fluid, they report feeling "finally at rest."
- **Institutional Quarantine:** The Council of Sighs strictly prohibits industrial dredging, mineral harvesting, or military installations along the coastline. `[ConHeAn]` is classified as a Planetary Sanctuary.

---

### 3.2 The Numbing Frozen Tundra [NuRoZen] (마비의 동토)

The Numbing Frozen Tundra, cataloged as `[NuRoZen]`, covers the northern third of Quadrant 3, forming a colossal polar cap of white dust, razor-sharp needle-ice, and permafrost glaciers.

#### Physical Characteristics
- **Cryogenic Parameters:** Ambient atmospheric temperatures consistently range between -55°C and -75°C, plunging to -90°C during polar vortex inversions.
- **White Dust Phenomenon:** The ground is blanketed not by standard frozen water snow, but by "White Dust" — micro-pulverized crystalline Han particles that absorb ambient thermal energy and kinetic friction.
- **Acoustic Freezing:** High-frequency sounds freeze directly in mid-air, crystallizing into brittle frost that falls to the snowbank with faint tinkling clicks. Normal vocal communication is impossible beyond thirty paces.

#### Metaphysical & Field Hazards
- **Emotional Anaesthesia:** The cold of `[NuRoZen]` does not merely freeze flesh; it numbs consciousness. Operatives operating within the tundra gradually lose the ability to feel distress, fear, grief, or personal attachment. While this prevents Panic states and Composure breaks, it creates a deadly psychological indifference to mortal danger.
- **Marble Stasis:** Personnel remaining stationary for more than twenty minutes risk irreversible crystallization. The blood and neural pathways freeze into translucent white Han jade, leaving the individual standing as a perfectly preserved, peaceful marble statue.
- **Survival Protocols:** Expeditions traversing `[NuRoZen]` rely on heavy tracked crawler rigs equipped with Grudge-burning thermal hearths and 432 Hz acoustic de-icing coils to maintain mental vitality.

---

### 3.3 The Sorrow Lake (한의 호수 — Han-ui Hosu)

Located in the southwestern tectonic depression between Somnarak's outer perimeter and the frontier of UnWiHan, The Sorrow Lake is an endorheic basin of concentrated dark liquid Han.

#### Geological Profile
- **Basin Scale:** Spanning approximately 340 kilometers across and reaching depths exceeding 1,800 meters.
- **Fluid Properties:** The lake contains pitch-black, highly dense fluid Han with zero organic plant or animal life. Its surface is mirror-smooth, completely undisturbed by surface winds.
- **The Rising Watermark:** Telemetry recorded over four centuries reveals that the lake's water level rises by approximately 2.3 centimeters per municipal decade. Geologists confirm that this rise corresponds directly to the cumulative unresolved sorrow generated by the urban population of Somnarak.
- **Hydraulic Pressurization:** Subterranean fissures beneath the lake feed the deep municipal pumps of Floor 4 and the Flerehan distillation plants.

---

### 3.4 The Crystal Peaks (크리스탈 봉우리 — Keuriseutal Bongwuri)

The northern alpine boundary separating Corner 1 from Corner 3 is dominated by the Crystal Peaks — a jagged, colossal mountain range whose summits exceed 7,200 meters above sea level.

#### Geological Profile
- **Tectonic Genesis:** Formed during ancient tectonic uplifts when high-pressure Han veins breached the crust at supersonic speeds, freezing into crystalline monoliths harder than industrial diamond.
- **Acoustic Needles:** The peaks are capped with thousands of slender, faceted crystal spires. As northern polar gales sweep across the ridges, these spires vibrate, shearing the wind into high-pitched harmonic soprano whistles (the Singing Needles).
- **Natural Alpine Shield:** The mountain wall prevents the hyper-cryogenic winds of `[NuRoZen]` from sweeping south into Somnarak's agricultural valleys, creating a natural thermal barrier.

---

### 3.5 The Sea of Glass (유리의 바다 — Yuri-ui Bada)

The Sea of Glass is a 2,400-kilometer transit corridor connecting Corner 1 (Somnarak) to Corner 2 (Cheonbulok).

#### Geological Profile
- **Vitrified Slag Plain:** The corridor was created during the ancient cataclysms of the Occlusihan War, where sustained orbital heat and high-potency Grudge strikes melted hundreds of square kilometers of silica bedrock into solid sheets of black obsidian and green glass.
- **Logistical Importance:** The surface is completely flat and devoid of soil or vegetation, serving as the primary overland trade route. Standard wheeled vehicles cannot operate due to razor-sharp obsidian shards; transit is maintained exclusively by the heavy, multi-wheeled sand-crawler rigs of the Horizon Caravan.
- **Thermal Heat Shimmer:** By day, solar reflection turns the glass surface into an incandescent mirror with temperatures exceeding 55°C; by night, rapid radiative heat loss plunges the surface to below freezing.

---

## 4. Subterranean Strata & Hydraulic Mechanics

The geological subsurface of Mugenhan is organized into distinct strata, meticulously cataloged by the Directorate of Territorial Survey:

| Stratum Layer | Depth Range | Lithological Composition | Metaphysical & Han Characteristics |
|---|---|---|---|
| **Stratum 01: Loam & Silt** | 0 to 50 m | Organic topsoil, alluvial clay, river sediment | Fertile agricultural soil sustaining municipal grain and root crops. |
| **Stratum 02: Basalt Crust** | 50 to 500 m | Dense volcanic basalt, granite bedrock | Structural foundation for city walls, towers, and surface aqueducts. |
| **Stratum 03: Crystalline Han Veins** | 500 to 2,500 m | Faceted Han crystal clusters, copper veins | Primary conduit network; mined for M.A.W. resonance and fuel cells. |
| **Stratum 04: The Flerehan Aquifer** | 2,500 to 6,000 m | Pressurized liquid Han aquifers, porous pumice | High-pressure hydraulic channels supplying municipal energy refineries. |
| **Stratum 05: The Cheongula Faults** | 6,000 to 15,000 m | Black tectonic slag, ancient foundation stone | Site of the First Sorrow; highly unstable tectonic fracture zones. |
| **Stratum 06: Deep Mantle Roots** | 15,000 m+ | Hyper-dense fluid mantle, Alpha Tree roots | Deep vault layer; anchors planetary acoustic resonance at 432 Hz. |

---

## 5. Planetary Cartographic Reference Matrix

| Geographic Zone | Quadrant / Corner | Primary Terrain | Dominant Han Element | Key Hazards & Features |
|---|---|---|---|---|
| **Somnarak Sovereign Basin** | Corner 1 (Cheonji) | Terraced valleys, urban foundation | Lament / Weight | Urban runoff, Desolate 10 km buffer, Alpha Tree root network. |
| **The Sorrow Lake** | Corner 1 / Corner 4 Border | Endorheic deep basin | Concentrated Lament | Dead black fluid, decade-scale rising water level, 0 organic life. |
| **The Sea of Glass** | Central Corridor | Vitrified obsidian sheets | Grudge / Weight | 2,400 km trade route, razor silica shards, extreme diurnal shifts. |
| **The Crystal Peaks** | Corner 1 / Corner 3 Border | Diamond-hard crystal spires | Void / Lament | 7,200 m summits, acoustic wind shear, Singing Needle hazards. |
| **Numbing Frozen Tundra [NuRoZen]** | Corner 3 (Mugeukji) | White dust permafrost | Weight / Void | -75°C polar freeze, Marble Stasis risk, emotional anaesthesia. |
| **The Consoling Untouched Ocean [ConHeAn]** | Corner 4 (UnWiHan) | Pristine fluid Han ocean | Lament | 528 Hz harmonic swell, glass kelp forests, peaceful surrender drift. |
| **Cheonbulok Foundry Basin** | Corner 2 (Cheonbulok) | Volcanic rifts, slag plains | Grudge | High-temperature foundries, heavy kinetic ordnance workshops. |

---

## 6. Archival Preservation Decree

This document stands as the definitive geographical codex of Planet Mugenhan. Any proposed municipal expansion, canal construction, or subterranean drilling exceeding Stratum 03 must submit environmental impact telemetry to the Directorate of Territorial Survey and the Horizon Caravan Geological Corps for acoustic resonance evaluation.

---

**Document ID:** `SOMNARAK-CODEX-GEO-001`  
**Registry Authority:** Directorate of Territorial Survey & Horizon Caravan  
**Classification:** Sovereign Archival Codex — Permanent Lore Standard
"""
    return content

if __name__ == "__main__":
    c = build_geology_md()
    with open("SOMNARAK-WORLD/Master_Codices/01_Cosmology_and_World_Order/SOMNARAK_GEOLOGY.md", "w", encoding="utf-8") as f:
        f.write(c)
    print("Successfully wrote SOMNARAK_GEOLOGY.md")
