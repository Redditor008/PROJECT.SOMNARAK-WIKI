# File finishedness — every file, measured

**Measured:** 2026-11-02 · **files:** 2,343 · **mean:** 99.5% · **median:** 100.0%

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
| `world-other` | 581 | 100.0% | 100.0% | 581 | 0 | 0 | 0 | 0 |
| `reference` | 469 | 100.0% | 100.0% | 469 | 0 | 0 | 0 | 0 |
| `se-dossier` | 290 | 100.0% | 100.0% | 290 | 0 | 0 | 0 | 0 |
| `root-doc` | 64 | 100.0% | 100.0% | 64 | 0 | 0 | 0 | 0 |
| `codex` | 45 | 100.0% | 100.0% | 45 | 0 | 0 | 0 | 0 |
| `template` | 42 | 100.0% | 100.0% | 42 | 0 | 0 | 0 | 0 |

## By wing

| Wing | Files | Mean | Median |
|---|---:|---:|---:|
| `SOMNARAK-WORLD/MAW_Codex_Sets` | 1,209 | 99.0% | 100.0% |
| `REFERENCE_SOMNARAK_WIKI` | 469 | 100.0% | 100.0% |
| `SOMNARAK-WORLD/Sorrow_Entities` | 291 | 100.0% | 100.0% |
| `SOMNARAK-WORLD/Ordeals` | 61 | 100.0% | 100.0% |
| `SOMNARAK-WORLD/Master_Codices` | 45 | 100.0% | 100.0% |
| `SOMNARAK-WORLD/Pages` | 44 | 100.0% | 100.0% |
| `TEMPLATES` | 42 | 100.0% | 100.0% |
| `PROJECT_MOON_RESEARCH` | 29 | 100.0% | 100.0% |
| `SOMNARAK-WORLD/Echo_Cores` | 21 | 100.0% | 100.0% |
| `GAME_BATTLE` | 18 | 100.0% | 100.0% |
| `SOMNARAK-WORLD/Hope_Transformations` | 15 | 100.0% | 100.0% |
| `SOMNARAK-WORLD/Unknown_Entities` | 13 | 100.0% | 100.0% |
| `SOMNARAK-WORLD/The_Absolvohan` | 11 | 100.0% | 100.0% |
| `CANON` | 10 | 100.0% | 100.0% |
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
| `max_amount` | 6 | No stock ceiling filed — no `Maximum Amount` row, no `Maximum / Echo Cost` column, no inline `max N`. |

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
| Registry 716–757 | 21 | 100.0% | 100.0% |

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
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_185_to_195/190_Rage_Statue/SE-190-D__MAW-G_The_Rage_Charm.md` | 81.8% | max_amount h1_match |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_001_to_007/001_Orphaned_Bell/SE-001-B__MAW-W_The_Laments_Requiem.md` | 90.9% | h1_match |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_001_to_007/002_Grieving_Colossus/SE-002-B__MAW-W_The_Mourning_Maul.md` | 90.9% | h1_match |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_001_to_007/005_Smothering_Mother/SE-005-B__MAW-W_The_Embrace_Fang.md` | 90.9% | h1_match |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_001_to_007/007_Brume/SE-007-B__MAW-W_The_Hope_Lens.md` | 90.9% | h1_match |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_009_to_015/009_Memory_Weaver/SE-009-B__MAW-W_The_Forgotten_Lens.md` | 90.9% | h1_match |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_009_to_015/010_Convergence/SE-010-B__MAW-W_The_Absolute_Maul.md` | 90.9% | h1_match |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_009_to_015/011_Whispering_Walls/SE-011-B__MAW-W_The_Listening_Requiem.md` | 90.9% | h1_match |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_009_to_015/014_Debt_Eater/SE-014-B__MAW-W_The_Debt_Lens.md` | 90.9% | h1_match |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_009_to_015/015_Debt_Scale/SE-015-B__MAW-W_The_Balance_Lens.md` | 90.9% | h1_match |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_016_to_031/019_Inherited_Debt/SE-019-B__MAW-W_The_Debt_Maul.md` | 90.9% | h1_match |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_016_to_031/019_Inherited_Debt/SE-019-C__MAW-S_The_Debt_Mantle.md` | 90.9% | h1_match |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_016_to_031/019_Inherited_Debt/SE-019-D__MAW-G_The_Debt_Chain.md` | 90.9% | h1_match |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_016_to_031/025_Silent_Child/SE-025-B__MAW-W_The_Silence_Lens.md` | 90.9% | h1_match |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_016_to_031/031_Observing_Bird/SE-031-B__MAW-W_The_Witness_Requiem.md` | 90.9% | h1_match |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_016_to_031/031_Observing_Bird/SE-031-C__MAW-S_The_Witness_Shroud.md` | 90.9% | h1_match |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_016_to_031/031_Observing_Bird/SE-031-D__MAW-G_The_Witness_Eye.md` | 90.9% | h1_match |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_032_to_042/032_Weighting_Bird/SE-032-B__MAW-W_The_Judgment_Fang.md` | 90.9% | h1_match |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_032_to_042/032_Weighting_Bird/SE-032-D__MAW-G_The_Judgment_Scale.md` | 90.9% | h1_match |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_032_to_042/036_Cracked_Hourglass/SE-036-B__MAW-W_The_Hourglass_Maul.md` | 90.9% | h1_match |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_032_to_042/036_Cracked_Hourglass/SE-036-D__MAW-G_The_Hourglass_Pendant.md` | 90.9% | h1_match |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_043_to_055/055_Weeping_Statue/SE-055-B__MAW-W_The_Tear_Requiem.md` | 90.9% | h1_match |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_043_to_055/055_Weeping_Statue/SE-055-C__MAW-S_The_Tear_Shroud.md` | 90.9% | h1_match |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_061_to_073/062_Inheritor/SE-062-B__MAW-W_The_Resentment_Fang.md` | 90.9% | h1_match |
| `SOMNARAK-WORLD/MAW_Codex_Sets/Registry_077_to_092/077_Memory_Thief/SE-077-B__MAW-W_The_Shadow_Lens.md` | 90.9% | h1_match |

## Reproduce

```bash
python3 tools/finishedness.py                      # summary
python3 tools/finishedness.py --worst 25           # lowest files
python3 tools/finishedness.py --csv out.csv        # every file, every missing key
```

