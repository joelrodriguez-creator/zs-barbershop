"""Convert all 5 locked icons to RGBA with the matte-black bg replaced by
full transparency. Brass pixels keep their RGB and full alpha; anti-aliased
edge pixels get proportional alpha so the icons blend cleanly onto any dark bg
without visible boxes."""
from PIL import Image
from pathlib import Path

ICONS = Path(__file__).parent.parent / "assets" / "generated" / "icons"
TARGETS = ["haircut", "beard-trim", "cut-beard", "lineup", "kids"]

for slug in TARGETS:
    src_path = ICONS / f"{slug}.png"
    img = Image.open(src_path).convert("RGB")
    W, H = img.size
    out = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    src_px = img.load()
    dst_px = out.load()

    # Reference matte-black bg the icons were rendered on.
    BG = 18
    kept = 0
    for y in range(H):
        for x in range(W):
            r, g, b = src_px[x, y]
            # Luminance difference from the bg — this is how visible the pixel is
            # against matte black. Pure bg → 0, pure brass → ~165 (200*0.3+163*0.59+90*0.11 ≈ 165).
            luma = 0.299 * r + 0.587 * g + 0.114 * b
            delta = luma - BG
            if delta <= 2:
                continue  # essentially bg, leave transparent
            # Map delta to alpha. Multiply so anti-aliased edges fade naturally
            # while solid brass becomes fully opaque.
            alpha = int(min(255, max(0, delta * 1.8)))
            dst_px[x, y] = (r, g, b, alpha)
            kept += 1

    out.save(src_path, "PNG")
    print(f"{slug}.png: {W}x{H}, kept {kept} pixels ({kept * 100 // (W*H)}%) with alpha")
