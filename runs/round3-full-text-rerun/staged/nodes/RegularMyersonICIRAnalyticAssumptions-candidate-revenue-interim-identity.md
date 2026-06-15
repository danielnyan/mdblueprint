---
id: RegularMyersonICIRAnalyticAssumptions-candidate-revenue-interim-identity
title: RegularMyersonICIRAnalyticAssumptions.candidate_revenue_interim_identity
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - RegularMyersonICIRAnalyticAssumptions.candidate_revenue_interim_identity
uses:
  - HasSameSellingEnvironment
  - IsRegularMyersonOptimalICIRAuction.isFeasible
  - IsFeasible
  - IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
  - IsIncentiveCompatible
  - IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
  - IsIndividuallyRationalOnSupport
  - InterimFubiniAnalyticAssumptions.hasExpectedRevenueInterimPaymentIdentity
  - PaymentInterimFubiniAssumptions.hasExpectedRevenueInterimPaymentIdentity
  - HasExpectedRevenueInterimPaymentIdentity
  - RegularMyersonICIRAnalyticAssumptions.candidate_interim_fubini
---

# RegularMyersonICIRAnalyticAssumptions.candidate_revenue_interim_identity

## Lean type

```lean
theorem RegularMyersonICIRAnalyticAssumptions.candidate_revenue_interim_identity [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] {A B : BayesianSingleItemAuction I} (h : A.RegularMyersonICIRAnalyticAssumptions) (henv : A.HasSameSellingEnvironment B) (hfeas : B.IsFeasible) (hIC : B.IsIncentiveCompatible) (hIR : B.IsIndividuallyRationalOnSupport) : A.HasExpectedRevenueInterimPaymentIdentity B
```

## Dependencies

- HasSameSellingEnvironment
- IsRegularMyersonOptimalICIRAuction.isFeasible
- IsFeasible
- IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
- IsIncentiveCompatible
- IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
- IsIndividuallyRationalOnSupport
- InterimFubiniAnalyticAssumptions.hasExpectedRevenueInterimPaymentIdentity
- PaymentInterimFubiniAssumptions.hasExpectedRevenueInterimPaymentIdentity
- HasExpectedRevenueInterimPaymentIdentity
- RegularMyersonICIRAnalyticAssumptions.candidate_interim_fubini
