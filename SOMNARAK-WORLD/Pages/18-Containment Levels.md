# Containment Levels

> *A bell that never stops ringing.*

**Containment Levels** measure facility stability during the day.

Containment Levels measure how much the House forgets that it is a house. The scale runs 1 to 5 — Tranquil, Stirred, Strained, Fractured, Rupture — and is signaled by two threads that never stop: Lumen flow and Fracture count. At Level 1 the Veil holds and First Watch is quiet; at Level 2 the Veil thins and First Watch Ordeals begin to walk the halls; at Level 3 and 4 Second and Third Watch Ordeals and then paired Watches appear; at Level 5 the Veil is a suggestion, sixty Ordeals and nine Reverberations can chain, the House’s bell never stops ringing, and the distinction between Threat (Risk Whisper to Sovereign, which measures an entity) and Containment (1 to 5, which measures the House) becomes the only thing that keeps a Warden from mistaking a loud sorrow for a failing Floor, a distinction tabulated in `CANONICAL_METRICS.json` and `SOMNARAK_WARDEN_GUIDE.md`.

Rising Level triggers both Ordeals and Reverberations, and the House prices each Watch accordingly. `CANON_TIMELINE.md`’s Watch logic — Level 1 to 2 gating First Watch, Level 3 to 4 gating Second and Third, Level 5 gating Tide Watch (e.g., `Ordeal_BLACK_Tide_Watch_The_Mountain`, the late-war Weight incursion that exceeds ordinary suppression doctrine) — is not a story but a schedule, and the sixteen battle scenarios under `GAME_BATTLE/` gate the same way, so that a Warden who learns Containment learns battle. The bell’s tone is the audible form of the same logic: a single tone at Stirred, a chain at Fractured, a continuous ring at Rupture, each tone mapping to a table that tells which Colors may surge that Watch and how many Veil points the surge will cost.

Response is therefore procedural, not heroic. At Stirred, complete the Floor’s Reverberation Work before the Watch ends; at Strained, quarantine Relic expansions rather than pursue them and stabilize Lumen before Veil; at Fractured and Rupture, accept that the day may be lost and trade Lumen for survival, because a lost day can be retried from the last accounting while a lost Veil cannot. Operations  [13-Operations](13-Operations.md) file the promise (maintain Maw’s Keep at Level 2 through Watch 2), Tactical Engine  [36-Tactical Engine](36-Tactical%20Engine.md) executes it (Tension → Clash → Resolution across Short 10, Medium 16, Long 20-plus turn bands), and the next Watch checks the Level again. See [10-Ordeals](10-Ordeals.md) for the sixty that walk at each Level and [11-Reverberations](11-Reverberations.md) for the nine that reverberate when the Level was earned by Lumen rupture rather than by neglect.

```text
+========================================================================+
|              SOMNARAK — CONTAINMENT LEVELS                             |
+------------------------------------------------------------------------+
| Scale                    | 1 to 5 (Tranquil to Rupture)                |
| Signal                   | Lumen flow and Fracture count               |
| Archive                  | Master_Codices/03_Watch_Cycle (16 systems)  |
+========================================================================+
```

## Scale

| Level | Name | State |
| --- | --- | --- |
| 1 | Tranquil | Veil holds, First Watch only |
| 2 | Stirred | Veil thins, First Watch Ordeals |
| 3 | Strained | Second and Third Watch Ordeals |
| 4 | Fractured | Multiple Watches, Reverberations chain |
| 5 | Rupture | Veil is suggestion — Ordeals (60) walk, nine Cores reverberate |

Sixteen battle scenarios gate Ordeals per Watch. Threat versus Containment are distinct: Risk Whisper to Sovereign measures entity, Containment 1 to 5 measures House.

## Response

Rising Level triggers Ordeals and Reverberations. Check `CANON_TIMELINE.md` Watch logic: Level 1 to 2 → First Watch, 3 to 4 → Second and Third, 5 → Tide Watch (e.g., `Ordeal_BLACK_Tide_Watch_The_Mountain`).

## See also

- [10-Ordeals](10-Ordeals.md)
- [11-Reverberations](11-Reverberations.md)
- [16-Daily Cycle](16-Daily%20Cycle.md)
