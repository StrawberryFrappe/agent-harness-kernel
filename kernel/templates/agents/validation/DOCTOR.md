# Doctor Workflow

Doctor is a harness coherence check, not a product runtime.

## Hard Blockers

- Root `AGENTS.md` does not point to `agents/`.
- `agents/RUN_STATE.md` does not show the current phase.
- Implementation is marked ready before harness review and user acceptance.
- Existing project rules were overwritten or ignored without a recorded
  decision.
- Major stack/product/deployment decisions are undocumented.
- Local/raw memory is not gitignored.
- Validation gates do not identify evidence.

## Warnings

- Placeholder sections remain.
- ADRs are missing for medium-impact decisions.
- Review index is stale.
- Traceability is sparse.
- Deployment target is deferred.
- Subagents are unavailable, reducing review strength.

## Doctor Record

| Date | Result | Hard Blockers | Warnings | Next Action |
|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD |

## Script Policy

Use the kernel's `scripts/harness_doctor.py` after mounting to automate
missing-file, placeholder, stale-path, and contradiction checks. The workflow
remains authoritative; the script is a guardrail against theatrical completion.
