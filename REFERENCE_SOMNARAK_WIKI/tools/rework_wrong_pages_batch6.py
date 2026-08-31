#!/usr/bin/env python3
"""Resonances split; expand thin encyclopedia pages (300+ is a floor, not a cap)."""
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
    SEARCH.append({"url": rel, "title": title, "description": desc[:180], "keywords": kw, "type": "article"})


def resonances():
    body = """
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p><strong>Resonances</strong> (공명 — Gongmyeong) are not scanners and not M.A.W. Each of the seven civic factions has a way of touching Han that is history, philosophy, and cost. <em>“Every faction sings a different note. The city is the chorus.”</em></p>
<p>This page is the seven notes. The seven <em>laws</em> are <a href="the-seven-absolute-taboos.html">the Taboos</a>. Enforcement guilds are <a href="../factions/the-giltong-enforcers.html">Giltong</a> and <a href="../factions/the-judexhan.html">Judexhan</a>. The old wiki pasted Taboos + Resonances + Giltong onto this URL from <code>SOMNARAK_TABOO_RESONANCE.md</code>. That paste is gone.</p>
</section>
<section class="wiki-section" id="table"><h2 class="section-title">The seven</h2>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>Faction</th><th>Resonance</th><th>Does</th><th>Cost</th></tr></thead>
<tbody>
<tr><td><a href="../factions/the-high-council.html">Council</a></td><td>The Weight (무게)</td><td>Absorb and redistribute Han</td><td>Ages faster</td></tr>
<tr><td><a href="../factions/the-architects.html">Architects</a></td><td>The Shaping (조형)</td><td>Mold solidified Han into structure</td><td>Feel the grief in the wall</td></tr>
<tr><td><a href="../factions/the-collectors.html">Collectors</a></td><td>The Scales (저울)</td><td>Measure and extract karmic debt</td><td>Memory bleed — other people’s grief</td></tr>
<tr><td><a href="../factions/the-keepers.html">Keepers</a></td><td>The Archive (기록)</td><td>Store and retrieve memory as Echoes</td><td>Identity erosion</td></tr>
<tr><td><a href="../factions/the-wardens.html">Wardens</a></td><td>The Barrier (방벽)</td><td>Han-suppression fields; the Veil’s grain</td><td>Numbness</td></tr>
<tr><td><a href="../factions/the-weavers.html">Weavers</a></td><td>The Dream (꿈)</td><td>Enter and navigate Somnus</td><td>Dream addiction</td></tr>
<tr><td><a href="../factions/the-reverie-directorate.html">R.D.</a></td><td>The Extraction (추출)</td><td>Pull M.A.W. from living contained entities</td><td>Entity personality bleed</td></tr>
</tbody></table></div>
</section>
<section class="wiki-section" id="weight"><h2 class="section-title">Council — The Weight</h2>
<p>A Council member can draw Han from a person or a district by contact or proximity and bear it as pain, aging, fatigue. That is why membership is chosen by weight carried. Majin’s Ω-fusion is the amplified form: whole districts. This is why the Director looks the oldest. Tools that sit beside the Resonance: Sigh Recorder, Decision Scale — see <a href="../factions/the-high-council.html">Council</a>.</p>
</section>
<section class="wiki-section" id="shaping"><h2 class="section-title">Architects — The Shaping</h2>
<p>Touch and concentration reshape Han-crystal into wall, cell, tool. Complex shapes cost more skill. The Architect feels the sorrow in the material; that is the Mark — grey hair, dark veins, altered eyes. Shapers and above work at a distance and can shape living Han in a cell. Compass and trowel are the handheld version of the same note.</p>
</section>
<section class="wiki-section" id="scales"><h2 class="section-title">Collectors — The Scales</h2>
<p>Observation and touch weigh a person’s debt and pull it as Echoes into the civic system. Fragments of that debt stay in the Collector. Distance is occupational. <a href="../entities/se-014-the-debt-eater.html">SE-014 Debt Eater</a> is the entity some Collectors still treat as a tool — it eats debt and leaves the person hollow. Ledger and Extraction Glove are tech; the Scales is the body doing the same job.</p>
</section>
<section class="wiki-section" id="archive"><h2 class="section-title">Keepers — The Archive</h2>
<p>Touch and ritual pull a memory into an Echo or put one back. Restoration is imperfect. The more a Keeper stores, the less of themselves remains. Oldest Keepers remember the city and forget their names. The Whispering Index talks constantly. Comforting. Maddening. Not the same as a wash-rig.</p>
</section>
<section class="wiki-section" id="barrier"><h2 class="section-title">Wardens — The Barrier</h2>
<p>Training and baton project a field that lowers intensity, slows Fracture, damps entities. The civic Veil is thousands of those fields layered. If Wardens stop, the Veil fails. Cost: feeling itself. Veteran Wardens enforce a hush they can no longer hear.</p>
</section>
<section class="wiki-section" id="dream"><h2 class="section-title">Weavers — The Dream</h2>
<p>Trance plus mask crosses into Somnus, where feeling is object and memory is landscape. Pull objects, information, entities. The Dream shows you what you want. Return gets harder. Some Weavers live more down there than on the street. Layer map: <a href="../lore/the-dream-realm.html">Dream realm</a>.</p>
</section>
<section class="wiki-section" id="extraction"><h2 class="section-title">R.D. — The Extraction</h2>
<p>Resonance with a living contained entity externalizes its sorrow as weapon, suit, gift. Dead or uncontained donors do not yield. Staff take on the entity’s habit; extreme cases Fracture. Zyrak can also extract memories — a Collector leftover, not standard R.D. Resonance. SE-003 still has no extractable M.A.W.; a Resonance does not invent a personality where the Codex says none exists.</p>
</section>
<section class="wiki-section" id="together"><h2 class="section-title">How they stack</h2>
<p>Weight then Shaping: Council drinks, Architect builds from what remains. Scales then Archive: debt pulled, memory of the pulling stored. Barrier then Dream: hush the street, walk the sleep. Extraction feeds everyone else’s kit. Menders and Judexhan do not have a seventh-plus Resonance in the seven-note table; they have kit and implant. Frays steal the notes they cannot sing.</p>
</section>
"""
    put(
        "mechanics/taboo-resonance-mechanics.html",
        "Faction Resonances",
        "Seven civic ways of touching Han — Weight, Shaping, Scales, Archive, Barrier, Dream, Extraction.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Mechanics</a> <i>/</i> <span>Resonances</span>',
        "Faction Resonances",
        "MECHANICS · 공명",
        [
            ("overview", "Overview"),
            ("table", "The seven"),
            ("weight", "Weight"),
            ("shaping", "Shaping"),
            ("scales", "Scales"),
            ("archive", "Archive"),
            ("barrier", "Barrier"),
            ("dream", "Dream"),
            ("extraction", "Extraction"),
            ("together", "How they stack"),
        ],
        body,
        '<a href="../lore/the-seven-absolute-taboos.html">Taboos</a> | <a href="../factions/index.html">Factions</a> | <a href="index.html">Mechanics</a>',
        "Resonance Gongmyeong Weight Shaping Scales Archive Barrier Dream Extraction",
    )


def rd():
    body = """
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The <strong>Reverie Directorate</strong> (리버리 지부) is Somnarak’s containment authority, founded Year 4,202. Nine people carry the city’s sorrow. None of them chose this. The Council funds the R.D. and does not fully understand it. It is not a sixth Head and not a Wing.</p>
<p>This page is organization and facility. Cycle / Absolvohan / energy quotas live on <a href="../lore/the-cycle-and-absolvohan.html">the Cycle</a>. Codes: <a href="secc-classification-system.html">SECC</a> is classification only. Floors: <a href="../departments/index.html">departments</a>. Resonance: Extraction, on <a href="../mechanics/taboo-resonance-mechanics.html">Resonances</a>.</p>
</section>
<section class="wiki-section" id="facility"><h2 class="section-title">Facility</h2>
<p>The main site is <strong>beneath the Alpha Tree</strong> — Zone A deep, down the root. The same Han-crystal that is the six civic buildings above continues as walls, floors, ceilings. The R.D. is not one tower on a skyline. It is the Tree’s basement: the Hand of Change, eight floors, cells keyed to specimens, a Lament Well, a Mnemonic Generator, Dream Chambers staffed with Weavers, extraction rigs that only work on the living and contained.</p>
<p>Architects built it, including passages not on the public plan. Wardens provide security and get pulled out of breaches more often than after-action admits. Keepers feed research. Collectors want debt data and have tried to hack twice. Giltong have investigated three times and filed nothing they could keep. Menders contract to both R.D. and Architects. The Absolvohan stockpile is an R.D. secret the Council is not meant to have; Weavers have seen it in Dream anyway.</p>
</section>
<section class="wiki-section" id="cores"><h2 class="section-title">Nine Echo-Cores</h2>
<p>Five operational departments, two specialized posts, Director, Secretary. Each Core is a person whose sorrow shapes the floor.</p>
<ul>
<li><a href="../characters/the-director-majin.html">Director Majin</a> — Floor 1 Neutral Command. Weight, amplified.</li>
<li><a href="../characters/the-secretary-seiyon.html">Secretary Seiyon</a> — remembers; forbidden from acting. Taboo 2’s grey area walking.</li>
<li><a href="../characters/the-containment-lead-dekan.html">Containment Lead Dekan</a> — entities in cells, Zone B wound.</li>
<li><a href="../characters/the-extraction-lead-zyrak.html">Extraction Lead Zyrak</a> — Floor 3. M.A.W. and, uniquely, memories.</li>
<li><a href="../characters/the-research-lead-ayshuk.html">Research Lead Ayshuk</a> — Floor 4 Insight Forge. Observation ladder.</li>
<li><a href="../characters/the-border-lead-mellda.html">Border Lead Mellda</a> — Floor 5. Wilderness Tide, no extract from SE-003.</li>
<li><a href="../characters/the-archive-lead-marjuk.html">Archive Lead Marjuk</a> — Floor 6 Deep Vault under the Tree.</li>
<li><a href="../characters/the-outsider-ishall.html">Outsider Ishall</a> — Floor 7 Shadow Corps. An enemy incorporated.</li>
<li><a href="../characters/the-exile-xyan.html">Exile Xyan</a> — Floor 8 Gate Watch. Left, drawn back, watches the Gate.</li>
</ul>
<p>Cores are not assigned by the personnel office. Agents rotate; Cores are the floor until suppression or exile. See <a href="../departments/agent-assignment.html">assignment</a>.</p>
</section>
<section class="wiki-section" id="ops"><h2 class="section-title">Sister operations</h2>
<p>Present-age trio: this Directorate (contain), <a href="../factions/the-sed-corps.html">SED</a> (explore), <a href="../factions/the-ucd-strike-force.html">UCD</a> (underworld descent). Index: <a href="../factions/the-founding-corporations.html">three operations</a>. Employee ranks, Sorrow Rod, room-type taxonomy belong on <a href="../departments/facility-room-types.html">room types</a> and <a href="../mechanics/default-standard-equipment.html">standard issue</a> — not pasted back here as a second Directorate manual.</p>
</section>
"""
    put(
        "factions/the-reverie-directorate.html",
        "The Reverie Directorate",
        "R.D. under the Alpha Tree — nine Echo-Cores, Hand of Change, Extraction Resonance.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="../factions/index.html">Factions</a> <i>/</i> <span>Reverie Directorate</span>',
        "The Reverie Directorate",
        "FACTION · FACILITY 01 · YEAR 4,202",
        [("overview", "Overview"), ("facility", "Facility"), ("cores", "Nine Echo-Cores"), ("ops", "Sister operations")],
        body,
        '<a href="../factions/index.html">Factions</a> | <a href="../departments/index.html">Floors</a> | <a href="../lore/the-cycle-and-absolvohan.html">Cycle</a>',
        "Reverie Directorate Echo-Cores Majin Alpha Tree Hand of Change Extraction",
    )


def judexhan():
    body = """
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The <strong>Judexhan</strong> (유덱스한) are the Council’s elite field agents — judgment incarnate, not Taboo clerks. Wardens hold streets and the wall. Giltong hunt the Seven Taboos. Judexhan weigh karmic debt on the battlefield and cut through it. <em>“The city punishes the Taboo. We find the one who broke it. These are not the same job.”</em> That quote is Giltong’s. Judexhan’s version is shorter: they do not find. They judge.</p>
<p>They report to the Council’s enforcement seat called <strong>The Shadow</strong> (Fourth Head in that numbering), not to the full Council table and not as a sixth civic guild. Near-total autonomy. Their own agenda. They are not on the Five Heads list (Architect, Collector, Keeper, Warden, Weaver).</p>
</section>
<section class="wiki-section" id="vs"><h2 class="section-title">Not Giltong</h2>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>Axis</th><th>Giltong</th><th>Judexhan</th></tr></thead>
<tbody>
<tr><td>Domain</td><td>The Seven Taboos</td><td>General judgment, high-priority enforcement</td></tr>
<tr><td>Authority</td><td>Independent, full Council</td><td>The Shadow only</td></tr>
<tr><td>Method</td><td>Detect, contain, correct</td><td>Weigh, judge, cut</td></tr>
<tr><td>Tools</td><td>Taboo Scanner, Containment Bonds, Arbiter</td><td>Judgment Blade, forehead implant</td></tr>
<tr><td>Temperament</td><td>Investigators — patient, archival</td><td>Executioners — swift</td></tr>
</tbody></table></div>
<p>Rivalry from overlapping authority. Mutual respect: Judexhan have pulled Giltong out of critical ops; Giltong have covered Judexhan work that skirted a Taboo. The Arbiter is a <em>retired</em> Judexhan — implant out, memory partly restored — the only person who has stood on both sides. See <a href="../factions/the-giltong-enforcers.html">Giltong</a> and <a href="../lore/the-seven-absolute-taboos.html">Taboos</a>.</p>
</section>
<section class="wiki-section" id="tools"><h2 class="section-title">Blade and implant</h2>
<p><strong>Judgment Blade</strong> (심판의 칼): crystallized judgment. Cuts Veil, entity shield, sorrow armor. Hits the debt-heavy harder. Drinks sorrow and gets heavier. Rejects a wielder who still owes. The grain records every judgment.</p>
<p><strong>Han-crystal implant</strong>: forehead, visible, pulsing. Command net, speed, endurance, drinks target sorrow, suppresses the wielder’s feeling. The crystal counts. At capacity the Judexhan is retired — taken deep under the Alpha Tree. Source does not say what happens next. A Judexhan who hesitates is already past the implant’s purpose; one who enjoys the count is why the Arbiter exists. Citizens rarely know the word. They know the light, and they step aside.</p>
</section>
<section class="wiki-section" id="place"><h2 class="section-title">When they deploy</h2>
<p>When Wardens fall, Judexhan deploy. They have no Zone C spire. Resonance table does not give them an eighth note; implant is not Weight. Tools also listed on <a href="../factions/faction-technology.html">faction technology</a>.</p>
</section>
"""
    put(
        "factions/the-judexhan.html",
        "The Judexhan",
        "Council elite arbiters — Judgment Blade, implant, The Shadow, parallel to Giltong.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Factions</a> <i>/</i> <span>Judexhan</span>',
        "The Judexhan",
        "FACTION · COUNCIL ELITE · 유덱스한",
        [("overview", "Overview"), ("vs", "Not Giltong"), ("tools", "Blade and implant"), ("place", "When they deploy")],
        body,
        '<a href="index.html">Factions</a> | <a href="the-giltong-enforcers.html">Giltong</a> | <a href="the-high-council.html">Council</a>',
        "Judexhan Judgment Blade implant The Shadow Arbiter Giltong",
    )


def dream():
    body = """
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The <strong>Dream Realm</strong> (Somnus, 유몽계) is not a second city. It is a dimensional layer of unformed potential — memory, desire, fear, sorrow that has not crystallized into street. Sleep in Somnarak is not rest. You enter. The guild that dives it is <a href="../factions/the-weavers.html">the Weavers</a>; their Resonance is The Dream. Relics, SED “narrative function,” and the Weaver org-chart do not belong in this heading stack.</p>
<p><em>“The Dream is not a place. It is a state — of mind, of memory, of sorrow.”</em></p>
</section>
<section class="wiki-section" id="veil"><h2 class="section-title">The Dream Veil</h2>
<p>꿈의 베일 — aurora, not a wall. Thinner at the Spire of Dreams, Echo Gardens, Alpha Tree. Thinning by the century. Strong feeling makes it thinner; Dream-stuff leaks. Touch unprepared and it pulls you through. Citizens who see it call it the most beautiful thing they have seen, which is how it kills.</p>
</section>
<section class="wiki-section" id="layers"><h2 class="section-title">Five layers</h2>
<p><strong>Shallow (1).</strong> Nightly sleep: your house, your shift, muted blue-grey. Safe and not restful. You wake tired because the layer is made of sorrow.</p>
<p><strong>Memory (2).</strong> Not only yours — the city’s. An endless library of crystals, each a life-fragment, air of old tears. Keepers argue a Layer 2 pull is not an Archive Echo. They still trade research with Weavers.</p>
<p><strong>Sorrow (3).</strong> Compressed civic grief. Unprepared divers do not come back whole. Pieces of identity sit here and wait.</p>
<p><strong>Deep (4).</strong> Forgotten truths. Weaver domain. Critical.</p>
<p><strong>Core (5).</strong> The heart. Unexplored in source. Unknown danger is still danger.</p>
<p>Each Dreamer sees a different street. The layer does not care about your map.</p>
</section>
<section class="wiki-section" id="diving"><h2 class="section-title">Dream-diving</h2>
<p>Deliberate entry, not sleep. Training, Resonance Mask, a reason. The Loom sends or pulls. Risks: dissolution, addiction to the mask’s replay, leaving yourself on Layer 3. Time stretches. Minutes upstairs, hours down. Directorate Dream Chambers are Weaver-staffed. Wardens do not trust the work.</p>
</section>
<section class="wiki-section" id="spire"><h2 class="section-title">Spire of Dreams</h2>
<p>Building 4, south point of the Alpha Tree, Zone A. Glass that shows illusions. Head Weaver’s seat. Collapse scenario in source: a Dream entity takes the Spire and traps the guild — Dream bleeding into the street without a handler. That lives on the Weavers page. See <a href="../locations/zone-a-core-nexus.html">Zone A</a> and <a href="../mechanics/taboo-resonance-mechanics.html">Resonances</a>.</p>
</section>
"""
    put(
        "lore/the-dream-realm.html",
        "The Dream Realm",
        "Somnus — Veil, five layers, diving. Weaver Resonance, not the Weaver guild dump.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Lore</a> <i>/</i> <span>Dream Realm</span>',
        "The Dream Realm",
        "LORE · SOMNUS · VEIL",
        [("overview", "Overview"), ("veil", "Dream Veil"), ("layers", "Five layers"), ("diving", "Dream-diving"), ("spire", "Spire of Dreams")],
        body,
        '<a href="index.html">Lore</a> | <a href="../factions/the-weavers.html">Weavers</a> | <a href="../mechanics/taboo-resonance-mechanics.html">Resonances</a>',
        "Dream Realm Somnus Veil Shallow Memory Sorrow Deep Core Weavers",
    )


def strip_narrative():
    files = [
        DOCS / "locations" / "the-desolate.html",
        DOCS / "lore" / "named-fractures.html",
        DOCS / "lore" / "the-weeping-river.html",
        DOCS / "mechanics" / "han-relic-registry.html",
    ]
    for p in files:
        if not p.exists():
            print("missing", p)
            continue
        t = p.read_text(encoding="utf-8")
        t2, n = re.subn(
            r'<section[^>]*id="[^"]*narrative-function[^"]*"[^>]*>.*?</section>',
            "",
            t,
            flags=re.S,
        )
        t2 = re.sub(r'<li><a href="#[^"]*narrative-function[^"]*">[^<]*</a></li>\s*', "", t2)
        t2 = re.sub(
            r'<li><a href="#[^"]*">[^<]*Narrative Function[^<]*</a></li>\s*',
            "",
            t2,
        )
        p.write_text(t2, encoding="utf-8")
        print(f"stripped narrative-function from {p.name} n={n}")


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
    resonances()
    rd()
    judexhan()
    dream()
    strip_narrative()
    patch_search()
    print("batch6 done")


if __name__ == "__main__":
    main()
