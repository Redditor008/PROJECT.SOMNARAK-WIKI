import re

css_path = "/home/user/01_Somnarak_Wiki/assets/css/wiki.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Let's add high-fidelity, spacious layout rules and large icon sizes at the end of wiki.css
new_rules = """

/* ==========================================================================
   UN-SQUISHED MODERN WIKI.GG / PROJECT MOON ARTICLE LAYOUT & PROMINENT ICONS
   ========================================================================== */

/* Main shell layout: 
   On home page, 3-column layout with right rail.
   On ALL article and sub-pages, 2-column layout (Left Rail + Spacious Full-Width Content). */
.wiki-shell {
  width: min(1680px, 98vw) !important;
  margin: 1rem auto 2.5rem !important;
  display: grid !important;
  grid-template-columns: 220px minmax(0, 1fr) !important;
  gap: 0 !important;
  background: rgba(5, 7, 10, 0.98) !important;
  border: 1px solid #2a1518 !important;
  box-shadow: 0 0 40px rgba(0, 0, 0, 0.8), 0 0 20px rgba(56, 189, 248, 0.05) !important;
}

/* Home page specific 3-column grid */
body.home-page .wiki-shell,
.wiki-shell.home-shell {
  grid-template-columns: 220px minmax(0, 1fr) 290px !important;
}

/* Floor rail behavior:
   On article pages, if floor-rail exists in DOM, it becomes a clean bottom navigation panel 
   so it NEVER squishes the article content! */
.wiki-shell:not(.home-shell) .floor-rail {
  grid-column: 1 / -1 !important;
  border-left: 0 !important;
  border-top: 1px solid #3a1c22 !important;
  background: linear-gradient(180deg, #090c12 0%, #030406 100%) !important;
  padding: 1.5rem 1.2rem !important;
  display: grid !important;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)) !important;
  gap: 0.75rem !important;
}

.wiki-shell:not(.home-shell) .floor-rail > h2 {
  grid-column: 1 / -1 !important;
  margin: 0 0 0.5rem !important;
  font-size: 1.3rem !important;
  text-align: left !important;
  border-bottom: 1px solid rgba(241, 223, 118, 0.2) !important;
  padding-bottom: 0.4rem !important;
}

.wiki-shell:not(.home-shell) .floor-rail .pm-action-btn,
.wiki-shell:not(.home-shell) .floor-rail .rail-action {
  grid-column: span 1 !important;
  margin-top: 0 !important;
}

/* Main Content Area: Wide, Spacious & Fully Readable */
#content {
  padding: 1.5rem clamp(1.2rem, 3vw, 2.8rem) 3.5rem !important;
  min-width: 0 !important;
  width: 100% !important;
}

/* ==========================================================================
   PROMINENT, VISUALLY STRIKING ICON SIZES (NO MORE TINY/SQUISHED ICONS)
   ========================================================================== */

/* Hero Banner Icons (Departments, Lore, Characters, Atlas) */
.department-hero {
  display: flex !important;
  align-items: center !important;
  gap: 1.8rem !important;
  padding: 1.6rem 2rem !important;
  background: linear-gradient(135deg, rgba(15, 20, 28, 0.95) 0%, rgba(5, 7, 10, 0.98) 100%) !important;
  border-left: 8px solid var(--floor, #ef5b55) !important;
  border-top: 1px solid rgba(255, 255, 255, 0.08) !important;
  border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05) !important;
  margin-bottom: 1.5rem !important;
  box-shadow: inset 0 0 30px rgba(0, 0, 0, 0.5), 0 4px 15px rgba(0, 0, 0, 0.4) !important;
}

.department-hero > img {
  width: 105px !important;
  height: 105px !important;
  min-width: 105px !important;
  max-width: 105px !important;
  padding: 12px !important;
  background: radial-gradient(circle, rgba(241, 223, 118, 0.12) 0%, rgba(0, 0, 0, 0.6) 80%) !important;
  border: 2px solid var(--floor, #f1df76) !important;
  border-radius: 6px !important;
  box-shadow: 0 0 15px rgba(241, 223, 118, 0.2), inset 0 0 10px rgba(0,0,0,0.8) !important;
  object-fit: contain !important;
}

.department-hero h1 {
  font-size: clamp(1.8rem, 3.2vw, 2.6rem) !important;
  letter-spacing: 0.04em !important;
  margin: 0.3rem 0 !important;
  line-height: 1.1 !important;
}

.department-hero p {
  color: #cbd5e1 !important;
  font-size: 1rem !important;
  margin: 0 !important;
  line-height: 1.4 !important;
}

/* Entity & Equipment Hero Banners */
.entity-hero, .item-hero {
  display: grid !important;
  grid-template-columns: 240px 1fr !important;
  gap: 1.8rem !important;
  align-items: center !important;
  padding: 1.8rem !important;
  background: linear-gradient(135deg, rgba(12, 17, 24, 0.95) 0%, rgba(4, 6, 8, 0.98) 100%) !important;
  border-left: 8px solid var(--entity, var(--item, #38bdf8)) !important;
  border-top: 1px solid #1e293b !important;
  margin-bottom: 1.5rem !important;
}

.entity-hero .entity-portrait,
.item-hero .item-portrait {
  width: 220px !important;
  height: 220px !important;
  min-width: 220px !important;
  object-fit: contain !important;
  background: radial-gradient(circle, rgba(0, 0, 0, 0.7) 0%, rgba(10, 15, 22, 0.9) 100%) !important;
  border: 2px solid var(--entity, var(--item, #38bdf8)) !important;
  border-radius: 4px !important;
  padding: 14px !important;
  box-shadow: 0 0 20px rgba(56, 189, 248, 0.2) !important;
}

.entity-hero h1, .item-hero h1 {
  font-size: clamp(2rem, 3.5vw, 3rem) !important;
  margin: 0.3rem 0 !important;
}

/* Entity & Character Gallery Cards (Hub Pages) */
.entity-gallery {
  display: grid !important;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)) !important;
  gap: 1.25rem !important;
  margin: 1.5rem 0 2.5rem !important;
}

.entity-card {
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  text-align: center !important;
  padding: 1.5rem 1.2rem !important;
  background: linear-gradient(180deg, #0a0e16 0%, #040608 100%) !important;
  border: 2px solid var(--card-border, #334155) !important;
  border-radius: 4px !important;
  transition: all 0.2s ease-in-out !important;
  text-decoration: none !important;
}

.entity-card:hover {
  transform: translateY(-4px) !important;
  border-color: var(--gold, #f1df76) !important;
  box-shadow: 0 8px 24px rgba(241, 223, 118, 0.15) !important;
  background: #0f1520 !important;
}

.entity-card img {
  width: 96px !important;
  height: 96px !important;
  min-width: 96px !important;
  max-width: 96px !important;
  object-fit: contain !important;
  padding: 10px !important;
  background: radial-gradient(circle, rgba(241, 223, 118, 0.08) 0%, rgba(0, 0, 0, 0.7) 80%) !important;
  border: 1px solid var(--card-border, rgba(241, 223, 118, 0.3)) !important;
  border-radius: 6px !important;
  margin-bottom: 0.9rem !important;
}

.entity-card h3 {
  font-size: 1.25rem !important;
  color: #fff !important;
  margin: 0.2rem 0 !important;
}

.entity-card p {
  font-size: 0.88rem !important;
  color: #94a3b8 !important;
  line-height: 1.35 !important;
  margin: 0.3rem 0 0 !important;
}

/* Home Page 2x4 Feature Grid Cards */
.pm-feature-grid {
  display: grid !important;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)) !important;
  gap: 1.2rem !important;
  margin: 1.8rem 0 !important;
}

.pm-card {
  min-height: 200px !important;
  padding: 1.5rem 1.2rem !important;
}

.pm-card .pm-card-icon {
  width: 92px !important;
  height: 92px !important;
  min-width: 92px !important;
  max-width: 92px !important;
  margin: 0.8rem auto !important;
  object-fit: contain !important;
  filter: drop-shadow(0 0 8px rgba(113, 239, 175, 0.4)) !important;
}

.pm-card.gold .pm-card-icon {
  filter: drop-shadow(0 0 8px rgba(241, 223, 118, 0.4)) !important;
}

.pm-card.crimson .pm-card-icon {
  filter: drop-shadow(0 0 8px rgba(239, 91, 85, 0.4)) !important;
}

.pm-card.cyan .pm-card-icon {
  filter: drop-shadow(0 0 8px rgba(56, 189, 248, 0.4)) !important;
}

/* Archive Portal Grid (Legacy / 404 pages) */
.archive-portal img {
  width: 90px !important;
  height: 90px !important;
  min-width: 90px !important;
  max-width: 90px !important;
  margin-bottom: 0.8rem !important;
}

/* Equipment Art Cards */
.equipment-art {
  height: 180px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  padding: 14px !important;
  background: radial-gradient(circle, rgba(0,0,0,0.4) 0%, rgba(5,8,12,0.9) 100%) !important;
}

.equipment-art img {
  width: 100% !important;
  height: 100% !important;
  max-height: 150px !important;
  object-fit: contain !important;
}

/* Work Responses & Class Grids */
.work-response img,
.registry-class-grid img,
.maw-class-grid img,
.maw-set-card img,
.zone-card img {
  width: 60px !important;
  height: 60px !important;
  min-width: 60px !important;
  object-fit: contain !important;
}

/* Left Rail Logo */
.site-mark img {
  width: 105px !important;
  height: 105px !important;
  object-fit: contain !important;
}

/* Floor Hazard Buttons */
.pm-hazard-btn img,
.floor-button img {
  width: 44px !important;
  height: 44px !important;
  min-width: 44px !important;
  object-fit: contain !important;
}

/* Meta Cards Grid: High Density & Clean Contrast */
.entity-meta-grid {
  display: grid !important;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)) !important;
  gap: 0.8rem !important;
  margin: 1.5rem 0 2rem !important;
}

.meta-card {
  padding: 0.9rem 1.1rem !important;
  background: rgba(12, 16, 23, 0.9) !important;
  border: 1px solid rgba(56, 189, 248, 0.25) !important;
  border-left: 4px solid var(--gold, #f1df76) !important;
}

.meta-card b {
  font-size: 0.72rem !important;
  color: #38bdf8 !important;
  letter-spacing: 0.12em !important;
}

.meta-card span {
  font-size: 0.95rem !important;
  color: #f8fafc !important;
  font-weight: 600 !important;
  margin-top: 0.25rem !important;
}

/* Article Body Typography & Spacing */
.article-body {
  font-size: 1.02rem !important;
  line-height: 1.75 !important;
  color: #e2e8f0 !important;
  max-width: 1300px !important;
}

.article-body h2 {
  font-size: 1.65rem !important;
  color: var(--gold, #f1df76) !important;
  border-bottom: 2px solid rgba(241, 223, 118, 0.25) !important;
  padding-bottom: 0.45rem !important;
  margin: 2.2rem 0 1rem !important;
  letter-spacing: 0.05em !important;
}

.article-body h3 {
  font-size: 1.28rem !important;
  color: #38bdf8 !important;
  margin: 1.6rem 0 0.6rem !important;
}

.article-body p {
  margin: 0.9rem 0 1.2rem !important;
}

.article-body blockquote {
  border-left: 4px solid var(--gold, #f1df76) !important;
  background: rgba(15, 23, 42, 0.6) !important;
  padding: 1.2rem 1.5rem !important;
  margin: 1.5rem 0 !important;
  font-style: italic !important;
  color: #f1f5f9 !important;
}

/* Data Tables */
.data-table {
  width: 100% !important;
  border-collapse: collapse !important;
  margin: 1.5rem 0 2rem !important;
  background: #080c12 !important;
  border: 1px solid #1e293b !important;
}

.data-table th {
  background: #0f172a !important;
  color: #f1df76 !important;
  padding: 0.9rem 1rem !important;
  text-align: left !important;
  font-size: 0.85rem !important;
  letter-spacing: 0.08em !important;
  border: 1px solid #1e293b !important;
}

.data-table td {
  padding: 0.85rem 1rem !important;
  border: 1px solid #1e293b !important;
  font-size: 0.92rem !important;
  color: #cbd5e1 !important;
}

.data-table tr:nth-child(even) {
  background: rgba(15, 23, 42, 0.3) !important;
}

/* Responsive adjustments */
@media (max-width: 900px) {
  .wiki-shell {
    display: flex !important;
    flex-direction: column !important;
    width: 100% !important;
    margin: 0 !important;
  }
  .left-rail {
    display: none !important;
  }
  .left-rail.open {
    display: block !important;
    position: fixed !important;
    inset: 38px auto 0 0 !important;
    z-index: 99 !important;
    width: 280px !important;
  }
  .entity-hero, .item-hero {
    grid-template-columns: 1fr !important;
  }
  .entity-hero .entity-portrait,
  .item-hero .item-portrait {
    margin: 0 auto !important;
  }
}
"""

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css + new_rules)

print("Updated wiki.css with prominent icon sizes and un-squished spacious layout.")
