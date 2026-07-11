from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def default_skill_root(script_path: Path | None = None) -> Path:
    path = (script_path or Path(__file__)).resolve()
    candidate = path.parent.parent
    if (candidate / "SKILL.md").is_file():
        return candidate
    return candidate / "skills" / "crossframe-max"


def load_schema(skill_root: Path | None = None) -> dict[str, Any]:
    root = (skill_root or default_skill_root()).resolve()
    return json.loads((root / "schemas" / "max-run-contract.schema.json").read_text(encoding="utf-8"))


def validate_schema_instance(instance: object, schema: dict[str, Any], path: str = "$") -> list[str]:
    """Evaluate the exact schema subset used by max-run-contract without third-party imports."""
    errors: list[str] = []

    def matches_type(value: object, expected: str) -> bool:
        return {
            "object": isinstance(value, dict),
            "array": isinstance(value, list),
            "string": isinstance(value, str),
            "boolean": isinstance(value, bool),
            "null": value is None,
            "integer": isinstance(value, int) and not isinstance(value, bool),
            "number": isinstance(value, (int, float)) and not isinstance(value, bool),
        }[expected]

    expected_type = schema.get("type")
    if expected_type is not None:
        accepted = [expected_type] if isinstance(expected_type, str) else expected_type
        if not any(matches_type(instance, item) for item in accepted):
            return [f"{path}: expected type {accepted}"]
    if "const" in schema and instance != schema["const"]:
        errors.append(f"{path}: expected const {schema['const']!r}")
    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{path}: value is not in enum")

    if isinstance(instance, dict):
        properties = schema.get("properties", {})
        for field in schema.get("required", []):
            if field not in instance:
                errors.append(f"{path}: missing {field}")
        if schema.get("additionalProperties") is False:
            for field in sorted(set(instance) - set(properties)):
                errors.append(f"{path}.{field}: additional property is forbidden")
        for field, child_schema in properties.items():
            if field in instance:
                errors.extend(validate_schema_instance(instance[field], child_schema, f"{path}.{field}"))

    if isinstance(instance, str) and len(instance) < schema.get("minLength", 0):
        errors.append(f"{path}: shorter than minLength")
    if isinstance(instance, list):
        if len(instance) < schema.get("minItems", 0):
            errors.append(f"{path}: fewer than minItems")
        if "maxItems" in schema and len(instance) > schema["maxItems"]:
            errors.append(f"{path}: more than maxItems")
        if schema.get("uniqueItems"):
            normalized = [json.dumps(item, ensure_ascii=False, sort_keys=True) for item in instance]
            if len(normalized) != len(set(normalized)):
                errors.append(f"{path}: items must be unique")
        if "items" in schema:
            for index, item in enumerate(instance):
                errors.extend(validate_schema_instance(item, schema["items"], f"{path}[{index}]"))

    for child_schema in schema.get("allOf", []):
        errors.extend(validate_schema_instance(instance, child_schema, path))
    if "anyOf" in schema and not any(
        not validate_schema_instance(instance, child_schema, path)
        for child_schema in schema["anyOf"]
    ):
        errors.append(f"{path}: no anyOf branch matched")
    if "if" in schema:
        branch = "then" if not validate_schema_instance(instance, schema["if"], path) else "else"
        if branch in schema:
            errors.extend(validate_schema_instance(instance, schema[branch], path))
    return errors


def validate_run_contract(data: object, skill_root: Path | None = None) -> list[str]:
    schema = load_schema(skill_root)
    return [
        f"max-run-contract.json {error}"
        for error in validate_schema_instance(data, schema)
    ]
