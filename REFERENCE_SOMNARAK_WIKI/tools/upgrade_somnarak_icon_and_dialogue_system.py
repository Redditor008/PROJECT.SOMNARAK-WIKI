import os
import re

def upgrade_somnarak_master():
    wiki_root = "/home/user/01_Somnarak_Wiki"
    assets_dir = os.path.join(wiki_root, "assets")
    icons_dir = os.path.join(assets_dir, "icons")
    avatars_dir = os.path.join(assets_dir, "avatars")
    banners_dir = os.path.join(assets_dir, "banners")
    profiles_dir = os.path.join(assets_dir, "profiles")
    entity_art_dir = os.path.join(assets_dir, "art/entities")
    hand_icons_dir = os.path.join(assets_dir, "layout/hand/icons")
    city_icons_dir = os.path.join(assets_dir, "layout/city/icons")
    user_icons_dir = "/home/user/icons"

    # =========================================================================
    # 1. ULTRA-DETAILED MASTER SOMNARAK SEAL (somnarak_icon.svg & brand_logo)
    # =========================================================================
    master_somnarak_seal_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <defs>
    <radialGradient id="sealBg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#1e1302"/>
      <stop offset="45%" stop-color="#0c1726"/>
      <stop offset="85%" stop-color="#040914"/>
      <stop offset="100%" stop-color="#010307"/>
    </radialGradient>
    <linearGradient id="goldEdge" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="35%" stop-color="#f1df76"/>
      <stop offset="70%" stop-color="#ca8a04"/>
      <stop offset="100%" stop-color="#854d0e"/>
    </linearGradient>
    <linearGradient id="cyanEdge" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e0f2fe"/>
      <stop offset="40%" stop-color="#38bdf8"/>
      <stop offset="80%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <radialGradient id="coreGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="30%" stop-color="#f59e0b"/>
      <stop offset="70%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#7f1d1d" stop-opacity="0"/>
    </radialGradient>
    <filter id="sealDropGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3.5" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <!-- Outer Cybernetic Chamfered Octagonal Frame -->
  <polygon points="100,4 170,30 196,100 170,170 100,196 30,170 4,100 30,30" fill="url(#sealBg)" stroke="url(#goldEdge)" stroke-width="4"/>
  <!-- Secondary Cyan Inset Border -->
  <polygon points="100,12 164,36 188,100 164,164 100,188 36,164 12,100 36,36" fill="none" stroke="url(#cyanEdge)" stroke-width="1.8" stroke-dasharray="8 4"/>

  <!-- 8-Spoke Chronometer Wheel (The 8 Floors & 1,778 Cycles) -->
  <circle cx="100" cy="100" r="72" fill="none" stroke="#f1df76" stroke-width="1.2" stroke-dasharray="4 3" opacity="0.6"/>
  <circle cx="100" cy="100" r="62" fill="none" stroke="#38bdf8" stroke-width="1.5"/>
  <line x1="100" y1="28" x2="100" y2="172" stroke="#f1df76" stroke-width="1" stroke-dasharray="2 2" opacity="0.7"/>
  <line x1="28" y1="100" x2="172" y2="100" stroke="#f1df76" stroke-width="1" stroke-dasharray="2 2" opacity="0.7"/>
  <line x1="48" y1="48" x2="152" y2="152" stroke="#38bdf8" stroke-width="0.8" opacity="0.5"/>
  <line x1="48" y1="152" x2="152" y2="48" stroke="#38bdf8" stroke-width="0.8" opacity="0.5"/>

  <!-- Tactical Rim Calibration Pips & Runes -->
  <polygon points="100,16 104,24 96,24" fill="#f1df76"/>
  <polygon points="100,184 104,176 96,176" fill="#f1df76"/>
  <polygon points="16,100 24,96 24,104" fill="#f1df76"/>
  <polygon points="184,100 176,96 176,104" fill="#f1df76"/>

  <!-- 12-Point Radiant Solar Dawn Starburst (Absolvohan Resonance) -->
  <g transform="translate(100, 100)" filter="url(#sealDropGlow)">
    <!-- 4 Cardinal Gold Beams -->
    <polygon points="0,-52 5,-20 0,0 -5,-20" fill="url(#goldEdge)"/>
    <polygon points="0,52 5,20 0,0 -5,20" fill="url(#goldEdge)"/>
    <polygon points="-52,0 -20,5 0,0 -20,-5" fill="url(#goldEdge)"/>
    <polygon points="52,0 20,5 0,0 20,-5" fill="url(#goldEdge)"/>
    <!-- 4 Diagonal Cyan Beams -->
    <polygon points="-36,-36 -12,-20 0,0 -20,-12" fill="url(#cyanEdge)"/>
    <polygon points="36,-36 12,-20 0,0 20,-12" fill="url(#cyanEdge)"/>
    <polygon points="-36,36 -12,20 0,0 -20,12" fill="url(#cyanEdge)"/>
    <polygon points="36,36 12,20 0,0 20,12" fill="url(#cyanEdge)"/>
  </g>

  <!-- The Sovereign Imperial Crown of Absolvohan -->
  <g transform="translate(100, 78)">
    <polygon points="-38,0 -28,-22 -14,-4 0,-30 14,-4 28,-22 38,0" fill="#451a03" stroke="url(#goldEdge)" stroke-width="2.2"/>
    <rect x="-38" y="0" width="76" height="8" rx="1.5" fill="#ca8a04" stroke="#ffffff" stroke-width="1"/>
    <circle cx="-28" cy="-22" r="3" fill="#ef4444" stroke="#ffffff" stroke-width="0.8"/>
    <circle cx="0" cy="-30" r="4.5" fill="#fef08a" stroke="#ffffff" stroke-width="1"/>
    <circle cx="28" cy="-22" r="3" fill="#ef4444" stroke="#ffffff" stroke-width="0.8"/>
    <circle cx="-18" cy="4" r="2" fill="#38bdf8"/>
    <circle cx="0" cy="4" r="2.5" fill="#fef08a"/>
    <circle cx="18" cy="4" r="2" fill="#38bdf8"/>
  </g>

  <!-- Central Crystallized Weeping Han Seed Core -->
  <g transform="translate(100, 114)" filter="url(#sealDropGlow)">
    <!-- Prismatic Energy Core Halo -->
    <circle cx="0" cy="0" r="24" fill="url(#coreGlow)"/>
    <!-- Weeping Tear & Seed of Hope -->
    <path d="M 0,-24 C -18,2 -16,22 0,28 C 16,22 18,2 0,-24 Z" fill="#082f49" stroke="url(#cyanEdge)" stroke-width="2.2"/>
    <!-- Inner Radiant Spark -->
    <circle cx="0" cy="8" r="8" fill="#ffffff" filter="url(#sealDropGlow)"/>
    <polygon points="0,-4 3,6 12,8 3,10 0,20 -3,10 -12,8 -3,6" fill="#fef08a"/>
    <!-- Flowing Droplet Trails -->
    <circle cx="0" cy="38" r="3" fill="#38bdf8"/>
    <circle cx="0" cy="48" r="1.8" fill="#38bdf8"/>
  </g>

  <!-- Canonical Terminal Inscription -->
  <text x="100" y="180" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" letter-spacing="2" text-anchor="middle">SOMNARAK</text>
  <text x="100" y="190" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="6.5" font-weight="bold" letter-spacing="1" text-anchor="middle">CYCLE 1,778 · 恨</text>
</svg>'''

    # Write Master Somnarak Icon to all primary locations
    somnarak_targets = [
        os.path.join(icons_dir, "somnarak_icon.svg"),
        os.path.join(icons_dir, "brand_logo.svg"),
        os.path.join(icons_dir, "icon_reverie_directorate_badge.svg"),
        os.path.join(hand_icons_dir, "icon_reverie_directorate_badge.svg"),
        os.path.join(city_icons_dir, "icon_reverie_directorate_badge.svg"),
        os.path.join(user_icons_dir, "somnarak_icon.svg")
    ]

    for p in somnarak_targets:
        with open(p, "w", encoding="utf-8") as f:
            f.write(master_somnarak_seal_svg)

    print("Created ultra-detailed Master Somnarak Heraldic Seal!")

    # =========================================================================
    # 2. BEAUTIFUL TERMINAL DIALOGUE LOG CARD SYSTEM (No more squished callouts)
    # =========================================================================
    css_path = os.path.join(assets_dir, "css/wiki.css")
    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()

    dialogue_css = '''
/* --- ADVANCED TERMINAL DIALOGUE & TRANSCRIPTION SYSTEM --- */
.dialogue-log-stream {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin: 1.5rem 0;
  width: 100%;
}

.terminal-dialogue-card {
  background: linear-gradient(180deg, #0f1726 0%, #060910 100%);
  border: 1.5px solid #38bdf8;
  border-left: 5px solid #f1df76;
  border-radius: 4px;
  padding: 14px 18px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.5);
  transition: transform 0.15s ease, border-color 0.15s ease;
  box-sizing: border-box;
  width: 100%;
}

.terminal-dialogue-card:hover {
  border-color: #f1df76;
  box-shadow: 0 4px 20px rgba(241, 223, 118, 0.15);
}

.terminal-dialogue-card.card-crimson {
  border-color: #ef5b55;
  border-left: 5px solid #ef5b55;
}

.terminal-dialogue-card.card-gold {
  border-color: #f1df76;
  border-left: 5px solid #f1df76;
}

.terminal-dialogue-card.card-cyan {
  border-color: #38bdf8;
  border-left: 5px solid #38bdf8;
}

.terminal-dialogue-card.card-green {
  border-color: #71efaf;
  border-left: 5px solid #71efaf;
}

.terminal-dialogue-card.card-purple {
  border-color: #c084fc;
  border-left: 5px solid #c084fc;
}

.dialogue-card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  padding-bottom: 8px;
  margin-bottom: 10px;
}

.dialogue-log-tag {
  font-family: 'JetBrains Mono', 'Courier New', monospace;
  font-size: 0.78rem;
  font-weight: bold;
  color: #f1df76;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.dialogue-speaker-badge {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.75rem;
  font-weight: bold;
  padding: 2px 8px;
  border-radius: 3px;
  background: #1e293b;
  color: #e2e8f0;
  border: 1px solid rgba(255, 255, 255, 0.15);
}

.dialogue-card-body {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.dialogue-line {
  font-size: 0.95rem;
  line-height: 1.6;
  color: #f1f5f9;
  font-style: italic;
  margin: 0;
  padding: 4px 0;
}

.dialogue-line p {
  margin: 0;
  padding: 0;
}

/* Enhancements for legacy wiki-callout when consecutive */
.wiki-callout {
  margin: 14px 0 !important;
  padding: 12px 16px !important;
  border-left: 4px solid #38bdf8 !important;
  background: #090e17 !important;
  border-radius: 3px !important;
  line-height: 1.55 !important;
}

.wiki-callout p {
  margin: 0 !important;
  color: #e2e8f0 !important;
  font-style: italic !important;
}

.wiki-quote {
  margin: 18px 0 !important;
  padding: 16px 20px !important;
  background: #0a111e !important;
  border: 1px solid #1e293b !important;
  border-left: 5px solid #f1df76 !important;
  border-radius: 4px !important;
}

.quote-author {
  font-family: 'JetBrains Mono', monospace !important;
  color: #f1df76 !important;
  font-weight: bold !important;
  font-size: 0.85rem !important;
  margin-top: 8px !important;
  text-align: right !important;
}
'''
    if "ADVANCED TERMINAL DIALOGUE" not in css:
        with open(css_path, "a", encoding="utf-8") as f:
            f.write(dialogue_css)
        print("Added Advanced Terminal Dialogue CSS rules!")

    # =========================================================================
    # 3. REFORMAT SQUISHED DIALOGUE SECTIONS ACROSS ALL CHARACTER PAGES
    # =========================================================================
    char_dir = os.path.join(wiki_root, "characters")
    for f in os.listdir(char_dir):
        if f.endswith(".html") and f != "index.html":
            p = os.path.join(char_dir, f)
            with open(p, "r", encoding="utf-8") as fp:
                html = fp.read()

            # Find dialogue section and upgrade squished callout sequences
            # Pattern: <section class="wiki-section" id="selected-dialogue-and-flavor-text">...
            if 'id="selected-dialogue-and-flavor-text"' in html:
                # Replace consecutive callouts under h3 headers with styled dialogue cards
                def replace_dialogue_section(match):
                    section_content = match.group(0)
                    # Convert <h3>Title</h3> followed by multiple <div class="wiki-callout"><p><em>“...”</em></p></div>
                    # into clean .terminal-dialogue-card
                    def card_converter(m_block):
                        h3_text = m_block.group(1).strip()
                        quotes = m_block.group(2)
                        lines = re.findall(r'<div class="wiki-callout"><p><em>(.*?)</em></p></div>', quotes, re.DOTALL)
                        if not lines:
                            return m_block.group(0)
                        
                        body_lines = "".join([f'<div class="dialogue-line"><p>“{l.strip().strip("“”") }”</p></div>' for l in lines])
                        
                        # Determine card color class based on title
                        card_cls = "card-gold"
                        if "Release" in h3_text or "Door" in h3_text:
                            card_cls = "card-cyan"
                        elif "Bell" in h3_text or "Furnace" in h3_text or "Cheongula" in h3_text:
                            card_cls = "card-crimson"

                        card = f'''<div class="terminal-dialogue-card {card_cls}">
  <div class="dialogue-card-header">
    <span class="dialogue-log-tag">{h3_text}</span>
    <span class="dialogue-speaker-badge">RECORDED TRANSCRIPTION</span>
  </div>
  <div class="dialogue-card-body">
    {body_lines}
  </div>
</div>'''
                        return card

                    subbed = re.sub(r'<h3>(.*?)</h3>\s*((?:<div class="wiki-callout">.*?</div>\s*)+)', card_converter, section_content, flags=re.DOTALL)
                    return subbed

                html = re.sub(r'<section class="wiki-section" id="selected-dialogue-and-flavor-text">.*?</section>', replace_dialogue_section, html, flags=re.DOTALL)

                with open(p, "w", encoding="utf-8") as fp:
                    fp.write(html)

    print("Reformatted all character dialogue sections with clean, divided terminal cards!")

if __name__ == "__main__":
    upgrade_somnarak_master()
