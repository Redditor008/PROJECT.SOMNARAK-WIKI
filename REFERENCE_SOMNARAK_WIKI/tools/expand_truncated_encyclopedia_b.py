#!/usr/bin/env python3
"""Expand remaining truncated pages. 100–300+ is a MINIMUM."""
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
<p>Time is counted ~6,000 years from the first Zone B settlement. Cheongula year 202. Occlusihan 202–223. Interim 223–234. Consolihan 234–245. Structuring 245–281. SED ~4200. Directorate 4202. Present Dawn Initiative ~4232–4238.</p>
</section>
<section class="wiki-section" id="occlusihan"><h2 class="section-title">Occlusihan — the First War</h2>
<p>Latin <em>occlusio</em> (to shut) + Han. After the Cheongula, six early factions tried to close the flow entirely, fighting in Zone B and fighting the city itself.</p>
<p><strong>Sealers</strong> built walls and made eruption points. <strong>Severers</strong> suppressed emotion and made Fracture hotspots. <strong>Offerers</strong> fed Han and made it stronger. <strong>Exilers</strong> shoved grief into Dream or Abyss and tore rifts. <strong>Converters</strong> transmuted — partial success, ancestor of Architect practice. <strong>Endurers</strong> accepted hunger — ancestor of Council fatalism. Nobody won. Exhaustion became the Consolihan.</p>
<p>Lesson filed by every later Head: fighting Han directly feeds it; severing it Fractures people; feeding it makes it hungrier. Working with it is the only partial success. RD, SED, and UCD are Year 4,200 operations, not these six.</p>
</section>
<section class="wiki-section" id="consolihan"><h2 class="section-title">Consolihan</h2>
<p>Latin <em>consolidare</em> + Han. Not a war against an army. A war to freeze a tide. After Occlusihan, sorrow pooled into rivers and ate settlements. Survivors combined Converter technique with Endurer philosophy and solidified Han into meaning. Where feeling gathered hardest, the <strong>Alpha Tree</strong> grew — not a building, a cumulation. Sigh Palace weeps. Six buildings hold. Spire of Dreams reaches. Abyssal Well drops. Archive light is rare. Crucible weight anchors.</p>
<p>The city grew around the Tree the way crystal grows on crystal. Taboos were first codified after this war; Giltong exist because Consolihan proved the city needed an immune system, not just walls. See <a href="the-alpha-tree.html">Alpha Tree</a> and <a href="../locations/zone-a-core-nexus.html">Zone A</a>.</p>
</section>
<section class="wiki-section" id="timeline"><h2 class="section-title">Timeline</h2>
<p>~0 first settlement in B around Han pools. ~0–202 Before-Time, Han flowing, structures from necessity. 202 Cheongula at the Maw. 202–223 Occlusihan, 21 years. 223–234 Interim, accumulation catastrophic. 234–245 Consolihan, Tree. 245–281 Structuring: C 245–254, D 254–267, E 267–281. Long Era until SED ~4200, R.D. 4202, present ~4238.</p>
<p>Discard: Old Dreamers, Founding Corporations as precursor Wings, Nine Veiled Edicts as LC seed-of-light copy. Use <a href="../factions/the-founding-corporations.html">the three operations</a> for R.D./SED/UCD.</p>
</section>
"""
    put(
        "lore/the-first-sovereign-war.html",
        "The Wars of Somnarak",
        "Cheongula, Occlusihan, Consolihan — timeline 0–281 and the present age. Not a Sovereign War of Old Dreamers.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Lore</a> <i>/</i> <span>Wars of Somnarak</span>',
        "The Wars of Somnarak",
        "LORE · HISTORY · 202–245",
        [("overview", "Overview"), ("occlusihan", "Occlusihan"), ("consolihan", "Consolihan"), ("timeline", "Timeline")],
        body,
        '<a href="index.html">Lore</a> | <a href="the-alpha-tree.html">Alpha Tree</a> | <a href="../factions/the-high-council.html">Council</a>',
        "Occlusihan Consolihan Cheongula Alpha Tree Wars Sealers Converters Endurers",
    )


def three_ops():
    body = r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>Somnarak does not have “founding precursor corporations” in the Wing/Fixer sense. It has <strong>three operations</strong> in the present age, all after year 4200:</p>
<ul>
<li><a href="the-reverie-directorate.html">Reverie Directorate (R.D.)</a> — contain Sorrow Entities, extract M.A.W., run Facility 01 under the Alpha Tree. Founded 4202. Resonance: Extraction.</li>
<li><a href="the-sed-corps.html">Somnarak Exploration Decreed (SED)</a> — map the unmapped, Corner cities, Desolate edges. Council decree ~4200.</li>
<li><a href="the-ucd-strike-force.html">Underworld Cleanup Descend (UCD)</a> — Fray raids, Wash District, black-market Han. Combat descent, not a Wing.</li>
</ul>
<p>One city, three missions, shared sorrow. The old page pasted the entire game-framework chapter (casts, loops, Hand of Hope ending) onto this URL. That dump is gone. Cast stays on character pages. Absolvohan stays on <a href="../lore/the-cycle-and-absolvohan.html">the Cycle</a>. Hand of Hope stays on <a href="../entities/hope-transformations.html">Hope Transformations</a>.</p>
</section>
<section class="wiki-section" id="connect"><h2 class="section-title">How they connect</h2>
<p>The Council funds the Directorate and does not fully understand it. SED walks what the facility will later have to contain. UCD hits the Frays that feed on what leaks from both. Menders contract to RD and Architects at once. Wardens back all three and trust none of the paperwork.</p>
<p>Shared world: Zones A–E, the Desolate, Cheonbulok and Mugeukji as Corner cities, the Gate. Shared threat: Han that will not stay in one jurisdiction. The Absolvohan is an RD secret the Council is not meant to have; Weavers are watching it in Dream anyway. SED Canto text and UCD Arc text stay on those long articles — this URL is only the three-operation index so a search for “founding corporations” lands on a correction.</p>
</section>
<section class="wiki-section" id="not-wings"><h2 class="section-title">Not Wings</h2>
<p>Do not map R.D. to Lobotomy Corporation, SED to Limbus, UCD to a Fixer Office and call them precursor corporations. Analog research belongs in REFERENCE, not in this article’s heading stack. If you need the six Occlusihan factions (Sealers, Severers, Offerers, Exilers, Converters, Endurers), that is <a href="../lore/the-first-sovereign-war.html">the wars</a>, year 202–223, not year 4202.</p>
</section>
"""
    put(
        "factions/the-founding-corporations.html",
        "The Three Operations",
        "R.D., SED, and UCD — present-age operations after 4200, not founding precursor corporations.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Factions</a> <i>/</i> <span>Three Operations</span>',
        "The Three Operations",
        "FACTION · R.D. · SED · UCD",
        [("overview", "Overview"), ("connect", "How they connect"), ("not-wings", "Not Wings")],
        body,
        '<a href="the-reverie-directorate.html">Directorate</a> | <a href="the-sed-corps.html">SED</a> | <a href="the-ucd-strike-force.html">UCD</a>',
        "Three Operations Reverie Directorate SED UCD not founding corporations",
    )


def faction_tech():
    body = r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>This page is an <strong>index of unique tools</strong>, not a paste of <code>SOMNARAK_FACTION_TECH.md</code>. Each guild article has a Tools section with the long description. Resonances (Weight, Shaping, Scales, Archive, Barrier, Dream, Extraction) are not devices — they are <a href="../mechanics/taboo-resonance-mechanics.html">ways of touching Han</a>. M.A.W. is extracted sorrow, not faction tech.</p>
<p>A tool that judges its user (Ledger, Blade, Scale) is still a tool. A Place that eats visitors (Memory Archive under the Tree) is entity geography. Do not paste the nineteen tech chapters back onto this URL for “completeness.”</p>
</section>
<section class="wiki-section" id="guilds"><h2 class="section-title">Guild instruments</h2>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>Faction</th><th>Tools</th><th>What they do in one line</th><th>Article</th></tr></thead>
<tbody>
<tr><td>Council</td><td>Sigh Recorder, Decision Scale</td><td>Store exhaled burden; weigh a decision’s sorrow (not its joy)</td><td><a href="the-high-council.html">Council</a></td></tr>
<tr><td>Architects</td><td>Sorrow Compass, Han-Trowel</td><td>Find Han-flow; cut and seal crystal with the user’s feeling</td><td><a href="the-architects.html">Architects</a></td></tr>
<tr><td>Collectors</td><td>Debt-Ledger, Extraction Glove</td><td>Show weight; pull Echoes; both judge malice</td><td><a href="the-collectors.html">Collectors</a></td></tr>
<tr><td>Keepers</td><td>Memory Lens, Whispering Index</td><td>Play Echoes; catalog that speaks in riddles</td><td><a href="the-keepers.html">Keepers</a></td></tr>
<tr><td>Wardens</td><td>Barrier Baton, Watchtower Eye</td><td>Suppression field; Desolate scan that sees feeling</td><td><a href="the-wardens.html">Wardens</a></td></tr>
<tr><td>Weavers</td><td>Dream Loom, Resonance Mask</td><td>Pull/send through Somnus; anchor identity</td><td><a href="the-weavers.html">Weavers</a></td></tr>
<tr><td>R.D.</td><td>Lament Well, cells, rigs, gauges</td><td>Contain, extract, measure — Extraction Resonance on top</td><td><a href="the-reverie-directorate.html">R.D.</a></td></tr>
<tr><td>Judexhan</td><td>Judgment Blade, forehead implant</td><td>Cut Han-defense; count absorbed sorrow until retirement</td><td><a href="the-judexhan.html">Judexhan</a></td></tr>
<tr><td>Giltong</td><td>Taboo Scanner, Containment Bonds</td><td>Read violation signatures; shut down Resonances</td><td><a href="the-giltong-enforcers.html">Giltong</a></td></tr>
<tr><td>Menders</td><td>Kit, Repair Rod</td><td>Field repair paid in the Mender’s own sorrow</td><td><a href="the-menders.html">Menders</a></td></tr>
</tbody></table></div>
</section>
<section class="wiki-section" id="fray"><h2 class="section-title">Fray and Raw</h2>
<p>Harvesters (Harvest Hook into the sorrow-layer), Debt Brokers, Veil Merchants, Memory Washers (wash-rig), Entity Traders — kits in <a href="the-underworld-and-wound-walkers.html">underworld</a> and <a href="the-memory-washers.html">Washers</a>. Whisper Market, Debtless, Veil Breakers, Memory Thieves, Gate Runners are named rows in source; they do not each get a 1,196-file registry. UCD raids them. A Harvest Hook is a crime tool, not an R.D. extract. A wash-rig is not a Memory Lens. Do not mix them on a loadout screen.</p>
</section>
<section class="wiki-section" id="rule"><h2 class="section-title">Rule</h2>
<p>Handheld kit ≠ Resonance ≠ M.A.W. The Ledger is kit; the Scales is the Collector’s body. The Baton is kit; the Barrier is the Warden’s field. The extraction rig is kit; Extraction is the R.D. note. Faction Resonances are in <code>SOMNARAK_TABOO_RESONANCE.md</code> §II and on the Resonances article. Taboos are laws, not tools.</p>
</section>
"""
    put(
        "factions/faction-technology.html",
        "Faction Technology",
        "Index of guild tools vs Resonances vs M.A.W. Long descriptions live on each faction page.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Factions</a> <i>/</i> <span>Faction Technology</span>',
        "Faction Technology",
        "FACTIONS · INSTRUMENTS",
        [("overview", "Overview"), ("guilds", "Guild instruments"), ("fray", "Fray and Raw"), ("rule", "Rule")],
        body,
        '<a href="index.html">Factions</a> | <a href="../mechanics/taboo-resonance-mechanics.html">Resonances</a> | <a href="../maw/index.html">M.A.W.</a>',
        "Faction technology Debt-Ledger Dream Loom Judgment Blade Taboo Scanner Repair Rod Resonance",
    )


def assignment():
    body = r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p><strong>Agent assignment</strong> is facility-wide, not a Floor 1 protocol. The old Neutral Command article pasted the whole personnel-placement chapter under Majin’s floor. LC analog: employees are listed on a personnel page, not only on Control Team. This URL is that split.</p>
<p><em>“The right person in the right room can contain a monster. The wrong person in the wrong room becomes one.”</em></p>
</section>
<section class="wiki-section" id="process"><h2 class="section-title">Process</h2>
<p>New personnel are tested on Resilience, Clarity, Composure, and Resolve. Scores gate which floors they may hold. Transfers exist and need approval. Inside a floor, room assignment follows the entity in the cell — Work Type preference, Han element, and the agent’s worst stat. Rotation is scheduled so no one lives on Border Watch or Extraction until they Fracture.</p>
<p>Floor 1 (Majin) wants composure under silence. Floor 2 wants people who will take the armor off. Floor 3 (Zyrak) wants people who can finish an extract without keeping the donor’s habit. Floor 4 files the observation that made the paper necessary. Floor 5 (Mellda) wants resolve against Weight. Floor 8 wants people who can hear a voice from outside and not open the door. Neutral Command signs. Insight Forge observes. A refused transfer is still an assignment.</p>
</section>
<section class="wiki-section" id="cores"><h2 class="section-title">Cores are not assigned</h2>
<p>Echo-Cores are the floor until suppression or exile. Agents rotate. A Core Suppression is a floor event, not a transfer request. Panic is what happens when assignment was wrong; Fracture is further down that road. See <a href="../mechanics/panic-states-and-corrosion.html">Panic</a>, <a href="facility-upgrades.html">upgrades</a>, <a href="../factions/the-reverie-directorate.html">Directorate</a>.</p>
</section>
"""
    put(
        "departments/agent-assignment.html",
        "Agent Assignment",
        "Facility-wide personnel placement by Resilience, Clarity, Composure, Resolve — not a Floor 1 dump.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Departments</a> <i>/</i> <span>Agent Assignment</span>',
        "Agent Assignment",
        "FACILITY · PERSONNEL",
        [("overview", "Overview"), ("process", "Process"), ("cores", "Cores are not assigned")],
        body,
        '<a href="index.html">Departments</a> | <a href="floor-1-neutral-command.html">Floor 1</a> | <a href="../factions/the-reverie-directorate.html">R.D.</a>',
        "Agent Assignment Resilience Clarity Composure Resolve floors Echo-Cores",
    )


def upgrades():
    body = r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p><strong>Facility upgrades</strong> are how the Hand of Change grows across cycles — cells, gauges, corridors, Mnemonic Generator load. Not Floor 1’s private construction budget. Architects build it. Extraction pays in Han-flux. Neutral Command approves it. The old wiki dumped the growth chapter onto Majin’s floor because that is where the signature sits.</p>
</section>
<section class="wiki-section" id="kinds"><h2 class="section-title">Kinds</h2>
<p>Containment (better cells, faster lock), observation (gauges, cameras, Insight tools), welfare (SP recovery rooms — so assignment mistakes kill slower), expansion (new rooms on a floor, not a ninth floor). Each upgrade has a Han-flux cost and a downtime. You do not upgrade Border Watch during a Tide Watch.</p>
<p>Architects are the only Head that wants the building to change. The Council resists because uncertainty makes Han. That fight is civic. The facility version is this page: which valve, which cell, which cycle. Secret passages the Architects already built into Facility 01 are not an “upgrade” on this ledger — they are a debt the Directorate has not paid. Welfare rooms do not erase Panic; they buy a shift. Expansion that crosses a Han-flow line without a Sorrow Compass reading is how Floor 5 inherits a new aperture.</p>
</section>
<section class="wiki-section" id="freeze"><h2 class="section-title">When it freezes</h2>
<p>Facility Meltdown: no new cells, no new valves, no Architect crews in the corridors. Rebuild is a later cycle. Tide Watch is the same freeze, for a different alarm color. A completed upgrade that nobody staffs is just a new room for an Ordeal to spawn in. Sign the assignment first, or do not pour the Han. See <a href="agent-assignment.html">assignment</a>, <a href="facility-meltdown-procedures.html">meltdown</a>, <a href="../factions/the-architects.html">Architects</a>.</p>
</section>
"""
    put(
        "departments/facility-upgrades.html",
        "Facility Upgrades",
        "Hand of Change growth — containment, observation, welfare, expansion. Not a Floor 1 chapter.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Departments</a> <i>/</i> <span>Facility Upgrades</span>',
        "Facility Upgrades",
        "FACILITY · GROWTH",
        [("overview", "Overview"), ("kinds", "Kinds"), ("freeze", "When it freezes")],
        body,
        '<a href="index.html">Departments</a> | <a href="../factions/the-architects.html">Architects</a> | <a href="floor-1-neutral-command.html">Floor 1</a>',
        "Facility upgrades Hand of Change cells gauges Architects Meltdown",
    )


def research():
    body = r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The R.D. <strong>research / observation</strong> ladder is how a Sorrow Entity goes from a code on a door to a profile you can work. Not Floor 4’s private manual. Insight Forge (Ayshuk) files it. Every floor uses it. The old wiki pasted “Research System” under Floor 4 because that is the lab. LC analog: Abnormality observation lives on the Abnormality and on Info Team, not only on one department dump.</p>
<p><em>“You cannot contain what you do not understand. You cannot understand what you have not observed.”</em></p>
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
<p>Observation Level is not Hope Intensity and not Coherence. Mixing those three on a clipboard is how a TETH-shaped job gets an ALEPH-shaped funeral — and those LC words do not belong on the clipboard either. See <a href="floor-4-insight-forge.html">Floor 4</a>, <a href="../mechanics/secc-classification-system.html">SECC</a>, <a href="../mechanics/the-four-work-types.html">Work Types</a>, <a href="../maw/maw-crafting-and-extraction.html">Extraction</a>.</p>
</section>
"""
    put(
        "departments/research-observation.html",
        "Research and Observation",
        "R.D. observation levels 0–4. Facility-wide, not a Floor 4 dump.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Departments</a> <i>/</i> <span>Research and Observation</span>',
        "Research and Observation",
        "FACILITY · INSIGHT",
        [("overview", "Overview"), ("levels", "Observation levels")],
        body,
        '<a href="floor-4-insight-forge.html">Floor 4</a> | <a href="../mechanics/secc-classification-system.html">SECC</a> | <a href="../mechanics/the-four-work-types.html">Work Types</a>',
        "Observation Level research Insight Forge Work Types SECC extraction",
    )


def missions():
    body = r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>LC analog: the <em>Missions</em> catalog lists every department’s jobs; each team page also lists its own. This URL is the catalog. Floor pages keep their daily-mission tables — those are not facility-wide dumps. They are that floor’s work.</p>
<p>Quotas in Han-Energy are operational targets, not civic tax. Floor 6 and 7 file none — Deep Vault and Shadow Corps do not mint energy; they keep secrets and listen. Floor 2’s 500 is the heavy cell-work number. Floor 5’s 50 is the border’s thin yield. Do not confuse a daily quota with an Ordeal Watch or a Core Suppression.</p>
</section>
<section class="wiki-section" id="catalog"><h2 class="section-title">By floor</h2>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>Floor</th><th>Lead</th><th>What the day is</th><th>Quota</th></tr></thead>
<tbody>
<tr><td><a href="floor-1-neutral-command.html">1 Neutral Command</a></td><td>Majin</td><td>Command, alarms, assignment signatures — no mission table (HR on <a href="agent-assignment.html">assignment</a>)</td><td>—</td></tr>
<tr><td><a href="floor-2-maws-keep.html">2 M.A.W.’s Keep</a></td><td>—</td><td>Work Types, gauges, breach return, new-entity processing, cell repair, Maw perimeter</td><td>500</td></tr>
<tr><td><a href="floor-3-extraction-hall.html">3 Extraction Hall</a></td><td>Zyrak</td><td>Extract, resonance scan, test, bond, issue, refine</td><td>300</td></tr>
<tr><td><a href="floor-4-insight-forge.html">4 Insight Forge</a></td><td>Ayshuk</td><td>Observe, classify, map Han, document — ladder on <a href="research-observation.html">observation</a></td><td>100</td></tr>
<tr><td><a href="floor-5-border-watch.html">5 Border Watch</a></td><td>Mellda</td><td>Patrol, Desolate recon, watchtowers, Tide telemetry</td><td>50</td></tr>
<tr><td><a href="floor-6-deep-vault.html">6 Deep Vault</a></td><td>Marjuk</td><td>Archive, Echo stabilize, Cheongula vault — no energy quota</td><td>None</td></tr>
<tr><td><a href="floor-7-shadow-corps.html">7 Shadow Corps</a></td><td>Ishall</td><td>Intel, infiltration, informants, counter-intel — no energy quota</td><td>None</td></tr>
<tr><td><a href="floor-8-gate-watch.html">8 Gate Watch</a></td><td>Xyan</td><td>Watch the Gate, outside contact, record without controlling return</td><td>—</td></tr>
</tbody></table></div>
</section>
<section class="wiki-section" id="not"><h2 class="section-title">Not missions</h2>
<p>Ordeals (five colors × four watches) are not a daily mission. Core Suppression is not a daily mission. Facility Meltdown is not a daily mission. UCD raids and SED expeditions are city operations, not floor quotas. A “new entity processing” line on Floor 2 is still Floor 2’s job, even when the specimen walked in from Zone E. See <a href="../mechanics/ordeals-framework.html">Ordeals</a>, <a href="facility-meltdown-procedures.html">meltdown</a>, <a href="core-suppression-guidelines.html">Core suppression</a>.</p>
</section>
"""
    put(
        "departments/daily-missions.html",
        "Daily Missions",
        "Catalog of each floor’s daily work and Han-Energy quotas. Per-floor tables stay on the floor pages.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Departments</a> <i>/</i> <span>Daily Missions</span>',
        "Daily Missions",
        "FACILITY · MISSIONS CATALOG",
        [("overview", "Overview"), ("catalog", "By floor"), ("not", "Not missions")],
        body,
        '<a href="index.html">Departments</a> | <a href="agent-assignment.html">Assignment</a> | <a href="floor-2-maws-keep.html">Floor 2</a>',
        "Daily missions floors quota Han-Energy Maw Keep Border Watch Gate",
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
<section class="wiki-section" id="first"><h2 class="section-title">First Watch (minor)</h2>
<p>Early Management Phase. After two or three work cycles, Han-density is Elevated. Five to ten weak manifestations spawn as a warning that free Han is accumulating. A Level 2 team can suppress them. Analog: LC Dawn / TETH.</p>
<p>Named First Watch examples: Blue Weeping Cluster, Black Rolling Weight, Pale The Forgotten, Grey Resentful Three, Purple The Seeping. They last about a minute if ignored, then move or fade — but they leave residue (cracked floors, missing memories, Fracture-like film).</p>
</section>
<section class="wiki-section" id="second"><h2 class="section-title">Second Watch (moderate)</h2>
<p>Mid-Management. After five or six work cycles the gauge is Critical. Ten to twenty bodies, or fewer stronger ones. Level 3+ with M.A.W. Analog: LC Noon / HE. Corridors stop being a swarm of larvae and start being a fight. Grey forms battalions. Purple roots into the Han-flow. Pale starts erasing ranks, not single names.</p>
</section>
<section class="wiki-section" id="third"><h2 class="section-title">Third Watch (major)</h2>
<p>Late Management, approaching Sorrow Tide. After eight or more cycles, or near Tide. A single large entity or a coordinated horde. Level 4+, specialized M.A.W., Containment Lead oversight. Analog: LC Dusk / WAW. If Third Watch is not handled it does not politely become Tide Watch later — it <em>is</em> the on-ramp. Dekan’s manual treats an unsuppressed Third as a floor-loss risk, not a delay.</p>
</section>
<section class="wiki-section" id="tide"><h2 class="section-title">Tide Watch (catastrophic)</h2>
<p>Sorrow Tide peak only, or a major breach cascade. Facility-wide. Echo-Cores and their top teams. Analog: LC Midnight / ALEPH. An unsuppressed Tide Watch before dawn can permanently damage the Hand of Change. Ordeals are mortal; they do not return from the Weeping. Tide Watch is the only suppression that can drop facility Han-density enough to matter city-wide — which is why Majin vetoed “deliberately spawn Tide Watches to bleed the city” three times.</p>
<p>Facility upgrades freeze during Tide Watch the same way they freeze during Meltdown — different alarm, same “no Architect crews in the corridor.” See <a href="../departments/facility-upgrades.html">upgrades</a>.</p>
</section>
<section class="wiki-section" id="retired"><h2 class="section-title">Retired overlay</h2>
<p>Older wiki text named four events Whisper, Surge, Breach, and Abyss and mapped them to morning / midday / evening / night. That list does not match <code>SOMNARAK_ORDEALS_FRAMEWORK.md</code>. The canon grid is <strong>five colors × four watches</strong>.</p>
</section>
"""
    put(
        "mechanics/the-four-ordeals.html",
        "The Four Watches",
        "First, Second, Third, and Tide Watch — Ordeal time axis. Not Whisper/Surge/Breach/Abyss.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Mechanics</a> <i>/</i> <span>The Four Watches</span>',
        "The Four Watches",
        "ORDEALS · TIME AXIS",
        [
            ("overview", "Overview"),
            ("first", "First Watch"),
            ("second", "Second Watch"),
            ("third", "Third Watch"),
            ("tide", "Tide Watch"),
            ("retired", "Retired overlay"),
        ],
        body,
        '<a href="ordeals-framework.html">Ordeals</a> | <a href="ordeal-blue.html">Blue</a> | <a href="index.html">Mechanics</a>',
        "Four Watches First Watch Tide Watch Ordeals Blue Black Pale Grey Purple",
    )


def locations():
    put(
        "locations/the-orphan-bell-tower.html",
        "The Orphan Bell Tower",
        "Place of SE-001 The Orphaned Bell — Zone B grief architecture, Lament’s Requiem, not a Worldbuilding Framework stub.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Atlas</a> <i>/</i> <span>Orphan Bell Tower</span>',
        "The Orphan Bell Tower",
        "ATLAS · ZONE B · SE-001",
        [("overview", "Overview"), ("place", "Place"), ("sound", "What the tower does")],
        r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The <strong>Orphan Bell Tower</strong> is the place-name attached to <a href="../entities/se-001-the-orphaned-bell.html">SE-001 The Orphaned Bell</a>. It is not a Worldbuilding Framework dump, and it is not “Sector 7” in an LC facility sense. The bell’s tale line is: <em>“The bell tolls for children who will never grow old.”</em></p>
<p>SE-001 is a contained City Sorrow. The tower is the architecture that grew around that grief — a vertical room that still thinks it is calling children home. Directorate observation treats the site and the entity as one operational problem: you do not schedule the tower without scheduling the Bell. M.A.W. from this donor is the Lament set — Requiem, Shroud, Edge — not a containment-log satellite. Those fake Instinct/Insight logs were deleted.</p>
</section>
<section class="wiki-section" id="place"><h2 class="section-title">Place</h2>
<p>Zone B carries the city’s oldest sorrows. The Old Lament (옛 탄식) is inner B, closest to A: first homes of solidified grief, walls that replay settlers, buildings that grew faces. A bell-tower that refuses to stop being a school-yard signal belongs in that grain of the city even when the containment cell is inside Facility 01.</p>
<p>Keepers want the sound archived. Collectors have tried to price the hour. Wardens treat an unsanctioned ring as a crowd problem. Weavers say the overtones continue in Somnus after the bronze stops. See <a href="zone-b-west-ward.html">Zone B</a>.</p>
</section>
<section class="wiki-section" id="sound"><h2 class="section-title">What the tower does</h2>
<p>A bell that tolls for the unaged is a Place as much as a Subject. People who grew up in B report knowing the hour by a ring that is not on any civic clock. Work types, breach, and M.A.W. live on the entity article and on <a href="../maw/maw-w-001-01-the-laments-requiem.html">Lament’s Requiem</a>. Combat records do not belong on this URL. This article is the room.</p>
</section>
""",
        '<a href="index.html">Atlas</a> | <a href="../entities/se-001-the-orphaned-bell.html">SE-001</a> | <a href="zone-b-west-ward.html">Zone B</a>',
        "Orphan Bell Tower SE-001 Orphaned Bell Zone B Old Lament Lament Requiem",
    )
    put(
        "locations/the-hollow-glass.html",
        "The Hollow Glass",
        "Bong’s Zone D tavern — only named neutral ground. The unemptied glass at 8:47.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Atlas</a> <i>/</i> <span>The Hollow Glass</span>',
        "The Hollow Glass",
        "ATLAS · ZONE D · NEUTRAL GROUND",
        [("overview", "Overview"), ("glass", "The glass that never empties"), ("use", "Use")],
        r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p><strong>The Hollow Glass</strong> is a tavern in Zone D, not a District 4 memorial and not an empty canonical-record box. It is the only named neutral ground in D: Wardens, Frays, Menders, Collectors, and ordinary citizens drink side by side. Fights do not happen there because Bong will not serve anyone who starts one. His silence is the house rule. His memory is worse — which is to say, complete.</p>
<p>Bong (봉) was a Collector, one of the honest ones. He found a phantom debt written by Debt Brokers onto a family that had never borrowed. He reported it three times. He was ignored, threatened, then fired. He opened the Glass the next month. That phantom obligation is the Collectors’ Taboo-5-adjacent sin done as Fray work; Bong left rather than keep the ledger.</p>
</section>
<section class="wiki-section" id="glass"><h2 class="section-title">The glass that never empties</h2>
<p>Third seat from the left is empty. The glass there is always full of the cheapest Han-water. Bong’s wife Fractured behind the bar on a quiet Tuesday. He swept the crystal himself. He never changed the layout. Every evening at 8:47 — the minute of the Fracture — he fills the glass and moves on. People who know leave an Echo beside it. He spends those Echoes on more Han-water.</p>
<p>His question in the Cast file: <em>“If I serve everyone’s sorrow in a glass, who serves mine?”</em> The tavern is open. The seat is empty. That is the memorial. There is no plaque, no Council ribbon, no SECC file.</p>
</section>
<section class="wiki-section" id="use"><h2 class="section-title">Use</h2>
<p>SED and UCD both know the door. Information moves here because nobody is in uniform at the bar — or everyone is, and Bong does not care. Neutral does not mean safe outside the threshold. Zone D is forge and gardens, Furnace refugees, Mender traffic. See <a href="zone-d-forge-and-gardens.html">Zone D</a>, <a href="../factions/the-underworld-and-wound-walkers.html">the underworld</a>, <a href="../factions/the-wardens.html">Wardens</a>.</p>
</section>
""",
        '<a href="index.html">Atlas</a> | <a href="zone-d-forge-and-gardens.html">Zone D</a> | <a href="../factions/the-underworld-and-wound-walkers.html">Underworld</a>',
        "Hollow Glass Bong Zone D tavern neutral ground 8:47 Debt Brokers",
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
<p>SE-009 weaves memories into webs. The library is the architecture of that habit: shelves that are not a civic catalog, pages that are not consented Echoes. R.D. Observation Level 3. The entity is mobile. The room is still a Place — people get lost in the stacks for hours they cannot later name.</p>
</section>
<section class="wiki-section" id="not-archive"><h2 class="section-title">Not the Grand Archive</h2>
<p>Building 2, Zone A, is the Keepers’ Grand Archive: history, Whispering Index, vaults into Dream-space. The Library of Stolen Pasts is a Zone B containment geography. Memory Fray / Washers steal from the Archive and sell. SE-009 is what happens when stolen recollection coagulates into a weaver instead of a ledger.</p>
<p>M.A.W. from this entity is the Forgotten set — <a href="../maw/maw-w-009-01-the-forgotten-lens.html">Forgotten Lens</a>, Veil, Mask — not the misfiled “Memory Blade” on the SE-003 slot. See <a href="../factions/the-memory-washers.html">Memory Washers</a> and <a href="zone-b-west-ward.html">Zone B</a>.</p>
</section>
<section class="wiki-section" id="work"><h2 class="section-title">Working the stacks</h2>
<p>Valid work against a memory-pressure Subject is not “read quietly.” Insight and related types on the entity page apply. Failed work or ignored activation (Sorrow Gauge climbing) is a breach of identity, not of masonry. Agents report leaving with someone else’s childhood stuck under the tongue.</p>
<p>Observation Level 3 means a Containment Lead signs the stack map before a new agent walks in; Floor 4 Insight Forge can request a memory-trace after, not during. If the room starts filing <em>your</em> name on a spine, leave. That is not a catalog error. That is the Weaver noticing you. Combat, SECC, and M.A.W. stay on the entity and arsenal pages. This article is the room.</p>
</section>
""",
        '<a href="index.html">Atlas</a> | <a href="../entities/se-009-the-memory-weaver.html">SE-009</a> | <a href="zone-b-west-ward.html">Zone B</a>',
        "Library of Stolen Pasts SE-009 Memory Weaver Zone B Forgotten Lens",
    )


def alpha():
    put(
        "lore/the-alpha-tree.html",
        "The Alpha Tree",
        "Cumulation of Consolihan feeling — six buildings, plaza of polished Han, R.D. in the roots.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Lore</a> <i>/</i> <span>Alpha Tree</span>',
        "The Alpha Tree",
        "LORE · ZONE A · CUMULATION",
        [("overview", "Overview"), ("six", "Six buildings"), ("roots", "Roots")],
        r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The <strong>Alpha Tree</strong> is not a building someone designed. It is a <strong>cumulation</strong> — the physical gathering of what Somnarak felt during the Consolihan, when flowing Han was frozen into meaning. The tallest pillar of a fortress built from frozen tears. The city grew around it the way crystal grows on crystal.</p>
<p>It sits at Zone A’s heart. Citizens are not permitted in the central plaza — only faction members and Council summons. The ground is polished Han, smooth, dark, faintly warm. The plaza hums. The city’s heartbeat. Open to the sky — one of the few places in A where you can see it.</p>
</section>
<section class="wiki-section" id="six"><h2 class="section-title">Six buildings</h2>
<p>Grief: weeping walls of the <strong>Sigh Palace</strong> (Council, north). Love: the bonds that hold the six together. Dream: <strong>Spire of Dreams</strong> (Weavers, south) reaching toward what could be. Nightmare: <strong>Abyssal Well</strong> (southwest) plunging into what must not be. Happiness: rare light through the <strong>Grand Archive</strong> (Keepers, northeast). Sadness: the weight that anchors the <strong>Crucible</strong> (southeast). Northwest: <strong>Architect’s Hall</strong>.</p>
<p>Taboo 1 exists because the Cheongula’s thousand stabilize this Tree. Returned dead would unseat it. The R.D. is not a seventh building on the plaza; it is the basement. See <a href="../locations/zone-a-core-nexus.html">Zone A</a> and <a href="the-first-sovereign-war.html">Consolihan</a>.</p>
</section>
<section class="wiki-section" id="roots"><h2 class="section-title">Roots</h2>
<p>The same Han-crystal continues down as Facility 01 — the Hand of Change. Marjuk’s Deep Vault is “A (Deep).” Retired Judexhan are taken under the Tree; source does not say what happens next. Dream Veil is thinner here. Keepers’ lowest vaults and the hungry Memory Archive both claim the underside. Do not treat those as one room.</p>
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
    print("expand B done")


if __name__ == "__main__":
    main()
