#!/usr/bin/env python3
"""
tools/builders/export_maw_csv_registry.py
================================================================================
PROJECT SOMNARAK — M.A.W. EQUIPMENT MASTER CSV / SPREADSHEET EXPORTER
================================================================================
Parses all 1,165 M.A.W. equipment dossiers across 42 sets in
SOMNARAK-WORLD/MAW_Codex_Sets/ and exports an authoritative, machine-readable
CSV spreadsheet dataset to REFERENCE_SOMNARAK_WIKI/MAW_EQUIPMENT_MASTER_REGISTRY.csv.
================================================================================
"""

import os
import glob
import re
import csv

def extract_maw_data():
    base_dir = "SOMNARAK-WORLD/MAW_Codex_Sets"
    maw_files = sorted([
        f for f in glob.glob(f"{base_dir}/**/*.md", recursive=True)
        if not f.endswith("README.md")
    ])

    records = []

    for fpath in maw_files:
        with open(fpath, "r", encoding="utf-8", errors="ignore") as fp:
            txt = fp.read()

        fname = os.path.basename(fpath)
        folder = os.path.dirname(fpath).replace("SOMNARAK-WORLD/MAW_Codex_Sets/", "")

        # 1. Equipment Type
        if "SIDE_CODEX" in fname or "-A__" in fname or "-A_" in fname:
            eq_type = "Side-Codex"
        elif "MAW-W" in fname or "-B__" in fname or "-B_" in fname:
            eq_type = "Weapon"
        elif "MAW-S" in fname or "-C__" in fname or "-C_" in fname:
            eq_type = "Suit"
        elif "MAW-G" in fname or "-D__" in fname or "-D_" in fname:
            eq_type = "Gift"
        else:
            eq_type = "Unknown"

        # 2. Item Name from Heading
        first_line = txt.strip().splitlines()[0] if txt.strip() else ""
        title_m = re.search(r"^#\s+(?:SIDE CODEX|M\.A\.W\.\s+[A-Z\s]+)—\s*(.+)$", first_line)
        if title_m:
            item_name = title_m.group(1).strip()
        else:
            # fallback from filename
            clean_name = fname.replace(".md", "").split("__")[-1]
            clean_name = re.sub(r"^(?:SIDE_CODEX_|MAW-[WSG]_)", "", clean_name)
            item_name = clean_name.replace("_", " ")

        # 3. Document ID
        doc_m = re.search(r"\*\*Document ID:\*\*\s*`?([A-Za-z0-9_-]+)`?", txt)
        doc_id = doc_m.group(1) if doc_m else fname.split("__")[0]

        # 4. Item Registry Code
        reg_m = re.search(r"\*\*Item Registry Code:\*\*\s*`?([A-Za-z0-9_-]+)`?", txt)
        reg_code = reg_m.group(1) if reg_m else doc_id

        # 5. Linked Entity ID & Name
        ent_m = re.search(r"\*\*Linked Entity(?:\s+ID)?:\*\*\s*`?([A-Za-z0-9_-]+)`?(?:\s*—\s*([^\n\r]+))?", txt)
        ent_id = ent_m.group(1) if ent_m else ""
        ent_name = ent_m.group(2).strip() if ent_m and ent_m.group(2) else ""
        if not ent_name:
            rel_m = re.search(r"\*\*Related Entity ID:\*\*\s*`?([A-Za-z0-9_-]+)`?", txt)
            if rel_m and not ent_id:
                ent_id = rel_m.group(1)

        # 6. Grade
        grade_m = re.search(r"\|\s*\*\*Grade\*\*\s*\|\s*([^|\n]+)\|", txt)
        grade = grade_m.group(1).strip() if grade_m else ""
        if not grade:
            grade_m2 = re.search(r"(?:Grade|Coherence / Potency)\s*[:|]\s*([^\n|]+)", txt)
            grade = grade_m2.group(1).strip() if grade_m2 else "N/A"

        # 7. Element
        elem_m = re.search(r"\|\s*\*\*Element\*\*\s*\|\s*([^|\n]+)\|", txt)
        element = elem_m.group(1).strip() if elem_m else ""
        if not elem_m:
            elem_m2 = re.search(r"Element(?:\s*/\s*Location)?\s*[:|]\s*([^|\n]+)", txt)
            element = elem_m2.group(1).strip() if elem_m2 else "N/A"

        # 8. Maximum Amount & Echo Cost
        max_m = re.search(r"\|\s*\*\*Maximum Amount\*\*\s*\|\s*([^|\n]+)\|", txt)
        max_amount = max_m.group(1).strip() if max_m else "N/A"

        echo_m = re.search(r"\|\s*\*\*Echo Cost\*\*\s*\|\s*([^|\n]+)\|", txt)
        echo_cost = echo_m.group(1).strip() if echo_m else "N/A"

        # 9. Signature Ability / Trait
        sig_m = re.search(r"###\s+(?:Signature Ability|Defensive Trait|Passive Ability)\s*—\s*([^\n\r]+)", txt)
        signature_ability = sig_m.group(1).strip() if sig_m else "N/A"

        # 10. Combat / Defense / Slot Stats
        stats_desc = "N/A"
        if eq_type == "Weapon":
            dmg_m = re.search(r"\|\s*\*\*Damage\*\*\s*\|\s*([^|\n]+)\|", txt)
            spd_m = re.search(r"\|\s*\*\*Speed\*\*\s*\|\s*([^|\n]+)\|", txt)
            rng_m = re.search(r"\|\s*\*\*Range\*\*\s*\|\s*([^|\n]+)\|", txt)
            dmg = dmg_m.group(1).strip() if dmg_m else "Variable"
            spd = spd_m.group(1).strip() if spd_m else "-"
            rng = rng_m.group(1).strip() if rng_m else "-"
            stats_desc = f"DMG: {dmg} | SPD: {spd} | RNG: {rng}"
        elif eq_type == "Suit":
            res_lament = re.search(r"\|\s*\*\*Lament[^\*]*\*\*\s*\|\s*([^|\n]+)\|", txt)
            res_grudge = re.search(r"\|\s*\*\*Grudge[^\*]*\*\*\s*\|\s*([^|\n]+)\|", txt)
            res_void = re.search(r"\|\s*\*\*Void[^\*]*\*\*\s*\|\s*([^|\n]+)\|", txt)
            res_weight = re.search(r"\|\s*\*\*Weight[^\*]*\*\*\s*\|\s*([^|\n]+)\|", txt)
            if res_lament and res_grudge and res_void and res_weight:
                stats_desc = f"Res: L:{res_lament.group(1).strip()} | G:{res_grudge.group(1).strip()} | V:{res_void.group(1).strip()} | W:{res_weight.group(1).strip()}"
            else:
                stats_desc = "Standard Attire Resistances"
        elif eq_type == "Gift":
            slot_m = re.search(r"\|\s*\*\*Slot\*\*\s*\|\s*([^|\n]+)\|", txt)
            chance_m = re.search(r"\|\s*\*\*Bestowal Chance\*\*\s*\|\s*([^|\n]+)\|", txt)
            slot = slot_m.group(1).strip() if slot_m else "Accessory"
            chance = chance_m.group(1).strip() if chance_m else "5%"
            stats_desc = f"Slot: {slot} | Bestowal: {chance}"
        elif eq_type == "Side-Codex":
            stats_desc = "Master Side-Codex Dossier & Extraction Rules"

        records.append({
            "Document_ID": doc_id,
            "Item_Registry_Code": reg_code,
            "Item_Name": item_name,
            "Equipment_Type": eq_type,
            "Linked_Entity_ID": ent_id,
            "Linked_Entity_Name": ent_name,
            "Grade": grade,
            "Element": element,
            "Maximum_Amount": max_amount,
            "Echo_Cost": echo_cost,
            "Combat_Parameters_Or_Resistances": stats_desc,
            "Signature_Ability": signature_ability,
            "Registry_Folder": folder,
            "File_Path": fpath
        })

    return records

def export_csv(output_path="REFERENCE_SOMNARAK_WIKI/MAW_EQUIPMENT_MASTER_REGISTRY.csv"):
    records = extract_maw_data()
    fieldnames = [
        "Document_ID",
        "Item_Registry_Code",
        "Item_Name",
        "Equipment_Type",
        "Linked_Entity_ID",
        "Linked_Entity_Name",
        "Grade",
        "Element",
        "Maximum_Amount",
        "Echo_Cost",
        "Combat_Parameters_Or_Resistances",
        "Signature_Ability",
        "Registry_Folder",
        "File_Path"
    ]

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as fp:
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

    print(f"Successfully exported {len(records)} M.A.W. equipment dossiers to {output_path}!")
    return len(records)

if __name__ == "__main__":
    export_csv()
