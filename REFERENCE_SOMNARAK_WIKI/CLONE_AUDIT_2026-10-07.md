# Clone Audit — is any dossier the same SE with the title and designation changed?

Audit date 2026-10-07. Owner's question, verbatim: *"How To Check It They Are The Same SE But Just
Change Title + Designation : [Combat Actions] Se It And Also Check Everything Else Like Comparison
Between SE File Maybe Some Already Change But You Could Detect If It Just A Change To Try To Hide It"*.

Tool: `tools/auditors/clone_audit.py` (this audit) and `tools/auditors/frame_dup.py` (prose frames).
Reproduce:

    python3 tools/auditors/clone_audit.py                 # whole-file check, top pairs
    python3 tools/auditors/clone_audit.py --sections      # every section, every pair
    python3 tools/auditors/clone_audit.py <file>          # one dossier's closest matches
    python3 tools/auditors/clone_audit.py --lineage       # lower-numbered wins; the copy diffed against it

## Method — what makes two dossiers 'the same file with the name changed'

A renamed copy keeps everything except the title, the registry code and the dossier's own name. So the
audit removes exactly those from **both** sides before comparing, and compares everything that remains on
four layers:

1. **body** — masked 5-gram containment both ways over every content line, tables included, so the
   Combat Actions move table is inside the measurement;
2. **prose** — the same over narrative lines only;
3. **sections** — every heading compared separately, so a copied table cannot hide behind an original
   narrative, and an original table cannot shield a copied narrative;
4. **lines** — exact matches and near-identical matches with a similarity ratio, which is what catches a
   copy that had a few words changed to disguise it.

Masked before counting: registry codes (`C-IIIγ-928`), sector ids, 1-5 digit figures, and the
dossier's own name words in English and Korean. Table pipes are dropped so cell text still counts.

**Thresholds.** Containment 1.00 means one side is the other's content; a deliberate rename-and-hide would
still read **>= 0.85**. Substantial copying reads 0.5-0.85. A whole file under 0.20 is a different dossier
that happens to share boilerplate.

## Finding 1 — No dossier is another dossier renamed

Strongest pair in the archive: **SE-N-IIIγ-917_Dawn_That_Forgot_잠드는_새벽.md** / **SE-N-IVδ-927_Dreaming_Plague_꿈의_전염병.md** — contains 0.169, contained-by 0.137.
Pairs at >= 0.50: **0**. At >= 0.30: **0**. At >= 0.15: **1**. At >= 0.08: **36**. Median pair: ~0.005.
On this measurement **no dossier in the wing is a renamed copy of another**; the closest pairs share
roughly a sixth of their material, which is boilerplate overlap, not a copy.

## Finding 2 — But 43 / 301 dossiers carry a whole section copied verbatim

`clone_audit.py --sections` compares every section separately. A section at >= 0.90 is the same text on
both sides with only names, codes and figures swapped — a copy, not a resemblance.

| section | files | pairs >=0.90 | pairs >=0.50 | pairs >=0.30 |
|---|---|---|---|---|
| Consequences | 297 | 26 | 167 | 206 |
| Operational Parameters | 301 | 15 | 56 | 97 |
| Log and Method | 88 | 0 | 54 | 99 |
| 증언 (Testimonium) | 297 | 2 | 49 | 52 |
| M.A.W. Suit | 296 | 0 | 38 | 105 |
| Combat Actions | 301 | 1 | 36 | 36 |
| Interaction Pattern | 263 | 0 | 35 | 94 |
| Core Stat Line | 300 | 1 | 28 | 83 |
| Trivia | 301 | 0 | 27 | 46 |
| 감각 묘사 (Flavor Text) | 301 | 0 | 22 | 119 |
| M.A.W. Weapon | 300 | 0 | 21 | 92 |
| Operational Notes | 300 | 7 | 16 | 29 |
| Escalation Notes | 300 | 0 | 13 | 59 |
| M.A.W. Use Notes | 299 | 0 | 13 | 90 |
| Tool Use Profile | 88 | 0 | 12 | 41 |
| Breach Behavior | 147 | 0 | 8 | 36 |

The worst family is **Consequences**: 297 files, **26 pairs >= 0.90**, 167 pairs >= 0.50, 206 >= 0.30.
Next: Operational Parameters (15/56/97), the Testimonium (2/49/52), Combat Actions (1/36/36), Core Stat
Line (1/28/83), Trivia (0/27/46), M.A.W. Suit (0/38/105), Log and Method (0/54/99).

**43 / 301** dossiers carry at least one verbatim section. The heaviest:

- 6 section(s) at >=0.90 (worst 1.00) — SE-C-IIIγ-102_The_Dancing_Chains_춤추는_사슬.md
- 6 section(s) at >=0.90 (worst 0.94) — SE-N-IIIγ-585_Floating_Tree_떠다니는_나무.md
- 5 section(s) at >=0.90 (worst 0.96) — SE-C-IIIγ-300_Memory_Lock_기억의_자물쇠.md
- 5 section(s) at >=0.90 (worst 0.96) — SE-C-IVβ-042_The_Angry_Maiden_분노의_처녀.md
- 5 section(s) at >=0.90 (worst 1.00) — SE-N-IIIγ-505_Dreaming_Ruin_돌아온_잔해.md
- 5 section(s) at >=0.90 (worst 1.00) — SE-N-IIα-125_Hollow_Echo_빈_메아리.md
- 5 section(s) at >=0.90 (worst 1.00) — SE-N-IIβ-170_Aphonia_침묵의_비명.md
- 5 section(s) at >=0.90 (worst 0.94) — SE-C-IVγ-009_The_Memory_Weaver_기억의_직공.md
- 4 section(s) at >=0.90 (worst 0.94) — SE-C-IVγ-255_Hollow_Architect_빈_건축가.md
- 4 section(s) at >=0.90 (worst 1.00) — SE-C-Iα-247_Torn_Flower_찢어진_꽃.md
- 4 section(s) at >=0.90 (worst 1.00) — SE-N-IIβ-627_Harvest_Beyond_the_Gate_녹아내린_열매.md
- 3 section(s) at >=0.90 (worst 0.98) — SE-N-Iα-519_Mourning_a_Life_I_Never_Lived_스며든_씨앗.md

## Finding 3 — The Combat Actions move table is a template with the flavour word swapped

This is the owner's named example, and the measurement confirms it:

| move name | dossiers carrying it |
|---|---|
| *The Settling* | 33 |
| *The First Weight* | 30 |
| *The Full Return* | 7 |
| *The Full Shatter* | 7 |
| *The Body Surge* | 5 |

The pattern is *The First Weight* (Debuff) / *The [X] Surge* / *The Settling* / *The [X] Collapse*, with X
swapped for the dossier's element — Mind, Dream, Body, Void. **One pair is identical even in the flavour
word**: Dawn That Forgot `N-IIIγ-917` and Dreaming Plague `N-IVδ-927` share the Combat Actions table
byte for byte after masking, containment **1.00 both ways**, and 42 further near-identical lines at >= 0.90.

Shared rows, by holder count:

- **4 dossiers** — `the settling attack all at once the pressure concentrates the entity focuses its full void weight on one point`
- **2 dossiers** — `the settling attack all at once the pressure concentrates the entity focuses its full grudge weight on one poi`
- **2 dossiers** — `the settling attack all at once the pressure concentrates the entity focuses its full lament weight on one poi`
- **2 dossiers** — `the first weight debuff it begins as a whisper in the void the entity s dream pressure settles over the target`

## Case file — Dawn That Forgot `N-IIIγ-917` / Dreaming Plague `N-IVδ-927`

| section | A in B | B in A |
|---|---|---|
| Combat Actions | 1.00 | 1.00 |
| 증언 (Testimonium) | 0.83 | 0.83 |
| Trivia | 0.71 | 0.71 |
| M.A.W. Weapon | 0.49 | 0.39 |
| M.A.W. Suit | 0.43 | 0.31 |
| M.A.W. Stigma | 0.38 | 0.27 |

Their narratives, origin sections and observation logs are their own: the whole-file figure stays at 0.169
because the copied part is the mechanical kit, not the story. **This is the pattern the owner described**,
one level down: not the whole dossier, but its Combat Actions, its equipment tables, its Trivia and its
Testimonium carried across with the names changed.

## Finding 4 — Lineage: the lower designation number wins, and the diff shows the cover-up

Owner's rule, 2026-10-07 — *"The One That Win Is The One With Lower Number In Their Designation Between Two
Copy Then You Can See What Was It Before The Cover UP"*. `clone_audit.py --lineage` applies it: in each copied
pair the **lower designation number is the source**, the higher is the copy, and the diff between them is what
the copy was before the title, designation and figures were changed. Two evidences are reported per pair — the
**substitutions** (exactly which tokens were swapped) and the **residue** (the source's own vocabulary still
sitting in the copy, where a swap was missed).

| winner — lower designation | copy | sections copied | shared lines | substitutions made in the copy | residue left in the copy |
|---|---|---|---|---|---|
| `O-IIIγ-924` Weighted Silence | `N-IVδ-927` Dreaming Plague | 5 | 32 | Weighted→Dreaming, Silence→Plague, 438→502, γ→δ, SECTOR-O-924→SECTOR-N-927 | 0 |
| `C-Iα-071` The Kind Healer | `C-IIIγ-105` The Lonely Giant | 4 | 17 | Kind→Lonely, Healer→Giant, 224→633, 15→40, 10→16 | **kind x4, healer x2** |
| `C-Iα-114` A Letter Never Sent | `O-IVδ-515` Last Warmth of Forty-Two | 3 | 31 | 310→820, 15→40, 6→28, 14→55, 5→3 | **never x3** |
| `N-IIIβ-941` Grieving Love | `O-IIIβ-944` Calling Bloom | 3 | 30 | Grieving→Calling, Love→Bloom, 540→480, 20→19, 50→45 | **love x5, grieving x1** |
| `N-IIIγ-917` Dawn That Forgot | `N-IVδ-927` Dreaming Plague | 3 | 29 | 29→24, 464→502, γ→δ, SECTOR-N-917→SECTOR-N-927 | 0 |
| `O-IIIγ-412` The Wedge That Held | `O-IVδ-515` Last Warmth of Forty-Two | 3 | 29 | 680→820, 30→40, 40→50, 60→70 | **held x6** |
| `C-IVγ-009` The Memory Weaver | `N-IIIβ-077` The Memory Thief | 3 | 25 | Weaver→Thief, 621→422, 40→25, 18→8, 41→20 | **weaver x1** |
| `N-IIβ-319` Magistrates Strike-Through | `O-IIIγ-412` The Wedge That Held | 3 | 25 | 480→680, 14→16, 20→30, 30→40 | **through x8, strike x7** |
| `C-IIIβ-072` Father's Broken Bond | `C-Iα-114` A Letter Never Sent | 3 | 22 | 520→310, 20→15, 80→10, β→α | **broken x3** |
| `C-IVβ-041` The Grieving Maiden | `C-Iα-071` The Kind Healer | 2 | 29 | Grieving→Kind, Maiden→Healer, 515→224, 25→15, 12→10 | 0 |
| `O-IIIγ-916` Allhallow | `C-IVδ-922` Miasma | 2 | 19 | Allhallow→Miasma, 449→474, γ→δ, SECTOR-O-916→SECTOR-C-922 | 0 |
| `O-IIIγ-924` Weighted Silence | `N-IIIγ-929` Dead Air | 2 | 17 | Weighted→Dead, Silence→Air, 438→458, SECTOR-O-924→SECTOR-N-929 | **silence x1** |

**What the table says.** The pattern is consistent: a copy is the source's block with the **name words**, the
**designation tokens** (class, potency Greek letter, number), the **sector id** and the **figures** swapped.
Two worked examples of "what it was before the cover-up":

- **`N-IVδ-927` Dreaming Plague was Weighted Silence `O-IIIγ-924`.** Five sections carried over; the swaps are
  its own new name (Weighted→Dreaming, Silence→Plague), its own potency letter (γ→δ), its own number and sector,
  and 438→502 in the figures. The same file also carries Dawn That Forgot's `N-IIIγ-917` Combat Actions and
  Testimonium (29 lines) — a copy of two sources at once.
- **`C-IIIγ-105` The Lonely Giant was The Kind Healer `C-Iα-071`** — and the cover-up did not finish: **"kind"
  survives in it four times and "healer" twice**, the source's own vocabulary left in place while the name was
  swapped. The same test names Calling Bloom (`love x5, grieving x1` from Grieving Love), The Wedge
  (`through x8, strike x7` from the Magistrates Strike-Through), Last Warmth (`never x3`, `held x6`) and
  Father's Broken Bond (`broken x3`).

**Chain.** The order is a partial order, not a single tree: **`C-IVβ-041` Grieving Maiden → `C-Iα-071` Kind
Healer → `C-IIIγ-105` Lonely Giant**, each step the lower number over the next, with the residue thinning at
every step. `N-IVδ-927` Dreaming Plague sits at the end of two chains at once (`O-IIIγ-924` and `N-IIIγ-917`).

**Also measured**, so it is not mistaken for the same thing: 38 pairs in the archive are genuinely **mutual**
(containment >= 0.9 both ways, e.g. The Debt Scale / The Cracked Hourglass's Core Stat Line) — those are
shared template text neither file wrote, and the designation rule does not apply to them.

## Finding 5 — What stays the same: the SECC header, and the Combat Actions table

Owner's observation, 2026-10-07 — *"Usually The Things That Still The Same Is [SECC Classification] Except
[**Physical Form + Designation**] And [Combat Actions]"*. Measured over **301 / 301** dossiers, and it holds:

**The SECC header.** Across the archive, exactly **two** of its fields carry **301 / 301 distinct values** —
`Designation` and `Physical Form`. Every other field is drawn from a shared pool:

| SECC field | distinct values | biggest pool value | files carrying a pooled value |
|---|---|---|---|
| Sorrow Category | 11 | City Sorrow (도한) | **290 / 301** |
| Element | 14 | Lament | **290 / 301** |
| R.D. Comprehension Level | 21 | 2 — Basic | **256 / 301** |
| Potency | 25 | Major (γ) | **246 / 301** |
| Movement | 81 | Mobile — walks upright | **179 / 301** |
| Coherence | 122 | Entity (IV) | **173 / 301** |
| Entity Type | 145 | **Subject** — Can breach | **129 / 301** |
| Manifestation | 59 | Subject-Body | **80 / 301** |
| **Designation** | **301** | — | **0 / 301 — unique per file** |
| **Physical Form** | **301** | — | **0 / 301 — unique per file** |
| Location | 126 | — | 0 / 301 (top value in 15) |

So the header is a template as the owner says: the two rows that are never shared are **Designation and Physical
Form**; the rest are drawn from lists where a single value covers 24-54% of the wing. The pair check sharpens
it: within a copy pair the SECC **pools** match but not the exact rows — `Weighted Silence` / `Dreaming Plague`
match on 3 rows (Entity Type, Element, Movement) and differ on 8; `Kind Healer` / `Lonely Giant` match on 3
(Sorrow Category, Manifestation, Movement); `Grieving Love` / `Calling Bloom` on 4; `Strike-Through` / `Wedge`
on 2. Outside the SECC block those same pairs share far more — 16, 8, 23 and 9 identical field rows respectively
across the Combat Record, M.A.W. and Battle tables — which is Finding 4's copied blocks seen from the other side.

**The Combat Actions table.**

| measure | value |
|---|---|
| dossiers with a Combat Actions table | **301 / 301** |
| carry the *First Weight / [X] Surge / The Settling / [X] Collapse* skeleton | **29 / 301** |
| *The Settling* | 33 dossiers |
| *The First Weight* | 30 dossiers |
| *The Full Return* / *The Full Shatter* | 7 each |
| tables identical byte-for-byte after masking | **1 pair** — Dawn That Forgot `N-IIIγ-917` / Dreaming Plague `N-IVδ-927` |
| pairs at >= 0.50 containment | **36** |

The move table is therefore a template with the flavour word swapped — *Mind*, *Dream*, *Body*, *Void* — and in
one pair not even that was changed. Both facts the owner named — the SECC header and the Combat Actions table —
are the two places the wing's copy problem actually lives, and both are now counted.

## What the check looks like going forward

1. Run `clone_audit.py` and `clone_audit.py --sections` before and after any batch; the counters to move
   are `pairs >= 0.90` and `files carrying a verbatim section` (**43 / 301** today).
2. Target, if the owner rules for one: no section pair at >= 0.90 and no whole-file pair at >= 0.30.
3. Fix in the existing units of ten, worst-first, growth-only (`R-15`): each copied block re-authored in the
   file's own terms, never deleted.

## Files

- `tools/auditors/clone_audit.py` — this audit (whole-file, section-level, near-identical lines).
- `tools/auditors/frame_dup.py` — prose-frame families with names and figures masked.
- Read-only; no dossier content was changed by either tool or by this audit.
