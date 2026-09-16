# Handoff

**This file is a letter, not a journal.** One agent writes it when it stops;
the next agent reads it and then **empties it back to this template**. Consuming
a handoff is what destroys it.

There is at most one handoff at a time. Content here means someone is mid-pass.
An empty template means nobody is.

Do not add a dated section per delivery. That is history, and history goes in
`agents/record/`, under a folder per developer per day. A handoff that has grown
dated sections was never consumed, and `harness_doctor.py` warns about it.

**Written:** TBD

While this reads `TBD`, the handoff is empty and nobody is mid-pass. Put the
date here when you write one, and set it back to `TBD` when you consume one.
`harness_doctor.py` reads this line to tell a live handoff from a spent one.

## Current State

TBD

## What Was Done

TBD

## What Was Verified

TBD

## What Was Not Done

TBD

## Blockers

TBD

## Next Exact Action

TBD

## Required Reads For Next Agent

1. `AGENTS.md`
2. `agents/RUN_STATE.md`
3. Recent entries under `agents/record/`
4. Relevant local logbook notes from `agents/local/logbook/YYYYMMDD/`, if
   available
5. Latest relevant review under `agents/reviews/`
6. `agents/planning/BACKLOG.md`

## On Pickup

1. Read the above.
2. If the work it describes is still live, carry it on.
3. Write anything durable into `agents/record/` before it is lost.
4. **Reset this file to the template**, `Written:` back to `TBD`. The letter has
   been delivered.
