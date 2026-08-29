#!/usr/bin/env python3
"""
tools/upgrade_dept_special_icons.py
Upgrades icon_dept_room_types.svg and icon_dept_incident_archive.svg
"""

import os

HAND_ICONS = "/home/user/01_Somnarak_Wiki/assets/layout/hand/icons"
WORKSPACE_ICONS = "/home/user/icons"
ASSETS_ICONS = "/home/user/01_Somnarak_Wiki/assets/icons"

room_types_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="roomGlow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.8"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#38bdf8" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="50" r="38" fill="url(#roomGlow)"/>

  <!-- Facility Blueprint Rooms Architecture -->
  <!-- Top Left: Containment Cell (Crimson Alert) -->
  <rect x="24" y="22" width="32" height="28" rx="2" fill="#1c0a0a" stroke="#ef4444" stroke-width="1.8"/>
  <circle cx="40" cy="36" r="4" fill="#ef4444"/>

  <!-- Top Right: Observation Deck (Cyan Stream) -->
  <rect x="64" y="22" width="32" height="28" rx="2" fill="#0c192c" stroke="#38bdf8" stroke-width="1.8"/>
  <ellipse cx="80" cy="36" rx="8" ry="4" fill="none" stroke="#38bdf8" stroke-width="1.5"/>

  <!-- Bottom Left: Han Sub-Station (Gold Power) -->
  <rect x="24" y="56" width="32" height="28" rx="2" fill="#1f1807" stroke="#f1df76" stroke-width="1.8"/>
  <polygon points="40,62 44,70 38,70 42,78 36,78 40,84" fill="#f1df76"/>

  <!-- Bottom Right: Medical Stasis (Green Pulse) -->
  <rect x="64" y="56" width="32" height="28" rx="2" fill="#062e22" stroke="#10b981" stroke-width="1.8"/>
  <line x1="72" y1="70" x2="88" y2="70" stroke="#71efaf" stroke-width="2"/>
  <line x1="80" y1="62" x2="80" y2="78" stroke="#71efaf" stroke-width="2"/>

  <!-- Interconnecting Transit Corridors -->
  <line x1="56" y1="36" x2="64" y2="36" stroke="#f1df76" stroke-width="2.5"/>
  <line x1="56" y1="70" x2="64" y2="70" stroke="#f1df76" stroke-width="2.5"/>
  <line x1="40" y1="50" x2="40" y2="56" stroke="#f1df76" stroke-width="2.5"/>
  <line x1="80" y1="50" x2="80" y2="56" stroke="#f1df76" stroke-width="2.5"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#0c192c" stroke="#38bdf8" stroke-width="1"/>
  <text x="60" y="108.5" fill="#38bdf8" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">FACILITY ROOMS</text>
</svg>"""

incident_archive_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="100%" height="100%">
  <defs>
    <radialGradient id="incGlow" cx="50%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#ef4444" stop-opacity="0.8"/>
      <stop offset="70%" stop-color="#070a12" stop-opacity="1"/>
    </radialGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="16" fill="#070a12" stroke="#ef4444" stroke-width="2.5"/>
  <rect x="8" y="8" width="104" height="104" rx="12" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
  <circle cx="60" cy="50" r="38" fill="url(#incGlow)"/>

  <!-- Classified Incident Dossier Folder -->
  <polygon points="26,30 52,30 58,38 94,38 94,86 26,86" fill="#1c1917" stroke="#ef4444" stroke-width="2"/>
  
  <!-- Document Lines inside Dossier -->
  <line x1="36" y1="48" x2="84" y2="48" stroke="#fca5a5" stroke-width="1.5"/>
  <line x1="36" y1="56" x2="84" y2="56" stroke="#fca5a5" stroke-width="1.5"/>
  <line x1="36" y1="64" x2="68" y2="64" stroke="#fca5a5" stroke-width="1.5"/>

  <!-- Glowing Red Breach Alert Stamp -->
  <rect x="44" y="60" width="46" height="18" rx="2" fill="#7f1d1d" stroke="#ef4444" stroke-width="1.8"/>
  <text x="67" y="73" fill="#ffffff" font-family="Impact, Arial" font-size="9" text-anchor="middle">BREACH</text>

  <!-- Hazard Alert Warning Triangle -->
  <polygon points="60,16 66,26 54,26" fill="#f1df76"/>
  <circle cx="60" cy="24" r="1" fill="#070a12"/>

  <!-- Label Banner -->
  <rect x="14" y="98" width="92" height="14" rx="3" fill="#200a0a" stroke="#ef4444" stroke-width="1"/>
  <text x="60" y="108.5" fill="#ef4444" font-family="monospace" font-size="7.5" font-weight="bold" text-anchor="middle">INCIDENT LOGS</text>
</svg>"""

for d in [HAND_ICONS, WORKSPACE_ICONS, ASSETS_ICONS]:
    with open(os.path.join(d, "icon_dept_room_types.svg"), "w", encoding="utf-8") as f:
        f.write(room_types_svg)
    with open(os.path.join(d, "icon_dept_incident_archive.svg"), "w", encoding="utf-8") as f:
        f.write(incident_archive_svg)

print("Upgraded special department icons!")
