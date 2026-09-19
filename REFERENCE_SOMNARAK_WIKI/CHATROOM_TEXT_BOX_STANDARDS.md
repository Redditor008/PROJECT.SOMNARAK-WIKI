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
| **Max Row Character Limit** | **48 Characters Max** | Universal ceiling ensuring zero line-wrapping or horizontal scroll on mobile and Arena.ai split chat screens. |

---

## 3. Reference Blueprints (48 Characters Exact Width)

### A. Single Text Box (Width: Exactly 48 Chars)
```
+----------------------------------------------+
| HEADER TITLE (PADDED TO 46 INNER CHARS)      |
+==============================================+
| Line content goes here                       |
| Another row of text                          |
+----------------------------------------------+
```

### B. Multi-Column Grid Table (Width: Exactly 48 Chars)
```
+----------------+-----------------------------+
| Header A       | Header B                    |
+================+=============================+
| Item 01        | Description text goes here  |
+----------------+-----------------------------+
| Item 02        | Another entry               |
+----------------+-----------------------------+
```
*(Width math: 1 + 16 + 1 + 29 + 1 = 48 characters total)*
