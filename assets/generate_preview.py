#!/usr/bin/env python3
"""Generate social preview image for Awesome Agent Skills repository"""

from PIL import Image, ImageDraw, ImageFont
import os

# Dimensions for GitHub social preview
WIDTH = 1280
HEIGHT = 640

# Color scheme - modern AI/tech theme
BG_COLOR = "#0F172A"  # Dark blue-gray
ACCENT_COLOR = "#8B5CF6"  # Purple
SECONDARY_COLOR = "#06B6D4"  # Cyan
TEXT_COLOR = "#F8FAFC"  # Off-white
SUBTITLE_COLOR = "#94A3B8"  # Light gray

# Create image
img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
draw = ImageDraw.Draw(img)

# Add gradient-like effect with circles
for i in range(5):
    x = WIDTH * (0.2 + i * 0.2)
    y = HEIGHT * (0.3 + (i % 2) * 0.4)
    radius = 150 - i * 20
    # Create circular gradient effect
    for r in range(radius, 0, -5):
        alpha = int((r / radius) * 30)
        color = f"#{ACCENT_COLOR[1:]}" if i % 2 == 0 else f"#{SECONDARY_COLOR[1:]}"
        # Draw semi-transparent circles
        left = x - r
        top = y - r
        right = x + r
        bottom = y + r
        draw.ellipse([left, top, right, bottom], fill=None, outline=color, width=2)

# Try to use system fonts, fallback to default
try:
    # Try to load a nice font
    title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 90)
    subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
    tagline_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)
except:
    # Fallback to default font
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()
    tagline_font = ImageFont.load_default()

# Add main title
title = "🎯 Awesome Agent Skills"
title_bbox = draw.textbbox((0, 0), title, font=title_font)
title_width = title_bbox[2] - title_bbox[0]
title_x = (WIDTH - title_width) // 2
title_y = 180

# Draw title with shadow effect
draw.text((title_x + 3, title_y + 3), title, fill="#000000", font=title_font)
draw.text((title_x, title_y), title, fill=TEXT_COLOR, font=title_font)

# Add tagline
tagline = "The definitive resource for Agent Skills"
tagline_bbox = draw.textbbox((0, 0), tagline, font=subtitle_font)
tagline_width = tagline_bbox[2] - tagline_bbox[0]
tagline_x = (WIDTH - tagline_width) // 2
tagline_y = title_y + 110

draw.text((tagline_x, tagline_y), tagline, fill=SUBTITLE_COLOR, font=subtitle_font)

# Add description
desc = "70+ Skills • Tools • Tutorials • Research"
desc_bbox = draw.textbbox((0, 0), desc, font=tagline_font)
desc_width = desc_bbox[2] - desc_bbox[0]
desc_x = (WIDTH - desc_width) // 2
desc_y = tagline_y + 70

draw.text((desc_x, desc_y), desc, fill=ACCENT_COLOR, font=tagline_font)

# Add bottom badge-like elements
badge_y = HEIGHT - 80
badge_texts = ["Claude", "Cursor", "GitHub Copilot", "OpenAI Codex"]
badge_spacing = 250
start_x = (WIDTH - (len(badge_texts) * badge_spacing - 50)) // 2

for i, text in enumerate(badge_texts):
    x = start_x + i * badge_spacing
    # Draw rounded rectangle
    draw.rounded_rectangle(
        [x, badge_y, x + 220, badge_y + 45],
        radius=22,
        fill=None,
        outline=SECONDARY_COLOR,
        width=2
    )
    # Draw text
    text_bbox = draw.textbbox((0, 0), text, font=tagline_font)
    text_width = text_bbox[2] - text_bbox[0]
    text_x = x + (220 - text_width) // 2
    text_y = badge_y + 8
    draw.text((text_x, text_y), text, fill=TEXT_COLOR, font=tagline_font)

# Save the image
output_path = os.path.join(os.path.dirname(__file__), 'social-preview.png')
img.save(output_path, 'PNG', optimize=True, quality=95)
print(f"Social preview image created: {output_path}")
print(f"Dimensions: {WIDTH}x{HEIGHT}px")
