---
id: dubinsSpanierProportional
title: dubinsSpanierProportional
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Divisible.DubinsSpanier
  declarations:
    - dubinsSpanierProportional
uses:
  - Allocation
  - IsEnvyFree.isProportional
  - IsProportional
  - MeasureValuation
---

# dubinsSpanierProportional

## Lean type

```lean
theorem dubinsSpanierProportional (n : ℕ) (hn : 0 < n) (μ : Fin n → Measure I) [∀ i, IsFiniteMeasure (μ i)] [∀ i, NoAtoms (μ i)] : ∃ A : Allocation (Fin n) I, IsAllocation A ∧ IsProportional n (MeasureValuation μ) A
```

## Dependencies

- Allocation
- IsEnvyFree.isProportional
- IsProportional
- MeasureValuation
