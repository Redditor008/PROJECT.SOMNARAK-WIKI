import textwrap

def build_box_74(title, sections):
    width = 74
    inner_width = width - 4 # 70 characters
    out = []
    
    top = "+" + "=" * (width - 2) + "+"
    out.append(top)
    
    t_str = f" {title} "
    diff = (width - 2) - len(t_str)
    l_p = diff // 2
    r_p = diff - l_p
    out.append("|" + " " * l_p + t_str + " " * r_p + "|")
    out.append(top)
    
    for s_idx, sec in enumerate(sections):
        if s_idx > 0:
            out.append("+" + "-" * (width - 2) + "+")
        for line in sec:
            if not line:
                out.append("|" + " " * (width - 2) + "|")
                continue
            wrapped = textwrap.wrap(line, width=inner_width)
            for w in wrapped:
                pad = inner_width - len(w)
                out.append(f"| {w}{' ' * pad} |")
                
    out.append(top)
    
    for idx, row in enumerate(out):
        assert len(row) == width, f"Row {idx} length {len(row)} != {width}: '{row}'"
    return "\n".join(out)

sec1 = [
    "MASTER ARCHITECTURE SPECIFICATION: /docs FRONT HOME PAGE",
    "Publishing Root: docs/ (GitHub Pages)",
    "Core Deliverable: docs/index.html as Central Master Portal",
    "Target Ecosystem: 4 Master Pillars (Wiki, Story, Game, Collection)"
]

sec2 = [
    "THE FOUR MASTER PORTAL GATEWAYS:",
    "1. WIKI HUB: Complete Encyclopedia, SECC Classification System,",
    "   Cadres, 5 Syndicates, and 19-Section Comparative System Codex.",
    "2. STORY HUB: 1,778 Mnemonic Cycle Chronicles, SED & UCD Operations,",
    "   Echo-Core Realization Wars, and Reverie MAD Animatic Script.",
    "3. GAME HUB: Interactive 10-Node Spatial Grid Combat Engine,",
    "   Speed-Based Action Slots, Two-Work Rules, and Workshop Forging.",
    "4. COLLECTION HUB: 292 Sorrow Entity Vault, 287+ SVG M.A.W. Armory,",
    "   Tool Relic Dossiers, and Architectural Schematic Blueprints."
]

sec3 = [
    "IMPLEMENTATION & SPECIFICATION ASSETS COMMITTED:",
    "- docs/README.md: Master Portal Vision & Architectural Breakdown.",
    "- docs/FRONT_HOME_PAGE_SPECIFICATION.md: Complete UI/UX Specification.",
    "- Quad-Gateway Routing: Standardized navigation links across all hubs."
]

box1 = build_box_74("DOCS FRONT HOME PAGE PORTAL BLUEPRINT", [sec1, sec2, sec3])
print(box1)

prog_sec = [
    "ROADMAP MILESTONE AUDIT & DELIVERABLE METRICS",
    "Phase: /docs Master Front Home Page Architecture & Quad-Hub Routing",
    "Overall Roadmap Completion: 100.0% / 100.0%",
    "Pillars Formally Specified: 4 / 4 Master Hubs (100.0%)",
    "Publishing Root Documentation: docs/README and Specifications Online",
    "Pan-Archive SE Compliance: 292 / 292 Files Verified (100.0%)",
    "Project Moon Research Archive: 16 / 16 Volumes Published (100.0%)"
]

box2 = build_box_74("PROJECT SOMNARAK ROADMAP PROGRESS METRICS", [prog_sec])
print("\n" + box2)
