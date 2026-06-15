---
id: centipedePrefix-has-spe-on
title: centipedePrefix_has_spe_on
kind: theorem
status: staged
lean:
  module: EconCSLib.Examples.CentipedeGame
  declarations:
    - centipedePrefix_has_spe_on
uses:
  - Strategy
  - IsSubgamePerfectOn
  - centipedePrefixTree
  - Kuhn_exists_SPE_on
---

# centipedePrefix_has_spe_on

## Lean type

```lean
theorem centipedePrefix_has_spe_on : ∃ σ : GameTree.Strategy (Fin 2) ℤ, GameTree.IsSubgamePerfectOn σ centipedePrefixTree
```

## Dependencies

- Strategy
- IsSubgamePerfectOn
- centipedePrefixTree
- Kuhn_exists_SPE_on
