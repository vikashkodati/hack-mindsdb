import rasterio
import numpy as np
import pandas as pd
import mindsdb
from datetime import timedelta, datetime
import mindsdb_sdk as mdb 

server = mdb.connect()  # Connects to the default port on localhost

# Step 1: Load the NDVI data from the GeoTIFF file
geotiff_file = 'ndvi_output.tiff'

with rasterio.open(geotiff_file) as src:
    ndvi_data = src.read(1)  # Read the first band (NDVI values)
    ndvi_data = np.ma.masked_equal(ndvi_data, src.nodata)  # Mask no-data values

# Step 2: Generate timestamps for each NDVI value (assuming daily data collection)
# Note: If your data doesn't have specific timestamps, we create mock timestamps for demonstration
# Here, we'll assume the data is for 30 days starting from a certain date
start_date = datetime(2024, 1, 1)  # Modify this based on the actual date range
timestamps = [start_date + timedelta(days=i) for i in range(ndvi_data.size)]

# Step 3: Flatten NDVI data and filter valid values
# NDVI is typically between -1 and 1, we'll filter any invalid values
valid_ndvi = ndvi_data[(ndvi_data >= -1) & (ndvi_data <= 1)].flatten()
valid_timestamps = np.array(timestamps[:valid_ndvi.size])  # Adjust timestamps to match valid NDVI data

# Step 4: Prepare the DataFrame with NDVI values and corresponding timestamps
ndvi_df = pd.DataFrame({
    'timestamp': valid_timestamps,
    'ndvi': valid_ndvi
})

# Step 5: Save the DataFrame to a CSV file (for learning and testing)
ndvi_df.to_csv('real_ndvi_data.csv', index=False)

# Step 6: Train an anomaly detection model using MindsDB
predictor = mdb.Predictor(name='ndvi_anomaly_detector')
predictor.learn(from_data='real_ndvi_data.csv', to_predict='ndvi')

# Step 7: Make predictions on the same dataset (for testing purposes)
results = predictor.predict(when_data='real_ndvi_data.csv')

# Step 8: Print the results (for debugging)
print("Anomaly Detection Results:")
print(results)
