---
id: isRevenueComparable-of-myersonPaymentIdentity-of-isDSIC-of-isZeroNormalized
title: isRevenueComparable_of_myersonPaymentIdentity_of_isDSIC_of_isZeroNormalized
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - isRevenueComparable_of_myersonPaymentIdentity_of_isDSIC_of_isZeroNormalized
uses:
  - HasSameSellingEnvironment
  - IsRegularMyersonOptimalICIRAuction.isFeasible
  - IsFeasible
  - InterimFubiniAnalyticAssumptions.integrableVirtualSurplus
  - IntegrableVirtualSurplus
  - HasMyersonPaymentRevenueVirtualSurplusIdentity
  - IsDSIC
  - isDSIC
  - IsZeroNormalized
  - IsRevenueComparable
  - hasExpectedRevenueVirtualSurplusIdentity_of_myersonPaymentIdentity_of_isDSIC_of_isZeroNormalized
---

# isRevenueComparable_of_myersonPaymentIdentity_of_isDSIC_of_isZeroNormalized

## Lean type

```lean
theorem isRevenueComparable_of_myersonPaymentIdentity_of_isDSIC_of_isZeroNormalized [Fintype I] [DecidableEq I] (A B : BayesianSingleItemAuction I) (henv : A.HasSameSellingEnvironment B) (hfeas : B.IsFeasible) (hint : A.IntegrableVirtualSurplus B.allocationRule) (hmyerson : A.HasMyersonPaymentRevenueVirtualSurplusIdentity B) (hdsic : B.IsDSIC) (hzero : B.IsZeroNormalized) : A.IsRevenueComparable B
```

## Dependencies

- HasSameSellingEnvironment
- IsRegularMyersonOptimalICIRAuction.isFeasible
- IsFeasible
- InterimFubiniAnalyticAssumptions.integrableVirtualSurplus
- IntegrableVirtualSurplus
- HasMyersonPaymentRevenueVirtualSurplusIdentity
- IsDSIC
- isDSIC
- IsZeroNormalized
- IsRevenueComparable
- hasExpectedRevenueVirtualSurplusIdentity_of_myersonPaymentIdentity_of_isDSIC_of_isZeroNormalized
