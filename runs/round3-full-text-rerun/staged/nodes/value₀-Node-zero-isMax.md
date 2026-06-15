---
id: value₀-Node-zero-isMax
title: value₀_Node_zero_isMax
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Zermelo
  declarations:
    - value₀_Node_zero_isMax
uses:
  - value₀_Node_eq_some_child
  - value₀_Node_zero_ge_child
---

# value₀_Node_zero_isMax

## Lean type

```lean
theorem value₀_Node_zero_isMax (h : GameTree (Fin 2) ℚ) (t : List (GameTree (Fin 2) ℚ)) : ∃ c ∈ h :: t, value₀ (Node (0 : Fin 2) h t) = value₀ c ∧ ∀ d ∈ h :: t, value₀ d ≤ value₀ c
```

## Dependencies

- value₀_Node_eq_some_child
- value₀_Node_zero_ge_child
