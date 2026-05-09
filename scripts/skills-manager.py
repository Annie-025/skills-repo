#!/usr/bin/env python3
"""Manage skills-inventory.json with no third-party dependencies."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

REPO_ROOT = Path(__file__).resolve().parents[1]
INVENTORY_PATH = REPO_ROOT / "skills-inventory.json"
REQUIRED_FIELDS = [
    "name", "description", "category", "path", "enabled", "priority",
    "use_cases", "invocation_examples", "dependencies", "needs_network",
    "blocking_steps", "conflicts", "last_updated",
]


def marker(kind: str, message: str) -> None:
    print(f"[{kind}] {message}")


def today() -> str:
    return date.today().isoformat()


def is_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https", "git", "ssh"} or value.startswith("git@")


def load_inventory() -> dict:
    if not INVENTORY_PATH.exists():
        raise FileNotFoundError(f"{INVENTORY_PATH} does not exist")
    return json.loads(INVENTORY_PATH.read_text(encoding="utf-8"))


def save_inventory(data: dict) -> None:
    data["last_updated"] = today()
    INVENTORY_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def get_skills(data: dict) -> list[dict]:
    skills = data.get("skills")
    if not isinstance(skills, list):
        raise ValueError("skills-inventory.json must contain a top-level 'skills' list")
    return skills


def find_skill(data: dict, name: str) -> dict | None:
    return next((skill for skill in get_skills(data) if skill.get("name") == name), None)


def cmd_list(_: argparse.Namespace) -> int:
    data = load_inventory()
    print(f"{'name':32} {'category':30} {'enabled':8} {'priority':8} {'network':8}")
    print("-" * 94)
    for skill in sorted(get_skills(data), key=lambda item: (item.get("category", ""), item.get("name", ""))):
        print(
            f"{skill.get('name', ''):32} {skill.get('category', ''):30} "
            f"{str(skill.get('enabled', False)):8} {str(skill.get('priority', '')):8} "
            f"{str(skill.get('needs_network', False)):8}"
        )
    return 0


def cmd_add(args: argparse.Namespace) -> int:
    data = load_inventory()
    if find_skill(data, args.name):
        marker("WARN", f"{args.name} already exists; not adding a duplicate.")
        return 0
    get_skills(data).append({
        "name": args.name,
        "description": "",
        "category": "custom",
        "path": args.path_or_url,
        "source": args.path_or_url,
        "enabled": True,
        "priority": 50,
        "use_cases": [],
        "invocation_examples": [],
        "dependencies": [],
        "needs_network": False,
        "blocking_steps": [],
        "conflicts": [],
        "last_updated": today(),
    })
    save_inventory(data)
    marker("OK", f"Added {args.name}. Please edit skills-inventory.json to complete metadata.")
    return 0


def cmd_remove(args: argparse.Namespace) -> int:
    data = load_inventory()
    skills = get_skills(data)
    remaining = [skill for skill in skills if skill.get("name") != args.name]
    if len(remaining) == len(skills):
        marker("WARN", f"{args.name} was not found.")
        return 0
    data["skills"] = remaining
    save_inventory(data)
    marker("OK", f"Removed {args.name} from inventory. Actual files were not deleted.")
    return 0


def set_enabled(name: str, enabled: bool) -> int:
    data = load_inventory()
    skill = find_skill(data, name)
    if not skill:
        marker("ERROR", f"{name} was not found.")
        return 1
    skill["enabled"] = enabled
    skill["last_updated"] = today()
    save_inventory(data)
    marker("OK", f"{name} enabled={enabled}.")
    return 0


def cmd_update(args: argparse.Namespace) -> int:
    data = load_inventory()
    targets = get_skills(data) if args.target == "all" else [find_skill(data, args.target)]
    if any(skill is None for skill in targets):
        marker("ERROR", f"{args.target} was not found.")
        return 1
    for skill in targets:
        skill["last_updated"] = today()
    save_inventory(data)
    marker("OK", f"Updated last_updated for {args.target}.")
    return 0


def cmd_doctor(_: argparse.Namespace) -> int:
    if not INVENTORY_PATH.exists():
        marker("ERROR", "skills-inventory.json does not exist.")
        return 1
    marker("OK", "skills-inventory.json exists.")
    try:
        data = load_inventory()
    except Exception as exc:
        marker("ERROR", f"JSON is invalid: {exc}")
        return 1
    marker("OK", "JSON is valid.")
    skills = get_skills(data)
    marker("OK", "Top-level skills list exists.")
    enabled_names = {skill.get("name") for skill in skills if skill.get("enabled") is True}
    seen = set()
    exit_code = 0
    for skill in skills:
        name = str(skill.get("name", "<unnamed>"))
        missing = [field for field in REQUIRED_FIELDS if field not in skill]
        if missing:
            marker("ERROR", f"{name} is missing required fields: {', '.join(missing)}")
            exit_code = 1
        if name in seen:
            marker("ERROR", f"Duplicate skill name: {name}")
            exit_code = 1
        seen.add(name)
        path_value = str(skill.get("path", ""))
        if not path_value:
            marker("ERROR", f"{name} has an empty path.")
            exit_code = 1
        elif is_url(path_value):
            marker("OK", f"{name} path is URL; local path check skipped.")
        elif Path(path_value).exists():
            marker("OK", f"{name} path exists.")
        else:
            marker("WARN", f"{name} path does not exist locally: {path_value}")
        if skill.get("enabled") is True and skill.get("blocking_steps"):
            marker("WARN", f"{name} is enabled but has blocking_steps: {skill.get('blocking_steps')}")
        for conflict in skill.get("conflicts", []) or []:
            if conflict in enabled_names:
                marker("WARN", f"{name} conflicts with enabled skill {conflict}.")
    if exit_code == 0:
        marker("OK", f"Doctor completed for {len(skills)} skill(s).")
    return exit_code


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Manage skills-inventory.json")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("list").set_defaults(func=cmd_list)
    add = sub.add_parser("add")
    add.add_argument("name")
    add.add_argument("path_or_url")
    add.set_defaults(func=cmd_add)
    remove = sub.add_parser("remove")
    remove.add_argument("name")
    remove.set_defaults(func=cmd_remove)
    enable = sub.add_parser("enable")
    enable.add_argument("name")
    enable.set_defaults(func=lambda args: set_enabled(args.name, True))
    disable = sub.add_parser("disable")
    disable.add_argument("name")
    disable.set_defaults(func=lambda args: set_enabled(args.name, False))
    update = sub.add_parser("update")
    update.add_argument("target", metavar="name|all")
    update.set_defaults(func=cmd_update)
    sub.add_parser("doctor").set_defaults(func=cmd_doctor)
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except Exception as exc:
        marker("ERROR", str(exc))
        return 1


if __name__ == "__main__":
    sys.exit(main())

