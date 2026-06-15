---
id: exAnte-revelation-principle
title: exAnte_revelation_principle
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.MechBayesian
  declarations:
    - exAnte_revelation_principle
uses:
  - StrategyProfile
  - IsExAnteBayesianNashEquilibrium
  - ExAnteRevelationPrincipleConclusion
  - DirectBayesianMechanismWithTransfers
  - truthfulStrategy
  - inducedAllocation
  - inducedPayments
  - Profile.ext
  - inducedMessages
  - directRevelation
---

# exAnte_revelation_principle

## Lean type

```lean
theorem exAnte_revelation_principle [DecidableEq I] [∀ i, MeasurableSpace (T i)] [∀ i, MeasurableSpace (M i)] (B : BayesianMechanismWithTransfers I T M A P) (u : A → (I → P) → (∀ i, T i) → I → ℝ) (σ : StrategyProfile T M) (hσ : B.IsExAnteBayesianNashEquilibrium u σ) : B.ExAnteRevelationPrincipleConclusion u σ
```

## Dependencies

- StrategyProfile
- IsExAnteBayesianNashEquilibrium
- ExAnteRevelationPrincipleConclusion
- DirectBayesianMechanismWithTransfers
- truthfulStrategy
- inducedAllocation
- inducedPayments
- Profile.ext
- inducedMessages
- directRevelation
