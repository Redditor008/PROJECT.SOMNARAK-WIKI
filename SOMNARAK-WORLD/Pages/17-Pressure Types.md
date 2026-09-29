# Pressure Types

> *Sorrow cuts in four directions.*

**Pressure Types** are the four damages sorrow inflicts.

Pressure is how sorrow cuts, and the House names four directions because grief does not wound in one way. Rue is Grudge  [원한]  (Wonhan) rendered as Crimson — body strain that breaks skin, bone, and compliance; Sable is Lament rendered as Black — will’s erosion, the slow hollowing that makes a specialist agree with a sorrow; Pale is Void  [공허]  (Gongheo) rendered as Pale White — mind’s erasure, where one percent Pale equals five percent of Max HP as conceptual damage that bypasses armor logic; and Gloom is Weight rendered as mixed — the combined burden that the House uses when a dossier refuses to decide. Per `Sorrow_Entities/README.md` these are also called Grudge, Lament, Void, and Weight as Elements, and per `CANONICAL_METRICS.json` each of the 292 dossiers declares which Pressures it deals and which it resists.

Choosing a Work-Type without checking Pressure is how specialists are lost, because Pressure and Work interact asymmetrically. A Place sorrow that inflicts Pale will punish a Pugnahan suppression even if the Behavior table marks Pugnahan as technically available for Subjects; an Object that deals Rue will reward a patient Ferrehan endurance over a hasty Viderehan observation. Example resistances make the lesson concrete: `SE-C-IIIγ-031 The Observing Bird` (Lament) resists Grudge-type Pressure and is therefore safer to approach with a Grudge-aligned M.A.W. set, while `SE-O-IIIγ-916 Allhallow` (Void)  [유령의 시간]  resists Lament, is weak to Grudge, and will therefore punish a Lament-leaning cadre. The Codex therefore teaches that dossier, Pressure, and M.A.W. must be read as a triple, not as a pair, and that the triple is filed per entity in `MAW_Codex_Sets/` and per system in `Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_MAW_CODEX.md`.

Tactically, Pressure is both damage type and narrative type. In `Tactical_Combat_Engine/` and `GAME_BATTLE/`’s sixteen scenarios, each battle tracks Han density, atmosphere, and Fracture warnings through Pressure bands, and the decoupled state machine treats Pale differently from Rue because Pale scales with Max HP while Rue scales with current HP. Outside combat, Pressure is encodeable: [38-Classification Code](38-Classification%20Code.md) carries Element as a trailing field, so `SE-C-IIIβ-014` declares Void without opening the dossier, and the House can sort its watchlist by which Pressure the next Watch can afford to meet. To train this sorting, [36-Tactical Engine](36-Tactical%20Engine.md) pairs Pressure interaction with Work resolution and Watch accounting, making Pressure not an afterthought but the first filter before any assignment. The same filing is maintained in `SOMNARAK_ENTITY_CODEX.md`, `CANONICAL_METRICS.json`, and `CANONICAL_REGISTRY.json`, where Origin, Rank, Potency, Element, and Manifestation are kept sortable for watch planning across the sixteen battle systems and forty-four Master Codices.

```text
+========================================================================+
|                SOMNARAK — PRESSURE TYPES                               |
+------------------------------------------------------------------------+
| Types                    | Rue · Sable · Pale · Gloom                  |
| Elements                 | Grudge · Lament · Void · Weight             |
| Archive                  | Sorrow_Entities/* · Master_Codices/03       |
+========================================================================+
```

## Four Pressures

| Pressure | Element | Target | Note |
| --- | --- | --- | --- |
| Rue | Grudge  [원한]  (Wonhan) | Body — Crimson | Physical strain |
| Sable | Lament | Will — Black | Erosion of composure |
| Pale | Void  [공허]  (Gongheo) | Mind — Pale White | 1 percent = 5 percent Max HP |
| Gloom | Weight | All — Mixed | Combined burden |

Per README Grudge, Lament, Void, Weight are the four canonical Elements.

## Tactics

Choosing a Work-Type without checking Pressure is how specialists are lost.

Example: `SE-C-IIIγ-031 Observing Bird` (Lament) resists Grudge-type Pressure but is vulnerable to Void. `SE-O-IIIγ-916 Allhallow` (Void) resists Lament, weak to Grudge.

See [38-Classification Code](38-Classification%20Code.md) for how Pressure is encoded per entity (Element field).

## See also

- [36-Tactical Engine](36-Tactical%20Engine.md)
- [38-Classification Code](38-Classification%20Code.md)
