import numpy as np
from detection import (
    generate_data_point,
    detect_anomaly_moving_average,
    detect_anomaly_isolation_forest,
)
from visualization import plot_data_stream


def main(visualize=False):
    history = []
    anomalies_moving_average = []
    anomalies_isolation_forest = []

    # Create a data stream generator
    t = 0
    while t < 100:  # Run for 100 time steps
        value = generate_data_point(t)
        history.append(value)

        # Detect anomalies using Moving Average
        is_anomaly_moving_average = detect_anomaly_moving_average(value, history)
        if is_anomaly_moving_average:
            anomalies_moving_average.append((t, value))  # Include index and value

        t += 1

    # Convert lists to numpy arrays
    history_np = np.array(history)

    # Detect anomalies using Isolation Forest
    anomalies_isolation_forest = detect_anomaly_isolation_forest(history_np)

    # Format anomalies for Isolation Forest
    anomalies_isolation_forest_formatted = [
        (i, history_np[i])
        for i in range(len(history_np))
        if anomalies_isolation_forest[i]
    ]

    # Print results
    print("\n--- Moving Average Anomaly Detection ---")
    print(
        f"Total anomalies detected by Moving Average: {len(anomalies_moving_average)}"
    )
    print("Anomalies detected:")
    print(anomalies_moving_average)

    print("\n--- Isolation Forest Anomaly Detection ---")
    print(
        f"Total anomalies detected by Isolation Forest: {len(anomalies_isolation_forest_formatted)}"
    )
    print("Anomalies detected:")
    print(anomalies_isolation_forest_formatted)

    # Visualize results if flag is set
    if visualize:
        plot_data_stream(history_np, anomalies_moving_average, "Moving Average")
        plot_data_stream(
            history_np, anomalies_isolation_forest_formatted, "Isolation Forest"
        )


if __name__ == "__main__":
    import sys

    # Check if visualize flag is passed as a command-line argument
    visualize = "--visualize" in sys.argv
    main(visualize)
