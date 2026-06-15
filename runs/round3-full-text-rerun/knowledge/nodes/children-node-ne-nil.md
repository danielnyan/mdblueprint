---
id: children-node-ne-nil
title: children_node_ne_nil
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.GameTree
  declarations:
    - children_node_ne_nil
uses:
---

# children_node_ne_nil

## Lean type

```lean
theorem children_node_ne_nil (m : N) (h : GameTree N U) (t : List (GameTree N U)) : children (Node m h t) ≠ []
```

## Dependencies

- none
