from collections import deque
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
source_path = ROOT / "public" / "assets" / "kgb-logo-extracted-prototype.png"
output_path = ROOT / "public" / "assets" / "kgb-logo-official.png"

image = Image.open(source_path).convert("RGBA")
width, height = image.size
pixels = image.load()


def is_background(pixel: tuple[int, int, int, int]) -> bool:
    red, green, blue, _ = pixel
    return max(red, green, blue) - min(red, green, blue) <= 10 and min(red, green, blue) >= 185


background = bytearray(width * height)
queue: deque[tuple[int, int]] = deque()

for x in range(width):
    for y in (0, height - 1):
        if is_background(pixels[x, y]) and not background[y * width + x]:
            background[y * width + x] = 1
            queue.append((x, y))

for y in range(height):
    for x in (0, width - 1):
        if is_background(pixels[x, y]) and not background[y * width + x]:
            background[y * width + x] = 1
            queue.append((x, y))

while queue:
    x, y = queue.popleft()
    for next_x, next_y in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
        if 0 <= next_x < width and 0 <= next_y < height:
            index = next_y * width + next_x
            if not background[index] and is_background(pixels[next_x, next_y]):
                background[index] = 1
                queue.append((next_x, next_y))

for y in range(height):
    for x in range(width):
        index = y * width + x
        if background[index]:
            pixels[x, y] = (255, 255, 255, 0)
        else:
            red, green, blue, _ = pixels[x, y]
            pixels[x, y] = (red, green, blue, 255)

alpha = image.getchannel("A")
bounds = alpha.getbbox()
if bounds:
    image = image.crop(bounds)

image.save(output_path, "PNG", optimize=True)
print(f"Saved {output_path} ({image.width}x{image.height})")
