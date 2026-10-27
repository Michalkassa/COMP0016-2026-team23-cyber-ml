# 0001: Repository structure and documentation approach

| Field | Value |
|---|---|
| Status | Proposed *(accept at next team meeting)* |
| Date | 2026-10-27 |
| Deciders | Team 23 |
| Consulted | Client (to confirm templates, module Task 3) |

## Context

The module requires an audit trail (weekly progress, fortnightly builds and client meetings, monthly videos, written work-package agreements) and a repo shared with the client. The source repo `ucl-cybersecurity-ml` contains the research brief, a research wiki and a dataset.

## Options considered

| Criterion | A: Single repo, docs-as-markdown | B: Code in GitHub, docs in SharePoint/Word | C: Separate code and docs repos |
|---|---|---|---|
| Client visibility | One link shows everything | Split across tools | Two links |
| Audit trail | Full git history | Weak version history | Good but fragmented |
| Effort | Low | Low | Medium |
| Review via PRs | Yes | No | Yes |

## Decision

Option A. One repo: `docs/` holds living documents, `project-management/` holds dated records, `templates/` holds all templates, and `research/wiki/` is carried over from the source repo. Raw data is not committed; `data/` holds datacards and `scripts/fetch_data.sh` retrieves the data.

## Consequences

Large binaries (videos, slides) live in shared storage and are linked. Everyone needs basic markdown and git skills.
