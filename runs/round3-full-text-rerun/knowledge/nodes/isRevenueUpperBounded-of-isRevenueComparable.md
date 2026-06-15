---
id: isRevenueUpperBounded-of-isRevenueComparable
title: isRevenueUpperBounded_of_isRevenueComparable
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - isRevenueUpperBounded_of_isRevenueComparable
uses:
  - IsRevenueComparable
  - IsRevenueUpperBounded
  - hasExpectedRevenueVirtualSurplusUpperBound_of_identity
---

# isRevenueUpperBounded_of_isRevenueComparable

## Lean type

```lean
theorem isRevenueUpperBounded_of_isRevenueComparable [Fintype I] (A B : BayesianSingleItemAuction I) (hB : A.IsRevenueComparable B) : A.IsRevenueUpperBounded B
```

## Dependencies

- IsRevenueComparable
- IsRevenueUpperBounded
- hasExpectedRevenueVirtualSurplusUpperBound_of_identity
