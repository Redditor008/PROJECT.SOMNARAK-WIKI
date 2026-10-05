#!/usr/bin/env python3
"""Shared vector-art kit for Somnarak wiki gallery generation.

Style target (v2): *illuminated archival dark-fantasy* -- layered atmospheric
depth, bloom lighting, engraved ornament, and stippled texture. Deliberately
NOT flat corporate minimal: every plate carries sky, architecture, subject,
foreground, and ornament layers with per-file seeded variation.
"""

import hashlib
import html
import random

# ---------------------------------------------------------------- palettes ---
# p  = primary accent   s  = deep secondary   hi = near-white highlight
# bg0/bg1 = backdrop gradient stops           mist = foreground mist tint
PALETTES = {
    "grudge":  {"p": "#ff6a5e", "s": "#7f1d1d", "hi": "#ffe0dc",
                "bg0": "#1c0b10", "bg1": "#05070d", "mist": "#ff6a5e"},
    "lament":  {"p": "#4cc3ff", "s": "#0c4a6e", "hi": "#d9f2ff",
                "bg0": "#0a1524", "bg1": "#04070d", "mist": "#4cc3ff"},
    "lumen":   {"p": "#ffc94d", "s": "#92400e", "hi": "#fff3d6",
                "bg0": "#1d1306", "bg1": "#0a0704", "mist": "#ffc94d"},
    "void":    {"p": "#c084fc", "s": "#581c87", "hi": "#f3e8ff",
                "bg0": "#140b24", "bg1": "#060409", "mist": "#c084fc"},
    "insight": {"p": "#4ade80", "s": "#14532d", "hi": "#dcfce7",
                "bg0": "#08160e", "bg1": "#030805", "mist": "#4ade80"},
    "weight":  {"p": "#93a4ff", "s": "#312e81", "hi": "#e2e6ff",
                "bg0": "#0c0e22", "bg1": "#04050c", "mist": "#93a4ff"},
    "gold":    {"p": "#d8b26a", "s": "#713f12", "hi": "#fdf3dd",
                "bg0": "#16110a", "bg1": "#070503", "mist": "#d8b26a"},
}

GILT = "#d8b26a"        # engraved gilt linework
GILT_DEEP = "#7a5a26"
IRON = "#2b3547"        # cold iron linework
IRON_SOFT = "#475569"
BONE = "#e8e2d2"        # bone-white engraving ink
INK = "#04060b"


def pal_for(slug):
    """Pick a pressure palette from slug keywords (Somnarak, never PM terms)."""
    s = slug.lower()
    if any(k in s for k in ["ordeal", "grudge", "combat", "breach", "crucible",
                            "red", "hunt", "quarantine", "emergency", "fire",
                            "thermal", "blood", "forge", "rage"]):
        return PALETTES["grudge"]
    if any(k in s for k in ["lament", "compass", "echo", "mental", "blue",
                            "panic", "acoustic", "sonar", "weeping", "river",
                            "choir", "tale", "dream"]):
        return PALETTES["lament"]
    if any(k in s for k in ["lumen", "harvest", "spire", "energy", "amber",
                            "dawn", "gold", "tree", "crystal", "hope", "sun",
                            "ingot"]):
        return PALETTES["lumen"]
    if any(k in s for k in ["void", "debt", "scale", "relic", "pale",
                            "extract", "violet", "purple", "maw", "abyss",
                            "chasm", "descent", "veil", "sovereign"]):
        return PALETTES["void"]
    if any(k in s for k in ["specialist", "cadre", "personnel", "insight",
                            "green", "clerk", "captain", "roster", "promotion",
                            "squad", "muster", "warden", "kang", "arin"]):
        return PALETTES["insight"]
    if any(k in s for k in ["weight", "shadow", "gate", "vault", "black",
                            "deep", "watch", "seal", "warden-black"]):
        return PALETTES["weight"]
    return PALETTES["gold"]


def rng_for(slug, salt="art"):
    seed = int(hashlib.sha256((salt + slug).encode()).hexdigest()[:8], 16)
    return random.Random(seed)


def esc(text):
    return html.escape(text)


# ------------------------------------------------------------- svg defs ----
def defs_block(p, grain=True):
    """Gradient + filter library shared by every plate."""
    grain_f = ""
    if grain:
        grain_f = (
            '<filter id="grainF" x="0" y="0" width="100%" height="100%">'
            '<feTurbulence type="fractalNoise" baseFrequency="0.9" '
            'numOctaves="2" stitchTiles="stitch" result="n"/>'
            '<feColorMatrix in="n" type="matrix" values="0 0 0 0 1 '
            "0 0 0 0 1 0 0 0 0 1 0 0 0 0.045 0\"/></filter>"
        )
    return (
        "<defs>"
        f'<linearGradient id="skyG" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0%" stop-color="{p["bg0"]}"/>'
        f'<stop offset="55%" stop-color="{p["bg1"]}"/>'
        f'<stop offset="100%" stop-color="#010203"/></linearGradient>'
        f'<radialGradient id="vigG" cx="50%" cy="42%" r="78%">'
        '<stop offset="0%" stop-color="#000000" stop-opacity="0"/>'
        '<stop offset="62%" stop-color="#000000" stop-opacity="0"/>'
        '<stop offset="100%" stop-color="#000000" stop-opacity="0.62"/>'
        "</radialGradient>"
        f'<radialGradient id="coreG" cx="50%" cy="50%" r="50%">'
        f'<stop offset="0%" stop-color="{p["hi"]}"/>'
        f'<stop offset="35%" stop-color="{p["p"]}"/>'
        f'<stop offset="100%" stop-color="{p["p"]}" stop-opacity="0"/>'
        "</radialGradient>"
        f'<linearGradient id="giltG" x1="0" y1="0" x2="1" y2="1">'
        f'<stop offset="0%" stop-color="{GILT}"/>'
        f'<stop offset="50%" stop-color="#f4e3bb"/>'
        f'<stop offset="100%" stop-color="{GILT_DEEP}"/></linearGradient>'
        f'<linearGradient id="ironG" x1="0" y1="0" x2="0" y2="1">'
        '<stop offset="0%" stop-color="#5b6b85"/>'
        '<stop offset="45%" stop-color="#232c3d"/>'
        '<stop offset="100%" stop-color="#0c1119"/></linearGradient>'
        '<filter id="glowF" x="-60%" y="-60%" width="220%" height="220%">'
        '<feGaussianBlur stdDeviation="4" result="b"/><feMerge>'
        '<feMergeNode in="b"/><feMergeNode in="SourceGraphic"/>'
        "</feMerge></filter>"
        '<filter id="bloomF" x="-80%" y="-80%" width="260%" height="260%">'
        '<feGaussianBlur stdDeviation="11" result="b"/><feMerge>'
        '<feMergeNode in="b"/><feMergeNode in="b"/>'
        '<feMergeNode in="SourceGraphic"/></feMerge></filter>'
        '<filter id="softF" x="-40%" y="-40%" width="180%" height="180%">'
        '<feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" '
        'flood-opacity="0.65"/></filter>'
        f"{grain_f}</defs>"
    )


def grain_rect(w, h):
    return (f'<rect width="{w}" height="{h}" filter="url(#grainF)" '
            'opacity="0.55"/>')


def vignette_rect(w, h):
    return f'<rect width="{w}" height="{h}" fill="url(#vigG)"/>'


# --------------------------------------------------------------- particles --
def starfield(rng, w, h, n, top_frac=0.72):
    out = []
    for _ in range(n):
        x = rng.uniform(0, w)
        y = rng.uniform(0, h * top_frac)
        r = rng.uniform(0.5, 1.7)
        o = rng.uniform(0.25, 0.95)
        c = rng.choice([BONE, "#bcd2ff", "#ffffff"])
        out.append(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.2f}" fill="{c}" '
            f'opacity="{o:.2f}"/>')
    # a few bright cross-sparkles
    for _ in range(max(2, n // 22)):
        x = rng.uniform(w * 0.06, w * 0.94)
        y = rng.uniform(h * 0.05, h * top_frac * 0.8)
        s = rng.uniform(3, 7)
        o = rng.uniform(0.5, 0.9)
        out.append(
            f'<path d="M {x:.1f} {y - s:.1f} L {x:.1f} {y + s:.1f} '
            f'M {x - s:.1f} {y:.1f} L {x + s:.1f} {y:.1f}" stroke="#ffffff" '
            f'stroke-width="1" opacity="{o:.2f}"/>')
    return "".join(out)


def embers(rng, w, h, n, color, y0=0.15, y1=0.95):
    out = []
    for _ in range(n):
        x = rng.uniform(0, w)
        y = rng.uniform(h * y0, h * y1)
        r = rng.uniform(1.0, 2.8)
        o = rng.uniform(0.3, 0.9)
        out.append(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.2f}" fill="{color}" '
            f'opacity="{o:.2f}" filter="url(#glowF)"/>')
    return "".join(out)


def light_rays(cx, cy, color, spans, length, op=0.10):
    """Soft translucent beams fanning from a focal point."""
    out = []
    for ang, half in spans:
        import math
        a0 = math.radians(ang - half)
        a1 = math.radians(ang + half)
        x0, y0 = cx + math.cos(a0) * length, cy + math.sin(a0) * length
        x1, y1 = cx + math.cos(a1) * length, cy + math.sin(a1) * length
        out.append(
            f'<polygon points="{cx},{cy} {x0:.0f},{y0:.0f} {x1:.0f},{y1:.0f}" '
            f'fill="{color}" opacity="{op}"/>')
    return "".join(out)


# ---------------------------------------------------------------- ornament --
def knurled_ring(cx, cy, r, n, color, op=0.8, wdt=2.0, tick=7):
    import math
    out = []
    for i in range(n):
        a = math.radians(i * 360.0 / n)
        x0, y0 = cx + math.cos(a) * r, cy + math.sin(a) * r
        x1, y1 = cx + math.cos(a) * (r + tick), cy + math.sin(a) * (r + tick)
        out.append(
            f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" '
            f'stroke="{color}" stroke-width="{wdt}" opacity="{op}"/>')
    return "".join(out)


def guilloche(cx, cy, radii, color, op=0.5):
    dashes = ["2,3", "10,4,2,4", "1,4", "14,5"]
    out = []
    for i, r in enumerate(radii):
        out.append(
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{color}" '
            f'stroke-width="1" stroke-dasharray="{dashes[i % len(dashes)]}" '
            f'opacity="{op}"/>')
    return "".join(out)


def corner_ornament(x, y, fx, fy, color, s=1.0):
    """Engraved corner flourish; fx/fy mirror the quadrant (+1/-1)."""
    pts = [
        f"M {x} {y + 26 * fy * s} L {x} {y + 8 * fy * s} "
        f"Q {x} {y} {x + 8 * fx * s} {y} L {x + 26 * fx * s} {y}",
        f"M {x + 5 * fx * s} {y + 20 * fy * s} "
        f"Q {x + 5 * fx * s} {y + 5 * fy * s} {x + 20 * fx * s} {y + 5 * fy * s}",
    ]
    dot = (f'<circle cx="{x + 12 * fx * s}" cy="{y + 12 * fy * s}" r="{2.4 * s}" '
           f'fill="{color}"/>')
    body = "".join(
        f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{2.2 * s}" '
        'stroke-linecap="round"/>' for d in paths(pts))
    return body + dot


def paths(items):
    return items


def rivet_row(x0, y0, x1, y1, n, color=GILT, r=2.2):
    out = []
    for i in range(n):
        t = 0 if n == 1 else i / (n - 1)
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        out.append(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="#0a0d14" '
            f'stroke="{color}" stroke-width="1"/>')
    return "".join(out)


def diamond(cx, cy, s, fill, stroke=None, sw=1.2):
    st = f'stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return (f'<polygon points="{cx},{cy - s} {cx + s},{cy} {cx},{cy + s} '
            f'{cx - s},{cy}" fill="{fill}" {st}/>')


def mist_band(x, y, w, h, color, op=0.16):
    return (f'<ellipse cx="{x + w / 2}" cy="{y + h / 2}" rx="{w / 2}" '
            f'ry="{h / 2}" fill="{color}" opacity="{op}" '
            'filter="url(#bloomF)"/>')


def floor_reflection(y, w, color, op=0.10):
    return (f'<rect x="0" y="{y}" width="{w}" height="3" fill="{color}" '
            f'opacity="{op * 2}"/>'
            f'<rect x="0" y="{y + 6}" width="{w}" height="1.5" fill="{color}" '
            f'opacity="{op}"/>')
