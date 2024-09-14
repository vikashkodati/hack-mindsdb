import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get Sentinel Hub credentials from environment variables
client_id = os.getenv("SENTINELHUB_CLIENT_ID")
client_secret = os.getenv("SENTINELHUB_CLIENT_SECRET")

# Sentinel Hub token endpoint
url = "https://services.sentinel-hub.com/oauth/token"

# Data for requesting the access token
data = {
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'client_credentials'
}

# Send the request to get the access token
response = requests.post(url, data=data)

# Check if the request was successful
if response.status_code == 200:
    token = response.json()['access_token']
    print(f"Access Token: {token}")
else:
    print(f"Error: {response.status_code}, {response.text}")
