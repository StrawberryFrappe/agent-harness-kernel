# Validation Gates

## Required Gates

| Gate | Applies When | Pass Criteria | Evidence |
|---|---|---|---|
| GATE-HM Harness Mounted | Always | Harness accepted by user after review | Harness mount review |
| GATE-LOCAL Local Mount | Always | `agents/local/CAPABILITIES.md` exists and is current | The file itself |
| GATE-DR Doctor | Always | No unresolved hard blockers | `agents/validation/DOCTOR.md` |
| GATE-TEST Tests | Code projects | Relevant tests pass | Test output / CI |
| GATE-DEPLOY Deployment | Deployable projects | Target deployment verified or blocker recorded | Deployment evidence |
| GATE-PQ Portfolio Quality | User-facing projects | Visible output is credible, polished, and demonstrable | Screenshots / review |

## Local Mount Gate

Implementation work requires the local half of the harness to exist. A harness
that does not know what its agent can do will either plan work the environment
cannot perform, or quietly downgrade a review to a single-agent pass without
saying so.

Because `agents/local/` never travels with the repository, every clone lands
without it and is forced through the setup. That is how the harness re-adapts to
each machine rather than arriving pre-loaded with its author's environment.

Reading documents and making trivial corrections are not blocked. The doctor
reports the absence as a warning, and as a hard blocker under `--strict`.

Setup instructions are in `agents/LOCAL_SETUP.md`, which is committed precisely
because the directory it describes is not.

## Portfolio Quality Gate

For user-facing products, the project fails this gate if it looks technically
present but embarrassing to show:

- scaffold or route-list UI;
- weak copy that describes implementation instead of product behavior;
- missing important states such as loading, empty, error, or success;
- controls that do not map to tested behavior;
- screenshots that do not prove real workflows.

## Rules

- Passing tests are not enough when the visible product is weak.
- Every gate names its evidence. A gate whose evidence is a claim rather than an
  artifact has not been passed.
