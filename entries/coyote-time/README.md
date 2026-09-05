# Coyote Time

## Overview

Named after Wile E. Coyote's tendency to hang in the air before realizing he's run off a cliff, coyote time is a brief window (typically 60–150ms) after a player walks off a platform edge during which they can still jump. It makes platforming feel fairer by compensating for imprecise inputs and human reaction time.

## How it works

1. Player walks off a platform edge
2. A coyote time timer starts (e.g., 100ms)
3. Within this window, the player can still press jump and get a normal jump
4. If they don't jump within the window, they fall normally

## Why it matters

Without coyote time, players frequently miss jumps they feel they should have made. The brain processes visual information and sends a jump command, but by the time the character is at the edge, they've already left the platform by a few pixels. Coyote time bridges that gap.

## Design considerations

- **Duration**: Too short and it's unnoticeable. Too long and jumping feels floaty or unpredictable. 80–120ms is the sweet spot for most games.
- **Visual feedback**: Some games show a brief "edge indicator" or subtle animation to communicate the window exists.
- **Interaction with jump buffering**: Coyote time pairs naturally with input buffering — the player presses jump slightly too late (coyote time) or slightly before landing (input buffer).
- **Should it be visible?**: Most games keep it invisible. Making it too obvious can break immersion.

## Platform-specific considerations

- **2D platformers**: Most critical here. Celeste and Super Meat Boy are the gold standard.
- **3D platformers**: Also important but the extra dimension gives more room for error.
- **Action games**: Can apply to ledge-grabbing or edge detection.

## References

- Celeste: 70ms coyote time, widely praised for making precision platforming feel fair
- Super Meat Boy: Generous coyote time combined with instant respawn
- Hollow Knight: Coyote time on ledge jumps
- Ori and the Blind Forest: Generous edge detection across all movement