---
id: optimalColumnStrategies
title: optimalColumnStrategies
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.MatrixGameNash
  declarations:
    - optimalColumnStrategies
uses:
---

# optimalColumnStrategies

## Lean type

```lean
def optimalColumnStrategies {𝕜 : Type} [Field 𝕜] [ConditionallyCompleteLinearOrder 𝕜] [IsStrictOrderedRing 𝕜] (A : MatrixGame I J 𝕜) : Set (stdSimplex 𝕜 J)
```

## Dependencies

- none
