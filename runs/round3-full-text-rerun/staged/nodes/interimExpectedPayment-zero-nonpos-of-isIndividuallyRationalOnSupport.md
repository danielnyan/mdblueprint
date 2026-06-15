---
id: interimExpectedPayment-zero-nonpos-of-isIndividuallyRationalOnSupport
title: interimExpectedPayment_zero_nonpos_of_isIndividuallyRationalOnSupport
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - interimExpectedPayment_zero_nonpos_of_isIndividuallyRationalOnSupport
uses:
  - IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
  - IsIndividuallyRationalOnSupport
---

# interimExpectedPayment_zero_nonpos_of_isIndividuallyRationalOnSupport

## Lean type

```lean
theorem interimExpectedPayment_zero_nonpos_of_isIndividuallyRationalOnSupport (A : BayesianSingleItemAuction I) (hIR : A.IsIndividuallyRationalOnSupport) (i : I) : A.interimExpectedPayment i 0 ≤ 0
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
- IsIndividuallyRationalOnSupport
