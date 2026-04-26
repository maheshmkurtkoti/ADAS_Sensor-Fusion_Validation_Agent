# ADAS_Sensor-Fusion_Validation_Agent
Validation Agent to validate the performance of Sensor Fusion(RADAR and CAMERA) with Ground truth data as LIDAR

# Fusion Validation Agent

This project simulates and validates sensor fusion (Radar + Camera) using Lidar as ground truth.

## Features
- Frame-level comparison (400 frames)
- TP / FP / FN computation
- Position error calculation
- Time synchronization detection
- Explainable insights (agent-based)

## Scenarios
- Normal
- False Positives
- False Negatives
- Time Delay

## How to run
```bash
python main.py
