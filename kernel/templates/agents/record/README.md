# Record

Running notes on what was actually happening, as it happened. Committed and
shared, so it survives the machine it was written on.

This is a **dump, not a document.** Nobody is expected to read it end to end.
It exists so that when something turns out to matter later, there is a trace.

## Shape

```text
agents/record/<SLUG>-<YYYYMMDD>/<whatever>.md
```

One folder per developer per day. `SLUG` is the author slug already used for
ADRs and reviews — `JZ`, `FS`. Inside, small files, one per session or per
thing. Name them however is obvious at the time.

```text
agents/record/JZ-20260916/pause-menu.md
agents/record/JZ-20260916/harness-cleanup.md
agents/record/FS-20260916/camera-limits.md
```

## Rules, Such As They Are

- **Low ceremony.** Notes, not reports. No required headings, no template to
  fill, no completeness bar. A paragraph is a fine entry.
- **Write, then leave it alone.** Do not groom old entries to keep them
  accurate. An entry says what someone believed that day, which is the useful
  part. Correct it in a newer entry.
- **Incremental.** Add as you go. Do not save it up for a tidy summary at the
  end; the summary is what never gets written.
- **Cite where you can.** A commit, an evidence ID, a review folder. A note
  that points at something checkable is worth several that do not.

## Why Folders Per Developer Per Day

Two people working at once write into two different folders, so git merges
their notes with no conflict. That is the same trick ADRs and `agents/reviews/`
already use, and neither has ever collided.

It is also why this can be committed at all. A single shared journal file
conflicts on every session — which is what pushed raw notes into the gitignored
`agents/local/logbook/` in the first place. What genuinely belongs in the local
half is **environment** truth: machine paths, capability scans, context notes
about one agent on one box. The story of what the project did is project truth.

## Not Here

- **Status** — where things stand now is `agents/RUN_STATE.md`, only there.
- **The handoff** — `agents/execution/HANDOFF.md`, emptied when consumed.
- **Plans** — what could be done and why is `agents/planning/BACKLOG.md`.
- **Decisions** — an ADR, if it is durable enough to bind future work.
- **Environment truth** — `agents/local/`.
