import matplotlib.pyplot as plt


def plot_data_stream(history, anomalies, title):
    """
    Visualize the data stream and anomalies.

    Args:
    - history (numpy array): Previous data points.
    - anomalies (list of tuples): Detected anomalies with their index and value.
    - title (str): Title of the plot.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(history, label="Data Stream")

    # Highlight anomalies
    if anomalies:
        anomaly_indices, anomaly_values = zip(*anomalies)
        plt.scatter(anomaly_indices, anomaly_values, color="red", label="Anomalies")

    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.title(title)
    plt.legend()
    plt.show()
