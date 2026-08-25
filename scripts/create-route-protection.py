from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
output_path = ROOT / "public" / "assets" / "route-protection.png"
scale = 3
width, height = 1200, 360
image = Image.new("RGBA", (width * scale, height * scale), (0, 0, 0, 0))
draw = ImageDraw.Draw(image)

ink = (16, 29, 39, 255)
blue = (10, 148, 201, 255)
yellow = (245, 196, 0, 255)
paper = (255, 255, 255, 255)


def point(x: int, y: int) -> tuple[int, int]:
    return x * scale, y * scale


def box(coords: tuple[int, int, int, int], fill=None, outline=None, width=1):
    draw.rounded_rectangle(tuple(value * scale for value in coords), radius=3 * scale, fill=fill, outline=outline, width=width * scale)


def line(coords: list[tuple[int, int]], fill, width=1):
    draw.line([point(x, y) for x, y in coords], fill=fill, width=width * scale, joint="curve")


# The yellow path is deliberately kept open so the HTML labels can sit below it.
line([(118, 180), (1082, 180)], yellow, 6)
for x, color in ((118, blue), (600, yellow), (1082, blue)):
    draw.ellipse(tuple(value * scale for value in (x - 15, 165, x + 15, 195)), fill=paper, outline=ink, width=5 * scale)
    draw.ellipse(tuple(value * scale for value in (x - 7, 173, x + 7, 187)), fill=color)

# Origin: a shipping container with a small port crane.
box((38, 105, 258, 230), fill=paper, outline=ink, width=6)
for x in (78, 118, 158, 198):
    line([(x, 112), (x, 223)], blue, 4)
line([(40, 103), (93, 68), (218, 68), (218, 103)], ink, 6)
line([(93, 68), (93, 125)], ink, 6)
line([(93, 125), (136, 125)], ink, 6)
line([(136, 125), (136, 145)], ink, 6)

# Protection: a clear shield with a check at the operational center.
draw.polygon([point(x, y) for x, y in [(600, 43), (683, 77), (673, 187), (600, 259), (527, 187), (517, 77)]], fill=yellow, outline=ink)
line([(555, 150), (587, 181), (650, 111)], blue, 12)
line([(555, 150), (587, 181), (650, 111)], ink, 5)

# Destination: a secure truck with a visible cargo body.
box((846, 106, 1013, 215), fill=blue, outline=ink, width=6)
line([(1013, 143), (1054, 143), (1090, 180), (1090, 215), (1013, 215)], ink, 6)
line([(1051, 147), (1051, 180), (1085, 180)], ink, 5)
line([(869, 117), (869, 204)], paper, 4)
line([(900, 117), (900, 204)], paper, 4)
line([(931, 117), (931, 204)], paper, 4)
for x in (891, 1049):
    draw.ellipse(tuple(value * scale for value in (x - 25, 195, x + 25, 245)), fill=ink)
    draw.ellipse(tuple(value * scale for value in (x - 10, 210, x + 10, 230)), fill=paper)

# A small yellow signal on the truck keeps the brand cue functional rather than decorative.
line([(1028, 125), (1060, 125)], yellow, 7)

image = image.resize((width, height), Image.Resampling.LANCZOS)
image.save(output_path, "PNG", optimize=True)
print(f"Saved {output_path} ({width}x{height}, RGBA)")
