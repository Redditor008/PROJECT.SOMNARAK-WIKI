import os

# Generate detailed SVGs for SE-001 through SE-015 based on Appearance + Tale
entities_svg = {
    "se-001.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 320" width="100%" height="100%">
  <defs>
    <radialGradient id="bellGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#05070a" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="ironGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#475569"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <rect width="320" height="320" fill="#07090e" rx="12"/>
  <circle cx="160" cy="160" r="140" fill="url(#bellGlow)"/>
  <!-- Gallows Timber Frame -->
  <path d="M60 280 L60 50 L260 50 L260 280" fill="none" stroke="#64748b" stroke-width="14" stroke-linecap="round"/>
  <path d="M60 90 L100 50 M260 90 L220 50" stroke="#475569" stroke-width="8"/>
  <!-- Hanging Chain -->
  <line x1="160" y1="50" x2="160" y2="95" stroke="#94a3b8" stroke-width="5" stroke-dasharray="6,4"/>
  <!-- The Orphaned Iron Bell -->
  <path d="M110 210 C110 140 130 95 160 95 C190 95 210 140 210 210 C225 220 230 235 230 245 L90 245 C90 235 95 220 110 210 Z" fill="url(#ironGrad)" stroke="#38bdf8" stroke-width="3"/>
  <!-- Black Weeping Tears dripping from bell rim -->
  <path d="M120 245 Q120 270 123 275 Q126 270 126 245 M160 245 Q160 285 164 290 Q168 285 168 245 M200 245 Q200 265 203 270 Q206 265 206 245" fill="#38bdf8" stroke="#38bdf8" stroke-width="2"/>
  <!-- Small child clapper silhouette inside -->
  <circle cx="160" cy="225" r="9" fill="#020617" stroke="#38bdf8" stroke-width="1.5"/>
  <path d="M154 234 Q160 248 166 234 Z" fill="#020617"/>
  <!-- Faint Bell Tone Soundwaves -->
  <path d="M75 160 A90 90 0 0 0 90 210 M245 160 A90 90 0 0 1 230 210" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,4" opacity="0.6"/>
  <!-- Archival ID -->
  <text x="160" y="305" font-family="'Impact', 'Arial Narrow Bold', sans-serif" font-size="14" fill="#38bdf8" letter-spacing="3" text-anchor="middle">SE-001 · THE ORPHANED BELL</text>
</svg>""",

    "se-002.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 320" width="100%" height="100%">
  <defs>
    <radialGradient id="colGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#6f7ee8" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#05070a" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="320" height="320" fill="#07090e" rx="12"/>
  <circle cx="160" cy="160" r="140" fill="url(#colGlow)"/>
  <!-- Colossus Sarcophagus on Shoulders -->
  <polygon points="60,95 260,95 240,60 80,60" fill="#1e293b" stroke="#e6c94d" stroke-width="3"/>
  <line x1="160" y1="60" x2="160" y2="95" stroke="#e6c94d" stroke-width="2"/>
  <circle cx="160" cy="77" r="6" fill="#e6c94d"/>
  <!-- Titanic Basalt Body -->
  <path d="M90 100 L230 100 L215 250 L105 250 Z" fill="#0f172a" stroke="#475569" stroke-width="3"/>
  <!-- Stone Head & Hollow Water-Falling Eyes -->
  <polygon points="135,110 185,110 175,150 145,150" fill="#1e293b" stroke="#6f7ee8" stroke-width="2"/>
  <!-- Blue Weeping Waterfalls from Eyes -->
  <path d="M148 135 L148 270 M172 135 L172 270" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
  <path d="M145 270 Q160 285 175 270" fill="none" stroke="#38bdf8" stroke-width="2"/>
  <!-- Basalt Leg Pillars -->
  <rect x="110" y="250" width="35" height="40" fill="#0f172a" stroke="#475569" stroke-width="2"/>
  <rect x="175" y="250" width="35" height="40" fill="#0f172a" stroke="#475569" stroke-width="2"/>
  <text x="160" y="305" font-family="'Impact', 'Arial Narrow Bold', sans-serif" font-size="14" fill="#e6c94d" letter-spacing="3" text-anchor="middle">SE-002 · THE GRIEVING COLOSSUS</text>
</svg>""",

    "se-003.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 320" width="100%" height="100%">
  <rect width="320" height="320" fill="#07090e" rx="12"/>
  <!-- Surging Mineral Ash Tide -->
  <path d="M30 250 Q80 180 130 220 Q190 120 240 180 Q290 80 270 260 L30 260 Z" fill="#1e293b" stroke="#ef5b55" stroke-width="3"/>
  <path d="M40 250 Q110 150 180 200 Q240 100 280 160" fill="none" stroke="#f8fafc" stroke-width="2" stroke-dasharray="6,4"/>
  <!-- Coral Spines protruding from wave crest -->
  <polygon points="240,110 255,140 235,145" fill="#f8fafc" stroke="#ef5b55"/>
  <polygon points="210,140 225,170 205,175" fill="#f8fafc" stroke="#ef5b55"/>
  <polygon points="170,160 185,190 165,195" fill="#f8fafc" stroke="#ef5b55"/>
  <polygon points="120,180 135,210 115,215" fill="#f8fafc" stroke="#ef5b55"/>
  <text x="160" y="305" font-family="'Impact', 'Arial Narrow Bold', sans-serif" font-size="14" fill="#ef5b55" letter-spacing="3" text-anchor="middle">SE-003 · THE WILDERNESS TIDE</text>
</svg>""",

    "se-005.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 320" width="100%" height="100%">
  <rect width="320" height="320" fill="#07090e" rx="12"/>
  <!-- Coiling Silk Swaddling Ribbons -->
  <path d="M40 160 C80 60 240 60 280 160 C240 260 80 260 40 160 Z" fill="none" stroke="#e6c94d" stroke-width="4" stroke-dasharray="12,6"/>
  <path d="M70 160 C100 90 220 90 250 160 C220 230 100 230 70 160 Z" fill="none" stroke="#ef5b55" stroke-width="2"/>
  <!-- Porcelain Mask & Multi-arms -->
  <circle cx="160" cy="140" r="32" fill="#f8fafc" stroke="#e6c94d" stroke-width="3"/>
  <!-- Slanted Sorrowful Eyes on Porcelain Face -->
  <line x1="145" y1="135" x2="155" y2="138" stroke="#090d16" stroke-width="2"/>
  <line x1="175" y1="135" x2="165" y2="138" stroke="#090d16" stroke-width="2"/>
  <circle cx="160" cy="155" r="3" fill="#ef5b55"/>
  <!-- Embracing Arms wrapped in ribbons -->
  <path d="M120 180 Q160 220 200 180" fill="none" stroke="#f8fafc" stroke-width="5" stroke-linecap="round"/>
  <text x="160" y="305" font-family="'Impact', 'Arial Narrow Bold', sans-serif" font-size="14" fill="#e6c94d" letter-spacing="3" text-anchor="middle">SE-005 · THE SMOTHERING MOTHER</text>
</svg>""",

    "se-007.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 320" width="100%" height="100%">
  <rect width="320" height="320" fill="#07090e" rx="12"/>
  <!-- Drifting Violet Brume Mist -->
  <path d="M50 160 Q100 110 160 140 Q220 100 270 160 Q230 220 160 190 Q90 230 50 160 Z" fill="#181329" stroke="#a855f7" stroke-width="3" opacity="0.8"/>
  <!-- Drifting Ghostly Lantern Eyes -->
  <circle cx="110" cy="150" r="10" fill="#f8fafc" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="110" cy="150" r="4" fill="#38bdf8"/>
  <circle cx="210" cy="140" r="12" fill="#f8fafc" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="210" cy="140" r="5" fill="#38bdf8"/>
  <circle cx="160" cy="175" r="8" fill="#f8fafc" stroke="#a855f7" stroke-width="1.5"/>
  <circle cx="160" cy="175" r="3" fill="#a855f7"/>
  <text x="160" y="305" font-family="'Impact', 'Arial Narrow Bold', sans-serif" font-size="14" fill="#a855f7" letter-spacing="3" text-anchor="middle">SE-007 · BRUME</text>
</svg>""",

    "se-009.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 320" width="100%" height="100%">
  <rect width="320" height="320" fill="#07090e" rx="12"/>
  <!-- Open Tome of Memories -->
  <polygon points="160,200 90,170 90,100 160,120" fill="#1e293b" stroke="#ef5b55" stroke-width="2"/>
  <polygon points="160,200 230,170 230,100 160,120" fill="#1e293b" stroke="#ef5b55" stroke-width="2"/>
  <!-- Silver Weaver Needles -->
  <line x1="80" y1="70" x2="160" y2="150" stroke="#f8fafc" stroke-width="3"/>
  <line x1="240" y1="70" x2="160" y2="150" stroke="#f8fafc" stroke-width="3"/>
  <line x1="160" y1="40" x2="160" y2="150" stroke="#f8fafc" stroke-width="3"/>
  <line x1="110" y1="50" x2="160" y2="150" stroke="#ef5b55" stroke-width="2"/>
  <line x1="210" y1="50" x2="160" y2="150" stroke="#ef5b55" stroke-width="2"/>
  <!-- Radiant Thread Spindle -->
  <circle cx="160" cy="150" r="14" fill="#ef5b55" stroke="#f1df76" stroke-width="2"/>
  <text x="160" y="305" font-family="'Impact', 'Arial Narrow Bold', sans-serif" font-size="14" fill="#ef5b55" letter-spacing="3" text-anchor="middle">SE-009 · THE MEMORY WEAVER</text>
</svg>""",

    "se-010.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 320" width="100%" height="100%">
  <rect width="320" height="320" fill="#07090e" rx="12"/>
  <!-- Crown of the All-Seeing Eye -->
  <polygon points="120,80 160,40 200,80 180,95 140,95" fill="#f1df76" stroke="#b45309" stroke-width="2"/>
  <circle cx="160" cy="70" r="7" fill="#ef5b55"/>
  <!-- Giant Feathered Scale Wings -->
  <polygon points="50,140 120,110 100,190" fill="#1e293b" stroke="#f1df76" stroke-width="2"/>
  <polygon points="270,140 200,110 220,190" fill="#1e293b" stroke="#f1df76" stroke-width="2"/>
  <!-- Execution Chains & Beaked Gullet -->
  <path d="M130 140 Q160 210 190 140 Z" fill="#0f172a" stroke="#ef5b55" stroke-width="3"/>
  <line x1="80" y1="190" x2="240" y2="190" stroke="#94a3b8" stroke-width="4" stroke-dasharray="6,4"/>
  <text x="160" y="305" font-family="'Impact', 'Arial Narrow Bold', sans-serif" font-size="14" fill="#f1df76" letter-spacing="3" text-anchor="middle">SE-010 · THE CONVERGENCE</text>
</svg>""",

    "se-011.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 320" width="100%" height="100%">
  <rect width="320" height="320" fill="#07090e" rx="12"/>
  <!-- Crumbling Brick Wall Structure -->
  <rect x="70" y="60" width="180" height="190" fill="#1e293b" stroke="#475569" stroke-width="3"/>
  <line x1="70" y1="120" x2="250" y2="120" stroke="#334155" stroke-width="2"/>
  <line x1="70" y1="180" x2="250" y2="180" stroke="#334155" stroke-width="2"/>
  <line x1="160" y1="60" x2="160" y2="120" stroke="#334155" stroke-width="2"/>
  <line x1="120" y1="120" x2="120" y2="180" stroke="#334155" stroke-width="2"/>
  <line x1="200" y1="120" x2="200" y2="180" stroke="#334155" stroke-width="2"/>
  <!-- Whispering Open Mouths inside Brickwork -->
  <ellipse cx="115" cy="90" rx="12" ry="6" fill="#020617" stroke="#38bdf8" stroke-width="1.5"/>
  <ellipse cx="205" cy="90" rx="12" ry="6" fill="#020617" stroke="#38bdf8" stroke-width="1.5"/>
  <ellipse cx="160" cy="150" rx="16" ry="8" fill="#020617" stroke="#38bdf8" stroke-width="1.5"/>
  <ellipse cx="115" cy="210" rx="12" ry="6" fill="#020617" stroke="#38bdf8" stroke-width="1.5"/>
  <ellipse cx="205" cy="210" rx="12" ry="6" fill="#020617" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="160" y="305" font-family="'Impact', 'Arial Narrow Bold', sans-serif" font-size="14" fill="#38bdf8" letter-spacing="3" text-anchor="middle">SE-011 · THE WHISPERING WALLS</text>
</svg>""",

    "se-014.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 320" width="100%" height="100%">
  <rect width="320" height="320" fill="#07090e" rx="12"/>
  <!-- Judge Collar & Beastly Gullet -->
  <polygon points="110,60 210,60 230,120 90,120" fill="#f8fafc" stroke="#475569" stroke-width="2"/>
  <!-- Massive Coin-Toothed Maw -->
  <path d="M80 130 Q160 240 240 130 Z" fill="#0f172a" stroke="#e6c94d" stroke-width="3"/>
  <!-- Golden Coin Teeth -->
  <circle cx="110" cy="145" r="7" fill="#e6c94d"/>
  <circle cx="135" cy="155" r="7" fill="#e6c94d"/>
  <circle cx="160" cy="160" r="7" fill="#e6c94d"/>
  <circle cx="185" cy="155" r="7" fill="#e6c94d"/>
  <circle cx="210" cy="145" r="7" fill="#e6c94d"/>
  <!-- Consumed Debt Ledger Scroll in gullet -->
  <rect x="135" y="180" width="50" height="40" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5" transform="rotate(15 160 200)"/>
  <text x="160" y="305" font-family="'Impact', 'Arial Narrow Bold', sans-serif" font-size="14" fill="#e6c94d" letter-spacing="3" text-anchor="middle">SE-014 · THE DEBT EATER</text>
</svg>""",

    "se-015.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 320" width="100%" height="100%">
  <rect width="320" height="320" fill="#07090e" rx="12"/>
  <!-- Balanced Scale Beam -->
  <polygon points="160,40 155,220 165,220" fill="#e6c94d"/>
  <line x1="70" y1="90" x2="250" y2="90" stroke="#e6c94d" stroke-width="6" stroke-linecap="round"/>
  <circle cx="160" cy="90" r="10" fill="#f1df76" stroke="#b45309" stroke-width="2"/>
  <!-- Left Pan: Glowing Tear / Heart of Han -->
  <line x1="70" y1="90" x2="55" y2="160" stroke="#94a3b8" stroke-width="2"/>
  <line x1="70" y1="90" x2="85" y2="160" stroke="#94a3b8" stroke-width="2"/>
  <path d="M45 160 Q70 180 95 160 Z" fill="#1e293b" stroke="#e6c94d" stroke-width="2"/>
  <circle cx="70" cy="150" r="8" fill="#38bdf8"/>
  <!-- Right Pan: Heavy Iron Debt Ingot (Tilted Down) -->
  <line x1="250" y1="90" x2="235" y2="180" stroke="#94a3b8" stroke-width="2"/>
  <line x1="250" y1="90" x2="265" y2="180" stroke="#94a3b8" stroke-width="2"/>
  <path d="M225 180 Q250 200 275 180 Z" fill="#1e293b" stroke="#e6c94d" stroke-width="2"/>
  <rect x="238" y="165" width="24" height="14" fill="#475569" stroke="#0f172a"/>
  <text x="160" y="305" font-family="'Impact', 'Arial Narrow Bold', sans-serif" font-size="14" fill="#e6c94d" letter-spacing="3" text-anchor="middle">SE-015 · THE DEBT SCALE</text>
</svg>"""
}

for fname, svg in entities_svg.items():
    dest = f"/home/user/01_Somnarak_Wiki/assets/art/entities/{fname}"
    with open(dest, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated rich appearance/tale SVG for {fname}")

print("All 10 Sorrow Entity appearance + tale SVGs successfully generated!")
