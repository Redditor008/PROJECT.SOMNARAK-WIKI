# R-62 — The Stamp

**Stated by the archive owner, 2026-10-25:**

> *"YOU SHOULD USED xxx Time[Can Be Days/Month/Years/Just Hour/Minute] BEFORE [REDACTED] Happened The
> Redacted Will Only Be Shown On The 00:00 Before XXX Happened Instead Of [REDACTED] So There Is A
> Clear Time Stamp For Easier Pinning"*

## 1. What he asked for

A **stamp** on every scene: the distance to the thing the scene is counting toward, written in the
largest honest unit, so a reader can pin the scene without doing arithmetic across twenty thousand
words. Where the event at the other end of that distance has no date, it is not guessed at — it is
written `[REDACTED]`, and it stays redacted until the story reaches the midnight before it.

## 2. The line

One line, directly under the heading, before the first line of prose:

```text
> **STAMP — 9 days before [REDACTED] happened · 17:40 · Floor 3, the bench**
```

**Three fields, in this order, separated by ` · `** — offset, clock, place. A fourth may follow only
when the scene moves inside itself (`then Day 11 in the same room`).

## 3. The unit is chosen by distance

| distance | unit |
|---|---|
| an era | years |
| an appointment, a season | months |
| a death, a filing, a span of shifts | days |
| a single night | hours |
| a seal closing | minutes |

A scene six years away is not stamped in days. A scene forty minutes away is not stamped in years.

## 4. The bracket

`[REDACTED]` is not a placeholder. It is the honest state of a record that has refused to date an
event, and it may not be filled in for the convenience of the table. Everything before the scene is
counted **toward** the bracket; everything after it is counted **from** the named event.

## 5. The lift

**The bracket is replaced exactly once, at 00:00 on the day of the anchor.** That scene is stamped
from midnight, and from that line onward the bracket does not appear again — not in a stamp, not in a
sentence, not in a heading.

```text
> **STAMP — 00:00 to 23:41, the day of the Solidification. The redaction lifts here · 23:24 · Floor 3**
```

## 6. What a stamp is not

It is not prose. It carries no italics, no dialogue, no gloss, and it never explains itself. The key
is this rule and § IV.6 of the structure standard; it is never printed inside the story.

## 7. Enforcement

`check_scene_stamps.py` (gate 56) fails any converted file with a scene that has no stamp, a stamp
missing a field, an offset with no unit, or a bracket that outlives its lift. Files not yet converted
are carried as a counted debt in the gate output, file by file, until they are stamped.
