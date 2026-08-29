import os
import re

CHAR_DIR = "/home/user/01_Somnarak_Wiki/characters"
os.makedirs(CHAR_DIR, exist_ok=True)

def get_left_rail():
    return """<aside class="left-rail"><div class="site-mark"><a href="../index.html"><img src="../assets/icons/somnarak_icon.svg" alt="Somnarak"><b>SOMNARAK</b><span>WIKI ARCHIVE</span></a></div>
<nav class="left-links" aria-label="Wiki navigation">
<section><h2>Archive</h2>
<a href="../index.html">Main page</a>
<a href="../characters/index.html">Characters Hub</a>
<a href="../lore/index.html">Lore &amp; Cosmology</a>
<a href="../factions/index.html">Factions &amp; Guilds</a>
<a href="../departments/index.html">Hand of Change</a>
<a href="../locations/index.html">Atlas &amp; Maps</a>
<a href="../mechanics/index.html">Battle &amp; Systems</a>
<a href="../entities/index.html">Sorrow Entities</a>
<a href="../maw/index.html">M.A.W. Codex</a>
</section>
<section><h2>Echo-Cores</h2>
<a href="the-director-majin.html">Majin (Director)</a>
<a href="the-secretary-seiyon.html">Seiyon (Secretary)</a>
<a href="the-containment-lead-dekan.html">Dekan (Containment)</a>
<a href="the-extraction-lead-zyrak.html">Zyrak (Extraction)</a>
<a href="the-research-lead-ayshuk.html">Ayshuk (Research)</a>
<a href="the-border-lead-mellda.html">Mellda (Border)</a>
<a href="the-archive-lead-marjuk.html">Marjuk (Archive)</a>
<a href="the-outsider-ishall.html">Ishall (Outsider)</a>
<a href="the-exile-xyan.html">Xyan (Exile)</a>
</section>
<section><h2>Cast &amp; Figures</h2>
<a href="kael.html">Kael (Warden Lead)</a>
<a href="soojin.html">Soojin (Master Weaver)</a>
<a href="cheonbulok-refugees.html">Cheonbulok Refugees</a>
<a href="high-architects.html">High Architects</a>
</section>
<section><h2>The Palm</h2>
<a href="../departments/floor-1-neutral-command.html">Neutral Command</a>
<a href="../departments/floor-2-maws-keep.html">The Maw’s Keep</a>
<a href="../departments/floor-3-extraction-hall.html">Extraction Hall</a>
</section>
<section><h2>Fingers &amp; Wing</h2>
<a href="../departments/floor-4-insight-forge.html">Insight Forge</a>
<a href="../departments/floor-5-border-watch.html">Border Watch</a>
<a href="../departments/floor-6-deep-vault.html">Deep Vault</a>
<a href="../departments/floor-7-shadow-corps.html">Shadow Corps</a>
<a href="../departments/floor-8-gate-watch.html">Gate Watch</a>
</section>
</nav></aside>"""

def get_floor_rail():
    return """<aside class="floor-rail" aria-label="Hand of Change departments"><h2>HAND OF CHANGE</h2>
<a class="floor-button f1" href="../departments/floor-1-neutral-command.html" style="--floor:#ef5b55"><span><small>FLOOR 1</small>NEUTRAL</span><img src="../assets/layout/hand/icons/icon_dept_f1_neutral.svg" alt=""></a>
<a class="floor-button f2" href="../departments/floor-2-maws-keep.html" style="--floor:#6f7ee8"><span><small>FLOOR 2</small>MAW’S KEEP</span><img src="../assets/layout/hand/icons/icon_dept_f2_maws_keep.svg" alt=""></a>
<a class="floor-button f3" href="../departments/floor-3-extraction-hall.html" style="--floor:#e6c94d"><span><small>FLOOR 3</small>EXTRACTION HALL</span><img src="../assets/layout/hand/icons/icon_dept_f3_extraction.svg" alt=""></a>
<a class="floor-button f4" href="../departments/floor-4-insight-forge.html" style="--floor:#47c978"><span><small>FLOOR 4</small>INSIGHT FORGE</span><img src="../assets/layout/hand/icons/icon_dept_f4_insight_forge.svg" alt=""></a>
<a class="floor-button f5" href="../departments/floor-5-border-watch.html" style="--floor:#d7d7d7"><span><small>FLOOR 5</small>BORDER WATCH</span><img src="../assets/layout/hand/icons/icon_dept_f5_border_watch.svg" alt=""></a>
<a class="floor-button f6" href="../departments/floor-6-deep-vault.html" style="--floor:#8d2e42"><span><small>FLOOR 6</small>DEEP VAULT</span><img src="../assets/layout/hand/icons/icon_dept_f6_deep_vault.svg" alt=""></a>
<a class="floor-button f7" href="../departments/floor-7-shadow-corps.html" style="--floor:#f0a6c4"><span><small>FLOOR 7</small>SHADOW CORPS</span><img src="../assets/layout/hand/icons/icon_dept_f7_shadow_corps.svg" alt=""></a>
<a class="floor-button f8" href="../departments/floor-8-gate-watch.html" style="--floor:#f4efa0"><span><small>FLOOR 8</small>GATE WATCH</span><img src="../assets/layout/hand/icons/icon_dept_f8_gate_watch.svg" alt=""></a>
<a class="rail-action" href="../departments/index.html">OPEN FACILITY DIRECTORY</a></aside>"""

def get_header():
    return """<header class="utility"><button class="nav-open" type="button" aria-label="Open navigation">☰</button><a class="utility-brand" href="../index.html">SOMNARAK.WIKI</a><span>YEAR 4,238 · DAWN INITIATIVE</span><nav><a class="selected" href="#content">Read</a><a href="index.html">Characters</a><a href="../entities/index.html">Sorrow Entities</a><a href="../maw/index.html">M.A.W.</a></nav><div class="search"><input id="search" data-index="../data/search.json" aria-label="Search" placeholder="Search Somnarak Wiki"><div id="results"></div></div></header>"""

def get_footer():
    return """<footer><div><b>SOMNARAK WIKI</b><br>Encyclopedia of the City of Unresolved Sorrow</div><div>Current record: Year 4,238 · Dawn Initiative</div><div>The Cycle has ended.<br>Xyan is home and commands Gate Watch.</div></footer>"""

print("Helper templates ready.")
