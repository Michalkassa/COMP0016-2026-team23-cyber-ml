# Contributing and team workflow

This repo is shared with our client and is assessed (website report 40%, system artefacts 50%, both with an *individual contribution* coefficient). Everything we do should leave a clear trail: who did what, when, and why.

## Where things go

| Thing | Location | Template |
|---|---|---|
| Weekly in-lab TA progress check | `project-management/weekly-progress/YYYY-MM-DD-week-NN.md` | [templates/weekly-progress.md](templates/weekly-progress.md) |
| Client meeting (≈ fortnightly) | `project-management/meetings/client/YYYY-MM-DD.md` | [templates/meeting-minutes.md](templates/meeting-minutes.md) |
| TA / supervisor meeting | `project-management/meetings/supervisor/YYYY-MM-DD.md` | same |
| Internal team meeting | `project-management/meetings/team/YYYY-MM-DD.md` | same |
| Sprint plan + review | `project-management/sprints/sprint-NN.md` | [templates/sprint.md](templates/sprint.md) |
| Work package | Row in `project-management/work-packages/register.md` + `WP-NN-short-name.md` | [templates/work-package.md](templates/work-package.md) |
| Written agreement with client (email) | `project-management/agreements/YYYY-MM-DD-topic.md` | [templates/agreement-record.md](templates/agreement-record.md) |
| Design / technical decision (3+ options compared) | `docs/03-design/decisions/NNNN-title.md` | [templates/decision-record.md](templates/decision-record.md) |
| Experiment | `experiments/configs/EXP-NNN-*.yaml` + `experiments/results/EXP-NNN/` | [templates/experiment-record.md](templates/experiment-record.md) |
| Fortnightly demo build | Git tag `build-NN` + entry in `builds/CHANGELOG.md` | [templates/build-notes.md](templates/build-notes.md) |
| Dev blog post | `media/blog/YYYY-MM-DD-title.md` | [templates/blog-post.md](templates/blog-post.md) |
| Monthly progress video | Entry in `media/videos/README.md` (video file hosted elsewhere) | [templates/video-plan.md](templates/video-plan.md) |
| Material AI tool use | Row in `docs/06-governance/ai-usage-log.md` | — |
| New risk | Row in `docs/06-governance/risk-register.md` | — |

Use ISO dates (`YYYY-MM-DD`) in filenames and documents. Copy templates; never edit them in place, except to improve the template for everyone.

## Weekly and fortnightly routine

**Every week (before the Tuesday lab)**

- [ ] Weekly progress file written: done / doing / blocked, one line per person.
- [ ] Contributions log updated by each member ([docs/01-team/contributions.md](docs/01-team/contributions.md)).
- [ ] Risk register checked.

**Every two weeks (sprint boundary)**

- [ ] Sprint review and next sprint plan written.
- [ ] Work packages agreed with the TA and noted in the register: who, what, by when.
- [ ] Work-package summary emailed to the client ("Hi, we would like to update you on the next two weeks…") and recorded in `project-management/agreements/`.
- [ ] Demo build tagged and runnable by the client; `builds/CHANGELOG.md` updated.
- [ ] Client meeting minutes committed within 24 h.
- [ ] Dev blog post published.

**Every month**

- [ ] Team progress video recorded and sent to the primary supervisor; logged in `media/videos/README.md`.

## Git workflow

- `main` is always runnable and is what the client sees. **Don't push directly to `main`.**
- Branch per issue: `feat/<issue>-short-name`, `fix/…`, `docs/…`, `exp/…` (experiments).
- Open a PR using the template; **at least one other team member reviews** before merge. Reviewing counts as contribution, so do it properly.
- Small, descriptive commits in the imperative ("Add recall-at-FPR metric"). Each person commits their own work under their own GitHub account; this is part of how individual contribution is evidenced.
- Link PRs to issues (`Closes #12`) and issues to work packages (`WP-03`).
- Tag demo builds `build-01`, `build-02`, … on `main`.

## Code standards

- Python package lives in `src/cyberml/`; tests mirror it in `tests/`.
- `ruff check .` and `pytest` must pass (enforced by CI).
- Results that appear in the report come from **scripts + versioned configs**, not from notebook state.
- Pin dataset versions, model versions and random seeds in experiment configs.
- **Never commit:** raw or restricted data, secrets/API keys, `.env` files, large model weights, video files. Use `.env.example` for configuration keys.

## Data, security and AI use

- Treat log content as untrusted input. Don't send dataset contents to external AI services unless the client has approved it in writing.
- Don't commit personal data. See [docs/06-governance/ethics-gdpr.md](docs/06-governance/ethics-gdpr.md).
- Record material AI assistance in [docs/06-governance/ai-usage-log.md](docs/06-governance/ai-usage-log.md) and check every AI-generated claim, reference and line of code. Plagiarism rules apply: cite everything.

## Professional communication

See [docs/01-team/communication.md](docs/01-team/communication.md). In short: email (not Teams) for staff and partners, within working hours, and every scope agreement goes in writing.
