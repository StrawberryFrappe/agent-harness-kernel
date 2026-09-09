# Capability Scan

Copy this file to `agents/local/CAPABILITIES.md` and fill it in. It is **local and
never committed** — it describes your machine and your agent, not the project.
See `agents/LOCAL_SETUP.md`.

Date of this scan: fill in. Re-scan when the environment changes.

## Platform

Name the agent, the model, and where it is running.

## Agent Capabilities

Record what was verified, not what was assumed.

| Capability | Available | Evidence / Notes |
|---|---|---|
| File read/write | unknown | Not checked |
| Shell commands | unknown | Not checked |
| Subagents | unknown | Not checked |
| Parallel tool calls | unknown | Not checked |
| Browser/UI inspection | unknown | Not checked |
| Network access | unknown | Not checked |
| GitHub/PR tooling | unknown | Not checked |
| Sandboxes or git worktrees permitted | unknown | Not checked |
| Image/PDF/doc generation | unknown | Not checked |

## Connected Integrations

List integrations and which are actually authorised. One that is configured but
unauthorised is not a capability, and planning around it will fail at the moment
it is needed.

## Machine Facts

Paths and binaries that exist only here. Anything recorded in this section must
not appear in the committed harness.

| Fact | Value |
|---|---|
| Checkout location | fill in |
| Other working trees | fill in |
| Project binaries and versions | fill in |

## Isolation Strategy

How you keep concurrent work from sharing a working tree — separate clones, git
worktrees, containers, or working serially. The committed workflow states only
the principle; the mechanism is yours and belongs here.

## Subagent Policy

- If subagents are available, use them for plan review, implementation review,
  adversarial verification, research, and parallel read-only inspection.
- If subagents are not available, document the downgrade and perform a labeled
  single-agent review.
- Never pretend a simulated role is an autonomous subagent.

## Downgrades

List capability downgrades and their effect on harness strength.
