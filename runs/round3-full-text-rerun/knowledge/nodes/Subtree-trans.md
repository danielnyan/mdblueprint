---
id: Subtree-trans
title: Subtree.trans
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.GameTree
  declarations:
    - Subtree.trans
uses:
  - IsPositiveAffineOf.refl
  - Indifferent.refl
  - IVariant.refl
---

# Subtree.trans

## Lean type

```lean
theorem Subtree.trans {r s g : GameTree N U} (hrs : Subtree r s) (hsg : Subtree s g) : Subtree r g
```

## Dependencies

- IsPositiveAffineOf.refl
- Indifferent.refl
- IVariant.refl
