import os
import glob
import re

WIKI_ROOT = "/home/user/01_Somnarak_Wiki"
html_files = sorted(glob.glob(os.path.join(WIKI_ROOT, "**", "*.html"), recursive=True))

for fpath in html_files:
    rel = os.path.relpath(fpath, WIKI_ROOT)
    depth = rel.count(os.sep)
    prefix = "../" * depth
    
    rail_replacement = f"""<aside class="left-rail"><div class="site-mark"><a href="{prefix}index.html"><img src="{prefix}assets/icons/somnarak_icon.svg" alt="Somnarak"><b>SOMNARAK</b><span>WIKI ARCHIVE</span></a></div>
<nav class="left-links" aria-label="Wiki navigation">
<section><h2>Archive</h2>
<a href="{prefix}index.html">Main page</a>
<a href="{prefix}characters/index.html">Characters Hub</a>
<a href="{prefix}lore/index.html">Lore &amp; Cosmology</a>
<a href="{prefix}factions/index.html">Factions &amp; Guilds</a>
<a href="{prefix}departments/index.html">Hand of Change</a>
<a href="{prefix}locations/index.html">Atlas &amp; Maps</a>
<a href="{prefix}mechanics/index.html">Battle &amp; Systems</a>
<a href="{prefix}entities/index.html">Sorrow Entities</a>
<a href="{prefix}maw/index.html">M.A.W. Codex</a>
</section>
<section><h2>Echo-Cores</h2>
<a href="{prefix}characters/the-director-majin.html">Majin (Director)</a>
<a href="{prefix}characters/the-secretary-seiyon.html">Seiyon (Secretary)</a>
<a href="{prefix}characters/the-containment-lead-dekan.html">Dekan (Containment)</a>
<a href="{prefix}characters/the-extraction-lead-zyrak.html">Zyrak (Extraction)</a>
<a href="{prefix}characters/the-research-lead-ayshuk.html">Ayshuk (Research)</a>
<a href="{prefix}characters/the-border-lead-mellda.html">Mellda (Border)</a>
<a href="{prefix}characters/the-archive-lead-marjuk.html">Marjuk (Archive)</a>
<a href="{prefix}characters/the-outsider-ishall.html">Ishall (Outsider)</a>
<a href="{prefix}characters/the-exile-xyan.html">Xyan (Exile)</a>
</section>
<section><h2>The Palm</h2>
<a href="{prefix}departments/floor-1-neutral-command.html">Neutral Command</a>
<a href="{prefix}departments/floor-2-maws-keep.html">The Maw’s Keep</a>
<a href="{prefix}departments/floor-3-extraction-hall.html">Extraction Hall</a>
</section>
<section><h2>Fingers &amp; Wing</h2>
<a href="{prefix}departments/floor-4-insight-forge.html">Insight Forge</a>
<a href="{prefix}departments/floor-5-border-watch.html">Border Watch</a>
<a href="{prefix}departments/floor-6-deep-vault.html">Deep Vault</a>
<a href="{prefix}departments/floor-7-shadow-corps.html">Shadow Corps</a>
<a href="{prefix}departments/floor-8-gate-watch.html">Gate Watch</a>
</section>
</nav></aside>"""

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
        
    if "<aside class=\"left-rail\">" in content:
        new_content = re.sub(r'<aside class="left-rail">[\s\S]*?</aside>', rail_replacement, content, count=1)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)

print("Synchronized left rail across all 93 HTML files.")
