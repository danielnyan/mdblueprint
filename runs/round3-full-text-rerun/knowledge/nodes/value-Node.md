---
id: value-Node
title: value_Node
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BackwardInduction
  declarations:
    - value_Node
uses:
  - argMaxOn
---

# value_Node

## Lean type

```lean
@[simp] theorem value_Node (m : N) (h : GameTree N U) (t : List (GameTree N U)) : value (Node m h t) = List.argMaxOn (fun v => v m) (value h) (valueList t)
```

## Dependencies

- argMaxOn
