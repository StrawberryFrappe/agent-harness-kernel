# Logbook Policy

Logbook entries are local agent memory by default.

## Location

Write detailed task notes under:

```text
agents/local/logbook/YYYYMMDD/
```

`agents/local/**` is gitignored. This keeps raw agent memory, deviations,
personal context, and context-management notes out of the shared repository.

## Promotion Rule

If a logbook fact matters across devices, collaborators, or future agents,
promote it. **Route by what kind of fact it is** — an earlier version of this
list named several destinations without saying which got what, and the
narrative ones converged into duplicate journals.

| Kind of fact | Goes to | Lifecycle |
|---|---|---|
| Where the work stands **now** | `agents/RUN_STATE.md` | Replaced, never appended |
| What happened, as it happened | `agents/record/<SLUG>-<YYYYMMDD>/` | Small files, added not groomed |
| The baton for the next agent | `agents/execution/HANDOFF.md` | Emptied when consumed |
| A decision and its rationale | `agents/adrs/` | Write-once, superseded not edited |
| An answered question | `agents/intake/QUESTIONS_SUMMARY.md` | Moves from open to answered |
| An assumption | `agents/intake/ASSUMPTIONS.md` | Retired when proven or disproven |
| What could be done and why | `agents/planning/BACKLOG.md` | Status-free registry |
| Proof a claim is true | `agents/validation/EVIDENCE_INDEX.md` | Append a row |
| A critique of work | `agents/reviews/`, indexed in `reviews_index.md` | Write-once |
| Structure and stack | `agents/architecture/` | Replaced as it changes |

If a fact seems to belong in two of these, it is probably two facts.

## Deviation Rule

If the agent detects drift from the harness:

1. Stop forward implementation work.
2. Write a local logbook entry.
3. Update `agents/execution/HANDOFF.md`.
4. Tell the user plainly what happened and why continuation needs refreshed
   context, explicit approval, or a handoff.
