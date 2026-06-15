---
id: IsMixedNashEq
title: IsMixedNashEq
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.MatrixGameNash
  declarations:
    - IsMixedNashEq
uses:
  - Strategy
  - MixedProfile
  - expectedPayoff
  - deviateMixed
---

# IsMixedNashEq

## Lean type

```lean
def IsMixedNashEq {𝕜 : Type} [Field 𝕜] [LinearOrder 𝕜] [IsStrictOrderedRing 𝕜] (A : MatrixGame I J 𝕜) (xx : stdSimplex 𝕜 I) (yy : stdSimplex 𝕜 J) : Prop
```

## Dependencies

- Strategy
- MixedProfile
- expectedPayoff
- deviateMixed
