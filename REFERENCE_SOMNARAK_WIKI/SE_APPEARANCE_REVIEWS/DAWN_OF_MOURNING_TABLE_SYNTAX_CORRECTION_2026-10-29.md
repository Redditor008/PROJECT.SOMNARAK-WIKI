# Dawn of Mourning — Combat Table Syntax Correction

**Date:** 2026-10-29  
**Designation:** `C-Vω-001`  
**Base commit:** `a5800477bf752b0e94148a72bed6bbbb6b0ef09b`  
**Before SHA-256:** `c41e960489ab2a9d4470a14349a5b32f640c07c45e9b2f8239a876a592aa31b0`  
**Final SHA-256:** `966feea825c302710ad17ebf5487a859379e93674f28003817b5e69a591c6e5b`  
**Outcome:** Table syntax corrected. Dawn remains **HELD** for the substantive source forks recorded in the R-34 recheck.

## What the owner found

The owner was correct. In the rendered Combat Actions table, the **Trigger** column was not receiving the Trigger text for the first four action rows.

The Trigger text was present in the Markdown source, but it was in the wrong parsed cell.

## Root cause

The header has five columns:

1. Name / Category
2. Flavor Text
3. Combat Move
4. Combat Effect/Stat
5. Trigger

Rows 83–86 contained this duration separator inside the fourth cell:

```text
| 8s, 2s per type
```

That unescaped `|` is another Markdown cell boundary. Those rows therefore parsed as **six cells**, not five:

| Lines | Parsed cells before repair |
|---|---|
| Header and separator | 5 |
| *The Four Sorrows* | 6 |
| *No Partial Light* | 6 |
| *The Mourning Light* | 6 |
| *The Mourners* | 6 |
| *The Mourning of All Things* | 5 |

The ordinary gate checks saw that each row began and ended with a pipe. They did **not** verify that every row had the same number of cells as the header. That is why they passed a visibly broken table.

## Repair

Four exact repairs replaced the internal duration separator:

```text
| 8s, 2s per type
```

with:

```text
; 8s total, 2s per type
```

No action names, flavour, moves, effects, segment values, triggers or sequence were changed in this syntax correction.

## Parsed result

Every line of the Combat Actions table now parses as five cells:

| Action | Parsed Trigger cell after repair |
|---|---|
| *The Four Sorrows* | At formation or on first entry into full sight, in the historical/projected sequence. |
| *No Partial Light* | After *The Four Sorrows*, while the target remains within the Dawn's sight. |
| *The Mourning Light* | When an exposed target remains in full sight after partial sight fails. |
| *The Mourners* | After sentence begins, when the blessed twelve take up the Mourner role in the projected sequence. |
| *The Mourning of All Things* | As the culmination after sentence and Mourner spread — not at the instant of formation. |

The same unescaped-pipe cell-count check was run over **every contiguous Markdown table block in the Dawn primary**. After repair, no table block has a cell-count mismatch.

## Rule correction

`R-34` now explicitly requires:

- unescaped-pipe cell counting for every table block;
- header/separator/row equality;
- parsed final-cell verification against its header, especially Combat Action Trigger cells.

A row that merely starts and ends with `|` is no longer treated as valid by itself.

## Validation

- `verify.py` — PASS
- `tpl.py` — PASS (`RESIDUE 0`)
- `sectfile.py` — PASS
- `wikistd.py` — PASS (`meets True`)
- `sect.py` — `GENERIC 0.002 (12 shared shingles)`
- Exact replay from the frozen before-file — equals final

## Commentary

This was not a lore disagreement. It was a basic Markdown parsing failure that the previous review and the ordinary tools both missed. The correct check is embarrassingly concrete: count the cells and read what lands under **Trigger**. On the repaired rows, the Trigger does.
