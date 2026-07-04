#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "catalog.json"
FORWARD_TESTS_ROOT = ROOT / "forward-tests"
REQUIRED_SECTIONS = (
    "Skill",
    "Prompt",
    "Expected Artifact Checklist",
    "Pass Conditions",
    "Fail Conditions",
)


def load_catalog_ids() -> tuple[set[str], list[str]]:
    try:
        data: dict[str, Any] = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return set(), ["catalog.json is missing"]
    except json.JSONDecodeError as exc:
        return set(), [f"catalog.json is not valid JSON: {exc}"]

    skills = data.get("skills")
    if not isinstance(skills, list):
        return set(), ["catalog.skills must be a list"]

    ids = {
        skill["id"]
        for skill in skills
        if isinstance(skill, dict) and isinstance(skill.get("id"), str)
    }
    return ids, []


def has_section(raw: str, section: str) -> bool:
    return re.search(rf"^## {re.escape(section)}\s*$", raw, re.MULTILINE) is not None


def validate_forward_test(path: Path, catalog_ids: set[str]) -> list[str]:
    scope = str(path.relative_to(ROOT))
    raw = path.read_text(encoding="utf-8")
    errors: list[str] = []

    if not raw.startswith("# Forward Test: "):
        errors.append(f"{scope} must start with '# Forward Test: '")

    for section in REQUIRED_SECTIONS:
        if not has_section(raw, section):
            errors.append(f"{scope} missing '## {section}' section")

    skill_match = re.search(r"^## Skill\s*\n+`([^`]+)`", raw, re.MULTILINE)
    if not skill_match:
        errors.append(f"{scope} must name the tested skill as a backticked id after '## Skill'")
    else:
        skill_id = skill_match.group(1)
        if skill_id not in catalog_ids:
            errors.append(f"{scope} references unknown skill {skill_id!r}")
        if path.stem != skill_id:
            errors.append(f"{scope} file stem must match skill id {skill_id!r}")

    if re.search(r"\b(TODO|TBD|placeholder)\b", raw, re.IGNORECASE):
        errors.append(f"{scope} contains TODO/TBD/placeholder text")

    return errors


def main() -> int:
    catalog_ids, errors = load_catalog_ids()

    if not FORWARD_TESTS_ROOT.is_dir():
        errors.append("forward-tests/ is missing")
        test_paths: list[Path] = []
    else:
        test_paths = sorted(
            path
            for path in FORWARD_TESTS_ROOT.glob("*.md")
            if path.name != "README.md"
        )

    if not test_paths:
        errors.append("forward-tests/ must contain at least one test markdown file")

    seen: set[str] = set()
    for path in test_paths:
        if path.stem in seen:
            errors.append(f"duplicate forward test for {path.stem!r}")
        seen.add(path.stem)
        errors.extend(validate_forward_test(path, catalog_ids))

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    print(f"forward tests ok: {len(test_paths)} tests")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
