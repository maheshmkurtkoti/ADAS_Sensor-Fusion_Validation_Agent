import numpy as np

DIST_THRESHOLD = 2.0

def match_and_evaluate(lidar, fusion):
    TP, FP, FN = 0, 0, 0
    errors = []

    for frame_lidar, frame_fusion in zip(lidar, fusion):
        matched = set()

        for l in frame_lidar:
            found = False

            for i, f in enumerate(frame_fusion):
                dist = np.linalg.norm(np.array(l) - np.array(f))

                if dist < DIST_THRESHOLD and i not in matched:
                    TP += 1
                    errors.append(dist)
                    matched.add(i)
                    found = True
                    break

            if not found:
                FN += 1

        FP += len(frame_fusion) - len(matched)

    mean_error = np.mean(errors) if errors else 0

    return TP, FP, FN, mean_error