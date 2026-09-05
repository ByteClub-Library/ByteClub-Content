# I-Frames (Invincibility Frames)

## Overview

I-frames are a brief window of invincibility granted to the player after taking damage. During this window, the player cannot be hit again, preventing stun-locking and giving them time to react and reposition.

## How it works

1. Player takes damage
2. I-frame timer starts (typically 0.5–2 seconds depending on the game)
3. During I-frames, the player is immune to all damage
4. Visual feedback indicates the I-frame state (flashing, transparency, glow)
5. When the timer expires, the player can be hit again

## Design considerations

- **Duration**: Too short and the player gets stun-locked. Too long and combat feels trivial. Dark Souls uses ~1 second. Hollow Knight uses ~0.5 seconds.
- **Visual clarity**: The player MUST know when they're invincible. Flashing, color changes, or transparency shifts are standard.
- **Animation sync**: I-frames should align with recovery animations so the player isn't hit during a wind-up.
- **Enemy applicability**: Should enemies also have I-frames? In Dark Souls, yes. In many action games, no.

## Variations

- **Hit-stun immunity**: Only knockback resistance, not full invincibility
- **Directional I-frames**: Invincibility only from certain angles (e.g., behind during a roll)
- **Partial I-frames**: Reduced damage rather than zero damage
- **Charging I-frames**: I-frames only while actively performing an action (rolling, dodging)

## References

- Dark Souls: Roll I-frames vary by equipment weight class
- Hollow Knight: Damage boost with brief invincibility after taking a hit
- Celeste: Death respawn gives I-frames during repositioning
- Dead Cells: Dodge roll I-frames are the primary defensive tool