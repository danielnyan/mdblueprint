---
id: HasSameSellingEnvironment-prior-eq
title: HasSameSellingEnvironment.prior_eq
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - HasSameSellingEnvironment.prior_eq
uses:
  - HasSameSellingEnvironment
---

# HasSameSellingEnvironment.prior_eq

## Lean type

```lean
theorem HasSameSellingEnvironment.prior_eq {A B : BayesianSingleItemAuction I} (h : A.HasSameSellingEnvironment B) : B.prior = A.prior
```

## Dependencies

- HasSameSellingEnvironment
