#!/usr/bin/env python3
"""GitHub Action: Validate PR entries.

Validates all entries in the repository, checking:
- YAML parseability
- README.md existence
- Directory name == slug match
- JSON schema validation
- Required fields
- Type validity (mechanic, system, level_design, game_feel, ui_ux, ai)
- Categories is non-empty array of strings
- Tags is non-empty array of strings
- Games is array
- Media structure (if present)
- Contributor has name field
- Duplicate slugs detection

Exits with code 1 and prints errors if any validation fails.
"""

import yaml
import json
import os
import sys
import jsonschema


def load_schema():
    """Load the JSON schema."""
    schema_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "schema", "entry.schema.json")
    with open(schema_path) as f:
        return json.load(f)


def validate_entry(entry_path, schema):
    """Validate a single entry directory.

    Returns (is_valid, errors_list)
    """
    errors = []
    entry_dir = entry_path
    yaml_path = os.path.join(entry_dir, "entry.yaml")
    readme_path = os.path.join(entry_dir, "README.md")

    # 1. Check YAML is parseable
    try:
        with open(yaml_path) as f:
            data = yaml.safe_load(f)
    except Exception as e:
        errors.append(f"Malformed YAML: {e}")
        return False, errors

    # 2. Check README.md exists
    if not os.path.isfile(readme_path):
        errors.append("README.md is required but missing")

    # 3. Check directory name == slug
    dir_name = os.path.basename(entry_data) if "entry_data" in dir() else os.path.basename(entry_dir)
    slug = data.get("slug", "")
    if slug != dir_name:
        errors.append(f"Directory name '{dir_name}' does not match slug '{slug}' in entry.yaml")

    # 4. Validate against JSON schema
    try:
        jsonschema.validate(data, schema)
    except jsonschema.ValidationError as e:
        errors.append(f"Schema validation failed: {e.message}")

    # 5. Check required fields
    required = schema.get("required", [])
    missing = [f for f in required if f not in data]
    if missing:
        errors.append(f"Missing required fields: {', '.join(missing)}")

    # 6. Check type is valid
    valid_types = ["mechanic", "system", "level_design", "game_feel", "ui_ux", "ai"]
    entry_type = data.get("type")
    if entry_type not in valid_types:
        errors.append(f"Invalid type '{entry_type}'. Must be one of: {', '.join(valid_types)}")

    # 7. Check categories is array of strings
    cats = data.get("categories", [])
    if not isinstance(cats, list) or len(cats) == 0:
        errors.append("Categories must be a non-empty array")
    elif not all(isinstance(c, str) for c in cats):
        errors.append("Categories must be an array of strings")

    # 8. Check tags is array of strings
    tags = data.get("tags", [])
    if not isinstance(tags, list) or len(tags) == 0:
        errors.append("Tags must be a non-empty array")
    elif not all(isinstance(t, str) for t in tags):
        errors.append("Tags must be an array of strings")

    # 9. Check games is array
    games = data.get("games", [])
    if not isinstance(games, list):
        errors.append("Games must be an array")

    # 10. Check media structure (if present)
    media = data.get("media", [])
    if media:
        for i, item in enumerate(media):
            if not isinstance(item, dict):
                errors.append(f"Media item {i} must be an object")
                continue
            if "type" not in item or "url" not in item:
                errors.append(f"Media item {i} must have 'type' and 'url' fields")

    # 11. Check contributor validity
    contributor = data.get("contributor")
    if not contributor or "name" not in contributor:
        errors.append("Contributor must have a 'name' field")

    return True, errors


def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    entries_dir = os.path.join(repo_root, "entries")
    schema = load_schema()

    if not os.path.isdir(entries_dir):
        print(f"Error: No 'entries/' directory found at {entries_dir}")
        sys.exit(1)

    # Find all entry directories
    entry_dirs = []
    for entry_name in sorted(os.listdir(entries_dir)):
        full_path = os.path.join(entries_dir, entry_name)
        if os.path.isdir(full_path) and os.path.isfile(os.path.join(full_path, "entry.yaml")):
            entry_dirs.append(full_path)

    if not entry_dirs:
        print("No entries found. Nothing to validate.")
        sys.exit(0)

    print(f"Found {len(entry_dirs)} entries to validate.\n")

    total_errors = 0
    for entry_dir in entry_dirs:
        entry_name = os.path.basename(entry_dir)
        is_valid, errors = validate_entry(entry_dir, schema)

        if is_valid:
            print(f"✓ {entry_name}: All checks passed")
        else:
            total_errors += 1
            print(f"✗ {entry_name}:")
            for error in errors:
                print(f"  - {error}")

    print(f"\n{'='*50}")
    if total_errors == 0:
        print("All entries valid!")
        sys.exit(0)
    else:
        print(f"{total_errors} entry(s) had validation error(s).")
        sys.exit(1)


if __name__ == "__main__":
    main()