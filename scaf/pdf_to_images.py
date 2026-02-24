from pdf2image import convert_from_path
import os

pdf_path   = "/Volumes/Extreme_SSD/macos/GitHub_be/pumped-scripts/test-apps/scaf/Architectural_Plans_12_Mirrabooka_Crescent_Little_Bay_p7_land.pdf"
output_dir = "/Volumes/Extreme_SSD/macos/GitHub_be/pumped-scripts/test-apps/scaf/extracted_images"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Convert PDF pages to images
print(f"Converting PDF to images...")
images = convert_from_path(pdf_path)

for i, image in enumerate(images):
    output_path = os.path.join(output_dir, f"page_{i+1}.png")
    image.save(output_path)
    print(f"✓ Saved: {output_path}")

print(f"\nTotal pages converted: {len(images)}")
