---
id: IsPlayerIGuarantee
title: IsPlayerIGuarantee
kind: theorem
status: staged
lean:
  module: EconCSLib.GameTheory.StrategicGame.ZeroSum.MatrixGameNash
  declarations:
    - IsPlayerIGuarantee
uses:
---

# IsPlayerIGuarantee

## Lean type

```lean
def IsPlayerIGuarantee {𝕜 : Type} [Field 𝕜] [LinearOrder 𝕜] [IsStrictOrderedRing 𝕜] (A : MatrixGame I J 𝕜) (w : 𝕜) : Prop
```

## Dependencies

- none
