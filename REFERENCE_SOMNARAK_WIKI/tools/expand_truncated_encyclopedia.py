#!/usr/bin/env python3
"""Expand pages truncated at ~300 words. 100–300+ is a MINIMUM, not a cap."""
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


def taboos():
    body = r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The <strong>Seven Taboos</strong> (일곱 금지 — Ilgop Geumji) are absolute prohibitions woven into Somnarak’s Han. They are not Council policy. They are not Warden standing orders. When one is broken, the <em>city</em> answers: buildings crack, streets shift, Sorrow Entities form, the offender’s debt skyrockets. The Council interprets what already happened. Giltong find the person. Judexhan judge when finding is not enough.</p>
<p><em>“Some things cannot be done. Not because they are difficult — but because the city will not allow it.”</em></p>
<p>This page is the seven laws — prohibit, why, city’s response, grey area. Enforcement guild: <a href="../factions/the-giltong-enforcers.html">Giltong</a>. Blade: <a href="../factions/the-judexhan.html">Judexhan</a>. Civic <em>powers</em> are <a href="../mechanics/taboo-resonance-mechanics.html">Resonances</a>, not Taboos. Do not paste Arbiter org-charts or Resonance tables here.</p>
</section>
<section class="wiki-section" id="one"><h2 class="section-title">1 — No Resurrection (부활 금지)</h2>
<p><em>“The dead do not return. To bring them back is to steal from the Maw.”</em> No one may reverse death or create a permanent copy of a deceased person. The Cheongula’s thousand stabilize the Alpha Tree. Returned dead would unseat that foundation. The city needs the dead to stay dead.</p>
<p>Break it: immediate karmic spike. The Maw activates — the thousand whisper louder, Zone B trembles. Extreme: the offender is consumed, dragged into the ground like the original thousand. Giltong response: containment plus Maw-activation assessment. Extreme severity.</p>
<p>Grey: Echo-Cores are Cast Effigies housing preserved consciousness, not graves emptied. The Council says that is not resurrection. The city has not punished them. Yet.</p>
</section>
<section class="wiki-section" id="two"><h2 class="section-title">2 — No True AI (진정한 인공지능 금지)</h2>
<p><em>“A machine that thinks as a human is a machine that can suffer as a human. We have enough suffering.”</em> No fully sentient artificial intelligence — independent thought, emotion, identity equal to a human. <a href="../characters/the-secretary-seiyon.html">Seiyon</a> is the proof and the warning: she feels, she suffers, she did not choose the role. The city does not want more of her on purpose.</p>
<p>Break it: erasure. The AI does not die; it unravels — memory corruption, personality fragmentation, dissolution. The Whispering Incident is the Giltong case: unknown maker, an AI that screamed, a whisper some say never stopped.</p>
<p>Grey: Seiyon is sentient and should not exist under a literal reading. She was not <em>created</em> sentient; she <em>became</em> so by accident. The Taboo prohibits deliberate creation. She is a loophole the city has not closed.</p>
</section>
<section class="wiki-section" id="three"><h2 class="section-title">3 — No Han Immunity (한 면역 금지)</h2>
<p><em>“No one is exempt from sorrow. To be immune is to be inhuman.”</em> No permanent immunity to Han, no zone completely free of sorrow. The Veil suppresses; it does not delete. The city needs citizens who can feel — that feeling is structure. An immune person cannot contribute. An immune zone is a zone that does not exist.</p>
<p>Break it: exile toward the Desolate. An immune zone destabilizes — cracks, Veil failure, Outside Sorrow in. The Immunity Cult still lives outside, unfeeling. High, not Maw-activation.</p>
<p>Grey: Research Lead Ayshuk cannot feel sorrow — Inner Sorrow taken by a Void entity. Empty is not blocked. The Taboo prohibits blocking, not absence. The city has not exiled them.</p>
</section>
<section class="wiki-section" id="four"><h2 class="section-title">4 — No Time Reversal (시간 역행 금지)</h2>
<p><em>“The past is written in Han. To rewrite it is to rewrite the city’s foundation.”</em> No reversing, altering, or erasing past events; no backward travel; no rewritten history. The Archive is every sorrow, death, Fracture. Change the past and the present’s walls have nothing to stand on. The Cycle already spent 1,778 years on a loop; private time-theft is not a second Absolvohan.</p>
<p>Break it: paradox. Reality destabilizes around the altered event. Entities form from the contradiction. Extreme: the area is unwritten — not destroyed, never-having-been. A Weaver who tried is frozen in one moment. Containment plus paradox assessment. Extreme.</p>
<p>Grey: Dream echoes of the past are recordings, not the past. Accessing Layer 2 is not time reversal. The city says so. The distinction is load-bearing.</p>
</section>
<section class="wiki-section" id="five"><h2 class="section-title">5 — No Sorrow Synthesis (한 합성 금지)</h2>
<p><em>“Sorrow cannot be manufactured. It can only be lived.”</em> No fabricating grief, inducing false trauma, or minting Han in a vat. The city is built on genuine grief. Artificial sorrow is hollow — no weight, no history. Replace the real with the fake and the walls go brittle.</p>
<p>Break it: rejection. The fake is expelled and becomes a Sorrow Entity — a hollow thing that eats real sorrow to fill itself. Source name: <strong>Synthetics</strong>, among the most dangerous in the city. The Memory Washers’ synthetic sorrow fought back; it had become sentient. High. Destruction of the product plus punishment.</p>
<p>Grey: Washers erase real memories and sell them as fuel. That is extraction, not creation. Collectors brush the line when they mint obligation that never existed. The city has not razed the Wash District for Taboo 5. UCD still raids them for crime.</p>
</section>
<section class="wiki-section" id="six"><h2 class="section-title">6 — No Cross-Boundary Fusion (경계 융합 금지)</h2>
<p><em>“City and wilderness do not merge. To fuse them is to unmake both.”</em> No permanent merge of structured Han (city) with unstructured Han (wilderness / UnWiHan). No making Outside Sorrow a civic building material. Zone E exists so this does not become policy.</p>
<p>Break it: fracture. The merged area splinters. Rules stop applying. A <strong>Fracture Zone</strong> is what remains. The Boundary Walker — a Desolate nomad — is the named case: containment, then a living wound. Extreme.</p>
<p>Grey: Border Lead Mellda carries an Outside Sorrow entity inside them. Personal, not structural. The Taboo prohibits fusing the city’s body with the wilderness, not a person who already walked out and came back carrying something.</p>
</section>
<section class="wiki-section" id="seven"><h2 class="section-title">7 — No Echo-Core Duplication (에코-코어 복제 금지)</h2>
<p><em>“Each Echo-Core is unique. To duplicate them is to split sorrow — and sorrow that is split is sorrow that is lost.”</em> No copy, duplicate, or second Cast Effigy identical to an existing Core. Each Core’s weight is a specific sorrow. Split it and both halves weaken.</p>
<p>Break it: fragmentation. Original and copy go unstable; identity dissolves; the copy never truly forms. The copy in the Giltong file screamed; it knew what it was. Extreme. Fragment the copy, investigate the maker.</p>
<p>Grey: Seiyon is a copy of Majin’s dead lover, not a copy of an Echo-Core. Duplicating people is Taboo 1’s neighbor; duplicating Cores is Taboo 7. The city accepts the technicality. Xeroxing Majin is not covered by that courtesy.</p>
</section>
<section class="wiki-section" id="summary"><h2 class="section-title">Summary</h2>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>#</th><th>Taboo</th><th>Prohibits</th><th>City’s response</th></tr></thead>
<tbody>
<tr><td>1</td><td>No Resurrection</td><td>Bringing back the dead</td><td>Maw activation, consumption</td></tr>
<tr><td>2</td><td>No True AI</td><td>Deliberate sentient machines</td><td>Erasure, dissolution</td></tr>
<tr><td>3</td><td>No Han Immunity</td><td>Blocking sorrow</td><td>Exile, destabilization</td></tr>
<tr><td>4</td><td>No Time Reversal</td><td>Altering the past</td><td>Paradox, unwriting</td></tr>
<tr><td>5</td><td>No Sorrow Synthesis</td><td>Manufacturing Han</td><td>Rejection, Synthetics</td></tr>
<tr><td>6</td><td>No Cross-Boundary Fusion</td><td>Merging city and wilderness</td><td>Fracture Zone</td></tr>
<tr><td>7</td><td>No Echo-Core Duplication</td><td>Copying a Core</td><td>Fragmentation, identity loss</td></tr>
</tbody></table></div>
<p>Giltong: one Senior per Taboo, Arbiter above, scanners, containment bonds, ~100 personnel, Council override on Taboo matters only. Cases live on their article. Resonances are how factions <em>touch</em> Han, not how the city forbids it.</p>
</section>
"""
    put(
        "lore/the-seven-absolute-taboos.html",
        "The Seven Taboos",
        "Seven Han-woven prohibitions: resurrection, true AI, immunity, time, synthesis, fusion, Core copies — prohibit, why, city’s response, grey area.",
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
            ("summary", "Summary"),
        ],
        body,
        '<a href="index.html">Lore</a> | <a href="../factions/the-giltong-enforcers.html">Giltong</a> | <a href="../mechanics/taboo-resonance-mechanics.html">Resonances</a>',
        "Seven Taboos Geumji Resurrection AI Immunity Time Synthesis Fusion Echo-Core Seiyon Ayshuk Mellda",
    )


def collectors():
    body = r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The <strong>Collectors</strong> (수금가 — Sugeumga; 추징) are Somnarak’s debt guild. Power is economic: karmic obligation, Echoes, payment. Headquarters: Collector’s Spire, Zone C, SECTOR-C-01, under the Head Collector (추징장), a Council seat. Philosophy: <em>“Debts must be paid. This is not cruelty — it is balance.”</em> Citizens avoid them. Architects shelter debtors. Debt Brokers undercut them. They are not Keepers and not Washers.</p>
<p>Every action in a Han-structural city writes a debt in the Abyss. Debts show up as aging, illness, bad luck, transformation. They can be transferred (the powerful shift them onto the weak), deferred (interest is more sorrow), or paid (suffering, sacrifice, Echoes). Resonance: <strong>The Scales</strong> — see <a href="../mechanics/taboo-resonance-mechanics.html">Resonances</a>.</p>
</section>
<section class="wiki-section" id="work"><h2 class="section-title">Work and structure</h2>
<p>Track and collect karmic debts, enforce the Cycle of Debt, regulate the Echo economy against inflation and counterfeiting, pursue evaders. Line: Head Collector → Senior Collectors (zone) → Collectors (field) → Assessors → apprentices. Beside the line: Debt Registry (who owes, how much, to whom) and Pursuit Division.</p>
<p>Trade: citizens give Echoes for “debt management.” The Directorate trades entity data for Echo funding and guards the rest; Collectors have tried to hack those systems twice. They pay Wardens a secret extra budget for muscle. They tried to monetize Dream-diving; Weavers refused. Alliance with the Council is economic policy with a reversed power dynamic: Collectors hold more Echoes than the Palace. Collapse trigger in source: a Head who hoards all Echoes, or a debt system nobody can pay.</p>
</section>
<section class="wiki-section" id="tools"><h2 class="section-title">Tools</h2>
<p><strong>Debt-Ledger</strong> (부채 장부): thin Han-crystal sheets. Debts display as weight — numbers, graphs, feeling. Scan a person. Transfer, payment, deferral go through it. Open it with malice and the pages show the Collector’s own debts.</p>
<p><strong>Extraction Glove</strong> (추출 장갑): dark Han-crystal, elongated fingers, palm glow. Draws Echoes through the palm. Painless, exhausting. The Collector feels a fragment of the debtor’s sorrow. Some go numb. Some break. That feeling is the Scales Resonance wearing a glove.</p>
<p>Related entities, not standard kit: <a href="../entities/se-014-the-debt-eater.html">SE-014 Debt Eater</a> consumes debt and leaves the person hollow. <a href="../entities/se-015-the-debt-scale.html">SE-015 Debt Scale</a> sits in Collector mythology and containment.</p>
</section>
<section class="wiki-section" id="row"><h2 class="section-title">Collector’s Row</h2>
<p>Zone C is their street. Chunhwa the Debt Widow stands outside every day with a sign: <em>“My husband paid his debt. Why does yours keep growing?”</em> Thirty years of payment; reclassified as compound interest; he Fractured from relief. The kindness protocol — for citizens who are truly desperate — exists on paper and is never used.</p>
<p>Taboo 5 (no sorrow synthesis) is the line Collectors brush when they invent obligation. The city has not called that a Taboo case yet. Debt Brokers already do the illegal version in the Frays. See <a href="../locations/zone-c-collectors-row.html">Zone C</a>.</p>
</section>
"""
    put(
        "factions/the-collectors.html",
        "The Collectors",
        "Sugeumga debt guild — Echoes, Debt-Ledger, Extraction Glove, Scales Resonance, Collector’s Spire.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Factions</a> <i>/</i> <span>The Collectors</span>',
        "The Collectors",
        "FACTION · ZONE C · DEBT",
        [("overview", "Overview"), ("work", "Work and structure"), ("tools", "Tools"), ("row", "Collector’s Row")],
        body,
        '<a href="index.html">Factions</a> | <a href="../mechanics/taboo-resonance-mechanics.html">Resonances</a> | <a href="../locations/zone-c-collectors-row.html">Zone C</a>',
        "Collectors Sugeumga Chujingjang Debt-Ledger Extraction Glove Scales Chunhwa",
    )


def weavers():
    body = r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The <strong>Weavers</strong> (직공 — Jikgong; Head 직녀장) are the Dream guild. Power is oneiric: Somnus, visions, the sleep/street boundary. Headquarters: Spire of Dreams, Building 4 of the Alpha Tree, south point of Zone A — glass that shows illusions. Philosophy: <em>“The Dream is not illusion. It is the world’s true face — we are the dream.”</em></p>
<p>The Council distrusts Dream influence. Citizens fear them. Wardens do not trust Dream work. Keepers rival them on memory (Archive vs Somnus) and still run a secret exchange. The Directorate cooperates — Dream Chambers, watch on the Absolvohan. Resonance: <strong>The Dream</strong>.</p>
</section>
<section class="wiki-section" id="work"><h2 class="section-title">Work and structure</h2>
<p>Manage the Dream/physical boundary, monitor Dream entities, run dives for research or retrieval, study how Han moves through the mind. Somnus is the subconscious layer of this world: emotions are objects, memories are rooms, desires are bodies. Time stretches. Depth is danger. Echoes of the Before-Time live there, distorted.</p>
<p>Line: Head Weaver → Senior Weavers → Weavers → Dream Divers → apprentices. Beside: Entity Division, Boundary Corps, Interpretation Bureau. Free consultations exist. Almost nobody accepts. They have seen the Council fall and the debt system collapse in vision and have not filed those reports. They have designed Dream-spaces Architects could build if Architects asked. They have accessed memories Keepers thought sealed.</p>
</section>
<section class="wiki-section" id="tools"><h2 class="section-title">Tools</h2>
<p><strong>Dream Loom</strong> (꿈 베틀): crystallized Dream that never holds one shape. Threads of light. Stretch them and pull objects, information, or entities out of Somnus — or send memories and warnings in. Idle, the Loom dreams on its own threads. Watching it is addictive.</p>
<p><strong>Resonance Mask</strong> (공명 가면): crystallized reality, warm, humming. Clear-crystal eyes see Dream and street at once. Anchors identity so the diver does not dissolve; yanks them back if they go too deep. Remembers every Dream the wearer entered. Touch it to revisit. That is the trap. Layer map: <a href="../lore/the-dream-realm.html">Dream realm</a>.</p>
</section>
<section class="wiki-section" id="not"><h2 class="section-title">Not SE-009, not Taboo 4</h2>
<p><a href="../entities/se-009-the-memory-weaver.html">SE-009 The Memory Weaver</a> is a Sorrow Entity in the library of stolen pasts. The guild is living people with looms. Accessing Dream-echoes of the past is not time reversal (Taboo 4 grey area). Collapse scenario: a Dream entity takes the Spire and traps the guild — Dream bleeding into the street. See <a href="../mechanics/taboo-resonance-mechanics.html">Resonances</a>.</p>
</section>
"""
    put(
        "factions/the-weavers.html",
        "The Weavers",
        "Jikgong Dream guild — Spire of Dreams, Loom, Mask, Somnus Resonance.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Factions</a> <i>/</i> <span>The Weavers</span>',
        "The Weavers",
        "FACTION · ZONE A · DREAM",
        [("overview", "Overview"), ("work", "Work and structure"), ("tools", "Tools"), ("not", "Not SE-009")],
        body,
        '<a href="index.html">Factions</a> | <a href="../lore/the-dream-realm.html">Dream realm</a> | <a href="../mechanics/taboo-resonance-mechanics.html">Resonances</a>',
        "Weavers Jikgong Dream Loom Resonance Mask Spire Somnus",
    )


def wardens():
    body = r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The <strong>Wardens</strong> (수호자 — Suhuja) are Somnarak’s military and street order. Power is force: patrols, Zone E against the Desolate, Fracture and overflow. Headquarters: Warden’s Citadel, Zone C Warden Quarter, Head Warden (수호장). Philosophy: <em>“We protect the city from itself — and from what lies beyond.”</em> Citizens respect them and do not love them. Frays treat them as the primary threat. Giltong run parallel Taboo enforcement. Judexhan are the Council’s sharper edge when streets are not enough.</p>
<p>They have disobeyed Council orders twice, both times to protect citizens. Architects make walls and gaps. Collectors rent them. Resonance: <strong>The Barrier</strong> — the Veil is thousands of Warden fields. If they stop, the Veil fails.</p>
</section>
<section class="wiki-section" id="work"><h2 class="section-title">Work and structure</h2>
<p>Public order, border defense, Han-overflow response (contain, evacuate, stabilize), Council decree enforcement. Line: Head Warden → five Zone Commanders → Sector Captains → Wardens → recruits. Arms: Border Corps (Zone E, worst posting, most honest), Containment Squad (Fracture and Sorrow-Wrought), Internal Affairs.</p>
<p>Violence in a Han-structural city writes more sorrow. That is the daily bind. The Directorate uses them as facility security and pulls them out of entity breaches more often than after-action admits. Architect construction zones have been unofficial training grounds. Collapse example: a Warden division Fracturing after a major breach, or a Desolate incursion that overwhelms the wall.</p>
</section>
<section class="wiki-section" id="tools"><h2 class="section-title">Tools</h2>
<p><strong>Barrier Baton</strong> (방벽 지팡이): reinforced Han-crystal, warm, tip-glow. Shield, barrier, or dampening zone — or a strike with held-down sorrow. Strength tracks calm. The baton absorbs what it suppresses. A veteran’s baton is emotionally dense. Cost of the Resonance: numbness. Oldest Wardens enforce a hush they cannot feel.</p>
<p><strong>Watchtower Eye</strong> (감시탑의 눈): head-sized sphere on Zone E towers. Scans the Desolate for Han-flow, entities, movement; alerts red. Sees emotional intensity, not only bodies. Also issued: temporary suppression gear, Fracture dampeners that slow and do not stop. See <a href="../entities/se-003-the-wilderness-tide.html">SE-003 Wilderness Tide</a> and <a href="../locations/zone-e-perimeter-bulwark.html">Zone E</a>.</p>
</section>
<section class="wiki-section" id="dilemma"><h2 class="section-title">Dilemma</h2>
<p>Do they serve the city or the Council? Internal corruption is named in source. Neutral ground with Frays exists only at <a href="../locations/the-hollow-glass.html">the Hollow Glass</a>. Taboo 6 is why the wall must not become a merge. Mellda’s personal Outside Sorrow is that Taboo’s grey area, not a Warden policy.</p>
</section>
"""
    put(
        "factions/the-wardens.html",
        "The Wardens",
        "Suhuja military guild — Citadel, Barrier Baton, Watchtower Eye, Veil fields, Zone E.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Factions</a> <i>/</i> <span>The Wardens</span>',
        "The Wardens",
        "FACTION · ORDER · ZONE E",
        [("overview", "Overview"), ("work", "Work and structure"), ("tools", "Tools"), ("dilemma", "Dilemma")],
        body,
        '<a href="index.html">Factions</a> | <a href="../locations/zone-e-perimeter-bulwark.html">Zone E</a> | <a href="../mechanics/taboo-resonance-mechanics.html">Resonances</a>',
        "Wardens Suhuja Barrier Baton Watchtower Eye Veil Zone E Border Corps",
    )


def keepers():
    body = r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The <strong>Keepers</strong> (기록관 — Girokgwan) are Somnarak’s memory guild. Power is information: Grand Archive (Building 2, Zone A), Echo vaults, which past is still speakable. Head Keeper (기록장) is a Council seat. Philosophy: <em>“We hold what would otherwise be lost. This is not power — it is responsibility.”</em></p>
<p>They are not <a href="the-memory-washers.html">Washers</a>. Washers erase. Keepers store. They are not Weavers. Weavers walk Somnus; Keepers walk shelves — though some shelves extend into Dream-space. Resonance: <strong>The Archive</strong> — crystallize sorrow into Echoes, pay with self.</p>
</section>
<section class="wiki-section" id="work"><h2 class="section-title">Work and structure</h2>
<p>Preserve history. Maintain Echo vaults. Research, translation, verification. Legal extraction, storage, imperfect restoration. Line: Head Keeper → Senior Archivists → Archivists → Scribes → apprentices. Beside: Memory Division, Vault Guard, Verification Bureau.</p>
<p>The Grand Archive is the second-largest building in Zone A, northeast of the Tree. Oldest records in the lowest vaults. The building answers to feeling: walk in angry and the Index will not help. Deep vaults hold Cheongula causation — the truth that could unseat the Council. Keepers have those records and choose not to release them. Preserve history, or control it?</p>
</section>
<section class="wiki-section" id="tools"><h2 class="section-title">Tools</h2>
<p><strong>Memory Lens</strong> (기록 렌즈): monocle of crystallized memory. An Echo near it plays as sight, sound, and feeling. Compare two memories and contradictions light. Look too often and the lens mixes the Keeper’s own past into the playback.</p>
<p><strong>Whispering Index</strong> (속삭임 색인): Han-crystal threads through the Archive. Touch, ask, and it answers in whispers and riddles. Some Keepers say it is alive. It talks constantly. Comforting. Maddening. Memory Fray has a copy of the index; the Keepers do not know.</p>
<p>Related geography: the Memory Archive under the Tree is a hungry Place that consumes visitors as stories. Grand Archive is the guild’s public face. Oldest Keepers remember the city and forget their names.</p>
</section>
<section class="wiki-section" id="relations"><h2 class="section-title">Relations</h2>
<p>Council depends on Keepers for legitimacy. Architects clash over demolition of historic sites. Collectors trade memories; Keepers recover stolen Echoes and keep them. Warden misconduct sits filed and forgotten. Weavers: rivalry on the surface, secret exchange underneath. R.D. gets Cheongula-like event records. Citizens trust Keepers with memory they thought lost.</p>
<p>If Keepers fall — Han-fire in the Grand Archive — Before-Time fragments die, the Maw’s secret dies, and the city asks whether an unremembered event happened. Weavers would try the Dream. The Directorate would keep what it already copied. Taboo 4 is why the past is not a playground; the Archive is the city’s argument that the past must remain readable.</p>
</section>
"""
    put(
        "factions/the-keepers.html",
        "The Keepers",
        "Girokgwan memory guild — Grand Archive, Memory Lens, Whispering Index, Archive Resonance.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Factions</a> <i>/</i> <span>The Keepers</span>',
        "The Keepers",
        "FACTION · ZONE A · GRAND ARCHIVE",
        [("overview", "Overview"), ("work", "Work and structure"), ("tools", "Tools"), ("relations", "Relations")],
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
<section class="wiki-section" id="place"><h2 class="section-title">Place in the underworld</h2>
<p>Filed with the Memory Fray / Memory Cartel (기억 카르텔), territory Zone B + C, specialty memory trafficking. Leader-title in the Fray table: “The Index,” a former Keeper. UCD treats Washers as a raid target, not a Council guild.</p>
<p>Related Frays: Harvesters (forced Echo extraction), Debt Brokers (Zone C debt trading), Veil Merchants (counterfeit Veil), Entity Traders (captured SEs). Commodity: stolen Archive pages and washed civilian recollection — “varies — rare memories are priceless.” A wash-rig is not a Memory Lens. A Harvest Hook is not an Extraction Glove.</p>
</section>
<section class="wiki-section" id="ucd"><h2 class="section-title">UCD Arc 2</h2>
<p><a href="the-ucd-strike-force.html">Underworld Cleanup Descend</a> Arc 2 is the Wash District operation: victims, the wash-rig, the harvest, confrontation, choice, return. That Canto-style article keeps the chapter text. This page is who they are when they are not being raided.</p>
<p>A wash does not make a Sorrow Entity. It makes a person who can Fracture later because the grief has nowhere to sit. If they cross into manufacturing hollow Han, that is Taboo 5 and Synthetics — the case file where the product fought back. The Directorate files ordinary washes under crime, not SECC.</p>
</section>
<section class="wiki-section" id="not-keepers"><h2 class="section-title">Not the Keepers</h2>
<p>Keepers preserve. Washers delete. Weavers walk the Dream. Collectors monetize obligation. Historical legitimacy and the Archive’s secret exchange with Weavers live on <a href="the-keepers.html">the Keepers</a>. See <a href="the-underworld-and-wound-walkers.html">Underworld</a> and <a href="../lore/the-seven-absolute-taboos.html">Taboos</a>.</p>
</section>
"""
    put(
        "factions/the-memory-washers.html",
        "The Memory Washers",
        "Fray memory-erasers of the Wash District. Not Keepers. UCD Arc 2. Taboo 5 grey area.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Factions</a> <i>/</i> <span>Memory Washers</span>',
        "The Memory Washers",
        "FRAY · ZONE B+C · WASH DISTRICT",
        [("overview", "Overview"), ("place", "Place in the underworld"), ("ucd", "UCD Arc 2"), ("not-keepers", "Not the Keepers")],
        body,
        '<a href="the-keepers.html">Keepers</a> | <a href="the-underworld-and-wound-walkers.html">Underworld</a> | <a href="the-ucd-strike-force.html">UCD</a>',
        "Memory Washers Fray Wash District UCD Arc 2 Taboo 5 Index",
    )


def menders():
    body = r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p><strong>Menders</strong> (수선자 — Suseonja) are independent operators, not a Council Head and not a seventh Resonance. They work the Raw — fixing, containing, protecting where guilds do not reach. They report to both the <a href="the-architects.html">Architects</a> and the <a href="the-reverie-directorate.html">Directorate</a>. That split loyalty is named in source.</p>
<p>Ranks run 7 (Novice) to 1 (Grandmaster). Five legendary Marks: Grey Veil, Crimson Thread, Pale Witness, Black Tide, Golden Echo. A Mark is not a rank; it is a scar the city still uses as a name. Organizations: the Mendery, Raw Collective, Threshold Walkers, Veil Watchers. Veil Watchers also feed Giltong when a Taboo signature shows on a repair. Novices who chase a Mark instead of a crack do not last the Raw.</p>
</section>
<section class="wiki-section" id="tools"><h2 class="section-title">Kit and rod</h2>
<p><strong>Mender’s Kit</strong> (수선자 도구함): leather-and-crystal case — trowels, probes, gauges, sealant, Echo reserves, a small Sorrow Gauge. Tools answer the user’s feeling. Each kit personalizes until it is as distinct as a fingerprint.</p>
<p><strong>Repair Rod</strong> (수리 막대): flexible Han-crystal, warm. Vibrates at cracks, fills them with the Mender’s own sorrow, reinforces weak spans, can be a weapon in an emergency. It remembers every repair. A veteran can walk the city by the rod’s map of failures. If the rod starts pulling toward the Desolate instead of a crack, stop. That is not a repair. That is a boundary (Taboo 6 adjacent).</p>
</section>
<section class="wiki-section" id="place"><h2 class="section-title">Place</h2>
<p>Alliance with the R.D. is field operations — unofficial contractors. Alliance with Architects is the same people on construction sites. Frays sometimes hire Menders, sometimes oppose them. Citizens pay Echoes for repair. Giltong treat them as witnesses, not hunters. Seol, in the Cast, is the youngest Mender who still repairs the Veil — a person page, not this guild.</p>
<p>They do not sit in the seven-note Resonance table. Shaping is Architects; Barrier is Wardens. Menders borrow both at street scale and pay in their own sorrow poured into other people’s walls. See <a href="faction-technology.html">faction technology</a> and <a href="the-underworld-and-wound-walkers.html">the Raw</a>.</p>
</section>
"""
    put(
        "factions/the-menders.html",
        "The Menders",
        "Independent Raw operators — kit, repair rod, ranks 7–1, Marks, dual report to Architects and R.D.",
        '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Factions</a> <i>/</i> <span>Menders</span>',
        "The Menders",
        "INDEPENDENT · RAW · 수선자",
        [("overview", "Overview"), ("tools", "Kit and rod"), ("place", "Place")],
        body,
        '<a href="the-architects.html">Architects</a> | <a href="the-reverie-directorate.html">Directorate</a> | <a href="faction-technology.html">Tech</a>',
        "Menders Suseonja Repair Rod Mendery Raw Collective Veil Watchers Marks",
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
    taboos()
    collectors()
    weavers()
    wardens()
    keepers()
    washers()
    menders()
    patch_search()
    print("expand A done")


if __name__ == "__main__":
    main()
