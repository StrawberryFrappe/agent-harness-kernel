# Project Agent Harness

This directory is the active project-specific harness. It is the operating
contract for agentic work in this repository.

## Read Order

1. `AGENTS.md`
2. `agents/RUN_STATE.md`
3. `agents/intake/PROJECT_BRIEF.md`
4. `agents/intake/PROJECT_PROFILE.md`
5. `agents/intake/SOURCE_MANIFEST.md`
6. `agents/intake/QUESTIONS_SUMMARY.md`
7. `agents/planning/ROADMAP.md`
8. `agents/planning/BACKLOG.md`
9. `agents/architecture/TECH_STACK.md`
10. `agents/validation/GATES.md`
11. `agents/execution/WORKFLOW.md`
12. Latest dated review under `agents/reviews/`
13. Relevant local logbook notes under `agents/local/logbook/` when available

## Operating Rules

- Do not start implementation until the mounted harness is accepted.
- Existing project rules are preserved and fused into this harness.
- Ask the user when product, stack, deployment, quality, or evidence decisions
  are unclear.
- Use subagents for review when available. If not available, document the
  downgrade in the capability scan and review.
- Keep local agent memory under `agents/local/`; do not commit it.
- Keep task logbook entries under `agents/local/logbook/`; promote durable
  facts into committed docs.
- Promote important decisions into ADRs, planning docs, validation docs, or
  architecture docs.
- If harness drift is detected, stop, write a handoff, and ask for continuation
  with refreshed context.

## Completion Standard

Work is complete only when the project-specific validation gates pass or when
the remaining blocker is explicitly documented and accepted by the user.
