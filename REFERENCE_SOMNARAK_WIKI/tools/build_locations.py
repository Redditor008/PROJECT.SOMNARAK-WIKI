import os
from generate_wiki_content import write_page

print("Building Locations Section...")

# 1. Zone A
write_page(
    folder="locations",
    filename="zone-a-core-nexus.html",
    title="Zone A — Core Nexus (중심 제1구역)",
    subtitle="The Heart of Somnarak · Directorate Spire, Station A, and The High Council Rotunda",
    color="#ef5b55",
    icon_svg="icon_dept_f1_neutral.svg",
    meta_cards=[
        ("District Designation", "Zone A · Administrative &amp; Energy Nexus"),
        ("Dominant Structure", "The Alpha Tree &amp; The Directorate Spire (1,100m)"),
        ("Key Institutions", "Floor 1 Neutral Command, High Council Chambers"),
        ("Resident Demographic", "Senior Directorate Staff, High Council Elders, Elite Guards"),
        ("Security Level", "Grade 5 (Supreme Directorate Shielding)")
    ],
    article_body="""
      <h2>District Overview</h2>
      <p><b>Zone A (Core Nexus)</b> is the radiant epicenter of Somnarak. Encompassing the massive trunk base of the Alpha Tree and the towering Directorate Spire, Zone A serves as the supreme seat of government, metabolic energy distribution, and strategic defense planning for the entire metropolis.</p>
      <h2>Key Landmarks</h2>
      <ul>
        <li><b>The Directorate Spire:</b> Monolithic 1,100-meter tower of polished resonant granite housing the executive bureaus.</li>
        <li><b>The Alpha Basin:</b> The glowing reservoir at the tree’s base where purified Alpha Sap is directed into underground aqueducts.</li>
        <li><b>The High Rotunda:</b> Golden-domed legislative chamber where the High Council of Elders convenes.</li>
      </ul>
    """
)

# 2. Zone B
write_page(
    folder="locations",
    filename="zone-b-west-ward.html",
    title="Zone B — West Ward (서부 주거구역)",
    subtitle="The Great Residential Spires · Orphan Bell Tower, Silk Lofts, and Refugee Quarters",
    color="#38bdf8",
    icon_svg="somnarak_city_icon.svg",
    meta_cards=[
        ("District Designation", "Zone B · High-Density Residential &amp; Cultural Ward"),
        ("Population", "Approx. 240,000 Residents (50% of Total Population)"),
        ("Key Landmarks", "The Orphan Bell Tower, The Silk Lofts, Cheonbulok Enclave"),
        ("Primary Industry", "Weaving Guild Workshops, Civic Academies, Retail"),
        ("Security Level", "Grade 2 (Warden Regular Patrols)")
    ],
    article_body="""
      <h2>The Living Spires of Somnarak</h2>
      <p><b>Zone B (West Ward)</b> is the vibrant residential and cultural heart of the city. Composed of dozens of soaring residential spires connected by sky-bridges and aerial tram lines, Zone B houses the majority of Somnarak's civilian population, guild artisans, and relocated frontier refugees.</p>
      <h2>Key Landmarks</h2>
      <ul>
        <li><b>The Orphan Bell Tower:</b> Historic gothic tower in Sector B-01, housing the memorial bell that resonates in sympathy with SE-001.</li>
        <li><b>The Silk Lofts:</b> Sprawling multi-tier textile mills where the Weavers Guild processes Alpha-spun silk.</li>
        <li><b>Sector B-04 (Cheonbulok District):</b> The cultural enclave of the Cheonbulok refugees, characterized by terraced housing and evening lanterns.</li>
      </ul>
    """
)

# 3. Zone C
write_page(
    folder="locations",
    filename="zone-c-collectors-row.html",
    title="Zone C — Collector’s Row (수집가의 회랑)",
    subtitle="The Grand Merchant Bazaar · Relic Exchanges, Pawn Alleys, and Underworld Ingress",
    color="#f1df76",
    icon_svg="icon_dept_f3_extraction.svg",
    meta_cards=[
        ("District Designation", "Zone C · Commercial, Relic &amp; Scrap Trading Ward"),
        ("Key Authority", "The Collectors Guild &amp; Warden Commerce Bureau"),
        ("Major Commerce", "Precursor Relic Auctions, Han Crystal Pawn, Food Stalls"),
        ("Subterranean Hazards", "Ingress to the Lawless Underworld &amp; Black Markets"),
        ("Security Level", "Grade 3 (Heavy Warden Presence / UCD Raids)")
    ],
    article_body="""
      <h2>The Roaring Relic Bazaar</h2>
      <p><b>Zone C (Collector's Row)</b> is a dense, multi-tiered commercial maze illuminated by buzzing amber neon signs and steam-vent lanterns. Here, scavengers, wasteland merchants of the Horizon Caravan, and licensed relic dealers trade pre-cataclysm artifacts, scrap metals, and distilled Han crystals.</p>
      <h2>Pawn Alleys &amp; Underworld Ingress</h2>
      <p>Behind the regulated auction halls lie the narrow "Pawn Alleys," where unregistered dealers barter illicit memory vials and contraband gear. Beneath the street grates lie the drainage ducts leading directly into the Underworld.</p>
    """
)

# 4. Zone D
write_page(
    folder="locations",
    filename="zone-d-forge-and-gardens.html",
    title="Zone D — Forge &amp; Gardens (단조와 수목원 구역)",
    subtitle="Heavy Industrial Foundries · Alpha Sap Arboretums, Research Labs, and The Hollow Glass",
    color="#47c978",
    icon_svg="icon_dept_f4_insight_forge.svg",
    meta_cards=[
        ("District Designation", "Zone D · Heavy Industry &amp; Agricultural Biospheres"),
        ("Primary Assets", "The Titan Foundries, The Grand Arboretums, Hydroponics"),
        ("Social Hub", "The Hollow Glass Tavern (Sector D-09)"),
        ("Managing Guilds", "The Architects Guild &amp; Agricultural Directorate"),
        ("Security Level", "Grade 3 (Industrial Defense Units)")
    ],
    article_body="""
      <h2>The Industrial &amp; Agricultural Heart</h2>
      <p><b>Zone D (Forge &amp; Gardens)</b> presents a striking contrast between colossal, smoke-belching foundries of the Architects Guild and vast, luminous glass-domed arboretums fed by Alpha Sap runoff. This district generates the building materials, replacement armor plates, and synthesized rations that sustain the entire city.</p>
      <h2>The Hollow Glass Tavern</h2>
      <p>Nestled between two abandoned blast furnaces in Sector D-09 lies <i>The Hollow Glass</i>, a famous neutral tavern run by Barkeeper Bong where off-duty wardens, underworld smugglers, and wasteland scouts mingle in uneasy peace.</p>
    """
)

# 5. Zone E
write_page(
    folder="locations",
    filename="zone-e-perimeter-bulwark.html",
    title="Zone E — Perimeter Bulwark (외곽 대방벽)",
    subtitle="The Titan Wall · Heavy Artillery Batteries, Border Watch Command, and Gate Outposts",
    color="#d7d7d7",
    icon_svg="icon_dept_f5_border_watch.svg",
    meta_cards=[
        ("District Designation", "Zone E · Military Bulwark &amp; Wasteland Border"),
        ("Wall Dimensions", "Height: 120m · Thickness: 45m · Circumference: 68km"),
        ("Command Unit", "Floor 5 Border Watch &amp; Warden 1st Division"),
        ("Garrison Outposts", "Gate of Dawn, North Iron Gate, SED Outpost Alpha"),
        ("Security Level", "Grade 4 (Active Military War Zone)")
    ],
    article_body="""
      <h2>The Great Titan Wall</h2>
      <p><b>Zone E (Perimeter Bulwark)</b> is the colossal outer ring of fortifications that seals Somnarak from the surrounding wastelands. Rising 120 meters above the ash plains, the Wall is armed with heavy kinetic cannons, resonant barrier projectors, and searchlight arrays.</p>
      <h2>The Border Watch Garrison</h2>
      <p>Under the command of Lead Mellda, the garrison stationed on the Bulwark conducts 24-hour vigils, scanning the horizon for entity migration swarms and coordinating the departure of SED exploration convoys.</p>
    """
)

# 6. The Desolate
write_page(
    folder="locations",
    filename="the-desolate.html",
    title="The Desolate (황무지 — The Outskirts)",
    subtitle="The Infinite Ashlands · Precursor Ruins, Toxic Han Storms, and Feral Horrors",
    color="#e8a317",
    icon_svg="icon_dept_f5_border_watch.svg",
    meta_cards=[
        ("Geographical Class", "Post-Cataclysm Ash Desert &amp; Shifting Miasma Plains"),
        ("Environmental Hazard", "Grade V Toxic Han Storms, Temporal Bleed"),
        ("Inhabitants", "Feral Sorrow Entities, Horizon Caravans, Outcast Nomads"),
        ("Known Ruins", "Sunken Citadel of Cheonbulok, Old Cheongula Sub-Levels"),
        ("Exploration Lead", "Yeonhwa (Sorrow Exploration Division)")
    ],
    article_body="""
      <h2>The Wasteland Beyond the Wall</h2>
      <p><b>The Desolate</b> (황무지) is the endless expanse of gray ash, petrified forests, and shattered precursor ruins that stretches endlessly beyond Somnarak’s Titan Wall. Bathed in constant twilight and swept by violent Han dust storms, the wasteland is hostile to all unprotected life.</p>
      <h2>Topological Instability</h2>
      <p>Due to the uncontained psychic pressure of the Maw beneath the earth, the topography of The Desolate shifts unpredictably. Landmarks documented by SED cartographers one month may sink beneath the ash or reappear kilometers away the next.</p>
    """
)

# 7. The Maw
write_page(
    folder="locations",
    filename="the-maw.html",
    title="The Maw (심연의 아가리 — The Abyssal Rift)",
    subtitle="The Primordial Rift · Bottomless Chasm of Weeping and Genesis Point of Calamities",
    color="#8d2e42",
    icon_svg="icon_dept_f8_gate_watch.svg",
    meta_cards=[
        ("Geological Class", "Metaphysical Chasm &amp; Infinite Psychic Sinkhole"),
        ("Depth", "Unfathomable (Estimated > 15,000m to Core Horizon)"),
        ("Origin Point", "Cheongula Cataclysm (Year 3,892)"),
        ("Guardians", "Floor 8 Gate Watch under Command of Xyan (The Exile)"),
        ("Containment Status", "Sealed by the Hand of Change Basal Ring")
    ],
    article_body="""
      <h2>The Infinite Pit of Grief</h2>
      <p><b>The Maw</b> (심연의 아가리) is the bottomless metaphysical abyss that yawns beneath the lowest foundations of the Hand of Change. Formed during the cataclysm of Year 3,892, it is the absolute origin point of all Sorrow Entities and the ultimate repository of humanity’s unexpressed sorrow.</p>
      <h2>The Gate Watch Vigil</h2>
      <p>Directly above the opening of the Maw sits Floor 8 (Gate Watch). Commander Xyan and his elite sentries maintain a perpetual watch over the chasm, holding the heavy blast iris shut against the rising tide of abyssal horrors.</p>
    """
)

# 8. Library of Stolen Pasts
write_page(
    folder="locations",
    filename="the-library-of-stolen-pasts.html",
    title="The Library of Stolen Pasts (빼앗긴 과거의 도서관)",
    subtitle="Subterranean Memory Archive · The Vault of Confiscated Identities in Sector B-02",
    color="#cbd5e1",
    icon_svg="icon_dept_f6_deep_vault.svg",
    meta_cards=[
        ("Facility Type", "Illicit Memory Archive &amp; Forensic Vault"),
        ("Location", "Sector B-02 Sub-Basement Tier 4"),
        ("Presiding Keeper", "Investigator Minho / Floor 6 Custodians"),
        ("Stored Holdings", "Over 50,000 Confiscated &amp; Scrubbed Memory Jars"),
        ("Security Status", "Strict Surveillance &amp; Forensic Lock")
    ],
    article_body="""
      <h2>The Crypt of Forgotten Lives</h2>
      <p><b>The Library of Stolen Pasts</b> is a hidden, subterranean vault situated beneath the West Ward. Maintained jointly by forensic investigators and Floor 6 deep archivists, this secure repository houses tens of thousands of glowing glass jars containing memories confiscated from illegal Memory Washer dens.</p>
    """
)

# 9. Orphan Bell Tower
write_page(
    folder="locations",
    filename="the-orphan-bell-tower.html",
    title="The Orphan Bell Tower (고아 종탑)",
    subtitle="Historic Sanctuary of Sector B-01 · The Resonant Spire of Mourning",
    color="#38bdf8",
    icon_svg="somnarak_city_icon.svg",
    meta_cards=[
        ("Structure Type", "Historic Monument &amp; Acoustic Sanctuary"),
        ("Location", "Zone B · Sector B-01 Central Plaza"),
        ("Resonant Entity", "Acoustic Symbiosis with SE-001 (The Orphaned Bell)"),
        ("Chime Frequency", "432 Hz Pure Lament Tone"),
        ("Civic Function", "Memorial Gathering &amp; Evening Bell Tolling")
    ],
    article_body="""
      <h2>The Spire of the Quiet Chime</h2>
      <p>Rising 80 meters above the cobbled plaza of Sector B-01, the <b>Orphan Bell Tower</b> is one of the oldest surviving structures in Somnarak. Its massive bronze bell was forged from mourning steel, ringing at dusk to pacify civilian sorrow across the West Ward.</p>
    """
)

# 10. The Hollow Glass
write_page(
    folder="locations",
    filename="the-hollow-glass.html",
    title="The Hollow Glass (공허의 잔)",
    subtitle="The Neutral Underworld Tavern · Information Exchange of Sector D-09",
    color="#e8a317",
    icon_svg="icon_dept_f7_shadow_corps.svg",
    meta_cards=[
        ("Establishment Type", "Neutral Saloon &amp; Black-Market Information Hub"),
        ("Location", "Zone D · Sector D-09 Foundry Alley"),
        ("Proprietor", "Barkeeper Bong (Retired Floor 7 Operative)"),
        ("Patrons", "Wardens, Scavengers, Shadow Corps, Horizon Traders"),
        ("Rules of the House", "Absolute Neutrality · Zero Combat Allowed")
    ],
    article_body="""
      <h2>The Tavern Where Enemies Drink</h2>
      <p><b>The Hollow Glass</b> is a legendary tavern built inside a decommissioned reverberation kiln in Zone D. Under the ironclad neutrality enforced by Barkeeper Bong, operatives from the Directorate and outlaws from the Underworld sit side by side to trade rumors, wasteland coordinates, and rare vintage Alpha brews.</p>
    """
)

# 11. Locations Hub (index.html)
write_page(
    folder="locations",
    filename="index.html",
    title="Atlas, Maps &amp; Locations Hub",
    subtitle="Comprehensive Geography of Somnarak, The Urban Zones, The Maw, and The Desolate",
    color="#38bdf8",
    icon_svg="somnarak_city_icon.svg",
    meta_cards=[
        ("Total Indexed Districts", "10 Major Zones &amp; Landmarks"),
        ("Cartographic Authority", "Sorrow Exploration Division (SED) &amp; Architects"),
        ("Interactive Schematics", "Facility Cutaway &amp; City Master Blueprint"),
        ("Active Era", "Year 4,238 · Dawn Initiative")
    ],
    article_body="""
      <h2>Urban Zones &amp; The Five Rings</h2>
      <div class="entity-gallery">
        <a class="entity-card" href="zone-a-core-nexus.html" style="--card-border:#ef5b55">
          <img src="../assets/icons/icon_dept_f1_neutral.svg" alt="">
          <h3>Zone A: Core Nexus</h3>
          <p>Directorate Spire, Alpha Tree Basin &amp; Council</p>
        </a>
        <a class="entity-card" href="zone-b-west-ward.html" style="--card-border:#38bdf8">
          <img src="../assets/icons/somnarak_city_icon.svg" alt="">
          <h3>Zone B: West Ward</h3>
          <p>Residential Spires, Silk Lofts &amp; Enclaves</p>
        </a>
        <a class="entity-card" href="zone-c-collectors-row.html" style="--card-border:#f1df76">
          <img src="../assets/icons/icon_dept_f3_extraction.svg" alt="">
          <h3>Zone C: Collector's Row</h3>
          <p>Relic Bazaar, Pawn Alleys &amp; Underworld Ingress</p>
        </a>
        <a class="entity-card" href="zone-d-forge-and-gardens.html" style="--card-border:#47c978">
          <img src="../assets/icons/icon_dept_f4_insight_forge.svg" alt="">
          <h3>Zone D: Forge &amp; Gardens</h3>
          <p>Heavy Foundries, Arboretums &amp; The Hollow Glass</p>
        </a>
        <a class="entity-card" href="zone-e-perimeter-bulwark.html" style="--card-border:#d7d7d7">
          <img src="../assets/icons/icon_dept_f5_border_watch.svg" alt="">
          <h3>Zone E: Perimeter Bulwark</h3>
          <p>Titan Wall, Artillery Batteries &amp; Gates</p>
        </a>
      </div>

      <h2>Abyssal Depths &amp; Wasteland Outskirts</h2>
      <div class="entity-gallery">
        <a class="entity-card" href="the-maw.html" style="--card-border:#8d2e42">
          <img src="../assets/icons/icon_dept_f8_gate_watch.svg" alt="">
          <h3>The Abyssal Maw</h3>
          <p>The Primordial Rift &amp; Chasm of Grief</p>
        </a>
        <a class="entity-card" href="the-desolate.html" style="--card-border:#e8a317">
          <img src="../assets/icons/icon_dept_f5_border_watch.svg" alt="">
          <h3>The Desolate</h3>
          <p>The Ash Plains &amp; Precursor Ruins</p>
        </a>
        <a class="entity-card" href="the-library-of-stolen-pasts.html" style="--card-border:#cbd5e1">
          <img src="../assets/icons/icon_dept_f6_deep_vault.svg" alt="">
          <h3>Library of Stolen Pasts</h3>
          <p>Subterranean Memory Archive (Sector B-02)</p>
        </a>
        <a class="entity-card" href="the-orphan-bell-tower.html" style="--card-border:#38bdf8">
          <img src="../assets/icons/somnarak_city_icon.svg" alt="">
          <h3>Orphan Bell Tower</h3>
          <p>Historic Gothic Bell Spire (Sector B-01)</p>
        </a>
        <a class="entity-card" href="the-hollow-glass.html" style="--card-border:#e8a317">
          <img src="../assets/icons/icon_dept_f7_shadow_corps.svg" alt="">
          <h3>The Hollow Glass</h3>
          <p>Neutral Underworld Tavern (Sector D-09)</p>
        </a>
      </div>
    """
)

print("Locations section built successfully.")
