V5 PREVIEW RESULT

DONE AND VERIFIED

V5-1: Dawn of Mourning is 12,000 in both the dossier and the side codex, and the CHANGELOG is corrected.
V5-2: The loop end and Hand of Hope are Year 4,238 everywhere, including the Absolvohan README and Part 9. UCD is 4,039 and the Katabagil descent is 3,970. Lint guards C1 and C2 were added.
V5-5: The ID letter definition in Sorrow_Entities/README.md now says City/Outside/Inner.
V5-6: The catalog has no risk names left.
V5-7: The rules doc now says Rank IV runs 390–1,000.
V5-8: The rules doc now says "At or below 15".
V5-9, V5-10 and V5-11: The retired-rank lint, the path lint (now covering docs/ and DEVELOPMENT.md) and the chronology lint are all in.
V5-13: Story share in the Absolvohan is about 12–15%. There are 38 new interludes of about 500 words each, and 0% of their sentences are reused.
V5-15: All 60 Ordeals have unique leads.
V5-14, partly: The length ladder exists, with medians of I 4,872, II 5,022, III 5,270, IV 5,533 and V 7,042. The 13 Rank V chronicles are bespoke (0% reused).
NOT DONE OR PARTLY DONE

V5-3: "292" is still in a couple of live docs (V6-4).
V5-4: one "44" remains in the root README (V6-4).
V5-12: it is a regression, not a fix (V6-1 and V6-2).
V5-14: the Rank II–IV additions are recycled stories (V6-3).
V5-15: one Ordeal still has the old text (V6-5).
V5-16: main is unchanged (V6-7).
V6 - FIX LIST (Project Somnarak)

PRIORITY 0 - BROKEN BUILD

V6-1. The V5-12 name-slotting broke the dossier field labels, and CI is red

It added "(Entity Name)" to table labels. Example in SE-C-IIIγ-081_The_Hollow_Saint: "Sorrow Category (The Hollow Saint)" and "Movement (The Hollow Saint)". The **Mechanics Reference (The Hollow Saint):** callout got the same treatment.
About 7,275 labels in 282 dossier files are affected.
The audit looks for "Sorrow Category" exactly. It now reports "282 scope mismatches" and a FAIL.
It also appended code tags to sentences, such as "...behavior. [SE-C-IIIγ-081]". There are about 2,007 of them across 287 files, and 4 Unknown_Entities files are affected.
Fix: revert both changes. Remove " (Entity Name)" from every table label and callout label, and remove the trailing " [SE-code]" tags. Then re-run all five tools before pushing. The Sorrow Category field must match the filename prefix again.
V6-2. The boilerplate is not actually fixed

The "39% → 2%" figure comes from making lines differ by their labels and name tags.
With labels, tags and names stripped, the shared-line share is about 41.7%, the same as before.
Fix: stop decorating labels. Rewrite the repeated prose lines in Behavior, Combat, Testimonium and Interactions so they differ in substance.
Count the table labels as fixed template structure, and measure only prose lines. Suggested target: under 25% shared prose.
Correct the CHANGELOG V5-12 claim, which currently says "~39% to ~2%".
PRIORITY 1 - CONTENT QUALITY

V6-3. The "length ladder" is padded with recycled stories

## Apex Record (80 Rank IV files, about 733 words each), ## Warden Record (82 files, about 327 words each) and ## Watch Record (70 files, about 166 words each) are built from about 10 story templates per section.
Each template is reused across about 8 entities with the name swapped. 93–96% of their sentences appear in 3 or more files.
Example: the "unfiled watch log in the commander's drawer" paragraph appears word for word in 6 Rank IV dossiers.
Fix: write unique content for each entity, or keep these as a few shared annex documents that the dossiers link to. Don't copy them 8 times.
The lower ranks are also still long (Rank I median about 4,900 words). I originally suggested shorter low ranks, which would make the ladder real.
PRIORITY 2 - STALE REFERENCES

V6-4. Leftover counts

SOMNARAK-WORLD/Pages/README.md, line 64: "292 containment records".
SOMNARAK-WORLD/Pages/01-Main Page.md, line 42: "all 292 crystallized sorrows" and "all 285 unique SECC codes". Change them to 291, and check the 285 against the 284-indexed catalog.
README.md, line 108: "44 Macro-Canon Master Codices". Change it to 49. Line 32 is already fixed.
Optional (historical): 7 lines of "292" in REFERENCE_SOMNARAK_WIKI/*.
V6-5. One Ordeal still has the old template line
SOMNARAK-WORLD/Ordeals/Ordeal_PURPLE_Third_Watch_The_Bloom_Hosts.md still contains "Engage with major-appropriate teams. Mixed-element M.A.W. recommended". Rewrite it like the other 59.

PRIORITY 3 - PROCESS AND LINT

V6-6. Prevent this kind of regression

Run the full gate set (audit, box, timeline, seam, links, tests) before every push. The V5-12 push failed the audit and still went out.
Add a lint that dossier table labels must come from a fixed list and may not contain parentheses with the entity name.
Add a lint that flags a trailing "[SE-…]" tag after a sentence.
V6-7. Process decision (yours)
main is still at 8f7138fb, and the arena branch is still ahead in open PR #11. Decide when to merge. I would wait until V6-1 is fixed and CI is green.
