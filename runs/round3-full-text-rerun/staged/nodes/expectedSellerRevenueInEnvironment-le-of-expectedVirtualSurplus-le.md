---
id: expectedSellerRevenueInEnvironment-le-of-expectedVirtualSurplus-le
title: expectedSellerRevenueInEnvironment_le_of_expectedVirtualSurplus_le
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - expectedSellerRevenueInEnvironment_le_of_expectedVirtualSurplus_le
uses:
  - HasExpectedRevenueVirtualSurplusIdentity
---

# expectedSellerRevenueInEnvironment_le_of_expectedVirtualSurplus_le

## Lean type

```lean
theorem expectedSellerRevenueInEnvironment_le_of_expectedVirtualSurplus_le [Fintype I] (A : BayesianSingleItemAuction I) {B C : BayesianSingleItemAuction I} (hB : A.HasExpectedRevenueVirtualSurplusIdentity B) (hC : A.HasExpectedRevenueVirtualSurplusIdentity C) (hvs : A.expectedVirtualSurplus B.allocationRule ≤ A.expectedVirtualSurplus C.allocationRule) : A.expectedSellerRevenueInEnvironment B ≤ A.expectedSellerRevenueInEnvironment C
```

## Dependencies

- HasExpectedRevenueVirtualSurplusIdentity
