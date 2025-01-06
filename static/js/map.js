let map;
let marker;

function initMap() {
    // Initialize map with a more interesting default view
    map = L.map('map').setView([20, 0], 2);
    
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Add click event to map
    map.on('click', async function(e) {
        const lat = e.latlng.lat;
        const lon = e.latlng.lng;
        
        console.log('Map clicked:', lat, lon); // Debug log
        
        // Update marker position
        if (marker) {
            marker.setLatLng([lat, lon]);
        } else {
            marker = L.marker([lat, lon]).addTo(map);
        }
        
        try {
            const response = await fetch('/weather_by_coords', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ lat, lon })
            });
            
            const data = await response.json();
            if (data.error) {
                alert(data.error);
                return;
            }
            updateMapWeather(data);
        } catch (error) {
            console.error('Error:', error);
            alert('Error fetching weather data');
        }
    });

    // Add close button event listener
    document.querySelector('.close-overlay').addEventListener('click', closeOverlay);

    // Add click event to overlay background to close it
    document.querySelector('.map-overlay').addEventListener('click', function(e) {
        if (e.target === this) {
            closeOverlay();
        }
    });

    // Prevent clicks inside the weather card from closing the overlay
    document.querySelector('.map-weather-card').addEventListener('click', function(e) {
        e.stopPropagation();
    });
}

function closeOverlay() {
    const overlay = document.querySelector('.map-overlay');
    overlay.classList.remove('visible');
    // Wait for transition to complete before hiding
    setTimeout(() => {
        overlay.style.display = 'none';
    }, 300); // Match this with your CSS transition duration
}

function updateMapWeather(data) {
    console.log('Updating weather with data:', data); // Debug log
    const overlay = document.querySelector('.map-overlay');
    const weatherCard = document.querySelector('.map-weather-card');
    
    // Add fallback icon handling
    const iconPath = `/static/images/${data.current.icon}`;
    console.log('Loading icon from:', iconPath); // Debug log
    const fallbackIcon = '/static/images/cloudy.png';
    
    weatherCard.innerHTML = `
        <h2>${data.current.city}</h2>
        <div class="weather-main">
            <img src="${iconPath}" 
                 alt="Weather icon" 
                 class="weather-icon"
                 onerror="this.onerror=null; this.src='${fallbackIcon}'; console.error('Failed to load icon:', '${iconPath}')"
            >
            <div class="temperature">${Math.round(data.current.temperature)}°C</div>
        </div>
        <div class="weather-details">
            <p class="description">${data.current.description}</p>
            <p class="humidity">Humidity: ${data.current.humidity}%</p>
        </div>
        ${renderHistory(data.history)}
    `;
    
    // Show overlay with animation
    overlay.style.display = 'block';
    overlay.offsetHeight; // Force reflow
    overlay.classList.add('visible');

    // Verify icon loading
    const iconImg = weatherCard.querySelector('.weather-icon');
    iconImg.addEventListener('load', () => {
        console.log('Icon loaded successfully:', iconPath);
    });
    iconImg.addEventListener('error', () => {
        console.error('Icon failed to load:', iconPath);
    });
}

function renderHistory(history) {
    if (!history || history.length === 0) return '';
    
    const historyHTML = history.map(record => `
        <div class="history-item">
            <div class="history-date">${new Date(record.timestamp).toLocaleString()}</div>
            <div class="history-temp">${Math.round(record.temperature)}°C</div>
            <div class="history-desc">${record.description}</div>
        </div>
    `).join('');
    
    return `
        <div class="history-card">
            <h3>Weather History</h3>
            <div class="history-list">
                ${historyHTML}
            </div>
        </div>
    `;
}

// Initialize map when page loads
document.addEventListener('DOMContentLoaded', initMap);

// Add this to the form submission handler in index.html
function handleCitySearch(data) {
    const lat = data.current.coordinates.lat;
    const lon = data.current.coordinates.lon;
    map.setView([lat, lon], 10);
    
    if (marker) {
        marker.setLatLng([lat, lon]);
    } else {
        marker = L.marker([lat, lon]).addTo(map);
    }
    
    updateMapWeather(data);
} 