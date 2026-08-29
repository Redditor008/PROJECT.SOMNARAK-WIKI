import os
import re

CHAR_DIR = "/home/user/01_Somnarak_Wiki/characters"
os.makedirs(CHAR_DIR, exist_ok=True)

# Helper to generate left rail
def get_left_rail(depth=1):
    prefix = "../" if depth == 1 else ""
    return f"""<aside class="left-rail"><div class="site-mark"><a href="{prefix}index.html"><img src="{prefix}assets/icons/somnarak_icon.svg" alt="Somnarak"><b>SOMNARAK</b><span>WIKI ARCHIVE</span></a></div>
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
<a href="{prefix}characters/the-director-majin.html">Majin (The Director)</a>
<a href="{prefix}characters/the-secretary-seiyon.html">Seiyon (The Secretary)</a>
<a href="{prefix}characters/the-containment-lead-dekan.html">Dekan (Containment)</a>
<a href="{prefix}characters/the-extraction-lead-zyrak.html">Zyrak (Extraction)</a>
<a href="{prefix}characters/the-research-lead-ayshuk.html">Ayshuk (Research)</a>
<a href="{prefix}characters/the-border-lead-mellda.html">Mellda (Border)</a>
<a href="{prefix}characters/the-archive-lead-marjuk.html">Marjuk (Archive)</a>
<a href="{prefix}characters/the-outsider-ishall.html">Ishall (Outsider)</a>
<a href="{prefix}characters/the-exile-xyan.html">Xyan (The Exile)</a>
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

def get_floor_rail(depth=1):
    prefix = "../" if depth == 1 else ""
    return f"""<aside class="floor-rail" aria-label="Hand of Change departments"><h2>HAND OF CHANGE</h2>
<a class="floor-button f1" href="{prefix}departments/floor-1-neutral-command.html" style="--floor:#ef5b55"><span><small>FLOOR 1</small>NEUTRAL</span><img src="{prefix}assets/layout/hand/icons/icon_dept_f1_neutral.svg" alt=""></a>
<a class="floor-button f2" href="{prefix}departments/floor-2-maws-keep.html" style="--floor:#6f7ee8"><span><small>FLOOR 2</small>MAW’S KEEP</span><img src="{prefix}assets/layout/hand/icons/icon_dept_f2_maws_keep.svg" alt=""></a>
<a class="floor-button f3" href="{prefix}departments/floor-3-extraction-hall.html" style="--floor:#e6c94d"><span><small>FLOOR 3</small>EXTRACTION HALL</span><img src="{prefix}assets/layout/hand/icons/icon_dept_f3_extraction.svg" alt=""></a>
<a class="floor-button f4" href="{prefix}departments/floor-4-insight-forge.html" style="--floor:#47c978"><span><small>FLOOR 4</small>INSIGHT FORGE</span><img src="{prefix}assets/layout/hand/icons/icon_dept_f4_insight_forge.svg" alt=""></a>
<a class="floor-button f5" href="{prefix}departments/floor-5-border-watch.html" style="--floor:#d7d7d7"><span><small>FLOOR 5</small>BORDER WATCH</span><img src="{prefix}assets/layout/hand/icons/icon_dept_f5_border_watch.svg" alt=""></a>
<a class="floor-button f6" href="{prefix}departments/floor-6-deep-vault.html" style="--floor:#8d2e42"><span><small>FLOOR 6</small>DEEP VAULT</span><img src="{prefix}assets/layout/hand/icons/icon_dept_f6_deep_vault.svg" alt=""></a>
<a class="floor-button f7" href="{prefix}departments/floor-7-shadow-corps.html" style="--floor:#f0a6c4"><span><small>FLOOR 7</small>SHADOW CORPS</span><img src="{prefix}assets/layout/hand/icons/icon_dept_f7_shadow_corps.svg" alt=""></a>
<a class="floor-button f8" href="{prefix}departments/floor-8-gate-watch.html" style="--floor:#f4efa0"><span><small>FLOOR 8</small>GATE WATCH</span><img src="{prefix}assets/layout/hand/icons/icon_dept_f8_gate_watch.svg" alt=""></a>
<a class="rail-action" href="{prefix}departments/index.html">OPEN FACILITY DIRECTORY</a></aside>"""

def get_header(depth=1):
    prefix = "../" if depth == 1 else ""
    return f"""<header class="utility"><button class="nav-open" type="button" aria-label="Open navigation">☰</button><a class="utility-brand" href="{prefix}index.html">SOMNARAK.WIKI</a><span>YEAR 4,238 · DAWN INITIATIVE</span><nav><a class="selected" href="#content">Read</a><a href="{prefix}characters/index.html">Characters</a><a href="{prefix}entities/index.html">Sorrow Entities</a><a href="{prefix}maw/index.html">M.A.W.</a></nav><div class="search"><input id="search" data-index="{prefix}data/search.json" aria-label="Search" placeholder="Search Somnarak Wiki"><div id="results"></div></div></header>"""

def get_footer():
    return """<footer><div><b>SOMNARAK WIKI</b><br>Encyclopedia of the City of Unresolved Sorrow</div><div>Current record: Year 4,238 · Dawn Initiative</div><div>The Cycle has ended.<br>Xyan is home and commands Gate Watch.</div></footer>"""

print("Character builder helper loaded.")
