# Enemy AI Patrol

## Overview

Patrol behavior is the foundation of enemy AI in stealth and action games. Enemies follow defined paths, creating predictable patterns that players can observe, learn, and exploit. The quality of patrol design directly impacts how satisfying stealth gameplay feels.

## Core components

### Waypoint system
Enemies follow a series of waypoints. The complexity ranges from:
- **Linear**: A → B → A → B (simple guard)
- **Loop**: A → B → C → A (perimeter patrol)
- **Randomized**: Random selection from available waypoints

### Detection states
- **Patrol**: Normal behavior, limited awareness
- **Suspicious**: Heard something, investigating
- **Alert**: Spotted the player, active pursuit
- **Searching**: Lost the player, looking around

### Perception
- **Vision cone**: Angular field of view with range limit
- **Hearing radius**: Detects nearby sounds (footsteps, gunfire)
- **Line of sight**: Blocked by walls and obstacles

## Design considerations

### Patrol readability
Players should be able to learn patrol patterns through observation. If patterns are too random, stealth becomes luck-based. If too predictable, it becomes trivial.

### Patrol variety
Different enemy types should have different patrol behaviors:
- **Stationary guards**: Stand in one spot, look around
- **Patrol guards**: Walk a set route
- **Roaming guards**: Move freely within an area
- **Alerted guards**: Change behavior based on events

### Failure states
What happens when the player is detected?
- **Full alert**: Everyone knows where you are
- **Partial alert**: Localized search, suspicion spreads
- **Grace period**: Brief window to hide before real consequences

## Behavior tree structure

```
Root
├── Is Alerted?
│   ├── Yes → Combat/Chase
│   └── No → Continue
├── Heard Sound?
│   ├── Yes → Investigate
│   └── No → Continue
├── Current Waypoint Reached?
│   ├── Yes → Next Waypoint
│   └── No → Move to Waypoint
└── Idle at Waypoint
    ├── Look Around
    └── Wait Duration
```

## References

- Metal Gear Solid V: Dynamic AI that adapts to player tactics
- Alien: Isolation: Alien AI with unpredictable patrol patterns
- The Last of Us: Guard AI with realistic patrol routes
- Dishonored: readable patrol patterns with readable vision cones