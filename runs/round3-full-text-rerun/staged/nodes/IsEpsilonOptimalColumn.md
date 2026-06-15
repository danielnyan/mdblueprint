---
id: IsEpsilonOptimalColumn
title: IsEpsilonOptimalColumn
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.MatrixGameNash
  declarations:
    - IsEpsilonOptimalColumn
uses:
---

# IsEpsilonOptimalColumn

## Lean type

```lean
def IsEpsilonOptimalColumn {𝕜 : Type} [Field 𝕜] [ConditionallyCompleteLinearOrder 𝕜] [IsStrictOrderedRing 𝕜] (A : MatrixGame I J 𝕜) (ε : 𝕜) (yy : stdSimplex 𝕜 J) : Prop
```

## Dependencies

- none
