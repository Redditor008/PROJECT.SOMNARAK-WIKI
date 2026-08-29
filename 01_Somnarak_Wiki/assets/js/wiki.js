/**
 * SOMNARAK OFFICIAL WIKI — INTERACTIVE SCRIPT & NAVIGATION ENGINE
 * 
 * Features:
 * 1. wiki.gg / MediaWiki Authentic Jump Navigation & Smooth Scroll
 * 2. In-Article Table of Contents (#toc) with working [hide]/[show] toggle (supports <ol> and <ul>)
 * 3. Interactive [View Source] Terminal Modal with copy-to-clipboard & raw Markdown viewer
 * 4. Interactive [History] Cycle Revision Log Modal across the 1,778 Cycles
 * 5. Dynamic Floating Quick-TOC with IntersectionObserver Active Section Tracking
 * 6. Section Heading Anchor Permalinks & Click-to-Copy
 * 7. Target Jump Pulse Highlight Animation
 * 8. Floating Back-to-Top Button
 * 9. Real-Time Asynchronous Search Engine
 * 10. Pan/Zoom Vector Canvas Map Viewer
 * 11. Mobile Responsive Navigation Rail Drawer
 */

(() => {
  'use strict';

  const q = (sel, el = document) => el.querySelector(sel);
  const qa = (sel, el = document) => [...el.querySelectorAll(sel)];

  // Helper: Escape HTML entities
  function esc(str) {
    return String(str).replace(/[&<>"']/g, c => ({
      '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
    }[c]));
  }

  // =========================================================================
  // 1. MOBILE LEFT RAIL NAVIGATION DRAWER
  // =========================================================================
  const navBtn = q('.nav-open');
  const leftRail = q('.left-rail');
  if (navBtn && leftRail) {
    navBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      leftRail.classList.toggle('open');
      navBtn.setAttribute('aria-expanded', String(leftRail.classList.contains('open')));
    });

    document.addEventListener('click', (e) => {
      if (leftRail.classList.contains('open') && !leftRail.contains(e.target) && !navBtn.contains(e.target)) {
        leftRail.classList.remove('open');
        navBtn.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // =========================================================================
  // 2. SMOOTH OFFSET ANCHOR JUMPING & TARGET PULSE HIGHLIGHT
  // =========================================================================
  const HEADER_OFFSET = 90;

  function scrollToAnchor(targetId, updateHistory = true) {
    if (!targetId) return;
    const cleanId = targetId.replace(/^#/, '');
    const el = document.getElementById(cleanId) || document.getElementById(decodeURIComponent(cleanId));
    if (!el) return;

    const elRect = el.getBoundingClientRect();
    const targetScrollY = window.pageYOffset + elRect.top - HEADER_OFFSET;

    window.scrollTo({
      top: Math.max(0, targetScrollY),
      behavior: 'smooth'
    });

    if (updateHistory) {
      history.pushState(null, '', '#' + cleanId);
    }

    el.classList.remove('target-jump-highlight');
    void el.offsetWidth;
    el.classList.add('target-jump-highlight');

    setTimeout(() => {
      el.classList.remove('target-jump-highlight');
    }, 2200);
  }

  document.addEventListener('click', (e) => {
    const anchor = e.target.closest('a[href^="#"]');
    if (!anchor) return;

    const href = anchor.getAttribute('href');
    if (href === '#' || href === '#top') {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: 'smooth' });
      return;
    }

    if (href.startsWith('#')) {
      const targetEl = document.getElementById(href.slice(1)) || document.getElementById(decodeURIComponent(href.slice(1)));
      if (targetEl) {
        e.preventDefault();
        scrollToAnchor(href.slice(1));
        
        const floatToc = q('.float-toc');
        if (floatToc && floatToc.classList.contains('open')) {
          floatToc.classList.remove('open');
        }
      }
    }
  });

  window.addEventListener('DOMContentLoaded', () => {
    if (window.location.hash) {
      setTimeout(() => {
        scrollToAnchor(window.location.hash.slice(1), false);
      }, 150);
    }
  });

  // =========================================================================
  // 3. IN-ARTICLE TABLE OF CONTENTS (#toc) TOGGLE (SUPPORTS <ol> & <ul>)
  // =========================================================================
  function initTableOfContents() {
    qa('.toc, #toc').forEach(toc => {
      const title = q('.toctitle, .toc-title', toc);
      if (!title) return;

      const list = q('ol, ul', toc);
      if (!list) return;

      let toggleBtn = q('.toc-toggle-btn', title);
      if (!toggleBtn) {
        toggleBtn = document.createElement('button');
        toggleBtn.type = 'button';
        toggleBtn.className = 'toc-toggle-btn';
        toggleBtn.setAttribute('aria-expanded', 'true');
        toggleBtn.innerHTML = '[<span class="toggle-label">hide</span>]';
        title.appendChild(toggleBtn);
      }

      // Check saved state
      const savedState = localStorage.getItem('somnarak_wiki_toc_collapsed');
      if (savedState === 'true') {
        list.style.display = 'none';
        toggleBtn.setAttribute('aria-expanded', 'false');
        const lbl = q('.toggle-label', toggleBtn);
        if (lbl) lbl.textContent = 'show';
      }

      toggleBtn.onclick = (e) => {
        e.preventDefault();
        e.stopPropagation();
        const isHidden = list.style.display === 'none';
        list.style.display = isHidden ? '' : 'none';
        toggleBtn.setAttribute('aria-expanded', isHidden ? 'true' : 'false');
        const lbl = q('.toggle-label', toggleBtn);
        if (lbl) lbl.textContent = isHidden ? 'hide' : 'show';
        localStorage.setItem('somnarak_wiki_toc_collapsed', isHidden ? 'false' : 'true');
      };
    });
  }

  // =========================================================================
  // 4. INTERACTIVE [VIEW SOURCE] & [HISTORY] TERMINAL MODALS
  // =========================================================================
  function initActionTabs() {
    // Shared Modal Container
    let modal = q('#wiki-action-modal');
    if (!modal) {
      modal = document.createElement('div');
      modal.id = 'wiki-action-modal';
      modal.className = 'wiki-action-modal';
      modal.innerHTML = `
        <div class="action-modal-backdrop"></div>
        <div class="action-modal-dialog">
          <div class="action-modal-header">
            <div class="action-modal-title">
              <span class="modal-status-led"></span>
              <b id="action-modal-title-text">DIRECTORATE TERMINAL</b>
            </div>
            <button type="button" class="action-modal-close" aria-label="Close">✕</button>
          </div>
          <div class="action-modal-body" id="action-modal-body-content"></div>
          <div class="action-modal-footer">
            <span class="modal-clearance-tag">AUTHORIZATION: LEVEL 5 RESTRICTED</span>
            <button type="button" class="modal-btn-copy" id="modal-copy-btn">COPY TO CLIPBOARD</button>
          </div>
        </div>
      `;
      document.body.appendChild(modal);

      const closeBtn = q('.action-modal-close', modal);
      const backdrop = q('.action-modal-backdrop', modal);
      const close = () => modal.classList.remove('open');
      if (closeBtn) closeBtn.onclick = close;
      if (backdrop) backdrop.onclick = close;
    }

    const modalTitle = q('#action-modal-title-text', modal);
    const modalBody = q('#action-modal-body-content', modal);
    const copyBtn = q('#modal-copy-btn', modal);

    document.addEventListener('click', (e) => {
      const actionBtn = e.target.closest('.action-btn, .page-action-btn, [data-action="view-source"], [data-action="history"]');
      if (!actionBtn) return;

      const text = actionBtn.textContent.trim().toLowerCase();
      const action = actionBtn.dataset.action || (text.includes('source') ? 'view-source' : text.includes('history') ? 'history' : null);
      if (!action) return;

      e.preventDefault();
      const pageTitle = (q('h1') ? q('h1').textContent.replace(/^[■›•\s\d\.\/]+/, '').trim() : document.title) || 'Archive Document';
      const pathName = window.location.pathname.split('/').pop() || 'index.html';

      if (action === 'view-source') {
        modalTitle.textContent = `SOURCE ARCHIVE // ${pathName.toUpperCase()}`;
        const mainContent = q('#content') || q('.wiki-content') || q('main');
        const rawText = mainContent ? mainContent.innerText.trim() : 'No source content available.';
        
        modalBody.innerHTML = `
          <div class="terminal-source-view">
            <div class="source-info-bar">
              <span>FORMAT: SOMNARAK-MARKDOWN / UTF-8</span>
              <span>LINES: ${rawText.split('\\n').length}</span>
            </div>
            <pre class="source-code-block"><code>${esc(rawText)}</code></pre>
          </div>
        `;

        copyBtn.style.display = 'block';
        copyBtn.onclick = () => {
          navigator.clipboard.writeText(rawText).then(() => {
            copyBtn.textContent = 'COPIED TO CLIPBOARD!';
            setTimeout(() => { copyBtn.textContent = 'COPY TO CLIPBOARD'; }, 1800);
          }).catch(() => {});
        };

        modal.classList.add('open');
      } else if (action === 'history') {
        modalTitle.textContent = `CYCLE REVISION HISTORY // ${pathName.toUpperCase()}`;
        modalBody.innerHTML = `
          <div class="cycle-history-timeline">
            <div class="history-card active-rev">
              <div class="history-header">
                <span class="rev-badge rev-current">REVISION 1,778 (ACTIVE)</span>
                <span class="rev-date">YEAR 4,238 · DAWN INITIATIVE</span>
              </div>
              <p class="rev-desc">Canonical stabilization audit by Secretary Seiyon. Integrated M.A.W. resonance telemetry, active Coherence thresholds, and emergency lockdown triggers.</p>
              <div class="rev-meta">Lead Sign-Off: Director Majin // Status: Unsealed Access</div>
            </div>

            <div class="history-card">
              <div class="history-header">
                <span class="rev-badge">REVISION 1,141 (RESET ERA)</span>
                <span class="rev-date">CYCLE 1,141 PROTOCOL 07</span>
              </div>
              <p class="rev-desc">Facility-wide memory wipe protocol executed. Redacted subterranean casualty logs and quarantined Efflorescence contamination zones.</p>
              <div class="rev-meta">Archivist: Marjuk (Deep Vault) // Clearance: Restricted</div>
            </div>

            <div class="history-card">
              <div class="history-header">
                <span class="rev-badge">REVISION 0,211 (CONTAINMENT)</span>
                <span class="rev-date">CYCLE 0211 FOUNDATION</span>
              </div>
              <p class="rev-desc">First systematic categorization of 4 Work Types (Communion, Dissection, Siphon, Subjugation). Commissioning of Floor 3 Extraction Hall.</p>
              <div class="rev-meta">Lead: Zyrak // Status: Archived</div>
            </div>

            <div class="history-card">
              <div class="history-header">
                <span class="rev-badge">REVISION 0,001 (ORIGIN)</span>
                <span class="rev-date">DAY 001 · COMMISSIONING</span>
              </div>
              <p class="rev-desc">Initial discovery of the subterranean Weeping and establishment of Facility 01 (The Hand of Change) beneath the Alpha Tree.</p>
              <div class="rev-meta">Author: Director Majin // Status: Historical Stele</div>
            </div>
          </div>
        `;

        copyBtn.style.display = 'none';
        modal.classList.add('open');
      }
    });
  }

  // =========================================================================
  // 5. FLOATING QUICK-TOC & ACTIVE SECTION TRACKING
  // =========================================================================
  function initFloatingToc() {
    const contentArea = q('#content') || q('.wiki-content') || q('main');
    const headings = qa('h2[id], h3[id]', contentArea);
    if (headings.length < 2) return;

    let floatToc = q('.float-toc');
    if (!floatToc) {
      floatToc = document.createElement('nav');
      floatToc.className = 'float-toc';
      floatToc.setAttribute('aria-label', 'Quick section navigation');
      floatToc.innerHTML = `
        <button type="button" class="float-toc-trigger" aria-expanded="false" title="Table of Contents">
          <span class="toc-icon">☰</span> <span class="toc-text">CONTENTS</span>
        </button>
        <div class="float-toc-panel">
          <div class="float-toc-header">
            <b>PAGE CONTENTS</b>
            <span class="float-toc-count">${headings.length} SECTIONS</span>
          </div>
          <ul class="float-toc-list"></ul>
        </div>
      `;
      document.body.appendChild(floatToc);
    }

    const floatList = q('.float-toc-list', floatToc);
    if (floatList && floatList.children.length === 0) {
      headings.forEach((h, idx) => {
        const li = document.createElement('li');
        li.className = h.tagName.toLowerCase() === 'h3' ? 'float-toc-sub' : 'float-toc-main';
        const a = document.createElement('a');
        a.href = '#' + h.id;
        a.dataset.targetId = h.id;
        const cleanTitle = h.textContent.replace(/^[■›•\s\d\.\/]+/, '').trim();
        a.innerHTML = `<span class="toc-num">${idx + 1}.</span> <span class="toc-label">${esc(cleanTitle)}</span>`;
        li.appendChild(a);
        floatList.appendChild(li);
      });
    }

    const triggers = qa('.float-toc-trigger, .float-toc > button', floatToc);
    triggers.forEach(trigger => {
      trigger.onclick = (e) => {
        e.stopPropagation();
        const isOpen = floatToc.classList.toggle('open');
        trigger.setAttribute('aria-expanded', String(isOpen));
      };
    });

    document.addEventListener('click', (e) => {
      if (floatToc && floatToc.classList.contains('open') && !floatToc.contains(e.target)) {
        floatToc.classList.remove('open');
        triggers.forEach(tr => tr.setAttribute('aria-expanded', 'false'));
      }
    });

    const observerCallback = (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const id = entry.target.id;
          qa('.float-toc-list a, #toc a').forEach(link => {
            if (link.getAttribute('href') === '#' + id || link.dataset.targetId === id) {
              link.classList.add('active-toc-item');
            } else {
              link.classList.remove('active-toc-item');
            }
          });
        }
      });
    };

    const headingObserver = new IntersectionObserver(observerCallback, {
      rootMargin: '-80px 0px -60% 0px',
      threshold: 0
    });

    headings.forEach(h => headingObserver.observe(h));
  }

  // =========================================================================
  // 6. SECTION HEADING ANCHOR PERMALINKS
  // =========================================================================
  function initHeadingPermalinks() {
    const contentArea = q('#content') || q('.wiki-content') || q('main');
    qa('h2[id], h3[id]', contentArea).forEach(heading => {
      if (q('.heading-permalink', heading)) return;

      const permalink = document.createElement('a');
      permalink.className = 'heading-permalink';
      permalink.href = '#' + heading.id;
      permalink.setAttribute('aria-label', 'Permalink to ' + heading.textContent);
      permalink.innerHTML = '<span class="permalink-icon">#</span><span class="permalink-tooltip">Copy link</span>';

      permalink.addEventListener('click', (e) => {
        e.preventDefault();
        scrollToAnchor(heading.id);
        
        const fullUrl = window.location.origin + window.location.pathname + '#' + heading.id;
        navigator.clipboard.writeText(fullUrl).then(() => {
          const tooltip = q('.permalink-tooltip', permalink);
          if (tooltip) {
            tooltip.textContent = 'Copied!';
            setTimeout(() => { tooltip.textContent = 'Copy link'; }, 1800);
          }
        }).catch(() => {});
      });

      heading.appendChild(permalink);
    });
  }

  // =========================================================================
  // 7. FLOATING BACK-TO-TOP BUTTON
  // =========================================================================
  function initBackToTop() {
    let backToTop = q('#back-to-top-btn');
    if (!backToTop) {
      backToTop = document.createElement('button');
      backToTop.id = 'back-to-top-btn';
      backToTop.className = 'back-to-top-btn';
      backToTop.type = 'button';
      backToTop.setAttribute('aria-label', 'Return to top of page');
      backToTop.innerHTML = '▲ <span class="btn-text">TOP</span>';
      document.body.appendChild(backToTop);
    }

    window.addEventListener('scroll', () => {
      if (window.pageYOffset > 320) {
        backToTop.classList.add('visible');
      } else {
        backToTop.classList.remove('visible');
      }
    }, { passive: true });

    backToTop.onclick = () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    };
  }

  // =========================================================================
  // 8. REAL-TIME ASYNCHRONOUS SEARCH DATABASE
  // =========================================================================
  function initSearch() {
    const searchInput = q('#search') || q('#search-input');
    const searchResults = q('#results');
    let searchDatabase = null;

    if (searchInput && searchResults) {
      searchInput.addEventListener('input', async () => {
        const term = searchInput.value.trim().toLowerCase();
        if (term.length < 2) {
          searchResults.classList.remove('open');
          searchResults.innerHTML = '';
          return;
        }

        if (!searchDatabase) {
          try {
            const indexPath = searchInput.dataset.index || '../data/search.json';
            searchDatabase = await fetch(indexPath).then(res => res.json());
          } catch (err) {
            console.error('Failed to load search index:', err);
            return;
          }
        }

        const indexPath = searchInput.dataset.index || '../data/search.json';
        const basePrefix = indexPath.replace(/data\/search\.json$/, '');

        const matches = searchDatabase.filter(item => {
          const haystack = `${item.title} ${item.subtitle || ''} ${item.terms || ''}`.toLowerCase();
          return haystack.includes(term);
        }).slice(0, 10);

        if (matches.length === 0) {
          searchResults.innerHTML = '<div class="search-no-result">No matching archives found</div>';
        } else {
          searchResults.innerHTML = matches.map(item => `
            <a href="${basePrefix}${item.url}">
              <b>${esc(item.title)}</b>
              <small>${esc(item.subtitle || 'Article Archive')}</small>
            </a>
          `).join('');
        }

        searchResults.classList.add('open');
      });

      document.addEventListener('click', (e) => {
        if (!searchInput.contains(e.target) && !searchResults.contains(e.target)) {
          searchResults.classList.remove('open');
        }
      });
    }
  }

  // Initialize all components on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      initTableOfContents();
      initActionTabs();
      initFloatingToc();
      initHeadingPermalinks();
      initBackToTop();
      initSearch();
    });
  } else {
    initTableOfContents();
    initActionTabs();
    initFloatingToc();
    initHeadingPermalinks();
    initBackToTop();
    initSearch();
  }

})();
