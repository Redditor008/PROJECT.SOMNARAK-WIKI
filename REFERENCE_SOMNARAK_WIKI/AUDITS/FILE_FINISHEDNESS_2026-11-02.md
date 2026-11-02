# File finishedness — every file, measured

**Measured:** 2026-11-02 · **files:** 2,351 · **mean:** 97.8% · **median:** 100.0%

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
| `maw-record` | 852 | 96.5% | 100.0% | 520 | 310 | 22 | 0 | 0 |
| `world-other` | 581 | 98.4% | 100.0% | 531 | 0 | 45 | 5 | 0 |
| `reference` | 468 | 98.3% | 100.0% | 420 | 0 | 48 | 0 | 0 |
| `se-dossier` | 290 | 99.8% | 100.0% | 282 | 8 | 0 | 0 | 0 |
| `root-doc` | 73 | 95.0% | 100.0% | 61 | 0 | 2 | 10 | 0 |
| `codex` | 45 | 99.6% | 100.0% | 44 | 0 | 1 | 0 | 0 |
| `template` | 42 | 98.4% | 100.0% | 38 | 0 | 4 | 0 | 0 |

## By wing

| Wing | Files | Mean | Median |
|---|---:|---:|---:|
| `SOMNARAK-WORLD/MAW_Codex_Sets` | 1,209 | 96.8% | 100.0% |
| `REFERENCE_SOMNARAK_WIKI` | 468 | 98.3% | 100.0% |
| `SOMNARAK-WORLD/Sorrow_Entities` | 291 | 99.8% | 100.0% |
| `SOMNARAK-WORLD/Ordeals` | 61 | 100.0% | 100.0% |
| `SOMNARAK-WORLD/Master_Codices` | 45 | 99.6% | 100.0% |
| `SOMNARAK-WORLD/Pages` | 44 | 100.0% | 100.0% |
| `TEMPLATES` | 42 | 98.4% | 100.0% |
| `PROJECT_MOON_RESEARCH` | 29 | 99.4% | 100.0% |
| `SOMNARAK-WORLD/Echo_Cores` | 21 | 100.0% | 100.0% |
| `GAME_BATTLE` | 18 | 100.0% | 100.0% |
| `SOMNARAK-WORLD/Hope_Transformations` | 15 | 100.0% | 100.0% |
| `SOMNARAK-WORLD/Unknown_Entities` | 13 | 98.7% | 100.0% |
| `SOMNARAK-WORLD/The_Absolvohan` | 11 | 98.5% | 100.0% |
| `tools` | 11 | 72.8% | 66.7% |
| `CANON` | 10 | 95.0% | 100.0% |
| `SOMNARAK-WORLD/Gieok_Jeojangso` | 9 | 100.0% | 100.0% |
| `SOMNARAK-WORLD/Katabagil` | 9 | 100.0% | 100.0% |
| `SOMNARAK-WORLD/Jipyeongseondae` | 8 | 97.9% | 100.0% |
| `SOMNARAK-WORLD/Katharcheok` | 8 | 97.9% | 100.0% |
| `SOMNARAK-WORLD/Story_Cantos` | 7 | 100.0% | 100.0% |
| `SOMNARAK-WORLD/Mugenhan_Ecology` | 6 | 100.0% | 100.0% |
| `SOMNARAK-WORLD/Nareumhan` | 6 | 100.0% | 100.0% |
| `(root)` | 3 | 100.0% | 100.0% |
| `SOMNARAK-WORLD/Tactical_Combat_Engine` | 3 | 100.0% | 100.0% |
| `SOMNARAK-WORLD/` | 2 | 100.0% | 100.0% |
| `docs` | 2 | 100.0% | 100.0% |

## Where the missing share actually is


| Obligation | Files missing it | What it means |
|---|---:|---|
| `appearance` | 133 | No Appearance section and no inline `**Appearance:**`. |
| `h1_match` | 125 | The H1 does not carry the subject the filename names. |
| `sections` | 70 | No second-level section — short index pages and stubs. |
| `substance` | 53 | Below the class word floor. |
| `corrosion_stock` | 50 | Corrosion prose present but not in the stock form. |
| `cost_line` | 28 | No Echo cost (weapons, suits) or bestowal chance (stigmas). |
| `statistics` | 16 | No damage/speed/range/chance/grade line at all. |
| `no_ai_tic` | 8 | Banned wording in a content file. |
| `max_amount` | 6 | No stock ceiling filed — no `Maximum Amount` row, no `Maximum / Echo Cost` column, no inline `max N`. |
| `h1` | 3 | No H1 at all. |
| `observation_log` | 3 | The 관찰 기록 section is under 40 words. |
| `operational_fields` | 2 | An Operational Parameters field is empty. |
| `nine_headings` | 1 | Missing one of the nine required dossier sections. |
| `story_log` | 1 | No numbered entry under 이야기 보고. |

## The M.A.W. registry, block by block

| Registry block | Files | Mean | Median |
|---|---:|---:|---:|
| Registry 683–709 | 21 | 83.0% | 91.7% |
| Registry 643–677 | 21 | 92.1% | 91.7% |
| Registry 716–757 | 21 | 92.5% | 91.7% |
| Registry 185–195 | 21 | 93.7% | 91.7% |
| Registry 1001–1043 | 173 | 93.7% | 91.7% |
| Registry 200–219 | 21 | 94.1% | 91.7% |
| Registry 170–184 | 21 | 95.2% | 100.0% |
| Registry 339–371 | 21 | 96.0% | 100.0% |
| Registry 009–015 | 21 | 96.4% | 100.0% |
| Registry 016–031 | 21 | 96.4% | 100.0% |
| Registry 489–519 | 25 | 96.7% | 100.0% |
| unfiled | 31 | 96.8% | 100.0% |
| Registry 525–559 | 17 | 97.1% | 100.0% |
| Registry 762–801 | 53 | 97.2% | 100.0% |
| Registry 993–997 | 9 | 97.2% | 100.0% |
| Registry 409–453 | 21 | 97.2% | 100.0% |
| Registry 130–150 | 21 | 97.2% | 100.0% |
| Registry 373–407 | 21 | 97.6% | 100.0% |
| Registry 001–007 | 21 | 97.6% | 100.0% |
| Registry 032–042 | 21 | 97.6% | 100.0% |
| Registry 077–092 | 21 | 97.6% | 100.0% |
| Registry 099–103 | 21 | 97.6% | 100.0% |
| Registry 821–852 | 29 | 98.0% | 100.0% |
| Registry 863–897 | 29 | 98.0% | 100.0% |
| Registry 315–330 | 21 | 98.0% | 100.0% |
| Registry 622–641 | 21 | 98.0% | 100.0% |
| Registry 119–127 | 21 | 98.0% | 100.0% |
| Registry 235–247 | 21 | 98.4% | 100.0% |
| Registry 265–285 | 22 | 98.5% | 100.0% |
| Registry 043–055 | 25 | 98.7% | 100.0% |
| Registry 560–585 | 13 | 98.7% | 100.0% |
| Registry 061–073 | 21 | 98.8% | 100.0% |
| Registry 220–233 | 21 | 98.8% | 100.0% |
| Registry 456–488 | 21 | 98.8% | 100.0% |
| Registry 105–115 | 21 | 98.8% | 100.0% |
| Registry 151–157 | 21 | 98.8% | 100.0% |
| Registry 159–169 | 21 | 98.8% | 100.0% |
| Registry 249–260 | 21 | 98.8% | 100.0% |
| Registry 941–976 | 49 | 99.0% | 100.0% |
| Registry 290–310 | 21 | 99.2% | 100.0% |
| Registry 589–617 | 21 | 99.2% | 100.0% |
| Registry 900–930 | 125 | 99.4% | 100.0% |

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
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_683_to_709/README.md` | 66.7% | sections substance |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_683_to_709/SE-686-A__SIDE_CODEX_Window_of_a_Thousand_Goodbyes.md` | 66.7% | sections substance |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_683_to_709/SE-689-A__SIDE_CODEX_Face_Beneath_Masks.md` | 66.7% | sections substance |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_683_to_709/SE-693-A__SIDE_CODEX_Undercurrent.md` | 66.7% | sections substance |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_716_to_757/README.md` | 66.7% | sections substance |
| `tools/tests/fixtures/SE-C-IIIγ-998_Bad_Label_Tag.md` | 66.7% | sections substance |
| `tools/tests/fixtures/SE-C-IIIγ-999_Good_Label_Sample.md` | 66.7% | sections substance |
| `tools/tests/fixtures/bad_seam_out_of_1000.md` | 66.7% | sections substance |
| `tools/tests/fixtures/bad_seam_splice.md` | 66.7% | sections substance |
| `tools/tests/fixtures/bad_timeline_6000_years.md` | 66.7% | sections substance |
| `tools/tests/fixtures/bad_timeline_year_future.md` | 66.7% | sections substance |
| `tools/tests/fixtures/bad_timeline_yoon_500.md` | 66.7% | sections substance |
| `tools/tests/fixtures/good_seam_sample.md` | 66.7% | sections substance |
| `tools/tests/fixtures/good_timeline_sample.md` | 66.7% | sections substance |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_683_to_709/SE-683-D__MAW-G_Swallowed_Furys_Ember.md` | 75.0% | statistics cost_line corrosion_stock |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_683_to_709/SE-686-D__MAW-G_Window_of_a_Thousand_Goodbyes_Shard.md` | 75.0% | statistics cost_line corrosion_stock |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_683_to_709/SE-689-D__MAW-G_The_Wall_Shard.md` | 75.0% | statistics cost_line corrosion_stock |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_683_to_709/SE-693-D__MAW-G_The_Rootbound_Staff.md` | 75.0% | statistics cost_line corrosion_stock |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_683_to_709/SE-709-D__MAW-G_Ungrievingness_Shard.md` | 75.0% | statistics cost_line corrosion_stock |
| `CANON/README.md` | 83.3% | sections |
| `PROJECT_MOON_RESEARCH/CROSS_VERSE/COMPLETE SYSTEM COMPARISON-SOMNARAK vs. Lobotomy Corporation.md` | 83.3% | h1 |
| `REFERENCE_SOMNARAK_WIKI/AUDITS/README.md` | 83.3% | sections |
| `REFERENCE_SOMNARAK_WIKI/GUIDES/README.md` | 83.3% | sections |
| `REFERENCE_SOMNARAK_WIKI/REGISTRY/QUOTE_REGISTER_LEDGER.md` | 83.3% | sections |

## Reproduce

```bash
python3 tools/finishedness.py                      # summary
python3 tools/finishedness.py --worst 25           # lowest files
python3 tools/finishedness.py --csv out.csv        # every file, every missing key
```

