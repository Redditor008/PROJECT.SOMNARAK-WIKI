import os

maw_svgs = {
    # Weapons
    "maw-w-001-01.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect width="200" height="200" fill="#07090e" rx="8"/>
  <line x1="30" y1="170" x2="150" y2="50" stroke="#64748b" stroke-width="8" stroke-linecap="round"/>
  <!-- Bell Hammer Head -->
  <path d="M120 40 L170 90 L180 80 L130 30 Z" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <path d="M140 20 C160 40 180 60 160 80 Z" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="155" cy="55" r="4" fill="#38bdf8"/>
  <text x="100" y="190" font-family="sans-serif" font-size="10" fill="#38bdf8" font-weight="bold" text-anchor="middle">LAMENT'S REQUIEM</text>
</svg>""",

    "maw-w-002-01.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect width="200" height="200" fill="#07090e" rx="8"/>
  <line x1="40" y1="160" x2="130" y2="70" stroke="#475569" stroke-width="12" stroke-linecap="round"/>
  <!-- Basalt Maul Head -->
  <polygon points="110,40 170,40 180,90 120,90" fill="#1e293b" stroke="#e6c94d" stroke-width="3"/>
  <line x1="145" y1="40" x2="145" y2="90" stroke="#38bdf8" stroke-width="2"/>
  <text x="100" y="190" font-family="sans-serif" font-size="10" fill="#e6c94d" font-weight="bold" text-anchor="middle">MOURNING MAUL</text>
</svg>""",

    "maw-w-005-01.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect width="200" height="200" fill="#07090e" rx="8"/>
  <!-- Twin Stilettos bound with silk -->
  <path d="M50 150 L140 40 L150 50 L60 160 Z" fill="#f8fafc" stroke="#e6c94d" stroke-width="2"/>
  <path d="M80 160 L170 50 L160 40 L70 150 Z" fill="#f8fafc" stroke="#ef5b55" stroke-width="2"/>
  <circle cx="105" cy="95" r="8" fill="#e6c94d"/>
  <text x="100" y="190" font-family="sans-serif" font-size="10" fill="#e6c94d" font-weight="bold" text-anchor="middle">EMBRACE FANG</text>
</svg>""",

    "maw-w-007-01.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect width="200" height="200" fill="#07090e" rx="8"/>
  <line x1="30" y1="170" x2="140" y2="60" stroke="#ca8a04" stroke-width="6"/>
  <!-- Brass Lens Prism Head -->
  <circle cx="150" cy="50" r="22" fill="#1e1b4b" stroke="#a855f7" stroke-width="3"/>
  <circle cx="150" cy="50" r="10" fill="#f8fafc" stroke="#38bdf8" stroke-width="2"/>
  <text x="100" y="190" font-family="sans-serif" font-size="10" fill="#a855f7" font-weight="bold" text-anchor="middle">HOPE LENS</text>
</svg>""",

    "maw-w-009-01.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect width="200" height="200" fill="#07090e" rx="8"/>
  <!-- Needle Rapier -->
  <line x1="40" y1="160" x2="160" y2="40" stroke="#f8fafc" stroke-width="3"/>
  <!-- Needle Eyelet with Crimson Thread -->
  <ellipse cx="160" cy="40" rx="3" ry="8" fill="none" stroke="#ef5b55" stroke-width="2" transform="rotate(45 160 40)"/>
  <circle cx="60" cy="140" r="12" fill="#1e293b" stroke="#ef5b55" stroke-width="2"/>
  <text x="100" y="190" font-family="sans-serif" font-size="10" fill="#ef5b55" font-weight="bold" text-anchor="middle">FORGOTTEN LENS</text>
</svg>""",

    "maw-w-010-01.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect width="200" height="200" fill="#07090e" rx="8"/>
  <line x1="30" y1="170" x2="140" y2="60" stroke="#ca8a04" stroke-width="10" stroke-linecap="round"/>
  <!-- Heavy Golden Balance Head -->
  <polygon points="110,40 180,40 190,80 120,80" fill="#f1df76" stroke="#b45309" stroke-width="3"/>
  <circle cx="150" cy="60" r="6" fill="#ef5b55"/>
  <text x="100" y="190" font-family="sans-serif" font-size="10" fill="#f1df76" font-weight="bold" text-anchor="middle">ABSOLUTE MAUL</text>
</svg>""",

    "maw-w-011-01.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect width="200" height="200" fill="#07090e" rx="8"/>
  <line x1="40" y1="160" x2="130" y2="70" stroke="#64748b" stroke-width="6"/>
  <!-- Tuning Fork Spear Head -->
  <path d="M120 80 L160 40 M140 100 L180 60" stroke="#38bdf8" stroke-width="4" stroke-linecap="round"/>
  <circle cx="130" cy="70" r="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <text x="100" y="190" font-family="sans-serif" font-size="10" fill="#38bdf8" font-weight="bold" text-anchor="middle">LISTENING REQUIEM</text>
</svg>""",

    "maw-w-014-01.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect width="200" height="200" fill="#07090e" rx="8"/>
  <!-- Coin Weighted Cleaver -->
  <polygon points="50,150 130,70 170,80 150,140" fill="#1e293b" stroke="#e6c94d" stroke-width="3"/>
  <circle cx="150" cy="95" r="7" fill="#f1df76"/>
  <text x="100" y="190" font-family="sans-serif" font-size="10" fill="#e6c94d" font-weight="bold" text-anchor="middle">DEBT LENS</text>
</svg>""",

    "maw-w-015-01.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect width="200" height="200" fill="#07090e" rx="8"/>
  <!-- Twin Bladed Balance Spear -->
  <line x1="30" y1="170" x2="170" y2="30" stroke="#ca8a04" stroke-width="5"/>
  <polygon points="150,50 175,25 155,25" fill="#f8fafc" stroke="#e6c94d"/>
  <polygon points="45,155 25,175 45,175" fill="#f8fafc" stroke="#e6c94d"/>
  <text x="100" y="190" font-family="sans-serif" font-size="10" fill="#e6c94d" font-weight="bold" text-anchor="middle">BALANCE LENS</text>
</svg>""",

    # Suits
    "maw-s-001-01.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect width="200" height="200" fill="#07090e" rx="8"/>
  <!-- Hooded Gray Coat with Bell Clasps -->
  <polygon points="100,30 60,60 70,160 130,160 140,60" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="100" cy="80" r="5" fill="#38bdf8"/>
  <circle cx="100" cy="110" r="5" fill="#38bdf8"/>
  <text x="100" y="190" font-family="sans-serif" font-size="10" fill="#38bdf8" font-weight="bold" text-anchor="middle">LAMENT'S SHROUD</text>
</svg>""",

    "maw-s-002-01.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect width="200" height="200" fill="#07090e" rx="8"/>
  <!-- Basalt Plate Armor -->
  <polygon points="100,30 50,70 65,160 135,160 150,70" fill="#0f172a" stroke="#475569" stroke-width="4"/>
  <line x1="100" y1="40" x2="100" y2="150" stroke="#38bdf8" stroke-width="2"/>
  <text x="100" y="190" font-family="sans-serif" font-size="10" fill="#e6c94d" font-weight="bold" text-anchor="middle">MOURNING MANTLE</text>
</svg>""",

    "maw-s-005-01.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect width="200" height="200" fill="#07090e" rx="8"/>
  <!-- Golden Silk Corset -->
  <polygon points="100,40 70,60 80,160 120,160 130,60" fill="#1e293b" stroke="#e6c94d" stroke-width="2"/>
  <path d="M75 80 Q100 100 125 80 M78 120 Q100 140 122 120" stroke="#ef5b55" stroke-width="2" fill="none"/>
  <text x="100" y="190" font-family="sans-serif" font-size="10" fill="#e6c94d" font-weight="bold" text-anchor="middle">EMBRACE PLATE</text>
</svg>""",

    "maw-s-007-01.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect width="200" height="200" fill="#07090e" rx="8"/>
  <!-- Translucent Violet Robe -->
  <polygon points="100,30 50,70 65,160 135,160 150,70" fill="#1e1b4b" stroke="#a855f7" stroke-width="2"/>
  <circle cx="100" cy="90" r="14" fill="#38bdf8" opacity="0.4"/>
  <text x="100" y="190" font-family="sans-serif" font-size="10" fill="#a855f7" font-weight="bold" text-anchor="middle">HOPE VEIL</text>
</svg>""",

    "maw-s-009-01.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect width="200" height="200" fill="#07090e" rx="8"/>
  <!-- Black Scholar's Coat -->
  <polygon points="100,30 60,60 70,160 130,160 140,60" fill="#090d16" stroke="#ef5b55" stroke-width="2"/>
  <line x1="80" y1="80" x2="120" y2="80" stroke="#f1df76" stroke-width="1.5"/>
  <text x="100" y="190" font-family="sans-serif" font-size="10" fill="#ef5b55" font-weight="bold" text-anchor="middle">FORGOTTEN VEIL</text>
</svg>""",

    "maw-s-010-01.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect width="200" height="200" fill="#07090e" rx="8"/>
  <!-- Golden Feathered Plate -->
  <polygon points="100,30 50,70 65,160 135,160 150,70" fill="#1c1917" stroke="#f1df76" stroke-width="3"/>
  <circle cx="100" cy="80" r="10" fill="#ef5b55"/>
  <text x="100" y="190" font-family="sans-serif" font-size="10" fill="#f1df76" font-weight="bold" text-anchor="middle">ABSOLUTE MANTLE</text>
</svg>""",

    "maw-s-011-01.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect width="200" height="200" fill="#07090e" rx="8"/>
  <!-- Plaster Hooded Coat -->
  <polygon points="100,30 60,60 70,160 130,160 140,60" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
  <circle cx="100" cy="90" r="6" fill="#020617"/>
  <text x="100" y="190" font-family="sans-serif" font-size="10" fill="#38bdf8" font-weight="bold" text-anchor="middle">LISTENING SHROUD</text>
</svg>""",

    "maw-s-014-01.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect width="200" height="200" fill="#07090e" rx="8"/>
  <!-- Wool Ledger Trenchcoat -->
  <polygon points="100,30 55,65 65,160 135,160 145,65" fill="#1e293b" stroke="#e6c94d" stroke-width="2"/>
  <rect x="85" y="80" width="30" height="40" fill="#fef08a" stroke="#ca8a04"/>
  <text x="100" y="190" font-family="sans-serif" font-size="10" fill="#e6c94d" font-weight="bold" text-anchor="middle">DEBT VEIL</text>
</svg>""",

    "maw-s-015-01.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect width="200" height="200" fill="#07090e" rx="8"/>
  <!-- Duelist Vest -->
  <polygon points="100,30 65,60 75,155 125,155 135,60" fill="#0f172a" stroke="#e6c94d" stroke-width="2"/>
  <line x1="100" y1="30" x2="100" y2="155" stroke="#f8fafc" stroke-width="1.5"/>
  <text x="100" y="190" font-family="sans-serif" font-size="10" fill="#e6c94d" font-weight="bold" text-anchor="middle">BALANCE VEIL</text>
</svg>""",

    # Gifts
    "maw-g-001-01.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect width="200" height="200" fill="#07090e" rx="8"/>
  <!-- Bell Earring -->
  <circle cx="100" cy="70" r="12" fill="none" stroke="#38bdf8" stroke-width="3"/>
  <path d="M85 130 C85 100 95 90 100 90 C105 90 115 100 115 130 Z" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="100" cy="135" r="3" fill="#38bdf8"/>
  <text x="100" y="190" font-family="sans-serif" font-size="10" fill="#38bdf8" font-weight="bold" text-anchor="middle">LAMENT'S EDGE</text>
</svg>""",

    "maw-g-002-01.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect width="200" height="200" fill="#07090e" rx="8"/>
  <!-- Basalt Shoulder Crest -->
  <polygon points="70,120 100,60 130,120 100,105" fill="#1e293b" stroke="#e6c94d" stroke-width="2"/>
  <circle cx="100" cy="85" r="4" fill="#38bdf8"/>
  <text x="100" y="190" font-family="sans-serif" font-size="10" fill="#e6c94d" font-weight="bold" text-anchor="middle">MOURNING SHELL</text>
</svg>""",

    "maw-g-005-01.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect width="200" height="200" fill="#07090e" rx="8"/>
  <!-- Silk Face Veil -->
  <polygon points="60,80 140,80 100,140" fill="#f8fafc" stroke="#e6c94d" stroke-width="2" opacity="0.8"/>
  <text x="100" y="190" font-family="sans-serif" font-size="10" fill="#e6c94d" font-weight="bold" text-anchor="middle">THE EMBRACE</text>
</svg>""",

    "maw-g-007-01.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect width="200" height="200" fill="#07090e" rx="8"/>
  <!-- Floating Glass Lantern -->
  <polygon points="85,60 115,60 125,130 75,130" fill="#1e1b4b" stroke="#ca8a04" stroke-width="2"/>
  <circle cx="100" cy="95" r="10" fill="#f8fafc" stroke="#a855f7" stroke-width="2"/>
  <text x="100" y="190" font-family="sans-serif" font-size="10" fill="#a855f7" font-weight="bold" text-anchor="middle">HOPE LANTERN</text>
</svg>""",

    "maw-g-009-01.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect width="200" height="200" fill="#07090e" rx="8"/>
  <!-- Book Spine Mask -->
  <polygon points="80,60 120,60 110,130 90,130" fill="#1e293b" stroke="#ef5b55" stroke-width="2"/>
  <line x1="100" y1="60" x2="100" y2="130" stroke="#f1df76" stroke-width="1.5"/>
  <text x="100" y="190" font-family="sans-serif" font-size="10" fill="#ef5b55" font-weight="bold" text-anchor="middle">FORGOTTEN MASK</text>
</svg>""",

    "maw-g-010-01.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect width="200" height="200" fill="#07090e" rx="8"/>
  <!-- Eye Crown Halo -->
  <polygon points="80,90 100,50 120,90 100,80" fill="#f1df76" stroke="#b45309" stroke-width="2"/>
  <circle cx="100" cy="72" r="4" fill="#ef5b55"/>
  <text x="100" y="190" font-family="sans-serif" font-size="10" fill="#f1df76" font-weight="bold" text-anchor="middle">ABSOLUTE VERDICT</text>
</svg>""",

    "maw-g-011-01.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect width="200" height="200" fill="#07090e" rx="8"/>
  <!-- Ear Shaped Stone -->
  <path d="M90 70 Q120 60 120 90 Q120 110 100 130 Z" fill="#334155" stroke="#38bdf8" stroke-width="2"/>
  <text x="100" y="190" font-family="sans-serif" font-size="10" fill="#38bdf8" font-weight="bold" text-anchor="middle">LISTENING STONE</text>
</svg>""",

    "maw-g-014-01.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect width="200" height="200" fill="#07090e" rx="8"/>
  <!-- Coin Chest Medallion -->
  <circle cx="100" cy="95" r="28" fill="#1e293b" stroke="#e6c94d" stroke-width="3"/>
  <circle cx="100" cy="95" r="14" fill="#f1df76" stroke="#b45309" stroke-width="2"/>
  <text x="100" y="190" font-family="sans-serif" font-size="10" fill="#e6c94d" font-weight="bold" text-anchor="middle">DEBT SCALE GIFT</text>
</svg>""",

    "maw-g-015-01.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <rect width="200" height="200" fill="#07090e" rx="8"/>
  <!-- Balance Pendant -->
  <circle cx="100" cy="50" r="10" fill="none" stroke="#e6c94d" stroke-width="2"/>
  <line x1="70" y1="90" x2="130" y2="90" stroke="#e6c94d" stroke-width="3"/>
  <circle cx="75" cy="115" r="6" fill="#38bdf8"/>
  <rect x="120" y="110" width="10" height="10" fill="#475569"/>
  <text x="100" y="190" font-family="sans-serif" font-size="10" fill="#e6c94d" font-weight="bold" text-anchor="middle">BALANCE PENDANT</text>
</svg>"""
}

for fname, svg in maw_svgs.items():
    dest = f"/home/user/01_Somnarak_Wiki/assets/art/maw/{fname}"
    with open(dest, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated rich M.A.W. appearance/tale SVG for {fname}")

print("All 27 M.A.W. Equipment appearance + tale SVGs successfully generated!")
