---
id: isOnTypeProfileInterior-isOnTypeProfileSupport
title: isOnTypeProfileInterior_isOnTypeProfileSupport
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - isOnTypeProfileInterior_isOnTypeProfileSupport
uses:
  - IsOnTypeProfileInterior
  - IsOnTypeProfileSupport
---

# isOnTypeProfileInterior_isOnTypeProfileSupport

## Lean type

```lean
theorem isOnTypeProfileInterior_isOnTypeProfileSupport (A : BayesianSingleItemAuction I) {t : I → ℝ} (ht : A.IsOnTypeProfileInterior t) : A.IsOnTypeProfileSupport t
```

## Dependencies

- IsOnTypeProfileInterior
- IsOnTypeProfileSupport
