import re

# Update index.html
with open("/home/user/01_Somnarak_Wiki/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace the hero container to be a sleek, centered/balanced Project Moon banner without any character standee
old_hero_pattern = r'<div class="pm-hero-container">.*?</div>\s*<div class="pm-slogan-bar">.*?</div>\s*</div>'

new_hero = """<div class="pm-hero-container">
      <div class="pm-hero-main pm-hero-centered">
        <div class="pm-brand-row">
          <img src="assets/icons/somnarak_icon.svg" alt="Somnarak Emblem">
          <div class="pm-brand-text">
            <h1>SOMNARAK<span>WIKI</span></h1>
            <strong>CITY OF UNRESOLVED SORROW</strong>
          </div>
        </div>
        <div class="pm-hero-subtext">
          Official encyclopedia of the city built around the Alpha Tree above the Weeping, its manifestations of Han, the Reverie Directorate, and the people who endure beyond the 1,778 Cycles.
        </div>
      </div>
      <div class="pm-slogan-bar">
        WITNESS THE SORROW, PRESERVE THE NAME <span>슬픔을 직시하고, 이름을 보존하라</span>
      </div>
    </div>"""

# If regex replace doesn't match easily, let's find the container directly
start_idx = html.find('<div class="pm-hero-container">')
end_idx = html.find('<!-- Chamfered Containment Box -->')

if start_idx != -1 and end_idx != -1:
    html = html[:start_idx] + new_hero + "\n\n    " + html[end_idx:]
    with open("/home/user/01_Somnarak_Wiki/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("index.html hero banner updated: character image removed!")
else:
    print("Could not find hero markers in index.html")
