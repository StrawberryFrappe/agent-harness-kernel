# Mounting Guide

This guide is for agents mounting Agent Harness Kernel into a target project.

## Key Distinction

The `kernel/templates/agents/` directory is not an active harness. It is a
template. The active harness exists only after the agent adapts it into the
target project as `agents/`.

## A Mount Produces Two Halves

**`agents/`** is project truth: shared, committed, identical for every
contributor.

**`agents/local/`** is environment truth: capabilities, machine paths, tooling,
raw session notes. It is never committed — `agents/local/.gitignore` contains `*`
and `!.gitignore`, so the directory ignores its own contents and arrives empty in
a fresh clone.

A mount is not finished until both exist. The test for which half something
belongs to: *would another developer's agent get confused if it had this?*

Because the local half never travels, every clone is forced through its setup.
That is how the harness re-adapts to each machine instead of arriving preloaded
with its author's environment. `agents/LOCAL_SETUP.md` is committed precisely so
the next machine knows what to build.

## More Than One Contributor

Ask the collaboration questions in `QUESTIONNAIRE.md` even when the repository
looks like one person's work. Two answers change the mount:

- **Author slugs.** If more than one person will create ADRs or reviews, agree
  slugs during the mount and record them in an ADR. ADRs are separate files, so
  two people each writing `0006-*.md` produce a silent duplicate that no merge
  conflict reveals.
- **Working language.** If contributors do not share one, name the canonical
  language of the harness and say whether translations are expected, before the
  documents multiply. Mount `agents/i18n/TRANSLATION_PROTOCOL.md` when the answer
  is more than one language; it defines how a translated copy tracks its source
  and how staleness between them is detected. Leave it out of a monolingual mount.

## Mounting Steps

1. Inspect the target repository before editing.
2. Inventory existing rules: `AGENTS.md`, `CLAUDE.md`, README, contribution
   docs, CI docs, scripts, tests, and deployment notes.
3. Run the capability scan **into `agents/local/CAPABILITIES.md`**, not into a
   committed document. It describes one machine and one agent, so it belongs in
   the local half. If subagents are unavailable, record the downgrade.
4. Ask the project grill questions in `kernel/QUESTIONNAIRE.md`.
5. Copy and adapt `kernel/templates/AGENTS.md` into the target root if no
   suitable root agent instructions exist. If they do exist, fuse them instead
   of overwriting.
6. Copy relevant template files from `kernel/templates/agents/` into the target
   `agents/` directory.
7. Adapt copied files to the project. Do not leave placeholder-only files as
   accepted harness docs.
8. Create or update root `AGENTS.md` so agents discover the mounted harness.
9. Create a dated review folder under `agents/reviews/YYYYMMDD/` only when it
   contains an actual review.
10. Run `scripts/harness_doctor.py --root <target>`.
11. STOP at the mandatory acceptance gate (below). Ask the user to accept or
    reject the mounted harness. Do not proceed past this step on your own.

## Mandatory Acceptance Gate

The acceptance gate is unconditional. The agent MUST present the mounted harness
and wait for explicit user acceptance before any implementation, build, compile,
application-code edit, or project tooling run.

This holds in every case, with no exceptions for:

- small or single-file projects ("scope too small" is not a waiver);
- high agent confidence or complete prior context;
- assumptions the agent judged "safe" — these especially must be double-checked,
  because a confident wrong assumption is the most expensive kind.

When context let the agent auto-fill docs instead of grilling, that is not a
shortcut around the gate. The agent must still surface every filled-in
assumption explicitly and let the user correct it. Skipping the gate because
"the answers were obvious" is the exact failure this rule exists to prevent.

Only an explicit user override, given after the agent states the risk, may skip
the gate. Silence, a prior "go ahead" from before the harness existed, or the
agent's own judgement do not count as an override.

If the agent has already started implementation before acceptance, it must stop,
disclose exactly what it did, and return to this gate.

## Existing Project Rules

Fuse, do not overwrite. If an existing rule conflicts with the kernel defaults,
record the conflict and ask the user before resolving it.

## Blank Projects

If the target has no code, use source documents and user answers to mount the
harness. Keep architecture and validation docs in draft status until enough
project depth exists.

## Existing Codebases

If the target has code, inspect maturity before recommending architecture. Do
not propose a broad refactor for mature projects unless the user asks for it.
