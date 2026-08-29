import os, re, glob
from bs4 import BeautifulSoup

wiki_root = '/home/user/01_Somnarak_Wiki'

# Master Canonical Entity, MAW, and Tales Matrix
ENTITIES_MASTER = [
    {
        'id': 'SE-001',
        'name_en': 'The Orphaned Bell',
        'name_kr': '고아의 종',
        'risk': 'PHANTASM',
        'risk_symbol': 'δ',
        'element': 'LAMENT',
        'element_kr': '비탄',
        'element_color': '#38bdf8',
        'floor': 'Floor 2 // Maw\'s Keep',
        'work_pref': 'Insight (65%) · Communion (55%)',
        'file': 'entities/se-001-the-orphaned-bell.html',
        'icon': 'assets/art/entities/se-001-icon.svg',
        'banner': 'assets/art/entities/se-001-banner.svg',
        'profile': 'assets/art/entities/se-001-profile.svg',
        'maw_weapon': {'id': 'MAW-W-001-01', 'name': 'Bell Striker', 'type': 'Hammer / Maul', 'file': 'maw/maw-w-001-01-the-laments-requiem.html', 'dmg': 'Lament 12-18'},
        'maw_suit': {'id': 'MAW-S-001-01', 'name': 'Bell Resonance Vestment', 'type': 'Suit / Vestment', 'file': 'maw/maw-s-001-01-the-laments-shroud.html', 'res': '0.6 Lament / 1.0 Grudge'},
        'maw_gift': {'id': 'MAW-G-001-01', 'name': 'Bell Clapper Charm', 'type': 'Accessory / Charm', 'file': 'maw/maw-g-001-01-laments-edge.html', 'stat': '+5 Max SP, +3 Psych Defense'},
        'tale': {
            'quote': 'The bell tolls for children who will never grow old.',
            'narrative': 'In the flooded basements of the Old Sector, an ancient bronze bell hung suspended from fractured stone arches. It wept liquid cyan Han tears that never evaporated. Whenever an abandoned child wept in the city above, the clapper swung of its own accord, ringing with a frequency that silenced despair by drowning the listener’s consciousness in azure mist.',
            'testimony': '\"We tried to cut the support chains during Cycle 0,412. The moment the blowtorch touched the bronze, every technician in a three-block radius forgot their own mother’s name. We leave the bell alone now. We only listen.\" — Lead Zyrak, Floor 2 Containment Log',
            'record': 'Directorate Containment Directive: SE-001 requires constant acoustic submersion. If Coherence Counter reaches 0, the bell rings at 440Hz resonance, forcing immediate cognitive collapse across all unshielded agents on Floor 2.'
        }
    },
    {
        'id': 'SE-002',
        'name_en': 'The Grieving Colossus',
        'name_kr': '슬퍼하는 거상',
        'risk': 'PHANTASM',
        'risk_symbol': 'δ',
        'element': 'GRUDGE',
        'element_kr': '원한',
        'element_color': '#ef5b55',
        'floor': 'Floor 2 // Maw\'s Keep',
        'work_pref': 'Subjugation (60%) · Siphon (50%)',
        'file': 'entities/se-002-the-grieving-colossus.html',
        'icon': 'assets/art/entities/se-002-icon.svg',
        'banner': 'assets/art/entities/se-002-banner.svg',
        'profile': 'assets/art/entities/se-002-profile.svg',
        'maw_weapon': {'id': 'MAW-W-002-01', 'name': 'Colossus Cleaver', 'type': 'Greatsword / Cleaver', 'file': 'maw/maw-w-002-01-the-mourning-maul.html', 'dmg': 'Grudge 18-26'},
        'maw_suit': {'id': 'MAW-S-002-01', 'name': 'Colossal Plate', 'type': 'Heavy Plate Armor', 'file': 'maw/maw-s-002-01-the-mourning-mantle.html', 'res': '0.5 Grudge / 0.8 Weight'},
        'maw_gift': {'id': 'MAW-G-002-01', 'name': 'Colossus Shard', 'type': 'Armor Plating / Brooch', 'file': 'maw/maw-g-002-01-the-mourning-shell.html', 'stat': '+8 Max HP, +5 Physical Defense'},
        'tale': {
            'quote': 'It walks. It weeps. Where its tears fall, buildings grow.',
            'narrative': 'Constructed from the crushed basalt of the Cheonbulok foundation, the Colossus wanders subterranean containment shafts carrying the collective weight of five thousand buried masons. Its tears are thick, boiling crimson sludge that solidifies upon contact with air into jagged monoliths of compressed regret.',
            'testimony': '\"Its footsteps shake the foundation of Floor 2 like a localized seismic fracture. When you stand before it, you do not feel hatred—you feel the crushing, impossible burden of labor that was never recognized.\" — Containment Specialist Doha',
            'record': 'Directorate Containment Directive: SE-002 must be pacified through heavy kinetic Work (Subjugation). Breach conditions trigger structural quakes across the entire Central Containment shaft.'
        }
    },
    {
        'id': 'SE-003',
        'name_en': 'The Thread of Memory',
        'name_kr': '기억의 실',
        'risk': 'SOMNA',
        'risk_symbol': 'β',
        'element': 'LAMENT',
        'element_kr': '비탄',
        'element_color': '#38bdf8',
        'floor': 'Floor 3 // Extraction Hall',
        'work_pref': 'Communion (70%) · Insight (60%)',
        'file': 'entities/se-003-the-wilderness-tide.html',
        'icon': 'assets/art/entities/se-003-icon.svg',
        'banner': 'assets/art/entities/se-003-banner.svg',
        'profile': 'assets/art/entities/se-003-profile.svg',
        'maw_weapon': {'id': 'MAW-W-003-01', 'name': 'Memory Blade', 'type': 'Filament Rapier', 'file': 'maw/maw-w-003-01-memory-blade.html', 'dmg': 'Lament 10-15'},
        'maw_suit': {'id': 'MAW-S-003-01', 'name': 'Tide Cloak', 'type': 'Woven Silk Cloak', 'file': 'maw/maw-s-003-01-tide-cloak.html', 'res': '0.7 Lament / 0.8 Void'},
        'maw_gift': {'id': 'MAW-G-003-01', 'name': 'Memory Thread Needle', 'type': 'Hairpin / Needle', 'file': 'maw/maw-g-003-01-memory-thread-needle.html', 'stat': '+4 Max SP, +5% Work Speed'},
        'tale': {
            'quote': 'It weaves your memories into webs.',
            'narrative': 'A floating, translucent spindle that spins gossamer threads from human nostalgia. Agents assigned to its chamber report seeing childhood bedrooms woven in shimmering azure silk across the ceiling. Each strand pulled from the entity weakens the subject’s recollection of traumatic incidents, leaving only a serene, vacant euphoria.',
            'testimony': '\"I went inside thinking about the breach on Day 14. When I came out, I remembered that someone had died, but I could no longer remember his face or voice. The thread had eaten his name.\" — Agent Harin',
            'record': 'Directorate Containment Directive: Limit continuous interaction to under 8 minutes per shift. Prolonged communion results in permanent amnesia of facility safety codes.'
        }
    },
    {
        'id': 'SE-004',
        'name_en': 'The Rust-Bleeding Sentry',
        'name_kr': '녹을 흘리는 보초',
        'risk': 'MORPHEAN',
        'risk_symbol': 'γ',
        'element': 'GRUDGE',
        'element_kr': '원한',
        'element_color': '#ef5b55',
        'floor': 'Floor 5 // Border Watch',
        'work_pref': 'Subjugation (65%) · Siphon (55%)',
        'file': 'entities/se-004-the-rust-bleeding-sentry.html',
        'icon': 'assets/art/entities/se-004-icon.svg',
        'banner': 'assets/art/entities/se-004-banner.svg',
        'profile': 'assets/art/entities/se-004-profile.svg',
        'maw_weapon': {'id': 'MAW-W-004-01', 'name': 'Rust Halberd', 'type': 'Polearm / Halberd', 'file': 'maw/maw-w-004-01-rust-halberd.html', 'dmg': 'Grudge 14-20 (15% Armor Shred)'},
        'maw_suit': {'id': 'MAW-S-004-01', 'name': 'Sentry\'s Iron Plate', 'type': 'Corroded Iron Cuirass', 'file': 'maw/maw-s-004-01-sentrys-iron-plate.html', 'res': '0.5 Grudge / 0.9 Lament'},
        'maw_gift': {'id': 'MAW-G-004-01', 'name': 'Corrosion Visor', 'type': 'Iron Mask / Visor', 'file': 'maw/maw-g-004-01-corrosion-visor.html', 'stat': '+4 Max HP, +3 Defense'},
        'tale': {
            'quote': 'He stands at attention. Waiting in the iron rain.',
            'narrative': 'An ancient iron automaton garrisoned at the border gate of District 14 during the First Fracture. Its internal clockwork has corroded into jagged flakes of rust, yet its stance remains rigid and unyielding. Corrosive reddish fluid weeps continuously from its optical sensors, dissolving the stone floor beneath its iron boots.',
            'testimony': '\"We told it the war ended five hundred years ago. It simply raised its halberd and stood straighter. It will guard that empty gateway until its iron bones turn to dust.\" — Border Watchman Minho',
            'record': 'Directorate Containment Directive: High kinetic armor required for all attendants. Sentry interprets any non-ceremonial movement as a hostile border incursion.'
        }
    },
    {
        'id': 'SE-005',
        'name_en': 'The Smothering Mother',
        'name_kr': '숨 막히는 어머니',
        'risk': 'AETHER',
        'risk_symbol': 'α',
        'element': 'LAMENT',
        'element_kr': '비탄',
        'element_color': '#38bdf8',
        'floor': 'Floor 1 // Neutral Core',
        'work_pref': 'Communion (80%) · Insight (75%)',
        'file': 'entities/se-005-the-smothering-mother.html',
        'icon': 'assets/art/entities/se-005-icon.svg',
        'banner': 'assets/art/entities/se-005-banner.svg',
        'profile': 'assets/art/entities/se-005-profile.svg',
        'maw_weapon': {'id': 'MAW-W-005-01', 'name': 'Cradle Lance', 'type': 'Porcelain Lance', 'file': 'maw/maw-w-005-01-the-embrace-fang.html', 'dmg': 'Lament 8-12'},
        'maw_suit': {'id': 'MAW-S-005-01', 'name': 'Cradle Harness', 'type': 'Silken Restraint Harness', 'file': 'maw/maw-s-005-01-the-embrace-plate.html', 'res': '0.7 Lament / 1.0 Grudge'},
        'maw_gift': {'id': 'MAW-G-005-01', 'name': 'Maternal Clasp', 'type': 'Gilded Porcelain Pendant', 'file': 'maw/maw-g-005-01-the-embrace.html', 'stat': '+3 Max SP, +4 Psychic Resilience'},
        'tale': {
            'quote': 'She holds you so tight you cannot breathe.',
            'narrative': 'A towering porcelain maternal effigy entwined with heavy black velvet swaddling bands. It manifests the overwhelming, suffocating grief of parental over-protection. When agents enter its chamber, soft lullabies echo through their cerebral implants, urging them to lay down their weapons and sleep forever inside its warm, porcelain embrace.',
            'testimony': '\"I felt so safe. I didn\'t want to leave. When the team dragged me out of the chamber, I was screaming at them for stealing my mother. I didn\'t realize my ribs were already cracked from the embrace.\" — Junior Agent Sora',
            'record': 'Directorate Containment Directive: Standard Communion protocol produces high positive Han flux. However, if work duration exceeds 120 seconds, immediate physical extraction is mandatory.'
        }
    },
    {
        'id': 'SE-006',
        'name_en': 'The Siphon Leech',
        'name_kr': '착취하는 거머리',
        'risk': 'SOMNA',
        'risk_symbol': 'β',
        'element': 'WEIGHT',
        'element_kr': '중압',
        'element_color': '#10b981',
        'floor': 'Floor 3 // Extraction Hall',
        'work_pref': 'Siphon (70%) · Dissection (60%)',
        'file': 'entities/se-006-the-siphon-leech.html',
        'icon': 'assets/art/entities/se-006-icon.svg',
        'banner': 'assets/art/entities/se-006-banner.svg',
        'profile': 'assets/art/entities/se-006-profile.svg',
        'maw_weapon': {'id': 'MAW-W-006-01', 'name': 'Siphon Cannula', 'type': 'Needle Cannula', 'file': 'maw/maw-w-006-01-siphon-cannula.html', 'dmg': 'Weight 10-16 (10% HP/SP Siphon)'},
        'maw_suit': {'id': 'MAW-S-006-01', 'name': 'Leech Membrane Suit', 'type': 'Annelid Polymer Suit', 'file': 'maw/maw-s-006-01-leech-membrane-suit.html', 'res': '0.6 Weight / 0.8 Grudge'},
        'maw_gift': {'id': 'MAW-G-006-01', 'name': 'Effluent Gland', 'type': 'Bio-Siphon Implant', 'file': 'maw/maw-g-006-01-effluent-gland.html', 'stat': '+5 Max HP, +5 Max SP'},
        'tale': {
            'quote': 'It drinks the dark effluent of forgotten sins.',
            'narrative': 'An amphibious segmented annelid organism extracted from the drainage flumes beneath Zone B. It feeds exclusively on the concentrated emotional runoff and biological waste of the city. As it feeds, its translucent skin pulsates with a rhythmic, sickly emerald glow, filtering heavy toxic sorrow into pure crystallized Han granules.',
            'testimony': '\"The suction sounds will keep you awake at night. But without the Leech, the drainage valves on Floor 3 would have clogged with coagulated grief decades ago.\" — Extraction Lead Zyrak',
            'record': 'Directorate Containment Directive: Regular Siphon protocol required every 4 hours. Failure to feed leads to pipe rupture and biological Weight damage contamination.'
        }
    },
    {
        'id': 'SE-007',
        'name_en': 'Brume (The Ashen Scribe)',
        'name_kr': '박무 (잿빛 필경사)',
        'risk': 'SOMNA',
        'risk_symbol': 'β',
        'element': 'LAMENT',
        'element_kr': '비탄',
        'element_color': '#38bdf8',
        'floor': 'Floor 6 // Deep Vault',
        'work_pref': 'Insight (70%) · Communion (60%)',
        'file': 'entities/se-007-brume.html',
        'icon': 'assets/art/entities/se-007-icon.svg',
        'banner': 'assets/art/entities/se-007-banner.svg',
        'profile': 'assets/art/entities/se-007-profile.svg',
        'maw_weapon': {'id': 'MAW-W-007-01', 'name': 'Ashen Slate Blade', 'type': 'Basalt Scribe Dagger', 'file': 'maw/maw-w-007-01-the-hope-lens.html', 'dmg': 'Lament 11-16'},
        'maw_suit': {'id': 'MAW-S-007-01', 'name': 'Ashen Shroud', 'type': 'Smoky Basalt Veil', 'file': 'maw/maw-s-007-01-the-hope-veil.html', 'res': '0.6 Lament / 0.8 Void'},
        'maw_gift': {'id': 'MAW-G-007-01', 'name': 'Brume Incense', 'type': 'Incense Censer Charm', 'file': 'maw/maw-g-007-01-the-hope-lantern.html', 'stat': '+6 Max SP, +4% Insight Success'},
        'tale': {
            'quote': 'Writing names on basalt slates that turn to ash.',
            'narrative': 'A spectral cloaked figure drifting within a swirling cloud of fine gray particulate fog. It sits perpetually before a basalt writing desk, meticulously carving the names of forgotten casualties into stone slates using an obsidian stylus. The moment a slate is completed, it crumbles into fine ash, dissolving back into the fog.',
            'testimony': '\"If you look closely into the mist, you can see your own name being carved. When it finishes the last stroke, you forget why you ever entered the Directorate.\" — Archivist Minjae',
            'record': 'Directorate Containment Directive: All personnel must wear active respiratory filtration and optic glare dampers when entering Containment Chamber 06-07.'
        }
    },
    {
        'id': 'SE-008',
        'name_en': 'The Iron Maiden of Regret',
        'name_kr': '후회의 철처녀',
        'risk': 'PHANTASM',
        'risk_symbol': 'δ',
        'element': 'GRUDGE',
        'element_kr': '원한/비탄',
        'element_color': '#ef4444',
        'floor': 'Floor 6 // Deep Vault',
        'work_pref': 'Subjugation (65%) · Siphon (50%)',
        'file': 'entities/se-008-the-iron-maiden-of-regret.html',
        'icon': 'assets/art/entities/se-008-icon.svg',
        'banner': 'assets/art/entities/se-008-banner.svg',
        'profile': 'assets/art/entities/se-008-profile.svg',
        'maw_weapon': {'id': 'MAW-W-008-01', 'name': 'Thorn Impaler', 'type': 'Barbed Great-Spear', 'file': 'maw/maw-w-008-01-thorn-impaler.html', 'dmg': 'Grudge/Lament 20-26'},
        'maw_suit': {'id': 'MAW-S-008-01', 'name': 'Sarcophagus Shroud', 'type': 'Spiked Iron Plate', 'file': 'maw/maw-s-008-01-sarcophagus-shroud.html', 'res': '0.4 Grudge / 0.5 Lament'},
        'maw_gift': {'id': 'MAW-G-008-01', 'name': 'Spike Crown', 'type': 'Crown of Thorns', 'file': 'maw/maw-g-008-01-spike-crown.html', 'stat': '+8 Max SP, +5 Physical Atk'},
        'tale': {
            'quote': 'A hollow sarcophagus lined with weeping steel thorns.',
            'narrative': 'An ornate Victorian-style iron sarcophagus standing upright in a pool of blackened oil. Its interior is lined with hundreds of hollow iron spikes that weep pressurized caustic steam. When an individual carrying deep unresolved remorse steps within three meters, the iron doors swing open and emit a haunting choral shriek.',
            'testimony': '\"The doors don\'t slam shut with brute force. They close gently, like a mother kissing a child goodnight. And then you hear the screams from inside.\" — Penal Warden Xyan',
            'record': 'Directorate Containment Directive: Severe kinetic suppression protocol. Any agent undergoing psychological Panic near SE-008 is immediately drawn inside by magnetic sorrow resonance.'
        }
    },
    {
        'id': 'SE-009',
        'name_en': 'The Memory Weaver (Drowned Bell)',
        'name_kr': '기억의 방직자 (수몰된 종)',
        'risk': 'SOMNA',
        'risk_symbol': 'β',
        'element': 'LAMENT',
        'element_kr': '비탄',
        'element_color': '#38bdf8',
        'floor': 'Floor 4 // Insight Forge',
        'work_pref': 'Communion (70%) · Insight (65%)',
        'file': 'entities/se-009-the-memory-weaver.html',
        'icon': 'assets/art/entities/se-009-icon.svg',
        'banner': 'assets/art/entities/se-009-banner.svg',
        'profile': 'assets/art/entities/se-009-profile.svg',
        'maw_weapon': {'id': 'MAW-W-009-01', 'name': 'Drowned Trident', 'type': 'Aquatic Filament Lance', 'file': 'maw/maw-w-009-01-the-forgotten-lens.html', 'dmg': 'Lament 12-17'},
        'maw_suit': {'id': 'MAW-S-009-01', 'name': 'Drowned Chainmail', 'type': 'Water-Repelling Mail', 'file': 'maw/maw-s-009-01-the-forgotten-veil.html', 'res': '0.6 Lament / 0.7 Void'},
        'maw_gift': {'id': 'MAW-G-009-01', 'name': 'Drowned Pendulum', 'type': 'Bronze Pendulum Talisman', 'file': 'maw/maw-g-009-01-the-forgotten-mask.html', 'stat': '+5 Max SP, +4% Siphon Yield'},
        'tale': {
            'quote': 'Submerged deep beneath the brine of drowned recollections.',
            'narrative': 'An aquatic bronze artifact submerged inside a massive pressure-sealed glass cylinder filled with heavy mineral brine. It pulsates with acoustic waves that replicate the sound of a submerged ship’s bell tolling in the deep abyss. The ripples in the water continually form moving silhouettes of drowned sailors and forgotten voyages.',
            'testimony': '\"If you press your hand against the glass, you don\'t feel water—you feel the cold sting of seawater and the overwhelming urge to breathe in the brine.\" — Research Lead Ayshuk',
            'record': 'Directorate Containment Directive: Acoustic dampening field must remain calibrated at 120dB suppression. Water salinity levels must not exceed 35 PSU.'
        }
    },
    {
        'id': 'SE-010',
        'name_en': 'The Convergence (The Absolute Verdict)',
        'name_kr': '수렴 (절대 판결)',
        'risk': 'APOCRYPHA',
        'risk_symbol': 'ε',
        'element': 'VOID',
        'element_kr': '공허',
        'element_color': '#f8fafc',
        'floor': 'Floor 8 // Gate Watch',
        'work_pref': 'Dissection (30%) · Restraint (30%)',
        'file': 'entities/se-010-the-convergence.html',
        'icon': 'assets/art/entities/se-010-icon.svg',
        'banner': 'assets/art/entities/se-010-banner.svg',
        'profile': 'assets/art/entities/se-010-profile.svg',
        'maw_weapon': {'id': 'MAW-W-010-01', 'name': 'Convergence Scythe', 'type': 'Cosmic Void Scythe', 'file': 'maw/maw-w-010-01-the-absolute-maul.html', 'dmg': 'Void 30-45 (% Max HP)'},
        'maw_suit': {'id': 'MAW-S-010-01', 'name': 'Convergence Aegis', 'type': 'Superdense Void Carapace', 'file': 'maw/maw-s-010-01-the-absolute-mantle.html', 'res': '0.3 Void / 0.4 All Elements'},
        'maw_gift': {'id': 'MAW-G-010-01', 'name': 'Singularity Eye', 'type': 'Coronal Crown / Ocular Implant', 'file': 'maw/maw-g-010-01-the-absolute-verdict.html', 'stat': '+15 Max HP, +15 Max SP, +10% Void Res'},
        'tale': {
            'quote': 'When the thousand eyes converge into the singular dawn.',
            'narrative': 'An apocalyptic orb of woven gravitational crowns and blinding white light hovering in the center of the Subterranean Singularity Vault. It represents the existential inevitability of complete soul dissolution. Breaching its containment field collapses the boundary between dream and reality across the entirety of Somnarak.',
            'testimony': '\"You do not observe The Convergence. It observes you, and with every second you stare, ten years of your future disappear into the singularity.\" — Director Majin',
            'record': 'Directorate Containment Directive: MAXIMUM CONTAINMENT PROTOCOL. Handled exclusively by Level V Master Agents equipped with Apocrypha-grade M.A.W. gear.'
        }
    },
    {
        'id': 'SE-011',
        'name_en': 'The Whispering Walls',
        'name_kr': '속삭이는 벽',
        'risk': 'PHANTASM',
        'risk_symbol': 'δ',
        'element': 'LAMENT',
        'element_kr': '비탄',
        'element_color': '#38bdf8',
        'floor': 'Floor 7 // Shadow Corps',
        'work_pref': 'Insight (60%) · Communion (55%)',
        'file': 'entities/se-011-the-whispering-walls.html',
        'icon': 'assets/art/entities/se-011-icon.svg',
        'banner': 'assets/art/entities/se-011-banner.svg',
        'profile': 'assets/art/entities/se-011-profile.svg',
        'maw_weapon': {'id': 'MAW-W-011-01', 'name': 'Whisper Flail', 'type': 'Acoustic Chain Flail', 'file': 'maw/maw-w-011-01-the-listening-requiem.html', 'dmg': 'Lament 16-22'},
        'maw_suit': {'id': 'MAW-S-011-01', 'name': 'Whisper Barrier Mail', 'type': 'Sound-Cancelling Mail', 'file': 'maw/maw-s-011-01-the-listening-shroud.html', 'res': '0.5 Lament / 0.7 Grudge'},
        'maw_gift': {'id': 'MAW-G-011-01', 'name': 'Whisper Earring', 'type': 'Sonic Resonator Earring', 'file': 'maw/maw-g-011-01-the-listening-stone.html', 'stat': '+7 Max SP, +5 Acoustic Def'},
        'tale': {
            'quote': 'The labyrinth bulkheads whisper the names of those who entered.',
            'narrative': 'A labyrinthine living bulkhead made of soundproofed reinforced lead tiles embedded with thousands of relief-sculpted faces. The faces continuously murmur secrets, classified passcodes, and private confessions stolen from Directorate personnel through acoustic resonance eavesdropping.',
            'testimony': '\"It told me the exact date of my retirement and the name of my unborn daughter. Then it laughed with my deceased brother\'s voice.\" — Tactical Officer Taeho',
            'record': 'Directorate Containment Directive: Operatives entering Containment Wing 07 must activate active white-noise generators. Any agent caught listening to whispered passcodes is subject to disciplinary memory wash.'
        }
    },
    {
        'id': 'SE-014',
        'name_en': 'The Debt Eater (Hollow Debt Eater)',
        'name_kr': '부채를 먹는 자 (공허한 채무 포식자)',
        'risk': 'APOCRYPHA',
        'risk_symbol': 'ε',
        'element': 'WEIGHT',
        'element_kr': '중압',
        'element_color': '#f1df76',
        'floor': 'Floor 6 // Deep Vault',
        'work_pref': 'Dissection (40%) · Siphon (40%)',
        'file': 'entities/se-014-the-debt-eater.html',
        'icon': 'assets/art/entities/se-014-icon.svg',
        'banner': 'assets/art/entities/se-014-banner.svg',
        'profile': 'assets/art/entities/se-014-profile.svg',
        'maw_weapon': {'id': 'MAW-W-014-01', 'name': 'Debt Ledger Blade', 'type': 'Ledger-Bound Greatsword', 'file': 'maw/maw-w-014-01-the-debt-lens.html', 'dmg': 'Weight 22-30 (Dual HP+SP)'},
        'maw_suit': {'id': 'MAW-S-014-01', 'name': 'Debt-Null Greatcoat', 'type': 'Karmic Nullification Coat', 'file': 'maw/maw-s-014-01-the-debt-veil.html', 'res': '0.4 Weight / 0.5 Void'},
        'maw_gift': {'id': 'MAW-G-014-01', 'name': 'Debt Ledger Coin', 'type': 'Ancient Cheonbulok Coin', 'file': 'maw/maw-g-014-01-the-debt-scale-gift.html', 'stat': '+10 Max HP, +10 Max SP, +8% Debt Null'},
        'tale': {
            'quote': 'It eats your debt. But it takes your feeling with it.',
            'narrative': 'A colossal vested ledger beast that devours contractual documents, financial IOUs, and emotional obligations. When it swallows a person\'s debt certificate, that debt is legally erased from all municipal archives. However, the debtor permanently loses the ability to feel empathy, joy, or gratitude.',
            'testimony': '\"I had ten million credits in debt to the High Council. The Debt Eater ate my ledger in three seconds. Now my bank account is zero, but when I look at my children, I feel nothing at all.\" — Anonymous Zone B Merchant',
            'record': 'Directorate Containment Directive: Strictly quarantined from municipal ledger feeds. High Council audit officers are prohibited from entering within 100 meters without written clearance from Director Majin.'
        }
    },
    {
        'id': 'SE-015',
        'name_en': 'The Debt Scale (Sovereign Debt Scale)',
        'name_kr': '부채의 저울 (군주의 저울)',
        'risk': 'APOCRYPHA',
        'risk_symbol': 'ε',
        'element': 'VOID',
        'element_kr': '공허',
        'element_color': '#f8fafc',
        'floor': 'Floor 8 // Gate Watch',
        'work_pref': 'Dissection (35%) · Restraint (35%)',
        'file': 'entities/se-015-the-debt-scale.html',
        'icon': 'assets/art/entities/se-015-icon.svg',
        'banner': 'assets/art/entities/se-015-banner.svg',
        'profile': 'assets/art/entities/se-015-profile.svg',
        'maw_weapon': {'id': 'MAW-W-015-01', 'name': 'Balance Blade', 'type': 'Sovereign Fulcrum Blade', 'file': 'maw/maw-w-015-01-the-balance-lens.html', 'dmg': 'Void 28-38 (% Max HP)'},
        'maw_suit': {'id': 'MAW-S-015-01', 'name': 'Sovereign Scale Armor', 'type': 'Equilibrium Plate Armor', 'file': 'maw/maw-s-015-01-the-balance-veil.html', 'res': '0.3 Void / 0.5 Weight'},
        'maw_gift': {'id': 'MAW-G-015-01', 'name': 'Judgment Fulcrum', 'type': 'Golden Balance Fulcrum', 'file': 'maw/maw-g-015-01-the-balance-pendant.html', 'stat': '+12 Max SP, +10% Void Res'},
        'tale': {
            'quote': 'The cosmic fulcrum weighs remorse against lead slates.',
            'narrative': 'A cosmic equilibrium balance forged from iridescent sovereign glass and obsidian pendulums. It measures the moral and psychological weight of an individual’s unresolved guilt against heavy lead slates. If the pan tilts beyond 45 degrees, the subject undergoes existential annihilation.',
            'testimony': '\"Nobody passes the scale. Even the most righteous officer carries a gram of regret that weighs like a mountain on the fulcrum.\" — Secretary Seiyon',
            'record': 'Directorate Containment Directive: Only agents with Fortitude V and Prudence V are permitted to conduct observation. Breach triggers facility-wide gravitational realignment.'
        }
    }
]

# 1. BUILD /lore/entity-tales.html
tales_cards = []
for e in ENTITIES_MASTER:
    t = e['tale']
    w = e['maw_weapon']
    s = e['maw_suit']
    g = e['maw_gift']
    card = f"""
        <article class="tale-card" id="{e['id'].lower()}-tale" style="border: 2px solid {e['element_color']}; background: #060a12; padding: 24px; margin-bottom: 28px; border-radius: 4px;">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:16px; border-bottom:1px solid #1e293b; padding-bottom:12px;">
            <div style="display:flex; align-items:center; gap:16px;">
              <img src="../{e['icon']}" alt="{e['id']}" style="width:64px; height:64px; border:1px solid {e['element_color']}; border-radius:4px; background:#020617; padding:4px;">
              <div>
                <span class="risk-badge risk-{e['risk']}" style="font-size:0.75rem;">{e['risk_symbol']} ({e['risk']})</span>
                <h3 style="color:#f8fafc; margin:4px 0 0 0; font-size:1.35rem; font-family:'Cinzel', serif;">{e['id']} — {e['name_en'].upper()}</h3>
                <div style="color:{e['element_color']}; font-family:'JetBrains Mono', monospace; font-size:0.85rem;">{e['name_kr']} · {e['element']} DAMAGE · {e['floor']}</div>
              </div>
            </div>
            <a href="../{e['file']}" class="jump-btn" style="font-size:0.75rem;">FULL DOSSIER →</a>
          </div>

          <blockquote style="margin: 0 0 16px 0; padding: 10px 16px; border-left: 3px solid {e['element_color']}; background: rgba(0,0,0,0.4); font-style: italic; color: #cbd5e1;">
            "{t['quote']}"
          </blockquote>

          <div style="display:grid; grid-template-columns: 1fr; gap: 14px;">
            <div style="background:#0b1120; padding:14px; border:1px solid #1e293b; border-radius:4px;">
              <h4 style="color:#f1df76; margin:0 0 6px 0; font-size:0.9rem; font-family:'JetBrains Mono', monospace;">I. 이야기 (NARRATIO) — THE TALE</h4>
              <p style="color:#94a3b8; margin:0; line-height:1.6; font-size:0.9rem;">{t['narrative']}</p>
            </div>

            <div style="background:#0b1120; padding:14px; border:1px solid #1e293b; border-radius:4px;">
              <h4 style="color:#38bdf8; margin:0 0 6px 0; font-size:0.9rem; font-family:'JetBrains Mono', monospace;">II. 증언 (TESTIMONIUM) — THE TESTIMONY</h4>
              <p style="color:#cbd5e1; margin:0; line-height:1.6; font-size:0.88rem; font-style:italic;">{t['testimony']}</p>
            </div>

            <div style="background:#0b1120; padding:14px; border:1px solid #1e293b; border-radius:4px;">
              <h4 style="color:#ef5b55; margin:0 0 6px 0; font-size:0.9rem; font-family:'JetBrains Mono', monospace;">III. 기록 (REGISTRUM) — DIRECTORATE RECORD</h4>
              <p style="color:#94a3b8; margin:0; line-height:1.6; font-size:0.88rem;">{t['record']}</p>
            </div>
          </div>

          <div style="margin-top:16px; padding-top:12px; border-top:1px solid #1e293b; display:flex; flex-wrap:wrap; gap:12px; font-size:0.8rem; font-family:'JetBrains Mono', monospace;">
            <span style="color:#64748b;">EXTRACTABLE M.A.W.:</span>
            <a href="../{w['file']}" style="color:#f1df76; text-decoration:none;">⚔️ {w['name']} ({w['id']})</a>
            <span style="color:#334155;">·</span>
            <a href="../{s['file']}" style="color:#38bdf8; text-decoration:none;">🛡️ {s['name']} ({s['id']})</a>
            <span style="color:#334155;">·</span>
            <a href="../{g['file']}" style="color:#10b981; text-decoration:none;">✨ {g['name']} ({g['id']})</a>
          </div>
        </article>
"""
    tales_cards.append(card)

tales_html_body = "".join(tales_cards)

tales_page_content = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Entity Tales (슬픔의 이야기) — Somnarak Directorate Wiki</title>
  <meta name="description" content="Canonical narrative chronicles, survivor testimonies, and Directorate records for all Sorrow Entities.">
  <link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg">
  <link rel="stylesheet" href="../assets/css/wiki.css">
  <script defer src="../assets/js/wiki.js"></script>
</head>
<body>
  <header class="utility">
    <div class="utility-left">
      <button class="nav-open" type="button" aria-label="Open navigation">☰</button>
      <a class="utility-brand" href="../index.html">SOMNARAK.WIKI</a>
      <span class="utility-era">YEAR 4,238 · DAWN INITIATIVE</span>
    </div>
    <nav aria-label="Main navigation">
      <a href="../index.html">Main page</a>
      <a href="../characters/index.html">Characters</a>
      <a href="index.html" class="active">Lore</a>
      <a href="../factions/index.html">Factions</a>
      <a href="../departments/index.html">Departments</a>
      <a href="../locations/index.html">Locations</a>
      <a href="../mechanics/index.html">Mechanics</a>
      <a href="../entities/index.html">Sorrow Entities</a>
      <a href="../maw/index.html">M.A.W.</a>
    </nav>
    <div class="search">
      <input id="search" data-index="../data/search.json" aria-label="Search" placeholder="Search Somnarak Wiki">
      <div id="results"></div>
    </div>
  </header>

  <div class="layout">
    <aside class="rail" aria-label="Site navigation">
      <div class="brand">
        <img src="../assets/icons/somnarak_icon.svg" alt="Somnarak Crest" class="brand-logo" width="36" height="36">
        <div>
          <div class="brand-title">SOMNARAK</div>
          <div class="brand-sub">DIRECTORATE CODEX</div>
        </div>
      </div>
      <div class="nav-section">
        <div class="nav-section-title">CODEX DIRECTORY</div>
        <a href="../index.html">Main Portal</a>
        <a href="../entities/index.html">Sorrow Entities</a>
        <a href="../maw/index.html">M.A.W. Armory</a>
        <a href="../departments/index.html">Facility 01 Floors</a>
        <a href="../characters/index.html">Echo-Cores &amp; Leads</a>
        <a href="index.html" class="active">Lore &amp; Cosmology</a>
        <a href="../locations/index.html">Metropolitan Atlas</a>
        <a href="../mechanics/index.html">Battle Mechanics</a>
        <a href="../factions/index.html">Factions &amp; Guilds</a>
      </div>
      <div class="nav-section">
        <div class="nav-section-title">HISTORICAL CHRONICLES</div>
        <a href="timeline-1778-cycles.html">1,778 Cycles Timeline</a>
        <a href="the-seven-taboos.html">The Seven Taboos</a>
        <a href="entity-tales.html" class="active">Entity Tales (이야기)</a>
        <a href="facility-incident-reports.html">Incident Reports 001–010</a>
      </div>
    </aside>

    <main class="content">
      <div class="hero-banner" style="background: linear-gradient(135deg, rgba(8, 14, 26, 0.95), rgba(15, 23, 42, 0.9)), url('../assets/icons/banner_lore.svg') center/cover;">
        <div class="hero-badge">CANONICAL ANTHOLOGY // ARCHIVAL SECTION 09</div>
        <h1 class="hero-title" style="font-size:2.2rem; color:#f8fafc; font-family:'Cinzel', serif;">ENTITY TALES (슬픔의 이야기)</h1>
        <p class="hero-subtitle" style="color:#94a3b8; max-width:850px;">
          The tripartite narrative records of Somnarak's Sorrow Entities. Every tale adheres to the canonical Korean folkloric structure: <b>이야기 (The Tale)</b>, <b>증언 (The Testimony)</b>, and <b>기록 (The Directorate Record)</b>.
        </p>
      </div>

      <div class="article-body">
        <div class="toc" id="toc">
          <div class="toc-title">TABLE OF CONTENTS <button type="button" class="toc-toggle">[hide]</button></div>
          <ol>
            {"".join([f'<li><a href="#{e["id"].lower()}-tale">{e["id"]} — {e["name_en"]} ({e["name_kr"]})</a></li>' for e in ENTITIES_MASTER])}
          </ol>
        </div>

        <section style="margin-top:28px;">
          {tales_html_body}
        </section>
      </div>

      <footer class="footer">
        <div class="footer-top">
          <div class="footer-brand">
            <img src="../assets/icons/somnarak_icon.svg" alt="Somnarak Crest" width="40" height="40">
            <div>
              <div class="footer-title">THE REVERIE DIRECTORATE</div>
              <div class="footer-sub">Subterranean Facility 01 · Primary Archival Network</div>
            </div>
          </div>
        </div>
        <div class="footer-bottom">
          <span>PROJECT SOMNARAK ENCYCLOPEDIA · CANONICAL CODEX</span>
          <span>CYCLE 1,778 · YEAR 4,238</span>
        </div>
      </footer>
    </main>
  </div>
</body>
</html>
"""

with open(f'{wiki_root}/lore/entity-tales.html', 'w', encoding='utf-8') as f:
    f.write(tales_page_content)
print("SUCCESS: Wrote /home/user/01_Somnarak_Wiki/lore/entity-tales.html")

# 2. REBUILD /entities/index.html (Entity Codex) WITH 100% MATCHED DESIGNATIONS & NAMES
entity_cards = []
for e in ENTITIES_MASTER:
    w = e['maw_weapon']
    s = e['maw_suit']
    g = e['maw_gift']
    card = f"""
          <!-- {e['id']} -->
          <div class="pm-entity-card" style="border:2px solid {e['element_color']}; background:#040d18;">
            <div class="entity-card-top">
              <img src="../{e['icon']}" alt="{e['id']}" class="entity-card-icon">
              <div class="entity-card-meta">
                <span class="risk-badge risk-{e['risk']}">{e['risk_symbol']} ({e['risk']})</span>
                <span class="damage-badge" style="border-color:{e['element_color']}; color:{e['element_color']};">{e['element']} DAMAGE</span>
                <div style="font-size:0.75rem; color:#f1df76; font-family:'JetBrains Mono', monospace; margin-top:4px;">{e['floor'].upper()}</div>
              </div>
            </div>
            <h3 class="entity-card-name" style="color:{e['element_color']};">{e['id']}: {e['name_en'].upper()}</h3>
            <div style="font-size:0.8rem; color:#64748b; font-family:'JetBrains Mono', monospace; margin-bottom:6px;">{e['name_kr']}</div>
            <p class="entity-card-desc">"{e['tale']['quote']}" {e['tale']['narrative'][:120]}...</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:14px; display:flex; justify-content:space-between;">
              <span><b>DAMAGE:</b> <span style="color:{e['element_color']};">{e['element']}</span></span>
              <span><b>WORK:</b> {e['work_pref'].split('·')[0].strip()}</span>
            </div>
            <div style="display:flex; gap:8px;">
              <a href="{os.path.basename(e['file'])}" class="jump-btn" style="flex:1; text-align:center;">FULL DOSSIER →</a>
              <a href="../lore/entity-tales.html#{e['id'].lower()}-tale" class="jump-btn" style="border-color:#f1df76; color:#f1df76;" title="Read Tale">이야기</a>
            </div>
          </div>
"""
    entity_cards.append(card)

with open(f'{wiki_root}/entities/index.html', 'r', encoding='utf-8') as f:
    e_html = f.read()

old_grid_pattern = r'<div class="hub-grid-3">[\s\S]*?<\/div>\s*<\/div>\s*<!-- Master Footer'
replacement = '<div class="hub-grid-3">' + "".join(entity_cards) + '        </div>\n      </div>\n\n      <!-- Master Footer'
new_e_html = re.sub(old_grid_pattern, replacement, e_html)
with open(f'{wiki_root}/entities/index.html', 'w', encoding='utf-8') as f:
    f.write(new_e_html)
print("SUCCESS: Synchronized /entities/index.html (Entity Codex) with 100% matched designations & tales!")

# 3. REBUILD /maw/index.html (M.A.W. Codex) WITH ALL 39 WEAPONS, SUITS, AND GIFTS
maw_weapons_rows = []
maw_suits_rows = []
maw_gifts_rows = []

for e in ENTITIES_MASTER:
    w = e['maw_weapon']
    s = e['maw_suit']
    g = e['maw_gift']
    
    # Weapon Row
    w_row = f"""
            <tr>
              <td><span class="damage-badge" style="color:{e['element_color']}; border-color:{e['element_color']};">{e['element']}</span></td>
              <td><b><a href="{os.path.basename(w['file'])}" style="color:#f1df76; text-decoration:none;">{w['name']}</a></b><br><small style="color:#64748b;">{w['id']}</small></td>
              <td><span class="risk-badge risk-{e['risk']}">{e['risk_symbol']} ({e['risk']})</span></td>
              <td><a href="../{e['file']}" style="color:#38bdf8; text-decoration:none;">{e['id']} {e['name_en']}</a></td>
              <td style="font-family:'JetBrains Mono', monospace; color:#cbd5e1;">{w['dmg']}</td>
              <td><a href="{os.path.basename(w['file'])}" class="jump-btn" style="padding:4px 10px; font-size:0.75rem;">VIEW →</a></td>
            </tr>
"""
    maw_weapons_rows.append(w_row)

    # Suit Row
    s_row = f"""
            <tr>
              <td><span class="damage-badge" style="color:{e['element_color']}; border-color:{e['element_color']};">{e['element']}</span></td>
              <td><b><a href="{os.path.basename(s['file'])}" style="color:#38bdf8; text-decoration:none;">{s['name']}</a></b><br><small style="color:#64748b;">{s['id']}</small></td>
              <td><span class="risk-badge risk-{e['risk']}">{e['risk_symbol']} ({e['risk']})</span></td>
              <td><a href="../{e['file']}" style="color:#38bdf8; text-decoration:none;">{e['id']} {e['name_en']}</a></td>
              <td style="font-family:'JetBrains Mono', monospace; color:#cbd5e1;">{s['res']}</td>
              <td><a href="{os.path.basename(s['file'])}" class="jump-btn" style="padding:4px 10px; font-size:0.75rem;">VIEW →</a></td>
            </tr>
"""
    maw_suits_rows.append(s_row)

    # Gift Row
    g_row = f"""
            <tr>
              <td><span class="damage-badge" style="color:{e['element_color']}; border-color:{e['element_color']};">{e['element']}</span></td>
              <td><b><a href="{os.path.basename(g['file'])}" style="color:#10b981; text-decoration:none;">{g['name']}</a></b><br><small style="color:#64748b;">{g['id']}</small></td>
              <td><span class="risk-badge risk-{e['risk']}">{e['risk_symbol']} ({e['risk']})</span></td>
              <td><a href="../{e['file']}" style="color:#38bdf8; text-decoration:none;">{e['id']} {e['name_en']}</a></td>
              <td style="font-family:'JetBrains Mono', monospace; color:#cbd5e1;">{g['stat']}</td>
              <td><a href="{os.path.basename(g['file'])}" class="jump-btn" style="padding:4px 10px; font-size:0.75rem;">VIEW →</a></td>
            </tr>
"""
    maw_gifts_rows.append(g_row)

maw_page_content = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>M.A.W. Armament Codex (실체화된 고통의 갑옷) — Somnarak Directorate Wiki</title>
  <meta name="description" content="Master registry of Materialized Agony Wear extracted from Sorrow Entities across all 4 elemental frequencies.">
  <link rel="icon" type="image/svg+xml" href="../assets/icons/somnarak_icon.svg">
  <link rel="stylesheet" href="../assets/css/wiki.css">
  <script defer src="../assets/js/wiki.js"></script>
</head>
<body>
  <header class="utility">
    <div class="utility-left">
      <button class="nav-open" type="button" aria-label="Open navigation">☰</button>
      <a class="utility-brand" href="../index.html">SOMNARAK.WIKI</a>
      <span class="utility-era">YEAR 4,238 · DAWN INITIATIVE</span>
    </div>
    <nav aria-label="Main navigation">
      <a href="../index.html">Main page</a>
      <a href="../characters/index.html">Characters</a>
      <a href="../lore/index.html">Lore</a>
      <a href="../factions/index.html">Factions</a>
      <a href="../departments/index.html">Departments</a>
      <a href="../locations/index.html">Locations</a>
      <a href="../mechanics/index.html">Mechanics</a>
      <a href="../entities/index.html">Sorrow Entities</a>
      <a href="index.html" class="active">M.A.W.</a>
    </nav>
    <div class="search">
      <input id="search" data-index="../data/search.json" aria-label="Search" placeholder="Search Somnarak Wiki">
      <div id="results"></div>
    </div>
  </header>

  <div class="layout">
    <aside class="rail" aria-label="Site navigation">
      <div class="brand">
        <img src="../assets/icons/somnarak_icon.svg" alt="Somnarak Crest" class="brand-logo" width="36" height="36">
        <div>
          <div class="brand-title">SOMNARAK</div>
          <div class="brand-sub">DIRECTORATE CODEX</div>
        </div>
      </div>
      <div class="nav-section">
        <div class="nav-section-title">CODEX DIRECTORY</div>
        <a href="../index.html">Main Portal</a>
        <a href="../entities/index.html">Sorrow Entities</a>
        <a href="index.html" class="active">M.A.W. Armory</a>
        <a href="../departments/index.html">Facility 01 Floors</a>
        <a href="../characters/index.html">Echo-Cores &amp; Leads</a>
        <a href="../lore/index.html">Lore &amp; Cosmology</a>
        <a href="../locations/index.html">Metropolitan Atlas</a>
        <a href="../mechanics/index.html">Battle Mechanics</a>
        <a href="../factions/index.html">Factions &amp; Guilds</a>
      </div>
      <div class="nav-section">
        <div class="nav-section-title">ARMORY SECTIONS</div>
        <a href="#weapons">M.A.W. Weapons (무기)</a>
        <a href="#suits">M.A.W. Suits (갑옷)</a>
        <a href="#gifts">M.A.W. Gifts (선물)</a>
        <a href="maw-crafting-and-extraction.html">Extraction Protocols</a>
        <a href="maw-set-synergies.html">Set Synergies</a>
      </div>
    </aside>

    <main class="content">
      <div class="hero-banner" style="background: linear-gradient(135deg, rgba(8, 14, 26, 0.95), rgba(15, 23, 42, 0.9)), url('../assets/icons/banner_maw.svg') center/cover;">
        <div class="hero-badge">ARMAMENT CODEX // REGISTRY 04</div>
        <h1 class="hero-title" style="font-size:2.2rem; color:#f8fafc; font-family:'Cinzel', serif;">M.A.W. ARMAMENT CODEX (실체화된 고통의 갑옷)</h1>
        <p class="hero-subtitle" style="color:#94a3b8; max-width:850px;">
          Materialized Agony Wear extracted from contained Sorrow Entities. Every piece resonates with the crystallized emotional trauma of its source specimen, converting raw sorrow into lethal offensive and defensive frequencies.
        </p>
      </div>

      <div class="article-body">
        <div class="toc" id="toc">
          <div class="toc-title">TABLE OF CONTENTS <button type="button" class="toc-toggle">[hide]</button></div>
          <ol>
            <li><a href="#weapons">1. M.A.W. Weapons Registry (무기 — 13 Weapons)</a></li>
            <li><a href="#suits">2. M.A.W. Suits Registry (갑옷 — 13 Suits)</a></li>
            <li><a href="#gifts">3. M.A.W. Gifts &amp; Accessories (선물 — 13 Gifts)</a></li>
            <li><a href="#rules">4. M.A.W. Calibration &amp; Corrosion Protocols</a></li>
          </ol>
        </div>

        <section id="weapons" style="margin-top:28px;">
          <h2 style="color:#f1df76; border-bottom:1px solid #334155; padding-bottom:8px; font-family:'Cinzel', serif;">1. M.A.W. WEAPONS REGISTRY (무기)</h2>
          <p style="color:#94a3b8;">Offensive weaponry extracted from contained Sorrow Entities, inflicting element-specific trauma matching the source entity's resonance.</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead>
                <tr>
                  <th>ELEMENT</th>
                  <th>WEAPON NAME &amp; ID</th>
                  <th>GRADE</th>
                  <th>SOURCE ENTITY</th>
                  <th>BASE DAMAGE</th>
                  <th>ACTION</th>
                </tr>
              </thead>
              <tbody>
                {"".join(maw_weapons_rows)}
              </tbody>
            </table>
          </div>
        </section>

        <section id="suits" style="margin-top:36px;">
          <h2 style="color:#38bdf8; border-bottom:1px solid #334155; padding-bottom:8px; font-family:'Cinzel', serif;">2. M.A.W. SUITS &amp; ARMOR REGISTRY (갑옷)</h2>
          <p style="color:#94a3b8;">Defensive armor sets forged from entity carapaces and woven trauma filaments, reducing incoming elemental damage multipliers.</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead>
                <tr>
                  <th>ELEMENT</th>
                  <th>SUIT NAME &amp; ID</th>
                  <th>GRADE</th>
                  <th>SOURCE ENTITY</th>
                  <th>RESISTANCE PROFILE</th>
                  <th>ACTION</th>
                </tr>
              </thead>
              <tbody>
                {"".join(maw_suits_rows)}
              </tbody>
            </table>
          </div>
        </section>

        <section id="gifts" style="margin-top:36px;">
          <h2 style="color:#10b981; border-bottom:1px solid #334155; padding-bottom:8px; font-family:'Cinzel', serif;">3. M.A.W. GIFTS &amp; ACCESSORIES (선물)</h2>
          <p style="color:#94a3b8;">Spontaneously manifested bodily ornaments and implants bestowed upon agents who achieve high synchronization during Work protocols.</p>
          <div class="table-wrap">
            <table class="data-table">
              <thead>
                <tr>
                  <th>ELEMENT</th>
                  <th>GIFT NAME &amp; ID</th>
                  <th>GRADE</th>
                  <th>SOURCE ENTITY</th>
                  <th>PASSIVE ATTRIBUTE BONUS</th>
                  <th>ACTION</th>
                </tr>
              </thead>
              <tbody>
                {"".join(maw_gifts_rows)}
              </tbody>
            </table>
          </div>
        </section>
      </div>

      <footer class="footer">
        <div class="footer-top">
          <div class="footer-brand">
            <img src="../assets/icons/somnarak_icon.svg" alt="Somnarak Crest" width="40" height="40">
            <div>
              <div class="footer-title">THE REVERIE DIRECTORATE</div>
              <div class="footer-sub">Subterranean Facility 01 · Extraction &amp; Calibration Armory</div>
            </div>
          </div>
        </div>
        <div class="footer-bottom">
          <span>PROJECT SOMNARAK ENCYCLOPEDIA · CANONICAL CODEX</span>
          <span>CYCLE 1,778 · YEAR 4,238</span>
        </div>
      </footer>
    </main>
  </div>
</body>
</html>
"""

with open(f'{wiki_root}/maw/index.html', 'w', encoding='utf-8') as f:
    f.write(maw_page_content)
print("SUCCESS: Synchronized /maw/index.html (M.A.W. Codex) with all 39 weapons, suits, and gifts!")
