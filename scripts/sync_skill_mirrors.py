from __future__ import annotations

import argparse
import filecmp
import shutil
from pathlib import Path


CROSSFRAME_SKILLS = [
    "crossframe",
    "crossframe-suite",
    "crossframe-essay",
    "crossframe-critical",
    "crossframe-review",
    "crossframe-dialogue",
    "crossframe-casebook",
    "crossframe-history",
    "crossframe-inquiry",
    "crossframe-max",
    "crossframe-public",
    "crossframe-org",
    "crossframe-teach",
    "crossframe-debate",
    "crossframe-notebook",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def same_tree(left: Path, right: Path) -> bool:
    if not left.exists() or not right.exists():
        return False
    comparison = filecmp.dircmp(left, right)
    if comparison.left_only or comparison.right_only or comparison.diff_files or comparison.funny_files:
        return False
    return all(same_tree(left / subdir, right / subdir) for subdir in comparison.common_dirs)


def sync_skill(src: Path, dst: Path, check_only: bool) -> None:
    require(src.is_dir(), f"missing source skill: {src}")
    if check_only:
        require(same_tree(src, dst), f"mirror drift: {dst}")
        return

    if dst.exists():
        require(dst.is_dir(), f"mirror destination is not a directory: {dst}")
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync CrossFrame skill mirrors from skills/crossframe*.")
    parser.add_argument("--repo", default=".", help="Repository root.")
    parser.add_argument(
        "--mirror",
        action="append",
        default=[],
        help="Mirror skill root. Defaults to .claude/skills when omitted.",
    )
    parser.add_argument("--check", action="store_true", help="Only check for mirror drift.")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    source_root = repo / "skills"
    require(source_root.is_dir(), f"missing skills directory: {source_root}")
    mirrors = [Path(value).resolve() for value in (args.mirror or [repo / ".claude" / "skills"])]

    for mirror_root in mirrors:
        if not args.check:
            mirror_root.mkdir(parents=True, exist_ok=True)
        for skill in CROSSFRAME_SKILLS:
            sync_skill(source_root / skill, mirror_root / skill, args.check)
        print(f"ok: {'checked' if args.check else 'synced'} {mirror_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
