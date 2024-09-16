import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get Sentinel Hub credentials and token from environment variables
client_id = os.getenv("SENTINELHUB_CLIENT_ID")
client_secret = os.getenv("SENTINELHUB_CLIENT_SECRET")
access_token = os.getenv("SENTINELHUB_ACCESS_TOKEN")

# Sentinel Hub Process API endpoint
url = 'https://services.sentinel-hub.com/api/v1/process'

# Example request payload (replace the bounding box coordinates with your area of interest)
payload = {
    "input": {
        "bounds": {
            "properties": {
                "crs": "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [
                            -94.04798984527588,
                            41.7930725281021
                        ],
                        [
                            -94.04803276062012,
                            41.805773608962869
                        ],
                        [
                            -94.06738758087158,
                            41.805901566741308
                        ],
                        [
                            -94.06734466552735,
                            41.7967199475024
                        ],
                        [
                            -94.06223773956299,
                            41.79144072064381
                        ],
                        [
                            -94.0504789352417,
                            41.791376727347969
                        ],
                        [
                            -94.05039310455322,
                            41.7930725281021
                        ],
                        [
                            -94.04798984527588,
                            41.7930725281021
                        ]
                    ]
                ]
            }
        },
        "data": [
            {
                "type": "sentinel-2-l2a",
                "dataFilter": {
                    "timeRange": {
                        "from": "2022-10-01T00:00:00Z",
                        "to": "2022-10-31T23:59:59Z"
                    }
                },
                "processing": {
                    "harmonizeValues": True
                }
            }
        ]
    },
    "output": {
        "width": 512,
        "height": 512,
        "responses": [
            {
                "identifier": "default",
                "format": {
                    "type": "image/tiff"
                }
            }
        ]
    }
}

# Sentinel Hub Evalscript (NDVI calculation)
evalscript = """
//VERSION=3
function setup() {
    return {
        input: [{
            bands: ["B04", "B08"],
            units: "REFLECTANCE"
        }],
        output: {
            id: "default",
            bands: 1,
            sampleType: SampleType.FLOAT32
        }
    };
}

function evaluatePixel(sample) {
    let ndvi = (sample.B08 - sample.B04) / (sample.B08 + sample.B04);
    return [ndvi];
}
"""

headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

# Send the request to Sentinel Hub Process API
response = requests.post(url, headers=headers, json={
    'input': payload['input'],
    'output': payload['output'],
    'evalscript': evalscript
})

# Handle the response
if response.status_code == 200:
    print("Data fetched successfully!")
    with open('ndvi_output.tiff', 'wb') as f:
        f.write(response.content)
else:
    print(f"Error fetching data: {response.status_code}, {response.text}")