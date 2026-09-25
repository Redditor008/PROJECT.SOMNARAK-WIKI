# Chatroom Text Box & Table Standards (Arena.ai)

**Authority:** User Directive & Visual Verification
**Target Environment:** Arena.ai Chatroom Output
**Tool Reference:** [tablesgenerator.com/text_tables](https://www.tablesgenerator.com/text_tables)

---

## 1. The Core Law: Always Use Fenced Code Blocks (```)

```
NEVER output raw text boxes or tables without ``` code fences!
```

**Why this is mandatory:**
1. **Whitespace Preservation:** Normal chatroom markdown/HTML collapses consecutive spaces into a single space, destroying all cell padding and causing crooked, jagged borders.
2. **Monospace Font:** Proportional fonts cause characters of varying widths (`W` vs `i`) to misalign column borders (`|`). Fenced code blocks force monospace rendering where every character has an identical width.

---

## 2. Table & Box Constraints

| Setting | Value | Rationale |
|---|---|---|
| **Enclosure** | **Fenced Code Block (``` ... ```)** | Mandatory. Prevents whitespace stripping and proportional font misalignment. |
| **Use Unicode symbols for borders** | **[No]** | Pure standard ASCII only (`+`, `-`, `|`, `=`). Eliminates font rendering glitches. |
| **Syntax Standard** | **reStructuredText [Yes]** | Clean grid table structure with `+===+===+` headers and `+---+---+` row dividers. |
| **Max Row Character Limit** | **74 Characters Exact** | Hard universal standard (74 columns) ensuring zero line-wrapping or horizontal scroll on Arena.ai chatroom viewports. |

---

## 3. Reference Blueprints (74 Characters Exact Width)

### A. Single Text Box (Width: Exactly 74 Chars)
```
+========================================================================+
| HEADER TITLE (PADDED TO 70 INNER CHARS)                                |
+------------------------------------------------------------------------+
| Line content goes here                                                 |
| Another row of text                                                    |
+========================================================================+
```

### B. Multi-Column Grid Table (Width: Exactly 74 Chars)
```
+--------------------------+---------------------------------------------+
| Header A                 | Header B                                    |
+==========================+=============================================+
| Item 01                  | Description text goes here                  |
+--------------------------+---------------------------------------------+
| Item 02                  | Another entry                               |
+--------------------------+---------------------------------------------+
```
*(Width math: 1 + 26 + 1 + 45 + 1 = 74 characters total)*

---

## 4. Multi-Line Cell Wrapping Rule (No Truncation)

```
NEVER slice, truncate, or cut words with ellipsis or string cuts!
```

When cell content exceeds the column's inner character limit:
1. Wrap the text across multiple lines (two or more rows) within that table row.
2. Ensure every word remains complete and intact.
3. Pad empty space on shorter sibling cells with spaces so column vertical borders (`|`) remain perfectly aligned.

### Example: Multi-Line Wrapped Row (Exact 74-Column Standard)
```text
+==========================+=============================================+
| STANDARD COMPONENT       | OPERATIONAL EXECUTION DETAIL                |
+--------------------------+---------------------------------------------+
| Automated Cell Wrapping  | Text exceeding the inner column boundary    |
| Architecture             | wraps cleanly into a visual sub-row without |
|                          | truncating or slicing any individual token. |
+==========================+=============================================+
```
In this pattern, the right-hand cell expands across multiple sub-rows while maintaining exact monospace border alignment across the entire 74-character width.

---

## 5. Typography Scope: Monospace ASCII Boxes vs. Rendered Markdown Tables

1. **Monospace ASCII Boxes (Inside ``` Code Fences):**
   - **Strictly ZERO Korean Hangul characters permitted.**
   - Use Latin Alphabet Romanization (Romaja) exclusively (e.g. *Haewon*, *Dohan*, *Naehan*, *Gieok Jeojangso*).
   - *Technical Rationale:* East Asian Hangul glyphs render as fullwidth (2 monospace columns wide), causing severe border misalignment, line-wrapping, and crooked vertical pipes (`|`).
2. **Rendered Markdown Tables (`| Key | Value |` Outside Code Fences):**
   - Standard GitHub Markdown tables are rendered by the browser engine with proportional variable cell widths and dynamic padding.
   - Korean Hangul is **fully permitted and encouraged** in markdown table cells for bilingual terminology and worldbuilding immersion, provided the mandatory two-space buffer (`  [한글]  `) is maintained alongside paired English and Romanized translations.

