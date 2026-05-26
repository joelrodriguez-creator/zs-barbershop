"""Crop the barber pole out of haircut-v4.png, leaving scissors+comb centered.

Strategy: paint the left region with the actual sampled background color so there's
no seam, detect bbox of the remaining brass content, then crop with even padding
so the result is a balanced square icon.
"""
from PIL import Image, ImageDraw
from pathlib import Path

ICONS = Path(__file__).parent.parent / "assets" / "generated" / "icons"
SRC = ICONS / "haircut-v4.png"
DST = ICONS / "haircut-edit.png"

img = Image.open(SRC).convert("RGB")
W, H = img.size
print(f"Source: {W}x{H}")

# Sample the actual background color from a corner so there's no seam.
bg = img.getpixel((10, 10))
print(f"Background color sampled: {bg}")

# Paint over the barber pole region with the sampled background.
# Pole + sparkle near it occupy the left ~42% horizontally.
draw = ImageDraw.Draw(img)
draw.rectangle([(0, 0), (int(W * 0.42), H)], fill=bg)

# Find bounding box of remaining brass content.
gray = img.convert("L")
threshold = max(bg[0], bg[1], bg[2]) + 20  # anything brighter than the bg
bbox = gray.point(lambda v: 255 if v > threshold else 0).getbbox()
print(f"Bbox of remaining content: {bbox}")

# Crop with even padding so the icon is balanced.
left, top, right, bottom = bbox
content_w = right - left
content_h = bottom - top
side = max(content_w, content_h)
pad = int(side * 0.20)  # 20% padding around content
target = side + 2 * pad

cx = (left + right) // 2
cy = (top + bottom) // 2
crop_box = (cx - target // 2, cy - target // 2, cx + target // 2, cy + target // 2)
# Clamp to image bounds.
crop_box = (max(0, crop_box[0]), max(0, crop_box[1]),
            min(W, crop_box[2]), min(H, crop_box[3]))

result = img.crop(crop_box)
# Ensure square by padding shortest side with sampled bg.
rw, rh = result.size
side = max(rw, rh)
square = Image.new("RGB", (side, side), bg)
square.paste(result, ((side - rw) // 2, (side - rh) // 2))
square.save(DST, "PNG")
print(f"Wrote {DST} ({side}x{side})")
