# Project Agent Instructions

This project uses a mounted Agent Harness Kernel under `agents/`.

## Required Read Order

1. `agents/README.md`
2. `agents/RUN_STATE.md`
3. `agents/intake/PROJECT_BRIEF.md`
4. `agents/intake/PROJECT_PROFILE.md`
5. `agents/intake/SOURCE_MANIFEST.md`
6. `agents/validation/GATES.md`
7. `agents/execution/WORKFLOW.md`
8. Latest relevant review under `agents/reviews/`

## Core Rules

- Do not implement application code until the mounted harness is accepted,
  unless the user explicitly overrides after risk disclosure. This gate is
  unconditional — it is not waived by small scope, high confidence, or complete
  context. Assumptions you filled from context, even "safe" ones, must be
  surfaced for the user to double-check before you proceed.
- Preserve existing project rules and fuse them into this file and `agents/`.
- Ask the user when product, stack, deployment, evidence, or quality decisions
  are unclear.
- Use subagents for review when available. If unavailable, document the
  capability downgrade.
- Keep raw memory and task logs under `agents/local/`; do not commit them.
- Promote durable decisions into ADRs, planning docs, architecture docs,
  validation docs, or review summaries.
- If you detect drift from the harness, stop forward work and produce a handoff.
