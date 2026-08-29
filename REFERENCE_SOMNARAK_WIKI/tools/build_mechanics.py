import os
from generate_wiki_content import write_page

print("Building Mechanics Section...")

# 1. Han Energy & Damage
write_page(
    folder="mechanics",
    filename="han-energy-and-damage.html",
    title="Han Energy &amp; Damage Types",
    subtitle="The 5-Type Damage Taxonomy · Elemental Resistances, Clash Multipliers, and Formula Matrices",
    color="#ef5b55",
    icon_svg="icon_dept_f4_insight_forge.svg",
    meta_cards=[
        ("System Type", "Tactical Combat &amp; Containment Math Engine"),
        ("Primary Damage Types", "Red (Grudge), Blue (Lament), Black (Weight)"),
        ("Advanced Damage Types", "Purple (Fracture), Pale (Absolute Verdict)"),
        ("Core Formula", "Effective Damage = Base Power × Resistance Multiplier"),
        ("Metaphysical Substrate", "Emotional Resonance Equilibrium")
    ],
    article_body="""
      <h2>Damage Type Taxonomy &amp; Elemental Properties</h2>
      <p>Combat and containment interactions in Somnarak operate on five distinct damage types, each representing a specific thermodynamic and psychological property of Han energy. The efficacy of an attack is determined by comparing the attack's damage type against the target's armor resistance coefficients.</p>

      <table class="data-table">
        <thead>
          <tr>
            <th>Damage Type</th>
            <th>Primary Aspect</th>
            <th>Target Metric</th>
            <th>Combat Behavior &amp; Effect</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><b style="color:#ef5b55">Red (Grudge / 원망)</b></td>
            <td>Physical Trauma</td>
            <td>HP (Health Points)</td>
            <td>Slashes flesh, fractures bone, and degrades mechanical armor. Deals pure physical damage.</td>
          </tr>
          <tr>
            <td><b style="color:#38bdf8">Blue (Lament / 비탄)</b></td>
            <td>Mental / Sanity</td>
            <td>SP (Sanity Points)</td>
            <td>Chills the mind, induces despair, and drains SP. When SP hits -45, targets trigger Panic states.</td>
          </tr>
          <tr>
            <td><b style="color:#a855f7">Black (Weight / 비중)</b></td>
            <td>Gravitational / Hybrid</td>
            <td>Both HP and SP</td>
            <td>Crushes physical frames while simultaneously exerting massive psychological pressure.</td>
          </tr>
          <tr>
            <td><b style="color:#c084fc">Purple (Fracture / 균열)</b></td>
            <td>Chaotic Collision</td>
            <td>HP and SP (Fluctuating)</td>
            <td>Bypasses 50% of target armor resistance; inflicts erratic random damage spikes.</td>
          </tr>
          <tr>
            <td><b style="color:#f8fafc">Pale (Verdict / 창백)</b></td>
            <td>Existential Extinction</td>
            <td>% Max HP (True Damage)</td>
            <td>Deals damage as a flat percentage of the target's total maximum health. Ignores standard armor.</td>
          </tr>
        </tbody>
      </table>

      <h2>Armor Resistance Multiplier Chart</h2>
      <p>Armor in Somnarak classifies resistance across five standard grades: <b>Fatal (2.0x)</b>, <b>Weak (1.5x)</b>, <b>Normal (1.0x)</b>, <b>Endure (0.5x)</b>, and <b>Immune (0.0x)</b>.</p>
    """
)

# 2. M.A.W. Equipment System
write_page(
    folder="mechanics",
    filename="maw-equipment-system.html",
    title="M.A.W. Equipment &amp; Resonance System",
    subtitle="Maw-Extracted Armaments · Weaponry, Resonant Suits, Gifts, and Tier Mechanics",
    color="#e6c94d",
    icon_svg="icon_dept_f3_extraction.svg",
    meta_cards=[
        ("Equipment Classification", "M.A.W. (Memory Alchemical Weaponry)"),
        ("Equipment Slots", "Weapon (공격), Suit (방어), Resonant Gift (장신구)"),
        ("Resonance Ranks", "Rank I (ZAYIN) to Rank V (ALEPH)"),
        ("Harvesting Facility", "Floor 3: Extraction Hall"),
        ("Wearer Requirement", "Minimum SP Threshold &amp; Psychological Calibration")
    ],
    article_body="""
      <h2>System Architecture</h2>
      <p><b>M.A.W.</b> (Memory Alchemical Weaponry / 마우 장비) represents the pinnacle of Somnarak combat technology. Extracted directly from subdued Sorrow Entities on Floor 3, M.A.W. equipment allows human operatives to channel the supernatural powers of entities without succumbing to their corruptive influence.</p>

      <h2>Equipment Categories</h2>
      <ul>
        <li><b>M.A.W. Weapons (무기):</b> Specialized melee armaments, firearms, and resonant lenses that deal elemental Han damage (Red, Blue, Black, Pale).</li>
        <li><b>M.A.W. Suits (방어구):</b> Psychotropic silk coats and reinforced plate armor crafted by the Weavers Guild, granting customized resistance profiles against specific damage types.</li>
        <li><b>M.A.W. Gifts (기프트):</b> Minor crystallized relics formed during successful containment operations, granting passive stat boosts and unique status effects.</li>
      </ul>

      <h2>Resonance Penalty &amp; Ego Erosion</h2>
      <p>Equipping high-tier M.A.W. gear (Rank IV or Rank V) on an operative with insufficient mental fortitude causes <i>Ego Erosion</i>, draining SP at the start of every combat turn and increasing the risk of spontaneous entity takeover.</p>
    """
)

# 3. Containment & Suppression
write_page(
    folder="mechanics",
    filename="containment-and-suppression.html",
    title="Containment &amp; Suppression Protocols",
    subtitle="The Four Work Types · Qliphoth / Sorrow Counters, Breach Triggers, and Tactical Subdual",
    color="#6f7ee8",
    icon_svg="icon_dept_f2_maws_keep.svg",
    meta_cards=[
        ("Core Operations", "Insight, Instinct, Attachment, Repression"),
        ("Hazard Metric", "Sorrow Counter / Qliphoth Counter"),
        ("Breach State", "Active Facility Incursion (Code Crimson)"),
        ("Suppression Units", "Floor 2 Vanguard &amp; Floor 5 Border Watch"),
        ("Success Metric", "Alpha Sap Yield &amp; Zero Casualty Rate")
    ],
    article_body="""
      <h2>The Four Standard Work Protocols</h2>
      <p>Every containment cell within the Hand of Change requires precise daily interaction to keep entities pacified and extract Alpha Sap. Operatives must select the work type best suited to the entity's psychological profile:</p>

      <table class="data-table">
        <thead>
          <tr>
            <th>Work Type</th>
            <th>Primary Objective</th>
            <th>Optimal For</th>
            <th>Failure Risk</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><b>Insight (통찰)</b></td>
            <td>Environmental adjustment, philosophical dialogue, structural cleaning</td>
            <td>Philosophical &amp; Abstract Entities</td>
            <td>High SP drain if entity rejects logic</td>
          </tr>
          <tr>
            <td><b>Instinct (본능)</b></td>
            <td>Biological feeding, physical comfort, thermal regulation</td>
            <td>Bestial &amp; Organic Entities</td>
            <td>Severe Red physical trauma on bad result</td>
          </tr>
          <tr>
            <td><b>Attachment (애착)</b></td>
            <td>Emotional listening, therapeutic bonding, shared mourning</td>
            <td>Sentient &amp; Tragic Entities</td>
            <td>Risk of psycho-symbiosis or possession</td>
          </tr>
          <tr>
            <td><b>Repression (억압)</b></td>
            <td>Resonant shock suppression, physical restraining, sensory deprivation</td>
            <td>Aggressive &amp; Predatory Entities</td>
            <td>Rapid decrease of Sorrow Counter</td>
          </tr>
        </tbody>
      </table>

      <h2>The Sorrow Counter &amp; Breach Cascade</h2>
      <p>Each entity possesses a <b>Sorrow Counter</b> (1 to 5). When an operative achieves a Bad Work outcome or an Ordeal strikes the facility, the counter drops. When it reaches 0, the cell containment lattice shatters, initiating an emergency breach requiring tactical suppression.</p>
    """
)

# 4. Fracture & Therapy
write_page(
    folder="mechanics",
    filename="fracture-and-therapy.html",
    title="Fracture &amp; Psychological Therapy",
    subtitle="Sanity Points (SP) · Panic States, Ego Breakdown, and Floor 4 Recovery Pods",
    color="#8d2e42",
    icon_svg="icon_dept_f4_insight_forge.svg",
    meta_cards=[
        ("Mental Health Metric", "SP (Sanity Points: -45 to +45)"),
        ("Panic Manifestations", "Berserk, Hysteria, Catatonia, Wandering"),
        ("Recovery Facility", "Floor 4 Insight Forge Neural Stabilization Baths"),
        ("Therapeutic Treatment", "Memory Anchoring &amp; Psychotropic Sedation"),
        ("Permanent Hazard", "Complete Soul Calcification / Entity Transmutation")
    ],
    article_body="""
      <h2>The Mechanics of Mental Collapse</h2>
      <p>In the high-stress environment of the Hand of Change, an operative’s mind is under constant psychic bombardment. Mental endurance is tracked via <b>Sanity Points (SP)</b>, fluctuating between -45 (Total Panic) and +45 (Perfect Euphoria/Focus).</p>

      <h2>The Four Canonical Panic States</h2>
      <table class="data-table">
        <thead>
          <tr>
            <th>Panic State</th>
            <th>Behavioral Profile</th>
            <th>Tactical Threat</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><b>Berserk (폭주)</b></td>
            <td>The operative enters an uncontrollable homicidal rage, attacking the nearest ally with M.A.W. weaponry.</td>
            <td>High friendly-fire lethality. Must be subdued with Blue damage.</td>
          </tr>
          <tr>
            <td><b>Hysteria (패닉)</b></td>
            <td>The operative screams incoherently, running randomly through corridors and lowering adjacent allies' SP.</td>
            <td>Can trigger a cascade panic across entire floors.</td>
          </tr>
          <tr>
            <td><b>Catatonia (혼수)</b></td>
            <td>The operative collapses into a motionless vegetative stupor, completely defenseless.</td>
            <td>Easy target for roaming breached entities.</td>
          </tr>
          <tr>
            <td><b>Wandering (방황)</b></td>
            <td>The operative mindlessly opens containment cell doors, triggering simultaneous facility breaches.</td>
            <td>Extreme emergency hazard. Requires immediate sedation.</td>
          </tr>
        </tbody>
      </table>
    """
)

# 5. Ordeals Framework
write_page(
    folder="mechanics",
    filename="ordeals-framework.html",
    title="The Ordeals Framework (시련 시스템)",
    subtitle="Time-Based Facility Incursions · Dawn, Noon, Dusk, and Midnight Calamities",
    color="#e8a317",
    icon_svg="the_hand_dr_icon_styled.svg",
    meta_cards=[
        ("System Type", "Dynamic Facility-Wide Emergency Event"),
        ("Ordeal Tiers", "Dawn (새벽), Noon (정오), Dusk (황혼), Midnight (자정)"),
        ("Elemental Spectrum", "Red (Claw), Blue (Circus), Green (Machine), Amber (Worm), Violet (Monolith)"),
        ("Trigger Condition", "Work Quota Thresholds per Working Day"),
        ("Reward", "Massive Alpha Sap Boost &amp; Floor Morale Restored")
    ],
    article_body="""
      <h2>Nature of the Ordeals</h2>
      <p><b>Ordeals</b> (시련, <i>Siryeon</i>) are spontaneous metaphysical incursions caused by the accumulation of excess emotional resonance within the Hand of Change. As extraction progresses throughout the day, the pressure causes spatial ruptures that spawn hostile apparitions across random corridors.</p>

      <h2>Ordeal Time Tiers</h2>
      <ul>
        <li><b>Dawn (새벽):</b> Minor apparitions that test basic frontline coordination. Easy to subdue with standard Warden units.</li>
        <li><b>Noon (정오):</b> Armored constructs and burrowing worms that actively disrupt ongoing containment work.</li>
        <li><b>Dusk (황혼):</b> Colossal monoliths and roving circus horrors that lower floor-wide Sorrow Counters upon entering corridors.</li>
        <li><b>Midnight (자정):</b> Facility-threatening singularities capable of slaughtering entire departments if not neutralized immediately.</li>
      </ul>
    """
)

# 6. Resonant Clash Mechanics
write_page(
    folder="mechanics",
    filename="resonant-clash-mechanics.html",
    title="Resonant Clash &amp; Stagger Break Systems",
    subtitle="Attack Speed, Clash Power Calculation, Emotional Multipliers, and Posture Shatter",
    color="#38bdf8",
    icon_svg="icon_dept_f2_maws_keep.svg",
    meta_cards=[
        ("Combat Phase", "Simultaneous Action Resolution (Clash)"),
        ("Key Attributes", "Speed Dice, Attack Power, Coin Toss / Dice Rolls"),
        ("Critical Mechanic", "Stagger Break (자세 붕괴 — 2.0x Damage Vulnerability)"),
        ("Clash Win Reward", "Direct Hit + SP Gain (+10 SP)"),
        ("Clash Loss Penalty", "Complete Action Cancellation + Stagger Damage")
    ],
    article_body="""
      <h2>The Resonant Clash</h2>
      <p>When an operative and a hostile entity target each other simultaneously, a <b>Resonant Clash (합, <i>Hap</i>)</b> occurs. Both combatants roll their respective attack dice, modified by their emotional frequency and SP level. The combatant with the higher final power roll wins the clash, nullifying the opponent's attack and delivering a direct strike.</p>

      <h2>Stagger Break (자세 붕괴)</h2>
      <p>Every combatant possesses a Stagger Threshold. Taking heavy kinetic or Black damage reduces this posture bar. When broken:</p>
      <ul>
        <li>All actions for the turn are cancelled.</li>
        <li>Target's defense resistances are temporarily set to <b>Fatal (2.0x)</b> across all damage types.</li>
        <li>Target is unable to clash or evade during the subsequent turn.</li>
      </ul>
    """
)

# 7. Mechanics Hub (index.html)
write_page(
    folder="mechanics",
    filename="index.html",
    title="Battle, Containment &amp; Game Systems Hub",
    subtitle="Comprehensive Mathematical, Tactical, and Operational Rulebooks of Somnarak",
    color="#f1df76",
    icon_svg="the_hand_dr_icon_styled.svg",
    meta_cards=[
        ("Indexed System Guides", "6 Comprehensive Rulebooks"),
        ("Target Disciplines", "Tactical Combat, Facility Containment, Mental Health"),
        ("System Fidelity", "Full Mathematical &amp; Formulaic Models"),
        ("Authority", "Reverie Directorate Operational Handbook")
    ],
    article_body="""
      <h2>System Mechanics Directories</h2>
      <p>Master the mathematical, tactical, and containment rules governing the world of Somnarak and the Hand of Change.</p>

      <div class="entity-gallery">
        <a class="entity-card" href="han-energy-and-damage.html" style="--card-border:#ef5b55">
          <img src="../assets/icons/icon_dept_f4_insight_forge.svg" alt="">
          <h3>Han &amp; Damage Types</h3>
          <p>Red, Blue, Black, Purple &amp; Pale Taxonomy</p>
        </a>
        <a class="entity-card" href="maw-equipment-system.html" style="--card-border:#e6c94d">
          <img src="../assets/icons/icon_dept_f3_extraction.svg" alt="">
          <h3>M.A.W. Codex System</h3>
          <p>Weapons, Suits, Gifts &amp; Resonance Tiers</p>
        </a>
        <a class="entity-card" href="containment-and-suppression.html" style="--card-border:#6f7ee8">
          <img src="../assets/icons/icon_dept_f2_maws_keep.svg" alt="">
          <h3>Containment Protocols</h3>
          <p>Insight, Instinct, Attachment &amp; Repression</p>
        </a>
        <a class="entity-card" href="fracture-and-therapy.html" style="--card-border:#8d2e42">
          <img src="../assets/icons/icon_dept_f4_insight_forge.svg" alt="">
          <h3>Fracture &amp; Therapy</h3>
          <p>SP Loss, Panic Behaviors &amp; Neural Baths</p>
        </a>
        <a class="entity-card" href="ordeals-framework.html" style="--card-border:#e8a317">
          <img src="../assets/icons/the_hand_dr_icon_styled.svg" alt="">
          <h3>The Ordeals Framework</h3>
          <p>Dawn to Midnight Incursions &amp; Apparitions</p>
        </a>
        <a class="entity-card" href="resonant-clash-mechanics.html" style="--card-border:#38bdf8">
          <img src="../assets/icons/icon_dept_f2_maws_keep.svg" alt="">
          <h3>Clash &amp; Stagger Break</h3>
          <p>Dice Formulas, Clash Resolution &amp; Posture</p>
        </a>
      </div>
    """
)

print("Mechanics section built successfully.")
