import os
from generate_wiki_content import write_page

print("Building Departments Section...")

# 1. Floor 1: Neutral Command
write_page(
    folder="departments",
    filename="floor-1-neutral-command.html",
    title="Floor 1 — Neutral Command (중립 사령부)",
    subtitle="The Apex Control Bridge · Lead Majin &amp; Seiyon · Central Nexus of the Hand of Change",
    color="#ef5b55",
    icon_svg="icon_dept_f1_neutral.svg",
    meta_cards=[
        ("Floor Designation", "Floor 1 (Apex / The Palm)"),
        ("Floor Color Theme", "Crimson &amp; Gold (#ef5b55)"),
        ("Department Lead", "Director Majin (Echo-Core 1)"),
        ("Chief Administrator", "Seiyon (Echo-Core 2)"),
        ("Key Installations", "Station A Core Chamber, Global Telemetry Bridge, Alpha Sap Throttle"),
        ("Floor Function", "Executive Facility Command &amp; Energy Grid Balancing")
    ],
    article_body="""
      <h2>Department Overview</h2>
      <p><b>Floor 1: Neutral Command</b> is the apex operational bridge and supreme nerve center of the Hand of Change. Positioned directly at the biological base of the Alpha Tree (Station A), Neutral Command oversees real-time telemetry from all eight subterranean floors, coordinates containment breach protocols, and regulates the flow of refined Alpha Sap to Somnarak's civic grid.</p>

      <h2>Floor Architecture &amp; Key Chambers</h2>
      <ul>
        <li><b>The Sovereign Bridge:</b> The circular command dais where Director Majin and Seiyon review real-time containment statistics and issue facility-wide orders.</li>
        <li><b>Station A (The Tree Core):</b> The hermetically sealed chamber where the colossal heartwood of the Alpha Tree intersects with the facility's primary sap intake manifold.</li>
        <li><b>The Executive Communications Array:</b> High-frequency psychotropic transmitters connecting the Directorate directly to the High Council and outer garrison outposts.</li>
      </ul>

      <h2>Department Mechanics &amp; Passives</h2>
      <p>When operating on Floor 1, staff benefit from <b>Zero-Point Stabilization</b>, reducing the passive SP drain caused by high-tier entity containment by 30% and providing immediate emergency lockdowns during containment breaches.</p>
    """
)

# 2. Floor 2: The Maw's Keep
write_page(
    folder="departments",
    filename="floor-2-maws-keep.html",
    title="Floor 2 — The Maw’s Keep (심연의 보루)",
    subtitle="Heavy Containment &amp; Frontline Vanguard · Lead Dekan · The Iron Citadel",
    color="#6f7ee8",
    icon_svg="icon_dept_f2_maws_keep.svg",
    meta_cards=[
        ("Floor Designation", "Floor 2 (Upper Hand / The Palm)"),
        ("Floor Color Theme", "Heavy Blue &amp; Slate (#6f7ee8)"),
        ("Department Lead", "Dekan (Echo-Core 3 / The Iron Sentry)"),
        ("Specialization", "High-Risk Containment, Physical Suppression, Blast Isolation"),
        ("Key Entities Housed", "SE-002 (The Grieving Colossus), SE-005 (The Smothering Mother)"),
        ("Security Rating", "Maximum Heavy Armor / Class IV Reinforced")
    ],
    article_body="""
      <h2>Department Overview</h2>
      <p><b>Floor 2: The Maw's Keep</b> is the heavily armored containment wing of the facility, engineered specifically to restrain massive, high-kinetic physical entities. Under the command of Echo-Core 3 Dekan, Floor 2 acts as the facility's unbreakable shield, housing entities whose physical strength or structural destruction capabilities would obliterate standard research facilities.</p>

      <h2>Containment Infrastructure</h2>
      <ul>
        <li><b>The Titan Vaults:</b> Reinforced cells lined with multi-layered mourning steel plates and hydraulic dampening pistons.</li>
        <li><b>The Heavy Armory:</b> Storage facility for high-caliber M.A.W. mauls, suppression shields, and kinetic shock-cannons.</li>
        <li><b>Bulkhead Quarantine Rings:</b> Segmented blast gates capable of sealing breached corridors within 1.2 seconds of Qliphoth collapse.</li>
      </ul>
    """
)

# 3. Floor 3: Extraction Hall
write_page(
    folder="departments",
    filename="floor-3-extraction-hall.html",
    title="Floor 3 — Extraction Hall (추출관)",
    subtitle="Alchemical Forges &amp; Sap Crystallization · Lead Zyrak · The Birthplace of M.A.W.",
    color="#e6c94d",
    icon_svg="icon_dept_f3_extraction.svg",
    meta_cards=[
        ("Floor Designation", "Floor 3 (Base of Palm)"),
        ("Floor Color Theme", "Amber &amp; Gold (#e6c94d)"),
        ("Department Lead", "Zyrak (Echo-Core 4 / Alchemical Lead)"),
        ("Specialization", "Han Crystallization, M.A.W. Forging, Sap Distillation"),
        ("Key Equipment Forged", "M.A.W. Weapons (Weapons, Suits, Resonant Gifts)"),
        ("Environmental State", "High Vapor Pressure / Aromatic Sap Distillation")
    ],
    article_body="""
      <h2>Department Overview</h2>
      <p><b>Floor 3: Extraction Hall</b> is the industrial and alchemical workshop of the Hand of Change. Directed by the meticulous alchemist Zyrak, this department extracts emotional Han from pacified entities, condenses it in pressurized catalytic vats, and weaves it into wearable M.A.W. combat equipment.</p>

      <h2>Key Facilities</h2>
      <ul>
        <li><b>The Catharsis Crucible:</b> The central forging vat where crystallized Alpha Sap is blended with raw emotional sorrow to cast weapon cores.</li>
        <li><b>The Weaving Lofts:</b> Secondary workshops operated in conjunction with the Weavers Guild to stitch psychotropic linings into combat suits.</li>
      </ul>
    """
)

# 4. Floor 4: Insight Forge
write_page(
    folder="departments",
    filename="floor-4-insight-forge.html",
    title="Floor 4 — Insight Forge (통찰의 대장간)",
    subtitle="Theoretical Metaphysics &amp; Therapy Labs · Lead Ayshuk · The Mind of the Facility",
    color="#47c978",
    icon_svg="icon_dept_f4_insight_forge.svg",
    meta_cards=[
        ("Floor Designation", "Floor 4 (First Finger)"),
        ("Floor Color Theme", "Emerald &amp; Mint (#47c978)"),
        ("Department Lead", "Ayshuk (Echo-Core 5 / Research Lead)"),
        ("Specialization", "Han Metaphysics, Entity Psychology, Neural Stabilization"),
        ("Key Installations", "The Resonant Observatories, SP Therapy Baths, Dream Pods"),
        ("Academic Output", "The Tri-Partite Matrix, Work Optimization Ratios")
    ],
    article_body="""
      <h2>Department Overview</h2>
      <p><b>Floor 4: Insight Forge</b> is the intellectual and psychiatric sanctuary of the facility. Under the leadership of Ayshuk, researchers study the emotional physics of Han, formulate containment formulas, and provide psychological therapy to staff recovering from mental fracture.</p>

      <h2>Key Facilities</h2>
      <ul>
        <li><b>The Neural Stabilization Baths:</b> Heated Alpha Sap pools that soothe traumatized minds and restore drained SP.</li>
        <li><b>The Resonant Observatories:</b> High-magnification optical laboratories studying the atomic crystallization of grief.</li>
      </ul>
    """
)

# 5. Floor 5: Border Watch
write_page(
    folder="departments",
    filename="floor-5-border-watch.html",
    title="Floor 5 — Border Watch (경계 감시단)",
    subtitle="Spatial Barrier Network &amp; Zone Defense · Lead Mellda · The Outer Shield",
    color="#d7d7d7",
    icon_svg="icon_dept_f5_border_watch.svg",
    meta_cards=[
        ("Floor Designation", "Floor 5 (Second Finger)"),
        ("Floor Color Theme", "Silver &amp; White (#d7d7d7)"),
        ("Department Lead", "Mellda (Echo-Core 6 / Border Lead)"),
        ("Specialization", "Spatial Anchoring, Perimeter Telemetry, Artillery Coordination"),
        ("Direct Integration", "Zone E Titan Wall &amp; Outer Defense Batteries"),
        ("Strategic Mandate", "Preventing Waste Miasma Infiltration &amp; Wasteland Swarms")
    ],
    article_body="""
      <h2>Department Overview</h2>
      <p><b>Floor 5: Border Watch</b> operates the subterranean spatial barrier generators that power the defensive shields of Somnarak’s outer walls. Commanded by Lead Mellda, this department coordinates defense telemetry between the Hand of Change and the Zone E Bulwark.</p>
    """
)

# 6. Floor 6: Deep Vault
write_page(
    folder="departments",
    filename="floor-6-deep-vault.html",
    title="Floor 6 — Deep Vault (심층 보관소)",
    subtitle="Cryo-Memory Cylinders &amp; Taboo Archives · Lead Marjuk · The Memory of Time",
    color="#8d2e42",
    icon_svg="icon_dept_f6_deep_vault.svg",
    meta_cards=[
        ("Floor Designation", "Floor 6 (Third Finger)"),
        ("Floor Color Theme", "Crimson-Wine &amp; Black (#8d2e42)"),
        ("Department Lead", "Marjuk (Echo-Core 7 / Archive Lead)"),
        ("Specialization", "Temporal Memory Storage, Taboo Quarantine, Cycle Records"),
        ("Operating Temperature", "-20°C Cryo-Resonant Preservation"),
        ("Stored Assets", "100,000+ Memory Cylinders of the 1,778 Cycles")
    ],
    article_body="""
      <h2>Department Overview</h2>
      <p><b>Floor 6: Deep Vault</b> is a sub-zero subterranean archival crypt where the un-erased records of Somnarak's history, prohibited taboos, and forgotten timelines are permanently preserved by Echo-Core 7 Marjuk.</p>
    """
)

# 7. Floor 7: Shadow Corps
write_page(
    folder="departments",
    filename="floor-7-shadow-corps.html",
    title="Floor 7 — Shadow Corps (그림자 분대)",
    subtitle="Covert Reconnaissance &amp; Underworld Ingress · Lead Ishall · The Hidden Hand",
    color="#f0a6c4",
    icon_svg="icon_dept_f7_shadow_corps.svg",
    meta_cards=[
        ("Floor Designation", "Floor 7 (Fourth Finger)"),
        ("Floor Color Theme", "Rose &amp; Shadow (#f0a6c4)"),
        ("Department Lead", "Ishall (Echo-Core 8 / The Outsider)"),
        ("Specialization", "Covert Infiltration, Dream Diving, Black Market Seizure"),
        ("Access Routes", "Subterranean Ducts to Zone C &amp; The Underworld"),
        ("Tactical Role", "Rogue Entity Recovery &amp; Taboo Interception")
    ],
    article_body="""
      <h2>Department Overview</h2>
      <p><b>Floor 7: Shadow Corps</b> is the Directorate’s covert operations hub. Led by Ishall, Shadow Corps operatives specialize in stealth, psychological reconnaissance, and operations in the lawless underbelly of Somnarak.</p>
    """
)

# 8. Floor 8: Gate Watch
write_page(
    folder="departments",
    filename="floor-8-gate-watch.html",
    title="Floor 8 — Gate Watch (문지기 초소)",
    subtitle="The Abyssal Threshold Garrison · Lead Xyan · The Final Sentinel of the Maw",
    color="#f4efa0",
    icon_svg="icon_dept_f8_gate_watch.svg",
    meta_cards=[
        ("Floor Designation", "Floor 8 (Wing / The Deepest Gate)"),
        ("Floor Color Theme", "Pale Gold &amp; Void (#f4efa0)"),
        ("Department Lead", "Xyan (Echo-Core 9 / The Exile)"),
        ("Specialization", "Maw Gateway Defense, Calamity Interception, Final Line"),
        ("Direct Boundary", "The Subterranean Abyssal Maw &amp; River Weeping"),
        ("Emergency Duty", "Detonation of Basal Bulkheads in Absolute Collapse")
    ],
    article_body="""
      <h2>Department Overview</h2>
      <p><b>Floor 8: Gate Watch</b> is the lowest and most perilous department in the Hand of Change. Located at the direct threshold of the Abyssal Maw, Commander Xyan and his sentries stand vigil over the gateway to ensure that the primordial horrors of the deep never rise into the upper city.</p>
    """
)

# 9. Departments Hub (index.html)
write_page(
    folder="departments",
    filename="index.html",
    title="Hand of Change Departments Hub",
    subtitle="The Eight Operational Floors of Somnarak's Subterranean Containment Complex",
    color="#f1df76",
    icon_svg="the_hand_dr_icon_styled.svg",
    meta_cards=[
        ("Facility Designation", "The Hand of Change (변화의 손)"),
        ("Total Operational Floors", "8 Specialized Departments"),
        ("Structural Form", "The Palm (Floors 1-3) &amp; The Fingers (Floors 4-8)"),
        ("Command Authority", "Director Majin &amp; Seiyon"),
        ("Active Era", "Year 4,238 · Dawn Initiative")
    ],
    article_body="""
      <h2>The Anatomy of the Hand of Change</h2>
      <p>The <b>Hand of Change</b> is the colossal eight-floor subterranean complex that stabilizes, harvests, and defends Somnarak. Structured conceptually as a human hand, the facility is divided into <b>The Palm</b> (Floors 1 to 3) and <b>The Fingers &amp; Wing</b> (Floors 4 to 8).</p>

      <h2>The Palm (Core Operations)</h2>
      <div class="entity-gallery">
        <a class="entity-card" href="floor-1-neutral-command.html" style="--card-border:#ef5b55">
          <img src="../assets/icons/icon_dept_f1_neutral.svg" alt="">
          <h3>Floor 1: Neutral Command</h3>
          <p>Lead: Majin &amp; Seiyon · Apex Command Bridge</p>
        </a>
        <a class="entity-card" href="floor-2-maws-keep.html" style="--card-border:#6f7ee8">
          <img src="../assets/icons/icon_dept_f2_maws_keep.svg" alt="">
          <h3>Floor 2: Maw’s Keep</h3>
          <p>Lead: Dekan · Heavy Containment Citadel</p>
        </a>
        <a class="entity-card" href="floor-3-extraction-hall.html" style="--card-border:#e6c94d">
          <img src="../assets/icons/icon_dept_f3_extraction.svg" alt="">
          <h3>Floor 3: Extraction Hall</h3>
          <p>Lead: Zyrak · M.A.W. Forges &amp; Alchemical Vats</p>
        </a>
      </div>

      <h2>The Fingers &amp; Wing (Specialized Wings)</h2>
      <div class="entity-gallery">
        <a class="entity-card" href="floor-4-insight-forge.html" style="--card-border:#47c978">
          <img src="../assets/icons/icon_dept_f4_insight_forge.svg" alt="">
          <h3>Floor 4: Insight Forge</h3>
          <p>Lead: Ayshuk · Metaphysics &amp; Therapy</p>
        </a>
        <a class="entity-card" href="floor-5-border-watch.html" style="--card-border:#d7d7d7">
          <img src="../assets/icons/icon_dept_f5_border_watch.svg" alt="">
          <h3>Floor 5: Border Watch</h3>
          <p>Lead: Mellda · Spatial Shields &amp; Wall Links</p>
        </a>
        <a class="entity-card" href="floor-6-deep-vault.html" style="--card-border:#8d2e42">
          <img src="../assets/icons/icon_dept_f6_deep_vault.svg" alt="">
          <h3>Floor 6: Deep Vault</h3>
          <p>Lead: Marjuk · Cryo-Memory Archives</p>
        </a>
        <a class="entity-card" href="floor-7-shadow-corps.html" style="--card-border:#f0a6c4">
          <img src="../assets/icons/icon_dept_f7_shadow_corps.svg" alt="">
          <h3>Floor 7: Shadow Corps</h3>
          <p>Lead: Ishall · Covert Infiltration</p>
        </a>
        <a class="entity-card" href="floor-8-gate-watch.html" style="--card-border:#f4efa0">
          <img src="../assets/icons/icon_dept_f8_gate_watch.svg" alt="">
          <h3>Floor 8: Gate Watch</h3>
          <p>Lead: Xyan · Maw Gateway Defense</p>
        </a>
      </div>
    """
)

print("Departments section built successfully.")
