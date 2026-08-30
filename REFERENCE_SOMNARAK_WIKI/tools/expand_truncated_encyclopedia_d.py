#!/usr/bin/env python3
"""Second-pass expansion for wars, ops, tech, facility, watches, locations. Floor ≠ cap."""
from __future__ import annotations

import importlib.util
import json
import pathlib
import re

TOOLS = pathlib.Path("/home/user/PROJECT.SOMNARAK-WIKI/REFERENCE_SOMNARAK_WIKI/tools")
spec = importlib.util.spec_from_file_location("purge_old_wrong_batch", TOOLS / "purge_old_wrong_batch.py")
purge = importlib.util.module_from_spec(spec)
spec.loader.exec_module(purge)
wrap = purge.wrap
DOCS = purge.DOCS
SEARCH = []


def wc(html: str) -> int:
    m = re.search(r"<main[^>]*>(.*)</main>", html, re.S)
    body = m.group(1) if m else html
    return len(re.findall(r"[A-Za-z0-9']+", re.sub(r"<[^>]+>", " ", body)))


def put(rel, title, desc, crumbs, h1, eyebrow, toc, body, cats, kw):
    doc = wrap(title, desc, crumbs, h1, eyebrow, toc, body, cats)
    (DOCS / rel).write_text(doc, encoding="utf-8")
    print(f"wrote {rel} ({wc(doc)}w)")
    SEARCH.append({"url": rel, "title": title, "description": desc[:200], "keywords": kw, "type": "article"})


def wars():
    body = r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>There was no “First Sovereign War” against “Old Dreamers” and “Founding Corporations.” That overlay was wiki invention. Canon wars from History:</p>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>War</th><th>Name</th><th>Cause</th><th>Outcome</th></tr></thead>
<tbody>
<tr><td>1st</td><td>The Cheongula (천구라)</td><td>Han consumed 1,000 citizens</td><td>Proof the city is alive and hungry. The Maw.</td></tr>
<tr><td>2nd</td><td>The Occlusihan (오클루시한)</td><td>Six factions tried to seal Han</td><td>Failed. Han grew. Fracture emerged.</td></tr>
<tr><td>3rd</td><td>The Consolihan (결한 전쟁)</td><td>Destabilized accumulation</td><td>Solidification. The Alpha Tree. Fortress of frozen tears.</td></tr>
<tr><td>4th (?)</td><td>The Third Conflict</td><td>Preservation vs reform</td><td>Council fatalism — or an ongoing cold war.</td></tr>
</tbody></table></div>
<p>Time is counted ~6,000 years from the first Zone B settlement. Cheongula year 202. Occlusihan 202–223. Interim 223–234. Consolihan 234–245. Structuring 245–281. SED ~4200. Directorate 4202. Present Dawn Initiative ~4232–4238. Full Cheongula article: <a href="the-cheongula-incident.html">the Cheongula</a>. Ages: <a href="the-three-ages-and-history.html">three ages</a>.</p>
</section>
<section class="wiki-section" id="cheongula"><h2 class="section-title">Cheongula — the First Sorrow</h2>
<p>Korean <em>Cheon</em> (천 — thousand) + Latin <em>gula</em> (throat, maw). The Maw of the Thousand. <em>“We thought the walls were just cold. We didn’t know they were starving.”</em></p>
<p>Early settlers treated Han as inert metaphysical concrete. One night in mid-layer Zone B the accumulation of unresolved grief went critical. Streets, beams, walls softened into black tar. Exactly 1,000 citizens were dragged down, digested, assimilated — bodies, memories, loves, terrors broken into structural material. When the tar re-solidified, the buildings had new jagged shapes and the concrete whispered.</p>
<p>What it proved: Han is hungry, living, predatory. The city consumes people to stay standing. The site is now the Maw. This page is the war that followed. The incident itself stays on its own article.</p>
</section>
<section class="wiki-section" id="occlusihan"><h2 class="section-title">Occlusihan — the First War</h2>
<p>Latin <em>occlusio</em> (to shut) + Han. The War to Seal the Grief. After the Cheongula, the populace realized they were living inside a cage that was slowly eating them. Panic bred fanaticism. Six early factions — corporate, religious, militaristic — rose. They disagreed on <em>how</em>. They agreed on one desperate goal: close, seal, or sever the flow of Han entirely. They fought in Zone B, and they fought the city itself. Han answered — growing, shifting, consuming.</p>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>Faction</th><th>Approach</th><th>Outcome</th></tr></thead>
<tbody>
<tr><td>Sealers</td><td>Walls, barriers, physical block</td><td>Pressure points. Han erupted.</td></tr>
<tr><td>Severers</td><td>Cut Han from people — emotional suppression</td><td>Numb zones. Fracture hotspots.</td></tr>
<tr><td>Offerers</td><td>Sacrifice, ritual, feed it willingly</td><td>Han grew stronger.</td></tr>
<tr><td>Exilers</td><td>Push grief into Dream or Abyss</td><td>Rifts between realms.</td></tr>
<tr><td>Converters</td><td>Transmute Han into something else</td><td>Partial success. Ancestor of Architect practice.</td></tr>
<tr><td>Endurers</td><td>Accept hunger. Learn to live with it</td><td>Ancestor of Council fatalism.</td></tr>
</tbody></table></div>
<p>Nobody won. Twenty-one years. Exhaustion became the Consolihan. Lesson filed by every later Head: fighting Han directly feeds it; severing it Fractures people; feeding it makes it hungrier. Working with it is the only partial success. Remembered as: <em>“We tried to kill the sorrow. The sorrow ate us instead.”</em> RD, SED, and UCD are Year 4,200 operations, not these six.</p>
</section>
<section class="wiki-section" id="consolihan"><h2 class="section-title">Consolihan</h2>
<p>Latin <em>consolidare</em> + Han. The Solidification of Grief. Not a war against an army. A war to freeze a tide. <em>“In the beginning, Han was a fluid, rising tide that threatened to drown us all. During the Consolihan, they learned how to freeze the water, building a fortress out of our frozen tears. The Alpha Tree is simply the tallest pillar.”</em></p>
<p>After Occlusihan the six interventions had wrecked Han’s (predatory) flow. Sorrow pooled into rivers, flooded valleys, ate settlements. Survivors tried release-rituals, offerings to Dream, pleas to Abyss. Nothing worked. Then they combined Converter technique with Endurer philosophy and tried to <strong>solidify</strong> it — freeze flowing sorrow into something that could be shaped, contained, managed.</p>
<p>It worked, not as planned. Han did not freeze into inert material. It crystallized into <strong>meaning</strong>. Grief, love, dream, nightmare, happiness, sadness poured into the solidifying Han. Where feeling gathered hardest, the <strong>Alpha Tree</strong> grew — not a building, a cumulation. Sigh Palace weeps. Six buildings hold. Spire of Dreams reaches. Abyssal Well drops. Archive light is rare. Crucible weight anchors.</p>
<p>The city grew around the Tree the way crystal grows on crystal. Taboos were first codified after this war; Giltong exist because Consolihan proved the city needed an immune system, not just walls. Calendar-zero for civic structure sits here. See <a href="the-alpha-tree.html">Alpha Tree</a> and <a href="../locations/zone-a-core-nexus.html">Zone A</a>.</p>
</section>
<section class="wiki-section" id="timeline"><h2 class="section-title">Timeline</h2>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>Year</th><th>Event</th><th>Zone</th></tr></thead>
<tbody>
<tr><td>~0</td><td>First settlement around Han pools</td><td>B</td></tr>
<tr><td>~0–202</td><td>Before-Time — Han flowing, structures from necessity</td><td>B</td></tr>
<tr><td>202</td><td>Cheongula — 1,000 consumed</td><td>B (Maw)</td></tr>
<tr><td>202–223</td><td>Occlusihan — 21 years</td><td>B</td></tr>
<tr><td>223–234</td><td>Interim — accumulation catastrophic</td><td>All</td></tr>
<tr><td>234–245</td><td>Consolihan — Solidification, Tree</td><td>A</td></tr>
<tr><td>245–254</td><td>Zone C constructed</td><td>C</td></tr>
<tr><td>254–267</td><td>Zone D built to contain B’s chaos</td><td>D</td></tr>
<tr><td>267–281</td><td>Zone E fortified; city complete</td><td>E</td></tr>
<tr><td>~4200</td><td>SED decreed</td><td>All</td></tr>
<tr><td>4202</td><td>Reverie Directorate founded</td><td>A</td></tr>
<tr><td>~4232–4238</td><td>Present / Dawn Initiative</td><td>All</td></tr>
</tbody></table></div>
<p>Durations: Before-Time ~202 years. The Wars 43 years (202–245). Structuring 36 years (245–281). Long Era ~3,900 years (281–4200) — working centuries; faction betrayals of Years 2,200–4,200 accumulate here. Current era from 4202. Discard: Old Dreamers, Founding Corporations as precursor Wings, Nine Veiled Edicts as LC seed-of-light copy. Use <a href="../factions/the-founding-corporations.html">the three operations</a> for R.D./SED/UCD.</p>
</section>
"""
    put(
        "lore/the-first-sovereign-war.html",
        "The Wars of Somnarak",
        "Cheongula, Occlusihan, Consolihan — six factions, Solidification, timeline 0–281 and the present age. Not a Sovereign War of Old Dreamers.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Lore</a> <i>/</i> <span>Wars of Somnarak</span>',
        "The Wars of Somnarak",
        "LORE · HISTORY · 202–245",
        [
            ("overview", "Overview"),
            ("cheongula", "Cheongula"),
            ("occlusihan", "Occlusihan"),
            ("consolihan", "Consolihan"),
            ("timeline", "Timeline"),
        ],
        body,
        '<a href="index.html">Lore</a> | <a href="the-cheongula-incident.html">Cheongula</a> | <a href="the-alpha-tree.html">Alpha Tree</a>',
        "Occlusihan Consolihan Cheongula Alpha Tree Wars Sealers Converters Endurers",
    )


def three_ops():
    body = r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>Somnarak does not have “founding precursor corporations” in the Wing/Fixer sense. It has <strong>three operations</strong> in the present age, all after year 4200. Source file title says “Three Corporations”; the civic fact is three missions, one city, shared sorrow.</p>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>Operation</th><th>Abbrev.</th><th>Mission</th><th>Article</th></tr></thead>
<tbody>
<tr><td>Reverie Directorate</td><td>R.D.</td><td>Contain Sorrow Entities, extract M.A.W., run Facility 01 under the Alpha Tree. Founded 4202. Resonance: Extraction.</td><td><a href="the-reverie-directorate.html">Directorate</a></td></tr>
<tr><td>Somnarak Exploration Decreed</td><td>SED</td><td>Map the unmapped — Corner cities, Desolate edges, forgotten districts. Council decree ~4200.</td><td><a href="the-sed-corps.html">SED</a></td></tr>
<tr><td>Underworld Cleanup Descend</td><td>UCD</td><td>Fray raids, Wash District, black-market Han. Combat descent, not a Wing.</td><td><a href="the-ucd-strike-force.html">UCD</a></td></tr>
</tbody></table></div>
<p>The old page pasted the entire game-framework chapter (casts, loops, Hand of Hope ending) onto this URL. That dump is gone. Cast stays on character pages. Absolvohan stays on <a href="../lore/the-cycle-and-absolvohan.html">the Cycle</a>. Hand of Hope stays on <a href="../entities/hope-transformations.html">Hope Transformations</a>. SED Canto text and UCD Arc text stay on those long articles.</p>
</section>
<section class="wiki-section" id="each"><h2 class="section-title">What each is</h2>
<p><strong>R.D.</strong> — containment facility in the Tree’s roots. Daily work is assignment, Work Types, Han-Energy, M.A.W. extraction, Ordeal response, breach return. Story through-line is the Absolvohan, which the Council is not meant to have. Weavers are watching it in Dream anyway.</p>
<p><strong>SED</strong> — exploration force into the Undercity, Forgotten Districts, Deep Gardens, Border Tunnels, the Scar, the Desolate. Mapping, entity encounters that are not always combat, environmental Han-hazards, moral choices about what to take home. Seven arcs in source, from Undercity toward the Source. Cast (Yeonhwa, Doha, Harin, Sora, Minjae, Jisoo, the Silent One) lives on character pages, not here.</p>
<p><strong>UCD</strong> — combat descent against Frays. Intelligence, infiltration, confrontation, choice. The Wash District is Arc 2. They hit the people who feed on what leaks from R.D. cells and SED maps.</p>
</section>
<section class="wiki-section" id="connect"><h2 class="section-title">How they connect</h2>
<p>The Council funds the Directorate and does not fully understand it. SED walks what the facility will later have to contain. UCD hits the Frays that feed on what leaks from both. Menders contract to RD and Architects at once. Wardens back all three and trust none of the paperwork.</p>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>Event</th><th>R.D.</th><th>SED</th><th>UCD</th></tr></thead>
<tbody>
<tr><td>Entity breach</td><td>Containment failure</td><td>Exploration disrupted</td><td>Crime increases</td></tr>
<tr><td>Fray operation</td><td>Security threat</td><td>Dangerous territory</td><td>Direct conflict</td></tr>
<tr><td>Han-storm</td><td>Facility stress</td><td>Environmental hazard</td><td>Border threat</td></tr>
<tr><td>Sorrow Tide</td><td>Energy surge</td><td>Entity agitation</td><td>Criminal activity</td></tr>
<tr><td>Cheongula anniversary</td><td>Maw activity</td><td>Undercity disturbance</td><td>Mourning period</td></tr>
</tbody></table></div>
<p>One story, three tellings: R.D. is containment — how the city manages sorrow. SED is discovery — what lies under the surface. UCD is justice — how the city confronts its crimes. Together they show a city built on sorrow, powered by grief, haunted by the Cheongula. Shared world: Zones A–E, the Desolate, Cheonbulok and Mugeukji as Corner cities, the Gate.</p>
</section>
<section class="wiki-section" id="not-wings"><h2 class="section-title">Not Wings</h2>
<p>Do not map R.D. to Lobotomy Corporation, SED to Limbus, UCD to a Fixer Office and call them precursor corporations. Analog research belongs in REFERENCE, not in this article’s heading stack. If you need the six Occlusihan factions (Sealers, Severers, Offerers, Exilers, Converters, Endurers), that is <a href="../lore/the-first-sovereign-war.html">the wars</a>, year 202–223, not year 4202.</p>
</section>
"""
    put(
        "factions/the-founding-corporations.html",
        "The Three Operations",
        "R.D., SED, and UCD — present-age operations after 4200, shared events, not founding precursor corporations.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Factions</a> <i>/</i> <span>Three Operations</span>',
        "The Three Operations",
        "FACTION · R.D. · SED · UCD",
        [
            ("overview", "Overview"),
            ("each", "What each is"),
            ("connect", "How they connect"),
            ("not-wings", "Not Wings"),
        ],
        body,
        '<a href="the-reverie-directorate.html">Directorate</a> | <a href="the-sed-corps.html">SED</a> | <a href="the-ucd-strike-force.html">UCD</a>',
        "Three Operations Reverie Directorate SED UCD not founding corporations",
    )


def faction_tech():
    body = r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>This page is an <strong>index of unique tools</strong>, not a paste of <code>SOMNARAK_FACTION_TECH.md</code>. Each guild article has a Tools section with the long description — appearance, how it works, unique trait. Resonances (Weight, Shaping, Scales, Archive, Barrier, Dream, Extraction) are not devices — they are <a href="../mechanics/taboo-resonance-mechanics.html">ways of touching Han</a>. M.A.W. is extracted sorrow, not faction tech.</p>
<p>A tool that judges its user (Ledger, Blade, Scale) is still a tool. A Place that eats visitors (Memory Archive under the Tree) is entity geography. Do not paste the nineteen tech chapters back onto this URL for “completeness.”</p>
</section>
<section class="wiki-section" id="guilds"><h2 class="section-title">Guild instruments</h2>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>Faction</th><th>Tools</th><th>What they do</th><th>Unique trait</th><th>Article</th></tr></thead>
<tbody>
<tr><td>Council</td><td>Sigh Recorder, Decision Scale</td><td>Store exhaled burden; weigh a decision’s sorrow (not its joy)</td><td>The Scale does not weigh happiness</td><td><a href="the-high-council.html">Council</a></td></tr>
<tr><td>Architects</td><td>Sorrow Compass, Han-Trowel</td><td>Find Han-flow; cut and seal crystal with the user’s feeling</td><td>The trowel cuts only as honestly as the hand</td><td><a href="the-architects.html">Architects</a></td></tr>
<tr><td>Collectors</td><td>Debt-Ledger, Extraction Glove</td><td>Show weight; pull Echoes</td><td>Both judge malice; the glove makes the Collector feel the debtor</td><td><a href="the-collectors.html">Collectors</a></td></tr>
<tr><td>Keepers</td><td>Memory Lens, Whispering Index</td><td>Play Echoes; catalog that speaks in riddles</td><td>Lens mixes the viewer in; Index may be alive</td><td><a href="the-keepers.html">Keepers</a></td></tr>
<tr><td>Wardens</td><td>Barrier Baton, Watchtower Eye</td><td>Suppression field; Desolate scan</td><td>Baton absorbs grief; Eye sees feeling</td><td><a href="the-wardens.html">Wardens</a></td></tr>
<tr><td>Weavers</td><td>Dream Loom, Resonance Mask</td><td>Pull/send through Somnus; anchor identity</td><td>Loom dreams idle; Mask is a library of dives</td><td><a href="the-weavers.html">Weavers</a></td></tr>
<tr><td>R.D.</td><td>Lament Well, cells, rigs, gauges</td><td>Contain, extract, measure</td><td>Extraction Resonance on top of the kit</td><td><a href="the-reverie-directorate.html">R.D.</a></td></tr>
<tr><td>Judexhan</td><td>Judgment Blade, forehead implant</td><td>Cut Han-defense; count absorbed sorrow until retirement</td><td>The implant is a countdown</td><td><a href="the-judexhan.html">Judexhan</a></td></tr>
<tr><td>Giltong</td><td>Taboo Scanner, Containment Bonds, Arbiter’s Blade, Taboo Archive</td><td>Read violation signatures; shut down Resonances</td><td>Scanner is the city’s immune read</td><td><a href="the-giltong-enforcers.html">Giltong</a></td></tr>
<tr><td>Menders</td><td>Kit, Repair Rod</td><td>Field repair paid in the Mender’s own sorrow</td><td>Rod maps every crack it has sealed</td><td><a href="the-menders.html">Menders</a></td></tr>
</tbody></table></div>
</section>
<section class="wiki-section" id="fray"><h2 class="section-title">Fray and underground</h2>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>Group</th><th>Tool</th><th>What it does</th></tr></thead>
<tbody>
<tr><td>Harvesters</td><td>Harvest Hook (수확 갈고리)</td><td>Forced extraction into the sorrow-layer. Crime tool, not an R.D. extract.</td></tr>
<tr><td>Debt Brokers</td><td>Debt-Transfer Pad</td><td>Buy, sell, forge obligation — including inherited debt.</td></tr>
<tr><td>Veil Merchants</td><td>Fake Veil-Stone</td><td>Counterfeit Veil access at ~10% of the tax.</td></tr>
<tr><td>Memory Washers</td><td>Wash-Rig</td><td>Chair that pulls memories as Echoes and leaves blank spots. Rigs whisper.</td></tr>
<tr><td>Entity Traders</td><td>Containment Cube</td><td>Portable cell for stolen Sorrow Entities.</td></tr>
<tr><td>Whisper Market</td><td>Whisper Pipe</td><td>Information brokerage — not a civic Whisper-Thread.</td></tr>
<tr><td>Debtless</td><td>Debt-Breaker</td><td>Liberation kit aimed at Collector ledgers.</td></tr>
<tr><td>Veil Breakers</td><td>Veil-Cracker</td><td>Activist tool against Veil generators.</td></tr>
<tr><td>Memory Thieves</td><td>Memory-Siphon</td><td>Black-market cousin of the Lens. Keepers hunt them.</td></tr>
<tr><td>Gate Runners</td><td>Gate-Key</td><td>Exile assistance through the Gate. ~500 Echoes a head in the Fray table.</td></tr>
</tbody></table></div>
<p>UCD raids them. A Harvest Hook is not an Extraction Glove. A wash-rig is not a Memory Lens. Do not mix them on a loadout screen. Long crime geography lives on <a href="the-underworld-and-wound-walkers.html">underworld</a> and <a href="the-memory-washers.html">Washers</a>.</p>
</section>
<section class="wiki-section" id="rule"><h2 class="section-title">Rule</h2>
<p>Handheld kit ≠ Resonance ≠ M.A.W. The Ledger is kit; the Scales is the Collector’s body. The Baton is kit; the Barrier is the Warden’s field. The extraction rig is kit; Extraction is the R.D. note. Faction Resonances are in <code>SOMNARAK_TABOO_RESONANCE.md</code> §II and on the Resonances article. Taboos are laws, not tools. Default R.D. issue (Sorrow Rod, Veil Vest, Echo Compass, Sorrow Gauge, Memory Anchor, Fracture Whistle) is personnel kit on the Directorate page, not this index.</p>
</section>
"""
    put(
        "factions/faction-technology.html",
        "Faction Technology",
        "Index of guild tools, Fray kits, and the rule: kit ≠ Resonance ≠ M.A.W. Long descriptions live on each faction page.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Factions</a> <i>/</i> <span>Faction Technology</span>',
        "Faction Technology",
        "FACTIONS · INSTRUMENTS",
        [
            ("overview", "Overview"),
            ("guilds", "Guild instruments"),
            ("fray", "Fray and underground"),
            ("rule", "Rule"),
        ],
        body,
        '<a href="index.html">Factions</a> | <a href="../mechanics/taboo-resonance-mechanics.html">Resonances</a> | <a href="../maw/index.html">M.A.W.</a>',
        "Faction technology Debt-Ledger Dream Loom Judgment Blade Taboo Scanner Repair Rod Wash-Rig Harvest Hook",
    )


def assignment():
    body = r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p><strong>Agent assignment</strong> is facility-wide, not a Floor 1 protocol. The old Neutral Command article pasted the whole personnel-placement chapter under Majin’s floor. LC analog: employees are listed on a personnel page, not only on Control Team. This URL is that split.</p>
<p><em>“The right person in the right room can contain a monster. The wrong person in the wrong room becomes one.”</em></p>
<p>Every R.D. body is scored on four attributes. Civilians average 20–30. Trained personnel 40–60. Echo-Cores exceed 80. Fragile 1–20, Average 21–40, Trained 41–60, Veteran 61–80, Exceptional 81–100.</p>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>Attribute</th><th>Color</th><th>Measures</th><th>Trains by</th></tr></thead>
<tbody>
<tr><td>Resilience</td><td>Deep Blue</td><td>Physical endurance — Han-weight before breaking. HP, heavy M.A.W., long shifts.</td><td>Labor, controlled Han exposure, bearing kit.</td></tr>
<tr><td>Clarity</td><td>Pale White</td><td>Mental stability — resist manipulation, memory theft, Dream bleed. SP.</td><td>Meditation, brief Dream dips, memory exercises.</td></tr>
<tr><td>Composure</td><td>Crimson</td><td>Emotional control — work speed, Flerehan without collapse, M.A.W. bond stability.</td><td>Feel without drowning; confrontation drills.</td></tr>
<tr><td>Resolve</td><td>Black</td><td>Willpower — act despite weight. Ferrehan, leadership, movement under Tide.</td><td>Purpose, endurance tests, moral choices.</td></tr>
</tbody></table></div>
<p>Work Type pairing: Flerehan wants Composure/Clarity. Pugnahan wants Resolve/Resilience. Viderehan wants Clarity/Composure. Ferrehan wants Resilience/Resolve. Full stat math stays with the Directorate handbook; this page is who goes where.</p>
</section>
<section class="wiki-section" id="process"><h2 class="section-title">Process</h2>
<p>Step 1 — Attribute assessment on all four. Step 2 — Floor assignment; transfers exist and need approval. Step 3 — Room assignment inside the floor; rotate to prevent burnout and exposure. Step 4 — Entity assignment for Work Types, by resonance compatibility.</p>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>Floor</th><th>Primary</th><th>Secondary</th><th>Why</th></tr></thead>
<tbody>
<tr><td>1 Neutral Command</td><td>Composure</td><td>Clarity</td><td>Administration under silence.</td></tr>
<tr><td>2 Maw’s Keep</td><td>Resilience</td><td>Resolve</td><td>Containment endurance.</td></tr>
<tr><td>3 Extraction Hall</td><td>Composure</td><td>Clarity</td><td>Finish an extract without keeping the donor’s habit.</td></tr>
<tr><td>4 Insight Forge</td><td>Clarity</td><td>Composure</td><td>Observe without becoming the paper.</td></tr>
<tr><td>5 Border Watch</td><td>Resolve</td><td>Resilience</td><td>Weight at the wall.</td></tr>
<tr><td>6 Deep Vault</td><td>Clarity</td><td>Resolve</td><td>Archives want clear thinking and moral strength.</td></tr>
<tr><td>7 Shadow Corps</td><td>Composure</td><td>Resolve</td><td>Infiltration: control plus determination.</td></tr>
<tr><td>8 Gate Watch</td><td>Resolve</td><td>Clarity</td><td>Hear a voice from outside and not open the door.</td></tr>
</tbody></table></div>
<p>Neutral Command signs. Insight Forge observes. A refused transfer is still an assignment. You do not live on Border Watch or Extraction until you Fracture; rotation exists because the alternative is a Core.</p>
</section>
<section class="wiki-section" id="entity"><h2 class="section-title">Entity assignment</h2>
<p>Resonance scan in the Extraction Hall. Attribute match against the entity’s requirements. Work Type preference against the entity’s response. Experience gates higher-risk cells.</p>
<p>Rules: no one works the same entity more than seven consecutive days. Mandatory three-day break between entity assignments. Maximum three Work Type interactions per entity per day. If the Sorrow Gauge exceeds 75%, the assignment is suspended.</p>
<p>Rotation: daily 8-hour room shifts; weekly entity rotation; monthly floor moves with approval; quarterly full reassessment. Inside a floor, room assignment also follows Han element and the agent’s worst stat — do not put a Fragile-Clarity clerk on a Void subject and call it training.</p>
</section>
<section class="wiki-section" id="cores"><h2 class="section-title">Cores are not assigned</h2>
<p>Echo-Cores are the floor until suppression or exile. Agents rotate. A Core Suppression is a floor event, not a transfer request. Panic is what happens when assignment was wrong; Fracture is further down that road. See <a href="../mechanics/panic-states-and-corrosion.html">Panic</a>, <a href="facility-upgrades.html">upgrades</a>, <a href="../factions/the-reverie-directorate.html">Directorate</a>.</p>
</section>
"""
    put(
        "departments/agent-assignment.html",
        "Agent Assignment",
        "Facility-wide personnel placement by Resilience, Clarity, Composure, Resolve — floors, entity rules, rotation. Not a Floor 1 dump.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Departments</a> <i>/</i> <span>Agent Assignment</span>',
        "Agent Assignment",
        "FACILITY · PERSONNEL",
        [
            ("overview", "Overview"),
            ("process", "Process"),
            ("entity", "Entity assignment"),
            ("cores", "Cores are not assigned"),
        ],
        body,
        '<a href="index.html">Departments</a> | <a href="floor-1-neutral-command.html">Floor 1</a> | <a href="../factions/the-reverie-directorate.html">R.D.</a>',
        "Agent Assignment Resilience Clarity Composure Resolve floors Echo-Cores rotation",
    )


def upgrades():
    body = r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p><strong>Facility upgrades</strong> are how the Hand of Change grows across cycles — cells, gauges, corridors, Mnemonic Generator load. Not Floor 1’s private construction budget. Architects build it. Extraction pays in Han-flux. Neutral Command approves it. The old wiki dumped the growth chapter onto Majin’s floor because that is where the signature sits.</p>
<p><em>“The Hand of Change is not static. It grows. It adapts. It improves — because we improve it.”</em></p>
</section>
<section class="wiki-section" id="kinds"><h2 class="section-title">Categories</h2>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>Category</th><th>What it is</th><th>Source</th></tr></thead>
<tbody>
<tr><td>Containment</td><td>Stronger cells, better suppression</td><td>Floor 4 research + Floor 2 feedback</td></tr>
<tr><td>Extraction</td><td>Higher M.A.W. yield, lower risk</td><td>Floor 3 + Floor 4</td></tr>
<tr><td>Research</td><td>Better tools, faster knowledge</td><td>Floor 4 innovation</td></tr>
<tr><td>Defense</td><td>Weapons, barriers, Zone E resistance</td><td>Floor 5 + Floor 4 design</td></tr>
<tr><td>Archive</td><td>Capacity, preservation</td><td>Floor 6</td></tr>
<tr><td>Intelligence</td><td>Sensors, Shadow network</td><td>Floor 7</td></tr>
<tr><td>Facility / welfare</td><td>Walls, conduits, SP recovery rooms</td><td>Maintenance + Architects</td></tr>
</tbody></table></div>
<p>Each upgrade has a Han-Energy cost and a downtime. You do not upgrade Border Watch during a Tide Watch. Secret passages the Architects already built into Facility 01 are not an “upgrade” on this ledger — they are a debt the Directorate has not paid. Welfare rooms do not erase Panic; they buy a shift. Expansion that crosses a Han-flow line without a Sorrow Compass reading is how Floor 5 inherits a new aperture.</p>
</section>
<section class="wiki-section" id="process"><h2 class="section-title">Process and examples</h2>
<p>Need identified (event, failure, or research) → Floor 4 researches → Architects design → Echo-Core approves → Maintenance and Technicians build → controlled test → deployment.</p>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>Upgrade</th><th>Floor</th><th>Effect</th><th>Cost</th></tr></thead>
<tbody>
<tr><td>Reinforced containment cells</td><td>2</td><td>+20% suppression</td><td>500 Han-Energy + Architect time</td></tr>
<tr><td>Enhanced extraction rigs</td><td>3</td><td>+15% M.A.W. yield</td><td>300 + research</td></tr>
<tr><td>Extended Echo Compass</td><td>4</td><td>+50 m detection</td><td>100 + materials</td></tr>
<tr><td>Border barrier enhancement</td><td>5</td><td>+30% Outside Sorrow resistance</td><td>200 + Wardens</td></tr>
<tr><td>Deep Vault expansion</td><td>6</td><td>+1000 storage</td><td>150 + construction</td></tr>
<tr><td>Shadow network expansion</td><td>7</td><td>+10 informants</td><td>Intelligence + Echoes</td></tr>
<tr><td>Han-conduit reinforcement</td><td>All</td><td>−50% leak chance</td><td>400 + maintenance</td></tr>
</tbody></table></div>
<p>Facility Level tracks total capability: 1 Basic (start), 2 Reinforced (5 upgrades, +10% efficiency), 3 Advanced (15, +20%, new research), 4 Fortified (30, +30%, new containment types), 5 Sovereign (50, +40%, maximum). Architects are the only Head that wants the building to change. The Council resists because uncertainty makes Han. That fight is civic. This page is which valve, which cell, which cycle.</p>
</section>
<section class="wiki-section" id="freeze"><h2 class="section-title">When it freezes</h2>
<p>Facility Meltdown: no new cells, no new valves, no Architect crews in the corridors. Rebuild is a later cycle. Tide Watch is the same freeze, for a different alarm color. A completed upgrade that nobody staffs is just a new room for an Ordeal to spawn in. Sign the assignment first, or do not pour the Han. See <a href="agent-assignment.html">assignment</a>, <a href="facility-meltdown-procedures.html">meltdown</a>, <a href="../factions/the-architects.html">Architects</a>.</p>
</section>
"""
    put(
        "departments/facility-upgrades.html",
        "Facility Upgrades",
        "Hand of Change growth — categories, process, example costs, Facility Level 1–5, freeze during Meltdown and Tide Watch.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Departments</a> <i>/</i> <span>Facility Upgrades</span>',
        "Facility Upgrades",
        "FACILITY · GROWTH",
        [
            ("overview", "Overview"),
            ("kinds", "Categories"),
            ("process", "Process and examples"),
            ("freeze", "When it freezes"),
        ],
        body,
        '<a href="index.html">Departments</a> | <a href="../factions/the-architects.html">Architects</a> | <a href="floor-1-neutral-command.html">Floor 1</a>',
        "Facility upgrades Hand of Change cells gauges Architects Meltdown Facility Level",
    )


def research():
    body = r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The R.D. <strong>research / observation</strong> ladder is how a Sorrow Entity goes from a code on a door to a profile you can work. Not Floor 4’s private manual. Insight Forge (Ayshuk) files it. Every floor uses it. The old wiki pasted “Research System” under Floor 4 because that is the lab. LC analog: Abnormality observation lives on the Abnormality and on Info Team, not only on one department dump.</p>
<p><em>“You cannot contain what you do not understand. You cannot understand what you have not observed.”</em> Knowledge is not given. It is earned through direct observation and interaction.</p>
</section>
<section class="wiki-section" id="levels"><h2 class="section-title">Observation levels</h2>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>Level</th><th>Name</th><th>What unlocks</th><th>How</th></tr></thead>
<tbody>
<tr><td>0</td><td>Unknown</td><td>Basic SECC (coherence, potency, origin)</td><td>Contained</td></tr>
<tr><td>1</td><td>Observed</td><td>Element, manifestation, basic behavior</td><td>1 successful Work Type</td></tr>
<tr><td>2</td><td>Studied</td><td>Patterns, Work preferences, Gauge triggers</td><td>5 successful works</td></tr>
<tr><td>3</td><td>Understood</td><td>Origin, core, M.A.W. potential, breach</td><td>15 works + 1 survived breach</td></tr>
<tr><td>4</td><td>Mastered</td><td>Full profile, optimal cell, all extracts, hidden properties</td><td>30 works + 3 breaches + entity-specific condition</td></tr>
</tbody></table></div>
<p>M.A.W. extraction is a separate risk event, not a level-up reward. SE-003 never leaves Level 5 border monitoring and still has <strong>no extractable M.A.W.</strong> Unregistered 004 / 006 / 008 have no observation ladder because they have no source card. Level 3 is where origin stories get written down; that is also where Keepers start asking for a copy and Collectors start asking for a price. Refuse both until Floor 4 signs.</p>
<p>Observation Level is not Hope Intensity and not Coherence. Mixing those three on a clipboard is how a TETH-shaped job gets an ALEPH-shaped funeral — and those LC words do not belong on the clipboard either.</p>
</section>
<section class="wiki-section" id="op"><h2 class="section-title">How observation works</h2>
<p>Contain on Floor 2, initial SECC, Level 0. Work Types generate <strong>Observation Points (OP)</strong>. Failed work generates fewer OP and may cause incidents. At thresholds, Research Projects unlock. Mastery is Level 4: all M.A.W. types, optimized containment, hidden properties.</p>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>Work Type</th><th>Success</th><th>Failure</th><th>Critical</th></tr></thead>
<tbody>
<tr><td>Flerehan</td><td>+2 OP</td><td>+0</td><td>+5</td></tr>
<tr><td>Pugnahan</td><td>+2 OP</td><td>+0</td><td>+5</td></tr>
<tr><td>Viderehan</td><td>+3 OP</td><td>+1</td><td>+6</td></tr>
<tr><td>Ferrehan</td><td>+1 OP</td><td>+0</td><td>+4</td></tr>
</tbody></table></div>
<p>OP gates: 0→1 needs 5; 1→2 needs 20 (25 cumulative); 2→3 needs 50 (75); 3→4 needs 100 (175). Viderehan is the fastest path. Projects at Level 1 include Basic Classification and Behavioral Study; Level 2 Origin Investigation, Sorrow Gauge Analysis, M.A.W. Potential; Level 3 Emotional Core, Containment Optimization, Hidden Properties; Level 4 Full Mastery after every previous project.</p>
</section>
<section class="wiki-section" id="people"><h2 class="section-title">Personnel, ledger, risk</h2>
<p>Floor 4 is the lab. Specialists: Entity Analyst, Han Researcher, Sorrow Cartographer, M.A.W. Specialist. Agents generate OP through daily work. Senior Agents lead projects. Every entity has a Research Ledger: SECC, Observation Level, OP, projects, unlocked knowledge, extraction history, personnel notes. Ayshuk reviews ledgers without bias because they cannot feel sorrow. <em>“I cannot feel what the entities feel. But I can see what they are. That is enough.”</em></p>
<p>Risks: resonance overload, false understanding, entity deception, Fracture, breach. Caps: maximum three Work Type interactions per entity per day; mandatory breaks; attribute monitoring; Sorrow Gauge pause; emergency containment on standby for high-risk work. See <a href="floor-4-insight-forge.html">Floor 4</a>, <a href="../mechanics/secc-classification-system.html">SECC</a>, <a href="../mechanics/the-four-work-types.html">Work Types</a>, <a href="../maw/maw-crafting-and-extraction.html">Extraction</a>.</p>
</section>
"""
    put(
        "departments/research-observation.html",
        "Research and Observation",
        "R.D. observation levels 0–4, Observation Points, research projects, ledger, risks. Facility-wide, not a Floor 4 dump.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Departments</a> <i>/</i> <span>Research and Observation</span>',
        "Research and Observation",
        "FACILITY · INSIGHT",
        [
            ("overview", "Overview"),
            ("levels", "Observation levels"),
            ("op", "How observation works"),
            ("people", "Personnel and risk"),
        ],
        body,
        '<a href="floor-4-insight-forge.html">Floor 4</a> | <a href="../mechanics/secc-classification-system.html">SECC</a> | <a href="../mechanics/the-four-work-types.html">Work Types</a>',
        "Observation Level research Insight Forge Work Types SECC OP Ayshuk",
    )


def missions():
    body = r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>LC analog: the <em>Missions</em> catalog lists every department’s jobs; each team page also lists its own. This URL is the catalog. Floor pages keep their daily-mission tables — those are not facility-wide dumps. They are that floor’s work.</p>
<p><em>“Every day, the same work. Every day, different sorrow.”</em> Quotas in Han-Energy are operational targets, not civic tax. Floor 6 and 7 file none — Deep Vault and Shadow Corps do not mint energy; they keep secrets and listen. Floor 2’s 500 is the heavy cell-work number. Floor 5’s 50 is the border’s thin yield. Do not confuse a daily quota with an Ordeal Watch or a Core Suppression.</p>
</section>
<section class="wiki-section" id="catalog"><h2 class="section-title">By floor</h2>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>Floor</th><th>Lead</th><th>What the day is</th><th>Quota</th></tr></thead>
<tbody>
<tr><td><a href="floor-1-neutral-command.html">1 Neutral Command</a></td><td>Majin</td><td>Command, alarms, assignment signatures — no mission table (HR on <a href="agent-assignment.html">assignment</a>)</td><td>—</td></tr>
<tr><td><a href="floor-2-maws-keep.html">2 Maw’s Keep</a></td><td>Dekan</td><td>Work Types, gauges, breach return, new-entity processing, cell repair, Maw perimeter</td><td>500</td></tr>
<tr><td><a href="floor-3-extraction-hall.html">3 Extraction Hall</a></td><td>Zyrak</td><td>Extract, resonance scan, test, bond, issue, refine</td><td>300</td></tr>
<tr><td><a href="floor-4-insight-forge.html">4 Insight Forge</a></td><td>Ayshuk</td><td>Observe, classify, map Han, document — ladder on <a href="research-observation.html">observation</a></td><td>100</td></tr>
<tr><td><a href="floor-5-border-watch.html">5 Border Watch</a></td><td>Mellda</td><td>Patrol, Desolate recon, watchtowers, Tide telemetry</td><td>50</td></tr>
<tr><td><a href="floor-6-deep-vault.html">6 Deep Vault</a></td><td>Marjuk</td><td>Archive, Echo stabilize, Cheongula vault — no energy quota</td><td>None</td></tr>
<tr><td><a href="floor-7-shadow-corps.html">7 Shadow Corps</a></td><td>Ishall</td><td>Intel, infiltration, informants, counter-intel — no energy quota</td><td>None</td></tr>
<tr><td><a href="floor-8-gate-watch.html">8 Gate Watch</a></td><td>Xyan</td><td>Watch the Gate, outside contact, record without controlling return</td><td>—</td></tr>
</tbody></table></div>
<p>Full per-floor rows (who, frequency, which room) stay on those floor pages. Do not strip them. This catalog is the extra index so a search for “missions” does not land on Floor 2 only.</p>
</section>
<section class="wiki-section" id="cross"><h2 class="section-title">Cross-field and failure</h2>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>Mission</th><th>Floors</th><th>What it is</th></tr></thead>
<tbody>
<tr><td>Entity transfer</td><td>2 + 4</td><td>Move a subject from cell to research</td></tr>
<tr><td>M.A.W. emergency</td><td>3 + 5</td><td>Extract from something captured in the field</td></tr>
<tr><td>Breach response</td><td>All</td><td>Facility-wide return-to-cell</td></tr>
<tr><td>Ordeal response</td><td>All</td><td>Color × Time suppression</td></tr>
<tr><td>Expedition</td><td>5 + 7</td><td>Joint Desolate recon + intelligence</td></tr>
<tr><td>Archive investigation</td><td>4 + 6</td><td>Research request that needs a vault key</td></tr>
</tbody></table></div>
<p>Failure: containment failure is a breach. Extraction failure damages M.A.W. and agitates the donor. Research failure is misinformation, wasted flux, possible Fracture. Border failure is Zone E. Intelligence failure is a surprise. Archive failure is a lost record. Personnel: minor → reassignment and training; major → attribute drop, demotion; critical → Fracture risk, removal; catastrophic → death, Fracture, or exile.</p>
</section>
<section class="wiki-section" id="not"><h2 class="section-title">Not missions</h2>
<p>Ordeals (five colors × four watches) are not a daily mission. Core Suppression is not a daily mission. Facility Meltdown is not a daily mission. UCD raids and SED expeditions are city operations, not floor quotas. A “new entity processing” line on Floor 2 is still Floor 2’s job, even when the specimen walked in from Zone E. See <a href="../mechanics/ordeals-framework.html">Ordeals</a>, <a href="facility-meltdown-procedures.html">meltdown</a>, <a href="core-suppression-guidelines.html">Core suppression</a>.</p>
</section>
"""
    put(
        "departments/daily-missions.html",
        "Daily Missions",
        "Catalog of each floor’s daily work and Han-Energy quotas, cross-field jobs, failure. Per-floor tables stay on the floor pages.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Departments</a> <i>/</i> <span>Daily Missions</span>',
        "Daily Missions",
        "FACILITY · MISSIONS CATALOG",
        [
            ("overview", "Overview"),
            ("catalog", "By floor"),
            ("cross", "Cross-field and failure"),
            ("not", "Not missions"),
        ],
        body,
        '<a href="index.html">Departments</a> | <a href="agent-assignment.html">Assignment</a> | <a href="floor-2-maws-keep.html">Floor 2</a>',
        "Daily missions floors quota Han-Energy Maw Keep Border Watch Gate cross-field",
    )


def four_watches():
    body = r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p><strong>The Four Watches</strong> are the time axis of Ordeals. Color is the Han type (Blue Lament, Black Weight, Pale Void, Grey Grudge, Purple raw Han). Time is severity. This page is Dawn / Noon / Dusk / Midnight in LC terms — First, Second, Third, and Tide Watch. It is <em>not</em> Whisper / Surge / Breach / Abyss. That four-name overlay mixed city atmosphere with Ordeals and is retired.</p>
<p>One Ordeal per Time per day. Times escalate. Color articles list the named manifestations:
<a href="ordeal-blue.html">Blue — Mourning Host</a> ·
<a href="ordeal-black.html">Black — Crushing Tide</a> ·
<a href="ordeal-pale.html">Pale — The Fading</a> ·
<a href="ordeal-grey.html">Grey — Resentful March</a> ·
<a href="ordeal-purple.html">Purple — The Corruption</a>.
Hub: <a href="ordeals-framework.html">Ordeals framework</a>.</p>
</section>
<section class="wiki-section" id="times"><h2 class="section-title">The four times</h2>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>Time</th><th>Severity</th><th>When</th><th>Trigger</th></tr></thead>
<tbody>
<tr><td>First Watch</td><td>Minor</td><td>Early Management, low accumulation</td><td>After 2–3 work cycles</td></tr>
<tr><td>Second Watch</td><td>Moderate</td><td>Mid-Management, Han building</td><td>After 5–6 work cycles</td></tr>
<tr><td>Third Watch</td><td>Major</td><td>Late Management, approaching Tide</td><td>After 8+ cycles or near-Tide</td></tr>
<tr><td>Tide Watch</td><td>Catastrophic</td><td>Sorrow Tide peak; facility-wide</td><td>Tide or major breach cascade</td></tr>
</tbody></table></div>
<p><strong>First Watch:</strong> five to ten weak bodies. Level 2 team. A warning that free Han is accumulating. Named examples: Blue Weeping Cluster, Black Rolling Weight, Pale The Forgotten, Grey Resentful Three, Purple The Seeping. They last about a minute if ignored, then move or fade — but they leave residue (cracked floors, missing memories, Fracture-like film). Also filed: Blue Leaking Eyes / Salt Puddles; Black Grinding Slab / Lead Footsteps; Pale Blanking / Pale Tracks; Grey Brawler / Spiteful Few; Purple Ooze / Spore Patches.</p>
<p><strong>Second Watch:</strong> ten to twenty bodies, or fewer stronger ones. Level 3+ with M.A.W. Corridors stop being a swarm of larvae and start being a fight. Grey forms battalions. Purple roots into the Han-flow. Pale starts erasing ranks, not single names. Named: Blue Brine Rain / Sobbing Wall / Wailing Choir; Black Crushing Column / Falling Mass / Sinking Floor; Pale Bleeding White / Erased Ranks / Faceless Legion; Grey Blade Wall / Grey Battalion / Rust Battalion; Purple Bloom / Rooted / Spore Field.</p>
<p><strong>Third Watch:</strong> a single large entity or a coordinated horde. Level 4+, specialized M.A.W., Containment Lead oversight. If Third Watch is not handled it does not politely become Tide Watch later — it <em>is</em> the on-ramp. Dekan’s manual treats an unsuppressed Third as a floor-loss risk, not a delay. Named: Blue Brine Walkers / Drowned Procession / Hollow Bells; Black Buried Pillar / Collapsing Arch / Pressing Vault; Pale Featureless / Pale Hush / Whiteout; Grey Forge March / Iron March / War Machine; Purple Bloom Hosts / Mycelium / Parasite.</p>
<p><strong>Tide Watch:</strong> facility-wide. Echo-Cores and their top teams. An unsuppressed Tide Watch before dawn can permanently damage the Hand of Change. Ordeals are mortal; they do not return from the Weeping. Tide Watch is the only suppression that can drop facility Han-density enough to matter city-wide — which is why Majin vetoed “deliberately spawn Tide Watches to bleed the city” three times. Named: Blue Drowned World / Mother Flood / Ocean of Tears; Black Final Ton / The Mountain / Sinking Continent; Pale Final Blank / The Nothing / The Unmade; Grey Arbiter / Gallows Field / The Judge; Purple Bloom-Wave / Fracture Wave / Garden of Rot. Facility upgrades freeze during Tide Watch the same way they freeze during Meltdown — different alarm, same “no Architect crews in the corridor.”</p>
</section>
<section class="wiki-section" id="gauge"><h2 class="section-title">Han-density and warning</h2>
<p>Every work cycle leaks residual Han into the facility atmosphere. The Han-Density Gauge tracks free (uncontained) energy. Clear 0–20% (no Ordeal risk). Elevated 21–40% (First Watch possible). Critical 41–60% (Second). Overload 61–80% (Third). Cascading 81–100% (Tide imminent).</p>
<p>Warning goes out on the Whisper-Thread 30–60 seconds before spawn: Color, Time, estimated floor/corridor/sector, recommended team. Ordeals are hostile to everything, including breached Sorrow Entities. Same-color Ordeals do not attack each other; different colors will fight. PURPLE can parasitically bond with a Sorrow Entity and temporarily empower it. Suppression yields residual Han-Energy (First Watch ~5% of daily quota; Tide Watch ~25%), lowers the gauge, and yields <strong>no M.A.W.</strong> — Ordeals dissolve on death.</p>
</section>
<section class="wiki-section" id="retired"><h2 class="section-title">Retired overlay</h2>
<p>Older wiki text named four events Whisper, Surge, Breach, and Abyss and mapped them to morning / midday / evening / night. That list does not match <code>SOMNARAK_ORDEALS_FRAMEWORK.md</code>. The canon grid is <strong>five colors × four watches</strong>.</p>
</section>
"""
    put(
        "mechanics/the-four-ordeals.html",
        "The Four Watches",
        "First, Second, Third, and Tide Watch — Ordeal time axis, Han-density gauge, named manifestations. Not Whisper/Surge/Breach/Abyss.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Mechanics</a> <i>/</i> <span>The Four Watches</span>',
        "The Four Watches",
        "ORDEALS · TIME AXIS",
        [
            ("overview", "Overview"),
            ("times", "The four times"),
            ("gauge", "Han-density"),
            ("retired", "Retired overlay"),
        ],
        body,
        '<a href="ordeals-framework.html">Ordeals</a> | <a href="ordeal-blue.html">Blue</a> | <a href="index.html">Mechanics</a>',
        "Four Watches First Watch Tide Watch Ordeals Blue Black Pale Grey Purple Han-Density",
    )


def locations():
    put(
        "locations/the-orphan-bell-tower.html",
        "The Orphan Bell Tower",
        "Place of SE-001 The Orphaned Bell — Zone B Old Lament grief architecture, Lament’s Requiem, not a Worldbuilding Framework stub.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Atlas</a> <i>/</i> <span>Orphan Bell Tower</span>',
        "The Orphan Bell Tower",
        "ATLAS · ZONE B · SE-001",
        [("overview", "Overview"), ("place", "Old Lament"), ("sound", "What the tower does")],
        r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The <strong>Orphan Bell Tower</strong> is the place-name attached to <a href="../entities/se-001-the-orphaned-bell.html">SE-001 The Orphaned Bell</a>. It is not a Worldbuilding Framework dump, and it is not “Sector 7” in an LC facility sense. The bell’s tale line is: <em>“The bell tolls for children who will never grow old.”</em></p>
<p>SE-001 is a contained City Sorrow. The tower is the architecture that grew around that grief — a vertical room that still thinks it is calling children home. Directorate observation treats the site and the entity as one operational problem: you do not schedule the tower without scheduling the Bell. M.A.W. from this donor is the Lament set — Requiem, Shroud, Edge — not a containment-log satellite. Those fake Instinct/Insight logs were deleted.</p>
</section>
<section class="wiki-section" id="place"><h2 class="section-title">Old Lament</h2>
<p>Zone B carries the city’s oldest sorrows. The Old Lament (옛 탄식 — Yet Tansik) is inner B, closest to A: first homes of solidified grief, walls that replay settlers, buildings that grew faces. Han signature: Lament (deep blue). About 8,000 of the oldest families, people who refuse to leave. Veil/Raw is 10/90 — the Veil cannot suppress sorrow this old. Sub-governor is an Elder Council that does not enforce rules; they <em>remember</em> them. The district is quiet — not peaceful, muted. Sound behaves differently here.</p>
<p>A bell-tower that refuses to stop being a school-yard signal belongs in that grain of the city even when the containment cell is inside Facility 01. The Lament’s secret: buildings do not just absorb sorrow, they replay it. At night the walls whisper the first settlers. Some say you can hear the Cheongula if you listen carefully enough.</p>
<p>Keepers want the sound archived. Collectors have tried to price the hour. Wardens treat an unsanctioned ring as a crowd problem. Weavers say the overtones continue in Somnus after the bronze stops. See <a href="zone-b-west-ward.html">Zone B</a>.</p>
</section>
<section class="wiki-section" id="sound"><h2 class="section-title">What the tower does</h2>
<p>A bell that tolls for the unaged is a Place as much as a Subject. People who grew up in B report knowing the hour by a ring that is not on any civic clock. Work types, breach, and M.A.W. live on the entity article and on <a href="../maw/maw-w-001-01-the-laments-requiem.html">Lament’s Requiem</a>. Combat records do not belong on this URL. This article is the room.</p>
</section>
""",
        '<a href="index.html">Atlas</a> | <a href="../entities/se-001-the-orphaned-bell.html">SE-001</a> | <a href="zone-b-west-ward.html">Zone B</a>',
        "Orphan Bell Tower SE-001 Orphaned Bell Zone B Old Lament Lament Requiem Yet Tansik",
    )
    put(
        "locations/the-hollow-glass.html",
        "The Hollow Glass",
        "Bong’s Zone D tavern — only named neutral ground. The unemptied glass at 8:47. Former Collector.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Atlas</a> <i>/</i> <span>The Hollow Glass</span>',
        "The Hollow Glass",
        "ATLAS · ZONE D · NEUTRAL GROUND",
        [("overview", "Overview"), ("origin", "Bong"), ("glass", "The glass that never empties"), ("use", "Use")],
        r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p><strong>The Hollow Glass</strong> is a tavern in Zone D, not a District 4 memorial and not an empty canonical-record box. It is the only named neutral ground in D: Wardens, Frays, Menders, Collectors, and ordinary citizens drink side by side. Fights do not happen there because Bong will not serve anyone who starts one. His silence is the house rule. His memory is worse — which is to say, complete.</p>
<p>Bong (봉), the Barkeeper (술집 주인). Premature white hair, shaved close at the sides; pale unreadable eyes; compact; ~166 cm; ~25; olive skin; ink-stained fingers always slightly tremulous. He serves everyone. He asks no questions. He hears everything.</p>
</section>
<section class="wiki-section" id="origin"><h2 class="section-title">Bong</h2>
<p>Bong was a Collector — one of the honest ones, and one of the best. Zone C, tracing debts, calculating obligations. He found a phantom debt written by Debt Brokers onto a family that had never borrowed. He reported it. Ignored. Reported again. Threatened. Reported a third time. Fired.</p>
<p>He opened the Glass the next month. A tavern where everyone is welcome, no one asks, no one judges, no one is turned away. Wardens and Frays, Collectors and citizens, rich and poor. That phantom obligation is the Collectors’ Taboo-5-adjacent sin done as Fray work; Bong left rather than keep the ledger. He still remembers every tab. He still does not collect.</p>
</section>
<section class="wiki-section" id="glass"><h2 class="section-title">The glass that never empties</h2>
<p>Third seat from the left is empty. The glass there is always full of the cheapest Han-water, barely worth an Echo. No one sits. No one drinks. No one asks. Everyone knows.</p>
<p>Bong’s wife Fractured behind the bar on a quiet Tuesday. He swept the crystal himself. He never changed the layout. Every evening at 8:47 — the minute of the Fracture — he fills the glass and moves on. He does not speak. He does not pray. People who know leave an Echo beside it, not as payment, as tribute. He collects them at closing and spends them on more Han-water.</p>
<p>His question in the Cast file: <em>“If I serve everyone’s sorrow in a glass, who serves mine?”</em> The tavern is always open. The seat is always empty. Serving is the only thing that keeps him from Fracturing himself. There is no plaque, no Council ribbon, no SECC file.</p>
</section>
<section class="wiki-section" id="use"><h2 class="section-title">Use</h2>
<p>SED and UCD both know the door. Information moves here because nobody is in uniform at the bar — or everyone is, and Bong does not care. Neutral does not mean safe outside the threshold. Zone D is forge and gardens, Furnace refugees, Mender traffic, Mask Market one street over. See <a href="zone-d-forge-and-gardens.html">Zone D</a>, <a href="../factions/the-underworld-and-wound-walkers.html">the underworld</a>, <a href="../factions/the-wardens.html">Wardens</a>, <a href="../factions/the-collectors.html">Collectors</a>.</p>
</section>
""",
        '<a href="index.html">Atlas</a> | <a href="zone-d-forge-and-gardens.html">Zone D</a> | <a href="../factions/the-underworld-and-wound-walkers.html">Underworld</a>',
        "Hollow Glass Bong Zone D tavern neutral ground 8:47 Debt Brokers Han-water",
    )
    put(
        "locations/the-library-of-stolen-pasts.html",
        "The Library of Stolen Pasts",
        "SECTOR-B-02 containment geography of SE-009 The Memory Weaver. Not the Grand Archive.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Atlas</a> <i>/</i> <span>Library of Stolen Pasts</span>',
        "The Library of Stolen Pasts",
        "ATLAS · ZONE B · SE-009",
        [("overview", "Overview"), ("not-archive", "Not the Grand Archive"), ("work", "Working the stacks")],
        r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The <strong>Library of Stolen Pasts</strong> is the location line on <a href="../entities/se-009-the-memory-weaver.html">SE-009 The Memory Weaver</a>: SECTOR-B-02, Zone B — library of stolen pasts; contained. It is not the Grand Archive. Keepers preserve. This room keeps what was taken.</p>
<p>SE-009 weaves memories into webs. Tale line: <em>“Threads of the unremembered. They move on their own.”</em> SECC: <code>C-IVγ-009 [VS]</code> — Subject, Entity (IV), Major (γ), City Sorrow, Void, Subject-Dream. Location line is this room: SECTOR-B-02, Zone B, contained. R.D. Observation Level 3 — Advanced. Primary pressure is identity / memory, not masonry.</p>
<p>The entity’s body is woven from crystallized memories rather than flesh — translucent, flickering with stolen faces and voices. Eight legs of braided memory-thread. Many eyes are Han-crystal sockets in which thousands of tiny recollections turn. It is cold, dry, almost weightless, and drips a thin numb damp wherever a memory dissolves. That drip is how the library smells. The stacks are not wood. They are the same thread, frozen into shelves. People get lost in them for hours they cannot later name.</p>
<p>The entity is mobile — it crawls. The room is still a Place. You can schedule the cell and still lose an afternoon to a corridor that was not on the stack map this morning.</p>
</section>
<section class="wiki-section" id="not-archive"><h2 class="section-title">Not the Grand Archive</h2>
<p>Building 2, Zone A, is the Keepers’ Grand Archive: history, Whispering Index, vaults into Dream-space. The Library of Stolen Pasts is a Zone B containment geography. Memory Fray / Washers steal from the Archive and sell. SE-009 is what happens when stolen recollection coagulates into a weaver instead of a ledger. The guild Weavers (직공) are living people with looms in the Spire; do not file this room under them.</p>
<p>M.A.W. from this entity is the Forgotten set — <a href="../maw/maw-w-009-01-the-forgotten-lens.html">Forgotten Lens</a>, Veil, Mask — not the misfiled “Memory Blade” on the SE-003 slot. See <a href="../factions/the-memory-washers.html">Memory Washers</a> and <a href="zone-b-west-ward.html">Zone B</a>.</p>
</section>
<section class="wiki-section" id="work"><h2 class="section-title">Working the stacks</h2>
<p>Valid work against a memory-pressure Subject is not “read quietly.” Insight and related types on the entity page apply. Failed work or ignored activation (Sorrow Gauge climbing) is a breach of identity, not of masonry. Agents report leaving with someone else’s childhood stuck under the tongue.</p>
<p>Observation Level 3 means a Containment Lead signs the stack map before a new agent walks in; Floor 4 Insight Forge can request a memory-trace after, not during. If the room starts filing <em>your</em> name on a spine, leave. That is not a catalog error. That is the Weaver noticing you. Combat, SECC, and M.A.W. stay on the entity and arsenal pages. This article is the room.</p>
</section>
""",
        '<a href="index.html">Atlas</a> | <a href="../entities/se-009-the-memory-weaver.html">SE-009</a> | <a href="zone-b-west-ward.html">Zone B</a>',
        "Library of Stolen Pasts SE-009 Memory Weaver Zone B Forgotten Lens SECTOR-B-02",
    )


def alpha():
    put(
        "lore/the-alpha-tree.html",
        "The Alpha Tree",
        "Cumulation of Consolihan feeling — diamond of six buildings, plaza of polished Han, R.D. in the roots.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Lore</a> <i>/</i> <span>Alpha Tree</span>',
        "The Alpha Tree",
        "LORE · ZONE A · CUMULATION",
        [("overview", "Overview"), ("six", "Six buildings"), ("plaza", "Plaza"), ("roots", "Roots")],
        r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The <strong>Alpha Tree</strong> is not a building someone designed. It is a <strong>cumulation</strong> — the physical gathering of what Somnarak felt during the Consolihan, when flowing Han was frozen into meaning. The tallest pillar of a fortress built from frozen tears. The city grew around it the way crystal grows on crystal.</p>
<p>Metaphor: a great tree from the center. Roots plunge into the Abyss; branches reach toward the Dream. Literal: six massive buildings around a central point inside Zone A’s diamond, extending vertically — deep underground and high into the sky.</p>
<p>The diamond is a square turned on its side — a foundation rotated, destabilized, still holding. Four points: inward, outward, downward (Abyss), upward (Dream). It is <em>perfect</em> while everything around it is jagged asymmetry. The core was designed (or grown as if designed). Everything else grew organically.</p>
</section>
<section class="wiki-section" id="six"><h2 class="section-title">Six buildings</h2>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>#</th><th>Name</th><th>Function</th><th>Position</th><th>Character</th></tr></thead>
<tbody>
<tr><td>1</td><td>Sigh Palace</td><td>Council of Sighs</td><td>North</td><td>Heavy, oppressive, beautiful. Walls that weep. Grief.</td></tr>
<tr><td>2</td><td>Grand Archive</td><td>Memory-bank</td><td>Northeast</td><td>Labyrinthine, whispered. Shelves into Dream-space. Rare happiness as light.</td></tr>
<tr><td>3</td><td>The Crucible</td><td>Raw Han processing</td><td>Southeast</td><td>Loud, hot, dangerous. Weight that anchors. Sadness.</td></tr>
<tr><td>4</td><td>Spire of Dreams</td><td>Dream gateway</td><td>South</td><td>Ethereal glass. Illusions. Reaching toward what could be.</td></tr>
<tr><td>5</td><td>Abyssal Well</td><td>Abyss gateway / containment</td><td>Southwest</td><td>Dark, deep, cold. Chains. Nightmare. Weight of debts.</td></tr>
<tr><td>6</td><td>Architect’s Hall</td><td>Architects work and train</td><td>Northwest</td><td>Practical, marked, alive. Blueprints. Love as the bonds that hold the six together.</td></tr>
</tbody></table></div>
<p>Taboo 1 exists because the Cheongula’s thousand stabilize this Tree. Returned dead would unseat it. See <a href="../locations/zone-a-core-nexus.html">Zone A</a> and <a href="the-first-sovereign-war.html">Consolihan</a>.</p>
</section>
<section class="wiki-section" id="plaza"><h2 class="section-title">Plaza</h2>
<p>The space between the six buildings is the heart. Open to the sky — one of the few places in A where you can see it. Ground is polished Han, smooth, dark, faintly warm. Citizens are not permitted — only faction members and Council summons. The plaza hums. The city’s heartbeat.</p>
</section>
<section class="wiki-section" id="roots"><h2 class="section-title">Roots</h2>
<p>The same Han-crystal continues down as Facility 01 — the Hand of Change. The R.D. is not a seventh building on the plaza; it is built <em>into</em> the Tree. Walls pulse. Floors are warm. The facility responds to emotional events (a Fracture makes the walls tremble), grows when Han accumulates, collapses rooms when sorrow disperses, and remembers. The Director’s Ω-grade M.A.W. fusion is connected; the Director feels every containment failure, every extraction, every Fracture, and the facility feels the Director back.</p>
<p>Marjuk’s Deep Vault is “A (Deep).” Retired Judexhan are taken under the Tree; source does not say what happens next. Dream Veil is thinner here. Keepers’ lowest vaults and the hungry Memory Archive both claim the underside. Do not treat those as one room.</p>
<p>Emotion-to-stone, from the Consolihan file: Grief became the weeping walls of the Sigh Palace. Love became the bonds that hold the six together. Dream became the Spire reaching toward what could be. Nightmare became the Abyssal Well plunging into what must not be. Happiness became the rare light through the Archive’s windows. Sadness became the weight that anchors the Crucible. The Tree is all of that at once. It is not a seventh Head. It is the reason the Heads have somewhere to sit.</p>
<p>Citizens who have never been summoned still feel it. Zone A’s streets slope toward the plaza even when the map says they do not. Han-Rails terminate at the diamond’s edge; you walk the last span. Architects treat the Tree as a living load-bearing member — you do not demolish a root to run a conduit. Collectors have tried to price the hum and been laughed out of the Palace. Weavers say the Spire is not a building that contains Dream; it is Dream that learned to stand up.</p>
</section>
""",
        '<a href="index.html">Lore</a> | <a href="../locations/zone-a-core-nexus.html">Zone A</a> | <a href="../factions/the-high-council.html">Council</a>',
        "Alpha Tree Consolihan Sigh Palace Grand Archive Spire Crucible Abyssal Well Architect Hall",
    )


def patch_search():
    sp = DOCS / "data" / "search.json"
    data = json.loads(sp.read_text(encoding="utf-8"))
    by = {e.get("url"): e for e in data}
    for e in SEARCH:
        if e["url"] in by:
            by[e["url"]].update({k: e[k] for k in ("title", "description", "keywords")})
        else:
            data.append(e)
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("search", len(data))


def main():
    wars()
    three_ops()
    faction_tech()
    assignment()
    upgrades()
    research()
    missions()
    four_watches()
    locations()
    alpha()
    patch_search()
    print("expand D done")


if __name__ == "__main__":
    main()
