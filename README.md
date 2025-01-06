# Interactive Weather Map Application

A dynamic weather application that combines real-time weather data with an interactive map interface. Users can check weather conditions worldwide by either searching for a city or clicking directly on the map.

## Features

- **Interactive Map Interface**: Click anywhere on the map to get weather information
- **City Search**: Search weather conditions by city name
- **Real-time Weather Data**: Get current weather conditions including:
  - Temperature
  - Weather description
  - Humidity
  - Custom weather icons
- **Weather History**: Track historical weather data for searched locations
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Custom SVG Weather Icons**: Beautiful, scalable weather icons for different conditions

## Technologies Used

### Frontend
- HTML5
- CSS3 with CSS Variables
- JavaScript (ES6+)
- Leaflet.js for interactive maps
- Responsive design with viewport units

### Backend
- Python 3.x
- Flask web framework
- SQLite database
- OpenWeatherMap API

### Dependencies
- Flask 3.0.0
- Requests 2.31.0
- Python-dotenv 1.0.0
- Pillow 10.2.0

2. Create a virtual environment and activate it:
3. Install required packages:
  pip install -r requirements.txt   
5. Create a `.env` file in the root directory and add your OpenWeatherMap API key:
   OPENWEATHER_API_KEY=your_api_key_here
7. Initialize the weather icons:
   python weather_icons.py
9. Run the application:
10. Open your browser and navigate to:

## Usage

1. **Search by City**:
   - Enter a city name in the search bar
   - Click "Get Weather" or press Enter

2. **Search by Map**:
   - Click anywhere on the map
   - Weather information will appear in an overlay

3. **View Weather History**:
   - Weather history is automatically displayed below current conditions
   - History is stored for each location searched


## Project Structure
weather-app/
├── static/
│ ├── images/ # Weather icons
│ ├── js/
│ │ └── map.js # Map interaction logic
│ └── style.css # Global styles
├── templates/
│ └── index.html # Main application template
├── app.py # Flask application
├── config.py # Configuration settings
├── database.py # Database operations
├── weather_icons.py # Icon generation
└── requirements.txt # Project dependencies

## API Integration

The application uses the OpenWeatherMap API to fetch weather data. The following endpoints are used:

- Current weather by city name
- Current weather by coordinates

## Database

The application uses SQLite to store:
- Weather history by location
- Temperature records
- Humidity data
- Weather descriptions
- Timestamps

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenWeatherMap API for weather data
- Leaflet.js for mapping functionality
- OpenStreetMap for map tiles
