#!/usr/bin/env python3
"""GitHub Action: Incremental Indexing.

Determines changed entries between the previous commit and HEAD,
then upserts/deletes them via the API's /internal/sync endpoint.

Uses:
- BYTECLUB_SYNC_TOKEN secret for Authorization: Bearer header
- API_URL secret for the API endpoint
- GitHub context for commit SHA and changed files
"""

import os
import sys
import json
import subprocess

# ── Helpers ──────────────────────────────────────────────────────────────
def run(cmd, **kwargs):
    """Run a shell command and return CompletedProcess."""
    return subprocess.run(cmd, capture_output=True, text=True, **kwargs)


def get_changed_files():
    """Get list of files changed between HEAD and its parent."""
    # If GITHUB_BASE_SHA is set (from repository_dispatch or manual), use it;
    # otherwise compare HEAD~1..HEAD.
    base = os.getenv("GITHUB_BASE_SHA") or "HEAD~1"
    result = run(["git", "diff", "--name-only", f"{base}..HEAD"])
    if result.returncode != 0:
        return []
    return [f for f in result.stdout.strip().splitlines() if f]


def get_deleted_entries(previous_files):
    """Determine which entry directories were deleted."""
    current_dirs = set()
    for root, dirs, files in os.walk("entries"):
        for d in dirs:
            current_dirs.add(d)

    previous_dirs = set()
    for f in previous_files:
        if f.startswith("entries/") and f.endswith("/entry.yaml"):
            previous_dirs.add(f.replace("entries/", "").replace("/entry.yaml", ""))

    return previous_dirs - current_dirs


def parse_entry_yaml(slug):
    """Read an entry's entry.yaml and return its fields."""
    yaml_path = f"entries/{slug}/entry.yaml"
    if not os.path.isfile(yaml_path):
        return None
    import yaml
    with open(yaml_path) as f:
        return yaml.safe_load(f)


# ── Main ─────────────────────────────────────────────────────────────────
def main():
    # ── Dependency check ─────────────────────────────────────────────────
    if not os.path.isdir("entries"):
        print("::error:: No 'entries/' directory found. Are we in the repo root?")
        sys.exit(1)

    # ── Get changed files ────────────────────────────────────────────────
    previous_files = get_changed_files()

    # ── Determine deleted entries ────────────────────────────────────────
    deleted_entries = get_deleted_entries(previous_files)

    # ── Determine added / modified entries ───────────────────────────────
    added_modified = {}
    for f in previous_files:
        if f.startswith("entries/") and f.endswith("/entry.yaml"):
            slug = f.replace("entries/", "").replace("/entry.yaml", "")
            # Check if the directory still exists
            if os.path.isdir(f"entries/{slug}"):
                added_modified[slug] = "modified"
            else:
                added_modified[slug] = "deleted"  # yaml file removed but dir might remain

    # Also check for brand-new entry directories not in the diff yet
    # (e.g., new directories created but yaml not tracked yet — unlikely but handle)
    current_dirs = set()
    for root, dirs, files in os.walk("entries"):
        for d in dirs:
            current_dirs.add(d)

    for d in current_dirs:
        if d not in added_modified:
            # New entry — check if its yaml is tracked
            yaml_path = f"entries/{d}/entry.yaml"
            if os.path.isfile(yaml_path):
                # Check if it's untracked in git
                result = run(["git", "ls-files", yaml_path])
                if not result.stdout.strip():  # untracked
                    added_modified[d] = "new"

    # ── Build sync payload ───────────────────────────────────────────────
    payload = {
        "commit": os.getenv("GITHUB_SHA", "unknown"),
        "changes": []
    }

    # ── Process additions / modifications ────────────────────────────────
    for slug in sorted(added_modified.keys()):
        if added_modified[slug] in ("new", "modified"):
            data = parse_entry_yaml(slug)
            if data is None:
                print(f"::warning:: Could not read entry.yaml for '{slug}'; skipping.")
                continue

            entry = {
                "action": "upsert",
                "entry": {
                    "slug": slug,
                    "name": data.get("name", ""),
                    "type": data.get("type", ""),
                    "categories": data.get("categories", []),
                    "tags": data.get("tags", []),
                    "games": data.get("games", []),
                    "description": data.get("description", ""),
                    "media": data.get("media", []),
                    "contributor": data.get("contributor", {}),
                },
            }
            payload["changes"].append(entry)

    # ── Process deletions ────────────────────────────────────────────────
    for slug in sorted(deleted_entries):
        payload["changes"].append({
            "action": "delete",
            "slug": slug,
        })

    # ── Write payload and sync ───────────────────────────────────────────
    payload_path = "/tmp/sync_payload.json"
    with open(payload_path, "w") as f:
        json.dump(payload, f, indent=2)

    # Get secrets from environment
    auth_token = os.getenv("BYTECLUB_SYNC_TOKEN", "")
    api_url = os.getenv("API_URL", "https://api.byteclub.dev/internal/sync")

    if not auth_token:
        print("::error:: Missing BYTECLUB_SYNC_TOKEN secret.")
        sys.exit(1)

    if not payload["changes"]:
        print("::notice:: No entries to index.")
        sys.exit(0)

    # Build curl command
    cmd = ["curl", "-s", "-X", "POST"]
    cmd.append(f"-H Authorization: Bearer {auth_token}")
    cmd.append("-H Content-Type: application/json")
    cmd.append(f"-d @{payload_path}")
    cmd.append(api_url)

    result = run(cmd)
    output = result.stdout.strip()
    stderr = result.stderr.strip()

    if result.returncode != 0:
        print(f"::error:: API request failed (exit {result.returncode})")
        if stderr:
            print(f"Stderr: {stderr}")
        sys.exit(1)

    # Basic success check
    if "error" in output.lower():
        print(f"::error:: API returned an error: {output}")
        sys.exit(1)

    print(f"Indexing complete. {len(payload['changes'])} entries synced.")
    # Set env vars for the commenting step
    os.environ["GITHUB_CHANGED_TOTAL"] = str(len(payload["changes"]))
    added_count = sum(1 for c in payload["changes"] if c["action"] == "upsert")
    os.environ["GITHUB_CHANGED_ADDED"] = str(added_count)
    os.environ["GITHUB_CHANGED_MODIFIED"] = str(len(payload["changes"]) - added_count)
    # Count deletions separately; we'll just use total - added for the deleted count
    os.environ["GITHUB_CHANGED_DELETED"] = str(len(payload["changes"]) - added_count)


if __name__ == "__main__":
    main()