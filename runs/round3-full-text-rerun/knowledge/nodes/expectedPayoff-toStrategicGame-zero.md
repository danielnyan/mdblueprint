---
id: expectedPayoff-toStrategicGame-zero
title: expectedPayoff_toStrategicGame_zero
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.MatrixGameNash
  declarations:
    - expectedPayoff_toStrategicGame_zero
uses:
  - MixedProfile
  - toStrategicGame
  - expectedPayoff
  - Strategy
---

# expectedPayoff_toStrategicGame_zero

## Lean type

```lean
theorem expectedPayoff_toStrategicGame_zero {𝕜 : Type} [Field 𝕜] [LinearOrder 𝕜] [IsStrictOrderedRing 𝕜] (A : MatrixGame I J 𝕜) (p : StrategicGame.MixedProfile A.toStrategicGame) : StrategicGame.expectedPayoff A.toStrategicGame p 0 = A.E (p 0) (p 1)
```

## Dependencies

- MixedProfile
- toStrategicGame
- expectedPayoff
- Strategy
