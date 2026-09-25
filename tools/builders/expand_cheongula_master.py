#!/usr/bin/env python3
"""
tools/expand_cheongula_master.py
Enriches SOMNARAK_CHEONGULA.md into an encyclopedic master codex while
strictly preserving 100% of the original text (Zero Shortening, Zero Summarizing).
"""

import os, sys
sys.path.append(os.path.dirname(__file__))
from box_formatter import make_box

def wrap_box(b):
    return "```text\n" + b + "\n```\n\n"

def build_enriched_cheongula():
    path = "SOMNARAK-WORLD/Master_Codices/01_Cosmology_and_World_Order/SOMNARAK_CHEONGULA.md"
    with open(path, "r", encoding="utf-8") as f:
        original = f.read()

    # Master top dossier box
    top_dossier = make_box("ARCHIVAL DOSSIER: THE CHEONGULA EVENT (YEAR 202 CALAMITY)", [
        "ARCHIVE CODE    : COSMO-CHEONGULA-ZERO-POINT-4238",
        "DATE & EPOCH    : Year 202, 2nd Month, Day 14 (The 44th Day of Frost)",
        "PRIMARY THEATER : Zone B (Western Industrial Basin / Sunken Quarry)",
        "CASUALTY TOLL   : Exactly 1,000 Registered Citizens Consumed",
        "---",
        "ONTOLOGICAL PHENOMENON & CIVIC AFTERMATH:",
        "- Tectonic Fissure Collapse into Primordial Liquid Han Mantle",
        "- Genesis of The Maw (Ravenous Maw) & The Subterranean Weeping",
        "- Creation of the Municipal Debt Ledger to Monetize Guilt",
        "- Universal Mandate of the Acoustic Veil & Censorship Ordinances",
        "- Establishment of Subterranean Facility 01 & Reverie Directorate",
        "---",
        "PRIMARY ARCHIVAL EYEWITNESS TESTIMONY:",
        "- Archive Lead Marjuk (Cryogen Stasis Eye / Sole Biological Scribe)",
        "- Containment Lead Dekan (Carries Living Maw Graft from Fissure Bed)",
        "- Council of Sighs Historical Expungement Order (Decree Alpha-01)"
    ])
    
    # Chronology matrix box
    chronology_box = make_box("CHRONOLOGY: FROM SETTLEMENT TO THE YEAR 202 CATACLYSM", [
        "EPOCH / YEAR         | INCIDENT & DEVELOPMENTAL PHASE",
        "---------------------+-----------------------------------------------",
        "Year 0               | Settlers arrive on Mugenhan; discover Han well",
        "Year 0 - 50          | Alpha Tree roots tapped for thermal heating",
        "Year 100             | Zone A fortified; laborers pushed to Zone B",
        "Year 150 - 180       | Liquid Han rises; foundations crack in Zone B",
        "Year 195             | Architect Jun warns Council of imminent breach",
        "Year 201 (Winter)    | Bedrock liquefies; blue steam vents in streets",
        "Year 202 (Month 2)   | THE CHEONGULA: Subterranean collapse consumes 1,000",
        "Year 203             | High Council enacts Historical Expungement Law"
    ])
    
    # Seismic telemetry warning box
    warning_box = make_box("THE 44-DAY RECORD OF UNHEEDED MUNICIPAL ALARMS", [
        "DAY & LOG NUMBER     | SEISMIC / ACOUSTIC OBSERVATION REPORT",
        "---------------------+-----------------------------------------------",
        "Day 03 (Log 1,102)   | Basalt pilings in Sub-Level 4 sink by 18 cm",
        "Day 12 (Log 1,145)   | Blue steam vents erupt inside tenement floors",
        "Day 21 (Log 1,189)   | Water wells turn bitter; liquid glows at 432 Hz",
        "Day 30 (Log 1,215)   | 400 miners refuse entry; Wardens enforce quotas",
        "Day 39 (Log 1,260)   | Architect Jun presents Council with breach model",
        "Day 44 (Hour 03:12)  | Structural collapse: 1,000 citizens swallowed"
    ])
    
    # The Seven Fissure points box
    fissures_box = make_box("THE SEVEN FISSURE POINTS OF THE CHEONGULA", [
        "FISSURE LOCUS        | GEOLOGICAL FEATURE      | RESIDUAL PHENOMENON",
        "---------------------+-------------------------+---------------------",
        "Point 1: The Lip     | Gaping 300m Rim Crater  | Acoustic Resonance",
        "Point 2: Sluice Bed  | Calcified Stone Steps   | Weeping River Source",
        "Point 3: Iron Basin  | Crushed Tenement Slag   | Magnetic Static Field",
        "Point 4: Bone Grove  | Needle-Glass Pillars    | Entity Nursery",
        "Point 5: The Throat  | Vertical 800m Chasm     | Gravitational Weight",
        "Point 6: Deep Sump   | Boiling Liquid Han Well | High-Pressure Grief",
        "Point 7: The Heart   | Central Maw Nucleus     | The Thousand's Cry"
    ])
    
    # Institutional tethers box
    inst_scars_box = make_box("THE FIVE INSTITUTIONS & THEIR CHEONGULA TETHERS", [
        "INSTITUTION          | HISTORICAL TETHER       | OPERATIONAL BURDEN",
        "---------------------+-------------------------+---------------------",
        "Reverie Directorate  | Floor 2 Dekan & Floor 6 | Contains Maw Entities",
        "SED Abyssal Corps    | Katabagil Passage 6     | Charts Sunken Quarry",
        "UCD Strike Force     | Katharcheok Operation 6 | Polices Zone B Fissure",
        "The Memory Archive   | Reception 6 (Lament)    | Preserves Lost Census",
        "The Horizon Caravan  | Gate of Sighs Memorial  | Escorts Fissure Exiles"
    ])
    
    # 1. Insert top dossier right after epigraph
    epigraph_anchor = '> *"The city was built on a grave. The grave was built on indifference. The indifference was built on the backs of people who didn\'t matter."*\n\n---\n\n'
    assert epigraph_anchor in original, "Epigraph anchor not found!"
    original = original.replace(epigraph_anchor, epigraph_anchor + wrap_box(top_dossier))
    
    # 2. Insert chronology box right before Section II
    sec2_anchor = "## II. The Warning Signs — The Han's Growth\n\n"
    assert sec2_anchor in original, "Section II anchor not found!"
    original = original.replace(sec2_anchor, wrap_box(chronology_box) + sec2_anchor)
    
    # 3. Insert warning box right before Section III
    sec3_anchor = "## III. The Cheongula — The Day of Consuming\n\n"
    assert sec3_anchor in original, "Section III anchor not found!"
    original = original.replace(sec3_anchor, wrap_box(warning_box) + sec3_anchor)
    
    # 4. Insert fissure points box in Section V right after "### The Weeping's Response"
    weeping_anchor = "The Cheongula did not just create the Maw. The Cheongula created the city's *emotional foundation*. Every citizen's sorrow is built on the thousand's neglect.\n\n---\n\n"
    assert weeping_anchor in original, "Weeping anchor not found!"
    fissures_insert = "The physical scar left by the Cheongula is divided into seven distinct geological and metaphysical trauma zones:\n\n" + wrap_box(fissures_box) + "These seven fissure points remain permanently classified. Under municipal law, entering within five hundred paces of Fissure Point 7 without a Level-5 Directorate clearance carries the immediate penalty of cognitive erasure.\n\n---\n\n"
    original = original.replace(weeping_anchor, weeping_anchor + fissures_insert)
    
    # 5. Insert institutional scars box in Section VIII right before "### The Debt System"
    sec8_anchor = "## VIII. The Connections — How The Cheongula Shaped Everything\n\n"
    assert sec8_anchor in original, "Section VIII anchor not found!"
    inst_insert = "The modern institutional framework of Somnarak exists as a direct psychological and mechanical defense against the horror of Year 202:\n\n" + wrap_box(inst_scars_box)
    original = original.replace(sec8_anchor, sec8_anchor + inst_insert)
    
    # 6. Append new Sections XI and XII at the very end
    appendix = []
    appendix.append("\n## XI. The Dawn Accord & The Historical Exhumation (Year 4,238 Restoration)\n\n")
    appendix.append("In the year 4,238, following the completion of the 1,778th Absolvohan cycle and the establishment of the overland highway to Cheonbulok, the leaders of the Five Institutions signed the **Dawn Accord (여명의 협약 / 黎明의 協約)**.\n\n")
    appendix.append("For four thousand years, the Council's response to the Cheongula was censorship, suppression, and debt. They taught the citizens to wear the Veil so they would not look down. They established the debt system so that sorrow could be bought and sold like grain.\n\n")
    appendix.append("Under the Dawn Accord, the truth of Year 202 was officially exhumed:\n\n")
    
    redemption_box = make_box("SOVEREIGN CONVERGENCE: REDEMPTION OF THE FIRST SORROW", [
        "1. Truth Over Erasure    : The Census of Year 202 restored to public light.",
        "2. Transmutation of Pain: Absolvohan releases the thousand from the Maw.",
        "3. Dismantlement of Debt : Civic debt forgiven; usury frays eradicated.",
        "4. The Horizon Accord   : The city looks outward to a living world."
    ])
    appendix.append(wrap_box(redemption_box))
    
    appendix.append("1. **The Restoration of the Census of Year 202:** The Memory Archive opened the sealed vaults of the 6th Stratum (Floor of Lamentation). For the first time in history, the names of the one thousand laborers were broadcast across the public radios of Zones A, B, C, D, and E.\n")
    appendix.append("2. **The De-Sanctification of the Council Vaults:** The classified decree *Alpha-01*—ordering Wardens to hold the perimeter and prevent rescue—was published on the outer walls of the High Council building.\n")
    appendix.append("3. **The Absolvohan Release:** As Director Majin unsealed the central resonance valves of Facility 01, the 45% planetary transmutation began. The howling from Fissure Point 7 shifted from a chord of unbearable agony into a quiet, warm resonance of rest.\n\n")
    appendix.append("---\n\n")
    
    appendix.append("## XII. Classified Scribe Logs: The Living Eye of Year 202\n\n")
    appendix.append("Preserved within Archive Lead Marjuk's stasis effigy is the only surviving unedited recording from Hour 03:12 of that fateful winter morning:\n\n")
    
    log_box = make_box("VOX RECORDING TRANSCRIPT: MARJUK STASIS LOG 001", [
        "TIMESTAMP        : Year 202, 2nd Month, Day 14 — Hour 03:12:44",
        "RECORDING RELIC  : Leaded Wire Wax Cylinder #04 (Unredacted)",
        "SCRIBE IDENTIFIER: Apprentice Scribe Marjuk (Age 19 at Event)",
        "---",
        "\"The ground didn't crack. It turned into black water.",
        " I saw the tenement of Master Mason Kang sink into the floor",
        " like a stone dropped in an oil drum. Kang was screaming out",
        " his daughter's name. The Wardens were locking the iron gates",
        " from the outside. I shouted at Warden Captain Vane to open",
        " the latch, but he held up the Council parchment. 'No entry.",
        " The tree needs the weight.' God forgive us. We watched them",
        " go down and we went home and ate our dinner.\"",
        "---",
        "CURRENT STATUS: AUTHENTICATED & PERMANENTLY UNSEALED"
    ])
    appendix.append(wrap_box(log_box))
    
    appendix.append("The Cheongula was the moment humanity fell into the dark. The Dawn of Hope is the long, agonizing, magnificent climb back into the morning light.\n\n")
    appendix.append("---\n\n")
    appendix.append('*Codex Authorization: High Director Majin & Archive Lead Marjuk. Verified by the Joint Council of the Five Institutions. Sealed under Sovereign Cosmological Record CORP-ZERO-POINT-4238.*\n')
    
    return original + "".join(appendix)

if __name__ == "__main__":
    content = build_enriched_cheongula()
    out_path = "SOMNARAK-WORLD/Master_Codices/01_Cosmology_and_World_Order/SOMNARAK_CHEONGULA.md"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("SOMNARAK_CHEONGULA.md expanded successfully!")
