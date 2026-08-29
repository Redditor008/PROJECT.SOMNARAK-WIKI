css_path = "/home/user/01_Somnarak_Wiki/assets/css/wiki.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

additional_css = """

/* ==========================================================================
   AUTHENTIC WIKI INLINE LINKS & WORD-SIZED ICONS
   ========================================================================== */

.wiki-icon {
  display: inline-block !important;
  width: 1.15em !important;
  height: 1.15em !important;
  min-width: 1.15em !important;
  vertical-align: -0.18em !important;
  margin: 0 0.22em 0 0.08em !important;
  object-fit: contain !important;
  filter: drop-shadow(0 1px 2px rgba(0,0,0,0.8));
}

.wiki-link {
  color: #38bdf8 !important;
  text-decoration: none !important;
  font-weight: 600 !important;
  border-bottom: 1px dotted rgba(56, 189, 248, 0.45) !important;
  transition: all 0.15s ease !important;
  display: inline-flex !important;
  align-items: center !important;
}

.wiki-link:hover {
  color: #f1df76 !important;
  border-bottom: 1px solid #f1df76 !important;
  text-shadow: 0 0 8px rgba(241, 223, 118, 0.4) !important;
}

.wiki-tag {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 1px 6px;
  border-radius: 3px;
  font-size: 0.82em;
  font-weight: 700;
  vertical-align: 0.05em;
  margin: 0 0.2em;
}

.wiki-tag.tag-red {
  background: rgba(239, 91, 85, 0.15);
  border: 1px solid rgba(239, 91, 85, 0.4);
  color: #ef5b55;
}

.wiki-tag.tag-blue {
  background: rgba(56, 189, 248, 0.15);
  border: 1px solid rgba(56, 189, 248, 0.4);
  color: #38bdf8;
}

.wiki-tag.tag-black {
  background: rgba(168, 85, 247, 0.15);
  border: 1px solid rgba(168, 85, 247, 0.4);
  color: #c084fc;
}

.wiki-tag.tag-pale {
  background: rgba(248, 250, 252, 0.15);
  border: 1px solid rgba(248, 250, 252, 0.4);
  color: #f8fafc;
}

.wiki-tag.tag-gold {
  background: rgba(241, 223, 118, 0.15);
  border: 1px solid rgba(241, 223, 118, 0.4);
  color: #f1df76;
}

/* Clear Shell Rules: 2-column by default, 3-column ONLY on home-shell */
.wiki-shell {
  width: min(1640px, 98vw) !important;
  margin: 1rem auto 2.5rem !important;
  display: grid !important;
  grid-template-columns: 220px minmax(0, 1fr) !important;
  gap: 0 !important;
  background: rgba(5, 7, 10, 0.98) !important;
  border: 1px solid #2a1518 !important;
}

.wiki-shell.home-shell {
  grid-template-columns: 220px minmax(0, 1fr) 285px !important;
}

@media (max-width: 1100px) {
  .wiki-shell.home-shell {
    grid-template-columns: 220px minmax(0, 1fr) !important;
  }
  .wiki-shell.home-shell .floor-rail {
    grid-column: 1 / -1 !important;
    border-left: 0 !important;
    border-top: 1px solid #3a1c22 !important;
    display: grid !important;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)) !important;
  }
}

@media (max-width: 860px) {
  .wiki-shell, .wiki-shell.home-shell {
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
    inset: 46px auto 0 0 !important;
    z-index: 120 !important;
    width: 280px !important;
  }
}

/* Typography polish for authentic Wiki readability */
.article-body {
  font-size: 1.05rem !important;
  line-height: 1.8 !important;
  color: #e2e8f0 !important;
}

.article-body p {
  margin: 1rem 0 1.25rem !important;
}

.article-body ul, .article-body ol {
  margin: 0.8rem 0 1.4rem 1.4rem !important;
  line-height: 1.75 !important;
}

.article-body li {
  margin-bottom: 0.5rem !important;
}

.article-body h2 {
  font-size: 1.75rem !important;
  margin-top: 2.4rem !important;
  margin-bottom: 0.9rem !important;
}

.article-body h3 {
  font-size: 1.35rem !important;
  margin-top: 1.8rem !important;
  margin-bottom: 0.6rem !important;
}
"""

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css + additional_css)

print("Updated wiki.css with inline wiki links and word-sized icons styling.")
