---
id: Subtree-tail-mem
title: Subtree.tail_mem
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.GameTree
  declarations:
    - Subtree.tail_mem
uses:
  - IsPositiveAffineOf.refl
  - Indifferent.refl
  - IVariant.refl
---

# Subtree.tail_mem

## Lean type

```lean
theorem Subtree.tail_mem (m : N) (h : GameTree N U) (t : List (GameTree N U)) {c : GameTree N U} (hmem : c ∈ t) : Subtree c (Node m h t)
```

## Dependencies

- IsPositiveAffineOf.refl
- Indifferent.refl
- IVariant.refl
