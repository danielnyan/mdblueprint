---
id: interimExpectedPayment-eq-of-hasInterimPaymentFormula-of-interimAllocProb-eq
title: interimExpectedPayment_eq_of_hasInterimPaymentFormula_of_interimAllocProb_eq
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - interimExpectedPayment_eq_of_hasInterimPaymentFormula_of_interimAllocProb_eq
uses:
  - HasInterimPaymentFormula
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# interimExpectedPayment_eq_of_hasInterimPaymentFormula_of_interimAllocProb_eq

## Lean type

```lean
theorem interimExpectedPayment_eq_of_hasInterimPaymentFormula_of_interimAllocProb_eq (A B : BayesianSingleItemAuction I) (hpayA : A.HasInterimPaymentFormula) (hpayB : B.HasInterimPaymentFormula) (i : I) (hQ : ∀ z : ℝ, A.interimAllocProb i z = B.interimAllocProb i z) (hM0 : A.interimExpectedPayment i 0 = B.interimExpectedPayment i 0) (v_i : ℝ) : A.interimExpectedPayment i v_i = B.interimExpectedPayment i v_i
```

## Dependencies

- HasInterimPaymentFormula
- IsPositiveAffineOf.symm
- Indifferent.symm
