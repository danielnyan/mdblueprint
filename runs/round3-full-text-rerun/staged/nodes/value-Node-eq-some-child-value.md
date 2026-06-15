---
id: value-Node-eq-some-child-value
title: value_Node_eq_some_child_value
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BackwardInduction
  declarations:
    - value_Node_eq_some_child_value
uses:
  - value_Node
  - argMaxOn_mem
  - mem_valueList_iff
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# value_Node_eq_some_child_value

## Lean type

```lean
theorem value_Node_eq_some_child_value (m : N) (h : GameTree N U) (t : List (GameTree N U)) : ∃ c ∈ h :: t, value (Node m h t) = value c
```

## Dependencies

- value_Node
- argMaxOn_mem
- mem_valueList_iff
- IsPositiveAffineOf.symm
- Indifferent.symm
