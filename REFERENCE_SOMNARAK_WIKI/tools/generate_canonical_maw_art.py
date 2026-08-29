import os

MAW_DIR = "/home/user/01_Somnarak_Wiki/assets/art/maw"
os.makedirs(MAW_DIR, exist_ok=True)

maw_art = {
    # 001 (Lament)
    "maw-w-001-01.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
  <rect width="160" height="160" rx="12" fill="#080d16" stroke="#f1df76" stroke-width="2"/>
  <line x1="30" y1="130" x2="130" y2="30" stroke="#38bdf8" stroke-width="5" stroke-linecap="round"/>
  <polygon points="120,20 140,40 120,45" fill="#f1df76"/>
  <circle cx="50" cy="110" r="8" fill="#ef5b55" stroke="#f1df76" stroke-width="1.5"/>
</svg>''',
    "maw-s-001-01.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
  <rect width="160" height="160" rx="12" fill="#080d16" stroke="#38bdf8" stroke-width="2"/>
  <path d="M 45 40 L 115 40 L 130 135 L 30 135 Z" fill="#131c2a" stroke="#38bdf8" stroke-width="2.5"/>
  <path d="M 80 40 L 80 135" stroke="#f1df76" stroke-width="2"/>
  <circle cx="80" cy="65" r="6" fill="#ef5b55"/>
</svg>''',
    "maw-g-001-01.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
  <rect width="160" height="160" rx="12" fill="#080d16" stroke="#ef5b55" stroke-width="2"/>
  <circle cx="80" cy="60" r="14" fill="none" stroke="#f1df76" stroke-width="2"/>
  <path d="M 80 74 L 80 120" stroke="#38bdf8" stroke-width="2.5"/>
  <polygon points="75,120 85,120 80,135" fill="#ef5b55"/>
</svg>''',

    # 002 (Mourning)
    "maw-w-002-01.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
  <rect width="160" height="160" rx="12" fill="#140a0b" stroke="#ef5b55" stroke-width="2"/>
  <line x1="30" y1="130" x2="110" y2="50" stroke="#78716c" stroke-width="5"/>
  <rect x="95" y="30" width="40" height="30" rx="4" fill="#292524" stroke="#f1df76" stroke-width="2.5"/>
</svg>''',
    "maw-s-002-01.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
  <rect width="160" height="160" rx="12" fill="#140a0b" stroke="#f1df76" stroke-width="2"/>
  <polygon points="40,35 120,35 135,125 80,145 25,125" fill="#292524" stroke="#ef5b55" stroke-width="2.5"/>
  <line x1="40" y1="75" x2="120" y2="75" stroke="#f1df76" stroke-width="2"/>
</svg>''',
    "maw-g-002-01.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
  <rect width="160" height="160" rx="12" fill="#140a0b" stroke="#ef5b55" stroke-width="2"/>
  <circle cx="80" cy="80" r="28" fill="#292524" stroke="#f1df76" stroke-width="2.5"/>
  <circle cx="80" cy="80" r="12" fill="#ef5b55"/>
</svg>''',

    # 005 (Embrace)
    "maw-w-005-01.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
  <rect width="160" height="160" rx="12" fill="#140810" stroke="#ef5b55" stroke-width="2"/>
  <path d="M 35 125 Q 75 90 125 35 Q 110 70 80 110 Z" fill="#ef5b55" stroke="#f1df76" stroke-width="2"/>
</svg>''',
    "maw-s-005-01.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
  <rect width="160" height="160" rx="12" fill="#140810" stroke="#f1df76" stroke-width="2"/>
  <path d="M 45 35 L 115 35 L 125 130 L 35 130 Z" fill="#250e1e" stroke="#ef5b55" stroke-width="2.5"/>
  <circle cx="80" cy="80" r="14" fill="#0f172a" stroke="#f1df76" stroke-width="2"/>
</svg>''',
    "maw-g-005-01.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
  <rect width="160" height="160" rx="12" fill="#140810" stroke="#ef5b55" stroke-width="2"/>
  <path d="M 40 70 Q 80 40 120 70" fill="none" stroke="#f1df76" stroke-width="3"/>
  <circle cx="80" cy="95" r="8" fill="#ef5b55"/>
</svg>''',

    # 007 (Brume / Hope)
    "maw-w-007-01.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
  <rect width="160" height="160" rx="12" fill="#08141e" stroke="#38bdf8" stroke-width="2"/>
  <rect x="30" y="70" width="90" height="20" rx="4" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="125" cy="80" r="10" fill="#f1df76"/>
</svg>''',
    "maw-s-007-01.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
  <rect width="160" height="160" rx="12" fill="#08141e" stroke="#f1df76" stroke-width="2"/>
  <path d="M 40 35 L 120 35 L 135 135 L 25 135 Z" fill="#075985" opacity="0.6" stroke="#38bdf8" stroke-width="2"/>
</svg>''',
    "maw-g-007-01.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
  <rect width="160" height="160" rx="12" fill="#08141e" stroke="#38bdf8" stroke-width="2"/>
  <rect x="55" y="45" width="50" height="70" rx="6" fill="#0c4a6e" stroke="#f1df76" stroke-width="2.5"/>
  <circle cx="80" cy="80" r="12" fill="#38bdf8"/>
</svg>''',

    # 009 (Memory)
    "maw-w-009-01.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
  <rect width="160" height="160" rx="12" fill="#0f0c18" stroke="#f1df76" stroke-width="2"/>
  <line x1="25" y1="135" x2="135" y2="25" stroke="#f1df76" stroke-width="3"/>
  <circle cx="45" cy="115" r="12" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
</svg>''',
    "maw-s-009-01.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
  <rect width="160" height="160" rx="12" fill="#0f0c18" stroke="#38bdf8" stroke-width="2"/>
  <path d="M 45 35 L 115 35 L 130 135 L 30 135 Z" fill="#1e1528" stroke="#f1df76" stroke-width="2"/>
</svg>''',
    "maw-g-009-01.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
  <rect width="160" height="160" rx="12" fill="#0f0c18" stroke="#f1df76" stroke-width="2"/>
  <path d="M 50 50 Q 80 40 110 50 L 105 100 Q 80 120 55 100 Z" fill="#f8fafc" stroke="#38bdf8" stroke-width="2"/>
</svg>''',

    # 010 (Convergence)
    "maw-w-010-01.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
  <rect width="160" height="160" rx="12" fill="#040608" stroke="#f1df76" stroke-width="2"/>
  <polygon points="75,20 85,20 95,120 65,120" fill="#f8fafc" stroke="#f1df76" stroke-width="2"/>
  <line x1="60" y1="120" x2="100" y2="120" stroke="#f1df76" stroke-width="4"/>
</svg>''',
    "maw-s-010-01.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
  <rect width="160" height="160" rx="12" fill="#040608" stroke="#38bdf8" stroke-width="2"/>
  <polygon points="40,35 120,35 135,135 25,135" fill="#0b111e" stroke="#f8fafc" stroke-width="2"/>
</svg>''',
    "maw-g-010-01.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
  <rect width="160" height="160" rx="12" fill="#040608" stroke="#f1df76" stroke-width="2"/>
  <polygon points="80,45 110,65 100,105 60,105 50,65" fill="#f1df76" stroke="#f8fafc" stroke-width="2"/>
</svg>''',

    # 011 (Whispering)
    "maw-w-011-01.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
  <rect width="160" height="160" rx="12" fill="#14110e" stroke="#38bdf8" stroke-width="2"/>
  <line x1="80" y1="140" x2="80" y2="30" stroke="#78716c" stroke-width="4"/>
  <path d="M 60 30 Q 80 50 100 30" fill="none" stroke="#38bdf8" stroke-width="3"/>
</svg>''',
    "maw-s-011-01.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
  <rect width="160" height="160" rx="12" fill="#14110e" stroke="#f1df76" stroke-width="2"/>
  <path d="M 45 35 L 115 35 L 125 130 L 35 130 Z" fill="#292524" stroke="#38bdf8" stroke-width="2"/>
</svg>''',
    "maw-g-011-01.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
  <rect width="160" height="160" rx="12" fill="#14110e" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="80" cy="80" r="22" fill="#292524" stroke="#f1df76" stroke-width="2"/>
  <circle cx="80" cy="80" r="8" fill="#38bdf8"/>
</svg>''',

    # 014 (Debt Eater)
    "maw-w-014-01.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
  <rect width="160" height="160" rx="12" fill="#161205" stroke="#f1df76" stroke-width="2"/>
  <polygon points="35,130 65,130 130,40 100,40" fill="#f1df76" stroke="#ef5b55" stroke-width="2"/>
</svg>''',
    "maw-s-014-01.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
  <rect width="160" height="160" rx="12" fill="#161205" stroke="#ef5b55" stroke-width="2"/>
  <path d="M 45 35 L 115 35 L 130 135 L 30 135 Z" fill="#2a1f05" stroke="#f1df76" stroke-width="2.5"/>
</svg>''',
    "maw-g-014-01.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
  <rect width="160" height="160" rx="12" fill="#161205" stroke="#f1df76" stroke-width="2"/>
  <circle cx="80" cy="80" r="24" fill="#f1df76" stroke="#ef5b55" stroke-width="2.5"/>
  <rect x="70" y="70" width="20" height="20" fill="#161205"/>
</svg>''',

    # 015 (Debt Scale)
    "maw-w-015-01.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
  <rect width="160" height="160" rx="12" fill="#0a0c10" stroke="#f1df76" stroke-width="2"/>
  <line x1="25" y1="135" x2="135" y2="25" stroke="#f1df76" stroke-width="3"/>
  <polygon points="125,20 140,35 125,40" fill="#38bdf8"/>
  <polygon points="20,125 35,140 35,120" fill="#ef5b55"/>
</svg>''',
    "maw-s-015-01.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
  <rect width="160" height="160" rx="12" fill="#0a0c10" stroke="#f1df76" stroke-width="2"/>
  <path d="M 45 35 L 80 35 L 80 135 L 30 135 Z" fill="#05070a" stroke="#38bdf8" stroke-width="2"/>
  <path d="M 80 35 L 115 35 L 130 135 L 80 135 Z" fill="#1e293b" stroke="#ef5b55" stroke-width="2"/>
</svg>''',
    "maw-g-015-01.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
  <rect width="160" height="160" rx="12" fill="#0a0c10" stroke="#38bdf8" stroke-width="2"/>
  <line x1="50" y1="65" x2="110" y2="65" stroke="#f1df76" stroke-width="2.5"/>
  <line x1="80" y1="50" x2="80" y2="110" stroke="#f1df76" stroke-width="2.5"/>
  <circle cx="55" cy="90" r="8" fill="#38bdf8"/>
  <circle cx="105" cy="90" r="8" fill="#ef5b55"/>
</svg>'''
}

for fn, code in maw_art.items():
    with open(os.path.join(MAW_DIR, fn), 'w', encoding='utf-8') as f:
        f.write(code)
    print(f"Written MAW Art: {fn}")

print(f"Generated {len(maw_art)} canonical MAW art assets.")
