---
id: truthfulStrategy
title: truthfulStrategy
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.MechBayesian
  declarations:
    - truthfulStrategy
uses:
  - StrategyProfile
  - DirectBayesianMechanismWithTransfers
  - exAnte_revelation_principle
---

# truthfulStrategy

## Lean type

```lean
def truthfulStrategy : BayesianMechanismWithTransfers.StrategyProfile T T
```

## Dependencies

- StrategyProfile
- DirectBayesianMechanismWithTransfers
- exAnte_revelation_principle
