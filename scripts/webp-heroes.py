#!/usr/bin/env python3
"""Convert the 3 final hero JPEGs to WebP siblings for faster loads.

Keeps the JPEGs in place as a fallback. Prints before/after file sizes and a
mean per-pixel difference (0-255 scale) so we can confirm the WebP is visually
indistinguishable from the source before wiring it into the CSS.
"""
from pathlib import Path
from PIL import Image, ImageChops
import statistics

HEROES = Path(__file__).resolve().parent.parent / "assets" / "generated" / "heroes"
QUALITY = 82          # high enough to be perceptually lossless on these photos
METHOD = 6            # slowest/best WebP encoder effort

finals = sorted(HEROES.glob("*-final.jpg"))
if not finals:
    raise SystemExit(f"No *-final.jpg heroes found in {HEROES}")

for jpg in finals:
    webp = jpg.with_suffix(".webp")
    src = Image.open(jpg).convert("RGB")
    src.save(webp, format="WEBP", quality=QUALITY, method=METHOD)

    # Re-decode the WebP and measure how far it drifted from the JPEG.
    rt = Image.open(webp).convert("RGB")
    diff = ImageChops.difference(src, rt)
    hist = diff.histogram()
    # mean abs diff across all channels/pixels
    total = sum(i % 256 * c for i, c in enumerate(hist))
    count = sum(hist)
    mean_diff = total / count if count else 0

    jpg_kb = jpg.stat().st_size / 1024
    webp_kb = webp.stat().st_size / 1024
    saved = (1 - webp_kb / jpg_kb) * 100
    print(f"{jpg.name:38s} {jpg_kb:7.1f} KB -> {webp.name:40s} {webp_kb:7.1f} KB "
          f"({saved:5.1f}% smaller)  mean pixel diff: {mean_diff:.2f}/255")
