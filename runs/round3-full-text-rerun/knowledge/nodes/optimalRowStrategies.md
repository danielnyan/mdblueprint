---
id: optimalRowStrategies
title: optimalRowStrategies
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.MatrixGameNash
  declarations:
    - optimalRowStrategies
uses:
---

# optimalRowStrategies

## Lean type

```lean
def optimalRowStrategies {𝕜 : Type} [Field 𝕜] [ConditionallyCompleteLinearOrder 𝕜] [IsStrictOrderedRing 𝕜] (A : MatrixGame I J 𝕜) : Set (stdSimplex 𝕜 I)
```

## Dependencies

- none
