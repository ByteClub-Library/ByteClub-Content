# Repository Structure

This document explains the ByteClub content repository directory structure and the indexing pipeline.

## Top-Level Layout

```
Content-repository/
├── entries/              # Entry directories (source of truth)
│   └── <slug>/
│       ├── entry.yaml
│       └── README.md
│
├── templates/            # Entry templates for contributors
│   └── entry.yaml
│
├── schema/               # JSON schemas for validation
│   └── entry.schema.json
│
├── docs/                 # Contribution documentation
│   ├── README.md
│   ├── contributing.md
│   ├── entry-format.md
│   └── repository-structure.md
│
├── .github/
│   └── workflows/
│       ├── validate.yml    # PR validation
│       └── index.yml       # Incremental indexing
│
├── README.md             # Root README (links to docs)
└── LICENSE
```

## Why Entries Are Self-Contained Directories

Each entry is a directory `entries/<slug>/` because:

- The directory name **must exactly match** the `slug` field in `entry.yaml`
- This provides an implicit, enforceable uniqueness constraint
- It makes listing entries trivial: `os.listdir("entries/")` gives you every slug
- It allows the GitHub Actions workflow to detect changes by comparing directory listings between commits
- It keeps all metadata (`entry.yaml`) and content (`README.md`) co-located

## Categories: Metadata, Not Directories

- Categories are **user-defined arrays of strings** stored in `entry.yaml`
- They are **not** separate directories under the entry
- This keeps the structure flat and simple
- The indexing pipeline reads categories from the YAML, not from the filesystem
- Categories are free-form — contributors can add any string

## Indexing Pipeline (High Level)

1. **Contributor creates PR** with new/modified `entries/<slug>/` directory
2. **`validate.yml` GitHub Actions** validates the entry on the PR
3. **PR merged to main** → **`index.yml` GitHub Actions** runs
4. **`index.yml`** compares changed files between commits
5. **Only affected entries** are processed (not the whole repo)
6. **Each affected entry** is upserted to the API via `POST /internal/sync`
7. **PostgreSQL** is updated with the indexed data
8. **ByteClub website** reads from the API

## Root README.md

The root `README.md` is concise and links to the documentation in `docs/`. It should not duplicate detailed contribution instructions.

## Adding a New Entry

```bash
# 1. Copy template
cp templates/entry.yaml entries/my-new-entry/
cp templates/README.md entries/my-new-entry/README.md

# 2. Fill in entries/my-new-entry/entry.yaml
#    Ensure the slug matches the directory name

# 3. Fill in entries/my-new-entry/README.md

# 4. Validate locally
python scripts/validate.py

# 5. Commit and open PR
git add entries/my-new-entry/
git commit -m "Add: My new entry"
git push origin HEAD

# 6. Wait for GitHub Actions validation
# 7. Maintainers review and merge

# 8. After merge, GitHub Actions indexes the entry automatically
```