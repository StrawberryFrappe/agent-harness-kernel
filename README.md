# Agent Harness Kernel

Agent Harness Kernel is a compact, project-specific harness starter for agentic
coding work across Codex, Claude Code, Gemini-style agents, and similar tools.

The kernel is not a factory runtime. It is a portable setup kit that helps an
agent inspect a repository, grill the user on missing decisions, and mount a
project-specific `agents/` harness that becomes the local source of truth.

## Intended Use

1. Clone or copy this repo into a new or existing project.
2. Ask the agent to run the setup prompt in `SETUP_PROMPT.md`.
3. The agent inspects the actual project, fuses existing rules, asks questions,
   and mounts or updates the project-local harness.
4. The user reviews the mounted harness.
5. Implementation starts only after user acceptance.

Useful setup references:

- `kernel/MOUNTING_GUIDE.md`
- `kernel/QUESTIONNAIRE.md`
- `scripts/harness_doctor.py`

The mounted harness is committed to the project by default. Local agent memory,
raw Q&A, scratch notes, and copied kernel provenance stay under `agents/local/`
in the target project and are ignored by git.

## Design Goals

- Project-specific over generic ceremony.
- Robust across machines and agent platforms.
- Explicit about real capability limits.
- Strong enough for serious projects, small enough to follow.
- Honest about what was done, delegated, simulated, skipped, or deferred.
- Built for iterative work: inspect, ask, decide, implement, verify, report.

## Mounted Shape

The active project harness should look like:

The template for the mounted harness lives under `kernel/templates/agents/`.
During mounting, the agent copies and adapts that template into the target
project's root as `agents/`.

After mounting, run:

```bash
python scripts/harness_doctor.py --root <target-project>
```

After mounting, `agents/local/**` is ignored. Everything else in the mounted
`agents/` tree is intended to be project-owned documentation and should usually
be committed.

## Non-Goals

- Do not simulate autonomous agents and call it real orchestration.
- Do not replace platform-native permissions, sandboxing, or review tools.
- Do not force a single frontend template, stack, or process on every project.
- Do not preserve kernel files just because they came from this repo.

Once mounted, the project-specific harness wins over the generic kernel.
