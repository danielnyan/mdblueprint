---
id: isOnTypeSupport-right
title: isOnTypeSupport_right
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - isOnTypeSupport_right
uses:
  - IsOnTypeSupport
---

# isOnTypeSupport_right

## Lean type

```lean
theorem isOnTypeSupport_right (A : BayesianSingleItemAuction I) {i : I} {v : ℝ} (hv : A.IsOnTypeSupport i v) : v ≤ A.typeData.omega i
```

## Dependencies

- IsOnTypeSupport
