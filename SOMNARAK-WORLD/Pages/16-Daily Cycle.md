# Daily Cycle

> *Morning is a negotiation.*

**Daily Cycle** is the operational day — Watches 1 through 4.

The Daily Cycle is the city’s day, and the day is four Watches long. Watch 1 is inspection — check the Veil, assign Viderehan, verify which dossiers are quiet enough to Work; Watch 2 is assignment — full Work, Lumen tally, Research increments; Watch 3 is strain — Mugenhan rises, the planetary lattice presses the Veil, and the House checks whether neglect will summon an Ordeal that Watch; Watch 4 is accounting — Research is bound, Reverberations are checked, containment is priced, and the day either holds or is lost to Fracture. The cycle is archived under `Master_Codices/03_Watch_Cycle/` alongside sixteen battle systems that are not separate from the day but are the day’s executable form, a point that makes [36-Tactical Engine](36-Tactical%20Engine.md) the combat analogue of this schedule.

Between Watches the House checks three thresholds that never sleep. The first is Reverberation — the nine Floor-bound ruptures tied to Echo-Cores, one per Floor from Floors 1 to 8 plus Central — which must be resolved by completing the Floor’s Reverberation Work before the Watch ends or Containment Level will rise. The second is Ordeal — sixty files across five Colors (BLACK Weight, BLUE Lament, GREY Grudge, PALE Void, PURPLE Raw Han) and four Watches (First, Second, Third, Tide) — which surge when Watch Meltdowns are left to thin the Veil. The third is Containment Level itself — Tranquil through Stirred, Strained, Fractured, to Rupture — which gates which Ordeals may appear that Watch. A day that survives all three tallies its Lumen and Research; a day that fails any one is a lesson filed under `GAME_BATTLE/`’s sixteen scenarios.

In the Reverie Directorate, this day was repeated 1,778 times between Years 4,232 and 4,238 — six external years — as a 365-day loop locked by the Mnemonic Generator beneath the Alpha Tree, each cycle producing 0.02 tons Han-crystal until the sum became supercritical and fueled the Absolvohan at Cycle 1,778. That repetition is why Lumen yield examples are given per Work — a successful Viderehan on `SE-C-IIIβ-014 The Debt Eater` yielding about 8 Lumen Units, a failed Work yielding Fracture instead — and why the same yield logic governs post-Dawn Watches on The Lantern, at Horizon Caravan’s six Arcs, and inside Gieok’s seven strata. The day is thus both municipal time and tactical time, and [13-Operations](13-Operations.md) translates the day’s promises into floor-issued missions that the Cycle then prices.

The Daily Cycle is also how the House learns to route, not maximize, because the planetary loop that the city runs is Weeping→Han→Lumen→Watch→Veil→Weeping, and over-extraction deepens the Maw that Katabagil first mapped at −2,000→−7,200 across seven Descents, a lesson the city learned when the Maw first opened at Cheongula in Year 200 and consumed a thousand as recorded in `Master_Codices/01_Cosmology_and_World_Order/SOMNARAK_CHEONGULA.md` and `SOMNARAK_GEOLOGY.md` where the same stratification is kept as terrain, not as entity. Each Watch therefore checks not only which dossier to Work but which Veil the Lumen that Work will cost, with Lumen yield examples that the House keeps visible — a successful Viderehan on `SE-C-IIIβ-014` yielding about 8 Lumen Units on Whisper, more for higher Risk, paid back as Fracture when the Veil is held poorly — and with portable cells after the Dawn that carry the same physics to Horizon Caravan’s six Arcs and Gieok’s seven strata at 40,000 LU primary plus 5,000 LU per floor plus 1,200 LU tertiary, green/amber/red gated, so that Surge logic inside Facility 01 remains Surge logic outside it and containment remains a routing problem rather than a combat problem, as priced in `SOMNARAK_LUMEN.md` and `SOMNARAK_WARDEN_GUIDE.md` where the House keeps the same filing without cutting, and the House never cuts — when a new grief is felt it is filed as a variant of one of the 292 plus 88 plus 12, not as a 293rd, and when a new Watch is felt it is filed as a variant of one of the four, not as a fifth, so the day remains four Watches and the city remains accountable.

In the Directorate the day was repeated 1,778 times between Years 4,232–4,238 — six external years made procedural by the Mnemonic Generator beneath the Alpha Tree  [알파 트리]  (Alpa Teuri) locked into a 365-day loop (366-day Mnemonic Engine in Absolvohan) — each cycle producing 0.02 tons Han-crystal until supercritical at Cycle 1,778 fueled the Absolvohan for twelve Hope Bearers, and that repetition is why the House teaches the day as both municipal time and tactical time. Four Watches — inspection (check Veil, assign Viderehan, verify quiet dossiers), assignment (full Work, tally Lumen, increment Research), strain (Mugenhan rises, Veil thins, check Ordeal gating), accounting (bind Research, check Reverberation nine and Containment 1→5, tally day as hold or loss) — are executed through the decoupled state machine and JSON battle schema in `Tactical_Combat_Engine/README.md` and `GAME_BATTLE/`’s sixteen scenarios, where Short 10 / Medium 16 / Long 20+ turn bands and ten-node grid with Range Bands price the same day as the municipal log does, so that a Warden who learns Daily Cycle learns Tactical and a Warden who learns Tactical learns Operations, as filed under `Master_Codices/03_Watch_Cycle/` alongside sixteen battle systems that are not separate from the day but are the day’s executable form, a practice the city keeps without cutting like .gg cuts when a paragraph is unfinished, because the backing directory is the single source of truth and the wiki is its ledger, not its replacement.

```text
+========================================================================+
|                  SOMNARAK — DAILY CYCLE                                |
+------------------------------------------------------------------------+
| Watches                  | 1 · 2 · 3 · 4                               |
| Currency                 | Lumen (boxed Han)                           |
| Archive                  | Master_Codices/03_Watch_Cycle (16 systems)  |
+========================================================================+
```

## The Four Watches

| Watch | Function |
| --- | --- |
| Watch 1 | Inspection — check Veil, assign Viderehan |
| Watch 2 | Assignment — full Work, Lumen tally |
| Watch 3 | Strain — Mugenhan rises, Ordeal check |
| Watch 4 | Accounting — Research, Reverberation, containment |

Between Watches the House checks Reverberation, Ordeal (60), and Containment Level (1 to 5). Day-end grants Lumen and Research.

In the Reverie Directorate, this 365-day Watch was repeated 1,778 times between Years 4,232 and 4,238 — six external years. It underwrites sixteen battle scenarios under `GAME_BATTLE/`.

## Example Yield

Successful Viderehan on `SE-C-IIIβ-014` yields about 8 Lumen; failure yields Fracture.

## See also

- [13-Operations](13-Operations.md)
- [36-Tactical Engine](36-Tactical%20Engine.md)
