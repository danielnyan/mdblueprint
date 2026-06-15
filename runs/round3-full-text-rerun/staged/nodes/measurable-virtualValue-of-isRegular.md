---
id: measurable-virtualValue-of-isRegular
title: measurable_virtualValue_of_isRegular
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - measurable_virtualValue_of_isRegular
uses:
  - IsRegular
---

# measurable_virtualValue_of_isRegular

## Lean type

```lean
theorem measurable_virtualValue_of_isRegular (A : BayesianSingleItemAuction I) (hA : A.IsRegular) (i : I) : Measurable (A.virtualValue i)
```

## Dependencies

- IsRegular
