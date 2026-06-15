---
id: interimExpectedPayment-eq-and-equilibriumPayoff-eq-of-hasInterimEnvelopeFormula
title: interimExpectedPayment_eq_and_equilibriumPayoff_eq_of_hasInterimEnvelopeFormula
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - interimExpectedPayment_eq_and_equilibriumPayoff_eq_of_hasInterimEnvelopeFormula
uses:
  - HasInterimEnvelopeFormula
  - interimExpectedPayment_eq_of_hasInterimPaymentFormula_of_interimAllocProb_eq
  - hasInterimPaymentFormula_of_hasInterimEnvelopeFormula
  - equilibriumPayoff_eq_of_hasInterimEnvelopeFormula_of_interimAllocProb_eq
---

# interimExpectedPayment_eq_and_equilibriumPayoff_eq_of_hasInterimEnvelopeFormula

## Lean type

```lean
theorem interimExpectedPayment_eq_and_equilibriumPayoff_eq_of_hasInterimEnvelopeFormula (A B : BayesianSingleItemAuction I) (henvA : A.HasInterimEnvelopeFormula) (henvB : B.HasInterimEnvelopeFormula) (i : I) (hQ : ∀ z : ℝ, A.interimAllocProb i z = B.interimAllocProb i z) (hM0 : A.interimExpectedPayment i 0 = B.interimExpectedPayment i 0) (v_i : ℝ) : A.interimExpectedPayment i v_i = B.interimExpectedPayment i v_i ∧ A.equilibriumPayoff i v_i = B.equilibriumPayoff i v_i
```

## Dependencies

- HasInterimEnvelopeFormula
- interimExpectedPayment_eq_of_hasInterimPaymentFormula_of_interimAllocProb_eq
- hasInterimPaymentFormula_of_hasInterimEnvelopeFormula
- equilibriumPayoff_eq_of_hasInterimEnvelopeFormula_of_interimAllocProb_eq
