import random
import math
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


# Moving average anomaly detection
def detect_anomaly_moving_average(value, history, window=5, threshold=2.0):
    """
    Detect anomaly in the data stream using moving average.
    """
    if len(history) < window:
        return False

    moving_avg = sum(history[-window:]) / window
    deviation = abs(value - moving_avg)

    return deviation > threshold


# Isolation Forest anomaly detection
def detect_anomaly_isolation_forest(data):
    """
    Detect anomalies in the data using Isolation Forest.
    """
    # Prepare data for Isolation Forest
    data_reshaped = [[x] for x in data]
    model = IsolationForest(contamination=0.05)  # Assuming 5% contamination
    model.fit(data_reshaped)
    predictions = model.predict(data_reshaped)

    # -1 for anomalies, 1 for normal points
    return [pred == -1 for pred in predictions]
