---
id: isRevenueUpperBounded-of-ic-ir-upper
title: isRevenueUpperBounded_of_ic_ir_upper
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - isRevenueUpperBounded_of_ic_ir_upper
uses:
  - IsFeasibleICIRIntegrable
  - IsRevenueUpperBounded
  - RegularMyersonICIRAnalyticAssumptions.candidate_interim_fubini
  - hasExpectedRevenueVirtualSurplusUpperBound_of_interim_identities
  - InterimFubiniAnalyticAssumptions.hasExpectedRevenueInterimPaymentIdentity
  - PaymentInterimFubiniAssumptions.hasExpectedRevenueInterimPaymentIdentity
  - HasExpectedRevenueInterimPaymentIdentity
  - InterimFubiniAnalyticAssumptions.hasExpectedVirtualSurplusInterimIdentity
  - HasExpectedVirtualSurplusInterimIdentity
  - hasInterimPaymentVirtualSurplusUpperBound_of_envelope_upper
  - RegularMyersonICIRAnalyticAssumptions.candidate_payment_envelope_upper
  - hasEnvelopeVirtualSurplusUpperBound_of_analyticAssumptions
  - RegularMyersonICIRAnalyticAssumptions.candidate_envelope_analytic
---

# isRevenueUpperBounded_of_ic_ir_upper

## Lean type

```lean
theorem isRevenueUpperBounded_of_ic_ir_upper [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A B : BayesianSingleItemAuction I) (h : A.RegularMyersonICIRAnalyticAssumptions) (hB : A.IsFeasibleICIRIntegrable B) : A.IsRevenueUpperBounded B
```

## Dependencies

- IsFeasibleICIRIntegrable
- IsRevenueUpperBounded
- RegularMyersonICIRAnalyticAssumptions.candidate_interim_fubini
- hasExpectedRevenueVirtualSurplusUpperBound_of_interim_identities
- InterimFubiniAnalyticAssumptions.hasExpectedRevenueInterimPaymentIdentity
- PaymentInterimFubiniAssumptions.hasExpectedRevenueInterimPaymentIdentity
- HasExpectedRevenueInterimPaymentIdentity
- InterimFubiniAnalyticAssumptions.hasExpectedVirtualSurplusInterimIdentity
- HasExpectedVirtualSurplusInterimIdentity
- hasInterimPaymentVirtualSurplusUpperBound_of_envelope_upper
- RegularMyersonICIRAnalyticAssumptions.candidate_payment_envelope_upper
- hasEnvelopeVirtualSurplusUpperBound_of_analyticAssumptions
- RegularMyersonICIRAnalyticAssumptions.candidate_envelope_analytic
