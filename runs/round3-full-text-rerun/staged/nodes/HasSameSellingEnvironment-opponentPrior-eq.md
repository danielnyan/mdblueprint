---
id: HasSameSellingEnvironment-opponentPrior-eq
title: HasSameSellingEnvironment.opponentPrior_eq
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - HasSameSellingEnvironment.opponentPrior_eq
uses:
  - HasSameSellingEnvironment
---

# HasSameSellingEnvironment.opponentPrior_eq

## Lean type

```lean
theorem HasSameSellingEnvironment.opponentPrior_eq {A B : BayesianSingleItemAuction I} (h : A.HasSameSellingEnvironment B) : B.opponentPrior = A.opponentPrior
```

## Dependencies

- HasSameSellingEnvironment
