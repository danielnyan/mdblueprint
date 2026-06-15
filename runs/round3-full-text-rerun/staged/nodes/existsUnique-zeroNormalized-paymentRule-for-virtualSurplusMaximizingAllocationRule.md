---
id: existsUnique-zeroNormalized-paymentRule-for-virtualSurplusMaximizingAllocationRule
title: existsUnique_zeroNormalized_paymentRule_for_virtualSurplusMaximizingAllocationRule
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - existsUnique_zeroNormalized_paymentRule_for_virtualSurplusMaximizingAllocationRule
uses:
  - IsRegular
  - ZeroNormalized
  - IsDSIC
  - isDSIC
  - existsUnique_zeroNormalized_payment_of_isMonotone
  - virtualSurplusMaximizingAllocationRule_isMonotone_of_isRegular
---

# existsUnique_zeroNormalized_paymentRule_for_virtualSurplusMaximizingAllocationRule

## Lean type

```lean
theorem existsUnique_zeroNormalized_paymentRule_for_virtualSurplusMaximizingAllocationRule [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) (hA : A.IsRegular) : ∃! p : (I → ℝ) → I → ℝ, SingleParameterMechanism.ZeroNormalized p ∧ ({ allocationRule
```

## Dependencies

- IsRegular
- ZeroNormalized
- IsDSIC
- isDSIC
- existsUnique_zeroNormalized_payment_of_isMonotone
- virtualSurplusMaximizingAllocationRule_isMonotone_of_isRegular
