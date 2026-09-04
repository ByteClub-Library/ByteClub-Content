# ByteClub Content Repository

Documentation for contributors who want to browse, understand, and add entries to the ByteClub games library.

## Documentation Overview

- [Repository Structure](/docs/repository-structure.md) — How the repo is organized
- [Entry Format](/docs/entry-format.md) — How to write an entry
- [Contributing](/docs/contributing.md) — How to get your entry merged
- [Schema](/schema/entry.schema.json) — JSON validation schema

## Quick Start

1. Fork this repository
2. Create a branch from `main`
3. Copy an entry from `templates/entry.yaml` to `entries/<slug>/`
4. Fill in `entry.yaml` and `README.md`
5. Run `python scripts/validate.py` locally (optional)
6. Open a Pull Request
7. GitHub Actions will validate your contribution automatically

See the [ contributing guide](/docs/contributing.md) for details.