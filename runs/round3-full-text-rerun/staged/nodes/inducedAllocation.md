---
id: inducedAllocation
title: inducedAllocation
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.MechBayesian
  declarations:
    - inducedAllocation
uses:
  - StrategyProfile
  - inducedMessages
---

# inducedAllocation

## Lean type

```lean
def inducedAllocation (B : BayesianMechanismWithTransfers I T M A P) (σ : StrategyProfile T M) (t : ∀ i, T i) : A
```

## Dependencies

- StrategyProfile
- inducedMessages
