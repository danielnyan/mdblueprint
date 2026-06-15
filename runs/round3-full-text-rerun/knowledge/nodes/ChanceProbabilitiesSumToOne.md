---
id: ChanceProbabilitiesSumToOne
title: ChanceProbabilitiesSumToOne
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.StochasticGameTree
  declarations:
    - ChanceProbabilitiesSumToOne
uses:
  - Strategy
  - IsCompletelyMixedProfile.player
  - IsCompletelyMixed.player
  - Player
  - expectedPayoff
---

# ChanceProbabilitiesSumToOne

## Lean type

```lean
def ChanceProbabilitiesSumToOne (headProb : ℚ) (tail : List (ℚ × StochasticGameTree N)) : Prop
```

## Dependencies

- Strategy
- IsCompletelyMixedProfile.player
- IsCompletelyMixed.player
- Player
- expectedPayoff
