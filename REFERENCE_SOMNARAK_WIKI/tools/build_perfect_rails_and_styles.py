import os, sys, re

CSS_PATH = "/home/user/01_Somnarak_Wiki/assets/css/wiki.css"
WIKI_DIR = "/home/user/01_Somnarak_Wiki"

# 1. Update CSS with the stylized Left Rail and L-Corp Right Rail
lcorp_rails_css = '''
/* ==========================================================================
   L-CORP AUTHENTIC INDUSTRIAL RIGHT RAIL & HIGH-CLARITY LEFT RAIL
   ========================================================================== */

/* --------------------------------------------------------------------------
   LEFT SIDEBAR: HIGH-CLARITY, HIGH-CONTRAST PROJECT MOON NAV RAIL
   -------------------------------------------------------------------------- */
.left-rail {
  background: linear-gradient(180deg, #070a12 0%, #030508 100%) !important;
  border-right: 2px solid #2d181d !important;
  padding: 1.6rem 0.9rem !important;
  box-shadow: inset -5px 0 25px rgba(0, 0, 0, 0.9) !important;
}

.site-mark {
  padding-bottom: 1.4rem !important;
  margin-bottom: 1.2rem !important;
  border-bottom: 2px solid rgba(241, 223, 118, 0.25) !important;
  text-align: center !important;
}

.site-mark a {
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  text-decoration: none !important;
}

.site-mark img {
  width: 110px !important;
  height: 110px !important;
  filter: drop-shadow(0 0 16px rgba(241, 223, 118, 0.5)) !important;
  transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

.site-mark a:hover img {
  transform: scale(1.08) !important;
  filter: drop-shadow(0 0 24px rgba(241, 223, 118, 0.75)) !important;
}

.site-mark b {
  font-family: Impact, "Arial Black", sans-serif !important;
  font-size: 1.6rem !important;
  letter-spacing: 0.14em !important;
  color: #f1df76 !important;
  margin-top: 10px !important;
  text-shadow: 0 0 12px rgba(241, 223, 118, 0.6) !important;
  display: block !important;
}

.site-mark span {
  font-size: 0.72rem !important;
  letter-spacing: 0.22em !important;
  color: #38bdf8 !important;
  font-weight: 800 !important;
  text-transform: uppercase !important;
  display: block !important;
  margin-top: 2px !important;
}

.left-links {
  display: flex !important;
  flex-direction: column !important;
  gap: 1.1rem !important;
}

.left-links section {
  border: 1px solid #223042 !important;
  background: linear-gradient(135deg, rgba(8, 12, 20, 0.95) 0%, rgba(4, 6, 10, 0.98) 100%) !important;
  padding: 0.85rem !important;
  border-radius: 3px !important;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.6) !important;
}

.left-links h2 {
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 0.92rem !important;
  letter-spacing: 0.12em !important;
  color: #f1df76 !important;
  text-transform: uppercase !important;
  border-bottom: 2px solid #2a3a50 !important;
  padding-bottom: 5px !important;
  margin: 0 0 8px !important;
  display: flex !important;
  align-items: center !important;
  gap: 6px !important;
}

.left-links h2:before {
  content: "■" !important;
  color: #ef5b55 !important;
  font-size: 0.8em !important;
}

.left-links a {
  display: flex !important;
  align-items: center !important;
  gap: 8px !important;
  color: #e2e8f0 !important;
  padding: 6px 8px !important;
  font-size: 0.84rem !important;
  font-weight: 500 !important;
  text-decoration: none !important;
  border-left: 3px solid transparent !important;
  border-radius: 0 2px 2px 0 !important;
  margin-bottom: 2px !important;
  transition: all 0.18s ease !important;
}

.left-links a:hover {
  color: #ffffff !important;
  background: linear-gradient(90deg, rgba(241, 223, 118, 0.15) 0%, rgba(241, 223, 118, 0.02) 100%) !important;
  border-left-color: #f1df76 !important;
  padding-left: 12px !important;
  text-shadow: 0 0 8px rgba(255, 255, 255, 0.6) !important;
}

.left-links a.active {
  color: #f1df76 !important;
  background: linear-gradient(90deg, rgba(241, 223, 118, 0.22) 0%, rgba(241, 223, 118, 0.05) 100%) !important;
  border-left-color: #f1df76 !important;
  font-weight: 700 !important;
}

/* --------------------------------------------------------------------------
   RIGHT SIDEBAR: L-CORP AUTHENTIC HAZARD FLOOR RAIL (index.html ONLY)
   -------------------------------------------------------------------------- */
.floor-rail {
  display: flex !important;
  flex-direction: column !important;
  background: linear-gradient(180deg, #090e18 0%, #03050a 100%) !important;
  border-left: 3px solid #331d22 !important;
  padding: 1.6rem 1.1rem !important;
  box-shadow: inset 8px 0 25px rgba(0, 0, 0, 0.95) !important;
  width: 100% !important;
  min-width: 0 !important;
}

/* L-Corp Header */
.floor-rail-header {
  text-align: center !important;
  margin-bottom: 1.3rem !important;
  padding-bottom: 0.75rem !important;
  border-bottom: 2px solid #ef5b55 !important;
  position: relative !important;
}

.floor-rail-header h2 {
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 1.45rem !important;
  letter-spacing: 0.14em !important;
  color: #f1df76 !important;
  text-transform: uppercase !important;
  margin: 0 !important;
  text-shadow: 0 0 12px rgba(241, 223, 118, 0.5) !important;
}

.floor-rail-header small {
  font-family: "Courier New", monospace !important;
  font-size: 0.65rem !important;
  letter-spacing: 0.18em !important;
  color: #38bdf8 !important;
  display: block !important;
  margin-top: 3px !important;
  font-weight: bold !important;
}

/* L-Corp Tactical Hazard Buttons */
.pm-hazard-btn {
  position: relative !important;
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  height: 56px !important;
  margin: 7px 0 !important;
  padding: 6px 14px 6px 48px !important;
  border: 2px solid var(--floor-color, #f1df76) !important;
  background: linear-gradient(90deg, rgba(12, 18, 28, 0.96) 0%, rgba(5, 8, 14, 0.98) 100%) !important;
  text-decoration: none !important;
  border-radius: 3px !important;
  overflow: hidden !important;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.7), inset 0 0 8px rgba(0, 0, 0, 0.6) !important;
  transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

/* Authentic L-Corp Thick Yellow/Black Diagonal Hazard Strip */
.pm-hazard-btn:before {
  content: "" !important;
  position: absolute !important;
  left: 0 !important;
  top: 0 !important;
  bottom: 0 !important;
  width: 38px !important;
  background: repeating-linear-gradient(
    -45deg,
    #f1df76,
    #f1df76 7px,
    #05070a 7px,
    #05070a 14px
  ) !important;
  border-right: 2px solid var(--floor-color, #f1df76) !important;
  box-shadow: 2px 0 6px rgba(0, 0, 0, 0.8) !important;
}

.pm-hazard-btn:hover {
  transform: translateX(6px) !important;
  border-color: #ffffff !important;
  background: linear-gradient(90deg, rgba(24, 36, 54, 0.98) 0%, rgba(12, 18, 28, 0.98) 100%) !important;
  box-shadow: 0 0 20px var(--floor-color, rgba(241, 223, 118, 0.6)), inset 0 0 12px var(--floor-color, rgba(241, 223, 118, 0.3)) !important;
}

.pm-hazard-btn-text {
  display: flex !important;
  flex-direction: column !important;
  z-index: 2 !important;
  margin-left: 4px !important;
}

.pm-hazard-btn-text small {
  font-family: Impact, "Arial Black", sans-serif !important;
  font-size: 0.68rem !important;
  letter-spacing: 0.14em !important;
  color: #94a3b8 !important;
  text-transform: uppercase !important;
  line-height: 1 !important;
  margin-bottom: 2px !important;
}

.pm-hazard-btn-text b {
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 1.05rem !important;
  letter-spacing: 0.06em !important;
  color: var(--floor-color, #f1df76) !important;
  text-transform: uppercase !important;
  text-shadow: 0 2px 6px rgba(0, 0, 0, 0.9) !important;
  line-height: 1.1 !important;
}

.pm-hazard-btn img {
  width: 42px !important;
  height: 42px !important;
  min-width: 42px !important;
  object-fit: contain !important;
  filter: drop-shadow(0 0 8px var(--floor-color, rgba(241, 223, 118, 0.5))) !important;
  transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
  z-index: 2 !important;
}

.pm-hazard-btn:hover img {
  transform: scale(1.18) rotate(3deg) !important;
}

/* L-Corp Heavy Action Buttons */
.pm-action-btn {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  padding: 11px 14px 11px 48px !important;
  margin: 12px 0 !important;
  border: 2px solid #f1df76 !important;
  background: linear-gradient(90deg, #141c2c 0%, #090e18 100%) !important;
  color: #ffffff !important;
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 1rem !important;
  letter-spacing: 0.1em !important;
  text-transform: uppercase !important;
  position: relative !important;
  text-decoration: none !important;
  border-radius: 3px !important;
  box-shadow: 0 0 16px rgba(241, 223, 118, 0.25) !important;
  transition: all 0.2s ease !important;
}

.pm-action-btn:before {
  content: "" !important;
  position: absolute !important;
  left: 0 !important;
  top: 0 !important;
  bottom: 0 !important;
  width: 38px !important;
  background: repeating-linear-gradient(
    -45deg,
    #ef5b55,
    #ef5b55 7px,
    #05070a 7px,
    #05070a 14px
  ) !important;
  border-right: 2px solid #f1df76 !important;
}

.pm-action-btn:hover {
  background: #1e2a42 !important;
  border-color: #ffffff !important;
  box-shadow: 0 0 22px rgba(241, 223, 118, 0.6) !important;
  transform: translateY(-2px) !important;
}

.pm-action-btn img {
  width: 30px !important;
  height: 30px !important;
  object-fit: contain !important;
}

/* Sister Projects Framed Cards */
.pm-related-section {
  margin-top: 1.8rem !important;
  border-top: 2px solid #2d181d !important;
  padding-top: 1.3rem !important;
}

.pm-related-section h3 {
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 0.92rem !important;
  letter-spacing: 0.14em !important;
  color: #38bdf8 !important;
  text-transform: uppercase !important;
  margin: 0 0 12px !important;
  display: flex !important;
  align-items: center !important;
  gap: 6px !important;
}

.pm-related-section h3:before {
  content: "///" !important;
  color: #ef5b55 !important;
}

.pm-related-card {
  display: block !important;
  border: 2px solid #223042 !important;
  background: #05080e !important;
  margin-bottom: 12px !important;
  text-decoration: none !important;
  border-radius: 3px !important;
  overflow: hidden !important;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.7) !important;
  transition: all 0.22s ease !important;
}

.pm-related-card:hover {
  border-color: #f1df76 !important;
  box-shadow: 0 0 16px rgba(241, 223, 118, 0.4) !important;
  transform: translateY(-3px) !important;
}

.pm-related-card img {
  width: 100% !important;
  height: 110px !important;
  object-fit: cover !important;
  border-bottom: 1px solid #1e293b !important;
  display: block !important;
}

.pm-related-card span {
  display: block !important;
  padding: 8px 12px !important;
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 0.85rem !important;
  letter-spacing: 0.08em !important;
  color: #f1df76 !important;
  text-transform: uppercase !important;
  background: #090e18 !important;
}

'''

with open(CSS_PATH, "a", encoding="utf-8") as f:
    f.write("\n" + lcorp_rails_css)

print("L-Corp Right Rail & High-Clarity Left Rail CSS appended.")
