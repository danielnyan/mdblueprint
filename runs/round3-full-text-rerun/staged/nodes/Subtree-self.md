---
id: Subtree-self
title: Subtree.self
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.GameTree
  declarations:
    - Subtree.self
uses:
  - IsPositiveAffineOf.refl
  - Indifferent.refl
  - IVariant.refl
---

# Subtree.self

## Lean type

```lean
theorem Subtree.self (g : GameTree N U) : Subtree g g
```

## Dependencies

- IsPositiveAffineOf.refl
- Indifferent.refl
- IVariant.refl
