#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "catalog.json"
SKILLS_ROOT = ROOT / "skills"
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def load_catalog() -> tuple[dict[str, Any] | None, list[str]]:
    try:
        raw = CATALOG_PATH.read_text(encoding="utf-8")
    except FileNotFoundError:
        return None, ["catalog.json is missing"]

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        return None, [f"catalog.json is not valid JSON: {exc}"]

    if not isinstance(data, dict):
        return None, ["catalog.json must contain a JSON object"]

    return data, []


def validate_string_field(obj: dict[str, Any], field: str, scope: str) -> list[str]:
    value = obj.get(field)
    if not isinstance(value, str) or not value.strip():
        return [f"{scope}.{field} must be a non-empty string"]
    return []


def validate_skill(skill: Any, index: int) -> list[str]:
    scope = f"skills[{index}]"
    errors: list[str] = []

    if not isinstance(skill, dict):
        return [f"{scope} must be an object"]

    for field in ("id", "name", "description", "path"):
        errors.extend(validate_string_field(skill, field, scope))

    skill_id = skill.get("id")
    if isinstance(skill_id, str) and not ID_RE.fullmatch(skill_id):
        errors.append(f"{scope}.id must be kebab-case")

    tags = skill.get("tags")
    if not isinstance(tags, list) or not tags:
        errors.append(f"{scope}.tags must be a non-empty list")
    elif not all(isinstance(tag, str) and tag.strip() for tag in tags):
        errors.append(f"{scope}.tags must contain only non-empty strings")

    path_value = skill.get("path")
    if isinstance(path_value, str):
        skill_path = Path(path_value)
        if skill_path.is_absolute() or ".." in skill_path.parts:
            errors.append(f"{scope}.path must be a safe relative path")
        elif skill_path.parts[:1] != ("skills",):
            errors.append(f"{scope}.path must be under skills/")
        else:
            resolved_path = (ROOT / skill_path).resolve()
            try:
                resolved_path.relative_to(SKILLS_ROOT.resolve())
            except ValueError:
                errors.append(f"{scope}.path must stay inside skills/")

            if not (resolved_path / "SKILL.md").is_file():
                errors.append(f"{scope}.path must contain SKILL.md")

    return errors


def main() -> int:
    catalog, errors = load_catalog()
    if catalog is None:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    for field in ("name", "description", "homepage"):
        errors.extend(validate_string_field(catalog, field, "catalog"))

    version = catalog.get("version")
    if not isinstance(version, int) or version < 1:
        errors.append("catalog.version must be a positive integer")

    maintainers = catalog.get("maintainers")
    if not isinstance(maintainers, list) or not maintainers:
        errors.append("catalog.maintainers must be a non-empty list")
    elif not all(isinstance(item, str) and item.strip() for item in maintainers):
        errors.append("catalog.maintainers must contain only non-empty strings")

    skills = catalog.get("skills")
    if not isinstance(skills, list):
        errors.append("catalog.skills must be a list")
        skills = []

    seen_ids: set[str] = set()
    for index, skill in enumerate(skills):
        errors.extend(validate_skill(skill, index))
        if isinstance(skill, dict) and isinstance(skill.get("id"), str):
            skill_id = skill["id"]
            if skill_id in seen_ids:
                errors.append(f"skills[{index}].id duplicates {skill_id!r}")
            seen_ids.add(skill_id)

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    print(f"catalog ok: {len(skills)} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
