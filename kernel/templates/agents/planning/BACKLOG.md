# Backlog

A registry of what could be done and why. **It carries no status.** Whether an
item is in progress, blocked or finished is recorded in `agents/RUN_STATE.md`
and nowhere else. An entry here changes when the work itself is redefined, not
when its state moves — which is why this file does not rot between sessions.

| ID | Area | Item | Why / Source | Done Evidence |
|---|---|---|---|---|
| BL-001 | Harness | Complete harness mounting | Kernel mount requested | Harness review accepted |

## When The Project Has An External Board

GitHub Projects, Jira, Linear and the like own board-worthy items. Name the
board here, and keep this file for the overflow: harness chores, documentation
gaps, decisions waiting on a person — work that is real but does not earn a
card.

Do not mirror the board. A hand-synced copy of a tool that already tracks status
is exactly the failure this file is shaped to avoid.

## Rules

- Backlog items should be tied to source, ADRs, user decisions, or explicit
  project goals.
- Do not pad the backlog with work that has no product, quality, evidence, or
  operational value.
- If a work item changes visible behavior, define how it will be verified.
- Remove an entry once it is done and its evidence is recorded elsewhere. A
  "Done" section here is status wearing a different hat.
