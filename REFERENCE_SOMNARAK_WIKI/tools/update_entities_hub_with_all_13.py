import os

all_entity_cards = """
          <!-- SE-001 -->
          <div class="pm-entity-card" style="border:2px solid #38bdf8; background:#040d18;">
            <div class="entity-card-top">
              <img src="../assets/art/entities/se-001-icon.svg" alt="SE-001" class="entity-card-icon">
              <div class="entity-card-meta">
                <span class="risk-badge risk-PHANTASM">δ (PHANTASM)</span>
                <span class="damage-badge dmg-cyan">LAMENT DAMAGE</span>
                <div style="font-size:0.75rem; color:#f1df76; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 2 // MAW'S KEEP</div>
              </div>
            </div>
            <h3 class="entity-card-name" style="color:#38bdf8;">SE-001: THE ORPHANED BELL</h3>
            <p class="entity-card-desc">Ancient bronze resonance bell weeping liquid cyan Han tears. Emits cognitive shockwaves upon Coherence depletion.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:14px; display:flex; justify-content:space-between;">
              <span><b>DAMAGE:</b> <span style="color:#38bdf8;">LAMENT (SP)</span></span>
              <span><b>WORK:</b> INSIGHT (65%)</span>
            </div>
            <a href="se-001-the-orphaned-bell.html" class="jump-btn">OPEN FULL DOSSIER &amp; ASSETS →</a>
          </div>

          <!-- SE-002 -->
          <div class="pm-entity-card" style="border:2px solid #ef5b55; background:#0c080a;">
            <div class="entity-card-top">
              <img src="../assets/art/entities/se-002-icon.svg" alt="SE-002" class="entity-card-icon">
              <div class="entity-card-meta">
                <span class="risk-badge risk-PHANTASM">δ (PHANTASM)</span>
                <span class="damage-badge dmg-red">GRUDGE DAMAGE</span>
                <div style="font-size:0.75rem; color:#f1df76; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 2 // MAW'S KEEP</div>
              </div>
            </div>
            <h3 class="entity-card-name" style="color:#ef5b55;">SE-002: GRIEVING COLOSSUS</h3>
            <p class="entity-card-desc">Subterranean basalt titan weeping crimson sludge through cracked mask. Massive kinetic shockwave hazard.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:14px; display:flex; justify-content:space-between;">
              <span><b>DAMAGE:</b> <span style="color:#ef5b55;">GRUDGE (HP)</span></span>
              <span><b>WORK:</b> SUBJUGATION (60%)</span>
            </div>
            <a href="se-002-the-grieving-colossus.html" class="jump-btn">OPEN FULL DOSSIER &amp; ASSETS →</a>
          </div>

          <!-- SE-003 -->
          <div class="pm-entity-card" style="border:2px solid #38bdf8; background:#060e1f;">
            <div class="entity-card-top">
              <img src="../assets/art/entities/se-003-icon.svg" alt="SE-003" class="entity-card-icon">
              <div class="entity-card-meta">
                <span class="risk-badge risk-SOMNA">β (SOMNA)</span>
                <span class="damage-badge dmg-cyan">LAMENT DAMAGE</span>
                <div style="font-size:0.75rem; color:#f1df76; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 3 // EXTRACTION</div>
              </div>
            </div>
            <h3 class="entity-card-name" style="color:#38bdf8;">SE-003: THREAD OF MEMORY</h3>
            <p class="entity-card-desc">Ethereal azure loom piercing human consciousness with memory-weaving needles. Induces selective amnesia.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:14px; display:flex; justify-content:space-between;">
              <span><b>DAMAGE:</b> <span style="color:#38bdf8;">LAMENT (SP)</span></span>
              <span><b>WORK:</b> COMMUNION (70%)</span>
            </div>
            <a href="se-003-the-wilderness-tide.html" class="jump-btn">OPEN FULL DOSSIER &amp; ASSETS →</a>
          </div>

          <!-- SE-004 -->
          <div class="pm-entity-card" style="border:2px solid #f97316; background:#120804;">
            <div class="entity-card-top">
              <img src="../assets/art/entities/se-004-icon.svg" alt="SE-004" class="entity-card-icon">
              <div class="entity-card-meta">
                <span class="risk-badge risk-MORPHEAN">γ (MORPHEAN)</span>
                <span class="damage-badge dmg-red">GRUDGE DAMAGE</span>
                <div style="font-size:0.75rem; color:#f1df76; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 5 // BORDER WATCH</div>
              </div>
            </div>
            <h3 class="entity-card-name" style="color:#f97316;">SE-004: RUST-BLEEDING SENTRY</h3>
            <p class="entity-card-desc">Automaton sentinel weeping corrosive rust from ocular slits. High armor-penetration halberd attacks.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:14px; display:flex; justify-content:space-between;">
              <span><b>DAMAGE:</b> <span style="color:#ef5b55;">GRUDGE (HP)</span></span>
              <span><b>WORK:</b> SUBJUGATION (65%)</span>
            </div>
            <a href="se-004-the-rust-bleeding-sentry.html" class="jump-btn">OPEN FULL DOSSIER &amp; ASSETS →</a>
          </div>

          <!-- SE-005 -->
          <div class="pm-entity-card" style="border:2px solid #f1df76; background:#141004;">
            <div class="entity-card-top">
              <img src="../assets/art/entities/se-005-icon.svg" alt="SE-005" class="entity-card-icon">
              <div class="entity-card-meta">
                <span class="risk-badge risk-AETHER">α (AETHER)</span>
                <span class="damage-badge dmg-cyan">LAMENT DAMAGE</span>
                <div style="font-size:0.75rem; color:#f1df76; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 1 // NEUTRAL CORE</div>
              </div>
            </div>
            <h3 class="entity-card-name" style="color:#f1df76;">SE-005: SMOTHERING CRADLE</h3>
            <p class="entity-card-desc">Golden porcelain maternal effigy entwined in suffocating dark shrouds. Induces passive despair aura.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:14px; display:flex; justify-content:space-between;">
              <span><b>DAMAGE:</b> <span style="color:#38bdf8;">LAMENT (SP)</span></span>
              <span><b>WORK:</b> COMMUNION (80%)</span>
            </div>
            <a href="se-005-the-smothering-mother.html" class="jump-btn">OPEN FULL DOSSIER &amp; ASSETS →</a>
          </div>

          <!-- SE-006 -->
          <div class="pm-entity-card" style="border:2px solid #10b981; background:#041510;">
            <div class="entity-card-top">
              <img src="../assets/art/entities/se-006-icon.svg" alt="SE-006" class="entity-card-icon">
              <div class="entity-card-meta">
                <span class="risk-badge risk-SOMNA">β (SOMNA)</span>
                <span class="damage-badge dmg-black">WEIGHT DAMAGE</span>
                <div style="font-size:0.75rem; color:#f1df76; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 3 // EXTRACTION</div>
              </div>
            </div>
            <h3 class="entity-card-name" style="color:#10b981;">SE-006: SIPHON LEECH</h3>
            <p class="entity-card-desc">Predatory annelid siphon organism drinking subterranean effluent. Drains agent HP and SP concurrently.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:14px; display:flex; justify-content:space-between;">
              <span><b>DAMAGE:</b> <span style="color:#94a3b8;">WEIGHT (HP+SP)</span></span>
              <span><b>WORK:</b> EXTRACTION (70%)</span>
            </div>
            <a href="se-006-the-siphon-leech.html" class="jump-btn">OPEN FULL DOSSIER &amp; ASSETS →</a>
          </div>

          <!-- SE-007 -->
          <div class="pm-entity-card" style="border:2px solid #94a3b8; background:#080c14;">
            <div class="entity-card-top">
              <img src="../assets/art/entities/se-007-icon.svg" alt="SE-007" class="entity-card-icon">
              <div class="entity-card-meta">
                <span class="risk-badge risk-SOMNA">β (SOMNA)</span>
                <span class="damage-badge dmg-cyan">LAMENT DAMAGE</span>
                <div style="font-size:0.75rem; color:#f1df76; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 6 // DEEP VAULT</div>
              </div>
            </div>
            <h3 class="entity-card-name" style="color:#cbd5e1;">SE-007: ASHEN SCRIBE</h3>
            <p class="entity-card-desc">Spectral cloaked recorder engraving forgotten names upon basalt slates. Demands high mental fortitude.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:14px; display:flex; justify-content:space-between;">
              <span><b>DAMAGE:</b> <span style="color:#38bdf8;">LAMENT (SP)</span></span>
              <span><b>WORK:</b> INSIGHT (70%)</span>
            </div>
            <a href="se-007-brume.html" class="jump-btn">OPEN FULL DOSSIER &amp; ASSETS →</a>
          </div>

          <!-- SE-008 -->
          <div class="pm-entity-card" style="border:2px solid #ef4444; background:#140407;">
            <div class="entity-card-top">
              <img src="../assets/art/entities/se-008-icon.svg" alt="SE-008" class="entity-card-icon">
              <div class="entity-card-meta">
                <span class="risk-badge risk-PHANTASM">δ (PHANTASM)</span>
                <span class="damage-badge dmg-red">GRUDGE/LAMENT</span>
                <div style="font-size:0.75rem; color:#f1df76; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 6 // DEEP VAULT</div>
              </div>
            </div>
            <h3 class="entity-card-name" style="color:#ef4444;">SE-008: IRON MAIDEN OF REGRET</h3>
            <p class="entity-card-desc">Torture sarcophagus covered in weeping black thorns. Extracts concentrated agony from panicking agents.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:14px; display:flex; justify-content:space-between;">
              <span><b>DAMAGE:</b> <span style="color:#ef5b55;">GRUDGE/LAMENT</span></span>
              <span><b>WORK:</b> SUBJUGATION (65%)</span>
            </div>
            <a href="se-008-the-iron-maiden-of-regret.html" class="jump-btn">OPEN FULL DOSSIER &amp; ASSETS →</a>
          </div>

          <!-- SE-009 -->
          <div class="pm-entity-card" style="border:2px solid #0284c7; background:#04101e;">
            <div class="entity-card-top">
              <img src="../assets/art/entities/se-009-icon.svg" alt="SE-009" class="entity-card-icon">
              <div class="entity-card-meta">
                <span class="risk-badge risk-SOMNA">β (SOMNA)</span>
                <span class="damage-badge dmg-cyan">LAMENT DAMAGE</span>
                <div style="font-size:0.75rem; color:#f1df76; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 4 // INSIGHT FORGE</div>
              </div>
            </div>
            <h3 class="entity-card-name" style="color:#38bdf8;">SE-009: DROWNED BELL</h3>
            <p class="entity-card-desc">Aquatic bronze bell submerged in subterranean tears. Tolling underwater pulses erode agent SP.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:14px; display:flex; justify-content:space-between;">
              <span><b>DAMAGE:</b> <span style="color:#38bdf8;">LAMENT (SP)</span></span>
              <span><b>WORK:</b> COMMUNION (70%)</span>
            </div>
            <a href="se-009-the-memory-weaver.html" class="jump-btn">OPEN FULL DOSSIER &amp; ASSETS →</a>
          </div>

          <!-- SE-010 -->
          <div class="pm-entity-card" style="border:2px solid #f8fafc; background:#100c24;">
            <div class="entity-card-top">
              <img src="../assets/art/entities/se-010-icon.svg" alt="SE-010" class="entity-card-icon">
              <div class="entity-card-meta">
                <span class="risk-badge risk-APOCRYPHA">ε (APOCRYPHA)</span>
                <span class="damage-badge dmg-white">VOID DAMAGE</span>
                <div style="font-size:0.75rem; color:#f1df76; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 8 // GATE WATCH</div>
              </div>
            </div>
            <h3 class="entity-card-name" style="color:#f8fafc;">SE-010: THE CONVERGENCE</h3>
            <p class="entity-card-desc">Apocalyptic sphere of interwoven crowns and existential void eye. Breaching initiates facility-wide Efflorescence.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:14px; display:flex; justify-content:space-between;">
              <span><b>DAMAGE:</b> <span style="color:#ffffff;">VOID (% MAX HP)</span></span>
              <span><b>WORK:</b> RESTRAINT (30%)</span>
            </div>
            <a href="se-010-the-convergence.html" class="jump-btn">OPEN FULL DOSSIER &amp; ASSETS →</a>
          </div>

          <!-- SE-011 -->
          <div class="pm-entity-card" style="border:2px solid #ef4444; background:#140407;">
            <div class="entity-card-top">
              <img src="../assets/art/entities/se-011-icon.svg" alt="SE-011" class="entity-card-icon">
              <div class="entity-card-meta">
                <span class="risk-badge risk-PHANTASM">δ (PHANTASM)</span>
                <span class="damage-badge dmg-cyan">LAMENT DAMAGE</span>
                <div style="font-size:0.75rem; color:#f1df76; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 7 // SHADOW CORPS</div>
              </div>
            </div>
            <h3 class="entity-card-name" style="color:#ef4444;">SE-011: WHISPERING WALLS</h3>
            <p class="entity-card-desc">Living labyrinth bulkhead embedded with screaming faces and acoustic resonance baffles.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:14px; display:flex; justify-content:space-between;">
              <span><b>DAMAGE:</b> <span style="color:#38bdf8;">LAMENT (SP)</span></span>
              <span><b>WORK:</b> INSIGHT (60%)</span>
            </div>
            <a href="se-011-the-whispering-walls.html" class="jump-btn">OPEN FULL DOSSIER &amp; ASSETS →</a>
          </div>

          <!-- SE-014 -->
          <div class="pm-entity-card" style="border:2px solid #f1df76; background:#140c03;">
            <div class="entity-card-top">
              <img src="../assets/art/entities/se-014-icon.svg" alt="SE-014" class="entity-card-icon">
              <div class="entity-card-meta">
                <span class="risk-badge risk-APOCRYPHA">ε (APOCRYPHA)</span>
                <span class="damage-badge dmg-black">WEIGHT DAMAGE</span>
                <div style="font-size:0.75rem; color:#f1df76; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 6 // DEEP VAULT</div>
              </div>
            </div>
            <h3 class="entity-card-name" style="color:#f1df76;">SE-014: HOLLOW DEBT EATER</h3>
            <p class="entity-card-desc">Vested ledger beast swallowing transactional memory seals and agent emotional collateral.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:14px; display:flex; justify-content:space-between;">
              <span><b>DAMAGE:</b> <span style="color:#94a3b8;">WEIGHT (HP+SP)</span></span>
              <span><b>WORK:</b> RESTRAINT (40%)</span>
            </div>
            <a href="se-014-the-debt-eater.html" class="jump-btn">OPEN FULL DOSSIER &amp; ASSETS →</a>
          </div>

          <!-- SE-015 -->
          <div class="pm-entity-card" style="border:2px solid #f8fafc; background:#0c0a1f;">
            <div class="entity-card-top">
              <img src="../assets/art/entities/se-015-icon.svg" alt="SE-015" class="entity-card-icon">
              <div class="entity-card-meta">
                <span class="risk-badge risk-APOCRYPHA">ε (APOCRYPHA)</span>
                <span class="damage-badge dmg-white">VOID DAMAGE</span>
                <div style="font-size:0.75rem; color:#f1df76; font-family:'JetBrains Mono', monospace; margin-top:4px;">FLOOR 8 // GATE WATCH</div>
              </div>
            </div>
            <h3 class="entity-card-name" style="color:#f8fafc;">SE-015: SOVEREIGN DEBT SCALE</h3>
            <p class="entity-card-desc">Cosmic balance scale weighing human remorse against lead slates. Inflicts lethal existential erasure.</p>
            <div style="font-size:0.8rem; color:#94a3b8; font-family:'JetBrains Mono', monospace; margin-bottom:14px; display:flex; justify-content:space-between;">
              <span><b>DAMAGE:</b> <span style="color:#ffffff;">VOID (% MAX HP)</span></span>
              <span><b>WORK:</b> RESTRAINT (35%)</span>
            </div>
            <a href="se-015-the-debt-scale.html" class="jump-btn">OPEN FULL DOSSIER &amp; ASSETS →</a>
          </div>
"""

with open('/home/user/01_Somnarak_Wiki/entities/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
old_grid_pattern = r'<div class="hub-grid-3">[\s\S]*?<\/div>\s*<\/div>\s*<!-- Master Footer'
replacement = '<div class="hub-grid-3">' + all_entity_cards + '        </div>\n      </div>\n\n      <!-- Master Footer'

new_html = re.sub(old_grid_pattern, replacement, html)
with open('/home/user/01_Somnarak_Wiki/entities/index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print('SUCCESS: Updated entities/index.html with all 13 canonical cards!')
