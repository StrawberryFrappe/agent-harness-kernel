# Workflow

## Harness Mounting

1. Inspect existing project files.
2. Preserve and fuse existing rules.
3. Run the capability scan into `agents/local/CAPABILITIES.md`.
4. Grill the user on unclear decisions.
5. Summarize answers, recording refusals as open questions rather than filling
   them in.
6. Draft or update project-specific harness files.
7. Run review.
8. Wait for user acceptance.

## Before Implementation

`agents/local/CAPABILITIES.md` must exist. See `agents/LOCAL_SETUP.md`.

The local half never travels with the repository, so a fresh clone always lands
without it. Building it is how the harness learns what this machine and this
agent can actually do, instead of inheriting assumptions from whoever mounted it.

## Implementation

1. Plan the task.
2. Review the plan, preferably with a subagent.
3. Implement within accepted scope.
4. Verify with the agreed gates.
5. Review the result.
6. Update traceability and evidence. Write local logbook notes under
   `agents/local/logbook/` when useful, then promote durable facts into
   committed docs.
7. Report what was done, what was delegated, and what remains.

## Isolating Concurrent Work

**Concurrent work must not share a working tree.** Two agents editing one
checkout will interleave changes that neither intended.

The mechanism is yours to choose — separate clones, git worktrees, containers, or
simply working serially. Record which you use in `agents/local/CAPABILITIES.md`,
along with any paths it depends on. The principle is shared; the mechanism is
local, because one developer's directory layout is meaningless on another
developer's machine.

Related: never use bare `git stash` or `git stash pop` when more than one tree
shares a repository. The stash stack is shared, and another session may be using
it. Prefer a temporary commit.

## Naming When More Than One Developer Contributes

Most harness IDs live in a single index table each — questions, assumptions,
backlog items, work items, evidence, sources. Two developers adding to the same
table produce a merge conflict, which is visible and resolvable.

**ADRs are the exception.** They are separate files, so two developers each
creating `0006-something.md` merge cleanly into two different documents both
claiming the same number, and nothing reports it.

Therefore, when a project has more than one contributor:

- ADR filenames carry an author slug: `<slug>-0006-decision-name.md`, referenced
  in prose as `ADR-<slug>-0006`.
- Review filenames carry it too: `implementation-review.<slug>.md`. Review
  **folders** stay `YYYYMMDD/`, because the doctor identifies them by an
  eight-digit name.
- The slug records **who minted the ID**, not who owns the subject.
- Append new rows at the end of index tables, so concurrent additions conflict
  rather than silently interleaving.

Pick slugs when the second contributor arrives, and record the choice in an ADR.
IDs minted before that point keep their bare form; state in the same ADR who they
belong to.

## Override Protocol

If the user says "just build it" before harness acceptance:

1. Explain the risk.
2. Ask for explicit override.
3. If confirmed, record the autonomous decisions and assumptions in the logbook
   and ADRs where appropriate.
4. Keep the smallest viable scope.

## Drift Protocol

If the agent detects it has deviated from the harness:

1. Stop forward implementation work.
2. Write a logbook entry describing the deviation.
3. Produce or update `agents/execution/HANDOFF.md`.
4. Tell the user plainly what happened.
5. Recommend context compression or a fresh continuation when appropriate.
