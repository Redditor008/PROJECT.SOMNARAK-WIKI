import os
import re

MECH_DIR = "/home/user/01_Somnarak_Wiki/mechanics"
os.makedirs(MECH_DIR, exist_ok=True)

from generate_all_characters import get_left_rail, get_floor_rail, get_header, get_footer

def build_mechanics_pages():
    # 1. han-energy-and-damage.html
    energy_html = f"""<!doctype html><html lang="en" data-article-status="curated"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Han Energy &amp; Damage Types — Somnarak Wiki</title><meta name="description" content="Technical framework of Han energy, elemental damage formulas, resistance multipliers, and tactical counters"><link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg"><link rel="stylesheet" href="../assets/css/wiki.css"><script defer src="../assets/js/wiki.js"></script></head><body>
{get_header()}
<nav class="float-toc" aria-label="On this page"><button type="button" aria-expanded="false">CONTENTS</button><div><strong>ON THIS PAGE</strong><ol><li class="l2"><a href="#overview">Overview</a></li><li class="l2"><a href="#elemental-mechanics">Elemental Mechanics</a></li><li class="l2"><a href="#the-four-primary-damage-types">The Four Primary Damage Types</a></li><li class="l2"><a href="#the-fifth-resonance-hope">The Fifth Resonance: Hope (Gold)</a></li><li class="l2"><a href="#resistance-and-multiplier-matrix">Resistance &amp; Multiplier Matrix</a></li><li class="l2"><a href="#combat-clash-mechanics">Combat Clash Mechanics</a></li></ol><a href="#content">↑ TOP</a></div></nav>
<div class="wiki-shell">
{get_left_rail()}
<main id="content"><div class="page-tabs"><span>Mechanics &amp; Systems</span><b>DAMAGE &amp; COMBAT PHYSICS</b></div><div class="breadcrumbs"><a href="../index.html">Main page</a><i>›</i><a href="index.html">Mechanics</a><i>›</i>Han Energy &amp; Damage</div>
<section class="department-hero" style="--floor:#ef5b55"><img src="../assets/icons/banner_mechanics.svg" alt=""><div><span>COMBAT FRAMEWORK · TACTICAL PHYSICS</span><h1>Han Energy &amp; Damage Types</h1><p>한 에너지와 피해 유형 — Han Eneoji-gwa Pihae Yuheong</p></div></section>
<blockquote class="motto" style="--floor:#ef5b55">“In standard warfare, armor repels steel. In Somnarak, armor must repel the grief behind the blow. If your resonance fails, your chest does not crack—your soul does.” — Tactical Training Manual</blockquote>
<section class="department-overview"><div><h2 id="overview">Overview</h2><p class="lead">Combat in the world of Somnarak is governed by the physical laws of <strong>Han Energy</strong>. Unlike kinetic kinetic trauma alone, attacks delivered by Sorrow Entities, M.A.W. weapons, and resonant artifacts inflict damage across four distinct emotional wavelengths: <strong>Lament</strong>, <strong>Grudge</strong>, <strong>Weight</strong>, and <strong>Void</strong>, supplemented by the restorative fifth resonance, <strong>Hope</strong>.</p><p>Understanding damage affinities, resistance multipliers, and the three phases of combat tension is essential for surviving suppression missions.</p></div><aside class="department-profile" style="--floor:#ef5b55"><h2 id="elemental-mechanics">System Profile</h2><dl><dt>System Type</dt><dd>Elemental Resonance &amp; Clash Dynamics</dd><dt>Primary Elements</dt><dd>Lament, Grudge, Weight, Void</dd><dt>Special Resonance</dt><dd>Hope (Dawn Initiative)</dd><dt>Core Defensive Stat</dt><dd>Resilience &amp; Mental Composure</dd><dt>Clash Phases</dt><dd>Tension → Clash → Resolution</dd><dt>Breach Multiplier</dt><dd>Fatal (x2.0), Weak (x1.5), Endure (x0.7), Ineffective (x0.5)</dd></dl></aside></section>
<article class="article-body">
<h2 id="the-four-primary-damage-types">The Four Primary Damage Types</h2>
<div class="table-wrap"><table class="data-table"><thead><tr><th>Damage Type</th><th>Visual Hue</th><th>Target Defense</th><th>Tactical Status Effect</th></tr></thead><tbody>
<tr><td><strong>Lament (비탄)</strong></td><td>Deep Blue (#38bdf8)</td><td>Composure / Mental SP</td><td><strong>Lament Drain:</strong> Inflicts mental fatigue, slows attack speed, and drains opponent SP.</td></tr>
<tr><td><strong>Grudge (원한)</strong></td><td>Crimson (#ef5b55)</td><td>Physical HP / Resilience</td><td><strong>Grudge Burn:</strong> Inflicts thermal kinetic damage that bypasses light shields and triggers stacking bleed.</td></tr>
<tr><td><strong>Weight (중압)</strong></td><td>Dense Black (#1e293b)</td><td>Armor Poise / Stagger</td><td><strong>Crushing Load:</strong> Increases target stagger threshold, slowing movement and fracturing heavy armor.</td></tr>
<tr><td><strong>Void (공허)</strong></td><td>Pale White (#f8fafc)</td><td>HP &amp; SP Simultaneously</td><td><strong>Apathy Hollow:</strong> Direct true damage that pierces both physical carapace and psychological wards.</td></tr>
</tbody></table></div>

<h2 id="the-fifth-resonance-hope">The Fifth Resonance: Hope (Gold)</h2>
<p>Introduced in Year 4,238 following the Absolvohan release, <strong>Hope</strong> (희망) is a unique catalytic frequency. It does not inflict lethal harm against humans; instead, it rapidly restores depleted Composure, purges psychological Fracture stages, and instantly dissolves low-tier Void hazes.</p>

<h2 id="resistance-and-multiplier-matrix">Resistance &amp; Multiplier Matrix</h2>
<p>Every operative and Sorrow Entity possesses innate defensive affinities against the four damage types, categorized across five standardized tiers:</p>
<div class="table-wrap"><table class="data-table"><thead><tr><th>Affinity Tier</th><th>Damage Multiplier</th><th>Visual Cue</th><th>Operational Rule</th></tr></thead><tbody>
<tr><td><strong>Fatal (치명)</strong></td><td><strong>2.0x Damage</strong></td><td>Red Strobe Alert</td><td>Immediate retreat or heavy barrier deployment required</td></tr>
<tr><td><strong>Weak (취약)</strong></td><td><strong>1.5x Damage</strong></td><td>Orange Flash</td><td>Avoid direct unmitigated hits; rotate frontline</td></tr>
<tr><td><strong>Normal (보통)</strong></td><td><strong>1.0x Damage</strong></td><td>White Impact</td><td>Standard baseline engagement</td></tr>
<tr><td><strong>Endure (견딤)</strong></td><td><strong>0.7x Damage</strong></td><td>Blue Shield Ripple</td><td>Optimal frontline tanking matchup</td></tr>
<tr><td><strong>Ineffective (저항)</strong></td><td><strong>0.5x Damage</strong></td><td>Golden Deflection</td><td>Near-complete mitigation; ideal counter-stance</td></tr>
</tbody></table></div>

<h2 id="combat-clash-mechanics">Combat Clash Mechanics</h2>
<p>When two opposing attacks target the same line of action, a <strong>Resonant Clash</strong> (충돌) occurs across three procedural phases:</p>
<ol>
<li><strong>Phase 1: Tension (긴장):</strong> Combatants lock weapons, comparing base speed and resonant power dice.</li>
<li><strong>Phase 2: Clash (충돌):</strong> Multiple rounds of dice rolling determine which fighter overcomes the other’s emotional momentum.</li>
<li><strong>Phase 3: Resolution (결의):</strong> The winner executes an uninterrupted strike while the loser suffers immediate Stagger and poise loss.</li>
</ol>
</article>
<nav class="article-nav"><a href="index.html">← Mechanics Hub</a><a href="maw-equipment-system.html">M.A.W. Equipment System →</a></nav>
</main>
{get_floor_rail()}
</div>
{get_footer()}
</body></html>"""

    with open(os.path.join(MECH_DIR, "han-energy-and-damage.html"), "w", encoding="utf-8") as f:
        f.write(energy_html)
    print("Generated mechanics/han-energy-and-damage.html")

    # 2. maw-equipment-system.html
    maw_sys_html = f"""<!doctype html><html lang="en" data-article-status="curated"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>M.A.W. Equipment System — Somnarak Wiki</title><meta name="description" content="Technical guide to Materialized Agony Wear, weapon grades, suit resistances, and resonance gifts"><link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg"><link rel="stylesheet" href="../assets/css/wiki.css"><script defer src="../assets/js/wiki.js"></script></head><body>
{get_header()}
<nav class="float-toc" aria-label="On this page"><button type="button" aria-expanded="false">CONTENTS</button><div><strong>ON THIS PAGE</strong><ol><li class="l2"><a href="#overview">Overview</a></li><li class="l2"><a href="#equipment-architecture">Equipment Architecture</a></li><li class="l2"><a href="#the-three-gear-types">The Three Gear Types</a></li><li class="l2"><a href="#potency-grades-alpha-to-omega">Potency Grades (α to ω)</a></li><li class="l2"><a href="#resonance-bonding-and-corruption">Resonance Bonding &amp; Corruption</a></li><li class="l2"><a href="#set-synergy-bonuses">Set Synergy Bonuses</a></li></ol><a href="#content">↑ TOP</a></div></nav>
<div class="wiki-shell">
{get_left_rail()}
<main id="content"><div class="page-tabs"><span>Mechanics &amp; Systems</span><b>EQUIPMENT SPECIFICATION</b></div><div class="breadcrumbs"><a href="../index.html">Main page</a><i>›</i><a href="index.html">Mechanics</a><i>›</i>M.A.W. Equipment System</div>
<section class="department-hero" style="--floor:#e8c25a"><img src="../assets/icons/weapon.svg" alt=""><div><span>ARMORY CODEX · M.A.W. PHYSICS</span><h1>M.A.W. Equipment System</h1><p>물질화된 고통의 장비 체계 — M.A.W. Jangbi Chegye</p></div></section>
<blockquote class="motto" style="--floor:#e8c25a">“You do not simply wield a M.A.W. weapon; you share a heartbeat with the agony that birthed it. Respect the bond, or become the next entity in the cell.” — Extraction Lead Zyrak</blockquote>
<section class="department-overview"><div><h2 id="overview">Overview</h2><p class="lead"><strong>M.A.W.</strong> (<em>Materialized Agony Wear</em> — 물질화된 고통의 장비) is the specialized class of combat gear extracted directly from the crystallized emotional resonance of Sorrow Entities. Manufactured in Floor 3 (Extraction Hall) and refined with the assistance of the Weaver Guild, M.A.W. items allow human operatives to harness entity-tier offensive and defensive abilities.</p><p>Every complete M.A.W. Set consists of three complementary components: a <strong>Weapon</strong> (<em>MAW-W</em>), a <strong>Suit</strong> (<em>MAW-S</em>), and a <strong>Gift</strong> (<em>MAW-G</em>), rated from Minor (α) to Transcendent (ω).</p></div><aside class="department-profile" style="--floor:#e8c25a"><h2 id="equipment-architecture">Armory Profile</h2><dl><dt>Designation</dt><dd>Materialized Agony Wear (M.A.W.)</dd><dt>Component Types</dt><dd>Weapons, Suits, Resonance Gifts</dd><dt>Potency Tiers</dt><dd>α (Minor), β (Moderate), γ (Major), δ (Critical), ω (Transcendent)</dd><dt>Harvesting Dept</dt><dd>Floor 3 · Extraction Hall</dd><dt>Textile Partner</dt><dd>The Weavers (Zone D Echo Gardens)</dd><dt>Resonance Limit</dt><dd>Max 7 Consecutive Days per Operative</dd></dl></aside></section>
<article class="article-body">
<h2 id="the-three-gear-types">The Three Gear Types</h2>
<div class="table-wrap"><table class="data-table"><thead><tr><th>Component</th><th>Codex Prefix</th><th>Functional Purpose</th><th>Operative Requirement</th></tr></thead><tbody>
<tr><td><strong>M.A.W. Weapon</strong></td><td><code>MAW-W-###-##</code></td><td>Channels entity resonance into melee, ranged, or acoustic kinetic strikes</td><td>Requires minimum Resolve &amp; Resilience stats</td></tr>
<tr><td><strong>M.A.W. Suit</strong></td><td><code>MAW-S-###-##</code></td><td>Reinforced composite armor providing damage resistances against specific elements</td><td>Requires minimum Composure &amp; Clarity stats</td></tr>
<tr><td><strong>M.A.W. Gift</strong></td><td><code>MAW-G-###-##</code></td><td>Biological/spiritual artifact that bonds to the operative’s body (mask, brooch, pendant)</td><td>Acquired through high-affinity containment Work</td></tr>
</tbody></table></div>

<h2 id="potency-grades-alpha-to-omega">Potency Grades (α to ω)</h2>
<p>M.A.W. equipment potency corresponds to the hazard classification of the source entity:</p>
<ul>
<li><strong>α (Alpha — Minor):</strong> Extracted from ZAYIN-class entities. Safe for rookie operatives; minimal psychological feedback.</li>
<li><strong>β (Beta — Moderate):</strong> Extracted from TETH-class entities. Standard field issue for regular defense personnel.</li>
<li><strong>γ (Gamma — Major):</strong> Extracted from HE-class entities. Requires veteran clearance; exhibits noticeable emotional weight.</li>
<li><strong>δ (Delta — Critical):</strong> Extracted from WAW-class entities. Devastating power; requires rigorous psychological screening.</li>
<li><strong>ω (Omega — Transcendent):</strong> Extracted from ALEPH-class entities or unique events. Extreme lethality; carries irreversible fusion risks (e.g. Majin’s Reaper fusion).</li>
</ul>

<h2 id="resonance-bonding-and-corruption">Resonance Bonding &amp; Corruption</h2>
<p>When an operative equips a M.A.W. weapon or suit, an emotional feedback loop is established between the user and the crystalline core. If an operative’s SP drops to zero while wearing high-tier gear, the entity’s lingering grief can override the user’s consciousness, triggering <strong>M.A.W. Corrosion</strong> (장비 침식) where the wearer transforms into a hostile combatant.</p>

<h2 id="set-synergy-bonuses">Set Synergy Bonuses</h2>
<p>Equipping all three matching components of a single set (e.g., <em>Named Vigil</em>, <em>Procession Without a Name</em>, <em>Absolute Set</em>) unlocks <strong>Set Resonance</strong>, granting operatives passive damage multipliers, immunity to Stagger from matching elements, and unique awakened combat skills.</p>
</article>
<nav class="article-nav"><a href="han-energy-and-damage.html">← Han Energy &amp; Damage</a><a href="containment-and-suppression.html">Containment &amp; Suppression →</a></nav>
</main>
{get_floor_rail()}
</div>
{get_footer()}
</body></html>"""

    with open(os.path.join(MECH_DIR, "maw-equipment-system.html"), "w", encoding="utf-8") as f:
        f.write(maw_sys_html)
    print("Generated mechanics/maw-equipment-system.html")

    # 3. containment-and-suppression.html
    contain_sys_html = f"""<!doctype html><html lang="en" data-article-status="curated"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Containment &amp; Suppression Protocols — Somnarak Wiki</title><meta name="description" content="Operational guide to the Four Work Types, Sorrow Gauges, breach triggers, and tactical suppression"><link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg"><link rel="stylesheet" href="../assets/css/wiki.css"><script defer src="../assets/js/wiki.js"></script></head><body>
{get_header()}
<nav class="float-toc" aria-label="On this page"><button type="button" aria-expanded="false">CONTENTS</button><div><strong>ON THIS PAGE</strong><ol><li class="l2"><a href="#overview">Overview</a></li><li class="l2"><a href="#containment-rules">Containment Rules</a></li><li class="l2"><a href="#the-four-work-types">The Four Work Types</a></li><li class="l2"><a href="#the-sorrow-gauge-and-qliphoth-analogs">The Sorrow Gauge &amp; Breach Triggers</a></li><li class="l2"><a href="#breach-suppression-protocols">Breach Suppression Protocols</a></li></ol><a href="#content">↑ TOP</a></div></nav>
<div class="wiki-shell">
{get_left_rail()}
<main id="content"><div class="page-tabs"><span>Mechanics &amp; Systems</span><b>OPERATIONAL PROTOCOL</b></div><div class="breadcrumbs"><a href="../index.html">Main page</a><i>›</i><a href="index.html">Mechanics</a><i>›</i>Containment &amp; Suppression</div>
<section class="department-hero" style="--floor:#6f7ee8"><img src="../assets/icons/ferrehan.svg" alt=""><div><span>CONTAINMENT CODEX · FACILITY OPERATIONS</span><h1>Containment &amp; Suppression Protocols</h1><p>격리와 제압 규약 — Gyeokri-gwa Jeap Gyuyak</p></div></section>
<blockquote class="motto" style="--floor:#6f7ee8">“A containment cell is not a cage; it is a conversation. If you speak in anger to an entity born of grief, the answer will always be blood.” — Containment Lead Dekan</blockquote>
<section class="department-overview"><div><h2 id="overview">Overview</h2><p class="lead">Facility operations within the Reverie Directorate revolve around two interlocking procedures: <strong>Containment Work</strong> (격리 작업 — pacifying entities to harvest Han-Energy) and <strong>Breach Suppression</strong> (탈출 제압 — neutralizing escaped entities when containment fields fail).</p><p>Personnel execute one of the <strong>Four Work Types</strong> based on the entity’s psychological profile, monitoring the <strong>Sorrow Gauge</strong> to prevent catastrophic breach thresholds.</p></div><aside class="department-profile" style="--floor:#6f7ee8"><h2 id="containment-rules">Operational Profile</h2><dl><dt>Governing Lead</dt><dd>Dekan, Containment Lead (Floor 2)</dd><dt>The Four Works</dt><dd>Ferrehan, Flerehan, Viderehan, Pugnahan</dd><dt>Work Success Metrics</dt><dd>Good (Green), Normal (Yellow), Bad (Red)</dd><dt>Threshold Indicator</dt><dd>Sorrow Gauge (슬픔 게이지, 0–100%)</dd><dt>Suppression Alert Tiers</dt><dd>Green → Amber → Crimson → Midnight</dd><dt>Core Mandatory Rule</dt><dd>Rotate Personnel Every 7 Days</dd></dl></aside></section>
<article class="article-body">
<h2 id="the-four-work-types">The Four Work Types</h2>
<p>Each Work Type represents a specific psychological and physical approach to interacting with a contained manifestation:</p>
<div class="table-wrap"><table class="data-table"><thead><tr><th>Work Type</th><th>Korean Title</th><th>Operational Method</th><th>Primary Attribute</th><th>Target Profile</th></tr></thead><tbody>
<tr><td><strong>Ferrehan (본능)</strong></td><td>페레한</td><td>Attending to physical and environmental needs, cleaning habitat, stabilizing crystal temperature</td><td><strong>Resilience (인내)</strong></td><td>Beast-like, architectural, or hunger-driven entities</td></tr>
<tr><td><strong>Flerehan (애착)</strong></td><td>플레레한</td><td>Acoustic consolation, shared weeping, listening to unspoken sorrow without judgment</td><td><strong>Composure (침착)</strong></td><td>Inner Sorrow and grief-focused maternal entities</td></tr>
<tr><td><strong>Viderehan (통찰)</strong></td><td>비데레한</td><td>Analytical observation, recording memory shifts, structural stress analysis</td><td><strong>Clarity (명료)</strong></td><td>Complex, rule-bound, and memory-weaving entities</td></tr>
<tr><td><strong>Pugnahan (억압)</strong></td><td>푸그나한</td><td>Restraining violent surges, applying kinetic dampening fields, asserting authority</td><td><strong>Resolve (정의)</strong></td><td>Wrathful, violent, or predatory Grudge entities</td></tr>
</tbody></table></div>

<h2 id="the-sorrow-gauge-and-qliphoth-analogs">The Sorrow Gauge &amp; Breach Triggers</h2>
<p>Every containment cell is equipped with a <strong>Sorrow Gauge</strong> (슬픔 게이지). Performing successful Work lowers or stabilizes the gauge; Bad results or forbidden interactions raise the gauge. When the Sorrow Gauge reaches 100%, the containment field collapses and the entity initiates a physical breach.</p>

<h2 id="breach-suppression-protocols">Breach Suppression Protocols</h2>
<p>Upon a breach sounding, Floor 2 (The Maw’s Keep) and Floor 5 (Border Watch) coordinate rapid suppression:</p>
<ul>
<li><strong>Phase 1 (Lockdown):</strong> Bulkhead doors seal the affected corridor to contain acoustic and psychic bleed.</li>
<li><strong>Phase 2 (Resonance Matching):</strong> Operatives equipped with opposing M.A.W. damage types engage the entity (e.g., Grudge weapons against Lament entities).</li>
<li><strong>Phase 3 (Re-Crystallization):</strong> Once staggered and reduced to 0 HP, the entity dissolves into dormant crystalline sludge and is vacuum-pumped back into its containment unit.</li>
</ul>
</article>
<nav class="article-nav"><a href="maw-equipment-system.html">← M.A.W. Equipment System</a><a href="fracture-and-therapy.html">Fracture &amp; Therapy →</a></nav>
</main>
{get_floor_rail()}
</div>
{get_footer()}
</body></html>"""

    with open(os.path.join(MECH_DIR, "containment-and-suppression.html"), "w", encoding="utf-8") as f:
        f.write(contain_sys_html)
    print("Generated mechanics/containment-and-suppression.html")

    # 4. fracture-and-therapy.html
    fracture_sys_html = f"""<!doctype html><html lang="en" data-article-status="curated"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Psychological Fracture &amp; Therapy — Somnarak Wiki</title><meta name="description" content="Diagnostic guide to mental wear, psychological fracture stages, panic behaviors, and infirmary therapy"><link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg"><link rel="stylesheet" href="../assets/css/wiki.css"><script defer src="../assets/js/wiki.js"></script></head><body>
{get_header()}
<nav class="float-toc" aria-label="On this page"><button type="button" aria-expanded="false">CONTENTS</button><div><strong>ON THIS PAGE</strong><ol><li class="l2"><a href="#overview">Overview</a></li><li class="l2"><a href="#diagnostic-profile">Diagnostic Profile</a></li><li class="l2"><a href="#the-stages-of-fracture">The Stages of Fracture</a></li><li class="l2"><a href="#panic-behavioral-archetypes">Panic Behavioral Archetypes</a></li><li class="l2"><a href="#infirmary-therapy-and-recovery">Infirmary Therapy &amp; Recovery</a></li></ol><a href="#content">↑ TOP</a></div></nav>
<div class="wiki-shell">
{get_left_rail()}
<main id="content"><div class="page-tabs"><span>Mechanics &amp; Systems</span><b>PSYCHOLOGICAL FRAMEWORK</b></div><div class="breadcrumbs"><a href="../index.html">Main page</a><i>›</i><a href="index.html">Mechanics</a><i>›</i>Fracture &amp; Therapy</div>
<section class="department-hero" style="--floor:#8d2e42"><img src="../assets/icons/fracture.svg" alt=""><div><span>MEDICAL CODEX · MENTAL HEALTH</span><h1>Psychological Fracture &amp; Therapy</h1><p>정신적 균열과 치유 — Jeongsinjeok Gyunyeol-gwa Chiyu</p></div></section>
<blockquote class="motto" style="--floor:#8d2e42">“The mind is glass held over a flame. Expose it to too much grief, and it will crack. The art of medicine in this city is teaching the pieces how to fit together again.” — Chief Medical Officer Vian</blockquote>
<section class="department-overview"><div><h2 id="overview">Overview</h2><p class="lead">In Somnarak, prolonged exposure to high-resonance Han, entity contact, and M.A.W. feedback inflicts severe mental stress known as <strong>Fracture</strong> (균열 — <em>Gyunyeol</em>). When an operative’s psychological defense (<em>Sanity Points / SP</em>) degrades, the individual undergoes progressive stages of mental collapse.</p><p>Understanding the warning signs of Fracture and deploying timely therapeutic interventions in Floor 1’s Infirmary and Zone D’s Echo Gardens prevents irreversible psychological metamorphosis.</p></div><aside class="department-profile" style="--floor:#8d2e42"><h2 id="diagnostic-profile">Diagnostic Profile</h2><dl><dt>Condition Title</dt><dd>Psychological Fracture (정신적 균열)</dd><dt>Primary Diagnostic Stat</dt><dd>Sanity Points (SP, Max 100 / Min -100)</dd><dt>Progression Stages</dt><dd>Stage 1 (Strain) → Stage 2 (Hairline) → Stage 3 (Rupture) → Stage 4 (Metamorphosis)</dd><dt>Primary Treatment</dt><dd>Acoustic Dampening Lofts &amp; Weeping Dilution Therapy</dd><dt>Facility Treatment Point</dt><dd>Floor 1 Neutral Infirmary &amp; Zone D Gardens</dd></dl></aside></section>
<article class="article-body">
<h2 id="the-stages-of-fracture">The Stages of Fracture</h2>
<div class="table-wrap"><table class="data-table"><thead><tr><th>Fracture Stage</th><th>SP Range</th><th>Symptom Manifestations</th><th>Operational Status</th></tr></thead><tbody>
<tr><td><strong>Stage 1: Strain (피로)</strong></td><td>+50 to +20 SP</td><td>Mild auditory tinnitus, phantom weeping sounds, slight sleep disruption</td><td>Fit for duty; mandatory counseling break</td></tr>
<tr><td><strong>Stage 2: Hairline (미세 균열)</strong></td><td>+19 to 0 SP</td><td>Visual hallucinations of deceased relatives, sudden bursts of crying or anger</td><td>Restricted duty; forbidden from WAW/ALEPH work</td></tr>
<tr><td><strong>Stage 3: Rupture (파열)</strong></td><td>-1 to -50 SP</td><td>Total loss of emotional regulation, aggressive panic, inability to recognize colleagues</td><td>Immediate combat suppression; quarantine</td></tr>
<tr><td><strong>Stage 4: Metamorphosis (변형)</strong></td><td>-51 to -100 SP</td><td>Biological crystallization; the human psyche collapses into a permanent Minor SE</td><td>Permanent irreversible transformation</td></tr>
</tbody></table></div>

<h2 id="panic-behavioral-archetypes">Panic Behavioral Archetypes</h2>
<p>When an operative hits zero SP during an active breach, they enter one of four distinct <strong>Panic Archetypes</strong> based on their dominant personal trait:</p>
<ul>
<li><strong>The Mourner (Lament):</strong> Collapses into uncontrollable weeping, becoming completely immobile and vulnerable.</li>
<li><strong>The Berserker (Grudge):</strong> Attacks the nearest entity or colleague with reckless frenzy, ignoring self-preservation.</li>
<li><strong>The Wanderer (Void):</strong> Flees aimlessly down corridors, randomly opening containment doors.</li>
<li><strong>The Zealot (Weight):</strong> Surrenders to the entity’s psychic aura, actively defending the breach against Directorate suppression teams.</li>
</ul>

<h2 id="infirmary-therapy-and-recovery">Infirmary Therapy &amp; Recovery</h2>
<p>Floor 1’s Infirmary utilizes specialized <strong>Resonance Pods</strong> filled with diluted, purified Weeping fluid. These pods neutralize crystallized psychic buildup in the brain stem while Master Weavers from Zone D play calibrated harmonic harp frequencies to realign the patient’s fractured emotional polarity.</p>
</article>
<nav class="article-nav"><a href="containment-and-suppression.html">← Containment &amp; Suppression</a><a href="index.html">Mechanics Hub →</a></nav>
</main>
{get_floor_rail()}
</div>
{get_footer()}
</body></html>"""

    with open(os.path.join(MECH_DIR, "fracture-and-therapy.html"), "w", encoding="utf-8") as f:
        f.write(fracture_sys_html)
    print("Generated mechanics/fracture-and-therapy.html")

    # 5. mechanics/index.html (Mechanics Hub)
    mech_hub_html = f"""<!doctype html><html lang="en" data-article-status="curated"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Battle &amp; Game Mechanics — Somnarak Wiki</title><meta name="description" content="Comprehensive reference for Somnarak battle mechanics, Han energy, M.A.W. equipment, containment, and mental health"><link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg"><link rel="stylesheet" href="../assets/css/wiki.css"><script defer src="../assets/js/wiki.js"></script></head><body>
{get_header()}
<nav class="float-toc" aria-label="On this page"><button type="button" aria-expanded="false">CONTENTS</button><div><strong>ON THIS PAGE</strong><ol><li class="l2"><a href="#overview">Overview</a></li><li class="l2"><a href="#core-systems">Core Systems</a></li><li class="l2"><a href="#mechanics-index">Mechanics Index</a></li><li class="l2"><a href="#tactical-summary">Tactical Summary</a></li></ol><a href="#content">↑ TOP</a></div></nav>
<div class="wiki-shell">
{get_left_rail()}
<main id="content"><div class="page-tabs"><span>Mechanics &amp; Systems</span><b>TACTICAL REFERENCE</b></div><div class="breadcrumbs"><a href="../index.html">Main page</a><i>›</i>Mechanics</div>
<section class="wide-hero"><div><span>SOMNARAK COMBAT &amp; FACILITY SYSTEMS</span><h1>Battle &amp; Systems Mechanics</h1><p>전투 및 시스템 규약 — Jeontu mit Siseutem Gyuyak</p></div><img src="../assets/icons/banner_mechanics.svg" alt="Mechanics of Somnarak"></section>
<article class="article-body">
<h2 id="overview">Overview</h2>
<p>The operational and combat systems of Somnarak translate the metaphysical weight of sorrow into exact tactical mechanics. Whether managing containment shifts in the Hand of Change or engaging rogue entities in the Desolate, personnel operate under rigorous procedural systems governing energy, armor, mental stability, and weapon resonance.</p>

<h2 id="core-systems">Core Systems</h2>
<div class="contents-grid">
<section>
<h3>Combat Physics</h3>
<a href="han-energy-and-damage.html"><strong>Han Energy &amp; Damage</strong><br><small>Lament, Grudge, Weight, Void, and Hope formulas</small></a>
<a href="han-energy-and-damage.html#combat-clash-mechanics"><strong>Resonant Clashes</strong><br><small>Tension, Clash, and Resolution duel mechanics</small></a>
</section>
<section>
<h3>M.A.W. Gear</h3>
<a href="maw-equipment-system.html"><strong>M.A.W. Equipment System</strong><br><small>Weapons, Suits, Gifts, and Potency Tiers (α–ω)</small></a>
<a href="maw-equipment-system.html#set-synergy-bonuses"><strong>Set Resonance</strong><br><small>Matching bonuses and corrosion avoidance</small></a>
</section>
<section>
<h3>Containment Ops</h3>
<a href="containment-and-suppression.html"><strong>Containment Protocols</strong><br><small>The Four Works: Ferrehan, Flerehan, Viderehan, Pugnahan</small></a>
<a href="containment-and-suppression.html#breach-suppression-protocols"><strong>Breach Suppression</strong><br><small>Containment cell alerts and suppression tactics</small></a>
</section>
<section>
<h3>Mental Health</h3>
<a href="fracture-and-therapy.html"><strong>Psychological Fracture</strong><br><small>Sanity tracking, stages of breakdown, panic archetypes</small></a>
<a href="fracture-and-therapy.html#infirmary-therapy-and-recovery"><strong>Infirmary Recovery</strong><br><small>Resonance pods and acoustic harp treatment</small></a>
</section>
</div>

<h2 id="mechanics-index">Mechanics Index</h2>
<div class="table-wrap"><table class="data-table"><thead><tr><th>System Section</th><th>Primary Focus</th><th>Key Variables</th><th>Operational Application</th></tr></thead><tbody>
<tr><td><a href="han-energy-and-damage.html"><strong>Han Energy &amp; Damage</strong></a></td><td>Damage calculation and elemental affinities</td><td>Lament, Grudge, Weight, Void, Hope</td><td>Direct combat engagements, armor optimization</td></tr>
<tr><td><a href="maw-equipment-system.html"><strong>M.A.W. Equipment System</strong></a></td><td>Weapon, suit, and gift specifications</td><td>Potency (α–ω), Resonance bonding, Corrosion</td><td>Armory loadouts, operative gear matching</td></tr>
<tr><td><a href="containment-and-suppression.html"><strong>Containment &amp; Suppression</strong></a></td><td>Daily entity management and breach response</td><td>The Four Works, Sorrow Gauge (0–100%)</td><td>Floor operations, energy harvesting</td></tr>
<tr><td><a href="fracture-and-therapy.html"><strong>Fracture &amp; Therapy</strong></a></td><td>Mental health diagnostics and recovery</td><td>SP (+100 to -100), 4 Panic Archetypes</td><td>Infirmary rotation, psychological protection</td></tr>
</tbody></table></div>

<h2 id="tactical-summary">Tactical Summary</h2>
<p>Every operational success in Somnarak relies on balance: equip the proper M.A.W. resistance against the target’s damage type, maintain operative SP above hairline fracture thresholds, and choose the containment Work that honors the entity’s original sorrow.</p>
</article>
</main>
{get_floor_rail()}
</div>
{get_footer()}
</body></html>"""

    with open(os.path.join(MECH_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(mech_hub_html)
    print("Generated mechanics/index.html")

build_mechanics_pages()
