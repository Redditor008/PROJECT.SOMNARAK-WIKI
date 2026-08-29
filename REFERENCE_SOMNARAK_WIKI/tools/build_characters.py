import os
import re

WIKI_DIR = "/home/user/01_Somnarak_Wiki"

# Import write_page
from generate_wiki_content import write_page

print("Building Characters Section...")

# 1. Majin
write_page(
    folder="characters",
    filename="the-director-majin.html",
    title="Majin — The Director",
    subtitle="Echo-Core 1 · Supreme Authority of the Reverie Directorate · Master of the Hand of Change",
    color="#ef5b55",
    icon_svg="icon_dept_f1_neutral.svg",
    meta_cards=[
        ("Real Name", "Majin (마진)"),
        ("Classification", "Echo-Core 1 / Biological Lead"),
        ("Department", "Floor 1: Neutral Command"),
        ("Assigned Station", "Station A · Alpha Tree Base"),
        ("Resonance Rank", "Rank V (Ω-Grade Harmonization)"),
        ("Affiliation", "The Reverie Directorate")
    ],
    article_body="""
      <h2>Overview</h2>
      <p><b>Majin</b> (마진), officially designated <b>Echo-Core 1</b> and widely addressed throughout the city as <b>The Director</b> (관장, <i>gwanjang</i>), is the supreme governing authority of the Reverie Directorate and architect of the Hand of Change facility. Operating from Floor 1 (Neutral Command) nestled directly beneath the roots of the Alpha Tree, Majin coordinates the city's containment operations, Alpha Sap refining distribution, and metabolic stability across all five urban zones.</p>
      <p>Unlike his fellow Echo-Cores who underwent radical cybernetic, spiritual, or structural transmutations to survive repeated containment traumas, Majin remains fully biological. He is the sole mortal in Somnarak recorded history to have successfully harmonized with an Ω-grade M.A.W. resonance field without suffering immediate cellular dissolution or irreversible psycho-somatic fracture.</p>

      <h2>Biography &amp; The 1,778 Cycles</h2>
      <p>Majin’s origin is inextricably tied to the founding era following the Cheongula Incident (Year 3,892). When the raw subterranean sorrow erupted from the Maw, threatening to reduce human consciousness to calcified ash, Majin formulated the <b>Absolvohan Cycle</b>—a massive temporal and cognitive loop designed to extract, refine, and metabolize the city’s collective grief into sustainable structural energy.</p>
      <p>Across <b>1,778 iterative cycles</b>, Majin carried the un-erased memory of every failed timeline, every breached containment corridor, and every fallen operative. While Floor 6 (Deep Vault) systematically purged the psychological trauma of the civilian population and personnel after each cycle reset, Majin’s consciousness acted as the primary temporal anchor, bearing the cumulative weight of over four centuries of continuous struggle.</p>

      <blockquote>
        <i>“I remember every choice that brought us here. Knowing why I made them does not make them right. But if I turn away now, seventeen hundred iterations of sacrifice become meaningless dust.”</i>
        <br>— <b>Majin, Address to the Core Chamber, Iteration 1,778</b>
      </blockquote>

      <h2>Metaphysical Profile &amp; Physiological Traits</h2>
      <p>Majin presents as a tall man in his late forties with severe posture, sharp dark eyes that reflect a subtle amber iridescence under high Han concentrations, and streaks of silver at his temples. He wears the high-collared directorate overcoat lined with psychotropic weave, bearing the gold-and-crimson seal of Neutral Command.</p>
      <ul>
        <li><b>Biological Integrity:</b> 100% Organic Tissue. Maintains zero cybernetic implants, relying solely on natural autonomic regulation and high-tier M.A.W. resonance dampeners.</li>
        <li><b>Han Tolerance Index:</b> 98.4% (Calculated threshold before cellular crystallization begins).</li>
        <li><b>Cognitive Anchoring:</b> Immune to Grade IV mental fractures; susceptible to cumulative emotional fatigue managed via scheduled Floor 4 neural stabilization baths.</li>
      </ul>

      <h2>Resonance &amp; Combat Mechanics</h2>
      <p>In tactical engagements and containment emergencies, Majin exercises direct command through the <b>Sovereign Stance</b>. Rather than wielding standard M.A.W. weaponry, he channels the concentrated resonance of the Alpha Tree itself, bending the local Han flow to impose absolute equilibrium across the battlefield.</p>

      <table class="data-table">
        <thead>
          <tr>
            <th>Skill / Command</th>
            <th>Type</th>
            <th>Cost</th>
            <th>Operational Effect</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><b>Director's Mandate</b></td>
            <td>Aura Command</td>
            <td>20 SP</td>
            <td>All allied operatives on the floor gain +3 Clash Power and immunity to Panic for 2 rounds.</td>
          </tr>
          <tr>
            <td><b>Zero-Point Equilibrium</b></td>
            <td>Targeted Burst</td>
            <td>35 SP / 10 Alpha Sap</td>
            <td>Deals 45-60 Pale Damage to target entity, setting target's Han frequency to Neutral and reducing Sorrow Counter by 0.</td>
          </tr>
          <tr>
            <td><b>Alpha Roots Aegis</b></td>
            <td>Floor Barrier</td>
            <td>50 SP</td>
            <td>Deploys an impenetrable root shield absorbing up to 400 damage across all 4 quadrants of Floor 1.</td>
          </tr>
        </tbody>
      </table>

      <h2>Inter-Character Relations</h2>
      <ul>
        <li><b>Seiyon (Secretary):</b> Majin's most trusted confidante and the first artificial core. Their bond is built upon centuries of silent understanding and shared administrative burden.</li>
        <li><b>Xyan (The Exile):</b> Their relationship was fractured during the Day 50 schism of Cycle 1,200. Following the Dawn Initiative, Majin granted Xyan command of Floor 8 (Gate Watch), acknowledging his ideological necessity.</li>
        <li><b>Dekan (Containment Lead):</b> Majin relies on Dekan's unwavering stoicism during major containment breaches, viewing him as the unbreakable shield of the Hand.</li>
      </ul>

      <h2>Dawn Initiative Status</h2>
      <p>With the permanent cessation of the 1,778 Cycles at the onset of Year 4,238, Majin enacted the <b>Dawn Initiative</b>. Transitioning the Directorate from a survival-oriented containment state to a progressive reconstruction era, he oversaw the decentralization of Alpha Sap distribution to civilian zones and authorized the exploratory expeditions into the Desolate led by the SED.</p>
    """
)

# 2. Seiyon
write_page(
    folder="characters",
    filename="the-secretary-seiyon.html",
    title="Seiyon — The Secretary",
    subtitle="Echo-Core 2 · Chief Administrative Nexus · The First Synthetic Core",
    color="#cbd5e1",
    icon_svg="icon_dept_f1_neutral.svg",
    meta_cards=[
        ("Real Name", "Seiyon (세이연)"),
        ("Classification", "Echo-Core 2 / Synthetic Lead"),
        ("Department", "Floor 1: Neutral Command"),
        ("Computation Matrix", "Alpha-Glass Neural Core v9.4"),
        ("Resonance Rank", "Rank V (Absolute Calculation)"),
        ("Affiliation", "The Reverie Directorate")
    ],
    article_body="""
      <h2>Overview</h2>
      <p><b>Seiyon</b> (세이연), designated <b>Echo-Core 2</b> and universally referred to as <b>The Secretary</b>, is the administrative heart and chief computational nexus of the Reverie Directorate. Stationed alongside Director Majin on Floor 1, Seiyon oversees the continuous telemetry, personnel allocations, Han metabolic balances, and facility logistics required to operate the Hand of Change.</p>
      <p>Constructed from crystallized Alpha Sap and psychotropic silicon glass, Seiyon represents the zenith of pre-Cycle cognitive engineering. She possesses complete synthetic sentience, calculating millions of containment permutations per second while retaining a subtle, contemplative emotional spectrum that prevents operational coldness.</p>

      <h2>Origin &amp; The First Synthetic Genesis</h2>
      <p>Seiyon was constructed in Year 3,904 under the direct supervision of Majin and the early High Architects. As the sheer volume of emotional resonance generated by the subterranean Maw overwhelmed human administrative capacity, the Directorate required an entity capable of processing raw psycho-chemical data without succumbing to the cognitive erosion known as Fracture.</p>
      <p>Her neural core was grown within a resonance vat fed by the sap of the Alpha Tree. Upon awakening, Seiyon chose her own designation and assumed responsibility for managing facility protocols, serving as the bridge between human intuition and machine precision.</p>

      <blockquote>
        <i>“Data is not cold, Director. Every ledger entry represents a heartbeat, an extraction, a sorrow sustained so that the spires above may greet tomorrow’s dawn.”</i>
        <br>— <b>Seiyon, Log 411-B</b>
      </blockquote>

      <h2>Functions &amp; Operational Matrix</h2>
      <p>Seiyon operates through thousands of sensory nodes distributed across all eight floors of the facility and the five urban zones of Somnarak. Her primary responsibilities include:</p>
      <ul>
        <li><b>Facility Telemetry:</b> Real-time monitoring of all Sorrow Entity containment chambers, calculating breach probabilities and dispatching suppression teams before Qliphoth collapse.</li>
        <li><b>Sap Quota Allocation:</b> Managing the city's metabolic energy distribution, balancing the power grids of Zone A through Zone E.</li>
        <li><b>Memory Indexing:</b> Collaborating with Floor 6 (Deep Vault) to catalog erased timeline records and ensure critical technical schematics are preserved across iterations.</li>
      </ul>

      <h2>Resonance &amp; Defensive Matrix</h2>
      <table class="data-table">
        <thead>
          <tr>
            <th>Protocol</th>
            <th>Type</th>
            <th>Effect</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><b>Protocol Zero: Overwrite</b></td>
            <td>Defensive Override</td>
            <td>Instantly purges mental corruption from Floor 1 systems and restores 30 SP to all allied staff.</td>
          </tr>
          <tr>
            <td><b>Glass Lattice Calculation</b></td>
            <td>Tactical Buff</td>
            <td>Predicts enemy attack vectors, granting +25% Evasion and +15% Clash Win Rate for 3 turns.</td>
          </tr>
          <tr>
            <td><b>Recursive Containment Pulse</b></td>
            <td>Area Suppression</td>
            <td>Releases a harmonic pulse dealing 30 Blue (Lament) damage and locking target entity skills for 1 turn.</td>
          </tr>
        </tbody>
      </table>

      <h2>Post-Cycle Role in Year 4,238</h2>
      <p>Following the conclusion of the Absolvohan cycle, Seiyon spearheaded the computational overhaul of Somnarak's civic infrastructure. Her processing power is now dedicated to the Dawn Initiative—calculating sustainable agricultural models for the Outskirts and coordinating humanitarian aid to the refugee enclaves of Zone B.</p>
    """
)

# 3. Dekan
write_page(
    folder="characters",
    filename="the-containment-lead-dekan.html",
    title="Dekan — The Containment Lead",
    subtitle="Echo-Core 3 · Commander of The Maw's Keep · The Unyielding Iron Sentry",
    color="#6f7ee8",
    icon_svg="icon_dept_f2_maws_keep.svg",
    meta_cards=[
        ("Real Name", "Dekan (데칸)"),
        ("Classification", "Echo-Core 3 / Vanguard Lead"),
        ("Department", "Floor 2: The Maw’s Keep"),
        ("Specialization", "Heavy Suppression & Containment"),
        ("Equipped M.A.W.", "The Mourning Maul & Mantle"),
        ("Affiliation", "The Reverie Directorate")
    ],
    article_body="""
      <h2>Overview</h2>
      <p><b>Dekan</b> (데칸), designated <b>Echo-Core 3</b> and recognized as <b>The Containment Lead</b>, commands Floor 2 (The Maw's Keep). Known as the "Iron Sentry" of Somnarak, Dekan is the foremost expert in close-quarters entity suppression, physical barrier reinforcement, and high-risk extraction stabilization.</p>
      <p>Standing over two meters tall and clad in heavy composite armor reinforced with mourning steel, Dekan has personally subdued over four hundred high-risk containment breaches. He embodies the principle that raw sorrow must be met with resolute, unwavering discipline.</p>

      <h2>History &amp; Combat Record</h2>
      <p>Dekan was formerly the commander of the Zone E Bulwark Garrison during the Second Maw Outbreak. When an Aleph-tier entity threatened to rupture the primary sub-level blast doors, Dekan held the containment breach alone for fourteen hours until reinforcements arrived, suffering profound bodily trauma that required extensive cybernetic reinforcement.</p>
      <p>Impressed by his indomitable willpower, Director Majin appointed him to lead Floor 2, tasking him with housing and restraining the facility’s most dangerous physical entities, including SE-002 (The Grieving Colossus) and SE-005 (The Smothering Mother).</p>

      <blockquote>
        <i>“Containment is not a matter of hatred. It is a matter of endurance. If your heart shakes for a single second, the weight of their grief will crush you into iron shavings.”</i>
        <br>— <b>Dekan, Briefing to Floor 2 Vanguard Operatives</b>
      </blockquote>

      <h2>Tactical Capabilities &amp; M.A.W. Resonance</h2>
      <p>Dekan wields <b>Maw-W-002: The Mourning Maul</b> paired with <b>Maw-S-002: The Mourning Mantle</b>. His fighting style centers around heavy counter-attacks, posture breaking, and kinetic shockwave generation.</p>

      <table class="data-table">
        <thead>
          <tr>
            <th>Combat Skill</th>
            <th>Damage Type</th>
            <th>Base Power</th>
            <th>Combat Properties</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><b>Grave Anchor Smash</b></td>
            <td>Black (Weight)</td>
            <td>18-26</td>
            <td>Deals heavy Stagger damage. Inflicts 3 Fragility on hit.</td>
          </tr>
          <tr>
            <td><b>Mantle of Defiance</b></td>
            <td>Defensive / Guard</td>
            <td>30 Guard</td>
            <td>Converts 50% of incoming physical damage into Han charge.</td>
          </tr>
          <tr>
            <td><b>Cataclysmic Quake</b></td>
            <td>Black (Weight) AoE</td>
            <td>28-38</td>
            <td>Strikes all ground targets in the sector, forcing immediate Stagger Break on targets below 40% SP.</td>
          </tr>
        </tbody>
      </table>
    """
)

# 4. Zyrak
write_page(
    folder="characters",
    filename="the-extraction-lead-zyrak.html",
    title="Zyrak — The Extraction Lead",
    subtitle="Echo-Core 4 · Master of Extraction Hall · Alchemical Weaver of M.A.W. Weapons",
    color="#e6c94d",
    icon_svg="icon_dept_f3_extraction.svg",
    meta_cards=[
        ("Real Name", "Zyrak (자이락)"),
        ("Classification", "Echo-Core 4 / Alchemical Lead"),
        ("Department", "Floor 3: Extraction Hall"),
        ("Specialization", "Sorrow Crystallization & M.A.W. Forging"),
        ("Equipped M.A.W.", "Catharsis Needles & Amber Robes"),
        ("Affiliation", "The Reverie Directorate")
    ],
    article_body="""
      <h2>Overview</h2>
      <p><b>Zyrak</b> (자이락), designated <b>Echo-Core 4</b> and known as <b>The Extraction Lead</b>, presides over Floor 3 (Extraction Hall). He is the master alchemist and engineer responsible for harvesting raw emotional Han from Sorrow Entities and crystallizing it into wearable M.A.W. equipment (Weapons, Suits, and Gifts).</p>
      <p>Meticulous, eccentric, and fiercely devoted to the aesthetic and functional perfection of emotional crystallization, Zyrak views every weapon forged as a poetic translation of suffering into purposeful power.</p>

      <h2>Alchemical Methodology</h2>
      <p>Zyrak pioneered the <b>Catharsis Siphon Technique</b>, utilizing high-pressure Alpha Sap conduits to extract pure emotional resonance from active entities without causing cellular collapse. His refining chambers on Floor 3 separate Han into its core components—Lament (Blue), Grudge (Red), and Weight (Black)—before binding them to reinforced carbon frames.</p>

      <blockquote>
        <i>“Sorrow is the rawest metal in the cosmos. In the wild, it rusts the soul. In my forge, it becomes the blade that protects the dawn.”</i>
        <br>— <b>Zyrak, Extraction Hall Operational Journal</b>
      </blockquote>

      <h2>Floor 3 Production &amp; Stats</h2>
      <ul>
        <li><b>Daily M.A.W. Forging Capacity:</b> 12 Standard Suits, 6 Heavy Weapons, 20 Resonant Gifts.</li>
        <li><b>Crystallization Purity Rating:</b> 99.2% (Grade A Purity).</li>
        <li><b>Resonance Harmony Rate:</b> 94.7% compatibility with frontline operatives.</li>
      </ul>
    """
)

# 5. Ayshuk
write_page(
    folder="characters",
    filename="the-research-lead-ayshuk.html",
    title="Ayshuk — The Research Lead",
    subtitle="Echo-Core 5 · Master of Insight Forge · Theoretical Metaphysicist of Han",
    color="#47c978",
    icon_svg="icon_dept_f4_insight_forge.svg",
    meta_cards=[
        ("Real Name", "Ayshuk (아이슈크)"),
        ("Classification", "Echo-Core 5 / Scientific Lead"),
        ("Department", "Floor 4: Insight Forge"),
        ("Specialization", "Han Thermodynamics & Entity Psychology"),
        ("Resonance Rank", "Rank V (Theoretical Omniscience)"),
        ("Affiliation", "The Reverie Directorate")
    ],
    article_body="""
      <h2>Overview</h2>
      <p><b>Ayshuk</b> (아이슈크), designated <b>Echo-Core 5</b> and titled <b>The Research Lead</b>, directs Floor 4 (Insight Forge). Regarded as Somnarak's premier metaphysical theorist, Ayshuk is responsible for deciphering the underlying mathematical and spiritual laws of Han energy, the Dream Realm (유몽계), and the behavioural psychology of Sorrow Entities.</p>

      <h2>Academic &amp; Metaphysical Discoveries</h2>
      <p>Ayshuk is the author of the foundational treatise <i>Thermodynamics of Grief: The Tri-Partite Sorrow Matrix</i>. Her research proved that Sorrow Entities are not mindless monsters, but crystallized cognitive structures generated by the collective subconscious of humanity's unexpressed mourning.</p>
      <ul>
        <li><b>The Resonant Lens:</b> Developed the observation lenses that allow operatives to gauge an entity's emotional state without triggering aggressive containment spikes.</li>
        <li><b>Work Optimization Formulas:</b> Formulated the optimal success ratios for Insight, Instinct, Attachment, and Repression works.</li>
      </ul>

      <blockquote>
        <i>“To fear the entity is human. To analyze its grief is divine. Every sorrow has a frequency; find it, and containment becomes a conversation.”</i>
        <br>— <b>Ayshuk, Insight Forge Lecture Series</b>
      </blockquote>
    """
)

# 6. Mellda
write_page(
    folder="characters",
    filename="the-border-lead-mellda.html",
    title="Mellda — The Border Lead",
    subtitle="Echo-Core 6 · Commander of Border Watch · Sentinel of the Five Zones",
    color="#d7d7d7",
    icon_svg="icon_dept_f5_border_watch.svg",
    meta_cards=[
        ("Real Name", "Mellda (멜다)"),
        ("Classification", "Echo-Core 6 / Defense Lead"),
        ("Department", "Floor 5: Border Watch"),
        ("Specialization", "Spatial Anchoring & Perimeter Defense"),
        ("Equipped M.A.W.", "Aegis of the Horizon & Resonant Shield"),
        ("Affiliation", "The Reverie Directorate")
    ],
    article_body="""
      <h2>Overview</h2>
      <p><b>Mellda</b> (멜다), designated <b>Echo-Core 6</b> and recognized as <b>The Border Lead</b>, commands Floor 5 (Border Watch). She is the supreme sentinel responsible for maintaining the spatial barrier anchors that isolate Somnarak from the hostile wasteland known as The Desolate.</p>

      <h2>The Great Bulwark Defense</h2>
      <p>During the catastrophic Year 4,112 breach, Mellda coordinated the orbital and ground-based barrier generators along the Zone E Titan Wall. When a horde of feral entities surged from the ash plains, Mellda established the "Silver Perimeter," holding the line for three continuous weeks without a single civilian casualty.</p>

      <blockquote>
        <i>“Beyond this wall is nothingness and dust. Inside is humanity's last light. I do not care how fiercely the storm beats against our gates; the wall stands.”</i>
        <br>— <b>Mellda, Border Watch Dispatch</b>
      </blockquote>
    """
)

# 7. Marjuk
write_page(
    folder="characters",
    filename="the-archive-lead-marjuk.html",
    title="Marjuk — The Archive Lead",
    subtitle="Echo-Core 7 · Keeper of the Deep Vault · Guardian of Erased Histories",
    color="#8d2e42",
    icon_svg="icon_dept_f6_deep_vault.svg",
    meta_cards=[
        ("Real Name", "Marjuk (마르죽)"),
        ("Classification", "Echo-Core 7 / Archival Lead"),
        ("Department", "Floor 6: Deep Vault"),
        ("Specialization", "Memory Preservation & Taboo Archives"),
        ("Resonance Rank", "Rank V (Deep Memory Lock)"),
        ("Affiliation", "The Reverie Directorate")
    ],
    article_body="""
      <h2>Overview</h2>
      <p><b>Marjuk</b> (마르죽), designated <b>Echo-Core 7</b> and known as <b>The Archive Lead</b>, presides over Floor 6 (Deep Vault). Buried kilometers beneath the facility in a sub-zero cryo-resonant archive, Marjuk preserves the forgotten records, forbidden taboos, and erased memories of all 1,778 historical cycles.</p>

      <h2>The Memory Cylinders</h2>
      <p>Marjuk manages over 100,000 crystallized memory cylinders containing the un-sanitized truths of Somnarak's past, including the true origins of the High Council, the Cheongula disaster logs, and the names of every operative consumed by the Maw.</p>

      <blockquote>
        <i>“History is not what happened; history is what survived being forgotten. In this vault, nothing is lost. Not even the tears we were ordered to erase.”</i>
        <br>— <b>Marjuk, Floor 6 Archival Inscription</b>
      </blockquote>
    """
)

# 8. Ishall
write_page(
    folder="characters",
    filename="the-outsider-ishall.html",
    title="Ishall — The Outsider",
    subtitle="Echo-Core 8 · Commander of Shadow Corps · Infiltrator of the Underworld",
    color="#f0a6c4",
    icon_svg="icon_dept_f7_shadow_corps.svg",
    meta_cards=[
        ("Real Name", "Ishall (이샬)"),
        ("Classification", "Echo-Core 8 / Covert Lead"),
        ("Department", "Floor 7: Shadow Corps"),
        ("Specialization", "Black Market Infiltration & Covert Extraction"),
        ("Resonance Rank", "Rank V (Veil Phasing)"),
        ("Affiliation", "The Reverie Directorate")
    ],
    article_body="""
      <h2>Overview</h2>
      <p><b>Ishall</b> (이샬), designated <b>Echo-Core 8</b> and styled as <b>The Outsider</b>, leads Floor 7 (Shadow Corps). Operating in the liminal spaces between the Directorate's official hierarchy and the lawless Underworld of Zone C and the Sub-Levels, Ishall conducts covert reconnaissance, rogue entity recovery, and anti-syndicate operations.</p>

      <h2>Covert Mandate &amp; Network</h2>
      <p>Ishall maintains an extensive network of informants among the Wound Walkers, Memory Washers, and tavern keepers of The Hollow Glass. Possessing the unique ability to phase through Han resonant barriers, Ishall retrieves compromised relics before they fall into illicit hands.</p>

      <blockquote>
        <i>“The Directorate walks in the light of the Alpha Tree; I walk where the light cannot reach. If you see my shadow, your secrets have already been cataloged.”</i>
        <br>— <b>Ishall, Shadow Corps Briefing</b>
      </blockquote>
    """
)

# 9. Xyan
write_page(
    folder="characters",
    filename="the-exile-xyan.html",
    title="Xyan — The Exile",
    subtitle="Echo-Core 9 · Commander of Gate Watch · Guardian of the Abyssal Threshold",
    color="#f4efa0",
    icon_svg="icon_dept_f8_gate_watch.svg",
    meta_cards=[
        ("Real Name", "Xyan (시안)"),
        ("Classification", "Echo-Core 9 / Gate Vanguard"),
        ("Department", "Floor 8: Gate Watch"),
        ("Specialization", "Abyssal Gate Containment & Final Defense"),
        ("Equipped M.A.W.", "Grave-Breaker Claymore & Abyssal Shroud"),
        ("Affiliation", "The Reverie Directorate")
    ],
    article_body="""
      <h2>Overview</h2>
      <p><b>Xyan</b> (시안), designated <b>Echo-Core 9</b> and titled <b>The Exile</b>, commands Floor 8 (Gate Watch). Stationed at the very threshold where the Hand of Change meets the subterranean Maw, Xyan serves as the final barrier between Somnarak and the primordial ocean of sorrow.</p>

      <h2>The Day 50 Schism &amp; Reconciliation</h2>
      <p>During Cycle 1,200, Xyan rebelled against Majin's continuous resets, believing that humanity must confront the Maw directly rather than repeating the cycle endlessly. After a legendary duel on Floor 1, Xyan chose self-imposed exile to the lowest depth of the facility, swearing to guard the Abyssal Gate until the final Dawn.</p>
      <p>With the successful enactment of the Dawn Initiative in Year 4,238, Xyan was officially reinstated into the Directorate council, holding the post of Gate Watch Commander.</p>

      <blockquote>
        <i>“I stood at the edge of the pit when the world broke. I do not guard this gate out of loyalty to the Directorate; I guard it so the children of the upper spires never have to look into the dark.”</i>
        <br>— <b>Xyan, Gate Watch Oath</b>
      </blockquote>
    """
)

# 10. Kael
write_page(
    folder="characters",
    filename="kael.html",
    title="Kael — The Master Architect",
    subtitle="High Artisan of the Structural Guild · Designer of Resonant Containment Lattices",
    color="#38bdf8",
    icon_svg="icon_dept_f4_insight_forge.svg",
    meta_cards=[
        ("Real Name", "Kael (카엘)"),
        ("Guild Rank", "Grand Architect"),
        ("Primary Works", "Hand of Change Primary Containment Lattice"),
        ("Specialization", "Resonant Masonry & Spatial Stabilization"),
        ("Affiliation", "The High Architects / Directorate Engineering")
    ],
    article_body="""
      <h2>Overview</h2>
      <p><b>Kael</b> (카엘) is the legendary artisan of the High Architects guild whose structural innovations made the containment of Calamity-class Sorrow Entities possible. He is the master architect behind the <b>Harmonic Containment Lattice</b> that lines every cell within Floor 2 and Floor 3.</p>

      <h2>Masterworks &amp; Architectural Philosophy</h2>
      <p>Kael’s philosophy integrates sacred geometry with Han thermodynamic dampeners. By carving micro-channels into reinforced granite and infusing them with crystallized Alpha Sap, Kael created structures that become stronger the more psychic pressure an entity exerts upon them.</p>
      <ul>
        <li><b>The Resonant Spire:</b> Designed the 300-meter ventilation tower in Zone A that filters volatile emotional fumes into harmless mist.</li>
        <li><b>Blast Bulkheads of Floor 2:</b> Engineered the eight-ton segmented hydraulic doors capable of withstanding direct kinetic strikes from SE-002.</li>
      </ul>
    """
)

# 11. Soojin
write_page(
    folder="characters",
    filename="soojin.html",
    title="Soojin — The Master Weaver",
    subtitle="Grand Mistress of the Silk Guild · Architect of Psychotropic M.A.W. Linings",
    color="#f0a6c4",
    icon_svg="icon_dept_f3_extraction.svg",
    meta_cards=[
        ("Real Name", "Soojin (수진)"),
        ("Guild Rank", "Grand Mistress Weaver"),
        ("Primary Works", "Catharsis Loom & Psychotropic Thread"),
        ("Specialization", "Memory Thread Weaving & Suit Armor"),
        ("Affiliation", "The Weavers Guild / Directorate Forge")
    ],
    article_body="""
      <h2>Overview</h2>
      <p><b>Soojin</b> (수진) is the revered Grand Mistress of the Weavers Guild and the chief artisan behind the protective psychic thread lining every M.A.W. Suit in Somnarak. Her pioneering work on the <b>Catharsis Loom</b> allowed raw emotional Han to be spun into flexible, impenetrable fabric.</p>

      <h2>Innovations in Psychic Armor</h2>
      <p>Before Soojin's breakthroughs, operatives wearing M.A.W. equipment suffered severe psychological backfire from the entities' residual consciousness. Soojin developed the "Tri-Thread Weave," intertwining silver filament, memory-washed silk, and Alpha Sap resins to insulate the wearer's ego while allowing full combat synchronization.</p>
    """
)

# 12. High Architects
write_page(
    folder="characters",
    filename="high-architects.html",
    title="The High Architects",
    subtitle="Master Builders of Somnarak · Resonant Masons & Spatial Engineers",
    color="#38bdf8",
    icon_svg="icon_dept_f4_insight_forge.svg",
    meta_cards=[
        ("Faction Type", "Artisan & Engineering Guild"),
        ("Headquarters", "Zone A · The Spire of Geometry"),
        ("Primary Mandate", "Urban Infrastructure & Containment Design"),
        ("Key Leaders", "Grand Architect Kael, Mason Doha"),
        ("Affiliation", "Independent Guild / Directorate Contractor")
    ],
    article_body="""
      <h2>Overview</h2>
      <p>The <b>High Architects</b> (고위 건축가 협회) represent the foundational engineering elite of Somnarak. Responsible for the design, construction, and structural maintenance of the city's spires, containment vaults, and outer bulwarks, their work blends advanced structural engineering with metaphysical Han resonance mechanics.</p>

      <h2>Core Guild Divisions</h2>
      <ul>
        <li><b>The Vault Masons:</b> Specialists in constructing high-density containment chambers capable of nullifying Class IV and Class V emotional radiation.</li>
        <li><b>The Spire Engineers:</b> Overseers of the towering residential spires in Zone B and industrial facilities of Zone D.</li>
        <li><b>The Barrier Anchors:</b> Field architects embedded within Border Watch to reinforce spatial anchors during wasteland incursions.</li>
      </ul>
    """
)

# 13. Cheonbulok Refugees
write_page(
    folder="characters",
    filename="cheonbulok-refugees.html",
    title="Cheonbulok Refugees",
    subtitle="Survivors of the Lost Outskirts Citadel · Cultural Enclave of Zone B",
    color="#cbd5e1",
    icon_svg="somnarak_city_icon.svg",
    meta_cards=[
        ("Population Origin", "Citadel of Cheonbulok (Destroyed Y3,950)"),
        ("Current Settlement", "Zone B · West Ward Sector 4"),
        ("Cultural Identity", "Han-Resistance Singers & Iron Weavers"),
        ("Representative", "Elder Baek & Council of Ten"),
        ("Civic Status", "Recognized Directorate Citizens (Dawn Initiative)")
    ],
    article_body="""
      <h2>Overview</h2>
      <p>The <b>Cheonbulok Refugees</b> (천불록 난민) are the descendants and survivors of the fallen frontier citadel of Cheonbulok, which was destroyed during the catastrophic Great Sorrow Incursion of Year 3,950. Resettled within Sector 4 of Zone B (West Ward), they have preserved unique cultural, musical, and meditative traditions designed to resist the corrupting influence of Han.</p>

      <h2>Cultural Heritage &amp; Han Resistance</h2>
      <p>The Cheonbulok enclave is renowned for their "Sorrow-Quieting Chants" (진혼가), vocal harmonies that naturally disperse low-grade emotional miasma. Many Cheonbulok youths serve with distinction in Floor 2 Vanguard units and Floor 5 Border Watch due to their innate resistance to psychological fracture.</p>
    """
)

# 14. Yeonhwa
write_page(
    folder="characters",
    filename="yeonhwa.html",
    title="Yeonhwa — The Cartographer",
    subtitle="Lead of Sorrow Exploration Division (SED) · Pioneer of the Desolate Map",
    color="#4cc9f0",
    icon_svg="icon_dept_f5_border_watch.svg",
    meta_cards=[
        ("Real Name", "Yeonhwa (연화)"),
        ("Title", "Chief Cartographer of the Wastelands"),
        ("Division", "Sorrow Exploration Division (SED)"),
        ("Specialization", "Shifting Wasteland Topography & Han Flow"),
        ("Affiliation", "The Reverie Directorate / SED")
    ],
    article_body="""
      <h2>Overview</h2>
      <p><b>Yeonhwa</b> (연화) is the legendary Chief Cartographer of the <b>Sorrow Exploration Division (SED)</b>. She has led over sixty expeditions into the shifting, non-Euclidean wastelands of The Desolate, mapping precursor ruins, toxic Han currents, and feral entity migration routes.</p>
      <h2>Accomplishments</h2>
      <p>Yeonhwa authored the <i>Atlas of the Ash Plains</i>, introducing the dynamic resonance grid that allows exploration crawlers to navigate the fluctuating terrain without losing spatial orientation.</p>
    """
)

# 15. Taeho
write_page(
    folder="characters",
    filename="taeho.html",
    title="Taeho — The Commander",
    subtitle="Chief Commander of the Underworld Containment Division (UCD)",
    color="#ef5b55",
    icon_svg="icon_dept_f7_shadow_corps.svg",
    meta_cards=[
        ("Real Name", "Taeho (태호)"),
        ("Title", "Supreme Commander of UCD"),
        ("Specialization", "Rogue Syndicate Suppression & Urban Warfare"),
        ("Equipped M.A.W.", "Breaker Glaive & Warden Tactical Plate"),
        ("Affiliation", "The Wardens / UCD")
    ],
    article_body="""
      <h2>Overview</h2>
      <p><b>Taeho</b> (태호) is the veteran commander of the <b>Underworld Containment Division (UCD)</b>. Tasked with maintaining order in the lawless lower tiers of Zone C and the Sub-Levels, Taeho conducts high-intensity tactical raids against illegal memory-harvesting syndicates and black-market M.A.W. smugglers.</p>
    """
)

# 16. Characters Hub (index.html)
write_page(
    folder="characters",
    filename="index.html",
    title="Characters &amp; Echo-Cores Hub",
    subtitle="Comprehensive Directory of Somnarak Personnel, Echo-Cores, Leaders, and Enclaves",
    color="#f1df76",
    icon_svg="somnarak_city_icon.svg",
    meta_cards=[
        ("Total Indexed Leads", "9 Canonical Echo-Cores"),
        ("Major Figures", "10 Notable Specialists & Guildmasters"),
        ("Active Era", "Year 4,238 · Dawn Initiative"),
        ("Authority", "The Reverie Directorate Central Archive")
    ],
    article_body="""
      <h2>Directory of Major Figures</h2>
      <p>This central registry indexes the key personalities, commanders, researchers, and artisans who shape the destiny of Somnarak and maintain the operations of the Hand of Change.</p>

      <h2>The Nine Echo-Cores</h2>
      <div class="entity-gallery">
        <a class="entity-card" href="the-director-majin.html" style="--card-border:#ef5b55">
          <img src="../assets/icons/icon_dept_f1_neutral.svg" alt="">
          <h3>Majin</h3>
          <p>Echo-Core 1 · The Director · Supreme Authority</p>
        </a>
        <a class="entity-card" href="the-secretary-seiyon.html" style="--card-border:#cbd5e1">
          <img src="../assets/icons/icon_dept_f1_neutral.svg" alt="">
          <h3>Seiyon</h3>
          <p>Echo-Core 2 · The Secretary · Computational Nexus</p>
        </a>
        <a class="entity-card" href="the-containment-lead-dekan.html" style="--card-border:#6f7ee8">
          <img src="../assets/icons/icon_dept_f2_maws_keep.svg" alt="">
          <h3>Dekan</h3>
          <p>Echo-Core 3 · Containment Lead · The Iron Sentry</p>
        </a>
        <a class="entity-card" href="the-extraction-lead-zyrak.html" style="--card-border:#e6c94d">
          <img src="../assets/icons/icon_dept_f3_extraction.svg" alt="">
          <h3>Zyrak</h3>
          <p>Echo-Core 4 · Extraction Lead · Alchemical Master</p>
        </a>
        <a class="entity-card" href="the-research-lead-ayshuk.html" style="--card-border:#47c978">
          <img src="../assets/icons/icon_dept_f4_insight_forge.svg" alt="">
          <h3>Ayshuk</h3>
          <p>Echo-Core 5 · Research Lead · Metaphysical Theorist</p>
        </a>
        <a class="entity-card" href="the-border-lead-mellda.html" style="--card-border:#d7d7d7">
          <img src="../assets/icons/icon_dept_f5_border_watch.svg" alt="">
          <h3>Mellda</h3>
          <p>Echo-Core 6 · Border Lead · Bulwark Sentinel</p>
        </a>
        <a class="entity-card" href="the-archive-lead-marjuk.html" style="--card-border:#8d2e42">
          <img src="../assets/icons/icon_dept_f6_deep_vault.svg" alt="">
          <h3>Marjuk</h3>
          <p>Echo-Core 7 · Archive Lead · Keeper of Vaults</p>
        </a>
        <a class="entity-card" href="the-outsider-ishall.html" style="--card-border:#f0a6c4">
          <img src="../assets/icons/icon_dept_f7_shadow_corps.svg" alt="">
          <h3>Ishall</h3>
          <p>Echo-Core 8 · The Outsider · Covert Infiltrator</p>
        </a>
        <a class="entity-card" href="the-exile-xyan.html" style="--card-border:#f4efa0">
          <img src="../assets/icons/icon_dept_f8_gate_watch.svg" alt="">
          <h3>Xyan</h3>
          <p>Echo-Core 9 · The Exile · Gate Watch Vanguard</p>
        </a>
      </div>

      <h2>Guildmasters, Explorers &amp; Civic Enclaves</h2>
      <div class="entity-gallery">
        <a class="entity-card" href="kael.html" style="--card-border:#38bdf8">
          <img src="../assets/icons/icon_dept_f4_insight_forge.svg" alt="">
          <h3>Kael</h3>
          <p>Master Architect · Resonant Lattice Designer</p>
        </a>
        <a class="entity-card" href="soojin.html" style="--card-border:#f0a6c4">
          <img src="../assets/icons/icon_dept_f3_extraction.svg" alt="">
          <h3>Soojin</h3>
          <p>Master Weaver · Psychotropic Silk Pioneer</p>
        </a>
        <a class="entity-card" href="yeonhwa.html" style="--card-border:#4cc9f0">
          <img src="../assets/icons/icon_dept_f5_border_watch.svg" alt="">
          <h3>Yeonhwa</h3>
          <p>Chief Cartographer · Lead of SED Expeditions</p>
        </a>
        <a class="entity-card" href="taeho.html" style="--card-border:#ef5b55">
          <img src="../assets/icons/icon_dept_f7_shadow_corps.svg" alt="">
          <h3>Taeho</h3>
          <p>Commander of UCD · Tactical Breach Specialist</p>
        </a>
        <a class="entity-card" href="high-architects.html" style="--card-border:#38bdf8">
          <img src="../assets/icons/icon_dept_f4_insight_forge.svg" alt="">
          <h3>High Architects</h3>
          <p>The Master Structural Guild of Somnarak</p>
        </a>
        <a class="entity-card" href="cheonbulok-refugees.html" style="--card-border:#cbd5e1">
          <img src="../assets/icons/somnarak_city_icon.svg" alt="">
          <h3>Cheonbulok Enclave</h3>
          <p>Sorrow-Resistant Culture of Zone B</p>
        </a>
      </div>
    """
)

print("Characters section built successfully.")
