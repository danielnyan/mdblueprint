---
id: toCakeValuation
title: toCakeValuation
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Divisible.Instance
  declarations:
    - toCakeValuation
uses:
  - MeasureValuation
  - toCardinalInstance
---

# toCakeValuation

## Lean type

```lean
def toCakeValuation {N Ω : Type*} [MeasurableSpace Ω] (I : MeasureInstance N Ω) : CakeValuation N Ω ENNReal
```

## Dependencies

- MeasureValuation
- toCardinalInstance
