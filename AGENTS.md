# Agent Harness Kernel Instructions

You are operating inside the Agent Harness Kernel starter.

## Prime Directive

Do not implement application code from this kernel alone. First mount or update
the project-specific harness, ask the required questions, run a harness review,
and wait for user acceptance unless the user explicitly overrides this rule.

## Setup Entry

Read `SETUP_PROMPT.md`, then inspect the target repository before editing. If
this kernel is cloned as a subfolder, treat this folder as setup material and
fuse `kernel/templates/` into the target project root.

## Fusion Rules

- Preserve existing project rules such as `AGENTS.md`, `CLAUDE.md`, README
  instructions, contribution guides, and CI notes.
- If an existing rule conflicts with this kernel, record the conflict and ask
  the user before changing behavior.
- Create or update `agents/` as the active harness folder.
- Keep raw local memory under the mounted `agents/local/`, and ensure it is
  gitignored.
- Promote durable decisions into ADRs, summaries, architecture docs, backlog,
  validation gates, or traceability docs.

## Required Behavior

- Inspect before proposing architecture.
- Grill the user on unclear product, stack, deployment, evidence, and workflow
  decisions.
- Discover whether the current platform can spawn subagents. If not, document
  the downgrade.
- Use adversarial review when possible.
- Be explicit about what was done directly, delegated, simulated, skipped, or
  deferred.
- Stop and hand off if you detect that you drifted from the mounted harness.
