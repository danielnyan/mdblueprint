---
id: hasExpectedRevenueVirtualSurplusUpperBound-of-interim-identities
title: hasExpectedRevenueVirtualSurplusUpperBound_of_interim_identities
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - hasExpectedRevenueVirtualSurplusUpperBound_of_interim_identities
uses:
  - InterimFubiniAnalyticAssumptions.hasExpectedRevenueInterimPaymentIdentity
  - PaymentInterimFubiniAssumptions.hasExpectedRevenueInterimPaymentIdentity
  - HasExpectedRevenueInterimPaymentIdentity
  - InterimFubiniAnalyticAssumptions.hasExpectedVirtualSurplusInterimIdentity
  - HasExpectedVirtualSurplusInterimIdentity
  - HasInterimPaymentVirtualSurplusUpperBound
  - HasExpectedRevenueVirtualSurplusUpperBound
---

# hasExpectedRevenueVirtualSurplusUpperBound_of_interim_identities

## Lean type

```lean
theorem hasExpectedRevenueVirtualSurplusUpperBound_of_interim_identities [Fintype I] (A B : BayesianSingleItemAuction I) (hrev : A.HasExpectedRevenueInterimPaymentIdentity B) (hvs : A.HasExpectedVirtualSurplusInterimIdentity B) (hupper : A.HasInterimPaymentVirtualSurplusUpperBound B) : A.HasExpectedRevenueVirtualSurplusUpperBound B
```

## Dependencies

- InterimFubiniAnalyticAssumptions.hasExpectedRevenueInterimPaymentIdentity
- PaymentInterimFubiniAssumptions.hasExpectedRevenueInterimPaymentIdentity
- HasExpectedRevenueInterimPaymentIdentity
- InterimFubiniAnalyticAssumptions.hasExpectedVirtualSurplusInterimIdentity
- HasExpectedVirtualSurplusInterimIdentity
- HasInterimPaymentVirtualSurplusUpperBound
- HasExpectedRevenueVirtualSurplusUpperBound
