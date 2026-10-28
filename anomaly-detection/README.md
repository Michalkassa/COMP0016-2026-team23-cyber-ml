# Anomaly detection

Does TabPFN find malicious log activity better than standard detectors?

| Step | Output |
|---|---|
| 1. Load + label data | Clean dataset, splits (prefer time-based) |
| 2. Baselines | Logistic regression, random forest / XGBoost, Isolation Forest |
| 3. TabPFN | Same splits and features |
| 4. Freeze protocol | Metrics and thresholds fixed before test |
| 5. Evaluate | Recall at agreed false-alert rate, PR-AUC, uncertainty, compute cost |

Data: [../data](../data/DATACARD-wendover.md) (`../scripts/fetch_data.sh`).
