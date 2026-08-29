#!/usr/bin/env python3
"""
tools/append_rich_homepage_css.py
Appends high-contrast styling for homepage features and spotlight grids to wiki.css
"""

css_to_add = """
/* ==========================================================================
   HOMEPAGE ENRICHMENT & SPOTLIGHT STYLES
   ========================================================================== */

.pm-dispatch-banner {
  background: #090e18;
  border: 1px solid #f59e0b;
  border-left: 5px solid #f59e0b;
  border-radius: 6px;
  padding: 14px 18px;
  margin-bottom: 24px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
}

.dispatch-header {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 0.85rem;
  letter-spacing: 0.08em;
  color: #f1df76;
  border-bottom: 1px solid rgba(241, 223, 118, 0.2);
  padding-bottom: 8px;
  margin-bottom: 10px;
}

.dispatch-time {
  margin-left: auto;
  font-family: monospace;
  color: #94a3b8;
  font-size: 0.75rem;
}

.dispatch-content {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.dispatch-item {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  font-size: 0.88rem;
  line-height: 1.45;
  color: #cbd5e1;
}

.disp-tag {
  font-size: 0.7rem;
  font-weight: bold;
  padding: 2px 6px;
  border-radius: 3px;
  text-transform: uppercase;
  font-family: monospace;
  white-space: nowrap;
}

.disp-tag.alert-amber { background: #78350f; color: #fef08a; border: 1px solid #f59e0b; }
.disp-tag.alert-blue  { background: #0c4a6e; color: #7dd3fc; border: 1px solid #38bdf8; }
.disp-tag.alert-red   { background: #7f1d1d; color: #fca5a5; border: 1px solid #ef4444; }

.section-title-bar {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  border-bottom: 2px solid #38bdf8;
  padding-bottom: 6px;
  margin-top: 28px;
  margin-bottom: 16px;
}

.section-title-bar h2 {
  font-size: 1.25rem;
  color: #f1df76;
  margin: 0;
  letter-spacing: 0.05em;
}

.section-title-bar .title-sub {
  font-size: 0.75rem;
  color: #94a3b8;
  font-family: monospace;
}

.section-lead-text {
  font-size: 0.95rem;
  line-height: 1.6;
  color: #cbd5e1;
  margin-bottom: 16px;
}

/* Featured Entity Spotlight */
.featured-spotlight-grid {
  display: grid;
  grid-template-columns: 220px 1fr;
  gap: 20px;
  background: #090e18;
  border: 1px solid #ef5b55;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 24px;
  box-shadow: 0 4px 20px rgba(239, 91, 85, 0.15);
}

@media (max-width: 768px) {
  .featured-spotlight-grid {
    grid-template-columns: 1fr;
  }
}

.spotlight-visual {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: #070a12;
  border: 1px solid rgba(239, 91, 85, 0.4);
  border-radius: 6px;
  padding: 14px;
}

.spotlight-img {
  width: 150px;
  height: 150px;
  object-fit: contain;
  filter: drop-shadow(0 0 12px rgba(239, 91, 85, 0.5));
  margin-bottom: 12px;
}

.spotlight-badges {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  justify-content: center;
}

.han-badge {
  background: #1e1b4b;
  color: #c084fc;
  border: 1px solid #818cf8;
  font-size: 0.7rem;
  font-family: monospace;
  padding: 2px 6px;
  border-radius: 3px;
  font-weight: bold;
}

.spotlight-body {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.spotlight-meta-header h3 {
  margin: 0 0 4px 0;
  font-size: 1.25rem;
}

.spotlight-meta-header h3 a {
  color: #f1df76;
  text-decoration: none;
}

.spotlight-meta-header h3 a:hover {
  color: #ffffff;
  text-decoration: underline;
}

.spotlight-meta-header small {
  color: #94a3b8;
  font-family: monospace;
  font-size: 0.78rem;
}

.spotlight-body p {
  margin: 0;
  font-size: 0.92rem;
  line-height: 1.55;
  color: #cbd5e1;
}

.spotlight-actions {
  display: flex;
  gap: 12px;
  margin-top: 6px;
  flex-wrap: wrap;
}

.pm-btn-primary {
  display: inline-block;
  background: #b91c1c;
  color: #ffffff;
  padding: 8px 16px;
  border-radius: 4px;
  font-size: 0.82rem;
  font-weight: bold;
  text-decoration: none;
  border: 1px solid #ef4444;
  transition: background 0.2s;
}

.pm-btn-primary:hover {
  background: #dc2626;
  color: #ffffff;
}

.pm-btn-secondary {
  display: inline-block;
  background: #0f172a;
  color: #38bdf8;
  padding: 8px 16px;
  border-radius: 4px;
  font-size: 0.82rem;
  font-weight: bold;
  text-decoration: none;
  border: 1px solid #0284c7;
  transition: background 0.2s;
}

.pm-btn-secondary:hover {
  background: #0369a1;
  color: #ffffff;
}

/* Comprehensive Article Directory */
.portal-category-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 16px;
  margin-top: 14px;
}

.portal-cat-box {
  background: #090e18;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 6px;
  padding: 16px;
}

.portal-cat-box h4 {
  margin: 0 0 12px 0;
  font-size: 0.95rem;
  color: #f1df76;
  display: flex;
  align-items: center;
  gap: 8px;
  border-bottom: 1px solid rgba(241, 223, 118, 0.2);
  padding-bottom: 6px;
}

.portal-cat-box h4 .cat-icon {
  width: 18px;
  height: 18px;
}

.portal-cat-box ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.portal-cat-box ul li {
  font-size: 0.85rem;
}

.portal-cat-box ul li a {
  color: #cbd5e1;
  text-decoration: none;
  transition: color 0.15s;
}

.portal-cat-box ul li a:hover {
  color: #38bdf8;
  text-decoration: underline;
}
"""

with open("/home/user/01_Somnarak_Wiki/assets/css/wiki.css", "a", encoding="utf-8") as f:
    f.write(css_to_add)

print("Appended rich homepage styling to wiki.css!")
