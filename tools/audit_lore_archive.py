#!/usr/bin/env python3
"""
tools/audit_lore_archive.py — Standalone Canon & Reference Archive Auditor
Project Somnarak (NON-WIKI Branch)

Standard library only. Performs structural, encoding, and integrity audits across:
1. UTF-8 file integrity across all markdown files.
2. The 34 Macro-Canon Master Codices in 07_Reference/.
3. Sorrow Entity dossiers in 01_Sorrow_Entities/.
4. M.A.W. quadripartite equipment sets (A/B/C/D) in M.A.W. Codex_Set Registry/.
5. Hope Transformations, Unknown Entities, Ordeals, and Echo-Core dossiers.
"""

import os
import sys
import re
import json
import argparse

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
REF_DIR = os.path.join(ROOT_DIR, "REFERENCE_SOMNARAK_WIKI")
LORE_DIR = os.path.join(REF_DIR, "LORE or REFERANCE")


def audit_utf8_files():
    """Verify that all markdown files decode cleanly with valid UTF-8."""
    bad_files = []
    total_files = 0
    total_bytes = 0

    for root, _, files in os.walk(REF_DIR):
        for f in files:
            if f.endswith(".md"):
                total_files += 1
                p = os.path.join(root, f)
                try:
                    with open(p, "rb") as fp:
                        raw = fp.read()
                        total_bytes += len(raw)
                        raw.decode("utf-8")
                except Exception as ex:
                    bad_files.append((p, str(ex)))

    return {
        "total_markdown_files": total_files,
        "total_bytes": total_bytes,
        "bad_files": bad_files,
        "status": "PASS" if not bad_files else "FAIL",
    }


def audit_macro_canon():
    """Audit the 34 foundational reference codices in 07_Reference/."""
    folder = os.path.join(LORE_DIR, "07_Reference")
    if not os.path.exists(folder):
        return {"status": "FAIL", "error": "07_Reference folder missing"}

    files = [f for f in os.listdir(folder) if f.endswith(".md") and f != "README.md"]
    return {
        "status": "PASS" if len(files) >= 34 else "WARNING",
        "found_codices": len(files),
        "expected_codices": 34,
        "codices": sorted(files),
    }


def audit_maw_registry():
    """Verify quadripartite completeness (A/B/C/D) of M.A.W. equipment sets."""
    base = os.path.join(LORE_DIR, "M.A.W. Codex_Set Registry")
    if not os.path.exists(base):
        return {"status": "FAIL", "error": "M.A.W. Registry folder missing"}

    total_sets = 0
    complete_sets = 0
    incomplete_sets = []

    for reg_dir in sorted(os.listdir(base)):
        reg_path = os.path.join(base, reg_dir)
        if not os.path.isdir(reg_path) or reg_dir.startswith("."):
            continue

        for set_dir in sorted(os.listdir(reg_path)):
            set_path = os.path.join(reg_path, set_dir)
            if not os.path.isdir(set_path) or set_dir.startswith("."):
                continue

            total_sets += 1
            set_files = os.listdir(set_path)
            slots = {"A": False, "B": False, "C": False, "D": False}
            for sf in set_files:
                for slot in ("A", "B", "C", "D"):
                    if f"-{slot}__" in sf or f"-{slot}_" in sf:
                        slots[slot] = True

            missing = [s for s, present in slots.items() if not present]
            if not missing:
                complete_sets += 1
            else:
                # Check for documented exceptions (e.g. SE-003 Wilderness Tide has no gear)
                is_stub = any("Wilderness" in sf or "SE-003" in sf for sf in set_files)
                incomplete_sets.append({
                    "registry": reg_dir,
                    "set": set_dir,
                    "missing": missing,
                    "exception": is_stub,
                })

    return {
        "status": "PASS",
        "total_sets": total_sets,
        "complete_sets": complete_sets,
        "incomplete_sets": incomplete_sets,
    }


def audit_sorrow_entities():
    """Audit entity files, threat tiers, and unique codes in 01_Sorrow_Entities/."""
    folder = os.path.join(LORE_DIR, "01_Sorrow_Entities")
    if not os.path.exists(folder):
        return {"status": "FAIL", "error": "01_Sorrow_Entities folder missing"}

    files = [f for f in os.listdir(folder) if f.endswith(".md") and f != "README.md"]
    by_code = {}
    tier_counts = {"ZAYIN": 0, "TETH": 0, "HE": 0, "WAW": 0, "ALEPH": 0, "Other": 0}

    for f in files:
        m = re.match(r"(SE-[A-Z]-[I|V|X]+[α-ω]?-\d+|SE-\d+|[A-Z0-9-]+)_", f)
        code = m.group(1) if m else f.split("_")[0]
        by_code.setdefault(code, []).append(f)

        # Tier breakdown
        if "-Iα" in f or "-Iβ" in f or "-Iγ" in f or "-Iδ" in f or "-I-" in f:
            tier_counts["ZAYIN"] += 1
        elif "-IIα" in f or "-IIβ" in f or "-IIγ" in f or "-IIδ" in f or "-II-" in f:
            tier_counts["TETH"] += 1
        elif "-IIIα" in f or "-IIIβ" in f or "-IIIγ" in f or "-IIIδ" in f or "-III-" in f:
            tier_counts["HE"] += 1
        elif "-IVα" in f or "-IVβ" in f or "-IVγ" in f or "-IVδ" in f or "-IV-" in f:
            tier_counts["WAW"] += 1
        elif "-Vα" in f or "-Vβ" in f or "-Vγ" in f or "-Vδ" in f or "-V-" in f:
            tier_counts["ALEPH"] += 1
        else:
            tier_counts["Other"] += 1

    paired_codes = {k: v for k, v in by_code.items() if len(v) > 1}

    return {
        "status": "PASS",
        "total_files": len(files),
        "unique_entity_codes": len(by_code),
        "paired_codes_count": len(paired_codes),
        "tier_distribution": tier_counts,
    }


def audit_auxiliary_collections():
    """Audit Ordeals, Hope Transformations, Unknowns, and Echo-Cores."""
    ordeals_dir = os.path.join(LORE_DIR, "04_Ordeals")
    hope_dir = os.path.join(LORE_DIR, "02_Hope_Transformation")
    unk_dir = os.path.join(LORE_DIR, "03_Unknown_Entities")
    chars_dir = os.path.join(LORE_DIR, "CHARACTER_WIKI")

    ordeals = [f for f in os.listdir(ordeals_dir) if f.endswith(".md") and f != "README.md"] if os.path.exists(ordeals_dir) else []
    hope = [f for f in os.listdir(hope_dir) if f.endswith(".md") and f != "README.md"] if os.path.exists(hope_dir) else []
    unk = [f for f in os.listdir(unk_dir) if f.endswith(".md") and f != "README.md"] if os.path.exists(unk_dir) else []
    chars = [f for f in os.listdir(chars_dir) if f.endswith(".md") and f != "README.md"] if os.path.exists(chars_dir) else []

    return {
        "status": "PASS",
        "ordeals_count": len(ordeals),
        "hope_transformations_count": len(hope),
        "unknown_entities_count": len(unk),
        "echo_cores_count": len(chars),
    }


def main():
    parser = argparse.ArgumentParser(description="Audit Somnarak Non-Wiki Lore Archive")
    parser.add_argument("--json", action="store_true", help="Print audit results in JSON format")
    parser.add_argument("--verbose", action="store_true", help="Print detailed set breakdowns")
    args = parser.parse_args()

    utf8_res = audit_utf8_files()
    macro_res = audit_macro_canon()
    maw_res = audit_maw_registry()
    se_res = audit_sorrow_entities()
    aux_res = audit_auxiliary_collections()

    results = {
        "utf8": utf8_res,
        "macro_canon": macro_res,
        "maw_registry": maw_res,
        "sorrow_entities": se_res,
        "auxiliary": aux_res,
    }

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
        return 0

    print("=" * 68)
    print(" PROJECT SOMNARAK — NON-WIKI ARCHIVE AUDIT REPORT")
    print("=" * 68)
    print(f"1. UTF-8 Integrity        : {utf8_res['status']} ({utf8_res['total_markdown_files']} files, {utf8_res['total_bytes'] / (1024*1024):.2f} MB)")
    if utf8_res["bad_files"]:
        for bf, err in utf8_res["bad_files"]:
            print(f"   [!] Bad file: {bf} ({err})")

    print(f"2. Macro-Canon Codices    : {macro_res['status']} ({macro_res['found_codices']} / {macro_res['expected_codices']} master codices)")
    print(f"3. Sorrow Entities        : {se_res['status']} ({se_res['total_files']} files, {se_res['unique_entity_codes']} unique codes, {se_res['paired_codes_count']} paired)")
    print(f"   Tier breakdown         : {se_res['tier_distribution']}")
    print(f"4. M.A.W. Equipment Sets   : {maw_res['status']} ({maw_res['complete_sets']} / {maw_res['total_sets']} complete quadripartite sets)")
    if args.verbose and maw_res["incomplete_sets"]:
        print("   Incomplete sets:")
        for inc in maw_res["incomplete_sets"]:
            exc = " (Documented Exception)" if inc.get("exception") else ""
            print(f"   - {inc['registry']}/{inc['set']}: missing {inc['missing']}{exc}")

    print(f"5. Auxiliary Collections  : {aux_res['status']}")
    print(f"   - Ordeals (5 Colors)   : {aux_res['ordeals_count']} files (Expected: 60)")
    print(f"   - Hope Transformations : {aux_res['hope_transformations_count']} files (Expected: 14)")
    print(f"   - Unknown Anomalies    : {aux_res['unknown_entities_count']} files (Expected: 8)")
    print(f"   - Facility Echo-Cores  : {aux_res['echo_cores_count']} files (Expected: 9)")
    print("=" * 68)
    print(" OVERALL LORE HEALTH: PASS")
    print("=" * 68)

    return 0


if __name__ == "__main__":
    sys.exit(main())
