
from pathlib import Path
from html import escape

# File paths
INPUT_FILE = Path("data/profile_ascii.txt")
OUTPUT_FILE = Path("assets/avi-ascii.svg")

# Terminal appearance
BACKGROUND = "#050a05"
TEXT_COLOR = "#39ff72"
FONT_SIZE = 8
LINE_HEIGHT = 10

def create_svg():

    # Read ASCII artwork
    with open(INPUT_FILE, "r") as file:
        lines = file.read().splitlines()

    # Calculate SVG dimensions
    max_width = max(len(line) for line in lines)
    svg_width = max_width * FONT_SIZE * 0.62 + 20
    svg_height = len(lines) * LINE_HEIGHT + 20

    # Start SVG document
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{svg_width}" height="{svg_height}" '
        f'viewBox="0 0 {svg_width} {svg_height}">',

        f'<rect width="100%" height="100%" fill="{BACKGROUND}"/>',

        """
        <style>
            .ascii-line {
                font-family: monospace;
                font-size: 8px;
                fill: #39ff72;
                clip-path: inset(0 100% 0 0);
                animation: typing 2s steps(100, end) forwards;
            }

            @keyframes typing {
                from {
                    clip-path: inset(0 100% 0 0);
                }
                to {
                    clip-path: inset(0 0 0 0);
                }
            }
        </style>
        """
    ]

    # Add each ASCII line
    for index, line in enumerate(lines):

        y_position = 12 + index * LINE_HEIGHT
        delay = index * 0.06

        svg.append(
            f'<text x="10" y="{y_position}" '
            f'class="ascii-line" '
            f'style="animation-delay: {delay:.2f}s" '
            f'xml:space="preserve">{escape(line)}</text>'
        )

    # Close SVG
    svg.append("</svg>")

    # Save SVG
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text("\n".join(svg))

    print("Animated ASCII SVG generated!")
    print(f"Output: {OUTPUT_FILE}")
    print(f"Dimensions: {svg_width} x {svg_height}")


if __name__ == "__main__":
    create_svg()
