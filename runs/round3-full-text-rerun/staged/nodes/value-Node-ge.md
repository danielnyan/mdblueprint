---
id: value-Node-ge
title: value_Node_ge
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BackwardInduction
  declarations:
    - value_Node_ge
uses:
  - value_Node
  - valueList_eq_map
  - argMaxOn_ge
---

# value_Node_ge

## Lean type

```lean
theorem value_Node_ge (m : N) (h : GameTree N U) (t : List (GameTree N U)) (c : GameTree N U) (hmem : c ∈ h :: t) : (value c) m ≤ (value (Node m h t)) m
```

## Dependencies

- value_Node
- valueList_eq_map
- argMaxOn_ge
