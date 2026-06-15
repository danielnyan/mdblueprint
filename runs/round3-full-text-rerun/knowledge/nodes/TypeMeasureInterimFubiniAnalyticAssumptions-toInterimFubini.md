---
id: TypeMeasureInterimFubiniAnalyticAssumptions-toInterimFubini
title: TypeMeasureInterimFubiniAnalyticAssumptions.toInterimFubini
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - TypeMeasureInterimFubiniAnalyticAssumptions.toInterimFubini
uses:
  - integral_typeMeasure_eq_intervalIntegral_mul
  - typeDensity_measurable
  - EnvelopeVirtualSurplusEnvironmentAssumptions.typeDensity_nonnegative_ae
  - RegularMyersonICIRAnalyticAssumptions.typeDensity_nonnegative_ae
---

# TypeMeasureInterimFubiniAnalyticAssumptions.toInterimFubini

## Lean type

```lean
theorem TypeMeasureInterimFubiniAnalyticAssumptions.toInterimFubini [Fintype I] {A B : BayesianSingleItemAuction I} (h : A.TypeMeasureInterimFubiniAnalyticAssumptions B) : A.InterimFubiniAnalyticAssumptions B
```

## Dependencies

- integral_typeMeasure_eq_intervalIntegral_mul
- typeDensity_measurable
- EnvelopeVirtualSurplusEnvironmentAssumptions.typeDensity_nonnegative_ae
- RegularMyersonICIRAnalyticAssumptions.typeDensity_nonnegative_ae
