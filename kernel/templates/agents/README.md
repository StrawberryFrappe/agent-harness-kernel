# Project Agent Harness

This directory is the active project-specific harness. It is the operating
contract for agentic work in this repository.

## Two Halves

What lives here is **project truth**: shared, committed, the same for everyone.

**Environment truth** — what your agent can do, where your checkout is, which
binaries you invoke — lives in `agents/local/`, which is never committed. Every
clone arrives without it, and building it is how the harness adapts to the
machine it landed on. Start at `agents/LOCAL_SETUP.md`.

## Read Order

1. `AGENTS.md`
2. `agents/RUN_STATE.md`
3. `agents/LOCAL_SETUP.md`, and your own `agents/local/CAPABILITIES.md`
4. `agents/intake/PROJECT_BRIEF.md`
5. `agents/intake/PROJECT_PROFILE.md`
6. `agents/intake/SOURCE_MANIFEST.md`
7. `agents/intake/QUESTIONS_SUMMARY.md`
8. `agents/planning/ROADMAP.md`
9. `agents/planning/BACKLOG.md`
10. `agents/architecture/TECH_STACK.md`
11. `agents/validation/GATES.md`
12. `agents/execution/WORKFLOW.md`
13. `agents/i18n/TRANSLATION_PROTOCOL.md`, when the project carries more than one
    working language
14. Latest dated review under `agents/reviews/`
15. Recent entries under `agents/record/`, when you need to know what was
    happening rather than where things stand

## Where A Fact Goes

Route by what kind of fact it is. An earlier version of this harness listed
destinations without saying which got what, and the narrative ones converged
into duplicate journals.

| Kind of fact | Goes to | Lifecycle |
|---|---|---|
| Where the work stands **now** | `agents/RUN_STATE.md` | Replaced, never appended |
| What happened, as it happened | `agents/record/<SLUG>-<YYYYMMDD>/` | Small files, added not groomed |
| The baton for the next agent | `agents/execution/HANDOFF.md` | Emptied when consumed |
| A decision and its rationale | `agents/adrs/` | Write-once, superseded not edited |
| An answered question | `agents/intake/QUESTIONS_SUMMARY.md` | Moves from open to answered |
| An assumption | `agents/intake/ASSUMPTIONS.md` | Retired when proven or disproven |
| What could be done and why | `agents/planning/BACKLOG.md` | Status-free registry |
| Proof a claim is true | `agents/validation/EVIDENCE_INDEX.md` | Append a row |
| A critique of work | `agents/reviews/`, indexed in `reviews_index.md` | Write-once |
| Structure and stack | `agents/architecture/` | Replaced as it changes |
| Environment truth — machine paths, tooling, capabilities | `agents/local/` | Never committed |

If a fact seems to belong in two of these, it is probably two facts.

## Operating Rules

- Do not start implementation until the mounted harness is accepted.
- Do not start implementation until the local half exists. See GATE-LOCAL in
  `agents/validation/GATES.md`.
- Existing project rules are preserved and fused into this harness.
- Ask the user when product, stack, deployment, quality, or evidence decisions
  are unclear.
- Decide review strength from your own capability scan, not from a committed
  document or another developer's review.
- Keep environment truth under `agents/local/`; it is never committed.
- **Every change to `RUN_STATE.md` needs a matching entry in `agents/record/`.**
  Status says where things stand; the record says how they got there. Updating
  one without the other is how the story gets lost.
- Promote important decisions into ADRs, planning docs, validation docs, or
  architecture docs.
- Record status in `agents/RUN_STATE.md` only, keep it short, and keep it in the
  present tense. Planning documents describe what the work is and why;
  duplicating its state across several files is how those files go stale.
- Narrative of what happened goes in `agents/record/`, under a folder per
  developer per day. It is a dump, not a document — write as you go.
- A handoff is a letter, not a journal. Whoever picks one up empties it.
- Cite artifacts rather than asserting them. A citation is checkable, and the
  doctor checks that cited paths exist.
- If harness drift is detected, stop, write a handoff, and ask for continuation
  with refreshed context.

## Completion Standard

Work is complete only when the project-specific validation gates pass, or when
the remaining blocker is explicitly documented and accepted by the user.
