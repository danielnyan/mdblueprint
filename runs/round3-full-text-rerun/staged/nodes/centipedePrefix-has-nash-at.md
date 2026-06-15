---
id: centipedePrefix-has-nash-at
title: centipedePrefix_has_nash_at
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CentipedeGame
  declarations:
    - centipedePrefix_has_nash_at
uses:
  - Strategy
  - IsNashAt
  - centipedePrefixTree
  - centipedePrefix_has_spe_on
  - IsSubgamePerfectOn.toNashAt
---

# centipedePrefix_has_nash_at

## Lean type

```lean
theorem centipedePrefix_has_nash_at : ∃ σ : GameTree.Strategy (Fin 2) ℤ, GameTree.IsNashAt σ centipedePrefixTree
```

## Dependencies

- Strategy
- IsNashAt
- centipedePrefixTree
- centipedePrefix_has_spe_on
- IsSubgamePerfectOn.toNashAt
