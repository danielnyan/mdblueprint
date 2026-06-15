---
id: isOnTypeSupport-left
title: isOnTypeSupport_left
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - isOnTypeSupport_left
uses:
  - IsOnTypeSupport
---

# isOnTypeSupport_left

## Lean type

```lean
theorem isOnTypeSupport_left (A : BayesianSingleItemAuction I) {i : I} {v : ℝ} (hv : A.IsOnTypeSupport i v) : 0 ≤ v
```

## Dependencies

- IsOnTypeSupport
