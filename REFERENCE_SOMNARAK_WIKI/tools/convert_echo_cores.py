import os, sys, re, html

SOURCE_DIR = "/home/user/salvaged_source_materials/FOR WIKI/00_Source_Materials/Character_Wiki"
OUTPUT_DIR = "/home/user/01_Somnarak_Wiki/characters"

echo_core_files = {
    "THE_DIRECTOR.md": ("the-director-majin.html", "Director Majin", "Echo-Core 1 · Supreme Directorate Authority", "1"),
    "THE_SECRETARY.md": ("the-secretary-seiyon.html", "Seiyon", "Echo-Core 2 · Central Archives & Memory Index", "2"),
    "THE_CONTAINMENT_LEAD.md": ("the-containment-lead-dekan.html", "Dekan", "Echo-Core 3 · Sorrow Containment & Ward Warden", "3"),
    "THE_EXTRACTION_LEAD.md": ("the-extraction-lead-zyrak.html", "Zyrak", "Echo-Core 4 · M.A.W. Siphoning & Forge Master", "4"),
    "THE_RESEARCH_LEAD.md": ("the-research-lead-ayshuk.html", "Ayshuk", "Echo-Core 5 · Han Kinetics & Anomaly Analysis", "5"),
    "THE_BORDER_LEAD.md": ("the-border-lead-mellda.html", "Mellda", "Echo-Core 6 · Outer Bulwark & Acoustic Bastion", "6"),
    "THE_ARCHIVE_LEAD.md": ("the-archive-lead-marjuk.html", "Marjuk", "Echo-Core 7 · Deep Vault & Precursor Records", "7"),
    "THE_OUTSIDER.md": ("the-outsider-ishall.html", "Ishall", "Echo-Core 8 · Desolate Reconnaissance & Void Diver", "8"),
    "THE_EXILE.md": ("the-exile-xyan.html", "Xyan", "Echo-Core 9 · The Forbidden Gate & Taboo Resonance", "9"),
}

def parse_markdown_to_wiki_sections(md_text):
    lines = md_text.splitlines()
    quote_text = ""
    quote_author = ""
    
    i = 0
    while i < min(30, len(lines)):
        line = lines[i].strip()
        if line.startswith('> _“') or line.startswith('> "') or line.startswith('> _"') or line.startswith('> _“'):
            quote_text = line.replace('> ', '').strip('_"“')
            if i + 1 < len(lines) and lines[i+1].strip().startswith('> —'):
                quote_author = lines[i+1].strip().replace('> —', '').replace('**', '').strip()
                i += 1
        i += 1
        
    sections = []
    current_title = "Overview"
    current_lines = []
    
    in_toc = False
    for line in lines:
        sline = line.strip()
        if sline.startswith('## Contents'):
            in_toc = True
            continue
        if in_toc:
            if sline.startswith('## '):
                in_toc = False
            else:
                continue
                
        if sline.startswith('## '):
            if current_lines:
                sections.append((current_title, current_lines))
            current_title = sline.replace('## ', '').strip()
            current_title = re.sub(r'\[.*?\]', '', current_title).strip()
            # remove anchor jump links if present
            current_title = re.sub(r'\(#.*?\)', '', current_title).strip()
            current_lines = []
        else:
            current_lines.append(line)
            
    if current_lines:
        sections.append((current_title, current_lines))
        
    return quote_text, quote_author, sections

def format_inline_markdown(text):
    # bold italics
    text = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    # bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    # italics
    text = re.sub(r'(?<!\w)_(.*?)_(?!\w)', r'<em>\1</em>', text)
    text = re.sub(r'(?<!\w)\*(.*?)\*(?!\w)', r'<em>\1</em>', text)
    # inline code
    text = re.sub(r'`(.*?)`', r'<code>\1</code>', text)
    # markdown links [text](url)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" class="wiki-link">\1</a>', text)
    return text

def format_lines_to_html(lines):
    out = []
    in_table = False
    table_rows = []
    
    in_ul = False
    in_ol = False
    in_quote = False
    quote_buf = []
    
    def flush_table():
        nonlocal in_table, table_rows
        if not table_rows:
            return ""
        header = table_rows[0]
        start_idx = 1
        if len(table_rows) > 1 and re.match(r'^\|?[\s\-:|]+\|?$', table_rows[1].strip()):
            start_idx = 2
            
        th_cols = [format_inline_markdown(c.strip()) for c in header.strip('|').split('|')]
        html_t = ['<div class="table-wrap"><table class="wiki-table">']
        html_t.append('<thead><tr>' + ''.join([f'<th>{c}</th>' for c in th_cols]) + '</tr></thead>')
        html_t.append('<tbody>')
        for r in table_rows[start_idx:]:
            if not r.strip(): continue
            td_cols = [format_inline_markdown(c.strip()) for c in r.strip('|').split('|')]
            while len(td_cols) < len(th_cols): td_cols.append('')
            td_cols = td_cols[:len(th_cols)]
            html_t.append('<tr>' + ''.join([f'<td>{c}</td>' for c in td_cols]) + '</tr>')
        html_t.append('</tbody></table></div>')
        table_rows = []
        in_table = False
        return '\n'.join(html_t)
        
    def flush_quote():
        nonlocal in_quote, quote_buf
        if not quote_buf:
            return ""
        q_text = format_inline_markdown(" ".join(quote_buf))
        q_html = f'<div class="wiki-callout"><p>{q_text}</p></div>'
        quote_buf = []
        in_quote = False
        return q_html

    for line in lines:
        sline = line.strip()
        
        # Table detection
        if sline.startswith('|') and sline.endswith('|'):
            if in_quote: out.append(flush_quote())
            if in_ul: out.append('</ul>'); in_ul = False
            if in_ol: out.append('</ol>'); in_ol = False
            in_table = True
            table_rows.append(sline)
            continue
        elif in_table:
            out.append(flush_table())
            
        # Blockquote detection
        if sline.startswith('>'):
            if in_ul: out.append('</ul>'); in_ul = False
            if in_ol: out.append('</ol>'); in_ol = False
            in_quote = True
            quote_buf.append(sline.lstrip('>').strip())
            continue
        elif in_quote:
            out.append(flush_quote())
            
        # Headers inside section (### or ####)
        if sline.startswith('### '):
            if in_ul: out.append('</ul>'); in_ul = False
            if in_ol: out.append('</ol>'); in_ol = False
            h_text = format_inline_markdown(sline.replace('### ', '').strip())
            # remove anchor links
            h_text = re.sub(r'\[#.*?\]', '', h_text).strip()
            out.append(f'<h3>{h_text}</h3>')
            continue
        if sline.startswith('#### '):
            if in_ul: out.append('</ul>'); in_ul = False
            if in_ol: out.append('</ol>'); in_ol = False
            h_text = format_inline_markdown(sline.replace('#### ', '').strip())
            out.append(f'<h4>{h_text}</h4>')
            continue
            
        # Lists
        if sline.startswith('- ') or sline.startswith('* '):
            if not in_ul:
                if in_ol: out.append('</ol>'); in_ol = False
                out.append('<ul>')
                in_ul = True
            item_text = format_inline_markdown(sline[2:].strip())
            out.append(f'<li>{item_text}</li>')
            continue
        elif in_ul and not sline.startswith('- ') and not sline.startswith('* '):
            out.append('</ul>')
            in_ul = False
            
        if re.match(r'^\d+\.\s', sline):
            if not in_ol:
                if in_ul: out.append('</ul>'); in_ul = False
                out.append('<ol>')
                in_ol = True
            item_text = format_inline_markdown(re.sub(r'^\d+\.\s', '', sline).strip())
            out.append(f'<li>{item_text}</li>')
            continue
        elif in_ol and not re.match(r'^\d+\.\s', sline):
            out.append('</ol>')
            in_ol = False
            
        if not sline:
            continue
            
        if sline.startswith('---'):
            continue
            
        # Paragraph text
        out.append(f'<p>{format_inline_markdown(sline)}</p>')
        
    if in_table: out.append(flush_table())
    if in_quote: out.append(flush_quote())
    if in_ul: out.append('</ul>')
    if in_ol: out.append('</ol>')
    
    return '\n'.join(out)

print("Echo core converter updated.")
