# 22 — BOX & TABLE FORMATTING TEMPLATE

**Template ID:** `T-22-FORMAT`  
**Generates:** Any ASCII box or table inside `SOMNARAK-WORLD/**/*.md` or `GAME_BATTLE/**/*.md`  
**Authority:** `TEST_TEXT_BOX_WIDTHS.md` + `REFERENCE_SOMNARAK_WIKI/CHATROOM_TEXT_BOX_STANDARDS.md` + `tools/check_box_symmetry.py` + `tools/box_formatter.py`

---

## DEEP KNOWLEDGE — READ BEFORE WRITING

- **Two legal widths — never mix:**
  * **Chatroom / Standard Boxes:** **Exactly 74 columns** (`+` to `+`, `|` to `|`) — every row equal to the longest row. This is the Arena chatroom standard and the default for dossiers.
  * **Tactical Monitors / Wide Boxes:** **127–128 columns** (`len(line) in [127,128]`) — for 10-Node grids, GBS monitors, and wide-form `Tactical_Combat_Engine` displays only.
- **Zero Hangul inside boxes.** Inside any ````text fence box, use Romaja only (`Dohan`, `Naehan`, `Oehan`, `Gieok Jeojangso`). Hangul inside boxes renders as fullwidth and breaks alignment (2 columns per glyph).
- **Outside boxes:** Korean requires two-space buffer: `  [한글]  ` with Romanization + English — e.g., `  한  / Han [Grief]`, `  도한  / Dohan [City Sorrow]`.
- **Enclosure:** Every box/table MUST be inside ````text ... ```` fences (or ```` ... ```` with no language that triggers markdown auto-link). Never raw HTML `<br>`, never LaTeX `$...$`, never bare `.md` that auto-links inside a box.
- **Growth rule:** A single logical cell/row may grow vertically up to **5 visual sub-rows** (word-wrap, not slice). Never truncate tokens or use `…` to fake width. Pad every sub-row to exact width.
- **Formatter:** Use `python3 tools/box_formatter.py` or `https://www.tablesgenerator.com/text_tables` → Text Tables → reStructuredText style (`+===+`, `+---+`).

---

## 74-COLUMN BOX TEMPLATES (Default — Copy-Paste Safe)

### Single Text Box (74 Cols)

```text
+========================================================================+
|                     HEADER TITLE (CAPS, CENTERED)                      |
+------------------------------------------------------------------------+
| Line content padded to exactly 70 inner chars + 2 borders = 74         |
| Another row of text — every row measures 74 from | to |                |
+========================================================================+
```

Width math: `+` (1) + `=`×70 (70) + `+` (1) = 72? No — correct: `+` (1) + `-×72` (72) + `+` (1)=74? Check: `+========================================================================+` is 1+72+1=74. Verify with `python3 -c "print(len('+========================================================================+'))"` → 74. Pad inner to 72 between `|`s.

### Multi-Column Grid Table (74 Cols)

```text
+--------------------------+-----------------------------------------------+
| Header A (26 inner)      | Header B (45 inner)                           |
+==========================+===============================================+
| Item 01                  | Description text that wraps naturally at      |
|                          | word boundaries into up to five sub-rows      |
|                          | without truncating any words or tokens.       |
+--------------------------+-----------------------------------------------+
| Item 02                  | Another entry                                 |
+--------------------------+-----------------------------------------------+
```

Width math: `|`(1)+26+`|`(1)+45+`|`(1)=74. Use `tablesgenerator.com` Text Tables, then verify every row `len==74`.

### Multi-Line Cell Wrapping (5-Row Growth Example)

```text
+--------------------------+---------------------------------------------+
| STANDARD COMPONENT       | OPERATIONAL EXECUTION DETAIL                |
+==========================+=============================================+
| Automated Vertical       | A single logical row expands cleanly up to  |
| Growth Standard          | five visual sub-rows vertically without     |
| (1 to 5 Rows Capped)     | cutting or truncating any words, ensuring   |
|                          | complete information density and pristine   |
|                          | geometric symmetry across every boundary.   |
+--------------------------+---------------------------------------------+
```

---

## 127-COLUMN WIDE-FORMAT TEMPLATE (Tactical Monitors Only)

```text
+====================================================================================================================================================+
|                                         WIDE-FORMAT TACTICAL MONITOR — 10-NODE GRID ENGAGEMENT [N01–N10]                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------+
| N01   N02   N03   N04   N05   N06   N07   N08   N09   N10   |                    SORROW TIDE: +10% / PHASE                                         |
| [JIN] [SEO] [TAE] [MIN] [COV]        [ENTITY BODY — CROWN / HEART / FOUNDATION] |                    PHASE: 2 / STAGGER: 60%                       |
+====================================================================================================================================================+
```

Verify with `python3 -c "print(len('+===============================================================================================================================+'))"` → 127 or 128.

---

## VERIFICATION COMMAND (Before Commit)

```bash
python3 tools/check_box_symmetry.py
python3 tools/text_box_double_checker.py
# Both must report: PASS (0 crooked rows), RESULT: PASSED
```

**Test snippet:**

```bash
python3 -c "
s='+========================================================================+'
print(len(s), '→', 'PASS' if len(s)==74 else 'FAIL')
"
```

---

## VALIDATION CHECKLIST

- [ ] Every box inside ````text fences.
- [ ] Every row from `+` to `+` and `|` to `|` measures exactly 74 (or 127–128 for wide) — verified with `len()`.
- [ ] Zero Hangul inside boxes (Romaja only); Korean outside uses `  [한글]  ` buffer with Romaja + English.
- [ ] No `<br>`, no `$...$`, no bare `.md` auto-link inside box.
- [ ] No truncation: word-wrap up to 5 sub-rows, never `…` or slice.
