import matplotlib.pyplot as plt
import numpy as np

def visualize(lidar, fusion, frame_id=50):
    l = np.array(lidar[frame_id])
    f = np.array(fusion[frame_id])

    plt.figure()

    if len(l) > 0:
        plt.scatter(l[:, 0], l[:, 1], label="Lidar (GT)", marker='o')

    if len(f) > 0:
        plt.scatter(f[:, 0], f[:, 1], label="Fusion", marker='x')

    plt.title(f"Frame {frame_id}")
    plt.legend()
    plt.grid()
    plt.show()

    
def animate_frames(lidar, fusion, TP, FP, FN):
    plt.ion()
    fig, ax = plt.subplots()
    for frame_id in range(len(lidar)):
        ax.clear()
        l = np.array(lidar[frame_id])
        f = np.array(fusion[frame_id])
        if len(l) > 0:
            ax.scatter(l[:, 0], l[:, 1], label="Lidar (GT)", marker='o')
        if len(f) > 0:
            ax.scatter(f[:, 0], f[:, 1], label="Fusion", marker='x')
        ax.set_title(f"Frame {frame_id}")
        ax.legend()
        ax.grid()
        # Show metrics on plot
        text = f"TP: {TP}  FP: {FP}  FN: {FN}"
        ax.text(0.02, 0.95, text, transform=ax.transAxes)
        plt.pause(0.05)
    plt.ioff()
    plt.show()