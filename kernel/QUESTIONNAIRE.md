# Mount Questionnaire

Ask these during harness mounting. Do not ask all questions as a giant form if
the answer is already clear from repository evidence; summarize what you found
and ask only for confirmation.

## Product

- What is the product or system supposed to do?
- Who uses it?
- What would make the project successful?
- What is explicitly out of scope?
- Is this for portfolio, coursework, production, internal use, or experiment?

## Source Authority

- What documents, tickets, designs, rubrics, or conversations are source of
  truth?
- Which source wins if sources conflict?
- Are there source-backed requirement IDs to preserve?
- Are drafts allowed to evolve into requirements?

## Stack

- Is there an existing stack?
- Is the current stack accepted or open to change?
- If no stack exists, what constraints matter: speed, deployability, hiring,
  learning value, cost, offline use, mobile, accessibility, data, or security?

## Architecture

- Is the project new, prototype, early product, mature, legacy, or rescue?
- Are broad architecture changes allowed?
- Should the harness create an SRS now?
- Are C4 or 4+1 diagrams useful for this project?

## Quality Bar

- What must be tested?
- What evidence does the user actually inspect?
- Does user-facing polish matter?
- Should `GATE-PQ Portfolio Quality` be active?
- What would be embarrassing to ship or show?

## Deployment

- Is deployment in scope?
- Where should it run?
- Are credentials or target hosts available?
- If deployment is deferred, what local evidence is enough for now?

## Workflow

- Should implementation be blocked until harness acceptance?
- Are subagents available on this platform?
- Which tasks should be delegated?
- How should the agent report deviations?
- What should happen if the user says "just build it"?

## Privacy And Memory

- What project facts should be committed?
- What personal or raw context should stay local under `agents/local/`?
- What should be promoted into ADRs or durable docs?
