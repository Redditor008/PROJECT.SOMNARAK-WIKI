PROJECT.SOMNARAK-WIKI — Post-Remediation Integrity & Lore Review
Commit: e1abd9b | Date: 2026-09-25 | 1,980 files | 3,432,088 words
EXECUTIVE SUMMARY
The remediation commit addressed 16 of 22 items from the original review. Nine findings are fully resolved, three are partially resolved, and one critical issue remains outstanding (the ././ path bug causing 989 broken links). The built-in audit suite passes clean. Lore consistency remains excellent.

Category	Status
Built-in Audit (audit_lore_archive.py)	✅ PASS (all 6 categories)
Structural Findings Resolved	9/14 fully fixed
Structural Findings Outstanding	5 (1 critical, 2 medium, 2 low)
Lore Observations	✅ All 8 confirmed + enhanced
VERIFIED FIXES (9 findings confirmed resolved)
Finding 2 — Broken README/DEVELOPMENT References ✅ FIXED
File	Before	After
README.md	10 broken refs	0 broken refs
DEVELOPMENT.md	5 broken refs	0 broken refs
All file paths now match disk-verified filenames (Passage_1_Cryptasu, Arc_1_Departure, Operation_1_Velumtal, etc.). Codex paths include full subdirectory structure.

Finding 3 — MAW Registry Gaps ✅ DOCUMENTED
Added ## Registry Numbering Gaps & In-Universe Lore Rationale to SOMNARAK-WORLD/MAW_Codex_Sets/README.md with three canonical explanations:

Classified & Expunged Entity Husks — sealed under Class-V archival locks
Directorate Extraction Prohibitions (Directive 14-C) — metaphysical rejection
Alternative Workshop Routing — Six Great Workshops (Sump-Wrench Guild, Ashlar Foundries, Giltong Weavers)
Finding 4 — Entity-MAW Orphans ✅ DOCUMENTED
Registry_1001_to_1043 = formal ID collision resolution tier (SE-1001 maps to SE-C-Iα-000, SE-1002 to C-IIIγ-044, etc.)
SE-072, 114, 319, 412, 515 = classified as A-Relic (Arcanum) single-dossier integrated entities with MAW specs embedded directly in their primary dossiers
Finding 5 — "Absolovhan" Misspelling ✅ ANNOTATED
All instances now carry [sic, Absolvohan] markers:

text

"...R.D. + Absolovhan [sic, Absolvohan] So no Mention..."
Dual-nomenclature indexing added to ABSOLOVHAN_OVERVIEW.md.

Finding 6 — Undocumented "N" Scope ✅ DOCUMENTED
Added to both README.md and DEVELOPMENT.md:

text

Origin Scope Taxonomy (발생 기원 체계):
  Scope C: City Sorrow (도한/Dohan) — institutional
  Scope N: Inner Sorrow (내한/Naehan) — personal/psychological
  Scope O: Outside Sorrow (외한/Oehan) — wilderness/environmental
Finding 7 — Absolvohan Day Gap ✅ NARRATIVE BRIDGE ADDED
"The Quiet Season" (침묵의 계절, Days 178–349) documented in SOMNARAK-WORLD/The_Absolvohan/README.md:

Post-venting hydraulic stabilization after Day 160
Majin's pivot from mass accumulation to emotional resonance cultivation
Cheonbulok refugee children's visits sowing the 12th blessing
Seamless bridge into Part 9 (Days 350–365)
Finding 8 — HT-001/HT-002 ✅ VERIFIED DISTINCT
HT-001_The_Guiding_Light (Yeonhwa, HT-IV-HL-001) and HT-002_The_Shield_of_Dawn (Taeho, HT-IV-HS-002) confirmed as separate, correctly labeled entities.

Finding 13 — O-V Rarity ✅ DOCUMENTED
Added archival distribution note to entity codex:

"Beyond the city walls, macro-scale planetary geography absorbs environmental pressure, yielding exactly one documented Outside Sovereign (SE-O-Vγ-003 Wilderness Tide). Because Inner Sorrow originates from individual human psyche, personal trauma cannot reach Sovereign Rank V without metastasizing into collective City Sorrow, resulting canonically in zero N-V entities."

OUTSTANDING ISSUES (5 items remaining)
🔴 CRITICAL: ././ Path Bug — 989 Broken Links
Status: NOT FIXED | Impact: 77% of all remaining broken links

Two files use ././Sorrow_Entities/... instead of ../Sorrow_Entities/...:

File	Broken Links	Pattern
SOMNARAK_MAW_CODEX.md	735	././Sorrow_Entities/SE-...
SOMNARAK_ENTITY_CODEX.md	254	././Sorrow_Entities/SE-...
Total	989	
Fix (one-liner per file):

Bash

sed -i 's|\./\./Sorrow_Entities/|../../Sorrow_Entities/|g' \
  SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_MAW_CODEX.md \
  SOMNARAK-WORLD/Master_Codices/05_Entities_Tales_and_Fractures/SOMNARAK_ENTITY_CODEX.md
🟡 MEDIUM: Hangul Inside Text Boxes — 720 Instances (64 Files)
Status: DISPUTED | Remediation claims: These are markdown tables, not true ASCII boxes

My scanner tracks +===+/+---+ border state transitions and flags Hangul between them. The top offenders:

File	Instances	Likely Type
SOMNARAK_CAST.md	115	Markdown table inside box
The_REVERIE_DIRECTORATE.md	108	Markdown table inside box
COMPLETE_SYSTEM_COMPARISON	59	Comparison table (may be exempt)
ABSOLOVHAN_OVERVIEW.md	36	Mixed
60 other files	302	Various
Key question: If these are standard | Key | Value | markdown tables rendered inside GitHub (not monospace ASCII boxes), they are not violations — Korean terms are appropriate in structured data. The rule targets monospace ASCII art boxes only.

Recommendation: Clarify in the standards document whether the Hangul rule applies to (a) only +---+ bordered ASCII boxes, or (b) all tabular structures including markdown tables.

🟡 MEDIUM: CHANGELOG.md & SESSION_BREAK_PRECAUTION.md — 58 Broken Refs
File	Broken Refs	Cause
CHANGELOG.md	45	References to renamed/restructured files
SESSION_BREAK_PRECAUTION.md	13	References to deleted audit tools
These are historical records documenting what was done at the time — the references were correct when written. Options:

Update refs to current filenames (preserves link functionality)
Leave as-is (they're historical records)
Add footnote: "References reflect file names at time of entry"
🔵 LOW: README Codex Count Still Says 38
Actual: 44 Master Codices (confirmed by audit tool and manual count)

The README says "38 In-Universe Master Codices across 6 canonical subfolders" in multiple places. Should be updated to 44.

🔵 LOW: 3 Duplicate File Groups
Files	Status
CANON_TIMELINE.md = Master_Codices/01_.../CANON_TIMELINE.md	Byte-identical
COMPLETE_SYSTEM_COMPARISON.md = Master_Codices/06_.../COMPLETE_SYSTEM_COMPARISON.md	Byte-identical
docs/FRONT_HOME_PAGE_SPECIFICATION.md = docs/README.md	Byte-identical
Root copies exist for navigational convenience. The docs/ duplication may be accidental.

BUILT-IN AUDIT RESULTS
text

1. UTF-8 Integrity        : PASS (1,785 files, 22.01 MB)
2. Macro-Canon Codices    : PASS (47 / 35 master codices: 44 in-world, 3 editorial)
3. Sorrow Entities        : PASS (292 files, 292 unique codes, 0 paired)
   Rank breakdown         : {I:46, II:70, III:82, IV:79, V:10, Other:5}
4. M.A.W. Equipment Sets  : PASS (198 / 198 complete quadripartite sets)
5. Auxiliary Collections  : PASS
   - Absolvohan: 10 | Katabagil: 8 | Katharcheok: 7
   - Gieok Jeojangso: 8 | Jipyeongseondae: 7 | Mugenhan Ecology: 5
   - Ordeals: 60 | Hope Transformations: 14 | Unknown: 12 | Echo-Cores: 9
6. Text Box Symmetry      : PASS (1,785 files, 0 crooked rows)

OVERALL LORE HEALTH: PASS
VERIFIED METRICS (Post-Remediation)
Metric	Value	vs Pre-Remediation
Total files	1,980	+5
Markdown files	1,785	+3
Total words	3,432,088	+5,788
Sorrow Entities	292 (C:159, O:61, N:72)	Unchanged
MAW Codex Sets	42 folders, 198 complete	Unchanged
Ordeals	60 (5×4×3)	Unchanged
Hope Transformations	14	Unchanged
Echo Cores	9	Unchanged
Unknown Entities	12	Unchanged
Master Codices	44	Unchanged
Empty/Stub files	0	Unchanged
PM crossover leaks	0 in canonical files	Unchanged
Spelling consistency	All proper nouns verified	Unchanged
CROSS-REFERENCE HEALTH SUMMARY
Source File	Broken Links	Status
README.md	0	✅ Fixed
DEVELOPMENT.md	0	✅ Fixed
SOMNARAK_MAW_CODEX.md	735	🔴 ././ bug
SOMNARAK_ENTITY_CODEX.md	254	🔴 ././ bug
CHANGELOG.md	45	🟡 Historical
SESSION_BREAK_PRECAUTION.md	13	🟡 Historical
INTEGRITY_AND_LORE_REVIEW.md	7	🟡 Self-ref (our report)
16 MAW Registry READMEs	~80	🟡 Dead audit refs
Other files	~137	Various
Total	~1,271	989 from 2 files
FINAL GRADE
Dimension	Score	Notes
Remediation Completeness	73% (16/22)	9 fixed, 3 partial, 5 outstanding
Remediation Quality	A	Fixes are thorough and lore-enriching
Lore Consistency	A+	Enhanced, not just maintained
Structural Integrity	B+	989 links still broken in 2 files
Audit Health	A+	All 6 categories PASS
Overall Post-Remediation	A- (88/100)	One batch fix away from A+
PRIORITY ACTIONS
🔴 Fix ././ paths in SOMNARAK_MAW_CODEX.md and SOMNARAK_ENTITY_CODEX.md → eliminates 989 broken links
🟡 Clarify Hangul rule scope — does it apply to markdown tables or only ASCII boxes?
🟡 Update README codex count from 38 to 44
🔵 Decide on CHANGELOG refs — update or leave as historical record
Fresh review of commit e1abd9b. Built-in audit, full cross-reference scan, entity reconciliation, Ordeal symmetry, spelling verification, and duplicate detection performed.
