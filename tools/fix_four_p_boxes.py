#!/usr/bin/env python3
"""
tools/fix_four_p_boxes.py
Replaces any crooked Four P-Framework boxes with the perfectly symmetrical 71-column version.
"""

import sys
import re

def make_box(title, raw_rows, width=71):
    top = "+" + "=" * (width - 2) + "+"
    div = "+" + "-" * (width - 2) + "+"
    bot = top
    out = [top]
    if title:
        t_pad = (width - 2 - len(title)) // 2
        t_line = "|" + " " * t_pad + title + " " * (width - 2 - len(title) - t_pad) + "|"
        out.append(t_line)
        out.append(div)

    for r in raw_rows:
        if r == "---":
            out.append(div)
        else:
            pad_len = width - 2 - 1 - len(r)
            out.append("| " + r + " " * pad_len + "|")
    out.append(bot)
    return "\n".join(out)

rows = [
    "Pillar Code | Tactical Domain     | Core Battle Function",
    "---",
    "P1: Passive | Weapon Trait Arts   | Speed triggers & range bonuses",
    "P2: Panic   | SP Breakdown & Loss | Burden drain, states & recovery",
    "P3: Parry   | Active Defense/Guard| Melee deflects & intercepts",
    "P4: Posture | Poise & Stagger Bar | Momentum math & dual breaks"
]
correct_box = make_box("THE FOUR P-FRAMEWORK (PASSIVE / PANIC / PARRY / POSTURE)", rows)

files = [
    "SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_BATTLE_SYSTEM.md",
    "SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_BATTLE_SYSTEM_STYLES.md",
    "SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_MAW_CODEX.md",
    "SOMNARAK-WORLD/The_Absolvohan/ABSOLOVHAN_OVERVIEW.md"
]

pattern = re.compile(r"\+\={69}\+\n\|\s*THE FOUR P-FRAMEWORK \(PASSIVE / PANIC / PARRY / POSTURE\)\s*\|\n[\s\S]*?\+\={69}\+", re.M)

for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content, count = pattern.subn(correct_box, content)
    if count > 0:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Replaced {count} instances in {fpath}")
    else:
        print(f"Pattern not found in {fpath}")
