import os

def build_all_ultra_svgs():
    base_dir = "/home/user/01_Somnarak_Wiki/assets"
    
    # 1. ENTITY SVGs (400x400 viewBox, rich multi-layered composition)
    entity_art_dir = os.path.join(base_dir, "art/entities")
    os.makedirs(entity_art_dir, exist_ok=True)
    
    entities = {
        "se-001.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <radialGradient id="se001Bg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#1e293b" stop-opacity="0.9"/>
      <stop offset="60%" stop-color="#090d16" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#030712" stop-opacity="1"/>
    </radialGradient>
    <radialGradient id="se001Aura" cx="50%" cy="45%" r="45%">
      <stop offset="0%" stop-color="#f1df76" stop-opacity="0.25"/>
      <stop offset="50%" stop-color="#38bdf8" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="bronzeBell" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2d3748"/>
      <stop offset="30%" stop-color="#4a5568"/>
      <stop offset="70%" stop-color="#1a202c"/>
      <stop offset="100%" stop-color="#0d1117"/>
    </linearGradient>
    <linearGradient id="goldTrim" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f1df76"/>
      <stop offset="50%" stop-color="#fff3b0"/>
      <stop offset="100%" stop-color="#d4af37"/>
    </linearGradient>
    <filter id="cyanGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <!-- Frame & Backdrop -->
  <rect x="6" y="6" width="388" height="388" rx="20" fill="url(#se001Bg)" stroke="#f1df76" stroke-width="2.5"/>
  <rect x="14" y="14" width="372" height="372" rx="14" fill="none" stroke="#38bdf8" stroke-width="1" stroke-dasharray="8 4" opacity="0.4"/>
  <circle cx="200" cy="190" r="150" fill="url(#se001Aura)"/>
  
  <!-- Technical Grid Elements -->
  <g opacity="0.15" stroke="#38bdf8" stroke-width="1">
    <line x1="20" y1="200" x2="380" y2="200"/>
    <line x1="200" y1="20" x2="200" y2="380"/>
    <circle cx="200" cy="190" r="170" fill="none" stroke-dasharray="4 6"/>
  </g>

  <!-- Toll Wave Harmonics -->
  <g opacity="0.4" filter="url(#cyanGlow)">
    <path d="M 50 200 Q 120 160 200 160 Q 280 160 350 200" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3 3"/>
    <path d="M 40 240 Q 120 190 200 190 Q 280 190 360 240" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3 3"/>
    <path d="M 30 280 Q 120 220 200 220 Q 280 220 370 280" fill="none" stroke="#f1df76" stroke-width="1.5" stroke-dasharray="4 4"/>
  </g>

  <!-- Suspension Shackle -->
  <path d="M 175 40 L 225 40 L 220 70 L 180 70 Z" fill="#1e293b" stroke="#f1df76" stroke-width="2.5"/>
  <circle cx="200" cy="55" r="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
  
  <!-- Bell Main Body -->
  <path d="M 140 90 C 140 65, 260 65, 260 90 C 260 140, 295 240, 310 275 C 315 285, 305 295, 290 295 L 110 295 C 95 295, 85 285, 90 275 C 105 240, 140 140, 140 90 Z" fill="url(#bronzeBell)" stroke="url(#goldTrim)" stroke-width="3.5"/>
  
  <!-- Bell Rim Base -->
  <ellipse cx="200" cy="295" rx="100" ry="24" fill="#111827" stroke="url(#goldTrim)" stroke-width="3"/>
  <ellipse cx="200" cy="295" rx="75" ry="16" fill="#050811" stroke="#38bdf8" stroke-width="1.5"/>

  <!-- Weeping Clapper -->
  <path d="M 195 270 L 205 270 L 212 330 L 188 330 Z" fill="#1e293b" stroke="#ef5b55" stroke-width="2"/>
  <circle cx="200" cy="335" r="22" fill="#ef5b55" stroke="#f1df76" stroke-width="2.5" filter="url(#cyanGlow)"/>
  <circle cx="200" cy="335" r="10" fill="#7f1d1d"/>

  <!-- Fissures and Weeping Eyes Relief on Bell -->
  <!-- Tear Cracks -->
  <path d="M 200 120 L 190 155 L 210 185 L 195 230 L 202 260" fill="none" stroke="#38bdf8" stroke-width="2.5" filter="url(#cyanGlow)"/>
  <path d="M 190 155 L 170 175 L 165 210" fill="none" stroke="#38bdf8" stroke-width="1.8" opacity="0.8"/>
  <path d="M 210 185 L 235 205 L 230 245" fill="none" stroke="#38bdf8" stroke-width="1.8" opacity="0.8"/>

  <!-- Engraved Weeping Faces -->
  <circle cx="170" cy="145" r="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <circle cx="170" cy="145" r="3" fill="#38bdf8"/>
  <path d="M 170 153 Q 165 185 160 215" fill="none" stroke="#38bdf8" stroke-width="2" opacity="0.85"/>

  <circle cx="230" cy="145" r="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <circle cx="230" cy="145" r="3" fill="#38bdf8"/>
  <path d="M 230 153 Q 235 185 240 215" fill="none" stroke="#38bdf8" stroke-width="2" opacity="0.85"/>

  <!-- Mouth Inscription of Mourning -->
  <path d="M 180 180 Q 200 165 220 180" fill="none" stroke="#f1df76" stroke-width="2.5"/>
  <path d="M 185 188 Q 200 178 215 188" fill="none" stroke="#f1df76" stroke-width="1.5" opacity="0.7"/>

  <!-- Decorative Filigree Bands -->
  <path d="M 132 105 Q 200 120 268 105" fill="none" stroke="#f1df76" stroke-width="2"/>
  <path d="M 108 245 Q 200 275 292 245" fill="none" stroke="#f1df76" stroke-width="2.5"/>

  <!-- Han Particle Embers -->
  <circle cx="120" cy="310" r="3" fill="#f1df76" opacity="0.8"/>
  <circle cx="280" cy="320" r="3" fill="#38bdf8" opacity="0.8"/>
  <circle cx="85" cy="170" r="2.5" fill="#38bdf8" opacity="0.6"/>
  <circle cx="315" cy="160" r="2.5" fill="#f1df76" opacity="0.6"/>
  
  <!-- Classification Badge Overlay -->
  <rect x="26" y="26" width="90" height="26" rx="6" fill="#090d16" stroke="#f1df76" stroke-width="1.5"/>
  <text x="71" y="44" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">SE-001</text>
  <rect x="284" y="26" width="90" height="26" rx="6" fill="#090d16" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="329" y="44" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">SOMNA</text>
</svg>''',

        "se-002.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <radialGradient id="se002Bg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#2d1215" stop-opacity="0.9"/>
      <stop offset="60%" stop-color="#130608" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#050102" stop-opacity="1"/>
    </radialGradient>
    <radialGradient id="crimsonAura" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ef5b55" stop-opacity="0.35"/>
      <stop offset="60%" stop-color="#b91c1c" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>
    <filter id="crimsonGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <rect x="6" y="6" width="388" height="388" rx="20" fill="url(#se002Bg)" stroke="#ef5b55" stroke-width="2.5"/>
  <rect x="14" y="14" width="372" height="372" rx="14" fill="none" stroke="#f1df76" stroke-width="1" stroke-dasharray="8 4" opacity="0.4"/>
  <circle cx="200" cy="200" r="160" fill="url(#crimsonAura)"/>

  <!-- Colossus Heavy Stone Monolith Silhouette -->
  <!-- Shoulder Spires / Broken Architecture -->
  <path d="M 60 210 L 90 120 L 130 160 L 150 110 L 180 170 L 200 130 L 220 170 L 250 110 L 270 160 L 310 120 L 340 210 L 370 360 L 30 360 Z" fill="#1b1c22" stroke="#ef5b55" stroke-width="3"/>
  
  <!-- Obsidian Crags & Armor Plates -->
  <polygon points="100,200 160,180 180,260 90,270" fill="#2a2b36" stroke="#f1df76" stroke-width="2"/>
  <polygon points="240,180 300,200 310,270 220,260" fill="#2a2b36" stroke="#f1df76" stroke-width="2"/>
  <polygon points="150,220 250,220 270,330 130,330" fill="#15161c" stroke="#ef5b55" stroke-width="2.5"/>

  <!-- Central Grieving Visage Fissure -->
  <path d="M 190 140 L 210 140 L 215 190 L 185 190 Z" fill="#0b0c10" stroke="#f1df76" stroke-width="2"/>
  <!-- Glowing Crimson Core Eye Fissures -->
  <g filter="url(#crimsonGlow)">
    <circle cx="180" cy="165" r="7" fill="#ef5b55"/>
    <circle cx="220" cy="165" r="7" fill="#ef5b55"/>
    <path d="M 180 172 L 175 220 L 160 280 L 170 340" fill="none" stroke="#ef5b55" stroke-width="3"/>
    <path d="M 220 172 L 225 220 L 240 280 L 230 340" fill="none" stroke="#ef5b55" stroke-width="3"/>
    <path d="M 200 190 L 200 240 L 195 290 L 205 350" fill="none" stroke="#f1df76" stroke-width="2.5"/>
  </g>

  <!-- Crushed Buildings at Base -->
  <polygon points="70,360 85,310 120,320 130,360" fill="#0f1015" stroke="#71efaf" stroke-width="1.5"/>
  <polygon points="270,360 285,315 320,325 330,360" fill="#0f1015" stroke="#71efaf" stroke-width="1.5"/>

  <!-- Floating Han Magma Embers -->
  <circle cx="80" cy="100" r="3" fill="#ef5b55" opacity="0.9"/>
  <circle cx="320" cy="90" r="4" fill="#ef5b55" opacity="0.9"/>
  <circle cx="140" cy="60" r="2.5" fill="#f1df76" opacity="0.8"/>
  <circle cx="260" cy="50" r="3" fill="#f1df76" opacity="0.8"/>

  <!-- Classification Badge Overlay -->
  <rect x="26" y="26" width="90" height="26" rx="6" fill="#090d16" stroke="#ef5b55" stroke-width="1.5"/>
  <text x="71" y="44" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">SE-002</text>
  <rect x="274" y="26" width="100" height="26" rx="6" fill="#090d16" stroke="#ef5b55" stroke-width="1.5"/>
  <text x="324" y="44" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">PHANTASM</text>
</svg>''',

        "se-003.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <radialGradient id="se003Bg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#042f2e" stop-opacity="0.9"/>
      <stop offset="70%" stop-color="#021a19" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#010d0c" stop-opacity="1"/>
    </radialGradient>
    <filter id="emeraldGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <rect x="6" y="6" width="388" height="388" rx="20" fill="url(#se003Bg)" stroke="#71efaf" stroke-width="2.5"/>
  <rect x="14" y="14" width="372" height="372" rx="14" fill="none" stroke="#38bdf8" stroke-width="1" stroke-dasharray="8 4" opacity="0.4"/>

  <!-- Surging Wilderness Bio-Fluid Waves -->
  <path d="M 20 360 Q 90 280 160 320 T 300 270 T 380 340 L 380 380 L 20 380 Z" fill="#064e3b" stroke="#71efaf" stroke-width="2"/>
  <path d="M 20 310 Q 100 210 190 260 T 330 180 T 380 260 L 380 380 L 20 380 Z" fill="#042f2e" stroke="#38bdf8" stroke-width="2.5"/>
  <path d="M 20 240 Q 80 120 180 180 T 310 100 T 380 190 L 380 380 L 20 380 Z" fill="#021d1c" stroke="#71efaf" stroke-width="3"/>

  <!-- Cresting Skeletal Tsunami Claws -->
  <g filter="url(#emeraldGlow)" stroke="#71efaf" stroke-width="2.5" fill="none">
    <path d="M 280 130 C 270 80, 230 70, 210 100 C 200 120, 215 150, 240 160"/>
    <path d="M 245 90 C 240 60, 210 50, 190 80"/>
    <path d="M 320 110 C 310 50, 260 40, 230 75"/>
  </g>

  <!-- Grasping Tendrils & Skeletal Limbs Emerging from Tide -->
  <path d="M 80 340 L 95 260 L 80 230 L 105 240 L 110 210" fill="none" stroke="#f1df76" stroke-width="2.5"/>
  <path d="M 140 330 L 155 240 L 175 220 L 165 190" fill="none" stroke="#71efaf" stroke-width="2"/>
  <path d="M 260 350 L 280 270 L 305 250 L 310 220" fill="none" stroke="#38bdf8" stroke-width="2"/>

  <!-- Han Tide Vortices -->
  <circle cx="200" cy="270" r="16" fill="none" stroke="#71efaf" stroke-width="2" stroke-dasharray="4 4"/>
  <circle cx="200" cy="270" r="6" fill="#71efaf" filter="url(#emeraldGlow)"/>

  <!-- Classification Badge Overlay -->
  <rect x="26" y="26" width="90" height="26" rx="6" fill="#090d16" stroke="#71efaf" stroke-width="1.5"/>
  <text x="71" y="44" fill="#71efaf" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">SE-003</text>
  <rect x="274" y="26" width="100" height="26" rx="6" fill="#090d16" stroke="#f1df76" stroke-width="1.5"/>
  <text x="324" y="44" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">MORPHEAN</text>
</svg>''',

        "se-005.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <radialGradient id="se005Bg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#1e1b4b" stop-opacity="0.9"/>
      <stop offset="60%" stop-color="#0f0d26" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#050410" stop-opacity="1"/>
    </radialGradient>
    <filter id="indigoGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <rect x="6" y="6" width="388" height="388" rx="20" fill="url(#se005Bg)" stroke="#c084fc" stroke-width="2.5"/>
  <rect x="14" y="14" width="372" height="372" rx="14" fill="none" stroke="#ef5b55" stroke-width="1" stroke-dasharray="8 4" opacity="0.4"/>

  <!-- Towering Shrouded Maternal Silhouette -->
  <path d="M 200 60 C 150 60, 110 100, 100 180 C 85 300, 60 340, 40 370 L 360 370 C 340 340, 315 300, 300 180 C 290 100, 250 60, 200 60 Z" fill="#111122" stroke="#c084fc" stroke-width="3"/>
  
  <!-- Obsidian Needle Arms Enveloping -->
  <path d="M 120 180 C 140 230, 160 280, 200 290 C 240 280, 260 230, 280 180" fill="none" stroke="#f1df76" stroke-width="3"/>
  <path d="M 120 180 L 160 270 L 190 280" fill="none" stroke="#ef5b55" stroke-width="2.5"/>
  <path d="M 280 180 L 240 270 L 210 280" fill="none" stroke="#ef5b55" stroke-width="2.5"/>

  <!-- Swaddled Blank Silhouette in Center -->
  <ellipse cx="200" cy="240" rx="35" ry="50" fill="#080811" stroke="#38bdf8" stroke-width="2"/>
  <circle cx="200" cy="215" r="14" fill="#1f2937" stroke="#38bdf8" stroke-width="1.5"/>

  <!-- Faceless Shroud Veil with Single Bleeding Stigmata -->
  <ellipse cx="200" cy="115" rx="32" ry="42" fill="#090914" stroke="#c084fc" stroke-width="2"/>
  <circle cx="200" cy="115" r="6" fill="#ef5b55" filter="url(#indigoGlow)"/>
  <path d="M 200 121 L 200 155" fill="none" stroke="#ef5b55" stroke-width="2.5"/>

  <!-- Entangling Cradle Ribbons -->
  <g stroke="#c084fc" stroke-width="1.5" fill="none" opacity="0.75" filter="url(#indigoGlow)">
    <path d="M 80 200 Q 200 230 320 200"/>
    <path d="M 70 260 Q 200 300 330 260"/>
    <path d="M 60 320 Q 200 370 340 320"/>
  </g>

  <!-- Classification Badge Overlay -->
  <rect x="26" y="26" width="90" height="26" rx="6" fill="#090d16" stroke="#c084fc" stroke-width="1.5"/>
  <text x="71" y="44" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">SE-005</text>
  <rect x="274" y="26" width="100" height="26" rx="6" fill="#090d16" stroke="#ef5b55" stroke-width="1.5"/>
  <text x="324" y="44" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">PHANTASM</text>
</svg>''',

        "se-007.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <radialGradient id="se007Bg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#1e293b" stop-opacity="0.9"/>
      <stop offset="70%" stop-color="#090e17" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#020408" stop-opacity="1"/>
    </radialGradient>
    <filter id="brumeGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <rect x="6" y="6" width="388" height="388" rx="20" fill="url(#se007Bg)" stroke="#38bdf8" stroke-width="2.5"/>
  <rect x="14" y="14" width="372" height="372" rx="14" fill="none" stroke="#71efaf" stroke-width="1" stroke-dasharray="8 4" opacity="0.4"/>

  <!-- Spectral Brume Vapor Clouds -->
  <g filter="url(#brumeGlow)" opacity="0.8">
    <ellipse cx="200" cy="200" rx="130" ry="80" fill="#38bdf8" opacity="0.25"/>
    <ellipse cx="160" cy="170" rx="90" ry="60" fill="#71efaf" opacity="0.2"/>
    <ellipse cx="240" cy="230" rx="100" ry="70" fill="#f8fafc" opacity="0.3"/>
  </g>

  <!-- Particulate Aerosol Swirls -->
  <path d="M 60 200 Q 140 120 220 180 T 340 160" fill="none" stroke="#38bdf8" stroke-width="3" opacity="0.8"/>
  <path d="M 70 240 Q 180 300 260 220 T 350 250" fill="none" stroke="#71efaf" stroke-width="2.5" opacity="0.8"/>
  <path d="M 100 150 Q 200 80 290 140 T 330 210" fill="none" stroke="#f1df76" stroke-width="2" opacity="0.7"/>

  <!-- Weeping Ocular Fog Suspensions -->
  <g stroke="#38bdf8" stroke-width="2" fill="#0f172a">
    <path d="M 150 170 Q 170 150 190 170 Q 170 190 150 170 Z"/>
    <circle cx="170" cy="170" r="4" fill="#38bdf8"/>
    
    <path d="M 210 210 Q 230 190 250 210 Q 230 230 210 210 Z"/>
    <circle cx="230" cy="210" r="4" fill="#71efaf"/>

    <path d="M 180 240 Q 200 220 220 240 Q 200 260 180 240 Z"/>
    <circle cx="200" cy="240" r="4" fill="#f1df76"/>
  </g>

  <!-- Condensed Droplets -->
  <path d="M 170 174 L 170 195" fill="none" stroke="#38bdf8" stroke-width="1.8"/>
  <path d="M 230 214 L 230 235" fill="none" stroke="#71efaf" stroke-width="1.8"/>

  <!-- Classification Badge Overlay -->
  <rect x="26" y="26" width="90" height="26" rx="6" fill="#090d16" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="71" y="44" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">SE-007</text>
  <rect x="284" y="26" width="90" height="26" rx="6" fill="#090d16" stroke="#71efaf" stroke-width="1.5"/>
  <text x="329" y="44" fill="#71efaf" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">AETHER</text>
</svg>''',

        "se-009.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <radialGradient id="se009Bg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#1e1b4b" stop-opacity="0.9"/>
      <stop offset="70%" stop-color="#0b0a1a" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#04030a" stop-opacity="1"/>
    </radialGradient>
    <filter id="azureGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <rect x="6" y="6" width="388" height="388" rx="20" fill="url(#se009Bg)" stroke="#38bdf8" stroke-width="2.5"/>
  <rect x="14" y="14" width="372" height="372" rx="14" fill="none" stroke="#c084fc" stroke-width="1" stroke-dasharray="8 4" opacity="0.4"/>

  <!-- Clockwork Loom Frame & Gearwork -->
  <g stroke="#c084fc" stroke-width="2" fill="#131127">
    <circle cx="200" cy="120" r="45" stroke-dasharray="6 4"/>
    <circle cx="200" cy="120" r="25"/>
    <line x1="155" y1="120" x2="245" y2="120"/>
    <line x1="200" y1="75" x2="200" y2="165"/>
  </g>

  <!-- Arachnid Clockwork Legs -->
  <g stroke="#38bdf8" stroke-width="3" fill="none">
    <path d="M 160 120 L 100 80 L 50 140 L 60 220"/>
    <path d="M 160 140 L 80 160 L 40 230 L 70 300"/>
    <path d="M 240 120 L 300 80 L 350 140 L 340 220"/>
    <path d="M 240 140 L 320 160 L 360 230 L 330 300"/>
  </g>

  <!-- Woven Memory Filaments & Severed Human Silhouettes -->
  <g filter="url(#azureGlow)" stroke="#38bdf8" stroke-width="1.8" opacity="0.85">
    <line x1="160" y1="140" x2="120" y2="340"/>
    <line x1="180" y1="155" x2="160" y2="360"/>
    <line x1="200" y1="165" x2="200" y2="370"/>
    <line x1="220" y1="155" x2="240" y2="360"/>
    <line x1="240" y1="140" x2="280" y2="340"/>
  </g>

  <!-- Severed Memory Silhouettes in Weave -->
  <g fill="#1e1b4b" stroke="#f1df76" stroke-width="1.5">
    <circle cx="160" cy="270" r="10"/>
    <path d="M 145 310 Q 160 285 175 310 Z"/>

    <circle cx="240" cy="270" r="10"/>
    <path d="M 225 310 Q 240 285 255 310 Z"/>
  </g>

  <!-- Central Azure Ocular Core -->
  <circle cx="200" cy="120" r="12" fill="#38bdf8" filter="url(#azureGlow)"/>

  <!-- Classification Badge Overlay -->
  <rect x="26" y="26" width="90" height="26" rx="6" fill="#090d16" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="71" y="44" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">SE-009</text>
  <rect x="274" y="26" width="100" height="26" rx="6" fill="#090d16" stroke="#f1df76" stroke-width="1.5"/>
  <text x="324" y="44" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">MORPHEAN</text>
</svg>''',

        "se-010.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <radialGradient id="se010Bg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#3b0764" stop-opacity="0.9"/>
      <stop offset="60%" stop-color="#18022b" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#06000b" stop-opacity="1"/>
    </radialGradient>
    <filter id="purpleGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <rect x="6" y="6" width="388" height="388" rx="20" fill="url(#se010Bg)" stroke="#c084fc" stroke-width="2.5"/>
  <rect x="14" y="14" width="372" height="372" rx="14" fill="none" stroke="#ef5b55" stroke-width="1" stroke-dasharray="8 4" opacity="0.4"/>

  <!-- Cosmic Singularity Vortex Rings -->
  <g filter="url(#purpleGlow)" fill="none">
    <ellipse cx="200" cy="200" rx="150" ry="50" stroke="#c084fc" stroke-width="2" transform="rotate(-25 200 200)"/>
    <ellipse cx="200" cy="200" rx="140" ry="45" stroke="#ef5b55" stroke-width="2.5" transform="rotate(35 200 200)"/>
    <ellipse cx="200" cy="200" rx="120" ry="40" stroke="#f1df76" stroke-width="2" transform="rotate(85 200 200)"/>
  </g>

  <!-- Central Black Hole Singularity -->
  <circle cx="200" cy="200" r="45" fill="#030005" stroke="#c084fc" stroke-width="3"/>
  <circle cx="200" cy="200" r="30" fill="#000000" stroke="#ef5b55" stroke-width="2"/>
  <circle cx="200" cy="200" r="10" fill="#f1df76" filter="url(#purpleGlow)"/>

  <!-- Shattered Floating Porcelain Masks Spiraling Inward -->
  <g stroke="#f8fafc" stroke-width="1.5" fill="#1e1b4b">
    <!-- Mask 1 Top Left -->
    <path d="M 100 120 Q 120 100 140 120 Q 130 150 110 140 Z"/>
    <circle cx="118" cy="122" r="3" fill="#ef5b55"/>
    
    <!-- Mask 2 Bottom Right -->
    <path d="M 280 270 Q 300 250 310 280 Q 290 300 270 285 Z"/>
    <circle cx="295" cy="275" r="3" fill="#38bdf8"/>

    <!-- Mask 3 Top Right -->
    <path d="M 270 110 Q 290 120 280 140 Q 255 130 260 115 Z"/>
  </g>

  <!-- Gravitational Pull Accents -->
  <g stroke="#f1df76" stroke-width="1" stroke-dasharray="3 3" opacity="0.7">
    <line x1="80" y1="80" x2="170" y2="170"/>
    <line x1="320" y1="320" x2="230" y2="230"/>
    <line x1="320" y1="80" x2="230" y2="170"/>
    <line x1="80" y1="320" x2="170" y2="230"/>
  </g>

  <!-- Classification Badge Overlay -->
  <rect x="26" y="26" width="90" height="26" rx="6" fill="#090d16" stroke="#c084fc" stroke-width="1.5"/>
  <text x="71" y="44" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">SE-010</text>
  <rect x="264" y="26" width="110" height="26" rx="6" fill="#090d16" stroke="#c084fc" stroke-width="1.5"/>
  <text x="319" y="44" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">APOCRYPHA</text>
</svg>''',

        "se-011.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <radialGradient id="se011Bg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#1e293b" stop-opacity="0.9"/>
      <stop offset="70%" stop-color="#0f172a" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#020617" stop-opacity="1"/>
    </radialGradient>
    <filter id="wallGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <rect x="6" y="6" width="388" height="388" rx="20" fill="url(#se011Bg)" stroke="#38bdf8" stroke-width="2.5"/>
  <rect x="14" y="14" width="372" height="372" rx="14" fill="none" stroke="#f1df76" stroke-width="1" stroke-dasharray="8 4" opacity="0.4"/>

  <!-- Brutalist Concrete Acoustic Slabs -->
  <rect x="70" y="80" width="80" height="240" fill="#182232" stroke="#38bdf8" stroke-width="2"/>
  <rect x="160" y="60" width="80" height="280" fill="#202d42" stroke="#f1df76" stroke-width="2.5"/>
  <rect x="250" y="80" width="80" height="240" fill="#182232" stroke="#38bdf8" stroke-width="2"/>

  <!-- Screaming Embedded Bas-Relief Faces -->
  <g fill="#0f172a" stroke="#38bdf8" stroke-width="1.8">
    <!-- Left Slab Faces -->
    <circle cx="110" cy="140" r="16"/>
    <ellipse cx="110" cy="145" rx="6" ry="9" fill="#020617" stroke="#38bdf8"/>
    
    <circle cx="110" cy="240" r="14"/>
    <ellipse cx="110" cy="244" rx="5" ry="8" fill="#020617" stroke="#38bdf8"/>

    <!-- Center Slab Agonized Faces -->
    <circle cx="200" cy="120" r="20" stroke="#f1df76"/>
    <ellipse cx="200" cy="126" rx="8" ry="12" fill="#020617" stroke="#f1df76"/>
    <circle cx="192" cy="114" r="3" fill="#f1df76"/>
    <circle cx="208" cy="114" r="3" fill="#f1df76"/>

    <circle cx="200" cy="220" r="22" stroke="#ef5b55"/>
    <ellipse cx="200" cy="228" rx="9" ry="14" fill="#020617" stroke="#ef5b55"/>

    <!-- Right Slab Faces -->
    <circle cx="290" cy="160" r="16"/>
    <ellipse cx="290" cy="165" rx="6" ry="9" fill="#020617" stroke="#38bdf8"/>
    
    <circle cx="290" cy="260" r="14"/>
    <ellipse cx="290" cy="264" rx="5" ry="8" fill="#020617" stroke="#38bdf8"/>
  </g>

  <!-- Acoustic Harmonic Vibration Waveforms -->
  <g filter="url(#wallGlow)" stroke="#38bdf8" stroke-width="2" fill="none" opacity="0.8">
    <path d="M 30 200 C 50 180, 50 220, 70 200"/>
    <path d="M 330 200 C 350 180, 350 220, 370 200"/>
    <path d="M 40 140 C 55 125, 55 155, 70 140"/>
    <path d="M 330 260 C 345 245, 345 275, 360 260"/>
  </g>

  <!-- Classification Badge Overlay -->
  <rect x="26" y="26" width="90" height="26" rx="6" fill="#090d16" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="71" y="44" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">SE-011</text>
  <rect x="284" y="26" width="90" height="26" rx="6" fill="#090d16" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="329" y="44" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">SOMNA</text>
</svg>''',

        "se-014.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <radialGradient id="se014Bg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#3a2505" stop-opacity="0.9"/>
      <stop offset="70%" stop-color="#190e02" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#080400" stop-opacity="1"/>
    </radialGradient>
    <filter id="goldGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <rect x="6" y="6" width="388" height="388" rx="20" fill="url(#se014Bg)" stroke="#f1df76" stroke-width="2.5"/>
  <rect x="14" y="14" width="372" height="372" rx="14" fill="none" stroke="#ef5b55" stroke-width="1" stroke-dasharray="8 4" opacity="0.4"/>

  <!-- Gaping Ledger Beast Silhouette -->
  <!-- Coin Scaled Body -->
  <path d="M 80 340 C 60 220, 100 120, 200 100 C 300 120, 340 220, 320 340 Z" fill="#1c1409" stroke="#f1df76" stroke-width="3"/>
  
  <!-- Massive Gaping Ledger Jaw -->
  <path d="M 120 160 Q 200 80 280 160 L 260 260 Q 200 320 140 260 Z" fill="#0a0602" stroke="#ef5b55" stroke-width="3"/>

  <!-- Molten Gold Teeth & Fangs -->
  <g fill="#f1df76" stroke="#b45309" stroke-width="1.5" filter="url(#goldGlow)">
    <polygon points="140,165 155,195 150,165"/>
    <polygon points="165,160 180,200 175,160"/>
    <polygon points="190,158 200,205 210,158"/>
    <polygon points="225,160 220,200 235,160"/>
    <polygon points="250,165 245,195 260,165"/>

    <!-- Bottom Teeth -->
    <polygon points="150,250 160,220 170,250"/>
    <polygon points="180,255 195,215 205,255"/>
    <polygon points="215,255 225,220 235,250"/>
    <polygon points="240,245 250,225 255,245"/>
  </g>

  <!-- Flowing Gold Coins & Dissolved Debt Ledgers In Throat -->
  <circle cx="200" cy="210" r="14" fill="#ef5b55" filter="url(#goldGlow)"/>
  <circle cx="180" cy="290" r="12" fill="#f1df76" stroke="#78350f" stroke-width="2"/>
  <circle cx="220" cy="295" r="10" fill="#f1df76" stroke="#78350f" stroke-width="2"/>
  <circle cx="200" cy="330" r="15" fill="#f1df76" stroke="#78350f" stroke-width="2"/>

  <!-- Scale Patterns on Sides -->
  <g stroke="#f1df76" stroke-width="1.5" fill="none" opacity="0.6">
    <path d="M 90 220 Q 110 200 130 220"/>
    <path d="M 85 250 Q 105 230 125 250"/>
    <path d="M 270 220 Q 290 200 310 220"/>
    <path d="M 275 250 Q 295 230 315 250"/>
  </g>

  <!-- Classification Badge Overlay -->
  <rect x="26" y="26" width="90" height="26" rx="6" fill="#090d16" stroke="#f1df76" stroke-width="1.5"/>
  <text x="71" y="44" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">SE-014</text>
  <rect x="274" y="26" width="100" height="26" rx="6" fill="#090d16" stroke="#ef5b55" stroke-width="1.5"/>
  <text x="324" y="44" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">PHANTASM</text>
</svg>''',

        "se-015.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <radialGradient id="se015Bg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#1f2937" stop-opacity="0.9"/>
      <stop offset="70%" stop-color="#0f172a" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#020617" stop-opacity="1"/>
    </radialGradient>
    <filter id="balanceGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <rect x="6" y="6" width="388" height="388" rx="20" fill="url(#se015Bg)" stroke="#f1df76" stroke-width="2.5"/>
  <rect x="14" y="14" width="372" height="372" rx="14" fill="none" stroke="#38bdf8" stroke-width="1" stroke-dasharray="8 4" opacity="0.4"/>

  <!-- Ornate Balance Scale Fulcrum & Pillar -->
  <rect x="194" y="80" width="12" height="250" fill="#222d3d" stroke="#f1df76" stroke-width="2"/>
  <polygon points="160,340 240,340 220,310 180,310" fill="#141c28" stroke="#f1df76" stroke-width="2.5"/>
  
  <!-- Scale Pivot Crown -->
  <circle cx="200" cy="80" r="16" fill="#0f172a" stroke="#f1df76" stroke-width="3"/>
  <circle cx="200" cy="80" r="6" fill="#ef5b55" filter="url(#balanceGlow)"/>

  <!-- Tilted Balance Beam -->
  <!-- Beam tilted slightly: left higher (x=80, y=95), right lower (x=320, y=125) -->
  <line x1="70" y1="95" x2="330" y2="125" stroke="#f1df76" stroke-width="4"/>

  <!-- Left Pan Strings & Dish (Obsidian Heart) -->
  <line x1="85" y1="97" x2="55" y2="190" stroke="#38bdf8" stroke-width="1.8"/>
  <line x1="85" y1="97" x2="115" y2="190" stroke="#38bdf8" stroke-width="1.8"/>
  <path d="M 45 190 Q 85 210 125 190 Z" fill="#0e1726" stroke="#f1df76" stroke-width="2"/>
  <!-- Obsidian Heart on Left Pan -->
  <path d="M 85 160 C 70 145, 60 165, 85 185 C 110 165, 100 145, 85 160 Z" fill="#18181b" stroke="#ef5b55" stroke-width="2" filter="url(#balanceGlow)"/>

  <!-- Right Pan Strings & Dish (Crystallized Tear Gems) -->
  <line x1="315" y1="123" x2="285" y2="230" stroke="#38bdf8" stroke-width="1.8"/>
  <line x1="315" y1="123" x2="345" y2="230" stroke="#38bdf8" stroke-width="1.8"/>
  <path d="M 275 230 Q 315 250 355 230 Z" fill="#0e1726" stroke="#f1df76" stroke-width="2"/>
  <!-- Glowing Crystallized Blue Tears on Right Pan -->
  <g fill="#38bdf8" stroke="#ffffff" stroke-width="1" filter="url(#balanceGlow)">
    <polygon points="315,190 325,210 315,225 305,210"/>
    <polygon points="300,205 308,220 300,228 292,220"/>
    <polygon points="330,205 338,220 330,228 322,220"/>
  </g>

  <!-- Han Aura Radiance -->
  <circle cx="200" cy="80" r="40" fill="none" stroke="#38bdf8" stroke-width="1" stroke-dasharray="3 3" opacity="0.6"/>

  <!-- Classification Badge Overlay -->
  <rect x="26" y="26" width="90" height="26" rx="6" fill="#090d16" stroke="#f1df76" stroke-width="1.5"/>
  <text x="71" y="44" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">SE-015</text>
  <rect x="274" y="26" width="100" height="26" rx="6" fill="#090d16" stroke="#f1df76" stroke-width="1.5"/>
  <text x="324" y="44" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">MORPHEAN</text>
</svg>'''
    }

    for fname, svg_content in entities.items():
        with open(os.path.join(entity_art_dir, fname), "w", encoding="utf-8") as f:
            f.write(svg_content)
    print(f"Generated {len(entities)} ultra-HD entity showcase SVGs!")

    # 2. DEPARTMENT FLOOR BLUEPRINTS SVGs (assets/layout/hand/blueprints/)
    floor_bp_dir = os.path.join(base_dir, "layout/hand/blueprints")
    os.makedirs(floor_bp_dir, exist_ok=True)

    floors = {
        "floor-1-neutral-blueprint.svg": ("FLOOR 01: NEUTRAL COMMAND", "Core Nexus & Sovereign Overrides", "#71efaf", "DIRECTOR MAJIN / SECRETARY SEIYON"),
        "floor-2-maws-keep-blueprint.svg": ("FLOOR 02: MAW'S KEEP", "M.A.W. Arsenal & Forging Vaults", "#ef5b55", "ARMORY DIRECTIVE & STRIKE SQUADS"),
        "floor-3-extraction-hall-blueprint.svg": ("FLOOR 03: EXTRACTION HALL", "Han-Flux Siphoning & Wells", "#38bdf8", "EXTRACTION LEAD ZYRAK"),
        "floor-4-insight-forge-blueprint.svg": ("FLOOR 04: INSIGHT FORGE", "Resonance Labs & Analysis Matrix", "#f1df76", "RESEARCH LEAD AYSHUK"),
        "floor-5-border-watch-blueprint.svg": ("FLOOR 05: BORDER WATCH", "High-Security Containment Matrix", "#ef5b55", "BORDER LEAD MELLDA"),
        "floor-6-deep-vault-blueprint.svg": ("FLOOR 06: DEEP VAULT", "Sub-Level Archive & Static Chambers", "#c084fc", "CONTAINMENT LEAD DEKAN / MARJUK"),
        "floor-7-shadow-corps-blueprint.svg": ("FLOOR 07: SHADOW CORPS", "Rapid Interception & Strike Cells", "#ef5b55", "THE OUTSIDER ISHALL"),
        "floor-8-gate-watch-blueprint.svg": ("FLOOR 08: GATE WATCH", "Desolate Ramparts & Void Grid", "#f1df76", "THE EXILE XYAN")
    }

    for bp_name, (title, sub, color, lead) in floors.items():
        bp_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400" width="100%" height="100%">
  <defs>
    <pattern id="gridPattern_{bp_name[:4]}" width="20" height="20" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="20" y2="0" stroke="#1e293b" stroke-width="0.8"/>
      <line x1="0" y1="0" x2="0" y2="20" stroke="#1e293b" stroke-width="0.8"/>
    </pattern>
    <radialGradient id="bgGlow_{bp_name[:4]}" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{color}" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#090d16" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <!-- Background -->
  <rect x="0" y="0" width="600" height="400" fill="#080c14"/>
  <rect x="0" y="0" width="600" height="400" fill="url(#gridPattern_{bp_name[:4]})"/>
  <circle cx="300" cy="200" r="220" fill="url(#bgGlow_{bp_name[:4]})"/>
  
  <!-- Outer Tactical Border -->
  <rect x="10" y="10" width="580" height="380" rx="10" fill="none" stroke="{color}" stroke-width="2"/>
  <rect x="16" y="16" width="568" height="368" rx="6" fill="none" stroke="#334155" stroke-width="1" stroke-dasharray="8 4"/>

  <!-- Blueprint Header Block -->
  <rect x="25" y="25" width="300" height="45" rx="4" fill="#0f172a" stroke="{color}" stroke-width="1.5"/>
  <text x="35" y="44" fill="{color}" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="bold">{title}</text>
  <text x="35" y="60" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="10">{sub}</text>

  <!-- Lead Badge -->
  <rect x="340" y="25" width="235" height="45" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="350" y="44" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold">COMMAND LEAD OVERSEER</text>
  <text x="350" y="60" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="11">{lead}</text>

  <!-- Tactical Floor Layout Grid -->
  <!-- Main Central Hall -->
  <rect x="200" y="120" width="200" height="160" fill="#0d1522" stroke="{color}" stroke-width="2"/>
  <text x="300" y="195" fill="#f8fafc" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">CENTRAL COMMAND HUB</text>
  <text x="300" y="215" fill="{color}" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">RESONANCE STABILIZER ACTIVE</text>

  <!-- Left Containment Wing -->
  <rect x="40" y="100" width="130" height="90" fill="#0f1a2e" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="105" y="140" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" text-anchor="middle">CELL BLOCK ALPHA</text>
  <text x="105" y="160" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="8" text-anchor="middle">ISOLATION SHIELDS</text>

  <rect x="40" y="210" width="130" height="90" fill="#0f1a2e" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="105" y="250" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" text-anchor="middle">CELL BLOCK BETA</text>
  <text x="105" y="270" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="8" text-anchor="middle">FLOW DAMPENERS</text>

  <!-- Right Operational Wing -->
  <rect x="430" y="100" width="130" height="90" fill="#0f1a2e" stroke="#f1df76" stroke-width="1.5"/>
  <text x="495" y="140" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" text-anchor="middle">EXTRACTION LAB</text>
  <text x="495" y="160" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="8" text-anchor="middle">SIPHON CONDUITS</text>

  <rect x="430" y="210" width="130" height="90" fill="#0f1a2e" stroke="#f1df76" stroke-width="1.5"/>
  <text x="495" y="250" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" text-anchor="middle">STAGING CORRIDOR</text>
  <text x="495" y="270" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="8" text-anchor="middle">RAPID SUPPRESSION</text>

  <!-- Connecting Corridors -->
  <line x1="170" y1="145" x2="200" y2="145" stroke="{color}" stroke-width="4"/>
  <line x1="170" y1="255" x2="200" y2="255" stroke="{color}" stroke-width="4"/>
  <line x1="400" y1="145" x2="430" y2="145" stroke="{color}" stroke-width="4"/>
  <line x1="400" y1="255" x2="430" y2="255" stroke="{color}" stroke-width="4"/>

  <!-- Evacuation Shafts / Elevators -->
  <rect x="270" y="300" width="60" height="60" fill="#1e1b4b" stroke="#c084fc" stroke-width="2"/>
  <text x="300" y="335" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold" text-anchor="middle">TRANSIT</text>

  <!-- Bottom Technical Footer -->
  <rect x="25" y="365" width="550" height="18" fill="#090d16" stroke="#1e293b" stroke-width="1"/>
  <text x="35" y="378" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="8">THE HAND OF CHANGE // FACILITY-01 ARCHITECTURAL REGISTRY // SECURITY CLEARANCE: LEVEL 5</text>
  <text x="565" y="378" fill="{color}" font-family="'JetBrains Mono', monospace" font-size="8" text-anchor="end">STATUS: NOMINAL</text>
</svg>'''
        with open(os.path.join(floor_bp_dir, bp_name), "w", encoding="utf-8") as f:
            f.write(bp_svg)
    print(f"Generated {len(floors)} department floor blueprints SVGs!")

    # 3. TECHNICAL INFOGRAPHICS SVGs (assets/diagrams/)
    diagram_dir = os.path.join(base_dir, "diagrams")
    os.makedirs(diagram_dir, exist_ok=True)

    # 3a. Han Energy Cycle Flowchart
    han_cycle_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="hanGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0c1322"/>
      <stop offset="100%" stop-color="#04070d"/>
    </linearGradient>
    <filter id="diagGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <rect x="6" y="6" width="788" height="438" rx="14" fill="url(#hanGrad)" stroke="#f1df76" stroke-width="2.5"/>
  <rect x="14" y="14" width="772" height="422" rx="10" fill="none" stroke="#38bdf8" stroke-width="1" stroke-dasharray="6 3" opacity="0.4"/>

  <text x="400" y="45" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="18" font-weight="bold" text-anchor="middle">HAN-FLUX RESONANCE &amp; EXTRACTION CYCLE</text>
  <text x="400" y="68" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">THE 4 PRIMORDIAL TRANSFORMATION PHASES IN FACILITY 01</text>

  <!-- 4 Phase Nodes -->
  <!-- Phase 1: Dohan (City Sorrow) -->
  <g transform="translate(60, 110)">
    <rect x="0" y="0" width="150" height="180" rx="8" fill="#0f172a" stroke="#f1df76" stroke-width="2"/>
    <text x="75" y="30" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">PHASE I: DOHAN</text>
    <text x="75" y="48" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">City Sorrow</text>
    <line x1="15" y1="60" x2="135" y2="60" stroke="#334155" stroke-width="1"/>
    <text x="15" y="80" fill="#e2e8f0" font-family="'JetBrains Mono', monospace" font-size="9">• Structural Han</text>
    <text x="15" y="100" fill="#e2e8f0" font-family="'JetBrains Mono', monospace" font-size="9">• Masonry Weep</text>
    <text x="15" y="120" fill="#e2e8f0" font-family="'JetBrains Mono', monospace" font-size="9">• Civic Debt Accum</text>
    <text x="15" y="150" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold">Yield: 10-25 Flux</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <path d="M 215 200 L 255 200" stroke="#f1df76" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
  <polygon points="260,200 248,193 248,207" fill="#f1df76"/>

  <!-- Phase 2: Oehan (Outside Sorrow) -->
  <g transform="translate(265, 110)">
    <rect x="0" y="0" width="150" height="180" rx="8" fill="#0f172a" stroke="#71efaf" stroke-width="2"/>
    <text x="75" y="30" fill="#71efaf" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">PHASE II: OEHAN</text>
    <text x="75" y="48" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">Outside Sorrow</text>
    <line x1="15" y1="60" x2="135" y2="60" stroke="#334155" stroke-width="1"/>
    <text x="15" y="80" fill="#e2e8f0" font-family="'JetBrains Mono', monospace" font-size="9">• Desolate Drift</text>
    <text x="15" y="100" fill="#e2e8f0" font-family="'JetBrains Mono', monospace" font-size="9">• Bio-Fluid Surge</text>
    <text x="15" y="120" fill="#e2e8f0" font-family="'JetBrains Mono', monospace" font-size="9">• Wilderness Tide</text>
    <text x="15" y="150" fill="#71efaf" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold">Yield: 30-55 Flux</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <polygon points="465,200 453,193 453,207" fill="#38bdf8"/>

  <!-- Phase 3: Chohan (Transcendent Sorrow) -->
  <g transform="translate(470, 110)">
    <rect x="0" y="0" width="150" height="180" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="75" y="30" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="bold" text-anchor="middle">PHASE III: CHOHAN</text>
    <text x="75" y="48" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">Transcendent Sorrow</text>
    <line x1="15" y1="60" x2="135" y2="60" stroke="#334155" stroke-width="1"/>
    <text x="15" y="80" fill="#e2e8f0" font-family="'JetBrains Mono', monospace" font-size="9">• High Resonance</text>
    <text x="15" y="100" fill="#e2e8f0" font-family="'JetBrains Mono', monospace" font-size="9">• M.A.W. Forging</text>
    <text x="15" y="120" fill="#e2e8f0" font-family="'JetBrains Mono', monospace" font-size="9">• Direct Extraction</text>
    <text x="15" y="150" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold">Yield: 60-90 Flux</text>
  </g>

  <!-- Arrow 3 -> 4 -->
  <polygon points="670,200 658,193 658,207" fill="#ef5b55"/>

  <!-- Phase 4: Absolvohan (Total Catharsis) -->
  <g transform="translate(675, 110)">
    <rect x="0" y="0" width="105" height="180" rx="8" fill="#0f172a" stroke="#ef5b55" stroke-width="2"/>
    <text x="52" y="30" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">ABSOLVOHAN</text>
    <text x="52" y="48" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="8" text-anchor="middle">Total Catharsis</text>
    <line x1="10" y1="60" x2="95" y2="60" stroke="#334155" stroke-width="1"/>
    <text x="10" y="80" fill="#e2e8f0" font-family="'JetBrains Mono', monospace" font-size="8">• Seed of Light</text>
    <text x="10" y="100" fill="#e2e8f0" font-family="'JetBrains Mono', monospace" font-size="8">• Cycle Reset</text>
    <text x="10" y="120" fill="#e2e8f0" font-family="'JetBrains Mono', monospace" font-size="8">• Core Release</text>
    <text x="10" y="150" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="bold">MAX EXTRACTION</text>
  </g>

  <!-- Bottom Interactive Note -->
  <rect x="60" y="330" width="720" height="75" rx="6" fill="#0d1524" stroke="#1e293b" stroke-width="1.5"/>
  <text x="80" y="355" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">TACTICAL EXTRACTION DIRECTIVE:</text>
  <text x="80" y="375" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="10">Han-Flux cannot be destroyed. Extraction siphons grief through the 4 Work Types into stable containment vats.</text>
  <text x="80" y="392" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="10">Failure to maintain Resonance Thresholds triggers a Sorrow Gauge breach and facility-wide meltdown alarm.</text>
</svg>'''

    with open(os.path.join(diagram_dir, "han_flux_resonance_cycle.svg"), "w", encoding="utf-8") as f:
        f.write(han_cycle_svg)

    # 3b. Four Work Types Matrix SVG
    work_matrix_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <defs>
    <linearGradient id="workBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0e1726"/>
      <stop offset="100%" stop-color="#050912"/>
    </linearGradient>
  </defs>

  <rect x="6" y="6" width="788" height="438" rx="14" fill="url(#workBg)" stroke="#38bdf8" stroke-width="2.5"/>
  <rect x="14" y="14" width="772" height="422" rx="10" fill="none" stroke="#f1df76" stroke-width="1" stroke-dasharray="6 3" opacity="0.4"/>

  <text x="400" y="45" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="18" font-weight="bold" text-anchor="middle">THE FOUR WORK TYPES OPERATIONAL MATRIX</text>
  <text x="400" y="68" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="11" text-anchor="middle">FACILITY-01 WORK SPECIALIZATION, AGENT ATTRIBUTE LINKAGE, AND RESISTANCE DYNAMICS</text>

  <!-- 4 Work Columns -->
  <!-- Instinct -->
  <g transform="translate(40, 95)">
    <rect x="0" y="0" width="170" height="230" rx="8" fill="#0f172a" stroke="#ef5b55" stroke-width="2"/>
    <text x="85" y="30" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="middle">INSTINCT (본능)</text>
    <text x="85" y="48" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">Primary: Fortitude (HP)</text>
    <line x1="15" y1="60" x2="155" y2="60" stroke="#334155" stroke-width="1"/>
    <text x="15" y="85" fill="#e2e8f0" font-family="'JetBrains Mono', monospace" font-size="10">Target Need: Physical</text>
    <text x="15" y="110" fill="#e2e8f0" font-family="'JetBrains Mono', monospace" font-size="10">Damage: Crimson (RED)</text>
    <text x="15" y="135" fill="#e2e8f0" font-family="'JetBrains Mono', monospace" font-size="10">Risk: Severe Trauma</text>
    <text x="15" y="160" fill="#e2e8f0" font-family="'JetBrains Mono', monospace" font-size="10">Affinity: Beast/Colossus</text>
    <rect x="15" y="180" width="140" height="35" rx="4" fill="#1e293b"/>
    <text x="85" y="202" fill="#ef5b55" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold" text-anchor="middle">SE-002 / SE-014 HIGH</text>
  </g>

  <!-- Insight -->
  <g transform="translate(225, 95)">
    <rect x="0" y="0" width="170" height="230" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <text x="85" y="30" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="middle">INSIGHT (통찰)</text>
    <text x="85" y="48" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">Primary: Prudence (SP)</text>
    <line x1="15" y1="60" x2="155" y2="60" stroke="#334155" stroke-width="1"/>
    <text x="15" y="85" fill="#e2e8f0" font-family="'JetBrains Mono', monospace" font-size="10">Target Need: Chamber</text>
    <text x="15" y="110" fill="#e2e8f0" font-family="'JetBrains Mono', monospace" font-size="10">Damage: Cyan (WHITE)</text>
    <text x="15" y="135" fill="#e2e8f0" font-family="'JetBrains Mono', monospace" font-size="10">Risk: Panic / Hallucination</text>
    <text x="15" y="160" fill="#e2e8f0" font-family="'JetBrains Mono', monospace" font-size="10">Affinity: Environmental</text>
    <rect x="15" y="180" width="140" height="35" rx="4" fill="#1e293b"/>
    <text x="85" y="202" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold" text-anchor="middle">SE-007 / SE-011 HIGH</text>
  </g>

  <!-- Attachment -->
  <g transform="translate(410, 95)">
    <rect x="0" y="0" width="170" height="230" rx="8" fill="#0f172a" stroke="#71efaf" stroke-width="2"/>
    <text x="85" y="30" fill="#71efaf" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="middle">ATTACHMENT (애착)</text>
    <text x="85" y="48" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">Primary: Temperance (SPD)</text>
    <line x1="15" y1="60" x2="155" y2="60" stroke="#334155" stroke-width="1"/>
    <text x="15" y="85" fill="#e2e8f0" font-family="'JetBrains Mono', monospace" font-size="10">Target Need: Social/Bond</text>
    <text x="15" y="110" fill="#e2e8f0" font-family="'JetBrains Mono', monospace" font-size="10">Damage: Emerald (BLACK)</text>
    <text x="15" y="135" fill="#e2e8f0" font-family="'JetBrains Mono', monospace" font-size="10">Risk: Parasitic Bonding</text>
    <text x="15" y="160" fill="#e2e8f0" font-family="'JetBrains Mono', monospace" font-size="10">Affinity: Sentient Relics</text>
    <rect x="15" y="180" width="140" height="35" rx="4" fill="#1e293b"/>
    <text x="85" y="202" fill="#71efaf" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold" text-anchor="middle">SE-001 / SE-005 HIGH</text>
  </g>

  <!-- Repression -->
  <g transform="translate(595, 95)">
    <rect x="0" y="0" width="165" height="230" rx="8" fill="#0f172a" stroke="#c084fc" stroke-width="2"/>
    <text x="82" y="30" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="bold" text-anchor="middle">REPRESSION (억압)</text>
    <text x="82" y="48" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">Primary: Justice (ATK)</text>
    <line x1="15" y1="60" x2="150" y2="60" stroke="#334155" stroke-width="1"/>
    <text x="15" y="85" fill="#e2e8f0" font-family="'JetBrains Mono', monospace" font-size="10">Target Need: Restraint</text>
    <text x="15" y="110" fill="#e2e8f0" font-family="'JetBrains Mono', monospace" font-size="10">Damage: Pale / Cosmic</text>
    <text x="15" y="135" fill="#e2e8f0" font-family="'JetBrains Mono', monospace" font-size="10">Risk: Immediate Breach</text>
    <text x="15" y="160" fill="#e2e8f0" font-family="'JetBrains Mono', monospace" font-size="10">Affinity: Cosmic Singularities</text>
    <rect x="15" y="180" width="135" height="35" rx="4" fill="#1e293b"/>
    <text x="82" y="202" fill="#c084fc" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold" text-anchor="middle">SE-010 / SE-015 HIGH</text>
  </g>

  <!-- Tactical Bottom Banner -->
  <rect x="40" y="345" width="720" height="70" rx="6" fill="#090d16" stroke="#253952" stroke-width="1.5"/>
  <text x="60" y="370" fill="#f1df76" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold">DIRECTOR'S WORK DISPATCH RULE:</text>
  <text x="60" y="390" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="10">Never assign an Agent with Fortitude &lt; Level III to SE-002 Repression. Mismatched work yields negative resonance box accumulation.</text>
</svg>'''

    with open(os.path.join(diagram_dir, "four_work_types_matrix.svg"), "w", encoding="utf-8") as f:
        f.write(work_matrix_svg)
    print("Generated all technical infographics SVGs!")

if __name__ == "__main__":
    build_all_ultra_svgs()
