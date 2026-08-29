import re

CSS_PATH = "/home/user/01_Somnarak_Wiki/assets/css/wiki.css"
INDEX_PATH = "/home/user/01_Somnarak_Wiki/index.html"

# 1. Append the sleek console styling for the Right Sidebar
sidebar_css = '''
/* ==========================================================================
   ULTIMATE RIGHT SIDEBAR: CONSOLE CARDS, MINI-BANNERS & CIRCULAR BADGES
   ========================================================================== */

/* Floor Rail Container */
.floor-rail {
  display: flex !important;
  flex-direction: column !important;
  gap: 12px !important;
  background: linear-gradient(180deg, #0a0e17 0%, #04060b 100%) !important;
  border-left: 3px solid #22344c !important;
  padding: 1.4rem 1rem !important;
  box-shadow: inset 10px 0 30px rgba(0, 0, 0, 0.95) !important;
  width: 100% !important;
  box-sizing: border-box !important;
}

/* Master Diagnostic Header Widget */
.floor-console-header {
  background: linear-gradient(135deg, #140608 0%, #0d1626 100%) !important;
  border: 2px solid #ef5b55 !important;
  border-radius: 6px !important;
  padding: 12px 14px !important;
  margin-bottom: 8px !important;
  box-shadow: 0 0 20px rgba(239, 91, 85, 0.3) !important;
}

.console-header-top {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  margin-bottom: 8px !important;
}

.console-radar-icon {
  width: 44px !important;
  height: 44px !important;
  object-fit: contain !important;
}

.console-title-wrap h2 {
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 1.35rem !important;
  letter-spacing: 0.12em !important;
  color: #f1df76 !important;
  margin: 0 !important;
  text-transform: uppercase !important;
}

.console-title-wrap small {
  font-family: "Courier New", monospace !important;
  font-size: 0.7rem !important;
  letter-spacing: 0.1em !important;
  color: #38bdf8 !important;
  font-weight: bold !important;
}

.console-status-bar {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  background: #060910 !important;
  border: 1px solid #1c2a3e !important;
  padding: 5px 10px !important;
  border-radius: 3px !important;
  font-family: "Courier New", monospace !important;
  font-size: 0.72rem !important;
  color: #94a3b8 !important;
}

/* Sleek Bespoke Floor Console Cards */
.floor-card-item {
  display: block !important;
  background: #080c14 !important;
  border: 2px solid var(--floor-border, #24354c) !important;
  border-radius: 6px !important;
  overflow: hidden !important;
  text-decoration: none !important;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.8) !important;
  transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1) !important;
  position: relative !important;
}

.floor-card-item:hover {
  border-color: #f1df76 !important;
  box-shadow: 0 0 20px var(--floor-glow, rgba(241, 223, 118, 0.5)), inset 0 0 10px rgba(0, 0, 0, 0.5) !important;
  transform: translateX(-4px) translateY(-2px) !important;
}

.floor-card-banner {
  width: 100% !important;
  height: auto !important;
  display: block !important;
  border-bottom: 1.5px solid var(--floor-border, #1e2c3e) !important;
}

/* Floor Details Strip Beneath Mini-Banner */
.floor-card-body {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  padding: 8px 12px !important;
  background: linear-gradient(90deg, #070a12 0%, #0c1422 100%) !important;
}

.floor-lead-info {
  display: flex !important;
  align-items: center !important;
  gap: 8px !important;
}

.floor-lead-avatar {
  width: 32px !important;
  height: 32px !important;
  border-radius: 50% !important;
  border: 1.5px solid var(--floor-border, #38bdf8) !important;
}

.floor-lead-text {
  display: flex !important;
  flex-direction: column !important;
}

.floor-lead-name {
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 0.82rem !important;
  color: #f1df76 !important;
  letter-spacing: 0.05em !important;
  text-transform: uppercase !important;
}

.floor-lead-role {
  font-family: "Courier New", monospace !important;
  font-size: 0.64rem !important;
  color: #94a3b8 !important;
  text-transform: uppercase !important;
}

.floor-card-pill {
  font-family: "Courier New", monospace !important;
  font-size: 0.68rem !important;
  font-weight: bold !important;
  padding: 3px 8px !important;
  border-radius: 3px !important;
  background: #111a28 !important;
  border: 1px solid var(--floor-border, #24354c) !important;
  color: var(--floor-border, #38bdf8) !important;
}

/* Blueprint Action Cards */
.blueprint-action-card {
  display: flex !important;
  align-items: center !important;
  gap: 12px !important;
  background: linear-gradient(90deg, #101c2e 0%, #070d17 100%) !important;
  border: 2px solid #38bdf8 !important;
  border-radius: 6px !important;
  padding: 10px 14px !important;
  text-decoration: none !important;
  box-shadow: 0 0 16px rgba(56, 189, 248, 0.25) !important;
  transition: all 0.2s ease !important;
  margin-top: 6px !important;
}

.blueprint-action-card:hover {
  background: #182d4a !important;
  border-color: #f1df76 !important;
  box-shadow: 0 0 24px rgba(241, 223, 118, 0.6) !important;
  transform: translateY(-2px) !important;
}

.blueprint-action-card img {
  width: 44px !important;
  height: 44px !important;
  object-fit: contain !important;
}

.blueprint-meta {
  display: flex !important;
  flex-direction: column !important;
}

.blueprint-title {
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 1.05rem !important;
  letter-spacing: 0.08em !important;
  color: #f1df76 !important;
  text-transform: uppercase !important;
}

.blueprint-sub {
  font-family: "Courier New", monospace !important;
  font-size: 0.68rem !important;
  color: #cbd5e1 !important;
}
'''

with open(CSS_PATH, "a", encoding="utf-8") as f:
    f.write("\n" + sidebar_css)

print("Appended Ultimate Sidebar CSS.")

# 2. Build the new rich Right Sidebar HTML for index.html
new_right_rail = '''
    <!-- Right Rail: Ultimate Multi-Scale Console with Mini-Banners, Avatars & Diagnostics -->
    <aside aria-label="Hand of Change Department Console" class="floor-rail">
      <!-- Master Facility Diagnostic Header -->
      <div class="floor-console-header">
        <div class="console-header-top">
          <div class="console-title-wrap">
            <h2>FACILITY 01 // SECTORS</h2>
            <small>THE HAND OF CHANGE SUBTERRANEAN SYSTEM</small>
          </div>
          <img src="assets/icons/hud_facility_radar.svg" alt="Radar" class="console-radar-icon">
        </div>
        <div class="console-status-bar">
          <span><span class="led-dot led-amber"></span> CODE AMBER</span>
          <span>CYCLE: 1,778</span>
          <span>FLUX: 98.4%</span>
        </div>
      </div>

      <!-- Floor 1: Neutral Command -->
      <a class="floor-card-item" href="departments/floor-1-neutral-command.html" style="--floor-border:#ef5b55; --floor-glow:rgba(239,91,85,0.6);">
        <img src="assets/banners/floor_banner_f1_neutral.svg" alt="Floor 1" class="floor-card-banner">
        <div class="floor-card-body">
          <div class="floor-lead-info">
            <img src="assets/avatars/avatar_core_majin.svg" alt="Majin" class="floor-lead-avatar">
            <div class="floor-lead-text">
              <span class="floor-lead-name">MAJIN</span>
              <span class="floor-lead-role">THE DIRECTOR</span>
            </div>
          </div>
          <span class="floor-card-pill">T-05 ALEPH</span>
        </div>
      </a>

      <!-- Floor 2: Maw's Keep -->
      <a class="floor-card-item" href="departments/floor-2-maws-keep.html" style="--floor-border:#5b75e8; --floor-glow:rgba(91,117,232,0.6);">
        <img src="assets/banners/floor_banner_f2_maws_keep.svg" alt="Floor 2" class="floor-card-banner">
        <div class="floor-card-body">
          <div class="floor-lead-info">
            <img src="assets/avatars/avatar_core_dekan.svg" alt="Dekan" class="floor-lead-avatar">
            <div class="floor-lead-text">
              <span class="floor-lead-name">DEKAN</span>
              <span class="floor-lead-role">CONTAINMENT LEAD</span>
            </div>
          </div>
          <span class="floor-card-pill">T-04 WAW</span>
        </div>
      </a>

      <!-- Floor 3: Extraction Hall -->
      <a class="floor-card-item" href="departments/floor-3-extraction-hall.html" style="--floor-border:#e6c843; --floor-glow:rgba(230,200,67,0.6);">
        <img src="assets/banners/floor_banner_f3_extraction.svg" alt="Floor 3" class="floor-card-banner">
        <div class="floor-card-body">
          <div class="floor-lead-info">
            <img src="assets/avatars/avatar_core_zyrak.svg" alt="Zyrak" class="floor-lead-avatar">
            <div class="floor-lead-text">
              <span class="floor-lead-name">ZYRAK</span>
              <span class="floor-lead-role">EXTRACTION LEAD</span>
            </div>
          </div>
          <span class="floor-card-pill">T-04 WAW</span>
        </div>
      </a>

      <!-- Floor 4: Insight Forge -->
      <a class="floor-card-item" href="departments/floor-4-insight-forge.html" style="--floor-border:#47c978; --floor-glow:rgba(71,201,120,0.6);">
        <img src="assets/banners/floor_banner_f4_insight_forge.svg" alt="Floor 4" class="floor-card-banner">
        <div class="floor-card-body">
          <div class="floor-lead-info">
            <img src="assets/avatars/avatar_core_ayshuk.svg" alt="Ayshuk" class="floor-lead-avatar">
            <div class="floor-lead-text">
              <span class="floor-lead-name">AYSHUK</span>
              <span class="floor-lead-role">RESEARCH LEAD</span>
            </div>
          </div>
          <span class="floor-card-pill">T-03 HE</span>
        </div>
      </a>

      <!-- Floor 5: Border Watch -->
      <a class="floor-card-item" href="departments/floor-5-border-watch.html" style="--floor-border:#d4d4d8; --floor-glow:rgba(212,212,216,0.6);">
        <img src="assets/banners/floor_banner_f5_border_watch.svg" alt="Floor 5" class="floor-card-banner">
        <div class="floor-card-body">
          <div class="floor-lead-info">
            <img src="assets/avatars/avatar_core_mellda.svg" alt="Mellda" class="floor-lead-avatar">
            <div class="floor-lead-text">
              <span class="floor-lead-name">MELLDA</span>
              <span class="floor-lead-role">BORDER LEAD</span>
            </div>
          </div>
          <span class="floor-card-pill">T-04 WAW</span>
        </div>
      </a>

      <!-- Floor 6: Deep Vault -->
      <a class="floor-card-item" href="departments/floor-6-deep-vault.html" style="--floor-border:#be123c; --floor-glow:rgba(190,18,60,0.6);">
        <img src="assets/banners/floor_banner_f6_deep_vault.svg" alt="Floor 6" class="floor-card-banner">
        <div class="floor-card-body">
          <div class="floor-lead-info">
            <img src="assets/avatars/avatar_core_marjuk.svg" alt="Marjuk" class="floor-lead-avatar">
            <div class="floor-lead-text">
              <span class="floor-lead-name">MARJUK</span>
              <span class="floor-lead-role">ARCHIVE LEAD</span>
            </div>
          </div>
          <span class="floor-card-pill">T-05 ALEPH</span>
        </div>
      </a>

      <!-- Floor 7: Shadow Corps -->
      <a class="floor-card-item" href="departments/floor-7-shadow-corps.html" style="--floor-border:#f43f5e; --floor-glow:rgba(244,63,94,0.6);">
        <img src="assets/banners/floor_banner_f7_shadow_corps.svg" alt="Floor 7" class="floor-card-banner">
        <div class="floor-card-body">
          <div class="floor-lead-info">
            <img src="assets/avatars/avatar_core_ishall.svg" alt="Ishall" class="floor-lead-avatar">
            <div class="floor-lead-text">
              <span class="floor-lead-name">ISHALL</span>
              <span class="floor-lead-role">THE OUTSIDER</span>
            </div>
          </div>
          <span class="floor-card-pill">T-05 ALEPH</span>
        </div>
      </a>

      <!-- Floor 8: Gate Watch -->
      <a class="floor-card-item" href="departments/floor-8-gate-watch.html" style="--floor-border:#fbbf24; --floor-glow:rgba(251,191,36,0.6);">
        <img src="assets/banners/floor_banner_f8_gate_watch.svg" alt="Floor 8" class="floor-card-banner">
        <div class="floor-card-body">
          <div class="floor-lead-info">
            <img src="assets/avatars/avatar_core_xyan.svg" alt="Xyan" class="floor-lead-avatar">
            <div class="floor-lead-text">
              <span class="floor-lead-name">XYAN</span>
              <span class="floor-lead-role">THE EXILE</span>
            </div>
          </div>
          <span class="floor-card-pill">T-05 ALEPH</span>
        </div>
      </a>

      <!-- Blueprint Cutaways Action Tiles -->
      <a class="blueprint-action-card" href="atlas/hand-of-change-map.html">
        <img src="assets/layout/hand/icons/the_hand_dr_icon_styled.svg" alt="Facility Blueprint">
        <div class="blueprint-meta">
          <span class="blueprint-title">FACILITY CUTAWAY MAP</span>
          <span class="blueprint-sub">EXPLORE ALL 8 SUBTERRANEAN FLOORS</span>
        </div>
      </a>

      <a class="blueprint-action-card" href="atlas/somnarak-city-map.html">
        <img src="assets/layout/city/icons/somnarak_city_icon.svg" alt="City Blueprint">
        <div class="blueprint-meta">
          <span class="blueprint-title">CITY MASTER BLUEPRINT</span>
          <span class="blueprint-sub">METROPOLITAN ZONES A–E &amp; OUTSKIRTS</span>
        </div>
      </a>
    </aside>
'''

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    content = f.read()

content = re.sub(r'<aside[^>]*class=[\'"][^\'"]*floor-rail[^\'"]*[\'"][^>]*>.*?</aside>', new_right_rail, content, flags=re.DOTALL)

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated index.html right rail with Ultimate Multi-Scale Console.")
