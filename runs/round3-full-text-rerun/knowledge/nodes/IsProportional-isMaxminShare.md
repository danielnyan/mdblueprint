---
id: IsProportional-isMaxminShare
title: IsProportional.isMaxminShare
kind: theorem
status: staged
lean:
  module: EconCSLib.SocialChoice.FairDivision.Indivisible.Implications
  declarations:
    - IsProportional.isMaxminShare
uses:
  - Allocation
  - IsEnvyFree.isProportional
  - IsProportional
  - toValuation
  - IsMaxminShare
---

# IsProportional.isMaxminShare

## Lean type

```lean
theorem IsProportional.isMaxminShare [Fintype N] [Nonempty N] [DecidableEq G] (w : AdditiveValuation N G) {allGoods : Finset G} {A : Allocation N G} (hProp : IsProportional (Fintype.card N) w.toValuation allGoods A) : IsMaxminShare w.toValuation allGoods A
```

## Dependencies

- Allocation
- IsEnvyFree.isProportional
- IsProportional
- toValuation
- IsMaxminShare
