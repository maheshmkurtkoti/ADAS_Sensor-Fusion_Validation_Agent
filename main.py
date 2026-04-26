from simulation import generate_data
from validation import match_and_evaluate
from agent import generate_insights
from visualization import visualize
from visualization import animate_frames

mode =  "normal"  # change here "normal" "false_positive" "false_negative" "time_delay"

lidar, fusion, timestamps = generate_data(mode)

TP, FP, FN, error = match_and_evaluate(lidar, fusion)

print(f"TP: {TP}, FP: {FP}, FN: {FN}")
print(f"Mean Position Error: {error:.2f}")

print(f"FP Rate: {FP/(TP+FP+FN):.2f}")
print(f"FN Rate: {FN/(TP+FP+FN):.2f}")

generate_insights(TP, FP, FN, mode)

#visualize(lidar, fusion)

animate_frames (lidar, fusion, TP, FP, FN)