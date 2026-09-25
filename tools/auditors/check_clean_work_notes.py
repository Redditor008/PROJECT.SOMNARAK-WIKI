import glob

files = glob.glob("SOMNARAK-WORLD/Sorrow_Entities/*.md")
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        txt = fp.read()
    if "Operational Work Notes" in txt and "cured.," not in txt:
        print(f"Clean file example: {f}")
        # print section
        start = txt.find("### Operational Work Notes")
        if start != -1:
            print(txt[start:start+400])
        break
