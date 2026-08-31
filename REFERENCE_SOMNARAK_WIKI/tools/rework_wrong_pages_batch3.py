#!/usr/bin/env python3
"""Keepers article, Dream/RD dump splits, unregistered SE-004/006/008."""
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
    text = re.sub(r"<[^>]+>", " ", body)
    return len(re.findall(r"[A-Za-z0-9']+", text))


SEARCH_UPDATES = []


def put(rel, title, desc, crumbs, h1, eyebrow, toc, body, cats, kw):
    doc = wrap(title, desc, crumbs, h1, eyebrow, toc, body, cats)
    (DOCS / rel).write_text(doc, encoding="utf-8")
    w = words(doc)
    print(f"wrote {rel} ({w}w)")
    if w < 300:
        print("  WARN under 300")
    SEARCH_UPDATES.append(
        {"url": rel, "title": title, "description": desc[:180], "keywords": kw, "type": "article"}
    )


def keepers():
    body = """
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The <strong>Keepers</strong> (기록관 — Girokgwan) are Somnarak’s memory guild. Power is information: they run the Grand Archive (Building 2, Zone A), hold Echo vaults, and decide which past is still speakable. Head Keeper title is 기록장 (Girokjang), a Council seat. Philosophy: <em>“We hold what would otherwise be lost. This is not power — it is responsibility.”</em></p>
<p>They are not <a href="the-memory-washers.html">Memory Washers</a>. Washers erase. Keepers store. They are not <a href="the-weavers.html">Weavers</a>. Weavers walk Somnus; Keepers walk shelves — though some shelves extend into Dream-space. The old wiki had no Keepers article, so Keeper lore was pasted onto Washers. That paste is gone.</p>
</section>
<section class="wiki-section" id="work"><h2 class="section-title">Work and structure</h2>
<p>Preserve history (records, memories, artifacts). Maintain Echo vaults. Research, translation, verification. Memory transactions — legal extraction, storage, imperfect restoration. Line: Head Keeper → Senior Archivists → Archivists → Scribes → apprentices. Beside the line: Memory Division, Vault Guard, Verification Bureau.</p>
<p>The Grand Archive is the second-largest building in Zone A, northeast of the Tree. Oldest records sit in the lowest vaults. The building answers to feeling: walk in angry and the Index will not help you. Deep vaults hold Cheongula causation — the truth that could unseat the Council. Keepers have those records and choose not to release them. That is the dilemma: preserve history, or control it?</p>
</section>
<section class="wiki-section" id="tools"><h2 class="section-title">Tools</h2>
<p><strong>Memory Lens</strong> (기록 렌즈): a monocle of crystallized memory. An Echo near the lens plays as sight, sound, and feeling. Compare two memories and contradictions light. Look too often and the lens starts mixing the Keeper’s own past into the playback.</p>
<p><strong>Whispering Index</strong> (속삭임 색인): not one device. Han-crystal threads through the Archive. Touch a thread, ask, and it answers in whispers and riddles. Some Keepers say it is alive. Memory Fray has a copy of the index; the Keepers do not know.</p>
<p>Related, not the same building: the Memory Archive under the Tree is a hungry Place that consumes visitors as stories. Grand Archive is the guild’s public face. See <a href="faction-technology.html">faction technology</a>.</p>
</section>
<section class="wiki-section" id="relations"><h2 class="section-title">Relations</h2>
<p>Council depends on Keepers for legitimacy. Architects clash over demolition of historic sites. Collectors trade memories; Keepers recover stolen Echoes and keep them. Wardens are mostly ignored; Warden misconduct sits filed and forgotten. Weavers: rivalry on the surface, secret exchange underneath. R.D. gets research support and Cheongula-like event records. Citizens trust Keepers with memory they thought lost.</p>
<p>If the Keepers fall — Han-fire in the Grand Archive — the Before-Time fragments die, the Maw’s secret dies, and the city has to ask whether an unremembered event happened. Weavers would try the Dream. The Directorate would keep what it already copied. Oral tradition would have to do the rest.</p>
</section>
"""
    put(
        "factions/the-keepers.html",
        "The Keepers",
        "Girokgwan memory guild — Grand Archive, Memory Lens, Whispering Index. Not the Washers.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Factions</a> <i>/</i> <span>The Keepers</span>',
        "The Keepers",
        "FACTION · ZONE A · GRAND ARCHIVE",
        [
            ("overview", "Overview"),
            ("work", "Work and structure"),
            ("tools", "Tools"),
            ("relations", "Relations"),
        ],
        body,
        '<a href="index.html">Factions</a> | <a href="the-high-council.html">Council</a> | <a href="the-memory-washers.html">Washers</a>',
        "Keepers Girokgwan Girokjang Grand Archive Memory Lens Whispering Index Echo vaults",
    )


def dream():
    body = """
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The <strong>Dream Realm</strong> (Somnus, 유몽계) is not a second city stacked on the first. It is a dimensional layer of unformed potential — memory, desire, fear, sorrow that has not crystallized into street. The city is the body. The Dream is the shadow. Sleep in Somnarak is not rest. You enter.</p>
<p>This page is the realm. The guild that dives it is <a href="../factions/the-weavers.html">the Weavers</a>. Relics and SED “narrative function” chapters from the source file do not belong in this heading stack.</p>
</section>
<section class="wiki-section" id="veil"><h2 class="section-title">The Dream Veil</h2>
<p>The Dream Veil (꿈의 베일) is a shimmering barrier, aurora-colored, not a wall. Thinner at the Spire of Dreams, the Echo Gardens, and the Alpha Tree. It is thinning by century. Strong feeling makes it thinner still; Dream-stuff leaks. Touching it unprepared can pull a person through. Citizens who see it call it the most beautiful thing they have seen, which is how it kills.</p>
</section>
<section class="wiki-section" id="layers"><h2 class="section-title">Five layers</h2>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>Layer</th><th>Name</th><th>What it is</th><th>Danger</th></tr></thead>
<tbody>
<tr><td>1</td><td>Shallow Dream</td><td>Nightly sleep: familiar rooms, muted blue-grey, no rest</td><td>Low</td></tr>
<tr><td>2</td><td>Memory Dream</td><td>City memories as an endless crystal library; air of old tears</td><td>Medium</td></tr>
<tr><td>3</td><td>Sorrow Dream</td><td>Compressed civic grief. Unprepared divers do not come back whole</td><td>High</td></tr>
<tr><td>4</td><td>Deep Dream</td><td>Forgotten truths. Weaver domain</td><td>Critical</td></tr>
<tr><td>5</td><td>Core Dream</td><td>The heart. Unexplored in source</td><td>Unknown</td></tr>
</tbody></table></div>
<p>Each Dreamer sees a different street. The layer does not care about your map.</p>
</section>
<section class="wiki-section" id="diving"><h2 class="section-title">Dream-diving</h2>
<p>A deliberate entry, not sleep. Training, a <a href="../factions/the-weavers.html">Resonance Mask</a>, and a reason. The Loom can send or pull. Risks: dissolution of identity, addiction to the mask’s replay, leaving a piece of yourself on Layer 3. Time stretches. Minutes upstairs can be hours down.</p>
<p>The Directorate keeps Dream Chambers. Weavers staff them. Wardens do not trust the work. Keepers argue that a memory pulled from Layer 2 is not the same as an Archive Echo — and then they trade research anyway.</p>
</section>
<section class="wiki-section" id="spire"><h2 class="section-title">Spire of Dreams</h2>
<p>Building 4, south point of the Alpha Tree, Zone A. Glass that shows illusions. Head Weaver’s seat. If the Weavers fall, source names a Dream entity taking the Spire and trapping the guild inside — Dream bleeding into the street without a handler. That collapse scenario lives on the guild page, not as a second Weaver article here.</p>
<p>See <a href="../locations/zone-a-core-nexus.html">Zone A</a>, <a href="../factions/the-weavers.html">Weavers</a>, <a href="../factions/the-keepers.html">Keepers</a>.</p>
</section>
"""
    put(
        "lore/the-dream-realm.html",
        "The Dream Realm",
        "Somnus — Dream Veil, five layers, diving. Weaver guild content lives on the Weavers page.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Lore</a> <i>/</i> <span>Dream Realm</span>',
        "The Dream Realm",
        "LORE · SOMNUS · VEIL",
        [
            ("overview", "Overview"),
            ("veil", "The Dream Veil"),
            ("layers", "Five layers"),
            ("diving", "Dream-diving"),
            ("spire", "Spire of Dreams"),
        ],
        body,
        '<a href="index.html">Lore</a> | <a href="../factions/the-weavers.html">Weavers</a> | <a href="../locations/zone-a-core-nexus.html">Zone A</a>',
        "Dream Realm Somnus Dream Veil Shallow Memory Sorrow Deep Core Dream-diving Spire",
    )


def rd():
    body = """
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The <strong>Reverie Directorate</strong> (리버리 지부) is Somnarak’s containment authority, founded Year 4,202. It studies Sorrow Entities, extracts M.A.W., and runs Facility 01 — the Hand of Change — under Zone A. The Council funds it and does not fully understand it. It is not a sixth Head. It is not a Wing.</p>
<p>This page is the organization. It is not a paste of Absolvohan, the 1,778 Cycles, energy quotas, or every Echo-Core’s embodiment register. Cycle text: <a href="../lore/the-cycle-and-absolvohan.html">the Cycle</a>. Classification codes: <a href="../mechanics/secc-classification-system.html">SECC</a>. Floors: <a href="../departments/index.html">departments</a>.</p>
</section>
<section class="wiki-section" id="cores"><h2 class="section-title">Nine Echo-Cores</h2>
<p>Five operational departments, two specialized posts, Director, Secretary. Each Core is a person whose sorrow shapes the floor.</p>
<ul>
<li><a href="../characters/the-director-majin.html">Director Majin</a> — Floor 1 Neutral Command. Supreme authority.</li>
<li><a href="../characters/the-secretary-seiyon.html">Secretary Seiyon</a> — remembers; forbidden from acting.</li>
<li><a href="../characters/the-containment-lead-dekan.html">Containment Lead Dekan</a> — Floor, Zone B wound. Entities in cells.</li>
<li><a href="../characters/the-extraction-lead-zyrak.html">Extraction Lead Zyrak</a> — Floor 3. M.A.W. from donors.</li>
<li><a href="../characters/the-research-lead-ayshuk.html">Research Lead Ayshuk</a> — Floor 4 Insight Forge.</li>
<li><a href="../characters/the-border-lead-mellda.html">Border Lead Mellda</a> — Floor 5. Outside Sorrow, Wilderness Tide.</li>
<li><a href="../characters/the-archive-lead-marjuk.html">Archive Lead Marjuk</a> — Floor 6 Deep Vault. Truth under the Tree.</li>
<li><a href="../characters/the-outsider-ishall.html">Outsider Ishall</a> — Floor 7 Shadow Corps. Mobile / field.</li>
<li><a href="../characters/the-exile-xyan.html">Exile Xyan</a> — Floor 8 Gate Watch. Returned route, Gate.</li>
</ul>
</section>
<section class="wiki-section" id="place"><h2 class="section-title">Place in the city</h2>
<p>Facility 01 sits in Zone A deep, in conversation with the Alpha Tree, not as a second skyline. Architects built it — including passages they did not put on the public plan. Wardens provide security and get pulled out of breaches more often than after-action admits. Weavers staff Dream Chambers. Keepers feed research. Collectors want debt data and have tried to hack twice. Giltong have investigated the R.D. three times and found nothing they could file. Menders contract to both R.D. and Architects.</p>
<p>The Absolvohan stockpile is an R.D. secret the Council is not meant to have. Weavers have seen it in Dream. Do not expand that paragraph into the Cycle article.</p>
</section>
<section class="wiki-section" id="ops"><h2 class="section-title">Sister operations</h2>
<p>Present-age trio, not founding corporations: this Directorate (contain), <a href="the-sed-corps.html">SED</a> (explore), <a href="the-ucd-strike-force.html">UCD</a> (underworld descent). Index: <a href="the-founding-corporations.html">three operations</a>. Tools list (Lament Well, Mnemonic Generator, cells, extraction rigs, gauges, effigy, suppression chambers): <a href="faction-technology.html">faction technology</a>.</p>
</section>
"""
    put(
        "factions/the-reverie-directorate.html",
        "The Reverie Directorate",
        "R.D. — Facility 01, nine Echo-Cores. Not the Cycle dump, not SECC, not energy quotas.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Factions</a> <i>/</i> <span>Reverie Directorate</span>',
        "The Reverie Directorate",
        "FACTION · FACILITY 01 · YEAR 4,202",
        [
            ("overview", "Overview"),
            ("cores", "Nine Echo-Cores"),
            ("place", "Place in the city"),
            ("ops", "Sister operations"),
        ],
        body,
        '<a href="index.html">Factions</a> | <a href="../departments/index.html">Floors</a> | <a href="../lore/the-cycle-and-absolvohan.html">Cycle</a>',
        "Reverie Directorate R.D. Echo-Cores Majin Facility 01 Hand of Change",
    )


def unregistered_se():
    pages = [
        (
            "entities/se-004-the-rust-bleeding-sentry.html",
            "SE-004 — Unregistered (Rust-Bleeding Sentry)",
            "004",
            "Rust-Bleeding Sentry",
            "The old sheet made SE-004 a clockwork border guard from a “Great Breach of Year 3,892,” weeping rust sludge, Floor 5. That year and that breach are not in 07_Reference. Codex_Set Registry jumps 003 Wilderness Tide → 005 Smothering Mother. No SE-004 folder exists under 01_Sorrow_Entities.",
        ),
        (
            "entities/se-006-the-siphon-leech.html",
            "SE-006 — Unregistered (Siphon Leech)",
            "006",
            "Siphon Leech",
            "The old sheet made SE-006 an effluent-canal parasite under Facility 01 with a siphon maw and Weight damage. Registry_001_to_007 has 003, 005, 007 only. No Siphon Leech profile exists in the entity corpus. The number was a wiki filler between Brume and Smothering Mother.",
        ),
        (
            "entities/se-008-the-iron-maiden-of-regret.html",
            "SE-008 — Unregistered (Iron Maiden of Regret)",
            "008",
            "Iron Maiden of Regret",
            "The old sheet made SE-008 a thorned sarcophagus on Floor 6 that snaps shut on panic. No 008 Codex set. Iron Maiden of Regret is not a 07_Reference designation. Panic-triggered architecture belongs in containment procedure, not in a made-up ALEPH analogue.",
        ),
    ]
    for rel, title, num, nick, lead in pages:
        body = f"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>{lead}</p>
<p>This URL stays so the thirteen-page hub does not 404. It is a retraction, not a specimen. Do not treat MORPHEAN / SOMNA / PHANTASM risk stickers on the old infobox as SECC. SECC lives on <a href="../mechanics/secc-classification-system.html">the classification page</a>.</p>
</section>
<section class="wiki-section" id="what-exists"><h2 class="section-title">What exists at this number</h2>
<p>Featured registry on this wiki with source cards: SE-001 Orphaned Bell, 002 Grieving Colossus, 003 Wilderness Tide, 005 Smothering Mother, 007 Brume, 009 Memory Weaver, 010 Convergence, 011 Whispering Walls, 014 Debt Eater, 015 Debt Scale. Unknown-numbered articles (247, 248, 250, 251, 901–903) are a different gap — they <em>do</em> have source files. SE-{num} does not.</p>
<p>M.A.W. URLs hung on this number (W/S/G-{num}) are marked unregistered on the arsenal side. Do not forge from them. Do not dump 275 extra entity HTML files to “fill” SE-{num}.</p>
</section>
<section class="wiki-section" id="if-source"><h2 class="section-title">If source arrives</h2>
<p>A later 01_Sorrow_Entities file that actually uses number {num} should overwrite this page from that file — designation, Work Types, breach, location. Until then the nickname “{nick}” is a retired wiki label, not canon. See <a href="index.html">Sorrow Entities</a> and <a href="list.html">the list</a> (thirteen is a fraction of ~3XX).</p>
</section>
"""
        put(
            rel,
            title,
            f"SE-{num} is not in the Codex or 01_Sorrow_Entities. Retired wiki nickname: {nick}.",
            f'<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Entities</a> <i>/</i> <span>SE-{num}</span>',
            title,
            f"SE-{num} · UNREGISTERED",
            [("overview", "Overview"), ("what-exists", "What exists at this number"), ("if-source", "If source arrives")],
            body,
            '<a href="index.html">Sorrow Entities</a> | <a href="list.html">List</a> | <a href="../maw/index.html">M.A.W.</a>',
            f"SE-{num} unregistered {nick} not in Codex",
        )


def patch_faction_index():
    p = DOCS / "factions" / "index.html"
    t = p.read_text(encoding="utf-8")
    t2 = t.replace(
        '<p class="entity-card-desc">Artisans weaving protective Veil fabrics, synaptic tapestries, and M.A.W. suit linings.</p>',
        '<p class="entity-card-desc">Dream guild — Somnus, Dream Loom, Resonance Mask, Spire of Dreams.</p>',
    )
    t2 = t2.replace(
        '<p class="entity-card-desc">Garrison legion manning the Perimeter Bulwark against wasteland horde incursions.</p>',
        '<p class="entity-card-desc">Military guild — Citadel, Barrier Baton, Zone E Border Corps.</p>',
    )
    t2 = t2.replace(
        '<p class="entity-card-desc">Scavenger cartel operating ',
        '<p class="entity-card-desc">Debt guild — Echo economy, Debt-Ledger, Collector’s Spire. Scavenger cartel operating ',
    )
    # insert Keepers card after Weavers card
    weaver_card_end = '</a></div>\n    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/icon_faction_wardens.svg"'
    keepers_card = '''</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/icon_faction_keepers.svg" alt="Keepers" class="entity-card-icon"><div class="entity-card-meta"><span class="risk-badge risk-he">MASTER GUILD</span></div></div><h3 class="entity-card-name">THE KEEPERS</h3><p class="entity-card-desc">Memory guild — Grand Archive, Memory Lens, Whispering Index. Not the Washers.</p><a href="the-keepers.html" class="jump-btn">VIEW GUILD DOSSIER →</a></div>
    <div class="pm-entity-card"><div class="entity-card-top"><img src="../assets/icons/icon_faction_wardens.svg"'''
    if "the-keepers.html" not in t2:
        if weaver_card_end in t2:
            t2 = t2.replace(weaver_card_end, keepers_card, 1)
            print("inserted Keepers card on factions index")
        else:
            print("WARN could not find Weavers/Wardens junction for Keepers card")
    if t2 != t:
        p.write_text(t2, encoding="utf-8")
        print("patched factions/index.html")


def patch_high_council_keepers_link():
    p = DOCS / "factions" / "the-high-council.html"
    t = p.read_text(encoding="utf-8")
    t2 = t.replace(
        "Head Keeper (기록장) — Grand Archive, Building 2. Memory, history, identity. No split Keepers article yet; do not confuse them with",
        'Head Keeper (기록장) — Grand Archive, Building 2. Memory, history, identity. Full article: <a href="the-keepers.html">the Keepers</a>. Do not confuse them with',
    )
    if t2 != t:
        p.write_text(t2, encoding="utf-8")
        print("patched high-council Keepers link")


def patch_search():
    sp = DOCS / "data" / "search.json"
    data = json.loads(sp.read_text(encoding="utf-8"))
    by = {e.get("url"): e for e in data}
    for e in SEARCH_UPDATES:
        old = by.get(e["url"])
        if old:
            old.update({k: e[k] for k in ("title", "description", "keywords") if e.get(k)})
        else:
            data.append(e)
            by[e["url"]] = e
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("search", len(data))


def main():
    keepers()
    dream()
    rd()
    unregistered_se()
    patch_faction_index()
    patch_high_council_keepers_link()
    patch_search()
    print("batch3 done")


if __name__ == "__main__":
    main()
