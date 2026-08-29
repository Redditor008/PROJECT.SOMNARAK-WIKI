import os
import re

def upgrade_tables_and_icons():
    wiki_root = "/home/user/01_Somnarak_Wiki"
    css_file = os.path.join(wiki_root, "assets/css/wiki.css")

    # 1. UPDATE CSS WITH EXTREMELY PROMINENT TABLE BORDERS AND ICON SIZES
    table_css_upgrade = '''
/* ==========================================================================
   ULTRA-PROMINENT INDUSTRIAL TABLE BORDERS & ENLARGED ICON SYSTEM
   ========================================================================== */

/* 1. MASTER TABLE WRAPPERS WITH GLOWING HIGH-CONTRAST BORDERS */
.table-wrap,
.pm-table-wrapper,
.wiki-table-container,
.data-table-wrap {
  width: 100% !important;
  overflow-x: auto !important;
  -webkit-overflow-scrolling: touch !important;
  margin: 1.8rem 0 2.4rem !important;
  background: #070c16 !important;
  border: 3px solid #f1df76 !important; /* Bold Gold Border */
  border-radius: 8px !important;
  box-shadow: 0 10px 35px rgba(0, 0, 0, 0.9), 0 0 20px rgba(241, 223, 118, 0.25), inset 0 0 15px rgba(56, 189, 248, 0.1) !important;
  padding: 2px !important;
}

/* 2. MASTER TABLES - CRISP GRID BORDERS ON EVERY CELL */
table,
table.wiki-table,
table.pm-table,
.pm-table,
.wiki-table,
.data-table table,
.home-table,
.source-table {
  width: 100% !important;
  border-collapse: collapse !important; /* Sharp grid borders */
  border-spacing: 0 !important;
  font-size: 0.95rem !important;
  text-align: left !important;
  color: #e2e8f0 !important;
  background: #080e1a !important;
  border: 2px solid #38bdf8 !important; /* Bold Cyan Grid */
}

/* 3. TABLE HEADERS - PROMINENT METALLIC BARS WITH GOLD LABELS */
table th,
table.wiki-table th,
table.pm-table th,
.pm-table th,
.wiki-table th,
.data-table th,
.home-table th,
.source-table th {
  background: linear-gradient(180deg, #1e334f 0%, #0f1c2e 100%) !important;
  color: #f1df76 !important;
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 0.95rem !important;
  letter-spacing: 0.09em !important;
  text-transform: uppercase !important;
  padding: 14px 18px !important;
  border: 2px solid #2b4566 !important;
  border-bottom: 3px solid #38bdf8 !important;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.9) !important;
}

/* 4. TABLE BODY CELLS - BOLD HIGH-CONTRAST BORDERS */
table td,
table.wiki-table td,
table.pm-table td,
.pm-table td,
.wiki-table td,
.data-table td,
.home-table td,
.source-table td {
  padding: 14px 18px !important;
  border: 1.5px solid #253a54 !important; /* Very visible cell borders */
  color: #cbd5e1 !important;
  font-size: 0.95rem !important;
  line-height: 1.6 !important;
  background: rgba(11, 18, 30, 0.9) !important;
  vertical-align: middle !important;
}

/* 5. ZEBRA STRIPING & HOVER */
table tbody tr:nth-child(even) td,
table.wiki-table tbody tr:nth-child(even) td,
table.pm-table tbody tr:nth-child(even) td {
  background: rgba(18, 30, 48, 0.95) !important;
}

table tbody tr:hover td,
table.wiki-table tbody tr:hover td,
table.pm-table tbody tr:hover td {
  background: rgba(56, 189, 248, 0.22) !important;
  color: #ffffff !important;
  border-color: #38bdf8 !important;
}

/* 6. ENLARGED IN-TEXT & IN-TABLE ICONS */
table td img,
.pm-table td img,
.wiki-table td img,
.in-text-icon,
.table-inline-icon {
  width: 32px !important;
  height: 32px !important;
  min-width: 32px !important;
  min-height: 32px !important;
  vertical-align: middle !important;
  margin-right: 10px !important;
  display: inline-block !important;
  border-radius: 6px !important;
  border: 1px solid rgba(56, 189, 248, 0.5) !important;
  background: #090d16 !important;
  padding: 2px !important;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.6) !important;
}

/* 7. ENLARGED STANDALONE CARD & HUB ICONS (NOT PART OF TEXT) */
.entity-card-icon,
.pm-entity-card .entity-card-icon,
.hub-card-icon,
.dept-card-icon,
.portal-cat-icon {
  width: 96px !important;
  height: 96px !important;
  min-width: 96px !important;
  min-height: 96px !important;
  object-fit: contain !important;
  margin-bottom: 12px !important;
  border-radius: 8px !important;
  border: 2px solid rgba(241, 223, 118, 0.4) !important;
  background: #080d17 !important;
  padding: 6px !important;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.8), 0 0 12px rgba(56, 189, 248, 0.2) !important;
}

/* Cross-Reference Directory Bottom Cards */
.cross-ref-card img {
  width: 64px !important;
  height: 64px !important;
  min-width: 64px !important;
  min-height: 64px !important;
  border-radius: 6px !important;
  padding: 4px !important;
  border: 1.5px solid #38bdf8 !important;
  background: #080d16 !important;
}

/* Department Directory Grid Icons */
.department-directory img {
  width: 64px !important;
  height: 64px !important;
  min-width: 64px !important;
  min-height: 64px !important;
}

/* Left Rail Site Mark Icon */
.site-mark img {
  width: 64px !important;
  height: 64px !important;
}

/* Right Rail Avatars */
.floor-avatar-wrap img {
  width: 56px !important;
  height: 56px !important;
}
'''

    with open(css_file, "a", encoding="utf-8") as f:
        f.write("\n" + table_css_upgrade + "\n")
    print("Appended ultra-prominent table border and enlarged icon rules to wiki.css!")

    # 2. UPDATE ALL HTML FILES: Replace tiny in-line icon widths (16px, 18px, 20px, 24px) with 32px and style badges
    html_files = []
    for root, dirs, files in os.walk(wiki_root):
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))

    updated_count = 0
    for file_path in html_files:
        with open(file_path, "r", encoding="utf-8") as f:
            html = f.read()

        original_html = html

        # Replace style="width:16px;..." or style="width:18px;..." or style="width:20px;..." with 32px high-visibility styling
        # Regex for in-text/in-table images
        html = re.sub(
            r'style="width:(?:16|18|20|22|24)px;vertical-align:middle;margin-right:(?:6|8)px;"',
            r'style="width:32px;height:32px;vertical-align:middle;margin-right:10px;display:inline-block;border-radius:4px;border:1px solid rgba(56,189,248,0.5);background:#090d16;padding:2px;"',
            html
        )

        # Also handle any generic width:16px or width:18px or width:20px on img tags inside tables
        html = re.sub(
            r'<img\s+src="([^"]+)"\s+alt=""\s+style="width:(?:16|18|20|24)px;[^"]*"',
            r'<img src="\1" alt="" style="width:32px;height:32px;vertical-align:middle;margin-right:10px;display:inline-block;border-radius:4px;border:1px solid rgba(56,189,248,0.5);background:#090d16;padding:2px;"',
            html
        )

        if html != original_html:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(html)
            updated_count += 1

    print(f"Updated in-text and in-table icon sizes across {updated_count} HTML files to 32px!")

if __name__ == "__main__":
    upgrade_tables_and_icons()
