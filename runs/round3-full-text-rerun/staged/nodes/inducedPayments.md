---
id: inducedPayments
title: inducedPayments
kind: theorem
status: staged
lean:
  module: EconCSLib.MechanismDesign.Auction.MechBayesian
  declarations:
    - inducedPayments
uses:
  - StrategyProfile
  - inducedMessages
---

# inducedPayments

## Lean type

```lean
def inducedPayments (B : BayesianMechanismWithTransfers I T M A P) (σ : StrategyProfile T M) (t : ∀ i, T i) : I → P
```

## Dependencies

- StrategyProfile
- inducedMessages
