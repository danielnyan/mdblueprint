---
id: proportional-exists
title: proportional_exists
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Divisible.Existence
  declarations:
    - proportional_exists
uses:
  - Allocation
  - IsEnvyFree.isProportional
  - IsProportional
  - MeasureValuation
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - dubinsSpanierProportional
  - Profile.ext
  - mem_iUnion
---

# proportional_exists

## Lean type

```lean
theorem proportional_exists {N : Type*} [Fintype N] [Nonempty N] (μ : N → Measure I) [∀ i, IsFiniteMeasure (μ i)] [∀ i, NoAtoms (μ i)] : ∃ A : Allocation N I, IsAllocation A ∧ IsProportional (Fintype.card N) (MeasureValuation μ) A
```

## Dependencies

- Allocation
- IsEnvyFree.isProportional
- IsProportional
- MeasureValuation
- IsPositiveAffineOf.symm
- Indifferent.symm
- dubinsSpanierProportional
- Profile.ext
- mem_iUnion
