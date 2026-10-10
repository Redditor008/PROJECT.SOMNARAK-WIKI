# Work In Progress

> *"Written down because several days of work does not survive in anybody's head."*

This file is the running state of the project. It is updated at the end of every working turn and is the authority on what has been done, what is open, and what comes next. Where it disagrees with recollection, this file is right.


**Volume split, 2026-10-09 — the record no longer fits in one file.** `WORK_IN_PROGRESS.md` had reached 718,945 B and `CHANGELOG.md` 755,141 B. GitHub truncates blobs at roughly 500 KB in the browser and stops displaying them past about 1 MB, so both were already being read in cut-off form. The closed work was moved **byte-for-byte** into numbered volumes — `WORK_IN_PROGRESS_VOL_01.md` onward, `CHANGELOG_VOL_01.md` onward — with a volume index in each live file. Nothing was rewritten, reordered within a volume, or deleted, and both splits were verified lossless line-by-line against `7b804e7`. New entries continue to go into the live files.

## M.A.W. Codex comparison — in progress (updated 2026-10-10)

**Owner directive:** compare the M.A.W. blocks inside each primary SE dossier with that entity's own Side Codex and individual Weapon, Suit and Stigma records. M.A.W. is the equipment form made from an entity's sorrow. The primary dossier is not assumed right, and a separate Codex is not copied blindly where its own slot or stat row conflicts with its description.

The re-runnable, read-only comparator is `tools/maw_compare.py`. It joins records on the SECC **Designation** inside the classification table and the Side Codex's **Source SECC Designation** — never on the filename prefix. It compares explicit fields in the matching individual Weapon, Suit, and Stigma Codices, and it now separately reads the Side Codex's embedded M.A.W. cards. `--check side` compares Side cards with primary SE blocks; `--check side-internal` compares Side cards with the individual item Codices. Fields that one source does not state are reported as review candidates, not declared defects. The Side-card parser covers 106 of 292 Side Codices: 42 full three-page stat-card sets, 36 compact bullet-card sets, five compact equipment-table card sets, and 23 identity-only M.A.W. set-page tables (name, grade, and element; no combat statistics). It parsed 318 Weapon/Suit/Stigma cards in those supported layouts: 249 stat-bearing cards and 69 identity-only records.

| Coverage | Result |
|---|---:|
| Primary SE designations parsed | **301 / 301** |
| Side Codices joined to a primary dossier | **292 / 292** |
| Complete `4/4` M.A.W. sets compared | **287 / 287** |
| Individual item records compared | **861 / 861** |
| Side Codices with a supported card/identity layout | **106 / 292** |
| Side-card records parsed in those layouts | **318 / 318** |
| Side-card / primary-block pairs compared | **318 / 861** |
| Exception sets excluded from full item comparison | **5 / 292** — four restricted / non-extractable records and Sornos' Side Codex only |
| Primary SE dossiers without an external Side Codex | **9 / 301** — five integrated A-Relics and four later dossiers with no separate Codex set |

**Resolved in this comparison pass.** The Suit review found **39 / 287** resistance profiles that were missing or contradicted the corresponding Suit Codex. All 39 now carry the item-specific four-value profile; six also received missing maximum-amount and Echo-cost fields. Suit resistance conflicts are now **0 / 287**. The expanded all-field comparator separately reports **8 / 287** Suit blocks with at least one item-Codex maximum-amount or Echo-cost value not stated in the primary (12 field rows); these are missing-field candidates, not resistance errors. Stigma statistics were restored where the primary block lacked its own Codex's slot, acquisition chance, or source-work effect; the Observing Bird's bonus now includes the Codex's additional **+4 Clarity**, and Mirror of Rising's Stigma grade is **α**. Seven individual Stigma Codex slot rows were corrected where their own physical description and the matching SE item both identified a different placement; three primary Stigma slot fields were aligned to their item Codex; the Masked Dancer and Rem entries now distinguish the registered slot from active or visible position. One primary-versus-individual Stigma-slot conflict remains, in Sorrow Fountain: its item Codex is internally divided between a Tail-slot vial record and a chest brooch description.

Three set-level contradictions were also reconciled from their own records. Amnesia now says that its two Director-signed extractions are separate from the third, 5% Stigma. The Unspoken Line now records two owner-consented shopfront extractions and a separate 5% Hand Stigma, instead of calling the set only two pieces. The Extinguished now distinguishes its one completed extraction and three registered equipment forms from the failed second attempt still held in the shelter. The Seam Edge's missing weapon statistics were filled from its own item Codex.

**Weapon review — first confirmed corrections (2026-10-09).** Weighting Bird `C-IIIγ-032` now gives its double-barrel Scale-Pistol the 7–12 Grudge damage, Fast speed, three-target line and 100% → 70% → 50% falloff recorded for that same appearance in its Weapon Codex; the dossier had said 12–18, Normal, two targets and 100% → 60%. Weeping Statue `C-IIβ-055` now gives its same travertine stiletto the Codex's 5–9 Lament damage and Normal speed, replacing 6–10 and Fast. Briar `C-IIIγ-145` now uses the same-form Codex and Side-card values for damage, speed, Skewer coverage and falloff; **Range remains untouched** because the Codex's stat row says 3 — Medium while its own Appearance says the harpoon shoots across Range 4. The record conflicts with itself, so one side was not chosen by fiat.

**Growth and regression check.** **46 / 301** primary dossiers changed: **39 / 46** grew, **7 / 46** stayed the same length, and **0 / 46** became shorter (`R-02`). The three newly checked files measured **7,730 → 7,735 words**, **7,705 → 7,705**, and **7,569 → 7,579**. Seven individual M.A.W. item Codex records also grew when their slot metadata was corrected against their own item form. Exact Codex bearer-cost sentences initially introduced **13 / 301** cross-dossier wording matches; those 17 cost lines were re-authored in each item's own terms, and the final couples gate remains **0 / 301** with **0 / 301** files carrying a couple.

**Still open; do not auto-rewrite.** The direct primary-versus-individual comparison has **146 / 861** item-name candidates. Of the **287 / 287** complete Weapon pairs, **94 / 287** blocks have at least one finding; **26 / 287** have a conflicting value and **74 / 287** omit at least one field stated in the item Codex (overlap). The per-field counts below distinguish conflicts from a value absent in the primary block; absence is not itself proof of a defect.

| Weapon field | Conflicts in primary / 287 | Item-Codex value not stated in primary / 287 |
|---|---:|---:|
| Damage | **16 / 287** | **9 / 287** |
| Speed | **16 / 287** | **9 / 287** |
| Range | **21 / 287** | **9 / 287** |
| Maximum amount | **0 / 287** | **9 / 287** |
| Echo cost | **0 / 287** | **9 / 287** |
| Grade | **0 / 287** | **3 / 287** |
| Element | **0 / 287** | **3 / 287** |
| Attack pattern | **14 / 287** | **53 / 287** |
| Target coverage | **1 / 287** | **42 / 287** |
| Falloff | **2 / 287** | **34 / 287** |

Suit resistance conflicts remain **0 / 287**; eight Suit blocks have at least one item-Codex maximum-amount or Echo-cost field not stated. The **1 / 287** direct Stigma-slot conflict is Sorrow Fountain. The comparator ignores an omitted damage-element label when the numeric band agrees, checks explicit speed/range descriptors, and now compares attack pattern, target coverage, and falloff as separately parsed fields.

**Initial structured Side-card screen (2026-10-09; baseline):** the comparison covered **83 / 292** Side Codices with a recognized layout and parsed **249 / 249** cards. At that screen, **25 / 249** cards had at least one stat conflict, **31 / 249** had a Side-stated value not present in the primary block, and **81 / 249** had a name difference; the groups overlapped. Side-versus-item flagged **14 / 249** stat-conflict cards and **70 / 249** name differences. These were candidates, not defects: names may be aliases and a card may describe another form. The other **209 / 292** Side Codices had no recognized layout. These are opening-scan figures; the live Weapon conflict queues are recorded below.

**Side-layout expansion, Batch 87 (2026-10-10; commit `1b6fa2fa`):** the read-only parser now recognizes 23 `PAGE 03 — M.A.W. SET PAGE` identity tables. It reads only piece name, grade, and element; it does not invent damage, speed, range, pattern, coverage, or falloff, and the test suite confirms that detailed cards keep precedence. Live parser coverage is **106 / 292** layouts and **318 / 861** Side/primary pairs (249 stat-bearing cards plus 69 identity-only records). The new layout screen surfaced five additional Side Weapon name candidates; Batch 87 dispositions three and leaves `C-Iα-011` and `C-IIIγ-062` for later review. The other **186 / 292** Side Codices still have no recognized layout; that separate audit remains open.

**Initial spot-review snapshot (2026-10-09):** no additional Weapon or name candidate was confirmed in that initial review. A spot review left Emberling `C-IIβ-101`, Rem `C-IIβ-135`, Unrung `C-IIβ-170`, Rage Statue `C-IIIγ-190`, Pall `C-IIβ-280`, and Timber Maw `C-IVγ-205` unchanged where core statistics, the primary block, and the item's own Appearance either disagree or describe different forms. Sorrow Fountain's Stigma remains split: the Side Codex/item identity says Tail-slot vial, while the item's Appearance and primary block describe a chest brooch; the Side card and item record say 4%, while the master registry says generic Accessory / 5%. Its Weapon remains held as well: Side/item core stats say 7–12, Fast 3, Medium 3, while the primary says 10–16, Normal 3, Long 4; the item's Resting / Active form says blade, but its Appearance describes the primary block's wand-mace. Briar's Weapon remains held: primary/linked Appearance says Range 4 while item/Side core says Range 3 — Medium; the item's Resting/Active fields describe a fang blade/defensive line rather than the rifle Appearance, with no documented transition. Its formal 7–12 band also conflicts with the primary Registry Addendum's needle-gun 11–17 summary. Preserve all records; do not select a value. Do not choose a disputed value by copying only one source. **At Batch 86 close (2026-10-10), cumulative source-led Weapon coverage is 34 / 287 eligible complete pairs (11.8%), with 253 / 287 lacking an individual disposition.** Against all primary dossiers, 34 / 301 (11.3%) have a source-led disposition and 267 / 301 remain without one; the automated screen remains 287 / 287, with 14 / 301 outside paired scope. Batches 80–84 added 15 / 15 unique dispositions, all held; Batch 85 added three supported Side-card profile corrections; Batch 86 adds three more, with residual Lens wording in Hollow Saint’s linked item and Fang/Skewer wording in Pyre’s linked item explicitly held on their Side pages. The primary-versus-item conflict screen remains 23 / 23, with one undispositioned case, Stormscale Sovereign `C-Vδ-949`. The live `--check side` Weapon slice has 9 unique primary/Side stat-conflict cards, all individually dispositioned; `--check side-internal` has 3 conflict cards, all individually dispositioned. Missing-only findings remain separate and are not defects by themselves. The primary *Hollow Tree* / Side *Timber Maw* distinction for `C-IVγ-205` remains unchanged. At that time, the separate structured-layout audit beyond the then-supported 83 Side Codex layouts remained open; Batch 87's expanded 106-layout coverage and the 186 still-unrecognized Side Codices are recorded below.

This comparison began as a standalone audit. On 2026-10-10, the owner explicitly reopened M.A.W. case review as Batch 76, separate from the completed cross-dossier text-overlap fix phase. A *couple* is a pair of dossier sections linked by matching distinctive wording; this M.A.W. batch does not reopen or change that fix phase.

**Batch 76 — CLOSED at three dossiers (2026-10-10).** The owner explicitly reopened M.A.W. reconciliation as a batch. This work remains separate from the completed cross-dossier text-overlap repair phase. The cases require form research, so the batch stays at the R-26 floor of three rather than expanding to five.

| Unit | Dossier | Outcome | Commit | Push |
|---|---|---|---|---|
| 1 / 3 | [Cracked_Flesh](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-921_Cracked_Flesh_%EA%B7%A0%EC%97%B4%EC%9D%98_%EB%93%A4%ED%8C%90.md "SE-C-IIIγ-921_Cracked_Flesh_균열의_들판.md") `C-IIIγ-921` | Spike/tendril profiles labeled; stats retained | `fae0d74` | PUSH VERIFIED |
| 2 / 3 | [Broken_Clock](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-044_Broken_Clock_%EB%B6%80%EC%84%9C%EC%A7%84_%EC%8B%9C%EA%B3%84.md "SE-C-IIIγ-044_Broken_Clock_부서진_시계.md") `C-IIIγ-044` | Held; one polearm, unexplained profile conflict | `06c5754` | PUSH VERIFIED |
| 3 / 3 | [Pall](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-280_Pall_%EB%88%88%EB%AC%BC%EC%9D%98_%EB%B2%A0%EC%9D%BC.md "SE-C-IIβ-280_Pall_눈물의_베일.md") `C-IIβ-280` | Held; primary, Side, and item describe different forms | `58c4dca` | PUSH VERIFIED |


**Unit 3 / 3 — Pall `C-IIβ-280` (held).** The primary calls the Weapon *The Surgeon's Cleaver* and describes a 22 cm triangular stiletto, but its pattern and Ability add a shield-bash and launched javelin. The Side Codex names a pavise and javelin, while its linked item's own Appearance describes a singing chalice; the item statistics say Lament 5–9, Speed 2, Range 2, Single. The master listing calls it a stiletto but repeats the pavise/javelin name in its detail entry. These descriptions do not establish one intended form, so no profile was copied and no primary or item value changed.

**Batch 76 status:** 3 / 3 dossier dispositions recorded — one form mapping clarified and two cases held. The held profiles remain open; next candidate is Emberling `C-IIβ-101`.

**Batch 77 — OPEN at five (2026-10-10).** The owner directed five M.A.W. checks and fixes per prompt. Review the next five held candidates from the source-led queue; no profile is copied unless descriptions, appearance, and form identity support it.

**Unit 1 / 5 — Emberling `C-IIβ-101`:** the Side Codex Stigma card said `Tail`, but the primary and linked item D identify a neck/collar brooch; item D's Appearance says it is pinned over the collar. I corrected the Side slot to `Neck / Collar`. The suit Codex heading also now uses the full official name already stated in its identity table, primary, and Side set record. The Weapon remains held: primary and item Appearance describe the Cinder-Breech Carbine, while the item identity and Core Statistics describe a blue blade and a short Single profile; no blade-to-carbine transition is documented, so no weapon value changed.

**Unit 2 / 5 — Rem `C-IIβ-135`:** the linked Suit Codex heading said *The Warm Shroud*, while its own Official name, the primary, and the Side set record say *The Somnolent Gossamer Shroud*; the heading now matches the recorded name, with its mechanics unchanged. The Weapon’s primary, title, type, Appearance, and master entry describe three levitating prisms, but its linked item identity/resting-active fields and Core Statistics, repeated by the Side card, describe a blue blade and a short Single strike. No prism-to-blade transition is documented, so the Weapon profile remains held and no values were copied.

**Unit 3 / 5 — Unrung `C-IIβ-170`:** the primary Weapon and the linked item’s Appearance describe a five-globe brass Orrery, but the item identity, Core Statistics, Side stat card, and master listing identify a Muffled Resonance-Bell / Silence Hammer profile. The linked item itself mixes those two forms, and no transition from bell or hammer to Orrery is recorded. I held the Weapon conflict without changing any values.



**Unit 4 / 5 — The Rage Statue `C-IIIγ-190`:** the Weapon remains held. The primary and master record identify the Vein-Heated Marble Brand, while the Side/item profile says Ash-Phoenix Culverin; the master catalog assigns that culverin to The Ember Phoenix (Entry 667), and no transfer or form transition is documented. I also kept the Suit label unresolved: the primary, Side set identity, item heading, and Appearance identify the Sculptor’s Flame-Hardened Apron & Cuirass, but the Side card and linked item’s function/maintenance text repeatedly call it a Rage Gauntlet and mention fist plates/palm seam. The evidence does not establish whether those are aliases or a leftover physical-form record, so neither label nor weapon statistics were changed.

**Unit 5 / 5 — Hollow Tree / Timber Maw `C-IVγ-205`:** I am keeping the naming difference visible: the primary calls it Hollow Tree, while the Side Codex calls the same designation Timber Maw. The primary and master Entry 217 identify the Ravenous Timber-Jaw as a two-metre cleaver, but the Side and linked item describe a staff with a different profile and no recorded transition; the Weapon remains held and no value changed. The Side Suit card’s *The Hollow Mantle* differs from the primary, set identity, and item’s *The Hollow Bark-Carapace*, but the documented Appearance itself describes a bark mantle, so I left it as a plausible short label rather than declaring it wrong. Likewise, Unrung’s *The Silence Veil* remains a possible shorthand: its formal Soundless Velvet Cassock identity and Appearance agree across the primary, set identity, and item, and that item’s own prose calls it the Veil. Neither label was changed without evidence that it names a different form.

**R-19 check and Batch 77 close:** R-19 applies to all five entities. Emberling, Rem, Unrung, The Rage Statue, and Hollow Tree already have Neutral rows with dossier evidence in `ENTITY_DISPOSITION_INDEX.md`; this equipment review changes none of that evidence, so no disposition changed. Batch 77 closes at **5 / 5**: three non-weapon corrections were confirmed (Emberling’s Stigma slot and suit heading, Rem’s suit heading); all five Weapon profiles remain held, and the Rage Statue Suit label/form also remains unresolved.

**Batch 78 — CLOSED at 5 / 5 (2026-10-10).** The owner asked to carry the research-based Weapon reconciliation through both the primary SE records and their Side/item Codices. A changed number is used only where the physical form and attack description identify the matching profile; any remaining undocumented form relationship stays held.

**Unit 1 / 5 — Emberling `C-IIβ-101`:** the primary, master Entry 121, and linked item’s own Appearance identify the 85cm Cinder-Breech Carbine, its lever-fed ember burst, and three high-velocity projectiles reaching Range 4. The linked item's Resting/Active identity and statistics, plus the Side card, instead described a short blue blade and a Single strike. I aligned those M.A.W. records to the carbine profile: Lament 6–11, Normal 3, Long 4, forward cone up to three targets, and 100% / 60% impact falloff; the already-supported primary weapon block was not changed.

**Unit 2 / 5 — Rem `C-IIβ-135`:** the primary, master Entry 127, and the linked item’s Appearance show three telekinetically suspended prisms launching across Range 4 and returning to orbit. The linked identity and Core Statistics, repeated by the Side card, described a short blue blade; I aligned those two M.A.W. records to the documented prism profile: Lament 6–10, Fast 4, Long 4, Tri-Prism Dart / Somnolent Orbit, and the recorded single-target or three-vector coverage and falloff. The primary block was already consistent and remains unchanged.

**Unit 3 / 5 — Unrung `C-IIβ-170`:** the initial Orrery reading was overturned by the source comparison. Unrung’s primary title and five-globe Appearance duplicate Aphonia `SE-N-IIβ-170`’s existing *Resonant Echo-Orrery* weapon block; that shared text is copy evidence, not independent confirmation. Unrung’s linked item identity/resting-active forms and the Side stat card give the same Muffled Resonance-Bell / Silence Hammer profile: Void 5–9, Normal 2, Short 2, one target, no secondary falloff; master Entry 130 confirms the canonical Bell name, Reliquary class, and silence effect. I corrected the primary block and the linked item’s copied Appearance/type to the bell-headed Han-glass hammer profile, clarified *Silence Hammer* as the Side card’s descriptive alias, and aligned the hearing-check schedule. Master Entry 130 was already consistent and remains unchanged. The primary’s roughly one-hour half-second hearing lag remains in its narrative; other records carry the corroborated one-hour and one-day hearing-check requirement rather than treating the lag as an additional stat.

**Unit 4 / 5 — The Rage Statue `C-IIIγ-190`:** the primary Weapon block, Side set row, and master Entry 67 identify the Vein-Heated Marble Brand, a blunt hafted weapon whose striking head is a marble forearm and clenched fist. The linked item's *Ash-Phoenix Culverin* title and Appearance were copied verbatim from Ember Phoenix's primary M.A.W. block; the master index also lists that Culverin under Ember Phoenix (Entry 667), although the detailed Entry 667 calls its weapon *The Rebirth Fang*. I corrected the Rage Statue item title/identity/Appearance to the Brand and clarified *Rage Fang* as its legacy Side/item-path alias; the Side card now uses the canonical name. **Weapon numbers remain held:** primary = Grudge 12–19, Slow 2, Short 2, Overhand Crush / Thermal Eruption, target plus 3m ground starburst; item and Side = Grudge 7–12, Fast 3, Medium 3, Skewer / 100% → 70% → 50%. Maximum 3 and 40 Echoes agree, but no third Brand-specific record resolves the attack-stat conflict. **Suit remains held:** the primary, Side set identity, item heading/Appearance, and master Entry 68 identify the Flame-Hardened Apron & Cuirass, while the item’s binding/function/maintenance and Side card repeatedly describe a Rage Gauntlet with fist plates and a palm seam. The physical prose does not establish whether those are components or a stale form record; resistance, maximum, and cost agree, so I changed no Suit label or statistics.

**Unit 5 / 5 — Hollow Tree / Timber Maw `C-IVγ-205`:** the primary name *Hollow Tree* and Side name *Timber Maw* remain distinct for the same designation. Primary and master Entry 217 describe the *Ravenous Timber-Jaw* as a two-metre cleaver (Weight 12–20, Slow 2, Range 3, Masticating Cleave / Heavy Chomp); the Side card calls it *The Hollow Staff* and gives a Han-absorption staff profile (Weight 7–12, Fast 3, Range 3, Skewer, up to three targets, 100% → 70% → 50%), repeated by the linked item’s own identity, function, and appearance. The primary Weapon block itself also contains the staff’s second stat set and Han-absorption ability alongside its cleaver description, but does not document a mode change or explain how the forms relate. The two forms therefore remain unresolved; no weapon name or value was transferred. The Side Suit’s *Hollow Mantle* remains a plausible shorthand for the item’s *Hollow Bark-Carapace*, since its own Appearance describes a bark mantle; no Suit rename was needed.

**Batch 78 close:** Units 1–3 aligned the linked weapon records to the supported primary profiles. Unit 4’s copied Culverin identity/Appearance was corrected to the Marble Brand, while numeric and Suit-form conflicts remain held. Unit 5’s cleaver/staff conflict remains held. All five dossier units have passed their per-unit gate and were pushed to the assigned branch.

**Batch 79 — CLOSED at 3 (2026-10-10).** Interpreting the owner’s “P” as continuing the individual Weapon review, I selected three already-recorded open cases without padding: Sorrow Fountain `C-IIIγ-088`, Briar `C-IIIγ-145`, and Pall `C-IIβ-280`.

**Unit 1 / 3 — The Sorrow Fountain `C-IIIγ-088`:** the primary, item heading/Official name, Side set row, and master Entry 43 name the *Weeping Basin-Aspergillum*. Its detailed Appearance in the primary and item is identical and describes a fluid-delivery wand-mace, while the item’s Resting/Active fields, Side card, and combat prose describe a blade; the Side card also used *The Sorrow Requiem*, a title present in Mourner’s Bloom’s weapon records. The primary’s numeric profile is Lament 10–16, Normal 3, Long 4, 60-degree cone up to four targets, 100% / 75%; item and Side give 7–12, Fast 3, Medium 3, Skewer, 100% → 70% → 50%. Master Entry 43 confirms the canonical Basin name but its index category is Reliquary — Censer/Bell, unlike the primary’s Magic/Blunt label, and supplies no numbers. With no documented form transition or base/special split, I changed only the Side-card title to the canonical name and marked the profile held; no statistics or physical form were selected. The separate Stigma slot conflict was not changed in this Weapon unit.

**Unit 2 / 3 — Briar `C-IIIγ-145` (held):** the primary M.A.W. heading, linked item's Official name/Appearance, Side set row/card, and master registry identify *The Briar-Spool Needle Gun*; the primary and linked Appearance both describe a 105 cm pneumatic rifle/harpoon, with identical wording. The primary, item core, and Side card agree in their formal stat fields on Speed 3 (Fast), three-target Skewer, 100% → 70% → 50% falloff, 40 Echoes, and 7–12 Grudge damage. Range remains unresolved: primary says 4 (Long, 5–20 m), item Appearance says the pneumatic harpoon shoots across Range 4, but item core and Side card say 3 (Medium). The repeated Appearance is not independent corroboration. A second damage conflict appears in the primary Registry Addendum’s digit summary (“needle gun 11–17 at 40 Echoes”), against 7–12 in the formal blocks; the master registry lists `DMG: Variable` and `RNG: -`, while the archetype index only confirms GUN / RANGE. The linked item's Resting/Active fields describe a crimson fang blade and defensive line rather than the rifle in Appearance, and no transition or stat split is documented. I changed no values or forms; the Side card now records the explicit range/damage/form hold. The primary's Registry Addendum says field contradictions are data and lines should remain as written, which supports preserving rather than silently reconciling them.

**Unit 3 / 3 — Pall `C-IIβ-280` (held; prior hold reaffirmed):** the primary calls it *The Surgeon's Cleaver* and describes a 22 cm triangular surgical stiletto, but its pattern/Ability add shield-bash and javelin attacks; its Damage Application says no weapon has cut anyone and the cleaver is an armoury name for the object kept in the outer room. The linked item's heading, Side set row, and master CSV use *The Weeping Veil-Pavise & Tear Javelin*; the item introduction instead calls it a short singing blade and its Appearance a deep-blue singing chalice. The Side compact card calls it *Tear Requiem* (also used by separate `MAW-W-041`). Numeric profiles conflict: primary Lament 6–10 / Slow 2 / Medium 3 / shield-bash-javelin / one target / 100% close and 80% javelin versus item Lament 5–9 / Normal 2 / Short 2 / Single 100%; Side follows the item's 5–9 / 2 / 2 / Single. Maximum 4 and 25 Echoes agree. Master CSV names Pavise/Javelin but leaves DMG variable and SPD/RNG unset; the archetype index instead lists Surgeon's Cleaver / mirror-polished square cleaver / Close. No record documents a form transition or base-versus-special split. No name, form, or disputed value changed; the Side card now states the hold.

**Batch 79 close:** three dossier units completed at the R-26 floor, without padding. Sorrow Fountain received only a Side-card title alignment; its weapon profile remains held. Briar and Pall remain held; no disputed numbers, forms, or names were selected or changed. Every unit passed its per-dossier gate and was pushed to the assigned branch.

| Unit | Primary SE dossier | Disposition | Unit commit | Push |
|---|---|---|---|---|
| 1 / 3 | [[SE-C-IIIγ-088_The_Sorrow_Fountain_슬픔의_분수](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-088_The_Sorrow_Fountain_%EC%8A%AC%ED%94%94%EC%9D%98_%EB%B6%84%EC%88%98.md "SE-C-IIIγ-088_The_Sorrow_Fountain_슬픔의_분수.md")] `C-IIIγ-088` | Side title aligned; form and stats held | `075a2baf` | PUSH VERIFIED |
| 2 / 3 | [[SE-C-IIIγ-145_Briar_가시의_정원](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-145_Briar_%EA%B0%80%EC%8B%9C%EC%9D%98_%EC%A0%95%EC%9B%90.md "SE-C-IIIγ-145_Briar_가시의_정원.md")] `C-IIIγ-145` | Range, damage, and form held | `1acf773d` | PUSH VERIFIED |
| 3 / 3 | [[SE-C-IIβ-280_Pall_눈물의_베일](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-280_Pall_%EB%88%88%EB%AC%BC%EC%9D%98_%EB%B2%A0%EC%9D%BC.md "SE-C-IIβ-280_Pall_눈물의_베일.md")] `C-IIβ-280` | Name, form, and profile held | `02eb07d2` | PUSH VERIFIED |

**Batch 80 — CLOSED at 3 (2026-10-10).** To show progress against the whole eligible review set—not just each batch—I am carrying forward the documented unique-dossier count. At Batch 79 close: **13 / 287** complete Weapon-pair dossiers had a source-led Weapon disposition (**4.5%**, **274 / 287** not yet individually reviewed); the comparator has screened **287 / 287** eligible pairs. The corpus contains **301** primary SE dossiers; **14** do not enter this complete-pair denominator (9 without an external Side Codex and 5 exception sets). Batch 80 takes the next three unreviewed primary Weapon profile candidates in comparator order: The Inherited Debt `N-IVβ-019`, The Cracked Hourglass `C-IIIβ-036`, and The Masked Dancer `C-IIβ-099`. Holds count as reviewed dispositions; duplicate re-reviews do not increment the unique count.

**Unit 1 / 3 — The Inherited Debt `N-IVβ-019` (held):** the primary and master archetype favor the named signet/ring and cone-gravity archetype, but the linked item's Appearance and use history repeatedly describe a two-handed maul/direct strike; the Side set row calls it a signet and “direct impact.” The primary itself has both `Conical Gravity Wave / Posture Crush` and a later Single / one-target / 100% formal line, and says it will not discharge against groups; the item combat record says Single. Damage 5–9, Normal 2, Short 2, maximum 4, and 25 Echoes match between primary and item; master CSV values are variable/unset, and the Side has no stat card. No form transition or rule resolves the ring/cone and maul/single-impact records. No source value changed; the Side set page records the hold. **Cumulative source-led progress: 14 / 287 (4.9%); 273 / 287 eligible dossiers remain unreviewed.**

**Unit 2 / 3 — The Cracked Hourglass `C-IIIβ-036` (held):** the primary and linked item repeat the same 35 cm floating Orrery / Range 4 beam Appearance verbatim, so it is not independent evidence. The item's core row instead calls it an Hourglass Sledge / Sand-Clock Hammer and gives Weight 9–16, Very Slow 1, Room 5, Ground Shockwave / Temporal Drag; its ability/history call it a maul whose stored action hits the chamber floor. The primary gives Weight 8–13, Normal 3, Long 4, Concentric Beam / Chrono-Singularity, line plus 4 m vortex, and 100% / 60%; the Side set row says “single impact.” Master registry supports the Orrery name, 9–16, maximum 4, and 25 Echoes but gives no speed/range; the archetype index also names the Orrery but says Short. No form transition or base/special split resolves the competing object/profile descriptions. No values changed; the Side set page now records the hold. **Cumulative source-led progress: 15 / 287 (5.2%); 272 / 287 eligible dossiers remain unreviewed.**

**Unit 3 / 3 — The Masked Dancer `C-IIβ-099` (held):** the primary first describes three telekinetic daggers with Grudge 4–8 per strike, three strikes, Fast 4, Medium 3, and Tri-Blade Flurry / Telekinetic Skewer; the linked item's Official name, the Side set row, and the master title/archetype support the Tri-Daggers identity; the item Core Statistics align with that first profile. The primary then includes a second unlabeled 5–9 / Normal 2 / Short 2 / Single / 100% profile; the Registrum also says “the glove's daggers at 5–9.” The Side card calls it *The Dancing Fang* and repeats 5–9 / 2 / 2 / Single, while the linked item's Appearance and Combat File describe one short crimson blade. The master CSV leaves damage variable and speed/range unset; its archetype confirms Tri-Daggers but gives a Short band. Maximum 4 and 25 Echoes agree. No transition or base-versus-special split resolves the three-dagger and single-Fang records, so no name/profile was changed; the Side card now records the hold. **Cumulative source-led progress: 16 / 287 (5.6%); 271 / 287 eligible dossiers remain unreviewed.**


**Batch 80 close:** three new unique dossiers received source-led dispositions. All three conflicts remain held; no primary SE or linked Weapon item values were changed. Each Side Codex now records the hold, each unit passed its own gate and was pushed, and duplicate reviews were not counted again.

| Unit | Primary SE dossier | Disposition | Cumulative source-led progress | Commit |
|---|---|---|---|---|
| 1 / 3 | [[SE-N-IVβ-019_The_Inherited_Debt_물려받은_빚](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-IV%CE%B2-019_The_Inherited_Debt_%EB%AC%BC%EB%A0%A4%EB%B0%9B%EC%9D%80_%EB%B9%9A.md "SE-N-IVβ-019_The_Inherited_Debt_물려받은_빚.md")] `N-IVβ-019` | Ring/cone vs maul/Single held | `14 / 287` · `273` remain | `012f5d09` |
| 2 / 3 | [[SE-C-IIIβ-036_The_Cracked_Hourglass_금이_간_모래시계](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B2-036_The_Cracked_Hourglass_%EA%B8%88%EC%9D%B4_%EA%B0%84_%EB%AA%A8%EB%9E%98%EC%8B%9C%EA%B3%84.md "SE-C-IIIβ-036_The_Cracked_Hourglass_금이_간_모래시계.md")] `C-IIIβ-036` | Orrery/beam vs hammer/shockwave held | `15 / 287` · `272` remain | `b4d3a0aa` |
| 3 / 3 | [[SE-C-IIβ-099_The_Masked_Dancer_가면_무용수](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-099_The_Masked_Dancer_%EA%B0%80%EB%A9%B4_%EB%AC%B4%EC%9A%A9%EC%88%98.md "SE-C-IIβ-099_The_Masked_Dancer_가면_무용수.md")] `C-IIβ-099` | Tri-Daggers vs single Fang held | `16 / 287` · `271` remain | `f05c74bc` |

**Cumulative progress after Batch 80 (not a batch-local fraction):**

| Measure | Completed | Total | Remaining | Coverage |
|---|---:|---:|---:|---:|
| Automated screen of complete Weapon pairs | `287` | `287` | `0` | **100%** |
| Unique source-led Weapon dispositions | `16` | `287` | `271` | **5.6%** |
| Same source-led dispositions, measured against all primary SE dossiers | `16` | `301` | `285` | **5.3%** |

The full corpus has **301** primary SE dossiers; **14** are outside the complete-pair Weapon scope (9 without an external Side Codex and 5 exception sets). The **271 / 287** are eligible dossiers without a documented individual source-led disposition—not 271 known defects or required edits. Holds count as dispositions; repeated reviews do not increase the unique count. The 16 counted designations are `C-IIIγ-032`, `C-IIβ-055`, `C-IIIγ-145`, `UNK-251`, `C-IIIγ-921`, `C-IIIγ-044`, `C-IIβ-280`, `C-IIβ-101`, `C-IIβ-135`, `C-IIβ-170`, `C-IIIγ-190`, `C-IVγ-205`, `C-IIIγ-088`, `N-IVβ-019`, `C-IIIβ-036`, and `C-IIβ-099`.


**Source-led cumulative coverage entering Batch 81: 16 / 287 (5.6%), with 271 / 287 eligible dossiers still lacking an individual disposition.** The comparator has automatically screened **287 / 287** complete pairs; the full primary-SE corpus is **301**, with **14** outside this paired scope. **Batch 81 opens at three** with the next three primary-versus-item conflict candidates in the current `--check weapon` order, after excluding previously dispositioned dossiers: Frozen Tear `C-IIβ-102`, I Alone Crossed `C-IVδ-106`, and Weeping Willow `C-IIIγ-140`. The review-history check found only unrelated prior work on these files: Frozen Tear's Batch 62 changes concerned baseline entity text/stat rows, I Alone Crossed appears in earlier couple planning, and Weeping Willow's earlier edits were base-stat/couple work. None had a prior individual Weapon disposition.

**Unit 1 / 3 — Frozen Tear `C-IIβ-102` (held):** the primary identifies *The Glacial Tear-Mirror* and describes an oval handheld tear-clear ice mirror in tarnished silver that refracts a focused beam across Range 4; its card is Lament 6–10 / Fast 4 / Long 4 / Focused Frost-Ray / Freezing Skewer. The Icedrop Side Codex has the same source designation `C-IIβ-102`, the event in which the mourner's first and only tear froze before it fell, and the same item name; its card and linked `SE-1010-B` instead repeat Lament 5–9 / Normal 2 / Short 2 / Single. The individual item has no separate Appearance section documenting a close-range form. The master registry leaves damage/speed/range variable or unset; the archetype index's `MAW-W-1010` row describes a short chiseled-bone bodkin, but no cross-reference explains its relationship to the `MAW-W-1010-01` mirror record. No transition or base/special split resolves these profiles; no values changed, and the Side Codex now records the hold. **Cumulative source-led progress: 17 / 287 (5.9%); 270 / 287 eligible dossiers remain without an individual disposition.**

**Unit 2 / 3 — I Alone Crossed `C-IVδ-106` (held):** the primary and linked item name *The Survivor's Span-Cleaver* and depict a fractured suspension-girder greatsword with trailing cables and a broad frontal sweep. They agree on Lament 14–22 / Slow 2 / Medium 3 / Sweeping Cleave–Structural Sever, explicit up-to-three-target coverage, and 100% → 70% → 50% falloff; the master row leaves numbers variable/unset and archetype row confirms a medium zweihander. The Side card instead calls it *I Alone Crossed Requiem* and gives Lament 10–15 / Fast 3 / Medium 3 / Skewer up to three, with the same falloff. The item calls its basic/signature action a blue Skewer line, but no record maps the Side values to a separate ability or alternate form. The linked item's Appearance supports the primary greatsword, while the Side card has no alternate Appearance. The `weapon` comparator's primary-item pattern difference results from splitting the slash-separated name; its reported missing coverage is already stated in the primary's `Target Coverage` line. The genuine Side-card profile conflict remains unresolved; no value, profile, or title changed, and the Side Codex now records the hold. **Cumulative source-led progress: 18 / 287 (6.3%); 269 / 287 eligible dossiers remain without an individual disposition.**

**Unit 3 / 3 — Weeping Willow `C-IIIγ-140` (held):** the primary and linked `SE-140-B` name *The Weeping Willow War-Scythe* and describe the same long willowwood haft, crescent Lament-crystal head, flexible tear-bearing tendrils, and sweeping/reaping motion. Both give Lament 9–15 / Normal 3 / Medium 3 / Reaping Arc–Cascading Sigh / up to three targets / 100% → 70% → 50% falloff. The Side card instead calls it *The Willow Requiem* and records Lament 7–12 / Fast 3 / Medium 3 / Skewer up to three, with the same maximum, cost, and falloff; it gives no alternate Appearance. The item also describes its basic/signature attack as a Skewer line, but no document maps the Side values to an ability profile or another form. The archetype index assigns `MAW-W-140` a Short band, whereas the primary, item, and Side card say Medium; the master row leaves damage/speed/range unset. The primary-item `weapon` pattern candidate is a slash-parsing artifact; the separate Side comparison confirms the real profile divergence. No profile, title, or reach value changed; the Side Codex now records the hold. **Cumulative source-led progress: 19 / 287 (6.6%); 268 / 287 eligible dossiers remain without an individual disposition.**

**Cumulative source-led coverage after Batch 81: 19 / 287 (6.6%), with 268 / 287 eligible dossiers still lacking an individual disposition. Batch 81 closed at three (2026-10-10).** Three new unique dossiers received source-led Weapon dispositions; all three remain held. No disputed primary or linked-item Weapon statistics, forms, or titles changed. Each Side Codex now states the evidence and why it does not resolve the profile. All three unit commits passed their per-dossier gate and were push-verified on the assigned branch.

| Unit | Primary SE dossier | Disposition | Cumulative source-led progress | Commit | Push |
|---|---|---|---|---|---|
| 1 / 3 | [[SE-C-IIβ-102_Frozen_Tear_얼어붙은_눈물](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-102_Frozen_Tear_%EC%96%BC%EC%96%B4%EB%B6%99%EC%9D%80_%EB%88%88%EB%AC%BC.md "SE-C-IIβ-102_Frozen_Tear_얼어붙은_눈물.md")] `C-IIβ-102` | Glacial mirror beam vs short Single profile held | `17 / 287` · `270` remain | `27faa82e` | PUSH VERIFIED |
| 2 / 3 | [[SE-C-IVδ-106_I_Alone_Crossed_부서진_다리](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-106_I_Alone_Crossed_%EB%B6%80%EC%84%9C%EC%A7%84_%EB%8B%A4%EB%A6%AC.md "SE-C-IVδ-106_I_Alone_Crossed_부서진_다리.md")] `C-IVδ-106` | Span-Cleaver vs Requiem profile held | `18 / 287` · `269` remain | `15e7cfe6` | PUSH VERIFIED |
| 3 / 3 | [[SE-C-IIIγ-140_Weeping_Willow_우는_버드나무](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-140_Weeping_Willow_%EC%9A%B0%EB%8A%94_%EB%B2%84%EB%93%9C%EB%82%98%EB%AC%B4.md "SE-C-IIIγ-140_Weeping_Willow_우는_버드나무.md")] `C-IIIγ-140` | War-Scythe vs Requiem profile/reach held | `19 / 287` · `268` remain | `dc4326d8` | PUSH VERIFIED |

**Cumulative progress after Batch 81 (not a batch-local fraction):**

| Measure | Completed | Total | Remaining | Coverage |
|---|---:|---:|---:|---:|
| Automated screen of complete Weapon pairs | `287` | `287` | `0` | **100%** |
| Unique source-led Weapon dispositions | `19` | `287` | `268` | **6.6%** |
| Same source-led dispositions, measured against all primary SE dossiers | `19` | `301` | `282` | **6.3%** |

The full corpus has **301** primary SE dossiers; **14** are outside the complete-pair Weapon scope (9 without an external Side Codex and 5 exception sets). The **268 / 287** are eligible dossiers without a documented individual source-led disposition—not known defects or required edits. Holds count as dispositions; repeated reviews do not increase the unique count. The 19 counted designations are `C-IIIγ-032`, `C-IIβ-055`, `C-IIIγ-145`, `UNK-251`, `C-IIIγ-921`, `C-IIIγ-044`, `C-IIβ-280`, `C-IIβ-101`, `C-IIβ-135`, `C-IIβ-170`, `C-IIIγ-190`, `C-IVγ-205`, `C-IIIγ-088`, `N-IVβ-019`, `C-IIIβ-036`, `C-IIβ-099`, `C-IIβ-102`, `C-IVδ-106`, and `C-IIIγ-140`.

**Batch 82 — opened at three (2026-10-10).** Entering cumulative source-led coverage was **19 / 287 (6.6%)**, with **268 / 287** eligible complete-pair dossiers lacking an individual disposition. The automatic screen remains **287 / 287**; the full primary-SE corpus is **301**, with **14** outside scope. After checking review history and excluding prior dispositions, the next three conflict-status candidates were Owed `C-IIIγ-180`, Frozen Window `C-IIβ-330`, and Clapperless `C-IIβ-340`. The history check found Owed's earlier grade/prose and couple entries, Frozen Window's Batch 61 shared-stat-row rewrite, and Clapperless's general cleanup/edit records; none was an individual Weapon disposition. Missing-only findings remain separate: an omitted field is not a defect by itself.

**Unit 1 / 3 — Owed `C-IIIγ-180` (held):** the primary's *Sarcophagus Wall-Ram* first describes a massive mortared-masonry ram / mobile bastion with Weight 12–20, Very Slow 1, Room 5, and Bastion Charge / Seismic Impact; the same block then gives an unlabeled Weight 7–12 / Fast 3 / Medium 3 / Skewer profile for up to three targets with 100% → 70% → 50% falloff. The Side card and `SE-180-B` give that latter profile and describe a broad black, ledger-lined maul. The master registry keeps the Wall-Ram name but leaves its numeric profile variable / unset; archetype `MAW-W-180` describes a long wall-battering ram / mobile bastion. No source identifies a separate mode or form, so neither profile is selected. Added the Side-Codex hold; no Weapon value or title changed. **Cumulative source-led progress: 20 / 287 (7.0%); 267 / 287 eligible dossiers remain without an individual disposition.**

**Unit 2 / 3 — Frozen Window `C-IIβ-330` (held):** the primary and `SE-330-B` repeat the same 210 cm four-pane mullion-pike Appearance verbatim, so it cannot independently settle the profile. The primary gives Weight 7–12 / Normal 3 / Range 3 (2.2 m reach plus 4 m frost-shatter); the linked item gives Weight 5–9 / Measured 2 / Range 2 / Single; the master row confirms Weight 5–9 / Measured 2 / Range 2, and the Side card repeats Weight 5–9 / Speed 2 / Range 2 / Single. The primary's *Glazing Shatter-Lance* and polearm/range classification do not map to the item's *Circuit Breaker* and melee classification; the Side card calls the pike profile “Maul,” and the `MAW-W-330` archetype row instead says “Lamentation Dirk.” No form or base/special split resolves these records. Added the Side-Codex hold; no Weapon value or title changed. **Cumulative source-led progress: 21 / 287 (7.3%); 266 / 287 eligible dossiers remain without an individual disposition.**

**Unit 3 / 3 — Clapperless `C-IIβ-340` (held):** the primary's *Cryo-Relic Lance* is an eight-foot ivory / glacier-ice spear with Void 6–10 / Fast 4 / Range 3 and an Ultrasonic Psychic Pulse / 4 m cone; the entity and Side subject are silent pale bells, while the linked *Clapperless Chime-Sceptre* is physically described as a pale Han-glass hammer. Side and item state Void 5–9 / Speed 2 / Range 2 / Single; maximum 4 and 25 Echoes agree. The master leaves damage, speed, and range variable / unset. The `MAW-W-340` index supports the Cryo-Relic Lance, while separate `MAW-W-285` names a Silent Memorial-Bell / Clapperless Monastery Bell (Room), with no crosswalk to `MAW-W-340-01`. No transformation or profile split reconciles lance, bell, and hammer. Added the Side-Codex hold; no Weapon value or form changed. **Cumulative source-led progress: 22 / 287 (7.7%); 265 / 287 eligible dossiers remain without an individual disposition.**

**Cumulative source-led coverage after Batch 82: 22 / 287 (7.7%), with 265 / 287 eligible dossiers still lacking an individual disposition. Batch 82 closed at three (2026-10-10).** The automated screen remains **287 / 287**; the full primary-SE corpus is **301**, with **14** outside this paired scope. All three new unique dispositions are holds; no disputed primary/item Weapon values, forms, or titles changed. Each Side Codex records the evidence and the unresolved relationship. Each of the three dossier holds was gated and push-verified individually; Frozen Window also received a separately gated / pushed follow-up correction to clarify the master-row attribution.

| Primary SE dossier | Disposition | Cumulative source-led progress | Commit | Push |
|---|---|---|---|---|
| 1 / 3 — [[SE-C-IIIγ-180_Owed_빚의_벽](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-180_Owed_%EB%B9%9A%EC%9D%98_%EB%B2%BD.md "SE-C-IIIγ-180_Owed_빚의_벽.md")] `C-IIIγ-180` | Ram/bastion vs unlabeled maul/Skewer profile held | `20 / 287` · `267` remain | `b90df653` | PUSH VERIFIED |
| 2 / 3 — [[SE-C-IIβ-330_Frozen_Window_얼어붙은_창](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-330_Frozen_Window_%EC%96%BC%EC%96%B4%EB%B6%99%EC%9D%80_%EC%B0%BD.md "SE-C-IIβ-330_Frozen_Window_얼어붙은_창.md")] `C-IIβ-330` | Pike profile conflict and index/name mismatch held | `21 / 287` · `266` remain | `cb9f7f5c` → `2d2da41a` | PUSH VERIFIED |
| 3 / 3 — [[SE-C-IIβ-340_Clapperless_빈_종](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-340_Clapperless_%EB%B9%88_%EC%A2%85.md "SE-C-IIβ-340_Clapperless_빈_종.md")] `C-IIβ-340` | Lance / bell / hammer identity and profile held | `22 / 287` · `265` remain | `fca6fb61` | PUSH VERIFIED |

**Cumulative progress after Batch 82 (not a batch-local fraction):**

| Measure | Completed | Total | Remaining | Coverage |
|---|---:|---:|---:|---:|
| Automated screen of complete Weapon pairs | `287` | `287` | `0` | **100%** |
| Unique source-led Weapon dispositions | `22` | `287` | `265` | **7.7%** |
| Same source-led dispositions, measured against all primary SE dossiers | `22` | `301` | `279` | **7.3%** |

The full corpus has **301** primary SE dossiers; **14** are outside the complete-pair Weapon scope (9 without an external Side Codex and 5 exception sets). The **265 / 287** are eligible dossiers without a documented individual source-led disposition—not known defects or required edits. Holds count as dispositions; repeated reviews do not increase the unique count. The 22 counted designations are `C-IIIγ-032`, `C-IIβ-055`, `C-IIIγ-145`, `UNK-251`, `C-IIIγ-921`, `C-IIIγ-044`, `C-IIβ-280`, `C-IIβ-101`, `C-IIβ-135`, `C-IIβ-170`, `C-IIIγ-190`, `C-IVγ-205`, `C-IIIγ-088`, `N-IVβ-019`, `C-IIIβ-036`, `C-IIβ-099`, `C-IIβ-102`, `C-IVδ-106`, `C-IIIγ-140`, `C-IIIγ-180`, `C-IIβ-330`, and `C-IIβ-340`.

**Batch 83 — opened at three (2026-10-10).** Entering cumulative source-led coverage was **22 / 287 (7.7%)**, with **265 / 287** eligible complete-pair dossiers lacking an individual disposition. The automatic screen remains **287 / 287**; the full primary-SE corpus is **301**, with **14** outside scope. After review-history checks, the next three open conflict candidates were Memorial Flame Mid-Ceremony `C-IVδ-763`, Grieving Love `N-IIIβ-941`, and Calling Bloom `O-IIIβ-944`. Memorial Flame's earlier work included Consequences and shroud edits plus Suit/Stigma category repairs that referenced the Weapon Category, not an individual Weapon-profile disposition; Grieving Love's earlier edits concerned dossier text and Breach Behavior; Calling Bloom's concerned the Suit ability and shared text/couple work. None had a prior individual Weapon disposition. These Side-card layouts were not surfaced by the automatic Side-card parser, so the Side rows and linked item descriptions were reviewed directly. Missing-only findings remain separate: an omitted field is not a defect by itself.

**Unit 1 / 3 — Memorial Flame Mid-Ceremony `C-IVδ-763` (held):** the primary and `SE-763-B` repeat the same two-paragraph Appearance of an antique brass candelabrum bodkin with an eight-inch spike, purple wax, and violet smoke; it is duplicated evidence, not independent corroboration. The primary gives Lament 14–22 / Normal 3 / Range 4 (Long) / Homing Wisp–Tracking Soul-Burn; the Side and linked item give Lament 10–15 / Fast 3 / Range 3 (Medium) / Skewer. Maximum 2 and 50 Echoes agree. The master registry leaves numeric stats unset; `MAW-W-763` supports the antique-brass Short-blade bodkin form and a Short band, not either listed reach. The Side's *Soul-Seeking Candelabrum* label also appears in the item quote and role text, while the item title/master use *The Candelabrum Bodkin*; this is a documented naming variation, not a second form. No source maps the profiles to separate modes or forms. Added a Side-Codex hold; no Weapon values or title changed. **Cumulative source-led progress: 23 / 287 (8.0%); 264 / 287 eligible dossiers remain without an individual disposition.**

**Unit 2 / 3 — Grieving Love `N-IIIβ-941` (held):** the primary and `SE-941-B` name *The Comforting Coil*. The primary's Appearance describes a coiled Lament Han-crystal whip; the item describes a grief-slime tendril extending and coiling around its target. The primary gives Range 2 (Medium), while the Side and item core row give Range 3 (Medium); Lament 5–10, Speed 2 (Normal), maximum 3, and 24 Echoes agree. The item prose says “medium range” but gives no physical reach measurement. The master leaves damage/speed/range variable; archetype `MAW-W-941` lists a Close / Spiked Knuckle Brand with no crosswalk to `MAW-W-941-01` or the coil Appearance. Nothing resolves Range 2 versus 3 or documents another form/mode. Added a Side-Codex hold; no values changed. **Cumulative source-led progress: 24 / 287 (8.4%); 263 / 287 eligible dossiers remain without an individual disposition.**

**Unit 3 / 3 — Calling Bloom `O-IIIβ-944` (held):** primary and item descriptions identify *The Murmur Vine* as a living whip-vine / grief-vine that coils and extends toward a target, but give no measured reach. The primary gives Range 3 (Long); the Side and linked item's core row give Range 4 (Long). Lament 5–9, Speed 2 (Normal), maximum 3, and 24 Echoes agree. The Side/item also specify an AoE profile and the item gives center/inner/outer falloff; the primary omits pattern, coverage, and falloff, which are not treated as defects. The master leaves numeric stats variable / unset. Archetype `MAW-W-944` lists PRIMAL / CLOSE (Snapping Bone Mandibles) / Close, without a crosswalk to `MAW-W-944-01` or this vine form. No reach measurement or base/special/form mapping selects Range 3 versus 4. Added a Side-Codex hold; no values changed. **Cumulative source-led progress: 25 / 287 (8.7%); 262 / 287 eligible dossiers remain without an individual disposition.**

**Cumulative source-led coverage after Batch 83: 25 / 287 (8.7%), with 262 / 287 eligible dossiers still lacking an individual disposition. Batch 83 closed at three (2026-10-10).** The automated screen remains **287 / 287**; the full primary-SE corpus is **301**, with **14** outside this paired scope. All three new unique dispositions are holds; no disputed primary/item Weapon values, forms, or titles changed. Each Side Codex records the evidence and unresolved relationship. All three dossier commits passed the per-dossier gate and were push-verified on the assigned branch.

| Primary SE dossier | Disposition | Cumulative source-led progress | Commit | Push |
|---|---|---|---|---|
| 1 / 3 — [[SE-C-IVδ-763_Memorial_Flame_Mid-Ceremony_사라진_불꽃](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-763_Memorial_Flame_Mid-Ceremony_%EC%82%AC%EB%9D%BC%EC%A7%84_%EB%B6%88%EA%BD%83.md "SE-C-IVδ-763_Memorial_Flame_Mid-Ceremony_사라진_불꽃.md")] `C-IVδ-763` | Bodkin/long tracking profile vs Side/item medium Skewer profile held | `23 / 287` · `264` remain | `5f4aeb91` | PUSH VERIFIED |
| 2 / 3 — [[SE-N-IIIβ-941_Grieving_Love_슬픈_사랑](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-III%CE%B2-941_Grieving_Love_%EC%8A%AC%ED%94%88_%EC%82%AC%EB%9E%91.md "SE-N-IIIβ-941_Grieving_Love_슬픈_사랑.md")] `N-IIIβ-941` | Range 2 vs 3 (both Medium) held | `24 / 287` · `263` remain | `ff236165` | PUSH VERIFIED |
| 3 / 3 — [[SE-O-IIIβ-944_Calling_Bloom_부르는_꽃](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-III%CE%B2-944_Calling_Bloom_%EB%B6%80%EB%A5%B4%EB%8A%94_%EA%BD%83.md "SE-O-IIIβ-944_Calling_Bloom_부르는_꽃.md")] `O-IIIβ-944` | Range 3 vs 4 (both Long) held | `25 / 287` · `262` remain | `c893035d` | PUSH VERIFIED |

**Cumulative progress after Batch 83 (not a batch-local fraction):**

| Measure | Completed | Total | Remaining | Coverage |
|---|---:|---:|---:|---:|
| Automated screen of complete Weapon pairs | `287` | `287` | `0` | **100%** |
| Unique source-led Weapon dispositions | `25` | `287` | `262` | **8.7%** |
| Same source-led dispositions, measured against all primary SE dossiers | `25` | `301` | `276` | **8.3%** |

The full corpus has **301** primary SE dossiers; **14** are outside the complete-pair Weapon scope (9 without an external Side Codex and 5 exception sets). The **262 / 287** are eligible dossiers without a documented individual source-led disposition—not known defects or required edits. Holds count as dispositions; repeated reviews do not increase the unique count. The 25 counted designations are `C-IIIγ-032`, `C-IIβ-055`, `C-IIIγ-145`, `UNK-251`, `C-IIIγ-921`, `C-IIIγ-044`, `C-IIβ-280`, `C-IIβ-101`, `C-IIβ-135`, `C-IIβ-170`, `C-IIIγ-190`, `C-IVγ-205`, `C-IIIγ-088`, `N-IVβ-019`, `C-IIIβ-036`, `C-IIβ-099`, `C-IIβ-102`, `C-IVδ-106`, `C-IIIγ-140`, `C-IIIγ-180`, `C-IIβ-330`, `C-IIβ-340`, `C-IVδ-763`, `N-IIIβ-941`, and `O-IIIβ-944`.

**Batch 84 — opened at 3 / 3 (2026-10-10).** Entering cumulative source-led coverage was **25 / 287 (8.7%)**, with **262 / 287** eligible complete-pair dossiers lacking an individual disposition. The automatic screen remained **287 / 287**; the full primary-SE corpus is **301**, with **14 / 301** outside scope. The conflict screen had **23 / 23** unique primary-versus-item candidates, with **4 / 23** still lacking individual dispositions; the next three in comparator order were Blackened Angel `C-IVγ-946`, Soot Fry `C-IIβ-947`, and Foam Flood `C-IIIγ-948`. History checks found no prior individual Weapon disposition for these cases. Blackened Angel's earlier work included the Batch 19 M.A.W. Appearance expansion and a Batch 74 Log and Method rewrite, not an individual range review. Soot Fry and Foam Flood had prior Appearance expansion, Interaction Pattern / R-29 cleanup, and other text work, but no individual Weapon-range disposition. The primary, Side set rows, linked item records, master-registry rows, archetypes, and the cross-flagged Stormscale context were reviewed directly. Missing-only findings remain separate: an omitted field is not a defect by itself.

**Unit 1 / 3 — Blackened Angel `C-IVγ-946` (held):** the primary gives *The Tarnish Plume* Range 2 (Medium); the linked item and Side set row give Range 3 (Medium). Weight 7–12, Speed 2 (Normal), maximum 3, and 30 Echoes agree. The Side row summarizes the linked item, rather than supplying an independent reach measurement. The primary's plume-tipped haft and the item's “medium range” prose give no measured reach. The master registry marks damage variable and speed/range unset, with maximum/cost `N/A`; archetype `MAW-W-946` indexes a MELEE / CLOSE Heavy Lead Cestus (Close), without an explicit crosswalk to `MAW-W-946-01` or the Plume. The primary omits pattern/falloff fields, which are not treated as defects. No source resolves Range 2 versus 3 or establishes separate forms. Added a Side-Codex range hold; no Weapon values changed. **Cumulative progress: 26 / 287 (9.1%); 261 / 287 eligible dossiers remain without an individual disposition.**

**Unit 2 / 3 — Soot Fry `C-IIβ-947` (held):** the primary gives *The Still Current* Range 3 (Long); the linked item's core row and Side set summary give Range 4 (Long). Weight 6–11, Speed 2 (Normal), maximum 3, and 24 Echoes agree. The Side row summarizes the linked item, not a separate reach measurement. “Long range” prose and a sinking-thrust ability do not measure the spear's reach; the primary's 20 cm resting silhouette / 2.2 m extended-fish dimensions describe the entity, not the weapon. The master registry marks damage variable and speed/range unset, with maximum/cost `N/A`; archetype `MAW-W-947` lists PRIMAL / CLOSE (Coiling Muscular Tendril), Short, without an explicit crosswalk to `MAW-W-947-01` or the spear. The Side/item AoE and falloff fields are omitted by the primary; this is not a defect finding. The cross-flagged Stormscale Sovereign is a distinct, forbidden composite with its own `MAW-W-949-01` weapon; no source maps its reach to either constituent weapon. Added a Side-Codex range hold; no Weapon values changed. **Cumulative progress: 27 / 287 (9.4%); 260 / 287 eligible dossiers remain without an individual disposition.**

**Unit 3 / 3 — Foam Flood `C-IIIγ-948` (held):** the primary gives *The Skyward Spear* Range 3 (Long); the linked item's core row and Side set summary give Range 4 (Long). Lament 7–12, Speed 3 (Fast), maximum 3, and 30 Echoes agree. The Side row summarizes the linked item rather than providing independent reach evidence. Both records depict a pale-stone spear carved as a rising dragon, but neither gives shaft length or measured reach; the entity carving's one-metre height is not the spear's effective reach. The item's “long range” and AoE description supply no numeric basis. The master registry marks damage variable and speed/range unset, with maximum/cost `N/A`; archetype `MAW-W-948` lists MELEE / CLOSE (Wrought-Iron Fist-Brand), Close, without an explicit crosswalk to `MAW-W-948-01` or the spear. Pattern/falloff omissions in the primary are not defects. The forbidden Stormscale transformation has a distinct M.A.W. item and no range-inheritance mapping. Added a Side-Codex range hold; no Weapon values changed. **Cumulative progress: 28 / 287 (9.8%); 259 / 287 eligible dossiers remain without an individual disposition.**

**Cumulative source-led coverage after Batch 84: 28 / 287 (9.8%), with 259 / 287 eligible dossiers still lacking an individual disposition. Batch 84 closed at 3 / 3 (2026-10-10).** The automated screen remains **287 / 287**; the full primary-SE corpus is **301**, with **14 / 301** outside the paired scope. All **3 / 3** new unique dispositions are holds; no disputed primary/item Weapon values or titles changed. Each Side Codex records the evidence and unresolved relationship. All three dossier commits passed their individual gates and were push-verified on the assigned branch.

| Primary SE dossier | Disposition | Cumulative source-led progress | Commit | Push |
|---|---|---|---|---|
| 1 / 3 — [[SE-C-IVγ-946_Blackened_Angel_검어진_천사](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B3-946_Blackened_Angel_%EA%B2%80%EC%96%B4%EC%A7%84_%EC%B2%9C%EC%82%AC.md "SE-C-IVγ-946_Blackened_Angel_검어진_천사.md")] `C-IVγ-946` | Range 2 vs 3 (both Medium) held | `26 / 287` · `261` remain | `6b09d5c4` | PUSH VERIFIED |
| 2 / 3 — [[SE-C-IIβ-947_Soot_Fry](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-947_Soot_Fry.md "SE-C-IIβ-947_Soot_Fry.md")] `C-IIβ-947` | Range 3 vs 4 (both Long) held | `27 / 287` · `260` remain | `25a1f598` | PUSH VERIFIED |
| 3 / 3 — [[SE-C-IIIγ-948_Foam_Flood](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-948_Foam_Flood.md "SE-C-IIIγ-948_Foam_Flood.md")] `C-IIIγ-948` | Range 3 vs 4 (both Long) held | `28 / 287` · `259` remain | `5dbbd683` | PUSH VERIFIED |

**Cumulative progress after Batch 84 (not a batch-local fraction):**

| Measure | Completed | Total | Remaining | Coverage |
|---|---:|---:|---:|---:|
| Automated screen of complete Weapon pairs | `287` | `287` | `0` | **100%** |
| Unique source-led Weapon dispositions | `28` | `287` | `259` | **9.8%** |
| Same source-led dispositions, measured against all primary SE dossiers | `28` | `301` | `273` | **9.3%** |

The full corpus has **301** primary SE dossiers; **14 / 301** are outside the complete-pair Weapon scope (9 without an external Side Codex and 5 exception sets). The **259 / 287** are eligible dossiers without a documented individual source-led disposition—not known defects or required edits. Holds count as dispositions; repeated reviews do not increase the unique count. The 28 counted designations are `C-IIIγ-032`, `C-IIβ-055`, `C-IIIγ-145`, `UNK-251`, `C-IIIγ-921`, `C-IIIγ-044`, `C-IIβ-280`, `C-IIβ-101`, `C-IIβ-135`, `C-IIβ-170`, `C-IIIγ-190`, `C-IVγ-205`, `C-IIIγ-088`, `N-IVβ-019`, `C-IIIβ-036`, `C-IIβ-099`, `C-IIβ-102`, `C-IVδ-106`, `C-IIIγ-140`, `C-IIIγ-180`, `C-IIβ-330`, `C-IIβ-340`, `C-IVδ-763`, `N-IIIβ-941`, `O-IIIβ-944`, `C-IVγ-946`, `C-IIβ-947`, and `C-IIIγ-948`.

The conflict-status screen still finds **23 / 23 unique primary-versus-item candidate dossiers**, including cases with documented holds; it is a candidate finder, not the individual-disposition ledger. After excluding individually dispositioned cases, **1 / 23** conflict candidate remains open: Stormscale Sovereign `C-Vδ-949`. Missing-only candidates remain separate: an omitted field is not a defect by itself.

**Batch 86 — opened and closed at three (2026-10-10).** Entering source-led coverage was **31 / 287 (10.8%)**, with **256 / 287** eligible complete pairs lacking an individual disposition; against all primary dossiers it was **31 / 301 (10.3%)**, with **270 / 301** without a disposition. The automated screen remains **287 / 287**, with **14 / 301** outside paired scope. The primary-versus-item conflict screen had one undispositioned case, Stormscale Sovereign `C-Vδ-949`, below the R-26 floor. The recognized Side Weapon conflict slices had three open cases. History checks found no prior individual source-led Side Weapon disposition for these profiles: the Side cards still carried their pre-overhaul profiles after the linked-item revisions, while earlier prose/couple cleanup did not reconcile the card conflicts. Missing-only findings were not treated as defects.

**Unit 1 / 3 — Debt Scale `C-IIIβ-015` (Side profile corrected):** the Side card still named *The Balance Lens* and gave Void 5–9 / Normal 2 / Short 2 / Single. Revision `b2c35a2f` changed the linked item to *The Balance Projector*, a counterbalanced crossbow; the current primary, item core, and master-registry row agree on Void 8–14 / Slow 2 / Long 4 / Precision Shot–Equalizing Bolt, and archetype `MAW-W-015` supports the crossbow / Long form. The Side set row and card now use the current name/profile and explicitly state one designated target. The old `SE-015-B` filename remains only as the linked path. **Cumulative source-led progress: 32 / 287 (11.1%); 255 / 287 eligible dossiers remain.**

**Unit 2 / 3 — Hollow Saint `C-IIIγ-081` (Side profile corrected; residual terminology held):** the Side card still named *The Hollow Lens* and gave Void 7–12 / Fast 3 / Medium 3 / Skewer. Revision `b2c35a2f` changed the linked item's identity, appearance, and combat profile to *The Hollow Sceptre*. The current primary and linked item identity/Appearance/Core Statistics support Void 8–14 / Normal 3 / Long 4; the master registry supports the Sceptre name, and `MAW-W-081` supports a Long Choral Staff (the registry's numeric combat fields remain variable/unset). The Side row/card now use *The Hollow Sceptre*, Line Skewer / Ultrasonic Beam, up to three aligned targets, retaining the matching 100% → 70% → 50% falloff and 3 / 40 cost. The linked item's extraction result, rejection rule, Basic Attack, Signature Ability, maintenance and set prose still say “Lens”; the Side page records this unresolved terminology hold, with no separate Lens form inferred. The old `SE-081-B` filename remains only as a path; the item record itself was not edited. **Cumulative source-led progress: 33 / 287 (11.5%); 254 / 287 eligible dossiers remain.**

**Unit 3 / 3 — Pyre of Truths `C-IVδ-092` (Side profile corrected; residual terminology held):** the Side card still named *The Burning Fang* and gave Grudge 10–15 / Fast 3 / Medium 3 / Skewer. Revision `ebcbd249` changed the linked item's name, forms, appearance, and core combat profile to *The Pyre Grimoire & Ash Lance*. The current primary and linked item core statistics agree on Grudge 14–22 / Normal 3 / Long 4 / Channeled Ash Burst–Consuming Conflagration; the master-registry name and `MAW-W-092` grimoire / flame-lance archetype support the identity and Long form (the registry's numeric combat fields remain variable/unset). The Side row/card now match, state up to three targets, and retain the matching falloff and 2 / 50 cost; its bearer cost and quick effect now reflect the current source text and grimoire-lance Appearance. The linked item's Basic Attack and Signature Ability still use “Fang” / “Skewer line”; this residual terminology is recorded as a hold, not a separate mode. `SE-092-B` was not edited and its old filename remains only as a path. **Cumulative source-led progress: 34 / 287 (11.8%); 253 / 287 eligible dossiers remain.**

**Cumulative source-led coverage after Batch 86: 34 / 287 (11.8%), with 253 / 287 eligible dossiers still lacking an individual disposition.** Against all 301 primary dossiers, **34 / 301 (11.3%)** have a disposition and **267 / 301** remain without one. The automated screen is **287 / 287**; **14 / 301** are outside the complete-pair scope. All three Side-card profiles were corrected from corroborated later item revisions; two residual linked-item terminology discrepancies remain explicitly held. Each dossier passed its individual gate and push verification on the assigned branch. The primary records and all linked-item Weapon records remained unchanged.

| Primary SE dossier | Disposition | Cumulative source-led progress | Commit | Push |
|---|---|---|---|---|
| 1 / 3 — [[SE-C-IIIβ-015_The_Debt_Scale_빚의_저울](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B2-015_The_Debt_Scale_%EB%B9%9A%EC%9D%98_%EC%A0%80%EC%9A%B8.md "SE-C-IIIβ-015_The_Debt_Scale_빚의_저울.md")] `C-IIIβ-015` | Side title/profile aligned to later revision | `32 / 287` (11.1%); `255` remain | `77b132de` | PUSH VERIFIED |
| 2 / 3 — [[SE-C-IIIγ-081_The_Hollow_Saint_빈_성자](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-081_The_Hollow_Saint_%EB%B9%88_%EC%84%B1%EC%9E%90.md "SE-C-IIIγ-081_The_Hollow_Saint_빈_성자.md")] `C-IIIγ-081` | Side title/profile aligned; linked-item Lens terminology held | `33 / 287` (11.5%); `254` remain | `48e6de5e` | PUSH VERIFIED |
| 3 / 3 — [[SE-C-IVδ-092_Pyre_of_Truths_타오르는_도서관](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-092_Pyre_of_Truths_%ED%83%80%EC%98%A4%EB%A5%B4%EB%8A%94_%EB%8F%84%EC%84%9C%EA%B4%80.md "SE-C-IVδ-092_Pyre_of_Truths_타오르는_도서관.md")] `C-IVδ-092` | Side title/profile aligned; linked-item Fang/Skewer terminology held | `34 / 287` (11.8%); `253` remain | `f0c0f9a6` | PUSH VERIFIED |

**Cumulative progress after Batch 86 (not a batch-local fraction):**

| Measure | Completed | Total | Remaining | Coverage |
|---|---:|---:|---:|---:|
| Automated screen of complete Weapon pairs | `287` | `287` | `0` | **100%** |
| Unique source-led Weapon dispositions | `34` | `287` | `253` | **11.8%** |
| Same source-led dispositions, measured against all primary SE dossiers | `34` | `301` | `267` | **11.3%** |

The full corpus has **301** primary SE dossiers; **14 / 301** are outside the complete-pair Weapon scope (9 without an external Side Codex and 5 exception sets). Holds count as dispositions; the **253 / 287** without an individual source-led disposition are not known defects or required edits. The 34 counted designations are `C-IIIγ-032`, `C-IIβ-055`, `C-IIIγ-145`, `UNK-251`, `C-IIIγ-921`, `C-IIIγ-044`, `C-IIβ-280`, `C-IIβ-101`, `C-IIβ-135`, `C-IIβ-170`, `C-IIIγ-190`, `C-IVγ-205`, `C-IIIγ-088`, `N-IVβ-019`, `C-IIIβ-036`, `C-IIβ-099`, `C-IIβ-102`, `C-IVδ-106`, `C-IIIγ-140`, `C-IIIγ-180`, `C-IIβ-330`, `C-IIβ-340`, `C-IVδ-763`, `N-IIIβ-941`, `O-IIIβ-944`, `C-IVγ-946`, `C-IIβ-947`, `C-IIIγ-948`, `C-IVδ-001`, `C-Vδ-002`, `N-IVδ-005`, `C-IIIβ-015`, `C-IIIγ-081`, and `C-IVδ-092`.

**Live conflict queues after Batch 86:** `--check weapon` still reports **23 / 23** primary-versus-item conflict candidates, with only Stormscale Sovereign `C-Vδ-949` lacking an individual disposition. The structured Side Weapon slice has 9 primary-versus-Side stat-conflict cards, all 9 individually dispositioned; Side-versus-item has 3 conflict cards, all 3 individually dispositioned. There are no unreviewed stat-conflict cards left in these recognized Side Weapon slices. Missing-only findings remain separate and are not defects by themselves; the separate parser-layout audit remains open.

**Batch 87 — opened and closed at three (2026-10-10).** Entering cumulative source-led coverage was **34 / 287 (11.8%)**, with **253 / 287** eligible complete pairs lacking an individual disposition; against all 301 primary dossiers, **34 / 301 (11.3%)** had one and **267 / 301** did not. The automated screen remains **287 / 287**, with **14 / 301** outside paired scope. The sole undispositioned primary-versus-item Weapon conflict is Stormscale Sovereign `C-Vδ-949`, below the R-26 floor by itself. The new identity-table layout surfaced five Side Weapon name candidates; history checks selected Memory Weaver `C-IVγ-009`, Debt Eater `C-IIIβ-014`, and Silent Child `N-Iα-025`, each with an item-title/form revision not yet reconciled on its Side page. These were not padded candidates. The batch stayed at the R-26 floor of three; all three cases passed their individual gates and push checks.

**Unit 1 / 3 — The Memory Weaver `C-IVγ-009` (Side title and purpose aligned; linked-item terminology held):** updated the identity-only Side set row from *The Forgotten Lens* to *The Weaver's Shuttle-Awl*. Revision `ebcbd249` retitled the same `MAW-W-009-01`, replacing the lens-edged disc with the cold-iron weaving shuttle, diamond awl, and memory spindle. The current primary block, item heading/Item Identity/Appearance, registry row, and `MAW-W-009` archetype support the Shuttle-Awl. The Side purpose now describes `Unweave` and its documented risk of severing a true memory. The linked item still says “Lens” in Ability and Limit; that residual term is held, with no second form inferred. The Side table has no numeric weapon fields, so none were added. **Cumulative source-led progress: 35 / 287 (12.2%); 252 remain.**

**Unit 2 / 3 — The Debt Eater `C-IIIβ-014` (Side title and purpose aligned; linked-item terminology held):** updated the Side row from *The Debt Lens* to *The Debt Prism*. Revision `b2c35a2f` changed the same item from a handheld lens to a floating Void-glass dodecahedron and revised its combat profile. The primary, current item identity/appearance/combat record, master-registry row, master Codex entry, and `MAW-W-014` archetype support the Prism; the Side purpose now reflects line-of-sight reading without claiming it judges the debt. “Lens” remains in the linked item's History of Use and Set Resonance and is held as residual wording, not a second form. No numeric profile was added to the identity-only Side table. **Cumulative source-led progress: 36 / 287 (12.5%); 251 remain.**

**Unit 3 / 3 — The Silent Child `N-Iα-025` (Side title and purpose aligned; naming hold retained):** changed the Side row from *The Silence Lens* to *The Hush Stiletto* and summarized the one-turn Quiet Interval. Revision `3abe5470` replaced the item's disc-like Silence Lens identity/Appearance with a nine-inch rubber-wrapped stiletto; the current primary, item appearance, registry row, and `MAW-W-025` short-blade archetype support the new title. The linked item's Ability/Limit still use “Lens,” and master M.A.W. Codex Entry 565 still says “The Silence Lens” although the master table, registry, primary, and archetype say *The Hush Stiletto*. Both remain explicit terminology holds; no alternate Lens form was inferred. No weapon numbers were added to the identity-only Side table. **Cumulative source-led progress: 37 / 287 (12.9%); 250 remain.**

| Side Codex dossier | Disposition | Cumulative source-led progress | Commit | Push |
|---|---|---|---|---|
| 1 / 3 — [SE-009-A · The Memory Weaver Side Codex](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/MAW_Codex_Sets/Registry_009_to_015/009_Memory_Weaver/SE-009-A__SIDE_CODEX_The_Memory_Weaver.md) (`C-IVγ-009`; [primary SE](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B3-009_The_Memory_Weaver_%EA%B8%B0%EC%96%B5%EC%9D%98_%EC%A7%81%EA%B3%B5.md)) | Side title/purpose aligned; linked-item “Lens” wording held | `35 / 287` (12.2%); `252` remain | `423c5eb1` | PUSH VERIFIED |
| 2 / 3 — [SE-014-A · The Debt Eater Side Codex](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/MAW_Codex_Sets/Registry_009_to_015/014_Debt_Eater/SE-014-A__SIDE_CODEX_The_Debt_Eater.md) (`C-IIIβ-014`; [primary SE](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B2-014_The_Debt_Eater_%EB%B9%9A%EC%9D%84_%EB%A8%B9%EB%8A%94_%EC%9E%90.md)) | Side title/purpose aligned; linked-item “Lens” wording held | `36 / 287` (12.5%); `251` remain | `c9dbcdcc` | PUSH VERIFIED |
| 3 / 3 — [SE-025-A · The Silent Child Side Codex](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/MAW_Codex_Sets/Registry_016_to_031/025_Silent_Child/SE-025-A__SIDE_CODEX_The_Silent_Child.md) (`N-Iα-025`; [primary SE](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-I%CE%B1-025_The_Silent_Child_%EC%A1%B0%EC%9A%A9%ED%95%9C_%EC%95%84%EC%9D%B4.md)) | Side title/purpose aligned; item and master-detail “Lens” wording held | `37 / 287` (12.9%); `250` remain | `8ba99cfe` | PUSH VERIFIED |

**Cumulative progress after Batch 87 (not a batch-local fraction):**

| Measure | Completed | Total | Remaining | Coverage |
|---|---:|---:|---:|---:|
| Automated screen of complete Weapon pairs | `287` | `287` | `0` | **100%** |
| Unique source-led Weapon dispositions | `37` | `287` | `250` | **12.9%** |
| Same dispositions, measured against all primary SE dossiers | `37` | `301` | `264` | **12.3%** |

Holds count as dispositions; the **250 / 287** dossiers without an individual disposition are not known defects or required edits. The three new designations are `C-IVγ-009`, `C-IIIβ-014`, and `N-Iα-025`; cumulative dispositions now total 37. No primary or linked-item Weapon records changed, and no unsupported numeric fields were added. The *Hollow Tree* primary / *Timber Maw* Side-Codex naming distinction for `C-IVγ-205` remains untouched. The recognized Side Weapon stat-conflict slices remain **9 / 9** primary-versus-Side and **3 / 3** Side-versus-item dispositioned; the primary/item screen remains **23 / 23** with Stormscale Sovereign `C-Vδ-949` the sole undispositioned case. Of the five newly surfaced identity-table Weapon name candidates, the two still open are `C-Iα-011` and `C-IIIγ-062`; these are candidates, not confirmed defects.

**Batch 85 — opened and closed at three (2026-10-10).** Entering coverage was **28 / 287 (9.8%)**, with **259 / 287** eligible complete pairs still lacking an individual disposition. The primary-versus-item queue alone had one undispositioned case—Stormscale Sovereign `C-Vδ-949`, below the R-26 floor. The recognized Side-card Weapon queues had six unreviewed cases; in comparator order, the first three were Orphaned Bell `C-IVδ-001`, Grieving Colossus `C-Vδ-002`, and Smothering Mother `N-IVδ-005`. All three were also present in the Side-versus-item screen. History checks found no earlier source-led Side/item profile disposition: the Orphaned Bell’s prior work covered prose, Suit/O-Relic material, and duplicated Relic structure; the Grieving Colossus’s 2026-10-05 R-29 weapon-ability/appearance rewrite did not reconcile the Side-card stat conflict; the Mother’s prior edits were prose and overlap cleanup. Missing-only fields were not treated as defects.

**Unit 1 / 3 — Orphaned Bell `C-IVδ-001` (Side profile corrected; linked category held):** the Side card still used the earlier *Lament’s Requiem* 10–15 / Fast 3 / Skewer entry. Item history `b2c35a2f` established Lament 12–18 / Slow 2 and Wide Arc / Line Resonance; `3abe5470` retitled and re-described the same `SE-001-B` item as the eight-inch First Dawn Stiletto. The current primary, linked item record, master-registry row, and `MAW-W-001` short-blade archetype support that profile. The Side weapon row/card now use *The First Dawn Stiletto*, matching damage, speed, range 3 (Medium), line coverage up to three linked targets, and 100% → 70% → 50% falloff. The Side’s set-level label **Lament’s Requiem Set** remains visible. The linked Item Identity category still says `MELEE (Resonating Greatsword)` despite the short-stiletto appearance and archetype; that separate category discrepancy is explicitly held, not silently normalized. **Cumulative source-led progress: 29 / 287 (10.1%); 258 / 287 eligible dossiers remain.**

**Unit 2 / 3 — Grieving Colossus `C-Vδ-002` (Side profile corrected):** the Side card retained *Mourning Maul* at Weight 10–15 / Fast 3 / Medium 3 / Skewer and 100% → 70% → 50%. The `ebcbd249` overhaul changed the same item code’s heading, appearance, combat profile, primary block, master entry, and archetype to *The Mourning Monument*: Weight 16–26 / Very Slow 1 / Room 5, Ground Shockwave / Seismic Grief, room-wide radial coverage, and 100% epicenter → 60% perimeter. The Side set row and compact card now follow that revision; the old `Mourning_Maul` filename remains only as the linked path, while the item heading and registries say Monument. No profile split is documented. **Cumulative source-led progress: 30 / 287 (10.5%); 257 / 287 eligible dossiers remain.**

**Unit 3 / 3 — Smothering Mother `N-IVδ-005` (Side profile corrected; linked form vocabulary held):** the Side card retained *Embrace Fang* at Grudge 10–15 / Fast 3 / Medium 3 / Skewer and three-target falloff. Item history `b2c35a2f` changed the profile to Grudge 12–18 / Fast 4 / Close 1 / Snapping Clamp, single-target coverage; `3abe5470` retitled and re-described the item as *The Devotion Executioner-Cleaver*. The current primary, linked combat record, master row, and `MAW-W-005` Close-cleaver archetype corroborate that revision. The Side row/card now use the cleaver title, close-range profile, one-target coverage, and single-target pull rule. A separate linked-item hold remains: its Item Identity still says bone-claw gauntlet / PRIMAL Rending Bone-Claw, while its heading and Appearance say butcher cleaver and the ability retains “Talon”/claw wording. No separate form transition is documented; the item record itself was not changed. **Cumulative source-led progress: 31 / 287 (10.8%); 256 / 287 eligible dossiers remain.**

**Cumulative source-led coverage after Batch 85: 31 / 287 (10.8%), with 256 / 287 eligible dossiers still lacking an individual disposition.** The automated screen remains **287 / 287**; the full corpus is **301** primary dossiers, with **14 / 301** outside the paired scope. All three Side-card Weapon profiles were corrected from the documented later item revisions; the two residual linked-item metadata/form discrepancies remain held. The three dossier gates passed and their commits were push-verified on the assigned branch.

| Primary SE dossier | Disposition | Cumulative source-led progress | Commit | Push |
|---|---|---|---|---|
| 1 / 3 — [[SE-C-IVδ-001_The_Orphaned_Bell_고아의_종](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-001_The_Orphaned_Bell_%EA%B3%A0%EC%95%84%EC%9D%98_%EC%A2%85.md "SE-C-IVδ-001_The_Orphaned_Bell_고아의_종.md")] `C-IVδ-001` | Side title/profile aligned; Item category held | `29 / 287` (10.1%); `258` remain | `239c57ab` | PUSH VERIFIED |
| 2 / 3 — [[SE-C-Vδ-002_The_Grieving_Colossus_슬픔의_거인](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-V%CE%B4-002_The_Grieving_Colossus_%EC%8A%AC%ED%94%94%EC%9D%98_%EA%B1%B0%EC%9D%B8.md "SE-C-Vδ-002_The_Grieving_Colossus_슬픔의_거인.md")] `C-Vδ-002` | Side title/profile aligned to later overhaul | `30 / 287` (10.5%); `257` remain | `5a0117c4` | PUSH VERIFIED |
| 3 / 3 — [[SE-N-IVδ-005_The_Smothering_Mother_질식하는_어머니](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-IV%CE%B4-005_The_Smothering_Mother_%EC%A7%88%EC%8B%9D%ED%95%98%EB%8A%94_%EC%96%B4%EB%A8%B8%EB%8B%88.md "SE-N-IVδ-005_The_Smothering_Mother_질식하는_어머니.md")] `N-IVδ-005` | Side title/profile aligned; linked form vocabulary held | `31 / 287` (10.8%); `256` remain | `08cb402c` | PUSH VERIFIED |

**Cumulative progress after Batch 85 (not a batch-local fraction):**

| Measure | Completed | Total | Remaining | Coverage |
|---|---:|---:|---:|---:|
| Automated screen of complete Weapon pairs | `287` | `287` | `0` | **100%** |
| Unique source-led Weapon dispositions | `31` | `287` | `256` | **10.8%** |
| Same source-led dispositions, measured against all primary SE dossiers | `31` | `301` | `270` | **10.3%** |

The full corpus has **301** primary SE dossiers; **14 / 301** are outside the complete-pair Weapon scope (9 without an external Side Codex and 5 exception sets). The **256 / 287** without a documented individual source-led disposition are not known defects or required edits; holds count as dispositions, and repeated reviews do not increase the unique count. The 31 counted designations are `C-IIIγ-032`, `C-IIβ-055`, `C-IIIγ-145`, `UNK-251`, `C-IIIγ-921`, `C-IIIγ-044`, `C-IIβ-280`, `C-IIβ-101`, `C-IIβ-135`, `C-IIβ-170`, `C-IIIγ-190`, `C-IVγ-205`, `C-IIIγ-088`, `N-IVβ-019`, `C-IIIβ-036`, `C-IIβ-099`, `C-IIβ-102`, `C-IVδ-106`, `C-IIIγ-140`, `C-IIIγ-180`, `C-IIβ-330`, `C-IIβ-340`, `C-IVδ-763`, `N-IIIβ-941`, `O-IIIβ-944`, `C-IVγ-946`, `C-IIβ-947`, `C-IIIγ-948`, `C-IVδ-001`, `C-Vδ-002`, and `N-IVδ-005`.

**Live conflict queues after Batch 85:** `--check weapon` still reports **23 / 23** primary-versus-item conflict candidates, with only Stormscale Sovereign `C-Vδ-949` lacking an individual disposition. The structured Side Weapon slice has 12 primary-versus-Side stat-conflict cards, 9 already dispositioned and 3 still open; Side-versus-item has 6, 3 already dispositioned and the same 3 open. The next three open Side cases are Debt Scale `C-IIIβ-015`, Hollow Saint `C-IIIγ-081`, and Pyre of Truths `C-IVδ-092`. Missing-only findings are separate and are not defects by themselves.

**Unit 2 / 3 — Broken Clock `C-IIIγ-044` (held).** The primary and linked item describe the same 135 cm two-handed brass polearm. The primary gives Weight 11–18, Slow 2, and Overhand Arc / Temporal Impact; the Side and item give Weight 7–12, Fast 3, and Skewer. The item documents no alternate form or base-versus-special stat split, and the master listing has no numeric profile. No value changed.


## Measured state

All figures below are measured, not estimated, and each names the tool that produced it: `boilerplate_report.py` for the body-line measures, `tpl.py` for template residue, `sect.py`/`sectfile.py` for file- and section-cleanliness, `wikistd.py` for `R-29` and its clauses.

**Reporting convention, owner's instruction, 2026-10-05:** every counter is written in fraction form — `x / y` — in this file, in `CHANGELOG.md`, in commit messages and in the PR body. A bare number is not used for a counter anywhere in the record from this turn on.
**Tables in the chatroom, owner's instruction, 2026-10-07 — "Remember The Table In Chatroom":** every report to the owner presents its counters and its results as **tables** — see the standing *Readability tables* ruling of the same date. Each `x / y` counter gets its own row (or its own cell) rather than being buried in a sentence; the per-batch unit table is `# | Dossier | Code | Generic mass (open → final) | Words (before → after)`; SE links and results tables keep to **≤ 5 columns and one row per dossier**, with the per-file plain-language notes as short bullets beneath. Where a table genuinely does not fit (a single boolean, a one-line blocker) prose is allowed — a bare paragraph of counters is not. This applies to the chatroom report, the `WORK_IN_PROGRESS.md` block, the `CHANGELOG.md` mount and the PR body alike.


**Batch ladder, owner's restatement, 2026-10-06 — "Always 3 or 5 then 7 or 10":** the batch size is always one of those four numbers and never any other; a cohort opens at **3 or 5** and the ladder climbs to **7** then **10**. There is no batch of four, six, eight or nine, and a cohort does not open at seven. Batch 22 was a batch of five and closed at five; **batch 23 therefore continues to its declared five**, and the next cohort opens at **seven** unless the owner directs otherwise. The quality clause still outranks size, and anything held is named rather than padded in.

**SE git link convention, owner's instruction, 2026-10-06, under [`R-12`](RULES/R-12_REFER_TO_GITHUB.md):** every finished dossier in a batch is reported with its **SE git link** — `[[SE-…_Name_한글](<github url> "SE-…_Name_한글.md")]`, generated by `python3 tools/ghlink.py <path>` — alongside its closing commit hash and `PUSH VERIFIED`, and this is not optional for units closed earlier in the same batch. The batch's section lists each finished dossier with its link, its commit and its counters, so a reader who arrives at the newest unit can still reach every file the batch produced. Reporting only the unit just closed is the mistake this paragraph exists to prevent.


**Breach recorded 2026-10-09 — the SE git link was dropped from the chatroom reports.** The convention above was not applied to the chatroom reports for batches 61 through 69. Those reports gave each unit its dossier, its code, its commit hash and `PUSH VERIFIED`, but not the `ghlink.py` link — and they reported only the unit just closed rather than every dossier the batch had produced, which is the specific mistake the paragraph exists to prevent. Both halves were being missed at once. Batch 69's links are recorded in its block below and were reposted to the chatroom the same turn. **From this turn every batch report ends with a table of every dossier the batch touched, each with its `ghlink.py` link, its commit, its counters and `PUSH VERIFIED`** — not only the newest unit.

**Batch pacing, owner's correction, 2026-10-05 (`R-26` amended), reaffirmed by the owner the same day — "This Rule Need To Be Remember":** the batch ladder starts at **3**, not 5 — **3 > 5 > 7 > 10** SE files per batch, ratcheting up only while the units are genuinely simple by `R-26`'s own test, and stopping at whatever number was finished properly. **The minimum for any batch is three SE files and that floor is absolute**; the ceiling is ten. Owner, 2026-10-08: *"P + Never Batch Anything Below 3"* — so a batch that cannot reach three finished units **stays open** into the next turn, with the record naming the units that were finished and the ones still owed, and it is never closed short. `R-26`'s quality clause still decides whether the ladder climbs, but since 2026-10-08 it can no longer produce a batch below three; the superseded permission is preserved in the rule file with the correction dated, as the superseded "start at five" wording is preserved below. The superseded "start at five" wording is preserved in the rule file with the correction dated. The units in this cohort are *not* simple by that test — 11–12 dirty sections, full Interaction Records, 5,000–8,000 words — so the ladder stays at the floor of three per batch for this cohort, and the per-dossier conditions and one-`gate.sh`-per-dossier rule are unchanged. Two rows moved this turn without a unit touching them — residue-free 103 → 108 and file-clean 158 → 162 — because the four Rank V rewrites and Ephemera retired shared lines outright, and a line that drops below ten holders stops counting against every remaining dossier. That is the documented spillover effect; it is not work performed this turn.

**Incident #47, same turn, repaired:** the batch-45 open docs commit (`87b313b`) emptied `CHANGELOG.md` — a snippet opened
**Trap, 2026-10-07 (Batch 52 close) — the PR body has a size cap.** Pull request #13's body grew past the platform limit and a `gh api -X PATCH … -F body=@file` for it returned HTTP 200 with the *new* body in the response while the stored body stayed old: the write had been dropped for length, silently. The limit observed is between 261,644 bytes (accepted) and 263,102 bytes (dropped), i.e. the common 262,144-byte issue-body cap. Rule from now on: keep the PR body under **~261,000 bytes** — trim each new batch section to fit, and check the readback after every PATCH (`gh api repos/…/pulls/13 --jq .body | wc -c`, then `grep` for the new section's heading); a 200 is not a write.

the file for writing before reading it, so the read returned nothing and the write wrote nothing. Caught by the next docs step
(`docs.py` anchor miss), restored from `ed80d83` the same turn (no history rewritten, no force-push), the lost open entry re-added,
and the offending pattern replaced with read-then-write everywhere it is used. Nothing else was touched by the bug.

**Abnormality quote research, owner's instruction, 2026-10-07 — *"Research Abnormality Quote For More DEEPER KNOWLEDGE"*:**
~90 quotes from the parent genre (Project Moon) read and sorted into eight registers; written up in
`ABNORMALITY_QUOTE_RESEARCH_2026-10-07.md` with sources. Findings for our method: genre quotes are spoken **by someone**
(ours are nearly all **about** something) and are **traces, not summaries**. Our register baseline, all 301: first person
singular **13 / 301 = 4.3%** · plural **17 / 301 = 5.6%** · second person **30 / 301 = 10.0%** · documentary nouns
**10 / 301 = 3.3%** · questions **0 / 301** · nested dialogue **0 / 301** · imperative openings **4 / 301 = 1.3%**.
`SE_QUOTE_GUIDE.md` now carries the register table and rules **7–10** (rule 4 amended); `quote_audit.py --registers`
measures the distribution for future batches. No dossier content changed. The next batch's six remaining copies may draw
on the register table — the identity test and the identity of each file still rule.
**Rollback #49** hit mid-turn (the gate refused: checkout not level with origin) and was recovered the same
turn — `reset --mixed` to the remote tip; worktree content preserved, no history rewritten, and a stray scratch file
(`quote_style.txt`) removed before the commit.

**Personalization phase, owner's direction, 2026-10-07 — *"Now Readying For Per-10 Batch Update For All SE That Need It
Because A Lot Sound Generic And Not Personalize At ALL"*:** measured with the new read-only auditor
`tools/auditors/personal_audit.py` (masked 6-gram families as in `frame_dup`, mechanics lines exempt and counted
separately): **301 measured · generic mass >= 5% in 101 / 301 → 11 batches of ten** — heavy (>= 10%) **13 / 301** ·
moderate (7–10%) **30 / 301** · light (5–7%) **58 / 301** · fine (< 5%) **200 / 301**. Full worst-first queue, tier
table, batch assignments and the unit method: `PERSONALIZATION_PLAN_2026-10-07.md`. Method per unit: read the file's top
shared frames (`--frames "<name>"`), re-author each **in place** in the file's own terms with its own furniture
(growth-only, `R-15`), checks per unit, one push (`A0`), docs row with the SE link (`R-12`). **Batch 47 — CLOSED at ten
(personalization, per-10, plus a same-batch repair wave)**, worst-first: Mourner's Bloom `C-Iα-330` (16.6%) · Once Upon `O-IIIγ-920` (16.2%) · Never
Discharged `O-IIβ-911` (14.8%) · Echo of Kindness `C-Iα-240` (12.6%) · Once Told `O-IVδ-930` (12.0%) · Vellum Man
`C-Iα-900` (11.7%) · Torn Flower `C-Iα-247` (11.3%) · Passing Bell `N-IIβ-919` (10.6%) · The Kind Healer `C-Iα-071`
(10.4%) · Moktak `N-IIβ-910` (10.2%). **Rollback #50** hit at this turn's open and was recovered the same turn
(`reset --mixed` to the remote tip; no content lost). No dossier content changed this turn.

**Reporting, owner's instruction, 2026-10-07 — *"Thee [Generic mass][Words][Final commit] Is Dont Needed Just Add What The New Quote
Is And What Type Of Quote It Is From Quote Structure Type Research"*:** from this turn on, batch tables drop the `[Generic mass] [Words]
[Final commit]` columns. A quote row instead carries **the new quote itself** and its **register type** taken from the quote-structure research
(`ABNORMALITY_QUOTE_RESEARCH_2026-10-07.md`, registers R1–R8). Counters stay in prose, in `x / y` form, never as table columns; the SE git link
stays in the row (`R-12`). The per-dossier commit hashes continue to be recorded in this file's batch rows and in the PR body notes.

**Quote phase completed, batch 48 (2026-10-07) — the paused remainder, plus the family's three R-29 gaps:** the six copies left over from batches
45–46 were re-authored in place and the family's open gaps closed in the same batch. Movement: distinct quotes **295 → 301 / 301**; duplicate
families **2 → 0 / 301**; dossiers sharing a quote **8 → 0 / 301** — the quote phase is closed with nothing left queued. `R-29` **287 → 290 / 301**:
parity complete **298 → 301 / 301** (no dossier is missing an interactions section), specific condition **293 → 295**, own numeric series **290 → 293**.
Six units, six different registers (R1, R2, R3, R5, R6, R7) — the wing's register profile now carries a first-person line, a question and a
second-person warning it did not have. Nothing deleted (`R-15`); every unit `UNIT CLOSED OK` (meets **True**, residual 0, 0 sections over 0.05).
Disclosures: **rollback #52** recovered at the turn's open (`reset --mixed` to the remote tip, no content lost); u3's series clause and u7's eight
pre-existing residual stock lines were completed in follow-up commits the same turn (`fc944f1`, `c674741`) — both units failed their first check
run after the unit commit and were repaired before this close.

**Quote phase part two, batch 46 result, 2026-10-07 — owner-directed, quotes replaced in place; both links per row:** ten more
family copies got their own quote, each checked against all 301 before writing. Distinct quotes **285 → 295 / 301**; duplicate
families **4 → 2**; dossiers inside a duplicated family **20 → 8 / 301**. `R-29` 286 → **287 / 301** (parity **298**) — Lacrima
also closed its interactions gap. Word growth **+563** (59,150 → 59,713); nothing deleted (`R-15`); every unit meets **True**.
Every b45 and b46 row carries **both links** — the fixed dossier and its source keeper (owner's instruction; b45 rows retrofitted
`10e029a`). Remaining duplicate quotes for the next batch — **6 copies**: F4's Lethe `C-IIIγ-928` · Dead Air `N-IIIγ-929` (source
Beating Relic `C-IIIγ-902`), and F5's Duri's Heart `C-IIβ-901` · Hatred Above `C-IVδ-923` · Weighted Silence `O-IIIγ-924` ·
Dreaming Plague `N-IVδ-927` (source Vellum Man `C-Iα-900`). Disclosures: **rollback #48** recovered at the open; Lacrima's two
pre-existing residual stock lines cleared line-locally (`24efe25`).

**Quote phase, batch 46 open — owner's direction, 2026-10-07:** *"P + When You Write The Quote And Fix It Link Both The Duplicated That Is Fix And The Source."*
Ten more shared quotes come out this round, and every row now carries **both links** — the fixed dossier and the source keeper whose
quote it was copied from. The batch-45 rows were retrofitted with their source links the same way (`10e029a`). Order, worst-first by
family then designation: **F2's last three** — Eleven Fifty-Nine `C-IIIγ-912` · Endless Shift `C-IVδ-915` · Allhallow `O-IIIγ-916`
(source: Breathing Stone `C-IVδ-907`); **F3's five** — Never Discharged `O-IIβ-911` · Ninety Seconds `C-IVδ-918` · Miasma `C-IVδ-922`
· Sky of Borrowed Faces `O-IIIγ-926` · Once Told `O-IVδ-930` (source: Glass Elsewhere `N-IIβ-903`); **F4's first two** — Thinking
Engine `C-IIIγ-904` · Lacrima `N-Iα-905` (source: Beating Relic `C-IIIγ-902`). Keepers unchanged — the lowest designation keeps its
line. Lacrima's unit also closes its `R-29` `parity` gap (interactions section) the way Dawn That Forgot did in batch 45. **Rollback
#48** hit at this turn's open and was recovered the same turn (`reset --mixed` to the remote tip; worktree content already matched,
dirty 0). Nothing else moved.

**Quote phase, batch 45 result, 2026-10-07 — owner-directed, quotes replaced in place:** ten dossiers got their own opening
quote; every draft checked against all 301 before writing (`quote_audit.py --check`). Distinct quotes **275 → 285 / 301**;
duplicated families **5 → 4**; dossiers inside a duplicated family **31 → 20 / 301**; the Grimoire family (8) cleared
entirely. Each unit: residual 0 · 0 sections over 0.05 · `tpl.py` 0 · meets **True** · quote unique. `R-29` 285 → **286 / 301**
(parity **297**, condition **293**, series **290**) — Dawn That Forgot also closed its R-29 gaps. Word growth **+569** across
the ten; nothing deleted (`R-15`). Remaining duplicate quotes for the next batch: **16 copies** — F2's three (Eleven Fifty-Nine
· Endless Shift · Allhallow), F3's five, F4's four, F5's four, keepers unchanged (Breathing Stone · Glass Elsewhere · Beating
Relic · Vellum Man). Disclosures: **rollback #46** recovered at the open; **incident #47** (CHANGELOG emptied by an
open-before-read snippet at `87b313b`, restored from `ed80d83` the same turn — `6f33ad2`); u3's series clause completed in a
second commit (`0991a9f`), the series clause first pass having left `series` False.

**Quote phase, batch 45 open — owner's direction, 2026-10-07:** *"DO The Quote One First Because That An Identity And Learn How To Write SE Quote."*
The opening quote is the file's identity, and the clone audit found it the archive's strongest clone call: a duplicated
quote lifts the chance of a cloned section inside the pair **18 / 84 = 21.4%** against the **1.20%** baseline (Finding 7).
Measured again today: **275 / 301** quotes are distinct; **270** appear once; **5 families / 31 dossiers** are exact
duplicates — Grimoire `C-IIβ-906` (8, keeps) · Breathing Stone `C-IVδ-907` (7, keeps) · Glass Elsewhere `N-IIβ-903`
(6, keeps) · Beating Relic `C-IIIγ-902` (5, keeps) · Vellum Man `C-Iα-900` (5, keeps). Learned and written down:
**`SE_QUOTE_GUIDE.md`** (the house form from the archive's own 270 distinct quotes; six rules; the family table) and
**`tools/auditors/quote_audit.py`** (`--check "<draft>"` against all 301 quotes; `--file PATH`). Method: the lowest
designation keeps its quote — the pre-cover-up text — and every other member is re-authored **in place** in that file's own
terms (`R-15`). Batch 45 takes the **26 copy-sides**, worst-first: family size, then designation ascending. Ten this batch:
F1's seven copies (Backward Hour · Amnesia · Dawn That Forgot · Passing Bell · Once Upon · Cracked Flesh · **Sorrow Mass** —
its number-words hold is untouched and this is disclosed) then F2's lowest three (Unwaking Block · Labyrinth of the
Unfinished Mind · Moktak). **Rollback #46** hit at this turn's open and was recovered the same turn (worktree already
equalled the remote tip; `reset --mixed` only).

**Clean phase, batch 44 result, 2026-10-07 — owner-directed, replace in place:** ten worst files cleaned, one wave
each, nothing deleted (`R-15`). Re-measured after the ten: whole-section instances **164 → 84**; files carrying >= 1 whole
copied section **57 / 301 → 47 / 301**; small overlaps only **95 / 301 → 102 / 301** (the cleaned files' remaining minor
overlaps moved into the fix-later set). By section: Consequences **94 → 51** · Operational Parameters **27 → 4** ·
Combat Actions **16 → 10** · Operational Notes **14 → 8** · Testimonium 6 · Core Stat Line 2 · Breach 2 · SECC 1 ·
Escalation **2 → 0**. `--plan` after the ten: heavy sides **135 → 131**, light sides **156 → 152**, pairs **540 → 488**.
Each of the ten files verifies **0** whole-copied sections of its own (`whole.py`). `R-29` movement: **285 / 301** meets
(parity **296 / 301** · condition **292 / 301** · series **289 / 301**), disposition **301 / 301**, section-clean
**301 / 301** — the one unit that moved counters was Dreaming Plague (interactions, suppression condition, series digits).

**Restart + clean-first plan, owner's method, 2026-10-07:** check restarted; `--plan` mode added. **57 / 301** files carry
>= 1 whole copied section (54 one, 3 two: Dancing Chains · Calling Bloom · Grieving Love); **95 / 301** small overlaps only.
Whole-section copies: **Consequences 94** · **Operational Parameters 27** · **Combat Actions 16** · Operational Notes 14 ·
Testimonium 6; 14 files carry CA/OP whole. Method: clean the 57 first, then fix the 95; verify with `--plan`. **Deletion is
flagged for the owner's ruling** — `R-15` is growth-only and `A5` needs a file-named instruction (delete outright vs
replace in place). No dossier content changed.

**Quote check restarted, owner's finding, 2026-10-07 — *"The Number One CALL That It WAS Clone … Is The SE Quote … So
Restart The Check"*:** run as `clone_audit.py --quotes`; report Finding 7. **5 exact duplicate quote families covering 31
dossiers**; within families **18 / 84 pairs carry a section clone (21.4%)** vs the archive's **1.20%** baseline — an **18×
lift**, the strongest single call found. Families: *It does not end…* (8) · *The city gave us this…* (7) · *The weight is
not punishment…* (6) · *When it comes…* (5) · *Something here remembers…* (5). Every family contains clones (0.50-0.87);
the quote is a cluster marker, not proof — Lethe and Dead Air share a quote and now score nothing above 0.50, the target
state. All 31 dossiers linked in the report. No dossier content changed.

**Audit links, owner's request, 2026-10-07 — *"in audit put the link so i can try to compare them"*:** `CLONE_AUDIT_2026-10-07.md`
now links **every pair named in it** (both sides, GitHub URLs on the working branch) with a 13-command `--pair` block, plus
links to the 12 heaviest files of the **43 / 301** carrying a verbatim section. New tool mode `clone_audit.py --pair A B` prints
containment both ways, per-section scores, and every shared line with substitutions marked. Read-only.

**SECC / Combat Actions pass, owner's observation, 2026-10-07 — *"Usually The Things That Still The Same Is [SECC
Classification] Except [**Physical Form + Designation**] And [Combat Actions"*]:** measured over **301 / 301**. SECC: exactly
**2 fields carry 301 / 301 distinct values — Designation and Physical Form**; the other eight are pools (Sorrow Category 11
distinct / top in 153 · Element 14 / 90 · Comprehension 21 / 163 · Potency 25 / 73 · Entity Type 145 / 104 · Coherence 122 /
53 · Movement 81 / 52 · Manifestation 59 / 37), pooled rows covering **290 / 301** files for Sorrow Category and Element. Copy
pairs match on **2-4 SECC rows, differ on 7-10** — they share the pools, not the exact table. Combat Actions (301 / 301
tables): *The Settling* x33, *The First Weight* x30, skeleton in **29 / 301**, **1 byte-identical pair**, **36** pairs at
>= 0.50. Report: `CLONE_AUDIT_2026-10-07.md` Finding 5. No dossier content changed; repair awaits the ruling.

**Lineage pass, owner's rule, 2026-10-07 — *"The One That Win Is The One With Lower Number In Their Designation Between
Two Copy Then You Can See What Was It Before The Cover UP"*:** `clone_audit.py --lineage` implemented and run. In each
copied pair the lower designation number is the source; the diff against it is the copy's pre-cover-up state. Findings:
**Dreaming Plague `N-IVδ-927` ← Weighted Silence `O-IIIγ-924`** (5 sections; Weighted→Dreaming, Silence→Plague,
438→502, γ→δ, sector swap) **and ← Dawn That Forgot `N-IIIγ-917`** (Combat Actions + Testimonium) · **Lonely Giant
`C-IIIγ-105` ← Kind Healer `C-Iα-071`** with **residue kind x4, healer x2** still in the copy · Calling Bloom ←
Grieving Love (**love x5, grieving x1**) · Wedge ← Magistrates Strike-Through (**through x8, strike x7**) · Last Warmth ←
Letter Never Sent (**never x3**) and ← Wedge (**held x6**) · **chain `C-IVβ-041` → `C-Iα-071` → `C-IIIγ-105`** · 38
pairs are mutual shared template text, rule not applicable. Full table: `CLONE_AUDIT_2026-10-07.md`, Finding 4. Repair
awaits the owner's ruling; no dossier content changed.

**Clone audit, owner's question, 2026-10-07 — *"How To Check It They Are The Same SE But Just Change Title + Designation :
[Combat Actions] Se It And Also Check Everything Else"*:** run with `tools/auditors/clone_audit.py`; full report in
`REFERENCE_SOMNARAK_WIKI/CLONE_AUDIT_2026-10-07.md`. The audit masks registry codes, sector ids, figures and the dossier's
own name words on both sides, then compares body, prose, each section separately, and near-identical lines. **Finding 1:** no
dossier is another renamed — strongest pair `N-IIIγ-917` / `N-IVδ-927` at **0.169**, **0** pairs at >= 0.50, **36** at
>= 0.08. **Finding 2:** **43 / 301** dossiers carry at least one section copied verbatim (>= 0.90) — Consequences (26 pairs
>= 0.90), Operational Parameters (15), Testimonium (2), Combat Actions (1), Core Stat Line (1). **Finding 3:** the Combat
Actions move table is a template with the flavour word swapped (*The Settling* 33 dossiers, *The First Weight* 30), and
**Dawn That Forgot `N-IIIγ-917` / Dreaming Plague `N-IVδ-927` share it byte for byte after masking** plus 42 lines at
>= 0.90, while their narratives stay their own. **Proposed counters:** section pairs >= 0.90 and files carrying a verbatim
section (**43 / 301** today); target if the owner rules for one — no section pair >= 0.90, no file pair >= 0.30. No dossier
content was changed; repair awaits the owner's ruling.

**Boilerplate audit, owner's observation, 2026-10-07 — *"Look Like From The 300 Something SE A Lot Of Then Just A
Copy With Change Name"*:** measured with the new `tools/auditors/frame_dup.py`, which masks registry codes, sector ids,
figures and each dossier's own name words before counting 6-grams — the class every existing gate is blind to. First run
over **301 / 301** dossiers: **6,393 masked 6-gram families spanning >= 3 dossiers (36,023 instances = 4.8% of prose
material)**; **9,705 grams in exactly-2-dossier pairs (1.3%)**, which no threshold of three or more can see; worst dossier
**17.7%**, median **4.6%**, **18 / 301** above 10%, **78 / 301** above 6%. The widest families are whole sentences —
**115 / 301** dossiers carry one sensory-description sentence with only the name changed, **82 / 301** carry the
"objection is minuted at every annual review" paragraph, **71 / 301** an identical M.A.W. work-response line, **69 / 301**
the identical Resolution prefix, **67 / 301** the defence-roster paragraph — and pairs such as Moktak
`N-IIβ-910` / Passing Bell `N-IIβ-919` carry lines that are byte-identical. **Why the existing gates passed them:**
`sect.py` / `sectfile.py` count 8-grams shared by >= 10 dossiers and mask nothing, and `tpl.py` compares raw lines. The
`R-29` parity clause requires the same **sections**; it does not license the same **sentences**. **Proposal awaiting the
owner's ruling:** adopt a frame counter — target, no family at >= 3 dossiers and no byte-identical prose line between
two dossiers — and work the widest families first in units of ten, growth-only (`R-15`), each re-authored in the file's
own terms. No dossier content was changed by this audit.

| Measure | Value |
|---|---|
| Dossier body lines | 31314 |
| Lines shared by 30+ dossiers | 0 |
| **Headline** | **0.00%** |
| Dossiers in the measured archive | 291 |
| **Dossiers rewritten (fixed counter)** | **291 / 291** |
| Unfinished-text breaks outstanding | 0 |
| **Dossiers free of template residue (Workstream 6)** | **240 / 302** |
| **Dossiers section-clean (`R-27`, every description-bearing section ≤ 0.05)** | **162 / 301** |
| **Dossiers meeting `R-29` (Workstream 9)** | **138 / 301** |
| **Reference pages surveyed for the standard (Comparative Study 02, four per level)** | **20 / 20** |
| **Pairings of our dossiers against the survey (Comparative Study 02)** | **10 / 10** |
| **Breach balance (`R-28`)** | **RE 63/83 · SE 45/177 · OP 21/41 — all floors met** |
| Dossiers file-clean (`R-24`, whole-file fraction ≤ 0.05 — secondary) | 266 / 302 |
| Archive median prose generic fraction | 0.014 |
| **Dispositions classified (Workstream 5)** | **301 / 301 — CLOSED** (re-based from 302 when the second Dawn of Mourning was retired) |

## Workstream 1 — De-boilerplate (CLOSED)

Whole-file rewriting of every dossier in the archive, bespoke per entity. Rules `R-02`, `R-04`, `R-05`, `R-14`, `R-15` all bind here.

**Closed at clean 291 of 291.** Headline 34.3% → **0.00%**. Growth-only throughout: no deletions, no shared annex, no threshold gaming, and the body line count rose from the opening measurement to 31,308. Every clean was its own commit and its own gate chain, per `R-21`. The workstream is reported as closed because the measure it was defined against returns zero, not because the archive is beyond improvement — residual stock phrasing below the 30-dossier threshold still exists in older files and is logged as ordinary maintenance rather than as this workstream.

**Workstream 5 now takes over as the active line of work, and runs under [`R-22`](RULES/R-22_TEN_DISPOSITIONS_PER_BATCH.md) — ten entities per batch, one commit per entity, the `R-18` split stated before any classifying starts, quoted evidence or pending.**

**Progress: 291 / 291 dossiers rewritten — complete.** This denominator is fixed by [`R-20`](RULES/R-20_ONE_FIXED_DENOMINATOR.md) and does not move. The band fractions used before `R-20` — `73 / 73`, `10 / 10`, `8 / 8`, `1 / 76` — are superseded and are not progress figures; they described the queue, and the queue shrinks partly by spillover from other files' cleans. Headline trajectory 34.3% → 0.00%.

### Queue depth — side figures, not progress

These say where the remaining damage sits and which file to open next. A fall in any of them is **not** a clean and is never written as `x / y`.

| Queue tier | Dossiers |
|---|---|
| at 20+ shared lines | 0 |
| at 15+ shared lines | 0 |
| at 10+ shared lines | 0 |
| at 1+ shared lines | 0 |

### Next targets, in order

_Empty._ The measured queue is exhausted: `tools/boilerplate_report.py` returns a census of
`[(0, 291)]` — every dossier in the archive now carries zero lines shared by 30 or more
dossiers. The last shared line was retired by clean 290 (Ninety Seconds, `C-IVδ-918`), which
took thirty files to zero at once by spillover. Clean 291 (Glass Elsewhere, `N-IIβ-903`) was
selected on residual stock rather than on shared lines, that being the only honest measure
left.

Nothing left to re-rank. Files drop down this list as global counts shift without being touched; that movement is spillover and is never counted against the fixed `N / 291` counter. The queue is never carried over from a previous turn without re-measuring.

### Residual floor

Most cleaned files keep 0–13 lines of genuine cross-reference furniture (`**Cross-References:**`, `- See Origin section…`, `**Threat Assessment:**`). These are not chased. The structural floor is 3.1%.

### Completed cleans

Fallow 50→12, Shard 49→9, Ephemera 48→12, Border Tree 48→11, Tear 48→11, Glass 48→12, Portcullis 47→11, Thralldom 47→12, Aphasia 47→12, Forgotten Tear 47→12, Anonym 47→12, Welcome Haven 47→11, Survivors' Breath 47→10, Quagmire 47→10, Yggdrasil Wound 46→13, Repose 46→11, Grasp 46→10, Uprooted 46→11, Sleeping Tree 46→10, Frozen Mirror 45→11, Heirloom 45→9, Spire 45→10, Memory Chain 45→10, Feu Follet 45→10, Broken Whisper 45→9, Ember Phoenix 44→10, Broken Fragment 44→9, Brume 44→11, Myrmidon 44→9, Broken Ruin 44→11, Errant 43→11, Atlas 43→11, Animus 43→10, Conservatory 43→9, Home to No One 43→9, Broken Door 42→10, Tower Erased Overnight 42→9, Relic Waiting for Its Maker 42→9, Exiles' Wall 41→10, Protest No One Remembers 41→10, Pent 41→9, The Silent Child 39→11, Broken Tear 39→10, Relic of a Thousand Owners 38→9, The Wrath Flame 38→10, Soaking Rope 38→11, Sleeping Shard 38→9, Forgotten Silence 38→9, Spreading Root 37→9, Dormant Monolith 37→9, Scar Walker 36→10, Homecoming Tree 36→1, Cenotaph 35→0, Dismissed Cry 35→0, Well of Unfinished Words 34→0, Bridge to Nowhere 33→0, Perennial 33→0, The Vanished Rope 33→1, Candela 33→1, Gavel 33→1, Mourning a Life I Never Lived 32→1, Torpor 32→1, Friendless Bridge 32→0, Risus 32→1, Labyrinth of Stolen Faces 32→1, Mirror of Soaking 31→0, Swallowed Fury 31→1, Stranded Between Two Shores 31→0, Sorrow Gate 31→1, The Lost Prince 31→1, Banyan 30→8 (residual is the standing cross-reference furniture), First Tear 30→0, The Frozen Veil 30→0, Laughing Mask 29→0, Hums 29→1, Apocrypha 28→10 and Homeless Sorrow 28→9 Driftglass 27→8 and Sehnsucht 27→8 and Breach 26→7 and Floating Fragment 25→10 and Neverlast 25→11 and Forgotten Soul 25→11 and Drowned Echo 24→8 and Corrosion Dream 24→9 and Torn Window 24→9 and Door to Nowhere 23→8 and Seething Tundra 21→4 and Mourner's Bloom 21→2 and Frozen Fury 21→0 and Absent Landmark 20→2 and Pandora's Jar 19→7 and Folly 19→1 and Somnium 19→1 and Collapsed Seed 18→0 and Hollow Echo 18→1 and Bridge of the Unchosen 18→0 and Dreaming Ruin 18→0 and Lacrima 17→0 and Hollowcast 16→0 and Miscast 16→0 and Clapperless 16→0 and Neglect Learned to Listen 15→0 and Aphonia 15→0 and Unwitnessed 15→0 and Anger Underfoot 15→0 and The Angry Maiden 15→0 and Unrung 15→0 and Sky of Borrowed Faces 14→0 and Bulwark 14→0 and The Inherited Debt 14→0 and Fading Fruit 14→0 and Doorway to Nowhere 14→0 and Forgotten Name 14→0 and Mirror of Rising 14→0 and The Debt Chain 14→0 and Deadline 14→0 and Sorrow Seed 14→0 and Midnight Choir 14→0 and Unsaid Blossoms 14→0 and Apnea 13→0 and Memory Lake 13→0 and Hollow Architect 13→0 and Barrier of Nothing 13→0 and Nemo 13→0 and Vanity Asleep 13→0 and Harbinger 13→0 and Deteriorata 13→0 and Cold Burn 13→0 and Redacted 13→0 and The Empty Mask 13→0 and Broken Clocktower 13→0 and Double Mouth 13→0 and Carrying Nothing 13→0 and Crucible 13→0 and Pall 13→0 and Flowing Seed 13→0 and Life Behind Glass 12→0 and Weight of Silence 12→0 and Forgotten Shadow 12→0, Vanished Tree 13→0, Thralldom 12→0, Patina 12→0, Last Fruit 12→0, Remembrance 12→0, Torn Flower 13→0, Aphasia 12→0, Black River 12→0, Broken Compass 12→0, Echo of Kindness 12→0, Holdout 12→0, Frozen Tear 12→0, Cleaved 12→0, Rem 12→0, Floating Tree 12→0, Soaking Shadow 12→0, Aegis 12→0, The Silent Maiden 12→0, Harvest Beyond the Gate 12→0, Unheard 12→0, Hollow Tree 12→0, Melting Rope 11→0, The Kind Healer 11→0, Sorrow Storm 11→0, The Grieving Maiden 12→0, Yggdrasil Wound 11→0, Panopticon 11→0, The Lonely Giant 11→0, Portcullis 11→0, Mirror of Broken 12→0, Loom of Unlived Dreams 11→0, Welcome Haven 11→0, Drowned Roots 11→0, The Guarding Bird 10→0, The Smothering Mother 11→0, The Silent Child 11→0, Walking Calendar 11→0, Every Last Goodbye 11→0, Anonym 10→0, Repose 11→0, Border Tree 11→0, Sleeping Weight 10→0, Restless Gap 11→0, Forgotten Soldier 8→0, Rift 11→0, Quagmire 10→0, Neverlast 10→0, Pyre of Truths 10→0, Whispering Gallery 10→0, Swallow 9→0, The Memory Thief 9→0, The Wrath Flame 9→0, Dormant Monolith 9→0, Relic Waiting for Its Maker 9→0, Forgotten Silence 9→0, Broken Tear 9→0, Sleeping Shard 9→0, Home to No One Who Knew Me 9→0, Pent 9→0, Conservatory 9→0, Soaking Rope 9→0, Tear Too Small to Honor 9→0, Broken Whisper 9→0, Protest No One Remembers 9→0, Memory Rain 8→0, Cracked Mirror 8→0, The Orphaned Bell 8→0, I Alone Crossed 8→0, Soaking Shard 8→0, Collapsed Whisper 8→0, Memorial Flame Mid-Ceremony 8→0, Willing Chains 8→0, Spire of Unanswered Prayer 8→0, Driftglass 8→0, Sehnsucht 8→0, Ember Phoenix 8→0, Brume 8→0, Apocrypha 8→0, Broken Fragment 8→0, Relic of a Thousand Owners 8→0, Feu Follet 8→0, Myrmidon 8→0, Atlas 8→0, Forgotten God 7→0, Forgotten Market Stall 7→0, Sorrow Fountain 7→0, Redcage 7→0, Dancing Chains 7→0, Memory Lock 7→0, Devouring Bloom 6→0, Floating Shard 7→0, Rising Well 7→0, Fading Whisper 7→0, Floating Pillar 6→0, Face Beneath Masks 6→0, Briar 6→0, The Rejector 6→0, Learned Your Face 6→0, Frozen Echo 6→0, The Hollow Knight 6→0, The Debtor 6→0, The Inheritor 6→0, The Hollow Saint 6→0, Flotsam 6→0, Broken Well 6→0, The Echo Compass 5→0, Sunken Pillar 6→0, The Rage Statue 5→0, The Masked Dancer 4→0, Broken Mirror 4→0, The Debt Eater 5→0, Kind Healer's Shadow 4→0, Whispering Walls 4→0, Frozen Window 4→0, Broken Promise 4→0, Debt-Collector's Lantern 2→0, The Debt Scale 1→0, The Hollow Choir 1→0, Owed 1→0, The Grieving Colossus 1→0, The Cracked Hourglass 1→0, Broken Clock 1→0, Weeping Willow 1→0, Spreading Well 1→0, Burning Root 1→0, Floating Well 1→0, Screaming Masonry 1→0, Beating Relic 1→0, Thinking Engine 1→0, Eleven Fifty-Nine 1→0, Backward Hour 1→0, Cracked Flesh 1→0, Lethe 1→0, The Foam Flood 1→0, The Happy Mask 1→0 (residual in the others is the standing cross-reference furniture).

## Workstream 6 — Template residue (OPEN, newly measured)

Raised by the archive owner on 2026-10-04, after Workstream 1 closed: *"Some From What You Explain Is Still Templatey Because Of The Previous AI"*. Governed by [`R-23`](RULES/R-23_LABELS_MAY_REPEAT_VALUES_MAY_NOT.md); full finding in [`TEMPLATE_RESIDUE_AUDIT.md`](TEMPLATE_RESIDUE_AUDIT.md).

The owner is right and the `0.00%` is also right. `tools/boilerplate_report.py` measures the `body` scope — `len(s) > 40 and not s.startswith(('|', '#', '>', '`'))` — so **no table row, blockquote or heading was ever counted**. The previous AI's slot-filled cells live exactly there. Workstream 1 is not reopened and its counter is not revised; this is a second measurement of a region the first one never looked at.

**Measured by `/home/user/wikitools/tpl.py`** — a line shared by ≥ 10 dossiers, ≥ 10 words of content, not on the sanctioned-furniture list (table headers, the five system blockquotes, values forced by the SECC code or the entity's role, the two global combat rules).

| Measure | Value |
|---|---|
| Distinct residue lines | 59 |
| Residue instances | 809 |
| Dossiers carrying residue | 201 / 303 |
| **Dossiers clean (fixed counter)** | **102 / 303** |

Opening baseline was 146 distinct / 3,745 instances / 11 clean. The first ten entities taken under this workstream were all drawn from the Workstream 5 pending pool, so each one closed a disposition row in the same commit as its clean.

Threshold is ten, not thirty, because this defect clusters by entity *role*: six Object/Place dossiers sharing one word-identical breach block is the normal size of it, and a thirty-dossier threshold scores that as zero.

### Order of work

1. **Operative values** — `**First Target**` (48 dossiers), breach `**Movement**` / `**Effect**`, the stock interaction effect cells. These block Workstream 5.
2. **Placeholder-instruction cells** — `**Before/During/After use**`, `**At limit**`, `**Distinctive markers**`, `**Position / movement**`, `**Material / signature**`. ~1,200 instances, mechanical, low risk.
3. **Reader-facing binary choices** — `Endure it … / Struggle free …` (178) and siblings.
4. **Slot-filled Origin prose** in the thin files, done entity by entity alongside its disposition.

Fixes are **growth, not deletion** (`R-15`). A cell is not fixed by removing it or by rewording it just under the threshold.

### Second measure — the Tale standard (`R-24`)

Raised by the owner on 2026-10-05: *"make sure that a lot of text is not just copy & paste … the Tale
section is already fixed."* He is right twice over. The Tale **is** finished — measured across all
298 dossiers that carry one, **no Tale section shares an eight-word run with ten other dossiers** —
and the sections around it are not. Measured with [`sect.py`](RULES/R-24_THE_TALE_STANDARD.md):

| Section | Score | Section | Score |
|---|---|---|---|
| `이야기 (Narratio)` — **The Tale** | **0.00** | `Behavior` | 0.64 |
| `증언 (Testimonium)` | **0.00** | `관찰 기록 (Observation Log)` | 0.65 |
| `SECC Classification` (all furniture) | **0.00** | `Breach Behavior` · `Story Log` | 0.77 |
| `Origin` | 0.16 | `Trivia` · `Expansion Behavior` | 0.80 |
| `Apex` / `Watch` Record | 0.42 / 0.45 | `감각 묘사 (Flavor Text)` | 0.89 |
| `Appearance` | 0.52 | `Registrum` · `Final Observation` | 0.96 |
| `Warden Record` | 0.62 | `M.A.W.` · `Operational Parameters` · `Combat Record` | **0.97–0.98** |

**First two files taken under this rule.** Moktak `N-IIβ-910` went 0.116 → **0.001** and Chain of
Memories `N-IIIβ-200` — then the most generic dossier in the archive — went 0.386 → **0.001** across
seventy rewritten lines, which also released the last entity held pending under Reason 1.
Nine dossiers have now been taken under this rule, worst first:

| Dossier | Before | After | Subs | Words |
|---|---|---|---|---|
| Chain of Memories `N-IIIβ-200` | 0.386 | **0.001** | 70 | 5,476 → 6,607 |
| Survivor's Span `N-IIβ-993` | 0.360 | **0.002** | 62 | 4,859 → 5,966 |
| The Unconsoled `C-IIIγ-248` | 0.298 | **0.000** | 57 | 5,213 → 6,142 |
| The Extinguished `N-IVγ-250` | 0.253 | **0.000** | 55 | 5,623 → 6,396 |
| The Unspoken Line `C-IVδ-251` | 0.247 | **0.001** | 56 | 5,739 → 6,665 |
| The Undelivered Thanks `N-IIIβ-247` | 0.243 | **0.000** | 49 | 5,385 → 6,199 |
| Broken Door `O-IIβ-757` | 0.224 | **0.004** | 62 | 6,625 → 7,760 |
| Vellum Man `C-Iα-900` | 0.224 | **0.000** | 63 | 2,880 → 4,106 |
| Moktak `N-IIβ-910` | 0.116 | **0.001** | 14 | 4,114 → 4,665 |

All nine kept `RESIDUAL 0` and residue 0 and all nine grew. Eight of the nine closed a Workstream 5
row in the same commit, because a dossier cannot be classified while its interaction cells are
instructions to an observer rather than observations. Vellum Man also lost a verbatim duplication
of its Tale inside its Origin section, which `verify.py --dupes` had been reporting for weeks.

**Comparative study.** `COMPARATIVE_STUDY_01_VELLUM_MAN_AND_BROKEN_DOOR.md` sets the two most recent
completions against each other and against two published Abnormality articles (`O-04-72` The
Burrowing Heaven, `T-09-97` Old Faith and Promise). Its three carried-forward findings — Story Log
escalation, the "record X, Y, Z" phrasing as residue even when `tpl.py` is silent, and
instrument-and-hazard unification — are quality bars for Workstream 7.

An earlier version of this block claimed the ten batch-2 dossiers were still generic at 0.103–0.129.
That was the first, furniture-blind cut of the metric. On prose they measure **0.014–0.041** and all
ten are at the standard; the claim has been corrected here and in `R-24` rather than quietly dropped.
What survives in a typical unrewritten file is the Combat Actions flavour text, the Battle Phases,
the M.A.W. appearance and ability lines, the observation-stage cells and the stock interaction
effects — 182 dossiers still sit above 0.05.

One generator artefact was found and repaired by this pass: 29 dossiers published an unevaluated
Python expression in the Combat Record `Difficulty` row, with the entity's numeric suffix standing
where the difficulty word belonged. All 29 were rebuilt from each file's own `Work difficulty` row.


## Volume index

This record outgrew the size at which GitHub renders a file in the browser (it truncates blobs
at roughly 500 KB and stops displaying them past about 1 MB). The closed work now lives in the
numbered volumes below. **Nothing was rewritten, reordered within a volume, or deleted** — every
block was moved byte-for-byte out of the file as it stood at `7b804e7`, and `WORK_IN_PROGRESS.md`
remains the authority on what is open and what comes next.

| Volume | Bytes | Original lines | Contents |
|---|---|---|---|
| [WORK_IN_PROGRESS_VOL_01.md](WORK_IN_PROGRESS_VOL_01.md) | 298,676 | 430–3351 | Batches 17, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 … |
| [WORK_IN_PROGRESS_VOL_02.md](WORK_IN_PROGRESS_VOL_02.md) | 250,882 | 3841–5199 | Batches 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46 … |

Volumes are ordered as they stood in the file: **Volume 01 is the older work**, the highest
number is the most recent archived work. The batches still being worked on are above, not in a volume.

## Workstream 9 — The R-29 Standard (opened 2026-10-05)

The owner named the target: *"what an abnormality wiki does, but better."* `R-29` writes that down
as a test with two halves, and `tools/wikistd.py` measures it.

**Parity — nine sections every dossier must carry**, mapped to what an abnormality page has:
identification, stats, work results, escalation/breach, equipment with its cost, flavour text,
observation and story logs, trivia, related entities.

**Better — six clauses above the floor:** every figure traceable to the dossier's own record; no
line shared with ten others; one instrument per holding and no instrument reused; the institutional
cost stated; projections labelled as projections; a disposition classified under `R-19` with quoted
evidence.

**Baseline, the day the rule was written: 27 / 302 meet it.**

| Clause | Dossiers |
|---|---|
| Parity complete | 267 |
| Specific management condition | 229 |
| Own numeric series | 176 |
| Disposition classified | 300 |
| Section-clean (`R-27`) | 70 |

Section-cleanliness is the binding constraint, as it has been since `R-27`. The parity gaps are
concentrated: 34 dossiers have no Entity Interaction Record, and four short-form Unknown-wing files
were missing seven sections each. The first of those four — The Glass Silt Drifter `O-IIIγ-1052` —
was completed from its own canon this turn and now meets `R-29` in full.

### Progress, 2026-10-05, second turn

**`R-29`: 27 → 43 / 302.** One `gate.sh` commit per dossier, each pushed and verified against the
remote ref. Draft pull request #12 into `NON-WIKI` is open and is not merged (`R-13`).

| Clause | Start of turn | Now |
|---|---|---|
| **Meets `R-29`** | **27** | **43** |
| Parity complete | 267 | 270 |
| Specific management condition | 229 | 236 |
| Own numeric series | 176 | 179 |
| Disposition classified | 300 | 302 |
| Section-clean (`R-27`) | 70 | 79 |

Dossiers by how many conditions they still fail: **0 → 43 · 1 → 114 · 2 → 112 · 3 → 26 · 4 → 7.**
Archive-wide there are **1,458 dirty sections in 223 dossiers**, which is the size of the Workstream 7
reset pass.

| Dossier | Gap | How it was closed |
|---|---|---|
| The Unbroken Pledge `N-IIIβ-1056` | 7 parity sections | Authored. Instrument: turns of the braid, read as ridges at the throat. Three bearers cannot be treated because the Office will only say *service cannot be confirmed*; this ties it to the Year 4164 instrument defined in the Forgotten Soldier file. |
| The Ancestral Guilt `N-Vω-1055` | 7 parity sections | Authored. Instrument: lines of script, one per generation of the visitor's lineage. The Starting Sorrow Gauge row read `980/980` against `6,800 / 6,800` in the Combat Record and was reconciled to the Combat Record; one pre-existing ` ,` seam repaired. |
| The Singing Needle `O-IVγ-1053` | 7 parity sections | Authored. The hazard and the instrument are one object: the picket anemometer cups stop when it sings, and the first bleed follows a median 4 seconds later. |
| Survivor's Span, Grasp, Errant | management condition | The sentence was already in the file as "Management is … / turns on …"; moved into the `Management:` form. `R-18` batch-short, nothing invented. |
| The Unspoken Line `C-IVδ-251` | management condition | One line written from its own Response sequence. |
| Uprooted, Memory Chain, Animus, Forgotten Tear | one dirty section | The whole section hung on one slot-filled sentence (below); replaced by one written from the file. |
| Mirror of Rising, Deadline | one dirty section, and `R-01` | The same sentence. Both also opened their Expanded origin context by narrating an earlier version of the file ("has been removed"); converted to cause. |
| Foam Flood, Soot Fry | one dirty section | One paragraph, the Interaction Pattern opener, rewritten from each file and deliberately not as parallel templates (`R-04`). |
| Exiles' Wall | one dirty section | One sentence, the stock "record the first X, the first Y" method opener. |
| The Debt Chain, Forgotten Name | `R-01` only | Each opened its Expanded origin context by narrating an earlier version of the file; converted to cause from facts already in the file. No `R-29` movement: both still have dirty sections. |

**The largest single residue found.** The sentence *"A choice presented to the observing worker at
the climax of contact. One path reveals `<Name>`; the other feeds it."* sits, name slotted, in the
`최종 관찰 (Final Observation)` section of **211** dossiers (217 at the start of the turn). It is `R-23`
shape 2, slot-filled prose, and it is the reason that section is dirty across most of the archive
(0.73 on the league table at the start of the turn). It is careful-detail under `R-18`: each
replacement is written from the one file, is longer than the template, and must not restate the two
table options. In a dossier where it is the only dirty line, one sentence completes the dossier.

The second family is the third sentence of the Interaction Pattern paragraph, *"… the team must
record whether the response changes in sound, movement, temperature, memory pressure, Sorrow Gauge,
or containment stability,"* which **127** dossiers still carry.

**Tooling changed this turn.**

- `tools/gate.sh` had the previous session's branch name hard-coded and would have pushed this
  session's commits there. It now pushes the checked-out session branch, refuses `main` and
  `NON-WIKI`, requires each linter's explicit PASS string (`R-11`), runs `audit_lore_archive.py`,
  regenerates and stages the metrics (the old step printed PASS unconditionally, and the CI
  SSOT-parity step was red on the inherited tree), and verifies HEAD against the remote ref.
- `tools/wikistd.py` keyed the disposition lookup on the first code inside the file, which misread
  the Kind-Healer progression variants `071b` and `071c` (filed under the base code by design). It
  now keys on the filename code; the dashboard reads 302 / 302, matching the index.
- `tools/dirtylines.py` (new): for each section over 0.05, only the lines inside it that carry
  shared 8-grams. Four dossiers were finished on its output, each on a single sentence.
- `tools/editmeta.py` (new): finds candidate `R-01` sentences (reconciliation notes about earlier
  wording). It reports and never edits.

**“Do Over All SE Docs Review” (2026-10-09) — a whole-wing defect audit for the classes the five gate tools do not cover. Not a batch: no batch number, no couple work.** Taken on the owner's directive after Batch 75 closed the fix phase at zero. `verify`, `tpl`, `sectfile`, `wikistd` and `couples` measure whether a dossier is complete, templated, self-similar, standard-conformant and non-overlapping with its neighbours. None of them asks whether a section *says what its heading claims*, whether prose was left **unfinished**, or whether a whole block was **pasted twice**. That is the gap this review closes. A new tool, `tools/review.py` (`509ab3e`), was written so the audit survives sandbox resets and can be re-run: `python3 tools/review.py [--check NAME] [--file PATH]`, eight checks — `truncated`, `midlower`, `placeholder`, `duprow`, `typemix`, `emptysec`, `shortsec`, `heading`.

**The first run produced 2,156 raw findings and almost all of them were the archive's own conventions, not defects.** Every check was then calibrated against all 301 dossiers before a single number was believed. The raw counts and what they actually were:

| check | raw | real | what the rest turned out to be |
|---|---|---|---|
| `truncated` | 29 | **0** | Every long no-terminal line ends in an epigraph attribution — `— Majin`, `— R.D. Researcher, Archive`, `— Sentinel Harin, post-watch` — which is house style, or is a multi-line table cell ending in `\|`. The short ones are song lyrics. A hard character cap was tested for and is not present. |
| `midlower` | 69 | **0** | `R.D. catalogued` and `M.A.W. extracted` — the abbreviations in every dossier, read as sentence starts. |
| `placeholder` | 13 | **0** | Prose *about* placeholders: “the placeholder fields have been filled from the SECC header.” Work already completed, not an unfilled slot. |
| `duprow` | 672 | **0** | The same row label in the summary table near the top and the detail table further down. By design. |
| `emptysec` | 561 | **0** | An H2 container whose entire content is an H3 — `## Combat Record` → `### Core Stat Line`. Template shape. |
| `shortsec` | 672 | **0** | Those same containers, plus `## Document Information`, which is a closing table. |
| `typemix` | 48 | **6 — REAL** | Vocabulary derived from the wing: Weapon sections declare WEAPON/FANTASY/PRIMAL/BLUNT/RANGE/GUN, Suit declares ARMOR or PROTECTIVE ATTIRE, Stigma declares ACCESSORY or STIGMA. Only a Suit or Stigma slot declaring a weapon class is a contradiction. |
| `heading` | 28 | **2 files — REAL** | Twenty of the twenty-two are `### Escalation Notes` appearing once under `## Activation / Expansion Behavior` and again under `## Breach Behavior` — different content under different parents, which is by design. Two files duplicate a whole Relic block. |

**Defect class 1 — a Weapon's Category line copied into the Suit and Stigma blocks. Six findings in three dossiers, all six fixed and pushed.** In each file the Suit and Stigma sections carried the Weapon's `**Category:**` line **including the parenthetical naming the weapon's own object**, so a shroud declared itself a blade and a hair clip declared itself a cleaver. Parentheticals were taken from each section's own Appearance text.

- **Memorial Flame Mid-Ceremony `C-IVδ-763`** (`9d7a1f1`) — the Suit declared `SHORT BLADE (Antique Brass Bodkin)` while its Appearance is a shroud of deep-blue silk gone grey with ash → `ARMOR (Ash-Greyed Mourner's Shroud)`; the Stigma declared the same while its Appearance is a wick ember mark on the skin → `ACCESSORY (Purple Wick Ember Mark)`.
- **Debt-Collector's Lantern `N-IIβ-250`** (`cfbc64e`) — the Suit declared `GUN (Flared Bronze Lantern Hand-Cannon)` while its Appearance is a lead-weighted oilskin trench-coat → `ARMOR (Lead-Weighted Oilskin Trench-Coat)`; the Stigma declared the same while its Appearance is a lantern-wick mark in the bearer's pupil → `ACCESSORY (Pale Lantern-Wick Mark)`.
- **Pall `C-IIβ-280`** (`665e52b`) — the deepest of the three. The Suit block carried the Category *and* the Weapon's Appearance: it declared `BLADES (Mirror-Polished Square Cleaver)` and then described a broad rectangular surgical cleaver, in a section named for a pallbearer's **layered shroud** whose Ability works by dissipating impact through layered cloth. → `ARMOR (Layered Pallbearer's Shroud)`, and the two Appearance paragraphs re-authored as the shroud, stitched from fabric steeped in tears that were never shed in front of anybody, which gives up a layer for every thing that lands. The Stigma → `ACCESSORY (Mourning Ribbon Hair Clip)`. The shroud prose went through three echo passes: “one at a time and” and “the next and the next” were stock in eighteen files, and “that reaches the wearer and the wearer” in two more. +39 words.

**Defect class 2 — a whole Relic block present twice. Two dossiers, both fixed and pushed; the owner put the decision to the review (“You Decided Based Of Research”) and it was settled on the evidence below.** `The Orphaned Bell C-IVδ-001` and `Driftglass O-IIIγ-914` each carry a `## Activation / Expansion Behavior` block **and** a `## Activation Behavior` block, and each of those contains its own `Tool Use Profile`, `Log and Method`, `Escalation Notes` and `Detailed Activation Record`. Eighty-eight files in the wing use `## Activation Behavior`; **these two files are the only ones in the wing that also carry `## Activation / Expansion Behavior`.** The two copies are not identical — the Log and Method rows are timed differently and the prose is independently worded — and in the Orphaned Bell the first block also holds a unique `### O-Relic (Officium) — Channeled Invocation` table that exists nowhere else in the file. So this could not be fixed by deleting a duplicate. The evidence settled it:

- `## Activation Behavior` is the standard heading in **88** dossiers, and in 87 of them its first sub-section is `### Tool Use Profile — X-Relic`, followed by Log and Method, Escalation Notes and Detailed Activation Record. Both second blocks match this shape and carry the three `> **This Relic…**` qualifier lines and the Activation Trigger / Effect / Duration / Risk rows. **The second block is canonical in both files.**
- `## Breach Behavior` exists in **147** dossiers, and **all 147 open with a `| **Breach Type**` row**. Neither of these two files has one.
- **Driftglass `O-IIIγ-914`** (`396500c`, 526 → 489 lines): the first block opened with a Breach Type / Movement / Effect / Duration / Suppression table. That is genuine breach content, mis-filed under a heading used nowhere else — not a duplicate. It is now a proper `## Breach Behavior` section carrying its own Escalation Notes (which was breach-flavoured: “spatial and quiet”, the junction sequence and drift speed). The duplicated Tool Use Profile, Log and Method and Detailed Activation Record sharing that block were removed. The Activation block below is untouched.
- **The Orphaned Bell `C-IVδ-001`** (`adc74c4`, 561 → 509 lines): this file has no breach content at all. The first block's Activation Trigger and Effect were repeated **verbatim** in the second, and its containment wording is carried in the second block's Management row. Its one unique holding was the `### O-Relic (Officium) — Channeled Invocation` table — How to Channel, Beneficial Effect, Risk, Termination Method — which exists **nowhere else in the wing**. That table was moved into the standard Activation Behavior block ahead of the Tool Use Profile; the duplicated block was removed.

`python3 tools/review.py` over 301 dossiers now reports **`heading` 0 and `typemix` 0**, and the wing is still at **0 couples / 301** — the fix phase did not regress.

**The Batch 68 figure for first-draft echo was wrong and has been corrected in place.** The block claimed that *“eight of the ten units scored their worst echo on a first draft”*. Nothing measured supports that: the batch table holds first-pass echo counts for **three** units only (7, 8 and 9 — 17→1, 5→1 and 11→1 echoed grams) and names **one** exception (unit 6, clean on the first pass). Units 1–5 and 10 have their word deltas recorded but no first-pass echo measurement. The count is now **three of the ten**, with the old figure quoted and the reason for the correction written beside it. Recorded, not force-pushed.

**PR #13 now notes that the Driftglass defect it recorded has been resolved.** Its Batch 67 disclosure said Driftglass *“carries its entire relic triad twice — `### Tool Use Profile` at line 160 and again at 217”*. That is the block this review restructured at `396500c`. The body was updated to say so — which took care, because the body stands at **262,143 / 262,144 bytes** against GitHub's limit, leaving **one byte** of headroom. `gh pr edit` fails on this repository with a Projects-classic GraphQL deprecation error and exits non-zero **without applying the edit**; the update had to go through `gh api -X PATCH`. The PR remains `OPEN`, draft, `MERGEABLE` — the owner merges (`U4` / `R-13`).

**Two further defects were found by hand during the review and are recorded but not yet fixed.** (1) RESOLVED (`903aa74`) — Pall `C-IIβ-280`'s **Weapon** block held three different objects at once: the Category read `BLADES (Mirror-Polished Square Cleaver)`, the Attack Pattern and Ability described a shield-bash and a launched barbed javelin, and the Appearance described a needle-pointed triangular stiletto, twenty-two centimetres, three-edged, with a teardrop pommel and a braided mourning-thread grip. None of the wording was borrowed from another dossier — `needle-pointed triangular stiletto`, `teardrop pommel`, `Mirror-Polished Square Cleaver` and `Veil Bastion` each occur in exactly one file in the wing — so this was an inconsistency inside the block rather than a paste. The **Damage Application** row already supplies the reading that resolves it: *“Nothing on this holding has ever cut anybody; the cleaver is listed because the armoury lists it and is kept in the outer room.”* The armoury's name for the piece is the fiction's own, not the file's error, so the name stays and the Category parenthetical now reads `BLADES (Triangular Surgical Stiletto)` — naming the object the Appearance describes. (2) The Orphaned Bell splits its two Relic blocks with a stray `## Activation Behavior` H2 that sits *between* them rather than before either.

**The tool is left in the repository as a re-runnable gate.** `python3 tools/review.py` over 301 dossiers now reports `typemix` 0 and `heading` 8 (the two known duplicated-block files); the other six checks are calibrated to report only what is not house style.



**Batch 75 — CLOSED at five. This is the closing batch of the fix phase: couples in the plan fall 5 → 0 / 301, and the wing is at ZERO. Every stage of the program is now complete.**

Taken on the owner's “p”, with the owner electing **“clear all five in one batch (75)”** when asked what the second batch should be. That answer **released the frozen pair** — Melting Rope `N-IIIγ-447` × Forgotten Shadow `N-IIβ-453`, 0.72 in `### M.A.W. Use Notes`, held by standing decision since batch 61 and never worked in thirty-five batches. It was the last couple in the wing. It is gone.

**The fix phase is over.** From 261 couples at the opening of batch 61 to **0 couples across 301 dossiers**, worked one file at a time, the lighter side of each pair rewritten in its own terms, growth only (`R-15`), every unit pushed and verified in the turn it was applied. No dossier in the wing now shares a distinctive passage with another.

**The freeze had held for thirty-five batches and was released by the owner, not by the worker.** It is recorded here because the standing decision was real and was kept: batches 61 through 74 left that pair alone, even when it was the worst tie in the wing and even when the ladder's worst-first rule pointed straight at it. It was cleared in a single unit once the owner released it — one paragraph, twenty-five words, and the heaviest tie in the archive came apart.

**Unit 4 emptied the 0.50–0.59 tier.** Corrosion Dream's two blocks took the last couple in that band, leaving the released 0.72 as the only thing in the wing. Unit 5 then took that too. The tier table — 0.70+ / 0.60–0.69 / 0.50–0.59 — is now empty in all three bands.

**The last three units each echoed this archive's own work from earlier in the same turn.** Corrosion Dream collided with **Every Last Goodbye (unit 3 of this batch, twenty minutes earlier)** on “with continued exposure the first impression”. Memorial Flame collided with **Face Beneath Masks (unit 2, ten minutes earlier)** on “and this is what turns”. By the end of the batch the corpus being differed from was, in real time, the batch itself.

**Rollbacks #109 and #110 both struck this turn** — one at the turn boundary, one mid-unit after the Remembrance commit had been made locally. Both were recovered with `git fetch` + `git reset --mixed FETCH_HEAD`; nothing force-pushed, nothing lost. Ten rollbacks in a row now recovered this way.

| # | Dossier | Structure | Fixed in place | Couples | Words (before → after) |
|---|---|---|---|---|---|
| 1 | [Remembrance](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-115_Remembrance_%EA%B8%B0%EC%96%B5%EC%9D%98_%EC%9A%B0%EB%AC%BC.md "SE-C-IIIγ-115_Remembrance_기억의_우물.md") | O-Relic SE — Offertorium | the `**Expanded origin context**` paragraph | **1** | 6,970 → 6,991 (+21) |
| 2 | [Face_Beneath_Masks](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-II%CE%B2-689_Face_Beneath_Masks_%EC%8A%A4%EB%A9%B0%EB%93%A0_%EB%B2%BD.md "SE-N-IIβ-689_Face_Beneath_Masks_스며든_벽.md") | Subject SE | the Wall Veil's appearance, ability and cost | **1** | 7,923 → 7,962 (+39) |
| 3 | [Memorial_Flame_Mid-Ceremony](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-763_Memorial_Flame_Mid-Ceremony_%EC%82%AC%EB%9D%BC%EC%A7%84_%EB%B6%88%EA%BD%83.md "SE-C-IVδ-763_Memorial_Flame_Mid-Ceremony_사라진_불꽃.md") | Non-Subject SE | the shroud's appearance and ability | **1** | 7,602 → 7,642 (+40) |
| 4 | [Corrosion_Dream](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-III%CE%B3-915_Corrosion_Dream_%EB%85%B9%EC%8A%A8_%EB%8B%A4%EB%A6%AC.md "SE-O-IIIγ-915_Corrosion_Dream_녹슨_다리.md") | Subject SE | two flavour-text blocks | **1** | 7,336 → 7,343 (+7) |
| 5 | [Melting_Rope](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-III%CE%B3-447_Melting_Rope_%EB%85%B9%EC%95%84%EB%82%B4%EB%A6%B0_%EB%B0%A7%EC%A4%84.md "SE-N-IIIγ-447_Melting_Rope_녹아내린_밧줄.md") | Subject SE | the `### M.A.W. Use Notes` paragraph — **the pair released from the freeze this turn** | **1** | 7,280 → 7,305 (+25) |

- `C-IIIγ-115` Remembrance — `647e7fe` — PUSH VERIFIED — 1 couple cleared — [[SE-C-IIIγ-115_Remembrance_기억의_우물](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-115_Remembrance_%EA%B8%B0%EC%96%B5%EC%9D%98_%EC%9A%B0%EB%AC%BC.md "SE-C-IIIγ-115_Remembrance_기억의_우물.md")]
- `N-IIβ-689` Face Beneath Masks — `4c89354` — PUSH VERIFIED — 1 couple cleared — [[SE-N-IIβ-689_Face_Beneath_Masks_스며든_벽](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-II%CE%B2-689_Face_Beneath_Masks_%EC%8A%A4%EB%A9%B0%EB%93%A0_%EB%B2%BD.md "SE-N-IIβ-689_Face_Beneath_Masks_스며든_벽.md")]
- `C-IVδ-763` Memorial Flame Mid-Ceremony — `c578599` — PUSH VERIFIED — 1 couple cleared — [[SE-C-IVδ-763_Memorial_Flame_Mid-Ceremony_사라진_불꽃](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-763_Memorial_Flame_Mid-Ceremony_%EC%82%AC%EB%9D%BC%EC%A7%84_%EB%B6%88%EA%BD%83.md "SE-C-IVδ-763_Memorial_Flame_Mid-Ceremony_사라진_불꽃.md")]
- `O-IIIγ-915` Corrosion Dream — `8470a6a` — PUSH VERIFIED — 1 couple cleared — [[SE-O-IIIγ-915_Corrosion_Dream_녹슨_다리](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-III%CE%B3-915_Corrosion_Dream_%EB%85%B9%EC%8A%A8_%EB%8B%A4%EB%A6%AC.md "SE-O-IIIγ-915_Corrosion_Dream_녹슨_다리.md")]
- `N-IIIγ-447` Melting Rope — `3c934d6` — PUSH VERIFIED — 1 couple cleared — [[SE-N-IIIγ-447_Melting_Rope_녹아내린_밧줄](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-III%CE%B3-447_Melting_Rope_%EB%85%B9%EC%95%84%EB%82%B4%EB%A6%B0_%EB%B0%A7%EC%A4%84.md "SE-N-IIIγ-447_Melting_Rope_녹아내린_밧줄.md")]


**The section mix is empty, because there are no couples left to distribute.**

**There is no Batch 76 to open.** With the fix phase closed and every other stage already at its target, no work remains in this program. `R-26` forbids padding a batch to reach a number, so nothing is opened for the sake of it. What remains is the standing housekeeping: PR #13, which the owner merges (`U4`), and the two volume splits, which are current.

Disclosures: the turn opened on a rolled-back sandbox and was levelled with `git fetch` + `git reset --mixed FETCH_HEAD` (rollbacks **#109** at the boundary and **#110** mid-unit). Word counts are measured against `b3a77f2`, the base Batch 75 landed on. The zero was measured twice, in two separate scans, before it was recorded here. PR #13 was **not** updated — its body stands at 262,124 / 262,144 B with 20 B of headroom; the full record with links is here and in `CHANGELOG.md`.


**Batch 74 — CLOSED at five; the fix phase continues: couples in the plan fall 10 → 5 / 301, with 5 cleared and none newly measurable, and no file in the wing newly measurable against another.**

Taken on the owner's “p” after Batch 73 closed at five. The rung stayed at five for the second batch running, on the same reasoning as before: `R-26` climbs on evidence, and this work is not “simple” by that rule's own test — every dossier here runs between 4,800 and 9,900 words with a full section set. Five were opened and five were finished.

**The wing is down to five couples, and four of them are reachable.** What remains: the frozen 0.72 (Melting Rope × Forgotten Shadow, held by standing decision), and four pairs sitting **exactly on the 0.50 floor** — Remembrance × Labyrinth of Stolen Faces on Origin, The Happy Mask × Face Beneath Masks on M.A.W. Suit, I Alone Crossed × Memorial Flame Mid-Ceremony on M.A.W. Suit, and Weighting Bird × Corrosion Dream on 감각 묘사.

**The fix phase is now one batch from its end.** Four reachable couples against a batch floor of three means Batch 75 opens at three, closes at four, and the phase is done. `R-26` forbids padding, so the closing batch will simply finish what is there and record it.

**Unit 3 was a repair as much as a rewrite.** Blackened Angel's `### Log and Method` carried a fragment of lowercase, unpunctuated prose welded into the middle of its 30-second row — `forged during a collector named kangmin, who held debts over half a district…` — which was the entity's own origin, told badly, in the wrong place. It was rebuilt as proper sentences about Kangmin, the Collector who came nightly to wish ill on his debtors, and the angel that could not refuse him. The overlap with Relic Waiting for Its Maker went with it.

**Unit 5 was the smallest unit yet: two table cells, fourteen words.** Dead Air's whole problem with Allhallow was one trigger cell — `When the Sorrow Gauge reaches 65%.` — and one effect cell. Both were rewritten in the file's own terms and the couple cleared on the first drafting pass. It is the second unit in a row to clear in one pass (after Calling Bloom in batch 73), and the pattern in both is the same: **the smaller the shared surface, the faster it falls.**

**The structural labels keep being the hardest thing to differ from.** Three of this batch's five units collided on a bold label plus the word that follows it — `**When the entity activates:**`, `**At first contact:**`, `**Interaction method:**`. Those labels cannot be renamed (`label_lint` R4 holds them to a closed vocabulary), so the whole burden falls on the first three words after the colon. `it` and `the` are the two words every other dossier reaches for; any concrete noun will do instead.

**Unit 4 collided with this archive's own Burning Root (batch 72).** Both files needed an interaction-method paragraph, and the first draft of The Hollow Choir's reached for “take each party on its own across a run of cycles” — the exact shape written for Burning Root three batches earlier. The fix was to give each file its own nouns: Burning Root measures heat and rooting; The Hollow Choir measures voices inside a sealed acoustic boundary.

**Rollback #108 struck at the turn boundary** — local HEAD at `408797c`, 282 modified files showing, remote at `aba795b`. `git fetch` + `git reset --mixed FETCH_HEAD` levelled it in one step; nothing force-pushed, nothing lost. Eight rollbacks in a row recovered this way.

| # | Dossier | Structure | Fixed in place | Couples | Words (before → after) |
|---|---|---|---|---|---|
| 1 | [Cleaved](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-775_Cleaved_%EC%B0%A2%EC%96%B4%EC%A7%84_%ED%83%91.md "SE-C-IIβ-775_Cleaved_찢어진_탑.md") | Subject SE | three `### Consequences` bullets | **1** | 7,076 → 7,159 (+83) |
| 2 | [The_Kind_Healer](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-I%CE%B1-071_The_Kind_Healer_%EC%B9%9C%EC%A0%88%ED%95%9C_%EC%B9%98%EC%9C%A0%EC%9E%90.md "SE-C-Iα-071_The_Kind_Healer_친절한_치유자.md") | Subject SE | the four flavour-text blocks | **1** | 7,374 → 7,398 (+24) |
| 3 | [Blackened_Angel](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B3-946_Blackened_Angel_%EA%B2%80%EC%96%B4%EC%A7%84_%EC%B2%9C%EC%82%AC.md "SE-C-IVγ-946_Blackened_Angel_검어진_천사.md") | O-Relic SE — Offertorium | three `### Log and Method` cells, and the broken lower-case fragment in the 30-second row | **1** | 9,923 → 9,953 (+30) |
| 4 | [The_Hollow_Choir](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-021_The_Hollow_Choir_%EB%B9%88_%ED%95%A9%EC%B0%BD%EB%8B%A8.md "SE-C-IIIγ-021_The_Hollow_Choir_빈_합창단.md") | Subject SE | the interaction method and the paragraph before it | **1** | 7,869 → 7,914 (+45) |
| 5 | [Dead_Air](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-III%CE%B3-929_Dead_Air_%EC%9C%A0%EB%A0%B9%EC%9D%98_%EC%95%95%EB%A0%A5.md "SE-N-IIIγ-929_Dead_Air_유령의_압력.md") | Non-Subject SE | two `### Combat Actions` cells | **1** | 4,785 → 4,799 (+14) |

- `C-IIβ-775` Cleaved — `d707810` — PUSH VERIFIED — 1 couple cleared — [[SE-C-IIβ-775_Cleaved_찢어진_탑](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-775_Cleaved_%EC%B0%A2%EC%96%B4%EC%A7%84_%ED%83%91.md "SE-C-IIβ-775_Cleaved_찢어진_탑.md")]
- `C-Iα-071` The Kind Healer — `b0bff9d` — PUSH VERIFIED — 1 couple cleared — [[SE-C-Iα-071_The_Kind_Healer_친절한_치유자](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-I%CE%B1-071_The_Kind_Healer_%EC%B9%9C%EC%A0%88%ED%95%9C_%EC%B9%98%EC%9C%A0%EC%9E%90.md "SE-C-Iα-071_The_Kind_Healer_친절한_치유자.md")]
- `C-IVγ-946` Blackened Angel — `cdff7d4` — PUSH VERIFIED — 1 couple cleared — [[SE-C-IVγ-946_Blackened_Angel_검어진_천사](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B3-946_Blackened_Angel_%EA%B2%80%EC%96%B4%EC%A7%84_%EC%B2%9C%EC%82%AC.md "SE-C-IVγ-946_Blackened_Angel_검어진_천사.md")]
- `C-IIIγ-021` The Hollow Choir — `8f62c48` — PUSH VERIFIED — 1 couple cleared — [[SE-C-IIIγ-021_The_Hollow_Choir_빈_합창단](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-021_The_Hollow_Choir_%EB%B9%88_%ED%95%A9%EC%B0%BD%EB%8B%A8.md "SE-C-IIIγ-021_The_Hollow_Choir_빈_합창단.md")]
- `N-IIIγ-929` Dead Air — `7f62e01` — PUSH VERIFIED — 1 couple cleared — [[SE-N-IIIγ-929_Dead_Air_유령의_압력](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-III%CE%B3-929_Dead_Air_%EC%9C%A0%EB%A0%B9%EC%9D%98_%EC%95%95%EB%A0%A5.md "SE-N-IIIγ-929_Dead_Air_유령의_압력.md")]


**The section mix is down to four sections.** `### M.A.W. Suit` **2**, and one each on Origin, M.A.W. Use Notes and 감각 묘사 (Flavor Text).

**Next rung: Batch 75 opens at three and is the closing batch of the fix phase.** Four reachable couples remain — Remembrance `C-IIIγ-115` × Labyrinth of Stolen Faces `C-IVγ-180` at 0.50 on Origin · The Happy Mask `C-IIβ-051` × Face Beneath Masks `N-IIβ-689` at 0.50 on M.A.W. Suit · I Alone Crossed `C-IVδ-106` × Memorial Flame Mid-Ceremony `C-IVδ-763` at 0.50 on M.A.W. Suit · Weighting Bird `C-IIIγ-032` × Corrosion Dream `O-IIIγ-915` at 0.50 on 감각 묘사. `R-26` forbids padding to reach a number, so it will close at four and record that. **When it closes, every stage of the program is done except the one couple held by standing decision.**

Disclosures: the turn opened on a rolled-back sandbox at `408797c` and was levelled to `aba795b` with `git fetch` + `git reset --mixed FETCH_HEAD` (rollback **#108**). Word counts are measured against `aba795b`, the base Batch 74 landed on. PR #13 was **not** updated — its body stands at 262,124 / 262,144 B with 20 B of headroom and cannot take a further batch; the full record with links is here and in `CHANGELOG.md`.


**Batch 73 — CLOSED at five; the fix phase continues: couples in the plan fall 15 → 10 / 301, with 5 cleared and none newly measurable, and no file in the wing newly measurable against another.**

Taken on the owner's “p” after Batch 72 closed at five. **The ladder did not ratchet to seven, and that was a decision.** `R-26` climbs 3 > 5 > 7 > 10 on evidence, and two of Batch 72's five units needed four and five rewriting passes before the shared wording was gone. That is not “simple”, so the rung stayed at five. Five were opened and five were finished.

**The wing is down to ten couples on twenty files, and nine of the ten are reachable.** The 0.72 Melting Rope × Forgotten Shadow pair is held by standing decision and is not worked. Everything else sits between 0.50 and 0.53 — a spread of three hundredths — so worst-first and any-first remain the same ordering, and the tier table still cannot choose between them.

**One unit cleared on the first drafting pass.** Calling Bloom's entire problem was a single ability line — one sentence, eight shared word-runs, all of them in the same clause. It is the smallest unit of this phase so far and the only one that needed no rework. The lesson is that the size of the fix has nothing to do with the size of the file: 7,302 words rode on one sentence.

**Unit 4 met the three stock stat rows a fourth time, and this time the yield row had already been half-fixed.** `**Han-Energy yield**` in Relic of a Thousand Owners had been patched before — `20–28 per successful work cycle, counted from the form records rather than from the figure` — and still carried the same runs as Ember Phoenix, because the patch had changed the tail of the row and not the head. The repair is to move the number out of the leading position: *“Twenty to twenty-eight, earned solely when a cycle runs to its end…”* A row that begins with a figure will always look like every other row that begins with a figure.

**The gauge row was a twin again, for the fourth batch running.** `**Starting Sorrow Gauge**` appeared at L30 and L70 with byte-identical values. Both were rewritten **by line index** before the spec was built, each with its own gloss — the opening figure belongs to the chain of owners, not to the object. `apply.py` matches per line, so a duplicated row can never be handled by one replacement.

**Two units echoed this archive's own recent work.** Stranded Between Two Shores overlapped **Vanity Asleep `N-IIIγ-954` (batch 72)** on “has a history in this” and “in the small hours”, and Relic of a Thousand Owners overlapped **Floating Pillar `N-IIIγ-409` (batch 71)** on “only on a cycle that”. Every spec is checked against all 301 files, but the files most likely to collide are the ones rewritten last month.

**Rollback #107 struck at the turn boundary.** Local HEAD was `408797c` with 282 modified files showing while the remote stood at `9c9aa4b`. `git fetch` + `git reset --mixed FETCH_HEAD` levelled it in one step and the batch ran clean; nothing was force-pushed and no work was discarded. This is now the standard opening move of a turn, not an incident.

| # | Dossier | Structure | Fixed in place | Couples | Words (before → after) |
|---|---|---|---|---|---|
| 1 | [Stranded_Between_Two_Shores](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-823_Stranded_Between_Two_Shores_%EA%B0%80%EB%9D%BC%EC%95%89%EC%9D%80_%EB%8B%A4%EB%A6%AC.md "SE-C-IVδ-823_Stranded_Between_Two_Shores_가라앉은_다리.md") | Subject SE | the four flavour-text blocks | **1** | 7,383 → 7,403 (+20) |
| 2 | [Calling_Bloom](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-III%CE%B2-944_Calling_Bloom_%EB%B6%80%EB%A5%B4%EB%8A%94_%EA%BD%83.md "SE-O-IIIβ-944_Calling_Bloom_부르는_꽃.md") | Subject SE | the Petal Mantle's ability line | **1** | 7,302 → 7,324 (+22) |
| 3 | [Every_Last_Goodbye](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-230_Every_Last_Goodbye_%EB%A7%88%EC%A7%80%EB%A7%89_%EA%B8%B0%EC%96%B5.md "SE-C-IVδ-230_Every_Last_Goodbye_마지막_기억.md") | Subject SE | the containment-priority and gauge rows of `### Escalation Notes` | **1** | 8,610 → 8,634 (+24) |
| 4 | [Relic_of_a_Thousand_Owners](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-IV%CE%B4-792_Relic_of_a_Thousand_Owners_%ED%9D%90%EB%A5%B4%EB%8A%94_%EC%9C%A0%EB%AC%BC.md "SE-O-IVδ-792_Relic_of_a_Thousand_Owners_흐르는_유물.md") | Subject SE | the three stock stat rows, the gauge row in both tables | **1** | 8,556 → 8,630 (+74) |
| 5 | [Dreaming_Ruin](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-III%CE%B3-505_Dreaming_Ruin_%EB%8F%8C%EC%95%84%EC%98%A8_%EC%9E%94%ED%95%B4.md "SE-N-IIIγ-505_Dreaming_Ruin_돌아온_잔해.md") | Subject SE | the `### M.A.W. Use Notes` paragraph | **1** | 7,361 → 7,374 (+13) |

- `C-IVδ-823` Stranded Between Two Shores — `ff173bb` — PUSH VERIFIED — 1 couple cleared — [[SE-C-IVδ-823_Stranded_Between_Two_Shores_가라앉은_다리](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-823_Stranded_Between_Two_Shores_%EA%B0%80%EB%9D%BC%EC%95%89%EC%9D%80_%EB%8B%A4%EB%A6%AC.md "SE-C-IVδ-823_Stranded_Between_Two_Shores_가라앉은_다리.md")]
- `O-IIIβ-944` Calling Bloom — `012541c` — PUSH VERIFIED — 1 couple cleared — [[SE-O-IIIβ-944_Calling_Bloom_부르는_꽃](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-III%CE%B2-944_Calling_Bloom_%EB%B6%80%EB%A5%B4%EB%8A%94_%EA%BD%83.md "SE-O-IIIβ-944_Calling_Bloom_부르는_꽃.md")]
- `C-IVδ-230` Every Last Goodbye — `1c57a25` — PUSH VERIFIED — 1 couple cleared — [[SE-C-IVδ-230_Every_Last_Goodbye_마지막_기억](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-230_Every_Last_Goodbye_%EB%A7%88%EC%A7%80%EB%A7%89_%EA%B8%B0%EC%96%B5.md "SE-C-IVδ-230_Every_Last_Goodbye_마지막_기억.md")]
- `O-IVδ-792` Relic of a Thousand Owners — `382c4a5` — PUSH VERIFIED — 1 couple cleared — [[SE-O-IVδ-792_Relic_of_a_Thousand_Owners_흐르는_유물](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-IV%CE%B4-792_Relic_of_a_Thousand_Owners_%ED%9D%90%EB%A5%B4%EB%8A%94_%EC%9C%A0%EB%AC%BC.md "SE-O-IVδ-792_Relic_of_a_Thousand_Owners_흐르는_유물.md")]
- `N-IIIγ-505` Dreaming Ruin — `dc29a4e` — PUSH VERIFIED — 1 couple cleared — [[SE-N-IIIγ-505_Dreaming_Ruin_돌아온_잔해](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-III%CE%B3-505_Dreaming_Ruin_%EB%8F%8C%EC%95%84%EC%98%A8_%EC%9E%94%ED%95%B4.md "SE-N-IIIγ-505_Dreaming_Ruin_돌아온_잔해.md")]


**The section mix is flat and thinning.** `### M.A.W. Suit` **2** · 감각 묘사 (Flavor Text) **2**, and one each across Combat Actions, Consequences, Origin, M.A.W. Use Notes, Interaction Pattern and Log and Method.

**Next rung: Batch 74 opens at five**, or at seven if the owner judges these five simple — three cleared in three passes or fewer, one in a single pass, and only unit 5 needed five. Remaining candidates, all single-couple files: Rem `C-IIβ-135` × Cleaved `C-IIβ-775` at 0.53 on Consequences · The Lonely Giant `C-IIIγ-105` × The Kind Healer `C-Iα-071` at 0.53 on 감각 묘사 · Blackened Angel `C-IVγ-946` × Relic Waiting for Its Maker `O-IIIγ-651` at 0.52 on Log and Method · The Hollow Choir `C-IIIγ-021` × Broken Promise `N-IIIγ-160` at 0.52 on Interaction Pattern · Dead Air `N-IIIγ-929` × Allhallow `O-IIIγ-916` at 0.50 on Combat Actions.

Disclosures: the turn opened on a rolled-back sandbox at `408797c` and was levelled to `9c9aa4b` with `git fetch` + `git reset --mixed FETCH_HEAD` (rollback **#107**). Word counts are measured against `9c9aa4b`, the base Batch 73 landed on. PR #13 was **not** updated — its body stands at 262,124 / 262,144 B with 20 B of headroom and cannot take a further batch; the full record with links is here and in `CHANGELOG.md`. At 1.0 couple cleared per unit, the nine reachable couples are ≈ **9 units**.


**Batch 72 — CLOSED at five; the fix phase continues: couples in the plan fall 20 → 15 / 301, with 5 cleared and none newly measurable, and no file in the wing newly measurable against another.**

Taken on the owner's “p” after Batch 71 closed at three; the ladder ratcheted 3 → 5. Same shape as the batches before it: one file per unit, the **lighter** side of each pair rewritten in its own terms, every unit pushed and verified inside the turn.

**No file in the wing carries two couples any more.** Batch 71 ended with Forgotten Shadow `N-IIβ-453` holding the last two-couple file; unit 5 cleared its reachable side and the wing is now fifteen isolated pairs, each with a single file on each end. The heavy-side pick that drove batches 70 and 71 has nothing left to bite on, and from here the arithmetic is exactly one unit per couple.

**Everything left except the frozen 0.72 sits in 0.50–0.54.** The spread across fourteen of the fifteen is four hundredths. Worst-first ordering and any-first ordering are now the same ordering, and the tier table has stopped being a useful way to choose.

**The ladder ratcheted on evidence, not on optimism.** Batch 71's three units each needed three or four rewriting passes before the shared wording was gone, so they were not “simple” in `R-26`'s sense; they were nonetheless all finished properly, and the record at `d756e73` named five as the next rung. Five were opened and five were finished.

**Unit 3 met the oldest trap in the kit and it still cost a pass.** The Echoing Zweihander's description spans two paragraphs, and `apply.py` matches **per line** — a replacement carrying a blank line inside it can never match. The spec was rebuilt as two single-line replacements and applied first time. The rule is unchanged: one replacement per line, always.

**Unit 4 showed how far the schema lists reach.** “a breach, an expansion, a transformation, an anomaly or a Sorrow Tide” and “the gauge, the seal, the personnel exposure log” are not boilerplate — they are real content — but they are the same content in a dozen dossiers, and they alone put the first draft into **46 files**. Reordering a list and splitting it with dashes is enough to break the run without losing a single item.

**Unit 2 echoed work done one batch earlier.** Burning Root's draft overlapped Weeping Willow `C-IIIγ-140`, rewritten in batch 71, on “on its own for several cycles”. A batch does not start from a clean slate: the previous batch's prose is now part of the corpus the next one has to differ from.

**The turn opened on a rollback and lost nothing.** Local HEAD had fallen back to `408797c` with 279 modified files showing, while the remote stood at `d756e73`. `git fetch` + `git reset --mixed FETCH_HEAD` levelled it in one step — that moves HEAD and the index and never touches the working tree — and the batch then ran clean. Never `git pull`, never force-push. Rollback **#106**.

| # | Dossier | Structure | Fixed in place | Couples | Words (before → after) |
|---|---|---|---|---|---|
| 1 | [Vanity_Asleep](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-III%CE%B3-954_Vanity_Asleep_%EC%9E%A0%EB%93%A0_%EA%B1%B0%EC%9A%B8.md "SE-N-IIIγ-954_Vanity_Asleep_잠든_거울.md") | Subject SE | the four flavour-text blocks | **1** | 7,060 → 7,094 (+34) |
| 2 | [Burning_Root](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-558_Burning_Root_%ED%83%80%EC%98%A4%EB%A5%B4%EB%8A%94_%EB%BF%8C%EB%A6%AC.md "SE-C-IIIγ-558_Burning_Root_타오르는_뿌리.md") | Subject SE | the interaction method and the paragraph that introduces it | **1** | 7,051 → 7,109 (+58) |
| 3 | [Heirloom](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-IV%CE%B4-909_Heirloom_%EC%8A%A4%EB%A9%B0%EB%93%A0_%EB%A9%94%EC%95%84%EB%A6%AC.md "SE-O-IVδ-909_Heirloom_스며든_메아리.md") | Non-Subject SE | the Echoing Zweihander's appearance and the note on how it is wielded | **1** | 7,221 → 7,257 (+36) |
| 4 | [Shard_of_a_Broken_Promise](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-IV%CE%B4-851_Shard_of_a_Broken_Promise_%EB%B6%80%EC%84%9C%EC%A7%84_%EC%A1%B0%EA%B0%81.md "SE-O-IVδ-851_Shard_of_a_Broken_Promise_부서진_조각.md") | I-Relic SE — Indumentum | both `### Registry Addendum` paragraphs | **1** | 7,391 → 7,449 (+58) |
| 5 | [Floating_Fragment](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-I%CE%B1-453_Floating_Fragment_%EB%96%A0%EB%8B%A4%EB%8B%88%EB%8A%94_%ED%8C%8C%ED%8E%B8.md "SE-O-Iα-453_Floating_Fragment_떠다니는_파편.md") | Subject SE | the Crying Shroud sabre's appearance and the note on how it cuts | **1** | 5,909 → 5,924 (+15) |

- `N-IIIγ-954` Vanity Asleep — `31f4e4d` — PUSH VERIFIED — 1 couple cleared — [[SE-N-IIIγ-954_Vanity_Asleep_잠든_거울](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-III%CE%B3-954_Vanity_Asleep_%EC%9E%A0%EB%93%A0_%EA%B1%B0%EC%9A%B8.md "SE-N-IIIγ-954_Vanity_Asleep_잠든_거울.md")]
- `C-IIIγ-558` Burning Root — `ddb4061` — PUSH VERIFIED — 1 couple cleared — [[SE-C-IIIγ-558_Burning_Root_타오르는_뿌리](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-558_Burning_Root_%ED%83%80%EC%98%A4%EB%A5%B4%EB%8A%94_%EB%BF%8C%EB%A6%AC.md "SE-C-IIIγ-558_Burning_Root_타오르는_뿌리.md")]
- `O-IVδ-909` Heirloom — `801b2d8` — PUSH VERIFIED — 1 couple cleared — [[SE-O-IVδ-909_Heirloom_스며든_메아리](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-IV%CE%B4-909_Heirloom_%EC%8A%A4%EB%A9%B0%EB%93%A0_%EB%A9%94%EC%95%84%EB%A6%AC.md "SE-O-IVδ-909_Heirloom_스며든_메아리.md")]
- `O-IVδ-851` Shard of a Broken Promise — `685e594` — PUSH VERIFIED — 1 couple cleared — [[SE-O-IVδ-851_Shard_of_a_Broken_Promise_부서진_조각](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-IV%CE%B4-851_Shard_of_a_Broken_Promise_%EB%B6%80%EC%84%9C%EC%A7%84_%EC%A1%B0%EA%B0%81.md "SE-O-IVδ-851_Shard_of_a_Broken_Promise_부서진_조각.md")]
- `O-Iα-453` Floating Fragment — `a2ba3d5` — PUSH VERIFIED — 1 couple cleared — [[SE-O-Iα-453_Floating_Fragment_떠다니는_파편](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-I%CE%B1-453_Floating_Fragment_%EB%96%A0%EB%8B%A4%EB%8B%88%EB%8A%94_%ED%8C%8C%ED%8E%B8.md "SE-O-Iα-453_Floating_Fragment_떠다니는_파편.md")]


**The section mix is now flat.** `### M.A.W. Suit` **3** · 감각 묘사 (Flavor Text) **3** · `### M.A.W. Use Notes` **2**, and one each across Operational Parameters, Combat Actions, Consequences, Origin, Escalation Notes, Interaction Pattern and Log and Method.

**Next rung: Batch 73 opens at seven**, per the ladder (3 > 5 > 7 > 10), if these five are judged simple — three of them cleared on two passes or fewer, but units 2 and 4 needed four and five. Worst-first candidates, all now single-couple files: Rising Wall `C-IVδ-255` × Stranded Between Two Shores `C-IVδ-823` at 0.54 on 감각 묘사 · Grieving Love `N-IIIβ-941` × Calling Bloom `O-IIIβ-944` at 0.54 on M.A.W. Suit · Walking Calendar `C-IVδ-220` × Every Last Goodbye `C-IVδ-230` at 0.54 on Escalation Notes · Ember `O-IVδ-190` × Relic of a Thousand Owners `O-IVδ-792` at 0.54 on Operational Parameters · The Rage Statue `C-IIIγ-190` × Dreaming Ruin `N-IIIγ-505` at 0.53 on M.A.W. Use Notes.

Disclosures: the turn opened on a rolled-back sandbox at `408797c` and was levelled to `d756e73` with `git fetch` + `git reset --mixed FETCH_HEAD` (rollback **#106**); nothing was force-pushed and no work was discarded. Word counts are measured against `77d9389`, the base Batch 71 landed on. PR #13 was **not** updated — its body stands at 262,124 / 262,144 B with 20 B of headroom and cannot take a further batch; the full record with links is here and in `CHANGELOG.md`. At 1.0 couple cleared per unit across b72, the remaining fifteen are ≈ **15 units**, of which one (the frozen 0.72) is not reachable.


**Batch 71 — CLOSED at three; the fix phase continues: couples in the plan fall 25 → 20 / 301, with 5 cleared and none newly measurable, and no file in the wing newly measurable against another.**

Taken on the owner's "p" after Batch 70 closed at five; the ladder's next rung after five is three, and the owner's absolute floor is three. Same shape as the batches before it: one file per unit, the file's own lines rewritten in its own terms, every unit pushed and verified inside the turn.

**The plan was beaten by three.** Batch 71 was planned at 25 → 23 and landed at **25 → 20**. The two files carrying two couples each — Weeping Willow and Floating Pillar — cleared both, and the unit that was meant to be the last word on the batch, The Hollow Knight, cleared the 0.63 pair as well.

**The 0.60–0.69 tier is now empty.** Batch 70 left exactly one couple in it; unit 3 cleared it. What remains is the frozen 0.72 (Melting Rope × Forgotten Shadow, held by standing decision) and nineteen couples in 0.50–0.59. **The entire remaining backlog now sits inside the band the fix phase was written for.**

**Only one file in the wing carries two couples now** — Forgotten Shadow `N-IIβ-453` — and one of its two is the frozen 0.72, so only one of them is reachable. Every other couple is a one-couple file on both sides, which is why the yield per unit has settled at one and the arithmetic from here is one unit per couple.

**The same three stock stat rows surfaced twice again, and they are always twins.** Units 1 and 2 both met `**Starting Sorrow Gauge**` · `**Han-Energy yield**` · `**Han Dust Drop (Vessel Destruction)**`. In both files the gauge row appears **twice** — once in `## Operational Parameters` (≈L30) and once in `### Core Stat Line` (≈L71). `apply.py` matches per line, so both copies have to be rewritten **by index** before a spec can be built, and each copy gets its own gloss rather than the same sentence repeated.

**Echo is dominated by what the file already said, not by what you add.** Unit 2's first draft scored **161 echoes across 45 files**, and the two worst offenders were phrases the rewrite had *kept* — "which is the only pressure this holding makes" (≈20 dossiers) and "the wearer's own account of themselves" (≈10). The fix is never to soften the new sentence; it is to find the kept phrase doing the damage.

**A phrase can be stock without being on any residue list.** "cold to the touch" is not in `tools/verify.py`'s `STOCK`, passes `wikistd`, `sectfile` and `tpl` clean, and was already in eleven dossiers. `precheck_all.py` is the only thing that can see this, which is why it runs on every spec before anything is applied.

**The rollback struck mid-batch again.** Unit 1 was committed locally on a rolled-back base (`408797c`) and the push was rejected with `! [rejected] … (fetch first)`. Recovered with `git fetch` + `git reset --mixed FETCH_HEAD`, which moves HEAD and the index and never touches the worktree — the edit was still there afterwards and needed only re-committing. Never `git pull`, never force-push. Rollback **#105**.

| # | Dossier | Structure | Fixed in place | Couples | Words (before → after) |
|---|---|---|---|---|---|
| 1 | [Weeping_Willow](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-140_Weeping_Willow_%EC%9A%B0%EB%8A%94_%EB%B2%84%EB%93%9C%EB%82%98%EB%AC%B4.md "SE-C-IIIγ-140_Weeping_Willow_우는_버드나무.md") | Non-Subject SE | the three stock stat rows in both tables, the Resistance row, and the `**Interaction method**` paragraph | **2** | 7,361 → 7,541 (+180) |
| 2 | [Floating_Pillar](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-III%CE%B3-409_Floating_Pillar_%EB%96%A0%EB%8B%A4%EB%8B%88%EB%8A%94_%EA%B8%B0%EB%91%A5.md "SE-N-IIIγ-409_Floating_Pillar_떠다니는_기둥.md") | Subject SE | the three stock stat rows (both copies of the gauge row) and the Empty Veil's appearance, ability and cost | **2** | 7,556 → 7,691 (+135) |
| 3 | [The_Hollow_Knight](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B3-073_The_Hollow_Knight_%EB%B9%88_%EA%B8%B0%EC%82%AC.md "SE-C-IVγ-073_The_Hollow_Knight_빈_기사.md") | Subject SE | the Duty Plate's appearance and ability | **1** | 8,042 → 8,064 (+22) |

- `C-IIIγ-140` Weeping Willow — `d129938` — PUSH VERIFIED — 2 couples cleared — [[SE-C-IIIγ-140_Weeping_Willow_우는_버드나무](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-140_Weeping_Willow_%EC%9A%B0%EB%8A%94_%EB%B2%84%EB%93%9C%EB%82%98%EB%AC%B4.md "SE-C-IIIγ-140_Weeping_Willow_우는_버드나무.md")]
- `N-IIIγ-409` Floating Pillar — `e9ac783` — PUSH VERIFIED — 2 couples cleared — [[SE-N-IIIγ-409_Floating_Pillar_떠다니는_기둥](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-III%CE%B3-409_Floating_Pillar_%EB%96%A0%EB%8B%A4%EB%8B%88%EB%8A%94_%EA%B8%B0%EB%91%A5.md "SE-N-IIIγ-409_Floating_Pillar_떠다니는_기둥.md")]
- `C-IVγ-073` The Hollow Knight — `07c8e11` — PUSH VERIFIED — 1 couples cleared — [[SE-C-IVγ-073_The_Hollow_Knight_빈_기사](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B3-073_The_Hollow_Knight_%EB%B9%88_%EA%B8%B0%EC%82%AC.md "SE-C-IVγ-073_The_Hollow_Knight_빈_기사.md")]

**The section mix holds, and it is flatter than it was.** `### M.A.W. Suit` is still the worst section at **4**, level with 감각 묘사 (Flavor Text) at **4**; then `### M.A.W. Use Notes` 2 · `### Interaction Pattern` 2 · and one each across Operational Parameters, Combat Actions, Consequences, Origin, Escalation Notes, M.A.W. Weapon, Registry Addendum and Log and Method.

**Next rung: Batch 72 opens at five**, per the ladder (three → five → seven → ten). Worst-first candidates — Vanity Asleep `N-IIIγ-954` × The Wrath Flame `O-IIIβ-120` at 0.58 on 감각 묘사 · Owed `C-IIIγ-180` × Burning Root `C-IIIγ-558` at 0.57 on Interaction Pattern · Labyrinth of the Unfinished `C-IVδ-909` × Heirloom `O-IVδ-909` at 0.56 on M.A.W. Weapon · Shard of a Broken Promise `O-IVδ-851` × Fallow `O-Iα-554` at 0.55 on Registry Addendum · Forgotten Shadow `N-IIβ-453` × Floating Fragment `O-Iα-453` at 0.55 on M.A.W. Suit. **All nineteen remaining couples except the frozen 0.72 are now in 0.50–0.59, so worst-first and any-first are the same ordering from here.**

Disclosures: the turn opened on a rolled-back sandbox at `408797c` and was levelled to `77d9389` with `git fetch` + `git reset --mixed FETCH_HEAD` (rollback **#105**); nothing was force-pushed and no work was discarded. PR #13 was **not** updated this turn — its body stands at 262,124 / 262,144 B with 20 B of headroom and cannot take a further batch; the full b71 record with links is here and in `CHANGELOG.md`. At 1.40 couples cleared per unit across b71, the remaining twenty are ≈ **14 units**.



**Batch 70 — CLOSED at five; the fix phase continues: couples in the plan fall 32 → 25 / 301, with 7 cleared and none newly measurable, and no file in the wing now carries three couples.**

Taken on the owner's "p", after Batch 69 closed at three; the owner elected five. Same shape as the batches before it: one file per unit, the lighter side's small overlaps edited line by line in the file's own terms, never block-replaced, growth only (`R-15`). Five files worked and **seven couples cleared**, because two of the units cleared two each.

**The heavy-side rule paid twice more, and it is now the default read.** Dejà Vu `C-IVδ-125` was the heavy side of 0.57 against Dawn of Mourning and 0.55 against Barrier of Nothing, in two different sections; one unit rewrote both and cleared both. Harvest Beyond the Gate `N-IIβ-627` was the heavy side of 0.56 against Echo of Kindness and of 0.53 against Torn Flower, again in two sections; one unit cleared both. **When a file carries two couples it is worth checking whether it is the heavy side of both before spending two units on it.**

**The same three stock stat rows keep surfacing, and they are always twins.** Units 2 and 4 both ran into `**Starting Sorrow Gauge**` · `**Han-Energy yield**` · `**Han Dust Drop (Vessel Destruction)**`. In both files the row appears **twice, byte-identical** — once under `## Operational Parameters` and once under `### Core Stat Line`. `apply.py` matches **per line** and aborts on a non-unique `sub`, and a multi-line `sub` can never match at all, because the occurrence count is taken line by line. **The working pattern is: rewrite the Core Stat Line twin first, by direct line index, which makes the Operational Parameters copy unique; then let `apply.py` do the rest.** Both units needed the twin rewritten anyway — the gram is shared through both copies, so fixing one alone would not have cleared the couple.

**Self-echo now reaches across units inside one batch.** Unit 4 reached for the label unit 2 had coined an hour earlier — `Han-Energy per completed cycle` — and scored **4** against Harvest, the file unit 2 had just rewritten. Renamed to `Han-Energy booked per cycle` and the worst run fell to **1**. **Invent a fresh label per file. Do not reuse a phrase you coined earlier in the same batch, however well it reads.** The partner check stays at 0 in both cases; only the all-301 check catches this.

**The dossier label vocabulary is closed, and `unit_np.sh` does not check it.** Units 2 and 4 renamed the stock stat rows to break the shared grams — `**Starting Sorrow Gauge**` became *Gauge when a watch opens*, `**Han-Energy yield**` became *Han-Energy per completed cycle*, `**Han Dust Drop (Vessel Destruction)**` became *Han Dust recovered on destruction*. Both units passed every gate in `unit_np.sh` and were pushed. `gate.sh` then refused the docs commit with **8 × `LABEL_NOT_ALLOWED`**: `tools/label_lint.py` rule R4 holds those labels to a fixed vocabulary and no open-ended fallback. **The repair is to keep the label and move the value** — put prose ahead of the figures, so `| **Han-Energy yield** | Paid only for a cycle that finishes — 12–18 …` breaks the `han energy yield ~ ~` gram without touching the label. Both couples stayed cleared afterwards, which confirms the overlap was in the **value**, not the label. Corrected in `8bb74bf` and `05a9abd`. **From this turn: never rename a `**bold**` table row label; change what it says, not what it is called.**

**The record was split this turn.** `WORK_IN_PROGRESS.md` went 718,945 → **171,764 B** and `CHANGELOG.md` 755,141 → **87,006 B**, both into numbered volumes, both verified lossless line-by-line against `7b804e7`. This block is the first written into the split record.

| # | Dossier | Structure | Fixed in place | Couples | Words (before → after) |
|---|---|---|---|---|---|
| 1 | [Dejà_Vu](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-125_Dej%C3%A0_Vu_%EB%8F%8C%EC%95%84%EC%98%A8_%EC%97%B4%EB%A7%A4.md "SE-C-IVδ-125_Dejà_Vu_돌아온_열매.md") | Subject SE | the `**Interaction method**` paragraph and three `### Consequences` bullets | **2** | 8,657 → 8,740 (+83) |
| 2 | [Harvest_Beyond_the_Gate](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-II%CE%B2-627_Harvest_Beyond_the_Gate_%EB%85%B9%EC%95%84%EB%82%B4%EB%A6%B0_%EC%97%B4%EB%A7%A4.md "SE-N-IIβ-627_Harvest_Beyond_the_Gate_녹아내린_열매.md") | Non-Subject SE | the three stock stat rows (both copies) and the `### Registry Addendum` review requirement | **2** | 7,454 → 7,551 (+97) |
| 3 | [Conservatory](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-IV%CE%B4-852_Conservatory_%EC%9E%8A%ED%98%80%EC%A7%84_%EC%9E%94%ED%95%B4.md "SE-N-IVδ-852_Conservatory_잊혀진_잔해.md") | I-Relic SE | the whole `### Log and Method` table, four rows | **1** | 9,460 → 9,589 (+129) |
| 4 | [Doorway_to_Nowhere](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-II%CE%B2-152_Doorway_to_Nowhere_%EB%96%A0%EB%8F%84%EB%8A%94_%EB%AC%B8.md "SE-N-IIβ-152_Doorway_to_Nowhere_떠도는_문.md") | Subject SE | the three stock stat rows (both copies) | **1** | 8,564 → 8,646 (+82) |
| 5 | [Backward_Hour](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-913_Backward_Hour_%EC%B9%B4%EC%9A%B4%ED%8A%B8%EB%8B%A4%EC%9A%B4_%EC%8B%9C%EA%B3%84.md "SE-C-IIIγ-913_Backward_Hour_카운트다운_시계.md") | Non-Subject SE | the `### M.A.W. Use Notes` paragraph | **1** | 6,063 → 6,124 (+61) |

- `C-IVδ-125` Dejà Vu — `5009734` — PUSH VERIFIED — 2 couples cleared — [[SE-C-IVδ-125_Dejà_Vu_돌아온_열매](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-125_Dej%C3%A0_Vu_%EB%8F%8C%EC%95%84%EC%98%A8_%EC%97%B4%EB%A7%A4.md "SE-C-IVδ-125_Dejà_Vu_돌아온_열매.md")]
- `N-IIβ-627` Harvest Beyond the Gate — `262b847` — PUSH VERIFIED — 2 couples cleared — [[SE-N-IIβ-627_Harvest_Beyond_the_Gate_녹아내린_열매](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-II%CE%B2-627_Harvest_Beyond_the_Gate_%EB%85%B9%EC%95%84%EB%82%B4%EB%A6%B0_%EC%97%B4%EB%A7%A4.md "SE-N-IIβ-627_Harvest_Beyond_the_Gate_녹아내린_열매.md")]
- `N-IVδ-852` Conservatory — `aabc2d3` — PUSH VERIFIED — 1 couples cleared — [[SE-N-IVδ-852_Conservatory_잊혀진_잔해](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-IV%CE%B4-852_Conservatory_%EC%9E%8A%ED%98%80%EC%A7%84_%EC%9E%94%ED%95%B4.md "SE-N-IVδ-852_Conservatory_잊혀진_잔해.md")]
- `N-IIβ-152` Doorway to Nowhere — `24f75e0` — PUSH VERIFIED — 1 couples cleared — [[SE-N-IIβ-152_Doorway_to_Nowhere_떠도는_문](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-II%CE%B2-152_Doorway_to_Nowhere_%EB%96%A0%EB%8F%84%EB%8A%94_%EB%AC%B8.md "SE-N-IIβ-152_Doorway_to_Nowhere_떠도는_문.md")]
- `C-IIIγ-913` Backward Hour — `616a307` — PUSH VERIFIED — 1 couples cleared — [[SE-C-IIIγ-913_Backward_Hour_카운트다운_시계](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-913_Backward_Hour_%EC%B9%B4%EC%9A%B4%ED%8A%B8%EB%8B%A4%EC%9A%B4_%EC%8B%9C%EA%B3%84.md "SE-C-IIIγ-913_Backward_Hour_카운트다운_시계.md")]

| Counter | Open | Close |
|---|---|---|
| Couples in the plan (≥ 0.50 on either side) | 32 / 301 | **25 / 301** |
| Couples cleared this batch | — | **7** |
| Couples newly measurable | — | **0** |
| Files carrying a couple | 57 / 301 | **45 / 301** |
| Section-pairs over 0.50 | 32 | 25 |
| Couples ≥ 0.70 | 1 / 32 | 1 / 25 |
| Couples 0.60–0.69 | 4 / 32 | 1 / 25 |
| Couples 0.50–0.59 | 27 / 32 | 23 / 25 |
| Files carrying three or more couples | 0 / 301 | **0 / 301** |
| Files carrying two couples | 7 / 301 | **5 / 301** |
| Carrying — Subject SE | — | 28 / 142 |
| Carrying — Non-Subject SE | — | 8 / 71 |
| Carrying — I-Relic SE | — | 6 / 53 |
| Carrying — O-Relic SE | — | 3 / 28 |
| Carrying — A-Relic SE | — | 0 / 7 |
| Carrying — structure unreadable | — | 0 / 301 |
| Files carrying a whole copied section | 0 / 301 | 0 / 301 |
| Stock-line residue (`verify.py`) | 0 / 301 | 0 / 301 |
| `R-29`, all five clauses | 301 / 301 | 301 / 301 |
| Personalization queue | 0 / 301 | 0 / 301 |
| Duplicate quote families | 0 / 301 | 0 / 301 |
| Words (the five files) | 40,198 | 40,650 (+452) |

**Where the remainder sits.** No file carries three couples and five carry two: Hollow Choir `C-IIIγ-021` · Weeping Willow `C-IIIγ-140` · Broken Promise `N-IIIγ-160` · Floating Pillar `N-IIIγ-409` · Forgotten Shadow `N-IIβ-453`. The worst tie in the wing is still **Melting Rope `N-IIIγ-447` × Forgotten Shadow `N-IIβ-453`, 0.72 in M.A.W. Use Notes — frozen, skipped by standing decision.** Behind it: Hollow Knight `C-IVγ-073` × Smothering Mother `N-IVδ-005` 0.63 (M.A.W. Suit) · Vanity Asleep `N-IIIγ-954` × Wrath Flame `O-IIIβ-120` 0.58 (감각 묘사) · Owed `C-IIIγ-180` × Burning Root `C-IIIγ-558` 0.57 (Interaction Pattern).

**The 0.60–0.69 tier has nearly emptied** — 4 couples down to **1**. What is left is almost entirely in the 0.50–0.59 band (23 of 25), which is the long flat tail: single-section overlaps that each take a unit and clear one couple.

**`### M.A.W. Suit` is still the worst section at 6**, more than double anything else: 감각 묘사 (Flavor Text) 4 · Interaction Pattern 3 · Operational Parameters 2 · M.A.W. Use Notes 2.

**Next rung: Batch 71 opens at three**, per the ladder and the owner's absolute floor. Worst-first candidates — Hollow Knight `C-IVγ-073` (0.63, M.A.W. Suit) · Hollow Choir `C-IIIγ-021` (two couples) · Weeping Willow `C-IIIγ-140` (two couples) · Broken Promise `N-IIIγ-160` (two couples).

Disclosures: the turn opened on a rolled-back sandbox and `syncbranch.py` refused a merge because the worktree held newer content than the index; reconciled by hand with `git fetch` + `git reset --mixed FETCH_HEAD`, which moves HEAD and the index and never touches files (rollback **#104**). Nothing was measured on a stale tree and no work was overwritten. The kit survived the turn boundary at `tools/kit/` — the seventh turn running. Every unit was pushed and verified in the turn it was applied (`A0`). All figures above are measured at `616a307`.


**Batch 69 — CLOSED at three; the fix phase continues: couples in the plan fall 37 → 32 / 301, with 5 cleared and none newly measurable, and no file in the wing now carries three couples.**

Taken on the owner's "p", after Batch 68 closed at ten. The ladder opened at three and the batch closes at three — the owner's absolute floor, and a valid rung. Same shape as the batches before it: one file per unit, the lighter side's small overlaps edited line by line in the file's own terms, never block-replaced, growth only (`R-15`). Three files worked, **five couples cleared** — because two of the three units cleared two each.

**A unit is worth two couples when the file is the heavy side of two ties in the same section.** The Repeated Survivor `N-IVδ-902` read 0.56 against The Debtor and 0.56 against Briar, both in `### Escalation Notes`, with the partners at 0.15 and 0.06 — so the stock was the Survivor's, and one three-bullet rewrite cleared both. The Well of Unfinished Words `N-IIβ-778` read 0.53 against Blackened Angel and 0.51 against Relic Waiting for Its Maker, both in `### Log and Method`, with the partners at 0.38 and 0.49. Rewriting the shared section on the heavy file breaks **both** directions at once, because the direction is measured as *A's distinctive grams found in B*: once B no longer holds the shared text, neither A→B nor B→A survives. **Read both directions before choosing a file — the higher number is the side to edit.**

**The `### Log and Method` table is one row per line, not two cells.** Unit 3's first spec used eight anchors, one per cell; the Log and Method cells share a table line, so two anchors resolved to the same line and `apply.py` reported `sub NOT FOUND` on the second. Rebuilt as one replacement per row, four in total. **When a section is a table, count the lines before writing the spec.**

**Stock phrasing survives into the replacement.** Unit 1's first draft opened a Trivia line with *"It is the only holding in the wing whose…"* — four other dossiers already carry that phrase, and it scored 4 against three of them on the all-301 check while scoring **0** against the actual partner. Reworded to *"Nothing a worker said ever proved it to the file. The tooling did…"* and the worst run dropped to 1. **The partner check is not sufficient; `precheck_all.py` across all 301 is.**

| # | Dossier | Structure | Fixed in place | Couples | Words (before → after) |
|---|---|---|---|---|---|
| 1 | [[SE-C-IVδ-915_Endless_Shift_끝없는_교대.md](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-915_Endless_Shift_%EB%81%9D%EC%97%86%EB%8A%94_%EA%B5%90%EB%8C%80.md)](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-915_Endless_Shift_%EB%81%9D%EC%97%86%EB%8A%94_%EA%B5%90%EB%8C%80.md) | Non-Subject SE | all three `## Trivia` lines | **1** | 6,587 → 6,665 (+78) |
| 2 | [[SE-N-IVδ-902_The_Repeated_Survivor_되풀이의_생존자.md](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Unknown_Entities/SE-N-IV%CE%B4-902_The_Repeated_Survivor_%EB%90%98%ED%92%80%EC%9D%B4%EC%9D%98_%EC%83%9D%EC%A1%B4%EC%9E%90.md)](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Unknown_Entities/SE-N-IV%CE%B4-902_The_Repeated_Survivor_%EB%90%98%ED%92%80%EC%9D%B4%EC%9D%98_%EC%83%9D%EC%A1%B4%EC%9E%90.md) | Subject SE | all three `### Escalation Notes` bullets | **2** | 5,719 → 5,780 (+61) |
| 3 | [[SE-N-IIβ-778_Well_of_Unfinished_Words_솟구친_우물.md](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-II%CE%B2-778_Well_of_Unfinished_Words_%EC%86%9F%EA%B5%AC%EC%B9%9C_%EC%9A%B0%EB%AC%BC.md)](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-II%CE%B2-778_Well_of_Unfinished_Words_%EC%86%9F%EA%B5%AC%EC%B9%9C_%EC%9A%B0%EB%AC%BC.md) | O-Relic SE | the whole `### Log and Method` table, four rows | **2** | 6,996 → 7,020 (+24) |

- `C-IVδ-915` Endless Shift — `f003e42` — PUSH VERIFIED — 1 couples cleared — [[SE-C-IVδ-915_Endless_Shift_끝없는_교대](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-915_Endless_Shift_%EB%81%9D%EC%97%86%EB%8A%94_%EA%B5%90%EB%8C%80.md "SE-C-IVδ-915_Endless_Shift_끝없는_교대.md")]
- `N-IVδ-902` The Repeated Survivor — `fd84f2f` — PUSH VERIFIED — 2 couples cleared — [[SE-N-IVδ-902_The_Repeated_Survivor_되풀이의_생존자](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Unknown_Entities/SE-N-IV%CE%B4-902_The_Repeated_Survivor_%EB%90%98%ED%92%80%EC%9D%B4%EC%9D%98_%EC%83%9D%EC%A1%B4%EC%9E%90.md "SE-N-IVδ-902_The_Repeated_Survivor_되풀이의_생존자.md")]
- `N-IIβ-778` Well of Unfinished Words — `e329731` — PUSH VERIFIED — 2 couples cleared — [[SE-N-IIβ-778_Well_of_Unfinished_Words_솟구친_우물](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-II%CE%B2-778_Well_of_Unfinished_Words_%EC%86%9F%EA%B5%AC%EC%B9%9C_%EC%9A%B0%EB%AC%BC.md "SE-N-IIβ-778_Well_of_Unfinished_Words_솟구친_우물.md")]

| Counter | Open | Close |
|---|---|---|
| Couples in the plan (≥ 0.50 on either side) | 37 / 301 | **32 / 301** |
| Couples cleared this batch | — | **5** |
| Couples newly measurable | — | **0** |
| Files carrying a couple | 63 / 301 | **57 / 301** |
| Section-pairs over 0.50 | 37 | 32 |
| Couples ≥ 0.70 | 2 / 37 | 1 / 32 |
| Couples 0.60–0.69 | 4 / 37 | 4 / 32 |
| Couples 0.50–0.59 | 31 / 37 | 27 / 32 |
| Files carrying three or more couples | 0 / 301 | **0 / 301** |
| Files carrying two couples | 11 / 301 | **7 / 301** |
| Carrying — Subject SE | — | 34 / 142 |
| Carrying — Non-Subject SE | — | 12 / 71 |
| Carrying — I-Relic SE | — | 8 / 53 |
| Carrying — O-Relic SE | — | 3 / 28 |
| Carrying — A-Relic SE | — | 0 / 7 |
| Carrying — structure unreadable | — | 0 / 301 |
| Files carrying a whole copied section | 0 / 301 | 0 / 301 |
| Stock-line residue (`verify.py`) | 0 / 301 | 0 / 301 |
| `R-29`, all five clauses | 301 / 301 | 301 / 301 |
| Personalization queue | 0 / 301 | 0 / 301 |
| Duplicate quote families | 0 / 301 | 0 / 301 |
| Words (the three files) | 19,302 | 19,465 (+163) |

**Where the remainder sits.** No file carries three couples and seven carry two: Hollow Choir `C-IIIγ-021` · Weeping Willow `C-IIIγ-140` · Dejà Vu `C-IVδ-125` · Broken Promise `N-IIIγ-160` · Floating Pillar `N-IIIγ-409` · Forgotten Shadow `N-IIβ-453` · Harvest Beyond the Gate `N-IIβ-627`. The worst tie in the wing is still **Melting Rope `N-IIIγ-447` × Forgotten Shadow `N-IIβ-453`, 0.72 in M.A.W. Use Notes — frozen, skipped by standing decision.** Behind it: Conservatory `N-IVδ-852` × Quagmire `O-IVδ-168` 0.64 (Log and Method) · Doorway to Nowhere `N-IIβ-152` × Scar Walker `O-IIIδ-011` 0.64 (Operational Parameters) · Eleven Fifty-Nine `C-IIIγ-912` × Backward Hour `C-IIIγ-913` 0.63 (M.A.W. Use Notes) · Hollow Knight `C-IVγ-073` × Smothering Mother `N-IVδ-005` 0.63 (M.A.W. Suit).

**The section mix holds.** `### M.A.W. Suit` is still the worst section at **6**, ahead of `## Operational Parameters` 4 · 감각 묘사 (Flavor Text) 4 · Interaction Pattern 4 · `### M.A.W. Use Notes` 3.

**Next rung: Batch 70 opens at three**, per the ladder and the owner's absolute floor. Worst-first candidates — Conservatory `N-IVδ-852` (0.64, I-Relic, and the heavy side) · Dejà Vu `C-IVδ-125` (two couples) · Harvest Beyond the Gate `N-IIβ-627` (two couples) · Hollow Choir `C-IIIγ-021` (two couples).

Disclosures: the turn opened on a stale sandbox at `bcf103f` and was levelled with `tools/syncbranch.py` to `933936e` before measurement (rollback **#103**); nothing was measured on a stale tree. The kit survived the turn boundary intact at `tools/kit/` and no rebuild was needed — the sixth turn running. Every unit was pushed and verified in the turn it was applied (`A0`). All figures above are measured at `e329731`.


**Batch 68 — CLOSED at ten; the fix phase continues: couples in the plan fall 50 → 37 / 301, with 13 cleared and none newly measurable, and no file in the wing now carries three couples.**

Taken on the owner's "p", after Batch 67 closed at seven. The ladder was opened at three, raised to five on the second "p" and to seven on the third, and the batch closes at ten. Same shape as the batches before it: one file per unit, the lighter side's small overlaps edited line by line in the file's own terms, never block-replaced, growth only (`R-15`). Two files needed two units each — Broken Clock `C-IIIγ-044` and The Memory Weaver `C-IVγ-009` — so ten units covered eight files, and all eight now carry **0 couples**.

**A third category of overlap surfaced, and it was self-inflicted.** Batches 61 through 67 had found two things behind a couple: generator stock pasted into two or three dossiers and never finished, and shared prose carried across the wing. Unit 9 found a third. The Masked Dancer `C-IIβ-099` and The Rage Statue `C-IIIγ-190` were coupled at 0.64 in `## Operational Parameters` by an editorial aside — *"The Object/Place restriction does not apply here and earlier copies of this line were wrong to imply it"* — that an earlier batch of this same programme had written into **both** files. The couple was my own correction note, duplicated. Replacing the Dancer's copy with the fact restated from its own Behavior table cleared both of the Dancer's couples at once and dropped the Statue from two to one. **When a couple's distinctive grams include phrases like `were wrong to imply it` or `earlier copies of this line`, the culprit is a prior batch, not the generator.**

**First drafts that keep the source's word order still echo badly — budget two passes.** > **Correction recorded 2026-10-09.** The sentence below originally read *“Eight of the ten units scored their worst echo on a first draft”*. That count is **not supported by anything measured**: the batch record holds first-pass echo figures for **three** units only — 7, 8 and 9 — and names **one** exception, unit 6. Units 1–5 and 10 have their word deltas recorded but no first-pass echo count, so no “eight of ten” can be derived from this file. The count has been narrowed to what is actually evidenced, and the lesson the paragraph is making — budget two passes — is unchanged. Recorded here rather than corrected by force-push (`R-` standing decision).

Three of the ten units scored their worst echo on a first draft that preserved the original's word order and needed a second pass before they were clean: the Memory Weaver's unit 7 went from 17 echoed grams to 1 once the stock opening *"You know it is there before you see it"* was reworded; unit 8 went 5 → 1; unit 9 went 11 → 1. The fix is to break the noun phrase and swap the verb, not to append clauses. Unit 6 was the exception — 0 echoed grams on the first pass — and it was also the only unit that replaced the offending **tail** of a row rather than the whole row, which is the technique to reach for when a row's opening clause is also the file's `R-29` condition.

**Self-echo against files rewritten earlier in the same batch is now the dominant failure mode.** Three units scored their worst all-301 run against a file this batch had already rewritten, not against the partner they were aimed at. `precheck_all.py` across the whole wing is now read before every apply, not only the two-partner check.

**The kit is committed, and it now survives the turn boundary.** Through four consecutive turns the working kit had to be rebuilt from scratch at the open of the turn. Excluding it with `.git/info/exclude` kept `git status` clean but did **not** make it persist: untracked files are lost at the turn boundary whether they are excluded or not, and only **tracked** content survives. The kit lives at `tools/kit/` and is tracked (`fef3c7c`) — `couples.py`, `apply.py`, `precheck.py`, `precheck_all.py`, `attr.py`, `unit_np.sh` and `tools.py`, documented in `tools/kit/README.md` together with the three silent bugs it carries fixes for. Five turns have now opened with the kit intact and no rebuild.

| # | Dossier | Structure | Fixed in place | Words (before → after) |
|---|---|---|---|---|
| 1 | [[SE-C-IIIγ-044_Broken_Clock_부서진_시계.md](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-044_Broken_Clock_%EB%B6%80%EC%84%9C%EC%A7%84_%EC%8B%9C%EA%B3%84.md)](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-044_Broken_Clock_%EB%B6%80%EC%84%9C%EC%A7%84_%EC%8B%9C%EA%B3%84.md) | I-Relic SE | the `Resolution Condition` row | 8,058 → 8,108 (+50) |
| 2 | [[SE-C-IIIγ-044_Broken_Clock_부서진_시계.md](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-044_Broken_Clock_%EB%B6%80%EC%84%9C%EC%A7%84_%EC%8B%9C%EA%B3%84.md)](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-044_Broken_Clock_%EB%B6%80%EC%84%9C%EC%A7%84_%EC%8B%9C%EA%B3%84.md) | I-Relic SE | both `## 상호작용` Interaction Pattern paragraphs | 8,108 → 8,152 (+44) |
| 3 | [[SE-C-IIIγ-061_The_Debtor_빚진_자.md](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-061_The_Debtor_%EB%B9%9A%EC%A7%84_%EC%9E%90.md)](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-061_The_Debtor_%EB%B9%9A%EC%A7%84_%EC%9E%90.md) | Subject SE | the M.A.W. Suit appearance, ability and cost | 7,138 → 7,228 (+90) |
| 4 | [[SE-C-IVβ-042_The_Angry_Maiden_분노의_처녀.md](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B2-042_The_Angry_Maiden_%EB%B6%84%EB%85%B8%EC%9D%98_%EC%B2%98%EB%85%80.md)](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B2-042_The_Angry_Maiden_%EB%B6%84%EB%85%B8%EC%9D%98_%EC%B2%98%EB%85%80.md) | Subject SE | the `Recommended response` row | 9,311 → 9,365 (+54) |
| 5 | [[SE-O-IIIβ-120_The_Wrath_Flame_분노의_불꽃.md](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-III%CE%B2-120_The_Wrath_Flame_%EB%B6%84%EB%85%B8%EC%9D%98_%EB%B6%88%EA%BD%83.md)](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-III%CE%B2-120_The_Wrath_Flame_%EB%B6%84%EB%85%B8%EC%9D%98_%EB%B6%88%EA%BD%83.md) | Subject SE | the `Physical Form` row | 6,954 → 6,986 (+32) |
| 6 | [[SE-C-Iα-779_Miscast_찢어진_유물.md](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-I%CE%B1-779_Miscast_%EC%B0%A2%EC%96%B4%EC%A7%84_%EC%9C%A0%EB%AC%BC.md)](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-I%CE%B1-779_Miscast_%EC%B0%A2%EC%96%B4%EC%A7%84_%EC%9C%A0%EB%AC%BC.md) | I-Relic SE | the **tail** of the `Recommended response` row; the opening clause is the file’s `R-29` condition and was left standing | 7,637 → 7,663 (+26) |
| 7 | [[SE-C-IVγ-009_The_Memory_Weaver_기억의_직공.md](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B3-009_The_Memory_Weaver_%EA%B8%B0%EC%96%B5%EC%9D%98_%EC%A7%81%EA%B3%B5.md)](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B3-009_The_Memory_Weaver_%EA%B8%B0%EC%96%B5%EC%9D%98_%EC%A7%81%EA%B3%B5.md) | Subject SE | the four generated contact paragraphs under 감각 묘사 (Flavor Text) | 8,545 → 8,611 (+66) |
| 8 | [[SE-C-IVγ-009_The_Memory_Weaver_기억의_직공.md](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B3-009_The_Memory_Weaver_%EA%B8%B0%EC%96%B5%EC%9D%98_%EC%A7%81%EA%B3%B5.md)](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B3-009_The_Memory_Weaver_%EA%B8%B0%EC%96%B5%EC%9D%98_%EC%A7%81%EA%B3%B5.md) | Subject SE | the M.A.W. Suit ability and cost, and both Operational Work Notes paragraphs | 8,611 → 8,656 (+45) |
| 9 | [[SE-C-IIβ-099_The_Masked_Dancer_가면_무용수.md](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-099_The_Masked_Dancer_%EA%B0%80%EB%A9%B4_%EB%AC%B4%EC%9A%A9%EC%88%98.md)](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-099_The_Masked_Dancer_%EA%B0%80%EB%A9%B4_%EB%AC%B4%EC%9A%A9%EC%88%98.md) | Subject SE | the `Recommended response` row — an earlier batch’s editorial aside, duplicated into two files | 7,743 → 7,783 (+40) |
| 10 | [[SE-C-IVδ-918_Ninety_Seconds_반복되는_생각.md](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-918_Ninety_Seconds_%EB%B0%98%EB%B3%B5%EB%90%98%EB%8A%94_%EC%83%9D%EA%B0%81.md)](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-918_Ninety_Seconds_%EB%B0%98%EB%B3%B5%EB%90%98%EB%8A%94_%EC%83%9D%EA%B0%81.md) | Non-Subject SE | the `Resistance` row and all three `## Trivia` lines | 6,475 → 6,550 (+75) |

- `C-IIIγ-044` Broken Clock — `a4a4dc7` — PUSH VERIFIED — [[SE-C-IIIγ-044_Broken_Clock_부서진_시계.md](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-044_Broken_Clock_%EB%B6%80%EC%84%9C%EC%A7%84_%EC%8B%9C%EA%B3%84.md)](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-044_Broken_Clock_%EB%B6%80%EC%84%9C%EC%A7%84_%EC%8B%9C%EA%B3%84.md)
- `C-IIIγ-061` The Debtor — `3c93ec4` — PUSH VERIFIED — [[SE-C-IIIγ-061_The_Debtor_빚진_자.md](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-061_The_Debtor_%EB%B9%9A%EC%A7%84_%EC%9E%90.md)](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-061_The_Debtor_%EB%B9%9A%EC%A7%84_%EC%9E%90.md)
- `C-IVβ-042` The Angry Maiden — `bcf103f` — PUSH VERIFIED — [[SE-C-IVβ-042_The_Angry_Maiden_분노의_처녀.md](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B2-042_The_Angry_Maiden_%EB%B6%84%EB%85%B8%EC%9D%98_%EC%B2%98%EB%85%80.md)](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B2-042_The_Angry_Maiden_%EB%B6%84%EB%85%B8%EC%9D%98_%EC%B2%98%EB%85%80.md)
- `O-IIIβ-120` The Wrath Flame — `9e11198` — PUSH VERIFIED — [[SE-O-IIIβ-120_The_Wrath_Flame_분노의_불꽃.md](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-III%CE%B2-120_The_Wrath_Flame_%EB%B6%84%EB%85%B8%EC%9D%98_%EB%B6%88%EA%BD%83.md)](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-III%CE%B2-120_The_Wrath_Flame_%EB%B6%84%EB%85%B8%EC%9D%98_%EB%B6%88%EA%BD%83.md)
- `C-Iα-779` Miscast — `daaf27d` — PUSH VERIFIED — [[SE-C-Iα-779_Miscast_찢어진_유물.md](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-I%CE%B1-779_Miscast_%EC%B0%A2%EC%96%B4%EC%A7%84_%EC%9C%A0%EB%AC%BC.md)](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-I%CE%B1-779_Miscast_%EC%B0%A2%EC%96%B4%EC%A7%84_%EC%9C%A0%EB%AC%BC.md)
- `C-IVγ-009` The Memory Weaver — `3261657` — PUSH VERIFIED — [[SE-C-IVγ-009_The_Memory_Weaver_기억의_직공.md](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B3-009_The_Memory_Weaver_%EA%B8%B0%EC%96%B5%EC%9D%98_%EC%A7%81%EA%B3%B5.md)](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B3-009_The_Memory_Weaver_%EA%B8%B0%EC%96%B5%EC%9D%98_%EC%A7%81%EA%B3%B5.md)
- `C-IIβ-099` The Masked Dancer — `5556ecc` — PUSH VERIFIED — [[SE-C-IIβ-099_The_Masked_Dancer_가면_무용수.md](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-099_The_Masked_Dancer_%EA%B0%80%EB%A9%B4_%EB%AC%B4%EC%9A%A9%EC%88%98.md)](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-099_The_Masked_Dancer_%EA%B0%80%EB%A9%B4_%EB%AC%B4%EC%9A%A9%EC%88%98.md)
- `C-IVδ-918` Ninety Seconds — `7e26c1c` — PUSH VERIFIED — [[SE-C-IVδ-918_Ninety_Seconds_반복되는_생각.md](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-918_Ninety_Seconds_%EB%B0%98%EB%B3%B5%EB%90%98%EB%8A%94_%EC%83%9D%EA%B0%81.md)](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-918_Ninety_Seconds_%EB%B0%98%EB%B3%B5%EB%90%98%EB%8A%94_%EC%83%9D%EA%B0%81.md)

| Counter | Open | Close |
|---|---|---|
| Couples in the plan (≥ 0.50 on either side) | 50 / 301 | **37 / 301** |
| Couples cleared this batch | — | **13** |
| Couples newly measurable | — | **0** |
| Files carrying a couple | 78 / 301 | **63 / 301** |
| Section-pairs over 0.50 | 50 | 37 |
| Couples ≥ 0.70 | 5 / 50 | 2 / 37 |
| Couples 0.60–0.69 | 11 / 50 | 4 / 37 |
| Couples 0.50–0.59 | 34 / 50 | 31 / 37 |
| Files carrying three or more couples | 0 / 301 | **0 / 301** |
| Files carrying two couples | 22 / 301 | **11 / 301** |
| Carrying — Subject SE | — | 37 / 142 |
| Carrying — Non-Subject SE | — | 14 / 71 |
| Carrying — I-Relic SE | — | 8 / 53 |
| Carrying — O-Relic SE | — | 4 / 28 |
| Carrying — A-Relic SE | — | 0 / 7 |
| Carrying — structure unreadable | — | 0 / 301 |
| Files carrying a whole copied section | 0 / 301 | 0 / 301 |
| Stock-line residue (`verify.py`) | 0 / 301 | 0 / 301 |
| `R-29`, all five clauses | 301 / 301 | 301 / 301 |
| Personalization queue | 0 / 301 | 0 / 301 |
| Duplicate quote families | 0 / 301 | 0 / 301 |
| Words (the eight files) | 61,861 | 62,383 (+522) |

**Where the remainder sits.** No file carries three couples, and eleven carry two: Hollow Choir `C-IIIγ-021` · Weeping Willow `C-IIIγ-140` · Blackened Angel `C-IVγ-946` · Dejà Vu `C-IVδ-125` · Broken Promise `N-IIIγ-160` · Floating Pillar `N-IIIγ-409` · Forgotten Shadow `N-IIβ-453` · Harvest Beyond the Gate `N-IIβ-627` · Well of Unfinished Words `N-IIβ-778` · Relic Waiting for Its Maker `O-IIIγ-651` · The Repeated Survivor `N-IVδ-902`. The worst tie in the wing is **Endless Shift `C-IVδ-915` × Sorrow Mass `C-Vω-925`, 0.71 in `## Trivia`**. Behind it: Melting Rope `N-IIIγ-447` × Forgotten Shadow `N-IIβ-453` 0.70 in M.A.W. Use Notes (**frozen — skipped by standing decision**), then Conservatory `N-IVδ-852` × Quagmire `O-IVδ-168` 0.64 in Log and Method and Doorway to Nowhere `N-IIβ-152` × Scar Walker `O-IIIδ-011` 0.64 in Operational Parameters.

**The section mix has turned over.** `### M.A.W. Suit` is now the worst section in the wing at **6** couples, ahead of `## Operational Parameters` at 4. Behind them: 감각 묘사 (Flavor Text) 4 · `## 상호작용` Interaction Pattern 4 · `### Log and Method` 4 · `### Escalation Notes` 3 · `### M.A.W. Use Notes` 3.

**Next rung: Batch 69 opens at three**, per the ladder and the owner's absolute floor. Worst-first candidates — Endless Shift `C-IVδ-915` (0.71, Trivia) · Sorrow Mass `C-Vω-925` (0.71, same tie, other side) · Conservatory `N-IVδ-852` (0.64, I-Relic) · Hollow Choir `C-IIIγ-021` (two couples).

Disclosures: every unit opened on a rolled-back sandbox and was levelled with `tools/syncbranch.py` before measurement (rollbacks **#99–#102**, each stale at `408797c`, dirty 273–275 files); nothing was measured on a stale tree. Every unit was pushed and verified in the turn it was applied (`A0`). All figures above are measured at `7e26c1c`.


**Batch 65 — CLOSED at seven; the fix phase continues: couples in the plan fall 129 → 106 / 301, the A-Relic structure goes from 2 / 7 files carrying a couple to 0 / 7, the generator's stock Work-Types tail survives in 1 file of 301 instead of 4, and all seven files worked now carry 0 couples each.**

Taken on the owner's "p" at the open, after Batch 64. Same shape as the batches before it: one file per unit, the light side's small overlaps edited line by line in the file's own terms, never block-replaced, growth-only (`R-15`), one validated push per unit (`A0`/`A1`), acceptance in both directions beneath 0.50, every report written to **`R-31`**. Two things shaped this batch. First, measurement before writing: every unit attributed its couple to individual rows before a word was drafted, which showed that four of the seven files were bound by a single table row and that several other rows are wing-wide furniture (297–581 owning files) which cannot form a couple at all and were therefore left alone rather than churned. Second, three of the rows repaired were not merely duplicated but **wrong about their own dossier** — the generator's tail sentence “Viderehan and Ferrehan are the valid Work Types and nothing else has been authorised” had been pasted into Subject dossiers whose own Behavior tables give all four Work Types real responses, and into a holding whose Watch Record forbids speech outright. Mid-batch the owner ruled *"Never Batch Anything Below 3"*, which contradicted `R-26` as written; the rule was amended in the same turn (`b2a9bb9`) so that the floor of three is absolute and a batch that cannot reach three finished units stays open instead of closing short.

| # | Dossier | Code | Fixed in place | Words (before → after) |
|---|---|---|---|---|
| 1 | [[SE-O-IVδ-115_Broken_Fragment_부서진_파편](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-IV%CE%B4-115_Broken_Fragment_%EB%B6%80%EC%84%9C%EC%A7%84_%ED%8C%8C%ED%8E%B8.md "SE-O-IVδ-115_Broken_Fragment_부서진_파편.md")] | `O-IVδ-115` | I-Relic SE — six Core Stat Line rows and all eight Log and Method cells re-authored for the fragment too heavy to lift; two broken generator splices repaired (a 30-Second Log cell carrying a foreign origin sentence, a 2-Minute Method cell with a doubled subject) | 8,490 → 8,661 (+171) |
| 2 | [[SE-N-IIIβ-160_The_Debt_Chain_빚의_사슬](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-III%CE%B2-160_The_Debt_Chain_%EB%B9%9A%EC%9D%98_%EC%82%AC%EC%8A%AC.md "SE-N-IIIβ-160_The_Debt_Chain_빚의_사슬.md")] | `N-IIIβ-160` | I-Relic SE — the Recommended response row and all three Binding Mantle paragraphs (appearance, ability, cost) re-authored; the dangling Entity Type splice “gloves do not work and have been” completed from the file's own activation line; the furniture rows left alone on purpose | 9,009 → 9,339 (+330) |
| 3 | [[SE-C-IVδ-219_Soaking_Shard_솟구친_조각](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-219_Soaking_Shard_%EC%86%9F%EA%B5%AC%EC%B9%9C_%EC%A1%B0%EA%B0%81.md "SE-C-IVδ-219_Soaking_Shard_솟구친_조각.md")] | `C-IVδ-219` | O-Relic SE — three Consequences bullets, the Tool Use Profile termination row and operational rule, and all eight Log and Method cells re-authored for the shard that stays wet in a vault the instruments call dry; two generator splices repaired | 8,248 → 8,582 (+334) |
| 4 | [[SE-N-IIα-215_Forgotten_Name_잊혀진_이름](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-II%CE%B1-215_Forgotten_Name_%EC%9E%8A%ED%98%80%EC%A7%84_%EC%9D%B4%EB%A6%84.md "SE-N-IIα-215_Forgotten_Name_잊혀진_이름.md")] | `N-IIα-215` | Subject SE — the Recommended response row rewritten against the file's own canon — it told staff to speak a name the Watch Record forbids speaking, and named two Work Types where the Behavior table gives four; one classification splice repaired | 8,500 → 8,593 (+93) |
| 5 | [[SE-N-IIβ-456_Fading_Fruit_번져가는_열매](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-II%CE%B2-456_Fading_Fruit_%EB%B2%88%EC%A0%B8%EA%B0%80%EB%8A%94_%EC%97%B4%EB%A7%A4.md "SE-N-IIβ-456_Fading_Fruit_번져가는_열매.md")] | `N-IIβ-456` | Non-Subject SE — the Recommended response row re-authored for the garden where nothing has ever been eaten; the two-Work-Type rule kept because this file really is an Object/Place; splice scan clean | 8,339 → 8,440 (+101) |
| 6 | [[SE-N-IVβ-019_The_Inherited_Debt_물려받은_빚](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-IV%CE%B2-019_The_Inherited_Debt_%EB%AC%BC%EB%A0%A4%EB%B0%9B%EC%9D%80_%EB%B9%9A.md "SE-N-IVβ-019_The_Inherited_Debt_물려받은_빚.md")] | `N-IVβ-019` | Subject SE — the Recommended response row re-authored against the file's own four-Work-Type table, where Flerehan is the fastest gauge drop it has; Survivors' Breath `O-IVδ-895` cleared with it, uneedited | 9,490 → 9,602 (+112) |
| 7 | [[SE-C-IIIβ-072_Fathers_Broken_Bond_아버지의_부러진_차용패](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B2-072_Fathers_Broken_Bond_%EC%95%84%EB%B2%84%EC%A7%80%EC%9D%98_%EB%B6%80%EB%9F%AC%EC%A7%84_%EC%B0%A8%EC%9A%A9%ED%8C%A8.md "SE-C-IIIβ-072_Fathers_Broken_Bond_아버지의_부러진_차용패.md")] | `C-IIIβ-072` | A-Relic SE — all eight Log and Method cells, the Escalation Notes watch paragraph and the fully stock Response sequence re-authored for Han-Sol's snapped tally tablet; the spliced 3-Uses cell repaired; Last Warmth of Forty-Two `O-IVδ-515` cleared with it, taking the A-Relic structure to 0 / 7 | 4,730 → 5,168 (+438) |

- `O-IVδ-115` SE-O-IVδ-115 — `1f72091` — PUSH VERIFIED — [[SE-O-IVδ-115_Broken_Fragment_부서진_파편](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-IV%CE%B4-115_Broken_Fragment_%EB%B6%80%EC%84%9C%EC%A7%84_%ED%8C%8C%ED%8E%B8.md "SE-O-IVδ-115_Broken_Fragment_부서진_파편.md")]
- `N-IIIβ-160` SE-N-IIIβ-160 — `526ccd0` — PUSH VERIFIED — [[SE-N-IIIβ-160_The_Debt_Chain_빚의_사슬](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-III%CE%B2-160_The_Debt_Chain_%EB%B9%9A%EC%9D%98_%EC%82%AC%EC%8A%AC.md "SE-N-IIIβ-160_The_Debt_Chain_빚의_사슬.md")]
- `C-IVδ-219` SE-C-IVδ-219 — `eb3d31c` — PUSH VERIFIED — [[SE-C-IVδ-219_Soaking_Shard_솟구친_조각](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-219_Soaking_Shard_%EC%86%9F%EA%B5%AC%EC%B9%9C_%EC%A1%B0%EA%B0%81.md "SE-C-IVδ-219_Soaking_Shard_솟구친_조각.md")]
- `N-IIα-215` SE-N-IIα-215 — `944fb63` — PUSH VERIFIED — [[SE-N-IIα-215_Forgotten_Name_잊혀진_이름](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-II%CE%B1-215_Forgotten_Name_%EC%9E%8A%ED%98%80%EC%A7%84_%EC%9D%B4%EB%A6%84.md "SE-N-IIα-215_Forgotten_Name_잊혀진_이름.md")]
- `N-IIβ-456` SE-N-IIβ-456 — `7ad235c` — PUSH VERIFIED — [[SE-N-IIβ-456_Fading_Fruit_번져가는_열매](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-II%CE%B2-456_Fading_Fruit_%EB%B2%88%EC%A0%B8%EA%B0%80%EB%8A%94_%EC%97%B4%EB%A7%A4.md "SE-N-IIβ-456_Fading_Fruit_번져가는_열매.md")]
- `N-IVβ-019` SE-N-IVβ-019 — `5010408` — PUSH VERIFIED — [[SE-N-IVβ-019_The_Inherited_Debt_물려받은_빚](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-IV%CE%B2-019_The_Inherited_Debt_%EB%AC%BC%EB%A0%A4%EB%B0%9B%EC%9D%80_%EB%B9%9A.md "SE-N-IVβ-019_The_Inherited_Debt_물려받은_빚.md")]
- `C-IIIβ-072` SE-C-IIIβ-072 — `db63d52` — PUSH VERIFIED — [[SE-C-IIIβ-072_Fathers_Broken_Bond_아버지의_부러진_차용패](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B2-072_Fathers_Broken_Bond_%EC%95%84%EB%B2%84%EC%A7%80%EC%9D%98_%EB%B6%80%EB%9F%AC%EC%A7%84_%EC%B0%A8%EC%9A%A9%ED%8C%A8.md "SE-C-IIIβ-072_Fathers_Broken_Bond_아버지의_부러진_차용패.md")]

| Counter | Open | Close |
|---|---|---|
| Couples in the plan (≥ 0.50 on either side) | 129 / 301 | **106 / 301** |
| Section-pairs over 0.50 | 143 | 116 |
| Files carrying a couple | 118 / 301 | 107 / 301 |
| Ties ≥ 0.70 | 13 / 129 | 12 / 106 |
| Ties 0.60–0.69 | 35 / 129 | 22 / 106 |
| Ties 0.50–0.59 | 81 / 129 | 72 / 106 |
| Ties inside one structure | 94 / 129 | 80 / 106 |
| A-Relic files carrying a couple | 2 / 7 | **0 / 7** |
| I-Relic files carrying a couple | 20 / 53 | 17 / 53 |
| O-Relic files carrying a couple | 10 / 28 | 8 / 28 |
| Subject files carrying a couple | 64 / 142 | 61 / 142 |
| Non-Subject files carrying a couple | 22 / 71 | 21 / 71 |
| Files carrying the generator's stock Work-Types tail | 4 / 301 | **1 / 301** |
| Files carrying a whole copied section | 0 / 301 | 0 / 301 |
| Stock-line residue (`verify.py`) | 0 / 301 | 0 / 301 |
| `R-29`, all five clauses | 301 / 301 | 301 / 301 |
| Personalization queue | 0 / 301 | 0 / 301 |
| Duplicate quote families | 0 / 301 | 0 / 301 |
| Distinct wing shingles (`sect.grams`, N=8, whole-file) | 1,504,568 | 1,506,215 (+1,647) |
| Words (the seven files) | 56,806 | 58,385 (+1,579) |
| Words (the wing, 301 files) | 2,204,718 | 2,206,297 (+1,579) |

Probes: close-time 301-file probe — each of the seven units at **0 couples**, and two further files cleared without being edited (Survivors' Breath `O-IVδ-895` at u6, Last Warmth of Forty-Two `O-IVδ-515` at u7). A pair-level diff of the open tree (`cf23de2`) against the close tree (`db63d52`), keyed on basenames so the two trees compare, gives **23 couples cleared and 0 newly measurable**, net −23, and the seven units account for all 23 (6+5+5+3+2+1+1). Per-unit echo prechecks, against a comparison list of 25–39 files holding each unit's partners plus every file shipped in Batches 62–65: u1 **5 → 3 → 1 → 0** · u2 **14 → 3 → 2 → 0** · u3 **16 → 1 → 0** · u4 **0 first pass** · u5 **3 → 0** · u6 **10 → 4 → 0** · u7 **16 → 4 → 0**. A second, wider pass introduced this batch checks every introduced run against all 301 dossiers and keeps only distinctively owned ones: u4, u5 and u6 finished at **0 files**, u3 at 29 files with a worst of 3 runs, u7 at 3 files with 1 run each, all far below the ten-run couple threshold.

Disclosures: every unit opened on a rolled-back sandbox and was levelled with `tools/syncbranch.py` before measurement (rollbacks **#82–#88**, each stale at `408797c`, dirty 273–274 files); nothing was force-pushed. The working kit does not survive a turn — `/tmp` and even a directory beside the repository are both wiped, which a probe file confirmed at u6 — so it was rebuilt and re-validated against the shipped census at every open; the rebuild is measured, not assumed, and it reproduced 123, 118, 113, 110, 108 and 107 couples in turn. One consequence is worth recording: the rebuilt kit splits the tier bands one pair differently from the Batch 64 close report (13 ties ≥ 0.70 at the open rather than 12), while the couple total of 129 is identical; the tier split is a secondary breakdown and is now measured one way only. u2's first gate run refused the push on a whitespace bug in the rebuilt gate script rather than on anything in the dossier; the pattern was fixed and the same edits passed every check. u2, u3 and u5 deliberately left furniture rows alone (Han-Energy yield, Han Dust Drop, Starting Sorrow Gauge, the stock `**Response sequence:**` where it was not distinctive) because a run owned by more than 25 files cannot form a couple, so rewriting it would add echo risk and move no counter. Three archive inconsistencies remain recorded and uncorrected, awaiting the owner's ruling, and one new inconsistency is reported rather than silently fixed: Survivors' Breath `O-IVδ-895` still carries the stock two-Work-Type tail in a Subject dossier whose own table lists four; it now forms no couple, so it is queued as defect repair.

Next rung: **Batch 66 opens at ten**, per the ladder and the owner's absolute floor. Worst-first candidates — Mourner's Bloom `C-Iα-330` (4, O-Relic) · Hatred Above `C-IVδ-923` (4, Non-Subject) · Weighted Silence `O-IIIγ-924` (4, Non-Subject) · Double Mouth `C-IIβ-716` (4, Subject) · Screaming Masonry `C-IIIγ-891` (4, I-Relic) · Hollow Saint `C-IIIγ-081` (4, Subject) · Collapsed Whisper `C-IVδ-249` (4, Subject); plus two zero-couple defect repairs, Survivors' Breath `O-IVδ-895` and Last Warmth of Forty-Two `O-IVδ-515`. Worst single tie in the wing is unchanged: Sleeping Tree `O-IIIγ-374` × Driftglass `O-IIIγ-914` at **0.77** in `### Tool Use Profile`, both I-Relic.

**Batch 67 — CLOSED at seven; the fix phase continues: couples in the plan fall 69 → 50 / 301, with 19 cleared and none newly measurable, and no file in the wing now carries three couples.**

Taken on the owner's "p", after Batch 66 closed at ten. The ladder was opened at ten and the batch is recorded as closing at seven, which is a valid rung: one file per unit, the lighter side's small overlaps edited line by line in the file's own terms, never block-replaced. All seven units were chosen the same way — the files carrying the most couples first, then the worst tie among them — and all seven finished at 0 couples.

**Every unit this batch found generator stock rather than shared prose.** In each case the overlap was a template block that had been pasted into two or three dossiers and never finished: the I-Relic Tool Use Profile frame, the five-line Testimonium, the equipment ability-and-cost frame, the Combat Actions table, the Breach Behavior rows, and the four-row Log and Method table. None of the seven required a judgement about authorship; each simply needed the block replaced with what the file already said about itself elsewhere.

**Three defects were found on the way and are recorded rather than silently fixed.** Driftglass `O-IIIγ-914` carries its whole relic triad twice — `### Tool Use Profile` at line 160 and again at line 217, with `### Log and Method` and `### Detailed Activation Record` likewise doubled. Amnesia `O-IIβ-914` has no readable `Tool Type` or `Entity Type` row at all, so its structure cannot be determined by script. Myrmidon `O-IIβ-235` carried the `Appearance :` label artifact. One generator splice was repaired in passing: Sorrow Fountain `C-IIIγ-088` read *"a single visible stream. forged during tears"*, with the sentence broken and lower-cased mid-cell.

**The kit is now persistent.** The working kit had to be rebuilt from scratch at the open of every turn from `/tmp`, four times running. It now lives at `.kit/` inside the repository root, which is the only location that survives the turn boundary, and it is excluded from Git through `.git/info/exclude` so it never enters a commit. Three bugs were fixed on the last rebuild and are worth naming because they are silent: `files_under()` resolved one directory too high when called without a base; `unit_np.sh` read `sectfile.py`'s verdict from the first line of its output when the verdict is on the last; and `attr.py` matched filenames without Unicode normalisation, so a code containing γ never matched.

| # | Dossier | Structure | Fixed in place | Words (before → after) |
|---|---|---|---|---|
| 1 | [[SE-O-IIIγ-374_Sleeping_Tree_잠든_나무](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-III%CE%B3-374_Sleeping_Tree_%EC%9E%A0%EB%93%A0_%EB%82%98%EB%AC%B4.md "SE-O-IIIγ-374_Sleeping_Tree_잠든_나무.md")] | I-Relic | Tool Use Profile rows, operational rule | 7,737 → 7,875 |
| 2 | [[SE-O-IIβ-914_Amnesia_잊혀진_일분](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-II%CE%B2-914_Amnesia_%EC%9E%8A%ED%98%80%EC%A7%84_%EC%9D%BC%EB%B6%84.md "SE-O-IIβ-914_Amnesia_잊혀진_일분.md")] | Unreadable | Testimonium, Trivia | 5,019 → 5,132 |
| 3 | [[SE-C-IVδ-249_Collapsed_Whisper_무너진_속삭임](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-249_Collapsed_Whisper_%EB%AC%B4%EB%84%88%EC%A7%84_%EC%86%8D%EC%82%AD%EC%9E%84.md "SE-C-IVδ-249_Collapsed_Whisper_무너진_속삭임.md")] | Subject | Weapon and suit ability and cost | 7,449 → 7,568 |
| 4 | [[SE-O-IIIγ-924_Weighted_Silence_침묵의_구역](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-III%CE%B3-924_Weighted_Silence_%EC%B9%A8%EB%AC%B5%EC%9D%98_%EA%B5%AC%EC%97%AD.md "SE-O-IIIγ-924_Weighted_Silence_침묵의_구역.md")] | O-Relic | Four Combat Actions rows, two appearances | 4,886 → 4,965 |
| 5 | [[SE-N-IIIβ-247_The_Undelivered_Thanks_전하지_못한_감사](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Unknown_Entities/SE-N-III%CE%B2-247_The_Undelivered_Thanks_%EC%A0%84%ED%95%98%EC%A7%80_%EB%AA%BB%ED%95%9C_%EA%B0%90%EC%82%AC.md "SE-N-IIIβ-247_The_Undelivered_Thanks_전하지_못한_감사.md")] | Non-Subject | Three Breach Behavior rows | 6,240 → 6,320 |
| 6 | [[SE-O-IIβ-235_Myrmidon_찢어진_영혼](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-II%CE%B2-235_Myrmidon_%EC%B0%A2%EC%96%B4%EC%A7%84_%EC%98%81%ED%98%BC.md "SE-O-IIβ-235_Myrmidon_찢어진_영혼.md")] | O-Relic | Breach row, response row, urn appearance | 7,198 → 7,309 |
| 7 | [[SE-C-IIIγ-088_The_Sorrow_Fountain_슬픔의_분수](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-088_The_Sorrow_Fountain_%EC%8A%AC%ED%94%94%EC%9D%98_%EB%B6%84%EC%88%98.md "SE-C-IIIγ-088_The_Sorrow_Fountain_슬픔의_분수.md")] | Subject | All four Log and Method rows | 8,019 → 8,123 |

- `O-IIIγ-374` Sleeping Tree — `3c1e184` — PUSH VERIFIED — [[SE-O-IIIγ-374_Sleeping_Tree_잠든_나무](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-III%CE%B3-374_Sleeping_Tree_%EC%9E%A0%EB%93%A0_%EB%82%98%EB%AC%B4.md "SE-O-IIIγ-374_Sleeping_Tree_잠든_나무.md")]
- `O-IIβ-914` Amnesia — `4ba7f3c` — PUSH VERIFIED — [[SE-O-IIβ-914_Amnesia_잊혀진_일분](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-II%CE%B2-914_Amnesia_%EC%9E%8A%ED%98%80%EC%A7%84_%EC%9D%BC%EB%B6%84.md "SE-O-IIβ-914_Amnesia_잊혀진_일분.md")]
- `C-IVδ-249` Collapsed Whisper — `99b0c9b` — PUSH VERIFIED — [[SE-C-IVδ-249_Collapsed_Whisper_무너진_속삭임](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-249_Collapsed_Whisper_%EB%AC%B4%EB%84%88%EC%A7%84_%EC%86%8D%EC%82%AD%EC%9E%84.md "SE-C-IVδ-249_Collapsed_Whisper_무너진_속삭임.md")]
- `O-IIIγ-924` Weighted Silence — `3d4f19e` — PUSH VERIFIED — [[SE-O-IIIγ-924_Weighted_Silence_침묵의_구역](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-III%CE%B3-924_Weighted_Silence_%EC%B9%A8%EB%AC%B5%EC%9D%98_%EA%B5%AC%EC%97%AD.md "SE-O-IIIγ-924_Weighted_Silence_침묵의_구역.md")]
- `N-IIIβ-247` Undelivered Thanks — `584171e` — PUSH VERIFIED — [[SE-N-IIIβ-247_The_Undelivered_Thanks_전하지_못한_감사](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Unknown_Entities/SE-N-III%CE%B2-247_The_Undelivered_Thanks_%EC%A0%84%ED%95%98%EC%A7%80_%EB%AA%BB%ED%95%9C_%EA%B0%90%EC%82%AC.md "SE-N-IIIβ-247_The_Undelivered_Thanks_전하지_못한_감사.md")]
- `O-IIβ-235` Myrmidon — `48c1089` — PUSH VERIFIED — [[SE-O-IIβ-235_Myrmidon_찢어진_영혼](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-II%CE%B2-235_Myrmidon_%EC%B0%A2%EC%96%B4%EC%A7%84_%EC%98%81%ED%98%BC.md "SE-O-IIβ-235_Myrmidon_찢어진_영혼.md")]
- `C-IIIγ-088` Sorrow Fountain — `3f314ce` — PUSH VERIFIED — [[SE-C-IIIγ-088_The_Sorrow_Fountain_슬픔의_분수](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-088_The_Sorrow_Fountain_%EC%8A%AC%ED%94%94%EC%9D%98_%EB%B6%84%EC%88%98.md "SE-C-IIIγ-088_The_Sorrow_Fountain_슬픔의_분수.md")]

| Counter | Open | Close |
|---|---|---|
| Couples in the plan (≥ 0.50 on either side) | 69 / 301 | **50 / 301** |
| Couples cleared this batch | — | **19** |
| Couples newly measurable | — | **0** |
| Files carrying a couple | 93 / 301 | 78 / 301 |
| Section-pairs over 0.50 | 57 | 51 |
| Ties ≥ 0.70 | 7 / 69 | 5 / 50 |
| Ties 0.60–0.69 | 14 / 69 | 11 / 50 |
| Ties 0.50–0.59 | 48 / 69 | 34 / 50 |
| Files carrying three or more couples | 8 / 301 | **0 / 301** |
| Carrying — Subject SE | — | 47 / 157 |
| Carrying — Non-Subject SE | — | 7 / 35 |
| Carrying — I-Relic SE | — | 11 / 50 |
| Carrying — O-Relic SE | — | 4 / 25 |
| Carrying — A-Relic SE | — | 0 / 7 |
| Carrying — structure unreadable | — | 9 / 27 |
| Files carrying a whole copied section | 0 / 301 | 0 / 301 |
| Stock-line residue (`verify.py`) | 0 / 301 | 0 / 301 |
| `R-29`, all five clauses | 301 / 301 | 301 / 301 |
| Personalization queue | 0 / 301 | 0 / 301 |
| Duplicate quote families | 0 / 301 | 0 / 301 |
| Words (the seven files) | 46,548 | 47,292 (+744) |

**Where the remainder sits.** No file carries three couples. The worst tie in the wing is Broken Clock `C-IIIγ-044` × Frozen Echo `C-IIIγ-609` at 0.73 in Core Stat Line. Behind it: Angry Maiden `C-IVβ-042` × Somnium `C-IVγ-175` 0.71 in Operational Parameters, Endless Shift `C-IVδ-915` × Sorrow Mass `C-Vω-925` 0.71 in Trivia, and Debtor `C-IIIγ-061` × Sorrow Seed `C-Iα-300` 0.70 in M.A.W. Suit. Melting Rope `N-IIIγ-447` × Forgotten Shadow `N-IIβ-453` at 0.72 is left alone because both files are on the frozen list. By section the remainder is Operational Parameters 9 · M.A.W. Suit 8 · Flavor Text 5 · Interaction Pattern 5 · Log and Method 4.

**Open findings, recorded for a ruling and not fixed silently.** 27 / 301 files have no parseable `Tool Type` or `Entity Type` row, so their structure cannot be read by script; 9 / 301 of them carry a couple. Driftglass `O-IIIγ-914` has its relic triad duplicated. The `Appearance :` label artifact is present in 142 / 504 files across the tree, not only in dossiers.

**Batch 66 — CLOSED at ten; the fix phase continues: couples in the plan fall 106 → 69 / 301, with 37 cleared and none newly measurable, and all ten files worked now carry 0 couples each.**

Taken on the owner's "p", after Batch 65 closed at seven. The ladder put this batch at ten from the open and it held: one file per unit, the lighter side's small overlaps edited line by line in the file's own terms, never block-replaced. Two units turned out to be carrying generator defects rather than shared prose. Screaming Masonry `C-IIIγ-891` had the word "grudge" doubled inside its own weapon ability. Kind Healer's Shadow `N-IIβ-280` had the two M.A.W. descriptions transposed — the section headed "The Healer's Shroud" described a surgical cleaver, and the weapon named "The Surgeon's Cleaver" described a needle-pointed stiletto. Both were repaired in place, along with the `Appearance :` label in that file, which is a generator artifact still present in 142 / 504 files.

**One correction to the record.** The u10 commit message describes Kind Healer's Shadow as Non-Subject and calls the row it replaced wrong. That is not right. The file's `Entity Type` row reads **Subject**, and the row read "This is a Subject and all four Work Types are open to it" — a correct statement, duplicated from the classification table. What u10 did was replace that boilerplate with the same fact restated from the file's own Behavior table and Operational Notes: which work types answer, what each one does to the gauge, and the one-cycle-per-person-per-shift rule. No content was lost or mis-stated, and the file still passes every gate. The commit message is wrong and is corrected here rather than by force-push, which is prohibited.

| # | Dossier | Structure | Fixed in place | Words (before → after) |
|---|---|---|---|---|
| 1 | [[SE-C-IIβ-716_Double_Mouth_찢어진_속삭임](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-716_Double_Mouth_%EC%B0%A2%EC%96%B4%EC%A7%84_%EC%86%8D%EC%82%AD%EC%9E%84.md "SE-C-IIβ-716_Double_Mouth_찢어진_속삭임.md")] | Subject | M.A.W. Weapon + Suit | 6,899 → 7,396 |
| 2 | [[SE-C-IIIγ-081_The_Hollow_Saint_빈_성자](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-081_The_Hollow_Saint_%EB%B9%88_%EC%84%B1%EC%9E%90.md "SE-C-IIIγ-081_The_Hollow_Saint_빈_성자.md")] | Subject | M.A.W. Weapon + Suit, Registry Addendum | 7,437 → 7,883 |
| 3 | [[SE-C-IIIγ-891_Screaming_Masonry_스며든_절규](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-891_Screaming_Masonry_%EC%8A%A4%EB%A9%B0%EB%93%A0_%EC%A0%88%EA%B7%9C.md "SE-C-IIIγ-891_Screaming_Masonry_스며든_절규.md")] | I-Relic | M.A.W. Weapon + Suit; doubled “grudge grudge” | 7,520 → 7,948 |
| 4 | [[SE-C-Iα-330_Mourner's_Bloom_슬픔의_꽃](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-I%CE%B1-330_Mourner%27s_Bloom_%EC%8A%AC%ED%94%94%EC%9D%98_%EA%BD%83.md "SE-C-Iα-330_Mourner's_Bloom_슬픔의_꽃.md")] | O-Relic | Operational Parameters, Core Stat Line | 7,124 → 7,274 |
| 5 | [[SE-C-IVδ-923_Hatred_Above_분노의_폭풍](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-923_Hatred_Above_%EB%B6%84%EB%85%B8%EC%9D%98_%ED%8F%AD%ED%92%8D.md "SE-C-IVδ-923_Hatred_Above_분노의_폭풍.md")] | Subject | Testimonium, Combat Actions | 5,118 → 5,334 |
| 6 | [[SE-C-IIIγ-031_The_Observing_Bird_지켜보는_새](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-031_The_Observing_Bird_%EC%A7%80%EC%BC%9C%EB%B3%B4%EB%8A%94_%EC%83%88.md "SE-C-IIIγ-031_The_Observing_Bird_지켜보는_새.md")] | Subject | Flavor Text, M.A.W. Suit | 8,329 → 8,723 |
| 7 | [[SE-O-IVδ-897_Welcome_Haven_부서진_벽](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-IV%CE%B4-897_Welcome_Haven_%EB%B6%80%EC%84%9C%EC%A7%84_%EB%B2%BD.md "SE-O-IVδ-897_Welcome_Haven_부서진_벽.md")] | Subject | Flavor Text (four contact paragraphs) | 8,233 → 8,480 |
| 8 | [[SE-C-IVγ-130_Deteriorata_무너지는_성자](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B3-130_Deteriorata_%EB%AC%B4%EB%84%88%EC%A7%80%EB%8A%94_%EC%84%B1%EC%9E%90.md "SE-C-IVγ-130_Deteriorata_무너지는_성자.md")] | Subject | Consequences, M.A.W. Weapon | 7,439 → 7,709 |
| 9 | [[SE-C-IVδ-668_Frozen_Fury_얼어붙은_잔해](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-668_Frozen_Fury_%EC%96%BC%EC%96%B4%EB%B6%99%EC%9D%80_%EC%9E%94%ED%95%B4.md "SE-C-IVδ-668_Frozen_Fury_얼어붙은_잔해.md")] | I-Relic | Log and Method (all four rows), Consequences | 8,079 → 8,261 |
| 10 | [[SE-N-IIβ-280_Kind_Healer's_Shadow_치유자의_그림자](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-II%CE%B2-280_Kind_Healer%27s_Shadow_%EC%B9%98%EC%9C%A0%EC%9E%90%EC%9D%98_%EA%B7%B8%EB%A6%BC%EC%9E%90.md "SE-N-IIβ-280_Kind_Healer's_Shadow_치유자의_그림자.md")] | Subject | M.A.W. Weapon + Suit, Operational Parameters | 6,895 → 7,106 |

- `C-IIβ-716` Double Mouth — `77503d2` — PUSH VERIFIED — [[SE-C-IIβ-716_Double_Mouth_찢어진_속삭임](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-716_Double_Mouth_%EC%B0%A2%EC%96%B4%EC%A7%84_%EC%86%8D%EC%82%AD%EC%9E%84.md "SE-C-IIβ-716_Double_Mouth_찢어진_속삭임.md")]
- `C-IIIγ-081` Hollow Saint — `5d84aa9` — PUSH VERIFIED — [[SE-C-IIIγ-081_The_Hollow_Saint_빈_성자](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-081_The_Hollow_Saint_%EB%B9%88_%EC%84%B1%EC%9E%90.md "SE-C-IIIγ-081_The_Hollow_Saint_빈_성자.md")]
- `C-IIIγ-891` Screaming Masonry — `effab0e` — PUSH VERIFIED — [[SE-C-IIIγ-891_Screaming_Masonry_스며든_절규](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-891_Screaming_Masonry_%EC%8A%A4%EB%A9%B0%EB%93%A0_%EC%A0%88%EA%B7%9C.md "SE-C-IIIγ-891_Screaming_Masonry_스며든_절규.md")]
- `C-Iα-330` Mourner's Bloom — `00a1248` — PUSH VERIFIED — [[SE-C-Iα-330_Mourner's_Bloom_슬픔의_꽃](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-I%CE%B1-330_Mourner%27s_Bloom_%EC%8A%AC%ED%94%94%EC%9D%98_%EA%BD%83.md "SE-C-Iα-330_Mourner's_Bloom_슬픔의_꽃.md")]
- `C-IVδ-923` Hatred Above — `26307a4` — PUSH VERIFIED — [[SE-C-IVδ-923_Hatred_Above_분노의_폭풍](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-923_Hatred_Above_%EB%B6%84%EB%85%B8%EC%9D%98_%ED%8F%AD%ED%92%8D.md "SE-C-IVδ-923_Hatred_Above_분노의_폭풍.md")]
- `C-IIIγ-031` Observing Bird — `09d3c06` — PUSH VERIFIED — [[SE-C-IIIγ-031_The_Observing_Bird_지켜보는_새](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-031_The_Observing_Bird_%EC%A7%80%EC%BC%9C%EB%B3%B4%EB%8A%94_%EC%83%88.md "SE-C-IIIγ-031_The_Observing_Bird_지켜보는_새.md")]
- `O-IVδ-897` Welcome Haven — `3fc7eb7` — PUSH VERIFIED — [[SE-O-IVδ-897_Welcome_Haven_부서진_벽](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-IV%CE%B4-897_Welcome_Haven_%EB%B6%80%EC%84%9C%EC%A7%84_%EB%B2%BD.md "SE-O-IVδ-897_Welcome_Haven_부서진_벽.md")]
- `C-IVγ-130` Deteriorata — `1fb5736` — PUSH VERIFIED — [[SE-C-IVγ-130_Deteriorata_무너지는_성자](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B3-130_Deteriorata_%EB%AC%B4%EB%84%88%EC%A7%80%EB%8A%94_%EC%84%B1%EC%9E%90.md "SE-C-IVγ-130_Deteriorata_무너지는_성자.md")]
- `C-IVδ-668` Frozen Fury — `d2fadcb` — PUSH VERIFIED — [[SE-C-IVδ-668_Frozen_Fury_얼어붙은_잔해](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-668_Frozen_Fury_%EC%96%BC%EC%96%B4%EB%B6%99%EC%9D%80_%EC%9E%94%ED%95%B4.md "SE-C-IVδ-668_Frozen_Fury_얼어붙은_잔해.md")]
- `N-IIβ-280` Kind Healer's Shadow — `22acca9` — PUSH VERIFIED — [[SE-N-IIβ-280_Kind_Healer's_Shadow_치유자의_그림자](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-II%CE%B2-280_Kind_Healer%27s_Shadow_%EC%B9%98%EC%9C%A0%EC%9E%90%EC%9D%98_%EA%B7%B8%EB%A6%BC%EC%9E%90.md "SE-N-IIβ-280_Kind_Healer's_Shadow_치유자의_그림자.md")]

| Counter | Open | Close |
|---|---|---|
| Couples in the plan (≥ 0.50 on either side) | 106 / 301 | **69 / 301** |
| Couples cleared this batch | — | **37** |
| Couples newly measurable | — | **0** |
| Files carrying a couple | 107 / 301 | 93 / 301 |
| Section-pairs over 0.50 | 109 | 72 |
| Ties ≥ 0.70 | 10 / 106 | 7 / 69 |
| Ties 0.60–0.69 | 14 / 106 | 14 / 69 |
| Ties 0.50–0.59 | 82 / 106 | 48 / 69 |
| Files carrying four couples | 8 / 301 | 0 / 301 |
| Carrying — Subject SE | — | 57 / 157 |
| Carrying — Non-Subject SE | — | 7 / 35 |
| Carrying — I-Relic SE | — | 12 / 50 |
| Carrying — O-Relic SE | — | 5 / 25 |
| Carrying — A-Relic SE | — | 0 / 7 |
| Files carrying a whole copied section | 0 / 301 | 0 / 301 |
| Stock-line residue (`verify.py`) | 0 / 301 | 0 / 301 |
| `R-29`, all five clauses | 301 / 301 | 301 / 301 |
| Personalization queue | 0 / 301 | 0 / 301 |
| Duplicate quote families | 0 / 301 | 0 / 301 |
| Words (the ten files) | 73,073 | 76,114 (+3,041) |

**Where the remainder sits.** No file now carries four couples. The worst tie in the wing is unchanged and still unworked: Sleeping Tree `O-IIIγ-374` × Driftglass `O-IIIγ-914` at 0.77 in Tool Use Profile, both I-Relic. Behind it: Broken Clock `C-IIIγ-044` × Frozen Echo `C-IIIγ-609` 0.73 in Core Stat Line, and Eleven Fifty-Nine `C-IIIγ-912` × Amnesia `O-IIβ-914` 0.73 in Testimonium. By section the remainder is M.A.W. Suit 12 · Operational Parameters 10 · Log and Method 7 · Flavor Text 5 · Interaction Pattern 5.

**Open finding, not a unit.** 27 / 301 files have no parseable `Tool Type` or `Entity Type` row in their SECC Classification table, so their structure cannot be read by script; 12 / 301 of them carry a couple. This does not move a counter and is recorded here for a ruling rather than fixed silently.

**Batch 64 — CLOSED at five; the fix phase continues: couples in the plan fall 150 → 129 / 301, the A-Relic structure goes from 7 / 7 files carrying a couple to 2 / 7, and all five files worked now carry 0 couples each.**

Taken on the owner's "p" at the open, after Batch 63. Same shape as the batches before it: one file per unit, the light side's small overlaps edited line by line in the file's own terms, never block-replaced, growth-only (`R-15`), one validated push per unit (`A0`/`A1`), acceptance in both directions beneath 0.50, every report written to **`R-31`**. Two things changed the shape of this batch. The first was an owner correction — *"Wrong The Five SE Docs Is Subject SE, Non-Subject SE, And The Three Relic Type SE That Why I Test You, You Not Even Know That SE Have Five Distinct Structure For It DOCS"* — and the taxonomy was measured off the files and written down at `REFERENCE_SOMNARAK_WIKI/SE_DOC_STRUCTURES.md` (`4645e7e`): Subject **142** · Non-Subject **71** · I-Relic **53** · O-Relic **28** · A-Relic **7** = 301 / 301, the discriminator being the relic triad (`### Tool Use Profile — {I,O,A}-Relic` + `### Log and Method` + `### Detailed Activation Record`), present in **88 / 88** relic files and **0 / 213** non-relic files. The second was that units 3 to 5 then worked the A-Relic class deliberately, and the taxonomy held: u3's five ties were one section against five files of the same class, and u4's three were the same two sections against three more of them.

| # | Dossier | Code | Fixed in place | Words (before → after) |
|---|---|---|---|---|
| 1 | [[SE-C-IVδ-250_Restless_Gap_찢어진_흔적](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-250_Restless_Gap_%EC%B0%A2%EC%96%B4%EC%A7%84_%ED%9D%94%EC%A0%81.md "SE-C-IVδ-250_Restless_Gap_찢어진_흔적.md")] | `C-IVδ-250` | Subject SE — all four Consequences bullets, the Trace Mantle's appearance, ability and cost, and both Vigil Hand-Cannon appearance paragraphs re-authored for the zone that breaks sequence (six couples) | 7,905 → 8,106 |
| 2 | [[SE-N-IVδ-517_Broken_Tear_부서진_눈물](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-IV%CE%B4-517_Broken_Tear_%EB%B6%80%EC%84%9C%EC%A7%84_%EB%88%88%EB%AC%BC.md "SE-N-IVδ-517_Broken_Tear_부서진_눈물.md")] | `N-IVδ-517` | Subject SE — the four generated contact paragraphs in the flavor text, two Escalation Notes lines and three Breach Behavior rows re-authored for the tear that outlived the woman who wept it (six couples) | 8,419 → 8,591 |
| 3 | [[SE-C-IIβ-290_Broken_Compass_부서진_나침반](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-290_Broken_Compass_%EB%B6%80%EC%84%9C%EC%A7%84_%EB%82%98%EC%B9%A8%EB%B0%98.md "SE-C-IIβ-290_Broken_Compass_부서진_나침반.md")] | `C-IIβ-290` | A-Relic — all eight Log and Method cells re-authored for the Compass that gives one bearing toward grief instead of the destination asked for; five couples, all against A-Relic files, all in that one section | 7,533 → 7,639 |
| 4 | [[SE-C-Iα-114_A_Letter_Never_Sent_부치지_못한_편지](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-I%CE%B1-114_A_Letter_Never_Sent_%EB%B6%80%EC%B9%98%EC%A7%80_%EB%AA%BB%ED%95%9C_%ED%8E%B8%EC%A7%80.md "SE-C-Iα-114_A_Letter_Never_Sent_부치지_못한_편지.md")] | `C-Iα-114` | A-Relic — the Escalation Notes watch paragraph and response sequence plus all eight Log and Method cells re-authored for the unbroken indigo seal (three couples; Magistrates Strike-Through cleared as a side effect) | 4,391 → 4,577 |
| 5 | [[SE-N-IIβ-250_Debt-Collector_s-Lantern_추징관의_등불](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-II%CE%B2-250_Debt-Collector_s-Lantern_%EC%B6%94%EC%A7%95%EA%B4%80%EC%9D%98_%EB%93%B1%EB%B6%88.md "SE-N-IIβ-250_Debt-Collector_s-Lantern_추징관의_등불.md")] | `N-IIβ-250` | A-Relic — five Core Stat Line rows and four operational parameter rows re-authored for the lantern that is never lifted from its mount (two couples, both against I-Relic files) | 7,507 → 7,683 |

- `C-IVδ-250` Restless Gap — `59d0343` — PUSH VERIFIED — [[SE-C-IVδ-250_Restless_Gap_찢어진_흔적](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-250_Restless_Gap_%EC%B0%A2%EC%96%B4%EC%A7%84_%ED%9D%94%EC%A0%81.md "SE-C-IVδ-250_Restless_Gap_찢어진_흔적.md")]
- `N-IVδ-517` Broken Tear — `d847eca` — PUSH VERIFIED — [[SE-N-IVδ-517_Broken_Tear_부서진_눈물](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-IV%CE%B4-517_Broken_Tear_%EB%B6%80%EC%84%9C%EC%A7%84_%EB%88%88%EB%AC%BC.md "SE-N-IVδ-517_Broken_Tear_부서진_눈물.md")]
- `C-IIβ-290` Broken Compass — `85dadfe` — PUSH VERIFIED — [[SE-C-IIβ-290_Broken_Compass_부서진_나침반](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-290_Broken_Compass_%EB%B6%80%EC%84%9C%EC%A7%84_%EB%82%98%EC%B9%A8%EB%B0%98.md "SE-C-IIβ-290_Broken_Compass_부서진_나침반.md")]
- `C-Iα-114` A Letter Never Sent — `ccf6088` — PUSH VERIFIED — [[SE-C-Iα-114_A_Letter_Never_Sent_부치지_못한_편지](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-I%CE%B1-114_A_Letter_Never_Sent_%EB%B6%80%EC%B9%98%EC%A7%80_%EB%AA%BB%ED%95%9C_%ED%8E%B8%EC%A7%80.md "SE-C-Iα-114_A_Letter_Never_Sent_부치지_못한_편지.md")]
- `N-IIβ-250` Debt-Collector's Lantern — `012a23b` — PUSH VERIFIED — [[SE-N-IIβ-250_Debt-Collector_s-Lantern_추징관의_등불](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-II%CE%B2-250_Debt-Collector_s-Lantern_%EC%B6%94%EC%A7%95%EA%B4%80%EC%9D%98_%EB%93%B1%EB%B6%88.md "SE-N-IIβ-250_Debt-Collector_s-Lantern_추징관의_등불.md")]

| Counter | Open | Close |
|---|---|---|
| Couples in the plan (≥ 0.50 on either side) | 150 / 301 | **129 / 301** |
| Section-pairs over 0.50 | 166 | 143 |
| Files carrying a couple | 127 / 301 | 118 / 301 |
| Ties ≥ 0.70 | 14 / 150 | 12 / 129 |
| Ties 0.60–0.69 | 44 / 150 | 35 / 129 |
| Ties 0.50–0.59 | 92 / 150 | 82 / 129 |
| Ties inside one structure | 110 / 150 | 94 / 129 |
| A-Relic files carrying a couple | 7 / 7 | **2 / 7** |
| Files carrying a whole copied section | 0 / 301 | 0 / 301 |
| Stock-line residue (`verify.py`) | 0 / 301 | 0 / 301 |
| `R-29`, all five clauses | 301 / 301 | 301 / 301 |
| Personalization queue | 0 / 301 | 0 / 301 |
| Duplicate quote families | 0 / 301 | 0 / 301 |
| Distinct wing shingles (`sect.grams`, N=8) | 1,447,869 | 1,449,246 (+1,377) |
| Words (the five files) | 35,755 | 36,596 (+841) |
| Words (the wing, 301 files) | 2,203,877 | 2,204,718 (+841) |

Probes: close-time 301-file probe — each of the five units at **0 couples**. A pair-level diff of the open tree (`fb4b8db`) against the close tree (`012a23b`) gives **22 couples cleared and 1 newly measurable**, net −21: the one that appeared is Cracked Hourglass `C-IIIβ-036` × Broken Fragment `O-IVδ-115`, 0.61, `### Core Stat Line`, which came into measurement when u5 took stock grams out of the Lantern and dropped those grams from 26 owning files to 25, the `DISTINCTIVE_MAX` ceiling. Per-unit echo prechecks u1 **1 → 0** · u2 **2 → 0** · u3 **0 on the first pass** · u4 **8 → 1 → 0** · u5 **12 → 5 → 5 → 0**, the comparison list holding each unit's partners plus all ten Batch 62 files plus every Batch 63 and Batch 64 file already shipped. Disclosures: every unit opened on a rolled-back sandbox and was levelled with `tools/syncbranch.py` before anything was measured (rollbacks **#77** to **#81**, each stale at `408797c`, dirty 272–273 files); nothing was force-pushed. u3's first draft passed the echo check at 0 and was still reworded, because it contained a house phrase on the do-not-draft list (*"the whole of what"*); the reworded draft is what shipped. u5's Resolution Condition row was reworded with `wikistd.py`'s `condition()` checked first — this file's condition is read from the `| **Management** |` row, not from the stat table, and that row was not touched. Next rung worst-first: Broken Fragment `O-IVδ-115` (6, I-Relic) · Debt Chain `N-IIIβ-160` (5, I-Relic) · Soaking Shard `C-IVδ-219` (5, O-Relic) · Forgotten Name `N-IIα-215` (4, Subject) · Fading Fruit `N-IIβ-456` (4, Non-Subject) · Inherited Debt `N-IVβ-019` (4, Subject). The two A-Relic files still carrying: Fathers Broken Bond `C-IIIβ-072` (1) · Last Warmth of Forty-Two `O-IVδ-515` (1). The worst single tie in the wing is unchanged: Sleeping Tree `O-IIIγ-374` × Driftglass `O-IIIγ-914`, 0.77, `### Tool Use Profile`, both I-Relic.

**Batch 63 — CLOSED at three; the fix phase continues: couples in the plan fall 168 → 150 / 301, and all three files worked now carry 0 couples each.**

Taken on the owner's "p" at the open, after Batch 62. Same shape as the batch before: one file per unit, the light side's small overlaps edited line by line in the file's own terms, never block-replaced, growth-only (`R-15`), one validated push per unit (`A0`/`A1`), acceptance in both directions beneath 0.50, and every report written to **`R-31`** — answer first, linked cell names, counters as `x / y`. Each unit's echo precheck ran against that unit's own partners plus all ten Batch 62 files plus every Batch 63 file already shipped, which caught self-reuse before it reached the archive rather than after.

| # | Dossier | Code | Fixed in place | Words (before → after) |
|---|---|---|---|---|
| 1 | [[SE-C-IIIβ-015_The_Debt_Scale_빚의_저울](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B2-015_The_Debt_Scale_%EB%B9%9A%EC%9D%98_%EC%A0%80%EC%9A%B8.md "SE-C-IIIβ-015_The_Debt_Scale_빚의_저울.md")] | `C-IIIβ-015` | 17 replacements: the Core Stat Line rows, the Resolution Condition (which also carried a repaired generator sentence), both Interaction Pattern paragraphs, four operational parameter rows and the Balance Veil and Balance Projector cells — six couples broken, all four partners now under 0.50 in both directions | 7,444 → 7,807 |
| 2 | [[SE-C-IIβ-170_Unrung_침묵의_종](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-170_Unrung_%EC%B9%A8%EB%AC%B5%EC%9D%98_%EC%A2%85.md "SE-C-IIβ-170_Unrung_침묵의_종.md")] | `C-IIβ-170` | five Core Stat Line rows and four operational parameter rows re-authored for the bell that chose silence, plus the repair of a generator truncation that had left the Recommended response row mid-sentence ("across the directorate and every —") — six couples broken | 8,943 → 9,131 |
| 3 | [[SE-C-IVδ-092_Pyre_of_Truths_타오르는_도서관](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-092_Pyre_of_Truths_%ED%83%80%EC%98%A4%EB%A5%B4%EB%8A%94_%EB%8F%84%EC%84%9C%EA%B4%80.md "SE-C-IVδ-092_Pyre_of_Truths_타오르는_도서관.md")] | `C-IVδ-092` | the four Consequences bullets and the Burning Plate's appearance, ability and cost re-authored for the library that burns without consuming — six couples broken, five of them in the M.A.W. Suit section | 8,163 → 8,313 |

- `C-IIIβ-015` The Debt Scale — `aed93f9` — PUSH VERIFIED — [[SE-C-IIIβ-015_The_Debt_Scale_빚의_저울](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B2-015_The_Debt_Scale_%EB%B9%9A%EC%9D%98_%EC%A0%80%EC%9A%B8.md "SE-C-IIIβ-015_The_Debt_Scale_빚의_저울.md")]
- `C-IIβ-170` Unrung — `1626a7b` — PUSH VERIFIED — [[SE-C-IIβ-170_Unrung_침묵의_종](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-170_Unrung_%EC%B9%A8%EB%AC%B5%EC%9D%98_%EC%A2%85.md "SE-C-IIβ-170_Unrung_침묵의_종.md")]
- `C-IVδ-092` Pyre of Truths — `9049538` — PUSH VERIFIED — [[SE-C-IVδ-092_Pyre_of_Truths_타오르는_도서관](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-092_Pyre_of_Truths_%ED%83%80%EC%98%A4%EB%A5%B4%EB%8A%94_%EB%8F%84%EC%84%9C%EA%B4%80.md "SE-C-IVδ-092_Pyre_of_Truths_타오르는_도서관.md")]

| Counter | Open | Close |
|---|---|---|
| Couples in the plan (≥ 0.50 on either side) | 168 / 301 | **150 / 301** |
| Section-pairs over 0.50 | 186 | 166 |
| Files carrying a couple | 130 / 301 | 127 / 301 |
| Ties ≥ 0.70 | 17 / 168 | 14 / 150 |
| Ties 0.60–0.69 | 51 / 168 | 44 / 150 |
| Ties 0.50–0.59 | 100 / 168 | 92 / 150 |
| Files carrying a whole copied section | 0 / 301 | 0 / 301 |
| Stock-line residue (`verify.py`) | 0 / 301 | 0 / 301 |
| `R-29`, all five clauses | 301 / 301 | 301 / 301 |
| Personalization queue | 0 / 301 | 0 / 301 |
| Duplicate quote families | 0 / 301 | 0 / 301 |
| Distinct wing shingles (`sect.grams`, N=8) | 1,447,005 | 1,447,869 (+864) |
| Words (the three files) | 24,550 | 25,251 (+701) |
| Words (the wing, 301 files) | 2,203,176 | 2,203,877 (+701) |

Probes: close-time 301-file probe — each of the three units at **0 couples**, worst residual inside the batch 0.49 (Pyre of Truths × Rising Wall, Consequences, the partner's own direction). Per-unit echo prechecks u1 **44 → 17 → 1 → 0** · u2 **12 → 4 → 0** · u3 **1 → 0**. Disclosures: every unit opened on a rolled-back sandbox and was levelled with `tools/syncbranch.py` before anything was measured (rollbacks **#73** at the open, **#75** at u2, **#76** at u3, each stale at `408797c` and dirty 271–272 files); nothing was force-pushed. u2 taught a drafting rule now standing: inside a stat row the words placed directly after the figures collide with other files' rows, so the gloss follows a middle dot instead. Next rung, worst-first: Restless Gap `C-IVδ-250` (6) · Broken Tear `N-IVδ-517` (6) · Debt Chain `N-IIIβ-160` (5) · Broken Fragment `O-IVδ-115` (5) · Soaking Shard `C-IVδ-219` (5). The worst single tie in the wing is unchanged: Sleeping Tree `O-IIIγ-374` × Driftglass `O-IIIγ-914`, 0.77, Tool Use Profile.

**Batch 62 — CLOSED at ten (nine ladder units plus the held one); the fix phase continues: couples in the plan fall 237 → 168 / 301, and the stock-line residue closes at 0 / 301.**

Taken on the owner's "p" at the open, after Batch 61. The batch stayed inside the fix phase: one file per unit, the light side's small overlaps edited line by line in the file's own terms, never block-replaced, growth-only (`R-15`), one validated push per unit (`A0`/`A1`), acceptance in both directions beneath 0.50. Two owner directives arrived mid-batch and were written down as rules before the next unit was taken: **`R-31`**, the chatroom readability rule (`e260585`), and its same-day amendment putting each SE's git link on its own name inside any table that lists the entity and the sections fixed on it (`a4a8dc5`, with `tools/ghlink.py --plain` added so the cell form is printed rather than hand-typed). The held file was released by the owner's instruction *"Do The Held One At The Same Time"* and shipped beside unit 7.

| # | Dossier | Code | Fixed in place | Words (before → after) |
|---|---|---|---|---|
| 1 | [[SE-C-IIβ-185_Whispering_Gallery_속삭이는_갤러리](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-185_Whispering_Gallery_%EC%86%8D%EC%82%AD%EC%9D%B4%EB%8A%94_%EA%B0%A4%EB%9F%AC%EB%A6%AC.md "SE-C-IIβ-185_Whispering_Gallery_속삭이는_갤러리.md")] | `C-IIβ-185` | M.A.W. Suit, Weapon and Field Use Record cells re-authored for the hall (× Spreading Well 0.78/0.76 · 0.54/0.51 · 0.51/0.51 → 0.035/0.044 · 0.213/0.198 · 0.129/0.144) | 7,518 → 7,554 |
| 2 | [[SE-C-IVδ-767_Swallow_번져가는_그림자](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-767_Swallow_%EB%B2%88%EC%A0%B8%EA%B0%80%EB%8A%94_%EA%B7%B8%EB%A6%BC%EC%9E%90.md "SE-C-IVδ-767_Swallow_번져가는_그림자.md")] | `C-IVδ-767` | the Consequences quartet and the Escalation Notes re-authored for the shadow’s duration (six couples broken at once, worst residual 0.064) | 8,155 → 8,249 |
| 3 | [[SE-O-Iα-794_Portcullis_무너진_문](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-I%CE%B1-794_Portcullis_%EB%AC%B4%EB%84%88%EC%A7%84_%EB%AC%B8.md "SE-O-Iα-794_Portcullis_무너진_문.md")] | `O-Iα-794` | Core Stat Line rows, the Log and Method table and the operational parameter rows re-authored for the Door (twelve couples, worst residual 0.324) | 7,984 → 8,155 |
| 4 | [[SE-C-IIIγ-902_Beating_Relic_고동치는_유물](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-902_Beating_Relic_%EA%B3%A0%EB%8F%99%EC%B9%98%EB%8A%94_%EC%9C%A0%EB%AC%BC.md "SE-C-IIIγ-902_Beating_Relic_고동치는_유물.md")] | `C-IIIγ-902` | the stat rows, the veil’s appearance and ability and the blade’s appearance, ability and cost re-authored for the stone (nine couples) | 6,313 → 6,467 |
| 5 | [[SE-C-IIβ-102_Frozen_Tear_얼어붙은_눈물](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-102_Frozen_Tear_%EC%96%BC%EC%96%B4%EB%B6%99%EC%9D%80_%EB%88%88%EB%AC%BC.md "SE-C-IIβ-102_Frozen_Tear_얼어붙은_눈물.md")] | `C-IIβ-102` | the Consequences, the Log and Method cells and the stat rows re-authored for the tear, plus a second tightening pass on the Broken Fragment lines (nine couples) | 8,146 → 8,293 |
| 6 | [[SE-C-IIIγ-300_Memory_Lock_기억의_자물쇠](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-300_Memory_Lock_%EA%B8%B0%EC%96%B5%EC%9D%98_%EC%9E%90%EB%AC%BC%EC%87%A0.md "SE-C-IIIγ-300_Memory_Lock_기억의_자물쇠.md")] | `C-IIIγ-300` | all eight Log and Method cells, the O-Relic rows and the Trivia lines re-authored for the plate and the whisper (ten couples) | 7,704 → 7,963 |
| 7 | [[SE-C-IVβ-041_The_Grieving_Maiden_슬픔의_처녀](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B2-041_The_Grieving_Maiden_%EC%8A%AC%ED%94%94%EC%9D%98_%EC%B2%98%EB%85%80.md "SE-C-IVβ-041_The_Grieving_Maiden_슬픔의_처녀.md")] | `C-IVβ-041` | the four flavor paragraphs and the Consequences re-authored for the woman made of crystallized tears (eight couples) | 8,001 → 8,177 |
| held | [[SE-C-Iα-869_Homecoming_Tree_돌아온_나무](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-I%CE%B1-869_Homecoming_Tree_%EB%8F%8C%EC%95%84%EC%98%A8_%EB%82%98%EB%AC%B4.md "SE-C-Iα-869_Homecoming_Tree_돌아온_나무.md")] | `C-Iα-869` | Story Log Entry 1: the last surviving generator stock line re-authored in the Tree’s own terms, facts and figures standing (residue 1 → 0 / 301) | 7,406 → 7,441 |
| 8 | [[SE-C-IVγ-240_Broken_Clocktower_부서진_시계탑](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B3-240_Broken_Clocktower_%EB%B6%80%EC%84%9C%EC%A7%84_%EC%8B%9C%EA%B3%84%ED%83%91.md "SE-C-IVγ-240_Broken_Clocktower_부서진_시계탑.md")] | `C-IVγ-240` | the Consequences bullets, all eight Log and Method cells and the Mercy Broadsword’s appearance re-authored for 3:47 (eight couples) | 8,164 → 8,439 |
| 9 | [[SE-C-IVδ-505_Cold_Burn_얼어붙은_그림자](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-505_Cold_Burn_%EC%96%BC%EC%96%B4%EB%B6%99%EC%9D%80_%EA%B7%B8%EB%A6%BC%EC%9E%90.md "SE-C-IVδ-505_Cold_Burn_얼어붙은_그림자.md")] | `C-IVδ-505` | all four Consequences bullets, the Returning Arbalest’s appearance and cost and the veil’s ability and cost re-authored for the vault approach (six couples) | 7,769 → 8,048 |

- `C-IIβ-185` Whispering Gallery — `7f27a33` — PUSH VERIFIED — [[SE-C-IIβ-185_Whispering_Gallery_속삭이는_갤러리](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-185_Whispering_Gallery_%EC%86%8D%EC%82%AD%EC%9D%B4%EB%8A%94_%EA%B0%A4%EB%9F%AC%EB%A6%AC.md "SE-C-IIβ-185_Whispering_Gallery_속삭이는_갤러리.md")]
- `C-IVδ-767` Swallow — `4c85f02` — PUSH VERIFIED — [[SE-C-IVδ-767_Swallow_번져가는_그림자](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-767_Swallow_%EB%B2%88%EC%A0%B8%EA%B0%80%EB%8A%94_%EA%B7%B8%EB%A6%BC%EC%9E%90.md "SE-C-IVδ-767_Swallow_번져가는_그림자.md")]
- `O-Iα-794` Portcullis — `90bf03a` — PUSH VERIFIED — [[SE-O-Iα-794_Portcullis_무너진_문](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-I%CE%B1-794_Portcullis_%EB%AC%B4%EB%84%88%EC%A7%84_%EB%AC%B8.md "SE-O-Iα-794_Portcullis_무너진_문.md")]
- `C-IIIγ-902` Beating Relic — `73568df` — PUSH VERIFIED — [[SE-C-IIIγ-902_Beating_Relic_고동치는_유물](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-902_Beating_Relic_%EA%B3%A0%EB%8F%99%EC%B9%98%EB%8A%94_%EC%9C%A0%EB%AC%BC.md "SE-C-IIIγ-902_Beating_Relic_고동치는_유물.md")]
- `C-IIβ-102` Frozen Tear — `433e096` — PUSH VERIFIED — [[SE-C-IIβ-102_Frozen_Tear_얼어붙은_눈물](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-102_Frozen_Tear_%EC%96%BC%EC%96%B4%EB%B6%99%EC%9D%80_%EB%88%88%EB%AC%BC.md "SE-C-IIβ-102_Frozen_Tear_얼어붙은_눈물.md")]
- `C-IIIγ-300` Memory Lock — `0783ef9` — PUSH VERIFIED — [[SE-C-IIIγ-300_Memory_Lock_기억의_자물쇠](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-300_Memory_Lock_%EA%B8%B0%EC%96%B5%EC%9D%98_%EC%9E%90%EB%AC%BC%EC%87%A0.md "SE-C-IIIγ-300_Memory_Lock_기억의_자물쇠.md")]
- `C-IVβ-041` The Grieving Maiden — `a4c81d2` — PUSH VERIFIED — [[SE-C-IVβ-041_The_Grieving_Maiden_슬픔의_처녀](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B2-041_The_Grieving_Maiden_%EC%8A%AC%ED%94%94%EC%9D%98_%EC%B2%98%EB%85%80.md "SE-C-IVβ-041_The_Grieving_Maiden_슬픔의_처녀.md")]
- `C-Iα-869` Homecoming Tree — `be95f5e` — PUSH VERIFIED — [[SE-C-Iα-869_Homecoming_Tree_돌아온_나무](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-I%CE%B1-869_Homecoming_Tree_%EB%8F%8C%EC%95%84%EC%98%A8_%EB%82%98%EB%AC%B4.md "SE-C-Iα-869_Homecoming_Tree_돌아온_나무.md")]
- `C-IVγ-240` Broken Clocktower — `73bd5cc` — PUSH VERIFIED — [[SE-C-IVγ-240_Broken_Clocktower_부서진_시계탑](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B3-240_Broken_Clocktower_%EB%B6%80%EC%84%9C%EC%A7%84_%EC%8B%9C%EA%B3%84%ED%83%91.md "SE-C-IVγ-240_Broken_Clocktower_부서진_시계탑.md")]
- `C-IVδ-505` Cold Burn — `b2526fd` — PUSH VERIFIED — [[SE-C-IVδ-505_Cold_Burn_얼어붙은_그림자](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-505_Cold_Burn_%EC%96%BC%EC%96%B4%EB%B6%99%EC%9D%80_%EA%B7%B8%EB%A6%BC%EC%9E%90.md "SE-C-IVδ-505_Cold_Burn_얼어붙은_그림자.md")]

| Counter | Open | Close |
|---|---|---|
| Couples in the plan (≥ 0.50 on either side) | 237 / 301 | **168 / 301** |
| Section-pairs over 0.50 | 263 | 186 |
| Files carrying a couple | 148 / 301 | 130 / 301 |
| Ties ≥ 0.70 | 29 / 237 | 17 / 168 |
| Ties 0.60–0.69 | 82 / 237 | 51 / 168 |
| Ties 0.50–0.59 | 126 / 237 | 100 / 168 |
| Files carrying a whole copied section | 0 / 301 | 0 / 301 |
| Stock-line residue (`verify.py`) | 1 / 301 | **0 / 301** |
| `R-29`, all five clauses | 301 / 301 | 301 / 301 |
| Personalization queue | 0 / 301 | 0 / 301 |
| Duplicate quote families | 0 / 301 | 0 / 301 |
| Distinct wing shingles (`sect.grams`, N=8, prose) | 1,444,290 | 1,447,005 (+2,715) |
| Words (the ten units) | 77,160 | 78,786 (+1,626) |
| Words (the wing) | 2,201,550 | 2,203,176 (+1,626) |

- **Per-file, in plain language** — Whispering Gallery: the hall's own cloth now carries the cells — the unbrushed nap, the weave that holds the hall's silence, the pair system logging the wearer's numbness, the observer making the call. Swallow: duration is the threat, the shadow's edge further across the floor each watch, logged unlike a stock event. Portcullis: threshold readings taken at the door and never inside the tunnel, the recitation and the gauge falling together, the leaf's grief breaching the bearer. Beating Relic: the stone on its plinth, the pulse rather than the blow, minutes of memory entered by the Armoury against the bearer, the edge going for the target's grief before the target. Frozen Tear: the sitter's own limit, the Tear drawing on the bearer at the minute, the direction changing at two. Memory Lock: the cold plate with no keyhole, the truthful admission, the whisper that reverses, the wanting arriving in the listener's own voice. Grieving Maiden: the room thickening around unshed tears, her grief arriving ahead of her voice, the sorrow that goes home with the worker. Homecoming Tree: Entry 1 opens on the class before the history and keeps every fact and figure, with the smell of cold rain arriving ahead of the Tree. Broken Clocktower: 3:47 throughout — the gears waking while the hands stay put, the six-metre field, Weight arriving behind the arm that swung it. Cold Burn: the vault approach, the lattice along the seam at knee height, the order that says until relieved, and the arbalest whose spool returns every bolt because nothing may be left on the floor.
- **Movement** — couples **237 → 168** (69 broken: u1 1 · u2 6 · u3 12 · u4 9 · u5 9 · u6 10 · u7 8 · u8 8 · u9 6); section-pairs 263 → 186; files carrying a couple 148 → 130 / 301. Every one of the ten files now measures **0 couples** against all 301. The batch added **+1,626** words and deleted nothing; the wing's own word delta is the same +1,626, which is the check that nothing outside the ten moved. Next rung, worst-first: Debt Scale `C-IIIβ-015` (6 couples) · Unrung `C-IIβ-170` (6) · Pyre of Truths `C-IVδ-092` (6) · Restless Gap `C-IVδ-250` (6) · Broken Tear `N-IVδ-517` (6); worst single tie in the wing Sleeping Tree `O-IIIγ-374` × Driftglass `O-IIIγ-914` at 0.77 (Tool Use Profile).
- **Probes** — close-time probe across all 301 dossiers: each of the ten units re-measured at **0 couples**, so no cross-unit echo survived the batch. Per-unit introduced-gram prechecks: u6 **14 echoes → 0** after rewording · u7 **3 → 0** · u8 **30 → 0** (27 of them against u6's own new lines) · u9 **9 → 0** (8 against u8's). From u8 on the precheck's comparison list holds the batch's already-shipped units as well as the target's partners; u1–u5 ran with the target alone in the list, which is exactly the gap the close-time probe covers. The shingles row is measured with `sect.grams` at both ends this turn; the b61 row used the older kit measure, so only this batch's movement (+2,715) is comparable, not the absolutes.
- **Residuals, disclosed** — the partners each unit was fixed against still carry their own **pre-existing** couples (Happy Mask 4 · Soaking Shard 5 · Blackened Angel 4 · Well of Unfinished Words 4 · Relic Waiting for Its Maker 4 · Sorrow Fountain 4 · Broken Clocktower's former partners 1–8). None were created by this batch; all are in the queue. Holdout `C-IIβ-240`, Empty Mask `C-IIβ-054` and Floating Well `C-IIIγ-448` were left at **0 couples** by the batch's work.
- **Disclosures** — rollbacks **#68, #69, #70, #71, #72** were recovered at turn opens with `tools/syncbranch.py` (stale `408797c` against remotes `5ab8ae0` / `433e096` / `0783ef9` / `73bd5cc` / `b2526fd`); nothing force-pushed, nothing deleted, no work lost. The kit's `/tmp` workspace clears between turns and was rebuilt four times. One gate refusal was the rebuilt runner passing `--file` to `wikistd.py`, which takes a bare path: the spec had already applied, the runner was patched, the gates were re-run, and the file was never re-applied. Unit 5 needed a second tightening pass inside its own unit (the Broken Fragment Core Stat Line still read 0.55 after the first nine replacements; three further lines brought it to 0).

**Batch 61 — CLOSED at seven; the fix phase begins: the partial-overlap queue worked worst-first, and pairs in the plan fall 261 → 237 / 301.**

Taken on the owner's go-ahead after Batch 60. With the whole-copy wave finished, the clone audit's `--plan` is now all partial pairs — sections at 0.50–0.85 on the higher side, no whole copies anywhere in the wing. The owner's method for this half (“Fix the lighter one … 1 to 3 small section similar to fix”) is the light side's small overlaps, edited **line by line in the file's own terms instead of block-replaced**; the rung of seven took the worst rows of the plan, one file per unit, growth-only (`R-15`), one push per unit (`A0`).

| # | Dossier | Code | Fixed in place | Words (before → after) |
|---|---|---|---|---|
| 1 | [[SE-C-IVδ-230_Every_Last_Goodbye_마지막_기억](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-230_Every_Last_Goodbye_%EB%A7%88%EC%A7%80%EB%A7%89_%EA%B8%B0%EC%96%B5.md "SE-C-IVδ-230_Every_Last_Goodbye_마지막_기억.md")] | `C-IVδ-230` | the stock Consequences quartet (0.85 / 0.81 vs `Aegis`) re-authored in the vault’s own terms | 8,398 → 8,462 |
| 2 | [[SE-C-IIβ-357_Carrying_Nothing_사라진_무게](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-357_Carrying_Nothing_%EC%82%AC%EB%9D%BC%EC%A7%84_%EB%AC%B4%EA%B2%8C.md "SE-C-IIβ-357_Carrying_Nothing_사라진_무게.md")] | `C-IIβ-357` | the same quartet, variant form (0.83 / 0.85 vs `Happy Mask`) in the emptied carrier’s own terms | 6,890 → 6,956 |
| 3 | [[SE-N-IVδ-927_Dreaming_Plague_꿈의_전염병](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-IV%CE%B4-927_Dreaming_Plague_%EA%BF%88%EC%9D%98_%EC%A0%84%EC%97%BC%EB%B3%91.md "SE-N-IVδ-927_Dreaming_Plague_꿈의_전염병.md")] | `N-IVδ-927` | the five-line Testimonium (0.83 / 0.83 vs `Dawn That Forgot`) re-voiced for the plague | 5,258 → 5,290 |
| 4 | [[SE-C-IIβ-330_Frozen_Window_얼어붙은_창](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-330_Frozen_Window_%EC%96%BC%EC%96%B4%EB%B6%99%EC%9D%80_%EC%B0%BD.md "SE-C-IIβ-330_Frozen_Window_얼어붙은_창.md")] | `C-IIβ-330` | the shared stat-table rows (0.82 vs `Masked Dancer`) extended in the Window’s own terms | 7,739 → 7,876 |
| 5 | [[SE-C-IIIγ-088_The_Sorrow_Fountain_슬픔의_분수](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-088_The_Sorrow_Fountain_%EC%8A%AC%ED%94%94%EC%9D%98_%EB%B6%84%EC%88%98.md "SE-C-IIIγ-088_The_Sorrow_Fountain_슬픔의_분수.md")] | `C-IIIγ-088` | the Registry Addendum (0.82 / 0.80 vs `Hollow Saint`): scaffold sentence, review clause and the digit run’s order restructured | 7,825 → 7,895 |
| 6 | [[SE-O-Iα-554_Fallow_녹슨_씨앗](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-I%CE%B1-554_Fallow_%EB%85%B9%EC%8A%A8_%EC%94%A8%EC%95%97.md "SE-O-Iα-554_Fallow_녹슨_씨앗.md")] | `O-Iα-554` | the relic-class Tool Use Profile and Log and Method rows (0.77 / 0.79 vs `Sleeping Tree`; 0.79 vs `Driftglass`) re-authored for the Seed | 6,218 → 6,290 |
| 7 | [[SE-C-IVδ-001_The_Orphaned_Bell_고아의_종](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-001_The_Orphaned_Bell_%EA%B3%A0%EC%95%84%EC%9D%98_%EC%A2%85.md "SE-C-IVδ-001_The_Orphaned_Bell_고아의_종.md")] | `C-IVδ-001` | the leveraged unit — suit cells, the second O-Relic block’s rows, five Method cells and the Consequences, **nine pairs at once** | 8,726 → 8,929 |

- `C-IVδ-230` Every Last Goodbye — `175351f` — PUSH VERIFIED — [[SE-C-IVδ-230_Every_Last_Goodbye_마지막_기억](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-230_Every_Last_Goodbye_%EB%A7%88%EC%A7%80%EB%A7%89_%EA%B8%B0%EC%96%B5.md "SE-C-IVδ-230_Every_Last_Goodbye_마지막_기억.md")]
- `C-IIβ-357` Carrying Nothing — `3f7eeef` — PUSH VERIFIED — [[SE-C-IIβ-357_Carrying_Nothing_사라진_무게](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-357_Carrying_Nothing_%EC%82%AC%EB%9D%BC%EC%A7%84_%EB%AC%B4%EA%B2%8C.md "SE-C-IIβ-357_Carrying_Nothing_사라진_무게.md")]
- `N-IVδ-927` Dreaming Plague — `6dbd828` — PUSH VERIFIED — [[SE-N-IVδ-927_Dreaming_Plague_꿈의_전염병](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-IV%CE%B4-927_Dreaming_Plague_%EA%BF%88%EC%9D%98_%EC%A0%84%EC%97%BC%EB%B3%91.md "SE-N-IVδ-927_Dreaming_Plague_꿈의_전염병.md")]
- `C-IIβ-330` Frozen Window — `b48e3f5` — PUSH VERIFIED — [[SE-C-IIβ-330_Frozen_Window_얼어붙은_창](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-II%CE%B2-330_Frozen_Window_%EC%96%BC%EC%96%B4%EB%B6%99%EC%9D%80_%EC%B0%BD.md "SE-C-IIβ-330_Frozen_Window_얼어붙은_창.md")]
- `C-IIIγ-088` Sorrow Fountain — `81e0184` — PUSH VERIFIED — [[SE-C-IIIγ-088_The_Sorrow_Fountain_슬픔의_분수](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-088_The_Sorrow_Fountain_%EC%8A%AC%ED%94%94%EC%9D%98_%EB%B6%84%EC%88%98.md "SE-C-IIIγ-088_The_Sorrow_Fountain_슬픔의_분수.md")]
- `O-Iα-554` Fallow — `da67025` — PUSH VERIFIED — [[SE-O-Iα-554_Fallow_녹슨_씨앗](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-I%CE%B1-554_Fallow_%EB%85%B9%EC%8A%A8_%EC%94%A8%EC%95%97.md "SE-O-Iα-554_Fallow_녹슨_씨앗.md")]
- `C-IVδ-001` Orphaned Bell — `0313fcd` — PUSH VERIFIED — [[SE-C-IVδ-001_The_Orphaned_Bell_고아의_종](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-001_The_Orphaned_Bell_%EA%B3%A0%EC%95%84%EC%9D%98_%EC%A2%85.md "SE-C-IVδ-001_The_Orphaned_Bell_고아의_종.md")]

| Counter | Open | Close |
|---|---|---|
| Pairs in the plan (`--plan`, ≥ 0.50 on either side) | 261 / 301 | **237 / 301** |
| Heavy sides (the side to clean) | 103 / 301 | 97 / 301 |
| Light sides (the side to fix) | 119 / 301 | 115 / 301 |
| Files appearing in any ≥ 0.50 pair | — | 148 / 301 (first measurement under this counter) |
| Files carrying a whole copied section | 0 / 301 | 0 / 301 |
| R-29 (all five clauses) | 301 / 301 | 301 / 301 |
| Personalization queue | 0 / 301 | 0 / 301 |
| Stock-line residue | 1 / 301 | 1 / 301 (Homecoming Tree held) |
| Distinct wing shingles | 726,825 | 727,293 |
| Words (the seven) | 51,054 | 51,698 (+644) |

- **Per-file, in plain language** — Every Last Goodbye: the four consequences are the vault’s own now — endings held that were never the worker’s to hold, the showing that will not stop with the wave, the price collected in leave-takings. Carrying Nothing: the same four in the carrier’s terms — the cost that appears in no schedule, and the one departure in the file that carries a stated reason. Dreaming Plague: a testimony that knows the difference between the void and a void caught off somebody else’s sleep. Frozen Window: its stat rows now say what the holding actually grades (viewing time), and that the figure can be destroyed without ending the departure. Sorrow Fountain: grief with somewhere to move, a pool that has never held the same water twice, and the registry’s digits in the pool’s own order. Fallow: the relic-class rows in the Seed’s own terms — answers to skin, the creeper line surveyed to prove it let go, the blue kept at the skin for days. Orphaned Bell: the suit, the O-Relic block, the five Method cells and the consequences all in the bell’s own register — names said back, the toll that will not wait for the next watch.
- **Movement** — pairs **261 → 237** (24 broken); heavy sides 103 → 97; light sides 119 → 115. Every unit grew; the batch added **+644** words and deleted nothing. The next rung, worst-first from the plan: `Memory Lock` `C-IIIγ-300` (10 pair(s)), `Beating Relic` `C-IIIγ-902` (9), `Happy Mask` `C-IIβ-051` (6), `Unrung` `C-IIβ-170` (6), `Pyre of Truths` `C-IVδ-092` (6).
- **Probes** — introduced-gram probe across all 301 dossiers: 80 single-gram incidences at x4 or below, every one on a canonical or stock fragment (the R.D. Comprehension line, “a M.A.W. is never costless”, the registry digit bullet) — **0 new pairs at ≥ 0.50**; family check 0 / 0. `precheck.py` 0 before every push.
- **Residuals, disclosed** — the seven files each still carry 1–4 **pre-existing** partial pairs, none of them created by this batch and all next in the queue: Carrying Nothing × Double Mouth (0.71), × Collapsed Whisper (0.61), × Pyre of Truths (0.53), × Welcome Haven (0.51); Sorrow Fountain × Soaking Shard (0.61), × Memory Lock (0.57), × Well of Unfinished Words (0.56), × Broken Clocktower (0.55), × Blackened Angel (0.54), × Relic Waiting for Its Maker (0.51); Dreaming Plague × Weighted Silence (0.59); Every Last Goodbye × Memory Lock (0.55) and × Walking Calendar (0.54); Fallow × Shard of a Broken Promise (0.55).
- **Disclosures** — rollback **#66** recovered at the open (`tools/syncbranch.py`: stale `408797c` against remote `7d25b30`; now level, nothing force-pushed, no deletions). Unit 5 needed two repair passes inside its own unit before its push: the first pass left the pair at 0.54 / 0.61 because the scaffold sentences and the digit run still carried the Saint’s shape (fixed by restructuring both), and the second draft came out net-negative (R-15) and was re-worded to a positive delta before anything was pushed. Frozen Window’s `Starting Sorrow Gauge` row occurs twice in that file (SECC and the operational table); the two were re-authored as a single scoped replacement. The Orphaned Bell carries two `Tool Use Profile — O-Relic` blocks; the audit reads the later one, and its rows were the ones re-authored.

**Batch 60 — CLOSED at seven; the clone clean-first wave completed: files carrying a whole copied section 7 → 0 / 301.**

Taken on the owner's go-ahead after Batch 59. The seven dossiers named at the b59 close as the remaining whole-copy files were worked worst-first, each copied block **replaced in place** in the file's own terms, growth-only (`R-15`), one push per unit (`A0`) — the b44 clean-phase method, with the lineage rule applied (where a pair is mutual, the lower designation holds the source and the higher is the copy cleaned: `Dancing Chains` `C-IIIγ-102` holds the `Redcage` `C-IIIγ-120` Core Stat Line).

| # | Dossier | Code | Cleaned in place | Words (before → after) |
|---|---|---|---|---|
| 1 | [[SE-C-IIIγ-120_Redcage_분노의_감옥](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-120_Redcage_%EB%B6%84%EB%85%B8%EC%9D%98_%EA%B0%90%EC%98%A5.md "SE-C-IIIγ-120_Redcage_분노의_감옥.md")] | `C-IIIγ-120` | the copied Core Stat Line rows (1.00 / 0.96 vs `Dancing Chains`) re-authored in the Cage’s own terms | 7,943 → 8,110 |
| 2 | [[SE-C-IIIγ-902_Beating_Relic_고동치는_유물](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-902_Beating_Relic_%EA%B3%A0%EB%8F%99%EC%B9%98%EB%8A%94_%EC%9C%A0%EB%AC%BC.md "SE-C-IIIγ-902_Beating_Relic_고동치는_유물.md")] | `C-IIIγ-902` | the copied Combat Actions table (0.87 vs `Hatred Above`) re-voiced as the relic’s own | 6,141 → 6,205 |
| 3 | [[SE-C-IVδ-255_Rising_Wall_솟아오른_벽](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-255_Rising_Wall_%EC%86%9F%EC%95%84%EC%98%A4%EB%A5%B8_%EB%B2%BD.md "SE-C-IVδ-255_Rising_Wall_솟아오른_벽.md")] | `C-IVδ-255` | the copied Breach Behavior rows (0.86 vs `Broken Tear`) in the Wall’s own terms | 7,987 → 8,072 |
| 4 | [[SE-C-IVδ-763_Memorial_Flame_Mid-Ceremony_사라진_불꽃](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-763_Memorial_Flame_Mid-Ceremony_%EC%82%AC%EB%9D%BC%EC%A7%84_%EB%B6%88%EA%BD%83.md "SE-C-IVδ-763_Memorial_Flame_Mid-Ceremony_사라진_불꽃.md")] | `C-IVδ-763` | the copied Consequences bullets (0.89 vs `Memory Thief`) as the interrupted vigil’s own | 7,393 → 7,475 |
| 5 | [[SE-C-IVδ-922_Miasma_우는_안개](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-922_Miasma_%EC%9A%B0%EB%8A%94_%EC%95%88%EA%B0%9C.md "SE-C-IVδ-922_Miasma_우는_안개.md")] | `C-IVδ-922` | the copied Combat Actions table (0.87 vs `Allhallow`) re-voiced as the bank’s own; the breach quote’s doubled word repaired | 5,223 → 5,325 |
| 6 | [[SE-N-IIIβ-941_Grieving_Love_슬픈_사랑](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-III%CE%B2-941_Grieving_Love_%EC%8A%AC%ED%94%88_%EC%82%AC%EB%9E%91.md "SE-N-IIIβ-941_Grieving_Love_슬픈_사랑.md")] | `N-IIIβ-941` | the copied Breach Behavior rows (0.86 vs `Calling Bloom`) in her own terms | 6,646 → 6,710 |
| 7 | [[SE-O-IVδ-190_Ember_Phoenix_불사조](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-IV%CE%B4-190_Ember_Phoenix_%EB%B6%88%EC%82%AC%EC%A1%B0.md "SE-O-IVδ-190_Ember_Phoenix_불사조.md")] | `O-IVδ-190` | the copied SECC row set (0.86 vs `Wrath Flame`), both `Coherence` rows | 7,671 → 7,788 |

- `C-IIIγ-120` Redcage — `b3e194e` — PUSH VERIFIED — [[SE-C-IIIγ-120_Redcage_분노의_감옥](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-120_Redcage_%EB%B6%84%EB%85%B8%EC%9D%98_%EA%B0%90%EC%98%A5.md "SE-C-IIIγ-120_Redcage_분노의_감옥.md")]
- `C-IIIγ-902` Beating Relic — `3a0c40e` — PUSH VERIFIED — [[SE-C-IIIγ-902_Beating_Relic_고동치는_유물](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-III%CE%B3-902_Beating_Relic_%EA%B3%A0%EB%8F%99%EC%B9%98%EB%8A%94_%EC%9C%A0%EB%AC%BC.md "SE-C-IIIγ-902_Beating_Relic_고동치는_유물.md")]
- `C-IVδ-255` Rising Wall — `46de386` — PUSH VERIFIED — [[SE-C-IVδ-255_Rising_Wall_솟아오른_벽](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-255_Rising_Wall_%EC%86%9F%EC%95%84%EC%98%A4%EB%A5%B8_%EB%B2%BD.md "SE-C-IVδ-255_Rising_Wall_솟아오른_벽.md")]
- `C-IVδ-763` Memorial Flame — `752fa04` — PUSH VERIFIED — [[SE-C-IVδ-763_Memorial_Flame_Mid-Ceremony_사라진_불꽃](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-763_Memorial_Flame_Mid-Ceremony_%EC%82%AC%EB%9D%BC%EC%A7%84_%EB%B6%88%EA%BD%83.md "SE-C-IVδ-763_Memorial_Flame_Mid-Ceremony_사라진_불꽃.md")]
- `C-IVδ-922` Miasma — `58b2156` — PUSH VERIFIED — [[SE-C-IVδ-922_Miasma_우는_안개](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-922_Miasma_%EC%9A%B0%EB%8A%94_%EC%95%88%EA%B0%9C.md "SE-C-IVδ-922_Miasma_우는_안개.md")]
- `C-IVδ-922` Miasma (u5 fix) — `7245f8d` — PUSH VERIFIED — [[SE-C-IVδ-922_Miasma_우는_안개](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-C-IV%CE%B4-922_Miasma_%EC%9A%B0%EB%8A%94_%EC%95%88%EA%B0%9C.md "SE-C-IVδ-922_Miasma_우는_안개.md")]
- `N-IIIβ-941` Grieving Love — `cbfbbf7` — PUSH VERIFIED — [[SE-N-IIIβ-941_Grieving_Love_슬픈_사랑](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-N-III%CE%B2-941_Grieving_Love_%EC%8A%AC%ED%94%88_%EC%82%AC%EB%9E%91.md "SE-N-IIIβ-941_Grieving_Love_슬픈_사랑.md")]
- `O-IVδ-190` Ember Phoenix — `f4785ac` — PUSH VERIFIED — [[SE-O-IVδ-190_Ember_Phoenix_불사조](https://github.com/Redditor008/PROJECT.SOMNARAK-WIKI/blob/arena/01a10bcc-project-somnarak-wiki/SOMNARAK-WORLD/Sorrow_Entities/SE-O-IV%CE%B4-190_Ember_Phoenix_%EB%B6%88%EC%82%AC%EC%A1%B0.md "SE-O-IVδ-190_Ember_Phoenix_불사조.md")]

| Counter | Open | Close |
|---|---|---|
| Files carrying ≥ 1 whole copied section (copy direction) | 7 / 301 | **0 / 301** |
| Files appearing in any ≥ 0.85 section pair | 14 / 301 | **0 / 301** |
| R-29 (all five clauses) | 301 / 301 | 301 / 301 |
| Personalization queue | 0 / 301 | 0 / 301 |
| Stock-line residue | 1 / 301 | 1 / 301 (Homecoming Tree held) |
| Distinct wing shingles | 726,700 | 726,825 |
| Words (the seven) | 49,004 | 49,685 (+681) |

- **Per-file, in plain language** — Redcage: its counted rows are now the Cage’s own — the case being argued through the bars, the wave taken off it, the injustice read aloud, neither side stepping past the bars. Beating Relic: the four moves are the stone’s own — the warmth before the hand, the second heart, the clenched certainty, the open hand. Rising Wall: its breach rows describe the cold coming off the Wall and the marks the cordon works to, not a borrowed wail. Memorial Flame: the Consequences are the interrupted vigil’s — detail attached to a grief the worker cannot claim. Miasma: the four moves are the bank’s own — the roll-in, the particulars, the filling run, the whole flood. Grieving Love: her breach rows are hers — the arms held out, the invitation that reads as kindness, the cure that takes the parts. Ember Phoenix: its SECC rows are the Phoenix’s own, both `Coherence` rows, in the classification and in the operational record alike.
- **Movement** — whole-copy files **7 → 0 / 301**, and with them the whole ≥ 0.85 structure: files appearing in any ≥ 0.85 section pair **14 → 0 / 301**. No section in the wing now measures ≥ 0.85 against any other. Every unit grew; the batch added **+681** words and deleted nothing. The fix-later set is now the sub-0.85 partial overlaps, worst-first: Memory Lock `C-IIIγ-300` (11 pairs), Beating Relic (9), Happy Mask `C-IIβ-051` (7), Pyre of Truths `C-IVδ-092` (7).
- **Probes** — `bnew.py`: **0** introduced-on-both-sides families, **0** introduced-once echoes. After cleaning, every one of the seven files measures < 0.85 on every section it shares with the corpus (highest remaining partial: Redcage 0.39 toward Dancing Chains’ Core Stat Line stub; all others ≤ 0.23).
- **Disclosures** — rollback **#65** recovered at the open (`tools/syncbranch.py`: stale `408797c` against remote `78b450e`, 267 files nominal; now level, nothing force-pushed, no deletions). One cross-unit echo inside the batch: u5’s trigger junction echoed the batch’s own damage/trigger frame across three batch files and was re-worded on the later side (`7245f8d`; `precheck.py` re-run at 0 before that push). Miasma’s breach quote carried the generator’s doubled word (“The lament lament spreads”, byte-identical with `Allhallow`) and was repaired inside u5. Ember Phoenix’s `Coherence` row occurs twice (SECC and R.D. Operational Record); both were re-authored, the second anchored sequentially. The b59 disclosure is closed out: the `Dancing Chains` × `Redcage` Core Stat Line pair now measures **0.05 / 0.39**.


## Workstream 8 — Breach Balance (`R-28`, done 2026-10-05)

The archive declared **285 of 302 entities capable of breaching**. It was generator output, not a
finding: **72 of the 83 relic dossiers had no Breach Behavior section at all** — an Activation
Behavior section, a Stationary movement row — and still read *Can breach via Transform*.

**112 dossiers reclassified non-breaching**, each on its own evidence, under the categories the
archive already had: activation only, corruption of its own zone, expansion in place, manifestation
in place, transformation in place. Nothing with a `Breach type: Escape` was touched.

| Group | Total | Non-breaching | Share | Floor |
|---|---|---|---|---|
| RE — relics (a Tool Type is declared) | 83 | 63 | 75.9% | ≥ 75% |
| SE — Subject / Time / Hazard / Phenomenon | 178 | 45 | 25.3% | ≥ 25% |
| OP — Object/Place, no Tool Type | 41 | 21 | 51.2% | ≥ 50% |

**The reclassification was carried through every dependent section**, on the owner's instruction:
Behavior, Combat Record and Actions, Operational Notes and Work Notes, Escalation Notes,
Consequences, M.A.W. Use Notes, Field Use Record, Observation Log, Registry Addendum and the Entity
Interaction Record. 716 breach-asserting lines were found in the 112 files; three passes cleared
them, the `## Breach Behavior` heading became `## Containment Event Behavior` in the 36 files that
had one, and the sampler that parses on that boundary was taught both names. Five lines remain and
are correct: they state the entity expands *rather than* escaping.

Qualifying candidates outnumbered the quota in every group (RE 72, SE 65, OP 34), so no dossier had
to be stretched to reach a floor. Inside each converted file the `Breach type` line became
`Event type (non-breach)` and prose claiming a breach capability was corrected; 37 files needed that
second pass. `tools/breach.py` is wired into `gate.sh` and refuses a commit that drops a group below
its floor.

## Workstream 5 — Entity Disposition Index: CLOSED (2026-10-05)

**302 / 302 entity dossiers classified, 0 pending.** The last three were Grasp `O-IVδ-762` (Neutral),
Once Told `O-IVδ-930` (Neutral) and Dawn of Mourning `C-Vω-002` (**Negative** — Breach `Secondary
Effect` raises every other holding's gauge 10% a turn and `First Target` inverts Hope Bearers, which
is the `R-19` Negative mechanism on both limbs).

Three corrections were made at closure and they matter more than the last three rows:

1. **The denominator was wrong.** The index counted against 303 catalogued files, but one of them —
   `Book_of_Regressor_Log_Dramaturgy.md` — is a side-story log with no SECC code and no mechanics.
   It can never carry a disposition. It is now declared out of scope and the denominator is 302.
2. **Ten entities had two rows each**, written in different batches, all in the Neutral section. The
   old counter counted rows rather than distinct codes, so it read 300 when 299 entities were
   covered. The thinner row of each pair was removed and the counter now counts codes.
3. **The tooling now lives in the repository.** `verify.py`, `disp.py` and `gate.sh` had been kept
   outside the repo and were lost when the sandbox reset; everything they had produced survived in
   the working tree, but the tools themselves did not. They have been rebuilt in `tools/` and
   `gate.sh` now fails the commit on an unclosed table row — the check that silently passed three
   times during the `R-25` batches.

## Workstream 7 — The Reset Pass (PLANNED, not started)

**Instructed by the archive owner, 2026-10-05:** *"Later do a reset fixed based the two re-research."*
Scheduled deliberately for later and recorded here now so that the sequencing is not lost.

**What it is.** A single archive-wide pass that re-fixes every dossier against **both** measures at
once, replacing the current one-entity-at-a-time progress:

1. **`tpl.py` — template residue** (`R-23`): a line shared by ten or more dossiers that is not
   sanctioned furniture. Labels may repeat; values may not.
2. **`sect.py` — the Tale standard** (`R-24`): prose generic fraction ≤ 0.05, furniture excluded,
   measured against the one section of the archive that already reads as written rather than
   generated.

**Why it waits.** Three things have to be true before a reset is worth running, and two of them are
not yet:

- The measures must be stable. `sect.py` was recalibrated once already, on its first real use, and a
  reset built on a metric that is still moving would have to be run twice.
- The per-entity method must be proven across enough shapes of dossier. Five are done; the Object,
  Place, Time and Hazard roles each carry a different stock skeleton and at least one of each should
  be finished by hand before the pattern is generalised.
- The rewrite must stay authored. `R-15` growth-only and `R-05` no-paraphrase both still bind: the
  reset is a schedule for doing the work in one sweep, **not** a licence to generate replacement
  text mechanically. A reset that produced a new shared skeleton would simply move the defect.

**Shape it will take when it runs.** Worst-first by `sect.py --files`, one commit per dossier, both
checkers to zero plus the prose measure under 0.05 before the commit, and a disposition row in the
same commit wherever the dossier is still pending — which is what the last five have done.

## Workstream 2 — Unfinished text (closed on both scans)

**391 breaks completed.** 312 that ended a line, and 79 more that did not — cut mid-clause with another fragment fused on after the break, so the line ended on a full stop and read as finished. Both scans now return zero. Detail in `UNFINISHED_TEXT_REGISTER.md`.

26 mid-line ellipses remain and are deliberate: dramatic pauses in dialogue and testimony. They were each read before being left alone.

Two defects here were invisible to the scan written for them — thirty `| **Form** |` cells cut at 150 characters with no mark, and these 79. Both were found by reading a file, not by scanning the archive.

## Workstream 4 — Splice seams (queued, not started)

Six shared instruction paragraphs carry a dangling fragment left over from a splice — a clause repeated at the end of a sentence that had already said it.

| Fragment | Field it sits in | Files |
|---|---|---|
| `such as "strange" or "anomalous."` | Appearance protocol | 204 |
| `to repeat;` | Interaction method | 209 |
| trailing `alone.` | Observation method | 281 |
| `. before Work or contact.` | Identification cell | 223 |
| `. a Sorrow Tide, breach, Ordeal, or transformation event.` | Interaction method | 204 |
| `....` | various | 24 |

These are **not** batchable, by `R-18`. The broken grammar is currently the only visible mark on paragraphs that are boilerplate underneath; repairing the grammar across all of them at once would clear the tell and leave the boilerplate. All six fields are already on the per-file rewrite list, so Workstream 1 retires them as it goes. The census is kept here so the scale is not forgotten.

## Workstream 3 — Rules (standing)

`RULES/` holds one file per standing rule. A rule is written there the moment it is stated. Nothing is kept only in conversation.

## Deliberately untouched

- `REGISTRY_MASTER_STATUS.md` lines 324 and 330.
- `**Entry 1 — Containment Description**`, present in 256 files: structural, ruled out of scope.
- Entry numbering across Story Logs: structural furniture, kept (`R-10`).

## Standing blemishes in pushed history

Not repaired, because history is not rewritten (`R-17`).

- A commit message reading `48->??`.
- A commit pushed with two open `label_lint` violations, fixed in a later commit.
- A commit message reading `45->10` where the measured figure was 9.
- The Memory Chain commit message reads `6,601 -> 6,613`; the measured figures were 6,613 -> 6,624.
- The Final Door, Forgotten God and Convergence commit messages say "nothing new invented" and "restated in digits", which is accurate, and describe the units as closing the series clause; the clause was failing on a counting convention, as the measurement finding above says.
- The Torn Window commit message calls it "the worst section on the Study 01 league table when this campaign began". It was the worst *file* on Study 01's table (0.293 generic fraction), at the time Study 01 was written.
- The first R-01 conversions for The Debtor (`a0d4308`) and Broken Clock (`3994646`) each added an inference the file does not state; replaced in `4ff03eb` and `545204c`.
- The Sorrow Tide commit message says "no word was turned into a digit". The new Observation Log bullets do state, in digits, figures that other sections of the file give in words (nine stations, eleven minutes, sixty years). Nothing was invented, but the sentence was too strong.
- The Foam Flood and Soot Fry commit messages describe the stock opener as carried by many dossiers. The exact first sentence ("does not exist in total isolation") was in those two files only; the shared part was the third sentence, which 127 dossiers still carry.
- **The Black River commit message (`2c6ec93`) says `8,048 -> 8,708 words`; the measured figures were 8,048 -> 9,018.** The starting figure was taken correctly and the end figure was not re-measured before the message was written. Recorded here rather than amended (`R-17`: history is not rewritten). The Sorrow Storm message's figures (8,291 -> 9,209) were re-measured against `git show HEAD:` before it was written and are correct.

## Traps that have cost time

- Local git history truncates between turns. `git fetch` + `git reset --mixed FETCH_HEAD` runs first in every commit block.
- `label_lint.py` exits 0 while printing violations.
- `set -e` does not abort on a failing left-hand side of `&&`.
- Two cleaner patterns sharing an opening fragment will eat each other; the assert catches it and aborts before writing.
- Changing a Story Log entry tag without changing the entry under it leaves the document claiming to be one thing and reading as another. Caught in Forgotten Silence after the tag was rewritten and the paragraph was not.
- Replacing a whole Story Log entry leaves the original `**Entry N — <…>**` header standing above the replacement, so the file briefly carries two. No tool flags it; `grep -n` the entry header after any Story-Log rewrite (Broken Whisper, batch 4, 2026-10-05).
- An entity code appended inside an interaction row's bold label (`| **The Lost Prince `C-IVγ-091`** |`) trips `label_lint.py` with `LABEL_NOT_ALLOWED`, and `gate.sh` blocks before committing. Put the code in the row's other columns, as plain text or backticked (The Vanished Rope, batch 5, 2026-10-05).
- Measuring on a hand-rolled line scan gives the wrong population. Use `br.collect`.
- A branch name written into a script outlives the session it belonged to. `gate.sh` had one; it now reads the checked-out branch.
- A helper kept outside the repository is lost on a sandbox reset. `dirtylines.py` lives in `tools/` for that reason.
- Two replacements written to cure the same slot-filled line must not be parallel templates; that reintroduces the defect one level up. Vary structure and focus (Foam Flood and Soot Fry).
- A key taken from the first match inside a file can differ from the key the index uses; match on the filename code.
- **`gh pr edit` does not apply here.** It exits 1 with `GraphQL: Projects (classic) is being deprecated in favor of the new Projects experience` and leaves the body untouched, while still looking like an attempted edit in the console. The previous turn's note that PR #13's body "carries all eight units" was therefore wrong. Set a body with `gh api -X PATCH repos/Redditor008/PROJECT.SOMNARAK-WIKI/pulls/<n> -F body=@<file> --jq '.number, .state'` and verify by grepping the result of `gh pr view <n> --json body -q .body`. The body now carries all nine units, checked that way.

