---
id: InterimFubiniAnalyticAssumptions-hasExpectedVirtualSurplusInterimIdentity
title: InterimFubiniAnalyticAssumptions.hasExpectedVirtualSurplusInterimIdentity
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - InterimFubiniAnalyticAssumptions.hasExpectedVirtualSurplusInterimIdentity
uses:
  - HasExpectedVirtualSurplusInterimIdentity
  - typeDensity_measurable
  - EnvelopeVirtualSurplusEnvironmentAssumptions.typeDensity_nonnegative_ae
  - RegularMyersonICIRAnalyticAssumptions.typeDensity_nonnegative_ae
---

# InterimFubiniAnalyticAssumptions.hasExpectedVirtualSurplusInterimIdentity

## Lean type

```lean
theorem InterimFubiniAnalyticAssumptions.hasExpectedVirtualSurplusInterimIdentity [Fintype I] {A B : BayesianSingleItemAuction I} (h : A.InterimFubiniAnalyticAssumptions B) : A.HasExpectedVirtualSurplusInterimIdentity B
```

## Dependencies

- HasExpectedVirtualSurplusInterimIdentity
- typeDensity_measurable
- EnvelopeVirtualSurplusEnvironmentAssumptions.typeDensity_nonnegative_ae
- RegularMyersonICIRAnalyticAssumptions.typeDensity_nonnegative_ae
