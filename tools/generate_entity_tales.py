#!/usr/bin/env python3
"""Generate the public Entity Tales page from CANONICAL source.

Reads:
  REFERENCE_SOMNARAK_WIKI/LORE or REFERANCE/07_Reference/SOMNARAK_ENTITY_TALES.md
  REFERENCE_SOMNARAK_WIKI/LORE or REFERANCE/07_Reference/SOMNARAK_ENTITY_CODEX.md

Writes:
  docs/lore/entity-tales.html

The generator is idempotent. It preserves the existing global chrome (top bar,
left rail, footer) and only rewrites the <main> content, so it can be run again
after source edits without touching site-wide navigation.
"""

from __future__ import annotations

import argparse
import html
import os
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TALES_SRC = REPO / "REFERENCE_SOMNARAK_WIKI" / "LORE or REFERANCE" / "07_Reference" / "SOMNARAK_ENTITY_TALES.md"
CODEX_SRC = REPO / "REFERENCE_SOMNARAK_WIKI" / "LORE or REFERANCE" / "07_Reference" / "SOMNARAK_ENTITY_CODEX.md"
OUT_PAGE = REPO / "docs" / "lore" / "entity-tales.html"
SEARCH_INDEX = REPO / "docs" / "data" / "search.json"

# Existing public Sorrow Entity dossiers.  Full record pages remain scarce; most
# tale entities resolve to the registry, so the generator only links dossiers
# that actually exist.
DOSSIER_BY_NAME = {
    "The Orphaned Bell": "entities/se-001-the-orphaned-bell.html",
    "The Grieving Colossus": "entities/se-002-the-grieving-colossus.html",
    "The Wilderness Tide": "entities/se-003-the-wilderness-tide.html",
    "The Smothering Mother": "entities/se-005-the-smothering-mother.html",
    "Brume": "entities/se-007-brume.html",
    "The Memory Weaver": "entities/se-009-the-memory-weaver.html",
    "The Convergence": "entities/se-010-the-convergence.html",
    "The Whispering Walls": "entities/se-011-the-whispering-walls.html",
    "The Debt Eater": "entities/se-014-the-debt-eater.html",
    "The Debt Scale": "entities/se-015-the-debt-scale.html",
}

ELEMENT_COLORS = {
    "Lament": "#38bdf8",
    "Grudge": "#ef5b55",
    "Void": "#e2e8f0",
    "Weight": "#c9a86a",
    "Mixed": "#a78bfa",
}


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def clean_md(value: str) -> str:
    """Strip simple Markdown emphasis/code markers before HTML escaping."""
    return value.replace("**", "").replace("`", "").replace("*", "")


def slugify(value: str) -> str:
    value = value.replace("’", "'").replace("‘", "'")
    value = re.sub(r"[^A-Za-z0-9]+", "-", value).strip("-").lower()
    return value or "entity"


def load_codex() -> dict[str, tuple[str, str]]:
    """Return {code: (canonical_name, element)} from SOMNARAK_ENTITY_CODEX.md."""
    out: dict[str, tuple[str, str]] = {}
    if not CODEX_SRC.exists():
        return out
    text = CODEX_SRC.read_text(encoding="utf-8", errors="replace")
    for line in text.splitlines():
        m = re.match(
            r"\|\s*`((?:C|N|O|D|S|U)-[A-Za-z0-9αβγδω\-]+)\s*\[[A-Za-z]+\]`\s*\|\s*\[([^\]]+)\]",
            line,
        )
        if not m:
            continue
        code = m.group(1).strip()
        name = m.group(2).strip()
        # The table has an element in the third column, but some rows use a
        # plain parentheses tail; keep it optional.
        columns = line.split("|")
        element = ""
        if len(columns) >= 4:
            element = columns[3].strip()
        out[code] = (name, element)
    return out


def split_tale_blocks(body: str) -> dict[str, str]:
    """Split a tale body on its ### headings."""
    blocks: dict[str, str] = {}
    matches = list(re.finditer(r"^###\s+(.+?)\s*$", body, re.M))
    if not matches:
        return blocks
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        key = re.sub(r"\s*\(.+?\)\s*—\s*.+$", "", match.group(1)).strip().lower()
        if key == "":
            key = match.group(1).strip().lower()
        blocks[key] = body[match.end():end].strip()
    return blocks


def parse_tales() -> list[dict[str, object]]:
    text = TALES_SRC.read_text(encoding="utf-8", errors="replace")
    tales: list[dict[str, object]] = []
    # Split on the tale heading and process each chunk.  This keeps the full
    # body instead of stopping at the first line break.
    chunks = re.split(r"\n## Tale (\d+): ", text)
    # chunks[0] is the preamble; then pairs of (num, body).
    for index in range(1, len(chunks), 2):
        num = int(chunks[index])
        chunk = chunks[index + 1]
        title_line, _, body = chunk.partition("\n")
        title = title_line.strip()
        code_m = re.search(r"\*\*Designation:\*\*\s*`([^`]+)`", body)
        code = code_m.group(1).replace("SE-", "", 1) if code_m else ""

        # Korean name in the tale heading.
        korean = ""
        title_parts = re.search(r"^(.+?)\s*\(\s*(.*?)\s*\)$", title)
        if title_parts:
            title = title_parts.group(1).strip()
            korean = title_parts.group(2).strip()

        blocks = split_tale_blocks(body)

        # Narrative paragraphs.
        narrative_raw = blocks.get("이야기", "")
        narrative = []
        for para in re.split(r"\n\s*\n", narrative_raw):
            para = "\n".join(
                line.strip() for line in para.splitlines() if line.strip() and not line.strip().startswith(">")
            ).strip()
            if para:
                narrative.append(para)

        # Testimony blockquotes (lines beginning with >).
        testimony_raw = blocks.get("증언", "")
        testimony = []
        for line in testimony_raw.splitlines():
            line = line.strip()
            if not line.startswith(">"):
                continue
            content = line.lstrip(">").strip()
            content = re.sub(r"^\*", "", content).strip()
            # Remove the markdown italic marker that follows the quote and
            # precedes the speaker attribution (e.g. “...”* — Keeper).
            content = re.sub(r"\*\s*(—|–)", r"\1", content).strip()
            content = re.sub(r"\*$", "", content).strip()
            if content:
                testimony.append(content)

        # Record fields.
        record_raw = blocks.get("기록", "")
        record = parse_record(record_raw)
        addendum_raw = blocks.get("registry addendum", "")

        tales.append(
            {
                "num": num,
                "title": title,
                "korean": korean,
                "code": code,
                "narrative": narrative,
                "testimony": testimony,
                "record": record,
                "addendum": addendum_raw,
            }
        )
    return tales


def parse_record(raw: str) -> list[tuple[str, list[str]]]:
    """Parse the ### 기록 block into [(field, [value lines])]."""
    fields: list[tuple[str, list[str]]] = []
    current: tuple[str, list[str]] | None = None
    for line in raw.splitlines():
        line = line.rstrip()
        if not line.strip():
            continue
        m = re.match(r"^\*\*(.+?):\*\*\s*(.*)$", line.strip())
        if m:
            field_name = m.group(1).strip()
            value = m.group(2).strip()
            if current:
                fields.append(current)
            current = (field_name, [value] if value else [])
            continue
        stripped = line.strip()
        if current is not None:
            current[1].append(stripped)
        else:
            fields.append((stripped, []))
    if current:
        fields.append(current)
    return fields


def render_record(fields: list[tuple[str, list[str]]]) -> str:
    out = ['<div class="tale-record">']
    for name, values in fields:
        if not values:
            continue
        out.append(f"<div class=\"tale-record-row\"><span class=\"tale-record-key\">{esc(name)}</span>")
        content: list[str] = []
        bullets: list[str] = []
        for value in values:
            if value.startswith("- "):
                bullets.append(value[2:].strip())
            elif value.startswith("*"):
                bullets.append(value.lstrip("* ").strip())
            elif value:
                content.append(clean_md(value.strip()))
        if content:
            out.append(f"<span class=\"tale-record-value\">{esc(' '.join(content))}</span>")
        if bullets:
            out.append('<ul class="tale-record-list">')
            for bullet in bullets:
                out.append(f"<li>{esc(clean_md(bullet))}</li>")
            out.append("</ul>")
        out.append("</div>")
    out.append("</div>")
    return "\n".join(out)


def render_tale(tale: dict[str, object], codex: dict[str, tuple[str, str]]) -> str:
    num = int(tale["num"])
    title = str(tale["title"])
    korean = str(tale["korean"])
    code = str(tale["code"])
    narrative = list(tale["narrative"])
    testimony = list(tale["testimony"])
    record = list(tale["record"])

    canonical = title
    element = ""
    codex_entry = codex.get(code)
    if codex_entry:
        canonical = codex_entry[0]
        element = codex_entry[1]
    alias = canonical if canonical.lower() != title.lower() else ""

    anchor = f"tale-{num:03d}-{slugify(canonical)}"
    dossier = DOSSIER_BY_NAME.get(canonical)

    blocks = []
    blocks.append('<article class="tale-card" id="' + esc(anchor) + '">')
    blocks.append('<header class="tale-card-head">')
    blocks.append(
        f'<span class="tale-ordinal">TALE {num:03d}</span>'
    )
    blocks.append(f'<h3 class="tale-name">{esc(canonical)}</h3>')
    sub = []
    if korean:
        sub.append(esc(korean))
    if code:
        sub.append(f"SECC {esc(code)}")
    if element:
        sub.append(esc(element))
    if sub:
        blocks.append(f'<div class="tale-subline">{" · ".join(sub)}</div>')
    if alias:
        blocks.append(f'<div class="tale-alias">Tale epithet: {esc(alias)}</div>')
    if dossier:
        blocks.append(
            f'<a class="tale-dossier-link" href="../{esc(dossier)}">FULL DOSSIER →</a>'
        )
    else:
        blocks.append(
            '<a class="tale-dossier-link" href="../entities/list.html">SECC REGISTRY →</a>'
        )
    blocks.append("</header>")

    blocks.append('<div class="tale-card-body">')
    blocks.append('<section class="tale-block tale-narratio">')
    blocks.append('<h4 class="tale-block-title">I. 이야기 (NARRATIO) — THE TALE</h4>')
    for para in narrative:
        blocks.append(f'<p>{esc(clean_md(para))}</p>')
    if not narrative:
        blocks.append("<p>No narrative text recorded for this tale.</p>")
    blocks.append("</section>")

    blocks.append('<section class="tale-block tale-testimonium">')
    blocks.append('<h4 class="tale-block-title">II. 증언 (TESTIMONIUM) — THE TESTIMONY</h4>')
    for quote in testimony:
        blocks.append(f'<blockquote>{esc(clean_md(quote))}</blockquote>')
    if not testimony:
        blocks.append("<p>No testimony recorded for this tale.</p>")
    blocks.append("</section>")

    blocks.append('<section class="tale-block tale-registrum">')
    blocks.append('<h4 class="tale-block-title">III. 기록 (REGISTRUM) — THE RECORD</h4>')
    blocks.append(render_record(record))
    blocks.append("</section>")
    blocks.append("</div>")
    blocks.append("</article>")
    return "\n".join(blocks)


def render_index(tales: list[dict[str, object]], codex: dict[str, tuple[str, str]]) -> str:
    rows = []
    for tale in tales:
        num = int(tale["num"])
        canonical = str(tale["title"])
        codex_entry = codex.get(str(tale["code"]))
        if codex_entry:
            canonical = codex_entry[0]
        anchor = f"tale-{num:03d}-{slugify(canonical)}"
        rows.append(f'<a href="#{esc(anchor)}"><b>{num:03d}</b> {esc(canonical)}</a>')
    return '\n<nav class="tale-index" aria-label="Entity Tales index">\n' + "\n".join(rows) + "\n</nav>"


PAGE_STYLE = """<style>
  .tale-main .hero-banner{position:relative;padding:34px 38px;}
  .tale-mark{position:absolute;right:34px;top:34px;filter:drop-shadow(0 0 14px rgba(56,189,248,.25));}
  .tale-intro{color:#94a3b8;font-size:0.95rem;max-width:980px;line-height:1.7;margin:8px 0 26px;}
  .tale-index{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:6px;margin:18px 0 34px;padding:14px;background:rgba(6,10,18,.72);border:1px solid #1e293b;border-radius:4px;}
  .tale-index a{display:flex;gap:8px;align-items:baseline;color:#cbd5e1;text-decoration:none;font-family:'JetBrains Mono','Courier New',monospace;font-size:.76rem;padding:4px 6px;border-left:2px solid #1e293b;}
  .tale-index a:hover{color:#f1df76;border-left-color:#f1df76;background:rgba(15,23,42,.6);}
  .tale-index b{color:#64748b;font-weight:700;}
  .tale-card{border:1px solid #26344a;background:#060a12;padding:20px 22px;margin-bottom:24px;border-radius:4px;box-shadow:0 4px 22px rgba(0,0,0,.35);}
  .tale-card-head{display:flex;flex-wrap:wrap;align-items:flex-start;gap:10px 16px;margin-bottom:14px;padding-bottom:12px;border-bottom:1px solid #1e293b;}
  .tale-ordinal{font-family:'JetBrains Mono',monospace;font-size:.72rem;color:#64748b;letter-spacing:.12em;border:1px solid #334155;padding:3px 8px;border-radius:3px;align-self:center;}
  .tale-name{margin:0;color:#f8fafc;font-family:'Cinzel',serif;font-size:1.26rem;line-height:1.2;letter-spacing:.02em;}
  .tale-subline{color:#38bdf8;font-family:'JetBrains Mono',monospace;font-size:.78rem;width:100%;}
  .tale-alias{color:#f1df76;font-size:.8rem;font-family:'JetBrains Mono',monospace;width:100%;}
  .tale-dossier-link{margin-left:auto;align-self:center;color:#f1df76;text-decoration:none;font-family:'JetBrains Mono',monospace;font-size:.72rem;border:1px solid #334155;padding:5px 10px;border-radius:3px;}
  .tale-dossier-link:hover{background:rgba(241,223,118,.08);border-color:#f1df76;}
  .tale-card-body{display:grid;grid-template-columns:1fr;gap:14px;}
  .tale-block{background:#0b1120;border:1px solid #1e293b;border-radius:4px;padding:14px 16px;}
  .tale-block-title{margin:0 0 8px;color:#f1df76;font-family:'JetBrains Mono',monospace;font-size:.84rem;letter-spacing:.05em;}
  .tale-testimonium .tale-block-title{color:#38bdf8;}
  .tale-registrum .tale-block-title{color:#ef5b55;}
  .tale-block p{margin:0 0 12px;color:#94a3b8;line-height:1.72;font-size:.9rem;}
  .tale-block p:last-child{margin-bottom:0;}
  .tale-block blockquote{margin:0 0 12px;padding:8px 12px;color:#cbd5e1;font-style:italic;font-size:.88rem;border-left:3px solid #38bdf8;background:rgba(0,0,0,.3);}
  .tale-block blockquote:last-child{margin-bottom:0;}
  .tale-record{display:grid;gap:6px;}
  .tale-record-row{display:grid;grid-template-columns:minmax(160px,220px) 1fr;gap:12px;align-items:start;padding:5px 4px;border-bottom:1px dashed #1e293b;}
  .tale-record-row:last-child{border-bottom:0;}
  .tale-record-key{color:#64748b;font-family:'JetBrains Mono',monospace;font-size:.74rem;text-transform:uppercase;letter-spacing:.04em;}
  .tale-record-value{color:#94a3b8;font-size:.86rem;line-height:1.62;}
  .tale-record-list{margin:2px 0 6px;padding-left:18px;color:#94a3b8;font-size:.86rem;line-height:1.62;}
  .tale-addendum{margin:34px 0 24px;padding:16px 18px;background:#0b1120;border:1px solid #1e293b;border-radius:4px;color:#94a3b8;font-size:.86rem;line-height:1.7;}
  .tale-addendum strong{color:#cbd5e1;}
  @media (max-width:760px){.tale-record-row{grid-template-columns:1fr;}.tale-card-head{flex-direction:column;}.tale-dossier-link{margin-left:0;}}
</style>"""


def render_main(tales: list[dict[str, object]], codex: dict[str, tuple[str, str]]) -> str:
    cards = [render_tale(tale, codex) for tale in tales]
    addendum = ""
    first = next((tale for tale in tales if str(tale["addendum"]).strip()), None)
    if first is not None:
        addendum = (
            '<section class="tale-addendum" id="registry-addendum">'
            '<h4 class="tale-block-title">REGISTRY ADDENDUM — CANON SOURCE NOTE</h4>'
            "<p><strong>Source note.</strong> Every entity record in "
            "<code>SOMNARAK_ENTITY_TALES.md</code> is followed by the same "
            "operational interpretation / review requirement. The full addendum "
            "is reproduced once below so the twenty-four-six-tale anthology does "
            "not repeat it two hundred forty-six times.</p>"
            "<p>" + esc(clean_md(str(first["addendum"]).strip())) + "</p>"
            "</section>"
        )

    parts = [
        '<main class="content tale-main" id="content">',
        '  <div class="hero-banner" style="background: linear-gradient(135deg, rgba(8, 14, 26, 0.95), rgba(15, 23, 42, 0.9)), url(\'../assets/icons/banner_lore.svg\') center/cover;">',
        '    <div class="hero-badge">CANONICAL ANTHOLOGY // ARCHIVAL SECTION 09</div>',
        '    <h1 class="hero-title">ENTITY TALES (슬픔의 이야기)</h1>',
        '    <p class="hero-subtitle">The tripartite narrative records of Somnarak\'s Sorrow Entities — 이야기 (The Tale), 증언 (The Testimony), 기록 (The Directorate Record) — published in source order from <code>SOMNARAK_ENTITY_TALES.md</code>.</p>',
        '    <svg class="tale-mark" viewBox="0 0 96 96" width="96" height="96" role="img" aria-label="Entity Tales sigil: a weeping ring of story rings" xmlns="http://www.w3.org/2000/svg">',
        '      <circle cx="48" cy="48" r="40" fill="none" stroke="#f1df76" stroke-width="2"/>',
        '      <circle cx="48" cy="48" r="30" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="8 5"/>',
        '      <path d="M48 18 C30 30 30 44 48 52 C66 44 66 30 48 18 Z" fill="none" stroke="#cbd5e1" stroke-width="1.5"/>',
        '      <circle cx="48" cy="62" r="3" fill="#ef5b55"/>',
        '    </svg>',
        '  </div>',
        '  <div class="article-body">',
        '    <div class="toc" id="toc">',
        '      <div class="toc-title">Contents</div>',
        '      <div class="toc-body"><ol><li><a href="#entity-tales-index">Entity Tales Index (246)</a></li></ol></div>',
        '    </div>',
        '    <section class="tale-intro" id="entity-tales-index">',
        '      <h2 class="section-title">ENTITY TALES INDEX</h2>',
        '      <p>{0} canonical Sorrow Entity narrative records, source-led from each entity record. Every entry keeps its SECC designation, codename, Korean name, full tale, testimony, and directorate record. Codenames published below are the canonical names from the SECC/Entity Codex; missing fields are omitted rather than invented.</p>'.format(len(tales)),
    ]
    parts.append("    </section>")
    parts.append(render_index(tales, codex))
    parts.append("    <section class=\"tale-collection\">")
    parts.append("\n".join(cards))
    parts.append("    </section>")
    parts.append(addendum)
    parts.append("  </div>")
    parts.append("</main>")
    return "\n".join(parts)


def update_search_entry(tales: list[dict[str, object]]) -> None:
    if not SEARCH_INDEX.exists():
        return
    import json
    entries = json.loads(SEARCH_INDEX.read_text(encoding="utf-8"))
    names = [str(tale["title"]) for tale in tales]
    for entry in entries:
        if entry.get("url") == "lore/entity-tales.html":
            entry["description"] = (
                "Canonical narrative chronicles, survivor testimonies, and "
                "Directorate records for all 246 Sorrow Entities."
            )
            entry["keywords"] = " ".join(
                ["Entity Tales (슬픔의 이야기)", "Lore & Cosmology", "lore", *names[:246]]
            )
            break
    SEARCH_INDEX.write_text(json.dumps(entries, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate docs/lore/entity-tales.html from canon.")
    parser.add_argument("--dry-run", action="store_true", help="print counts without writing")
    args = parser.parse_args()

    if not TALES_SRC.exists():
        print(f"FAIL: missing source {TALES_SRC}", file=sys.stderr)
        return 1
    if not OUT_PAGE.exists():
        print(f"FAIL: missing output template {OUT_PAGE}", file=sys.stderr)
        return 1

    tales = parse_tales()
    codex = load_codex()
    print(f"parsed {len(tales)} tales; codex {len(codex)} entries")

    main_html = render_main(tales, codex)

    if args.dry_run:
        print(f"dry run: page sections ok, tales {len(tales)}, bytes {len(main_html)}")
        return 0

    template = OUT_PAGE.read_text(encoding="utf-8", errors="replace")
    # Remove generator-injected style blocks so reruns stay idempotent.
    template = re.sub(r"<style>.*?</style>", "", template, flags=re.S)
    start = template.find('<main class="content tale-main" id="content">')
    end = template.find("</main>", start)
    if start < 0 or end < 0:
        print("FAIL: unable to locate <main> in entity-tales.html", file=sys.stderr)
        return 1

    before = template[:start]
    after = template[end + len("</main>"):].lstrip()
    style_url = re.sub(r"(</head>)", PAGE_STYLE + r"\1", before, count=1)
    new_page = style_url + main_html + "\n" + after
    OUT_PAGE.write_text(new_page, encoding="utf-8")
    update_search_entry(tales)
    print(f"PASS: wrote {OUT_PAGE} ({OUT_PAGE.stat().st_size} bytes) after source rebuild")
    return 0


if __name__ == "__main__":
    sys.exit(main())
