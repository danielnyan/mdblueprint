---
id: children
title: children
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.GameTree
  declarations:
    - children
uses:
---

# children

## Lean type

```lean
@[simp] def children : GameTree N U → List (GameTree N U) | Leaf _ => [] | Node _ h t => h :: t /-- Children of a `Node` are never empty. -/
```

## Dependencies

- none
