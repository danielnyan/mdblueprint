---
id: ef-exists-and-proportional
title: ef_exists_and_proportional
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Divisible.Existence
  declarations:
    - ef_exists_and_proportional
uses:
  - Allocation
  - IsEnvyFree
  - MeasureValuation
  - IsEnvyFree.isProportional
  - IsProportional
  - ef_exists
---

# ef_exists_and_proportional

## Lean type

```lean
theorem ef_exists_and_proportional {N : Type*} [Fintype N] [Nonempty N] (μ : N → Measure I) [∀ i, IsFiniteMeasure (μ i)] [∀ i, NoAtoms (μ i)] : ∃ A : Allocation N I, IsAllocation A ∧ IsEnvyFree (MeasureValuation μ) A ∧ IsProportional (Fintype.card N) (MeasureValuation μ) A
```

## Dependencies

- Allocation
- IsEnvyFree
- MeasureValuation
- IsEnvyFree.isProportional
- IsProportional
- ef_exists
