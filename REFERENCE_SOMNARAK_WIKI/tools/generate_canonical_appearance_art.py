import os

ENT_DIR = "/home/user/01_Somnarak_Wiki/assets/art/entities"
MAW_DIR = "/home/user/01_Somnarak_Wiki/assets/art/maw"
os.makedirs(ENT_DIR, exist_ok=True)
os.makedirs(MAW_DIR, exist_ok=True)

entity_art = {
    "se-001.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
  <rect width="200" height="200" rx="16" fill="#090d16" stroke="#f1df76" stroke-width="2.5"/>
  <circle cx="100" cy="100" r="85" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="6,4"/>
  <!-- Bell Structure -->
  <path d="M 65 50 Q 100 30 135 50 L 145 130 Q 155 155 160 160 L 40 160 Q 45 155 55 130 Z" fill="#182333" stroke="#f1df76" stroke-width="3"/>
  <ellipse cx="100" cy="160" rx="60" ry="12" fill="#0e1724" stroke="#f1df76" stroke-width="2"/>
  <circle cx="100" cy="160" r="14" fill="#ef5b55" stroke="#f1df76" stroke-width="2"/>
  <!-- Cracks and Crying Face Engraving -->
  <path d="M 100 70 L 95 95 L 108 115 L 100 140" fill="none" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="85" cy="85" r="4" fill="#38bdf8"/>
  <circle cx="115" cy="85" r="4" fill="#38bdf8"/>
  <path d="M 85 89 Q 85 110 82 120" fill="none" stroke="#38bdf8" stroke-width="1.5"/>
  <path d="M 115 89 Q 115 110 118 120" fill="none" stroke="#38bdf8" stroke-width="1.5"/>
  <path d="M 90 105 Q 100 95 110 105" fill="none" stroke="#f1df76" stroke-width="2"/>
</svg>''',

    "se-002.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
  <rect width="200" height="200" rx="16" fill="#0d0a0b" stroke="#ef5b55" stroke-width="2.5"/>
  <!-- Grieving Colossus Torso & Stone Mask -->
  <polygon points="50,40 150,40 170,160 100,180 30,160" fill="#1e1b18" stroke="#f1df76" stroke-width="3"/>
  <!-- Chains -->
  <line x1="20" y1="60" x2="180" y2="60" stroke="#94a3b8" stroke-width="3" stroke-dasharray="8,4"/>
  <line x1="30" y1="120" x2="170" y2="120" stroke="#94a3b8" stroke-width="3" stroke-dasharray="8,4"/>
  <!-- Glowing Sorrow Heart -->
  <circle cx="100" cy="110" r="22" fill="#ef5b55" stroke="#f1df76" stroke-width="3"/>
  <circle cx="100" cy="110" r="10" fill="#f1df76"/>
  <!-- Weeping Eyes on Chest -->
  <polygon points="75,70 90,75 80,85" fill="#38bdf8"/>
  <polygon points="125,70 110,75 120,85" fill="#38bdf8"/>
</svg>''',

    "se-003.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
  <rect width="200" height="200" rx="16" fill="#050e14" stroke="#38bdf8" stroke-width="2.5"/>
  <!-- Wilderness Tide Waves -->
  <path d="M 20 140 Q 60 90 100 130 T 180 120 L 180 180 L 20 180 Z" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2.5"/>
  <path d="M 20 110 Q 70 60 120 100 T 180 80 L 180 180 L 20 180 Z" fill="#075985" opacity="0.6"/>
  <!-- Sunken Lanterns & Reaching Hands -->
  <circle cx="80" cy="110" r="8" fill="#f1df76" stroke="#fff" stroke-width="1.5"/>
  <circle cx="140" cy="90" r="6" fill="#f1df76" stroke="#fff" stroke-width="1.5"/>
  <path d="M 50 130 L 45 105 L 40 110 M 45 105 L 50 108" fill="none" stroke="#f8fafc" stroke-width="2"/>
  <path d="M 120 120 L 125 95 L 130 100 M 125 95 L 120 98" fill="none" stroke="#f8fafc" stroke-width="2"/>
</svg>''',

    "se-005.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
  <rect width="200" height="200" rx="16" fill="#130810" stroke="#ef5b55" stroke-width="2.5"/>
  <!-- Smothering Mother Veil & Cradle -->
  <path d="M 100 30 C 60 30, 40 80, 40 170 L 160 170 C 160 80, 140 30, 100 30 Z" fill="#240c1c" stroke="#f1df76" stroke-width="2.5"/>
  <circle cx="100" cy="65" r="18" fill="#10050d" stroke="#ef5b55" stroke-width="2"/>
  <!-- Shroud Arms holding empty crib -->
  <path d="M 50 120 Q 100 160 150 120" fill="none" stroke="#ef5b55" stroke-width="3"/>
  <polygon points="80,115 120,115 110,140 90,140" fill="#0f172a" stroke="#f1df76" stroke-width="1.5"/>
  <!-- Red crying tears -->
  <circle cx="94" cy="65" r="2.5" fill="#ef5b55"/>
  <circle cx="106" cy="65" r="2.5" fill="#ef5b55"/>
</svg>''',

    "se-007.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
  <rect width="200" height="200" rx="16" fill="#08141e" stroke="#38bdf8" stroke-width="2.5"/>
  <!-- Brume Cyan Mist Serpent -->
  <path d="M 30 150 Q 70 40 120 120 T 170 60" fill="none" stroke="#38bdf8" stroke-width="12" stroke-linecap="round" opacity="0.4"/>
  <path d="M 30 150 Q 70 40 120 120 T 170 60" fill="none" stroke="#e0f2fe" stroke-width="4" stroke-linecap="round"/>
  <!-- Glowing Eye Slits -->
  <line x1="160" y1="56" x2="175" y2="58" stroke="#f1df76" stroke-width="2.5"/>
  <line x1="162" y1="64" x2="177" y2="66" stroke="#f1df76" stroke-width="2.5"/>
  <circle cx="100" cy="100" r="70" fill="none" stroke="#38bdf8" stroke-width="1" stroke-dasharray="4,8"/>
</svg>''',

    "se-009.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
  <rect width="200" height="200" rx="16" fill="#0f0c18" stroke="#f1df76" stroke-width="2.5"/>
  <!-- Memory Weaver Loom & Needles -->
  <line x1="40" y1="40" x2="160" y2="40" stroke="#f1df76" stroke-width="4"/>
  <line x1="40" y1="160" x2="160" y2="160" stroke="#f1df76" stroke-width="4"/>
  <!-- Vertical Warp Threads -->
  <line x1="60" y1="40" x2="60" y2="160" stroke="#38bdf8" stroke-width="1.5"/>
  <line x1="80" y1="40" x2="80" y2="160" stroke="#38bdf8" stroke-width="1.5"/>
  <line x1="100" y1="40" x2="100" y2="160" stroke="#38bdf8" stroke-width="1.5"/>
  <line x1="120" y1="40" x2="120" y2="160" stroke="#38bdf8" stroke-width="1.5"/>
  <line x1="140" y1="40" x2="140" y2="160" stroke="#38bdf8" stroke-width="1.5"/>
  <!-- Golden Shuttle / Needle -->
  <polygon points="100,75 165,100 100,125 35,100" fill="#1e1528" stroke="#f1df76" stroke-width="2.5"/>
  <circle cx="100" cy="100" r="10" fill="#38bdf8" stroke="#f1df76" stroke-width="1.5"/>
</svg>''',

    "se-010.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
  <rect width="200" height="200" rx="16" fill="#040608" stroke="#f1df76" stroke-width="2.5"/>
  <!-- Convergence Singularity Triangular Gate -->
  <polygon points="100,25 175,165 25,165" fill="#090d14" stroke="#f1df76" stroke-width="3"/>
  <polygon points="100,60 150,150 50,150" fill="#030406" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="100" cy="120" r="20" fill="#f8fafc" stroke="#f1df76" stroke-width="3"/>
  <circle cx="100" cy="120" r="8" fill="#040608"/>
  <!-- Energy Rays -->
  <line x1="100" y1="15" x2="100" y2="25" stroke="#f8fafc" stroke-width="2"/>
  <line x1="185" y1="175" x2="175" y2="165" stroke="#f8fafc" stroke-width="2"/>
  <line x1="15" y1="175" x2="25" y2="165" stroke="#f8fafc" stroke-width="2"/>
</svg>''',

    "se-011.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
  <rect width="200" height="200" rx="16" fill="#14110e" stroke="#38bdf8" stroke-width="2.5"/>
  <!-- Whispering Walls Masonry with embedded mouths -->
  <line x1="30" y1="70" x2="170" y2="70" stroke="#78716c" stroke-width="2"/>
  <line x1="30" y1="130" x2="170" y2="130" stroke="#78716c" stroke-width="2"/>
  <!-- Embedded Mouths / Acoustic Conduits -->
  <path d="M 60 50 Q 75 40 90 50 Q 75 60 60 50 Z" fill="#0c0a09" stroke="#ef5b55" stroke-width="1.8"/>
  <path d="M 110 50 Q 125 40 140 50 Q 125 60 110 50 Z" fill="#0c0a09" stroke="#ef5b55" stroke-width="1.8"/>
  <path d="M 85 100 Q 100 85 115 100 Q 100 115 85 100 Z" fill="#0c0a09" stroke="#38bdf8" stroke-width="2.2"/>
  <path d="M 60 150 Q 75 140 90 150 Q 75 160 60 150 Z" fill="#0c0a09" stroke="#ef5b55" stroke-width="1.8"/>
  <path d="M 110 150 Q 125 140 140 150 Q 125 160 110 150 Z" fill="#0c0a09" stroke="#ef5b55" stroke-width="1.8"/>
</svg>''',

    "se-014.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
  <rect width="200" height="200" rx="16" fill="#161205" stroke="#f1df76" stroke-width="2.5"/>
  <!-- Debt Eater Ledger Teeth & Coin Scales -->
  <rect x="40" y="45" width="120" height="110" rx="8" fill="#292008" stroke="#f1df76" stroke-width="3"/>
  <!-- Open Ledger Mouth -->
  <polygon points="55,100 100,70 145,100 100,130" fill="#0b0802" stroke="#ef5b55" stroke-width="2"/>
  <!-- Sharp Coin Teeth -->
  <polygon points="65,95 75,95 70,85" fill="#f1df76"/>
  <polygon points="85,90 95,90 90,80" fill="#f1df76"/>
  <polygon points="105,90 115,90 110,80" fill="#f1df76"/>
  <polygon points="125,95 135,95 130,85" fill="#f1df76"/>
  <circle cx="100" cy="100" r="12" fill="#ef5b55"/>
</svg>''',

    "se-015.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
  <rect width="200" height="200" rx="16" fill="#0a0c10" stroke="#f1df76" stroke-width="2.5"/>
  <!-- Debt Scale Fulcrum & Pans -->
  <line x1="100" y1="30" x2="100" y2="160" stroke="#f1df76" stroke-width="3.5"/>
  <polygon points="80,170 120,170 100,155" fill="#f1df76"/>
  <!-- Beam -->
  <line x1="45" y1="65" x2="155" y2="55" stroke="#f1df76" stroke-width="3"/>
  <!-- Left Pan (Soul) -->
  <line x1="45" y1="65" x2="35" y2="115" stroke="#38bdf8" stroke-width="1.5"/>
  <line x1="45" y1="65" x2="55" y2="115" stroke="#38bdf8" stroke-width="1.5"/>
  <path d="M 25 115 Q 45 130 65 115 Z" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="45" cy="105" r="7" fill="#38bdf8"/>
  <!-- Right Pan (Calcified Debt) -->
  <line x1="155" y1="55" x2="145" y2="105" stroke="#ef5b55" stroke-width="1.5"/>
  <line x1="155" y1="55" x2="165" y2="105" stroke="#ef5b55" stroke-width="1.5"/>
  <path d="M 135 105 Q 155 120 175 105 Z" fill="#0f172a" stroke="#ef5b55" stroke-width="2"/>
  <polygon points="150,100 160,100 155,90" fill="#ef5b55"/>
</svg>'''
}

for fn, code in entity_art.items():
    with open(os.path.join(ENT_DIR, fn), 'w', encoding='utf-8') as f:
        f.write(code)
    print(f"Written Entity Art: {fn}")

print("Canonical Entity appearance art generation complete.")
