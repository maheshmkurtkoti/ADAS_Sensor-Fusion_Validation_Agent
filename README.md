# ADAS Sensor Fusion Validation Agent

A simulation-based validation framework for evaluating **Radar + Camera sensor fusion performance** against **Lidar ground truth** in an ADAS environment.

This project models how real automotive perception stacks are evaluated using frame-level sensor logs and KPI-based validation metrics.

---

## 🧠 Problem Statement

In modern ADAS systems, multiple sensors (Radar, Camera) are fused to detect and track objects around the vehicle.

However, fusion outputs can suffer from:
- False detections (ghost objects)
- Missed detections
- Position inaccuracies
- Sensor time synchronization issues

This project builds a **validation layer** to evaluate fusion quality against Lidar ground truth.

---

## ⚙️ What This System Does

The agent simulates and evaluates sensor fusion performance by:

- Comparing **Fusion output (Radar + Camera)** with **Lidar ground truth**
- Performing **frame-by-frame matching across 400+ frames**
- Computing ADAS KPIs:
  - True Positives (TP)
  - False Positives (FP)
  - False Negatives (FN)
- Estimating:
  - Mean position error (object-level deviation)
  - Temporal misalignment between sensors
- Generating **explainable insights (agent logic)** for system behavior

---

## 📊 Validation Logic

Each frame is treated as a perception cycle (~50ms).

The system evaluates:
- Object-level matching between Fusion and Lidar detections
- Spatial deviation using Euclidean distance
- Missed and spurious detections
- Temporal inconsistencies across sensor streams

---

## 🧪 Scenarios Simulated

To test robustness of fusion systems:

- **Normal Condition**
  - Stable fusion with aligned sensors

- **False Positive Scenario**
  - Radar noise / ghost detections

- **False Negative Scenario**
  - Missed objects due to occlusion or weak detection

- **Time Synchronization Issue**
  - Misaligned timestamps between sensors affecting fusion quality

---

## 📈 Outputs Generated

For each scenario, the system generates:

- KPI metrics:
  - TP / FP / FN counts
  - Normalized rates (%)
  - Mean position error (meters & cm)

- Worst-case frame detection:
  - Frame with maximum deviation

- Explainable AI-style insights:
  - Human-readable diagnostic reasoning

- Visualization-ready JSON outputs:
  - Used directly by frontend dashboard

---

## 🧠 Key Insight

This project mimics a simplified **ADAS validation pipeline** used in automotive engineering:

> Sensor logs → Fusion output → Ground truth comparison → KPI evaluation → System health interpretation

---

## 🛠 Tech Stack

- Python
- NumPy
- Matplotlib
- Custom simulation engine for sensor logs

---

## ▶️ How to Run

```bash
python main.py
