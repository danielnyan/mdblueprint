---
id: IsEnvyFree-isProportional-additive
title: IsEnvyFree.isProportional_additive
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.Implications
  declarations:
    - IsEnvyFree.isProportional_additive
uses:
  - Allocation
  - IsEnvyFree
  - toValuation
  - IsEnvyFree.isProportional
  - IsProportional
---

# IsEnvyFree.isProportional_additive

## Lean type

```lean
theorem IsEnvyFree.isProportional_additive [Fintype N] [DecidableEq G] (w : AdditiveValuation N G) {allGoods : Finset G} {A : Allocation N G} (hA : IsAllocation allGoods A) (hEF : IsEnvyFree w.toValuation A) : IsProportional (Fintype.card N) w.toValuation allGoods A
```

## Dependencies

- Allocation
- IsEnvyFree
- toValuation
- IsEnvyFree.isProportional
- IsProportional
