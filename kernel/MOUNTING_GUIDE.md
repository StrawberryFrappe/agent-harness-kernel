# Mounting Guide

This guide is for agents mounting Agent Harness Kernel into a target project.

## Key Distinction

The `kernel/templates/agents/` directory is not an active harness. It is a
template. The active harness exists only after the agent adapts it into the
target project as `agents/`.

## Mounting Steps

1. Inspect the target repository before editing.
2. Inventory existing rules: `AGENTS.md`, `CLAUDE.md`, README, contribution
   docs, CI docs, scripts, tests, and deployment notes.
3. Run the capability scan. If subagents are unavailable, record the downgrade.
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
11. Ask the user to accept or reject the mounted harness.

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
