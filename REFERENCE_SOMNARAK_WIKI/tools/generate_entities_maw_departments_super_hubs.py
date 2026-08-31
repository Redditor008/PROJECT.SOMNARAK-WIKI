import os, sys
sys.path.insert(0, '/home/user')
from tools.build_deep_canon_wiki import get_base_template

WIKI_DIR = "/home/user/01_Somnarak_Wiki"

# ==============================================================================
# 6. DEPARTMENTS HUB (departments/index.html)
# ==============================================================================
dept_hub_html = '''
<div class="wiki-callout" style="border-left: 5px solid #f1df76; background: linear-gradient(135deg, #0d121c 0%, #06080d 100%);">
  <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
    <div>
      <span class="badge badge-canon" style="margin-bottom: 6px;">FACILITY ARCHITECTURE</span>
      <h2 style="margin: 0; color: #f1df76; font-size: 1.6rem; font-family: Impact, sans-serif;">HAND OF CHANGE — OPERATIONAL FLOORS</h2>
      <p style="margin: 4px 0 0; color: #94a3b8; font-size: 0.88rem;">The Subterranean Complex of the Reverie Directorate · 8 Operational Floors · Hand Architecture</p>
    </div>
    <div style="display: flex; gap: 8px;">
      <span class="badge badge-source">8 FLOORS</span>
      <span class="badge badge-source">12 BUREAUS</span>
      <span class="badge badge-source">10 INCIDENTS</span>
    </div>
  </div>
</div>

<section class="wiki-section" id="eight-facility-floors">
  <h2 class="section-title">The Eight Facility Floors (층별 구조)</h2>
  <p>The <strong>Hand of Change</strong> (변화의 손) descends vertically beneath the root bulb of the <a href="../lore/the-alpha-tree.html" class="wiki-link">Alpha Tree</a>. Each floor serves a distinct containment, industrial, or cognitive mandate overseen by a resident Echo-Core:</p>
  
  <div class="table-wrap">
    <table class="wiki-table">
      <thead>
        <tr>
          <th>Floor #</th>
          <th>Department Name</th>
          <th>Department Lead</th>
          <th>Primary Mandate</th>
          <th>Hazard Level</th>
          <th>Floor Action</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Floor 1</strong></td>
          <td><a href="floor-1-neutral-command.html" class="wiki-link">Neutral Command</a></td>
          <td><a href="../characters/the-director-majin.html" class="wiki-link">Director Majin</a></td>
          <td>Directorate Central Nexus, Alpha Siphon control, executive war room</td>
          <td><span class="badge badge-source">LEVEL 1 RESTRICTED</span></td>
          <td><a href="floor-1-neutral-command.html" class="action-btn">Enter Floor 1 →</a></td>
        </tr>
        <tr>
          <td><strong>Floor 2</strong></td>
          <td><a href="floor-2-maws-keep.html" class="wiki-link">Maw's Keep</a></td>
          <td><a href="../characters/the-secretary-seiyon.html" class="wiki-link">Seiyon</a> / <a href="../characters/the-containment-lead-dekan.html" class="wiki-link">Dekan</a></td>
          <td>ZAYIN/TETH/HE Sorrow Entity containment wards &amp; holding cells</td>
          <td><span class="badge badge-source">LEVEL 2 CONTAINMENT</span></td>
          <td><a href="floor-2-maws-keep.html" class="action-btn">Enter Floor 2 →</a></td>
        </tr>
        <tr>
          <td><strong>Floor 3</strong></td>
          <td><a href="floor-3-extraction-hall.html" class="wiki-link">Extraction Hall</a></td>
          <td><a href="../characters/the-extraction-lead-zyrak.html" class="wiki-link">Zyrak</a></td>
          <td>M.A.W. Siphoning furnaces, crystallization labs &amp; armory forging</td>
          <td><span class="badge badge-source">LEVEL 3 INDUSTRIAL</span></td>
          <td><a href="floor-3-extraction-hall.html" class="action-btn">Enter Floor 3 →</a></td>
        </tr>
        <tr>
          <td><strong>Floor 4</strong></td>
          <td><a href="floor-4-insight-forge.html" class="wiki-link">Insight Forge</a></td>
          <td><a href="../characters/the-research-lead-ayshuk.html" class="wiki-link">Ayshuk</a></td>
          <td>Han particle physics, soul resonance testing &amp; cognitive therapy labs</td>
          <td><span class="badge badge-source">LEVEL 4 RESEARCH</span></td>
          <td><a href="floor-4-insight-forge.html" class="action-btn">Enter Floor 4 →</a></td>
        </tr>
        <tr>
          <td><strong>Floor 5</strong></td>
          <td><a href="floor-5-border-watch.html" class="wiki-link">Border Watch</a></td>
          <td><a href="../characters/the-border-lead-mellda.html" class="wiki-link">Mellda</a></td>
          <td>Perimeter acoustic sensors, seismic radar &amp; external blast barriers</td>
          <td><span class="badge badge-source">LEVEL 5 DEFENSE</span></td>
          <td><a href="floor-5-border-watch.html" class="action-btn">Enter Floor 5 →</a></td>
        </tr>
        <tr>
          <td><strong>Floor 6</strong></td>
          <td><a href="floor-6-deep-vault.html" class="wiki-link">Deep Vault</a></td>
          <td><a href="../characters/the-archive-lead-marjuk.html" class="wiki-link">Marjuk</a></td>
          <td>Cryogenic storage of 1.4M citizen identities &amp; Precursor Relics</td>
          <td><span class="badge badge-source">LEVEL 6 VAULT</span></td>
          <td><a href="floor-6-deep-vault.html" class="action-btn">Enter Floor 6 →</a></td>
        </tr>
        <tr>
          <td><strong>Floor 7</strong></td>
          <td><a href="floor-7-shadow-corps.html" class="wiki-link">Shadow Corps</a></td>
          <td><a href="../characters/the-outsider-ishall.html" class="wiki-link">Ishall</a></td>
          <td>Void diving preparation, infiltration staging &amp; deep scout barracks</td>
          <td><span class="badge badge-source">LEVEL 7 RECON</span></td>
          <td><a href="floor-7-shadow-corps.html" class="action-btn">Enter Floor 7 →</a></td>
        </tr>
        <tr>
          <td><strong>Floor 8</strong></td>
          <td><a href="floor-8-gate-watch.html" class="wiki-link">Gate Watch</a></td>
          <td><a href="../characters/the-exile-xyan.html" class="wiki-link">Xyan</a></td>
          <td>The Forbidden Gate sealing the Abyssal Weeping River</td>
          <td><span class="badge badge-source" style="border-color: #ef4444; color: #ef4444;">LEVEL 8 HAZARD Ω</span></td>
          <td><a href="floor-8-gate-watch.html" class="action-btn">Enter Floor 8 →</a></td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

<section class="wiki-section" id="department-technical-archives">
  <h2 class="section-title">Department Technical Archives &amp; Incident Records</h2>
  <div class="archive-portal-grid" style="grid-template-columns: repeat(auto-fill, minmax(290px, 1fr)); gap: 16px; margin-top: 1rem;">
    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <a href="facility-room-types.html" style="color: #f1df76; font-size: 1.1rem; font-family: Impact, sans-serif; text-decoration: none; display: block; margin-bottom: 4px;">FACILITY ROOM TYPES</a>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">Catalog of standard room archetypes: Containment Units, Siphon Chambers, Blast Vestibules, Cryo-Vaults, and Quarantine Corridors.</p>
      <a href="facility-room-types.html" class="action-btn">View Architecture Specs →</a>
    </div>

    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <a href="incident-reports-archive.html" style="color: #f1df76; font-size: 1.1rem; font-family: Impact, sans-serif; text-decoration: none; display: block; margin-bottom: 4px;">INCIDENT REPORTS ARCHIVE</a>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">Declassified reports on 10 major facility breaches (Incidents 001 to 010), containment failures, and emergency purge interventions.</p>
      <a href="incident-reports-archive.html" class="action-btn">Examine Incident Logs →</a>
    </div>

    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <a href="../atlas/hand-of-change-map.html" style="color: #f1df76; font-size: 1.1rem; font-family: Impact, sans-serif; text-decoration: none; display: block; margin-bottom: 4px;">FACILITY CUTAWAY SCHEMATIC</a>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">Full-scale interactive cutaway diagram showing vertical elevators, power conduits, containment vaults, and floor connection gates.</p>
      <a href="../atlas/hand-of-change-map.html" class="action-btn">Open Interactive Blueprint →</a>
    </div>
  </div>
</section>
'''

toc_dept = [
    ("eight-facility-floors", "The Eight Facility Floors"),
    ("department-technical-archives", "Department Technical Archives & Incident Records")
]

p_dept = get_base_template("Facility Floors & Departments Hub", "Facility Floors", "departments/index.html", "../", dept_hub_html, toc_dept)
with open(os.path.join(WIKI_DIR, "departments/index.html"), 'w', encoding='utf-8') as f:
    f.write(p_dept)
print("Built Super Hub: departments/index.html")

# ==============================================================================
# 7. ENTITIES HUB (entities/index.html)
# ==============================================================================
ent_hub_html = '''
<div class="wiki-callout" style="border-left: 5px solid #ef4444; background: linear-gradient(135deg, #0d121c 0%, #06080d 100%);">
  <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
    <div>
      <span class="badge badge-canon" style="margin-bottom: 6px;">CONTAINMENT REGISTRY</span>
      <h2 style="margin: 0; color: #ef4444; font-size: 1.6rem; font-family: Impact, sans-serif;">SORROW ENTITY CONTAINMENT REGISTRY</h2>
      <p style="margin: 4px 0 0; color: #94a3b8; font-size: 0.88rem;">Sorrow Entity Classification Code (SECC) · Work Protocols · Qliphoth Frequency Counters</p>
    </div>
    <div style="display: flex; gap: 8px;">
      <span class="badge badge-source">ZAYIN TO ALEPH</span>
      <span class="badge badge-source">10 CORE DOSSIERS</span>
      <span class="badge badge-source">4 WORK TYPES</span>
    </div>
  </div>
</div>

<section class="wiki-section" id="core-entities-catalog">
  <h2 class="section-title">Primary Containment Dossiers</h2>
  <div class="archive-portal-grid" style="grid-template-columns: repeat(auto-fill, minmax(290px, 1fr)); gap: 16px; margin-top: 1rem;">
    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <div style="display: flex; gap: 12px; align-items: center; margin-bottom: 8px;">
        <img src="../assets/art/entities/se-001.svg" style="width: 52px; height: 52px; border-radius: 4px;" alt="">
        <div>
          <a href="se-001-the-orphaned-bell.html" style="color: #f1df76; font-size: 1.05rem; font-family: Impact, sans-serif; text-decoration: none;">SE-001: THE ORPHANED BELL</a>
          <div style="font-size: 0.72rem; color: #38bdf8;">Risk: <span class="badge" style="background: #042f2e; color: #2dd4bf;">ZAYIN</span> · WHITE Damage</div>
        </div>
      </div>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">Dark crystal bell forged from unfulfilled parental searches. Weeps acoustic sorrow waves that soothe terrified minds when approached with Attachment.</p>
      <a href="se-001-the-orphaned-bell.html" class="action-btn">Examine Dossier &amp; Tale →</a>
    </div>

    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <div style="display: flex; gap: 12px; align-items: center; margin-bottom: 8px;">
        <img src="../assets/art/entities/se-002-profile.svg" style="width: 52px; height: 52px; border-radius: 4px;" alt="">
        <div>
          <a href="se-002-the-grieving-colossus.html" style="color: #f1df76; font-size: 1.05rem; font-family: Impact, sans-serif; text-decoration: none;">SE-002: THE GRIEVING COLOSSUS</a>
          <div style="font-size: 0.72rem; color: #38bdf8;">Risk: <span class="badge" style="background: #082f49; color: #38bdf8;">TETH</span> · RED Damage</div>
        </div>
      </div>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">Bound stone titan bearing the weight of fallen precursor citadels. Crushes containment barriers if repressed with violent force.</p>
      <a href="se-002-the-grieving-colossus.html" class="action-btn">Examine Dossier &amp; Tale →</a>
    </div>

    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <div style="display: flex; gap: 12px; align-items: center; margin-bottom: 8px;">
        <img src="../assets/art/entities/se-003.svg" style="width: 52px; height: 52px; border-radius: 4px;" alt="">
        <div>
          <a href="se-003-the-wilderness-tide.html" style="color: #f1df76; font-size: 1.05rem; font-family: Impact, sans-serif; text-decoration: none;">SE-003: THE WILDERNESS TIDE</a>
          <div style="font-size: 0.72rem; color: #38bdf8;">Risk: <span class="badge" style="background: #2e2004; color: #facc15;">HE</span> · BLACK Damage</div>
        </div>
      </div>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">Subconscious oceanic surge carrying drowned memories. Floods containment chambers with corrosive brine if work order duration exceeds 45s.</p>
      <a href="se-003-the-wilderness-tide.html" class="action-btn">Examine Dossier &amp; Tale →</a>
    </div>

    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <div style="display: flex; gap: 12px; align-items: center; margin-bottom: 8px;">
        <img src="../assets/art/entities/se-005-profile.svg" style="width: 52px; height: 52px; border-radius: 4px;" alt="">
        <div>
          <a href="se-005-the-smothering-mother.html" style="color: #f1df76; font-size: 1.05rem; font-family: Impact, sans-serif; text-decoration: none;">SE-005: THE SMOTHERING MOTHER</a>
          <div style="font-size: 0.72rem; color: #38bdf8;">Risk: <span class="badge" style="background: #2e2004; color: #facc15;">HE</span> · RED/WHITE Damage</div>
        </div>
      </div>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">Veiled maternal wraith holding an empty iron cradle. Traps assigned agents in asphyxiating mourning shrouds upon Bad work results.</p>
      <a href="se-005-the-smothering-mother.html" class="action-btn">Examine Dossier &amp; Tale →</a>
    </div>

    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <div style="display: flex; gap: 12px; align-items: center; margin-bottom: 8px;">
        <img src="../assets/art/entities/se-007.svg" style="width: 52px; height: 52px; border-radius: 4px;" alt="">
        <div>
          <a href="se-007-brume.html" style="color: #f1df76; font-size: 1.05rem; font-family: Impact, sans-serif; text-decoration: none;">SE-007: BRUME</a>
          <div style="font-size: 0.72rem; color: #38bdf8;">Risk: <span class="badge" style="background: #2e0827; color: #e879f9;">WAW</span> · PALE Damage</div>
        </div>
      </div>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">Sentient vaporous serpent drifting through ventilation shafts. Inverts reality perception and erases agent memories upon containment escape.</p>
      <a href="se-007-brume.html" class="action-btn">Examine Dossier &amp; Tale →</a>
    </div>

    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <div style="display: flex; gap: 12px; align-items: center; margin-bottom: 8px;">
        <img src="../assets/art/entities/se-010-profile.svg" style="width: 52px; height: 52px; border-radius: 4px;" alt="">
        <div>
          <a href="se-010-the-convergence.html" style="color: #f1df76; font-size: 1.05rem; font-family: Impact, sans-serif; text-decoration: none;">SE-010: THE CONVERGENCE</a>
          <div style="font-size: 0.72rem; color: #38bdf8;">Risk: <span class="badge" style="background: #3b0707; color: #f87171;">ALEPH</span> · ABSOLUTE PALE</div>
        </div>
      </div>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">Monolithic singularity gate born from the collective despair of 1,778 resets. Generates facility-wide temporal fractures if Qliphoth counter reaches 0.</p>
      <a href="se-010-the-convergence.html" class="action-btn">Examine Dossier &amp; Tale →</a>
    </div>
  </div>
</section>
'''

toc_ent = [
    ("core-entities-catalog", "Primary Containment Dossiers")
]

p_ent = get_base_template("Sorrow Entity Containment Registry", "Sorrow Entities", "entities/index.html", "../", ent_hub_html, toc_ent)
with open(os.path.join(WIKI_DIR, "entities/index.html"), 'w', encoding='utf-8') as f:
    f.write(p_ent)
print("Built Super Hub: entities/index.html")

# ==============================================================================
# 8. M.A.W. HUB (maw/index.html)
# ==============================================================================
maw_hub_html = '''
<div class="wiki-callout" style="border-left: 5px solid #f1df76; background: linear-gradient(135deg, #0d121c 0%, #06080d 100%);">
  <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
    <div>
      <span class="badge badge-canon" style="margin-bottom: 6px;">EQUIPMENT ARMORY</span>
      <h2 style="margin: 0; color: #f1df76; font-size: 1.6rem; font-family: Impact, sans-serif;">M.A.W. SYNTHESIS &amp; EQUIPMENT CODEX</h2>
      <p style="margin: 4px 0 0; color: #94a3b8; font-size: 0.88rem;">Manifestation of Absorbed Wrath · Weapons (MAW-W) · Suits (MAW-S) · Gifts (MAW-G)</p>
    </div>
    <div style="display: flex; gap: 8px;">
      <span class="badge badge-source">27 ARTIFACTS</span>
      <span class="badge badge-source">3 GEAR SLOTS</span>
      <span class="badge badge-source">RESONANCE SYNC</span>
    </div>
  </div>
</div>

<section class="wiki-section" id="maw-triad-system">
  <h2 class="section-title">The M.A.W. Equipment Triad System</h2>
  <p><strong>M.A.W.</strong> (Manifestation of Absorbed Wrath — 흡수된 분노의 발현) equipment is harvested directly from the crystallized emotional cores of subdued Sorrow Entities within Floor 3's extraction furnaces. Each complete set consists of three complementary components:</p>
  
  <div class="table-wrap">
    <table class="wiki-table">
      <thead>
        <tr>
          <th>Slot Category</th>
          <th>Prefix Code</th>
          <th>Operational Function</th>
          <th>Resonance Mechanic</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>M.A.W. Weapon</strong></td>
          <td><code>MAW-W</code></td>
          <td>Offensive weapon channeling focused Han damage (RED, WHITE, BLACK, PALE).</td>
          <td>Clash Power bonus &amp; Damage multiplier on Stagger Break.</td>
        </tr>
        <tr>
          <td><strong>M.A.W. Suit</strong></td>
          <td><code>MAW-S</code></td>
          <td>Defensive protective attire providing resistance coefficients (0.5x to 2.0x).</td>
          <td>Damage reduction &amp; Mental panic resistance threshold.</td>
        </tr>
        <tr>
          <td><strong>M.A.W. Gift</strong></td>
          <td><code>MAW-G</code></td>
          <td>Specialized cosmetic/psychic relic altering agent base attributes permanently.</td>
          <td>Passive skill triggers, stat buffs, and unique aura effects.</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

<section class="wiki-section" id="featured-maw-sets">
  <h2 class="section-title">Featured M.A.W. Armaments</h2>
  <div class="archive-portal-grid" style="grid-template-columns: repeat(auto-fill, minmax(290px, 1fr)); gap: 16px; margin-top: 1rem;">
    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <div style="display: flex; gap: 12px; align-items: center; margin-bottom: 8px;">
        <img src="../assets/art/maw/maw-w-001-01.svg" style="width: 52px; height: 52px; border-radius: 4px;" alt="">
        <div>
          <a href="maw-w-001-01-the-laments-requiem.html" style="color: #f1df76; font-size: 1.05rem; font-family: Impact, sans-serif; text-decoration: none;">LAMENT'S REQUIEM</a>
          <div style="font-size: 0.72rem; color: #38bdf8;">MAW-W · Source: SE-001 · WHITE 5–8</div>
        </div>
      </div>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">Acoustic bell blade that emits a pure chiming resonance on hit, restoring 3 SP to nearby allies on Clash win.</p>
      <a href="maw-w-001-01-the-laments-requiem.html" class="action-btn">View Weapon Specs →</a>
    </div>

    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <div style="display: flex; gap: 12px; align-items: center; margin-bottom: 8px;">
        <img src="../assets/art/maw/maw-s-001-01.svg" style="width: 52px; height: 52px; border-radius: 4px;" alt="">
        <div>
          <a href="maw-s-001-01-the-laments-shroud.html" style="color: #f1df76; font-size: 1.05rem; font-family: Impact, sans-serif; text-decoration: none;">LAMENT'S SHROUD</a>
          <div style="font-size: 0.72rem; color: #38bdf8;">MAW-S · Source: SE-001 · WHITE 0.6x</div>
        </div>
      </div>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">Reinforced heavy trenchcoat woven with bronze chime threads, mitigating cognitive stress from soundwave entities.</p>
      <a href="maw-s-001-01-the-laments-shroud.html" class="action-btn">View Suit Specs →</a>
    </div>

    <div class="archive-portal" style="border: 1px solid #334155; padding: 18px; text-align: left; background: #070d16; border-radius: 4px;">
      <div style="display: flex; gap: 12px; align-items: center; margin-bottom: 8px;">
        <img src="../assets/art/maw/maw-g-001-01.svg" style="width: 52px; height: 52px; border-radius: 4px;" alt="">
        <div>
          <a href="maw-g-001-01-laments-edge.html" style="color: #f1df76; font-size: 1.05rem; font-family: Impact, sans-serif; text-decoration: none;">LAMENT'S EDGE</a>
          <div style="font-size: 0.72rem; color: #38bdf8;">MAW-G · Slot: Ear · Prudence +4</div>
        </div>
      </div>
      <p style="font-size: 0.82rem; color: #cbd5e1; margin: 0 0 10px; line-height: 1.5;">Miniature crystal chime earring vibrating at the frequency of forgotten memories, increasing Insight work success by +5%.</p>
      <a href="maw-g-001-01-laments-edge.html" class="action-btn">View Gift Specs →</a>
    </div>
  </div>
</section>
'''

toc_maw = [
    ("maw-triad-system", "The M.A.W. Equipment Triad System"),
    ("featured-maw-sets", "Featured M.A.W. Armaments")
]

p_maw = get_base_template("M.A.W. Synthesis & Equipment Codex", "M.A.W. Equipment", "maw/index.html", "../", maw_hub_html, toc_maw)
with open(os.path.join(WIKI_DIR, "maw/index.html"), 'w', encoding='utf-8') as f:
    f.write(p_maw)
print("Built Super Hub: maw/index.html")

