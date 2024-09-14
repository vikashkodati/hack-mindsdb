import rasterio
import numpy as np
from scipy import stats

# Open the GeoTIFF file
with rasterio.open('ndvi_output.tiff') as src:
    ndvi_data = src.read(1)  # Read the first band

    # Mask out no-data values
    ndvi_data = np.ma.masked_equal(ndvi_data, src.nodata)

# Filter out invalid NDVI values (NDVI should be between -1 and 1)
valid_ndvi = ndvi_data[(ndvi_data >= -1) & (ndvi_data <= 1)]

# Check if we have valid NDVI data
if valid_ndvi.size > 0:
    # Calculate basic statistics
    mean_ndvi = np.mean(valid_ndvi)
    std_ndvi = np.std(valid_ndvi)
    z_scores = stats.zscore(valid_ndvi)

    # Identify potential anomalies (e.g., NDVI values more than 2 standard deviations from the mean)
    anomalies = np.abs(z_scores) > 2

    # Print results
    print(f"Mean NDVI: {mean_ndvi:.4f}")
    print(f"NDVI Standard Deviation: {std_ndvi:.4f}")
    print(f"Number of potential anomalies: {np.sum(anomalies)}")
    print(f"Percentage of anomalies: {(np.sum(anomalies) / len(valid_ndvi)) * 100:.2f}%")
else:
    print("No valid NDVI data found.")
