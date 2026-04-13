#!/usr/bin/env python3
"""Generate pinball-themed PWA icons using PIL"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_icon(size):
    """Create a pinball icon at the specified size."""
    img = Image.new('RGB', (size, size), color=(13, 17, 23))
    draw = ImageDraw.Draw(img)

    center = size // 2
    ball_radius = int(size * 0.25)
    portal_radius = int(size * 0.35)

    # Portal background rings (purple/blue gradient effect)
    ring_colors = ['#7950f2', '#5c7cfa', '#4c6ef5', '#339af0']
    for i, color in enumerate(ring_colors):
        r = int(portal_radius * (1 - i * 0.2))
        if r > 0:
            draw.ellipse(
                [(center - r, center - r), (center + r, center + r)],
                outline=color,
                width=max(1, size // 64)
            )

    # Ball
    ball_color = (196, 168, 130)
    inner_color = (13, 17, 23)
    draw.ellipse(
        [(center - ball_radius, center - ball_radius),
         (center + ball_radius, center + ball_radius)],
        fill=ball_color,
        outline=ball_color
    )

    # Ball highlight
    highlight_r = int(ball_radius * 0.6)
    draw.ellipse(
        [(center - highlight_r, center - highlight_r),
         (center + highlight_r, center + highlight_r)],
        fill=inner_color,
        outline=None
    )

    # Shine
    shine_r = int(ball_radius * 0.25)
    draw.ellipse(
        [(center - shine_r + size // 16, center - shine_r - size // 16),
         (center + shine_r + size // 16, center + shine_r - size // 16)],
        fill=ring_colors[1],
        outline=None
    )

    return img

# Create icons
sizes = [192, 512]
script_dir = os.path.dirname(os.path.abspath(__file__))

for size in sizes:
    icon = create_icon(size)
    icon_path = os.path.join(script_dir, f'icon-{size}.png')
    icon.save(icon_path)
    print(f'Created {icon_path}')

print('Icon generation complete!')
