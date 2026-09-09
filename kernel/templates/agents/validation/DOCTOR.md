# Doctor Workflow

Doctor is a harness coherence check, not a product runtime.

## What A Green Run Does Not Mean

**A green doctor run is a structural check, not a truth check.** It confirms that
required files exist, that cited paths resolve, and that local memory is really
ignored. It cannot tell whether a document's content is accurate, whether an open
question was quietly answered by inference, or whether an assumption has been
laundered into a requirement.

Never cite a clean doctor run as evidence that a document's claims are true. That
is what the reviews under `agents/reviews/` are for.

## Running It

```bash
python scripts/harness_doctor.py --root <target-project>
```

| Flag | Effect |
|---|---|
| `--strict` | Placeholders and empty dated review folders become hard blockers |
| `--kernel <path>` | Enables the template-adaptation check |
| `--stale-days N` | Warn when the newest dated review is older than N days |
| `--warnings-as-errors` | Exit non-zero on any warning, for CI |

Findings are tagged with a category so severity can be reasoned about per check.

## Hard Blockers

- A required file is missing.
- Root `AGENTS.md` does not point to `agents/`.
- **A document cites a path under `agents/` that does not exist.** A citation is
  where a claim becomes checkable; an unresolvable one usually means the artifact
  was never written.
- `agents/local/` is not actually ignored by git, as reported by `git check-ignore`
  rather than by reading the ignore file.
- A dated review looks unfilled.
- `agents/RUN_STATE.md` does not show the current phase.
- Implementation is marked ready before harness review and user acceptance.
- Existing project rules were overwritten or ignored without a recorded decision.
- Major stack, product or deployment decisions are undocumented.
- Validation gates do not identify evidence.

## Warnings

- An expected file is missing — the mount works, but the read order expects it.
- A document cites a path outside `agents/` that does not exist. Softer, because
  such a reference may be kernel-relative or may legitimately have moved.
- `AGENTS.md` does not name the read-order entry points.
- No ADR exists beyond the kernel default `0001`, which usually means nobody was
  grilled.
- An active document is byte-identical to its kernel template. Sometimes a real
  decision; the point is to make it a stated one rather than an oversight.
- A dated review folder is empty, or dated in the future.
- Placeholder sections remain.
- Traceability is sparse, or the deployment target is deferred.
- Subagents are unavailable, reducing review strength.

## Doctor Record

| Date | Result | Hard Blockers | Warnings | Next Action |
|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD |

## Script Policy

The script is a guardrail against theatrical completion, not the authority. The
workflow in `execution/WORKFLOW.md` and the gates in `validation/GATES.md` remain
authoritative.
