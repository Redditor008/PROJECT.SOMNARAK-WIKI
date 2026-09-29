# Risk Levels

> *Risk is how loudly the sorrow remembers.*

**Risk Levels** rank Sorrow Entities from Whisper to Sovereign.

Risk Levels rank how loudly a sorrow remembers, and the House answers with how much Veil it is willing to risk. The scale runs I Whisper (Residue, 46 dossiers) through II Murmur (Echo, 70), III Lament (Fragment, 82), IV Wail (Entity, 79), to V Starless (Sovereign, 10), plus five without fixed Rank where Hazard and Time nuances override Rank, as reconciled in `Sorrow_Entities/README.md`, `CANONICAL_REGISTRY.json`, and `Master_Codices/05_Entities_Tales_and_Fractures/SOMNARAK_ENTITY_CODEX.md`. Potency α Minor through ω Catastrophic refines within Rank, and Sovereign is city-scale — a sorrow that the House cannot keep on a single Floor without risking fusion if stored beside its kin. The scale borrows its cadence from wiki.gg’s ZAYIN through ALEPH but translates it into Somnarak’s audible metaphor: a Whisper can be Worked with a single specialist, a Starless requires a Floor to forget it had walls.

Distribution is municipal fact, not flavor. Of 292 entities, Whisper I holds 46 quiet rooms, Murmur II holds 70 murmuring halls, Fragment III holds 82 lamenting corridors, Entity IV holds 79 wailing Floors, Sovereign V holds 10 city-scale threats, and five Hazard and Time dossiers remain unfixed because their activation logic — Relic Time that skips, Unshaped abstraction that depends on being observed — cannot be ranked without lying. Sovereigns are further split by geography: thirteen City Sovereigns plus one Outside Sovereign `SE-O-Vγ-003 Wilderness Tide`  [야생의 파도]  (Yasaeng-ui Pado), the only sorrow the city allows to remain planetary terrain rather than containment, and zero Inner Sovereigns because personal trauma cannot reach Sovereign without becoming City, a point that keeps `SOMNARAK_GEOLOGY.md` from being misread as a catalog. The sole Outside Sovereign is therefore both exception and proof.

Risk determines Lumen yield versus breach cost, and the House prices each Watch accordingly. A higher Risk pays more Lumen per successful Work — roughly 8 Lumen for a Whisper Place such as `SE-C-IIIβ-014 The Debt Eater` on Viderehan, more for a Lament or Wail — but its Mugenhan failure costs more Veil when Work is neglected or when the wrong Work-Type is assigned. The sixteen battle scenarios under `GAME_BATTLE/` gate by Risk, and [38-Classification Code](38-Classification%20Code.md) encodes Risk as Rank in SECC so that `SE-C-IIIβ-014` declares Fragment without opening the dossier and the House can sort its watchlist before dawn. To read Risk is to know, before any narrative, what the House can afford to Work that Watch. The same filing is maintained in `SOMNARAK_ENTITY_CODEX.md`, `CANONICAL_METRICS.json`, and `CANONICAL_REGISTRY.json`, where Origin, Rank, Potency, Element, and Manifestation are kept sortable for watch planning across the sixteen battle systems and forty-four Master Codices.

Rank is also retrieval time, and the city keeps that retrieval visible so that it never cuts like .gg cuts when a paragraph is unfinished. I Whisper (Residue, 46) is a quiet room that a single specialist can hold with Viderehan for 8 LU and a single M.A.W. Gift that replaces the previous gift in that slot; II Murmur (Echo, 70) is a murmuring hall that needs a Floor to remember it had walls; III Lament (Fragment, 82) is a lamenting corridor where the Sorrow Gauge is most legible; IV Wail (Entity, 79) is a wailing Floor where the Behavior table’s Decrease/Stable/Increase per Work must be read as dossier-specific, not as universal permission; V Starless (Sovereign, 10) is a city-scale threat where the House cannot keep the sorrow on a single Floor without risking fusion if stored beside its kin (Three Birds, Three Sisters, debt-kin indexed in `Master_Codices/05_Entities_Tales_and_Fractures/SOMNARAK_ENTITIES.md`), plus five Hazard/Time dossiers unfixed because their activation logic — Relic Time that skips like `SE-C-IIIβ-036 Cracked Hourglass`  [금이 간 모래시계]  or `044 Broken Clock`  [부서진 시계] , Unshaped abstraction that depends on being observed like `SE-O-IIIγ-916 Allhallow`  [유령의 시간]  — cannot be ranked without lying, a nuance the House keeps by not ranking them rather than by cutting them. The same ranking is taught in wiki.gg’s ZAYIN→ALEPH but translated into Somnarak’s audible metaphor — Whisper→Starless — so that the cadence is kept while the names are Somnarak’s, as audited by `seam_lint.py` at 74 columns exact.

Sovereigns are also geography, and the city keeps that geography because the `.gg` habit of cutting unfinished geography would hide that thirteen City Sovereigns plus one Outside Sovereign `SE-O-Vγ-003 Wilderness Tide`  [야생의 파도]  (Yasaeng-ui Pado) plus zero Inner Sovereigns is not a count but a law: City  [도한]  (Dohan) 159 / Inner  [내한]  (Naehan) 72 / Outside  [외한]  (Oehan) 61 describe where Han pooled, and personal trauma cannot reach Sovereign without becoming City, while the Outside Sovereign remains tide-like and is therefore kept as planetary terrain in `SOMNARAK_GEOLOGY.md` — the sole exception the city allows to remain tide rather than containment — and no other macro-geographical feature (Undercity, Raw, Desolate Outskirts, Wound, Maw at −2,000→−7,200 via Katabagil seven Descents, Weeping  [비탄의 강] ) is filed as an entity, a discipline that keeps `SOMNARAK_GEOLOGY.md` from being misread as a catalog and Gieok from being misfiled as a company. The House therefore never cuts — when a new Sovereign is felt it is filed as a variant of one of the ten plus one, not as an eleventh, and when a new grief is felt it is filed as a variant of one of the 292 plus 88 plus 12, not as a 293rd, and fandom’s completion of wiki.gg’s stubs is kept as citation, not as replacement, so that the city never invents to fill a stub but files to keep what it has.

```text
+========================================================================+
|                 SOMNARAK — RISK LEVELS                                 |
+------------------------------------------------------------------------+
| Scale                    | Whisper · Murmur · Lament · Wail · Starless |
| Archive                  | Sorrow_Entities/* and SECC                  |
+========================================================================+
```

## Scale

Risk is how much the House forgets. Whisper is a quiet room; Starless is a Floor that forgets it had walls.

| Rank | Name | Potency | Behavior |
| --- | --- | --- | --- |
| I | Whisper  [속삭임]  (Soksagim) | Residue | Quiet room |
| II | Murmur  [웅얼거림]  (Wungeolgeorim) | Echo | Murmuring hall |
| III | Lament  [비명]  (Bimyeong) | Fragment | Lamenting corridor |
| IV | Wail  [통곡]  (Tonggok) | Entity | Wailing Floor |
| V | Starless  [별 없는]  (Byeol Eomneun) | Sovereign | City-scale |

Potency α to ω refines within Rank; Sovereign is city-scale.

## Distribution

Per `Sorrow_Entities/README` and `CANONICAL_REGISTRY.json`:

| Risk | Count |
| --- | --- |
| Whisper / I Residue | 46 |
| Murmur / II Echo | 70 |
| Lament / III Fragment | 82 |
| Wail / IV Entity | 79 |
| Starless / V Sovereign | 10 |
| Unfixed (Hazard, Time) | 5 |

Sovereigns: 13 City plus 1 Outside `SE-O-Vγ-003 Wilderness Tide` plus 0 Inner.

Higher Risk pays more Lumen per Work, but its Mugenhan failure costs more Veil.

## See also

- [07-Sorrow Entities](07-Sorrow%20Entities.md)
- [38-Classification Code](38-Classification%20Code.md)
