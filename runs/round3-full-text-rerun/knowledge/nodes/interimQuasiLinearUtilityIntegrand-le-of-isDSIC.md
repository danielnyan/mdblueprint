---
id: interimQuasiLinearUtilityIntegrand-le-of-isDSIC
title: interimQuasiLinearUtilityIntegrand_le_of_isDSIC
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.BayesianSingleItem
  declarations:
    - interimQuasiLinearUtilityIntegrand_le_of_isDSIC
uses:
  - IsDSIC
  - isDSIC
  - OpponentTypeProfile
  - toStrategicGame
  - IsStrictlyDominant.isWeaklyDominant
  - IsWeaklyDominant
  - WeaklyDominates
---

# interimQuasiLinearUtilityIntegrand_le_of_isDSIC

## Lean type

```lean
theorem interimQuasiLinearUtilityIntegrand_le_of_isDSIC [DecidableEq I] (A : BayesianSingleItemAuction I) (hdsic : A.IsDSIC) (i : I) (t_i z_i : ℝ) (t : OpponentTypeProfile I i) : A.interimQuasiLinearUtilityIntegrand i t_i z_i t ≤ A.interimQuasiLinearUtilityIntegrand i t_i t_i t
```

## Dependencies

- IsDSIC
- isDSIC
- OpponentTypeProfile
- toStrategicGame
- IsStrictlyDominant.isWeaklyDominant
- IsWeaklyDominant
- WeaklyDominates
