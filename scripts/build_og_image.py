"""Build the 1200x630 link-preview image (assets/images/og-image.jpg).

Run from the repo root:  python3 scripts/build_og_image.py
Colors match the navy palette in style.css.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BG = "#eef1f6"
NAVY = "#1c2e5a"
NAVY_MUTED = "#556a90"
PILL = "#c9d6ec"
ACCENT = "#2c4a85"

NAME = "Katrina Michelle"
TITLE = "Communications, Strategy & AI Adoption"
PLACE = "Munich, Germany"
URL = "ktrnab.github.io"

SERIF = "/System/Library/Fonts/Supplemental/Georgia.ttf"
SANS = "/System/Library/Fonts/Helvetica.ttc"

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

d.rectangle([0, 0, 9, H], fill=ACCENT)

d.text((84, 180), NAME, font=ImageFont.truetype(SERIF, 72), fill=NAVY)
d.text((84, 278), TITLE, font=ImageFont.truetype(SANS, 30), fill=NAVY_MUTED)

pill_font = ImageFont.truetype(SANS, 24)
tw = d.textlength(PLACE, font=pill_font)
d.rounded_rectangle([84, 360, 84 + tw + 98, 405], radius=23, fill=PILL)
d.text((104, 369), PLACE, font=pill_font, fill=NAVY)

d.text((84, 498), URL, font=ImageFont.truetype(SANS, 24), fill=ACCENT)

img.save("assets/images/og-image.jpg", quality=90)
print("wrote assets/images/og-image.jpg")
