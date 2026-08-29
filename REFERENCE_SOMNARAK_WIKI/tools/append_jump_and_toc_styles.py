#!/usr/bin/env python3
"""
tools/append_jump_and_toc_styles.py
Appends comprehensive wiki.gg/MediaWiki authentic TOC, jump navigation,
target pulse highlight, floating active tracking, and back-to-top styles.
"""

import os

WIKI_CSS = "/home/user/01_Somnarak_Wiki/assets/css/wiki.css"

JUMP_CSS = """

/* ==========================================================================
   WIKI.GG / MEDIAWIKI AUTHENTIC JUMP NAVIGATION & TOC STYLES
   ========================================================================== */

/* 1. In-Article Table of Contents (#toc) Box */
#toc, .toc {
  background: linear-gradient(180deg, #0a101d 0%, #050810 100%) !important;
  border: 1.5px solid #22354d !important;
  border-left: 4px solid #f1df76 !important;
  padding: 14px 18px !important;
  margin: 1.6rem 0 2rem !important;
  border-radius: 4px !important;
  display: table !important;
  min-width: min(320px, 100%) !important;
  max-width: 100% !important;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.7) !important;
  box-sizing: border-box !important;
}

.toctitle, .toc-title {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  gap: 12px !important;
  padding-bottom: 8px !important;
  margin-bottom: 10px !important;
  border-bottom: 1px solid rgba(241, 223, 118, 0.25) !important;
}

.toctitle h2, .toc-title h2, #toc-heading {
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 1.05rem !important;
  letter-spacing: 0.1em !important;
  color: #f1df76 !important;
  margin: 0 !important;
  padding: 0 !important;
  border: none !important;
  text-transform: uppercase !important;
}

.toc-toggle-btn {
  background: transparent !important;
  border: none !important;
  color: #38bdf8 !important;
  font-family: "Courier New", monospace !important;
  font-size: 0.8rem !important;
  font-weight: bold !important;
  cursor: pointer !important;
  padding: 2px 6px !important;
  border-radius: 2px !important;
  transition: all 0.15s ease !important;
}

.toc-toggle-btn:hover {
  color: #fff !important;
  background: rgba(56, 189, 248, 0.15) !important;
}

#toc ul, .toc ul {
  list-style: none !important;
  padding: 0 !important;
  margin: 0 !important;
}

#toc ul ul, .toc ul ul {
  padding-left: 18px !important;
  margin-top: 4px !important;
}

#toc li, .toc li {
  margin-bottom: 6px !important;
  font-size: 0.88rem !important;
  line-height: 1.4 !important;
}

#toc a, .toc a {
  color: #cbd5e1 !important;
  text-decoration: none !important;
  display: inline-flex !important;
  align-items: baseline !important;
  gap: 6px !important;
  padding: 2px 4px !important;
  border-radius: 2px !important;
  transition: all 0.15s ease !important;
}

#toc a:hover, .toc a:hover {
  color: #f1df76 !important;
  background: rgba(241, 223, 118, 0.12) !important;
}

.tocnumber {
  color: #38bdf8 !important;
  font-family: "Courier New", monospace !important;
  font-weight: bold !important;
  font-size: 0.82rem !important;
}

.toctext {
  color: #e2e8f0 !important;
}

/* 2. Floating Quick-TOC Navigation Widget */
.float-toc {
  position: fixed !important;
  bottom: 24px !important;
  left: 24px !important;
  z-index: 95 !important;
}

.float-toc-trigger {
  display: flex !important;
  align-items: center !important;
  gap: 8px !important;
  background: #090e18 !important;
  border: 1.5px solid #f1df76 !important;
  color: #f1df76 !important;
  padding: 8px 14px !important;
  border-radius: 20px !important;
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 0.85rem !important;
  letter-spacing: 0.08em !important;
  cursor: pointer !important;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.8), 0 0 10px rgba(241, 223, 118, 0.3) !important;
  transition: all 0.2s ease !important;
}

.float-toc-trigger:hover {
  background: #141f33 !important;
  color: #ffffff !important;
  transform: translateY(-2px) !important;
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.9), 0 0 14px rgba(56, 189, 248, 0.5) !important;
}

.float-toc-panel {
  display: none !important;
  position: absolute !important;
  bottom: 48px !important;
  left: 0 !important;
  width: min(340px, 85vw) !important;
  max-height: min(480px, 70vh) !important;
  overflow-y: auto !important;
  background: #060910 !important;
  border: 1.5px solid #223854 !important;
  border-left: 4px solid #38bdf8 !important;
  border-radius: 6px !important;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.9) !important;
  padding: 12px 14px !important;
  box-sizing: border-box !important;
}

.float-toc.open .float-toc-panel {
  display: block !important;
  animation: floatTocFadeIn 0.18s ease-out !important;
}

@keyframes floatTocFadeIn {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}

.float-toc-header {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  padding-bottom: 8px !important;
  margin-bottom: 8px !important;
  border-bottom: 1px solid #1e293b !important;
}

.float-toc-header b {
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 0.88rem !important;
  color: #f1df76 !important;
  letter-spacing: 0.08em !important;
}

.float-toc-count {
  font-family: "Courier New", monospace !important;
  font-size: 0.72rem !important;
  color: #64748b !important;
  font-weight: bold !important;
}

.float-toc-list {
  list-style: none !important;
  padding: 0 !important;
  margin: 0 !important;
}

.float-toc-list li {
  margin-bottom: 4px !important;
}

.float-toc-list a {
  display: flex !important;
  align-items: center !important;
  gap: 8px !important;
  color: #94a3b8 !important;
  font-size: 0.82rem !important;
  padding: 5px 8px !important;
  border-radius: 3px !important;
  text-decoration: none !important;
  border-left: 2px solid transparent !important;
  transition: all 0.15s ease !important;
}

.float-toc-list a:hover {
  color: #fff !important;
  background: rgba(56, 189, 248, 0.12) !important;
  border-left-color: #38bdf8 !important;
}

.float-toc-list a.active-toc-item {
  color: #f1df76 !important;
  background: rgba(241, 223, 118, 0.15) !important;
  border-left-color: #f1df76 !important;
  font-weight: bold !important;
}

.float-toc-sub a {
  padding-left: 18px !important;
  font-size: 0.78rem !important;
}

/* 3. Target Jump Pulse Highlight Animation */
.target-jump-highlight {
  animation: sectionJumpPulse 2.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
  border-radius: 4px !important;
}

@keyframes sectionJumpPulse {
  0% {
    background-color: rgba(241, 223, 118, 0.35) !important;
    outline: 3px solid #f1df76 !important;
    box-shadow: 0 0 24px rgba(241, 223, 118, 0.6) !important;
  }
  50% {
    background-color: rgba(56, 189, 248, 0.2) !important;
    outline: 2px solid #38bdf8 !important;
    box-shadow: 0 0 16px rgba(56, 189, 248, 0.4) !important;
  }
  100% {
    background-color: transparent !important;
    outline: 0px solid transparent !important;
    box-shadow: none !important;
  }
}

/* 4. Section Heading Anchor Permalinks */
.heading-permalink {
  display: inline-flex !important;
  align-items: center !important;
  margin-left: 8px !important;
  color: #64748b !important;
  font-size: 0.8em !important;
  text-decoration: none !important;
  opacity: 0 !important;
  transition: opacity 0.2s ease, color 0.2s ease !important;
  position: relative !important;
}

h2:hover .heading-permalink,
h3:hover .heading-permalink,
.section-banner:hover .heading-permalink {
  opacity: 1 !important;
}

.heading-permalink:hover {
  color: #f1df76 !important;
}

.permalink-tooltip {
  position: absolute !important;
  top: -24px !important;
  left: 50% !important;
  transform: translateX(-50%) !important;
  background: #0f172a !important;
  border: 1px solid #f1df76 !important;
  color: #f1df76 !important;
  font-size: 0.65rem !important;
  padding: 2px 6px !important;
  border-radius: 2px !important;
  white-space: nowrap !important;
  display: none !important;
}

.heading-permalink:hover .permalink-tooltip {
  display: block !important;
}

/* 5. Floating Back-to-Top Button */
.back-to-top-btn {
  position: fixed !important;
  bottom: 24px !important;
  right: 24px !important;
  z-index: 95 !important;
  background: #090e18 !important;
  border: 1.5px solid #38bdf8 !important;
  color: #38bdf8 !important;
  padding: 8px 14px !important;
  border-radius: 20px !important;
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 0.82rem !important;
  letter-spacing: 0.08em !important;
  cursor: pointer !important;
  opacity: 0 !important;
  pointer-events: none !important;
  transform: translateY(10px) !important;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.8) !important;
  transition: all 0.22s ease !important;
}

.back-to-top-btn.visible {
  opacity: 1 !important;
  pointer-events: auto !important;
  transform: translateY(0) !important;
}

.back-to-top-btn:hover {
  background: #101c30 !important;
  border-color: #f1df76 !important;
  color: #f1df76 !important;
  box-shadow: 0 0 16px rgba(241, 223, 118, 0.45) !important;
  transform: translateY(-2px) !important;
}
"""

with open(WIKI_CSS, "a", encoding="utf-8") as f:
    f.write(JUMP_CSS)

print("Appended complete wiki.gg / MediaWiki authentic jump navigation styles to wiki.css!")
