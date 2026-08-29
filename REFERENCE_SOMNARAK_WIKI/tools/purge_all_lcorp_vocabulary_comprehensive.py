#!/usr/bin/env python3
"""
tools/purge_all_lcorp_vocabulary_comprehensive.py
Fast, compiled regex replacements across all HTML, JS, CSS files.
"""

import os, re

WIKI_DIR = "/home/user/01_Somnarak_Wiki"

RAW_REPLACEMENTS = [
    (re.compile(r"\bL-Corp\b"), "The Reverie Directorate"),
    (re.compile(r"\bL Corp\b"), "The Reverie Directorate"),
    (re.compile(r"\bL\.Corp\b"), "The Reverie Directorate"),
    (re.compile(r"\bLobotomy Corporation\b"), "The Reverie Directorate"),
    (re.compile(r"\bLobotomy Corp\b"), "The Reverie Directorate"),
    (re.compile(r"\bLobotomy\b"), "Directorate"),
    (re.compile(r"\bProject Moon\b"), "Somnarak"),
    (re.compile(r"\bProjectMoon\b"), "Somnarak"),
    (re.compile(r"\bAbnormality\b"), "Sorrow Entity"),
    (re.compile(r"\bAbnormalities\b"), "Sorrow Entities"),
    (re.compile(r"\bAbno\b"), "Sorrow Entity"),
    (re.compile(r"\bAbnos\b"), "Sorrow Entities"),
    (re.compile(r"\bE\.G\.O\b"), "M.A.W."),
    (re.compile(r"\bE\.G\.O\.\b"), "M.A.W."),
    (re.compile(r"\bEGO\b"), "M.A.W."),
    (re.compile(r"\bEGO-Corrosion\b"), "M.A.W.-Corrosion"),
    (re.compile(r"\bEGO Corrosion\b"), "M.A.W. Corrosion"),
    (re.compile(r"\bEGO corrosion\b"), "M.A.W. corrosion"),
    (re.compile(r"\bego corrosion\b"), "M.A.W. corrosion"),
    (re.compile(r"\bego\b"), "M.A.W."),
    (re.compile(r"\bEnkephalin\b"), "Han-Flux"),
    (re.compile(r"\benkephalin\b"), "Han-flux"),
    (re.compile(r"\bPE-Box\b"), "Positive Han-Flux"),
    (re.compile(r"\bPE-Boxes\b"), "Positive Han-Flux"),
    (re.compile(r"\bPE Box\b"), "Positive Han-Flux"),
    (re.compile(r"\bPE Boxes\b"), "Positive Han-Flux"),
    (re.compile(r"\bPE box\b"), "Positive Han-Flux"),
    (re.compile(r"\bPE boxes\b"), "Positive Han-Flux"),
    (re.compile(r"\bNE-Box\b"), "Negative Han-Flux"),
    (re.compile(r"\bNE-Boxes\b"), "Negative Han-Flux"),
    (re.compile(r"\bNE Box\b"), "Negative Han-Flux"),
    (re.compile(r"\bNE Boxes\b"), "Negative Han-Flux"),
    (re.compile(r"\bNE box\b"), "Negative Han-Flux"),
    (re.compile(r"\bNE boxes\b"), "Negative Han-Flux"),
    (re.compile(r"\bQliphoth Counter\b"), "Coherence Counter"),
    (re.compile(r"\bqliphoth counter\b"), "coherence counter"),
    (re.compile(r"\bQliphoth Meltdown\b"), "Resonance Meltdown"),
    (re.compile(r"\bqliphoth meltdown\b"), "resonance meltdown"),
    (re.compile(r"\bQliphoth\b"), "Coherence"),
    (re.compile(r"\bqliphoth\b"), "coherence"),
    (re.compile(r"\bSephirah\b"), "Echo-Core Lead"),
    (re.compile(r"\bSephirot\b"), "Echo-Core Leads"),
    (re.compile(r"\bSephiroth\b"), "Echo-Core Leads"),
    (re.compile(r"\bsephirah\b"), "Echo-Core lead"),
    (re.compile(r"\bsephirot\b"), "Echo-Core leads"),
    (re.compile(r"\bsephiroth\b"), "Echo-Core leads"),
    (re.compile(r"\bFortitude\b"), "Resolve"),
    (re.compile(r"\bfortitude\b"), "resolve"),
    (re.compile(r"\bPrudence\b"), "Resilience"),
    (re.compile(r"\bprudence\b"), "resilience"),
    (re.compile(r"\bTemperance\b"), "Composure"),
    (re.compile(r"\btemperance\b"), "composure"),
    (re.compile(r"\bJustice stat\b"), "Clarity stat"),
    (re.compile(r"\bJustice attribute\b"), "Clarity attribute"),
    (re.compile(r"\bJustice affinity\b"), "Clarity affinity"),
    (re.compile(r"\bJustice \(정의/속도\)\b"), "Clarity (명료성/속도)"),
    (re.compile(r"\bJustice Level\b"), "Clarity Level"),
    (re.compile(r"\bJustice IV\b"), "Clarity IV"),
    (re.compile(r"\bJustice V\b"), "Clarity V"),
    (re.compile(r"\bJustice III\b"), "Clarity III"),
    (re.compile(r"\bJustice II\b"), "Clarity II"),
    (re.compile(r"\bJustice I\b"), "Clarity I"),
    (re.compile(r"\bInstinct Work\b"), "Observation Work"),
    (re.compile(r"\bInstinct work\b"), "Observation work"),
    (re.compile(r"\binstinct work\b"), "observation work"),
    (re.compile(r"\bAttachment Work\b"), "Extraction Work"),
    (re.compile(r"\bAttachment work\b"), "Extraction work"),
    (re.compile(r"\battachment work\b"), "extraction work"),
    (re.compile(r"\bRepression Work\b"), "Restraint Work"),
    (re.compile(r"\bRepression work\b"), "Restraint work"),
    (re.compile(r"\brepression work\b"), "restraint work")
]

def purge_files():
    total_mods = 0
    for root, dirs, files in os.walk(WIKI_DIR):
        if "downloads" in root or "assets/art" in root or "assets/icons" in root:
            continue
        for file in files:
            if file.endswith((".html", ".js", ".css")):
                path = os.path.join(root, file)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()

                    new_content = content
                    for reg, repl in RAW_REPLACEMENTS:
                        new_content = reg.sub(repl, new_content)

                    if new_content != content:
                        with open(path, "w", encoding="utf-8") as f:
                            f.write(new_content)
                        total_mods += 1
                except Exception as e:
                    print(f"Error on {path}: {e}")

    print(f"Purged all L-Corp vocabulary across {total_mods} files in 01_Somnarak_Wiki!")

if __name__ == "__main__":
    purge_files()
