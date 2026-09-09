#!/usr/bin/env python3
"""Validate a mounted Agent Harness Kernel target.

This script checks the target project's active harness. It does not mount the
harness and it does not validate product correctness.

A green run is a STRUCTURAL check, not a truth check. It confirms that required
files exist, that cited paths resolve, and that local memory is really ignored.
It cannot confirm that what a document says is true, and must never be cited as
evidence that a document's claims are accurate.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import re
import subprocess
import sys
from pathlib import Path


# Absence is a hard blocker: the harness does not function without these.
REQUIRED_FILES = [
    "AGENTS.md",
    "agents/README.md",
    "agents/RUN_STATE.md",
    "agents/intake/PROJECT_BRIEF.md",
    "agents/intake/PROJECT_PROFILE.md",
    "agents/intake/SOURCE_MANIFEST.md",
    "agents/intake/QUESTIONS_SUMMARY.md",
    "agents/planning/BACKLOG.md",
    "agents/planning/TRACEABILITY.md",
    "agents/validation/GATES.md",
    "agents/validation/DOCTOR.md",
    "agents/execution/WORKFLOW.md",
    "agents/execution/REVIEW_PROTOCOL.md",
    "agents/reviews/reviews_index.md",
    "agents/local/.gitignore",
]

# Absence is a warning: the mount works, but the kernel's read order and mounting
# guide expect these, so a mount without them has probably skipped a step.
EXPECTED_FILES = [
    "agents/intake/ASSUMPTIONS.md",
    "agents/planning/ROADMAP.md",
    "agents/planning/WORK_ITEMS.md",
    "agents/validation/TEST_STRATEGY.md",
    "agents/validation/EVIDENCE_INDEX.md",
    "agents/execution/HANDOFF.md",
    "agents/execution/LOGBOOK_POLICY.md",
    "agents/architecture/TECH_STACK.md",
]

PLACEHOLDER_MARKERS = [
    "TBD",
    "TODO",
    "HOLD / APPROVE WITH FIXES / APPROVE",
    "unknown | Not checked",
]

# Referential integrity. A backtick span with no whitespace is the kernel's own
# citation style. Candidate prefixes are derived from the target at run time
# rather than hardcoded, so the check configures itself for any project layout.
BACKTICK_SPAN = re.compile(r"`([^`\s]+)`")
LINE_SUFFIX = re.compile(r":\d+$")
REF_SKIP_TOKENS = ("*", "<", ">", "YYYYMMDD", "://")

DATED_DIR = re.compile(r"^(\d{4})(\d{2})(\d{2})$")


class Report:
    """Findings carry a category so severity can be reasoned about per check."""

    def __init__(self) -> None:
        self.blockers: list[tuple[str, str]] = []
        self.warnings: list[tuple[str, str]] = []

    def block(self, category: str, message: str) -> None:
        self.blockers.append((category, message))

    def warn(self, category: str, message: str) -> None:
        self.warnings.append((category, message))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def relative(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def collect_markdown(root: Path) -> list[Path]:
    agents = root / "agents"
    if not agents.exists():
        return []
    return [
        path
        for path in agents.rglob("*.md")
        if "/local/" not in path.as_posix().replace("\\", "/")
        and "/templates/" not in path.as_posix().replace("\\", "/")
    ]


def derive_prefixes(root: Path) -> set[str]:
    """Top-level directories of the target, used to recognise path citations."""
    try:
        return {
            item.name
            for item in root.iterdir()
            if item.is_dir() and not item.name.startswith(".")
        }
    except OSError:
        return set()


def check_references(root: Path, report: Report) -> None:
    """Every cited path must resolve. A citation is where a claim becomes checkable.

    Harness-internal references are fully under the harness's control, so a broken
    one is a blocker. References out into project source may be kernel-relative or
    may legitimately have moved, so those are warnings.
    """
    prefixes = derive_prefixes(root)
    if not prefixes:
        return
    for path in collect_markdown(root):
        seen: set[str] = set()
        for raw in BACKTICK_SPAN.findall(read_text(path)):
            if any(token in raw for token in REF_SKIP_TOKENS):
                continue
            if "/" not in raw:
                continue
            ref = LINE_SUFFIX.sub("", raw).rstrip("/")
            if ref.split("/", 1)[0] not in prefixes:
                continue
            if ref.startswith("agents/local/"):
                continue  # gitignored by design; frequently absent
            if ref in seen or (root / ref).exists():
                continue
            seen.add(ref)
            message = f"{relative(path, root)} cites a path that does not exist: {ref}"
            if ref.startswith("agents/"):
                report.block("references", message)
            else:
                report.warn("references", message)


def check_local_ignored(root: Path, report: Report) -> None:
    """Ask git for effective behaviour rather than reading the ignore file.

    A text check cannot see a parent .gitignore negation. Falls back to the older
    substring test when git is unavailable or the target is not a repository.
    """
    local_dir = root / "agents" / "local"
    ignore_file = local_dir / ".gitignore"
    probe = local_dir / ".doctor-probe"
    if local_dir.is_dir():
        try:
            probe.write_text("", encoding="utf-8")
            result = subprocess.run(
                ["git", "-C", str(root), "check-ignore", "-q", str(probe)],
                capture_output=True,
            )
            # 0 = ignored, 1 = definitively not ignored, anything else (128) means
            # git could not answer - usually not a repository - so fall back rather
            # than blocking a target that was exported or copied out of git.
            if result.returncode == 0:
                return
            if result.returncode == 1:
                report.block(
                    "local-memory",
                    "agents/local/ is not actually ignored by git",
                )
                return
        except (OSError, subprocess.SubprocessError):
            pass  # fall through to the text check
        finally:
            try:
                probe.unlink()
            except OSError:
                pass
    if ignore_file.exists() and "*" not in read_text(ignore_file):
        report.block(
            "local-memory",
            "agents/local/.gitignore does not ignore local memory by default",
        )


def check_root_agents(root: Path, report: Report) -> None:
    root_agents = root / "AGENTS.md"
    if not root_agents.exists():
        return
    text = read_text(root_agents)
    if "agents/" not in text.lower():
        report.block(
            "discovery",
            "AGENTS.md does not point agents to the mounted agents/ harness",
        )
        return
    # A bare substring can be satisfied by prose, a code fence, or a sentence
    # saying the harness was removed. Naming the read order is stronger.
    missing = [
        name
        for name in ("agents/README.md", "agents/RUN_STATE.md")
        if name not in text
    ]
    if missing:
        report.warn(
            "discovery",
            f"AGENTS.md does not name the read-order entry points: {', '.join(missing)}",
        )


def check_reviews(
    root: Path, report: Report, strict: bool, stale_days: int | None
) -> None:
    reviews_root = root / "agents" / "reviews"
    if not reviews_root.exists():
        report.warn("reviews", "agents/reviews/ does not exist")
        return

    today = _dt.date.today()
    newest: _dt.date | None = None

    for item in sorted(reviews_root.iterdir()):
        if not item.is_dir():
            continue
        match = DATED_DIR.match(item.name)
        if not match:
            continue
        try:
            folder_date = _dt.date(*(int(part) for part in match.groups()))
        except ValueError:
            report.warn("reviews", f"{relative(item, root)} is not a valid date")
            continue
        if folder_date > today:
            report.warn("reviews", f"{relative(item, root)} is dated in the future")
        newest = folder_date if newest is None else max(newest, folder_date)

        review_files = list(item.glob("*.md"))
        if not review_files:
            message = f"{relative(item, root)} has no review markdown files"
            if strict:
                report.block("reviews", message)
            else:
                report.warn("reviews", message)
        for review in review_files:
            text = read_text(review)
            if "TBD" in text or "HOLD / APPROVE WITH FIXES / APPROVE" in text:
                report.block(
                    "reviews",
                    f"{relative(review, root)} looks like an unfilled dated review",
                )

    if stale_days is not None and newest is not None:
        age = (today - newest).days
        if age > stale_days:
            report.warn(
                "reviews",
                f"newest dated review is {age} days old (threshold {stale_days})",
            )


def check_adrs(root: Path, report: Report) -> None:
    adrs = root / "agents" / "adrs"
    if not adrs.is_dir():
        report.warn("adrs", "agents/adrs/ does not exist")
        return
    # The kernel ships 0001 as a default. A mount carrying only that one recorded
    # no decisions of its own, which usually means nobody was grilled.
    own = [path for path in adrs.glob("*.md") if not path.stem.endswith("0001")]
    if not own:
        report.warn(
            "adrs",
            "no ADR beyond the kernel default 0001 - were any decisions recorded?",
        )


def check_template_identity(root: Path, kernel: Path, report: Report) -> None:
    """Byte-identical to the template is the strongest available signal that no
    adaptation happened. Always a warning: identity is sometimes a real decision,
    and the point is to make the mounting agent say so, not to forbid it."""
    template_root = kernel / "kernel" / "templates" / "agents"
    if not template_root.is_dir():
        report.warn("adaptation", f"no template tree at {template_root}")
        return
    for template in sorted(template_root.rglob("*.md")):
        target = root / "agents" / template.relative_to(template_root)
        if not target.exists():
            continue
        try:
            if target.read_bytes() == template.read_bytes():
                report.warn(
                    "adaptation",
                    f"{relative(target, root)} is byte-identical to the kernel template",
                )
        except OSError:
            continue


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Check a mounted Agent Harness Kernel project."
    )
    parser.add_argument("--root", default=".", help="Target project root to check.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat placeholders and empty dated review folders as hard blockers.",
    )
    parser.add_argument(
        "--kernel",
        default=None,
        help="Path to the kernel, enabling the template-adaptation check.",
    )
    parser.add_argument(
        "--stale-days",
        type=int,
        default=None,
        help="Warn when the newest dated review is older than this many days.",
    )
    parser.add_argument(
        "--warnings-as-errors",
        action="store_true",
        help="Exit non-zero when any warning is reported, for CI use.",
    )
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    report = Report()

    for rel in REQUIRED_FILES:
        if not (root / rel).exists():
            report.block("required-files", f"missing required file: {rel}")

    for rel in EXPECTED_FILES:
        if not (root / rel).exists():
            report.warn("expected-files", f"missing expected file: {rel}")

    check_root_agents(root, report)
    check_local_ignored(root, report)
    check_adrs(root, report)
    check_references(root, report)
    check_reviews(root, report, args.strict, args.stale_days)

    for path in collect_markdown(root):
        text = read_text(path)
        hits = [marker for marker in PLACEHOLDER_MARKERS if marker in text]
        if hits:
            message = (
                f"{relative(path, root)} contains placeholder markers: "
                f"{', '.join(hits)}"
            )
            if args.strict:
                report.block("placeholders", message)
            else:
                report.warn("placeholders", message)

    if args.kernel:
        check_template_identity(root, Path(args.kernel).resolve(), report)

    print("Agent Harness Doctor")
    print(f"root: {root}")
    print(f"hard_blockers: {len(report.blockers)}")
    for category, item in report.blockers:
        print(f"BLOCKER [{category}]: {item}")
    print(f"warnings: {len(report.warnings)}")
    for category, item in report.warnings:
        print(f"WARNING [{category}]: {item}")

    if report.blockers:
        return 1
    if args.warnings_as_errors and report.warnings:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
