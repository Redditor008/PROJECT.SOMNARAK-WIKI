import os

css_blueprint = """
/* ==========================================================================
   ENRICHED BLUEPRINT CARDS FOR RIGHT RAIL (THE HAND & SOMNARAK CITY)
   ========================================================================== */
.blueprint-quick-panels {
  display: flex !important;
  flex-direction: column !important;
  gap: 12px !important;
  margin-top: 14px !important;
}

.blueprint-card-widget {
  display: flex !important;
  align-items: center !important;
  gap: 14px !important;
  background: linear-gradient(135deg, #0d1726 0%, #050810 100%) !important;
  border: 1.5px solid #223854 !important;
  border-left: 4px solid #38bdf8 !important;
  border-radius: 6px !important;
  padding: 10px 12px !important;
  text-decoration: none !important;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.7) !important;
  transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

.blueprint-card-widget:nth-child(2) {
  border-left-color: #c084fc !important;
}

.blueprint-card-widget:hover {
  transform: translateY(-2px) !important;
  background: linear-gradient(135deg, #16243b 0%, #0a101f 100%) !important;
  border-color: #f1df76 !important;
  box-shadow: 0 0 20px rgba(241, 223, 118, 0.45) !important;
}

.blueprint-thumb-box {
  width: 58px !important;
  height: 58px !important;
  min-width: 58px !important;
  max-width: 58px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  background: #020408 !important;
  border: 1px solid #1e293b !important;
  border-radius: 4px !important;
  padding: 3px !important;
  box-sizing: border-box !important;
}

.blueprint-thumb-img {
  width: 100% !important;
  height: 100% !important;
  object-fit: contain !important;
  filter: drop-shadow(0 0 6px rgba(56, 189, 248, 0.5)) !important;
  transition: transform 0.2s ease !important;
}

.blueprint-card-widget:nth-child(2) .blueprint-thumb-img {
  filter: drop-shadow(0 0 6px rgba(192, 132, 252, 0.5)) !important;
}

.blueprint-card-widget:hover .blueprint-thumb-img {
  transform: scale(1.08) !important;
}

.blueprint-widget-meta {
  display: flex !important;
  flex-direction: column !important;
  gap: 2px !important;
  min-width: 0 !important;
  flex: 1 !important;
}

.blueprint-widget-meta .widget-title {
  font-family: Impact, "Arial Narrow Bold", sans-serif !important;
  font-size: 0.96rem !important;
  letter-spacing: 0.08em !important;
  color: #f1df76 !important;
  text-transform: uppercase !important;
  line-height: 1.2 !important;
}

.blueprint-card-widget:hover .widget-title {
  color: #ffffff !important;
}

.blueprint-widget-meta .widget-sub {
  font-family: "Courier New", monospace !important;
  font-size: 0.72rem !important;
  font-weight: 600 !important;
  color: #94a3b8 !important;
  line-height: 1.3 !important;
}
"""

with open('/home/user/01_Somnarak_Wiki/assets/css/wiki.css', 'a', encoding='utf-8') as f:
    f.write('\n' + css_blueprint.strip() + '\n')

print('SUCCESS: Appended enriched blueprint widget CSS!')
