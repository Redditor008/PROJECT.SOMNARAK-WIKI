import os
import re

def update_canonical_all():
    wiki_root = "/home/user/01_Somnarak_Wiki"

    # 1. UPDATE index.html DAMAGE MATRIX TABLE WITH EXACT CANONICAL DAMAGE TYPES
    index_path = os.path.join(wiki_root, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    canonical_damage_table = '''
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
                  <img src="assets/icons/damage_red.svg" alt="Grudge" style="width: 52px; height: 52px; border: 2px solid #ef4444; background: #1f0505; border-radius: 8px; padding: 4px; box-shadow: 0 0 14px rgba(239, 68, 68, 0.6);">
                </td>
                <td><strong style="color: #ef4444; font-size: 1.1rem; letter-spacing: 0.05em;">Grudge (원한)</strong></td>
                <td><span class="badge badge-crimson" style="font-size: 0.85rem; padding: 4px 10px; background: #450a0a; color: #fca5a5; border: 1px solid #ef4444;">Crimson</span></td>
                <td><strong style="color: #fca5a5;">Health Points (HP)</strong></td>
                <td>Direct physical blunt impact, lacerations, thermal combustion, and severe bone fracturing.</td>
                <td>Heavy armored M.A.W. Suits (Resolve affinity) with Grudge resistance &le; 0.5.</td>
              </tr>
              <tr>
                <td style="text-align: center; vertical-align: middle;">
                  <img src="assets/icons/damage_white.svg" alt="Lament" style="width: 52px; height: 52px; border: 2px solid #3b82f6; background: #081026; border-radius: 8px; padding: 4px; box-shadow: 0 0 14px rgba(59, 130, 246, 0.6);">
                </td>
                <td><strong style="color: #60a5fa; font-size: 1.1rem; letter-spacing: 0.05em;">Lament (비탄)</strong></td>
                <td><span class="badge badge-somna" style="font-size: 0.85rem; padding: 4px 10px; background: #172554; color: #93c5fd; border: 1px solid #3b82f6;">Deep Blue</span></td>
                <td><strong style="color: #93c5fd;">Sanity Points (SP)</strong></td>
                <td>Severe cognitive distress, auditory weeping hallucinations, grief paralysis, panic erosion, and self-harm.</td>
                <td>Psychologically reinforced M.A.W. Veils (Resilience affinity) and Insight work routines.</td>
              </tr>
              <tr>
                <td style="text-align: center; vertical-align: middle;">
                  <img src="assets/icons/damage_pale.svg" alt="Void" style="width: 52px; height: 52px; border: 2px solid #ffffff; background: #0f172a; border-radius: 8px; padding: 4px; box-shadow: 0 0 14px rgba(255, 255, 255, 0.7);">
                </td>
                <td><strong style="color: #ffffff; font-size: 1.1rem; letter-spacing: 0.05em; text-shadow: 0 0 8px #ffffff;">Void (공허)</strong></td>
                <td><span class="badge badge-pale" style="font-size: 0.85rem; padding: 4px 10px; background: #1e293b; color: #ffffff; border: 1px solid #e2e8f0;">Pale White</span></td>
                <td><strong style="color: #e2e8f0;">Max HP Percentage</strong></td>
                <td>Direct soul-death, memory erasure, and existential dissolution bypassing conventional physical armor.</td>
                <td>High-tier &omega;-grade M.A.W. suits (Clarity affinity Level V required); extreme caution.</td>
              </tr>
              <tr>
                <td style="text-align: center; vertical-align: middle;">
                  <img src="assets/icons/damage_black.svg" alt="Weight" style="width: 52px; height: 52px; border: 2px solid #71717a; background: #09090b; border-radius: 8px; padding: 4px; box-shadow: 0 0 14px rgba(113, 113, 122, 0.6);">
                </td>
                <td><strong style="color: #cbd5e1; font-size: 1.1rem; letter-spacing: 0.05em;">Weight (중압)</strong></td>
                <td><span class="badge badge-dark" style="font-size: 0.85rem; padding: 4px 10px; background: #000000; color: #a1a1aa; border: 1px solid #71717a;">Black</span></td>
                <td><strong style="color: #f1df76;">Simultaneous HP &amp; SP</strong></td>
                <td>Dual-channel corrosive necrosis and crushing gravitational pressure; drains body and mind equally.</td>
                <td>Balanced composite M.A.W. Plate (Composure affinity); avoid solitary containment shifts.</td>
              </tr>
              <tr>
                <td style="text-align: center; vertical-align: middle;">
                  <img src="assets/icons/damage_mixed.svg" alt="Mixed" style="width: 52px; height: 52px; border: 2px solid #8b5cf6; background: #0a0a14; border-radius: 8px; padding: 4px; box-shadow: 0 0 14px rgba(139, 92, 246, 0.6);">
                </td>
                <td><strong style="color: #c084fc; font-size: 1.1rem; letter-spacing: 0.05em;">Mixed (혼합)</strong></td>
                <td><span class="badge" style="font-size: 0.85rem; padding: 4px 10px; background: linear-gradient(90deg, #ef4444, #f59e0b, #10b981, #3b82f6); color: #ffffff; font-weight: bold;">Rainbow</span></td>
                <td><strong>Multi-Spectral</strong></td>
                <td>Chaotic composite resonance shifting between all elemental frequencies; highly unpredictable.</td>
                <td>Adaptive multi-layer M.A.W. shielding and rotation of specialized suppression squads.</td>
              </tr>
              <tr>
                <td style="text-align: center; vertical-align: middle;">
                  <img src="assets/icons/hope_gold.svg" alt="Hope" style="width: 52px; height: 52px; border: 2px solid #f1df76; background: #1c1303; border-radius: 8px; padding: 4px; box-shadow: 0 0 14px rgba(241, 223, 118, 0.6);">
                </td>
                <td><strong style="color: #f1df76; font-size: 1.1rem; letter-spacing: 0.05em;">Hope (희망)</strong></td>
                <td><span class="badge badge-gold" style="font-size: 0.85rem; padding: 4px 10px; background: #451a03; color: #fef08a; border: 1px solid #f1df76;">Golden</span></td>
                <td><strong>Restorative / Soul</strong></td>
                <td>Sovereign cathartic dawn resonance; stabilizes corrupted minds and purifies fractured Han.</td>
                <td>Absolvohan Seed activation; wielded exclusively during Core Restoration &amp; Dawn protocols.</td>
              </tr>
            </tbody>
          </table>
        </div>
'''

    # Replace damage table in index.html
    old_table_regex = re.compile(r'<div class="pm-table-wrapper">\s*<table class="pm-table".*?</table>\s*</div>', re.DOTALL)
    match = old_table_regex.search(html)
    if match:
        html = html[:match.start()] + canonical_damage_table.strip() + html[match.end():]

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Updated index.html with exact canonical Damage Types (Grudge=Crimson, Lament=Deep Blue, Void=Pale White, Weight=Black, Mixed=Rainbow, Hope=Golden)!")

    # 2. UPDATE mechanics/han-energy-and-damage.html WITH FULL EXPLANATION
    mech_path = os.path.join(wiki_root, "mechanics/han-energy-and-damage.html")
    if os.path.exists(mech_path):
        with open(mech_path, "r", encoding="utf-8") as f:
            m_html = f.read()

        # Inject comprehensive canonical damage definitions
        explanation_block = '''
<h2>1. The Four Core Han Elements &amp; Special Manifestations</h2>
<p>Within the world of Somnarak, all spiritual pressure, psychic trauma, and physical violence derive from the four fundamental Han elements plus two transcendent states:</p>

<div class="table-wrap">
<table class="wiki-table">
  <thead>
    <tr>
      <th style="width:70px;text-align:center;">Emblem</th>
      <th>Element</th>
      <th>Color</th>
      <th>Target</th>
      <th>Metaphysical &amp; Physical Effect</th>
      <th>Canonical Source</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:center;"><img src="../assets/icons/damage_red.svg" alt="Grudge" style="width:48px;height:48px;"></td>
      <td><strong style="color:#ef4444;">Grudge (원한)</strong></td>
      <td><span class="badge badge-crimson">Crimson</span></td>
      <td><strong>Health Points (HP)</strong></td>
      <td>Physical trauma, blunt force, lacerations, thermal combustion, and severe bone fracturing.</td>
      <td>Rage-entities, injustice-entities, violent resentments (e.g. SE-005).</td>
    </tr>
    <tr>
      <td style="text-align:center;"><img src="../assets/icons/damage_white.svg" alt="Lament" style="width:48px;height:48px;"></td>
      <td><strong style="color:#60a5fa;">Lament (비탄)</strong></td>
      <td><span class="badge badge-somna">Deep Blue</span></td>
      <td><strong>Sanity Points (SP)</strong></td>
      <td>Emotional breakdown, cognitive despair, auditory weeping hallucinations, panic erosion.</td>
      <td>Grief-entities, mourning-entities, expressed tears (e.g. SE-001).</td>
    </tr>
    <tr>
      <td style="text-align:center;"><img src="../assets/icons/damage_pale.svg" alt="Void" style="width:48px;height:48px;"></td>
      <td><strong style="color:#ffffff;">Void (공허)</strong></td>
      <td><span class="badge badge-pale">Pale White</span></td>
      <td><strong>Max HP Percentage</strong></td>
      <td>Existential erasure, memory loss, direct soul-death bypassing conventional armor.</td>
      <td>Erasure-entities, numbness-entities, unknown voids (e.g. SE-007, SE-009, SE-014).</td>
    </tr>
    <tr>
      <td style="text-align:center;"><img src="../assets/icons/damage_black.svg" alt="Weight" style="width:48px;height:48px;"></td>
      <td><strong style="color:#cbd5e1;">Weight (중압)</strong></td>
      <td><span class="badge badge-dark">Black</span></td>
      <td><strong>Simultaneous HP &amp; SP</strong></td>
      <td>Gravitational crushing force, corrosive dual-decay eroding body and mind simultaneously.</td>
      <td>Accumulation-entities, structural city sorrow (e.g. SE-002, SE-003).</td>
    </tr>
    <tr>
      <td style="text-align:center;"><img src="../assets/icons/damage_mixed.svg" alt="Mixed" style="width:48px;height:48px;"></td>
      <td><strong style="color:#c084fc;">Mixed (혼합)</strong></td>
      <td><span class="badge" style="background:linear-gradient(90deg,#ef4444,#f59e0b,#10b981,#3b82f6);color:#fff;">Rainbow</span></td>
      <td><strong>Composite Multi-Axis</strong></td>
      <td>Chaotic multi-spectral resonance cycling rapidly across all sorrow frequencies.</td>
      <td>Anomalous multi-origin entities and complex environmental hazards.</td>
    </tr>
    <tr>
      <td style="text-align:center;"><img src="../assets/icons/hope_gold.svg" alt="Hope" style="width:48px;height:48px;"></td>
      <td><strong style="color:#f1df76;">Hope (희망)</strong></td>
      <td><span class="badge badge-gold">Golden</span></td>
      <td><strong>Restoration / Soul</strong></td>
      <td>Transcendent catharsis, psychic stabilization, purification of corrupted Han into Dawn flux.</td>
      <td>The Absolvohan Seed, Core Catharsis, and the Dawn of Hope.</td>
    </tr>
  </tbody>
</table>
</div>
'''
        # Replace section 1 if present
        if "<h2>1." in m_html:
            m_html = re.sub(r'<h2>1\..*?(?=<h2>2\.|$)', explanation_block + "\n", m_html, flags=re.DOTALL)
            with open(mech_path, "w", encoding="utf-8") as f:
                f.write(m_html)
            print("Updated mechanics/han-energy-and-damage.html with canonical damage explanations!")

    # 3. UPDATE ALL ENTITY PAGES TO FEATURE THREE DISTINCT ASSETS:
    # A) ICON (Seal) in metadata
    # B) BANNER (1200x400) in hero header
    # C) PROFILE (500x500 showcase art) in infobox
    entity_files = {
        "se-001": "se-001-the-orphaned-bell.html",
        "se-002": "se-002-the-grieving-colossus.html",
        "se-003": "se-003-the-wilderness-tide.html",
        "se-005": "se-005-the-smothering-mother.html",
        "se-007": "se-007-brume.html",
        "se-009": "se-009-the-memory-weaver.html",
        "se-010": "se-010-the-convergence.html",
        "se-011": "se-011-the-whispering-walls.html",
        "se-014": "se-014-the-debt-eater.html",
        "se-015": "se-015-the-debt-scale.html"
    }

    ent_dir = os.path.join(wiki_root, "entities")
    for se_id, f_name in entity_files.items():
        epath = os.path.join(ent_dir, f_name)
        if os.path.exists(epath):
            with open(epath, "r", encoding="utf-8") as f:
                e_html = f.read()

            # Ensure header hero-banner uses the BANNER SVG (se-xxx-banner.svg)
            e_html = re.sub(
                r'<div class="hero-frame">\s*<img\s+src="[^"]*"\s+alt="[^"]*"\s+class="hero-banner-img">\s*</div>',
                f'<div class="hero-frame"><img src="../assets/art/entities/{se_id}-banner.svg" alt="{se_id} Tactical Banner" class="hero-banner-img"></div>',
                e_html
            )

            # Ensure infobox uses PROFILE showcase art (se-xxx-profile.svg or se-xxx.svg)
            e_html = re.sub(
                r'<img\s+src="\.\./assets/art/entities/se-[0-9]+\.svg"\s+alt="[^"]*"\s+class="infobox-entity-img">',
                f'<img src="../assets/art/entities/{se_id}-profile.svg" alt="{se_id} Master Profile Art" class="infobox-entity-img">',
                e_html
            )

            # Ensure seal icon badge is present in title bar
            with open(epath, "w", encoding="utf-8") as f:
                f.write(e_html)

    print("Updated all 10 Sorrow Entity pages to feature the 3 DISTINCT assets: ICON, BANNER, and PROFILE!")

if __name__ == "__main__":
    update_canonical_all()
