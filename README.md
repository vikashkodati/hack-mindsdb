---
title: Terrasentinels
emoji: 📚
colorFrom: pink
colorTo: yellow
sdk: streamlit
sdk_version: 1.38.0
app_file: app.py
pinned: false
---

# Data Fetcher AI Agent

This Streamlit app simulates fetching Sentinel-2 satellite imagery data and storing it in a PostgreSQL database. It's designed to demonstrate the process of data collection and storage for further analysis using tools like MindsDB for anomaly detection.

## Features

- Input your OpenAI API key securely
- Input geographical coordinates (latitude and longitude)
- Specify date range for data collection
- Simulate data storage in PostgreSQL
- Prepare data for analysis with MindsDB

## How to Use

1. Enter your OpenAI API key in the sidebar (this is required to run the app)
2. Enter your Earth Engine Project ID (or use the default)
3. Input the latitude and longitude of your area of interest
4. Select the start and end dates for your data collection period
5. Provide a name for your image
6. Click "Fetch Sentinel-2 Image" to simulate the data collection and storage process

## Security Note

Your API key is not stored and is only used for the current session. It's securely handled and not displayed after entry.

## Note

This app is a simulation and does not actually connect to Earth Engine or store data in PostgreSQL. It's designed to demonstrate the user interface and workflow of such a system.

## Future Improvements

- Implement actual connection to Earth Engine
- Set up real-time data storage in PostgreSQL
- Integrate MindsDB for anomaly detection and data analysis

Feel free to contribute to this project or use it as a starting point for your own data analysis workflows!