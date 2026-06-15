---
id: toDirectBayesianMechanismWithTransfers
title: toDirectBayesianMechanismWithTransfers
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - toDirectBayesianMechanismWithTransfers
uses:
  - DirectBayesianMechanismWithTransfers
---

# toDirectBayesianMechanismWithTransfers

## Lean type

```lean
def toDirectBayesianMechanismWithTransfers (A : BayesianSingleItemAuction I) : DirectBayesianMechanismWithTransfers I (fun _ => ℝ) (I → ℝ) ℝ
```

## Dependencies

- DirectBayesianMechanismWithTransfers
