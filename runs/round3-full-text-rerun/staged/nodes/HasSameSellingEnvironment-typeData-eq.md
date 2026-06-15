---
id: HasSameSellingEnvironment-typeData-eq
title: HasSameSellingEnvironment.typeData_eq
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - HasSameSellingEnvironment.typeData_eq
uses:
  - HasSameSellingEnvironment
---

# HasSameSellingEnvironment.typeData_eq

## Lean type

```lean
theorem HasSameSellingEnvironment.typeData_eq {A B : BayesianSingleItemAuction I} (h : A.HasSameSellingEnvironment B) : B.typeData = A.typeData
```

## Dependencies

- HasSameSellingEnvironment
