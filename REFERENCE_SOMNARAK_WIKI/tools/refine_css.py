import re

CSS_PATH = "/home/user/01_Somnarak_Wiki/assets/css/wiki.css"

with open(CSS_PATH, "r", encoding="utf-8") as f:
    css = f.read()

# 1. Replace overflow-wrap:anywhere on #content with overflow-wrap:break-word; word-break:normal
css = css.replace("overflow-wrap:anywhere", "overflow-wrap:break-word;word-break:normal")

# 2. Clean clip-paths that slice text
css = re.sub(r'clip-path:polygon\([^)]+\);?', '', css)

# 3. Enhance floor buttons and rail action
css = css.replace(
    '.floor-button{position:relative;display:flex;align-items:center;justify-content:space-between;height:58px;margin:7px 0;padding:7px 9px 7px 30px;border:2px solid var(--floor);color:var(--floor);',
    '.floor-button{position:relative;display:flex;align-items:center;justify-content:space-between;height:58px;margin:7px 0;padding:7px 12px 7px 24px;border:2px solid var(--floor);color:var(--floor);border-left:5px solid var(--floor);'
)

# 4. Enhance typography rules so no words get cut or hyphenated awkwardly
typography_fixes = """
h1, h2, h3, h4, b, strong, span, p, a, dt, dd, th, td {
  word-break: normal;
  overflow-wrap: break-word;
}
.home-wordmark h1, .map-title h1, .department-hero h1, .entity-hero h1, .wide-hero h1 {
  white-space: normal;
  word-break: normal;
  overflow-wrap: break-word;
}
"""
css += "\n" + typography_fixes.strip()

with open(CSS_PATH, "w", encoding="utf-8") as f:
    f.write(css)

print("CSS refined successfully. Clip-path text cuts removed, overflow-wrap corrected to prevent word cutting.")
