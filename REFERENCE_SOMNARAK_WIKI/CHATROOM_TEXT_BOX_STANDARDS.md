# Chatroom Text Box & Table Standards (Arena.ai)

**Authority:** User Directive  
**Target Environment:** Arena.ai Chatroom Output  
**Tool Reference:** [tablesgenerator.com/text_tables](https://www.tablesgenerator.com/text_tables)

---

## 1. Core Constraints

| Setting | Value | Rationale |
|---|---|---|
| **Use Unicode symbols for borders** | **[No]** | Prevents terminal/font rendering artifacts across disparate client platforms. Strictly use standard ASCII (`+`, `-`, `|`, `=`). |
| **Syntax Standard** | **reStructuredText [Yes]** | Clean grid table structure with distinct header separators (`+===+===+`) and cell dividers (`+---+---+`). |
| **Max Row Character Limit** | **67 Characters Exactly** | Verified through character-by-character testing in Arena.ai chatroom view without code block fences to prevent line-wrapping. |

---

## 2. Specification Examples

### A. Single Box / Text Banner (Width: Exactly 67 Chars)
```
+-----------------------------------------------------------------+
| TITLE / HEADER TEXT (PADDED TO 65 INNER CHARS)                  |
+=================================================================+
| Body line text content                                          |
+-----------------------------------------------------------------+
```

### B. Multi-Column Grid Table (Width: Exactly 67 Chars)
```
+------------------+----------------------------------------------+
| Header A         | Header B                                     |
+==================+==============================================+
| Item 01          | Description text (padded to fit column)      |
+------------------+----------------------------------------------+
| Item 02          | Description text                             |
+------------------+----------------------------------------------+
```
*(Column widths: 18 + 46 + 3 border characters = 67 characters total)*

### C. Compact Mobile Profile (Width: 48 Chars)
```
+----------------+-----------------------------+
| Header A       | Header B                    |
+================+=============================+
| Item 01        | Description text            |
+----------------+-----------------------------+
```
