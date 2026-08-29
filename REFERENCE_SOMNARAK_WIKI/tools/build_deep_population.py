import os
from generate_wiki_content import write_page

print("Building Deep Canonical Lore Additions...")

# 1. Minho
write_page(
    folder="characters",
    filename="minho.html",
    title="Minho — The Investigator",
    subtitle="Chief Forensic Inspector · Custodian of the Library of Stolen Pasts · Taboo Hunter",
    color="#cbd5e1",
    icon_svg="icon_dept_f6_deep_vault.svg",
    meta_cards=[
        ("Real Name", "Minho (민호)"),
        ("Title", "Chief Forensic Inspector"),
        ("Department", "Floor 6 Forensic Bureau / Sector B-02"),
        ("Specialization", "Memory Recovery &amp; Anti-Counterfeiting"),
        ("Affiliation", "Reverie Directorate Archival Division")
    ],
    article_body="""
      <h2>Overview</h2>
      <p><b>Minho</b> (민호) is the Chief Forensic Inspector of the Directorate’s Archival Division and the official custodian of the <i>Library of Stolen Pasts</i> in Sector B-02. Dedicated to investigating illegal memory-trafficking networks and black-market identity scrubbing, Minho has recovered over forty thousand illicitly harvested memory cylinders, restoring stolen identities to surviving families across Zone B.</p>
      <h2>Forensic Methodology</h2>
      <p>Minho utilizes the <b>Catharsis Spectrograph</b>, a proprietary optical sensor capable of analyzing the micro-resonance of crystallized memories to identify the original owner’s emotional signature, tracing scrubbed memories back to their origin point even after multiple washings by criminal syndicates.</p>
    """
)

# 2. Sora
write_page(
    folder="characters",
    filename="sora.html",
    title="Sora — The Lost Dreamer",
    subtitle="Grand Weaver of the Deep Currents · The Conscious Anchor Adrift in Yumonggye",
    color="#6f7ee8",
    icon_svg="icon_dept_f7_shadow_corps.svg",
    meta_cards=[
        ("Real Name", "Sora (소라)"),
        ("Title", "The Adrift Weaver"),
        ("Metaphysical State", "Deep Dream Realm Resonance Anchor"),
        ("Specialization", "Subconscious Threading &amp; Cognitive Navigation"),
        ("Affiliation", "The Weavers Guild / Deep Resonance Project")
    ],
    article_body="""
      <h2>Overview</h2>
      <p><b>Sora</b> (소라) is a legendary master weaver who entered a permanent meditative trance during the Year 4,115 Dream Breach to prevent a massive psychic tear in the fabric separating Somnarak from the Dream Realm. Her biological body rests in a stasis pod on Floor 7, while her active consciousness drifts through the deepest currents of <i>Yumonggye</i>, serving as a metaphysical lighthouse for exploratory dream-divers.</p>
    """
)

# 3. Doha
write_page(
    folder="characters",
    filename="doha.html",
    title="Doha — The Grand Mason",
    subtitle="Senior Elder of the High Architects · Builder of the Maw Basal Ring &amp; Floor 8 Bulkheads",
    color="#38bdf8",
    icon_svg="icon_dept_f4_insight_forge.svg",
    meta_cards=[
        ("Real Name", "Doha (도하)"),
        ("Guild Title", "Grand Mason Elder"),
        ("Primary Construction", "Basal Containment Iris of Floor 8"),
        ("Specialization", "Ultra-High Pressure Resonant Masonry"),
        ("Affiliation", "The High Architects / Directorate Engineering")
    ],
    article_body="""
      <h2>Overview</h2>
      <p><b>Doha</b> (도하) is the venerable master mason of the High Architects who engineered the colossal 50-meter-thick hydraulic iris that seals Floor 8 (Gate Watch) from the subterranean Maw. Utilizing compressed basalt infused with Alpha Sap glass, Doha's construction has withstood over four centuries of continuous abyssal kinetic pressure without a single structural failure.</p>
    """
)

# 4. Joon
write_page(
    folder="characters",
    filename="joon.html",
    title="Joon — The Combat Engineer",
    subtitle="Senior Barrier Specialist of Border Watch · Master of Kinetic Barrier Projection",
    color="#d7d7d7",
    icon_svg="icon_dept_f5_border_watch.svg",
    meta_cards=[
        ("Real Name", "Joon (준)"),
        ("Rank", "Senior Chief Combat Engineer"),
        ("Department", "Floor 5: Border Watch"),
        ("Specialization", "Harmonic Barrier Arrays &amp; Artillery Fortification"),
        ("Affiliation", "Border Watch / Zone E Garrison")
    ],
    article_body="""
      <h2>Overview</h2>
      <p><b>Joon</b> (준) is the premier battlefield engineer of Floor 5 Border Watch. Stationed on the Zone E Titan Wall, Joon oversees the maintenance and dynamic phase-shifting of the forty-eight harmonic barrier projectors that shield Somnarak from wasteland Han storms and feral entity bombardments.</p>
    """
)

# 5. The Doorspeech
write_page(
    folder="lore",
    filename="the-doorspeech.html",
    title="The Doorspeech (문언 — Mun-eon)",
    subtitle="The Metaphysical Dialect of the Abyssal Threshold · Acoustic Han Phonetics",
    color="#8d2e42",
    icon_svg="icon_dept_f8_gate_watch.svg",
    meta_cards=[
        ("Linguistic Class", "Metaphysical Resonant Dialect"),
        ("Source", "Acoustic Echoes of the Subterranean Maw"),
        ("First Recorded", "Year 3,893 · Post-Cheongula Breach"),
        ("Usage", "Echo-Core Designation Names &amp; Gate Locking Incantations"),
        ("Hazards", "Vocal Resonance Causes Spontaneous SP Fluctuations")
    ],
    article_body="""
      <h2>Nature of the Doorspeech</h2>
      <p><b>The Doorspeech</b> (문언, <i>Mun-eon</i>) is the eerie, non-human phonetic dialect that reverberates from the subterranean Maw and echoes through the structural bulkheads of Floor 8. Composed of low-frequency harmonic vibrations rather than traditional syntax, it is the native language through which raw Han communicates its emotional state.</p>
      <h2>The Echo-Core Inscriptions</h2>
      <p>Each of the Nine Echo-Cores possesses an unpronounceable Doorspeech fragment inscribed into their core mantle. These phonetic sequences serve as unique encryption keys that allow the Leads to synchronize with the Hand of Change facility without suffering psychic collapse.</p>
    """
)

# 6. The Dawn of Hope
write_page(
    folder="lore",
    filename="the-dawn-of-hope.html",
    title="The Dawn of Hope (희망의 여명 — Year 4,238)",
    subtitle="The Grand Reconstruction Blueprint · Decentralization of Sap and Wasteland Colonization",
    color="#f1df76",
    icon_svg="somnarak_city_icon.svg",
    meta_cards=[
        ("Initiative Title", "The Dawn Initiative (여명 계획)"),
        ("Proclamation Date", "Year 4,238 · Day 51 (Post-Cycle 1,778)"),
        ("Author", "Director Majin &amp; Joint Directorate-Council Committee"),
        ("Core Objectives", "Civic Sap Decentralization, Outskirts Reclamation, Linear Time"),
        ("Current Status", "Active Implementation Across All 5 Zones")
    ],
    article_body="""
      <h2>The Post-Cycle Era</h2>
      <p>The <b>Dawn of Hope</b> marks the official transition of Somnarak from an isolated, defensive survival state trapped in the 1,778 resets to a forward-looking, progressive civilization. Enacted on Day 51 of Year 4,238 following the stabilization of the Maw singularity, the initiative establishes a comprehensive blueprint for the next century of human expansion.</p>
      <h2>Core Strategic Pillars</h2>
      <ul>
        <li><b>Sap Decentralization:</b> Reallocating 40% of refined Alpha Sap directly to civilian power grids and agricultural biospheres in Zone B and Zone D.</li>
        <li><b>The Outskirts Reclamation:</b> Deploying SED survey fleets and Horizon Caravans to establish fortified pioneer outposts in the habitable fringes of The Desolate.</li>
        <li><b>Civic Memory Restitution:</b> Floor 6 working in conjunction with civilian tribunals to unseal historical records and restore familial lineages erased during the resets.</li>
      </ul>
    """
)

# 7. Faction Technology
write_page(
    folder="factions",
    filename="faction-technology.html",
    title="Comparative Faction Technology Matrix",
    subtitle="Engineering Paradigms · Directorate Alchemistry, Architect Masonry, Weaver Silk, and Waste Scrap",
    color="#38bdf8",
    icon_svg="icon_dept_f4_insight_forge.svg",
    meta_cards=[
        ("Technical Scope", "City-Wide Technology Comparative Assessment"),
        ("Authoring Bureau", "Floor 4 Insight Forge Engineering Bureau"),
        ("Key Paradigms", "Alpha Sap Thermodynamics, Resonant Geometry, Psychotropics"),
        ("Classification", "Universal Technical Reference")
    ],
    article_body="""
      <h2>Overview of Somnarak Technology</h2>
      <p>Technology in Somnarak is not uniform; each major institution and guild utilizes a distinct technological paradigm derived from how they interact with Han energy and Alpha Sap.</p>
      
      <table class="data-table">
        <thead>
          <tr>
            <th>Faction / Guild</th>
            <th>Primary Technological Paradigm</th>
            <th>Signature Inventions &amp; Gear</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><b>Reverie Directorate</b></td>
            <td>Alpha Sap Thermodynamics &amp; M.A.W. Extraction</td>
            <td>M.A.W. Weapons &amp; Suits, Catharsis Siphons, Containment Lattices</td>
          </tr>
          <tr>
            <td><b>High Architects</b></td>
            <td>Resonant Geometry &amp; Spatial Anchoring</td>
            <td>Resonant Granite, Hydraulic Blast Bulkheads, Spire Ventilation Arrays</td>
          </tr>
          <tr>
            <td><b>The Weavers</b></td>
            <td>Psychotropic Silk Spinning &amp; Cognitive Lining</td>
            <td>Catharsis Looms, Memory Filaments, Mental Insulation Shrouds</td>
          </tr>
          <tr>
            <td><b>The Wardens</b></td>
            <td>Kinetic Shock &amp; Crowd Riot Suppression</td>
            <td>Lament Shock-Mauls, Kinetic Barrier Shields, Tactical Suppression Armor</td>
          </tr>
          <tr>
            <td><b>The Horizon Caravan</b></td>
            <td>All-Terrain Heavy Engineering &amp; Waste Scrap</td>
            <td>Titan Land-Crawlers, Han Filtration Mask Rigs, Precursor Power Plants</td>
          </tr>
        </tbody>
      </table>
    """
)

# 8. Han Relics & Tools
write_page(
    folder="mechanics",
    filename="han-relics-and-tools.html",
    title="Han Relics &amp; Tool Entities System",
    subtitle="Equippable Relics · Use Intervals, Ego Intrusion Mechanics, and Extraction Rules",
    color="#e6c94d",
    icon_svg="icon_dept_f3_extraction.svg",
    meta_cards=[
        ("Entity Category", "Tool-Type Sorrow Entities (I-Relic / Indumentum)"),
        ("Operating Types", "Equippable, Sustained-Use, Single-Discharge, Place-Anchored"),
        ("Key Metric", "Time Interval vs SP Intrusion Threshold"),
        ("Representative Entity", "SE-001 The Orphaned Bell (I-Relic)"),
        ("Operational Handlers", "Floor 3 Extraction Staff &amp; Field Specialists")
    ],
    article_body="""
      <h2>The Nature of Tool Entities</h2>
      <p>Unlike autonomous, sentient Sorrow Entities that wander containment chambers, <b>Tool-Type Sorrow Entities (I-Relics)</b> manifest as physical objects, wearable garments, musical instruments, or stationary monuments that can be actively operated by staff to produce powerful buffs or tactical effects.</p>
      <h2>The Double-Edged Burden: Ego Intrusion</h2>
      <p>Operating a Tool SE grants immediate supernatural advantages (e.g. floor-wide healing, damage nullification, or accelerated work speed). However, continuous operation drains the operator's SP according to strict time intervals. Exceeding the safe operational threshold triggers <i>Ego Intrusion</i>, causing irreversible panic or permanent physical assimilation into the tool.</p>
    """
)

# 9. Unknown Cities
write_page(
    folder="locations",
    filename="unknown-cities.html",
    title="The Lost Frontier Cities (미지의 폐허 도시군)",
    subtitle="Precursor Settlements of the Desolate · Cheonbulok, Old Cheongula, Haerim, and Namsan",
    color="#e8a317",
    icon_svg="somnarak_city_icon.svg",
    meta_cards=[
        ("Geographical Region", "The Desolate (100km–400km Radius from Bulwark)"),
        ("Documented Ruins", "Citadel of Cheonbulok, Old Cheongula, Port Haerim, Spire Namsan"),
        ("Survey Authority", "Sorrow Exploration Division (SED) &amp; Horizon Caravans"),
        ("Status", "Sunk in Ashen Strata / Infested with Feral Calamities")
    ],
    article_body="""
      <h2>The Ghost Metropolises of the Ash Plains</h2>
      <p>Somnarak is not the first city built by humanity in the post-cataclysm era; it is simply the only one that survived. Across the vast ash wastes of The Desolate lie the sunken, petrified remains of sister citadels that fell to the subterranean Maw or perished during the early resource wars.</p>

      <h2>Major Documented Ruin Sites</h2>
      <ul>
        <li><b>Sunken Citadel of Cheonbulok (천불록 유적):</b> Located 140km west; ancient industrial citadel encased in calcified weeping crystal. Ancestral homeland of the Zone B refugees.</li>
        <li><b>Old Cheongula Reactor Basin (구 청구라 분지):</b> Located 60km south; the radioactive, Han-flooded crater of the Year 3,892 disaster where SE-010 first awakened.</li>
        <li><b>Port Haerim (해림 폐항):</b> Located 280km east; an ancient dry sea harbor where precursor naval vessels lie buried beneath blue sorrow salt.</li>
        <li><b>Spire Namsan (남산 첨탑군):</b> Located 350km north; three shattered communications towers that still transmit faint radio pulses into the upper atmosphere.</li>
      </ul>
    """
)

print("Deep canonical additions built successfully.")
