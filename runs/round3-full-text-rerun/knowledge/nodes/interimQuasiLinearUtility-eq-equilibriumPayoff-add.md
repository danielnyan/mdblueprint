---
id: interimQuasiLinearUtility-eq-equilibriumPayoff-add
title: interimQuasiLinearUtility_eq_equilibriumPayoff_add
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - interimQuasiLinearUtility_eq_equilibriumPayoff_add
uses:
---

# interimQuasiLinearUtility_eq_equilibriumPayoff_add

## Lean type

```lean
theorem interimQuasiLinearUtility_eq_equilibriumPayoff_add (A : BayesianSingleItemAuction I) (i : I) (t_i z_i : ℝ) : A.interimQuasiLinearUtility i t_i z_i = A.equilibriumPayoff i z_i + A.interimAllocProb i z_i * (t_i - z_i)
```

## Dependencies

- none
