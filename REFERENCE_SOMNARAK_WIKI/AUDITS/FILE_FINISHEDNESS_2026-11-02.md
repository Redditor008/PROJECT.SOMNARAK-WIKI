# File finishedness — every file, measured

**Measured:** 2026-11-02 · **files:** 2,343 · **mean:** 99.3% · **median:** 100.0%

## What this number is

A file's percentage is **the share of its filed obligations it meets**. The obligations are not
opinions: they are the sections its template requires, the fields its own class carries in
90%+ of its members, the debts already on the record (the `Maximum Amount` gap, the
filename/H1 mismatch, the corrosion-prose debt), and the defect classes the linters police
(scaffold braces, split compounds, banned wording).

**It is not a judgement of writing quality.** A dossier at 100% meets every structural
obligation that can be checked mechanically; that is all it means. Nothing here reads for
meaning, and a 100% file is not a good file — it is a file with nothing missing from its
checklist.

The rubric is in `tools/finishedness.py`; every file's missing obligations are printed in the
CSV beside it, so any score can be argued with.

## By class

| Class | Files | Mean | Median | Complete ≥95% | Near 85–95% | Substantial 70–85% | Partial 50–70% | Thin <50% |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `maw-record` | 852 | 98.6% | 100.0% | 722 | 129 | 1 | 0 | 0 |
| `world-other` | 581 | 99.9% | 100.0% | 579 | 0 | 2 | 0 | 0 |
| `reference` | 469 | 99.1% | 100.0% | 443 | 0 | 26 | 0 | 0 |
| `se-dossier` | 290 | 99.8% | 100.0% | 285 | 5 | 0 | 0 | 0 |
| `root-doc` | 64 | 99.5% | 100.0% | 63 | 0 | 0 | 1 | 0 |
| `codex` | 45 | 100.0% | 100.0% | 45 | 0 | 0 | 0 | 0 |
| `template` | 42 | 100.0% | 100.0% | 42 | 0 | 0 | 0 | 0 |

## By wing

| Wing | Files | Mean | Median |
|---|---:|---:|---:|
| `SOMNARAK-WORLD/MAW_Codex_Sets` | 1,209 | 99.0% | 100.0% |
| `REFERENCE_SOMNARAK_WIKI` | 469 | 99.1% | 100.0% |
| `SOMNARAK-WORLD/Sorrow_Entities` | 291 | 99.8% | 100.0% |
| `SOMNARAK-WORLD/Ordeals` | 61 | 100.0% | 100.0% |
| `SOMNARAK-WORLD/Master_Codices` | 45 | 100.0% | 100.0% |
| `SOMNARAK-WORLD/Pages` | 44 | 100.0% | 100.0% |
| `TEMPLATES` | 42 | 100.0% | 100.0% |
| `PROJECT_MOON_RESEARCH` | 29 | 100.0% | 100.0% |
| `SOMNARAK-WORLD/Echo_Cores` | 21 | 100.0% | 100.0% |
| `GAME_BATTLE` | 18 | 100.0% | 100.0% |
| `SOMNARAK-WORLD/Hope_Transformations` | 15 | 100.0% | 100.0% |
| `SOMNARAK-WORLD/Unknown_Entities` | 13 | 98.7% | 100.0% |
| `SOMNARAK-WORLD/The_Absolvohan` | 11 | 100.0% | 100.0% |
| `CANON` | 10 | 96.7% | 100.0% |
| `SOMNARAK-WORLD/Gieok_Jeojangso` | 9 | 100.0% | 100.0% |
| `SOMNARAK-WORLD/Katabagil` | 9 | 100.0% | 100.0% |
| `SOMNARAK-WORLD/Jipyeongseondae` | 8 | 100.0% | 100.0% |
| `SOMNARAK-WORLD/Katharcheok` | 8 | 100.0% | 100.0% |
| `SOMNARAK-WORLD/Story_Cantos` | 7 | 100.0% | 100.0% |
| `SOMNARAK-WORLD/Mugenhan_Ecology` | 6 | 100.0% | 100.0% |
| `SOMNARAK-WORLD/Nareumhan` | 6 | 100.0% | 100.0% |
| `(root)` | 3 | 100.0% | 100.0% |
| `SOMNARAK-WORLD/Tactical_Combat_Engine` | 3 | 100.0% | 100.0% |
| `SOMNARAK-WORLD/` | 2 | 100.0% | 100.0% |
| `docs` | 2 | 100.0% | 100.0% |
| `tools` | 2 | 100.0% | 100.0% |

## Where the missing share actually is


| Obligation | Files missing it | What it means |
|---|---:|---|
| `h1_match` | 125 | The H1 does not carry the subject the filename names. |
| `sections` | 29 | No second-level section — short index pages and stubs. |
| `max_amount` | 6 | No stock ceiling filed — no `Maximum Amount` row, no `Maximum / Echo Cost` column, no inline `max N`. |
| `observation_log` | 3 | The 관찰 기록 section is under 40 words. |
| `operational_fields` | 2 | An Operational Parameters field is empty. |
| `h1` | 1 | No H1 at all. |
| `nine_headings` | 1 | Missing one of the nine required dossier sections. |
| `story_log` | 1 | No numbered entry under 이야기 보고. |

## The M.A.W. registry, block by block

| Registry block | Files | Mean | Median |
|---|---:|---:|---:|
| Registry 185–195 | 21 | 96.1% | 100.0% |
| Registry 016–031 | 21 | 97.0% | 100.0% |
| Registry 170–184 | 21 | 97.0% | 100.0% |
| Registry 077–092 | 21 | 97.4% | 100.0% |
| Registry 099–103 | 21 | 97.4% | 100.0% |
| Registry 130–150 | 21 | 97.4% | 100.0% |
| Registry 339–371 | 21 | 97.4% | 100.0% |
| Registry 009–015 | 21 | 97.8% | 100.0% |
| Registry 119–127 | 21 | 97.8% | 100.0% |
| Registry 001–007 | 21 | 98.3% | 100.0% |
| Registry 032–042 | 21 | 98.3% | 100.0% |
| Registry 200–219 | 21 | 98.3% | 100.0% |
| Registry 762–801 | 53 | 98.3% | 100.0% |
| Registry 821–852 | 29 | 98.4% | 100.0% |
| Registry 863–897 | 29 | 98.4% | 100.0% |
| Registry 105–115 | 21 | 98.7% | 100.0% |
| Registry 151–157 | 21 | 98.7% | 100.0% |
| Registry 159–169 | 21 | 98.7% | 100.0% |
| Registry 315–330 | 21 | 98.7% | 100.0% |
| Registry 622–641 | 21 | 98.7% | 100.0% |
| Registry 265–285 | 22 | 98.8% | 100.0% |
| Registry 993–997 | 9 | 99.0% | 100.0% |
| Registry 716–757 | 21 | 99.2% | 100.0% |
| Registry 941–976 | 49 | 99.3% | 100.0% |
| Registry 043–055 | 25 | 99.3% | 100.0% |
| Registry 900–930 | 125 | 99.5% | 100.0% |
| Registry 1001–1043 | 173 | 99.5% | 100.0% |
| Registry 061–073 | 21 | 99.6% | 100.0% |
| unfiled | 31 | 100.0% | 100.0% |
| Registry 220–233 | 21 | 100.0% | 100.0% |
| Registry 235–247 | 21 | 100.0% | 100.0% |
| Registry 249–260 | 21 | 100.0% | 100.0% |
| Registry 290–310 | 21 | 100.0% | 100.0% |
| Registry 373–407 | 21 | 100.0% | 100.0% |
| Registry 409–453 | 21 | 100.0% | 100.0% |
| Registry 456–488 | 21 | 100.0% | 100.0% |
| Registry 489–519 | 25 | 100.0% | 100.0% |
| Registry 525–559 | 17 | 100.0% | 100.0% |
| Registry 560–585 | 13 | 100.0% | 100.0% |
| Registry 589–617 | 21 | 100.0% | 100.0% |
| Registry 643–677 | 21 | 100.0% | 100.0% |
| Registry 683–709 | 21 | 100.0% | 100.0% |

## The stock-ceiling debt, stated precisely

The standing figure was *199 filed / 653 blank*. Re-measured with a wider definition — the row,
the weapon/suit `Maximum / Echo Cost` column, and the compact inline `max N` all count as a
filing — the number is **846 of 852 filed, 6 not filed**
(weapons 284/284, suits 284/284, stigmas 278/284).

The difference is not a correction of the old figure — it is a correction of what counts. The
old count read only the explicit `Maximum Amount` label. **The stigma finding stands exactly as
recorded: 278 of 284 stigmas file a stock ceiling, because the Stigma schema has the field nowhere.**

## Lowest-scoring files

| File | Score | Missing |
|---|---:|---|
| `CANON/INTEGRITY_AND_LORE_REVIEW.md` | 66.7% | h1 sections |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_185_to_195/190_Rage_Statue/SE-190-D__MAW-G_The_Rage_Charm.md` | 81.8% | max_amount h1_match |
| `REFERENCE_SOMNARAK_WIKI/RULES/R-14_WHAT_BOILERPLATE_IS.md` | 83.3% | sections |
| `REFERENCE_SOMNARAK_WIKI/RULES/R-15_CLEAN_FIX_VERIFICATION.md` | 83.3% | sections |
| `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B184_CLOSE.md` | 83.3% | sections |
| `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B185_CLOSE.md` | 83.3% | sections |
| `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B186_CLOSE.md` | 83.3% | sections |
| `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B187_CLOSE.md` | 83.3% | sections |
| `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B188_CLOSE.md` | 83.3% | sections |
| `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B189_CLOSE.md` | 83.3% | sections |
| `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B190_CLOSE.md` | 83.3% | sections |
| `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B191_CLOSE.md` | 83.3% | sections |
| `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B192_CLOSE.md` | 83.3% | sections |
| `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B193_CLOSE.md` | 83.3% | sections |
| `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B194_CLOSE.md` | 83.3% | sections |
| `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B195_CLOSE.md` | 83.3% | sections |
| `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B196_CLOSE.md` | 83.3% | sections |
| `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B197_CLOSE.md` | 83.3% | sections |
| `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B198_CLOSE.md` | 83.3% | sections |
| `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B199_CLOSE.md` | 83.3% | sections |
| `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B200_CLOSE.md` | 83.3% | sections |
| `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B201_CLOSE.md` | 83.3% | sections |
| `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B202_CLOSE.md` | 83.3% | sections |
| `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B203_CLOSE.md` | 83.3% | sections |
| `REFERENCE_SOMNARAK_WIKI/SE_APPEARANCE_REVIEWS/B204_CLOSE.md` | 83.3% | sections |

## Reproduce

```bash
python3 tools/finishedness.py                      # summary
python3 tools/finishedness.py --worst 25           # lowest files
python3 tools/finishedness.py --csv out.csv        # every file, every missing key
```

