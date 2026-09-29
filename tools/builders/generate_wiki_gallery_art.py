#!/usr/bin/env python3
"""Generate rich illuminated-archival wiki art (v2) for all gallery SVGs.

Four archetypes (same canvas contract as v1 so page layouts never shift):
  ICON    256x256    engraved medallion + glowing gradient glyph + enamel plate
  BANNER  1200x320   layered nocturnal panorama + cartouche title
  MAP     1200x800   luminous CAD blueprint, 3 layout variants
  GALLERY 800x600    ornate museum frame + layered illustrative scene

Usage:  python3 tools/builders/generate_wiki_gallery_art.py
"""

import pathlib
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from wiki_art_kit import (  # noqa: E402
    BONE, GILT, GILT_DEEP, INK, IRON, IRON_SOFT, corner_ornament, defs_block,
    diamond, embers, esc, floor_reflection, grain_rect, guilloche,
    knurled_ring, light_rays, mist_band, pal_for, rivet_row, rng_for,
    starfield, vignette_rect,
)

IMG_DIR = pathlib.Path("SOMNARAK-WORLD/Pages/images")
PRESERVE = {"somnarak-city-layout.svg", "the-hand-facility-layout.svg"}

SERIF = "'Cinzel','Palatino Linotype',Georgia,serif"
SANS = "'Segoe UI',-apple-system,Roboto,'Helvetica Neue',sans-serif"
MONO = "'Cascadia Code',Consolas,'Liberation Mono',monospace"


# ================================================================ classify ==
def classify_file(slug):
    s = slug.lower()
    if any(k in s for k in [
        "layout", "map", "wireframe", "grid", "overview", "chasm-descent",
        "elevator-shaft", "containment-cell-array", "chamber-layout",
        "corridor-overview", "pioneering-mine-pits", "department-floor-grid",
        "place-entity-chamber", "channeled-use-chamber",
        "tool-relic-chamber-layout",
    ]):
        return "MAP"
    if any(k in s for k in [
        "banner", "spire", "departure", "awakening", "transmutation", "portal",
        "illumination", "midnight-sovereign", "midnight-incursion",
        "council-chamber", "alpha-tree", "the-mnemonic-cycle-1778",
        "the-six-cantos", "the-dawn-of-hope",
    ]):
        return "BANNER"
    if any(k in s for k in [
        "icon", "weapon", "scythe", "ribbon", "sash", "seal", "armband",
        "armbands", "relic", "artifact", "mechanism", "gauge", "dial",
        "roulette", "elements", "ingot", "reskins", "combat-profiling",
        "suits", "suit-armor", "suit-weaving", "gift-manifestation",
        "elements-graphic", "risk-tiers", "risk-levels", "fear-level",
        "damage-calculation", "meltdown-gauge", "escape-counter",
        "thermal-warning-gauge", "sovereign-class-alarm",
        "promotion-and-ranks", "gimbaled-needle", "the-echo-compass-artifact",
        "the-debt-scale-relic",
    ]):
        return "ICON"
    return "GALLERY"


# ================================================================== ICON ===
def _g_scythe(p):
    g = (f'<defs><linearGradient id="blG" x1="0" y1="0" x2="1" y2="1">'
         f'<stop offset="0%" stop-color="{p["hi"]}"/>'
         f'<stop offset="45%" stop-color="{p["p"]}"/>'
         f'<stop offset="100%" stop-color="{p["s"]}"/></linearGradient></defs>')
    return g + (
        f'<g filter="url(#glowF)">'
        f'<path d="M 178 42 C 128 48, 66 86, 52 148 C 74 126, 120 104, '
        f'162 99 L 168 82 Z" fill="url(#blG)" stroke="{p["hi"]}" '
        f'stroke-width="1.6"/>'
        f'<path d="M 62 132 C 84 176, 140 202, 196 212 L 191 201 C 146 191, '
        f'94 166, 78 126 Z" fill="{IRON_SOFT}" opacity="0.9"/>'
        f'<line x1="172" y1="48" x2="78" y2="206" stroke="#10151f" '
        f'stroke-width="8" stroke-linecap="round"/>'
        f'<line x1="172" y1="48" x2="78" y2="206" stroke="url(#ironG)" '
        f'stroke-width="5" stroke-linecap="round"/>'
        f'<line x1="166" y1="54" x2="86" y2="198" stroke="{p["p"]}" '
        f'stroke-width="1.6"/>'
        f'<circle cx="172" cy="48" r="7" fill="#0b0f17" stroke="{p["p"]}" '
        f'stroke-width="2.4"/>'
        f'<circle cx="172" cy="48" r="2.4" fill="{p["hi"]}"/>'
        f'<circle cx="118" cy="78" r="3" fill="{p["hi"]}"/>'
        f'<circle cx="94" cy="108" r="2.4" fill="{p["hi"]}" opacity="0.8"/>'
        f'<circle cx="140" cy="150" r="2" fill="{p["hi"]}" opacity="0.6"/>'
        "</g>")


def _g_compass(p):
    return (
        f'<g filter="url(#glowF)">'
        f'<circle cx="128" cy="116" r="64" fill="#0a0f18" stroke="{p["p"]}" '
        f'stroke-width="3.4"/>'
        f'<circle cx="128" cy="116" r="64" fill="none" stroke="{p["hi"]}" '
        f'stroke-width="0.8" opacity="0.7"/>'
        f'<circle cx="128" cy="116" r="55" fill="none" stroke="{p["p"]}" '
        f'stroke-width="1" stroke-dasharray="3,3" opacity="0.8"/>'
        f'<circle cx="128" cy="116" r="45" fill="#111a2a" stroke="{p["p"]}" '
        f'stroke-width="2"/>'
        f'<polygon points="128,68 135,116 128,109 121,116" fill="{p["p"]}" '
        f'stroke="{p["hi"]}" stroke-width="0.8"/>'
        f'<polygon points="128,164 135,116 128,123 121,116" fill="{IRON_SOFT}"/>'
        f'<polygon points="80,116 128,109 121,116 128,123" fill="{IRON_SOFT}"/>'
        f'<polygon points="176,116 128,109 135,116 128,123" fill="{IRON_SOFT}"/>'
        f'<circle cx="128" cy="116" r="8" fill="{p["hi"]}" stroke="{p["p"]}" '
        f'stroke-width="2.2"/>'
        f'<circle cx="128" cy="116" r="2.6" fill="#0a0f18"/>'
        "</g>")


def _g_scale(p):
    return (
        f'<g filter="url(#glowF)" stroke-linecap="round">'
        f'<rect x="106" y="170" width="44" height="10" rx="3" fill="url(#ironG)" '
        f'stroke="{p["p"]}" stroke-width="1.4"/>'
        f'<line x1="128" y1="62" x2="128" y2="172" stroke="{p["p"]}" '
        f'stroke-width="5"/>'
        f'<line x1="128" y1="62" x2="128" y2="172" stroke="{p["hi"]}" '
        f'stroke-width="1.4" opacity="0.8"/>'
        f'<circle cx="128" cy="62" r="5" fill="{p["hi"]}" stroke="{p["p"]}" '
        f'stroke-width="1.6"/>'
        f'<line x1="64" y1="86" x2="192" y2="86" stroke="{p["p"]}" '
        f'stroke-width="4"/>'
        f'<circle cx="128" cy="86" r="6.5" fill="#0b0f17" stroke="{p["hi"]}" '
        f'stroke-width="1.8"/>'
        f'<line x1="64" y1="86" x2="48" y2="132" stroke="{IRON_SOFT}" '
        f'stroke-width="1.8"/>'
        f'<line x1="64" y1="86" x2="80" y2="132" stroke="{IRON_SOFT}" '
        f'stroke-width="1.8"/>'
        f'<path d="M 42 132 Q 64 150 86 132 Z" fill="{p["s"]}" '
        f'stroke="{p["hi"]}" stroke-width="1.6"/>'
        f'<circle cx="58" cy="130" r="5" fill="#05070c" stroke="{p["p"]}" '
        f'stroke-width="1.2"/>'
        f'<circle cx="70" cy="129" r="6" fill="#05070c" stroke="{p["p"]}" '
        f'stroke-width="1.2"/>'
        f'<line x1="192" y1="86" x2="176" y2="132" stroke="{IRON_SOFT}" '
        f'stroke-width="1.8"/>'
        f'<line x1="192" y1="86" x2="208" y2="132" stroke="{IRON_SOFT}" '
        f'stroke-width="1.8"/>'
        f'<path d="M 170 132 Q 192 150 214 132 Z" fill="{p["s"]}" '
        f'stroke="{p["hi"]}" stroke-width="1.6"/>'
        f'<polygon points="192,118 197,130 187,130" fill="{p["hi"]}"/>'
        "</g>")


def _g_furnace(p):
    return (
        f'<g filter="url(#glowF)">'
        f'<rect x="182" y="168" width="14" height="26" fill="url(#ironG)"/>'
        f'<rect x="60" y="168" width="14" height="26" fill="url(#ironG)"/>'
        f'<path d="M 82 82 L 174 82 L 162 156 Q 128 180 94 156 Z" '
        f'fill="url(#ironG)" stroke="{p["p"]}" stroke-width="3"/>'
        f'<ellipse cx="128" cy="82" rx="46" ry="13" fill="#05070c" '
        f'stroke="{p["p"]}" stroke-width="2.2"/>'
        f'<ellipse cx="128" cy="83" rx="35" ry="8.5" fill="{p["p"]}" '
        f'filter="url(#bloomF)"/>'
        f'<ellipse cx="128" cy="83" rx="18" ry="4.6" fill="{p["hi"]}"/>'
        f'<circle cx="128" cy="132" r="17" fill="#05070c" stroke="{p["p"]}" '
        f'stroke-width="2.2"/>'
        f'<path d="M 122 140 Q 128 118 134 140 Q 128 136 122 140 Z" '
        f'fill="{p["p"]}" filter="url(#bloomF)"/>'
        f'<line x1="68" y1="108" x2="82" y2="108" stroke="{p["p"]}" '
        f'stroke-width="3.4"/>'
        f'<line x1="174" y1="108" x2="188" y2="108" stroke="{p["p"]}" '
        f'stroke-width="3.4"/>'
        f'<line x1="68" y1="140" x2="80" y2="140" stroke="{p["p"]}" '
        f'stroke-width="2.4" opacity="0.7"/>'
        f'<line x1="176" y1="140" x2="188" y2="140" stroke="{p["p"]}" '
        f'stroke-width="2.4" opacity="0.7"/>'
        "</g>")


def _g_crest(p):
    return (
        f'<g filter="url(#glowF)">'
        f'<path d="M 86 62 L 170 62 L 170 118 Q 170 164 128 180 '
        f'Q 86 164 86 118 Z" fill="#141b2c" stroke="{p["p"]}" '
        f'stroke-width="3"/>'
        f'<path d="M 95 71 L 161 71 L 161 117 Q 161 152 128 166 '
        f'Q 95 152 95 117 Z" fill="none" stroke="{p["p"]}" stroke-width="1" '
        f'stroke-dasharray="3,2" opacity="0.8"/>'
        f'<polygon points="128,82 134,134 128,142 122,134" fill="{p["p"]}" '
        f'stroke="{p["hi"]}" stroke-width="0.8"/>'
        f'<circle cx="128" cy="82" r="4.5" fill="{p["hi"]}"/>'
        f'<line x1="106" y1="110" x2="150" y2="110" stroke="{p["p"]}" '
        f'stroke-width="2.2"/>'
        f'<line x1="112" y1="120" x2="144" y2="120" stroke="{p["p"]}" '
        f'stroke-width="1.2" opacity="0.7"/>'
        f'<path d="M 70 150 L 98 150 L 98 158 L 70 158 Z" fill="{p["s"]}" '
        f'stroke="{p["p"]}" stroke-width="1" transform="rotate(18 84 154)"/>'
        f'<path d="M 158 150 L 186 150 L 186 158 L 158 158 Z" fill="{p["s"]}" '
        f'stroke="{p["p"]}" stroke-width="1" transform="rotate(-18 172 154)"/>'
        "</g>")


def _g_armor(p):
    return (
        f'<g filter="url(#glowF)">'
        f'<path d="M 90 62 L 166 62 L 182 114 L 161 176 L 95 176 L 74 114 Z" '
        f'fill="url(#ironG)" stroke="{p["p"]}" stroke-width="3"/>'
        f'<polygon points="128,66 110,104 146,104" fill="#05070c" '
        f'stroke="{p["p"]}" stroke-width="1.6"/>'
        f'<line x1="128" y1="104" x2="128" y2="176" stroke="{p["p"]}" '
        f'stroke-width="2"/>'
        f'<path d="M 96 84 L 74 114 L 86 118 L 104 92 Z" fill="{p["s"]}" '
        f'stroke="{p["p"]}" stroke-width="1.2"/>'
        f'<path d="M 160 84 L 182 114 L 170 118 L 152 92 Z" fill="{p["s"]}" '
        f'stroke="{p["p"]}" stroke-width="1.2"/>'
        f'<rect x="100" y="140" width="56" height="9" rx="2" fill="{p["p"]}" '
        f'stroke="{p["hi"]}" stroke-width="0.8"/>'
        f'<circle cx="128" cy="122" r="5" fill="{p["hi"]}" stroke="{p["p"]}" '
        f'stroke-width="1.4"/>'
        "</g>")


def _g_crystal(p):
    return (
        f'<g filter="url(#glowF)">'
        f'<polygon points="128,52 180,90 180,148 128,186 76,148 76,90" '
        f'fill="#0a0f1a" stroke="{p["p"]}" stroke-width="3"/>'
        f'<polygon points="128,52 180,90 128,120 76,90" fill="{p["p"]}" '
        f'opacity="0.45"/>'
        f'<polygon points="76,90 128,120 128,186 76,148" fill="{p["s"]}" '
        f'opacity="0.75" stroke="{p["p"]}" stroke-width="1"/>'
        f'<polygon points="180,90 128,120 128,186 180,148" fill="{p["p"]}" '
        f'opacity="0.85" stroke="{p["hi"]}" stroke-width="1"/>'
        f'<line x1="128" y1="52" x2="128" y2="186" stroke="{p["hi"]}" '
        f'stroke-width="1" opacity="0.7"/>'
        f'<circle cx="128" cy="120" r="5" fill="{p["hi"]}" '
        f'filter="url(#bloomF)"/>'
        f'<polygon points="150,66 154,74 146,74" fill="{p["hi"]}" opacity="0.9"/>'
        "</g>")


def _g_sigil(p):
    return (
        f'<g filter="url(#glowF)">'
        f'<circle cx="128" cy="116" r="52" fill="#0c1220" stroke="{p["p"]}" '
        f'stroke-width="3"/>'
        f'<circle cx="128" cy="116" r="44" fill="none" stroke="{p["p"]}" '
        f'stroke-width="1" stroke-dasharray="2,3" opacity="0.8"/>'
        f'<polygon points="128,74 160,136 96,136" fill="none" '
        f'stroke="{p["p"]}" stroke-width="2.2"/>'
        f'<polygon points="128,158 160,96 96,96" fill="none" '
        f'stroke="{p["p"]}" stroke-width="1.4" opacity="0.65"/>'
        f'<circle cx="128" cy="116" r="9" fill="{p["hi"]}" stroke="{p["p"]}" '
        f'stroke-width="2"/>'
        f'<circle cx="128" cy="116" r="3" fill="#0c1220"/>'
        "</g>")


def _g_gauge(p):
    ticks = "".join(
        f'<line x1="{128 + 44 * __import__("math").cos(a)}" '
        f'y1="{116 + 44 * __import__("math").sin(a)}" '
        f'x2="{128 + 52 * __import__("math").cos(a)}" '
        f'y2="{116 + 52 * __import__("math").sin(a)}" stroke="{p["p"]}" '
        f'stroke-width="2"/>'
        for a in [3.49 + i * 0.44 for i in range(7)])
    return (
        f'<g filter="url(#glowF)">'
        f'<circle cx="128" cy="116" r="58" fill="#0a0f18" stroke="{p["p"]}" '
        f'stroke-width="3"/>'
        f'<path d="M 80 150 A 56 56 0 0 1 176 150" fill="none" '
        f'stroke="{p["s"]}" stroke-width="9"/>'
        f'<path d="M 80 150 A 56 56 0 0 1 140 66" fill="none" '
        f'stroke="{p["p"]}" stroke-width="9"/>'
        f'<path d="M 80 150 A 56 56 0 0 1 140 66" fill="none" '
        f'stroke="{p["hi"]}" stroke-width="2" opacity="0.8"/>'
        f"{ticks}"
        f'<line x1="128" y1="116" x2="152" y2="80" stroke="{p["hi"]}" '
        f'stroke-width="3.4" stroke-linecap="round"/>'
        f'<circle cx="128" cy="116" r="8" fill="#0a0f18" stroke="{p["p"]}" '
        f'stroke-width="2.4"/>'
        f'<circle cx="128" cy="116" r="2.6" fill="{p["hi"]}"/>'
        "</g>")


def _g_roulette(p):
    import math
    segs = []
    cols = [p["p"], p["s"], p["hi"], IRON_SOFT]
    for i in range(8):
        a0, a1 = math.radians(i * 45), math.radians(i * 45 + 45)
        x0, y0 = 128 + 54 * math.cos(a0), 116 + 54 * math.sin(a0)
        x1, y1 = 128 + 54 * math.cos(a1), 116 + 54 * math.sin(a1)
        segs.append(
            f'<path d="M 128 116 L {x0:.1f} {y0:.1f} A 54 54 0 0 1 '
            f'{x1:.1f} {y1:.1f} Z" fill="{cols[i % 4]}" opacity="0.85" '
            f'stroke="#05070c" stroke-width="1"/>')
    return (
        f'<g filter="url(#glowF)">{"".join(segs)}'
        f'<circle cx="128" cy="116" r="54" fill="none" stroke="{p["p"]}" '
        f'stroke-width="3"/>'
        f'<circle cx="128" cy="116" r="12" fill="#0a0f18" stroke="{p["hi"]}" '
        f'stroke-width="2"/>'
        f'<polygon points="128,52 134,70 122,70" fill="{p["hi"]}" '
        f'stroke="{p["p"]}" stroke-width="1.4"/>'
        "</g>")


def _g_orbs(p):
    cols = ["#ff6a5e", "#4cc3ff", "#c084fc", "#93a4ff"]
    names = ["G", "L", "V", "W"]
    out = [f'<g filter="url(#glowF)">']
    import math
    for i in range(4):
        a = math.radians(-90 + i * 90)
        x, y = 128 + 40 * math.cos(a), 116 + 40 * math.sin(a)
        out.append(
            f'<circle cx="{x:.0f}" cy="{y:.0f}" r="24" fill="#0a0f18" '
            f'stroke="{cols[i]}" stroke-width="2.6"/>'
            f'<circle cx="{x:.0f}" cy="{y:.0f}" r="13" fill="{cols[i]}" '
            f'opacity="0.85"/>'
            f'<circle cx="{x - 4:.0f}" cy="{y - 4:.0f}" r="4" fill="#ffffff" '
            f'opacity="0.85"/>'
            f'<text x="{x:.0f}" y="{y + 38:.0f}" text-anchor="middle" '
            f'font-family="{SANS}" font-size="11" font-weight="bold" '
            f'fill="{cols[i]}">{names[i]}</text>')
    out.append(f'<circle cx="128" cy="116" r="7" fill="{p["hi"]}" '
               f'stroke="{p["p"]}" stroke-width="2"/>')
    out.append("</g>")
    return "".join(out)


def _g_shield(p):
    return (
        f'<g filter="url(#glowF)">'
        f'<path d="M 128 58 L 172 74 L 172 116 Q 172 152 128 178 '
        f'Q 84 152 84 116 L 84 74 Z" fill="url(#ironG)" stroke="{p["p"]}" '
        f'stroke-width="3"/>'
        f'<path d="M 128 70 L 160 82 L 160 116 Q 160 144 128 164 '
        f'Q 96 144 96 116 L 96 82 Z" fill="none" stroke="{p["p"]}" '
        f'stroke-width="1.2" opacity="0.7"/>'
        f'<line x1="128" y1="70" x2="128" y2="164" stroke="{p["p"]}" '
        f'stroke-width="1.6"/>'
        f'<circle cx="128" cy="112" r="14" fill="#05070c" stroke="{p["hi"]}" '
        f'stroke-width="2"/>'
        f'<circle cx="128" cy="112" r="5" fill="{p["p"]}" '
        f'filter="url(#bloomF)"/>'
        "</g>")


def _g_sword(p):
    return (
        f'<g filter="url(#glowF)">'
        f'<polygon points="128,52 136,66 132,150 124,150 120,66" '
        f'fill="{p["hi"]}" stroke="{p["p"]}" stroke-width="1.4"/>'
        f'<line x1="128" y1="56" x2="128" y2="148" stroke="{p["p"]}" '
        f'stroke-width="1.2"/>'
        f'<line x1="100" y1="156" x2="156" y2="156" stroke="{p["p"]}" '
        f'stroke-width="6" stroke-linecap="round"/>'
        f'<circle cx="100" cy="156" r="5" fill="{p["hi"]}" stroke="{p["p"]}" '
        f'stroke-width="1.4"/>'
        f'<circle cx="156" cy="156" r="5" fill="{p["hi"]}" stroke="{p["p"]}" '
        f'stroke-width="1.4"/>'
        f'<rect x="123" y="160" width="10" height="22" rx="2" fill="url(#ironG)" '
        f'stroke="{p["p"]}" stroke-width="1.2"/>'
        f'<circle cx="128" cy="188" r="6" fill="{p["p"]}" stroke="{p["hi"]}" '
        f'stroke-width="1.4"/>'
        "</g>")


def _g_bell(p):
    return (
        f'<g filter="url(#glowF)">'
        f'<line x1="128" y1="52" x2="128" y2="66" stroke="{p["p"]}" '
        f'stroke-width="4"/>'
        f'<path d="M 96 150 Q 96 96 128 96 Q 160 96 160 150 L 170 162 '
        f'L 86 162 Z" fill="url(#giltG)" stroke="{p["p"]}" stroke-width="2"/>'
        f'<line x1="112" y1="112" x2="112" y2="146" stroke="{p["s"]}" '
        f'stroke-width="1.4" opacity="0.8"/>'
        f'<line x1="128" y1="108" x2="128" y2="146" stroke="{p["s"]}" '
        f'stroke-width="1.4" opacity="0.8"/>'
        f'<line x1="144" y1="112" x2="144" y2="146" stroke="{p["s"]}" '
        f'stroke-width="1.4" opacity="0.8"/>'
        f'<circle cx="128" cy="172" r="8" fill="{p["p"]}" stroke="{p["hi"]}" '
        f'stroke-width="1.4"/>'
        f'<path d="M 76 120 Q 66 140 72 162" fill="none" stroke="{p["p"]}" '
        f'stroke-width="2" opacity="0.7"/>'
        f'<path d="M 180 120 Q 190 140 184 162" fill="none" stroke="{p["p"]}" '
        f'stroke-width="2" opacity="0.7"/>'
        "</g>")


def _g_gift(p):
    return (
        f'<g filter="url(#glowF)">'
        f'<rect x="92" y="100" width="72" height="62" rx="6" fill="{p["s"]}" '
        f'stroke="{p["p"]}" stroke-width="2.6"/>'
        f'<rect x="86" y="88" width="84" height="18" rx="5" fill="{p["p"]}" '
        f'stroke="{p["hi"]}" stroke-width="1.2"/>'
        f'<line x1="128" y1="88" x2="128" y2="162" stroke="{p["hi"]}" '
        f'stroke-width="5"/>'
        f'<line x1="92" y1="125" x2="164" y2="125" stroke="{p["hi"]}" '
        f'stroke-width="5"/>'
        f'<path d="M 128 88 Q 108 70 116 62 Q 124 56 128 74 Q 132 56 140 62 '
        f'Q 148 70 128 88 Z" fill="{p["hi"]}" stroke="{p["p"]}" '
        f'stroke-width="1.4"/>'
        f'<circle cx="104" cy="146" r="3" fill="{p["hi"]}"/>'
        f'<circle cx="152" cy="146" r="3" fill="{p["hi"]}"/>'
        "</g>")


ICON_GLYPHS = [
    (("scythe", "blade"), _g_scythe),
    (("needle", "artifact", "dial"), _g_compass),
    (("relic",), _g_scale),
    (("furnace", "crucible", "thermal"), _g_furnace),
    (("crest", "armband", "sash", "ribbon", "promotion", "captain"), _g_crest),
    (("suit", "weaving", "reskins", "armor"), _g_armor),
    (("crystal", "ingot", "elements-graphic"), _g_crystal),
    (("gauge", "meltdown", "escape", "fear", "damage", "risk", "alarm",
      "counter"), _g_gauge),
    (("roulette", "tactical-hitbox"), _g_roulette),
    (("elements", "orbs"), _g_orbs),
    (("shield", "sovereign", "ward", "resistance"), _g_shield),
    (("sword", "combat-profiling", "clash"), _g_sword),
    (("bell", "choir", "chime"), _g_bell),
    (("gift", "charm"), _g_gift),
]


def icon_glyph(slug, p):
    s = slug.lower()
    for keys, fn in ICON_GLYPHS:
        if any(k in s for k in keys):
            return fn(p)
    return _g_sigil(p)


def build_icon(slug, title, p):
    rng = rng_for(slug, "icon")
    stars = starfield(rng, 256, 256, 26, top_frac=1.0)
    mote = embers(rng, 256, 256, 7, p["p"], y0=0.1, y1=0.9)
    knurl = knurled_ring(128, 118, 100, 56, p["p"], op=0.55, wdt=1.6, tick=5)
    guil = guilloche(128, 118, [88, 80], p["p"], op=0.4)
    import math
    pips = "".join(
        diamond(128 + 93 * math.cos(math.radians(45 + i * 90)),
                118 + 93 * math.sin(math.radians(45 + i * 90)),
                4, "#0b0f17", p["p"], 1.4) for i in range(4))
    label = esc(title.upper())
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" '
        f'width="256" height="256">{defs_block(p)}'
        f'<rect width="256" height="256" fill="url(#skyG)"/>'
        f"{stars}{mote}"
        f'<circle cx="128" cy="118" r="112" fill="#070b13" opacity="0.72"/>'
        f'<circle cx="128" cy="118" r="112" fill="none" stroke="url(#giltG)" '
        f'stroke-width="5"/>'
        f'<circle cx="128" cy="118" r="105" fill="none" stroke="{p["p"]}" '
        f'stroke-width="1.2" opacity="0.9"/>'
        f"{knurl}{guil}{pips}"
        f'<circle cx="128" cy="118" r="72" fill="{p["p"]}" opacity="0.10" '
        f'filter="url(#bloomF)"/>'
        f"{icon_glyph(slug, p)}"
        f'<rect x="30" y="210" width="196" height="26" rx="13" fill="#05080e" '
        f'stroke="{p["p"]}" stroke-width="1.6"/>'
        f'<rect x="34" y="213" width="188" height="20" rx="10" fill="none" '
        f'stroke="{GILT}" stroke-width="0.7" opacity="0.7"/>'
        f'<text x="128" y="227" text-anchor="middle" font-family="{SANS}" '
        f'font-size="9.5" font-weight="bold" fill="{BONE}" letter-spacing="1">'
        f"{label}</text>"
        f"{vignette_rect(256, 256)}{grain_rect(256, 256)}</svg>")


# ================================================================ BANNER ===
def _skyline(rng, variant, y_base, color, op):
    """Far silhouette ridge: spires / domes / jagged ruins."""
    pts = [f"M 0 320 L 0 {y_base + rng.uniform(-12, 12):.0f}"]
    x = 0
    while x < 1200:
        w = rng.uniform(26, 90)
        if variant == 0:  # needle spires
            h = rng.uniform(40, 150)
            pts.append(f"L {x + w * 0.4:.0f} {y_base - h:.0f} "
                       f"L {x + w * 0.55:.0f} {y_base - h - 26:.0f} "
                       f"L {x + w * 0.7:.0f} {y_base - h:.0f} "
                       f"L {x + w:.0f} {y_base + rng.uniform(-10, 10):.0f}")
        elif variant == 1:  # stepped domes
            h = rng.uniform(30, 90)
            pts.append(f"L {x + w * 0.2:.0f} {y_base - h:.0f} "
                       f"Q {x + w * 0.5:.0f} {y_base - h - 34:.0f} "
                       f"{x + w * 0.8:.0f} {y_base - h:.0f} "
                       f"L {x + w:.0f} {y_base + rng.uniform(-10, 10):.0f}")
        else:  # broken ruins
            h = rng.uniform(24, 120)
            pts.append(f"L {x + w * 0.3:.0f} {y_base - h:.0f} "
                       f"L {x + w * 0.45:.0f} {y_base - h + 18:.0f} "
                       f"L {x + w * 0.62:.0f} {y_base - h * 0.55:.0f} "
                       f"L {x + w:.0f} {y_base + rng.uniform(-10, 10):.0f}")
        x += w
    pts.append("L 1200 320 Z")
    return (f'<path d="{" ".join(pts)}" fill="{color}" opacity="{op}"/>')


def _lit_windows(rng, y, color):
    out = []
    for x in range(70, 1140, 34):
        if rng.random() < 0.55:
            h = rng.uniform(4, 9)
            out.append(
                f'<rect x="{x}" y="{y + rng.uniform(-3, 3):.1f}" width="5" '
                f'height="{h:.1f}" fill="{color}" opacity="0.85"/>')
    return "".join(out)


def build_banner(slug, title, p):
    rng = rng_for(slug, "banner")
    variant = rng.randrange(3)
    orb_x = rng.uniform(180, 1020)
    orb_y = rng.uniform(64, 120)
    orb_r = rng.uniform(26, 44)
    fs = min(44, (780 / max(8, len(title)) - 3) / 0.62)
    stars = starfield(rng, 1200, 320, 120, top_frac=0.6)
    motes = embers(rng, 1200, 320, 34, p["mist"], y0=0.35, y1=1.0)
    rays = light_rays(600, 330, p["p"], [(270, 9), (255, 6), (285, 6)], 420,
                      op=0.08)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 320" '
        f'width="1200" height="320">{defs_block(p)}'
        f'<rect width="1200" height="320" fill="url(#skyG)"/>{stars}'
        f'<circle cx="{orb_x:.0f}" cy="{orb_y:.0f}" r="{orb_r * 2.6:.0f}" '
        f'fill="url(#coreG)" opacity="0.55"/>'
        f'<circle cx="{orb_x:.0f}" cy="{orb_y:.0f}" r="{orb_r:.0f}" '
        f'fill="{p["p"]}" opacity="0.9" filter="url(#bloomF)"/>'
        f'<circle cx="{orb_x:.0f}" cy="{orb_y:.0f}" r="{orb_r * 0.55:.0f}" '
        f'fill="{p["hi"]}" opacity="0.95"/>'
        f'<circle cx="{orb_x:.0f}" cy="{orb_y:.0f}" r="{orb_r + 9:.0f}" '
        f'fill="none" stroke="{p["p"]}" stroke-width="1" opacity="0.6"/>'
        f'<ellipse cx="600" cy="238" rx="560" ry="60" fill="{p["p"]}" '
        f'opacity="0.10" filter="url(#bloomF)"/>'
        f'<ellipse cx="600" cy="252" rx="620" ry="26" fill="{p["p"]}" '
        f'opacity="0.14" filter="url(#bloomF)"/>'
        f"{_skyline(rng, variant, 236, '#04070d', 0.95)}"
        f"{_skyline(rng, (variant + 1) % 3, 262, '#0a0f1a', 0.9)}"
        f"{_lit_windows(rng, 252, p['p'])}"
        f'<path d="M 0 320 L 0 292 Q 300 268 600 292 T 1200 292 L 1200 320 Z" '
        f'fill="#02040a"/>'
        f"{mist_band(120, 268, 960, 44, p['mist'], 0.14)}{rays}{motes}"
        f'<line x1="48" y1="26" x2="1152" y2="26" stroke="url(#giltG)" '
        f'stroke-width="2"/>'
        f'<line x1="48" y1="294" x2="1152" y2="294" stroke="url(#giltG)" '
        f'stroke-width="2"/>'
        f"{diamond(600, 26, 6, '#0a0d14', GILT)}"
        f"{diamond(600, 294, 6, '#0a0d14', GILT)}"
        f"{diamond(48, 26, 4, GILT)}{diamond(1152, 26, 4, GILT)}"
        f"{diamond(48, 294, 4, GILT)}{diamond(1152, 294, 4, GILT)}"
        f'<rect x="180" y="118" width="840" height="104" rx="10" '
        f'fill="#04060b" opacity="0.78"/>'
        f'<rect x="180" y="118" width="840" height="104" rx="10" fill="none" '
        f'stroke="url(#giltG)" stroke-width="1.8"/>'
        f"{corner_ornament(180, 118, 1, 1, GILT, 0.8)}"
        f"{corner_ornament(1020, 118, -1, 1, GILT, 0.8)}"
        f"{corner_ornament(180, 222, 1, -1, GILT, 0.8)}"
        f"{corner_ornament(1020, 222, -1, -1, GILT, 0.8)}"
        f'<text x="600" y="{118 + fs + 22:.0f}" text-anchor="middle" '
        f'font-family="{SERIF}" font-size="{fs:.0f}" font-weight="bold" '
        f'fill="{BONE}" letter-spacing="3">{esc(title.upper())}</text>'
        f'<text x="600" y="206" text-anchor="middle" font-family="{SANS}" '
        f'font-size="12" font-weight="600" fill="{p["p"]}" '
        f'letter-spacing="3.5">PROJECT SOMNARAK &#9670; CYCLE 1,778</text>'
        f"{vignette_rect(1200, 320)}{grain_rect(1200, 320)}</svg>")


# =================================================================== MAP ===
def _map_room(x, y, w, h, name, sub, p, accent=True, label_top=False):
    c = p["p"] if accent else IRON_SOFT
    ny = y + 36 if label_top else y + h / 2 - 2
    sy = y + 53 if label_top else y + h / 2 + 15
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="#0b1322" '
        f'stroke="{c}" stroke-width="2.4"/>'
        f'<rect x="{x + 5}" y="{y + 5}" width="{w - 10}" height="{h - 10}" '
        f'rx="2" fill="none" stroke="{c}" stroke-width="0.8" opacity="0.5"/>'
        f'<text x="{x + w / 2}" y="{ny}" text-anchor="middle" '
        f'font-family="{SANS}" font-size="13" font-weight="bold" '
        f'fill="{BONE}">{esc(name)}</text>'
        f'<text x="{x + w / 2}" y="{sy}" text-anchor="middle" '
        f'font-family="{MONO}" font-size="9" fill="{c}">{esc(sub)}</text>')


def _map_node(x, y, p, label=None):
    out = (f'<circle cx="{x}" cy="{y}" r="10" fill="{p["p"]}" opacity="0.25" '
           f'filter="url(#bloomF)"/>'
           f'<circle cx="{x}" cy="{y}" r="5" fill="#0b1322" stroke="{p["p"]}" '
           f'stroke-width="2"/>'
           f'<circle cx="{x}" cy="{y}" r="1.8" fill="{p["hi"]}"/>')
    if label:
        out += (f'<text x="{x + 12}" y="{y + 4}" font-family="{MONO}" '
                f'font-size="9" fill="{p["p"]}">{esc(label)}</text>')
    return out


def _map_frame(p, title):
    return (
        f'<rect width="1200" height="800" fill="#060b16"/>'
        f'<rect width="1200" height="800" fill="url(#skyG)" opacity="0.55"/>'
        f'<g stroke="#16233a" stroke-width="0.8" opacity="0.8">'
        + "".join(f'<line x1="{x}" y1="0" x2="{x}" y2="800"/>'
                  for x in range(0, 1201, 30))
        + "".join(f'<line x1="0" y1="{y}" x2="1200" y2="{y}"/>'
                  for y in range(0, 801, 30))
        + "</g>"
        f'<rect x="24" y="24" width="1152" height="752" fill="none" '
        f'stroke="{p["p"]}" stroke-width="2.2"/>'
        f'<rect x="32" y="32" width="1136" height="736" fill="none" '
        f'stroke="{IRON_SOFT}" stroke-width="1"/>'
        f"{corner_ornament(24, 24, 1, 1, p['p'], 1.1)}"
        f"{corner_ornament(1176, 24, -1, 1, p['p'], 1.1)}"
        f"{corner_ornament(24, 776, 1, -1, p['p'], 1.1)}"
        f"{corner_ornament(1176, 776, -1, -1, p['p'], 1.1)}"
        f'<rect x="48" y="48" width="470" height="58" fill="#04060b" '
        f'opacity="0.85" stroke="{p["p"]}" stroke-width="1.4"/>'
        f'<text x="66" y="72" font-family="{MONO}" font-size="13" '
        f'font-weight="bold" fill="{p["p"]}">FACILITY 01 // SURVEY SCHEMATIC'
        f"</text>"
        f'<text x="66" y="91" font-family="{SANS}" font-size="11" '
        f'fill="{BONE}">{esc(title.upper())} &#183; SECTOR ASIYAH</text>')


def _map_legend(p, items):
    rows = "".join(
        f'<circle cx="830" cy="{690 + i * 20}" r="4" fill="none" '
        f'stroke="{p["p"]}" stroke-width="1.6"/>'
        f'<text x="844" y="{694 + i * 20}" font-family="{MONO}" font-size="10" '
        f'fill="{BONE}">{esc(t)}</text>' for i, t in enumerate(items))
    return (
        f'<rect x="812" y="640" width="328" height="{66 + len(items) * 20}" '
        f'fill="#04060b" opacity="0.88" stroke="{p["p"]}" stroke-width="1.4"/>'
        f'<text x="828" y="661" font-family="{MONO}" font-size="10" '
        f'font-weight="bold" fill="{p["p"]}">LEGEND</text>{rows}')


def _map_titleblock(p):
    return (
        f'<rect x="812" y="560" width="328" height="76" fill="#04060b" '
        f'opacity="0.88" stroke="{p["p"]}" stroke-width="1.4"/>'
        f"{rivet_row(824, 570, 1128, 570, 12, p['p'], 1.6)}"
        f'<text x="828" y="592" font-family="{MONO}" font-size="10" '
        f'font-weight="bold" fill="{p["p"]}">REVERIE DIRECTORATE SURVEY</text>'
        f'<text x="828" y="609" font-family="{MONO}" font-size="9" '
        f'fill="{BONE}">DWG ASIYAH-01 &#183; SCALE 1:500</text>'
        f'<text x="828" y="626" font-family="{MONO}" font-size="9" '
        f'fill="#4ade80">CYCLE 1,778 &#183; APPROVED FOR CANON</text>')


def _compass_rose(x, y, p):
    return (
        f'<circle cx="{x}" cy="{y}" r="26" fill="#04060b" opacity="0.85" '
        f'stroke="{p["p"]}" stroke-width="1.6"/>'
        f'<polygon points="{x},{y - 20} {x + 5},{y} {x},{y - 4} {x - 5},{y}" '
        f'fill="{p["p"]}"/>'
        f'<polygon points="{x},{y + 20} {x + 5},{y} {x},{y + 4} {x - 5},{y}" '
        f'fill="{IRON_SOFT}"/>'
        f'<polygon points="{x - 20},{y} {x},{y - 5} {x - 4},{y} {x},{y + 5}" '
        f'fill="{IRON_SOFT}"/>'
        f'<polygon points="{x + 20},{y} {x},{y - 5} {x + 4},{y} {x},{y + 5}" '
        f'fill="{IRON_SOFT}"/>'
        f'<text x="{x}" y="{y - 30}" text-anchor="middle" '
        f'font-family="{MONO}" font-size="11" font-weight="bold" '
        f'fill="{p["p"]}">N</text>')


def build_map(slug, title, p):
    s = slug.lower()
    body = _map_frame(p, title)
    if any(k in s for k in ["elevator-shaft", "chasm-descent", "wireframe"]):
        # --- vertical shaft section -------------------------------------
        body += (
            f'<rect x="520" y="150" width="160" height="470" fill="#0b1322" '
            f'stroke="{p["p"]}" stroke-width="2.6"/>'
            + "".join(
                f'<line x1="520" y1="{190 + i * 62}" x2="680" y2="{190 + i * 62}" '
                f'stroke="{IRON_SOFT}" stroke-width="1.2"/>'
                f'<text x="505" y="{194 + i * 62}" text-anchor="end" '
                f'font-family="{MONO}" font-size="10" fill="{BONE}">F{-i if i else 0} '
                f'{"CENTRAL" if i == 4 else "WING " + str(9 - i) if i else "SURFACE"}</text>'
                f'<rect x="600" y="{196 + i * 62}" width="34" height="22" '
                f'fill="#04060b" stroke="{p["p"]}" stroke-width="1.4"/>'
                f'<text x="617" y="{211 + i * 62}" text-anchor="middle" '
                f'font-family="{MONO}" font-size="9" fill="{p["hi"]}">LIFT</text>'
                for i in range(7))
            + f'<line x1="600" y1="150" x2="600" y2="620" stroke="{p["p"]}" '
            f'stroke-width="1" stroke-dasharray="5,4" opacity="0.7"/>'
            + _map_node(600, 150, p, "SURFACE LOCK")
            + _map_node(600, 620, p, "MAW GATE")
            + _map_room(170, 220, 240, 110, "WINCH HOUSE", "CABLE / 40T", p)
            + _map_room(790, 220, 240, 110, "COUNTERWEIGHT", "BALLAST HALL", p)
            + _map_room(170, 420, 240, 110, "SUMP PUMPS", "WEEPING DRAIN", p, False)
            + _map_room(790, 420, 240, 110, "SEALED ARCHIVE", "RESTRICTED", p, False)
            + _map_legend(p, ["Lift car position", "Survey node",
                              "Restricted volume"])
            + _compass_rose(1116, 120, p)
            + _map_titleblock(p))
    elif any(k in s for k in ["mine-pits", "mugenhan", "place-entity",
                              "weeping", "current"]):
        # --- cavern / mine survey ----------------------------------------
        import math
        rng = rng_for(slug, "cavern")
        contour = []
        for ring in range(4):
            rx, ry = 330 - ring * 62, 200 - ring * 38
            pts = []
            for i in range(26):
                a = math.radians(i * 360 / 26)
                wob = 1 + rng.uniform(-0.09, 0.09)
                pts.append(f"{600 + rx * wob * math.cos(a):.0f},"
                           f"{400 + ry * wob * math.sin(a):.0f}")
            contour.append(
                f'<polygon points="{" ".join(pts)}" fill="none" '
                f'stroke="{p["p"]}" stroke-width="{2.2 - ring * 0.4}" '
                f'opacity="{0.9 - ring * 0.18}"/>')
        body += (
            "".join(contour)
            + f'<ellipse cx="600" cy="400" rx="52" ry="34" fill="{p["p"]}" '
            f'opacity="0.3" filter="url(#bloomF)"/>'
            + _map_node(600, 400, p, "PRIMARY SHAFT")
            + _map_node(430, 330, p, "ADIT N-2")
            + _map_node(770, 470, p, "ADIT S-1")
            + _map_node(690, 300, p, "PUMP SUMP")
            + f'<path d="M 600 400 L 430 330 M 600 400 L 770 470 M 600 400 '
            f'L 690 300" stroke="{p["p"]}" stroke-width="1.6" '
            f'stroke-dasharray="6,4"/>'
            + _map_room(120, 560, 250, 100, "HEADFRAME", "HOIST / 12T", p)
            + _map_room(830, 560, 250, 100, "SORTING YARD", "HAN ORE", p, False)
            + _map_legend(p, ["Contour interval 10 m", "Drift (dashed)",
                              "Primary shaft"])
            + _compass_rose(1116, 120, p)
            + _map_titleblock(p))
    else:
        # --- department block plan ---------------------------------------
        body += (
            _map_room(400, 230, 400, 230, "MAIN ROOM ATRIUM", "HEALING 6/12", p)
            + f'<circle cx="600" cy="345" r="62" fill="none" stroke="{p["p"]}" '
            f'stroke-width="1.4" stroke-dasharray="7,5"/>'
            + f'<circle cx="600" cy="345" r="30" fill="#04060b" '
            f'stroke="{p["p"]}" stroke-width="2"/>'
            + f'<circle cx="600" cy="345" r="12" fill="{p["p"]}" '
            f'filter="url(#bloomF)"/>'
            + f'<text x="600" y="348" text-anchor="middle" '
            f'font-family="{MONO}" font-size="8" fill="#04060b" '
            f'font-weight="bold">GEN</text>'
            + _map_room(130, 140, 190, 150, "CELL 01", "SUBJECT UNIT", p)
            + _map_room(130, 430, 190, 150, "CELL 02", "SUBJECT UNIT", p)
            + _map_room(880, 140, 190, 150, "CELL 03", "TOOL RELIC", p, False)
            + _map_room(880, 430, 190, 150, "CELL 04", "TOOL RELIC", p, False)
            + f'<path d="M 320 215 L 400 275 M 320 505 L 400 415 '
            f'M 880 215 L 800 275 M 880 505 L 800 415" stroke="{p["p"]}" '
            f'stroke-width="4"/>'
            + f'<line x1="360" y1="228" x2="360" y2="258" stroke="#ff6a5e" '
            f'stroke-width="6"/>'
            + f'<line x1="840" y1="228" x2="840" y2="258" stroke="#ff6a5e" '
            f'stroke-width="6"/>'
            + _map_node(360, 243, p, "AIRLOCK W")
            + _map_node(840, 243, p, "AIRLOCK E")
            + f'<rect x="572" y="480" width="56" height="230" fill="#04060b" '
            f'stroke="{p["p"]}" stroke-width="2"/>'
            + f'<line x1="600" y1="480" x2="600" y2="710" stroke="{p["p"]}" '
            f'stroke-dasharray="4,4"/>'
            + f'<rect x="580" y="560" width="40" height="42" fill="#0b1322" '
            f'stroke="{p["hi"]}" stroke-width="1.4"/>'
            + f'<text x="600" y="585" text-anchor="middle" '
            f'font-family="{MONO}" font-size="9" fill="{p["hi"]}">LIFT</text>'
            + _map_legend(p, ["Airlock checkpoint", "Healing generator",
                              "Lift shaft"])
            + _compass_rose(1116, 120, p)
            + _map_titleblock(p))
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" '
        f'width="1200" height="800">{defs_block(p)}{body}'
        f"{vignette_rect(1200, 800)}{grain_rect(1200, 800)}</svg>")


# ============================================================== GALLERY ===
def _halo(cx, cy, r, p, op=0.5):
    return (
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#coreG)" '
        f'opacity="{op}"/>'
        f'<circle cx="{cx}" cy="{cy}" r="{r * 0.62:.0f}" fill="none" '
        f'stroke="{p["p"]}" stroke-width="1.4" stroke-dasharray="6,5" '
        f'opacity="0.65"/>'
        f'<circle cx="{cx}" cy="{cy}" r="{r * 0.8:.0f}" fill="none" '
        f'stroke="{p["p"]}" stroke-width="0.8" opacity="0.4"/>')


def _hall(p, arch_w=560, top=92, base=482):
    cx = 400
    return (
        f'<path d="M {cx - arch_w / 2} {base} L {cx - arch_w / 2} {top + 70} '
        f'Q {cx - arch_w / 2} {top} {cx} {top} '
        f'Q {cx + arch_w / 2} {top} {cx + arch_w / 2} {top + 70} '
        f'L {cx + arch_w / 2} {base} Z" fill="#070c15" stroke="{IRON}" '
        f'stroke-width="2.5"/>'
        f'<path d="M {cx - arch_w / 2 + 26} {base} '
        f'L {cx - arch_w / 2 + 26} {top + 92} '
        f'Q {cx - arch_w / 2 + 26} {top + 26} {cx} {top + 26} '
        f'Q {cx + arch_w / 2 - 26} {top + 26} {cx + arch_w / 2 - 26} '
        f'{top + 92} L {cx + arch_w / 2 - 26} {base}" fill="none" '
        f'stroke="{p["p"]}" stroke-width="1" opacity="0.45"/>'
        f'<line x1="{cx - 60}" y1="{top - 2}" x2="{cx - 60}" y2="{top + 60}" '
        f'stroke="{p["p"]}" stroke-width="2" opacity="0.5"/>'
        f'<line x1="{cx + 60}" y1="{top - 2}" x2="{cx + 60}" y2="{top + 60}" '
        f'stroke="{p["p"]}" stroke-width="2" opacity="0.5"/>'
        f'<rect x="{cx - arch_w / 2}" y="{base}" width="{arch_w}" height="5" '
        f'fill="{p["p"]}" opacity="0.5"/>'
        + floor_reflection(base + 8, 800, p["p"], 0.12))


def _floor(p, y=470):
    return (
        f'<ellipse cx="400" cy="{y + 6}" rx="300" ry="26" fill="#02040a"/>'
        f'<ellipse cx="400" cy="{y}" rx="250" ry="18" fill="none" '
        f'stroke="{p["p"]}" stroke-width="1.6" opacity="0.55"/>'
        f'<ellipse cx="400" cy="{y}" rx="180" ry="12" fill="none" '
        f'stroke="{p["p"]}" stroke-width="0.9" opacity="0.35"/>'
        + floor_reflection(y + 12, 800, p["p"], 0.10))


def _ledger_page(x, y, rot, op):
    return (
        f'<g transform="rotate({rot} {x} {y})" opacity="{op}">'
        f'<rect x="{x}" y="{y}" width="26" height="17" fill="{BONE}"/>'
        f'<line x1="{x + 4}" y1="{y + 5}" x2="{x + 22}" y2="{y + 5}" '
        f'stroke="#5b6478" stroke-width="1"/>'
        f'<line x1="{x + 4}" y1="{y + 9}" x2="{x + 22}" y2="{y + 9}" '
        f'stroke="#5b6478" stroke-width="1"/>'
        f'<line x1="{x + 4}" y1="{y + 13}" x2="{x + 16}" y2="{y + 13}" '
        f'stroke="#8a2be2" stroke-width="1"/></g>')


# ---------------------------------------------------------- scene: eater --
def sc_specter(p, rng):
    pages = "".join(_ledger_page(x, y, r, o) for x, y, r, o in
                    [(238, 452, -14, 0.9), (300, 466, 9, 0.75),
                     (486, 458, 22, 0.85), (540, 446, -8, 0.7),
                     (262, 470, 4, 0.6)])
    wisps = "".join(
        f'<path d="M {x} 470 Q {x + rng.uniform(-30, 30):.0f} 380 '
        f'{x + rng.uniform(-46, 46):.0f} 300" stroke="{p["p"]}" '
        f'stroke-width="1.6" fill="none" opacity="0.4"/>' for x in
        (300, 340, 460, 500))
    return (
        _hall(p) + _halo(400, 300, 190, p)
        + light_rays(400, 470, p["p"], [(270, 12), (250, 7), (290, 7)], 420,
                     op=0.07)
        + wisps + _floor(p)
        + f'<path d="M 326 470 C 318 320, 348 210, 388 152 '
        f'C 398 136, 410 136, 420 152 C 460 210, 490 320, 482 470 '
        f'Q 440 452 400 470 Q 360 452 326 470 Z" fill="#030509" '
        f'stroke="{p["p"]}" stroke-width="2"/>'
        + f'<path d="M 352 470 C 350 340, 372 240, 396 180" fill="none" '
        f'stroke="{p["p"]}" stroke-width="1.2" opacity="0.55"/>'
        + f'<path d="M 456 470 C 458 340, 436 240, 412 180" fill="none" '
        f'stroke="{p["p"]}" stroke-width="1.2" opacity="0.55"/>'
        + f'<path d="M 376 168 Q 404 138 432 168 Q 404 196 376 168 Z" '
        f'fill="#000000" stroke="{p["p"]}" stroke-width="1.6"/>'
        + f'<circle cx="404" cy="167" r="5" fill="{p["hi"]}" '
        f'filter="url(#bloomF)"/>'
        + f'<line x1="452" y1="112" x2="348" y2="470" stroke="#0d1119" '
        f'stroke-width="9" stroke-linecap="round"/>'
        + f'<line x1="452" y1="112" x2="348" y2="470" stroke="url(#ironG)" '
        f'stroke-width="5.5" stroke-linecap="round"/>'
        + f'<path d="M 452 112 Q 536 58 578 134 Q 494 122 440 124 Z" '
        f'fill="{p["p"]}" stroke="{p["hi"]}" stroke-width="2" '
        f'filter="url(#glowF)"/>'
        + f'<path d="M 470 108 Q 530 70 560 118" fill="none" '
        f'stroke="{p["hi"]}" stroke-width="1.4" opacity="0.9"/>' + pages)


# --------------------------------------------------------- scene: furnace --
def sc_furnace(p, rng):
    vents = "".join(
        f'<path d="M {x} 96 Q {x + rng.uniform(-16, 16):.0f} 66 '
        f'{x + rng.uniform(-24, 24):.0f} 44" stroke="#8b98ad" '
        f'stroke-width="2.4" fill="none" opacity="0.5"/>' for x in
        (360, 400, 440))
    return (
        _hall(p, arch_w=620) + _halo(400, 300, 170, p)
        + f'<rect x="196" y="150" width="408" height="320" rx="10" '
        f'fill="url(#ironG)" stroke="{IRON_SOFT}" stroke-width="3"/>'
        + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="#05070c" '
                  f'stroke="{p["p"]}" stroke-width="1.2"/>'
                  for x in (214, 586) for y in (168, 452))
        + f'<rect x="196" y="150" width="408" height="26" rx="10" fill="{p["s"]}" '
        f'opacity="0.85"/>' + vents
        + f'<line x1="400" y1="150" x2="400" y2="96" stroke="#05070c" '
        f'stroke-width="16"/>'
        + f'<line x1="400" y1="150" x2="400" y2="96" stroke="url(#ironG)" '
        f'stroke-width="10"/>'
        + f'<circle cx="400" cy="305" r="112" fill="#04060b" stroke="{p["p"]}" '
        f'stroke-width="4"/>'
        + f'<circle cx="400" cy="305" r="88" fill="#1c0a08" stroke="{p["p"]}" '
        f'stroke-width="2"/>'
        + f'<circle cx="400" cy="305" r="58" fill="{p["p"]}" '
        f'filter="url(#bloomF)"/>'
        + f'<circle cx="400" cy="305" r="30" fill="{p["hi"]}" opacity="0.95"/>'
        + f'<path d="M 382 328 Q 400 268 418 328 Q 400 316 382 328 Z" '
        f'fill="#fff" opacity="0.85"/>'
        + "".join(f'<rect x="{x}" y="{y}" width="46" height="30" rx="3" '
                  f'fill="url(#ironG)" stroke="{p["p"]}" stroke-width="1.6"/>'
                  for x, y in [(150, 220), (604, 220), (150, 350), (604, 350)])
        + _floor(p, 478) + mist_band(150, 440, 500, 40, p["mist"], 0.14))


# -------------------------------------------------------- scene: astrolabe --
def sc_astrolabe(p, rng):
    rings = "".join(
        f'<circle cx="400" cy="252" r="{r}" fill="none" stroke="{p["p"]}" '
        f'stroke-width="1.1" opacity="{o}"/>' for r, o in
        [(118, 0.5), (140, 0.35), (162, 0.22)])
    ticks = knurled_ring(400, 252, 96, 36, p["p"], op=0.6, wdt=1.4, tick=6)
    return (
        _hall(p) + _halo(400, 252, 200, p)
        + light_rays(400, 252, p["p"], [(90, 14), (270, 14)], 380, op=0.06)
        + f'<ellipse cx="400" cy="470" rx="200" ry="24" fill="#02040a"/>'
        + f'<polygon points="356,470 444,470 424,330 376,330" fill="url(#ironG)" '
        f'stroke="{p["p"]}" stroke-width="2"/>'
        + f'<rect x="368" y="318" width="64" height="14" rx="3" fill="{p["s"]}" '
        f'stroke="{p["p"]}" stroke-width="1.4"/>' + rings + ticks
        + f'<circle cx="400" cy="252" r="82" fill="#0a1020" stroke="{p["p"]}" '
        f'stroke-width="3"/>'
        + f'<circle cx="400" cy="252" r="66" fill="none" stroke="{p["p"]}" '
        f'stroke-width="1.4" stroke-dasharray="7,5"/>'
        + f'<circle cx="400" cy="252" r="46" fill="#141c30" stroke="{p["p"]}" '
        f'stroke-width="2"/>'
        + f'<polygon points="400,188 409,252 400,241 391,252" fill="{p["p"]}" '
        f'stroke="{p["hi"]}" stroke-width="0.9" filter="url(#glowF)"/>'
        + f'<polygon points="400,316 409,252 400,263 391,252" '
        f'fill="{IRON_SOFT}"/>'
        + f'<polygon points="336,252 400,241 389,252 400,263" '
        f'fill="{IRON_SOFT}"/>'
        + f'<polygon points="464,252 400,241 411,252 400,263" '
        f'fill="{IRON_SOFT}"/>'
        + f'<circle cx="400" cy="252" r="9" fill="{p["hi"]}" '
        f'stroke="{p["p"]}" stroke-width="2.2"/>'
        + "".join(f'<circle cx="{x}" cy="{y}" r="2.4" fill="{p["hi"]}"/>' for
                  x, y in [(330, 190), (472, 200), (350, 320), (458, 322)])
        + _floor(p, 478))


# ------------------------------------------------------------ scene: scale --
def sc_scale(p, rng):
    chains = "".join(
        f'<circle cx="{x}" cy="{y + i * 9}" r="1.8" fill="{p["hi"]}" '
        f'opacity="0.8"/>' for x, y in [(252, 268), (548, 262)]
        for i in range(6))
    return (
        _hall(p) + _halo(400, 300, 180, p)
        + f'<ellipse cx="400" cy="474" rx="230" ry="24" fill="#02040a"/>'
        + f'<rect x="292" y="408" width="216" height="62" rx="5" '
        f'fill="url(#ironG)" stroke="{p["p"]}" stroke-width="2"/>'
        + f'<rect x="292" y="408" width="216" height="14" rx="5" '
        f'fill="{p["s"]}" opacity="0.9"/>'
        + f'<line x1="400" y1="196" x2="400" y2="410" stroke="{p["p"]}" '
        f'stroke-width="7" stroke-linecap="round"/>'
        + f'<line x1="400" y1="196" x2="400" y2="410" stroke="{p["hi"]}" '
        f'stroke-width="1.6" opacity="0.8"/>'
        + f'<circle cx="400" cy="188" r="8" fill="{p["hi"]}" '
        f'stroke="{p["p"]}" stroke-width="2"/>'
        + f'<line x1="252" y1="238" x2="548" y2="238" stroke="{p["p"]}" '
        f'stroke-width="5" stroke-linecap="round"/>'
        + f'<circle cx="400" cy="238" r="9" fill="#0b0f17" stroke="{p["hi"]}" '
        f'stroke-width="2"/>'
        + f'<line x1="252" y1="238" x2="222" y2="332" stroke="{IRON_SOFT}" '
        f'stroke-width="2.2"/>'
        + f'<line x1="252" y1="238" x2="282" y2="332" stroke="{IRON_SOFT}" '
        f'stroke-width="2.2"/>'
        + f'<path d="M 212 332 Q 252 364 292 332 Z" fill="#0c1220" '
        f'stroke="{p["p"]}" stroke-width="2.2"/>'
        + f'<circle cx="242" cy="330" r="9" fill="#04060b" stroke="{p["p"]}" '
        f'stroke-width="1.4"/>'
        + f'<circle cx="264" cy="328" r="10" fill="#04060b" stroke="{p["p"]}" '
        f'stroke-width="1.4"/>'
        + f'<line x1="548" y1="238" x2="518" y2="302" stroke="{IRON_SOFT}" '
        f'stroke-width="2.2"/>'
        + f'<line x1="548" y1="238" x2="578" y2="302" stroke="{IRON_SOFT}" '
        f'stroke-width="2.2"/>'
        + f'<path d="M 508 302 Q 548 334 588 302 Z" fill="#0c1220" '
        f'stroke="{p["p"]}" stroke-width="2.2"/>'
        + f'<polygon points="548,282 557,300 539,300" fill="{p["hi"]}" '
        f'filter="url(#glowF)"/>' + chains + _floor(p, 478))


# ------------------------------------------------------------ scene: squad --
def _operative(x, base_y, h, p, lead):
    armor = p["p"] if lead else IRON_SOFT
    fill = "#1a2334" if lead else "#101623"
    w = 26 if lead else 21
    return (
        f'<path d="M {x - w} {base_y} L {x - w + 5} {base_y - h} '
        f'L {x + w - 5} {base_y - h} L {x + w} {base_y} Z" fill="{fill}" '
        f'stroke="{armor}" stroke-width="2"/>'
        f'<circle cx="{x}" cy="{base_y - h - 20}" r="17" fill="#0b0f17" '
        f'stroke="{armor}" stroke-width="2"/>'
        f'<rect x="{x - 9}" y="{base_y - h - 25}" width="18" height="7" rx="2" '
        f'fill="{armor}" filter="url(#glowF)"/>'
        f'<line x1="{x + w - 6}" y1="{base_y - h + 26}" x2="{x + w + 34}" '
        f'y2="{base_y - h + 8}" stroke="{armor}" stroke-width="4.5" '
        f'stroke-linecap="round"/>'
        f'<line x1="{x}" y1="{base_y - h + 6}" x2="{x}" y2="{base_y - 8}" '
        f'stroke="{armor}" stroke-width="1.2" opacity="0.6"/>')


def sc_squad(p, rng):
    return (
        f'<rect x="90" y="96" width="620" height="384" fill="#060a12" '
        f'stroke="{IRON}" stroke-width="2.5"/>'
        + f'<line x1="90" y1="428" x2="710" y2="428" stroke="{p["p"]}" '
        + f'stroke-width="3"/>'
        + "".join(f'<rect x="{x}" y="120" width="26" height="308" '
                  f'fill="#0b101c" stroke="{IRON}" stroke-width="1.2"/>'
                  for x in (140, 634))
        + "".join(f'<rect x="{x}" y="132" width="26" height="10" '
                  f'fill="{p["p"]}" opacity="0.7"/>' for x in (140, 634))
        + _halo(400, 300, 170, p, 0.35)
        + _operative(298, 428, 128, p, False)
        + _operative(400, 428, 150, p, True)
        + _operative(502, 428, 128, p, False)
        + f'<ellipse cx="400" cy="452" rx="240" ry="18" fill="#02040a"/>'
        + mist_band(150, 420, 500, 36, p["mist"], 0.13)
        + _floor(p, 478))


# ---------------------------------------------------------- scene: monolith --
def sc_monolith(p, rng):
    cracks = "".join(
        f'<path d="M 400 200 L {400 + dx} {300 + i * 40} L {400 + dx + d2} '
        f'{340 + i * 40}" stroke="{p["p"]}" stroke-width="1.6" fill="none" '
        f'opacity="0.7" filter="url(#glowF)"/>'
        for i, (dx, d2) in enumerate([(-26, 14), (30, -12), (-8, 20)]))
    return (
        f'<rect x="90" y="96" width="620" height="384" fill="#0e0609" '
        f'stroke="{p["p"]}" stroke-width="2.5"/>'
        + f'<line x1="90" y1="428" x2="710" y2="428" stroke="{p["p"]}" '
        + f'stroke-width="3"/>'
        + "".join(f'<circle cx="{x}" cy="130" r="9" fill="{p["p"]}" '
                  f'filter="url(#bloomF)"/>'
                  f'<circle cx="{x}" cy="130" r="15" fill="none" '
                  f'stroke="{p["p"]}" stroke-width="1" opacity="0.6"/>'
                  for x in (150, 650))
        + _halo(400, 280, 190, p)
        + f'<polygon points="400,116 496,428 304,428" fill="#160709" '
        f'stroke="{p["p"]}" stroke-width="3"/>'
        + f'<polygon points="400,166 462,398 338,398" fill="none" '
        f'stroke="{p["p"]}" stroke-width="1.4" stroke-dasharray="5,4" '
        f'opacity="0.7"/>' + cracks
        + f'<circle cx="400" cy="272" r="30" fill="{p["p"]}" '
        f'filter="url(#bloomF)"/>'
        + f'<circle cx="400" cy="272" r="14" fill="{p["hi"]}"/>'
        + f'<circle cx="400" cy="272" r="5" fill="#160709"/>'
        + f'<ellipse cx="400" cy="452" rx="230" ry="18" fill="#02040a"/>'
        + _floor(p, 478))


# ------------------------------------------------------------- scene: train --
def sc_train(p, rng):
    cars = "".join(
        f'<rect x="{x}" y="300" width="150" height="96" rx="8" '
        f'fill="url(#ironG)" stroke="{p["p"]}" stroke-width="2.4"/>'
        f'<rect x="{x}" y="300" width="150" height="22" rx="8" fill="{p["s"]}" '
        f'opacity="0.9"/>'
        + "".join(f'<rect x="{x + 18 + i * 30}" y="336" width="16" height="22" '
                  f'rx="2" fill="{p["p"]}" opacity="0.85"/>' for i in range(4))
        + f'<circle cx="{x + 40}" cy="404" r="16" fill="#05070c" '
        f'stroke="{p["p"]}" stroke-width="2.4"/>'
        + f'<circle cx="{x + 110}" cy="404" r="16" fill="#05070c" '
        f'stroke="{p["p"]}" stroke-width="2.4"/>' for x in (150, 310, 470))
    smoke = "".join(
        f'<circle cx="{230 + i * 26}" cy="{238 - i * 26}" r="{14 + i * 7}" '
        f'fill="#8b98ad" opacity="{0.34 - i * 0.06}"/>' for i in range(4))
    return (
        _halo(400, 280, 220, p, 0.4) + smoke
        + f'<polygon points="150,300 120,262 180,262 210,300" fill="url(#ironG)" '
        f'stroke="{p["p"]}" stroke-width="2.2"/>'
        + f'<circle cx="128" cy="330" r="14" fill="{p["hi"]}" '
        f'filter="url(#bloomF)"/>' + cars
        + f'<rect x="110" y="424" width="580" height="10" fill="{p["s"]}" '
        f'opacity="0.9"/>' + "".join(
            f'<line x1="{x}" y1="424" x2="{x}" y2="448" stroke="{IRON_SOFT}" '
            f'stroke-width="4"/>' for x in range(130, 680, 34))
        + f'<ellipse cx="400" cy="462" rx="300" ry="20" fill="#02040a"/>'
        + mist_band(140, 430, 520, 36, p["mist"], 0.13) + _floor(p, 482))


# ------------------------------------------------------------- scene: river --
def sc_river(p, rng):
    bands = "".join(
        f'<path d="M 120 {300 + i * 34} Q 280 {282 + i * 34} 400 '
        f'{300 + i * 34} T 680 {300 + i * 34}" fill="none" stroke="{p["p"]}" '
        f'stroke-width="{7 - i}" opacity="{0.5 - i * 0.09}" '
        f'filter="url(#glowF)"/>' for i in range(4))
    falls = "".join(
        f'<rect x="{x}" y="150" width="12" height="150" fill="{p["p"]}" '
        f'opacity="0.35" filter="url(#bloomF)"/>' for x in (250, 420, 560))
    return (
        _hall(p, arch_w=660) + _halo(400, 330, 190, p, 0.4) + falls
        + f'<path d="M 120 300 Q 280 282 400 300 T 680 300 L 680 470 L 120 470 Z" '
        f'fill="#08131f" stroke="{p["p"]}" stroke-width="2"/>' + bands
        + "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="{p["hi"]}"/>' for
                  x, y in [(200, 330), (330, 356), (470, 336), (590, 370),
                           (270, 400), (520, 410)])
        + "".join(f'<polygon points="{x},250 {x + 14},250 {x + 7},292" '
                  f'fill="{IRON_SOFT}" opacity="0.8"/>' for x in
                  (180, 320, 480, 600))
        + _floor(p, 482))


# ----------------------------------------------------------- scene: archive --
def sc_archive(p, rng):
    shelves = "".join(
        f'<rect x="{x}" y="150" width="120" height="250" fill="#0a0e18" '
        f'stroke="{IRON}" stroke-width="2"/>'
        + "".join(f'<rect x="{x + 10}" y="{y}" width="100" height="12" '
                  f'fill="{p["s"] if (i % 3 == 0) else "#1a2334"}" '
                  f'stroke="{p["p"]}" stroke-width="0.7" opacity="0.9"/>'
                  for i, y in enumerate(range(170, 380, 26)))
        for x in (120, 560))
    return (
        _hall(p, arch_w=700) + shelves + _halo(400, 300, 170, p, 0.4)
        + f'<rect x="300" y="380" width="200" height="24" rx="3" '
        f'fill="url(#ironG)" stroke="{p["p"]}" stroke-width="1.6"/>'
        + f'<rect x="312" y="388" width="14" height="84" fill="url(#ironG)"/>'
        + f'<rect x="474" y="388" width="14" height="84" fill="url(#ironG)"/>'
        + f'<polygon points="400,252 492,292 492,372 400,332 Z" fill="{p["s"]}" '
        f'stroke="{p["p"]}" stroke-width="2"/>'
        + f'<polygon points="400,252 308,292 308,372 400,332 Z" fill="#1a2334" '
        f'stroke="{p["p"]}" stroke-width="2"/>'
        + "".join(f'<line x1="322" y1="{y}" x2="386" y2="{y - 22}" '
                  f'stroke="{BONE}" stroke-width="1" opacity="0.7"/>'
                  for y in (330, 342, 354))
        + "".join(f'<line x1="414" y1="{y - 22}" x2="478" y2="{y}" '
                  f'stroke="{BONE}" stroke-width="1" opacity="0.7"/>'
                  for y in (330, 342, 354))
        + f'<circle cx="400" cy="252" r="8" fill="{p["hi"]}" '
        f'filter="url(#bloomF)"/>'
        + light_rays(400, 300, p["p"], [(270, 10)], 300, op=0.08)
        + _floor(p, 482))


# --------------------------------------------------------------- scene: loom --
def sc_loom(p, rng):
    threads = "".join(
        f'<line x1="{200 + i * 30}" y1="150" x2="{200 + i * 30}" y2="380" '
        f'stroke="{p["p"]}" stroke-width="1" opacity="0.55"/>' for i in range(14))
    blades = "".join(
        f'<polygon points="{x},170 {x + 16},200 {x + 8},300 {x - 8},300 '
        f'{x},{200}" fill="{p["hi"]}" stroke="{p["p"]}" stroke-width="1.4" '
        f'opacity="0.95" filter="url(#glowF)"/>' for x in (250, 400, 550))
    return (
        _hall(p) + _halo(400, 280, 180, p, 0.4)
        + f'<rect x="180" y="130" width="440" height="18" rx="6" '
        f'fill="url(#ironG)" stroke="{p["p"]}" stroke-width="1.6"/>'
        + f'<rect x="180" y="380" width="440" height="18" rx="6" '
        f'fill="url(#ironG)" stroke="{p["p"]}" stroke-width="1.6"/>'
        + f'<rect x="168" y="130" width="20" height="268" fill="url(#ironG)"/>'
        + f'<rect x="612" y="130" width="20" height="268" fill="url(#ironG)"/>'
        + threads + blades
        + f'<ellipse cx="400" cy="470" rx="240" ry="20" fill="#02040a"/>'
        + _floor(p, 482))


# ---------------------------------------------------------- scene: cell_door --
def sc_cell_door(p, rng):
    return (
        _hall(p, arch_w=640) + _halo(400, 290, 180, p, 0.4)
        + f'<rect x="270" y="150" width="260" height="300" rx="8" '
        f'fill="url(#ironG)" stroke="{p["p"]}" stroke-width="3"/>'
        + f'<rect x="270" y="150" width="260" height="34" rx="8" '
        f'fill="{p["s"]}" opacity="0.9"/>'
        + f'<rect x="286" y="200" width="96" height="60" rx="4" fill="#04060b" '
        f'stroke="{p["p"]}" stroke-width="2"/>'
        + f'<circle cx="310" cy="230" r="12" fill="{p["p"]}" '
        f'filter="url(#bloomF)"/>'
        + f'<circle cx="350" cy="230" r="6" fill="{p["hi"]}" opacity="0.9"/>'
        + f'<rect x="398" y="200" width="116" height="60" rx="4" fill="#04060b" '
        f'stroke="{p["p"]}" stroke-width="2"/>'
        + "".join(f'<rect x="408" y="{246 - i * 12}" width="96" height="7" '
                  f'fill="{p["p"]}" opacity="{0.9 - i * 0.18}"/>' for i in range(4))
        + f'<circle cx="400" cy="350" r="34" fill="#04060b" stroke="{p["p"]}" '
        f'stroke-width="2.6"/>'
        + "".join(f'<line x1="400" y1="350" x2="{400 + 34 * (1 if i % 2 == 0 else -1) * 0.7:.0f}" '
                  f'y2="{350 + (26 if i < 2 else -26)}" stroke="{p["p"]}" '
                  f'stroke-width="4"/>' for i in range(4))
        + f'<circle cx="400" cy="350" r="8" fill="{p["hi"]}" '
        f'stroke="{p["p"]}" stroke-width="2"/>'
        + f'<rect x="150" y="300" width="60" height="26" fill="url(#ironG)" '
        f'stroke="{p["p"]}" stroke-width="1.4"/>'
        + f'<rect x="590" y="300" width="60" height="26" fill="url(#ironG)" '
        f'stroke="{p["p"]}" stroke-width="1.4"/>'
        + _floor(p, 478))


# --------------------------------------------------------------- scene: rift --
def sc_rift(p, rng):
    shards = "".join(
        f'<polygon points="{x},{y} {x + 18},{y + 8} {x + 6},{y + 30}" '
        f'fill="{IRON_SOFT}" stroke="{p["p"]}" stroke-width="1" opacity="0.9" '
        f'transform="rotate({rng.uniform(-30, 30):.0f} {x} {y})"/>' for x, y in
        [(250, 200), (520, 180), (300, 360), (490, 380), (220, 300), (560, 300)])
    return (
        _hall(p) + _halo(400, 290, 200, p, 0.55)
        + f'<path d="M 372 110 C 350 200, 448 260, 380 340 C 350 380, 420 430, '
        f'396 478 L 428 478 C 452 420, 380 370, 410 330 C 478 250, 380 190, '
        f'404 110 Z" fill="{p["p"]}" filter="url(#bloomF)"/>'
        + f'<path d="M 392 110 C 376 200, 442 260, 392 340 C 370 380, 414 430, '
        f'398 478" fill="none" stroke="{p["hi"]}" stroke-width="3"/>'
        + shards
        + light_rays(400, 290, p["p"], [(0, 12), (180, 12)], 380, op=0.07)
        + _floor(p, 482))


# -------------------------------------------------------- scene: instruments --
def sc_instruments(p, rng):
    dials = "".join(
        f'<circle cx="{x}" cy="250" r="52" fill="#0a0f18" stroke="{p["p"]}" '
        f'stroke-width="2.4"/>'
        f'<path d="M {x - 36} 268 A 44 44 0 0 1 {x + 36} 268" fill="none" '
        f'stroke="{p["s"]}" stroke-width="7"/>'
        f'<path d="M {x - 36} 268 A 44 44 0 0 1 {x + a} {268 + b}" fill="none" '
        f'stroke="{p["p"]}" stroke-width="7"/>'
        f'<line x1="{x}" y1="250" x2="{x + c}" y2="{250 + d}" '
        f'stroke="{p["hi"]}" stroke-width="3" stroke-linecap="round"/>'
        f'<circle cx="{x}" cy="250" r="6" fill="#0a0f18" stroke="{p["p"]}" '
        f'stroke-width="2"/>' for x, a, b, c, d in
        [(230, 10, -38, 18, -26), (400, 30, -18, 30, -6), (570, -8, -40, -14, -28)])
    return (
        _hall(p, arch_w=680) + _halo(400, 280, 180, p, 0.35)
        + f'<rect x="150" y="150" width="500" height="230" rx="10" '
        f'fill="url(#ironG)" stroke="{IRON_SOFT}" stroke-width="3"/>' + dials
        + "".join(f'<rect x="{200 + i * 90}" y="392" width="56" height="60" rx="4" '
                  f'fill="#0a0f18" stroke="{p["p"]}" stroke-width="1.6"/>'
                  f'<rect x="{206 + i * 90}" y="{398 + (i % 3) * 8}" width="44" '
                  f'height="6" fill="{p["p"]}" opacity="0.8"/>'
                  f'<circle cx="{228 + i * 90}" cy="434" r="7" fill="{p["p"]}" '
                  f'filter="url(#glowF)"/>' for i in range(4))
        + _floor(p, 482))


# -------------------------------------------------------- scene: chart_table --
def sc_chart_table(p, rng):
    stars_c = "".join(
        f'<circle cx="{220 + rng.uniform(0, 360):.0f}" '
        f'cy="{180 + rng.uniform(0, 180):.0f}" r="2.6" fill="{p["hi"]}"/>' for _ in
        range(16))
    lines = "".join(
        f'<line x1="{220 + rng.uniform(0, 360):.0f}" '
        f'y1="{180 + rng.uniform(0, 180):.0f}" '
        f'x2="{220 + rng.uniform(0, 360):.0f}" '
        f'y2="{180 + rng.uniform(0, 180):.0f}" stroke="{p["p"]}" '
        f'stroke-width="1" opacity="0.5"/>' for _ in range(9))
    return (
        _hall(p, arch_w=700) + _halo(400, 280, 180, p, 0.35)
        + f'<polygon points="170,400 630,400 580,470 220,470" fill="url(#ironG)" '
        f'stroke="{p["p"]}" stroke-width="2"/>'
        + f'<polygon points="200,168 600,168 650,392 150,392" fill="#0a1020" '
        f'stroke="{GILT}" stroke-width="2.4"/>' + lines + stars_c
        + f'<circle cx="400" cy="275" r="34" fill="none" stroke="{p["p"]}" '
        f'stroke-width="2"/>'
        + f'<circle cx="400" cy="275" r="12" fill="{p["p"]}" '
        f'filter="url(#bloomF)"/>'
        + guilloche(400, 275, [52, 66], p["p"], 0.5)
        + _floor(p, 484))


# -------------------------------------------------------------- scene: choir --
def sc_choir(p, rng):
    bells = "".join(
        f'<line x1="{x}" y1="130" x2="{x}" y2="{y - 52}" stroke="{p["p"]}" '
        f'stroke-width="3"/>'
        f'<path d="M {x - 30} {y} Q {x - 30} {y - 48} {x} {y - 48} '
        f'Q {x + 30} {y - 48} {x + 30} {y} L {x + 38} {y + 12} '
        f'L {x - 38} {y + 12} Z" fill="url(#giltG)" stroke="{p["p"]}" '
        f'stroke-width="1.8"/>'
        f'<circle cx="{x}" cy="{y + 22}" r="8" fill="{p["p"]}" '
        f'stroke="{p["hi"]}" stroke-width="1.2"/>'
        f'<path d="M {x - 52} {y - 20} Q {x - 62} {y + 6} {x - 54} {y + 26}" '
        f'fill="none" stroke="{p["p"]}" stroke-width="1.8" opacity="0.7"/>'
        f'<path d="M {x + 52} {y - 20} Q {x + 62} {y + 6} {x + 54} {y + 26}" '
        f'fill="none" stroke="{p["p"]}" stroke-width="1.8" opacity="0.7"/>'
        for x, y in [(250, 300), (400, 260), (550, 300)])
    return (
        _hall(p) + _halo(400, 280, 190, p, 0.4)
        + f'<rect x="150" y="118" width="500" height="16" rx="6" '
        f'fill="url(#ironG)" stroke="{p["p"]}" stroke-width="1.4"/>' + bells
        + mist_band(170, 400, 460, 44, p["mist"], 0.13) + _floor(p, 482))


# ---------------------------------------------------------- scene: hourglass --
def sc_hourglass(p, rng):
    return (
        _hall(p) + _halo(400, 280, 180, p, 0.4)
        + f'<rect x="310" y="140" width="180" height="16" rx="6" '
        f'fill="url(#ironG)" stroke="{p["p"]}" stroke-width="1.6"/>'
        + f'<rect x="310" y="404" width="180" height="16" rx="6" '
        f'fill="url(#ironG)" stroke="{p["p"]}" stroke-width="1.6"/>'
        + f'<rect x="300" y="140" width="16" height="280" fill="url(#ironG)"/>'
        + f'<rect x="484" y="140" width="16" height="280" fill="url(#ironG)"/>'
        + f'<polygon points="330,160 470,160 400,280 Z" fill="#0a1020" '
        f'stroke="{p["p"]}" stroke-width="2"/>'
        + f'<polygon points="330,400 470,400 400,280 Z" fill="#0a1020" '
        f'stroke="{p["p"]}" stroke-width="2"/>'
        + f'<polygon points="352,160 448,160 400,248 Z" fill="{p["p"]}" '
        f'opacity="0.75"/>'
        + f'<polygon points="360,400 440,400 400,320 Z" fill="{p["p"]}" '
        f'opacity="0.75"/>'
        + f'<line x1="400" y1="252" x2="400" y2="316" stroke="{p["hi"]}" '
        f'stroke-width="2.6" filter="url(#glowF)"/>'
        + f'<path d="M 470 190 L 448 230 L 462 262" fill="none" '
        f'stroke="{p["hi"]}" stroke-width="1.4" opacity="0.9"/>'
        + f'<ellipse cx="400" cy="470" rx="200" ry="20" fill="#02040a"/>'
        + _floor(p, 482))


# ------------------------------------------------------------- scene: mirror --
def sc_mirror(p, rng):
    return (
        _hall(p) + _halo(400, 290, 170, p, 0.4)
        + f'<ellipse cx="400" cy="330" rx="170" ry="110" fill="#0a1020" '
        f'stroke="{GILT}" stroke-width="3"/>'
        + f'<ellipse cx="400" cy="330" rx="150" ry="94" fill="{p["s"]}" '
        f'opacity="0.5"/>'
        + f'<ellipse cx="400" cy="330" rx="104" ry="62" fill="{p["p"]}" '
        f'opacity="0.35" filter="url(#bloomF)"/>'
        + "".join(f'<ellipse cx="400" cy="330" rx="{rx}" ry="{rx * 0.6:.0f}" '
                  f'fill="none" stroke="{p["hi"]}" stroke-width="1.2" '
                  f'opacity="{o}"/>' for rx, o in
                  [(60, 0.7), (90, 0.5), (122, 0.3)])
        + f'<path d="M 368 330 Q 400 300 432 330 Q 400 348 368 330 Z" '
        f'fill="#04060b" stroke="{p["hi"]}" stroke-width="1.6"/>'
        + f'<circle cx="400" cy="328" r="5" fill="{p["hi"]}" '
        f'filter="url(#bloomF)"/>'
        + "".join(f'<rect x="{x}" y="430" width="26" height="44" '
                  f'fill="url(#ironG)" stroke="{p["p"]}" stroke-width="1.4"/>'
                  for x in (280, 494))
        + _floor(p, 484))


# -------------------------------------------------------------- scene: tanks --
def sc_tanks(p, rng):
    tanks = "".join(
        f'<rect x="{x}" y="180" width="110" height="240" rx="14" '
        f'fill="#0a1020" stroke="{p["p"]}" stroke-width="2.6"/>'
        f'<rect x="{x}" y="180" width="110" height="30" rx="14" '
        f'fill="{p["s"]}" opacity="0.9"/>'
        f'<rect x="{x + 10}" y="{250 + i * 22}" width="90" height="160" '
        f'fill="{p["p"]}" opacity="0.5" filter="url(#glowF)"/>'
        f'<rect x="{x + 10}" y="{250 + i * 22}" width="90" height="10" '
        f'fill="{p["hi"]}" opacity="0.85"/>'
        + "".join(f'<circle cx="{x + 30 + j * 22}" cy="{300 + i * 22 + k * 24}" '
                  f'r="3.4" fill="{p["hi"]}" opacity="0.8"/>' for j in range(3)
                  for k in range(3))
        for i, x in enumerate((200, 345, 490)))
    pipes = "".join(
        f'<line x1="{x}" y1="180" x2="{x}" y2="130" stroke="url(#ironG)" '
        f'stroke-width="12"/>' for x in (255, 400, 545))
    return (
        _hall(p, arch_w=680) + _halo(400, 300, 190, p, 0.4) + pipes
        + f'<rect x="180" y="114" width="440" height="20" rx="8" '
        f'fill="url(#ironG)" stroke="{p["p"]}" stroke-width="1.6"/>' + tanks
        + _floor(p, 482))


# ---------------------------------------------------------------- scene: gate --
def sc_gate(p, rng):
    rings = "".join(
        f'<circle cx="400" cy="330" r="{r}" fill="none" stroke="{p["p"]}" '
        f'stroke-width="{w}" opacity="{o}"/>' for r, w, o in
        [(120, 3, 0.9), (100, 1.4, 0.6), (140, 1, 0.4)])
    steps = "".join(
        f'<rect x="{400 - w / 2}" y="{452 - i * 14}" width="{w}" height="14" '
        f'fill="url(#ironG)" stroke="{p["p"]}" stroke-width="1" opacity="0.9"/>'
        for i, w in enumerate((360, 300, 240)))
    return (
        _hall(p, arch_w=700) + _halo(400, 330, 200, p, 0.5) + rings
        + f'<circle cx="400" cy="330" r="80" fill="{p["s"]}" opacity="0.55"/>'
        + f'<circle cx="400" cy="330" r="48" fill="{p["p"]}" '
        f'filter="url(#bloomF)"/>'
        + f'<circle cx="400" cy="330" r="20" fill="{p["hi"]}"/>'
        + knurled_ring(400, 330, 132, 40, p["p"], op=0.6, wdt=1.6, tick=8)
        + "".join(f'<rect x="{x}" y="200" width="34" height="252" '
                  f'fill="url(#ironG)" stroke="{p["p"]}" stroke-width="1.6"/>'
                  for x in (226, 540))
        + steps + _floor(p, 484))


# ------------------------------------------------------------- scene: totems --
def sc_totems(p, rng):
    cols = ["#ff6a5e", "#4cc3ff", "#c084fc", "#93a4ff"]
    pil = "".join(
        f'<rect x="{x}" y="{250 - h}" width="64" height="{h + 200}" rx="6" '
        f'fill="#0a0f18" stroke="{c}" stroke-width="2.4"/>'
        f'<rect x="{x}" y="{250 - h}" width="64" height="18" rx="6" fill="{c}" '
        f'opacity="0.85"/>'
        f'<circle cx="{x + 32}" cy="{292 - h}" r="14" fill="{c}" '
        f'filter="url(#bloomF)"/>'
        + "".join(f'<rect x="{x + 12}" y="{y}" width="40" height="6" fill="{c}" '
                  f'opacity="{0.85 - (y - 320) / 400}"/>' for y in
                  range(320, 420, 22)) for x, h, c in
        [(180, 60, cols[0]), (296, 110, cols[1]), (412, 80, cols[2]),
         (528, 130, cols[3])])
    return (
        _hall(p, arch_w=700) + _halo(400, 300, 190, p, 0.3) + pil
        + mist_band(150, 430, 500, 36, p["mist"], 0.12) + _floor(p, 482))


# ---------------------------------------------------------- scene: war_table --
def sc_war_table(p, rng):
    tokens = "".join(
        f'<circle cx="{x}" cy="{y}" r="11" fill="{c}" stroke="{p["hi"]}" '
        f'stroke-width="1.4" filter="url(#glowF)"/>' for x, y, c in
        [(300, 330, p["p"]), (380, 300, "#4cc3ff"), (460, 340, "#ff6a5e"),
         (520, 305, "#4ade80"), (350, 370, GILT)])
    return (
        _hall(p, arch_w=700) + _halo(400, 320, 180, p, 0.35)
        + f'<polygon points="170,392 630,392 580,470 220,470" fill="url(#ironG)" '
        f'stroke="{p["p"]}" stroke-width="2.2"/>'
        + f'<polygon points="205,220 595,220 630,380 170,380" fill="#0c1322" '
        f'stroke="{GILT}" stroke-width="2.2"/>' + "".join(
            f'<line x1="{200 + i * 44}" y1="222" x2="{186 + i * 44}" y2="378" '
            f'stroke="{IRON}" stroke-width="1"/>' for i in range(10))
        + "".join(f'<line x1="198" y1="{240 + i * 28}" x2="602" y2="{240 + i * 28}" '
                  f'stroke="{IRON}" stroke-width="1"/>' for i in range(5))
        + tokens
        + f'<path d="M 300 330 L 380 300 L 460 340" fill="none" '
        f'stroke="{p["hi"]}" stroke-width="1.4" stroke-dasharray="5,4"/>'
        + f'<rect x="180" y="180" width="120" height="26" fill="#04060b" '
        f'opacity="0.9" stroke="{p["p"]}" stroke-width="1.2"/>'
        + f'<text x="240" y="198" text-anchor="middle" font-family="{MONO}" '
        f'font-size="11" font-weight="bold" fill="{p["p"]}">WAR TABLE</text>'
        + _floor(p, 484))


# ------------------------------------------------------------ scene: ribbons --
def sc_ribbons(p, rng):
    rib = "".join(
        f'<path d="M 140 {200 + i * 46} C 300 {160 + i * 46}, 500 '
        f'{240 + i * 46}, 660 {200 + i * 46}" fill="none" stroke="{c}" '
        f'stroke-width="{9 - i * 1.4}" opacity="0.55" filter="url(#glowF)"/>'
        for i, c in enumerate([p["p"], p["hi"], p["s"], GILT]))
    motes = "".join(
        f'<circle cx="{220 + rng.uniform(0, 360):.0f}" '
        f'cy="{180 + rng.uniform(0, 220):.0f}" r="2.4" fill="{p["hi"]}"/>' for _ in
        range(22))
    return (
        _hall(p) + _halo(400, 300, 190, p, 0.4) + rib + motes
        + f'<circle cx="400" cy="300" r="34" fill="{p["p"]}" '
        f'filter="url(#bloomF)"/>'
        + f'<circle cx="400" cy="300" r="14" fill="{p["hi"]}"/>'
        + _floor(p, 482))


# ----------------------------------------------------- scene: relic_pedestal --
def sc_relic_pedestal(p, rng):
    return (
        _hall(p) + _halo(400, 250, 170, p, 0.5)
        + light_rays(400, 240, p["p"], [(90, 10)], 320, op=0.09)
        + f'<polygon points="360,470 440,470 424,340 376,340" fill="url(#ironG)" '
        f'stroke="{p["p"]}" stroke-width="2"/>'
        + f'<rect x="366" y="326" width="68" height="16" rx="3" fill="{p["s"]}" '
        f'stroke="{p["p"]}" stroke-width="1.4"/>'
        + f'<polygon points="400,170 452,240 400,310 348,240" fill="{p["s"]}" '
        f'stroke="{p["p"]}" stroke-width="2.4" filter="url(#glowF)"/>'
        + f'<polygon points="400,170 452,240 400,240" fill="{p["p"]}" '
        f'opacity="0.6"/>'
        + f'<polygon points="348,240 400,240 400,310" fill="{p["p"]}" '
        f'opacity="0.6"/>'
        + f'<line x1="400" y1="170" x2="400" y2="310" stroke="{p["hi"]}" '
        f'stroke-width="1.2" opacity="0.8"/>'
        + f'<circle cx="400" cy="240" r="10" fill="{p["hi"]}" '
        f'filter="url(#bloomF)"/>'
        + guilloche(400, 240, [78, 92], p["p"], 0.5) + _floor(p, 482))


# -------------------------------------------------------------- scene: clash --
def sc_clash(p, rng):
    burst = "".join(
        f'<line x1="400" y1="290" x2="{400 + dx}" y2="{290 + dy}" '
        f'stroke="{p["hi"] if i % 3 == 0 else p["p"]}" stroke-width="2.6" '
        f'opacity="0.85"/>' for i, (dx, dy) in enumerate(
            [(150, -90), (-150, -80), (170, 30), (-170, 40), (90, -140),
             (-90, -140), (120, 120), (-120, 120)]))
    return (
        _hall(p, arch_w=680) + _halo(400, 290, 200, p, 0.55) + burst
        + _operative(268, 452, 120, p, False)
        + f'<polygon points="532,290 580,400 484,400" fill="#160709" '
        f'stroke="{p["p"]}" stroke-width="2.4"/>'
        + f'<circle cx="532" cy="348" r="14" fill="{p["p"]}" '
        f'filter="url(#bloomF)"/>'
        + f'<line x1="330" y1="330" x2="480" y2="330" stroke="{p["hi"]}" '
        f'stroke-width="3" filter="url(#glowF)"/>'
        + f'<circle cx="404" cy="330" r="18" fill="none" stroke="{p["hi"]}" '
        f'stroke-width="2"/>'
        + mist_band(150, 430, 500, 36, p["mist"], 0.13) + _floor(p, 482))


# ------------------------------------------------------------ scene: rotunda --
def sc_rotunda(p, rng):
    cols = "".join(
        f'<rect x="{x}" y="150" width="30" height="300" fill="url(#ironG)" '
        f'stroke="{p["p"]}" stroke-width="1.2"/>'
        f'<rect x="{x - 5}" y="140" width="40" height="12" fill="{p["s"]}" '
        f'stroke="{p["p"]}" stroke-width="1"/>'
        f'<rect x="{x - 5}" y="448" width="40" height="12" fill="{p["s"]}" '
        f'stroke="{p["p"]}" stroke-width="1"/>' for x in (170, 600))
    return (
        _hall(p, arch_w=700) + cols + _halo(400, 290, 180, p, 0.45)
        + f'<ellipse cx="400" cy="430" rx="150" ry="26" fill="#02040a"/>'
        + f'<polygon points="400,330 460,400 340,400" fill="url(#ironG)" '
        f'stroke="{p["p"]}" stroke-width="2"/>'
        + f'<circle cx="400" cy="300" r="56" fill="#0a1020" stroke="{p["p"]}" '
        f'stroke-width="2.6"/>'
        + f'<circle cx="400" cy="300" r="34" fill="{p["p"]}" opacity="0.8" '
        f'filter="url(#glowF)"/>'
        + f'<circle cx="400" cy="300" r="13" fill="{p["hi"]}"/>'
        + guilloche(400, 300, [74, 90], p["p"], 0.5)
        + light_rays(400, 300, p["p"], [(270, 12)], 340, op=0.07)
        + _floor(p, 482))


SCENES = [
    (("debt-eater", "eater"), sc_specter),
    (("crucible", "forge"), sc_furnace),
    (("compass", "sonar"), sc_astrolabe),
    (("debt-scale", "scale-bearer"), sc_scale),
    (("clash", "multi-angle", "suppression-combat"), sc_clash),
    (("squad", "cadre", "specialist", "personnel", "clerk", "roster",
      "muster", "deployment", "upgraded", "emerging-tempered"), sc_squad),
    (("ordeal", "monolith", "midnight", "tide-watch", "incursion", "violet",
      "sovereign"), sc_monolith),
    (("train", "caravan", "horizon"), sc_train),
    (("weeping", "subterranean-current", "river"), sc_river),
    (("vault", "sealed", "archive", "ledger", "sanctuary", "municipal",
      "memorial", "codex", "catalog", "bulletin", "tale", "tomes"), sc_archive),
    (("loom", "weaving", "armament", "showcase", "weapon-display",
      "fabrication"), sc_loom),
    (("breach", "rift"), sc_rift),
    (("secc", "syntax", "schematic", "diagram", "tech-trees", "tier",
      "progression", "registry", "origins"), sc_chart_table),
    (("gauge", "hitbox", "tactical", "roulette", "console", "hud",
      "protocol", "hologram", "observation", "research", "visualizer",
      "calculator", "calculation"), sc_instruments),
    (("cell", "containment-unit", "containment-chamber", "containment-door",
      "sorrow-entity", "overloaded", "alarm"), sc_cell_door),
    (("choir", "mellda", "manifestation", "bell"), sc_choir),
    (("hourglass", "cracked"), sc_hourglass),
    (("mirror", "pool"), sc_mirror),
    (("well", "mnemonic", "generator", "extraction", "harvesting", "conduit",
      "battery", "energy-box", "storage"), sc_tanks),
    (("gate", "realization"), sc_gate),
    (("fear", "panic", "elements", "pressure", "aura", "inversion",
      "risk-levels", "entity-types", "entity-risk"), sc_totems),
    (("mission", "briefing", "dispatch", "menu", "evaluation", "report",
      "dossier", "cognition", "filter", "linter", "style-guide",
      "dream-born", "mugenhan-lattice"), sc_war_table),
    (("dream", "abstraction", "veiled", "mellda"), sc_ribbons),
    (("equippable", "interaction", "tool-relic", "relic-in-corridor",
      "gift-manifestation"), sc_relic_pedestal),
    (("elevator", "kiting", "maneuver", "shaft-network"), sc_gate),
]


def gallery_scene(slug, p, rng):
    s = slug.lower()
    for keys, fn in SCENES:
        if any(k in s for k in keys):
            return fn(p, rng)
    return sc_rotunda(p, rng)


def build_gallery(slug, title, p):
    rng = rng_for(slug, "gallery")
    stars = starfield(rng, 800, 600, 60, top_frac=0.55)
    motes = embers(rng, 800, 600, 20, p["mist"], y0=0.2, y1=0.85)
    label = esc(title.upper())
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" '
        f'width="800" height="600">{defs_block(p)}'
        f'<rect width="800" height="600" fill="url(#skyG)"/>{stars}'
        f"{gallery_scene(slug, p, rng)}{motes}"
        f'<rect x="14" y="14" width="772" height="572" fill="none" '
        f'stroke="url(#giltG)" stroke-width="3"/>'
        f'<rect x="22" y="22" width="756" height="556" fill="none" '
        f'stroke="{IRON_SOFT}" stroke-width="1"/>'
        f'<rect x="30" y="30" width="740" height="540" fill="none" '
        f'stroke="{p["p"]}" stroke-width="1" opacity="0.55"/>'
        f"{corner_ornament(14, 14, 1, 1, GILT, 1.2)}"
        f"{corner_ornament(786, 14, -1, 1, GILT, 1.2)}"
        f"{corner_ornament(14, 586, 1, -1, GILT, 1.2)}"
        f"{corner_ornament(786, 586, -1, -1, GILT, 1.2)}"
        f"{rivet_row(60, 14, 740, 14, 16)}{rivet_row(60, 586, 740, 586, 16)}"
        f"{rivet_row(14, 60, 14, 540, 11)}{rivet_row(786, 60, 786, 540, 11)}"
        f'<rect x="170" y="512" width="460" height="50" rx="6" fill="#04060b" '
        f'opacity="0.92" stroke="url(#giltG)" stroke-width="1.8"/>'
        f'<text x="400" y="532" text-anchor="middle" font-family="{SERIF}" '
        f'font-size="13.5" font-weight="bold" fill="{BONE}" letter-spacing="1">'
        f"{label}</text>"
        f'<text x="400" y="550" text-anchor="middle" font-family="{SANS}" '
        f'font-size="9" fill="{p["p"]}" letter-spacing="2">ARCHIVAL '
        f"EXHIBITION PLATE &#9670; FACILITY 01</text>"
        f"{vignette_rect(800, 600)}{grain_rect(800, 600)}</svg>")


# ================================================================== main ===
def main():
    counts = {"ICON": 0, "BANNER": 0, "MAP": 0, "GALLERY": 0}
    errors = []
    for svg_file in sorted(IMG_DIR.glob("*.svg")):
        if svg_file.name in PRESERVE:
            continue
        slug = svg_file.stem
        title = slug.replace("-", " ").title()
        p = pal_for(slug)
        arch = classify_file(slug)
        if arch == "ICON":
            content = build_icon(slug, title, p)
        elif arch == "BANNER":
            content = build_banner(slug, title, p)
        elif arch == "MAP":
            content = build_map(slug, title, p)
        else:
            content = build_gallery(slug, title, p)
        try:
            ET.fromstring(content)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{svg_file.name}: {exc}")
            continue
        svg_file.write_text(content, encoding="utf-8")
        counts[arch] += 1
    print(f"ICON={counts['ICON']} BANNER={counts['BANNER']} "
          f"MAP={counts['MAP']} GALLERY={counts['GALLERY']} "
          f"TOTAL={sum(counts.values())}")
    if errors:
        print("ERRORS:")
        for err in errors:
            print(f"  {err}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()

