#!/usr/bin/env python3
"""Validate a mounted Agent Harness Kernel target.

This script checks the target project's active harness. It does not mount the
harness and it does not validate product correctness.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


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

PLACEHOLDER_MARKERS = [
    "TBD",
    "TODO",
    "HOLD / APPROVE WITH FIXES / APPROVE",
    "unknown | Not checked",
]


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


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check a mounted Agent Harness Kernel project.")
    parser.add_argument("--root", default=".", help="Target project root to check.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat placeholders in active harness docs as hard blockers.",
    )
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    blockers: list[str] = []
    warnings: list[str] = []

    for rel in REQUIRED_FILES:
        if not (root / rel).exists():
            blockers.append(f"missing required file: {rel}")

    root_agents = root / "AGENTS.md"
    if root_agents.exists():
        text = read_text(root_agents).lower()
        if "agents/" not in text:
            blockers.append("AGENTS.md does not point agents to the mounted agents/ harness")

    local_ignore = root / "agents" / "local" / ".gitignore"
    if local_ignore.exists():
        ignore_text = read_text(local_ignore)
        if "*" not in ignore_text:
            blockers.append("agents/local/.gitignore does not ignore local memory by default")

    for path in collect_markdown(root):
        text = read_text(path)
        hits = [marker for marker in PLACEHOLDER_MARKERS if marker in text]
        if hits:
            message = f"{relative(path, root)} contains placeholder markers: {', '.join(hits)}"
            if args.strict:
                blockers.append(message)
            else:
                warnings.append(message)

    reviews_root = root / "agents" / "reviews"
    if reviews_root.exists():
        dated_dirs = [
            item
            for item in reviews_root.iterdir()
            if item.is_dir() and item.name.isdigit() and len(item.name) == 8
        ]
        for dated in dated_dirs:
            review_files = list(dated.glob("*.md"))
            if not review_files:
                warnings.append(f"{relative(dated, root)} has no review markdown files")
            for review in review_files:
                text = read_text(review)
                if "TBD" in text or "HOLD / APPROVE WITH FIXES / APPROVE" in text:
                    blockers.append(f"{relative(review, root)} looks like an unfilled dated review")
    else:
        warnings.append("agents/reviews/ does not exist")

    print("Agent Harness Doctor")
    print(f"root: {root}")
    print(f"hard_blockers: {len(blockers)}")
    for item in blockers:
        print(f"BLOCKER: {item}")
    print(f"warnings: {len(warnings)}")
    for item in warnings:
        print(f"WARNING: {item}")

    if blockers:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
