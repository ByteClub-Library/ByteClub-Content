# Spawn Waves

## Overview

Spawn waves structure enemy encounters into distinct phases. Instead of all enemies appearing at once, they arrive in waves — creating rhythm, managing difficulty, and giving players natural breathing room between intense moments.

## Wave structures

### Fixed waves
Pre-scripted enemy counts and compositions per wave. Common in horde modes and survival games.

### Dynamic waves
The Director AI (Left 4 Dead) adjusts wave composition based on player performance, stress levels, and game state.

### Escalating waves
Each wave increases in difficulty — more enemies, tougher types, or faster spawn rates.

### Mixed waves
Combines fixed and dynamic elements. Some waves are scripted for story beats, others adapt to player skill.

## Design considerations

- **Pacing between waves**: Dead air kills tension. Too little downtime overwhelms. 10–30 seconds is typical.
- **Wave telegraphing**: Audio cues, visual indicators, or UI warnings before a wave starts
- **Climax waves**: The final wave should feel like a peak — maximum pressure, special enemies
- **Recovery windows**: Players need moments to heal, reload, and reposition
- **Anti-clustering**: Enemies shouldn't all spawn from the same point — distribute spawn locations

## Spawn mechanics

- **Spawn points**: Fixed locations around the arena
- **Spawn directors**: AI that picks spawn locations based on player position
- **Off-screen spawning**: Classic but can feel unfair if exploited
- **Environmental spawning**: Enemies emerge from specific world features (vents, doors, ground)

## References

- Left 4 Dead 2: The Director dynamically adjusts wave intensity
- Deep Rock Galactic: Each mission type has unique spawn rules
- Vampire Survivors: Enemies spawn continuously with escalating density
- Risk of Rain 2: Difficulty scales with time, not waves