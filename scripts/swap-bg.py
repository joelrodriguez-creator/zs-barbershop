"""Take beard-trim-r2-v2 (beard on olive/tan bg) and re-render on matte black,
keeping only the brass lines and recentering with balanced padding (matches
the haircut.png treatment)."""
from PIL import Image
from pathlib import Path

ICONS = Path(__file__).parent.parent / "assets" / "generated" / "icons"
SRC = ICONS / "beard-trim-r2-v2.png"
DST = ICONS / "beard-trim-edit.png"

src = Image.open(SRC).convert("RGB")
W, H = src.size

# Matte-black target bg (matches haircut.png — sampled value was ~ (18,18,18)).
BG = (18, 18, 18)

# Build a new image: keep only the brass pixels, everything else becomes BG.
# Brass ≈ (200, 163, 90). Detect via: red dominant, blue < red, decent saturation.
out = Image.new("RGB", (W, H), BG)
src_px = src.load()
out_px = out.load()
brass_pixels = 0
for y in range(H):
    for x in range(W):
        r, g, b = src_px[x, y]
        # Heuristic: brass ≈ (200,163,90). Strict: bright, very warm, orange not yellow.
        if r > 150 and r - b > 70 and r - g > 25:
            out_px[x, y] = (r, g, b)
            brass_pixels += 1

print(f"Kept {brass_pixels} brass pixels ({brass_pixels * 100 // (W*H)}%)")

# Find bbox of brass content, crop with even padding so the icon fills like haircut.
gray = out.convert("L")
bbox = gray.point(lambda v: 255 if v > 50 else 0).getbbox()
print(f"Bbox of brass content: {bbox}")

left, top, right, bottom = bbox
cw = right - left
ch = bottom - top
side = max(cw, ch)
pad = int(side * 0.20)
target = side + 2 * pad

cx = (left + right) // 2
cy = (top + bottom) // 2
crop_box = (cx - target // 2, cy - target // 2, cx + target // 2, cy + target // 2)
crop_box = (max(0, crop_box[0]), max(0, crop_box[1]),
            min(W, crop_box[2]), min(H, crop_box[3]))

result = out.crop(crop_box)
rw, rh = result.size
side = max(rw, rh)
square = Image.new("RGB", (side, side), BG)
square.paste(result, ((side - rw) // 2, (side - rh) // 2))
square.save(DST, "PNG")
print(f"Wrote {DST} ({side}x{side})")
