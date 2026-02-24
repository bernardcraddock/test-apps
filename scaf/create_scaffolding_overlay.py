import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np
from matplotlib.patches import FancyArrowPatch, Rectangle, Polygon

# Load the architectural image
img_path = "/Volumes/Extreme_SSD/macos/GitHub_be/pumped-scripts/test-apps/scaf/extracted_images/page_1.png"
img = Image.open(img_path)

# Get image dimensions
img_width, img_height = img.size
print(f"Image size: {img_width} × {img_height} pixels")

# Create figure with image as background
fig, ax = plt.subplots(figsize=(16, 10), dpi=100)
ax.imshow(img, extent=[0, img_width, 0, img_height], aspect='auto', alpha=0.9)

# Scaffolding parameters (in pixels, scaled to image)
# From markdown: Ridge height 34.445, site drop 2.2m, building length ~33.5m

# Scaling factors (approximate from image analysis)
pixels_per_meter_horizontal = img_width / 33.5  # ~32 pixels per meter
pixels_per_meter_vertical = img_height / 10  # ~38 pixels per meter

# Building envelope (approximate from section drawing)
building_start_x = 100  # pixels from left
building_width = 32 * 33.5  # Building length in pixels
building_height = 10 * 38  # Max height in pixels
ridge_height = 9.6 * 38  # Ridge at 9.6m

# Draw scaffolding framework
scaffold_color = 'red'
scaffold_alpha = 0.6
scaffold_linewidth = 2

# Vertical scaffolding tubes (spaced every 2m = 64 pixels)
tube_spacing_px = 2 * pixels_per_meter_horizontal
for x in np.arange(building_start_x, building_start_x + building_width, tube_spacing_px):
    ax.plot([x, x], [0, img_height], color=scaffold_color, linewidth=scaffold_linewidth, 
            linestyle='--', alpha=scaffold_alpha, label='Vertical tubes' if x == building_start_x else '')

# Horizontal scaffolding platforms (spaced every 2m = 76 pixels)
platform_spacing_px = 2 * pixels_per_meter_vertical
for y in np.arange(100, ridge_height + 100, platform_spacing_px):
    ax.plot([building_start_x - 50, building_start_x + building_width + 50], [y, y], 
            color=scaffold_color, linewidth=1.5, linestyle='--', alpha=scaffold_alpha * 0.6)

# Diagonal bracing (X-pattern for stability)
brace_spacing_px = 200
brace_height_px = 150
for x in np.arange(building_start_x, building_start_x + building_width, brace_spacing_px * 2):
    for y_start in np.arange(100, ridge_height - brace_height_px, brace_height_px * 2):
        # Left diagonal
        ax.plot([x, x + brace_spacing_px], [y_start, y_start + brace_height_px], 
                color=scaffold_color, linewidth=1, linestyle=':', alpha=scaffold_alpha * 0.4)
        # Right diagonal
        ax.plot([x + brace_spacing_px, x], [y_start, y_start + brace_height_px], 
                color=scaffold_color, linewidth=1, linestyle=':', alpha=scaffold_alpha * 0.4)

# Add dimension annotations
# Height dimension (left side)
ax.annotate('', xy=(50, 100), xytext=(50, ridge_height + 50),
            arrowprops=dict(arrowstyle='<->', color='blue', lw=2))
ax.text(30, ridge_height / 2, 'H: 9.6m\n(RL 34.445)', fontsize=10, fontweight='bold', 
        ha='right', va='center', color='blue',
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

# Length dimension (bottom)
ax.annotate('', xy=(building_start_x - 20, 50), xytext=(building_start_x + building_width + 20, 50),
            arrowprops=dict(arrowstyle='<->', color='blue', lw=2))
ax.text(building_start_x + building_width / 2, 20, 'L: 33.5m', fontsize=10, fontweight='bold', 
        ha='center', va='top', color='blue',
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

# Add title
ax.text(img_width / 2, img_height - 30, 'Scaffolding Overlay - Iteration 1',
        fontsize=14, fontweight='bold', ha='center',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

# Legend
legend_text = ('Scaffolding Components:\n' +
               '-- Vertical tubes (2m spacing)\n' +
               '-- Horizontal platforms (2m spacing)\n' +
               ': Diagonal bracing (X-pattern)')
ax.text(img_width - 150, img_height - 150, legend_text, fontsize=9, ha='left', va='top',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8, edgecolor='red', linewidth=2))

# Remove axis ticks
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(0, img_width)
ax.set_ylim(0, img_height)

plt.tight_layout()
plt.savefig('/Volumes/Extreme_SSD/macos/GitHub_be/pumped-scripts/test-apps/scaf/scaffolding_overlay_v1.png',
           dpi=100, bbox_inches='tight', facecolor='white')
print("✓ Scaffolding overlay saved: scaffolding_overlay_v1.png")

plt.show()
