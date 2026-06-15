---
id: value₀-Node-eq-some-child
title: value₀_Node_eq_some_child
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Zermelo
  declarations:
    - value₀_Node_eq_some_child
uses:
  - value_Node_eq_some_child_value
---

# value₀_Node_eq_some_child

## Lean type

```lean
theorem value₀_Node_eq_some_child (m : Fin 2) (h : GameTree (Fin 2) ℚ) (t : List (GameTree (Fin 2) ℚ)) : ∃ c ∈ h :: t, value₀ (Node m h t) = value₀ c
```

## Dependencies

- value_Node_eq_some_child_value
