# M.A.W. Stock Ceiling Audit — what the `Maximum Amount` field actually holds

**Raised:** 2026-11-02 · **Rule:** [`R-37`](../../REFERENCE_SOMNARAK_WIKI/RULES/R-37_MAW_STOCK_CEILING.md) · **Law:** `SOMNARAK_MAW_CODEX.md` §I.1
**Scope:** all 852 `-B/-C/-D` records under `SOMNARAK-WORLD/MAW_Codex_Sets/`

---

## Why this audit exists

The owner asked a plain question the archive had never answered: **how many of each M.A.W. piece can exist per Sorrow Entity, per type?** Every dossier files a figure in `Maximum Amount`. No codex said what the figure meant, what its upper bound was, or what could lower it. Three separate readings were possible, and nothing in the text ruled any of them out:

- the figure is the **remaining stock** — so a piece on loan, a piece in a vault, a piece carried by a living bearer are all one lower;
- the figure is a **lifetime total** — so it never moves at all;
- the figure is **this bearer's allotment** — so it resets on every issue.

Only the first is true, and only in the narrow form set out in `R-37`.

## The parse, and the false basis it corrects

The field is regex-hostile, and two earlier attempts produced wrong totals. Both failures are recorded here so the next auditor does not repeat them.

**Failure 1 — the combat-table header.** `Maximum / Echo Cost` also appears as a **column header** in the combat stat tables: `| Damage | Speed | Range | Pattern / Falloff | Maximum / Echo Cost |`. A pattern that matches the string anywhere in the file returns **362** rows that are headers, not amounts. Inflates the count; contributes nothing.

**Failure 2 — counting matches, not files.** Several records carry **both** a `Maximum Amount` row *and* a `Maximum / Echo cost` row. Counting matches rather than records double-counts them, which is how a survey can report 298 where the true per-record count is 199.

**The working recipe** — a row counts only where the label is the **first cell of its own row**, plus the inline bold form:

```python
row = re.compile(r'(?im)^\|\s*\**\s*(?:Maximum|Max)\s*(?:Amount|/\s*(?:Echo\s*)?Cost)\s*\**\s*\|\s*(.+?)\s*\|\s*$')
inl = re.compile(r'(?i)\*\*\s*(?:Maximum|Max)\s*/\s*(?:Echo\s*)?Cost\s*:?\s*\*\*\s*(\d+)')
```

First match per file, `row` before `inl`. Surface forms found: `Maximum Amount` 150 · `Maximum / Echo Cost` row 33 · inline `**Maximum / Cost:**` 16.

## The result

| | Weapon | Suit | Stigma |
|---|---:|---:|---:|
| States a figure | 98 | 101 | 0 |
| States none | 186 | 183 | 284 |
| **1 — Held** | 1 | 1 | — |
| **2 — Limited** | 17 | 17 | — |
| **3 — Standard** | 32 | 33 | — |
| **4 — Stocked** | 30 | 31 | — |
| **5 — Abundant** | 18 | 19 | — |

**852 records. 199 state a figure. 653 do not.** No record files above five; none files zero.

The Stigma column is empty by design: every Stigma record answers `Acquisition Probability` instead, which is the **rate of arrival**, not the **size of the holding**. The two questions were being asked of one field, which is why Stigmas appeared to be missing data rather than answering a different question.

## The band-word corrections — 48 files

The law fixes the word to the figure. Forty-eight records wrote a word that contradicted their own number, or wrote no word at all. All were corrected to the record's own figure; **every existing note was preserved in parentheses**, and no figure was changed.

| Was | Became | Files |
|---|---|---:|
| `4 — Limited` | `4 — Stocked` | 24 |
| `5 — Standard` | `5 — Abundant` | 12 |
| `4 — Standard Cadre` | `4 — Stocked (Standard Cadre)` | 2 |
| `3 — controlled operational issue` | `3 — Standard (controlled operational issue)` | 2 |
| `5 — regular qualified allocation` | `5 — Abundant (regular qualified allocation)` | 2 |
| `2 — sealed/historical pair` | `2 — Limited (sealed historical pair)` | 2 |
| `1/2/3` with no word | `1 — Held` / `2 — Limited` / `3 — Standard` | 6 |
| `4 — stocked …qualified teams` | `4 — Stocked (…qualified teams)` | 2 |

Re-scan after correction: **0 misfiles**.

## What this audit does not do

It does not invent a figure for the 653 records that file none. A blank field is a debt, not a licence, and `R-37` says so in terms. Filling those figures is a per-record decision that needs the record's own extraction history — the batch that writes them must read each file, not sample it.

It also does not touch the 123 filename↔H1 mismatches, which remain an open owner decision under `A5`.
