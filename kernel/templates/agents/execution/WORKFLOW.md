# Workflow

## Harness Mounting

1. Inspect existing project files.
2. Preserve and fuse existing rules.
3. Run capability scan.
4. Grill the user on unclear decisions.
5. Summarize answers.
6. Draft or update project-specific harness files.
7. Run review.
8. Wait for user acceptance.

## Implementation

1. Plan the task.
2. Review the plan, preferably with a subagent.
3. Implement within accepted scope.
4. Verify with the agreed gates.
5. Review the result.
6. Update traceability and evidence. Write local logbook notes under
   `agents/local/logbook/` when useful, then promote durable facts into
   committed docs.
7. Report what was done and what remains.

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
4. Recommend context compression or a fresh continuation when appropriate.
