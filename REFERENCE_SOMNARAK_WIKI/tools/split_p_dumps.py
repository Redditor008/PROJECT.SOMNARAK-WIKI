#!/usr/bin/env python3
"""P continue: split leftover PROJECT_SOMNARAK dumps; fix titles that disagree with source MD."""
from __future__ import annotations

import pathlib
import re

DOCS = pathlib.Path("/home/user/PROJECT.SOMNARAK-WIKI/docs")


def splice_lore(rel: str, crumb_last: str, h1: str, toc_items: list[tuple[str, str]], body: str) -> None:
    path = DOCS / rel
    t = path.read_text(encoding="utf-8")
    lis = "\n".join(f'<li><a href="#{i}">{lab}</a></li>' for i, lab in toc_items)
    toc = f'<div class="toc" id="toc">\n<div class="toc-title">Contents</div>\n<div class="toc-body">\n<ol>\n{lis}\n</ol>\n</div>\n</div>\n'
    start = t.find("<!-- Breadcrumbs")
    if start < 0:
        start = t.find('<div class="breadcrumbs">')
    end = t.find("<!-- Page Footer")
    if start < 0 or end < 0:
        raise SystemExit(f"cannot splice {rel} start={start} end={end}")
    mid = f"""<!-- Breadcrumbs -->
<div class="breadcrumbs">
<a href="../index.html">Somnarak</a> <i>/</i>
<a href="index.html">Lore &amp; World</a> <i>/</i>
<span>{crumb_last}</span>
</div>
<!-- Article Header -->
<div class="article-header">
<div class="article-eyebrow">LORE &amp; WORLD RECORD</div>
<h1 class="article-title">{h1}</h1>
<div class="article-subbar">
<span class="badge badge-canon">CANONICAL ARTIFACT</span>
<span class="badge badge-source">SOURCE VERIFIED</span>
<div class="article-actions">
<span class="action-btn">History</span>
<span class="action-btn">View Source</span>
</div>
</div>
</div>
{toc}
{body}
<div class="wiki-callout">
<p><strong>CANONICAL RECORD:</strong> Sourced from <em>PROJECT_SOMNARAK.md</em> — this chapter only. Other books stay on their own pages.</p>
</div>

"""
    path.write_text(t[:start] + mid + t[end:], encoding="utf-8")
    print("spliced", rel)


def cosmology():
    body = r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>Somnarak sits between two primordial states. <strong>The Dream (Somnus)</strong> is unformed potential — memory, desire, fear. It is not inherently kind: a prison of nostalgia, a labyrinth of false hopes. It manifests as illusion, subconscious entities, altered states. <strong>The Abyss (Narak)</strong> is consequence — actions have weight, debts are collected. It is not purely punitive: a crucible of growth, a forge of truth. It manifests as physical law, karmic debt, systemic oppression.</p>
<p>This page is cosmology: Dream, Abyss, Han as binder. The three categories of Han (City / Outside / Inner) live on <a href="the-three-sorrows.html">the Three Sorrows</a>. Entity origin lives on <a href="the-weeping-river.html">the Weeping</a>. Classification codes live on <a href="../mechanics/secc-classification-system.html">SECC</a>. Aesthetic notes and the open-question dump that used to sit under this URL are gone — those were leftover <code>PROJECT_SOMNARAK.md</code> chapters X and XI.</p>
<p>The old title “Five Layers” mixed Somnus’s dive-layers with cosmology. Dive layers stay on <a href="the-dream-realm.html">the Dream realm</a>.</p>
</section>
<section class="wiki-section" id="han"><h2 class="section-title">Han (한) — the binding force</h2>
<p>Han is collective grief that has become <em>structural</em> — not only emotion, but material. Mortar between bricks. Foundation of buildings. Blood of the city. It accumulates over generations into architecture, law, memory, transformation. It <strong>cannot be destroyed</strong> — only managed, redirected, or transformed.</p>
<p>In the Before-Time it flowed like weather. After the Becoming it pooled. After the Structuring it is the world. Wars that tried to seal it, sever it, or feed it are on <a href="the-first-sovereign-war.html">the Wars of Somnarak</a>. The Tree that froze it into meaning is on <a href="the-alpha-tree.html">the Alpha Tree</a>.</p>
</section>
<section class="wiki-section" id="three"><h2 class="section-title">Three Sorrows — index</h2>
<p>Not all sorrow is the same. Han shows as three categories. Full articles on each stay on the Three Sorrows page; this is the cosmological index so a search for “cosmology” does not paste Zone B weeping-walls into this URL.</p>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>Category</th><th>Korean</th><th>Source</th><th>Character</th><th>Manifestation</th></tr></thead>
<tbody>
<tr><td>City Sorrow</td><td>도한 (Dohan)</td><td>City structure, systems, history</td><td>Collective, ambient, structural</td><td>Weeping buildings, whispering streets, the city’s weight</td></tr>
<tr><td>Outside Sorrow</td><td>외한 (Oehan)</td><td>Wilderness, Desolate, external forces</td><td>Wild, unstructured, invasive</td><td>Raw Han flows, wilderness entities, Desolate anomalies</td></tr>
<tr><td>Inner Sorrow</td><td>내한 (Naehan)</td><td>Personal grief, private trauma</td><td>Intimate, corrosive</td><td>Fracture, Architect’s Mark, debt accumulation</td></tr>
</tbody></table></div>
<p>City Sorrow is institutional — Collectors, Council, the city’s existence feeding on inhabitants. Zone B feels it most; Zone A channels it through the Tree; the Maw is its extreme. Outside Sorrow has no master beyond the wall. Inner Sorrow is the one that Fractures a single person. How the three interact, who is affected, and the danger of each: <a href="the-three-sorrows.html">Three Sorrows</a>.</p>
</section>
<section class="wiki-section" id="nested"><h2 class="section-title">Nested world</h2>
<p>Outside → in, from the world-bible: Mugenhan (the world) contains the wilderness and other settlements; the unofficial zone is the Desolate; Somnarak is the city of five zones around the Alpha Tree. The Veil/Raw split is civic governance, not a cosmological layer — that atlas page is <a href="../locations/district-structure-veil-and-raw.html">District structure</a>.</p>
<p>Open questions that belong to cosmology (not a dump of every unanswered line in the bible): why Han began to accumulate; whether Dream and Abyss were always this close; whether the Tree was grown or designed. Faction answers contradict. Keepers hold fragments. Weavers hold echoes. The Council holds a story that sounds like weather becoming law.</p>
</section>
"""
    splice_lore(
        "lore/somnarak-cosmology.html",
        "Cosmology",
        "Somnarak Cosmology",
        [
            ("overview", "Overview"),
            ("han", "Han"),
            ("three", "Three Sorrows index"),
            ("nested", "Nested world"),
        ],
        body,
    )


def ages():
    body = r"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>Somnarak’s history is three ages. Boundaries are not sharp — they blur, overlap, and contradict depending on who tells the story. This page is Age I / II / III only. Cheongula, Occlusihan, Consolihan, and the year table live on <a href="the-first-sovereign-war.html">the Wars of Somnarak</a>. SED / UCD / R.D. operations are not “historic wars”; they are present-age missions on their own articles. The old paste of <em>Operations — Story Arcs</em> onto this URL is gone.</p>
<pre class="wiki-pre">THE BEFORE-TIME          THE BECOMING           THE STRUCTURING
(Unknown duration)       (Unknown duration)      (Current age)
     │                        │                        │
     ▼                        ▼                        ▼
  Han existed              Han condensed            Han became
  but flowed               into pockets,            structural —
  freely, like             wells, rivers.           the foundation
  weather.                 People gathered.         of reality.
                                                    The city rose.</pre>
</section>
<section class="wiki-section" id="one"><h2 class="section-title">Age I — The Before-Time (선시대)</h2>
<p>Han existed — it always has. Grief, sorrow, injustice are as old as consciousness. In the Before-Time Han was <strong>ambient</strong>. It flowed like weather: through, into low places, dispersing with time.</p>
<p>The world was not paradise. People suffered. They grieved. They raged. Sorrow was <em>personal</em> — it belonged to the one who felt it, and when they died, it faded. Han did not build up. It did not crystallize. It did not become structural.</p>
<p>What existed: small communities — villages, tribes, wandering groups — with their own mourning rituals and release practices. Dream and Abyss were distant, otherworldly, not woven into daily life. No cities. No Architects. No Council. No system.</p>
<p>No complete record survives. The Archive’s deepest vaults hold fragments — contradictory, incomplete, corrupted. Dream echoes hold images and feelings, not facts. The wilderness may hold traces. Each faction reads the fragments differently. What they suggest: impermanence (sorrow passed, joy passed, nothing fixed); freedom with instability; a world the Council calls unsustainable.</p>
</section>
<section class="wiki-section" id="two"><h2 class="section-title">Age II — The Becoming (변천)</h2>
<p>The central mystery: Han began to <strong>accumulate</strong>. Instead of flowing through and dispersing, it pooled, crystallized, persisted. Why?</p>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>Theory</th><th>Proponent</th><th>Claim</th></tr></thead>
<tbody>
<tr><td>Inevitable</td><td>Council</td><td>Accumulation is natural. Before-Time was unsustainable.</td></tr>
<tr><td>Catastrophe</td><td>Some Architects</td><td>A single massive injustice — the First Sorrow — broke the cycle.</td></tr>
<tr><td>Choice</td><td>Heretical scholars</td><td>Someone chose to make Han structural. A deal was made.</td></tr>
<tr><td>Corruption</td><td>Weavers</td><td>Dream and Abyss drew too close. Han trapped between them.</td></tr>
<tr><td>Weight</td><td>Collectors</td><td>Enough sorrow, injustice, debt — gravity did the rest.</td></tr>
</tbody></table></div>
<p>Fragmented sequence: Han pooled in valleys, caves, the spaces between communities. People noticed — sorrow lingered, grief did not fade, the dead were not forgotten. Communities gathered around the pools (study, worship, flight, or no choice). Pools grew on collective suffering. Han crystallized into the first solid sorrow-material. The first structures were built not by Architects (they did not exist) but by desperate people using the only material available: solidified grief.</p>
<p>Where the greatest pool formed, people gathered. This settlement became <a href="../locations/zone-b-west-ward.html">Zone B</a> — oldest, most wounded, jagged from unskilled construction. Survival, not design.</p>
</section>
<section class="wiki-section" id="three"><h2 class="section-title">Age III — The Structuring (구조화)</h2>
<p>The moment Han became structural — sorrow stopped being <em>in</em> the world and became <em>the</em> world — is the great unknown. Consequences are clear: Han is foundational. Buildings, laws, physical reality are held together by sorrow. The city needs Han; without it, structures collapse. Han accumulates faster than it disperses. The weight only grows.</p>
<p>During the Becoming, someone (or something) designed — or grew — the <a href="the-alpha-tree.html">Alpha Tree</a>. Unlike Zone B’s desperation, the Tree is a perfect diamond in chaos. Council: it was always there, grown from the first sorrow. Architects: someone built it; the geometry is too perfect. Keepers: blueprint fragments, builders’ names redacted. Weavers: the Dream designed it through us.</p>
<p>The Tree is the anchor. Six buildings manage Han flow. It extends up toward Dream and down toward Abyss. Without it the city collapses under its own sorrow.</p>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>Phase</th><th>Zone</th><th>How</th><th>Why</th></tr></thead>
<tbody>
<tr><td>1st</td><td>B West</td><td>Desperate, organic, violent</td><td>Shelter from raw Han</td></tr>
<tr><td>2nd</td><td>C East</td><td>Deliberate, architectural</td><td>Order — the system begins</td></tr>
<tr><td>3rd</td><td>D Mantle</td><td>Designed to contain B</td><td>Containment of chaos</td></tr>
<tr><td>4th</td><td>E Perimeter</td><td>Fortified, defensive</td><td>Wall against the unknown</td></tr>
</tbody></table></div>
<p>Governance coalesced from practical necessity, not ideology. First leaders were those who had survived the most — absorbed the heaviest Han and endured. They did not choose to rule; they were chosen by their weight. The Council of Sighs was not founded so much as it condensed, like Han. Fatalism was observed: <em>“This is what is. We manage.”</em></p>
<p>The first Architects realized: if Han is structural, it can be shaped. Survivors who learned to work with what was killing them. Architect’s Hall is the sixth building of the Tree — last, most practical. They are the only Head that believes the future can be different even if the system cannot be broken.</p>
<p>Year numbers, Cheongula, Occlusihan, Consolihan: <a href="the-first-sovereign-war.html">Wars</a>. Present operations after 4200: <a href="../factions/the-founding-corporations.html">three operations</a>.</p>
</section>
"""
    splice_lore(
        "lore/the-three-ages-and-history.html",
        "Three Ages",
        "The Three Ages",
        [
            ("overview", "Overview"),
            ("one", "Age I Before-Time"),
            ("two", "Age II Becoming"),
            ("three", "Age III Structuring"),
        ],
        body,
    )


def fix_titles():
    jobs = [
        (
            "mechanics/secc-classification-system.html",
            "SECC Classification System (AETHER to APOCRYPHA)",
            "SECC Classification System",
        ),
        (
            "factions/the-sed-corps.html",
            "Sorrow Exploration Division (SED)",
            "Somnarak Exploration Decreed (SED)",
        ),
        (
            "factions/the-ucd-strike-force.html",
            "Underworld Containment Division (UCD)",
            "Underworld Cleanup Descend (UCD)",
        ),
        (
            "lore/the-doorspeech.html",
            "The Doorspeech (Mun-eon) &amp; Acoustic Mantles",
            "The Doorspeech",
        ),
        (
            "lore/the-weeping-river.html",
            "The Weeping River &amp; Abyssal Hydrology",
            "The Weeping",
        ),
    ]
    for rel, old, new in jobs:
        p = DOCS / rel
        t = p.read_text(encoding="utf-8")
        n = t.count(old)
        t2 = t.replace(old, new)
        # crumb span sometimes matches h1
        if t2 != t:
            p.write_text(t2, encoding="utf-8")
            print(f"title {rel}: {n} → {new}")
        else:
            print(f"title {rel}: no exact H1 match")
            m = re.search(r'<h1 class="article-title">([^<]+)</h1>', t)
            print("  actual", m.group(1) if m else None)


def main():
    cosmology()
    ages()
    fix_titles()
    print("split P dumps done")


if __name__ == "__main__":
    main()
