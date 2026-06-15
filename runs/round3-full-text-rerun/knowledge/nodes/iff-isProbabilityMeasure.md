---
id: iff-isProbabilityMeasure
title: iff_isProbabilityMeasure
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Divisible.Valuation
  declarations:
    - iff_isProbabilityMeasure
uses:
  - IsNormalized
  - MeasureValuation
---

# iff_isProbabilityMeasure

## Lean type

```lean
lemma iff_isProbabilityMeasure {N Ω : Type*} [MeasurableSpace Ω] (μ : N → MeasureTheory.Measure Ω) : IsNormalized (MeasureValuation μ) ↔ ∀ i, MeasureTheory.IsProbabilityMeasure (μ i)
```

## Dependencies

- IsNormalized
- MeasureValuation
