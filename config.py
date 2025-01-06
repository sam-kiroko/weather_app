import os
from dotenv import load_dotenv
from pathlib import Path

def setup_config():
    try:
        # Get the directory containing this file
        base_dir = Path(__file__).resolve().parent
        
        print(f"Base directory: {base_dir}")
        print(f"Current working directory: {os.getcwd()}")
        
        # Look for .env file in both current directory and parent directory
        env_path = base_dir / '.env'
        if not env_path.exists():
            env_path = base_dir.parent / '.env'
        
        print(f"Looking for .env file at: {env_path}")
        print(f".env file exists: {env_path.exists()}")
        
        # Load environment variables
        load_dotenv(env_path)
        
        # Get API key
        api_key = os.getenv('OPENWEATHER_API_KEY')
        if not api_key:
            raise ValueError("OPENWEATHER_API_KEY not found in environment variables")
        
        print("API key loaded successfully")
        
        return {
            'OPENWEATHER_API_KEY': api_key,
            'DATABASE_NAME': 'weather.db'
        }
        
    except Exception as e:
        print(f"Error in config setup: {str(e)}")
        raise

# Load configuration
try:
    config = setup_config()
    OPENWEATHER_API_KEY = config['OPENWEATHER_API_KEY']
    DATABASE_NAME = config['DATABASE_NAME']
except Exception as e:
    print(f"Failed to load configuration: {str(e)}")
    raise 