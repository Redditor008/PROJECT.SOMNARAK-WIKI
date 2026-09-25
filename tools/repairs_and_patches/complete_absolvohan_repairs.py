#!/usr/bin/env python3
"""
tools/complete_absolvohan_repairs.py
Exhaustively resolves all unclosed brackets, parentheses, and sliced words
in The Absolvohan Parts 2 through 8 text boxes.
"""

import os
import re

BRACKET_MAP = {
    '[60% STAGGER TRIGG': '[60% STAGGER TRIGGERED]',
    '[60% STAGGER TRIGGERE': '[60% STAGGER TRIGGERED]',
    '[ALL-AGENTS': '[ALL-AGENTS]',
    '[AY': '[AYSHUK]',
    '[BURNIN': '[BURNING]',
    '[COLLAP': '[COLLAPSED]',
    '[COLLAPS': '[COLLAPSED]',
    '[COLLAPSE': '[COLLAPSED]',
    '[COLLAPSED': '[COLLAPSED]',
    '[CRA': '[CRACKED]',
    '[CRACK': '[CRACKED]',
    '[CRACKE': '[CRACKED]',
    '[CRACKED': '[CRACKED]',
    '[CRITIC': '[CRITICAL]',
    '[CRITICA': '[CRITICAL]',
    '[CRITICAL': '[CRITICAL]',
    '[DE': '[DEKAN]',
    '[DEK': '[DEKAN]',
    '[ENGAGE': '[ENGAGED]',
    '[ENGAGED': '[ENGAGED]',
    '[FRACTU': '[FRACTURED]',
    '[FRACTURE': '[FRACTURED]',
    '[FROZEN': '[FROZEN]',
    '[GROUND': '[GROUNDED]',
    '[IS': '[ISHALL]',
    '[M': '[MAJIN]',
    '[MA': '[MAJIN]',
    '[MAJ': '[MAJIN]',
    '[MELTING': '[MELTING]',
    '[OVERHEA': '[OVERHEATED]',
    '[PINNE': '[PINNED]',
    '[PINNED': '[PINNED]',
    '[POISON': '[POISONED]',
    '[STAGG': '[STAGGERED]',
    '[STAGGE': '[STAGGERED]',
    '[STAGGER': '[STAGGERED]',
    '[STAGGERE': '[STAGGERED]',
    '[STALLE': '[STALLED]',
    '[TRAPPE': '[TRAPPED]',
    '[TRAPPED': '[TRAPPED]',
    '[UNSTA': '[UNSTABLE]',
    '[UNSTAB': '[UNSTABLE]',
    '[WEAKEN': '[WEAKENED]',
    '[ZY': '[ZYRAK]',
}

PAREN_MAP = {
    '(% Max HP Decay Puls': '(% Max HP Decay Pulse)',
    '(+10 All Work Speeds &': '(+10 All Work Speeds)',
    '(+10 Max Clarity / SP': '(+10 Max Clarity / SP)',
    '(+10': '(+10% Han Extract)',
    '(+10% Han Extract': '(+10% Han Extract)',
    '(+10% Movement /': '(+10% Movement / Speed)',
    '(+10% Physical Defense': '(+10% Physical Defense)',
    '(+15% Evasion / Move': '(+15% Evasion / Movement)',
    '(+15% Physical': '(+15% Physical Resist)',
    '(+15% Physical Grudge': '(+15% Physical Grudge)',
    '(+15% SP Damage': '(+15% SP Damage)',
    '(+15% Void Damage': '(+15% Void Damage)',
    '(+15%': '(+15% Physical Resist)',
    '(+20% M.A.W. Attack': '(+20% M.A.W. Attack)',
    '(+8% Work Success': '(+8% Work Success Resonance)',
    '(2 A': '(2 AP)',
    '(3 A': '(3 AP)',
    '(3 AP + 1': '(3 AP + 1 Move)',
    '(3 AP Bas': '(3 AP Base)',
    '(4 AP Bas': '(4 AP Base)',
    '(85dB Sanity Scree': '(85dB Sanity Screech)',
    '(ALL ORDEALS DISSOLVE': '(ALL ORDEALS DISSOLVED)',
    '(ALL ORDEALS PACIFIED': '(ALL ORDEALS PACIFIED)',
    '(ANCHOR SPECIALIST': '(ANCHOR SPECIALIST)',
    '(Acoustic and Atmospheric Purity Confirmed': '(Acoustic and Atmospheric Purity Confirmed)',
    '(All Ordeals Cease': '(All Ordeals Ceased)',
    '(All Systems Locked and In Golden P': '(All Systems Locked and In Golden Posture)',
    '(Atmospheric Pale 62/160 / 60% Stag': '(Atmospheric Pale 62/160 / 60% Stagger)',
    '(Ayshuk, Mellda, Marjuk, Ishall / Condenser': '(Ayshuk, Mellda, Marjuk, Ishall / Condenser)',
    '(BREACH SPECIALIS': '(BREACH SPECIALIST)',
    '(Band': '(Band 3)',
    '(Bathed in Radiant Warm Gold / Full Sanctification': '(Bathed in Radiant Warm Gold / Full Sanctification)',
    '(Bedrock Anchor': '(Bedrock Anchor)',
    '(Blanketing the 12 Hydraulic Piston Sleeves': '(Blanketing the 12 Hydraulic Piston Sleeves)',
    '(Bulwark Shield / Threshold Vow Ready': '(Bulwark Shield / Threshold Vow Ready)',
    '(Bulwark Stance / Threshold Vow Ready': '(Bulwark Stance / Threshold Vow Ready)',
    '(CONTAINMENT TRANSCEND': '(CONTAINMENT TRANSCENDED)',
    '(Charging Global Sanity Vortex / Posture': '(Charging Global Sanity Vortex / Posture 150/150)',
    '(Charging Kinetic Piston / Posture 120': '(Charging Kinetic Piston / Posture 120/120)',
    '(Charging Subterranean Sunder / Posture': '(Charging Subterranean Sunder / Posture 160/160)',
    '(Charging Void Cyclone / Posture 120/1': '(Charging Void Cyclone / Posture 120/120)',
    '(Completely Dissolved to Ash / Purged by Scrubber': '(Completely Dissolved to Ash / Purged by Scrubbers)',
    '(Completely Primed for Day 160 Dawn Releas': '(Completely Primed for Day 160 Dawn Release)',
    '(Compressive Basalt Core / Posture 112': '(Compressive Basalt Core / Posture 112/160)',
    '(Cooled into Inert Obsidian Glass / Sipho': '(Cooled into Inert Obsidian Glass / Siphoned)',
    '(Detonated Safely / Slag Siphoned into Flues': '(Detonated Safely / Slag Siphoned into Flues)',
    '(Detonated inside Stasis Vault / 0 Casua': '(Detonated inside Stasis Vault / 0 Casualties)',
    '(Directional Guard Absorption / Freezing Nodes': '(Directional Guard Absorption / Freezing Nodes)',
    '(Directional Guard Absorption Act': '(Directional Guard Absorption Active)',
    '(Directional Guard Absorption Activ': '(Directional Guard Absorption Active)',
    '(Disintegrated into White Ash / Siphoned': '(Disintegrated into White Ash / Siphoned)',
    '(Dissecting Heart Core with Relic Digits': '(Dissecting Heart Core with Relic Digits)',
    '(Dissolved into Amber Crystals / Siphone': '(Dissolved into Amber Crystals / Siphoned)',
    '(Dissolved into Crimson Vapor / Siphoned': '(Dissolved into Crimson Vapor / Siphoned)',
    '(Dissolved into Pure Living Crystalline Wa': '(Dissolved into Pure Living Crystalline Water)',
    '(Dissolved into Radiant White Light / Siphon': '(Dissolved into Radiant White Light / Siphoned)',
    '(Dissolved to Starlight & Han Vapor / Siphone': '(Dissolved to Starlight & Han Vapor / Siphoned)',
    '(Driving Arm-Blade into Ventral Shell': '(Driving Arm-Blade into Ventral Shell)',
    '(Driving Dual Piercers into Spinal Ven': '(Driving Dual Piercers into Spinal Vents)',
    '(Exceptional': '(Exceptional)',
    '(Flawless': '(Flawless)',
    '(Flerehan Duet Climaxes in Absolute Acc': '(Flerehan Duet Climaxes in Absolute Accord)',
    '(Freezing Vertebrae with Stasis Fiel': '(Freezing Vertebrae with Stasis Field)',
    '(Friction Coefficient Dropped to 0': '(Friction Coefficient Dropped to 0.0)',
    '(GATE WATCH LE': '(GATE WATCH LEAD)',
    '(Gentle Awakening Pu': '(Gentle Awakening Pulse)',
    '(Gentle Trance Pul': '(Gentle Trance Pulse)',
    '(Gravitational': '(Gravitational)',
    '(Gravitational A': '(Gravitational Affinity)',
    '(Grudge / Heavy / 2 A': '(Grudge / Heavy / 2 AP)',
    '(Grudge / Heavy / 2 AP': '(Grudge / Heavy / 2 AP)',
    '(Grudge / Medium /': '(Grudge / Medium / 1 AP)',
    '(Grudge / Medium / 1': '(Grudge / Medium / 1 AP)',
    '(HP: 59 - PROMOTE': '(HP: 59 - PROMOTED)',
    '(Heals 2 SP': '(Heals 2 SP)',
    '(Heavy / Spd -1 / Postu': '(Heavy / Spd -1 / Posture 70)',
    '(Heavy / Spd 0 under A': '(Heavy / Spd 0 under Aura)',
    '(Heavy / Spd 0 under': '(Heavy / Spd 0 under Aura)',
    '(Heavy / Speed Delta -': '(Heavy / Speed Delta -1)',
    '(Heavy / Speed Delta -1': '(Heavy / Speed Delta -1)',
    '(High-Velocity': '(High-Velocity)',
    '(Hydraulic Pressure Clamp Engaged': '(Hydraulic Pressure Clamp Engaged)',
    '(Lament / Medium /': '(Lament / Medium / 1 AP)',
    '(Lament Piercing /': '(Lament Piercing / Resonance)',
    '(Line Anchor / Judgment Scale Raised / Band 2': '(Line Anchor / Judgment Scale Raised / Band 2)',
    '(Liquefying into Dense Golden Fluid / Pale 32': '(Liquefying into Dense Golden Fluid / Pale 32/160)',
    '(Lowering Carbine / Confirming Zero Casualties': '(Lowering Carbine / Confirming Zero Casualties)',
    '(Majin, Seiyon, Dekan, Zyrak / Kinetic Cruci': '(Majin, Seiyon, Dekan, Zyrak / Kinetic Crucible)',
    '(Max HP Cleansing Pu': '(Max HP Cleansing Pulse)',
    '(Medium / Spd +1 under': '(Medium / Spd +1 under Aura)',
    '(Medium / Spd 0 / Pos': '(Medium / Spd 0 / Posture 50)',
    '(Medium / Spd 0 / Post': '(Medium / Spd 0 / Posture 50)',
    '(Milestone': '(Milestone)',
    '(Momentum Surge / Alignment Vector': '(Momentum Surge / Alignment Vector)',
    '(Momentum Surge / Channelling Pneumatic Flow': '(Momentum Surge / Channelling Pneumatic Flow)',
    '(Momentum Surge Primed / +2 Speed Nex': '(Momentum Surge Primed / +2 Speed Next Turn)',
    '(Momentum Surge Primed / +2 Speed Next T': '(Momentum Surge Primed / +2 Speed Next Turn)',
    '(Momentum Surge Primed / Repositioning to Nod': '(Momentum Surge Primed / Repositioning to Node)',
    '(NODE 02 INGRESS': '(NODE 02 INGRESS)',
    '(Outstanding': '(Outstanding)',
    '(Pale Resonance 54/140 / 60% Stagge': '(Pale Resonance 54/140 / 60% Stagger)',
    '(Physical': '(Physical)',
    '(Point-Blank Band 1 / Basalt Great-Maul Cleav': '(Point-Blank Band 1 / Basalt Great-Maul Cleave)',
    '(Point-Blank Band 1 / Cleaving Segment Joints': '(Point-Blank Band 1 / Cleaving Segment Joints)',
    '(Point-Blank Band 1 / Embrace Fang Vicious Gua': '(Point-Blank Band 1 / Embrace Fang Vicious Guard)',
    '(Point-Blank Band 1 / Smashing Crystalline Ba': '(Point-Blank Band 1 / Smashing Crystalline Base)',
    '(Point-Blank Band 1 / Warhammer Cleave Landed': '(Point-Blank Band 1 / Warhammer Cleave Landed)',
    '(Posture 114/180 / Anterior Shell Fissure': '(Posture 114/180 / Anterior Shell Fissure)',
    '(Posture 124/200 / Anterior Shell Crac': '(Posture 124/200 / Anterior Shell Crack)',
    '(Posture 130/200 / Mandible Lock': '(Posture 130/200 / Mandible Lock)',
    '(Posture 42/100 / Optical Focal Aperture Severed': '(Posture 42/100 / Optical Focal Aperture Severed)',
    '(Posture 44/120 / Feeder Tendrils Severed by No': '(Posture 44/120 / Feeder Tendrils Severed by Node)',
    "(Posture 44/130 / Base Fractured by Sim's Mau": "(Posture 44/130 / Base Fractured by Sim's Maul)",
    "(Posture 46/120 / Pierced by Mellda's": "(Posture 46/120 / Pierced by Mellda's Spear)",
    '(Posture 48/120 / Suspension Ring': '(Posture 48/120 / Suspension Ring)',
    '(Posture 52/130 / Scythe Blade Blocked by Kang': '(Posture 52/130 / Scythe Blade Blocked by Kang)',
    '(Posture 54/140 / Carapace Fractured by Kan': '(Posture 54/140 / Carapace Fractured by Kang)',
    '(Posture 56/120 / Base Drive Fractured': '(Posture 56/120 / Base Drive Fractured)',
    '(Posture 68/140 / Spectral Mantle Pierce': '(Posture 68/140 / Spectral Mantle Pierced)',
    '(Posture 76/200 / Scales Pierced by Tak &': '(Posture 76/200 / Scales Pierced by Tak & Zyrak)',
    '(Posture 84/180 / Dimensional Matrix Fractur': '(Posture 84/180 / Dimensional Matrix Fractured)',
    '(Predicting Refraction Angles / Ban': '(Predicting Refraction Angles / Band 3)',
    '(Predictive HUD Projecting Trajecto': '(Predictive HUD Projecting Trajectory)',
    '(Preparing Pincer Charge / Posture 90/90': '(Preparing Pincer Charge / Posture 90/90)',
    '(Pulverized into River Silt / Purified': '(Pulverized into River Silt / Purified)',
    '(Range Band 2 / Blessed Scalpel Optical Stri': '(Range Band 2 / Blessed Scalpel Optical Strike)',
    "(Range Band 2 / Cherub's Lyre Harmonic Chords": "(Range Band 2 / Cherub's Lyre Harmonic Chords)",
    '(Range Band 2 / Extraction Lance S': '(Range Band 2 / Extraction Lance Siphon)',
    '(Range Band 2 / Feather Mantle Vocal Resonance': '(Range Band 2 / Feather Mantle Vocal Resonance)',
    '(Range Band 2 / Lament Requiem Harmonic Blast': '(Range Band 2 / Lament Requiem Harmonic Blast)',
    '(Range Band 2 / Maw Bastion Acoustic War': '(Range Band 2 / Maw Bastion Acoustic Ward)',
    '(Range Band 2 / Singing First Verse of Lullab': '(Range Band 2 / Singing First Verse of Lullaby)',
    '(Range Band 3 / Choral Lament & Thermal': '(Range Band 3 / Choral Lament & Thermal Beam)',
    '(Range Band 3 / Heavy Maul Ready to Intercept': '(Range Band 3 / Heavy Maul Ready to Intercept)',
    '(Rear Infiltration / Void Talons Readied': '(Rear Infiltration / Void Talons Readied)',
    '(Recovered / Channeling 20% Max HP Pale Pulse': '(Recovered / Channeling 20% Max HP Pale Pulse)',
    '(Recovered / Channeling 3.2G Gravitational Ruptu': '(Recovered / Channeling 3.2G Gravitational Rupture)',
    '(Recovered / Channeling Ancient Ballast Quak': '(Recovered / Channeling Ancient Ballast Quake)',
    '(Recovered / Channeling Mudslide Erupt': '(Recovered / Channeling Mudslide Eruption)',
    '(Recovered / Channeling Thermal Super-Torque': '(Recovered / Channeling Thermal Super-Torque)',
    '(Recovered / Chanting Shattered Memory Su': '(Recovered / Chanting Shattered Memory Surge)',
    '(Recovered / Charging Global Void Death-Ra': '(Recovered / Charging Global Void Death-Ray)',
    '(SP: 60 - PROMOTED': '(SP: 60 - PROMOTED)',
    '(STAGGER LEVEL 1 / 1.5x DAMAGE / Posture 34/20': '(STAGGER LEVEL 1 / 1.5x DAMAGE / Posture 34/200)',
    '(Sacred Blade / 2 A': '(Sacred Blade / 2 AP)',
    '(Sanity Corrosion /': '(Sanity Corrosion / Void)',
    '(Shattered into Prismatic Glass & Han Mist': '(Shattered into Prismatic Glass & Han Mist)',
    '(Shattered to Crystalline Gravel / Gravity Resto': '(Shattered to Crystalline Gravel / Gravity Restored)',
    '(Shielding Acoustic Bounce off Vault Wal': '(Shielding Acoustic Bounce off Vault Walls)',
    '(Singing Before-Time Forgiveness Refrai': '(Singing Before-Time Forgiveness Refrain)',
    '(Siphoning Excess Screech into Res': '(Siphoning Excess Screech into Reservoir)',
    '(Sorrow 46/130 / Sinking into Deep Reverie': '(Sorrow 46/130 / Sinking into Deep Reverie)',
    '(Speed Delta +1 / Postu': '(Speed Delta +1 / Posture 50)',
    '(Stabilizing Viscosity Gradient Across Valve': '(Stabilizing Viscosity Gradient Across Valves)',
    '(Stagger': '(Stagger 1: 96)',
    '(Swirling into Void Cyclone / Grounded by Mell': '(Swirling into Void Cyclone / Grounded by Mellda)',
    '(TERMINAL STAGGER / AGITATION 0/120 / PURE HOP': '(TERMINAL STAGGER / AGITATION 0/120 / PURE HOPE)',
    '(TERMINAL STAGGER / PALE 0/140 / PURE DAWN LI': '(TERMINAL STAGGER / PALE 0/140 / PURE DAWN LIGHT)',
    '(TERMINAL STAGGER / PALE 0/150 / 12 CROWNS R': '(TERMINAL STAGGER / PALE 0/150 / 12 CROWNS RELEASED)',
    '(TERMINAL STAGGER / PALE 0/160 / FULL CONDENS': '(TERMINAL STAGGER / PALE 0/160 / FULL CONDENSED)',
    '(TERMINAL STAGGER / POSTURE 0/100 / 2.0x': '(TERMINAL STAGGER / POSTURE 0/100 / 2.0x DAMAGE)',
    '(TERMINAL STAGGER / POSTURE 0/110 / 2.0x DM': '(TERMINAL STAGGER / POSTURE 0/110 / 2.0x DAMAGE)',
    '(TERMINAL STAGGER / POSTURE 0/120 / 2.0x D': '(TERMINAL STAGGER / POSTURE 0/120 / 2.0x DAMAGE)',
    '(TERMINAL STAGGER / POSTURE 0/120 / CORE FRACTUR': '(TERMINAL STAGGER / POSTURE 0/120 / CORE FRACTURED)',
    '(TERMINAL STAGGER / POSTURE 0/130 / 2.0x DMG': '(TERMINAL STAGGER / POSTURE 0/130 / 2.0x DAMAGE)',
    '(TERMINAL STAGGER / POSTURE 0/140 / 2.0x': '(TERMINAL STAGGER / POSTURE 0/140 / 2.0x DAMAGE)',
    '(TERMINAL STAGGER / POSTURE 0/150 / 2.0x DM': '(TERMINAL STAGGER / POSTURE 0/150 / 2.0x DAMAGE)',
    '(TERMINAL STAGGER / POSTURE 0/160 / 2.': '(TERMINAL STAGGER / POSTURE 0/160 / 2.0x DAMAGE)',
    '(TERMINAL STAGGER / POSTURE 0/160 / 2.0x': '(TERMINAL STAGGER / POSTURE 0/160 / 2.0x DAMAGE)',
    '(TERMINAL STAGGER / POSTURE 0/160 / 2.0x D': '(TERMINAL STAGGER / POSTURE 0/160 / 2.0x DAMAGE)',
    '(TERMINAL STAGGER / POSTURE 0/170 / 2.0x': '(TERMINAL STAGGER / POSTURE 0/170 / 2.0x DAMAGE)',
    '(TERMINAL STAGGER / POSTURE 0/170 / 2.0x D': '(TERMINAL STAGGER / POSTURE 0/170 / 2.0x DAMAGE)',
    '(TERMINAL STAGGER / POSTURE 0/180 / 2.0x': '(TERMINAL STAGGER / POSTURE 0/180 / 2.0x DAMAGE)',
    '(TERMINAL STAGGER / POSTURE 0/180 / 2.0x DMG': '(TERMINAL STAGGER / POSTURE 0/180 / 2.0x DAMAGE)',
    '(TERMINAL STAGGER / POSTURE 0/200 / 2.': '(TERMINAL STAGGER / POSTURE 0/200 / 2.0x DAMAGE)',
    '(TERMINAL STAGGER / POSTURE 0/200 / 2.0x': '(TERMINAL STAGGER / POSTURE 0/200 / 2.0x DAMAGE)',
    '(TERMINAL STAGGER / POSTURE 0/200 / 2.0x DM': '(TERMINAL STAGGER / POSTURE 0/200 / 2.0x DAMAGE)',
    '(TERMINAL STAGGER / POSTURE 0/80 / 2.0x D': '(TERMINAL STAGGER / POSTURE 0/80 / 2.0x DAMAGE)',
    '(TERMINAL STAGGER / SORROW 0/130 / PEACEFU': '(TERMINAL STAGGER / SORROW 0/130 / PEACEFUL)',
    '(THE SMOTHERING': '(THE SMOTHERING SHROUD)',
    '(Tel': '(Telepathic Sync)',
    '(Transmutative Light': '(Transmutative Light)',
    '(Triggers at SP <': '(Triggers at SP <= -25)',
    '(Triggers at SP <=': '(Triggers at SP <= -35)',
    '(Unified Directional Guard Absorpti': '(Unified Directional Guard Absorption)',
    '(VOID SPECIALIST': '(VOID SPECIALIST)',
    '(Venting Toxic Cloud / Blinded by Scrubb': '(Venting Toxic Cloud / Blinded by Scrubbers)',
    '(Vigorous Harmon': '(Vigorous Harmony)',
    '(Void / Light / 1': '(Void / Light / 1 AP)',
    '(Void / Medium / 1 AP': '(Void / Medium / 1 AP)',
    '(Void Piercing /': '(Void Piercing / Resonance)',
    '(W': '(White Resonance)',
    '(WILL': '(WILLOW)',
    '(Wall of': '(Wall of Thorns)',
    '(Weight / Heavy / 2': '(Weight / Heavy / 2 AP)',
    '(Weight / Heavy /': '(Weight / Heavy / 2 AP)',
    '(Weight / Medium /': '(Weight / Medium / 1 AP)',
    '(White: 1.': '(White: 1.5x Multiplier)',
    '(Wings Folded / Pale Light Warm Gol': '(Wings Folded / Pale Light Warm Gold)',
    '(Work Success Up': '(Work Success Up)',
    '(Zero Resistance / Primed for Cycl': '(Zero Resistance / Primed for Cycle 1)',
}

def clean_row_content(inner):
    # Strip any trailing pipe if present
    inner = inner.rstrip('|').strip()

    # Check for bracket replacements
    for k, v in BRACKET_MAP.items():
        if inner.endswith(k):
            inner = inner[:-len(k)] + v
            break
        # also check with space or whatever
    
    # Check for paren replacements
    for k, v in PAREN_MAP.items():
        if inner.endswith(k):
            inner = inner[:-len(k)] + v
            break

    # Fix specific internal patterns
    if inner.count('(') > inner.count(')'):
        # unclosed paren at end
        if inner.endswith('('):
            inner = inner[:-1].strip()
        elif not inner.endswith(')'):
            inner = inner + ')'

    if inner.count('[') > inner.count(']'):
        # unclosed bracket at end
        if inner.endswith('['):
            inner = inner[:-1].strip()
        elif not inner.endswith(']'):
            inner = inner + ']'

    return inner

def format_clean_line(inner, orig_line):
    # Indentation preservation
    if orig_line.startswith("|     [N01]"):
        return f"|     {inner.strip()}     |"
    
    # Check if pipe table row
    if " | " in inner and not inner.startswith("- ") and not inner.startswith("1."):
        # Table row: keep spacing
        inner_s = inner.strip()
        if len(inner_s) <= 67:
            return f"| {inner_s.ljust(67)} |"
        else:
            # compress multi spaces
            inner_c = re.sub(r'  +', ' ', inner_s)
            if len(inner_c) <= 67:
                return f"| {inner_c.ljust(67)} |"
            return f"| {inner_s[:67]} |"

    inner_s = inner.strip()
    if len(inner_s) <= 67:
        return f"| {inner_s.ljust(67)} |"
    
    inner_c = re.sub(r'  +', ' ', inner_s)
    if len(inner_c) <= 67:
        return f"| {inner_c.ljust(67)} |"

    # If it is slightly longer than 67, fit it
    return f"| {inner_c[:67]} |"

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
            inner = stripped[1:-1].strip()
            orig_inner = inner
            
            cleaned_inner = clean_row_content(inner)
            if cleaned_inner != orig_inner:
                modified = True
            
            formatted = format_clean_line(cleaned_inner, line)
            new_lines.append(formatted + "\n")
            continue

        if not (line.startswith("|") and stripped.endswith("|")):
            in_box = False

        new_lines.append(line)

    if modified:
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print(f"Repaired delimiters in: {path}")

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
