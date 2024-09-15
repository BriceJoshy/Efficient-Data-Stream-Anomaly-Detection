# Efficient Data Stream Anomaly Detection

## Project Overview

This project focuses on detecting anomalies in a continuous data stream using different anomaly detection techniques. The data stream is simulated to represent real-time sequences of floating-point numbers, which could correspond to various metrics such as financial transactions or system metrics.

## Project Objectives

1. **Algorithm Selection**: Implement and compare different algorithms for anomaly detection that can adapt to concept drift and seasonal variations.
2. **Data Stream Simulation**: Design a function to simulate a data stream with regular patterns, seasonal elements, and random noise.
3. **Anomaly Detection**: Develop mechanisms to detect anomalies in real-time as the data is streamed.
4. **Optimization**: Ensure that the algorithms are optimized for both speed and efficiency.
5. **Visualization**: Create a visualization tool to display both the data stream and any detected anomalies.

## Implementation

### Modules

1. **detection.py**: Contains functions for generating data points and detecting anomalies using different methods.

   - `generate_data_point(t)`: Simulates data points with regular patterns, noise, and occasional anomalies.
   - `detect_anomaly_moving_average(value, history, window=5, threshold=2.0)`: Anomaly detection using a moving average method.
   - `detect_anomaly_isolation_forest(data)`: Anomaly detection using Isolation Forest.

2. **visualization.py**: Contains functions for visualizing the data stream and detected anomalies.

   - `plot_data_stream(history, anomalies, title)`: Plots the data stream with highlighted anomalies.

3. **main.py**: The main script that integrates the above modules and performs the following:
   - Simulates a data stream.
   - Applies anomaly detection methods.
   - Visualizes the results if specified.

### Algorithms

1. **Z-score**:

   - **Description**: A statistical method that measures how many standard deviations a data point is from the mean. It assumes data follows a normal distribution.
   - **Advantages**: Simple and easy to implement.
   - **Limitations**: Assumes normal distribution, may not perform well with skewed or heavy-tailed distributions.

2. **Moving Average-Based Anomaly Detection**:

   - **Description**: Detects anomalies by comparing the current value to the moving average of previous values.
   - **Parameters**:
     - `window`: Number of previous values to include in the moving average (default: 10).
     - `threshold`: Amount of deviation to classify a value as an anomaly (default: 2.0).

3. **Isolation Forest**:
   - **Description**: A tree-based method that isolates anomalies instead of profiling normal data. It is efficient and works well with large datasets.
   - **Advantages**: Fast, accurate, works well with large datasets, memory efficient, and does not require feature scaling.
   - **Basic Idea**: Anomalous points are isolated faster, with fewer splits required to separate them from normal points.

## Requirements

- Python 3.x
- `numpy`
- `matplotlib`
- `scikit-learn`

To install the necessary packages, use:

```bash
pip install -r requirements.txt
```

## Usage

To run the project and visualize results, execute:

```bash
python main.py --visualize
```

To run without visualization, simply use:

```bash
python main.py
```
