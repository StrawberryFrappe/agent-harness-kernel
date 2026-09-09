# Translation Protocol

A project whose contributors do not share a working language ends up with the same
document twice. This file defines how the second copy relates to the first, so that
drift between them is detected mechanically rather than noticed too late.

## Canonical Language

Every translatable document has exactly one canonical file, `FOO.md`. A translation
lives beside it as `FOO.<lang>.md`, where `<lang>` is a lowercase ISO 639-1 code.
The canonical language is named once, during the mount, and recorded in an ADR — not
inferred per file from whichever language a document happens to be written in.

**Canonical wins.** Where a translation and its source disagree, the source is
authoritative until the translation is brought current. A translation is a view of a
decision, never the place a decision is made.

## The One Test

> Does this translation's recorded `source_sha` still match the hash of the canonical
> file it names?

If yes, the translation was written against the source as it stands. If no, the source
moved and the translation has not caught up. That is all the test claims — a matching
hash does not mean the translation is *good*, only that it is not stale.

## Frontmatter

Every `FOO.<lang>.md` opens with:

```yaml
---
source: agents/path/to/FOO.md
source_sha: 3f2a9c1e8b7d4a6f0c5e2b9d8a1f4c7e3b6d9a2f
source_sha_algo: git-blob-sha1
translated: 2026-01-31
translator: agent
---
```

| Field | Meaning |
|---|---|
| `source` | Repository-relative path to the canonical file this translation tracks |
| `source_sha` | The canonical file's hash at the moment this translation was last brought current |
| `source_sha_algo` | Names the algorithm, so a later tooling change cannot silently misread an old value |
| `translated` | Date of the last translate-on-touch pass, for human triage |
| `translator` | Who or what produced it. Optional, and useful once more than one person or agent does |

The canonical file carries no frontmatter of its own. It does not need to know it has
been translated, and a list of its translations would be one more thing to keep current.

## Computing And Checking `source_sha`

Use git's own blob hash, with filters off:

```bash
git hash-object --no-filters agents/path/to/FOO.md
```

It needs no tooling the project does not already have. **`--no-filters` is not
optional.** Without it, git applies whatever line-ending conversion the local
`core.autocrlf` is set to, so two contributors can hash the same unchanged file and
get two different answers — the protocol would then report drift that does not exist,
which is worse than reporting none at all. Harness markdown is frequently CRLF, and a
project that has not pinned line endings in `.gitattributes` cannot assume its
contributors are configured alike. `--no-filters` hashes the bytes on disk rather
than a version of them that depends on local configuration.

Checking is the same command run against the current canonical file, compared to the
value in the translation's frontmatter. A mismatch is a fact, not a verdict — it says
the source changed, and nothing about whether the change mattered.

**The limit of this, stated plainly:** hashing bytes on disk is deterministic given
the same bytes on disk, which is not the same as being platform-independent. A
project whose contributors check out different line endings — some CRLF, some LF —
will see mismatches on files nobody edited. If that describes the project, pin the
line endings in `.gitattributes` (`*.md text eol=lf` is the usual answer) so every
working tree agrees, and the hash becomes stable everywhere. Do that once, at the
mount, rather than discovering it from a false alarm later.

## Translate On Touch

- **Whoever edits `FOO.md` updates `FOO.<lang>.md` in the same change** — or leaves it
  stale deliberately and says so in the change itself.
- Silent drift is the failure this protocol exists to prevent. Visible drift — flagged,
  dated, explained — is an acceptable interim state and sometimes the honest one.
- Refreshing a translation means re-reading the source in full, not patching the lines
  that look new. A diff of the source is a hint about where to look, not the work.

## What Gets Translated

Translate what a reader working in the non-canonical language must act on. That is
usually onboarding material, the operating rules they are held to, and the documents
naming their own area of the codebase.

Not everything earns a translation. Dated records — reviews, evidence entries, logbook
notes — are read rarely and by whoever went looking for them; translating them doubles
the maintenance surface for very little. Decide per document, and record the decision
somewhere a future contributor will find it rather than re-deriving it.

## Terminology

Terms bind to the project's glossary, wherever the project keeps one. A translation
must never invent its own rendering of a term the glossary already defines, and a term
that has no agreed translation belongs in the glossary before it appears in prose.

Where the canonical language's term is the one the team actually says out loud, keep it
untranslated and say so in the glossary. Translating a word nobody uses is worse than
leaving it alone.

## What Stays Untranslated

Human-authored source material from outside the harness — specifications, briefs,
reference documents supplied to the project — is out of scope. Quote it in its original
language and attribute it. Retranslating someone else's document to make it consistent
with the harness silently replaces their words with the agent's.

## Keeping It Current

This file names no language pair. Fill in `<lang>` per project, and add a worked example
only once the project has actually exercised the protocol — a hypothetical example is
worse than none, because it gets copied.

When the canonical language itself changes, that is an ADR, not an edit here.
