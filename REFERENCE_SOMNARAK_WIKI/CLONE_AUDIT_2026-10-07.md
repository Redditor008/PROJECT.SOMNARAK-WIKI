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
    python3 tools/auditors/clone_audit.py --pair A B      # one pair in full: sections, shared lines, swaps
    python3 tools/auditors/clone_audit.py --quotes        # restarted from the SE quote: families and the clones inside
    python3 tools/auditors/clone_audit.py --plan          # light vs heavy: who to fix, who to clean

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

## Finding 6 — Compare the pairs yourself (links, owner's request 2026-10-07)

Every pair named in this audit is linked below, both sides, on the working branch. Open the two tabs and
compare — or run the pair inspector, which prints the containment, the per-section scores, and every shared
line with the substitutions marked:

    python3 tools/auditors/clone_audit.py --pair <winning file> <copy file>

| source — lower designation | copy | sections copied | what the diff shows |
|---|---|---|---|
| [[SE-N-IIIγ-917_Dawn_That_Forgot_잠드는_새벽](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-III%CE%B3-917_Dawn_That_Forgot_%EC%9E%A0%EB%93%9C%EB%8A%94_%EC%83%88%EB%B2%BD.md "SE-N-IIIγ-917_Dawn_That_Forgot_잠드는_새벽.md")] | [[SE-N-IVδ-927_Dreaming_Plague_꿈의_전염병](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-IV%CE%B4-927_Dreaming_Plague_%EA%BF%88%EC%9D%98_%EC%A0%84%EC%97%BC%EB%B3%91.md "SE-N-IVδ-927_Dreaming_Plague_꿈의_전염병.md")] | Combat Actions, Trivia, 증언 (Testimonium) | 29 lines; Combat Actions identical 1.00 / 1.00 |
| [[SE-O-IIIγ-924_Weighted_Silence_침묵의_구역](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-III%CE%B3-924_Weighted_Silence_%EC%B9%A8%EB%AC%B5%EC%9D%98_%EA%B5%AC%EC%97%AD.md "SE-O-IIIγ-924_Weighted_Silence_침묵의_구역.md")] | [[SE-N-IVδ-927_Dreaming_Plague_꿈의_전염병](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-IV%CE%B4-927_Dreaming_Plague_%EA%BF%88%EC%9D%98_%EC%A0%84%EC%97%BC%EB%B3%91.md "SE-N-IVδ-927_Dreaming_Plague_꿈의_전염병.md")] | Combat Actions, M.A.W. Suit, M.A.W. Weapon, Trivia, 증언 | 32 lines; Weighted→Dreaming, Silence→Plague, 438→502 |
| [[SE-C-Iα-071_The_Kind_Healer_친절한_치유자](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-I%CE%B1-071_The_Kind_Healer_%EC%B9%9C%EC%A0%88%ED%95%9C_%EC%B9%98%EC%9C%A0%EC%9E%90.md "SE-C-Iα-071_The_Kind_Healer_친절한_치유자.md")] | [[SE-C-IIIγ-105_The_Lonely_Giant_외로운_거인](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-105_The_Lonely_Giant_%EC%99%B8%EB%A1%9C%EC%9A%B4_%EA%B1%B0%EC%9D%B8.md "SE-C-IIIγ-105_The_Lonely_Giant_외로운_거인.md")] | Consequences, Interaction Pattern, Operational Work Notes, 감각 묘사 | 17 lines; residue **kind ×4, healer ×2** |
| [[SE-C-Iα-114_A_Letter_Never_Sent_부치지_못한_편지](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-I%CE%B1-114_A_Letter_Never_Sent_%EB%B6%80%EC%B9%98%EC%A7%80_%EB%AA%BB%ED%95%9C_%ED%8E%B8%EC%A7%80.md "SE-C-Iα-114_A_Letter_Never_Sent_부치지_못한_편지.md")] | [[SE-O-IVδ-515_The_Last_Warmth_of_Forty-Two_마흔둘의_마지막_온기](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-IV%CE%B4-515_The_Last_Warmth_of_Forty-Two_%EB%A7%88%ED%9D%94%EB%91%98%EC%9D%98_%EB%A7%88%EC%A7%80%EB%A7%89_%EC%98%A8%EA%B8%B0.md "SE-O-IVδ-515_The_Last_Warmth_of_Forty-Two_마흔둘의_마지막_온기.md")] | Escalation Notes, Log and Method, M.A.W. Equipment | 31 lines; residue **never ×3** |
| [[SE-N-IIIβ-941_Grieving_Love_슬픈_사랑](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-III%CE%B2-941_Grieving_Love_%EC%8A%AC%ED%94%88_%EC%82%AC%EB%9E%91.md "SE-N-IIIβ-941_Grieving_Love_슬픈_사랑.md")] | [[SE-O-IIIβ-944_Calling_Bloom_부르는_꽃](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-III%CE%B2-944_Calling_Bloom_%EB%B6%80%EB%A5%B4%EB%8A%94_%EA%BD%83.md "SE-O-IIIβ-944_Calling_Bloom_부르는_꽃.md")] | Breach Behavior, Escalation Notes, M.A.W. Suit | 30 lines; residue **love ×5** |
| [[SE-O-IIIγ-412_The_Wedge_That_Held_끝끝내_버틴_쐐기](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-III%CE%B3-412_The_Wedge_That_Held_%EB%81%9D%EB%81%9D%EB%82%B4_%EB%B2%84%ED%8B%B4_%EC%90%90%EA%B8%B0.md "SE-O-IIIγ-412_The_Wedge_That_Held_끝끝내_버틴_쐐기.md")] | [[SE-O-IVδ-515_The_Last_Warmth_of_Forty-Two_마흔둘의_마지막_온기](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-IV%CE%B4-515_The_Last_Warmth_of_Forty-Two_%EB%A7%88%ED%9D%94%EB%91%98%EC%9D%98_%EB%A7%88%EC%A7%80%EB%A7%89_%EC%98%A8%EA%B8%B0.md "SE-O-IVδ-515_The_Last_Warmth_of_Forty-Two_마흔둘의_마지막_온기.md")] | Battle Phases, M.A.W. Equipment, Operational Notes | 29 lines; residue **held ×6** |
| [[SE-C-IVγ-009_The_Memory_Weaver_기억의_직공](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B3-009_The_Memory_Weaver_%EA%B8%B0%EC%96%B5%EC%9D%98_%EC%A7%81%EA%B3%B5.md "SE-C-IVγ-009_The_Memory_Weaver_기억의_직공.md")] | [[SE-N-IIIβ-077_The_Memory_Thief_기록_도둑](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-III%CE%B2-077_The_Memory_Thief_%EA%B8%B0%EB%A1%9D_%EB%8F%84%EB%91%91.md "SE-N-IIIβ-077_The_Memory_Thief_기록_도둑.md")] | Consequences, M.A.W. Suit, Operational Work Notes | 25 lines; Weaver→Thief, 621→422 |
| [[SE-N-IIβ-319_The_Magistrates_Strike-Through_판관의_취소선](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-II%CE%B2-319_The_Magistrates_Strike-Through_%ED%8C%90%EA%B4%80%EC%9D%98_%EC%B7%A8%EC%86%8C%EC%84%A0.md "SE-N-IIβ-319_The_Magistrates_Strike-Through_판관의_취소선.md")] | [[SE-O-IIIγ-412_The_Wedge_That_Held_끝끝내_버틴_쐐기](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-III%CE%B3-412_The_Wedge_That_Held_%EB%81%9D%EB%81%9D%EB%82%B4_%EB%B2%84%ED%8B%B4_%EC%90%90%EA%B8%B0.md "SE-O-IIIγ-412_The_Wedge_That_Held_끝끝내_버틴_쐐기.md")] | Battle Phases, Escalation Notes, M.A.W. Equipment | 25 lines; residue **through ×8, strike ×7** |
| [[SE-C-IIIβ-072_Fathers_Broken_Bond_아버지의_부러진_차용패](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B2-072_Fathers_Broken_Bond_%EC%95%84%EB%B2%84%EC%A7%80%EC%9D%98_%EB%B6%80%EB%9F%AC%EC%A7%84_%EC%B0%A8%EC%9A%A9%ED%8C%A8.md "SE-C-IIIβ-072_Fathers_Broken_Bond_아버지의_부러진_차용패.md")] | [[SE-C-Iα-114_A_Letter_Never_Sent_부치지_못한_편지](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-I%CE%B1-114_A_Letter_Never_Sent_%EB%B6%80%EC%B9%98%EC%A7%80_%EB%AA%BB%ED%95%9C_%ED%8E%B8%EC%A7%80.md "SE-C-Iα-114_A_Letter_Never_Sent_부치지_못한_편지.md")] | Escalation Notes, Log and Method, M.A.W. Equipment | 22 lines; **broken ×3** |
| [[SE-C-IVβ-041_The_Grieving_Maiden_슬픔의_처녀](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B2-041_The_Grieving_Maiden_%EC%8A%AC%ED%94%94%EC%9D%98_%EC%B2%98%EB%85%80.md "SE-C-IVβ-041_The_Grieving_Maiden_슬픔의_처녀.md")] | [[SE-C-Iα-071_The_Kind_Healer_친절한_치유자](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-I%CE%B1-071_The_Kind_Healer_%EC%B9%9C%EC%A0%88%ED%95%9C_%EC%B9%98%EC%9C%A0%EC%9E%90.md "SE-C-Iα-071_The_Kind_Healer_친절한_치유자.md")] | Consequences, 감각 묘사 | 29 lines; chain step 1 |
| [[SE-C-Iα-071_The_Kind_Healer_친절한_치유자](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-I%CE%B1-071_The_Kind_Healer_%EC%B9%9C%EC%A0%88%ED%95%9C_%EC%B9%98%EC%9C%A0%EC%9E%90.md "SE-C-Iα-071_The_Kind_Healer_친절한_치유자.md")] | [[SE-C-IIIγ-105_The_Lonely_Giant_외로운_거인](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-105_The_Lonely_Giant_%EC%99%B8%EB%A1%9C%EC%9A%B4_%EA%B1%B0%EC%9D%B8.md "SE-C-IIIγ-105_The_Lonely_Giant_외로운_거인.md")] | (chain step 2 — same pair as row 3) |  |
| [[SE-O-IIIγ-916_Allhallow_유령의_시간](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-III%CE%B3-916_Allhallow_%EC%9C%A0%EB%A0%B9%EC%9D%98_%EC%8B%9C%EA%B0%84.md "SE-O-IIIγ-916_Allhallow_유령의_시간.md")] | [[SE-C-IVδ-922_Miasma_우는_안개](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-922_Miasma_%EC%9A%B0%EB%8A%94_%EC%95%88%EA%B0%9C.md "SE-C-IVδ-922_Miasma_우는_안개.md")] | Combat Actions, 증언 | 19 lines; Allhallow→Miasma |
| [[SE-O-IIIγ-924_Weighted_Silence_침묵의_구역](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-III%CE%B3-924_Weighted_Silence_%EC%B9%A8%EB%AC%B5%EC%9D%98_%EA%B5%AC%EC%97%AD.md "SE-O-IIIγ-924_Weighted_Silence_침묵의_구역.md")] | [[SE-N-IIIγ-929_Dead_Air_유령의_압력](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-III%CE%B3-929_Dead_Air_%EC%9C%A0%EB%A0%B9%EC%9D%98_%EC%95%95%EB%A0%A5.md "SE-N-IIIγ-929_Dead_Air_유령의_압력.md")] | Combat Actions, 증언 | 17 lines; Weighted→Dead, Silence→Air |

All 13 commands, ready to paste:

```bash
python3 tools/auditors/clone_audit.py --pair 'SOMNARAK-WORLD/Sorrow_Entities/SE-N-IIIγ-917_Dawn_That_Forgot_잠드는_새벽.md' 'SOMNARAK-WORLD/Sorrow_Entities/SE-N-IVδ-927_Dreaming_Plague_꿈의_전염병.md'
python3 tools/auditors/clone_audit.py --pair 'SOMNARAK-WORLD/Sorrow_Entities/SE-O-IIIγ-924_Weighted_Silence_침묵의_구역.md' 'SOMNARAK-WORLD/Sorrow_Entities/SE-N-IVδ-927_Dreaming_Plague_꿈의_전염병.md'
python3 tools/auditors/clone_audit.py --pair 'SOMNARAK-WORLD/Sorrow_Entities/SE-C-Iα-071_The_Kind_Healer_친절한_치유자.md' 'SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIIγ-105_The_Lonely_Giant_외로운_거인.md'
python3 tools/auditors/clone_audit.py --pair 'SOMNARAK-WORLD/Sorrow_Entities/SE-C-Iα-114_A_Letter_Never_Sent_부치지_못한_편지.md' 'SOMNARAK-WORLD/Sorrow_Entities/SE-O-IVδ-515_The_Last_Warmth_of_Forty-Two_마흔둘의_마지막_온기.md'
python3 tools/auditors/clone_audit.py --pair 'SOMNARAK-WORLD/Sorrow_Entities/SE-N-IIIβ-941_Grieving_Love_슬픈_사랑.md' 'SOMNARAK-WORLD/Sorrow_Entities/SE-O-IIIβ-944_Calling_Bloom_부르는_꽃.md'
python3 tools/auditors/clone_audit.py --pair 'SOMNARAK-WORLD/Sorrow_Entities/SE-O-IIIγ-412_The_Wedge_That_Held_끝끝내_버틴_쐐기.md' 'SOMNARAK-WORLD/Sorrow_Entities/SE-O-IVδ-515_The_Last_Warmth_of_Forty-Two_마흔둘의_마지막_온기.md'
python3 tools/auditors/clone_audit.py --pair 'SOMNARAK-WORLD/Sorrow_Entities/SE-C-IVγ-009_The_Memory_Weaver_기억의_직공.md' 'SOMNARAK-WORLD/Sorrow_Entities/SE-N-IIIβ-077_The_Memory_Thief_기록_도둑.md'
python3 tools/auditors/clone_audit.py --pair 'SOMNARAK-WORLD/Sorrow_Entities/SE-N-IIβ-319_The_Magistrates_Strike-Through_판관의_취소선.md' 'SOMNARAK-WORLD/Sorrow_Entities/SE-O-IIIγ-412_The_Wedge_That_Held_끝끝내_버틴_쐐기.md'
python3 tools/auditors/clone_audit.py --pair 'SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIIβ-072_Fathers_Broken_Bond_아버지의_부러진_차용패.md' 'SOMNARAK-WORLD/Sorrow_Entities/SE-C-Iα-114_A_Letter_Never_Sent_부치지_못한_편지.md'
python3 tools/auditors/clone_audit.py --pair 'SOMNARAK-WORLD/Sorrow_Entities/SE-C-IVβ-041_The_Grieving_Maiden_슬픔의_처녀.md' 'SOMNARAK-WORLD/Sorrow_Entities/SE-C-Iα-071_The_Kind_Healer_친절한_치유자.md'
python3 tools/auditors/clone_audit.py --pair 'SOMNARAK-WORLD/Sorrow_Entities/SE-C-Iα-071_The_Kind_Healer_친절한_치유자.md' 'SOMNARAK-WORLD/Sorrow_Entities/SE-C-IIIγ-105_The_Lonely_Giant_외로운_거인.md'
python3 tools/auditors/clone_audit.py --pair 'SOMNARAK-WORLD/Sorrow_Entities/SE-O-IIIγ-916_Allhallow_유령의_시간.md' 'SOMNARAK-WORLD/Sorrow_Entities/SE-C-IVδ-922_Miasma_우는_안개.md'
python3 tools/auditors/clone_audit.py --pair 'SOMNARAK-WORLD/Sorrow_Entities/SE-O-IIIγ-924_Weighted_Silence_침묵의_구역.md' 'SOMNARAK-WORLD/Sorrow_Entities/SE-N-IIIγ-929_Dead_Air_유령의_압력.md'
```

The **43 / 301** dossiers carrying a verbatim section (Finding 2), heaviest first — open any of them and
search for the section named in the table above:

- [[SE-C-IIIγ-102_The_Dancing_Chains_춤추는_사슬](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-102_The_Dancing_Chains_%EC%B6%A4%EC%B6%94%EB%8A%94_%EC%82%AC%EC%8A%AC.md "SE-C-IIIγ-102_The_Dancing_Chains_춤추는_사슬.md")]
- [[SE-N-IIIγ-585_Floating_Tree_떠다니는_나무](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-III%CE%B3-585_Floating_Tree_%EB%96%A0%EB%8B%A4%EB%8B%88%EB%8A%94_%EB%82%98%EB%AC%B4.md "SE-N-IIIγ-585_Floating_Tree_떠다니는_나무.md")]
- [[SE-C-IIIγ-300_Memory_Lock_기억의_자물쇠](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-300_Memory_Lock_%EA%B8%B0%EC%96%B5%EC%9D%98_%EC%9E%90%EB%AC%BC%EC%87%A0.md "SE-C-IIIγ-300_Memory_Lock_기억의_자물쇠.md")]
- [[SE-C-IVβ-042_The_Angry_Maiden_분노의_처녀](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B2-042_The_Angry_Maiden_%EB%B6%84%EB%85%B8%EC%9D%98_%EC%B2%98%EB%85%80.md "SE-C-IVβ-042_The_Angry_Maiden_분노의_처녀.md")]
- [[SE-N-IIIγ-505_Dreaming_Ruin_돌아온_잔해](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-III%CE%B3-505_Dreaming_Ruin_%EB%8F%8C%EC%95%84%EC%98%A8_%EC%9E%94%ED%95%B4.md "SE-N-IIIγ-505_Dreaming_Ruin_돌아온_잔해.md")]
- [[SE-N-IIα-125_Hollow_Echo_빈_메아리](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-II%CE%B1-125_Hollow_Echo_%EB%B9%88_%EB%A9%94%EC%95%84%EB%A6%AC.md "SE-N-IIα-125_Hollow_Echo_빈_메아리.md")]
- [[SE-N-IIβ-170_Aphonia_침묵의_비명](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-II%CE%B2-170_Aphonia_%EC%B9%A8%EB%AC%B5%EC%9D%98_%EB%B9%84%EB%AA%85.md "SE-N-IIβ-170_Aphonia_침묵의_비명.md")]
- [[SE-C-IVγ-009_The_Memory_Weaver_기억의_직공](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B3-009_The_Memory_Weaver_%EA%B8%B0%EC%96%B5%EC%9D%98_%EC%A7%81%EA%B3%B5.md "SE-C-IVγ-009_The_Memory_Weaver_기억의_직공.md")]
- [[SE-C-IVγ-255_Hollow_Architect_빈_건축가](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B3-255_Hollow_Architect_%EB%B9%88_%EA%B1%B4%EC%B6%95%EA%B0%80.md "SE-C-IVγ-255_Hollow_Architect_빈_건축가.md")]
- [[SE-C-Iα-247_Torn_Flower_찢어진_꽃](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-I%CE%B1-247_Torn_Flower_%EC%B0%A2%EC%96%B4%EC%A7%84_%EA%BD%83.md "SE-C-Iα-247_Torn_Flower_찢어진_꽃.md")]
- [[SE-N-IIβ-627_Harvest_Beyond_the_Gate_녹아내린_열매](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-II%CE%B2-627_Harvest_Beyond_the_Gate_%EB%85%B9%EC%95%84%EB%82%B4%EB%A6%B0_%EC%97%B4%EB%A7%A4.md "SE-N-IIβ-627_Harvest_Beyond_the_Gate_녹아내린_열매.md")]
- [[SE-N-Iα-519_Mourning_a_Life_I_Never_Lived_스며든_씨앗](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-I%CE%B1-519_Mourning_a_Life_I_Never_Lived_%EC%8A%A4%EB%A9%B0%EB%93%A0_%EC%94%A8%EC%95%97.md "SE-N-Iα-519_Mourning_a_Life_I_Never_Lived_스며든_씨앗.md")]

Whole-file check for yourself: `python3 tools/auditors/clone_audit.py` (pairs), `--sections` (every section,
every pair), `--lineage` (which number wins), `--pair A B` (one pair in full).

## Finding 7 — Restarting the check from the SE quote: the first call of a clone

Owner's finding, 2026-10-07 — *"The Number One CALL That It WAS Clone That Was Trying To Get Up Lifted By The
Other AI Is The SE Quote e.g. the one below SE Name/Title And Above SE [SECC Classification]"*. The blockquote
between the title and `## SECC Classification` is the part a reskin pass pastes in whole, so it is the first
place a clone shows. Check restarted there with `clone_audit.py --quotes`. **The finding holds, and strongly:**

| measure | value |
|---|---|
| dossiers with an opening quote | **301 / 301** |
| **exact duplicate quote families** | **5** |
| dossiers sitting in one | **31 / 301** |
| within-family pairs carrying a section clone (>= 0.50) | **18 / 84 = 21.4%** |
| archive baseline, all 45,150 pairs | **540 = 1.20%** |
| **lift** | **18x** |

A duplicated opening quote is therefore **eighteen times more likely** to sit inside a copy cluster than a
random pair of dossiers. It is the strongest single call in the archive — stronger than any section measurement,
because it is the one line every clone kept without editing.

**Family — "It does not end. It merely pauses between heartbeats." (8 dossiers)**

| dossier | |
|---|---|
| [[SE-C-IIIγ-913_Backward_Hour_카운트다운_시계](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-913_Backward_Hour_%EC%B9%B4%EC%9A%B4%ED%8A%B8%EB%8B%A4%EC%9A%B4_%EC%8B%9C%EA%B3%84.md "SE-C-IIIγ-913_Backward_Hour_카운트다운_시계.md")] | |
| [[SE-C-IIIγ-921_Cracked_Flesh_균열의_들판](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-921_Cracked_Flesh_%EA%B7%A0%EC%97%B4%EC%9D%98_%EB%93%A4%ED%8C%90.md "SE-C-IIIγ-921_Cracked_Flesh_균열의_들판.md")] | |
| [[SE-C-IIβ-906_Grimoire_스스로_쓰는_책](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-906_Grimoire_%EC%8A%A4%EC%8A%A4%EB%A1%9C_%EC%93%B0%EB%8A%94_%EC%B1%85.md "SE-C-IIβ-906_Grimoire_스스로_쓰는_책.md")] | |
| [[SE-C-Vω-925_Sorrow_Mass_압살의_한](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-V%CF%89-925_Sorrow_Mass_%EC%95%95%EC%82%B4%EC%9D%98_%ED%95%9C.md "SE-C-Vω-925_Sorrow_Mass_압살의_한.md")] | |
| [[SE-N-IIIγ-917_Dawn_That_Forgot_잠드는_새벽](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-III%CE%B3-917_Dawn_That_Forgot_%EC%9E%A0%EB%93%9C%EB%8A%94_%EC%83%88%EB%B2%BD.md "SE-N-IIIγ-917_Dawn_That_Forgot_잠드는_새벽.md")] | |
| [[SE-N-IIβ-919_Passing_Bell_조상의_시간](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-II%CE%B2-919_Passing_Bell_%EC%A1%B0%EC%83%81%EC%9D%98_%EC%8B%9C%EA%B0%84.md "SE-N-IIβ-919_Passing_Bell_조상의_시간.md")] | |
| [[SE-O-IIIγ-920_Once_Upon_이야기의_시간](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-III%CE%B3-920_Once_Upon_%EC%9D%B4%EC%95%BC%EA%B8%B0%EC%9D%98_%EC%8B%9C%EA%B0%84.md "SE-O-IIIγ-920_Once_Upon_이야기의_시간.md")] | |
| [[SE-O-IIβ-914_Amnesia_잊혀진_일분](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-II%CE%B2-914_Amnesia_%EC%9E%8A%ED%98%80%EC%A7%84_%EC%9D%BC%EB%B6%84.md "SE-O-IIβ-914_Amnesia_잊혀진_일분.md")] | |

Clones inside the family (lower designation → copy, with the section and its score):

- Passing Bell → Sorrow Mass 0.69 (Testimonium)
- Amnesia → Dawn That Forgot 0.54 (Trivia)
- Dawn That Forgot → Passing Bell 0.52 (Testimonium)

**Family — "The city gave us this. We did not ask for it." (7 dossiers)**

| dossier | |
|---|---|
| [[SE-C-IIIγ-912_Eleven_Fifty-Nine_슬픔의_시간](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-912_Eleven_Fifty-Nine_%EC%8A%AC%ED%94%94%EC%9D%98_%EC%8B%9C%EA%B0%84.md "SE-C-IIIγ-912_Eleven_Fifty-Nine_슬픔의_시간.md")] | |
| [[SE-C-IVδ-907_Breathing_Stone_살아있는_벽](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-907_Breathing_Stone_%EC%82%B4%EC%95%84%EC%9E%88%EB%8A%94_%EB%B2%BD.md "SE-C-IVδ-907_Breathing_Stone_살아있는_벽.md")] | |
| [[SE-C-IVδ-909_Labyrinth_of_the_Unfinished_Mind_생각의_미로](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-909_Labyrinth_of_the_Unfinished_Mind_%EC%83%9D%EA%B0%81%EC%9D%98_%EB%AF%B8%EB%A1%9C.md "SE-C-IVδ-909_Labyrinth_of_the_Unfinished_Mind_생각의_미로.md")] | |
| [[SE-C-IVδ-915_Endless_Shift_끝없는_교대](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-915_Endless_Shift_%EB%81%9D%EC%97%86%EB%8A%94_%EA%B5%90%EB%8C%80.md "SE-C-IVδ-915_Endless_Shift_끝없는_교대.md")] | |
| [[SE-N-IIIγ-908_Unwaking_Block_잠드는_구역](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-III%CE%B3-908_Unwaking_Block_%EC%9E%A0%EB%93%9C%EB%8A%94_%EA%B5%AC%EC%97%AD.md "SE-N-IIIγ-908_Unwaking_Block_잠드는_구역.md")] | |
| [[SE-N-IIβ-910_Moktak_조상의_전당](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-II%CE%B2-910_Moktak_%EC%A1%B0%EC%83%81%EC%9D%98_%EC%A0%84%EB%8B%B9.md "SE-N-IIβ-910_Moktak_조상의_전당.md")] | |
| [[SE-O-IIIγ-916_Allhallow_유령의_시간](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-III%CE%B3-916_Allhallow_%EC%9C%A0%EB%A0%B9%EC%9D%98_%EC%8B%9C%EA%B0%84.md "SE-O-IIIγ-916_Allhallow_유령의_시간.md")] | |

Clones inside the family (lower designation → copy, with the section and its score):

- Unwaking Block → Allhallow 0.70 (Testimonium)
- Unwaking Block → Moktak 0.66 (Testimonium)
- Moktak → Allhallow 0.64 (Testimonium)
- Breathing Stone → Moktak 0.54 (Trivia)

**Family — "The weight is not punishment. It is recognition." (6 dossiers)**

| dossier | |
|---|---|
| [[SE-C-IVδ-918_Ninety_Seconds_반복되는_생각](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-918_Ninety_Seconds_%EB%B0%98%EB%B3%B5%EB%90%98%EB%8A%94_%EC%83%9D%EA%B0%81.md "SE-C-IVδ-918_Ninety_Seconds_반복되는_생각.md")] | |
| [[SE-C-IVδ-922_Miasma_우는_안개](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-922_Miasma_%EC%9A%B0%EB%8A%94_%EC%95%88%EA%B0%9C.md "SE-C-IVδ-922_Miasma_우는_안개.md")] | |
| [[SE-N-IIβ-903_Glass_Elsewhere_환영의_거울](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-II%CE%B2-903_Glass_Elsewhere_%ED%99%98%EC%98%81%EC%9D%98_%EA%B1%B0%EC%9A%B8.md "SE-N-IIβ-903_Glass_Elsewhere_환영의_거울.md")] | |
| [[SE-O-IIIγ-926_Sky_of_Borrowed_Faces_환각의_격자](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-III%CE%B3-926_Sky_of_Borrowed_Faces_%ED%99%98%EA%B0%81%EC%9D%98_%EA%B2%A9%EC%9E%90.md "SE-O-IIIγ-926_Sky_of_Borrowed_Faces_환각의_격자.md")] | |
| [[SE-O-IIβ-911_Never_Discharged_영원한_환자](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-II%CE%B2-911_Never_Discharged_%EC%98%81%EC%9B%90%ED%95%9C_%ED%99%98%EC%9E%90.md "SE-O-IIβ-911_Never_Discharged_영원한_환자.md")] | |
| [[SE-O-IVδ-930_Once_Told_살아_있는_서사](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-IV%CE%B4-930_Once_Told_%EC%82%B4%EC%95%84_%EC%9E%88%EB%8A%94_%EC%84%9C%EC%82%AC.md "SE-O-IVδ-930_Once_Told_살아_있는_서사.md")] | |

Clones inside the family (lower designation → copy, with the section and its score):

- Miasma → Sky of Borrowed Faces 0.65 (Operational Parameters)
- Never Discharged → Miasma 0.64 (Testimonium)
- Miasma → Once Told 0.54 (Trivia)

**Family — "When it comes, you will know. Everyone knows." (5 dossiers)**

| dossier | |
|---|---|
| [[SE-C-IIIγ-902_Beating_Relic_고동치는_유물](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-902_Beating_Relic_%EA%B3%A0%EB%8F%99%EC%B9%98%EB%8A%94_%EC%9C%A0%EB%AC%BC.md "SE-C-IIIγ-902_Beating_Relic_고동치는_유물.md")] | |
| [[SE-C-IIIγ-904_Thinking_Engine_생각하는_기계](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-904_Thinking_Engine_%EC%83%9D%EA%B0%81%ED%95%98%EB%8A%94_%EA%B8%B0%EA%B3%84.md "SE-C-IIIγ-904_Thinking_Engine_생각하는_기계.md")] | |
| [[SE-C-IIIγ-928_Lethe_혼란의_독기](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-928_Lethe_%ED%98%BC%EB%9E%80%EC%9D%98_%EB%8F%85%EA%B8%B0.md "SE-C-IIIγ-928_Lethe_혼란의_독기.md")] | |
| [[SE-N-IIIγ-929_Dead_Air_유령의_압력](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-III%CE%B3-929_Dead_Air_%EC%9C%A0%EB%A0%B9%EC%9D%98_%EC%95%95%EB%A0%A5.md "SE-N-IIIγ-929_Dead_Air_유령의_압력.md")] | |
| [[SE-N-Iα-905_Lacrima_영혼의_그릇](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-I%CE%B1-905_Lacrima_%EC%98%81%ED%98%BC%EC%9D%98_%EA%B7%B8%EB%A6%87.md "SE-N-Iα-905_Lacrima_영혼의_그릇.md")] | |

Clones inside the family (lower designation → copy, with the section and its score):

- Beating Relic → Thinking Engine 0.70 (Core Stat Line)
- Lacrima → Dead Air 0.65 (Operational Parameters)
- Beating Relic → Lacrima 0.65 (Operational Parameters)
- Beating Relic → Dead Air 0.50 (Combat Actions)

**Family — "Something here remembers what we chose to forget." (5 dossiers)**

| dossier | |
|---|---|
| [[SE-C-IIβ-901_Duri's_Heart_보존된_심장](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-901_Duri%27s_Heart_%EB%B3%B4%EC%A1%B4%EB%90%9C_%EC%8B%AC%EC%9E%A5.md "SE-C-IIβ-901_Duri's_Heart_보존된_심장.md")] | |
| [[SE-C-IVδ-923_Hatred_Above_분노의_폭풍](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-923_Hatred_Above_%EB%B6%84%EB%85%B8%EC%9D%98_%ED%8F%AD%ED%92%8D.md "SE-C-IVδ-923_Hatred_Above_분노의_폭풍.md")] | |
| [[SE-C-Iα-900_Vellum_Man_잊혀진_이야기꾼](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-I%CE%B1-900_Vellum_Man_%EC%9E%8A%ED%98%80%EC%A7%84_%EC%9D%B4%EC%95%BC%EA%B8%B0%EA%BE%BC.md "SE-C-Iα-900_Vellum_Man_잊혀진_이야기꾼.md")] | |
| [[SE-N-IVδ-927_Dreaming_Plague_꿈의_전염병](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-IV%CE%B4-927_Dreaming_Plague_%EA%BF%88%EC%9D%98_%EC%A0%84%EC%97%BC%EB%B3%91.md "SE-N-IVδ-927_Dreaming_Plague_꿈의_전염병.md")] | |
| [[SE-O-IIIγ-924_Weighted_Silence_침묵의_구역](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-III%CE%B3-924_Weighted_Silence_%EC%B9%A8%EB%AC%B5%EC%9D%98_%EA%B5%AC%EC%97%AD.md "SE-O-IIIγ-924_Weighted_Silence_침묵의_구역.md")] | |

Clones inside the family (lower designation → copy, with the section and its score):

- Weighted Silence → Dreaming Plague 0.87 (Combat Actions)
- Vellum Man → Weighted Silence 0.72 (Testimonium)
- Vellum Man → Dreaming Plague 0.63 (Testimonium)
- Hatred Above → Weighted Silence 0.50 (Combat Actions)

**What the quote does and does not say.** It is a *cluster marker*, not a proof: a shared quote says the two
files came through the same pass, and the check then looks inside them — in **all five families** it found
section clones, but the clones are 0.50-0.87, i.e. edited copies (the byte-identical pair, Dawn That Forgot /
Dreaming Plague, straddles two families: their quote differs while their Combat Actions does not). One family
was already repaired in this programme — `Lethe` and `Dead Air` share the quote and now score no section above
0.50 between them, which is the target state for the rest.

Reproduce: `python3 tools/auditors/clone_audit.py --quotes` (families, members, and the clones inside each).

## Finding 8 — Restart re-check, and the clean-first plan (owner's method, 2026-10-07)

Owner's direction — *"Fix the lighter one … 1 to 3 small section similar to fix and deleted the one with 2 big as in
a whole [Combat Action] + [Operational Parameters] COPY SECTION. So we do clean first than fixed. But at first restart
re-check."* Check restarted from scratch; the plan below is what it returns.

**Restart re-check, all four modes:**

| mode | result |
|---|---|
| `--quotes` | **5** duplicate quote families, **31 / 301** dossiers, within-family clone rate **18 / 84 = 21.4%** vs **1.20%** baseline (**18× lift**) |
| `--sections` | **43 / 301** dossiers carry a section at >= 0.90; Consequences (26 pairs >= 0.90), Operational Parameters (15), Testimonium (2), Combat Actions (1) |
| whole-file | strongest pair **0.169**; **0** pairs at >= 0.50 — no renamed dossiers |
| `--lineage` | lower designation wins; residue traces (`kind x4`, `love x5`, `through x8`) |

**Light vs heavy (new `--plan` mode):**

| measure | value |
|---|---|
| files carrying **>= 1 whole copied section** (>= 0.85) | **57 / 301** — 54 with one, **3 with two** |
| files with **only small overlaps** (0.50-0.85) | **95 / 301** |
| sections copied whole, by frequency | **Consequences 94** · **Operational Parameters 27** · **Combat Actions 16** · Operational Notes 14 · Testimonium 6 · Core Stat Line 2 · Breach Behavior 2 · Escalation Notes 2 · SECC 1 |

The two sections the owner named are the structural ones: **Operational Parameters whole in 27 files, Combat Actions
whole in 16** — 14 files carry one of those two whole.

**The 3 files carrying TWO whole copies (first to clean):**

| file | whole copies |
|---|---|
| [[SE-C-IIIγ-102_The_Dancing_Chains_춤추는_사슬](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-102_The_Dancing_Chains_%EC%B6%A4%EC%B6%94%EB%8A%94_%EC%82%AC%EC%8A%AC.md "SE-C-IIIγ-102_The_Dancing_Chains_춤추는_사슬.md")] | Core Stat Line, Operational Parameters |
| [[SE-O-IIIβ-944_Calling_Bloom_부르는_꽃](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-III%CE%B2-944_Calling_Bloom_%EB%B6%80%EB%A5%B4%EB%8A%94_%EA%BD%83.md "SE-O-IIIβ-944_Calling_Bloom_부르는_꽃.md")] | Escalation Notes, Operational Notes |
| [[SE-N-IIIβ-941_Grieving_Love_슬픈_사랑](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-III%CE%B2-941_Grieving_Love_%EC%8A%AC%ED%94%88_%EC%82%AC%EB%9E%91.md "SE-N-IIIβ-941_Grieving_Love_슬픈_사랑.md")] | Breach Behavior, Escalation Notes |

**The 14 files carrying Combat Actions and/or Operational Parameters whole:**

- [[SE-N-IIIγ-917_Dawn_That_Forgot_잠드는_새벽](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-III%CE%B3-917_Dawn_That_Forgot_%EC%9E%A0%EB%93%9C%EB%8A%94_%EC%83%88%EB%B2%BD.md "SE-N-IIIγ-917_Dawn_That_Forgot_잠드는_새벽.md")] — *Combat Actions*
- [[SE-N-IVδ-927_Dreaming_Plague_꿈의_전염병](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-IV%CE%B4-927_Dreaming_Plague_%EA%BF%88%EC%9D%98_%EC%A0%84%EC%97%BC%EB%B3%91.md "SE-N-IVδ-927_Dreaming_Plague_꿈의_전염병.md")] — *Combat Actions*
- [[SE-N-Iα-905_Lacrima_영혼의_그릇](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-I%CE%B1-905_Lacrima_%EC%98%81%ED%98%BC%EC%9D%98_%EA%B7%B8%EB%A6%87.md "SE-N-Iα-905_Lacrima_영혼의_그릇.md")] — *Combat Actions*
- [[SE-O-IIIγ-924_Weighted_Silence_침묵의_구역](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-III%CE%B3-924_Weighted_Silence_%EC%B9%A8%EB%AC%B5%EC%9D%98_%EA%B5%AC%EC%97%AD.md "SE-O-IIIγ-924_Weighted_Silence_침묵의_구역.md")] — *Combat Actions*
- [[SE-C-IIIγ-102_The_Dancing_Chains_춤추는_사슬](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-102_The_Dancing_Chains_%EC%B6%A4%EC%B6%94%EB%8A%94_%EC%82%AC%EC%8A%AC.md "SE-C-IIIγ-102_The_Dancing_Chains_춤추는_사슬.md")] — *Operational Parameters*
- [[SE-C-IIIγ-300_Memory_Lock_기억의_자물쇠](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-300_Memory_Lock_%EA%B8%B0%EC%96%B5%EC%9D%98_%EC%9E%90%EB%AC%BC%EC%87%A0.md "SE-C-IIIγ-300_Memory_Lock_기억의_자물쇠.md")] — *Operational Parameters*
- [[SE-C-IVβ-042_The_Angry_Maiden_분노의_처녀](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B2-042_The_Angry_Maiden_%EB%B6%84%EB%85%B8%EC%9D%98_%EC%B2%98%EB%85%80.md "SE-C-IVβ-042_The_Angry_Maiden_분노의_처녀.md")] — *Operational Parameters*
- [[SE-N-IIIγ-505_Dreaming_Ruin_돌아온_잔해](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-III%CE%B3-505_Dreaming_Ruin_%EB%8F%8C%EC%95%84%EC%98%A8_%EC%9E%94%ED%95%B4.md "SE-N-IIIγ-505_Dreaming_Ruin_돌아온_잔해.md")] — *Operational Parameters*
- [[SE-N-IIα-125_Hollow_Echo_빈_메아리](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-II%CE%B1-125_Hollow_Echo_%EB%B9%88_%EB%A9%94%EC%95%84%EB%A6%AC.md "SE-N-IIα-125_Hollow_Echo_빈_메아리.md")] — *Operational Parameters*
- [[SE-N-IIβ-170_Aphonia_침묵의_비명](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-II%CE%B2-170_Aphonia_%EC%B9%A8%EB%AC%B5%EC%9D%98_%EB%B9%84%EB%AA%85.md "SE-N-IIβ-170_Aphonia_침묵의_비명.md")] — *Operational Parameters*

**Method (clean first, then fix):**

1. **Clean** — the **57** files carrying whole copied sections. Their copied sections are the same text on both sides
   with names and figures swapped; `--pair A B` prints the block score by score.
2. **Fix** — the **95** files left with only small overlaps (1-3 sections at 0.50-0.85), edited line by line in the
   file's own terms instead of block-replaced.
3. **Verify** — `clone_audit.py --plan` before and after; the counters to move are *files with a whole copy*
   (**57 / 301**) and *files with small overlaps alone* (**95 / 301**).

**Open decision, flagged rather than taken:** the owner's word is "deleted". Standing rule `R-15` is growth-only
("grows rather than deletes") and `A5` forbids deleting owner content without a file-named instruction, so the clean
phase waits on one answer: delete the copied section outright, or replace it in place with fresh writing. Nothing has
been deleted; the audit remains read-only.

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
