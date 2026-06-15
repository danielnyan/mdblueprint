---
id: equilibriumPayoff-eq-of-hasInterimEnvelopeFormula-of-interimAllocProb-eq
title: equilibriumPayoff_eq_of_hasInterimEnvelopeFormula_of_interimAllocProb_eq
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - equilibriumPayoff_eq_of_hasInterimEnvelopeFormula_of_interimAllocProb_eq
uses:
  - HasInterimEnvelopeFormula
  - IsPositiveAffineOf.symm
  - Indifferent.symm
---

# equilibriumPayoff_eq_of_hasInterimEnvelopeFormula_of_interimAllocProb_eq

## Lean type

```lean
theorem equilibriumPayoff_eq_of_hasInterimEnvelopeFormula_of_interimAllocProb_eq (A B : BayesianSingleItemAuction I) (henvA : A.HasInterimEnvelopeFormula) (henvB : B.HasInterimEnvelopeFormula) (i : I) (hQ : ∀ z : ℝ, A.interimAllocProb i z = B.interimAllocProb i z) (hM0 : A.interimExpectedPayment i 0 = B.interimExpectedPayment i 0) (v_i : ℝ) : A.equilibriumPayoff i v_i = B.equilibriumPayoff i v_i
```

## Dependencies

- HasInterimEnvelopeFormula
- IsPositiveAffineOf.symm
- Indifferent.symm
