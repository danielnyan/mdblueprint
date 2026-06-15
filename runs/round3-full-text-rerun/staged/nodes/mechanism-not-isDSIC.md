---
id: mechanism-not-isDSIC
title: mechanism_not_isDSIC
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.FirstPrice
  declarations:
    - mechanism_not_isDSIC
uses:
  - mechanism_isDSIC
  - IsDSIC
  - isDSIC
  - toStrategicGame
  - no_dominant_strategy
  - IsStrictlyDominant.isWeaklyDominant
  - IsWeaklyDominant
  - WeaklyDominates
---

# mechanism_not_isDSIC

## Lean type

```lean
theorem mechanism_not_isDSIC (ha : ∃ a : U, 0 < a) : ¬ mechanism.isDSIC (fun (w : I) (pay : I → U) (vals : I → U) (i : I) => if i = w then vals i - pay i else 0)
```

## Dependencies

- mechanism_isDSIC
- IsDSIC
- isDSIC
- toStrategicGame
- no_dominant_strategy
- IsStrictlyDominant.isWeaklyDominant
- IsWeaklyDominant
- WeaklyDominates
