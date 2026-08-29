import os
import re

FAC_DIR = "/home/user/01_Somnarak_Wiki/factions"
os.makedirs(FAC_DIR, exist_ok=True)

from generate_all_characters import get_left_rail, get_floor_rail, get_header, get_footer

def build_faction_pages():
    # 1. the-reverie-directorate.html
    rd_html = f"""<!doctype html><html lang="en" data-article-status="curated"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>The Reverie Directorate — Somnarak Wiki</title><meta name="description" content="Supreme institution governing sorrow containment, M.A.W. extraction, and research beneath the Alpha Tree"><link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg"><link rel="stylesheet" href="../assets/css/wiki.css"><script defer src="../assets/js/wiki.js"></script></head><body>
{get_header()}
<nav class="float-toc" aria-label="On this page"><button type="button" aria-expanded="false">CONTENTS</button><div><strong>ON THIS PAGE</strong><ol><li class="l2"><a href="#overview">Overview</a></li><li class="l2"><a href="#institutional-profile">Institutional Profile</a></li><li class="l2"><a href="#the-hand-of-change-facility">The Hand of Change Facility</a></li><li class="l2"><a href="#the-nine-echo-cores">The Nine Echo-Cores</a></li><li class="l2"><a href="#operational-mandate">Operational Mandate</a></li><li class="l2"><a href="#post-cycle-reformation">Post-Cycle Reformation (Year 4,238)</a></li></ol><a href="#content">↑ TOP</a></div></nav>
<div class="wiki-shell">
{get_left_rail()}
<main id="content"><div class="page-tabs"><span>Factions &amp; Guilds</span><b>PRIMARY INSTITUTION</b></div><div class="breadcrumbs"><a href="../index.html">Main page</a><i>›</i><a href="index.html">Factions</a><i>›</i>The Reverie Directorate</div>
<section class="department-hero" style="--floor:#ef5b55"><img src="../assets/layout/hand/icons/the_hand_dr_icon.svg" alt=""><div><span>CENTRAL AUTHORITY · CORPORATION 1</span><h1>The Reverie Directorate</h1><p>리버리 지부 — Riberi Jibu (The Reverie Directorate)</p></div></section>
<blockquote class="motto" style="--floor:#ef5b55">“We do not contain sorrow to conquer it; we contain sorrow so the city may wake to tomorrow.” — Director Majin</blockquote>
<section class="department-overview"><div><h2 id="overview">Overview</h2><p class="lead"><strong>The Reverie Directorate</strong> (리버리 지부) is the paramount scientific, containment, and defense institution of Somnarak. Established in the aftermath of the Cheongula Incident of Year 180, the Directorate operates from the <strong>Hand of Change</strong>, an eight-floor subterranean facility constructed directly inside the root mass of the Alpha Tree.</p><p>Led by Director Majin and governed through the Nine Echo-Cores, the Directorate possesses sole legal jurisdiction over Sorrow Entity containment, M.A.W. equipment extraction, Han physics research, and the defense of the city’s outer perimeter gates.</p></div><aside class="department-profile" style="--floor:#ef5b55"><h2 id="institutional-profile">Institutional Profile</h2><dl><dt>Formal Name</dt><dd>The Reverie Directorate (리버리 지부)</dd><dt>Headquarters</dt><dd>The Hand of Change (Alpha Tree Roots)</dd><dt>Supreme Leader</dt><dd>Majin, The Director (관장)</dd><dt>Administrative Lead</dt><dd>Seiyon, The Secretary (비서)</dd><dt>Operational Structure</dt><dd>8 Floors (Palm, Fingers, Wing)</dd><dt>Primary Jurisdiction</dt><dd>Entity Containment, M.A.W. Extraction, Veil Power</dd><dt>Current Status</dt><dd>Reformed · Active under Dawn Initiative</dd></dl></aside></section>
<article class="article-body">
<h2 id="the-hand-of-change-facility">The Hand of Change Facility</h2>
<p>The Directorate’s headquarters is anatomically designed to distribute functional responsibilities across specialized geological levels:</p>
<ul>
<li><strong>The Palm (Floors 1–3):</strong> The central core consisting of <em>Floor 1 Neutral Command</em> (executive authority), <em>Floor 2 The Maw’s Keep</em> (Maw perimeter containment), and <em>Floor 3 Extraction Hall</em> (M.A.W. crystallization).</li>
<li><strong>The Fingers (Floors 4–7):</strong> Specialized exploratory branches consisting of <em>Floor 4 Insight Forge</em> (research), <em>Floor 5 Border Watch</em> (Threshold defense), <em>Floor 6 Deep Vault</em> (historical records and the Final Door), and <em>Floor 7 Shadow Corps</em> (urban intelligence).</li>
<li><strong>The Wing (Floor 8):</strong> The lateral gatehouse of <em>Floor 8 Gate Watch</em>, directly interfacing with the Desolate and commanded by the returned Exile, Xyan.</li>
</ul>

<h2 id="the-nine-echo-cores">The Nine Echo-Cores</h2>
<p>The Directorate is guided by nine commanding intelligences known as Echo-Cores. Each Echo-Core maintains a deep emotional bond with their floor and represents a crucial fragment of the Doorspeech prophecy:</p>
<div class="table-wrap"><table class="data-table"><thead><tr><th>Core</th><th>Lead Official</th><th>Department &amp; Floor</th><th>Operational Mandate</th></tr></thead><tbody>
<tr><td><strong>1</strong></td><td><a href="../characters/the-director-majin.html"><strong>Majin (마진)</strong></a></td><td>Floor 1 · Neutral Command</td><td>Supreme facility command, work authorization, crisis intervention</td></tr>
<tr><td><strong>2</strong></td><td><a href="../characters/the-secretary-seiyon.html"><strong>Seiyon (세이연)</strong></a></td><td>Floor 1 · Administration</td><td>Facility metrics, scheduling, inter-floor coordination, historical truth</td></tr>
<tr><td><strong>3</strong></td><td><a href="../characters/the-containment-lead-dekan.html"><strong>Dekan (데칸)</strong></a></td><td>Floor 2 · The Maw’s Keep</td><td>Subterranean containment, breach suppression, Maw perimeter guards</td></tr>
<tr><td><strong>4</strong></td><td><a href="../characters/the-extraction-lead-zyrak.html"><strong>Zyrak (지락)</strong></a></td><td>Floor 3 · Extraction Hall</td><td>M.A.W. crystallization, resonance harvesting, weapon safety limits</td></tr>
<tr><td><strong>5</strong></td><td><a href="../characters/the-research-lead-ayshuk.html"><strong>Ayshuk (아이숙)</strong></a></td><td>Floor 4 · Insight Forge</td><td>Han physics, Sorrow Spectrometry, Void-condition analysis</td></tr>
<tr><td><strong>6</strong></td><td><a href="../characters/the-border-lead-mellda.html"><strong>Mellda (멜다)</strong></a></td><td>Floor 5 · Border Watch</td><td>Zone E threshold, Desolate perimeter surveillance, Aegis maintenance</td></tr>
<tr><td><strong>7</strong></td><td><a href="../characters/the-archive-lead-marjuk.html"><strong>Marjuk (마주크)</strong></a></td><td>Floor 6 · Deep Vault</td><td>Grand Archive, pre-Cycle records, memory wells, Final Door oversight</td></tr>
<tr><td><strong>8</strong></td><td><a href="../characters/the-outsider-ishall.html"><strong>Ishall (이샬)</strong></a></td><td>Floor 7 · Shadow Corps</td><td>Undercover intelligence, counter-Fray ops, black market M.A.W. recovery</td></tr>
<tr><td><strong>9</strong></td><td><a href="../characters/the-exile-xyan.html"><strong>Xyan (시안)</strong></a></td><td>Floor 8 · Gate Watch</td><td>Outer Gate command, long-range reconnaissance, expedition routing</td></tr>
</tbody></table></div>

<h2 id="operational-mandate">Operational Mandate</h2>
<p>The Directorate is legally tasked with providing the municipal grid with stable Han-Energy while minimizing psychological casualties. Under the Four Work Types (<em>Ferrehan</em>, <em>Flerehan</em>, <em>Viderehan</em>, <em>Pugnahan</em>), personnel enter containment cells to pacify entities and harvest crystallized sorrow without triggering destructive breaches.</p>

<h2 id="post-cycle-reformation">Post-Cycle Reformation (Year 4,238)</h2>
<p>Following the termination of the 1,778-Cycle loop, the Directorate dismantled its secretive policies. The hidden Absolvohan reserve was publicly disclosed, worker safety limits were tripled, and the Directorate entered into a formal cooperative treaty with the High Council and the Horizon Caravan.</p>
</article>
<nav class="article-nav"><a href="index.html">← Factions Hub</a><a href="the-high-council.html">The High Council →</a></nav>
</main>
{get_floor_rail()}
</div>
{get_footer()}
</body></html>"""

    with open(os.path.join(FAC_DIR, "the-reverie-directorate.html"), "w", encoding="utf-8") as f:
        f.write(rd_html)
    print("Generated factions/the-reverie-directorate.html")

    # 2. the-high-council.html
    council_html = f"""<!doctype html><html lang="en" data-article-status="curated"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>The High Council (Council of Sighs) — Somnarak Wiki</title><meta name="description" content="Civil governance body of Somnarak, managing municipal law, commerce, and district administration"><link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg"><link rel="stylesheet" href="../assets/css/wiki.css"><script defer src="../assets/js/wiki.js"></script></head><body>
{get_header()}
<nav class="float-toc" aria-label="On this page"><button type="button" aria-expanded="false">CONTENTS</button><div><strong>ON THIS PAGE</strong><ol><li class="l2"><a href="#overview">Overview</a></li><li class="l2"><a href="#council-profile">Council Profile</a></li><li class="l2"><a href="#the-three-chambers">The Three Chambers</a></li><li class="l2"><a href="#civil-law-and-taxation">Civil Law &amp; Han Taxation</a></li><li class="l2"><a href="#relations-with-the-directorate">Relations with the Directorate</a></li><li class="l2"><a href="#faction-technology">Faction Technology</a></li></ol><a href="#content">↑ TOP</a></div></nav>
<div class="wiki-shell">
{get_left_rail()}
<main id="content"><div class="page-tabs"><span>Factions &amp; Guilds</span><b>CIVIL GOVERNANCE</b></div><div class="breadcrumbs"><a href="../index.html">Main page</a><i>›</i><a href="index.html">Factions</a><i>›</i>The High Council</div>
<section class="department-hero" style="--floor:#f1df76"><img src="../assets/icons/fac_council.svg" alt=""><div><span>GOVERNING BODY · ZONE A</span><h1>The High Council</h1><p>한숨의 의회 — Hansum-ui Uihoe (The Council of Sighs)</p></div></section>
<blockquote class="motto" style="--floor:#f1df76">“To rule is to weigh every sigh in the city and decide which ones the treasury can afford to answer.” — Chancellor Yul</blockquote>
<section class="department-overview"><div><h2 id="overview">Overview</h2><p class="lead"><strong>The High Council</strong> (대회의), formally known as the <strong>Council of Sighs</strong> (한숨의 의회), is the civilian parliamentary authority governing Somnarak. Seated in the Grand Rotunda within the lower trunk of the Alpha Tree in Zone A, the Council oversees municipal taxation, commerce, district housing, the legal code, and civilian guild relations.</p><p>While the Reverie Directorate maintains military and containment sovereignty, the Council controls the allocation of raw municipal funding, grain distribution, and public infrastructure across all five zones.</p></div><aside class="department-profile" style="--floor:#f1df76"><h2 id="council-profile">Council Profile</h2><dl><dt>Official Name</dt><dd>The Council of Sighs (한숨의 의회)</dd><dt>Seat of Power</dt><dd>The Grand Rotunda, Zone A Core</dd><dt>Presiding Official</dt><dd>Chancellor Yul (수석 재상)</dd><dt>Governing Seats</dt><dd>33 Councilors across 5 Zones</dd><dt>Core Jurisdiction</dt><dd>Civil Law, Commerce, Energy Allocations</dd><dt>Signature Element</dt><dd>Weight (Black) + Clarity (White)</dd><dt>Current Policy</dt><dd>Dawn Reconstruction &amp; Refugee Asylum</dd></dl></aside></section>
<article class="article-body">
<h2 id="the-three-chambers">The Three Chambers</h2>
<p>The Council of Sighs operates through three distinct legislative bodies:</p>
<ul>
<li><strong>The Chamber of the Plumb:</strong> Composed of senior High Architects and urban planners who regulate building permits, defensive wall maintenance, and structural safety codes.</li>
<li><strong>The Chamber of Accounts:</strong> Controlled by senior representatives of the Collector Guild who manage municipal debts, commercial trade duties, and energy distribution contracts.</li>
<li><strong>The Chamber of Petitions:</strong> The civilian forum where district elders, refugee delegates, and neighborhood Menders present grievances and request emergency aid.</li>
</ul>

<h2 id="civil-law-and-taxation">Civil Law &amp; Han Taxation</h2>
<p>Because ordinary coins hold little value in an economy fueled by psychic energy, the Council levies the <strong>Resonant Surcharge</strong> (한세 — <em>Hanse</em>). Commercial enterprises and guild houses pay taxes in certified Han-fuel canisters harvested from regulated secondary wells, which the Council redistributes to maintain street lamps, water filtration, and the Aegis Veil generators.</p>

<h2 id="relations-with-the-directorate">Relations with the Directorate</h2>
<p>The relationship between the Council and the Directorate has historically been fraught with tension. During the Cycle, Council auditors frequently accused Director Majin of withholding energy reserves. Following the Day 365 disclosure, the Council granted the Directorate permanent ministerial autonomy in exchange for transparent public casualty logs and energy quotas.</p>

<h2 id="faction-technology">Faction Technology</h2>
<p>Council officials utilize proprietary governance technology:</p>
<div class="table-wrap"><table class="data-table"><thead><tr><th>Technology</th><th>Designation</th><th>Function</th></tr></thead><tbody><tr><td><strong>The Sigh-Recorder</strong></td><td>한숨 기록기</td><td>Acoustic parchment device that transcribes the emotional sincerity of political speeches</td></tr><tr><td><strong>The Decision Scale</strong></td><td>결정 저울</td><td>Weighted brass apparatus used to calculate the economic impact of legislative bills</td></tr><tr><td><strong>The Resonant Seal</strong></td><td>공명 직인</td><td>Pneumatic wax stamper that imbues official laws with binding legal weight</td></tr></tbody></table></div>
</article>
<nav class="article-nav"><a href="the-reverie-directorate.html">← The Reverie Directorate</a><a href="the-architects.html">The Architects →</a></nav>
</main>
{get_floor_rail()}
</div>
{get_footer()}
</body></html>"""

    with open(os.path.join(FAC_DIR, "the-high-council.html"), "w", encoding="utf-8") as f:
        f.write(council_html)
    print("Generated factions/the-high-council.html")

    # 3. the-architects.html
    arch_fac_html = f"""<!doctype html><html lang="en" data-article-status="curated"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>The Architects — Somnarak Wiki</title><meta name="description" content="The guild of master builders and engineers shaping Somnarak's masonry and containment geometry"><link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg"><link rel="stylesheet" href="../assets/css/wiki.css"><script defer src="../assets/js/wiki.js"></script></head><body>
{get_header()}
<nav class="float-toc" aria-label="On this page"><button type="button" aria-expanded="false">CONTENTS</button><div><strong>ON THIS PAGE</strong><ol><li class="l2"><a href="#overview">Overview</a></li><li class="l2"><a href="#guild-profile">Guild Profile</a></li><li class="l2"><a href="#the-geometry-of-sorrow">The Geometry of Sorrow</a></li><li class="l2"><a href="#major-works">Major Works</a></li><li class="l2"><a href="#architectural-tools-and-tech">Architectural Tools &amp; Tech</a></li></ol><a href="#content">↑ TOP</a></div></nav>
<div class="wiki-shell">
{get_left_rail()}
<main id="content"><div class="page-tabs"><span>Factions &amp; Guilds</span><b>STRUCTURAL GUILD</b></div><div class="breadcrumbs"><a href="../index.html">Main page</a><i>›</i><a href="index.html">Factions</a><i>›</i>The Architects</div>
<section class="department-hero" style="--floor:#f1df76"><img src="../assets/icons/fac_architects.svg" alt=""><div><span>CIVIL GUILD · MASTER BUILDERS</span><h1>The Architects</h1><p>건축가 길드 — Geonchukga Gildeu</p></div></section>
<blockquote class="motto" style="--floor:#f1df76">“Every wall is a statement of will against the abyss. Make it plumb, or the void will find the seam.” — Architect Rulebook</blockquote>
<section class="department-overview"><div><h2 id="overview">Overview</h2><p class="lead"><strong>The Architects</strong> (건축가) form the premier structural engineering guild responsible for the planning, construction, and physical maintenance of Somnarak. Working alongside the Directorate’s containment leads and the Council’s urban planners, the Architects specialize in <em>Sorrow Masonry</em>—the delicate science of building load-bearing structures that can withstand intense Han-radiation.</p><p>From the cyclopean outer walls of Zone E to the intricate acoustic dampening tiles lining the Deep Vault, the Architects ensure the city does not crumble under its own accumulated psychic weight.</p></div><aside class="department-profile" style="--floor:#f1df76"><h2 id="guild-profile">Guild Profile</h2><dl><dt>Guild Title</dt><dd>The High Guild of Architects (건축가)</dd><dt>Guildhall</dt><dd>The Spire of Plumb Lines, Zone A</dd><dt>Grandmaster</dt><dd>Master Orak (Historical) / Ilan (Current)</dd><dt>Guild Membership</dt><dd>~3,400 Master Builders &amp; Apprentices</dd><dt>Core Craft</dt><dd>Sorrow Masonry, Kinetic Bracing, Veil Anchors</dd><dt>Primary Signature</dt><dd>Weight (Black) + Clarity (White)</dd><dt>Current Mission</dt><dd>Rebuilding Zone D Mantle &amp; Western Walls</dd></dl></aside></section>
<article class="article-body">
<h2 id="the-geometry-of-sorrow">The Geometry of Sorrow</h2>
<p>Unlike standard civil architecture, building in Somnarak requires mastering the flow of subterranean emotional resonance. The Architects adhere to strict geometric rules designed to prevent resonance traps:</p>
<ul>
<li><strong>No Dead Angles:</strong> Rooms must avoid acute 90-degree internal corners where Han-residue can stagnate and nucleate into minor Object SEs.</li>
<li><strong>Acoustic Weeping Channels:</strong> Basements must incorporate gravity drainage channels that divert condensated Weeping fluid away from residential living quarters.</li>
<li><strong>Sacrificial Foundations:</strong> Outer perimeter gates feature breakaway basal joints that absorb kinetic shockwaves from migrating Colossus entities without transmitting vibrations to inner districts.</li>
</ul>

<h2 id="major-works">Major Works</h2>
<div class="table-wrap"><table class="data-table"><thead><tr><th>Structure</th><th>Location</th><th>Engineering Significance</th></tr></thead><tbody><tr><td><strong>The Hand of Change</strong></td><td>Zone A Root Hollow</td><td>Subterranean 8-floor anatomical facility carved directly into living petrified timber</td></tr><tr><td><strong>The Aegis Wall</strong></td><td>Zone E Bulwark</td><td>Thirty-meter-tall basalt bulwark equipped with crystalline resonance emitters</td></tr><tr><td><strong>The Spire of Sighs</strong></td><td>Zone A Core</td><td>Spiraling administrative tower wrapped around the trunk of the Alpha Tree</td></tr><tr><td><strong>The Maw Containment Rim</strong></td><td>Zone B Perimeter</td><td>Reinforced titanium-alloy retaining ring preventing chasm erosion around SE-1003</td></tr></tbody></table></div>

<h2 id="architectural-tools-and-tech">Architectural Tools &amp; Tech</h2>
<p>Guild artisans employ specialized instruments: the <strong>Sorrow Compass</strong> (locates psychic stress nodes), the <strong>Resonant Plumb</strong> (ensures vertical stability against gravitational distortion), and <strong>Han-Trowels</strong> (chemically temper mortar using powdered Void-crystal).</p>
</article>
<nav class="article-nav"><a href="the-high-council.html">← The High Council</a><a href="the-weavers.html">The Weavers →</a></nav>
</main>
{get_floor_rail()}
</div>
{get_footer()}
</body></html>"""

    with open(os.path.join(FAC_DIR, "the-architects.html"), "w", encoding="utf-8") as f:
        f.write(arch_fac_html)
    print("Generated factions/the-architects.html")

    # 4. the-weavers.html
    weavers_html = f"""<!doctype html><html lang="en" data-article-status="curated"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>The Weavers — Somnarak Wiki</title><meta name="description" content="Artisans of the Echo Gardens specializing in memory filaments, psychic attunement, and M.A.W. suit linings"><link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg"><link rel="stylesheet" href="../assets/css/wiki.css"><script defer src="../assets/js/wiki.js"></script></head><body>
{get_header()}
<nav class="float-toc" aria-label="On this page"><button type="button" aria-expanded="false">CONTENTS</button><div><strong>ON THIS PAGE</strong><ol><li class="l2"><a href="#overview">Overview</a></li><li class="l2"><a href="#guild-profile">Guild Profile</a></li><li class="l2"><a href="#the-art-of-emotional-spinning">The Art of Emotional Spinning</a></li><li class="l2"><a href="#m-a-w-suit-collaboration">M.A.W. Suit Collaboration</a></li><li class="l2"><a href="#the-seven-harmonic-looms">The Seven Harmonic Looms</a></li></ol><a href="#content">↑ TOP</a></div></nav>
<div class="wiki-shell">
{get_left_rail()}
<main id="content"><div class="page-tabs"><span>Factions &amp; Guilds</span><b>TEXTILE &amp; RESONANCE GUILD</b></div><div class="breadcrumbs"><a href="../index.html">Main page</a><i>›</i><a href="index.html">Factions</a><i>›</i>The Weavers</div>
<section class="department-hero" style="--floor:#83d6ad"><img src="../assets/icons/fac_weavers.svg" alt=""><div><span>ARTISAN GUILD · ZONE D ECHO GARDENS</span><h1>The Weavers</h1><p>직조공 길드 — Jikjogong Gildeu</p></div></section>
<blockquote class="motto" style="--floor:#83d6ad">“Iron breaks under weight; silk yields and returns. To survive the grief of Somnarak, one must learn to bend without fraying.” — Master Soojin</blockquote>
<section class="department-overview"><div><h2 id="overview">Overview</h2><p class="lead"><strong>The Weavers</strong> (직조공) are the celebrated guild of acoustic artisans, memory spinners, and textile alchemists centered in the Echo Gardens of Zone D. By harmonizing raw emotional frequencies through mechanical looms, the Weavers transform ephemeral sorrow filaments into high-tensile crystalline fabrics.</p><p>Their specialized textiles are essential for manufacturing the inner ballistic and psychic dampening layers of all Directorate M.A.W. Suits, providing operatives with protection against mind-fracturing entity resonance.</p></div><aside class="department-profile" style="--floor:#83d6ad"><h2 id="guild-profile">Guild Profile</h2><dl><dt>Guild Designation</dt><dd>The Weavers of the Echo Gardens (직조공)</dd><dt>Headquarters</dt><dd>The Loom Spires, Zone D Terraces</dd><dt>Guild Elder</dt><dd>Master Soojin (수진)</dd><dt>Membership</dt><dd>~1,800 Spinners, Attuners, &amp; Loomsmen</dd><dt>Signature Element</dt><dd>Lament (Deep Blue) + Void (Pale White)</dd><dt>Primary Deliverable</dt><dd>Resonance Silks, Dampening Veils, M.A.W. Linings</dd><dt>Current Focus</dt><dd>Integrating Hope Filaments into Medical Gauze</dd></dl></aside></section>
<article class="article-body">
<h2 id="the-art-of-emotional-spinning">The Art of Emotional Spinning</h2>
<p>When human consciousness undergoes extreme grief or trauma, the subconscious mind sheds micro-filaments of psychic residue. Left alone, these threads dissipate or form parasitic memory cobwebs. The Weavers gather these filaments using <strong>Acoustic Tuning Forks</strong>, aligning the emotional charge of the strands before feeding them into specialized spinning wheels.</p>

<h2 id="m-a-w-suit-collaboration">M.A.W. Suit Collaboration</h2>
<p>The Directorate’s Extraction Hall (Floor 3) relies directly on the Weavers to produce protective gear. While the Directorate forges the external carapace plates from crystallized entity residue, the Weavers supply the flexible under-suit mesh. This mesh disperses kinetic impact and filters out psychic whispers that would otherwise induce panic in the wearer.</p>

<h2 id="the-seven-harmonic-looms">The Seven Harmonic Looms</h2>
<div class="table-wrap"><table class="data-table"><thead><tr><th>Loom Station</th><th>Thread Type</th><th>Emotional Resonance</th><th>Application</th></tr></thead><tbody><tr><td><strong>Loom 1 (Lament)</strong></td><td>Deep Blue Silk</td><td>Pure mourning &amp; remembrance</td><td>Acoustic shielding for Deep Vault archives</td></tr><tr><td><strong>Loom 2 (Grudge)</strong></td><td>Crimson Filament</td><td>Righteous fury &amp; resolve</td><td>Thermal lining for heavy combat armor</td></tr><tr><td><strong>Loom 3 (Void)</strong></td><td>Silver Mist-Taffeta</td><td>Apathy &amp; emotional numbness</td><td>Stealth cloaks for Shadow Corps operatives</td></tr><tr><td><strong>Loom 4 (Hope)</strong></td><td>Golden Dawn Thread</td><td>Post-Cycle restoration</td><td>Medical bandages accelerating Fracture healing</td></tr></tbody></table></div>
</article>
<nav class="article-nav"><a href="the-architects.html">← The Architects</a><a href="the-wardens.html">The Wardens →</a></nav>
</main>
{get_floor_rail()}
</div>
{get_footer()}
</body></html>"""

    with open(os.path.join(FAC_DIR, "the-weavers.html"), "w", encoding="utf-8") as f:
        f.write(weavers_html)
    print("Generated factions/the-weavers.html")

    # 5. the-wardens.html
    wardens_html = f"""<!doctype html><html lang="en" data-article-status="curated"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>The Wardens — Somnarak Wiki</title><meta name="description" content="The military perimeter defense forces garrisoned along Zone E and the Aegis Wall"><link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg"><link rel="stylesheet" href="../assets/css/wiki.css"><script defer src="../assets/js/wiki.js"></script></head><body>
{get_header()}
<nav class="float-toc" aria-label="On this page"><button type="button" aria-expanded="false">CONTENTS</button><div><strong>ON THIS PAGE</strong><ol><li class="l2"><a href="#overview">Overview</a></li><li class="l2"><a href="#warden-profile">Warden Profile</a></li><li class="l2"><a href="#the-perimeter-defense-network">The Perimeter Defense Network</a></li><li class="l2"><a href="#the-aegis-veil">The Aegis Veil</a></li><li class="l2"><a href="#garrison-regiments-and-tactics">Garrison Regiments &amp; Tactics</a></li></ol><a href="#content">↑ TOP</a></div></nav>
<div class="wiki-shell">
{get_left_rail()}
<main id="content"><div class="page-tabs"><span>Factions &amp; Guilds</span><b>MILITARY DEFENSE FORCE</b></div><div class="breadcrumbs"><a href="../index.html">Main page</a><i>›</i><a href="index.html">Factions</a><i>›</i>The Wardens</div>
<section class="department-hero" style="--floor:#d7d7d7"><img src="../assets/icons/fac_wardens.svg" alt=""><div><span>MILITARY GARRISON · ZONE E BULWARK</span><h1>The Wardens</h1><p>경계 수호대 — Gyeonggye Suhoda (The Wardens)</p></div></section>
<blockquote class="motto" style="--floor:#d7d7d7">“We stand between the breathing city and the freezing void. Behind us is warmth; before us is nothingness. We do not step back.” — Warden Oath</blockquote>
<section class="department-overview"><div><h2 id="overview">Overview</h2><p class="lead"><strong>The Wardens</strong> (수호대) are the permanent military border defense force of Somnarak, garrisoned along the thirty-meter basalt fortifications of <strong>Zone E</strong> (The Bulwark). Tasked with repelling incursions from massive Outside Sorrow Entities and maintaining the city’s perimeter energy shield, the Wardens are the first and last line of defense against the Desolate.</p><p>Operating under the strategic oversight of Border Lead Mellda (Floor 5) and cooperating with Gate Watch (Floor 8), the Wardens combine heavy artillery, kinetic barrier pylons, and specialized M.A.W. weaponry to protect the civilian population.</p></div><aside class="department-profile" style="--floor:#d7d7d7"><h2 id="warden-profile">Garrison Profile</h2><dl><dt>Force Designation</dt><dd>The Municipal Wardens (경계 수호대)</dd><dt>Headquarters</dt><dd>Fortress Threshold, Zone E North Gate</dd><dt>Strategic Commander</dt><dd>Mellda, Border Lead (Floor 5)</dd><dt>Active Strength</dt><dd>~6,800 Frontline Defenders &amp; Artillerists</dd><dt>Primary Defensive Line</dt><dd>The Aegis Bulwark (Zone E Outer Ring)</dd><dt>Signature Element</dt><dd>Weight (Black) + Resolve (Green)</dd><dt>Current Posture</dt><dd>Active Vigilance · Supporting Horizon Expeditions</dd></dl></aside></section>
<article class="article-body">
<h2 id="the-perimeter-defense-network">The Perimeter Defense Network</h2>
<p>The defensive network consists of twelve massive bastions spaced along the circular perimeter wall, linked by heavy underground transit tunnels. Each bastion houses heavy <strong>Han-Mortar Batteries</strong> capable of firing stabilized Weight-crystal shells into incoming entity swarms.</p>

<h2 id="the-aegis-veil">The Aegis Veil</h2>
<p>The primary barrier safeguarding Somnarak is the <strong>Aegis Veil</strong> (방호 베일), a dome-shaped electromagnetic and psychic energy field powered by the Alpha Tree’s central generator. The Veil reflects low-tier Outside entities and insulates the city against the lethal sub-zero cold of the Desolate.</p>

<h2 id="garrison-regiments-and-tactics">Garrison Regiments &amp; Tactics</h2>
<div class="table-wrap"><table class="data-table"><thead><tr><th>Regiment</th><th>Tactical Stance</th><th>Primary Weaponry</th><th>Operational Role</th></tr></thead><tbody><tr><td><strong>The Iron Wall Vanguard</strong></td><td>Heavy Frontline Bracing</td><td>Reinforced Tower Shields &amp; Anchor Pikes</td><td>Halts Colossus breaches at outer gates</td></tr><tr><td><strong>The Veil Artillerists</strong></td><td>Long-Range Kinetic Bombardment</td><td>Pneumatic Han-Mortars &amp; Rail Howitzers</td><td>Breaks up migratory Wilderness Tides (SE-003)</td></tr><tr><td><strong>The Outrunner Scouts</strong></td><td>Rapid Reconnaissance</td><td>Light Crossbows &amp; Desolate Skimmers</td><td>Patrols the two-kilometer neutral zone outside Gate 1–5</td></tr></tbody></table></div>
</article>
<nav class="article-nav"><a href="the-weavers.html">← The Weavers</a><a href="the-collectors.html">The Collectors →</a></nav>
</main>
{get_floor_rail()}
</div>
{get_footer()}
</body></html>"""

    with open(os.path.join(FAC_DIR, "the-wardens.html"), "w", encoding="utf-8") as f:
        f.write(wardens_html)
    print("Generated factions/the-wardens.html")

    # 6. the-collectors.html
    collectors_html = f"""<!doctype html><html lang="en" data-article-status="curated"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>The Collectors — Somnarak Wiki</title><meta name="description" content="The debt enforcement guild and commercial houses controlling Zone C (Collector's Row)"><link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg"><link rel="stylesheet" href="../assets/css/wiki.css"><script defer src="../assets/js/wiki.js"></script></head><body>
{get_header()}
<nav class="float-toc" aria-label="On this page"><button type="button" aria-expanded="false">CONTENTS</button><div><strong>ON THIS PAGE</strong><ol><li class="l2"><a href="#overview">Overview</a></li><li class="l2"><a href="#guild-profile">Guild Profile</a></li><li class="l2"><a href="#the-debt-economy">The Debt Economy</a></li><li class="l2"><a href="#the-courts-of-reckoning">The Courts of Reckoning</a></li><li class="l2"><a href="#commercial-houses-and-m-a-w-trade">Commercial Houses &amp; M.A.W. Trade</a></li></ol><a href="#content">↑ TOP</a></div></nav>
<div class="wiki-shell">
{get_left_rail()}
<main id="content"><div class="page-tabs"><span>Factions &amp; Guilds</span><b>COMMERCIAL &amp; DEBT GUILD</b></div><div class="breadcrumbs"><a href="../index.html">Main page</a><i>›</i><a href="index.html">Factions</a><i>›</i>The Collectors</div>
<section class="department-hero" style="--floor:#e6c94d"><img src="../assets/icons/fac_collectors.svg" alt=""><div><span>COMMERCIAL SYNDICATE · ZONE C</span><h1>The Collectors</h1><p>수금가 길드 — Sugeumga Gildeu (The Collectors)</p></div></section>
<blockquote class="motto" style="--floor:#e6c94d">“Every breath in this city has a price. If you cannot pay in coin, the ledger will balance in tears.” — Collector Bailiff Gyeol</blockquote>
<section class="department-overview"><div><h2 id="overview">Overview</h2><p class="lead"><strong>The Collectors</strong> (수금가) constitute the powerful banking, debt enforcement, and commercial consortium dominating <strong>Zone C</strong> (Collector’s Row). Operating the municipal banks, pawn vaults, and M.A.W. trading exchanges, the Collectors enforce the principle that emotional and material debts are legally interchangeable.</p><p>Closely aligned with the Directorate’s Extraction Hall (Floor 3) and overseeing access to SE-014 (The Debt Eater) and SE-015 (The Debt Scale), the Collectors manage the city’s economic liquidity through strict debt ledgers.</p></div><aside class="department-profile" style="--floor:#e6c94d"><h2 id="guild-profile">Guild Profile</h2><dl><dt>Syndicate Name</dt><dd>The High Guild of Collectors (수금가)</dd><dt>Headquarters</dt><dd>The Exchange of Scales, Zone C</dd><dt>Grand Bailiff</dt><dd>Senior Bailiff Gyeol (수석 집행관)</dd><dt>Jurisdiction</dt><dd>Commercial Banking, Debt Liens, Equipment Auction</dd><dt>Signature Element</dt><dd>Void (Pale White) + Weight (Black)</dd><dt>Controlled Entities</dt><dd>SE-014 (Debt Eater), SE-015 (Debt Scale)</dd><dt>Current Status</dt><dd>Regulated under Post-Cycle Debt Caps</dd></dl></aside></section>
<article class="article-body">
<h2 id="the-debt-economy">The Debt Economy</h2>
<p>In Somnarak, a debt is not merely an abstract number on paper; unresolved financial distress generates measurable Void-type Han. The Collectors harvest this psychic pressure by offering debt-consolidation contracts. Citizens unable to pay monetary loans can surrender a portion of their emotional memories or enter temporary servitude at extraction refineries.</p>

<h2 id="the-courts-of-reckoning">The Courts of Reckoning</h2>
<p>In the central plazas of Zone C, Collector judges preside over the <strong>Courts of Reckoning</strong>. Here, disputes are settled not with juries, but by placing the debtor and creditor before <strong>SE-015 (The Debt Scale)</strong>. The entity measures the metaphysical weight of the obligation, issuing binding judgments that cannot be appealed.</p>

<h2 id="commercial-houses-and-m-a-w-trade">Commercial Houses &amp; M.A.W. Trade</h2>
<div class="table-wrap"><table class="data-table"><thead><tr><th>Trading House</th><th>Primary Commodity</th><th>Market Influence</th></tr></thead><tbody><tr><td><strong>The Gilded Ledger</strong></td><td>High-Grade Han-Canisters</td><td>Controls 60% of civilian energy distribution</td></tr><tr><td><strong>The Vault of Pledges</strong></td><td>Decommissioned M.A.W. Weapons</td><td>Licensed dealer for civilian self-defense equipment</td></tr><tr><td><strong>The Memory Brokerage</strong></td><td>Refined Memory Crystals</td><td>Supplies insight data to research institutions</td></tr></tbody></table></div>
</article>
<nav class="article-nav"><a href="the-wardens.html">← The Wardens</a><a href="the-underworld-and-wound-walkers.html">The Underworld &amp; Wound Walkers →</a></nav>
</main>
{get_floor_rail()}
</div>
{get_footer()}
</body></html>"""

    with open(os.path.join(FAC_DIR, "the-collectors.html"), "w", encoding="utf-8") as f:
        f.write(collectors_html)
    print("Generated factions/the-collectors.html")

    # 7. the-underworld-and-wound-walkers.html
    underworld_html = f"""<!doctype html><html lang="en" data-article-status="curated"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>The Underworld, Frays &amp; Wound Walkers — Somnarak Wiki</title><meta name="description" content="Subterranean criminal syndicates, independent Menders, and the legendary Wound Walkers"><link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg"><link rel="stylesheet" href="../assets/css/wiki.css"><script defer src="../assets/js/wiki.js"></script></head><body>
{get_header()}
<nav class="float-toc" aria-label="On this page"><button type="button" aria-expanded="false">CONTENTS</button><div><strong>ON THIS PAGE</strong><ol><li class="l2"><a href="#overview">Overview</a></li><li class="l2"><a href="#underground-profile">Underground Profile</a></li><li class="l2"><a href="#the-menders-suseonja">The Menders (수선자)</a></li><li class="l2"><a href="#the-criminal-frays">The Criminal Frays</a></li><li class="l2"><a href="#the-wound-walkers-company-4">The Wound Walkers (Company 4)</a></li></ol><a href="#content">↑ TOP</a></div></nav>
<div class="wiki-shell">
{get_left_rail()}
<main id="content"><div class="page-tabs"><span>Factions &amp; Guilds</span><b>SUBTERRANEAN &amp; INDEPENDENT</b></div><div class="breadcrumbs"><a href="../index.html">Main page</a><i>›</i><a href="index.html">Factions</a><i>›</i>The Underworld &amp; Wound Walkers</div>
<section class="department-hero" style="--floor:#f0a6c4"><img src="../assets/icons/ref_underworld.svg" alt=""><div><span>INDEPENDENT OPERATORS · SHADOW FACTIONS</span><h1>The Underworld &amp; Wound Walkers</h1><p>지하 세계와 상처 걷는 자 — Jiha Segye-gwa Sangcheo Geonneun Ja</p></div></section>
<blockquote class="motto" style="--floor:#f0a6c4">“The Directorate owns the Spire; the Council owns the Streets; but the deep conduits belong to those who know how to mend what the city discards.” — Shade Whisperer</blockquote>
<section class="department-overview"><div><h2 id="overview">Overview</h2><p class="lead">Beneath the orderly avenues of Somnarak lies a sprawling subterranean underworld of drainage conduits, abandoned mining shafts, and black-market lofts. In this shadowy network operate the <strong>Menders</strong> (수선자 — independent doctors and mechanics), the <strong>Frays</strong> (범죄 조직 — illicit contraband syndicates), and the legendary <strong>Wound Walkers</strong> (상처 걷는 자).</p><p>Surviving outside official Council charters, these underground factions provide essential black-market medical care, salvage discarded M.A.W. fragments, and maintain their own fragile codes of honor.</p></div><aside class="department-profile" style="--floor:#f0a6c4"><h2 id="underground-profile">Underworld Profile</h2><dl><dt>Domain</dt><dd>Subterranean Conduits beneath Zone B &amp; C</dd><dt>Primary Groups</dt><dd>Menders (Suseonja), Shades, Frays, Wound Walkers</dd><dt>Key Leaders</dt><dd>Sooah (Wound Walker Lead), Old Han the Mender</dd><dt>Primary Currency</dt><dd>Unregistered Han-Canisters &amp; Scrap Alloy</dd><dt>Signature Element</dt><dd>Grudge (Crimson) + Void (Pale White)</dd><dt>Relationship to Directorate</dt><dd>Covert Surveillance (Floor 7 Shadow Corps)</dd></dl></aside></section>
<article class="article-body">
<h2 id="the-menders-suseonja">The Menders (수선자 — Suseonja)</h2>
<p>The Menders are rogue surgeons, mental therapists, and unlicensed blacksmiths who treat citizens suffering from psychological Fracture or Han-burns. Because official Directorate infirmaries require mandatory debt registration with the Collectors, working-class citizens in Zone D frequently seek out Mender clinics for confidential treatment.</p>

<h2 id="the-criminal-frays">The Criminal Frays</h2>
<p>The criminal underworld is organized into syndicated syndicates known as <strong>Frays</strong> (올 — <em>Ol</em>). The Frays specialize in trafficking black-market M.A.W. items, smuggling outside relics from the Desolate past Gate 5, and laundering unregistered Han-canisters through subterranean distilleries.</p>
<div class="table-wrap"><table class="data-table"><thead><tr><th>Syndicate</th><th>Territory</th><th>Primary Operation</th></tr></thead><tbody><tr><td><strong>The Rust Claw Fray</strong></td><td>Zone D Sub-tier</td><td>Scrap metal salvage and unlicensed weapon modification</td></tr><tr><td><strong>The Silent Coin Fray</strong></td><td>Zone C Drainage Network</td><td>Counterfeiting debt tallies and black market pawn loans</td></tr><tr><td><strong>The Shadow Veil Fray</strong></td><td>Zone B Fissure Border</td><td>Trafficking raw Weeping fluid and acoustic narcotics</td></tr></tbody></table></div>

<h2 id="the-wound-walkers-company-4">The Wound Walkers (Company 4)</h2>
<p>In the post-Cycle era of Year 4,250+, a new faction known as the <strong>Wound Walkers</strong> (상처 걷는 자) emerged. Led by the wanderer <strong>Sooah</strong>, this group of ascetic pilgrims travels along the city’s deepest geological wound lines, utilizing specialized resonance needles to stitch closed open psychic fissures and bring final rest to lingering sorrow.</p>
</article>
<nav class="article-nav"><a href="the-collectors.html">← The Collectors</a><a href="index.html">Factions Hub →</a></nav>
</main>
{get_floor_rail()}
</div>
{get_footer()}
</body></html>"""

    with open(os.path.join(FAC_DIR, "the-underworld-and-wound-walkers.html"), "w", encoding="utf-8") as f:
        f.write(underworld_html)
    print("Generated factions/the-underworld-and-wound-walkers.html")

    # 8. factions/index.html (Factions Hub)
    factions_hub_html = f"""<!doctype html><html lang="en" data-article-status="curated"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Factions &amp; Guilds — Somnarak Wiki</title><meta name="description" content="Comprehensive directory of the political institutions, civil guilds, military forces, and underground syndicates of Somnarak"><link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg"><link rel="stylesheet" href="../assets/css/wiki.css"><script defer src="../assets/js/wiki.js"></script></head><body>
{get_header()}
<nav class="float-toc" aria-label="On this page"><button type="button" aria-expanded="false">CONTENTS</button><div><strong>ON THIS PAGE</strong><ol><li class="l2"><a href="#overview">Overview</a></li><li class="l2"><a href="#the-major-powers">The Major Powers</a></li><li class="l2"><a href="#institutional-directory">Institutional Directory</a></li><li class="l2"><a href="#power-matrix">Power &amp; Debt Matrix</a></li></ol><a href="#content">↑ TOP</a></div></nav>
<div class="wiki-shell">
{get_left_rail()}
<main id="content"><div class="page-tabs"><span>Factions &amp; Guilds</span><b>INSTITUTIONAL DIRECTORY</b></div><div class="breadcrumbs"><a href="../index.html">Main page</a><i>›</i>Factions</div>
<section class="wide-hero"><div><span>SOMNARAK POLITICAL &amp; CIVIC ARCHIVE</span><h1>Factions &amp; Guilds</h1><p>세력과 길드 기록 — Seryeok-gwa Gildeu Girok</p></div><img src="../assets/icons/banner_factions.svg" alt="Factions of Somnarak"></section>
<article class="article-body">
<h2 id="overview">Overview</h2>
<p>Power in Somnarak is distributed across an intricate web of scientific corporations, civil legislative councils, specialized artisan guilds, military garrisons, and underground syndicates. This registry indexes the governing bodies, commercial houses, and independent factions that maintain the delicate balance of metropolitan society.</p>

<h2 id="the-major-powers">The Major Powers</h2>
<div class="department-directory">
<a href="the-reverie-directorate.html" style="--floor:#ef5b55"><img src="../assets/layout/hand/icons/the_hand_dr_icon.svg" alt=""><span>CENTRAL POWER</span><b>The Reverie Directorate</b><small>Supreme Containment Authority · Floor 1–8</small></a>
<a href="the-high-council.html" style="--floor:#f1df76"><img src="../assets/icons/fac_council.svg" alt=""><span>CIVIL GOVERNANCE</span><b>The High Council</b><small>Council of Sighs · Legislative Authority</small></a>
<a href="the-architects.html" style="--floor:#f1df76"><img src="../assets/icons/fac_architects.svg" alt=""><span>ENGINEERING</span><b>The Architects</b><small>Master Builders &amp; Sorrow Masonry Guild</small></a>
<a href="the-weavers.html" style="--floor:#83d6ad"><img src="../assets/icons/fac_weavers.svg" alt=""><span>TEXTILE &amp; RESONANCE</span><b>The Weavers</b><small>Echo Gardens · Memory Filaments &amp; M.A.W. Suits</small></a>
<a href="the-wardens.html" style="--floor:#d7d7d7"><img src="../assets/icons/fac_wardens.svg" alt=""><span>MILITARY DEFENSE</span><b>The Wardens</b><small>Zone E Bulwark · Perimeter Artillery &amp; Veil</small></a>
<a href="the-collectors.html" style="--floor:#e6c94d"><img src="../assets/icons/fac_collectors.svg" alt=""><span>COMMERCE &amp; DEBT</span><b>The Collectors</b><small>Zone C · Banking, Debt Liens &amp; M.A.W. Trade</small></a>
<a href="the-underworld-and-wound-walkers.html" style="--floor:#f0a6c4"><img src="../assets/icons/ref_underworld.svg" alt=""><span>UNDERGROUND</span><b>Underworld &amp; Wound Walkers</b><small>Menders, Frays, and Pilgrims of the Fissure</small></a>
<a href="../characters/kael.html" style="--floor:#e8c25a"><img src="../assets/icons/ref_horizon_caravan.svg" alt=""><span>EXPEDITIONARY</span><b>The Horizon Caravan</b><small>The Drift Throne · Trans-Desolate Navigation</small></a>
</div>

<h2 id="institutional-directory">Institutional Directory</h2>
<div class="table-wrap"><table class="data-table"><thead><tr><th>Faction</th><th>Leadership</th><th>Primary Domain</th><th>Core Specialty</th><th>Resonant Signature</th></tr></thead><tbody>
<tr><td><a href="the-reverie-directorate.html"><strong>The Reverie Directorate</strong></a></td><td>Director Majin &amp; Nine Cores</td><td>The Hand of Change (Root Mass)</td><td>Entity Containment, M.A.W. Extraction, Veil Power</td><td>All Four Elements + Hope</td></tr>
<tr><td><a href="the-high-council.html"><strong>The High Council</strong></a></td><td>Chancellor Yul</td><td>Zone A Grand Rotunda</td><td>Civil Legislation, Municipal Tax, Public Works</td><td>Weight (Black) + Clarity</td></tr>
<tr><td><a href="the-architects.html"><strong>The Architects</strong></a></td><td>Master Ilan</td><td>Zone A Plumb Spire</td><td>Sorrow Masonry, Urban Grid, Containment Cells</td><td>Weight (Black) + Clarity</td></tr>
<tr><td><a href="the-weavers.html"><strong>The Weavers</strong></a></td><td>Master Soojin</td><td>Zone D Echo Gardens</td><td>Memory Spinning, Suit Linings, Acoustic Looms</td><td>Lament (Deep Blue) + Void</td></tr>
<tr><td><a href="the-wardens.html"><strong>The Wardens</strong></a></td><td>Border Lead Mellda</td><td>Zone E Aegis Bulwark</td><td>Perimeter Defense, Artillery, Outer Gates</td><td>Weight (Black) + Resolve</td></tr>
<tr><td><a href="the-collectors.html"><strong>The Collectors</strong></a></td><td>Grand Bailiff Gyeol</td><td>Zone C Collector’s Row</td><td>Banking, Debt Enforcement, Equipment Trade</td><td>Void (Pale White) + Weight</td></tr>
<tr><td><a href="the-underworld-and-wound-walkers.html"><strong>Underworld &amp; Frays</strong></a></td><td>Sooah &amp; Mender Elders</td><td>Subterranean Conduits</td><td>Illicit Healing, Black Markets, Fissure Stitching</td><td>Grudge (Crimson) + Void</td></tr>
</tbody></table></div>

<h2 id="power-matrix">Power &amp; Debt Matrix</h2>
<p>The factions are bound by mutual dependency: the Directorate provides energy; the Council allocates funds; the Architects build the walls; the Weavers line the armor; the Wardens defend the borders; the Collectors balance the books; and the Underworld absorbs the society’s discarded pain.</p>
</article>
</main>
{get_floor_rail()}
</div>
{get_footer()}
</body></html>"""

    with open(os.path.join(FAC_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(factions_hub_html)
    print("Generated factions/index.html")

build_faction_pages()
