---
id: virtualSurplusMaximizingAuction-hasIntegrableInterimObjects-of-isRegular
title: virtualSurplusMaximizingAuction_hasIntegrableInterimObjects_of_isRegular
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingAuction_hasIntegrableInterimObjects_of_isRegular
uses:
  - IsRegular
  - HasIntegrableInterimObjects
  - virtualSurplusMaximizingAuction_hasIntegrableInterimObjects_of_aestronglyMeasurable
  - measurable_virtualValue_of_isRegular
---

# virtualSurplusMaximizingAuction_hasIntegrableInterimObjects_of_isRegular

## Lean type

```lean
theorem virtualSurplusMaximizingAuction_hasIntegrableInterimObjects_of_isRegular [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) (hA : A.IsRegular) : A.virtualSurplusMaximizingAuction.HasIntegrableInterimObjects
```

## Dependencies

- IsRegular
- HasIntegrableInterimObjects
- virtualSurplusMaximizingAuction_hasIntegrableInterimObjects_of_aestronglyMeasurable
- measurable_virtualValue_of_isRegular
