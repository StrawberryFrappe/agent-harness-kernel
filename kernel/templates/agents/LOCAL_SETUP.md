# Local Setup

The harness is split in two. This file is committed, and it tells you how to
build the half that is not.

## Why There Are Two Halves

**Project truth** is shared and committed: what is being built, the architecture,
ADRs, gates, open questions, the source manifest. Identical for every developer on
every machine, and still true next year.

**Environment truth** is local and never committed: which agent you run, whether
it has subagents, which integrations are connected, where your checkout lives,
which binaries you invoke, how you parallelise work. Different per person, per
machine, and it goes stale.

The test for which half something belongs to:

> **Would another developer's agent get confused if it had this?**

If yes, it is local. A path that exists only on your machine, a capability only
your platform has, a tool only you installed. Committing those makes every other
developer's agent read instructions it cannot follow — and believe them.

## The Local Half Is The Adaptation Mechanism

Because `agents/local/` never travels with the repository, **every clone is forced
through this setup.** That is the point, not a limitation.

A harness that shipped its author's environment would arrive on the next machine
already wrong, and confidently so. A harness that ships only project truth arrives
incomplete and *says so* — the gate below refuses implementation work until the new
machine describes itself. The harness re-adapts to each environment it lands in,
because it cannot do anything else.

## How It Is Kept Out Of Git

`agents/local/.gitignore` ships containing:

```
*
!.gitignore
```

The directory ignores its own contents, keeping only the ignore file itself, so
the folder exists in a fresh clone but arrives empty. Nothing outside needs to
know about it, and no rule in the project's root ignore file can leak the
arrangement.

The doctor verifies this by asking `git check-ignore` whether a probe file inside
`agents/local/` is actually ignored, rather than by reading the ignore file —
a text check cannot see a parent negation that would silently undo it.

## What To Create

| Path | Purpose |
|---|---|
| `agents/local/CAPABILITIES.md` | **Required.** Your capability scan and machine facts |
| `agents/local/logbook/` | Optional. Raw session notes; promote durable facts into committed docs |

Copy `agents/templates/capability-scan-template.md` to
`agents/local/CAPABILITIES.md` and fill it in. It asks for:

- which agent and platform you run, and whether it has subagents;
- which integrations are connected **and authorised**;
- whether you may create sandboxes or git worktrees;
- your checkout locations and the binaries this project needs;
- how you isolate parallel work.

Record what you verified, not what you assume. An unverified capability claim is
worse than an absent one, because the harness will plan around it.

## The Gate

Implementation work requires `agents/local/CAPABILITIES.md` to exist. The doctor
reports its absence as a warning, and as a hard blocker under `--strict`.

A harness that does not know what its agent can do will either plan work the
environment cannot perform, or quietly downgrade a review to a single-agent pass
and not mention it.

Reading documents and making trivial corrections are not blocked.

## Keeping It Honest

Re-run the scan when the environment changes — a new agent, a newly connected
integration, a revoked permission. A capability scan is a snapshot, and its date
is part of the evidence.
