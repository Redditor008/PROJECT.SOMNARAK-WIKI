#!/usr/bin/env python3
"""
tools/upgrade_all_table_and_box_styles.py
Injects prominent, high-contrast, glowing, and beautifully styled CSS
for every table, box, callout, infobox, card, panel, and TOC across the wiki.
"""

CSS_ADDITIONS = """
/* ==========================================================================
   HIGH-CONTRAST MASTER TABLE & BOX STYLIZATION ENGINE
   ========================================================================== */

/* 1. MASTER TABLES & WRAPPERS */
.table-wrap,
.pm-table-wrapper {
  width: 100% !important;
  overflow-x: auto !important;
  -webkit-overflow-scrolling: touch !important;
  margin: 1.4rem 0 2rem !important;
  background: #080d17 !important;
  border: 2px solid #253952 !important;
  border-radius: 6px !important;
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.75), 0 0 12px rgba(37, 57, 82, 0.35) !important;
}

table,
table.wiki-table,
table.pm-table,
.data-table table,
.home-table,
.source-table {
  width: 100% !important;
  border-collapse: separate !important;
  border-spacing: 0 !important;
  font-size: 0.92rem !important;
  text-align: left !important;
  color: #e2e8f0 !important;
  background: transparent !important;
}

/* Table Header Cells */
table th,
table.wiki-table th,
table.pm-table th,
.data-table th,
.home-table th,
.source-table th {
  background: linear-gradient(180deg, #18283f 0%, #0c1624 100%) !important;
  color: #f1df76 !important;
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 0.88rem !important;
  letter-spacing: 0.08em !important;
  text-transform: uppercase !important;
  padding: 12px 16px !important;
  border-bottom: 2px solid #38bdf8 !important;
  border-right: 1px solid #1e334d !important;
  white-space: nowrap !important;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.8) !important;
}

table th:last-child,
table.wiki-table th:last-child,
table.pm-table th:last-child {
  border-right: none !important;
}

/* Table Body Cells */
table td,
table.wiki-table td,
table.pm-table td,
.data-table td,
.home-table td,
.source-table td {
  padding: 11px 16px !important;
  border-bottom: 1px solid #1b2b3f !important;
  border-right: 1px solid #14202e !important;
  color: #cbd5e1 !important;
  font-size: 0.92rem !important;
  line-height: 1.55 !important;
  background: rgba(10, 16, 26, 0.75) !important;
  transition: background 0.15s ease !important;
}

table td:last-child,
table.wiki-table td:last-child,
table.pm-table td:last-child {
  border-right: none !important;
}

/* Alternating Row Striping */
table tbody tr:nth-child(even) td,
table.wiki-table tbody tr:nth-child(even) td,
table.pm-table tbody tr:nth-child(even) td {
  background: rgba(16, 27, 44, 0.9) !important;
}

/* Row Hover State */
table tbody tr:hover td,
table.wiki-table tbody tr:hover td,
table.pm-table tbody tr:hover td {
  background: rgba(56, 189, 248, 0.18) !important;
  color: #ffffff !important;
}

/* Table Hyperlinks */
table td a,
table.wiki-table td a,
table.pm-table td a {
  color: #38bdf8 !important;
  font-weight: 600 !important;
  text-decoration: none !important;
}

table td a:hover,
table.wiki-table td a:hover,
table.pm-table td a:hover {
  color: #f1df76 !important;
  text-decoration: underline !important;
}

/* Table Code / Tags */
table td code,
table.wiki-table td code {
  background: #0f1c2e !important;
  border: 1px solid #2b4566 !important;
  color: #fef08a !important;
  padding: 2px 6px !important;
  border-radius: 3px !important;
  font-family: monospace !important;
  font-size: 0.82rem !important;
}

/* 2. MASTER CALLOUTS, DIRECTIVES & QUOTE BOXES */
.wiki-callout,
.terminal-callout,
.story-panel,
.entity-protocol {
  border: 2px solid #38bdf8 !important;
  border-left: 6px solid #38bdf8 !important;
  background: linear-gradient(135deg, #0a1424 0%, #050a12 100%) !important;
  padding: 16px 20px !important;
  margin: 1.6rem 0 !important;
  border-radius: 6px !important;
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.7), 0 0 16px rgba(56, 189, 248, 0.2) !important;
  position: relative !important;
}

.wiki-callout p,
.terminal-callout p,
.story-panel p,
.entity-protocol p {
  margin: 0 0 8px 0 !important;
  color: #e2e8f0 !important;
  font-size: 0.94rem !important;
  line-height: 1.65 !important;
}

.wiki-callout p:last-child,
.terminal-callout p:last-child {
  margin-bottom: 0 !important;
}

.wiki-callout header,
.terminal-callout header {
  font-family: Impact, "Arial Black", sans-serif !important;
  font-size: 0.9rem !important;
  letter-spacing: 0.1em !important;
  color: #f1df76 !important;
  text-transform: uppercase !important;
  margin-bottom: 8px !important;
  display: flex !important;
  align-items: center !important;
  gap: 8px !important;
  border-bottom: 1px solid rgba(241, 223, 118, 0.2) !important;
  padding-bottom: 4px !important;
}

/* Hazard Theme Callout */
.wiki-callout.hazard,
.terminal-callout.hazard,
.hazard-box {
  border-color: #ef5b55 !important;
  border-left-color: #ef5b55 !important;
  background: linear-gradient(135deg, #1f0b0e 0%, #0a0405 100%) !important;
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.7), 0 0 16px rgba(239, 91, 85, 0.25) !important;
}

.wiki-callout.hazard header,
.terminal-callout.hazard header {
  color: #ef5b55 !important;
  border-bottom-color: rgba(239, 91, 85, 0.25) !important;
}

/* Tactical Directive Box */
.tactical-directive-box {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  background: linear-gradient(90deg, #180e18 0%, #080d18 100%) !important;
  border: 2px solid #ef5b55 !important;
  border-left: 6px solid #f1df76 !important;
  padding: 14px 20px !important;
  margin: 1.6rem 0 !important;
  border-radius: 6px !important;
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.7), 0 0 16px rgba(239, 91, 85, 0.2) !important;
  box-sizing: border-box !important;
  width: 100% !important;
}

/* Quotes & Testimonials */
.entity-quote,
.wiki-quote,
blockquote {
  border-left: 5px solid #f1df76 !important;
  border-top: 1px solid rgba(241, 223, 118, 0.3) !important;
  border-bottom: 1px solid rgba(241, 223, 118, 0.3) !important;
  border-right: 1px solid rgba(241, 223, 118, 0.15) !important;
  background: linear-gradient(135deg, #141206 0%, #080802 100%) !important;
  padding: 16px 22px !important;
  border-radius: 4px !important;
  margin: 1.6rem 0 !important;
  font-style: italic !important;
  color: #fef08a !important;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.6), 0 0 12px rgba(241, 223, 118, 0.15) !important;
}

.quote-author {
  display: block !important;
  text-align: right !important;
  color: #f1df76 !important;
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 0.85rem !important;
  letter-spacing: 0.08em !important;
  margin-top: 8px !important;
  font-style: normal !important;
}

/* 3. INFOBOXES & ARTIFACT PANELS */
.entity-infobox,
.item-infobox,
.character-infobox,
.infobox {
  border: 2.5px solid #f1df76 !important;
  background: #080d16 !important;
  border-radius: 6px !important;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.9), 0 0 20px rgba(241, 223, 118, 0.2) !important;
  overflow: hidden !important;
  margin: 0 0 2rem 0 !important;
}

.entity-infobox > h2,
.item-infobox > h2,
.infobox > h2 {
  margin: 0 !important;
  padding: 12px 16px !important;
  background: linear-gradient(90deg, #b45309 0%, #78350f 100%) !important;
  color: #ffffff !important;
  font-family: Impact, "Arial Black", sans-serif !important;
  font-size: 1.3rem !important;
  letter-spacing: 0.08em !important;
  text-align: center !important;
  border-bottom: 2px solid #f1df76 !important;
  text-shadow: 0 2px 6px rgba(0, 0, 0, 0.8) !important;
}

.entity-infobox table,
.item-infobox table,
.infobox table {
  width: 100% !important;
  border-collapse: collapse !important;
  margin: 0 !important;
  background: transparent !important;
}

.entity-infobox table th,
.item-infobox table th,
.infobox table th {
  background: #0d1726 !important;
  color: #38bdf8 !important;
  border-bottom: 1px solid #1e334d !important;
  border-right: 1px solid #1e334d !important;
  padding: 8px 12px !important;
  font-size: 0.82rem !important;
  width: 35% !important;
}

.entity-infobox table td,
.item-infobox table td,
.infobox table td {
  background: #090e18 !important;
  color: #e2e8f0 !important;
  border-bottom: 1px solid #1e334d !important;
  border-right: none !important;
  padding: 8px 12px !important;
  font-size: 0.88rem !important;
}

/* 4. TABLE OF CONTENTS (TOC) */
.toc,
.article-toc,
.wiki-toc {
  border: 2px solid #38bdf8 !important;
  background: linear-gradient(135deg, #08101e 0%, #040810 100%) !important;
  border-radius: 6px !important;
  padding: 16px 22px !important;
  margin: 1.6rem 0 !important;
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.75), 0 0 16px rgba(56, 189, 248, 0.25) !important;
}

.toc-title {
  font-family: Impact, "Arial Black", sans-serif !important;
  font-size: 1rem !important;
  letter-spacing: 0.08em !important;
  color: #f1df76 !important;
  text-transform: uppercase !important;
  border-bottom: 1.5px solid rgba(241, 223, 118, 0.3) !important;
  padding-bottom: 6px !important;
  margin-bottom: 10px !important;
  display: flex !important;
  align-items: center !important;
  gap: 8px !important;
}

.toc ul,
.article-toc ul {
  list-style: none !important;
  padding-left: 0 !important;
  margin: 0 !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 6px !important;
}

.toc ul li a,
.article-toc ul li a {
  color: #cbd5e1 !important;
  text-decoration: none !important;
  font-size: 0.88rem !important;
  transition: all 0.15s ease !important;
}

.toc ul li a:hover,
.article-toc ul li a:hover {
  color: #38bdf8 !important;
  padding-left: 4px !important;
}

/* 5. CARDS & DIRECTORY BOXES */
.cross-ref-card {
  display: flex !important;
  align-items: center !important;
  gap: 12px !important;
  background: #08101c !important;
  border: 2px solid #223854 !important;
  padding: 12px 16px !important;
  border-radius: 6px !important;
  text-decoration: none !important;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.6) !important;
  transition: all 0.2s ease !important;
}

.cross-ref-card:hover {
  background: #0f1e34 !important;
  border-color: #38bdf8 !important;
  box-shadow: 0 0 20px rgba(56, 189, 248, 0.45) !important;
  transform: translateY(-3px) !important;
}

.pm-entity-card {
  background: linear-gradient(180deg, #0e182a 0%, #060a12 100%) !important;
  border: 2.5px solid var(--card-border, #38bdf8) !important;
  padding: 18px !important;
  border-radius: 6px !important;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.85), 0 0 16px rgba(56, 189, 248, 0.15) !important;
  transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

.pm-entity-card:hover {
  transform: translateY(-4px) !important;
  border-color: #f1df76 !important;
  box-shadow: 0 0 24px rgba(241, 223, 118, 0.5) !important;
}

.triad-card,
.equipment-card {
  background: #090e18 !important;
  border: 2px solid #223854 !important;
  border-radius: 6px !important;
  padding: 16px !important;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.7) !important;
}
"""

with open("/home/user/01_Somnarak_Wiki/assets/css/wiki.css", "a", encoding="utf-8") as f:
    f.write(CSS_ADDITIONS)

print("Injected high-contrast master table and box styles into wiki.css!")
