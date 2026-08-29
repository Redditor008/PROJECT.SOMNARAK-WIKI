import os
import re

CHAR_DIR = "/home/user/01_Somnarak_Wiki/characters"
os.makedirs(CHAR_DIR, exist_ok=True)

def md_to_html(md_text):
    # Convert bold, italics, code
    text = md_text
    # Handle tables
    lines = text.split("\n")
    out_lines = []
    in_table = False
    table_rows = []
    
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            if not in_table:
                in_table = True
                table_rows = []
            table_rows.append(stripped)
        else:
            if in_table:
                in_table = False
                out_lines.append(render_table(table_rows))
            out_lines.append(line)
    if in_table:
        out_lines.append(render_table(table_rows))
    
    text = "\n".join(out_lines)
    
    # Process headers
    def replace_h(match):
        level = len(match.group(1))
        title = match.group(2).strip()
        slug = re.sub(r"[^a-zA-Z0-9]+", "-", title.lower()).strip("-")
        return f'<h{level} id="{slug}">{title}</h{level}>'
    
    text = re.sub(r'^(#{1,6})\s+(.+)$', replace_h, text, flags=re.M)
    
    # Process blockquotes
    text = re.sub(r'^>\s+(.+)$', r'<blockquote>\1</blockquote>', text, flags=re.M)
    # Combine consecutive blockquotes
    text = re.sub(r'</blockquote>\s*<blockquote>', '<br>', text)
    
    # Process bold/italics
    text = re.sub(r'\*\*\*([^*]+)\*\*\*', r'<strong><em>\1</em></strong>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', text)
    text = re.sub(r'_([^_]+)_', r'<em>\1</em>', text)
    
    # Process lists
    text = re.sub(r'^\s*-\s+(.+)$', r'<li>\1</li>', text, flags=re.M)
    text = re.sub(r'((?:<li>.+</li>\s*)+)', r'<ul>\1</ul>', text)
    
    # Process paragraphs
    paragraphs = []
    for block in text.split("\n\n"):
        block = block.strip()
        if not block:
            continue
        if block.startswith("<h") or block.startswith("<blockquote") or block.startswith("<div") or block.startswith("<ul") or block.startswith("<table"):
            paragraphs.append(block)
        else:
            paragraphs.append(f"<p>{block}</p>")
            
    return "\n".join(paragraphs)

def render_table(rows):
    if len(rows) < 2:
        return ""
    header_cols = [c.strip() for c in rows[0].strip("|").split("|")]
    has_separator = len(rows) > 1 and "---" in rows[1]
    data_rows = rows[2:] if has_separator else rows[1:]
    
    html = ['<div class="table-wrap"><table class="data-table"><thead><tr>']
    for hc in header_cols:
        html.append(f'<th>{hc}</th>')
    html.append('</tr></thead><tbody>')
    
    for r in data_rows:
        cols = [c.strip() for c in r.strip("|").split("|")]
        html.append('<tr>')
        for c in cols:
            html.append(f'<td>{c}</td>')
        html.append('</tr>')
    html.append('</tbody></table></div>')
    return "\n".join(html)

def build_toc(html_content):
    headers = re.findall(r'<h([23]) id="([^"]+)">([^<]+)</h[23]>', html_content)
    toc_items = []
    for level, slug, title in headers:
        toc_items.append(f'<li class="l{level}"><a href="#{slug}">{title}</a></li>')
    return "\n".join(toc_items)

print("Parser functions initialized.")
