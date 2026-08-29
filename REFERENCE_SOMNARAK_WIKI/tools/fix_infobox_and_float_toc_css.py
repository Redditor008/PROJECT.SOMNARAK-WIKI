import os, re, glob
from bs4 import BeautifulSoup

wiki_root = '/home/user/01_Somnarak_Wiki'

# 1. UPDATE wiki.css TO PERFECTLY FIX:
# - Left-side floating TOC (.float-toc)
# - 2-column article grid (.entity-article, .character-article)
# - Zero text overflow (word-break, max-width, box-sizing)
# - Side infobox table styling (.entity-infobox, .character-infobox)

css_fixes = """
/* =========================================================================
   COMPREHENSIVE LAYOUT & SIDE-TABLE FIXES
   ========================================================================= */

/* Fix 2-Column Article Grid (Main Content Left + Side Table Right) */
.entity-article,
.character-article,
.wiki-article-grid {
  display: grid !important;
  grid-template-columns: minmax(0, 1fr) 340px !important;
  gap: 32px !important;
  align-items: start !important;
  width: 100% !important;
  max-width: 100% !important;
  box-sizing: border-box !important;
  margin-bottom: 2.5rem !important;
}

@media (max-width: 1080px) {
  .entity-article,
  .character-article,
  .wiki-article-grid {
    grid-template-columns: 1fr !important;
  }
}

/* Ensure ALL text containers stay inside boxes without overflow */
.entity-main-content,
.character-main-content,
.article-body,
.article-text,
.story-panel,
.set-resonance,
.tactical-directive-box,
.fast-jump-nav,
.page-tabs,
.breadcrumbs,
.article-header {
  min-width: 0 !important;
  max-width: 100% !important;
  box-sizing: border-box !important;
  overflow-wrap: break-word !important;
  word-break: break-word !important;
}

/* Side Table Infobox (Entity & Character Infobox) */
.entity-infobox,
.character-infobox,
.item-infobox {
  width: 100% !important;
  max-width: 340px !important;
  box-sizing: border-box !important;
  background: #080d16 !important;
  border: 2px solid var(--entity, #f1df76) !important;
  border-radius: 6px !important;
  position: sticky !important;
  top: 70px !important;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.85) !important;
  overflow: hidden !important;
  margin: 0 !important;
}

.entity-infobox > h2,
.character-infobox > h2,
.item-infobox > h2 {
  margin: 0 !important;
  padding: 12px 16px !important;
  background: var(--entity, #f1df76) !important;
  color: #000000 !important;
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 1.3rem !important;
  letter-spacing: 0.08em !important;
  text-align: center !important;
  text-shadow: none !important;
  border-bottom: 2px solid rgba(0, 0, 0, 0.4) !important;
}

.entity-infobox > h3,
.character-infobox > h3,
.item-infobox > h3 {
  margin: 0 !important;
  padding: 8px 12px !important;
  background: #0d1726 !important;
  color: var(--entity, #f1df76) !important;
  font-family: 'JetBrains Mono', monospace !important;
  font-size: 0.85rem !important;
  letter-spacing: 0.06em !important;
  border-top: 1px solid #1e293b !important;
  border-bottom: 1px solid #1e293b !important;
  text-transform: uppercase !important;
}

.infobox-image-wrap {
  background: #040710 !important;
  padding: 16px !important;
  text-align: center !important;
  border-bottom: 1px solid #1e293b !important;
}

.infobox-image-wrap img {
  max-width: 180px !important;
  max-height: 180px !important;
  width: auto !important;
  height: auto !important;
  display: inline-block !important;
  border-radius: 6px !important;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.6) !important;
}

.fact-grid {
  display: grid !important;
  grid-template-columns: 42% 58% !important;
  margin: 0 !important;
  font-size: 0.8rem !important;
  font-family: 'JetBrains Mono', monospace !important;
}

.fact-grid dt {
  background: #090e18 !important;
  color: #94a3b8 !important;
  padding: 7px 10px !important;
  border-bottom: 1px solid #172336 !important;
  border-right: 1px solid #172336 !important;
  font-weight: normal !important;
}

.fact-grid dd {
  background: #060a12 !important;
  color: #e2e8f0 !important;
  padding: 7px 10px !important;
  margin: 0 !important;
  border-bottom: 1px solid #172336 !important;
  font-weight: 500 !important;
}

/* Infobox Stat Table */
.infobox-stat-table {
  width: 100% !important;
  border-collapse: collapse !important;
  margin: 0 !important;
  font-family: 'JetBrains Mono', monospace !important;
  font-size: 0.78rem !important;
}

.infobox-stat-table th {
  background: #0b1322 !important;
  color: #38bdf8 !important;
  padding: 6px 8px !important;
  border-bottom: 1px solid #1e293b !important;
  border-right: 1px solid #1e293b !important;
  text-align: left !important;
  font-size: 0.75rem !important;
}

.infobox-stat-table td {
  background: #060912 !important;
  color: #f8fafc !important;
  padding: 6px 8px !important;
  border-bottom: 1px solid #1e293b !important;
  font-size: 0.78rem !important;
}

/* =========================================================================
   LEFT-SIDE FLOATING TABLE OF CONTENTS (.float-toc)
   ========================================================================= */
.float-toc {
  position: fixed !important;
  left: 0 !important;
  top: 140px !important;
  z-index: 999 !important;
  display: flex !important;
  align-items: flex-start !important;
}

/* Vertical Tab Button */
.float-toc-trigger,
.float-toc > button {
  writing-mode: vertical-rl !important;
  transform: rotate(180deg) !important;
  background: #080e1a !important;
  border: 1.5px solid #f1df76 !important;
  border-left: none !important;
  color: #f1df76 !important;
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 0.78rem !important;
  letter-spacing: 0.12em !important;
  padding: 14px 7px !important;
  cursor: pointer !important;
  border-radius: 0 6px 6px 0 !important;
  box-shadow: 4px 4px 18px rgba(0, 0, 0, 0.85), 0 0 10px rgba(241, 223, 118, 0.25) !important;
  transition: all 0.2s ease !important;
  user-select: none !important;
}

.float-toc-trigger:hover,
.float-toc > button:hover {
  background: #121e33 !important;
  color: #ffffff !important;
  box-shadow: 6px 6px 22px rgba(0, 0, 0, 0.95), 0 0 14px rgba(56, 189, 248, 0.5) !important;
}

/* Floating Drawer Panel */
.float-toc-panel,
.float-toc > div {
  display: none !important;
  width: 320px !important;
  max-width: 85vw !important;
  max-height: 75vh !important;
  overflow-y: auto !important;
  background: #060912 !important;
  border: 2px solid #38bdf8 !important;
  border-left: 4px solid #f1df76 !important;
  border-radius: 0 8px 8px 0 !important;
  padding: 14px 16px !important;
  box-shadow: 8px 12px 35px rgba(0, 0, 0, 0.95) !important;
  box-sizing: border-box !important;
}

.float-toc.open .float-toc-panel,
.float-toc.open > div {
  display: block !important;
  animation: floatTocSlideRight 0.18s ease-out !important;
}

@keyframes floatTocSlideRight {
  from { opacity: 0; transform: translateX(-15px); }
  to { opacity: 1; transform: translateX(0); }
}

.float-toc strong,
.float-toc-header {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  color: #f1df76 !important;
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 0.9rem !important;
  letter-spacing: 0.08em !important;
  border-bottom: 1px solid #1e293b !important;
  padding-bottom: 8px !important;
  margin-bottom: 10px !important;
}

.float-toc ol,
.float-toc ul,
.float-toc-list {
  list-style: none !important;
  padding: 0 !important;
  margin: 0 !important;
}

.float-toc li {
  margin-bottom: 4px !important;
}

.float-toc li a {
  display: block !important;
  color: #94a3b8 !important;
  font-size: 0.8rem !important;
  font-family: 'Inter', -apple-system, sans-serif !important;
  padding: 5px 8px !important;
  border-radius: 3px !important;
  text-decoration: none !important;
  border-left: 2px solid transparent !important;
  transition: all 0.15s ease !important;
}

.float-toc li a:hover {
  color: #ffffff !important;
  background: rgba(56, 189, 248, 0.12) !important;
  border-left-color: #38bdf8 !important;
  padding-left: 12px !important;
}

.float-toc li.l3 a,
.float-toc-sub a {
  padding-left: 16px !important;
  font-size: 0.75rem !important;
  color: #64748b !important;
}

.float-toc li a.active-toc-item {
  color: #f1df76 !important;
  background: rgba(241, 223, 118, 0.15) !important;
  border-left-color: #f1df76 !important;
  font-weight: bold !important;
}
"""

with open(f'{wiki_root}/assets/css/wiki.css', 'a', encoding='utf-8') as f:
    f.write(css_fixes)

print("SUCCESS: Appended responsive side-table and floating left TOC fixes to wiki.css!")
