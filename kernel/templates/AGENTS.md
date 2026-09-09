# Project Agent Instructions

This project uses a mounted Agent Harness Kernel under `agents/`.

## Required Read Order

1. `agents/README.md`
2. `agents/RUN_STATE.md`
3. `agents/LOCAL_SETUP.md`
4. `agents/intake/PROJECT_BRIEF.md`
5. `agents/intake/PROJECT_PROFILE.md`
6. `agents/intake/SOURCE_MANIFEST.md`
7. `agents/validation/GATES.md`
8. `agents/execution/WORKFLOW.md`
9. `agents/i18n/TRANSLATION_PROTOCOL.md`, when the project carries more than one
   working language
10. Latest relevant review under `agents/reviews/`

## The Local Half

`agents/` is project truth and is committed. What your agent can do, where your
checkout lives, and which binaries you invoke are **environment truth**, and live
in `agents/local/`, which is never committed.

A fresh clone therefore arrives incomplete on purpose. Build the local half
before implementation work — `agents/LOCAL_SETUP.md` says how, and GATE-LOCAL
enforces it.

## Core Rules

- Do not implement application code until the mounted harness is accepted,
  unless the user explicitly overrides after risk disclosure. This gate is
  unconditional — it is not waived by small scope, high confidence, or complete
  context. Assumptions you filled from context, even "safe" ones, must be
  surfaced for the user to double-check before you proceed.
- Do not implement application code until `agents/local/CAPABILITIES.md` exists.
- Preserve existing project rules and fuse them into this file and `agents/`.
- Ask the user when product, stack, deployment, evidence, or quality decisions
  are unclear.
- Decide review strength from your own capability scan. Do not assume a
  capability because a committed document mentions it.
- Keep environment truth, raw memory and task logs under `agents/local/`; never
  commit them.
- Promote durable decisions into ADRs, planning docs, architecture docs,
  validation docs, or review summaries.
- When more than one person contributes, ADR and review filenames carry an
  author slug. See the naming rules in `agents/execution/WORKFLOW.md`.
- If you detect drift from the harness, stop forward work and produce a handoff.
