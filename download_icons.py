import os
import requests

# Create the directory if it doesn't exist
os.makedirs('static/images', exist_ok=True)

# Dictionary of weather icons to download
WEATHER_ICONS = {
    'sunny.png': 'https://openweathermap.org/img/wn/01d@2x.png',
    'cloudy.png': 'https://openweathermap.org/img/wn/03d@2x.png',
    'rainy.png': 'https://openweathermap.org/img/wn/10d@2x.png',
    'thunder.png': 'https://openweathermap.org/img/wn/11d@2x.png',
    'snowy.png': 'https://openweathermap.org/img/wn/13d@2x.png',
    'mist.png': 'https://openweathermap.org/img/wn/50d@2x.png'
}

def download_icons():
    for filename, url in WEATHER_ICONS.items():
        filepath = os.path.join('static/images', filename)
        try:
            response = requests.get(url)
            response.raise_for_status()
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f'Successfully downloaded {filename}')
        except Exception as e:
            print(f'Failed to download {filename}: {e}')

if __name__ == '__main__':
    download_icons() 