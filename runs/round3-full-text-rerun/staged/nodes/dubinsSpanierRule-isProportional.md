---
id: dubinsSpanierRule-isProportional
title: dubinsSpanierRule_isProportional
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Divisible.DubinsSpanier
  declarations:
    - dubinsSpanierRule_isProportional
uses:
  - IsEnvyFree.isProportional
  - IsProportional
  - dubinsSpanier_exists_proportional_allocation
---

# dubinsSpanierRule_isProportional

## Lean type

```lean
theorem dubinsSpanierRule_isProportional (n : ℕ) (hn : 0 < n) (M : MeasureInstance (Fin n) I) [∀ i, IsFiniteMeasure (M.measure i)] [∀ i, NoAtoms (M.measure i)] : M.IsProportional n (dubinsSpanierRule n hn M).1
```

## Dependencies

- IsEnvyFree.isProportional
- IsProportional
- dubinsSpanier_exists_proportional_allocation
