import re

css_path = "/home/user/01_Somnarak_Wiki/assets/css/wiki.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Let's craft the supreme stylized Project Moon / wiki.gg styling engine
stylized_rules = """

/* ==========================================================================
   PERFECT 100% - 130% ZOOM RESPONSIVENESS & PROJECT MOON STYLIZATION ENGINE
   ========================================================================== */

/* Universal text sizing and layout adaptation for 100% to 130%+ zoom */
:root {
  --font-base: clamp(14px, 0.95vw, 16px);
  --fluid-h1: clamp(1.6rem, 2.6vw, 2.5rem);
  --fluid-h2: clamp(1.25rem, 1.8vw, 1.65rem);
  --fluid-h3: clamp(1.05rem, 1.3vw, 1.25rem);
  --fluid-body: clamp(0.92rem, 1.05vw, 1.05rem);
}

html {
  font-size: var(--font-base);
  -webkit-text-size-adjust: 100%;
  text-size-adjust: 100%;
}

body {
  font-family: Arial, "Segoe UI", -apple-system, sans-serif;
  font-size: var(--fluid-body);
  line-height: 1.7;
  color: #e2e8f0;
  background: #040609;
}

/* ==========================================================================
   130% ZOOM SAFE TOP UTILITY HEADER
   ========================================================================== */
.utility {
  min-height: 44px !important;
  height: auto !important;
  background: linear-gradient(180deg, #0d121c 0%, #06080d 100%) !important;
  color: #e2e8f0 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  gap: 8px !important;
  padding: 4px clamp(8px, 1.5vw, 16px) !important;
  position: sticky !important;
  top: 0 !important;
  z-index: 100 !important;
  border-bottom: 1px solid #1e293b !important;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.8) !important;
  flex-wrap: wrap !important;
}

.utility-left {
  display: flex !important;
  align-items: center !important;
  gap: 8px !important;
  flex-shrink: 0 !important;
}

.utility-brand {
  font-family: Impact, "Arial Black", sans-serif !important;
  font-size: clamp(1rem, 1.2vw, 1.15rem) !important;
  font-weight: 900 !important;
  color: #ef5b55 !important;
  letter-spacing: 0.08em !important;
  text-decoration: none !important;
  white-space: nowrap !important;
}

.utility-brand:hover {
  color: #f1df76 !important;
}

.utility-era {
  font-size: 0.68rem !important;
  font-weight: 800 !important;
  letter-spacing: 0.08em !important;
  color: #38bdf8 !important;
  background: rgba(56, 189, 248, 0.12) !important;
  border: 1px solid rgba(56, 189, 248, 0.35) !important;
  padding: 2px 7px !important;
  border-radius: 3px !important;
  white-space: nowrap !important;
  text-transform: uppercase !important;
}

.utility nav {
  display: flex !important;
  align-items: center !important;
  gap: 2px !important;
  flex-wrap: wrap !important;
  margin: 0 4px !important;
}

.utility nav a {
  display: inline-flex !important;
  align-items: center !important;
  padding: 4px clamp(5px, 0.7vw, 9px) !important;
  font-size: clamp(0.72rem, 0.82vw, 0.82rem) !important;
  font-weight: 600 !important;
  color: #cbd5e1 !important;
  text-decoration: none !important;
  border-radius: 3px !important;
  white-space: nowrap !important;
  transition: all 0.15s ease !important;
}

.utility nav a:hover {
  color: #fff !important;
  background: rgba(241, 223, 118, 0.15) !important;
}

.utility nav a.selected {
  color: #f1df76 !important;
  background: rgba(241, 223, 118, 0.2) !important;
  border-bottom: 2px solid #f1df76 !important;
}

.search input {
  background: #090d14 !important;
  border: 1px solid #334155 !important;
  color: #f8fafc !important;
  width: clamp(120px, 12vw, 180px) !important;
  padding: 4px 8px !important;
  font-size: 0.78rem !important;
  border-radius: 3px !important;
}

/* At 130% zoom on narrower screens, collapse nav into hamburger if needed */
@media (max-width: 1080px) {
  .utility nav a {
    padding: 3px 6px !important;
    font-size: 0.72rem !important;
  }
}

@media (max-width: 900px) {
  .utility nav {
    display: none !important;
  }
  .nav-open {
    display: block !important;
  }
}

/* ==========================================================================
   WIKI-SHELL & CONTENT SIZING FOR 100% - 130% ZOOM
   ========================================================================== */
.wiki-shell {
  width: min(1640px, 98vw) !important;
  margin: 0.8rem auto 2.5rem !important;
  display: grid !important;
  grid-template-columns: minmax(190px, 220px) minmax(0, 1fr) !important;
  gap: 0 !important;
  background: rgba(6, 8, 12, 0.98) !important;
  border: 1px solid #221518 !important;
  box-shadow: 0 0 35px rgba(0, 0, 0, 0.9) !important;
}

.wiki-shell.home-shell {
  grid-template-columns: minmax(190px, 210px) minmax(0, 1fr) minmax(240px, 280px) !important;
}

#content {
  padding: 1.2rem clamp(1rem, 2.5vw, 2.5rem) 3rem !important;
  min-width: 0 !important;
  width: 100% !important;
  overflow-x: hidden !important;
}

/* ==========================================================================
   DEEPLY STYLIZED PROJECT MOON TYPOGRAPHY & CALLOUT BOXES
   ========================================================================== */

/* Page Tabs Header */
.page-tabs {
  height: 38px !important;
  display: flex !important;
  align-items: center !important;
  border-bottom: 2px solid #33161a !important;
  margin-bottom: 1.2rem !important;
}

.page-tabs span {
  padding: 6px 14px 4px !important;
  background: rgba(239, 91, 85, 0.12) !important;
  border: 1px solid #33161a !important;
  border-bottom: 0 !important;
  color: #ef5b55 !important;
  font-size: 0.75rem !important;
  font-weight: 700 !important;
  letter-spacing: 0.1em !important;
  text-transform: uppercase !important;
}

.page-tabs b {
  margin-left: auto !important;
  color: #71efaf !important;
  font-family: Impact, "Arial Black", sans-serif !important;
  font-size: 0.85rem !important;
  letter-spacing: 0.12em !important;
  padding: 4px 10px !important;
  background: rgba(113, 239, 175, 0.08) !important;
  border: 1px solid rgba(113, 239, 175, 0.25) !important;
}

/* Breadcrumbs */
.breadcrumbs {
  font-size: 0.8rem !important;
  color: #94a3b8 !important;
  margin: 0 0 1rem !important;
  display: flex !important;
  align-items: center !important;
  flex-wrap: wrap !important;
  gap: 4px !important;
}

.breadcrumbs a {
  color: #38bdf8 !important;
  font-weight: 500 !important;
}

.breadcrumbs a:hover {
  color: #f1df76 !important;
  text-decoration: underline !important;
}

.breadcrumbs i {
  color: #64748b !important;
  font-style: normal !important;
  margin: 0 2px !important;
}

/* Styled Section Headings with Terminal Accents */
.article-body h2 {
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: var(--fluid-h2) !important;
  color: #f1df76 !important;
  letter-spacing: 0.06em !important;
  text-transform: uppercase !important;
  border-bottom: 2px solid rgba(241, 223, 118, 0.3) !important;
  padding-bottom: 0.4rem !important;
  margin: 2.2rem 0 0.9rem !important;
  position: relative !important;
  display: flex !important;
  align-items: center !important;
}

.article-body h2:before {
  content: "■ " !important;
  color: #ef5b55 !important;
  font-size: 0.75em !important;
  margin-right: 0.4em !important;
}

.article-body h3 {
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: var(--fluid-h3) !important;
  color: #38bdf8 !important;
  letter-spacing: 0.05em !important;
  margin: 1.6rem 0 0.5rem !important;
  display: flex !important;
  align-items: center !important;
}

.article-body h3:before {
  content: "› " !important;
  color: #f1df76 !important;
  font-weight: bold !important;
  margin-right: 0.3em !important;
}

/* High-Impact Lore Quotes */
.article-body blockquote {
  border-left: 4px solid #f1df76 !important;
  border-right: 1px solid rgba(241, 223, 118, 0.2) !important;
  background: radial-gradient(circle at 0% 50%, rgba(241, 223, 118, 0.08) 0%, rgba(10, 14, 22, 0.85) 100%) !important;
  padding: 1.1rem 1.4rem !important;
  margin: 1.4rem 0 !important;
  font-style: italic !important;
  color: #f8fafc !important;
  border-radius: 0 4px 4px 0 !important;
  box-shadow: inset 0 0 15px rgba(0, 0, 0, 0.6) !important;
}

.article-body blockquote i {
  color: #f1df76 !important;
  font-style: normal !important;
}

/* Styled Terminal Callout Boxes */
.terminal-callout {
  border: 1px solid #334155 !important;
  border-left: 5px solid #38bdf8 !important;
  background: linear-gradient(135deg, rgba(8, 14, 24, 0.95) 0%, rgba(4, 7, 12, 0.98) 100%) !important;
  padding: 1rem 1.3rem !important;
  margin: 1.4rem 0 !important;
  border-radius: 3px !important;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5) !important;
}

.terminal-callout header {
  font-family: Impact, "Arial Black", sans-serif !important;
  font-size: 0.85rem !important;
  letter-spacing: 0.1em !important;
  color: #38bdf8 !important;
  text-transform: uppercase !important;
  margin-bottom: 0.4rem !important;
  display: flex !important;
  align-items: center !important;
  gap: 6px !important;
}

/* Responsive Table Styling */
.table-wrap {
  width: 100% !important;
  overflow-x: auto !important;
  margin: 1.4rem 0 1.8rem !important;
  border: 1px solid #223042 !important;
  border-radius: 4px !important;
  background: #06090e !important;
}

.data-table {
  width: 100% !important;
  border-collapse: collapse !important;
  font-size: 0.9rem !important;
  text-align: left !important;
}

.data-table th {
  background: linear-gradient(180deg, #111a28 0%, #0a101a 100%) !important;
  color: #f1df76 !important;
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 0.82rem !important;
  letter-spacing: 0.08em !important;
  text-transform: uppercase !important;
  padding: 0.75rem 0.9rem !important;
  border-bottom: 2px solid #223042 !important;
  white-space: nowrap !important;
}

.data-table td {
  padding: 0.7rem 0.9rem !important;
  border-bottom: 1px solid #16202c !important;
  color: #cbd5e1 !important;
  vertical-align: top !important;
  line-height: 1.5 !important;
}

.data-table tr:nth-child(even) {
  background: rgba(15, 23, 42, 0.4) !important;
}

.data-table tr:hover {
  background: rgba(56, 189, 248, 0.06) !important;
}

/* Styled Lists */
.article-body ul, .article-body ol {
  padding-left: 1.4rem !important;
  margin: 0.8rem 0 1.2rem !important;
}

.article-body li {
  margin-bottom: 0.5rem !important;
  color: #cbd5e1 !important;
}

.article-body li strong, .article-body li b {
  color: #f8fafc !important;
}
"""

css = css + stylized_rules

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("wiki.css enhanced with 100%-130% zoom safety and Project Moon stylization.")
