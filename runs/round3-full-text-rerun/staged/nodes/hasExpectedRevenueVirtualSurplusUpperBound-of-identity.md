---
id: hasExpectedRevenueVirtualSurplusUpperBound-of-identity
title: hasExpectedRevenueVirtualSurplusUpperBound_of_identity
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - hasExpectedRevenueVirtualSurplusUpperBound_of_identity
uses:
  - HasExpectedRevenueVirtualSurplusIdentity
  - HasExpectedRevenueVirtualSurplusUpperBound
---

# hasExpectedRevenueVirtualSurplusUpperBound_of_identity

## Lean type

```lean
theorem hasExpectedRevenueVirtualSurplusUpperBound_of_identity [Fintype I] (A B : BayesianSingleItemAuction I) (hB : A.HasExpectedRevenueVirtualSurplusIdentity B) : A.HasExpectedRevenueVirtualSurplusUpperBound B
```

## Dependencies

- HasExpectedRevenueVirtualSurplusIdentity
- HasExpectedRevenueVirtualSurplusUpperBound
