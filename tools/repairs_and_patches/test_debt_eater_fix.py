import re

with open("SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIIβ-014_The_Debt_Eater_빚을_먹는_자.md", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Fix the classification splice
text_new = re.sub(r'(\bdifferent tiers\.)\s+the entity[\'’]s classification\.\s+', r'\1 ', text)

# 2. Fix cured., not permanent healing
text_new = text_new.replace("The entity is calmer, not cured., not permanent healing.", "The entity is calmer, not cured; the procedure achieves containment stabilization, not permanent healing.")

# 3. Fix not healing. or fed
text_new = text_new.replace("the wound is responding, not healing. or fed the entity’s originating sorrow.", "the wound is responding, not healing, or the work has inadvertently fed the entity’s originating sorrow.")

# 4. Fix not predicted. before the next assignment
text_new = text_new.replace("a visual change not predicted. before the next assignment.", "a visual change not predicted must be documented before the next assignment.")

print("=== BEFORE ===")
start = text.find("### Operational Work Notes")
print(text[start:start+650])

print("=== AFTER ===")
start_new = text_new.find("### Operational Work Notes")
print(text_new[start_new:start_new+650])
