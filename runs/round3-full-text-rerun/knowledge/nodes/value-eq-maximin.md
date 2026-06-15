---
id: value-eq-maximin
title: value_eq_maximin
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.MatrixGameNash
  declarations:
    - value_eq_maximin
uses:
---

# value_eq_maximin

## Lean type

```lean
theorem value_eq_maximin {𝕜 : Type} [Field 𝕜] [ConditionallyCompleteLinearOrder 𝕜] [IsStrictOrderedRing 𝕜] (A : MatrixGame I J 𝕜) : A.value = A.maximin
```

## Dependencies

- none
