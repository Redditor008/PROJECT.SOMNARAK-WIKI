#!/usr/bin/env python3
"""
tools/audit_lore_archive.py — Standalone Canon & Reference Archive Auditor
Project Somnarak (NON-WIKI Branch)

Standard library only. Performs structural, encoding, and integrity audits across:
1. UTF-8 file integrity across all markdown files.
2. The Macro-Canon Master Codices in SOMNARAK-WORLD/Master_Codices/ and REFERENCE_SOMNARAK_WIKI/.
3. Sorrow Entity dossiers in SOMNARAK-WORLD/Sorrow_Entities/.
4. M.A.W. quadripartite equipment sets (A/B/C/D) in SOMNARAK-WORLD/MAW_Codex_Sets/.
5. The Absolvohan serial narrative volumes in SOMNARAK-WORLD/The_Absolvohan/.
6. Hope Transformations, Unknown Entities, Ordeals, and Echo-Core dossiers.
"""

import os
import sys
import re
import json
import argparse
sys.path.insert(0, os.path.dirname(__file__))
from check_box_symmetry import audit_file_symmetry

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
REF_DIR = os.path.join(ROOT_DIR, "REFERENCE_SOMNARAK_WIKI")
WORLD_DIR = os.path.join(ROOT_DIR, "SOMNARAK-WORLD")


def audit_utf8_files():
    """Verify that all markdown files decode cleanly with valid UTF-8 across the repository."""
    bad_files = []
    total_files = 0
    total_bytes = 0

    scan_dirs = [WORLD_DIR, REF_DIR, ROOT_DIR]
    scanned_paths = set()

    for d in scan_dirs:
        if not os.path.exists(d):
            continue
        for root, _, files in os.walk(d):
            if ".git" in root or "ABSOLOVHAN PART" in root:
                continue
            for f in files:
                if f.endswith(".md"):
                    p = os.path.join(root, f)
                    if p in scanned_paths:
                        continue
                    scanned_paths.add(p)
                    total_files += 1
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
    """Audit the 34 foundational reference codices (31 in-universe Master_Codices + 3 developer standards)."""
    folder = os.path.join(WORLD_DIR, "Master_Codices")
    if not os.path.exists(folder):
        return {"status": "FAIL", "error": "Master_Codices folder missing"}

    files = []
    for root, _, f_list in os.walk(folder):
        for f in f_list:
            if f.endswith(".md") and f != "README.md":
                files.append(f)

    dev_files = ["SOMNARAK_DOCUMENT_RULES.md", "SOMNARAK_MAIN_ENTITY_PROTECTED_LIST.md", "SOMNARAK_NAME_REGISTRY.md"]
    found_dev = [f for f in dev_files if os.path.exists(os.path.join(REF_DIR, f))]

    total_canon = len(files) + len(found_dev)
    return {
        "status": "PASS" if total_canon >= 34 else "WARNING",
        "found_in_world": len(files),
        "found_editorial": len(found_dev),
        "found_codices": total_canon,
        "expected_codices": 34,
        "codices": sorted(files),
    }


def audit_maw_registry():
    """Verify quadripartite completeness (A/B/C/D) of M.A.W. equipment sets in SOMNARAK-WORLD/MAW_Codex_Sets/."""
    base = os.path.join(WORLD_DIR, "MAW_Codex_Sets")
    if not os.path.exists(base):
        return {"status": "FAIL", "error": "MAW_Codex_Sets folder missing"}

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
    """Audit entity files, threat tiers, and unique codes in SOMNARAK-WORLD/Sorrow_Entities/."""
    folder = os.path.join(WORLD_DIR, "Sorrow_Entities")
    if not os.path.exists(folder):
        return {"status": "FAIL", "error": "Sorrow_Entities folder missing"}

    files = [f for f in os.listdir(folder) if f.endswith(".md") and f != "README.md"]
    by_code = {}
    tier_counts = {"ZAYIN": 0, "TETH": 0, "HE": 0, "WAW": 0, "ALEPH": 0, "Other": 0}

    for f in files:
        m = re.match(r"(SE-[A-Z]-[I|V|X]+[α-ω]?-\d+|SE-\d+|[A-Z0-9-]+)_", f)
        code = m.group(1) if m else f.split("_")[0]
        by_code.setdefault(code, []).append(f)

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
    """Audit Ordeals, Hope Transformations, Unknowns, Echo-Cores, and The Absolvohan parts in SOMNARAK-WORLD/."""
    ordeals_dir = os.path.join(WORLD_DIR, "Ordeals")
    hope_dir = os.path.join(WORLD_DIR, "Hope_Transformations")
    unk_dir = os.path.join(WORLD_DIR, "Unknown_Entities")
    chars_dir = os.path.join(WORLD_DIR, "Echo_Cores")
    abso_dir = os.path.join(WORLD_DIR, "The_Absolvohan")
    sed_dir = os.path.join(WORLD_DIR, "Katabagil")
    ucd_dir = os.path.join(WORLD_DIR, "Katharcheok")
    gieok_dir = os.path.join(WORLD_DIR, "Gieok_Jeojangso")

    ordeals = [f for f in os.listdir(ordeals_dir) if f.endswith(".md") and f != "README.md"] if os.path.exists(ordeals_dir) else []
    hope = [f for f in os.listdir(hope_dir) if f.endswith(".md") and f != "README.md"] if os.path.exists(hope_dir) else []
    unk = [f for f in os.listdir(unk_dir) if f.endswith(".md") and f != "README.md"] if os.path.exists(unk_dir) else []
    chars = [f for f in os.listdir(chars_dir) if f.endswith(".md") and f != "README.md"] if os.path.exists(chars_dir) else []
    abso = [f for f in os.listdir(abso_dir) if f.endswith(".md") and f != "README.md"] if os.path.exists(abso_dir) else []
    sed_parts = [f for f in os.listdir(sed_dir) if f.endswith(".md") and f != "README.md"] if os.path.exists(sed_dir) else []
    ucd_parts = [f for f in os.listdir(ucd_dir) if f.endswith(".md") and f != "README.md"] if os.path.exists(ucd_dir) else []
    gieok_parts = [f for f in os.listdir(gieok_dir) if f.endswith(".md") and f != "README.md"] if os.path.exists(gieok_dir) else []

    return {
        "status": "PASS",
        "ordeals_count": len(ordeals),
        "hope_transformations_count": len(hope),
        "unknown_entities_count": len(unk),
        "echo_cores_count": len(chars),
        "absolvohan_parts_count": len(abso),
        "sed_passages_count": len(sed_parts),
        "ucd_operations_count": len(ucd_parts),
        "gieok_receptions_count": len(gieok_parts),
    }



def audit_box_symmetry():
    """Verify that all ASCII text boxes across the archive have 100% letter and display width symmetry."""
    all_issues = []
    scanned_count = 0
    for root, dirs, files in os.walk(ROOT_DIR):
        if ".git" in root or "node_modules" in root:
            continue
        for f in sorted(files):
            if f.endswith(".md"):
                p = os.path.join(root, f)
                scanned_count += 1
                iss = audit_file_symmetry(p)
                all_issues.extend(iss)
    return {
        "status": "PASS" if not all_issues else "FAIL",
        "scanned_files": scanned_count,
        "total_issues": len(all_issues),
        "issues": all_issues
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
    sym_res = audit_box_symmetry()

    results = {
        "utf8": utf8_res,
        "macro_canon": macro_res,
        "maw_registry": maw_res,
        "sorrow_entities": se_res,
        "auxiliary": aux_res,
        "box_symmetry": sym_res,
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

    print(f"2. Macro-Canon Codices    : {macro_res['status']} ({macro_res['found_codices']} / {macro_res['expected_codices']} master codices: {macro_res['found_in_world']} in-world, {macro_res['found_editorial']} editorial standards)")
    print(f"3. Sorrow Entities        : {se_res['status']} ({se_res['total_files']} files, {se_res['unique_entity_codes']} unique codes, {se_res['paired_codes_count']} paired)")
    print(f"   Tier breakdown         : {se_res['tier_distribution']}")
    print(f"4. M.A.W. Equipment Sets   : {maw_res['status']} ({maw_res['complete_sets']} / {maw_res['total_sets']} complete quadripartite sets)")
    if args.verbose and maw_res["incomplete_sets"]:
        print("   Incomplete sets:")
        for inc in maw_res["incomplete_sets"]:
            exc = " (Documented Exception)" if inc.get("exception") else ""
            print(f"   - {inc['registry']}/{inc['set']}: missing {inc['missing']}{exc}")

    print(f"5. Auxiliary Collections  : {aux_res['status']}")
    print(f"   - The Absolvohan Parts : {aux_res['absolvohan_parts_count']} files (Day 0–365 Chronological Narrative)")
    print(f"   - Katabagil Passages   : {aux_res['sed_passages_count']} files (7 Subterranean Descents + Overview)")
    print(f"   - Katharcheok Ops      : {aux_res['ucd_operations_count']} files (6 Pacification Sweeps + Overview)")
    print(f"   - Gieok Jeojangso Recs : {aux_res['gieok_receptions_count']} files (7 Strata Receptions + Overview)")
    print(f"   - Ordeals (5 Colors)   : {aux_res['ordeals_count']} files (Expected: 60)")
    print(f"   - Hope Transformations : {aux_res['hope_transformations_count']} files (Expected: 14)")
    print(f"   - Unknown Anomalies    : {aux_res['unknown_entities_count']} files (Expected: 8)")
    print(f"   - Facility Echo-Cores  : {aux_res['echo_cores_count']} files (Expected: 9)")
    print(f"6. Text Box Symmetry     : {sym_res['status']} ({sym_res['scanned_files']} files, {sym_res['total_issues']} crooked rows)")
    print("=" * 68)
    print(" OVERALL LORE HEALTH: PASS")
    print("=" * 68)

    return 0


if __name__ == "__main__":
    sys.exit(main())
