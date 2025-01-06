import os
import shutil

# Create the static/images directory if it doesn't exist
os.makedirs('static/images', exist_ok=True)

# Source directory containing your weather icons
src_dir = 'weather-icons'  # Adjust this path to your weather-icons folder location

# Copy all SVG files from weather-icons to static/images
for file in os.listdir(src_dir):
    if file.endswith('.svg'):
        src_file = os.path.join(src_dir, file)
        dst_file = os.path.join('static/images', file)
        shutil.copy2(src_file, dst_file)
        print(f'Copied {file} to static/images/') 