import os

def upgrade_all_remaining_svgs():
    wiki_root = "/home/user/01_Somnarak_Wiki"
    icons_dir = os.path.join(wiki_root, "assets/icons")
    entity_art_dir = os.path.join(wiki_root, "assets/art/entities")
    user_icons_dir = "/home/user/icons"

    os.makedirs(entity_art_dir, exist_ok=True)

    # 1. THE 10 CANONICAL SORROW ENTITY ICONS (Detailed Heraldic Seals)
    entity_icons = {
        "se-001": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#180407" stroke="#ef5b55" stroke-width="3.5"/>
  <polygon points="60,10 108,26 108,82 60,110 12,82 12,26" fill="#0b0103" stroke="#f1df76" stroke-width="1.2" stroke-dasharray="6 3"/>
  <!-- Colossal Cracked Basalt Mask -->
  <polygon points="34,28 86,28 80,78 60,94 40,78" fill="#2d060a" stroke="#ef5b55" stroke-width="2.5"/>
  <!-- Silver Weeping Tear Channels -->
  <path d="M 44,48 L 44,74 Q 40,84 46,86 Q 52,84 48,74 L 48,48" fill="#e2e8f0" stroke="#38bdf8" stroke-width="1.2"/>
  <path d="M 76,48 L 76,74 Q 72,84 78,86 Q 84,84 80,74 L 80,48" fill="#e2e8f0" stroke="#38bdf8" stroke-width="1.2"/>
  <!-- Fissure Cracks Bleeding Crimson Han -->
  <line x1="60" y1="28" x2="60" y2="56" stroke="#ef5b55" stroke-width="2"/>
  <line x1="60" y1="56" x2="52" y2="68" stroke="#ef5b55" stroke-width="2"/>
  <circle cx="46" cy="46" r="4" fill="#000000" stroke="#ef5b55" stroke-width="1.5"/>
  <circle cx="74" cy="46" r="4" fill="#000000" stroke="#ef5b55" stroke-width="1.5"/>
  <text x="60" y="104" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">WEEPING COLOSSUS</text>
</svg>''',

        "se-003": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#031526" stroke="#38bdf8" stroke-width="3.5"/>
  <polygon points="60,10 108,26 108,82 60,110 12,82 12,26" fill="#01070e" stroke="#38bdf8" stroke-width="1.2" stroke-dasharray="6 3"/>
  <!-- Spider-Silk Loom & Memory Weave -->
  <circle cx="60" cy="54" r="26" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4 2"/>
  <line x1="34" y1="36" x2="86" y2="72" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="86" y1="36" x2="34" y2="72" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="60" y1="24" x2="60" y2="84" stroke="#ffffff" stroke-width="1.5"/>
  <!-- Sapphire Siphon Needle -->
  <polygon points="60,20 64,52 60,88 56,52" fill="#38bdf8" stroke="#ffffff" stroke-width="1.2"/>
  <circle cx="60" cy="34" r="3" fill="#ffffff"/>
  <text x="60" y="104" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">THREAD OF MEMORY</text>
</svg>''',

        "se-004": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#130421" stroke="#c084fc" stroke-width="3.5"/>
  <polygon points="60,10 108,26 108,82 60,110 12,82 12,26" fill="#08010f" stroke="#c084fc" stroke-width="1.2" stroke-dasharray="6 3"/>
  <!-- Shattered Obsidian Mirror Frame -->
  <polygon points="60,22 88,44 82,78 60,90 38,78 32,44" fill="#2d0a4e" stroke="#c084fc" stroke-width="2.5"/>
  <!-- Fracture Shards Refracting Eye -->
  <line x1="60" y1="22" x2="60" y2="90" stroke="#f8fafc" stroke-width="1.5"/>
  <line x1="32" y1="44" x2="82" y2="78" stroke="#f8fafc" stroke-width="1.5"/>
  <circle cx="60" cy="56" r="8" fill="#ef5b55" stroke="#ffffff" stroke-width="1.5"/>
  <circle cx="60" cy="56" r="3" fill="#000000"/>
  <text x="60" y="104" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">OBSIDIAN MIRROR</text>
</svg>''',

        "se-006": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#1c1402" stroke="#f1df76" stroke-width="3.5"/>
  <polygon points="60,10 108,26 108,82 60,110 12,82 12,26" fill="#0d0901" stroke="#f1df76" stroke-width="1.2" stroke-dasharray="6 3"/>
  <!-- Clockwork Bronze Gear Wheel -->
  <circle cx="60" cy="54" r="24" fill="#451a03" stroke="#f1df76" stroke-width="2.5"/>
  <circle cx="60" cy="54" r="14" fill="#1c1402" stroke="#f1df76" stroke-width="1.5"/>
  <circle cx="60" cy="54" r="6" fill="#ef5b55"/>
  <!-- Gear Teeth -->
  <rect x="57" y="24" width="6" height="6" fill="#f1df76"/>
  <rect x="57" y="78" width="6" height="6" fill="#f1df76"/>
  <rect x="30" y="51" width="6" height="6" fill="#f1df76"/>
  <rect x="84" y="51" width="6" height="6" fill="#f1df76"/>
  <text x="60" y="104" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">CLOCKWORK HEART</text>
</svg>''',

        "se-007": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#1f0608" stroke="#ef5b55" stroke-width="3.5"/>
  <polygon points="60,10 108,26 108,82 60,110 12,82 12,26" fill="#0b0103" stroke="#ef5b55" stroke-width="1.2" stroke-dasharray="6 3"/>
  <!-- Burnt Parchment Scroll & Crimson Quill -->
  <path d="M 36,32 L 84,32 L 80,78 L 32,78 Z" fill="#450a0a" stroke="#ef5b55" stroke-width="2"/>
  <line x1="42" y1="44" x2="74" y2="44" stroke="#f1df76" stroke-width="1.5"/>
  <line x1="42" y1="54" x2="74" y2="54" stroke="#f1df76" stroke-width="1.5"/>
  <line x1="42" y1="64" x2="68" y2="64" stroke="#f1df76" stroke-width="1.5"/>
  <!-- Feather Quill with Glowing Runic Tip -->
  <polygon points="84,20 62,60 58,68 66,64" fill="#f8fafc" stroke="#ef5b55" stroke-width="1.2"/>
  <circle cx="58" cy="68" r="2.5" fill="#f1df76"/>
  <text x="60" y="104" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">ASHEN SCRIBE</text>
</svg>''',

        "se-008": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#031526" stroke="#38bdf8" stroke-width="3.5"/>
  <polygon points="60,10 108,26 108,82 60,110 12,82 12,26" fill="#01070e" stroke="#38bdf8" stroke-width="1.2" stroke-dasharray="6 3"/>
  <!-- Gilded Bone Rocking Cradle -->
  <path d="M 28,50 L 92,50 L 84,72 L 36,72 Z" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2"/>
  <path d="M 24,78 Q 60,90 96,78" fill="none" stroke="#f1df76" stroke-width="2.5"/>
  <line x1="36" y1="72" x2="32" y2="82" stroke="#f1df76" stroke-width="2"/>
  <line x1="84" y1="72" x2="88" y2="82" stroke="#f1df76" stroke-width="2"/>
  <!-- Hanging Mobile Stars -->
  <polygon points="60,26 63,32 70,34 65,39 66,46 60,42 54,46 55,39 50,34 57,32" fill="#ffffff"/>
  <text x="60" y="104" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">FORGOTTEN CRADLE</text>
</svg>''',

        "se-009": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#041b2c" stroke="#38bdf8" stroke-width="3.5"/>
  <polygon points="60,10 108,26 108,82 60,110 12,82 12,26" fill="#020d17" stroke="#38bdf8" stroke-width="1.2" stroke-dasharray="6 3"/>
  <!-- Submerged Brass Bell with Patina -->
  <path d="M 44,28 L 76,28 L 84,70 L 90,76 L 30,76 L 36,70 Z" fill="#0e7490" stroke="#38bdf8" stroke-width="2.2"/>
  <!-- Heavy Clapper -->
  <circle cx="60" cy="82" r="6" fill="#f1df76" stroke="#ffffff" stroke-width="1"/>
  <!-- Submerged Wave Ripples -->
  <path d="M 20,40 Q 60,48 100,40" fill="none" stroke="#38bdf8" stroke-width="1.2" opacity="0.6"/>
  <path d="M 20,60 Q 60,68 100,60" fill="none" stroke="#38bdf8" stroke-width="1.2" opacity="0.6"/>
  <text x="60" y="104" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">DROWNED BELL</text>
</svg>''',

        "se-011": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#1f0608" stroke="#ef5b55" stroke-width="3.5"/>
  <polygon points="60,10 108,26 108,82 60,110 12,82 12,26" fill="#0b0103" stroke="#ef5b55" stroke-width="1.2" stroke-dasharray="6 3"/>
  <!-- Iron Maiden Sarcophagus Frame -->
  <path d="M 42,22 L 78,22 L 86,52 L 80,86 L 40,86 L 34,52 Z" fill="#450a0a" stroke="#ef5b55" stroke-width="2.5"/>
  <!-- Internal Spikes -->
  <polygon points="40,36 50,38 40,40" fill="#f1df76"/>
  <polygon points="40,54 50,56 40,58" fill="#f1df76"/>
  <polygon points="80,36 70,38 80,40" fill="#f1df76"/>
  <polygon points="80,54 70,56 80,58" fill="#f1df76"/>
  <!-- Weeping Faceplate -->
  <circle cx="60" cy="36" r="7" fill="#2d060a" stroke="#ffffff" stroke-width="1"/>
  <text x="60" y="104" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">IRON MAIDEN</text>
</svg>''',

        "se-014": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#130421" stroke="#c084fc" stroke-width="3.5"/>
  <polygon points="60,10 108,26 108,82 60,110 12,82 12,26" fill="#08010f" stroke="#c084fc" stroke-width="1.2" stroke-dasharray="6 3"/>
  <!-- Porcelain Tragedy Mask with Wide Open Singing Mouth -->
  <ellipse cx="60" cy="52" rx="26" ry="32" fill="#f8fafc" stroke="#c084fc" stroke-width="2"/>
  <ellipse cx="48" cy="42" rx="4" ry="6" fill="#000000"/>
  <ellipse cx="72" cy="42" rx="4" ry="6" fill="#000000"/>
  <!-- Open Singing Void Maw -->
  <ellipse cx="60" cy="62" rx="10" ry="14" fill="#3b0764" stroke="#c084fc" stroke-width="2"/>
  <!-- Soundwave Rings -->
  <circle cx="60" cy="62" r="22" fill="none" stroke="#c084fc" stroke-width="1.2" stroke-dasharray="3 3"/>
  <text x="60" y="104" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">HOLLOW SINGER</text>
</svg>''',

        "se-015": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#1c1402" stroke="#f1df76" stroke-width="3.5"/>
  <polygon points="60,10 108,26 108,82 60,110 12,82 12,26" fill="#0d0901" stroke="#f1df76" stroke-width="1.2" stroke-dasharray="6 3"/>
  <!-- Radiant Golden Halo Ring -->
  <circle cx="60" cy="50" r="26" fill="none" stroke="#fef08a" stroke-width="2.5" stroke-dasharray="6 3"/>
  <!-- Jagged Black Iron Crown -->
  <polygon points="34,60 42,32 50,52 60,24 70,52 78,32 86,60 34,60" fill="#0f172a" stroke="#f1df76" stroke-width="2"/>
  <rect x="34" y="60" width="52" height="10" rx="1" fill="#451a03" stroke="#f1df76" stroke-width="1.5"/>
  <!-- Bleeding Thorns & Jewels -->
  <circle cx="48" cy="65" r="2.5" fill="#ef5b55"/>
  <circle cx="60" cy="65" r="3" fill="#fef08a"/>
  <circle cx="72" cy="65" r="2.5" fill="#ef5b55"/>
  <text x="60" y="104" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold" text-anchor="middle">SOVEREIGN CROWN</text>
</svg>'''
    }

    for se_id, svg_code in entity_icons.items():
        # Write to entity_art_dir and icons_dir
        with open(os.path.join(entity_art_dir, f"{se_id}-icon.svg"), "w", encoding="utf-8") as f:
            f.write(svg_code)
        with open(os.path.join(icons_dir, f"{se_id}.svg"), "w", encoding="utf-8") as f:
            f.write(svg_code)
        with open(os.path.join(icons_dir, f"entity_icon_{se_id.replace('-', '_')}.svg"), "w", encoding="utf-8") as f:
            f.write(svg_code)
        with open(os.path.join(user_icons_dir, f"{se_id}.svg"), "w", encoding="utf-8") as f:
            f.write(svg_code)

    # 2. STATS AND LORE ICONS (clarity, warmth, composure, resilience, resolve, spark, flame, veil, etc.)
    stat_icons = {
        "clarity.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#031526" stroke="#38bdf8" stroke-width="3.5"/>
  <polygon points="60,26 84,68 36,68" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="60" cy="54" r="7" fill="#ffffff"/>
  <text x="60" y="104" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">CLARITY // PRISM</text>
</svg>''',

        "warmth.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#1c1402" stroke="#f1df76" stroke-width="3.5"/>
  <circle cx="60" cy="52" r="18" fill="#f59e0b" stroke="#ffffff" stroke-width="1.5"/>
  <polygon points="60,24 64,32 56,32" fill="#f1df76"/>
  <polygon points="60,80 64,72 56,72" fill="#f1df76"/>
  <text x="60" y="104" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">WARMTH // AMBER</text>
</svg>''',

        "composure.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#04140d" stroke="#71efaf" stroke-width="3.5"/>
  <rect x="36" y="34" width="48" height="38" rx="4" fill="#064e3b" stroke="#71efaf" stroke-width="2"/>
  <line x1="42" y1="53" x2="78" y2="53" stroke="#ffffff" stroke-width="2.5"/>
  <text x="60" y="104" fill="#71efaf" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">COMPOSURE // EQUIL</text>
</svg>''',

        "resilience.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#1f0608" stroke="#ef5b55" stroke-width="3.5"/>
  <polygon points="36,28 84,28 78,78 60,88 42,78" fill="#450a0a" stroke="#ef5b55" stroke-width="2.2"/>
  <circle cx="60" cy="54" r="8" fill="#f1df76"/>
  <text x="60" y="104" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">RESILIENCE // WARD</text>
</svg>''',

        "resolve.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#1c1402" stroke="#f1df76" stroke-width="3.5"/>
  <polygon points="60,20 70,44 94,54 70,64 60,88 50,64 26,54 50,44" fill="#fef08a" stroke="#ffffff" stroke-width="1.5"/>
  <text x="60" y="104" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">RESOLVE // WILL</text>
</svg>''',

        "spark.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#1c1402" stroke="#f1df76" stroke-width="3.5"/>
  <circle cx="60" cy="54" r="14" fill="#fef08a"/>
  <line x1="60" y1="24" x2="60" y2="84" stroke="#ffffff" stroke-width="3"/>
  <line x1="30" y1="54" x2="90" y2="54" stroke="#ffffff" stroke-width="3"/>
  <text x="60" y="104" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">SPARK OF HAN</text>
</svg>''',

        "flame.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#1f0608" stroke="#ef5b55" stroke-width="3.5"/>
  <path d="M 60,24 Q 78,50 68,68 Q 60,82 52,68 Q 42,50 60,24 Z" fill="#ef5b55" stroke="#ffffff" stroke-width="1.8"/>
  <circle cx="60" cy="62" r="5" fill="#f1df76"/>
  <text x="60" y="104" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">FLAME // SURGE</text>
</svg>''',

        "veil.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#130421" stroke="#c084fc" stroke-width="3.5"/>
  <ellipse cx="60" cy="54" rx="30" ry="16" fill="#3b0764" stroke="#c084fc" stroke-width="2"/>
  <circle cx="60" cy="54" r="7" fill="#ffffff"/>
  <text x="60" y="104" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">VEIL // OCCULT</text>
</svg>''',

        "pugnahan.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <polygon points="60,4 114,24 114,86 60,116 6,86 6,24" fill="#1f0608" stroke="#ef5b55" stroke-width="3.5"/>
  <polygon points="60,20 84,40 76,78 60,88 44,78 36,40" fill="#450a0a" stroke="#ef5b55" stroke-width="2"/>
  <line x1="30" y1="84" x2="90" y2="24" stroke="#ffffff" stroke-width="3"/>
  <circle cx="60" cy="54" r="6" fill="#f1df76"/>
  <text x="60" y="104" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold" text-anchor="middle">PUGNAHAN // COMBAT</text>
</svg>'''
    }

    for fname, code in stat_icons.items():
        with open(os.path.join(icons_dir, fname), "w", encoding="utf-8") as f:
            f.write(code)
        with open(os.path.join(user_icons_dir, fname), "w", encoding="utf-8") as f:
            f.write(code)

    print("Upgraded all entity and stat icons to rich detailed SVGs!")

if __name__ == "__main__":
    upgrade_all_remaining_svgs()
