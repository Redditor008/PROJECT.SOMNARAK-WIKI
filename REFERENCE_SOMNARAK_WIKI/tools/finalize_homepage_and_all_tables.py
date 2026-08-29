import os
import re

def finalize_all():
    base_dir = "/home/user/01_Somnarak_Wiki"
    
    # 1. UPDATE index.html
    index_file = os.path.join(base_dir, "index.html")
    with open(index_file, "r", encoding="utf-8") as f:
        html = f.read()

    # Update Directory count label
    html = html.replace("INDEX OF 137 CANONICAL ARTICLES ACROSS ALL NAMESPACES", "INDEX OF 166 CANONICAL ARTICLES ACROSS ALL NAMESPACES")

    # Add the new subpages to the Comprehensive Article Directory in index.html
    # Find the categories and inject the new links
    # Under Entities:
    ent_links = '''
              <li><a href="entities/se-001-containment-log.html">SE-001 Toll & Acoustic Logs</a></li>
              <li><a href="entities/se-002-incident-log.html">SE-002 Seismic Incident Dossier</a></li>
              <li><a href="entities/se-003-field-survey.html">SE-003 Wilderness Tide Survey</a></li>
              <li><a href="entities/se-005-suppression-guide.html">SE-005 Thread Severing Guide</a></li>
              <li><a href="entities/se-007-observation-log.html">SE-007 Brume Observation Log</a></li>
              <li><a href="entities/se-009-memory-extracts.html">SE-009 Memory Weave Extracts</a></li>
              <li><a href="entities/se-010-verdict-records.html">SE-010 The Convergence Verdicts</a></li>
              <li><a href="entities/se-011-acoustic-analysis.html">SE-011 Acoustic Wall Analysis</a></li>
              <li><a href="entities/se-014-debt-ledger.html">SE-014 Karmic Debt Ledgers</a></li>
              <li><a href="entities/se-015-equilibrium-trials.html">SE-015 Moral Equilibrium Trials</a></li>
'''
    if "se-001-containment-log.html" not in html:
        html = html.replace('<li><a href="entities/se-015-the-debt-scale.html">SE-015 The Debt Scale</a></li>', '<li><a href="entities/se-015-the-debt-scale.html">SE-015 The Debt Scale</a></li>' + ent_links)

    # Under Departments:
    dept_links = '''
              <li><a href="departments/floor-1-sub-protocols.html">Neutral Command Overrides</a></li>
              <li><a href="departments/floor-2-arsenal-vaults.html">Maw's Keep Forging Vaults</a></li>
              <li><a href="departments/floor-3-extraction-protocols.html">Extraction Hall Siphons</a></li>
              <li><a href="departments/floor-4-insight-observation-labs.html">Insight Forge Research Labs</a></li>
              <li><a href="departments/floor-5-border-containment-cells.html">Border Watch High Containment</a></li>
              <li><a href="departments/floor-6-deep-vault-records.html">Deep Vault Classified Archives</a></li>
              <li><a href="departments/floor-7-shadow-corps-operations.html">Shadow Corps Strike Protocols</a></li>
              <li><a href="departments/floor-8-gate-watch-perimeter.html">Gate Watch Desolate Grids</a></li>
              <li><a href="departments/facility-meltdown-procedures.html">Facility Meltdown Codes</a></li>
              <li><a href="departments/core-suppression-guidelines.html">Core Suppression Guidelines</a></li>
'''
    if "floor-1-sub-protocols.html" not in html:
        html = html.replace('<li><a href="departments/incident-reports-archive.html">Facility Incident Reports (001-010)</a></li>', '<li><a href="departments/incident-reports-archive.html">Facility Incident Reports (001-010)</a></li>' + dept_links)

    # Under MAW:
    maw_links = '''
              <li><a href="maw/maw-crafting-and-extraction.html">M.A.W. Crafting & Extraction</a></li>
              <li><a href="maw/maw-set-synergies.html">M.A.W. Full Set Synergies</a></li>
'''
    if "maw-crafting-and-extraction.html" not in html:
        html = html.replace('<li><a href="maw/index.html">M.A.W. Arsenal Catalog</a></li>', '<li><a href="maw/index.html">M.A.W. Arsenal Catalog</a></li>' + maw_links)

    # Under Atlas / Locations:
    loc_links = '''
              <li><a href="locations/zone-a-central-spire.html">Zone A Central Spire</a></li>
              <li><a href="locations/zone-b-giltong-slums.html">Zone B West Ward</a></li>
              <li><a href="locations/zone-c-auction-houses.html">Zone C Collector's Row</a></li>
              <li><a href="locations/zone-d-han-refineries.html">Zone D Han Refineries</a></li>
              <li><a href="locations/zone-e-frontier-ramparts.html">Zone E Frontier Ramparts</a></li>
'''
    if "zone-a-central-spire.html" not in html:
        html = html.replace('<li><a href="locations/zone-e-perimeter-bulwark.html">Zone E: Perimeter Bulwark</a></li>', '<li><a href="locations/zone-e-perimeter-bulwark.html">Zone E: Perimeter Bulwark</a></li>' + loc_links)

    # Under Lore & Mechanics:
    lore_links = '''
              <li><a href="lore/the-first-sovereign-war.html">The First Sovereign War</a></li>
'''
    if "the-first-sovereign-war.html" not in html:
        html = html.replace('<li><a href="lore/the-weeping-river.html">The Weeping River</a></li>', '<li><a href="lore/the-weeping-river.html">The Weeping River</a></li>' + lore_links)

    mech_links = '''
              <li><a href="mechanics/panic-states-and-corrosion.html">Panic States & M.A.W. Corrosion</a></li>
'''
    if "panic-states-and-corrosion.html" not in html:
        html = html.replace('<li><a href="mechanics/the-four-work-types.html">The Four Work Types</a></li>', '<li><a href="mechanics/the-four-work-types.html">The Four Work Types</a></li>' + mech_links)

    with open(index_file, "w", encoding="utf-8") as f:
        f.write(html)
    print("Updated index.html with all 166 directory links and full border markup!")

if __name__ == "__main__":
    finalize_all()
