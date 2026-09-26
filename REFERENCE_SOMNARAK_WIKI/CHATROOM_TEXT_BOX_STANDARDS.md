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

## 4. Multi-Line Cell Wrapping & Vertical Growth Standard (No Truncation)

```
NEVER slice, truncate, or cut words with ellipsis or string cuts!
```

### The 5-Row Vertical Growth Rule (User Directive)
A single logical row or table cell can and should **grow vertically up to 5 visual sub-rows** to accommodate rich descriptions, stats, or narrative context:
1. **Zero Truncation:** Never cut off words, truncate tokens, or use artificial string slicing.
2. **Clean Word Wrapping:** Wrap text naturally at word boundaries into visual sub-rows.
3. **The 5-Row Cleanliness Cap:** Cap vertical cell growth at **5 visual sub-rows** per logical entry. Text exceeding 5 rows becomes visually cluttered and unclean; distill content to fit within 1 to 5 rows.
4. **Symmetrical Padding:** Every wrapped sub-row must be padded to the exact target monospace display width so all outer borders (`|`) and internal dividers remain 100% vertically aligned.

### Example: Multi-Line Wrapped Row (Exact 74-Column Standard)
```text
+==========================+=============================================+
| STANDARD COMPONENT       | OPERATIONAL EXECUTION DETAIL                |
+--------------------------+---------------------------------------------+
| Automated Vertical       | A single logical row expands cleanly up to  |
| Growth Standard          | five visual sub-rows vertically without     |
| (1 to 5 Rows Capped)     | cutting or truncating any words, ensuring   |
|                          | complete information density and pristine   |
|                          | geometric symmetry across every boundary.   |
+==========================+=============================================+
```
In this pattern, the right-hand cell expands cleanly across multiple sub-rows while maintaining exact monospace border alignment across the entire 74-character width.

---

## 5. Typography Scope: Monospace ASCII Boxes vs. Rendered Markdown Tables

1. **Monospace ASCII Boxes (Inside ``` Code Fences):**
   - **Strictly ZERO Korean Hangul characters permitted.**
   - Use Latin Alphabet Romanization (Romaja) exclusively (e.g. *Haewon*, *Dohan*, *Naehan*, *Gieok Jeojangso*).
   - *Technical Rationale:* East Asian Hangul glyphs render as fullwidth (2 monospace columns wide), causing severe border misalignment, line-wrapping, and crooked vertical pipes (`|`).
2. **Rendered Markdown Tables (`| Key | Value |` Outside Code Fences):**
   - Standard GitHub Markdown tables are rendered by the browser engine with proportional variable cell widths and dynamic padding.
   - Korean Hangul is **fully permitted and encouraged** in markdown table cells for bilingual terminology and worldbuilding immersion, provided the mandatory two-space buffer (`  [한글]  `) is maintained alongside paired English and Romanized translations.

