import os
from PIL import Image, ImageDraw

# Create static/images directory if it doesn't exist
os.makedirs('static/images', exist_ok=True)

def create_sunny_icon():
    img = Image.new('RGBA', (100, 100), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    # Draw sun
    draw.ellipse([20, 20, 80, 80], fill='yellow', outline='orange', width=2)
    return img

def create_cloudy_icon():
    img = Image.new('RGBA', (100, 100), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    # Draw cloud
    draw.ellipse([30, 30, 70, 70], fill='#e0e0e0', outline='#808080', width=2)
    return img

def create_rainy_icon():
    img = Image.new('RGBA', (100, 100), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    # Draw cloud
    draw.ellipse([30, 20, 70, 50], fill='#a0a0a0', outline='#808080', width=2)
    # Draw raindrops
    for x in range(35, 71, 15):
        draw.line([x, 60, x-5, 75], fill='blue', width=2)
    return img

def create_thunder_icon():
    img = Image.new('RGBA', (100, 100), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    # Draw lightning bolt
    points = [(50,20), (30,50), (45,50), (25,80), (75,45), (55,45), (70,20)]
    draw.polygon(points, fill='yellow', outline='orange')
    return img

def create_snowy_icon():
    img = Image.new('RGBA', (100, 100), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    # Draw snowflakes
    for x in range(30, 71, 20):
        draw.ellipse([x-5, 45, x+5, 55], fill='white', outline='#e0e0e0')
    return img

def create_mist_icon():
    img = Image.new('RGBA', (100, 100), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    # Draw mist lines
    for y in range(40, 71, 15):
        draw.line([20, y, 80, y], fill='#c0c0c0', width=5)
    return img

# Dictionary of icon creation functions
ICONS = {
    'sunny.png': create_sunny_icon,
    'cloudy.png': create_cloudy_icon,
    'rainy.png': create_rainy_icon,
    'thunder.png': create_thunder_icon,
    'snowy.png': create_snowy_icon,
    'mist.png': create_mist_icon
}

def create_icons():
    for filename, create_func in ICONS.items():
        filepath = os.path.join('static/images', filename)
        try:
            img = create_func()
            img.save(filepath, 'PNG')
            print(f'Successfully created {filename}')
        except Exception as e:
            print(f'Failed to create {filename}: {e}')

if __name__ == '__main__':
    create_icons() 