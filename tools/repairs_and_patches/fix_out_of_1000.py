import glob

files = glob.glob("SOMNARAK-WORLD/Ordeals/*.md")
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        txt = fp.read()
    txt = txt.replace(" out of 1000", "")
    txt = txt.replace("..", "...")
    with open(f, 'w', encoding='utf-8') as fp:
        fp.write(txt)

print("Cleaned 'out of 1000' and double periods in Ordeals.")
