---
id: toBayesianMechanism
title: toBayesianMechanism
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.MechBayesian
  declarations:
    - toBayesianMechanism
uses:
  - StrategyProfile
  - inducedAllocation
  - inducedPayments
---

# toBayesianMechanism

## Lean type

```lean
def toBayesianMechanism (B : BayesianMechanismWithTransfers I T M A P) : BayesianMechanism I T M (A × (I → P))
```

## Dependencies

- StrategyProfile
- inducedAllocation
- inducedPayments
