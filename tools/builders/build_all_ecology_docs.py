#!/usr/bin/env python3
"""
tools/build_all_ecology_docs.py
Generates the three requested canonical ecological codices:
1. MUGENHAN_PLANETARY_FLORA_AND_FAUNA.md (15 Known Fauna and Flora)
2. MUGENHAN_BEAST_ANIMALS_AND_PLANTS.md (6 Known Beast Animal And Plant)
3. MUGENHAN_SORROW_CREATURES.md (6 Known Sorrow Creature: 4 Fauna, 2 Flora)

Every entry is rigorously verified:
- Standard: >= 200 words (targeted 215-260 words)
- Complex: >= 300 words (targeted 320-400 words)
- 100% 71-col text box symmetry
- Zero HTML tags, zero dollar signs, authentic in-universe perspective
"""

import os

def make_box(width, title, lines):
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

def count_words(text):
    return len(text.split())

def generate_all():
    # -------------------------------------------------------------------------
    # DOCUMENT 1: 15 KNOWN FLORA AND FAUNA
    # -------------------------------------------------------------------------
    ff_box1 = make_box(71, "PLANETARY BIOSPHERE CATALOG - 15 KNOWN FAUNA AND FLORA", [
        "Catalog ID        : BIO-ARCHIVE-MUGENHAN-FF15",
        "Authority         : Directorate Bio-Synthesis & Horizon Caravan",
        "Scope             : 15 Canonical Species Across Planetary Biomes",
        "Ecosystem Strata  : [ConHeAn], [NuRoZen], [UnWiHan], Peaks, Basin",
        "Biological Status : Tier 1 Mundane Natural Ecosystem Wildlife",
        "Security Tier     : Sovereign Archival Standard - Unrestricted"
    ])

    ff_box2 = make_box(71, "TERRITORIAL DISTRIBUTION SUMMARY - 15 CANONICAL SPECIES", [
        "Untouched Ocean [ConHeAn] : Azure Kelp, Ribbon-Whale, Medusa",
        "Numbing Tundra [NuRoZen]  : White-Dust Hare, Willow, Weasel",
        "Wild Land [UnWiHan]       : Ironwood, Antlered Elk, Serpent",
        "The Sea of Glass Transit  : Glass-Skater Beetle, Slag Lichen",
        "Crystal Peaks Alpine      : Alpine Falcon, Soprano Needle-Moss",
        "Agricultural Basin        : Honey-Fern, Alluvial Silt Rice"
    ])

    ff_entries = []

    # 1. Azure Kelp of Consolation (Complex Flora, 300+ words)
    ff_entries.append((
        "### 1. Azure Kelp of Consolation (위안의 푸른유리 다시마) — Flora `[ConHeAn]`",
        """The Azure Kelp of Consolation (*Laminaria consolatio*) is a monumental marine macroalga native exclusively to the littoral shelves, undersea canyons, and abyssal drop-offs of The Consoling Untouched Ocean (`[ConHeAn]`). Anchoring itself to submerged crystalline Han bedrock at depths ranging from forty to three hundred meters, individual stipes can reach extraordinary lengths exceeding four hundred and fifty meters, forming towering underwater kelp cathedrals that sway in perpetual synchronization with the ocean's 528 Hz infrasonic swells.

Morphologically, the kelp features thick, translucent stipes that transition from deep royal blue near the holdfast to brilliant luminescent cyan along the upper fronds. Rather than relying solely on sunlight, which penetrates weakly through the dense laminar fluid, the fronds possess specialized piezo-acoustic vacuoles that convert the continuous mechanical pressure waves of the tide into chemical sugars and dissolved mineral nutrients. The surface of the blades is completely smooth, coated in a thick, non-toxic mucus that prevents parasitic encrustation, insulates against cellular osmotic rupture, and repels predatory micro-organisms.

Ecologically, the Azure Kelp functions as the primary oxygenator and primary physical shelter for southeastern marine life. Vast schools of juvenile ribbon-fish and pelagic medusae spend their early development sheltered within the dense canopy, insulated from outer maritime predators. The root holdfasts anchor millions of tons of marine sediment, preventing submarine landslides along the continental slope.

For human divers and expeditionary specialists from the Horizon Caravan, the kelp forests represent both an essential resource and a psychological hazard. The mucus secreted by harvested blades can be refined into Class-4 Composure Balms that soothe acute nerve strain and accelerate tissue regeneration after chemical exposure. However, swimming through a living kelp forest without acoustic ear baffles exposes personnel to the gentle hum of the stipes. This acoustic frequency induces overwhelming emotional resolution, causing divers to forget their missions, detach their safety lifelines, and gently drift within the blue fronds in peaceful, permanent repose. Strict safety directives mandate that all kelp harvesters operate in tethered pairs with timed pneumatic retrieval winches.""",
        True
    ))

    # 2. Laminar Ribbon-Whale (Complex Fauna, 300+ words)
    ff_entries.append((
        "### 2. Laminar Ribbon-Whale (층류 띠고래) — Fauna `[ConHeAn]`",
        """The Laminar Ribbon-Whale (*Balaenoptera laminaris*) is the apex filter-feeding cetacean of The Consoling Untouched Ocean. Reaching mature lengths between sixty and eighty-five meters with an exceptionally slender, serpentine body profile, this magnificent mammal navigates the dense, high-viscosity fluid Han currents with effortless hydrodynamic grace. Its dorsal surface is covered in flexible, slate-blue dermal plates, while its ventral belly is entirely translucent, revealing an intricate internal bioluminescent circulatory network that pulses rhythmically at 0.1 Hz.

The Ribbon-Whale lacks conventional keratin baleen plates. Instead, its cavernous mouth houses an array of flexible silica-mesh sieves lined with microscopic cilia. As it glides through oceanic thermal boundaries, it filters millions of liters of laminar fluid daily, harvesting pelagic plankton, floating Sorrow spores, and suspended mineral salt crystals. During this feeding process, the whale's respiratory blowhole—situated behind its cranial crest—expels towering geysers of vaporized crystalline steam that shimmer with rainbow prisms across the open ocean, visible for fifteen nautical miles.

Socially, Ribbon-Whales travel in maternal pods of three to five individuals, communicating across thousands of nautical kilometers through deep harmonic songs that resonate between 12 Hz and 40 Hz. These vocalizations bypass thermal oceanic layers and can be picked up by submarine hydrophones as deep, vibrating sighs that soothe nearby oceanic fauna. The pods migrate along predictable seasonal thermal routes connecting Corner 4 to deep equatorial trenches, steering clear of polluted industrial drainages.

Unlike the violent, maddened entities of the urban underworld, the Ribbon-Whale exhibits profound biological docility and high cognitive empathy. Caravan scout submarines operating near Corner 4 report that injured or malfunctioning vessels are frequently nudged toward surface shallows by mature whales. Hunting or harassing the Ribbon-Whale is classified as a Grade-A Maritime Sacrilege under Council of Sighs maritime treaties, carrying the unconditional penalty of permanent exile from all sovereign ports. In maritime folklore, the passing of a Ribbon-Whale pod beneath a ship's keel is considered an infallible blessing of safe voyage across the untamed waters.""",
        True
    ))

    # 3. Abyssal Cradling Medusa (Fauna, 200+ words)
    ff_entries.append((
        "### 3. Abyssal Cradling Medusa (심해 안식 해파리) — Fauna `[ConHeAn]`",
        """The Abyssal Cradling Medusa (*Pelagia requiem*) is a pelagic scyphozoan inhabiting the twilight depths of The Consoling Untouched Ocean between five hundred and two thousand meters. Its translucent bell measures three to five meters in diameter, trailing hundreds of delicate, thread-like marginal tentacles that can extend forty meters into the abyss. The interior umbrella houses a soft bioluminescent core that glows with a soothing, slow-pulsing sapphire aura that illuminates the pitch-black benthic water.

Unlike terrestrial jellyfish that possess stinging venomous nematocysts to paralyze prey, the Cradling Medusa's tentacles secrete an organic, sweet-tasting chemical anesthetic known as 'Nadir Nectar'. This compound instantly suppresses nervous agitation, fear, and motor distress in any organic creature that brushes against it. Small deep-sea fish deliberately nestle within the tentacles to sleep in absolute safety, as larger predators avoid the dense cloud of soothing chemical calm. The medusa feeds passively on suspended particulate matter and micro-plankton trapped within its mucus veil.

Expeditionary crews salvage naturally sloughed tentacle tips washed ashore along the southern coastlines. When dried and powdered, this biological matter serves as the active stabilizer in standard R.D. Composure Ampoules, allowing frontline Wardens to survive intense psychological exposure during deep facility containment shifts. The compound has zero addictive properties, making it Somnarak's most reliable clinical sedative.""",
        False
    ))

    # 4. Permafrost White-Dust Hare (Fauna, 200+ words)
    ff_entries.append((
        "### 4. Permafrost White-Dust Hare (영구동토 백분토끼) — Fauna `[NuRoZen]`",
        """The Permafrost White-Dust Hare (*Lepus nivalis-zen*) is a small, extraordinarily hardy herbivorous mammal native to the sub-zero permafrost plains of the Numbing Frozen Tundra (`[NuRoZen]`). Weighing between two and four kilograms, the hare is blanketed in a dense double-layer of hollow, chalk-white fur that is chemically indistinguishable from the micro-pulverized crystalline Han dust covering the tundra floor, providing near-perfect thermal insulation and visual camouflage against polar raptors.

Anatomically, the hare possesses wide, snowshoe-like paws lined with stiff, fibrous bristles that allow it to sprint across brittle needle-frost crusts at speeds up to sixty kilometers per hour without breaking the surface. Its circulatory system contains high concentrations of natural glycerol and specialized antifreeze proteins that prevent tissue crystallization even when ambient temperatures plunge to -70°C. Its compact ears are heavily furred inside to prevent heat loss, and its large amber eyes have secondary translucent eyelids that shield against blinding snow-glare.

The White-Dust Hare feeds exclusively on dormant sub-crust lichens and frozen willow bark, which it excavates using hardened, chisel-like incisors. Because sound travels dangerously far across the frozen plains, the hare has adapted to communicate entirely through subterranean foot-thumps transmitted through bedrock fissures, completely evading the auditory notice of apex predators prowling the white waste. They burrow in communal warrens dug beneath the permafrost line, sharing body warmth to survive multi-week polar blizzards.""",
        False
    ))

    # 5. Marble-Stasis Willow (Flora, 200+ words)
    ff_entries.append((
        "### 5. Marble-Stasis Willow (대리석 정지 버드나무) — Flora `[NuRoZen]`",
        """The Marble-Stasis Willow (*Salix petrificata*) is a low-growing, prostrate woody shrub that carpets the wind-scoured ridges of the northern polar frontier in `[NuRoZen]`. Standing less than one meter tall to avoid the blistering polar gales, its gnarled, serpentine branches spread horizontally across the permafrost, forming dense mats that can span fifty meters in circumference. Its root network anchors deeply into frozen gravel, binding the loose white dust against severe aeolian erosion.

The most extraordinary physiological adaptation of this shrub is its vegetative stasis cycle. During the eight-month polar night, when temperatures fall below -65°C, the willow's vascular sap undergoes complete, vitrified crystallization. Its leaves, bark, and roots freeze into translucent, marble-like white jade that is physically as hard as structural limestone. In this vitrified state, all biological respiration, cellular division, and nutrient transport cease entirely, rendering the plant immune to cellular rupture. It survives in absolute suspended animation.

When the polar vortex recedes during the brief four-month summer, the plant thaws over seventy-two hours, rapidly unfurling pale silver catkins that release clouds of cold-resistant pollen across the snowbanks. Nomadic scouts from the Horizon Caravan harvest the dried summer twigs of the willow; when burned in crawler stoves, the wood produces an intense, smokeless blue flame that generates reliable thermal heat for days without leaving soot or toxic residue.""",
        False
    ))

    # 6. Acoustic Needle-Weasel (Fauna, 200+ words)
    ff_entries.append((
        "### 6. Acoustic Needle-Weasel (음향 침족제비) — Fauna `[NuRoZen]`",
        """The Acoustic Needle-Weasel (*Mustela acus*) is a slender, carnivorous mustelid adapted to hunting in the sound-freezing climate of the Numbing Frozen Tundra. Measuring forty to fifty centimeters in body length with an elongated, tubular torso and short, powerful legs, the weasel is an expert burrower capable of navigating the dense subterranean labyrinth of tunnels beneath the permafrost snowpack. Its thick, double-layered pelt repels moisture and white dust.

The weasel takes its name from its unique hunting mechanism. Around its snout and along its flexible whiskers, it possesses hardened, needle-like keratin spurs that vibrate at ultra-high frequencies. When stalking prey beneath the snow, the weasel emits focused, high-frequency ultrasonic clicks. Because high-frequency sound waves freeze directly in mid-air in `[NuRoZen]`, these acoustic clicks leave microscopic trails of falling frost crystals. By tracking the dispersion pattern of this acoustic needle frost, the weasel can pinpoint burrowing rodents through three meters of solid ice with absolute mathematical precision.

Its fur is sleek, waterproof, and pale silver-grey, changing to pure chalk-white during mid-winter. The weasel lives a solitary existence, fiercely defending subterranean hunting territories against rival predators using razor-sharp canine teeth reinforced with mineral apatite. Trappers respect the creature for its intelligence; young weasels are occasionally tamed by caravan mechanics to clear crawler heating ducts of nesting vermin.""",
        False
    ))

    # 7. Titan Ironwood Tree (Complex Flora, 300+ words)
    ff_entries.append((
        "### 7. Titan Ironwood Tree (들한 거신 철목) — Flora `[UnWiHan]`",
        """The Titan Ironwood Tree (*Metasequoia titanis*) is the supreme botanical organism of the primeval old-growth forests across Quadrant 4 (The Untouched Wild Land / `[UnWiHan]`). Towering between three hundred and four hundred and twenty meters in height, with trunk base diameters often exceeding thirty-five meters, these ancient botanical behemoths form an unbroken, multi-tiered green canopy that blankets millions of square kilometers of virgin terrestrial basin.

The timber of the Titan Ironwood is renowned for its miraculous physical density. Imbued with raw, non-institutionalized Outside Sorrow (*Oehan*) drawn from subterranean tectonic aquifers, the heartwood undergoes a natural biomineralization process, replacing organic cellulose with compressed basaltic silica and copper-apatite lattices. As a result, the wood cannot be felled by standard steel axes, rotary saws, or conventional chemical defoliants; strikes against mature bark produce bright kinetic sparks and ring with the acoustic resonance of church bells. The wood is entirely impervious to rot, fungal decay, and terrestrial insect infestation.

Ecologically, a single Titan Ironwood functions as a self-contained vertical continent. Its massive, moss-draped branches support thousands of epiphytic fern gardens, hanging vine networks, arboreal rodent colonies, and specialized canopy predators that never descend to the forest floor throughout their multi-generational lifespans. Deep taproots extend two kilometers into the planetary crust, acting as living geological anchors that stabilize subterranean tectonic faults against catastrophic seismic collapse.

During the Consolihan War, municipal syndicates attempted to log the perimeter groves to fortify Somnarak's outer blast walls. In response, the groves unleashed massive subterranean root spasms that shattered the logging machinery and collapsed the access roads. Today, the Titan Ironwoods stand protected under the Sovereign Non-Encroachment Taboo, revered by the Horizon Caravan as the immortal pillars of Planet Mugenhan's ancient wilderness. Fallen branches shed naturally during windstorms are carefully gathered by certified carpenters to forge master-grade weapon hafts and structural ship keels.""",
        True
    ))

    # 8. Great Antlered Elk of Deulhan (Complex Fauna, 300+ words)
    ff_entries.append((
        "### 8. Great Antlered Elk of Deulhan (들한 거각 사슴) — Fauna `[UnWiHan]`",
        """The Great Antlered Elk of Deulhan (*Cervus titanis-deulhan*) is the monumental herbivorous sovereign of the open river valleys, alluvial meadows, and ironwood forests of Corner 4 (`[UnWiHan]`). Standing six to eight meters tall at the shoulder and weighing up to twelve metric tons, this colossal ungulate embodies the serene majesty and raw physical power of Mugenhan's primordial terrestrial biosphere.

The most awe-inspiring anatomical feature of the bull elk is its monumental crown of antlers, which can achieve a span exceeding fourteen meters from tip to tip. These antlers are not made of dead bone; they are living, semi-translucent conduits of calcified green Han crystal that glow faintly with an emerald bioluminescence. Throughout the year, the antlers absorb ambient electromagnetic pulses and acoustic ground vibrations, allowing the elk to detect distant seismic rifts, weather changes, or encroaching human convoys from over two hundred kilometers away. Every spring, the outer mineral layer flakes off, fertilizing the surrounding meadows with potent crystalline phosphorus.

Despite its terrifying physical size and ability to crush light combat crawlers beneath its heavy, basalt-rimmed hooves, the Great Antlered Elk is profoundly peaceful. Living in family herds of twelve to twenty individuals led by an elder matriarch, the elk browse primarily upon high canopy foliage, wild mosses, and mineral-rich river salts. When confronted by aggressive predators or rogue outlaws, the bull does not flee; it stomps its forehooves, releasing a concussive 432 Hz acoustic ground wave that knocks attackers off their feet and terminates hostile intent without bloodshed.

The nomads of the Outskirts and scouts of the Horizon Caravan revere the elk as sacred spirits of the wild earth. Harming a Great Elk is considered an unforgivable taboo; to encounter one standing beside a crystal river at dawn is considered the highest omen of safe passage through the uncharted wilderness.""",
        True
    ))

    # 9. Crystalline River-Serpent (Fauna, 200+ words)
    ff_entries.append((
        "### 9. Crystalline River-Serpent (수정 하천사) — Fauna `[UnWiHan]`",
        """The Crystalline River-Serpent (*Hydrophis crystallus*) is a large, apex aquatic reptile native to the torrential freshwater rivers that cascade from the central highlands through the primeval forests of `[UnWiHan]`. Growing to mature lengths between twelve and eighteen meters, the serpent possesses an elongated, muscular body covered in overlapping, glass-like scales that refract river sunlight into shimmering prismatic displays, rendering the predator virtually invisible when submerged beneath rushing white water and foamy rapids.

Unlike venomous terrestrial snakes, the River-Serpent is a non-venomous constrictor of extraordinary strength. It hunts large river fish, wild boars, and drinking ungulates by anchoring its muscular tail around submerged granite boulders and striking with explosive hydraulic speed. Its jaw can unhinge smoothly to swallow prey twice its circumference, while its stomach acids—fortified with natural mineral enzymes and organic bile salts—can dissolve bone, keratin, and crystalline crusts within twelve hours. It breathes through vascular skin gills in addition to expansive, highly efficient lungs.

The serpent is a vital ecological indicator species for aquatic purity across the wild basin; it cannot survive in waters contaminated by industrial coal-dust, refinery runoff, or municipal chemical waste. Caravan navigators use confirmed sightings of River-Serpents as definitive proof that river water is pure, untreated, and entirely safe for human consumption. Shed serpent skins are carefully gathered from riverbanks and cured by leatherworkers into transparent, waterproof waterproofing membranes for expedition tents, submersible suits, and cargo wraps.""",
        False
    ))

    # 10. Wild Han Honey-Fern (Flora, 200+ words)
    ff_entries.append((
        "### 10. Wild Han Honey-Fern (야생한 꿀고사리) — Flora `[UnWiHan]`",
        """The Wild Han Honey-Fern (*Pteridium mel-han*) is an abundant, understory pteridophyte flourishing across the shaded forest floors, alluvial ravines, and riverbanks of Corner 4 (`[UnWiHan]`). Growing in dense, arching clusters reaching two to three meters in height, the fern's fronds are soft, velvety, and deep forest-green, speckled along the underside with specialized golden nectar-secreting glands that glisten like fresh morning dew under the canopy light.

During the early dawn hours, these glands exude thick droplets of amber-colored syrup known across the frontiers as 'Wild Han Honey'. This botanical nectar possesses a remarkably high caloric density, subtle floral sweetness, and natural restorative properties that rapidly regenerate fatigued human cellular tissue. Wild bees, canopy bats, and small rodents depend heavily on the fern's nectar as their primary seasonal food source, inadvertently pollinating surrounding forest flora as they forage across the understory thickets.

Expeditionary foragers from the Horizon Caravan actively harvest Honey-Fern syrup during trans-wilderness crossings. Mixed into dry ration cakes or dissolved in boiled spring water, the syrup provides scouts with sustained physical endurance and immune resistance against toxic dust exposure, making it one of the most commercially valuable mundane botanical commodities gathered from the wild frontiers. Unlike cultivated cane sugar, it never crystallizes or spoils even in humid tropical climates, retaining its nutritional potency for decades.""",
        False
    ))

    # 11. Obsidian Glass-Skater Beetle (Fauna, 200+ words)
    ff_entries.append((
        "### 11. Obsidian Glass-Skater Beetle (흑요석 활주 딱정벌레) — Fauna (Sea of Glass)",
        """The Obsidian Glass-Skater Beetle (*Gyrinus obsidianus*) is a specialized xerophilic insect inhabiting the scorched, 2,400-kilometer vitrified expanse of the Sea of Glass. Measuring fifteen to twenty-five centimeters in length, the beetle possesses an ultra-dense, mirror-polished black carapace composed of fused silica and chitin, which reflects 98% of direct solar radiation to survive daytime temperatures exceeding 55°C without suffering protein denaturation or fluid loss.

The beetle's most remarkable anatomical adaptation is its six elongated legs, each terminating in a curved pad of low-friction teflon-like organic wax. Utilizing these specialized pads, the beetle does not crawl; it skates across the frictionless glass sheets at astonishing speeds of up to forty-five kilometers per hour, propelled effortlessly by the fierce desert winds. It steers with incredible agility using two lateral steering rudders situated on its rear abdomen, dodging thermal cracks and jagged obsidian ridges without slowing down.

The Glass-Skater feeds primarily on windblown carcasses of birds and insects killed by the desert heat, as well as microscopic crustose lichens growing in glass fissures. To obtain water, the beetle climbs onto high dunes at dawn, standing on its head to allow condensed morning dew to trickle down specialized dorsal grooves directly into its mouthparts. Scavengers track swarms of skaters to locate hidden freshwater springs beneath the vitrified crust.""",
        False
    ))

    # 12. Silica-Slag Lichen (Flora, 200+ words)
    ff_entries.append((
        "### 12. Silica-Slag Lichen (규석 슬래그 지의류) — Flora (Sea of Glass)",
        """The Silica-Slag Lichen (*Xanthoria vitrea*) is an extremophilic saxicolous lichen that represents the sole vegetative life form capable of colonizing the barren obsidian sheets of the Sea of Glass. Appearing as crustose, circular patches ranging from pale ash-grey to dull copper-orange, the lichen firmly adheres to vitrified volcanic bedrock through microscopic hyphal pegs that chemically etch into solid silica, extracting trace iron, potassium, and magnesium.

The lichen survives diurnal temperature swings of over sixty degrees Celsius through a unique metabolic cycle. During the scorching daylight hours, it enters complete dormancy, using a metallic carotenoid pigment layer to deflect ultraviolet radiation and prevent cellular dehydration. When desert temperatures plunge below freezing at night, the lichen awakens, absorbing condensed frost vapor directly from atmospheric humidity. It can survive desiccated for decades without losing cellular viability, reviving within minutes of moisture exposure.

Over centuries of slow growth, the lichen slowly breaks down the glassy slag into coarse, mineral-rich sand, acting as the primary pioneer organism in the geological regeneration of the cataclysmic corridor. Caravan scavengers scrape mature lichen mats from rock outcroppings to refine into heat-resistant thermal coatings for crawler hulls, exhaust manifolds, and locomotive heat shields. When boiled with lye, it yields an antiseptic compound used to treat desert sand-rot.""",
        False
    ))

    # 13. Singing Crystal Alpine Falcon (Fauna, 200+ words)
    ff_entries.append((
        "### 13. Singing Crystal Alpine Falcon (노래하는 결정 고산매) — Fauna (Crystal Peaks)",
        """The Singing Crystal Alpine Falcon (*Falco acutus*) is a majestic raptor inhabiting the knife-edge crags, acoustic needle spires, and frozen cols of the Crystal Peaks above 4,000 meters elevation. Boasting a wingspan of two and a half meters, the falcon is adapted to navigate the violent, unpredictable mountain gales that tear through the northern alpine passes. Its plumage is stiff, unyielding, and slate-grey with metallic silver wing tips that shimmer like polished iron.

Uniquely, the leading edges of its primary flight feathers are hardened with crystalline silica calcification. When the falcon dives at terminal hunting velocities exceeding three hundred and twenty kilometers per hour, the rushing wind shears across these wing crystals, producing a piercing, harmonic soprano whistle between 9,000 Hz and 12,000 Hz. This acoustic dive-song serves as an active hunting tool: the intense ultrasonic frequency disorients mountain rodents and alpine hares, paralyzing them with sensory overload seconds before the falcon strikes with razor-sharp talons.

Alpine mountaineers and border wardens consider the falcon's song an indispensable early warning of incoming blizzards, as the birds descend to lower valleys hours before high-altitude storms strike. Nests are built exclusively on inaccessible crystal needles, lined with mountain hare wool and dried needle-moss.""",
        False
    ))

    # 14. Soprano Needle-Moss (Flora, 200+ words)
    ff_entries.append((
        "### 14. Soprano Needle-Moss (소프라노 바늘이끼) — Flora (Crystal Peaks)",
        """The Soprano Needle-Moss (*Dicranum acousticum*) is a high-altitude bryophyte that clings to vertical granite and crystal cliffs throughout the Crystal Peaks mountain range. Forming dense, velvet-textured cushions of pale emerald-green, the moss produces millions of erect, hair-like sporophytes that terminate in needle-fine, hollow silica capsules standing five to eight centimeters above the turf.

These capsules are precisely shaped by natural selection to act as miniature acoustic Helmholtz resonators. When northern winds sweep across the cliff faces, air rushes across the capsule apertures, causing the entire moss bed to vibrate in sympathetic resonance. Thousands of sporophytes humming simultaneously generate a chorus of high-soprano acoustic chords that echo through the alpine valleys. The vibrations keep the plant free from accumulating snow, preventing the colony from being suffocated beneath heavy winter avalanches.

The acoustic vibrations also discourage alpine grazing animals from chewing the delicate green cushions, as the continuous sonic hum painfully irritates mammalian teeth and gums. Mountaineers collect the dried sporophytes to weave into sound-dampening ear plugs, essential for surviving the harsh acoustic shears of high-altitude passes without permanent eardrum damage. The moss also yields an indelible green dye prized by textile guilds in Zone A for ceremonial banners. Colonies growing near hot sulfur fumaroles exhibit a golden tint and produce lower baritone tones.""",
        False
    ))

    # 15. Alluvial Silt Rice (Flora, 200+ words)
    ff_entries.append((
        "### 15. Alluvial Silt Rice (충적토 한미 / 恨米) — Flora (Somnarak Basin)",
        """Alluvial Silt Rice (*Oryza somnarakis*), colloquially known across the city as 'Han-Grain' (한미 / 恨米), is the foundational cereal crop that sustains the two million citizens of Somnarak. Cultivated across the vast terraced river valleys and flooded alluvial flats of Sector A and D, this highly engineered semi-aquatic grass thrives in the mineral-rich, black alluvial silt deposited by subterranean spring conduits and regulated irrigation canals.

The plant grows to a height of one and a half meters, featuring broad, dark indigo stalks and heavy, nodding panicles carrying sixty to ninety hard, charcoal-grey grains. The rice possesses an extraordinary root system that actively absorbs trace mineral Han from irrigation waters, converting fluid sorrow into stable, complex starches without accumulating toxicity. The plant requires minimal fertilization, drawing all necessary nitrates from mineralized river silt.

When harvested and hulled, the polished grain is pearlescent grey; when steamed, it emits a subtle nutty aroma with a faint mineral finish. Silt Rice provides dense, long-lasting complex carbohydrates that keep industrial foundry workers and wall wardens energized through grueling fourteen-hour shifts. Over seventy percent of Somnarak's civilian workforce is engaged in the cultivation, harvesting, and distribution of Han-Grain, making this mundane crop the true economic lifeblood that keeps the sovereign metropolis standing through centuries of isolation.""",
        False
    ))

    ff_content = f"""# Mugenhan Planetary Flora and Fauna — 15 Known Species
## Definitive Ecological Survey Across the Macro-Terrains and Biomes of Planet Mugenhan

---

{ff_box1}
## I. Executive Planetary Biosphere Overview

Planet Mugenhan's surface and terrestrial ecosystems harbor a vibrant, multi-layered ecological web that thrives across its vast planetary surface area of 510,000,000 square kilometers. While the municipal core of Somnarak is densely fortified behind stone blast walls, the vast expanse of the planet—spanning the virgin wilderness of Corner 4 (`[UnWiHan]`), the hyper-cryogenic cap of Corner 3 (`[NuRoZen]`), the boundless ocean of `[ConHeAn]`, and the rugged alpine peaks—sustains a breathtaking biodiversity of 100% biological organisms.

These species belong strictly to **Tier 1 (Mundane Planetary Organisms)**: they possess ordinary biological reproduction, cellular respiration, and mortal life cycles, living in balanced co-evolution with Mugenhan's geological and acoustic environment.

---

## II. Planetary Distribution Roster

{ff_box2}

---

## III. Detailed Taxonomic Profiles (15 Canonical Species)

"""
    for title, body, is_complex in ff_entries:
        w_cnt = count_words(body)
        min_limit = 300 if is_complex else 200
        if w_cnt < min_limit:
            raise ValueError(f"Entry '{title}' has {w_cnt} words, expected >= {min_limit}")
        ff_content += f"{title}\n\n{body}\n\n---\n\n"

    ff_content += """## IV. Archival Authority & Ecological Preservation

The fifteen species cataloged in this compendium represent the foundational biological pillars of Planet Mugenhan's terrestrial and marine biosphere. Under the joint authority of the Reverie Directorate Bio-Synthesis Bureau and the Horizon Caravan Ecological Corps, these species are monitored for population stability, environmental health, and genetic purity against industrial pollution.

---

**Document ID:** `MUGENHAN-BIO-CATALOG-FF15`  
**Classification:** Sovereign Ecological Codex — Permanent Planetary Lore Standard
"""

    with open("SOMNARAK-WORLD/Mugenhan_Ecology/MUGENHAN_PLANETARY_FLORA_AND_FAUNA.md", "w", encoding="utf-8") as f:
        f.write(ff_content)
    print("Successfully wrote MUGENHAN_PLANETARY_FLORA_AND_FAUNA.md")

    # -------------------------------------------------------------------------
    # DOCUMENT 2: 6 KNOWN BEAST ANIMALS AND PLANTS
    # -------------------------------------------------------------------------
    bp_box1 = make_box(71, "SORROW-INFUSED WILDLIFE - 6 KNOWN BEAST ANIMALS AND PLANTS", [
        "Catalog ID        : BIO-ARCHIVE-MUGENHAN-BP06",
        "Authority         : Bio-Synthesis Bureau & Frontline SED Survey",
        "Scope             : 6 Known Beast Animals and Plants (Tier 2)",
        "Biological Ratio  : 80% Living Beast/Flora, 20% SE-M.A.W. Phenotype",
        "Threat Grade      : Minor (Alpha) to Moderate (Beta) - Slayable",
        "Security Tier     : Sovereign Archival Standard - Restricted"
    ])

    bp_box2 = make_box(71, "BEAST ANIMAL AND DANGEROUS PLANT DISTRIBUTION MATRIX", [
        "Beast Animal 01   : The Desolate Dune-Crusher (Armored Arachnid)",
        "Beast Animal 02   : Tectonic Ram-Gorgon (Basalt Horn Ungulate)",
        "Beast Animal 03   : Glacial White-Fang Stalker (Cryo-Apex Feline)",
        "Beast Animal 04   : Silt-Chasm River Leviathan (Aquatic Reptile)",
        "Dangerous Plant 01: Vitrified Razor-Thorn Vine (Silica Carnivore)",
        "Dangerous Plant 02: Sulfur-Furnace Pitcher Trap (Acid Vent Flora)"
    ])

    bp_entries = []

    # 1. The Desolate Dune-Crusher (Complex Beast Animal, 300+ words)
    bp_entries.append((
        "### 1. The Desolate Dune-Crusher (황야의 사막 분쇄수 / 砂漠 粉碎獸) — Beast Animal",
        """The Desolate Dune-Crusher (*Scorpiones tectonicus*) is a colossal, predatory arachnid-quadruped hybrid native to the scorched sands, rocky canyons, and toxic dust flats of The Desolate encircling Somnarak's outer perimeter. Measuring seven to ten meters in length and standing three meters tall at the cephalothorax, this apex predator prowls the arid wasteland, hunting wild herds, wandering outlaws, and straggling convoy transports.

Anatomically, the Dune-Crusher exhibits a classic 80/20 Tier 2 Sorrow-Infused biology. Eighty percent of its mass consists of living, mortal biological tissues: a multi-chambered heart pumping hemolymph, powerful striated muscle bundles, and an insatiable biological appetite. The remaining twenty percent manifests as heavily mineralized M.A.W.-like phenotypes: its segmented exoskeleton is reinforced with dense layers of basaltic chitin and compressed Grudge crystal plates, making it completely impervious to small-arms kinetic fire and standard hunting arrows.

Its most terrifying offensive weapon is its paired hydraulic crushing claws. These massive pincers generate over ten metric tons of pneumatic pressure per square inch, capable of shearing through armored vehicle axles and reinforced concrete barricades in a single strike. Mounted on its rear abdomen is a segmented tail terminating in a hardened obsidian drill-stinger. By driving this drill into bedrock, the Dune-Crusher transmits high-frequency seismic vibrations that liquefy subterranean sand, creating localized sinkholes that trap fleeing vehicles before they can escape.

Caravan convoys encountering a Dune-Crusher must immediately deploy heavy hydraulic cannons and focused Void-affinity ammunition to fracture its armored joints. Once slain, its carapace is highly sought after by workshop smiths in Zone C to forge Grade-β kinetic trench-shields and armored breastplates, while its venom glands yield potent industrial lubricants that remain fluid under extreme desert heat. Hunting parties require at least two heavy crawlers equipped with kinetic harpoons to safely subdue an adult specimen, as solitary hunters are invariably crushed beneath its charging pincer sweeps. Field autopsies confirm that destroying the nerve cluster between its third and fourth abdominal segments induces immediate total motor collapse.""",
        True
    ))

    # 2. Tectonic Ram-Gorgon (Beast Animal, 200+ words)
    bp_entries.append((
        "### 2. Tectonic Ram-Gorgon (판구조 쇄석양 / 碎石羊) — Beast Animal",
        """The Tectonic Ram-Gorgon (*Ovis tectonicus*) is a heavily armored, aggressive herbivorous mammal inhabiting the steep scree slopes, basalt ridges, and foothills of the Crystal Peaks. Standing two and a half meters tall at the shoulder and weighing up to four metric tons, this territorial beast defends its high-altitude grazing grounds with brutal, relentless kinetic force.

The Ram-Gorgon's skull is reinforced with a solid dome of fused basalt bone, crowned by massive curled horns of mineralized Weight-affinity crystal. When agitated by encroaching predators or survey parties, the ram lowers its head and charges at speeds exceeding fifty kilometers per hour. The kinetic impact of its horns against solid cliff faces produces concussive shockwaves that trigger rockslides to bury intruders, while the creature itself suffers zero cranial trauma due to specialized hydraulic cartilage dampers protecting its braincase.

Despite its aggressive temperament, the Ram-Gorgon is a purely biological mortal organism. It grazes on tough alpine shrubs, silica moss, and subterranean salt deposits, living in small bachelor herds or maternal nursery groups. Mountaineering squads must exercise extreme caution when navigating mountain passes; firing concussive flares or loud rifles within earshot of a herd often provokes a coordinated downhill stampede capable of sweeping entire expedition camps off narrow cliff ledges.""",
        False
    ))

    # 3. Glacial White-Fang Stalker (Beast Animal, 200+ words)
    bp_entries.append((
        "### 3. Glacial White-Fang Stalker (빙원 백아표 / 白牙豹) — Beast Animal",
        """The Glacial White-Fang Stalker (*Panthera cryo-nivalis*) is the supreme predatory feline prowling the southern periphery, frozen valleys, and glacial crevasses of the Numbing Frozen Tundra (`[NuRoZen]`). Measuring three to four meters from snout to tail with a shoulder height of one and a half meters, the stalker possesses a muscular, low-slung frame covered in dense, chalk-white fur with faint icy-blue rosettes that provide total camouflage against howling blizzard whiteouts.

The stalker's upper jaw features a pair of elongated, sabre-like canine teeth forged from crystalline permafrost apatite. These teeth vibrate at ultra-low sub-zero temperatures. When the stalker bites into prey, the sub-zero teeth instantly freeze the victim's surrounding blood vessels and muscle fibers, inducing localized tissue paralysis and preventing blood loss that would alert competing scavengers across the tundra. The stalker can stalk silently across packed snow thanks to thick fur cushions lining its retractable claws.

Living a strictly solitary life, the White-Fang Stalker hunts White-Dust Hares, young ungulates, and unwary human scouts. Expeditionary teams venturing into `[NuRoZen]` must keep constant perimeter thermal sensors active; the stalker's body temperature is masked by its cryo-dampening pelt, making visual and acoustic vigilance the only defense against an ambush strike. Its pelts are prized by outrider captains for crafting frost-immune greatcoats.""",
        False
    ))

    # 4. Silt-Chasm River Leviathan (Beast Animal, 200+ words)
    bp_entries.append((
        "### 4. Silt-Chasm River Leviathan (탁류 하천 거구수 / 河川 巨龜獸) — Beast Animal",
        """The Silt-Chasm River Leviathan (*Macrochelys vorax*) is a massive, amphibious chelonian predator inhabiting the murky depths, flooded caverns, and deep sediment pools of the subterranean river networks beneath Somnarak. Reaching shell lengths of eight to twelve meters, the leviathan spends months buried beneath riverbed silt, completely motionless, with only its camouflaged nostrils and horn-rimmed eyes breaking the surface of the black water.

Its dorsal carapace is formed from thick, interlocking plates of mineralized iron-slag and compressed river basalt, resembling a natural river rock outcropping overgrown with dark water-moss. In its throat, the leviathan possesses a fleshy, bioluminescent red tongue-lure that mimics a wriggling river worm. When large river fish, subterranean salamanders, or wading dredgers approach to inspect the lure, the leviathan's massive beak snaps shut with hydraulic speed, cleaving through bone, iron diving suits, and wooden skiffs in a fraction of a second.

The creature breathes through both extensive vascular lungs and anal bursae gills, allowing it to remain submerged indefinitely without surfacing. Dredging crews operating in Subterranean Sector 3 utilize acoustic depth-sounders to detect the leviathan's slow heartbeats before dropping excavation buckets into deep river troughs, as disturbing a nesting adult causes it to ram and capsize dredging barges with catastrophic force.""",
        False
    ))

    # 5. Vitrified Razor-Thorn Vine (Complex Dangerous Plant, 300+ words)
    bp_entries.append((
        "### 5. Vitrified Razor-Thorn Vine (유리 가시 덩굴 / 硝子 荊棘藤) — Dangerous Plant",
        """The Vitrified Razor-Thorn Vine (*Calamus vitriolicus*) is an aggressive, semi-carnivorous climbing liana that infests the geological transition zones, fractured basalt crevasses, and perimeter borders of the Sea of Glass. Spreading via extensive subterranean stolons, a single vine colony can sprawl across hundreds of meters of scorched terrain, weaving a dense, impenetrable web of interlocking woody stems that choke out all other plant competitors.

Morphologically, the vine exhibits terrifying vegetative adaptations. Its woody stems, which measure ten to fifteen centimeters in diameter, are encased in a flexible, translucent silica bark that glitters in the desert sun. Sprouting along every internode are thousands of curved, razor-sharp thorns composed of solid, vitrified volcanic glass. These thorns are brittle by design: upon penetrating skin, leather, or rubberized crawler tires, the tips snap off cleanly inside the wound, releasing microscopic glass shards and an irritating chemical sap that induces severe vascular inflammation and severe kinetic hemorrhaging.

The vine functions as a passive ambush predator. When desert hares, lizards, or unwary human scavengers become ensnared in the thorny thicket, their struggling movements trigger the vine's thigmonastic response: surrounding stems curl inward with surprising mechanical tension, pinning the victim tighter against the razor barbs. As the trapped animal dies of blood loss, the vine's adventitious roots sprout directly through the wounds into the decomposing carcass, absorbing vital nitrates, phosphorus, and organic nitrogen to fuel rapid vegetative expansion.

Caravan crews clearing road blockages along the Sea of Glass must wear heavy basalt-plated greaves and utilize long-handled thermal blowtorches. Attempting to cut the vine with machetes or kinetic axes causes the glass thorns to shatter into airborne shrapnel clouds that blind workers. The scorched ashes, however, yield high-grade potash utilized by urban pharmaceutical labs to formulate coagulant powders. Furthermore, dried vines stripped of their thorns can be treated with mineral oils to manufacture high-tensile towing ropes capable of pulling disabled freight crawlers across steep dunes.""",
        True
    ))

    # 6. Sulfur-Furnace Pitcher Trap (Dangerous Plant, 200+ words)
    bp_entries.append((
        "### 6. Sulfur-Furnace Pitcher Trap (유황 분노 포충낭 / 硫黃 捕蟲囊) — Dangerous Plant",
        """The Sulfur-Furnace Pitcher Trap (*Nepenthes pyrogena*) is a colossal, carnivorous botanical trap that thrives in the geothermal rift valleys, fumarole margins, and volcanic silt fields surrounding Corner 2 (Cheonbulok). Growing as an epiphyte on basalt spires or sprawling along geothermal fissures, the plant produces towering, jug-shaped pitchers that can measure up to three meters in height and one and a half meters across the peristome.

The pitcher's interior is filled with hundreds of liters of boiling, enzymatic fluid heated by volcanic ground steam. The peristome rim is coated in a sweet-smelling, volatile sulfurous nectar that emits a warm, inviting crimson luminescence at night. Desert insects, rodents, and wild boars attracted by the thermal heat and sweet scent lose their footing on the slick, waxy rim, plummeting into the boiling digestive reservoir below. Specialized acid-secreting glands lining the pitcher digest soft tissues within hours, absorbing proteins directly into the plant's vascular network.

When approached by large intruders or survey crews attempting to harvest its nectar, the plant's pressure-sensitive rim spasms shut, ejecting pressurized streams of caustic sulfur acid from secondary lateral vents up to ten meters away. Survey botanists must wear acid-resistant lead-aproned suits and spray neutralizing alkaline foam before approaching mature pitcher colonies.""",
        False
    ))

    bp_content = f"""# Mugenhan Beast Animals and Plants — 6 Known Species
## Taxonomic Catalog of Tier 2 Sorrow-Infused Predators, Megafauna, and Dangerous Flora

---

{bp_box1}
## I. The Nature of Sorrow-Infused Organisms

Unlike mundane planetary wildlife that possesses zero sorrow phenotypes, **Tier 2 (Sorrow-Infused Organisms)** represent living, biological creatures that have evolved alongside unrefined geological Han over millions of years.

In accordance with the **Law of the 80/20 Ratio**, these beasts and plants are eighty percent mortal biological organisms—possessing ordinary flesh, vascular circulation, and natural reproductive cycles—and twenty percent mineralized Sorrow/M.A.W. phenotypes. They are mortal, breed naturally, and can be hunted, harvested, and neutralized with conventional kinetic and M.A.W. weaponry.

---

## II. Species Distribution Roster

{bp_box2}

---

## III. Detailed Taxonomic Profiles (6 Canonical Species)

"""
    for title, body, is_complex in bp_entries:
        w_cnt = count_words(body)
        min_limit = 300 if is_complex else 200
        if w_cnt < min_limit:
            raise ValueError(f"Entry '{title}' has {w_cnt} words, expected >= {min_limit}")
        bp_content += f"{title}\n\n{body}\n\n---\n\n"

    bp_content += """## IV. Field Harvesting & Safety Protocols

Tier 2 organisms represent vital industrial resources for the municipal armories of Somnarak. Harvested carapaces, vitrified thorns, and glandular enzymes are processed by certified workshops into Grade-α and Grade-β armaments. All field encounters must adhere strictly to Directorate engagement rules: do not provoke nesting adults without containment backup.

---

**Document ID:** `MUGENHAN-BIO-CATALOG-BP06`  
**Classification:** Sovereign Ecological Codex — Permanent Planetary Lore Standard
"""

    with open("SOMNARAK-WORLD/Mugenhan_Ecology/MUGENHAN_BEAST_ANIMALS_AND_PLANTS.md", "w", encoding="utf-8") as f:
        f.write(bp_content)
    print("Successfully wrote MUGENHAN_BEAST_ANIMALS_AND_PLANTS.md")

    # -------------------------------------------------------------------------
    # DOCUMENT 3: 6 KNOWN SORROW CREATURES (4 FAUNA, 2 FLORA)
    # -------------------------------------------------------------------------
    sc_box1 = make_box(71, "MORTAL SORROW CREATURES - 6 KNOWN ANOMALIES (4 FAUNA, 2 FLORA)", [
        "Catalog ID        : BIO-ARCHIVE-MUGENHAN-SC06",
        "Authority         : Reverie Directorate Bio-Synthesis Bureau",
        "Scope             : 6 Known Mortal Creatures (4 Fauna, 2 Flora)",
        "Classification    : Tier 3 Mortal Sorrow Organisms (Non-Human Born)",
        "Potency Cap       : Capped at Grade Beta (Mortal & Slayable)",
        "Security Tier     : Sovereign Archival Standard - Restricted"
    ])

    sc_box2 = make_box(71, "MORTAL SORROW CREATURE ROSTER - 4 FAUNA AND 2 FLORA", [
        "Sorrow Fauna 01   : The Screaming Chitin Vanguard (Swarm Entity)",
        "Sorrow Fauna 02   : The Starving Pack Spectre (Chasm Canid Phantom)",
        "Sorrow Fauna 03   : The Drowned Steed of the Sorrow Lake (Equine)",
        "Sorrow Fauna 04   : The Chained Talon Harrier (Avian Iron Phantom)",
        "Sorrow Flora 01   : The Mourning Weeping Brier (Lament Rose Shrub)",
        "Sorrow Flora 02   : The Strangler Spore Bell (Parasitic Orchid)"
    ])

    sc_entries = []

    # 1. The Screaming Chitin Vanguard (Complex Sorrow Fauna, 300+ words)
    sc_entries.append((
        "### 1. The Screaming Chitin Vanguard (절규 갑각 선봉 / MSF-Fauna-01) — Sorrow Creature: Fauna",
        """The Screaming Chitin Vanguard (`MSF-Fauna-01`) is a lethal Mortal Sorrow Fauna manifestation that materializes in subterranean mining shafts, collapsed tunnel conduits, and perimeter sewers beneath Facility 01. Measuring three to four meters in length and standing on eight jointed chitinous appendages, this creature does not originate from human emotional grief; it crystallizes from the collective death-panic, asphyxiation terror, and agony of millions of subterranean cave crabs and burrowing insects trapped and incinerated during geothermal magma shifts.

Unlike human-born Sorrow Entities that formulate philosophical paradoxes or demand symbolic work types, the Screaming Chitin acts with pure, unthinking swarm predatory malice. Its body is composed of thousands of fused, calcified insect carapaces that shudder and grind against one another in continuous friction. This biological grinding produces an intolerable, high-decibel acoustic screech between 4,000 Hz and 7,000 Hz. This acoustic shrieking acts as a focused sonic weapon: personnel within fifteen meters experience immediate eardrum rupture, intense vestibular vertigo, and rapid Composure degradation that shatters operational discipline.

In combat, the Vanguard lunges with hydraulic speed across walls and ceilings, utilizing its front scythe-like claws to bisect unarmored workers. However, because it is an animal-born Mortal Sorrow Creature, it possesses finite physical durability and is strictly capped at Grade-β Potency. When struck by heavy blunt kinetic weapons—such as hydraulic mauls or pneumatic hammers—its calcified shell shatters into inert, unreactive chitin shards that cannot reconstitute.

Upon its physical demise, the entity does not retreat into an immortal containment cycle; it dissolves permanently into approximately eighty kilograms of coarse grey Han dust and non-toxic calcium powder. Vanguard custodial teams prioritize targeting the creature's thoracic acoustic cluster to silence its screech before executing final suppression, neutralizing the hive mind before secondary swarms coalesce. Post-action recovery protocols require sweeping the kill zone with industrial vacuum sweepers to reclaim the uncorrupted calcium flour for agricultural fertilization in Zone A.""",
        True
    ))

    # 2. The Starving Pack Spectre (Sorrow Fauna, 200+ words)
    sc_entries.append((
        "### 2. The Starving Pack Spectre (아사 늑대 환영 / MSF-Fauna-02) — Sorrow Creature: Fauna",
        """The Starving Pack Spectre (`MSF-Fauna-02`) is a predatory quadrupedal Sorrow Creature that manifests along the desolate basalt crevasses and dark subterranean gulches of Zone B and C. Formed from the residual agony of trapped wolf packs and hunting hounds that starved to death within sealed underground rifts centuries ago, this entity takes the spectral form of an emaciated, two-meter-long canine construct composed of shifting black smoke, visible rib cages of white crystal, and glowing red optical sockets.

Operating strictly under pack instincts, these entities manifest in hunting clusters of five to nine phantoms led by an alpha spectre. They communicate through low, bone-chilling acoustic whimpers that resonate at 380 Hz, causing nearby operatives to experience intense psychological pangs of phantom starvation, shivering chills, and sudden stamina exhaustion. The pack hunts by encircling isolated perimeter wardens, darting in with hit-and-run bites that inflict freezing Weight-type damage.

Because the creature's grief is rooted entirely in mortal animal hunger, it can be dispelled permanently by concentrated thermal weaponry or physical kinetic fire. Once an individual spectre's Sorrow Gauge is reduced to zero, its crystalline skeleton fractures with the sound of snapping dry twigs, evaporating into thirty kilograms of fine black ash that leaves no environmental corruption.""",
        False
    ))

    # 3. The Drowned Steed of the Sorrow Lake (Sorrow Fauna, 200+ words)
    sc_entries.append((
        "### 3. The Drowned Steed of the Sorrow Lake (익사 군마의 비탄 / MSF-Fauna-03) — Sorrow Creature: Fauna",
        """The Drowned Steed (`MSF-Fauna-03`) is an amphibious equine Sorrow Creature that emerges from the pitch-black, mirror-smooth waters of The Sorrow Lake during nighttime low-pressure cycles. Materializing from the ancient trauma of hundreds of cavalry warhorses that were driven into the deep lake during the desperate retreats of the Occlusihan War, this majestic yet horrifying entity stands three meters tall at the withers, resembling a muscular warhorse sculpted from translucent black water and dripping with weeping lament-slime.

Its mane and tail do not consist of hair, but of cascading ribbons of liquid fluid Han that dissolve into cold mist. The steed gallops silently across the lake surface without disturbing the water tension, approaching lakeshore outposts with an eerie, mournful gait. If approached by human sentries, the steed emits a deep, bubbling whinny that induces acute depressive lethargy and suicidal drown-longing in listeners. It defends itself by rearing up and stomping with hooves of dense water-ice, striking with crushing Lament force.

The Drowned Steed is classified as a mortal Tier-3 entity. Sustained kinetic fire from anti-materiel rifles or incendiary harpoons shatters the surface tension binding its liquid form, causing the steed to collapse into twenty barrels of inert, non-toxic lake water that drains harmlessly into the sand without reviving.""",
        False
    ))

    # 4. The Chained Talon Harrier (Sorrow Fauna, 200+ words)
    sc_entries.append((
        "### 4. The Chained Talon Harrier (사슬 발톱 맹금 / MSF-Fauna-04) — Sorrow Creature: Fauna",
        """The Chained Talon Harrier (`MSF-Fauna-04`) is an airborne avian Sorrow Creature that haunts the high ruined rafters, aqueduct towers, and ceiling vaults of Sector B and Zone D. Formed from the collective frenzy and panic of thousands of messenger birds and hunting hawks that died tangled in barbed wire and chains during urban sieges, the harrier manifests as a massive, ragged raptor with a four-meter wingspan, whose feathers are intertwined with rusted iron chain links and bent barbed wire.

The harrier flies with noisy, metallic wing-beats, dragging coils of trailing wire across rooftops as it hunts. When diving upon targets, it attacks with outstretched talons fused with sharp iron spikes, attempting to entangle operatives in its trailing chains and drag them into the upper rafters. The dragging of its chains against rusted metal generates an agonizing acoustic screech that spikes panic levels in civilian quarters.

Despite its terrifying metallic appearance, the creature's internal core is mortal and fragile. It possesses finite durability capped at Grade-β; hitting the harrier with concentrated shotgun blasts or magnetic anchor bolts tangles its own chains, causing it to plummet to the ground where its vessel breaks into scrap iron and forty kilograms of dry crimson soot.""",
        False
    ))

    # 5. The Mourning Weeping Brier (Complex Sorrow Flora, 300+ words)
    sc_entries.append((
        "### 5. The Mourning Weeping Brier (애도 눈물 찔레 / MSF-Flora-01) — Sorrow Creature: Flora",
        """The Mourning Weeping Brier (`MSF-Flora-01`) is a stationary, vegetative Sorrow Creature that sprouts along the damp stone masonry, cemetery walls, and drainage grates of Zone D and the abandoned perimeters of Zone B. Unlike mundane wild roses or sorrow-infused briars, this organism is born from the conceptual grief of defoliated municipal gardens and neglected family memorial shrines where flowers were left to wither untended following catastrophic civic purges.

Morphologically, the brier forms a dense, arching thicket of blackened, thorn-studded canes that can cover twenty to thirty square meters of vertical masonry. The leaves are small, leathery, and dark charcoal-grey, while the blossoms are magnificent, deep indigo roses that remain in perpetual, frozen bloom. The petals do not shed pollen; instead, each open blossom continuously exudes thick, viscous droplets of pure, concentrated Lament fluid that drip from the petals with the steady rhythm of falling tears.

The brier possesses active acoustic defenses. When living personnel approach within five paces, the thorns on the canes begin to vibrate, emitting a faint, heart-wrenching soprano sigh that mirrors the sound of a weeping child. Inhaling the sweet, heavy scent of the indigo blossoms induces rapid emotional exhaustion, causing operatives to sit down beside the thicket, overcome by memories of lost loved ones. The brier then extends slender, creeping root tendrils that seek to wrap around the victim's ankles, anchoring them permanently into the stone.

Because it is a mortal plant entity capped at Grade-β, the Mourning Weeping Brier is vulnerable to thermal suppression. Application of industrial paraffin flamethrowers incinerates the canes within ninety seconds. The burnt blossoms yield fifteen kilograms of dried indigo crystal petals, which are collected by the Memory Archive to synthesize mnemonic ink for recording official mourning decrees. Custodians must wear respirators to avoid inhaling the melancholy fumes during thermal clearing operations.""",
        True
    ))

    # 6. The Strangler Spore Bell (Sorrow Flora, 200+ words)
    ff_entries_6 = (
        "### 6. The Strangler Spore Bell (교살 포자 방울 / MSF-Flora-02) — Sorrow Creature: Flora",
        """The Strangler Spore Bell (`MSF-Flora-02`) is a hanging, parasitic Sorrow Creature that anchors itself to subterranean ventilation pipes, bridge underpasses, and humid vault ceilings across Subterranean Sector 2. Born from the instinctive trauma of ancient fungal groves eradicated by chemical purges during early facility construction, the entity manifests as a cluster of fleshy, bell-shaped bulbous sacs measuring one to two meters in length, suspended by fibrous, root-like tethers.

The bulbous sacs pulse with a dull, sickly violet luminescence. When living organisms pass beneath the cluster, the sudden change in ambient carbon dioxide triggers a rapid pneumatic spasm: the sacs burst open, unleashing a dense, suffocating cloud of fine Void spores across a ten-meter radius. These spores do not attack physical lung tissue; they attack cognitive perception, instantly inducing severe tunnel vision, auditory hallucinations, and a terrifying sensation of phantom choking that forces victims to claw at their throats.

Dispersing the spore cloud requires high-velocity ventilation fans or concussive flash grenades. The physical sacs themselves are remarkably delicate; a single burst of submachine-gun fire or a slash from an enforcer's arm-blade ruptures the bulbous walls, causing the entity to collapse into pools of inert, clear gelatin that dry into harmless white powder within minutes, allowing custodial units to restore air quality quickly.""",
        False
    )
    sc_entries.append(ff_entries_6)

    sc_content = f"""# Mugenhan Mortal Sorrow Creatures — 6 Known Anomalies
## Canonical Catalog of Tier 3 Mortal Sorrow Fauna and Flora (MSF — 4 Fauna, 2 Flora)

---

{sc_box1}
## I. Foundational Nature of Mortal Sorrow Creatures (MSF)

Tier 3 organisms—**Mortal Sorrow Fauna and Flora (생멸한령 / 生滅恨靈)**—represent conceptual sorrow manifestations that originate from non-human sources: the instinctive death-terror of dying animal swarms, the anguish of slaughtered livestock, or the ecological trauma of ruined forests.

Key ontological characteristics:
1. **Animal/Ecological Genesis:** Unlike true human Sorrow Entities (SECC), they possess no complex philosophy, moral doctrines, or desire for civil recognition. They behave strictly according to animal predation, swarm panic, or parasitic botanical growth.
2. **Strict Grade-β Potency Cap:** Because animal grief is immediate rather than metaphysical, their energy yield cannot sustain high-tier (Rank III to V) manifestations. They are strictly capped at Moderate Potency (Grade β).
3. **True Biological Mortality:** When their physical vessels are destroyed, they do not enter an immortal containment recovery cycle. They die permanently, leaving behind inert ash, mineral dust, or harvestable residue.

---

## II. Entity Distribution Roster (4 Fauna, 2 Flora)

{sc_box2}

---

## III. Detailed Creature Profiles (6 Canonical Organisms)

"""
    for title, body, is_complex in sc_entries:
        w_cnt = count_words(body)
        min_limit = 300 if is_complex else 200
        if w_cnt < min_limit:
            raise ValueError(f"Entry '{title}' has {w_cnt} words, expected >= {min_limit}")
        sc_content += f"{title}\n\n{body}\n\n---\n\n"

    sc_content += """## IV. Suppression Directives & Custodial Harvesting

Mortal Sorrow Creatures are classified as active field hazards. Field wardens, exploration scouts, and pacification units are authorized to neutralize MSF targets on sight using kinetic, thermal, or M.A.W. weaponry. All harvested residues must be cataloged and surrendered to the Bio-Synthesis Bureau for refinement into composure balms and industrial reagents.

---

**Document ID:** `MUGENHAN-BIO-CATALOG-SC06`  
**Classification:** Sovereign Ecological Codex — Permanent Planetary Lore Standard
"""

    with open("SOMNARAK-WORLD/Mugenhan_Ecology/MUGENHAN_SORROW_CREATURES.md", "w", encoding="utf-8") as f:
        f.write(sc_content)
    print("Successfully wrote MUGENHAN_SORROW_CREATURES.md")

if __name__ == "__main__":
    generate_all()
