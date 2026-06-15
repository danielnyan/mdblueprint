---
id: interimExpectedPayment-le-alloc-mul-sub-integral-of-isIncentiveCompatible-of-isIndividuallyRationalOnSupport
title: interimExpectedPayment_le_alloc_mul_sub_integral_of_isIncentiveCompatible_of_isIndividuallyRationalOnSupport
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - interimExpectedPayment_le_alloc_mul_sub_integral_of_isIncentiveCompatible_of_isIndividuallyRationalOnSupport
uses:
  - IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
  - IsIncentiveCompatible
  - IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
  - IsIndividuallyRationalOnSupport
  - hasInterimPaymentFormula_of_isIncentiveCompatible
  - interimExpectedPayment_zero_nonpos_of_isIndividuallyRationalOnSupport
---

# interimExpectedPayment_le_alloc_mul_sub_integral_of_isIncentiveCompatible_of_isIndividuallyRationalOnSupport

## Lean type

```lean
theorem interimExpectedPayment_le_alloc_mul_sub_integral_of_isIncentiveCompatible_of_isIndividuallyRationalOnSupport (A : BayesianSingleItemAuction I) (hIC : A.IsIncentiveCompatible) (hIR : A.IsIndividuallyRationalOnSupport) (i : I) (v_i : ℝ) : A.interimExpectedPayment i v_i ≤ A.interimAllocProb i v_i * v_i - ∫ z in 0..v_i, A.interimAllocProb i z
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
- IsIncentiveCompatible
- IsRegularMyersonOptimalICIRAuction.isIndividuallyRationalOnSupport
- IsIndividuallyRationalOnSupport
- hasInterimPaymentFormula_of_isIncentiveCompatible
- interimExpectedPayment_zero_nonpos_of_isIndividuallyRationalOnSupport
