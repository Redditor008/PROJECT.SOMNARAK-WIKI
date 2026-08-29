import os

support_chars = {
    'icon_char_taeho.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <radialGradient id="g_tae" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#450a0a"/>
      <stop offset="70%" stop-color="#1a0406"/>
      <stop offset="100%" stop-color="#050810"/>
    </radialGradient>
  </defs>
  <rect width="120" height="120" rx="10" fill="url(#g_tae)" stroke="#ef5b55" stroke-width="2.5"/>
  <!-- UCD Tactical Heavy Shield & Breaching Maul -->
  <polygon points="60,16 98,34 98,82 60,104 22,82 22,34" fill="#1c0406" stroke="#ef5b55" stroke-width="2"/>
  <line x1="36" y1="36" x2="84" y2="84" stroke="#f1df76" stroke-width="4" stroke-linecap="round"/>
  <rect x="74" y="26" width="18" height="22" rx="3" fill="#ef5b55" stroke="#f1df76" stroke-width="1.5"/>
  <circle cx="60" cy="60" r="14" fill="#450a0a" stroke="#ef5b55" stroke-width="2"/>
  <circle cx="60" cy="60" r="6" fill="#f1df76"/>
</svg>''',

    'icon_char_yeonhwa.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <radialGradient id="g_yeon" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#082f49"/>
      <stop offset="70%" stop-color="#031624"/>
      <stop offset="100%" stop-color="#050810"/>
    </radialGradient>
  </defs>
  <rect width="120" height="120" rx="10" fill="url(#g_yeon)" stroke="#38bdf8" stroke-width="2.5"/>
  <!-- Amnestic Solvent Flask & Mind Mirror -->
  <circle cx="60" cy="60" r="38" fill="none" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="6 3"/>
  <polygon points="52,24 68,24 74,52 46,52" fill="#0c4a6e" stroke="#38bdf8" stroke-width="1.5"/>
  <path d="M46,52 C34,70 34,92 60,96 C86,92 86,70 74,52 Z" fill="#082f49" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="60" cy="74" r="12" fill="#38bdf8" opacity="0.8"/>
  <circle cx="60" cy="74" r="5" fill="#ffffff"/>
</svg>''',

    'icon_char_kael.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <radialGradient id="g_kael" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#422006"/>
      <stop offset="70%" stop-color="#1c0f03"/>
      <stop offset="100%" stop-color="#050810"/>
    </radialGradient>
  </defs>
  <rect width="120" height="120" rx="10" fill="url(#g_kael)" stroke="#f1df76" stroke-width="2.5"/>
  <!-- Guild Abacus & Gold Scales -->
  <line x1="26" y1="46" x2="94" y2="46" stroke="#f1df76" stroke-width="2.5"/>
  <line x1="60" y1="26" x2="60" y2="94" stroke="#f1df76" stroke-width="3"/>
  <!-- Scale Pans -->
  <polygon points="34,46 22,76 46,76" fill="#1c0f03" stroke="#f1df76" stroke-width="1.5"/>
  <polygon points="86,46 74,76 98,76" fill="#1c0f03" stroke="#f1df76" stroke-width="1.5"/>
  <circle cx="34" cy="76" r="4" fill="#ef5b55"/>
  <circle cx="86" cy="76" r="4" fill="#38bdf8"/>
  <circle cx="60" cy="26" r="5" fill="#f1df76"/>
</svg>''',

    'icon_char_minho.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <radialGradient id="g_min" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#1e1b4b"/>
      <stop offset="70%" stop-color="#0b0922"/>
      <stop offset="100%" stop-color="#050810"/>
    </radialGradient>
  </defs>
  <rect width="120" height="120" rx="10" fill="url(#g_min)" stroke="#818cf8" stroke-width="2.5"/>
  <!-- Containment Stun Baton & HUD Visor -->
  <rect x="26" y="38" width="68" height="22" rx="4" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
  <line x1="32" y1="49" x2="88" y2="49" stroke="#38bdf8" stroke-width="3"/>
  <line x1="30" y1="92" x2="90" y2="32" stroke="#f1df76" stroke-width="3.5" stroke-linecap="round"/>
  <circle cx="88" cy="34" r="6" fill="#ef5b55"/>
</svg>''',

    'icon_char_soojin.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <radialGradient id="g_soo" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#064e3b"/>
      <stop offset="70%" stop-color="#022119"/>
      <stop offset="100%" stop-color="#050810"/>
    </radialGradient>
  </defs>
  <rect width="120" height="120" rx="10" fill="url(#g_soo)" stroke="#71efaf" stroke-width="2.5"/>
  <!-- Handheld Siphon Pressure Gauge & Injector -->
  <circle cx="60" cy="54" r="26" fill="#04231b" stroke="#71efaf" stroke-width="2"/>
  <line x1="60" y1="54" x2="74" y2="42" stroke="#ef5b55" stroke-width="2.5"/>
  <circle cx="60" cy="54" r="4" fill="#f1df76"/>
  <rect x="54" y="80" width="12" height="24" rx="2" fill="#064e3b" stroke="#71efaf" stroke-width="1.5"/>
  <line x1="60" y1="80" x2="60" y2="104" stroke="#38bdf8" stroke-width="2"/>
</svg>''',

    'icon_char_sora.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <radialGradient id="g_sora" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#431407"/>
      <stop offset="70%" stop-color="#1c0702"/>
      <stop offset="100%" stop-color="#050810"/>
    </radialGradient>
  </defs>
  <rect width="120" height="120" rx="10" fill="url(#g_sora)" stroke="#fb923c" stroke-width="2.5"/>
  <!-- Border Scout Night Scope & Crosshairs -->
  <circle cx="60" cy="60" r="36" fill="none" stroke="#fb923c" stroke-width="2"/>
  <circle cx="60" cy="60" r="22" fill="#1c0702" stroke="#f1df76" stroke-width="1.5" stroke-dasharray="6 3"/>
  <line x1="18" y1="60" x2="102" y2="60" stroke="#fb923c" stroke-width="1.5"/>
  <line x1="60" y1="18" x2="60" y2="102" stroke="#fb923c" stroke-width="1.5"/>
  <circle cx="60" cy="60" r="5" fill="#ef5b55"/>
</svg>''',

    'icon_char_doha.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <radialGradient id="g_doha" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#3b0764"/>
      <stop offset="70%" stop-color="#140224"/>
      <stop offset="100%" stop-color="#050810"/>
    </radialGradient>
  </defs>
  <rect width="120" height="120" rx="10" fill="url(#g_doha)" stroke="#c084fc" stroke-width="2.5"/>
  <!-- Council Ivory Scepter & Law Scroll -->
  <rect x="34" y="30" width="52" height="60" rx="4" fill="#140224" stroke="#c084fc" stroke-width="1.8"/>
  <line x1="42" y1="44" x2="78" y2="44" stroke="#f1df76" stroke-width="2"/>
  <line x1="42" y1="56" x2="78" y2="56" stroke="#f1df76" stroke-width="2" stroke-dasharray="4 2"/>
  <line x1="42" y1="68" x2="68" y2="68" stroke="#f1df76" stroke-width="2" stroke-dasharray="4 2"/>
  <line x1="24" y1="94" x2="96" y2="22" stroke="#f1df76" stroke-width="3"/>
  <circle cx="96" cy="22" r="5" fill="#38bdf8"/>
</svg>''',

    'icon_char_joon.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <radialGradient id="g_joon" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="70%" stop-color="#060912"/>
      <stop offset="100%" stop-color="#020306"/>
    </radialGradient>
  </defs>
  <rect width="120" height="120" rx="10" fill="url(#g_joon)" stroke="#64748b" stroke-width="2.5"/>
  <!-- Smuggler Lockpick & Shadow Dagger -->
  <polygon points="60,20 72,50 60,100 48,50" fill="#0f172a" stroke="#94a3b8" stroke-width="2"/>
  <circle cx="60" cy="50" r="10" fill="#38bdf8" opacity="0.7"/>
  <line x1="30" y1="90" x2="90" y2="90" stroke="#f1df76" stroke-width="2.5"/>
  <circle cx="60" cy="50" r="3" fill="#ffffff"/>
</svg>'''
}

dirs = ['/home/user/01_Somnarak_Wiki/assets/icons', '/home/user/icons']

for filename, content in support_chars.items():
    # Write icon_char_* and icon_core_*
    core_name = filename.replace('icon_char_', 'icon_core_')
    for d in dirs:
        os.makedirs(d, exist_ok=True)
        for name in [filename, core_name]:
            p = os.path.join(d, name)
            with open(p, 'w', encoding='utf-8') as f:
                f.write(content.strip())
            print(f'Wrote {p}')

print('SUCCESS: Upgraded all support character artifact icons!')
