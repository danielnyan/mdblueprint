---
id: isIndividuallyRationalOnSupport-iff-interimExpectedPayment-zero-nonpos
title: isIndividuallyRationalOnSupport_iff_interimExpectedPayment_zero_nonpos
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - isIndividuallyRationalOnSupport_iff_interimExpectedPayment_zero_nonpos
uses:
  - HasInterimEnvelopeFormula
  - HasNonnegativeInterimAllocationIntegralOnSupport
  - IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
  - IsIndividuallyRationalOnSupport
---

# isIndividuallyRationalOnSupport_iff_interimExpectedPayment_zero_nonpos

## Lean type

```lean
theorem isIndividuallyRationalOnSupport_iff_interimExpectedPayment_zero_nonpos (A : BayesianSingleItemAuction I) (henv : A.HasInterimEnvelopeFormula) (hint_nonneg : A.HasNonnegativeInterimAllocationIntegralOnSupport) : A.IsIndividuallyRationalOnSupport ↔ ∀ i : I, A.interimExpectedPayment i 0 ≤ 0
```

## Dependencies

- HasInterimEnvelopeFormula
- HasNonnegativeInterimAllocationIntegralOnSupport
- IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
- IsIndividuallyRationalOnSupport
