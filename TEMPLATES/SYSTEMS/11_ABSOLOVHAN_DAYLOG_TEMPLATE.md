# 11 — ABSOLOVHAN DAYLOG TEMPLATE

**Template ID:** `T-11-ABSO`  
**Generates:** `SOMNARAK-WORLD/The_Absolvohan/Part_{{N}}_Days_{{RANGE}}.md`  
**Authority:** `SOMNARAK-WORLD/The_Absolvohan/README.md` + `ABSOLOVHAN_OVERVIEW.md` + Global Primer Laws 1,2

---

## DEEP KNOWLEDGE — READ BEFORE WRITING

- **Absolvohan = 366 days across 1,778 Cycles** — the repeating Day 0–365 loop inside Facility 01. Every Part covers a date range + Overview. Day 0 is Director Wakes; Day 365+ is Epilogue / Quiet Season.
- **Days are operational chronicles, not wiki articles.** Each Day has Time, Floor, Cast, Sorrow Pressure, Work log, Combat Gauntlet (turn-by-turn with 10-Node Grid, Speed-to-AP, 4P Framework, Dual-Threshold), and Aftermath.
- **Cycles are ONLY inside Absolvohan.** Outside references to “Cycle 1,778” must be retrospective survivor testimony, not current calendar.
- **There are 9 Parts:** Part_1 Day 0–Days 25 to Part_9 Days 350–365. Keep sequence and never skip Days.

---

## FILE NAMING

```
SOMNARAK-WORLD/The_Absolvohan/Part_{{N}}_Days_{{START}}_to_{{END}}_{{Title}}.md
```

Example: `Part_1_Day_0_The_Director_Wakes.md`

---

## SCAFFOLD

~~~markdown
# The Absolvohan — Part {{N}}: {{TITLE_EN}} (Days {{START}}–{{END}})

> *“{{Epigraph — the facility’s mood across these days.}}”*

**Chronicle ID:** `ABSO-P{{N}}-{{START}}-{{END}}`  
**Date Range:** Day {{START}} — Day {{END}} (Cycle {{1–1778}})  
**Author:** {{Floor Lead — e.g., Containment Lead Dekan, Floor 2}}  
**Classification:** Facility 01 — Absolvohan Cycle Log

## OVERVIEW OF THIS PART

{{1 paragraph: what this date block means in the year-long loop — early Dawn probes, mid-year Rust, late-year Meltdown, etc.}}

## DAY {{N}} — {{DAY_TITLE_EN}} — {{KOREAN_TITLE}}

**Time:** {{HH:MM}} · **Floor:** {{1–8}} · **Cast:** {{Operatives + Echo-Core}}  
**Sorrow Pressure:** {{15–85% Gauge}} · **Ambient Han:** {{mMb}}  
**Operational Objective:** {{What must be held/sealed/extracted today}}

### Morning Log — Work & Observation

{{Work types performed, Gauge changes, what was learned — respect Two-Work-Type for Object/Place.}}

### Afternoon — Combat Gauntlet

{{Full turn-by-turn GBS integration:}}

**Operative Base Speed Die & Natural Range Band | M.A.W.-W Speed/Range Modifier | Four P-Framework (Passives, Panic, Parry, Posture) | Dual-Threshold Stagger (60% Rupture, 25% Meltdown) | Sorrow Tide tick (+10% Han saturation) per 6-turn Phase**

- **Turn 1–6 (Phase 1):** {{10-Node grid deployment, Speed-to-AP, clashes, stagger checks, Tide tick. Name Operatives and SECC.}}
- **Turn 7–12 (Phase 2):** {{Escalation, boss stance, part rupture at 60%.}}
- **Turn 13–18 (Phase 3 if applicable):** {{Tide, Meltdown at 25%, resolution.}}

### Evening — Aftermath & Quiet

{{Injuries, Composure, Veil repairs, letters that were not sent, what was carried forward to next Day.}}

## DAY {{N+1}} — {{TITLE}} (Repeat structure per Day in range)

{{Same 3 blocks: Morning / Afternoon Gauntlet / Evening}}

## PART CLOSURE — WHAT THIS BLOCK TEACHES

{{1 paragraph cross-Day synthesis: how this block changes the next. Seed for next Part.}}

*For full technical specifications, see `SOMNARAK-WORLD/Master_Codices/03_Systems_Combat_Engine_and_Physics/SOMNARAK_BATTLE_SYSTEM.md` and `ABSOLOVHAN_OVERVIEW.md`.*
~~~

---

## VALIDATION CHECKLIST

- [ ] Day range sequential and non-overlapping with other Parts.
- [ ] Every Day has Morning + Afternoon Gauntlet (with 10-Node + 4P + Dual-Threshold) + Evening.
- [ ] Cycle numbers only inside Absolvohan logs (outside refs are retrospective testimony if any).
- [ ] Tone is operational chronicle, not wiki.
