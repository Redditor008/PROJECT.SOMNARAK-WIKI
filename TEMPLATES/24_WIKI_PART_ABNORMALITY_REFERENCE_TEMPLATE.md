# 24 — WIKI PART ABNORMALITY REFERENCE TEMPLATE

**Template ID:** `T-24-WIKI-PART`  
**Generates:** Any `PROJECT_MOON_RESEARCH/` volume or `REFERENCE_SOMNARAK_WIKI/` index that cites LobCorp wiki parts — specifically §§ 8 & 9  
**Authority:** `REFERENCE_SOMNARAK_WIKI/WIKI_PARTS_ABNORMALITIES_SECTIONS_8_AND_9.md` + `PROJECT_MOON_RESEARCH/13_TOOL_ABNORMALITIES_ENCYCLOPEDIA.md` + Global Primer Laws 7,8,9  
**Canonical Anchors:**
- [[8 Tool Abnormalities](https://lobotomycorporation.wiki.gg/wiki/Abnormalities#Tool_Abnormalities)]
- [[9 Classification Code](https://lobotomycorporation.wiki.gg/wiki/Abnormalities#Classification_Code)]
- [[8 Tool Abnormalities](https://lobotomycorp.fandom.com/wiki/Abnormalities#Tool_Abnormalities)]
- [[9 Classification Code](https://lobotomycorp.fandom.com/wiki/Abnormalities#Classification_Code)]

---

## DEEP KNOWLEDGE — READ BEFORE WRITING

- **Wiki parts are section anchors, not pages.** `Abnormalities#Tool_Abnormalities` is §8 of the `Abnormalities` page; `Abnormalities#Classification_Code` is §9. Cite them as `Abnormalities §§ 8–9`, never as standalone pages.
- **Two mirrors exist — always cite both.** `lobotomycorporation.wiki.gg` is the primary canonical mirror; `lobotomycorp.fandom.com` is the legacy Fandom mirror (identical anchors: `#Tool_Abnormalities` and `#Classification_Code`). Provide wiki.gg first, fandom second.
- **§8 Tool Abnormalities** = `T-` class, three types (Single-Use / Equippable / Channeled), every 4th day of 6-day cycle, tool-type `09` (one `07`), `Number of Uses` / `Time of Use` unlock, capability badges (Instadeath / Alteration / Facility Benefit). See `13_TOOL_ABNORMALITIES_ENCYCLOPEDIA.md` for the `T-09-82` through `T-09-89` master matrix.
- **§9 Classification Code** = Letter-XX-YY format. First letter: `F` Fairytale, `T` Trauma, `O` Original, `D` Donation, `M` Mythical (Limbus). Second number unclear, third unique code, Legacy last letter = Risk Level (`Z/T/H/W/A`). Compare to Somnarak **SECC** `SE-[Origin]-[Rank][Potency]-[Number]` via `COMPLETE_SYSTEM_COMPARISON_SOMNARAK_VS_LOBOTOMY_CORPORATION.md` and `TEMPLATES/01_SORROW_ENTITY_DOSSIER_TEMPLATE.md`.
- **PM terms are banned in `SOMNARAK-WORLD/`** — never write `Tool Abnormality` or `Abnormality` in canon dossiers. In `PROJECT_MOON_RESEARCH/` and `REFERENCE_SOMNARAK_WIKI/` they are allowed as research terms. When a `SOMNARAK-WORLD/` codex needs to reference PM structure, do it only in an out-of-universe footnote that points to `REFERENCE_SOMNARAK_WIKI/WIKI_PARTS_ABNORMALITIES_SECTIONS_8_AND_9.md` — never in body prose.
- **Box law:** Any `## Wiki Part Reference` box inside a volume must be exactly 74 cols (`+` to `+`, `|` to `|`) or 127–128 wide for tactical monitors, inside ````text fences, zero Hangul inside (Romaja only), Korean outside with `  [한글]  ` buffer.

---

## FILE NAMING

- **Index:** `REFERENCE_SOMNARAK_WIKI/WIKI_PARTS_ABNORMALITIES_SECTIONS_8_AND_9.md` (you are here — the SSOT wiki-part index)
- **Volume header:** `PROJECT_MOON_RESEARCH/13_TOOL_ABNORMALITIES_ENCYCLOPEDIA.md` — already wired
- **New research volume citing §§ 8/9:** `PROJECT_MOON_RESEARCH/{{XX}}_{{TOPIC}}.md` — add the Wiki Part Reference box below at top
- **This template:** `TEMPLATES/24_WIKI_PART_ABNORMALITY_REFERENCE_TEMPLATE.md`

---

## SCAFFOLD — WIKI PART REFERENCE BOX (Copy-Paste Safe — 74 cols)

For any `PROJECT_MOON_RESEARCH/` volume that cites §§ 8 & 9, paste this box directly under the `### ARCHIVAL SOURCE:` line:

~~~markdown
> **Wiki Part Reference — Abnormalities §§ 8 & 9:** This volume covers §8 in full. For direct wiki-part anchors across both mirrors, see `REFERENCE_SOMNARAK_WIKI/WIKI_PARTS_ABNORMALITIES_SECTIONS_8_AND_9.md` — [[8 Tool Abnormalities](https://lobotomycorporation.wiki.gg/wiki/Abnormalities#Tool_Abnormalities)] · [[9 Classification Code](https://lobotomycorporation.wiki.gg/wiki/Abnormalities#Classification_Code)] · Mirrors: [[8 Tool Abnormalities](https://lobotomycorp.fandom.com/wiki/Abnormalities#Tool_Abnormalities)] · [[9 Classification Code](https://lobotomycorp.fandom.com/wiki/Abnormalities#Classification_Code)].

```text
+========================================================================+
|              WIKI PART ANCHORS — ABNORMALITIES §§ 8 & 9                |
+------------------------------------------------------------------------+
| §8 Tool Abnormalities  | wiki.gg: Abnormalities#Tool_Abnormalities     |
|                        | fandom.com: Abnormalities#Tool_Abnormalities  |
| §9 Classification Code | wiki.gg: Abnormalities#Classification_Code    |
|                        | fandom.com: Abnormalities#Classification_Code |
+========================================================================+
```
~~~

Box verification: `python3 -c "print(len('+========================================================================+'))"` → `74` (run `tools/check_box_symmetry.py` — must PASS).

---

## SCAFFOLD — CLEAN MIRROR TABLE (For prose sections — outside boxes)

~~~markdown
| Wiki Part | Primary Mirror (wiki.gg) | Legacy Mirror (fandom.com) |
|---|---|---|
| **§8 Tool Abnormalities** | [wiki.gg — Tool Abnormalities](https://lobotomycorporation.wiki.gg/wiki/Abnormalities#Tool_Abnormalities) | [fandom.com — Tool Abnormalities](https://lobotomycorp.fandom.com/wiki/Abnormalities#Tool_Abnormalities) |
| **§9 Classification Code** | [wiki.gg — Classification Code](https://lobotomycorporation.wiki.gg/wiki/Abnormalities#Classification_Code) | [fandom.com — Classification Code](https://lobotomycorp.fandom.com/wiki/Abnormalities#Classification_Code) |
~~~

---

## SCAFFOLD — SOMNARAK-WORLD FOOTNOTE (PM Terms Banned — Link Only)

If a `SOMNARAK-WORLD/Master_Codices/` codex must note the PM analogue for comparative integrity, use ONLY this HTML comment footnote — never body prose:

~~~markdown
<!-- OUT-OF-UNIVERSE REFERENCE — DO NOT COPY PM TERMS INTO CANON BODY -->
<!-- Wiki parts for comparative footnote only: Abnormalities §§ 8–9 via REFERENCE_SOMNARAK_WIKI/WIKI_PARTS_ABNORMALITIES_SECTIONS_8_AND_9.md — wiki.gg §§ 8/9 + fandom §§ 8/9 -->
~~~

---

## HOW THIS IS WIRED AS SOMETHING

1. **This template** — `TEMPLATES/24_WIKI_PART_ABNORMALITY_REFERENCE_TEMPLATE.md` — the deep-knowledge-first authoring kit for any future wiki-part citation (you are here).
2. **Index** — `REFERENCE_SOMNARAK_WIKI/WIKI_PARTS_ABNORMALITIES_SECTIONS_8_AND_9.md` — the SSOT wiki-part index listing all four links verbatim as requested: `[[8 Tool Abnormalities](wiki.gg)]` · `[[9 Classification Code](wiki.gg)]` · `[[8 Tool Abnormalities](fandom)]` · `[[9 Classification Code](fandom)]` plus §8/§9 summaries and cross-wiring.
3. **Volume** — `PROJECT_MOON_RESEARCH/13_TOOL_ABNORMALITIES_ENCYCLOPEDIA.md` — header now wired with the 74-col box and mirror table, pointing to the index.

---

## VALIDATION CHECKLIST

- [ ] All four links present verbatim as requested: `[[8 Tool Abnormalities](wiki.gg)]` · `[[9 Classification Code](wiki.gg)]` · `[[8 Tool Abnormalities](fandom)]` · `[[9 Classification Code](fandom)]` — plus clean `[wiki.gg — ...]` table.
- [ ] Box is exactly 74 cols (`+` to `+`, `|` to `|`) inside ````text fences, zero Hangul inside, `  [한글]  ` buffer outside if Korean appears.
- [ ] `§8` summary includes: `T-` class, 3 types (Single/Equippable/Channeled), 4th day / 6-day cycle, type `09` (one `07`), unlock via `Number of Uses` / `Time of Use`, 3 capability badges.
- [ ] `§9` summary includes: Letter-XX-YY, `F/T/O/D/M` letters with one-line glosses, second number unclear, third unique, Legacy `Z/T/H/W/A`, comparison to SECC `SE-[Origin]-[Rank][Potency]-[Number]`.
- [ ] PM terms appear ONLY in `PROJECT_MOON_RESEARCH/` or `REFERENCE_SOMNARAK_WIKI/` — never in `SOMNARAK-WORLD/` body (footnote comment only if needed).
- [ ] Cross-wiring: index → volume → template all reference each other with full canonical paths.
- [ ] `tools/check_box_symmetry.py` PASS, `tools/seam_lint.py` PASS, `tools/timeline_lint.py` PASS.

---

*For the live source pages, see: [wiki.gg Abnormalities](https://lobotomycorporation.wiki.gg/wiki/Abnormalities) (TOC §§ 8 & 9) and [fandom Abnormalities](https://lobotomycorp.fandom.com/wiki/Abnormalities) — verified anchors 2026-09-28.*
