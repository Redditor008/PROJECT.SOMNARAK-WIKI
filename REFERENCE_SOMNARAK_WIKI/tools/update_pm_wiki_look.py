import re

css_additions = """
/* ==========================================================================
   PROJECT MOON / WIKI.GG AUTHENTIC PORTAL LAYOUT
   ========================================================================== */

.pm-hero-container {
  display: flex;
  flex-direction: column;
  margin-bottom: 24px;
  border: 1px solid #331518;
  background: radial-gradient(circle at 65% 35%, #2a0e14 0%, #050608 65%);
  position: relative;
  overflow: hidden;
}

.pm-hero-main {
  display: grid;
  grid-template-columns: minmax(0, 1.25fr) minmax(240px, 0.75fr);
  min-height: 280px;
  padding: 24px 28px 12px 34px;
  align-items: center;
}

.pm-hero-left {
  display: flex;
  flex-direction: column;
  justify-content: center;
  z-index: 2;
}

.pm-brand-row {
  display: flex;
  align-items: center;
  gap: 20px;
}

.pm-brand-row img {
  width: 90px;
  height: 90px;
  filter: drop-shadow(0 0 12px rgba(239, 91, 85, 0.4));
}

.pm-brand-text h1 {
  font: clamp(2.8rem, 4.8vw, 4.4rem)/0.88 Impact, "Arial Narrow Bold", sans-serif;
  letter-spacing: 0.03em;
  color: #fff;
  margin: 0;
  text-transform: uppercase;
}

.pm-brand-text h1 span {
  color: #f1df76;
}

.pm-brand-text strong {
  display: block;
  font: 1.1rem Impact, "Arial Narrow Bold", sans-serif;
  letter-spacing: 0.28em;
  color: #ef5b55;
  margin-top: 6px;
}

.pm-hero-subtext {
  margin-top: 14px;
  font-size: 0.95rem;
  color: #c4c0a5;
  max-width: 540px;
  line-height: 1.45;
}

.pm-hero-right {
  display: flex;
  justify-content: center;
  align-items: flex-end;
  z-index: 2;
  height: 100%;
}

.pm-hero-standee {
  max-height: 290px;
  width: auto;
  filter: drop-shadow(0 4px 16px rgba(0,0,0,0.85));
  transition: transform 0.3s ease;
}

.pm-hero-standee:hover {
  transform: scale(1.02);
}

.pm-slogan-bar {
  background: linear-gradient(90deg, #8d2e42 0%, #ef5b55 50%, #8d2e42 100%);
  color: #fff;
  text-align: center;
  padding: 12px 20px;
  font: 1.35rem Impact, "Arial Narrow Bold", sans-serif;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  border-top: 1px solid #ff7b75;
  border-bottom: 1px solid #4a151b;
  box-shadow: 0 4px 12px rgba(0,0,0,0.5);
  z-index: 3;
}

.pm-slogan-bar span {
  display: inline-block;
  margin-left: 12px;
  font-family: 'Segoe UI', Arial, sans-serif;
  font-size: 0.85rem;
  letter-spacing: 0.06em;
  color: #ffd2d0;
  vertical-align: middle;
}

/* Chamfered Containment Box */
.pm-intro-chamfer {
  position: relative;
  background: #06080b;
  border: 2px solid #d97706;
  clip-path: polygon(18px 0%, 100% 0%, 100% calc(100% - 18px), calc(100% - 18px) 100%, 0% 100%, 0% 18px);
  padding: 24px 30px;
  margin-bottom: 32px;
  box-shadow: inset 0 0 20px rgba(217, 119, 6, 0.08);
}

.pm-intro-chamfer p {
  font-style: italic;
  font-size: 0.98rem;
  line-height: 1.65;
  color: #e5e2cc;
  margin: 0 0 12px;
}

.pm-intro-chamfer p:last-child {
  margin-bottom: 0;
  font-style: normal;
  color: #f1df76;
  font-weight: 500;
  font-size: 0.92rem;
  border-top: 1px dashed rgba(217, 119, 6, 0.4);
  padding-top: 10px;
}

/* 2x4 Project Moon Neon Feature Grid */
.pm-feature-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  margin-bottom: 36px;
}

.pm-card {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 160px;
  padding: 24px 12px 16px;
  border: 2px solid #4ade80;
  background: #040608;
  color: #4ade80;
  text-decoration: none;
  transition: all 0.2s ease;
}

.pm-card.gold {
  border-color: #f1df76;
  color: #f1df76;
}

.pm-card.crimson {
  border-color: #ef5b55;
  color: #ef5b55;
}

.pm-card.cyan {
  border-color: #38bdf8;
  color: #38bdf8;
}

.pm-card:hover {
  background: #09120e;
  box-shadow: 0 0 16px rgba(74, 222, 128, 0.25);
  transform: translateY(-2px);
}

.pm-card.gold:hover {
  background: #141207;
  box-shadow: 0 0 16px rgba(241, 223, 118, 0.25);
}

.pm-card.crimson:hover {
  background: #170709;
  box-shadow: 0 0 16px rgba(239, 91, 85, 0.25);
}

.pm-card.cyan:hover {
  background: #06111a;
  box-shadow: 0 0 16px rgba(56, 189, 248, 0.25);
}

.pm-card-title {
  position: absolute;
  top: -10px;
  background: #000;
  padding: 0 10px;
  font: 0.82rem Impact, "Arial Narrow Bold", sans-serif;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  white-space: nowrap;
}

.pm-card-icon {
  width: 76px;
  height: 76px;
  object-fit: contain;
  margin: 6px 0 8px;
  filter: drop-shadow(0 2px 6px rgba(0,0,0,0.7));
}

.pm-card-sub {
  font-size: 0.72rem;
  color: #aaa;
  text-align: center;
  line-height: 1.2;
}

/* Hazard Chevron Department Buttons in Right Rail */
.pm-hazard-btn {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 52px;
  margin: 7px 0;
  padding: 6px 12px 6px 44px;
  border: 2px solid var(--floor-color, #f1df76);
  background: #050608;
  text-decoration: none;
  overflow: hidden;
  transition: all 0.2s ease;
}

.pm-hazard-btn:before {
  content: "";
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 34px;
  background: repeating-linear-gradient(
    -45deg,
    #fff,
    #fff 4px,
    #000 4px,
    #000 9px
  );
  border-right: 2px solid var(--floor-color, #f1df76);
}

.pm-hazard-btn:hover {
  background: #111418;
  box-shadow: 0 0 12px var(--floor-color, rgba(241, 223, 118, 0.3));
}

.pm-hazard-btn-text {
  display: flex;
  flex-direction: column;
}

.pm-hazard-btn-text b {
  font: 0.98rem Impact, "Arial Narrow Bold", sans-serif;
  letter-spacing: 0.06em;
  color: var(--floor-color, #fff);
  text-transform: uppercase;
}

.pm-hazard-btn-text small {
  font-size: 0.62rem;
  color: #bbb;
  letter-spacing: 0.08em;
}

.pm-hazard-btn img {
  width: 32px;
  height: 32px;
  object-fit: contain;
}

/* Action & Related Archive Hazard Boxes */
.pm-action-btn {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 14px 10px 44px;
  margin: 10px 0;
  border: 2px solid #fff;
  background: #08090c;
  color: #fff;
  font: 1.05rem Impact, "Arial Narrow Bold", sans-serif;
  letter-spacing: 0.08em;
  position: relative;
  text-decoration: none;
}

.pm-action-btn:before {
  content: "";
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 34px;
  background: repeating-linear-gradient(
    -45deg,
    #fff,
    #fff 4px,
    #000 4px,
    #000 9px
  );
  border-right: 2px solid #fff;
}

.pm-action-btn:hover {
  background: #1c2026;
}

.pm-action-btn img {
  width: 28px;
  height: 28px;
  margin-left: auto;
}

.pm-related-section {
  margin-top: 24px;
  text-align: center;
}

.pm-related-section h3 {
  font: 1.15rem Impact, "Arial Narrow Bold", sans-serif;
  letter-spacing: 0.12em;
  color: #f1df76;
  margin: 0 0 12px;
  text-transform: uppercase;
}

.pm-related-card {
  display: block;
  border: 2px dashed #f1df76;
  padding: 8px;
  margin-bottom: 14px;
  background: #050608;
  position: relative;
  text-decoration: none;
  transition: transform 0.2s ease;
}

.pm-related-card:hover {
  transform: scale(1.02);
  border-style: solid;
}

.pm-related-card img {
  display: block;
  width: 100%;
  max-height: 85px;
  object-fit: cover;
  border: 1px solid #333;
}

.pm-related-card span {
  display: block;
  font-size: 0.72rem;
  color: #ddd;
  margin-top: 6px;
  font-weight: bold;
  letter-spacing: 0.05em;
}
"""

with open("/home/user/01_Somnarak_Wiki/assets/css/wiki.css", "a", encoding="utf-8") as fp:
    fp.write("\n" + css_additions)

print("wiki.css updated with PM authentic layout classes.")
