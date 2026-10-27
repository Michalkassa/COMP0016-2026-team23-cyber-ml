# Schedule, sprints and milestones

Source: COMP0016 Launch Lecture 1 (2026-27), "Schedule for the two terms" (tentative). **Moodle is authoritative for deadlines. Re-check it and update this file whenever dates move.**

## Module milestones

| Date | Academic week | Milestone |
|---|---|---|
| Mon 5 Oct 2026 | 6 | Term 1 starts; IBM SkillsBuild; project set-up |
| Fri 16 Oct 2026 | 7 | IBM SkillsBuild courses complete (up to 7) |
| w/c 12 Oct 2026 | 7 | Projects start; team allocated; GitHub set up |
| Weeks 7–10 | 7–10 | Requirements and design; TAs start; client design sessions |
| **Mon 9 Nov 2026** | 11 (reading) | **Agree client deliverables; requirements sealed by end of reading week** |
| Nov 2026 (Moodle) | — | **Coursework 1: Requirements & Design (5%)** |
| Weeks 12–14 | 12–14 | DevOps, experimental prototyping |
| Weeks 15–16 | 15–16 | System Prototype 1; update website; Term 1 progress notes |
| Wed 16 Dec 2026 | 16 | Lecture Pt 1 (Dr Yun Fu): assessment of deliverables |
| Week 20 (w/c 11 Jan 2027) | T2 wk 1 | Prototype 1 demonstrated to client; TA approves elevator pitch; Lecture Pt 2 |
| **Fri 22 Jan 2027** | 21 | **Elevator pitch to client audience (Presentation, 5%)** |
| Weeks 22–24 | 22–24 | Prototype 2; IP and GDPR update on solution and website |
| w/c 15 Feb 2027 | 25 | Reading week |
| **Fri 12 Mar 2027** | 28 | **All development stops; submission window opens** |
| **Tue 16 Mar 2027** | 29 | **Showcase (in person, lab session)** |
| Sat 20 Mar 2027 | 29 | Report website finished; **final client hand-over** |
| **Wed 24 Mar 2027, 16:00** | 30 | **Submission window closes (Website Report 40%, System Artefacts 50%)** |

## Sprint plan (proposed, two-week sprints)

The research brief proposes five three-week sprints from January to March and notes that this doesn't fit. We use **two-week sprints from October**, matching the fortnightly client meeting and demo-build cadence. The brief's five decision gates map onto them as shown below. *Confirm with the supervisor and Avanade, then record the agreement in [project-management/agreements/](../../project-management/agreements/).*

| Sprint | Dates | Focus | Brief gate / exit criterion | Build |
|---|---|---|---|---|
| S0 | 12–25 Oct | Team formation, repo, templates, SkillsBuild | Repo and templates agreed with client | — |
| S1 | 26 Oct – 8 Nov | Practitioner interviews, discovery, task and dataset selection, requirements draft | **Gate 1:** a feasible, authorised study (task, user, data, labels agreed) | build-01 (data loader + EDA) |
| S2 | 9 – 22 Nov | Requirements sealed; Coursework 1; sourced review table; evaluation protocol draft; agent rubric draft | Requirements signed off in writing | build-02 |
| S3 | 23 Nov – 6 Dec | DevOps/CI, feature pipeline, baselines, agent skeleton | Baselines reproducible from config | build-03 |
| S4 | 7 – 18 Dec | **Prototype 1**: baselines + first TabPFN run + agent workflow v1; website update | **Gate 2:** data, model rights and evaluation design adequate; protocol ready to freeze | build-04 = Prototype 1 |
| — | 19 Dec – 10 Jan | Winter break (optional low-intensity work only) | — | — |
| S5 | 11 – 24 Jan | Demo P1 to client; elevator pitch (22 Jan); **freeze evaluation protocol** | Pitch delivered; protocol v1.0 frozen | build-05 |
| S6 | 25 Jan – 7 Feb | Full benchmark runs; agent comparative evaluation; IP/GDPR update | Benchmark results with uncertainty | build-06 |
| S7 | 8 – 21 Feb | **Prototype 2**; Azure/Fabric demonstrator | **Gate 3:** evidence supports demo narrative; experimental scope frozen | build-07 = Prototype 2 |
| S8 | 22 Feb – 12 Mar | Demonstrator polish, technical deck, executive pitch, report | **Gate 4:** findings traceable, integration claims match what works | build-08 = release candidate |
| H | 12 – 24 Mar | Packaging, testing, showcase, hand-over, submissions | **Gate 5:** proceed / revise / stop recommendation | `v1.0.0` final release |

## Recurring cadence

| Frequency | Activity | Record |
|---|---|---|
| Weekly (Tue lab) | In-lab progress check with TA (recorded for assessment) | `project-management/weekly-progress/` |
| Weekly | Meeting with IXN client supervisor (lecture says weekly; at least fortnightly) | `project-management/meetings/client/` |
| Fortnightly | Demo build the client can run | `builds/CHANGELOG.md` + git tag |
| Fortnightly | Work packages agreed with the TA and confirmed by email with the client | `project-management/work-packages/`, `project-management/agreements/` |
| Fortnightly | Development blog post | `media/blog/` |
| Monthly | Team progress video sent to primary supervisor, discussed the following week | `media/videos/README.md` |
