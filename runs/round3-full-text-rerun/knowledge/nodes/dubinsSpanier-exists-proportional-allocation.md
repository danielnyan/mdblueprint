---
id: dubinsSpanier-exists-proportional-allocation
title: dubinsSpanier_exists_proportional_allocation
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Divisible.DubinsSpanier
  declarations:
    - dubinsSpanier_exists_proportional_allocation
uses:
  - Allocation
  - IsEnvyFree.isProportional
  - IsProportional
  - dubinsSpanierProportional
---

# dubinsSpanier_exists_proportional_allocation

## Lean type

```lean
theorem dubinsSpanier_exists_proportional_allocation (n : ℕ) (hn : 0 < n) (M : MeasureInstance (Fin n) I) [∀ i, IsFiniteMeasure (M.measure i)] [∀ i, NoAtoms (M.measure i)] : ∃ A : Allocation (Fin n) I, IsAllocation A ∧ M.IsProportional n A
```

## Dependencies

- Allocation
- IsEnvyFree.isProportional
- IsProportional
- dubinsSpanierProportional
