# Project Agent Harness

This directory is the active project-specific harness. It is the operating
contract for agentic work in this repository.

## Two Halves

What lives here is **project truth**: shared, committed, the same for everyone.

**Environment truth** — what your agent can do, where your checkout is, which
binaries you invoke — lives in `agents/local/`, which is never committed. Every
clone arrives without it, and building it is how the harness adapts to the
machine it landed on. Start at `agents/LOCAL_SETUP.md`.

## Read Order

1. `AGENTS.md`
2. `agents/RUN_STATE.md`
3. `agents/LOCAL_SETUP.md`, and your own `agents/local/CAPABILITIES.md`
4. `agents/intake/PROJECT_BRIEF.md`
5. `agents/intake/PROJECT_PROFILE.md`
6. `agents/intake/SOURCE_MANIFEST.md`
7. `agents/intake/QUESTIONS_SUMMARY.md`
8. `agents/planning/ROADMAP.md`
9. `agents/planning/BACKLOG.md`
10. `agents/architecture/TECH_STACK.md`
11. `agents/validation/GATES.md`
12. `agents/execution/WORKFLOW.md`
13. `agents/i18n/TRANSLATION_PROTOCOL.md`, when the project carries more than one
    working language
14. Latest dated review under `agents/reviews/`
15. Relevant local logbook notes under `agents/local/logbook/` when available

## Operating Rules

- Do not start implementation until the mounted harness is accepted.
- Do not start implementation until the local half exists. See GATE-LOCAL in
  `agents/validation/GATES.md`.
- Existing project rules are preserved and fused into this harness.
- Ask the user when product, stack, deployment, quality, or evidence decisions
  are unclear.
- Decide review strength from your own capability scan, not from a committed
  document or another developer's review.
- Keep environment truth under `agents/local/`; it is never committed.
- Keep task logbook entries under `agents/local/logbook/`; promote durable facts
  into committed docs.
- Promote important decisions into ADRs, planning docs, validation docs, or
  architecture docs.
- Cite artifacts rather than asserting them. A citation is checkable, and the
  doctor checks that cited paths exist.
- If harness drift is detected, stop, write a handoff, and ask for continuation
  with refreshed context.

## Completion Standard

Work is complete only when the project-specific validation gates pass, or when
the remaining blocker is explicitly documented and accepted by the user.
