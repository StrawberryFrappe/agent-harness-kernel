# Validation Gates

## Required Gates

| Gate | Applies When | Pass Criteria | Evidence |
|---|---|---|---|
| GATE-HM Harness Mounted | Always | Harness accepted by user after review | Harness mount review |
| GATE-DR Doctor | Always | No unresolved hard blockers | `agents/validation/DOCTOR.md` |
| GATE-TEST Tests | Code projects | Relevant tests pass | Test output / CI |
| GATE-DEPLOY Deployment | Deployable projects | Target deployment verified or blocker recorded | Deployment evidence |
| GATE-PQ Portfolio Quality | User-facing projects | Visible output is credible, polished, and demonstrable | Screenshots / review |

## Portfolio Quality Gate

For user-facing products, the project fails this gate if it looks technically
present but embarrassing to show:

- scaffold or route-list UI;
- weak copy that describes implementation instead of product behavior;
- missing important states such as loading, empty, error, or success;
- controls that do not map to tested behavior;
- screenshots that do not prove real workflows.

## Rule

Passing tests are not enough when the visible product is weak.
