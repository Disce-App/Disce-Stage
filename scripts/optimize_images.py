#!/usr/bin/env python3
"""Image optimization pipeline for Disce Stage (DESIGN-BRIEF.md Section 9).

Reads a master image from ``images/`` (masters are never modified) and writes
AVIF (primary) + WebP (fallback) derivatives into ``images/derived/`` at a set
of target widths, capped by the master's real pixel width so nothing is ever
upscaled. It also emits a <= 1 KB WebP LQIP placeholder (about 24 px wide) and
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

Budgets (Section 9): hero-class <= 250 KB AVIF at the largest width,
card-class <= 120 KB. Quality starts at ~q50 and is stepped down until the
largest AVIF meets the budget (or the floor is reached).
"""

import argparse
import base64
import io
import json
import os
import sys

try:
    from PIL import Image
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


def target_widths(master_width, requested, append_native=True):
    widths = sorted({int(w) for w in requested if 0 < int(w) <= master_width})
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
             append_native=True):
    image = Image.open(master)
    image.load()
    image = apply_crop(image, crop_inset, crop_box)
    master_w, master_h = image.size
    rgb = image.convert("RGB")

    widths = target_widths(master_w, requested_widths, append_native)
    largest = widths[-1]

    # Pick the highest AVIF quality whose largest-width output meets budget.
    quality = AVIF_QUALITY_START
    avif_sizes = {}
    while True:
        for width in widths:
            height = scaled_height(width, master_w, master_h)
            resized = rgb.resize((width, height), Image.LANCZOS)
            avif_sizes[width] = encode_avif(resized, quality) if width == largest else None
        if len(avif_sizes[largest]) <= BUDGETS[kind] or quality <= AVIF_QUALITY_FLOOR:
            break
        quality -= AVIF_QUALITY_STEP

    os.makedirs(out_dir, exist_ok=True)
    stem = os.path.splitext(os.path.basename(master))[0]
    derivatives = []

    for width in widths:
        height = scaled_height(width, master_w, master_h)
        resized = rgb.resize((width, height), Image.LANCZOS)
        avif_data = encode_avif(resized, quality)
        webp_data = encode_webp(resized)
        avif_path = os.path.join(out_dir, f"{stem}-{width}.avif")
        webp_path = os.path.join(out_dir, f"{stem}-{width}.webp")
        with open(avif_path, "wb") as fh:
            fh.write(avif_data)
        with open(webp_path, "wb") as fh:
            fh.write(webp_data)
        derivatives.append({"format": "avif", "width": width, "height": height,
                            "file": avif_path, "bytes": len(avif_data)})
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

    largest_avif = next(d for d in derivatives if d["format"] == "avif" and d["width"] == largest)
    return {
        "master": master,
        "kind": kind,
        "crop": {"inset_percent": crop_inset, "box": list(crop_box) if crop_box else None},
        "master_width": master_w,
        "master_height": master_h,
        "max_width": largest,
        "upscaled": False,
        "budget_bytes": BUDGETS[kind],
        "budget_ok": largest_avif["bytes"] <= BUDGETS[kind],
        "quality": {"avif": quality, "webp": WEBP_QUALITY},
        "lqip": lqip,
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
    manifest = optimize(args.master, args.kind, args.out, requested,
                        crop_inset=args.crop_inset, crop_box=crop_box,
                        append_native=not args.no_native)
    print(json.dumps(manifest, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
