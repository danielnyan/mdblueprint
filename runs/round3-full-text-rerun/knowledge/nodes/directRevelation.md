---
id: directRevelation
title: directRevelation
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.MechBayesian
  declarations:
    - directRevelation
uses:
  - StrategyProfile
  - DirectBayesianMechanismWithTransfers
  - inducedAllocation
  - inducedPayments
---

# directRevelation

## Lean type

```lean
def directRevelation (B : BayesianMechanismWithTransfers I T M A P) (σ : StrategyProfile T M) : DirectBayesianMechanismWithTransfers I T A P
```

## Dependencies

- StrategyProfile
- DirectBayesianMechanismWithTransfers
- inducedAllocation
- inducedPayments
