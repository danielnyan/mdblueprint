---
id: IsExAnteBayesianNashEquilibrium
title: IsExAnteBayesianNashEquilibrium
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.MechBayesian
  declarations:
    - IsExAnteBayesianNashEquilibrium
uses:
  - StrategyProfile
  - IsMeasurableStrategyProfile
---

# IsExAnteBayesianNashEquilibrium

## Lean type

```lean
def IsExAnteBayesianNashEquilibrium [DecidableEq I] [∀ i, MeasurableSpace (M i)] (B : BayesianMechanismWithTransfers I T M A P) (u : A → (I → P) → (∀ i, T i) → I → ℝ) (σ : StrategyProfile T M) : Prop
```

## Dependencies

- StrategyProfile
- IsMeasurableStrategyProfile
