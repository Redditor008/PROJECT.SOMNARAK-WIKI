import re

f = "SOMNARAK-WORLD/Ordeals/Ordeal_BLACK_First_Watch_The_Grinding_Slab.md"
with open(f, 'r', encoding='utf-8') as fp:
    txt = fp.read()

# 1. Fix C2: out of 1000
txt = re.sub(r'(\bHP\s*\|\s*\d+/\d+)\s+out of 1000', r'\1', txt)

# 2. Fix B3: Year 4247 -> Year 4238
txt = txt.replace("Date:** Year 4247", "Date:** Year 4238")

# 3. Fix C5: double dots ..
txt = re.sub(r'\.\.', '.', txt)

# 4. Fix C4: double brackets and en dashes
txt = re.sub(r'\*\*\[\[(.*?)\]\]\*\*', r'**[\1]**', txt)
# en dash in ranges
txt = re.sub(r'(\d+)-(\d+)', r'\1–\2', txt)

# 5. Fix C3: Bespoke abilities
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

for ent, desc in bespoke_abilities.items():
    # Replace placeholder ability for this entity
    pattern = re.compile(rf'(###\s+{re.escape(ent)}[^\n]*\n[\s\S]*?\*\*Ability:\*\*\s*)Deals damage themed to its form and element\.\s*', re.IGNORECASE)
    txt = pattern.sub(rf'\1{desc} ', txt)

# 6. Fix C1: Spawn Roster header based on actual physical forms
forms = re.findall(r'\*\*Physical Form:\*\*\s*([A-Za-z0-9\-]+)', txt)
unique_forms = sorted(list(set(forms)))
forms_str = " / ".join(unique_forms)
header_pattern = re.compile(r'## Spawn Roster \([^\)]+\)')
txt = header_pattern.sub(f'## Spawn Roster ({forms_str})', txt)

print("=== SAMPLE DIFF SNIPPETS ===")
print("Header:", re.search(r'## Spawn Roster.*', txt).group(0))
print("Grinding Maw Ability:", re.search(r'### The Grinding Maw[\s\S]*?\*\*Ability:\*\*.*', txt).group(0).splitlines()[-1])
print("Date check:", re.search(r'\*\*Date:\*\*.*', txt).group(0))
