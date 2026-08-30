#!/usr/bin/env python3
"""Rewrite dump guild/location/war pages and leftover classification crumbs."""
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
    text = re.sub(r"<script[\s\S]*?</script>", " ", body)
    text = re.sub(r"<[^>]+>", " ", text)
    return len(re.findall(r"[A-Za-z0-9']+", text))


def put(rel: str, title: str, desc: str, crumbs: str, h1: str, eyebrow: str, toc, body: str, cats: str, search_kw: str):
    doc = wrap(title, desc, crumbs, h1, eyebrow, toc, body, cats)
    path = DOCS / rel
    path.write_text(doc, encoding="utf-8")
    w = words(doc)
    print(f"wrote {rel} ({w}w)")
    if w < 300:
        print("  WARN under 300")
    return {
        "url": rel,
        "title": title,
        "description": desc[:180],
        "keywords": search_kw,
        "type": "article",
    }


SEARCH_UPDATES = []


def council():
    body = """
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The <strong>Council of Sighs</strong> (한숨의 의회) sits in the Sigh Palace — Building 1 of the Alpha Tree, Zone A. It is Somnarak’s top civil authority, and it is more shock-absorber than throne. Membership is chosen by the <em>weight carried</em>: how much Han a person has absorbed and still not Fractured. Rulers are often the most broken people in the city. Membership is for life, or until the member can no longer bear it.</p>
<p>Philosophy: <em>“This is inevitable. We merely manage the flow of grief.”</em> The Council decides <em>what</em> must happen. The Five Heads decide <em>how</em>. Citizens bear the cost. Sector authorities, not the Palace, govern daily life.</p>
<p>This page is the Council. It is not a paste of every faction-relations table and collapse chapter from <code>PROJECT_SOMNARAK.md</code>. Those belong on the guild articles and on <a href="faction-technology.html">faction technology</a>.</p>
</section>
<section class="wiki-section" id="work"><h2 class="section-title">What the Council does</h2>
<p>It sets city-wide policy, resolves disputes between Heads, approves or denies major structural changes (new sectors, demolitions), and maintains the city’s relationship with the Dream and the Abyss. It does not police alleys. That is the Wardens. It does not collect Echoes. That is the Collectors.</p>
<p>Weakness: they are chosen for endurance, not wisdom. Many are numb. They resist change because uncertainty creates Han. The Head Architect is the regular opponent — the only Head that pushes reform. Strength: they have survived what would break anyone else. Fatalism here is realism. When they say a thing is inevitable they are speaking from the Cheongula, the Occlusihan, and six thousand years of watching people try to kill sorrow and get eaten.</p>
</section>
<section class="wiki-section" id="heads"><h2 class="section-title">The Five Heads</h2>
<p>Each Head controls a domain, reports to the Council, and operates with real autonomy. Full guild articles:</p>
<ul>
<li><a href="the-architects.html">Head Architect (건축장)</a> — Architect’s Hall, Building 6. Expansion, repair, Han-flow reroute. The only faction that tries to change the city.</li>
<li><a href="the-collectors.html">Head Collector (추징장)</a> — Collector’s Spire, Zone C. Debt, Echo economy, pursuit. The most feared.</li>
<li>Head Keeper (기록장) — Grand Archive, Building 2. Memory, history, identity. No split Keepers article yet; do not confuse them with <a href="the-memory-washers.html">Memory Washers</a>.</li>
<li><a href="the-wardens.html">Head Warden (수호장)</a> — Warden’s Citadel. Order, Zone E border, Fracture response.</li>
<li><a href="the-weavers.html">Head Weaver (직녀장)</a> — Spire of Dreams, Building 4. Dream-diving, boundary, interpretation.</li>
</ul>
<p>The Reverie Directorate is funded by the Council and is not a sixth Head. See <a href="the-reverie-directorate.html">the Directorate</a>. Giltong report to the Council as Taboo enforcement, parallel to Wardens.</p>
</section>
<section class="wiki-section" id="tech"><h2 class="section-title">Palace instruments</h2>
<p><strong>The Sigh Recorder</strong> (한숨 기록기) is a fist-sized crystalline orb. When a Council member sighs, the orb stores the exhaled sorrow as a compressed Echo of the decision that caused it. Playback transfers a fraction of that burden to the listener. Debates use it so the room can feel the weight, not only hear the argument.</p>
<p><strong>The Decision Scale</strong> (결정 저울) measures the sorrow a proposed decision will create. It is never wrong, and it only shows sorrow, not joy. A choice that makes people happy and also makes people suffer still tips. The Council has to weigh joy themselves. See <a href="faction-technology.html">faction technology</a>.</p>
</section>
<section class="wiki-section" id="not-dump"><h2 class="section-title">What this page is not</h2>
<p>It is not “V. Governance — The Fatalistic Order” followed by every relations table, trade matrix, rivalry, collusion cell, and faction-collapse phase list. Those chapters live in source and should be split: relations onto each guild, collapse onto a dedicated article when written, RD/SED/UCD onto <a href="the-founding-corporations.html">the three operations</a>.</p>
</section>
"""
    SEARCH_UPDATES.append(
        put(
            "factions/the-high-council.html",
            "The Council of Sighs",
            "Somnarak’s Council of Sighs — endurance as authority, Five Heads, Sigh Recorder and Decision Scale.",
            '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Factions</a> <i>/</i> <span>Council of Sighs</span>',
            "The Council of Sighs",
            "FACTION · ZONE A · SIGH PALACE",
            [
                ("overview", "Overview"),
                ("work", "What the Council does"),
                ("heads", "The Five Heads"),
                ("tech", "Palace instruments"),
                ("not-dump", "What this page is not"),
            ],
            body,
            '<a href="index.html">Factions</a> | <a href="the-architects.html">Architects</a> | <a href="faction-technology.html">Faction tech</a>',
            "Council of Sighs High Council Five Heads Sigh Palace Geonchukjang Chujingjang Girokjang Suhujang Jiknyeojang",
        )
    )


def collectors():
    body = """
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The <strong>Collectors</strong> (수금가 — Sugeumga; also 추징) are Somnarak’s debt guild. Power is economic: they track karmic obligation, manage Echoes, and enforce payment. Headquarters is the Collector’s Spire in Zone C (SECTOR-C-01), under the Head Collector (추징장). Citizens avoid them. Architects shelter debtors. Debt Brokers undercut them from the Frays. They are not the Keepers and they are not the Memory Washers.</p>
<p>Philosophy: <em>“Debts must be paid. This is not cruelty — it is balance.”</em> Every action in a Han-structural city writes a debt in the Abyss. Debts manifest as aging, illness, bad luck, transformation. They can be transferred (the powerful shift them onto the weak), deferred (interest is more sorrow), or paid (suffering, sacrifice, Echoes).</p>
</section>
<section class="wiki-section" id="work"><h2 class="section-title">Work and structure</h2>
<p>They track and collect karmic debts, enforce the Cycle of Debt, regulate the Echo economy against inflation and counterfeiting, and pursue evaders. Internal line: Head Collector → Senior Collectors (zone) → Collectors (field) → Assessors → apprentices. Two offices sit beside that line: the Debt Registry (who owes, how much, to whom) and the Pursuit Division.</p>
<p>Trade: citizens give Echoes for “debt management.” The Directorate trades entity data for Echo funding and then guards the rest of its ledgers; Collectors have tried to hack those systems twice. Collectors pay Wardens a secret extra budget for debt enforcement. They tried to monetize Dream-diving; Weavers refused.</p>
</section>
<section class="wiki-section" id="tools"><h2 class="section-title">Tools</h2>
<p><strong>Debt-Ledger</strong> (부채 장부): a book of thin Han-crystal sheets. Debts display as weight — numbers, graphs, emotional impression. It can scan a person. Transfer, payment, and deferral go through it. If a Collector opens it with malice, the pages show the Collector’s own debts.</p>
<p><strong>Extraction Glove</strong> (추출 장갑): dark Han-crystal, elongated fingers, palm glow. Placed on a debtor it draws Echoes through the palm. Painless, exhausting. The Collector feels a fragment of the debtor’s sorrow. Some go numb. Some break.</p>
<p>Related entities, not tools: <a href="../entities/se-014-the-debt-eater.html">SE-014 Debt Eater</a> and <a href="../entities/se-015-the-debt-scale.html">SE-015 Debt Scale</a> sit in Collector mythology and containment, not in every field kit.</p>
</section>
<section class="wiki-section" id="row"><h2 class="section-title">Collector’s Row</h2>
<p>Zone C is their street. Chunhwa the Debt Widow stands outside it every day with a sign: <em>“My husband paid his debt. Why does yours keep growing?”</em> He paid for thirty years; the guild reclassified the remainder as compound interest; he Fractured from relief. The kindness protocol — for citizens who are truly desperate — exists on paper and is never used.</p>
<p>Alliance with the Council is economic policy with a reversed power dynamic: Collectors hold more Echoes than the Palace. Collapse trigger in source: a Head who hoards all Echoes, or a debt system nobody can pay. See <a href="zone-c-collectors-row.html">Zone C</a> if that atlas page is the street; otherwise <a href="../locations/zone-c-collectors-row.html">Collectors’ Row</a>.</p>
</section>
"""
    SEARCH_UPDATES.append(
        put(
            "factions/the-collectors.html",
            "The Collectors",
            "Sugeumga debt guild — Echo economy, Debt-Ledger, Extraction Glove, Collector’s Spire in Zone C.",
            '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Factions</a> <i>/</i> <span>The Collectors</span>',
            "The Collectors",
            "FACTION · ZONE C · DEBT",
            [
                ("overview", "Overview"),
                ("work", "Work and structure"),
                ("tools", "Tools"),
                ("row", "Collector’s Row"),
            ],
            body,
            '<a href="index.html">Factions</a> | <a href="the-high-council.html">Council</a> | <a href="../locations/zone-c-collectors-row.html">Zone C</a>',
            "Collectors Sugeumga Chujingjang Debt-Ledger Extraction Glove Echoes Zone C Collector Spire Chunhwa",
        )
    )


def weavers():
    body = """
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The <strong>Weavers</strong> (직공 — Jikgong; Head title 직녀장) are the Dream guild. Power is oneiric: they walk Somnus, interpret visions, and keep the boundary between sleep and the street from tearing. Headquarters is the Spire of Dreams, Building 4 of the Alpha Tree, south point of Zone A — glass that shows illusions, reality bent at the edges.</p>
<p>Philosophy: <em>“The Dream is not illusion. It is the world’s true face — we are the dream.”</em> The Council distrusts Dream influence. Citizens fear them. Wardens do not trust Dream work. Keepers rival them: both handle memory, Keepers through the Archive, Weavers through the Dream. The Directorate cooperates — Weavers supply Dream support, including watch on the Absolvohan.</p>
</section>
<section class="wiki-section" id="work"><h2 class="section-title">Work and structure</h2>
<p>They manage the Dream/physical boundary, monitor Dream entities, run Dream-dives for research or retrieval, and study how Han moves through the mind. Somnus is not another planet. It is the subconscious layer of this one: emotions are objects, memories are rooms, desires are bodies. Time stretches. Depth is danger. Echoes of the Before-Time live there, distorted.</p>
<p>Line: Head Weaver → Senior Weavers → Weavers → Dream Divers → apprentices. Beside the line: Entity Division, Boundary Corps, Interpretation Bureau. Free Dream consultations are offered. Almost nobody accepts.</p>
<p>They have seen the Council fall and the debt system collapse in vision and have not filed those reports. They have designed Dream-spaces Architects could build if Architects asked. They have accessed memories Keepers thought sealed. They have a secret exchange program with Keepers anyway.</p>
</section>
<section class="wiki-section" id="tools"><h2 class="section-title">Tools</h2>
<p><strong>Dream Loom</strong> (꿈 베틀): a frame of crystallized Dream that never holds one shape. Threads of light. Stretch them and you pull objects, information, or entities out of Somnus — or send memories and warnings in. Idle, the Loom dreams on its own threads. Watching it is addictive.</p>
<p><strong>Resonance Mask</strong> (공명 가면): crystallized reality, warm, humming. Eyes of clear crystal see Dream and street at once. It anchors identity so the diver does not dissolve, and it yanks them back if they go too deep. It remembers every Dream the wearer entered. Touch it and you can revisit. That is the trap.</p>
</section>
<section class="wiki-section" id="not-se009"><h2 class="section-title">Not SE-009</h2>
<p><a href="../entities/se-009-the-memory-weaver.html">SE-009 The Memory Weaver</a> is a Sorrow Entity in the library of stolen pasts. The guild is living people with looms. Do not file the entity as the Head Weaver. See <a href="../lore/the-dream-realm.html">the Dream realm</a> and <a href="faction-technology.html">faction technology</a>.</p>
</section>
"""
    SEARCH_UPDATES.append(
        put(
            "factions/the-weavers.html",
            "The Weavers",
            "Jikgong Dream guild — Spire of Dreams, Dream Loom, Resonance Mask, Somnus boundary.",
            '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Factions</a> <i>/</i> <span>The Weavers</span>',
            "The Weavers",
            "FACTION · ZONE A · DREAM",
            [
                ("overview", "Overview"),
                ("work", "Work and structure"),
                ("tools", "Tools"),
                ("not-se009", "Not SE-009"),
            ],
            body,
            '<a href="index.html">Factions</a> | <a href="../lore/the-dream-realm.html">Dream realm</a> | <a href="faction-technology.html">Faction tech</a>',
            "Weavers Jikgong Jiknyeojang Dream Loom Resonance Mask Spire of Dreams Somnus",
        )
    )


def wardens():
    body = """
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The <strong>Wardens</strong> (수호자 — Suhuja; also 경비) are Somnarak’s military and street order. Power is force: they patrol zones, hold Zone E against the Desolate, and answer Fracture and overflow. Headquarters is the Warden’s Citadel in Zone C’s Warden Quarter, under the Head Warden (수호장). Citizens respect them and do not love them. Frays treat them as the primary threat. Giltong run parallel enforcement — Taboo, not patrol.</p>
<p>Philosophy: <em>“We protect the city from itself — and from what lies beyond.”</em> They have disobeyed Council orders twice, both times to protect citizens. They need Architects for walls and resent the gaps construction opens. Collectors need them for debt muscle; Wardens resent being rented.</p>
</section>
<section class="wiki-section" id="work"><h2 class="section-title">Work and structure</h2>
<p>Public order, border defense, Han-overflow response (contain, evacuate, stabilize), Council decree enforcement. Line: Head Warden → five Zone Commanders → Sector Captains → Wardens → recruits. Three specialist arms: Border Corps (Zone E, worst posting, most honest), Containment Squad (Fracture and Sorrow-Wrought), Internal Affairs (the guild watching itself).</p>
<p>Violence in a Han-structural city writes more sorrow. That is the daily bind. The Directorate uses Wardens as facility security; RD has pulled Wardens out of entity breaches more times than Warden after-action admits. Architect construction zones have been used as unofficial training grounds.</p>
</section>
<section class="wiki-section" id="tools"><h2 class="section-title">Tools</h2>
<p><strong>Barrier Baton</strong> (방벽 지팡이): reinforced Han-crystal, warm, tip-glow. Projects a small suppression field — shield, barrier, or dampening zone — or strikes with the weight of held-down sorrow. Strength tracks the Warden’s calm. The baton absorbs what it suppresses. A veteran’s baton is emotionally dense.</p>
<p><strong>Watchtower Eye</strong> (감시탑의 눈): head-sized crystalline sphere on Zone E towers. Scans the Desolate for Han-flow, entities, movement; alerts red. It sees emotional intensity, not only bodies. Frightened civilians and a calm patrol do not look the same.</p>
<p>Also issued: temporary Han-suppression gear, Fracture dampeners that slow and do not stop, and the Barrier network around key sites. See <a href="../locations/zone-e-perimeter-bulwark.html">Zone E</a> and <a href="../entities/se-003-the-wilderness-tide.html">SE-003 Wilderness Tide</a>.</p>
</section>
<section class="wiki-section" id="dilemma"><h2 class="section-title">Dilemma</h2>
<p>Do they serve the city or the Council? Internal corruption is named in source, not denied. Collapse example: an entire Warden division Fracturing after a major breach, or a Desolate incursion that overwhelms the wall. Neutral ground with Frays exists only at <a href="../locations/the-hollow-glass.html">the Hollow Glass</a> in Zone D — Bong’s tavern — and not because Wardens made it so.</p>
</section>
"""
    SEARCH_UPDATES.append(
        put(
            "factions/the-wardens.html",
            "The Wardens",
            "Suhuja military guild — Citadel, Barrier Baton, Watchtower Eye, Zone E Border Corps.",
            '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Factions</a> <i>/</i> <span>The Wardens</span>',
            "The Wardens",
            "FACTION · ORDER · ZONE E",
            [
                ("overview", "Overview"),
                ("work", "Work and structure"),
                ("tools", "Tools"),
                ("dilemma", "Dilemma"),
            ],
            body,
            '<a href="index.html">Factions</a> | <a href="../locations/zone-e-perimeter-bulwark.html">Zone E</a> | <a href="faction-technology.html">Faction tech</a>',
            "Wardens Suhuja Suhujang Barrier Baton Watchtower Eye Zone E Border Corps Fracture",
        )
    )


def orphan_bell():
    body = """
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The <strong>Orphan Bell Tower</strong> is the place-name attached to <a href="../entities/se-001-the-orphaned-bell.html">SE-001 The Orphaned Bell</a>. It is not a Worldbuilding Framework dump, and it is not “Sector 7” in an LC facility sense. The bell’s tale line is: <em>“The bell tolls for children who will never grow old.”</em></p>
<p>SE-001 is a contained City Sorrow. The tower is the architecture that grew around that grief — a vertical room that still thinks it is calling children home. Directorate observation treats the site and the entity as one operational problem: you do not schedule the tower without scheduling the Bell.</p>
</section>
<section class="wiki-section" id="place"><h2 class="section-title">Place</h2>
<p>Zone B carries the city’s oldest sorrows. The Old Lament (옛 탄식) is inner B, closest to A: first homes of solidified grief, walls that replay settlers, buildings that grew faces. A bell-tower that refuses to stop being a school-yard signal belongs in that grain of the city even when the containment cell is inside Facility 01.</p>
<p>Do not confuse this page with deleted satellite logs (<code>se-001-containment-log</code>). Instinct/Insight paste is gone. Work types, breach, and M.A.W. live on the entity article and on <a href="../maw/maw-w-001-01-the-laments-requiem.html">Lament’s Requiem</a>.</p>
</section>
<section class="wiki-section" id="sound"><h2 class="section-title">What the tower does</h2>
<p>A bell that tolls for the unaged is a Place as much as a Subject. People who grew up in B report knowing the hour by a ring that is not on any civic clock. Keepers want the sound archived. Collectors have tried to price the hour. Wardens treat an unsanctioned ring as a crowd problem. Weavers say the overtones continue in Somnus after the bronze stops.</p>
<p>See <a href="../locations/zone-b-west-ward.html">Zone B</a>, <a href="../entities/se-001-the-orphaned-bell.html">SE-001</a>, and <a href="../lore/the-book-of-regressor.html">the Book of the Regressor</a> when that record cites the Bell.</p>
</section>
"""
    SEARCH_UPDATES.append(
        put(
            "locations/the-orphan-bell-tower.html",
            "The Orphan Bell Tower",
            "Place of SE-001 The Orphaned Bell — Zone B grief architecture, not a Worldbuilding Framework stub.",
            '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Atlas</a> <i>/</i> <span>Orphan Bell Tower</span>',
            "The Orphan Bell Tower",
            "ATLAS · ZONE B · SE-001",
            [("overview", "Overview"), ("place", "Place"), ("sound", "What the tower does")],
            body,
            '<a href="index.html">Atlas</a> | <a href="../entities/se-001-the-orphaned-bell.html">SE-001</a> | <a href="zone-b-west-ward.html">Zone B</a>',
            "Orphan Bell Tower SE-001 Orphaned Bell Zone B Old Lament",
        )
    )


def hollow_glass():
    body = """
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p><strong>The Hollow Glass</strong> is a tavern in Zone D, not a District 4 memorial and not an empty canonical-record box. It is the only named neutral ground in D: Wardens, Frays, Menders, Collectors, and ordinary citizens drink side by side. Fights do not happen there because Bong will not serve anyone who starts one. His silence is the house rule. His memory is worse — which is to say, complete.</p>
<p>Bong (봉) was a Collector, one of the honest ones. He found a phantom debt written by Debt Brokers onto a family that had never borrowed. He reported it three times. He was ignored, threatened, then fired. He opened the Glass the next month.</p>
</section>
<section class="wiki-section" id="glass"><h2 class="section-title">The glass that never empties</h2>
<p>Third seat from the left is empty. The glass there is always full of the cheapest Han-water. Bong’s wife Fractured behind the bar on a quiet Tuesday. He swept the crystal himself. He never changed the layout. Every evening at 8:47 — the minute of the Fracture — he fills the glass and moves on. People who know leave an Echo beside it. He spends those Echoes on more Han-water.</p>
<p>His question in the Cast file: <em>“If I serve everyone’s sorrow in a glass, who serves mine?”</em> The tavern is open. The seat is empty. That is the memorial. There is no plaque, no Council ribbon, no SECC file.</p>
</section>
<section class="wiki-section" id="use"><h2 class="section-title">Use</h2>
<p>SED and UCD both know the door. Information moves here because nobody is in uniform at the bar — or everyone is, and Bong does not care. Neutral does not mean safe outside the threshold. Zone D is forge and gardens, Furnace refugees, Mender traffic. See <a href="zone-d-forge-and-gardens.html">Zone D</a>, <a href="../factions/the-underworld-and-wound-walkers.html">the underworld</a>, and <a href="../factions/the-wardens.html">Wardens</a>.</p>
</section>
"""
    SEARCH_UPDATES.append(
        put(
            "locations/the-hollow-glass.html",
            "The Hollow Glass",
            "Bong’s Zone D tavern — only named neutral ground. The unemptied glass at 8:47.",
            '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Atlas</a> <i>/</i> <span>The Hollow Glass</span>',
            "The Hollow Glass",
            "ATLAS · ZONE D · NEUTRAL GROUND",
            [("overview", "Overview"), ("glass", "The glass that never empties"), ("use", "Use")],
            body,
            '<a href="index.html">Atlas</a> | <a href="zone-d-forge-and-gardens.html">Zone D</a> | <a href="../factions/the-underworld-and-wound-walkers.html">Underworld</a>',
            "Hollow Glass Bong Zone D tavern neutral ground Debt Brokers",
        )
    )


def library():
    body = """
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The <strong>Library of Stolen Pasts</strong> is the location line on <a href="../entities/se-009-the-memory-weaver.html">SE-009 The Memory Weaver</a>: SECTOR-B-02, Zone B — library of stolen pasts; contained. It is not the Grand Archive. Keepers preserve. This room keeps what was taken.</p>
<p>SE-009 weaves memories into webs. The library is the architecture of that habit: shelves that are not a civic catalog, pages that are not consented Echoes. R.D. Observation Level 3. The entity is mobile. The room is still a Place — people get lost in the stacks for hours they cannot later name.</p>
</section>
<section class="wiki-section" id="not-archive"><h2 class="section-title">Not the Grand Archive</h2>
<p>Building 2, Zone A, is the Keepers’ Grand Archive: history, Whispering Index, vaults into Dream-space. The Library of Stolen Pasts is a Zone B containment geography. Memory Fray / Washers steal from the Archive and sell. SE-009 is what happens when stolen recollection coagulates into a weaver instead of a ledger.</p>
<p>M.A.W. from this entity is the Forgotten set — <a href="../maw/maw-w-009-01-the-forgotten-lens.html">Forgotten Lens</a>, Veil, Mask — not the misfiled “Memory Blade” on the SE-003 slot. See <a href="../factions/the-memory-washers.html">Memory Washers</a> and <a href="../locations/zone-b-west-ward.html">Zone B</a>.</p>
</section>
<section class="wiki-section" id="work"><h2 class="section-title">Working the stacks</h2>
<p>Valid work against a memory-pressure Subject is not “read quietly.” Insight and related types on the entity page apply. Failed work or ignored activation (Sorrow Gauge climbing) is a breach of identity, not of masonry. Agents report leaving with someone else’s childhood stuck under the tongue.</p>
<p>Do not dump the whole SE-009 combat record onto this URL. Combat, SECC, and M.A.W. stay on the entity and arsenal pages. This article is the room.</p>
</section>
"""
    SEARCH_UPDATES.append(
        put(
            "locations/the-library-of-stolen-pasts.html",
            "The Library of Stolen Pasts",
            "SECTOR-B-02 containment geography of SE-009 The Memory Weaver. Not the Grand Archive.",
            '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Atlas</a> <i>/</i> <span>Library of Stolen Pasts</span>',
            "The Library of Stolen Pasts",
            "ATLAS · ZONE B · SE-009",
            [("overview", "Overview"), ("not-archive", "Not the Grand Archive"), ("work", "Working the stacks")],
            body,
            '<a href="index.html">Atlas</a> | <a href="../entities/se-009-the-memory-weaver.html">SE-009</a> | <a href="zone-b-west-ward.html">Zone B</a>',
            "Library of Stolen Pasts SE-009 Memory Weaver Zone B SECTOR-B-02 Forgotten Lens",
        )
    )


def wars():
    body = """
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>There was no “First Sovereign War” against “Old Dreamers” and “Founding Corporations.” That overlay was wiki invention. Canon wars, from <code>PROJECT_SOMNARAK.md</code> History:</p>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>War</th><th>Name</th><th>Cause</th><th>Outcome</th></tr></thead>
<tbody>
<tr><td>1st</td><td>The Cheongula (천구라)</td><td>Han consumed 1,000 citizens</td><td>Proof the city is alive and hungry. Panic. The Maw.</td></tr>
<tr><td>2nd</td><td>The Occlusihan (오클루시한)</td><td>Six factions tried to seal Han</td><td>Failed. Han grew. Fracture emerged.</td></tr>
<tr><td>3rd</td><td>The Consolihan (결한 전쟁)</td><td>Destabilized accumulation</td><td>Solidification. The Alpha Tree. The city as fortress of frozen tears.</td></tr>
<tr><td>4th (?)</td><td>The Third Conflict</td><td>Preservation vs reform</td><td>Council fatalism — or an ongoing cold war.</td></tr>
</tbody></table></div>
<p>Somnarak is counted ~6,000 years from the first Zone B settlement. Cheongula is year 202. Occlusihan 202–223. Consolihan 234–245. Structuring 245–281. SED ~4200. Directorate 4202. Present Dawn Initiative ~4232–4238.</p>
</section>
<section class="wiki-section" id="occlusihan"><h2 class="section-title">Occlusihan — the First War</h2>
<p>Latin <em>occlusio</em> (to shut) + Han. After the Cheongula, six early factions tried to close the flow entirely, fighting in Zone B and fighting the city itself.</p>
<p>Sealers built walls and made eruption points. Severers suppressed emotion and made Fracture hotspots. Offerers fed Han and made it stronger. Exilers shoved grief into Dream or Abyss and tore rifts. Converters transmuted — partial success, ancestor of Architect practice. Endurers accepted hunger — ancestor of Council fatalism. Nobody won. Exhaustion became the Consolihan.</p>
<p>Lesson filed by every later Head: fighting Han directly feeds it; severing it Fractures people; feeding it makes it hungrier. Working with it is the only partial success.</p>
</section>
<section class="wiki-section" id="consolihan"><h2 class="section-title">Consolihan</h2>
<p>Latin <em>consolidare</em> + Han. Not a war against an army. A war to freeze a tide. After Occlusihan, sorrow pooled into rivers and ate settlements. Survivors combined Converter technique with Endurer philosophy and solidified Han into meaning. Where feeling gathered hardest, the <strong>Alpha Tree</strong> grew — not a building, a cumulation. Sigh Palace weeps. Six buildings hold. Spire of Dreams reaches. Abyssal Well drops. Archive light is rare. Crucible weight anchors.</p>
<p>The city grew around the Tree the way crystal grows on crystal. See <a href="../locations/zone-a-core-nexus.html">Zone A</a> and <a href="../lore/index.html">lore</a>.</p>
</section>
<section class="wiki-section" id="retired"><h2 class="section-title">Retired overlay</h2>
<p>Discard: Old Dreamers, Founding Corporations as precursor Wings, Nine Veiled Edicts as LC seed-of-light copy. RD, SED, and UCD are Year 4,200 operations, not Age I corporations. Use <a href="../factions/the-founding-corporations.html">the three operations</a> for that split.</p>
</section>
"""
    SEARCH_UPDATES.append(
        put(
            "lore/the-first-sovereign-war.html",
            "The Wars of Somnarak",
            "Cheongula, Occlusihan, Consolihan — not a Sovereign War of Old Dreamers.",
            '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Lore</a> <i>/</i> <span>Wars of Somnarak</span>',
            "The Wars of Somnarak",
            "LORE · HISTORY · 202–245",
            [
                ("overview", "Overview"),
                ("occlusihan", "Occlusihan"),
                ("consolihan", "Consolihan"),
                ("retired", "Retired overlay"),
            ],
            body,
            '<a href="index.html">Lore</a> | <a href="../locations/zone-a-core-nexus.html">Zone A</a> | <a href="../factions/the-high-council.html">Council</a>',
            "Occlusihan Consolihan Cheongula Alpha Tree Wars of Somnarak First War",
        )
    )


def three_ops():
    body = """
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>Somnarak does not have “founding precursor corporations” in the Wing/Fixer sense. It has <strong>three operations</strong> in the present age, all after year 4200:</p>
<ul>
<li><a href="the-reverie-directorate.html">Reverie Directorate (R.D.)</a> — contain Sorrow Entities, extract M.A.W., run Facility 01. Founded 4202.</li>
<li><a href="the-sed-corps.html">Somnarak Exploration Decreed (SED)</a> — map the unmapped, Corner cities, Desolate edges. Council decree ~4200.</li>
<li><a href="the-ucd-strike-force.html">Underworld Cleanup Descend (UCD)</a> — Fray raids, Wash District, black-market Han. Combat descent, not a Wing.</li>
</ul>
<p>One city, three missions, shared sorrow. The old page pasted the entire game-framework chapter (casts, loops, Hand of Hope ending) onto this URL. That dump is gone. Cast stays on character pages. Absolvohan stays on <a href="../lore/the-cycle-and-absolvohan.html">the Cycle</a>. Hand of Hope stays on <a href="../entities/hope-transformations.html">Hope Transformations</a>.</p>
</section>
<section class="wiki-section" id="connect"><h2 class="section-title">How they connect</h2>
<p>The Council funds the Directorate and does not fully understand it. SED walks what the facility will later have to contain. UCD hits the Frays that feed on what leaks from both. Menders contract to RD and Architects at once. Wardens back all three and trust none of the paperwork.</p>
<p>Shared world: Zones A–E, the Desolate, Cheonbulok and Mugeukji as Corner cities, the Gate. Shared threat: Han that will not stay in one jurisdiction. The Absolvohan is an RD secret the Council is not meant to have; Weavers are watching it in Dream anyway.</p>
</section>
<section class="wiki-section" id="not-wings"><h2 class="section-title">Not Wings</h2>
<p>Do not map R.D. to Lobotomy Corporation, SED to Limbus, UCD to a Fixer Office and call them precursor corporations. Analog research belongs in REFERENCE, not in this article’s heading stack. If you need the six Occlusihan factions (Sealers, Severers, Offerers, Exilers, Converters, Endurers), that is <a href="../lore/the-first-sovereign-war.html">the wars</a>, year 202–223, not year 4202.</p>
</section>
"""
    SEARCH_UPDATES.append(
        put(
            "factions/the-founding-corporations.html",
            "The Three Operations",
            "R.D., SED, and UCD — present-age operations, not founding precursor corporations.",
            '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Factions</a> <i>/</i> <span>Three Operations</span>',
            "The Three Operations",
            "FACTION · R.D. · SED · UCD",
            [("overview", "Overview"), ("connect", "How they connect"), ("not-wings", "Not Wings")],
            body,
            '<a href="the-reverie-directorate.html">Directorate</a> | <a href="the-sed-corps.html">SED</a> | <a href="the-ucd-strike-force.html">UCD</a>',
            "Three Operations Reverie Directorate SED UCD not founding corporations",
        )
    )


def strip_han_dump():
    p = DOCS / "mechanics" / "han-energy-and-damage.html"
    t = p.read_text(encoding="utf-8")
    t2 = re.sub(
        r'<section class="wiki-section" id="vii-han-classification">.*?</section>',
        '<section class="wiki-section" id="secc-pointer"><h2 class="section-title">Classification</h2>'
        "<p>Entity codes do not live on this damage page. Use "
        '<a href="secc-classification-system.html">SECC — classification codes only</a>. '
        "SCS (Dohan/Oehan/Naehan) is superseded; origin letters are C / O / N. "
        "This article stays on the four elemental aspects of sorrow as damage: Lament, Grudge, Void, Weight.</p>"
        "</section>",
        t,
        count=1,
        flags=re.S,
    )
    t2 = t2.replace(
        '<li><a href="#vii-han-classification">Sorrow Entities — Classification</a></li>',
        '<li><a href="#secc-pointer">Classification</a></li>',
    )
    t2 = t2.replace(
        '<li><a href="#sorrow-entities-classification">Sorrow Entities — Classification</a></li>',
        '<li><a href="#secc-pointer">Classification</a></li>',
    )
    if t2 != t:
        p.write_text(t2, encoding="utf-8")
        print("stripped han-energy classification dump", words(t2), "w")
    else:
        print("han-energy: no dump match")


def maw_003():
    common_tail = """
<p>Source: <code>SE-003-A</code> Border Lead Mellda, Year 4,238, Restricted. Codex set completion 1/1 — subject card only. Record status: active Zone E border phenomenon. Do not invent a rapier, a needle, or a cloak and hang them on this number.</p>
<p>See <a href="../entities/se-003-the-wilderness-tide.html">SE-003</a>, <a href="../factions/the-wardens.html">Wardens</a>, <a href="../locations/zone-e-perimeter-bulwark.html">Zone E</a>. Memory equipment belongs to <a href="maw-w-009-01-the-forgotten-lens.html">SE-009 Forgotten Lens</a>.</p>
"""
    pages = [
        (
            "maw/maw-w-003-01-memory-blade.html",
            "MAW-W-003 — No extract (retracted Memory Blade)",
            "Weapon",
            "The wiki filed <strong>Memory Blade</strong> here as a filament rapier from “SE-003 The Thread of Memory.” That entity name is false. SE-003 is the Wilderness Tide, Place-Weight, Outside Sorrow, no extractable M.A.W. The Memory Blade filename is a misfile of SE-009’s Forgotten set.",
        ),
        (
            "maw/maw-s-003-01-tide-cloak.html",
            "MAW-S-003 — No extract (retracted Tide Cloak)",
            "Suit",
            "<strong>Tide Cloak</strong> was a placeholder suit on this URL. A Place-Weight surge at the wall does not yield a wearable. Residue is measured in millimeters of salt and dissolved fragments, not in cloth. Extraction activity is forbidden under Collapse / Drowned City protocol.",
        ),
        (
            "maw/maw-g-003-01-memory-thread-needle.html",
            "MAW-G-003 — No extract (retracted Memory Thread Needle)",
            "Gift",
            "<strong>Memory Thread Needle</strong> was a gift stub pointing at the same false “Thread of Memory.” Insight-work bonuses do not drop from a wilderness pressure line. If you need a memory gift, use <a href=\"maw-g-009-01-the-forgotten-mask.html\">Forgotten Mask</a>.",
        ),
    ]
    for rel, title, kind, lead in pages:
        body = f"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>{lead}</p>
<p>This URL is kept so old links do not 404. It is not an equipment sheet. It is the retraction.</p>
</section>
<section class="wiki-section" id="why"><h2 class="section-title">Why SE-003 yields nothing</h2>
<p>The Tide is not one person’s grief in a body. It is unstructured Han beyond the wall — a world never organized into names. Mellda’s card: Object/Place, Place-Weight, Coherence V Sovereign, Potency γ Major, Element Weight Black, form 3–15 m, Observation Level 5, <strong>M.A.W. Status: No extractable M.A.W.</strong></p>
<p>Viderehan maps. Ferrehan holds the line. Flerehan is invalid (no individual grief). Pugnahan is invalid (no personality). You cannot forge a personality’s weapon from a weather.</p>
</section>
<section class="wiki-section" id="protocol"><h2 class="section-title">Border protocol, not arsenal</h2>
<p>Watchtower scale runs Green → Amber → Red → Black → Collapse. Residue depth is the after-action unit. A {kind.lower()} extract is not on that list. During Collapse, no extraction activity is permitted at all.</p>
{common_tail}
</section>
"""
        SEARCH_UPDATES.append(
            put(
                rel,
                title,
                "SE-003 Wilderness Tide has no extractable M.A.W. This slot is a retracted misfile.",
                f'<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">M.A.W.</a> <i>/</i> <span>{title}</span>',
                title,
                f"M.A.W. · {kind.upper()} · RETRACTED",
                [("overview", "Overview"), ("why", "Why SE-003 yields nothing"), ("protocol", "Border protocol")],
                body,
                '<a href="index.html">M.A.W.</a> | <a href="../entities/se-003-the-wilderness-tide.html">SE-003</a> | <a href="maw-w-009-01-the-forgotten-lens.html">Forgotten Lens</a>',
                "SE-003 Wilderness Tide no extractable MAW retracted Memory Blade Tide Cloak",
            )
        )


def expand_short_mechanics():
    """Grow remaining short protocol pages without inventing Wings lore."""
    panic = DOCS / "mechanics" / "panic-states-and-corrosion.html"
    t = panic.read_text(encoding="utf-8")
    extra = """
<section class="wiki-section" id="source-note">
<h2 class="section-title">How this sits in canon</h2>
<p>Panic is an agent failure state, not an Ordeal and not a Sorrow Entity. SP tracks Clarity. White/Black Han and witnessed breaches drain it. At 0 the four behaviors (murderous, suicidal, wandering, helpless — names as already tabled) take the body. M.A.W. Corrosion is a separate track: equipment that has drunk too much of its donor entity starts writing that entity’s habit onto the wearer.</p>
<p>Remedy is rest, transfer off the floor, and in extreme cases Core-adjacent counseling — not a Memory Wash. Washers erase; they do not restore SP. Keepers can store a panic memory; they should not be asked to delete it as treatment. See <a href="han-energy-and-damage.html">Han damage</a> and <a href="../maw/maw-crafting-and-extraction.html">M.A.W. extraction</a>.</p>
<p>Do not confuse facility Panic with city Fracture. Fracture is a person becoming Han-structure. Panic is still a person, briefly unusable. An untreated panic loop is one of the documented roads into Fracture, which is why Internal Affairs and Insight Forge share the after-action.</p>
</section>
"""
    if 'id="source-note"' not in t:
        t = t.replace("</article>", extra + "</article>") if "</article>" in t else t.replace("</main>", extra + "</main>")
        panic.write_text(t, encoding="utf-8")
        print("expanded panic", words(t), "w")

    for rel, blurb in [
        (
            "departments/core-suppression-guidelines.html",
            """
<section class="wiki-section" id="source-note">
<h2 class="section-title">Scope</h2>
<p>Core Suppression is an Echo-Core event on one floor, analog to a Sephirah meltdown only as a <em>structure</em> (one patron, one department, one ideological fracture). It is not a Facility Meltdown and not an Ordeal Watch. Majin’s floor goes nihilistic-silent; other Cores have their own listed debuffs on this page’s table. Daily Recordings and Absolvohan cycles stay on <a href="../lore/the-cycle-and-absolvohan.html">the Cycle</a> — do not paste Day 1–50 onto this URL.</p>
<p>Suppression is trauma confrontation inside a Core’s dream-construct of their department. M.A.W. still works. Ordeals can overlap and should be treated as a second problem, not as the Core. See <a href="facility-meltdown-procedures.html">facility meltdown</a> when more than one floor is gone.</p>
</section>
""",
        ),
        (
            "departments/facility-meltdown-procedures.html",
            """
<section class="wiki-section" id="source-note">
<h2 class="section-title">Scope</h2>
<p>Facility Meltdown is all eight floors at once — Han-flux over threshold, lifts locking down, Floor 1 bunkers for non-combat staff. It is not one Core’s dream-construct and not a Tide Watch, though a Tide Watch can <em>cause</em> it. Code Meltdown Level IV is the civilian-evac line.</p>
<p>Border (Zone E) can be in Collapse from <a href="../entities/se-003-the-wilderness-tide.html">Wilderness Tide</a> at the same time. Those are different commands. Do not send Border Shield teams to Floor 4 Insight because the alarm color looked similar. See <a href="core-suppression-guidelines.html">Core suppression</a> and <a href="../mechanics/ordeals-framework.html">Ordeals</a>.</p>
</section>
""",
        ),
        (
            "maw/maw-crafting-and-extraction.html",
            """
<section class="wiki-section" id="source-note">
<h2 class="section-title">Registry rule</h2>
<p>Extraction is a separate risk event, not a work-cycle reward. SE-003 Wilderness Tide has <strong>no extractable M.A.W.</strong> — the W/S/G-003 URLs on this wiki are retractions. Real sets in the Codex follow the donor entity: Lament’s Requiem (001), Mourning Maul (002), Embrace Fang (005), Hope Lens (007), Forgotten Lens (009), Absolute Maul (010), Listening Requiem (011), Debt Lens (014), Balance Lens (015).</p>
<p>Do not generate 1,196 registry HTML files. This page is the forging rule: research level, Han flux cost, stat gate, per-cycle limit. Individual sheets stay on their MAW-W/S/G articles. See <a href="index.html">M.A.W. hub</a>.</p>
</section>
""",
        ),
    ]:
        p = DOCS / rel
        t = p.read_text(encoding="utf-8")
        if 'id="source-note"' not in t:
            t = t.replace("</article>", blurb + "</article>") if "</article>" in t else t.replace("</main>", blurb + "</main>")
            p.write_text(t, encoding="utf-8")
            print("expanded", rel, words(t), "w")


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
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("search entries", len(data))


def main():
    council()
    collectors()
    weavers()
    wardens()
    orphan_bell()
    hollow_glass()
    library()
    wars()
    three_ops()
    strip_han_dump()
    maw_003()
    expand_short_mechanics()
    patch_search()
    print("batch2 done")


if __name__ == "__main__":
    main()
