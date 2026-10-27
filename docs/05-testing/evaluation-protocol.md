# Detection evaluation protocol

*Version 0.0 (draft) · **Freeze before inspecting any test-set result**. After freezing, any change needs a new version and a note in the change log (research brief §3).*

| Field | Value |
|---|---|
| Task (unit of analysis, target / anomaly definition) | |
| Dataset + version / hash | |
| Label definition and provenance | |
| Split strategy (prefer temporal / environment hold-out) | |
| Preprocessing (fit on train only) | |
| Excluded features (identifiers, leakage) | |
| Models compared + versions | |
| Tuning budget per model | |
| Threshold selection (on validation) | |
| **Primary metric:** recall at false-alert budget of … | |
| Secondary metrics (precision, PR-AUC, FPR, per-class, calibration) | |
| Uncertainty method (suited to dependent records) | |
| Seeds / repeats | |
| Compute and cost recording | |

## Pre-test checks

- [ ] Duplicates checked
- [ ] Identifier and target leakage checked
- [ ] Class imbalance documented
- [ ] Label provenance documented

## Change log

| Version | Date | Change | Reason | Frozen? |
|---|---|---|---|---|
