---
id: IsZeroSum-of-subtree
title: IsZeroSum.of_subtree
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.Zermelo
  declarations:
    - IsZeroSum.of_subtree
uses:
  - IsZeroSum
  - IsPositiveAffineOf.refl
  - Indifferent.refl
  - IVariant.refl
  - IsZeroSum.head
  - Subtree.head
  - IsZeroSum.tail_mem
  - Subtree.tail_mem
---

# IsZeroSum.of_subtree

## Lean type

```lean
theorem IsZeroSum.of_subtree {s g : GameTree (Fin 2) ℚ} (hzs : IsZeroSum g) (hsub : Subtree s g) : IsZeroSum s
```

## Dependencies

- IsZeroSum
- IsPositiveAffineOf.refl
- Indifferent.refl
- IVariant.refl
- IsZeroSum.head
- Subtree.head
- IsZeroSum.tail_mem
- Subtree.tail_mem
