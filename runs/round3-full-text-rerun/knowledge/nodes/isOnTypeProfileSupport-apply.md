---
id: isOnTypeProfileSupport-apply
title: isOnTypeProfileSupport_apply
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - isOnTypeProfileSupport_apply
uses:
  - IsOnTypeProfileSupport
  - IsOnTypeSupport
---

# isOnTypeProfileSupport_apply

## Lean type

```lean
theorem isOnTypeProfileSupport_apply (A : BayesianSingleItemAuction I) {t : I → ℝ} (ht : A.IsOnTypeProfileSupport t) (i : I) : A.IsOnTypeSupport i (t i)
```

## Dependencies

- IsOnTypeProfileSupport
- IsOnTypeSupport
