import glob
import re
import os

files = sorted(glob.glob("SOMNARAK-WORLD/Ordeals/*.md"))
print(f"Processing {len(files)} Ordeal files...")

bespoke_abilities = {
    "The Grinding Maw": "It unhinges its wide flat jaw and surges forward, grinding basalt teeth against stone and flesh to crush targets beneath sheer geological tonnage.",
    "The Living Avalanche": "It surges forward as an unyielding landslide of stone debris and jagged rebar, burying targets under suffocating weight and fracturing defenses.",
    "The Clockwork Press": "Its heavy pneumatic press-plate slams down in a rhythmic industrial cycle, compressing anything beneath it into flattened scrap.",
    "The Blade Storm": "It spins into a violent vortex of spinning scrap-iron and rusted sickle blades, lacerating all targets within reach with relentless grudge pressure.",
    "The Dirge Engine": "It emits a rhythmic acoustic thrum from exposed iron bellows, rattling chest cavities and forcing brine to seep from ocular ducts.",
    "The Erasure Projector": "It projects a beam of intense, bleaching monochrome light that scrubs pigment and memory from whatever it touches, unmaking physical coherence.",
    "The Eyeless Hound": "It lunges forward with blind predatory frenzy, tearing at exposed flanks with jaws formed of calcified sorrow-bone.",
    "The Parasite Bloom": "It bursts into a shower of virulent fungal spores, taking root in exposed wounds and leeching physical vitality to sprout rot-tendrils.",
    "The Root Network": "Thick black roots erupt from the flagstones to seize ankles and limbs, dragging targets down into the damp soil of the lower stratum.",
    "The Sorrow Fog": "It billows outward in a dense, freezing mist of aerosolized brine, choking respiratory passages and inducing profound sorrow paralysis.",
    "The Spore Loom": "It weaves a dense aerial web of infectious mycelial filaments that entangles movement and infects armor seals with encroaching decay.",
    "The Weeping Leviathan": "It crashes its colossal waterlogged bulk across the chamber, unleashing a tidal surge of concentrated brine that sweeps away defensive formations."
}

modified_count = 0

for f in files:
    if f.endswith("README.md"):
        continue
    with open(f, 'r', encoding='utf-8') as fp:
        orig = fp.read()
    
    txt = orig
    
    # 1. C2: Remove "out of 1000"
    txt = re.sub(r'(\bHP\s*\|\s*\d+/\d+)\s+out of 1000', r'\1', txt)
    
    # 2. B3: Re-anchor Date: Year 4247 -> Year 4238
    txt = txt.replace("Date:** Year 4247", "Date:** Year 4238")
    txt = txt.replace("Date:** Year 4220", "Date:** Year 4238 — Archive Retrieval Epoch")
    
    # 3. C5: Double dots ..
    txt = re.sub(r'\.\.', '.', txt)
    
    # 4. C4: Double brackets **[[...]]** -> **[...]**
    txt = re.sub(r'\*\*\[\[(.*?)\]\]\*\*', r'**[\1]**', txt)
    
    # En dash in damage ranges (e.g. 14-22 -> 14–22)
    def fix_dash(m):
        return f"{m.group(1)}–{m.group(2)}"
    txt = re.sub(r'(\d+)-(\d+)', fix_dash, txt)
    
    # 5. C3: Bespoke abilities
    for ent, desc in bespoke_abilities.items():
        pattern = re.compile(rf'(###\s+{re.escape(ent)}[^\n]*\n[\s\S]*?\*\*Ability:\*\*\s*)Deals damage themed to its form and element\.\s*', re.IGNORECASE)
        txt = pattern.sub(rf'\1{desc} ', txt)
    
    # 6. C1: Dynamic Spawn Roster Header
    forms = re.findall(r'\*\*Physical Form:\*\*\s*([A-Za-z0-9\-]+)', txt)
    if forms:
        unique_forms = sorted(list(set(forms)))
        forms_str = " / ".join(unique_forms)
        header_pattern = re.compile(r'## Spawn Roster \([^\)]+\)')
        txt = header_pattern.sub(f'## Spawn Roster ({forms_str})', txt)
        # Also clean subtitle if it mentions specific fixed forms
        txt = re.sub(
            r'covering physical form types \(Monster, Non-Crystal, Non-Humanoid\)',
            f'covering documented physical form types ({forms_str})',
            txt
        )
        txt = re.sub(
            r'covering physical form types \(Monster, Machine, Non-Humanoid\)',
            f'covering documented physical form types ({forms_str})',
            txt
        )

    if txt != orig:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(txt)
        modified_count += 1

print(f"Successfully repaired {modified_count} Ordeal files!")
