
from PIL import Image, ImageEnhance

# Define input and output paths
input_path = "assets/profile.jpg"
output_path = "data/profile_processed.png"

# Open the original photograph
image = Image.open(input_path)

# Convert to grayscale
image = image.convert("L")

# Resize the image
image = image.resize((200, 200))

# Improve contrast
enhancer = ImageEnhance.Contrast(image)
image = enhancer.enhance(1.5)

# Save processed image
image.save(output_path)

print("Image processing completed!")
print(f"Saved to: {output_path}")
