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
planning docs, architecture docs where useful, validation gates, and review
protocol.

Produce both halves. `agents/` is project truth and is shared. Environment
truth — what this agent can do, where this checkout lives, which binaries this
project needs — goes in `agents/local/`, which is never committed, together with
raw agent memory. Write the capability scan there, not into a committed
document. Commit `agents/LOCAL_SETUP.md` so the next machine knows what to build.

Ask whether anyone else works in this repository, what tooling and language they
use, and whether ADRs need author slugs. Ask before assuming it is a solo
project.

Run a harness review. If subagents are available, use one for review. If not,
document the downgrade and perform a clearly labeled single-agent review.

Run `scripts/harness_doctor.py --root <target-project>` after mounting. Treat
hard blockers as mount failures and warnings as issues to summarize for the
user.

Then STOP and present the mounted harness for my explicit acceptance. This
acceptance gate is mandatory and unconditional: it applies no matter how small
the project is, no matter how confident you are, and no matter how much context
you already have. Auto-filling docs from prior context is not a substitute for
my acceptance — it is exactly the case that most needs a double-check. Surface
every assumption you made (including "safe" ones) and wait. Do not build,
compile, edit application code, or run project tooling until I accept, unless I
explicitly override this gate after you explain the risk.
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
