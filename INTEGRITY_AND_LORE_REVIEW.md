PRIORITY 1 - CANON CONFLICTS

V5-1. Dawn of Mourning has two different HP values

SOMNARAK-WORLD/Sorrow_Entities/SE-C-Vω-002_Dawn_of_Mourning_애도의_여명.md, line 59, says 12,000/12,000.
SOMNARAK-WORLD/MAW_Codex_Sets/Registry_043_to_055/044_Dawn_of_Mourning/SE-044-A__SIDE_CODEX_Dawn_of_Mourning.md, line 25, says 1200/1200. The CHANGELOG also says "Dawn 1,200".
The rules doc now calls 12,000 "a documented outlier", but the side codex still disagrees.
Fix: choose one value and make the dossier, the side codex and the CHANGELOG match. The other 72 of 73 side codices already match their dossiers.
V5-2. Year 4,233 versus 4,238, and other timeline mismatches (V1-F residue)
The status note says the Absolvohan end-year mismatch is "already bridged". It is not. CANON_TIMELINE.md (lines 61 and 110) and The_REVERIE_DIRECTORATE.md (lines 330 and 2946) put the Hand of Hope and the end of Cycle 1,778 in Year 4,238. Other files put them in 4,232–4,233.

The_Absolvohan/README.md, lines 52 and 231, says "Post-Loop Calendar Year 4,233" and that the loop "breaks into Year 4,233".
The_Absolvohan/Part_9_Days_350_to_365.md says Year 4233 at lines 448, 508 and 881.
The_Absolvohan/ABSOLOVHAN_OVERVIEW.md says "Dawn of Year 4,233" at lines 1633 and 1640.
Master_Codices/02_Institutional_Wings_and_Chronicles/The_UNDERWORLD_CLEANUP_DESCEND.md, near lines 486–492, says Year 4,232 "Absolvohan fires; 15% converted to Hope" and Year 4,233 "Katharcheok Campaign executed". The timeline says the UCD ran Years 3,973–4,039.
The_SOMNARAK_EXPLORATION_DECREE.md, near lines 548–566, says Year 4,233 "Katabagil Descent executed; Seven Passages completed". The timeline says the SED descents ran Years 2,460–3,970. The same table also says Year 4,247 for the Nadir.
Also check Part 9 line 448, "the year 4232+1778 is over". It reads as a garbled year.
Fix: decide whether the loop ends and the Hand of Hope opens in Year 4,233 or 4,238. Then make the timeline, the Absolvohan, the UCD codex and the decree codex agree, and keep the SED and UCD dates consistent with the timeline.
PRIORITY 2 - DOCS THAT DISAGREE WITH THE ARCHIVE

V5-3. "292" remains in live docs
The status note says these files have no "292". They do. Change all to 291.

SOMNARAK-WORLD/Unknown_Entities/README.md, line 13
SOMNARAK-WORLD/README_FIRST.md, line 33. It also says "over 1,700 technical files", so update that number too.
SOMNARAK-WORLD/Tactical_Combat_Engine/WHAT_CAN_BE_DONE.md, line 61
SOMNARAK-WORLD/Pages/42-Navigation.md, line 15 ("292 Sorrow Entities (285 SECC) - 88 Relics", which also needs checking against the 284-indexed catalog) and line 84
Optional, historical: REFERENCE_SOMNARAK_WIKI/WIKI_PARTS_SOMNARAK_WORLD.md (lines 6, 45 and 104) and WIKI_PARTS_ABNORMALITIES.md (line 97)
V5-4. Root README and the audit still have old counts

README.md, line 32, says "44 In-Universe Master Codices". Master_Codices/ holds 49 files, and the audit reports 49 in-world plus 3 editorial.
README.md, line 91, says "(12 Volumes)". Everywhere else says 16.
tools/audit_lore_archive.py has a stale constant. It expects 35 and finds 52, so the printed line reads "52 / 35 master codices", and the docstring at line 67 still says "35 foundational reference codices (32 + 3)". The status note says that string is absent repo-wide, but it is built at runtime (line 318). Update the expected count and the docstring.
V5-5. The ID letter is defined wrongly
File: SOMNARAK-WORLD/Sorrow_Entities/README.md, about lines 18–32.
It defines [M] as Manifestation Class (C Concrete, N Non-physical, A Abstract). The files and the audit use C = City, N = Inner Sorrow, O = Outside Sorrow. Rewrite it.

V5-6. The catalog uses Project Moon risk names
File: REFERENCE_SOMNARAK_WIKI/SORROW_ENTITIES_CATALOG.md. There are 204 hits for ZAYIN, TETH, HE, WAW and ALEPH. Either replace them with Residue, Echo, Fragment, Entity and Sovereign, or whitelist the folder in the vocabulary policy.

V5-7. The HP anchors in the rules doc are not literally true
File: SOMNARAK-WORLD/Tactical_Combat_Engine/ACTION_DICE_AND_CLASH_RULES.md, line 106.
"Rank IV dossiers run 600–950" is wrong. The measured range is 390–1,000, with a median of about 824 across 80 dossiers. Rank V runs from 521 to 12,000. Change the wording to the real range, or say "typically 600–950 with outliers".

V5-8. The Transform line wording is implicit
The rules doc never writes "at or below 15". It says "15 — onset begins" and "recovery above 15 arrests onset". Add the explicit phrase so it matches the Junior Warden at exactly 15 in Descent 5.

PRIORITY 3 - LINT AND TOOL GAPS

V5-9. Nothing prevents the old rank names from coming back
Add a seam_lint rule that flags Wail, Whisper or Murmur next to "Rank" or a Roman numeral. Whitelist the deprecation note in SOMNARAK_ENTITY_CODEX.md (line 59).

V5-10. The path lint skips the places that had broken references
tools/seam_lint.py, lines 65–70, still skips docs/, TEMPLATES/, REFERENCE_*, tools/ and DEVELOPMENT.md. Remove docs/ and DEVELOPMENT.md from the skip list, since people read them.

V5-11. The timeline lint can't catch chronology conflicts like V5-2
It passes all 1,794 files while 4,232/4,233 conflicts exist. Add a rule that flags "Year 4,233" and "Year 4,232" when they appear in the same sentence as Hand of Hope, Dawn, Absolvohan fires or loop ends. Also flag any SED or UCD campaign dated after Year 4,200.

PRIORITY 4 - CONTENT SHAPE (deferred by you; the repo marks these "no targets set")

I suggest measurable targets below.

V5-12. Dossier boilerplate (V1-I)
About 36.8% of lines are shared by 30 or more dossiers. Suggested target: under 25%.

V5-13. The Absolvohan is mostly logs (V3-N7)
Story is about 5% of the text and gameplay logs are about 95%. The "sampled days" note explains the format but doesn't change the ratio. Suggested target: add narrative scenes for the key days, or set an explicit ratio goal, for example 15% story.

V5-14. Dossier length is flat by rank (V3-N8)
Every rank has a median of about 4,700–5,100 words. Suggested target: Rank I about 2,500–3,000 words, Rank II about 3,500, Rank IV about 5,500, and Rank V about 7,000 or more.

V5-15. Ordeal polish (optional)
The Ordeals now meet the depth bar. Each one still keeps its old template lead sentence, and the unique-line share is about 24%. For example, two files still contain "Engage with major-appropriate teams. Mixed-element M.A.W. recommended". A final pass could reword those lead sentences.

V5-16. Process (your decision)
main is still at 8f7138fb, and all the work is only on the arena branch (open PR #11). Decide when to merge.
