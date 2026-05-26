"""Take lineup-v4.png (clipper + separate coiled cord) and produce a clipper-only
icon, rotated to vertical, centered on a square matte-black canvas.

Strategy: paint out cord regions, rotate, then re-render brass-only on a fresh
pure-black canvas so there are no compression-artifact rectangles."""
from PIL import Image, ImageDraw
from pathlib import Path

ICONS = Path(__file__).parent.parent / "assets" / "generated" / "icons"
SRC = ICONS / "lineup-v4.png"
DST = ICONS / "lineup-edit.png"

img = Image.open(SRC).convert("RGB")
W, H = img.size
print(f"Source: {W}x{H}")

bg_sampled = img.getpixel((10, 10))
print(f"Background sampled: {bg_sampled}")

# Use the same matte-black target the rest of the icon set uses.
BG = (18, 18, 18)

# Paint out cord coil (right half) and cord stub (bottom-left).
draw = ImageDraw.Draw(img)
draw.rectangle([(int(W * 0.48), 0), (W, H)], fill=bg_sampled)
draw.rectangle([(0, int(H * 0.62)), (int(W * 0.48), H)], fill=bg_sampled)

# Bbox of clipper while still in source coordinates (so rotation has room).
gray = img.convert("L")
threshold = max(bg_sampled[0], bg_sampled[1], bg_sampled[2]) + 25
bbox = gray.point(lambda v: 255 if v > threshold else 0).getbbox()
print(f"Bbox of clipper: {bbox}")

# Crop with generous padding so rotation doesn't clip the blade tips.
left, top, right, bottom = bbox
cw = right - left
ch = bottom - top
side = max(cw, ch)
pad = int(side * 0.45)  # extra room for rotation
target = side + 2 * pad
cx = (left + right) // 2
cy = (top + bottom) // 2
crop_box = (max(0, cx - target // 2), max(0, cy - target // 2),
            min(W, cx + target // 2), min(H, cy + target // 2))
result = img.crop(crop_box)

# Rotate clipper to vertical (~22° counter-clockwise straightens V4's tilt).
ANGLE = 22
result = result.rotate(ANGLE, resample=Image.BICUBIC, fillcolor=bg_sampled, expand=True)
print(f"Rotated by {ANGLE}°. Size: {result.size}")

# Brass-only re-render on pure matte black. Detect any pixel that's
# clearly warmer than bg (red+green dominant, blue lowest).
RW, RH = result.size
clean = Image.new("RGB", (RW, RH), BG)
src_px = result.load()
dst_px = clean.load()
brass = 0
for y in range(RH):
    for x in range(RW):
        r, g, b = src_px[x, y]
        # Brass: warm — R high, G medium-high, B lowest, and R noticeably brighter than bg.
        if r > 100 and r >= g and g > b + 15 and r > b + 30:
            dst_px[x, y] = (r, g, b)
            brass += 1
print(f"Kept {brass} brass pixels ({brass * 100 // (RW*RH)}%)")

# Re-bbox the clean clipper, recenter on padded square canvas.
gray2 = clean.convert("L")
bb = gray2.point(lambda v: 255 if v > 50 else 0).getbbox()
if not bb:
    raise SystemExit("No brass content detected after extraction.")
print(f"Clean bbox: {bb}")

content = clean.crop(bb)
cw2, ch2 = content.size
final_side = max(cw2, ch2)
final_pad = int(final_side * 0.20)
canvas_side = final_side + 2 * final_pad
square = Image.new("RGB", (canvas_side, canvas_side), BG)
square.paste(content, ((canvas_side - cw2) // 2, (canvas_side - ch2) // 2))
square.save(DST, "PNG")
print(f"Wrote {DST} ({canvas_side}x{canvas_side})")
