import os
import re

WIKI_DIR = "/home/user/01_Somnarak_Wiki"
SOURCE_DIR = "/home/user/salvaged_source_materials/FOR WIKI/00_Source_Materials"

# Read character markdown source files
char_files = {
    "the-director-majin.html": ("THE_DIRECTOR.md", "Director Majin", "Floor 1: Neutral Command", "Pure Han", "#ef5b55", "Majin"),
    "the-secretary-seiyon.html": ("THE_SECRETARY.md", "Secretary Seiyon", "Floor 1: Neutral Command", "Ferrehan", "#ef5b55", "Seiyon"),
    "the-containment-lead-dekan.html": ("THE_CONTAINMENT_LEAD.md", "Containment Lead Dekan", "Floor 2: Maw's Keep", "Iron Han / Pugnahan", "#6f7ee8", "Dekan"),
    "the-extraction-lead-zyrak.html": ("THE_EXTRACTION_LEAD.md", "Extraction Lead Zyrak", "Floor 3: Extraction Hall", "Weaver Han / Flerehan", "#e6c94d", "Zyrak"),
    "the-research-lead-ayshuk.html": ("THE_RESEARCH_LEAD.md", "Research Lead Ayshuk", "Floor 4: Insight Forge", "Insight Han / Viderehan", "#47c978", "Ayshuk"),
    "the-border-lead-mellda.html": ("THE_BORDER_LEAD.md", "Border Lead Mellda", "Floor 5: Border Watch", "Border Han / Aegis Pure", "#d7d7d7", "Mellda"),
    "the-archive-lead-marjuk.html": ("THE_ARCHIVE_LEAD.md", "Archive Lead Marjuk", "Floor 6: Deep Vault", "Deep Archive Han", "#8d2e42", "Marjuk"),
    "the-outsider-ishall.html": ("THE_OUTSIDER.md", "The Outsider Ishall", "Floor 7: Shadow Corps", "Shadow Han / Void", "#f0a6c4", "Ishall"),
    "the-exile-xyan.html": ("THE_EXILE.md", "The Exile Xyan", "Floor 8: Gate Watch", "Gate Watch Han / Dawn Light", "#f4efa0", "Xyan"),
}

def clean_md_to_html(md_text):
    # Remove leading markdown headers and convert sections
    lines = md_text.split('\n')
    out = []
    in_list = False
    in_table = False
    table_lines = []

    def flush_table():
        nonlocal in_table, table_lines
        if not table_lines:
            return ""
        header = table_lines[0]
        html_t = '<div class="table-wrap"><table class="data-table"><thead><tr>'
        for c in [x.strip() for x in header.split('|')[1:-1]]:
            html_t += f'<th>{c}</th>'
        html_t += '</tr></thead><tbody>'
        for r in table_lines[2:]:
            cols = [x.strip() for x in r.split('|')[1:-1]]
            if any(cols):
                html_t += '<tr>' + ''.join(f'<td>{c}</td>' for c in cols) + '</tr>'
        html_t += '</tbody></table></div>'
        table_lines = []
        in_table = False
        return html_t

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty
        if not line:
            if in_list:
                out.append('</ul>')
                in_list = False
            if in_table:
                out.append(flush_table())
            i += 1
            continue

        # Skip table of contents markers
        if re.match(r'^#{1,3}\s*(?:Contents|Table of Contents)', line, re.IGNORECASE):
            i += 1
            while i < len(lines) and (lines[i].strip().startswith(('-', '*', '1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.')) or not lines[i].strip()):
                i += 1
            continue

        # Tables
        if line.startswith('|') and line.endswith('|'):
            if in_list:
                out.append('</ul>')
                in_list = False
            in_table = True
            table_lines.append(line)
            i += 1
            continue
        elif in_table:
            out.append(flush_table())

        # Headers
        if line.startswith('#'):
            if in_list:
                out.append('</ul>')
                in_list = False
            level = len(line.split()[0])
            text = line.lstrip('#').strip()
            # Clean outline numbers like "1. Profile" -> "Profile"
            text = re.sub(r'^\d+\.\s*', '', text)
            tag = f'h{min(level + 1, 4)}'
            # Convert formatting inside header
            text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
            out.append(f'<{tag}>{text}</{tag}>')
            i += 1
            continue

        # Lists
        if line.startswith(('-', '*', '+')) and not line.startswith('---'):
            if in_table:
                out.append(flush_table())
            if not in_list:
                out.append('<ul>')
                in_list = True
            item_text = line.lstrip('-*+ ').strip()
            item_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', item_text)
            item_text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', item_text)
            item_text = re.sub(r'`(.*?)`', r'<code>\1</code>', item_text)
            out.append(f'<li>{item_text}</li>')
            i += 1
            continue

        # Numbered list
        if re.match(r'^\d+\.\s+', line):
            if in_table:
                out.append(flush_table())
            if not in_list:
                out.append('<ol>')
                in_list = True
            item_text = re.sub(r'^\d+\.\s+', '', line)
            item_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', item_text)
            item_text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', item_text)
            item_text = re.sub(r'`(.*?)`', r'<code>\1</code>', item_text)
            out.append(f'<li>{item_text}</li>')
            i += 1
            continue

        if in_list:
            out.append('</ul>')
            in_list = False

        # Blockquotes
        if line.startswith('>'):
            quote_text = line.lstrip('> ').strip()
            quote_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', quote_text)
            quote_text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', quote_text)
            out.append(f'<blockquote class="dossier-quote">{quote_text}</blockquote>')
            i += 1
            continue

        # Paragraphs
        p_text = line
        p_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', p_text)
        p_text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', p_text)
        p_text = re.sub(r'`(.*?)`', r'<code>\1</code>', p_text)
        # Convert markdown links [text](url) -> <a href="url">text</a>
        p_text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', p_text)
        out.append(f'<p>{p_text}</p>')
        i += 1

    if in_list:
        out.append('</ul>')
    if in_table:
        out.append(flush_table())

    return '\n'.join(out)

for html_name, (src_md, title, dept, han_type, color, short_name) in char_files.items():
    md_path = os.path.join(SOURCE_DIR, "Character_Wiki", src_md)
    if not os.path.exists(md_path):
        continue
    with open(md_path, "r", encoding="utf-8") as f:
        raw_md = f.read()

    body_content = clean_md_to_html(raw_md)

    page_html = f"""<!doctype html>
<html lang="en" data-article-status="curated">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{title} — Somnarak Wiki</title>
  <meta name="description" content="Official Reverie Directorate archival dossier for {title}, {dept}. Echo-Core Resonance: {han_type}.">
  <link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg">
  <link rel="stylesheet" href="../assets/css/wiki.css">
  <script defer src="../assets/js/wiki.js"></script>
</head>
<body>
<header class="utility">
  <button class="nav-open" type="button" aria-label="Open navigation">☰</button>
  <a class="utility-brand" href="../index.html">SOMNARAK.WIKI</a>
  <span>YEAR 4,238 · DAWN INITIATIVE</span>
  <nav>
    <a href="../index.html">Main page</a>
    <a class="selected" href="index.html">Characters</a>
    <a href="../lore/index.html">Lore</a>
    <a href="../factions/index.html">Factions</a>
    <a href="../entities/index.html">Sorrow Entities</a>
    <a href="../maw/index.html">M.A.W.</a>
  </nav>
  <div class="search">
    <input id="search" data-index="../data/search.json" aria-label="Search" placeholder="Search Somnarak Wiki">
    <div id="results"></div>
  </div>
</header>

<div class="wiki-shell">
  <aside class="left-rail">
    <div class="site-mark">
      <a href="../index.html">
        <img src="../assets/icons/somnarak_icon.svg" alt="Somnarak">
        <b>SOMNARAK</b>
        <span>WIKI ARCHIVE</span>
      </a>
    </div>
    <nav class="left-links" aria-label="Wiki navigation">
      <section>
        <h2>Archive</h2>
        <a href="../index.html">Main page</a>
        <a href="index.html">Characters Hub</a>
        <a href="../lore/index.html">Lore &amp; Cosmology</a>
        <a href="../factions/index.html">Factions &amp; Guilds</a>
        <a href="../departments/index.html">Hand of Change</a>
        <a href="../locations/index.html">Atlas &amp; Maps</a>
        <a href="../mechanics/index.html">Battle &amp; Systems</a>
        <a href="../entities/index.html">Sorrow Entities</a>
        <a href="../maw/index.html">M.A.W. Codex</a>
      </section>
      <section>
        <h2>Echo-Cores</h2>
        <a href="the-director-majin.html" {"style='color:#fff;font-weight:bold;'" if "majin" in html_name else ""}>Majin (Director)</a>
        <a href="the-secretary-seiyon.html" {"style='color:#fff;font-weight:bold;'" if "seiyon" in html_name else ""}>Seiyon (Secretary)</a>
        <a href="the-containment-lead-dekan.html" {"style='color:#fff;font-weight:bold;'" if "dekan" in html_name else ""}>Dekan (Containment)</a>
        <a href="the-extraction-lead-zyrak.html" {"style='color:#fff;font-weight:bold;'" if "zyrak" in html_name else ""}>Zyrak (Extraction)</a>
        <a href="the-research-lead-ayshuk.html" {"style='color:#fff;font-weight:bold;'" if "ayshuk" in html_name else ""}>Ayshuk (Research)</a>
        <a href="the-border-lead-mellda.html" {"style='color:#fff;font-weight:bold;'" if "mellda" in html_name else ""}>Mellda (Border)</a>
        <a href="the-archive-lead-marjuk.html" {"style='color:#fff;font-weight:bold;'" if "marjuk" in html_name else ""}>Marjuk (Archive)</a>
        <a href="the-outsider-ishall.html" {"style='color:#fff;font-weight:bold;'" if "ishall" in html_name else ""}>Ishall (Outsider)</a>
        <a href="the-exile-xyan.html" {"style='color:#fff;font-weight:bold;'" if "xyan" in html_name else ""}>Xyan (Exile)</a>
      </section>
    </nav>
  </aside>

  <main id="content">
    <div class="page-tabs">
      <span>Archival Dossier</span>
      <b>ECHO-CORE REGISTRY // YEAR 4,238</b>
    </div>
    <div class="breadcrumbs">
      <a href="../index.html">Main page</a><i>›</i><a href="index.html">Characters</a><i>›</i>{title}
    </div>

    <!-- Department Hero Header -->
    <section class="department-hero" style="--floor:{color}">
      <img src="../assets/icons/banner_characters.svg" alt="">
      <div>
        <span>REVERIE DIRECTORATE // DOSSIER CLASSIFICATION</span>
        <h1>{title}</h1>
        <p>{dept} · Resonance: <strong>{han_type}</strong></p>
      </div>
    </section>

    <!-- Infobox Data Table -->
    <div class="entity-meta-grid" style="margin: 20px 0;">
      <div class="meta-card">
        <b>DESIGNATION</b>
        <span>{title}</span>
      </div>
      <div class="meta-card">
        <b>FACILITY SECTOR</b>
        <span>{dept}</span>
      </div>
      <div class="meta-card">
        <b>HAN RESONANCE</b>
        <span>{han_type}</span>
      </div>
      <div class="meta-card">
        <b>CURRENT STATUS</b>
        <span>Active · Dawn Initiative</span>
      </div>
    </div>

    <!-- Body Content -->
    <article class="article-body">
      {body_content}
    </article>
  </main>

  <aside class="floor-rail" aria-label="Hand of Change departments">
    <h2>HAND OF CHANGE</h2>
    <a class="floor-button f1" href="../departments/floor-1-neutral-command.html" style="--floor:#ef5b55"><span><small>FLOOR 1</small>NEUTRAL</span><img src="../assets/layout/hand/icons/icon_dept_f1_neutral.svg" alt=""></a>
    <a class="floor-button f2" href="../departments/floor-2-maws-keep.html" style="--floor:#6f7ee8"><span><small>FLOOR 2</small>MAW’S KEEP</span><img src="../assets/layout/hand/icons/icon_dept_f2_maws_keep.svg" alt=""></a>
    <a class="floor-button f3" href="../departments/floor-3-extraction-hall.html" style="--floor:#e6c94d"><span><small>FLOOR 3</small>EXTRACTION HALL</span><img src="../assets/layout/hand/icons/icon_dept_f3_extraction.svg" alt=""></a>
    <a class="floor-button f4" href="../departments/floor-4-insight-forge.html" style="--floor:#47c978"><span><small>FLOOR 4</small>INSIGHT FORGE</span><img src="../assets/layout/hand/icons/icon_dept_f4_insight_forge.svg" alt=""></a>
    <a class="floor-button f5" href="../departments/floor-5-border-watch.html" style="--floor:#d7d7d7"><span><small>FLOOR 5</small>BORDER WATCH</span><img src="../assets/layout/hand/icons/icon_dept_f5_border_watch.svg" alt=""></a>
    <a class="floor-button f6" href="../departments/floor-6-deep-vault.html" style="--floor:#8d2e42"><span><small>FLOOR 6</small>DEEP VAULT</span><img src="../assets/layout/hand/icons/icon_dept_f6_deep_vault.svg" alt=""></a>
    <a class="floor-button f7" href="../departments/floor-7-shadow-corps.html" style="--floor:#f0a6c4"><span><small>FLOOR 7</small>SHADOW CORPS</span><img src="../assets/layout/hand/icons/icon_dept_f7_shadow_corps.svg" alt=""></a>
    <a class="floor-button f8" href="../departments/floor-8-gate-watch.html" style="--floor:#f4efa0"><span><small>FLOOR 8</small>GATE WATCH</span><img src="../assets/layout/hand/icons/icon_dept_f8_gate_watch.svg" alt=""></a>
    <a class="rail-action" href="../departments/index.html">OPEN FACILITY DIRECTORY</a>
  </aside>
</div>

<footer>
  <div><b>SOMNARAK WIKI</b><br>Encyclopedia of the City of Unresolved Sorrow</div>
  <div>Current record: Year 4,238 · Dawn Initiative</div>
  <div>The Cycle has ended.<br>Xyan is home and commands Gate Watch.</div>
</footer>
</body>
</html>
"""
    dest_path = os.path.join(WIKI_DIR, "characters", html_name)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(page_html)
    print(f"Generated complete character dossier for {html_name} ({len(page_html)} bytes)")
