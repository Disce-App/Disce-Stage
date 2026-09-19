#!/usr/bin/env python3
"""Generate the DISCE halftone-dot pattern family.

The brand already carries a halftone dot texture (``images/halftone-*.png``):
a square lattice of ``--green`` circles whose radius ramps across the field.
This script generalises that single asset into a small, named vocabulary in
which every pattern is the **same dot primitive** (a lattice of circles) driven
by a different scalar/vector field. The result is one coherent family rather
than a pile of unrelated textures.

Motifs
------
  bloom    radial ramp from an anchor corner/point        (today's asset)
  current  dot centres pushed along a smooth vector field  (organic flow)
  arena    concentric rings, radius modulated by distance   (ripples)
  depth    two overlaid fields in two colours               (front/back)
  wave     radius follows a diagonal sine                    (dunes)
  terrain  radius encodes an elevation silhouette            (skyline)
  trail    dots sampled along cubic bezier paths             (constellation)
  moire    two rotated lattices interfering                  (print plaid)
  seam     blooms across the middle, dissolves at both edges (divider)

Output is a single-colour (or two-colour for ``depth``) **palette PNG with a
transparent background**, so it can be dropped over the paper grain, a
cream-dim band, or a dark surface with no baked-in paper tone. Dots are
hard-edged on purpose: the halftone is a print texture, not an anti-aliased
illustration.

Determinism
-----------
All motifs are analytic and the only randomness (``trail``'s faint field,
optional jitter) comes from ``--seed``. The same arguments reproduce the same
bytes.

Dependencies
------------
Pillow only, and only as an out-of-tree dev dependency (same convention as
``scripts/optimize_images.py``):
    PYTHONPATH=/tmp/pylibs python3 scripts/generate_dot_patterns.py ...

Examples
--------
    # the four shortlisted field motifs, transparent, token colours
    python3 scripts/generate_dot_patterns.py --motif bloom   --out images/derived --name dot-bloom-green
    python3 scripts/generate_dot_patterns.py --motif current --out images/derived --name dot-current-green
    python3 scripts/generate_dot_patterns.py --motif arena   --out images/derived --name dot-arena-green
    python3 scripts/generate_dot_patterns.py --motif depth   --out images/derived --name dot-depth-green

    # an ochre variant for dark surfaces (brief §5: no bright green on dark)
    python3 scripts/generate_dot_patterns.py --motif current --color E3AF50 --out images/derived --name dot-current-ochre

The output directory is created if needed. The script never touches existing
masters under ``images/``; it only writes the file you name.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys

try:
    from PIL import Image, ImageDraw
except ImportError:  # pragma: no cover
    sys.exit("Missing dependency: Pillow (dev-only, keep it outside the tree).")

# Token defaults (DESIGN-BRIEF §5).
GREEN = "4FAC4E"
GREEN_DARK = "357435"
GREEN_SAGE = "77816A"
OCHRE = "E3AF50"
PARCHMENT = "D5C09D"

MOTIFS = ("bloom", "current", "arena", "depth", "wave", "terrain", "trail", "moire", "seam")


def hex_rgb(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    if len(value) != 6:
        raise SystemExit(f"colour must be a 6-digit hex, got {value!r}")
    return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


def _smooth(x: float) -> float:
    """0..1 smoothstep from a raw sine in -1..1 (keeps dots off the extremes)."""
    return 0.5 + 0.5 * x


def draw_motif(im: Image.Image, motif: str, p: dict, idx: dict) -> None:
    """Draw one motif onto the palette image ``im`` (index 0 = transparent)."""
    d = ImageDraw.Draw(im)
    w, h = im.size
    pitch = p["pitch"]
    r0 = p["radius"]
    mn = p["min_radius"]

    step = max(1, int(round(pitch)))

    def grid():
        for y in range(int(pitch * 0.5), h, step):
            for x in range(int(pitch * 0.5), w, step):
                yield x, y

    def disc(x, y, r, index):
        if r > 0.25:
            d.ellipse((x - r, y - r, x + r, y + r), fill=index)

    def coord(value, extent):
        """Fraction of the extent when |value| <= 1, else an absolute pixel."""
        return value * extent if abs(value) <= 1 else value

    if motif == "bloom":
        ax, ay = p.get("anchor", [0.0, 0.0])
        ax, ay = coord(ax, w), coord(ay, h)
        reach = p.get("reach", max(w, h) * 0.9)
        for x, y in grid():
            r = r0 * max(mn, 1.0 - math.hypot(x - ax, y - ay) / reach)
            disc(x, y, r, idx["primary"])

    elif motif == "current":
        amp = p.get("amp", 7.0)
        for x, y in grid():
            a = math.sin(x / 190.0 + y / 260.0) * math.pi + math.cos(x / 330.0 - y / 170.0) * math.pi
            r = r0 * (mn + (1 - mn) * _smooth(math.sin(x / 130.0 - y / 110.0)))
            disc(x + math.cos(a) * amp, y + math.sin(a) * amp, r, idx["primary"])

    elif motif == "arena":
        cx, cy = p.get("center", [0.5, 0.5])
        cx, cy = coord(cx, w), coord(cy, h)
        ring = p.get("ring", 26.0)
        reach = p.get("reach", min(w, h) * 0.56)
        for x, y in grid():
            dist = math.hypot(x - cx, y - cy)
            if dist > reach:
                continue
            r = r0 * (mn + (1 - mn) * _smooth(math.sin(dist / ring))) * (1 - dist / (reach * 1.1))
            disc(x, y, r, idx["primary"])

    elif motif == "depth":
        for x, y in grid():
            r = r0 * (mn + (1 - mn) * _smooth(math.sin(x / 180.0 + y / 120.0)))
            disc(x, y, r, idx["secondary"])
        for x, y in grid():
            r = r0 * (mn + (1 - mn) * _smooth(math.sin(x / 300.0 - y / 220.0 + 0.8)))
            disc(x, y, r, idx["primary"])

    elif motif == "wave":
        kx, ky = p.get("wavelength", [210.0, 150.0])
        for x, y in grid():
            r = r0 * (mn + (1 - mn) * _smooth(math.sin(2 * math.pi * (x / kx - y / ky))))
            disc(x, y, r, idx["primary"])

    elif motif == "terrain":
        for x, y in grid():
            e = (0.52 + 0.26 * math.sin(x / 300.0) + 0.12 * math.sin(x / 95.0 + 1.4)
                 + 0.08 * math.sin(x / 41.0)) * h - (h - y)
            disc(x, y, r0 * min(1.0, max(mn, e / 120.0)), idx["primary"])

    elif motif == "trail":
        for x, y in grid():
            disc(x, y, r0 * 0.16, idx["secondary"])
        for k, (p0, p1, p2, p3) in enumerate([
            ((0, h * 0.78), (w * 0.3, h * 0.1), (w * 0.62, h * 0.95), (w, h * 0.28)),
            ((0, h * 0.5), (w * 0.35, h * 0.9), (w * 0.7, h * 0.06), (w, h * 0.6)),
        ]):
            for i in range(260):
                t = i / 259.0
                mt = 1 - t
                x = mt**3 * p0[0] + 3 * mt * mt * t * p1[0] + 3 * mt * t * t * p2[0] + t**3 * p3[0]
                y = mt**3 * p0[1] + 3 * mt * mt * t * p1[1] + 3 * mt * t * t * p2[1] + t**3 * p3[1]
                r = 1.0 + r0 * 0.8 * math.sin(math.pi * t) * (0.6 + 0.4 * k)
                disc(x, y, r, idx["primary"])

    elif motif == "moire":
        base = Image.new("P", (w, h), 0)
        bd = ImageDraw.Draw(base)
        for x, y in grid():
            bd.ellipse((x - 4.4, y - 4.4, x + 4.4, y + 4.4), fill=1)
        rotated = base.rotate(6, center=(w / 2, h / 2), resample=Image.BICUBIC, expand=False)
        for y in range(h):
            for x in range(w):
                if rotated.getpixel((x, y)) == 1 and im.getpixel((x, y)) == 0:
                    im.putpixel((x, y), idx["primary"])

    elif motif == "seam":
        for x, y in grid():
            r = r0 * (mn + (1 - mn) * math.sin(math.pi * x / w))
            disc(x, y, r, idx["primary"])

    else:  # pragma: no cover
        raise SystemExit(f"unknown motif {motif!r}; choose from {', '.join(MOTIFS)}")


def build(args) -> str:
    p = {
        "pitch": args.pitch,
        "radius": args.radius,
        "min_radius": args.min_radius,
    }
    if args.params:
        try:
            p.update(json.loads(args.params))
        except json.JSONDecodeError as exc:
            raise SystemExit(f"--params must be JSON: {exc}") from exc

    primary = hex_rgb(args.color)
    secondary = hex_rgb(args.color2)

    # Palette: 0 transparent, 1 primary, 2 secondary.
    pal = bytearray(768)
    for i, rgb in ((1, primary), (2, secondary)):
        pal[i * 3 : i * 3 + 3] = bytes(rgb)

    im = Image.new("P", (args.width, args.height), 0)
    im.putpalette(bytes(pal))
    draw_motif(im, args.motif, p, {"primary": 1, "secondary": 2})
    im.info["transparency"] = 0  # only index 0 is transparent

    os.makedirs(args.out, exist_ok=True)
    stem = args.name or f"dot-{args.motif}-{args.color.lstrip('#')}"
    path = os.path.join(args.out, f"{stem}.png")
    im.save(path, optimize=True)
    return path


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--motif", choices=MOTIFS)
    ap.add_argument("--width", type=int, default=1200)
    ap.add_argument("--height", type=int, default=420)
    ap.add_argument("--pitch", type=float, default=17.0, help="lattice pitch in px")
    ap.add_argument("--radius", type=float, default=6.0, help="base dot radius r0")
    ap.add_argument("--min-radius", type=float, default=0.05, help="smallest radius as a fraction of r0")
    ap.add_argument("--color", default=GREEN, help="primary dot colour (hex, default --green)")
    ap.add_argument("--color2", default=GREEN_SAGE, help="secondary colour for depth/trail (hex)")
    ap.add_argument("--seed", type=int, default=20260919)
    ap.add_argument("--params", default="", help="motif-specific JSON, e.g. '{\"reach\":760,\"anchor\":[120,60]}'")
    ap.add_argument("--out", default="images/derived")
    ap.add_argument("--name", default="", help="output stem without extension")
    ap.add_argument("--list-motifs", action="store_true")
    args = ap.parse_args(argv)

    if args.list_motifs:
        print("\n".join(MOTIFS))
        return 0
    if not args.motif:
        ap.error("--motif is required (or use --list-motifs)")

    path = build(args)
    print(json.dumps({
        "motif": args.motif,
        "file": path,
        "bytes": os.path.getsize(path),
        "width": args.width,
        "height": args.height,
        "color": args.color,
        "color2": args.color2,
        "seed": args.seed,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
