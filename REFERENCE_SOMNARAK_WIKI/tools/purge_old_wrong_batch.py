#!/usr/bin/env python3
"""Purge nested satellite stubs and leftover dump crumbs. Rewrite wrong articles."""
from __future__ import annotations

import json
import pathlib
import re

ROOT = pathlib.Path("/home/user/PROJECT.SOMNARAK-WIKI")
DOCS = ROOT / "docs"
CSSV = "20260830af"

# Old nested subpages from build_all_nested_subpages.py — fake LC logs, not canon.
PURGE = {
    "entities/se-001-containment-log.html": "entities/se-001-the-orphaned-bell.html",
    "entities/se-002-incident-log.html": "entities/se-002-the-grieving-colossus.html",
    "entities/se-003-field-survey.html": "entities/se-003-the-wilderness-tide.html",
    "entities/se-005-suppression-guide.html": "entities/se-005-the-smothering-mother.html",
    "entities/se-007-observation-log.html": "entities/se-007-brume.html",
    "entities/se-009-memory-extracts.html": "entities/se-009-the-memory-weaver.html",
    "entities/se-010-verdict-records.html": "entities/se-010-the-convergence.html",
    "entities/se-011-acoustic-analysis.html": "entities/se-011-the-whispering-walls.html",
    "entities/se-014-debt-ledger.html": "entities/se-014-the-debt-eater.html",
    "entities/se-015-equilibrium-trials.html": "entities/se-015-the-debt-scale.html",
    "departments/floor-1-sub-protocols.html": "departments/floor-1-neutral-command.html",
    "departments/floor-2-arsenal-vaults.html": "departments/floor-2-maws-keep.html",
    "departments/floor-3-extraction-protocols.html": "departments/floor-3-extraction-hall.html",
    "departments/floor-4-insight-observation-labs.html": "departments/floor-4-insight-forge.html",
    "departments/floor-5-border-containment-cells.html": "departments/floor-5-border-watch.html",
    "departments/floor-6-deep-vault-records.html": "departments/floor-6-deep-vault.html",
    "departments/floor-7-shadow-corps-operations.html": "departments/floor-7-shadow-corps.html",
    "departments/floor-8-gate-watch-perimeter.html": "departments/floor-8-gate-watch.html",
    "locations/zone-a-central-spire.html": "locations/zone-a-core-nexus.html",
    "locations/zone-b-giltong-slums.html": "locations/zone-b-west-ward.html",
    "locations/zone-c-auction-houses.html": "locations/zone-c-collectors-row.html",
    "locations/zone-d-han-refineries.html": "locations/zone-d-forge-and-gardens.html",
    "locations/zone-e-frontier-ramparts.html": "locations/zone-e-perimeter-bulwark.html",
}


def rewrite_links(html: str, src_rel: str) -> str:
    src_dir = pathlib.PurePosixPath(src_rel).parent
    out = html
    for old, new in PURGE.items():
        old_name = pathlib.PurePosixPath(old).name
        new_name = pathlib.PurePosixPath(new).name
        old_dir = pathlib.PurePosixPath(old).parent
        new_dir = pathlib.PurePosixPath(new).parent
        # same-folder filename
        out = out.replace(old_name, new_name)
        # full relative from docs root
        out = out.replace(old, new)
        # ../folder/file
        out = out.replace(f"../{old}", f"../{new}")
    return out


def purge_satellites():
    # rewrite every html then delete
    for p in DOCS.rglob("*.html"):
        if "assets" in p.parts:
            continue
        rel = str(p.relative_to(DOCS)).replace("\\", "/")
        raw = p.read_text(encoding="utf-8", errors="replace")
        new = rewrite_links(raw, rel)
        if new != raw:
            p.write_text(new, encoding="utf-8")
            print("rewrote links", rel)
    deleted = []
    for old in PURGE:
        path = DOCS / old
        if path.exists():
            path.unlink()
            deleted.append(old)
            print("DELETED", old)
    sp = DOCS / "data" / "search.json"
    data = json.loads(sp.read_text(encoding="utf-8"))
    keep = [e for e in data if e.get("url") not in PURGE]
    sp.write_text(json.dumps(keep, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"search {len(data)} -> {len(keep)}; deleted {len(deleted)}")


def strip_architects_crumb():
    p = DOCS / "factions" / "the-architects.html"
    t = p.read_text(encoding="utf-8")
    t2 = re.sub(
        r'<section class="wiki-section" id="worldbuilding-framework">.*?</section>',
        "",
        t,
        count=1,
        flags=re.S,
    )
    t2 = t2.replace('<li><a href="#worldbuilding-framework">Worldbuilding Framework</a></li>\n', "")
    if t2 != t:
        p.write_text(t2, encoding="utf-8")
        print("stripped Architects Worldbuilding Framework leftover")


# reuse chrome from previous generator by importing is messy; inline a compact wrap
from html import escape as esc

HEADER = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{{title}} — Somnarak Official Wiki</title>
<meta name="description" content="{{desc}}"/>
<link href="../assets/icons/somnarak_icon.svg" rel="icon" type="image/svg+xml"/>
<link href="../assets/css/wiki.css?v={CSSV}" rel="stylesheet"/>
<script defer src="../assets/js/wiki.js?v={CSSV}"></script>
</head>
<body>
<header class="utility">
<div class="utility-left">
<button aria-label="Open navigation" class="nav-open" type="button">☰</button>
<a class="utility-brand" href="../index.html">SOMNARAK.WIKI</a>
<span class="utility-era">YEAR 4,238 · DAWN INITIATIVE</span>
</div>
<nav aria-label="Main navigation">
<a href="../index.html">Main page</a>
<a href="../characters/index.html">Characters</a>
<a href="../lore/index.html">Lore</a>
<a href="../locations/index.html">Atlas</a>
<a href="../factions/index.html">Factions</a>
<a href="../departments/index.html">Departments</a>
<a href="../entities/index.html">Entities</a>
<a href="../maw/index.html">M.A.W.</a>
<a href="../mechanics/index.html">Mechanics</a>
</nav>
<div class="search">
<input autocomplete="off" id="search" data-index="../data/search.json" placeholder="Search archive...">
<div id="results"></div>
</div>
</header>
<div class="wiki-shell">
<aside class="left-rail">
<div class="site-mark">
<a href="../index.html">
<img src="../assets/icons/somnarak_icon.svg" alt="Somnarak Emblem">
<b>SOMNARAK</b>
<span>OFFICIAL WIKI ARCHIVE</span>
</a>
</div>
<nav aria-label="Wiki navigation" class="left-links">
<section>
<h2>DATABASE HUBS</h2>
<a href="../index.html">Main Overview</a>
<a href="../entities/index.html">Sorrow Entities</a>
<a href="../factions/index.html">Factions &amp; Guilds</a>
<a href="../departments/index.html">Facility Floors</a>
<a href="../mechanics/ordeals-framework.html">Ordeals</a>
<a href="../lore/index.html">Lore &amp; Cosmology</a>
</section>
</nav>
</aside>
<main id="content">
"""

FOOT = """
<footer class="article-footer">
<div class="footer-categories"><strong>Categories:</strong> {cats}</div>
</footer>
</main></div></body></html>
"""


def wrap(title, desc, crumbs, h1, eyebrow, toc_items, body, cats):
    lis = "\n".join(f'<li><a href="#{i}">{esc(t)}</a></li>' for i, t in toc_items)
    toc = f'<nav class="toc hub-toc toc-panel"><div class="toc-title">Contents</div><ol>{lis}</ol></nav>'
    art = f"""<div class="breadcrumbs">{crumbs}</div>
<div class="article-header">
<div class="article-eyebrow">{esc(eyebrow)}</div>
<h1 class="article-title">{esc(h1)}</h1>
</div>
{toc}
{body}
"""
    return HEADER.format(title=esc(title), desc=esc(desc)[:300]) + art + FOOT.format(cats=cats)


def rewrite_four_watches():
    body = """
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p><strong>The Four Watches</strong> are the time axis of Ordeals. Color is the Han type (Blue Lament, Black Weight, Pale Void, Grey Grudge, Purple raw Han). Time is severity. This page is Dawn / Noon / Dusk / Midnight in LC terms — First, Second, Third, and Tide Watch. It is <em>not</em> Whisper / Surge / Breach / Abyss. That four-name overlay was a dump leftover and is retired.</p>
<p>One Ordeal per Time per day. Times escalate. Color articles list the named manifestations:</p>
<p>
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
<p>Mid-Management. After five or six work cycles the gauge is Critical. Ten to twenty bodies, or fewer stronger ones. Level 3+ with M.A.W. Analog: LC Noon / HE.</p>
<p>Second Watch is where corridors stop being “a swarm of larvae” and start being a fight. Grey forms battalions. Purple roots into the Han-flow. Pale starts erasing ranks, not single names.</p>
</section>
<section class="wiki-section" id="third"><h2 class="section-title">Third Watch (major)</h2>
<p>Late Management, approaching Sorrow Tide. After eight or more cycles, or near Tide. A single large entity or a coordinated horde. Level 4+, specialized M.A.W., Containment Lead oversight. Analog: LC Dusk / WAW.</p>
<p>If Third Watch is not handled it does not politely become Tide Watch later — it <em>is</em> the on-ramp. Dekan’s manual treats an unsuppressed Third as a floor-loss risk, not a delay.</p>
</section>
<section class="wiki-section" id="tide"><h2 class="section-title">Tide Watch (catastrophic)</h2>
<p>Sorrow Tide peak only, or a major breach cascade. Facility-wide. Echo-Cores and their top teams. Analog: LC Midnight / ALEPH. An unsuppressed Tide Watch before dawn can permanently damage the Hand of Change.</p>
<p>Ordeals are mortal. They do not return from the Weeping. Tide Watch is the only suppression that can drop facility Han-density enough to matter city-wide — which is why Majin vetoed “deliberately spawn Tide Watches to bleed the city” three times.</p>
</section>
<section class="wiki-section" id="retired"><h2 class="section-title">Retired overlay</h2>
<p>Older wiki text named four events Whisper, Surge, Breach, and Abyss and mapped them to morning / midday / evening / night. That list mixed city atmosphere with Ordeals and does not match <code>SOMNARAK_ORDEALS_FRAMEWORK.md</code>. The canon grid is <strong>five colors × four watches</strong>. Use the color articles and this time axis.</p>
</section>
"""
    crumbs = '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Mechanics</a> <i>/</i> <span>The Four Watches</span>'
    cats = '<a href="ordeals-framework.html">Ordeals</a> | <a href="the-four-ordeals.html">Four Watches</a> | <a href="index.html">Mechanics</a>'
    doc = wrap(
        "The Four Watches",
        "First, Second, Third, and Tide Watch — the time axis of Ordeals. Not Whisper/Surge/Breach/Abyss.",
        crumbs,
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
        cats,
    )
    (DOCS / "mechanics" / "the-four-ordeals.html").write_text(doc, encoding="utf-8")
    print("rewrote the-four-ordeals.html as Four Watches")


def rewrite_memory_washers():
    body = """
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The <strong>Memory Washers</strong> (기억 세척자) are not the Keepers. Keepers (기록관) preserve the Archive. Washers erase. They are a Fray operation in Zone B and C — the Wash District — and they are the subject of UCD Arc 2. The old wiki page pasted Keeper lore onto this URL. That paste is gone.</p>
<p>A wash-rig strips a memory from a living person and sells the remainder. Victims keep walking. They cannot say what was taken. Collectors hate them because washed debt is hard to prove. Keepers hunt them because the Archive is supposed to be the only legal memory store.</p>
</section>
<section class="wiki-section" id="place"><h2 class="section-title">Place in the underworld</h2>
<p>Underworld classification files them with the Memory Fray / Memory Cartel (기억 카르텔), territory Zone B + C, specialty memory trafficking. The leader-title in the Fray table is “The Index,” a former Keeper. UCD treats the Washers as a raid target, not a guild with a Council seat.</p>
<p>Related Frays: Harvesters (forced Echo extraction), Debt Brokers (Zone C debt trading), Veil Merchants (counterfeit Veil), Entity Traders (captured SEs). Washers sit on the memory commodity: stolen Archive pages and washed civilian recollection, priced “varies — rare memories are priceless.”</p>
</section>
<section class="wiki-section" id="ucd"><h2 class="section-title">UCD Arc 2</h2>
<p><a href="the-ucd-strike-force.html">Underworld Cleanup Descend</a> Arc 2 is the Wash District operation: victims, the wash-rig, the harvest, confrontation, choice, return. That Canto-style article keeps the chapter text. This page is the faction identity — who they are when they are not being raided.</p>
<p>A wash does not make a Sorrow Entity. It makes a person who can Fracture later because the grief has nowhere to sit. The Directorate files the Washers under crime, not SECC.</p>
</section>
<section class="wiki-section" id="not-keepers"><h2 class="section-title">Not the Keepers</h2>
<p>Keepers preserve. Washers delete. Weavers walk the Dream. Collectors monetize obligation. If a sentence on this URL mentions “historical legitimacy” or “the Archive’s secret exchange with Weavers,” it belonged on a Keepers article that has not been split yet — not here.</p>
<p>See <a href="the-underworld-and-wound-walkers.html">Underworld</a>, <a href="faction-technology.html">Faction technology</a>, and <a href="the-ucd-strike-force.html">UCD</a>.</p>
</section>
"""
    crumbs = '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Factions</a> <i>/</i> <span>Memory Washers</span>'
    cats = '<a href="index.html">Factions</a> | <a href="the-underworld-and-wound-walkers.html">Underworld</a> | <a href="the-ucd-strike-force.html">UCD</a>'
    doc = wrap(
        "The Memory Washers",
        "Fray memory-erasers of the Wash District. Not the Keepers. UCD Arc 2 target.",
        crumbs,
        "The Memory Washers",
        "FRAY · ZONE B+C",
        [
            ("overview", "Overview"),
            ("place", "Place in the underworld"),
            ("ucd", "UCD Arc 2"),
            ("not-keepers", "Not the Keepers"),
        ],
        body,
        cats,
    )
    (DOCS / "factions" / "the-memory-washers.html").write_text(doc, encoding="utf-8")
    print("rewrote the-memory-washers.html")


def patch_search_titles():
    sp = DOCS / "data" / "search.json"
    data = json.loads(sp.read_text(encoding="utf-8"))
    for e in data:
        if e.get("url") == "mechanics/the-four-ordeals.html":
            e["title"] = "The Four Watches"
            e["description"] = "First, Second, Third, and Tide Watch — Ordeal time axis."
            e["keywords"] = "Four Watches First Watch Tide Watch Ordeals Blue Black Pale Grey Purple"
        if e.get("url") == "factions/the-memory-washers.html":
            e["title"] = "The Memory Washers"
            e["description"] = "Fray memory-erasers. Not the Keepers."
            e["keywords"] = "Memory Washers Fray Wash District UCD Arc 2"
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    purge_satellites()
    strip_architects_crumb()
    rewrite_four_watches()
    rewrite_memory_washers()
    patch_search_titles()
    print("batch done")


if __name__ == "__main__":
    main()
