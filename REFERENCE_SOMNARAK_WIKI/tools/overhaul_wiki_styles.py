import os, re

CSS_PATH = "/home/user/01_Somnarak_Wiki/assets/css/wiki.css"

with open(CSS_PATH, "r", encoding="utf-8") as f:
    css = f.read()

# Let's inspect where .floor-rail is forced to grid-column: 1/-1
# Remove the bad overrides that break the vertical right sidebar
css_cleaned = re.sub(r'\.floor-rail\s*\{[^}]*grid-column:\s*1\s*/\s*-1[^}]*\}', '', css)

# Add our master Project Moon / Somnarak High-Tech Terminal CSS Suite
pm_master_css = '''
/* ==========================================================================
   PROJECT MOON / SOMNARAK CANONICAL HIGH-CONTRAST TERMINAL STYLES
   ========================================================================== */

/* Root World Colors */
:root {
  --sn-gold: #f1df76;
  --sn-gold-glow: rgba(241, 223, 118, 0.4);
  --sn-cyan: #38bdf8;
  --sn-cyan-glow: rgba(56, 189, 248, 0.4);
  --sn-crimson: #ef5b55;
  --sn-crimson-glow: rgba(239, 91, 85, 0.4);
  --sn-green: #71efaf;
  --sn-green-glow: rgba(113, 239, 175, 0.4);
  --sn-dark-bg: #040609;
  --sn-panel-bg: #070a10;
  --sn-border: #221518;
  --sn-border-bright: #3d2227;
}

body {
  background-color: #040609 !important;
  background-image: 
    radial-gradient(circle at 50% 0%, rgba(13, 26, 44, 0.5) 0%, transparent 60%),
    linear-gradient(rgba(241, 223, 118, 0.015) 1px, transparent 1px),
    linear-gradient(90deg, rgba(241, 223, 118, 0.015) 1px, transparent 1px) !important;
  background-size: 100% 100%, 32px 32px, 32px 32px !important;
  color: #e2e8f0 !important;
  font-family: Arial, "Segoe UI", -apple-system, sans-serif !important;
}

/* Master Wiki Shell */
.wiki-shell {
  width: min(1680px, 98vw) !important;
  margin: 1rem auto 3rem !important;
  background: rgba(6, 9, 14, 0.98) !important;
  border: 1px solid #331d22 !important;
  box-shadow: 0 0 40px rgba(0, 0, 0, 0.95), inset 0 0 20px rgba(0, 0, 0, 0.8) !important;
  display: grid !important;
  grid-template-columns: 220px minmax(0, 1fr) !important;
}

/* Home Page Shell: Strict 3-Column Grid with Proud Vertical Right Rail */
.wiki-shell.home-shell {
  grid-template-columns: 220px minmax(0, 1fr) 310px !important;
}

@media (max-width: 1200px) {
  .wiki-shell.home-shell {
    grid-template-columns: 200px minmax(0, 1fr) 280px !important;
  }
}

@media (max-width: 992px) {
  .wiki-shell, .wiki-shell.home-shell {
    grid-template-columns: 1fr !important;
  }
  .left-rail, .floor-rail {
    border: 0 !important;
    border-bottom: 2px solid #331d22 !important;
  }
}

/* Left Navigation Rail */
.left-rail {
  background: linear-gradient(180deg, #070a10 0%, #030407 100%) !important;
  border-right: 1px solid #2d181d !important;
  padding: 1.5rem 1rem !important;
}

.site-mark a {
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  text-decoration: none !important;
  padding-bottom: 1.2rem !important;
  border-bottom: 1px solid rgba(241, 223, 118, 0.2) !important;
}

.site-mark img {
  width: 96px !important;
  height: 96px !important;
  filter: drop-shadow(0 0 12px rgba(241, 223, 118, 0.4)) !important;
  transition: transform 0.2s ease !important;
}

.site-mark a:hover img {
  transform: scale(1.05) !important;
}

.site-mark b {
  font-family: Impact, "Arial Black", sans-serif !important;
  font-size: 1.5rem !important;
  letter-spacing: 0.12em !important;
  color: var(--sn-gold) !important;
  margin-top: 8px !important;
  text-shadow: 0 0 10px rgba(241, 223, 118, 0.5) !important;
}

.site-mark span {
  font-size: 0.68rem !important;
  letter-spacing: 0.2em !important;
  color: #38bdf8 !important;
  font-weight: bold !important;
}

.left-links section {
  border: 1px solid #1f293d !important;
  background: #05080e !important;
  margin-top: 1rem !important;
  padding: 0.75rem !important;
  border-radius: 2px !important;
}

.left-links h2 {
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 0.88rem !important;
  letter-spacing: 0.1em !important;
  color: var(--sn-gold) !important;
  text-transform: uppercase !important;
  border-bottom: 1px solid #1e293b !important;
  padding-bottom: 4px !important;
  margin: 0 0 6px !important;
}

.left-links a {
  display: flex !important;
  align-items: center !important;
  gap: 6px !important;
  color: #cbd5e1 !important;
  padding: 4px 6px !important;
  font-size: 0.82rem !important;
  text-decoration: none !important;
  border-left: 2px solid transparent !important;
  transition: all 0.15s ease !important;
}

.left-links a:hover {
  color: #fff !important;
  background: rgba(56, 189, 248, 0.12) !important;
  border-left-color: var(--sn-cyan) !important;
  padding-left: 9px !important;
}

/* ==========================================================================
   RIGHT SIDEBAR: AUTHENTIC PROJECT MOON HAZARD FLOOR RAIL
   ========================================================================== */
.floor-rail {
  display: block !important;
  grid-column: auto !important;
  background: linear-gradient(180deg, #090d16 0%, #030508 100%) !important;
  border-left: 2px solid #331d22 !important;
  padding: 1.5rem 1rem !important;
  box-shadow: inset 5px 0 20px rgba(0, 0, 0, 0.8) !important;
}

.floor-rail > h2 {
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 1.35rem !important;
  letter-spacing: 0.12em !important;
  color: var(--sn-gold) !important;
  text-align: center !important;
  text-transform: uppercase !important;
  margin: 0 0 1.2rem !important;
  padding-bottom: 0.5rem !important;
  border-bottom: 2px solid rgba(241, 223, 118, 0.3) !important;
  text-shadow: 0 0 10px rgba(241, 223, 118, 0.4) !important;
}

/* Tactical Hazard Chevron Buttons */
.pm-hazard-btn {
  position: relative !important;
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  height: 54px !important;
  margin: 8px 0 !important;
  padding: 6px 12px 6px 44px !important;
  border: 2px solid var(--floor-color, #f1df76) !important;
  background: linear-gradient(90deg, rgba(8, 12, 18, 0.95) 0%, rgba(4, 6, 9, 0.98) 100%) !important;
  text-decoration: none !important;
  border-radius: 3px !important;
  overflow: hidden !important;
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.6) !important;
}

/* Authentic Diagonal Yellow-Black Hazard Striping */
.pm-hazard-btn:before {
  content: "" !important;
  position: absolute !important;
  left: 0 !important;
  top: 0 !important;
  bottom: 0 !important;
  width: 36px !important;
  background: repeating-linear-gradient(
    -45deg,
    #f1df76,
    #f1df76 6px,
    #05070a 6px,
    #05070a 12px
  ) !important;
  border-right: 2px solid var(--floor-color, #f1df76) !important;
}

.pm-hazard-btn:hover {
  transform: translateX(4px) !important;
  background: linear-gradient(90deg, rgba(18, 26, 38, 0.95) 0%, rgba(10, 15, 24, 0.98) 100%) !important;
  box-shadow: 0 0 16px var(--floor-color, rgba(241, 223, 118, 0.5)), inset 0 0 10px var(--floor-color, rgba(241, 223, 118, 0.2)) !important;
  border-color: #fff !important;
}

.pm-hazard-btn-text {
  display: flex !important;
  flex-direction: column !important;
  z-index: 2 !important;
}

.pm-hazard-btn-text small {
  font-family: Impact, "Arial Black", sans-serif !important;
  font-size: 0.65rem !important;
  letter-spacing: 0.12em !important;
  color: #94a3b8 !important;
  text-transform: uppercase !important;
}

.pm-hazard-btn-text b {
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 0.98rem !important;
  letter-spacing: 0.06em !important;
  color: var(--floor-color, #f1df76) !important;
  text-transform: uppercase !important;
  text-shadow: 0 1px 4px rgba(0, 0, 0, 0.8) !important;
}

.pm-hazard-btn img {
  width: 36px !important;
  height: 36px !important;
  object-fit: contain !important;
  filter: drop-shadow(0 0 6px var(--floor-color, rgba(241, 223, 118, 0.4))) !important;
  transition: transform 0.2s ease !important;
  z-index: 2 !important;
}

.pm-hazard-btn:hover img {
  transform: scale(1.15) !important;
}

/* Bold Action Buttons */
.pm-action-btn {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  padding: 10px 14px 10px 44px !important;
  margin: 12px 0 !important;
  border: 2px solid var(--sn-gold) !important;
  background: linear-gradient(90deg, #121824 0%, #090d14 100%) !important;
  color: #fff !important;
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 0.95rem !important;
  letter-spacing: 0.08em !important;
  position: relative !important;
  text-decoration: none !important;
  border-radius: 3px !important;
  box-shadow: 0 0 14px rgba(241, 223, 118, 0.2) !important;
  transition: all 0.2s ease !important;
}

.pm-action-btn:before {
  content: "" !important;
  position: absolute !important;
  left: 0 !important;
  top: 0 !important;
  bottom: 0 !important;
  width: 36px !important;
  background: repeating-linear-gradient(
    -45deg,
    #ef5b55,
    #ef5b55 6px,
    #05070a 6px,
    #05070a 12px
  ) !important;
  border-right: 2px solid var(--sn-gold) !important;
}

.pm-action-btn:hover {
  background: #1c2436 !important;
  border-color: #fff !important;
  box-shadow: 0 0 20px rgba(241, 223, 118, 0.5) !important;
  transform: translateY(-2px) !important;
}

.pm-action-btn img {
  width: 28px !important;
  height: 28px !important;
  object-fit: contain !important;
}

/* Related Directories Section */
.pm-related-section {
  margin-top: 1.8rem !important;
  border-top: 1px solid #2d181d !important;
  padding-top: 1.2rem !important;
}

.pm-related-section h3 {
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 0.88rem !important;
  letter-spacing: 0.12em !important;
  color: #38bdf8 !important;
  text-transform: uppercase !important;
  margin: 0 0 10px !important;
}

.pm-related-card {
  display: block !important;
  border: 1px solid #223042 !important;
  background: #05080e !important;
  margin-bottom: 10px !important;
  text-decoration: none !important;
  border-radius: 3px !important;
  overflow: hidden !important;
  transition: all 0.2s ease !important;
}

.pm-related-card:hover {
  border-color: #f1df76 !important;
  box-shadow: 0 0 12px rgba(241, 223, 118, 0.3) !important;
  transform: translateY(-2px) !important;
}

.pm-related-card img {
  width: 100% !important;
  height: 100px !important;
  object-fit: cover !important;
  border-bottom: 1px solid #1e293b !important;
  display: block !important;
}

.pm-related-card span {
  display: block !important;
  padding: 8px 10px !important;
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 0.82rem !important;
  letter-spacing: 0.08em !important;
  color: #f1df76 !important;
  text-transform: uppercase !important;
}

/* ==========================================================================
   HOMEPAGE HERO & CHAMFERED TECH CONTAINERS
   ========================================================================== */
.pm-hero-container {
  border: 2px solid #2a4365 !important;
  background: radial-gradient(circle at 80% 40%, rgba(14, 42, 71, 0.6) 0%, rgba(4, 7, 12, 0.98) 100%) !important;
  margin-bottom: 1.8rem !important;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.8) !important;
  border-radius: 4px !important;
  overflow: hidden !important;
}

.pm-hero-main {
  padding: 2.2rem 2.5rem !important;
}

.pm-brand-row {
  display: flex !important;
  align-items: center !important;
  gap: 20px !important;
  margin-bottom: 1rem !important;
}

.pm-brand-row img {
  width: 80px !important;
  height: 80px !important;
  filter: drop-shadow(0 0 15px rgba(241, 223, 118, 0.6)) !important;
}

.pm-brand-text h1 {
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: clamp(2.8rem, 4.5vw, 4.2rem) !important;
  line-height: 0.9 !important;
  letter-spacing: 0.04em !important;
  color: var(--sn-gold) !important;
  margin: 0 !important;
  text-shadow: 0 0 20px rgba(241, 223, 118, 0.4) !important;
}

.pm-brand-text h1 span {
  color: #38bdf8 !important;
  font-size: 0.7em !important;
  margin-left: 8px !important;
}

.pm-brand-text strong {
  display: block !important;
  font-size: 0.85rem !important;
  letter-spacing: 0.25em !important;
  color: #e2e8f0 !important;
  margin-top: 6px !important;
}

.pm-hero-subtext {
  max-width: 850px !important;
  font-size: 1.02rem !important;
  color: #cbd5e1 !important;
  line-height: 1.6 !important;
}

.pm-slogan-bar {
  background: linear-gradient(90deg, #991b1b 0%, #ef4444 50%, #7f1d1d 100%) !important;
  color: #fff !important;
  padding: 12px 24px !important;
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 1.15rem !important;
  letter-spacing: 0.12em !important;
  display: flex !important;
  justify-content: space-between !important;
  align-items: center !important;
  border-top: 1px solid #f87171 !important;
  text-shadow: 0 1px 4px rgba(0, 0, 0, 0.8) !important;
}

.pm-slogan-bar span {
  font-family: Arial, "Segoe UI", sans-serif !important;
  font-size: 0.82rem !important;
  letter-spacing: 0.08em !important;
  opacity: 0.9 !important;
}

/* Chamfered 45-degree Angled Synopsis Box */
.pm-intro-chamfer {
  position: relative !important;
  background: linear-gradient(135deg, #090d16 0%, #040609 100%) !important;
  border: 2px solid #d97706 !important;
  padding: 1.8rem 2.2rem !important;
  margin-bottom: 2.2rem !important;
  box-shadow: 0 0 25px rgba(217, 119, 6, 0.25) !important;
  clip-path: polygon(
    0 0, 
    calc(100% - 24px) 0, 
    100% 24px, 
    100% 100%, 
    24px 100%, 
    0 calc(100% - 24px)
  ) !important;
}

.pm-intro-chamfer p {
  margin: 0 0 0.8rem !important;
  font-size: 0.98rem !important;
  line-height: 1.7 !important;
  color: #e2e8f0 !important;
}

.pm-intro-chamfer p:last-child {
  margin-bottom: 0 !important;
  color: #f1df76 !important;
  font-weight: 600 !important;
}

/* 2x4 Feature Portal Grid */
.pm-feature-grid {
  display: grid !important;
  grid-template-columns: repeat(4, 1fr) !important;
  gap: 16px !important;
  margin-top: 1.5rem !important;
}

@media (max-width: 1100px) {
  .pm-feature-grid {
    grid-template-columns: repeat(2, 1fr) !important;
  }
}

@media (max-width: 600px) {
  .pm-feature-grid {
    grid-template-columns: 1fr !important;
  }
}

.pm-card {
  position: relative !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  min-height: 190px !important;
  padding: 24px 14px 18px !important;
  border: 2px solid #71efaf !important;
  background: radial-gradient(circle at 50% 50%, rgba(113, 239, 175, 0.08) 0%, rgba(4, 7, 12, 0.98) 100%) !important;
  color: #71efaf !important;
  text-decoration: none !important;
  border-radius: 4px !important;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.7) !important;
}

.pm-card.gold {
  border-color: #f1df76 !important;
  background: radial-gradient(circle at 50% 50%, rgba(241, 223, 118, 0.08) 0%, rgba(4, 7, 12, 0.98) 100%) !important;
  color: #f1df76 !important;
}

.pm-card.crimson {
  border-color: #ef5b55 !important;
  background: radial-gradient(circle at 50% 50%, rgba(239, 91, 85, 0.08) 0%, rgba(4, 7, 12, 0.98) 100%) !important;
  color: #ef5b55 !important;
}

.pm-card.cyan {
  border-color: #38bdf8 !important;
  background: radial-gradient(circle at 50% 50%, rgba(56, 189, 248, 0.08) 0%, rgba(4, 7, 12, 0.98) 100%) !important;
  color: #38bdf8 !important;
}

.pm-card:hover {
  transform: translateY(-4px) !important;
  box-shadow: 0 0 25px currentColor !important;
  border-color: #fff !important;
}

.pm-card-title {
  position: absolute !important;
  top: -12px !important;
  background: #040609 !important;
  padding: 2px 10px !important;
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 0.85rem !important;
  letter-spacing: 0.12em !important;
  color: inherit !important;
  text-transform: uppercase !important;
  border: 1px solid currentColor !important;
  border-radius: 2px !important;
}

.pm-card-icon {
  width: 84px !important;
  height: 84px !important;
  object-fit: contain !important;
  margin: 8px 0 10px !important;
  filter: drop-shadow(0 0 10px currentColor) !important;
  transition: transform 0.2s ease !important;
}

.pm-card:hover .pm-card-icon {
  transform: scale(1.1) !important;
}

.pm-card-sub {
  font-size: 0.76rem !important;
  color: #cbd5e1 !important;
  text-align: center !important;
  line-height: 1.35 !important;
}

'''

with open(CSS_PATH, "w", encoding="utf-8") as f:
    f.write(css_cleaned + "\n" + pm_master_css)

print("Master visual styling and right rail overhaul appended to wiki.css.")
