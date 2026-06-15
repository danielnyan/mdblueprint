---
id: value₀-Node-zero-ge-child
title: value₀_Node_zero_ge_child
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Zermelo
  declarations:
    - value₀_Node_zero_ge_child
uses:
  - value_Node_ge
---

# value₀_Node_zero_ge_child

## Lean type

```lean
theorem value₀_Node_zero_ge_child (h : GameTree (Fin 2) ℚ) (t : List (GameTree (Fin 2) ℚ)) (c : GameTree (Fin 2) ℚ) (hmem : c ∈ h :: t) : value₀ c ≤ value₀ (Node (0 : Fin 2) h t)
```

## Dependencies

- value_Node_ge
