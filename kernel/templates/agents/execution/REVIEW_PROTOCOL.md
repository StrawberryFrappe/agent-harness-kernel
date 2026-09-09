# Review Protocol

## Review Types

- Harness mount review
- Capability scan
- Maturity review
- Plan review
- Implementation review
- Adversarial review
- Final review

## Severity

- P0: blocking
- P1: blocking unless explicitly mitigated
- P2: should fix or document
- P3: optional improvement

## Capability Scans Are Per Developer

Review strength depends on what the reviewing agent can actually do, and that
differs per person and per machine. There is no project-wide answer, so the
harness does not record one.

- Each developer keeps their own scan at `agents/local/CAPABILITIES.md`, which is
  never committed. See `agents/LOCAL_SETUP.md`.
- Read your own scan before deciding how a review will be performed. Never assume
  a capability because a committed document, or another developer's review,
  mentions it.
- A dated capability scan under `agents/reviews/` is a historical record of one
  machine at one time. It is evidence about the past, not a claim about the
  current environment.

## Rules

- Use subagents for review when available.
- If subagents are unavailable, label the review as single-agent and record the
  downgrade in your local scan and in the review itself.
- Findings should cite files, commands, screenshots, or source evidence. A
  citation is checkable; an assertion is not.
- Do not count simulated roles as autonomous review.
- A blocking review finding must update `agents/RUN_STATE.md`.

## When More Than One Developer Reviews

Review filenames carry an author slug so two people reviewing on the same day do
not collide: `capability-scan.<slug>.md`, `implementation-review.<slug>.md`.
Review **folders** stay `YYYYMMDD/`. The naming rules are in
`agents/execution/WORKFLOW.md`.
