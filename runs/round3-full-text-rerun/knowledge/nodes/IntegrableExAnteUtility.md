---
id: IntegrableExAnteUtility
title: IntegrableExAnteUtility
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.MechBayesian
  declarations:
    - IntegrableExAnteUtility
uses:
  - StrategyProfile
  - inducedAllocation
  - inducedPayments
---

# IntegrableExAnteUtility

## Lean type

```lean
def IntegrableExAnteUtility (B : BayesianMechanismWithTransfers I T M A P) (u : A → (I → P) → (∀ i, T i) → I → ℝ) (σ : StrategyProfile T M) (i : I) : Prop
```

## Dependencies

- StrategyProfile
- inducedAllocation
- inducedPayments
