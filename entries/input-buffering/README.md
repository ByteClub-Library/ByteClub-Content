# Input Buffering

## Overview

Input buffering stores player inputs that arrive during an animation or action lock, and executes them as soon as the current action completes. This makes controls feel responsive — the player presses jump during a landing animation, and the character jumps the instant the animation ends, rather than requiring frame-perfect timing.

## How it works

1. Player initiates action (e.g., attack)
2. During the attack animation, player presses jump
3. The jump input is stored in a buffer
4. When the attack animation completes, the buffered jump executes immediately

## Buffer window

The buffer window is how long after pressing a button the input remains "remembered":

- **Short** (1–3 frames / 16–50ms): Nearly imperceptible, requires near-frame-perfect input
- **Medium** (6–10 frames / 100–166ms): The sweet spot for most action games
- **Long** (15+ frames / 250ms+): Very forgiving but can feel like the game is playing itself

## Why it matters

Without input buffering, players must time their next input to the exact frame the current animation ends. This creates a disconnect between intention and execution. With buffering, pressing jump "early" still works — the game just waits for the right moment.

## Design considerations

- **Per-action buffering**: Different actions might have different buffer windows. A jump might have a longer buffer than a dodge.
- **Buffer visualization**: Some games show a subtle indicator when an input is buffered
- **Buffer clearing**: Should inputs expire? If the player presses jump, waits 2 seconds, then the attack ends, should the jump still happen?
- **Negative edge**: Some fighting games use "button release" timing in addition to press timing

## Interaction with coyote time

Input buffering pairs naturally with coyote time:
- **Buffering**: Press jump slightly before landing → jump executes on landing
- **Coyote time**: Press jump slightly after leaving a ledge → jump still works
- Together, they make platforming feel incredibly responsive

## References

- Celeste: Buffer window of ~6 frames, combined with coyote time
- Street Fighter 6: Input buffer for special move cancels
- Hollow Knight: Generous buffering on all actions
- Dead Cells: Buffer window on dodge and attack inputs