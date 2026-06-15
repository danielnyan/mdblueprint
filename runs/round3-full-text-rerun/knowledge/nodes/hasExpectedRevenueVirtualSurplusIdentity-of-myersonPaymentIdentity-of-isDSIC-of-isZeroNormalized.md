---
id: hasExpectedRevenueVirtualSurplusIdentity-of-myersonPaymentIdentity-of-isDSIC-of-isZeroNormalized
title: hasExpectedRevenueVirtualSurplusIdentity_of_myersonPaymentIdentity_of_isDSIC_of_isZeroNormalized
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - hasExpectedRevenueVirtualSurplusIdentity_of_myersonPaymentIdentity_of_isDSIC_of_isZeroNormalized
uses:
  - HasMyersonPaymentRevenueVirtualSurplusIdentity
  - IsDSIC
  - isDSIC
  - IsZeroNormalized
  - HasExpectedRevenueVirtualSurplusIdentity
  - expectedSellerRevenueInEnvironment_eq_myersonPaymentRevenueInEnvironment_of_isDSIC_of_isZeroNormalized
---

# hasExpectedRevenueVirtualSurplusIdentity_of_myersonPaymentIdentity_of_isDSIC_of_isZeroNormalized

## Lean type

```lean
theorem hasExpectedRevenueVirtualSurplusIdentity_of_myersonPaymentIdentity_of_isDSIC_of_isZeroNormalized [Fintype I] [DecidableEq I] (A B : BayesianSingleItemAuction I) (hmyerson : A.HasMyersonPaymentRevenueVirtualSurplusIdentity B) (hdsic : B.IsDSIC) (hzero : B.IsZeroNormalized) : A.HasExpectedRevenueVirtualSurplusIdentity B
```

## Dependencies

- HasMyersonPaymentRevenueVirtualSurplusIdentity
- IsDSIC
- isDSIC
- IsZeroNormalized
- HasExpectedRevenueVirtualSurplusIdentity
- expectedSellerRevenueInEnvironment_eq_myersonPaymentRevenueInEnvironment_of_isDSIC_of_isZeroNormalized
