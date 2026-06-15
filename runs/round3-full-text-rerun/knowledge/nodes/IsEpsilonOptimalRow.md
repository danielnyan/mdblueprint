---
id: IsEpsilonOptimalRow
title: IsEpsilonOptimalRow
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.MatrixGameNash
  declarations:
    - IsEpsilonOptimalRow
uses:
---

# IsEpsilonOptimalRow

## Lean type

```lean
def IsEpsilonOptimalRow {𝕜 : Type} [Field 𝕜] [ConditionallyCompleteLinearOrder 𝕜] [IsStrictOrderedRing 𝕜] (A : MatrixGame I J 𝕜) (ε : 𝕜) (xx : stdSimplex 𝕜 I) : Prop
```

## Dependencies

- none
