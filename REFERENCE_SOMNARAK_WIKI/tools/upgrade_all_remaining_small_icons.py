import os

def upgrade_remaining_small_icons():
    wiki_root = "/home/user/01_Somnarak_Wiki"
    icons_dir = os.path.join(wiki_root, "assets/icons")
    user_icons_dir = "/home/user/icons"

    upgrades = {
        "weight.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#090d16" stroke="#94a3b8" stroke-width="3.5"/>
  <polygon points="60,12 106,28 106,82 60,108 14,82 14,28" fill="#020408" stroke="#ef5b55" stroke-width="1.2" stroke-dasharray="6 3"/>
  <circle cx="60" cy="48" r="22" fill="#090d16" stroke="#c084fc" stroke-width="2.5"/>
  <circle cx="60" cy="48" r="14" fill="#000000" stroke="#f1df76" stroke-width="1"/>
  <polygon points="42,28 46,38 38,38" fill="#c084fc"/>
  <polygon points="60,22 65,34 55,34" fill="#f1df76"/>
  <polygon points="78,28 82,38 74,38" fill="#c084fc"/>
  <text x="60" y="104" fill="#cbd5e1" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">WEIGHT // DUAL</text>
</svg>''',

        "mixed.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="rainbowGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="25%" stop-color="#f59e0b"/>
      <stop offset="50%" stop-color="#10b981"/>
      <stop offset="75%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#c084fc"/>
    </linearGradient>
  </defs>
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#090d16" stroke="url(#rainbowGrad2)" stroke-width="3.5"/>
  <polygon points="60,20 88,38 88,70 60,88 32,70 32,38" fill="none" stroke="url(#rainbowGrad2)" stroke-width="3"/>
  <circle cx="60" cy="54" r="7" fill="#ffffff"/>
  <text x="60" y="104" fill="#f8fafc" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">MIXED // RESONANCE</text>
</svg>''',

        "maw.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#1c1402" stroke="#f1df76" stroke-width="3.5"/>
  <polygon points="60,20 90,38 82,80 60,92 38,80 30,38" fill="#451a03" stroke="#f1df76" stroke-width="2"/>
  <line x1="30" y1="84" x2="90" y2="24" stroke="#ffffff" stroke-width="3"/>
  <circle cx="60" cy="54" r="6" fill="#ef5b55"/>
  <text x="60" y="104" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">M.A.W. CORE</text>
</svg>''',

        "light.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#1c1402" stroke="#f1df76" stroke-width="3.5"/>
  <circle cx="60" cy="54" r="16" fill="#fef08a"/>
  <line x1="60" y1="20" x2="60" y2="88" stroke="#ffffff" stroke-width="2.5"/>
  <line x1="26" y1="54" x2="94" y2="54" stroke="#ffffff" stroke-width="2.5"/>
  <text x="60" y="104" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">DAWN LIGHT</text>
</svg>'''
    }

    for fname, code in upgrades.items():
        for d in [icons_dir, user_icons_dir]:
            with open(os.path.join(d, fname), "w", encoding="utf-8") as f:
                f.write(code)

    print("Upgraded remaining small icons!")

if __name__ == "__main__":
    upgrade_remaining_small_icons()
