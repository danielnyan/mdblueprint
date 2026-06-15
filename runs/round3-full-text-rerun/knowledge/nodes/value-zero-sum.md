---
id: value-zero-sum
title: value_zero_sum
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Zermelo
  declarations:
    - value_zero_sum
uses:
  - IsZeroSum
  - strong_induction
  - Arena.Reachable.step
  - CPState.step
  - value_Node_eq_some_child_value
  - IsZeroSum.child_mem
  - Subtree.child_mem
---

# value_zero_sum

## Lean type

```lean
theorem value_zero_sum (g : GameTree (Fin 2) ℚ) (hzs : IsZeroSum g) : (value g) 0 + (value g) 1 = 0
```

## Dependencies

- IsZeroSum
- strong_induction
- Arena.Reachable.step
- CPState.step
- value_Node_eq_some_child_value
- IsZeroSum.child_mem
- Subtree.child_mem
