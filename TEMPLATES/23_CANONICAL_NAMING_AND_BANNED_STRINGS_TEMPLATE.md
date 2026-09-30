# 23 — CANONICAL NAMING & BANNED STRINGS TEMPLATE

**Template ID:** `T-23-NAMING`  
**Generates:** Any name, code, or term in `SOMNARAK-WORLD/` or `GAME_BATTLE/`  
**Authority:** `REFERENCE_SOMNARAK_WIKI/SOMNARAK_NAME_REGISTRY.md` + `REFERENCE_SOMNARAK_WIKI/SOMNARAK_DOCUMENT_RULES.md` + `tools/banned_strings.txt` + `tools/seam_lint.py`

---

## DEEP KNOWLEDGE — READ BEFORE WRITING

- **Naming is law, not flavor.** A wrong name is a lore break that fails audit.
- **Sorrow Entity names** are drawn from the 292 catalog or its paired variants. When inventing narrative persons (citizens, wardens, syndicate leaders), use Korean civilian names (Min-Jae, Seol-A, Taeho, Ha-Eun, Seiyon) + rank/call-sign, never PM crossover names (Roland, Angela, Ayin, Carmen, etc. — banned).
- **SECC is immutable.** Do not “improve” a code. Copy it verbatim: `SE-{{ORIGIN}}-{{RANK}}{{POTENCY}}-{{NUM}}`. Origins C/N/O, Ranks I–V, Potencies α/β/γ/δ/ω. Element ABBRs: `[VS]` Void-Sovereign etc. are optional but must match if used.
- **Company taxonomy:** 5 Main Companies + 5 Sub Companies = 10 Primary Companies. All else = “Somnarak Outsider Factory.” Memory Archive is a municipal sanctuary, not a company — never list it among the 10.
- **Geography naming** belongs in `SOMNARAK_GEOLOGY.md` register — The Maw (terrain), The Weeping (river), Weeping corridors, Dust Flats, Crystal Peaks, Sea of Glass, Consoling Ocean [ConHeAn], Numbing Tundra [NuRoZen], Sorrow Lake. Never file terrain as SE.

---

## BANNED STRINGS — ZERO TOLERANCE (from `tools/banned_strings.txt`)

**Project Moon Crossover (NEVER in canon):**
`Abnormality`, `E.G.O`, `EGO`, `Sephirah`, `Qliphoth`, `Cogito`, `L-Corp`, `L Corporation`, `Fixer`, `Hana Association`, `Thumb`, `Index`, `Middle`, `Ring`, `Pinky`, `ZAYIN`, `TETH`, `HE`, `WAW`, `ALEPH`, `Peccatula`, `Wing` (except Somnarak’s 10 Companies context), `Nest`, `Backstreets`

**Modern / Anachronistic Slips (NEVER in canon):**
`GPS` (use `surface magnetic reference` / `Han-flow navigation`), `battery acid` (use `corrosive vitriol` / `sulfuric vitriol`), `hospital` (use `Sanatorium` / `Hospice-steel`), `phone` (use `acoustic relay`), `DNA` (use `ancestral bloodline resonance seal`), `Kevlar` (use `armored weave`), `Teflon` (use `vitrified low-friction secretion`), `depleted uranium` (use `cold-cast basalt AP`), `Amnestic` (use `Oblivion Pollen Wave`), numerical `Hz`/`kHz` (use `Harmonic Ley-Resonance` / `Infrasonic Groans` / `Ultrasonic Resonance` / `Consoling Resonance Wave`)

**Sanctioned Replacements (ALWAYS use):**
`Sorrow Entity (SE)`, `SECC`, `M.A.W. (비탄의 무장 / Bitan-ui Mujang [Armament of Woe])`, `Han (한 / 恨)`, `Reverie Directorate (몽환국 / Monghwan-guk)`, `Echo-Cores`, `Absolvohan`, `Council of Sighs`, `The Weeping (비탄의 강)`, `The Maw (심연의 아가리)`, `Grudge (원한 / Wonhan [Crimson])`, `Lament (비탄 / Bitan [Lament])`, `Void (공허 / Gongheo [Void])`, `Weight (비중 / Bijung [Weight])`, `Ferrehan (인내작업)`, `Flerehan (공감작업)`, `Pugnahan (억제작업)`, `Viderehan (관찰작업)`

---

## NAMING CONVENTIONS BY DOCUMENT TYPE

| Document | Convention | Example |
|---|---|---|
| **Sorrow Entity File** | `SE-{{ORIGIN}}-{{RANK}}{{POTENCY}}-{{NUM}}_{{English_With_Underscores}}_{{Korean}}.md` | `SE-C-IIIβ-014_The_Debt_Eater_빚을_먹는_자.md` |
| **M.A.W. Side Codex** | `SE-{{ID}}-A__SIDE_CODEX_{{Name}}.md` / `SE-{{ID}}-A` | `SE-001-A__SIDE_CODEX_The_Orphaned_Bell.md` |
| **M.A.W. Weapon** | `SE-{{ID}}-B__MAW-W_{{Name}}.md` / `MAW-W-{{NUM}}-01` | `SE-001-B__MAW-W_The_Laments_Requiem.md` |
| **M.A.W. Suit** | `SE-{{ID}}-C__MAW-S_{{Name}}.md` / `MAW-S-{{NUM}}-01` | `SE-001-C__MAW-S_The_Laments_Shroud.md` |
| **M.A.W. Stigma** | `SE-{{ID}}-D__MAW-G_{{Name}}.md` / `MAW-G-{{NUM}}-01` | `SE-001-D__MAW-G_Laments_Edge.md` |
| **Ordeal** | `Ordeal_{{COLOR}}_{{WATCH}}_{{Name}}.md` | `Ordeal_BLUE_First_Watch_The_Voice.md` |
| **Hope Transform** | `HT-{{NUM}}_{{Name}}_{{Korean}}.md` | `HT-001_The_Guiding_Light_인도의_빛.md` |
| **Unknown Entity** | `SE-{{CODE}}_{{Name}}.md` | `SE-O-IIIγ-1052_The_Glass_Silt_Drifter.md` |
| **Echo-Core** | `THE_{{ROLE}}.md` (caps) | `THE_CONTAINMENT_LEAD.md` |
| **Absolvohan** | `Part_{{N}}_Days_{{START}}_to_{{END}}_{{Title}}.md` | `Part_1_Day_0_The_Director_Wakes.md` |
| **Katabagil** | `Passage_{{N}}_{{Name}}.md` | `Passage_1_Cryptasu.md` |
| **Gieok Reading** | `Reading_{{N}}_{{Name}}.md` | `Reading_1_First_Keeper.md` |
| **Story Canto** | `CANTO_{{XX}}_{{TITLE}}_{{NAME}}.md` | `CANTO_01_THE_BASTION_ANCHOR_MIN_JAE.md` |

*Example filenames in the table above are illustrative; no such files are required to exist.*

---

## KOREAN BUFFER RULE (Outside Boxes Only)

**Inside any ````text box:** ZERO Hangul. Use Romaja: `Dohan`, `Naehan`, `Oehan`, `Gieok Jeojangso`, `Jipyeongseondae`, `Katabagil`, `Katharcheok`, `Mugenhan`.

**Outside boxes (prose, tables):** Korean **must** use two-space buffer + Romaja + English:

~~~markdown
Correct: `  한  / Han [Grief]` · `  도한  / Dohan [City Sorrow]` · `  빚을 먹는 자  / Bijeul Meokneun Ja [He Who Eats Debt]`
Wrong:   `한/Han` (no buffer) or `빚을 먹는 자` inside a ````text box
~~~

---

## PRE-GENERATION VOCABULARY GATE

Before writing any canon line, run:

```bash
grep -r -i -E "Abnormality|E\.G\.O|Sephirah|Cogito|Fixer|Nest|Backstreet|GPS|battery acid|Kevlar|Teflon|Hz" SOMNARAK-WORLD/
# Must return 0 lines. If it hits, replace per sanctioned list above.
python3 tools/seam_lint.py
python3 tools/timeline_lint.py
```

---

## VALIDATION CHECKLIST

- [ ] Every SECC/HT/Ordeal code exists or follows sanctioned numbering (no invented `SE-999`).
- [ ] No banned string in generated text (manual grep + `seam_lint.py` PASS).
- [ ] Company count = 10 (5+5); geography not filed as SE; Archive is sanctuary not company.
- [ ] File name matches convention exactly (underscores, suffixes, caps).
- [ ] Korean buffer `  [한글]  ` correct outside boxes; zero Hangul inside boxes.
- [ ] Weapon/terrain timestamps are period-agnostic (Year 0000–9999+ archetypes permitted).
