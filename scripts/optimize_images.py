#!/usr/bin/env python3
"""Image optimization pipeline for Disce Stage (DESIGN-BRIEF.md Section 9).

Reads a master image from ``images/`` (masters are never modified) and writes
AVIF (primary) + WebP (fallback) derivatives into ``images/derived/`` at a set
of target widths, capped by the master's real pixel width so nothing is ever
upscaled. It also emits a <= 1 KB WebP LQIP (about 24 px wide) and
a JSON manifest on stdout.

Runtime dependencies (NOT vendored into the repo; install outside the tree):

    Python 3.10+
    Pillow              >= 11
    pillow-avif-plugin  (AVIF encoder; import name ``pillow_avif``)

Example setup:

    python3 -m pip install --target /tmp/pylibs Pillow pillow-avif-plugin
    PYTHONPATH=/tmp/pylibs python3 scripts/optimize_images.py \\
        images/DISCE_B04_r4_causeway-palms.png --kind hero

Optional cropping (masters are never modified): ``--crop-inset 4`` removes a
symmetric 4% paper-mat border, ``--crop-box 73,41,1256,942`` takes an explicit
region, and ``--no-native`` skips the appended master width for oversized
sources. Crops are applied before resizing, so derivatives inherit the crop.

Alpha derivatives (for CSS masks etc.): ``--keep-alpha`` preserves the alpha
channel instead of flattening over the paper background, ``--formats webp``
restricts output to one format, and ``--suffix=-mask`` disambiguates the stem
(e.g. ``dach-map-mask-1600.webp``).

Budgets (Section 9): hero-class <= 250 KB AVIF at the largest width,
card-class <= 120 KB. Quality starts at ~q50 and is stepped down until the
largest AVIF meets the budget (or the floor is reached).
"""

import argparse
import base64
import io
import json
import math
import os
import sys

try:
    from PIL import Image, ImageFilter
except ImportError:  # pragma: no cover
    sys.exit("Missing dependency: Pillow. See the module docstring for setup.")

try:
    import pillow_avif  # noqa: F401  (registers the AVIF encoder with Pillow)
except ImportError:  # pragma: no cover
    sys.exit("Missing dependency: pillow-avif-plugin. See the module docstring for setup.")

# Section 9 target widths; filtered down to the master width (no upscaling).
DEFAULT_WIDTHS = (768, 1280, 1920, 2560)
BUDGETS = {"hero": 250 * 1024, "card": 120 * 1024}
AVIF_QUALITY_START = 50
AVIF_QUALITY_FLOOR = 20
AVIF_QUALITY_STEP = 5
AVIF_SPEED = 6
WEBP_QUALITY = 72
LQIP_WIDTH = 24
LQIP_MAX_BYTES = 1024


def flatten_alpha(image, background):
    """Composite a transparent master over ``background`` (an ``(r, g, b)``
    tuple). AVIF/WebP here are encoded as RGB, so without this a PNG with an
    alpha channel (e.g. the line-art ``dach-map.png``) would flatten to black.
    """
    if image.mode in ("RGBA", "LA") or (image.mode == "P" and "transparency" in image.info):
        rgba = image.convert("RGBA")
        bg = Image.new("RGB", rgba.size, background)
        bg.paste(rgba, mask=rgba.split()[-1])
        return bg
    return image


def target_widths(master_width, requested, append_native=True, allow_upscale=False):
    """Resolve the output widths. By default nothing is ever upscaled past the
    master width (DESIGN-BRIEF §9); ``allow_upscale`` is an explicit opt-in for
    the rare approved case (e.g. a blurred ambient layer where softness is
    acceptable), and then the master width is still appended if not present.
    """
    limit = float("inf") if allow_upscale else master_width
    widths = sorted({int(w) for w in requested if 0 < int(w) <= limit})
    if append_native and master_width not in widths:
        widths.append(master_width)
        widths.sort()
    if not widths:
        widths = [master_width]
    return widths


def apply_crop(image, crop_inset, crop_box):
    """Return a cropped copy of ``image`` (masters stay untouched on disk).

    ``crop_inset`` removes a symmetric percentage border (e.g. the printed
    paper mat around the C04/B03/A08/B01 masters); ``crop_box`` is an explicit
    ``(left, top, width, height)`` region in master pixels. ``crop_box`` wins
    if both are supplied.
    """
    if crop_box:
        left, top, width, height = crop_box
        return image.crop((left, top, left + width, top + height))
    if crop_inset:
        master_w, master_h = image.size
        dx = round(master_w * crop_inset / 100)
        dy = round(master_h * crop_inset / 100)
        return image.crop((dx, dy, master_w - dx, master_h - dy))
    return image


def scaled_height(width, master_w, master_h):
    return max(1, round(master_h * width / master_w))


def encode_avif(image, quality):
    buf = io.BytesIO()
    image.save(buf, "AVIF", quality=quality, speed=AVIF_SPEED)
    return buf.getvalue()


def encode_webp(image, quality=WEBP_QUALITY):
    buf = io.BytesIO()
    image.save(buf, "WEBP", quality=quality, method=6)
    return buf.getvalue()


def make_lqip(image):
    width = min(LQIP_WIDTH, image.width)
    height = max(1, round(image.height * width / image.width))
    small = image.resize((width, height), Image.LANCZOS)
    for quality in (40, 30, 20, 10):
        data = encode_webp(small, quality)
        if len(data) <= LQIP_MAX_BYTES:
            return small, data, quality
    return small, data, quality


def optimize(master, kind, out_dir, requested_widths, crop_inset=None, crop_box=None,
             append_native=True, background=(251, 248, 239), keep_alpha=False,
             formats=("avif", "webp"), suffix="", allow_upscale=False):
    image = Image.open(master)
    image.load()
    image = apply_crop(image, crop_inset, crop_box)
    if not keep_alpha:
        image = flatten_alpha(image, background)
        rgb = image.convert("RGB")
    else:
        # Preserve the alpha channel so the derivative can be used as a CSS
        # mask (e.g. the DACH map watermark). Still normalise to RGBA.
        rgb = image.convert("RGBA") if image.mode != "RGBA" else image
    master_w, master_h = rgb.size

    widths = target_widths(master_w, requested_widths, append_native, allow_upscale)
    largest = widths[-1]

    # Pick the highest AVIF quality whose largest-width output meets budget.
    quality = AVIF_QUALITY_START
    avif_sizes = {}
    if "avif" in formats:
        while True:
            for width in widths:
                height = scaled_height(width, master_w, master_h)
                resized = rgb.resize((width, height), Image.LANCZOS)
                avif_sizes[width] = encode_avif(resized, quality) if width == largest else None
            if len(avif_sizes[largest]) <= BUDGETS[kind] or quality <= AVIF_QUALITY_FLOOR:
                break
            quality -= AVIF_QUALITY_STEP

    os.makedirs(out_dir, exist_ok=True)
    stem = os.path.splitext(os.path.basename(master))[0] + suffix
    derivatives = []

    for width in widths:
        height = scaled_height(width, master_w, master_h)
        resized = rgb.resize((width, height), Image.LANCZOS)
        if "avif" in formats:
            avif_data = encode_avif(resized, quality)
            avif_path = os.path.join(out_dir, f"{stem}-{width}.avif")
            with open(avif_path, "wb") as fh:
                fh.write(avif_data)
            derivatives.append({"format": "avif", "width": width, "height": height,
                                "file": avif_path, "bytes": len(avif_data)})
        if "webp" in formats:
            webp_data = encode_webp(resized)
            webp_path = os.path.join(out_dir, f"{stem}-{width}.webp")
            with open(webp_path, "wb") as fh:
                fh.write(webp_data)
            derivatives.append({"format": "webp", "width": width, "height": height,
                                "file": webp_path, "bytes": len(webp_data)})

    lqip_img, lqip_data, lqip_quality = make_lqip(rgb)
    lqip_path = os.path.join(out_dir, f"{stem}-lqip.webp")
    with open(lqip_path, "wb") as fh:
        fh.write(lqip_data)
    lqip = {
        "file": lqip_path,
        "width": lqip_img.width,
        "height": lqip_img.height,
        "bytes": len(lqip_data),
        "quality": lqip_quality,
        "data_uri": "data:image/webp;base64," + base64.b64encode(lqip_data).decode("ascii"),
    }

    largest_avif = next((d for d in derivatives if d["format"] == "avif" and d["width"] == largest), None)
    return {
        "master": master,
        "kind": kind,
        "suffix": suffix,
        "alpha": keep_alpha,
        "crop": {"inset_percent": crop_inset, "box": list(crop_box) if crop_box else None},
        "master_width": master_w,
        "master_height": master_h,
        "max_width": largest,
        "upscaled": False,
        "budget_bytes": BUDGETS[kind],
        "budget_ok": (largest_avif["bytes"] <= BUDGETS[kind]) if largest_avif else None,
        "quality": {"avif": quality if "avif" in formats else None, "webp": WEBP_QUALITY},
        "lqip": lqip,
        "derivatives": derivatives,
    }


def _mat_mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def _mat_lerp(a, b, t):
    return [[a[i][j] + (b[i][j] - a[i][j]) * t for j in range(3)] for i in range(3)]


def _identity3():
    return [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]


def css_filter_matrix(grayscale=0.0, sepia=0.0, hue_rotate=0.0, saturate=1.0):
    """Build the 3x3 matrix for the CSS filter chain used by the kernel ghost
    (``grayscale(0.7) sepia(0.42) hue-rotate(42deg) saturate(0.9)``). The CSS
    Filter Effects matrices operate on non-linear sRGB, which is exactly what
    Pillow's ``Image.convert`` matrix does, so the baked result matches the
    live CSS it replaces.
    """
    m = _identity3()
    if grayscale:
        luma = 0.2126, 0.7152, 0.0722
        m = _mat_mul(_mat_lerp(_identity3(), [list(luma)] * 3, grayscale), m)
    if sepia:
        sep = [[0.393, 0.769, 0.189], [0.349, 0.686, 0.168], [0.272, 0.534, 0.131]]
        m = _mat_mul(_mat_lerp(_identity3(), sep, sepia), m)
    if hue_rotate:
        a = math.radians(hue_rotate)
        c, s = math.cos(a), math.sin(a)
        m = _mat_mul([
            [0.213 + c * 0.787 - s * 0.213, 0.715 - c * 0.715 - s * 0.715, 0.072 - c * 0.072 + s * 0.928],
            [0.213 - c * 0.213 + s * 0.143, 0.715 + c * 0.285 + s * 0.140, 0.072 - c * 0.072 - s * 0.283],
            [0.213 - c * 0.213 - s * 0.787, 0.715 - c * 0.715 + s * 0.715, 0.072 + c * 0.928 + s * 0.072],
        ], m)
    if saturate != 1.0:
        t = saturate
        m = _mat_mul([
            [0.213 + 0.787 * t, 0.715 - 0.715 * t, 0.072 - 0.072 * t],
            [0.213 - 0.213 * t, 0.715 + 0.285 * t, 0.072 - 0.072 * t],
            [0.213 - 0.213 * t, 0.715 - 0.715 * t, 0.072 + 0.928 * t],
        ], m)
    return m


def radial_mask(size, cx, cy, rx, ry, solid, fade):
    """Soft-edge alpha mask (L) with a solid core up to ``solid`` of the
    normalised radius and a linear falloff to transparent at ``fade``. Computed
    small and upscaled - it is a blur, so the interpolation is free quality.
    """
    width, height = size
    sw, sh = 64, max(8, round(64 * height / width))
    small = Image.new("L", (sw, sh))
    px = small.load()
    for j in range(sh):
        dy = ((j + 0.5) * height / sh - cy) / ry
        for i in range(sw):
            dx = ((i + 0.5) * width / sw - cx) / rx
            d = math.hypot(dx, dy)
            if d <= solid:
                v = 1.0
            elif d >= fade:
                v = 0.0
            else:
                v = (fade - d) / (fade - solid)
            px[i, j] = int(round(v * 255))
    return small.resize((width, height), Image.BILINEAR)


def bake_ghost(master, out_dir, widths, opacity, paper, anchor, ratio,
               grayscale=0.7, sepia=0.42, hue_rotate=42.0, saturate=0.9,
               blur=0.6, scale=1.0, mask_rx=0.5, mask_ry=0.94,
               suffix="-ghost-baked", formats=("avif", "webp"),
               avif_quality=AVIF_QUALITY_START):
    """Bake the ambient ghost into flat files: grade + opacity + soft edges +
    presence anchor, composited over the section paper tone. The page then
    renders one plain, unfiltered, unmasked background layer at opacity 1, so
    there is no live filter/mask/compositing cost. One file per serving width.
    """
    image = Image.open(master)
    image.load()
    rgb = flatten_alpha(image, paper).convert("RGB")
    matrix = css_filter_matrix(grayscale, sepia, hue_rotate, saturate)
    # Pillow's 12-tuple matrix is 3 rows of (r, g, b, offset); our filters have
    # no offsets, so each row gets a trailing 0.
    flat = [v for row in matrix for v in (list(row) + [0.0])]
    graded = rgb.convert("RGB", tuple(flat))

    os.makedirs(out_dir, exist_ok=True)
    stem = os.path.splitext(os.path.basename(master))[0] + suffix
    a = anchor / 100.0  # CLI anchor is a percentage
    derivatives = []
    for width in widths:
        height = max(1, round(width * ratio))
        tower_h = max(1, round(height * scale))
        scaled_w = max(1, round(graded.width * tower_h / graded.height))
        tower = graded.resize((scaled_w, tower_h), Image.LANCZOS)
        if blur:
            tower = tower.filter(ImageFilter.GaussianBlur(blur))
        canvas = Image.new("RGB", (width, height), paper)
        x_off = int(round(a * width - scaled_w / 2))
        y_off = int(round((height - tower_h) / 2))
        # Lay the (wider) tower onto a canvas-sized paper sheet, then composite
        # that sheet over the flat paper using the soft-edge alpha.
        layer = Image.new("RGB", (width, height), paper)
        layer.paste(tower, (x_off, y_off))
        mask = radial_mask((width, height), cx=a * width, cy=0.5 * height,
                           rx=mask_rx * width, ry=mask_ry * height, solid=0.28, fade=0.82)
        alpha = mask.point(lambda v: int(round(v * opacity)))
        canvas.paste(layer, (0, 0), alpha)

        if "avif" in formats:
            data = encode_avif(canvas, avif_quality)
            path = os.path.join(out_dir, f"{stem}-{width}.avif")
            with open(path, "wb") as fh:
                fh.write(data)
            derivatives.append({"format": "avif", "width": width, "height": height,
                                "file": path, "bytes": len(data)})
        if "webp" in formats:
            data = encode_webp(canvas)
            path = os.path.join(out_dir, f"{stem}-{width}.webp")
            with open(path, "wb") as fh:
                fh.write(data)
            derivatives.append({"format": "webp", "width": width, "height": height,
                                "file": path, "bytes": len(data)})

    return {
        "mode": "bake-ghost",
        "master": master,
        "opacity": opacity,
        "paper": "#%02X%02X%02X" % paper,
        "anchor": anchor,
        "ratio": ratio,
        "grade": {"grayscale": grayscale, "sepia": sepia,
                  "hue_rotate": hue_rotate, "saturate": saturate, "blur": blur},
        "derivatives": derivatives,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description="Disce Stage image optimizer (Section 9).")
    parser.add_argument("master", help="path to a master image under images/")
    parser.add_argument("--kind", choices=sorted(BUDGETS), default="hero",
                        help="asset class controlling the AVIF budget (default: hero)")
    parser.add_argument("--out", default="images/derived", help="output directory")
    parser.add_argument("--widths", default=",".join(str(w) for w in DEFAULT_WIDTHS),
                        help="comma-separated target widths; capped by the master width")
    parser.add_argument("--crop-inset", type=float, default=None,
                        help="symmetric inset crop, percent of each edge (paper mat removal)")
    parser.add_argument("--crop-box", default=None,
                        help="explicit 'left,top,width,height' crop in master pixels")
    parser.add_argument("--no-native", action="store_true",
                        help="do not append the master width (useful for oversized sources)")
    parser.add_argument("--allow-upscale", action="store_true",
                        help="allow output widths above the master width (explicit, "
                             "approved opt-in; default is never upscale)")
    parser.add_argument("--keep-alpha", action="store_true",
                        help="preserve the alpha channel instead of flattening "
                             "(for mask/drop-shadow derivatives)")
    parser.add_argument("--formats", default="avif,webp",
                        help="comma-separated output formats (default: avif,webp)")
    parser.add_argument("--suffix", default="",
                        help="string appended to the output stem, e.g. '-mask'")
    parser.add_argument("--background", default="#FBF8EF",
                        help="hex colour to flatten image transparency over (default: site paper)")
    parser.add_argument("--bake-ghost", action="store_true",
                        help="bake mode: flatten grade + opacity + soft edges + anchor "
                             "into one composited file per width (no LQIP)")
    parser.add_argument("--bake-opacity", type=float, default=0.06,
                        help="ghost opacity baked into the file (bake mode)")
    parser.add_argument("--bake-anchor", type=float, default=80.0,
                        help="horizontal presence anchor, percent (bake mode)")
    parser.add_argument("--bake-ratio", type=float, default=2.63,
                        help="canvas height/width ratio (bake mode)")
    parser.add_argument("--bake-blur", type=float, default=0.6,
                        help="Gaussian blur radius baked in (bake mode)")
    parser.add_argument("--bake-scale", type=float, default=1.0,
                        help="tower height as a fraction of the canvas (bake mode)")
    parser.add_argument("--bake-mask-rx", type=float, default=0.5,
                        help="soft-edge mask x radius, fraction of width (bake mode)")
    parser.add_argument("--bake-mask-ry", type=float, default=0.94,
                        help="soft-edge mask y radius, fraction of height (bake mode)")
    args = parser.parse_args(argv)

    requested = [w for w in args.widths.split(",") if w.strip()]
    crop_box = None
    if args.crop_box:
        try:
            crop_box = tuple(int(v) for v in args.crop_box.split(","))
        except ValueError:
            sys.exit("--crop-box must be 'left,top,width,height' in integers")
        if len(crop_box) != 4:
            sys.exit("--crop-box must be 'left,top,width,height' in integers")
    bg = args.background.lstrip("#")
    if len(bg) != 6:
        sys.exit("--background must be a 6-digit hex colour, e.g. #FBF8EF")
    background = tuple(int(bg[i:i + 2], 16) for i in (0, 2, 4))
    formats = tuple(f.strip() for f in args.formats.split(",") if f.strip())
    for fmt in formats:
        if fmt not in ("avif", "webp"):
            sys.exit(f"unsupported format: {fmt}")
    if args.bake_ghost:
        manifest = bake_ghost(
            args.master, args.out, [int(w) for w in requested],
            opacity=args.bake_opacity, paper=background, anchor=args.bake_anchor,
            ratio=args.bake_ratio, blur=args.bake_blur, scale=args.bake_scale,
            mask_rx=args.bake_mask_rx, mask_ry=args.bake_mask_ry,
            suffix=args.suffix or "-ghost-baked", formats=formats)
        print(json.dumps(manifest, indent=2))
        return 0

    manifest = optimize(args.master, args.kind, args.out, requested,
                        crop_inset=args.crop_inset, crop_box=crop_box,
                        append_native=not args.no_native, background=background,
                        keep_alpha=args.keep_alpha, formats=formats, suffix=args.suffix,
                        allow_upscale=args.allow_upscale)
    print(json.dumps(manifest, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
