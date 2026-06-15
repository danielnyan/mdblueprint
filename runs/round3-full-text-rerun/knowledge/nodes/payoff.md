---
id: payoff
title: payoff
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CentipedeGame
  declarations:
    - payoff
uses:
  - IsCompletelyMixedProfile.player
  - IsCompletelyMixed.player
  - Player
---

# payoff

## Lean type

```lean
def payoff : PrefixState → Fin 2 → ℤ | stop0, i => if i = 0 then 1 else 0 | stop1, i => if i = 0 then 0 else 3 | continue1, i => if i = 0 then 3 else 2 | root, _ => 0 | afterContinue, _ => 0 end PrefixState /-- Arena-style presentation of the two-decision Centipede prefix. -/
```

## Dependencies

- IsCompletelyMixedProfile.player
- IsCompletelyMixed.player
- Player
