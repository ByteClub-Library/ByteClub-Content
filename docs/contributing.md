# Contributing to ByteClub

Want to add an entry to the ByteClub games library? Great! This guide walks you through the entire process.

## Overview

The ByteClub content repository is the source of truth for all indexed game entries. The workflow is:

1. **Create a PR** → **GitHub Actions validates** → **Maintainers review/merge** → **GitHub Actions indexes** → **API serves** → **Website reads**

## How to Contribute

### 1. Fork & Branch

```bash
# 1. Fork this repository on GitHub
# 2. Clone your fork
git clone https://github.com/your-username/games-library.git
cd games-library

# 3. Create a branch
git checkout -b add-new-entry
```

### 2. Copy the Template

```bash
# Copy the entry template into a new directory
# The directory NAME must match the slug in entry.yaml
cp templates/entry.yaml entries/my-new-entry/
cp templates/README.md entries/my-new-entry/README.md
```

### 3. Fill in `entries/my-new-entry/entry.yaml`

Replace the placeholder values:

- `name` - Human-readable entry name
- `slug` - Must exactly match the directory name (`my-new-entry`)
- `type` - One of: `mechanic`, `system`, `level_design`, `game_feel`, `ui_ux`, `ai`
- `categories` - Array of strings (e.g., `[- movement, traversal]`)
- `tags` - Array of arbitrary strings (e.g., `[- mobility, physics]`)
- `games` - Array of game titles this entry relates to
- `description` - Brief description
- `media` - Optional media references
- `contributor` - Your name and GitHub handle

### 4. Fill in `entries/my-new-entry/README.md`

Human-readable content about the entry. Include:

- Overview/description
- How it works
- Design considerations
- Variations (optional)

**Do not duplicate all metadata from entry.yaml** — only add human-readable context.

### 4. Validate Locally (Optional but Recommended)

```bash
python scripts/validate.py
```

This runs the same validation as GitHub Actions.

### 5. Open a Pull Request

- Target: `main` branch
- Title: e.g., "Add: Grappling Hook mechanic"
- Describe what you've added

### 6. What Happens After Merge

1. GitHub Actions `index.yml` detects the changed entries
2. Only the affected entries are synced to the API
3. The API PostgreSQL index is updated
4. The ByteClub website reflects the new entry

### 7. Validation in CI

GitHub Actions runs `validate.yml` on your PR. It will:

- Validate `entry.yaml` against the JSON schema
- Check directory name == slug
- Ensure `README.md` exists
- Detect duplicate slugs
- Detect malformed YAML

If any check fails, the CI will show clear error messages and the PR cannot be merged until fixed.

## Need Help?

Open an issue or discuss on the [ByteClub community forum](https://byteclub.dev).