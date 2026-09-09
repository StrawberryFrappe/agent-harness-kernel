# ADR 0001: Harness Mounting Policy

## Status

Accepted by kernel default; **confirm all three choices during project mount.**

## Context

Agentic coding platforms do not consistently share global rules, memories,
skills, workflows, or subagent capabilities across devices and tools. A
project-local harness makes the operating contract travel with the repository
instead of with one person's tool configuration.

Three choices follow from that, and the kernel default is not right for every
project.

## Decision

### 1. The harness is a project-local `agents/` tree

It is the operating contract. Existing project rules are preserved and fused
rather than overwritten. The generic kernel does not remain authoritative after
mounting.

### 2. The harness is split into a shared half and a local half

`agents/` is **project truth**: shared, committed, identical for every
contributor. `agents/local/` is **environment truth**: capabilities, machine
paths, tooling, raw session notes. It is never committed.

The test for which half something belongs to: *would another developer's agent
get confused if it had this?*

`agents/local/.gitignore` contains `*` and `!.gitignore`, so the directory
ignores its own contents and arrives empty in a fresh clone. That is the
adaptation mechanism, not a gap — a harness cannot inherit its author's
environment, so each machine is made to describe itself before implementation
work begins (GATE-LOCAL).

### 3. The shared half is committed by default

The project carries its own operating context, and work stays consistent across
devices and platforms.

**A project may choose otherwise.** Some owners do not want harness files in a
shared repository — because collaborators object, or because the harness is being
trialled before it is proposed to the wider team. If so, exclude it through
`.git/info/exclude`, which is never committed, rather than through the tracked
`.gitignore`, which would itself announce the harness in a diff.

Record the choice here, and record what it is protecting against, so it can be
revisited when that reason expires. A private mount is usually a phase, not a
permanent state.

## Consequences

- Work is more consistent across devices and platforms.
- The project carries its own operating context.
- Every clone requires a local setup step before implementation. Intended.
- **If the harness is private:** the exclusion is machine-local, so a clone
  elsewhere has none of it; `git add -f` bypasses it entirely; and decisions
  recorded here reach no collaborator until the policy changes. Track that as an
  open question rather than accepting it silently.
- **If the harness is shared:** anything written here is readable by everyone with
  repository access, including candid assessments. Write accordingly.
