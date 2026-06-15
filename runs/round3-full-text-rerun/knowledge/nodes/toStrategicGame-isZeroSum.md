---
id: toStrategicGame-isZeroSum
title: toStrategicGame_isZeroSum
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.MatrixGameNash
  declarations:
    - toStrategicGame_isZeroSum
uses:
  - IsZeroSum
  - toStrategicGame
  - Strategy
  - MixedProfile
---

# toStrategicGame_isZeroSum

## Lean type

```lean
theorem toStrategicGame_isZeroSum {𝕜 : Type} [Field 𝕜] [LinearOrder 𝕜] [IsStrictOrderedRing 𝕜] (A : MatrixGame I J 𝕜) : StrategicGame.IsZeroSum A.toStrategicGame
```

## Dependencies

- IsZeroSum
- toStrategicGame
- Strategy
- MixedProfile
