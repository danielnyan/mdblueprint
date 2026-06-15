---
id: isIncentiveCompatible-iff-equilibriumPayoff-ge
title: isIncentiveCompatible_iff_equilibriumPayoff_ge
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - isIncentiveCompatible_iff_equilibriumPayoff_ge
uses:
  - IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
  - IsIncentiveCompatible
  - interimQuasiLinearUtility_eq_equilibriumPayoff_add
---

# isIncentiveCompatible_iff_equilibriumPayoff_ge

## Lean type

```lean
theorem isIncentiveCompatible_iff_equilibriumPayoff_ge (A : BayesianSingleItemAuction I) : A.IsIncentiveCompatible ↔ ∀ (i : I) (v_i x_i : ℝ), A.equilibriumPayoff i v_i ≥ A.equilibriumPayoff i x_i + A.interimAllocProb i x_i * (v_i - x_i)
```

## Dependencies

- IsRegularMyersonOptimalICIRAuction.isIncentiveCompatible
- IsIncentiveCompatible
- interimQuasiLinearUtility_eq_equilibriumPayoff_add
