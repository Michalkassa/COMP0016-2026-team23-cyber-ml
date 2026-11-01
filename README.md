# Generative Data Science for Cybersecurity

COMP0016 2026–27 · Team 23 · Avanade

Benchmark a tabular foundation model (TabPFN) against standard detectors on security logs, build a human-supervised AI assistant for modellers, demo it on Azure/Fabric, and recommend whether Avanade should pursue it.

## Where to find things

**The project**
- [Specification](SPECIFICATION.md): partner, scope, requirements, constraints, data, ethics, IP
  - [Requirements](SPECIFICATION.md#detailed-requirements) · [Stretch](SPECIFICATION.md#stretch-requirements) · [Out of scope](SPECIFICATION.md#out-of-scope) · [Acceptance criteria](SPECIFICATION.md#acceptance-criteria)
- [Anomaly detection](anomaly-detection/README.md): does TabPFN beat standard detectors?
  - [Dataset card](anomaly-detection/data/DATACARD-wendover.md)
- [Meta-statistician](metastatician/README.md): does an AI assistant improve the modeller's analysis?
- [Client brief and research wiki](https://github.com/elikling/ucl-cybersecurity-ml)

**Tracking** ([LOG.md](LOG.md))
- [Meetings and weekly progress](LOG.md#meetings-and-weekly-progress)
- [Work packages](LOG.md#work-packages)
- [Deliverables: builds, videos, submissions](LOG.md#deliverables)
- [Decisions](LOG.md#decisions) · [Risks](LOG.md#risks)
- [Contributions](LOG.md#contributions-everyone-weekly) · [AI use](LOG.md#ai-use)

**Templates** ([TEMPLATES.md](TEMPLATES.md))
- [Meeting minutes](TEMPLATES.md#meeting-minutes) · [Work package](TEMPLATES.md#work-package) · [Biweekly build](TEMPLATES.md#biweekly-build) · [Monthly video](TEMPLATES.md#monthly-video) · [Website report](TEMPLATES.md#website-report)

**Repo**
- [Licence](LICENCE.md) · [PR template](.github/pull_request_template.md) · [CI](.github/workflows/ci.yml) · [Environment variables](.env.example)

## Timeline

Every two weeks: runnable build demoed to the client. Monthly: progress video to the supervisor.

| When | Do | Where | Graded |
|---|---|---|---|
| ✅ 27 Oct | Client introduction, initial ideas and requirements | [Meetings](LOG.md#meetings-and-weekly-progress) | |
| **→ Now** | Team drafts the requirements | [Requirements](SPECIFICATION.md#detailed-requirements) | |
| Before 9 Nov | Email requirements to the client for approval | [Specification](SPECIFICATION.md) | |
| **9 Nov 16:00** | Client approves → requirements sealed (approval email logged) | [Decisions](LOG.md#decisions) | |
| After approval | Video presenting the agreed requirements | [Video template](TEMPLATES.md#monthly-video) · [Deliverables](LOG.md#deliverables) | |
| Nov | Submit requirements & design | [Specification](SPECIFICATION.md) | **5%** |
| Nov–Dec | Data + baselines + TabPFN + agent v1 → **Prototype 1** | [Anomaly detection](anomaly-detection/README.md) · [Meta-statistician](metastatician/README.md) | |
| Jan, term 2 week 1 | Prototype 1 demoed to client | [Deliverables](LOG.md#deliverables) | |
| 22 Jan | Elevator pitch | [Deliverables](LOG.md#deliverables) | **5%** |
| Jan–Feb | Full benchmark, agent evaluation, Azure demo → **Prototype 2**; IP and GDPR update | [IP](SPECIFICATION.md#ip-and-licensing) · [GDPR](SPECIFICATION.md#ethical-approval-and-gdpr-compliance) | |
| 12 Mar | Development stops; testing, deployment, hand-over materials | [Hand-over](SPECIFICATION.md#code-hosting-and-hand-over) | |
| 16 Mar | Showcase | | |
| 20 Mar | Website report finished; client hand-over | [Website report](TEMPLATES.md#website-report) | |
| **24 Mar 16:00** | Submit website report + system artefacts | [Deliverables](LOG.md#deliverables) | **40% + 50%** |

## Grade rules

1. Everyone codes, writes website sections and talks to the client, using their own git account.
2. Every agreement goes in writing (email) and is logged.
3. Compare 3+ options for every major decision.
4. Report honest results with uncertainty; label anything illustrative.
5. Keep every build runnable; cite sources and AI use.
