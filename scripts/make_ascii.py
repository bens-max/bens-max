
from PIL import Image

input_path = "data/profile_processed.png"
output_path = "data/profile_ascii.txt"

# Characters arranged from darkest to brightest
ascii_chars = "@%#*+=-:. "

# Open image
image = Image.open(input_path).convert("L")

# Resize to account for terminal character proportions
image = image.resize((100, 50))

ascii_art = ""

for y in range(image.height):
    for x in range(image.width):
        brightness = image.getpixel((x, y))

        index = int(brightness / 256 * len(ascii_chars))
        index = min(index, len(ascii_chars) - 1)

        ascii_art += ascii_chars[index]

    ascii_art += "\n"

# Save ASCII artwork
with open(output_path, "w") as file:
    file.write(ascii_art)

print("ASCII conversion completed!")
print(f"Saved to: {output_path}")
