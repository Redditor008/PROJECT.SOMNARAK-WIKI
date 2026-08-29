import os
import glob
import re

WIKI_ROOT = "/home/user/01_Somnarak_Wiki"
html_files = sorted(glob.glob(os.path.join(WIKI_ROOT, "**", "*.html"), recursive=True))

print(f"Auditing links and resources across {len(html_files)} HTML files...")

broken_links = []
broken_images = []
broken_resources = []

for fpath in html_files:
    rel_path = os.path.relpath(fpath, WIKI_ROOT)
    dir_path = os.path.dirname(fpath)
    
    with open(fpath, "r", encoding="utf-8") as fp:
        html = fp.read()
        
    # Check <a> links
    for m in re.finditer(r'<a[^>]+href=["\']([^"\']+)["\']', html):
        href = m.group(1)
        if href.startswith("#") or href.startswith("http://") or href.startswith("https://") or href.startswith("mailto:"):
            continue
        # Strip anchor
        target_file = href.split("#")[0]
        if not target_file:
            continue
        resolved = os.path.normpath(os.path.join(dir_path, target_file))
        if not os.path.exists(resolved):
            broken_links.append((rel_path, href, resolved))
            
    # Check <img> sources
    for m in re.finditer(r'<img[^>]+src=["\']([^"\']+)["\']', html):
        src = m.group(1)
        if src.startswith("data:") or src.startswith("http://") or src.startswith("https://"):
            continue
        resolved = os.path.normpath(os.path.join(dir_path, src))
        if not os.path.exists(resolved):
            broken_images.append((rel_path, src, resolved))
            
    # Check <link> and <script>
    for m in re.finditer(r'<(?:link[^>]+href|script[^>]+src)=["\']([^"\']+)["\']', html):
        res = m.group(1)
        if res.startswith("data:") or res.startswith("http://") or res.startswith("https://"):
            continue
        resolved = os.path.normpath(os.path.join(dir_path, res))
        if not os.path.exists(resolved):
            broken_resources.append((rel_path, res, resolved))

print(f"Total broken links: {len(broken_links)}")
for r, h, res in broken_links[:10]:
    print(f"  [Link] In {r}: {h} -> {res}")
    
print(f"Total broken images: {len(broken_images)}")
for r, s, res in broken_images[:10]:
    print(f"  [Img] In {r}: {src} -> {res}")
    
print(f"Total broken resources: {len(broken_resources)}")
for r, res, path in broken_resources[:10]:
    print(f"  [Res] In {r}: {res} -> {path}")

if not broken_links and not broken_images and not broken_resources:
    print("PERFECT: 100% OF ALL INTERNAL LINKS, IMAGES, AND RESOURCES RESOLVE TO VALID LOCAL FILES!")
