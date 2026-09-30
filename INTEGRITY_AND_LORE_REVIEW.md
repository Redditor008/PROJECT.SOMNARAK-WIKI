V1–V4 MISSED FIXED LIST

Items marked PARTIAL are also listed here, because they aren't fully fixed.

V1 - NOT FIXED

V1-D (NOT FIXED). The First Tear and Forgotten God ages still conflict.

Descent_4_The_Tear.md, line 100, still says "four billion years of oldest grief".
Descent_5_The_Waking.md, line 119, still says the God sat "for the first time in four thousand years".
The dossiers SE-C-Vδ-290 (Tear) and SE-C-Vδ-265 (God) say six thousand years and six millennia.
Six thousand years is also longer than the timeline allows, since the world is only about 4,238 years old.
Fix: pick one age that fits the timeline, at most 4,238 years. Then change Descent 4, Descent 5 and both dossiers to match. The added "record split" note explains Tear versus God. It doesn't settle the ages.
Other "six thousand years" lines to check: Absolvohan/Part_8_Days_149_to_177.md line 955, Unknown_Entities/SE-C-IIIγ-248 and SE-N-IVδ-901.
V1-E (NOT FIXED). The timeline now contradicts itself on Cycle versus Year.

A new note in CANON_TIMELINE.md says no Cycle-to-Year conversion exists except Cycle 1,778 = Year 4,238.
Line 53 still pairs "Year 3,972" with "Cycle 1,512". Line 60 says 1,778 cycles last about 6 external years.
Fix: remove or reword the "Cycle 1,512" pairing on line 53. It appears in both copies of the timeline.
V1-F (NOT FIXED). The SED dates still disagree between documents.

The_SOMNARAK_EXPLORATION_DECREE.md (chronology near lines 548–566) says Year 1,840 for the SED mandate, Year 4,232 for the Absolvohan activating, Year 4,233 for the Katabagil descent, and Year 4,247 for the Nadir.
CANON_TIMELINE.md says SED descents ran Years 2,460–3,970, but the decree that created SED came around Year 4,200 (a 1,700-year gap).
The Absolvohan README and Part 9 end at Year 4,233, but the timeline puts the Dawn at 4,238.
The new note in GAME_BATTLE Scenario 04 ("Year Zero = MMSS 2460") doesn't reconcile any of these.
Fix: choose one SED chronology and make the decree codex, the timeline, Scenario 04 and the Absolvohan end-year agree.
V1-H (PARTIAL). The 999 placeholder HPs are all fixed, and the lint rule was retired. Two small things remain.

The Walking Calendar dossier (SE-C-IVδ-220, line 17) still says "Movement: Stationary — a device", yet its own text says "each step adding another year" and "lead-heavy and slow". Change the movement field to match the description.
tools/banned_strings.txt line 23 still bans "Year 4247", although the lint rule that used it was retired and several codices legitimately use 4247.
V1-I (PARTIAL). Dossier boilerplate fell from 41% to about 37%. It is still high.

V2 - NOT FIXED

V2-God age (NOT FIXED). This is the same problem as V1-D.

V2-Thin Ordeals (PARTIAL). 20 of the 60 Ordeals are now deep: the 10 Tide Watch files and the 10 in batch 1 of the new deepening work. The other 40 are still about 950 words. That work is in progress, so this is for your tracking only.

V3 - NOT FIXED

V3-N2 (PARTIAL). 19 serial numbers still repeat within a prefix letter. This is documented in the Entity Codex, but the SOMNARAK_DOCUMENT_RULES.md ID section is still wrong. It still uses the old SE-[Number] format.

V3-N4 (PARTIAL). The entity counts are fixed in the catalog and the timeline, but "292" is still in these files:

TEMPLATES/00, 01, 08, 19 and 23
Unknown_Entities/README.md
WHAT_CAN_BE_DONE.md
README_FIRST.md
SOMNARAK-WORLD/README.md, which also says "159 City" instead of 158
The root README.md also still says "44 codices", "1,706 files" next to "1,897", and "12-volume" next to "16 volumes". The audit's "52 / 35" expected-count line looks out of date too.

V3-N7 (PARTIAL). A "sampled days" note and a Quiet Season bridge were added, but story is still about 4.7% of the Absolvohan.

V3-N8 (PARTIAL). Six Sovereign dossiers were expanded, but the median length is still flat across ranks, about 4,700–5,100 words.

V3-N9 (PARTIAL). The ranks are correct in Master_Codices/README.md. THE_HAND_DR_LAYOUT.svg still shows Three Birds as RANK IV (should be III) and Smothering Mother as RANK III (should be IV).

V3-N10 (NOT FIXED). This is a process item for you. main is still at 8f7138fb, and the work is only on the arena branch.

V4 - NOT FIXED

V4-W1 (PARTIAL). The canonical rank names are in almost every file, but two "Wail" leftovers remain.

Pages/38-Classification Code.md, line 60, says "IV — Wail". It should say Entity.
Descent_4_The_Tear.md, line 48, says "Wail rank". It should say Entity.
V4-W6 (PARTIAL). The Transform line is in the rules doc. The rules say "at 15, onset begins", but the Junior Warden sits at exactly 15 SP in Descent 5 with no onset effects. Decide whether the line means "15 or below" or "below 15", and make the rules doc or Descent 5 match.

---

## Addendum — Link-Integrity Re-verification (2026-09-30, commit-tracked)

Fresh automated sweep with new repo-native checker `tools/check_links.py`
(inline links/images; resolves files + anchors; skips fenced blocks and
inline code spans holding intentional verbatim `URL`/`...`/`wiki.gg`
examples in REFERENCE and TEMPLATES).

- **Scope:** 2715 links across 1877 markdown files.
- **Baseline:** 16 broken — 3 canonical missing-anchor slugs (stale TOC
  text), 13 verbatim-in-code examples (tool now skips).
- **Fixes applied:**
  - `SOMNARAK-WORLD/Pages/17-Pressure Types.md`: `#3-pale-...` →
    `#3-void-conceptual-scaling-the-one-percent-axiom`.
  - `SOMNARAK-WORLD/Pages/19-Lumen Surge.md`: `#2-extraction-physics-...-ticks`
    → `#2-extraction-physics-positive-vs-negative-boxes`.
  - `SOMNARAK-WORLD/Pages/30-Overview.md`: `#4-the-four-observation-levels-...`
    → `#4-the-four-comprehension-levels-and-codex-progression`.
- **Post-fix result:** **BROKEN TOTAL: 0** (exit 0; negative control with a
  planted broken link exits 1 with detail output).
- **Cross-claim spot checks:** entity total 291 = 158 canonical + 61 other +
  72 non-SE; `Absolovhan` 8/8 occurrences intentional (5x `[sic]` decree
  quotes, CHANGELOG Finding-5 meta, review row, `ABSOLOVHAN_OVERVIEW.md:3`
  documented dual-spelling nomenclature note); `Absolvohan` 610 uses.
- **Durability:** `tools/check_links.py` added as a CI gate step in
  `.github/workflows/ci.yml` ("Verify Internal Link Integrity"), failing
  the build on any future broken link.

---

## Fix Status — V1–V4 Missed List (2026-09-30/10-01, commits 09d517f8 + pending)

FIXED & PUSHED (`09d517f8`, round 1):
- V1-E: Cycle-1,512 pairing reworded in both timeline copies (no calendar conversion implied).
- V1-H: Walking Calendar movement → Slow Walking; `Year 4247` removed from banned_strings (no live rule consumed it; tests green).
- V3-N2: RULES ID section rewritten to canonical `SE-[Origin]-[Coherence][Potency]-[Number]` + serial-slot semantics (authority: Entity Codex).
- V3-N4: 292→291 (TEMPLATES x5, WORLD README x2 + 159→158 City), 44→49 codices (WIKI_PARTS x2), root README 12→16-volume (x2) + 1,706→1,897 files.
- V3-N9: SVG ranks swapped (Three Birds III, Smothering Mother IV).
- V4-W1: both Wail→Entity. Other `Wail` hits are skill/attack names, not ranks — kept.
- V4-W6: rule ("at or below 15") stands; Descent 5 now shows Junior Warden onset + Transform scar.

FIXED THIS ROUND (round 2):
- V1-D + V2-God age: GLOBAL six→four thousand years / six→four millennia (143 replacements, 55 files); D4 billion→thousand. Face/family counts in Ocean ordeal + review/CHANGELOG history untouched.
- V1-F: 1,840 mandate stands; ~4,200 reworded as re-charter in both timelines + PROJECT_SOMNARAK + REVERIE_DIRECTORATE + AUDIT (prose + 71-col box, width preserved).

VERIFIED STALE / NO ACTION:
- V2-Thin Ordeals: all 60 ≥1224w (floor was 1197 at batch-5 push; review's "40 still ~950" predates completion).
- V3-N4 sub-claims: Unknown_Entities/README, WHAT_CAN_BE_DONE, README_FIRST have no "292" (already clean); audit "52/35" string absent repo-wide.
- V1-F sub-claim: Absolvohan end 4,233 vs Dawn 4,238 already bridged in Absolvohan README (loop ends 4,233; Dawn Initiative 4,238 carries remaining 85%).
- V3-N10: user-side process item (merge to main).

DEFERRED (per user 2026-10-01): V1-I, V3-N7, V3-N8 metric trio — no targets set.
