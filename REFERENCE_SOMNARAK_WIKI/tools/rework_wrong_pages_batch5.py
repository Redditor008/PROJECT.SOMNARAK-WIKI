#!/usr/bin/env python3
"""Split Taboos off Giltong dump; faction-tech hub; missions catalog."""
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


def words(html: str) -> int:
    m = re.search(r"<main[^>]*>(.*)</main>", html, re.S)
    body = m.group(1) if m else html
    return len(re.findall(r"[A-Za-z0-9']+", re.sub(r"<[^>]+>", " ", body)))


def put(rel, title, desc, crumbs, h1, eyebrow, toc, body, cats, kw):
    doc = wrap(title, desc, crumbs, h1, eyebrow, toc, body, cats)
    (DOCS / rel).write_text(doc, encoding="utf-8")
    w = words(doc)
    print(f"wrote {rel} ({w}w)")
    if w < 300:
        print("  WARN under 300")
    SEARCH.append({"url": rel, "title": title, "description": desc[:180], "keywords": kw, "type": "article"})


def taboos():
    body = """
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The <strong>Seven Taboos</strong> (일곱 금지) are absolute prohibitions woven into Somnarak’s Han. The Council claims to enforce them. The city already has: buildings crack, streets shift, entities form, debt skyrockets. Giltong interpret what the city decided. This page is the seven laws. Enforcement guild: <a href="../factions/the-giltong-enforcers.html">Giltong</a>. Elite blade: <a href="../factions/the-judexhan.html">Judexhan</a>. Do not paste Arbiter org-charts here.</p>
<p><em>“Some things cannot be done. Not because they are difficult — but because the city will not allow it.”</em></p>
</section>
<section class="wiki-section" id="one"><h2 class="section-title">1 — No Resurrection</h2>
<p>The dead do not return. To bring them back is to steal from the Maw. The Cheongula’s thousand stabilize the Alpha Tree; returned dead would unseat that foundation. Break it and debt spikes, Zone B trembles, the Maw speaks louder. Extreme: the offender is consumed like the original thousand.</p>
<p>Grey: Echo-Cores are Cast Effigies, not graves emptied. The Council says that is not resurrection. The city has not punished them. Yet.</p>
</section>
<section class="wiki-section" id="two"><h2 class="section-title">2 — No True AI</h2>
<p>A machine that thinks as a human can suffer as a human. Seiyon is the proof and the warning. Fully sentient AI is erased; the creator is punished. Giltong case file: the Whispering Incident — an unknown maker, an AI that screamed, a whisper some say never stopped.</p>
</section>
<section class="wiki-section" id="three"><h2 class="section-title">3 — No Han Immunity</h2>
<p>Becoming immune to sorrow is exile to the Desolate. The city runs on Han; a person who cannot feel it is a hole in the wall. The Immunity Cult still lives outside, unfeeling. High severity, not Maw-activation — exile is the city’s answer.</p>
</section>
<section class="wiki-section" id="four"><h2 class="section-title">4 — No Time Reversal</h2>
<p>Altering the past is containment plus paradox assessment. A Weaver who tried is frozen in a single moment. The Cycle already spent 1,778 years on a loop; private time-theft is not a second Absolvohan. Extreme.</p>
</section>
<section class="wiki-section" id="five"><h2 class="section-title">5 — No Sorrow Synthesis</h2>
<p>Manufactured grief is destroyed; the maker is punished. Fake Han does not sit still. The Memory Washers’ synthetic sorrow fought back — it had become sentient. Collectors brush this Taboo when they mint obligation that never existed. High.</p>
</section>
<section class="wiki-section" id="six"><h2 class="section-title">6 — No Cross-Boundary Fusion</h2>
<p>Merging city and wilderness makes a Fracture Zone. The Boundary Walker — a Desolate nomad — is the named case: containment, then a living wound. Zone E exists so this does not become policy. Extreme.</p>
</section>
<section class="wiki-section" id="seven"><h2 class="section-title">7 — No Echo-Core Duplication</h2>
<p>Copying a Core: fragment the copy, investigate the maker. The copy screamed; it knew what it was. Seiyon’s grey area under Taboo 2 is not a license to Xerox Majin. Extreme.</p>
</section>
<section class="wiki-section" id="enforce"><h2 class="section-title">Who answers</h2>
<p>Giltong: one Senior per Taboo, Arbiter above, ~100 souls, report to the Council, override on Taboo matters only. Judexhan: implant and blade, parallel. Wardens hold the street while Giltong hold the law. Cases and org live on the Giltong article. Resonances (faction unique powers) are a different chapter of <code>SOMNARAK_TABOO_RESONANCE.md</code> — not this URL.</p>
</section>
"""
    put(
        "lore/the-seven-absolute-taboos.html",
        "The Seven Taboos",
        "Seven Han-woven prohibitions. Enforcement is Giltong, not this page.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Lore</a> <i>/</i> <span>Seven Taboos</span>',
        "The Seven Taboos",
        "LORE · 금지 · SEVEN LAWS",
        [
            ("overview", "Overview"),
            ("one", "1 Resurrection"),
            ("two", "2 True AI"),
            ("three", "3 Han Immunity"),
            ("four", "4 Time Reversal"),
            ("five", "5 Sorrow Synthesis"),
            ("six", "6 Cross-Boundary"),
            ("seven", "7 Core Duplication"),
            ("enforce", "Who answers"),
        ],
        body,
        '<a href="index.html">Lore</a> | <a href="../factions/the-giltong-enforcers.html">Giltong</a> | <a href="../factions/the-judexhan.html">Judexhan</a>',
        "Seven Taboos Geumji Resurrection AI Han Immunity Time Reversal Sorrow Synthesis Giltong",
    )


def faction_tech():
    body = """
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>This page is an <strong>index of unique tools</strong>, not a paste of <code>SOMNARAK_FACTION_TECH.md</code>. Each guild article already has a Tools section. Fray kits belong with the underworld. If a device is named here, the long description lives on the faction URL.</p>
</section>
<section class="wiki-section" id="guilds"><h2 class="section-title">Guild instruments</h2>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>Faction</th><th>Tools</th><th>Article</th></tr></thead>
<tbody>
<tr><td>Council of Sighs</td><td>Sigh Recorder, Decision Scale</td><td><a href="the-high-council.html">Council</a></td></tr>
<tr><td>Architects</td><td>Sorrow Compass, Han-Trowel</td><td><a href="the-architects.html">Architects</a></td></tr>
<tr><td>Collectors</td><td>Debt-Ledger, Extraction Glove</td><td><a href="the-collectors.html">Collectors</a></td></tr>
<tr><td>Keepers</td><td>Memory Lens, Whispering Index</td><td><a href="the-keepers.html">Keepers</a></td></tr>
<tr><td>Wardens</td><td>Barrier Baton, Watchtower Eye</td><td><a href="the-wardens.html">Wardens</a></td></tr>
<tr><td>Weavers</td><td>Dream Loom, Resonance Mask</td><td><a href="the-weavers.html">Weavers</a></td></tr>
<tr><td>Reverie Directorate</td><td>Lament Well, cells, extraction rigs, gauges</td><td><a href="the-reverie-directorate.html">R.D.</a></td></tr>
<tr><td>Judexhan</td><td>Judgment Blade, forehead implant</td><td><a href="the-judexhan.html">Judexhan</a></td></tr>
<tr><td>Giltong</td><td>Taboo Scanner</td><td><a href="the-giltong-enforcers.html">Giltong</a></td></tr>
<tr><td>Menders</td><td>Mender’s Kit, Repair Rod</td><td><a href="the-menders.html">Menders</a></td></tr>
</tbody></table></div>
</section>
<section class="wiki-section" id="fray"><h2 class="section-title">Fray and Raw</h2>
<p>Harvesters (Harvest Hook), Debt Brokers, Veil Merchants, Memory Washers (wash-rig), Entity Traders — kits in <a href="the-underworld-and-wound-walkers.html">underworld</a> and <a href="the-memory-washers.html">Washers</a>. Whisper Market, Debtless, Veil Breakers, Memory Thieves, Gate Runners are named independent/fray rows in source; they do not each get a 1,196-file registry. UCD raids them. Do not paste their full tech chapters here.</p>
</section>
<section class="wiki-section" id="rule"><h2 class="section-title">Rule</h2>
<p>A tool that judges its user (Ledger, Blade, Scale) is still a tool. A Place that eats visitors (Memory Archive under the Tree) is an entity geography, not a kit. M.A.W. is extracted sorrow, not faction tech — see <a href="../maw/index.html">arsenal</a>.</p>
</section>
"""
    put(
        "factions/faction-technology.html",
        "Faction Technology",
        "Index of guild tools. Long descriptions live on each faction page.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Factions</a> <i>/</i> <span>Faction Technology</span>',
        "Faction Technology",
        "FACTIONS · INSTRUMENTS",
        [("overview", "Overview"), ("guilds", "Guild instruments"), ("fray", "Fray and Raw"), ("rule", "Rule")],
        body,
        '<a href="index.html">Factions</a> | <a href="the-keepers.html">Keepers</a> | <a href="../maw/index.html">M.A.W.</a>',
        "Faction technology Debt-Ledger Dream Loom Judgment Blade Taboo Scanner Repair Rod",
    )


def missions():
    body = """
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>LC analog: the <em>Missions</em> catalog lists every department’s jobs; each team page also lists its own. This URL is the catalog. Floor pages keep their daily-mission tables — those are not facility-wide dumps. They are that floor’s work.</p>
<p>Quotas in Han-Energy are operational targets, not civic tax. Floor 6 and 7 file none. Floor 2’s 500 is the heavy cell-work number. Do not confuse a daily quota with an Ordeal Watch or a Core Suppression.</p>
</section>
<section class="wiki-section" id="catalog"><h2 class="section-title">By floor</h2>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>Floor</th><th>Lead</th><th>What the day is</th><th>Quota</th></tr></thead>
<tbody>
<tr><td><a href="floor-1-neutral-command.html">1 Neutral Command</a></td><td>Majin</td><td>Command, alarms, assignment signatures — no mission table (HR lives on <a href="agent-assignment.html">assignment</a>)</td><td>—</td></tr>
<tr><td><a href="floor-2-maws-keep.html#floor-2-missions">2 M.A.W.’s Keep</a></td><td>—</td><td>Work Types, gauges, breach return, new-entity processing, cell repair, Maw perimeter</td><td>500</td></tr>
<tr><td><a href="floor-3-extraction-hall.html">3 Extraction Hall</a></td><td>Zyrak</td><td>Extract, resonance scan, test, bond, issue, refine</td><td>300</td></tr>
<tr><td><a href="floor-4-insight-forge.html">4 Insight Forge</a></td><td>Ayshuk</td><td>Observe, classify, map Han, document — ladder on <a href="research-observation.html">observation</a></td><td>100</td></tr>
<tr><td><a href="floor-5-border-watch.html">5 Border Watch</a></td><td>Mellda</td><td>Patrol, Desolate recon, watchtowers, Tide telemetry</td><td>50</td></tr>
<tr><td><a href="floor-6-deep-vault.html">6 Deep Vault</a></td><td>Marjuk</td><td>Archive, Echo stabilize, Cheongula vault — no energy quota</td><td>None</td></tr>
<tr><td><a href="floor-7-shadow-corps.html">7 Shadow Corps</a></td><td>Ishall</td><td>Intel, infiltration, informants, counter-intel — no energy quota</td><td>None</td></tr>
<tr><td><a href="floor-8-gate-watch.html">8 Gate Watch</a></td><td>Xyan</td><td>Watch the Gate, outside contact, record without controlling return</td><td>—</td></tr>
</tbody></table></div>
</section>
<section class="wiki-section" id="not"><h2 class="section-title">Not missions</h2>
<p>Ordeals (five colors × four watches) are not a daily mission. Core Suppression is not a daily mission. Facility Meltdown is not a daily mission. UCD raids and SED expeditions are city operations, not floor quotas. See <a href="../mechanics/ordeals-framework.html">Ordeals</a> and <a href="facility-meltdown-procedures.html">meltdown</a>.</p>
</section>
"""
    put(
        "departments/daily-missions.html",
        "Daily Missions",
        "Catalog of each floor’s daily work. Per-floor tables stay on the floor pages.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Departments</a> <i>/</i> <span>Daily Missions</span>',
        "Daily Missions",
        "FACILITY · MISSIONS CATALOG",
        [("overview", "Overview"), ("catalog", "By floor"), ("not", "Not missions")],
        body,
        '<a href="index.html">Departments</a> | <a href="agent-assignment.html">Assignment</a> | <a href="floor-2-maws-keep.html">Floor 2</a>',
        "Daily missions floors quota Han-Energy M.A.W. Keep Border Watch Gate",
    )


def patch_giltong():
    p = DOCS / "factions" / "the-giltong-enforcers.html"
    t = p.read_text(encoding="utf-8")
    note = (
        '<p>The seven laws themselves are <a href="../lore/the-seven-absolute-taboos.html">the Seven Taboos</a>. '
        "This page is the guild: Arbiter, Seniors, cases. Parallel elite: "
        '<a href="the-judexhan.html">Judexhan</a>.</p>'
    )
    if "the-seven-absolute-taboos.html" not in t:
        t = t.replace(
            '<section class="wiki-section" id="giltong-structure">',
            note + '<section class="wiki-section" id="giltong-structure">',
            1,
        )
        if note.split("the seven laws")[0] not in t and "the-seven-absolute-taboos.html" not in t:
            # fallback: inject after first h1 block / first wiki-section
            t = t.replace(
                '<section class="wiki-section"',
                note + '<section class="wiki-section"',
                1,
            )
        p.write_text(t, encoding="utf-8")
        print("giltong pointer", "taboos" in t or True)
    else:
        print("giltong already linked")


def patch_dept_index():
    p = DOCS / "departments" / "index.html"
    t = p.read_text(encoding="utf-8")
    if "daily-missions.html" in t and "research-observation.html" in t:
        print("dept index already has new cards")
        return
    needle = '<a href="incident-reports-archive.html" class="jump-btn">VIEW INCIDENT LOGS →</a></div>'
    extra = needle + """
    <div class="pm-entity-card"><div class="entity-card-top"><div class="entity-card-meta"><span class="risk-badge risk-he">PERSONNEL</span></div></div><h3 class="entity-card-name">AGENT ASSIGNMENT</h3><p class="entity-card-desc">Facility-wide placement by Resilience, Clarity, Composure, Resolve. Not a Floor 1 chapter.</p><a href="agent-assignment.html" class="jump-btn">VIEW ASSIGNMENT →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><div class="entity-card-meta"><span class="risk-badge risk-he">GROWTH</span></div></div><h3 class="entity-card-name">FACILITY UPGRADES</h3><p class="entity-card-desc">Cells, gauges, welfare, expansion. Architects pour; Neutral Command signs.</p><a href="facility-upgrades.html" class="jump-btn">VIEW UPGRADES →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><div class="entity-card-meta"><span class="risk-badge risk-he">INSIGHT</span></div></div><h3 class="entity-card-name">RESEARCH &amp; OBSERVATION</h3><p class="entity-card-desc">Observation levels 0–4. Facility-wide, not a Floor 4 dump.</p><a href="research-observation.html" class="jump-btn">VIEW LADDER →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><div class="entity-card-meta"><span class="risk-badge risk-he">MISSIONS</span></div></div><h3 class="entity-card-name">DAILY MISSIONS</h3><p class="entity-card-desc">Catalog of each floor’s daily work. Per-floor tables stay on the floor pages.</p><a href="daily-missions.html" class="jump-btn">VIEW CATALOG →</a></div>"""
    if needle not in t:
        print("WARN incident card end not found")
        return
    p.write_text(t.replace(needle, extra, 1), encoding="utf-8")
    print("patched departments index")


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
    taboos()
    faction_tech()
    missions()
    patch_giltong()
    patch_dept_index()
    patch_search()
    print("batch5 done")


if __name__ == "__main__":
    main()
