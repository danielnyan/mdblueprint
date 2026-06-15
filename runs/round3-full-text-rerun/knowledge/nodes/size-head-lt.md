---
id: size-head-lt
title: size_head_lt
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.GameTree
  declarations:
    - size_head_lt
uses:
---

# size_head_lt

## Lean type

```lean
theorem size_head_lt (m : N) (h : GameTree N U) (t : List (GameTree N U)) : h.size < (Node m h t).size
```

## Dependencies

- none
