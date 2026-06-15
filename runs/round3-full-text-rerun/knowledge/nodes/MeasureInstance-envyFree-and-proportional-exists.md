---
id: MeasureInstance-envyFree-and-proportional-exists
title: MeasureInstance.envyFree_and_proportional_exists
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Divisible.Existence
  declarations:
    - MeasureInstance.envyFree_and_proportional_exists
uses:
  - Allocation
  - IsEnvyFree
  - IsEnvyFree.isProportional
  - IsProportional
  - ef_exists_and_proportional
---

# MeasureInstance.envyFree_and_proportional_exists

## Lean type

```lean
theorem MeasureInstance.envyFree_and_proportional_exists {N : Type*} [Fintype N] [Nonempty N] (M : MeasureInstance N I) [∀ i, IsFiniteMeasure (M.measure i)] [∀ i, NoAtoms (M.measure i)] : ∃ A : Allocation N I, IsAllocation A ∧ M.IsEnvyFree A ∧ M.IsProportional (Fintype.card N) A
```

## Dependencies

- Allocation
- IsEnvyFree
- IsEnvyFree.isProportional
- IsProportional
- ef_exists_and_proportional
