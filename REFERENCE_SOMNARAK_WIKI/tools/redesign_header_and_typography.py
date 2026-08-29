import re

css_path = "/home/user/01_Somnarak_Wiki/assets/css/wiki.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Replace .utility CSS rules with a modern, bulletproof responsive utility bar
utility_replacement = """
/* ==========================================================================
   BULLETPROOF RESPONSIVE UTILITY HEADER BAR
   ========================================================================== */

.utility {
  min-height: 46px;
  height: auto;
  background: linear-gradient(180deg, #0d121d 0%, #070a10 100%);
  color: #e2e8f0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 6px 16px;
  position: sticky;
  top: 0;
  z-index: 100;
  border-bottom: 1px solid #1e293b;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.7);
  flex-wrap: wrap;
}

.utility-left {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-shrink: 0;
}

.utility-brand {
  font-family: var(--display, Impact, sans-serif);
  font-size: 1.15rem;
  font-weight: 900;
  color: #ef5b55;
  letter-spacing: 0.08em;
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 6px;
}

.utility-brand:hover {
  color: #f1df76;
}

.utility-era,
.utility > span {
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  color: #38bdf8;
  background: rgba(56, 189, 248, 0.12);
  border: 1px solid rgba(56, 189, 248, 0.35);
  padding: 3px 8px;
  border-radius: 3px;
  white-space: nowrap;
  display: inline-flex;
  align-items: center;
}

.utility nav {
  display: flex;
  align-items: center;
  gap: 2px;
  flex-wrap: wrap;
}

.utility nav a {
  display: inline-flex;
  align-items: center;
  padding: 5px 10px;
  font-size: 0.8rem;
  font-weight: 600;
  color: #cbd5e1;
  text-decoration: none;
  border-radius: 3px;
  transition: all 0.15s ease;
  white-space: nowrap;
}

.utility nav a:hover {
  color: #fff;
  background: rgba(241, 223, 118, 0.12);
}

.utility nav a.selected {
  color: #f1df76;
  background: rgba(241, 223, 118, 0.18);
  border-bottom: 2px solid #f1df76;
}

.utility-right {
  display: flex;
  align-items: center;
  gap: 10px;
}

.search {
  position: relative;
}

.search input {
  background: #0b0f17;
  border: 1px solid #334155;
  color: #f8fafc;
  width: clamp(140px, 16vw, 240px);
  padding: 6px 12px;
  font-size: 0.82rem;
  border-radius: 3px;
  transition: border-color 0.2s, width 0.2s;
}

.search input:focus {
  outline: none;
  border-color: #38bdf8;
  box-shadow: 0 0 8px rgba(56, 189, 248, 0.3);
}

.search #results {
  display: none;
  position: absolute;
  right: 0;
  top: 36px;
  width: min(380px, 90vw);
  background: #070a10;
  border: 1px solid #f1df76;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.9);
  border-radius: 3px;
  z-index: 110;
  max-height: 400px;
  overflow-y: auto;
}

.search #results.open {
  display: block;
}

.search #results a {
  display: block;
  padding: 10px 14px;
  border-bottom: 1px solid #1e293b;
  text-decoration: none;
  color: #e2e8f0;
}

.search #results a:hover {
  background: rgba(241, 223, 118, 0.1);
  color: #f1df76;
}

.search #results b {
  display: block;
  font-size: 0.9rem;
  color: #f1df76;
}

.search #results small {
  display: block;
  font-size: 0.75rem;
  color: #94a3b8;
  margin-top: 2px;
}

.nav-open {
  display: none;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid #334155;
  border-radius: 3px;
  color: #f1df76;
  font-size: 1.1rem;
  padding: 4px 10px;
  cursor: pointer;
}

@media (max-width: 960px) {
  .utility nav {
    display: none;
  }
  .nav-open {
    display: block;
  }
}

@media (max-width: 600px) {
  .utility {
    padding: 6px 10px;
  }
  .utility-era,
  .utility > span {
    display: none;
  }
  .search input {
    width: 130px;
  }
}
"""

# Let's clean up any previous .utility blocks and append the refined version
css = re.sub(r'\.utility\s*\{[^}]*\}', '', css)
css = re.sub(r'\.utility-brand\s*\{[^}]*\}', '', css)
css = re.sub(r'\.utility>span\s*\{[^}]*\}', '', css)
css = re.sub(r'\.utility\s+nav\s*\{[^}]*\}', '', css)
css = re.sub(r'\.utility\s+nav\s+a\s*\{[^}]*\}', '', css)
css = re.sub(r'\.utility\s+nav\s+a\.selected\s*\{[^}]*\}', '', css)

css = css + utility_replacement

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("wiki.css updated with responsive header.")
