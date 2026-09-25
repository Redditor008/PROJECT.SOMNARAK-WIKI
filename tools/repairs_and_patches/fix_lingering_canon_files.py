#!/usr/bin/env python3
"""
tools/fix_lingering_canon_files.py
Cleans up legacy developer meta notes, crossover leftovers, and ensures 100% lore integrity:
1. The_REVERIE_DIRECTORATE.md: removes developer 'Lobotomy-Class' and 'In Lobotomy Corporation' notes
2. SOMNARAK_HORIZON_CARAVAN.md: transforms legacy 'PM Elements Used' and 'Limbus Company' into canonical in-universe systems
3. SOMNARAK_MEMORY_ARCHIVE.md: transforms legacy 'PM Elements Used' and 'Library of Ruina' into canonical in-universe systems
4. SOMNARAK_NAMED_FRACTURES.md: cleans 'Soul & Ego State' into 'Soul & Identity State'
5. SE-C-IIIβ-014 (both files): cleans 'ego buffers' into 'identity buffers'
6. SOMNARAK_UNDERWORLD.md: cleans 'Mender Associations' into 'Restoration Guilds'
7. SOMNARAK_HAN_RELICS.md & SOMNARAK_CORPORATIONS.md: cleans reality/environmental 'distortions' into 'disruptions'
8. Echo_Cores (EXILE, OUTSIDER, SECRETARY) & HT-007: cleans 'distortion' into 'disruption'
"""

import sys
import os

def replace_in_file(path, old_text, new_text):
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return False
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    if old_text in content:
        new_content = content.replace(old_text, new_text)
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Replaced successfully in {path}")
        return True
    else:
        print(f"Target text not found in {path}")
        return False

# 1. The_REVERIE_DIRECTORATE.md
replace_in_file(
    "SOMNARAK-WORLD/Master_Codices/02_Institutional_Wings_and_Chronicles/The_REVERIE_DIRECTORATE.md",
    "## Advanced Facility Systems & Operational Protocols (Lobotomy-Class Mechanics Expanded)",
    "## Advanced Facility Systems & Operational Protocols (Enterprise Containment Mechanics Expanded)"
)
replace_in_file(
    "SOMNARAK-WORLD/Master_Codices/02_Institutional_Wings_and_Chronicles/The_REVERIE_DIRECTORATE.md",
    "In Lobotomy Corporation, non-living containment units are designated as \"Tool Abnormalities\". In Project Somnarak, these entities are **NOT** designated under a fabricated \"Class-T\" (in canonical SECC syntax, **T** denotes **Time Manifestation**, while **O** is Object, **P** is Place, and **H** is Hazard). Instead, they are canonically classified as **Relic-Entities (유물형 슬픔 개체)**: manifested sorrow artifacts, architectural relics, and temporal anomalies categorized under three operational **Tool Classes**:",
    "In advanced sorrow physics, non-living containment apparatuses are designated as **Relic-Entities (유물형 슬픔 개체)**: manifested sorrow artifacts, architectural relics, and temporal anomalies categorized under three operational **Tool Classes** (in canonical SECC syntax, **O** is Object, **P** is Place, **H** is Hazard, and **T** is Time Manifestation):"
)

# 2. SOMNARAK_HORIZON_CARAVAN.md
replace_in_file(
    "SOMNARAK-WORLD/Master_Codices/01_Cosmology_and_World_Order/SOMNARAK_HORIZON_CARAVAN.md",
    "**Game Style:** Limbus Company — Bus Travel, Urban Threat Levels, Identity Variants",
    "**Game Style:** Expedition Tactical RPG — Mobile Throne Transit, Regional Threat Scales, Identity Variant Shifts"
)
replace_in_file(
    "SOMNARAK-WORLD/Master_Codices/01_Cosmology_and_World_Order/SOMNARAK_HORIZON_CARAVAN.md",
    """## VII. PM Elements Used

| PM Game | Element | How Used |
|---|---|---|
| **Limbus** | Bus Mechanic | The Drift Throne — mobile base |
| **Limbus** | Urban Threat Levels | Danger increases near cities |
| **LoR** | District Exploration | Traveling between cities |
| **LC** | Facility Management | Managing the Caravan's supplies |""",
    """## VII. Core Structural Dynamics & Travel Physics

| Engine Domain | Mechanical Element | Institutional Implementation |
|---|---|---|
| **Mobile Transit** | Nomadic Base Engine | The Drift Throne — self-sustaining all-terrain command crawler |
| **Danger Gradient**| Regional Threat Scales | Atmospheric Han concentration increases in proximity to ruined city outskirts |
| **Inter-Zone Trek**| District Traversal | Navigating subterranean tunnels and fractured overland trade routes |
| **Resource Economy**| Expedition Supply Matrix | Managing rations, Han battery filters, and caravan structural maintenance |"""
)

# 3. SOMNARAK_MEMORY_ARCHIVE.md
replace_in_file(
    "SOMNARAK-WORLD/Master_Codices/01_Cosmology_and_World_Order/SOMNARAK_MEMORY_ARCHIVE.md",
    "**Game Style:** Library of Ruina — Reception Battles, Floor Realizations, Key Pages",
    "**Game Style:** Mnemonic Combat Framework — Guest Confrontations, Floor Realizations, Mnemonic Core Transmutation"
)
replace_in_file(
    "SOMNARAK-WORLD/Master_Codices/01_Cosmology_and_World_Order/SOMNARAK_MEMORY_ARCHIVE.md",
    """## VII. PM Elements Used

| PM Game | Element | How Used |
|---|---|---|
| **LoR** | Reception Battles | Combat encounters with the Archive's preserved |
| **LoR** | Floor Realizations | Character exploration through combat |
| **LoR** | Key Pages | Character progression through battle |
| **LoR** | The Library | The Memory Archive — consumes and preserves |
| **LoR** | Urban Threat Levels | Archive floor danger ratings |
| **LC** | Memory Repository | The Archive's preservation system |""",
    """## VII. Core Structural Dynamics & Mnemonic Physics

| Engine Domain | Mechanical Element | Institutional Implementation |
|---|---|---|
| **Mnemonic Clashes** | Reception Confrontations | Tactical combat gauntlets confronting the Archive's preserved emotional memories |
| **Psychic Trials** | Floor Realizations | Navigating the suppressed trauma of Floor Leads to transmute despair into Hope |
| **Soul Formations** | Key Core Transmutation | Operative progression and stat scaling through crystallized mnemonic pages |
| **Mnemonic Domain** | The Grand Archive | 6,000-year-old subterranean complex consuming identities and preserving history |
| **Stratum Danger** | Floor Threat Metrics | Increasing metaphysical danger across the vertical floors of the Archive |
| **Core Preservation**| Memory Repository | The Alpha Tree deep vault safeguarding cognitive records against cyclical rewinds |"""
)

# 4. SOMNARAK_NAMED_FRACTURES.md
replace_in_file(
    "SOMNARAK-WORLD/Master_Codices/05_Entities_Tales_and_Fractures/SOMNARAK_NAMED_FRACTURES.md",
    "| **Soul & Ego State** | Complete ontological dissolution; human ego erased | Retains core human soul; suffers severe trauma saturation |",
    "| **Soul & Identity State** | Complete ontological dissolution; human identity erased | Retains core human soul; suffers severe trauma saturation |"
)

# 5. SE-C-IIIβ-014 (both files)
replace_in_file(
    "SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIIβ-014_Debt_Eater_빚을_먹는_자.md",
    "dissolves ungrounded ego buffers.",
    "dissolves ungrounded identity buffers."
)
replace_in_file(
    "SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIIβ-014_The_Debt_Eater_빚을_먹는_자.md",
    "dissolves ungrounded ego buffers.",
    "dissolves ungrounded identity buffers."
)

# 6. SOMNARAK_UNDERWORLD.md
replace_in_file(
    "SOMNARAK-WORLD/Master_Codices/04_Municipal_Society_and_Demographics/SOMNARAK_UNDERWORLD.md",
    "Unlike the standard Mender Associations, Menders are mostly **independent**.",
    "Unlike formal municipal Restoration Guilds, Menders are mostly **independent**."
)

# 7. SOMNARAK_HAN_RELICS.md & SOMNARAK_CORPORATIONS.md
replace_in_file(
    "SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_HAN_RELICS.md",
    "causing localized reality distortions, gravity inversions, and spontaneous Sorrow Entity manifestations.",
    "causing localized reality disruptions, gravity inversions, and spontaneous Sorrow Entity manifestations."
)
replace_in_file(
    "SOMNARAK-WORLD/Master_Codices/04_Municipal_Society_and_Demographics/SOMNARAK_CORPORATIONS.md",
    "navigate encounters with wild entities and hostile environmental distortions",
    "navigate encounters with wild entities and hostile environmental disruptions"
)

# 8. Echo_Cores (EXILE, OUTSIDER, SECRETARY) & HT-007
replace_in_file(
    "SOMNARAK-WORLD/Echo_Cores/THE_EXILE.md",
    "- Gate distortion;",
    "- Gate disruption;"
)
replace_in_file(
    "SOMNARAK-WORLD/Echo_Cores/THE_OUTSIDER.md",
    "causes false pressure in Ishall's palms, depth distortion, and delayed hand-position feedback.",
    "causes false pressure in Ishall's palms, depth disruption, and delayed hand-position feedback."
)
replace_in_file(
    "SOMNARAK-WORLD/Echo_Cores/THE_OUTSIDER.md",
    "- **Element Signature:** Pure **Void (Pale White)** area-denial and spatial distortion.",
    "- **Element Signature:** Pure **Void (Pale White)** area-denial and spatial disruption."
)
replace_in_file(
    "SOMNARAK-WORLD/Echo_Cores/THE_SECRETARY.md",
    "Any visible distortion is limited to directly relevant overload,",
    "Any visible disruption is limited to directly relevant overload,"
)
replace_in_file(
    "SOMNARAK-WORLD/Echo_Cores/THE_SECRETARY.md",
    "Similar distortions may occur during network failure,",
    "Similar disruptions may occur during network failure,"
)
replace_in_file(
    "SOMNARAK-WORLD/Hope_Transformations/HT-007_The_Silent_Vigil_침묵의_경계.md",
    "through darkness or Veil distortion.",
    "through darkness or Veil disruption."
)
replace_in_file(
    "SOMNARAK-WORLD/Hope_Transformations/HT-007_The_Silent_Vigil_침묵의_경계.md",
    "Reveals movement hidden by darkness or Veil distortion.",
    "Reveals movement hidden by darkness or Veil disruption."
)

print("Finished cleanup routine!")
