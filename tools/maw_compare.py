#!/usr/bin/env python3
"""Compare SE-dossier M.A.W. blocks with their own completed M.A.W. Codex set.

This is a conservative review aid, not an auto-fixer.  It maps on the dossier's
SECC Designation (never the filename), uses the Side Codex to identify the set,
and compares each embedded Weapon/Suit/Stigma block with its matching individual
Codex.  Reports are candidates for human triage: names can be aliases, and a
Codex may not explicitly record every field present in an SE dossier.

Run from the repository root:
    python3 tools/maw_compare.py
    python3 tools/maw_compare.py --check suit --limit 200
    python3 tools/maw_compare.py --check weapon --limit 50
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
            elif key in ("damage", "speed", "range"):
                # A header row is not a fact row (e.g. Damage | Speed | Range).
                if value.lower() not in ("speed", "range", "pattern", "record", "value"):
                    facts[key].append(value)
            elif key in ("max amount", "maximum amount"):
                facts["max_amount"].append(value)
            elif key in ("echo cost", "cost") and "echo" in value.lower():
                facts["echo_cost"].append(value)
            elif key in ("slot", "slot / chance"):
                facts["slot"].append(value)
                chance = re.search(r"(\d+(?:\.\d+)?)\s*%", value)
                if chance:
                    facts["chance"].append(chance.group(0))
            elif key in ("acquisition probability", "bestowal", "chance"):
                if "%" in value or re.search(r"\d", value):
                    facts["chance"].append(value)
            elif key in ("effect", "bonus", "stat effect", "source-work bonus"):
                facts["effect"].append(value)

        # Horizontal weapon-stat table, e.g. Damage | Speed | Range | ...
        for i, cells in enumerate(table[:-1]):
            headers = [clean_cell(c).lower() for c in cells]
            if "damage" in headers and "speed" in headers and "range" in headers:
                vals = table[i + 1]
                if len(vals) != len(cells):
                    continue
                for header, value in zip(headers, vals):
                    value = clean_cell(value)
                    if header in ("damage", "speed", "range") and value:
                        facts[header].append(value)
                    elif header in ("maximum / echo cost", "max / echo cost"):
                        mmax = re.search(r"(\d+)\s*/", value)
                        mcost = re.search(r"/(?:\s*)(\d+)\s*Sorrow\s+Echoes", value, re.I)
                        if mmax:
                            facts["max_amount"].append(mmax.group(1))
                        if mcost:
                            facts["echo_cost"].append(mcost.group(1) + " Sorrow Echoes")
                    elif header in ("maximum amount", "max amount") and value:
                        facts["max_amount"].append(value)
                    elif "echo cost" in header and value:
                        facts["echo_cost"].append(value)

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

    # Explicit inline fields, including the compactly formatted weapon tables.
    for key, labels in {
        "grade": ("Grade",),
        "element": ("Element",),
        "damage": ("Damage",),
        "speed": ("Speed",),
        "range": ("Range",),
        "max_amount": ("Maximum Amount", "Max Amount"),
        "echo_cost": ("Echo Cost",),
        "slot": ("Slot",),
        "chance": ("Acquisition Probability", "Bestowal"),
        "effect": ("Effect", "Bonus"),
    }.items():
        for value in value_after_label(text, labels):
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
        "slot": ("Slot",),
        "chance": ("Acquisition Probability",),
        "effect": ("Effect",),
    }.items():
        for value in value_after_label(text, labels):
            facts[key].append(value)

    # Non-bold inline stat lines are common in older dossiers.
    for key in ("damage", "speed", "range", "max_amount", "slot", "chance", "effect"):
        labels = {
            "max_amount": r"(?:Max(?:imum)? Amount)",
            "chance": r"Acquisition Probability",
        }.get(key, re.escape(key.replace("_", " ")))
        for m in re.finditer(r"(?im)^\s*" + labels + r"\s*:\s*([^\n]+)", text):
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
        m = re.search(r"\b(Lament|Grudge|Void|Weight)\b[^\d]*(\d+(?:\.\d+)?)\s*[–—-]\s*(\d+(?:\.\d+)?)", value, re.I)
        if m:
            return (m.group(1).lower(), float(m.group(2)), float(m.group(3)))
        nums = re.findall(r"\d+(?:\.\d+)?", value)
        return tuple(float(n) for n in nums[:2]) if nums else None
    if key in ("speed", "range", "max_amount"):
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
    bad = [raw for raw, norm in embedded_norm if norm not in source_norm]
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
            if normalize_name(name) != normalize_name(codex_name):
                reports.append({"category": "name", "field": kind, "primary": name, "codex": codex_name, "path": str(primary_path.relative_to(ROOT)), "line": start, "status": "candidate"})

            for field in ("grade", "element"):
                mismatch = compare_values(kind.lower(), field, codex_f.get(field, []), embedded_f.get(field, []), str(primary_path.relative_to(ROOT)), start)
                if mismatch:
                    reports.append(mismatch)

            fields = {
                "Weapon": ("damage", "speed", "range", "max_amount", "echo_cost"),
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
    parser.add_argument("--check", choices=("all", "inventory", "name", "grade", "element", "weapon", "suit", "stigma"), default="all")
    parser.add_argument("--limit", type=int, default=200, help="Maximum mismatch rows to print (default: 200; use 0 for all)")
    args = parser.parse_args()

    summary, reports = load_data()
    print("M.A.W. Codex comparison (candidate differences; not an auto-fixer)")
    print(f"  mapped primary dossiers : {summary['mapped_primary_dossiers']}")
    print(f"  external Side Codices   : {summary['registry_side_codices']}")
    print(f"  complete 4/4 sets       : {summary['complete_sets']}")
    print(f"  item pairs compared     : {summary['complete_item_pairs']}")
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
            print(f"  {row['status']:8s} {row['path']}:{row['line']} — {row['field']}: SE={row['primary']} | Codex={row['codex']}")
        if len(selected) > limit:
            print(f"  ... {len(selected) - limit} more; raise --limit or use --limit 0")


if __name__ == "__main__":
    main()
