import os, sys, re, html
sys.path.insert(0, '/home/user')
from tools.build_deep_canon_wiki import get_base_template
from tools.convert_echo_cores import echo_core_files, parse_markdown_to_wiki_sections, format_lines_to_html

SOURCE_DIR = "/home/user/salvaged_source_materials/FOR WIKI/00_Source_Materials/Character_Wiki"
OUTPUT_DIR = "/home/user/01_Somnarak_Wiki/characters"

def build_echo_core_page(src_file, dst_file, title, subtitle, core_num):
    src_path = os.path.join(SOURCE_DIR, src_file)
    with open(src_path, 'r', encoding='utf-8') as f:
        md_text = f.read()
        
    quote_text, quote_author, sections = parse_markdown_to_wiki_sections(md_text)
    
    content_parts = []
    toc_items = []
    
    if quote_text:
        content_parts.append(f'''
        <div class="wiki-quote">
          <p>“{quote_text}”</p>
          <div class="quote-author">— {quote_author or title}</div>
        </div>
        ''')

    for s_title, s_lines in sections:
        s_id = re.sub(r'[^a-zA-Z0-9]+', '-', s_title.lower()).strip('-')
        if not s_id:
            s_id = "section"
        
        if s_title != "Overview" or len(s_lines) > 2:
            toc_items.append((s_id, s_title))
            
        s_body_html = format_lines_to_html(s_lines)
        
        content_parts.append(f'''
        <section class="wiki-section" id="{s_id}">
          <h2 class="section-title">{s_title}</h2>
          {s_body_html}
        </section>
        ''')
        
    full_content = '\n'.join(content_parts)
    
    page_html = get_base_template(
        title=f"Echo-Core {core_num} — {title}",
        category_label="Characters",
        category_href="characters/index.html",
        rel_prefix="../",
        content_html=full_content,
        toc_items=toc_items
    )
    
    out_path = os.path.join(OUTPUT_DIR, dst_file)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(page_html)
    print(f"Generated: {dst_file} ({len(page_html)} chars, {len(sections)} sections)")

for src, (dst, title, subtitle, num) in echo_core_files.items():
    build_echo_core_page(src, dst, title, subtitle, num)

print("\nAll 9 Echo-Core character pages built directly from source dossiers.")
