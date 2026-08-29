#!/usr/bin/env python3
"""
tools/purge_foreign_vocabulary.py
Scans and completely replaces all non-Somnarak / L-Corp / Lobotomy / Project Moon
vocabulary across all HTML, CSS, JS, and SVG files with 100% pure canonical Somnarak terms.
"""

import os, re, glob

WIKI_DIR = "/home/user/01_Somnarak_Wiki"

# Define canonical term replacements
REPLACEMENTS = [
    # Qliphoth replacements
    (r"\bQliphoth frequency counters\b", "Coherence resonance counters"),
    (r"\bQliphoth frequency modulators\b", "Coherence flux modulators"),
    (r"\bQliphoth frequency\b", "Coherence frequency"),
    (r"\bQliphoth counters\b", "Coherence counters"),
    (r"\bQliphoth counter\b", "Coherence counter"),
    (r"\bQliphoth\b", "Coherence Flux"),
    (r"\bLIVE QLIPHOTH SENSOR CONSOLE\b", "LIVE COHERENCE FLUX CONSOLE"),
    (r"\bqliphoth\b", "coherence"),

    # L-Corp and Lobotomy replacements
    (r"\bL-Corp Authentic Industrial Right Rail\b", "Directorate Industrial Sector Console"),
    (r"\bL-Corp Authentic Right Rail\b", "Directorate Sector Console"),
    (r"\bL-Corp Header\b", "Directorate Header"),
    (r"\bL-Corp Tactical Hazard Buttons\b", "Directorate Sector Access Controls"),
    (r"\bL-Corp Heavy Action Buttons\b", "Directorate Command Action Controls"),
    (r"\bL-Corp 72px Tall Hazard Buttons\b", "Directorate Sector Access Controls"),
    (r"\bAuthentic L-Corp\b", "Authentic Directorate"),
    (r"\bL-Corp\b", "The Reverie Directorate"),
    (r"\bL-CORP\b", "DIRECTORATE"),
    (r"\bLobotomy Corporation\b", "The Reverie Directorate"),
    (r"\bLobotomy\b", "Somnarak Containment"),

    # Abnormalities / E.G.O replacements
    (r"\bAbnormalities\b", "Sorrow Entities"),
    (r"\bAbnormality\b", "Sorrow Entity"),
    (r"\bE\.G\.O Equipment\b", "M.A.W. Equipment"),
    (r"\bE\.G\.O Arsenal\b", "M.A.W. Arsenal"),
    (r"\bE\.G\.O\b", "M.A.W."),

    # Other franchise terms
    (r"\bLimbus\b", "The Frontier Expedition"),
    (r"\bRuina\b", "The Great Collapse"),
    (r"\bAngela\b", "The Central Automaton"),
]

def purge_files():
    all_files = glob.glob(os.path.join(WIKI_DIR, "**/*.*"), recursive=True)
    modified_count = 0

    for file_path in all_files:
        ext = os.path.splitext(file_path)[1].lower()
        if ext not in [".html", ".css", ".js", ".svg", ".json", ".csv"]:
            continue

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception:
            continue

        orig = content

        # Special handling for founding corporations comparison table
        if "the-founding-corporations.html" in file_path:
            # Replace comparative table rows with pure Somnarak corporate history
            content = re.sub(
                r'<p><strong>Game Style:</strong>\s*Lobotomy Corporation[^\n<]*</p>',
                '<p><strong>Operational Focus:</strong> Subterranean Containment & Han Stabilization</p>',
                content
            )
            content = re.sub(
                r'<tr><td><strong>Company</strong></td><td>Lobotomy Corporation</td><td>.*?</td></tr>',
                '<tr><td><strong>Governing Body</strong></td><td>Founding Consortium</td><td><span><a class="wiki-link" href="../factions/the-reverie-directorate.html">The Reverie Directorate</a></span></td></tr>',
                content
            )
            content = re.sub(
                r'<tr><td><strong>Entities</strong></td><td>Abnormalities</td><td>.*?</td></tr>',
                '<tr><td><strong>Classified Phenomenon</strong></td><td>Agony Manifestations</td><td><span><a class="wiki-link" href="../entities/index.html">Sorrow Entities</a> (246 Cataloged)</span></td></tr>',
                content
            )
            content = re.sub(
                r'<tr><td><strong>Energy</strong></td><td>Qliphoth</td><td>Han-crystal</td></tr>',
                '<tr><td><strong>Power Singularity</strong></td><td>Han Flux Resonance</td><td><span>Crystallized Han & Agony Siphons</span></td></tr>',
                content
            )
            content = re.sub(
                r'<tr><td><strong>Equipment</strong></td><td>E\.G\.O</td><td>.*?</td></tr>',
                '<tr><td><strong>Combat Armament</strong></td><td>Resonance Forged Gear</td><td><span><a class="wiki-link" href="../maw/index.html">M.A.W. Systems</a> (Weapons, Suits, Gifts)</span></td></tr>',
                content
            )
            content = re.sub(
                r'<tr><td><strong>Facility Core</strong></td><td>Angela</td><td>.*?</td></tr>',
                '<tr><td><strong>Administrative Core</strong></td><td>Executive AI Subsystem</td><td><span><a class="wiki-link" href="../characters/the-director-majin.html">Director Majin</a> & <a class="wiki-link" href="../characters/the-secretary-seiyon.html">Secretary Seiyon</a></span></td></tr>',
                content
            )

        # Apply regex replacements
        for pattern, replacement in REPLACEMENTS:
            content = re.sub(pattern, replacement, content)

        if content != orig:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            modified_count += 1
            print(f"Purged foreign terms in: {os.path.relpath(file_path, WIKI_DIR)}")

    print(f"\nTotal files updated with pure Somnarak vocabulary: {modified_count}")

if __name__ == "__main__":
    purge_files()
