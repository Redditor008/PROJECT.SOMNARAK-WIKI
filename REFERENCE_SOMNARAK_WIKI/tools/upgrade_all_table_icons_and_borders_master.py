import os
import re

def upgrade_master():
    wiki_root = "/home/user/01_Somnarak_Wiki"
    css_file = os.path.join(wiki_root, "assets/css/wiki.css")

    # 1. ADD MASTER HIGH-VISIBILITY ICON & BORDER RULES IN CSS
    master_css = '''
/* ==========================================================================
   ULTRA-HD ICON SIZING & MASTER TABLE BORDER ARCHITECTURE
   ========================================================================== */

/* 1. MASTER TABLE WRAPPER - GOLD NEON FRAME */
.table-wrap,
.pm-table-wrapper,
.wiki-table-container,
.data-table-wrap,
.spotlight-data-table {
  width: 100% !important;
  overflow-x: auto !important;
  -webkit-overflow-scrolling: touch !important;
  margin: 2rem 0 2.5rem !important;
  background: #060a12 !important;
  border: 3.5px solid #f1df76 !important; /* Thick High-Contrast Gold Outer Border */
  border-radius: 8px !important;
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.95), 0 0 25px rgba(241, 223, 118, 0.3) !important;
  padding: 0 !important;
}

/* 2. TABLE GRID - THICK 2.5PX BORDERS ON EVERY CELL */
table,
table.wiki-table,
table.pm-table,
.pm-table,
.wiki-table,
.data-table table,
.home-table,
.source-table {
  width: 100% !important;
  border-collapse: collapse !important;
  border-spacing: 0 !important;
  font-size: 0.96rem !important;
  text-align: left !important;
  color: #f1f5f9 !important;
  background: #080e1a !important;
  border: 2.5px solid #38bdf8 !important; /* Thick Cyan Border */
}

/* 3. TABLE HEADER CELLS */
table th,
table.wiki-table th,
table.pm-table th,
.pm-table th,
.wiki-table th,
.data-table th,
.home-table th,
.source-table th {
  background: linear-gradient(180deg, #1b2e47 0%, #0c1827 100%) !important;
  color: #f1df76 !important;
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 1rem !important;
  letter-spacing: 0.09em !important;
  text-transform: uppercase !important;
  padding: 16px 20px !important;
  border: 2px solid #2b4566 !important;
  border-bottom: 3.5px solid #38bdf8 !important;
  text-shadow: 0 2px 5px rgba(0, 0, 0, 0.95) !important;
}

/* 4. TABLE BODY CELLS */
table td,
table.wiki-table td,
table.pm-table td,
.pm-table td,
.wiki-table td,
.data-table td,
.home-table td,
.source-table td {
  padding: 15px 20px !important;
  border: 2px solid #20334a !important; /* Prominent solid grid lines */
  color: #e2e8f0 !important;
  font-size: 0.95rem !important;
  line-height: 1.65 !important;
  background: rgba(9, 15, 26, 0.95) !important;
  vertical-align: middle !important;
}

/* 5. ZEBRA STRIPING & HOVER */
table tbody tr:nth-child(even) td,
table.wiki-table tbody tr:nth-child(even) td,
table.pm-table tbody tr:nth-child(even) td {
  background: rgba(15, 25, 42, 0.98) !important;
}

table tbody tr:hover td,
table.wiki-table tbody tr:hover td,
table.pm-table tbody tr:hover td {
  background: rgba(56, 189, 248, 0.25) !important;
  color: #ffffff !important;
  border-color: #38bdf8 !important;
}

/* 6. TABLE ICONS - MASSIVE 48PX HIGH-VISIBILITY EMBLEMS */
table td img,
.pm-table td img,
.wiki-table td img,
.table-icon-large {
  width: 52px !important;
  height: 52px !important;
  min-width: 52px !important;
  min-height: 52px !important;
  vertical-align: middle !important;
  display: inline-block !important;
  border-radius: 8px !important;
  border: 2px solid #38bdf8 !important;
  background: #040811 !important;
  padding: 4px !important;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.9), 0 0 10px rgba(56, 189, 248, 0.35) !important;
  margin-right: 12px !important;
}

/* 7. STANDALONE PORTAL & HUB CARD ICONS */
.entity-card-icon,
.pm-entity-card .entity-card-icon,
.hub-card-icon,
.dept-card-icon,
.portal-cat-icon {
  width: 110px !important;
  height: 110px !important;
  min-width: 110px !important;
  min-height: 110px !important;
  object-fit: contain !important;
  margin-bottom: 14px !important;
  border-radius: 10px !important;
  border: 2.5px solid #f1df76 !important;
  background: #060a12 !important;
  padding: 8px !important;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.9), 0 0 15px rgba(241, 223, 118, 0.3) !important;
}

/* 8. DIRECTORY & CROSS-REFERENCE ICONS */
.department-directory img,
.cross-ref-card img {
  width: 72px !important;
  height: 72px !important;
  min-width: 72px !important;
  min-height: 72px !important;
  border-radius: 8px !important;
  padding: 5px !important;
  border: 2px solid #38bdf8 !important;
  background: #060a12 !important;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.8) !important;
}

.site-mark img {
  width: 72px !important;
  height: 72px !important;
}

.floor-avatar-wrap img {
  width: 64px !important;
  height: 64px !important;
}
'''

    with open(css_file, "a", encoding="utf-8") as f:
        f.write("\n" + master_css + "\n")
    print("Injected master high-visibility icon & table border CSS rules!")

    # 2. UPGRADE index.html DAMAGE MATRIX TABLE & FLOOR SUMMARY TABLE
    index_path = os.path.join(wiki_root, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        index_html = f.read()

    # Build the ultra-rich 4-Way Han Damage Matrix Table with dedicated Icon Column & 52px icons
    new_damage_table = '''
        <div class="pm-table-wrapper">
          <table class="pm-table" style="border: 2.5px solid #38bdf8;">
            <thead>
              <tr>
                <th style="width: 80px; text-align: center;">Visual</th>
                <th>Damage Type</th>
                <th>Dominant Color</th>
                <th>Target Attribute</th>
                <th>Psychic &amp; Physical Effects</th>
                <th>Primary Mitigation Strategy</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="text-align: center; vertical-align: middle;">
                  <img src="assets/icons/damage_red.svg" alt="Grudge Emblem" style="width: 52px; height: 52px; border: 2px solid #ef4444; background: #1f0505; border-radius: 8px; padding: 4px; box-shadow: 0 0 14px rgba(239, 68, 68, 0.6);">
                </td>
                <td><strong style="color: #ef4444; font-size: 1.1rem; letter-spacing: 0.05em;">Grudge (원한)</strong></td>
                <td><span class="badge badge-crimson" style="font-size: 0.85rem; padding: 4px 10px;">Crimson / Fiery Red</span></td>
                <td><strong style="color: #fca5a5;">Health Points (HP)</strong></td>
                <td>Direct physical blunt impact, lacerations, thermal combustion, and severe bone fracturing.</td>
                <td>Heavy armored M.A.W. Suits (Resolve affinity) with Grudge resistance &le; 0.5.</td>
              </tr>
              <tr>
                <td style="text-align: center; vertical-align: middle;">
                  <img src="assets/icons/damage_white.svg" alt="Lament Emblem" style="width: 52px; height: 52px; border: 2px solid #38bdf8; background: #041424; border-radius: 8px; padding: 4px; box-shadow: 0 0 14px rgba(56, 189, 248, 0.6);">
                </td>
                <td><strong style="color: #38bdf8; font-size: 1.1rem; letter-spacing: 0.05em;">Lament (비탄)</strong></td>
                <td><span class="badge badge-somna" style="font-size: 0.85rem; padding: 4px 10px;">Azure / Cyan Blue</span></td>
                <td><strong style="color: #7dd3fc;">Sanity Points (SP)</strong></td>
                <td>Severe cognitive distress, auditory hallucinations, grief paralysis, panic erosion, and self-harm.</td>
                <td>Psychologically reinforced M.A.W. Veils (Resilience affinity) and Insight work routines.</td>
              </tr>
              <tr>
                <td style="text-align: center; vertical-align: middle;">
                  <img src="assets/icons/damage_black.svg" alt="Void Emblem" style="width: 52px; height: 52px; border: 2px solid #f1df76; background: #241904; border-radius: 8px; padding: 4px; box-shadow: 0 0 14px rgba(241, 223, 118, 0.6);">
                </td>
                <td><strong style="color: #f1df76; font-size: 1.1rem; letter-spacing: 0.05em;">Void (공허)</strong></td>
                <td><span class="badge badge-gold" style="font-size: 0.85rem; padding: 4px 10px;">Amber / Obsidian Gold</span></td>
                <td><strong style="color: #fef08a;">Simultaneous HP &amp; SP</strong></td>
                <td>Dual-channel corrosive necrosis and existential ego dissolution; drains body and mind equally.</td>
                <td>Balanced composite M.A.W. Plate (Composure affinity); avoid solitary containment shifts.</td>
              </tr>
              <tr>
                <td style="text-align: center; vertical-align: middle;">
                  <img src="assets/icons/damage_pale.svg" alt="Pale Emblem" style="width: 52px; height: 52px; border: 2px solid #ffffff; background: #12102b; border-radius: 8px; padding: 4px; box-shadow: 0 0 14px rgba(255, 255, 255, 0.7);">
                </td>
                <td><strong style="color: #ffffff; font-size: 1.1rem; letter-spacing: 0.05em; text-shadow: 0 0 8px #ffffff;">Pale (창백)</strong></td>
                <td><span class="badge badge-pale" style="font-size: 0.85rem; padding: 4px 10px; background: #1e1b4b; color: #ffffff; border: 1px solid #818cf8;">Pristine / Ghost White</span></td>
                <td><strong style="color: #e0e7ff;">Max HP Percentage</strong></td>
                <td>Direct soul-death bypassing conventional physical armor; deals damage scaling off maximum HP.</td>
                <td>High-tier &omega;-grade M.A.W. suits (Clarity affinity Level V required); extreme caution.</td>
              </tr>
            </tbody>
          </table>
        </div>
'''

    # Replace the old damage table block in index.html
    old_table_pattern = re.compile(r'<div class="pm-table-wrapper">\s*<table class="pm-table">\s*<thead>\s*<tr>\s*<th>Damage Type</th>.*?</table>\s*</div>', re.DOTALL)
    if old_table_pattern.search(index_html):
        index_html = old_table_pattern.sub(new_damage_table.strip(), index_html)

    # Upgrade Floor summary table in index.html with large lead avatars
    floor_table_pattern = re.compile(r'<table class="pm-table">\s*<thead>\s*<tr>\s*<th>Floor</th>.*?</table>', re.DOTALL)
    # Ensure floor table avatars use 52px size
    index_html = re.sub(
        r'<img src="(assets/avatars/[^"]+)" alt="" style="[^"]*">',
        r'<img src="\1" alt="" style="width: 52px; height: 52px; border-radius: 50%; border: 2px solid #38bdf8; background: #060d18; vertical-align: middle; margin-right: 12px; display: inline-block; padding: 2px; box-shadow: 0 0 10px rgba(56, 189, 248, 0.4);">',
        index_html
    )

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(index_html)
    print("Updated index.html with prominent Damage Matrix table and 52px icons!")

    # 3. UPGRADE ALL OTHER HTML FILES: Replace in-table icons with 52px size
    all_html = []
    for root, dirs, files in os.walk(wiki_root):
        for file in files:
            if file.endswith(".html"):
                all_html.append(os.path.join(root, file))

    for fpath in all_html:
        with open(fpath, "r", encoding="utf-8") as f:
            c = f.read()
        orig = c
        c = re.sub(
            r'style="width:32px;height:32px;vertical-align:middle;margin-right:10px;display:inline-block;border-radius:4px;border:1px solid rgba\(56,189,248,0.5\);background:#090d16;padding:2px;"',
            r'style="width: 50px; height: 50px; vertical-align: middle; margin-right: 12px; display: inline-block; border-radius: 8px; border: 2px solid #38bdf8; background: #060b14; padding: 4px; box-shadow: 0 4px 14px rgba(0,0,0,0.8), 0 0 10px rgba(56,189,248,0.3);"',
            c
        )
        if c != orig:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(c)

    print(f"Updated icon sizing across all {len(all_html)} HTML files!")

if __name__ == "__main__":
    upgrade_master()
