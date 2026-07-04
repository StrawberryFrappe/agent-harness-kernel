# Traceability

Traceability links sources, user decisions, ADRs, work items, tests, evidence,
and final behavior.

| Trace ID | Source / Decision | Work Item | Verification | Evidence |
|---|---|---|---|---|
| TR-001 | Kernel mount requested | WI-001 | Harness review | agents/reviews/ |

## Rules

- Traceability should grow as the project evolves.
- For requirements-heavy projects, preserve source-backed IDs.
- For lightweight projects, trace decisions and outcomes instead of inventing
  artificial requirements.
- Do not expose internal trace IDs in user-facing products unless the product
  itself is an admin/audit tool and the user approves it.
