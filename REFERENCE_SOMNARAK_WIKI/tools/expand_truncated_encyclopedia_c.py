#!/usr/bin/env python3
"""Second-pass expansion. 100–300+ is a FLOOR, not a cap. Pull remaining source."""
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


def collectors():
    body = r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The <strong>Collectors</strong> (수금가 — Sugeumga; 추징) are Somnarak’s debt guild. Power is economic: karmic obligation, Echoes, payment. Headquarters: the Collector’s Spire, Zone C, SECTOR-C-01, under the Head Collector (추징장 — Chujingjang), a Council seat. Philosophy: <em>“Debts must be paid. This is not cruelty — it is balance.”</em> They are the most feared civic guild. Citizens avoid them. Architects shelter debtors. Debt Brokers undercut them. They are not Keepers and not Washers.</p>
<p>Every action in a Han-structural city writes a debt in the Abyss. Debts show up as aging, illness, bad luck, transformation, or a street that will not open. They can be transferred (the powerful shift them onto the weak), deferred (interest is more sorrow), inherited (parent to child), or paid (suffering, sacrifice, Echoes). Resonance: <strong>The Scales</strong> — see <a href="../mechanics/taboo-resonance-mechanics.html">Resonances</a>. The Ledger is kit. The Scales is the body.</p>
</section>
<section class="wiki-section" id="work"><h2 class="section-title">Work and structure</h2>
<p>Track and collect karmic debts. Enforce the Cycle of Debt. Regulate the Echo economy against inflation, counterfeiting, and hoarding. Pursue evaders. The Head Collector sits on the Council and is still the person the Palace cannot tax without asking.</p>
<p>Line: Head Collector → Senior Collectors (zone) → Collectors (field) → Assessors → apprentices. Beside the line: the <strong>Debt Registry</strong> (who owes, how much, to whom) and the <strong>Pursuit Division</strong> (specialists in tracking people who thought Zone E would save them).</p>
<p>Trade: citizens give Echoes for “debt management.” The Directorate trades entity data for Echo funding and guards the rest; Collectors have tried to hack those systems twice. They pay Wardens a secret extra budget for muscle. They tried to monetize Dream-diving; Weavers refused. Alliance with the Council is economic policy with a reversed power dynamic: Collectors hold more Echoes than the Palace.</p>
<p>Tension, in their own mouths: Architects — <em>“You build shelters for those who should be paying.”</em> Council — <em>“You are too lenient.”</em> Citizens — <em>“You take what little we have.”</em> Keepers — <em>“You erase people’s pasts to pay their debts. Who are they when they have nothing left?”</em> The Head must balance enforcement with mercy or the city turns. Some Collectors believe in the system. Others are disillusioned. Bong was one of the honest ones; the guild fired him for reporting phantom debt three times. See <a href="../locations/the-hollow-glass.html">the Hollow Glass</a>.</p>
</section>
<section class="wiki-section" id="debt"><h2 class="section-title">The Cycle of Debt</h2>
<p>Debt is not a metaphor. Every action creates an obligation in the Abyss that is physical, measurable, and enforceable.</p>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>Action</th><th>Debt created</th><th>Payment</th></tr></thead>
<tbody>
<tr><td>Living (daily)</td><td>Small — ambient</td><td>Paid by existing in the city</td></tr>
<tr><td>Using M.A.W.</td><td>Moderate — per use</td><td>Emotional / physical toll</td></tr>
<tr><td>Causing harm</td><td>Large — proportional</td><td>Karmic balance</td></tr>
<tr><td>Creating sorrow</td><td>Massive — amplified</td><td>Suffering or Echoes</td></tr>
<tr><td>Refusing to pay</td><td>Accumulates — interest</td><td>The Collectors come</td></tr>
</tbody></table></div>
<p>Manifestation: physical (aging, illness, weakness), emotional (numbness, despair, rage), metaphysical (bad luck, attracting Sorrow Entities), structural (buildings crack, paths close). Echoes (메아리 — Meori) are crystallized fragments of memory and emotion — the currency the guild prices. Common sorrow is grey and cheap. Genuine joy is gold and rare. First sorrow is black and not for sale. Uses: trade, consumption (addictive), refinement, M.A.W. fuel, dark-market harvest.</p>
</section>
<section class="wiki-section" id="tools"><h2 class="section-title">Tools</h2>
<p><strong>Debt-Ledger</strong> (부채 장부 — Bicheo Jangbu): a book of thin Han-crystal sheets. Debts display as weight — numbers, graphs, feeling. Scan a person. Transfer, payment, deferral go through it. Unique trait: it <em>judges</em>. Open it with malice and the pages show the Collector’s own debts.</p>
<p><strong>Extraction Glove</strong> (추출 장갑 — Chuchul Janggap): dark Han-crystal, elongated fingers, palm glow. Draws Echoes through the palm. Painless, exhausting. The Collector feels a fragment of the debtor’s sorrow. Some go numb. Some break. That feeling is the Scales Resonance wearing a glove.</p>
<p>Related entities, not standard kit: <a href="../entities/se-014-the-debt-eater.html">SE-014 Debt Eater</a> consumes debt and leaves the person hollow. <a href="../entities/se-015-the-debt-scale.html">SE-015 Debt Scale</a> sits in Collector mythology and containment. Source also names “the Scales” as a measuring tool; do not confuse that handheld with the Resonance or with SE-015.</p>
</section>
<section class="wiki-section" id="row"><h2 class="section-title">Collector’s Row</h2>
<p><a href="../locations/zone-c-collectors-row.html">Collector’s Row</a> (추징자 거리) is mid Zone C. Han signature: Grudge + Weight. About 12,000 Collectors, assessors, scribes, debt-workers. Buildings are tall, dark, narrow-windowed. The Debt Registry dominates. Scales are displayed everywhere. The air is heavy the way moisture is heavy. Citizens do not come here unless they owe, or are paying for someone who does. Veil/Raw split is 80/20 — the Veil is strong, but debt seeps.</p>
<p>Chunhwa the Debt Widow (빚의 과부) stands outside every day with a sign: <em>“My husband paid his debt. Why does yours keep growing?”</em> Thirty years of payment; reclassified as compound interest; he Fractured from <em>relief</em> — joy at being free, not grief. The kindness protocol — for citizens who are truly desperate — exists on paper and is never used.</p>
<p>Story hook in source: the Registry develops a glitch — debts transferred without consent, to people who do not exist. Phantom obligation is already Fray work (Debt Brokers). Taboo 5 is the line Collectors brush when they invent obligation. The city has not called that a Taboo case yet.</p>
</section>
<section class="wiki-section" id="fall"><h2 class="section-title">If the Collectors fall</h2>
<p>Trigger in source: a Fray uprising destroys the Debt Registry — all records lost. No enforcement; Echoes lose backing; Council taxation fails; citizens are “free” and without structure. Who fills the void: Debt Brokers take the economy, the Council invents a new system, the R.D. starts taking Echoes direct. Collapse trigger also named: a Head who hoards all Echoes, or a debt system nobody can pay. Question: <em>“If no one owes anything, is the city free — or is it lost?”</em></p>
</section>
"""
    put(
        "factions/the-collectors.html",
        "The Collectors",
        "Sugeumga debt guild — Cycle of Debt, Echoes, Debt-Ledger, Extraction Glove, Scales Resonance, Collector’s Spire and Row.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Factions</a> <i>/</i> <span>The Collectors</span>',
        "The Collectors",
        "FACTION · ZONE C · DEBT",
        [
            ("overview", "Overview"),
            ("work", "Work and structure"),
            ("debt", "Cycle of Debt"),
            ("tools", "Tools"),
            ("row", "Collector’s Row"),
            ("fall", "If they fall"),
        ],
        body,
        '<a href="index.html">Factions</a> | <a href="../mechanics/taboo-resonance-mechanics.html">Resonances</a> | <a href="../locations/zone-c-collectors-row.html">Zone C</a>',
        "Collectors Sugeumga Chujingjang Debt-Ledger Extraction Glove Scales Chunhwa Echoes Cycle of Debt",
    )


def weavers():
    body = r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The <strong>Weavers</strong> (직공 — Jikgong; Head 직녀장 — Jiknyeojang) are the Dream guild. Power is oneiric: Somnus, visions, the sleep/street boundary. Headquarters: Spire of Dreams, Building 4 of the Alpha Tree, south point of Zone A — glass that shows illusions; reality bends at its edges. Philosophy: <em>“The Dream is not illusion. It is the world’s true face — we are the dream.”</em> Source calls them the most mysterious faction.</p>
<p>The Council distrusts Dream influence. Citizens fear them as sorcerers who play with minds. Wardens do not trust Dream work. Architects ignore them (physical vs Somnus) and get ignored back. Keepers rival them on memory (Archive vs Dream) and still run a secret exchange. The Directorate cooperates — Dream Chambers, watch on the Absolvohan. Resonance: <strong>The Dream</strong>.</p>
</section>
<section class="wiki-section" id="somnus"><h2 class="section-title">Somnus</h2>
<p>The Dream Realm is not a separate world. It is the <strong>subconscious layer</strong> of this one. Emotions are objects. Memories are rooms. Desires are bodies. Time stretches: minutes on the street can be hours inside. Depth is danger. Echoes of the Before-Time live there, distorted. Layer map: <a href="../lore/the-dream-realm.html">Dream realm</a>.</p>
<p>What they do: manage the Dream/physical boundary; monitor and contain Dream entities; run dives for research or retrieval; study how Han moves through the mind. Free consultations exist. Almost nobody accepts. They have seen the Council fall and the debt system collapse in vision and have not filed those reports. They have designed Dream-spaces Architects could build if Architects asked. They have accessed memories Keepers thought sealed.</p>
<p>The Weaver’s dilemma, named in source: the Dream contains truths and also lies. Dream-diving is addictive — it shows you what you want to see. Some Weavers live more in Somnus than on the street. <em>Is the Dream a tool — or a trap?</em></p>
</section>
<section class="wiki-section" id="work"><h2 class="section-title">Work and structure</h2>
<p>Line: Head Weaver → Senior Weavers (zone monitors) → Weavers → Dream Divers → apprentices. Beside: <strong>Entity Division</strong> (study, contain, speak with Dream beings), <strong>Boundary Corps</strong> (the barrier between Dream and street), <strong>Interpretation Bureau</strong> (symbols, visions, prophecies).</p>
<p>Partnerships with Dream entities exist. Trust is fragile. Dream extraction pulls objects or information out — what comes out may not be what you asked for. The Whisper-Thread, the city’s quiet communication, fails if the Spire falls; that is why a Weaver collapse is not only a guild problem.</p>
</section>
<section class="wiki-section" id="tools"><h2 class="section-title">Tools</h2>
<p><strong>Dream Loom</strong> (꿈 베틀 — Kkum Betel): a frame of crystallized Dream that never holds one shape. Threads of light. Stretch them and pull objects, information, or entities out of Somnus — or send memories, messages, warnings in. Unique trait: idle, the Loom dreams on its own threads. Watching it is addictive.</p>
<p><strong>Resonance Mask</strong> (공명 가면 — Gongmyeong Gamyeon): crystallized reality, warm, humming. Clear-crystal eyes see Dream and street at once. Anchors identity so the diver does not dissolve; yanks them back if they go too deep. Remembers every Dream the wearer entered. Touch it to revisit. That is the trap.</p>
</section>
<section class="wiki-section" id="not"><h2 class="section-title">Not SE-009, not Taboo 4</h2>
<p><a href="../entities/se-009-the-memory-weaver.html">SE-009 The Memory Weaver</a> is a Sorrow Entity in the <a href="../locations/the-library-of-stolen-pasts.html">library of stolen pasts</a>. The guild is living people with looms. Accessing Dream-echoes of the past is not time reversal (Taboo 4 grey area). The city says so. The distinction is load-bearing.</p>
<p>If they fall: a Dream entity takes the Spire and traps the guild — Dream bleeding into the street, Dream entities walking, Whisper-Thread down, citizens hallucinating. Who fills the void: R.D. Dream-containment, Keepers on the boundary, civilians on Memory Anchors. Question: <em>“If the Dream is uncontrolled, does the city wake up — or does it fall asleep forever?”</em> See <a href="../mechanics/taboo-resonance-mechanics.html">Resonances</a>.</p>
</section>
"""
    put(
        "factions/the-weavers.html",
        "The Weavers",
        "Jikgong Dream guild — Spire of Dreams, Somnus, Loom, Resonance Mask, Dream Resonance.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Factions</a> <i>/</i> <span>The Weavers</span>',
        "The Weavers",
        "FACTION · ZONE A · DREAM",
        [
            ("overview", "Overview"),
            ("somnus", "Somnus"),
            ("work", "Work and structure"),
            ("tools", "Tools"),
            ("not", "Not SE-009"),
        ],
        body,
        '<a href="index.html">Factions</a> | <a href="../lore/the-dream-realm.html">Dream realm</a> | <a href="../mechanics/taboo-resonance-mechanics.html">Resonances</a>',
        "Weavers Jikgong Dream Loom Resonance Mask Spire Somnus Jiknyeojang",
    )


def wardens():
    body = r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The <strong>Wardens</strong> (수호자 — Suhuja) are Somnarak’s military and street order. Power is force: patrols, Zone E against the Desolate, Fracture and overflow. Headquarters: Warden’s Citadel, Zone C Warden Quarter, Head Warden (수호장 — Suhujang). Philosophy: <em>“We protect the city from itself — and from what lies beyond.”</em> Citizens respect them and do not love them. Frays treat them as the primary threat. Giltong run parallel Taboo enforcement. Judexhan are the Council’s sharper edge when streets are not enough.</p>
<p>They have disobeyed Council orders twice, both times to protect citizens. Architects make walls and gaps. Collectors rent them. Resonance: <strong>The Barrier</strong> — the Veil is thousands of Warden fields. If they stop, the Veil fails.</p>
</section>
<section class="wiki-section" id="work"><h2 class="section-title">Work and structure</h2>
<p>Public order (police, patrols, dispute resolution). Border defense, especially Zone E. Han-overflow response: contain, evacuate, stabilize. Council decree enforcement, with force if necessary. They are the city’s shield. Violence in a Han-structural city writes more sorrow. That is the daily bind.</p>
<p>Line: Head Warden → five Zone Commanders → Sector Captains → Wardens → recruits. Arms: <strong>Border Corps</strong> (Zone E, worst posting, most honest), <strong>Containment Squad</strong> (Fracture and Sorrow-Wrought), <strong>Internal Affairs</strong> (monitors Warden corruption — named as rampant in source).</p>
<p>The Directorate uses them as facility security and pulls them out of entity breaches more often than after-action admits. Architect construction zones have been unofficial training grounds. Tension: Architects — <em>“Your construction zones create security gaps.”</em> Collectors — <em>“We need your muscle, but you resent being used.”</em> Citizens — <em>“You protect us — but from what? From ourselves?”</em> Council — <em>“You enforce our decrees — but do you believe in them?”</em></p>
</section>
<section class="wiki-section" id="tools"><h2 class="section-title">Tools</h2>
<p><strong>Barrier Baton</strong> (방벽 지팡이 — Bangbyeok Jipangi): reinforced Han-crystal, warm, tip-glow. Projects a small suppression field — shield, barrier, or dampening zone — or a strike with held-down sorrow. Strength tracks calm. Unique trait: the baton <em>absorbs</em> what it suppresses. A veteran’s baton is emotionally dense. Cost of the Resonance: numbness. Oldest Wardens enforce a hush they cannot feel.</p>
<p><strong>Watchtower Eye</strong> (감시탑의 눈 — Gamsitap-ui Nun): head-sized crystalline sphere on Zone E towers. Scans the Desolate for Han-flow, entities, movement; alerts red. Unique trait: it sees emotional intensity, not only bodies. A frightened crowd registers differently than a calm patrol.</p>
<p>Also issued: temporary Han-suppression gear (dampens, does not delete), Fracture dampeners that slow and do not stop. See <a href="../entities/se-003-the-wilderness-tide.html">SE-003 Wilderness Tide</a> and <a href="../locations/zone-e-perimeter-bulwark.html">Zone E</a>.</p>
</section>
<section class="wiki-section" id="dilemma"><h2 class="section-title">Dilemma</h2>
<p>Do they serve the city or the Council? Internal corruption is named. Neutral ground with Frays exists only at <a href="../locations/the-hollow-glass.html">the Hollow Glass</a>. Taboo 6 is why the wall must not become a merge. Mellda’s personal Outside Sorrow is that Taboo’s grey area, not a Warden policy.</p>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>Faction</th><th>Dynamic</th></tr></thead>
<tbody>
<tr><td>Council</td><td>Dependence — Wardens enforce decrees, not always believing them.</td></tr>
<tr><td>Architects</td><td>Tension — construction zones are security gaps; unofficial training grounds.</td></tr>
<tr><td>Collectors</td><td>Dependence — extra budget for muscle; Wardens resent being rented.</td></tr>
<tr><td>Keepers</td><td>Neutral on paper; misconduct files sit forgotten.</td></tr>
<tr><td>Weavers</td><td>Distrust of Dream work.</td></tr>
<tr><td>R.D.</td><td>Supportive security; pulled into breaches more than after-action admits.</td></tr>
<tr><td>Giltong</td><td>Parallel enforcement — Taboos vs streets.</td></tr>
<tr><td>Frays</td><td>Hostile — Wardens are the primary threat.</td></tr>
<tr><td>Citizens</td><td>Respected, not loved.</td></tr>
</tbody></table></div>
<p>If they fall: a Desolate incursion overwhelms Zone E. The border collapses. Outside Sorrow floods. Zone E becomes a war zone. The Veil generators shut down. Citizens go unprotected. Who fills the void: Judexhan deploy, R.D. emergency protocols, civilians arm themselves, the Desolate expands. Question: <em>“If the wall falls, does the city survive — or does the wilderness consume it?”</em></p>
</section>
"""
    put(
        "factions/the-wardens.html",
        "The Wardens",
        "Suhuja military guild — Citadel, Barrier Baton, Watchtower Eye, Veil fields, Zone E Border Corps.",
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
        '<a href="index.html">Factions</a> | <a href="../locations/zone-e-perimeter-bulwark.html">Zone E</a> | <a href="../mechanics/taboo-resonance-mechanics.html">Resonances</a>',
        "Wardens Suhuja Barrier Baton Watchtower Eye Veil Zone E Border Corps",
    )


def keepers():
    body = r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The <strong>Keepers</strong> (기록관 — Girokgwan) are Somnarak’s memory guild. Power is information: Grand Archive (Building 2, Zone A, northeast of the Tree), Echo vaults, which past is still speakable. Head Keeper (기록장 — Girokjang) is a Council seat. Philosophy: <em>“We hold what would otherwise be lost. This is not power — it is responsibility.”</em> Source calls them the guardians of identity.</p>
<p>They are not <a href="the-memory-washers.html">Washers</a>. Washers erase. Keepers store. They are not Weavers. Weavers walk Somnus; Keepers walk shelves — though some shelves extend into Dream-space. Resonance: <strong>The Archive</strong> — crystallize sorrow into Echoes, pay with self.</p>
</section>
<section class="wiki-section" id="archive"><h2 class="section-title">The Grand Archive</h2>
<p>Second-largest building in Zone A. Vast, labyrinthine, whispered. The air tastes of old tears. It extends deep underground — oldest records in the lowest vaults. Shelves extend into Dream-space; some records exist only partly on the street. The building is <em>alive</em>: it answers to feeling. Walk in angry and the Index will not help.</p>
<p>What they do: preserve history (records, memories, artifacts); maintain Echo vaults; research, translation, verification; legal extraction, storage, imperfect restoration; memory-related transactions the Council pretends are not a market. Deep vaults hold Cheongula causation — the truth that could unseat the Council. Keepers have those records and choose not to release them. Preserve history, or control it?</p>
<p>Related geography, not the same room: the Memory Archive under the Tree is a hungry Place that consumes visitors as stories. Grand Archive is the guild’s public face. Oldest Keepers remember the city and forget their names. See <a href="../lore/the-alpha-tree.html">Alpha Tree</a>.</p>
</section>
<section class="wiki-section" id="work"><h2 class="section-title">Work, structure, tools</h2>
<p>Line: Head Keeper → Senior Archivists (zone curators) → Archivists → Scribes → apprentices. Beside: <strong>Memory Division</strong> (extraction, storage, restoration), <strong>Vault Guard</strong> (deepest, most dangerous records), <strong>Verification Bureau</strong> (authenticity of records and memories).</p>
<p><strong>Memory Lens</strong> (기록 렌즈 — Girok Renjeu): a monocle of crystallized memory. An Echo near it plays as sight, sound, and feeling. Compare two memories and contradictions light. Unique trait: the lens <em>remembers the viewer</em>. Look too often and it mixes the Keeper’s own past into the playback. The boundary between self and other blurs.</p>
<p><strong>Whispering Index</strong> (속삭임 색인 — Soksagim Saegin): not one device — Han-crystal threads through the Archive. Touch, ask, and it answers in whispers, riddles, fragments. Catalogs every Echo by emotion, date, source, content. Cross-references the unrelated. Some Keepers say it is alive. It talks constantly. Comforting. Maddening. Memory Fray has a copy of the index; the Keepers do not know.</p>
</section>
<section class="wiki-section" id="relations"><h2 class="section-title">Relations</h2>
<p>Council depends on Keepers for legitimacy and tells them some truths should stay buried. Architects clash over demolition of historic sites — preserve vs build. Collectors trade memories; Keepers recover stolen Echoes and keep them. Wardens: Warden misconduct sits filed and forgotten. Weavers: rivalry on the surface, secret exchange underneath. R.D. gets Cheongula-like event records. Frays: Memory Thieves and the Memory Fray steal from the Archive. Citizens trust Keepers with memory they thought lost.</p>
<p>If Keepers fall — Han-fire in the Grand Archive — Before-Time fragments die, the Maw’s secret dies, and the city asks whether an unremembered event happened. Who fills the void: Weavers try the Dream; the Directorate keeps what it already copied; citizens fall back on oral tradition. Taboo 4 is why the past is not a playground; the Archive is the city’s argument that the past must remain readable. Question: <em>“If no one remembers, did it happen — or does the city write a new history?”</em></p>
</section>
"""
    put(
        "factions/the-keepers.html",
        "The Keepers",
        "Girokgwan memory guild — Grand Archive, Memory Lens, Whispering Index, Archive Resonance.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Factions</a> <i>/</i> <span>The Keepers</span>',
        "The Keepers",
        "FACTION · ZONE A · GRAND ARCHIVE",
        [
            ("overview", "Overview"),
            ("archive", "Grand Archive"),
            ("work", "Work and tools"),
            ("relations", "Relations"),
        ],
        body,
        '<a href="index.html">Factions</a> | <a href="the-memory-washers.html">Washers</a> | <a href="../mechanics/taboo-resonance-mechanics.html">Resonances</a>',
        "Keepers Girokgwan Grand Archive Memory Lens Whispering Index Archive Resonance",
    )


def washers():
    body = r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The <strong>Memory Washers</strong> (기억 세척자) are not the Keepers. Keepers preserve. Washers erase. They are a Fray operation in Zone B and C — the Wash District — and the subject of UCD Arc 2. The old wiki pasted Keeper lore onto this URL. That paste is gone.</p>
<p>A wash-rig strips a memory from a living person and sells the remainder. Victims keep walking. They cannot say what was taken. Collectors hate them because washed debt is hard to prove. Keepers hunt them because the Archive is supposed to be the only legal memory store. Taboo 5’s grey area: the sorrow they sell is real, only extracted. The city has not called the Wash District a synthesis case. UCD still raids them for crime.</p>
</section>
<section class="wiki-section" id="rig"><h2 class="section-title">The Wash-Rig</h2>
<p><strong>Wash-Rig</strong> (세척 장치 — Sejeok Jangchi): a chair with Han-crystal headrest, armrests, footrests. The crystal glows when active. The target is strapped in. The rig resonates with the target’s memory-Echoes. Specific memories are pulled out as crystallized Echoes. The person forgets — blank spots where a childhood, a debt, a face used to be. Extracted Echoes are collected and sold.</p>
<p>Unique trait: the rig <em>remembers what it erases</em>. Stolen memories sit in the crystal. Some rigs have centuries of other people’s lives embedded in them. The rigs whisper at night. A wash-rig is not a Memory Lens. A Harvest Hook is not an Extraction Glove. Do not mix them on a loadout screen.</p>
<p>A wash does not make a Sorrow Entity. It makes a person who can Fracture later because the grief has nowhere to sit. If they cross into manufacturing hollow Han, that is Taboo 5 and <strong>Synthetics</strong> — the case file where the product fought back. The Directorate files ordinary washes under crime, not SECC.</p>
</section>
<section class="wiki-section" id="place"><h2 class="section-title">Place in the underworld</h2>
<p>Filed with the Memory Fray / Memory Cartel (기억 카르텔), territory Zone B + C, specialty memory trafficking. Leader-title in the Fray table: “The Index,” a former Keeper. UCD treats Washers as a raid target, not a Council guild. Hierarchy of a Fray: Boss → Lieutenants → Operators → Runners, plus Associates (freelancers, informants).</p>
<p>Related Frays: Harvesters (Zone B, forced Echo extraction, “The Farmer”), Debt Brokers (Zone C, debt trading including inherited debt, “The Scales” — a former Collector), Veil Merchants (Zone D, counterfeit Veil, “The Mask”), Entity Traders (Zone D+E, captured SEs, “The Cage” — a former R.D. researcher). Commodity on the Fray table: stolen Archive pages and washed civilian recollection — “varies — rare memories are priceless.” Keepers hunt you for this. Collectors hunt Harvesters. Wardens hunt everyone.</p>
<p>Underground rooms that move this cargo: the Hollow (Old Lament walls), the Scales (underground debt exchange under Collector’s Row), the Unmasked (Zone D identity market), the Gate’s Shadow, the Desolate Drift. Memory as a domain is controlled by Keepers and challenged by Memory Fray and Memory Thieves. See <a href="the-underworld-and-wound-walkers.html">Underworld</a>.</p>
</section>
<section class="wiki-section" id="ucd"><h2 class="section-title">UCD Arc 2</h2>
<p><a href="the-ucd-strike-force.html">Underworld Cleanup Descend</a> Arc 2 is the Wash District operation: victims, the wash-rig, the harvest, confrontation, choice, return. That Canto-style article keeps the chapter text. This page is who they are when they are not being raided.</p>
</section>
<section class="wiki-section" id="not-keepers"><h2 class="section-title">Not the Keepers</h2>
<p>Keepers preserve. Washers delete. Weavers walk the Dream. Collectors monetize obligation. Historical legitimacy and the Archive’s secret exchange with Weavers live on <a href="the-keepers.html">the Keepers</a>. Taboo 5 lives on <a href="../lore/the-seven-absolute-taboos.html">Taboos</a>.</p>
</section>
"""
    put(
        "factions/the-memory-washers.html",
        "The Memory Washers",
        "Fray memory-erasers of the Wash District. Wash-rig, Memory Cartel, UCD Arc 2. Not Keepers. Taboo 5 grey area.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Factions</a> <i>/</i> <span>Memory Washers</span>',
        "The Memory Washers",
        "FRAY · ZONE B+C · WASH DISTRICT",
        [
            ("overview", "Overview"),
            ("rig", "Wash-Rig"),
            ("place", "Place in the underworld"),
            ("ucd", "UCD Arc 2"),
            ("not-keepers", "Not the Keepers"),
        ],
        body,
        '<a href="the-keepers.html">Keepers</a> | <a href="the-underworld-and-wound-walkers.html">Underworld</a> | <a href="the-ucd-strike-force.html">UCD</a>',
        "Memory Washers Fray Wash District Wash-Rig UCD Arc 2 Taboo 5 Index Memory Cartel",
    )


def menders():
    body = r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p><strong>Menders</strong> (수선자 — Suseonja; also 땜장이 — Ttemjangii in the relations matrix) are independent operators, not a Council Head and not a seventh Resonance. They work the Raw — where Wardens will not go, where the R.D. does not reach, where Collectors are too slow. They fix, contain, protect, mediate. They report to both the <a href="the-architects.html">Architects</a> and the <a href="the-reverie-directorate.html">Directorate</a>. That split loyalty is named in source.</p>
<p>Why they exist: Wardens protect the Veil, not the Raw. The R.D. contains Sorrow Entities, not everyday cracks. Collectors enforce debt, they do not help. Architects build, they do not repair. Menders fill the gaps.</p>
</section>
<section class="wiki-section" id="services"><h2 class="section-title">Services</h2>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>Service</th><th>What it is</th><th>Payment</th></tr></thead>
<tbody>
<tr><td>Repair</td><td>Fix damaged buildings, reinforce Han structures</td><td>Echoes</td></tr>
<tr><td>Containment</td><td>Minor Sorrow Entities the R.D. will not schedule</td><td>Echoes + entity rights</td></tr>
<tr><td>Mediation</td><td>Disputes between citizens, factions, districts</td><td>Echoes or favors</td></tr>
<tr><td>Protection</td><td>Guard people or rooms in the Raw</td><td>Echoes</td></tr>
<tr><td>Retrieval</td><td>Lost people, stolen items, missing memories</td><td>Echoes + information</td></tr>
<tr><td>Fracture response</td><td>Arrive before the Wardens</td><td>Echoes + risk</td></tr>
<tr><td>Escort</td><td>Through the Raw or the Desolate</td><td>Echoes</td></tr>
</tbody></table></div>
</section>
<section class="wiki-section" id="ranks"><h2 class="section-title">Ranks and Marks</h2>
<p>Ranks run 7 (Novice — basic Han sensing, small shops) through 6 Journeyman, 5 Adept, 4 Veteran (R.D. contracts), 3 Expert (Council / R.D.), 2 Master (M.A.W. proficiency), 1 Grandmaster (near-Architect, only the most dangerous contracts).</p>
<p>Above Rank 1 are the <strong>Marks</strong> — legendary names, a handful in the city’s history. A Mark is not a rank; it is a scar the city still uses as a name. Novices who chase a Mark instead of a crack do not last the Raw.</p>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>Mark</th><th>Status</th><th>Legend</th></tr></thead>
<tbody>
<tr><td>Grey Veil</td><td>Active</td><td>Can suppress an entire district’s sorrow. No one has seen their face.</td></tr>
<tr><td>Crimson Thread</td><td>Deceased</td><td>Died containing a Sovereign-class entity. Their M.A.W. is still active — bonded to no one.</td></tr>
<tr><td>Pale Witness</td><td>Missing</td><td>Entered the Dream and never returned. Some say they found the Before-Time.</td></tr>
<tr><td>Black Tide</td><td>Active</td><td>Works only in the Desolate. Knows Outside Sorrow the R.D. does not.</td></tr>
<tr><td>Golden Echo</td><td>Active</td><td>Trades memories not for profit but for redemption — returns lost recollection.</td></tr>
</tbody></table></div>
<p>Loose organizations, not a Council guild: the <strong>Mendery</strong> (Zone D contract hall, all grades, neutral ground), <strong>Raw Collective</strong> (refuse the Veil on principle), <strong>Threshold Walkers</strong> (Desolate escorts — they know it better than anyone), <strong>Veil Watchers</strong> (monitor Veil integrity, report to no one — and feed Giltong when a Taboo signature shows on a repair).</p>
</section>
<section class="wiki-section" id="tools"><h2 class="section-title">Kit and rod</h2>
<p><strong>Mender’s Kit</strong> (수선자 도구함 — Suseonja Doguhan): leather-and-crystal case — trowels, probes, gauges, sealant, Echo reserves, a small Sorrow Gauge. Tools answer the user’s feeling. Each kit personalizes until it is as distinct as a fingerprint.</p>
<p><strong>Repair Rod</strong> (수리 막대 — Suri Makdae): flexible Han-crystal, warm. Vibrates at cracks, fills them with the Mender’s own sorrow, reinforces weak spans, can be a weapon in an emergency. It remembers every repair. A veteran can walk the city by the rod’s map of failures. If the rod starts pulling toward the Desolate instead of a crack, stop. That is not a repair. That is a boundary (Taboo 6 adjacent).</p>
</section>
<section class="wiki-section" id="place"><h2 class="section-title">Place</h2>
<p>Alliance with the R.D. is field operations — unofficial contractors. Alliance with Architects is the same people on construction sites. Frays sometimes hire Menders, sometimes oppose them. Citizens pay Echoes for repair. Giltong treat them as witnesses, not hunters. Seol, in the Cast, is the youngest Mender who still repairs the Veil — a person page, not this guild.</p>
<p>They do not sit in the seven-note Resonance table. Shaping is Architects; Barrier is Wardens. Menders borrow both at street scale and pay in their own sorrow poured into other people’s walls. In the domain table: the Raw is Fray-local, challenged by individual Menders and by Wardens when they enter; debt is Collectors, challenged by Brokers, Debtless, and Menders. See <a href="faction-technology.html">faction technology</a> and <a href="the-underworld-and-wound-walkers.html">the Raw</a>.</p>
</section>
"""
    put(
        "factions/the-menders.html",
        "The Menders",
        "Independent Raw operators — services, ranks 7–1, five Marks, Mendery, kit, repair rod. Dual report to Architects and R.D.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Factions</a> <i>/</i> <span>Menders</span>',
        "The Menders",
        "INDEPENDENT · RAW · 수선자",
        [
            ("overview", "Overview"),
            ("services", "Services"),
            ("ranks", "Ranks and Marks"),
            ("tools", "Kit and rod"),
            ("place", "Place"),
        ],
        body,
        '<a href="the-architects.html">Architects</a> | <a href="the-reverie-directorate.html">Directorate</a> | <a href="faction-technology.html">Tech</a>',
        "Menders Suseonja Repair Rod Mendery Raw Collective Veil Watchers Marks Grey Veil",
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
    collectors()
    weavers()
    wardens()
    keepers()
    washers()
    menders()
    patch_search()
    print("expand C guilds done")


if __name__ == "__main__":
    main()
