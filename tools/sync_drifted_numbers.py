# 1. Update SOMNARAK-WORLD/Tactical_Combat_Engine/WHAT_CAN_BE_DONE.md
f1 = "SOMNARAK-WORLD/Tactical_Combat_Engine/WHAT_CAN_BE_DONE.md"
with open(f1, "r", encoding="utf-8") as fp:
    c1 = fp.read()
c1_new = c1.replace("287 Sorrow Entities", "292 Sorrow Entities")
with open(f1, "w", encoding="utf-8") as fp:
    fp.write(c1_new)

# 2. Update README.md
f2 = "README.md"
with open(f2, "r", encoding="utf-8") as fp:
    c2 = fp.read()
c2_new = c2.replace("Over 1,730 curated canonical markdown files", "Over 1,706 curated canonical markdown files in SOMNARAK-WORLD (1,940+ total files)")
c2_new = c2_new.replace("Corpus (1,730+ files)", "Corpus (1,706 files)")
with open(f2, "w", encoding="utf-8") as fp:
    fp.write(c2_new)

# 3. Update DEVELOPMENT.md
f3 = "DEVELOPMENT.md"
with open(f3, "r", encoding="utf-8") as fp:
    c3 = fp.read()
c3_new = c3.replace("Corpus (1,730+ files)", "Corpus (1,706 files)")
with open(f3, "w", encoding="utf-8") as fp:
    fp.write(c3_new)

print("Synchronized drifted numbers in README.md, DEVELOPMENT.md, and WHAT_CAN_BE_DONE.md.")
