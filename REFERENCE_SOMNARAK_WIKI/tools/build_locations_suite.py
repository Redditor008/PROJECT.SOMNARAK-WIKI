import os
import re

LOC_DIR = "/home/user/01_Somnarak_Wiki/locations"
os.makedirs(LOC_DIR, exist_ok=True)

from generate_all_characters import get_left_rail, get_floor_rail, get_header, get_footer

def build_locations_pages():
    # 1. zone-a-core-nexus.html
    za_html = f"""<!doctype html><html lang="en" data-article-status="curated"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Zone A: The Core Nexus — Somnarak Wiki</title><meta name="description" content="Detailed cartographic and municipal dossier for Zone A, the Alpha Tree, and the central spire"><link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg"><link rel="stylesheet" href="../assets/css/wiki.css"><script defer src="../assets/js/wiki.js"></script></head><body>
{get_header()}
<nav class="float-toc" aria-label="On this page"><button type="button" aria-expanded="false">CONTENTS</button><div><strong>ON THIS PAGE</strong><ol><li class="l2"><a href="#overview">Overview</a></li><li class="l2"><a href="#zone-profile">Zone Profile</a></li><li class="l2"><a href="#central-spire-and-alpha-tree">Central Spire &amp; Alpha Tree</a></li><li class="l2"><a href="#key-districts-and-landmarks">Key Districts &amp; Landmarks</a></li><li class="l2"><a href="#subterranean-interface-the-hand">Subterranean Interface (The Hand)</a></li></ol><a href="#content">↑ TOP</a></div></nav>
<div class="wiki-shell">
{get_left_rail()}
<main id="content"><div class="page-tabs"><span>Atlas &amp; Locations</span><b>MUNICIPAL CARTOGRAPHY</b></div><div class="breadcrumbs"><a href="../index.html">Main page</a><i>›</i><a href="index.html">Locations</a><i>›</i>Zone A</div>
<section class="department-hero" style="--floor:#47c978"><img src="../assets/layout/city/icons/icon_zone_a_core.svg" alt=""><div><span>METROPOLITAN ATLAS · ZONE A</span><h1>Zone A: The Core Nexus</h1><p>중심 구역 — Jungsim Guyeok (The Heart of the City)</p></div></section>
<blockquote class="motto" style="--floor:#47c978">“All roads spiral inward toward the Tree. All grief flows downward toward the roots.” — Municipal Inscription</blockquote>
<section class="department-overview"><div><h2 id="overview">Overview</h2><p class="lead"><strong>Zone A</strong> (The Core Nexus) is the geographical, political, and spiritual center of Somnarak. Enclosing the colossal 1,400-meter crystalline column of the <strong>Alpha Tree</strong>, Zone A houses the supreme governing institutions of the city: the Council of Sighs Grand Rotunda, the High Guild of Architects Spire, and the surface portals leading into the subterranean Hand of Change.</p><p>Surrounded by a pristine moat of purified resonance canals, Zone A enjoys the lowest ambient entity threat index and the highest concentration of crystalline energy.</p></div><aside class="department-profile" style="--floor:#47c978"><h2 id="zone-profile">District Profile</h2><dl><dt>Designation</dt><dd>Zone A — The Core Nexus (중심 구역)</dd><dt>Central Monument</dt><dd>The Alpha Tree (1,420m Spire)</dd><dt>Governing Authority</dt><dd>The High Council (Council of Sighs)</dd><dt>Resident Population</dt><dd>~65,000 citizens &amp; officials</dd><dt>Threat Index</dt><dd>Level 1 — Secure (ZAYIN Threshold)</dd><dt>Primary Access</dt><dd>The Four Radial Avenues &amp; Core Monorail</dd></dl></aside></section>
<article class="article-body">
<h2 id="central-spire-and-alpha-tree">Central Spire &amp; Alpha Tree</h2>
<p>The entire zone is constructed on concentric stone terraces radiating outward from the trunk of the Alpha Tree. The Tree’s massive petrified roots plunge thousands of meters into the subterranean crust, acting as the structural foundation for the city’s highest towers.</p>

<h2 id="key-districts-and-landmarks">Key Districts &amp; Landmarks</h2>
<div class="table-wrap"><table class="data-table"><thead><tr><th>District / Landmark</th><th>Location</th><th>Significance</th></tr></thead><tbody>
<tr><td><strong>The Grand Rotunda</strong></td><td>Lower Alpha Trunk</td><td>Parliamentary seat of the Council of Sighs and the Chancellor’s offices</td></tr>
<tr><td><strong>The Spire of Plumb Lines</strong></td><td>Zone A East Flank</td><td>Guildhall and drafting studios of the High Architects</td></tr>
<tr><td><strong>The Central Moat</strong></td><td>Zone A Perimeter Ring</td><td>Purified water barrier filtering out acoustic grief frequencies</td></tr>
<tr><td><strong>The Portal of the Palm</strong></td><td>Tree Root Bastion</td><td>Direct secure elevator access to Floor 1 Neutral Command</td></tr>
</tbody></table></div>

<h2 id="subterranean-interface-the-hand">Subterranean Interface (The Hand)</h2>
<p>Directly beneath the paved plazas of Zone A lies the eight-floor complex of the Hand of Change. Heavy acoustic dampening vaults ensure that entity suppression operations taking place in the lower levels do not disturb civilian governance above.</p>
</article>
<nav class="article-nav"><a href="index.html">← Atlas Hub</a><a href="zone-b-west-ward.html">Zone B: The West Ward →</a></nav>
</main>
{get_floor_rail()}
</div>
{get_footer()}
</body></html>"""

    with open(os.path.join(LOC_DIR, "zone-a-core-nexus.html"), "w", encoding="utf-8") as f:
        f.write(za_html)
    print("Generated locations/zone-a-core-nexus.html")

    # 2. zone-b-west-ward.html
    zb_html = f"""<!doctype html><html lang="en" data-article-status="curated"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Zone B: The West Ward (Old Lament) — Somnarak Wiki</title><meta name="description" content="Municipal dossier for Zone B, the Western Sector, the Maw perimeter, and the Whispering Masonry"><link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg"><link rel="stylesheet" href="../assets/css/wiki.css"><script defer src="../assets/js/wiki.js"></script></head><body>
{get_header()}
<nav class="float-toc" aria-label="On this page"><button type="button" aria-expanded="false">CONTENTS</button><div><strong>ON THIS PAGE</strong><ol><li class="l2"><a href="#overview">Overview</a></li><li class="l2"><a href="#zone-profile">Zone Profile</a></li><li class="l2"><a href="#the-cheongula-scars">The Cheongula Scars</a></li><li class="l2"><a href="#contained-and-ambient-entities">Contained &amp; Ambient Entities</a></li><li class="l2"><a href="#the-maw-perimeter-wall">The Maw Perimeter Wall</a></li></ol><a href="#content">↑ TOP</a></div></nav>
<div class="wiki-shell">
{get_left_rail()}
<main id="content"><div class="page-tabs"><span>Atlas &amp; Locations</span><b>MUNICIPAL CARTOGRAPHY</b></div><div class="breadcrumbs"><a href="../index.html">Main page</a><i>›</i><a href="index.html">Locations</a><i>›</i>Zone B</div>
<section class="department-hero" style="--floor:#6f7ee8"><img src="../assets/layout/city/icons/icon_zone_b_west.svg" alt=""><div><span>METROPOLITAN ATLAS · ZONE B</span><h1>Zone B: The West Ward</h1><p>서부 구역 — Seobu Guyeok (Old Lament &amp; The Maw)</p></div></section>
<blockquote class="motto" style="--floor:#6f7ee8">“Listen closely to the stone before you knock. In Zone B, the masonry answers back.” — West Ward Proverb</blockquote>
<section class="department-overview"><div><h2 id="overview">Overview</h2><p class="lead"><strong>Zone B</strong> (The West Ward), also known as <strong>Old Lament</strong> (옛 비탄), is the historical sector that bore the direct brunt of the Cheongula Incident in Year 180. Characterized by labyrinthine blue-slate architecture, weeping stone fountains, and the yawning chasm of <strong>The Maw</strong>, Zone B has the highest concentration of Lament-class entities in Somnarak.</p><p>Supervised from Floor 2 (The Maw’s Keep) and protected by specialized acoustic dampener arrays, Zone B houses scholars, memory archivists, and veteran containment squads.</p></div><aside class="department-profile" style="--floor:#6f7ee8"><h2 id="zone-profile">District Profile</h2><dl><dt>Designation</dt><dd>Zone B — The West Ward (서부 구역)</dd><dt>Primary Sector</dt><dd>SECTOR-B-01 &amp; SECTOR-B-02</dd><dt>Key Feature</dt><dd>The Maw Chasm (SE-1003) &amp; Whispering Walls</dd><dt>Dominant Element</dt><dd>Lament (Deep Blue)</dd><dt>Population Count</dt><dd>~110,000 citizens &amp; researchers</dd><dt>Threat Index</dt><dd>Level 3 — Hazardous (WAW / HE Ambient)</dd></dl></aside></section>
<article class="article-body">
<h2 id="the-cheongula-scars">The Cheongula Scars</h2>
<p>Much of Zone B was reconstructed following the catastrophic collapse of Shaft 7. The blue slate stones used in the masonry were quarried from the exposed lip of the Weeping, causing the entire district to absorb and re-emit ambient acoustic vibrations.</p>

<h2 id="contained-and-ambient-entities">Contained &amp; Ambient Entities</h2>
<p>Zone B is the primary habitat for several foundational Sorrow Entities:</p>
<ul>
<li><strong>SE-001 (The Orphaned Bell):</strong> Housed in the specialized Bell Tower of SECTOR-B-01.</li>
<li><strong>SE-009 (The Memory Weaver):</strong> Contained within the Library of Stolen Pasts in SECTOR-B-02.</li>
<li><strong>SE-011 (The Whispering Walls):</strong> Integrated directly into the ambient residential architecture of Old Lament.</li>
</ul>

<h2 id="the-maw-perimeter-wall">The Maw Perimeter Wall</h2>
<p>The western boundary of Zone B drops precipitously into the one-kilometer-wide abyss of the Maw. A cyclopean retaining wall reinforced with acoustic resonators prevents the chasm’s liquid grief vapors from spilling into residential boulevards.</p>
</article>
<nav class="article-nav"><a href="zone-a-core-nexus.html">← Zone A: Core Nexus</a><a href="zone-c-collectors-row.html">Zone C: Collector's Row →</a></nav>
</main>
{get_floor_rail()}
</div>
{get_footer()}
</body></html>"""

    with open(os.path.join(LOC_DIR, "zone-b-west-ward.html"), "w", encoding="utf-8") as f:
        f.write(zb_html)
    print("Generated locations/zone-b-west-ward.html")

    # 3. zone-c-collectors-row.html
    zc_html = f"""<!doctype html><html lang="en" data-article-status="curated"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Zone C: Collector's Row — Somnarak Wiki</title><meta name="description" content="Municipal dossier for Zone C, the Eastern Sector, commercial banking, pawn courts, and debt extraction"><link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg"><link rel="stylesheet" href="../assets/css/wiki.css"><script defer src="../assets/js/wiki.js"></script></head><body>
{get_header()}
<nav class="float-toc" aria-label="On this page"><button type="button" aria-expanded="false">CONTENTS</button><div><strong>ON THIS PAGE</strong><ol><li class="l2"><a href="#overview">Overview</a></li><li class="l2"><a href="#zone-profile">Zone Profile</a></li><li class="l2"><a href="#commercial-architecture">Commercial Architecture</a></li><li class="l2"><a href="#the-debt-courts-and-extraction">The Debt Courts &amp; Extraction</a></li><li class="l2"><a href="#the-subterranean-exchanges">The Subterranean Exchanges</a></li></ol><a href="#content">↑ TOP</a></div></nav>
<div class="wiki-shell">
{get_left_rail()}
<main id="content"><div class="page-tabs"><span>Atlas &amp; Locations</span><b>MUNICIPAL CARTOGRAPHY</b></div><div class="breadcrumbs"><a href="../index.html">Main page</a><i>›</i><a href="index.html">Locations</a><i>›</i>Zone C</div>
<section class="department-hero" style="--floor:#e6c94d"><img src="../assets/layout/city/icons/icon_zone_c_east.svg" alt=""><div><span>METROPOLITAN ATLAS · ZONE C</span><h1>Zone C: Collector's Row</h1><p>동부 구역 — Dongbu Guyeok (The Financial &amp; Debt District)</p></div></section>
<blockquote class="motto" style="--floor:#e6c94d">“In Zone C, every stone has a ledger number and every window has a balance.” — Merchant Proverb</blockquote>
<section class="department-overview"><div><h2 id="overview">Overview</h2><p class="lead"><strong>Zone C</strong> (The Eastern Sector), widely called <strong>Collector’s Row</strong> (수금가의 거리), is the bustling financial, commercial, and legal trading hub of Somnarak. Dominated by the grand banking palaces and pawn exchanges of the Collector Guild, Zone C processes the city’s economic transactions and debt tallies.</p><p>Coordinated with Floor 3 (Extraction Hall) and housing SE-014 (The Debt Eater) and SE-015 (The Debt Scale) in SECTOR-C-01, Zone C metabolizes municipal financial distress into refined Han-crystals.</p></div><aside class="department-profile" style="--floor:#e6c94d"><h2 id="zone-profile">District Profile</h2><dl><dt>Designation</dt><dd>Zone C — Collector's Row (동부 구역)</dd><dt>Primary Sector</dt><dd>SECTOR-C-01 (Collector Courts)</dd><dt>Dominant Guild</dt><dd>The High Guild of Collectors (수금가)</dd><dt>Dominant Element</dt><dd>Void (Pale White) + Weight (Black)</dd><dt>Population Count</dt><dd>~185,000 merchants, bankers, &amp; clerks</dd><dt>Threat Index</dt><dd>Level 2 — Controlled (TETH / HE Controlled)</dd></dl></aside></section>
<article class="article-body">
<h2 id="commercial-architecture">Commercial Architecture</h2>
<p>Zone C features towering neoclassical limestone facades adorned with gilded brass scale motifs. Broad avenues lined with exchange booths, pawn houses, and energy dispensaries accommodate heavy pedestrian and caravan traffic.</p>

<h2 id="the-debt-courts-and-extraction">The Debt Courts &amp; Extraction</h2>
<p>In the central court of SECTOR-C-01, debtors appear before Collector bailiffs to settle accounts through emotional extraction. When debts cannot be discharged in currency, the court authorizes controlled resonance exposure to SE-014 or SE-015, converting financial guilt into stabilized energy canisters.</p>

<h2 id="the-subterranean-exchanges">The Subterranean Exchanges</h2>
<p>Beneath the grand marble halls lie the drainage vaults and black-market exchanges where independent Menders and Frays trade decommissioned M.A.W. components and unregistered Han fuel cells.</p>
</article>
<nav class="article-nav"><a href="zone-b-west-ward.html">← Zone B: West Ward</a><a href="zone-d-forge-and-gardens.html">Zone D: Forge &amp; Gardens →</a></nav>
</main>
{get_floor_rail()}
</div>
{get_footer()}
</body></html>"""

    with open(os.path.join(LOC_DIR, "zone-c-collectors-row.html"), "w", encoding="utf-8") as f:
        f.write(zc_html)
    print("Generated locations/zone-c-collectors-row.html")

    # 4. zone-d-forge-and-gardens.html
    zd_html = f"""<!doctype html><html lang="en" data-article-status="curated"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Zone D: The Mantle (Forge &amp; Gardens) — Somnarak Wiki</title><meta name="description" content="Municipal dossier for Zone D, the Forge District, Echo Gardens, and the Colossus Migration Corridor"><link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg"><link rel="stylesheet" href="../assets/css/wiki.css"><script defer src="../assets/js/wiki.js"></script></head><body>
{get_header()}
<nav class="float-toc" aria-label="On this page"><button type="button" aria-expanded="false">CONTENTS</button><div><strong>ON THIS PAGE</strong><ol><li class="l2"><a href="#overview">Overview</a></li><li class="l2"><a href="#zone-profile">Zone Profile</a></li><li class="l2"><a href="#the-insight-forge-district">The Insight Forge District</a></li><li class="l2"><a href="#the-echo-gardens">The Echo Gardens</a></li><li class="l2"><a href="#the-colossus-migration-corridor">The Colossus Migration Corridor</a></li></ol><a href="#content">↑ TOP</a></div></nav>
<div class="wiki-shell">
{get_left_rail()}
<main id="content"><div class="page-tabs"><span>Atlas &amp; Locations</span><b>MUNICIPAL CARTOGRAPHY</b></div><div class="breadcrumbs"><a href="../index.html">Main page</a><i>›</i><a href="index.html">Locations</a><i>›</i>Zone D</div>
<section class="department-hero" style="--floor:#d67d32"><img src="../assets/layout/city/icons/icon_zone_d_flanks.svg" alt=""><div><span>METROPOLITAN ATLAS · ZONE D</span><h1>Zone D: The Mantle</h1><p>외곽 맨틀 — Oegwak Maenteul (The Forge &amp; Echo Gardens)</p></div></section>
<blockquote class="motto" style="--floor:#d67d32">“Where the hammer strikes metal in the east, the harp sings to the willows in the west.” — Artisan Maxim</blockquote>
<section class="department-overview"><div><h2 id="overview">Overview</h2><p class="lead"><strong>Zone D</strong> (The Mantle) is the sprawling industrial and biological ring encircling the inner city. Spanning two starkly contrasting cultural landscapes, Zone D contains the thunderous heavy industrial foundries of the <strong>Insight Forge District</strong> in SECTOR-D-01 and the tranquil, crystalline botanical sanctuaries of the <strong>Echo Gardens</strong>.</p><p>Zone D is also crossed by the permanent migration trench of <strong>SE-002 (The Grieving Colossus)</strong>, requiring specialized kinetic shock-absorbing architecture.</p></div><aside class="department-profile" style="--floor:#d67d32"><h2 id="zone-profile">District Profile</h2><dl><dt>Designation</dt><dd>Zone D — The Mantle (외곽 맨틀)</dd><dt>Key Districts</dt><dd>SECTOR-D-01 (Forge) &amp; The Echo Gardens</dd><dt>Dominant Guilds</dt><dd>The Weavers (West) &amp; Forge Smiths (East)</dd><dt>Resident Entities</dt><dd>SE-002 (Colossus Corridor), SE-005 (Mother)</dd><dt>Population Count</dt><dd>~240,000 artisans, smiths, &amp; refugees</dd><dt>Threat Index</dt><dd>Level 3 — Dynamic (WAW Transient)</dd></dl></aside></section>
<article class="article-body">
<h2 id="the-insight-forge-district">The Insight Forge District</h2>
<p>In the eastern sector of Zone D, dozens of blast furnaces and smelting refineries operate around the clock. Here, Cheonbulok refugee smiths and Directorate engineers forge M.A.W. weapon frames and vehicle armor plates from refined Grudge-crystal alloys.</p>

<h2 id="the-echo-gardens">The Echo Gardens</h2>
<p>In the western terraced sector, the Weaver Guild tends vast botanical groves where weeping willows and crystalline reeds filter urban acoustic noise. These gardens serve as convalescent grounds for recovering Fracture patients.</p>

<h2 id="the-colossus-migration-corridor">The Colossus Migration Corridor</h2>
<p>A broad, four-hundred-meter-wide stone avenue circles the midpoint of Zone D. This trench is the uncontained migration route of SE-002 (The Grieving Colossus). High Architects designed all intersecting bridges with hydraulic lift mechanisms to allow the colossus to pass without triggering municipal breaches.</p>
</article>
<nav class="article-nav"><a href="zone-c-collectors-row.html">← Zone C: Collector's Row</a><a href="zone-e-perimeter-bulwark.html">Zone E: Perimeter Bulwark →</a></nav>
</main>
{get_floor_rail()}
</div>
{get_footer()}
</body></html>"""

    with open(os.path.join(LOC_DIR, "zone-d-forge-and-gardens.html"), "w", encoding="utf-8") as f:
        f.write(zd_html)
    print("Generated locations/zone-d-forge-and-gardens.html")

    # 5. zone-e-perimeter-bulwark.html
    ze_html = f"""<!doctype html><html lang="en" data-article-status="curated"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Zone E: The Perimeter Bulwark — Somnarak Wiki</title><meta name="description" content="Municipal dossier for Zone E, the outer Aegis Wall, the Threshold, and Gates 1–5"><link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg"><link rel="stylesheet" href="../assets/css/wiki.css"><script defer src="../assets/js/wiki.js"></script></head><body>
{get_header()}
<nav class="float-toc" aria-label="On this page"><button type="button" aria-expanded="false">CONTENTS</button><div><strong>ON THIS PAGE</strong><ol><li class="l2"><a href="#overview">Overview</a></li><li class="l2"><a href="#zone-profile">Zone Profile</a></li><li class="l2"><a href="#the-aegis-wall-fortifications">The Aegis Wall Fortifications</a></li><li class="l2"><a href="#the-five-metropolitan-gates">The Five Metropolitan Gates</a></li><li class="l2"><a href="#gate-watch-command">Gate Watch Command</a></li></ol><a href="#content">↑ TOP</a></div></nav>
<div class="wiki-shell">
{get_left_rail()}
<main id="content"><div class="page-tabs"><span>Atlas &amp; Locations</span><b>MUNICIPAL CARTOGRAPHY</b></div><div class="breadcrumbs"><a href="../index.html">Main page</a><i>›</i><a href="index.html">Locations</a><i>›</i>Zone E</div>
<section class="department-hero" style="--floor:#d7d7d7"><img src="../assets/layout/city/icons/icon_zone_e_bulwark.svg" alt=""><div><span>METROPOLITAN ATLAS · ZONE E</span><h1>Zone E: The Perimeter Bulwark</h1><p>경계선 구역 — Gyeonggyeseon Guyeok (The Aegis Wall &amp; Gates)</p></div></section>
<blockquote class="motto" style="--floor:#d7d7d7">“Beyond this stone lies the Desolate. Look upon the horizon, remember your oaths, and let nothing cross unmeasured.” — Inscription at Gate 1</blockquote>
<section class="department-overview"><div><h2 id="overview">Overview</h2><p class="lead"><strong>Zone E</strong> (The Perimeter Bulwark), formally designated <strong>The Threshold</strong> (문턱), is the outermost defensive ring of Somnarak. Enclosing the city within a thirty-meter-tall basalt bulwark over forty kilometers in circumference, Zone E houses the Warden garrisons, artillery bastions, and the five monumental Gates that connect Somnarak to the Desolate.</p><p>Coordinated between Floor 5 (Border Watch) and Floor 8 (Gate Watch), Zone E repels Outside Sorrow incursions and controls all trade and expeditionary traffic.</p></div><aside class="department-profile" style="--floor:#d7d7d7"><h2 id="zone-profile">District Profile</h2><dl><dt>Designation</dt><dd>Zone E — The Perimeter Bulwark (경계선)</dd><dt>Primary Sector</dt><dd>SECTOR-E-01 (Fortress Threshold)</dd><dt>Garrison Force</dt><dd>The Municipal Wardens &amp; Gate Watch</dd><dt>Total Circumference</dt><dd>42.6 kilometers of fortified wall</dd><dt>Resident Population</dt><dd>~45,000 wardens, artillerists, &amp; scouts</dd><dt>Threat Index</dt><dd>Level 4 — Critical (ALEPH Perimeter Incursions)</dd></dl></aside></section>
<article class="article-body">
<h2 id="the-aegis-wall-fortifications">The Aegis Wall Fortifications</h2>
<p>The Aegis Wall is built of interlocking basalt slabs treated with Void-crystal glaze. Twelve heavily fortified bastions house pneumatic Han-artillery batteries capable of bombarding Outside Sorrow Entity tides (such as SE-003, The Wilderness Tide) before they reach the perimeter.</p>

<h2 id="the-five-metropolitan-gates">The Five Metropolitan Gates</h2>
<div class="table-wrap"><table class="data-table"><thead><tr><th>Gate</th><th>Cardinal Position</th><th>Primary Transit Function</th></tr></thead><tbody>
<tr><td><strong>Gate 1 (Dawn Gate)</strong></td><td>North-East</td><td>Main diplomatic and civilian trade portal connecting to northern caravan routes</td></tr>
<tr><td><strong>Gate 2 (Forge Gate)</strong></td><td>East</td><td>Heavy industrial freight transit for ore shipments and mineral slag</td></tr>
<tr><td><strong>Gate 3 (Maw Gate)</strong></td><td>West</td><td>Restricted military gate adjacent to the western lip of the Maw</td></tr>
<tr><td><strong>Gate 4 (Furnace Gate)</strong></td><td>South</td><td>Entry point for Cheonbulok refugee columns and scrap crawlers</td></tr>
<tr><td><strong>Gate 5 (Exile Gate)</strong></td><td>North-West</td><td>Sealed high-security gate commanded by Xyan (Floor 8 Gate Watch)</td></tr>
</tbody></table></div>

<h2 id="gate-watch-command">Gate Watch Command</h2>
<p>At Gate 5 stands the command fortress of Floor 8 Gate Watch. In Year 4,238, the returned Exile Xyan personally oversees the gatehouse, guiding Horizon Caravan expeditions into the uncharted wastes of Mugenhan.</p>
</article>
<nav class="article-nav"><a href="zone-d-forge-and-gardens.html">← Zone D: The Mantle</a><a href="the-desolate.html">The Desolate →</a></nav>
</main>
{get_floor_rail()}
</div>
{get_footer()}
</body></html>"""

    with open(os.path.join(LOC_DIR, "zone-e-perimeter-bulwark.html"), "w", encoding="utf-8") as f:
        f.write(ze_html)
    print("Generated locations/zone-e-perimeter-bulwark.html")

    # 6. the-desolate.html
    desolate_html = f"""<!doctype html><html lang="en" data-article-status="curated"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>The Desolate — Somnarak Wiki</title><meta name="description" content="Cartographic dossier for the vast, freezing liminal wilderness beyond Somnarak's perimeter walls"><link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg"><link rel="stylesheet" href="../assets/css/wiki.css"><script defer src="../assets/js/wiki.js"></script></head><body>
{get_header()}
<nav class="float-toc" aria-label="On this page"><button type="button" aria-expanded="false">CONTENTS</button><div><strong>ON THIS PAGE</strong><ol><li class="l2"><a href="#overview">Overview</a></li><li class="l2"><a href="#environmental-profile">Environmental Profile</a></li><li class="l2"><a href="#the-nature-of-the-wastes">The Nature of the Wastes</a></li><li class="l2"><a href="#outside-entities-and-phenomena">Outside Entities &amp; Phenomena</a></li><li class="l2"><a href="#the-desolate-highway">The Desolate Highway</a></li></ol><a href="#content">↑ TOP</a></div></nav>
<div class="wiki-shell">
{get_left_rail()}
<main id="content"><div class="page-tabs"><span>Atlas &amp; Locations</span><b>LIMINAL WILDERNESS</b></div><div class="breadcrumbs"><a href="../index.html">Main page</a><i>›</i><a href="index.html">Locations</a><i>›</i>The Desolate</div>
<section class="department-hero" style="--floor:#38bdf8"><img src="../assets/icons/ref_the_desolate.svg" alt=""><div><span>EXTERNAL ATLAS · LIMINAL WASTES</span><h1>The Desolate</h1><p>황량 — Hwangryang (The Endless Wilderness)</p></div></section>
<blockquote class="motto" style="--floor:#38bdf8">“The city is a spark in the dark; the Desolate is the night that watches the spark burn.” — Desolate Wanderer Saying</blockquote>
<section class="department-overview"><div><h2 id="overview">Overview</h2><p class="lead"><strong>The Desolate</strong> (황량) is the infinite, freezing wilderness stretching outward beyond the perimeter bulwarks of Somnarak. Characterized by shifting sands of crushed crystalline bone, sub-zero winds, and vast roving tides of Outside Sorrow, the Desolate separates the four isolated metropolitan centers of Mugenhan.</p><p>Home to approximately 16,000 nomadic wanderers, exiled Menders, and Outside Sorrow Entities, the Desolate is navigated by the Horizon Caravan aboard the <em>Drift Throne</em>.</p></div><aside class="department-profile" style="--floor:#38bdf8"><h2 id="environmental-profile">Wilderness Profile</h2><dl><dt>Designation</dt><dd>The Desolate (황량 — The Liminal Space)</dd><dt>Geographic Scope</dt><dd>Infinite expanse across Mugenhan</dd><dt>Ambient Temperature</dt><dd>-15°C to -45°C</dd><dt>Primary Hazard</dt><dd>Sorrow Sandstorms &amp; Void Amnesia</dd><dt>Dominant Entities</dt><dd>SE-003 (Tide), SE-007 (Brume), SE-884 (Tundra)</dd><dt>Nomadic Population</dt><dd>~16,000 wanderers &amp; clan scouts</dd><dt>Key Highway</dt><dd>The Trans-Desolate Caravan Route</dd></dl></aside></section>
<article class="article-body">
<h2 id="the-nature-of-the-wastes">The Nature of the Wastes</h2>
<p>Unlike ordinary earthly deserts, the soil of the Desolate is composed of pulverized silicate minerals and dormant Han-crystal dust. Exposure to the open wind without a resonant Veil lantern induces rapid hypothermia and gradual memory loss (<em>Void Erosion</em>).</p>

<h2 id="outside-entities-and-phenomena">Outside Entities &amp; Phenomena</h2>
<p>The Desolate is roamed by colossal Outside Sorrow Entities that have no fixed physical cells:</p>
<ul>
<li><strong>SE-003 (The Wilderness Tide):</strong> A sweeping, migratory storm of kinetic weight that rolls across the plains like an ocean tide.</li>
<li><strong>SE-007 (Brume):</strong> Phantasmal drifting fog banks that swallow landmarks and induce auditory mirages of lost homes.</li>
<li><strong>SE-884 (Seething Tundra):</strong> Glaciated plains where volcanic heat vents clash violently with frozen sorrow winds.</li>
</ul>

<h2 id="the-desolate-highway">The Desolate Highway</h2>
<p>In Year 4,238, Kael and the Horizon Caravan anchored the first permanent relay beacons across the southern wastes, creating a mapped corridor connecting Somnarak’s Gate 4 to the volcanic gates of Cheonbulok.</p>
</article>
<nav class="article-nav"><a href="zone-e-perimeter-bulwark.html">← Zone E: Perimeter Bulwark</a><a href="the-maw.html">The Maw →</a></nav>
</main>
{get_floor_rail()}
</div>
{get_footer()}
</body></html>"""

    with open(os.path.join(LOC_DIR, "the-desolate.html"), "w", encoding="utf-8") as f:
        f.write(desolate_html)
    print("Generated locations/the-desolate.html")

    # 7. the-maw.html
    maw_loc_html = f"""<!doctype html><html lang="en" data-article-status="curated"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>The Maw (The Great Chasm) — Somnarak Wiki</title><meta name="description" content="Geological and containment dossier for the bottomless chasm created during the Cheongula Incident"><link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg"><link rel="stylesheet" href="../assets/css/wiki.css"><script defer src="../assets/js/wiki.js"></script></head><body>
{get_header()}
<nav class="float-toc" aria-label="On this page"><button type="button" aria-expanded="false">CONTENTS</button><div><strong>ON THIS PAGE</strong><ol><li class="l2"><a href="#overview">Overview</a></li><li class="l2"><a href="#chasm-profile">Chasm Profile</a></li><li class="l2"><a href="#formation-and-depth">Formation &amp; Geological Depth</a></li><li class="l2"><a href="#the-weeping-confluence">The Weeping Confluence</a></li><li class="l2"><a href="#containment-keep-floor-2">Floor 2 Containment Keep</a></li></ol><a href="#content">↑ TOP</a></div></nav>
<div class="wiki-shell">
{get_left_rail()}
<main id="content"><div class="page-tabs"><span>Atlas &amp; Locations</span><b>GEOLOGICAL ABYSS</b></div><div class="breadcrumbs"><a href="../index.html">Main page</a><i>›</i><a href="index.html">Locations</a><i>›</i>The Maw</div>
<section class="department-hero" style="--floor:#6f7ee8"><img src="../assets/icons/art_maw.svg" alt=""><div><span>GEOLOGICAL DOSSIER · ZONE B CRATER</span><h1>The Maw</h1><p>입구 — Ipgu (The Maw / The Great Chasm)</p></div></section>
<blockquote class="motto" style="--floor:#6f7ee8">“It does not chew; it waits. It was opened by a scream, and it will remain open until the river runs dry.” — Containment Officer Dekan</blockquote>
<section class="department-overview"><div><h2 id="overview">Overview</h2><p class="lead"><strong>The Maw</strong> (입구 — <em>Ipgu</em>), cataloged in the entity registry as <strong>SE-1003</strong>, is the colossal, bottomless geological chasm situated in Western Zone B. Created during the Cheongula Incident of Year 180 when Shaft 7 collapsed into the subterranean river of the Weeping, the Maw spans over one kilometer across and plunges into unmeasured subterranean depths.</p><p>Surrounded by a heavy ring of titanium-alloy retaining bulkheads and acoustic resonators, the Maw is permanently garrisoned by the containment teams of Floor 2 (The Maw’s Keep).</p></div><aside class="department-profile" style="--floor:#6f7ee8"><h2 id="chasm-profile">Chasm Profile</h2><dl><dt>Geological Feature</dt><dd>The Maw (입구 — The Abyss)</dd><dt>Location</dt><dd>Zone B Western Sector</dd><dt>Width / Depth</dt><dd>1.2 km diameter / Depth unmeasured (&gt;5,000m)</dd><dt>Origin Date</dt><dd>Year 180 (Cheongula Catastrophe)</dd><dt>Primary Inflow</dt><dd>The Subterranean Weeping River</dd><dt>Guard Unit</dt><dd>Floor 2 Maw's Keep Garrison</dd><dt>Entity Classification</dt><dd>Normal Object SE (SE-1003 · ALEPH-tier)</dd></dl></aside></section>
<article class="article-body">
<h2 id="formation-and-depth">Formation &amp; Geological Depth</h2>
<p>The chasm opened when over-pressurized Weeping fluid flash-evaporated, liquifying the structural granite bedrock beneath thirty city blocks. Sonar and resonant probes deployed into the Maw have recorded continuous acoustic echoes extending deeper than five thousand meters without detecting a solid floor.</p>

<h2 id="the-weeping-confluence">The Weeping Confluence</h2>
<p>Luminescent blue liquid grief continuously cascades down the sheer interior walls of the Maw in massive subterranean waterfalls. The mist rising from these cascades generates a permanent micro-climate of heavy humidity and subsonic auditory whispers in western Zone B.</p>

<h2 id="containment-keep-floor-2">Floor 2 Containment Keep</h2>
<p>The Directorate constructed <strong>The Maw’s Keep</strong> (Floor 2 of the Hand of Change) directly along the subterranean perimeter shelf of the chasm. Here, Containment Lead Dekan’s squads monitor the water levels and maintain the acoustic baffles that prevent the chasm from expanding eastward toward the Alpha Tree.</p>
</article>
<nav class="article-nav"><a href="the-desolate.html">← The Desolate</a><a href="index.html">Atlas Hub →</a></nav>
</main>
{get_floor_rail()}
</div>
{get_footer()}
</body></html>"""

    with open(os.path.join(LOC_DIR, "the-maw.html"), "w", encoding="utf-8") as f:
        f.write(maw_loc_html)
    print("Generated locations/the-maw.html")

    # 8. locations/index.html (Locations Hub)
    loc_hub_html = f"""<!doctype html><html lang="en" data-article-status="curated"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Metropolitan Atlas &amp; Locations — Somnarak Wiki</title><meta name="description" content="Comprehensive geographic directory and interactive atlas for Somnarak Zones A–E, The Maw, and the Desolate"><link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg"><link rel="stylesheet" href="../assets/css/wiki.css"><script defer src="../assets/js/wiki.js"></script></head><body>
{get_header()}
<nav class="float-toc" aria-label="On this page"><button type="button" aria-expanded="false">CONTENTS</button><div><strong>ON THIS PAGE</strong><ol><li class="l2"><a href="#overview">Overview</a></li><li class="l2"><a href="#full-size-map-blueprints">Full-Size Map Blueprints</a></li><li class="l2"><a href="#five-concentric-zones">The Five Concentric Zones</a></li><li class="l2"><a href="#external-and-geological-regions">External &amp; Geological Regions</a></li><li class="l2"><a href="#municipal-register">Municipal Register</a></li></ol><a href="#content">↑ TOP</a></div></nav>
<div class="wiki-shell">
{get_left_rail()}
<main id="content"><div class="page-tabs"><span>Atlas &amp; Locations</span><b>METROPOLITAN ATLAS</b></div><div class="breadcrumbs"><a href="../index.html">Main page</a><i>›</i>Locations</div>
<section class="wide-hero"><div><span>SOMNARAK CARTOGRAPHIC REGISTRY</span><h1>Metropolitan Atlas &amp; Locations</h1><p>도시 지리지와 구역 기록 — Dosi Jiriji-gwa Guyeok Girok</p></div><img src="../assets/icons/banner_locations.svg" alt="Atlas of Somnarak"></section>
<article class="article-body">
<h2 id="overview">Overview</h2>
<p>Somnarak is engineered in five concentric geometric zones radiating outward from the Alpha Tree in Zone A to the cyclopean perimeter bulwarks of Zone E. Beyond the walls lies the boundless wilderness of the Desolate, while deep beneath Western Zone B yawns the catastrophic abyss of the Maw.</p>

<h2 id="full-size-map-blueprints">Full-Size Map Blueprints</h2>
<p>Explore high-resolution vector blueprints of the facility and the city:</p>
<div class="archive-portal-grid">
<a class="archive-portal" href="../atlas/somnarak-city-map.html" style="--portal:#a78bfa"><span>METROPOLIS</span><img src="../assets/layout/city/icons/somnarak_city_icon.svg" alt=""><b>SOMNARAK CITY MAP</b><small>Readable vector atlas of Zones A–E &amp; Gates</small></a>
<a class="archive-portal" href="../atlas/hand-of-change-map.html" style="--portal:#4cc9f0"><span>FACILITY</span><img src="../assets/layout/hand/icons/the_hand_dr_icon.svg" alt=""><b>HAND OF CHANGE CUTAWAY</b><small>Full 1,800px Directorate blueprint</small></a>
</div>

<h2 id="five-concentric-zones">The Five Concentric Zones</h2>
<div class="department-directory">
<a href="zone-a-core-nexus.html" style="--floor:#47c978"><img src="../assets/layout/city/icons/icon_zone_a_core.svg" alt=""><span>ZONE A</span><b>The Core Nexus</b><small>The Alpha Tree, Council Rotunda, Plumb Spire</small></a>
<a href="zone-b-west-ward.html" style="--floor:#6f7ee8"><img src="../assets/layout/city/icons/icon_zone_b_west.svg" alt=""><span>ZONE B</span><b>The West Ward</b><small>Old Lament, Whispering Masonry, Maw Lip</small></a>
<a href="zone-c-collectors-row.html" style="--floor:#e6c94d"><img src="../assets/layout/city/icons/icon_zone_c_east.svg" alt=""><span>ZONE C</span><b>Collector's Row</b><small>Commercial Banks, Pawn Courts, Debt Eater Access</small></a>
<a href="zone-d-forge-and-gardens.html" style="--floor:#d67d32"><img src="../assets/layout/city/icons/icon_zone_d_flanks.svg" alt=""><span>ZONE D</span><b>The Mantle</b><small>Insight Forge, Echo Gardens, Colossus Corridor</small></a>
<a href="zone-e-perimeter-bulwark.html" style="--floor:#d7d7d7"><img src="../assets/layout/city/icons/icon_zone_e_bulwark.svg" alt=""><span>ZONE E</span><b>The Perimeter Bulwark</b><small>Aegis Wall, Fortress Threshold, Gates 1–5</small></a>
</div>

<h2 id="external-and-geological-regions">External &amp; Geological Regions</h2>
<div class="contents-grid">
<section>
<h3>The Outer Wastes</h3>
<a href="the-desolate.html"><strong>The Desolate (황량)</strong><br><small>Endless freezing wilderness, shifting Han-flow lines</small></a>
<a href="../characters/kael.html"><strong>The Desolate Highway</strong><br><small>Beacon-marked route connecting to Cheonbulok</small></a>
</section>
<section>
<h3>Subterranean Abyss</h3>
<a href="the-maw.html"><strong>The Maw (입구)</strong><br><small>The 1.2km chasm created by the Cheongula Incident</small></a>
<a href="../lore/somnarak-cosmology.html#the-river-of-liquid-grief-the-weeping"><strong>The Weeping River</strong><br><small>Subterranean river of liquid grief feeding all Han</small></a>
</section>
</div>

<h2 id="municipal-register">Municipal Register</h2>
<div class="table-wrap"><table class="data-table"><thead><tr><th>District</th><th>Governing Body</th><th>Key Landmark</th><th>Resident Population</th><th>Threat Rating</th></tr></thead><tbody>
<tr><td><a href="zone-a-core-nexus.html"><strong>Zone A (Core Nexus)</strong></a></td><td>The High Council</td><td>The Alpha Tree (1,420m)</td><td>~65,000</td><td>Level 1 (Secure)</td></tr>
<tr><td><a href="zone-b-west-ward.html"><strong>Zone B (West Ward)</strong></a></td><td>Floor 2 / Keepers</td><td>Old Lament &amp; Bell Tower</td><td>~110,000</td><td>Level 3 (Hazardous)</td></tr>
<tr><td><a href="zone-c-collectors-row.html"><strong>Zone C (Collector's Row)</strong></a></td><td>The Collectors</td><td>The Exchange of Scales</td><td>~185,000</td><td>Level 2 (Controlled)</td></tr>
<tr><td><a href="zone-d-forge-and-gardens.html"><strong>Zone D (The Mantle)</strong></a></td><td>Weavers &amp; Smiths</td><td>Forge District &amp; Gardens</td><td>~240,000</td><td>Level 3 (Dynamic)</td></tr>
<tr><td><a href="zone-e-perimeter-bulwark.html"><strong>Zone E (Bulwark)</strong></a></td><td>The Wardens</td><td>The Aegis Wall &amp; Gate 1–5</td><td>~45,000</td><td>Level 4 (Critical)</td></tr>
<tr><td><a href="the-desolate.html"><strong>The Desolate</strong></a></td><td>Horizon Caravan</td><td>The Drift Highway</td><td>~16,000</td><td>Level 5 (Extreme)</td></tr>
<tr><td><a href="the-maw.html"><strong>The Maw</strong></a></td><td>Floor 2 Maw's Keep</td><td>Subterranean Cascades</td><td>Garrison Only</td><td>Level 5 (Uncontained)</td></tr>
</tbody></table></div>
</article>
</main>
{get_floor_rail()}
</div>
{get_footer()}
</body></html>"""

    with open(os.path.join(LOC_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(loc_hub_html)
    print("Generated locations/index.html")

build_locations_pages()
