import re
import glob
import os
import sys

# ---------------------------------------------------------------------------
# V6-6. Guards the three label/tag regressions identified in V6-1:
#   R1 LABEL_CODE_PAREN  - a table label decorated with an entity code
#   R2 LABEL_SELF_NAME   - a table label decorated with its own entity name
#   R3 BARE_CODE_TAG     - a bare [SE-...] tag appended to text (NOT a link)
#   R5 CALLOUT_SELF_NAME - an Entry callout decorated with the entity's own name
#   R6 WORKTYPE_SELF_NAME - a Work Type label decorated with the entity's own name
#   R7 RECORD_SUFFIX_SELF_NAME - a '(<Name> record.)' suffix on shared furniture
#   R4 LABEL_NOT_ALLOWED - a table label outside the fixed vocabulary
#
# R3 scans every line including table cells. The original V6-1 sweep only
# caught end-of-sentence tags, which left 395 tags alive inside table cells
# across 282 dossiers. Do not narrow this back to line endings.
# ---------------------------------------------------------------------------

DOSSIER_DIRS = ["SOMNARAK-WORLD/Sorrow_Entities", "SOMNARAK-WORLD/Unknown_Entities"]

# Structural schema labels: the dossier skeleton.
SCHEMA_LABELS = {
    "Activation", "Activation or escalation", "Activation threshold", "After use",
    "At limit", "Battle Length", "Battlefield", "Before use", "Breach Type",
    "Coherence", "Coherence modifier", "Containment", "Designation", "Difficulty",
    "Distinctive markers", "Duration", "Duration / rate", "During use", "Effect",
    "Element", "Entity Type", "Entity role", "Escalation", "Expansion Effect",
    "Expansion Rate", "Expansion Trigger", "Ferrehan", "First Target", "Flerehan",
    "Form", "Han Dust Drop (Vessel Destruction)", "Han Pressure [ATK]",
    "Han-Energy yield", "Identification", "Initial exposure", "Location",
    "Management", "Manifestation", "Material / signature", "Movement",
    "OBSERVATION SUCCESS", "Physical Form", "Position / movement",
    "Post-contact review", "Potency", "Potency modifier", "Primary Effect",
    "Primary Pressure", "Primary effect", "Primary pressure", "Pugnahan",
    "R.D. Comprehension Level", "Recommended response", "Resistance",
    "Resolution Condition", "Retained non-breach mechanic", "Risk", "Risk tier",
    "Secondary Effect", "State change",
    "Sorrow Category", "Sorrow Gauge [HP]", "Speed", "Starting Sorrow Gauge",
    "Sustained observation", "Termination / Return", "Threat Role",
    "Tool / M.A.W. grade", "Tool Class", "Tool Type", "Trigger", "Use Mode",
    "Valid Work Types", "Vessel-Destructible", "Viderehan", "Work difficulty",
}

# Curated one-off labels: material specs, phase rows, and outcome rows.
EXTRA_LABELS = {
    "(Grudge)", "(Lament)", "(Void)", "(Weight)",
    "Acid Scars", "Acoustic Dead Zone", "Acoustic Signature", "Aftermath",
    "All Training Personnel", "Alloy Composition", "Beneficial Effect",
    "Breach", "Breach Designation", "Breach Designation Shift", "Build",
    "Caught in the Storm", "Cold Burn", "Collar Seal", "Confession initiated",
    "Contained Designation", "Containment Status", "Dimensions / Mass",
    "Envelope Medium", "First Recorded", "Glass Medium", "Han Dust Drop",
    "Han-Energy Yield", "How to Channel", "Impact", "Initial contact",
    "Initial manifestation", "Initial observation", "Internal Gas",
    "Length / Diameter", "Lull", "M.A.W. Extraction", "Metallurgy",
    "Metamorphosis Type", "Mineral Structure", "OBSERVATION FAIL", "Origin",
    "Recession", "Residue Adhesion", "SECC Designation", "Seal Compound",
    "Seam Weakness", "Speed / Expansion", "Suppression", "Surface Markings",
    "Surge", "Termination Method", "Thermal Delta", "Thermal Equilibrium",
    "Thermal Output", "Threat Score", "Visual confirmation", "Weight",
    # Unknown_Entities wing schema variants.
    "Activation / escalation", "Boundary / movement", "Management / containment",
    "Movement / spread", "MEW SPECIAL <3",
    # One-off outcome rows retained from the historical record.
    "OBSERVATION SUCCESS (the historical resolution)",
    "SE-C-V\u03b4-949 (the classified outcome)",
    "Observe the Tide from the Watchtower during a surge.",
}

# In-world proper nouns used as cross-reference row keys that are not catalogued
# entities: places, groups, named personnel, and destroyed vessels.
CROSS_REF_EXTRAS = {
    'Archive Lead Marjuk', 'Area affected', 'Director Majin', 'Eleventh conversion',
    'Expansion Type', 'Faceless Glass', 'Fading Ruin', 'Failure condition',
    'MEW LIGHT BEAAAAAM', 'MEWTASTICAL TRANSFORM', 'Persona color state', 'Reverberant',
    'Sealed Rage', 'Silence We Forgot We Made', 'Sornos', 'The Alpha Tree',
    'The Architects', 'The Border Lead', 'The Burning Hope', "The Cartographer's Ghost",
    'The Convergence (Three Birds)', 'The Crystal Peaks', 'The Debt Clock',
    'The Defiant Ember', 'The Dream Weaver', 'The Drift Fog', 'The Echo Gardens',
    'The Echo-Cores', 'The Echo-Cores (R.D.)', 'The Eternal Warmth', 'The Exile',
    "The Exile's Gate", 'The Flowing Bridge', 'The Frozen Bridge', 'The Frozen Relic',
    'The Frozen Ruin', 'The Frozen Sigh', 'The Frozen Veil (destroyed)',
    'The Garden of Thorns', 'The Gentle Flame', 'The Grieving Fountain',
    'The Grieving The Lonely Giant', 'The Guardian of the Gate', 'The Guiding Light',
    'The Hand of Hope', 'The Iron Judge', 'The Last Memory', 'The Masked Market',
    'The Melting Saint', 'The Melting Tower', 'The Memory Archive',
    'The Memory Archive / Seiyon', 'The Mirror of Sorrows', 'The Outside Sorrow',
    'The Preserved Heart', 'The Rage Flame', 'The Rage Forge', 'The Returning Fruit',
    'The Returning Relic', 'The Returning Tree', 'The Rising Bridge',
    'The Rising Mirror', 'The Rootless', 'The Rusted Seed', 'The Rusted Soul',
    'The Rusted Wall', 'The Rusted Whisper', 'The Shadow at the Door',
    'The Shared Glass', 'The Silent Scream', 'The Singing Stone', 'The Sleeping Relic',
    'The Sleeping Wall', 'The Sorrow Flower', 'The Sorrow Lake', 'The Sorrow River',
    'The Spreading Tree', 'The Storm arrives', 'The Storm passes', 'The Sunken Bridge',
    'The Sunken Tower', 'The Torn Soul', 'The Torn Tower', 'The Torn Trace',
    'The Trinity of Dawn', 'The Undersong', 'The Vanished Flame', 'The Vanished Ruin',
    'The Vanished Seed', 'The Vanished Shadow', 'The Vanished Tower',
    'The Vanished Wall', 'The Wandering Chain', 'The Wandering Door',
    'The Wandering Sigh', 'The Wandering Trace', 'The Weaver of Dreams', 'The Weeping',
    'The Weight of Years', 'Torn Loyalty', 'Untended Seed', 'Vestige', 'Visible change',
    'Weapon focus',
}

# Entity-code shapes: full 'SE-C-IIIγ-021' and bare 'C-IIβ-947'.
P_CODE = re.compile(r'\b(?:SE-)?[CON]-(?:I{1,3}|IV|V)[\u03b1-\u03c9]?-\d+\b')
# A bare [SE-...] tag. A markdown link '[SE-...](path)' is legitimate.
P_BARE_TAG = re.compile(r'\[\s*(?:SE-)?[CON]-[^\]\n]{1,28}\](?!\()')
# First cell of a table row, bolded.
P_BOLD_CELL = re.compile(r'\*\*(.+?)\*\*')
# Counter rows such as '3 blessings observed' / '10 turns survived' / '2'.
P_COUNTER = re.compile(r'^\d+[a-z]?\b.*$|^\d+$')


def entity_identity(path):
    """Return (display name, code) derived from the dossier filename."""
    base = os.path.basename(path)[:-3]
    m = re.match(r'(SE-[^_]+)_(.*)', base)
    if not m:
        return None, None
    code, rest = m.group(1), m.group(2)
    parts = rest.split('_')
    cut = next((i for i, p in enumerate(parts)
                if re.search(r'[\uac00-\ud7af]', p)), len(parts))
    return ' '.join(parts[:cut]).strip(), code


def catalogued_names():
    """Entity names from the catalog and from dossier filenames on disk."""
    names = set()
    cat = "REFERENCE_SOMNARAK_WIKI/SORROW_ENTITIES_CATALOG.md"
    if os.path.exists(cat):
        with open(cat, 'r', encoding='utf-8') as fp:
            # Catalog rows are: | `SE-code` | **English Codename** | ... |
            for m in re.finditer(r'\|\s*`(SE-[^`]+)`\s*\|\s*\*\*(.+?)\*\*\s*\|', fp.read()):
                names.add(m.group(2).strip())
    for d in DOSSIER_DIRS:
        for f in glob.glob(os.path.join(d, "*.md")):
            n, _ = entity_identity(f)
            if n:
                names.add(n)
    return names


_NAMES = None


def label_allowed(label):
    """A label must come from the fixed vocabulary. No open-ended fallback."""
    global _NAMES
    if label in SCHEMA_LABELS or label in EXTRA_LABELS or label in CROSS_REF_EXTRAS:
        return True
    if P_COUNTER.match(label):
        return True
    if _NAMES is None:
        _NAMES = catalogued_names()
    bare = re.sub(r"^The\s+", "", label).strip()
    return label in _NAMES or bare in _NAMES or ("The " + bare) in _NAMES


# R5: bold "Entry N (Something) --" callout headers. The entity's own name in
# that parenthetical is the V5-12 decoration pattern, not differentiation.
P_ENTRY_DECOR = re.compile(r"\*\*Entry (\d+)\s*\(([^)]+)\)\s*[-\u2014]")

# R6: bold Work Type cell labels in the Behavior table. "**Flerehan (Name)**"
# is the same V5-12 decoration pattern in a third syntactic position, missed by
# both the V6-1 sweep (table *labels* only, not bold runs inside cells) and by
# R5 (Entry callouts only). The Work Type vocabulary is fixed and closed, so a
# parenthetical after it can never be legitimate differentiation.
WORK_TYPES = ("Flerehan", "Pugnahan", "Viderehan", "Ferrehan")
P_WORKTYPE_DECOR = re.compile(
    r"\*\*(" + "|".join(WORK_TYPES) + r")\s*\(([^)]+)\)\*\*")


# R7: "(<Entity Name> record.)" appended to Relic capability callouts and to the
# Story Log preamble. The sentences it trails are identical in every dossier;
# the name is there to make shared furniture look authored. Same V5-12 pattern
# as R5/R6, fourth syntactic position.
P_RECORD_DECOR = re.compile(r"\(([^)]+?) record\.\)")


def audit_file(path):
    """Return a list of violation strings for one dossier."""
    name, code = entity_identity(path)
    if name is None:
        return []
    errors = []
    with open(path, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()

    for idx, line in enumerate(lines, start=1):
        # R3: bare code tags anywhere, table cells included.
        for m in P_BARE_TAG.finditer(line):
            errors.append(
                f"{path}:{idx} -> [BARE_CODE_TAG] '{m.group(0)}' "
                f"appended to text; code tags are not a differentiation device")

        # R5: an Entry callout decorated with the entity's own name.
        for m in P_ENTRY_DECOR.finditer(line):
            inner = m.group(2).strip()
            if inner == name or inner in name or name in inner:
                errors.append(
                    f"{path}:{idx} -> [CALLOUT_SELF_NAME] Entry header "
                    f"'{m.group(0)}' is decorated with the entity's own name")

        # R6: a Work Type label decorated with the entity's own name.
        for m in P_WORKTYPE_DECOR.finditer(line):
            inner = m.group(2).strip()
            if inner == name or inner in name or name in inner:
                errors.append(
                    f"{path}:{idx} -> [WORKTYPE_SELF_NAME] Work Type label "
                    f"'{m.group(0)}' is decorated with the entity's own name")

        # R7: a "(<Name> record.)" suffix on otherwise shared furniture.
        for m in P_RECORD_DECOR.finditer(line):
            inner = m.group(1).strip()
            if inner == name or inner in name or name in inner:
                errors.append(
                    f"{path}:{idx} -> [RECORD_SUFFIX_SELF_NAME] suffix "
                    f"'{m.group(0)}' decorates shared text with the entity's own name")

        stripped = line.strip()
        if not stripped.startswith('|'):
            continue
        cells = [c.strip() for c in stripped.strip('|').split('|')]
        if len(cells) < 2:
            continue
        m = P_BOLD_CELL.fullmatch(cells[0])
        if not m:
            continue
        label = m.group(1).strip()

        for pm in re.finditer(r'\(([^)]*)\)', label):
            inner = pm.group(1)
            # R1: code in a label parenthetical.
            if P_CODE.search(inner):
                errors.append(
                    f"{path}:{idx} -> [LABEL_CODE_PAREN] label '{label}' "
                    f"carries an entity code in parentheses")
            # R2: own name in a label parenthetical.
            if name and name.lower() in inner.lower():
                errors.append(
                    f"{path}:{idx} -> [LABEL_SELF_NAME] label '{label}' "
                    f"is decorated with its own entity name")

        # R4: label outside the fixed vocabulary.
        if not label_allowed(label):
            errors.append(
                f"{path}:{idx} -> [LABEL_NOT_ALLOWED] label '{label}' "
                f"is not in the fixed dossier label vocabulary")
    return errors


def main():
    print("=== PROJECT SOMNARAK // DOSSIER LABEL & CODE-TAG LINTER ===")
    files = []
    for d in DOSSIER_DIRS:
        files.extend(sorted(glob.glob(os.path.join(d, "*.md"))))
    files = [f for f in files if re.match(r'SE-[^_]+_', os.path.basename(f))]

    errors = []
    for f in files:
        errors.extend(audit_file(f))

    print(f"Audited {len(files)} dossiers across {len(DOSSIER_DIRS)} wings.")
    if errors:
        print(f"\n[FAIL] Found {len(errors)} label / code-tag violation(s):")
        for e in errors[:25]:
            print("  -", e)
        if len(errors) > 25:
            print(f"  ... and {len(errors) - 25} more.")
        sys.exit(1)
    print("[PASS] 0 label or code-tag violations found! "
          "All dossier labels come from the fixed vocabulary.")


if __name__ == "__main__":
    main()
