WEATHER_ICONS = {
    'clear-day.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
        <circle cx="32" cy="32" r="16" fill="#FFD700" stroke="#FFA500" stroke-width="2"/>
        <g fill="#FFD700">
            <rect x="30" y="8" width="4" height="8" rx="2"/>
            <rect x="30" y="48" width="4" height="8" rx="2"/>
            <rect x="48" y="30" width="8" height="4" rx="2"/>
            <rect x="8" y="30" width="8" height="4" rx="2"/>
        </g>
    </svg>''',
    
    'cloudy.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
        <path d="M16 32 Q16 24 24 24 Q24 16 32 16 Q40 16 40 24 Q48 24 48 32 Q48 40 40 40 L24 40 Q16 40 16 32Z" 
              fill="#E0E0E0" stroke="#808080" stroke-width="2"/>
    </svg>''',
    
    'rain.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
        <path d="M16 24 Q16 16 24 16 Q24 8 32 8 Q40 8 40 16 Q48 16 48 24 Q48 32 40 32 L24 32 Q16 32 16 24Z" 
              fill="#A0A0A0" stroke="#808080" stroke-width="2"/>
        <g stroke="#4169E1" stroke-width="2">
            <line x1="24" y1="40" x2="22" y2="48"/>
            <line x1="32" y1="40" x2="30" y2="48"/>
            <line x1="40" y1="40" x2="38" y2="48"/>
        </g>
    </svg>''',
    
    'thunderstorms.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
        <path d="M16 24 Q16 16 24 16 Q24 8 32 8 Q40 8 40 16 Q48 16 48 24 Q48 32 40 32 L24 32 Q16 32 16 24Z" 
              fill="#666" stroke="#444" stroke-width="2"/>
        <path d="M32 28 L26 38 L34 38 L28 52" fill="none" stroke="#FFD700" stroke-width="3"/>
    </svg>''',
    
    'snow.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
        <path d="M16 24 Q16 16 24 16 Q24 8 32 8 Q40 8 40 16 Q48 16 48 24 Q48 32 40 32 L24 32 Q16 32 16 24Z" 
              fill="#E0E0E0" stroke="#808080" stroke-width="2"/>
        <g fill="#FFF">
            <circle cx="24" cy="44" r="3"/>
            <circle cx="32" cy="48" r="3"/>
            <circle cx="40" cy="44" r="3"/>
        </g>
    </svg>''',
    
    'mist.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
        <g stroke="#B0B0B0" stroke-width="3">
            <line x1="16" y1="24" x2="48" y2="24"/>
            <line x1="16" y1="32" x2="48" y2="32"/>
            <line x1="16" y1="40" x2="48" y2="40"/>
        </g>
    </svg>'''
}

def save_icons():
    import os
    
    # Create static/images directory if it doesn't exist
    os.makedirs('static/images', exist_ok=True)
    
    # Save each icon
    for filename, svg_content in WEATHER_ICONS.items():
        filepath = os.path.join('static/images', filename)
        with open(filepath, 'w') as f:
            f.write(svg_content)
        print(f'Created {filename}')

if __name__ == '__main__':
    save_icons() 