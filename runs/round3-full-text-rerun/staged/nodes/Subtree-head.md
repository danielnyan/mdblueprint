---
id: Subtree-head
title: Subtree.head
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.GameTree
  declarations:
    - Subtree.head
uses:
  - IsPositiveAffineOf.refl
  - Indifferent.refl
  - IVariant.refl
---

# Subtree.head

## Lean type

```lean
theorem Subtree.head (m : N) (h : GameTree N U) (t : List (GameTree N U)) : Subtree h (Node m h t)
```

## Dependencies

- IsPositiveAffineOf.refl
- Indifferent.refl
- IVariant.refl
