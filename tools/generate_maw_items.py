#!/usr/bin/env python3
"""Generate M.A.W. item pages from the Codex Set Registry.

Reads item records from
``REFERENCE_SOMNARAK_WIKI/LORE or REFERANCE/M.A.W. Codex_Set Registry``
(files named ``<DONOR>-<SLOT>__MAW-<W|S|G>_<Name>.md``) and publishes one
public page per item under ``docs/maw/``, with a per-item source-led SVG
composition under ``docs/assets/art/maw/``.

The parser is format-tolerant: appearance, canonical ability, and bearer or
wielder cost are recovered from section headings (``### Appearance``,
``### Protective Ability — X``, ``### Bearer Cost``), from ``| Field | Record |``
tables, and from inline ``**Field:**`` lines depending on how each registry
record is written.

The SVG renderer is content-driven rather than seed-random. Each composition
is selected from the object written into the item's name, ``Type`` descriptor,
and Appearance sentence, then finished with small motifs tied to function
keywords (grief, memory, silence, corrosion, judgment, listening, etc.). The
primitives are still varied deterministically per record so every composition
stays structurally unique.

The tool is idempotent by default. ``--force`` regenerates every published page
and SVG (used after a parser or renderer change).

Usage:
    python tools/generate_maw_items.py            # publish all missing items
    python tools/generate_maw_items.py --force    # rewrite every item page/SVG
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

ASSET_VERSION = "20260903m1"


# --------------------------------------------------------------------------
# Small text helpers
# --------------------------------------------------------------------------

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


def clean_inline(value: str) -> str:
    """Remove bold/italic/code markup and collapse whitespace."""
    value = re.sub(r"\*\*([^*]+)\*\*", r"\1", value)
    value = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"\1", value)
    value = re.sub(r"`([^`]*)`", r"\1", value)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def clean_para_text(value: str) -> str:
    """Clean a multi-line block: drop HR lines and heading markers.

    Keeps paragraph boundaries so ``md_paras`` can still produce <p> blocks.
    """
    if not value:
        return ""
    lines: list[str] = []
    for line in value.splitlines():
        raw = line.strip()
        if not raw:
            if lines and lines[-1] != "":
                lines.append("")
            continue
        if re.match(r"^[-*_]{3,}\s*$", raw):
            continue
        if re.match(r"^#{1,6}\s+.*$", raw):
            raw = re.sub(r"^#{1,6}\s*", "", raw)
        raw = clean_inline(raw)
        if raw:
            lines.append(raw)
    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines)


# --------------------------------------------------------------------------
# Parser
# --------------------------------------------------------------------------

def split_sections(text: str) -> list[tuple[int, str, str]]:
    """Split a registry record into heading sections.

    Returns ``(level, heading, body)`` where the body no longer includes the
    heading line and stops before the next heading of any level.
    """
    lines = text.splitlines()
    sections: list[tuple[int, str, list[str]]] = []
    current: tuple[int, str, list[str]] | None = None
    for line in lines:
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            if current is not None:
                sections.append(current)
            current = (len(m.group(1)), m.group(2).strip(), [])
        elif current is not None:
            current[2].append(line)
    if current is not None:
        sections.append(current)
    return [(level, heading, "\n".join(body)) for level, heading, body in sections]


def mdt_rows(text: str) -> list[tuple[str, str]]:
    """Return ``(left, right)`` pairs from two-column ``| Field | Record |`` rows."""
    rows: list[tuple[str, str]] = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|") or not line.endswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        # Only two-column Field / Record rows are treated as key-value pairs.
        # Multi-column stat blocks (Grade/Element | Damage | ...) are parsed
        # separately by the core-statistics matcher.
        if len(cells) != 2:
            continue
        left = clean_inline(cells[0])
        right = clean_inline(cells[1])
        if not left or re.match(r"^[:\s|-]+$", left):
            continue
        if right and right not in ("—", "–", "-", " "):
            rows.append((left, right))
    return rows


def resistance_rows(text: str) -> list[tuple[str, str, str, str]]:
    """Return Element/Multiplier/Label/Field Meaning rows from resistance tables."""
    lines = [ln.strip() for ln in text.splitlines() if ln.strip().startswith("|")]
    header_idx: set[int] = set()
    for i, line in enumerate(lines):
        if re.match(r"^\|\s*Element\s*\|\s*Multiplier\s*\|\s*Label\s*\|\s*Field Meaning\s*\|\s*$", line, re.I):
            header_idx.add(i)
    rows: list[tuple[str, str, str, str]] = []
    for i, line in enumerate(lines):
        if i in header_idx:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 4:
            continue
        elem, mult, label, meaning = cells[:4]
        elem = clean_inline(elem)
        if not elem or re.match(r"^[:\s|-]+$", elem):
            continue
        rows.append((elem, mult, label, meaning))
    return rows


def bold_fields(text: str) -> dict[str, str]:
    """Extract inline ``**Field:** value`` definitions.

    A line-wise scan is used so that several fields on one line
    (``**Source bonus:** x. **Cost:** y.``) do not swallow each other.
    A field whose value starts on the current line and continues onto a
    non-field continuation line still absorbs that continuation.
    """
    found: dict[str, str] = {}
    pending_key: str | None = None
    for line in text.splitlines():
        markers = list(re.finditer(r"\*\*([^\n*]{2,}?):\*\*", line))
        if markers:
            # Continuation lines that begin a new block should not append to
            # the previous field (headings, tables, separators, list items).
            if pending_key and not line.lstrip().startswith(("#", "|", "-", "*", "---", "```")):
                prev_value = found.get(pending_key, "")
                if prev_value and not prev_value.endswith((".", "!", "?", ":")):
                    found[pending_key] = prev_value + "\n" + clean_inline(line)
            pending_key = None
            for i, m in enumerate(markers):
                key = clean_inline(m.group(1))
                start = m.end()
                end = markers[i + 1].start() if i + 1 < len(markers) else len(line)
                raw_value = line[start:end].strip()
                value = clean_inline(raw_value)
                if key and value:
                    found[key.lower()] = value
                    pending_key = key.lower()
                elif key and key.lower() not in found:
                    found[key.lower()] = ""
                    pending_key = key.lower()
        elif pending_key and line.strip() and not line.lstrip().startswith(("#", "|", "-", "---", "```")) and not re.match(r"^\s*$", line):
            # Single-line field value continuing onto a prose line.
            prev_value = found.get(pending_key, "")
            if prev_value:
                found[pending_key] = prev_value + "\n" + clean_inline(line)
        elif pending_key and not line.strip():
            pending_key = None
    return {k: clean_para_text(v) for k, v in found.items() if v}


def first_row(row_pairs: list[tuple[str, str]], *names: str) -> str | None:
    """Return the first table row whose left field matches any name."""
    wanted = {n.lower() for n in names}
    for left, right in row_pairs:
        if left.lower() in wanted:
            return right
    return None


def first_bold(bold: dict[str, str], *names: str) -> str | None:
    for n in names:
        v = bold.get(n.lower())
        if v:
            return v
    return None


def section_body(
    sections: list[tuple[int, str, str]], *names: str, prefix: bool = False
) -> str | None:
    """Return a heading section body by exact or prefix heading match."""
    wanted = {n.lower() for n in names}
    for level, heading, body in sections:
        h = heading.strip().lower()
        for w in wanted:
            if h == w or (prefix and h.startswith(w)):
                return clean_para_text(body)
    return None


def heading_with_label(sections: list[tuple[int, str, str]], *labels: str) -> str | None:
    """Extract the label after an em dash in a titled ability heading.

    ``'### Protective Ability — Absence Margin'`` -> ``'Absence Margin'``.
    """
    wanted = tuple(l.lower() for l in labels)
    for _level, heading, _body in sections:
        h = heading.strip()
        lowered = h.lower()
        if any(lowered.startswith(w) for w in wanted) and "—" in h:
            label = h.split("—", 1)[1].strip()
            if label:
                return label
    return None


def parse_record(text: str) -> dict:
    f: dict = {}

    sections = split_sections(text)
    row_pairs = mdt_rows(text)
    bold = bold_fields(text)

    def first(pattern: str, group: int = 1, flags: int = re.M | re.I):
        m = re.search(pattern, text, flags)
        return m.group(group).strip() if m else None

    f["name"] = first(r"^# M\.A\.W\. \w+ — (.+)$")
    f["flavor"] = first(r"^>\s*\*?[“\"](.+?)[”\"]\*?\s*$", flags=re.S | re.I)
    f["doc_id"] = first(r"\*\*Document ID:\*\* *`([^`]+)`")
    ent = re.search(r"\*\*Linked Entity:\*\* *`?(SE-\d+|UNK-\d+)`? — ([^\n]+)", text)
    f["entity"] = ent.group(1) if ent else None
    f["entity_name"] = ent.group(2).strip() if ent else None
    f["code"] = first(r"\*\*Item Registry Code:\*\* *`([^`]+)`")
    f["author"] = first(r"\*\*Author:\*\* *([^\n]+)")
    f["date"] = first(r"\*\*Date:\*\* *([^\n]+)")
    f["classification"] = first(r"\*\*Classification:\*\* *([^\n]+)")
    f["set_completion"] = first(r"\*\*Codex Set Completion:\*\* *`([^`]+)`")
    f["secc"] = first(r"\*\*Source SECC Designation:\*\* *`([^`]+)`")

    f["type_raw"] = first_row(row_pairs, "Type") or first_bold(bold, "Type")
    f["grade_raw"] = first_row(row_pairs, "Grade") or first_bold(bold, "Grade")
    f["element_raw"] = (
        first_row(row_pairs, "Element")
        or first_bold(bold, "Grade / Element", "Element", "Grade & Element")
    )

    # Appearance: table row, section heading, or inline bold (in that order).
    f["appearance"] = first_row(row_pairs, "Appearance")
    if not f["appearance"]:
        f["appearance"] = section_body(sections, "Appearance", "BESTOWAL & APPEARANCE", "APPEARANCE", prefix=True)
    if not f["appearance"]:
        f["appearance"] = first_bold(bold, "Appearance")

    f["damage"] = first_row(row_pairs, "Damage") or first_bold(bold, "Damage")
    f["speed_range"] = first_row(row_pairs, "Speed / Range") or first_bold(bold, "Speed / Range")
    f["speed"] = first_row(row_pairs, "Speed") or first_bold(bold, "Speed")
    f["range"] = first_row(row_pairs, "Range") or first_bold(bold, "Range")
    f["pattern"] = (
        first_row(row_pairs, "Attack Pattern", "Pattern")
        or first_bold(bold, "Attack Pattern", "Pattern")
    )
    f["coverage"] = (
        first_row(row_pairs, "Target Coverage", "Coverage")
        or first_bold(bold, "Target Coverage", "Coverage")
    )
    f["falloff"] = (
        first_row(row_pairs, "Falloff Rule", "Falloff")
        or first_bold(bold, "Falloff Rule", "Falloff")
    )
    f["max_raw"] = (
        first_row(row_pairs, "Max Amount", "Maximum Amount", "Maximum")
        or first_bold(bold, "Max Amount", "Maximum Amount", "Maximum")
    )
    f["echo_raw"] = (
        first_row(row_pairs, "Echo cost", "Echo Cost", "Sorrow Echoes")
        or first_bold(bold, "Echo cost", "Echo Cost", "Sorrow Echoes")
    )

    for el in ("Lament", "Grudge", "Void", "Weight"):
        row = first_row(row_pairs, f"{el} resistance", f"{el} Resistance", el)
        if row:
            f[f"res_{el}"] = row
    res_tables = resistance_rows(text)
    for elem, mult, label, meaning in res_tables:
        f[f"res_{elem}"] = f"{mult} — {label} — {meaning}"

    # Compact resistance row: ``| Lament | Grudge | Void | Weight | Maximum / Cost |``
    compact_res = re.search(
        r"^\|\s*Lament\s*\|\s*Grudge\s*\|\s*Void\s*\|\s*Weight\s*\|\s*Maximum\s*/\s*Cost\s*\|\s*$\n"
        r"^\|[\s:\-|]+$.*\n"
        r"^\|\s*([^|\n]+)\|\s*([^|\n]+)\|\s*([^|\n]+)\|\s*([^|\n]+)\|\s*([^|\n]+)\|\s*$",
        text,
        re.M,
    )
    if compact_res:
        vals = [c.strip() for c in compact_res.groups()]
        for el, value in zip(("Lament", "Grudge", "Void", "Weight"), vals[:4]):
            f[f"res_{el}"] = value
        mc = [x.strip() for x in vals[4].split("/")] if "/" in vals[4] else [vals[4]]
        if len(mc) == 2:
            if not f.get("max_raw"):
                f["max_raw"] = mc[0]
            if not f.get("echo_raw"):
                f["echo_raw"] = mc[1]
        elif mc:
            if not f.get("max_raw"):
                f["max_raw"] = mc[0]

    # Ability
    ability_name = heading_with_label(sections, "Protective Ability", "Signature Ability", "Gift Effect", "Ability")
    f["ability_name"] = ability_name
    f["canonical_ability"] = (
        first_row(row_pairs, "Canonical ability", "Canonical Ability")
        or first_bold(bold, "Canonical ability", "Canonical Ability")
    )
    effect_parts = []
    for label in ("Unentered Name", "Distinct Listener", "Source bonus", "Passive", "Active", "Effect", "Ability", "Standard", "Signature", "Hidden Name", "Inherited"):
        value = first_bold(bold, label)
        if value:
            effect_parts.append(f"{label}: {value}")
    if effect_parts:
        ability_body = "\n\n".join(effect_parts)
    else:
        ability_body = (
            section_body(sections, "EFFECT & HIDDEN CONDITION", "EFFECT FILE", "GIFT STATISTICS", "ABILITY FILE", "SOURCE ABILITY", "COMBAT FILE", "PROTECTION FILE", "WEAPON FILE", prefix=True)
            or section_body(sections, "Protective Ability", "Signature Ability", "Gift Effect", "Ability", prefix=True)
            or section_body(sections, "PROTECTIVE ABILITY", "GIFT EFFECT", "SIGNATURE ABILITY", prefix=True)
        )
    if ability_body:
        # Keep cost/limit fields out of ability copy; they render separately.
        ability_body = re.sub(r"(?m)^\s*Cost:\s*.*$", "", ability_body)
        ability_body = re.sub(r"(?m)^\s*Bearer cost:\s*.*$", "", ability_body)
        ability_body = re.sub(r"(?m)^\s*Limit:\s*.*$", "", ability_body)
        ability_body = re.sub(r"(?m)^\s*Rejection(?: rule)?:\s*.*$", "", ability_body)
        ability_body = ability_body.strip()
    if not ability_body:
        ability_body = f["canonical_ability"]
    f["ability_body"] = ability_body

    # Cost: section takes precedence over inline field.
    cost = (
        section_body(sections, "Bearer Cost", "Wearer Cost", "Wielder Cost", "Cost", prefix=True)
        or first_bold(bold, "Bearer cost", "Bearer Cost", "Wearer cost", "Weilder cost", "Wielder cost", "Operational / binding cost", "Operational / Binding Cost", "Operational cost", "Binding cost", "Cost")
        or first_row(row_pairs, "Bearer cost", "Bearer Cost", "Wearer cost", "Wielder cost", "Operational cost", "Binding cost", "Cost")
    )
    if not cost and f.get("echo_raw"):
        # Cost panel falls back to the resource cost when the record has no
        # prose "bearer cost" field but does list an Echo cost.
        cost = f["echo_raw"]
    f["bearer_cost"] = cost

    f["limit"] = (
        first_bold(bold, "Limit", "Binding rule", "Binding requirement", "Rejection rule", "Rejection", "Failure mode")
        or section_body(sections, "Binding Rule", "Rejection Rule", "Limit", "Failure Mode", prefix=True)
    )
    f["corrosion"] = (
        first_bold(bold, "Corrosion", "Corrosion & Care", "Failures", "Failure")
        or section_body(sections, "Corrosion", "Corrosion & Care", "Failures", "Failure", prefix=True)
    )
    f["maintenance"] = first_bold(bold, "Maintenance") or section_body(sections, "Maintenance", prefix=True)
    f["shutdown"] = (
        first_bold(bold, "Emergency shutdown", "Shutdown", "Emergency Shutdown")
        or section_body(sections, "Emergency Shutdown", "Shutdown", prefix=True)
    )

    # Item-specific history
    h = section_body(sections, "ITEM-SPECIFIC HISTORY", "HISTORY OF USE", prefix=True)
    inc = re.search(r"\*\*Incident — ([^:]+):\*\* *([^\n]+)", text)
    if inc:
        f["incident_name"] = inc.group(1).strip()
        f["incident"] = inc.group(2).strip()
    elif h:
        f["incident"] = h
        f.setdefault("incident_name", None)
    else:
        # Some records place the history under a ### subsection (e.g.
        # ``### Gift Record — Returned Without a Name``). Capture the whole
        # ``## HISTORY OF USE`` block, subheading included.
        hblock = re.search(
            r"(?m)^##\s*(ITEM-SPECIFIC HISTORY|HISTORY OF USE)\b[^\n]*\n(.*?)(?=\n## |\n\*\*Document ID:|\n---)",
            text,
            re.S,
        )
        if hblock:
            f["incident"] = clean_para_text(hblock.group(2))
            f.setdefault("incident_name", None)

    # Compact intro summary: ``A Tail ember granted...: **α Grudge; 5%; +1
    # Resilience.** It converts one suppressed emotion into brief strength;
    # cost: the bearer cannot hide grief.``
    intro = re.search(
        r"\*\*([αβγδεω]) ([A-Za-z]+); ([^;]+); ([^.)]+)(?:\.)?\*\*\s*([^\n]+)",
        text,
    )
    if intro:
        if not f.get("grade_raw"):
            f["grade_raw"] = intro.group(1)
        if not f.get("element_raw"):
            f["element_raw"] = intro.group(2)
        if not f.get("max_raw"):
            f["max_raw"] = clean_inline(intro.group(4))
        body = intro.group(5).strip()
        cost_m = re.search(r"(?:;\s*cost:|\scost:|\bCost:)\s*(.+)$", body, re.I)
        if cost_m:
            if not f.get("bearer_cost"):
                f["bearer_cost"] = clean_inline(cost_m.group(1))
            body = body[: cost_m.start()].strip()
        if not f.get("ability_body") and body:
            f["ability_body"] = clean_inline(body)
        if not f.get("bonus"):
            f["bonus"] = clean_inline(intro.group(3))

    # Record-level inline summary for the compact CORE STATISTICS block
    inline = re.search(
        r"\*\*([αβγδεω]) ([A-Za-z]+); (L/G/V/W) ([\d./]+); max (\d+); (\d+) Echoes\.\*\* *(.+)",
        text,
    )
    if inline:
        if not f.get("grade_raw"):
            f["grade_raw"] = inline.group(1)
        if not f.get("element_raw"):
            f["element_raw"] = inline.group(2)
        if not f.get("max_raw"):
            f["max_raw"] = inline.group(5)
        if not f.get("echo_raw"):
            f["echo_raw"] = inline.group(6) + " Sorrow Echoes"
        if not f.get("ability_body"):
            f["ability_body"] = inline.group(7).strip()

    # Format C: bold "Grade / Element:" field + CORE STATISTICS value row
    ge = re.search(r"\*\*Grade\s*/?\s*Element:\*\* *([αβγδεω])\s*/?\s*([A-Za-z]+)", text)
    if ge:
        if not f.get("grade_raw"):
            f["grade_raw"] = ge.group(1)
        if not f.get("element_raw"):
            f["element_raw"] = ge.group(2)

    # Style used by canonical source stat blocks:
    #   | Grade / Element | Damage | Speed / Range | Pattern | Maximum / Cost |
    core = re.search(
        r"^\|\s*Grade\s*/\s*Element\s*\|\s*Damage\s*\|\s*Speed\s*(?:/\s*Range)?\s*\|\s*Pattern\s*\|\s*Maximum\s*/\s*Cost\s*\|\s*$\n"
        r"^\|[\s:\-|]+$.*\n"
        r"^\|\s*([^|\n]+)\|([^|\n]+)\|([^|\n]+)\|([^|\n]+)\|([^|\n]+)\|\s*$",
        text,
        re.M,
    )
    if core:
        ge_cell, dmg_cell, spd_cell, pat_cell, cost_cell = (c.strip() for c in core.groups())
        if not f.get("grade_raw"):
            f["grade_raw"] = ge_cell
        if not f.get("element_raw"):
            f["element_raw"] = ge_cell
        if not f.get("damage"):
            f["damage"] = dmg_cell
        if "/" in spd_cell and not f.get("speed_range"):
            f["speed_range"] = spd_cell
        elif not f.get("speed"):
            f["speed"] = spd_cell
        if not f.get("pattern"):
            f["pattern"] = pat_cell
        mc = [x.strip() for x in cost_cell.split("/")] if "/" in cost_cell else [cost_cell]
        if len(mc) == 2:
            if not f.get("max_raw"):
                f["max_raw"] = mc[0]
            if not f.get("echo_raw"):
                f["echo_raw"] = mc[1]
        elif mc:
            if not f.get("max_raw"):
                f["max_raw"] = mc[0]

    cs = re.search(
        r"\|\s*Damage\s*\|\s*Speed\s*\|[^|\n]*\|\s*Pattern\s*/?\s*Falloff\s*\|\s*Maximum\s*/?\s*Echo Cost\s*\|\n"
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

    # grade/element cleanup
    g = f.get("grade_raw") or ""
    f["grade"] = g[0] if g and g[0] in "αβγδεω" else None
    e = f.get("element_raw") or ""
    elem_part = e
    if "/" in e:
        first, rest = e.split("/", 1)
        first = first.strip()
        if first in "αβγδεω":
            if f.get("grade") is None:
                f["grade"] = first
            # Element position is always the token after the grade slash.
            elem_part = rest.strip()
    f["element"] = elem_part.split(" — ")[0].strip() if elem_part else None
    f["element_sub"] = elem_part.split(" — ")[1].strip() if elem_part and " — " in elem_part else None
    t = f.get("type_raw") or ""
    f["subtype"] = t.split(" — ")[1].strip() if " — " in t else None

    if not f["element"]:
        dm0 = re.match(r"^(Lament|Grudge|Void|Weight|Mixed)\b", f.get("damage") or "")
        if dm0:
            f["element"] = dm0.group(1)

    # Element fallback: the subtype descriptor, appearance, or the resistance
    # table often name the element when the canonical block does not carry a
    # dedicated Element row.
    if not f["element"]:
        for source in (f.get("subtype"), f.get("appearance"), f.get("type_raw"), f.get("name")):
            for el in ("Lament", "Grudge", "Void", "Weight"):
                if re.search(rf"\b{el}\b", source or "", re.I):
                    f["element"] = el
                    break
            if f["element"]:
                break
    if not f["element"]:
        res_names = [f.get(f"res_{el}") for el in ("Lament", "Grudge", "Void", "Weight")]
        for idx, value in enumerate(res_names):
            if value and re.search(r"\b(?:Resistant|Resistance)\b", value, re.I):
                f["element"] = ("Lament", "Grudge", "Void", "Weight")[idx]
                break
    if not f["element"]:
        # Resolve from the resistance row with the smallest (best) multiplier.
        best_col: str | None = None
        best_num: float | None = None
        for el in ("Lament", "Grudge", "Void", "Weight"):
            value = first_row(row_pairs, f"{el} resistance", f"{el} Resistance") or first_bold(bold, f"{el} resistance", f"{el} Resistance")
            if value:
                m = re.search(r"(\d+(?:\.\d+)?)", value)
                num = float(m.group(1)) if m else None
                if num is not None and (best_num is None or num < best_num):
                    best_num = num
                    best_col = el
        if best_col:
            f["element"] = best_col

    return f


def color_for(element: str | None) -> str:
    return ELEMENT_COLOR.get(element or "", "#3e8bd5")


# --------------------------------------------------------------------------
# Content-driven SVG renderer
# --------------------------------------------------------------------------

OBJECT_SPELLING = {
    "blade": "BLADE",
    "fang": "FANG",
    "lens": "LENS",
    "maul": "MAUL",
    "hammer": "HAMMER",
    "spear": "SPEAR",
    "shaft": "STAFF",
    "rod": "STAFF",
    "baton": "BATON",
    "shard": "SHARD",
    "coil": "COIL",
    "axe": "AXE",
    "veil": "VEIL",
    "shroud": "SHROUD",
    "plate": "PLATE",
    "mantle": "MANTLE",
    "shield": "SHIELD",
    "armor": "ARMOR",
    "harness": "HARNESS",
    "gauntlet": "GAUNTLET",
    "charm": "CHARM",
    "token": "TOKEN",
    "lantern": "LANTERN",
    "stone": "STONE",
    "bell": "BELL",
    "ring": "RING",
    "pendant": "PENDANT",
    "mask": "MASK",
    "vial": "VIAL",
    "compass": "COMPASS",
    "crown": "CROWN",
    "thread": "THREAD",
    "tether": "THREAD",
    "ember": "EMBER",
    "seed": "SEED",
    "key": "KEY",
    "eye": "EYE",
    "tear": "TEAR",
    "fragment": "FRAGMENT",
    "bracelet": "BRACELET",
    "link": "LINK",
    "clasp": "CLASP",
    "heart": "HEART",
}


def detectable_text(it: dict) -> str:
    f = it["fields"]
    return " ".join(
        [
            f.get("name") or "",
            f.get("subtype") or "",
            f.get("appearance") or "",
            f.get("ability_body") or "",
            f.get("canonical_ability") or "",
            f.get("bearer_cost") or "",
        ]
    ).lower()


def appearance_detail_label(it: dict, base_label: str) -> str:
    """Pull the concrete object phrase from the Appearance sentence.

    ``'A thin blue charm shaped like the edge of a broken bell clapper.'``
    contributes ``'BROKEN BELL CLAPPER'``, so the art comment is more faithful
    to the record than the generic category noun alone.
    """
    f = it["fields"]
    appearance = f.get("appearance") or ""
    text = appearance.lower()
    phrase: str | None = None
    m = re.search(r"shaped like (?:the )?(?:edge of )?(?:a |an )?(.+?)(?:\.|,|;| and | that | which | it |$)", text)
    if not m:
        m = re.search(r"(?:like|as) (?:a |an )?(.+?)(?:\.|,|;| and | that | which | it |$)", text)
    if m:
        phrase = m.group(1).strip()
    if phrase:
        phrase = re.sub(r"\b(the|a|an|of|with|in|on)\b", "", phrase)
        phrase = re.sub(r"[^A-Za-z0-9' -]", "", phrase).strip()
        phrase = re.sub(r"\s+", " ", phrase)
        words = phrase.split()
        if 1 <= len(words) <= 4 and re.search(r"[A-Za-z]", phrase):
            return " ".join(w.upper() for w in words)
    # Fallback: prepend a concrete material/shape adjective from the Appearance
    # sentence to the generic category noun (e.g. "crystal blade").
    adjective = None
    for a, b in (
        (r"\bcrystal\b", "CRYSTAL"),
        (r"\bglass\b", "GLASS"),
        (r"\bice\b|ic[ey]", "ICE"),
        (r"\bchain\b|link\b", "CHAINED"),
        (r"\bthread\b|cord\b", "THREADED"),
        (r"\bpale blue\b", "PALE BLUE"),
        (r"\bdeep blue\b", "DEEP BLUE"),
        (r"\bblack\b", "BLACK"),
        (r"\bwraps\b|wrought\b", "WROUGHT"),
        (r"\bcarved\b", "CARVED"),
    ):
        if re.search(a, text):
            adjective = b
            break
    if adjective:
        return f"{adjective} {base_label}"
    subtype = f.get("subtype") or ""
    if subtype:
        subtype = re.sub(r" — .*", "", subtype).strip()
        if subtype:
            return " ".join(w.upper() for w in subtype.split()[:3])
    return base_label


def appearance_detail_shapes(it: dict, color: str, r) -> list[str]:
    """Add small detail marks selected from the Appearance/function writing.

    These are intentionally secondary to the object silhouette but are driven
    by the record: a crystal gets facet seams, a broken object gets a crack,
    draping fabric gets folds, weeping gets falling ripples, fire gets flames,
    a chain gets links.
    """
    text = detectable_text(it)
    cx, cy = 200.0, 192.0
    marks: list[str] = []
    n = 0

    def add(mark: str, x: float, y: float, scale: float) -> None:
        nonlocal n
        marks.append(
            f'  <g transform="rotate({r(30 + n * 2, -16, 16)} {x:.1f} {y:.1f})">'
            f"    {mark}\n  </g>"
        )
        n += 1

    if re.search(r"\bcrystal\b|\bglass\b|\bice\b|\bgem\b|\bfacet", text):
        for i in range(3):
            off = (i - 1) * 16
            add(
                f'<path d="M{cx + off:.1f} {cy - 104:.1f} L{cx + off + 14:.1f} {cy + 92:.1f}" fill="none" stroke="#e0f2fe" stroke-width="1" opacity=".38"/>',
                214.0,
                128.0,
                0.8,
            )
    if re.search(r"\bbreak\b|\bcrack\b|\bfractur\b|\bchip\b", text):
        add(
            f'<path d="M{cx - 30:.1f} {cy + 56:.1f} L{cx - 6:.1f} {cy + 26:.1f} L{cx - 18:.1f} {cy:.1f}" fill="none" stroke="#e0f2fe" stroke-width="1.6" opacity=".55"/>',
            158.0,
            236.0,
            0.8,
        )
    if re.search(r"\bveil\b|\bshroud\b|\bcloth\b|\bfabric\b|\bmantle\b", text):
        for i in range(3):
            y = cy + 16 + i * 30
            add(
                f'<path d="M{cx - 64:.1f} {y:.1f} Q{cx:.1f} {y + 18:.1f} {cx + 64:.1f} {y - 6:.1f}" fill="none" stroke="{color}" stroke-width="1.2" opacity=".4"/>',
                200.0,
                236.0,
                0.8,
            )
    if re.search(r"\bweep\b|\btear\b|\bdroplet\b|\brain\b|\bstill cold\b|\bcold\b", text):
        for i in range(3):
            x = cx - 24 + i * 24
            y = cy + 34 + i * 12
            add(
                f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{4 + i:.1f}" fill="#e0f2fe" opacity=".3"/>',
                172.0,
                252.0,
                0.8,
            )
    if re.search(r"\bflame\b|\bburn\b|\bember\b|\bglow\b|\bfire\b|\bwarm\b", text):
        add(
            f'<path d="M{cx:.1f} {cy + 86:.1f} C{cx - 10:.1f} {cy + 52:.1f}, {cx + 12:.1f} {cy + 38:.1f}, {cx + 2:.1f} {cy - 6:.1f}" fill="none" stroke="{color}" stroke-width="2" opacity=".55"/>',
            236.0,
            250.0,
            0.8,
        )
    if re.search(r"\bchain\b|\blink\b|\bcord\b|\btether\b|\bbound\b", text):
        for i in range(3):
            x = cx + (i - 1) * 12
            add(
                f'<circle cx="{x + 4:.1f}" cy="{cy + 72:.1f}" r="5" fill="none" stroke="{color}" stroke-width="1.6" opacity=".45"/>',
                200.0,
                278.0,
                0.8,
            )
    if re.search(r"\blens\b|\bglass\b|\bmirror\b|\breflect\b", text):
        add(
            f'<ellipse cx="{cx + 54:.1f}" cy="{cy - 42:.1f}" rx="7" ry="12" fill="none" stroke="#e0f2fe" stroke-width="1.1" opacity=".4"/>',
            258.0,
            136.0,
            0.8,
        )
    return marks


def detect_object(it: dict) -> tuple[str, str]:
    """Return (object_key, label) from the record's own writing."""
    f = it["fields"]
    text = detectable_text(it)
    itype = it["type"]

    # We prioritize the concrete noun written in the title and Type descriptor.
    pools: dict[str, list[str]] = {
        "weapon": [
            "fang", "maul", "hammer", "halberd", "lens", "spear", "lance",
            "javelin", "axe", "cleaver", "dagger", "blade", "edge", "sword",
            "shard", "rod", "staff", "baton", "coil", "whip", "chain", "saw",
        ],
        "suit": [
            "shroud", "veil", "plate", "mantle", "cloak", "shield", "vest",
            "harness", "armor", "gauntlet", "barrier", "brace", "burden", "corselet",
        ],
        "gift": [
            "lantern", "charm", "token", "stone", "bell", "ring", "pendant",
            "amulet", "mask", "vial", "flask", "compass", "crown", "thread",
            "cord", "tether", "shard", "fragment", "ember", "spark", "seed",
            "key", "eye", "tear", "droplet", "bracelet", "link", "clasp",
            "heart", "veil", "fang", "blade", "lens", "reflection", "scale",
        ],
    }

    def has(keys: list[str]) -> str | None:
        for key in keys:
            if re.search(rf"\b{re.escape(key)}\b", text):
                return key
        return None

    type_key = {"W": "weapon", "S": "suit", "G": "gift"}[itype]
    primary = has(pools[type_key])
    if not primary:
        # Weapons and suits can be written with synonyms drawn from the other
        # pool (e.g. a lens-edged disc is still a weapon); gifts are a broad
        # accessory category, so fall back to the item type.
        for pool_name in ("weapon", "suit", "gift"):
            if pool_name == type_key:
                continue
            primary = has(pools[pool_name])
            if primary:
                break
    if not primary:
        primary = has(pools[type_key]) or {
            "W": "blade",
            "S": "plate",
            "G": "charm",
        }[itype]

    # Normalize synonyms to a small set of drawing archetypes.
    normalized = {
        "edge": "blade",
        "sword": "blade",
        "dagger": "blade",
        "saw": "blade",
        "cleaver": "axe",
        "halberd": "spear",
        "lance": "spear",
        "javelin": "spear",
        "whip": "coil",
        "chain": "coil",
        "staff": "rod",
        "baton": "rod",
        "rod": "rod",
        "armor": "plate",
        "corselet": "plate",
        "barrier": "shield",
        "brace": "shield",
        "cloak": "mantle",
        "vest": "harness",
        "amulet": "pendant",
        "flask": "vial",
        "spark": "ember",
        "droplet": "tear",
        "cord": "thread",
        "tether": "thread",
        "fragment": "shard",
        "reflection": "lens",
        "scale": "pendant",
        "heart": "charm",
    }
    obj = normalized.get(primary, primary)
    if obj not in OBJECT_SPELLING:
        obj = {"W": "blade", "S": "plate", "G": "charm"}[itype]
    label = OBJECT_SPELLING[obj]
    if obj == "blade" and "curved" in text:
        label = "CURVED BLADE"
    if obj == "lens" and "pale" in text:
        label = "PALE LENS"
    if obj == "shroud" and "tear" in text:
        label = "TEAR SHROUD"
    return obj, label


def _path(*points: tuple[float, float]) -> str:
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in points)


# Each object draws into the 400x400 canvas around (200,196). We keep the
# object recognizable while varying proportions and finish from the record.
def _draw_blade(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    length = r(2, 132, 168)
    width = r(3, 12, 20)
    top = (cx, cy - length)
    out = [f'<path d="M{cx - width} {cy} L{cx - width * 0.42} {cy - length * 0.72} '
           f'L{top[0]:.1f} {top[1]:.1f} L{cx + width * 0.42} {cy - length * 0.66} '
           f'L{cx + width} {cy} Z" fill="{color}" fill-opacity=".24" stroke="{color}" stroke-width="3"/>']
    out.append(f'<path d="M{cx} {cy} L{top[0]:.1f} {top[1]:.1f}" fill="none" stroke="{accent}" stroke-width="1.5" opacity=".8"/>')
    out.append(f'<rect x="{cx - width * 0.5:.1f}" y="{cy - length * 0.58:.1f}" width="{width:.1f}" height="{length * 0.42:.1f}" fill="none" stroke="{color}" stroke-width="1" opacity=".45"/>')
    out.append(f'<rect x="{cx - width - 10:.1f}" y="{cy - 5:.1f}" width="{2 * width + 20:.1f}" height="10" rx="4" fill="{color}" fill-opacity=".45"/>')
    out.append(f'<rect x="{cx - 7:.1f}" y="{cy + 4:.1f}" width="14" height="{r(4, 34, 52):.1f}" rx="5" fill="#1f2937" stroke="{color}" stroke-width="2"/>')
    out.append(f'<circle cx="{cx:.1f}" cy="{cy + 16 + r(4, 34, 52):.1f}" r="{r(5, 5, 8):.1f}" fill="{color}" fill-opacity=".7"/>')
    return out


def _draw_fang(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    curve = r(2, 18, 34)
    length = r(3, 122, 158)
    top = (cx + curve, cy - length)
    out = [f'<path d="M{cx - 14} {cy} C{cx - 20} {cy - length * 0.55}, {top[0]:.1f} {top[1]:.1f} '
           f'{top[0] + 6:.1f} {top[1]:.1f} C{top[0] - 4:.1f} {cy - length * 0.52}, '
           f'{cx + 20} {cy - length * 0.34}, {cx + 15} {cy} Z" fill="{color}" fill-opacity=".26" stroke="{color}" stroke-width="3"/>']
    out.append(f'<path d="M{cx - 4} {cy - 8} C{cx + 8} {cy - length * 0.46}, {top[0] - 2:.1f} {top[1] + 8:.1f} '
               f'{top[0] + 3:.1f} {top[1] + 6:.1f}" fill="none" stroke="{accent}" stroke-width="1.5" opacity=".72"/>')
    out.append(f'<rect x="{cx - 18:.1f}" y="{cy - 8:.1f}" width="36" height="9" rx="4" fill="{color}" fill-opacity=".42"/>')
    out.append(f'<rect x="{cx - 7:.1f}" y="{cy:.1f}" width="14" height="{r(4, 42, 60):.1f}" rx="5" fill="#1f2937" stroke="{color}" stroke-width="2"/>')
    out.append(f'<circle cx="{cx:.1f}" cy="{cy + 12 + r(4, 42, 60):.1f}" r="5" fill="{color}" fill-opacity=".65"/>')
    return out


def _draw_lens(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    rx = r(2, 48, 66)
    ry = r(3, 60, 82)
    out = [
        f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="none" stroke="{color}" stroke-width="4"/>',
        f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx - 9:.1f}" ry="{ry - 12:.1f}" fill="{color}" fill-opacity=".18"/>',
        f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx - 18:.1f}" ry="{ry - 22:.1f}" fill="none" stroke="{accent}" stroke-width="1.2" opacity=".75"/>',
    ]
    for k in range(r(4, 3, 5)):
        ang = -50 + k * 26
        import math
        a = math.radians(ang)
        x1 = cx + math.cos(a) * rx
        y1 = cy + math.sin(a) * ry
        x2 = cx + math.cos(a) * (rx - 9)
        y2 = cy + math.sin(a) * (ry - 12)
        out.append(f'<path d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}" stroke="{accent}" stroke-width="1" opacity=".5"/>')
    out.append(f'<rect x="{cx - rx - 12:.1f}" y="{cy - 6:.1f}" width="{2 * rx + 24:.1f}" height="12" rx="5" fill="{color}" fill-opacity=".4"/>')
    out.append(f'<rect x="{cx - 6:.1f}" y="{cy + ry:.1f}" width="12" height="{r(4, 26, 40):.1f}" rx="4" fill="#1f2937" stroke="{color}" stroke-width="2"/>')
    return out


def _draw_maul(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    head_w = r(2, 38, 58)
    head_h = r(3, 26, 40)
    length = r(4, 96, 118)
    out = [f'<rect x="{cx - head_w:.1f}" y="{cy - head_h:.1f}" width="{2 * head_w:.1f}" height="{2 * head_h:.1f}" rx="7" fill="{color}" fill-opacity=".24" stroke="{color}" stroke-width="3.5"/>']
    out.append(f'<path d="M{cx - head_w * 0.6:.1f} {cy - head_h * 0.7:.1f} L{cx + head_w * 0.6:.1f} {cy - head_h * 0.7:.1f}" stroke="{accent}" stroke-width="1.3" opacity=".7"/>')
    out.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r(5, 8, 12):.1f}" fill="none" stroke="{accent}" stroke-width="1.2" opacity=".7"/>')
    out.append(f'<rect x="{cx - 6:.1f}" y="{cy + head_h:.1f}" width="12" height="{length:.1f}" rx="4" fill="#1f2937" stroke="{color}" stroke-width="2"/>')
    out.append(f'<circle cx="{cx:.1f}" cy="{cy + head_h + length + 10:.1f}" r="7" fill="{color}" fill-opacity=".55"/>')
    return out


def _draw_hammer(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    width = r(2, 44, 62)
    head_h = r(3, 18, 26)
    length = r(4, 78, 100)
    out = [f'<rect x="{cx - width:.1f}" y="{cy - head_h:.1f}" width="{2 * width:.1f}" height="{2 * head_h:.1f}" rx="6" fill="{color}" fill-opacity=".22" stroke="{color}" stroke-width="3"/>']
    out.append(f'<path d="M{cx - width + 7:.1f} {cy - head_h + 6:.1f} L{cx + width - 9:.1f} {cy + head_h - 6:.1f}" stroke="{accent}" stroke-width="1.1" opacity=".6"/>')
    out.append(f'<rect x="{cx - 5:.1f}" y="{cy + head_h:.1f}" width="10" height="{length:.1f}" rx="4" fill="#1f2937" stroke="{color}" stroke-width="2"/>')
    out.append(f'<circle cx="{cx:.1f}" cy="{cy + head_h + length + 8:.1f}" r="6" fill="{color}" fill-opacity=".55"/>')
    return out


def _draw_spear(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    length = r(2, 120, 150)
    tip_w = r(3, 10, 16)
    out = [f'<path d="M{cx - tip_w:.1f} {cy + 18:.1f} L{cx} {cy - length} L{cx + tip_w:.1f} {cy + 18:.1f} Z" fill="{color}" fill-opacity=".28" stroke="{color}" stroke-width="3"/>']
    out.append(f'<path d="M{cx:.1f} {cy + 18:.1f} L{cx:.1f} {cy - length}" stroke="{accent}" stroke-width="1.4" opacity=".75"/>')
    out.append(f'<rect x="{cx - 4:.1f}" y="{cy - length + 16:.1f}" width="8" height="{r(4, 40, 56):.1f}" fill="{color}" fill-opacity=".4"/>')
    out.append(f'<rect x="{cx - 3:.1f}" y="{cy + 16:.1f}" width="6" height="{r(5, 92, 118):.1f}" rx="3" fill="#1f2937" stroke="{color}" stroke-width="2"/>')
    out.append(f'<path d="M{cx - 6:.1f} {cy + 70:.1f} L{cx + 6:.1f} {cy + 82:.1f} L{cx - 6:.1f} {cy + 94:.1f} Z" fill="{color}" fill-opacity=".4"/>')
    return out


def _draw_rod(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    length = r(2, 108, 140)
    out = [f'<rect x="{cx - 4:.1f}" y="{cy - length:.1f}" width="8" height="{length:.1f}" rx="4" fill="#1f2937" stroke="{color}" stroke-width="2"/>']
    for k in range(r(3, 3, 6)):
        y = cy - length + 20 + k * (length - 36) / max(r(3, 3, 6), 1)
        out.append(f'<path d="M{cx - 7:.1f} {y:.1f} L{cx + 7:.1f} {y:.1f}" stroke="{color}" stroke-width="1.4" opacity=".55"/>')
    out.append(f'<circle cx="{cx:.1f}" cy="{cy - length - 8:.1f}" r="{r(4, 6, 10):.1f}" fill="{color}" fill-opacity=".6"/>')
    out.append(f'<circle cx="{cx:.1f}" cy="{cy + 12:.1f}" r="{r(5, 6, 9):.1f}" fill="{color}" fill-opacity=".55"/>')
    return out


def _draw_shard(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    h = r(2, 78, 116)
    w = r(3, 16, 28)
    tilt = r(4, -18, 18)
    pts = _path((cx - w, cy + h * 0.5), (cx - w * 0.4, cy - h * 0.45), (cx + w * 0.2, cy - h * 0.62), (cx + w, cy - h * 0.1), (cx + w * 0.55, cy + h * 0.58))
    out = [f'<path d="M{pts} Z" fill="{color}" fill-opacity=".26" stroke="{color}" stroke-width="3" transform="rotate({tilt} {cx} {cy})"/>']
    out.append(f'<path d="M{cx - w * 0.5:.1f} {cy + h * 0.32:.1f} L{cx + w * 0.18:.1f} {cy - h * 0.52:.1f}" stroke="{accent}" stroke-width="1.3" opacity=".7"/>')
    return out


def _draw_coil(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    seg = r(2, 34, 48)
    out = []
    for k in range(r(3, 4, 7)):
        y = cy - (r(3, 3, 6) * seg) + k * seg
        xoff = -10 + k * 3
        out.append(f'<path d="M{cx - seg + xoff:.1f} {y:.1f} Q{cx + xoff:.1f} {y - 24:.1f} {cx + seg + xoff:.1f} {y:.1f}" fill="none" stroke="{color}" stroke-width="3"/>')
    out.append(f'<path d="M{cx:.1f} {cy - 70:.1f} L{cx:.1f} {cy + 78:.1f}" stroke="{accent}" stroke-width="1.2" opacity=".6"/>')
    return out


def _draw_axe(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    width = r(2, 26, 38)
    height = r(3, 34, 50)
    out = [f'<path d="M{cx - 4:.1f} {cy - height:.1f} C{cx - width * 2:.1f} {cy - height * 0.4:.1f}, {cx - width * 1.8:.1f} {cy + height * 0.4:.1f}, {cx - 4:.1f} {cy + height:.1f} Z" fill="{color}" fill-opacity=".24" stroke="{color}" stroke-width="3"/>']
    out.append(f'<path d="M{cx - 4:.1f} {cy - height:.1f} C{cx - width * 1.4:.1f} {cy - height * 0.2:.1f}, {cx - width:.1f} {cy + height * 0.35:.1f}, {cx - 4:.1f} {cy + height:.1f}" stroke="{accent}" stroke-width="1.2" opacity=".6"/>')
    out.append(f'<rect x="{cx - 5:.1f}" y="{cy - height * 0.54:.1f}" width="10" height="{height * 1.08:.1f}" rx="4" fill="#1f2937" stroke="{color}" stroke-width="2"/>')
    out.append(f'<rect x="{cx - 4:.1f}" y="{cy + height * 0.55:.1f}" width="8" height="{r(4, 54, 78):.1f}" rx="3" fill="#1f2937" stroke="{color}" stroke-width="2"/>')
    return out


def _draw_veil(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    w = r(2, 62, 88)
    h = r(3, 86, 116)
    out = [f'<path d="M{cx - w:.1f} {cy - h * 0.72:.1f} Q{cx} {cy - h * 1.12:.1f} {cx + w:.1f} {cy - h * 0.72:.1f} L{cx + w * 0.92:.1f} {cy + h * 0.62:.1f} Q{cx} {cy + h * 0.92:.1f} {cx - w * 0.92:.1f} {cy + h * 0.62:.1f} Z" fill="{color}" fill-opacity=".16" stroke="{color}" stroke-width="3"/>']
    for k in range(r(3, 3, 5)):
        y = cy - h * 0.45 + k * 20
        out.append(f'<path d="M{cx - w + 8:.1f} {y:.1f} Q{cx} {y + 14:.1f} {cx + w - 8:.1f} {y - 4:.1f}" stroke="{accent}" stroke-width="1" opacity=".45"/>')
    out.append(f'<circle cx="{cx:.1f}" cy="{cy - h * 0.68:.1f}" r="7" fill="{color}" fill-opacity=".65"/>')
    return out


def _draw_shroud(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    w = r(2, 46, 66)
    h = r(3, 118, 158)
    out = [f'<path d="M{cx - w * 0.5:.1f} {cy - h * 0.95:.1f} C{cx - w * 0.7:.1f} {cy - h * 0.34:.1f}, {cx - w:.1f} {cy + h * 0.1:.1f}, {cx - w * 0.66:.1f} {cy + h * 0.72:.1f} C{cx - 16:.1f} {cy + h * 0.9:.1f}, {cx + 16:.1f} {cy + h * 0.9:.1f}, {cx + w * 0.66:.1f} {cy + h * 0.72:.1f} C{cx + w:.1f} {cy + h * 0.1:.1f}, {cx + w * 0.7:.1f} {cy - h * 0.34:.1f}, {cx + w * 0.5:.1f} {cy - h * 0.95:.1f} Z" fill="{color}" fill-opacity=".18" stroke="{color}" stroke-width="3"/>']
    out.append(f'<path d="M{cx - w * 0.34:.1f} {cy - h * 0.82:.1f} Q{cx} {cy - h * 0.44:.1f} {cx + w * 0.34:.1f} {cy - h * 0.82:.1f}" stroke="{accent}" stroke-width="1.3" opacity=".55"/>')
    out.append(f'<path d="M{cx - 2:.1f} {cy - h * 0.86:.1f} L{cx - 6:.1f} {cy + h * 0.34:.1f}" stroke="{color}" stroke-width="1.6" opacity=".55"/>')
    out.append(f'<path d="M{cx + 2:.1f} {cy - h * 0.86:.1f} L{cx + 6:.1f} {cy + h * 0.34:.1f}" stroke="{color}" stroke-width="1.6" opacity=".55"/>')
    return out


def _draw_plate(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    w = r(2, 66, 92)
    h = r(3, 76, 108)
    out = [f'<path d="M{cx - w:.1f} {cy - h * 0.2:.1f} L{cx - w * 0.46:.1f} {cy - h * 0.56:.1f} L{cx - 18:.1f} {cy - h * 0.78:.1f} L{cx + 18:.1f} {cy - h * 0.78:.1f} L{cx + w * 0.46:.1f} {cy - h * 0.56:.1f} L{cx + w:.1f} {cy - h * 0.2:.1f} L{cx + w * 0.78:.1f} {cy + h * 0.52:.1f} L{cx} {cy + h * 0.82:.1f} L{cx - w * 0.78:.1f} {cy + h * 0.52:.1f} Z" fill="{color}" fill-opacity=".22" stroke="{color}" stroke-width="3"/>']
    out.append(f'<path d="M{cx - w * 0.78:.1f} {cy - h * 0.3:.1f} L{cx + w * 0.78:.1f} {cy - h * 0.3:.1f}" stroke="{color}" stroke-width="1.5" opacity=".6"/>')
    out.append(f'<circle cx="{cx:.1f}" cy="{cy + 6:.1f}" r="{r(4, 13, 20):.1f}" fill="none" stroke="{accent}" stroke-width="1.8" opacity=".72"/>')
    out.append(f'<circle cx="{cx:.1f}" cy="{cy + 6:.1f}" r="{r(5, 6, 10):.1f}" fill="{color}" fill-opacity=".5"/>')
    return out


def _draw_mantle(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    w = r(2, 58, 82)
    h = r(3, 74, 104)
    out = [f'<path d="M{cx - w:.1f} {cy - h * 0.14:.1f} L{cx - w * 0.62:.1f} {cy - h * 0.56:.1f} L{cx - 14} {cy - h * 0.72:.1f} L{cx + 14} {cy - h * 0.72:.1f} L{cx + w * 0.62:.1f} {cy - h * 0.56:.1f} L{cx + w:.1f} {cy - h * 0.14:.1f} L{cx + w * 0.8:.1f} {cy + h * 0.6:.1f} L{cx - w * 0.8:.1f} {cy + h * 0.6:.1f} Z" fill="{color}" fill-opacity=".18" stroke="{color}" stroke-width="3"/>']
    out.append(f'<path d="M{cx - w * 0.86:.1f} {cy + h * 0.35:.1f} Q{cx} {cy + h * 0.58:.1f} {cx + w * 0.86:.1f} {cy + h * 0.35:.1f}" stroke="{accent}" stroke-width="1.1" opacity=".5"/>')
    out.append(f'<circle cx="{cx:.1f}" cy="{cy - h * 0.64:.1f}" r="5" fill="{color}" fill-opacity=".7"/>')
    return out


def _draw_shield(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    w = r(2, 58, 82)
    h = r(3, 78, 108)
    out = [f'<path d="M{cx:.1f} {cy - h * 0.72:.1f} L{cx + w:.1f} {cy - h * 0.5:.1f} L{cx + w:.1f} {cy + h * 0.1:.1f} Q{cx + w * 0.72:.1f} {cy + h * 0.54:.1f} {cx:.1f} {cy + h * 0.82:.1f} Q{cx - w * 0.72:.1f} {cy + h * 0.54:.1f} {cx - w:.1f} {cy + h * 0.1:.1f} L{cx - w:.1f} {cy - h * 0.5:.1f} Z" fill="{color}" fill-opacity=".2" stroke="{color}" stroke-width="3"/>']
    out.append(f'<path d="M{cx:.1f} {cy - h * 0.64:.1f} L{cx:.1f} {cy + h * 0.72:.1f}" stroke="{accent}" stroke-width="1.3" opacity=".55"/>')
    out.append(f'<path d="M{cx - w * 0.56:.1f} {cy - h * 0.2:.1f} L{cx + w * 0.56:.1f} {cy - h * 0.2:.1f}" stroke="{accent}" stroke-width="1.2" opacity=".5"/>')
    out.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r(4, 11, 16):.1f}" fill="none" stroke="{color}" stroke-width="2"/>')
    return out


def _draw_harness(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    w = r(2, 42, 62)
    h = r(3, 104, 142)
    out = [f'<path d="M{cx - w:.1f} {cy - h * 0.58:.1f} L{cx + w:.1f} {cy - h * 0.58:.1f} L{cx + w * 0.86:.1f} {cy + h * 0.52:.1f} L{cx - w * 0.86:.1f} {cy + h * 0.52:.1f} Z" fill="{color}" fill-opacity=".18" stroke="{color}" stroke-width="3"/>']
    for k in range(r(3, 3, 5)):
        y = cy - h * 0.38 + k * 20
        out.append(f'<path d="M{cx - w + 8:.1f} {y:.1f} L{cx + w - 8:.1f} {y:.1f}" stroke="{accent}" stroke-width="1" opacity=".5"/>')
    out.append(f'<circle cx="{cx:.1f}" cy="{cy + 4:.1f}" r="7" fill="{color}" fill-opacity=".55"/>')
    return out


def _draw_gauntlet(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    w = r(2, 26, 38)
    h = r(3, 74, 100)
    out = [f'<path d="M{cx - w:.1f} {cy - h * 0.66:.1f} C{cx - w * 1.28:.1f} {cy - h * 0.18:.1f}, {cx - w * 1.05:.1f} {cy + h * 0.34:.1f}, {cx - w * 0.82:.1f} {cy + h * 0.62:.1f} L{cx + w * 0.82:.1f} {cy + h * 0.62:.1f} C{cx + w * 1.05:.1f} {cy + h * 0.34:.1f}, {cx + w * 1.28:.1f} {cy - h * 0.18:.1f}, {cx + w:.1f} {cy - h * 0.66:.1f} Z" fill="{color}" fill-opacity=".22" stroke="{color}" stroke-width="3"/>']
    for k in range(r(3, 3, 5)):
        y = cy - h * 0.42 + k * 18
        out.append(f'<path d="M{cx - w * 0.82:.1f} {y:.1f} L{cx + w * 0.82:.1f} {y:.1f}" stroke="{accent}" stroke-width="1" opacity=".45"/>')
    return out


def _draw_charm(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    size = r(2, 40, 62)
    gap = r(3, 22, 38)
    out = [f'<path d="M{cx:.1f} {cy - size - gap:.1f} L{cx:.1f} {cy - size * 0.34:.1f}" stroke="{accent}" stroke-width="2" opacity=".8"/>']
    out.append(f'<circle cx="{cx:.1f}" cy="{cy - size * 0.34:.1f}" r="5" fill="{accent}" opacity=".5"/>')
    out.append(f'<path d="M{cx - size * 0.78:.1f} {cy - size * 0.2:.1f} Q{cx} {cy - size:.1f} {cx + size * 0.78:.1f} {cy - size * 0.2:.1f} L{cx + size * 0.58:.1f} {cy + size * 0.62:.1f} Q{cx} {cy + size:.1f} {cx - size * 0.58:.1f} {cy + size * 0.62:.1f} Z" fill="{color}" fill-opacity=".22" stroke="{color}" stroke-width="3"/>')
    out.append(f'<path d="M{cx - size * 0.38:.1f} {cy + size * 0.2:.1f} L{cx + size * 0.38:.1f} {cy + size * 0.2:.1f}" stroke="{accent}" stroke-width="1.2" opacity=".6"/>')
    return out


def _draw_token(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    size = r(2, 34, 56)
    kind = r(3, 0, 3)
    if kind == 0:
        path = f"M{cx - size:.1f} {cy} A{size:.1f} {size:.1f} 0 1 1 {cx + size:.1f} {cy} A{size:.1f} {size:.1f} 0 1 1 {cx - size:.1f} {cy} Z"
    else:
        path = f"M{cx - size:.1f} {cy - size * 0.7:.1f} L{cx + size:.1f} {cy - size * 0.7:.1f} L{cx + size * 0.55:.1f} {cy + size * 0.7:.1f} L{cx - size * 0.55:.1f} {cy + size * 0.7:.1f} Z"
    out = [f'<path d="{path}" fill="{color}" fill-opacity=".2" stroke="{color}" stroke-width="3"/>']
    out.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r(4, 8, 14):.1f}" fill="none" stroke="{accent}" stroke-width="1.4" opacity=".65"/>')
    return out


def _draw_lantern(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    w = r(2, 28, 40)
    h = r(3, 52, 72)
    out = [f'<path d="M{cx - w:.1f} {cy - h * 0.6:.1f} L{cx + w:.1f} {cy - h * 0.6:.1f} L{cx + w * 0.76:.1f} {cy + h * 0.62:.1f} L{cx - w * 0.76:.1f} {cy + h * 0.62:.1f} Z" fill="{color}" fill-opacity=".18" stroke="{color}" stroke-width="3"/>']
    out.append(f'<path d="M{cx - w * 0.36:.1f} {cy - h * 0.78:.1f} L{cx + w * 0.36:.1f} {cy - h * 0.78:.1f} L{cx + w * 0.1:.1f} {cy - h * 0.9:.1f} L{cx - w * 0.1:.1f} {cy - h * 0.9:.1f} Z" fill="{color}" fill-opacity=".5"/>')
    out.append(f'<path d="M{cx - w * 0.7:.1f} {cy:.1f} L{cx + w * 0.7:.1f} {cy:.1f}" stroke="{accent}" stroke-width="1" opacity=".55"/>')
    out.append(f'<rect x="{cx - w * 0.4:.1f}" y="{cy + h * 0.62:.1f}" width="{w * 0.8:.1f}" height="6" rx="3" fill="{color}" fill-opacity=".5"/>')
    return out


def _draw_stone(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    w = r(2, 34, 56)
    h = r(3, 40, 62)
    out = [f'<path d="M{cx - w:.1f} {cy + h * 0.6:.1f} Q{cx - w * 1.2:.1f} {cy - h * 0.3:.1f}, {cx - w * 0.3:.1f} {cy - h * 0.66:.1f} Q{cx + w * 0.5:.1f} {cy - h:.1f}, {cx + w:.1f} {cy - h * 0.2:.1f} Q{cx + w * 0.92:.1f} {cy + h * 0.52:.1f} {cx:.1f} {cy + h * 0.68:.1f} Z" fill="{color}" fill-opacity=".2" stroke="{color}" stroke-width="3"/>']
    out.append(f'<path d="M{cx - w * 0.46:.1f} {cy + h * 0.16:.1f} C{cx - w * 0.2:.1f} {cy - h * 0.36:.1f}, {cx + w * 0.12:.1f} {cy - h * 0.28:.1f}, {cx + w * 0.42:.1f} {cy + h * 0.08:.1f}" stroke="{accent}" stroke-width="1.1" opacity=".55"/>')
    return out


def _draw_bell(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    w = r(2, 34, 50)
    h = r(3, 46, 70)
    out = [f'<path d="M{cx - w * 0.36:.1f} {cy - h * 0.72:.1f} L{cx + w * 0.36:.1f} {cy - h * 0.72:.1f} C{cx + w * 0.78:.1f} {cy - h * 0.2:.1f}, {cx + w:.1f} {cy + h * 0.34:.1f}, {cx + w:.1f} {cy + h * 0.5:.1f} L{cx - w:.1f} {cy + h * 0.5:.1f} C{cx - w:.1f} {cy + h * 0.34:.1f}, {cx - w * 0.78:.1f} {cy - h * 0.2:.1f}, {cx - w * 0.36:.1f} {cy - h * 0.72:.1f} Z" fill="{color}" fill-opacity=".2" stroke="{color}" stroke-width="3"/>']
    out.append(f'<path d="M{cx - w:.1f} {cy + h * 0.5:.1f} L{cx - w * 1.1:.1f} {cy + h * 0.62:.1f} L{cx + w * 1.1:.1f} {cy + h * 0.62:.1f} L{cx + w:.1f} {cy + h * 0.5:.1f}" fill="{color}" fill-opacity=".4"/>')
    out.append(f'<circle cx="{cx:.1f}" cy="{cy + h * 0.72:.1f}" r="5" fill="{accent}" opacity=".6"/>')
    out.append(f'<path d="M{cx:.1f} {cy - h * 0.72:.1f} L{cx:.1f} {cy - h * 0.94:.1f}" stroke="{color}" stroke-width="3"/>')
    out.append(f'<circle cx="{cx:.1f}" cy="{cy - h * 0.98:.1f}" r="4" fill="{color}" fill-opacity=".7"/>')
    return out


def _draw_ring(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    rx = r(2, 42, 62)
    ry = r(3, 52, 76)
    out = [f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="none" stroke="{color}" stroke-width="5"/>']
    out.append(f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx - 10:.1f}" ry="{ry - 14:.1f}" fill="{color}" fill-opacity=".12"/>')
    out.append(f'<circle cx="{cx:.1f}" cy="{cy - ry + 4:.1f}" r="5" fill="{accent}" opacity=".6"/>')
    out.append(f'<path d="M{cx - rx:.1f} {cy - ry * 0.2:.1f} L{cx + rx:.1f} {cy - ry * 0.2:.1f}" stroke="{accent}" stroke-width="1" opacity=".5"/>')
    return out


def _draw_pendant(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    size = r(2, 26, 44)
    gap = r(3, 38, 60)
    out = [f'<path d="M{cx - size * 0.7:.1f} {cy - gap - size:.1f} Q{cx} {cy - gap - size * 2:.1f} {cx + size * 0.7:.1f} {cy - gap - size:.1f}" fill="none" stroke="{accent}" stroke-width="1.6" opacity=".7"/>']
    out.append(f'<path d="M{cx - size * 0.5:.1f} {cy - gap:.1f} L{cx + size * 0.5:.1f} {cy - gap:.1f}" stroke="{accent}" stroke-width="1.4" opacity=".7"/>')
    out.append(f'<path d="M{cx - size * 0.62:.1f} {cy - gap + size * 0.2:.1f} Q{cx} {cy - gap + size:.1f} {cx + size * 0.62:.1f} {cy - gap + size * 0.2:.1f} L{cx + size * 0.42:.1f} {cy - gap + size:.1f} Q{cx} {cy - gap + size * 1.32:.1f} {cx - size * 0.42:.1f} {cy - gap + size:.1f} Z" fill="{color}" fill-opacity=".22" stroke="{color}" stroke-width="3"/>')
    return out


def _draw_mask(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    w = r(2, 42, 60)
    h = r(3, 58, 82)
    out = [f'<path d="M{cx - w:.1f} {cy - h * 0.32:.1f} Q{cx} {cy - h:.1f} {cx + w:.1f} {cy - h * 0.32:.1f} Q{cx + w:.1f} {cy + h * 0.46:.1f} {cx:.1f} {cy + h * 0.82:.1f} Q{cx - w:.1f} {cy + h * 0.46:.1f} {cx - w:.1f} {cy - h * 0.32:.1f} Z" fill="{color}" fill-opacity=".2" stroke="{color}" stroke-width="3"/>']
    out.append(f'<ellipse cx="{cx - w * 0.42:.1f}" cy="{cy - h * 0.12:.1f}" rx="{r(4, 6, 9):.1f}" ry="6" fill="#0b1220" stroke="{accent}" stroke-width="1.2" opacity=".7"/>')
    out.append(f'<ellipse cx="{cx + w * 0.42:.1f}" cy="{cy - h * 0.12:.1f}" rx="{r(5, 6, 9):.1f}" ry="6" fill="#0b1220" stroke="{accent}" stroke-width="1.2" opacity=".7"/>')
    out.append(f'<path d="M{cx - 22:.1f} {cy + h * 0.28:.1f} Q{cx} {cy + h * 0.46:.1f} {cx + 22:.1f} {cy + h * 0.28:.1f}" stroke="{color}" stroke-width="1.6" opacity=".65"/>')
    return out


def _draw_vial(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    w = r(2, 24, 36)
    h = r(3, 54, 76)
    out = [f'<path d="M{cx - w:.1f} {cy - h * 0.55:.1f} C{cx - w:.1f} {cy - h * 0.15:.1f}, {cx - w * 0.7:.1f} {cy - h * 0.0:.1f} {cx - w * 0.7:.1f} {cy + h * 0.52:.1f} L{cx + w * 0.7:.1f} {cy + h * 0.52:.1f} C{cx + w * 0.7:.1f} {cy - h * 0.0:.1f}, {cx + w:.1f} {cy - h * 0.15:.1f}, {cx + w:.1f} {cy - h * 0.55:.1f} Z" fill="{color}" fill-opacity=".18" stroke="{color}" stroke-width="3"/>']
    out.append(f'<path d="M{cx - w * 0.42:.1f} {cy + h * 0.44:.1f} C{cx - w * 0.3:.1f} {cy + h * 0.08:.1f}, {cx + w * 0.3:.1f} {cy + h * 0.08:.1f}, {cx + w * 0.42:.1f} {cy + h * 0.44:.1f}" fill="{color}" fill-opacity=".28"/>')
    out.append(f'<rect x="{cx - w * 0.24:.1f}" y="{cy - h * 0.72:.1f}" width="{w * 0.48:.1f}" height="{h * 0.2:.1f}" rx="3" fill="{accent}" opacity=".6"/>')
    return out


def _draw_compass(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    size = r(2, 38, 56)
    tilt = r(3, 0, 360)
    out = [f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{size:.1f}" fill="{color}" fill-opacity=".16" stroke="{color}" stroke-width="3"/>']
    out.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{size * 0.8:.1f}" fill="none" stroke="{accent}" stroke-width="1" opacity=".55"/>')
    out.append(f'<path d="M{cx:.1f} {cy - size * 0.72:.1f} L{cx + size * 0.3:.1f} {cy:.1f} L{cx:.1f} {cy + size * 0.72:.1f} L{cx - size * 0.3:.1f} {cy:.1f} Z" fill="{color}" fill-opacity=".45" transform="rotate({tilt} {cx} {cy})"/>')
    out.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="4" fill="{accent}" opacity=".7"/>')
    return out


def _draw_crown(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    w = r(2, 50, 72)
    h = r(3, 30, 48)
    spikes = r(4, 4, 6)
    pts = [(cx + w, cy + h * 0.6)]
    for k in range(spikes):
        x = cx + w - (2 * w * k / (spikes - 1))
        pts.append((x - w * 0.14 / max(1, spikes * 0.32), cy - h * 0.7))
        pts.append((x - w * 0.14 / max(1, spikes * 0.32) + 0.1, cy - h * 0.12))
        pts.append((x + w * 0.22, cy - h * 0.12))
    pts.append((cx - w, cy + h * 0.6))
    out = [f'<path d="M{_path(*pts)} Z" fill="{color}" fill-opacity=".22" stroke="{color}" stroke-width="3"/>']
    out.append(f'<path d="M{cx - w:.1f} {cy + h * 0.54:.1f} L{cx + w:.1f} {cy + h * 0.54:.1f}" stroke="{accent}" stroke-width="1.2" opacity=".55"/>')
    out.append(f'<circle cx="{cx:.1f}" cy="{cy - h * 0.78:.1f}" r="4" fill="{accent}" opacity=".7"/>')
    return out


def _draw_thread(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    length = r(2, 100, 140)
    seg = r(3, 28, 44)
    out = [f'<path d="M{cx - 24:.1f} {cy - length:.1f} C{cx + 24:.1f} {cy - length - 18:.1f}, {cx - 30:.1f} {cy - length * 0.4:.1f}, {cx + 26:.1f} {cy - length * 0.2:.1f} C{cx - 20:.1f} {cy - length * 0.05:.1f}, {cx + 26:.1f} {cy + 20:.1f}, {cx - 22:.1f} {cy + length * 0.48:.1f}" fill="none" stroke="{color}" stroke-width="3"/>']
    out.append(f'<path d="M{cx + 16:.1f} {cy - length * 0.36:.1f} C{cx - 10:.1f} {cy - length * 0.28:.1f}, {cx + 18:.1f} {cy - length * 0.08:.1f}, {cx - 14:.1f} {cy:.1f}" fill="none" stroke="{accent}" stroke-width="1" opacity=".55"/>')
    out.append(f'<circle cx="{cx - 22:.1f}" cy="{cy + length * 0.48:.1f}" r="5" fill="{color}" fill-opacity=".6"/>')
    return out


def _draw_ember(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    size = r(2, 30, 46)
    out = [f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{size:.1f}" fill="{color}" fill-opacity=".16"/>']
    out.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{size * 0.62:.1f}" fill="{color}" fill-opacity=".28"/>')
    out.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{size * 0.25:.1f}" fill="{accent}" opacity=".55"/>')
    return out


def _draw_seed(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    size = r(2, 26, 42)
    out = [f'<path d="M{cx - size * 0.72:.1f} {cy + size * 0.8:.1f} Q{cx - size * 1.3:.1f} {cy:.1f}, {cx:.1f} {cy - size * 0.36:.1f} Q{cx + size * 1.3:.1f} {cy:.1f}, {cx + size * 0.72:.1f} {cy + size * 0.8:.1f} Z" fill="{color}" fill-opacity=".22" stroke="{color}" stroke-width="3"/>']
    out.append(f'<path d="M{cx:.1f} {cy - size * 0.32:.1f} C{cx - 8:.1f} {cy - size * 0.9:.1f}, {cx + 8:.1f} {cy - size * 0.9:.1f}, {cx:.1f} {cy - size * 0.32:.1f}" fill="none" stroke="{accent}" stroke-width="1.4" opacity=".7"/>')
    out.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="5" fill="{color}" fill-opacity=".55"/>')
    return out


def _draw_key(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    head = r(2, 30, 44)
    length = r(3, 64, 88)
    out = [f'<path d="M{cx - head * 0.5:.1f} {cy - head * 0.8:.1f} A{head:.1f} {head:.1f} 0 1 1 {cx + head * 0.5:.1f} {cy - head * 0.8:.1f} Z" fill="{color}" fill-opacity=".16" stroke="{color}" stroke-width="3"/>']
    out.append(f'<path d="M{cx:.1f} {cy - head * 0.4:.1f} L{cx:.1f} {cy + length:.1f}" stroke="{color}" stroke-width="4"/>')
    out.append(f'<path d="M{cx:.1f} {cy + length:.1f} L{cx + 16:.1f} {cy + length:.1f} M{cx:.1f} {cy + length * 0.8:.1f} L{cx + 12:.1f} {cy + length * 0.8:.1f}" stroke="{color}" stroke-width="2.4"/>')
    out.append(f'<circle cx="{cx:.1f}" cy="{cy - head * 0.8:.1f}" r="4" fill="{accent}" opacity=".55"/>')
    return out


def _draw_eye(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    w = r(2, 46, 66)
    h = r(3, 24, 34)
    out = [f'<path d="M{cx - w:.1f} {cy:.1f} Q{cx} {cy - h:.1f} {cx + w:.1f} {cy:.1f} Q{cx} {cy + h:.1f} {cx - w:.1f} {cy:.1f} Z" fill="{color}" fill-opacity=".16" stroke="{color}" stroke-width="3"/>']
    out.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r(4, 12, 18):.1f}" fill="none" stroke="{accent}" stroke-width="1.6" opacity=".7"/>')
    out.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="4" fill="{accent}" opacity=".55"/>')
    return out


def _draw_tear(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    size = r(2, 34, 56)
    out = [f'<path d="M{cx:.1f} {cy - size:.1f} C{cx + size * 0.72:.1f} {cy - size * 0.18:.1f}, {cx + size * 0.78:.1f} {cy + size * 0.42:.1f}, {cx:.1f} {cy + size * 0.62:.1f} C{cx - size * 0.78:.1f} {cy + size * 0.42:.1f}, {cx - size * 0.72:.1f} {cy - size * 0.18:.1f}, {cx:.1f} {cy - size:.1f} Z" fill="{color}" fill-opacity=".22" stroke="{color}" stroke-width="3"/>']
    out.append(f'<path d="M{cx:.1f} {cy - size * 0.74:.1f} L{cx:.1f} {cy + size * 0.36:.1f}" stroke="{accent}" stroke-width="1.2" opacity=".6"/>')
    return out


def _draw_bracelet(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    rx = r(2, 44, 62)
    ry = r(3, 58, 80)
    out = [f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="none" stroke="{color}" stroke-width="5"/>']
    for k in range(r(4, 4, 7)):
        import math
        a = math.radians((360 / r(4, 4, 7)) * k)
        x = cx + math.cos(a) * rx
        y = cy + math.sin(a) * ry
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{color}" fill-opacity=".6"/>')
    return out


def _draw_fragment(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    h = r(2, 72, 104)
    w = r(3, 16, 26)
    out = [f'<path d="M{cx - w:.1f} {cy + h * 0.5:.1f} L{cx - w * 0.62:.1f} {cy - h * 0.34:.1f} L{cx:.1f} {cy - h * 0.6:.1f} L{cx + w * 0.62:.1f} {cy - h * 0.22:.1f} L{cx + w:.1f} {cy + h * 0.46:.1f} Z" fill="{color}" fill-opacity=".24" stroke="{color}" stroke-width="3"/>']
    out.append(f'<path d="M{cx - w * 0.6:.1f} {cy - h * 0.3:.1f} L{cx + w * 0.2:.1f} {cy + h * 0.3:.1f}" stroke="{accent}" stroke-width="1.2" opacity=".6"/>')
    return out


def _draw_link(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    size = r(2, 30, 46)
    out = [f'<circle cx="{cx - size * 0.66:.1f}" cy="{cy:.1f}" r="{size * 0.7:.1f}" fill="none" stroke="{color}" stroke-width="5"/>']
    out.append(f'<circle cx="{cx + size * 0.66:.1f}" cy="{cy:.1f}" r="{size * 0.7:.1f}" fill="none" stroke="{color}" stroke-width="5"/>')
    out.append(f'<path d="M{cx - size * 0.57:.1f} {cy - size * 0.5:.1f} L{cx + size * 0.57:.1f} {cy - size * 0.5:.1f}" stroke="{accent}" stroke-width="1.2" opacity=".55"/>')
    return out


def _draw_clasp(cx: float, cy: float, r, color: str, accent: str) -> list[str]:
    w = r(2, 30, 44)
    h = r(3, 24, 36)
    out = [f'<path d="M{cx - w:.1f} {cy:.1f} Q{cx} {cy - h:.1f} {cx + w:.1f} {cy:.1f} Q{cx} {cy + h:.1f} {cx - w:.1f} {cy:.1f} Z" fill="{color}" fill-opacity=".18" stroke="{color}" stroke-width="3"/>']
    out.append(f'<path d="M{cx - w * 0.38:.1f} {cy + h * 0.22:.1f} L{cx + w * 0.38:.1f} {cy + h * 0.22:.1f}" stroke="{accent}" stroke-width="1.2" opacity=".6"/>')
    out.append(f'<circle cx="{cx:.1f}" cy="{cy - h * 0.3:.1f}" r="4" fill="{color}" fill-opacity=".6"/>')
    return out


def _draw_fallback(cx: float, cy: float, r, color: str, accent: str, itype: str) -> list[str]:
    if itype == "W":
        return _draw_blade(cx, cy, r, color, accent)
    if itype == "S":
        return _draw_plate(cx, cy, r, color, accent)
    return _draw_charm(cx, cy, r, color, accent)


DRAW_FN = {
    "blade": _draw_blade,
    "fang": _draw_fang,
    "lens": _draw_lens,
    "maul": _draw_maul,
    "hammer": _draw_hammer,
    "spear": _draw_spear,
    "rod": _draw_rod,
    "shard": _draw_shard,
    "coil": _draw_coil,
    "axe": _draw_axe,
    "veil": _draw_veil,
    "shroud": _draw_shroud,
    "plate": _draw_plate,
    "mantle": _draw_mantle,
    "shield": _draw_shield,
    "harness": _draw_harness,
    "gauntlet": _draw_gauntlet,
    "charm": _draw_charm,
    "token": _draw_token,
    "lantern": _draw_lantern,
    "stone": _draw_stone,
    "bell": _draw_bell,
    "ring": _draw_ring,
    "pendant": _draw_pendant,
    "mask": _draw_mask,
    "vial": _draw_vial,
    "compass": _draw_compass,
    "crown": _draw_crown,
    "thread": _draw_thread,
    "ember": _draw_ember,
    "seed": _draw_seed,
    "key": _draw_key,
    "eye": _draw_eye,
    "tear": _draw_tear,
    "bracelet": _draw_bracelet,
    "fragment": _draw_fragment,
    "link": _draw_link,
    "clasp": _draw_clasp,
}


def function_motifs(it: dict) -> list[tuple[str, float, float, float, str]]:
    """Return small semantic motifs tied to the item's function language.

    Each tuple is (kind, x, y, scale, color). The motifs are drawn as simple
    elemental marks so art reflects the item's function as well as its object.
    """
    text = detectable_text(it).lower()
    color = it["color"]
    motifs: list[tuple[str, float, float, float, str]] = []
    if any(w in text for w in ("grief", "sorrow", "weep", "weeps", "lament", "cry", "mourn")):
        motifs.append(("tear", 148.0, 112.0, 0.36, "#e0f2fe"))
        motifs.append(("tear", 252.0, 96.0, 0.26, color))
    if any(w in text for w in ("memory", "remember", "recall", "forget", "forgotten", "witness")):
        motifs.append(("eye", 200.0, 82.0, 0.5, "#e0f2fe"))
    if any(w in text for w in ("silence", "silent", "sound", "toll", "echo", "bell")):
        motifs.append(("ring", 200.0, 320.0, 0.34, color))
    if any(w in text for w in ("corros", "decay", "rot", "acid", "eat", "dissolve")):
        motifs.append(("drop", 152.0, 300.0, 0.28, "#e0f2fe"))
    if any(w in text for w in ("judge", "verdict", "account", "debt", "weight", "burden")):
        motifs.append(("scale", 250.0, 320.0, 0.5, color))
    if any(w in text for w in ("listen", "hearing", "sound", "voice", "whisper")):
        motifs.append(("wave", 162.0, 118.0, 0.42, "#e0f2fe"))
    if any(w in text for w in ("light", "lantern", "glow", "warm", "ember", "flare")):
        motifs.append(("glow", 200.0, 120.0, 0.6, "#f1df76"))
    if any(w in text for w in ("seal", "bind", "locked", "shut", "curse")):
        motifs.append(("key", 152.0, 312.0, 0.3, color))
    if any(w in text for w in ("protect", "guard", "shield", "barrier", "veil")):
        motifs.append(("arc", 200.0, 236.0, 0.72, "#e0f2fe"))
    return motifs


def motif_svg(kind: str, x: float, y: float, scale: float, color: str) -> str:
    s = scale
    if kind == "tear":
        return (
            f'<path d="M{x:.1f} {y - 16 * s:.1f} C{x + 12 * s:.1f} {y - 3 * s:.1f}, '
            f'{x + 12 * s:.1f} {y + 8 * s:.1f}, {x:.1f} {y + 14 * s:.1f} '
            f'C{x - 12 * s:.1f} {y + 8 * s:.1f}, {x - 12 * s:.1f} {y - 3 * s:.1f}, '
            f'{x:.1f} {y - 16 * s:.1f} Z" fill="{color}" opacity=".42"/>'
        )
    if kind == "eye":
        return (
            f'<path d="M{x - 18 * s:.1f} {y:.1f} Q{x:.1f} {y - 8 * s:.1f} {x + 18 * s:.1f} {y:.1f} '
            f'Q{x:.1f} {y + 8 * s:.1f} {x - 18 * s:.1f} {y:.1f} Z" fill="{color}" opacity=".4"/>'
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{4 * s:.1f}" fill="{color}" opacity=".65"/>'
        )
    if kind == "ring":
        return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{14 * s:.1f}" fill="none" stroke="{color}" stroke-width="{4 * s:.1f}" opacity=".42"/>'
    if kind == "drop":
        return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{8 * s:.1f}" fill="{color}" opacity=".36"/>'
    if kind == "scale":
        return (
            f'<path d="M{x:.1f} {y - 13 * s:.1f} L{x:.1f} {y + 13 * s:.1f}" stroke="{color}" stroke-width="{3 * s:.1f}" opacity=".5"/>'
            f'<path d="M{x - 16 * s:.1f} {y - 8 * s:.1f} Q{x:.1f} {y - 14 * s:.1f} {x + 16 * s:.1f} {y - 8 * s:.1f}" fill="none" stroke="{color}" stroke-width="2" opacity=".45"/>'
        )
    if kind == "wave":
        return (
            f'<path d="M{x - 16 * s:.1f} {y:.1f} Q{x} {y - 16 * s:.1f} {x + 16 * s:.1f} {y:.1f}" fill="none" stroke="{color}" stroke-width="{3 * s:.1f}" opacity=".42"/>'
            f'<path d="M{x - 11 * s:.1f} {y + 8 * s:.1f} Q{x} {y - 4 * s:.1f} {x + 11 * s:.1f} {y + 8 * s:.1f}" fill="none" stroke="{color}" stroke-width="{2 * s:.1f}" opacity=".32"/>'
        )
    if kind == "glow":
        return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{12 * s:.1f}" fill="#f1df76" opacity=".22"/>'
    if kind == "key":
        return (
            f'<path d="M{x:.1f} {y - 10 * s:.1f} L{x:.1f} {y + 10 * s:.1f}" stroke="{color}" stroke-width="{2.4 * s:.1f}" opacity=".5"/>'
            f'<circle cx="{x:.1f}" cy="{y - 9 * s:.1f}" r="{5 * s:.1f}" fill="none" stroke="{color}" stroke-width="1.6" opacity=".5"/>'
        )
    if kind == "arc":
        return (
            f'<path d="M{x - 24 * s:.1f} {y:.1f} Q{x:.1f} {y - 26 * s:.1f} {x + 24 * s:.1f} {y:.1f}" fill="none" stroke="{color}" stroke-width="2.4" opacity=".38"/>'
        )
    return ""


def make_svg(item: dict) -> str:
    """Content-driven 400x400 item art.

    The dominant geometry is chosen from the object noun in the item's Title,
    Type descriptor, and Appearance sentence. Function keywords add a small
    elemental motif cluster. Record-specific proportions still vary the
    composition so every item remains structurally unique.
    """
    f = item["fields"]
    code = item["code"]
    name = f["name"] or ""
    itype = item["type"]
    color = item["color"]
    seed_bytes = hashlib.sha256(
        "|".join(
            [
                code,
                name,
                f.get("subtype") or "",
                f.get("appearance") or "",
                f.get("ability_body") or "",
                f.get("canonical_ability") or "",
            ]
        ).encode()
    ).digest()
    seed = int.from_bytes(seed_bytes[:8], "big")

    def r(idx: int, lo: int, hi: int) -> int:
        return lo + ((seed >> (idx * 8)) & 0xFFFF) % max(1, hi - lo + 1)

    obj, base_label = detect_object(item)
    label = appearance_detail_label(item, base_label)
    uid = hashlib.sha1(code.encode()).hexdigest()[:6]
    bg, gl = f"bg{uid}", f"gl{uid}"

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%" role="img" aria-label="{html.escape(name.upper())}">',
    ]
    parts.append("  <!-- SOURCE-DERIVED ART: TYPE + TITLE + APPEARANCE + FUNCTION -->")
    parts.append(f"  <!-- {TYPE_LABEL[itype].upper()} // {label} -->")
    parts.append("  <defs>")
    parts.append(f'    <radialGradient id="{bg}" cx="50%" cy="42%" r="58%">')
    parts.append('      <stop offset="0%" stop-color="#111827"/>')
    parts.append('      <stop offset="100%" stop-color="#030712"/>')
    parts.append("    </radialGradient>")
    parts.append(f'    <radialGradient id="{gl}" cx="50%" cy="46%" r="42%">')
    parts.append(f'      <stop offset="0%" stop-color="{color}" stop-opacity=".2"/>')
    parts.append('      <stop offset="100%" stop-color="#000" stop-opacity="0"/>')
    parts.append("    </radialGradient>")
    parts.append("  </defs>")
    parts.append(f'  <rect x="6" y="6" width="388" height="388" rx="14" fill="url(#{bg})" stroke="{color}" stroke-width="2.4"/>')
    parts.append(f'  <rect x="14" y="14" width="372" height="372" rx="10" fill="none" stroke="#f1df76" stroke-width="1" stroke-dasharray="7 4" opacity=".35"/>')
    parts.append(f'  <circle cx="200" cy="188" r="{108 + r(0, 0, 26)}" fill="url(#{gl})"/>')

    # Main object
    cx, cy = 200.0, 192.0
    draw = DRAW_FN.get(obj)
    if draw is None:
        draw = lambda a, b, c, d, e: _draw_fallback(a, b, c, d, e, itype)  # noqa: E731
    rot = r(1, -12, 12)
    parts.append(f'  <g transform="rotate({rot} {cx} {cy})">')
    parts.extend(draw(cx, cy, r, color, "#e0f2fe"))
    parts.append("  </g>")

    # Appearance-derived detail marks (crystal seams, cracks, folds, ripples,
    # flames, links) — selected from the record's own Appearance/function text.
    parts.extend(appearance_detail_shapes(item, color, r))

    # Function motifs (small, non-duplicating elemental marks)
    motifs = function_motifs(item)
    for idx, (kind, mx, my, scale, mcolor) in enumerate(motifs):
        parts.append(f'  <g transform="rotate({r(2 + idx * 3, -14, 14)} {mx} {my})" opacity=".9">')
        parts.append(f"    " + motif_svg(kind, mx, my, scale, mcolor))
        parts.append("  </g>")

    parts.append(f'  <text x="{16 + r(9, 0, 6)}" y="380" font-family="monospace" font-size="15" letter-spacing="2" fill="{color}">{html.escape(code)}</text>')
    parts.append("</svg>")
    return "\n".join(parts)


def esc(s: str | None) -> str:
    return html.escape(s or "", quote=True)


def md_paras(s: str | None) -> str:
    """Render source text (with **bold** and line breaks) as <p> blocks.

    Heading markers and horizontal rules are stripped so registry text never
    leaks ``###`` or ``---`` into the public page.
    """
    if not s:
        return ""
    out = []
    for para in re.split(r"\n\s*\n", s):
        para = para.strip()
        if not para:
            continue
        para = re.sub(r"(?m)^#{1,6}\s+", "", para)
        para = re.sub(r"(?m)^\s*[-*_]{3,}\s*$", "", para)
        para = re.sub(r"\s*[-*_]{3,}\s*$", "", para)
        para = para.strip()
        if not para:
            continue
        para = esc(para)
        para = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", para)
        para = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", para)
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
        b.append(md_paras(f["appearance"]))
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
    triad.append("  </div>")
    triad.append("</div>")
    c.append("\n".join(triad))

    c.append(CROSS_REF)
    return "\n".join(c)


_SLOT_LETTER = {"W": "B", "S": "C", "G": "D"}


def _footer_for_page(post_main: str, it: dict) -> str:
    """Stamp per-item footer filing fields over the shared footer template."""
    f = it["fields"]
    code = f["code"] or it["code"]
    name_spaced = slugify(f["name"] or it["name_raw"]).replace("-", " ")
    slot = _SLOT_LETTER.get(it["type"], "B")
    src = f"ITEM ID {donor_display(it['donor'])}-{slot}"
    new_post = re.sub(
        r'(<code class="footer-filed-code">)[^<]*(</code>)',
        rf"\g<1>{html.escape(code)}\g<2>",
        post_main,
        count=1,
    )
    new_post = re.sub(
        r'(<span class="footer-filed-name">)[^<]*(</span>)',
        rf"\g<1>{html.escape(name_spaced)}\g<2>",
        new_post,
        count=1,
    )
    new_post = re.sub(
        r'(<code class="footer-filed-src">)[^<]*(</code>)',
        rf"\g<1>{html.escape(src)}\g<2>",
        new_post,
        count=1,
    )
    return new_post


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


def main() -> int:
    global ASSET_VERSION
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--force", action="store_true", help="rewrite every published item page and SVG")
    parser.add_argument("--version", default=ASSET_VERSION)
    args = parser.parse_args()
    ASSET_VERSION = args.version

    find_entity_pages()
    _ENTITY_ART.clear()
    for p in (DOCS / "assets" / "art" / "entities").glob("se-*.svg"):
        m = re.match(r"^se-(\d{3})\.svg$", p.name)
        if m:
            _ENTITY_ART.add(m.group(1))

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

    if args.force:
        todo = items
    else:
        todo = [it for it in items if not (MAW_DIR / it["file"]).exists()]
    if args.limit:
        todo = todo[: args.limit]

    published = 0
    rewritten = 0
    problems: list[str] = []
    for it in todo:
        f = it["fields"]
        if not f.get("name"):
            problems.append(f"{it['path'].name}: no name parsed")
            continue
        svg = make_svg(it)
        content = build_content(it)
        head_title = f'{f["name"]} — Somnarak Wiki'
        desc = f'{TYPE_LABEL[it["type"]]} of {donor_display(it["donor"])} — {it["code"]}'
        new_head = pre_main.replace(
            re.search(r"<title>.*?</title>", pre_main, re.S).group(0), f"<title>{html.escape(head_title)}</title>"
        )
        new_post = _footer_for_page(post_main, it)
        page = new_head + '<main id="content">\n' + content + "\n</main>" + new_post
        if not args.dry_run:
            (MAW_DIR / it["file"]).write_text(page, encoding="utf-8")
            (ART_DIR / it["art_name"]).write_text(svg, encoding="utf-8")
        published += 1
        if args.force:
            rewritten += 1

    mode = "forced rewrite" if args.force else "incremental"
    skipped = len(items) - published - len(problems)
    print(f"registry items: {len(items)}; {mode}: {published} pages + SVGs; skipped: {skipped}")
    if rewritten:
        print(f"rewritten pages + SVGs: {rewritten}")
    if problems:
        print("parse problems:")
        for p in problems[:20]:
            print("  " + p)
    return 0 if not problems else 2


_ENTITY_ART: set[str] = set()

if __name__ == "__main__":
    sys.exit(main())
