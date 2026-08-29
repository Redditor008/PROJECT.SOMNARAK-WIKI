import os

CSS_PATH = "/home/user/01_Somnarak_Wiki/assets/css/wiki.css"

tactical_css = '''
/* ==========================================================================
   ADVANCED TACTICAL HUD, FAST-JUMP BARS, MODAL WINDOWS & BADGES
   ========================================================================== */

/* 1. Fast-Jump Category Pills Bar */
.fast-jump-nav {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 6px;
  background: linear-gradient(90deg, #0d1522 0%, #060a12 100%);
  border: 1.5px solid #22354d;
  border-left: 4px solid #f1df76;
  padding: 8px 14px;
  margin-bottom: 1.2rem;
  border-radius: 4px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.7);
}

.fast-jump-title {
  font-family: Impact, "Arial Narrow Bold", sans-serif;
  font-size: 0.82rem;
  letter-spacing: 0.1em;
  color: #f1df76;
  text-transform: uppercase;
  margin-right: 8px;
  display: flex;
  align-items: center;
  gap: 6px;
}

.fast-jump-pills {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  align-items: center;
}

.jump-pill {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  background: #111a28;
  border: 1px solid #2d425c;
  color: #cbd5e1;
  font-family: "Courier New", monospace;
  font-size: 0.74rem;
  font-weight: bold;
  padding: 3px 8px;
  border-radius: 3px;
  text-decoration: none;
  transition: all 0.18s ease;
  white-space: nowrap;
}

.jump-pill:hover {
  background: #1e3a5f;
  border-color: #38bdf8;
  color: #ffffff;
  box-shadow: 0 0 10px rgba(56, 189, 248, 0.5);
  transform: translateY(-1px);
}

.jump-pill.active {
  background: #2b1f14;
  border-color: #f1df76;
  color: #f1df76;
  box-shadow: 0 0 8px rgba(241, 223, 118, 0.4);
}

/* 2. Tactical HUD Status Bar */
.tactical-hud-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  background: #05080e;
  border: 1px solid #1e293b;
  border-top: 2px solid #ef5b55;
  padding: 6px 14px;
  margin-bottom: 1rem;
  font-family: "Courier New", monospace;
  font-size: 0.72rem;
  color: #94a3b8;
  border-radius: 3px;
}

.hud-item {
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.hud-label {
  color: #64748b;
  font-weight: bold;
}

/* Pulsing LED dots */
.led-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  display: inline-block;
  box-shadow: 0 0 8px currentColor;
}

.led-green { background: #10b981; color: #10b981; animation: pulse-green 2s infinite; }
.led-amber { background: #f59e0b; color: #f59e0b; animation: pulse-amber 2s infinite; }
.led-red { background: #ef4444; color: #ef4444; animation: pulse-red 1.5s infinite; }
.led-cyan { background: #38bdf8; color: #38bdf8; animation: pulse-cyan 2s infinite; }

@keyframes pulse-green {
  0%, 100% { opacity: 1; filter: drop-shadow(0 0 4px #10b981); }
  50% { opacity: 0.4; filter: drop-shadow(0 0 1px #10b981); }
}
@keyframes pulse-amber {
  0%, 100% { opacity: 1; filter: drop-shadow(0 0 4px #f59e0b); }
  50% { opacity: 0.4; filter: drop-shadow(0 0 1px #f59e0b); }
}
@keyframes pulse-red {
  0%, 100% { opacity: 1; filter: drop-shadow(0 0 6px #ef4444); }
  50% { opacity: 0.3; filter: drop-shadow(0 0 1px #ef4444); }
}

/* 3. Tactical Directive Box & Wave Visualizer */
.tactical-directive-box {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: linear-gradient(90deg, #0e1726 0%, #060a10 100%);
  border: 1.5px solid #223854;
  border-left: 4px solid #ef5b55;
  padding: 10px 16px;
  margin: 1.2rem 0;
  border-radius: 4px;
}

.directive-text {
  font-family: "Courier New", monospace;
  font-size: 0.8rem;
  color: #e2e8f0;
}

.directive-text b {
  color: #f1df76;
}

.directive-wave {
  width: 140px;
  height: 32px;
  object-fit: contain;
  opacity: 0.85;
}

/* 4. Tactical Damage Resistance Matrix */
.tactical-resist-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 8px;
  margin: 1.2rem 0;
}

@media (max-width: 768px) {
  .tactical-resist-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

.resist-cell {
  display: flex;
  align-items: center;
  gap: 10px;
  background: #080d16;
  border: 1.5px solid #1e293b;
  padding: 8px 12px;
  border-radius: 4px;
  box-shadow: inset 0 0 8px rgba(0, 0, 0, 0.8);
}

.resist-cell img {
  width: 32px;
  height: 32px;
  object-fit: contain;
}

.resist-meta {
  display: flex;
  flex-direction: column;
}

.resist-name {
  font-family: Impact, "Arial Narrow Bold", sans-serif;
  font-size: 0.85rem;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}

.resist-val {
  font-family: "Courier New", monospace;
  font-size: 0.76rem;
  font-weight: bold;
}

.val-weak { color: #ef4444; }
.val-normal { color: #f1df76; }
.val-resist { color: #10b981; }
.val-immune { color: #38bdf8; }

/* 5. Work Affinity Matrix Box */
.work-affinity-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 8px;
  margin: 1.2rem 0;
}

@media (max-width: 768px) {
  .work-affinity-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

.work-affinity-cell {
  display: flex;
  align-items: center;
  gap: 10px;
  background: #090e18;
  border: 1.5px solid #223246;
  padding: 8px 12px;
  border-radius: 4px;
}

.work-affinity-cell img {
  width: 32px;
  height: 32px;
  object-fit: contain;
}

.work-meta {
  display: flex;
  flex-direction: column;
}

.work-name {
  font-family: Impact, "Arial Narrow Bold", sans-serif;
  font-size: 0.85rem;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: #e2e8f0;
}

.work-rate {
  font-family: "Courier New", monospace;
  font-size: 0.76rem;
  font-weight: bold;
  color: #38bdf8;
}

/* 6. M.A.W. Triad Linkage Box */
.maw-triad-box {
  background: linear-gradient(180deg, #0a111e 0%, #04070e 100%);
  border: 2px solid #2d425c;
  border-top: 3px solid #f1df76;
  padding: 14px 18px;
  margin: 1.8rem 0;
  border-radius: 4px;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.8);
}

.maw-triad-header {
  font-family: Impact, "Arial Narrow Bold", sans-serif;
  font-size: 1.05rem;
  letter-spacing: 0.1em;
  color: #f1df76;
  text-transform: uppercase;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.maw-triad-header:before {
  content: "///";
  color: #ef5b55;
}

.maw-triad-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
}

@media (max-width: 800px) {
  .maw-triad-grid {
    grid-template-columns: 1fr;
  }
}

.triad-card {
  display: flex;
  align-items: center;
  gap: 10px;
  background: #0d1726;
  border: 1.5px solid #243b59;
  padding: 10px 14px;
  border-radius: 4px;
  text-decoration: none;
  transition: all 0.2s ease;
}

.triad-card:hover {
  background: #18283e;
  border-color: #f1df76;
  box-shadow: 0 0 14px rgba(241, 223, 118, 0.4);
  transform: translateY(-2px);
}

.triad-card img {
  width: 42px;
  height: 42px;
  object-fit: contain;
}

.triad-meta {
  display: flex;
  flex-direction: column;
}

.triad-type {
  font-family: "Courier New", monospace;
  font-size: 0.68rem;
  font-weight: bold;
  color: #38bdf8;
  text-transform: uppercase;
}

.triad-name {
  font-family: Impact, "Arial Narrow Bold", sans-serif;
  font-size: 0.95rem;
  color: #f1df76;
  text-transform: uppercase;
}

/* 7. Bottom Canonical Cross-Links Directory */
.cross-reference-section {
  background: linear-gradient(180deg, #090f1a 0%, #03060c 100%);
  border: 2px solid #1e2c3e;
  border-top: 3px solid #38bdf8;
  padding: 18px 20px;
  margin-top: 3rem;
  border-radius: 4px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.85);
}

.cross-ref-header {
  font-family: Impact, "Arial Narrow Bold", sans-serif;
  font-size: 1.15rem;
  letter-spacing: 0.12em;
  color: #38bdf8;
  text-transform: uppercase;
  margin-bottom: 14px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.cross-ref-header:before {
  content: "///";
  color: #ef5b55;
}

.cross-ref-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 12px;
}

.cross-ref-card {
  display: flex;
  align-items: center;
  gap: 12px;
  background: #060b14;
  border: 1.5px solid #1c2a3d;
  padding: 10px 14px;
  border-radius: 4px;
  text-decoration: none;
  transition: all 0.2s ease;
}

.cross-ref-card:hover {
  background: #111e30;
  border-color: #38bdf8;
  box-shadow: 0 0 16px rgba(56, 189, 248, 0.4);
  transform: translateY(-2px);
}

.cross-ref-card img {
  width: 44px;
  height: 44px;
  object-fit: contain;
}

.cross-ref-meta {
  display: flex;
  flex-direction: column;
}

.cross-ref-cat {
  font-family: "Courier New", monospace;
  font-size: 0.68rem;
  font-weight: bold;
  color: #94a3b8;
  text-transform: uppercase;
}

.cross-ref-title {
  font-family: Impact, "Arial Narrow Bold", sans-serif;
  font-size: 0.95rem;
  color: #f1df76;
  text-transform: uppercase;
}

/* 8. Super Hub Card Enhancement */
.hub-grid-3 {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 18px;
  margin: 1.8rem 0;
}

.pm-entity-card {
  background: linear-gradient(180deg, #0c1422 0%, #050810 100%);
  border: 2px solid var(--card-border, #24354c);
  padding: 16px;
  border-radius: 4px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.85);
  transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
}

.pm-entity-card:hover {
  transform: translateY(-4px);
  border-color: #f1df76;
  box-shadow: 0 0 22px rgba(241, 223, 118, 0.45);
}

.entity-card-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;
}

.entity-card-icon {
  width: 64px;
  height: 64px;
  object-fit: contain;
  filter: drop-shadow(0 0 8px rgba(241, 223, 118, 0.3));
}

.entity-card-meta {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 4px;
}

.entity-card-name {
  font-family: Impact, "Arial Narrow Bold", sans-serif;
  font-size: 1.15rem;
  letter-spacing: 0.06em;
  color: #f1df76;
  margin: 0 0 8px 0;
  text-transform: uppercase;
}

.entity-card-desc {
  font-family: "Segoe UI", system-ui, sans-serif;
  font-size: 0.88rem;
  line-height: 1.45;
  color: #cbd5e1;
  margin: 0 0 12px 0;
  flex-grow: 1;
}

.entity-card-stats {
  display: flex;
  justify-content: space-between;
  background: #060a12;
  border: 1px solid #1c2a3d;
  padding: 6px 10px;
  margin-bottom: 12px;
  border-radius: 3px;
  font-family: "Courier New", monospace;
  font-size: 0.72rem;
  color: #94a3b8;
}

.jump-btn {
  display: block;
  text-align: center;
  background: linear-gradient(90deg, #18283e 0%, #0d1726 100%);
  border: 1.5px solid #38bdf8;
  color: #38bdf8;
  font-family: Impact, "Arial Narrow Bold", sans-serif;
  font-size: 0.95rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 8px 12px;
  border-radius: 3px;
  text-decoration: none;
  transition: all 0.2s ease;
}

.jump-btn:hover {
  background: #38bdf8;
  color: #040810;
  box-shadow: 0 0 14px rgba(56, 189, 248, 0.7);
}

.sub-category-header {
  font-family: Impact, "Arial Narrow Bold", sans-serif;
  font-size: 1.35rem;
  letter-spacing: 0.12em;
  color: #f1df76;
  text-transform: uppercase;
  border-bottom: 2px solid #ef5b55;
  padding-bottom: 6px;
  margin: 2.2rem 0 1.2rem 0;
}
'''

with open(CSS_PATH, "a", encoding="utf-8") as f:
    f.write("\n" + tactical_css)

print("Appended Tactical CSS Styles.")
