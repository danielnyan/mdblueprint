---
id: IsOnTypeProfileSupport
title: IsOnTypeProfileSupport
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - IsOnTypeProfileSupport
uses:
  - IsOnTypeSupport
---

# IsOnTypeProfileSupport

## Lean type

```lean
def IsOnTypeProfileSupport (A : BayesianSingleItemAuction I) (t : I → ℝ) : Prop
```

## Dependencies

- IsOnTypeSupport
