# Setup Prompt

Use this prompt when dropping Agent Harness Kernel into a project.

```text
Scan this repo and mount Agent Harness Kernel for this project.

First inspect the existing files, rules, code, docs, tests, deployment setup,
and any source materials. Preserve and fuse existing project rules instead of
overwriting them.

Before implementation, grill me on unclear product, stack, deployment, evidence,
workflow, quality, and collaboration decisions. Always prefer asking over
assuming during harness mounting.

Use `kernel/MOUNTING_GUIDE.md`, `kernel/QUESTIONNAIRE.md`, and
`kernel/templates/agents/` as setup material.

Create or update the project-local `agents/` harness, including current state,
project profile, source manifest, questions summary, assumptions, ADRs,
planning docs, architecture docs where useful, validation gates, review
protocol, capability scan, and local gitignore for agent-only memory.

Run a harness review. If subagents are available, use one for review. If not,
document the downgrade and perform a clearly labeled single-agent review.

Run `scripts/harness_doctor.py --root <target-project>` after mounting. Treat
hard blockers as mount failures and warnings as issues to summarize for the
user.

Do not implement application code until I accept the mounted harness, unless I
explicitly override that gate after you explain the risk.
```

## Expected Agent Output

The agent should produce:

- a mounted `agents/` harness;
- root `AGENTS.md` updates or a safe merge proposal;
- a capability scan;
- a dated harness mount review;
- a questions summary;
- initial ADRs for important setup decisions;
- a clear next action and acceptance gate.
