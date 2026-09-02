#!/usr/bin/env python3
"""Generate M.A.W. item pages from the Codex Set Registry.

Reads item records from
``REFERENCE_SOMNARAK_WIKI/LORE or REFERANCE/M.A.W. Codex_Set Registry``
(files named ``<DONOR>-<SLOT>__MAW-<W|S|G>_<Name>.md``) and publishes one
public page per item under ``docs/maw/``, with a per-item source-led SVG
composition under ``docs/assets/art/maw/``.

The tool is idempotent: items whose page file already exists are skipped,
so the registry can be re-run after new records are added.

Usage:
    python tools/generate_maw_items.py            # publish all missing items
    python tools/generate_maw_items.py --dry-run  # report only
    python tools/generate_maw_items.py --limit N  # at most N new pages

Every generated page carries only text that exists in the source record or
in the site's own established template language. Missing fields are left
out rather than invented.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "REFERENCE_SOMNARAK_WIKI" / "LORE or REFERANCE" / "M.A.W. Codex_Set Registry"
DOCS = ROOT / "docs"
MAW_DIR = DOCS / "maw"
ART_DIR = DOCS / "assets" / "art" / "maw"

TEMPLATE_PAGE = MAW_DIR / "maw-w-001-01-the-laments-requiem.html"

GRADE_LABEL = {"α": "Minor", "β": "Moderate", "γ": "Major", "δ": "Critical"}
ELEMENT_COLOR = {
    "Lament": "#3e8bd5",
    "Grudge": "#d64a4a",
    "Void": "#8a8f98",
    "Weight": "#c9a86a",
    "Mixed": "#777777",
}
TYPE_LABEL = {"W": "Weapon", "S": "Suit", "G": "Gift"}
TYPE_RANK = {"W": 0, "S": 1, "G": 2}

# Entity pages that exist (donor code -> ../entities/ file)
ENTITY_PAGES: dict[str, str] = {}


def find_entity_pages() -> None:
    global ENTITY_PAGES
    pattern = re.compile(r"^se-(\d{3})-.*\.html$")
    for p in sorted((DOCS / "entities").glob("se-*.html")):
        m = pattern.match(p.name)
        if m and "field-record" not in p.name:
            ENTITY_PAGES[f"SE-{m.group(1)}"] = f"../entities/{p.name}"


def slugify(name: str) -> str:
    s = name.lower().replace("’", "").replace("'", "")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return re.sub(r"-{2,}", "-", s)


def donor_id(donor: str) -> tuple[str, int]:
    """Return (filename token, sort key) for a donor code."""
    if donor.startswith("SE-"):
        n = int(donor.split("-")[1])
        return f"{n:03d}", n * 2
    if donor.startswith("UNK_"):
        n = int(donor.split("_")[1])
        return f"unk{n}", 100000 + n
    raise ValueError(donor)


def donor_display(donor: str) -> str:
    return donor.replace("UNK_", "UNK-")


def parse_record(text: str) -> dict:
    f: dict = {}

    def first(pattern: str, group: int = 1, flags=re.M | re.I):
        m = re.search(pattern, text, flags)
        return m.group(group).strip() if m else None

    def row(key: str):
        for m in re.finditer(rf"\|\s*\**{re.escape(key)}\**\s*\|\s*([^|\n]+?)\s*\|", text, re.I):
            line_end = text.find("\n", m.end())
            if line_end != -1:
                nxt_end = text.find("\n", line_end + 1)
                nxt = text[line_end + 1 : nxt_end if nxt_end != -1 else len(text)]
                if re.match(r"^\s*\|[\s:\-|]+$", nxt) and "-" in nxt:
                    continue  # matched row is a table header, skip
            return m.group(1).strip()
        return None

    def bold(key: str):
        m = re.search(rf"\*\*{re.escape(key)}:?\*\* *([^\n]+?) *$", text, re.M)
        return m.group(1).strip() if m else None

    def bullet(key: str):
        m = re.search(rf"^\s*[-*]\s*{re.escape(key)}: (.+)$", text, re.M)
        return m.group(1).strip() if m else None

    f["name"] = first(r"^# M\.A\.W\. \w+ — (.+)$")
    f["flavor"] = first(r"^> \*“?(.+?)”?\* ?$")
    f["doc_id"] = first(r"\*\*Document ID:\*\* *`([^`]+)`")
    ent = re.search(r"\*\*Linked Entity:\*\* *`?(SE-\d+|UNK-\d+)`? — ([^\n]+)", text)
    f["entity"] = ent.group(1) if ent else None
    f["entity_name"] = ent.group(2).strip() if ent else None
    f["code"] = first(r"\*\*Item Registry Code:\*\* *`([^`]+)`")
    f["author"] = first(r"\*\*Author:\*\* *([^\n]+)")
    f["date"] = first(r"\*\*Date:\*\* *([^\n]+)")
    f["classification"] = first(r"\*\*Classification:\*\* *([^\n]+)")
    f["set_completion"] = first(r"\*\*Codex Set Completion:\*\* *`([^`]+)`")

    f["type_raw"] = row("Type") or bold("Type")
    f["grade_raw"] = row("Grade") or bold("Grade")
    f["element_raw"] = row("Element") or bold("Element")
    f["appearance"] = row("Appearance")
    f["damage"] = row("Damage") or bold("Damage")
    f["speed_range"] = row("Speed / Range") or bold("Speed / Range")
    f["speed"] = row("Speed") or bold("Speed")
    f["range"] = row("Range") or bold("Range")
    f["pattern"] = row("Attack Pattern") or row("Pattern") or bold("Pattern")
    f["coverage"] = row("Target Coverage") or row("Coverage") or bold("Coverage")
    f["falloff"] = row("Falloff Rule") or row("Falloff") or bold("Falloff")
    f["max_raw"] = row("Max Amount") or row("Maximum Amount") or bold("Max Amount")
    f["echo_raw"] = row("Echo cost") or row("Echo Cost") or bold("Echo cost") or bold("Echo Cost")
    f["ability_name"] = first(r"^### Ability — (.+)$")
    f["canonical_ability"] = row("Canonical ability")
    f["bearer_cost"] = row("Bearer cost") or bold("Cost") or bold("Bearer cost")
    f["limit"] = bold("Limit")
    f["corrosion"] = bold("Corrosion")
    f["maintenance"] = bold("Maintenance")
    f["shutdown"] = bold("Shutdown")

    for el in ("Lament", "Grudge", "Void", "Weight"):
        f[f"res_{el}"] = row(f"{el} resistance")

    # Ability body: section after "### Ability — X" up to the next ### or doc footer
    ab = re.search(r"^### Ability — .+?\n\n(.*?)(?=\n### |\n\*\*Document ID:|\n---)", text, re.M | re.S)
    f["ability_body"] = ab.group(1).strip() if ab else None
    if f["ability_body"]:
        body = re.sub(r"(?m)^[ \t]*\*\*Limit:\*\*.*$", "", f["ability_body"])
        body = re.sub(r"(?m)^[ \t]*\*\*(?:Cost|Bearer cost):\*\*.*$", "", body)
        lines = body.split("\n")
        while lines and re.match(r"^\s*\*\*(?:Damage|Speed(?:\s*/\s*Range)?|Range|Pattern|Coverage|Falloff|Target Coverage|Falloff Rule)\b", lines[0]):
            lines.pop(0)
        f["ability_body"] = "\n".join(lines).strip() or None

    inc = re.search(r"^### Incident Record\n\n(.*?)(?=\n### |\n\*\*Document ID:|\n---)", text, re.M | re.S)
    if not inc:
        inc = re.search(r"\*\*Incident — ([^:]+):\*\* *([^\n]+)", text)
        if inc:
            f["incident_name"] = inc.group(1).strip()
            f["incident"] = inc.group(2).strip()
    if inc and f.get("incident") is None:
        f["incident"] = re.sub(r"\s+", " ", inc.group(1)).strip()
        f.setdefault("incident_name", None)

    # Inline summary line: "**δ Mixed; L/G/V/W ...; max 2; 45 Echoes.** ..."
    inline = re.search(r"\*\*([αβγδεω]) ([A-Za-z]+); (L/G/V/W) ([\d./]+); max (\d+); (\d+) Echoes\.\*\* *(.+)", text)
    if inline:
        if not f.get("grade_raw"):
            f["grade_raw"] = inline.group(1)
        if not f.get("element_raw"):
            f["element_raw"] = inline.group(2)
        if not f.get("max_raw"):
            f["max_raw"] = inline.group(5)
        if not f.get("echo_raw"):
            f["echo_raw"] = inline.group(6) + " Sorrow Echoes"
        if not f["appearance"] and not f["ability_body"]:
            f["ability_body"] = inline.group(7).strip()

    # Format C: bold "Grade / Element:" field + CORE STATISTICS value row
    ge = re.search(r"\*\*Grade\s*/\s*Element:\*\* *([αβγδεω])\s*/\s*([A-Za-z]+)", text)
    if ge:
        if not f.get("grade_raw"):
            f["grade_raw"] = ge.group(1)
        if not f.get("element_raw"):
            f["element_raw"] = ge.group(2)
    cs = re.search(
        r"\|\s*Damage\s*\|\s*Speed\s*\|[^|\n]*\|\s*Pattern\s*/\s*Falloff\s*\|\s*Maximum\s*/\s*Echo Cost\s*\|\n"
        r"\|[\s:\-|]+\|\n\|([^|\n]+)\|([^|\n]+)\|([^|\n]+)\|([^|\n]+)\|([^|\n]+)\|",
        text,
    )
    if cs:
        def cell(v: str) -> str | None:
            v = v.strip()
            return None if v in ("", "—", "–", "-") else v
        if not f.get("damage"):
            f["damage"] = cell(cs.group(1))
        if not f.get("speed"):
            f["speed"] = cell(cs.group(2))
        if not f.get("range"):
            f["range"] = cell(cs.group(3))
        pf = [x.strip() for x in cs.group(4).split("/")]
        if len(pf) == 2:
            if not f.get("pattern"):
                f["pattern"] = cell(pf[0])
            if not f.get("falloff"):
                f["falloff"] = cell(pf[1])
        mc = [x.strip() for x in cs.group(5).split("/")]
        if len(mc) == 2:
            if not f.get("max_raw"):
                f["max_raw"] = cell(mc[0])
            if not f.get("echo_raw"):
                f["echo_raw"] = cell(mc[1])
    # Format C extras: SECC designation, binding rule, failure bullets, item history
    f["secc"] = first(r"\*\*Source SECC Designation:\*\* *`([^`]+)`")
    if not f.get("canonical_ability"):
        f["canonical_ability"] = bold("Canonical ability")
    if not f.get("limit"):
        f["limit"] = bold("Binding rule") or bold("Failure mode")
    if not f.get("corrosion"):
        c_bits = []
        for key, label in (("First sign", "First sign"), ("Escalation", "Escalation"), ("Terminal state", "Terminal state")):
            v = bullet(key)
            if v:
                c_bits.append(f"{label}: {v}")
        if c_bits:
            f["corrosion"] = " ".join(c_bits)
    if not f.get("incident"):
        h = re.search(r"## ITEM-SPECIFIC HISTORY[^\n]*\n\n(.*?)(?=\n## |\n\*\*Document ID:|\n---)", text, re.S)
        if h:
            f["incident"] = re.sub(r"\s+", " ", h.group(1)).strip()
            f.setdefault("incident_name", None)

    # grade/element cleanup: take the base token before an em dash
    g = f.get("grade_raw") or ""
    f["grade"] = g[0] if g and g[0] in "αβγδεω" else None
    e = f.get("element_raw") or ""
    f["element"] = e.split(" — ")[0].strip() if e else None
    f["element_sub"] = e.split(" — ")[1].strip() if " — " in e else None
    t = f.get("type_raw") or ""
    f["subtype"] = t.split(" — ")[1].strip() if " — " in t else None

    # element fallback: the damage line leads with the element name
    if not f["element"]:
        dm0 = re.match(r"^(Lament|Grudge|Void|Weight|Mixed)\b", f.get("damage") or "")
        if dm0:
            f["element"] = dm0.group(1)
    # keep the raw damage value; only rebuild it when it lacks the element lead
    if f.get("damage") and not re.match(r"^(Lament|Grudge|Void|Weight|Mixed)\s+\d", f["damage"]):
        m = re.search(r"(\d+)(?:–|-)(\d+)", f["damage"])
        if m:
            f["damage"] = f"{f['element'] or ''} {m.group(1)}–{m.group(2)}".strip()

    return f


def color_for(element: str | None) -> str:
    return ELEMENT_COLOR.get(element or "", "#3e8bd5")


def make_svg(code: str, name: str, itype: str, color: str, seed: int) -> str:
    """Source-led 400x400 item art. Geometry is seeded from the registry
    code so every composition is structurally unique (the SVG audit's
    cross-subject recolor check)."""
    rnd = lambda i: (seed >> (i % 28) * 8) & 0xFF  # noqa: E731
    uid = hashlib.sha1(code.encode()).hexdigest()[:6]
    bg, gl = f"bg{uid}", f"gl{uid}"
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%" role="img" aria-label="{html.escape(name.upper())}">',
        f"  <defs>",
        f'    <radialGradient id="{bg}" cx="50%" cy="42%" r="58%">',
        f'      <stop offset="0%" stop-color="#111827"/>',
        f'      <stop offset="100%" stop-color="#030712"/>',
        f'    </radialGradient>',
        f'    <radialGradient id="{gl}" cx="50%" cy="46%" r="42%">',
        f'      <stop offset="0%" stop-color="{color}" stop-opacity=".22"/>',
        f'      <stop offset="100%" stop-color="#000" stop-opacity="0"/>',
        f"    </radialGradient>",
        f"  </defs>",
        f'  <rect x="6" y="6" width="388" height="388" rx="14" fill="url(#{bg})" stroke="{color}" stroke-width="2.4"/>',
        f'  <rect x="14" y="14" width="372" height="372" rx="10" fill="none" stroke="#f1df76" stroke-width="1" stroke-dasharray="7 4" opacity=".35"/>',
        f'  <circle cx="200" cy="188" r="{110 + rnd(0) % 40}" fill="url(#{gl})"/>',
    ]
    cx, cy = 200.0, 190.0
    rot = rnd(1) % 27 - 13  # -13..13 degrees
    if itype == "W":
        length = 150 + rnd(2) % 90        # 150..239
        half_w = 7 + rnd(3) % 11          # 7..17
        tip_dx = rnd(4) % 26 - 13         # tip lateral offset
        guard = 26 + rnd(5) % 26
        pommel = 5 + rnd(6) % 6
        top = (cx + tip_dx, cy - length)
        mid_l = (cx - half_w, cy - length * 0.35)
        mid_r = (cx + half_w, cy - length * 0.30)
        blade = (
            f"M{cx - guard} {cy} L{mid_l[0]:.1f} {mid_l[1]:.1f} L{top[0]:.1f} {top[1]:.1f} "
            f"L{mid_r[0]:.1f} {mid_r[1]:.1f} L{cx + guard} {cy} Z"
        )
        parts.append(f'  <g transform="rotate({rot} {cx} {cy})">')
        parts.append(f'    <path d="{blade}" fill="{color}" fill-opacity=".28" stroke="{color}" stroke-width="3"/>')
        parts.append(f'    <path d="M{cx} {cy} L{top[0]:.1f} {top[1]:.1f}" fill="none" stroke="#e0f2fe" stroke-width="1.4" opacity=".8"/>')
        ticks = 3 + rnd(7) % 4
        for k in range(ticks):
            t0 = 0.35 + k * (0.5 / ticks)
            tx = cx + (top[0] - cx) * t0
            ty = cy + (top[1] - cy) * t0
            parts.append(f'    <path d="M{tx - 6:.1f} {ty:.1f} L{tx + 6:.1f} {ty + 4:.1f}" fill="none" stroke="#e0f2fe" stroke-width="1" opacity=".5"/>')
        parts.append(f'    <rect x="{cx - guard - 8:.1f}" y="{cy - 4:.1f}" width="{2 * guard + 16:.1f}" height="8" rx="3" fill="{color}" fill-opacity=".5"/>')
        parts.append(f'    <rect x="{cx - 7:.1f}" y="{cy + 4:.1f}" width="14" height="46" rx="5" fill="#1f2937" stroke="{color}" stroke-width="2"/>')
        parts.append(f'    <circle cx="{cx:.1f}" cy="{cy + 58:.1f}" r="{pommel}" fill="{color}" fill-opacity=".7"/>')
        parts.append("  </g>")
    elif itype == "S":
        w = 60 + rnd(2) % 40              # half shoulder width 60..99
        h = 80 + rnd(3) % 44
        notch = 12 + rnd(4) % 20
        plate = (
            f"M{cx - w} {cy - h * 0.2} L{cx - w * 0.4} {cy - h * 0.55} L{cx - notch} {cy - h * 0.75} "
            f"L{cx + notch} {cy - h * 0.75} L{cx + w * 0.4} {cy - h * 0.55} L{cx + w} {cy - h * 0.2} "
            f"L{cx + w * 0.75} {cy + h * 0.55} L{cx} {cy + h * 0.8 + notch} L{cx - w * 0.75} {cy + h * 0.55} Z"
        )
        parts.append(f'  <g transform="rotate({rot} {cx} {cy})">')
        parts.append(f'    <path d="{plate}" fill="{color}" fill-opacity=".22" stroke="{color}" stroke-width="3"/>')
        parts.append(f'    <path d="M{cx - w * 0.75:.1f} {cy - h * 0.35:.1f} L{cx + w * 0.75:.1f} {cy - h * 0.35:.1f}" fill="none" stroke="{color}" stroke-width="1.6" opacity=".7"/>')
        core_r = 14 + rnd(5) % 14
        parts.append(f'    <circle cx="{cx:.1f}" cy="{cy + 6:.1f}" r="{core_r}" fill="none" stroke="#e0f2fe" stroke-width="2" opacity=".8"/>')
        parts.append(f'    <circle cx="{cx:.1f}" cy="{cy + 6:.1f}" r="{core_r - 6}" fill="{color}" fill-opacity=".5"/>')
        lapels = 2 + rnd(6) % 3
        for k in range(lapels):
            ly = cy + h * 0.15 + k * 16
            parts.append(f'    <path d="M{cx - 20:.1f} {ly:.1f} L{cx + 20:.1f} {ly + 6:.1f}" fill="none" stroke="{color}" stroke-width="1.2" opacity=".55"/>')
        parts.append("  </g>")
    else:  # G — carried talisman
        outer = 68 + rnd(2) % 34
        inner = outer * 0.55
        glyph_n = 3 + rnd(3) % 3
        parts.append(f'  <g transform="rotate({rot} {cx} {cy - 10})">')
        parts.append(f'    <circle cx="{cx:.1f}" cy="{cy - 10:.1f}" r="{outer}" fill="{color}" fill-opacity=".16" stroke="{color}" stroke-width="3"/>')
        parts.append(f'    <circle cx="{cx:.1f}" cy="{cy - 10:.1f}" r="{inner:.1f}" fill="none" stroke="{color}" stroke-width="1.6" opacity=".8"/>')
        for k in range(glyph_n):
            ang = (seed >> k) % 360
            r2 = inner * (0.5 + (rnd(8 + k) % 40) / 100.0)
            x1 = cx + inner * 0.9 * ((ang % 360) / 60.0 - 0.5)
            y1 = cy - 10 - r2
            x2 = cx + (r2 * 0.7) * (((ang * 7) % 100) / 50.0 - 1)
            y2 = cy - 10 + r2 * 0.6
            parts.append(f'    <path d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}" fill="none" stroke="#e0f2fe" stroke-width="1.6" opacity=".75"/>')
        parts.append(f'    <circle cx="{cx:.1f}" cy="{cy - 10:.1f}" r="8" fill="{color}" fill-opacity=".7"/>')
        parts.append(f'    <path d="M{cx:.1f} {cy - 10 + outer:.1f} L{cx - 10:.1f} {cy + 62:.1f} L{cx + 10:.1f} {cy + 62:.1f} Z" fill="{color}" fill-opacity=".4"/>')
        parts.append("  </g>")
    code_x = 16 + rnd(9) % 6
    parts.append(f'  <text x="{code_x}" y="380" font-family="monospace" font-size="15" letter-spacing="2" fill="{color}">{html.escape(code)}</text>')
    parts.append("</svg>")
    return "\n".join(parts)


def esc(s: str | None) -> str:
    return html.escape(s or "", quote=True)


def md_paras(s: str | None) -> str:
    """Render source text (with **bold** and line breaks) as <p> blocks."""
    if not s:
        return ""
    out = []
    for para in re.split(r"\n\s*\n", s):
        para = para.strip()
        if not para:
            continue
        para = esc(para)
        para = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", para)
        para = para.replace("\n", "<br/>")
        out.append(f"<p>{para}</p>")
    return "".join(out)


def table_rows(rows: list[tuple[str, str | None]]) -> str:
    body = "".join(
        f"<tr><td><strong>{esc(k)}</strong></td><td>{esc(v)}</td></tr>" for k, v in rows if v
    )
    if not body:
        return ""
    return (
        '<div class="table-wrap"><table class="data-table">'
        f"<thead><tr><th>Field</th><th>Record</th></tr></thead><tbody>{body}</tbody></table></div>"
    )


def build_content(item: dict) -> str:
    f = item["fields"]
    color = item["color"]
    t = item["type"]
    donor_disp = donor_display(item["donor"])
    ent_page = ENTITY_PAGES.get(item["donor"])
    donor_text = f"{donor_disp} — {f['entity_name']}"
    donor_ref = (
        f'<a href="{ent_page}">{esc(donor_text)}</a>' if ent_page else esc(donor_text)
    )
    grade = (f"{f['grade']} — {GRADE_LABEL[f['grade']]}" if f["grade"] in GRADE_LABEL else f["grade"]) if f["grade"] else None
    element = f"{f['element']} — {f['element_sub']}" if f.get("element_sub") else f["element"]
    hero_span = " · ".join(x for x in [TYPE_LABEL[t], grade, element] if x)
    img = f'../assets/art/maw/{item["art_name"]}?v={ASSET_VERSION}'
    code = f["code"] or item["code"]

    pills = []
    for tt in ("W", "S", "G"):
        sib = item["siblings"][tt]
        label = {"W": "WPN", "S": "SUIT", "G": "GIFT"}[tt]
        dtok = item["donor_token"]
        if dtok.startswith("unk"):
            label += f"-U{dtok[3:]}"
        else:
            label += f"-{dtok}"
        cls = "jump-pill active" if tt == t else "jump-pill"
        pills.append(f'<a href="{sib}" class="{cls}">{label}</a>')
    pills.append('<a href="index.html" class="jump-pill">✦ Arsenal Hub</a>')

    c = []
    c.append('<!-- Tactical Fast-Jump Subpage Bar -->')
    c.append('<div class="fast-jump-nav">')
    c.append('  <span class="fast-jump-title">/// RAPID JUMP:</span>')
    c.append('  <div class="fast-jump-pills">')
    c.append("    " + " ".join(pills))
    c.append("  </div>")
    c.append("</div>")
    c.append('<!-- Tactical Directive Status HUD -->')
    c.append('<div class="tactical-directive-box">')
    c.append('  <div class="directive-text">')
    c.append('    <span class="led-dot led-green"></span> <b>STATUS:</b> ARCHIVE VERIFIED &nbsp;|&nbsp;')
    c.append("    <b>CLEARANCE:</b> LEVEL-4 OVERSIGHT &nbsp;|&nbsp;")
    c.append("    <b>PROTOCOL:</b> REVERIE DIRECTORATE")
    c.append("  </div>")
    c.append('  <img src="../assets/icons/hud_resonance_wave.svg" alt="Resonance Wave" class="directive-wave">')
    c.append("</div>")
    c.append('<div class="page-tabs"><span>M.A.W. Equipment</span><b>MAIN CANON</b></div>')
    c.append(f'<div class="breadcrumbs"><a href="../index.html">Main page</a><i>›</i><a href="index.html">M.A.W. Equipment</a><i>›</i>{esc(code)}</div>')
    c.append(f'<section class="item-hero enriched" style="--item:{color}"><img alt="Illustration of {esc(f["name"])}" class="item-portrait" src="{img}"/><div><span>{esc(hero_span)}</span><h1>{esc(f["name"])}</h1><p>Materialized Agony Wear of {donor_ref}</p><i><img alt="" src="../assets/icons/{ "weapon" if t == "W" else "suit" if t == "S" else "gift" }.svg"/>{esc(code)}</i></div></section>')

    if f.get("flavor"):
        c.append(f'<blockquote class="entity-quote" style="--entity:{color}">“{esc(f["flavor"])}”</blockquote>')

    # FUNCTION / PRICE
    ability_text = f.get("ability_body") or f.get("canonical_ability")
    price_text = f.get("bearer_cost")
    func = md_paras(ability_text) or "<p>Unrecorded in the registry.</p>"
    price = md_paras(price_text) or "<p>Unrecorded in the registry.</p>"
    c.append(f'<section class="item-mechanic" style="--item:{color}"><article><span>FUNCTION</span>{func}</article><article><span>PRICE</span>{price}</article></section>')

    # Body
    b = []
    b.append('<div class="item-columns"><article class="article-body">')
    b.append('<h2 id="overview">Overview</h2>')
    b.append(
        f"<p><strong>{esc(f['name'])}</strong> is the registered {TYPE_LABEL[t].lower()} expression of "
        f"{donor_ref}. Its function, restriction, and cost are inseparable: the item carries a usable "
        f"form of {esc(f['element'] or 'sorrow')} while preserving the failure or obligation that shaped its source.</p>"
    )
    if f.get("appearance"):
        b.append('<h2 id="appearance">Appearance</h2>')
        b.append(f"<p>{esc(f['appearance'])}</p>")
    elif f.get("subtype"):
        b.append('<h2 id="appearance">Appearance</h2>')
        b.append(f"<p>Filed as {esc(f['subtype'])}.</p>")
    b.append('<h2 id="extraction-or-bestowal">Extraction or Bestowal</h2>')
    ext = (
        f"Extraction follows an approved Named Vigil or equivalent Floor 2 rite as recorded on the "
        f'<a href="maw-crafting-and-extraction.html">extraction protocols</a> sheet.'
    )
    if f.get("author"):
        ext += f" The registry sheet was filed by {esc(f['author'])}."
    if f.get("date"):
        ext += f" Filing date: {esc(f['date'])}."
    if f.get("classification"):
        ext += f" Classification: {esc(f['classification'])}."
    if f.get("set_completion"):
        ext += f" Codex set completion is recorded at {esc(f['set_completion'])}."
    b.append(f"<p>{ext}</p>")
    if f.get("limit"):
        b.append('<h3 id="rejection-rule">Rejection Rule</h3>')
        b.append(md_paras(f["limit"]))

    stats = []
    if t == "W":
        if f.get("speed") and f.get("range"):
            stats = [("Damage", f.get("damage")), ("Speed", f.get("speed")), ("Range", f.get("range"))]
        elif f.get("speed_range"):
            stats = [("Damage", f.get("damage")), ("Speed / Range", f.get("speed_range"))]
        else:
            stats = [("Damage", f.get("damage"))]
        stats += [
            ("Pattern", f.get("pattern")),
            ("Coverage", f.get("coverage")), ("Falloff", f.get("falloff")),
            ("Maximum", f.get("max_raw")), ("Echo cost", f.get("echo_raw")),
        ]
    elif t == "S":
        stats = [
            ("Lament resistance", f.get("res_Lament")), ("Grudge resistance", f.get("res_Grudge")),
            ("Void resistance", f.get("res_Void")), ("Weight resistance", f.get("res_Weight")),
            ("Maximum", f.get("max_raw")), ("Echo cost", f.get("echo_raw")),
        ]
    else:
        stats = [("Maximum", f.get("max_raw")), ("Echo cost", f.get("echo_raw"))]
        if f.get("damage"):
            stats.insert(0, ("Effect", f.get("damage")))
    stats_html = table_rows(stats)
    if stats_html:
        b.append('<h2 id="operational-statistics">Operational Statistics</h2>')
        b.append(stats_html)

    rec_h2 = {"W": ("combat-record", "Combat Record"), "S": ("resistance-record", "Resistance Record"), "G": ("gift-record", "Gift Record")}[t]
    ab_h3 = {"W": ("signature-ability", "Signature Ability"), "S": ("protective-ability", "Protective Ability"), "G": ("gift-effect", "Gift Effect")}[t]
    cost_h3 = {"W": ("wielder-cost", "Wielder Cost"), "S": ("bearer-cost", "Bearer Cost"), "G": ("bearer-cost", "Bearer Cost")}[t]
    if ability_text or f.get("limit") or stats_html:
        hist = [f'<section class="item-history" style="--item:{color}"><h2 id="{rec_h2[0]}">{rec_h2[1]}</h2>']
        if stats_html:
            hist.append(stats_html)
        if ability_text:
            ab_title = f"{ab_h3[1]} — {f['ability_name']}" if f.get("ability_name") else ab_h3[1]
            hist.append(f'<h3 id="{ab_h3[0]}">{esc(ab_title)}</h3>')
            hist.append(md_paras(ability_text))
        if f.get("limit"):
            hist.append(f'<p><strong>Limit:</strong> {esc(f["limit"])}</p>')
        if price_text:
            hist.append(f'<h3 id="{cost_h3[0]}">{cost_h3[1]}</h3>')
            hist.append(md_paras(price_text))
        hist.append("</section>")
        b.append("".join(hist))
    elif price_text:
        b.append(f'<h3 id="{cost_h3[0]}">{cost_h3[1]}</h3>' + md_paras(price_text))

    for key, (hid, title) in {
        "corrosion": ("corrosion", "Corrosion"),
        "maintenance": ("maintenance", "Maintenance"),
        "shutdown": ("shutdown", "Shutdown"),
    }.items():
        if f.get(key):
            b.append(f'<h3 id="{hid}">{title}</h3>')
            b.append(md_paras(f[key]))

    if f.get("incident"):
        b.append('<h2 id="history-of-use">History of Use</h2>')
        if f.get("incident_name"):
            b.append(f"<p><strong>Incident — {esc(f['incident_name'])}:</strong> {esc(f['incident'])}</p>")
        else:
            b.append(md_paras(f["incident"]))

    # Set resonance
    others = [item["siblings"][tt] for tt in ("W", "S", "G") if tt != t]
    other_names = [
        (tt, item["sibling_fields"][tt]["name"]) for tt in ("W", "S", "G") if tt != t
    ]
    b.append('<h2 id="set-resonance">Set Resonance</h2>')
    if other_names:
        n1, n2 = other_names
        b.append(
            f"<p>With {esc(n1[1])} and {esc(n2[1])}, {esc(f['name'])} completes the "
            f"{esc(donor_disp)} set. Resonance notes are recorded on the "
            f'<a href="maw-set-synergies.html">set synergies</a> page.</p>'
        )
    else:
        b.append(f"<p>The {esc(donor_disp)} set has no other published pieces yet.</p>")
    diagram = [f'<div class="set-diagram" style="--item:{color}">']
    for tt in ("W", "S", "G"):
        sib = item["siblings"][tt]
        sib_img = item["sibling_art"][tt]
        sib_name = item["sibling_fields"][tt]["name"]
        cls = "current" if tt == t else ""
        diagram.append(
            f'<a class="{cls}" href="{sib}"><img alt="" src="../assets/art/maw/{sib_img}?v={ASSET_VERSION}"/>'
            f"<span>{TYPE_LABEL[tt]}</span><b>{esc(sib_name)}</b></a>"
        )
    diagram.append("</div>")
    b.append("".join(diagram))

    b.append('<h2 id="source-relationship">Source Relationship</h2>')
    b.append(
        f"<p>The item remains linked to {donor_ref}. Its statistics do not transfer to another piece "
        "of the same grade, and its history cannot be used as the history of the linked Suit, Weapon, or Gift.</p>"
    )
    b.append("</article>")

    # Infobox
    ent_plain = f"{donor_disp} — {f['entity_name']}" if f.get("entity_name") else donor_disp
    ent_cell = (
        f"<dd><a href='{ent_page}'>{esc(ent_plain)}</a></dd>" if ent_page else f"<dd>{esc(ent_plain)}</dd>"
    )
    type_cell = f"{TYPE_LABEL[t]}{' — ' + esc(f['subtype']) if f.get('subtype') else ''}"
    dl = [
        ("Registry code", code),
        ("Type", type_cell),
        ("Grade", grade),
        ("Element", element),
        ("Maximum", f.get("max_raw")),
        ("Echo cost", f.get("echo_raw")),
        ("SECC", f.get("secc")),
        ("Classification", f.get("classification")),
        ("Filed", f.get("author")),
    ]
    dl_html = "".join(f"<dt>{esc(k)}</dt><dd>{esc(v)}</dd>" for k, v in dl if v)
    b.append(f'<aside class="item-infobox" style="--item:{color}"><img alt="" src="{img}"/><h2 id="registry-record">Registry Record</h2><dl class="fact-grid"><dt>Registry code</dt><dd>{esc(code)}</dd>{ent_cell}{dl_html}</dl></aside></div>')

    c.append("".join(b))

    # Prev / next
    left = (
        f'<a href="{item["prev"]}">← {esc(item["prev_name"])}</a>'
        if item.get("prev")
        else '<a href="index.html">← M.A.W. registry</a>'
    )
    right = (
        f'<a href="{item["next"]}">{esc(item["next_name"])} →</a>'
        if item.get("next")
        else '<a href="index.html">M.A.W. registry →</a>'
    )
    c.append(f'<nav class="article-nav">{left}{right}</nav>')

    # Triad box
    ent_art = f"../assets/art/entities/se-{item['donor_token']}.svg" if item["donor_token"] in _ENTITY_ART else "../assets/icons/ref_absolvohan.svg"
    ent_href = ent_page or "../entities/list.html"
    triad = ['<div class="maw-triad-box">', '  <div class="maw-triad-header">M.A.W. TRIAD SET SYNERGY &amp; SOURCE ENTITY</div>', '  <div class="maw-triad-grid">']
    triad.append(
        f'    <a href="{ent_href}" class="triad-card" style="border-color:{color};">\n'
        f'      <img src="{ent_art}" alt="Entity">\n'
        f'      <div class="triad-meta"><span class="triad-type">SOURCE ENTITY ({esc(donor_disp)})</span><span class="triad-name">{esc(f.get("entity_name") or "")}</span></div>\n'
        f"    </a>"
    )
    for tt in ("W", "S", "G"):
        if tt == t:
            continue
        sib = item["siblings"][tt]
        triad.append(
            f'    <a href="{sib}" class="triad-card">\n'
            f'      <img src="../assets/art/maw/{item["sibling_art"][tt]}?v={ASSET_VERSION}" alt="{TYPE_LABEL[tt]}">\n'
            f'      <div class="triad-meta"><span class="triad-type">SET {TYPE_LABEL[tt].upper()}</span><span class="triad-name">{esc(item["sibling_fields"][tt]["name"])}</span></div>\n'
            f"    </a>"
        )
    # self card as third slot when only entity+1 sibling shown (never; 2 siblings always exist)
    triad.append("  </div>")
    triad.append("</div>")
    c.append("\n".join(triad))

    c.append(CROSS_REF)
    return "\n".join(c)


CROSS_REF = """<!-- Bottom Cross-Reference Directory -->

    <!-- M.A.W. Set Synergy Triad -->
<section class="cross-reference-section">
  <div class="cross-ref-header">CANONICAL CROSS-LINKS &amp; ATLAS CONNECTIONS</div>
  <div class="cross-ref-grid">
    <a href="../departments/floor-1-neutral-command.html" class="cross-ref-card">
      <img src="../assets/layout/hand/icons/icon_dept_f1_neutral.svg" alt="Command">
      <div class="cross-ref-meta"><span class="cross-ref-cat">FACILITY COMMAND</span><span class="cross-ref-title">NEUTRAL COMMAND</span></div>
    </a> <a href="../characters/the-director-majin.html" class="cross-ref-card">
      <img src="../assets/icons/icon_core_majin.svg" alt="Majin">
      <div class="cross-ref-meta"><span class="cross-ref-cat">EXECUTIVE LEAD</span><span class="cross-ref-title">DIRECTOR MAJIN</span></div>
    </a> <a href="../lore/the-cycle-and-absolvohan.html" class="cross-ref-card">
      <img src="../assets/icons/ref_absolvohan.svg" alt="Absolvohan">
      <div class="cross-ref-meta"><span class="cross-ref-cat">PRIMARY CANON</span><span class="cross-ref-title">1,778 CYCLES</span></div>
    </a> <a href="../atlas/hand-of-change-map.html" class="cross-ref-card">
      <img src="../assets/layout/hand/icons/the_hand_dr_icon_styled.svg" alt="Facility Map">
      <div class="cross-ref-meta"><span class="cross-ref-cat">SCHEMATIC ATLAS</span><span class="cross-ref-title">HAND OF CHANGE MAP</span></div>
    </a>
  </div>
</section>"""

ASSET_VERSION = "20260902b"


def main() -> int:
    global ASSET_VERSION
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--version", default="20260902b")
    args = parser.parse_args()
    ASSET_VERSION = args.version

    find_entity_pages()
    _ENTITY_ART.clear()
    for p in (DOCS / "assets" / "art" / "entities").glob("se-*.svg"):
        _ENTITY_ART.add(p.stem.split("-")[1])

    template = TEMPLATE_PAGE.read_text(encoding="utf-8")
    pre_main = template[: template.index('<main id="content">')]
    post_main = template[template.index("</main>") + len("</main>") :]

    items: list[dict] = []
    if not REGISTRY.is_dir():
        print(f"FAIL: registry missing at {REGISTRY}")
        return 1
    for root, _, files in os.walk(REGISTRY):
        for fn in files:
            m = re.match(r"^(UNK_\d+|SE-\d+)-[A-D]__MAW-([WSG])_(.+)\.md$", fn)
            if not m:
                continue
            donor, t, name = m.group(1), m.group(2), m.group(3)
            text = Path(root, fn).read_text(encoding="utf-8", errors="replace")
            f = parse_record(text)
            code = f["code"] or f"MAW-{t}-{donor_display(donor)}-01"
            items.append(
                {
                    "donor": donor,
                    "type": t,
                    "name_raw": name,
                    "fields": f,
                    "code": code,
                    "path": Path(root, fn),
                }
            )
    items.sort(key=lambda i: (donor_id(i["donor"])[1], TYPE_RANK[i["type"]], i["code"]))

    # assign slugs / files (stable, collision-free; keeps previously published
    # filenames when the slug was extended in an earlier release)
    existing = {p.name for p in MAW_DIR.glob("*.html")}
    used: set[str] = set()
    for it in items:
        tok, _ = donor_id(it["donor"])
        base = f"maw-{it['type'].lower()}-{tok}-01-{slugify(it['fields']['name'] or it['name_raw'])}"
        slug = base
        if f"{base}.html" in used or (f"{base}.html" not in existing):
            cands = sorted(n for n in existing if n.startswith(base + "-"))
            if cands:
                slug = cands[0][: -len(".html")]
            else:
                n = 2
                while f"{slug}.html" in used or f"{slug}.html" in existing:
                    slug = f"{base}-{n}"
                    n += 1
        it["file"] = slug + ".html"
        it["art_name"] = f"maw-{it['type'].lower()}-{tok}-01.svg"
        it["donor_token"] = tok
        it["color"] = color_for(it["fields"]["element"])
        it["seed"] = int(hashlib.sha256(it["code"].encode()).hexdigest(), 16) % (2 ** 28)
        used.add(it["file"])

    # siblings + prev/next
    by_donor: dict[str, dict] = {}
    for it in items:
        by_donor.setdefault(it["donor"], {})[it["type"]] = it
    for i, it in enumerate(items):
        sib = by_donor[it["donor"]]
        it["siblings"] = {tt: s["file"] for tt, s in sib.items()}
        it["sibling_fields"] = {tt: s["fields"] for tt, s in sib.items()}
        it["sibling_art"] = {tt: s["art_name"] for tt, s in sib.items()}
        it["prev"] = items[i - 1]["file"] if i > 0 else None
        it["prev_name"] = items[i - 1]["fields"]["name"] if i > 0 else None
        it["next"] = items[i + 1]["file"] if i < len(items) - 1 else None
        it["next_name"] = items[i + 1]["fields"]["name"] if i < len(items) - 1 else None

    todo = [it for it in items if not (MAW_DIR / it["file"]).exists()]
    if args.limit:
        todo = todo[: args.limit]

    published = 0
    problems: list[str] = []
    for it in todo:
        f = it["fields"]
        if not f.get("name"):
            problems.append(f"{it['path'].name}: no name parsed")
            continue
        svg = make_svg(it["code"], f["name"], it["type"], it["color"], it["seed"])
        content = build_content(it)
        head_title = f'{f["name"]} — Somnarak Wiki'
        desc = f'{TYPE_LABEL[it["type"]]} of {donor_display(it["donor"])} — {it["code"]}'
        new_head = pre_main.replace(
            re.search(r"<title>.*?</title>", pre_main, re.S).group(0), f"<title>{html.escape(head_title)}</title>"
        )
        page = new_head + '<main id="content">\n' + content + "\n</main>" + post_main
        if not args.dry_run:
            (MAW_DIR / it["file"]).write_text(page, encoding="utf-8")
            (ART_DIR / it["art_name"]).write_text(svg, encoding="utf-8")
        published += 1

    print(f"registry items: {len(items)}; existing pages: {len(items) - len(todo)}; new this run: {published}")
    if problems:
        print("parse problems:")
        for p in problems[:20]:
            print("  " + p)
    return 0 if not problems else 2


_ENTITY_ART: set[str] = set()

if __name__ == "__main__":
    sys.exit(main())
