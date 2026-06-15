---
id: outcome-Node
title: outcome_Node
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.GameTreeSPE
  declarations:
    - outcome_Node
uses:
  - Strategy
  - value_Node_eq_some_child_value
---

# outcome_Node

## Lean type

```lean
@[simp] theorem outcome_Node (σ : Strategy N U) (m : N) (h : GameTree N U) (t : List (GameTree N U)) : outcome σ (Node m h t) = outcome σ (σ m h t).val
```

## Dependencies

- Strategy
- value_Node_eq_some_child_value
