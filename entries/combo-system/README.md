# Combo System

## Overview

A combo system chains individual attacks into fluid sequences. Each successive hit in the chain can deal escalating damage, earn style points, or unlock finisher moves. The system rewards timing, variety, and mastery.

## Core mechanics

- **Combo counter**: Tracks the number of consecutive hits
- **Combo timer**: A window during which the next input must be entered to continue the chain
- **Damage scaling**: Later hits in the chain may deal reduced or increased damage
- **Style ranking**: Some systems (DMC, Bayonetta) reward variety and punish repetition

## Design dimensions

### Input timing
- **Fixed windows**: Each button press must occur within a specific frame window
- **Generous windows**: Forgiving timing for accessibility
- **Rhythm-based**: Tied to music or beat (Hi-Fi Rush, Metal: Hellsinger)

### Combo structure
- **Linear**: Hit 1 → Hit 2 → Hit 3 (predictable sequence)
- **Branching**: Hit 1 → Hit 2A or Hit 2B depending on direction/input
- **Stance-based**: Different combos from different player states
- **Weapon-dependent**: Combos change based on equipped weapon

### Reward structure
- **Damage scaling**: Later hits do more damage
- **Style meter**: DMC's style rank (D → SSS) rewards variety
- **Resource generation**: Hades gives combo-dependent rewards
- **Finishers**: Unlock a powerful final move at combo threshold

## Anti-patterns

- **Button mashing**: If any sequence works, there's no skill expression
- **Punishing the player**: Combos that are too hard to extend feel frustrating
- **No visual feedback**: Players need to see the combo counter and feel each hit
- **Infinite loops**: Combos that never end trivialize combat

## References

- Devil May Cry 5: Style system with weapon-switching combos
- Bayonetta: Wicked Weaves at combo end, torture attacks
- Street Fighter 6: Drive system with cancel windows
- Hades: Combo-dependent boon interactions