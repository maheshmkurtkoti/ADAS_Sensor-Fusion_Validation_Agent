import numpy as np

NUM_FRAMES = 400
NUM_OBJECTS = 3

def generate_data(mode="normal"):
    lidar_data = []
    fusion_data = []
    timestamps = []

    for t in range(NUM_FRAMES):
        frame_lidar = []
        frame_fusion = []

        time = t * 0.05  # 50ms cycle
        timestamps.append(time)

        for obj_id in range(NUM_OBJECTS):
            x = t * 0.1 + np.random.uniform(-2, 2) + obj_id * 3
            y = obj_id * 2 + np.random.uniform(-1, 1)

            # Lidar (ground truth)
            frame_lidar.append([x, y])

            # Fusion (noisy)
            fx = x + np.random.randn() * 0.5
            fy = y + np.random.randn() * 0.5
            frame_fusion.append([fx, fy])

        # --------- SCENARIOS ----------
        if mode == "false_positive":
            frame_fusion.append([
                np.random.uniform(0, 50),
                np.random.uniform(0, 10)
            ])

        if mode == "false_negative":
            if len(frame_fusion) > 0:
                frame_fusion.pop()

        if mode == "time_delay":
            if t > 2:
                delayed_frame = lidar_data[t - 2]

                frame_fusion = []
                for x, y in delayed_frame:
                    fx = x + np.random.randn() * 0.5
                    fy = y + np.random.randn() * 0.5
                    frame_fusion.append([fx, fy])

        # --------------------------------

        lidar_data.append(frame_lidar)
        fusion_data.append(frame_fusion)

    return lidar_data, fusion_data, timestamps