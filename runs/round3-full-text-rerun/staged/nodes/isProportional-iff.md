---
id: isProportional-iff
title: isProportional_iff
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.Checker
  declarations:
    - isProportional_iff
uses:
  - Valuation
  - Allocation
  - IsEnvyFree.isProportional
  - IsProportional
---

# isProportional_iff

## Lean type

```lean
theorem isProportional_iff [Fintype N] (n : ℕ) (v : Valuation N G) (allGoods : Finset G) (A : Allocation N G) : isProportional n v allGoods A = true ↔ IsProportional n v allGoods A
```

## Dependencies

- Valuation
- Allocation
- IsEnvyFree.isProportional
- IsProportional
