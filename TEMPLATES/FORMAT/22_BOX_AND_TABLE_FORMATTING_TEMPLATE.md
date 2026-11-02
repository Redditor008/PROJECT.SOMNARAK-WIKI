# 22 — BOX & TABLE FORMATTING TEMPLATE

**Template ID:** `T-22-FORMAT`  
**Generates:** Any ASCII box or table inside `SOMNARAK-WORLD/**/*.md` or `GAME_BATTLE/**/*.md`  
**Authority:** `ARCHIVE/TEST_TEXT_BOX_WIDTHS.md` + `REFERENCE_SOMNARAK_WIKI/GUIDES/CHATROOM_TEXT_BOX_STANDARDS.md` + `tools/check_box_symmetry.py` + `tools/box_formatter.py`

---

## DEEP KNOWLEDGE — READ BEFORE WRITING

- **Three widths in use — match the file you are writing into:**
  * **Content boxes — 71 columns** (`+` to `+`): **972 of the 1,204 boxes in `SOMNARAK-WORLD/` are 71.** This is the de-facto standard for dossiers, codices and GAME_BATTLE monitors, and it is what the archive actually reads as. Do not "correct" a 71-wide box to 74.
  * **Reference and canon boxes — 74 columns**: 117 in `SOMNARAK-WORLD/`, 8 in `CANON/`, 8 in `REFERENCE_SOMNARAK_WIKI/`, 5 in `TEMPLATES/`. The Arena chatroom width, used for specification and comparison tables.
  * **Compact boxes — 48 columns**: 105 in `SOMNARAK-WORLD/`, 42 in `PROJECT_MOON_RESEARCH/` — short summary panels.
  * **Tactical Monitors — 127–128 columns**: reserved for 10-Node grids and wide `Tactical_Combat_Engine` displays. The worked example below is the only one currently in the tree.
  * Whatever the width, **every row in a given box must measure the same**. Mixing widths *inside one document* is the error this bullet is about; using a different width from a neighbouring file is not.

  > **Measured 2026-11-02, 1,422 boxes:** 71 → 1,087 · 74 → 172 · 48 → 147. An earlier version of this template claimed "two legal widths, exactly 74", which 1,250 of the archive's own boxes contradicted. The count above is the authority; re-measure with `python3 tools/textbox.py <file>` before quoting a width.
- **Zero Hangul inside boxes.** Inside any ````text fence box, use Romaja only (`Dohan`, `Naehan`, `Oehan`, `Gieok Jeojangso`). Hangul inside boxes renders as fullwidth and breaks alignment (2 columns per glyph).
- **Outside boxes:** Korean requires two-space buffer: `  [한글]  ` with Romanization + English — e.g., `  한  / Han [Grief]`, `  도한  / Dohan [City Sorrow]`.
- **Enclosure:** Every box/table MUST be inside ````text ... ```` fences (or ```` ... ```` with no language that triggers markdown auto-link). Never raw HTML `<br>`, never LaTeX `$...$`, never bare `.md` that auto-links inside a box.
- **Growth rule:** A single logical cell/row may grow vertically up to **5 visual sub-rows** (word-wrap, not slice). Never truncate tokens or use `…` to fake width. Pad every sub-row to exact width.
- **Formatter:** Use `python3 tools/textbox.py` (see `tools/textbox.py --help`) — it verifies every row before printing and refuses a box it cannot make square. `python3 tools/box_formatter.py` and `https://www.tablesgenerator.com/text_tables` → Text Tables → reStructuredText style (`+===+`, `+---+`) also work. **Never retype a box by hand:** a box that is perfect in the file becomes crooked in transcription.

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

Width math: 1 border + 72 inner + 1 border = **74**. Every cap and every content row pads to 72 characters between the rails. Verify with `python3 tools/textbox.py FILE`, which measures the whole box and names any row that disagrees.

### Multi-Column Grid Table (74 Cols)

```text
+--------------------------+---------------------------------------------+
| Header A (26 inner)      | Header B (45 inner)                         |
+==========================+=============================================+
| Item 01                  | Description text that wraps naturally at    |
|                          | word boundaries into up to five sub-rows    |
|                          | without truncating any words or tokens.     |
+--------------------------+---------------------------------------------+
| Item 02                  | Another entry                               |
+--------------------------+---------------------------------------------+
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
+-----------------------------------------------------------------------------------------------------------------------------+
| WIDE-FORMAT TACTICAL MONITOR - 10-NODE GRID ENGAGEMENT [N01–N10]                                                            |
+----------------------------------------------------------------------------------+------------------------------------------+
| N01   N02   N03   N04   N05   N06   N07   N08   N09   N10                        | SORROW TIDE: +10% / PHASE                |
| [JIN] [SEO] [TAE] [MIN] [COV]        [ENTITY BODY — CROWN / HEART / FOUNDATION]  | PHASE: 2 / STAGGER: 60%                  |
+----------------------------------------------------------------------------------+------------------------------------------+
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
- [ ] Every row in the box measures the **same** width (71, 74, 48 or 127–128 as that file uses) — verified with `python3 tools/textbox.py FILE`, which refuses a crooked box instead of guessing.
- [ ] Zero Hangul inside boxes (Romaja only); Korean outside uses `  [한글]  ` buffer with Romaja + English.
- [ ] No `<br>`, no `$...$`, no bare `.md` auto-link inside box.
- [ ] No truncation: word-wrap up to 5 sub-rows, never `…` or slice.
