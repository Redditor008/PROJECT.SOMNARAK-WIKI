import os, re

CSS_PATH = "/home/user/01_Somnarak_Wiki/assets/css/wiki.css"
INDEX_PATH = "/home/user/01_Somnarak_Wiki/index.html"

# 1. Append the ultimate L-Corp Right Rail CSS
lcorp_ultimate_css = '''
/* ==========================================================================
   ULTIMATE L-CORP RIGHT SIDEBAR STYLING (380px WIDE, 72px TALL BUTTONS)
   ========================================================================== */

.wiki-shell.home-shell {
  width: min(1720px, 98vw) !important;
  grid-template-columns: 220px minmax(0, 1fr) 380px !important;
}

@media (max-width: 1300px) {
  .wiki-shell.home-shell {
    grid-template-columns: 200px minmax(0, 1fr) 340px !important;
  }
}

@media (max-width: 1024px) {
  .wiki-shell.home-shell {
    grid-template-columns: 1fr !important;
  }
}

/* Master Floor Rail Container */
.floor-rail {
  display: flex !important;
  flex-direction: column !important;
  background: linear-gradient(180deg, #090e18 0%, #03050a 100%) !important;
  border-left: 3px solid #331d22 !important;
  padding: 1.8rem 1.2rem !important;
  box-shadow: inset 10px 0 30px rgba(0, 0, 0, 0.95) !important;
  width: 100% !important;
  box-sizing: border-box !important;
}

/* Industrial Header Banner */
.floor-rail-header {
  background: linear-gradient(90deg, #1a080c 0%, #2b0c14 50%, #1a080c 100%) !important;
  border: 2px solid #ef5b55 !important;
  padding: 12px 14px !important;
  margin-bottom: 1.4rem !important;
  text-align: center !important;
  border-radius: 4px !important;
  box-shadow: 0 0 16px rgba(239, 91, 85, 0.35) !important;
  position: relative !important;
}

.floor-rail-header h2 {
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 1.55rem !important;
  letter-spacing: 0.14em !important;
  color: #f1df76 !important;
  text-transform: uppercase !important;
  margin: 0 !important;
  text-shadow: 0 0 12px rgba(241, 223, 118, 0.6) !important;
}

.floor-rail-header small {
  font-family: "Courier New", monospace !important;
  font-size: 0.72rem !important;
  letter-spacing: 0.16em !important;
  color: #38bdf8 !important;
  display: block !important;
  margin-top: 4px !important;
  font-weight: bold !important;
  text-transform: uppercase !important;
}

/* Authentic L-Corp 72px Tall Hazard Buttons */
.pm-hazard-btn {
  position: relative !important;
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  min-height: 72px !important;
  margin: 9px 0 !important;
  padding: 8px 14px 8px 56px !important;
  border: 2.5px solid var(--floor-color, #f1df76) !important;
  background: linear-gradient(90deg, rgba(14, 20, 32, 0.98) 0%, rgba(6, 9, 16, 0.98) 100%) !important;
  text-decoration: none !important;
  border-radius: 4px !important;
  overflow: hidden !important;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.8), inset 0 0 10px rgba(0, 0, 0, 0.6) !important;
  transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

/* Thick 46px Diagonal Yellow/Black Hazard Stripe on Left */
.pm-hazard-btn:before {
  content: "" !important;
  position: absolute !important;
  left: 0 !important;
  top: 0 !important;
  bottom: 0 !important;
  width: 46px !important;
  background: repeating-linear-gradient(
    -45deg,
    #f1df76,
    #f1df76 8px,
    #05070a 8px,
    #05070a 16px
  ) !important;
  border-right: 2.5px solid var(--floor-color, #f1df76) !important;
  box-shadow: 2px 0 8px rgba(0, 0, 0, 0.8) !important;
}

.pm-hazard-btn:hover {
  transform: translateX(8px) !important;
  border-color: #ffffff !important;
  background: linear-gradient(90deg, rgba(28, 42, 65, 0.98) 0%, rgba(14, 22, 34, 0.98) 100%) !important;
  box-shadow: 0 0 24px var(--floor-color, rgba(241, 223, 118, 0.7)), inset 0 0 15px var(--floor-color, rgba(241, 223, 118, 0.4)) !important;
}

.pm-hazard-btn-text {
  display: flex !important;
  flex-direction: column !important;
  z-index: 2 !important;
  margin-left: 6px !important;
}

.pm-hazard-btn-text small {
  font-family: "Courier New", monospace !important;
  font-size: 0.72rem !important;
  letter-spacing: 0.12em !important;
  color: #94a3b8 !important;
  text-transform: uppercase !important;
  line-height: 1 !important;
  margin-bottom: 4px !important;
  font-weight: bold !important;
}

.pm-hazard-btn-text b {
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 1.18rem !important;
  letter-spacing: 0.06em !important;
  color: var(--floor-color, #f1df76) !important;
  text-transform: uppercase !important;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.95) !important;
  line-height: 1.15 !important;
}

/* Large 52px Prominent Department Badges */
.pm-hazard-btn img {
  width: 52px !important;
  height: 52px !important;
  min-width: 52px !important;
  max-width: 52px !important;
  object-fit: contain !important;
  filter: drop-shadow(0 0 10px var(--floor-color, rgba(241, 223, 118, 0.6))) !important;
  transition: transform 0.22s cubic-bezier(0.16, 1, 0.3, 1) !important;
  z-index: 2 !important;
}

.pm-hazard-btn:hover img {
  transform: scale(1.2) rotate(4deg) !important;
}

/* 64px Tall Action Buttons */
.pm-action-btn {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  min-height: 64px !important;
  padding: 10px 16px 10px 56px !important;
  margin: 14px 0 !important;
  border: 2.5px solid #f1df76 !important;
  background: linear-gradient(90deg, #182236 0%, #0a101c 100%) !important;
  color: #ffffff !important;
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 1.08rem !important;
  letter-spacing: 0.1em !important;
  text-transform: uppercase !important;
  position: relative !important;
  text-decoration: none !important;
  border-radius: 4px !important;
  box-shadow: 0 0 18px rgba(241, 223, 118, 0.3) !important;
  transition: all 0.22s ease !important;
}

.pm-action-btn:before {
  content: "" !important;
  position: absolute !important;
  left: 0 !important;
  top: 0 !important;
  bottom: 0 !important;
  width: 46px !important;
  background: repeating-linear-gradient(
    -45deg,
    #ef5b55,
    #ef5b55 8px,
    #05070a 8px,
    #05070a 16px
  ) !important;
  border-right: 2.5px solid #f1df76 !important;
}

.pm-action-btn:hover {
  background: #243352 !important;
  border-color: #ffffff !important;
  box-shadow: 0 0 26px rgba(241, 223, 118, 0.7) !important;
  transform: translateY(-3px) !important;
}

.pm-action-btn img {
  width: 38px !important;
  height: 38px !important;
  min-width: 38px !important;
  object-fit: contain !important;
}

/* Sister Projects Framed Cards */
.pm-related-section {
  margin-top: 2rem !important;
  border-top: 2px solid #2d181d !important;
  padding-top: 1.4rem !important;
}

.pm-related-section h3 {
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 1rem !important;
  letter-spacing: 0.14em !important;
  color: #38bdf8 !important;
  text-transform: uppercase !important;
  margin: 0 0 14px !important;
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
  margin-bottom: 14px !important;
  text-decoration: none !important;
  border-radius: 4px !important;
  overflow: hidden !important;
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.8) !important;
  transition: all 0.22s ease !important;
}

.pm-related-card:hover {
  border-color: #f1df76 !important;
  box-shadow: 0 0 20px rgba(241, 223, 118, 0.5) !important;
  transform: translateY(-3px) !important;
}

.pm-related-card img {
  width: 100% !important;
  height: 125px !important;
  object-fit: cover !important;
  border-bottom: 2px solid #1e293b !important;
  display: block !important;
}

.pm-related-card span {
  display: block !important;
  padding: 10px 14px !important;
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 0.92rem !important;
  letter-spacing: 0.08em !important;
  color: #f1df76 !important;
  text-transform: uppercase !important;
  background: #090e18 !important;
}
'''

with open(CSS_PATH, "a", encoding="utf-8") as f:
    f.write("\n" + lcorp_ultimate_css)

print("Appended Ultimate L-Corp CSS.")

# 2. Update index.html right rail with rich department details
index_right_rail_html = '''
    <!-- Right Rail: Authentic L-Corp Hazard Chevron Department Buttons -->
    <aside aria-label="Hand of Change departments" class="floor-rail">
      <div class="floor-rail-header">
        <h2>/// HAND OF CHANGE ///</h2>
        <small>REVERIE DIRECTORATE FACILITY</small>
      </div>

      <!-- Floor 1: Neutral Command -->
      <a class="pm-hazard-btn" href="departments/floor-1-neutral-command.html" style="--floor-color:#ef5b55">
        <div class="pm-hazard-btn-text">
          <small>[ SECTOR 01 // PALM CORE ]</small>
          <b>NEUTRAL COMMAND</b>
        </div>
        <img src="assets/layout/hand/icons/icon_dept_f1_neutral.svg" alt="Floor 1 Badge">
      </a>

      <!-- Floor 2: Maw's Keep -->
      <a class="pm-hazard-btn" href="departments/floor-2-maws-keep.html" style="--floor-color:#5b75e8">
        <div class="pm-hazard-btn-text">
          <small>[ SECTOR 02 // WARD KEEP ]</small>
          <b>MAW’S KEEP</b>
        </div>
        <img src="assets/layout/hand/icons/icon_dept_f2_maws_keep.svg" alt="Floor 2 Badge">
      </a>

      <!-- Floor 3: Extraction Hall -->
      <a class="pm-hazard-btn" href="departments/floor-3-extraction-hall.html" style="--floor-color:#e6c843">
        <div class="pm-hazard-btn-text">
          <small>[ SECTOR 03 // SIPHON FORGE ]</small>
          <b>EXTRACTION HALL</b>
        </div>
        <img src="assets/layout/hand/icons/icon_dept_f3_extraction.svg" alt="Floor 3 Badge">
      </a>

      <!-- Floor 4: Insight Forge -->
      <a class="pm-hazard-btn" href="departments/floor-4-insight-forge.html" style="--floor-color:#47c978">
        <div class="pm-hazard-btn-text">
          <small>[ SECTOR 04 // RESEARCH CORE ]</small>
          <b>INSIGHT FORGE</b>
        </div>
        <img src="assets/layout/hand/icons/icon_dept_f4_insight_forge.svg" alt="Floor 4 Badge">
      </a>

      <!-- Floor 5: Border Watch -->
      <a class="pm-hazard-btn" href="departments/floor-5-border-watch.html" style="--floor-color:#d4d4d8">
        <div class="pm-hazard-btn-text">
          <small>[ SECTOR 05 // BORDER BASTION ]</small>
          <b>BORDER WATCH</b>
        </div>
        <img src="assets/layout/hand/icons/icon_dept_f5_border_watch.svg" alt="Floor 5 Badge">
      </a>

      <!-- Floor 6: Deep Vault -->
      <a class="pm-hazard-btn" href="departments/floor-6-deep-vault.html" style="--floor-color:#be123c">
        <div class="pm-hazard-btn-text">
          <small>[ SECTOR 06 // CRYO ARCHIVE ]</small>
          <b>DEEP VAULT</b>
        </div>
        <img src="assets/layout/hand/icons/icon_dept_f6_deep_vault.svg" alt="Floor 6 Badge">
      </a>

      <!-- Floor 7: Shadow Corps -->
      <a class="pm-hazard-btn" href="departments/floor-7-shadow-corps.html" style="--floor-color:#f43f5e">
        <div class="pm-hazard-btn-text">
          <small>[ SECTOR 07 // VOID DIVERS ]</small>
          <b>SHADOW CORPS</b>
        </div>
        <img src="assets/layout/hand/icons/icon_dept_f7_shadow_corps.svg" alt="Floor 7 Badge">
      </a>

      <!-- Floor 8: Gate Watch -->
      <a class="pm-hazard-btn" href="departments/floor-8-gate-watch.html" style="--floor-color:#fbbf24">
        <div class="pm-hazard-btn-text">
          <small>[ SECTOR 08 // TABOO GATE ]</small>
          <b>GATE WATCH</b>
        </div>
        <img src="assets/layout/hand/icons/icon_dept_f8_gate_watch.svg" alt="Floor 8 Badge">
      </a>

      <!-- Action Buttons -->
      <a class="pm-action-btn" href="atlas/hand-of-change-map.html">
        FACILITY CUTAWAY MAP
        <img src="assets/layout/hand/icons/the_hand_dr_icon_styled.svg" alt="">
      </a>
      <a class="pm-action-btn" href="atlas/somnarak-city-map.html">
        CITY MASTER BLUEPRINT
        <img src="assets/layout/city/icons/somnarak_city_icon.svg" alt="">
      </a>

      <!-- Related Directories -->
      <div class="pm-related-section">
        <h3>RELATED DIRECTORIES</h3>
        <a class="pm-related-card" href="departments/index.html">
          <img src="assets/layout/hand/blueprints/THE_HAND_DR_LAYOUT.png" alt="The Hand of Change">
          <span>THE HAND OF CHANGE DIRECTORY</span>
        </a>
        <a class="pm-related-card" href="locations/index.html">
          <img src="assets/layout/city/blueprints/SOMNARAK_CITY_LAYOUT.png" alt="Somnarak City Atlas">
          <span>SOMNARAK URBAN ATLAS</span>
        </a>
      </div>
    </aside>
'''

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    index_content = f.read()

index_content = re.sub(r'<aside[^>]*class=[\'"][^\'"]*floor-rail[^\'"]*[\'"][^>]*>.*?</aside>', index_right_rail_html, index_content, flags=re.DOTALL)

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(index_content)

print("Updated index.html right rail successfully.")
