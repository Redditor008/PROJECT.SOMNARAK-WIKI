#!/usr/bin/env python3
"""Compare primary SE M.A.W. blocks with matching Side and individual Codices.

This is a conservative review aid, not an auto-fixer. It maps on the dossier's
SECC Designation (never the filename), joins the Side Codex and individual
Weapon/Suit/Stigma records, and parses recognized Side Codex card and set-page
layouts. Reports are candidates for human triage: names can be aliases, some
records describe another form, and fields omitted by one source are not assumed
wrong.

Run from the repository root:
    python3 tools/maw_compare.py
    python3 tools/maw_compare.py --check side --limit 200
    python3 tools/maw_compare.py --check side-internal --limit 50
    python3 tools/maw_compare.py --check suit --limit 200
"""
from __future__ import annotations

import argparse
import csv
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "REFERENCE_SOMNARAK_WIKI" / "MAW_EQUIPMENT_MASTER_REGISTRY.csv"
WORLD = ROOT / "SOMNARAK-WORLD"
CODE_RE = re.compile(r"([CNOAI]-[IVX]+[αβγδω]-\d{3,4}[a-z]?)")
ELEMENTS = ("Lament", "Grudge", "Void", "Weight")
TYPE_TO_ROW = {"Weapon": "Weapon", "Suit": "Suit", "Stigma": "Gift"}
ROW_TO_TYPE = {v: k for k, v in TYPE_TO_ROW.items()}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def designation_from_primary(text: str) -> str | None:
    """Use the SECC table's authoritative designation, not a path prefix."""
    m = re.search(r"^\s*\|\s*\*\*Designation\*\*\s*\|\s*`?([^`\n|]+)", text, re.M)
    code = CODE_RE.search(m.group(1)) if m else None
    return code.group(1) if code else None


def designation_from_side(text: str) -> str | None:
    for line in text.splitlines():
        if "SECC Designation" in line:
            m = CODE_RE.search(line)
            if m:
                return m.group(1)
    return None


def markdown_tables(text: str):
    """Yield contiguous Markdown tables as (line-number, rows)."""
    rows = []
    start = None
    for number, line in enumerate(text.splitlines(), 1):
        if "|" not in line:
            if rows:
                yield start, rows
                rows, start = [], None
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        cells = [re.sub(r"\*\*|`", "", c).strip() for c in cells]
        if not cells or all(re.fullmatch(r"[-: ]+", c or " ") for c in cells):
            if rows:
                continue
            else:
                continue
        if start is None:
            start = number
        rows.append(cells)
    if rows:
        yield start, rows


def normalize_name(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).lower().replace("’", "'")
    value = re.sub(r"^the\s+", "", value.strip())
    value = re.sub(r"\([^)]*\)", "", value)
    return re.sub(r"[^a-z0-9]+", "", value)


def heading_name(text: str) -> str | None:
    m = re.search(
        r"^#\s+M\.A\.W\.\s+(?:WEAPON|SUIT|STIGMA|PROTECTIVE ATTIRE)\s*[—–-]\s*(.+)$",
        text,
        re.M | re.I,
    )
    return m.group(1).strip() if m else None


def parse_primary_blocks(text: str):
    """Return embedded item blocks keyed by canonical item type."""
    lines = text.splitlines()
    in_maw = False
    current_type = current_name = None
    current_start = 0
    body = []
    result = defaultdict(list)
    pattern = re.compile(
        r"^#{3,4}\s+M\.A\.W\.\s+(Weapon|Suit|Stigma|Armor|Armour|Gift)\b\s*(?:[—–-]\s*(.*))?$"
    )
    for number, line in enumerate(lines, 1):
        if re.match(r"^##\s+M\.A\.W\.\s+Equipment\s*$", line):
            in_maw = True
            continue
        if in_maw and re.match(r"^##\s+", line):
            if current_type:
                result[current_type].append((current_name or "", current_start, body))
            break
        if not in_maw:
            continue
        if re.match(r"^#{3,4}\s+", line):
            if current_type:
                result[current_type].append((current_name or "", current_start, body))
            current_type = current_name = None
            body = []
            m = pattern.match(line)
            if m:
                raw_type = m.group(1)
                current_type = {"Armor": "Suit", "Armour": "Suit", "Gift": "Stigma"}.get(raw_type, raw_type)
                current_name = (m.group(2) or "").strip()
                current_start = number
            continue
        if current_type:
            body.append((number, line))
    else:
        if current_type:
            result[current_type].append((current_name or "", current_start, body))
    return result


def value_after_label(text: str, labels: tuple[str, ...]) -> list[str]:
    """Read bold inline fields; stop before a following field on the same line."""
    values = []
    for label in labels:
        pat = re.compile(
            r"\*\*" + re.escape(label) + r"\s*:\*\*\s*(.*?)(?=\s+\*\*[A-Za-z][A-Za-z /-]*\s*:\*\*|\s*\||$)",
            re.I | re.M,
        )
        for m in pat.finditer(text):
            values.append(m.group(1).strip())
    return values


def clean_cell(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().replace("**", "").replace("`", ""))


def add_pattern_facts(facts, value: str):
    """Keep the pattern text and extract its independently comparable details."""
    value = clean_cell(value)
    if not value:
        return
    facts["pattern"].append(value)
    coverage = re.search(r"\bup to\s+(\d+)\s+targets?\b", value, re.I)
    if not coverage:
        coverage = re.search(r"\b(\d+)\s+targets?\b", value, re.I)
    if not coverage and (re.search(r"\bone (?:designated )?target\b", value, re.I) or re.search(r"\bsingle(?:[- ]target)?\b", value, re.I)):
        facts["coverage"].append("1 target")
    elif coverage:
        facts["coverage"].append(coverage.group(0))
    percentages = re.findall(r"\d+(?:\.\d+)?\s*%", value)
    if len(percentages) >= 2 and ("→" in value or "->" in value or "falloff" in value.lower()):
        facts["falloff"].append(value)


def doc_facts(text: str, item_type: str):
    """Extract explicit facts from the individual M.A.W. Codex document."""
    facts = defaultdict(list)
    title = heading_name(text)
    if title:
        facts["name"].append(title)

    # Inline compact metadata used by the newer Codex records.
    m = re.search(r"\*\*Grade\s*/\s*Element:\*\*\s*([^/|\n]+?)\s*/\s*([^|\n]+)", text, re.I)
    if m:
        facts["grade"].append(m.group(1).strip())
        facts["element"].append(m.group(2).strip())
    for value in value_after_label(text, ("Type / Slot",)):
        pair = re.split(r"\s*/\s*", value, maxsplit=1)
        if len(pair) == 2:
            facts["slot"].append(pair[1])
    for value in value_after_label(text, ("Acquisition",)):
        if "%" in value or re.search(r"\d", value):
            facts["chance"].append(value)

    table_rows = []
    for _, table in markdown_tables(text):
        table_rows.extend(table)
        # Key / value tables from older and newer individual Codices.
        for cells in table:
            if len(cells) < 2:
                continue
            key = clean_cell(cells[0]).strip(":").lower()
            value = clean_cell(cells[1])
            if not value:
                continue
            if key == "grade" and re.search(r"[αβγδω]", value):
                facts["grade"].append(value)
            elif key == "element" and re.match(r"(?:Lament|Grudge|Void|Weight|Mixed)\b", value, re.I):
                facts["element"].append(value)
            elif key in ("speed / range", "speed and range"):
                # Compact Codices record both fields in one key/value cell.
                # Keep the paired values separate so a changed descriptor is
                # visible as well as a changed numeric band.
                pair = re.split(r"\s*/\s*", value, maxsplit=1)
                if len(pair) == 2:
                    facts["speed"].append(pair[0])
                    facts["range"].append(pair[1])
            elif key in ("pattern / coverage", "attack pattern / coverage", "pattern / target coverage"):
                pair = re.split(r"\s*/\s*", value, maxsplit=1)
                if len(pair) == 2:
                    add_pattern_facts(facts, pair[0])
                    facts["coverage"].append(pair[1])
            elif key in ("coverage / falloff", "target coverage / falloff"):
                facts["coverage"].append(value)
                facts["falloff"].append(value)
            elif key in ("grade / element", "element / grade"):
                pair = re.split(r"\s*/\s*", value, maxsplit=1)
                if len(pair) == 2:
                    facts["grade"].append(pair[0] if re.search(r"[αβγδω]", pair[0]) else pair[1])
                    facts["element"].append(pair[0] if re.search(r"(?:Lament|Grudge|Void|Weight|Mixed)\b", pair[0], re.I) else pair[1])
            elif key in ("lament / grudge", "grudge / lament", "void / weight", "weight / void"):
                pair = re.split(r"\s*/\s*", value, maxsplit=1)
                elements = re.split(r"\s*/\s*", key)
                if len(pair) == 2 and len(elements) == 2:
                    for element, raw in zip(elements, pair):
                        number = re.search(r"\d+(?:\.\d+)?", raw)
                        if number:
                            facts["resistance"].append((element.title(), number.group(0)))
            elif key in ("maximum amount / echo cost", "max amount / echo cost", "maximum / echo cost", "max / echo cost", "maximum / cost", "max / cost"):
                pair = re.split(r"\s*/\s*", value, maxsplit=1)
                if len(pair) == 2:
                    amount = re.search(r"\d+(?:\.\d+)?", pair[0])
                    cost = re.search(r"\d[\d,]*", pair[1])
                    if amount:
                        facts["max_amount"].append(amount.group(0))
                    if cost:
                        facts["echo_cost"].append(cost.group(0) + " Sorrow Echoes")
            elif key in ("damage", "speed", "range"):
                # A header row is not a fact row (e.g. Damage | Speed | Range).
                if value.lower() not in ("speed", "range", "speed / range", "pattern", "maximum / echo cost", "record", "value"):
                    facts[key].append(value)
            elif key in ("pattern", "attack pattern"):
                add_pattern_facts(facts, value)
            elif key in ("target coverage", "coverage"):
                facts["coverage"].append(value)
            elif key in ("falloff", "falloff rule"):
                facts["falloff"].append(value)
            elif key in ("max amount", "maximum amount", "maximum", "max"):
                facts["max_amount"].append(value)
            elif key in ("echo cost", "cost") and "echo" in value.lower():
                facts["echo_cost"].append(value)
            elif key in ("slot", "slot / chance"):
                facts["slot"].append(value)
                chance = re.search(r"(\d+(?:\.\d+)?)\s*%", value)
                if chance:
                    facts["chance"].append(chance.group(0))
            elif key in ("acquisition probability", "acquisition chance", "bestowal", "chance"):
                if "%" in value or re.search(r"\d", value):
                    facts["chance"].append(value)
            elif key in ("effect", "bonus", "stat effect", "source-work bonus", "source bonus", "set effect"):
                facts["effect"].append(value)

        # Horizontal weapon-stat table, e.g. Damage | Speed | Range | ...
        for i, cells in enumerate(table[:-1]):
            headers = [clean_cell(c).lower() for c in cells]
            if "damage" in headers and (("speed" in headers and "range" in headers) or "speed / range" in headers or "speed and range" in headers):
                vals = table[i + 1]
                if len(vals) != len(cells):
                    continue
                for header, value in zip(headers, vals):
                    value = clean_cell(value)
                    if header in ("damage", "speed", "range") and value:
                        facts[header].append(value)
                    elif header in ("speed / range", "speed and range") and value:
                        pair = re.split(r"\s*/\s*", value, maxsplit=1)
                        if len(pair) == 2:
                            facts["speed"].append(pair[0])
                            facts["range"].append(pair[1])
                    elif header in ("maximum / echo cost", "max / echo cost"):
                        pair = re.split(r"\s*/\s*", value, maxsplit=1)
                        if len(pair) == 2:
                            mmax = re.search(r"\d+(?:\.\d+)?", pair[0])
                            mcost = re.search(r"\d[\d,]*", pair[1])
                            if mmax:
                                facts["max_amount"].append(mmax.group(0))
                            if mcost:
                                facts["echo_cost"].append(mcost.group(0) + " Sorrow Echoes")
                    elif header in ("maximum amount", "max amount", "maximum", "max") and value:
                        facts["max_amount"].append(value)
                    elif "echo cost" in header and value:
                        cost = re.search(r"\d[\d,]*", value)
                        if cost:
                            facts["echo_cost"].append(cost.group(0) + " Sorrow Echoes")
                    elif header in ("pattern", "attack pattern") and value:
                        add_pattern_facts(facts, value)
                    elif header in ("falloff", "falloff rule") and value:
                        facts["falloff"].append(value)
                    elif header in ("target coverage", "coverage") and value:
                        facts["coverage"].append(value)

        # Suit resistance tables with one row per damage type.
        for i, cells in enumerate(table[:-1]):
            headers = [clean_cell(c).lower() for c in cells]
            if "element" in headers and ("multiplier" in headers or "resistance" in headers):
                ei = headers.index("element")
                ri = headers.index("multiplier") if "multiplier" in headers else headers.index("resistance")
                for row in table[i + 1 :]:
                    if len(row) <= max(ei, ri):
                        break
                    element = clean_cell(row[ei])
                    value = clean_cell(row[ri])
                    if element.lower() not in {x.lower() for x in ELEMENTS}:
                        break
                    if re.match(r"\d+(?:\.\d+)?", value):
                        facts["resistance"].append((element, re.match(r"\d+(?:\.\d+)?", value).group(0)))

        # Newer suit tables use the four elements as column headings.
        lower_headers = [clean_cell(c).lower() for c in table[0]] if table else []
        if all(el.lower() in lower_headers for el in ELEMENTS):
            row = next((r for r in table[1:] if len(r) >= len(lower_headers)), None)
            if row:
                for el in ELEMENTS:
                    index = lower_headers.index(el.lower())
                    val = clean_cell(row[index])
                    mval = re.match(r"(\d+(?:\.\d+)?)", val)
                    if mval:
                        facts["resistance"].append((el, mval.group(1)))
                for index, header in enumerate(lower_headers):
                    if header in ("maximum / echo cost", "max / echo cost"):
                        pair = re.split(r"\s*/\s*", clean_cell(row[index]), maxsplit=1)
                        if len(pair) == 2:
                            amount = re.search(r"\d+(?:\.\d+)?", pair[0])
                            cost = re.search(r"\d[\d,]*", pair[1])
                            if amount:
                                facts["max_amount"].append(amount.group(0))
                            if cost:
                                facts["echo_cost"].append(cost.group(0) + " Sorrow Echoes")

    # Explicit inline fields, including the compactly formatted weapon tables.
    for key, labels in {
        "grade": ("Grade",),
        "element": ("Element",),
        "damage": ("Damage",),
        "speed": ("Speed",),
        "range": ("Range",),
        "max_amount": ("Maximum Amount", "Max Amount"),
        "echo_cost": ("Echo Cost",),
        "pattern": ("Pattern", "Attack Pattern"),
        "coverage": ("Target Coverage", "Coverage"),
        "falloff": ("Falloff", "Falloff Rule"),
        "slot": ("Slot",),
        "chance": ("Acquisition Probability", "Acquisition Chance", "Bestowal"),
        "effect": ("Effect", "Bonus", "Source Bonus", "Source-Work Bonus", "Set Effect"),
    }.items():
        for value in value_after_label(text, labels):
            if key == "pattern":
                add_pattern_facts(facts, value)
            else:
                facts[key].append(value)

    # Compact four-resistance notation used in several codices.
    for m in re.finditer(
        r"(?:L/G/V/W|Lament\s*/\s*Grudge\s*/\s*Void\s*/\s*Weight)\s*[:;]?\s*"
        r"(\d+(?:\.\d+)?)\s*(?:\([^)]*\)\s*/\s*|/\s*)"
        r"(\d+(?:\.\d+)?)\s*(?:\([^)]*\)\s*/\s*|/\s*)"
        r"(\d+(?:\.\d+)?)\s*(?:\([^)]*\)\s*/\s*|/\s*)"
        r"(\d+(?:\.\d+)?)",
        text,
        re.I,
    ):
        for element, value in zip(ELEMENTS, m.groups()):
            facts["resistance"].append((element, value))

    return facts


def page_sections(text: str):
    """Yield Side Codex page title, its line number, and body text."""
    lines = text.splitlines()
    starts = [i for i, line in enumerate(lines) if re.match(r"^## PAGE\b", line)]
    for index, start in enumerate(starts):
        end = starts[index + 1] if index + 1 < len(starts) else len(lines)
        yield lines[start].strip(), start + 1, "\n".join(lines[start + 1 : end])


def compact_bullet_facts(line: str):
    """Parse one typed equipment record from a compact Side Codex bullet."""
    match = re.match(r"\s*-\s*\*\*(.+?)(?::)?\*\*\s*:?\s*(.+)$", line)
    if not match:
        return None
    name, record = match.groups()
    stat_record = record.split(". ", 1)[0]
    facts = defaultdict(list)
    facts["name"].append(name.strip())

    element_values = re.findall(
        r"\b(Lament|Grudge|Void|Weight)\s+(\d+(?:\.\d+)?)\b", stat_record, re.I
    )
    if len({element.lower() for element, _ in element_values}) == 4:
        kind = "Suit"
        facts["resistance"].extend((element.title(), value) for element, value in element_values)
    elif re.search(r"\bStigma\b", stat_record, re.I) or (
        re.search(r"\b(?:Head|Tail|Chest|Hand|Neck|Shoulder|Face|Ear|Eye)\b", stat_record, re.I)
        and re.search(r"\d+(?:\.\d+)?\s*%", stat_record)
        and re.search(r"\+\s*\d", stat_record)
    ):
        kind = "Stigma"
    else:
        kind = "Weapon"
        damage = re.search(
            r"\b(Lament|Grudge|Void|Weight|Mixed)\s+(\d+(?:\.\d+)?)\s*[–—-]\s*(\d+(?:\.\d+)?)",
            stat_record,
            re.I,
        )
        if damage:
            facts["damage"].append(f"{damage.group(1)} {damage.group(2)}–{damage.group(3)}")
        for field in ("speed", "range"):
            value = re.search(r"\b" + field + r"\s+([^;]+)", stat_record, re.I)
            if value:
                facts[field].append(value.group(1).strip())
        if re.search(r"\b(?:Skewer|Single|Cone|AoE|Area|Beam|Line|Burst|Sweep|Piercing)\b", stat_record, re.I):
            add_pattern_facts(facts, stat_record)
    maximum = re.search(r"(?:\b(\d+(?:\.\d+)?)\s+maximum\b|\bmaximum\s+(\d+(?:\.\d+)?))", stat_record, re.I)
    if maximum:
        facts["max_amount"].append(next(group for group in maximum.groups() if group))
    cost = re.search(r"(\d[\d,]*)\s*(?:Sorrow\s+)?Echoes?\b", stat_record, re.I)
    if cost:
        facts["echo_cost"].append(cost.group(1) + " Sorrow Echoes")
    if kind == "Stigma":
        slot = re.search(r"\b(Head|Tail|Chest|Hand|Neck|Shoulder|Face|Ear|Eye)\s+Stigma\b", stat_record, re.I)
        if not slot:
            slot = re.search(r"\bStigma\s+(Head|Tail|Chest|Hand|Neck|Shoulder|Face|Ear|Eye)\b", stat_record, re.I)
        if not slot:
            slot = re.search(r"\b(Head|Tail|Chest|Hand|Neck|Shoulder|Face|Ear|Eye)\b", stat_record, re.I)
        if slot:
            facts["slot"].append(slot.group(0))
        chance = re.search(r"\b(\d+(?:\.\d+)?)\s*%", stat_record)
        if chance:
            facts["chance"].append(chance.group(0))
        bonus = re.search(r"\+\s*\d+(?:\.\d+)?[^.;]*", stat_record)
        if bonus and re.search(r"\b(?:source|bonus|during)\b", bonus.group(0), re.I):
            facts["effect"].append(bonus.group(0).strip())
    return kind, facts


def parse_side_cards(text: str):
    """Extract typed M.A.W. facts from the recognized Side Codex card layouts."""
    cards = {}

    def add_card(kind, facts, name, line):
        if kind in cards:
            return
        if name:
            facts["name"].append(name.strip())
        cards[kind] = {"facts": facts, "line": line}

    sections = list(page_sections(text))
    # Full, one-page-per-equipment stat cards.
    for title, line, body in sections:
        upper = title.upper()
        kind = next((candidate for candidate in ("Weapon", "Suit", "Stigma") if candidate.upper() + " STAT CARD" in upper), None)
        if not kind:
            continue
        name_match = re.search(
            r"(?m)^###\s+M\.A\.W\.\s+(?:Weapon|Suit|Stigma|Protective Attire)\s*[—–-]\s*(.+)$",
            body,
        )
        add_card(kind, doc_facts(body, kind), name_match.group(1).strip() if name_match else None, line)

    # Compact cards represented by one table per equipment piece.
    for title, line, body in sections:
        if "COMPACT EQUIPMENT CARDS" not in title.upper():
            continue
        lines = body.splitlines()
        headers = [i for i, value in enumerate(lines) if re.match(r"^###\s+", value)]
        for index, start in enumerate(headers):
            end = headers[index + 1] if index + 1 < len(headers) else len(lines)
            name = re.sub(r"^###\s+", "", lines[start]).strip()
            facts = doc_facts("\n".join(lines[start + 1 : end]), "")
            if facts.get("resistance"):
                kind = "Suit"
            elif facts.get("slot") or facts.get("chance"):
                kind = "Stigma"
            elif facts.get("damage") or facts.get("speed"):
                kind = "Weapon"
            else:
                kind = ("Weapon", "Suit", "Stigma")[index] if index < 3 else None
            if kind:
                add_card(kind, facts, name, line + start + 1)

    # Compact one-line records, used in 36 Side Codices.
    for title, line, body in sections:
        if "COMPACT M.A.W. CARDS" not in title.upper() and "COMPACT CARDS" not in title.upper():
            continue
        for offset, bullet in enumerate(body.splitlines(), 1):
            parsed = compact_bullet_facts(bullet)
            if parsed:
                kind, facts = parsed
                add_card(kind, facts, None, line + offset)

    # Compact set-page tables that provide identity, grade, and element but no combat card.
    # Keep these identity-only records visible to name/grade/element comparison without
    # manufacturing damage, speed, range, pattern, coverage, or falloff values.
    for title, line, body in sections:
        if "M.A.W. SET PAGE" not in title.upper():
            continue
        for table_line, table in markdown_tables(body):
            headers = [clean_cell(cell).lower() for cell in table[0]]
            required = ("piece", "name", "grade", "element")
            if not all(header in headers for header in required):
                continue
            indexes = {header: headers.index(header) for header in required}
            kind_map = {
                "weapon": "Weapon",
                "suit": "Suit",
                "armor": "Suit",
                "armour": "Suit",
                "stigma": "Stigma",
                "gift": "Stigma",
            }
            for row_index, row in enumerate(table[1:], 1):
                if len(row) <= max(indexes.values()):
                    continue
                kind = kind_map.get(clean_cell(row[indexes["piece"]]).lower())
                name = clean_cell(row[indexes["name"]])
                if not kind or not name:
                    continue
                facts = defaultdict(list)
                grade = clean_cell(row[indexes["grade"]])
                element = clean_cell(row[indexes["element"]])
                if grade:
                    facts["grade"].append(grade)
                if element:
                    facts["element"].append(element)
                add_card(kind, facts, name, line + table_line + row_index)


    return cards


def primary_facts(block):
    name, start, numbered_lines = block
    text = "\n".join(line for _, line in numbered_lines)
    facts = defaultdict(list)
    facts["name"].append(name)

    for key, labels in {
        "grade": ("Grade",),
        "element": ("Element",),
        "damage": ("Damage",),
        "speed": ("Speed",),
        "range": ("Range",),
        "max_amount": ("Max Amount", "Maximum Amount"),
        "echo_cost": ("Cost", "Echo Cost"),
        "pattern": ("Pattern", "Attack Pattern"),
        "coverage": ("Target Coverage", "Coverage"),
        "falloff": ("Falloff", "Falloff Rule"),
        "slot": ("Slot",),
        "chance": ("Acquisition Probability",),
        "effect": ("Effect", "Bonus", "Source Bonus", "Source-Work Bonus"),
    }.items():
        for value in value_after_label(text, labels):
            if key == "pattern":
                add_pattern_facts(facts, value)
            else:
                facts[key].append(value)

    # Non-bold inline stat lines are common in older dossiers.
    for key in ("damage", "speed", "range", "max_amount", "pattern", "coverage", "falloff", "slot", "chance", "effect"):
        labels = {
            "max_amount": r"(?:Max(?:imum)? Amount)",
            "pattern": r"(?:Attack )?Pattern",
            "coverage": r"(?:Target )?Coverage",
            "falloff": r"Falloff(?: Rule)?",
            "chance": r"Acquisition Probability",
        }.get(key, re.escape(key.replace("_", " ")))
        for m in re.finditer(r"(?im)^\s*" + labels + r"\s*:\s*([^\n]+)", text):
            if key == "pattern":
                add_pattern_facts(facts, m.group(1))
            else:
                facts[key].append(m.group(1).strip())

    for m in re.finditer(r"\b(Lament|Grudge|Void|Weight)\s*:\s*(\d+(?:\.\d+)?)", text, re.I):
        facts["resistance"].append((m.group(1), m.group(2)))
    for _, table in markdown_tables(text):
        for row in table:
            if len(row) >= 2 and row[0].strip().lower() in {x.lower() for x in ELEMENTS}:
                val = re.match(r"(\d+(?:\.\d+)?)", row[1].strip())
                if val:
                    facts["resistance"].append((row[0].strip(), val.group(1)))

    # Echo charge is distinct from the bearer's narrative cost.
    all_text = text
    for m in re.finditer(r"(\d[\d,]*)\s*Sorrow\s+Echoes", all_text, re.I):
        facts["echo_cost"].append(m.group(1) + " Sorrow Echoes")
    return facts


def normalize_scalar(key: str, value):
    if isinstance(value, tuple):
        key_name, raw = value
        if key == "resistance":
            try:
                return key_name.lower(), float(raw)
            except ValueError:
                return None
    value = clean_cell(str(value))
    if key == "grade":
        m = re.search(r"[αβγδω]", value)
        return m.group(0) if m else None
    if key == "element":
        for element in ELEMENTS:
            if re.search(r"\b" + element + r"\b", value, re.I):
                return element.lower()
        if re.search(r"\bMixed\b", value, re.I):
            return "mixed"
        return None
    if key == "damage":
        m = re.search(r"\b(Lament|Grudge|Void|Weight|Mixed)\b[^\d]*(\d+(?:\.\d+)?)\s*[–—-]\s*(\d+(?:\.\d+)?)", value, re.I)
        if m:
            return (m.group(1).lower(), float(m.group(2)), float(m.group(3)))
        nums = re.findall(r"\d+(?:\.\d+)?", value)
        return (None, float(nums[0]), float(nums[1])) if len(nums) >= 2 else None
    if key in ("speed", "range"):
        number = re.search(r"\d+(?:\.\d+)?", value)
        if not number:
            return None
        labels = {
            "speed": ("very fast", "instant", "fast", "normal", "slow", "measured", "steady", "rapid"),
            "range": ("close", "short", "medium", "long", "room", "global", "melee", "touch", "extended"),
        }[key]
        label = next((item for item in labels if re.search(r"\b" + re.escape(item) + r"\b", value, re.I)), None)
        return float(number.group(0)), label
    if key == "pattern":
        lowered = value.lower()
        for label in ("skewer", "single", "cone", "aoe", "area of effect", "area", "beam", "line", "burst", "sweep", "piercing"):
            if re.search(r"\b" + re.escape(label) + r"\b", lowered):
                return "aoe" if label == "area of effect" else label
        return re.sub(r"[^a-z0-9]+", " ", lowered).strip() or None
    if key == "coverage":
        m = re.search(r"\b(?:up to\s*)?(\d+(?:\.\d+)?)\s+(?:designated\s+)?targets?\b", value, re.I)
        if m:
            return float(m.group(1))
        if re.search(r"\b(?:single|one)(?:\s+designated)?\s+target\b", value, re.I):
            return 1.0
        if re.search(r"\ball\s+(?:grounded\s+)?targets?\b", value, re.I):
            return "all"
        return None
    if key == "falloff":
        percentages = re.findall(r"(\d+(?:\.\d+)?)\s*%", value)
        return tuple(float(number) for number in percentages) if len(percentages) >= 2 else None
    if key == "max_amount":
        m = re.search(r"\d+(?:\.\d+)?", value)
        return float(m.group(0)) if m else None
    if key == "echo_cost":
        m = re.search(r"(\d[\d,]*)\s*Sorrow\s+Echoes", value, re.I)
        if m:
            return int(m.group(1).replace(",", ""))
        nums = re.findall(r"\d[\d,]*", value)
        if "Sorrow Echoes" in value and nums:
            return int(nums[-1].replace(",", ""))
        return None
    if key == "chance":
        m = re.search(r"(\d+(?:\.\d+)?)\s*%", value)
        return float(m.group(1)) if m else None
    if key == "effect":
        numbers = sorted({float(number) for number in re.findall(r"\+\s*(\d+(?:\.\d+)?)", value)})
        return tuple(numbers) if numbers else None
    if key == "slot":
        value = re.split(r"\*\*|\|", value)[0].strip().lower()
        # Some registry-form Codices put the bestowal chance in the same cell
        # (e.g. “Tail · 4%”); it is not part of the body slot. Compare the
        # location family, treating Head/Eye and Head as compatible specificity.
        value = re.split(r"[·;]", value, maxsplit=1)[0].strip()
        value = re.sub(r"\s*/\s*\d+(?:\.\d+)?\s*%.*$", "", value)
        value = value.split("/", 1)[0].strip().rstrip(" ,;·-")
        value = re.sub(r"\s+", " ", value)
        # Eye, brow, face, and ear are sublocations of the Head family; the
        # order of “Eye / Head” versus “Head / Right Eye” is not a slot change.
        for family, terms in {
            "head": ("head", "eye", "face", "brow", "ear"),
            "neck": ("neck", "throat", "choker", "collar"),
            "chest": ("chest", "brooch", "breast"),
            "hand": ("hand", "knuckle", "finger"),
            "shoulder": ("shoulder",),
            "tail": ("tail",),
        }.items():
            if any(re.search(r"\b" + re.escape(term) + r"\b", value) for term in terms):
                return family
        return value or None
    return value.lower() or None


def equivalent_values(field: str, left, right) -> bool:
    """Compare parsed values while accounting for redundant omitted labels.

    Weapon element is also checked as its own explicit M.A.W. field. Older
    item Codices often record a bare damage range while the primary dossier
    prefixes that same range with the element, so the damage comparison must
    not treat the redundant label as a different range. Likewise, a missing
    speed/range descriptor does not contradict an otherwise matching numeric
    band; when both records give a descriptor, it must agree.
    """
    if field == "damage":
        if not (isinstance(left, tuple) and isinstance(right, tuple) and len(left) == len(right) == 3):
            return left == right
        left_element, left_min, left_max = left
        right_element, right_min, right_max = right
        return (left_min, left_max) == (right_min, right_max) and (
            left_element is None or right_element is None or left_element == right_element
        )
    if field in ("speed", "range"):
        if not (isinstance(left, tuple) and isinstance(right, tuple) and len(left) == len(right) == 2):
            return left == right
        left_number, left_label = left
        right_number, right_label = right
        return left_number == right_number and (
            left_label is None or right_label is None or left_label == right_label
        )
    return left == right


def compare_values(category: str, field: str, source_values, embedded_values, path: str, line: int):
    """Return a mismatch only when the Codex has an explicit value to compare."""
    source_norm = {normalize_scalar(field, v) for v in source_values}
    source_norm.discard(None)
    if not source_norm:
        return None
    embedded_norm = [(v, normalize_scalar(field, v)) for v in embedded_values]
    embedded_norm = [(raw, norm) for raw, norm in embedded_norm if norm is not None]
    if not embedded_norm:
        return {
            "category": category,
            "field": field,
            "primary": "(not stated)",
            "codex": ", ".join(map(str, sorted(source_norm, key=str))),
            "path": path,
            "line": line,
            "status": "missing",
        }
    bad = [
        raw
        for raw, norm in embedded_norm
        if not any(equivalent_values(field, norm, source) for source in source_norm)
    ]
    if bad:
        return {
            "category": category,
            "field": field,
            "primary": "; ".join(map(str, bad)),
            "codex": ", ".join(map(str, sorted(source_norm, key=str))),
            "path": path,
            "line": line,
            "status": "conflict",
        }
    return None


def load_data():
    rows = list(csv.DictReader(REGISTRY.open(encoding="utf-8", newline="")))
    groups = defaultdict(list)
    for row in rows:
        groups[row["Linked_Entity_ID"]].append(row)

    primary_by_code = {}
    for path in sorted(WORLD.glob("*/SE-*.md")):
        text = read(path)
        code = designation_from_primary(text)
        if code:
            primary_by_code[code] = (path, text)

    reports = []
    summary = Counter()
    complete_pairs = 0
    complete_sets = 0
    for entity_id, group in sorted(groups.items()):
        side = next((r for r in group if r["Equipment_Type"] == "Side-Codex"), None)
        if not side:
            continue
        side_text = read(ROOT / side["File_Path"])
        code = designation_from_side(side_text)
        completion = re.search(r"Codex Set Completion:\*\*\s*`?([^`\s]+)", side_text)
        status = completion.group(1) if completion else "unmarked"
        primary = primary_by_code.get(code) if code else None
        if not primary:
            summary["unmapped_side_codex"] += 1
            continue
        primary_path, primary_text = primary
        blocks = parse_primary_blocks(primary_text)
        if status != "4/4":
            summary["exception_sets"] += 1
            continue
        complete_sets += 1
        side_cards = parse_side_cards(side_text)
        if side_cards:
            summary["side_card_sets"] += 1
            summary["side_card_records"] += len(side_cards)
        side_file = ROOT / side["File_Path"]
        for kind in TYPE_TO_ROW:
            item = next((r for r in group if r["Equipment_Type"] == TYPE_TO_ROW[kind]), None)
            if not item:
                reports.append({"category": "inventory", "field": kind, "primary": "(no item record)", "codex": "expected item record", "path": str(primary_path.relative_to(ROOT)), "line": 1, "status": "missing"})
                continue
            item_path = ROOT / item["File_Path"]
            codex_text = read(item_path)
            codex_f = doc_facts(codex_text, kind)
            block = next(iter(blocks.get(kind, [])), None)
            if not block:
                reports.append({"category": "inventory", "field": kind, "primary": "(no embedded block)", "codex": heading_name(codex_text) or "item record present", "path": str(primary_path.relative_to(ROOT)), "line": 1, "status": "missing"})
                continue
            name, start, numbered = block
            embedded_f = primary_facts(block)
            complete_pairs += 1
            summary["complete_item_pairs"] += 1

            codex_name = (codex_f.get("name") or [heading_name(codex_text) or ""])[0]
            side_card = side_cards.get(kind)
            if side_card:
                summary["side_card_pairs"] += 1
                side_f = side_card["facts"]
                side_line = side_card["line"]
                side_name = (side_f.get("name") or [""])[0]
                side_path = str(side_file.relative_to(ROOT))
                if side_name and normalize_name(name) != normalize_name(side_name):
                    reports.append({"category": "side", "field": kind.lower() + ".name", "primary": name, "codex": side_name, "path": side_path, "line": side_line, "status": "candidate", "primary_label": "Primary SE", "codex_label": "Side Codex"})
                if side_name and codex_name and normalize_name(codex_name) != normalize_name(side_name):
                    reports.append({"category": "side_internal", "field": kind.lower() + ".name", "primary": side_name, "codex": codex_name, "path": side_path, "line": side_line, "status": "candidate", "primary_label": "Side Codex", "codex_label": "Item Codex"})

                side_fields = {
                    "Weapon": ("grade", "element", "damage", "speed", "range", "max_amount", "echo_cost", "pattern", "coverage", "falloff"),
                    "Suit": ("grade", "element", "resistance", "max_amount", "echo_cost"),
                    "Stigma": ("grade", "element", "slot", "chance", "effect", "max_amount", "echo_cost"),
                }[kind]
                for field in side_fields:
                    mismatch = compare_values("side", field, side_f.get(field, []), embedded_f.get(field, []), side_path, side_line)
                    if mismatch:
                        mismatch["field"] = kind.lower() + "." + field
                        mismatch["primary_label"] = "Primary SE"
                        mismatch["codex_label"] = "Side Codex"
                        reports.append(mismatch)
                    if side_f.get(field) and codex_f.get(field):
                        mismatch = compare_values("side_internal", field, codex_f.get(field, []), side_f.get(field, []), side_path, side_line)
                        if mismatch:
                            mismatch["field"] = kind.lower() + "." + field
                            mismatch["primary_label"] = "Side Codex"
                            mismatch["codex_label"] = "Item Codex"
                            reports.append(mismatch)

            if normalize_name(name) != normalize_name(codex_name):
                reports.append({"category": "name", "field": kind, "primary": name, "codex": codex_name, "path": str(primary_path.relative_to(ROOT)), "line": start, "status": "candidate"})

            for field in ("grade", "element"):
                mismatch = compare_values(kind.lower(), field, codex_f.get(field, []), embedded_f.get(field, []), str(primary_path.relative_to(ROOT)), start)
                if mismatch:
                    reports.append(mismatch)

            fields = {
                "Weapon": ("damage", "speed", "range", "max_amount", "echo_cost", "pattern", "coverage", "falloff"),
                "Suit": ("resistance", "max_amount", "echo_cost"),
                "Stigma": ("slot", "chance", "effect"),
            }[kind]
            for field in fields:
                # Do not compare effect prose; only a matching explicit numeric bonus is comparable.
                if field == "effect" and not codex_f.get(field):
                    continue
                mismatch = compare_values(kind.lower(), field, codex_f.get(field, []), embedded_f.get(field, []), str(primary_path.relative_to(ROOT)), start)
                if mismatch:
                    reports.append(mismatch)

    summary["complete_sets"] = complete_sets
    summary["complete_item_pairs"] = complete_pairs
    summary["mapped_primary_dossiers"] = len(primary_by_code)
    summary["registry_side_codices"] = sum(1 for g in groups.values() if any(r["Equipment_Type"] == "Side-Codex" for r in g))
    return summary, reports


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", choices=("all", "inventory", "name", "grade", "element", "weapon", "suit", "stigma", "side", "side-internal"), default="all")
    parser.add_argument("--limit", type=int, default=200, help="Maximum mismatch rows to print (default: 200; use 0 for all)")
    args = parser.parse_args()

    summary, reports = load_data()
    print("M.A.W. Codex comparison (candidate differences; not an auto-fixer)")
    print(f"  mapped primary dossiers : {summary['mapped_primary_dossiers']}")
    print(f"  external Side Codices   : {summary['registry_side_codices']}")
    print(f"  complete 4/4 sets       : {summary['complete_sets']}")
    print(f"  item pairs compared     : {summary['complete_item_pairs']}")
    print(f"  Side Codex card sets    : {summary['side_card_sets']}")
    print(f"  Side card records       : {summary['side_card_records']}")
    print(f"  Side card/SE pairs      : {summary['side_card_pairs']}")
    print(f"  exception sets skipped  : {summary['exception_sets']}")

    counts = Counter(r["category"] if r["category"] in ("name", "inventory", "grade", "element") else r["category"] + "." + r["field"] for r in reports)
    print("\nFindings by class:")
    if not counts:
        print("  none")
    else:
        for key, n in sorted(counts.items()):
            print(f"  {key:24s} {n}")

    if args.check == "all":
        selected = reports
    elif args.check in ("inventory", "name", "grade", "element"):
        selected = [r for r in reports if r["category"] == args.check]
    elif args.check == "side":
        selected = [r for r in reports if r["category"] == "side"]
    elif args.check == "side-internal":
        selected = [r for r in reports if r["category"] == "side_internal"]
    elif args.check == "weapon":
        selected = [r for r in reports if r["category"] == "weapon"]
    elif args.check == "suit":
        selected = [r for r in reports if r["category"] == "suit"]
    else:
        selected = [r for r in reports if r["category"] == "stigma"]

    if selected:
        print(f"\nDetails ({len(selected)} candidate finding(s)):")
        limit = args.limit if args.limit > 0 else len(selected)
        for row in selected[:limit]:
            left_label = row.get("primary_label", "SE")
            right_label = row.get("codex_label", "Codex")
            print(f"  {row['status']:8s} {row['path']}:{row['line']} — {row['field']}: {left_label}={row['primary']} | {right_label}={row['codex']}")
        if len(selected) > limit:
            print(f"  ... {len(selected) - limit} more; raise --limit or use --limit 0")


if __name__ == "__main__":
    main()
