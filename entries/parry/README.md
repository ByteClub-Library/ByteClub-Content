# Parry

## Overview

A parry is a timed defensive action where the player deflects an incoming attack at the moment of impact. Successful parries typically create openings for counter-attacks, deal posture/posture damage, or negate damage entirely. It's one of the highest skill-expression mechanics in action games.

## Core loop

1. Player reads incoming attack
2. Player times a defensive input to match the attack's impact frame
3. Successful parry: damage negated, counter-attack window opened
4. Failed parry: full damage taken, often with额外punishment

## Design dimensions

### Timing window
- **Strict** (Sekiro): ~6 frames (100ms). High skill ceiling, demanding mastery
- **Moderate** (Cuphead): ~10-15 frames. Forgiving enough to learn, tight enough to feel earned
- **Generous** (Dead Cells): ~20+ frames. More about decision-making than frame precision

### Reward structure
- **Posture damage** (Sekiro): Parries build toward breaking the enemy's stance
- **Counter-attack** (Street Fighter): Successful parry opens a free punish
- **Resource generation**: Some systems give meter, health, or ammo on parry
- **Nothing**: The reward IS negating damage — simplest form

### Visual/audio feedback
- **Hitstop freeze**: Brief pause on successful parry (critical for feel)
- **Screen shake**: Subtle shake communicates impact
- **Distinct sound**: A sharp, satisfying audio cue
- **Particle effects**: Sparks, shockwaves, visual flair

### Enemy telegraphing
- **Wind-up animations**: Clear pre-attack animations
- **Color indicators**: Flashing attack indicators (Sekiro's perilous attack kanji)
- **Audio cues**: Distinct sounds before unblockable attacks

## Anti-patterns

- **No telegraphing**: If you can't read the attack, you can't parry it
- **Punishing failure too hard**: One-hit kills for missed parries discourage learning
- **No feedback**: If a parry doesn't feel impactful, players won't engage with it
- **Universal applicability**: Not every attack should be parryable — unblockables add variety

## References

- Sekiro: Deflection system with posture meter, the gold standard for parry design
- Street Fighter 6: Perfect Parry withDrive Impact follow-up
- Dead Cells: Shield parry with timing-based window
- Cuphead: Parry on pink projectiles, core mechanic