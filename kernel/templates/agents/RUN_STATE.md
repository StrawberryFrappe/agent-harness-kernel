# Run State

This file is the **single owner of status**. Current phase, what is in progress,
what is blocked, and what has been verified are recorded here and in no other
document. Planning and architecture documents say what the work is and why; only
this one says where it stands.

Write it as the work happens, not as a bookkeeping pass afterwards. A status
table that needs a separate update step is the first thing to go stale.

**Replace, do not append. Keep it short.** This file describes the present, so
it should stay roughly the same size over the life of the project. If it is
growing a dated section per delivery, it has become a changelog — that history
belongs in `agents/record/`, under a folder per developer per day.

## Current Phase

Harness mounting pending.

## Status

- Kernel copied or cloned.
- Project inspection not complete.
- User grill not complete.
- Harness review not complete.
- Implementation is blocked until user accepts the mounted harness.

## Next Action

Inspect the target project and fill `agents/intake/PROJECT_BRIEF.md`,
`agents/intake/SOURCE_MANIFEST.md`, and `agents/reviews/<date>/capability_scan.md`.

## Blockers

- User has not accepted the mounted harness.

## Last Verified State

No project validation has been run yet.
