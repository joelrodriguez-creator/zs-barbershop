"""Tighten cut-beard.png, lineup.png, and kids.png so they match haircut.png's
content-to-canvas ratio. For the framed icons (lineup, kids) also strip the
cream/white outer mat so they sit cleanly on the page's matte-black bg.

Method: extract only the brass pixels (warm tones), then re-render on pure
matte-black canvas with the same 20% padding as haircut.png — same pattern
used for the beard-trim background swap."""
from PIL import Image
from pathlib import Path

ICONS = Path(__file__).parent.parent / "assets" / "generated" / "icons"
BG = (18, 18, 18)
TARGETS = ["cut-beard", "lineup", "kids"]

for slug in TARGETS:
    src_path = ICONS / f"{slug}.png"
    bak_path = ICONS / f"{slug}-raw.png"
    out_path = ICONS / f"{slug}.png"

    # Back up the raw version (only on first run — once bak exists, don't overwrite).
    if not bak_path.exists():
        Image.open(src_path).save(bak_path)
        print(f"Backed up: {bak_path.name}")

    img = Image.open(bak_path).convert("RGB")
    W, H = img.size
    print(f"\n{slug}: source {W}x{H}")

    # Brass detection: warm pixels, R highest, B lowest, R clearly above bg level.
    clean = Image.new("RGB", (W, H), BG)
    src_px = img.load()
    dst_px = clean.load()
    brass = 0
    for y in range(H):
        for x in range(W):
            r, g, b = src_px[x, y]
            if r > 110 and r >= g and g > b + 15 and r > b + 30 and r < 250:
                dst_px[x, y] = (r, g, b)
                brass += 1
    print(f"  Brass pixels: {brass} ({brass * 100 // (W*H)}%)")

    # Bbox of the brass content.
    gray = clean.convert("L")
    bb = gray.point(lambda v: 255 if v > 50 else 0).getbbox()
    if not bb:
        print(f"  WARNING: no brass detected in {slug}")
        continue
    print(f"  Bbox: {bb}")

    content = clean.crop(bb)
    cw, ch = content.size
    side = max(cw, ch)
    pad = int(side * 0.18)  # slightly tighter than haircut's 20% to maximize content
    canvas = side + 2 * pad
    square = Image.new("RGB", (canvas, canvas), BG)
    square.paste(content, ((canvas - cw) // 2, (canvas - ch) // 2))
    square.save(out_path, "PNG")
    print(f"  Wrote {out_path.name} ({canvas}x{canvas})")
