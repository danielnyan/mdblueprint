---
id: isMixedNashEq-iff-isSaddlePoint
title: isMixedNashEq_iff_isSaddlePoint
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.MatrixGameNash
  declarations:
    - isMixedNashEq_iff_isSaddlePoint
uses:
  - IsMixedNashEq
  - IsSaddlePoint
---

# isMixedNashEq_iff_isSaddlePoint

## Lean type

```lean
theorem isMixedNashEq_iff_isSaddlePoint {𝕜 : Type} [Field 𝕜] [LinearOrder 𝕜] [IsStrictOrderedRing 𝕜] (A : MatrixGame I J 𝕜) (xx : stdSimplex 𝕜 I) (yy : stdSimplex 𝕜 J) : A.IsMixedNashEq xx yy ↔ A.IsSaddlePoint xx yy
```

## Dependencies

- IsMixedNashEq
- IsSaddlePoint
