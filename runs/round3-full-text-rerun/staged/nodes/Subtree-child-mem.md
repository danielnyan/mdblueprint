---
id: Subtree-child-mem
title: Subtree.child_mem
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.GameTree
  declarations:
    - Subtree.child_mem
uses:
  - IsZeroSum.head
  - Subtree.head
  - IsZeroSum.tail_mem
  - Subtree.tail_mem
---

# Subtree.child_mem

## Lean type

```lean
theorem Subtree.child_mem (m : N) (h : GameTree N U) (t : List (GameTree N U)) {c : GameTree N U} (hmem : c ∈ h :: t) : Subtree c (Node m h t)
```

## Dependencies

- IsZeroSum.head
- Subtree.head
- IsZeroSum.tail_mem
- Subtree.tail_mem
