#!/usr/bin/env python3
"""Unregistered SE hub labels, Judexhan/Menders, floor-dump splits."""
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


def words(html: str) -> int:
    m = re.search(r"<main[^>]*>(.*)</main>", html, re.S)
    body = m.group(1) if m else html
    return len(re.findall(r"[A-Za-z0-9']+", re.sub(r"<[^>]+>", " ", body)))


SEARCH = []


def put(rel, title, desc, crumbs, h1, eyebrow, toc, body, cats, kw):
    doc = wrap(title, desc, crumbs, h1, eyebrow, toc, body, cats)
    (DOCS / rel).write_text(doc, encoding="utf-8")
    w = words(doc)
    print(f"wrote {rel} ({w}w)")
    if w < 300:
        print("  WARN under 300")
    SEARCH.append({"url": rel, "title": title, "description": desc[:180], "keywords": kw, "type": "article"})


def patch_list():
    p = DOCS / "entities" / "list.html"
    t = p.read_text(encoding="utf-8")
    repls = [
        (
            """<tr>
            <td><a href="se-004-the-rust-bleeding-sentry.html"><b>SE-004</b><br><code>C-IIIγ-004 [VS]</code></a></td>
            <td class="el-portrait"><a href="se-004-the-rust-bleeding-sentry.html"><img src="../assets/art/entities/se-004-profile.svg" alt="The Rust-Bleeding Sentry"></a></td>
            <td><a href="se-004-the-rust-bleeding-sentry.html"><b>The Rust-Bleeding Sentry</b></a><br><i>녹을 흘리는 보초</i></td>
            <td><span class="secc-pill secc-major">γ Major</span></td>
            <td class="el-han"><img src="../assets/icons/damage_void.svg" alt=""><span style="color:#e7edf2">Void</span></td>
            <td>Normal / Subject</td>
            <td><a href="../maw/maw-w-004-01-rust-halberd.html">Rust Halberd</a></td>
          </tr>""",
            """<tr>
            <td><a href="se-004-the-rust-bleeding-sentry.html"><b>SE-004</b><br><code>UNREGISTERED</code></a></td>
            <td class="el-portrait"><a href="se-004-the-rust-bleeding-sentry.html"><img src="../assets/art/entities/se-004-profile.svg" alt="SE-004 unregistered"></a></td>
            <td><a href="se-004-the-rust-bleeding-sentry.html"><b>SE-004 (retraction)</b></a><br><i>not in Codex</i></td>
            <td><span class="secc-pill">unregistered</span></td>
            <td>—</td>
            <td>—</td>
            <td><a href="../maw/maw-w-004-01-rust-halberd.html">no extract</a></td>
          </tr>""",
        ),
        (
            """<tr>
            <td><a href="se-006-the-siphon-leech.html"><b>SE-006</b><br><code>C-IIβ-006 [VO]</code></a></td>
            <td class="el-portrait"><a href="se-006-the-siphon-leech.html"><img src="../assets/art/entities/se-006-profile.svg" alt="The Siphon Leech"></a></td>
            <td><a href="se-006-the-siphon-leech.html"><b>The Siphon Leech</b></a><br><i>착취하는 거머리</i></td>
            <td><span class="secc-pill secc-mod">β Moderate</span></td>
            <td class="el-han"><img src="../assets/icons/damage_void.svg" alt=""><span style="color:#e7edf2">Void</span></td>
            <td>Normal / Object</td>
            <td><a href="../maw/maw-w-006-01-siphon-cannula.html">Siphon Cannula</a></td>
          </tr>""",
            """<tr>
            <td><a href="se-006-the-siphon-leech.html"><b>SE-006</b><br><code>UNREGISTERED</code></a></td>
            <td class="el-portrait"><a href="se-006-the-siphon-leech.html"><img src="../assets/art/entities/se-006-profile.svg" alt="SE-006 unregistered"></a></td>
            <td><a href="se-006-the-siphon-leech.html"><b>SE-006 (retraction)</b></a><br><i>not in Codex</i></td>
            <td><span class="secc-pill">unregistered</span></td>
            <td>—</td>
            <td>—</td>
            <td><a href="../maw/maw-w-006-01-siphon-cannula.html">no extract</a></td>
          </tr>""",
        ),
        (
            """<tr>
            <td><a href="se-008-the-iron-maiden-of-regret.html"><b>SE-008</b><br><code>C-IVδ-008 [VS]</code></a></td>
            <td class="el-portrait"><a href="se-008-the-iron-maiden-of-regret.html"><img src="../assets/art/entities/se-008-profile.svg" alt="The Iron Maiden of Regret"></a></td>
            <td><a href="se-008-the-iron-maiden-of-regret.html"><b>The Iron Maiden of Regret</b></a><br><i>후회의 철처녀</i></td>
            <td><span class="secc-pill secc-crit">δ Critical</span></td>
            <td class="el-han"><img src="../assets/icons/damage_void.svg" alt=""><span style="color:#e7edf2">Void</span></td>
            <td>Normal / Subject</td>
            <td><a href="../maw/maw-w-008-01-thorn-impaler.html">Thorn Impaler</a></td>
          </tr>""",
            """<tr>
            <td><a href="se-008-the-iron-maiden-of-regret.html"><b>SE-008</b><br><code>UNREGISTERED</code></a></td>
            <td class="el-portrait"><a href="se-008-the-iron-maiden-of-regret.html"><img src="../assets/art/entities/se-008-profile.svg" alt="SE-008 unregistered"></a></td>
            <td><a href="se-008-the-iron-maiden-of-regret.html"><b>SE-008 (retraction)</b></a><br><i>not in Codex</i></td>
            <td><span class="secc-pill">unregistered</span></td>
            <td>—</td>
            <td>—</td>
            <td><a href="../maw/maw-w-008-01-thorn-impaler.html">no extract</a></td>
          </tr>""",
        ),
    ]
    for old, new in repls:
        if old not in t:
            print("WARN list row not exact match")
        else:
            t = t.replace(old, new)
    t = t.replace(
        "The public wiki currently publishes <strong>13 of 288</strong> catalogued Sorrow Entities (<strong>4.5%</strong>).",
        "The public wiki currently publishes <strong>10 Codex-backed dossiers</strong> plus <strong>3 unregistered slots</strong> (004 / 006 / 008 retractions) of 288 catalogued Sorrow Entities.",
    )
    t = t.replace(
        "<small>13 / 288 published · remaining registers not yet added</small>",
        "<small>10 sourced + 3 retractions / 288 · remaining registers not yet added</small>",
    )
    p.write_text(t, encoding="utf-8")
    print("patched entities/list.html")


def patch_entity_index_tiles():
    p = DOCS / "entities" / "index.html"
    t = p.read_text(encoding="utf-8")
    t = t.replace(
        """          <a class="entity-codex-tile" href="se-004-the-rust-bleeding-sentry.html" style="--tile:#e7edf2">
            <span>SE-004 · γ MAJOR</span>
            <img src="../assets/art/entities/se-004-icon.svg" alt="">
            <b>The Rust-Bleeding Sentry</b>
            <small>C-IIIγ-004 [VS] · Void Subject</small>
          </a>""",
        """          <a class="entity-codex-tile" href="se-004-the-rust-bleeding-sentry.html" style="--tile:#e7edf2">
            <span>SE-004 · UNREGISTERED</span>
            <img src="../assets/art/entities/se-004-icon.svg" alt="">
            <b>SE-004 (retraction)</b>
            <small>Not in Codex_Set Registry</small>
          </a>""",
    )
    # 006 and 008 tiles - find by href
    t = re.sub(
        r'(<a class="entity-codex-tile" href="se-006-the-siphon-leech.html"[^>]*>)[\s\S]*?(</a>)',
        r"""\1
            <span>SE-006 · UNREGISTERED</span>
            <img src="../assets/art/entities/se-006-icon.svg" alt="">
            <b>SE-006 (retraction)</b>
            <small>Not in Codex_Set Registry</small>
          \2""",
        t,
        count=1,
    )
    t = re.sub(
        r'(<a class="entity-codex-tile" href="se-008-the-iron-maiden-of-regret.html"[^>]*>)[\s\S]*?(</a>)',
        r"""\1
            <span>SE-008 · UNREGISTERED</span>
            <img src="../assets/art/entities/se-008-icon.svg" alt="">
            <b>SE-008 (retraction)</b>
            <small>Not in Codex_Set Registry</small>
          \2""",
        t,
        count=1,
    )
    p.write_text(t, encoding="utf-8")
    print("patched entities/index.html tiles")


def patch_maw_index():
    p = DOCS / "maw" / "index.html"
    t = p.read_text(encoding="utf-8")
    t = t.replace("SE-004 The Rust-Bleeding Sentry", "SE-004 unregistered")
    t = t.replace("SE-006 The Siphon Leech", "SE-006 unregistered")
    t = t.replace("SE-008 The Iron Maiden of Regret", "SE-008 unregistered")
    p.write_text(t, encoding="utf-8")
    print("patched maw/index.html donor labels")


def strip_section(path: pathlib.Path, section_id: str, toc_href: str | None = None):
    t = path.read_text(encoding="utf-8")
    t2, n = re.subn(
        rf'<section class="wiki-section" id="{section_id}">.*?</section>',
        "",
        t,
        count=1,
        flags=re.S,
    )
    if toc_href:
        t2 = re.sub(rf'<li><a href="#{toc_href}">[^<]*</a></li>\s*', "", t2)
        t2 = re.sub(rf'<li><a href="#{section_id}">[^<]*</a></li>\s*', "", t2)
    path.write_text(t2, encoding="utf-8")
    print(f"stripped #{section_id} from {path.name} (n={n})")


def judexhan():
    body = """
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The <strong>Judexhan</strong> are the Council’s elite agents — not a sixth Head, not the Wardens, not the Giltong. Wardens hold streets and the wall. Giltong hunt Taboo. Judexhan judge. They are the implant-bearing operators who cut through Veil and entity shield when a debt or a decree has to be ended, not patrolled.</p>
<p>The Giltong Arbiter is a <em>retired</em> Judexhan: implant removed, memory partly restored, the only person who has stood on both the enforcement side and the Taboo side. Parallel, not identical. See <a href="the-giltong-enforcers.html">Giltong</a> and <a href="../lore/the-seven-absolute-taboos.html">the Seven Taboos</a>.</p>
</section>
<section class="wiki-section" id="tools"><h2 class="section-title">Blade and implant</h2>
<p><strong>Judgment Blade</strong> (심판의 칼): crystallized judgment, dark, heavy, faint Han-light. It cuts Han-defenses — Veil, entity shield, sorrow armor. It hits harder on heavy karmic debt. It drinks sorrow on contact and gets heavier. Anyone with unresolved debt cannot wield it; the blade rejects them. The crystalline grain records every judgment for anyone who knows how to read it.</p>
<p><strong>Han-crystal implant</strong> (한 크리스탈 이식): a forehead crystal, visible, pulsing with stored sorrow. It ties the Judexhan to the Council command net, raises speed and endurance, drinks target sorrow into the body, and suppresses the wielder’s own feeling so hesitation does not happen. The crystal <em>counts</em>. At capacity the Judexhan is “retired” — taken deep under the Alpha Tree. Source does not say what happens next.</p>
</section>
<section class="wiki-section" id="place"><h2 class="section-title">Place in the web</h2>
<p>When Wardens fall, the Judexhan deploy. They are not a citizen-facing guild with a Zone C spire. They are the Council’s sharp edge. They do not sit on the Five Heads list. Do not file them as a Wing or as Fixers. Tools also live on <a href="faction-technology.html">faction technology</a>.</p>
</section>
"""
    put(
        "factions/the-judexhan.html",
        "The Judexhan",
        "Council elite arbiters — Judgment Blade, forehead implant, retirement under the Alpha Tree.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Factions</a> <i>/</i> <span>Judexhan</span>',
        "The Judexhan",
        "FACTION · COUNCIL ELITE",
        [("overview", "Overview"), ("tools", "Blade and implant"), ("place", "Place in the web")],
        body,
        '<a href="index.html">Factions</a> | <a href="the-giltong-enforcers.html">Giltong</a> | <a href="the-high-council.html">Council</a>',
        "Judexhan Judgment Blade Han-crystal implant Arbiter Council elite",
    )


def menders():
    body = """
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p><strong>Menders</strong> (수선자 — Suseonja) are independent operators, not a Council Head. They work the Raw — fixing, containing, protecting where guilds do not reach. They report to both the <a href="the-architects.html">Architects</a> and the <a href="the-reverie-directorate.html">Directorate</a>. That split loyalty is named in source, not hinted.</p>
<p>Ranks run 7 (Novice) to 1 (Grandmaster). Five legendary Marks: Grey Veil, Crimson Thread, Pale Witness, Black Tide, Golden Echo. Organizations: the Mendery, Raw Collective, Threshold Walkers, Veil Watchers. Veil Watchers also feed Giltong when a Taboo signature shows on a repair.</p>
</section>
<section class="wiki-section" id="tools"><h2 class="section-title">Kit and rod</h2>
<p><strong>Mender’s Kit</strong> (수선자 도구함): leather-and-crystal case — trowels, probes, gauges, sealant, Echo reserves, a small Sorrow Gauge. Tools answer the user’s feeling. Each kit personalizes until it is as distinct as a fingerprint.</p>
<p><strong>Repair Rod</strong> (수리 막대): flexible Han-crystal, warm. It vibrates at cracks, fills them with the Mender’s own sorrow, reinforces weak spans, and can be a weapon in an emergency. It remembers every repair. A veteran can walk the city by the rod’s map of failures.</p>
</section>
<section class="wiki-section" id="place"><h2 class="section-title">Place</h2>
<p>Alliance with the R.D. is field operations — unofficial contractors. Alliance with Architects is the same people on construction sites. Frays sometimes hire Menders, sometimes oppose them. Citizens pay Echoes for repair. Giltong treat them as witnesses, not hunters. See <a href="faction-technology.html">faction technology</a> and <a href="the-underworld-and-wound-walkers.html">the Raw / underworld</a>.</p>
</section>
"""
    put(
        "factions/the-menders.html",
        "The Menders",
        "Independent Raw operators — kit, repair rod, dual report to Architects and R.D.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Factions</a> <i>/</i> <span>Menders</span>',
        "The Menders",
        "INDEPENDENT · RAW",
        [("overview", "Overview"), ("tools", "Kit and rod"), ("place", "Place")],
        body,
        '<a href="index.html">Factions</a> | <a href="the-architects.html">Architects</a> | <a href="the-reverie-directorate.html">Directorate</a>',
        "Menders Suseonja Repair Rod Mendery Raw Collective Veil Watchers",
    )


def assignment():
    body = """
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p><strong>Agent assignment</strong> is facility-wide, not a Floor 1 protocol. The old Neutral Command article pasted the whole personnel-placement chapter under Majin’s floor. LC analog: employees are listed on a personnel page, not only on Control Team. This URL is that split.</p>
<p>Quote in source: <em>“The right person in the right room can contain a monster. The wrong person in the wrong room becomes one.”</em></p>
</section>
<section class="wiki-section" id="process"><h2 class="section-title">Process</h2>
<p>New personnel are tested on Resilience, Clarity, Composure, and Resolve. Scores gate which floors they may hold. Transfers exist and need approval. Inside a floor, room assignment follows the entity in the cell — Work Type preference, Han element, and the agent’s worst stat. Rotation is scheduled so no one lives on Border Watch or Extraction until they Fracture.</p>
<p>Floor 1 (Majin) wants composure under silence. Floor 5 (Mellda) wants resolve against Weight. Floor 3 (Zyrak) wants people who can finish an extract without keeping the donor’s habit. Do not read this as “Floor 1 runs HR.” Neutral Command signs the paper. Insight Forge files the observation that made the paper necessary.</p>
</section>
<section class="wiki-section" id="see"><h2 class="section-title">See also</h2>
<p><a href="floor-1-neutral-command.html">Floor 1</a> is command rooms, not this chapter. <a href="facility-upgrades.html">Facility upgrades</a> is growth over time. <a href="../mechanics/panic-states-and-corrosion.html">Panic</a> is what happens when assignment was wrong. <a href="../factions/the-reverie-directorate.html">Directorate</a> is the org chart.</p>
</section>
"""
    put(
        "departments/agent-assignment.html",
        "Agent Assignment",
        "Facility-wide personnel placement by attribute — not a Floor 1 dump.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Departments</a> <i>/</i> <span>Agent Assignment</span>',
        "Agent Assignment",
        "FACILITY · PERSONNEL",
        [("overview", "Overview"), ("process", "Process"), ("see", "See also")],
        body,
        '<a href="index.html">Departments</a> | <a href="floor-1-neutral-command.html">Floor 1</a> | <a href="../factions/the-reverie-directorate.html">R.D.</a>',
        "Agent Assignment personnel Resilience Clarity Composure Resolve floors",
    )


def upgrades():
    body = """
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p><strong>Facility upgrades</strong> are how the Hand of Change grows across cycles — cells, gauges, corridors, Mnemonic Generator load. This is not Floor 1’s private construction budget. Architects build it. Extraction pays for it in Han-flux. Neutral Command approves it. The old wiki dumped the growth chapter onto Majin’s floor because that is where the signature sits.</p>
</section>
<section class="wiki-section" id="kinds"><h2 class="section-title">Kinds</h2>
<p>Source groups upgrades as containment (better cells, faster lock), observation (gauges, cameras, Insight tools), welfare (SP recovery rooms — so assignment mistakes kill slower), and expansion (new rooms on a floor, not a ninth floor). Each upgrade has a Han-flux cost and a downtime. You do not upgrade Border Watch during a Tide Watch.</p>
<p>Architects are the only Head that wants the building to change. The Council resists because uncertainty makes Han. That fight is civic. The facility version is this page: which valve, which cell, which cycle.</p>
</section>
<section class="wiki-section" id="see"><h2 class="section-title">See also</h2>
<p><a href="../factions/the-architects.html">Architects</a>, <a href="agent-assignment.html">assignment</a>, <a href="facility-meltdown-procedures.html">meltdown</a>, <a href="../atlas/hand-of-change-map.html">Hand of Change map</a>. Do not paste the whole construction guild onto this URL.</p>
</section>
"""
    put(
        "departments/facility-upgrades.html",
        "Facility Upgrades",
        "Hand of Change growth — containment, observation, welfare, expansion. Not a Floor 1 chapter.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Departments</a> <i>/</i> <span>Facility Upgrades</span>',
        "Facility Upgrades",
        "FACILITY · GROWTH",
        [("overview", "Overview"), ("kinds", "Kinds"), ("see", "See also")],
        body,
        '<a href="index.html">Departments</a> | <a href="../factions/the-architects.html">Architects</a> | <a href="floor-1-neutral-command.html">Floor 1</a>',
        "Facility upgrades Hand of Change cells gauges Architects",
    )


def research():
    body = """
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The R.D. <strong>research / observation</strong> ladder is how a Sorrow Entity goes from a code on a door to a profile you can work. It is not Floor 4’s private manual. Insight Forge (Ayshuk) files it. Every floor uses it. The old wiki pasted “Research System — Entity Observation &amp; Knowledge” under Floor 4 because that is the lab. LC analog: Abnormality observation lives on the Abnormality and on Info Team, not only on one department dump.</p>
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
<p>M.A.W. extraction is a separate risk event, not a level-up reward. SE-003 never leaves Level 5 border monitoring and still has <strong>no extractable M.A.W.</strong> Unregistered 004 / 006 / 008 have no observation ladder because they have no source card.</p>
</section>
<section class="wiki-section" id="see"><h2 class="section-title">See also</h2>
<p><a href="floor-4-insight-forge.html">Floor 4</a> is the lab. <a href="../mechanics/secc-classification-system.html">SECC</a> is the code. <a href="../mechanics/the-four-work-types.html">Work Types</a> are how you climb the ladder. <a href="../maw/maw-crafting-and-extraction.html">Extraction</a> is the other event.</p>
</section>
"""
    put(
        "departments/research-observation.html",
        "Research and Observation",
        "R.D. observation levels 0–4. Facility-wide, not a Floor 4 dump.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Departments</a> <i>/</i> <span>Research and Observation</span>',
        "Research and Observation",
        "FACILITY · INSIGHT",
        [("overview", "Overview"), ("levels", "Observation levels"), ("see", "See also")],
        body,
        '<a href="floor-4-insight-forge.html">Floor 4</a> | <a href="../mechanics/secc-classification-system.html">SECC</a> | <a href="../mechanics/the-four-work-types.html">Work Types</a>',
        "Observation Level research Insight Forge Work Types SECC",
    )


def patch_floors_pointers():
    f1 = DOCS / "departments" / "floor-1-neutral-command.html"
    t = f1.read_text(encoding="utf-8")
    pointer = (
        '<p>Personnel placement and facility growth are not Floor 1 chapters. See '
        '<a href="agent-assignment.html">agent assignment</a> and '
        '<a href="facility-upgrades.html">facility upgrades</a>.</p>'
    )
    if "agent-assignment.html" not in t:
        t = t.replace(
            '<section class="wiki-section" id="operational-protocols">',
            '<section class="wiki-section" id="operational-protocols">' + pointer,
            1,
        )
        f1.write_text(t, encoding="utf-8")
        print("pointer on floor-1")
    f4 = DOCS / "departments" / "floor-4-insight-forge.html"
    t = f4.read_text(encoding="utf-8")
    pointer = (
        '<p>Observation levels are facility-wide. See '
        '<a href="research-observation.html">research and observation</a>.</p>'
    )
    if "research-observation.html" not in t:
        t = t.replace(
            '<section class="wiki-section" id="operational-protocols">',
            '<section class="wiki-section" id="operational-protocols">' + pointer,
            1,
        )
        f4.write_text(t, encoding="utf-8")
        print("pointer on floor-4")


def patch_faction_index():
    p = DOCS / "factions" / "index.html"
    t = p.read_text(encoding="utf-8")
    if "the-judexhan.html" in t:
        print("faction index already has judexhan")
        return
    needle = '<a href="the-giltong-enforcers.html" class="jump-btn">VIEW ENFORCER CODE →</a></div>'
    extra = needle + """
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/icon_faction_giltong.svg" alt="Judexhan" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">COUNCIL ELITE</span></div></div><h3 class="entity-card-name">THE JUDEXHAN</h3><p class="entity-card-desc">Council arbiters — Judgment Blade, forehead implant. Not Giltong, not Wardens.</p><a href="the-judexhan.html" class="jump-btn">VIEW ARBITER DOSSIER →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/icon_faction_architects.svg" alt="Menders" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">INDEPENDENT</span></div></div><h3 class="entity-card-name">THE MENDERS</h3><p class="entity-card-desc">Raw operators — kit and repair rod. Dual report to Architects and R.D.</p><a href="the-menders.html" class="jump-btn">VIEW MENDER DOSSIER →</a></div>"""
    if needle not in t:
        print("WARN giltong card end not found")
        return
    p.write_text(t.replace(needle, extra, 1), encoding="utf-8")
    print("patched factions index Judexhan+Menders")


def patch_search():
    sp = DOCS / "data" / "search.json"
    data = json.loads(sp.read_text(encoding="utf-8"))
    by = {e.get("url"): e for e in data}
    for e in SEARCH:
        if e["url"] in by:
            by[e["url"]].update({k: e[k] for k in ("title", "description", "keywords")})
        else:
            data.append(e)
    # list keywords
    for e in data:
        if e.get("url") == "entities/list.html":
            e["description"] = "Published slice: 10 Codex-backed + 3 unregistered slots of ~288."
        if e.get("url") in (
            "entities/se-004-the-rust-bleeding-sentry.html",
            "entities/se-006-the-siphon-leech.html",
            "entities/se-008-the-iron-maiden-of-regret.html",
        ):
            e["keywords"] = (e.get("keywords") or "") + " unregistered retraction"
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("search", len(data))


def main():
    patch_list()
    patch_entity_index_tiles()
    patch_maw_index()
    strip_section(
        DOCS / "departments" / "floor-1-neutral-command.html",
        "agent-assignment",
        "agent-assignment",
    )
    strip_section(
        DOCS / "departments" / "floor-1-neutral-command.html",
        "facility-upgrades",
        "facility-upgrades",
    )
    strip_section(
        DOCS / "departments" / "floor-4-insight-forge.html",
        "research-system",
        "research-system",
    )
    judexhan()
    menders()
    assignment()
    upgrades()
    research()
    patch_floors_pointers()
    patch_faction_index()
    patch_search()
    print("batch4 done")


if __name__ == "__main__":
    main()
