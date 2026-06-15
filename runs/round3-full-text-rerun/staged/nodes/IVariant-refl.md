---
id: IVariant-refl
title: IVariant.refl
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.ExtensiveGame.GameTreeSPE
  declarations:
    - IVariant.refl
uses:
  - Strategy
  - IVariant
---

# IVariant.refl

## Lean type

```lean
theorem IVariant.refl (i : N) (σ : Strategy N U) : IVariant i σ σ
```

## Dependencies

- Strategy
- IVariant
