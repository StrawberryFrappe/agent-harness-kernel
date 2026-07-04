# ADR 0001: Harness Mounting Policy

## Status

Accepted by kernel default; confirm during project mount.

## Context

Agentic coding platforms do not consistently share global rules, memories,
skills, workflows, or subagent capabilities across devices and tools.

## Decision

Use a committed, project-local `agents/` harness as the operating contract.
Keep raw agent memory and copied kernel provenance under `agents/local/`, which
is gitignored. Preserve and fuse existing project rules instead of overwriting
them.

## Consequences

- Work is more consistent across devices and platforms.
- The project carries its own operating context.
- Some collaborators may dislike committed harness files; this is accepted for
  consistency unless the project owner changes the policy.
- The generic kernel does not remain authoritative after mounting.
