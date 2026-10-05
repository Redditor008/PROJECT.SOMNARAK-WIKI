#!/usr/bin/env python3
"""
tools/purge_pm_vocabulary.py
Systematically purges all foreign Project Moon terminology across SOMNARAK-WORLD/ and tools/,
replacing with authentic in-universe Project Somnarak vocabulary.
"""

import os
import re

TEXT_REPLACEMENTS = [
    # Ordeal Watches
    (r"\bMidnight Ordeal\b", "Tide Watch Ordeal"),
    (r"\bNoon Ordeal\b", "Second Watch Ordeal"),
    (r"\bDusk Ordeal\b", "Third Watch Ordeal"),
    (r"\bDawn Ordeal\b", "First Watch Ordeal"),

    # Ordeal Colors
    (r"\bAmber Second Watch Ordeal\b", "Purple Second Watch Ordeal"),
    (r"\bAmber Third Watch Ordeal\b", "Black Third Watch Ordeal"),
    (r"\bCrimson Second Watch Ordeal\b", "Grey Second Watch Ordeal"),
    (r"\bCrimson Third Watch Ordeal\b", "Grey Third Watch Ordeal"),
    (r"\bViolet Second Watch Ordeal\b", "Purple Second Watch Ordeal"),
    (r"\bGreen Third Watch Ordeal\b", "Pale Third Watch Ordeal"),
    (r"\bViolet Third Watch Ordeal\b", "Purple Third Watch Ordeal"),
    (r"\bGreen or Amber First Watch Ordeal\b", "Pale or Black First Watch Ordeal"),

    # Entity Ranks & Tiers
    (r"\(WAW and ALEPH grades\)", "(Rank IV Entity and Rank V Sovereign grades)"),
    (r"\(WAW and ALEPH tiers\)", "(Rank IV Entity and Rank V Sovereign tiers)"),
    (r"captured Rank IV Entity and Rank V Sovereign entities", "captured Rank IV Entity and Rank V Sovereign entities"),
    (r"Rank IV Entity Matrix", "Rank IV Entity Matrix"),
    (r"Rank V Sovereign Outbreak", "Rank V Sovereign Outbreak"),
    (r"Grade-γ stones", "Grade-γ stones"),
    (r"\(TETH/HE Contraband Sorrow Entity\)", "(Rank II/III Contraband Sorrow Entity)"),
    (r"\(TETH-grade\)", "(Rank II Echo)"),
    (r"Rank II (Echo) and Rank I (Residue) grade fragments", "Rank II (Echo) and Rank I (Residue) grade fragments"),
    (r"Rank II and Rank I grade", "Rank II and Rank I grade"),
    (r"Appears safe — Rank I Residue level", "Appears safe — Rank I Residue level"),
    (r"Risk increases — Rank II Echo level", "Risk increases — Rank II Echo level"),
    (r"Danger rises — Rank III Fragment level", "Danger rises — Rank III Fragment level"),
    (r"Rank V Sovereign equivalent", "Rank V Sovereign equivalent"),
    (r"high-tier \(HE, WAW, ALEPH\)", "high-tier (Rank III Fragment, Rank IV Entity, Rank V Sovereign)"),
    (r"Tiers: `I` \(ZAYIN\), `II` \(TETH\), `III` \(HE\), `IV` \(WAW\), `V` \(ALEPH\)",
     "Coherence Ranks: `I` (Residue / 잔여물), `II` (Echo / 메아리), `III` (Fragment / 파편), `IV` (Entity / 존재), `V` (Sovereign / 군주)"),
    (r"`I` \(\*\*ZAYIN\*\*\): Negligible or passive threat", "`I` (**Rank I: Residue / 잔여물**): Negligible or passive threat"),
    (r"`II` \(\*\*TETH\*\*\): Low-to-moderate threat", "`II` (**Rank II: Echo / 메아리**): Low-to-moderate threat"),
    (r"`III` \(\*\*HE\*\*\): Significant threat", "`III` (**Rank III: Fragment / 파편**): Significant threat"),
    (r"`IV` \(\*\*WAW\*\*\): Critical threat", "`IV` (**Rank IV: Entity / 존재**): Critical threat"),
    (r"`V` \(\*\*ALEPH\*\*\): Catastrophic existential threat", "`V` (**Rank V: Sovereign / 군주**): Catastrophic existential threat"),
]

def purge_file(path):
    # Exclude the comparative integrity audit which legitimately analyzes PM terms
    if "SOMNARAK_PM_COMPARATIVE_INTEGRITY_AUDIT.md" in path:
        return False

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    orig = content
    for pattern, repl in TEXT_REPLACEMENTS:
        content = re.sub(pattern, repl, content)

    if content != orig:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False

def main():
    modified = []
    for root, dirs, files in os.walk("SOMNARAK-WORLD"):
        for f in sorted(files):
            if f.endswith(".md"):
                p = os.path.join(root, f)
                if purge_file(p):
                    modified.append(p)

    for root, dirs, files in os.walk("tools"):
        for f in sorted(files):
            if f.endswith(".py"):
                p = os.path.join(root, f)
                if purge_file(p):
                    modified.append(p)

    print(f"Purged PM vocabulary from {len(modified)} files.")

if __name__ == "__main__":
    main()
