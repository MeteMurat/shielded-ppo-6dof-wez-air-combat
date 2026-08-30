
import numpy as np
import matplotlib.pyplot as plt
import os

def find_latest_metrics_file():
    for root, dirs, files in os.walk('.'):
        for file in sorted(files):
            if file.endswith('_metrics.npz'):
                return os.path.join(root, file)
    return None

def plot_metrics(file_path):
    data = np.load(file_path)
    ata = data['ata']
    distance = data['distance']
    mach = data['mach']
    height = data['height']
    time_steps = np.arange(len(ata))

    # ATA vs Distance
    fig1, ax1 = plt.subplots()
    ax1.plot(time_steps, ata, label="ATA (deg)", color="blue")
    ax1.set_ylabel("ATA (deg)", color="blue")
    ax1.set_xlabel("Timestep")
    ax1.tick_params(axis='y', labelcolor="blue")

    ax2 = ax1.twinx()
    ax2.plot(time_steps, distance, label="Distance (m)", color="red")
    ax2.set_ylabel("Distance (m)", color="red")
    ax2.tick_params(axis='y', labelcolor="red")
    plt.title("ATA vs Distance")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Mach vs Height
    fig2, ax3 = plt.subplots()
    ax3.plot(time_steps, mach, label="Mach", color="green")
    ax3.set_ylabel("Mach", color="green")
    ax3.set_xlabel("Timestep")
    ax3.tick_params(axis='y', labelcolor="green")

    ax4 = ax3.twinx()
    ax4.plot(time_steps, height, label="Height (ft)", color="orange")
    ax4.set_ylabel("Height (ft)", color="orange")
    ax4.tick_params(axis='y', labelcolor="orange")
    plt.title("Mach vs Height")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    file_path = find_latest_metrics_file()
    if file_path:
        print(f"Plotting metrics from: {file_path}")
        plot_metrics(file_path)
    else:
        print("No episode_*_metrics.npz file found.")
