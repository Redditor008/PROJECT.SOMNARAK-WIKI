import os
from generate_wiki_content import write_page

print("Building Lore Section...")

# 1. Somnarak Cosmology
write_page(
    folder="lore",
    filename="somnarak-cosmology.html",
    title="Somnarak Cosmology &amp; World Structure",
    subtitle="The Metaphysical Architecture of Reality · The Five Layers, The Dream Realm, and The Abyssal Maw",
    color="#38bdf8",
    icon_svg="somnarak_city_icon.svg",
    meta_cards=[
        ("Cosmic Classification", "Post-Cataclysm Closed Metaphysical System"),
        ("Primary Energy Substrate", "Han (한 / 恨) Emotional Thermodynamic Flow"),
        ("Core Metaphysical Pillar", "The Alpha Tree (Station A)"),
        ("Abyssal Substrate", "The Weeping (흐느낌의 강) / The Subterranean Maw"),
        ("Active Epoch", "Year 4,238 · Post-Absolvohan Dawn Era")
    ],
    article_body="""
      <h2>Metaphysical Architecture of the World</h2>
      <p>The cosmos of <b>Somnarak</b> operates on a unique metaphysical and thermodynamic foundation where unexpressed human emotion—specifically grief, sorrow, unresolved regret, and existential longing, collectively known as <b>Han (한)</b>—functions as both a physical element and a cosmic substrate. Unlike traditional material realities, physical space within Somnarak and the surrounding wastelands is shaped, distorted, and stabilized directly by the density and emotional purity of this psychic flow.</p>

      <h2>The Five Structural Layers of Existence</h2>
      <p>According to the metaphysical doctrines established by Lead Ayshuk and preserved in Floor 4 (Insight Forge), existence in Somnarak is divided into five vertical and conceptual layers:</p>
      
      <table class="data-table">
        <thead>
          <tr>
            <th>Layer Designation</th>
            <th>Metaphysical Realm</th>
            <th>Primary Characteristics &amp; Inhabitants</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><b>Layer 1: The High Canopy</b></td>
            <td>Upper Alpha Sphere</td>
            <td>The radiant crown of the Alpha Tree, filtering atmospheric miasma and generating the golden light that illuminates Zones A through C.</td>
          </tr>
          <tr>
            <td><b>Layer 2: The Urban Spires</b></td>
            <td>Material Somnarak</td>
            <td>The five inhabited civic zones (A through E), housing humanity within resonant granite spires and protective barrier wards.</td>
          </tr>
          <tr>
            <td><b>Layer 3: The Hand of Change</b></td>
            <td>Subterranean Facility</td>
            <td>The eight-floor administrative and containment complex spanning kilometers downward into the earth beneath the Alpha Tree roots.</td>
          </tr>
          <tr>
            <td><b>Layer 4: The River Weeping</b></td>
            <td>Subconscious Hydrology</td>
            <td>The subterranean fluid basin (흐느낌의 강) where un-harvested sorrow condenses into heavy psychic water, giving birth to Sorrow Entities.</td>
          </tr>
          <tr>
            <td><b>Layer 5: The Abyssal Maw</b></td>
            <td>The Deep Void / Maw</td>
            <td>The bottomless metaphysical rift at the center of the world. The absolute source of primordial Han and the genesis point of Calamity-class horrors.</td>
          </tr>
        </tbody>
      </table>

      <h2>The Dream Realm (유몽계 — Yumonggye)</h2>
      <p>Parallel to physical space lies the <b>Dream Realm</b>, an ethereal dimension composed entirely of subconscious cognitive currents. During sleep or severe psychological fracture, human consciousness drifts into the shallow fringes of this ocean. High-tier Weavers and Echo-Cores can project their will into the Dream Realm to repair fractured minds or anchor unstable containment barriers.</p>

      <h2>Han Thermodynamics &amp; Metabolic Law</h2>
      <p>Energy cannot be created from nothing; in Somnarak, civic energy is extracted directly from human emotion. Sorrow is harvested, condensed into crystallized Alpha Sap, refined in Floor 3, and metabolized across the city grid. If the emotional balance tilts too far into despair, entities spontaneously manifest; if suppressed entirely, the population suffers cognitive petrification.</p>
    """
)

# 2. The Three Sorrows
write_page(
    folder="lore",
    filename="the-three-sorrows.html",
    title="The Three Sorrows (삼비 — 3-Sorrow Matrix)",
    subtitle="The Fundamental Emotional Spectrum of Han · Lament, Grudge, and Weight",
    color="#ef5b55",
    icon_svg="icon_dept_f4_insight_forge.svg",
    meta_cards=[
        ("System Type", "Tri-Partite Emotional Physics Matrix"),
        ("Primary Aspects", "Lament (비탄), Grudge (원망), Weight (비중)"),
        ("Derived Complex", "Fracture (Purple) &amp; Absolute Void (Pale)"),
        ("Formulated By", "Echo-Core 5 (Ayshuk) · Insight Forge Y3,920"),
        ("Practical Application", "M.A.W. Resonance &amp; Work Efficiency Tuning")
    ],
    article_body="""
      <h2>The Tri-Partite Matrix Overview</h2>
      <p>All psychic resonance, entity manifestations, and M.A.W. weaponry within Somnarak derive from the <b>Three Sorrows (삼비, <i>Sambee</i>)</b>. Formulated by Echo-Core 5 Ayshuk following decades of empirical containment research, this tri-partite classification provides the scientific framework for understanding and manipulating Han energy.</p>

      <h2>The Three Fundamental Emotional Spectra</h2>

      <h3>1. Lament (비탄 — <i>Bitan</i>) · Blue Spectrum</h3>
      <p>Lament represents passive, introspective grief—the sorrow of loss, mourning for what once was, and the quiet acceptance of tragedy. It is characterized by low thermal output, high mental resonance, and cold crystallization.</p>
      <ul>
        <li><b>Manifestation:</b> Crystalline tears, frost-like sap formations, acoustic resonance chimes.</li>
        <li><b>Tactical Damage:</b> Blue (Mental / SP Damage). Targets the cognitive stability and sanity of operatives.</li>
        <li><b>Representative Entity:</b> SE-001 (The Orphaned Bell).</li>
      </ul>

      <h3>2. Grudge (원망 — <i>Wonmang</i>) · Red Spectrum</h3>
      <p>Grudge represents active, outward-projecting fury—the burning anger against injustice, betrayal, and unavenged suffering. It exhibits high thermodynamic volatility and extreme kinetic acceleration.</p>
      <ul>
        <li><b>Manifestation:</b> Searing crimson flames, jagged razor-spikes, boiling Alpha Sap.</li>
        <li><b>Tactical Damage:</b> Red (Physical / HP Damage). Slashes flesh, fractures armor, and causes structural degradation.</li>
        <li><b>Representative Entity:</b> SE-007 (Brume / Burning Fog).</li>
      </ul>

      <h3>3. Weight (비중 — <i>Bijung</i>) · Black Spectrum</h3>
      <p>Weight represents oppressive, crushing despair—the inescapable burden of debt, guilt, duty, and mortality. It exhibits immense gravitational distortion and spatial compression.</p>
      <ul>
        <li><b>Manifestation:</b> Heavy iron chains, crushing black miasma, gravitational sinkholes.</li>
        <li><b>Tactical Damage:</b> Black (Hybrid HP + SP Damage). Crushes physical bodies while simultaneously draining mental will.</li>
        <li><b>Representative Entity:</b> SE-002 (The Grieving Colossus) and SE-015 (The Debt Scale).</li>
      </ul>

      <h2>The Composite Spectra: Fracture &amp; Pale</h2>
      <p>When multiple sorrows collide without reaching equilibrium, two composite phenomena emerge:</p>
      <ul>
        <li><b>Fracture (균열 — Purple Spectrum):</b> The chaotic collision of Grudge and Lament. Inflicts erratic fluctuating damage and bypasses standard mental shields.</li>
        <li><b>Pale / Absolute Verdict (창백 — White/Pale Spectrum):</b> The complete extinction of emotion into absolute zero. Deals percentage-based maximum HP damage, dissolving biological and synthetic matter directly into primordial dust (e.g., SE-010 The Convergence).</li>
      </ul>
    """
)

# 3. The Cycle & Absolvohan
write_page(
    folder="lore",
    filename="the-cycle-and-absolvohan.html",
    title="The Cycle &amp; The Absolvohan Ritual",
    subtitle="The 1,778 Temporal Iterations · The Nine Parts of Absolvohan · The Dawn of Year 4,238",
    color="#e6c94d",
    icon_svg="the_hand_dr_icon_styled.svg",
    meta_cards=[
        ("Ritual Designation", "Absolvohan (앱솔보한 — Complete Absolution)"),
        ("Temporal Duration", "1,778 Iterations (Approx. 440 Continuous Years)"),
        ("Ritual Architect", "Director Majin (Echo-Core 1)"),
        ("Temporal Anchor", "Deep Vault (Floor 6) &amp; Alpha Tree Core"),
        ("Resolution Status", "Completed Day 50 · Dawn Initiative Enacted")
    ],
    article_body="""
      <h2>The Grand Metaphysical Loop</h2>
      <p>The <b>Absolvohan Cycle</b> was a vast, multi-century temporal and cognitive loop engineered by Director Majin to prevent the total annihilation of Somnarak. Following the catastrophic containment failures of the Early Era, Majin realized that humanity lacked the technological and psychic maturity to withstand the subterranean Maw in a linear timeline.</p>
      <p>By binding the root core of the Alpha Tree to the temporal dampeners of Floor 6 (Deep Vault), Majin established a 50-day iterative reset cycle. Each cycle allowed the Directorate to harvest Han, refine M.A.W. prototypes, train operatives, and decipher entity psychology. At the conclusion of Day 50, or upon catastrophic facility breach, the timeline reset, wiping civilian and operational memories while Majin preserved the cumulative data.</p>

      <h2>The Nine Canonical Parts of Absolvohan</h2>
      <table class="data-table">
        <thead>
          <tr>
            <th>Part</th>
            <th>Title</th>
            <th>Core Metaphysical Phase</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><b>Part 1</b></td>
            <td>The Waking Ledger</td>
            <td>Director Majin awakens on Day 0; Seiyon delivers the opening telemetry report of all eight floors.</td>
          </tr>
          <tr>
            <td><b>Part 2</b></td>
            <td>The Siphon of Tears</td>
            <td>Floor 3 Extraction Hall initiates baseline Alpha Sap extraction from Low-Risk Sorrow Entities.</td>
          </tr>
          <tr>
            <td><b>Part 3</b></td>
            <td>The Iron Vigil</td>
            <td>Floor 2 under Dekan subdues the first cascade breaches of Class III and IV entities.</td>
          </tr>
          <tr>
            <td><b>Part 4</b></td>
            <td>The Insight Thesis</td>
            <td>Floor 4 Ayshuk formulates emotional frequency formulas to stabilize volatile containment cells.</td>
          </tr>
          <tr>
            <td><b>Part 5</b></td>
            <td>The Perimeter Wall</td>
            <td>Floor 5 Mellda engages outer wasteland incursions along the Zone E Bulwark.</td>
          </tr>
          <tr>
            <td><b>Part 6</b></td>
            <td>The Deep Cry</td>
            <td>Floor 6 Marjuk archives fallen personnel records into cryo-memory cylinders.</td>
          </tr>
          <tr>
            <td><b>Part 7</b></td>
            <td>The Shadow Ingress</td>
            <td>Floor 7 Ishall recovers rogue M.A.W. prototypes from the Underworld syndicates.</td>
          </tr>
          <tr>
            <td><b>Part 8</b></td>
            <td>The Day 50 Standoff</td>
            <td>Floor 8 Xyan stands before the Abyssal Maw as the final entity, SE-010 The Convergence, tests the city's resolve.</td>
          </tr>
          <tr>
            <td><b>Part 9</b></td>
            <td>The Dawn Unbroken</td>
            <td>Iteration 1,778 reaches perfect resonance harmony; the loop breaks, and permanent linear time resumes.</td>
          </tr>
        </tbody>
      </table>

      <h2>The Epilogue: Year 4,238</h2>
      <p>On the final day of Iteration 1,778, the combined harmony of all nine Echo-Cores successfully neutralized the singularity of The Convergence without triggering a reset. Majin officially declared the end of the Absolvohan Cycle, initiating the <b>Dawn Initiative</b> to rebuild human civilization in linear time.</p>
    """
)

# 4. The Alpha Tree
write_page(
    folder="lore",
    filename="the-alpha-tree.html",
    title="The Alpha Tree (알파 트리 — Station A)",
    subtitle="The Living Core of Somnarak · Botany, Sap Refinement, and Metabolic Life Support",
    color="#47c978",
    icon_svg="icon_dept_f4_insight_forge.svg",
    meta_cards=[
        ("Botanical Class", "Gigantic Resonant Psycho-Arbor (Ω-Grade)"),
        ("Height &amp; Span", "Canopy: 850m Height · Taproot Depth: 3,200m"),
        ("Primary Product", "Alpha Sap (황금 수액 — Liquid Han Distillate)"),
        ("Location", "Zone A · Hand of Change Central Axis"),
        ("Civic Function", "Atmospheric Purification &amp; Power Generation")
    ],
    article_body="""
      <h2>Anatomy &amp; Botanical Structure</h2>
      <p>The <b>Alpha Tree</b> (알파 트리) is the colossal, bioluminescent arboreal entity that anchors the entire physical and metaphysical structure of Somnarak. Rising 850 meters above Zone A and driving taproots kilometers deep into the subterranean strata, the Tree serves as the city's primary power generator, atmospheric oxygenator, and emotional filter.</p>

      <h2>The Four Botanical Tiers</h2>
      <ul>
        <li><b>The Golden Canopy:</b> The vast, glowing upper branches that span the sky above Zone A and Zone D, emitting a gentle 580nm golden light that substitutes for the sun in post-cataclysm skies.</li>
        <li><b>The Trunk &amp; Heartwood:</b> Massive granite-like bark infused with crystalline conduits that channel refined Han from the lower extraction chambers to the city grid.</li>
        <li><b>The Core Chamber (Station A):</b> Located directly on Floor 1, where Director Majin and Seiyon monitor the Tree’s pulse and manage metabolic flow.</li>
        <li><b>The Taproot Mycelium:</b> Deep subterranean roots that extend into the River Weeping, actively drawing raw sorrow from the Maw and transmuting it into usable life energy.</li>
      </ul>

      <h2>Alpha Sap Refinement &amp; Utilization</h2>
      <p>The sap of the Alpha Tree (황금 수액) is a dense, golden, highly conductive liquid that acts as the universal lifeblood of Somnarak:</p>
      <ul>
        <li><b>Civic Power:</b> Powers the streetlights, transit trams, and heating grids of all five urban zones.</li>
        <li><b>Food Synthesis:</b> Processed in Zone D Arboretums into nutrient-dense synthetic sustenance for the civilian population.</li>
        <li><b>M.A.W. Binding Agent:</b> Used by Floor 3 to stabilize emotional resonance during weapon forging.</li>
      </ul>
    """
)

# 5. The Cheongula Incident
write_page(
    folder="lore",
    filename="the-cheongula-incident.html",
    title="The Cheongula Incident (청구라 참사)",
    subtitle="The Cataclysm of Year 3,892 · The Fall of the First Citadel &amp; Directorate Founding",
    color="#8d2e42",
    icon_svg="somnarak_city_icon.svg",
    meta_cards=[
        ("Date of Disaster", "Year 3,892 · Month 4, Day 12"),
        ("Casualty Count", "Estimated 142,000 Casualties (84% of Population)"),
        ("Origin Point", "Old Cheongula Sub-Level Reactor"),
        ("Entity Responsible", "Rupture of Subterranean Maw / SE-010 Manifestation"),
        ("Historical Consequence", "Founding of the Reverie Directorate &amp; Hand of Change")
    ],
    article_body="""
      <h2>Historical Background</h2>
      <p>The <b>Cheongula Incident</b> (청구라 참사) is the foundational tragedy of modern Somnarak history. In Year 3,892, the precursor industrial metropolis of Cheongula suffered an unprecedented catastrophic rupture in its deep geothermal extraction wells, piercing the metaphysical boundary of the subterranean Maw.</p>

      <h2>Chronology of the Rupture</h2>
      <table class="data-table">
        <thead>
          <tr>
            <th>Time</th>
            <th>Incident Log &amp; Tactical Event</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><b>04:12 AM</b></td>
            <td>Deep Reactor 7 reports extreme negative pressure and acoustic reverberations resembling human screaming.</td>
          </tr>
          <tr>
            <td><b>05:40 AM</b></td>
            <td>Subterranean Maw breaches containment. Raw, unrefined Han floods the lower residential districts, causing spontaneous mass mental fracture.</td>
          </tr>
          <tr>
            <td><b>08:15 AM</b></td>
            <td>SE-010 (The Convergence) manifests at the center of the civic plaza, dissolving 40,000 residents into a single weeping cognitive singularity.</td>
          </tr>
          <tr>
            <td><b>01:00 PM</b></td>
            <td>Majin, then Chief Engineer, activates the experimental Alpha Sap dampeners, sealing the lower gates and preserving the surviving northern sector.</td>
          </tr>
        </tbody>
      </table>

      <h2>The Rebuilding &amp; Directorate Mandate</h2>
      <p>From the ashes of Cheongula, Majin and the surviving engineers founded the <b>Reverie Directorate</b>. The city was reorganized into five defensive concentric zones, and construction began on the Hand of Change to ensure that humanity would never again be defenseless against the subterranean abyss.</p>
    """
)

# 6. The Dream Realm
write_page(
    folder="lore",
    filename="the-dream-realm.html",
    title="The Dream Realm (유몽계 — Yumonggye)",
    subtitle="The Ocean of Subconscious Memory · Dream Diving and Cognitive Topography",
    color="#6f7ee8",
    icon_svg="icon_dept_f7_shadow_corps.svg",
    meta_cards=[
        ("Dimension Class", "Metaphysical Cognitive Substrate"),
        ("Exploration Method", "Psychotropic Weave Diving / Floor 4 Neural Pods"),
        ("Primary Hazards", "Ego Dissolution, Adrift Sleepers, Nightmare Singularities"),
        ("Key Specialists", "The Weavers Guild &amp; Shadow Corps"),
        ("Direct Access Point", "Floor 7 Sub-Level Chambers")
    ],
    article_body="""
      <h2>Nature of the Dream Realm</h2>
      <p>The <b>Dream Realm</b> (유몽계, <i>Yumonggye</i>) is the boundless metaphysical ocean of human subconsciousness that flows beneath the physical world of Somnarak. Every unexpressed sorrow, repressed dream, and lost memory enters this ocean, forming fluid currents of living cognitive energy.</p>

      <h2>Dream Diving (몽수 — Mongsoo)</h2>
      <p>Specialized operatives from the Weavers Guild and Floor 7 Shadow Corps perform "Dream Dives" by submerging into psychotropic Alpha Sap vats. While tethered by silver memory lines, divers navigate the psychological landscape to:</p>
      <ul>
        <li>Recover fractured memories of high-value personnel.</li>
        <li>Track the pre-manifestation gestation of dangerous Sorrow Entities.</li>
        <li>Establish telepathic communication links across long distances.</li>
      </ul>
    """
)

# 7. The Weeping River
write_page(
    folder="lore",
    filename="the-weeping-river.html",
    title="The River Weeping (흐느낌의 강)",
    subtitle="The Subterranean Abyssal Hydrology · Fluid Han Mechanics and Origin of Entities",
    color="#38bdf8",
    icon_svg="icon_dept_f2_maws_keep.svg",
    meta_cards=[
        ("Hydrological Class", "Subterranean Liquid Han Stream"),
        ("Depth &amp; Flow", "Sub-Level 8 to Abyssal Maw (Fluid Velocity: 14 m/s)"),
        ("Thermal Gradient", "-12°C to +4°C (Cryo-Resonant)"),
        ("Chemical Composition", "92% Condensed Grief / 8% Dissolved Alpha Sap"),
        ("Security Level", "Strict Directorate Quarantine")
    ],
    article_body="""
      <h2>Hydrological Profile</h2>
      <p>The <b>River Weeping</b> (흐느낌의 강) is the dark, luminescent subterranean river that flows through the deepest caverns beneath the Hand of Change before plunging into the Abyssal Maw. Formed from the condensation of millions of historical tears and unexpressed grief, its waters shimmer with a pale cyan phosphorescence.</p>

      <h2>Phenomena &amp; Entity Birth</h2>
      <p>When emotional resonance in the city reaches critical mass, eddies within the River Weeping undergo spontaneous phase transition, crystallizing into the core seeds that spawn Sorrow Entities. Floor 8 Gate Watch maintains continuous acoustic sensors along its banks to detect impending births.</p>
    """
)

# 8. The Seven Absolute Taboos
write_page(
    folder="lore",
    filename="the-seven-absolute-taboos.html",
    title="The Seven Absolute Taboos (7대 절대 금기)",
    subtitle="The Supreme Metaphysical and Civic Prohibitions of Somnarak",
    color="#ef5b55",
    icon_svg="icon_dept_f6_deep_vault.svg",
    meta_cards=[
        ("Legal Authority", "The High Council &amp; Reverie Directorate Charter"),
        ("Enforcement Agency", "Floor 7 Shadow Corps &amp; UCD Tactical Strike Force"),
        ("Penalty for Violation", "Immediate Memory Scrubbing / Permanent Exile to Floor 8"),
        ("Enacted Era", "Year 3,910 (Post-Cheongula Charter)"),
        ("Current Status", "Active and Inviolable")
    ],
    article_body="""
      <h2>The Inviolable Prohibitions</h2>
      <p>To prevent the recurrence of the Cheongula cataclysm, the Directorate and High Council established the <b>Seven Absolute Taboos</b>. These laws govern the safe handling of Han, human consciousness, and M.A.W. resonance.</p>

      <table class="data-table">
        <thead>
          <tr>
            <th>Taboo #</th>
            <th>Prohibition Title</th>
            <th>Legal &amp; Metaphysical Rationale</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><b>Taboo 1</b></td>
            <td><b>Memory Counterfeiting</b></td>
            <td>Fabricating or falsifying human memories using synthetic Alpha Sap disrupts psychological resonance, risking mass cognitive fracture.</td>
          </tr>
          <tr>
            <td><b>Taboo 2</b></td>
            <td><b>Unlicensed Han Extraction</b></td>
            <td>Harvesting grief from living citizens outside Directorate-certified facilities causes irreversible soul calcification.</td>
          </tr>
          <tr>
            <td><b>Taboo 3</b></td>
            <td><b>Abyssal Gate Piercing</b></td>
            <td>Attempting to drill, dig, or teleport beneath Floor 8 into the deep Maw risks triggering a cataclysmic flood of primordial sorrow.</td>
          </tr>
          <tr>
            <td><b>Taboo 4</b></td>
            <td><b>Human-Entity Fusion</b></td>
            <td>Permanently fusing human biological tissue with a live Sorrow Entity without Ω-grade authorization results in uncontrollable abominations.</td>
          </tr>
          <tr>
            <td><b>Taboo 5</b></td>
            <td><b>Hoarding Precursor Relics</b></td>
            <td>Concealing Grade IV or higher Han relics prevents city-wide defense calibration and invites sudden entity incursions.</td>
          </tr>
          <tr>
            <td><b>Taboo 6</b></td>
            <td><b>Desolate Exile Returning</b></td>
            <td>Entering the city from The Desolate without undergoing quarantine and neural scanning is strictly prohibited to stop waste miasma infection.</td>
          </tr>
          <tr>
            <td><b>Taboo 7</b></td>
            <td><b>Cycle Record Disclosure</b></td>
            <td>Disclosing the true history of the 1,778 resets to un-anchored civilians causes fatal existential despair and panic collapses.</td>
          </tr>
        </tbody>
      </table>
    """
)

# 9. Daily Life in Somnarak
write_page(
    folder="lore",
    filename="daily-life-in-somnarak.html",
    title="Daily Life &amp; Culture in Somnarak",
    subtitle="Civic Society, The Echo-Token Economy, Spire Architecture, and Cultural Rituals",
    color="#f1df76",
    icon_svg="somnarak_city_icon.svg",
    meta_cards=[
        ("Civilian Population", "Approx. 480,000 Inhabitants across 5 Zones"),
        ("Primary Currency", "Echo-Tokens (에코 토큰 — Sap-Backed Credit)"),
        ("Primary Sustenance", "Alpha-Synthesized Rations &amp; Hydroponic Produce"),
        ("Dominant Language", "Somnarak Standard (Korean-derived Common Tongue)"),
        ("Social Structure", "Directorate Citizens, Guild Artisans, Enclave Refugees")
    ],
    article_body="""
      <h2>Urban Life Beneath the Alpha Canopy</h2>
      <p>Life within the five concentric zones of Somnarak is defined by resilience, communal solidarity, and deep respect for the emotional currents that sustain the city. Despite the ever-present threat of the Maw and the surrounding Desolate, civil society flourishes with rich cultural traditions, bustling bazaars, and innovative technologies.</p>

      <h2>Economy &amp; Echo-Tokens</h2>
      <p>The city's financial system is pegged directly to refined Alpha Sap. <b>Echo-Tokens</b> represent fractional shares of energy kilowatt-hours and emotional stabilization rations. Citizens earn tokens through industrial labor, craft guilds, facility maintenance, and civil defense services.</p>

      <h2>Cultural Rituals &amp; Funeral Traditions</h2>
      <p>In a city powered by sorrow, death and remembrance hold sacred significance. The <b>Evening Return (귀환제)</b> is a daily twilight ceremony where families light amber lanterns along their balconies to honor lost ancestors, guiding wandering emotional echoes back to the roots of the Alpha Tree.</p>
    """
)

# 10. Lore Hub (index.html)
write_page(
    folder="lore",
    filename="index.html",
    title="Lore &amp; World Encyclopedia Hub",
    subtitle="Comprehensive Compendium of Somnarak Cosmology, History, Metaphysics, and Culture",
    color="#38bdf8",
    icon_svg="somnarak_city_icon.svg",
    meta_cards=[
        ("Indexed Lore Articles", "9 Major Canonical Compendiums"),
        ("Cosmic Timeline", "Year 3,892 to Year 4,238 (Dawn Era)"),
        ("Primary Focus", "Cosmology, Metaphysics, History, and Society"),
        ("Classification", "Universal Knowledge Base")
    ],
    article_body="""
      <h2>Lore &amp; Metaphysical Compendiums</h2>
      <p>Explore the history, cosmology, emotional physics, and societal structures that define the world of Somnarak.</p>

      <div class="entity-gallery">
        <a class="entity-card" href="somnarak-cosmology.html" style="--card-border:#38bdf8">
          <img src="../assets/icons/somnarak_city_icon.svg" alt="">
          <h3>Cosmology</h3>
          <p>The Five Layers of Reality, Dream Realm &amp; Maw</p>
        </a>
        <a class="entity-card" href="the-three-sorrows.html" style="--card-border:#ef5b55">
          <img src="../assets/icons/icon_dept_f4_insight_forge.svg" alt="">
          <h3>The Three Sorrows</h3>
          <p>Lament, Grudge, Weight &amp; The Han Spectrum</p>
        </a>
        <a class="entity-card" href="the-cycle-and-absolvohan.html" style="--card-border:#e6c94d">
          <img src="../assets/icons/the_hand_dr_icon_styled.svg" alt="">
          <h3>The Absolvohan Cycle</h3>
          <p>The 1,778 Resets, Ritual Parts 1-9 &amp; Dawn</p>
        </a>
        <a class="entity-card" href="the-alpha-tree.html" style="--card-border:#47c978">
          <img src="../assets/icons/icon_dept_f4_insight_forge.svg" alt="">
          <h3>The Alpha Tree</h3>
          <p>Canopy, Core Chamber &amp; Alpha Sap Refining</p>
        </a>
        <a class="entity-card" href="the-cheongula-incident.html" style="--card-border:#8d2e42">
          <img src="../assets/icons/somnarak_city_icon.svg" alt="">
          <h3>The Cheongula Incident</h3>
          <p>Year 3,892 Cataclysm &amp; Directorate Founding</p>
        </a>
        <a class="entity-card" href="the-dream-realm.html" style="--card-border:#6f7ee8">
          <img src="../assets/icons/icon_dept_f7_shadow_corps.svg" alt="">
          <h3>The Dream Realm</h3>
          <p>Subconscious Navigation &amp; Dream Diving</p>
        </a>
        <a class="entity-card" href="the-weeping-river.html" style="--card-border:#38bdf8">
          <img src="../assets/icons/icon_dept_f2_maws_keep.svg" alt="">
          <h3>The River Weeping</h3>
          <p>Abyssal Hydrology &amp; Entity Genesis</p>
        </a>
        <a class="entity-card" href="the-seven-absolute-taboos.html" style="--card-border:#ef5b55">
          <img src="../assets/icons/icon_dept_f6_deep_vault.svg" alt="">
          <h3>Seven Absolute Taboos</h3>
          <p>Inviolable Laws of Han &amp; Consciousness</p>
        </a>
        <a class="entity-card" href="daily-life-in-somnarak.html" style="--card-border:#f1df76">
          <img src="../assets/icons/somnarak_city_icon.svg" alt="">
          <h3>Daily Life &amp; Society</h3>
          <p>Economy, Spire Architecture &amp; Culture</p>
        </a>
      </div>
    """
)

print("Lore section built successfully.")
