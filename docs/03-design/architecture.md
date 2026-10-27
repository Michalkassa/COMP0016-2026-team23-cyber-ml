# System architecture

*Version 0.0 (template) · Last updated: YYYY-MM-DD*. Fill in once requirements are agreed. Each major choice links to a [decision record](decisions/).

## Context

*(who/what interacts with the system; a context diagram)*

## Components

| Component | Responsibility | Code location | Status |
|---|---|---|---|
| Data ingestion & preparation | | `src/cyberml/data.py` | |
| Feature engineering | | `src/cyberml/features/` | |
| Detection models (baselines, foundation model) | | `src/cyberml/models/` | |
| Evaluation & metrics | | `src/cyberml/metrics.py` | |
| Agentic system | | `src/cyberml/agent/` | |
| Demonstrator / UI | | | |

## Data flow

*(diagram: dataset → preparation → scoring → analyst-facing result)*

## Deployment view

*(local / UCL GPU / Azure / Fabric; mark what is **working** vs **illustrative**)*

## Security and privacy considerations

## Change log

| Version | Date | Change |
|---|---|---|
