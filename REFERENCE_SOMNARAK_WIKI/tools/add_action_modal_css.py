import os

css_modals = """
/* ==========================================================================
   INTERACTIVE [VIEW SOURCE] & [HISTORY] TERMINAL MODAL STYLES
   ========================================================================== */
.action-btn, .page-action-btn {
  display: inline-flex !important;
  align-items: center !important;
  gap: 6px !important;
  background: rgba(15, 23, 42, 0.9) !important;
  border: 1.5px solid #223854 !important;
  color: #94a3b8 !important;
  padding: 4px 12px !important;
  border-radius: 4px !important;
  font-family: 'JetBrains Mono', 'Courier New', monospace !important;
  font-size: 0.78rem !important;
  font-weight: 700 !important;
  cursor: pointer !important;
  transition: all 0.2s ease !important;
  user-select: none !important;
}

.action-btn:hover, .page-action-btn:hover {
  background: #1e293b !important;
  border-color: #f1df76 !important;
  color: #f1df76 !important;
  box-shadow: 0 0 10px rgba(241, 223, 118, 0.35) !important;
}

.wiki-action-modal {
  display: none;
  position: fixed;
  inset: 0;
  z-index: 1000;
  align-items: center;
  justify-content: center;
}

.wiki-action-modal.open {
  display: flex !important;
}

.action-modal-backdrop {
  position: absolute;
  inset: 0;
  background: rgba(2, 4, 8, 0.85);
  backdrop-filter: blur(4px);
}

.action-modal-dialog {
  position: relative;
  z-index: 1001;
  width: min(840px, 92vw);
  max-height: min(720px, 86vh);
  background: #060a12;
  border: 2px solid #38bdf8;
  border-radius: 8px;
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.95), 0 0 25px rgba(56, 189, 248, 0.35);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  animation: modalFadeIn 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes modalFadeIn {
  from { opacity: 0; transform: scale(0.96) translateY(10px); }
  to { opacity: 1; transform: scale(1) translateY(0); }
}

.action-modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 18px;
  background: linear-gradient(90deg, #0e1726 0%, #080d16 100%);
  border-bottom: 1.5px solid #1e293b;
}

.action-modal-title {
  display: flex;
  align-items: center;
  gap: 10px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.95rem;
  color: #f1df76;
  letter-spacing: 0.08em;
}

.modal-status-led {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #71efaf;
  box-shadow: 0 0 8px #71efaf;
}

.action-modal-close {
  background: none;
  border: 1px solid #334155;
  color: #94a3b8;
  font-size: 1rem;
  cursor: pointer;
  padding: 2px 8px;
  border-radius: 4px;
  transition: all 0.15s ease;
}

.action-modal-close:hover {
  background: #ef5b55;
  color: #fff;
  border-color: #ef5b55;
}

.action-modal-body {
  flex: 1;
  overflow-y: auto;
  padding: 18px;
  background: #03060a;
}

.action-modal-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 18px;
  background: #080d16;
  border-top: 1.5px solid #1e293b;
}

.modal-clearance-tag {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.72rem;
  color: #64748b;
  font-weight: 700;
}

.modal-btn-copy {
  background: #1e3a5f;
  border: 1px solid #38bdf8;
  color: #38bdf8;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.78rem;
  font-weight: 700;
  padding: 6px 14px;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.modal-btn-copy:hover {
  background: #38bdf8;
  color: #040810;
  box-shadow: 0 0 10px rgba(56, 189, 248, 0.5);
}

/* Terminal Source View Block */
.terminal-source-view {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.source-info-bar {
  display: flex;
  justify-content: space-between;
  font-family: 'Courier New', monospace;
  font-size: 0.75rem;
  color: #64748b;
  padding-bottom: 6px;
  border-bottom: 1px solid #1e293b;
}

.source-code-block {
  background: #020408;
  border: 1px solid #1e293b;
  padding: 14px;
  border-radius: 4px;
  overflow-x: auto;
  font-family: 'JetBrains Mono', 'Courier New', monospace;
  font-size: 0.8rem;
  color: #71efaf;
  line-height: 1.5;
  max-height: 440px;
}

/* Cycle History Cards */
.cycle-history-timeline {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.history-card {
  background: #080e18;
  border: 1.5px solid #1e293b;
  border-left: 4px solid #64748b;
  border-radius: 4px;
  padding: 12px 16px;
}

.history-card.active-rev {
  border-left-color: #f1df76;
  background: #0d1626;
  box-shadow: 0 0 12px rgba(241, 223, 118, 0.15);
}

.history-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 6px;
}

.rev-badge {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.76rem;
  font-weight: 800;
  color: #94a3b8;
  background: rgba(255, 255, 255, 0.06);
  padding: 2px 8px;
  border-radius: 2px;
}

.rev-badge.rev-current {
  color: #f1df76;
  background: rgba(241, 223, 118, 0.12);
  border: 1px solid rgba(241, 223, 118, 0.3);
}

.rev-date {
  font-family: 'Courier New', monospace;
  font-size: 0.72rem;
  color: #64748b;
}

.rev-desc {
  font-size: 0.82rem;
  color: #cbd5e1;
  line-height: 1.4;
  margin: 0 0 6px 0;
}

.rev-meta {
  font-family: 'Courier New', monospace;
  font-size: 0.7rem;
  color: #38bdf8;
}
"""

with open('/home/user/01_Somnarak_Wiki/assets/css/wiki.css', 'a', encoding='utf-8') as f:
    f.write('\n' + css_modals.strip() + '\n')

print('SUCCESS: Appended interactive modal and action-btn styles to wiki.css!')
