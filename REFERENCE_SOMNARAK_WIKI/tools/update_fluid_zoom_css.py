with open("/home/user/01_Somnarak_Wiki/assets/css/wiki.css", "r", encoding="utf-8") as f:
    css = f.read()

fluid_zoom_css = """
/* ==========================================================================
   FLUID ZOOM & RESPONSIVE SCALING ENGINE
   Supports browser zoom levels from 25% to 500% seamlessly
   ========================================================================== */

:root {
  --fluid-body: clamp(0.88rem, 0.82rem + 0.22vw, 1.05rem);
  --fluid-h1: clamp(1.8rem, 3vw + 0.8rem, 3.4rem);
  --fluid-h2: clamp(1.35rem, 1.8vw + 0.5rem, 2.1rem);
  --fluid-h3: clamp(1.08rem, 1.2vw + 0.35rem, 1.55rem);
  --fluid-h4: clamp(0.92rem, 0.8vw + 0.25rem, 1.22rem);
  --fluid-small: clamp(0.72rem, 0.68rem + 0.15vw, 0.85rem);
}

html {
  font-size: 100%;
  -webkit-text-size-adjust: 100%;
  text-size-adjust: 100%;
  box-sizing: border-box;
}

*, *:before, *:after {
  box-sizing: inherit;
}

body {
  font-size: var(--fluid-body);
  line-height: 1.65;
  overflow-x: hidden;
  word-wrap: break-word;
  overflow-wrap: break-word;
}

h1 { font-size: var(--fluid-h1); line-height: 1.15; }
h2 { font-size: var(--fluid-h2); line-height: 1.25; margin-top: 1.5em; margin-bottom: 0.5em; }
h3 { font-size: var(--fluid-h3); line-height: 1.3; margin-top: 1.2em; margin-bottom: 0.4em; }
h4 { font-size: var(--fluid-h4); line-height: 1.35; }
small { font-size: var(--fluid-small); }

p, li, td, th, dt, dd {
  font-size: var(--fluid-body);
  line-height: 1.65;
  overflow-wrap: break-word;
  word-break: normal;
}

/* Fluid Shell Grid that scales and wraps on high zoom */
.wiki-shell {
  width: min(1600px, 96vw);
  margin: 1.2rem auto 2rem;
  display: grid;
  grid-template-columns: minmax(180px, 14rem) minmax(0, 1fr) minmax(220px, 18rem);
  gap: 0;
  transition: all 0.2s ease;
}

@media (max-width: 1200px) {
  .wiki-shell {
    grid-template-columns: minmax(160px, 12rem) minmax(0, 1fr);
  }
  .floor-rail {
    grid-column: 1 / -1;
    border-left: 0;
    border-top: 1px solid var(--line);
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(min(100%, 14rem), 1fr));
    gap: 0.5rem;
  }
}

@media (max-width: 800px) {
  .wiki-shell {
    display: flex;
    flex-direction: column;
    width: 100%;
    margin: 0;
  }
  .left-rail {
    display: none;
  }
  .left-rail.open {
    display: block;
    position: fixed;
    z-index: 999;
    inset: 38px auto 0 0;
    width: min(85vw, 20rem);
    box-shadow: 0 0 30px rgba(0,0,0,0.9);
  }
}

/* Fluid Tables & Containers */
.table-wrap {
  width: 100%;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  margin: 1rem 0 1.5rem;
}

.data-table {
  width: 100%;
  min-width: min(100%, 480px);
  border-collapse: collapse;
}

.data-table th, .data-table td {
  padding: clamp(0.4rem, 0.3rem + 0.3vw, 0.8rem) clamp(0.5rem, 0.4rem + 0.4vw, 1rem);
  font-size: var(--fluid-body);
}

/* Fluid 2x4 Feature Grid */
.pm-feature-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 14rem), 1fr));
  gap: clamp(0.6rem, 0.4rem + 0.5vw, 1.2rem);
  margin-bottom: 2rem;
}

/* Fluid Portals Grid */
.archive-portal-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 15rem), 1fr));
  gap: clamp(0.6rem, 0.4rem + 0.5vw, 1.2rem);
}

.archive-portal {
  min-height: clamp(8rem, 6rem + 3vw, 12rem);
  padding: clamp(1rem, 0.8rem + 0.5vw, 1.5rem) clamp(0.6rem, 0.4rem + 0.4vw, 1rem);
}

.archive-portal img {
  width: clamp(3rem, 2.5rem + 1.5vw, 5rem);
  height: clamp(3rem, 2.5rem + 1.5vw, 5rem);
}

/* Fluid Department Hero */
.department-hero {
  padding: clamp(1rem, 0.8rem + 0.8vw, 2rem);
  gap: clamp(0.8rem, 0.6rem + 0.6vw, 1.5rem);
  flex-wrap: wrap;
}

.department-hero img {
  width: clamp(3.5rem, 3rem + 1.8vw, 6rem);
  height: clamp(3.5rem, 3rem + 1.8vw, 6rem);
  flex-shrink: 0;
}

.department-hero h1 {
  font-size: var(--fluid-h1);
  margin: 0.2rem 0;
}

/* Fluid Meta Cards Grid */
.entity-meta-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 12rem), 1fr));
  gap: clamp(0.4rem, 0.3rem + 0.3vw, 0.8rem);
  margin: 1.2rem 0;
}

.meta-card {
  padding: clamp(0.6rem, 0.4rem + 0.4vw, 1rem);
}

.meta-card b {
  font-size: var(--fluid-small);
}

.meta-card span {
  font-size: var(--fluid-body);
}

/* Fluid Article Body & Quotes */
.article-body {
  font-size: var(--fluid-body);
  max-width: 100%;
}

.article-body ul, .article-body ol {
  padding-left: clamp(1.2rem, 1rem + 0.8vw, 2rem);
}

.dossier-quote, blockquote.motto {
  padding: clamp(0.8rem, 0.6rem + 0.6vw, 1.4rem) clamp(1rem, 0.8rem + 0.8vw, 1.8rem);
  font-size: clamp(0.92rem, 0.85rem + 0.25vw, 1.15rem);
  margin: 1.2rem 0;
}
"""

with open("/home/user/01_Somnarak_Wiki/assets/css/wiki.css", "a", encoding="utf-8") as f:
    f.write("\n" + fluid_zoom_css)

print("Fluid zoom CSS engine appended successfully!")
