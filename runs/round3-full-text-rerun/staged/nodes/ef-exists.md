---
id: ef-exists
title: ef_exists
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Divisible.Existence
  declarations:
    - ef_exists
uses:
  - Allocation
  - IsEnvyFree
  - MeasureValuation
  - IsPositiveAffineOf.symm
  - Indifferent.symm
  - Profile.ext
  - mem_iUnion
---

# ef_exists

## Lean type

```lean
theorem ef_exists {N : Type*} [Fintype N] [Nonempty N] (μ : N → Measure I) [∀ i, IsFiniteMeasure (μ i)] [∀ i, NoAtoms (μ i)] : ∃ A : Allocation N I, IsAllocation A ∧ IsEnvyFree (MeasureValuation μ) A
```

## Dependencies

- Allocation
- IsEnvyFree
- MeasureValuation
- IsPositiveAffineOf.symm
- Indifferent.symm
- Profile.ext
- mem_iUnion
