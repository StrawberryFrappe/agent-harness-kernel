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
promote it into one of these committed locations:

- `agents/RUN_STATE.md`
- `agents/intake/QUESTIONS_SUMMARY.md`
- `agents/intake/ASSUMPTIONS.md`
- `agents/adrs/`
- `agents/planning/`
- `agents/architecture/`
- `agents/validation/EVIDENCE_INDEX.md`
- `agents/execution/HANDOFF.md`
- `agents/reviews/reviews_index.md`

## Deviation Rule

If the agent detects drift from the harness:

1. Stop forward implementation work.
2. Write a local logbook entry.
3. Update `agents/execution/HANDOFF.md`.
4. Tell the user plainly what happened and why continuation needs refreshed
   context, explicit approval, or a handoff.
