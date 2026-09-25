import glob
import re

files = glob.glob("SOMNARAK-WORLD/**/*.md", recursive=True)

# Replacements dictionary for Group 1 (not permanent healing)
rep_g1 = {
    "Do not mistake management for resolution., not permanent healing.": "Do not mistake management for resolution; containment offers temporary calm, not permanent healing.",
    "It does not confirm the entity is safe — only quieter., not permanent healing.": "It does not confirm the entity is safe — only quieter; this is stabilization, not permanent healing.",
    "The deep structure of its grief is untouched., not permanent healing.": "The deep structure of its grief is untouched; this reflects containment stabilization, not permanent healing.",
    "The entity is calmer, not cured., not permanent healing.": "The entity is calmer, not cured; the procedure achieves containment stabilization, not permanent healing.",
    "The pressure subsides; the source persists., not permanent healing.": "The pressure subsides; the source persists, providing containment stabilization, not permanent healing.",
    "The pressure will return unless the work cycle is sustained., not permanent healing.": "The pressure will return unless the work cycle is sustained; this is ongoing stabilization, not permanent healing.",
}

# Replacements for Group 2 (or fed the entity's originating sorrow)
# Handle curly and straight quotes
def fix_g2(text):
    text = re.sub(
        r"A rising gauge means the Work Type has triggered the entity['’]s originating sorrow — the wound is responding, not healing\.\s+or fed the entity['’]s originating sorrow\.",
        "A rising gauge means the Work Type has triggered the entity’s originating sorrow — the wound is responding, not healing, or the work has inadvertently fed the entity’s originating sorrow.",
        text
    )
    text = re.sub(
        r"Pull back and reassess\.\s+or fed the entity['’]s originating sorrow\.",
        "Pull back and reassess before the procedure inadvertently feeds the entity’s originating sorrow.",
        text
    )
    text = re.sub(
        r"The entity['’]s grief is louder now, not quieter\.\s+or fed the entity['’]s originating sorrow\.",
        "The entity’s grief is louder now, not quieter, indicating that the work has aggravated or fed the entity’s originating sorrow.",
        text
    )
    text = re.sub(
        r"The gauge rising signals that the Work Type is resonating with the entity['’]s wound rather than soothing it\.\s+or fed the entity['’]s originating sorrow\.",
        "The gauge rising signals that the Work Type is resonating with the entity’s wound rather than soothing it, or has inadvertently fed the entity’s originating sorrow.",
        text
    )
    text = re.sub(
        r"The sorrow is growing\.\s+or fed the entity['’]s originating sorrow\.",
        "The sorrow is growing, indicating that the procedure has provoked or fed the entity’s originating sorrow.",
        text
    )
    text = re.sub(
        r"The wrong Work Type has been applied, or the right one has been overused\.\s+or fed the entity['’]s originating sorrow\.",
        "The wrong Work Type has been applied, or the right one has been overused, inadvertently feeding the entity’s originating sorrow.",
        text
    )
    return text

# Replacements for Group 3 (before the next assignment)
def fix_g3(text):
    text = re.sub(
        r"Anomalous responses are not errors to dismiss; they are signals that the entity has changed or the file is incomplete\.\s+before the next assignment\.",
        "Anomalous responses are not errors to dismiss; they are signals that the entity has changed or the file is incomplete, and must be logged before the next assignment.",
        text
    )
    text = re.sub(
        r"Log deviations immediately — an unexpected gauge movement, a sound not described in the file, a visual change not predicted\.\s+before the next assignment\.",
        "Log deviations immediately — an unexpected gauge movement, a sound not described in the file, or a visual change not predicted must be documented before the next assignment.",
        text
    )
    text = re.sub(
        r"Log them, flag them, and adjust the next assignment accordingly\.\s+before the next assignment\.",
        "Log them, flag them, and adjust protocols accordingly before the next assignment.",
        text
    )
    text = re.sub(
        r"Preserve it before the next work cycle begins\.\s+before the next assignment\.",
        "Preserve all observations before the next work cycle begins and log them before the next assignment.",
        text
    )
    text = re.sub(
        r"The file is a baseline, not a ceiling\.\s+before the next assignment\.",
        "The file is a baseline, not a ceiling; all deviations must be recorded before the next assignment.",
        text
    )
    text = re.sub(
        r"Write it down\.\s+before the next assignment\.",
        "Write it down and update logs before the next assignment.",
        text
    )
    return text

# Classification splice regex
cls_regex = re.compile(r'(\.)\s+the entity[\'’]s classification\.\s+', re.IGNORECASE)

modified_count = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        orig = fp.read()
    
    text = orig
    # Fix classification splice
    text = cls_regex.sub(r'\1 ', text)
    
    # Fix Group 1
    for k, v in rep_g1.items():
        if k in text:
            text = text.replace(k, v)
    
    # Fix Group 2
    text = fix_g2(text)
    
    # Fix Group 3
    text = fix_g3(text)
    
    if text != orig:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(text)
        modified_count += 1

print(f"Successfully repaired semantic seams in {modified_count} files!")
