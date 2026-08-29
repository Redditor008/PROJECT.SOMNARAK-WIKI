import os, re, glob
from bs4 import BeautifulSoup

wiki_root = '/home/user/01_Somnarak_Wiki'

# CANONICAL REVERIE DIRECTORATE CHARACTER DATA
CHARACTERS_CANON_DATA = {
    'the-director-majin.html': {
        'id': 'CORE-01',
        'title_en': 'Director Majin',
        'title_kr': '관장 마진',
        'dept': 'Executive Suite // Floor 1 & Floor 8 Central',
        'clearance': 'Level 5 Sovereign Overseer',
        'resonance': 'Dawn Absolvohan & Weight (528 Hz)',
        'status': 'Active · Fused Ω-M.A.W. Sovereign',
        'icon': 'assets/icons/avatar_core_majin.svg',
        'color': '#f1df76',
        'stats': {
            'resilience': 'Level V (EX) · 140 HP [♦ Deep Blue]',
            'clarity': 'Level V (EX) · 150 SP [♠ Pale White]',
            'composure': 'Level V (EX) · 100% Work Efficiency [♣ Crimson]',
            'resolve': 'Level V (EX) · 1.5s Attack Interval [★ Black/Gold]'
        },
        'signature_gear': {
            'weapon_title': 'Reaper Hungered (Ω-M.A.W. Fused Scythe)',
            'weapon_desc': '10–20 Grudge direct + 3 Lament/s for 10s (Pierce line through 3 targets, 100%→70%→50% falloff).',
            'special_title': 'Phantom Reptile Beast (Special Burst)',
            'special_desc': '999 Weight (Black) damage bite + 5s Room Slowness aura (Cost: 90% HP + 90% SP).',
            'uniform_title': 'Director\'s Imperial Regalia Shroud',
            'uniform_desc': 'Irreversible sovereign fusion armor; internalizes operational Han exchanges.'
        }
    },
    'the-secretary-seiyon.html': {
        'id': 'CORE-02',
        'title_en': 'Secretary Seiyon',
        'title_kr': '비서 세이연',
        'dept': 'Administrative Intelligence // Floor 8 Gate Watch',
        'clearance': 'Level 5 High Administrator',
        'resonance': 'Harmonic Logic (440 Hz)',
        'status': 'Active · AI Construct Synced',
        'icon': 'assets/icons/avatar_core_seiyon.svg',
        'color': '#38bdf8',
        'stats': {
            'resilience': 'Level III (Normal) · 90 HP [♦ Deep Blue]',
            'clarity': 'Level V (EX) · 160 SP [♠ Pale White]',
            'composure': 'Level V (EX) · 100% Protocol Focus [♣ Crimson]',
            'resolve': 'Level III (Normal) · 2.0s Action Interval [★ Black/Gold]'
        },
        'signature_gear': {
            'weapon_title': 'Logic Grid Stave (Manufactured Terminal Tool)',
            'weapon_desc': 'Emits high-frequency Lament dampening pulses across administrative terminals.',
            'special_title': 'Year 4233 Awakening Memory Crystal',
            'special_desc': 'Preserves pre-Cycle archival records against civic memory washes.',
            'uniform_title': 'Directorate Secretary Chiffon Uniform',
            'uniform_desc': 'Insulated against acoustic and psychic interference (0.5 Lament resistance).'
        }
    },
    'the-containment-lead-dekan.html': {
        'id': 'CORE-03',
        'title_en': 'Containment Lead Dekan',
        'title_kr': '감금 책임자 데칸',
        'dept': 'Floor 1 // Neutral Core',
        'clearance': 'Level 4 Senior Containment Lead',
        'resonance': 'Basalt Dampening (120 Hz)',
        'status': 'Active · Sector 1 Stabilized',
        'icon': 'assets/icons/avatar_core_dekan.svg',
        'color': '#f1df76',
        'stats': {
            'resilience': 'Level V (EX) · 130 HP [♦ Deep Blue]',
            'clarity': 'Level IV (Master) · 110 SP [♠ Pale White]',
            'composure': 'Level V (EX) · 95% Work Stability [♣ Crimson]',
            'resolve': 'Level III (Normal) · 2.2s Combat Speed [★ Black/Gold]'
        },
        'signature_gear': {
            'weapon_title': 'Trench Barricade Shield & Kinetic Mace',
            'weapon_desc': 'Heavy kinetic bash (Grudge 14–22); deploys mobile acoustic blast wall.',
            'special_title': 'Acoustic Dampening Gate Lock',
            'special_desc': 'Instantly resets containment chamber resonance frequency upon breach alert.',
            'uniform_title': 'Lead Containment Cuirass',
            'uniform_desc': 'Heavy lead-lined ballistic armor (0.4 Grudge resistance).'
        }
    },
    'the-extraction-lead-zyrak.html': {
        'id': 'CORE-04',
        'title_en': 'Extraction Lead Zyrak',
        'title_kr': '추출 책임자 지락',
        'dept': 'Floor 2 // Maw\'s Keep',
        'clearance': 'Level 4 Senior Extraction Lead',
        'resonance': 'Siphon Resonance (280 Hz)',
        'status': 'Active · M.A.W. Forge Operational',
        'icon': 'assets/icons/avatar_core_zyrak.svg',
        'color': '#ef5b55',
        'stats': {
            'resilience': 'Level IV (Master) · 120 HP [♦ Deep Blue]',
            'clarity': 'Level IV (Master) · 115 SP [♠ Pale White]',
            'composure': 'Level V (EX) · 95% Extraction Accuracy [♣ Crimson]',
            'resolve': 'Level IV (Master) · 1.8s Combat Speed [★ Black/Gold]'
        },
        'signature_gear': {
            'weapon_title': 'Foundry Heavy Forge Maul',
            'weapon_desc': 'Strikes with concentrated Han kinetic impact (Grudge/Weight 16–25).',
            'special_title': 'Han Fluid Siphon Dial Array',
            'special_desc': 'Accelerates M.A.W. equipment extraction rate by +25% during Communion.',
            'uniform_title': 'Foundry Basalt Smelter Apron',
            'uniform_desc': 'Thermal and caustic effluent proofing (0.5 Weight resistance).'
        }
    },
    'the-research-lead-ayshuk.html': {
        'id': 'CORE-05',
        'title_en': 'Research Lead Ayshuk',
        'title_kr': '연구 책임자 아이슉',
        'dept': 'Floor 3 // Insight Forge',
        'clearance': 'Level 4 Senior Research Lead',
        'resonance': 'Spectral Prism (620 Hz)',
        'status': 'Active · Observation Analysis Online',
        'icon': 'assets/icons/avatar_core_ayshuk.svg',
        'color': '#38bdf8',
        'stats': {
            'resilience': 'Level III (Normal) · 85 HP [♦ Deep Blue]',
            'clarity': 'Level V (EX) · 145 SP [♠ Pale White]',
            'composure': 'Level V (EX) · 100% Analysis Focus [♣ Crimson]',
            'resolve': 'Level III (Normal) · 2.4s Combat Speed [★ Black/Gold]'
        },
        'signature_gear': {
            'weapon_title': 'Prism Analysis Scalpel Stave',
            'weapon_desc': 'Dissects entity behavioral waveforms (Lament 10–16 mental focus).',
            'special_title': 'Resonance Microscope Ocular Lens',
            'special_desc': 'Reveals hidden Observation Levels and breach triggers 2x faster.',
            'uniform_title': 'Insulated Research Shroud',
            'uniform_desc': 'High psychic resistance fabric (0.5 Lament / 0.7 Void resistance).'
        }
    },
    'the-border-lead-mellda.html': {
        'id': 'CORE-06',
        'title_en': 'Border Lead Mellda',
        'title_kr': '경계 책임자 멜다',
        'dept': 'Floor 4 // Shadow Corps',
        'clearance': 'Level 4 Senior Security Lead',
        'resonance': 'Kinetic Weight Strike (180 Hz)',
        'status': 'Active · Border Sentinel Primed',
        'icon': 'assets/icons/avatar_core_mellda.svg',
        'color': '#f97316',
        'stats': {
            'resilience': 'Level V (EX) · 135 HP [♦ Deep Blue]',
            'clarity': 'Level III (Normal) · 95 SP [♠ Pale White]',
            'composure': 'Level IV (Master) · 85% Combat Composure [♣ Crimson]',
            'resolve': 'Level V (EX) · 1.2s Rapid Strike [★ Black/Gold]'
        },
        'signature_gear': {
            'weapon_title': 'Threshold Vow (δ-Equivalent Integrated Cyborg Weapon)',
            'weapon_desc': '6–16 Weight direct + 2 Grudge/s for 10s (Pierce line through 3 targets, Room range).',
            'special_title': 'Singular Weight Wave (Special Pulse)',
            'special_desc': '25 Weight (Black) linear shockwave through 3 targets (15s recharge).',
            'uniform_title': 'Integrated Cyborg Armor Frame',
            'uniform_desc': 'Reinforced border defense plating (0.4 Grudge / 0.6 Weight resistance).'
        }
    },
    'the-archive-lead-marjuk.html': {
        'id': 'CORE-07',
        'title_en': 'Archive Lead Marjuk',
        'title_kr': '기록 책임자 마르죽',
        'dept': 'Floor 5 // Deep Vault',
        'clearance': 'Level 4 Senior Archive Lead',
        'resonance': 'Cryogenic Void (95 Hz)',
        'status': 'Active · Cryo Preserved',
        'icon': 'assets/icons/avatar_core_marjuk.svg',
        'color': '#cbd5e1',
        'stats': {
            'resilience': 'Level IV (Master) · 105 HP [♦ Deep Blue]',
            'clarity': 'Level V (EX) · 150 SP [♠ Pale White]',
            'composure': 'Level IV (Master) · 90% Archival Focus [♣ Crimson]',
            'resolve': 'Level III (Normal) · 2.5s Action Interval [★ Black/Gold]'
        },
        'signature_gear': {
            'weapon_title': 'Basalt Scribe Obsidian Quill',
            'weapon_desc': 'Carves immutable historical records (Void 12–18 existential damage).',
            'special_title': 'Basalt Tablet of 1,778 Cycles',
            'special_desc': 'Holds memory records of all 1,778 facility resets without memory degradation.',
            'uniform_title': 'Cryo Vault Insulation Shroud',
            'uniform_desc': 'Absolute zero cryogenic barrier (0.4 Void / 0.6 Lament resistance).'
        }
    },
    'the-outsider-ishall.html': {
        'id': 'CORE-08',
        'title_en': 'The Outsider Ishall',
        'title_kr': '외부인 이샬',
        'dept': 'Floor 6 // Cryo Archive',
        'clearance': 'Level 4 External Core Lead',
        'resonance': 'Android Sync (360 Hz)',
        'status': 'Active · Stage 1 Corrosion Monitored',
        'icon': 'assets/icons/avatar_core_ishall.svg',
        'color': '#10b981',
        'stats': {
            'resilience': 'Level IV (Master) · 115 HP [♦ Deep Blue]',
            'clarity': 'Level IV (Master) · 120 SP [♠ Pale White]',
            'composure': 'Level IV (Master) · 90% Sensorium Balance [♣ Crimson]',
            'resolve': 'Level IV (Master) · 1.6s Combat Speed [★ Black/Gold]'
        },
        'signature_gear': {
            'weapon_title': 'Unanswered — Converging Refusal (δ-Critical Artifact Hands)',
            'weapon_desc': '10–15 Grudge + 1.5 Void/s for 6s (Paired remote AoE, Cost: 18 Sorrow Echoes).',
            'special_title': 'Closed Ground (Area-Denial Field)',
            'special_desc': '2 Void/s for 10s in center zone; disrupts Han movement (Cost: 45 Sorrow Echoes).',
            'uniform_title': 'Android Ceramic Outer Chassis',
            'uniform_desc': 'External technology composite frame (0.5 Grudge / 0.5 Void resistance).'
        }
    },
    'the-exile-xyan.html': {
        'id': 'CORE-09',
        'title_en': 'The Exile Xyan',
        'title_kr': '추방자 시안',
        'dept': 'Floor 7 // Penal Watch',
        'clearance': 'Level 4 Senior Disciplinary Lead',
        'resonance': 'Execution Pulse (50 Hz)',
        'status': 'Active · Penance Protocol Online',
        'icon': 'assets/icons/avatar_core_xyan.svg',
        'color': '#ef4444',
        'stats': {
            'resilience': 'Level V (EX) · 140 HP [♦ Deep Blue]',
            'clarity': 'Level III (Normal) · 90 SP [♠ Pale White]',
            'composure': 'Level III (Normal) · 75% Penance Focus [♣ Crimson]',
            'resolve': 'Level V (EX) · 1.1s Rapid Execution [★ Black/Gold]'
        },
        'signature_gear': {
            'weapon_title': 'Penal Execution Heavy Cleaver',
            'weapon_desc': 'Brutal disciplinary strike (Grudge 22–32 heavy kinetic laceration).',
            'special_title': 'Guilt Calibration Penance Collar',
            'special_desc': 'Converts incoming psychological panic into kinetic physical attack power.',
            'uniform_title': 'Shackled Iron Penal Plate',
            'uniform_desc': 'Heavy wrought-iron punishment harness (0.4 Grudge resistance).'
        }
    },
    'taeho.html': {
        'id': 'UCD-01',
        'title_en': 'Commander Taeho',
        'title_kr': '지휘관 태호',
        'dept': 'Underworld Cleanup Descend // Task Force',
        'clearance': 'Level 4 Strike Leader',
        'resonance': 'Tactical Command (210 Hz)',
        'status': 'Active · UCD 6 Arcs Leader',
        'icon': 'assets/icons/avatar_char_taeho.svg',
        'color': '#ef5b55',
        'stats': {
            'resilience': 'Level V (EX) · 130 HP [♦ Deep Blue]',
            'clarity': 'Level IV (Master) · 110 SP [♠ Pale White]',
            'composure': 'Level IV (Master) · 88% Strike Composure [♣ Crimson]',
            'resolve': 'Level IV (Master) · 1.4s Tactical Speed [★ Black/Gold]'
        },
        'signature_gear': {
            'weapon_title': 'Tactical Heavy Breach Shotgun',
            'weapon_desc': 'Close-range kinetic spread (Grudge 18–26 direct).',
            'special_title': 'Strike Telemetry Command Beacon',
            'special_desc': 'Coordinates 6-member squad focus fire, increasing squad damage by +20%.',
            'uniform_title': 'Reinforced Ballistic Carapace',
            'uniform_desc': 'Underworld tactical combat armor (0.5 Grudge / 0.7 Weight resistance).'
        }
    },
    'yeonhwa.html': {
        'id': 'SED-01',
        'title_en': 'Cartographer Yeonhwa',
        'title_kr': '지도제작자 연화',
        'dept': 'Somnarak Exploration Decreed // Corps',
        'clearance': 'Level 4 Frontier Expedition Lead',
        'resonance': 'Spatial Compass (315 Hz)',
        'status': 'Active · SED 7 Arcs Mapping',
        'icon': 'assets/icons/avatar_char_yeonhwa.svg',
        'color': '#38bdf8',
        'stats': {
            'resilience': 'Level III (Normal) · 95 HP [♦ Deep Blue]',
            'clarity': 'Level V (EX) · 140 SP [♠ Pale White]',
            'composure': 'Level V (EX) · 95% Cartographic Precision [♣ Crimson]',
            'resolve': 'Level III (Normal) · 2.1s Action Interval [★ Black/Gold]'
        },
        'signature_gear': {
            'weapon_title': 'Surveyor Sextant Rapier',
            'weapon_desc': 'Precision piercing blade with spatial measurement calibrations (Lament 12–18).',
            'special_title': 'Zone Mapping Astrolabe Key',
            'special_desc': 'Detects uncharted subterranean tunnels and Cheongula fracture faults.',
            'uniform_title': 'Topographer Weather Shroud',
            'uniform_desc': 'Insulated frontier exploration cloak (0.6 Lament / 0.7 Void resistance).'
        }
    },
    'minho.html': {
        'id': 'UCD-02',
        'title_en': 'Investigator Minho',
        'title_kr': '수사관 민호',
        'dept': 'UCD Intelligence Division',
        'clearance': 'Level 3 Detective',
        'resonance': 'Inquiry Logic (480 Hz)',
        'status': 'Active · Infiltration Detective',
        'icon': 'assets/icons/avatar_char_minho.svg',
        'color': '#38bdf8',
        'stats': {
            'resilience': 'Level III (Normal) · 90 HP [♦ Deep Blue]',
            'clarity': 'Level IV (Master) · 125 SP [♠ Pale White]',
            'composure': 'Level IV (Master) · 90% Forensic Composure [♣ Crimson]',
            'resolve': 'Level IV (Master) · 1.7s Reaction Speed [★ Black/Gold]'
        },
        'signature_gear': {
            'weapon_title': 'Forensic Taser Stave',
            'weapon_desc': 'Non-lethal electrical shock & interrogative pulse (Lament 10–15).',
            'special_title': 'Memory Scanner Eyepiece',
            'special_desc': 'Detects memory tampering and identifies Memory Washer contraband.',
            'uniform_title': 'Concealment Trench Coat',
            'uniform_desc': 'Undercover street attire with hidden Kevlar lining (0.7 Grudge resistance).'
        }
    },
    'soojin.html': {
        'id': 'UCD-03',
        'title_en': 'Entity Handler Soojin',
        'title_kr': '개체 조련사 수진',
        'dept': 'UCD Containment Wing',
        'clearance': 'Level 3 Pacification Specialist',
        'resonance': 'Beast Whisper (330 Hz)',
        'status': 'Active · Field Entity Pacifier',
        'icon': 'assets/icons/avatar_char_soojin.svg',
        'color': '#10b981',
        'stats': {
            'resilience': 'Level IV (Master) · 110 HP [♦ Deep Blue]',
            'clarity': 'Level IV (Master) · 130 SP [♠ Pale White]',
            'composure': 'Level V (EX) · 95% Empathy Focus [♣ Crimson]',
            'resolve': 'Level III (Normal) · 2.0s Combat Speed [★ Black/Gold]'
        },
        'signature_gear': {
            'weapon_title': 'Sorrow Pacification Whip',
            'weapon_desc': 'Entangles wild sorrow entities and pacifies aggression (Weight 12–18).',
            'special_title': 'Sorrow Calming Whistle',
            'special_desc': 'Emits soothing resonance frequencies that lower entity Gauge by 15%.',
            'uniform_title': 'Pheromone Neutralizer Vest',
            'uniform_desc': 'Reinforced handler vest protecting against entity bites (0.6 Weight resistance).'
        }
    },
    'doha.html': {
        'id': 'SED-02',
        'title_en': 'Master Mason Doha',
        'title_kr': '석공 도하',
        'dept': 'SED Defensive Vanguard',
        'clearance': 'Level 3 Vanguard Mason',
        'resonance': 'Granite Ward (110 Hz)',
        'status': 'Active · Base Fortification',
        'icon': 'assets/icons/avatar_char_doha.svg',
        'color': '#f59e0b',
        'stats': {
            'resilience': 'Level V (EX) · 145 HP [♦ Deep Blue]',
            'clarity': 'Level III (Normal) · 85 SP [♠ Pale White]',
            'composure': 'Level IV (Master) · 80% Masonry Focus [♣ Crimson]',
            'resolve': 'Level III (Normal) · 2.4s Heavy Strike [★ Black/Gold]'
        },
        'signature_gear': {
            'weapon_title': 'Mason Sledge Hammer',
            'weapon_desc': 'Crushes basalt obstacles and breaches barricades (Grudge 18–26).',
            'special_title': 'Granite Anchor Chisel',
            'special_desc': 'Erects temporary stone walls in combat to absorb 200 incoming damage.',
            'uniform_title': 'Basalt Reinforced Harness',
            'uniform_desc': 'Heavy mason gear with protective slag aprons (0.4 Grudge resistance).'
        }
    },
    'joon.html': {
        'id': 'UCD-04',
        'title_en': 'Acoustic Engineer Joon',
        'title_kr': '음향 기술자 준',
        'dept': 'UCD Technology Division',
        'clearance': 'Level 3 Tech Specialist',
        'resonance': 'Waveform Phase (580 Hz)',
        'status': 'Active · Grid Calibration',
        'icon': 'assets/icons/avatar_char_joon.svg',
        'color': '#38bdf8',
        'stats': {
            'resilience': 'Level III (Normal) · 85 HP [♦ Deep Blue]',
            'clarity': 'Level IV (Master) · 135 SP [♠ Pale White]',
            'composure': 'Level V (EX) · 98% Acoustic Precision [♣ Crimson]',
            'resolve': 'Level III (Normal) · 2.2s Action Interval [★ Black/Gold]'
        },
        'signature_gear': {
            'weapon_title': 'Sonic Pulse Frequency Emitter',
            'weapon_desc': 'Disrupts illegal sound transmissions and siren wails (Lament 12–16).',
            'special_title': 'Tuning Fork Phase Resonator',
            'special_desc': 'Neutralizes acoustic taboo violations within a 15-meter radius.',
            'uniform_title': 'Acoustic Insulated Jumpsuit',
            'uniform_desc': 'Soundproofed fabric dampening high-decibel screams (0.5 Lament resistance).'
        }
    },
    'sora.html': {
        'id': 'SED-03',
        'title_en': 'The Dreamer Sora',
        'title_kr': '몽상가 소라',
        'dept': 'SED Ethereal Reconnaissance',
        'clearance': 'Level 3 Psychic Lead',
        'resonance': 'Dream Frequency (710 Hz)',
        'status': 'Active · Deep Dream Dive',
        'icon': 'assets/icons/avatar_char_sora.svg',
        'color': '#a855f7',
        'stats': {
            'resilience': 'Level II (Vulnerable) · 75 HP [♦ Deep Blue]',
            'clarity': 'Level V (EX) · 165 SP [♠ Pale White]',
            'composure': 'Level V (EX) · 100% Dream Stability [♣ Crimson]',
            'resolve': 'Level II (Slow) · 2.8s Action Speed [★ Black/Gold]'
        },
        'signature_gear': {
            'weapon_title': 'Dream Needle Filament Dagger',
            'weapon_desc': 'Sever ethereal connections in the Dream layer (Lament/Void 14–20).',
            'special_title': 'Lucid Sleep Bell Relic',
            'special_desc': 'Anchors consciousness during deep dream-dives, preventing memory theft.',
            'uniform_title': 'Ethereal Weave Robes',
            'uniform_desc': 'Spun from dream filaments (0.4 Lament / 0.5 Void resistance).'
        }
    },
    'kael.html': {
        'id': 'OUT-01',
        'title_en': 'Kael the Exile',
        'title_kr': '추방자 카엘',
        'dept': 'Desolate Outskirts // Nomad Sovereign Kingdom',
        'clearance': 'External Sovereign Warlord',
        'resonance': 'Han Storm Surge (85 Hz)',
        'status': 'Active · Independent Sovereign',
        'icon': 'assets/icons/avatar_char_kael.svg',
        'color': '#ef4444',
        'stats': {
            'resilience': 'Level V (EX) · 150 HP [♦ Deep Blue]',
            'clarity': 'Level IV (Master) · 110 SP [♠ Pale White]',
            'composure': 'Level III (Normal) · 75% Warlord Focus [♣ Crimson]',
            'resolve': 'Level V (EX) · 1.2s Whirlwind Strike [★ Black/Gold]'
        },
        'signature_gear': {
            'weapon_title': 'Storm Cleaver Greatsword',
            'weapon_desc': 'Heavy jagged blade forged from storm-hardened Han slag (Grudge 24–36).',
            'special_title': 'The Scar Horizon Compass',
            'special_desc': 'Guides caravans safely through category-5 Han storms in the Desolate.',
            'uniform_title': 'Nomad Warlord Cuirass',
            'uniform_desc': 'Weather-beaten heavy armor (0.4 Grudge / 0.6 Weight resistance).'
        }
    },
    'high-architects.html': {
        'id': 'ORG-01',
        'title_en': 'The High Architects',
        'title_kr': '상위 건축가 길드',
        'dept': 'Zone C // Master Guild Council',
        'clearance': 'Civic Master Authority',
        'resonance': 'Geometric Harmony (400 Hz)',
        'status': 'Active · Infrastructure Monopoly',
        'icon': 'assets/icons/avatar_char_high_architects.svg',
        'color': '#f1df76',
        'stats': {
            'resilience': 'Level IV (Master) · 110 HP [♦ Deep Blue]',
            'clarity': 'Level V (EX) · 140 SP [♠ Pale White]',
            'composure': 'Level V (EX) · 100% Geometric Design [♣ Crimson]',
            'resolve': 'Level III (Normal) · 2.0s Action Speed [★ Black/Gold]'
        },
        'signature_gear': {
            'weapon_title': 'Guild Master Compass Staff',
            'weapon_desc': 'Architectural drafting staff emitting precision cutting beams (Grudge/Lament 12–18).',
            'special_title': 'City Blueprint Keystone',
            'special_desc': 'Authorizes instant structural alterations to municipal district walls.',
            'uniform_title': 'Ceremonial Draftsman Robes',
            'uniform_desc': 'Gilded master robes of the Architects Guild (0.6 Lament / 0.6 Grudge).'
        }
    },
    'cheonbulok-refugees.html': {
        'id': 'REF-02',
        'title_en': 'Cheonbulok Refugees',
        'title_kr': '천불록 난민 연합',
        'dept': 'Zone E // Corner 2 Colony',
        'clearance': 'Displaced Sovereign Colony',
        'resonance': 'Furnace Ash (150 Hz)',
        'status': 'Active · Survival Vigil',
        'icon': 'assets/icons/avatar_char_cheonbulok_refugees.svg',
        'color': '#f97316',
        'stats': {
            'resilience': 'Level IV (Master) · 125 HP [♦ Deep Blue]',
            'clarity': 'Level III (Normal) · 90 SP [♠ Pale White]',
            'composure': 'Level IV (Master) · 85% Survival Focus [♣ Crimson]',
            'resolve': 'Level IV (Master) · 1.6s Combat Reflexes [★ Black/Gold]'
        },
        'signature_gear': {
            'weapon_title': 'Refugee Defense Speargun',
            'weapon_desc': 'Improvised pneumatic spear firing heated scrap metal (Grudge 14–22).',
            'special_title': 'Furnace Shard Ember',
            'special_desc': 'Warm glowing ember from Corner 2’s dying furnace, warding off cold Desolate mist.',
            'uniform_title': 'Ash-Coated Scavenger Cloak',
            'uniform_desc': 'Thick multi-layered scrap fabric (0.5 Grudge / 0.6 Weight resistance).'
        }
    }
}

def generate_canon_infobox(data):
    stats = data['stats']
    gear = data['signature_gear']
    return f"""
      <aside class="character-infobox" style="--entity: {data['color']};">
        <h2 id="{data['id'].lower()}">{data['id']} // {data['title_en'].upper()}</h2>
        <div class="infobox-image-wrap">
          <img src="../{data['icon']}" alt="{data['title_en']} Regalia" class="character-portrait" style="border: 2px solid {data['color']};">
          <div style="font-family:'Cinzel', serif; font-size:1.1rem; color:#f8fafc; margin-top:8px; font-weight:bold;">{data['title_en']}</div>
          <div style="font-family:'JetBrains Mono', monospace; font-size:0.85rem; color:{data['color']};">{data['title_kr']}</div>
        </div>

        <dl class="fact-grid">
          <dt>Formal ID</dt>
          <dd>{data['id']}</dd>
          <dt>Department</dt>
          <dd>{data['dept']}</dd>
          <dt>Clearance</dt>
          <dd>{data['clearance']}</dd>
          <dt>Resonance</dt>
          <dd>{data['resonance']}</dd>
          <dt>Status</dt>
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

        <h3 id="signature-loadout">Signature Equipment &amp; M.A.W.</h3>
        <dl class="fact-grid">
          <dt>Signature Weapon</dt>
          <dd style="color:#f1df76;"><b>{gear['weapon_title']}</b><br><small style="color:#94a3b8;">{gear['weapon_desc']}</small></dd>
          <dt>Special Protocol</dt>
          <dd style="color:#38bdf8;"><b>{gear['special_title']}</b><br><small style="color:#94a3b8;">{gear['special_desc']}</small></dd>
          <dt>Attire / Armor</dt>
          <dd style="color:#10b981;"><b>{gear['uniform_title']}</b><br><small style="color:#94a3b8;">{gear['uniform_desc']}</small></dd>
        </dl>
      </aside>
"""

# Replace in all character files
for fname, data in CHARACTERS_CANON_DATA.items():
    fpath = f'{wiki_root}/characters/{fname}'
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    new_infobox = generate_canon_infobox(data)

    # Check if page already has <aside class="character-infobox"...
    if '<aside class="character-infobox"' in html:
        # Replace existing aside
        pattern = r'<aside class="character-infobox"[\s\S]*?<\/aside>'
        new_html = re.sub(pattern, new_infobox.strip(), html)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"SUCCESS: Updated {fname} with CANONICAL R.D. ATTRIBUTES & SIGNATURE M.A.W.!")
    else:
        print(f"No aside found in {fname}")

print("COMPLETED ALL CHARACTER PAGES TO CANONICAL REVERIE DIRECTORATE STANDARDS!")
