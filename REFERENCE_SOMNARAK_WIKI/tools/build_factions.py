import os
from generate_wiki_content import write_page

print("Building Factions Section...")

# 1. Reverie Directorate
write_page(
    folder="factions",
    filename="the-reverie-directorate.html",
    title="The Reverie Directorate (레버리 관리국)",
    subtitle="Supreme Governing Authority · Master of the Hand of Change · Custodian of the Five Zones",
    color="#ef5b55",
    icon_svg="icon_dept_f1_neutral.svg",
    meta_cards=[
        ("Institutional Classification", "Supreme Civil &amp; Military Directorate"),
        ("Headquarters", "Zone A · The Directorate Spire &amp; Floor 1"),
        ("Supreme Commander", "Director Majin (Echo-Core 1)"),
        ("Executive Arm", "Hand of Change (8 Operational Floors)"),
        ("Active Mandate", "Civic Stability, Han Refining, Dawn Initiative")
    ],
    article_body="""
      <h2>Institutional Overview</h2>
      <p>The <b>Reverie Directorate</b> (레버리 관리국, <i>Rebeori Gwanriguk</i>) is the central governing institution, scientific authority, and military command of Somnarak. Established in the aftermath of the Year 3,892 Cheongula Cataclysm, the Directorate exercises supreme jurisdiction over the city's energy distribution, containment infrastructure, M.A.W. manufacturing, and border defense.</p>
      <p>Operating from the monolithic Directorate Spire in Zone A and the subterranean Hand of Change complex, the Directorate is divided into twelve specialized administrative bureaus and eight operational floors, coordinating thousands of researchers, wardens, containment specialists, and alchemical engineers.</p>

      <h2>Organizational Hierarchy &amp; Bureaus</h2>
      <table class="data-table">
        <thead>
          <tr>
            <th>Bureau</th>
            <th>Primary Jurisdiction</th>
            <th>Executive Oversight</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><b>Bureau of Supreme Command</b></td>
            <td>Strategic city policy, Dawn Initiative, emergency martial law</td>
            <td>Director Majin</td>
          </tr>
          <tr>
            <td><b>Bureau of Facility Telemetry</b></td>
            <td>Floor telemetry, algorithmic prediction, energy balance</td>
            <td>Seiyon (The Secretary)</td>
          </tr>
          <tr>
            <td><b>Bureau of Containment Logistics</b></td>
            <td>Entity suppression protocols, cell reinforcement, armor supply</td>
            <td>Dekan &amp; The Wardens</td>
          </tr>
          <tr>
            <td><b>Bureau of Metaphysical Research</b></td>
            <td>Han thermodynamic studies, Dream Diving, taboo monitoring</td>
            <td>Ayshuk &amp; Insight Forge</td>
          </tr>
        </tbody>
      </table>

      <h2>The Hand of Change Mandate</h2>
      <p>The Directorate's most vital asset is the <b>Hand of Change</b>, an eight-floor subterranean facility directly integrated with the root network of the Alpha Tree. Here, raw sorrow extracted from containment cells is refined into the lifeblood of Somnarak, ensuring the city's power grid never fails.</p>
    """
)

# 2. The High Council
write_page(
    folder="factions",
    filename="the-high-council.html",
    title="The High Council of Elders (원로 최고평의회)",
    subtitle="Legislative Assembly of Somnarak · Aristocratic Overseers of Commerce and Civil Law",
    color="#e6c94d",
    icon_svg="somnarak_city_icon.svg",
    meta_cards=[
        ("Governing Type", "Oligarchic Legislative Council"),
        ("Chamber Location", "Zone A · The High Rotunda of Spires"),
        ("Presiding Officer", "High Elder Han Baek-Ryong"),
        ("Primary Influence", "Civic Taxation, Alpha Sap Allocation, Trade Charters"),
        ("Political Alignment", "Conservative Pragmatism / Directorate Oversight")
    ],
    article_body="""
      <h2>Council Structure &amp; Governance</h2>
      <p>The <b>High Council of Elders</b> (원로 최고평의회) is the aristocratic legislative assembly representing the founding merchant families, industrial cartels, and senior district elders of Somnarak. While Director Majin wields absolute executive authority during containment crises, the High Council manages civil law, internal trade tariffs, residential zoning, and tax collection.</p>

      <h2>Political Dynamic with the Directorate</h2>
      <p>The relationship between the High Council and the Reverie Directorate has historically been characterized by tense negotiation. While the Council finances major infrastructure projects and supplies raw materials from the industrial foundries of Zone D, they continuously lobby for greater civilian access to refined Alpha Sap and reduced expenditure on deep-containment research.</p>
    """
)

# 3. The Architects
write_page(
    folder="factions",
    filename="the-architects.html",
    title="The Architects Guild (건축가 협회)",
    subtitle="Master Masons and Spatial Engineers · Builders of the Resonant Spires",
    color="#38bdf8",
    icon_svg="icon_dept_f4_insight_forge.svg",
    meta_cards=[
        ("Guild Classification", "Structural &amp; Metaphysical Engineering Guild"),
        ("Guildmaster", "Grand Master Doha / Artisan Kael"),
        ("Headquarters", "Zone D · The Foundational Masonry Spire"),
        ("Core Technology", "Resonant Granite, Spatial Anchors, Hydraulic Bulkheads"),
        ("Signature Project", "Hand of Change Primary Containment Lattice")
    ],
    article_body="""
      <h2>Architectural Philosophy &amp; Guild Mandate</h2>
      <p>The <b>Architects Guild</b> (건축가 협회) consists of the master builders, structural engineers, and spatial metaphysicians who constructed the spires, bridges, and containment cells of Somnarak. Their unique engineering discipline blends standard architectural physics with <i>Resonant Geometry</i>—the art of shaping physical materials to deflect and nullify high-frequency emotional waves.</p>
      <h2>Key Innovations</h2>
      <ul>
        <li><b>Resonant Granite:</b> Composite stone infused with micro-pulverized Alpha Sap, capable of absorbing kinetic and psychic shockwaves without cracking.</li>
        <li><b>Spatial Anchors:</b> Heavy pylons driven into the bedrock that prevent non-Euclidean spatial distortions caused by Calamity-class entities.</li>
      </ul>
    """
)

# 4. The Weavers
write_page(
    folder="factions",
    filename="the-weavers.html",
    title="The Weavers Guild (직조공 협회)",
    subtitle="Artisans of Consciousness · Psychotropic Silk Spinners and M.A.W. Suit Tailors",
    color="#f0a6c4",
    icon_svg="icon_dept_f3_extraction.svg",
    meta_cards=[
        ("Guild Classification", "Psychic Textile &amp; Armor Manufacturing Guild"),
        ("Grand Mistress", "Mistress Soojin"),
        ("Workshops", "Zone B · The Silk Lofts / Floor 3 Tailories"),
        ("Core Material", "Alpha-Spun Psychotropic Silk &amp; Memory Filament"),
        ("Primary Product", "M.A.W. Resonant Suits &amp; Mental Protective Shrouds")
    ],
    article_body="""
      <h2>The Art of Psychic Weaving</h2>
      <p>The <b>Weavers Guild</b> (직조공 협회) holds the sacred monopoly on spinning and tailoring psychotropic fabrics in Somnarak. By blending natural silkworm thread with crystallized Alpha Sap and silver memory filaments, the Weavers produce cloth capable of deflecting mental attacks, insulating against psychic miasma, and binding volatile Han energy into wearable M.A.W. Suits.</p>
      <h2>The Catharsis Loom</h2>
      <p>The centerpiece of the guild is the <i>Catharsis Loom</i>, a colossal harmonic weaving frame designed by Mistress Soojin. The loom translates the emotional frequencies of harvested entities into intricate geometric patterns, creating suits that empower operatives while shielding their minds from madness.</p>
    """
)

# 5. The Wardens
write_page(
    folder="factions",
    filename="the-wardens.html",
    title="The Wardens of Somnarak (수호단)",
    subtitle="The Iron Constabulary · Peacekeepers of the Five Zones &amp; Containment First-Responders",
    color="#6f7ee8",
    icon_svg="icon_dept_f2_maws_keep.svg",
    meta_cards=[
        ("Organization Type", "Paramilitary Constabulary &amp; City Defense"),
        ("Supreme Marshal", "Marshal Taeho"),
        ("Garrison Posts", "Zone A Central Barracks &amp; Zone E Bulwark"),
        ("Standard Gear", "Lament-Reinforced Armor &amp; Shock Mauls"),
        ("Civic Responsibility", "Riot Control, District Curfew, Anti-Breach Defense")
    ],
    article_body="""
      <h2>The Constabulary Mandate</h2>
      <p>The <b>Wardens</b> (수호단, <i>Suhodan</i>) are the uniformed law enforcement officers and first-response containment squads of Somnarak. Stationed at fortified watchtowers across all five urban zones, the Wardens maintain civil order, enforce Directorate curfews, and deploy tactical suppression teams when rogue entities breach the facility perimeter.</p>
      <h2>Training &amp; Tactical Doctrine</h2>
      <p>Every Warden undergoes intense mental fortitude conditioning at the Zone E Academy to resist panic effects. Armed with heavy shock-batons and kinetic blast shields, they form the frontline bulwark protecting civilian spires from sudden horror outbreaks.</p>
    """
)

# 6. The Collectors
write_page(
    folder="factions",
    filename="the-collectors.html",
    title="The Collectors Guild (수집가 길드)",
    subtitle="Relic Appraisers, Salvage Merchants, and Antiquarians of Precursor Artifacts",
    color="#f1df76",
    icon_svg="icon_dept_f3_extraction.svg",
    meta_cards=[
        ("Guild Classification", "Commercial Appraisal &amp; Salvage Syndicate"),
        ("Headquarters", "Zone C · Collector’s Row"),
        ("Guildmaster", "Elder Jin of the Golden Scales"),
        ("Primary Commerce", "Precursor Relic Valuation, Han Crystal Trade, Pawn Exchanges"),
        ("Affiliation", "Semi-Independent Guild")
    ],
    article_body="""
      <h2>Commerce of the Forbidden</h2>
      <p>The <b>Collectors Guild</b> (수집가 길드) operates from the dense, neon-lit alleys of Zone C (Collector's Row). Specializing in the recovery, appraisal, and auctioning of pre-cataclysm machinery and crystallized Han relics brought back from The Desolate, the Collectors are the economic engine behind Somnarak's technological retrofitting.</p>
      <h2>The Relic Valuation Scale</h2>
      <p>Using calibrated resonance scales, guild appraisers determine the emotional purity and energy yield of salvaged artifacts, converting raw wasteland salvage into spendable Echo-Tokens.</p>
    """
)

# 7. Underworld & Wound Walkers
write_page(
    folder="factions",
    filename="the-underworld-and-wound-walkers.html",
    title="The Underworld &amp; The Wound Walkers (상흔의 순례자)",
    subtitle="The Subterranean Shadow Society · Outcasts, Scrap-Divers, and Heretical Cults",
    color="#8d2e42",
    icon_svg="icon_dept_f7_shadow_corps.svg",
    meta_cards=[
        ("Faction Classification", "Underground Subculture &amp; Survivor Network"),
        ("Territory", "Sub-Level Sewers, Abandoned Vats, Zone C Lower Tiers"),
        ("Key Figures", "Barkeeper Bong (The Hollow Glass), Prophet Kye"),
        ("Core Philosophy", "Symbiosis with Han / Acceptance of Grief"),
        ("Threat Level", "Monitored by Shadow Corps (Floor 7)")
    ],
    article_body="""
      <h2>Life in the Subterranean Shadows</h2>
      <p>Beneath the gleaming spires of the upper zones lies the sprawling labyrinth of the <b>Underworld</b>. Inhabited by outcasts, failed operatives, unlicensed relic scavengers, and the philosophical cult known as the <b>Wound Walkers</b> (상흔의 순례자), this sub-level society survives on illicit Alpha Sap taps and discarded containment scrap.</p>
      <h2>The Philosophy of Scars</h2>
      <p>Unlike the Directorate which seeks to harness and refine sorrow, the Wound Walkers believe that grief is the true evolutionary form of human consciousness. Adorning their bodies with ritual scarring and crude Han-imbued jewelry, they navigate the deep conduits of the Maw without fear.</p>
    """
)

# 8. Memory Washers
write_page(
    folder="factions",
    filename="the-memory-washers.html",
    title="The Memory Washers (기억 세척단)",
    subtitle="Illicit Black-Market Syndicate · Identity Scrubbers and Emotional Laundering",
    color="#cbd5e1",
    icon_svg="icon_dept_f6_deep_vault.svg",
    meta_cards=[
        ("Syndicate Type", "Underworld Crime Syndicate"),
        ("Illegal Service", "Trauma Scrubbing, Identity Forgery, Stolen Catharsis"),
        ("Primary Base", "Sector B-02 Sub-Basements"),
        ("Targeted By", "Floor 6 Deep Vault &amp; UCD Tactical Strike Force"),
        ("Taboo Violation", "Taboo 1 (Memory Counterfeiting)")
    ],
    article_body="""
      <h2>The Black Market of Forgetfulness</h2>
      <p>The <b>Memory Washers</b> (기억 세척단) are a notorious underworld syndicate that trades in the most precious commodity in Somnarak: oblivion. For citizens and traumatized veterans unable to bear their personal grief, the Washers use bootleg Alpha Sap distillates to forcefully scrub traumatic memories, selling the extracted emotional residue on the black market.</p>
    """
)

# 9. Horizon Caravan
write_page(
    folder="factions",
    filename="the-horizon-caravan.html",
    title="The Horizon Caravan (지평선 캐러밴)",
    subtitle="Nomadic Wasteland Merchant Fleet · Crawlers of the Desolate Ashlands",
    color="#e8a317",
    icon_svg="somnarak_city_icon.svg",
    meta_cards=[
        ("Fleet Classification", "Armored Nomadic Trade Caravan"),
        ("Vessels", "Titan Crawler 'Gilded Horizon' &amp; 14 Escort Rigs"),
        ("Caravan Master", "Captain Kang"),
        ("Operational Zone", "The Desolate / Precursor Outskirts"),
        ("Trade Goods", "Ancient Precursor Alloy, Rare Sap Flora, Relics")
    ],
    article_body="""
      <h2>Pioneers of the Ashen Horizon</h2>
      <p>The <b>Horizon Caravan</b> (지평선 캐러밴) is a fleet of colossal, tracked land-crawlers that traverses the treacherous wastelands beyond Zone E. Trading between Somnarak and isolated outpost settlements across The Desolate, they brave toxic Han sandstorms and feral entity packs to bring back invaluable pre-cataclysm technologies.</p>
    """
)

# 10. SED Corps
write_page(
    folder="factions",
    filename="the-sed-corps.html",
    title="Sorrow Exploration Division (SED — 비애 탐사대)",
    subtitle="The Vanguard Wasteland Survey Corps · Cartographers of the Unknown",
    color="#4cc9f0",
    icon_svg="icon_dept_f5_border_watch.svg",
    meta_cards=[
        ("Division Classification", "Specialized Deep-Exploration Survey Corps"),
        ("Commanding Officer", "Lead Cartographer Yeonhwa"),
        ("Base of Operations", "Zone E Outpost Alpha"),
        ("Mission Scope", "Topographical Mapping of The Desolate, Precursor Discovery"),
        ("Affiliation", "Reverie Directorate External Division")
    ],
    article_body="""
      <h2>Mapping the Infinite Ruin</h2>
      <p>The <b>Sorrow Exploration Division (SED)</b> is the elite expeditionary arm of the Directorate. Equipped with all-terrain exploration rigs, long-range resonance beacons, and high-tier M.A.W. suits, SED scouts venture hundreds of kilometers into the uncharted ash plains to catalog topological shifts and identify emerging threats before they reach Somnarak.</p>
    """
)

# 11. UCD Strike Force
write_page(
    folder="factions",
    filename="the-ucd-strike-force.html",
    title="Underworld Containment Division (UCD — 암흑가 진압대)",
    subtitle="Tactical Breach Strike Division · Hunters of Rogue Entities &amp; Black Markets",
    color="#ef5b55",
    icon_svg="icon_dept_f7_shadow_corps.svg",
    meta_cards=[
        ("Division Classification", "High-Intensity Urban Strike Division"),
        ("Division Commander", "Commander Taeho"),
        ("Operational Zone", "Zone C Underworld &amp; Sub-Level Facilities"),
        ("Tactical Doctrine", "Rapid Incursion, Anti-Syndicate Raids, Relic Seizure"),
        ("Affiliation", "Joint Directorate-Warden Tactical Task Force")
    ],
    article_body="""
      <h2>Enforcing the Iron Law</h2>
      <p>The <b>Underworld Containment Division (UCD)</b> is the Directorate’s heavy-response tactical task force assigned to root out illegal syndicates, shut down unauthorized Han extraction dens, and neutralize escaped entities hiding in the labyrinthine sub-levels of Somnarak.</p>
    """
)

# 12. Factions Hub (index.html)
write_page(
    folder="factions",
    filename="index.html",
    title="Factions, Guilds &amp; Organizations Hub",
    subtitle="Comprehensive Directory of Somnarak Institutions, Artisan Guilds, and Underworld Syndicates",
    color="#f1df76",
    icon_svg="somnarak_city_icon.svg",
    meta_cards=[
        ("Total Indexed Factions", "11 Major Organizations"),
        ("Authority Structure", "Directorate Central Hierarchy &amp; Independent Guilds"),
        ("Active Era", "Year 4,238 · Dawn Initiative"),
        ("Archive Integrity", "100% Directorate Verified")
    ],
    article_body="""
      <h2>Governing &amp; Military Institutions</h2>
      <div class="entity-gallery">
        <a class="entity-card" href="the-reverie-directorate.html" style="--card-border:#ef5b55">
          <img src="../assets/icons/icon_dept_f1_neutral.svg" alt="">
          <h3>Reverie Directorate</h3>
          <p>Supreme Authority · Hand of Change</p>
        </a>
        <a class="entity-card" href="the-high-council.html" style="--card-border:#e6c94d">
          <img src="../assets/icons/somnarak_city_icon.svg" alt="">
          <h3>The High Council</h3>
          <p>Legislative Senate · Commerce Overseers</p>
        </a>
        <a class="entity-card" href="the-wardens.html" style="--card-border:#6f7ee8">
          <img src="../assets/icons/icon_dept_f2_maws_keep.svg" alt="">
          <h3>The Wardens</h3>
          <p>Iron Constabulary · City Peacekeepers</p>
        </a>
        <a class="entity-card" href="the-ucd-strike-force.html" style="--card-border:#ef5b55">
          <img src="../assets/icons/icon_dept_f7_shadow_corps.svg" alt="">
          <h3>UCD Strike Force</h3>
          <p>Underworld Breach Suppression Squad</p>
        </a>
        <a class="entity-card" href="the-sed-corps.html" style="--card-border:#4cc9f0">
          <img src="../assets/icons/icon_dept_f5_border_watch.svg" alt="">
          <h3>SED Survey Corps</h3>
          <p>Wasteland Exploration Division</p>
        </a>
      </div>

      <h2>Artisan Guilds &amp; Underworld Syndicates</h2>
      <div class="entity-gallery">
        <a class="entity-card" href="the-architects.html" style="--card-border:#38bdf8">
          <img src="../assets/icons/icon_dept_f4_insight_forge.svg" alt="">
          <h3>The Architects</h3>
          <p>Resonant Masons · Spire Builders</p>
        </a>
        <a class="entity-card" href="the-weavers.html" style="--card-border:#f0a6c4">
          <img src="../assets/icons/icon_dept_f3_extraction.svg" alt="">
          <h3>The Weavers Guild</h3>
          <p>Psychotropic Silk &amp; Armor Tailors</p>
        </a>
        <a class="entity-card" href="the-collectors.html" style="--card-border:#f1df76">
          <img src="../assets/icons/icon_dept_f3_extraction.svg" alt="">
          <h3>The Collectors</h3>
          <p>Relic Appraisers · Pawn Exchanges</p>
        </a>
        <a class="entity-card" href="the-horizon-caravan.html" style="--card-border:#e8a317">
          <img src="../assets/icons/somnarak_city_icon.svg" alt="">
          <h3>Horizon Caravan</h3>
          <p>Nomadic Wasteland Merchant Fleet</p>
        </a>
        <a class="entity-card" href="the-underworld-and-wound-walkers.html" style="--card-border:#8d2e42">
          <img src="../assets/icons/icon_dept_f7_shadow_corps.svg" alt="">
          <h3>The Wound Walkers</h3>
          <p>Subterranean Outcast Society</p>
        </a>
        <a class="entity-card" href="the-memory-washers.html" style="--card-border:#cbd5e1">
          <img src="../assets/icons/icon_dept_f6_deep_vault.svg" alt="">
          <h3>Memory Washers</h3>
          <p>Black Market Identity Scrubbers</p>
        </a>
      </div>
    """
)

print("Factions section built successfully.")
