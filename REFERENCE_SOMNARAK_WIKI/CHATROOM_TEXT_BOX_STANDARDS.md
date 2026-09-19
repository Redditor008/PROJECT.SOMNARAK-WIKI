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
| **Max Row Character Limit** | **48 Characters** | Hard ceiling for mobile screens and Arena.ai split chatroom UI to prevent unwanted line wrapping. |

---

## 2. Specification Examples

### A. Single Box / Text Banner (Width: 48 Chars)
```
+----------------------------------------------+
| TITLE / HEADER TEXT                          |
+==============================================+
| Body line 1 (padded up to 46 content chars)  |
| Body line 2                                  |
+----------------------------------------------+
```

### B. Multi-Column Grid Table (Width: 48 Chars)
```
+----------------+-----------------------------+
| Header A       | Header B                    |
+================+=============================+
| Item 01        | Description text            |
+----------------+-----------------------------+
| Item 02        | Description text            |
+----------------+-----------------------------+
```
*(Column widths: 16 + 29 + 3 border characters = 48 characters total)*
