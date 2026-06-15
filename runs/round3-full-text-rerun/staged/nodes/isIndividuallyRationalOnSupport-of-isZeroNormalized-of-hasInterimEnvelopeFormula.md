---
id: isIndividuallyRationalOnSupport-of-isZeroNormalized-of-hasInterimEnvelopeFormula
title: isIndividuallyRationalOnSupport_of_isZeroNormalized_of_hasInterimEnvelopeFormula
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - isIndividuallyRationalOnSupport_of_isZeroNormalized_of_hasInterimEnvelopeFormula
uses:
  - IsZeroNormalized
  - HasInterimEnvelopeFormula
  - HasNonnegativeInterimAllocationIntegralOnSupport
  - IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
  - IsIndividuallyRationalOnSupport
  - isIndividuallyRationalOnSupport_iff_interimExpectedPayment_zero_nonpos
  - interimExpectedPayment_zero_of_isZeroNormalized
  - IsRegular
  - bid_le_maxBid
  - eq_argmaxBid_of_strict_max
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# isIndividuallyRationalOnSupport_of_isZeroNormalized_of_hasInterimEnvelopeFormula

## Lean type

```lean
theorem isIndividuallyRationalOnSupport_of_isZeroNormalized_of_hasInterimEnvelopeFormula [DecidableEq I] (B : BayesianSingleItemAuction I) (hzero : B.IsZeroNormalized) (henv : B.HasInterimEnvelopeFormula) (hint_nonneg : B.HasNonnegativeInterimAllocationIntegralOnSupport) : B.IsIndividuallyRationalOnSupport
```

## Dependencies

- IsZeroNormalized
- HasInterimEnvelopeFormula
- HasNonnegativeInterimAllocationIntegralOnSupport
- IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
- IsIndividuallyRationalOnSupport
- isIndividuallyRationalOnSupport_iff_interimExpectedPayment_zero_nonpos
- interimExpectedPayment_zero_of_isZeroNormalized
- IsRegular
- bid_le_maxBid
- eq_argmaxBid_of_strict_max
- IsPositiveAffineOf.symm
- Indifferent.symm
