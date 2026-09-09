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

## Collaboration

Ask these even when the repository looks like one person's work. The answers
decide naming, language, and whether the harness is shared at all.

- **Does anyone else work in this repository?** If so, how many people?
- What agent and tooling do they use? A harness written for one agent can
  mislead another.
- **What language do they work in?** If contributors do not share a working
  language, decide which one the harness is written in, and whether translations
  are expected. Name the canonical language so it does not drift, and mount the
  translation protocol template so the second copy has a defined relationship to
  the first rather than an assumed one.
- Will more than one person create ADRs or reviews? If yes, agree author slugs
  now and record them in an ADR. See the naming rules in the workflow template.
- Who owns which parts of the codebase, and is that division a preference or a
  contract?
- How do decisions reach the people not in this conversation?

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
- Which tasks should be delegated?
- How should the agent report deviations?
- What should happen if the user says "just build it"?
- How is concurrent work isolated, if it happens at all?

## Privacy And Memory

- Is the harness committed, or kept out of the repository? If it is kept out,
  what is it being kept from, and for how long?
- What project facts should be committed?
- What belongs in the local half — machine paths, capabilities, tooling, raw
  session notes? Apply the test: would another developer's agent get confused if
  it had this?
- What should be promoted into ADRs or durable docs?

## Capabilities

These answers go into `agents/local/CAPABILITIES.md`, not into a committed
document, because they describe one machine rather than the project.

- Which agent and platform is this, and does it have subagents?
- Which integrations are connected, and which are actually authorised?
- May the agent create sandboxes or git worktrees?
- Which binaries and paths does this project need locally?
