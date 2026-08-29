import os, sys, glob, re
sys.path.insert(0, '/home/user')
from tools.build_deep_canon_wiki import get_base_template
from tools.convert_echo_cores import parse_markdown_to_wiki_sections, format_lines_to_html

ABS_DIR = "/home/user/salvaged_source_materials/FOR WIKI/00_Source_Materials/Absolvohan"
WIKI_DIR = "/home/user/01_Somnarak_Wiki"

content_parts = []
toc_items = [
    ("overview", "Overview of the 1,778 Cycles"),
    ("singularity-mechanics", "The Absolvohan Singularity & Reset Protocol")
]

content_parts.append('''
<section class="wiki-section" id="overview">
  <h2 class="section-title">Overview of the 1,778 Cycles</h2>
  <div class="wiki-callout">
    <p><strong>CANONICAL CHRONICLE:</strong> The temporal loop known as <em>Absolvohan</em> (시간의 순환) spans 1,778 iterations of a 365-day cycle orchestrated by <a href="../characters/the-director-majin.html" class="wiki-link">Director Majin</a> to achieve the Singularity condition for the Dawn of Hope.</p>
  </div>
  <p>Beneath the canopy of the <a href="../lore/the-alpha-tree.html" class="wiki-link">Alpha Tree</a>, inside the subterranean complex of the <a href="../atlas/hand-of-change-map.html" class="wiki-link">Hand of Change</a>, time does not flow linearly. When the terminal reset occurs at Day 365, all structural damage, agent casualties, and containment breaches revert to Day 0. Only Director Majin and specific Echo-Core resonance matrices retain cognitive persistence across iterations.</p>
</section>

<section class="wiki-section" id="singularity-mechanics">
  <h2 class="section-title">The Absolvohan Singularity &amp; Reset Protocol</h2>
  <div class="table-wrap">
    <table class="wiki-table">
      <thead>
        <tr>
          <th>Cycle Phase</th>
          <th>Day Range</th>
          <th>Operational Focus</th>
          <th>Primary Hazards &amp; Manifestations</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Phase I: Initiation</strong></td>
          <td>Days 0 – 25</td>
          <td>Director awakening, early containment stabilization</td>
          <td>ZAYIN/TETH entity acclimatization, low-tier Han seeps</td>
        </tr>
        <tr>
          <td><strong>Phase II: Escalation</strong></td>
          <td>Days 29 – 73</td>
          <td>M.A.W. extraction expansion, Floor 3 &amp; 4 breakthroughs</td>
          <td>HE/WAW entity awakenings, acoustic echoes from The Desolate</td>
        </tr>
        <tr>
          <td><strong>Phase III: Taboo Cascade</strong></td>
          <td>Days 77 – 121</td>
          <td>Echo-Core memory bleed audits, Floor 6 Vault checks</td>
          <td>Taboo resonance backfires, soul calcification spikes</td>
        </tr>
        <tr>
          <td><strong>Phase IV: Incursion</strong></td>
          <td>Days 125 – 177</td>
          <td>Deep Desolate expeditions, Underworld containment clashes</td>
          <td>ALEPH-grade breaches, Ordeal Tide Watches (Midnight)</td>
        </tr>
        <tr>
          <td><strong>Phase V: Singularity</strong></td>
          <td>Days 350 – 365</td>
          <td>Alpha Siphon saturation, terminal convergence</td>
          <td>Temporal fracture collapse, Cycle 1,778 Dawn Breakthrough</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>
''')

# Add each of the 9 Parts
for i in range(1, 10):
    part_file = os.path.join(ABS_DIR, f"ABSOLOVHAN PART {i}.md")
    if os.path.exists(part_file):
        with open(part_file, 'r', encoding='utf-8') as fp:
            p_text = fp.read()
        p_q, p_auth, p_sections = parse_markdown_to_wiki_sections(p_text)
        part_title = f"Absolvohan Part {i} — " + (p_sections[0][0] if p_sections else f"Days {i*40}")
        part_id = f"absolvohan-part-{i}"
        toc_items.append((part_id, part_title))
        
        part_body = []
        if p_q:
            part_body.append(f'<div class="wiki-quote"><p>“{p_q}”</p><div class="quote-author">— {p_auth or "Absolvohan Record"}</div></div>')
            
        for st, slines in p_sections:
            part_body.append(f'<h3>{st}</h3>{format_lines_to_html(slines)}')
            
        content_parts.append(f'''
        <section class="wiki-section" id="{part_id}">
          <h2 class="section-title">{part_title}</h2>
          {''.join(part_body)}
        </section>
        ''')

full_html = get_base_template(
    title="The Cycle & Absolvohan (시간의 순환)",
    category_label="Lore & World",
    category_href="lore/index.html",
    rel_prefix="../",
    content_html='\n'.join(content_parts),
    toc_items=toc_items
)

out_p = os.path.join(WIKI_DIR, "lore/the-cycle-and-absolvohan.html")
with open(out_p, 'w', encoding='utf-8') as f:
    f.write(full_html)

print(f"Generated complete Absolvohan chronicle: lore/the-cycle-and-absolvohan.html ({len(full_html)} chars, {len(toc_items)} sections)")
