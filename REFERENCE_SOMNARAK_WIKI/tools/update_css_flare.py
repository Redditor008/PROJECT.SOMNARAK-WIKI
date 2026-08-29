with open("/home/user/01_Somnarak_Wiki/assets/css/wiki.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace body background with high-flare Somnarak atmospheric background
old_body_bg = 'body{margin:0;background:#e8dc83;color:var(--ink);font:16px/1.55 var(--body);min-height:100vh}body:before{content:"";position:fixed;inset:0;z-index:-1;background:linear-gradient(145deg,#101910 0 12%,transparent 12% 76%,#182317 76%),linear-gradient(20deg,transparent 0 60%,#cfc566 60% 68%,transparent 68%)}'

new_body_bg = """
:root {
  --som-gold: #f1df76;
  --som-gold-glow: rgba(241, 223, 118, 0.35);
  --som-cyan: #38bdf8;
  --som-cyan-glow: rgba(56, 189, 248, 0.35);
  --som-crimson: #ef5b55;
  --som-crimson-dark: #8d2e42;
  --som-crimson-glow: rgba(239, 91, 85, 0.35);
  --som-black: #05070a;
  --som-gray-dark: #0e121a;
  --som-gray-mid: #1a2230;
  --som-white: #f8fafc;
  --som-pale: #cbd5e1;
}

body {
  margin: 0;
  background-color: #05070a;
  color: #f1f5f9;
  font: 16px/1.6 Arial, "Segoe UI", -apple-system, BlinkMacSystemFont, sans-serif;
  min-height: 100vh;
  position: relative;
}

body:before {
  content: "";
  position: fixed;
  inset: 0;
  z-index: -1;
  background: 
    /* Ambient Glows: Gold, Cyan, Crimson, Pale */
    radial-gradient(circle at 15% 20%, rgba(241, 223, 118, 0.12) 0%, transparent 40%),
    radial-gradient(circle at 85% 25%, rgba(56, 189, 248, 0.14) 0%, transparent 45%),
    radial-gradient(circle at 50% 75%, rgba(239, 91, 85, 0.12) 0%, transparent 50%),
    radial-gradient(circle at 80% 85%, rgba(203, 213, 225, 0.08) 0%, transparent 35%),
    /* Tech Circuit Grid & Hazard Cross-Hatch */
    linear-gradient(rgba(56, 189, 248, 0.04) 1px, transparent 1px),
    linear-gradient(90deg, rgba(241, 223, 118, 0.04) 1px, transparent 1px),
    linear-gradient(135deg, rgba(141, 46, 66, 0.08) 25%, transparent 25%, transparent 50%, rgba(141, 46, 66, 0.08) 50%, rgba(141, 46, 66, 0.08) 75%, transparent 75%, transparent),
    /* Deep Obsidian Bedrock */
    linear-gradient(180deg, #070a0f 0%, #030406 100%);
  background-size: 100% 100%, 100% 100%, 100% 100%, 100% 100%, 48px 48px, 48px 48px, 120px 120px, 100% 100%;
  pointer-events: none;
}

/* Subtle Glowing Tech Frame on Shell */
.wiki-shell {
  box-shadow: 0 0 35px rgba(56, 189, 248, 0.08), inset 0 0 1px rgba(241, 223, 118, 0.2);
  border: 1px solid #1e293b;
  background: rgba(8, 11, 16, 0.96);
  backdrop-filter: blur(8px);
}

.left-rail {
  background: linear-gradient(180deg, #06080d 0%, #0a0e17 100%);
  border-right: 1px solid #1e293b;
}

.left-links section {
  border: 1px solid #1e293b;
  background: rgba(14, 20, 30, 0.6);
  margin-bottom: 12px;
  box-shadow: inset 0 0 8px rgba(0,0,0,0.4);
}

.left-links h2 {
  color: #f1df76;
  border-bottom: 1px solid #334155;
  padding-bottom: 4px;
}

.floor-rail {
  background: linear-gradient(180deg, #090d14 0%, #040609 100%);
  border-left: 1px solid #1e293b;
}
"""

if "body{" in css:
    # Append or replace
    css = css.replace("body{margin:0;background:#e8dc83", "body{margin:0;background:#05070a")
    css += "\n" + new_body_bg

with open("/home/user/01_Somnarak_Wiki/assets/css/wiki.css", "w", encoding="utf-8") as f:
    f.write(css)

print("CSS updated with high-flare multi-layered atmospheric background!")
