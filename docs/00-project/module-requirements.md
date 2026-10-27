# What the module requires (COMP0016 Launch Lecture 1)

This is a checklist of everything the 2026-27 launch lecture asks teams to produce or record, with where each item lives in this repo. The slides themselves are on [Moodle](https://moodle.ucl.ac.uk/course/view.php?id=56434) and are deliberately not copied here.

## Assessment

| # | Component | Type | Weight | Due (see Moodle) | Where we prepare it |
|---|---|---|---|---|---|
| 1 | Coursework: Requirements & Design | Group | 5% | Nov 2026, 16:00 | [specification.md](specification.md), [../02-requirements/](../02-requirements/), [../03-design/](../03-design/) |
| 2 | Presentation (remote online), the elevator pitch | Group | 5% | Jan 2027, 16:00 | [../../media/presentations/](../../media/presentations/) |
| 3 | Website Report | Group × individual coefficient | 40% | Mar 2027, 16:00 | [../../website/](../../website/) |
| 4 | System Artefacts | Group × individual coefficient | 50% | Mar 2027, 16:00 | `src/`, `tests/`, `experiments/`, [../../builds/](../../builds/), [../07-handover/](../07-handover/) |

**Individual coefficient** comes from TA and lecturer input (weekly), client-liaison input (weekly), and self and peer assessment (IPAC). **Every member must contribute to every aspect, including programming and the website.** Evidence: [../01-team/contributions.md](../01-team/contributions.md), git history, PR reviews and weekly progress files.

## Deliverables to the client (end of Term 2)

| Deliverable | Where |
|---|---|
| A system: working prototype and its code | `src/`, `builds/`, `docs/07-handover/` |
| A report (website) | `website/` |
| A series of videos showing monthly progression | `media/videos/` |

Project-specific deliverables from the Avanade brief (technical presentation, benchmark package, Agentic Meta-Statistician, Azure/Fabric demonstrator, executive pitch) are tracked in [../02-requirements/requirements.md](../02-requirements/requirements.md#7-deliverables).

## Set-up tasks (weeks 6–7)

| Task | Requirement | Status / location |
|---|---|---|
| 1 | Motivation tracking form | Done individually |
| 2 | Up to 7 IBM SkillsBuild courses by Fri 16 Oct 2026 (Design Thinking, HCI and AI emphasised) | [../01-team/skills-build.md](../01-team/skills-build.md) |
| 3 | Professional templates for **video submissions, reports, weekly minutes and work packages**, agreed with the client | [../../templates/](../../templates/); agreement in `project-management/agreements/` |
| 4 | GitHub repo `COMP0016-2026-teamXX-projectname`, shared with partners; **problem statement**, `README.md`, `licence.md` (confirm with supervisor), other template docs | This repo; [../../README.md](../../README.md); [../../LICENCE.md](../../LICENCE.md) |
| 5–6 | Agentic set-up (announced the following week) | Add details here when released |

## Ongoing process requirements

| Requirement (lecture) | How we satisfy it |
|---|---|
| Weekly in-lab progress check, recorded for assessment | `project-management/weekly-progress/` |
| Meet the client every two weeks (if not weekly); builds they can run | `project-management/meetings/client/`, `builds/` |
| Every two weeks a build to demo progression (TA) | Git tags `build-NN`, [../../builds/CHANGELOG.md](../../builds/CHANGELOG.md) |
| Monthly update video, sent to primary supervisor | `media/videos/` |
| Biweekly development videos, blogs and portfolios | `media/blog/`, `media/videos/` |
| Up-to-date GitHub with readme and instructions as it develops | `README.md` (keep the Getting-started section current) |
| **Folder of experimental builds showing progression** | `builds/`, `experiments/` |
| **Weekly builds and an audit trail of progress** | Git history, weekly progress, sprint reviews |
| Define multiple solutions; compare 3+ ways of doing a task; fit for purpose? wanted? expert vs public views; resources (hosting, token spend) | Decision records in [../03-design/decisions/](../03-design/decisions/) ([template](../../templates/decision-record.md)) |
| Work packages documented between team lead and roles | [../../project-management/work-packages/register.md](../../project-management/work-packages/register.md) |
| Bi-weekly work-package agreement with the TA: who, what, by when | Same register, "TA agreed" column |
| Work-package scopes agreed with the client in writing by email; requirements sealed by end of Reading Week 1 | `project-management/agreements/` |
| Risk awareness, testing and evaluation, AI safety | [../06-governance/risk-register.md](../06-governance/risk-register.md), [../05-testing/](../05-testing/) |
| IP and GDPR update on solution and website (Term 2 wks 3–5) | [../06-governance/](../06-governance/) |
| Deployment processes, package testing, materials hand-over | [../07-handover/](../07-handover/) |
| Cite sources; no plagiarism; check AI outputs | References in every doc; [../06-governance/ai-usage-log.md](../06-governance/ai-usage-log.md) |

## Support contacts (from the lecture)

| Who | Role | Office hours |
|---|---|---|
| Prof Dean Mohamedally (DM) | Module lead | Tue 10–11 in lab, or email |
| Prof Graham Roberts (GR) | Deputy module lead | Tue 11–12 in lab, or email |
| Dr Yun Fu (YF) | Project labs and TA manager | Tue 2–3 in lab, or email |
| Prof Jennifer Rode (JR) | Reasonable adjustments | TBC |
| Dr Emmanuel Letier (EL) | Team issues and systems validation (T2) | TBC |
| Strategic Alliances Team | Partner issues (e.g. 2+ rejected meeting slots in a row: notify SAT **and** DM) | cs.strategicalliancesteam@ucl.ac.uk |
| Tech Support Group | GPU / lab machines | request@cs.ucl.ac.uk, <https://tsg.cs.ucl.ac.uk/> |

Email academics 24 h in advance for a meeting.

## Compute available (UCL CS)

Lab 1.21 (RTX 4070 Ti Super, 32 GB), Lab 1.05 (RTX 3090, 128 GB), time-share machines *blaze*, *cream*, *vanilla*, and the bookable Remote Workstation Service. See <https://tsg.cs.ucl.ac.uk/>. Record which one each experiment used in its experiment record.
