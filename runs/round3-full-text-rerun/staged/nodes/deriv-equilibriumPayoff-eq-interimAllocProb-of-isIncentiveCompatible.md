---
id: deriv-equilibriumPayoff-eq-interimAllocProb-of-isIncentiveCompatible
title: deriv_equilibriumPayoff_eq_interimAllocProb_of_isIncentiveCompatible
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - deriv_equilibriumPayoff_eq_interimAllocProb_of_isIncentiveCompatible
uses:
  - IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
  - IsIncentiveCompatible
---

# deriv_equilibriumPayoff_eq_interimAllocProb_of_isIncentiveCompatible

## Lean type

```lean
theorem deriv_equilibriumPayoff_eq_interimAllocProb_of_isIncentiveCompatible (A : BayesianSingleItemAuction I) (hIC : A.IsIncentiveCompatible) {i : I} {v_i : ℝ} (hdiff : DifferentiableAt ℝ (A.equilibriumPayoff i) v_i) : deriv (A.equilibriumPayoff i) v_i = A.interimAllocProb i v_i
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
- IsIncentiveCompatible
