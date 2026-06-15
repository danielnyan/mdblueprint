---
id: MeasureInstance-envyFree-exists
title: MeasureInstance.envyFree_exists
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Divisible.Existence
  declarations:
    - MeasureInstance.envyFree_exists
uses:
  - Allocation
  - IsEnvyFree
  - ef_exists
---

# MeasureInstance.envyFree_exists

## Lean type

```lean
theorem MeasureInstance.envyFree_exists {N : Type*} [Fintype N] [Nonempty N] (M : MeasureInstance N I) [∀ i, IsFiniteMeasure (M.measure i)] [∀ i, NoAtoms (M.measure i)] : ∃ A : Allocation N I, IsAllocation A ∧ M.IsEnvyFree A
```

## Dependencies

- Allocation
- IsEnvyFree
- ef_exists
