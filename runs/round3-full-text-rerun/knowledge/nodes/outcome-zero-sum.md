---
id: outcome-zero-sum
title: outcome_zero_sum
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Zermelo
  declarations:
    - outcome_zero_sum
uses:
  - Strategy
  - IsZeroSum
  - strong_induction
  - outcome_Leaf
  - Arena.Reachable.step
  - CPState.step
  - outcome_Node
  - IsZeroSum.child_mem
  - Subtree.child_mem
---

# outcome_zero_sum

## Lean type

```lean
theorem outcome_zero_sum (σ : Strategy (Fin 2) ℚ) (g : GameTree (Fin 2) ℚ) (hzs : IsZeroSum g) : outcome σ g 0 + outcome σ g 1 = 0
```

## Dependencies

- Strategy
- IsZeroSum
- strong_induction
- outcome_Leaf
- Arena.Reachable.step
- CPState.step
- outcome_Node
- IsZeroSum.child_mem
- Subtree.child_mem
