# Capability Scan

## Platform

Name the platform and environment.

## Agent Capabilities

| Capability | Available | Evidence / Notes |
|---|---|---|
| File read/write | unknown | Not checked |
| Shell commands | unknown | Not checked |
| Subagents | unknown | Not checked |
| Parallel tool calls | unknown | Not checked |
| Browser/UI inspection | unknown | Not checked |
| Network access | unknown | Not checked |
| GitHub/PR tooling | unknown | Not checked |
| Google Docs/Drive export | unknown | Not checked |
| Image/PDF/doc generation | unknown | Not checked |

## Subagent Policy

- If subagents are available, use them for plan review, implementation review,
  adversarial verification, research, and parallel read-only inspection where
  appropriate.
- If subagents are not available, document the downgrade and perform a labeled
  single-agent review.
- Never pretend a simulated role is an autonomous subagent.

## Downgrades

List capability downgrades and their effect on harness strength.
