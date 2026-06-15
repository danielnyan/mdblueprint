---
id: value-Leaf
title: value_Leaf
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.BackwardInduction
  declarations:
    - value_Leaf
uses:
---

# value_Leaf

## Lean type

```lean
@[simp] theorem value_Leaf (p : N → U) : value (Leaf p : GameTree N U) = p
```

## Dependencies

- none
