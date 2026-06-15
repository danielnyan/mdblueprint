---
id: IsSaddlePoint
title: IsSaddlePoint
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.MatrixGameNash
  declarations:
    - IsSaddlePoint
uses:
  - IsMixedNashEq
---

# IsSaddlePoint

## Lean type

```lean
abbrev IsSaddlePoint {𝕜 : Type} [Field 𝕜] [LinearOrder 𝕜] [IsStrictOrderedRing 𝕜] (A : MatrixGame I J 𝕜) (xx : stdSimplex 𝕜 I) (yy : stdSimplex 𝕜 J) : Prop
```

## Dependencies

- IsMixedNashEq
