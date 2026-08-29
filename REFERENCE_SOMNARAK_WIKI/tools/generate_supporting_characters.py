import os
import re
from generate_all_characters import get_left_rail, get_floor_rail, get_header, get_footer

CHAR_DIR = "/home/user/01_Somnarak_Wiki/characters"

# 1. Kael
kael_html = f"""<!doctype html><html lang="en" data-article-status="curated"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Kael (The Drift King) — Somnarak Wiki</title><meta name="description" content="Captain of the Horizon Caravan and pioneer of the Desolate Han-flow routes"><link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg"><link rel="stylesheet" href="../assets/css/wiki.css"><script defer src="../assets/js/wiki.js"></script></head><body>
{get_header()}
<nav class="float-toc" aria-label="On this page"><button type="button" aria-expanded="false">CONTENTS</button><div><strong>ON THIS PAGE</strong><ol><li class="l2"><a href="#overview">Overview</a></li><li class="l2"><a href="#profile">Dossier Profile</a></li><li class="l2"><a href="#the-horizon-caravan">The Horizon Caravan</a></li><li class="l2"><a href="#the-drift-throne">The Drift Throne</a></li><li class="l2"><a href="#combat-tactics-and-identities">Combat Tactics &amp; Identities</a></li><li class="l2"><a href="#relationships">Relationships &amp; Routes</a></li></ol><a href="#content">↑ TOP</a></div></nav>
<div class="wiki-shell">
{get_left_rail()}
<main id="content"><div class="page-tabs"><span>Characters</span><b>FIELD EXPEDITION</b></div><div class="breadcrumbs"><a href="../index.html">Main page</a><i>›</i><a href="index.html">Characters</a><i>›</i>Kael</div>
<section class="department-hero" style="--floor:#e8c25a"><img src="../assets/icons/ref_horizon_caravan.svg" alt=""><div><span>HORIZON CARAVAN · CAPTAIN</span><h1>Kael</h1><p>카엘 — 표류왕 (The Drift King)</p></div></section>
<blockquote class="motto" style="--floor:#e8c25a">“The city thinks it is the world. It is not. The world is larger than any city. And someone has to cross it.” — Kael</blockquote>
<section class="department-overview"><div><h2 id="overview">Overview</h2><p class="lead"><strong>Kael</strong> (카엘), titled <strong>The Drift King</strong> (漂流王 — <em>Hyouryuou</em>), is the commander of the <strong>Horizon Caravan</strong> (지평선 대 — <em>Jipyeongseon Dae</em>) in Year 4,238. Operating in parallel with the Directorate’s Dawn Initiative, Kael commands the <em>Drift Throne</em>—a massive reinforced crawler designed to navigate the shifting Han-tides across the Desolate between Somnarak, Cheonbulok, and the unknown corners of Mugenhan.</p><p>Born in the harsh outer perimeter of Zone E, Kael spent two decades mapping the migration paths of Outside Sorrow Entities. Rather than retreating behind the Aegis Veil, he proved that resonance anchors could allow a mobile expedition to survive indefinitely beyond the metropolitan wall.</p></div><aside class="department-profile" style="--floor:#e8c25a"><h2 id="profile">Dossier Profile</h2><dl><dt>Real Name</dt><dd>Kael (카엘)</dd><dt>Title</dt><dd>The Drift King / Caravan Captain</dd><dt>Affiliation</dt><dd>Horizon Caravan (Company 3) / SED Ally</dd><dt>Origin</dt><dd>Zone E Perimeter Bulwark</dd><dt>Signature</dt><dd>Weight (Black) + Hope (Gold)</dd><dt>Vehicle</dt><dd>The Drift Throne (Han-Crawler)</dd><dt>Primary Weapon</dt><dd>Han-Tempered Anchor Pike</dd><dt>Current Status</dt><dd>Active — Desolate Transit (Year 4,238)</dd></dl></aside></section>
<article class="article-body">
<h2 id="the-horizon-caravan">The Horizon Caravan</h2>
<p>Following the Absolvohan release on Day 365, approximately 15% of ambient sorrow transformed into Hope-gold resonance. While the Directorate focused inward on department restructuring and containment stability, Kael organized the Horizon Caravan to break the isolation separating Somnarak from the other surviving metropolitan centers of Mugenhan.</p>
<p>The Caravan operates under three strict expeditionary mandates:</p>
<ul>
<li><strong>Establish the Desolate Highway:</strong> Anchor permanent relay beacons along the Han-flow lines connecting Zone E to Corner 2 (Cheonbulok).</li>
<li><strong>Rescue Stranded Wanderers:</strong> Provide medical aid, Han-stasis stabilization, and extraction for wanderers and Menders trapped in the liminal wastes.</li>
<li><strong>Recover Pre-Cycle Relics:</strong> Retrieve lost technology and historical archives from abandoned research outposts that predate the 1,778 Cycles.</li>
</ul>

<h2 id="the-drift-throne">The Drift Throne</h2>
<p>The flagship of the Caravan is the <strong>Drift Throne</strong>, a mobile fortress built on crawler tracks and stabilized by four massive Han-dispersion skids. Engineered in collaboration with sympathetic Forge artisans and Underworld Menders, the vehicle generates an artificial micro-Veil that repels low-tier Outside Sorrow Entities like Brume drifts and Void echoes.</p>
<div class="table-wrap"><table class="data-table"><thead><tr><th>Component</th><th>Technical Specification</th><th>Operational Role</th></tr></thead><tbody><tr><td><strong>Han-Drive Core</strong></td><td>Dual-chamber resonance reactor powered by refined Gold/Weight crystals</td><td>Provides continuous propulsion and shield barrier power</td></tr><tr><td><strong>Anchor Skids</strong></td><td>Deployable ground stakes forged from hardened Ferrehan alloys</td><td>Stabilizes the vehicle during violent Sorrow Sandstorms</td></tr><tr><td><strong>Echo Hydro-Beds</strong></td><td>Infirmary pods utilizing diluted Weeping fluid for cellular regeneration</td><td>Heals severe Fracture trauma and Han-burns</td></tr><tr><td><strong>Beacon Launcher</strong></td><td>Pneumatic mortar firing resonant relay pylons</td><td>Marks navigable channels across shifting terrain</td></tr></tbody></table></div>

<h2 id="combat-tactics-and-identities">Combat Tactics &amp; Identities</h2>
<p>Kael fights with a modified <strong>Anchor Pike</strong>, utilizing heavy physical Weight strikes combined with directional Hope bursts to break enemy poise and shatter crystalline shells. In combat encounters, he coordinates the Caravan’s diverse specialists through distinct tactical stances:</p>
<ul>
<li><strong>Vanguard Breaker:</strong> Frontline stance prioritizing parrying heavy attacks from Colossus-class entities.</li>
<li><strong>Wayfinder Command:</strong> Midline tactical posture granting morale buffs and Fracture resistance to Caravan allies.</li>
<li><strong>Hope Vanguard (Awakened):</strong> Unleashes stored Absolvohan resonance, temporarily turning the Anchor Pike into a blazing golden conduit that cleanses despair.</li>
</ul>

<h2 id="relationships">Relationships &amp; Routes</h2>
<p><strong>Xyan (Echo-Core 9):</strong> Kael holds deep respect for the Exile. When Xyan guarded the Outer Gate alone, Kael was one of the few caravan runners permitted to transmit supplies and status reports across the perimeter threshold.</p>
<p><strong>Mellda (Echo-Core 6):</strong> Mellda maintains formal jurisdiction over Zone E, occasionally issuing border permits to Kael while cautioning him against venturing too close to the Seething Tundra.</p>
<p><strong>Director Majin:</strong> Kael views the Directorate with cautious pragmatism, accepting their equipment commissions while rejecting any central command over Caravan operations.</p>
</article>
<nav class="article-nav"><a href="the-exile-xyan.html">← Xyan, the Exile</a><a href="soojin.html">Soojin, Master Weaver →</a></nav>
</main>
{get_floor_rail()}
</div>
{get_footer()}
</body></html>"""

with open(os.path.join(CHAR_DIR, "kael.html"), "w", encoding="utf-8") as f:
    f.write(kael_html)
print("Generated kael.html")

# 2. Soojin
soojin_html = f"""<!doctype html><html lang="en" data-article-status="curated"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Soojin (Master Weaver) — Somnarak Wiki</title><meta name="description" content="Master Weaver of the Echo Gardens and specialist in resonance attunement"><link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg"><link rel="stylesheet" href="../assets/css/wiki.css"><script defer src="../assets/js/wiki.js"></script></head><body>
{get_header()}
<nav class="float-toc" aria-label="On this page"><button type="button" aria-expanded="false">CONTENTS</button><div><strong>ON THIS PAGE</strong><ol><li class="l2"><a href="#overview">Overview</a></li><li class="l2"><a href="#profile">Dossier Profile</a></li><li class="l2"><a href="#the-weaving-arts">The Weaving Arts</a></li><li class="l2"><a href="#the-echo-gardens">The Echo Gardens</a></li><li class="l2"><a href="#role-in-underworld-cleanup">Role in Underworld Cleanup (UCD)</a></li><li class="l2"><a href="#equipment-and-resonance">Equipment &amp; Resonance</a></li></ol><a href="#content">↑ TOP</a></div></nav>
<div class="wiki-shell">
{get_left_rail()}
<main id="content"><div class="page-tabs"><span>Characters</span><b>RESONANCE ARTISAN</b></div><div class="breadcrumbs"><a href="../index.html">Main page</a><i>›</i><a href="index.html">Characters</a><i>›</i>Soojin</div>
<section class="department-hero" style="--floor:#83d6ad"><img src="../assets/icons/fac_weavers.svg" alt=""><div><span>WEAVER GUILD · MASTER ARTISAN</span><h1>Soojin</h1><p>수진 — 직조 명인 (Master Weaver)</p></div></section>
<blockquote class="motto" style="--floor:#83d6ad">“Grief is not a wound to be stitched shut and forgotten. It is a thread. Weave it true, and it becomes armor.” — Soojin</blockquote>
<section class="department-overview"><div><h2 id="overview">Overview</h2><p class="lead"><strong>Soojin</strong> (수진) is the leading artisan of the <strong>Weaver Guild</strong> in the Echo Gardens of Zone D. Renowned throughout Somnarak as the foremost living authority on Han-filament manipulation and emotional harmonic tuning, Soojin bridges the delicate divide between artistic expression and tactical defense.</p><p>Her specialized techniques allow raw grief, remorse, and unexpressed longing to be spun into flexible crystalline fibers. These fibers form the protective under-linings of all high-tier M.A.W. Suits and provide the acoustic shielding used in the Directorate’s Deep Vault.</p></div><aside class="department-profile" style="--floor:#83d6ad"><h2 id="profile">Dossier Profile</h2><dl><dt>Real Name</dt><dd>Soojin (수진)</dd><dt>Title</dt><dd>Master Weaver / Echo Singer</dd><dt>Affiliation</dt><dd>The Weavers of the Echo Gardens / UCD Taskforce</dd><dt>Station</dt><dd>Zone D — Echo Gardens &amp; Loom Spires</dd><dt>Signature</dt><dd>Lament (Deep Blue) + Void (Pale White)</dd><dt>Primary Tool</dt><dd>Resonant Silver Shuttle &amp; Tuning Harp</dd><dt>Specialty</dt><dd>Emotional Threading &amp; Fracture Repair</dd><dt>Current Status</dt><dd>Active — Master Guild Counselor</dd></dl></aside></section>
<article class="article-body">
<h2 id="the-weaving-arts">The Weaving Arts</h2>
<p>Unlike metal-forging in the Insight Forge, Weaving operates on the subtle acoustic resonance of Han. When a citizen experiences overwhelming sorrow or undergoes severe mental Fracture, their emotional emission manifests as unstable microscopic filaments. Without intervention, these threads tangle, inducing localized spatial distortions or giving rise to Minor Object Entities.</p>
<p>Master Soojin developed the <strong>Seven Harmonic Looms</strong>, mechanical weaving stations equipped with acoustic dampeners that capture ambient filaments and align their emotional polarity:</p>
<ul>
<li><strong>Lament Threads (Deep Blue):</strong> Spun from tears and sorrow; exhibits extreme tensile strength and shock dissipation.</li>
<li><strong>Grudge Threads (Crimson):</strong> Spun from anger and injustice; retains sharp thermal conductivity and kinetic feedback.</li>
<li><strong>Hope Threads (Gold):</strong> Spun from post-Cycle dawn resonance; accelerates natural biological healing and mental stabilization.</li>
</ul>

<h2 id="the-echo-gardens">The Echo Gardens</h2>
<p>Soojin oversees the botanical and acoustic sanctuaries located in the inner terracing of Zone D. In the Echo Gardens, weeping willows and crystalline reeds grow along runoff streams originating from the Alpha Tree. These flora absorb ambient noise from the Forge and convert erratic city noise into soft, harmonious tones where recovering personnel rest.</p>

<h2 id="role-in-underworld-cleanup">Role in Underworld Cleanup (UCD)</h2>
<p>During the Underworld Cleanup Descend (UCD) operations beneath Zone B and C, Soojin served as chief resonance consultant. She designed portable dampening screens that shielded cleanup crews from the lethal sonic frequencies emitted by rogue acoustic entities like SE-021 (Hollow Choir) and SE-1013 (Undersong).</p>

<h2 id="equipment-and-resonance">Equipment &amp; Resonance</h2>
<p>Soojin wears the custom-crafted <strong>Silken Mantle of Sighs</strong>, a multi-layered garment woven from three generations of her family’s refined Lament threads. In her hands, the <strong>Resonant Silver Shuttle</strong> functions both as a delicate precision loom needle and a defensive rapier capable of severing hostile psychic tethers.</p>
</article>
<nav class="article-nav"><a href="kael.html">← Kael, the Drift King</a><a href="cheonbulok-refugees.html">Cheonbulok Refugees →</a></nav>
</main>
{get_floor_rail()}
</div>
{get_footer()}
</body></html>"""

with open(os.path.join(CHAR_DIR, "soojin.html"), "w", encoding="utf-8") as f:
    f.write(soojin_html)
print("Generated soojin.html")

# 3. Cheonbulok Refugees
cheon_html = f"""<!doctype html><html lang="en" data-article-status="curated"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Cheonbulok Refugees &amp; Desolate Wanderers — Somnarak Wiki</title><meta name="description" content="Chronicle and demographic dossier of the survivors arriving from Corner 2 (The City of a Thousand Rages)"><link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg"><link rel="stylesheet" href="../assets/css/wiki.css"><script defer src="../assets/js/wiki.js"></script></head><body>
{get_header()}
<nav class="float-toc" aria-label="On this page"><button type="button" aria-expanded="false">CONTENTS</button><div><strong>ON THIS PAGE</strong><ol><li class="l2"><a href="#overview">Overview</a></li><li class="l2"><a href="#profile">Dossier Profile</a></li><li class="l2"><a href="#corner-2-the-city-of-a-thousand-rages">Corner 2 — The City of a Thousand Rages</a></li><li class="l2"><a href="#the-great-migration">The Great Migration</a></li><li class="l2"><a href="#settlement-in-zone-d-and-the-mantle">Settlement in Zone D &amp; The Mantle</a></li><li class="l2"><a href="#social-integration-and-conflict">Social Integration &amp; Conflict</a></li></ol><a href="#content">↑ TOP</a></div></nav>
<div class="wiki-shell">
{get_left_rail()}
<main id="content"><div class="page-tabs"><span>Characters</span><b>DEMOGRAPHIC COHORT</b></div><div class="breadcrumbs"><a href="../index.html">Main page</a><i>›</i><a href="index.html">Characters</a><i>›</i>Cheonbulok Refugees</div>
<section class="department-hero" style="--floor:#d67d32"><img src="../assets/icons/ref_unknown_cities.svg" alt=""><div><span>MUGENHAN · IMMIGRANT COHORT</span><h1>Cheonbulok Refugees</h1><p>천불록 피난민 — Cheonbulok Pinanmin</p></div></section>
<blockquote class="motto" style="--floor:#d67d32">“Somnarak weeps its sorrow into the river. In Cheonbulok, we burned our sorrow until the sky turned black. Neither city learned to stop.” — Elder Bak, Furnace Clan</blockquote>
<section class="department-overview"><div><h2 id="overview">Overview</h2><p class="lead">The <strong>Cheonbulok Refugees</strong> (천불록 피난민) represent the largest external demographic influx into Somnarak since the Founding Era. Originating from <strong>Corner 2 of Mugenhan</strong>—the legendary subterranean industrial metropolis known as <em>The City of a Thousand Rages</em>—these survivors navigated the hazardous expanse of the Desolate on foot and aboard jury-rigged scrap crawlers.</p><p>Possessing unique physiological adaptations to volcanic heat and high Grudge concentrations, the refugees have fundamentally transformed the industrial landscape of Zone D (The Mantle) and sparked complex political negotiations within the Council of Sighs.</p></div><aside class="department-profile" style="--floor:#d67d32"><h2 id="profile">Dossier Profile</h2><dl><dt>Designation</dt><dd>External Immigrant Demographic</dd><dt>Origin City</dt><dd>Cheonbulok (Corner 2 of Mugenhan)</dd><dt>Primary Location</dt><dd>Zone D — Furnace Ward &amp; Outer Slums</dd><dt>Signature Element</dt><dd>Grudge (Crimson) + Weight (Black)</dd><dt>Key Leaders</dt><dd>Elder Bak, Mara the Mender, Captain Jin</dd><dt>Population Count</dt><dd>~14,200 documented arrivals</dd><dt>Current Status</dt><dd>Integrated Provisional Citizenship</dd></dl></aside></section>
<article class="article-body">
<h2 id="corner-2-the-city-of-a-thousand-rages">Corner 2 — The City of a Thousand Rages</h2>
<p>Unlike Somnarak, which was built around the living biological roots of the Alpha Tree and the liquid grief of the Weeping, Cheonbulok was constructed inside a massive subterranean magma chamber. Its civil architecture was driven by <strong>Volcanic Han-Engines</strong> that metabolized unbridled fury, resentment, and generational grudge into pure kinetic energy.</p>
<p>When the Great Rupture fractured Cheonbulok’s thermal containment seals in Year 4,210, millions of tons of superheated molten slag flooded the lower tiers, forcing the surviving clans into a desperate exodus across the freezing Desolate tundra.</p>

<h2 id="the-great-migration">The Great Migration</h2>
<p>For twenty-eight years, caravan columns trekked through the lethal Outside Sorrow zones. Many perished from cold or were consumed by roaming Void entities like SE-007 (Brume). The survivors who reached Somnarak’s Western Bulwark were hardened survivalists with profound knowledge of slag-tempering, kinetic bracing, and heat-resistant metallurgy.</p>

<h2 id="settlement-in-zone-d-and-the-mantle">Settlement in Zone D &amp; The Mantle</h2>
<p>Upon arrival at Gate 4, the Directorate and Council granted provisional asylum, establishing the <strong>Furnace Ward</strong> in the lower industrial tier of Zone D. Here, refugee smiths revitalized Somnarak’s heavy manufacturing sector, introducing the <em>Crimson Slag-Forging</em> technique that dramatically increased the durability of M.A.W. weapon housings.</p>

<h2 id="social-integration-and-conflict">Social Integration &amp; Conflict</h2>
<p>Despite their industrial contributions, tensions persist between Somnarak natives and Cheonbulok arrivals:</p>
<ul>
<li><strong>Philosophical Divergence:</strong> Somnarak culture treats sorrow with contemplative mourning and quiet remembrance; Cheonbulok survivors channel it into fiery defiance and outward labor.</li>
<li><strong>Collector Disputes:</strong> The Collectors of Zone C have repeatedly attempted to impose municipal debt liens on arriving families, resulting in fierce resistance from refugee Mender militias.</li>
<li><strong>Directorate Collaboration:</strong> Floor 4 (Insight Forge) and Floor 5 (Border Watch) actively recruit Cheonbulok veterans for high-temperature research and outer perimeter expeditions.</li>
</ul>
</article>
<nav class="article-nav"><a href="soojin.html">← Soojin, Master Weaver</a><a href="high-architects.html">The High Architects →</a></nav>
</main>
{get_floor_rail()}
</div>
{get_footer()}
</body></html>"""

with open(os.path.join(CHAR_DIR, "cheonbulok-refugees.html"), "w", encoding="utf-8") as f:
    f.write(cheon_html)
print("Generated cheonbulok-refugees.html")

# 4. High Architects
arch_html = f"""<!doctype html><html lang="en" data-article-status="curated"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>The High Architects — Somnarak Wiki</title><meta name="description" content="The structural masterminds and city planners who designed Somnarak and the Hand of Change"><link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg"><link rel="stylesheet" href="../assets/css/wiki.css"><script defer src="../assets/js/wiki.js"></script></head><body>
{get_header()}
<nav class="float-toc" aria-label="On this page"><button type="button" aria-expanded="false">CONTENTS</button><div><strong>ON THIS PAGE</strong><ol><li class="l2"><a href="#overview">Overview</a></li><li class="l2"><a href="#profile">Dossier Profile</a></li><li class="l2"><a href="#the-architectural-canon">The Architectural Canon</a></li><li class="l2"><a href="#founding-masters">Founding Masters</a></li><li class="l2"><a href="#engineering-the-hand-of-change">Engineering the Hand of Change</a></li><li class="l2"><a href="#the-sorrow-compass-and-masonry">The Sorrow Compass &amp; Masonry</a></li></ol><a href="#content">↑ TOP</a></div></nav>
<div class="wiki-shell">
{get_left_rail()}
<main id="content"><div class="page-tabs"><span>Characters</span><b>CIVIL GUILD LEADERSHIP</b></div><div class="breadcrumbs"><a href="../index.html">Main page</a><i>›</i><a href="index.html">Characters</a><i>›</i>The High Architects</div>
<section class="department-hero" style="--floor:#f1df76"><img src="../assets/icons/fac_architects.svg" alt=""><div><span>GUILD OF ARCHITECTS · COUNCIL OF MASTERS</span><h1>The High Architects</h1><p>대건축가 연합 — Daegeonchukga Yeonhap</p></div></section>
<blockquote class="motto" style="--floor:#f1df76">“To lay a stone in Somnarak is to make a covenant with gravity and grief. If the foundation does not breathe, the Han will shatter the wall.” — Master Orak</blockquote>
<section class="department-overview"><div><h2 id="overview">Overview</h2><p class="lead"><strong>The High Architects</strong> (대건축가 연합) are the elite guild of structural engineers, geometricians, and Han-channeling master builders who designed the urban grid of Somnarak and the subterranean complex of the Hand of Change. Working at the intersection of classical masonry and sorrow physics, they engineered the city to survive the immense tectonic and psychic pressure exerted by the Alpha Tree and the Weeping.</p><p>From the crystalline spire of Zone A to the cyclopean bulwarks of Zone E, every wall, archway, conduit, and containment chamber was drafted under the strict geometric canons of the Architects.</p></div><aside class="department-profile" style="--floor:#f1df76"><h2 id="profile">Dossier Profile</h2><dl><dt>Guild Title</dt><dd>The High Architects (대건축가)</dd><dt>Headquarters</dt><dd>Zone A — The Spire of Plumb Lines</dd><dt>Governing Body</dt><dd>The Triad of the Trowel</dd><dt>Signature Element</dt><dd>Weight (Black) + Clarity (White)</dd><dt>Primary Instruments</dt><dd>The Sorrow Compass &amp; Resonant Plumb</dd><dt>Key Figures</dt><dd>Master Orak, The Blind Architect (Nunmeon), Ilan</dd><dt>Current Doctrine</dt><dd>Dawn Reconstructive Expansion</dd></dl></aside></section>
<article class="article-body">
<h2 id="the-architectural-canon">The Architectural Canon</h2>
<p>Building in Somnarak differs fundamentally from conventional construction. Because Han flows through solid matter like groundwater through porous limestone, an unshielded masonry wall will gradually absorb emotional resonance until it manifests structural crying, warping, or auditory echoes (as seen in SE-011, The Whispering Walls).</p>
<p>To prevent municipal degeneration, the High Architects instituted the <strong>Four Building Principles</strong>:</p>
<div class="table-wrap"><table class="data-table"><thead><tr><th>Principle</th><th>Architectural Rule</th><th>Structural Purpose</th></tr></thead><tbody><tr><td><strong>Porous Alignment</strong></td><td>Every foundation must maintain micro-channels parallel to the natural flow of the Weeping</td><td>Prevents pressure buildup that leads to spontaneous Object SE manifestation</td></tr><tr><td><strong>Harmonic Bracing</strong></td><td>Load-bearing pillars must incorporate acoustic counter-weights</td><td>Dampens low-frequency vibrations generated by Colossus migration</td></tr><tr><td><strong>Crystalline Glazing</strong></td><td>Interior walls in containment zones must be lined with refined Void-glass</td><td>Reflects and isolates volatile psychic radiation</td></tr><tr><td><strong>Sacrificial Joints</strong></td><td>Sections adjacent to the Maw are engineered with rapid-collapse shear pins</td><td>Enables instant physical isolation during catastrophic breach events</td></tr></tbody></table></div>

<h2 id="founding-masters">Founding Masters</h2>
<p><strong>Master Orak (The First Mason):</strong> Chief engineer of the Founding Era who drafted the concentric five-zone circular plan centered on the Alpha Tree.</p>
<p><strong>The Blind Architect (Nunmeon Geonchukga):</strong> A legendary figure who lost his sight during the Cheongula Incident. He possesses the supernatural ability to feel Han-stress lines through the soles of his feet, guiding the reinforcement of the lower Deep Vault chambers.</p>
<p><strong>Senior Surveyor Ilan:</strong> The contemporary guild representative overseeing the reconstruction of Zone D’s outer perimeter during the Dawn Initiative.</p>

<h2 id="engineering-the-hand-of-change">Engineering the Hand of Change</h2>
<p>The facility known as the Hand of Change represents the crowning masterpiece of Architect engineering. Carved directly into the root network of the Alpha Tree, the facility spans eight distinct operational floors configured in an anatomical hand layout. The Palm (Floors 1–3) anchors central mass and containment, the Fingers (Floors 4–7) extend outward into specialized rock strata, and the Wing (Floor 8) projects laterally toward the boundary of the Desolate.</p>

<h2 id="the-sorrow-compass-and-masonry">The Sorrow Compass &amp; Masonry</h2>
<p>Every accredited Architect carries the <strong>Sorrow Compass</strong> (한의 나침반), a gyroscopic brass instrument with a needle suspended in purified Weeping mineral oil. The needle points not toward magnetic north, but toward the nearest concentration of unresolved psychic mass, allowing surveyors to avoid building atop latent entity spawn points.</p>
</article>
<nav class="article-nav"><a href="cheonbulok-refugees.html">← Cheonbulok Refugees</a><a href="index.html">Characters Hub →</a></nav>
</main>
{get_floor_rail()}
</div>
{get_footer()}
</body></html>"""

with open(os.path.join(CHAR_DIR, "high-architects.html"), "w", encoding="utf-8") as f:
    f.write(arch_html)
print("Generated high-architects.html")

# 5. Characters Hub (characters/index.html)
hub_html = f"""<!doctype html><html lang="en" data-article-status="curated"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Characters &amp; Figures — Somnarak Wiki</title><meta name="description" content="Comprehensive directory of the Nine Echo-Cores, Directorate leadership, guild masters, and notable figures of Somnarak"><link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg"><link rel="stylesheet" href="../assets/css/wiki.css"><script defer src="../assets/js/wiki.js"></script></head><body>
{get_header()}
<nav class="float-toc" aria-label="On this page"><button type="button" aria-expanded="false">CONTENTS</button><div><strong>ON THIS PAGE</strong><ol><li class="l2"><a href="#overview">Overview</a></li><li class="l2"><a href="#the-nine-echo-cores">The Nine Echo-Cores</a></li><li class="l2"><a href="#command-directory">Command Directory</a></li><li class="l2"><a href="#civic-and-field-figures">Civic &amp; Field Figures</a></li><li class="l2"><a href="#demographic-cohorts">Demographic Cohorts</a></li></ol><a href="#content">↑ TOP</a></div></nav>
<div class="wiki-shell">
{get_left_rail()}
<main id="content"><div class="page-tabs"><span>Characters</span><b>DIRECTORY &amp; DOSSIERS</b></div><div class="breadcrumbs"><a href="../index.html">Main page</a><i>›</i>Characters</div>
<section class="wide-hero"><div><span>SOMNARAK BIOGRAPHICAL REGISTRY</span><h1>Characters &amp; Figures</h1><p>인물 기록소 — Inmul Girokso</p></div><img src="../assets/icons/banner_characters.svg" alt="Characters of Somnarak"></section>
<article class="article-body">
<h2 id="overview">Overview</h2>
<p>The history of Somnarak is recorded not merely in stones and institutional charters, but in the memories, sacrifices, and unbroken resolve of its people. From the supreme command of the Reverie Directorate to the wandering caravan runners traversing the Desolate, this registry chronicles the key figures who shaped the city across 1,778 Cycles and lead the transition into the Dawn Initiative of Year 4,238.</p>

<h2 id="the-nine-echo-cores">The Nine Echo-Cores</h2>
<p>The <strong>Nine Echo-Cores</strong> represent the foundational leadership pillars of the Reverie Directorate. Each Echo-Core commands a designated operational floor within the Hand of Change, embodies a distinct philosophical perspective on sorrow, and carries a unique resonant signature.</p>

<div class="department-directory">
<a href="the-director-majin.html" style="--floor:#ef5b55"><img src="../assets/layout/hand/icons/icon_dept_f1_neutral.svg" alt=""><span>ECHO-CORE 1</span><b>Majin (The Director)</b><small>Supreme Authority · Floor 1 Neutral Command</small></a>
<a href="the-secretary-seiyon.html" style="--floor:#ef5b55"><img src="../assets/layout/hand/icons/icon_dept_f1_neutral.svg" alt=""><span>ECHO-CORE 2</span><b>Seiyon (The Secretary)</b><small>Administrative AI Intelligence · Floor 1</small></a>
<a href="the-containment-lead-dekan.html" style="--floor:#6f7ee8"><img src="../assets/layout/hand/icons/icon_dept_f2_maws_keep.svg" alt=""><span>ECHO-CORE 3</span><b>Dekan (Containment Lead)</b><small>Neokvox · Floor 2 The Maw’s Keep</small></a>
<a href="the-extraction-lead-zyrak.html" style="--floor:#e6c94d"><img src="../assets/layout/hand/icons/icon_dept_f3_extraction.svg" alt=""><span>ECHO-CORE 4</span><b>Zyrak (Extraction Lead)</b><small>Nukimanus · Floor 3 Extraction Hall</small></a>
<a href="the-research-lead-ayshuk.html" style="--floor:#47c978"><img src="../assets/layout/hand/icons/icon_dept_f4_insight_forge.svg" alt=""><span>ECHO-CORE 5</span><b>Ayshuk (Research Lead)</b><small>Kenopathos · Floor 4 Insight Forge</small></a>
<a href="the-border-lead-mellda.html" style="--floor:#d7d7d7"><img src="../assets/layout/hand/icons/icon_dept_f5_border_watch.svg" alt=""><span>ECHO-CORE 6</span><b>Mellda (Border Lead)</b><small>Munkaeri · Floor 5 Border Watch</small></a>
<a href="the-archive-lead-marjuk.html" style="--floor:#8d2e42"><img src="../assets/layout/hand/icons/icon_dept_f6_deep_vault.svg" alt=""><span>ECHO-CORE 7</span><b>Marjuk (Archive Lead)</b><small>Veniago · Floor 6 Deep Vault</small></a>
<a href="the-outsider-ishall.html" style="--floor:#f0a6c4"><img src="../assets/layout/hand/icons/icon_dept_f7_shadow_corps.svg" alt=""><span>ECHO-CORE 8</span><b>Ishall (The Outsider)</b><small>Nemona · Floor 7 Shadow Corps</small></a>
<a href="the-exile-xyan.html" style="--floor:#f4efa0"><img src="../assets/layout/hand/icons/icon_dept_f8_gate_watch.svg" alt=""><span>ECHO-CORE 9</span><b>Xyan (The Exile)</b><small>Sotogil · Floor 8 Gate Watch Command</small></a>
</div>

<h2 id="command-directory">Command Directory</h2>
<div class="table-wrap"><table class="data-table"><thead><tr><th>Core</th><th>Name &amp; Korean</th><th>Office / Designation</th><th>Station / Floor</th><th>Resonant Signature</th></tr></thead><tbody>
<tr><td><strong>1</strong></td><td><a href="the-director-majin.html"><strong>Majin (마진)</strong></a></td><td>The Director (관장)</td><td>Floor 1 · Neutral Command</td><td>Weight + Grudge + Lament</td></tr>
<tr><td><strong>2</strong></td><td><a href="the-secretary-seiyon.html"><strong>Seiyon (세이연)</strong></a></td><td>The Secretary (비서)</td><td>Floor 1 · Central Station</td><td>Lament + Void</td></tr>
<tr><td><strong>3</strong></td><td><a href="the-containment-lead-dekan.html"><strong>Dekan (데칸)</strong></a></td><td>Containment Lead (Neokvox)</td><td>Floor 2 · The Maw’s Keep</td><td>Grudge (Crimson)</td></tr>
<tr><td><strong>4</strong></td><td><a href="the-extraction-lead-zyrak.html"><strong>Zyrak (지락)</strong></a></td><td>Extraction Lead (Nukimanus)</td><td>Floor 3 · Extraction Hall</td><td>Grudge + Void</td></tr>
<tr><td><strong>5</strong></td><td><a href="the-research-lead-ayshuk.html"><strong>Ayshuk (아이숙)</strong></a></td><td>Research Lead (Kenopathos)</td><td>Floor 4 · Insight Forge</td><td>Void (Pale White)</td></tr>
<tr><td><strong>6</strong></td><td><a href="the-border-lead-mellda.html"><strong>Mellda (멜다)</strong></a></td><td>Border Lead (Munkaeri)</td><td>Floor 5 · Border Watch</td><td>Weight + Grudge</td></tr>
<tr><td><strong>7</strong></td><td><a href="the-archive-lead-marjuk.html"><strong>Marjuk (마주크)</strong></a></td><td>Archive Lead (Veniago)</td><td>Floor 6 · Deep Vault</td><td>Lament (Deep Blue)</td></tr>
<tr><td><strong>8</strong></td><td><a href="the-outsider-ishall.html"><strong>Ishall (이샬)</strong></a></td><td>The Outsider (Nemona)</td><td>Floor 7 · Shadow Corps</td><td>Void + Lament</td></tr>
<tr><td><strong>9</strong></td><td><a href="the-exile-xyan.html"><strong>Xyan (시안)</strong></a></td><td>The Exile (Sotogil)</td><td>Floor 8 · Gate Watch</td><td>Weight + Lament</td></tr>
</tbody></table></div>

<h2 id="civic-and-field-figures">Civic &amp; Field Figures</h2>
<p>Beyond the Directorate’s central staff, prominent guild leaders, caravan captains, and master artisans maintain the infrastructure of Somnarak:</p>
<div class="table-wrap"><table class="data-table"><thead><tr><th>Character</th><th>Role &amp; Affiliation</th><th>Primary Location</th><th>Field of Expertise</th></tr></thead><tbody>
<tr><td><a href="kael.html"><strong>Kael (카엘)</strong></a></td><td>The Drift King / Caravan Captain</td><td>The Desolate / Mobile</td><td>Desolate Navigation, Han-Tide Survival, Vanguard Defense</td></tr>
<tr><td><a href="soojin.html"><strong>Soojin (수진)</strong></a></td><td>Master Weaver / Echo Singer</td><td>Zone D · Echo Gardens</td><td>Emotional Threading, M.A.W. Suit Linings, Fracture Repair</td></tr>
<tr><td><a href="high-architects.html"><strong>The High Architects</strong></a></td><td>Master Builders Guild</td><td>Zone A · Plumb Spire</td><td>Urban Grid Design, Sorrow Masonry, Containment Architecture</td></tr>
</tbody></table></div>

<h2 id="demographic-cohorts">Demographic Cohorts</h2>
<p>Communities and immigrant populations playing vital roles in the city’s evolving culture:</p>
<ul>
<li><a href="cheonbulok-refugees.html"><strong>Cheonbulok Refugees (천불록 피난민):</strong></a> Over 14,000 survivors from Corner 2 (The City of a Thousand Rages), bringing advanced volcanic slag-forging technology to Zone D.</li>
<li><strong>The Desolate Wanderers:</strong> Independent clans and Menders operating in the liminal wastes between metropolitan boundaries.</li>
<li><strong>The Underworld Frays:</strong> Shadow syndicates and contraband traders operating in the subterranean conduits beneath Zone C.</li>
</ul>
</article>
</main>
{get_floor_rail()}
</div>
{get_footer()}
</body></html>"""

with open(os.path.join(CHAR_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(hub_html)
print("Generated characters/index.html")
