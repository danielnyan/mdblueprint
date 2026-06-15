---
id: ExAnteRevelationPrincipleConclusion
title: ExAnteRevelationPrincipleConclusion
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.MechBayesian
  declarations:
    - ExAnteRevelationPrincipleConclusion
uses:
  - StrategyProfile
  - directRevelation
  - IsExAnteBayesianNashEquilibrium
  - DirectBayesianMechanismWithTransfers
  - truthfulStrategy
---

# ExAnteRevelationPrincipleConclusion

## Lean type

```lean
def ExAnteRevelationPrincipleConclusion [DecidableEq I] [∀ i, MeasurableSpace (T i)] [∀ i, MeasurableSpace (M i)] (B : BayesianMechanismWithTransfers I T M A P) (u : A → (I → P) → (∀ i, T i) → I → ℝ) (σ : StrategyProfile T M) : Prop
```

## Dependencies

- StrategyProfile
- directRevelation
- IsExAnteBayesianNashEquilibrium
- DirectBayesianMechanismWithTransfers
- truthfulStrategy
