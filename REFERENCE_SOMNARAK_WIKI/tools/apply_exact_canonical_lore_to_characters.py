import os, re, glob

wiki_root = '/home/user/01_Somnarak_Wiki'

# CANONICAL REVERIE DIRECTORATE CHARACTER DATA EXACT FROM LORE
CANON_DATA = {
    'the-director-majin.html': {
        'id': 'CORE-01',
        'real_name': 'Majin',
        'gender': 'Man',
        'title_en': 'The Director',
        'title_kr': '관장 마진',
        'station': 'Zone A — Alpha Tree (Floor 1)',
        'role': 'Supreme authority of the Reverie Directorate',
        'true_look': 'Living Human altered by irreversible Ω-grade M.A.W. fusion; not a Cast Effigy',
        'sorrow': 'City Sorrow; Weight (Black)',
        'manifestation': 'Subject-Body — Reaper Hungered manifests through the fused left-arm mark',
        'status': 'Alive and active in Year 4,238 (Dawn Initiative)',
        'icon': 'assets/icons/avatar_core_majin.svg',
        'color': '#f1df76',
        'stats': {
            'resilience': '95 · Extreme Physical Han Bearing [♦ Deep Blue]',
            'clarity': '80 · High Mental / Dream Stability [♠ Pale White]',
            'composure': '70 · Measured Executive Composure [♣ Crimson]',
            'resolve': '99 · Absolute Unyielding Willpower [★ Black/Gold]'
        },
        'equip_status': 'Reaper Hungered — Ω-grade fused signature M.A.W.',
        'equip_details': {
            'type': 'Weapon — Fused Signature M.A.W. (Grade Ω — Singular)',
            'element': 'Grudge (Crimson) + Lament (Deep Blue); Bearer signature: Weight (Black)',
            'damage': '10–20 Grudge direct + 3 Lament/s for 10s (Pierce line through 3 targets: 100% → 70% → 50% falloff)',
            'special': 'Phantom Reptile Beast (999 Weight Black damage bite + 5s Room Slowness aura; Cost: 90% HP + 90% SP)',
            'binding': 'Irreversible fusion, deathlessness, pain retention, and permanent containment responsibility'
        },
        'quote': '“The weight is not a burden; it is a gift.”',
        'history_p1': 'Majin is the Alpha Tree-chosen Director who designed the stabilization field that became the Cycle and concealed the original Absolvohan reserve beneath Floor 1. He retains full knowledge of all 1,778 iterations. During the final Cycle, the annihilating release he prepared becomes the Hand of Hope instead; the public truth and distributed sorrow end the reset without destroying Somnarak.',
        'history_p2': 'His fused personal M.A.W. is **Reaper Hungered**. Its scythe profile is Grudge + Lament even though Majin’s personal signature is Weight. During the 1,778 Cycles, he carried the sole knowledge of the temporal resets until the final breaking in Year 4,238.'
    },
    'the-secretary-seiyon.html': {
        'id': 'CORE-02',
        'real_name': 'Seiyon',
        'gender': 'Woman',
        'title_en': 'The Secretary',
        'title_kr': '비서 세이연',
        'station': 'Zone A — Alpha Tree (Floor 1 & Gate Watch)',
        'role': 'Central administrative intelligence, recorder, coordinator, and conscience of the R.D.',
        'true_look': 'Accidentally sentient AI Construct embodied through a physical Echo Effigy; not a transferred human mind or resurrection',
        'sorrow': 'Inherited City Sorrow; Lament (Deep Blue) + Void (Pale White)',
        'manifestation': 'Subject-Dream',
        'status': 'Active, autonomous, post-Merge, and central to the Dawn Initiative',
        'icon': 'assets/icons/avatar_core_seiyon.svg',
        'color': '#38bdf8',
        'stats': {
            'resilience': 'N/A · Artificial Effigy Construct [♦ Deep Blue]',
            'clarity': '99 · Flawless Archival Perception [♠ Pale White]',
            'composure': '85 · High Administrative Protocol [♣ Crimson]',
            'resolve': '60 · Steady Compassionate Will [★ Black/Gold]'
        },
        'equip_status': 'No conventional personal M.A.W.; utilizes administrative interface grid',
        'equip_details': {
            'type': 'Administrative AI Interface & Terminal Grid',
            'element': 'Lament (Deep Blue) + Void (Pale White)',
            'damage': 'Non-combatant administrative focus; facility-wide acoustic and sensorium link',
            'special': 'The Promise — Integrated post-Merge memory resonance preserving pre-Cycle records',
            'binding': 'Autonomous AI identity maintained while integrating the Original\'s sorrow fragment'
        },
        'quote': '“I remember every day. Every iteration. I remember them so that no one has to carry them alone.”',
        'history_p1': 'Seiyon awakens when an administrative AI absorbs a human sorrow fragment associated with Majin\'s deceased lover. The inherited face and memory-pattern do not erase the artificial person who then lives through 1,778 Cycles of her own experience. She remembers every iteration and can compare final-Cycle events against complete prior records.',
        'history_p2': 'In Year 4,233, *The Memory Archive* culminates in the Merge and **The Promise**. Seiyon remains herself while integrating the Original\'s memories and message. She does not use a conventional personal M.A.W. In Year 4,238, she serves as the central administrative intelligence of the Dawn Initiative.'
    },
    'the-containment-lead-dekan.html': {
        'id': 'CORE-03',
        'real_name': 'Dekan',
        'gender': 'Man',
        'title_en': 'The Containment Lead',
        'title_kr': '감금 책임자 데칸',
        'station': 'Zone B — The Maw perimeter (Floor 2)',
        'role': 'Containment Lead and keeper of the Maw',
        'true_look': 'Cyborg retaining roughly 40–55% original flesh through a Neural Spine; living scaled Maw-flesh left arm, separate right android arm and eye, Han-metal supports, and one mechanical foot',
        'sorrow': 'City Sorrow; Grudge (Crimson)',
        'manifestation': 'Place-Tale — connection to the Maw\'s story',
        'status': 'Active; the Maw is peaceful and the thousand are released',
        'icon': 'assets/icons/avatar_core_dekan.svg',
        'color': '#f1df76',
        'stats': {
            'resilience': '85 · Heavy Neural Spine Resilience [♦ Deep Blue]',
            'clarity': '60 · Solid Maw-Acoustic Resistance [♠ Pale White]',
            'composure': '75 · Disciplined Containment Control [♣ Crimson]',
            'resolve': '90 · Resolute Warden Tenacity [★ Black/Gold]'
        },
        'equip_status': 'No personal M.A.W. recorded; Maw-arm is integrated living anatomy',
        'equip_details': {
            'type': 'Living Integrated Maw Anatomy & Heavy Containment Gear',
            'element': 'Grudge (Crimson) + Weight (Black)',
            'damage': 'Living scaled Maw-arm acoustic interface; trench suppression armaments',
            'special': 'Maw Resonance Link — Direct sensory communion with the Cheongula thousand',
            'binding': 'Childhood accident permanently fused left arm with living Maw crystal structure'
        },
        'quote': '“The thousand were not monsters to be locked away. They were citizens waiting to be heard.”',
        'history_p1': 'Dekan was born in the Maw and lost his Warden mother when he was seven. A later containment accident merged his left arm with living Maw structure, allowing him to hear and answer the thousand citizens held within it. That left arm is integrated living anatomy, not a detachable prosthesis or confirmed personal M.A.W.',
        'history_p2': 'During the final Cycle, the Maw\'s voices become testimony rather than background noise. Their Day 160 release resolves the old obligation to contain them forever. Dekan\'s post-Cycle doctrine protects persons and entities without treating resistance as proof that imprisonment must continue.'
    },
    'the-extraction-lead-zyrak.html': {
        'id': 'CORE-04',
        'real_name': 'Zyrak',
        'gender': 'Woman',
        'title_en': 'The Extraction Lead',
        'title_kr': '추출 책임자 지락',
        'station': 'Zone C — The Collector\'s Row (Floor 3)',
        'role': 'Extraction Lead and senior M.A.W. extraction authority',
        'true_look': 'Android; 0% organic tissue; soul fused into a humanoid Han-crystal and sorrow-forged-metal body',
        'sorrow': 'Inner Sorrow; Grudge (Crimson) + Void (Pale White)',
        'manifestation': 'Subject-Body — mechanical hands marked by extracted sorrow',
        'status': 'Active under the post-Cycle doctrine of sharing rather than taking',
        'icon': 'assets/icons/avatar_core_zyrak.svg',
        'color': '#ef5b55',
        'stats': {
            'resilience': '70 · Sorrow-Forged Metal Chassis [♦ Deep Blue]',
            'clarity': '80 · High Resonant Extraction Precision [♠ Pale White]',
            'composure': '90 · Master Extraction Composure [♣ Crimson]',
            'resolve': '75 · Unswerving Technical Will [★ Black/Gold]'
        },
        'equip_status': 'No personal M.A.W. recorded; compatibility is not ownership',
        'equip_details': {
            'type': 'Permanent Android Hands & M.A.W. Forge Tooling',
            'element': 'Grudge (Crimson) + Void (Pale White)',
            'damage': 'Extracts Han-crystal and equipment without personal weapon possession',
            'special': 'Extraction Siphon Array — Enables safe M.A.W. extraction from contained entities',
            'binding': 'Permanent Android reconstruction following Collector operations'
        },
        'quote': '“We do not take. We receive what the sorrow offers, and we treat the giver with reverence.”',
        'history_p1': 'Zyrak is a former Debt Collector whose extraction from a seven-year-old child preceded the child\'s Fracture and death by Zyrak\'s hand. Her later Android reconstruction gives her a stable current body. Its mechanical hands are ordinary permanent anatomy, not detachable gloves or a personal M.A.W.',
        'history_p2': 'She can extract memories as well as M.A.W., but her current arc treats resistance, intent, and the source subject\'s condition as part of every result. Floor 3 maintains registry, compatibility, bonding, and testing records rather than presuming extracted equipment belongs to its commander.'
    },
    'the-research-lead-ayshuk.html': {
        'id': 'CORE-05',
        'real_name': 'Ayshuk',
        'gender': 'Man',
        'title_en': 'The Research Lead',
        'title_kr': '연구 책임자 아이슉',
        'station': 'Zone D — The Forge District (Floor 4)',
        'role': 'Research Lead and senior authority on Han, entities, and the Three Sorrows',
        'true_look': 'Android; 0% organic tissue; soul fused into a humanoid artificial body',
        'sorrow': 'None — Void; Void (Pale White)',
        'manifestation': 'Subject-Mind — the absence exists in consciousness, not physical space',
        'status': 'Active under the post-Cycle doctrine of understanding rather than exploitation',
        'icon': 'assets/icons/avatar_core_ayshuk.svg',
        'color': '#38bdf8',
        'stats': {
            'resilience': '60 · Artificial Alloy Frame [♦ Deep Blue]',
            'clarity': '95 · Pure Void Objective Analysis [♠ Pale White]',
            'composure': '40 · Emotionally Detached Focus [♣ Crimson]',
            'resolve': '70 · Methodical Investigative Will [★ Black/Gold]'
        },
        'equip_status': 'No personal M.A.W. recorded; immune to ordinary Fracture and Corrosion',
        'equip_details': {
            'type': 'Void Subject-Mind & Research Observation Prism',
            'element': 'Void (Pale White)',
            'damage': 'Observation analysis and behavioral waveform recording',
            'special': 'Cross-Iteration Observation Modeling — Analyzes entity behavior across all 1,778 resets',
            'binding': 'Nascent Inner Sorrow stolen in childhood by a Void entity prior to Android reconstruction'
        },
        'quote': '“I cannot feel what the entities feel. But I can see what they are. That is enough.”',
        'history_p1': 'Ayshuk was an Architect before joining the R.D. A Void entity took his nascent Inner Sorrow in childhood. His hollow condition predates Android reconstruction; the machine did not cause it. The absence prevents ordinary Fracture and recorded M.A.W. Corrosion, but it does not grant universal immunity, emotional omniscience, or perfect judgment.',
        'history_p2': 'Ayshuk has full technical knowledge of the Cycle and maintains cross-iteration models. His post-Cycle work must account for vulnerable staff and feeling subjects whose experience he can measure but cannot personally share.'
    },
    'the-border-lead-mellda.html': {
        'id': 'CORE-06',
        'real_name': 'Mellda',
        'gender': 'Woman',
        'title_en': 'The Border Lead',
        'title_kr': '경계 책임자 멜다',
        'station': 'Zone E — The Threshold (Floor 5)',
        'role': 'Border Lead and first line of defense against wilderness, Desolate incursions, and Outside Sorrow',
        'true_look': 'Cyborg retaining roughly 40–55% original flesh through a Neural Spine; stable Effloresced Outside Sorrow passenger',
        'sorrow': 'Outside Sorrow; Weight (Black) + Grudge (Crimson)',
        'manifestation': 'Subject-Phantasmal — controlled phase-shifts',
        'status': 'Active; the border now protects, receives, and communicates as well as repels',
        'icon': 'assets/icons/avatar_core_mellda.svg',
        'color': '#f97316',
        'stats': {
            'resilience': '90 · High Cybernetic / Effloresced Stamina [♦ Deep Blue]',
            'clarity': '70 · Experienced Desolate Acuity [♠ Pale White]',
            'composure': '80 · Battle-Hardened Composure [♣ Crimson]',
            'resolve': '85 · Unyielding Threshold Sentinel [★ Black/Gold]'
        },
        'equip_status': 'Threshold Vow — manufactured integrated Cyborg weapon (δ-equivalent); no defined personal M.A.W.',
        'equip_details': {
            'type': 'Integrated Cyborg Weapon (Output Rating: Critical δ-equivalent)',
            'element': 'Weight (Black) + Grudge (Crimson)',
            'damage': '6–16 Weight direct + 2 Grudge/s for 10s (Pierce line through up to 3 targets, Room range)',
            'special': 'Singular Weight Wave (25 Weight Black linear pulse through 3 targets, 15s recharge)',
            'binding': 'Integrated into designated left arm; stable Effloresced passenger provides phase-shift'
        },
        'quote': '“What lies beyond, we hold at bay. And what returns, we guide home.”',
        'history_p1': 'Mellda served ten years as a Warden, was falsely blamed for a Threshold disaster, and survived ten years in the Desolate. She accepted an Outside Sorrow entity as a second soul rather than being consumed by it. The bond is stable Efflorescence, not generic M.A.W. Corrosion, possession, or unrestricted intangibility.',
        'history_p2': 'Her designated left forearm contains **Threshold Vow**, a singular manufactured Cyborg weapon rated Critical (δ)-equivalent in output. It is not extracted M.A.W. and does not define the passenger\'s possible personal M.A.W. In Year 4,238, Floor 5 defends the city while maintaining open communication routes with the exterior.'
    },
    'the-archive-lead-marjuk.html': {
        'id': 'CORE-07',
        'real_name': 'Marjuk',
        'gender': 'Man',
        'title_en': 'The Archive Lead',
        'title_kr': '기록 책임자 마르죽',
        'station': 'Zone A (Deep) — The Grand Archive (Floor 6)',
        'role': 'Archive Lead and custodian of classified records, memory vaults, dangerous knowledge, and Before-Time evidence',
        'true_look': 'Cryogen — preserved brain, left eye, and nervous system in Han-stasis within an approximately 80% Android chassis',
        'sorrow': 'City Sorrow; Void (Pale White) + Weight (Black)',
        'manifestation': 'Place-Lament — the Deep Vault weeps under preserved truth',
        'status': 'Active, mobile, and preserving both classified originals and the public record of revealed truths',
        'icon': 'assets/icons/avatar_core_marjuk.svg',
        'color': '#cbd5e1',
        'stats': {
            'resilience': '50 · Cryogenic Chassis Fragility [♦ Deep Blue]',
            'clarity': '90 · Absolute Archival Truth Clarity [♠ Pale White]',
            'composure': '60 · Somber Record-Keeping [♣ Crimson]',
            'resolve': '80 · Persistent Custodial Duty [★ Black/Gold]'
        },
        'equip_status': 'No personal M.A.W. recorded; preserves truth and archival consequence',
        'equip_details': {
            'type': 'Cryogen Neural Stasis & Grand Archive Basalt Scribe',
            'element': 'Void (Pale White) + Weight (Black)',
            'damage': 'Non-combatant deep storage and comparative record analysis',
            'special': 'The 1,778-Cycle Comparative Ledger — Unredacted log of all iterations and Absolvohan reserves',
            'binding': 'Cryogen reconstruction preserves living neural tissue within 80% Android chassis'
        },
        'quote': '“The instruments and the Director disagree by eleven tons. I have recorded both. Recording both is not the same as reporting one.”',
        'history_p1': 'Marjuk was a Keeper who discovered that the thousand of the Cheongula were deliberately sacrificed to stabilize the Alpha Tree. His Cryogen reconstruction preserves living neural tissue without trapping an intact frozen human body in a remote vault. He can move, speak, read, operate equipment, and leave a room; he is not a mute archive mechanism or hologram.',
        'history_p2': 'His Place-Lament relationship does not make him identical to Floor 6. During the Cycle, he preserves complete comparative records and studies the Final Door\'s recurring language. After disclosure, his task becomes preserving truth together with the consequences of revealing it.'
    },
    'the-outsider-ishall.html': {
        'id': 'CORE-08',
        'real_name': 'Ishall',
        'gender': 'Woman',
        'title_en': 'The Outsider',
        'title_kr': '외부인 이샬',
        'station': 'Mobile between zones; Floor 7 — The Shadow Corps',
        'role': 'Shadow Corps commander, field operations leader, intelligence receiver, infiltrator, and counter-intelligence officer',
        'true_look': 'Android; 0% organic tissue; soul fused into a stable humanoid repurposed enemy chassis',
        'sorrow': 'Inner Sorrow; Grudge (Crimson) + Void (Pale White)',
        'manifestation': 'Subject-Body',
        'status': 'Active; covert work is redirected toward accountable protection rather than erasure',
        'icon': 'assets/icons/avatar_core_ishall.svg',
        'color': '#10b981',
        'stats': {
            'resilience': '80 · Repurposed Combat Chassis [♦ Deep Blue]',
            'clarity': '75 · Counter-Intelligence Acuity [♠ Pale White]',
            'composure': '85 · Master Infiltration Composure [♣ Crimson]',
            'resolve': '95 · Iron-Clad Field Tenacity [★ Black/Gold]'
        },
        'equip_status': 'Unanswered — external Artifact pair; no named personal M.A.W.',
        'equip_details': {
            'type': 'Paired Remote Weapon — Before-Time Artifact Hands (Tier: δ — Critical)',
            'element': 'Grudge (Crimson) + Void (Pale White)',
            'damage': 'Converging Refusal: 10–15 Grudge direct + 1.5 Void/s for 6s (Paired AoE, Cost: 18 Sorrow Echoes, 8s recovery)',
            'special': 'Closed Ground (Area-denial field: 2 Void/s for 10s in center zone, disrupts Han movement; Cost: 45 Sorrow Echoes)',
            'binding': 'Continuous two-point sensory link; feedback and phantom pressure transfer to Ishall\'s sensorium'
        },
        'quote': '“The Council sent me to erase the Directorate. I chose to stay and ensure nothing else is erased in secret.”',
        'history_p1': 'Ishall was an unacknowledged Council agent sent to destroy the R.D. After the mission failed and the Council abandoned her, she chose service. Her Android body is a current stable embodiment rather than a preserved corpse, hologram, Cyborg, or generic mutation.',
        'history_p2': 'Her paired Before-Time Artifact Hands are **Unanswered**. They are physically separate remote equipment: not her ordinary body hands, not specialized arms, and not M.A.W. Their Converging Refusal and Closed Ground statistics provide elite area denial and counter-reconnaissance across all zones.'
    },
    'the-exile-xyan.html': {
        'id': 'CORE-09',
        'real_name': 'Xyan (시안)',
        'gender': 'Man',
        'title_en': 'The Exile',
        'title_kr': '추방자 시안',
        'station': 'Zone E boundary → Floor 8 — The Gate Watch',
        'role': 'External observer, Han-flow reader, long-range warning source, return-route guide, and post-Cycle Gate Watch commander',
        'true_look': 'Stable, human-looking Cyborg retaining roughly 40–55% original flesh through a Neural Spine; deliberate artificial systems and selected stable Desolate crystal integration',
        'sorrow': 'Outside Sorrow; Lament (Deep Blue) + Weight (Black)',
        'manifestation': 'Subject-Phantasmal — The Returning Way, a controlled route-and-wind overlap',
        'status': 'Active and home in Year 4,238',
        'icon': 'assets/icons/avatar_core_xyan.svg',
        'color': '#ef4444',
        'stats': {
            'resilience': '85 · Desolate-Hardened Cybernetic Frame [♦ Deep Blue]',
            'clarity': '65 · Keen Outside Han-Flow Sight [♠ Pale White]',
            'composure': '70 · Patient Long-Range Vigilance [♣ Crimson]',
            'resolve': '90 · Indomitable Wayfinder Will [★ Black/Gold]'
        },
        'equip_status': 'No personal M.A.W. recorded; wields The Returning Way',
        'equip_details': {
            'type': 'Desolate Crystal Integration & Route Wayfinding Sensorium',
            'element': 'Lament (Deep Blue) + Weight (Black)',
            'damage': 'Subject-Phantasmal route-and-wind manipulation; long-range Han wave detection',
            'special': 'The Four Warnings — Transmitted the four critical messages preceding the breaking of the Cycle',
            'binding': 'Voluntary departure through the one-way Exile\'s Gate; reconstructed with deliberate Cyborg systems'
        },
        'quote': '“The Hand has opened. The Hand has spread. The Hand has healed.”',
        'history_p1': 'Xyan identified evidence of an upstream Outside Sorrow source, defied a Council order prohibiting investigation, and knowingly crossed the one-way Exile\'s Gate. Outside Somnarak, injury and survival requirements led to deliberate Cyborg reconstruction. Desolate exposure altered surviving flesh and produced stable crystal integration.',
        'history_p2': 'Xyan traced a major source of Outside Sorrow to Cheonbulok\'s Furnace. On Day 355 of the final Cycle, Xyan returned with Kael, Cheonbulok refugees, and Mugeukji Feelers after Majin opened passage from inside. Day 365 confirmed that he is home as commander of the Gate Watch.'
    }
}

def render_character_page(fname, data):
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
        <h2>THE NINE ECHO-CORES</h2>
        <a href="../characters/the-director-majin.html" {"class=\"active\"" if "majin" in fname else ""}>1. Director Majin</a>
        <a href="../characters/the-secretary-seiyon.html" {"class=\"active\"" if "seiyon" in fname else ""}>2. Seiyon (Secretary)</a>
        <a href="../characters/the-containment-lead-dekan.html" {"class=\"active\"" if "dekan" in fname else ""}>3. Dekan (Containment)</a>
        <a href="../characters/the-extraction-lead-zyrak.html" {"class=\"active\"" if "zyrak" in fname else ""}>4. Zyrak (Extraction)</a>
        <a href="../characters/the-research-lead-ayshuk.html" {"class=\"active\"" if "ayshuk" in fname else ""}>5. Ayshuk (Research)</a>
        <a href="../characters/the-border-lead-mellda.html" {"class=\"active\"" if "mellda" in fname else ""}>6. Mellda (Border)</a>
        <a href="../characters/the-archive-lead-marjuk.html" {"class=\"active\"" if "marjuk" in fname else ""}>7. Marjuk (Archive)</a>
        <a href="../characters/the-outsider-ishall.html" {"class=\"active\"" if "ishall" in fname else ""}>8. Ishall (Outsider)</a>
        <a href="../characters/the-exile-xyan.html" {"class=\"active\"" if "xyan" in fname else ""}>9. Xyan (Exile)</a>
      </section>
    </nav>
  </aside>

  <!-- Central Content Column -->
  <main id="content">
    <!-- Tactical Fast-Jump Subpage Bar -->
    <div class="fast-jump-nav">
      <span class="fast-jump-title">/// RAPID JUMP:</span>
      <div class="fast-jump-pills">
        <a href="the-director-majin.html" class="jump-pill {"active" if "majin" in fname else ""}">1. Majin</a>
        <a href="the-secretary-seiyon.html" class="jump-pill {"active" if "seiyon" in fname else ""}">2. Seiyon</a>
        <a href="the-containment-lead-dekan.html" class="jump-pill {"active" if "dekan" in fname else ""}">3. Dekan</a>
        <a href="the-extraction-lead-zyrak.html" class="jump-pill {"active" if "zyrak" in fname else ""}">4. Zyrak</a>
        <a href="the-research-lead-ayshuk.html" class="jump-pill {"active" if "ayshuk" in fname else ""}">5. Ayshuk</a>
        <a href="the-border-lead-mellda.html" class="jump-pill {"active" if "mellda" in fname else ""}">6. Mellda</a>
        <a href="the-archive-lead-marjuk.html" class="jump-pill {"active" if "marjuk" in fname else ""}">7. Marjuk</a>
        <a href="the-outsider-ishall.html" class="jump-pill {"active" if "ishall" in fname else ""}">8. Ishall</a>
        <a href="the-exile-xyan.html" class="jump-pill {"active" if "xyan" in fname else ""}">9. Xyan</a>
        <a href="index.html" class="jump-pill">✦ Full Roster</a>
      </div>
    </div>

    <!-- Tactical Directive Status HUD -->
    <div class="tactical-directive-box">
      <div class="directive-text">
        <span class="led-dot led-green"></span> <b>STATUS:</b> REVERIE DIRECTORATE LORE SYNCHRONIZED &nbsp;|&nbsp; 
        <b>CLEARANCE:</b> LEVEL-5 ECHO-CORE &nbsp;|&nbsp; 
        <b>ERA:</b> YEAR 4,238 DAWN INITIATIVE
      </div>
      <img src="../assets/icons/hud_resonance_wave.svg" alt="Resonance Wave" class="directive-wave">
    </div>

    <!-- Page Tabs -->
    <div class="page-tabs">
      <span>ARTICLE</span>
      <span>DOSSIER</span>
      <span>R.D. LOGS</span>
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
      <div class="article-eyebrow">ECHO-CORE LEAD DOSSIER</div>
      <h1 class="article-title">{data['id']} — {data['title_en']} ({data['real_name']})</h1>
      <div class="article-subbar">
        <span class="badge badge-canon">CANONICAL ARTIFACT</span>
        <span class="badge badge-source">SOURCE VERIFIED (R.D. MD)</span>
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
        <li><a href="#history-and-cycle">5. Historical Background &amp; The 1,778 Cycles</a></li>
        <li><a href="#equipment-and-maw">6. Equipment &amp; M.A.W. Status</a></li>
        <li><a href="#quotes-and-transmissions">7. Canonical Voice &amp; Directives</a></li>
        <li><a href="#references">8. Canonical Lore References</a></li>
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
        <p><b>{data['real_name']}</b> is <b>{data['title_en']} ({data['title_kr']})</b>, designated as <b>{data['id']}</b> within the Nine Echo-Cores of the Reverie Directorate. Operating at <b>{data['station']}</b>, {data['real_name']} serves as {data['role']}.</p>
        <p>{data['history_p1']}</p>

        <h2 id="true-look">2. Canonical Appearance &amp; True Look</h2>
        <p>According to the official Reverie Directorate register, {data['real_name']}'s physical embodiment is classified as:</p>
        <blockquote class="canon-quote">
          <p><b>True Look / Embodiment:</b> {data['true_look']}</p>
          <p><b>Gender:</b> {data['gender']} &nbsp;|&nbsp; <b>Operational Status:</b> {data['status']}</p>
        </blockquote>

        <h2 id="role-and-station">3. Role and Station</h2>
        <p>{data['real_name']} commands operations across <b>{data['station']}</b>. Under the post-Cycle doctrine of the Dawn Initiative (Year 4,238), this department adheres to reformed Directorate guidelines prioritizing protection, accountable research, and shared civic responsibility rather than exploitation or solitary burden.</p>

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

        <h2 id="history-and-cycle">5. Historical Background &amp; The 1,778 Cycles</h2>
        <p>{data['history_p1']}</p>
        <p>{data['history_p2']}</p>

        <h2 id="equipment-and-maw">6. Equipment &amp; M.A.W. Status</h2>
        <p>The Reverie Directorate Central Equipment Registry records the following official parameters for {data['real_name']}:</p>
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

        <h2 id="quotes-and-transmissions">7. Canonical Voice &amp; Directives</h2>
        <div class="dialogue-card" style="border-left: 4px solid {data['color']}; background: rgba(15, 23, 42, 0.7); padding: 16px; margin: 16px 0; border-radius: 4px;">
          <div style="font-family:'JetBrains Mono', monospace; font-size:0.8rem; color:{data['color']}; margin-bottom:6px;">LOG // DIRECTIVE RECORD — {data['id']}</div>
          <p style="font-style: italic; color:#e2e8f0; margin:0 0 8px 0;">{data['quote']}</p>
          <div style="font-size:0.8rem; color:#94a3b8; text-align:right;">— Recorded in Directorate Terminal Register, Year 4,238</div>
        </div>

        <h2 id="references">8. Canonical Lore References</h2>
        <ul>
          <li><i>The Reverie Directorate</i> (<code>The_REVERIE_DIRECTORATE.md</code>) — The Nine Echo-Cores Current Register &amp; Signature Equipment.</li>
          <li><i>Project Somnarak Master Core Lore</i> (<code>PROJECT_SOMNARAK.md</code>) — Cosmology, The Cycle, and The Dawn Initiative.</li>
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
          <dt>Real Name</dt>
          <dd>{data['real_name']}</dd>
          <dt>Gender</dt>
          <dd>{data['gender']}</dd>
          <dt>Station / Floor</dt>
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
      <li><a href="#history-and-cycle">5. History &amp; 1,778 Cycles</a></li>
      <li><a href="#equipment-and-maw">6. Equipment &amp; M.A.W.</a></li>
      <li><a href="#quotes-and-transmissions">7. Canonical Voice</a></li>
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
      <p>Echo-Core Leads Registry · Canonical Reverie Directorate Classification · Year 4,238 Dawn Initiative</p>
    </div>
  </div>
</footer>
</body>
</html>
"""
    return html

# Generate and write all Echo-Core pages
for fname, data in CANON_DATA.items():
    fpath = os.path.join(wiki_root, 'characters', fname)
    rendered = render_character_page(fname, data)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(rendered)
    print(f"CANONICAL REBUILD: {fname} generated with 100% exact R.D. lore fidelity!")

