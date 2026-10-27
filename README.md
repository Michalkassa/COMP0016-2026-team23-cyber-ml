# Generative Data Science for Cybersecurity

**COMP0016 Systems Engineering 2026–27 · Team 23 · Industry partner: Avanade (via UCL IXN)**

## Problem statement

Security teams want to know if newer AI tools (generative assistants, agentic analysis systems and tabular foundation models such as TabPFN) can find malicious behaviour in structured security logs better than established statistical and machine-learning methods. They also need to know where these tools don't help.

This project will:

1. **Benchmark** a tabular foundation model against established baselines on one defensive detection task. The main metric is recall at an agreed false-alert budget, reported with uncertainty and compute cost.
2. **Build and evaluate** a prototype *Agentic Meta-Statistician*. This is a small, human-supervised team of AI roles that helps a cybersecurity modeller frame a problem, check the data, run approved experiments and review the statistical reasoning.
3. **Demonstrate** the analysis journey on Azure / Microsoft Fabric and turn the findings into a recommendation for a possible Avanade accelerator offering.

A negative or inconclusive result counts as a valid outcome if it is reproducible. Full brief: [docs/00-project/research-brief.md](docs/00-project/research-brief.md) · Abstract: [docs/00-project/abstract.md](docs/00-project/abstract.md)

> **Status:** Term 1, requirements and design phase. Requirements to be captured from the client kick-off call (2026-10-27). See the [schedule](docs/00-project/schedule.md) and the latest [weekly progress](project-management/weekly-progress/).

## For the client and reviewers: start here

| You want to… | Go to |
|---|---|
| Understand the project and what was agreed | [Specification](docs/00-project/specification.md) · [Requirements](docs/02-requirements/requirements.md) |
| See current progress | [Weekly progress](project-management/weekly-progress/) · [Sprints](project-management/sprints/) · [Builds](builds/CHANGELOG.md) |
| See what was decided and why | [Decision records](docs/03-design/decisions/) · [Client meeting minutes](project-management/meetings/client/) |
| See who is doing what | [Work packages](project-management/work-packages/register.md) · [Team](docs/01-team/team.md) |
| Check risks, ethics, data and IP | [Risk register](docs/06-governance/risk-register.md) · [Ethics & GDPR](docs/06-governance/ethics-gdpr.md) · [IP & licensing](docs/06-governance/ip-licensing.md) |
| Read the research evidence base | [Research wiki](research/wiki/index.md) |
| Run the code | [Getting started](#getting-started) below |

A full map of the documentation is in [docs/README.md](docs/README.md).

## Repository layout

```text
.
├── docs/                    Living project documentation (numbered by lifecycle stage)
│   ├── 00-project/          Brief, abstract, specification, module requirements, schedule
│   ├── 01-team/             Team, roles, communication, contributions, IBM SkillsBuild
│   ├── 02-requirements/     MoSCoW requirements, stakeholders, acceptance criteria
│   ├── 03-design/           Architecture and decision records (options compared)
│   ├── 04-research/         Literature review outputs (links into research/wiki)
│   ├── 05-testing/          Test strategy, frozen evaluation protocol, agent evaluation rubric
│   ├── 06-governance/       Risks, ethics/GDPR, IP & licensing, AI-use log
│   └── 07-handover/         Final hand-over checklist, user and deployment manuals
├── project-management/      The audit trail: weekly progress, meetings, sprints, work packages, agreements
├── media/                   Dev blog, monthly videos, presentations (elevator pitch, final)
├── website/                 Source and plan for the project report website (40% component)
├── builds/                  Fortnightly demo builds and their changelog
├── research/                Source-grounded research wiki (+ raw captures where allowed)
├── templates/               All document templates; copy them, never edit in place
├── src/cyberml/             Python package: data loading, features, models, metrics, agent
├── tests/                   Unit and integration tests (pytest)
├── experiments/             Experiment configs and small result artefacts
├── notebooks/               Exploratory notebooks (not the source of truth for results)
├── data/                    Datacards and access instructions only; raw data is git-ignored
└── scripts/                 Helper scripts (e.g. fetching data)
```

## Getting started

Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/) (or plain `pip`).

```bash
# 1. Install the package with dev tools
uv venv && source .venv/bin/activate
uv pip install -e ".[dev]"

# 2. Get the dataset (not committed, see data/README.md)
./scripts/fetch_data.sh                # clones from the upstream repo
# or: ./scripts/fetch_data.sh /path/to/ucl-cybersecurity-ml   (local copy)

# 3. Check everything works
pytest
ruff check .
```

## How we work

Read [CONTRIBUTING.md](CONTRIBUTING.md) before your first commit. It covers branching, pull requests, where each document goes, and the weekly and fortnightly routine that keeps this repo audit-ready.

## Team

See [docs/01-team/team.md](docs/01-team/team.md).

## Licence

To be confirmed with the academic supervisor and Avanade. See [LICENCE.md](LICENCE.md).
