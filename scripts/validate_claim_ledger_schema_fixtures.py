from __future__ import annotations

import argparse
import json
from pathlib import Path

from jsonschema import Draft202012Validator


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate claim ledger schema fixtures.")
    parser.add_argument("--repo", default=".", help="Repository root.")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    schema_path = repo / "skills" / "crossframe" / "schemas" / "claim-ledger.schema.json"
    fixture_dir = repo / "skills" / "crossframe" / "schemas" / "fixtures"
    schema = load_json(schema_path)
    validator = Draft202012Validator(schema)

    fixtures = sorted(fixture_dir.glob("*.json"))
    if not fixtures:
        raise SystemExit(f"missing claim ledger fixtures: {fixture_dir}")

    checked = 0
    for fixture in fixtures:
        instance = load_json(fixture)
        errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.path))
        should_pass = fixture.name.startswith("valid-")
        should_fail = fixture.name.startswith("invalid-")

        if not should_pass and not should_fail:
            raise SystemExit(f"fixture name must start with valid- or invalid-: {fixture.name}")

        if should_pass and errors:
            details = "\n".join(f"- {'/'.join(map(str, error.path))}: {error.message}" for error in errors)
            raise SystemExit(f"valid fixture failed schema validation: {fixture.name}\n{details}")

        if should_fail and not errors:
            raise SystemExit(f"invalid fixture unexpectedly passed schema validation: {fixture.name}")

        checked += 1

    print(f"ok: claim ledger schema fixtures validated: {checked}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
