# NDVI Anomaly Detection Project

This project is focused on detecting anomalies in satellite telemetry data (NDVI) using Sentinel Hub for data fetching and MindsDB for anomaly detection. The project includes scripts to fetch, analyze, and train models on NDVI data for anomaly detection.

## Project Overview

### Objective
The goal of this project is to retrieve NDVI (Normalized Difference Vegetation Index) data from satellite imagery and detect potential anomalies using statistical analysis and machine learning models.

### Workflow
1. **Fetch NDVI Data**: Retrieve NDVI data from Sentinel Hub.
2. **Analyze NDVI Data**: Preprocess and calculate statistical metrics on the fetched NDVI data.
3. **Train Anomaly Detection Model**: Train a machine learning model using MindsDB to detect anomalies in the NDVI data.

---

## Directory Structure

```
hack-mindsdb/
│
├── .venv/                  # Python virtual environment
├── docs/                   # Documentation and related files
├── others/                 # Scripts not directly related to anomaly detection
│
├── .env                    # Environment variables for API keys and credentials
├── fetch_ndvi_data.py       # Script to fetch NDVI data from Sentinel Hub
├── analyze_ndvi_data.py     # Script to preprocess and analyze the NDVI GeoTIFF data
├── train_ndvi_anomaly_model.py # Script to train a MindsDB model for anomaly detection
├── ndvi_output.tiff         # Example NDVI GeoTIFF output
├── requirements.txt         # Python package dependencies
├── README.md                # Project documentation (this file)
└── LICENSE                  # Project license
```

---

## Scripts and Their Purposes

### 1. `fetch_ndvi_data.py`
This script is responsible for fetching NDVI data from the Sentinel Hub API. It uses the Sentinel Hub Process API to retrieve satellite imagery, calculate NDVI values, and save the output as a GeoTIFF file.

**Usage**:
- Set up the `.env` file with your Sentinel Hub credentials.
- Run the script to fetch NDVI data for a given region and time range.

### 2. `analyze_ndvi_data.py`
This script preprocesses and analyzes the NDVI data saved in the GeoTIFF format. It calculates basic statistics such as mean and standard deviation, and identifies potential anomalies using z-scores.

**Usage**:
- Run the script after fetching NDVI data to analyze it and detect initial anomalies.

### 3. `train_ndvi_anomaly_model.py`
This script trains a MindsDB model to detect anomalies in the NDVI data. It uses the data processed by the `analyze_ndvi_data.py` script and trains a model capable of detecting more complex patterns of anomalies.

**Usage**:
- Use this script to train an anomaly detection model on the preprocessed NDVI data and make predictions on new data.

---

## How to Set Up and Run the Project

### 1. Set Up the Environment
- Clone the repository:
  ```bash
  git clone https://github.com/your-repo/hack-mindsdb.git
  cd hack-mindsdb
  ```

- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

- Set up the `.env` file with your API keys and credentials:
  ```
  SENTINELHUB_CLIENT_ID=your_client_id
  SENTINELHUB_CLIENT_SECRET=your_client_secret
  EARTHDATA_API_KEY=your_nasa_earthdata_key
  ```

### 2. Fetch NDVI Data
Run the `fetch_ndvi_data.py` script to fetch NDVI data from Sentinel Hub:
```bash
python fetch_ndvi_data.py
```

### 3. Analyze NDVI Data
After fetching the NDVI data, analyze it using the `analyze_ndvi_data.py` script:
```bash
python analyze_ndvi_data.py
```

### 4. Train MindsDB Anomaly Detection Model
Train the MindsDB anomaly detection model on the NDVI data:
```bash
python train_ndvi_anomaly_model.py
```

---

## Future Work
- Implement real-time anomaly detection by integrating periodic data fetching and model prediction.
- Extend the project to detect more types of anomalies beyond NDVI-based vegetation health metrics.
- Integrate NASA EarthData API to supplement the NDVI data with additional satellite data.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
```