import os, sys, re, html
sys.path.insert(0, '/home/user')
from tools.build_deep_canon_wiki import get_base_template
from tools.convert_echo_cores import parse_markdown_to_wiki_sections, format_lines_to_html

SOURCE_DIR = "/home/user/salvaged_source_materials/FOR WIKI/00_Source_Materials/World_Reference"
WIKI_DIR = "/home/user/01_Somnarak_Wiki"

# Mapping of source markdown files to wiki destination pages
file_mappings = [
    # Lore
    ("SOMNARAK_CHEONGULA.md", "lore/the-cheongula-incident.html", "The Cheongula Incident (Year 3,892)", "Lore & World", "lore/index.html"),
    ("SOMNARAK_DAWN_OF_HOPE.md", "lore/the-dawn-of-hope.html", "The Dawn of Hope & Reconstruction", "Lore & World", "lore/index.html"),
    ("SOMNARAK_DAILY_LIFE.md", "lore/daily-life-in-somnarak.html", "Daily Life & Society in Somnarak", "Lore & World", "lore/index.html"),
    ("SOMNARAK_NAMED_FRACTURES.md", "lore/named-fractures.html", "The Eight Named Fractures", "Lore & World", "lore/index.html"),
    ("SOMNARAK_NAME_REGISTRY.md", "lore/somnarak-name-registry.html", "The Somnarak Name Registry & Cryo-Archive", "Lore & World", "lore/index.html"),
    ("SOMNARAK_THE_DOORSPEECH.md", "lore/the-doorspeech.html", "The Doorspeech (Mun-eon) & Acoustic Mantles", "Lore & World", "lore/index.html"),
    ("SOMNARAK_THE_WEEPING.md", "lore/the-weeping-river.html", "The Weeping River & Abyssal Hydrology", "Lore & World", "lore/index.html"),
    ("SOMNARAK_DREAM_REALM.md", "lore/the-dream-realm.html", "The Dream Realm (Yumonggye) & Subconscious Ocean", "Lore & World", "lore/index.html"),
    
    # Mechanics
    ("SOMNARAK_BATTLE_SYSTEM.md", "mechanics/resonant-clash-mechanics.html", "Resonant Clash & Combat Mechanics", "Systems & Mechanics", "mechanics/index.html"),
    ("SOMNARAK_ENEMY_LIST.md", "mechanics/enemy-bestiary.html", "Enemy Bestiary & Hostile Entity Register", "Systems & Mechanics", "mechanics/index.html"),
    ("SOMNARAK_HAN_RELICS.md", "mechanics/han-relic-registry.html", "Han Relic Registry (Grades I–V)", "Systems & Mechanics", "mechanics/index.html"),
    ("SOMNARAK_TABOO_RESONANCE.md", "mechanics/taboo-resonance-mechanics.html", "Taboo Resonance & Soul Calcification", "Systems & Mechanics", "mechanics/index.html"),
    ("SOMNARAK_ORDEALS_FRAMEWORK.md", "mechanics/ordeals-framework.html", "Ordeals Framework & Incursion Waves", "Systems & Mechanics", "mechanics/index.html"),
    
    # Factions
    ("SOMNARAK_CORPORATIONS.md", "factions/the-founding-corporations.html", "The Founding Precursor Corporations", "Factions & Guilds", "factions/index.html"),
    ("SOMNARAK_FACTION_TECH.md", "factions/faction-technology.html", "Comparative Faction Technology & Engineering", "Factions & Guilds", "factions/index.html"),
    ("SOMNARAK_FACTION_RELATIONS.md", "factions/index.html", "Factions & Guilds Directory", "Factions & Guilds", "factions/index.html"),
    ("SOMNARAK_HORIZON_CARAVAN.md", "factions/the-horizon-caravan.html", "The Horizon Caravan Guild", "Factions & Guilds", "factions/index.html"),
    ("SOMNARAK_WOUND_WALKERS.md", "factions/the-underworld-and-wound-walkers.html", "The Underworld & Wound Walkers", "Factions & Guilds", "factions/index.html"),
    
    # Locations
    ("SOMNARAK_THE_DESOLATE.md", "locations/the-desolate.html", "The Desolate (Hwangmuji)", "Locations & Atlas", "locations/index.html"),
    ("SOMNARAK_UNKNOWN_CITIES.md", "locations/unknown-cities.html", "Unknown Cities & Precursor Ruins", "Locations & Atlas", "locations/index.html"),
]

for src_name, dst_rel, title, cat_label, cat_href in file_mappings:
    src_path = os.path.join(SOURCE_DIR, src_name)
    if not os.path.exists(src_path):
        print(f"Warning: {src_path} does not exist.")
        continue
        
    with open(src_path, 'r', encoding='utf-8') as f:
        md_text = f.read()
        
    quote_text, quote_author, sections = parse_markdown_to_wiki_sections(md_text)
    
    toc_items = []
    content_parts = []
    
    if quote_text:
        content_parts.append(f'''
        <div class="wiki-quote">
          <p>“{quote_text}”</p>
          <div class="quote-author">— {quote_author or title}</div>
        </div>
        ''')

    for s_title, s_lines in sections:
        sid = re.sub(r'[^a-zA-Z0-9]+', '-', s_title.lower()).strip('-') or 'sec'
        if s_title != "Overview" or len(s_lines) > 2:
            toc_items.append((sid, s_title))
            
        s_body_html = format_lines_to_html(s_lines)
        content_parts.append(f'''
        <section class="wiki-section" id="{sid}">
          <h2 class="section-title">{s_title}</h2>
          {s_body_html}
        </section>
        ''')
        
    full_content = '\n'.join(content_parts)
    page_html = get_base_template(
        title=title,
        category_label=cat_label,
        category_href=cat_href,
        rel_prefix="../",
        content_html=full_content,
        toc_items=toc_items
    )
    
    dst_path = os.path.join(WIKI_DIR, dst_rel)
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(page_html)
    print(f"Built deep canon page: {dst_rel} ({len(page_html)} chars, {len(sections)} sections)")

print("\nDeep canon conversion completed for lore, mechanics, factions, and locations.")
