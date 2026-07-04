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
ALLOWED_TYPES = {"flow", "atomic", "reference", "tool"}
ALLOWED_MATURITY = {"draft", "beta", "stable"}
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
MAX_SKILL_LINES = 500
MAX_REFERENCE_LINES = 200


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


def validate_string_list(obj: dict[str, Any], field: str, scope: str, required: bool) -> list[str]:
    value = obj.get(field)
    if value is None and not required:
        return []
    if not isinstance(value, list) or (required and not value):
        return [f"{scope}.{field} must be a non-empty list"]
    if not all(isinstance(item, str) and item.strip() for item in value):
        return [f"{scope}.{field} must contain only non-empty strings"]
    return []


def parse_frontmatter(skill_md: Path, scope: str) -> tuple[dict[str, str], list[str]]:
    try:
        raw = skill_md.read_text(encoding="utf-8")
    except FileNotFoundError:
        return {}, [f"{scope}.path must contain SKILL.md"]

    match = FRONTMATTER_RE.match(raw)
    if not match:
        return {}, [f"{scope}.SKILL.md must start with YAML frontmatter"]

    values: dict[str, str] = {}
    errors: list[str] = []
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            errors.append(f"{scope}.SKILL.md frontmatter line is invalid: {line!r}")
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key not in {"name", "description", "disable-model-invocation"}:
            errors.append(f"{scope}.SKILL.md frontmatter has unsupported key {key!r}")
        values[key] = value

    for field in ("name", "description"):
        if not values.get(field):
            errors.append(f"{scope}.SKILL.md frontmatter missing {field!r}")

    return values, errors


def has_heading(raw: str, heading: str) -> bool:
    return re.search(rf"^## {re.escape(heading)}\s*$", raw, re.MULTILINE) is not None


def has_heading_prefix(raw: str, prefix: str) -> bool:
    return re.search(rf"^## {re.escape(prefix)}", raw, re.MULTILINE) is not None


def validate_skill_body(skill_md: Path, skill_type: Any, scope: str) -> list[str]:
    try:
        raw = skill_md.read_text(encoding="utf-8")
    except FileNotFoundError:
        return []

    errors: list[str] = []
    line_count = len(raw.splitlines())
    if line_count > MAX_SKILL_LINES:
        errors.append(
            f"{scope}.SKILL.md must be {MAX_SKILL_LINES} lines or fewer, got {line_count}"
        )

    if skill_type == "flow":
        required = ("Intake", "Completion")
        for heading in required:
            if not has_heading(raw, heading):
                errors.append(f"{scope}.SKILL.md missing '## {heading}' section")
        if not (
            has_heading_prefix(raw, "Route by")
            or has_heading(raw, "Route")
            or has_heading(raw, "Routing")
        ):
            errors.append(f"{scope}.SKILL.md flow skill must include a route section")
    else:
        for heading in ("Inputs", "Workflow", "Completion"):
            if not has_heading(raw, heading):
                errors.append(f"{scope}.SKILL.md missing '## {heading}' section")
        if not any(
            has_heading(raw, heading)
            for heading in ("Validation", "Quality Gates", "Rules")
        ):
            errors.append(
                f"{scope}.SKILL.md must include Validation, Quality Gates, or Rules"
            )

    references_dir = skill_md.parent / "references"
    if references_dir.is_dir():
        for reference in sorted(references_dir.glob("*.md")):
            rel = f"references/{reference.name}"
            if rel not in raw:
                errors.append(f"{scope}.SKILL.md must link to {rel}")
            reference_raw = reference.read_text(encoding="utf-8")
            reference_lines = len(reference_raw.splitlines())
            if reference_lines > MAX_REFERENCE_LINES:
                errors.append(
                    f"{scope}.{rel} must be {MAX_REFERENCE_LINES} lines or fewer, got {reference_lines}"
                )
            if not reference_raw.startswith("# "):
                errors.append(f"{scope}.{rel} must start with an H1 heading")

    return errors


def validate_skill(skill: Any, index: int) -> tuple[list[str], str | None]:
    scope = f"skills[{index}]"
    errors: list[str] = []

    if not isinstance(skill, dict):
        return [f"{scope} must be an object"], None

    for field in ("id", "name", "description", "path"):
        errors.extend(validate_string_field(skill, field, scope))

    skill_id = skill.get("id")
    if isinstance(skill_id, str) and not ID_RE.fullmatch(skill_id):
        errors.append(f"{scope}.id must be kebab-case")

    skill_type = skill.get("type")
    if skill_type not in ALLOWED_TYPES:
        errors.append(f"{scope}.type must be one of {sorted(ALLOWED_TYPES)}")

    maturity = skill.get("maturity")
    if maturity not in ALLOWED_MATURITY:
        errors.append(f"{scope}.maturity must be one of {sorted(ALLOWED_MATURITY)}")

    errors.extend(validate_string_field(skill, "domain", scope))
    errors.extend(validate_string_list(skill, "tags", scope, required=True))
    errors.extend(validate_string_list(skill, "depends_on", scope, required=False))
    errors.extend(validate_string_list(skill, "source_inspiration", scope, required=False))

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

            skill_md = resolved_path / "SKILL.md"
            frontmatter, frontmatter_errors = parse_frontmatter(skill_md, scope)
            errors.extend(frontmatter_errors)
            errors.extend(validate_skill_body(skill_md, skill_type, scope))
            if frontmatter:
                if isinstance(skill_id, str) and frontmatter.get("name") != skill_id:
                    errors.append(
                        f"{scope}.SKILL.md name must match catalog id {skill_id!r}"
                    )
                description = frontmatter.get("description", "")
                if isinstance(skill.get("description"), str) and description != skill["description"]:
                    errors.append(
                        f"{scope}.description must match SKILL.md frontmatter description"
                    )

    return errors, skill_id if isinstance(skill_id, str) else None


def main() -> int:
    catalog, errors = load_catalog()
    if catalog is None:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    for field in ("name", "description", "homepage", "license"):
        errors.extend(validate_string_field(catalog, field, "catalog"))
    errors.extend(validate_string_list(catalog, "compatibility", "catalog", required=True))

    version = catalog.get("version")
    if not isinstance(version, int) or version < 1:
        errors.append("catalog.version must be a positive integer")

    maintainers = catalog.get("maintainers")
    if not isinstance(maintainers, list) or not maintainers:
        errors.append("catalog.maintainers must be a non-empty list")
    elif not all(isinstance(item, str) and item.strip() for item in maintainers):
        errors.append("catalog.maintainers must contain only non-empty strings")

    errors.extend(validate_string_list(catalog, "contributors", "catalog", required=False))

    skills = catalog.get("skills")
    if not isinstance(skills, list):
        errors.append("catalog.skills must be a list")
        skills = []

    seen_ids: set[str] = set()
    dependencies: list[tuple[str, str]] = []
    for index, skill in enumerate(skills):
        skill_errors, skill_id = validate_skill(skill, index)
        errors.extend(skill_errors)
        if isinstance(skill, dict) and isinstance(skill.get("id"), str):
            skill_id = skill["id"]
            if skill_id in seen_ids:
                errors.append(f"skills[{index}].id duplicates {skill_id!r}")
            seen_ids.add(skill_id)
            for dependency in skill.get("depends_on", []):
                if isinstance(dependency, str):
                    dependencies.append((skill_id, dependency))

    for skill_id, dependency in dependencies:
        if dependency not in seen_ids:
            errors.append(f"{skill_id!r} depends on unknown skill {dependency!r}")

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    print(f"catalog ok: {len(skills)} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
