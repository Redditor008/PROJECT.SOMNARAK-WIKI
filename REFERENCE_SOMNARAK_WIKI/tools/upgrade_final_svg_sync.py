import os
import shutil

def upgrade_final_sync():
    wiki_root = "/home/user/01_Somnarak_Wiki"
    icons_dir = os.path.join(wiki_root, "assets/icons")
    avatars_dir = os.path.join(wiki_root, "assets/avatars")
    hand_icons_dir = os.path.join(wiki_root, "assets/layout/hand/icons")
    city_icons_dir = os.path.join(wiki_root, "assets/layout/city/icons")
    entity_art_dir = os.path.join(wiki_root, "assets/art/entities")
    user_icons_dir = "/home/user/icons"

    final_svgs = {
        "inner.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#04140d" stroke="#71efaf" stroke-width="3.5"/>
  <circle cx="60" cy="54" r="24" fill="#064e3b" stroke="#71efaf" stroke-width="2"/>
  <circle cx="60" cy="54" r="10" fill="#f1df76" stroke="#ffffff" stroke-width="1.5"/>
  <text x="60" y="104" fill="#71efaf" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">INNER // PSYCHE</text>
</svg>''',

        "or_inner.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#04140d" stroke="#71efaf" stroke-width="3.5"/>
  <circle cx="60" cy="54" r="24" fill="#064e3b" stroke="#71efaf" stroke-width="2"/>
  <circle cx="60" cy="54" r="10" fill="#f1df76" stroke="#ffffff" stroke-width="1.5"/>
  <text x="60" y="104" fill="#71efaf" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">INNER ORIGIN</text>
</svg>''',

        "outside.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#130421" stroke="#c084fc" stroke-width="3.5"/>
  <circle cx="60" cy="54" r="24" fill="none" stroke="#c084fc" stroke-width="2" stroke-dasharray="6 3"/>
  <polygon points="60,26 84,68 36,68" fill="#3b0764" stroke="#f1df76" stroke-width="1.8"/>
  <text x="60" y="104" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">OUTSIDE // VOID</text>
</svg>''',

        "or_outside.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#130421" stroke="#c084fc" stroke-width="3.5"/>
  <circle cx="60" cy="54" r="24" fill="none" stroke="#c084fc" stroke-width="2" stroke-dasharray="6 3"/>
  <polygon points="60,26 84,68 36,68" fill="#3b0764" stroke="#f1df76" stroke-width="1.8"/>
  <text x="60" y="104" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">OUTSIDE ORIGIN</text>
</svg>''',

        "or_city.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#1c1402" stroke="#f1df76" stroke-width="3.5"/>
  <rect x="34" y="40" width="22" height="42" fill="#451a03" stroke="#f1df76" stroke-width="1.8"/>
  <rect x="64" y="28" width="24" height="54" fill="#451a03" stroke="#f1df76" stroke-width="1.8"/>
  <text x="60" y="104" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">CITY ORIGIN</text>
</svg>''',

        "origin.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#031526" stroke="#38bdf8" stroke-width="3.5"/>
  <circle cx="60" cy="54" r="24" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="6 3"/>
  <circle cx="60" cy="54" r="10" fill="#f1df76"/>
  <text x="60" y="104" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">ORIGIN CLASSIFICATION</text>
</svg>''',

        "manifestation.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#1f0608" stroke="#ef5b55" stroke-width="3.5"/>
  <polygon points="60,24 88,78 32,78" fill="#450a0a" stroke="#ef5b55" stroke-width="2"/>
  <circle cx="60" cy="56" r="6" fill="#f1df76"/>
  <text x="60" y="104" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">MANIFESTATION</text>
</svg>''',

        "number.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#031526" stroke="#38bdf8" stroke-width="3.5"/>
  <rect x="36" y="32" width="48" height="46" rx="4" fill="#082f49" stroke="#38bdf8" stroke-width="2"/>
  <text x="60" y="62" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="20" font-weight="bold" text-anchor="middle">#SE</text>
  <text x="60" y="104" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">CODE ID</text>
</svg>''',

        "hbox.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#1f0608" stroke="#ef5b55" stroke-width="3.5"/>
  <rect x="32" y="30" width="56" height="50" rx="3" fill="#450a0a" stroke="#ef5b55" stroke-width="2"/>
  <line x1="32" y1="55" x2="88" y2="55" stroke="#f1df76" stroke-width="1.8"/>
  <line x1="60" y1="30" x2="60" y2="80" stroke="#f1df76" stroke-width="1.8"/>
  <text x="60" y="104" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">CONTAINMENT BOX</text>
</svg>''',

        "sorrow_gauge.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#031526" stroke="#38bdf8" stroke-width="3.5"/>
  <path d="M 30,76 A 34 34 0 0 1 90,76" fill="none" stroke="#38bdf8" stroke-width="6" stroke-dasharray="6 3"/>
  <line x1="60" y1="76" x2="74" y2="48" stroke="#ef5b55" stroke-width="3.5" stroke-linecap="round"/>
  <circle cx="60" cy="76" r="6" fill="#ffffff"/>
  <text x="60" y="104" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">SORROW GAUGE</text>
</svg>'''
    }

    for fname, code in final_svgs.items():
        with open(os.path.join(icons_dir, fname), "w", encoding="utf-8") as f:
            f.write(code)
        with open(os.path.join(user_icons_dir, fname), "w", encoding="utf-8") as f:
            f.write(code)

    # Sync navigation icons across all dirs
    nav_files = [f for f in os.listdir(icons_dir) if f.startswith("nav_")]
    target_dirs = [avatars_dir, hand_icons_dir, city_icons_dir]
    for nd in target_dirs:
        for nf in nav_files:
            src = os.path.join(icons_dir, nf)
            dst = os.path.join(nd, nf)
            if os.path.exists(dst):
                shutil.copyfile(src, dst)

    print("Synchronized all navigation and final rich icons across all sub-folders!")

if __name__ == "__main__":
    upgrade_final_sync()
