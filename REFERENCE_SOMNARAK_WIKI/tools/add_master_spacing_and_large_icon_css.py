import os

css_overhaul = """
/* ==========================================================================
   MASTER SPACING, LARGE ICON PROMINENCE & ZERO BORDER COLLISION OVERHAUL
   ========================================================================== */

/* 1. MASTER HUB CARDS (Homepage & Portals) */
.master-hub-grid {
  display: grid !important;
  grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)) !important;
  gap: 1.6rem !important;
  margin: 2rem 0 3rem 0 !important;
  width: 100% !important;
  box-sizing: border-box !important;
}

.master-hub-card {
  position: relative !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: space-between !important;
  background: linear-gradient(145deg, #0a101d 0%, #04060c 100%) !important;
  border: 2px solid #223854 !important;
  border-radius: 8px !important;
  padding: 1.6rem !important;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.8) !important;
  transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.25s ease, box-shadow 0.25s ease !important;
  box-sizing: border-box !important;
}

.master-hub-card:hover {
  transform: translateY(-5px) !important;
}

/* Hub Card Header with Generous Chip Spacing */
.hub-card-header {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  padding: 0 0 14px 0 !important;
  border-bottom: 1.5px solid rgba(255, 255, 255, 0.14) !important;
  margin-bottom: 16px !important;
  gap: 12px !important;
}

.hub-card-badge {
  display: inline-flex !important;
  align-items: center !important;
  font-family: 'Courier New', monospace !important;
  font-size: 0.78rem !important;
  font-weight: 800 !important;
  letter-spacing: 0.12em !important;
  padding: 5px 12px !important;
  border-radius: 4px !important;
  background: rgba(15, 23, 42, 0.95) !important;
  color: #38bdf8 !important;
  border: 1.5px solid #224268 !important;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.7) !important;
  white-space: nowrap !important;
}

.hub-card-counter {
  display: inline-flex !important;
  align-items: center !important;
  font-family: 'JetBrains Mono', 'Courier New', monospace !important;
  font-size: 0.82rem !important;
  font-weight: 800 !important;
  letter-spacing: 0.1em !important;
  color: #f1df76 !important;
  background: #141207 !important;
  padding: 5px 14px !important;
  border: 1.5px solid #ca8a04 !important;
  border-radius: 4px !important;
  box-shadow: 0 0 12px rgba(241, 223, 118, 0.3) !important;
  white-space: nowrap !important;
  margin-left: auto !important;
}

/* Hub Card Body with Large Prominent 112px Icon */
.hub-card-body {
  display: flex !important;
  align-items: center !important;
  gap: 20px !important;
  margin: 10px 0 18px 0 !important;
}

.hub-card-icon {
  width: 112px !important;
  height: 112px !important;
  min-width: 112px !important;
  max-width: 112px !important;
  padding: 8px !important;
  background: radial-gradient(circle at 50% 50%, rgba(255, 255, 255, 0.08) 0%, rgba(4, 7, 12, 0.98) 100%) !important;
  border: 2px solid currentColor !important;
  border-radius: 10px !important;
  filter: drop-shadow(0 4px 14px rgba(0, 0, 0, 0.9)) !important;
  object-fit: contain !important;
  transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), filter 0.25s ease !important;
  box-sizing: border-box !important;
}

.hub-entities .hub-card-icon { color: #ef5b55 !important; }
.hub-maw .hub-card-icon { color: #f1df76 !important; }
.hub-characters .hub-card-icon { color: #c084fc !important; }
.hub-mechanics .hub-card-icon { color: #38bdf8 !important; }
.hub-factions .hub-card-icon { color: #eab308 !important; }
.hub-departments .hub-card-icon { color: #71efaf !important; }
.hub-locations .hub-card-icon { color: #fb923c !important; }
.hub-lore .hub-card-icon { color: #818cf8 !important; }

.master-hub-card:hover .hub-card-icon {
  transform: scale(1.08) !important;
  filter: drop-shadow(0 0 16px currentColor) !important;
}

.hub-card-info {
  flex: 1 !important;
  min-width: 0 !important;
}

.hub-card-title {
  margin: 0 0 6px 0 !important;
  font-family: Impact, 'Arial Narrow Bold', sans-serif !important;
  font-size: 1.35rem !important;
  letter-spacing: 0.08em !important;
  line-height: 1.25 !important;
}

.hub-card-title a {
  color: #ffffff !important;
  text-decoration: none !important;
  transition: color 0.15s ease !important;
}

.hub-card-sub {
  display: block !important;
  font-size: 0.82rem !important;
  color: #94a3b8 !important;
  font-weight: 700 !important;
  margin-bottom: 8px !important;
  letter-spacing: 0.05em !important;
}

.hub-card-desc {
  margin: 0 !important;
  font-size: 0.86rem !important;
  color: #cbd5e1 !important;
  line-height: 1.5 !important;
}

/* Hub Card Footer with Spacious CTA Button & Quick Chips */
.hub-card-footer {
  display: flex !important;
  flex-direction: column !important;
  gap: 12px !important;
  margin-top: auto !important;
  padding-top: 14px !important;
  border-top: 1.5px solid rgba(255, 255, 255, 0.08) !important;
}

.hub-enter-btn {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  padding: 12px 20px !important;
  border-radius: 4px !important;
  font-family: Impact, 'Arial Narrow Bold', sans-serif !important;
  font-size: 0.98rem !important;
  letter-spacing: 0.1em !important;
  text-decoration: none !important;
  text-transform: uppercase !important;
  background: #0d1624 !important;
  border: 1.8px solid currentColor !important;
  transition: all 0.2s ease !important;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.6) !important;
}

.hub-card-links {
  display: flex !important;
  flex-wrap: wrap !important;
  gap: 8px !important;
}

.hub-card-links a {
  font-family: 'JetBrains Mono', 'Courier New', monospace !important;
  font-size: 0.78rem !important;
  font-weight: 700 !important;
  color: #94a3b8 !important;
  background: rgba(15, 23, 42, 0.95) !important;
  border: 1.5px solid #223854 !important;
  padding: 5px 12px !important;
  border-radius: 4px !important;
  text-decoration: none !important;
  transition: all 0.15s ease !important;
}

.hub-card-links a:hover {
  background: #1e3a5f !important;
  color: #ffffff !important;
  border-color: #38bdf8 !important;
  box-shadow: 0 0 8px rgba(56, 189, 248, 0.5) !important;
}


/* 2. ALL ENTITY & CODEX CARDS (112px ICONS & ZERO-TOUCH SPACING) */
.pm-entity-card .entity-card-icon,
.entity-card-icon,
.dept-card-icon,
.char-icon,
.mech-icon,
.faction-icon,
.loc-icon,
.lore-icon {
  width: 112px !important;
  height: 112px !important;
  min-width: 112px !important;
  max-width: 112px !important;
  padding: 8px !important;
  background: radial-gradient(circle at 50% 50%, rgba(255, 255, 255, 0.08) 0%, rgba(4, 7, 12, 0.98) 100%) !important;
  border: 2px solid currentColor !important;
  border-radius: 10px !important;
  filter: drop-shadow(0 4px 14px rgba(0, 0, 0, 0.9)) !important;
  object-fit: contain !important;
  box-sizing: border-box !important;
}

.entity-card-top {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  margin-bottom: 16px !important;
  gap: 14px !important;
}

.entity-card-meta {
  display: flex !important;
  flex-direction: column !important;
  gap: 8px !important;
  align-items: flex-end !important;
}

.entity-card-name {
  font-family: Impact, 'Arial Narrow Bold', sans-serif !important;
  font-size: 1.35rem !important;
  letter-spacing: 0.08em !important;
  margin: 0 0 8px 0 !important;
  line-height: 1.25 !important;
}

.entity-card-desc {
  font-size: 0.86rem !important;
  line-height: 1.5 !important;
  color: #cbd5e1 !important;
  margin: 0 0 16px 0 !important;
}


/* 3. RIGHT SIDEBAR BLUEPRINT WIDGETS (PROMINENT 76px FRAMES) */
.blueprint-card-widget {
  display: flex !important;
  align-items: center !important;
  gap: 16px !important;
  background: linear-gradient(135deg, #0e1929 0%, #050812 100%) !important;
  border: 2px solid #223c5e !important;
  border-left: 5px solid #38bdf8 !important;
  border-radius: 8px !important;
  padding: 12px 16px !important;
  text-decoration: none !important;
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.8) !important;
  transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1) !important;
  box-sizing: border-box !important;
}

.blueprint-card-widget:nth-child(2) {
  border-left-color: #c084fc !important;
}

.blueprint-card-widget:hover {
  transform: translateY(-3px) !important;
  background: linear-gradient(135deg, #182a44 0%, #0a1122 100%) !important;
  border-color: #f1df76 !important;
  box-shadow: 0 0 24px rgba(241, 223, 118, 0.5) !important;
}

.blueprint-thumb-box {
  width: 76px !important;
  height: 76px !important;
  min-width: 76px !important;
  max-width: 76px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  background: #020408 !important;
  border: 1.8px solid #223854 !important;
  border-radius: 8px !important;
  padding: 4px !important;
  box-sizing: border-box !important;
}

.blueprint-thumb-img {
  width: 100% !important;
  height: 100% !important;
  object-fit: contain !important;
  filter: drop-shadow(0 0 10px rgba(56, 189, 248, 0.6)) !important;
  transition: transform 0.2s ease !important;
}

.blueprint-card-widget:nth-child(2) .blueprint-thumb-img {
  filter: drop-shadow(0 0 10px rgba(192, 132, 252, 0.6)) !important;
}

.blueprint-card-widget:hover .blueprint-thumb-img {
  transform: scale(1.1) !important;
}

.blueprint-widget-meta .widget-title {
  font-family: Impact, 'Arial Narrow Bold', sans-serif !important;
  font-size: 1.05rem !important;
  letter-spacing: 0.08em !important;
  color: #f1df76 !important;
  text-transform: uppercase !important;
  line-height: 1.25 !important;
  margin-bottom: 4px !important;
}

.blueprint-widget-meta .widget-sub {
  font-family: 'Courier New', monospace !important;
  font-size: 0.76rem !important;
  font-weight: 700 !important;
  color: #94a3b8 !important;
  line-height: 1.35 !important;
}


/* 4. ALL BADGES & CHIPS ACROSS WIKI (GENEROUS PADDING, ZERO TOUCHING) */
.risk-badge,
.damage-badge,
.han-badge,
.disp-tag,
.risk-tag,
.badge,
.status-pill,
.work-badge,
.dmg-badge {
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  padding: 5px 12px !important;
  margin: 3px 4px !important;
  line-height: 1.3 !important;
  border-radius: 4px !important;
  font-weight: 800 !important;
  box-sizing: border-box !important;
  white-space: nowrap !important;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.6) !important;
}

.spotlight-badges {
  display: flex !important;
  flex-wrap: wrap !important;
  gap: 8px !important;
  margin-top: 12px !important;
}

.dispatch-item {
  display: flex !important;
  align-items: flex-start !important;
  gap: 12px !important;
  padding: 8px 12px !important;
  margin-bottom: 8px !important;
  background: rgba(10, 16, 28, 0.7) !important;
  border-left: 3px solid #38bdf8 !important;
  border-radius: 4px !important;
}

.dispatch-item:last-child {
  margin-bottom: 0 !important;
}
"""

with open('/home/user/01_Somnarak_Wiki/assets/css/wiki.css', 'a', encoding='utf-8') as f:
    f.write('\n' + css_overhaul.strip() + '\n')

print('SUCCESS: Master spacing and prominent 112px icon CSS appended!')
