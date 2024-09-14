import requests
import os
from dotenv import load_dotenv

load_dotenv()

# NASA EarthData API URL
url = 'https://api.nasa.gov/planetary/earth/assets'

# Replace with your NASA API key
params = {
    'lon': longitude,  # Longitude of the area
    'lat': latitude,   # Latitude of the area
    'dim': 0.1,        # Dimension of the area
    'date': '2024-01-01',  # Date for the satellite data
    'api_key': os.environ.get('EARTHDATA_API_KEY')
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print("Satellite data fetched successfully!")
    print(data)
else:
    print(f"Failed to fetch data: {response.status_code}")
