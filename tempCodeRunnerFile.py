import random
import math
import numpy as np
from sklearn.ensemble import IsolationForest


# Function to generate data points
def generate_data_point(t):
    """
    Generate a simulated data point with regular pattern, noise, and occasional anomalies.
    """
    pattern = 10 * math.sin(t * 0.1)  # Regular wave pattern
    noise = random.uniform(-1, 1)  # Small random noise
    anomaly = 0

    # Randomly introduce large anomalies (rare spikes)
    if random.uniform(0, 1) > 0.98:
        anomaly = random.uniform(10, 20)  # Big spikes for anomalies

    return pattern + noise + anomaly  # Final data point


# Function to simulate a stream of data
def generate_data_stream(num_samples):
    """
    Generate a fixed number of data points in a simulated real-time data stream.
    """
    data = []
    for t in range(num_samples):
        data.append(generate_data_point(t))
    return np.array(data).reshape(-1, 1)  # Reshape for sklearn


# Moving average anomaly detection
def detect_anomaly_moving_average(value, history, window=5, threshold=2.0):
    """
    Detect anomaly in the data stream using moving average.

    Args:
    - value (float): Current value from the data stream.
    - history (list of float): Previous data points.
    - window (int): Number of points to consider for the moving average.
    - threshold (float): Deviation threshold to consider an anomaly.

    Returns:
    - bool: True if the value is an anomaly, False otherwise.
    """
    # If we don't have enough data yet, skip checking
    if len(history) < window:
        return False

    # Calculate moving average
    moving_avg = sum(history[-window:]) / window
    deviation = abs(value - moving_avg)  # How far the value is from average

    return deviation > threshold  # Return True if the value is an anomaly


# Number of samples to generate
num_samples = 1000

# Generate synthetic data
data = generate_data_stream(num_samples)

# Moving average anomaly detection
history = []
anomalies_moving_avg = []
for i in range(num_samples):
    value = data[i][0]  # Get the next data point
    history.append(value)  # Add to history

    # Detect if this value is an anomaly
    is_anomaly = detect_anomaly_moving_average(value, history)

    if is_anomaly:
        anomalies_moving_avg.append(value)

print("\n--- Moving Average Anomaly Detection ---")
print(f"Total anomalies detected by Moving Average: {len(anomalies_moving_avg)}")
print("Anomalies detected:")
for anomaly in anomalies_moving_avg:
    print(anomaly)

# Apply Isolation Forest
iso_forest = IsolationForest(
    contamination=0.05
)  # Adjust contamination as per expected anomaly rate

# Fit model
iso_forest.fit(data)

# Predict anomalies
predictions = iso_forest.predict(data)

# Convert predictions to boolean (1 for anomaly, -1 for normal)
anomalies_iforest = data[predictions == -1]

print("\n--- Isolation Forest Anomaly Detection ---")
print(f"Total anomalies detected by Isolation Forest: {len(anomalies_iforest)}")
print("Anomalies detected:")
for anomaly in anomalies_iforest:
    print(anomaly[0])  # Print the value only
