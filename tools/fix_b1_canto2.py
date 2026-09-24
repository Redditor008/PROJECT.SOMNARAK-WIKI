f = "SOMNARAK-WORLD/Story_Cantos/CANTO_02_THE_ACOUSTIC_VOID_SEOL_A.md"
with open(f, "r", encoding="utf-8") as fp:
    c = fp.read()

# Fix B1
old_b1 = '"Yoon\'s sister died five hundred years ago, Min-Jae,"'
new_b1 = '"Yoon\'s sister died two hundred years ago, Min-Jae,"'
assert old_b1 in c, f"Could not find '{old_b1}' in {f}"
c = c.replace(old_b1, new_b1)

with open(f, "w", encoding="utf-8") as fp:
    fp.write(c)

print("Fixed B1 in CANTO_02.")
