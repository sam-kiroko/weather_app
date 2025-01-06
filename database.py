import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    
    # Create table for weather records
    c.execute('''
        CREATE TABLE IF NOT EXISTS weather_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL,
            temperature REAL NOT NULL,
            description TEXT NOT NULL,
            humidity INTEGER NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def save_weather_data(city, temperature, description, humidity):
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    
    c.execute('''
        INSERT INTO weather_records (city, temperature, description, humidity)
        VALUES (?, ?, ?, ?)
    ''', (city, temperature, description, humidity))
    
    conn.commit()
    conn.close()

def get_weather_history(city):
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    
    c.execute('''
        SELECT * FROM weather_records 
        WHERE city = ? 
        ORDER BY timestamp DESC 
        LIMIT 10
    ''', (city,))
    
    records = c.fetchall()
    conn.close()
    return records 