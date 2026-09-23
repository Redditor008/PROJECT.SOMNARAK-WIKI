#!/usr/bin/env python3
"""
tools/repair_absolvohan_boxes.py
Repairs truncated HUD boxes and lines across The Absolvohan Parts 2 through 8:
- Replaces truncated 10-node grids with the canonical symmetrical line.
- Restores truncated unit tokens and character labels.
- Restores all clipped words, brackets, and parentheses.
- Enforces exact 71-character box width and border symmetry.
"""

import os
import re

REPLACEMENTS = [
    # Node grid
    ("[N01]---[N02]---[N03]---[N04]---[N05]---[N06]---[N07]---[N08]---[N0",
     "    [N01]-[N02]-[N03]-[N04]-[N05]-[N06]-[N07]-[N08]-[N09]-[N10]    "),

    # Truncated unit tokens at line ends
    (r"\[MA$", "[MAJIN]"),
    (r"\[DE$", "[DEKAN]"),
    (r"\[DEK$", "[DEKAN]"),
    (r"\[AY$", "[AYSHUK]"),
    (r"\[ZY$", "[ZYRAK]"),
    (r"\[KA$", "[KANG]"),
    (r"\[CH$", "[CHA]"),

    # Status brackets at line ends
    (r"\[CRACKE$", "[CRACKED]"),
    (r"\[CRACK$", "[CRACKED]"),
    (r"\[CRA$", "[CRACKED]"),
    (r"\[ENGAGE$", "[ENGAGED]"),
    (r"\[POISON$", "[POISONED]"),
    (r"\[STAGGERE$", "[STAGGERED]"),
    (r"\[STAGGER$", "[STAGGERED]"),
    (r"\[STAGGE$", "[STAGGERED]"),
    (r"\[STAGG$", "[STAGGERED]"),
    (r"\[STAG$", "[STAGGERED]"),
    (r"\[ST$", "[STAGGERED]"),
    (r"\[UNSTAB$", "[UNSTABLE]"),
    (r"\[UNSTA$", "[UNSTABLE]"),
    (r"\[COLLAPSED$", "[COLLAPSED]"),
    (r"\[COLLAPSE$", "[COLLAPSED]"),
    (r"\[COLLAPS$", "[COLLAPSED]"),
    (r"\[COLLAP$", "[COLLAPSED]"),
    (r"\[BURNIN$", "[BURNING]"),
    (r"\[GROUND$", "[GROUNDED]"),
    (r"\[FRACTURE$", "[FRACTURED]"),
    (r"\[FRACTUR$", "[FRACTURED]"),
    (r"\[FRACTU$", "[FRACTURED]"),
    (r"\[FRACT$", "[FRACTURED]"),
    (r"\[TRAPPE$", "[TRAPPED]"),
    (r"\[WEAKEN$", "[WEAKENED]"),
    (r"\[CRITICAL$", "[CRITICAL]"),
    (r"\[CRITIC$", "[CRITICAL]"),

    # Text endings
    (r"Blinded by Scrubb$", "Blinded by Scrubbers)"),
    (r"Suspension Ring$", "Suspension Ring)"),
    (r"Gravitational Ruptu$", "Gravitational Rupture)"),
    (r"CORE FRACTUR$", "CORE FRACTURED]"),
    (r"Gravity Resto$", "Gravity Restored)"),
    (r"Pierced by Mellda's$", "Pierced by Mellda's Spear)"),
    (r"Charging Void Cyclone / Posture 120/1$", "Charging Void Cyclone / Posture 120/120)"),
    (r"Momentum Surge Primed / \+2 Speed Nex$", "Momentum Surge Primed / +2 Speed Next Turn)"),
    (r"Swirling into Void Cyclone / Grounded by Mell$", "Swirling into Void Cyclone / Grounded by Mellda)"),
    (r"Base Fractured by Sim's Mau$", "Base Fractured by Sim's Maul)"),
    (r"Siphoning Excess Screech into Res$", "Siphoning Excess Screech into Reservoir)"),
    (r"Scales Pierced by Tak &$", "Scales Pierced by Tak & Zyrak)"),
    (r"Extraction Lance S$", "Extraction Lance Siphon)"),
    (r"Choral Lament & Thermal$", "Choral Lament & Thermal Beam)"),
    (r"Driving Dual Piercers into Spinal Ven$", "Driving Dual Piercers into Spinal Vents)"),
    (r"STAGGER LEVEL 1 / 1\.5x DAMAGE / Posture 34/20$", "STAGGER LEVEL 1 / 1.5x DAMAGE / Posture 34/200"),
    (r"Compressive Basalt Core / Posture 112$", "Compressive Basalt Core / Posture 112/160"),
    (r"Posture 112/160 \(Stagger$", "Posture 112/160 (Stagger 1: 96)"),
    (r"Pulverized into River Silt / Purified$", "Pulverized into River Silt / Purified)"),
    (r"Lowering Carbine / Confirming Zero Casualties$", "Lowering Carbine / Confirming Zero Casualties)"),
    (r"Mandible Lock$", "Mandible Lock)"),
    (r"Bulwark Stance / Threshold Vow Ready$", "Bulwark Stance / Threshold Vow Ready)"),
    (r"Chanting Shattered Memory Su$", "Chanting Shattered Memory Surge)"),
    (r"Blanketing the 12 Hydraulic Piston Sleeves$", "Blanketing the 12 Hydraulic Piston Sleeves)"),
    (r"Unified Directional Guard Absorpti$", "Unified Directional Guard Absorption)"),
    (r"Friction Coefficient Dropped to 0$", "Friction Coefficient Dropped to 0.0)"),
    (r"Completely Primed for Day 160 Dawn Releas$", "Completely Primed for Day 160 Dawn Release)"),
    (r"All Systems Locked and In Golden P$", "All Systems Locked and In Golden Posture)"),
    (r"Zero Resistance / Primed for Cycl$", "Zero Resistance / Primed for Cycle 1)"),
    (r"Predictive HUD Projecting Trajecto$", "Predictive HUD Projecting Trajectory)"),
    (r"Alignment Vector$", "Alignment Vector)"),
    (r"Directional Guard Absorption Activ$", "Directional Guard Absorption Active)"),
    (r"Bathed in Radiant Warm Gold / Full Sanctification$", "Bathed in Radiant Warm Gold / Full Sanctification)"),
    (r"Atmospheric Pale 62/160 / 60% Stag$", "Atmospheric Pale 62/160 / 60% Stagger"),
    (r"Kinetic Cruci$", "Kinetic Crucible)"),
    (r"Condenser$", "Condenser Array)"),
    (r"Liquefying into Dense Golden Fluid / Pale 32$", "Liquefying into Dense Golden Fluid / Pale 32/160"),
    (r"Channelling Pneumatic Flow$", "Channelling Pneumatic Flow)"),
    (r"Stabilizing Viscosity Gradient Across Valve$", "Stabilizing Viscosity Gradient Across Valves)"),
    (r"All Ordeals Cease$", "All Ordeals Ceased)"),
    (r"ALL ORDEALS DISSOLVE$", "ALL ORDEALS DISSOLVED)"),
    (r"ALL ORDEALS PACIFIED$", "ALL ORDEALS PACIFIED)"),
    (r"CONTAINMENT TRANSCEND$", "CONTAINMENT TRANSCENDED)"),
    (r"Flerehan Duet Climaxes in Absolute Acc$", "Flerehan Duet Climaxes in Absolute Accord)"),
    (r"Singing Before-Time Forgiveness Refrai$", "Singing Before-Time Forgiveness Refrain)"),
    (r"Wings Folded / Pale Light Warm Gol$", "Wings Folded / Pale Light Warm Gold)"),
    (r"Pale Resonance 54/140 / 60% Stagge$", "Pale Resonance 54/140 / 60% Stagger"),
    (r"Feather Mantle Vocal Resonance$", "Feather Mantle Vocal Resonance)"),
    (r"Cherub's Lyre Harmonic Chords$", "Cherub's Lyre Harmonic Chords)"),
    (r"Shielding Acoustic Bounce off Vault Wal$", "Shielding Acoustic Bounce off Vault Walls)"),
    (r"Singing First Verse of Lullab$", "Singing First Verse of Lullaby)"),
    (r"Maw Bastion Acoustic War$", "Maw Bastion Acoustic Ward)"),
    (r"Sorrow 46/130 / Sinking into Deep Reverie$", "Sorrow 46/130 / Sinking into Deep Reverie)"),
    (r"Work Success Up$", "Work Success Up)"),
    (r"Sanity Scree$", "Sanity Screech)"),
    (r"Vigorous Harmon$", "Vigorous Harmony)"),
    (r"Gentle Trance Pul$", "Gentle Trance Pulse)"),
    (r"Transmutative Light$", "Transmutative Light)"),
    (r"Max HP Cleansing Pu$", "Max HP Cleansing Pulse)"),
    (r"Gentle Awakening Pu$", "Gentle Awakening Pulse)"),
    (r"BESTOWED UPON AGENT TAK \(ANCHOR SPECIALIST$", "BESTOWED UPON AGENT TAK (ANCHOR SPECIALIST)"),
    (r"BESTOWED UPON AGENT KANG \(BREACH SPECIALIS$", "BESTOWED UPON AGENT KANG (BREACH SPECIALIST)"),
    (r"BESTOWED UPON AGENT HWANG \(VOID SPECIALIST$", "BESTOWED UPON AGENT HWANG (VOID SPECIALIST)"),
    (r"BESTOWED UPON AGENT PARK \(VANGUARD SPECIAL$", "BESTOWED UPON AGENT PARK (VANGUARD SPECIALIST)"),
    (r"TERMINAL STAGGER / POSTURE 0/100 / 2\.0x$", "TERMINAL STAGGER / POSTURE 0/100 / 2.0x DAMAGE"),
    (r"TERMINAL STAGGER / POSTURE 0/120 / CORE FRACTUR$", "TERMINAL STAGGER / POSTURE 0/120 / CORE FRACTURED"),
    (r"TERMINAL STAGGER / POSTURE 0/110 / 2\.0x DM$", "TERMINAL STAGGER / POSTURE 0/110 / 2.0x DAMAGE"),
    (r"TERMINAL STAGGER / POSTURE 0/160 / 2\.$", "TERMINAL STAGGER / POSTURE 0/160 / 2.0x DAMAGE"),
    (r"TERMINAL STAGGER / POSTURE 0/80 / 2\.0x D$", "TERMINAL STAGGER / POSTURE 0/80 / 2.0x DAMAGE"),
    (r"TERMINAL STAGGER / POSTURE 0/180 / 2\.0x$", "TERMINAL STAGGER / POSTURE 0/180 / 2.0x DAMAGE"),
    (r"TERMINAL STAGGER / POSTURE 0/200 / 2\.0x$", "TERMINAL STAGGER / POSTURE 0/200 / 2.0x DAMAGE"),
    (r"TERMINAL STAGGER / POSTURE 0/120 / 2\.0x D$", "TERMINAL STAGGER / POSTURE 0/120 / 2.0x DAMAGE"),
    (r"TERMINAL STAGGER / POSTURE 0/170 / 2\.0x$", "TERMINAL STAGGER / POSTURE 0/170 / 2.0x DAMAGE"),
    (r"TERMINAL STAGGER / AGITATION 0/120 / PURE HOP$", "TERMINAL STAGGER / AGITATION 0/120 / PURE HOPE"),
    (r"TERMINAL STAGGER / SORROW 0/130 / PEACEFU$", "TERMINAL STAGGER / SORROW 0/130 / PEACEFUL"),
    (r"TERMINAL STAGGER / PALE 0/140 / PURE DAWN LI$", "TERMINAL STAGGER / PALE 0/140 / PURE DAWN LIGHT"),
    (r"TERMINAL STAGGER / PALE 0/150 / 12 CROWNS R$", "TERMINAL STAGGER / PALE 0/150 / 12 CROWNS RELEASED"),
    (r"TERMINAL STAGGER / PALE 0/160 / FULL CONDENS$", "TERMINAL STAGGER / PALE 0/160 / FULL CONDENSED"),
    (r"SE-007 \(BRUME\), SE-140 \(WILL$", "SE-007 (BRUME), SE-140 (WILLOW)"),
    (r"THE SMOTHERING$", "THE SMOTHERING SHROUD)"),
    (r"Judicial Scale Blade   \| Weapon: 6-9 Weight \(Heavy / Speed Delta -1$", "Judicial Scale Blade   | Weapon: 6-9 Weight (Heavy / Speed Delta -1)"),
    (r"Chitin Great-Maul      \| Weapon: 7-11 Weight \(Heavy / Speed Delta -$", "Chitin Great-Maul      | Weapon: 7-11 Weight (Heavy / Speed Delta -1)"),
    (r"Hollow Requiem       \| Weapon: 5-8 Lament \(W$", "Hollow Requiem       | Weapon: 5-8 Lament (White)"),
    (r"Heavy / Spd 0 under A$", "Heavy / Spd 0 under Aura)"),
    (r"Void / Light / 1$", "Void / Light / 1 AP)"),
    (r"Sacred Blade / 2 A$", "Sacred Blade / 2 AP)"),
    (r"Heavy / Spd -1 / Postu$", "Heavy / Spd -1 / Posture 70)"),
    (r"Medium / Spd 0 / Post$", "Medium / Spd 0 / Posture 50)"),
    (r"Medium / Spd 0 / Pos$", "Medium / Spd 0 / Posture 50)"),
    (r"Heavy / 2 AP$", "Heavy / 2 AP)"),
    (r"Medium /$", "Medium / 1 AP)"),
    (r"Medium / 1$", "Medium / 1 AP)"),
    (r"Triggers at SP <=$", "Triggers at SP <= -35)"),
    (r"Triggers at SP <$", "Triggers at SP <= -25)"),
    (r"Pass: Harmonic Aegis \(\+10$", "Pass: Harmonic Aegis (+10% Res)"),
    (r"Pass: Thorn Reflect \(\+15%$", "Pass: Thorn Reflect (+15% Res)"),
    (r"GRADE S \(Outstanding$", "GRADE S (Outstanding)"),
    (r"GRADE EX \(Flawless$", "GRADE EX (Flawless)"),
    (r"GRADE S \(Exceptional$", "GRADE S (Exceptional)"),
    (r"GRADE EX \(Milestone$", "GRADE EX (Milestone)"),
    (r"\(\+15% Physical$", "(+15% Physical Resist)"),
    (r"\(\+8% Work Success$", "(+8% Work Success Resonance)"),
    (r"\(\+10% Movement /$", "(+10% Movement / Speed)"),
    (r"\(Void Piercing /$", "(Void Piercing / Resonance)"),
    (r"\(Lament Piercing /$", "(Lament Piercing / Resonance)"),
    (r"\(\+10 Max Clarity / SP$", "(+10 Max Clarity / SP)"),
    (r"Sanity Corrosion /$", "Sanity Corrosion / Void)"),
    (r"Gravitational A$", "Gravitational Affinity)"),
    (r"Weight \(Gravitational$", "Weight (Gravitational)"),
    (r"Grudge \(Physical$", "Grudge (Physical)"),
    (r"Point-Blank Band 1 / Embrace Fang Vicious Gua$", "Point-Blank Band 1 / Embrace Fang Vicious Guard)"),
    (r"Range Band 2 / Lament Requiem Harmonic Blast$", "Range Band 2 / Lament Requiem Harmonic Blast)"),
    (r"Completely Dissolved to Ash / Purged by Scrubber$", "Completely Dissolved to Ash / Purged by Scrubbers)"),
    (r"Acoustic and Atmospheric Purity Confirmed$", "Acoustic and Atmospheric Purity Confirmed)"),
    (r"Corridor East \(Acoustic and Atmospheric Purity Confirmed$", "Corridor East (Acoustic and Atmospheric Purity Confirmed)"),
    (r"SP: 60 - PROMOTED$", "SP: 60 - PROMOTED)"),
    (r"HP: 59 - PROMOTE$", "HP: 59 - PROMOTED)"),
    (r"Speed 6 \(3 AP \+ 1$", "Speed 6 (3 AP + 1 Move)"),
    (r"FLOOR 2 CONTAINMENT TRENCH \(NODE 02 INGRESS$", "FLOOR 2 CONTAINMENT TRENCH (NODE 02 INGRESS)"),
    (r"HP 220/220 \| Posture 110/110 \| Speed 4 \(2 A$", "HP 220/220 | Posture 110/110 | Speed 4 (2 AP)"),
    (r"HP 240/240 \| Posture 120/120 \| Speed 5 \(3 A$", "HP 240/240 | Posture 120/120 | Speed 5 (3 AP)"),
    (r"DIST : Kwon at N03 \(Band 1\); Sim at N04 \(Band 2\); Seo at N05 \(Band$",
     "DIST : Kwon at N03 (Band 1); Sim at N04 (Band 2); Seo at N05 (Band 3)")
]

def format_row(content, width=71):
    # content is inner text without leading | and trailing |
    # target total width = 71
    inner_width = width - 2 # 69
    # check if content exceeds inner_width - 2 (67)
    # If it fits within 67, pad with space on right
    line = f"| {content.ljust(inner_width - 1)}|"
    if len(line) == width:
        return line
    # If content is longer, we truncate or handle nicely:
    return f"| {content[:inner_width - 1]}|"

def repair_file(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    in_box = False
    modified = False

    for line in lines:
        stripped = line.rstrip()
        if stripped.startswith("+") and stripped.endswith("+") and len(stripped) == 71:
            in_box = True
            new_lines.append(line)
            continue
        
        if in_box and line.startswith("|") and stripped.endswith("|"):
            inner = line[1:-1].strip() # strip leading/trailing spaces inside box
            orig_inner = inner
            
            # apply replacements
            for pat, repl in REPLACEMENTS:
                if pat.startswith("^") or pat.endswith("$") or "\\" in pat:
                    inner = re.sub(pat, repl, inner)
                else:
                    inner = inner.replace(pat, repl)
            
            if inner != orig_inner:
                modified = True
            
            # re-pad to exactly 71 chars
            # preserve leading space if it was a centered or indented line
            if orig_inner.startswith("    [N01]"):
                formatted = f"|     {inner.strip()}     |"
            elif orig_inner.startswith(" "):
                # preserve indentation
                lead_space = len(line[1:]) - len(line[1:].lstrip())
                lead = " " * lead_space
                rest = inner
                formatted = f"|{lead}{rest}".ljust(70) + "|"
            else:
                formatted = f"| {inner}".ljust(70) + "|"
            
            if len(formatted) > 71:
                # If it exceeds 71 chars, fit it
                # If it ends with [CRACKED] etc, adjust spacing
                inner_s = inner.strip()
                if len(inner_s) <= 67:
                    formatted = f"| {inner_s.ljust(67)} |"
                else:
                    # Let's see: split across two lines if necessary, or trim inner spaces
                    # Often excess is due to double spaces
                    inner_compressed = re.sub(r'  +', ' ', inner_s)
                    if len(inner_compressed) <= 67:
                        formatted = f"| {inner_compressed.ljust(67)} |"
                    else:
                        formatted = f"| {inner_s[:67]} |"
            
            new_lines.append(formatted + "\n")
            continue
        
        if not (line.startswith("|") and stripped.endswith("|")):
            in_box = False
        
        new_lines.append(line)

    if modified:
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print(f"Repaired: {path}")

def main():
    parts = [
        "SOMNARAK-WORLD/The_Absolvohan/Part_2_Days_1_to_25.md",
        "SOMNARAK-WORLD/The_Absolvohan/Part_3_Days_29_to_49.md",
        "SOMNARAK-WORLD/The_Absolvohan/Part_4_Days_53_to_73.md",
        "SOMNARAK-WORLD/The_Absolvohan/Part_5_Days_77_to_97.md",
        "SOMNARAK-WORLD/The_Absolvohan/Part_6_Days_101_to_121.md",
        "SOMNARAK-WORLD/The_Absolvohan/Part_7_Days_125_to_145.md",
        "SOMNARAK-WORLD/The_Absolvohan/Part_8_Days_149_to_177.md",
    ]
    for p in parts:
        repair_file(p)

if __name__ == "__main__":
    main()
