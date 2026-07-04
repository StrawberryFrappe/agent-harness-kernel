# Review Protocol

## Review Types

- Harness mount review
- Capability scan
- Maturity review
- Plan review
- Implementation review
- Adversarial review
- Final review

## Severity

- P0: blocking
- P1: blocking unless explicitly mitigated
- P2: should fix or document
- P3: optional improvement

## Rules

- Use subagents for review when available.
- If subagents are unavailable, label the review as single-agent and record the
  downgrade.
- Findings should cite files, commands, screenshots, or source evidence.
- Do not count simulated roles as autonomous review.
- A blocking review finding must update `agents/RUN_STATE.md`.
