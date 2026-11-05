# TEMPLATES — The Authoring Kit

**Temporal Anchor:** Year 4,238 · Dawn Initiative · Cycle 1,778

Every file in this directory exists so that deep canonical knowledge is known **before** anything is generated. No dossier, codex, scenario or chronicle should be drafted without reading its template and the primer first.

The kit is branched by category, so a search for "what generates a dossier" does not have to walk a flat list of twenty-five numbers.

| Branch | Holds | Start here |
|---|---|---|
| [`SE/`](SE/README.md) | The primer, the dossier template, the side codex, and the three M.A.W. piece templates (00–05) | [`SE/00_GLOBAL_DEEP_KNOWLEDGE_PRIMER.md`](SE/00_GLOBAL_DEEP_KNOWLEDGE_PRIMER.md) |
| [`SE_CATEGORIES/`](TEMPLATES/SE_CATEGORIES/README.md) | The five category definitions and their five category templates: Subject, Non-Subject, I / O / A Relic | [`TEMPLATES/SE_CATEGORIES/README.md`](TEMPLATES/SE_CATEGORIES/README.md) |
| [`SYSTEMS/`](SYSTEMS/README.md) | One template per world system: Ordeal, Hope Transformation, Unknown Entity, Echo Core, Master Codex, Absolvohan, Katabagil, Katharcheok, Gieok, Jipyeongseondae, Story Canto, Mugenhan (06–17) | [`SYSTEMS/README.md`](SYSTEMS/README.md) |
| [`GAME/`](GAME/README.md) | Combat engine, battle scenario, boss mechanics, squad archetype (18–21) | [`GAME/README.md`](GAME/README.md) |
| [`FORMAT/`](FORMAT/README.md) | Boxes and tables, canonical naming and banned strings, wiki-part reference (22–24) | [`FORMAT/README.md`](FORMAT/README.md) |

## How To Use The Kit

1. **Read [`SE/00_GLOBAL_DEEP_KNOWLEDGE_PRIMER.md`](SE/00_GLOBAL_DEEP_KNOWLEDGE_PRIMER.md) first — always.** It carries the laws that apply to every generation task.
2. **Open the template for the document you are writing**, in the branch above.
3. **Fill every `{{PLACEHOLDER}}` in order.** Do not delete sections; write `N/A` only where the template permits it.
4. **Run the validation checklist at the end of the template** before committing. Each line names the tool that checks it where a tool exists.
5. **Run the gate:** `bash tools/gate.sh "<message>"`.

## Two Rules That Outrank The Template

- **Logic Path, Not Template Path.** Where a file's own record contradicts the scaffold — a holding that cannot fight having a Combat Record, a room that never leaves having a breach section — the record wins and the section changes shape. The templates describe the ordinary case; they do not overrule the evidence.
- **A template artefact is a defect the moment it appears in a finished file.** Placeholders, generic filler, and sentences that could sit in any of forty files are not "to be filled later"; they are the archive's own failure mode, and every checklist in this kit is written against it.
