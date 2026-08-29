#!/usr/bin/env python3
"""
tools/build_all_rich_lore_mech_icons.py
Builds personalized, high-detail vector SVG icons for Lore and Mechanics.
"""

import os

WIKI_ASSETS_ICONS = "/home/user/01_Somnarak_Wiki/assets/icons"
WORKSPACE_ICONS = "/home/user/icons"

def get_lore_icons():
    return {
        # Absolvohan - 9 Sacred Purification Tablets & Cleansing Fire
        "icon_lore_absolvohan.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="absGlow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#f1df76" stop-opacity="0.9"/>
      <stop offset="50%" stop-color="#ef5b55" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#070a12" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#f1df76" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="52" r="38" fill="url(#absGlow)"/>

  <!-- Stele Tablet -->
  <rect x="40" y="24" width="40" height="60" rx="4" fill="#1c1917" stroke="#f1df76" stroke-width="2"/>
  
  <!-- 9 Sacred Inscribed Runes/Lines (3x3 grid) -->
  <circle cx="48" cy="36" r="2.5" fill="#fef08a"/>
  <circle cx="60" cy="36" r="2.5" fill="#fef08a"/>
  <circle cx="72" cy="36" r="2.5" fill="#fef08a"/>
  
  <circle cx="48" cy="50" r="2.5" fill="#fef08a"/>
  <circle cx="60" cy="50" r="2.5" fill="#ef5b55"/>
  <circle cx="72" cy="50" r="2.5" fill="#fef08a"/>

  <circle cx="48" cy="64" r="2.5" fill="#fef08a"/>
  <circle cx="60" cy="64" r="2.5" fill="#fef08a"/>
  <circle cx="72" cy="64" r="2.5" fill="#fef08a"/>

  <!-- Cleansing Sacred Flame Tips -->
  <path d="M 60 14 Q 68 22 60 28 Q 52 22 60 14 Z" fill="#ef5b55"/>
  <circle cx="60" cy="22" r="2" fill="#fef08a"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#1f1807" stroke="#f1df76" stroke-width="1"/>
  <text x="60" y="108.5" fill="#f1df76" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">ABSOLVOHAN</text>
</svg>""",

        # Cheongula - Subterranean Vault Gates & Chained Locks
        "icon_lore_cheongula.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="cheGlow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.6"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#38bdf8" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="52" r="38" fill="url(#cheGlow)"/>

  <!-- Massive Subterranean Iron Vault Arch -->
  <path d="M 28 88 L 28 44 Q 60 18 92 44 L 92 88 Z" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
  <line x1="60" y1="24" x2="60" y2="88" stroke="#38bdf8" stroke-width="2"/>

  <!-- Heavy Horizontal Locking Bars & Chains -->
  <rect x="32" y="48" width="56" height="8" fill="#1e293b" stroke="#f1df76" stroke-width="1.2"/>
  <rect x="32" y="66" width="56" height="8" fill="#1e293b" stroke="#f1df76" stroke-width="1.2"/>

  <!-- Center Vault Lock Dial -->
  <circle cx="60" cy="57" r="8" fill="#070a12" stroke="#f1df76" stroke-width="2"/>
  <circle cx="60" cy="57" r="3" fill="#ef5b55"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#0c192c" stroke="#38bdf8" stroke-width="1"/>
  <text x="60" y="108.5" fill="#38bdf8" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">CHEONGULA</text>
</svg>""",

        # Dawn of Hope - Golden Sunburst rising over Brutalist Bulwark
        "icon_lore_dawn_of_hope.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="dawnGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fef08a" stop-opacity="1"/>
      <stop offset="40%" stop-color="#f59e0b" stop-opacity="0.8"/>
      <stop offset="80%" stop-color="#ef4444" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#070a12" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#f1df76" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="50" r="38" fill="url(#dawnGlow)"/>

  <!-- Rising Sun and Radiant Rays -->
  <circle cx="60" cy="54" r="16" fill="#fef08a" stroke="#f59e0b" stroke-width="2"/>
  <line x1="60" y1="24" x2="60" y2="34" stroke="#fef08a" stroke-width="2"/>
  <line x1="38" y1="32" x2="46" y2="40" stroke="#fef08a" stroke-width="2"/>
  <line x1="82" y1="32" x2="74" y2="40" stroke="#fef08a" stroke-width="2"/>
  <line x1="28" y1="54" x2="38" y2="54" stroke="#fef08a" stroke-width="2"/>
  <line x1="92" y1="54" x2="82" y2="54" stroke="#fef08a" stroke-width="2"/>

  <!-- City Bulwark Silhouette in Foreground -->
  <polygon points="20,88 20,70 36,70 36,62 48,62 48,72 72,72 72,62 84,62 84,70 100,70 100,88" fill="#1c1917" stroke="#f59e0b" stroke-width="1.5"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#1f1807" stroke="#f1df76" stroke-width="1"/>
  <text x="60" y="108.5" fill="#f1df76" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">DAWN OF HOPE</text>
</svg>""",

        # Doorspeech - Frequency Audio Waveform through Containment Door Iris
        "icon_lore_doorspeech.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="doorGlow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.8"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#38bdf8" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="52" r="38" fill="url(#doorGlow)"/>

  <!-- Heavy Door Iris Circle -->
  <circle cx="60" cy="52" r="28" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="60" cy="52" r="20" fill="#070a12" stroke="#f1df76" stroke-width="1.5"/>

  <!-- Audio Waveform passing through Center -->
  <line x1="42" y1="52" x2="42" y2="52" stroke="#38bdf8" stroke-width="2" stroke-linecap="round"/>
  <line x1="46" y1="46" x2="46" y2="58" stroke="#38bdf8" stroke-width="2" stroke-linecap="round"/>
  <line x1="50" y1="40" x2="50" y2="64" stroke="#71efaf" stroke-width="2" stroke-linecap="round"/>
  <line x1="55" y1="34" x2="55" y2="70" stroke="#f1df76" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="60" y1="30" x2="60" y2="74" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>
  <line x1="65" y1="34" x2="65" y2="70" stroke="#f1df76" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="70" y1="40" x2="70" y2="64" stroke="#71efaf" stroke-width="2" stroke-linecap="round"/>
  <line x1="74" y1="46" x2="74" y2="58" stroke="#38bdf8" stroke-width="2" stroke-linecap="round"/>
  <line x1="78" y1="52" x2="78" y2="52" stroke="#38bdf8" stroke-width="2" stroke-linecap="round"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#0c192c" stroke="#38bdf8" stroke-width="1"/>
  <text x="60" y="108.5" fill="#38bdf8" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">DOORSPEECH</text>
</svg>""",

        # Dream Realm - Surreal Floating Islands & Cosmic Nebula
        "icon_lore_dream_realm.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="dreamGlow" cx="50%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#c084fc" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#38bdf8" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#070a12" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#c084fc" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="52" r="38" fill="url(#dreamGlow)"/>

  <!-- Crescent Dream Moon -->
  <path d="M 72 26 A 14 14 0 1 0 84 48 A 12 12 0 1 1 72 26 Z" fill="#fef08a"/>

  <!-- Floating Surrealist Rock Islands -->
  <polygon points="34,60 62,60 52,74 40,70" fill="#1e1b4b" stroke="#c084fc" stroke-width="1.2"/>
  <polygon points="64,48 88,48 80,62 70,58" fill="#1e1b4b" stroke="#38bdf8" stroke-width="1.2"/>

  <!-- Crystalline Spire on Floating Rock -->
  <polygon points="46,44 50,60 42,60" fill="#c084fc"/>
  <polygon points="76,36 80,48 72,48" fill="#38bdf8"/>

  <!-- Connecting Resonant Energy Bridge -->
  <path d="M 48 58 Q 63 50 76 46" fill="none" stroke="#f1df76" stroke-width="1.2" stroke-dasharray="2,2"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#1e102f" stroke="#c084fc" stroke-width="1"/>
  <text x="60" y="108.5" fill="#e879f9" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">DREAM REALM</text>
</svg>""",

        # Daily Life - District 4 Rain-Slicked Lantern & Steam
        "icon_lore_daily_life.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="lifeGlow" cx="50%" cy="40%" r="50%">
      <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.9"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#f59e0b" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="48" r="38" fill="url(#lifeGlow)"/>

  <!-- Traditional Urban Street Lantern -->
  <polygon points="60,22 74,30 46,30" fill="#292524" stroke="#f59e0b" stroke-width="1.2"/>
  <rect x="50" y="30" width="20" height="26" rx="2" fill="#78350f" stroke="#fef08a" stroke-width="1.5"/>
  <circle cx="60" cy="43" r="6" fill="#fef08a"/>
  <polygon points="60,62 72,56 48,56" fill="#292524" stroke="#f59e0b" stroke-width="1.2"/>

  <!-- Rain Streaks & Puddle Reflection -->
  <line x1="36" y1="28" x2="32" y2="44" stroke="#38bdf8" stroke-width="1" stroke-dasharray="4,4"/>
  <line x1="84" y1="32" x2="80" y2="48" stroke="#38bdf8" stroke-width="1" stroke-dasharray="4,4"/>
  <ellipse cx="60" cy="80" rx="34" ry="6" fill="#1c1917" stroke="#f59e0b" stroke-width="1"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#241403" stroke="#f59e0b" stroke-width="1"/>
  <text x="60" y="108.5" fill="#fbbf24" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">DAILY LIFE</text>
</svg>""",

        # Named Fractures - Shattered Dimensional Glass with Metal Braces
        "icon_lore_named_fractures.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="fracGlow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#ef4444" stop-opacity="0.8"/>
      <stop offset="60%" stop-color="#38bdf8" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#070a12" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#ef4444" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="52" r="38" fill="url(#fracGlow)"/>

  <!-- Shattered Mirror Planes -->
  <polygon points="34,26 62,38 48,68 28,52" fill="#1c1917" stroke="#ef4444" stroke-width="1.5"/>
  <polygon points="62,38 90,28 82,64 48,68" fill="#0c192c" stroke="#38bdf8" stroke-width="1.5"/>
  <polygon points="48,68 82,64 68,88 38,82" fill="#1c0a0a" stroke="#ef4444" stroke-width="1.5"/>

  <!-- Heavy Industrial Containment Clamps / Braces -->
  <rect x="48" y="32" width="16" height="6" rx="2" fill="#334155" stroke="#f1df76" stroke-width="1"/>
  <rect x="58" y="62" width="16" height="6" rx="2" fill="#334155" stroke="#f1df76" stroke-width="1"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#200a0a" stroke="#ef4444" stroke-width="1"/>
  <text x="60" y="108.5" fill="#ef4444" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">NAMED FRACTURES</text>
</svg>""",

        # Night Hazards - Luminous Predatory Aberration Eyes & Eclipse
        "icon_lore_night_hazards.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="hazGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ef4444" stop-opacity="0.9"/>
      <stop offset="60%" stop-color="#7f1d1d" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#070a12" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#ef4444" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="52" r="38" fill="url(#hazGlow)"/>

  <!-- Eclipsed Black Sun / Moon -->
  <circle cx="60" cy="50" r="26" fill="#070a12" stroke="#ef4444" stroke-width="2"/>
  
  <!-- Fierce Glowing Aberration Eyes in Darkness -->
  <path d="M 38 48 Q 48 42 56 48 Q 48 54 38 48 Z" fill="#ef4444"/>
  <circle cx="48" cy="48" r="2.5" fill="#ffffff"/>

  <path d="M 64 48 Q 72 42 82 48 Q 72 54 64 48 Z" fill="#ef4444"/>
  <circle cx="72" cy="48" r="2.5" fill="#ffffff"/>

  <!-- Third Center Slit Eye -->
  <ellipse cx="60" cy="34" rx="5" ry="2.5" fill="#f1df76"/>
  <circle cx="60" cy="34" r="1.2" fill="#ffffff"/>

  <!-- Nocturnal Mist Tendrils -->
  <path d="M 28 74 Q 45 66 60 72 Q 75 78 92 70" fill="none" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,2"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#200a0a" stroke="#ef4444" stroke-width="1"/>
  <text x="60" y="108.5" fill="#ef4444" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">NIGHT HAZARDS</text>
</svg>""",

        # Name Registry - Monumental Stele Etched with Golden Inscriptions
        "icon_lore_name_registry.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="regGlow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#f1df76" stop-opacity="0.8"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#f1df76" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="52" r="38" fill="url(#regGlow)"/>

  <!-- Monumental Obsidian Stele -->
  <polygon points="40,20 80,20 86,88 34,88" fill="#1c1917" stroke="#f1df76" stroke-width="2"/>

  <!-- Glowing Inscribed Name Lines -->
  <line x1="44" y1="32" x2="76" y2="32" stroke="#fef08a" stroke-width="1.5"/>
  <line x1="46" y1="42" x2="74" y2="42" stroke="#fef08a" stroke-width="1.5"/>
  <line x1="44" y1="52" x2="76" y2="52" stroke="#fef08a" stroke-width="1.5"/>
  <line x1="48" y1="62" x2="72" y2="62" stroke="#fef08a" stroke-width="1.5"/>
  <line x1="46" y1="72" x2="74" y2="72" stroke="#fef08a" stroke-width="1.5"/>

  <!-- Eternal Memorial Flame at Base -->
  <polygon points="60,78 64,86 56,86" fill="#ef5b55"/>
  <circle cx="60" cy="82" r="1.5" fill="#ffffff"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#1f1807" stroke="#f1df76" stroke-width="1"/>
  <text x="60" y="108.5" fill="#f1df76" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">NAME REGISTRY</text>
</svg>""",

        # Three Ages - Tri-Tier Chronometer (Founding, Containment, Silence)
        "icon_lore_three_ages.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="ageGlow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#f1df76" stop-opacity="0.8"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#f1df76" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="52" r="38" fill="url(#ageGlow)"/>

  <!-- Master Clockwork Chronometer -->
  <circle cx="60" cy="52" r="32" fill="#0f172a" stroke="#f1df76" stroke-width="2"/>

  <!-- 3 Epoch Sectors (120 deg each) -->
  <line x1="60" y1="52" x2="60" y2="22" stroke="#ef5b55" stroke-width="2"/>
  <line x1="60" y1="52" x2="86" y2="67" stroke="#38bdf8" stroke-width="2"/>
  <line x1="60" y1="52" x2="34" y2="67" stroke="#71efaf" stroke-width="2"/>

  <!-- Sector Badges: I, II, III -->
  <circle cx="72" cy="38" r="4" fill="#ef5b55"/>
  <circle cx="60" cy="72" r="4" fill="#38bdf8"/>
  <circle cx="48" cy="38" r="4" fill="#71efaf"/>

  <!-- Central Gear Hub -->
  <circle cx="60" cy="52" r="6" fill="#070a12" stroke="#f1df76" stroke-width="2"/>
  <circle cx="60" cy="52" r="2" fill="#ffffff"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#1f1807" stroke="#f1df76" stroke-width="1"/>
  <text x="60" y="108.5" fill="#f1df76" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">THREE AGES</text>
</svg>""",

        # Weeping River - Flowing Subterranean Toxic Cyan Torrent
        "icon_lore_weeping_effluent.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="weepGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#06b6d4" stop-opacity="0.9"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#06b6d4" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="52" r="38" fill="url(#weepGlow)"/>

  <!-- Cavern Tunnel Arch -->
  <path d="M 24 86 Q 60 18 96 86 Z" fill="#0f172a" stroke="#0891b2" stroke-width="2"/>

  <!-- Flowing Effluent River Wave Curves -->
  <path d="M 28 78 Q 44 68 60 74 Q 76 80 92 72 L 92 86 L 28 86 Z" fill="#083344" stroke="#22d3ee" stroke-width="1.5"/>
  <path d="M 32 64 Q 48 54 64 60 Q 80 66 88 58" fill="none" stroke="#67e8f9" stroke-width="2"/>
  <path d="M 38 52 Q 52 44 68 50 Q 78 54 82 48" fill="none" stroke="#a5f3fc" stroke-width="1.5"/>

  <!-- Toxic Vapor Bubbles -->
  <circle cx="48" cy="42" r="3" fill="#22d3ee"/>
  <circle cx="72" cy="38" r="2.5" fill="#67e8f9"/>
  <circle cx="60" cy="32" r="2" fill="#cffafe"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#082f49" stroke="#06b6d4" stroke-width="1"/>
  <text x="60" y="108.5" fill="#22d3ee" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">THE WEEPING</text>
</svg>"""
    }

def get_mechanics_icons():
    return {
        # Han Energy & Damage Matrix - 4-Quadrant Elemental Diamond
        "icon_mech_han_energy_damage.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#ef4444" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>

  <!-- 4-Quadrant Diamond Matrix -->
  <!-- Top: Grudge (Crimson Red) -->
  <polygon points="60,20 86,46 60,46" fill="#dc2626" stroke="#fca5a5" stroke-width="1"/>
  <polygon points="60,20 34,46 60,46" fill="#991b1b" stroke="#fca5a5" stroke-width="1"/>
  
  <!-- Right: Lament (Cyan Blue) -->
  <polygon points="86,46 60,46 60,72" fill="#0284c7" stroke="#7dd3fc" stroke-width="1"/>
  <polygon points="86,46 60,72 86,72" fill="#0369a1" stroke="#7dd3fc" stroke-width="1"/>

  <!-- Bottom: Void (Gold Yellow) -->
  <polygon points="60,72 86,72 60,98" fill="#d97706" stroke="#fef08a" stroke-width="1"/>
  <polygon points="60,72 34,72 60,98" fill="#b45309" stroke="#fef08a" stroke-width="1"/>

  <!-- Left: Pale (White / Gray) -->
  <polygon points="34,46 60,46 60,72" fill="#64748b" stroke="#e2e8f0" stroke-width="1"/>
  <polygon points="34,46 60,72 34,72" fill="#475569" stroke="#e2e8f0" stroke-width="1"/>

  <!-- Center Pivot Core -->
  <circle cx="60" cy="59" r="8" fill="#070a12" stroke="#ffffff" stroke-width="2"/>
  <circle cx="60" cy="59" r="3" fill="#ffffff"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#1c0a0a" stroke="#ef4444" stroke-width="1"/>
  <text x="60" y="108.5" fill="#ef4444" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">DAMAGE MATRIX</text>
</svg>""",

        # Four Work Types - 4 Tactical Operation Modules
        "icon_mech_four_work_types.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#38bdf8" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>

  <!-- 4 Work Module Quadrants -->
  <!-- 1. Observation (Top Left - Red Eye) -->
  <rect x="22" y="22" width="34" height="34" rx="4" fill="#1c0a0a" stroke="#ef4444" stroke-width="1.5"/>
  <ellipse cx="39" cy="39" rx="10" ry="6" fill="none" stroke="#ef4444" stroke-width="1.5"/>
  <circle cx="39" cy="39" r="3" fill="#ef4444"/>

  <!-- 2. Extraction (Top Right - Cyan Flask) -->
  <rect x="64" y="22" width="34" height="34" rx="4" fill="#0c192c" stroke="#38bdf8" stroke-width="1.5"/>
  <polygon points="76,30 86,30 84,48 78,48" fill="#0284c7" stroke="#38bdf8" stroke-width="1.2"/>
  <circle cx="81" cy="42" r="2" fill="#ffffff"/>

  <!-- 3. Insight (Bottom Left - Green Gear) -->
  <rect x="22" y="60" width="34" height="34" rx="4" fill="#062e22" stroke="#10b981" stroke-width="1.5"/>
  <circle cx="39" cy="77" r="7" fill="none" stroke="#10b981" stroke-width="2"/>
  <circle cx="39" cy="77" r="2.5" fill="#71efaf"/>

  <!-- 4. Restraint (Bottom Right - Gold Chain) -->
  <rect x="64" y="60" width="34" height="34" rx="4" fill="#1f1807" stroke="#f1df76" stroke-width="1.5"/>
  <ellipse cx="81" cy="77" rx="8" ry="4" fill="none" stroke="#f1df76" stroke-width="2"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#0c192c" stroke="#38bdf8" stroke-width="1"/>
  <text x="60" y="108.5" fill="#38bdf8" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">FOUR WORK TYPES</text>
</svg>""",

        # SECC Classification - 5-Tier Risk Shield & Hazard Crown
        "icon_mech_secc_classification.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#ef4444" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>

  <!-- Outer Threat Shield -->
  <path d="M 32 24 L 88 24 L 88 56 Q 88 86 60 92 Q 32 86 32 56 Z" fill="#1c0a0a" stroke="#ef4444" stroke-width="2"/>
  
  <!-- Tier Hazard Crown -->
  <polygon points="40,32 48,22 60,30 72,22 80,32" fill="none" stroke="#f1df76" stroke-width="2"/>

  <!-- Roman / Korean Risk Grade Inscription -->
  <circle cx="60" cy="56" r="16" fill="#7f1d1d" stroke="#fca5a5" stroke-width="1.5"/>
  <text x="60" y="62" fill="#ffffff" font-family="Impact, Arial" font-size="16" font-weight="bold" text-anchor="middle">SECC</text>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#200a0a" stroke="#ef4444" stroke-width="1"/>
  <text x="60" y="108.5" fill="#ef4444" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">SECC THREAT TIER</text>
</svg>""",

        # Resonant Clash - Crossed Kinetic Energy Blades & Shockwave
        "icon_mech_resonant_clash.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="clashGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fef08a" stop-opacity="1"/>
      <stop offset="50%" stop-color="#ef4444" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#070a12" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#f1df76" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="52" r="36" fill="url(#clashGlow)"/>

  <!-- Blade 1 (Cyan) -->
  <line x1="28" y1="80" x2="84" y2="24" stroke="#38bdf8" stroke-width="4" stroke-linecap="round"/>
  <!-- Blade 2 (Crimson) -->
  <line x1="28" y1="24" x2="84" y2="80" stroke="#ef4444" stroke-width="4" stroke-linecap="round"/>

  <!-- Center Impact Spark & Clash Die -->
  <polygon points="60,42 66,52 76,52 68,60 72,70 60,64 48,70 52,60 44,52 54,52" fill="#fef08a"/>
  <circle cx="60" cy="52" r="4" fill="#ffffff"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#1f1807" stroke="#f1df76" stroke-width="1"/>
  <text x="60" y="108.5" fill="#f1df76" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">RESONANT CLASH</text>
</svg>""",

        # Ordeals Framework - 24-Hour Tactical Ordeal Clock
        "icon_mech_ordeals_framework.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#f59e0b" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>

  <!-- Tactical Ordeal Radar Dial -->
  <circle cx="60" cy="52" r="34" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>

  <!-- Ordeal Phase Sectors: Dawn, Noon, Dusk, Midnight -->
  <path d="M 60 52 L 60 18 A 34 34 0 0 1 94 52 Z" fill="#064e3b" stroke="#10b981" stroke-width="1"/>
  <path d="M 60 52 L 94 52 A 34 34 0 0 1 60 86 Z" fill="#0c4a6e" stroke="#0284c7" stroke-width="1"/>
  <path d="M 60 52 L 60 86 A 34 34 0 0 1 26 52 Z" fill="#7f1d1d" stroke="#ef4444" stroke-width="1"/>
  <path d="M 60 52 L 26 52 A 34 34 0 0 1 60 18 Z" fill="#3b0764" stroke="#a855f7" stroke-width="1"/>

  <!-- Ordeal Alert Radar Hand -->
  <line x1="60" y1="52" x2="84" y2="28" stroke="#f1df76" stroke-width="2.5" stroke-linecap="round"/>
  <circle cx="60" cy="52" r="5" fill="#f1df76"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#241403" stroke="#f59e0b" stroke-width="1"/>
  <text x="60" y="108.5" fill="#f59e0b" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">ORDEALS FRAMEWORK</text>
</svg>""",

        # Agent Statistics - Operative Radar Pentagon HUD
        "icon_mech_agent_stats.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#10b981" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>

  <!-- Radar Pentagon Wireframe -->
  <polygon points="60,20 90,42 80,78 40,78 30,42" fill="#062e22" stroke="#10b981" stroke-width="1.5"/>
  <polygon points="60,32 80,47 73,71 47,71 40,47" fill="#047857" opacity="0.5" stroke="#34d399" stroke-width="1"/>
  
  <!-- Tactical Stat Nodes (HP, SP, ATK, DEF, SPD) -->
  <circle cx="60" cy="20" r="3" fill="#ef4444"/>
  <circle cx="90" cy="42" r="3" fill="#38bdf8"/>
  <circle cx="80" cy="78" r="3" fill="#f1df76"/>
  <circle cx="40" cy="78" r="3" fill="#10b981"/>
  <circle cx="30" cy="42" r="3" fill="#a855f7"/>

  <!-- Center Pivot -->
  <circle cx="60" cy="52" r="3" fill="#ffffff"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#062e22" stroke="#10b981" stroke-width="1"/>
  <text x="60" y="108.5" fill="#34d399" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">AGENT STATS</text>
</svg>""",

        # Containment Suppression - Hydraulic Airlock & Laser Grid
        "icon_mech_containment_suppression.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#ef4444" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>

  <!-- Heavy Hydraulic Blast Door Frame -->
  <rect x="26" y="20" width="68" height="68" fill="#1c1917" stroke="#ef4444" stroke-width="2"/>
  
  <!-- Laser Security Suppression Grid -->
  <line x1="26" y1="36" x2="94" y2="36" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,2"/>
  <line x1="26" y1="54" x2="94" y2="54" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,2"/>
  <line x1="26" y1="72" x2="94" y2="72" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,2"/>
  
  <line x1="44" y1="20" x2="44" y2="88" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,2"/>
  <line x1="60" y1="20" x2="60" y2="88" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,2"/>
  <line x1="76" y1="20" x2="76" y2="88" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,2"/>

  <!-- Central Emergency Interlock Seal -->
  <polygon points="60,44 68,54 60,64 52,54" fill="#ef4444"/>
  <circle cx="60" cy="54" r="2" fill="#ffffff"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#200a0a" stroke="#ef4444" stroke-width="1"/>
  <text x="60" y="108.5" fill="#ef4444" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">CONTAINMENT</text>
</svg>""",

        # Standard Equipment - Directorate Sidearm & Ballistic Baton
        "icon_mech_standard_equipment.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#38bdf8" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>

  <!-- Kinetic 9mm Pistol Silhouette -->
  <path d="M 30 52 L 68 52 L 68 62 L 56 62 L 52 82 L 40 80 L 44 62 L 30 62 Z" fill="#1e293b" stroke="#38bdf8" stroke-width="1.8"/>
  <line x1="30" y1="56" x2="68" y2="56" stroke="#0284c7" stroke-width="1"/>

  <!-- Heavy Shock Baton -->
  <line x1="86" y1="24" x2="54" y2="86" stroke="#f1df76" stroke-width="4" stroke-linecap="round"/>
  <circle cx="86" cy="24" r="4" fill="#ef4444"/>

  <!-- Tactical Vest Badge -->
  <circle cx="60" cy="36" r="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <polygon points="60,31 65,36 60,41 55,36" fill="#38bdf8"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#0c192c" stroke="#38bdf8" stroke-width="1"/>
  <text x="60" y="108.5" fill="#38bdf8" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">STANDARD GEAR</text>
</svg>""",

        # Enemy Bestiary - Tactical Wireframe Target Acquisition Scanner
        "icon_mech_enemy_bestiary.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#ef4444" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>

  <!-- Target Acquisition Reticle -->
  <circle cx="60" cy="52" r="32" fill="#1c0a0a" stroke="#ef4444" stroke-width="1.5"/>
  <circle cx="60" cy="52" r="22" fill="none" stroke="#ef4444" stroke-width="1" stroke-dasharray="4,3"/>

  <!-- Reticle Corner Brackets -->
  <path d="M 32 36 L 32 24 L 44 24" fill="none" stroke="#f1df76" stroke-width="2"/>
  <path d="M 88 36 L 88 24 L 76 24" fill="none" stroke="#f1df76" stroke-width="2"/>
  <path d="M 32 68 L 32 80 L 44 80" fill="none" stroke="#f1df76" stroke-width="2"/>
  <path d="M 88 68 L 88 80 L 76 80" fill="none" stroke="#f1df76" stroke-width="2"/>

  <!-- Enemy Aberration Target Silhouette inside reticle -->
  <circle cx="60" cy="46" r="8" fill="#ef4444"/>
  <polygon points="52,54 68,54 74,72 46,72" fill="#ef4444"/>
  <circle cx="60" cy="46" r="2" fill="#ffffff"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#200a0a" stroke="#ef4444" stroke-width="1"/>
  <text x="60" y="108.5" fill="#ef4444" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">ENEMY BESTIARY</text>
</svg>""",

        # Fracture Therapy - Neuro-Stabilization Pod & Cyan Cadence
        "icon_mech_fracture_therapy.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="therGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.8"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#38bdf8" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="52" r="38" fill="url(#therGlow)"/>

  <!-- Medical Stasis Pod Capsule -->
  <rect x="42" y="20" width="36" height="66" rx="18" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
  
  <!-- Neuro-Calibrating Cadence Waves -->
  <path d="M 48 42 Q 60 36 72 42" fill="none" stroke="#71efaf" stroke-width="1.8"/>
  <path d="M 48 54 Q 60 48 72 54" fill="none" stroke="#38bdf8" stroke-width="1.8"/>
  <path d="M 48 66 Q 60 60 72 66" fill="none" stroke="#f1df76" stroke-width="1.8"/>

  <!-- Stabilization Core -->
  <circle cx="60" cy="52" r="4" fill="#ffffff"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#0c192c" stroke="#38bdf8" stroke-width="1"/>
  <text x="60" y="108.5" fill="#38bdf8" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">FRACTURE THERAPY</text>
</svg>""",

        # Han Relic Registry - Sealed Stasis Preservation Vessel
        "icon_mech_han_relic_registry.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="relicGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#f1df76" stop-opacity="0.9"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#f1df76" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="52" r="38" fill="url(#relicGlow)"/>

  <!-- Ancient Stasis Preservation Vessel -->
  <polygon points="44,28 76,28 84,76 36,76" fill="#1f1807" stroke="#f1df76" stroke-width="2"/>
  
  <!-- Floating Ancient Han Core inside Vessel -->
  <polygon points="60,38 72,52 60,66 48,52" fill="#d97706" stroke="#fef08a" stroke-width="1.8"/>
  <circle cx="60" cy="52" r="3" fill="#ffffff"/>

  <!-- Magnetic Stasis Rings -->
  <ellipse cx="60" cy="52" rx="20" ry="8" fill="none" stroke="#38bdf8" stroke-width="1.2" stroke-dasharray="3,2"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#1f1807" stroke="#f1df76" stroke-width="1"/>
  <text x="60" y="108.5" fill="#f1df76" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">RELIC REGISTRY</text>
</svg>""",

        # M.A.W. Equipment System - Weapon, Suit, and Gift Matrix
        "icon_mech_maw_equipment_system.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#f59e0b" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>

  <!-- Tri-System Synchronization Matrix -->
  <!-- Top: M.A.W. Gift (Halo/Crown) -->
  <circle cx="60" cy="28" r="10" fill="none" stroke="#fef08a" stroke-width="2"/>
  <circle cx="60" cy="28" r="4" fill="#fef08a"/>

  <!-- Left: M.A.W. Weapon (Blade) -->
  <line x1="30" y1="74" x2="48" y2="48" stroke="#ef4444" stroke-width="3" stroke-linecap="round"/>
  <line x1="36" y1="74" x2="48" y2="74" stroke="#ef4444" stroke-width="2"/>

  <!-- Right: M.A.W. Suit (Armored Cuirass) -->
  <polygon points="72,48 88,48 92,74 68,74" fill="#0c4a6e" stroke="#38bdf8" stroke-width="1.5"/>

  <!-- Interconnecting Resonance Lines -->
  <path d="M 60 38 L 42 56 L 78 56 Z" fill="none" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3,2"/>
  <circle cx="60" cy="56" r="4" fill="#f59e0b"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#241403" stroke="#f59e0b" stroke-width="1"/>
  <text x="60" y="108.5" fill="#f59e0b" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">M.A.W. SYSTEM</text>
</svg>""",

        # Taboo Resonance Mechanics - Resonance Wave Spike & Critical Threshold
        "icon_mech_taboo_resonance_mech.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#ef4444" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>

  <!-- Waveform Analyzer Screen -->
  <rect x="22" y="22" width="76" height="64" rx="4" fill="#1c0a0a" stroke="#ef4444" stroke-width="1.5"/>
  
  <!-- Critical Red Threshold Limit Line -->
  <line x1="22" y1="40" x2="98" y2="40" stroke="#fca5a5" stroke-width="1" stroke-dasharray="2,2"/>
  <text x="94" y="36" fill="#fca5a5" font-family="monospace" font-size="6" text-anchor="end">CRIT</text>

  <!-- Spiking Harmonic Resonance Wave -->
  <path d="M 24 64 L 38 64 L 46 54 L 54 72 L 60 28 L 66 78 L 74 58 L 82 64 L 96 64" fill="none" stroke="#ef4444" stroke-width="2"/>
  
  <!-- Peak Spike Warning Marker -->
  <circle cx="60" cy="28" r="3" fill="#f1df76"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#200a0a" stroke="#ef4444" stroke-width="1"/>
  <text x="60" y="108.5" fill="#ef4444" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">TABOO RESONANCE</text>
</svg>"""
    }

def main():
    lore = get_lore_icons()
    for name, svg in lore.items():
        p1 = os.path.join(WIKI_ASSETS_ICONS, name)
        p2 = os.path.join(WORKSPACE_ICONS, name)
        for p in [p1, p2]:
            with open(p, "w", encoding="utf-8") as f:
                f.write(svg)
        print(f"Generated Lore Icon: {name}")

    mech = get_mechanics_icons()
    for name, svg in mech.items():
        p1 = os.path.join(WIKI_ASSETS_ICONS, name)
        p2 = os.path.join(WORKSPACE_ICONS, name)
        for p in [p1, p2]:
            with open(p, "w", encoding="utf-8") as f:
                f.write(svg)
        print(f"Generated Mechanics Icon: {name}")

if __name__ == "__main__":
    main()
