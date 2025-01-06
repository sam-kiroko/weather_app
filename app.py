from flask import Flask, render_template, request, jsonify
import requests
from database import init_db, save_weather_data, get_weather_history
from config import OPENWEATHER_API_KEY

app = Flask(__name__)

# Weather condition code to icon mapping with stem word matching
WEATHER_ICONS = {
    'Clear': 'clear-day.svg',
    'Cloud': 'cloudy.svg',      # Will match 'Clouds', 'Cloudy'
    'Rain': 'rain.svg',         # Will match 'Rain', 'Raining'
    'Drizzle': 'drizzle.svg',
    'Thunder': 'thunderstorms.svg', # Will match 'Thunderstorm', 'Thunder'
    'Snow': 'snow.svg',         # Will match 'Snow', 'Snowing'
    'Mist': 'mist.svg',
    'Fog': 'fog.svg',
    'Haze': 'haze.svg',
    'default': 'cloudy.svg'
}

def get_weather_icon(condition):
    """Helper function to match weather condition with icon using stem words"""
    # Convert condition to title case for consistent matching
    condition = condition.title()
    print(f"Processing weather condition: {condition}")  # Debug log
    
    # Check for exact matches first
    if condition in WEATHER_ICONS:
        icon = WEATHER_ICONS[condition]
        print(f"Exact match found: {icon}")  # Debug log
        return icon
    
    # Check for stem word matches
    for stem, icon in WEATHER_ICONS.items():
        if stem in condition:  # e.g., 'Cloud' in 'Cloudy'
            print(f"Stem match found: {stem} in {condition} -> {icon}")  # Debug log
            return icon
    
    # Return default icon if no match found
    print(f"No match found, using default: {WEATHER_ICONS['default']}")  # Debug log
    return WEATHER_ICONS['default']

# Initialize database when app starts
with app.app_context():
    init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form.get('city')
    
    # Call OpenWeatherMap API
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather_main = data['weather'][0]['main']
        print(f"Weather condition received: {weather_main}")  # Debug log
        
        weather_data = {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'icon': get_weather_icon(weather_main),  # Use new helper function
            'coordinates': {
                'lat': data['coord']['lat'],
                'lon': data['coord']['lon']
            }
        }
        
        print(f"Selected icon: {weather_data['icon']}")  # Debug log
        
        # Save only the required fields to database
        db_data = {
            'city': weather_data['city'],
            'temperature': weather_data['temperature'],
            'description': weather_data['description'],
            'humidity': weather_data['humidity']
        }
        
        save_weather_data(**db_data)
        history = get_weather_history(city)
        
        return jsonify({
            'current': weather_data,
            'history': history
        })
    else:
        return jsonify({'error': 'City not found'}), 404

@app.route('/weather_by_coords', methods=['POST'])
def get_weather_by_coords():
    data = request.get_json()
    lat = data.get('lat')
    lon = data.get('lon')
    
    # Call OpenWeatherMap API with coordinates
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}&units=metric'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather_main = data['weather'][0]['main']
        city = data['name']
        
        print(f"Weather condition: {weather_main}")  # Debug log
        icon = get_weather_icon(weather_main)
        print(f"Selected icon: {icon}")  # Debug log
        
        weather_data = {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'icon': icon,
            'coordinates': {
                'lat': data['coord']['lat'],
                'lon': data['coord']['lon']
            }
        }
        
        # Save to database
        db_data = {
            'city': weather_data['city'],
            'temperature': weather_data['temperature'],
            'description': weather_data['description'],
            'humidity': weather_data['humidity']
        }
        
        save_weather_data(**db_data)
        history = get_weather_history(city)
        
        return jsonify({
            'current': weather_data,
            'history': history
        })
    else:
        return jsonify({'error': 'Location not found'}), 404

if __name__ == '__main__':
    app.run(debug=True) 