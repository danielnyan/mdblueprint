---
id: hasExpectedRevenueVirtualSurplusIdentity-of-interim-identities
title: hasExpectedRevenueVirtualSurplusIdentity_of_interim_identities
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - hasExpectedRevenueVirtualSurplusIdentity_of_interim_identities
uses:
  - InterimFubiniAnalyticAssumptions.hasExpectedRevenueInterimPaymentIdentity
  - PaymentInterimFubiniAssumptions.hasExpectedRevenueInterimPaymentIdentity
  - HasExpectedRevenueInterimPaymentIdentity
  - InterimFubiniAnalyticAssumptions.hasExpectedVirtualSurplusInterimIdentity
  - HasExpectedVirtualSurplusInterimIdentity
  - HasExpectedRevenueVirtualSurplusIdentity
---

# hasExpectedRevenueVirtualSurplusIdentity_of_interim_identities

## Lean type

```lean
theorem hasExpectedRevenueVirtualSurplusIdentity_of_interim_identities [Fintype I] (A B : BayesianSingleItemAuction I) (hrev : A.HasExpectedRevenueInterimPaymentIdentity B) (hvs : A.HasExpectedVirtualSurplusInterimIdentity B) (hid : ∀ i : I, (∫ v in 0..A.typeData.omega i, B.interimExpectedPayment i v * A.typeDensity i v) = ∫ v in 0..A.typeData.omega i, B.interimAllocProb i v * A.virtualValue i v * A.typeDensity i v) : A.HasExpectedRevenueVirtualSurplusIdentity B
```

## Dependencies

- InterimFubiniAnalyticAssumptions.hasExpectedRevenueInterimPaymentIdentity
- PaymentInterimFubiniAssumptions.hasExpectedRevenueInterimPaymentIdentity
- HasExpectedRevenueInterimPaymentIdentity
- InterimFubiniAnalyticAssumptions.hasExpectedVirtualSurplusInterimIdentity
- HasExpectedVirtualSurplusInterimIdentity
- HasExpectedRevenueVirtualSurplusIdentity
