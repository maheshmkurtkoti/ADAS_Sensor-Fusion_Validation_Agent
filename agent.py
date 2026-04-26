def generate_insights(TP, FP, FN, mode):
    total = TP + FP + FN
    fp_rate = FP / total if total else 0
    fn_rate = FN / total if total else 0

    print("\n--- INSIGHTS ---")

    if fp_rate > 0.2:
        print("⚠️ High False Positives → possible radar ghost / noise")

    if fn_rate > 0.2:
        print("⚠️ High False Negatives → possible occlusion / missed detection")

    if mode == "time_delay":
        print("⚠️ Time delay detected → synchronization issue")

    if fp_rate < 0.1 and fn_rate < 0.1:
        print("✅ Fusion performance looks stable")