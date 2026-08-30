#!/usr/bin/env python3
"""Place Lore/Reference sources onto wiki category pages (300+ word encyclopedia articles)."""
from __future__ import annotations

import html
import json
import pathlib
import re

ROOT = pathlib.Path("/home/user/PROJECT.SOMNARAK-WIKI")
DOCS = ROOT / "docs"
LORE = ROOT / "REFERENCE_SOMNARAK_WIKI" / "LORE or REFERANCE"
CSSV = "20260830ae"


def words(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


def extract_table(text: str) -> dict[str, str]:
    fields = {}
    for m in re.finditer(r"\|\s*\*\*(.+?)\*\*\s*\|\s*(.+?)\s*\|", text):
        fields[m.group(1).strip()] = re.sub(r"`", "", m.group(2)).strip()
    return fields


def extract_section(text: str, heading: str) -> str:
    pat = rf"^## {re.escape(heading)}\s*\n(.+?)(?=^## |\Z)"
    m = re.search(pat, text, re.M | re.S)
    return m.group(1).strip() if m else ""


def first_paras(md: str, n: int = 3, max_words: int = 220) -> list[str]:
    if not md:
        return []
    body = re.sub(r"^>.+\n?", "", md, flags=re.M)
    body = re.sub(r"\|.+\|\n?", "", body)
    body = re.sub(r"^[-*]{3,}\s*$", "", body, flags=re.M)
    body = re.sub(r"^### .+$", "", body, flags=re.M)
    chunks = [c.strip() for c in re.split(r"\n\s*\n", body) if c.strip()]
    out, total = [], 0
    for c in chunks:
        c = re.sub(r"\s+", " ", c)
        c = re.sub(r"\*\*(.+?)\*\*", r"\1", c)
        c = re.sub(r"\*(.+?)\*", r"\1", c)
        c = re.sub(r"`(.+?)`", r"\1", c)
        if len(c) < 40:
            continue
        w = words(c)
        if total and total + w > max_words:
            break
        out.append(c)
        total += w
        if len(out) >= n:
            break
    return out


def p_html(paras: list[str]) -> str:
    return "\n".join(f"<p>{html.escape(p)}</p>" for p in paras)


def toc_html(items: list[tuple[str, str]]) -> str:
    lis = "\n".join(f'<li><a href="#{i}">{html.escape(t)}</a></li>' for i, t in items)
    return f"""<nav class="toc hub-toc toc-panel" aria-label="Contents">
<div class="toc-title">Contents · jump to a section</div>
<ol>
{lis}
</ol>
</nav>"""


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
<a href="../departments/index.html">Facility</a>
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
<a href="../entities/hope-transformations.html">Hope Transformations</a>
<a href="../entities/unknown-entities.html">Unknown Entities</a>
<a href="../maw/index.html">M.A.W. Equipment</a>
<a href="../characters/index.html">Echo-Cores &amp; Cast</a>
<a href="../departments/index.html">Facility Floors</a>
<a href="../mechanics/ordeals-framework.html">Ordeals</a>
<a href="../lore/index.html">Lore &amp; Cosmology</a>
</section>
<section>
<h2>THE NINE ECHO-CORES</h2>
<a href="../characters/the-director-majin.html">1. Director Majin</a>
<a href="../characters/the-secretary-seiyon.html">2. Seiyon</a>
<a href="../characters/the-containment-lead-dekan.html">3. Dekan</a>
<a href="../characters/the-extraction-lead-zyrak.html">4. Zyrak</a>
<a href="../characters/the-research-lead-ayshuk.html">5. Ayshuk</a>
<a href="../characters/the-border-lead-mellda.html">6. Mellda</a>
<a href="../characters/the-archive-lead-marjuk.html">7. Marjuk</a>
<a href="../characters/the-outsider-ishall.html">8. Ishall</a>
<a href="../characters/the-exile-xyan.html">9. Xyan</a>
</section>
</nav>
</aside>
<main id="content">
"""

FOOTER = """
<footer class="article-footer">
<div class="footer-categories">
<strong>Categories:</strong>
{cats}
</div>
<div class="footer-disclaimer">Content is available under Somnarak Directorate Archival License unless otherwise noted.</div>
</footer>
<section class="cross-reference-section">
<div class="cross-ref-header">CANONICAL CROSS-LINKS</div>
<div class="cross-ref-grid">
<a href="../entities/index.html" class="cross-ref-card"><div class="cross-ref-meta"><span class="cross-ref-cat">REGISTRY</span><span class="cross-ref-title">SORROW ENTITIES</span></div></a>
<a href="../entities/hope-transformations.html" class="cross-ref-card"><div class="cross-ref-meta"><span class="cross-ref-cat">DAWN</span><span class="cross-ref-title">HOPE TRANSFORMATIONS</span></div></a>
<a href="../mechanics/ordeals-framework.html" class="cross-ref-card"><div class="cross-ref-meta"><span class="cross-ref-cat">FACILITY</span><span class="cross-ref-title">ORDEALS</span></div></a>
<a href="../lore/the-dawn-of-hope.html" class="cross-ref-card"><div class="cross-ref-meta"><span class="cross-ref-cat">STORY</span><span class="cross-ref-title">DAWN OF HOPE</span></div></a>
</div>
</section>
</main>
</div>
</body>
</html>
"""


def wrap(title: str, desc: str, crumbs: str, h1: str, eyebrow: str, toc: str, body: str, cats: str) -> str:
    head = HEADER.format(title=html.escape(title), desc=html.escape(desc)[:300])
    art = f"""<div class="breadcrumbs">{crumbs}</div>
<div class="article-header">
<div class="article-eyebrow">{html.escape(eyebrow)}</div>
<h1 class="article-title">{html.escape(h1)}</h1>
<div class="article-subbar">
<span class="badge badge-canon">CANONICAL ARTIFACT</span>
<span class="badge badge-source">SOURCE VERIFIED</span>
</div>
</div>
{toc}
{body}
"""
    return head + art + FOOTER.format(cats=cats)


def fact_table(rows: list[tuple[str, str]]) -> str:
    trs = "".join(
        f"<tr><th>{html.escape(k)}</th><td>{html.escape(v)}</td></tr>" for k, v in rows if v
    )
    return f'<div class="table-wrap"><table class="wiki-table"><tbody>{trs}</tbody></table></div>'


SEARCH_NEW: list[dict] = []


def emit(rel: str, html_doc: str, title: str, category: str, desc: str):
    path = DOCS / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html_doc, encoding="utf-8")
    body_w = words(re.sub(r"<[^>]+>", " ", html_doc))
    SEARCH_NEW.append(
        {
            "title": title,
            "url": rel,
            "category": category,
            "description": desc[:240],
            "keywords": f"{title} {category} {desc[:180]}",
        }
    )
    print(f"  {body_w:4d}w  {rel}")
    if body_w < 100:
        raise SystemExit(f"UNDER 100 WORDS: {rel}")
    return body_w


def slug_from_h1(h1: str) -> str:
    base = re.sub(r"\s*—\s*.+$", "", h1)
    base = re.sub(r"[^A-Za-z0-9]+", "-", base).strip("-").lower()
    return base


# ---------------------------------------------------------------------------
# Hope Transformations
# ---------------------------------------------------------------------------

HT_FILES = sorted((LORE / "02_Hope_Transformation").glob("*.md"))


def build_ht():
    cards = []
    pages = []
    for p in HT_FILES:
        t = p.read_text(encoding="utf-8", errors="replace")
        h1 = re.search(r"^# (.+)$", t, re.M).group(1)
        f = extract_table(t)
        reg = f.get("Registry Number") or ("HT-V-HH-001" if "Hand of Hope" in h1 else "HT-V-HC-001")
        slug = slug_from_h1(h1)
        if "Trinity" in h1:
            fname = "ht-v-hc-001-the-trinity-of-dawn.html"
        elif "Hand of Hope" in h1:
            fname = "ht-v-hh-001-the-hand-of-hope.html"
        else:
            num = re.search(r"HT-(\d+)", reg)
            fname = f"ht-{num.group(1).zfill(3) if num else '000'}-{slug}.html"
        appear = first_paras(extract_section(t, "Appearance"), 3, 200)
        origin = first_paras(extract_section(t, "Origin"), 3, 200)
        func = first_paras(
            extract_section(t, "Hope Function") or extract_section(t, "Operational Behavior"),
            3,
            180,
        )
        cost = first_paras(extract_section(t, "Hope Bearer Cost"), 2, 140)
        if words(" ".join(appear + origin + func + cost)) < 280:
            extra = first_paras(extract_section(t, "Activation / Expansion Behavior"), 2, 120)
            func += extra
        rows = [
            ("Designation", f.get("HT Designation") or reg),
            ("Registry", reg),
            ("Category", f.get("Hope Category", "Hope Transformation")),
            ("Aspect", f.get("Hope Aspect", "")),
            ("Coherence", f.get("Coherence", "")),
            ("Intensity", f.get("Hope Intensity", "")),
            ("Element", f.get("Hope Element", "")),
            ("Manifestation", f.get("Manifestation", "")),
            ("Bearer", f.get("Hope Bearer", "")),
            ("Bearer role", f.get("Bearer Role", "")),
            ("Source sorrow", f.get("Source", "")[:240]),
            ("Status", f.get("Transformation Status", "")),
        ]
        toc = toc_html(
            [
                ("overview", "Overview"),
                ("classification", "Classification"),
                ("appearance", "Appearance"),
                ("origin", "Origin"),
                ("function", "Hope function"),
                ("bearer", "Bearer cost"),
            ]
        )
        overview = (
            f"{h1} is a Hope Transformation — sorrow that the Hand of Hope turned into a bonded "
            f"hope entity without erasing the wound that made it. "
            f"{('It is borne by ' + f.get('Hope Bearer') + '. ') if f.get('Hope Bearer') else ''}"
            f"Unlike a Sorrow Entity, it is not contained in a cell and does not yield M.A.W. by extraction. "
            f"It remains stable only while the bond holds."
        )
        body = f"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>{html.escape(overview)}</p>
<p>Hope Transformations sit beside Sorrow Entities, not inside them. The Reverie Directorate catalogues Sorrow under SECC. Dawn Initiative bearers catalogue Hope under HT designations. The grief is still present; it is made usable.</p>
</section>
<section class="wiki-section" id="classification"><h2 class="section-title">Classification</h2>
{fact_table(rows)}
</section>
<section class="wiki-section" id="appearance"><h2 class="section-title">Appearance</h2>
{p_html(appear) or "<p>Physical form is recorded in the Hope Entity Classification table.</p>"}
</section>
<section class="wiki-section" id="origin"><h2 class="section-title">Origin</h2>
{p_html(origin)}
</section>
<section class="wiki-section" id="function"><h2 class="section-title">Hope function</h2>
{p_html(func)}
</section>
<section class="wiki-section" id="bearer"><h2 class="section-title">Bearer cost</h2>
{p_html(cost) or "<p>The transformation is bearer-dependent. If the bond fails, the hope entity destabilizes rather than reverting to a contained Sorrow Entity.</p>"}
<p>See <a href="hope-transformations.html">Hope Transformations</a> and <a href="../lore/the-dawn-of-hope.html">Dawn of Hope</a>.</p>
</section>
"""
        crumbs = (
            '<a href="../index.html">Somnarak</a> <i>/</i> '
            '<a href="index.html">Sorrow Entities</a> <i>/</i> '
            '<a href="hope-transformations.html">Hope Transformations</a> <i>/</i> '
            f"<span>{html.escape(h1)}</span>"
        )
        cats = (
            '<a href="hope-transformations.html">Hope Transformations</a> | '
            '<a href="../lore/the-dawn-of-hope.html">Dawn of Hope</a> | '
            '<a href="index.html">Sorrow Entities</a>'
        )
        desc = appear[0][:220] if appear else overview[:220]
        doc = wrap(h1, desc, crumbs, h1, "HOPE TRANSFORMATION", toc, body, cats)
        emit(f"entities/{fname}", doc, h1, "Hope Transformations", desc)
        pages.append((fname, h1, reg, f.get("Hope Bearer", ""), f.get("Hope Aspect", "")))
        cards.append((fname, h1, reg, f.get("Hope Bearer", ""), f.get("Hope Element", "")[:80]))

    # hub
    rows_html = "".join(
        f"<tr><td><a href='{fn}'>{html.escape(reg)}</a></td>"
        f"<td><a href='{fn}'>{html.escape(name)}</a></td>"
        f"<td>{html.escape(bearer or '—')}</td>"
        f"<td>{html.escape(aspect or '—')}</td></tr>"
        for fn, name, reg, bearer, aspect in pages
    )
    hub_body = f"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p><strong>Hope Transformations</strong> (희망 변환) are sorrow given a second shape by the Hand of Hope. They are not Sorrow Entities. They do not crystallize from the Weeping into a containment cell, they are not immortal in the SECC sense, and they do not produce M.A.W. weapons by extraction. Each one is bonded to a Dawn Initiative bearer whose original grief remains intact — the transformation makes that weight usable.</p>
<p>The public Archive publishes all <strong>14</strong> canonical Hope records from <code>02_Hope_Transformation</code>: twelve bearer bonds (HT-001 through HT-012) plus two Sovereign-class phenomena, the Trinity of Dawn and the Hand of Hope. This is a separate category from the 288 Sorrow Entities (of which 13 dossiers are on the wiki).</p>
<p>Analog on Project Moon wikis: Limbus keeps Identities / E.G.O as their own homepage tiles, not as Abnormality dumps. Hope Transformations are that kind of tile — a species with its own list.</p>
</section>
<section class="wiki-section" id="rule"><h2 class="section-title">Hope Transformation rule</h2>
<p>A Hope entity retains the sorrow from which it formed. It does not erase knowledge, guilt, or loss. It turns that burden into a function: light, shield, flame, spark, vigil, witness. If the bearer dies or rejects the bond, the Hope destabilizes. It does not politely become a contained SE.</p>
</section>
<section class="wiki-section" id="registry"><h2 class="section-title">Registry of fourteen</h2>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>ID</th><th>Name</th><th>Bearer</th><th>Aspect</th></tr></thead>
<tbody>{rows_html}</tbody>
</table></div>
</section>
<section class="wiki-section" id="related"><h2 class="section-title">Related records</h2>
<ul>
<li><a href="../lore/the-dawn-of-hope.html">Dawn of Hope</a> — Year 4238 operations that field these bonds.</li>
<li><a href="index.html">Sorrow Entities</a> — the grief these transformations were made from.</li>
<li><a href="unknown-entities.html">Unknown Entities</a> — including The Extinguished, a failed Hope Bearer afterimage.</li>
<li><a href="ht-v-hh-001-the-hand-of-hope.html">The Hand of Hope</a> — the Sovereign that performs the transformation.</li>
</ul>
</section>
"""
    toc = toc_html([("overview", "Overview"), ("rule", "Hope Transformation rule"), ("registry", "Registry of fourteen"), ("related", "Related records")])
    crumbs = '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Sorrow Entities</a> <i>/</i> <span>Hope Transformations</span>'
    cats = '<a href="hope-transformations.html">Hope Transformations</a> | <a href="../lore/the-dawn-of-hope.html">Dawn of Hope</a> | <a href="index.html">Sorrow Entities</a>'
    doc = wrap(
        "Hope Transformations",
        "Fourteen Hope entities bonded to Dawn Initiative bearers — sorrow made usable, not erased.",
        crumbs,
        "Hope Transformations",
        "CATEGORY HUB",
        toc,
        hub_body,
        cats,
    )
    emit("entities/hope-transformations.html", doc, "Hope Transformations", "Hope Transformations", "Fourteen Hope entities bonded to Dawn Initiative bearers.")


# ---------------------------------------------------------------------------
# Unknown Entities
# ---------------------------------------------------------------------------

UNK = [
    ("SE-N-IIIβ-247_The_Undelivered_Thanks_전하지_못한_감사.md", "unk-247-the-undelivered-thanks.html"),
    ("SE-C-IIIγ-248_The_Unconsoled_위로받지_못한_자.md", "unk-248-the-unconsoled.html"),
    ("SE-N-IVγ-250_The_Extinguished_꺼진_자.md", "unk-250-the-extinguished.html"),
    ("SE-C-IVδ-251_The_Unspoken_Line_그어진_선.md", "unk-251-the-unspoken-line.html"),
    ("SE-N-IVδ-901_The_Mewgical_Girl_야옹_마법소녀.md", "unk-901-the-mewgical-girl.html"),
    ("SE-N-IVδ-902_The_Repeated_Survivor_되풀이의_생존자.md", "unk-902-the-repeated-survivor.html"),
    ("SE-N-IIγ-903_The_Music_Box_of_Agony_고통의_오르골.md", "unk-903-the-music-box-of-agony.html"),
]


def build_unknown():
    listed = []
    for src_name, fname in UNK:
        p = LORE / "03_Unknown_Entities" / src_name
        t = p.read_text(encoding="utf-8", errors="replace")
        h1 = re.search(r"^# (.+)$", t, re.M).group(1)
        f = extract_table(t)
        appear = first_paras(extract_section(t, "Appearance"), 3, 200)
        origin = first_paras(extract_section(t, "Origin"), 3, 200)
        beh = first_paras(
            extract_section(t, "Behavior")
            or extract_section(t, "Behavior & Work Types")
            or extract_section(t, "Operational Behavior"),
            3,
            180,
        )
        if words(" ".join(appear + origin + beh)) < 280:
            beh += first_paras(extract_section(t, "Breach Behavior"), 2, 120)
        desig = f.get("Designation") or f.get("SECC Code") or ""
        rows = [
            ("Designation", desig),
            ("Coherence", f.get("Coherence", "")),
            ("Potency", f.get("Potency", "")),
            ("Element", f.get("Element", "")),
            ("Manifestation", f.get("Manifestation", "")),
            ("Physical form", (f.get("Physical Form") or "")[:280]),
        ]
        overview = (
            f"{h1} is filed with the Unknown Entities — specimens that have SECC-shaped designations "
            f"but are not among the thirteen public containment dossiers. "
            f"The Archive treats them as real, named threats. They are not placeholders."
        )
        toc = toc_html(
            [
                ("overview", "Overview"),
                ("classification", "Classification"),
                ("appearance", "Appearance"),
                ("origin", "Origin"),
                ("behavior", "Behavior"),
            ]
        )
        body = f"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>{html.escape(overview)}</p>
<p>Unknown here does not mean “unwritten.” It means the specimen is not yet on the protected thirteen. Source dossiers live under <code>03_Unknown_Entities</code>. Analog: a Distortion or unidentified Abnormality still gets its own article on Project Moon wikis.</p>
</section>
<section class="wiki-section" id="classification"><h2 class="section-title">Classification</h2>
{fact_table(rows)}
</section>
<section class="wiki-section" id="appearance"><h2 class="section-title">Appearance</h2>
{p_html(appear)}
</section>
<section class="wiki-section" id="origin"><h2 class="section-title">Origin</h2>
{p_html(origin)}
</section>
<section class="wiki-section" id="behavior"><h2 class="section-title">Behavior</h2>
{p_html(beh) or "<p>Work-type response is incomplete in the public extract; treat the specimen as uncontained until Floor 2 files a cell.</p>"}
<p>Return to <a href="unknown-entities.html">Unknown Entities</a>. SECC decoding: <a href="../mechanics/secc-classification-system.html">SECC classification</a>.</p>
</section>
"""
        crumbs = (
            '<a href="../index.html">Somnarak</a> <i>/</i> '
            '<a href="index.html">Sorrow Entities</a> <i>/</i> '
            '<a href="unknown-entities.html">Unknown Entities</a> <i>/</i> '
            f"<span>{html.escape(h1)}</span>"
        )
        cats = (
            '<a href="unknown-entities.html">Unknown Entities</a> | '
            '<a href="index.html">Sorrow Entities</a> | '
            '<a href="../mechanics/secc-classification-system.html">SECC</a>'
        )
        desc = appear[0][:220] if appear else overview[:220]
        doc = wrap(h1, desc, crumbs, h1, "UNKNOWN ENTITY", toc, body, cats)
        emit(f"entities/{fname}", doc, h1, "Unknown Entities", desc)
        listed.append((fname, h1, desig))

    rows_html = "".join(
        f"<tr><td><a href='{fn}'>{html.escape(d or '—')}</a></td><td><a href='{fn}'>{html.escape(n)}</a></td></tr>"
        for fn, n, d in listed
    )
    hub_body = f"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p><strong>Unknown Entities</strong> are named Sorrow specimens that are not in the thirteen public containment dossiers and not in the Hope Transformation register. The Directorate still has full dossiers. “Unknown” is an archive status, not a blank page.</p>
<p>Seven entity files and one dramaturgy book sit in <code>03_Unknown_Entities</code>. The book is a Cycle side-story and is filed under Lore, not here — same split LC uses between Abnormalities and Daily Recordings.</p>
</section>
<section class="wiki-section" id="registry"><h2 class="section-title">Seven uncatalogued specimens</h2>
<div class="table-wrap"><table class="wiki-table">
<thead><tr><th>Designation</th><th>Name</th></tr></thead>
<tbody>{rows_html}</tbody>
</table></div>
<p>The Extinguished is the afterimage of a Hope Bearer whose gold went cold. It is the warning that Hope Transformations can fail. The Unspoken Line is a junction that became an entity — a Place-type Void. The Music Box of Agony is an Object-Void that repeats one lullaby.</p>
</section>
<section class="wiki-section" id="story"><h2 class="section-title">Related story</h2>
<p><a href="../lore/the-book-of-regressor.html">The Book of Regressor</a> is a log of the loops, not an SE. It belongs with Absolvohan / Daily Recordings.</p>
</section>
"""
    toc = toc_html([("overview", "Overview"), ("registry", "Seven uncatalogued specimens"), ("story", "Related story")])
    crumbs = '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Sorrow Entities</a> <i>/</i> <span>Unknown Entities</span>'
    cats = '<a href="unknown-entities.html">Unknown Entities</a> | <a href="index.html">Sorrow Entities</a>'
    doc = wrap(
        "Unknown Entities",
        "Seven named Sorrow specimens outside the thirteen public dossiers.",
        crumbs,
        "Unknown Entities",
        "CATEGORY HUB",
        toc,
        hub_body,
        cats,
    )
    emit("entities/unknown-entities.html", doc, "Unknown Entities", "Unknown Entities", "Seven named Sorrow specimens outside the thirteen public dossiers.")


# ---------------------------------------------------------------------------
# Entity groups
# ---------------------------------------------------------------------------

def build_groups():
    t = (LORE / "07_Reference" / "SOMNARAK_ENTITIES.md").read_text(encoding="utf-8", errors="replace")
    groups = first_paras(extract_section(t, "I. Entity Groups (연결된 존재 — Yeongyeoldoen Jonjae)") or t, 6, 260)
    # pull named h3 blocks
    blocks = []
    for title in [
        "The Three Birds of the Forgotten Forest (잊혀진 숲의 새들)",
        "The Three Sisters of the Echo Gardens (메아리 정원의 세 자매)",
        "The Masked Troupe (가면 무리 — Gamyeon Muri)",
        "The Debt Triplets (빚의 삼胞 — Bit-ui Sambo)",
    ]:
        m = re.search(rf"^### {re.escape(title)}\s*\n(.+?)(?=^### |\Z)", t, re.M | re.S)
        if m:
            blocks.append((title, first_paras(m.group(1), 3, 160)))
    chain = first_paras(extract_section(t, "II. Transformation Chains (변형 사슬 — Byeonghyeong Saseol)"), 4, 200)
    fairy = first_paras(extract_section(t, "III. Fairy-Tale Entities (이야기 존재 — Iyagi Jonjae)"), 3, 160)
    inner = ""
    for title, paras in blocks:
        sid = slug_from_h1(title)
        inner += f'<h3 id="{sid}">{html.escape(title)}</h3>\n{p_html(paras)}\n'
    toc = toc_html(
        [
            ("overview", "Overview"),
            ("groups", "Linked groups"),
            ("chains", "Transformation chains"),
            ("tales", "Fairy-tale entities"),
        ]
    )
    body = f"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>Some Sorrow Entities are not solitary. They share a wound, a forest, a debt, or a stage. The Directorate files those as <strong>entity groups</strong> and <strong>transformation chains</strong> — the LC analog of the three Birds of the Black Forest, not extra copies of SECC.</p>
<p>This article is the public extract of <code>SOMNARAK_ENTITIES.md</code>. Individual members still get their own dossier when published (the Observing / Weighting / Guarding Birds already sit behind SE-010 The Convergence).</p>
{p_html(groups[:2])}
</section>
<section class="wiki-section" id="groups"><h2 class="section-title">Linked groups</h2>
{inner}
</section>
<section class="wiki-section" id="chains"><h2 class="section-title">Transformation chains</h2>
{p_html(chain)}
<p>Chains are not Hope Transformations. A chain is sorrow becoming a worse or different sorrow. Hope is a Hand-of-Hope rewrite. Mixing the two categories is how you get The Extinguished.</p>
</section>
<section class="wiki-section" id="tales"><h2 class="section-title">Fairy-tale entities</h2>
{p_html(fairy)}
<p>Related: <a href="index.html">Sorrow Entities</a>, <a href="se-010-the-convergence.html">The Convergence</a>, <a href="se-014-the-debt-eater.html">The Debt Eater</a>.</p>
</section>
"""
    crumbs = '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Sorrow Entities</a> <i>/</i> <span>Entity Groups</span>'
    cats = '<a href="index.html">Sorrow Entities</a> | <a href="entity-groups-and-chains.html">Entity Groups</a>'
    doc = wrap(
        "Entity Groups and Transformation Chains",
        "Linked Sorrow sets: three birds, three sisters, masked troupe, debt triplets, and evolution chains.",
        crumbs,
        "Entity Groups and Transformation Chains",
        "SORROW ENTITIES",
        toc,
        body,
        cats,
    )
    emit(
        "entities/entity-groups-and-chains.html",
        doc,
        "Entity Groups and Transformation Chains",
        "Sorrow Entities",
        "Linked Sorrow sets and evolution chains.",
    )


# ---------------------------------------------------------------------------
# Ordeal colors
# ---------------------------------------------------------------------------

COLORS = {
    "BLUE": {
        "file": "ordeal-blue.html",
        "title": "Blue Ordeals — The Mourning Host",
        "han": "Lament (Deep Blue)",
        "theme": "Weeping, emotional assault, Composure drain, memory flood",
        "blurb": (
            "Blue Ordeals form from accumulated Lament Han. They weep, wail, and assault the mind. "
            "Multiple translucent figures drain Composure and force personnel to relive grief. "
            "They move in groups, moaning; their attacks are emotional rather than physical. "
            "A room of Blue Ordeals can reduce a team to weeping in seconds. Weak individually; overwhelming in swarms."
        ),
        "hex": "#38bdf8",
    },
    "BLACK": {
        "file": "ordeal-black.html",
        "title": "Black Ordeals — The Crushing Tide",
        "han": "Weight (Black)",
        "theme": "Crushing force, physical damage, structural destruction",
        "blurb": (
            "Black Ordeals form from accumulated Weight Han. They are slow, dense, and physically devastating. "
            "Dark, heavy figures crush, flatten, and press down. Attacks are purely physical — broken bones, "
            "collapsed corridors, pinned personnel. They move slowly but hit with the force of collapsing buildings. "
            "Resistant to emotional and identity attacks; vulnerable to overwhelming physical force or speed."
        ),
        "hex": "#94a3b8",
    },
    "PALE": {
        "file": "ordeal-pale.html",
        "title": "Pale Ordeals — The Fading",
        "han": "Void (Pale White)",
        "theme": "Erasure, identity theft, Clarity drain, absence",
        "blurb": (
            "Pale Ordeals form from accumulated Void Han. They erase identity, memory, presence, existence. "
            "Featureless pale-white figures drain Clarity and cause personnel to forget who they are, where they are, "
            "and why they came. Silent and cold. A Pale Ordeal does not kill the body; it erases the person inside it, "
            "leaving an empty shell that must be carried out."
        ),
        "hex": "#e2e8f0",
    },
    "GREY": {
        "file": "ordeal-grey.html",
        "title": "Grey Ordeals — The Resentful March",
        "han": "Grudge (desaturated Crimson)",
        "theme": "Hostility, aggression, violence, Resilience damage",
        "blurb": (
            "Grey Ordeals form from accumulated Grudge Han. They are hostile, aggressive, armed — injustice given form. "
            "Humanoid figures carry weapons of crystallized resentment (blades, hammers, chains). They hunt personnel, "
            "coordinate in groups, and fight with tactical intelligence. The most combat-intensive color; suppression "
            "requires trained teams with M.A.W. weapons."
        ),
        "hex": "#64748b",
    },
    "PURPLE": {
        "file": "ordeal-purple.html",
        "title": "Purple Ordeals — The Corruption",
        "han": "Raw Han / mixed",
        "theme": "Chaos, infection, parasitic transformation",
        "blurb": (
            "Purple Ordeals form from raw, unprocessed Han — the Weeping’s pressure leaking upward. "
            "They are the most chaotic color. Purple-tinged masses shift form, spawn smaller manifestations, "
            "infect facility Han-flow, and attempt to bond parasitically with personnel (temporary Fracture-like symptoms). "
            "Rarest and most dangerous: they corrupt, transform, and spread. Suppression needs force, grounding, and observation together."
        ),
        "hex": "#c084fc",
    },
}

WATCHES = ["First_Watch", "Second_Watch", "Third_Watch", "Tide_Watch"]
WATCH_LABEL = {
    "First_Watch": "First Watch (minor)",
    "Second_Watch": "Second Watch (moderate)",
    "Third_Watch": "Third Watch (major)",
    "Tide_Watch": "Tide Watch (catastrophic)",
}


def ordeal_names(color: str, watch: str) -> list[tuple[str, pathlib.Path]]:
    d = LORE / "04_Ordeals"
    out = []
    for p in sorted(d.glob(f"Ordeal_{color}_{watch}_*.md")):
        h1 = re.search(r"^# (.+)$", p.read_text(encoding="utf-8", errors="replace"), re.M)
        name = h1.group(1) if h1 else p.stem
        out.append((name, p))
    return out


def featured_paras(path: pathlib.Path) -> list[str]:
    t = path.read_text(encoding="utf-8", errors="replace")
    for h in ("Appearance", "Behavior", "Formation", "Overview"):
        paras = first_paras(extract_section(t, h), 2, 140)
        if paras:
            return paras
    return first_paras(t.split("\n", 2)[-1], 2, 140)


def build_ordeals():
    for color, meta in COLORS.items():
        watch_html = ""
        toc_items = [("overview", "Overview"), ("watches", "The four watches"), ("suppression", "Suppression")]
        for w in WATCHES:
            names = ordeal_names(color, w)
            label = WATCH_LABEL[w]
            sid = w.lower().replace("_", "-")
            toc_items.append((sid, label))
            lis = "".join(f"<li>{html.escape(n)}</li>" for n, _ in names)
            feat = ""
            if names:
                # prefer framework sample names when present
                pick = names[0][1]
                for n, path in names:
                    if any(k in n for k in ("Weeping Cluster", "Rolling Weight", "Forgotten", "Resentful Three", "Seeping", "Ocean of Tears", "Mountain", "Nothing", "Judge", "Fracture Wave")):
                        pick = path
                        break
                feat = p_html(featured_paras(pick))
            watch_html += f"""
<h3 id="{sid}">{html.escape(label)}</h3>
<p>Named {color.title()} {label.split('(')[0].strip()} manifestations on file:</p>
<ul>{lis}</ul>
{feat}
"""
        toc = toc_html(toc_items[:5])
        body = f"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p><strong>{html.escape(meta['title'])}</strong> are one of five Ordeal colors in the Hand of Change. Color is the Han type. Time (First / Second / Third / Tide Watch) is the severity. This page is the color article — the LC analog of Amber or Crimson Ordeals — not sixty separate stubs.</p>
<p>{html.escape(meta['blurb'])}</p>
{fact_table([("Color", color), ("Han source", meta["han"]), ("Theme", meta["theme"]), ("Mortality", "Ordeals are mortal. They are not Sorrow Entities. They cannot be contained or extracted into M.A.W.")])}
</section>
<section class="wiki-section" id="watches"><h2 class="section-title">The four watches</h2>
<p>One Ordeal per Time per day. Times escalate. First Watch is a warning that Han is accumulating. Tide Watch is a facility-wide crisis that only Echo-Cores and their top teams engage. An unsuppressed Tide Watch can permanently damage the Hand of Change.</p>
{watch_html}
</section>
<section class="wiki-section" id="suppression"><h2 class="section-title">Suppression</h2>
<p>Ordeals cannot be worked. Viderehan / Flerehan / Pugnahan / Ferrehan do not apply. They appear, they wander, they attack, and they must be destroyed. They yield no E.G.O. They do not return from the Weeping.</p>
<p>Hub: <a href="ordeals-framework.html">Ordeals framework</a>. Time axis: <a href="the-four-ordeals.html">The Four Watches</a>. Sister colors:
<a href="ordeal-blue.html">Blue</a> ·
<a href="ordeal-black.html">Black</a> ·
<a href="ordeal-pale.html">Pale</a> ·
<a href="ordeal-grey.html">Grey</a> ·
<a href="ordeal-purple.html">Purple</a>.</p>
</section>
"""
        crumbs = (
            '<a href="../index.html">Somnarak</a> <i>/</i> '
            '<a href="index.html">Mechanics</a> <i>/</i> '
            '<a href="ordeals-framework.html">Ordeals</a> <i>/</i> '
            f"<span>{html.escape(color.title())}</span>"
        )
        cats = (
            f'<a href="ordeals-framework.html">Ordeals</a> | '
            f'<a href="{meta["file"]}">{html.escape(color.title())}</a> | '
            f'<a href="index.html">Mechanics</a>'
        )
        doc = wrap(meta["title"], meta["blurb"][:220], crumbs, meta["title"], "ORDEAL COLOR", toc, body, cats)
        emit(f"mechanics/{meta['file']}", doc, meta["title"], "Ordeals", meta["blurb"][:220])


# ---------------------------------------------------------------------------
# Book of Regressor
# ---------------------------------------------------------------------------

def build_book():
    t = (LORE / "03_Unknown_Entities" / "Book_of_Regressor_Log_Dramaturgy.md").read_text(
        encoding="utf-8", errors="replace"
    )
    h1 = "The Book of Regressor"
    paras = first_paras(t, 8, 420)
    toc = toc_html([("overview", "Overview"), ("log", "The log"), ("place", "Where it belongs")])
    body = f"""
<section class="wiki-section" id="overview"><h2 class="section-title">Overview</h2>
<p>The Book of Regressor is a side story inside the Absolvohan — dramaturgy, not a Sorrow Entity. It speaks in the first person as the book that holds the loop. The one who loops wrote in its margins; the book is the cause of the turning, and they are the cost.</p>
<p>This is the LC analog of a Small Story or a Key Page story: it lives next to Daily Recordings, not on the Abnormalities list. Filing it as an Unknown Entity would be the same mistake as pasting Absolvohan day logs onto Floor 1.</p>
</section>
<section class="wiki-section" id="log"><h2 class="section-title">The log</h2>
{p_html(paras)}
</section>
<section class="wiki-section" id="place"><h2 class="section-title">Where it belongs</h2>
<p>Primary story hub: <a href="the-cycle-and-absolvohan.html">The Cycle and Absolvohan</a>. Related specimen (loop body): <a href="../entities/unk-902-the-repeated-survivor.html">The Repeated Survivor</a>. Unknown list: <a href="../entities/unknown-entities.html">Unknown Entities</a>.</p>
</section>
"""
    crumbs = '<a href="../index.html">Somnarak</a> <i>/</i> <a href="index.html">Lore</a> <i>/</i> <span>The Book of Regressor</span>'
    cats = '<a href="the-cycle-and-absolvohan.html">The Cycle</a> | <a href="index.html">Lore</a> | <a href="../entities/unknown-entities.html">Unknown Entities</a>'
    doc = wrap(h1, paras[0][:220] if paras else h1, crumbs, h1, "STORY / DRAMATURGY", toc, body, cats)
    emit("lore/the-book-of-regressor.html", doc, h1, "Lore & Cosmology", "Absolvohan side-story: the book that holds the loop.")


def patch_entity_hub():
    p = DOCS / "entities" / "index.html"
    t = p.read_text(encoding="utf-8")
    old = """      <nav class="abno-tabs" aria-label="Sorrow Entity pages">
        <a class="abno-tab is-on" href="index.html">SORROW ENTITIES</a>
        <a class="abno-tab" href="list.html">LIST OF SORROW ENTITIES</a>
      </nav>"""
    new = """      <nav class="abno-tabs" aria-label="Sorrow Entity pages">
        <a class="abno-tab is-on" href="index.html">SORROW ENTITIES</a>
        <a class="abno-tab" href="list.html">LIST OF SORROW ENTITIES</a>
        <a class="abno-tab" href="hope-transformations.html">HOPE TRANSFORMATIONS</a>
        <a class="abno-tab" href="unknown-entities.html">UNKNOWN ENTITIES</a>
      </nav>"""
    if old in t:
        t = t.replace(old, new)
    t = t.replace("wiki.css?v=20260830ad", f"wiki.css?v={CSSV}")
    rel = """          <li><a href="../mechanics/the-four-ordeals.html">Ordeals</a> — event-form sorrow that cannot be boxed.</li>"""
    rel2 = """          <li><a href="../mechanics/ordeals-framework.html">Ordeals</a> — five colors × four watches; mortal, not contained.</li>
          <li><a href="hope-transformations.html">Hope Transformations</a> — fourteen Dawn bonds, not SECC cells.</li>
          <li><a href="unknown-entities.html">Unknown Entities</a> — seven named specimens outside the thirteen dossiers.</li>
          <li><a href="entity-groups-and-chains.html">Entity groups</a> — birds, sisters, troupe, debt triplets.</li>"""
    if rel in t:
        t = t.replace(rel, rel2, 1)
    p.write_text(t, encoding="utf-8")
    print("patched entities/index.html tabs")


def patch_mechanics_hub():
    p = DOCS / "mechanics" / "index.html"
    t = p.read_text(encoding="utf-8")
    needle = '<a href="ordeals-framework.html" class="jump-btn">VIEW ORDEAL WAVES →</a></div>'
    extra = f"""
    <div class="pm-entity-card" style="--card-border:#38bdf8;"><div class="entity-card-top"><div class="entity-card-meta"><span class="risk-badge risk-he">BLUE</span></div></div><h3 class="entity-card-name">BLUE ORDEALS</h3><p class="entity-card-desc">The Mourning Host — Lament swarms that drain Composure.</p><a href="ordeal-blue.html" class="jump-btn">VIEW BLUE →</a></div>
    <div class="pm-entity-card" style="--card-border:#94a3b8;"><div class="entity-card-top"><div class="entity-card-meta"><span class="risk-badge risk-he">BLACK</span></div></div><h3 class="entity-card-name">BLACK ORDEALS</h3><p class="entity-card-desc">The Crushing Tide — Weight that flattens corridors.</p><a href="ordeal-black.html" class="jump-btn">VIEW BLACK →</a></div>
    <div class="pm-entity-card" style="--card-border:#e2e8f0;"><div class="entity-card-top"><div class="entity-card-meta"><span class="risk-badge risk-he">PALE</span></div></div><h3 class="entity-card-name">PALE ORDEALS</h3><p class="entity-card-desc">The Fading — Void that erases the person inside the body.</p><a href="ordeal-pale.html" class="jump-btn">VIEW PALE →</a></div>
    <div class="pm-entity-card" style="--card-border:#64748b;"><div class="entity-card-top"><div class="entity-card-meta"><span class="risk-badge risk-he">GREY</span></div></div><h3 class="entity-card-name">GREY ORDEALS</h3><p class="entity-card-desc">The Resentful March — Grudge infantry with crystallized weapons.</p><a href="ordeal-grey.html" class="jump-btn">VIEW GREY →</a></div>
    <div class="pm-entity-card" style="--card-border:#c084fc;"><div class="entity-card-top"><div class="entity-card-meta"><span class="risk-badge risk-he">PURPLE</span></div></div><h3 class="entity-card-name">PURPLE ORDEALS</h3><p class="entity-card-desc">The Corruption — raw Han that infects and spreads.</p><a href="ordeal-purple.html" class="jump-btn">VIEW PURPLE →</a></div>
"""
    if needle in t and "ordeal-blue.html" not in t:
        t = t.replace(needle, needle + extra, 1)
    t = t.replace("wiki.css?v=20260830ad", f"wiki.css?v={CSSV}")
    p.write_text(t, encoding="utf-8")
    print("patched mechanics/index.html ordeal colors")


def patch_search():
    sp = DOCS / "data" / "search.json"
    data = json.loads(sp.read_text(encoding="utf-8"))
    have = {e.get("url") for e in data}
    added = 0
    for e in SEARCH_NEW:
        if e["url"] not in have:
            data.append(e)
            added += 1
    sp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"search.json +{added} entries")


def main():
    print("=== Hope Transformations ===")
    build_ht()
    print("=== Unknown Entities ===")
    build_unknown()
    print("=== Entity groups ===")
    build_groups()
    print("=== Ordeal colors ===")
    build_ordeals()
    print("=== Book of Regressor ===")
    build_book()
    patch_entity_hub()
    patch_mechanics_hub()
    patch_search()
    print("done")


if __name__ == "__main__":
    main()
