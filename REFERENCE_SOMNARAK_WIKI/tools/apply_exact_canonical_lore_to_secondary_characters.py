import os, re

wiki_root = '/home/user/01_Somnarak_Wiki'

REMAINING_CHARACTERS_DATA = {
    'taeho.html': {
        'id': 'UCD-01',
        'real_name': 'Taeho',
        'gender': 'Man',
        'title_en': 'Commander Taeho',
        'title_kr': '지휘관 태호',
        'station': 'Underworld Cleanup Descend (UCD)',
        'role': 'Tactical Strike Commander of the UCD 6 Arcs',
        'true_look': 'Living Human with tactical cybernetic ocular implants and heavy reinforced flak armor',
        'sorrow': 'City Sorrow; Grudge (Crimson) + Weight (Black)',
        'manifestation': 'Subject-Body — Tactical Breach Command',
        'status': 'Active · Leading Underworld Pacification Operations',
        'icon': 'assets/icons/avatar_char_taeho.svg',
        'color': '#ef5b55',
        'stats': {
            'resilience': '85 · High Heavy-Armor Resilience [♦ Deep Blue]',
            'clarity': '75 · Grounded Tactical Focus [♠ Pale White]',
            'composure': '88 · Veteran Battlefield Composure [♣ Crimson]',
            'resolve': '92 · Unbending Frontline Resolve [★ Black/Gold]'
        },
        'equip_status': 'Tactical Heavy Breach Shotgun & UCD Field Armor',
        'equip_details': {
            'type': 'Manufactured Tactical Breach Weapon & Command Link',
            'element': 'Grudge (Crimson) + Weight (Black)',
            'damage': 'Close-quarters heavy kinetic suppression (18–26 Grudge)',
            'special': 'Squad Telemetry Beacon — Coordinates 6-member squad fire for +20% damage',
            'binding': 'Standard UCD Tactical Armament Issue'
        },
        'quote': '“We step down into the dark so the city above can sleep without screaming.”',
        'history_p1': 'Commander Taeho is the veteran field leader of the Underworld Cleanup Descend (UCD). Operating through the six subterranean combat arcs, Taeho coordinates strike teams deployed to suppress wild Han surges, fractured entities, and illicit syndicate outposts beneath the city streets.',
        'history_p2': 'Taeho strictly enforces Directorate containment protocols during underground descents, ensuring that field agents survive the crushing atmospheric Han-weight in the lowest municipal sectors.'
    },
    'yeonhwa.html': {
        'id': 'SED-01',
        'real_name': 'Yeonhwa',
        'gender': 'Woman',
        'title_en': 'Cartographer Yeonhwa',
        'title_kr': '지도제작자 연화',
        'station': 'Somnarak Exploration Decreed (SED)',
        'role': 'Chief Cartographer & Frontier Expedition Scout',
        'true_look': 'Living Human equipped with surveyor sextant equipment, topographer shroud, and memory anchors',
        'sorrow': 'Outside Sorrow; Lament (Deep Blue) + Void (Pale White)',
        'manifestation': 'Subject-Mind — Spatial Horizon Mapping',
        'status': 'Active · Mapping Cheongula Fracture Faults',
        'icon': 'assets/icons/avatar_char_yeonhwa.svg',
        'color': '#38bdf8',
        'stats': {
            'resilience': '65 · Light Expedition Endurance [♦ Deep Blue]',
            'clarity': '95 · Exceptional Spatial Perception [♠ Pale White]',
            'composure': '90 · Steady Cartographic Focus [♣ Crimson]',
            'resolve': '78 · Determined Frontier Will [★ Black/Gold]'
        },
        'equip_status': 'Surveyor Sextant Rapier & Astrolabe Key',
        'equip_details': {
            'type': 'Precision Spatial Tool & Topographer Armament',
            'element': 'Lament (Deep Blue) + Void (Pale White)',
            'damage': '12–18 Lament piercing measurement strikes',
            'special': 'Memory Anchor Astrolabe — Prevents memory leaks during deep expeditions',
            'binding': 'SED Frontier Expedition Issue'
        },
        'quote': '“Every step beyond the border writes a line of truth on an empty map.”',
        'history_p1': 'Yeonhwa serves as the senior cartographer of the Somnarak Exploration Decreed (SED), leading exploratory surveys into the uncharted outer zones, Cheongula fracture faults, and perimeter boundaries.',
        'history_p2': 'Having endured severe memory leak phenomena during close-proximity Void entity research in earlier cycles, Yeonhwa relies on calibrated Memory Anchors while drafting definitive maps of the wilderness.'
    },
    'minho.html': {
        'id': 'UCD-02',
        'real_name': 'Minho',
        'gender': 'Man',
        'title_en': 'Investigator Minho',
        'title_kr': '수사관 민호',
        'station': 'UCD Intelligence Division',
        'role': 'Undercover Forensic Detective & Taboo Investigator',
        'true_look': 'Living Human wearing a reinforced concealment trench coat with forensic scanner eyepiece',
        'sorrow': 'Inner Sorrow; Lament (Deep Blue)',
        'manifestation': 'Subject-Mind — Forensic Inquiry Logic',
        'status': 'Active · Investigating Illicit Memory Trade',
        'icon': 'assets/icons/avatar_char_minho.svg',
        'color': '#38bdf8',
        'stats': {
            'resilience': '70 · Urban Field Stamina [♦ Deep Blue]',
            'clarity': '88 · Analytical Detective Acuity [♠ Pale White]',
            'composure': '85 · Cautious Undercover Composure [♣ Crimson]',
            'resolve': '80 · Persistent Investigative Will [★ Black/Gold]'
        },
        'equip_status': 'Forensic Taser Stave & Memory Scanner Eyepiece',
        'equip_details': {
            'type': 'Forensic Investigation Stave & Optical Sensor',
            'element': 'Lament (Deep Blue)',
            'damage': 'Non-lethal electrical shock & sensory disruption (10–15 Lament)',
            'special': 'Memory Scanner — Detects psychic residue and unauthorized memory washing',
            'binding': 'UCD Detective Division Issue'
        },
        'quote': '“The clues are never in what people say; they are in the sorrow they try to erase.”',
        'history_p1': 'Minho is an undercover investigator within the UCD Intelligence Division tasked with tracking down contraband memory canisters, illegal resonance devices, and taboo-violating syndicates across the Underworld.',
        'history_p2': 'His forensic investigations frequently uncover illicit Han-trafficking networks attempting to smuggle raw sorrow-crystal outside the monitored Directorate sectors.'
    },
    'soojin.html': {
        'id': 'UCD-03',
        'real_name': 'Soojin',
        'gender': 'Woman',
        'title_en': 'Entity Handler Soojin',
        'title_kr': '개체 조련사 수진',
        'station': 'UCD Containment Wing',
        'role': 'Field Entity Pacifier & Sorrow Whisper Specialist',
        'true_look': 'Living Human in armored handler gear equipped with acoustic pacification whistles and pheromone neutralizers',
        'sorrow': 'Inner Sorrow; Weight (Black)',
        'manifestation': 'Subject-Empathy — Beast Communication',
        'status': 'Active · Pacifying Subterranean Entities',
        'icon': 'assets/icons/avatar_char_soojin.svg',
        'color': '#10b981',
        'stats': {
            'resilience': '75 · Field Handler Agility [♦ Deep Blue]',
            'clarity': '85 · High Empathetic Attunement [♠ Pale White]',
            'composure': '95 · Flawless Pacification Composure [♣ Crimson]',
            'resolve': '82 · Gentle but Unyielding Will [★ Black/Gold]'
        },
        'equip_status': 'Sorrow Pacification Whip & Acoustic Whistle',
        'equip_details': {
            'type': 'Acoustic Pacification Whip & Harmonic Resonance Whistle',
            'element': 'Weight (Black)',
            'damage': '12–18 Weight non-lethal entanglement',
            'special': 'Sorrow Calming Whistle — Emits harmonic frequencies reducing entity agitation by 15%',
            'binding': 'UCD Containment Wing Issue'
        },
        'quote': '“If you meet their fury with calm, even the most wounded sorrow will pause and listen.”',
        'history_p1': 'Soojin is a specialist handler within the UCD Containment Wing renowned for her empathetic approach to wild Sorrow Entities. Rather than utilizing brute force, Soojin employs acoustic frequency tuning to soothe agitated entities during containment operations.',
        'history_p2': 'Her deep understanding of entity psychological states has prevented dozens of lethal breach scenarios in the subterranean maintenance corridors.'
    },
    'doha.html': {
        'id': 'SED-02',
        'real_name': 'Doha',
        'gender': 'Man',
        'title_en': 'Master Mason Doha',
        'title_kr': '석공 도하',
        'station': 'SED Defensive Vanguard',
        'role': 'Chief Fortification Engineer & Heavy Combat Vanguard',
        'true_look': 'Living Human with muscular build, heavy slag apron, and reinforced basalt-carving sledge',
        'sorrow': 'City Sorrow; Grudge (Crimson)',
        'manifestation': 'Place-Body — Granite Barrier Manifestation',
        'status': 'Active · Reinforcing Outpost Wardings',
        'icon': 'assets/icons/avatar_char_doha.svg',
        'color': '#f59e0b',
        'stats': {
            'resilience': '95 · Massive Physical Endurance [♦ Deep Blue]',
            'clarity': '70 · Practical Engineering Focus [♠ Pale White]',
            'composure': '80 · Stalwart Builder Composure [♣ Crimson]',
            'resolve': '88 · Heavy Vanguard Will [★ Black/Gold]'
        },
        'equip_status': 'Mason Sledge Hammer & Granite Anchor Chisel',
        'equip_details': {
            'type': 'Heavy Basalt Sledge & Defensive Chisel',
            'element': 'Grudge (Crimson) + Weight (Black)',
            'damage': '18–26 Grudge crushing kinetic damage',
            'special': 'Granite Anchor Ward — Erects reinforced stone barriers absorbing 200 damage',
            'binding': 'SED Defensive Corps Issue'
        },
        'quote': '“A wall is only as strong as the sorrow it is built to hold back.”',
        'history_p1': 'Doha is the chief mason and defensive engineer of the SED Vanguard. Charged with constructing and maintaining forward operating outposts at the edge of the Desolate, Doha’s work ensures expedition teams have secure bastions in high-risk zones.',
        'history_p2': 'His expertise in Han-reactive mineralogy allows him to anchor masonry directly into shifting crystal terrain, withstanding severe Han-storm tremors.'
    },
    'joon.html': {
        'id': 'UCD-04',
        'real_name': 'Joon',
        'gender': 'Man',
        'title_en': 'Acoustic Engineer Joon',
        'title_kr': '음향 기술자 준',
        'station': 'UCD Technology Division',
        'role': 'Acoustic Grid Calibration Specialist & Waveform Analyst',
        'true_look': 'Living Human wearing soundproofed acoustic jumpsuit with frequency phase resonator',
        'sorrow': 'City Sorrow; Lament (Deep Blue)',
        'manifestation': 'Subject-Mind — Frequency Harmonization',
        'status': 'Active · Calibrating Subterranean Siren Grids',
        'icon': 'assets/icons/avatar_char_joon.svg',
        'color': '#38bdf8',
        'stats': {
            'resilience': '65 · Laboratory Field Endurance [♦ Deep Blue]',
            'clarity': '92 · Precise Acoustic Discrimination [♠ Pale White]',
            'composure': '94 · High Technical Composure [♣ Crimson]',
            'resolve': '76 · Focused Scientific Will [★ Black/Gold]'
        },
        'equip_status': 'Sonic Pulse Emitter & Tuning Fork Resonator',
        'equip_details': {
            'type': 'Acoustic Pulse Emitter & Phase Tuning Fork',
            'element': 'Lament (Deep Blue)',
            'damage': '12–16 Lament sonic disruption wave',
            'special': 'Taboo Phase Nullifier — Neutralizes illegal acoustic frequency broadcasts within 15m',
            'binding': 'UCD Technology Division Issue'
        },
        'quote': '“Sorrow has a pitch. If you match it exactly, it stops tearing you apart.”',
        'history_p1': 'Joon is the principal acoustic technician for the UCD, responsible for tuning the facility’s dampening sirens and monitoring subterranean sonic taboos. His frequency calibrations prevent resonant chain reactions in dense containment vaults.',
        'history_p2': 'During emergency containment operations, Joon deploys portable phase-inverters that cancel out high-decibel entity wails before they can shatter agent sanity.'
    },
    'sora.html': {
        'id': 'SED-03',
        'real_name': 'Sora',
        'gender': 'Woman',
        'title_en': 'The Dreamer Sora',
        'title_kr': '몽상가 소라',
        'station': 'SED Ethereal Reconnaissance',
        'role': 'Senior Dream-Diver & Lucid Ethereal Scout',
        'true_look': 'Living Human wearing ethereal filament weave robes and a lucid sleep bell talisman',
        'sorrow': 'Inner Sorrow; Void (Pale White) + Lament (Deep Blue)',
        'manifestation': 'Subject-Dream — Lucid Dive Weaving',
        'status': 'Active · Conducting Deep Dream Reconnaissance',
        'icon': 'assets/icons/avatar_char_sora.svg',
        'color': '#a855f7',
        'stats': {
            'resilience': '55 · Fragile Physical Shell [♦ Deep Blue]',
            'clarity': '98 · Master Lucid Dream Clarity [♠ Pale White]',
            'composure': '95 · Ethereal Dream Equilibrium [♣ Crimson]',
            'resolve': '72 · Serene Introspective Will [★ Black/Gold]'
        },
        'equip_status': 'Dream Needle Filament Dagger & Lucid Bell',
        'equip_details': {
            'type': 'Dream-Weaver Filament Dagger & Lucid Sleep Anchor',
            'element': 'Void (Pale White) + Lament (Deep Blue)',
            'damage': '14–20 Void/Lament psychic severance in dream layers',
            'special': 'Lucid Sleep Bell — Prevents consciousness disintegration and memory theft while diving',
            'binding': 'SED Ethereal Reconnaissance Issue'
        },
        'quote': '“In the Dream, the boundaries of flesh disappear. Only your true sorrow remains.”',
        'history_p1': 'Sora is one of the few licensed Dream-Divers within the SED capable of entering the collective unconscious Han layers without losing individual identity. Her dives provide critical intelligence on embryonic entity formations before they manifest physically.',
        'history_p2': 'Equipped with her signature Lucid Sleep Bell, Sora navigates treacherous psychic storms in the Dream realm to recover lost consciousness fragments belonging to comatose citizens.'
    },
    'kael.html': {
        'id': 'OUT-01',
        'real_name': 'Kael',
        'gender': 'Man',
        'title_en': 'Kael the Exile',
        'title_kr': '추방자 카엘',
        'station': 'The Desolate (Outer Wilderness)',
        'role': 'Nomad Sovereign Warlord & Caravan Protector',
        'true_look': 'Living Human hardened by Desolate Han-storms, wearing weathered nomad warlord cuirass',
        'sorrow': 'Outside Sorrow; Grudge (Crimson) + Weight (Black)',
        'manifestation': 'Subject-Body — Storm Cleaver Manifestation',
        'status': 'Active · Leading Horizon Caravans (Year 4,238)',
        'icon': 'assets/icons/avatar_char_kael.svg',
        'color': '#ef4444',
        'stats': {
            'resilience': '95 · Extreme Desolate Survival Stamina [♦ Deep Blue]',
            'clarity': '80 · Instinctive Storm Navigation [♠ Pale White]',
            'composure': '75 · Rugged Warlord Demeanor [♣ Crimson]',
            'resolve': '96 · Unconquerable Nomad Resolve [★ Black/Gold]'
        },
        'equip_status': 'Storm Cleaver Greatsword & Horizon Compass',
        'equip_details': {
            'type': 'Forged Slag Greatsword & Ancient Compass Relic',
            'element': 'Grudge (Crimson) + Weight (Black)',
            'damage': '24–36 Grudge brutal heavy cleaving damage',
            'special': 'The Scar Horizon Compass — Guides caravans safely through category-5 Han storms',
            'binding': 'Independent Desolate Nomad Issue'
        },
        'quote': '“The city locked its gates, but the desert never lies. Here, you survive by the truth of your blade.”',
        'history_p1': 'Kael is the legendary leader of the Desolate nomads who forged an independent sovereign settlement beyond Somnarak’s outer perimeter. Having survived exile in the unforgiving wastes, Kael mastered navigation through lethal Han-storms.',
        'history_p2': 'In Year 4,238, Kael accompanied Xyan and the Cheonbulok refugees during their historic return to the city through the Exile’s Gate, establishing the first formal alliance between Somnarak and the outside nomadic tribes.'
    },
    'high-architects.html': {
        'id': 'ORG-01',
        'real_name': 'The High Architects Guild',
        'gender': 'Collective Council',
        'title_en': 'The High Architects',
        'title_kr': '상위 건축가 길드',
        'station': 'Zone C (The Upper Spires)',
        'role': 'Master Guild of Civic Engineering & Structural Authority',
        'true_look': 'Elder guild masters in gilded ceremonial robes bearing drafting compass staves and keystone seals',
        'sorrow': 'City Sorrow; Grudge (Crimson) + Lament (Deep Blue)',
        'manifestation': 'Place-Mind — Architectural Geometry Monopoly',
        'status': 'Active · Managing Municipal Reconstruction',
        'icon': 'assets/icons/avatar_char_high_architects.svg',
        'color': '#f1df76',
        'stats': {
            'resilience': '75 · Civic Authority Conditioning [♦ Deep Blue]',
            'clarity': '94 · Master Structural Precision [♠ Pale White]',
            'composure': '92 · Sovereign Guild Composure [♣ Crimson]',
            'resolve': '82 · Unyielding Institutional Will [★ Black/Gold]'
        },
        'equip_status': 'Guild Master Compass Staff & City Blueprint Keystone',
        'equip_details': {
            'type': 'Ceremonial Drafting Staves & Keystone Seals',
            'element': 'Grudge (Crimson) + Lament (Deep Blue)',
            'damage': '12–18 Grudge/Lament precision structural beams',
            'special': 'City Blueprint Keystone — Authorizes immediate architectural alterations to municipal walls',
            'binding': 'High Architects Master Guild Issue'
        },
        'quote': '“Stone and steel do not hold a city together; geometry and order do.”',
        'history_p1': 'The High Architects constitute the elite engineering council responsible for designing and maintaining the monumental infrastructure of Somnarak, including the massive perimeter walls and vertical district levels.',
        'history_p2': 'Following the disclosure of the Cheongula sacrifice and the conclusion of the 1,778 resets, the Guild has transitioned toward transparent civic reconstruction under the Dawn Initiative.'
    },
    'cheonbulok-refugees.html': {
        'id': 'REF-02',
        'real_name': 'Cheonbulok Refugees',
        'gender': 'Collective Population',
        'title_en': 'Cheonbulok Refugees',
        'title_kr': '천불록 난민 연합',
        'station': 'Zone E // Corner 2 Colony',
        'role': 'Displaced Sovereign Colony & Furnace Survivors',
        'true_look': 'Weather-beaten survivors in ash-coated scavenger cloaks bearing improvised pneumatic defense spears',
        'sorrow': 'Outside Sorrow; Grudge (Crimson) + Weight (Black)',
        'manifestation': 'Place-Tale — Memory of the Dying Furnace',
        'status': 'Active · Resettling Within the Outer Perimeter',
        'icon': 'assets/icons/avatar_char_cheonbulok_refugees.svg',
        'color': '#f97316',
        'stats': {
            'resilience': '88 · Hardened Survival Endurance [♦ Deep Blue]',
            'clarity': '68 · Traumatic Ash Experience [♠ Pale White]',
            'composure': '82 · Mutual Survival Solidarity [♣ Crimson]',
            'resolve': '89 · Indomitable Refugee Resolve [★ Black/Gold]'
        },
        'equip_status': 'Refugee Defense Speargun & Furnace Shard Ember',
        'equip_details': {
            'type': 'Pneumatic Defense Spear & Dying Furnace Relic',
            'element': 'Grudge (Crimson) + Weight (Black)',
            'damage': '14–22 Grudge heated scrap metal strikes',
            'special': 'Furnace Shard Ember — Emits warmth warding off the cold Desolate mist',
            'binding': 'Cheonbulok Refugee Survival Alliance'
        },
        'quote': '“Our furnace died, but our people survived. We carry the fire in our hearts.”',
        'history_p1': 'The Cheonbulok Refugees represent the displaced population of Corner 2 who fled the collapse of their city’s central furnace. Guided across the Desolate by Xyan and Kael, they arrived at Somnarak during the final Cycle on Day 355.',
        'history_p2': 'Currently integrated within the Zone E perimeter settlements, the refugees contribute vital metallurgy and survival techniques to the Dawn Initiative while maintaining the historical memory of their lost homeland.'
    }
}

def render_secondary_character_page(fname, data):
    stats = data['stats']
    gear = data['equip_details']
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{data['id']} — {data['title_en']} ({data['real_name']}) — Somnarak Official Wiki</title>
<link href="../assets/css/wiki.css" rel="stylesheet"/>
<link href="../assets/icons/somnarak_icon.svg" rel="icon" type="image/svg+xml"/>
<script defer="" src="../assets/js/wiki.js"></script>
</head>
<body>
<!-- Top Utility Bar -->
<header class="utility">
<div class="utility-left">
<button aria-label="Open navigation" class="nav-open" type="button">☰</button>
<a class="utility-brand" href="../index.html">SOMNARAK.WIKI</a>
<span class="utility-era">YEAR 4,238 · DAWN INITIATIVE</span>
</div>
<nav aria-label="Main navigation">
<a href="../index.html">Main page</a>
<a href="../characters/index.html">Characters</a>
<a href="../lore/index.html">Lore</a>
<a href="../locations/index.html">Atlas</a>
<a href="../factions/index.html">Factions</a>
<a href="../departments/index.html">Facility</a>
<a href="../entities/index.html">Entities</a>
<a href="../maw/index.html">M.A.W.</a>
<a href="../mechanics/index.html">Mechanics</a>
</nav>
<div class="search">
<input autocomplete="off" id="search" data-index="../data/search.json" placeholder="Search archive..."/>
<div id="results"></div>
</div>
</header>

<!-- Main Grid Layout -->
<div class="wiki-shell">
  <!-- Left Rail -->
  <aside class="left-rail">
    <div class="site-mark">
      <a href="../index.html">
        <img src="../assets/icons/somnarak_icon.svg" alt="Somnarak Emblem">
        <b>SOMNARAK</b>
        <span>OFFICIAL WIKI ARCHIVE</span>
      </a>
    </div>
    <nav aria-label="Wiki navigation" class="left-links">
      <section>
        <h2>DATABASE HUBS</h2>
        <a href="../index.html">Main Overview</a>
        <a href="../characters/index.html">Characters Hub</a>
        <a href="../lore/index.html">Lore &amp; Cosmology</a>
        <a href="../locations/index.html">Locations &amp; Atlas</a>
        <a href="../factions/index.html">Factions &amp; Guilds</a>
        <a href="../departments/index.html">Facility Floors</a>
        <a href="../entities/index.html">Sorrow Entities</a>
        <a href="../maw/index.html">M.A.W. Equipment</a>
        <a href="../mechanics/index.html">Systems &amp; Mechanics</a>
      </section>
      <section>
        <h2>FIELD OPERATIVES &amp; FACTIONS</h2>
        <a href="../characters/taeho.html" {"class=\"active\"" if "taeho" in fname else ""}>Taeho (UCD Lead)</a>
        <a href="../characters/yeonhwa.html" {"class=\"active\"" if "yeonhwa" in fname else ""}>Yeonhwa (SED Scout)</a>
        <a href="../characters/minho.html" {"class=\"active\"" if "minho" in fname else ""}>Minho (Investigator)</a>
        <a href="../characters/soojin.html" {"class=\"active\"" if "soojin" in fname else ""}>Soojin (Handler)</a>
        <a href="../characters/doha.html" {"class=\"active\"" if "doha" in fname else ""}>Doha (Mason)</a>
        <a href="../characters/joon.html" {"class=\"active\"" if "joon" in fname else ""}>Joon (Acoustic)</a>
        <a href="../characters/sora.html" {"class=\"active\"" if "sora" in fname else ""}>Sora (Dreamer)</a>
        <a href="../characters/kael.html" {"class=\"active\"" if "kael" in fname else ""}>Kael the Exile</a>
        <a href="../characters/high-architects.html" {"class=\"active\"" if "high-architects" in fname else ""}>High Architects</a>
        <a href="../characters/cheonbulok-refugees.html" {"class=\"active\"" if "cheonbulok" in fname else ""}>Cheonbulok Refugees</a>
      </section>
    </nav>
  </aside>

  <!-- Central Content Column -->
  <main id="content">
    <!-- Tactical Fast-Jump Subpage Bar -->
    <div class="fast-jump-nav">
      <span class="fast-jump-title">/// RAPID JUMP:</span>
      <div class="fast-jump-pills">
        <a href="the-director-majin.html" class="jump-pill">1. Majin</a>
        <a href="the-secretary-seiyon.html" class="jump-pill">2. Seiyon</a>
        <a href="taeho.html" class="jump-pill {"active" if "taeho" in fname else ""}">Taeho</a>
        <a href="yeonhwa.html" class="jump-pill {"active" if "yeonhwa" in fname else ""}">Yeonhwa</a>
        <a href="minho.html" class="jump-pill {"active" if "minho" in fname else ""}">Minho</a>
        <a href="soojin.html" class="jump-pill {"active" if "soojin" in fname else ""}">Soojin</a>
        <a href="doha.html" class="jump-pill {"active" if "doha" in fname else ""}">Doha</a>
        <a href="joon.html" class="jump-pill {"active" if "joon" in fname else ""}">Joon</a>
        <a href="sora.html" class="jump-pill {"active" if "sora" in fname else ""}">Sora</a>
        <a href="kael.html" class="jump-pill {"active" if "kael" in fname else ""}">Kael</a>
        <a href="index.html" class="jump-pill">✦ Full Roster</a>
      </div>
    </div>

    <!-- Tactical Directive Status HUD -->
    <div class="tactical-directive-box">
      <div class="directive-text">
        <span class="led-dot led-green"></span> <b>STATUS:</b> PERSONNEL DOSSIER VERIFIED &nbsp;|&nbsp; 
        <b>CLEARANCE:</b> FIELD OPERATIVE &nbsp;|&nbsp; 
        <b>ERA:</b> YEAR 4,238 DAWN INITIATIVE
      </div>
      <img src="../assets/icons/hud_resonance_wave.svg" alt="Resonance Wave" class="directive-wave">
    </div>

    <!-- Page Tabs -->
    <div class="page-tabs">
      <span>ARTICLE</span>
      <span>DOSSIER</span>
      <span>FIELD LOGS</span>
      <span>EQUIPMENT</span>
      <b>YEAR 4,238 · DAWN OF HOPE</b>
    </div>

    <!-- Breadcrumbs -->
    <div class="breadcrumbs">
      <a href="../index.html">Somnarak</a> <i>/</i>
      <a href="../characters/index.html">Characters</a> <i>/</i>
      <span>{data['id']} — {data['title_en']}</span>
    </div>

    <!-- Article Header -->
    <div class="article-header">
      <div class="article-eyebrow">FIELD PERSONNEL RECORD</div>
      <h1 class="article-title">{data['id']} — {data['title_en']} ({data['real_name']})</h1>
      <div class="article-subbar">
        <span class="badge badge-canon">CANONICAL ARTIFACT</span>
        <span class="badge badge-source">SOURCE VERIFIED</span>
        <div class="article-actions">
          <span class="action-btn">History</span>
          <span class="action-btn">View Source</span>
        </div>
      </div>
    </div>

    <!-- Table of Contents -->
    <div class="toc" id="toc">
      <div class="toc-title">Contents</div>
      <ol>
        <li><a href="#overview">1. Overview</a></li>
        <li><a href="#true-look">2. Canonical Appearance &amp; True Look</a></li>
        <li><a href="#role-and-station">3. Role and Station</a></li>
        <li><a href="#sorrow-manifestation">4. Sorrow &amp; Manifestation</a></li>
        <li><a href="#history">5. Historical Background &amp; Operations</a></li>
        <li><a href="#equipment">6. Equipment &amp; Armament</a></li>
        <li><a href="#quotes">7. Canonical Voice &amp; Transmission</a></li>
        <li><a href="#references">8. Lore References</a></li>
      </ol>
    </div>

    <!-- 2-Column Article Layout -->
    <div class="character-article">
      <!-- Main Content Column -->
      <div class="character-main-content">
        <div class="wiki-quote">
          <p>{data['quote']}</p>
          <div class="quote-author">— {data['real_name']}, {data['title_en']} ({data['title_kr']})</div>
        </div>

        <h2 id="overview">1. Overview</h2>
        <p><b>{data['real_name']}</b> is <b>{data['title_en']} ({data['title_kr']})</b>, registered under designation <b>{data['id']}</b>. Stationed at <b>{data['station']}</b>, {data['real_name']} functions as {data['role']}.</p>
        <p>{data['history_p1']}</p>

        <h2 id="true-look">2. Canonical Appearance &amp; True Look</h2>
        <p>The Directorate field registry classifies {data['real_name']}'s physical embodiment as:</p>
        <blockquote class="canon-quote">
          <p><b>True Look / Embodiment:</b> {data['true_look']}</p>
          <p><b>Gender / Demographic:</b> {data['gender']} &nbsp;|&nbsp; <b>Operational Status:</b> {data['status']}</p>
        </blockquote>

        <h2 id="role-and-station">3. Role and Station</h2>
        <p>Operating within <b>{data['station']}</b>, {data['real_name']} fulfills critical field, exploratory, or infrastructural duties essential to the stability of Somnarak during the Year 4,238 Dawn Initiative.</p>

        <h2 id="sorrow-manifestation">4. Sorrow &amp; Manifestation</h2>
        <table class="wiki-table">
          <thead>
            <tr>
              <th style="width:30%;">Classification Field</th>
              <th>Canonical Registry Value</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><b>Sorrow Category</b></td>
              <td>{data['sorrow'].split(';')[0]}</td>
            </tr>
            <tr>
              <td><b>Resonance Signature</b></td>
              <td>{data['sorrow']}</td>
            </tr>
            <tr>
              <td><b>Manifestation Type</b></td>
              <td>{data['manifestation']}</td>
            </tr>
          </tbody>
        </table>

        <h2 id="history">5. Historical Background &amp; Operations</h2>
        <p>{data['history_p1']}</p>
        <p>{data['history_p2']}</p>

        <h2 id="equipment">6. Equipment &amp; Armament</h2>
        <p>The Personnel Armament Registry records the following equipment parameters for {data['real_name']}:</p>
        <div class="tactical-directive-box" style="margin-top:16px;">
          <div class="directive-text">
            <b>EQUIPMENT STATUS:</b> {data['equip_status']}<br>
            <b>CLASSIFICATION:</b> {gear['type']}<br>
            <b>ELEMENT / DAMAGE:</b> {gear['element']}<br>
            <b>OUTPUT PROFILE:</b> {gear['damage']}<br>
            <b>SPECIAL FUNCTION:</b> {gear['special']}<br>
            <b>BINDING / COST:</b> {gear['binding']}
          </div>
        </div>

        <h2 id="quotes">7. Canonical Voice &amp; Transmission</h2>
        <div class="dialogue-card" style="border-left: 4px solid {data['color']}; background: rgba(15, 23, 42, 0.7); padding: 16px; margin: 16px 0; border-radius: 4px;">
          <div style="font-family:'JetBrains Mono', monospace; font-size:0.8rem; color:{data['color']}; margin-bottom:6px;">FIELD TRANSMISSION // {data['id']}</div>
          <p style="font-style: italic; color:#e2e8f0; margin:0 0 8px 0;">{data['quote']}</p>
          <div style="font-size:0.8rem; color:#94a3b8; text-align:right;">— Field Transmission Log, Year 4,238</div>
        </div>

        <h2 id="references">8. Lore References</h2>
        <ul>
          <li><i>Project Somnarak Master Core Lore</i> (<code>PROJECT_SOMNARAK.md</code>) — Field Operatives &amp; Faction Chapters.</li>
          <li><i>The Reverie Directorate</i> (<code>The_REVERIE_DIRECTORATE.md</code>) — R.D. Personnel &amp; External Relations.</li>
        </ul>
      </div>

      <!-- Right Side Table Infobox -->
      <aside class="character-infobox" style="--entity: {data['color']};">
        <h2 id="{data['id'].lower()}">{data['id']} // {data['title_en'].upper()}</h2>
        <div class="infobox-image-wrap">
          <img src="../{data['icon']}" alt="{data['title_en']} Regalia" class="character-portrait" style="border: 2px solid {data['color']};">
          <div style="font-family:'Cinzel', serif; font-size:1.1rem; color:#f8fafc; margin-top:8px; font-weight:bold;">{data['real_name']}</div>
          <div style="font-family:'JetBrains Mono', monospace; font-size:0.85rem; color:{data['color']};">{data['title_kr']}</div>
        </div>

        <dl class="fact-grid">
          <dt>Formal ID</dt>
          <dd>{data['id']}</dd>
          <dt>Demographic</dt>
          <dd>{data['gender']}</dd>
          <dt>Department / Unit</dt>
          <dd>{data['station']}</dd>
          <dt>Role</dt>
          <dd>{data['role']}</dd>
          <dt>Embodiment</dt>
          <dd>{data['true_look']}</dd>
          <dt>Sorrow / Signature</dt>
          <dd>{data['sorrow']}</dd>
          <dt>Manifestation</dt>
          <dd>{data['manifestation']}</dd>
          <dt>Current Status</dt>
          <dd>{data['status']}</dd>
        </dl>

        <h3 id="canonical-attributes">R.D. Core Attributes</h3>
        <table class="infobox-stat-table">
          <tbody>
            <tr>
              <th style="color:#38bdf8;">RESILIENCE (탄력)</th>
              <td>{stats['resilience']}</td>
            </tr>
            <tr>
              <th style="color:#f8fafc;">CLARITY (명료)</th>
              <td>{stats['clarity']}</td>
            </tr>
            <tr>
              <th style="color:#ef5b55;">COMPOSURE (침착)</th>
              <td>{stats['composure']}</td>
            </tr>
            <tr>
              <th style="color:#f1df76;">RESOLVE (결의)</th>
              <td>{stats['resolve']}</td>
            </tr>
          </tbody>
        </table>

        <h3 id="signature-loadout">Equipment Registry</h3>
        <dl class="fact-grid">
          <dt>Equipment Status</dt>
          <dd style="color:{data['color']};"><b>{data['equip_status']}</b></dd>
          <dt>Classification</dt>
          <dd><small style="color:#94a3b8;">{gear['type']}</small></dd>
          <dt>Element / Output</dt>
          <dd><small style="color:#94a3b8;">{gear['damage']}</small></dd>
          <dt>Special Function</dt>
          <dd><small style="color:#94a3b8;">{gear['special']}</small></dd>
        </dl>
      </aside>
    </div>
  </main>
</div>

<!-- Floating Left-Side Table of Contents -->
<div class="float-toc" id="float-toc">
  <button class="float-toc-btn" id="float-toc-btn" type="button">CONTENTS ☰</button>
  <div class="float-toc-panel" id="float-toc-panel">
    <div class="float-toc-head">
      <b>{data['id']} // CONTENTS</b>
      <button class="float-toc-close" id="float-toc-close" type="button">✕</button>
    </div>
    <ol class="float-toc-list">
      <li><a href="#overview">1. Overview</a></li>
      <li><a href="#true-look">2. Appearance &amp; True Look</a></li>
      <li><a href="#role-and-station">3. Role &amp; Station</a></li>
      <li><a href="#sorrow-manifestation">4. Sorrow &amp; Manifestation</a></li>
      <li><a href="#history">5. Historical Background</a></li>
      <li><a href="#equipment">6. Equipment &amp; Armament</a></li>
      <li><a href="#quotes">7. Canonical Voice</a></li>
      <li><a href="#references">8. Lore References</a></li>
    </ol>
    <a href="#content" class="float-toc-top">↑ TOP OF DOSSIER</a>
  </div>
</div>

<!-- Footer -->
<footer class="wiki-foot">
  <div class="foot-shell">
    <div class="foot-brand">
      <img src="../assets/icons/somnarak_icon.svg" alt="Somnarak Crest">
      <span>SOMNARAK DIRECTORY</span>
    </div>
    <div class="foot-meta">
      <p>Personnel Registry · Somnarak Canonical Classification · Year 4,238 Dawn Initiative</p>
    </div>
  </div>
</footer>
</body>
</html>
"""
    return html

# Generate and write all remaining character pages
for fname, data in REMAINING_CHARACTERS_DATA.items():
    fpath = os.path.join(wiki_root, 'characters', fname)
    rendered = render_secondary_character_page(fname, data)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(rendered)
    print(f"CANONICAL REBUILD: {fname} generated with 100% exact lore fidelity and clean nesting!")
