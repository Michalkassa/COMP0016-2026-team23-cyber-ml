# Project management: the audit trail

Dated, append-only records of what happened. Don't rewrite past records. Correct them with a dated note.

| Folder | Contents | Naming | Template |
|---|---|---|---|
| [weekly-progress/](weekly-progress/) | TA in-lab progress checks | `YYYY-MM-DD-week-NN.md` | [weekly-progress](../templates/weekly-progress.md) |
| [meetings/client/](meetings/client/) | Avanade meetings | `YYYY-MM-DD[-topic].md` | [meeting-minutes](../templates/meeting-minutes.md) |
| [meetings/supervisor/](meetings/supervisor/) | Supervisor / TA meetings | same | same |
| [meetings/team/](meetings/team/) | Internal meetings, stand-ups, retros | same | same |
| [sprints/](sprints/) | Sprint plans and reviews | `sprint-NN.md` | [sprint](../templates/sprint.md) |
| [work-packages/](work-packages/) | [Register](work-packages/register.md) + one file per WP | `WP-NN-short-name.md` | [work-package](../templates/work-package.md) |
| [agreements/](agreements/) | Written email agreements with client | `YYYY-MM-DD-topic.md` | [agreement-record](../templates/agreement-record.md) |

Day-to-day tasks are GitHub Issues on the project board. Each issue references its `WP-NN`.
