---
id: value₀-Node-one-isMin
title: value₀_Node_one_isMin
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Zermelo
  declarations:
    - value₀_Node_one_isMin
uses:
  - IsZeroSum
  - value₀_Node_eq_some_child
  - value₀_Node_one_le_child
---

# value₀_Node_one_isMin

## Lean type

```lean
theorem value₀_Node_one_isMin (h : GameTree (Fin 2) ℚ) (t : List (GameTree (Fin 2) ℚ)) (hzs : IsZeroSum (Node (1 : Fin 2) h t)) : ∃ c ∈ h :: t, value₀ (Node (1 : Fin 2) h t) = value₀ c ∧ ∀ d ∈ h :: t, value₀ c ≤ value₀ d
```

## Dependencies

- IsZeroSum
- value₀_Node_eq_some_child
- value₀_Node_one_le_child
