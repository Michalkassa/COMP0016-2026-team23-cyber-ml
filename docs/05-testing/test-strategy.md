# Test strategy

*Version 0.0 (template) · Last updated: YYYY-MM-DD*

## Software testing

| Level | What | Tooling | Where | When run |
|---|---|---|---|---|
| Unit | Functions in `src/cyberml/` | pytest | `tests/` | Every PR (CI) |
| Integration | Pipeline end-to-end on a small fixture | pytest | `tests/integration/` | Every PR (CI) |
| Regression | Results of frozen configs don't drift unexpectedly | pytest + stored reference metrics | `tests/regression/` | Before each build tag |
| Functional / acceptance | Each requirement's acceptance criterion | Manual checklist + scripts | Table below | Each build / sign-off |
| Static checks | Lint, formatting | ruff | CI | Every PR |

## Acceptance test matrix

| Requirement ID | Acceptance criterion | Test (automated / manual) | Last result | Date |
|---|---|---|---|---|

## AI / model evaluation

- Detection models: see [evaluation-protocol.md](evaluation-protocol.md).
- Agentic system: see [agent-evaluation.md](agent-evaluation.md).
- **Checking AI-generated outputs:** generated code needs tests and review; generated claims need a cited source; record notable corrections in the [AI-use log](../06-governance/ai-usage-log.md).

## Test data

Use small synthetic or sanitised fixtures in `tests/fixtures/`. Never put real dataset extracts in tests.
