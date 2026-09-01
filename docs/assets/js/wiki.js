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
 * 11. Responsive Primary Archive Navigation Drawer
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
  // 1. RESPONSIVE PRIMARY ARCHIVE NAVIGATION
  // =========================================================================
  const navBtn = q('.nav-open');
  const primaryNav = q('.utility-nav');
  if (navBtn && primaryNav) {
    const closePrimaryNav = () => {
      primaryNav.classList.remove('nav-visible');
      navBtn.setAttribute('aria-expanded', 'false');
    };

    navBtn.addEventListener('click', (event) => {
      event.stopPropagation();
      const isOpen = primaryNav.classList.toggle('nav-visible');
      navBtn.setAttribute('aria-expanded', String(isOpen));
    });

    primaryNav.addEventListener('click', (event) => {
      if (event.target.closest('a')) closePrimaryNav();
    });

    document.addEventListener('click', (event) => {
      if (
        primaryNav.classList.contains('nav-visible')
        && !primaryNav.contains(event.target)
        && !navBtn.contains(event.target)
      ) {
        closePrimaryNav();
      }
    });

    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && primaryNav.classList.contains('nav-visible')) {
        closePrimaryNav();
        navBtn.focus();
      }
    });

    window.addEventListener('resize', () => {
      if (window.innerWidth > 900) closePrimaryNav();
    }, { passive: true });
  }

  // =========================================================================
  // 2. SMOOTH OFFSET ANCHOR JUMPING & TARGET PULSE HIGHLIGHT
  // =========================================================================
  function getHeaderOffset() {
    const topBar = q('.utility');
    return Math.ceil(topBar ? topBar.getBoundingClientRect().height : 74) + 16;
  }

  function scrollToAnchor(targetId, updateHistory = true) {
    if (!targetId) return;
    const cleanId = targetId.replace(/^#/, '');
    const el = document.getElementById(cleanId) || document.getElementById(decodeURIComponent(cleanId));
    if (!el) return;

    const elRect = el.getBoundingClientRect();
    const targetScrollY = window.pageYOffset + elRect.top - getHeaderOffset();

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
  // =========================================================================
  // 1b. RUNTIME HEADING ANCHORS (MediaWiki-style auto ids)
  // Many wiki pages have h2/h3 section titles without id attributes, which
  // leaves the floating page-contents and sidebar TOC with nothing to link
  // to. Assign a stable slug id to every heading that lacks one, before any
  // TOC is built. Existing ids are always preserved.
  // =========================================================================
  function slugifyHeading(text) {
    return String(text)
      .replace(/&[a-z]+;/gi, ' ')
      .replace(/[^\p{L}\p{N}\s_-]/gu, ' ')
      .trim()
      .replace(/\s+/g, '-')
      .replace(/^[^-_\p{L}\p{N}]+/u, '')
      .replace(/-+$/g, '')
      .toLowerCase();
  }

  function ensureHeadingIds(contentArea) {
    const root = contentArea || document;
    qa('h2, h3', root).forEach((h) => {
      if (h.closest('.float-toc')) return;
      if (h.id) return;
      const base = slugifyHeading(h.textContent) || 'section';
      let id = base;
      let n = 2;
      while (root.querySelector(`[id="${id}"]`) || document.getElementById(id)) {
        id = `${base}-${n}`;
        n += 1;
      }
      h.id = id;
    });
  }

  function initTableOfContents() {
    qa('.toc, #toc').forEach(toc => {
      const title = q('.toctitle, .toc-title', toc);
      if (!title) return;

      const body = q('.toc-body', toc);
      const lists = body ? [body] : qa('ol, ul', toc);
      if (!lists.length) return;

      let toggleBtn = q('.toc-toggle-btn', title);
      if (!toggleBtn) {
        toggleBtn = document.createElement('button');
        toggleBtn.type = 'button';
        toggleBtn.className = 'toc-toggle-btn';
        toggleBtn.setAttribute('aria-expanded', 'true');
        toggleBtn.innerHTML = '[<span class="toggle-label">hide</span>]';
        title.appendChild(toggleBtn);
      }

      const setHidden = (hidden) => {
        lists.forEach(list => { list.style.display = hidden ? 'none' : ''; });
        toggleBtn.setAttribute('aria-expanded', hidden ? 'false' : 'true');
        const lbl = q('.toggle-label', toggleBtn);
        if (lbl) lbl.textContent = hidden ? 'show' : 'hide';
      };

      const savedState = localStorage.getItem('somnarak_wiki_toc_collapsed');
      if (savedState === 'true') setHidden(true);

      toggleBtn.onclick = (e) => {
        e.preventDefault();
        e.stopPropagation();
        const isHidden = lists[0].style.display === 'none';
        setHidden(!isHidden);
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
    if (document.body.classList.contains('home-page') || document.body.classList.contains('hub-page')) return;

    const contentArea = q('#content') || q('.wiki-content') || q('main');
    if (!contentArea) return;

    const skipTitle = /^(DATABASE HUBS|THE NINE ECHO-CORES|CARTOGRAPHY|FACILITY 01|ENTITY REGISTRY)$/i;
    const clean = (el) => el.textContent.replace(/^[■›•\s\d\.\/]+/, '').replace(/#$/, '').trim();

    // Collect every addressable h2 in the content area, whether or not it is
    // wrapped in a .wiki-section (entity/lore pages use flat h2[id] sections).
    const items = [];
    const seen = new Set();
    qa('h2[id]', contentArea).forEach((h) => {
      if (h.closest('.float-toc')) return;
      const sec = h.closest('.wiki-section');
      if (sec && sec.classList.contains('codex-stub')) return;
      if (seen.has(h.id)) return;
      seen.add(h.id);
      const title = clean(h);
      if (!title || skipTitle.test(title)) return;
      const home = (sec && sec.getAttribute('data-toc-home')) || h.getAttribute('data-toc-home');
      items.push({
        id: h.id,
        title,
        home,
        el: h,
        away: Boolean(home),
        sub: false
      });
    });

    const inPage = items.filter(it => !it.away);
    const useH3 = inPage.length > 0 && inPage.length <= 10;
    if (useH3) {
      inPage.forEach(it => {
        let node = it.el.nextElementSibling;
        while (node && node.tagName !== 'H2') {
          if (node.tagName === 'H3' && node.id && !seen.has(node.id)) {
            const title = clean(node);
            if (title) {
              seen.add(node.id);
              items.push({ id: node.id, title, home: null, el: node, away: false, sub: true });
            }
          }
          node = node.nextElementSibling;
        }
      });
    }

    const visible = items.filter(it => !it.away || it.home);
    if (visible.length < 2) return;

    const hereCount = visible.filter(it => !it.away).length;
    const awayCount = visible.filter(it => it.away).length;

    let floatToc = q('.float-toc');
    if (!floatToc) {
      floatToc = document.createElement('nav');
      floatToc.className = 'float-toc';
      floatToc.setAttribute('aria-label', 'Page contents');
      document.body.appendChild(floatToc);
    }

    floatToc.innerHTML = `
      <button type="button" class="float-toc-trigger" aria-expanded="false" title="Page contents">
        <span class="toc-icon">☰</span>
        <span class="toc-text">PAGE CONTENTS</span>
      </button>
      <div class="float-toc-panel">
        <div class="float-toc-header">
          <b>PAGE CONTENTS</b>
          <span class="float-toc-count">${hereCount || visible.length} HERE</span>
        </div>
        <p class="float-toc-hint">Gold = this page. Cyan ↗ = opens the dedicated record.</p>
        <ul class="float-toc-list"></ul>
      </div>
    `;

    const floatList = q('.float-toc-list', floatToc);
    let nHere = 0;
    let nAway = 0;
    let drewAwayHead = false;
    visible.forEach((it) => {
      if (it.away && !drewAwayHead) {
        const sep = document.createElement('li');
        sep.className = 'float-toc-sep';
        sep.textContent = 'Other records';
        floatList.appendChild(sep);
        drewAwayHead = true;
      }
      const li = document.createElement('li');
      li.className = it.sub ? 'float-toc-sub' : (it.away ? 'float-toc-away' : 'float-toc-main');
      const a = document.createElement('a');
      if (it.away && it.home) {
        a.href = it.home;
        a.className = 'toc-away';
        nAway += 1;
        a.innerHTML = `<span class="toc-num">↗</span> <span class="toc-label">${esc(it.title)}</span>`;
      } else {
        a.href = '#' + it.id;
        a.dataset.targetId = it.id;
        nHere += 1;
        a.innerHTML = `<span class="toc-num">${nHere}</span> <span class="toc-label">${esc(it.title)}</span>`;
      }
      li.appendChild(a);
      floatList.appendChild(li);
    });

    const countEl = q('.float-toc-count', floatToc);
    if (countEl) {
      countEl.textContent = awayCount ? `${hereCount} HERE · ${awayCount} AWAY` : `${hereCount} SECTIONS`;
    }

    const trigger = q('.float-toc-trigger', floatToc);
    trigger.onclick = (e) => {
      e.stopPropagation();
      const isOpen = floatToc.classList.toggle('open');
      trigger.setAttribute('aria-expanded', String(isOpen));
    };

    document.addEventListener('click', (e) => {
      if (floatToc.classList.contains('open') && !floatToc.contains(e.target)) {
        floatToc.classList.remove('open');
        trigger.setAttribute('aria-expanded', 'false');
      }
    });

    const inPageEls = visible.filter(it => !it.away).map(it => it.el);
    if (inPageEls.length && typeof IntersectionObserver !== 'undefined') {
      const headingObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (!entry.isIntersecting) return;
          const id = entry.target.id;
          qa('.float-toc-list a').forEach(link => {
            link.classList.toggle('active-toc-item', link.dataset.targetId === id);
          });
        });
      }, { rootMargin: '-90px 0px -62% 0px', threshold: 0 });
      inPageEls.forEach(h => headingObserver.observe(h));
    }

    // Stick at the last rail: the visible tab keeps its natural position
    // (it is never pushed down), and a long transparent hit zone extends
    // BELOW the tab. That lower hit edge always stops exactly 2px before
    // the top of the lower footer (or the viewport bottom while the footer
    // is off-screen). Only when the footer rises up to that lower hit edge
    // does the tab itself lift, tracking the footer's top edge upward and
    // exiting through the top of the viewport — the visible tab therefore
    // stops exactly before the top of the bottom-bar box and can never
    // cross it. The left edge is pinned to the actual content column
    // because the left-rail width changes across breakpoints.
    const hitExt = document.createElement('span');
    hitExt.className = 'float-toc-hit-ext';
    hitExt.setAttribute('aria-hidden', 'true');
    floatToc.appendChild(hitExt);
    hitExt.addEventListener('click', (e) => {
      e.stopPropagation();
      trigger.click();
    });

    const footer = q('footer.global-footer') || q('footer');
    if (footer) {
      const MAX_EXT = 220;  // longest the transparent lower hit zone gets
      const STOP = 2;       // stop line sits 2px above the footer's top edge
      const LEFT_INSET = 6;
      let ticking = false;
      const updateStick = () => {
        ticking = false;
        const h = floatToc.offsetHeight || 60;
        const btnH = trigger ? (trigger.offsetHeight || h) : h;
        const footerTop = footer.getBoundingClientRect().top;
        const isNarrow = window.matchMedia
          ? window.matchMedia('(max-width: 1100px)').matches
          : window.innerWidth <= 1100;
        const topBar = q('.utility');
        const barH = topBar ? (topBar.offsetHeight || 48) : 48;
        // Resting position: vertically centered in the viewport, but never
        // tucked behind the sticky top bar on short screens.
        const baseTop = Math.max(barH + 14, Math.round((window.innerHeight - h) / 2));
        const naturalTop = isNarrow ? window.innerHeight - 18 - h : baseTop;
        // The lower hit edge stops here: 2px above the footer's top edge,
        // or 2px above the viewport bottom while the footer is off-screen.
        const stopLine = Math.min(footerTop, window.innerHeight) - STOP;
        const top = Math.min(naturalTop, stopLine - h);
        const ext = Math.max(0, Math.min(MAX_EXT, Math.round(stopLine - (top + h))));
        const contentRect = contentArea.getBoundingClientRect();
        let left = Math.max(8, Math.round(contentRect.left + LEFT_INSET));
        // If the left-rail drawer is open (narrow screens), slide the
        // widget to the right of it so the two never clip each other.
        const drawer = q('.left-rail');
        if (drawer && drawer.classList.contains('open')) {
          const dRect = drawer.getBoundingClientRect();
          if (dRect.right > 0 && dRect.left < window.innerWidth) {
            left = Math.max(left, Math.round(dRect.right + 8));
          }
        }
        floatToc.style.setProperty('--float-toc-top', Math.round(top) + 'px');
        floatToc.style.setProperty('--float-toc-bottom', 'auto');
        floatToc.style.setProperty('--float-toc-left', left + 'px');
        floatToc.style.setProperty('--float-toc-hit-ext', ext + 'px');
        floatToc.style.setProperty('--float-toc-hit-ext-top', btnH + 'px');
      };
      const requestStick = () => {
        if (!ticking) {
          ticking = true;
          requestAnimationFrame(updateStick);
        }
      };
      window.addEventListener('scroll', requestStick, { passive: true });
      window.addEventListener('resize', requestStick, { passive: true });
      // The drawer only ever toggles on a click — re-evaluate then too.
      document.addEventListener('click', requestStick, { passive: true });
      updateStick();
    }
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
      const setResultsOpen = (open) => {
        searchResults.classList.toggle('open', open);
        searchInput.setAttribute('aria-expanded', String(open));
      };

      searchInput.addEventListener('input', async () => {
        const term = searchInput.value.trim().toLowerCase();
        if (term.length < 2) {
          setResultsOpen(false);
          searchResults.innerHTML = '';
          return;
        }

        if (!searchDatabase) {
          try {
            const indexPath = searchInput.dataset.index || '../data/search.json';
            searchDatabase = await fetch(indexPath).then(res => {
              if (!res.ok) throw new Error(`Search index returned ${res.status}`);
              return res.json();
            });
          } catch (err) {
            console.error('Failed to load search index:', err);
            searchResults.innerHTML = '<div class="search-no-result">Archive index unavailable</div>';
            setResultsOpen(true);
            return;
          }
        }

        const indexPath = searchInput.dataset.index || '../data/search.json';
        const basePrefix = indexPath.replace(/data\/search\.json$/, '');

        const matches = searchDatabase.filter(item => {
          const haystack = [
            item.title,
            item.subtitle,
            item.terms,
            item.keywords,
            item.description,
            item.category
          ].filter(Boolean).join(' ').toLowerCase();
          return haystack.includes(term);
        }).slice(0, 12);

        if (matches.length === 0) {
          searchResults.innerHTML = '<div class="search-no-result">No matching archives found</div>';
        } else {
          searchResults.innerHTML = matches.map(item => `
            <a href="${basePrefix}${item.url}">
              <b>${esc(item.title)}</b>
              <small>${esc(item.category || item.subtitle || 'Article Archive')}</small>
            </a>
          `).join('');
        }

        setResultsOpen(true);
      });

      searchInput.addEventListener('keydown', (event) => {
        if (event.key === 'Escape') {
          setResultsOpen(false);
          searchInput.blur();
        }
      });

      document.addEventListener('keydown', (event) => {
        const target = event.target;
        const isTyping = target instanceof HTMLInputElement
          || target instanceof HTMLTextAreaElement
          || target.isContentEditable;
        if (event.key === '/' && !isTyping && !event.metaKey && !event.ctrlKey && !event.altKey) {
          event.preventDefault();
          searchInput.focus();
          searchInput.select();
        }
      });

      document.addEventListener('click', (event) => {
        if (!searchInput.contains(event.target) && !searchResults.contains(event.target)) {
          setResultsOpen(false);
        }
      });
    }
  }

  // Random Archive — jumps the reader to a random public record.
  // >>> RANDOM_ARCHIVE_PAGES (generated by tools/sync_random_archive.py — do not edit)
  const RANDOM_ARCHIVE_PAGES = [
    "assets/icons/icons_gallery.html",
    "atlas/hand-of-change-map.html",
    "atlas/somnarak-city-map.html",
    "characters/cheonbulok-refugees.html",
    "characters/doha.html",
    "characters/high-architects.html",
    "characters/index.html",
    "characters/joon.html",
    "characters/kael.html",
    "characters/minho.html",
    "characters/soojin.html",
    "characters/sora.html",
    "characters/taeho.html",
    "characters/the-archive-lead-marjuk.html",
    "characters/the-border-lead-mellda.html",
    "characters/the-containment-lead-dekan.html",
    "characters/the-director-majin.html",
    "characters/the-exile-xyan.html",
    "characters/the-extraction-lead-zyrak.html",
    "characters/the-outsider-ishall.html",
    "characters/the-research-lead-ayshuk.html",
    "characters/the-secretary-seiyon.html",
    "characters/yeonhwa.html",
    "departments/agent-assignment.html",
    "departments/core-suppression-guidelines.html",
    "departments/daily-cycle.html",
    "departments/daily-missions.html",
    "departments/facility-meltdown-procedures.html",
    "departments/facility-room-types.html",
    "departments/facility-upgrades.html",
    "departments/floor-1-neutral-command.html",
    "departments/floor-2-maws-keep.html",
    "departments/floor-3-extraction-hall.html",
    "departments/floor-4-insight-forge.html",
    "departments/floor-5-border-watch.html",
    "departments/floor-6-deep-vault.html",
    "departments/floor-7-shadow-corps.html",
    "departments/floor-8-gate-watch.html",
    "departments/incident-reports-archive.html",
    "departments/index.html",
    "departments/research-observation.html",
    "downloads.html",
    "entities/entity-groups-and-chains.html",
    "entities/hope-transformations.html",
    "entities/ht-001-the-guiding-light.html",
    "entities/ht-002-the-shield-of-dawn.html",
    "entities/ht-003-the-gentle-flame.html",
    "entities/ht-004-the-reuniting-spark.html",
    "entities/ht-005-the-defiant-ember.html",
    "entities/ht-006-the-eternal-warmth.html",
    "entities/ht-007-the-silent-vigil.html",
    "entities/ht-008-the-healing-touch.html",
    "entities/ht-009-the-burning-hope.html",
    "entities/ht-010-the-living-memory.html",
    "entities/ht-011-the-shared-glass.html",
    "entities/ht-012-the-standing-witness.html",
    "entities/ht-v-hc-001-the-trinity-of-dawn.html",
    "entities/ht-v-hh-001-the-hand-of-hope.html",
    "entities/index.html",
    "entities/list.html",
    "entities/se-001-the-orphaned-bell.html",
    "entities/se-002-the-grieving-colossus.html",
    "entities/se-003-the-wilderness-tide.html",
    "entities/se-005-the-smothering-mother.html",
    "entities/se-007-brume.html",
    "entities/se-009-the-memory-weaver.html",
    "entities/se-010-the-convergence.html",
    "entities/se-011-the-whispering-walls.html",
    "entities/se-014-the-debt-eater.html",
    "entities/se-015-the-debt-scale.html",
    "entities/unk-247-the-undelivered-thanks.html",
    "entities/unk-248-the-unconsoled.html",
    "entities/unk-250-the-extinguished.html",
    "entities/unk-251-the-unspoken-line.html",
    "entities/unk-901-the-mewgical-girl.html",
    "entities/unk-902-the-repeated-survivor.html",
    "entities/unk-903-the-music-box-of-agony.html",
    "entities/unknown-entities.html",
    "factions/faction-technology.html",
    "factions/index.html",
    "factions/the-architects.html",
    "factions/the-collectors.html",
    "factions/the-founding-corporations.html",
    "factions/the-giltong-enforcers.html",
    "factions/the-high-council.html",
    "factions/the-horizon-caravan.html",
    "factions/the-judexhan.html",
    "factions/the-keepers.html",
    "factions/the-memory-washers.html",
    "factions/the-menders.html",
    "factions/the-reverie-directorate.html",
    "factions/the-sed-corps.html",
    "factions/the-ucd-strike-force.html",
    "factions/the-underworld-and-wound-walkers.html",
    "factions/the-wardens.html",
    "factions/the-weavers.html",
    "index.html",
    "locations/district-structure-veil-and-raw.html",
    "locations/index.html",
    "locations/the-desolate.html",
    "locations/the-hollow-glass.html",
    "locations/the-library-of-stolen-pasts.html",
    "locations/the-maw.html",
    "locations/the-orphan-bell-tower.html",
    "locations/unknown-cities.html",
    "locations/zone-a-core-nexus.html",
    "locations/zone-b-west-ward.html",
    "locations/zone-c-collectors-row.html",
    "locations/zone-d-forge-and-gardens.html",
    "locations/zone-e-perimeter-bulwark.html",
    "lore/daily-life-in-somnarak.html",
    "lore/efflorescence-and-fracture.html",
    "lore/entity-tales.html",
    "lore/facility-incident-reports.html",
    "lore/index.html",
    "lore/named-fractures.html",
    "lore/night-hazards-and-vigil.html",
    "lore/somnarak-cosmology.html",
    "lore/somnarak-name-registry.html",
    "lore/the-alpha-tree.html",
    "lore/the-book-of-regressor.html",
    "lore/the-cheongula-incident.html",
    "lore/the-cycle-and-absolvohan.html",
    "lore/the-dawn-of-hope.html",
    "lore/the-doorspeech.html",
    "lore/the-dream-realm.html",
    "lore/the-first-sovereign-war.html",
    "lore/the-seven-absolute-taboos.html",
    "lore/the-three-ages-and-history.html",
    "lore/the-three-sorrows.html",
    "lore/the-weeping-river.html",
    "maw/index.html",
    "maw/maw-crafting-and-extraction.html",
    "maw/maw-g-001-01-laments-edge.html",
    "maw/maw-g-002-01-the-mourning-shell.html",
    "maw/maw-g-003-01-memory-thread-needle.html",
    "maw/maw-g-004-01-corrosion-visor.html",
    "maw/maw-g-005-01-the-embrace.html",
    "maw/maw-g-006-01-effluent-gland.html",
    "maw/maw-g-007-01-the-hope-lantern.html",
    "maw/maw-g-008-01-spike-crown.html",
    "maw/maw-g-009-01-the-forgotten-mask.html",
    "maw/maw-g-010-01-the-absolute-verdict.html",
    "maw/maw-g-011-01-the-listening-stone.html",
    "maw/maw-g-014-01-the-debt-scale-gift.html",
    "maw/maw-g-015-01-the-balance-pendant.html",
    "maw/maw-s-001-01-the-laments-shroud.html",
    "maw/maw-s-002-01-the-mourning-mantle.html",
    "maw/maw-s-003-01-tide-cloak.html",
    "maw/maw-s-004-01-sentrys-iron-plate.html",
    "maw/maw-s-005-01-the-embrace-plate.html",
    "maw/maw-s-006-01-leech-membrane-suit.html",
    "maw/maw-s-007-01-the-hope-veil.html",
    "maw/maw-s-008-01-sarcophagus-shroud.html",
    "maw/maw-s-009-01-the-forgotten-veil.html",
    "maw/maw-s-010-01-the-absolute-mantle.html",
    "maw/maw-s-011-01-the-listening-shroud.html",
    "maw/maw-s-014-01-the-debt-veil.html",
    "maw/maw-s-015-01-the-balance-veil.html",
    "maw/maw-set-synergies.html",
    "maw/maw-w-001-01-the-laments-requiem.html",
    "maw/maw-w-002-01-the-mourning-maul.html",
    "maw/maw-w-003-01-memory-blade.html",
    "maw/maw-w-004-01-rust-halberd.html",
    "maw/maw-w-005-01-the-embrace-fang.html",
    "maw/maw-w-006-01-siphon-cannula.html",
    "maw/maw-w-007-01-the-hope-lens.html",
    "maw/maw-w-008-01-thorn-impaler.html",
    "maw/maw-w-009-01-the-forgotten-lens.html",
    "maw/maw-w-010-01-the-absolute-maul.html",
    "maw/maw-w-011-01-the-listening-requiem.html",
    "maw/maw-w-014-01-the-debt-lens.html",
    "maw/maw-w-015-01-the-balance-lens.html",
    "mechanics/agent-attributes-and-stats.html",
    "mechanics/containment-and-suppression.html",
    "mechanics/default-standard-equipment.html",
    "mechanics/enemy-bestiary.html",
    "mechanics/fracture-and-therapy.html",
    "mechanics/han-energy-and-damage.html",
    "mechanics/han-relic-registry.html",
    "mechanics/han-relics-and-tools.html",
    "mechanics/index.html",
    "mechanics/maw-equipment-system.html",
    "mechanics/ordeal-black.html",
    "mechanics/ordeal-blue.html",
    "mechanics/ordeal-grey.html",
    "mechanics/ordeal-pale.html",
    "mechanics/ordeal-purple.html",
    "mechanics/ordeals-framework.html",
    "mechanics/panic-states-and-corrosion.html",
    "mechanics/resonant-clash-mechanics.html",
    "mechanics/taboo-resonance-mechanics.html",
    "mechanics/the-four-ordeals.html",
    "mechanics/the-four-work-types.html",
    "project/downloads.html",
    "project/source-map.html"
  ];
// <<< RANDOM_ARCHIVE_PAGES

  function initRandomArchive() {
    if (!RANDOM_ARCHIVE_PAGES.length) return;
    document.addEventListener('click', (event) => {
      const trigger = event.target.closest('[data-random-archive]');
      if (!trigger) return;
      event.preventDefault();
      const brand = document.querySelector('a.footer-brand');
      const rootPrefix = brand ? (brand.getAttribute('href') || '') : '';
      const current = (location.pathname.split('/').pop() || 'index.html').toLowerCase();
      let pick = current;
      while (pick === current && RANDOM_ARCHIVE_PAGES.length > 1) {
        pick = RANDOM_ARCHIVE_PAGES[(Math.random() * RANDOM_ARCHIVE_PAGES.length) | 0].toLowerCase();
      }
      location.href = rootPrefix + pick;
    });
  }

  // Initialize all components on DOM ready
  const runInit = () => {
    const contentArea = q('#content') || q('.wiki-content') || q('main');
    ensureHeadingIds(contentArea);
    initTableOfContents();
    initActionTabs();
    initFloatingToc();
    initHeadingPermalinks();
    initBackToTop();
    initSearch();
    initRandomArchive();
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', runInit);
  } else {
    runInit();
  }

})();
