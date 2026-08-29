import os

# Complete Synchronized Suite: 13 Entities (120x120 Icon & 500x500 Profile with IDENTICAL Signature Silhouettes)

ENTITIES_SUITE = {}

# -------------------------------------------------------------
# SE-001: The Orphaned Bell (Arched Cathedral Bell Tower)
# -------------------------------------------------------------
ENTITIES_SUITE['se-001'] = {
    'icon': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="se1-glow-sm" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#020617" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="se1-bronze-sm" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="50%" stop-color="#b45309"/>
      <stop offset="100%" stop-color="#78350f"/>
    </linearGradient>
  </defs>
  <path d="M 20,114 L 20,45 Q 60,4 100,45 L 100,114 Z" fill="#040d1a" stroke="#38bdf8" stroke-width="3"/>
  <path d="M 26,108 L 26,48 Q 60,12 94,48 L 94,108 Z" fill="#0b1329" stroke="#f1df76" stroke-width="1.5"/>
  <circle cx="60" cy="65" r="38" fill="url(#se1-glow-sm)"/>
  <path d="M 32,65 A 28,28 0 0,1 88,65" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.7"/>
  <path d="M 24,65 A 36,36 0 0,1 96,65" fill="none" stroke="#38bdf8" stroke-width="1" stroke-dasharray="2,4" opacity="0.4"/>
  <rect x="57" y="16" width="6" height="10" rx="3" fill="none" stroke="#94a3b8" stroke-width="2"/>
  <rect x="57" y="24" width="6" height="10" rx="3" fill="none" stroke="#f1df76" stroke-width="2"/>
  <path d="M 60,32 C 46,32 42,54 38,72 C 36,82 32,86 30,88 L 90,88 C 88,86 84,82 82,72 C 78,54 74,32 60,32 Z" fill="url(#se1-bronze-sm)" stroke="#f1df76" stroke-width="2"/>
  <ellipse cx="60" cy="88" rx="30" ry="5.5" fill="#78350f" stroke="#f1df76" stroke-width="2"/>
  <path d="M 60,90 C 57,94 55,100 57,104 C 59,108 61,108 63,104 C 65,100 63,94 60,90 Z" fill="#38bdf8"/>
  <path d="M 44,89 C 42,92 41,96 42,99 C 43,102 45,102 46,99 C 47,96 46,92 44,89 Z" fill="#38bdf8" opacity="0.85"/>
  <path d="M 76,89 C 74,92 73,96 74,99 C 75,102 77,102 78,99 C 79,96 78,92 76,89 Z" fill="#38bdf8" opacity="0.85"/>
  <circle cx="60" cy="90" r="4.5" fill="#f1df76" stroke="#b45309" stroke-width="1.5"/>
</svg>""",

    'profile': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <radialGradient id="se1-glow-lg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.7"/>
      <stop offset="60%" stop-color="#0369a1" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#020617" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="se1-bronze-lg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fbbf24"/>
      <stop offset="40%" stop-color="#d97706"/>
      <stop offset="80%" stop-color="#92400e"/>
      <stop offset="100%" stop-color="#451a03"/>
    </linearGradient>
  </defs>
  <rect width="500" height="500" fill="#020617"/>
  <path d="M 70,480 L 70,180 Q 250,15 430,180 L 430,480 Z" fill="#040e21" stroke="#38bdf8" stroke-width="6"/>
  <path d="M 90,460 L 90,195 Q 250,45 410,195 L 410,460 Z" fill="#091733" stroke="#f1df76" stroke-width="3"/>
  <circle cx="250" cy="270" r="170" fill="url(#se1-glow-lg)"/>
  <path d="M 130,270 A 120,120 0 0,1 370,270" fill="none" stroke="#38bdf8" stroke-width="3" stroke-dasharray="8,6" opacity="0.8"/>
  <path d="M 100,270 A 150,150 0 0,1 400,270" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="6,8" opacity="0.5"/>
  <rect x="236" y="60" width="28" height="45" rx="12" fill="none" stroke="#94a3b8" stroke-width="6"/>
  <rect x="236" y="95" width="28" height="45" rx="12" fill="none" stroke="#f1df76" stroke-width="6"/>
  <rect x="236" y="130" width="28" height="45" rx="12" fill="none" stroke="#d97706" stroke-width="6"/>
  <path d="M 250,140 C 190,140 170,230 155,300 C 145,345 130,360 120,370 L 380,370 C 370,360 355,345 345,300 C 330,230 310,140 250,140 Z" fill="url(#se1-bronze-lg)" stroke="#f1df76" stroke-width="5"/>
  <path d="M 165,280 Q 250,305 335,280" fill="none" stroke="#fef08a" stroke-width="3.5"/>
  <ellipse cx="250" cy="370" rx="130" ry="24" fill="#78350f" stroke="#f1df76" stroke-width="5"/>
  <line x1="250" y1="300" x2="250" y2="380" stroke="#f1df76" stroke-width="8"/>
  <circle cx="250" cy="380" r="22" fill="#f59e0b" stroke="#78350f" stroke-width="4"/>
  <path d="M 250,390 C 235,410 230,440 238,455 C 245,470 255,470 262,455 C 270,440 265,410 250,390 Z" fill="#38bdf8"/>
  <path d="M 180,380 C 172,395 168,418 174,430 C 178,440 186,440 190,430 C 196,418 190,395 180,380 Z" fill="#38bdf8" opacity="0.9"/>
  <path d="M 320,380 C 312,395 308,418 314,430 C 318,440 326,440 330,430 C 336,418 330,395 320,380 Z" fill="#38bdf8" opacity="0.9"/>
</svg>"""
}

# -------------------------------------------------------------
# SE-002: The Grieving Colossus (Basalt Monolith Hex-Shield)
# -------------------------------------------------------------
ENTITIES_SUITE['se-002'] = {
    'icon': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="se2-basalt-sm" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#334155"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <radialGradient id="se2-crimson-sm" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ef4444" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#450a0a" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <polygon points="60,6 110,24 114,94 60,114 6,94 10,24" fill="#140608" stroke="#ef5b55" stroke-width="3"/>
  <polygon points="60,12 104,28 108,90 60,108 12,90 16,28" fill="url(#se2-basalt-sm)" stroke="#7f1d1d" stroke-width="1.5"/>
  <circle cx="60" cy="58" r="40" fill="url(#se2-crimson-sm)"/>
  <polygon points="20,40 38,24 50,34 32,54" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
  <polygon points="100,40 82,24 70,34 88,54" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
  <path d="M 40,32 L 80,32 L 76,82 L 60,94 L 44,82 Z" fill="#0f172a" stroke="#ef5b55" stroke-width="2.5"/>
  <path d="M 60,32 L 58,48 L 64,56 L 56,72 L 60,94" fill="none" stroke="#ef4444" stroke-width="2"/>
  <line x1="46" y1="46" x2="54" y2="46" stroke="#fca5a5" stroke-width="3" stroke-linecap="round"/>
  <line x1="66" y1="46" x2="74" y2="46" stroke="#fca5a5" stroke-width="3" stroke-linecap="round"/>
  <path d="M 50,49 L 48,78 L 46,92" fill="none" stroke="#ef4444" stroke-width="2.5"/>
  <path d="M 70,49 L 72,78 L 74,92" fill="none" stroke="#ef4444" stroke-width="2.5"/>
</svg>""",

    'profile': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <linearGradient id="se2-basalt-lg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#475569"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#090d16"/>
    </linearGradient>
    <radialGradient id="se2-crimson-lg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ef4444" stop-opacity="0.9"/>
      <stop offset="50%" stop-color="#991b1b" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="500" height="500" fill="#0b0305"/>
  <polygon points="250,20 460,95 475,395 250,480 25,395 40,95" fill="#1c060a" stroke="#ef5b55" stroke-width="6"/>
  <polygon points="250,45 435,115 450,375 250,450 50,375 65,115" fill="url(#se2-basalt-lg)" stroke="#7f1d1d" stroke-width="3"/>
  <circle cx="250" cy="240" r="160" fill="url(#se2-crimson-lg)"/>
  <polygon points="80,165 155,100 205,140 130,225" fill="#1e293b" stroke="#64748b" stroke-width="4"/>
  <polygon points="420,165 345,100 295,140 370,225" fill="#1e293b" stroke="#64748b" stroke-width="4"/>
  <path d="M 165,130 L 335,130 L 315,345 L 250,395 L 185,345 Z" fill="#0f172a" stroke="#ef5b55" stroke-width="6"/>
  <path d="M 250,130 L 240,195 L 268,230 L 235,295 L 250,395" fill="none" stroke="#ef4444" stroke-width="5"/>
  <line x1="190" y1="185" x2="225" y2="185" stroke="#fca5a5" stroke-width="8" stroke-linecap="round"/>
  <line x1="275" y1="185" x2="310" y2="185" stroke="#fca5a5" stroke-width="8" stroke-linecap="round"/>
  <path d="M 205,195 L 200,320 L 190,385" fill="none" stroke="#ef4444" stroke-width="7" stroke-linecap="round"/>
  <path d="M 295,195 L 300,320 L 310,385" fill="none" stroke="#ef4444" stroke-width="7" stroke-linecap="round"/>
</svg>"""
}

# -------------------------------------------------------------
# SE-003: The Thread of Memory (Radiant Diamond Spindle Lozenge)
# -------------------------------------------------------------
ENTITIES_SUITE['se-003'] = {
    'icon': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="se3-azure-sm" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="50%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
  </defs>
  <polygon points="60,6 114,60 60,114 6,60" fill="#051329" stroke="#38bdf8" stroke-width="3"/>
  <polygon points="60,14 106,60 60,106 14,60" fill="#020817" stroke="#f1df76" stroke-width="1.5"/>
  <line x1="60" y1="14" x2="60" y2="106" stroke="#38bdf8" stroke-width="1" stroke-dasharray="3,3" opacity="0.7"/>
  <line x1="14" y1="60" x2="106" y2="60" stroke="#38bdf8" stroke-width="1" stroke-dasharray="3,3" opacity="0.7"/>
  <circle cx="60" cy="60" r="26" fill="none" stroke="#38bdf8" stroke-width="1.5" opacity="0.6"/>
  <line x1="26" y1="26" x2="94" y2="94" stroke="#f8fafc" stroke-width="2.5" stroke-linecap="round"/>
  <circle cx="28" cy="28" r="3" fill="#38bdf8"/>
  <line x1="94" y1="26" x2="26" y2="94" stroke="#f8fafc" stroke-width="2.5" stroke-linecap="round"/>
  <circle cx="92" cy="28" r="3" fill="#38bdf8"/>
  <polygon points="60,34 72,60 60,86 48,60" fill="url(#se3-azure-sm)" stroke="#f8fafc" stroke-width="2"/>
  <ellipse cx="60" cy="60" rx="6" ry="14" fill="#bae6fd"/>
  <path d="M 46,50 Q 60,42 74,50 Q 60,58 46,50" fill="none" stroke="#f1df76" stroke-width="1.5"/>
  <path d="M 46,70 Q 60,62 74,70 Q 60,78 46,70" fill="none" stroke="#f1df76" stroke-width="1.5"/>
</svg>""",

    'profile': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <linearGradient id="se3-azure-lg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7dd3fc"/>
      <stop offset="40%" stop-color="#0284c7"/>
      <stop offset="80%" stop-color="#0369a1"/>
      <stop offset="100%" stop-color="#082f49"/>
    </linearGradient>
    <radialGradient id="se3-glow-lg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.8"/>
      <stop offset="60%" stop-color="#0284c7" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#020617" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="500" height="500" fill="#020817"/>
  <polygon points="250,20 480,250 250,480 20,250" fill="#04142e" stroke="#38bdf8" stroke-width="6"/>
  <polygon points="250,50 450,250 250,450 50,250" fill="#010a19" stroke="#f1df76" stroke-width="3"/>
  <circle cx="250" cy="250" r="160" fill="url(#se3-glow-lg)"/>
  <line x1="250" y1="50" x2="250" y2="450" stroke="#38bdf8" stroke-width="2" stroke-dasharray="8,6" opacity="0.7"/>
  <line x1="50" y1="250" x2="450" y2="250" stroke="#38bdf8" stroke-width="2" stroke-dasharray="8,6" opacity="0.7"/>
  <line x1="110" y1="110" x2="390" y2="390" stroke="#f8fafc" stroke-width="6" stroke-linecap="round"/>
  <circle cx="115" cy="115" r="8" fill="#38bdf8" stroke="#ffffff" stroke-width="2"/>
  <line x1="390" y1="110" x2="110" y2="390" stroke="#f8fafc" stroke-width="6" stroke-linecap="round"/>
  <circle cx="385" cy="115" r="8" fill="#38bdf8" stroke="#ffffff" stroke-width="2"/>
  <polygon points="250,140 300,250 250,360 200,250" fill="url(#se3-azure-lg)" stroke="#f8fafc" stroke-width="5"/>
  <ellipse cx="250" cy="250" rx="25" ry="55" fill="#bae6fd"/>
  <path d="M 190,210 Q 250,175 310,210 Q 250,245 190,210" fill="none" stroke="#f1df76" stroke-width="4"/>
  <path d="M 190,290 Q 250,255 310,290 Q 250,325 190,290" fill="none" stroke="#f1df76" stroke-width="4"/>
</svg>"""
}

# -------------------------------------------------------------
# SE-004: The Rust-Bleeding Sentry (Riveted Octagonal Iron Bastion)
# -------------------------------------------------------------
ENTITIES_SUITE['se-004'] = {
    'icon': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="se4-rust-sm" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ea580c"/>
      <stop offset="50%" stop-color="#9a3412"/>
      <stop offset="100%" stop-color="#431407"/>
    </linearGradient>
  </defs>
  <polygon points="38,8 82,8 112,38 112,82 82,112 38,112 8,82 8,38" fill="#1c0a04" stroke="#ea580c" stroke-width="3"/>
  <polygon points="40,14 80,14 106,40 106,80 80,106 40,106 14,80 14,40" fill="#0f0502" stroke="#475569" stroke-width="2"/>
  <circle cx="38" cy="11" r="2" fill="#94a3b8"/><circle cx="82" cy="11" r="2" fill="#94a3b8"/>
  <circle cx="109" cy="38" r="2" fill="#94a3b8"/><circle cx="109" cy="82" r="2" fill="#94a3b8"/>
  <line x1="20" y1="20" x2="100" y2="100" stroke="#64748b" stroke-width="3"/>
  <path d="M 20,20 L 32,16 L 28,32 Z" fill="#ea580c" stroke="#f97316" stroke-width="1"/>
  <line x1="100" y1="20" x2="20" y2="100" stroke="#64748b" stroke-width="3"/>
  <path d="M 100,20 L 88,16 L 92,32 Z" fill="#ea580c" stroke="#f97316" stroke-width="1"/>
  <path d="M 38,40 L 82,40 L 78,82 L 60,94 L 42,82 Z" fill="url(#se4-rust-sm)" stroke="#f97316" stroke-width="2"/>
  <rect x="44" y="52" width="32" height="6" fill="#0f172a" stroke="#f97316" stroke-width="1.5"/>
  <circle cx="52" cy="55" r="2" fill="#ef4444"/><circle cx="68" cy="55" r="2" fill="#ef4444"/>
  <path d="M 52,58 L 50,78 L 48,88" fill="none" stroke="#ea580c" stroke-width="2" stroke-linecap="round"/>
  <path d="M 68,58 L 70,78 L 72,88" fill="none" stroke="#ea580c" stroke-width="2" stroke-linecap="round"/>
</svg>""",

    'profile': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <linearGradient id="se4-rust-lg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f97316"/>
      <stop offset="40%" stop-color="#c2410c"/>
      <stop offset="80%" stop-color="#7c2d12"/>
      <stop offset="100%" stop-color="#2d0a02"/>
    </linearGradient>
  </defs>
  <rect width="500" height="500" fill="#0f0502"/>
  <!-- Octagonal Bastion Outer Silhouette (Identical to Icon) -->
  <polygon points="150,25 350,25 475,150 475,350 350,475 150,475 25,350 25,150" fill="#240c05" stroke="#ea580c" stroke-width="6"/>
  <polygon points="160,45 340,45 455,160 455,340 340,455 160,455 45,340 45,160" fill="#0d0401" stroke="#475569" stroke-width="3"/>
  <!-- Corner Rivets -->
  <circle cx="150" cy="35" r="5" fill="#94a3b8"/><circle cx="350" cy="35" r="5" fill="#94a3b8"/>
  <circle cx="465" cy="150" r="5" fill="#94a3b8"/><circle cx="465" cy="350" r="5" fill="#94a3b8"/>
  <circle cx="350" cy="465" r="5" fill="#94a3b8"/><circle cx="150" cy="465" r="5" fill="#94a3b8"/>
  <circle cx="35" cy="350" r="5" fill="#94a3b8"/><circle cx="35" cy="150" r="5" fill="#94a3b8"/>
  <!-- Crossed Rust Halberds -->
  <line x1="80" y1="80" x2="420" y2="420" stroke="#64748b" stroke-width="8"/>
  <path d="M 80,80 L 130,65 L 115,130 Z" fill="#ea580c" stroke="#f97316" stroke-width="3"/>
  <line x1="420" y1="80" x2="80" y2="420" stroke="#64748b" stroke-width="8"/>
  <path d="M 420,80 L 370,65 L 385,130 Z" fill="#ea580c" stroke="#f97316" stroke-width="3"/>
  <!-- Automaton Helm -->
  <path d="M 160,160 L 340,160 L 325,330 L 250,380 L 175,330 Z" fill="url(#se4-rust-lg)" stroke="#f97316" stroke-width="5"/>
  <rect x="180" y="210" width="140" height="24" fill="#020617" stroke="#f97316" stroke-width="3"/>
  <circle cx="215" cy="222" r="6" fill="#ef4444"/><circle cx="285" cy="222" r="6" fill="#ef4444"/>
  <path d="M 215,234 L 210,310 L 205,355" fill="none" stroke="#ea580c" stroke-width="6" stroke-linecap="round"/>
  <path d="M 285,234 L 290,310 L 295,355" fill="none" stroke="#ea580c" stroke-width="6" stroke-linecap="round"/>
</svg>"""
}

# -------------------------------------------------------------
# SE-005: The Smothering Mother (Gilded Cameo Teardrop Medallion)
# -------------------------------------------------------------
ENTITIES_SUITE['se-005'] = {
    'icon': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="se5-gold-sm" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="50%" stop-color="#eab308"/>
      <stop offset="100%" stop-color="#854d0e"/>
    </linearGradient>
  </defs>
  <path d="M 60,6 C 92,6 112,38 112,74 C 112,98 88,114 60,114 C 32,114 8,98 8,74 C 8,38 28,6 60,6 Z" fill="#0c0a14" stroke="url(#se5-gold-sm)" stroke-width="3"/>
  <path d="M 60,12 C 86,12 104,40 104,72 C 104,94 84,108 60,108 C 36,108 16,94 16,72 C 16,40 34,12 60,12 Z" fill="#030712" stroke="#f1df76" stroke-width="1"/>
  <path d="M 24,70 C 40,50 80,90 96,70" fill="none" stroke="#475569" stroke-width="3.5"/>
  <path d="M 24,82 C 40,62 80,102 96,82" fill="none" stroke="#1e293b" stroke-width="4.5"/>
  <path d="M 44,48 C 44,30 76,30 76,48 C 76,64 44,64 44,48 Z" fill="#f8fafc" stroke="#f1df76" stroke-width="1.5"/>
  <path d="M 50,46 Q 54,50 58,46" fill="none" stroke="#64748b" stroke-width="1.5"/>
  <path d="M 62,46 Q 66,50 70,46" fill="none" stroke="#64748b" stroke-width="1.5"/>
  <polygon points="60,68 68,76 60,84 52,76" fill="url(#se5-gold-sm)" stroke="#ffffff" stroke-width="1"/>
  <circle cx="60" cy="76" r="2.5" fill="#38bdf8"/>
</svg>""",

    'profile': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <linearGradient id="se5-gold-lg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="40%" stop-color="#eab308"/>
      <stop offset="80%" stop-color="#854d0e"/>
      <stop offset="100%" stop-color="#422006"/>
    </linearGradient>
  </defs>
  <rect width="500" height="500" fill="#050308"/>
  <!-- Teardrop Cameo Medallion Frame (Identical to Icon) -->
  <path d="M 250,25 C 380,25 465,160 465,310 C 465,410 365,475 250,475 C 135,475 35,410 35,310 C 35,160 120,25 250,25 Z" fill="#140f20" stroke="url(#se5-gold-lg)" stroke-width="6"/>
  <path d="M 250,50 C 355,50 430,170 430,295 C 430,385 345,445 250,445 C 155,445 70,385 70,295 C 70,170 145,50 250,50 Z" fill="#07040b" stroke="#f1df76" stroke-width="3"/>
  <path d="M 100,290 C 165,210 335,370 400,290" fill="none" stroke="#475569" stroke-width="12"/>
  <path d="M 100,340 C 165,260 335,420 400,340" fill="none" stroke="#1e293b" stroke-width="14"/>
  <path d="M 185,200 C 185,120 315,120 315,200 C 315,265 185,265 185,200 Z" fill="#ffffff" stroke="#f1df76" stroke-width="4"/>
  <circle cx="250" cy="190" r="90" fill="none" stroke="#f1df76" stroke-width="3" stroke-dasharray="10,6"/>
  <path d="M 210,190 Q 225,205 240,190" fill="none" stroke="#64748b" stroke-width="4"/>
  <path d="M 260,190 Q 275,205 290,190" fill="none" stroke="#64748b" stroke-width="4"/>
  <polygon points="250,280 280,310 250,340 220,310" fill="url(#se5-gold-lg)" stroke="#ffffff" stroke-width="3"/>
  <circle cx="250" cy="310" r="10" fill="#38bdf8"/>
</svg>"""
}

# -------------------------------------------------------------
# SE-006: The Siphon Leech (Biohazard Vortex Turbine)
# -------------------------------------------------------------
ENTITIES_SUITE['se-006'] = {
    'icon': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="se6-green-sm" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="60%" stop-color="#047857"/>
      <stop offset="100%" stop-color="#022c22"/>
    </radialGradient>
  </defs>
  <circle cx="60" cy="60" r="54" fill="#021f18" stroke="#10b981" stroke-width="3"/>
  <circle cx="60" cy="60" r="48" fill="#01140f" stroke="#059669" stroke-width="1.5"/>
  <circle cx="60" cy="60" r="38" fill="url(#se6-green-sm)"/>
  <circle cx="60" cy="60" r="26" fill="#022c22" stroke="#6ee7b7" stroke-width="2"/>
  <circle cx="60" cy="60" r="16" fill="#01140f" stroke="#a7f3d0" stroke-width="1.5"/>
  <circle cx="60" cy="60" r="6" fill="#000000"/>
  <polygon points="60,34 58,40 62,40" fill="#f8fafc"/>
  <polygon points="60,86 58,80 62,80" fill="#f8fafc"/>
  <polygon points="34,60 40,58 40,62" fill="#f8fafc"/>
  <polygon points="86,60 80,58 80,62" fill="#f8fafc"/>
  <path d="M 22,36 Q 36,24 50,22" fill="none" stroke="#34d399" stroke-width="2"/>
  <path d="M 98,84 Q 84,96 70,98" fill="none" stroke="#34d399" stroke-width="2"/>
</svg>""",

    'profile': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <radialGradient id="se6-green-lg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#34d399"/>
      <stop offset="50%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#022c22"/>
    </radialGradient>
  </defs>
  <rect width="500" height="500" fill="#010d0a"/>
  <!-- Circular Turbine Frame (Identical to Icon) -->
  <circle cx="250" cy="250" r="225" fill="#03261e" stroke="#10b981" stroke-width="6"/>
  <circle cx="250" cy="250" r="200" fill="#01140f" stroke="#059669" stroke-width="3"/>
  <circle cx="250" cy="250" r="160" fill="url(#se6-green-lg)"/>
  <circle cx="250" cy="250" r="110" fill="#022c22" stroke="#6ee7b7" stroke-width="5"/>
  <circle cx="250" cy="250" r="70" fill="#01140f" stroke="#a7f3d0" stroke-width="4"/>
  <circle cx="250" cy="250" r="25" fill="#000000"/>
  <!-- Barbed Concentric Teeth -->
  <polygon points="250,140 242,165 258,165" fill="#ffffff"/>
  <polygon points="250,360 242,335 258,335" fill="#ffffff"/>
  <polygon points="140,250 165,242 165,258" fill="#ffffff"/>
  <polygon points="360,250 335,242 335,258" fill="#ffffff"/>
  <!-- Siphon Pump Curved Blades -->
  <path d="M 90,150 Q 150,100 210,90" fill="none" stroke="#34d399" stroke-width="6"/>
  <path d="M 410,350 Q 350,400 290,410" fill="none" stroke="#34d399" stroke-width="6"/>
</svg>"""
}

# -------------------------------------------------------------
# SE-007: Brume (Archival Rounded Basalt Tablet)
# -------------------------------------------------------------
ENTITIES_SUITE['se-007'] = {
    'icon': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="se7-slate-sm" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#475569"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <rect x="10" y="8" width="100" height="104" rx="14" fill="#070c14" stroke="#94a3b8" stroke-width="2.5"/>
  <rect x="16" y="14" width="88" height="92" rx="10" fill="url(#se7-slate-sm)" stroke="#38bdf8" stroke-width="1.5"/>
  <path d="M 16,35 C 35,25 45,45 65,30 C 85,15 95,35 104,28" fill="none" stroke="#cbd5e1" stroke-width="2" opacity="0.6"/>
  <path d="M 16,85 C 35,75 45,95 65,80 C 85,65 95,85 104,78" fill="none" stroke="#cbd5e1" stroke-width="2" opacity="0.6"/>
  <rect x="34" y="30" width="52" height="60" rx="4" fill="#020617" stroke="#64748b" stroke-width="1.5"/>
  <line x1="42" y1="42" x2="78" y2="42" stroke="#38bdf8" stroke-width="1.5"/>
  <line x1="42" y1="52" x2="74" y2="52" stroke="#38bdf8" stroke-width="1.5"/>
  <line x1="42" y1="62" x2="70" y2="62" stroke="#38bdf8" stroke-width="1.5"/>
  <line x1="84" y1="24" x2="56" y2="76" stroke="#f1df76" stroke-width="3" stroke-linecap="round"/>
  <polygon points="56,76 52,82 59,79" fill="#f8fafc"/>
</svg>""",

    'profile': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <linearGradient id="se7-slate-lg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#64748b"/>
      <stop offset="50%" stop-color="#334155"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <rect width="500" height="500" fill="#040812"/>
  <!-- Rounded Tablet Outer Silhouette (Identical to Icon) -->
  <rect x="40" y="35" width="420" height="430" rx="50" fill="#0a121e" stroke="#94a3b8" stroke-width="6"/>
  <rect x="65" y="60" width="370" height="380" rx="40" fill="url(#se7-slate-lg)" stroke="#38bdf8" stroke-width="3"/>
  <!-- Swirling Fog Ribbons -->
  <path d="M 65,150 C 150,110 190,190 280,130 C 370,70 410,150 435,120" fill="none" stroke="#cbd5e1" stroke-width="6" opacity="0.6"/>
  <path d="M 65,350 C 150,310 190,390 280,330 C 370,270 410,350 435,320" fill="none" stroke="#cbd5e1" stroke-width="6" opacity="0.6"/>
  <!-- Basalt Tablet -->
  <rect x="140" y="130" width="220" height="240" rx="16" fill="#020617" stroke="#64748b" stroke-width="4"/>
  <line x1="170" y1="180" x2="330" y2="180" stroke="#38bdf8" stroke-width="4"/>
  <line x1="170" y1="220" x2="310" y2="220" stroke="#38bdf8" stroke-width="4"/>
  <line x1="170" y1="260" x2="290" y2="260" stroke="#38bdf8" stroke-width="4"/>
  <line x1="170" y1="300" x2="260" y2="300" stroke="#38bdf8" stroke-width="4"/>
  <!-- Obsidian Stylus -->
  <line x1="350" y1="100" x2="240" y2="310" stroke="#f1df76" stroke-width="8" stroke-linecap="round"/>
  <polygon points="240,310 225,335 250,325" fill="#f8fafc"/>
</svg>"""
}

# -------------------------------------------------------------
# SE-008: The Iron Maiden of Regret (Gothic Reliquary Arch)
# -------------------------------------------------------------
ENTITIES_SUITE['se-008'] = {
    'icon': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="se8-crimson-sm" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#7f1d1d"/>
    </linearGradient>
  </defs>
  <path d="M 60,4 L 106,30 L 106,112 L 14,112 L 14,30 Z" fill="#170307" stroke="#ef4444" stroke-width="3"/>
  <path d="M 60,12 L 98,34 L 98,104 L 22,104 L 22,34 Z" fill="#090103" stroke="#991b1b" stroke-width="1.5"/>
  <ellipse cx="60" cy="30" rx="20" ry="6" fill="none" stroke="#ef4444" stroke-width="2"/>
  <line x1="44" y1="26" x2="40" y2="20" stroke="#ef4444" stroke-width="2"/>
  <line x1="76" y1="26" x2="80" y2="20" stroke="#ef4444" stroke-width="2"/>
  <rect x="36" y="40" width="48" height="60" rx="4" fill="#1e293b" stroke="#f1df76" stroke-width="1.5"/>
  <line x1="42" y1="48" x2="56" y2="52" stroke="#ef4444" stroke-width="2"/>
  <line x1="42" y1="60" x2="58" y2="62" stroke="#ef4444" stroke-width="2"/>
  <line x1="78" y1="48" x2="64" y2="52" stroke="#ef4444" stroke-width="2"/>
  <line x1="78" y1="60" x2="62" y2="62" stroke="#ef4444" stroke-width="2"/>
  <line x1="60" y1="44" x2="60" y2="92" stroke="#f87171" stroke-width="1.5" stroke-dasharray="2,2"/>
</svg>""",

    'profile': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <linearGradient id="se8-iron-lg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#64748b"/>
      <stop offset="50%" stop-color="#334155"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <rect width="500" height="500" fill="#0b0103"/>
  <!-- Gothic Reliquary Arch (Identical to Icon) -->
  <path d="M 250,20 L 440,120 L 440,470 L 60,470 L 60,120 Z" fill="#170307" stroke="#ef4444" stroke-width="6"/>
  <path d="M 250,50 L 410,140 L 410,440 L 90,440 L 90,140 Z" fill="#090103" stroke="#991b1b" stroke-width="3"/>
  <ellipse cx="250" cy="120" rx="80" ry="24" fill="none" stroke="#ef4444" stroke-width="4"/>
  <line x1="180" y1="105" x2="165" y2="80" stroke="#ef4444" stroke-width="4"/>
  <line x1="320" y1="105" x2="335" y2="80" stroke="#ef4444" stroke-width="4"/>
  <rect x="150" y="160" width="200" height="240" rx="16" fill="url(#se8-iron-lg)" stroke="#f1df76" stroke-width="4"/>
  <line x1="170" y1="200" x2="230" y2="215" stroke="#ef4444" stroke-width="5" stroke-linecap="round"/>
  <line x1="170" y1="250" x2="235" y2="260" stroke="#ef4444" stroke-width="5" stroke-linecap="round"/>
  <line x1="330" y1="200" x2="270" y2="215" stroke="#ef4444" stroke-width="5" stroke-linecap="round"/>
  <line x1="330" y1="250" x2="265" y2="260" stroke="#ef4444" stroke-width="5" stroke-linecap="round"/>
  <line x1="250" y1="180" x2="250" y2="370" stroke="#f87171" stroke-width="4" stroke-dasharray="6,4"/>
</svg>"""
}

# -------------------------------------------------------------
# SE-009: Drowned Bell (Bolted Submersible Porthole Ring)
# -------------------------------------------------------------
ENTITIES_SUITE['se-009'] = {
    'icon': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="se9-ocean-sm" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="70%" stop-color="#0369a1"/>
      <stop offset="100%" stop-color="#082f49"/>
    </radialGradient>
  </defs>
  <circle cx="60" cy="60" r="54" fill="#04121e" stroke="#0284c7" stroke-width="3"/>
  <circle cx="60" cy="60" r="46" fill="url(#se9-ocean-sm)" stroke="#ca8a04" stroke-width="2.5"/>
  <circle cx="60" cy="10" r="2.5" fill="#f1df76"/><circle cx="60" cy="110" r="2.5" fill="#f1df76"/>
  <circle cx="10" cy="60" r="2.5" fill="#f1df76"/><circle cx="110" cy="60" r="2.5" fill="#f1df76"/>
  <path d="M 60,34 C 50,34 46,48 42,62 C 40,70 38,72 36,74 L 84,74 C 82,72 80,70 78,62 C 74,48 70,34 60,34 Z" fill="#b45309" stroke="#f1df76" stroke-width="1.5"/>
  <ellipse cx="60" cy="74" rx="24" ry="4" fill="#78350f" stroke="#f1df76" stroke-width="1.5"/>
  <circle cx="60" cy="74" r="16" fill="none" stroke="#7dd3fc" stroke-width="1" stroke-dasharray="2,3" opacity="0.8"/>
  <circle cx="44" cy="42" r="2" fill="#e0f2fe" opacity="0.7"/><circle cx="76" cy="46" r="2.5" fill="#e0f2fe" opacity="0.7"/>
</svg>""",

    'profile': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <radialGradient id="se9-ocean-lg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="60%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#082f49"/>
    </radialGradient>
  </defs>
  <rect width="500" height="500" fill="#020d17"/>
  <!-- Bolted Porthole (Identical to Icon) -->
  <circle cx="250" cy="250" r="225" fill="#04121e" stroke="#0284c7" stroke-width="6"/>
  <circle cx="250" cy="250" r="190" fill="url(#se9-ocean-lg)" stroke="#ca8a04" stroke-width="5"/>
  <!-- 8 Heavy Bolts -->
  <circle cx="250" cy="40" r="8" fill="#f1df76"/><circle cx="250" cy="460" r="8" fill="#f1df76"/>
  <circle cx="40" cy="250" r="8" fill="#f1df76"/><circle cx="460" cy="250" r="8" fill="#f1df76"/>
  <circle cx="100" cy="100" r="8" fill="#f1df76"/><circle cx="400" cy="400" r="8" fill="#f1df76"/>
  <circle cx="400" cy="100" r="8" fill="#f1df76"/><circle cx="100" cy="400" r="8" fill="#f1df76"/>
  <!-- Submerged Bronze Bell -->
  <path d="M 250,140 C 205,140 190,200 175,260 C 165,290 155,300 150,310 L 350,310 C 345,300 335,290 325,260 C 310,200 295,140 250,140 Z" fill="#b45309" stroke="#f1df76" stroke-width="4"/>
  <ellipse cx="250" cy="310" rx="100" ry="16" fill="#78350f" stroke="#f1df76" stroke-width="4"/>
  <circle cx="250" cy="310" r="70" fill="none" stroke="#7dd3fc" stroke-width="2" stroke-dasharray="6,6" opacity="0.8"/>
  <circle cx="180" cy="180" r="8" fill="#e0f2fe" opacity="0.7"/><circle cx="320" cy="200" r="10" fill="#e0f2fe" opacity="0.7"/>
</svg>"""
}

# -------------------------------------------------------------
# SE-010: The Convergence (12-Pointed Singularity Star)
# -------------------------------------------------------------
ENTITIES_SUITE['se-010'] = {
    'icon': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="se10-void-sm" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="30%" stop-color="#c7d2fe"/>
      <stop offset="70%" stop-color="#312e81"/>
      <stop offset="100%" stop-color="#020617"/>
    </radialGradient>
  </defs>
  <circle cx="60" cy="60" r="56" fill="#050314" stroke="#e0e7ff" stroke-width="2.5"/>
  <polygon points="60,6 66,42 98,22 78,54 114,60 78,66 98,98 66,78 60,114 54,78 22,98 42,66 6,60 42,54 22,22 54,42" fill="none" stroke="#818cf8" stroke-width="1.5"/>
  <circle cx="60" cy="60" r="34" fill="url(#se10-void-sm)" stroke="#ffffff" stroke-width="2"/>
  <circle cx="60" cy="60" r="22" fill="#000000" stroke="#f1df76" stroke-width="2"/>
  <ellipse cx="60" cy="60" rx="14" ry="7" fill="#ffffff"/>
  <circle cx="60" cy="60" r="4.5" fill="#000000"/>
  <circle cx="62" cy="58" r="1.5" fill="#38bdf8"/>
</svg>""",

    'profile': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <radialGradient id="se10-void-lg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="30%" stop-color="#c7d2fe"/>
      <stop offset="60%" stop-color="#4338ca"/>
      <stop offset="100%" stop-color="#020617"/>
    </radialGradient>
  </defs>
  <rect width="500" height="500" fill="#03020a"/>
  <!-- 12-Pointed Singularity Star Outer Silhouette (Identical to Icon) -->
  <circle cx="250" cy="250" r="235" fill="#050314" stroke="#e0e7ff" stroke-width="6"/>
  <polygon points="250,25 275,175 410,90 325,225 475,250 325,275 410,410 275,325 250,475 225,325 90,410 175,275 25,250 175,225 90,90 225,175" fill="none" stroke="#818cf8" stroke-width="4"/>
  <circle cx="250" cy="250" r="140" fill="url(#se10-void-lg)" stroke="#ffffff" stroke-width="5"/>
  <circle cx="250" cy="250" r="90" fill="#000000" stroke="#f1df76" stroke-width="4"/>
  <ellipse cx="250" cy="250" rx="60" ry="30" fill="#ffffff"/>
  <circle cx="250" cy="250" r="18" fill="#000000"/>
  <circle cx="256" cy="244" r="6" fill="#38bdf8"/>
</svg>"""
}

# -------------------------------------------------------------
# SE-011: The Whispering Walls (Crenelated Labyrinth Wall)
# -------------------------------------------------------------
ENTITIES_SUITE['se-011'] = {
    'icon': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="se11-lead-sm" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#475569"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
  </defs>
  <polygon points="20,10 40,10 40,18 60,18 60,10 80,10 80,18 100,18 100,10 108,18 108,86 60,114 12,86 12,18" fill="#0b0f19" stroke="#ef4444" stroke-width="2.5"/>
  <rect x="22" y="26" width="76" height="68" fill="url(#se11-lead-sm)" stroke="#38bdf8" stroke-width="1.5"/>
  <line x1="22" y1="48" x2="98" y2="48" stroke="#334155" stroke-width="1.5"/>
  <line x1="22" y1="70" x2="98" y2="70" stroke="#334155" stroke-width="1.5"/>
  <line x1="47" y1="26" x2="47" y2="94" stroke="#334155" stroke-width="1.5"/>
  <line x1="73" y1="26" x2="73" y2="94" stroke="#334155" stroke-width="1.5"/>
  <ellipse cx="60" cy="37" rx="6" ry="7" fill="#0f172a" stroke="#cbd5e1" stroke-width="1"/>
  <ellipse cx="60" cy="40" rx="2" ry="3" fill="#ef4444"/>
  <ellipse cx="35" cy="59" rx="6" ry="7" fill="#0f172a" stroke="#cbd5e1" stroke-width="1"/>
  <ellipse cx="35" cy="62" rx="2" ry="3" fill="#ef4444"/>
  <ellipse cx="85" cy="59" rx="6" ry="7" fill="#0f172a" stroke="#cbd5e1" stroke-width="1"/>
  <ellipse cx="85" cy="62" rx="2" ry="3" fill="#ef4444"/>
</svg>""",

    'profile': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <linearGradient id="se11-lead-lg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#64748b"/>
      <stop offset="50%" stop-color="#334155"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
  </defs>
  <rect width="500" height="500" fill="#060912"/>
  <!-- Crenelated Fortress Labyrinth Shield (Identical to Icon) -->
  <polygon points="80,40 160,40 160,70 240,70 240,40 320,40 320,70 400,70 400,40 435,70 435,360 250,470 65,360 65,70" fill="#0b0f19" stroke="#ef4444" stroke-width="6"/>
  <rect x="90" y="100" width="320" height="280" fill="url(#se11-lead-lg)" stroke="#38bdf8" stroke-width="4"/>
  <line x1="90" y1="190" x2="410" y2="190" stroke="#1e293b" stroke-width="4"/>
  <line x1="90" y1="280" x2="410" y2="280" stroke="#1e293b" stroke-width="4"/>
  <line x1="195" y1="100" x2="195" y2="380" stroke="#1e293b" stroke-width="4"/>
  <line x1="305" y1="100" x2="305" y2="380" stroke="#1e293b" stroke-width="4"/>
  <!-- Three Whispering Relief Faces -->
  <ellipse cx="250" cy="145" rx="24" ry="28" fill="#0f172a" stroke="#cbd5e1" stroke-width="3"/>
  <ellipse cx="250" cy="155" rx="8" ry="12" fill="#ef4444"/>
  <ellipse cx="145" cy="235" rx="24" ry="28" fill="#0f172a" stroke="#cbd5e1" stroke-width="3"/>
  <ellipse cx="145" cy="245" rx="8" ry="12" fill="#ef4444"/>
  <ellipse cx="355" cy="235" rx="24" ry="28" fill="#0f172a" stroke="#cbd5e1" stroke-width="3"/>
  <ellipse cx="355" cy="245" rx="8" ry="12" fill="#ef4444"/>
</svg>"""
}

# -------------------------------------------------------------
# SE-014: The Debt Eater (Imperial Square-Hole Coin Seal)
# -------------------------------------------------------------
ENTITIES_SUITE['se-014'] = {
    'icon': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="se14-gold-sm" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="50%" stop-color="#eab308"/>
      <stop offset="100%" stop-color="#713f12"/>
    </linearGradient>
  </defs>
  <circle cx="60" cy="60" r="54" fill="#140d04" stroke="url(#se14-gold-sm)" stroke-width="3"/>
  <circle cx="60" cy="60" r="46" fill="#0a0501" stroke="#ca8a04" stroke-width="1.5"/>
  <rect x="54" y="16" width="12" height="6" fill="#eab308"/><rect x="54" y="98" width="12" height="6" fill="#eab308"/>
  <path d="M 28,42 Q 60,20 92,42 Q 96,68 92,82 Q 60,98 28,82 Z" fill="#18181b" stroke="#f1df76" stroke-width="2"/>
  <polygon points="34,46 38,54 42,46" fill="#fef08a"/><polygon points="46,44 50,54 54,44" fill="#fef08a"/>
  <polygon points="58,44 62,54 66,44" fill="#fef08a"/><polygon points="70,44 74,54 78,44" fill="#fef08a"/>
  <polygon points="38,78 42,70 46,78" fill="#fef08a"/><polygon points="50,80 54,70 58,80" fill="#fef08a"/>
  <polygon points="62,80 66,70 70,80" fill="#fef08a"/><polygon points="74,78 78,70 82,78" fill="#fef08a"/>
  <polygon points="46,58 60,54 74,58 74,68 60,64 46,68" fill="#f8fafc" stroke="#94a3b8" stroke-width="1"/>
</svg>""",

    'profile': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <linearGradient id="se14-gold-lg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="40%" stop-color="#eab308"/>
      <stop offset="80%" stop-color="#854d0e"/>
      <stop offset="100%" stop-color="#422006"/>
    </linearGradient>
  </defs>
  <rect width="500" height="500" fill="#0a0602"/>
  <!-- Ancient Coin Frame (Identical to Icon) -->
  <circle cx="250" cy="250" r="225" fill="#1f1406" stroke="url(#se14-gold-lg)" stroke-width="6"/>
  <circle cx="250" cy="250" r="190" fill="#0d0802" stroke="#ca8a04" stroke-width="3"/>
  <!-- Archival Coin Inscriptions -->
  <rect x="225" y="65" width="50" height="25" fill="#eab308"/>
  <rect x="225" y="410" width="50" height="25" fill="#eab308"/>
  <!-- Vested Beast Jaw -->
  <path d="M 120,180 Q 250,90 380,180 Q 400,280 380,340 Q 250,410 120,340 Z" fill="#18181b" stroke="#f1df76" stroke-width="5"/>
  <!-- Gold Teeth -->
  <polygon points="150,195 165,225 180,195" fill="#fef08a"/>
  <polygon points="200,185 215,225 230,185" fill="#fef08a"/>
  <polygon points="250,185 265,225 280,185" fill="#fef08a"/>
  <polygon points="300,185 315,225 330,185" fill="#fef08a"/>
  <polygon points="350,195 365,225 380,195" fill="#fef08a"/>
  <!-- Swallowed Ledger -->
  <polygon points="180,240 250,225 320,240 320,285 250,270 180,285" fill="#f8fafc" stroke="#94a3b8" stroke-width="3"/>
  <line x1="250" y1="225" x2="250" y2="270" stroke="#ef4444" stroke-width="4"/>
</svg>"""
}

# -------------------------------------------------------------
# SE-015: The Debt Scale (Balanced Diamond Fulcrum)
# -------------------------------------------------------------
ENTITIES_SUITE['se-015'] = {
    'icon': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="se15-sovereign-sm" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="50%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#1e3a8a"/>
    </linearGradient>
  </defs>
  <polygon points="60,4 114,60 60,116 6,60" fill="#060814" stroke="#f8fafc" stroke-width="2.5"/>
  <polygon points="60,12 106,60 60,108 14,60" fill="#02040a" stroke="#f1df76" stroke-width="1.5"/>
  <polygon points="50,18 55,14 60,18 65,14 70,18 68,24 52,24" fill="#f1df76" stroke="#ffffff" stroke-width="1"/>
  <line x1="60" y1="24" x2="60" y2="98" stroke="#f8fafc" stroke-width="3" stroke-linecap="round"/>
  <line x1="26" y1="38" x2="94" y2="38" stroke="#f1df76" stroke-width="3" stroke-linecap="round"/>
  <circle cx="60" cy="38" r="4" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5"/>
  <line x1="30" y1="38" x2="22" y2="68" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="30" y1="38" x2="38" y2="68" stroke="#94a3b8" stroke-width="1.5"/>
  <path d="M 18,68 Q 30,76 42,68 Z" fill="url(#se15-sovereign-sm)" stroke="#f1df76" stroke-width="1.5"/>
  <circle cx="30" cy="62" r="3.5" fill="#ef4444"/>
  <line x1="90" y1="38" x2="82" y2="68" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="90" y1="38" x2="98" y2="68" stroke="#94a3b8" stroke-width="1.5"/>
  <path d="M 78,68 Q 90,76 102,68 Z" fill="url(#se15-sovereign-sm)" stroke="#f1df76" stroke-width="1.5"/>
  <rect x="85" y="58" width="10" height="7" fill="#64748b" stroke="#f8fafc" stroke-width="1"/>
</svg>""",

    'profile': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <linearGradient id="se15-sovereign-lg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="40%" stop-color="#38bdf8"/>
      <stop offset="80%" stop-color="#1e3a8a"/>
      <stop offset="100%" stop-color="#020617"/>
    </linearGradient>
  </defs>
  <rect width="500" height="500" fill="#03040a"/>
  <!-- Diamond Fulcrum Frame (Identical to Icon) -->
  <polygon points="250,15 485,250 250,485 15,250" fill="#090d1f" stroke="#f8fafc" stroke-width="6"/>
  <polygon points="250,45 455,250 250,455 45,250" fill="#02040b" stroke="#f1df76" stroke-width="3"/>
  <!-- Sovereign Crown -->
  <polygon points="210,75 230,60 250,75 270,60 290,75 280,100 220,100" fill="#f1df76" stroke="#ffffff" stroke-width="3"/>
  <!-- Central Sovereign Sword Fulcrum -->
  <line x1="250" y1="100" x2="250" y2="410" stroke="#f8fafc" stroke-width="8" stroke-linecap="round"/>
  <!-- Horizontal Balance Beam -->
  <line x1="110" y1="160" x2="390" y2="160" stroke="#f1df76" stroke-width="8" stroke-linecap="round"/>
  <circle cx="250" cy="160" r="14" fill="#38bdf8" stroke="#ffffff" stroke-width="4"/>
  <!-- Left Scale Pan (Weeping Heart) -->
  <line x1="130" y1="160" x2="95" y2="280" stroke="#94a3b8" stroke-width="4"/>
  <line x1="130" y1="160" x2="165" y2="280" stroke="#94a3b8" stroke-width="4"/>
  <path d="M 80,280 Q 130,310 180,280 Z" fill="url(#se15-sovereign-lg)" stroke="#f1df76" stroke-width="4"/>
  <circle cx="130" cy="255" r="14" fill="#ef4444"/>
  <!-- Right Scale Pan (Lead Slates) -->
  <line x1="370" y1="160" x2="335" y2="280" stroke="#94a3b8" stroke-width="4"/>
  <line x1="370" y1="160" x2="405" y2="280" stroke="#94a3b8" stroke-width="4"/>
  <path d="M 320,280 Q 370,310 420,280 Z" fill="url(#se15-sovereign-lg)" stroke="#f1df76" stroke-width="4"/>
  <rect x="350" y="240" width="40" height="28" fill="#64748b" stroke="#f8fafc" stroke-width="3"/>
</svg>"""
}

# Write all synchronized SVGs to assets/art/entities/ and icons/
wiki_art_dir = "/home/user/01_Somnarak_Wiki/assets/art/entities"
icons_dir = "/home/user/icons"

for key, data in ENTITIES_SUITE.items():
    icon_name = f"{key}-icon.svg"
    prof_name = f"{key}-profile.svg"
    
    with open(f"{wiki_art_dir}/{icon_name}", 'w', encoding='utf-8') as f:
        f.write(data['icon'].strip())
    with open(f"{wiki_art_dir}/{prof_name}", 'w', encoding='utf-8') as f:
        f.write(data['profile'].strip())
        
    with open(f"{icons_dir}/{icon_name}", 'w', encoding='utf-8') as f:
        f.write(data['icon'].strip())
    with open(f"{icons_dir}/{prof_name}", 'w', encoding='utf-8') as f:
        f.write(data['profile'].strip())
        
    print(f"Synchronized Icon & Profile for {key.upper()} with identical matching silhouette!")

print("SUCCESS: All 13 Sorrow Entities now possess 100% synchronized, appearance+tale accurate Icon & Profile vector art!")
