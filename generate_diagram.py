from PIL import Image, ImageDraw, ImageFont
import os

# Create a canvas
width, height = 1200, 600
img = Image.new('RGB', (width, height), color=(30, 30, 30))
draw = ImageDraw.Draw(img)

def draw_box(x, y, w, h, title, detail, color):
    # Box shadow
    draw.rectangle([x+5, y+5, x+w+5, y+h+5], fill=(10, 10, 10))
    # Main box
    draw.rectangle([x, y, x+w, y+h], fill=color, outline=(255, 255, 255), width=2)
    # Text
    draw.text((x+20, y+20), title, fill=(255, 255, 255))
    draw.text((x+20, y+60), detail, fill=(255, 255, 255))

# Colors
ORANGE = (230, 126, 34)
BLUE = (52, 152, 219)
GREEN = (46, 204, 113)
PURPLE = (155, 89, 182)

# Flow: Heart -> Gearbox -> Bucket -> Action
draw_box(50, 200, 220, 120, "1. THE HEART", "16,000,000 Hz\n(Crystal Osc)", ORANGE)
draw_box(330, 200, 220, 120, "2. THE GEARBOX", "Prescaler /1024\nWait for 1024 beats", BLUE)
draw_box(610, 200, 250, 120, "3. THE BUCKET", "Timer1 counts up\nTarget: 15,625", GREEN)
draw_box(920, 200, 220, 120, "4. THE ACTION", "Match! -> Toggle LED\nReset to 0", PURPLE)

# Draw Arrows
def arrow(x1, y1, x2, y2):
    draw.line([x1, y1, x2, y2], fill=(255, 255, 255), width=3)
    draw.polygon([x2, y2, x2-10, y2-5, x2-10, y2+5], fill=(255, 255, 255))

arrow(270, 260, 320, 260)
arrow(550, 260, 600, 260)
arrow(860, 260, 910, 260)

img.save('timer_diagram.png')
