---
id: exists-mixed-nash-equilibrium
title: exists_mixed_nash_equilibrium
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.MatrixGameNash
  declarations:
    - exists_mixed_nash_equilibrium
uses:
  - IsMixedNashEq
  - isMixedNashEq_of_pure
  - toStrategicGame
  - Strategy
---

# exists_mixed_nash_equilibrium

## Lean type

```lean
theorem exists_mixed_nash_equilibrium {𝕜 : Type} [Field 𝕜] [LinearOrder 𝕜] [IsStrictOrderedRing 𝕜] (A : MatrixGame I J 𝕜) : ∃ (xx : stdSimplex 𝕜 I) (yy : stdSimplex 𝕜 J), A.IsMixedNashEq xx yy
```

## Dependencies

- IsMixedNashEq
- isMixedNashEq_of_pure
- toStrategicGame
- Strategy
