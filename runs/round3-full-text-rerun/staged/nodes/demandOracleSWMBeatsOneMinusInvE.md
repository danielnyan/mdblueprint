---
id: demandOracleSWMBeatsOneMinusInvE
title: demandOracleSWMBeatsOneMinusInvE
kind: theorem
status: staged
lean:
  module: EconCSLib.OpenProblem.SubmodularWelfareDemandOracle
  declarations:
    - demandOracleSWMBeatsOneMinusInvE
uses:
  - BundlePartitionAllocation
---

# demandOracleSWMBeatsOneMinusInvE

## Lean type

```lean
theorem demandOracleSWMBeatsOneMinusInvE (I Ω : Type*) {G : Type*} [Fintype I] [Fintype Ω] [DecidableEq G] (M : Finset G) [Fintype (BundlePartitionAllocation I M)] [Nonempty (BundlePartitionAllocation I M)] : answer(sorry) ↔ DemandOracleSWMBeatsOneMinusInvEStatement I Ω M
```

## Dependencies

- BundlePartitionAllocation
