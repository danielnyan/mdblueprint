---
id: value₀-Node-one-le-child
title: value₀_Node_one_le_child
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Zermelo
  declarations:
    - value₀_Node_one_le_child
uses:
  - IsZeroSum
  - value_Node_ge
  - value_one_eq_neg_value₀
  - IsZeroSum.child_mem
  - Subtree.child_mem
---

# value₀_Node_one_le_child

## Lean type

```lean
theorem value₀_Node_one_le_child (h : GameTree (Fin 2) ℚ) (t : List (GameTree (Fin 2) ℚ)) (hzs : IsZeroSum (Node (1 : Fin 2) h t)) (c : GameTree (Fin 2) ℚ) (hmem : c ∈ h :: t) : value₀ (Node (1 : Fin 2) h t) ≤ value₀ c
```

## Dependencies

- IsZeroSum
- value_Node_ge
- value_one_eq_neg_value₀
- IsZeroSum.child_mem
- Subtree.child_mem
