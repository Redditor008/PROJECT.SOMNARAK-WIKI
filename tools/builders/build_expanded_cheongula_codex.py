#!/usr/bin/env python3
"""
tools/build_expanded_cheongula_codex.py
Generates the enriched, deeply detailed master codex:
SOMNARAK-WORLD/Master_Codices/01_Cosmology_and_World_Order/SOMNARAK_CHEONGULA.md
"""

import sys, os
sys.path.append(os.path.dirname(__file__))
from box_formatter import make_box

def wrap_box(b):
    return "```text\n" + b + "\n```\n\n"

def build_codex():
    sections = []
    
    # Title & Subtitle
    sections.append("# SOMNARAK — The Cheongula Deep Dive (청굴라 총론 / 靑窟落 總論)\n")
    sections.append("## The First Sorrow, The Great Cataclysm of Year 202 & The Maw Genesis\n")
    sections.append("### Master Cosmological Codex — Classified Sovereign Archive (Year 4,238 Restoration Edition)\n\n")
    
    # Master Dossier Box
    dossier = make_box("ARCHIVAL DOSSIER: THE CHEONGULA EVENT (YEAR 202 CALAMITY)", [
        "CLASSIFICATION   : SOVEREIGN ORIGIN ARCHIVE / ZERO-POINT CANON",
        "DATE OF INCIDENT : Year 202, 2nd Month, Day 14 (The 44th Day of Frost)",
        "PRIMARY THEATER  : Zone B (Western Industrial Basin / The Sunken Quarry)",
        "CASUALTY TOLL    : Exactly 1,000 Registered Citizens Consumed",
        "---",
        "ONTOLOGICAL PHENOMENON:",
        "- Tectonic Fissure Collapse into Primordial Liquid Han Mantle",
        "- Genesis of The Maw (Agwi / Ravenous Maw) & The Weeping River",
        "- Institutional Implantation of the Municipal Debt Ledger",
        "- Universal Mandate of the Acoustic Veil & Censorship Ordinances",
        "---",
        "PRIMARY ARCHIVAL TESTIMONY:",
        "- Archive Lead Marjuk (Cryogen Stasis Eye / Sole Biological Witness)",
        "- Containment Lead Dekan (Carries Living Maw Graft from Fissure Bed)",
        "- Council of Sighs Historical Expungement Order (Decree Alpha-01)"
    ])
    sections.append(wrap_box(dossier))
    
    # Master Epigraph
    sections.append('> *"The city was built on a grave. The grave was built on indifference. The indifference was built on the backs of people who didn\'t matter. And the people who didn\'t matter are still screaming beneath our feet."*\n')
    sections.append('> — Archive Lead Marjuk, Living Biological Eyewitness, Stasis Transcript Fragment 001\n\n')
    sections.append('---\n\n')
    
    # Section I: Executive Overview
    sections.append("## Section I: Executive Overview — The Original Sin of Somnarak\n\n")
    sections.append("The **Cheongula (청굴라 / 靑窟落)**—literally 'The Collapse of the Blue Grotto'—is the foundational trauma of Somnarak. On the fourteenth day of the second month in Year 202 of the Municipal Calendar, a massive tectonic fracture beneath the western industrial tenements of **Zone B** collapsed into the subterranean mantle. Exactly **one thousand laborers, miners, and stone-cutters** were swallowed alive by a surge of supercritical, unstructured Liquid Han.\n\n")
    sections.append("The Cheongula was not an unavoidable natural catastrophe, nor was it a heroic sacrificial ritual. It was the direct consequence of **systemic municipal neglect**—the High Council's deliberate refusal to reinforce the foundation pilings of Zone B because the citizens living there were impoverished laborers deemed economically expendable.\n\n")
    sections.append("Every core institution, geopolitical border, mechanical system, and psychological defense mechanism in modern Somnarak traces its genesis directly to the Cheongula:\n")
    sections.append("- **The Maw (아귀 / Agwi):** The gaping subterranean abyss formed by the collapse, radiating perpetual sorrow.\n")
    sections.append("- **The Weeping (눈물의 강):** The subterranean river of liquid grief that surged upward through the fracture.\n")
    sections.append("- **The Municipal Debt Ledger:** The quantified economic system created to monetize guilt and control sorrow.\n")
    sections.append("- **The Acoustic Veil:** The mandatory sound-dampening silk cowls instituted to prevent citizens from hearing the dying screams of the thousand.\n")
    sections.append("- **The Reverie Directorate:** The subterranean containment wing established to suppress the entities spawned from the fissure.\n\n")
    sections.append('---\n\n')
    
    # Section II: Historical Timeline Matrix
    sections.append("## Section II: Historical Chronology of the Disaster (Years 0 to 202)\n\n")
    
    timeline_box = make_box("CHRONOLOGY: FROM SETTLEMENT TO THE YEAR 202 CATACLYSM", [
        "EPOCH / YEAR         | INCIDENT & DEVELOPMENTAL PHASE",
        "--------------------+------------------------------------------------",
        "Year 0              | Settlers arrive on Mugenhan; discover Han basin",
        "Year 0 - 50         | Alpha Tree roots tapped for thermal heating",
        "Year 100            | Zone A fortified; laborers pushed to Zone B",
        "Year 150 - 180      | Liquid Han rises; foundations crack in Zone B",
        "Year 195            | Architect Jun warns Council of imminent breach",
        "Year 201 (Winter)   | Bedrock liquefies; blue steam vents in streets",
        "Year 202 (Month 2)  | THE CHEONGULA: Subterranean collapse consumes 1,000",
        "Year 203            | High Council enacts Historical Expungement Law"
    ])
    sections.append(wrap_box(timeline_box))
    
    sections.append("### 2.1 The Founding Era (Years 0 to 100)\n\n")
    sections.append("Six thousand years prior to the current era, the original human colonists arrived on the barren continent of Mugenhan as refugees fleeing an unrecorded planetary cataclysm. Drawn by an acoustic humming vibrating through the earth, they established a permanent encampment around a monumental bio-crystalline structure: **The Alpha Tree (알파 나무)**.\n\n")
    sections.append("The early settlers discovered that the planet's mantle was saturated with **Han (한 / 恨)**—a primordial, fluid state of condensed metaphysical sorrow. When channeled through the roots of the Alpha Tree, Liquid Han could be stabilized into luminescence, clean thermal energy, and acoustic force fields. Somnarak was born not out of conquest, but out of desperate energetic symbiosis.\n\n")
    sections.append("### 2.2 The Great Disparity & The Zoning of Zone B (Years 100 to 180)\n\n")
    sections.append("As the population grew, the fertile core of Zone A became reserved exclusively for the ruling bureaucratic elite, high scholars, and the nascent **Council of Sighs**. The working class—miners, basalt masons, pipe-fitters, and hydraulic laborers—were relocated westward into the low-lying basin designated **Zone B**.\n\n")
    sections.append("Zone B sat directly above the geological fault where the Alpha Tree's deepest root-tendrils met the subterranean aquifers. Here, the ground was perpetually cold, damp, and prone to tremors. The bedrock was porous basalt, saturated with weeping condensation that the miners called 'Blue Brine.'\n\n")
    sections.append('---\n\n')
    
    # Section III: The 44 Days of Warning & Council Indifference
    sections.append("## Section III: The 44 Days of Warning & Council Indifference\n\n")
    sections.append("In the winter of Year 201, the signs of catastrophic structural failure became undeniable. Over forty-four consecutive days, seismic alarms blared across Zone B:\n\n")
    
    warning_box = make_box("THE 44-DAY RECORD OF UNHEEDED MUNICIPAL ALARMS", [
        "DAY & LOG NUMBER     | SEISMIC / ACOUSTIC OBSERVATION REPORT",
        "--------------------+------------------------------------------------",
        "Day 03 (Log 1,102)  | Basalt pilings in Sub-Level 4 sink by 18 cm",
        "Day 12 (Log 1,145)  | Blue steam vents erupt inside tenement kitchens",
        "Day 21 (Log 1,189)  | Water wells turn bitter; liquid glows at 432 Hz",
        "Day 30 (Log 1,215)  | 400 miners refuse entry; Wardens enforce quotas",
        "Day 39 (Log 1,260)  | Architect Jun presents Council with breach model",
        "Day 44 (Hour 03:12) | Structural collapse: 1,000 citizens swallowed"
    ])
    sections.append(wrap_box(warning_box))
    
    sections.append("### 3.1 The Jun Memorial Deposition\n\n")
    sections.append("On Day 39, Chief Architect Jun appeared before the Council of Sighs with physical core samples demonstrating that the bedrock beneath Zone B had turned into slurry. Jun requested an emergency budget of 40,000 marks to drive twenty adamantine stabilization caissons beneath the residential quarters.\n\n")
    sections.append("The Council rejected the proposal by unanimous vote. The recorded minutes from Session 84 summarize their chilling rationale:\n\n")
    sections.append('> *"The treasury cannot justify forty thousand marks for temporary shoring in a district whose tax yield is less than three percent of municipal revenue. The laborers exaggerate the tremors to negotiate lower extraction quotas. Reinforce the Warden patrols to ensure morning shift attendance."*\n')
    sections.append('> — Official Minutes, Council of Sighs, Year 202 (Exhumed Fragment 14)\n\n')
    sections.append('---\n\n')
    
    # Section IV: The Collapse of Year 202
    sections.append("## Section IV: The Day the Floor Fell (Year 202, Month 2, Day 14)\n\n")
    sections.append("At precisely 03:12 AM on the fourteenth day of the second month, the subterranean floor of Zone B gave way along a three-kilometer fault line. A cavernous void seven hundred meters wide opened beneath the sleeping tenements.\n\n")
    sections.append("Eyewitness accounts describe the horror not as a crash, but as an **inward acoustic implosion**. The earth did not merely crack; it dissolved into a howling vortex of dark azure liquid. Five residential blocks containing exactly one thousand registered men, women, and children plunged into the boiling subterranean river of sorrow.\n\n")
    sections.append("As the victims fell, their collective terror, agony, and betrayal catalyzed a catastrophic metaphysical reaction within the Liquid Han. The liquid crystallized instantaneously into jagged, miles-long needles of black and crimson glass, impaling the falling buildings in mid-air.\n\n")
    sections.append('The thousand souls were not granted the mercy of quick deaths. Suspended within the hyper-dense, crystalline matrix of the newly formed abyss, their consciousnesses merged into a single, permanent hive-mind of agonizing lamentation: **The Maw (아귀 / Agwi)**.\n\n')
    sections.append('---\n\n')
    
    # Section V: The Seven Fissure Points of Zone B
    sections.append("## Section V: The Seven Fissure Points of Zone B (칠대 단층점)\n\n")
    sections.append("The physical scar left by the Cheongula is divided into seven distinct geological and metaphysical trauma zones:\n\n")
    
    fissures_box = make_box("THE SEVEN FISSURE POINTS OF THE CHEONGULA", [
        "FISSURE LOCUS        | GEOLOGICAL FEATURE      | RESIDUAL PHENOMENON",
        "--------------------+-------------------------+----------------------",
        "Point 1: The Lip    | Gaping 300m Rim Crater  | Acoustic Resonance",
        "Point 2: Sluice Bed | Calcified Stone Steps   | Weeping River Source",
        "Point 3: Iron Basin | Crushed Tenement Slag   | Magnetic Static Field",
        "Point 4: Bone Grove | Needle-Glass Pillars    | Entity Nursery",
        "Point 5: The Throat | Vertical 800m Chasm     | Gravitational Weight",
        "Point 6: Deep Sump  | Boiling Liquid Han Well | High-Pressure Grief",
        "Point 7: The Heart  | Central Maw Nucleus     | The Thousand's Scream"
    ])
    sections.append(wrap_box(fissures_box))
    
    sections.append("These seven fissure points remain permanently classified. Under municipal law, entering within five hundred paces of Fissure Point 7 without a Level-5 Directorate clearance carries the immediate penalty of cognitive erasure.\n\n")
    sections.append('---\n\n')
    
    # Section VI: How the Five Institutions Bear the Scar
    sections.append("## Section VI: How the Five Institutions Bear the Scar\n\n")
    sections.append("The modern institutional framework of Somnarak exists as a direct psychological and mechanical defense against the horror of Year 202:\n\n")
    
    inst_scars_box = make_box("THE FIVE INSTITUTIONS & THEIR CHEONGULA TETHERS", [
        "INSTITUTION          | HISTORICAL TETHER       | OPERATIONAL BURDEN",
        "--------------------+-------------------------+----------------------",
        "Reverie Directorate | Floor 2 Dekan & Floor 6 | Contains Maw Entities",
        "SED Abyssal Corps   | Katabagil Passage 6     | Charts Sunken Quarry",
        "UCD Strike Force    | Katharcheok Operation 6 | Polices Zone B Fissure",
        "The Memory Archive  | Reception 6 (Lament)    | Preserves Lost Census",
        "The Horizon Caravan | Gate of Sighs Waystation| Escorts Fissure Exiles"
    ])
    sections.append(wrap_box(inst_scars_box))
    
    sections.append("### 6.1 The Reverie Directorate: Dekan & Marjuk\n\n")
    sections.append("- **Containment Lead Dekan:** Dekan's right arm was severed during an expedition into the Fissure bed forty years ago; the limb was replaced by fusing a living, crimson-scaled tendon harvested directly from the Maw's crystalline mantle. The scales pulse at the exact 432 Hz frequency of the thousand victims.\n")
    sections.append("- **Archive Lead Marjuk:** The sole surviving biological witness from Year 202. His living brain and optic nerve, preserved in stasis fluid within an armored effigy, whisper the names of the one thousand laborers during every REM cycle.\n")
    sections.append("- **Director Majin's Guilt:** The Director's 1,778 loops are an unyielding refusal to accept a universe built upon the forgotten sacrifice of Year 202. The **Absolvohan** is designed to release and transmute the thousand souls from their crystalline torment.\n\n")
    sections.append("### 6.2 The Other Wings\n\n")
    sections.append("- **The SED:** In Katabagil Passage 6 (**Traumagol**), the Bore Fleet discovered the petrified ruins of the original Zone B tenements suspended upside-down in the subterranean dark.\n")
    sections.append("- **The UCD:** In Katharcheok Operation 6 (**Basileugung**), the Strike Force breached the Underworld King's palace, discovering that the syndicate's throne was bolted directly over the bubbling vent of Fissure Point 5.\n")
    sections.append("- **The Memory Archive:** On the 6th Floor of the Spire (**Stratum of Lamentation**), Keeper Elyra guards the **Census of Year 202**—a book bound in ash that records every name, birth date, and unfulfilled dream of the thousand.\n")
    sections.append("- **The Horizon Caravan:** At Kilometer 0 before the Gate of Sighs, Kael established the **Cairn of the Unheard**—a stone monument where desert nomads leave copper coins before setting out across the sand.\n\n")
    sections.append('---\n\n')
    
    # Section VII: The Philosophical Inquest & The Dawn of Redemption
    sections.append("## Section VII: The Philosophical Inquest & The Dawn of Redemption\n\n")
    sections.append("The Cheongula poses the ultimate ethical question of Project Somnarak: **Can a civilization built upon the deliberate sacrifice of its weakest members ever truly be redeemed?**\n\n")
    sections.append("For four thousand years, the Council's answer was censorship, suppression, and debt. They taught the citizens to wear the Veil so they would not look down. They established the debt system so that sorrow could be bought and sold like grain.\n\n")
    sections.append("In Year 4,238, the **Dawn Accord** reversed this four-millennium doctrine. The five institutions have sworn to break the cycle:\n\n")
    
    redemption_box = make_box("SOVEREIGN CONVERGENCE: REDEMPTION OF THE FIRST SORROW", [
        "1. Truth Over Erasure    : The Census of Year 202 restored to public light.",
        "2. Transmutation of Pain: Absolvohan releases the thousand from the Maw.",
        "3. Dismantlement of Debt : Civic debt forgiven; usury frays eradicated.",
        "4. The Horizon Accord   : The city looks outward to a living world."
    ])
    sections.append(wrap_box(redemption_box))
    
    sections.append("The Cheongula was the moment humanity fell into the dark. The Dawn of Hope is the long, agonizing, magnificent climb back into the morning light.\n")
    
    return "".join(sections)

if __name__ == "__main__":
    content = build_codex()
    out_path = "SOMNARAK-WORLD/Master_Codices/01_Cosmology_and_World_Order/SOMNARAK_CHEONGULA.md"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("SOMNARAK_CHEONGULA.md expanded successfully!")
