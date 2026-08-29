import os

# 13 TRULY BESPOKE, DISTINCT, APPEARANCE-ACCURATE VECTOR ICONS
ENTITY_ICONS_SVG = {
    # SE-001: The Orphaned Bell (Arched Cathedral Bell Tower + Weeping Cyan Tears + Bronze Clapper)
    'se-001-icon.svg': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="se1-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#020617" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="se1-bronze" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="50%" stop-color="#b45309"/>
      <stop offset="100%" stop-color="#78350f"/>
    </linearGradient>
  </defs>
  <!-- Background Glow -->
  <circle cx="60" cy="60" r="56" fill="#040d1a" stroke="#38bdf8" stroke-width="2.5"/>
  <circle cx="60" cy="60" r="50" fill="url(#se1-glow)"/>
  
  <!-- Cathedral Arch Frame -->
  <path d="M 30,105 L 30,45 Q 60,10 90,45 L 90,105 Z" fill="#0b1329" stroke="#38bdf8" stroke-width="2" opacity="0.8"/>
  
  <!-- Acoustic Wave Rings -->
  <path d="M 22,60 A 38,38 0 0,1 98,60" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3" opacity="0.6"/>
  <path d="M 14,60 A 46,46 0 0,1 106,60" fill="none" stroke="#38bdf8" stroke-width="1" stroke-dasharray="2,4" opacity="0.4"/>
  
  <!-- Support Chain Links -->
  <rect x="57" y="16" width="6" height="12" rx="3" fill="none" stroke="#94a3b8" stroke-width="2"/>
  <rect x="57" y="24" width="6" height="12" rx="3" fill="none" stroke="#f1df76" stroke-width="2"/>
  
  <!-- Bronze Bell Body -->
  <path d="M 60,32 C 45,32 40,55 36,75 C 34,85 30,88 28,90 L 92,90 C 90,88 86,85 84,75 C 80,55 75,32 60,32 Z" fill="url(#se1-bronze)" stroke="#f1df76" stroke-width="2"/>
  
  <!-- Bell Rim Lip -->
  <ellipse cx="60" cy="90" rx="32" ry="6" fill="#78350f" stroke="#f1df76" stroke-width="2"/>
  
  <!-- Weeping Cyan Han Tears -->
  <path d="M 60,92 C 57,96 55,102 57,106 C 59,110 61,110 63,106 C 65,102 63,96 60,92 Z" fill="#38bdf8"/>
  <path d="M 44,91 C 42,94 41,98 42,101 C 43,104 45,104 46,101 C 47,98 46,94 44,91 Z" fill="#38bdf8" opacity="0.8"/>
  <path d="M 76,91 C 74,94 73,98 74,101 C 75,104 77,104 78,101 C 79,98 78,94 76,91 Z" fill="#38bdf8" opacity="0.8"/>
  
  <!-- Central Swinging Clapper -->
  <circle cx="60" cy="92" r="5" fill="#f1df76" stroke="#b45309" stroke-width="1.5"/>
  
  <!-- Ancient Inscription Band -->
  <path d="M 39,66 Q 60,72 81,66" fill="none" stroke="#f1df76" stroke-width="1.5"/>
</svg>""",

    # SE-002: The Grieving Colossus (Basalt Monolith + Weeping Cracked Mask + Jagged Crags)
    'se-002-icon.svg': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="se2-basalt" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#334155"/>
      <stop offset="50%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <radialGradient id="se2-crimson" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ef4444" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#450a0a" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <!-- Basalt Polygonal Frame -->
  <polygon points="60,6 110,24 114,94 60,114 6,94 10,24" fill="#140608" stroke="#ef5b55" stroke-width="3"/>
  <polygon points="60,12 104,28 108,90 60,108 12,90 16,28" fill="url(#se2-basalt)" stroke="#7f1d1d" stroke-width="1.5"/>
  <circle cx="60" cy="58" r="42" fill="url(#se2-crimson)"/>
  
  <!-- Colossus Cragged Shoulders -->
  <polygon points="20,40 38,24 50,34 32,54" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
  <polygon points="100,40 82,24 70,34 88,54" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
  
  <!-- Giant Weeping Mask -->
  <path d="M 40,32 L 80,32 L 76,82 L 60,94 L 44,82 Z" fill="#0f172a" stroke="#ef5b55" stroke-width="2.5"/>
  
  <!-- Deep Facial Fissure Cracks -->
  <path d="M 60,32 L 58,48 L 64,56 L 56,72 L 60,94" fill="none" stroke="#ef4444" stroke-width="2"/>
  <path d="M 58,48 L 44,52" fill="none" stroke="#ef4444" stroke-width="1.5"/>
  <path d="M 64,56 L 76,60" fill="none" stroke="#ef4444" stroke-width="1.5"/>
  
  <!-- Weeping Eye Slits -->
  <line x1="46" y1="46" x2="54" y2="46" stroke="#fca5a5" stroke-width="3" stroke-linecap="round"/>
  <line x1="66" y1="46" x2="74" y2="46" stroke="#fca5a5" stroke-width="3" stroke-linecap="round"/>
  
  <!-- Boiling Crimson Sludge Streams -->
  <path d="M 50,49 L 48,78 L 46,92" fill="none" stroke="#ef4444" stroke-width="2.5"/>
  <path d="M 70,49 L 72,78 L 74,92" fill="none" stroke="#ef4444" stroke-width="2.5"/>
  
  <!-- Seismic Shockwave Baseline -->
  <polyline points="26,102 36,98 46,104 60,96 74,104 84,98 94,102" fill="none" stroke="#f1df76" stroke-width="2"/>
</svg>""",

    # SE-003: The Thread of Memory (Azure Spindle Loom + Radiant Needles + Weft Webs)
    'se-003-icon.svg': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="se3-azure" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="50%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
  </defs>
  <!-- Diamond / Lozenge Frame -->
  <polygon points="60,6 114,60 60,114 6,60" fill="#051329" stroke="#38bdf8" stroke-width="2.5"/>
  <polygon points="60,14 106,60 60,106 14,60" fill="#020817" stroke="#f1df76" stroke-width="1.5"/>
  
  <!-- Radiating Memory Threads -->
  <line x1="60" y1="14" x2="60" y2="106" stroke="#38bdf8" stroke-width="1" stroke-dasharray="3,3" opacity="0.7"/>
  <line x1="14" y1="60" x2="106" y2="60" stroke="#38bdf8" stroke-width="1" stroke-dasharray="3,3" opacity="0.7"/>
  <circle cx="60" cy="60" r="38" fill="none" stroke="#0ea5e9" stroke-width="1" opacity="0.4"/>
  <circle cx="60" cy="60" r="26" fill="none" stroke="#38bdf8" stroke-width="1.5" opacity="0.6"/>
  
  <!-- Crossed Crystal Needles -->
  <line x1="26" y1="26" x2="94" y2="94" stroke="#f8fafc" stroke-width="2.5" stroke-linecap="round"/>
  <circle cx="28" cy="28" r="3" fill="#38bdf8"/>
  <line x1="94" y1="26" x2="26" y2="94" stroke="#f8fafc" stroke-width="2.5" stroke-linecap="round"/>
  <circle cx="92" cy="28" r="3" fill="#38bdf8"/>
  
  <!-- Central Floating Spindle -->
  <polygon points="60,34 72,60 60,86 48,60" fill="url(#se3-azure)" stroke="#f8fafc" stroke-width="2"/>
  <ellipse cx="60" cy="60" rx="6" ry="14" fill="#bae6fd"/>
  
  <!-- Woven Gossamer Thread Coils -->
  <path d="M 46,50 Q 60,42 74,50 Q 60,58 46,50" fill="none" stroke="#f1df76" stroke-width="1.5"/>
  <path d="M 46,70 Q 60,62 74,70 Q 60,78 46,70" fill="none" stroke="#f1df76" stroke-width="1.5"/>
</svg>""",

    # SE-004: The Rust-Bleeding Sentry (Fortified Octagonal Bastion + Visor Slits + Rust Halberd)
    'se-004-icon.svg': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="se4-rust" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ea580c"/>
      <stop offset="50%" stop-color="#9a3412"/>
      <stop offset="100%" stop-color="#431407"/>
    </linearGradient>
  </defs>
  <!-- Octagonal Iron Fortification Frame -->
  <polygon points="38,8 82,8 112,38 112,82 82,112 38,112 8,82 8,38" fill="#1c0a04" stroke="#ea580c" stroke-width="3"/>
  <polygon points="40,14 80,14 106,40 106,80 80,106 40,106 14,80 14,40" fill="#0f0502" stroke="#475569" stroke-width="2"/>
  
  <!-- Rivets around border -->
  <circle cx="38" cy="11" r="2" fill="#94a3b8"/><circle cx="82" cy="11" r="2" fill="#94a3b8"/>
  <circle cx="109" cy="38" r="2" fill="#94a3b8"/><circle cx="109" cy="82" r="2" fill="#94a3b8"/>
  <circle cx="82" cy="109" r="2" fill="#94a3b8"/><circle cx="38" cy="109" r="2" fill="#94a3b8"/>
  <circle cx="11" cy="82" r="2" fill="#94a3b8"/><circle cx="11" cy="38" r="2" fill="#94a3b8"/>
  
  <!-- Crossed Rust Halberds -->
  <line x1="20" y1="20" x2="100" y2="100" stroke="#64748b" stroke-width="3"/>
  <path d="M 20,20 L 32,16 L 28,32 Z" fill="#ea580c" stroke="#f97316" stroke-width="1"/>
  <line x1="100" y1="20" x2="20" y2="100" stroke="#64748b" stroke-width="3"/>
  <path d="M 100,20 L 88,16 L 92,32 Z" fill="#ea580c" stroke="#f97316" stroke-width="1"/>
  
  <!-- Automaton Helm -->
  <path d="M 38,40 L 82,40 L 78,82 L 60,94 L 42,82 Z" fill="url(#se4-rust)" stroke="#f97316" stroke-width="2"/>
  
  <!-- Horizontal Visor Slit -->
  <rect x="44" y="52" width="32" height="6" fill="#0f172a" stroke="#f97316" stroke-width="1.5"/>
  <circle cx="52" cy="55" r="2" fill="#ef4444"/>
  <circle cx="68" cy="55" r="2" fill="#ef4444"/>
  
  <!-- Corrosive Rust Drops Streaming from Visor -->
  <path d="M 52,58 L 50,78 L 48,88" fill="none" stroke="#ea580c" stroke-width="2" stroke-linecap="round"/>
  <path d="M 68,58 L 70,78 L 72,88" fill="none" stroke="#ea580c" stroke-width="2" stroke-linecap="round"/>
</svg>""",

    # SE-005: The Smothering Mother (Cameo Teardrop Medallion + Velvet Swaddles + Porcelain Effigy)
    'se-005-icon.svg': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="se5-gold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="50%" stop-color="#eab308"/>
      <stop offset="100%" stop-color="#854d0e"/>
    </linearGradient>
    <linearGradient id="se5-porcelain" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#cbd5e1"/>
    </linearGradient>
  </defs>
  <!-- Teardrop Cameo Medallion Frame -->
  <path d="M 60,6 C 92,6 112,38 112,74 C 112,98 88,114 60,114 C 32,114 8,98 8,74 C 8,38 28,6 60,6 Z" fill="#0c0a14" stroke="url(#se5-gold)" stroke-width="3"/>
  <path d="M 60,12 C 86,12 104,40 104,72 C 104,94 84,108 60,108 C 36,108 16,94 16,72 C 16,40 34,12 60,12 Z" fill="#030712" stroke="#f1df76" stroke-width="1"/>
  
  <!-- Velvet Swaddling Ribbons Intertwined -->
  <path d="M 24,70 C 40,50 80,90 96,70" fill="none" stroke="#475569" stroke-width="4"/>
  <path d="M 24,82 C 40,62 80,102 96,82" fill="none" stroke="#1e293b" stroke-width="5"/>
  
  <!-- Hooded Porcelain Mother Head -->
  <path d="M 44,48 C 44,30 76,30 76,48 C 76,64 44,64 44,48 Z" fill="url(#se5-porcelain)" stroke="#f1df76" stroke-width="1.5"/>
  
  <!-- Serene Weeping Closed Eyes -->
  <path d="M 50,46 Q 54,50 58,46" fill="none" stroke="#64748b" stroke-width="1.5"/>
  <path d="M 62,46 Q 66,50 70,46" fill="none" stroke="#64748b" stroke-width="1.5"/>
  
  <!-- Maternal Porcelain Halo -->
  <circle cx="60" cy="46" r="22" fill="none" stroke="#f1df76" stroke-width="1.5" stroke-dasharray="4,2"/>
  
  <!-- Gilded Central Clasp at Chest -->
  <polygon points="60,68 68,76 60,84 52,76" fill="url(#se5-gold)" stroke="#ffffff" stroke-width="1"/>
  <circle cx="60" cy="76" r="3" fill="#38bdf8"/>
</svg>""",

    # SE-006: The Siphon Leech (Biohazard Vortex Turbine + Annelid Siphon Rings)
    'se-006-icon.svg': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="se6-green" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="60%" stop-color="#047857"/>
      <stop offset="100%" stop-color="#022c22"/>
    </radialGradient>
  </defs>
  <!-- Circular Turbine Frame -->
  <circle cx="60" cy="60" r="54" fill="#021f18" stroke="#10b981" stroke-width="3"/>
  <circle cx="60" cy="60" r="48" fill="#01140f" stroke="#059669" stroke-width="1.5"/>
  
  <!-- Toxic Siphon Chamber -->
  <circle cx="60" cy="60" r="38" fill="url(#se6-green)"/>
  
  <!-- Concentric Toothed Leech Mouth -->
  <circle cx="60" cy="60" r="26" fill="#022c22" stroke="#6ee7b7" stroke-width="2"/>
  <circle cx="60" cy="60" r="16" fill="#01140f" stroke="#a7f3d0" stroke-width="1.5"/>
  <circle cx="60" cy="60" r="6" fill="#000000"/>
  
  <!-- Barbed Suction Teeth (Radiating Points) -->
  <polygon points="60,34 58,40 62,40" fill="#f8fafc"/>
  <polygon points="60,86 58,80 62,80" fill="#f8fafc"/>
  <polygon points="34,60 40,58 40,62" fill="#f8fafc"/>
  <polygon points="86,60 80,58 80,62" fill="#f8fafc"/>
  <polygon points="42,42 47,46 45,49" fill="#f8fafc"/>
  <polygon points="78,78 73,74 75,71" fill="#f8fafc"/>
  <polygon points="78,42 74,47 71,45" fill="#f8fafc"/>
  <polygon points="42,78 46,73 49,75" fill="#f8fafc"/>
  
  <!-- Siphon Flow Pumps (Curved Chevrons) -->
  <path d="M 22,36 Q 36,24 50,22" fill="none" stroke="#34d399" stroke-width="2"/>
  <path d="M 98,84 Q 84,96 70,98" fill="none" stroke="#34d399" stroke-width="2"/>
</svg>""",

    # SE-007: Brume / Ashen Scribe (Archival Basalt Tablet + Obsidian Quill + Particulate Fog)
    'se-007-icon.svg': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="se7-slate" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#475569"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <!-- Rounded Tablet Outline -->
  <rect x="10" y="8" width="100" height="104" rx="14" fill="#070c14" stroke="#94a3b8" stroke-width="2.5"/>
  <rect x="16" y="14" width="88" height="92" rx="10" fill="url(#se7-slate)" stroke="#38bdf8" stroke-width="1.5"/>
  
  <!-- Swirling Ash Clouds / Fog Scrolls -->
  <path d="M 16,35 C 35,25 45,45 65,30 C 85,15 95,35 104,28" fill="none" stroke="#cbd5e1" stroke-width="2" opacity="0.6"/>
  <path d="M 16,85 C 35,75 45,95 65,80 C 85,65 95,85 104,78" fill="none" stroke="#cbd5e1" stroke-width="2" opacity="0.6"/>
  
  <!-- Basalt Tablet with Carved Names -->
  <rect x="34" y="30" width="52" height="60" rx="4" fill="#020617" stroke="#64748b" stroke-width="1.5"/>
  <line x1="42" y1="42" x2="78" y2="42" stroke="#38bdf8" stroke-width="1.5"/>
  <line x1="42" y1="52" x2="74" y2="52" stroke="#38bdf8" stroke-width="1.5"/>
  <line x1="42" y1="62" x2="70" y2="62" stroke="#38bdf8" stroke-width="1.5"/>
  <line x1="42" y1="72" x2="64" y2="72" stroke="#38bdf8" stroke-width="1.5"/>
  
  <!-- Diagonal Obsidian Quill Stylus -->
  <line x1="84" y1="24" x2="56" y2="76" stroke="#f1df76" stroke-width="3" stroke-linecap="round"/>
  <polygon points="56,76 52,82 59,79" fill="#f8fafc"/>
  
  <!-- Crumbling Ash Particles -->
  <circle cx="78" cy="74" r="1.5" fill="#94a3b8"/><circle cx="84" cy="68" r="2" fill="#94a3b8"/>
  <circle cx="82" cy="82" r="1.5" fill="#94a3b8"/><circle cx="88" cy="78" r="1" fill="#94a3b8"/>
</svg>""",

    # SE-008: The Iron Maiden of Regret (Gothic Reliquary Arch + Spike Lattice + Crown of Thorns)
    'se-008-icon.svg': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="se8-crimson" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444"/>
      <stop offset="100%" stop-color="#7f1d1d"/>
    </linearGradient>
  </defs>
  <!-- Pointed Gothic Reliquary Frame -->
  <path d="M 60,4 L 106,30 L 106,112 L 14,112 L 14,30 Z" fill="#170307" stroke="#ef4444" stroke-width="3"/>
  <path d="M 60,12 L 98,34 L 98,104 L 22,104 L 22,34 Z" fill="#090103" stroke="#991b1b" stroke-width="1.5"/>
  
  <!-- Crown of Thorns Header -->
  <ellipse cx="60" cy="30" rx="20" ry="6" fill="none" stroke="#ef4444" stroke-width="2"/>
  <line x1="44" y1="26" x2="40" y2="20" stroke="#ef4444" stroke-width="2"/>
  <line x1="54" y1="24" x2="52" y2="18" stroke="#ef4444" stroke-width="2"/>
  <line x1="66" y1="24" x2="68" y2="18" stroke="#ef4444" stroke-width="2"/>
  <line x1="76" y1="26" x2="80" y2="20" stroke="#ef4444" stroke-width="2"/>
  
  <!-- Iron Sarcophagus Body (Half Open) -->
  <rect x="36" y="40" width="48" height="60" rx="4" fill="#1e293b" stroke="#f1df76" stroke-width="1.5"/>
  
  <!-- Interior Barbed Spikes -->
  <line x1="42" y1="48" x2="56" y2="52" stroke="#ef4444" stroke-width="2"/>
  <line x1="42" y1="60" x2="58" y2="62" stroke="#ef4444" stroke-width="2"/>
  <line x1="42" y1="72" x2="56" y2="74" stroke="#ef4444" stroke-width="2"/>
  <line x1="42" y1="84" x2="54" y2="86" stroke="#ef4444" stroke-width="2"/>
  
  <line x1="78" y1="48" x2="64" y2="52" stroke="#ef4444" stroke-width="2"/>
  <line x1="78" y1="60" x2="62" y2="62" stroke="#ef4444" stroke-width="2"/>
  <line x1="78" y1="72" x2="64" y2="74" stroke="#ef4444" stroke-width="2"/>
  <line x1="78" y1="84" x2="66" y2="86" stroke="#ef4444" stroke-width="2"/>
  
  <!-- Center Crying Effigy Slit -->
  <line x1="60" y1="44" x2="60" y2="92" stroke="#f87171" stroke-width="1.5" stroke-dasharray="2,2"/>
</svg>""",

    # SE-009: The Memory Weaver / Drowned Bell (Bolted Diving Porthole + Submerged Bell + Sonar Waves)
    'se-009-icon.svg': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="se9-ocean" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="70%" stop-color="#0369a1"/>
      <stop offset="100%" stop-color="#082f49"/>
    </radialGradient>
  </defs>
  <!-- Bolted Submersible Porthole Frame -->
  <circle cx="60" cy="60" r="54" fill="#04121e" stroke="#0284c7" stroke-width="3"/>
  <circle cx="60" cy="60" r="46" fill="url(#se9-ocean)" stroke="#ca8a04" stroke-width="2.5"/>
  
  <!-- Porthole Bolts (8 surrounding bolts) -->
  <circle cx="60" cy="10" r="2.5" fill="#f1df76"/><circle cx="60" cy="110" r="2.5" fill="#f1df76"/>
  <circle cx="10" cy="60" r="2.5" fill="#f1df76"/><circle cx="110" cy="60" r="2.5" fill="#f1df76"/>
  <circle cx="25" cy="25" r="2.5" fill="#f1df76"/><circle cx="95" cy="95" r="2.5" fill="#f1df76"/>
  <circle cx="95" cy="25" r="2.5" fill="#f1df76"/><circle cx="25" cy="95" r="2.5" fill="#f1df76"/>
  
  <!-- Submerged Bronze Bell -->
  <path d="M 60,34 C 50,34 46,48 42,62 C 40,70 38,72 36,74 L 84,74 C 82,72 80,70 78,62 C 74,48 70,34 60,34 Z" fill="#b45309" stroke="#f1df76" stroke-width="1.5"/>
  <ellipse cx="60" cy="74" rx="24" ry="4" fill="#78350f" stroke="#f1df76" stroke-width="1.5"/>
  
  <!-- Underwater Sonar Rings -->
  <circle cx="60" cy="74" r="16" fill="none" stroke="#7dd3fc" stroke-width="1" stroke-dasharray="2,3" opacity="0.8"/>
  <circle cx="60" cy="74" r="28" fill="none" stroke="#7dd3fc" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
  
  <!-- Rising Aquatic Bubbles -->
  <circle cx="44" cy="42" r="2" fill="#e0f2fe" opacity="0.7"/>
  <circle cx="48" cy="30" r="3" fill="#e0f2fe" opacity="0.6"/>
  <circle cx="76" cy="46" r="2.5" fill="#e0f2fe" opacity="0.7"/>
  <circle cx="72" cy="34" r="1.5" fill="#e0f2fe" opacity="0.8"/>
</svg>""",

    # SE-010: The Convergence (12-Pointed Singularity Star + Interwoven Spiked Crowns + Void Eye)
    'se-010-icon.svg': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="se10-void" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="30%" stop-color="#c7d2fe"/>
      <stop offset="70%" stop-color="#312e81"/>
      <stop offset="100%" stop-color="#020617"/>
    </radialGradient>
  </defs>
  <!-- Background Deep Void Disc -->
  <circle cx="60" cy="60" r="56" fill="#050314" stroke="#e0e7ff" stroke-width="2.5"/>
  
  <!-- 12-Pointed Radiant Singularity Star -->
  <polygon points="60,6 66,42 98,22 78,54 114,60 78,66 98,98 66,78 60,114 54,78 22,98 42,66 6,60 42,54 22,22 54,42" fill="none" stroke="#818cf8" stroke-width="1.5"/>
  
  <!-- Concentric Spiked Crowns -->
  <circle cx="60" cy="60" r="34" fill="url(#se10-void)" stroke="#ffffff" stroke-width="2"/>
  
  <!-- Gravitational Warping Rays -->
  <circle cx="60" cy="60" r="22" fill="#000000" stroke="#f1df76" stroke-width="2"/>
  
  <!-- Central All-Seeing Void Eye -->
  <ellipse cx="60" cy="60" rx="14" ry="7" fill="#ffffff"/>
  <circle cx="60" cy="60" r="4.5" fill="#000000"/>
  <circle cx="62" cy="58" r="1.5" fill="#38bdf8"/>
</svg>""",

    # SE-011: The Whispering Walls (Crenelated Labyrinth Fortress + 3 Whispering Relief Faces)
    'se-011-icon.svg': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="se11-lead" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#475569"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
  </defs>
  <!-- Crenelated Fortress Labyrinth Shield -->
  <polygon points="20,10 40,10 40,18 60,18 60,10 80,10 80,18 100,18 100,10 108,18 108,86 60,114 12,86 12,18" fill="#0b0f19" stroke="#ef4444" stroke-width="2.5"/>
  
  <!-- Interlocking Lead Tiles Grid -->
  <rect x="22" y="26" width="76" height="68" fill="url(#se11-lead)" stroke="#38bdf8" stroke-width="1.5"/>
  <line x1="22" y1="48" x2="98" y2="48" stroke="#334155" stroke-width="1.5"/>
  <line x1="22" y1="70" x2="98" y2="70" stroke="#334155" stroke-width="1.5"/>
  <line x1="47" y1="26" x2="47" y2="94" stroke="#334155" stroke-width="1.5"/>
  <line x1="73" y1="26" x2="73" y2="94" stroke="#334155" stroke-width="1.5"/>
  
  <!-- Three Sculpted Whispering Faces -->
  <!-- Face 1 (Top Center) -->
  <ellipse cx="60" cy="37" rx="6" ry="7" fill="#0f172a" stroke="#cbd5e1" stroke-width="1"/>
  <ellipse cx="60" cy="40" rx="2" ry="3" fill="#ef4444"/>
  <!-- Face 2 (Bottom Left) -->
  <ellipse cx="35" cy="59" rx="6" ry="7" fill="#0f172a" stroke="#cbd5e1" stroke-width="1"/>
  <ellipse cx="35" cy="62" rx="2" ry="3" fill="#ef4444"/>
  <!-- Face 3 (Bottom Right) -->
  <ellipse cx="85" cy="59" rx="6" ry="7" fill="#0f172a" stroke="#cbd5e1" stroke-width="1"/>
  <ellipse cx="85" cy="62" rx="2" ry="3" fill="#ef4444"/>
  
  <!-- Radiating Whispering Acoustic Waves -->
  <path d="M 46,37 Q 50,32 54,37" fill="none" stroke="#38bdf8" stroke-width="1"/>
  <path d="M 66,37 Q 70,32 74,37" fill="none" stroke="#38bdf8" stroke-width="1"/>
</svg>""",

    # SE-014: The Debt Eater (Imperial Square-Cut Coin Seal + Vested Beast Jaw + Swallowed Ledger)
    'se-014-icon.svg': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="se14-gold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="50%" stop-color="#eab308"/>
      <stop offset="100%" stop-color="#713f12"/>
    </linearGradient>
  </defs>
  <!-- Ancient Cheonbulok Coin Frame (Circle with Square Hole Rim) -->
  <circle cx="60" cy="60" r="54" fill="#140d04" stroke="url(#se14-gold)" stroke-width="3"/>
  <circle cx="60" cy="60" r="46" fill="#0a0501" stroke="#ca8a04" stroke-width="1.5"/>
  
  <!-- Four Archival Coin Stamps -->
  <rect x="54" y="16" width="12" height="6" fill="#eab308"/>
  <rect x="54" y="98" width="12" height="6" fill="#eab308"/>
  <rect x="16" y="54" width="6" height="12" fill="#eab308"/>
  <rect x="98" y="54" width="6" height="12" fill="#eab308"/>
  
  <!-- Devouring Beast Jaw -->
  <path d="M 28,42 Q 60,20 92,42 Q 96,68 92,82 Q 60,98 28,82 Z" fill="#18181b" stroke="#f1df76" stroke-width="2"/>
  
  <!-- Sharp Gold Teeth Rows -->
  <polygon points="34,46 38,54 42,46" fill="#fef08a"/>
  <polygon points="46,44 50,54 54,44" fill="#fef08a"/>
  <polygon points="58,44 62,54 66,44" fill="#fef08a"/>
  <polygon points="70,44 74,54 78,44" fill="#fef08a"/>
  <polygon points="82,46 86,54 90,46" fill="#fef08a"/>
  
  <polygon points="38,78 42,70 46,78" fill="#fef08a"/>
  <polygon points="50,80 54,70 58,80" fill="#fef08a"/>
  <polygon points="62,80 66,70 70,80" fill="#fef08a"/>
  <polygon points="74,78 78,70 82,78" fill="#fef08a"/>
  
  <!-- Swallowed Open Debt Ledger Book in Throat -->
  <polygon points="46,58 60,54 74,58 74,68 60,64 46,68" fill="#f8fafc" stroke="#94a3b8" stroke-width="1"/>
  <line x1="60" y1="54" x2="60" y2="64" stroke="#ef4444" stroke-width="1.5"/>
</svg>""",

    # SE-015: The Debt Scale (Sovereign Sword Fulcrum + Balanced Crystal Pans + Sovereign Crown)
    'se-015-icon.svg': """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <linearGradient id="se15-sovereign" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="50%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#1e3a8a"/>
    </linearGradient>
  </defs>
  <!-- Diamond Balance Pediment Frame -->
  <polygon points="60,4 114,60 60,116 6,60" fill="#060814" stroke="#f8fafc" stroke-width="2.5"/>
  <polygon points="60,12 106,60 60,108 14,60" fill="#02040a" stroke="#f1df76" stroke-width="1.5"/>
  
  <!-- Sovereign Crown at Apex -->
  <polygon points="50,18 55,14 60,18 65,14 70,18 68,24 52,24" fill="#f1df76" stroke="#ffffff" stroke-width="1"/>
  
  <!-- Central Sovereign Sword Fulcrum -->
  <line x1="60" y1="24" x2="60" y2="98" stroke="#f8fafc" stroke-width="3" stroke-linecap="round"/>
  <polygon points="60,104 56,96 64,96" fill="#f8fafc"/>
  
  <!-- Horizontal Balance Beam -->
  <line x1="26" y1="38" x2="94" y2="38" stroke="#f1df76" stroke-width="3" stroke-linecap="round"/>
  <circle cx="60" cy="38" r="4" fill="#38bdf8" stroke="#ffffff" stroke-width="1.5"/>
  
  <!-- Left Scale Pan (Weeping Remorse Heart) -->
  <line x1="30" y1="38" x2="22" y2="68" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="30" y1="38" x2="38" y2="68" stroke="#94a3b8" stroke-width="1.5"/>
  <path d="M 18,68 Q 30,76 42,68 Z" fill="url(#se15-sovereign)" stroke="#f1df76" stroke-width="1.5"/>
  <!-- Weeping Tear -->
  <circle cx="30" cy="62" r="3.5" fill="#ef4444"/>
  
  <!-- Right Scale Pan (Lead Law Slates) -->
  <line x1="90" y1="38" x2="82" y2="68" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="90" y1="38" x2="98" y2="68" stroke="#94a3b8" stroke-width="1.5"/>
  <path d="M 78,68 Q 90,76 102,68 Z" fill="url(#se15-sovereign)" stroke="#f1df76" stroke-width="1.5"/>
  <!-- Lead Weight Block -->
  <rect x="85" y="58" width="10" height="7" fill="#64748b" stroke="#f8fafc" stroke-width="1"/>
</svg>"""
}

# Write to both /01_Somnarak_Wiki/assets/art/entities/ and /icons/
for fname, svg_content in ENTITY_ICONS_SVG.items():
    p1 = f"/home/user/01_Somnarak_Wiki/assets/art/entities/{fname}"
    p2 = f"/home/user/icons/{fname}"
    with open(p1, 'w', encoding='utf-8') as f:
        f.write(svg_content.strip())
    with open(p2, 'w', encoding='utf-8') as f:
        f.write(svg_content.strip())
    print(f"Wrote bespoke vector icon: {fname}")

print("SUCCESS: Generated all 13 completely unique and bespoke entity vector icons!")
