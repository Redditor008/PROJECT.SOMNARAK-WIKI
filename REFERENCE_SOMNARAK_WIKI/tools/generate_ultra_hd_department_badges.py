import os

LAYOUT_HAND_DIR = "/home/user/01_Somnarak_Wiki/assets/layout/hand/icons"
ICONS_DIR = "/home/user/01_Somnarak_Wiki/assets/icons"
os.makedirs(LAYOUT_HAND_DIR, exist_ok=True)
os.makedirs(ICONS_DIR, exist_ok=True)

# High-Detail, High-Contrast 100x100 Department Badges
dept_badges = {
    # Floor 1: Neutral Command (Control Team Crimson)
    "icon_dept_f1_neutral.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <defs>
    <radialGradient id="f1glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ef4444" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#450a0a" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="100" height="100" rx="16" fill="#140608" stroke="#ef4444" stroke-width="3"/>
  <circle cx="50" cy="50" r="42" fill="url(#f1glow)"/>
  <!-- Master Control Pylon & Crown -->
  <polygon points="50,16 82,78 18,78" fill="#2d0a0f" stroke="#f1df76" stroke-width="3"/>
  <polygon points="50,30 70,72 30,72" fill="#ef4444" stroke="#fff" stroke-width="1.8"/>
  <circle cx="50" cy="54" r="8" fill="#ffffff" stroke="#f1df76" stroke-width="2"/>
  <circle cx="50" cy="54" r="3.5" fill="#ef4444"/>
  <line x1="50" y1="6" x2="50" y2="16" stroke="#f1df76" stroke-width="3" stroke-linecap="round"/>
</svg>''',

    # Floor 2: Maw's Keep (Information Team Royal Blue)
    "icon_dept_f2_maws_keep.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <defs>
    <radialGradient id="f2glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#0c1a30" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="100" height="100" rx="16" fill="#070c18" stroke="#3b82f6" stroke-width="3"/>
  <circle cx="50" cy="50" r="42" fill="url(#f2glow)"/>
  <!-- Containment Ward Cage & All-Seeing Lens -->
  <rect x="22" y="22" width="56" height="56" rx="10" fill="#0c182e" stroke="#38bdf8" stroke-width="3"/>
  <circle cx="50" cy="50" r="16" fill="#1e3a8a" stroke="#f1df76" stroke-width="2.5"/>
  <circle cx="50" cy="50" r="7" fill="#f1df76"/>
  <!-- Containment Bars -->
  <line x1="36" y1="22" x2="36" y2="78" stroke="#38bdf8" stroke-width="2"/>
  <line x1="64" y1="22" x2="64" y2="78" stroke="#38bdf8" stroke-width="2"/>
</svg>''',

    # Floor 3: Extraction Hall (Training / Siphon Amber Gold)
    "icon_dept_f3_extraction.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <defs>
    <radialGradient id="f3glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#261704" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="100" height="100" rx="16" fill="#140f04" stroke="#f59e0b" stroke-width="3"/>
  <circle cx="50" cy="50" r="42" fill="url(#f3glow)"/>
  <!-- Siphon Forge Crucible & Extracted Diamond -->
  <polygon points="50,16 84,36 50,86 16,36" fill="#291a05" stroke="#f1df76" stroke-width="3"/>
  <polygon points="50,30 72,44 50,74 28,44" fill="#f59e0b" stroke="#fff" stroke-width="1.8"/>
  <circle cx="50" cy="48" r="8" fill="#ef4444" stroke="#f1df76" stroke-width="2"/>
</svg>''',

    # Floor 4: Insight Forge (Safety / Research Emerald Green)
    "icon_dept_f4_insight_forge.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <defs>
    <radialGradient id="f4glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#10b981" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#042318" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="100" height="100" rx="16" fill="#04120a" stroke="#10b981" stroke-width="3"/>
  <circle cx="50" cy="50" r="42" fill="url(#f4glow)"/>
  <!-- Kinetic Flask & Particle Matrix -->
  <circle cx="50" cy="50" r="28" fill="#082816" stroke="#10b981" stroke-width="3"/>
  <circle cx="50" cy="50" r="14" fill="none" stroke="#f1df76" stroke-width="2.5" stroke-dasharray="4,2"/>
  <circle cx="50" cy="50" r="6" fill="#f1df76"/>
  <line x1="50" y1="12" x2="50" y2="22" stroke="#10b981" stroke-width="3" stroke-linecap="round"/>
  <line x1="50" y1="78" x2="50" y2="88" stroke="#10b981" stroke-width="3" stroke-linecap="round"/>
</svg>''',

    # Floor 5: Border Watch (Central / Perimeter Heavy Platinum)
    "icon_dept_f5_border_watch.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <defs>
    <radialGradient id="f5glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#e4e4e7" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#18181b" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="100" height="100" rx="16" fill="#121215" stroke="#e4e4e7" stroke-width="3"/>
  <circle cx="50" cy="50" r="42" fill="url(#f5glow)"/>
  <!-- Bastion Shield & Acoustic Radar Pylon -->
  <polygon points="50,18 80,32 80,68 50,84 20,68 20,32" fill="#242429" stroke="#e4e4e7" stroke-width="3"/>
  <circle cx="50" cy="50" r="12" fill="#38bdf8" stroke="#fff" stroke-width="2"/>
  <line x1="50" y1="26" x2="50" y2="74" stroke="#f1df76" stroke-width="2"/>
</svg>''',

    # Floor 6: Deep Vault (Disciplinary Deep Claret)
    "icon_dept_f6_deep_vault.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <defs>
    <radialGradient id="f6glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#be123c" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#24040a" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="100" height="100" rx="16" fill="#180408" stroke="#be123c" stroke-width="3"/>
  <circle cx="50" cy="50" r="42" fill="url(#f6glow)"/>
  <!-- Subterranean Vault Gate & Sealed Tome -->
  <rect x="22" y="22" width="56" height="56" rx="8" fill="#2d0610" stroke="#f1df76" stroke-width="3"/>
  <circle cx="50" cy="50" r="14" fill="#0f0205" stroke="#be123c" stroke-width="2.5"/>
  <circle cx="50" cy="50" r="5" fill="#f1df76"/>
  <!-- Vault Dial Marks -->
  <line x1="50" y1="28" x2="50" y2="34" stroke="#f1df76" stroke-width="2.5"/>
  <line x1="50" y1="66" x2="50" y2="72" stroke="#f1df76" stroke-width="2.5"/>
  <line x1="28" y1="50" x2="34" y2="50" stroke="#f1df76" stroke-width="2.5"/>
  <line x1="66" y1="50" x2="72" y2="50" stroke="#f1df76" stroke-width="2.5"/>
</svg>''',

    # Floor 7: Shadow Corps (Welfare / Recon Pink)
    "icon_dept_f7_shadow_corps.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <defs>
    <radialGradient id="f7glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#f43f5e" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#2b040e" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="100" height="100" rx="16" fill="#1a040d" stroke="#f43f5e" stroke-width="3"/>
  <circle cx="50" cy="50" r="42" fill="url(#f7glow)"/>
  <!-- Void Diving Helm & Horizon Crescent -->
  <path d="M 24 50 Q 50 20 76 50 Q 50 80 24 50 Z" fill="#2e0618" stroke="#f43f5e" stroke-width="3"/>
  <circle cx="50" cy="50" r="12" fill="#0f0208" stroke="#f1df76" stroke-width="2.5"/>
  <polygon points="50,42 56,54 44,54" fill="#38bdf8"/>
</svg>''',

    # Floor 8: Gate Watch (Extraction / Primordial Gate Pale Gold)
    "icon_dept_f8_gate_watch.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <defs>
    <radialGradient id="f8glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fbbf24" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#241a02" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="100" height="100" rx="16" fill="#141003" stroke="#fbbf24" stroke-width="3"/>
  <circle cx="50" cy="50" r="42" fill="url(#f8glow)"/>
  <!-- The Forbidden Gate Monolith & Singularity Key -->
  <polygon points="50,14 84,82 16,82" fill="#261b03" stroke="#fbbf24" stroke-width="3"/>
  <circle cx="50" cy="58" r="14" fill="#ef4444" stroke="#fff" stroke-width="2.5"/>
  <circle cx="50" cy="58" r="5" fill="#fff"/>
  <line x1="50" y1="4" x2="50" y2="14" stroke="#fbbf24" stroke-width="3" stroke-linecap="round"/>
</svg>''',

    # Facility Cutaway Icon
    "the_hand_dr_icon_styled.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <defs>
    <radialGradient id="handglow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#f1df76" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#000" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="100" height="100" rx="16" fill="#0d0f14" stroke="#f1df76" stroke-width="3"/>
  <circle cx="50" cy="50" r="42" fill="url(#handglow)"/>
  <polygon points="50,16 84,34 84,72 50,88 16,72 16,34" fill="#1e222d" stroke="#f1df76" stroke-width="3"/>
  <circle cx="50" cy="52" r="14" fill="#38bdf8" stroke="#fff" stroke-width="2"/>
  <line x1="50" y1="20" x2="50" y2="84" stroke="#f1df76" stroke-width="2"/>
</svg>''',

    # City Master Blueprint Icon
    "somnarak_city_icon.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
  <defs>
    <radialGradient id="cityglow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#000" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="100" height="100" rx="16" fill="#08101a" stroke="#38bdf8" stroke-width="3"/>
  <circle cx="50" cy="50" r="42" fill="url(#cityglow)"/>
  <circle cx="50" cy="50" r="32" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="6,3"/>
  <polygon points="50,20 74,68 26,68" fill="#132438" stroke="#f1df76" stroke-width="3"/>
  <circle cx="50" cy="52" r="8" fill="#f1df76"/>
</svg>'''
}

for fn, svg_text in dept_badges.items():
    p1 = os.path.join(LAYOUT_HAND_DIR, fn)
    p2 = os.path.join(ICONS_DIR, fn)
    with open(p1, "w", encoding="utf-8") as f:
        f.write(svg_text)
    with open(p2, "w", encoding="utf-8") as f:
        f.write(svg_text)
    print(f"Written Ultra HD Badge: {fn}")

print("All 10 Ultra HD Department Badges Generated Successfully.")
