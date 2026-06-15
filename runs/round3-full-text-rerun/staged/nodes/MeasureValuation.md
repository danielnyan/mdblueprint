---
id: MeasureValuation
title: MeasureValuation
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Divisible.Valuation
  declarations:
    - MeasureValuation
uses:
---

# MeasureValuation

## Lean type

```lean
def MeasureValuation {N Ω : Type*} [MeasurableSpace Ω] (μ : N → MeasureTheory.Measure Ω) : CakeValuation N Ω ENNReal
```

## Dependencies

- none
