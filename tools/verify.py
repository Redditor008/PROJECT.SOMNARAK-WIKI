#!/usr/bin/env python3
"""verify.py <path> — per-dossier residue check.

Rebuilt in-repo after the helper copy outside the repository was lost.
Reports four things:
  RESIDUAL n  — lines containing a known stock phrase (the generator's own wording)
  seam        — orphaned sentence fragments left by a bad splice
  pipe        — every table row closes with '|'
  dupes       — paragraphs repeated verbatim in the same file
"""
import io, sys, re

STOCK = [
    "signature confirmed at", "Work Type responses logged:",
    "register is the dominant channel of contact",
    "pressure is different from standard", "First contact report:",
    "becomes a texture you can map", "becomes a force rather than a feeling",
    "does not leave you immediately. It lingers", "Stigmas are granted at random by",
    "is a conditional extension of", "classification is valid and necessary",
    "descriptor is not decorative", "Recheck containment status, Sorrow Gauge trend",
    "Viderehan and Ferrehan are valid Work Types.", "accumulates in the",
    "this is not standard", "Monitor the ", "is logged as a ",
    "Failed resistance applies pressure to", "Prolonged exposure may produce the entity's",
    "M.A.W. use carries the cost recorded", "Personnel should identify it by these markers",
    "The entity is fixed at its registered position",
    "manifestation is the primary identifying feature",
    "signature is unmistakable", "Operator, grade, Sorrow Gauge, emotional condition",
    "Activation time, visual feedback, effect strength",
    "Duration, activations, attribute changes, rejection signs",
    "Removal or discharge, injuries, lingering effects",
    "Flerehan and Pugnahan are not effective against this entity type",
]
SEAM = [" .", " ,", "..", "—.", "the the ", "Profile: The.", "Rule: The relic remains."]

def main(path):
    s = io.open(path, encoding="utf-8").read()
    lines = s.split("\n")
    hits = [(i + 1, l) for i, l in enumerate(lines) if any(k in l for k in STOCK)]
    print("RESIDUAL %d" % len(hits))
    for i, l in enumerate(hits[:40]):
        print("  %5d %s" % (l[0], l[1][:100]))
    seam = [(i + 1, k) for i, l in enumerate(lines) for k in SEAM if k in l]
    print("seam %s" % ([x[1] for x in seam] or []))
    nopipe = [l for l in lines if l.startswith("|") and not l.rstrip().endswith("|")]
    print("pipe %s" % (not nopipe))
    for l in nopipe:
        print("   NOPIPE: %s" % l[:96])
    paras, seen, dupes = [p.strip() for p in s.split("\n\n")], set(), []
    for p in paras:
        if len(p) > 120 and not p.startswith("|"):
            if p in seen:
                dupes.append(p[:60])
            seen.add(p)
    print("dupes %s" % dupes)
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
