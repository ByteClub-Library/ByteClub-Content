# Entry Format Reference

Complete reference for `entry.yaml` and `README.md` fields.

## `entry.yaml` Fields

### `name` (required)
- **Type**: string
- **Description**: Human-readable entry name
- **Example**: `Grappling Hook`

### `slug` (required)
- **Type**: string
- **Pattern**: `^[a-z0-9]+(?:-[a-z0-9]+)*$` (lowercase alphanumeric with hyphens)
- **Description**: Unique identifier; **directory name must exactly match this value**
- **Example**: `grappling-hook`
- **Constraint**: `entries/grappling-hook/` directory name must equal `grappling-hook`

### `type` (required)
- **Type**: enum
- **Values**: `mechanic`, `system`, `level_design`, `game_feel`, `ui_ux`, `ai`
- **Description**: Controlled vocabulary entry kind
- **Example**: `mechanic`
- **Note**: Easy to extend — just add new values to the enum

### `categories` (required)
- **Type**: array of strings
- **Description**: User-defined categories; an entry may belong to multiple categories
- **Min items**: 1
- **Example**: `[- movement, traversal]`
- **Note**: These are metadata, not directories. They are free-form strings.

### `tags` (required)
- **Type**: array of strings
- **Description**: Arbitrary tags for discovery
- **Min items**: 1
- **Example**: `[- mobility, physics, momentum]`
- **Note**: Free-form strings; no controlled vocabulary

### `games` (required)
- **Type**: array of strings
- **Description**: Games this entry relates to
- **Example**: `[- Terraria, Bionic Commando]`
- **Note**: Each item is a game title string

### `description` (required)
- **Type**: string, minLength 1
- **Description**: Description of the entry
- **Example**: `A traversal mechanic that allows the player to attach to surfaces and move through the environment.`
- **Format**: YAML multi-line string (`>` or `|`)

### `media` (optional)
- **Type**: array of objects
- **Description**: Media references (images, videos, GIFs, external URLs)
- **Items schema**:
  - `type` (enum): `image`, `video`, `gif`, `external`
  - `url` (string, format): The media URL
  - `source` (string, optional): Source attribution (e.g., `youtube`, `vimeo`)
- **Example**:
  ```yaml
  media:
    - type: video
      url: https://example.com/video
      source: youtube
    - type: image
      url: https://example.com/screenshot.png
  ```

### `contributor` (required)
- **Type**: object
- **Required field**: `name`
- **Properties**:
  - `name` (string, required): Contributor's name
  - `github` (string, optional): GitHub username/link
- **Example**:
  ```yaml
  contributor:
    name: ByteClub
    github: byteclub
  ```

## `README.md` Fields

- **Purpose**: Human-readable content about the entry
- **Content**: Overview, how it works, design considerations, variations
- **Rule**: Do **not** duplicate all metadata from `entry.yaml`. Only add contextual human-readable content.
- **Example structure**:
  ```markdown
  # Grappling Hook
  
  The grappling hook is a traversal mechanic...
  
  ## How it works
  
  ...
  
  ## Design considerations
  
  ...
  
  ## Variations
  
  - Swinging
  - Pull-to-target
  - Reel-in
  ```

## Validation Rules (Used by CI & Local Script)

| Rule | Description |
|------|-------------|
| slug format | Must match `^[a-z0-9]+(?:-[a-z0-9]+)*$` |
| directory name == slug | `os.path.basename(dir)` must equal the slug in entry.yaml |
| type validity | Must be one of: `mechanic`, `system`, `level_design`, `game_feel`, `ui_ux`, `ai` |
| categories is array | Must be a non-empty array of strings |
| tags is array | Must be a non-empty array of strings |
| games is array | Must be an array |
| media structure | If present, each item must have `type` and `url` |
| contributor validity | Must have `name` field |
| README.md exists | File must exist in the entry directory |

## Extending the Schema

To add new fields later:

1. Add the field to `entry.schema.json`
2. Add the field to `templates/entry.yaml`
3. Update `scripts/validate.py`
4. Update `docs/entry-format.md`