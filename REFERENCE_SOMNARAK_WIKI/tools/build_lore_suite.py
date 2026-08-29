import os
import re

LORE_DIR = "/home/user/01_Somnarak_Wiki/lore"
os.makedirs(LORE_DIR, exist_ok=True)

from generate_all_characters import get_left_rail, get_floor_rail, get_header, get_footer

def build_lore_pages():
    # 1. somnarak-cosmology.html
    cosmology_html = f"""<!doctype html><html lang="en" data-article-status="curated"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Somnarak Cosmology &amp; The Weeping — Somnarak Wiki</title><meta name="description" content="Cosmological foundation of the World of Dream and Abyss, Han physics, and the subterranean river of grief"><link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg"><link rel="stylesheet" href="../assets/css/wiki.css"><script defer src="../assets/js/wiki.js"></script></head><body>
{get_header()}
<nav class="float-toc" aria-label="On this page"><button type="button" aria-expanded="false">CONTENTS</button><div><strong>ON THIS PAGE</strong><ol><li class="l2"><a href="#overview">Overview</a></li><li class="l2"><a href="#cosmic-architecture">Cosmic Architecture</a></li><li class="l2"><a href="#the-two-primordial-states">The Two Primordial States</a></li><li class="l2"><a href="#the-river-of-liquid-grief-the-weeping">The Weeping (River of Liquid Grief)</a></li><li class="l2"><a href="#han-the-binding-force">Han — The Binding Force</a></li><li class="l2"><a href="#the-four-emotional-elements">The Four Emotional Elements</a></li><li class="l2"><a href="#the-seven-taboos">The Seven Absolute Taboos</a></li></ol><a href="#content">↑ TOP</a></div></nav>
<div class="wiki-shell">
{get_left_rail()}
<main id="content"><div class="page-tabs"><span>Lore &amp; Cosmology</span><b>COSMIC FOUNDATION</b></div><div class="breadcrumbs"><a href="../index.html">Main page</a><i>›</i><a href="index.html">Lore &amp; Cosmology</a><i>›</i>Somnarak Cosmology</div>
<section class="department-hero" style="--floor:#38bdf8"><img src="../assets/icons/banner_lore.svg" alt=""><div><span>SOMNARAK COSMIC SCHEMATIC</span><h1>Somnarak Cosmology</h1><p>꿈과 나락의 세계 — Gkum-gwa Narak-ui Segye</p></div></section>
<blockquote class="motto" style="--floor:#38bdf8">“The world did not begin with light or void. It began with an ache that refused to sleep.” — The First Record, Year 0</blockquote>
<section class="department-overview"><div><h2 id="overview">Overview</h2><p class="lead"><strong>Somnarak</strong> (소마나락) is the World of Dream (<em>Somnus</em>) and Abyss (<em>Narak</em>). Founded in the deep geological hollow beneath the Alpha Tree and elevated above the subterranean river known as <strong>The Weeping</strong>, the city exists within a closed cosmological framework where unexpressed human sorrow does not dissipate, but accumulates as a physical, energetic, and metaphysical constant known as <strong>Han</strong> (한).</p><p>Cosmologically, the universe is divided into four cardinal corners (<em>Mugenhan</em>), of which Somnarak is Corner 1. Outside the municipal boundary lies the infinite expanse of the Desolate, while deep beneath the foundations flows the primordial river that feeds all psychic resonance.</p></div><aside class="department-profile" style="--floor:#38bdf8"><h2 id="cosmic-architecture">Cosmic Profile</h2><dl><dt>Cosmological Name</dt><dd>Somnarak (Corner 1 of Mugenhan)</dd><dt>Foundational Anchor</dt><dd>The Alpha Tree &amp; The Weeping River</dd><dt>Primary Currency</dt><dd>Han-Energy / Emotional Resonance</dd><dt>Governing Principle</dt><dd>Conservation of Unresolved Sorrow</dd><dt>Cardinal Axis</dt><dd>Dream (Above) / Abyss (Below)</dd><dt>Dominant Elements</dt><dd>Lament, Grudge, Weight, Void, Hope</dd><dt>Current Era</dt><dd>Year 4,238 · Dawn Initiative</dd></dl></aside></section>
<article class="article-body">
<h2 id="the-two-primordial-states">The Two Primordial States</h2>
<p>Somnarak cosmology is defined by the perpetual tension between two fundamental states of being:</p>
<ul>
<li><strong>Somnus (The Dream Realm):</strong> The ethereal, weightless stratum that rests above the physical city. It is the domain of unfulfilled aspirations, sleeping consciousness, and delicate memory filaments. When untethered, the Dream manifests as phantasmal mirages and sleep illnesses.</li>
<li><strong>Narak (The Abyss):</strong> The dense, crushing geological under-stratum beneath Zone B and C. It is the realm of accumulated generational grudge, forgotten corpses, and the raw pressure of the Weeping. In Narak, matter compresses into dense Han-crystals capable of generating immense industrial power.</li>
</ul>

<h2 id="the-river-of-liquid-grief-the-weeping">The Weeping (River of Liquid Grief)</h2>
<p>Flowing through the deepest fissures beneath Zone B (The Maw), <strong>The Weeping</strong> (통곡의 강) is a subterranean river of luminescent, semi-viscous blue fluid. It is neither ordinary water nor pure magic; it is the condensed, liquid form of every tear shed and every unspoken lament felt across human history.</p>
<div class="table-wrap"><table class="data-table"><thead><tr><th>Property</th><th>Scientific Measurement</th><th>Cosmological Effect</th></tr></thead><tbody><tr><td><strong>Fluid Density</strong></td><td>1.42 g/cm³ at standard facility pressure</td><td>Sinks beneath ordinary water; coats solid surfaces in acoustic residue</td></tr><tr><td><strong>Thermal Signature</strong></td><td>Consistent 4.2°C regardless of ambient heat</td><td>Extracts ambient kinetic energy; induces emotional chill upon contact</td></tr><tr><td><strong>Resonant Emission</strong></td><td>Continuous 17 Hz subsonic hum</td><td>Generates the foundational background hum of the entire city</td></tr><tr><td><strong>Biological Interaction</strong></td><td>Causes immediate weeping and memory projection</td><td>Direct ingestion triggers rapid crystallization or permanent psychic Fracture</td></tr></tbody></table></div>

<h2 id="han-the-binding-force">Han — The Binding Force</h2>
<p><strong>Han</strong> (한) is the primary physical and metaphysical force in Somnarak. Produced whenever a sentient entity experiences injustice, loss, unfulfilled desire, or silent grief, Han does not degrade over time. Instead, it adheres to architecture, crystal matrices, and biological nervous systems. When harnessed by the Reverie Directorate, Han-Energy powers the city’s electrical grid, fuels M.A.W. weaponry, and sustains the protective Aegis Veil.</p>

<h2 id="the-four-emotional-elements">The Four Emotional Elements</h2>
<p>All Han manifestations express through one or more of four fundamental elemental signatures:</p>
<div class="table-wrap"><table class="data-table"><thead><tr><th>Element</th><th>Color Spectrum</th><th>Emotional Source</th><th>Tactical &amp; Physical Effect</th></tr></thead><tbody><tr><td><strong>Lament (비탄)</strong></td><td>Deep Blue (#38bdf8 / #1e3a8a)</td><td>Mourning, tears, sorrow of loss</td><td>Acoustic shockwaves, slowing, mental fatigue, cold dampening</td></tr><tr><td><strong>Grudge (원한)</strong></td><td>Crimson (#ef5b55 / #991b1b)</td><td>Anger, betrayal, righteous fury</td><td>Thermal combustion, kinetic piercing, bleeding, aggressive frenzy</td></tr><tr><td><strong>Weight (중압)</strong></td><td>Dense Black (#1e293b / #020617)</td><td>Crushing responsibility, guilt, debt</td><td>Gravitational compression, armor crushing, immobility, physical fatigue</td></tr><tr><td><strong>Void (공허)</strong></td><td>Pale White / Silver (#cbd5e1 / #f8fafc)</td><td>Apathy, erasure, amnesia, numbness</td><td>Resonance dispersion, shield bypass, memory erosion, psychic hollow</td></tr></tbody></table></div>

<h2 id="the-seven-taboos">The Seven Absolute Taboos</h2>
<p>To prevent the catastrophic unraveling of the metropolitan reality, the Council and Directorate enforce <strong>Seven Absolute Taboos</strong> (일곱 금지):</p>
<ol>
<li><strong>Taboo 1: No Resurrection (부활 금지):</strong> The dead must remain dead. Attempts to reanimate biological corpses using Han invariably produce uncontrollable ALEPH-tier Object SEs.</li>
<li><strong>Taboo 2: No True AI (진정한 인공지능 금지):</strong> Constructs must not possess unrestricted self-replicating emotion matrices without Directorate hard-coded limits.</li>
<li><strong>Taboo 3: No Han Immunity (한 면역 금지):</strong> No human or structure may be engineered to be completely immune to emotional resonance; total immunity shatters the social fabric.</li>
<li><strong>Taboo 4: No Time Reversal (시간 역행 금지):</strong> The temporal arrow must move forward; rewinding local time fractures the causality of the Weeping.</li>
<li><strong>Taboo 5: No Sorrow Synthesis (한 합성 금지):</strong> Artificially manufacturing human grief through industrial torture is punishable by immediate execution.</li>
<li><strong>Taboo 6: No Outside Gate Opening (외문 개방 금지):</strong> Gate 5 must remain sealed except under supreme Director authorization.</li>
<li><strong>Taboo 7: No Door Dismantling (최종 문 해체 금지):</strong> The Final Door in the Deep Vault must never be physically breached or disassembled.</li>
</ol>
</article>
<nav class="article-nav"><a href="index.html">← Lore Hub</a><a href="the-three-sorrows.html">The Three Sorrows →</a></nav>
</main>
{get_floor_rail()}
</div>
{get_footer()}
</body></html>"""

    with open(os.path.join(LORE_DIR, "somnarak-cosmology.html"), "w", encoding="utf-8") as f:
        f.write(cosmology_html)
    print("Generated lore/somnarak-cosmology.html")

    # 2. the-three-sorrows.html
    three_sorrows_html = f"""<!doctype html><html lang="en" data-article-status="curated"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>The Three Sorrows (Samhan) — Somnarak Wiki</title><meta name="description" content="Detailed analysis of City Sorrow (Dohan), Outside Sorrow (Oehan), and Inner Sorrow (Naehan)"><link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg"><link rel="stylesheet" href="../assets/css/wiki.css"><script defer src="../assets/js/wiki.js"></script></head><body>
{get_header()}
<nav class="float-toc" aria-label="On this page"><button type="button" aria-expanded="false">CONTENTS</button><div><strong>ON THIS PAGE</strong><ol><li class="l2"><a href="#overview">Overview</a></li><li class="l2"><a href="#tripartite-classification">Tripartite Classification</a></li><li class="l2"><a href="#city-sorrow-dohan">City Sorrow (도한 — Dohan)</a></li><li class="l2"><a href="#outside-sorrow-oehan">Outside Sorrow (외한 — Oehan)</a></li><li class="l2"><a href="#inner-sorrow-naehan">Inner Sorrow (내한 — Naehan)</a></li><li class="l2"><a href="#comparative-matrix">Comparative Matrix</a></li></ol><a href="#content">↑ TOP</a></div></nav>
<div class="wiki-shell">
{get_left_rail()}
<main id="content"><div class="page-tabs"><span>Lore &amp; Cosmology</span><b>CLASSIFICATION AXIS</b></div><div class="breadcrumbs"><a href="../index.html">Main page</a><i>›</i><a href="index.html">Lore &amp; Cosmology</a><i>›</i>The Three Sorrows</div>
<section class="department-hero" style="--floor:#71efaf"><img src="../assets/icons/origin.svg" alt=""><div><span>ORIGIN CODEX · SAMHAN</span><h1>The Three Sorrows</h1><p>삼한 — Samhan (Dohan, Oehan, Naehan)</p></div></section>
<blockquote class="motto" style="--floor:#71efaf">“Sorrow born of walls, sorrow born of wastes, sorrow born of blood. Know where the ache was planted, or the harvest will destroy you.” — Directorate Archival Maxim</blockquote>
<section class="department-overview"><div><h2 id="overview">Overview</h2><p class="lead">In Somnarak categorization, all manifestations of Han, Sorrow Entities, and emotional resonance originate from one of three primary environmental and psychological vectors known collectively as the <strong>Three Sorrows</strong> (삼한 — <em>Samhan</em>): <strong>City Sorrow</strong> (<em>Dohan</em>), <strong>Outside Sorrow</strong> (<em>Oehan</em>), and <strong>Inner Sorrow</strong> (<em>Naehan</em>).</p><p>Understanding an entity’s origin is the single most critical factor in determining containment containment protocols, extraction yields, and psychological hazard ratings for field personnel.</p></div><aside class="department-profile" style="--floor:#71efaf"><h2 id="tripartite-classification">Classification Profile</h2><dl><dt>Taxonomy</dt><dd>The Three Sorrows (삼한)</dd><dt>Primary Origins</dt><dd>City (C) / Outside (O) / Inner (N)</dd><dt>Diagnostic Tools</dt><dd>Sorrow Spectrometer &amp; Resonance Tuning Fork</dd><dt>Behavioral Scope</dt><dd>Structural / Environmental / Intimate</dd><dt>Threat Diversity</dt><dd>ZAYIN to ALEPH Across All Three</dd><dt>Containment Method</dt><dd>Four Work Types (Ferrehan, Pugnahan, etc.)</dd></dl></aside></section>
<article class="article-body">
<h2 id="city-sorrow-dohan">City Sorrow (도한 — Dohan)</h2>
<p><strong>Prefix Designation:</strong> <code>C-</code></p>
<p><strong>City Sorrow</strong> is generated by the collective pressures of urban civilization: bureaucratic injustice, unpaid debts, crowded housing, institutional neglect, economic servitude, and the shared grief of metropolitan catastrophes. It manifests within the walls of Somnarak and adheres strongly to masonry, documents, bells, tools, and municipal infrastructure.</p>
<ul>
<li><strong>Canonical Examples:</strong> SE-001 (The Orphaned Bell), SE-002 (The Grieving Colossus), SE-009 (The Memory Weaver), SE-014 (The Debt Eater), SE-015 (The Debt Scale).</li>
<li><strong>Operational Characteristics:</strong> Highly structured and rule-bound. City Entities often follow strict behavioral triggers, contract clauses, or algorithmic patterns that can be predicted and managed through systematic procedure.</li>
</ul>

<h2 id="outside-sorrow-oehan">Outside Sorrow (외한 — Oehan)</h2>
<p><strong>Prefix Designation:</strong> <code>O-</code></p>
<p><strong>Outside Sorrow</strong> originates from the infinite, freezing wilderness of the Desolate beyond Somnarak’s perimeter bulwarks. It is the sorrow of exile, isolation, lost travelers, forgotten civilizations, and the sheer uncaring vastness of the empty earth. It lacks the institutional structure of City Sorrow, manifesting as shifting weather patterns, vast geological tides, or phantasmal mists.</p>
<ul>
<li><strong>Canonical Examples:</strong> SE-003 (The Wilderness Tide), SE-007 (Brume), SE-884 (Seething Tundra), SE-993 (Survivor’s Span).</li>
<li><strong>Operational Characteristics:</strong> Highly volatile and expansive. Outside Entities rarely stay confined to a single room; they flow along atmospheric Han-currents and resist conventional containment cell dampeners.</li>
</ul>

<h2 id="inner-sorrow-naehan">Inner Sorrow (내한 — Naehan)</h2>
<p><strong>Prefix Designation:</strong> <code>N-</code></p>
<p><strong>Inner Sorrow</strong> is the most intimate and psychologically devastating category. It arises from biological relationships, familial betrayal, smothered maternal love, broken personal promises, self-loathing, and unresolved guilt carried in the blood. Inner Entities target individual human psychology directly, bypassing physical armor to assault the victim’s Composure and Clarity.</p>
<ul>
<li><strong>Canonical Examples:</strong> SE-005 (The Smothering Mother), SE-901 (Duri’s Heart), SE-941 (Grieving Love), SE-965 (Unheard).</li>
<li><strong>Operational Characteristics:</strong> Highly parasitic and invasive. Inner Entities frequently bond with personnel on an emotional level, inducing hallucinations, phantom familial voices, and rapid psychological Fracture.</li>
</ul>

<h2 id="comparative-matrix">Comparative Matrix</h2>
<div class="table-wrap"><table class="data-table"><thead><tr><th>Category</th><th>Source Vector</th><th>Primary Element</th><th>Behavioral Profile</th><th>Containment Vulnerability</th></tr></thead><tbody>
<tr><td><strong>City Sorrow (C-)</strong></td><td>Urban density, municipal debt, laws, collective memory</td><td>Weight / Lament / Void</td><td>Rule-governed, contract-driven, architectural</td><td>Vulnerable to <em>Viderehan</em> (Insight) and strict protocol adherence</td></tr>
<tr><td><strong>Outside Sorrow (O-)</strong></td><td>The Desolate, exile, vast horizons, abandoned ruins</td><td>Void / Weight / Lament</td><td>Atmospheric, migratory, expansive, formless</td><td>Vulnerable to <em>Ferrehan</em> (Instinct) and physical kinetic anchors</td></tr>
<tr><td><strong>Inner Sorrow (N-)</strong></td><td>Blood ties, smothered love, family grief, broken vows</td><td>Grudge / Lament</td><td>Psychic, parasitic, intimate, emotionally focused</td><td>Vulnerable to <em>Flerehan</em> (Attachment) and emotional catharsis</td></tr>
</tbody></table></div>
</article>
<nav class="article-nav"><a href="somnarak-cosmology.html">← Somnarak Cosmology</a><a href="the-cycle-and-absolvohan.html">The Cycle &amp; Absolvohan →</a></nav>
</main>
{get_floor_rail()}
</div>
{get_footer()}
</body></html>"""

    with open(os.path.join(LORE_DIR, "the-three-sorrows.html"), "w", encoding="utf-8") as f:
        f.write(three_sorrows_html)
    print("Generated lore/the-three-sorrows.html")

    # 3. the-cycle-and-absolvohan.html
    cycle_html = f"""<!doctype html><html lang="en" data-article-status="curated"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>The Cycle &amp; The Absolvohan — Somnarak Wiki</title><meta name="description" content="Chronicle of the 1,778 historical loop iterations, the hidden Han reserve, and the activation of the Hand of Hope"><link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg"><link rel="stylesheet" href="../assets/css/wiki.css"><script defer src="../assets/js/wiki.js"></script></head><body>
{get_header()}
<nav class="float-toc" aria-label="On this page"><button type="button" aria-expanded="false">CONTENTS</button><div><strong>ON THIS PAGE</strong><ol><li class="l2"><a href="#overview">Overview</a></li><li class="l2"><a href="#the-cycle-parameters">The Cycle Parameters</a></li><li class="l2"><a href="#the-1778-iterations">The 1,778 Iterations</a></li><li class="l2"><a href="#the-absolvohan-weapon-and-reserve">The Absolvohan Weapon &amp; Reserve</a></li><li class="l2"><a href="#day-365-the-final-choice">Day 365: The Final Choice</a></li><li class="l2"><a href="#the-dawn-initiative-year-4238">The Dawn Initiative (Year 4,238)</a></li></ol><a href="#content">↑ TOP</a></div></nav>
<div class="wiki-shell">
{get_left_rail()}
<main id="content"><div class="page-tabs"><span>Lore &amp; Cosmology</span><b>HISTORICAL LOOP &amp; DAWN</b></div><div class="breadcrumbs"><a href="../index.html">Main page</a><i>›</i><a href="index.html">Lore &amp; Cosmology</a><i>›</i>The Cycle &amp; Absolvohan</div>
<section class="department-hero" style="--floor:#f1df76"><img src="../assets/icons/ref_absolvohan.svg" alt=""><div><span>ARCHIVAL CHRONICLE · 1,778 ITERATIONS</span><h1>The Cycle &amp; Absolvohan</h1><p>순환과 해소한 — Sunhwan-gwa Haesohan</p></div></section>
<blockquote class="motto" style="--floor:#f1df76">“One thousand seven hundred and seventy-eight times we watched the city burn in the final second. On the last morning, we chose not to shoot the world, but to open the hand.” — Seiyon, The Secretary</blockquote>
<section class="department-overview"><div><h2 id="overview">Overview</h2><p class="lead"><strong>The Cycle</strong> (순환) was a closed temporal and metaphysical recursion loop designed by Director Majin to accumulate enough pure Han-Energy to solve Somnarak’s existential crisis. Spanning exactly 365 operational days per iteration, the loop repeated <strong>1,778 times</strong>, resetting the city’s population, physical infrastructure, and personnel while preserving the memory of only the Director and Secretary.</p><p>The accumulated energy was channeled into <strong>The Absolvohan</strong> (해소한), a catastrophic superweapon concealed beneath Floor 1. On Day 365 of the 1,778th Cycle, Majin refused the intended planetary wipe, instead distributing the energy across the city as the <em>Hand of Hope</em>, permanently ending the Cycle and initiating Year 4,238.</p></div><aside class="department-profile" style="--floor:#f1df76"><h2 id="the-cycle-parameters">Loop Parameters</h2><dl><dt>Iteration Count</dt><dd>1,778 completed cycles</dd><dt>Loop Duration</dt><dd>365 Days per cycle (Day 0 to Day 365)</dd><dt>Accumulated Reserve</dt><dd>47.3 tons of crystallized Absolvohan Han</dd><dt>Concealment Point</dt><dd>Sub-vault beneath Floor 1 Neutral Command</dd><dt>Resolution Event</dt><dd>The Hand of Hope Discharge (Year 4,238)</dd><dt>Current Status</dt><dd>Permanently Terminated · Linear Time Restored</dd></dl></aside></section>
<article class="article-body">
<h2 id="the-1778-iterations">The 1,778 Iterations</h2>
<p>Throughout the 1,778 Cycles, the Reverie Directorate operated under an agonizing routine. Every Cycle began on Day 0 with Seiyon’s morning report to Majin and progressed through escalating entity breaches, departmental breakdowns, and Ordeal surges until reaching the critical mass threshold on Day 365.</p>
<p>Across these iterations, Majin tested every conceivable combination of containment strategies, personnel assignments, and M.A.W. extractions, seeking a path that did not end in total metropolitan extinction. Each failed iteration culminated in the reset pulse, erasing the lives and memories of hundreds of thousands of citizens while adding to the Director’s unbearable weight of remembrance.</p>

<h2 id="the-absolvohan-weapon-and-reserve">The Absolvohan Weapon &amp; Reserve</h2>
<p>Beneath the floorboards of Floor 1 Neutral Command lay the facility’s deepest secret: the <strong>Absolvohan Cannon</strong> and its 47.3-ton reserve of ultra-refined Han-crystal. The Council of Sighs believed the Directorate was barely harvesting enough energy to meet municipal quotas, unaware that Majin was systematically skimming 30% of all extracted energy to fuel the weapon.</p>
<p>The original design called for the Absolvohan to fire a singular hyper-compressed beam into the heart of the Weeping, obliterating the river of grief and resetting the planet’s metaphysical foundation at the cost of incinerating Somnarak and all its inhabitants.</p>

<h2 id="day-365-the-final-choice">Day 365: The Final Choice</h2>
<p>In the climactic sequence of <em>Absolvohan Part 9</em>, as the facility buckled under simultaneous ALEPH breaches and the final Ordeal engulfed the Palm, Majin sat at the trigger terminal. Confronted by Seiyon’s testimony and the realization that erasing sorrow through annihilation would merely create the ultimate monument to despair, Majin altered the firing matrix.</p>
<p>Rather than firing downward into the Weeping, the Absolvohan Cannon discharged upward through the crown of the Alpha Tree, diffusing the 47.3 tons of Han into a magnificent golden atmospheric aurora known as the <strong>Hand of Hope</strong> (희망의 손). The release permanently transformed 15% of the world’s ambient sorrow into golden resonance, unlocked the Maw’s thousand trapped souls, and shattered the recursion loop forever.</p>

<h2 id="the-dawn-initiative-year-4238">The Dawn Initiative (Year 4,238)</h2>
<p>With linear time restored, the city entered <strong>Year 4,238</strong> under the <strong>Dawn Initiative</strong> (새벽 이니셔티브). The end of the Cycle did not eliminate grief or sorrow; instead, it proved that sorrow can be acknowledged, carried together, and transformed into enduring hope without sacrificing human dignity.</p>
</article>
<nav class="article-nav"><a href="the-three-sorrows.html">← The Three Sorrows</a><a href="the-alpha-tree.html">The Alpha Tree →</a></nav>
</main>
{get_floor_rail()}
</div>
{get_footer()}
</body></html>"""

    with open(os.path.join(LORE_DIR, "the-cycle-and-absolvohan.html"), "w", encoding="utf-8") as f:
        f.write(cycle_html)
    print("Generated lore/the-cycle-and-absolvohan.html")

    # 4. the-alpha-tree.html
    alpha_tree_html = f"""<!doctype html><html lang="en" data-article-status="curated"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>The Alpha Tree — Somnarak Wiki</title><meta name="description" content="Structural, biological, and energetic analysis of the Alpha Tree and the root facility"><link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg"><link rel="stylesheet" href="../assets/css/wiki.css"><script defer src="../assets/js/wiki.js"></script></head><body>
{get_header()}
<nav class="float-toc" aria-label="On this page"><button type="button" aria-expanded="false">CONTENTS</button><div><strong>ON THIS PAGE</strong><ol><li class="l2"><a href="#overview">Overview</a></li><li class="l2"><a href="#botanical-profile">Botanical Profile</a></li><li class="l2"><a href="#structural-anatomy">Structural Anatomy</a></li><li class="l2"><a href="#the-root-network-and-the-hand">The Root Network &amp; The Hand</a></li><li class="l2"><a href="#crystalline-sap-and-energy">Crystalline Sap &amp; Energy</a></li><li class="l2"><a href="#the-crown-and-the-dawn">The Crown &amp; The Dawn</a></li></ol><a href="#content">↑ TOP</a></div></nav>
<div class="wiki-shell">
{get_left_rail()}
<main id="content"><div class="page-tabs"><span>Lore &amp; Cosmology</span><b>STRUCTURAL MONUMENT</b></div><div class="breadcrumbs"><a href="../index.html">Main page</a><i>›</i><a href="index.html">Lore &amp; Cosmology</a><i>›</i>The Alpha Tree</div>
<section class="department-hero" style="--floor:#47c978"><img src="../assets/layout/city/icons/icon_alpha_tree.svg" alt=""><div><span>MONUMENT CODEX · ZONE A CORE</span><h1>The Alpha Tree</h1><p>알파 나무 — Alpha Namu</p></div></section>
<blockquote class="motto" style="--floor:#47c978">“It does not drink water from the soil; it drinks memory from the stone. Cut into its bark, and the wound sings before it bleeds.” — Insight Forge Field Notes</blockquote>
<section class="department-overview"><div><h2 id="overview">Overview</h2><p class="lead"><strong>The Alpha Tree</strong> (알파 나무) is the colossal crystalline botanical monument standing at the geographic and metaphysical center of Somnarak in Zone A. Rising over 1,400 meters into the sky and extending roots miles into the subterranean mantle, the Tree serves as the physical spine around which all five metropolitan zones are organized.</p><p>Neither purely organic plant nor mineral crystal, the Alpha Tree metabolizes the liquid grief of the Weeping through its root tendrils, filtering erratic emotional frequencies and exuding stabilized crystalline sap that powers the entire city.</p></div><aside class="department-profile" style="--floor:#47c978"><h2 id="botanical-profile">Structural Profile</h2><dl><dt>Designation</dt><dd>The Alpha Tree (Central Spire)</dd><dt>Height</dt><dd>1,420 meters above ground level</dd><dt>Root Depth</dt><dd>Over 4,800 meters into sub-mantle</dd><dt>Composition</dt><dd>Silicate-lignin crystal hybrid</dd><dt>Metabolic Input</dt><dd>The Weeping River (Subterranean)</dd><dt>Energy Output</dt><dd>Refined Han-Resonance (50,000+ MWh equiv)</dd><dt>Current Status</dt><dd>Awakened · Emitting Dawn Aurora</dd></dl></aside></section>
<article class="article-body">
<h2 id="structural-anatomy">Structural Anatomy</h2>
<p>The Tree is divided into three major structural tiers:</p>
<ul>
<li><strong>The Crown (Zone A Sky Spire):</strong> The upper crystalline boughs that pierce the cloud ceiling, acting as the city’s primary lightning rod and resonance broadcaster. During the Dawn Initiative, the Crown serves as the focal point for the golden Hand of Hope aurora.</li>
<li><strong>The Trunk (Zone A Municipal Core):</strong> The massive central column, over 300 meters in diameter, wrapped in the spiraling terraces of the Council of Sighs, High Architect studios, and government administrative spires.</li>
<li><strong>The Root System (The Deep Hand):</strong> The sprawling subterranean root mass where the Reverie Directorate constructed the eight operational floors of the Hand of Change.</li>
</ul>

<h2 id="the-root-network-and-the-hand">The Root Network &amp; The Hand</h2>
<p>The facility known as the Hand of Change is not built of poured concrete or steel beams; its hallways and chambers were excavated directly into the living, petrified root timber of the Alpha Tree. This organic-mineral matrix provides unmatched shock absorption against seismic tremors caused by Colossus entity migrations and naturally insulates containment cells against psychic bleed-through.</p>

<h2 id="crystalline-sap-and-energy">Crystalline Sap &amp; Energy</h2>
<p>As the roots drink from the Weeping, the tree filters raw agony through microscopic cellular sieves, precipitating <strong>Alpha Sap</strong>—a warm, amber-blue luminescent fluid. When refined by Floor 3 (Extraction Hall), this sap crystallizes into standard Han-Energy fuel cells used across all city districts.</p>

<h2 id="the-crown-and-the-dawn">The Crown &amp; The Dawn</h2>
<p>Following the Absolvohan discharge on Day 365, the Alpha Tree underwent a permanent biological metamorphosis. Its foliage, formerly a somber translucent violet, turned brilliant amber-gold, and its canopy now produces a continuous micro-climate of gentle warmth that shields Zone A and B from the bitter freezing winds of the Desolate.</p>
</article>
<nav class="article-nav"><a href="the-cycle-and-absolvohan.html">← The Cycle &amp; Absolvohan</a><a href="the-cheongula-incident.html">The Cheongula Incident →</a></nav>
</main>
{get_floor_rail()}
</div>
{get_footer()}
</body></html>"""

    with open(os.path.join(LORE_DIR, "the-alpha-tree.html"), "w", encoding="utf-8") as f:
        f.write(alpha_tree_html)
    print("Generated lore/the-alpha-tree.html")

    # 5. the-cheongula-incident.html
    cheongula_html = f"""<!doctype html><html lang="en" data-article-status="curated"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>The Cheongula Incident (The First Sorrow) — Somnarak Wiki</title><meta name="description" content="Chronicle of the historical disaster in Year 180 that shattered Zone B and created the Maw"><link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg"><link rel="stylesheet" href="../assets/css/wiki.css"><script defer src="../assets/js/wiki.js"></script></head><body>
{get_header()}
<nav class="float-toc" aria-label="On this page"><button type="button" aria-expanded="false">CONTENTS</button><div><strong>ON THIS PAGE</strong><ol><li class="l2"><a href="#overview">Overview</a></li><li class="l2"><a href="#incident-profile">Incident Profile</a></li><li class="l2"><a href="#the-founding-context-year-0-180">The Founding Context (Year 0–180)</a></li><li class="l2"><a href="#the-17-minute-resonance-surge">The 17-Minute Resonance Surge</a></li><li class="l2"><a href="#the-great-screaming-and-collapse">The Great Screaming &amp; Collapse</a></li><li class="l2"><a href="#aftermath-creation-of-the-maw">Aftermath &amp; Creation of The Maw</a></li></ol><a href="#content">↑ TOP</a></div></nav>
<div class="wiki-shell">
{get_left_rail()}
<main id="content"><div class="page-tabs"><span>Lore &amp; Cosmology</span><b>HISTORICAL CATASTROPHE</b></div><div class="breadcrumbs"><a href="../index.html">Main page</a><i>›</i><a href="index.html">Lore &amp; Cosmology</a><i>›</i>The Cheongula Incident</div>
<section class="department-hero" style="--floor:#8d2e42"><img src="../assets/icons/ref_cheongula.svg" alt=""><div><span>CATASTROPHE DOSSIER · YEAR 180</span><h1>The Cheongula Incident</h1><p>청굴아 참사 — Cheongula Chamsa (The First Sorrow)</p></div></section>
<blockquote class="motto" style="--floor:#8d2e42">“For seventeen minutes, no one could speak because the ground itself was screaming the names of the dead. When silence returned, Zone B was gone.” — Archive Record 001-A</blockquote>
<section class="department-overview"><div><h2 id="overview">Overview</h2><p class="lead"><strong>The Cheongula Incident</strong> (청굴아 참사), also remembered as <em>The First Sorrow</em>, was the catastrophic industrial and metaphysical disaster that occurred on the 14th day of the 8th Month in <strong>Year 180</strong>. Triggered by the over-extraction of raw Han from the subterranean fissures beneath Western Zone B, the incident caused the immediate physical and psychological collapse of thirty city blocks.</p><p>The event opened the bottomless geological chasm known today as <strong>The Maw</strong> (입구), claimed over 22,000 lives in under twenty minutes, and forced the founding of the Reverie Directorate to replace unregulated municipal mining.</p></div><aside class="department-profile" style="--floor:#8d2e42"><h2 id="incident-profile">Incident Profile</h2><dl><dt>Catastrophe Title</dt><dd>The Cheongula Incident (청굴아)</dd><dt>Date</dt><dd>Year 180 · Month 8, Day 14</dd><dt>Duration</dt><dd>17 minutes (Resonance Surge)</dd><dt>Casualties</dt><dd>22,410 confirmed deceased / fractured</dd><dt>Geological Result</dt><dd>Formation of The Maw in Zone B</dd><dt>Institutional Result</dt><dd>Establishment of Reverie Directorate</dd><dt>Direct SE Spawns</dt><dd>SE-001 (Bell), SE-011 (Walls), SE-1003 (Maw)</dd></dl></aside></section>
<article class="article-body">
<h2 id="the-founding-context-year-0-180">The Founding Context (Year 0–180)</h2>
<p>Following the founding of Somnarak around the Alpha Tree, early municipal mining companies discovered that subterranean rock formations in Western Zone B emitted vast thermal and electrical energy when subjected to mechanical friction. Unaware of the metaphysical nature of Han, commercial consortiums drilled dozens of deep shafts directly into the bedrock above the Weeping River.</p>

<h2 id="the-17-minute-resonance-surge">The 17-Minute Resonance Surge</h2>
<p>At 14:22 on August 14, Shaft 7 breached the primary subterranean reservoir of the Weeping. The high-pressure release of liquid grief did not flood the mines as ordinary water would; instead, it underwent instant acoustic flash-evaporation, releasing a deafening 120-decibel harmonic frequency that resonated with the emotional subconscious of every resident within a five-kilometer radius.</p>
<p>For seventeen agonizing minutes, citizens were paralyzed by involuntary sensory feedback, hearing their own deepest regrets and the collective voices of all who had died in the foundation shafts screaming in perfect unison.</p>

<h2 id="the-great-screaming-and-collapse">The Great Screaming &amp; Collapse</h2>
<p>The intense vibrational energy liquified structural masonry, causing entire apartment blocks, factories, and administrative courts to collapse inward like sand. The structural collapse crushed thousands of trapped miners while instantaneously fracturing the mental composure of rescue workers.</p>

<h2 id="aftermath-creation-of-the-maw">Aftermath &amp; Creation of The Maw</h2>
<p>When the resonance finally subsided, a permanent jagged abyss nearly one kilometer wide yawned where Western Zone B once stood. This crater—named <strong>The Maw</strong> (입구)—became a permanent conduit for raw sorrow and gave birth to Somnarak’s first canonical Sorrow Entities:</p>
<ul>
<li><strong>SE-001 (The Orphaned Bell):</strong> Formed from the shattered bronze bell of the Zone B municipal clock tower that rang continuously during the collapse.</li>
<li><strong>SE-011 (The Whispering Walls):</strong> Formed from the ruins of fractured apartment buildings that permanently retained the auditory memories of the victims.</li>
<li><strong>The Reverie Directorate Mandate:</strong> In response to the horror of Cheongula, the Council of Sighs stripped private mining guilds of all authority and chartered the Directorate to enforce absolute containment protocols.</li>
</ul>
</article>
<nav class="article-nav"><a href="the-alpha-tree.html">← The Alpha Tree</a><a href="index.html">Lore Hub →</a></nav>
</main>
{get_floor_rail()}
</div>
{get_footer()}
</body></html>"""

    with open(os.path.join(LORE_DIR, "the-cheongula-incident.html"), "w", encoding="utf-8") as f:
        f.write(cheongula_html)
    print("Generated lore/the-cheongula-incident.html")

    # 6. lore/index.html (Lore Hub)
    lore_hub_html = f"""<!doctype html><html lang="en" data-article-status="curated"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Lore &amp; Cosmology — Somnarak Wiki</title><meta name="description" content="Comprehensive encyclopedia of Somnarak cosmology, history, the 1,778 Cycles, Han physics, and catastrophes"><link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg"><link rel="stylesheet" href="../assets/css/wiki.css"><script defer src="../assets/js/wiki.js"></script></head><body>
{get_header()}
<nav class="float-toc" aria-label="On this page"><button type="button" aria-expanded="false">CONTENTS</button><div><strong>ON THIS PAGE</strong><ol><li class="l2"><a href="#overview">Overview</a></li><li class="l2"><a href="#core-cosmology">Core Cosmology</a></li><li class="l2"><a href="#historical-chronicles">Historical Chronicles</a></li><li class="l2"><a href="#physical-laws-and-taboos">Physical Laws &amp; Taboos</a></li></ol><a href="#content">↑ TOP</a></div></nav>
<div class="wiki-shell">
{get_left_rail()}
<main id="content"><div class="page-tabs"><span>Lore &amp; Cosmology</span><b>COMPREHENSIVE COMPENDIUM</b></div><div class="breadcrumbs"><a href="../index.html">Main page</a><i>›</i>Lore &amp; Cosmology</div>
<section class="wide-hero"><div><span>SOMNARAK HISTORICAL &amp; COSMIC ARCHIVE</span><h1>Lore &amp; Cosmology</h1><p>세계관과 역사 기록 — Segyegwan-gwa Yeoksa Girok</p></div><img src="../assets/icons/banner_lore.svg" alt="Lore of Somnarak"></section>
<article class="article-body">
<h2 id="overview">Overview</h2>
<p>The universe of Somnarak operates under strict metaphysical and cosmological laws where human sorrow, memory, and emotional debt are concrete physical forces. This compendium synthesizes over four thousand years of documented history, the cosmological physics of Dream and Abyss, the tragedy of the 1,778 Cycles, and the dawn of Year 4,238.</p>

<h2 id="core-cosmology">Core Cosmology</h2>
<div class="contents-grid">
<section>
<h3>Cosmology &amp; Physics</h3>
<a href="somnarak-cosmology.html"><strong>Somnarak Cosmology</strong><br><small>Dream (Somnus) &amp; Abyss (Narak), The Weeping foundation</small></a>
<a href="the-three-sorrows.html"><strong>The Three Sorrows (Samhan)</strong><br><small>City (Dohan), Outside (Oehan), and Inner (Naehan)</small></a>
<a href="the-alpha-tree.html"><strong>The Alpha Tree</strong><br><small>The 1,400m central crystalline spine and root facility</small></a>
</section>
<section>
<h3>Historical Eras</h3>
<a href="the-cycle-and-absolvohan.html"><strong>The Cycle &amp; Absolvohan</strong><br><small>The 1,778 iterations, hidden reserve, and Hand of Hope</small></a>
<a href="the-cheongula-incident.html"><strong>The Cheongula Incident</strong><br><small>The Year 180 catastrophe, 17-minute surge, and The Maw</small></a>
<a href="../atlas/somnarak-city-map.html"><strong>Metropolitan Atlas</strong><br><small>Zones A–E municipal geography and defensive gates</small></a>
</section>
<section>
<h3>Metaphysical Forces</h3>
<a href="../mechanics/han-energy-and-damage.html"><strong>Han-Energy Physics</strong><br><small>Grudge, Lament, Weight, Void, and Hope signatures</small></a>
<a href="somnarak-cosmology.html#the-seven-taboos"><strong>The Seven Absolute Taboos</strong><br><small>Universal prohibitions against resurrection and tampering</small></a>
<a href="../mechanics/fracture-and-therapy.html"><strong>Psychological Fracture</strong><br><small>Emotional wear, mental breakdown, and recovery pods</small></a>
</section>
<section>
<h3>Current Era (Year 4,238)</h3>
<a href="../departments/index.html"><strong>The Hand of Change</strong><br><small>Reverie Directorate post-Cycle operational doctrine</small></a>
<a href="../characters/kael.html"><strong>The Horizon Caravan</strong><br><small>Expeditions across the Desolate to Unknown Cities</small></a>
<a href="../characters/the-exile-xyan.html"><strong>Gate Watch Return</strong><br><small>Xyan commanding Floor 8 and the perimeter threshold</small></a>
</section>
</div>

<h2 id="historical-chronicles">Historical Chronicles</h2>
<div class="table-wrap"><table class="data-table"><thead><tr><th>Era / Year</th><th>Historical Chronicle</th><th>Cosmological Consequence</th></tr></thead><tbody>
<tr><td><strong>Year 0</strong></td><td><strong>The Founding</strong></td><td>Somnarak established around the Alpha Tree above the Weeping River.</td></tr>
<tr><td><strong>Year 180</strong></td><td><strong>The Cheongula Incident</strong></td><td>Shaft 7 breach creates The Maw; 22,000 lost; Reverie Directorate founded.</td></tr>
<tr><td><strong>Year 2,460</strong></td><td><strong>The Cycle Begins</strong></td><td>Director Majin initiates the 365-day recursion loop to harvest Absolvohan energy.</td></tr>
<tr><td><strong>Cycle 1–1,777</strong></td><td><strong>The Great Recurrence</strong></td><td>1,777 failed iterations; 47.3 tons of crystallized Han secretly stored under Floor 1.</td></tr>
<tr><td><strong>Cycle 1,778 (Day 365)</strong></td><td><strong>The Hand of Hope</strong></td><td>Majin refuses annihilation; Absolvohan discharges upward; 15% sorrow transformed to Hope.</td></tr>
<tr><td><strong>Year 4,238</strong></td><td><strong>Dawn Initiative</strong></td><td>The Cycle ends; Xyan returns to Gate Watch; linear time restored; city rebuilds.</td></tr>
</tbody></table></div>

<h2 id="physical-laws-and-taboos">Physical Laws &amp; Taboos</h2>
<p>In Somnarak, science and grief are inseparable. Han cannot be destroyed, only transformed or channeled through refined M.A.W. equipment and emotional therapy lofts. The city’s survival depends on maintaining the fragile equilibrium between acknowledging past sorrow and moving forward into linear dawn.</p>
</article>
</main>
{get_floor_rail()}
</div>
{get_footer()}
</body></html>"""

    with open(os.path.join(LORE_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(lore_hub_html)
    print("Generated lore/index.html")

build_lore_pages()
