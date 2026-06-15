---
id: virtualSurplusMaximizingMechanism-quasiLinearUtility-eq
title: virtualSurplusMaximizingMechanism_quasiLinearUtility_eq
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.OptimalSingleItem
  declarations:
    - virtualSurplusMaximizingMechanism_quasiLinearUtility_eq
uses:
  - quasiLinearUtility
  - withMyersonPayment_quasiLinearUtility_eq
---

# virtualSurplusMaximizingMechanism_quasiLinearUtility_eq

## Lean type

```lean
theorem virtualSurplusMaximizingMechanism_quasiLinearUtility_eq [Fintype I] [Nontrivial I] [DecidableEq I] [LinearOrder I] (A : BayesianSingleItemAuction I) (v b : I → ℝ) (i : I) : (A.virtualSurplusMaximizingMechanism).quasiLinearUtility b v i = (v i - b i) * A.virtualSurplusMaximizingAllocationRule b i + ∫ z in 0..b i, A.virtualSurplusMaximizingAllocationRule (Function.update b i z) i
```

## Dependencies

- quasiLinearUtility
- withMyersonPayment_quasiLinearUtility_eq
