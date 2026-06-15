---
id: MeasureInstance-proportional-exists
title: MeasureInstance.proportional_exists
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Divisible.Existence
  declarations:
    - MeasureInstance.proportional_exists
uses:
  - Allocation
  - IsEnvyFree.isProportional
  - IsProportional
  - proportional_exists
---

# MeasureInstance.proportional_exists

## Lean type

```lean
theorem MeasureInstance.proportional_exists {N : Type*} [Fintype N] [Nonempty N] (M : MeasureInstance N I) [∀ i, IsFiniteMeasure (M.measure i)] [∀ i, NoAtoms (M.measure i)] : ∃ A : Allocation N I, IsAllocation A ∧ M.IsProportional (Fintype.card N) A
```

## Dependencies

- Allocation
- IsEnvyFree.isProportional
- IsProportional
- proportional_exists
