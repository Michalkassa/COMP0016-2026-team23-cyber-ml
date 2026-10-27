# Experiments

Every result in the report must trace back to a **config + commit + dataset hash**.

- `configs/EXP-NNN-short-name.yaml`: committed; pins dataset version, model versions, seeds and protocol version.
- `results/EXP-NNN/`: committed **small** outputs (metrics JSON/CSV, figures, the [experiment record](../templates/experiment-record.md) as `README.md`).
- `runs/`: git-ignored scratch output, checkpoints and logs.

Negative and inconclusive results are kept. They are findings too.

| ID | Title | Owner | Protocol version | Status |
|---|---|---|---|---|
